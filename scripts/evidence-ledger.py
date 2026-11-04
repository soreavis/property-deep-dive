#!/usr/bin/env python3
"""Evidence ledger: remember which page proved each playbook line, so the next maintenance run
re-checks it with a fetch instead of an agent.

A maintenance agent that verifies a figure already records the deep page it read it on
(`evidence: [{url, fact, tier}]` in its patch). Without this ledger that URL is thrown away
after the PR, and the next run pays an agent to find the same page again.

    config/_evidence/<iso2>.json   {"urls": [...], "lines": {"<line hash>": {"u": [i, ...], "d": "YYYY-MM-DD"}}}

The key is a hash of the exact playbook line. Editing the line orphans its entry, which is the
point: changed text must be verified again.

    python3 scripts/evidence-ledger.py add RESULT.json [...] --date 2026-10-23
        RESULT is a workflow result (playbooks[].clusters[].items[]), a flat list of patch items,
        or a workflow journal.jsonl. Only lines present verbatim in the current playbook are kept.
    python3 scripts/evidence-ledger.py check --country fi [--out worklist.json]
        Re-fetch each ledger URL (source-verify's polite, TTL-cached fetcher) and re-read the
        line's figures on it. A line is CONFIRMED when every salient figure sits on one of its
        pages, each page holding its share within source-verify's COVER_WINDOW (source-verify.machine_confirmed). Everything else in a
        fast-changing section, ledgered or not, goes to the worklist for an agent, with the
        figures already found listed so the agent re-checks only the missing ones.
    python3 scripts/evidence-ledger.py stats
"""
from __future__ import annotations

import argparse
import asyncio
import datetime
import functools
import hashlib
import importlib.util
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER_DIR = ROOT / "config" / "_evidence"
COUNTRIES = ROOT / "skills" / "property-deep-dive" / "countries"
FAST = ("price", "tax", "rental", "risks", "mains", "work", "cost benchmark")
# Lines whose figures are not claims about a source page: honest estimates, pointers and
# arithmetic (check-playbooks.py checks that) need no agent re-read.
SETTLED = re.compile(r"(~\s*est\.|\best\.|≈|\bverify (at|with)\b|data not publicly available|\bcomputed\b|curated wisdom)", re.I)
MAX_UNCHANGED_DAYS = 365  # an unchanged page proves nothing new for ever: an agent re-reads the line once a year
# Poisson change model (Cho & Garcia-Molina 2003): rate = -ln((n-X+0.5)/(n+0.5)) / t. Measured on
# the 65 refuted LU and RS lines re-researched 12 days later, 4 of them changed. maintain.py apply
# prints the same estimate from each run's audit sample, so this number can be revised.
CHANGE_RATE_PER_DAY = 0.00525
AUDIT_SHARE = 0.10  # of the lines skipped as freshly proved, this share still goes to an agent
HINTS, HINT_WIDTH, K1 = 3, 300, 1.2
SEGMENT = re.compile(r"\n+|(?<=[.;!?])\s+")
TOKEN = re.compile(r"\d[\d.,\u00a0\u202f]*\d|\d|[^\W\d_]{4,}")
_spec = importlib.util.spec_from_file_location("source_verify", Path(__file__).parent / "source-verify.py")
SV = sys.modules["source_verify"] = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(SV)


def line_key(line: str) -> str:
    return hashlib.sha1(" ".join(line.split()).encode()).hexdigest()[:12]


def salient_values(line: str) -> list[dict]:
    vals = SV.extract_values(SV.mask_urls(SV.mask_inline_stamps(line)))
    return [v.__dict__ for v in vals if v.salient]


def playbook_lines(cc: str) -> list[tuple[str, str]]:
    """(section, line) for every line of the playbook, section = the enclosing `## ` heading."""
    out, section = [], ""
    for line in (COUNTRIES / cc / "playbook.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        out.append((section, line))
    return out


def load(cc: str) -> dict:
    p = LEDGER_DIR / f"{cc}.json"
    return json.loads(p.read_text()) if p.exists() else {"urls": [], "lines": {}}


def save(cc: str, led: dict) -> None:
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    used = sorted({i for e in led["lines"].values() for i in e["u"]})
    remap = {old: new for new, old in enumerate(used)}  # drop URLs no line cites any more
    led = {"urls": [led["urls"][i] for i in used],
           "lines": {k: {**e, "u": [remap[i] for i in e["u"]]} for k, e in sorted(led["lines"].items())}}
    j = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    urls = ",\n".join(j(u) for u in led["urls"])
    lines = ",\n".join(f"{j(k)}:{j(e)}" for k, e in led["lines"].items())
    (LEDGER_DIR / f"{cc}.json").write_text(f'{{"urls":[\n{urls}\n],\n"lines":{{\n{lines}\n}}}}\n')  # one entry per line


def iter_items(path: Path):
    """Patch items with evidence from a workflow result, a flat item list or a journal.jsonl."""
    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("new"), str) and isinstance(o.get("file"), str) and o.get("evidence") \
                    and o.get("status") != "DROP":
                yield o
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)
    if path.suffix == ".jsonl":
        for l in path.read_text().splitlines():
            yield from walk(json.loads(l).get("result"))
    else:
        yield from walk(json.loads(path.read_text()))


def cmd_add(paths: list[Path], date: str) -> int:
    current: dict[str, set[str]] = {}
    ledgers: dict[str, dict] = {}
    found: list[tuple[str, str, list[str]]] = []
    for path in paths:
        for it in iter_items(path):
            m = re.search(r"countries/([a-z]{2})/playbook\.md$", it["file"])
            urls = [e["url"] for e in it["evidence"] if isinstance(e, dict) and str(e.get("url", "")).startswith("http")]
            if not (m and urls):
                continue
            cc = m[1]
            if cc not in current:
                current[cc] = {line_key(l) for _, l in playbook_lines(cc)}
                ledgers[cc] = load(cc)
            # a line superseded later, or with no figure to re-check, stays out
            found += [(cc, line, urls) for line in it["new"].splitlines()
                      if line_key(line) in current[cc] and salient_values(line)]
    fetches = fetch_all(u for _, _, urls in found for u in urls)
    for cc, line, urls in found:
        put(ledgers[cc], line_key(line), urls, date, support_hash(line, urls, fetches))
    for cc, led in ledgers.items():
        save(cc, led)
    print(f"ledgered {len(found)} line-evidence pairs across {len(ledgers)} playbook(s)")
    return 0


def inline_urls(line: str) -> list[str]:
    return [(m.group("url") or m.group("bare")).rstrip(".,;:)") for m in SV.CITE_RE.finditer(line)]


SOURCE_TABLES = re.compile(r"^## .*(Source URL|Verification authorit|Primary sources)", re.I)


def named_sources(lines: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """(distinctive name word, URL) from the playbook's source / authority tables, so a line that
    says "source: Destatis" can be checked against the Destatis row's page by script."""
    out, on = [], False
    for _, line in lines:
        if line.startswith("## "):
            on = bool(SOURCE_TABLES.match(line))
        elif on and line.startswith("|"):
            urls = inline_urls(line)
            name = re.sub(r"[*`]", "", line.strip("|").split("|")[0]).strip()
            word = next((w for w in re.findall(r"[^\W\d_][\w-]{2,}", name) if w[0].isupper() or not w.isascii()), None)
            if urls and word:
                out.append((word, urls[0]))
    return out


def candidate_urls(line: str, named: list[tuple[str, str]]) -> list[str]:
    urls = inline_urls(line)
    if urls:
        return urls
    return list(dict.fromkeys(u for w, u in named if re.search(rf"(?<![\w-]){re.escape(w)}(?![\w-])", line)))[:3]


def covered_values(values: list[dict], urls: list[str], fetches: dict) -> tuple[set[int], dict]:
    """Indices of the values that sit together on one of the pages (each page may hold its own
    share of a line that cites several sources), plus the fetch status per URL."""
    needles = SV.confirm_needles(values)
    covered, status = set(), {}
    if not needles or not any(SV.is_confirm_strong(n) for v in needles for n in v):
        return covered, status
    for u in urls:
        fr = fetches.get(u)
        status[u] = fr.status if fr else "NOT_FETCHED"
        if not (fr and fr.status == "OK"):
            continue
        found = [i for i, v in enumerate(needles) if any(n in fr.text for n in v)]
        span = SV.min_cover_span(fr.text, [needles[i] for i in found]) if found else None
        if span is not None and span <= SV.cover_window(len(needles)):
            covered |= set(found)
    return covered, status


def fetch_all(urls) -> dict:
    urls = sorted(set(urls))
    sv = SV.load_sv_config()
    return asyncio.run(SV.fetch_unique(urls, SV.UL.load_config(SV.UL.read_plugin_version()), sv)) if urls else {}


def pages_read(urls: list[str], fetches: dict) -> bool:
    frs = [fetches.get(u) for u in urls]
    return bool(frs) and all(f and f.status == "OK" and f.text for f in frs)


@functools.lru_cache(maxsize=256)
def segments(text: str) -> tuple[str, ...]:
    return tuple(s.strip() for s in SEGMENT.split(text) if s.strip())


def support_hash(line: str, urls: list[str], fetches: dict) -> str | None:
    """Fingerprint of what the pages say about this line: every sentence or table row holding one
    of its values. Exact page hashes are too brittle (a quarter of 180 pages differed after six
    days, menus and news lists included); these segments move only when the line's own context
    does, and a changed figure drops its segment. None unless every page was read and one holds
    a value: a copy showing none of them is a shell or a login wall, and says nothing."""
    needles = [n for v in SV.confirm_needles(salient_values(line)) for n in v]
    if not pages_read(urls, fetches):
        return None
    kept = sorted({seg for u in urls for seg in segments(fetches[u].text) if any(n in seg for n in needles)})
    return hashlib.sha1("\0".join(kept).encode()).hexdigest()[:12] if kept else None


def age_days(entry: dict, today: str) -> int:
    return (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(entry["d"])).days


def unchanged(entry: dict | None, line: str, urls: list[str], fetches: dict, today: str) -> bool:
    return bool(entry and entry.get("h") and entry["h"] == support_hash(line, urls, fetches)
                and age_days(entry, today) <= MAX_UNCHANGED_DAYS)


def freshly_proved(entry: dict | None, urls: list[str], fetches: dict, today: str, max_risk: float) -> bool:
    """P(line changed since its proof) = 1 - e^(-rate * age) stays under max_risk, and no page
    contradicts that. Called after unchanged(), so a stored fingerprint here did not match: on
    pages that were read, that is a change signal."""
    if not entry or 1 - math.exp(-CHANGE_RATE_PER_DAY * age_days(entry, today)) >= max_risk:
        return False
    return not (entry.get("h") and pages_read(urls, fetches))


def in_audit_sample(key: str, today: str) -> bool:
    """Deterministic and unbiased: the same run picks the same lines, the next run others."""
    return int(hashlib.sha1(f"{key}{today}".encode()).hexdigest()[:8], 16) / 0xFFFFFFFF < AUDIT_SHARE


def tokens(text: str) -> list[str]:
    return [re.sub(r"[.,\u00a0\u202f]", "", t) if t[0].isdigit() else t.lower() for t in TOKEN.findall(text)]


def add_hints(rows: list[dict], fetches: dict) -> None:
    """BM25 over fixed-width passages of the pages this plan already read, so an agent starts from
    the likely passage instead of searching. A figure is a rare token, so it outranks the words;
    the width is fixed, so BM25's length term drops out."""
    wanted = {t for r in rows for t in tokens(r["line"])}
    passages, postings = [], {}
    for url, fr in fetches.items():
        text = " ".join((fr.text or "").split()) if fr.status == "OK" else ""
        for start in range(0, len(text), HINT_WIDTH // 2):
            chunk = text[start:start + HINT_WIDTH]
            counts = Counter(t for t in tokens(chunk) if t in wanted)
            passages.append((url, chunk))
            for t, tf in counts.items():
                postings.setdefault(t, []).append((len(passages) - 1, tf))
    for r in rows:
        scores: Counter = Counter()
        for t in set(tokens(r["line"])):
            hits = postings.get(t, [])
            idf = math.log(1 + (len(passages) - len(hits) + 0.5) / (len(hits) + 0.5))
            for pid, tf in hits:
                scores[pid] += idf * tf * (K1 + 1) / (tf + K1)
        seen, r["hints"] = set(), []
        for pid, _ in scores.most_common(200):
            url, chunk = passages[pid]
            if url not in seen:
                seen.add(url)
                r["hints"].append({"url": url, "text": chunk})
            if len(seen) == HINTS:
                break


def check(cc: str, touch_date: str | None = None, max_risk: float = 0.0) -> dict:
    """Machine-check every fast-section line; with touch_date, re-date the lines whose figures
    were re-read. A line is confirmed when its figures stand together on a page, or when the
    pages that proved it are byte-for-byte what they were then (the date stays that of the last
    real read, so MAX_UNCHANGED_DAYS applies). With max_risk, a line an agent proved recently is
    skipped too (status FRESH, date unchanged) unless it falls in the audit sample. A line with
    no ledger entry is tried against the URLs it cites itself, else against the source-table rows
    whose name it mentions."""
    led, lines = load(cc), playbook_lines(cc)
    named, rows = named_sources(lines), []
    today = touch_date or datetime.date.today().isoformat()
    for section, line in lines:
        vals = salient_values(line)
        if not vals or not any(k in section.lower() for k in FAST):
            continue
        e = led["lines"].get(line_key(line))
        if not e and SETTLED.search(line):
            continue
        rows.append({"section": section, "line": line.strip(), "values": vals, "ledgered": bool(e),
                     "urls": [led["urls"][i] for i in e["u"]] if e else candidate_urls(line, named)})
    fetches = fetch_all(u for r in rows for u in r["urls"])
    for r in rows:
        r["status"] = "NOT_CONFIRMED" if r["urls"] else "NO_EVIDENCE"
        covered, r["fetch"] = covered_values(r["values"], r["urls"], fetches)
        if covered and len(covered) == len(SV.confirm_needles(r["values"])):
            r["status"] = "CONFIRMED"
        elif unchanged(entry := led["lines"].get(line_key(r["line"])), r["line"], r["urls"], fetches, today):
            r["status"], r["unchanged"] = "CONFIRMED", True
        elif freshly_proved(entry, r["urls"], fetches, today, max_risk):
            if in_audit_sample(line_key(r["line"]), today):
                r["audit"] = max(age_days(entry, today), 1)
            else:
                r["status"], r["proved"] = "FRESH", entry["d"]
        if covered and r["status"] == "NOT_CONFIRMED":
            r["confirmed_values"] = [r["values"][i]["raw"] for i in sorted(covered)]
            r["missing_values"] = [v["raw"] for i, v in enumerate(r["values"]) if i not in covered]
    by: dict[str, dict] = {}
    for r in rows:
        by.setdefault(r["section"], {}).setdefault(r["status"], 0)
        by[r["section"]][r["status"]] += 1
    confirmed = [r for r in rows if r["status"] == "CONFIRMED"]
    fresh = [r for r in rows if r["status"] == "FRESH"]
    worklist = [r for r in rows if r["status"] not in ("CONFIRMED", "FRESH")]
    if touch_date:
        for r in confirmed:
            if not r.get("unchanged"):
                put(led, line_key(r["line"]), r["urls"], touch_date, support_hash(r["line"], r["urls"], fetches))
        for r in fresh:  # gives the line a change signal from now on; its date stays the proof's
            h = support_hash(r["line"], r["urls"], fetches)
            if h:
                led["lines"][line_key(r["line"])]["h"] = h
        save(cc, led)
        add_hints(worklist, fetches)
    return {"country": cc, "fast_lines": len(rows), "confirmed": len(confirmed), "fresh": fresh,
            "unchanged": sum(1 for r in confirmed if r.get("unchanged")), "by_section": by,
            "confirmed_rows": confirmed, "worklist": worklist}


def put(led: dict, key: str, urls: list[str], date: str, page_hash: str | None = None) -> None:
    idx = []
    for u in urls:
        if u not in led["urls"]:
            led["urls"].append(u)
        idx.append(led["urls"].index(u))
    prev = led["lines"].get(key)
    if prev and prev["d"] > date:
        return
    if page_hash:  # the fingerprint covers exactly these pages, so older URLs go
        led["lines"][key] = {"u": sorted(set(idx)), "d": date, "h": page_hash}
    else:
        led["lines"][key] = {"u": sorted(set(idx) | set(prev["u"] if prev else [])), "d": date}


def add_confirmed_lines(cc: str, pairs: list[tuple[str, list[str]]], date: str) -> int:
    """Ledger lines an agent confirmed WITHOUT patching them and the refuter accepted. Each is
    stored with the fingerprint of its pages, so the next run needs no agent for it while those
    pages stay the same. A page the script cannot read leaves the line out."""
    current = {line_key(l) for _, l in playbook_lines(cc)}
    pairs = [(l, [u for u in urls if u.startswith("http")]) for l, urls in pairs if line_key(l) in current]
    fetches = fetch_all(u for _, urls in pairs for u in urls)
    led, n = load(cc), 0
    for line, urls in pairs:
        h = support_hash(line, urls, fetches)
        if h:
            put(led, line_key(line), urls, date, h)
            n += 1
    save(cc, led)
    return n


def cmd_check(cc: str, out: Path | None) -> int:
    res = check(cc)
    print(json.dumps({k: res[k] for k in ("country", "fast_lines", "confirmed", "by_section")}
                     | {"to_agent": len(res["worklist"])}, ensure_ascii=False, indent=1))
    if out:
        out.write_text(json.dumps({"country": cc, "confirmed": res["confirmed_rows"], "worklist": res["worklist"]},
                                  ensure_ascii=False, indent=1))
    return 0


def cmd_stats() -> int:
    for p in sorted(LEDGER_DIR.glob("*.json")):
        led = json.loads(p.read_text())
        print(f"{p.stem}: {len(led['lines'])} lines, {len(led['urls'])} urls")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("paths", nargs="+", type=Path)
    a.add_argument("--date", required=True, help="the date the evidence was read (YYYY-MM-DD)")
    c = sub.add_parser("check")
    c.add_argument("--country", required=True)
    c.add_argument("--out", type=Path)
    sub.add_parser("stats")
    args = ap.parse_args()
    if args.cmd == "add":
        return cmd_add(args.paths, args.date)
    if args.cmd == "check":
        return cmd_check(args.country, args.out)
    return cmd_stats()


if __name__ == "__main__":
    sys.exit(main())
