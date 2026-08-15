#!/usr/bin/env python3
"""Drop feed matches that a recent feed-signal issue already reported.

`--window-days` in filter-feeds.py bounds staleness, not duplication: an item
published today keeps matching on every poll inside the window, and each poll
opened a fresh issue — one CJEU judgment and one EP adopted text each produced
three issues running (#302-#304, #317-#319). This filters the emitted match
blocks against what recent issues already carried.

A match answers to two identities, and either one being seen makes it a
duplicate. The link alone was not enough: EP plenary artefacts give one report's
debate, its votes and each sitting record their own URL under the same title, so
#375 carried 11 rows for a single file (A10-0025/2026). Titles are compared with
any trailing qualifier stripped — `(vote)`, `(debate)`, and the report reference
`(A10-0025/2026 - Rapporteur)`, which the sitting records carry and the debate
records omit. Qualifiers only ever trail, so a distinction carried in the title
body (a CJEU Opinion vs the Judgment in one case) still survives as its own row.

Run: python3 scripts/dedupe-feed-matches.py --matches _ci/matches.txt \
       --reported _ci/reported.txt
"""

from __future__ import annotations

import argparse
import re
import sys

HEADER_RE = re.compile(r"^- \*\*\[[^\]]+\]\*\* (.*)$")
LINK_RE = re.compile(r"<(https?://[^>\s]+)>")
EVENT_SUFFIX_RE = re.compile(
    r"\s*\((?:votes?|debates?|continuation|[ABC]\d{1,2}-\d{4}/\d{4}[^)]*)\)\s*$", re.I
)


def blocks(text: str) -> list[list[str]]:
    """Split filter-feeds output into one list of lines per match."""
    out: list[list[str]] = []
    for line in text.splitlines():
        if HEADER_RE.match(line):
            out.append([line])
        elif out:
            out[-1].append(line)
    return out


def title_key(title: str) -> str:
    """Normalised title, minus any trailing artefact or reference qualifiers."""
    text = " ".join(title.split())
    while True:
        stripped = EVENT_SUFFIX_RE.sub("", text)
        if stripped == text:
            return text.casefold()
        text = stripped


def keys(block: list[str]) -> set[str]:
    """Every identity this match answers to — its title and any links."""
    out = {title_key(HEADER_RE.match(block[0]).group(1))}
    out |= {m.group(1) for m in LINK_RE.finditer("\n".join(block))}
    return out


def reported_keys(text: str) -> set[str]:
    found = {m.group(1) for m in LINK_RE.finditer(text)}
    found |= {
        title_key(m.group(1))
        for m in (HEADER_RE.match(line) for line in text.splitlines())
        if m
    }
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matches", required=True)
    ap.add_argument("--reported", required=True)
    args = ap.parse_args()

    with open(args.matches, encoding="utf-8") as fh:
        found = blocks(fh.read())
    with open(args.reported, encoding="utf-8") as fh:
        seen = reported_keys(fh.read())

    fresh, collapsed, run_seen = [], 0, set()
    for block in found:
        identities = keys(block)
        if identities & seen:
            continue
        # Fold the rest of this run's artefacts for the same item in too, so one
        # file cannot open an issue carrying eleven rows of itself.
        if identities & run_seen:
            collapsed += 1
            continue
        fresh.append(block)
        run_seen |= identities

    for block in fresh:
        print("\n".join(block))

    print(
        f"dedupe: {len(found)} matched, "
        f"{len(found) - len(fresh) - collapsed} already reported, "
        f"{collapsed} same-item artefacts collapsed, {len(fresh)} new",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
