#!/usr/bin/env python3
"""Canonical parser for `shared/regulatory-watch.md` entries.

Three independent copies of this parser existed — in `regulatory-watch-revisit.yml`,
`transposition-alerts.yml` and `regwatch_promotions.py` — and all three shared one
defect: the entry regex was `^[-*]\\s+`([^`]+)`\\s*$`. The `[^`]+` class stops at the
first *nested* backtick, and entries routinely carry code spans inside their fields
(``Barbados Revenue Authority — `https://bra.gov.bb/` ``). Those lines failed the
closing-backtick anchor and were dropped with no warning: 27 of 394 entries, 8 of
them Tier-1, invisible to both schedulers. Six were already past their revisit date
while the revisit workflow reported "No overdue regulatory-watch entries" and closed
its own tracking issue.

The span therefore runs from the FIRST backtick on the line to the LAST. Every
consumer imports from here so the next fix lands in one place, and `--check` fails
CI if any bullet under a country header stops parsing.

Entry format (8 pipe-separated fields):

    - `effective | topic | summary | source | verified | revisit | tier | sections`

Run: python3 scripts/regwatch_parse.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGWATCH_PATH = REPO_ROOT / "skills" / "property-deep-dive" / "shared" / "regulatory-watch.md"

FIELD_COUNT = 8

# First backtick to last — NOT `[^`]+`, see module docstring.
ENTRY_RE = re.compile(r"^[-*]\s+`(.+)`\s*$")
# Anything that looks like it wants to be an entry, for the coverage guard.
BULLET_RE = re.compile(r"^[-*]\s+`")
HEADER_ISO2 = re.compile(r"\b([A-Z]{2})\b")
# A trailing "(XX)" in the sections field pins a multi-country entry to one country.
SECTIONS_ISO_RE = re.compile(r"\(([A-Z]{2})\)\s*$")
ISO_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})$")
# Effective dates may carry a parenthetical: "2026-01-01 (pending)".
EFFECTIVE_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})(?:\s*\(.*\))?$")


@dataclass(frozen=True)
class Entry:
    """One regulatory-watch row, already attributed to its country/countries."""

    line_no: int
    isos: tuple[str, ...]
    effective: str
    topic: str
    summary: str
    source: str
    verified: str
    revisit: str
    tier: str
    sections: str

    @property
    def revisit_date(self) -> date | None:
        """`revisit_by` as a date, or None for "(pending)"-style values."""
        return _to_date(self.revisit, ISO_DATE_RE)

    @property
    def effective_date(self) -> date | None:
        """`effective_date` as a date; tolerates a trailing parenthetical."""
        return _to_date(self.effective, EFFECTIVE_DATE_RE)


def _to_date(value: str, pattern: re.Pattern[str]) -> date | None:
    m = pattern.match(value)
    if not m:
        return None
    try:
        return date.fromisoformat(m.group(1))
    except ValueError:
        return None


def _is_country_header(line: str) -> bool:
    """A `### ` heading is a country header only if it carries a flag emoji.

    Section headings ("### Recently enacted reforms") also match the ISO2 regex,
    so the regional-indicator codepoints are what actually distinguish them.
    """
    return any(0x1F1E6 <= ord(c) <= 0x1F1FF for c in line)


def parse(text: str) -> tuple[list[Entry], list[tuple[int, str]]]:
    """Return (entries, unparsed) — `unparsed` is the coverage guard's input.

    A bullet is `unparsed` when it sits under a country header, opens with a
    backtick, and still fails to yield exactly FIELD_COUNT fields. Bullets
    outside a country header (the format spec at the top of the file) are not
    entries and are not reported.
    """
    entries: list[Entry] = []
    unparsed: list[tuple[int, str]] = []
    current_isos: list[str] = []

    for line_no, raw in enumerate(text.splitlines(), 1):
        if raw.startswith("### "):
            current_isos = (
                HEADER_ISO2.findall(raw.split("###", 1)[1]) if _is_country_header(raw) else []
            )
            continue
        if raw.startswith("#"):
            # Any other heading level ends the country's entry block — otherwise the
            # last country stays "current" through the file's trailing prose and the
            # "Related files" bullets get audited as malformed entries.
            current_isos = []
            continue
        if not current_isos or not BULLET_RE.match(raw):
            continue

        m = ENTRY_RE.match(raw)
        if not m:
            unparsed.append((line_no, raw.strip()))
            continue
        parts = [p.strip() for p in m.group(1).split("|")]
        if len(parts) != FIELD_COUNT:
            unparsed.append((line_no, raw.strip()))
            continue

        m_tag = SECTIONS_ISO_RE.search(parts[7])
        isos = [m_tag.group(1)] if m_tag and m_tag.group(1) in current_isos else current_isos
        entries.append(
            Entry(
                line_no=line_no,
                isos=tuple(isos),
                effective=parts[0],
                topic=parts[1],
                summary=parts[2],
                source=parts[3],
                verified=parts[4],
                revisit=parts[5],
                tier=parts[6],
                sections=parts[7],
            )
        )

    return entries, unparsed


def load(path: Path = REGWATCH_PATH) -> tuple[list[Entry], list[tuple[int, str]]]:
    return parse(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="fail if any entry does not parse")
    ap.add_argument("--path", type=Path, default=REGWATCH_PATH)
    args = ap.parse_args()

    entries, unparsed = load(args.path)
    print(f"{len(entries)} entries parsed from {args.path.name}")

    if unparsed:
        print(f"\n{len(unparsed)} bullet(s) under a country header did NOT parse:", file=sys.stderr)
        for line_no, raw in unparsed:
            print(f"  L{line_no}: {raw[:160]}", file=sys.stderr)
        print(
            f"\nEvery entry must be a single backtick span of {FIELD_COUNT} pipe-separated fields:"
            "\n  - `effective | topic | summary | source | verified | revisit | tier | sections`"
            "\nAn unparsed entry is invisible to the revisit and transposition schedulers.",
            file=sys.stderr,
        )
        return 1 if args.check else 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
