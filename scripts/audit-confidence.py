#!/usr/bin/env python3
"""
audit-confidence.py — verify primary-source URL count vs declared Confidence per playbook.

The skill drives 6-7 figure property decisions. Every playbook ends with a Status footer
declaring `**Confidence**: HIGH/MEDIUM/LOW`. Today that label is author-asserted, not
measured. This script measures it: count distinct primary-source URLs (gov / regulator /
multilateral) and verify the count meets a per-tier × per-confidence threshold.

A HIGH-confidence playbook with 8 government URLs is overclaiming. This script catches
that mechanically without per-claim provenance tagging.

Tier comes from _tiers.json. Confidence comes from the `**Confidence**:` line in the
playbook's Status footer. Compound labels (e.g., "MEDIUM-HIGH for X, MEDIUM for Y") are
parsed by the LOWEST level mentioned — the most lenient validation that still verifies
the floor the author has acknowledged.

Primary-source URLs are counted by domain (deduped). A URL counts as primary if its
domain matches a `.gov*` / `.gouv*` / `.gob*` / `.govt*` pattern, the multilateral list
(IMF / World Bank / BIS / IPCC / OECD / UN / EU institutions), or appears in
`scripts/primary-source-allowlist.txt` (curated central banks + statistics agencies that
don't carry a .gov subdomain — e.g., bom.mu, bcv.cv).

Exits 1 if any playbook fails. Prints a per-playbook diagnostic table either way.

Usage:
  python3 scripts/audit-confidence.py                # audit all playbooks
  python3 scripts/audit-confidence.py --tier=A       # filter by tier
  python3 scripts/audit-confidence.py --iso=mu       # single country
  python3 scripts/audit-confidence.py --verbose      # show URL list per playbook
  python3 scripts/audit-confidence.py --warn-only    # exit 0 even on failure (for soft rollout)

Calibration: thresholds are starting values. Adjust THRESHOLDS table as the playbook
population grows. Microstates (Tier-C) have a deliberately low floor; high-velocity
markets (Tier-A) carry a high floor matched to canonical playbook depth (FR/IT/CZ/SK).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
PLAYBOOKS_DIR = REPO_ROOT / "skills" / "property-deep-dive" / "countries"
TIERS_FILE = REPO_ROOT / "_tiers.json"
ALLOWLIST_FILE = REPO_ROOT / "scripts" / "primary-source-allowlist.txt"

# Per-tier × per-confidence URL-count thresholds. Starting values; calibrate as the
# population grows. Reasoning:
#   - Tier-A is high-velocity foreign-buyer markets; FR/IT/CZ/SK canonical playbooks
#     consistently carry 20+ primary URLs at HIGH confidence.
#   - Tier-C is microstates + frontier; primary-source coverage is genuinely thinner
#     (e.g., sm has ~28, ad similar — set the floor accordingly).
#   - LOW confidence acknowledges sparse data but should still meet a basic floor — a
#     LOW-confidence playbook with zero primary URLs isn't "low confidence", it's
#     "unsourced".
THRESHOLDS = {
    ("A", "HIGH"):   20,
    ("A", "MEDIUM"): 10,
    ("A", "LOW"):     5,
    ("B", "HIGH"):   15,
    ("B", "MEDIUM"):  7,
    ("B", "LOW"):     3,
    ("C", "HIGH"):   10,
    ("C", "MEDIUM"):  5,
    ("C", "LOW"):     3,
}

CONFIDENCE_LEVELS = ("LOW", "MEDIUM", "HIGH")  # ordered low → high

# Primary-source domain patterns. A URL whose hostname matches any of these counts as a
# primary government / regulator / multilateral source. Country-specific central-bank
# domains that don't fit these patterns (e.g., bom.mu) live in primary-source-allowlist.txt.
PRIMARY_HOST_PATTERNS = [
    # Most countries use one of these gov-identifying SLDs
    re.compile(r"\.gov(?:\.[a-z]{2,4})?$", re.IGNORECASE),       # gov, gov.uk, gov.cn, gov.gh
    re.compile(r"\.gouv\.[a-z]{2,4}$", re.IGNORECASE),           # gouv.fr
    re.compile(r"\.gob\.[a-z]{2,4}$", re.IGNORECASE),            # gob.es, gob.mx, gob.ar
    re.compile(r"\.govt\.[a-z]{2,4}$", re.IGNORECASE),           # govt.nz
    re.compile(r"\.go\.[a-z]{2,4}$", re.IGNORECASE),             # go.th, go.kr, go.jp, go.ke
    re.compile(r"\.gub\.[a-z]{2,4}$", re.IGNORECASE),            # gub.uy
    re.compile(r"\.gv\.[a-z]{2,4}$", re.IGNORECASE),             # gv.at
    re.compile(r"\.gc\.[a-z]{2,4}$", re.IGNORECASE),             # gc.ca (Canada federal)
    # Multi-stakeholder
    re.compile(r"(?:^|\.)govmu\.org$", re.IGNORECASE),           # Mauritius gov portal
    re.compile(r"(?:^|\.)europa\.eu$", re.IGNORECASE),           # EU institutions
    re.compile(r"(?:^|\.)un\.org$", re.IGNORECASE),              # UN
    re.compile(r"\.eu\.int$", re.IGNORECASE),                    # legacy EU
]

PRIMARY_EXACT_HOSTS = {
    "imf.org", "www.imf.org",
    "worldbank.org", "www.worldbank.org", "data.worldbank.org",
    "bis.org", "www.bis.org",
    "ipcc.ch", "www.ipcc.ch",
    "oecd.org", "www.oecd.org", "data.oecd.org",
    "wto.org", "www.wto.org",
    "fred.stlouisfed.org",  # Federal Reserve Economic Data — US Treasury data
}


def load_tier_map() -> dict[str, str]:
    """Map iso2 → tier letter (A/B/C) from _tiers.json."""
    data = json.loads(TIERS_FILE.read_text(encoding="utf-8"))
    out = {}
    for tier, info in data["tiers"].items():
        for code in info["codes"]:
            out[code] = tier
    return out


def load_allowlist() -> set[str]:
    """Curated primary-regulator domains that don't match the gov/gouv/gob patterns."""
    if not ALLOWLIST_FILE.exists():
        return set()
    out = set()
    for line in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
        # Strip inline comments (everything after `#`) and surrounding whitespace
        token = line.split("#", 1)[0].strip().lower()
        if token:
            out.add(token)
    return out


def extract_confidence(text: str) -> tuple[str | None, str]:
    """
    Pull the Confidence label from the Status footer.

    Returns (level, raw_line). level is the LOWEST of LOW/MEDIUM/HIGH mentioned on the
    line — the most-conservative validation of the author's claim. Returns (None, "")
    if no Confidence line is present.
    """
    m = re.search(r"\*\*Confidence\*\*:\s*([^\n]+)", text)
    if not m:
        return None, ""
    raw = m.group(1).strip()
    line_upper = raw.upper()
    levels_found = {lvl for lvl in CONFIDENCE_LEVELS if re.search(rf"\b{lvl}\b", line_upper)}
    if not levels_found:
        return None, raw
    for lvl in CONFIDENCE_LEVELS:
        if lvl in levels_found:
            return lvl, raw
    return None, raw


def is_primary_host(host: str, allowlist: set[str]) -> bool:
    """Decide whether a hostname counts as a primary government / regulator / multilateral source."""
    host = host.lower().strip()
    if not host:
        return False
    # Normalize: strip www. prefix for exact-match lookups (allowlist uses canonical form)
    bare = host[4:] if host.startswith("www.") else host
    if host in PRIMARY_EXACT_HOSTS or bare in PRIMARY_EXACT_HOSTS:
        return True
    if host in allowlist or bare in allowlist:
        return True
    for pat in PRIMARY_HOST_PATTERNS:
        if pat.search(host):
            return True
    return False


def count_primary_urls(text: str, allowlist: set[str]) -> tuple[int, set[str]]:
    """
    Count distinct primary-source domains. Dedupes by host so multiple deep-links to the
    same authority count once.
    """
    urls = re.findall(r"https?://[^\s\)\]\>\<\"\'\\`]+", text)
    primary_hosts: set[str] = set()
    for url in urls:
        # Trim trailing punctuation + Markdown delimiters that often wrap URLs in prose
        url = re.sub(r"[\.,;:!\?`*]+$", "", url)
        try:
            host = urlparse(url).netloc.lower()
        except Exception:
            continue
        if is_primary_host(host, allowlist):
            primary_hosts.add(host)
    return len(primary_hosts), primary_hosts


def audit_playbook(path: Path, tier_map: dict[str, str], allowlist: set[str]) -> dict:
    """Run the audit on one playbook. Returns a result dict (always)."""
    iso2 = path.parent.name
    text = path.read_text(encoding="utf-8")
    confidence, raw_conf = extract_confidence(text)
    url_count, hosts = count_primary_urls(text, allowlist)
    tier = tier_map.get(iso2, "?")
    threshold = THRESHOLDS.get((tier, confidence)) if confidence else None
    if confidence is None:
        passed = False
        reason = "no Confidence label found in Status footer"
    elif tier == "?":
        passed = False
        reason = f"iso2 not in _tiers.json"
    elif threshold is None:
        passed = False
        reason = f"no threshold for tier {tier} × confidence {confidence}"
    else:
        passed = url_count >= threshold
        reason = "" if passed else f"need ≥{threshold} primary URLs for tier {tier} × {confidence}; found {url_count}"
    return {
        "iso2": iso2,
        "tier": tier,
        "confidence": confidence,
        "raw_confidence": raw_conf,
        "url_count": url_count,
        "threshold": threshold,
        "pass": passed,
        "reason": reason,
        "hosts": hosts,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[1] if __doc__ else None)
    p.add_argument("--tier", choices=["A", "B", "C"], help="Filter to one tier")
    p.add_argument("--iso", help="Audit one country (iso2)")
    p.add_argument("-v", "--verbose", action="store_true", help="Print primary-source hosts per playbook")
    p.add_argument("--warn-only", action="store_true", help="Exit 0 even on failure (soft rollout)")
    args = p.parse_args()

    tier_map = load_tier_map()
    allowlist = load_allowlist()

    # Collect targets
    targets = []
    for playbook in sorted(PLAYBOOKS_DIR.glob("*/playbook.md")):
        if args.iso and playbook.parent.name != args.iso:
            continue
        targets.append(playbook)

    if not targets:
        print("No playbooks found.", file=sys.stderr)
        return 2

    # Run audits
    results = []
    for path in targets:
        r = audit_playbook(path, tier_map, allowlist)
        if args.tier and r["tier"] != args.tier:
            continue
        results.append(r)

    # Print table
    print(f"{'iso2':<5} {'tier':<5} {'conf':<8} {'urls':>5} {'min':>4} {'pass':>5}  reason")
    print("-" * 80)
    failures = []
    for r in results:
        ok = "✓" if r["pass"] else "✗"
        if not r["pass"]:
            failures.append(r)
        thresh_str = str(r["threshold"]) if r["threshold"] is not None else "-"
        conf_str = r["confidence"] or "?"
        print(
            f"{r['iso2']:<5} {r['tier']:<5} {conf_str:<8} "
            f"{r['url_count']:>5} {thresh_str:>4} {ok:>5}  {r['reason']}"
        )
        if args.verbose and r["hosts"]:
            for host in sorted(r["hosts"]):
                print(f"  · {host}")

    print()
    print(f"Audited {len(results)} playbooks; {len(failures)} failed")

    if failures and not args.warn_only:
        print()
        print("To fix a failing playbook, either:")
        print("  1. Add primary-source URLs (gov / regulator / multilateral) to back claims, OR")
        print("  2. Downgrade Confidence to a level whose threshold the URL count meets.")
        print(f"Threshold table: {THRESHOLDS}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
