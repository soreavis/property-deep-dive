#!/usr/bin/env python3
"""Source-content verifier harness for property-deep-dive.

The deterministic half of the source-content verifier (the LLM half is a Workflow —
see skills/property-deep-dive/shared/source-verifier.md). This script:

  * EXTRACTS verifiable claim↔citation pairs from the corpus — a markdown link to a
    PRIMARY source (gov-suffix or scripts/primary-source-allowlist.txt) whose surrounding
    sentence carries >=1 SALIENT value token (percentage / money / statute / specific date;
    a bare year does not count). Roster/navigation links carrying no number are filtered out.
  * SCORES + SAMPLES claims fetch-free (stale-marker > never-verified > oldest-stamp) so the
    expensive LLM layer sees a cost-bounded worklist, and the network touches only the sample.
  * FETCHES each cited page using url-liveness.py's polite-fetch primitives (robots.txt,
    per-host throttle, global rate cap, gov-suffix floor, EUR-Lex crawl-delay, Cloudflare
    detection, excluded hosts) — politeness config is read from config/_url-liveness.json,
    NOT redefined here. Reads the FULL body (url-liveness reads only a 4KB title slice),
    cleans HTML→text, caches with a content hash + TTL.
  * Runs a TOKEN-PRESENCE pre-filter: if NONE of a claim's salient value tokens appear
    anywhere on the cited page → TOKENS_ABSENT (a cheap, deterministic bug-catch — the
    claimed figure is literally not on the page it cites). Otherwise emits windowed excerpts
    around the hits for the LLM layer.
  * WRITES a worklist JSON (the LLM layer's input) + an extract JSON (every claim) + stats.

It NEVER edits a playbook, NEVER re-stamps `Last verified`, and NEVER emits a verdict on its
own — internal-consistency tooling cannot establish external accuracy. It produces evidence
for human + LLM review only. See CLAUDE.md § anti-hallucination contract.

Usage:
    python3 scripts/source-verify.py --extract                      # parse claims, no network; print stats
    python3 scripts/source-verify.py --extract --json OUT.json      # dump every extracted claim
    python3 scripts/source-verify.py --extract --country=fr         # one country (or shared/<stem>)
    python3 scripts/source-verify.py --build-worklist               # fetch the sampled claims, emit worklist
    python3 scripts/source-verify.py --build-worklist --sample=40 --country=fr
    python3 scripts/source-verify.py --build-worklist --include-secondary --section=Tax
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import importlib.util
import io
import json
import logging
import os
import random
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import urlparse

try:
    import aiohttp
except ImportError:
    sys.stderr.write("aiohttp not installed. Run: pip install aiohttp\n")
    sys.exit(2)

# PDF text extraction: prefer pdftotext (poppler — preserves columns in fee/rate-schedule
# tables, common in tax sources), fall back to pypdf (pure-python, no system dep). Both are
# optional; if neither is present a PDF degrades to status BINARY rather than crashing.
_HAS_PDFTOTEXT = shutil.which("pdftotext") is not None
try:
    import pypdf
    _HAS_PYPDF = True
    # pypdf logs broken-PDF recovery chatter ("incorrect startxref pointer", "EOF marker not
    # found", …) at WARNING when it falls back on a malformed file — silence it; pdf_to_text
    # already handles the failure by returning empty.
    logging.getLogger("pypdf").setLevel(logging.ERROR)
except Exception:
    _HAS_PYPDF = False

ROOT = Path(__file__).resolve().parent.parent
SV_CONFIG_PATH = ROOT / "config" / "_source-verify.json"
ALLOWLIST_PATH = ROOT / "scripts" / "primary-source-allowlist.txt"
OUT_DIR = ROOT / "_local" / "source-verify"
CONTENT_CACHE_DIR = OUT_DIR / "content-cache"

# Reuse url-liveness.py's polite-fetch primitives (file has a hyphen → import by spec).
_ul_spec = importlib.util.spec_from_file_location("url_liveness", str(ROOT / "scripts" / "url-liveness.py"))
url_liveness = importlib.util.module_from_spec(_ul_spec)
sys.modules["url_liveness"] = url_liveness
_ul_spec.loader.exec_module(url_liveness)
UL = url_liveness

MD_LINK_RE = re.compile(r"\[(?P<text>[^\]]+)\]\((?P<url>https?://[^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$")
# Inline stamp: "(2026-05-27 verified; source …)" or "(2026-05-27 stale-marker)". The keyword
# is followed by ";" in the verified form and ")" in the marker form — match either, so don't
# anchor on a trailing ")".
STAMP_RE = re.compile(r"\((\d{4}-\d{2}-\d{2})\s+(re-verified|verified|stale-marker|stale|updated)\b", re.IGNORECASE)

# ── Value extraction ─────────────────────────────────────────────────────────
PCT_RE = re.compile(r"(?<![\w.])\d{1,3}(?:[.,]\d+)?\s?(?:%|pp\b|percentage points)")
MONEY_SYMBOL_RE = re.compile(
    r"[€£$¥₹](?:\s?\d[\d.,]*)(?:\s?(?:k|m|bn|million|billion))?", re.IGNORECASE
)
_CCY = r"USD|EUR|GBP|CHF|AED|SAR|JPY|CNY|HKD|SGD|AUD|NZD|CAD|ZAR|INR|BRL|MXN|TRY|PLN|CZK|HUF|RON|SEK|NOK|DKK|ILS|KRW|THB|IDR|MYR|PHP|VND|BHD|KWD|QAR|OMR|MUR|XCD|KYD|BMD"
MONEY_CODE_RE = re.compile(
    rf"(?:(?:{_CCY})\s?\d[\d.,]*(?:\s?(?:k|m|bn|million|billion))?"
    rf"|\d[\d.,]*\s?(?:k|m|bn)?\s?(?:{_CCY}))",
    re.IGNORECASE,
)
ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_MONTHS = r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t|tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?"
DMY_RE = re.compile(rf"\b\d{{1,2}}\s(?:{_MONTHS})\.?\s\d{{4}}\b")
MY_RE = re.compile(rf"\b(?:{_MONTHS})\.?\s\d{{4}}\b")
YEAR_RE = re.compile(r"(?<!\d)(?:19|20)\d{2}(?!\d)")
STATUTE_RE = re.compile(
    r"(?:Loi|Law|Ley|Legge|Lei|Gesetz|Decreto|D[ée]cret|Decree|Regulation|Reg\.|Act|Cap\.?|Article|Art\.|§|No\.?|n°|nr\.?|Bekendtg[øo]relse|Verordnung)"
    r"\s?(?:[A-Z]{0,4}[-\s])?\d[\w./()-]*",
    re.IGNORECASE,
)
_MONTH_ABBR = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
    "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}
_MONTH_FULL = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April", "may": "May",
    "jun": "June", "jul": "July", "aug": "August", "sep": "September", "oct": "October",
    "nov": "November", "dec": "December",
}


@dataclass
class Value:
    type: str          # pct | money | statute | date | year
    raw: str
    norm: str
    needles: list[str] = field(default_factory=list)
    salient: bool = True


def _thousands_stripped(d: str) -> str | None:
    """If d is a thousands-grouped number ('300,000', '1.234.567', '77,700') return the
    separator-free form ('300000'). Returns None for decimals ('6.32', '1.3') — a group of
    !=3 digits after the first separator means it's a decimal, not a thousands separator."""
    parts = re.split(r"[.,]", d)
    if len(parts) >= 2 and parts[0] and all(len(p) == 3 for p in parts[1:]):
        return "".join(parts)
    return None


def _num_needles(raw: str) -> list[str]:
    """Pull the bare numeric core(s) of a token as search needles. Includes both decimal
    separators AND the separator-free form for thousands-grouped numbers, so a claimed
    '300,000' still matches a page rendering '300000' or 'CI$300,000'."""
    digits = re.findall(r"\d[\d.,]*\d|\d", raw)
    out: set[str] = set()
    for d in digits:
        d = d.strip(".,")
        if not d:
            continue
        out.add(d)
        if "," in d:
            out.add(d.replace(",", "."))
        if "." in d:
            out.add(d.replace(".", ","))
        bare = _thousands_stripped(d)
        if bare:
            out.add(bare)
    return sorted(out, key=len, reverse=True)


def _date_needles(raw: str) -> list[str]:
    needles: set[str] = set()
    iso = ISO_DATE_RE.search(raw)
    if iso:
        needles.add(iso.group(0))
        needles.add(iso.group(0)[:4])
    ym = re.search(rf"(?P<mon>{_MONTHS})\.?\s(?P<yr>\d{{4}})", raw, re.IGNORECASE)
    if ym:
        mon = ym.group("mon")[:3].lower()
        needles.add(ym.group("yr"))
        needles.add(mon.capitalize())          # abbreviated form ("Apr")
        if mon in _MONTH_FULL:
            needles.add(_MONTH_FULL[mon])       # full form ("April") — match pages that spell it out
        if mon in _MONTH_ABBR:
            needles.add(f"{ym.group('yr')}-{_MONTH_ABBR[mon]}")
    yr = YEAR_RE.search(raw)
    if yr:
        needles.add(yr.group(0))
    return sorted(needles)


def extract_values(text: str) -> list[Value]:
    """Extract value tokens from a claim sentence. Earlier/more-specific types win an offset
    so we don't double-count (a money token's digits also look like a bare year)."""
    claimed: list[tuple[int, int]] = []

    def free(s: int, e: int) -> bool:
        return not any(s < ce and cs < e for cs, ce in claimed)

    out: list[Value] = []

    def collect(regex, vtype, salient, needle_fn):
        for m in regex.finditer(text):
            s, e = m.span()
            if not free(s, e):
                continue
            claimed.append((s, e))
            raw = m.group(0).strip()
            needles = needle_fn(raw)
            if not needles:
                continue
            out.append(Value(type=vtype, raw=raw, norm=raw, needles=needles, salient=salient))

    # Order matters: most specific first so their spans get reserved. Dates run BEFORE statutes
    # because STATUTE_RE is IGNORECASE and would otherwise read "Nov 2024" as "No." + "v 2024".
    collect(MONEY_SYMBOL_RE, "money", True, _num_needles)
    collect(MONEY_CODE_RE, "money", True, _num_needles)
    collect(PCT_RE, "pct", True, _num_needles)
    collect(ISO_DATE_RE, "date", True, _date_needles)
    collect(DMY_RE, "date", True, _date_needles)
    collect(MY_RE, "date", True, _date_needles)
    collect(STATUTE_RE, "statute", True, lambda r: _num_needles(r))
    collect(YEAR_RE, "year", False, _date_needles)
    return out


# ── Primary-source gating ────────────────────────────────────────────────────
def load_allowlist() -> set[str]:
    hosts: set[str] = set()
    if not ALLOWLIST_PATH.exists():
        return hosts
    for line in ALLOWLIST_PATH.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            hosts.add(line.lower())
    return hosts


def source_tier(host: str, allowlist: set[str]) -> str | None:
    host = host.lower()
    if UL._is_gov_suffix(host):
        return "primary-gov"
    h = host[4:] if host.startswith("www.") else host
    if host in allowlist or h in allowlist:
        return "primary-allowlist"
    return None  # secondary / listing / forum


# ── SV config ────────────────────────────────────────────────────────────────
@dataclass
class SVConfig:
    raw: dict

    @property
    def primary_only(self) -> bool:
        return self.raw["extraction"]["primary_only"]

    @property
    def min_salient(self) -> int:
        return self.raw["extraction"]["min_salient_values"]

    @property
    def claim_window(self) -> int:
        return self.raw["extraction"]["claim_window_chars"]

    @property
    def skip_files(self) -> set[str]:
        return set(self.raw["extraction"]["skip_files"])

    @property
    def skip_headings(self) -> list[str]:
        return [h.lower() for h in self.raw["extraction"]["skip_headings"]]

    @property
    def scope_dirs(self) -> list[Path]:
        return [ROOT / d for d in self.raw["extraction"]["scope_dirs"]]

    @property
    def max_body_bytes(self) -> int:
        return self.raw["fetch"]["max_body_bytes"]

    @property
    def excerpt_window(self) -> int:
        return self.raw["fetch"]["excerpt_window_chars"]

    @property
    def max_excerpts(self) -> int:
        return self.raw["fetch"]["max_excerpts_per_claim"]

    @property
    def min_text_chars(self) -> int:
        return self.raw["fetch"].get("min_text_chars", 200)

    @property
    def js_spa_hosts(self) -> list[str]:
        return [h.lower() for h in self.raw["fetch"].get("js_spa_hosts", [])]

    @property
    def content_ttl_days(self) -> int:
        return self.raw["fetch"]["content_cache_ttl_days"]

    @property
    def binary_prefixes(self) -> list[str]:
        return self.raw["fetch"]["binary_content_prefixes"]

    @property
    def pdf_enabled(self) -> bool:
        return self.raw.get("pdf", {}).get("enabled", True)

    @property
    def pdf_max_pages(self) -> int:
        return self.raw.get("pdf", {}).get("max_pages", 0)

    @property
    def pdf_max_bytes(self) -> int:
        return self.raw.get("pdf", {}).get("max_bytes", 12_000_000)

    @property
    def default_sample(self) -> int:
        return self.raw["sampling"]["default_sample"]

    @property
    def priority_weights(self) -> dict:
        return self.raw["sampling"]["priority_weights"]


def load_sv_config() -> SVConfig:
    return SVConfig(raw=json.loads(SV_CONFIG_PATH.read_text(encoding="utf-8")))


# ── Claim extraction ─────────────────────────────────────────────────────────
@dataclass
class ClaimRecord:
    id: str
    scope: str            # iso2 for a country playbook, else "shared/<stem>"
    section: str
    line_no: int
    claim_text: str
    values: list[dict]
    source_url: str
    source_host: str
    source_tier: str
    inline_stamp: dict | None = None


def _scope_for(path: Path) -> str:
    parts = path.parts
    if "countries" in parts:
        i = parts.index("countries")
        if i + 1 < len(parts):
            return parts[i + 1]
    return f"shared/{path.stem}"


def _claim_sentence(line: str, link_start: int, window: int) -> str:
    """Return the line, or a window around the link if the line is long."""
    lead = len(line) - len(line.lstrip())
    line = line.strip()
    link_start = max(0, link_start - lead)
    if len(line) <= window:
        return line
    lo = max(0, link_start - window // 2)
    hi = min(len(line), link_start + window // 2)
    return ("…" if lo > 0 else "") + line[lo:hi].strip() + ("…" if hi < len(line) else "")


def iter_md_files(scope_dirs: list[Path], skip_files: set[str]):
    for d in scope_dirs:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            if path.name in skip_files:
                continue
            if any(p in UL.EXCLUDE_DIRS for p in path.parts):
                continue
            yield path


def extract_claims(
    sv: SVConfig,
    allowlist: set[str],
    primary_only: bool,
    only_scope: str | None = None,
    only_section: str | None = None,
) -> list[ClaimRecord]:
    claims: list[ClaimRecord] = []
    seen_ids: set[str] = set()   # collapse a line that links the same primary URL twice → identical id
    for path in iter_md_files(sv.scope_dirs, sv.skip_files):
        scope = _scope_for(path)
        if only_scope and scope != only_scope and not scope.endswith(f"/{only_scope}"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        section = ""
        for line_no, line in enumerate(text.splitlines(), 1):
            hm = HEADING_RE.match(line)
            if hm:
                section = hm.group(2).strip()
                continue
            if "](http" not in line:
                continue
            if any(sk in section.lower() for sk in sv.skip_headings):
                continue
            if only_section and only_section.lower() not in section.lower():
                continue
            values = extract_values(line)
            salient = [v for v in values if v.salient]
            if len(salient) < sv.min_salient:
                continue
            stamp = None
            sm = STAMP_RE.search(line)
            if sm:
                stamp = {"date": sm.group(1), "kind": sm.group(2).lower().replace("re-verified", "verified")}
            for lm in MD_LINK_RE.finditer(line):
                url = lm.group("url").rstrip(".,;:)")
                host = urlparse(url).netloc
                tier = source_tier(host, allowlist)
                if primary_only and tier is None:
                    continue
                claim_text = _claim_sentence(line, lm.start(), sv.claim_window)
                cid = f"{scope}:{line_no}:{hashlib.sha1(url.encode()).hexdigest()[:8]}"
                if cid in seen_ids:
                    continue
                seen_ids.add(cid)
                claims.append(ClaimRecord(
                    id=cid, scope=scope, section=section or "(none)", line_no=line_no,
                    claim_text=claim_text,
                    values=[asdict(v) for v in values],
                    source_url=url, source_host=host.lower(),
                    source_tier=tier or "secondary",
                    inline_stamp=stamp,
                ))
    return claims


# ── Fetch-free sample selection ──────────────────────────────────────────────
def _stamp_age_days(stamp: dict | None) -> int:
    if not stamp:
        return 9999
    try:
        d = datetime.strptime(stamp["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return max(0, (datetime.now(timezone.utc) - d).days)
    except Exception:
        return 9999


def selection_score(c: ClaimRecord, w: dict, rng: random.Random) -> float:
    s = 0.0
    if c.inline_stamp and c.inline_stamp.get("kind", "").startswith("stale"):
        s += w.get("stale_marker", 100)
    if not c.inline_stamp:
        s += w.get("never_verified", 50)
    else:
        s += (_stamp_age_days(c.inline_stamp) / 30.0) * w.get("stamp_age_per_30d", 8)
    if any(v["type"] in ("statute", "money") for v in c.values):
        s += w.get("salient_statute_or_money", 10)
    s += rng.random()  # deterministic tie-break (seeded)
    return s


def select_sample(claims: list[ClaimRecord], n: int, weights: dict, seed: int = 1234) -> list[ClaimRecord]:
    rng = random.Random(seed)
    ranked = sorted(claims, key=lambda c: selection_score(c, weights, rng), reverse=True)
    return ranked[:n]


# ── HTML→text ────────────────────────────────────────────────────────────────
_DROP_BLOCK_RE = re.compile(r"(?is)<(script|style|noscript|svg|head|template)[^>]*>.*?</\1>")
_COMMENT_RE = re.compile(r"(?is)<!--.*?-->")
_BR_RE = re.compile(r"(?is)<br\s*/?>")
_BLOCK_END_RE = re.compile(r"(?is)</(p|div|li|tr|h[1-6]|section|article|td|th)>")
_TAG_RE = re.compile(r"(?s)<[^>]+>")
_WS_RE = re.compile(r"[ \t ]+")
_NL_RE = re.compile(r"\n\s*\n\s*\n+")


def html_to_text(html: str) -> str:
    html = _DROP_BLOCK_RE.sub(" ", html)
    html = _COMMENT_RE.sub(" ", html)
    html = _BR_RE.sub("\n", html)
    html = _BLOCK_END_RE.sub("\n", html)
    text = _TAG_RE.sub(" ", html)
    text = unescape(text)
    text = _WS_RE.sub(" ", text)
    text = _NL_RE.sub("\n\n", text)
    return text.strip()


def pdf_to_text(raw: bytes, max_pages: int = 0) -> tuple[str, str]:
    """Extract text from PDF bytes. Returns (text, method). method is 'pdftotext' / 'pypdf' /
    '' (no extractor available or extraction failed). pdftotext -layout is tried first because
    it keeps table columns (fee/rate schedules); pypdf is the pure-python fallback."""
    if b"%PDF-" not in raw[:1024]:
        return "", ""   # not a PDF (e.g. an HTML interstitial at a .pdf URL) — don't feed the extractors
    if _HAS_PDFTOTEXT:
        try:
            args = ["pdftotext", "-layout"]
            if max_pages and max_pages > 0:
                args += ["-l", str(max_pages)]
            args += ["-", "-"]  # stdin → stdout, no temp files
            proc = subprocess.run(args, input=raw, capture_output=True, timeout=60)
            text = proc.stdout.decode("utf-8", errors="replace")
            if text.strip():
                return text, "pdftotext"
        except Exception:
            pass
    if _HAS_PYPDF:
        try:
            reader = pypdf.PdfReader(io.BytesIO(raw))
            pages = reader.pages[:max_pages] if (max_pages and max_pages > 0) else reader.pages
            text = "\n".join((p.extract_text() or "") for p in pages)
            if text.strip():
                return text, "pypdf"
        except Exception:
            pass
    return "", ""


def _is_pdf(ctype: str, url: str) -> bool:
    """A response is a PDF if its content-type says so OR the URL *path* ends in .pdf (path, not
    the whole URL, so a query string like `?download=1` doesn't defeat the suffix check)."""
    if (ctype or "").startswith("application/pdf"):
        return True
    return urlparse(url).path.lower().endswith(".pdf")


# ── Content cache ────────────────────────────────────────────────────────────
def _cache_index_path() -> Path:
    return CONTENT_CACHE_DIR / "index.json"


def load_content_index() -> dict[str, dict]:
    p = _cache_index_path()
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("entries", {})
    except Exception:
        return {}


def save_content_index(entries: dict[str, dict]) -> None:
    CONTENT_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    _cache_index_path().write_text(
        json.dumps({"version": 1, "written_at": datetime.now(timezone.utc).isoformat(), "entries": entries},
                   indent=2, sort_keys=True),
        encoding="utf-8",
    )


def _text_path(url: str) -> Path:
    return CONTENT_CACHE_DIR / (hashlib.sha1(url.encode()).hexdigest() + ".txt")


def content_is_fresh(entry: dict, ttl_days: int) -> bool:
    if entry.get("status") != "OK":
        return False
    try:
        t = datetime.fromisoformat(entry["fetched_at"].replace("Z", "+00:00"))
    except Exception:
        return False
    return datetime.now(timezone.utc) - t < timedelta(days=ttl_days)


# ── Fetch ────────────────────────────────────────────────────────────────────
@dataclass
class FetchResult:
    url: str
    status: str            # OK | DEAD | BINARY | PDF_NO_TEXT | EXCLUDED | ROBOTS | UNAVAILABLE
    http_status: int = 0
    content_type: str = ""
    content_hash: str = ""
    text: str = ""
    note: str = ""
    fetched_at: str = ""
    content_kind: str = ""       # "" (html) | "pdf:pdftotext" | "pdf:pypdf"
    content_changed: bool = False
    prev_fetched_at: str = ""


async def fetch_text(session, url, ul_cfg, sv: SVConfig, robots, throttles, rate_limiter, global_sem) -> FetchResult:
    now = datetime.now(timezone.utc).isoformat()
    host = urlparse(url).netloc.lower()
    if host in ul_cfg.excluded_hosts:
        return FetchResult(url, "EXCLUDED", note="host in excluded_hosts", fetched_at=now)
    if not await robots.can_fetch(url):
        return FetchResult(url, "ROBOTS", note="robots.txt Disallow", fetched_at=now)

    policy = ul_cfg.host_policy(host)
    cd = await robots.crawl_delay(host)
    interval = policy.interval_ms
    if cd is not None and cd * 1000 > interval:
        interval = int(cd * 1000)
    ht = throttles.get(host)
    if ht is None:
        ht = UL.HostThrottle(policy.concurrency, interval)
        throttles[host] = ht

    cf = ul_cfg.raw["cloudflare_challenge_markers"]
    last_note = "no response"
    for attempt in range(ul_cfg.max_retries):
        try:
            await ht.gate()
            async with ht.sem, global_sem:
                await rate_limiter.acquire()
                async with session.get(
                    url,
                    timeout=aiohttp.ClientTimeout(total=ul_cfg.request_timeout),
                    allow_redirects=True,
                    max_redirects=ul_cfg.follow_redirects_max,
                    headers={"User-Agent": ul_cfg.user_agent},
                ) as resp:
                    status = resp.status
                    ctype = (resp.content_type or "").lower()
                    headers_lc = {k.lower(): v for k, v in resp.headers.items()}
                    # Cloudflare / WAF challenge
                    if any(h.lower() in headers_lc for h in cf["headers"]) or status in (403, 429, 503, 999):
                        last_note = f"challenge/blocked http {status}"
                        if attempt < ul_cfg.max_retries - 1:
                            await asyncio.sleep(_backoff(ul_cfg, attempt, resp.headers))
                        continue
                    if status in (404, 410) or 400 <= status < 600:
                        if status >= 500:
                            last_note = f"http {status}"
                            if attempt < ul_cfg.max_retries - 1:
                                await asyncio.sleep(_backoff(ul_cfg, attempt, resp.headers))
                            continue
                        return FetchResult(url, "DEAD", http_status=status, content_type=ctype,
                                           note=f"http {status}", fetched_at=now)
                    is_pdf_candidate = _is_pdf(ctype, url)
                    # truly-binary (image/zip/etc.) — skip without downloading the body
                    if not is_pdf_candidate and any(ctype.startswith(p) for p in sv.binary_prefixes):
                        return FetchResult(url, "BINARY", http_status=status, content_type=ctype,
                                           note="binary content — defer to agent WebFetch", fetched_at=now)
                    # Read up to the cap via chunked iteration — resp.content.read(n) returns only the
                    # first buffered chunk (~32 KB), which truncates PDFs to an invalid file and clips
                    # long HTML pages. PDFs must be read in full (a truncated PDF won't parse).
                    cap = sv.pdf_max_bytes if is_pdf_candidate else sv.max_body_bytes
                    buf = bytearray()
                    async for chunk in resp.content.iter_chunked(65536):
                        buf.extend(chunk)
                        if len(buf) >= cap:
                            break
                    raw = bytes(buf[:cap])
                    # Confirm it's really a PDF by the magic bytes — a .pdf URL that serves an HTML
                    # interstitial / error page is NOT a PDF; fall through to HTML so its figure
                    # (if any) still gets token-checked, and the extractors aren't fed garbage.
                    if is_pdf_candidate and b"%PDF-" in raw[:1024]:
                        if not sv.pdf_enabled:
                            return FetchResult(url, "BINARY", http_status=status, content_type=ctype,
                                               note="pdf extraction disabled", fetched_at=now)
                        text, method = pdf_to_text(raw, sv.pdf_max_pages)
                        if not text:
                            have_extractor = _HAS_PDFTOTEXT or _HAS_PYPDF
                            return FetchResult(
                                url, "PDF_NO_TEXT" if have_extractor else "BINARY",
                                http_status=status, content_type=ctype,
                                note="PDF has no extractable text layer (scanned image?)" if have_extractor
                                     else "no PDF extractor available (install poppler-utils or pypdf)",
                                fetched_at=now)
                        return FetchResult(
                            url, "OK", http_status=status, content_type=ctype or "application/pdf",
                            content_hash=hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16],
                            text=text, content_kind=f"pdf:{method}", fetched_at=now)
                    body = raw.decode("utf-8", errors="replace")
                    title_m = UL._TITLE_RE.search(body[:4096])
                    title = title_m.group(1).strip() if title_m else ""
                    if title and any(t.lower() in title.lower() for t in cf["body_titles"]):
                        last_note = f"challenge title: {title[:50]}"
                        if attempt < ul_cfg.max_retries - 1:
                            await asyncio.sleep(_backoff(ul_cfg, attempt, resp.headers))
                        continue
                    # is_pdf_candidate-but-not-a-PDF reached here → it's an HTML interstitial; clean it
                    text = html_to_text(body) if ("html" in ctype or ctype == "" or is_pdf_candidate) else body
                    return FetchResult(
                        url, "OK", http_status=status, content_type=ctype,
                        content_hash=hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16],
                        text=text, fetched_at=now,
                    )
        except (asyncio.TimeoutError, aiohttp.ClientError) as e:
            last_note = f"{type(e).__name__}"
            if attempt < ul_cfg.max_retries - 1:
                await asyncio.sleep(_backoff(ul_cfg, attempt, {}))
        except Exception as e:
            last_note = f"{type(e).__name__}"
            if attempt < ul_cfg.max_retries - 1:
                await asyncio.sleep(_backoff(ul_cfg, attempt, {}))
    return FetchResult(url, "UNAVAILABLE", note=last_note, fetched_at=now)


def _backoff(ul_cfg, attempt: int, headers) -> float:
    ra = headers.get("Retry-After") if headers else None
    if ra:
        try:
            return min(float(ra), 60)
        except ValueError:
            pass
    base = ul_cfg.retry_backoff[min(attempt, len(ul_cfg.retry_backoff) - 1)]
    jitter = base * (ul_cfg.retry_jitter_pct / 100.0)
    return max(0.0, base + random.uniform(-jitter, jitter))


# ── Token-presence prior + excerpts ──────────────────────────────────────────
def find_excerpts(text: str, needles: list[str], window: int, max_n: int) -> tuple[list[str], list[str]]:
    """Return (excerpts, matched_needles). Case-insensitive substring search."""
    low = text.lower()
    excerpts: list[str] = []
    matched: list[str] = []
    seen_spans: list[tuple[int, int]] = []
    for needle in needles:
        idx = low.find(needle.lower())
        if idx == -1:
            continue
        matched.append(needle)
        if len(excerpts) >= max_n:
            continue
        lo = max(0, idx - window // 2)
        hi = min(len(text), idx + len(needle) + window // 2)
        if any(lo < se and ss < hi for ss, se in seen_spans):
            continue
        seen_spans.append((lo, hi))
        snippet = text[lo:hi].replace("\n", " ").strip()
        excerpts.append(("…" if lo > 0 else "") + snippet + ("…" if hi < len(text) else ""))
    return excerpts, matched


def _is_strong(needle: str) -> bool:
    """A needle is 'strong' (specific enough to be a real signal) if its digit core is >= 3 chars.
    Single/double-digit needles ('4', '20') match noise on any page and are weak on their own."""
    return len(needle.replace(" ", "")) >= 3


def build_prior(claim: ClaimRecord, fetch: FetchResult, sv: SVConfig) -> dict:
    salient_needles: list[str] = []
    for v in claim.values:
        if v["salient"]:
            salient_needles.extend(v["needles"])
    salient_needles = list(dict.fromkeys(salient_needles))
    # Search strong (specific) needles first so excerpts anchor on real figures, not bare digits.
    ordered = sorted(salient_needles, key=lambda n: (not _is_strong(n), -len(n)))

    if fetch.status == "BINARY":
        return {"prior": "SOURCE_BINARY", "matched_tokens": [], "missing_tokens": salient_needles, "excerpts": []}
    if fetch.status == "PDF_NO_TEXT":
        return {"prior": "PDF_NO_TEXT", "matched_tokens": [], "missing_tokens": salient_needles,
                "excerpts": [], "fetch_note": fetch.note}
    if fetch.status != "OK":
        return {"prior": "SOURCE_UNAVAILABLE", "matched_tokens": [], "missing_tokens": salient_needles,
                "excerpts": [], "fetch_note": fetch.note}

    excerpts, matched = find_excerpts(fetch.text, ordered, sv.excerpt_window, sv.max_excerpts)
    missing = [n for n in salient_needles if n not in matched]
    strong_matched = [n for n in matched if _is_strong(n)]
    if not matched:
        # An OK (200) page that yielded almost no readable text — a JS-SPA / client-
        # rendered shell (e.g. elegislation.gov.hk) or a blocked stub — cannot support
        # a TOKENS_ABSENT verdict: the page was never actually read, so "figure absent"
        # would be a false positive on a CORRECT citation. Downgrade a zero-match OK
        # fetch to SOURCE_UNAVAILABLE (indeterminate) when the host is a known JS-SPA
        # or the cleaned body is too thin to hold content.
        host = (urlparse(fetch.url).netloc or "").lower()
        js_spa = any(host == h or host.endswith("." + h) for h in sv.js_spa_hosts)
        if js_spa or len((fetch.text or "").strip()) < sv.min_text_chars:
            why = "known JS-rendered host" if js_spa else f"thin body <{sv.min_text_chars} chars"
            return {"prior": "SOURCE_UNAVAILABLE", "matched_tokens": [], "missing_tokens": salient_needles,
                    "excerpts": [], "fetch_note": f"indeterminate ({why}) — page not readable, not a missing figure"}
        prior = "TOKENS_ABSENT"          # claimed figure literally not on the cited page — strongest signal
    elif strong_matched:
        prior = "TOKENS_PRESENT"         # a specific figure matched — hand to LLM with excerpt
    else:
        prior = "WEAK_MATCH"             # only bare 1-2 digit needles matched (noise-prone) — LLM must resolve
    return {"prior": prior, "matched_tokens": matched, "strong_matched": strong_matched,
            "missing_tokens": missing, "excerpts": excerpts}


# ── Worklist orchestration ───────────────────────────────────────────────────
def _settle_change(status: str, new_hash: str, last_hash: str, stable_hash: str) -> tuple[bool, str]:
    """Settle-confirmed content-change detection. Returns (changed, new_stable_hash).

    A naive "hash differs from last run" flags every dynamic page (rate tickers, timestamps,
    rotating banners) every run — ~6% of gov portals, all noise. Instead a change is only
    CONFIRMED once the page has SETTLED at a new value: the current hash equals the immediately
    previous run's hash AND differs from the stable baseline. A dynamic page (hash differs every
    run) never settles → never flagged; a genuine change settles and surfaces one run later."""
    if status != "OK" or not new_hash:
        return False, stable_hash
    if not stable_hash:
        return False, new_hash                      # first content seen → establish baseline
    if new_hash == stable_hash:
        return False, stable_hash                   # unchanged (or reverted) → still stable
    if new_hash == last_hash:
        return True, new_hash                       # same new value 2 runs running → confirmed change
    return False, stable_hash                       # in flux (dynamic) → not yet confirmed, keep baseline


async def fetch_unique(urls: list[str], ul_cfg, sv: SVConfig, force_refresh: bool = False) -> dict[str, FetchResult]:
    """Fetch each URL once (TTL-cached). force_refresh=True (audit mode) always re-fetches so the
    content-change tripwire can compare this run's hash to the prior run's stored hash."""
    CONTENT_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    index = load_content_index()
    results: dict[str, FetchResult] = {}
    to_fetch: list[str] = []
    for u in urls:
        e = index.get(u)
        if e and not force_refresh and content_is_fresh(e, sv.content_ttl_days):
            tp = _text_path(u)
            text = tp.read_text(encoding="utf-8") if tp.exists() else ""
            results[u] = FetchResult(u, "OK", http_status=e.get("http_status", 0),
                                     content_type=e.get("content_type", ""),
                                     content_hash=e.get("content_hash", ""), text=text,
                                     note="cache", fetched_at=e["fetched_at"],
                                     content_kind=e.get("content_kind", ""))
        else:
            to_fetch.append(u)

    sys.stderr.write(f"[source-verify] {len(results)} cached, fetching {len(to_fetch)}"
                     f"{' (force-refresh)' if force_refresh else ''} …\n")
    if to_fetch:
        rate_limiter = UL.GlobalRateLimiter(ul_cfg.global_req_per_sec)
        global_sem = asyncio.Semaphore(ul_cfg.global_concurrency)
        throttles: dict = {}
        connector = aiohttp.TCPConnector(limit=ul_cfg.global_concurrency * 2, ssl=False)
        timeout = aiohttp.ClientTimeout(total=ul_cfg.request_timeout + 5)
        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            robots = UL.RobotsCache(session, ul_cfg.user_agent)
            fetched = await asyncio.gather(*(
                fetch_text(session, u, ul_cfg, sv, robots, throttles, rate_limiter, global_sem) for u in to_fetch
            ))
        for fr in fetched:
            prev = index.get(fr.url) or {}
            last_hash = prev.get("content_hash", "")     # the immediately-previous run's hash
            stable_hash = prev.get("stable_hash", "")    # the confirmed baseline
            # settle-confirmed change: dynamic pages (hash differs every run) are filtered out
            changed, new_stable = _settle_change(fr.status, fr.content_hash, last_hash, stable_hash)
            fr.content_changed = changed
            fr.prev_fetched_at = prev.get("stable_fetched_at", prev.get("fetched_at", "")) if changed else ""
            results[fr.url] = fr
            if fr.status == "OK":
                _text_path(fr.url).write_text(fr.text, encoding="utf-8")
            index[fr.url] = {"status": fr.status, "http_status": fr.http_status,
                             "content_type": fr.content_type, "content_hash": fr.content_hash,
                             "stable_hash": new_stable, "content_kind": fr.content_kind, "note": fr.note,
                             "fetched_at": fr.fetched_at,
                             # remember when the baseline was established, for the stale-after-verify check
                             "stable_fetched_at": (fr.fetched_at if (new_stable == fr.content_hash and changed)
                                                   else prev.get("stable_fetched_at", prev.get("fetched_at", ""))),
                             "content_changed": changed}
        save_content_index(index)
    return results


def build_worklist(claims: list[ClaimRecord], fetches: dict[str, FetchResult], sv: SVConfig) -> list[dict]:
    out = []
    for c in claims:
        fr = fetches.get(c.source_url) or FetchResult(c.source_url, "UNAVAILABLE", note="not fetched")
        prior = build_prior(c, fr, sv)
        rec = asdict(c)
        rec.update({
            "fetch_status": fr.status,
            "http_status": fr.http_status,
            "content_hash": fr.content_hash,
            "fetched_at": fr.fetched_at,
            "content_kind": fr.content_kind,
            "content_changed": fr.content_changed,
            "prev_fetched_at": fr.prev_fetched_at,
            **prior,
        })
        out.append(rec)
    return out


# ── Audit (deterministic, no-LLM report) ─────────────────────────────────────
def _changed_after_stamp(rec: dict) -> bool:
    """True if the cited page changed AND the change is newer than the claim's Last-verified stamp."""
    if not rec.get("content_changed"):
        return False
    stamp = rec.get("inline_stamp")
    prev = rec.get("prev_fetched_at")
    if not stamp or not prev:
        return True  # changed, but no stamp to compare → still worth surfacing
    try:
        sd = datetime.strptime(stamp["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        pd = datetime.fromisoformat(prev.replace("Z", "+00:00"))
        return pd >= sd
    except Exception:
        return True


def audit_report(worklist: list[dict]) -> dict:
    by_prior: dict[str, int] = {}
    tokens_absent, content_changed, stale_changed, pdf_no_text, unavailable = [], [], [], [], []
    for r in worklist:
        by_prior[r["prior"]] = by_prior.get(r["prior"], 0) + 1
        row = {"scope": r["scope"], "line_no": r["line_no"], "claim": r["claim_text"][:140],
               "url": r["source_url"], "missing": r.get("missing_tokens", [])[:6],
               "stamp": (r.get("inline_stamp") or {}).get("date", "")}
        if r["prior"] == "TOKENS_ABSENT":
            tokens_absent.append(row)
        if r["prior"] == "PDF_NO_TEXT":
            pdf_no_text.append(row)
        if r["prior"] == "SOURCE_UNAVAILABLE":
            unavailable.append(row)
        if r.get("content_changed"):
            crow = dict(row, prev_fetched_at=r.get("prev_fetched_at", ""))
            content_changed.append(crow)
            if _changed_after_stamp(r):
                stale_changed.append(crow)
    # flagged = DISTINCT claims in either bucket (a claim that is both absent AND changed counts once)
    flagged_keys = {(r["scope"], r["line_no"], r["url"]) for r in tokens_absent + content_changed}
    return {
        "total": len(worklist),
        "by_prior": dict(sorted(by_prior.items())),
        "tokens_absent": tokens_absent,
        "content_changed": content_changed,
        "stale_changed": stale_changed,   # changed after Last verified — highest priority
        "pdf_no_text": pdf_no_text,
        "source_unavailable": unavailable,
        "flagged": len(flagged_keys),
    }


def render_audit_md(rep: dict, last_run: str = "") -> str:
    def table(rows, cols, fmt):
        if not rows:
            return "_(none)_\n"
        out = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
        out += [fmt(r) for r in rows]
        return "\n".join(out) + "\n"

    L = [
        "# Source-content audit (deterministic — no LLM)",
        "",
        f"Run: {datetime.now(timezone.utc).isoformat()}  ·  previous run: {last_run or '(none)'}",
        f"Claims checked: {rep['total']}  ·  flagged: {rep['flagged']}",
        "",
        "> **These are tripwires, not verdicts.** A `TOKENS_ABSENT` figure may sit on a deeper page or be"
        " formatted differently; a changed page may be cosmetic. Triage before acting — run the LLM"
        " verification (`shared/source-verifier.md`) on anything that needs a judgement. Nothing here was auto-edited.",
        "",
        "## Prior breakdown",
        "",
    ]
    for k, v in rep["by_prior"].items():
        L.append(f"- {k}: {v}")
    L += [
        "",
        "## ⚠️ Source changed AFTER its `Last verified` date (re-verify first)",
        "",
        table(rep["stale_changed"], ["scope", "line", "claim", "changed-since", "url"],
              lambda r: f"| `{r['scope']}` | {r['line_no']} | {r['claim'][:80].replace('|', '/')} | {r.get('prev_fetched_at','')[:10]} | {r['url']} |"),
        "",
        f"## Cited page CHANGED since last run ({len(rep['content_changed'])})",
        "",
        table(rep["content_changed"], ["scope", "line", "url", "changed-since"],
              lambda r: f"| `{r['scope']}` | {r['line_no']} | {r['url']} | {r.get('prev_fetched_at','')[:10]} |"),
        "",
        f"## Figure NOT on cited page — `TOKENS_ABSENT` ({len(rep['tokens_absent'])})",
        "",
        table(rep["tokens_absent"], ["scope", "line", "claim", "missing", "url"],
              lambda r: f"| `{r['scope']}` | {r['line_no']} | {r['claim'][:70].replace('|', '/')} | {', '.join(map(str, r['missing']))} | {r['url']} |"),
        "",
        f"## PDF with no text layer ({len(rep['pdf_no_text'])})  ·  Source unavailable ({len(rep['source_unavailable'])})",
        "",
        "Listed in the JSON artifact. PDF_NO_TEXT = scanned image (needs OCR / manual read);"
        " SOURCE_UNAVAILABLE = blocked / timeout (often a Cloudflare challenge, cross-check `url-liveness`).",
        "",
        "Action: triage `stale_changed` first, then `TOKENS_ABSENT`. Run `/property-deep-dive --update --country=<iso2>`"
        " or the LLM verifier for any country with a cluster of flags.",
    ]
    return "\n".join(L)


def worklist_stats(worklist: list[dict]) -> dict:
    by_prior: dict[str, int] = {}
    by_scope: dict[str, int] = {}
    absent = []
    for r in worklist:
        by_prior[r["prior"]] = by_prior.get(r["prior"], 0) + 1
        by_scope[r["scope"]] = by_scope.get(r["scope"], 0) + 1
        if r["prior"] == "TOKENS_ABSENT":
            absent.append({"id": r["id"], "claim": r["claim_text"][:120], "url": r["source_url"],
                           "missing": r["missing_tokens"][:6]})
    return {
        "total": len(worklist),
        "by_prior": dict(sorted(by_prior.items())),
        "by_scope_top": dict(sorted(by_scope.items(), key=lambda x: -x[1])[:15]),
        "tokens_absent_count": len(absent),
        "tokens_absent": absent[:40],
    }


# ── CLI ──────────────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description="Source-content verifier — extract + fetch + worklist (deterministic half).")
    ap.add_argument("--extract", action="store_true", help="parse claims only (no network); print stats")
    ap.add_argument("--build-worklist", action="store_true", help="fetch sampled claims; emit worklist for the LLM layer")
    ap.add_argument("--audit", action="store_true", help="deterministic no-LLM audit: fetch all cited pages, report TOKENS_ABSENT + CONTENT_CHANGED")
    ap.add_argument("--ci", action="store_true", help="with --audit: write report.md/report.json/cache to _ci/source-verify/ + emit GITHUB_OUTPUT")
    ap.add_argument("--country", default=None, help="restrict to one scope (iso2, or shared/<stem>)")
    ap.add_argument("--section", default=None, help="restrict to claims under headings containing this text")
    ap.add_argument("--sample", type=int, default=None, help="claim cap for the worklist (default from config)")
    ap.add_argument("--include-secondary", action="store_true", help="also verify non-primary citations")
    ap.add_argument("--json", type=Path, default=None, help="with --extract: dump every extracted claim here")
    ap.add_argument("--out", type=Path, default=None, help="worklist output path (default _local/source-verify/worklist.json)")
    ap.add_argument("--seed", type=int, default=1234, help="sample-selection seed (deterministic)")
    args = ap.parse_args()

    if not (args.extract or args.build_worklist or args.audit):
        ap.print_help()
        return 2

    sv = load_sv_config()
    allowlist = load_allowlist()
    primary_only = sv.primary_only and not args.include_secondary

    claims = extract_claims(sv, allowlist, primary_only, only_scope=args.country, only_section=args.section)
    sys.stderr.write(f"[source-verify] extracted {len(claims)} claim↔citation pairs"
                     f" ({'primary-only' if primary_only else 'incl. secondary'})\n")

    if args.extract:
        by_scope: dict[str, int] = {}
        by_tier: dict[str, int] = {}
        for c in claims:
            by_scope[c.scope] = by_scope.get(c.scope, 0) + 1
            by_tier[c.source_tier] = by_tier.get(c.source_tier, 0) + 1
        print(json.dumps({
            "total_claims": len(claims),
            "scopes_covered": len(by_scope),
            "by_tier": by_tier,
            "top_scopes": dict(sorted(by_scope.items(), key=lambda x: -x[1])[:15]),
            "stamped": sum(1 for c in claims if c.inline_stamp),
            "stale_marked": sum(1 for c in claims if c.inline_stamp and c.inline_stamp["kind"].startswith("stale")),
            "never_verified": sum(1 for c in claims if not c.inline_stamp),
        }, indent=2))
        if args.json:
            args.json.parent.mkdir(parents=True, exist_ok=True)
            args.json.write_text(json.dumps([asdict(c) for c in claims], indent=2), encoding="utf-8")
            sys.stderr.write(f"[source-verify] wrote {len(claims)} claims → {args.json}\n")
        return 0

    if args.audit:
        ul_cfg = UL.load_config(UL.read_plugin_version())
        unique_urls = sorted({c.source_url for c in claims})
        sys.stderr.write(f"[source-verify] audit: fetching {len(unique_urls)} unique cited URLs (force-refresh) …\n")
        fetches = asyncio.run(fetch_unique(unique_urls, ul_cfg, sv, force_refresh=True))
        worklist = build_worklist(claims, fetches, sv)
        rep = audit_report(worklist)

        out_dir = (ROOT / "_ci" / "source-verify") if args.ci else (OUT_DIR / "audit")
        out_dir.mkdir(parents=True, exist_ok=True)
        # last-run lives in the cache dir so it persists across CI runs via the cache artifact.
        last_run = ""
        lr = CONTENT_CACHE_DIR / "last-run.txt"
        if lr.exists():
            last_run = lr.read_text(encoding="utf-8").strip()
        (out_dir / "report.json").write_text(json.dumps(rep, indent=2), encoding="utf-8")
        (out_dir / "report.md").write_text(render_audit_md(rep, last_run), encoding="utf-8")
        lr.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")

        print(json.dumps({k: rep[k] for k in ("total", "flagged", "by_prior")}
                         | {"tokens_absent": len(rep["tokens_absent"]),
                            "content_changed": len(rep["content_changed"]),
                            "stale_changed": len(rep["stale_changed"])}, indent=2))
        gh_out = os.environ.get("GITHUB_OUTPUT")
        if gh_out:
            with open(gh_out, "a", encoding="utf-8") as f:
                f.write(f"flagged={rep['flagged']}\n")
                f.write(f"tokens_absent={len(rep['tokens_absent'])}\n")
                f.write(f"content_changed={len(rep['content_changed'])}\n")
                f.write(f"stale_changed={len(rep['stale_changed'])}\n")
                f.write(f"has_flags={'true' if rep['flagged'] > 0 else 'false'}\n")
        sys.stderr.write(f"[source-verify] audit done → {out_dir}/report.md  (flagged {rep['flagged']})\n")
        return 0

    # --build-worklist
    n = args.sample if args.sample is not None else sv.default_sample
    sample = select_sample(claims, n, sv.priority_weights, seed=args.seed)
    sys.stderr.write(f"[source-verify] selected {len(sample)}/{len(claims)} claims for verification\n")
    unique_urls = sorted({c.source_url for c in sample})
    fetches = asyncio.run(fetch_unique(unique_urls, UL.load_config(UL.read_plugin_version()), sv))
    worklist = build_worklist(sample, fetches, sv)

    out = args.out or (OUT_DIR / "worklist.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    stats = worklist_stats(worklist)
    out.write_text(json.dumps({
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": stats,
        "items": worklist,
    }, indent=2), encoding="utf-8")
    print(json.dumps(stats, indent=2))
    sys.stderr.write(f"[source-verify] wrote worklist → {out}\n")
    sys.stderr.write("[source-verify] NEXT: hand worklist.json to the LLM layer — see shared/source-verifier.md.\n")
    if stats["tokens_absent_count"]:
        sys.stderr.write(f"[source-verify] ⚠️  {stats['tokens_absent_count']} claim(s) whose figure is ABSENT from the cited page — review first.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
