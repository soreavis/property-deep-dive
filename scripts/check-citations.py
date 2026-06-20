#!/usr/bin/env python3
"""Static portal-root citation linter (no network, no LLM, no deps).

Flags citations that point at a bare domain ROOT (e.g. `https://www.gov.ky/`) sitting next to a
specific figure — because the page that proves a number is almost never the homepage. This is the
authoring-time catch for the single most common weak-citation pattern (9 of 17 in the 2026-06-02
source-verification run). Advisory by default (exit 0); pass --strict to fail CI.

A line is flagged when ALL hold:
  * it contains a markdown link `[label](URL)` whose URL path is empty or "/" (a bare root),
  * the line carries a salient value (percentage / money amount / statute id),
  * the root host/URL is not in config/_source-verify.json linter.root_url_allowlist,
  * the line is NOT an explicit "verify here / verify at" pointer (those legitimately point at a portal).

Run: python3 scripts/check-citations.py [--strict] [--country=<iso2>]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "config" / "_source-verify.json"

MD_LINK_RE = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<url>https?://[^)\s]+)\)")
# Trigger ONLY on a percentage or money figure — a NUMBER that needs a specific page. Statute ids
# are deliberately excluded: "[Llei 21/2014](gazette-root)" is an accepted naming convention (the
# statute name IS the locator), and flagging it generates hundreds of false positives.
SALIENT_RE = re.compile(
    r"(?<![\w.])\d{1,3}(?:[.,]\d+)?\s?%"                                  # percentage
    r"|[€£$¥₹]\s?\d"                                                       # money symbol
    r"|(?:USD|EUR|GBP|CHF|AED|SAR|JPY|CNY|HKD|SGD|AUD|NZD|CAD|ZAR|INR|XCD|KYD|CI\$|HK\$|S\$)\s?\d",  # money code
    re.IGNORECASE,
)
# A "bare-host" link label looks like a domain (gov.ky, legislation.gov.ky, bopa.ad) — i.e. the
# citation is just a portal pointer, not a named document. Document labels ("Llei 21/2014",
# "DL 126/2021") have spaces/slashes and don't match. This is the precision filter.
HOSTLIKE_LABEL_RE = re.compile(r"^[a-z0-9][a-z0-9.-]*\.[a-z]{2,}$", re.IGNORECASE)

# Only flag PRIMARY-SOURCE roots (a deep gov/regulator page exists and should be cited). A
# commercial carrier/aggregator homepage cited for a tariff (orange.sk, telekom.hu, flat35.com)
# is an accepted convention, not the weak-citation pattern — skip it, or it drowns the signal.
_GOV_RE = re.compile(r"(?:^|\.)(?:gov|gouv|gob)(?:\.[a-z]{2,4})?$", re.IGNORECASE)
PRIMARY_ALLOW_PATH = ROOT / "scripts" / "primary-source-allowlist.txt"


def load_primary_hosts() -> set[str]:
    hosts: set[str] = set()
    if PRIMARY_ALLOW_PATH.exists():
        for line in PRIMARY_ALLOW_PATH.read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip().lower()
            if line:
                hosts.add(line)
    return hosts


_PRIMARY_HOSTS = load_primary_hosts()


def is_primary(host: str) -> bool:
    host = host.lower()
    if _GOV_RE.search(host):
        return True
    h = host[4:] if host.startswith("www.") else host
    return host in _PRIMARY_HOSTS or h in _PRIMARY_HOSTS
# Lines that legitimately frame the portal root as a navigation pointer for the reader.
POINTER_RE = re.compile(
    r"\b(?:verify|confirm|check|consult|cross-check|see|lookup|look up|search)\b[^.]{0,30}?"
    r"\b(?:at|here|current|the|via|on|using|directly)\b|\bsource:\s|\bper the\b",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^#{1,6}\s")


def is_root(url: str) -> bool:
    p = urlparse(url.rstrip(".,;:)"))
    return p.path in ("", "/") and not p.query and not p.fragment


def load_allowlist() -> set[str]:
    try:
        raw = json.loads(CFG.read_text(encoding="utf-8"))
        return {h.lower() for h in raw.get("linter", {}).get("root_url_allowlist", [])}
    except Exception:
        return set()


def scope_dirs() -> list[Path]:
    try:
        raw = json.loads(CFG.read_text(encoding="utf-8"))
        return [ROOT / d for d in raw["extraction"]["scope_dirs"]]
    except Exception:
        return [ROOT / "skills" / "property-deep-dive" / "countries",
                ROOT / "skills" / "property-deep-dive" / "shared"]


def flag_line(line: str, allow: set[str] = frozenset()) -> list[str]:
    """Return the root URLs on this single line that should be flagged — a bare-host link label
    sitting next to a money/percentage figure, not a navigation pointer. Empty list = clean.
    Pure function (no filesystem) so it is directly unit-testable."""
    if HEADING_RE.match(line) or "](http" not in line:
        return []
    if not SALIENT_RE.search(line) or POINTER_RE.search(line):
        return []
    out: list[str] = []
    for m in MD_LINK_RE.finditer(line):
        url = m.group("url").rstrip(".,;:)")
        if not is_root(url):
            continue
        # only flag bare-host labels (portal pointers), not named-document citations
        if not HOSTLIKE_LABEL_RE.match(m.group("label").strip()):
            continue
        host = urlparse(url).netloc.lower()
        if host in allow or url.lower() in allow:
            continue
        # only PRIMARY-SOURCE roots — a commercial carrier/aggregator homepage is fine as a pointer
        if not is_primary(host):
            continue
        out.append(url)
    return out


def lint(only_scope: str | None = None) -> list[dict]:
    allow = load_allowlist()
    findings: list[dict] = []
    for d in scope_dirs():
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            if only_scope and only_scope not in str(path):
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeDecodeError):
                continue
            for n, line in enumerate(lines, 1):
                for url in flag_line(line, allow):
                    findings.append({
                        "file": str(path.relative_to(ROOT)), "line": n, "url": url,
                        "context": line.strip()[:140],
                    })
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description="Static portal-root citation linter (advisory).")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any finding (fail CI)")
    ap.add_argument("--country", default=None, help="restrict to a scope substring")
    args = ap.parse_args()

    findings = lint(args.country)
    if not findings:
        print("✓ no domain-root citations next to a figure")
        return 0

    print(f"⚠️  {len(findings)} citation(s) point at a PRIMARY-SOURCE domain ROOT next to a figure "
          f"(point at the gov/regulator page that proves the number, or tag the line 'verify at'):\n")
    for f in findings:
        print(f"  {f['file']}:{f['line']}  → {f['url']}")
        print(f"      {f['context']}")
    print("\n(advisory — allowlist legitimate root pointers in config/_source-verify.json linter.root_url_allowlist)")
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
