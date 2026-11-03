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
                idx = []
                for u in urls:
                    if u not in led["urls"]:
                        led["urls"].append(u)
                    idx.append(led["urls"].index(u))
                prev = led["lines"].get(k)
                if prev and prev["d"] > date:
                    continue
                led["lines"][k] = {"u": sorted(set(idx) | set(prev["u"] if prev else [])), "d": date}
                added += 1
    for cc, led in ledgers.items():
        save(cc, led)
    print(f"ledgered {added} line-evidence pairs across {len(ledgers)} playbook(s)")
    return 0


def check(cc: str, touch_date: str | None = None) -> dict:
    """Machine-check every fast-section line; with touch_date, re-date the confirmed entries."""
    led, sv = load(cc), SV.load_sv_config()
    rows = []
    for section, line in playbook_lines(cc):
        vals = salient_values(line)
        if not vals or not any(k in section.lower() for k in FAST):
            continue
        e = led["lines"].get(line_key(line))
        if not e and SETTLED.search(line):
            continue
        rows.append({"section": section, "line": line.strip(), "values": vals,
                     "urls": [led["urls"][i] for i in e["u"]] if e else [], "ledger_date": e["d"] if e else None})
    urls = sorted({u for r in rows for u in r["urls"]})
    fetches = asyncio.run(SV.fetch_unique(urls, SV.UL.load_config(SV.UL.read_plugin_version()), sv)) if urls else {}
    for r in rows:
        r["status"] = "NO_EVIDENCE" if not r["urls"] else "NOT_CONFIRMED"
        needles = [v["needles"] for v in r["values"]]
        if not r["urls"] or not any(SV._is_strong(n) for v in needles for n in v):
            continue
        covered: set[int] = set()
        for u in r["urls"]:
            fr = fetches.get(u)
            r.setdefault("fetch", {})[u] = fr.status if fr else "NOT_FETCHED"
            if not (fr and fr.status == "OK"):
                continue
            found = [i for i, v in enumerate(needles) if any(n in fr.text for n in v)]
            span = SV.min_cover_span(fr.text, [needles[i] for i in found]) if found else None
            if span is not None and span <= SV.COVER_WINDOW:
                covered |= set(found)  # this page holds its share of the line's figures together
        if len(covered) == len(needles):
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
            led["lines"][line_key(r["line"])]["d"] = max(touch_date, led["lines"][line_key(r["line"])]["d"])
        save(cc, led)
    return {"country": cc, "fast_lines": len(rows), "confirmed": len(confirmed), "by_section": by,
            "confirmed_rows": confirmed, "worklist": [r for r in rows if r["status"] != "CONFIRMED"]}


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
