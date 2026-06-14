#!/usr/bin/env python3
"""Compute / validate the CalVer version for this repo so a release never
drifts into the wrong month.

The scheme (see README § Versioning + CONTRIBUTING § Release process):

    YYYY.0M.MICRO
      0M    = the CALENDAR month (01-12) the version belongs to
      MICRO = in-month patch counter; 0 = the monthly-cycle release,
              1+ = mid-month corrections. MICRO RESETS to 0 when the
              month rolls (e.g. 2026.06.7 -> 2026.07.0).

The drift this guards against: a bump that keeps the OLD month's namespace
after the calendar has rolled (what happened when 2026.05.x kept being bumped
through June instead of rolling to 2026.06.0).

Usage:
    python3 scripts/next-version.py                 # print the correct next version for *now*
    python3 scripts/next-version.py --current       # print the version currently in plugin.json
    python3 scripts/next-version.py --write          # bump plugin.json to the correct next version
    python3 scripts/next-version.py --check HEAD [--base BASE]
                                                     # exit 1 if HEAD is an invalid next-version
                                                     #   (BASE defaults to plugin.json on disk)
    python3 scripts/next-version.py --month 2026-07 ...   # override "now" (testing / CI determinism)

"Next version for now":
    - calendar month > version month  -> roll: <cur>.0
    - calendar month == version month -> same month: <cur>.<micro+1>
    - calendar month < version month  -> error (version is ahead of the calendar)

Used by:
- .github/workflows/version-month-guard.yml (--check) on every PR
- the release-cut process: run it to get the exact version, then bump plugin.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PLUGIN_JSON = Path(__file__).resolve().parent.parent / ".claude-plugin" / "plugin.json"
VERSION_RE = re.compile(r"^(\d{4})\.(0[1-9]|1[0-2])\.(\d+)$")


def parse(version: str) -> tuple[int, int, int]:
    """Return (year, month, micro) or raise ValueError with a precise reason."""
    m = VERSION_RE.match(version.strip())
    if not m:
        raise ValueError(
            f"'{version}' is not valid CalVer YYYY.0M.MICRO "
            f"(0M zero-padded 01-12, MICRO an integer)"
        )
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def read_plugin_version() -> str:
    return json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))["version"]


def current_ym(override: str | None) -> tuple[int, int]:
    if override:
        try:
            y, mo = override.split("-")
            return int(y), int(mo)
        except ValueError:
            sys.exit(f"--month must be YYYY-MM, got '{override}'")
    now = datetime.now(timezone.utc)
    return now.year, now.month


def next_version(cur_ver: str, ym: tuple[int, int]) -> str:
    cy, cm, cmicro = parse(cur_ver)
    y, mo = ym
    if (y, mo) > (cy, cm):
        return f"{y:04d}.{mo:02d}.0"
    if (y, mo) == (cy, cm):
        return f"{y:04d}.{mo:02d}.{cmicro + 1}"
    raise ValueError(
        f"plugin.json version {cur_ver} is AHEAD of the current month "
        f"{y:04d}.{mo:02d} — refusing to compute a lower version"
    )


def check(head: str, base: str | None, ym: tuple[int, int]) -> list[str]:
    """Return a list of rule violations (empty == valid)."""
    errors: list[str] = []
    try:
        hy, hm, hmicro = parse(head)
    except ValueError as e:
        return [str(e)]

    y, mo = ym
    cur = f"{y:04d}.{mo:02d}"
    head_ym = f"{hy:04d}.{hm:02d}"

    # Core anti-drift rule: the version month must be the current calendar month.
    if (hy, hm) != (y, mo):
        errors.append(
            f"version {head} is in month {head_ym} but the current UTC month is "
            f"{cur}. CalVer 0M = calendar month — roll to {cur}.0 (new month) or "
            f"{cur}.<next MICRO> (same month). See CONTRIBUTING § Release process."
        )

    if base and base.strip() and base.strip() != head.strip():
        try:
            by, bm, bmicro = parse(base)
        except ValueError:
            by = bm = bmicro = None  # base unparseable — skip the monotonic checks
        if by is not None:
            if (hy, hm) == (by, bm):
                if hmicro <= bmicro:
                    errors.append(
                        f"same month {head_ym} but MICRO did not increase "
                        f"({base} -> {head}); use {by:04d}.{bm:02d}.{bmicro + 1}"
                    )
            elif (hy, hm) > (by, bm):
                if hmicro != 0:
                    errors.append(
                        f"month rolled {by:04d}.{bm:02d} -> {head_ym} so MICRO must "
                        f"reset to 0; use {head_ym}.0 (got {head})"
                    )
            else:
                errors.append(
                    f"version month went backwards "
                    f"({by:04d}.{bm:02d} -> {head_ym}) — versions must not decrease"
                )
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description="Compute / validate this repo's CalVer version.")
    ap.add_argument("--current", action="store_true", help="print plugin.json's current version")
    ap.add_argument("--write", action="store_true", help="bump plugin.json to the next version")
    ap.add_argument("--check", metavar="HEAD", help="validate HEAD as a next-version; exit 1 if invalid")
    ap.add_argument("--base", metavar="BASE", help="base version for --check (default: plugin.json on disk)")
    ap.add_argument("--month", metavar="YYYY-MM", help="override the current month (testing / CI)")
    args = ap.parse_args()

    ym = current_ym(args.month)

    if args.current:
        print(read_plugin_version())
        return 0

    if args.check is not None:
        base = args.base if args.base is not None else read_plugin_version()
        errors = check(args.check, base, ym)
        if errors:
            in_actions = bool(os.environ.get("GITHUB_ACTIONS"))
            for e in errors:
                # GitHub reads `::error::` workflow commands from stdout; humans
                # get a plain ERROR line on stderr otherwise.
                if in_actions:
                    print(f"::error::{e}")
                else:
                    print(f"ERROR: {e}", file=sys.stderr)
            return 1
        print(f"OK: {args.check} is a valid version for {ym[0]:04d}.{ym[1]:02d}")
        return 0

    nxt = next_version(read_plugin_version(), ym)

    if args.write:
        raw = PLUGIN_JSON.read_text(encoding="utf-8")
        cur = read_plugin_version()
        new = raw.replace(f'"version": "{cur}"', f'"version": "{nxt}"', 1)
        if new == raw:
            sys.exit(f"could not find \"version\": \"{cur}\" in {PLUGIN_JSON}")
        PLUGIN_JSON.write_text(new, encoding="utf-8")
        print(f"bumped plugin.json {cur} -> {nxt}")
        return 0

    print(nxt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
