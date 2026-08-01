#!/usr/bin/env python3
"""Flag stale COUNTRY-count claims written in free prose.

The sister script `sync-docs.py` only rewrites counts inside `**N countries**`
bold/AUTOGEN markers. Counts written in ordinary sentences ("all 113 supported
countries", "100 of 103", "121 fully-populated") drift silently — that is how the
GitHub About blurb and ~11 doc sites went stale at the 103→121 expansion.

This guard greps tracked Markdown for country-count prose and classifies each hit:

  SCOPE   — "all N (supported) countries", "across N countries", "N fully-populated",
            "in all N countries", "N-country". These describe the whole corpus, so
            N MUST equal the canonical country count. A mismatch is an ERROR (exit 1).

  COVERAGE — "of N countries", "N of M countries". These are partial-coverage counts
            for a cross-cutting section and may legitimately be < corpus. Reported as
            a WARNING for human review (never auto-failed — see the scope-vs-count rule).

Excluded from scanning: CHANGELOG.md + ROADMAP.md and the archived changelog halves
under docs/changelog/** (all historical record — "all 109 supported countries" was
true when published and must not be rewritten to today's count), the country
playbooks under countries/** (populations, statute/article numbers), and the
hand-maintained country-matrix rows in SKILL.md (`| **xx** | ...`).

Usage:
    ./scripts/check-prose-counts.py            # report; exit 1 if any SCOPE mismatch
    ./scripts/check-prose-counts.py --check     # same (CI alias)
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COUNTRIES_DIR = ROOT / "skills" / "property-deep-dive" / "countries"

# Canonical country count = number of playbook directories.
CANON = sum(1 for p in COUNTRIES_DIR.iterdir() if p.is_dir())

EXCLUDE_FILES = {"CHANGELOG.md", "ROADMAP.md"}
EXCLUDE_PATH_PARTS = (
    "/countries/",        # playbooks carry populations + article numbers
    "/docs/changelog/",   # archived releases — frozen as published, same rule as CHANGELOG.md
)

# Number must look like a country count (avoid matching years, prices, statutes).
NUM = r"(?P<n>\b(?:9\d|1\d\d|2\d\d)\b)"  # 90-299
SCOPE_RES = [
    re.compile(rf"all {NUM}\s+(?:supported\s+)?countr", re.I),
    re.compile(rf"across\s+(?:all\s+)?{NUM}\s+(?:supported\s+)?countr", re.I),
    re.compile(rf"in all {NUM}\s+countr", re.I),
    re.compile(rf"{NUM}\s+supported countr", re.I),
    re.compile(rf"{NUM}\s+fully[- ]populated", re.I),
    re.compile(rf"{NUM}\s+in-scope countr", re.I),
]
# Two-number "M of N countries" — N is a coverage denominator to review (may be < corpus).
COVERAGE_RES = [
    re.compile(rf"\b\d+\s+of\s+{NUM}\s+countr", re.I),
]
# Skip when the number is a subset/approximate or a real-world nationality fact, not the corpus.
SKIP_BEFORE = re.compile(r"(?:~|≈|approximately|remaining|most|some|citizens of|nationals of|residents of)\s*$", re.I)


def _skip(line: str, start: int) -> bool:
    return bool(SKIP_BEFORE.search(line[max(0, start - 24):start]))
# country-matrix rows in SKILL.md
MATRIX_ROW = re.compile(r"^\|\s*\*\*[a-z]{2}\*\*\s*\|")


def tracked_md() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    return [ROOT / p for p in out]


def main() -> int:
    errors, warnings = [], []
    for md in tracked_md():
        rel = md.relative_to(ROOT).as_posix()
        if md.name in EXCLUDE_FILES or any(part in f"/{rel}" for part in EXCLUDE_PATH_PARTS):
            continue
        try:
            lines = md.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for i, line in enumerate(lines, 1):
            if MATRIX_ROW.match(line):
                continue
            for rx in SCOPE_RES:
                for m in rx.finditer(line):
                    if int(m.group("n")) != CANON and not _skip(line, m.start("n")):
                        errors.append((rel, i, m.group("n"), line.strip()[:130]))
            for rx in COVERAGE_RES:
                for m in rx.finditer(line):
                    if int(m.group("n")) != CANON and not _skip(line, m.start("n")):
                        warnings.append((rel, i, m.group("n"), line.strip()[:130]))

    print(f"Canonical country count: {CANON}\n")
    if warnings:
        print(f"⚠️  COVERAGE counts to review (may be intentionally partial) — {len(warnings)}:")
        for rel, i, n, snip in warnings:
            print(f"   {rel}:{i}  [{n}]  {snip}")
        print()
    if errors:
        print(f"❌ SCOPE-count mismatches (must equal {CANON}) — {len(errors)}:")
        for rel, i, n, snip in errors:
            print(f"   {rel}:{i}  [{n} → {CANON}]  {snip}")
        return 1
    print("✓ No stale scope-count prose.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
