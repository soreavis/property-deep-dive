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
import sys
from pathlib import Path

from regwatch_parse import REGWATCH_PATH, load


def parse(path: Path, days: int) -> list[tuple[str, str, str, str, str]]:
    """Walk regulatory-watch.md; return list of (iso2, effective, tier, topic, summary)."""
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=days)

    out: list[tuple[str, str, str, str, str]] = []
    for entry in load(path)[0]:
        # Strict YYYY-MM-DD only: a "(pending)" suffix means the reform has not landed,
        # and promotion fires when it does. `Entry.effective_date` deliberately tolerates
        # that suffix for the alert ladder, so parse the raw field here instead.
        try:
            effective = datetime.date.fromisoformat(entry.effective)
            tier_num = int(entry.tier)
        except ValueError:
            continue

        if tier_num not in (1, 2):
            continue
        if effective < cutoff or effective > today:
            # In the past beyond cutoff (already handled) OR future-dated (not yet effective)
            continue

        for iso in entry.isos:
            out.append((iso.lower(), entry.effective, entry.tier, entry.topic, entry.summary))

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
