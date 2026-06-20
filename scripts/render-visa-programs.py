#!/usr/bin/env python3
"""Render config/_visa-programs.json into the AUTOGEN block of
skills/property-deep-dive/shared/visa-programs.md.

Idempotent: running twice produces the same file.

Usage:
    python3 scripts/render-visa-programs.py            # write changes
    python3 scripts/render-visa-programs.py --check    # exit 1 if changes would be made
    python3 scripts/render-visa-programs.py --diff     # print diff, no write

Used by:
- .github/workflows/visa-programs-audit.yml in --check mode on every PR
- Manually after JSON edits

Source of truth: config/_visa-programs.json
"""
from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_FILE = REPO_ROOT / "config" / "_visa-programs.json"
MD_FILE = REPO_ROOT / "skills" / "property-deep-dive" / "shared" / "visa-programs.md"

START_MARK = "<!-- AUTOGEN-START: region-tables -->"
END_MARK = "<!-- AUTOGEN-END: region-tables -->"

COLS = [
    ("country", "Country"),
    ("programme", "Programme"),
    ("status", "Status"),
    ("min_threshold", "Min. threshold"),
    ("property_linked", "Property-linked?"),
    ("pr_citizenship", "PR/citizenship"),
    ("caveats", "Caveats"),
]


def render_block(programs: list[dict]) -> str:
    """Render the region-grouped tables block (without the AUTOGEN markers)."""
    # Preserve first-seen region order from the JSON
    regions: list[str] = []
    seen: set[str] = set()
    for p in programs:
        r = p.get("region") or ""
        if r and r not in seen:
            regions.append(r)
            seen.add(r)

    by_region: dict[str, list[dict]] = {r: [] for r in regions}
    for p in programs:
        r = p.get("region") or ""
        if r in by_region:
            by_region[r].append(p)

    def fmt_row(values: list[str]) -> str:
        # Empty cells render as `| |` (single space) to match the source markdown
        return "|" + "|".join(f" {v} " if v else " " for v in values) + "|"

    out_lines: list[str] = []
    for r in regions:
        out_lines.append(f"### {r}")
        out_lines.append("")
        out_lines.append(fmt_row([c[1] for c in COLS]))
        out_lines.append("|" + "|".join("---" for _ in COLS) + "|")
        for p in by_region[r]:
            row = [p.get(k, "") for k, _ in COLS]
            row[0] = row[0].upper()
            out_lines.append(fmt_row(row))
        out_lines.append("")
    return "\n".join(out_lines).rstrip() + "\n"


def splice(md: str, new_block: str) -> str:
    if START_MARK not in md or END_MARK not in md:
        raise SystemExit(
            f"AUTOGEN markers missing in {MD_FILE.relative_to(REPO_ROOT)}.\n"
            f"Insert '{START_MARK}' and '{END_MARK}' around the region-tables section first."
        )
    pre, _, rest = md.partition(START_MARK)
    _, _, post = rest.partition(END_MARK)
    return f"{pre}{START_MARK}\n\n{new_block}\n{END_MARK}{post}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if file would change")
    ap.add_argument("--diff", action="store_true", help="print diff, do not write")
    args = ap.parse_args()

    payload = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    block = render_block(payload["programs"])

    current = MD_FILE.read_text(encoding="utf-8")
    rendered = splice(current, block)

    if rendered == current:
        print("✓ visa-programs.md is in sync with config/_visa-programs.json")
        return 0

    if args.diff:
        diff = difflib.unified_diff(
            current.splitlines(keepends=True),
            rendered.splitlines(keepends=True),
            fromfile=str(MD_FILE.relative_to(REPO_ROOT)),
            tofile=str(MD_FILE.relative_to(REPO_ROOT)) + " (rendered)",
        )
        sys.stdout.writelines(diff)
        return 1 if args.check else 0

    if args.check:
        print(
            "✗ visa-programs.md is out of sync with config/_visa-programs.json.\n"
            "  Run: python3 scripts/render-visa-programs.py",
            file=sys.stderr,
        )
        return 1

    MD_FILE.write_text(rendered, encoding="utf-8")
    print(f"✓ Updated {MD_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
