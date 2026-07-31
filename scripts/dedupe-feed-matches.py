#!/usr/bin/env python3
"""Drop feed matches that a recent feed-signal issue already reported.

`--window-days` in filter-feeds.py bounds staleness, not duplication: an item
published today keeps matching on every poll inside the window, and each poll
opened a fresh issue — one CJEU judgment and one EP adopted text each produced
three issues running (#302-#304, #317-#319). This filters the emitted match
blocks against the links already carried by recent issues.

Run: python3 scripts/dedupe-feed-matches.py --matches _ci/matches.txt \
       --reported _ci/reported.txt
"""

from __future__ import annotations

import argparse
import re
import sys

HEADER_RE = re.compile(r"^- \*\*\[[^\]]+\]\*\* (.*)$")
LINK_RE = re.compile(r"<(https?://[^>\s]+)>")


def blocks(text: str) -> list[list[str]]:
    """Split filter-feeds output into one list of lines per match."""
    out: list[list[str]] = []
    for line in text.splitlines():
        if HEADER_RE.match(line):
            out.append([line])
        elif out:
            out[-1].append(line)
    return out


def key(block: list[str]) -> str:
    """Link if the feed gave one, else the normalised title."""
    link = LINK_RE.search("\n".join(block))
    if link:
        return link.group(1)
    return " ".join(HEADER_RE.match(block[0]).group(1).split()).casefold()


def reported_keys(text: str) -> set[str]:
    keys = {m.group(1) for m in LINK_RE.finditer(text)}
    keys |= {key([line]) for line in text.splitlines() if HEADER_RE.match(line)}
    return keys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matches", required=True)
    ap.add_argument("--reported", required=True)
    args = ap.parse_args()

    with open(args.matches, encoding="utf-8") as fh:
        found = blocks(fh.read())
    with open(args.reported, encoding="utf-8") as fh:
        seen = reported_keys(fh.read())

    fresh = [b for b in found if key(b) not in seen]
    for block in fresh:
        print("\n".join(block))

    print(
        f"dedupe: {len(found)} matched, {len(found) - len(fresh)} already reported, "
        f"{len(fresh)} new",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
