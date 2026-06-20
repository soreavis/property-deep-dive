#!/usr/bin/env python3
"""URL-liveness checker for property-deep-dive.

Async aiohttp checker that:
  * extracts every external https?:// URL from the corpus (excludes _local/, .git/, node_modules/, test-fixtures.md)
  * respects robots.txt (Disallow + Crawl-delay) per RFC 9309
  * throttles per-host (config-driven; EUR-Lex 1@10s, legifrance 1@2s, gov-suffix 1@1s, default 2@500ms)
  * caps global throughput (default 10 req/s + 64 concurrent)
  * does HEAD-then-GET with retry/backoff/Retry-After respect
  * detects Cloudflare challenges (cf-ray header / "Just a moment" title) and marks INDETERMINATE
  * caches LIVE/REDIRECT_LIVE 30d, AUTH_REQUIRED 7d (TTL configurable); never caches DEAD/TIMEOUT/INDETERMINATE
  * uses 3-run rolling fail-streak before declaring DEAD
  * forces 10% random refresh per run regardless of TTL (silent-rot catcher)
  * computes a score (LIVE-equivalents / non-excluded URLs) and writes JSON + Markdown report

Designed to ship as a GitHub Actions workflow weekly. Idempotent; uses a workflow artifact for cache.

Usage:
    python3 scripts/url-liveness.py --ci              # full pipeline, writes _ci/{results.json,report.md,cache.json,score.txt}
    python3 scripts/url-liveness.py --dry-run         # same but writes to _local/url-liveness-dry-run/
    python3 scripts/url-liveness.py --extract         # print URLs to stdout, exit
    python3 scripts/url-liveness.py --score-only PATH # recompute score from an existing cache.json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import random
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

try:
    import aiohttp
except ImportError:
    sys.stderr.write("aiohttp not installed. Run: pip install aiohttp\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "_url-liveness.json"
URL_RE = re.compile(r"https?://[^\s<>\"`{}\)\]]+")
EXCLUDE_FILES = {"test-fixtures.md"}
EXCLUDE_DIRS = {"node_modules", "_local", ".git"}

# ── Status classes ───────────────────────────────────────────────────────────
LIVE = "LIVE"
REDIRECT_LIVE = "REDIRECT_LIVE"
AUTH_REQUIRED = "AUTH_REQUIRED"
INDETERMINATE = "INDETERMINATE"
DEAD = "DEAD"
TIMEOUT = "TIMEOUT"
BOT_BLOCKED = "BOT_BLOCKED"
RATE_LIMITED = "RATE_LIMITED"
ROBOTS_EXCLUDED = "ROBOTS_EXCLUDED"
EXCLUDED = "EXCLUDED"

CACHEABLE_CLASSES = {LIVE, REDIRECT_LIVE, AUTH_REQUIRED}
SCORE_EXCLUDED_CLASSES = {ROBOTS_EXCLUDED, EXCLUDED}


# ── Config ───────────────────────────────────────────────────────────────────
@dataclass
class HostPolicy:
    concurrency: int
    interval_ms: int
    reason: str = ""


@dataclass
class Config:
    raw: dict
    plugin_version: str

    @property
    def global_concurrency(self) -> int:
        return self.raw["global"]["concurrency"]

    @property
    def global_req_per_sec(self) -> int:
        return self.raw["global"]["req_per_sec"]

    @property
    def request_timeout(self) -> int:
        return self.raw["global"]["request_timeout_seconds"]

    @property
    def max_retries(self) -> int:
        return self.raw["global"]["max_retries"]

    @property
    def retry_backoff(self) -> list[int]:
        return self.raw["global"]["retry_backoff_seconds"]

    @property
    def retry_jitter_pct(self) -> int:
        return self.raw["global"]["retry_jitter_pct"]

    @property
    def fail_streak_for_dead(self) -> int:
        return self.raw["global"]["fail_streak_for_dead"]

    @property
    def random_refresh_pct(self) -> int:
        return self.raw["global"]["random_refresh_pct"]

    @property
    def threshold_pct(self) -> int:
        return self.raw["global"]["threshold_pct"]

    @property
    def cache_ttl_days(self) -> dict[str, int]:
        return self.raw["global"]["cache_ttl_days"]

    @property
    def user_agent(self) -> str:
        ua = self.raw["global"]["user_agent"]
        return ua.replace("{version}", self.plugin_version)

    @property
    def follow_redirects_max(self) -> int:
        return self.raw["global"]["follow_redirects_max"]

    @property
    def excluded_hosts(self) -> set[str]:
        return {e["host"].lower() for e in self.raw.get("excluded_hosts", [])}

    @property
    def indeterminate_codes(self) -> set[int]:
        return set(self.raw["indeterminate_status_codes"])

    @property
    def live_codes(self) -> set[int]:
        return set(self.raw["live_status_codes"])

    @property
    def auth_codes(self) -> set[int]:
        return set(self.raw["auth_required_status_codes"])

    def host_policy(self, host: str) -> HostPolicy:
        host_lc = host.lower()
        overrides = self.raw.get("per_host_overrides", {})
        # exact match first, then suffix
        for h, p in overrides.items():
            if host_lc == h.lower() or host_lc.endswith("." + h.lower()):
                return HostPolicy(p["concurrency"], p["interval_ms"], p.get("reason", ""))
        if _is_gov_suffix(host_lc):
            g = self.raw.get("gov_suffix_default", {})
            if g:
                return HostPolicy(g["concurrency"], g["interval_ms"], g.get("reason", ""))
        d = self.raw["global"]
        return HostPolicy(d["default_per_host_concurrency"], d["default_per_host_interval_ms"], "default")


_GOV_SUFFIX_RE = re.compile(r"\.(?:gov|gouv|gob)(?:\.[a-z]{2,3})?$")


def _is_gov_suffix(host_lc: str) -> bool:
    return bool(_GOV_SUFFIX_RE.search(host_lc))


def load_config(plugin_version: str = "0.0.0") -> Config:
    raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return Config(raw=raw, plugin_version=plugin_version)


def read_plugin_version() -> str:
    try:
        p = ROOT / ".claude-plugin" / "plugin.json"
        return json.loads(p.read_text(encoding="utf-8")).get("version", "0.0.0")
    except Exception:
        return "0.0.0"


# ── URL extraction ───────────────────────────────────────────────────────────
def extract_urls() -> list[str]:
    seen: set[str] = set()
    for path in ROOT.rglob("*.md"):
        if path.name in EXCLUDE_FILES:
            continue
        if any(p in EXCLUDE_DIRS for p in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for m in URL_RE.finditer(text):
            end = m.end()
            if end < len(text) and text[end] in "<{":
                continue  # template placeholder
            url = m.group(0).rstrip(".,;:)")
            seen.add(url)
    return sorted(seen)


# ── Robots.txt ───────────────────────────────────────────────────────────────
class RobotsCache:
    def __init__(self, session: aiohttp.ClientSession, user_agent: str):
        self._session = session
        self._ua = user_agent
        self._cache: dict[str, RobotFileParser | None] = {}
        self._locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)

    async def get(self, host: str) -> RobotFileParser | None:
        if host in self._cache:
            return self._cache[host]
        async with self._locks[host]:
            if host in self._cache:
                return self._cache[host]
            rp = RobotFileParser()
            try:
                async with self._session.get(
                    f"https://{host}/robots.txt",
                    timeout=aiohttp.ClientTimeout(total=10),
                    allow_redirects=True,
                    headers={"User-Agent": self._ua},
                ) as resp:
                    if resp.status >= 400:
                        self._cache[host] = None
                        return None
                    body = await resp.text(errors="replace")
                    rp.parse(body.splitlines())
                    self._cache[host] = rp
                    return rp
            except Exception:
                self._cache[host] = None
                return None

    async def can_fetch(self, url: str) -> bool:
        host = urlparse(url).netloc
        rp = await self.get(host)
        if rp is None:
            return True
        try:
            return rp.can_fetch(self._ua, url)
        except Exception:
            return True

    async def crawl_delay(self, host: str) -> float | None:
        rp = await self.get(host)
        if rp is None:
            return None
        try:
            d = rp.crawl_delay(self._ua)
            if d is None:
                d = rp.crawl_delay("*")
            return float(d) if d is not None else None
        except Exception:
            return None


# ── Throttles ────────────────────────────────────────────────────────────────
class GlobalRateLimiter:
    """Token-bucket: drip rate_per_sec tokens/s, capacity = rate_per_sec."""

    def __init__(self, rate_per_sec: float):
        self._rate = rate_per_sec
        self._tokens = rate_per_sec
        self._last = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            while True:
                now = time.monotonic()
                elapsed = now - self._last
                self._tokens = min(self._rate, self._tokens + elapsed * self._rate)
                self._last = now
                if self._tokens >= 1:
                    self._tokens -= 1
                    return
                sleep_for = (1 - self._tokens) / self._rate
                await asyncio.sleep(sleep_for)


class HostThrottle:
    """Per-host: bounded concurrency AND minimum interval between request starts."""

    def __init__(self, concurrency: int, interval_ms: int):
        self.sem = asyncio.Semaphore(concurrency)
        self.interval = interval_ms / 1000.0
        self._last_start = 0.0
        self._lock = asyncio.Lock()

    async def gate(self):
        async with self._lock:
            now = time.monotonic()
            wait = (self._last_start + self.interval) - now
            if wait > 0:
                await asyncio.sleep(wait)
            self._last_start = time.monotonic()


# ── HTTP check ───────────────────────────────────────────────────────────────
@dataclass
class CheckResult:
    url: str
    status: int = 0
    cls: str = ""
    checked_at: str = ""
    fail_streak: int = 0
    final_url: str = ""
    note: str = ""


def _classify(status: int, body_title: str, headers: dict, cfg: Config) -> tuple[str, str]:
    if status in cfg.live_codes and 200 <= status < 300:
        return LIVE, ""
    if status in cfg.live_codes and 300 <= status < 400:
        return REDIRECT_LIVE, ""
    if status in cfg.auth_codes:
        return AUTH_REQUIRED, "auth required"
    # Cloudflare / WAF challenge detection
    headers_lc = {k.lower(): v for k, v in headers.items()}
    cf_markers = cfg.raw["cloudflare_challenge_markers"]
    if any(h.lower() in headers_lc for h in cf_markers["headers"]):
        return BOT_BLOCKED, "cloudflare/WAF marker header"
    if body_title and any(t.lower() in body_title.lower() for t in cf_markers["body_titles"]):
        return BOT_BLOCKED, f"challenge title: {body_title[:60]}"
    if status == 999:
        return BOT_BLOCKED, "999 datacenter-IP block (LinkedIn-style)"
    if status == 429:
        return RATE_LIMITED, "rate limited"
    if status in cfg.indeterminate_codes:
        return INDETERMINATE, f"indeterminate {status}"
    if status in (404, 410):
        return DEAD, f"http {status}"
    if status == 0:
        return TIMEOUT, "timeout/connection error"
    if 400 <= status < 500:
        return DEAD, f"http {status}"
    return INDETERMINATE, f"http {status}"


_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


async def _http_request(
    session: aiohttp.ClientSession,
    method: str,
    url: str,
    cfg: Config,
) -> tuple[int, str, dict, str]:
    """Return (status, body_title_or_empty, headers, final_url). status=0 on transport error."""
    try:
        async with session.request(
            method,
            url,
            timeout=aiohttp.ClientTimeout(total=cfg.request_timeout),
            allow_redirects=True,
            max_redirects=cfg.follow_redirects_max,
            headers={"User-Agent": cfg.user_agent},
        ) as resp:
            headers = dict(resp.headers)
            body_title = ""
            # Read a small slice only to look for challenge titles (cap 4KB)
            if method == "GET" and resp.content_type and "html" in resp.content_type.lower():
                try:
                    chunk = await resp.content.read(4096)
                    m = _TITLE_RE.search(chunk.decode("utf-8", errors="replace"))
                    if m:
                        body_title = m.group(1).strip()
                except Exception:
                    pass
            return resp.status, body_title, headers, str(resp.url)
    except asyncio.TimeoutError:
        return 0, "", {}, url
    except aiohttp.ClientError:
        return 0, "", {}, url
    except Exception:
        return 0, "", {}, url


def _retry_after_seconds(headers: dict) -> float | None:
    ra = headers.get("Retry-After") or headers.get("retry-after")
    if not ra:
        return None
    try:
        return float(ra)
    except ValueError:
        # could be HTTP-date; ignore in this scope
        return None


async def check_one(
    session: aiohttp.ClientSession,
    url: str,
    cfg: Config,
    host_throttle: HostThrottle,
    rate_limiter: GlobalRateLimiter,
    robots: RobotsCache,
) -> CheckResult:
    now_iso = datetime.now(timezone.utc).isoformat()

    # robots.txt check
    if not await robots.can_fetch(url):
        return CheckResult(url=url, status=0, cls=ROBOTS_EXCLUDED, checked_at=now_iso, note="robots.txt Disallow")

    last_status = 0
    last_final = url
    last_cls = INDETERMINATE
    last_note = ""
    note = ""

    for attempt in range(cfg.max_retries):
        await host_throttle.gate()
        async with host_throttle.sem:
            await rate_limiter.acquire()
            # HEAD first
            status, title, headers, final_url = await _http_request(session, "HEAD", url, cfg)
            # GET fallback on any non-success: HEAD-method allergy (400/405/406), bot-detection
            # 404 (sites serving 404 to non-browser clients), 403/auth, transport error (0), 5xx, or
            # the long-tail non-standard 4xx codes some WAFs emit (466/468/421/412 etc). The HEAD
            # response is unreliable for many gov / tax-authority hosts (triage 2026-05-27 showed
            # 74 / 267 reported-DEAD URLs returned 200 on GET with browser UA).
            head_succeeded_2xx_3xx = 200 <= status < 400
            if not head_succeeded_2xx_3xx:
                await host_throttle.gate()
                await rate_limiter.acquire()
                status, title, headers, final_url = await _http_request(session, "GET", url, cfg)

        last_status, last_final = status, final_url
        cls, note = _classify(status, title, headers, cfg)
        last_cls, last_note = cls, note
        if cls in (LIVE, REDIRECT_LIVE, AUTH_REQUIRED, BOT_BLOCKED, ROBOTS_EXCLUDED, DEAD):
            break
        # Retryable: TIMEOUT / RATE_LIMITED / INDETERMINATE 5xx
        if attempt < cfg.max_retries - 1:
            ra = _retry_after_seconds(headers)
            if ra is not None:
                sleep_for = min(ra, 60)
            else:
                base = cfg.retry_backoff[min(attempt, len(cfg.retry_backoff) - 1)]
                jitter = base * (cfg.retry_jitter_pct / 100.0)
                sleep_for = base + random.uniform(-jitter, jitter)
            await asyncio.sleep(max(0.0, sleep_for))

    return CheckResult(
        url=url,
        status=last_status,
        cls=last_cls,
        checked_at=now_iso,
        final_url=last_final if last_final != url else "",
        note=last_note,
    )


# ── Cache ────────────────────────────────────────────────────────────────────
def cache_load(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "entries" not in data:
            return {}
        return data["entries"]
    except Exception:
        return {}


def cache_save(path: Path, entries: dict[str, dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "written_at": datetime.now(timezone.utc).isoformat(),
        "entries": entries,
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def cache_is_fresh(entry: dict, cfg: Config) -> bool:
    cls = entry.get("cls", "")
    if cls not in CACHEABLE_CLASSES:
        return False
    ttl_days = cfg.cache_ttl_days.get(cls)
    if ttl_days is None:
        return False
    try:
        checked_at = datetime.fromisoformat(entry["checked_at"].replace("Z", "+00:00"))
    except Exception:
        return False
    return datetime.now(timezone.utc) - checked_at < timedelta(days=ttl_days)


def pick_random_refresh(urls: list[str], pct: int, seed: int | None = None) -> set[str]:
    if pct <= 0 or not urls:
        return set()
    rng = random.Random(seed) if seed is not None else random
    n = max(1, len(urls) * pct // 100)
    return set(rng.sample(urls, min(n, len(urls))))


# ── Scoring + report ─────────────────────────────────────────────────────────
def compute_score(entries: dict[str, dict], cfg: Config) -> dict[str, Any]:
    """Return summary stats. fail_streak ≥ cfg.fail_streak_for_dead → counted as DEAD."""
    total = 0
    counted = 0
    by_class: dict[str, int] = defaultdict(int)
    confirmed_dead: list[dict] = []
    pending_dead: list[dict] = []
    by_host_dead: dict[str, int] = defaultdict(int)

    for url, e in entries.items():
        cls = e.get("cls", "")
        fail_streak = e.get("fail_streak", 0)
        by_class[cls] += 1
        total += 1
        if cls in SCORE_EXCLUDED_CLASSES:
            continue
        counted += 1
        if cls in (DEAD, TIMEOUT) and fail_streak >= cfg.fail_streak_for_dead:
            confirmed_dead.append({"url": url, "cls": cls, "streak": fail_streak, "note": e.get("note", "")})
            by_host_dead[urlparse(url).netloc.lower()] += 1
        elif cls in (DEAD, TIMEOUT):
            pending_dead.append({"url": url, "cls": cls, "streak": fail_streak})

    confirmed_count = len(confirmed_dead)
    score = ((counted - confirmed_count) * 100) // counted if counted else 100
    return {
        "score": score,
        "total": total,
        "counted": counted,
        "confirmed_dead_count": confirmed_count,
        "confirmed_dead": confirmed_dead,
        "pending_dead": pending_dead,
        "by_class": dict(by_class),
        "by_host_dead": dict(sorted(by_host_dead.items(), key=lambda x: -x[1])),
    }


def render_report(
    summary: dict, last_success_iso: str, cache_hits: int, fresh_checks: int, cfg: Config
) -> str:
    score = summary["score"]
    flag = "🟢" if score >= cfg.threshold_pct else "🟠"
    lines = [
        f"# URL Liveness — score {score}%",
        "",
        f"{flag} Threshold: {cfg.threshold_pct}%.",
        "",
        f"Run timestamp: {datetime.now(timezone.utc).isoformat()}",
        f"Previous successful run: {last_success_iso or '(none recorded)'}",
        f"Total URLs in corpus: {summary['total']}  · counted toward score: {summary['counted']}  · excluded: {summary['total'] - summary['counted']}",
        f"Cache hits: {cache_hits}  · fresh checks this run: {fresh_checks}",
        "",
        "## Class breakdown",
        "",
    ]
    for c in sorted(summary["by_class"]):
        lines.append(f"- {c}: {summary['by_class'][c]}")
    lines.append("")
    lines.append("## Top failing hosts (≥3-week rolling fail = confirmed DEAD)")
    lines.append("")
    if not summary["by_host_dead"]:
        lines.append("(none)")
    else:
        lines.append("| count | host |")
        lines.append("|---|---|")
        for h, n in list(summary["by_host_dead"].items())[:20]:
            lines.append(f"| {n} | {h} |")
    lines.append("")
    lines.append("## Confirmed dead URLs (first 50)")
    lines.append("")
    if not summary["confirmed_dead"]:
        lines.append("(none)")
    else:
        for d in summary["confirmed_dead"][:50]:
            lines.append(f"- [{d['cls']} streak={d['streak']}] {d['url']}")
    lines.append("")
    lines.append("## Pending (single/double-week fails — NOT counted yet)")
    lines.append("")
    lines.append(f"{len(summary['pending_dead'])} URL(s) in pending state — re-checked next run.")
    lines.append("")
    lines.append("Action: run `/property-deep-dive --update --validate-only --country=<iso2>` for any country whose playbook contributes ≥5 confirmed-dead links.")
    return "\n".join(lines)


# ── Orchestrator ─────────────────────────────────────────────────────────────
async def run_check(
    urls: list[str],
    cfg: Config,
    cache: dict[str, dict],
    refresh_set: set[str],
    progress_every: int = 200,
) -> tuple[dict[str, dict], int, int]:
    """Mutate cache in place. Return (cache, cache_hits, fresh_checks)."""
    cache_hits = 0
    fresh_checks = 0
    host_throttles: dict[str, HostThrottle] = {}
    rate_limiter = GlobalRateLimiter(cfg.global_req_per_sec)
    global_sem = asyncio.Semaphore(cfg.global_concurrency)

    timeout = aiohttp.ClientTimeout(total=cfg.request_timeout + 5)
    connector = aiohttp.TCPConnector(limit=cfg.global_concurrency * 2, ssl=False)
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        robots = RobotsCache(session, cfg.user_agent)

        async def worker(url: str):
            nonlocal cache_hits, fresh_checks
            host = urlparse(url).netloc.lower()
            if host in cfg.excluded_hosts:
                cache[url] = {
                    "cls": EXCLUDED, "status": 0, "checked_at": datetime.now(timezone.utc).isoformat(),
                    "fail_streak": 0, "note": "host in excluded_hosts",
                }
                return
            entry = cache.get(url)
            use_cached = (
                entry is not None
                and url not in refresh_set
                and cache_is_fresh(entry, cfg)
            )
            if use_cached:
                cache_hits += 1
                return
            policy = cfg.host_policy(host)
            # Robots Crawl-delay can RAISE our floor; never lowers it
            cd = await robots.crawl_delay(host)
            if cd is not None and cd * 1000 > policy.interval_ms:
                policy = HostPolicy(policy.concurrency, int(cd * 1000), policy.reason + f" + robots Crawl-delay {cd}s")
            ht = host_throttles.get(host)
            if ht is None:
                ht = HostThrottle(policy.concurrency, policy.interval_ms)
                host_throttles[host] = ht

            async with global_sem:
                result = await check_one(session, url, cfg, ht, rate_limiter, robots)

            fresh_checks += 1
            prev_streak = entry.get("fail_streak", 0) if entry else 0
            prev_cls = entry.get("cls", "") if entry else ""
            new_streak = prev_streak
            if result.cls in (DEAD, TIMEOUT):
                new_streak = prev_streak + 1 if prev_cls in (DEAD, TIMEOUT) else 1
            else:
                new_streak = 0
            cache[url] = {
                "cls": result.cls,
                "status": result.status,
                "checked_at": result.checked_at,
                "fail_streak": new_streak,
                "final_url": result.final_url,
                "note": result.note,
            }
            if fresh_checks % progress_every == 0:
                sys.stderr.write(f"  …{fresh_checks} fresh checks, {cache_hits} cache hits\n")
                sys.stderr.flush()

        await asyncio.gather(*(worker(u) for u in urls))

    return cache, cache_hits, fresh_checks


def prune_cache(cache: dict[str, dict], current_urls: set[str]) -> int:
    """Drop entries whose URL is no longer in the corpus."""
    removed = [u for u in cache if u not in current_urls]
    for u in removed:
        del cache[u]
    return len(removed)


# ── CLI ──────────────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description="URL liveness checker — async, polite, cached.")
    ap.add_argument("--ci", action="store_true", help="full CI pipeline; writes to _ci/")
    ap.add_argument("--dry-run", action="store_true", help="same as --ci but writes to _local/url-liveness-dry-run/")
    ap.add_argument("--extract", action="store_true", help="extract URLs from corpus; print to stdout; exit")
    ap.add_argument("--score-only", type=Path, default=None, metavar="PATH", help="compute score from an existing cache.json; print summary; exit")
    ap.add_argument("--cache-in", type=Path, default=None, help="cache to restore from (default: <out_dir>/cache.json)")
    ap.add_argument("--last-success-in", type=Path, default=None, help="prior 'last-success.txt' (ISO timestamp) to display in report")
    args = ap.parse_args()

    if args.extract:
        for u in extract_urls():
            print(u)
        return 0

    cfg = load_config(read_plugin_version())

    if args.score_only:
        cache = cache_load(args.score_only)
        summary = compute_score(cache, cfg)
        print(json.dumps(summary, indent=2))
        return 0

    if not (args.ci or args.dry_run):
        ap.print_help()
        return 2

    out_dir = (ROOT / "_ci") if args.ci else (ROOT / "_local" / "url-liveness-dry-run")
    out_dir.mkdir(parents=True, exist_ok=True)

    cache_in = args.cache_in if args.cache_in else (out_dir / "cache.json")
    cache_out = out_dir / "cache.json"
    results_out = out_dir / "results.json"
    report_out = out_dir / "report.md"
    score_out = out_dir / "score.txt"
    last_success_out = out_dir / "last-success.txt"

    last_success = ""
    if args.last_success_in and args.last_success_in.exists():
        last_success = args.last_success_in.read_text(encoding="utf-8").strip()
    elif (out_dir / "last-success.txt").exists():
        last_success = (out_dir / "last-success.txt").read_text(encoding="utf-8").strip()

    sys.stderr.write(f"[url-liveness] extracting URLs from corpus under {ROOT} …\n")
    urls = extract_urls()
    sys.stderr.write(f"[url-liveness] {len(urls)} unique URLs found\n")

    cache = cache_load(cache_in)
    pruned = prune_cache(cache, set(urls))
    sys.stderr.write(f"[url-liveness] cache: {len(cache)} entries loaded from {cache_in} (pruned {pruned} stale)\n")

    refresh_set = pick_random_refresh(urls, cfg.random_refresh_pct, seed=int(time.time()))
    sys.stderr.write(f"[url-liveness] random refresh: {len(refresh_set)} URL(s) ({cfg.random_refresh_pct}%)\n")

    started = time.monotonic()
    cache, hits, fresh = asyncio.run(run_check(urls, cfg, cache, refresh_set))
    elapsed = time.monotonic() - started
    sys.stderr.write(f"[url-liveness] done in {elapsed:.1f}s — {hits} cache hits, {fresh} fresh checks\n")

    cache_save(cache_out, cache)
    summary = compute_score(cache, cfg)
    report = render_report(summary, last_success, hits, fresh, cfg)
    results_out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    report_out.write_text(report, encoding="utf-8")
    score_out.write_text(str(summary["score"]) + "\n", encoding="utf-8")

    if summary["score"] >= cfg.threshold_pct:
        last_success_out.write_text(datetime.now(timezone.utc).isoformat() + "\n", encoding="utf-8")

    # Emit GH outputs if in CI
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a", encoding="utf-8") as f:
            f.write(f"score={summary['score']}\n")
            f.write(f"total={summary['total']}\n")
            f.write(f"counted={summary['counted']}\n")
            f.write(f"confirmed_dead={summary['confirmed_dead_count']}\n")
            f.write(f"threshold={cfg.threshold_pct}\n")
            f.write(f"below_threshold={'true' if summary['score'] < cfg.threshold_pct else 'false'}\n")

    print(f"[url-liveness] score={summary['score']}%  counted={summary['counted']}  confirmed_dead={summary['confirmed_dead_count']}  threshold={cfg.threshold_pct}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
