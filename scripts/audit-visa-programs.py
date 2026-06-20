#!/usr/bin/env python3
"""Audit country playbooks for visa-program claims that contradict the
source-of-truth registry in config/_visa-programs.json.

The registry holds machine-readable status per programme. This script flags
any country playbook that names an ENDED / SUSPENDED / NEVER-LAUNCHED
programme without acknowledging that status. Catches drift mechanically
when a regulatory-watch entry lands in JSON but the matching playbook prose
hasn't been patched yet.

The match rule is intentionally loose: we look for the canonical programme
name (case-insensitive substring) in the playbook for that ISO2. If found,
we require an explicit status marker nearby (ENDED / CLOSED / SUSPENDED /
ABOLISHED / REPEALED / RULED ILLEGAL / NEVER OFFERED / PROPOSED) within a
configurable window of characters around the match. Missing → flag.

Usage:
    python3 scripts/audit-visa-programs.py             # audit all playbooks
    python3 scripts/audit-visa-programs.py --iso=pt    # one country
    python3 scripts/audit-visa-programs.py --warn-only # exit 0 even on failure

Exits 1 if any unacknowledged claim is found.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_FILE = REPO_ROOT / "config" / "_visa-programs.json"
PLAYBOOKS_DIR = REPO_ROOT / "skills" / "property-deep-dive" / "countries"

# Status values that demand explicit acknowledgement when the programme name
# appears in a country playbook.
NEEDS_ACK = (
    "ENDED",
    "CLOSED",
    "SUSPENDED",
    "RULED ILLEGAL",
    "NEVER LAUNCHED",
    "NEVER OFFERED",
    "PROPOSED",
    "REPEALED",
    "ABOLISHED",
    "PHASING OUT",
    "REDESIGN ANNOUNCED",
)

# Acknowledgement tokens we accept near the programme mention.
ACK_PATTERNS = (
    r"\bENDED\b",
    r"\bCLOSED\b",
    r"\bSUSPENDED\b",
    r"\bABOLISHED\b",
    r"\bREPEALED\b",
    r"\bILLEGAL\b",
    r"\bNEVER\s+(?:OFFERED|LAUNCHED)\b",
    r"\bPROPOSED\b",
    r"\bnot enacted\b",
    r"\bnot live\b",
    r"\bphasing out\b",
    r"\bgrandfathered\b",
    r"\bdormant\b",
    r"\bredesign\b",
    r"~~",  # strikethrough is itself an acknowledgement
)

ACK_WINDOW = 400  # chars around the match to scan for acknowledgement


def status_demands_ack(status: str) -> bool:
    s = status.upper()
    return any(token in s for token in NEEDS_ACK)


def searchable_core(programme_name: str) -> str | None:
    """Return the substring-searchable canonical core of a programme name, or
    None if the name is too short/generic to substring-match safely.

    Requiring multi-word names reduces false positives on generic phrases like
    "Self-Employed Persons" matching incidental playbook prose. The same gate
    decides whether a pair is audited (searchable) or skipped (surfaced in the
    summary) — see main() — so coverage is never over-reported.
    """
    # Strip markdown decorations from the canonical name for searching
    clean = re.sub(r"~~|[*]+", "", programme_name)
    # Drop trailing em-dash or parenthetical clauses; preserve internal hyphens
    # ("Start-Up Visa" must NOT become "Start").
    core = re.split(r"\s*[—(]\s*", clean, maxsplit=1)[0].strip()
    if len(core.split()) < 2 or len(core) < 6:
        return None
    return core


def find_unack_claims(playbook_text: str, programme_name: str) -> list[tuple[int, str]]:
    """Return (offset, snippet) tuples for unacknowledged claims."""
    core = searchable_core(programme_name)
    if core is None:
        return []

    pattern = re.compile(re.escape(core), re.IGNORECASE)
    out: list[tuple[int, str]] = []
    for m in pattern.finditer(playbook_text):
        start = max(0, m.start() - ACK_WINDOW)
        end = min(len(playbook_text), m.end() + ACK_WINDOW)
        window = playbook_text[start:end]
        if not any(re.search(p, window, re.IGNORECASE) for p in ACK_PATTERNS):
            snippet = playbook_text[max(0, m.start() - 60) : m.end() + 60].replace("\n", " ")
            out.append((m.start(), snippet))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--iso", help="single iso2 code to audit")
    ap.add_argument("--warn-only", action="store_true", help="exit 0 even on failure")
    args = ap.parse_args()

    payload = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    programs = payload["programs"]

    failures = 0
    audited = 0
    skipped = 0

    by_country: dict[str, list[dict]] = {}
    for p in programs:
        if not status_demands_ack(p.get("status", "")):
            continue
        by_country.setdefault(p["country"], []).append(p)

    countries = sorted(by_country.keys())
    if args.iso:
        countries = [c for c in countries if c == args.iso.lower()]

    for iso2 in countries:
        playbook = PLAYBOOKS_DIR / iso2 / "playbook.md"
        if not playbook.exists():
            continue
        text = playbook.read_text(encoding="utf-8")
        for prog in by_country[iso2]:
            if searchable_core(prog["programme"]) is None:
                skipped += 1
                continue
            audited += 1
            unack = find_unack_claims(text, prog["programme"])
            if unack:
                failures += 1
                print(
                    f"✗ {iso2.upper()} — '{prog['programme']}' "
                    f"(JSON status: {prog['status']!r}) "
                    f"mentioned {len(unack)}× without acknowledgement marker:"
                )
                for off, snip in unack[:2]:
                    print(f"    @{off}: …{snip}…")

    print()
    print(
        f"Audited {audited} programme×country pairs "
        f"({skipped} skipped — name too short/generic to substring-match safely); "
        f"{failures} unacknowledged."
    )
    if failures and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
