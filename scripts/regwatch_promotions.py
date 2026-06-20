#!/usr/bin/env python3
"""Parse regulatory-watch.md for recent Tier-1/2 entries and emit ISO2 codes
that should be promoted to Tier-A for the next refresh cycle.

Usage:
    python3 scripts/regwatch_promotions.py [--days 90]

Output: one line per promoted country in the form
    <iso2>\t<effective_date>\t<tier>\t<topic>\t<summary>

Promotion rule (from config/_tiers.json § promotion_rules):
- impact_tier in {1, 2}
- effective_date is a parseable YYYY-MM-DD within the last <days> days

Entries with suffix "(pending)" / "(in flight)" / non-parseable dates are skipped
(they're future-dated or estimated; promotion fires when they actually land).
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGWATCH_PATH = REPO_ROOT / "skills" / "property-deep-dive" / "shared" / "regulatory-watch.md"

# Multi-country header: extract every uppercase ISO2 token after a flag emoji
HEADER_ISO2 = re.compile(r"\b([A-Z]{2})\b")
# Bullet entry: - `<date> | <topic> | <summary> | <source> | <verified> | <revisit_by> | <tier> | <sections>`
BULLET = re.compile(r"^-\s+`([^`]+)`")


def parse(path: Path, days: int) -> list[tuple[str, str, str, str, str]]:
    """Walk regulatory-watch.md; return list of (iso2, effective, tier, topic, summary)."""
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=days)

    out: list[tuple[str, str, str, str, str]] = []
    current_isos: list[str] = []

    with path.open(encoding="utf-8") as f:
        for line in f:
            # Country header section
            if line.startswith("### "):
                # Stop at non-country headings (Recently enacted reforms / EU directives etc.)
                # Country headers always contain a flag emoji + 2-letter ISO2 token
                # Detect by presence of an ISO2 uppercase token and a flag-emoji-style codepoint
                if any(0x1F1E6 <= ord(c) <= 0x1F1FF for c in line):
                    current_isos = HEADER_ISO2.findall(line.split("###", 1)[1])
                else:
                    current_isos = []
                continue

            m = BULLET.match(line)
            if not m or not current_isos:
                continue

            fields = [s.strip() for s in m.group(1).split("|")]
            if len(fields) < 7:
                continue

            effective_raw = fields[0]
            topic = fields[1]
            summary = fields[2]
            tier = fields[6]

            # Skip parenthesised / range / non-strict-YYYY-MM-DD dates
            try:
                effective = datetime.date.fromisoformat(effective_raw)
            except ValueError:
                continue

            try:
                tier_num = int(tier)
            except ValueError:
                continue

            if tier_num not in (1, 2):
                continue
            if effective < cutoff or effective > today:
                # In the past beyond cutoff (already handled) OR future-dated (not yet effective)
                continue

            for iso in current_isos:
                out.append((iso.lower(), effective_raw, tier, topic, summary))

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=90, help="Look-back window (default: 90)")
    ap.add_argument("--path", type=Path, default=REGWATCH_PATH, help="Path to regulatory-watch.md")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"error: {args.path} not found", file=sys.stderr)
        return 1

    rows = parse(args.path, args.days)
    for iso2, effective, tier, topic, summary in rows:
        print(f"{iso2}\t{effective}\tT{tier}\t{topic}\t{summary[:80]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
