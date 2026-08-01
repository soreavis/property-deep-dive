#!/usr/bin/env python3
"""Cap the length of CHANGELOG bullets under [Unreleased].

CHANGELOG.md reached 512 KB across only 946 lines and 14 releases — roughly
540 bytes per line. The driver was never the number of releases; it was entry
length. At the time this guard was written the median bullet was 288 chars but
p75 was 1,268, p90 was 2,467, and the longest single bullet was 13,073 — a
research report living in a changelog.

The detail is not wasted, it is just in the wrong place: it belongs in the PR
body, which is permanent, linked from the squash commit, and does not get
re-read by everyone scanning for "what changed". A changelog bullet should say
what changed and why it matters, and stop.

Scope is deliberately narrow:

  * Only the `## [Unreleased]` section is checked. Released sections are
    historical record — rewriting them would be lying about what was published,
    and grandfathering keeps this guard from failing on 227 legacy bullets.
  * Only top-level `- ` bullets are measured. Nested list items, tables, and
    fenced blocks are exempt: a long table row is a formatting choice, not prose
    sprawl.

Usage:
    ./scripts/check-changelog-length.py             # report; exit 1 if any bullet is over
    ./scripts/check-changelog-length.py --check     # same (CI alias)
    ./scripts/check-changelog-length.py --max 800   # override the cap
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

CHANGELOG = Path(__file__).resolve().parent.parent / 'CHANGELOG.md'
DEFAULT_MAX = 600


def unreleased_bullets(text: str) -> list[tuple[int, str]]:
    """Return (1-indexed line number, bullet) for top-level bullets in [Unreleased]."""
    bullets: list[tuple[int, str]] = []
    in_section = False
    in_fence = False

    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.startswith('## '):
            # Any other `## [...]` heading ends the Unreleased section.
            in_section = line.strip() == '## [Unreleased]'
            continue
        if not in_section:
            continue
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith('- '):
            bullets.append((lineno, line))

    return bullets


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true', help='CI alias; behaviour is identical')
    ap.add_argument('--max', type=int, default=DEFAULT_MAX, dest='max_len')
    args = ap.parse_args()

    if not CHANGELOG.exists():
        print(f'ERROR: {CHANGELOG} not found', file=sys.stderr)
        return 1

    bullets = unreleased_bullets(CHANGELOG.read_text(encoding='utf-8'))
    over = [(n, b) for n, b in bullets if len(b) > args.max_len]

    print(f'[Unreleased] bullets: {len(bullets)}   cap: {args.max_len} chars')

    if not over:
        if bullets:
            print(f'longest: {max(len(b) for _, b in bullets)} chars')
        print('✓ All within cap.')
        return 0

    print(f'\n❌ {len(over)} bullet(s) over the cap:\n')
    for lineno, bullet in over:
        print(f'  CHANGELOG.md:{lineno}  {len(bullet)} chars (+{len(bullet) - args.max_len})')
        print(f'    {bullet[:100]}…\n')

    print('Trim to what changed and why it matters; move the investigation, evidence')
    print('and command output to the PR body — it is permanent and linked from the')
    print('squash commit. Released sections are exempt; this only checks [Unreleased].')
    return 1


if __name__ == '__main__':
    sys.exit(main())
