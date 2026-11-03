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
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER_DIR = ROOT / "config" / "_evidence"
COUNTRIES = ROOT / "skills" / "property-deep-dive" / "countries"
FAST = ("price", "tax", "rental", "risks", "mains", "work", "cost benchmark")
# Lines whose figures are not claims about a source page: honest estimates, pointers and
# arithmetic (check-playbooks.py checks that) need no agent re-read.
SETTLED = re.compile(r"(~\s*est\.|\best\.|≈|\bverify (at|with)\b|data not publicly available|\bcomputed\b|curated wisdom)", re.I)
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
           "lines": {k: {"u": [remap[i] for i in e["u"]], "d": e["d"]} for k, e in sorted(led["lines"].items())}}
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
    added = 0
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
            led = ledgers[cc]
            for line in it["new"].splitlines():
                k = line_key(line)
                if k not in current[cc] or not salient_values(line):
                    continue  # superseded later, or no figure to re-check
                put(led, k, urls, date)
                added += 1
    for cc, led in ledgers.items():
        save(cc, led)
    print(f"ledgered {added} line-evidence pairs across {len(ledgers)} playbook(s)")
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


def check(cc: str, touch_date: str | None = None) -> dict:
    """Machine-check every fast-section line; with touch_date, re-date the confirmed entries.
    A line with no ledger entry is tried against the URLs it cites itself, else against the
    source-table rows whose name it mentions; a hit is ledgered."""
    led, lines = load(cc), playbook_lines(cc)
    named, rows = named_sources(lines), []
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
        elif covered:
            r["confirmed_values"] = [r["values"][i]["raw"] for i in sorted(covered)]
            r["missing_values"] = [v["raw"] for i, v in enumerate(r["values"]) if i not in covered]
    by: dict[str, dict] = {}
    for r in rows:
        by.setdefault(r["section"], {}).setdefault(r["status"], 0)
        by[r["section"]][r["status"]] += 1
    confirmed = [r for r in rows if r["status"] == "CONFIRMED"]
    if touch_date and confirmed:
        for r in confirmed:
            k = line_key(r["line"])
            if k in led["lines"]:
                led["lines"][k]["d"] = max(touch_date, led["lines"][k]["d"])
            else:
                put(led, k, r["urls"], touch_date)
        save(cc, led)
    return {"country": cc, "fast_lines": len(rows), "confirmed": len(confirmed), "by_section": by,
            "confirmed_rows": confirmed, "worklist": [r for r in rows if r["status"] != "CONFIRMED"]}


def put(led: dict, key: str, urls: list[str], date: str) -> None:
    idx = []
    for u in urls:
        if u not in led["urls"]:
            led["urls"].append(u)
        idx.append(led["urls"].index(u))
    prev = led["lines"].get(key)
    if prev and prev["d"] > date:
        return
    led["lines"][key] = {"u": sorted(set(idx) | set(prev["u"] if prev else [])), "d": date}


def add_confirmed_lines(cc: str, pairs: list[tuple[str, list[str]]], date: str) -> int:
    """Ledger lines an agent confirmed WITHOUT patching them, but only those whose figures a
    script re-reads together on the given page: agent claims never enter the ledger unchecked."""
    current = {line_key(l): l for _, l in playbook_lines(cc)}
    pairs = [(l, [u for u in urls if u.startswith("http")]) for l, urls in pairs if line_key(l) in current]
    fetches = fetch_all(u for _, urls in pairs for u in urls)
    led, n = load(cc), 0
    for line, urls in pairs:
        vals = salient_values(line)
        covered, _ = covered_values(vals, urls, fetches)
        if vals and len(covered) == len(SV.confirm_needles(vals)):
            put(led, line_key(line), urls, date)
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
