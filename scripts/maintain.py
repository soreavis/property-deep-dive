#!/usr/bin/env python3
"""Maintenance driver: scripts do every step that needs no judgment, agents get only what is left.

    python3 scripts/maintain.py plan --countries fi,rs --date 2026-12-01 --out DIR
        Machine-check every fast-section line against the evidence ledger, refresh the ledger
        date of each confirmed line, and write DIR/<iso2>.json (worklist per cluster) plus
        DIR/plan.json — the Workflow input, listing ONLY clusters that still have lines to
        research. A cluster whose lines all re-confirmed gets no agent at all.
    python3 scripts/maintain.py precheck PATCHES.json
        For the refuter: re-read each patch's figures on its own evidence pages (no tokens) and
        print which patches are machine-confirmed, so it re-fetches only the rest.
    python3 scripts/maintain.py apply RESULT.json --date 2026-12-01 --plan DIR
        Apply the settled patches, ledger their evidence, and write each playbook's footer:
        Per-section verification rows for closed sections, an Update history bullet, and the
        playbook-level stamp = the OLDEST fast-section date once every fast section is dated
        (scripts/check-playbooks.py enforces the same rule in CI).

Workflow: scripts/workflows/pdd-maintain.js (research + refute per cluster; no stamp agents).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent / file)
    mod = sys.modules[name] = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


EL = _load("evidence_ledger", "evidence-ledger.py")
PV = _load("provenance", "provenance.py")
SV = EL.SV
CLUSTERS = {"market": ("price", "rental", "work"), "tax-legal": ("tax", "cost benchmark"), "risk-infra": ("risks", "mains")}
TABLE_HEAD = "### Per-section verification (overrides playbook-level date)"
STAMP_LINE = "✅ Fast-changing sections re-verified as of {d}; each section's date is in the Per-section verification table."
AGENT_LINES = 40
HOLD = ("ungrounded", "near miss", "quote not on page")
RUN_TALK = re.compile(r"worklist|confirmed_lines|refuter|line_errors|check-playbooks|ledger|\bpatch|old string", re.I)
DEFAULT_NOTE = "Figures re-read on their sources or labelled."


def fast_key(name: str) -> str | None:
    """`--work=<profession>` → work, `Cost benchmarks (FI 2026)` → cost benchmark. Keyed on the
    leading token so `--rental / Tax on rental` is rental, not tax."""
    m = re.match(r"\s*(?:Section:\s*)?`--([a-z]+)", name)
    if m:
        return m[1] if m[1] in sum(CLUSTERS.values(), ()) else None
    return "cost benchmark" if name.strip().lower().startswith("cost benchmark") else None


def cluster_of(key: str) -> str:
    return next(c for c, keys in CLUSTERS.items() if key in keys)


def fast_sections(text: str) -> dict[str, str]:
    """fast key → section heading text (without `Section:`), in playbook order, Status excluded."""
    body = text[:text.find("\n## Status")] if "\n## Status" in text else text
    out = {}
    for h in re.findall(r"^## (.+?)\s*$", body, re.M):
        k = fast_key(h)
        if k and k not in out:
            out[k] = re.sub(r"^Section:\s*", "", h)
    return out


# ── plan ─────────────────────────────────────────────────────────────────────
def pack(clusters: dict[str, dict]) -> dict[str, dict]:
    """First-fit decreasing into agents of at most AGENT_LINES lines. Measured on the first
    pipeline run, an agent costs about 510k weighted tokens before its first line and 11k per
    line, so fewer, fuller agents win until the context limit bites."""
    bins: list[dict] = []
    for name, c in sorted(clusters.items(), key=lambda kv: -len(kv[1]["lines"])):
        b = next((b for b in bins if len(b["lines"]) + len(c["lines"]) <= AGENT_LINES), None)
        if b:
            b["name"] += f"+{name}"
            b["sections"] += c["sections"]
            b["lines"] += c["lines"]
        else:
            bins.append({"name": name, **c})
    return {b.pop("name"): b for b in bins}


def cmd_plan(codes: list[str], date: str, out: Path, max_risk: float) -> int:
    out.mkdir(parents=True, exist_ok=True)
    plan, totals = [], [0, 0, 0]
    for cc in codes:
        res = EL.check(cc, touch_date=date, max_risk=max_risk)
        by_cluster: dict[str, dict] = {}
        for r in res["worklist"]:
            k = fast_key(r["section"])
            if k:
                c = by_cluster.setdefault(cluster_of(k), {"sections": [], "lines": []})
                if r["section"] not in c["sections"]:
                    c["sections"].append(r["section"])
                c["lines"].append({x: r[x] for x in ("section", "line", "status", "urls", "confirmed_values",
                                                     "missing_values", "audit", "expired", "hints") if r.get(x)})
        by_cluster = pack(by_cluster)
        fresh: dict[str, str] = {}
        for r in res["fresh"]:
            k = fast_key(r["section"])
            if k:
                fresh[k] = min(fresh.get(k, r["proved"]), r["proved"])
        (out / f"{cc}.json").write_text(json.dumps({"country": cc, "date": date, "clusters": by_cluster, "fresh": fresh,
                                                    "machine_confirmed": res["by_section"]}, ensure_ascii=False, indent=1))
        plan += [{"code": cc, "cluster": c, "sections": v["sections"], "lines": len(v["lines"])} for c, v in by_cluster.items()]
        totals[0] += res["fast_lines"]; totals[1] += res["confirmed"]; totals[2] += len(res["fresh"])
        print(f"{cc}: {res['confirmed']}/{res['fast_lines']} confirmed by script ({res['unchanged']} on unchanged pages), "
              f"{len(res['fresh'])} freshly proved; agents: {', '.join(f'{c} ({len(v['lines'])})' for c, v in by_cluster.items()) or 'none'}")
    (out / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(f"total: {totals[1]}/{totals[0]} confirmed by script, {totals[2]} freshly proved, "
          f"{sum(p['lines'] for p in plan)} lines for {len(plan)} research agent(s)")
    return 0


# ── precheck ─────────────────────────────────────────────────────────────────
def cmd_precheck(path: Path) -> int:
    items = json.loads(path.read_text())
    fetches = EL.fetch_all(e["url"] for it in items for e in it.get("evidence", []) if str(e.get("url", "")).startswith("http"))
    for i, it in enumerate(items):
        vals = [v for line in it["new"].splitlines() for v in EL.salient_values(line)]
        urls = [e["url"] for e in it.get("evidence", []) if e.get("url") in fetches]
        covered, _ = EL.covered_values(vals, urls, fetches)
        ok = bool(vals) and len(covered) == len(SV.confirm_needles(vals))
        flags = "; ".join(f"{f['kind']}: {f['figure']} {f.get('page_has') or ''}".strip() for f in PV.audit_patch(it, fetches)["findings"])
        print(f"{i}\t{'FLAGGED' if flags else 'MACHINE_CONFIRMED' if ok else 'REFETCH'}\t{it.get('section', '')[:40]}\t{flags}")
    return 0


# ── apply ────────────────────────────────────────────────────────────────────
def apply_items(items: list[dict]) -> tuple[int, list[dict]]:
    cache: dict[Path, str] = {}
    applied, conflicts = 0, []
    for it in items:
        rel = re.sub(r"^.*?(skills/property-deep-dive/)", r"\1", it["file"])
        if rel.startswith("/") or ".." in rel.split("/"):
            sys.exit(f"refusing path outside the repo: {it['file']}")
        p = ROOT / rel
        text = cache.setdefault(p, p.read_text(encoding="utf-8"))
        n = text.count(it["old"])
        if n == 1:
            cache[p] = text.replace(it["old"], it["new"])
            applied += 1
        elif not (n == 0 and it["new"] in text):
            conflicts.append({**it, "why": f"old occurs {n}x"})
    for p, t in cache.items():
        p.write_text(t, encoding="utf-8")
    return applied, conflicts


def upsert_rows(text: str, rows: dict[str, str]) -> str:
    """rows: fast key → full table row. Replaces the row of the same section, appends new ones,
    and creates the table at the end of the Status section when the playbook has none."""
    if TABLE_HEAD.split(" (")[0] not in text:
        s = text.find("\n## Status")
        nxt = text.find("\n## ", s + 1)
        nxt = len(text) if nxt < 0 else nxt
        table = f"\n\n{TABLE_HEAD}\n\n| Section | Last verified | Verifier | Notes |\n|---|---|---|---|\n"
        text = text[:nxt].rstrip("\n") + table + text[nxt:]
    head = text.find("### Per-section verification")
    lines = text[head:].split("\n")
    i = next(j for j, l in enumerate(lines) if l.startswith("|---"))
    end = i + 1
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    body = lines[i + 1:end]
    for k, row in rows.items():
        hit = [j for j, l in enumerate(body) if fast_key(l.strip("| ").split("|")[0]) == k]
        if hit:
            body[hit[0]] = row
            for j in reversed(hit[1:]):
                del body[j]
        else:
            body.append(row)
    return text[:head] + "\n".join(lines[:i + 1] + body + lines[end:])


def reader_note(note: str) -> str:
    """Section notes come from agents: keep the sentences about the facts, drop those about the run."""
    kept = [s for s in re.split(r"(?<=[.;])\s+", note) if not RUN_TALK.search(s)]
    return " ".join(kept).replace("|", "/").strip() or DEFAULT_NOTE


def section_dates(text: str) -> dict[str, str]:
    """A `--price` › Listings row dates that subsection, not the section."""
    head = text.find("### Per-section verification")
    out = {}
    if head < 0:
        return out
    for l in text[head:].split("\n")[1:]:
        if l.startswith("|"):
            cells = [c.strip() for c in l.strip("|").split("|")]
            k = fast_key(cells[0])
            if k and "›" not in cells[0] and len(cells) > 1 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[1]):
                out[k] = min(out.get(k, cells[1]), cells[1])
        elif out:
            break
    return out


def add_history(text: str, bullet: str) -> str:
    m = re.search(r"^## Update history\s*\n", text, re.M)
    if m:
        nxt = text.find("\n## ", m.end())
        nxt = len(text) if nxt < 0 else nxt
        return text[:nxt].rstrip("\n") + "\n" + bullet + "\n" + text[nxt:]
    m = re.search(r"^\*\*Update history\*\*:?\s*\n", text, re.M)
    if m:
        lines, pos = text[m.end():].split("\n"), 0
        while pos < len(lines) and (lines[pos].startswith(("- ", "  -")) or not lines[pos].strip() and pos == 0):
            pos += 1
        return text[:m.end()] + "\n".join(lines[:pos] + [bullet] + lines[pos:])
    return text.rstrip("\n") + f"\n\n## Update history\n\n{bullet}\n"


def restamp(text: str) -> tuple[str, str | None]:
    """Playbook date = oldest fast-section date, once every fast section has one and it is
    newer than the footer's current first stamp."""
    keys, dates = fast_sections(text), section_dates(text)
    if not keys or any(k not in dates for k in keys):
        return text, None
    d = min(dates[k] for k in keys)
    s = text.find("\n## Status")
    cur = re.search(r"(?:as of +|\*\*Last verified\*\*: *)(\d{4}-\d{2}-\d{2})", text[s:])
    if cur and cur[1] >= d:
        return text, None
    body = text[s + len("\n## Status"):]
    line = STAMP_LINE.format(d=d)
    if body.lstrip("\n").startswith("✅ Fast-changing sections re-verified as of"):
        body = re.sub(r"✅ Fast-changing sections re-verified as of [^\n]*", line, body, count=1)
    else:
        body = "\n\n" + line + "\n\n" + body.lstrip("\n")
    return text[:s] + "\n## Status" + body, d


NUMBER = re.compile(r"\d{1,3}(?:[,\u00a0\u202f]\d{3})+|\d{3,}")
ANCHOR = re.compile(r"\b[A-Z][a-zà-ÿ]{3,}\b")


def numbers(text: str) -> set[int]:
    return {int(re.sub(r"\D", "", n)) for n in NUMBER.findall(text)}


def roundings(n: int) -> set[int]:
    """14489 → {14489, 14490, 14500, 14000}: the forms a restatement elsewhere may round it to,
    down to two significant digits."""
    return {n} | {round(n, -k) for k in range(1, len(str(n)) - 1)}


def restatements(items: list[dict], text: str) -> list[dict]:
    """Lines still quoting a figure a patch replaced, exactly or rounded, and naming the same
    thing (a shared capitalised word). A changed figure that survives elsewhere contradicts it."""
    found = []
    for it in items:
        gone = numbers(it["old"]) - numbers(it["new"])
        anchors = set(ANCHOR.findall(it["old"]))
        forms = {f for n in gone if n >= 1000 for f in roundings(n)}
        for line in text.splitlines():
            if forms & numbers(line) and anchors & set(ANCHOR.findall(line)) and line not in it["new"]:
                found.append({"file": it["file"], "replaced": sorted(gone), "line": line.strip()})
    return found


def render_footer(cc: str, date: str, sections: list[dict], plan_dir: Path) -> str | None:
    p = EL.COUNTRIES / cc / "playbook.md"
    text = p.read_text(encoding="utf-8")
    keys = fast_sections(text)
    planned = json.loads((plan_dir / f"{cc}.json").read_text()) if (plan_dir / f"{cc}.json").exists() else {"clusters": {}}
    fresh = planned.get("fresh", {})
    researched = {fast_key(s) for c in planned["clusters"].values() for s in c["sections"]}
    rows, closed, still_open = {}, [], []
    for k, name in keys.items():
        s = next((x for x in sections if fast_key(x["section"]) == k), None)
        if k not in researched or (s and s.get("closed")):
            note = reader_note(s["note"]) if s else "Every figure re-read on its recorded source, or the source unchanged."
            rows[k] = f"| {name} | {min(date, fresh.get(k, date))} | {date} maintenance run | {note} |"
            closed.append(name)
        elif k in researched:
            still_open.append(name)
    if not rows:
        return None
    text = upsert_rows(text, rows)
    text, d = restamp(text)
    text = add_history(text, f"- **{date}** — Maintenance run: closed {', '.join(closed)}"
                             + (f"; still open {', '.join(still_open)}" if still_open else "")
                             + (f". Playbook-level date now {d}." if d else "."))
    p.write_text(text, encoding="utf-8")
    return d


def report_audit(items: list[dict], plan_dir: Path) -> None:
    """Change-rate estimate from the audit sample, to compare with EL.CHANGE_RATE_PER_DAY."""
    plans = [json.loads(f.read_text()) for f in plan_dir.glob("??.json")]
    ages = {EL.line_key(l["line"]): l["audit"] for p in plans for c in p["clusters"].values() for l in c["lines"] if l.get("audit")}
    if ages:
        changed = {EL.line_key(l) for it in items if it["kind"] == "fact-changed" for l in it["old"].splitlines()} & set(ages)
        n, x = len(ages), len(changed)
        rate = -math.log((n - x + 0.5) / (n + 0.5)) / (sum(ages.values()) / n)
        print(f"audit sample: {x} of {n} freshly proved lines changed, {rate:.5f}/day against {EL.CHANGE_RATE_PER_DAY}/day in use")


def hold_ungrounded(res: dict, items: list[dict]) -> tuple[list[dict], list[dict]]:
    """A patch whose new figures no evidence page shows stays out, unless the refuter says it read
    them itself, and its section stays open, so the line returns to the next run."""
    fetches = EL.fetch_all(e["url"] for i in items for e in i.get("evidence", []) if str(e.get("url", "")).startswith("http"))
    kept, held = [], []
    for it in items:
        bad = [] if it.get("flag_cleared") else [f for f in PV.audit_patch(it, fetches)["findings"] if f["kind"] in HOLD]
        (held if bad else kept).append({**it, "findings": bad} if bad else it)
    open_keys = {(h["file"], fast_key(h["section"])) for h in held}
    for p in res["playbooks"]:
        for c in p["clusters"]:
            files = {i["file"] for i in c["items"]}
            for s in c.get("sections", []):
                if any((f, fast_key(s["section"])) in open_keys for f in files):
                    s["closed"] = False
    return kept, held


def cmd_apply(result: Path, date: str, plan_dir: Path) -> int:
    res = json.loads(result.read_text())
    res = res.get("result", res)
    items = [i for p in res["playbooks"] for c in p["clusters"] for i in c["items"] if i.get("status") != "DROP"]
    items, held = hold_ungrounded(res, items)
    (result.parent / "held.json").write_text(json.dumps(held, ensure_ascii=False, indent=1))
    print(f"held {len(held)} patch(es) with figures no evidence page shows (→ {result.parent / 'held.json'})")
    applied, conflicts = apply_items(items)
    (result.parent / "conflicts.json").write_text(json.dumps(conflicts, ensure_ascii=False, indent=1))
    print(f"applied {applied}, conflicts {len(conflicts)} (→ {result.parent / 'conflicts.json'})")
    report_audit(items, plan_dir)
    follow = [f for p in res["playbooks"] for f in restatements(
        [i for c in p["clusters"] for i in c["items"] if i.get("status") != "DROP" and i["kind"] == "fact-changed"],
        (EL.COUNTRIES / p["code"] / "playbook.md").read_text(encoding="utf-8"))]
    (result.parent / "followups.json").write_text(json.dumps(follow, ensure_ascii=False, indent=1))
    print(f"{len(follow)} line(s) may still quote a replaced figure (→ {result.parent / 'followups.json'})")
    EL.cmd_add([result], date)
    for p in res["playbooks"]:
        pairs = [(c["line"], c["urls"]) for cl in p["clusters"] for c in cl.get("confirmed_lines", [])]
        if pairs:
            print(f"{p['code']}: ledgered {EL.add_confirmed_lines(p['code'], pairs, date)} of {len(pairs)} confirmed-unchanged lines")
    codes = {p["code"] for p in res["playbooks"]} | {json.loads(f.read_text())["country"]
                                                       for f in plan_dir.glob("*.json") if f.name != "plan.json"}
    for cc in sorted(codes):
        secs = [s for p in res["playbooks"] if p["code"] == cc for c in p["clusters"] for s in c.get("sections", [])]
        d = render_footer(cc, date, secs, plan_dir)
        print(f"{cc}: footer written{f', playbook date {d}' if d else ''}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("plan")
    a.add_argument("--countries", required=True)
    a.add_argument("--date", required=True)
    a.add_argument("--out", type=Path, required=True)
    a.add_argument("--max-risk", type=float, default=0.10, help="skip a proved line while P(changed since) stays under this")
    b = sub.add_parser("precheck")
    b.add_argument("patches", type=Path)
    c = sub.add_parser("apply")
    c.add_argument("result", type=Path)
    c.add_argument("--date", required=True)
    c.add_argument("--plan", type=Path, required=True)
    args = ap.parse_args()
    if args.cmd == "plan":
        return cmd_plan(args.countries.split(","), args.date, args.out, args.max_risk)
    if args.cmd == "precheck":
        return cmd_precheck(args.patches)
    return cmd_apply(args.result, args.date, args.plan)


if __name__ == "__main__":
    sys.exit(main())
