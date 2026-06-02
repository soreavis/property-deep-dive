#!/usr/bin/env python3
"""Generate config/_match-index.json for the `--match` discovery mode.

`--match` (reverse-`--compare`, see shared/compare.md § Reverse mode) ranks
countries against a user's constraints. This script precomputes the rank/band
per criterion **deterministically from the authoritative data the skill already
maintains** — it never invents a score.

Sources of truth (parsed, not duplicated):
- skills/property-deep-dive/shared/compare.md  → the "Precomputed verdict
  shortcuts" ranked lists (lowest/highest acquisition cost, lowest/highest
  annual carry, FX stability, foreign-buyer friendliness/friction, golden-visa,
  tax-reform direction). Each list is an ordered ranking; a country's position
  in it is its provenance (`src`).
- config/_visa-programs.json  → OPEN property-linked residency route (hard filter).

Anti-hallucination contract (mirrors shared/compare.md § Reverse mode):
- Every emitted band traces to a named compare.md list position (`src`). A country
  absent from a criterion's list gets NO band (null) — never a guessed value.
- The seven criteria with no precomputed list — yield, climate, healthcare,
  schools, safety, connectivity, cost-of-living — are emitted as
  {"status": "pending-extraction"}. They are populated by a SEPARATE grounded
  research + independent-audit pass (see _local/scope-match-section.md § Phase 2,
  § 11 Q7), and run as live MEDIUM extraction until then. This script must never
  fabricate them.

Banding (documented, rank-based, no false precision):
- "good" list of K, rank r (1 = best)  → band = round(55 + 45*(K-r)/(K-1))  ∈ [55,100]
- "bad"  list of K, rank r (1 = worst) → band = round(45*(r-1)/(K-1))        ∈ [0,45]
  (single-item lists → good 100 / bad 0)

Modes:
    ./scripts/render-match-index.py            # write config/_match-index.json
    ./scripts/render-match-index.py --check     # exit 1 if the committed file is stale
    ./scripts/render-match-index.py --diff      # print what would change, no write
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPARE_MD = ROOT / 'skills' / 'property-deep-dive' / 'shared' / 'compare.md'
VISA_JSON = ROOT / 'config' / '_visa-programs.json'
EXTRACTED_FILE = ROOT / 'config' / '_match-extracted.json'
OUT_FILE = ROOT / 'config' / '_match-index.json'

SCHEMA_VERSION = 1

# Criteria with no precomputed ranked list — never fabricated here.
PENDING_CRITERIA = [
    'yield', 'climate', 'healthcare', 'schools', 'safety',
    'connectivity', 'cost-of-living',
]

# Eurozone members — used to expand a "**Eurozone** (21 countries…)" list item
# into its members for the FX-stability criterion. (Stable, well-known set.)
EUROZONE = [
    'at', 'be', 'hr', 'cy', 'ee', 'fi', 'fr', 'de', 'gr', 'ie', 'it', 'lv',
    'lt', 'lu', 'mt', 'nl', 'pt', 'sk', 'si', 'es', 'bg',  # BG joined 1 Jan 2026
]

# EUR-pegged microstates with no FX risk for euro buyers (treaty euro) — pinned
# to the top FX tier alongside the eurozone (compare.md lists them "no FX risk").
FX_NO_FX_RISK = set(EUROZONE) | {'mc', 'ad'}

# Golden-visa list items that are documented ABSENCES, not friendly rankings
# (e.g. "SG / MO / LI — NO golden-visa via real estate"). Skipped for visa.
VISA_ABSENCE = re.compile(r'NO golden-visa', re.IGNORECASE)

# criterion -> (good-list header substring, bad-list header substring | None)
# Headers matched by a stable substring to survive the parenthetical suffixes.
CRITERION_LISTS = {
    'acquisition-cost': ('Lowest acquisition cost', 'Highest acquisition cost'),
    'annual-carry':     ('Lowest annual carry', 'Highest annual carry'),
    'fx':               ('Most stable currency', 'Highest FX risk'),
    'foreign-buyer':    ('Most foreign-buyer-friendly', 'Highest acquisition friction'),
    'visa':             ('Most golden-visa-friendly', None),
    'tax':              ('Cleanest 2026 tax reforms', 'Steepest 2026 tax reforms'),
}

# Ban keywords in the friction list → foreign-buyer-open = False (vs. merely
# costly/quota-restricted which stays "open but restricted").
# True bans only → foreign-buyer-open = False. Deliberately NOT a bare "barred"
# (which matches incidental clauses like "agricultural barred" / "rest barred"
# in designated-freehold-zone countries, e.g. OM/BH/JO, which ARE open in-zone
# — same structure as AE/QA/SA). Catches no-land-freehold regimes (TH/VN/PH/ID)
# and outright purchase bans (CA/AU/NZ established-homes, KW, non-NRI IN).
BAN_PATTERNS = re.compile(
    r'foreign-buyer ban|homes ban\b|homes banned|cannot own|foreigners CANNOT|'
    r'no land freehold|no land for foreigners|\bno land\b|no Hak Milik|'
    r'not available to foreigners',
    re.IGNORECASE,
)


def _band_good(rank: int, k: int) -> int:
    if k <= 1:
        return 100
    return round(55 + 45 * (k - rank) / (k - 1))


def _band_bad(rank: int, k: int) -> int:
    if k <= 1:
        return 0
    return round(45 * (rank - 1) / (k - 1))


def _extract_section(text: str, header_sub: str) -> str | None:
    """Return the body of the first '### <… header_sub …>' section up to the
    next '###' or '##' header, or None."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith('### ') and header_sub in line:
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if line.startswith('## ') or line.startswith('### '):
            break
        body.append(line)
    return '\n'.join(body)


_ITEM_RE = re.compile(r'^\s*(\d+)\.\s+\*{0,2}([A-Za-z]{2,})')


def _parse_ranked_codes(section_body: str, skip_re=None) -> list[str]:
    """Ordered ISO2 codes from a numbered list. Expands 'Eurozone'. Skips
    non-code leading words and any line matching skip_re (documented absences).
    De-dupes, preserving first occurrence."""
    out: list[str] = []
    for line in section_body.splitlines():
        m = _ITEM_RE.match(line)
        if not m:
            continue
        if skip_re is not None and skip_re.search(line):
            continue
        token = m.group(2)
        if token.lower() == 'eurozone':
            for c in EUROZONE:
                if c not in out:
                    out.append(c)
            continue
        if len(token) == 2 and token.isupper():
            code = token.lower()
            if code not in out:
                out.append(code)
    return out


def _parse_friction_open_flags(section_body: str) -> dict[str, bool]:
    """For the friction list, map code -> foreign-buyer-open (False on a true
    ban keyword, True for merely costly/quota-restricted)."""
    flags: dict[str, bool] = {}
    for line in section_body.splitlines():
        m = _ITEM_RE.match(line)
        if not m or not (len(m.group(2)) == 2 and m.group(2).isupper()):
            continue
        code = m.group(2).lower()
        flags[code] = not bool(BAN_PATTERNS.search(line))
    return flags


def _load_visa_routes() -> set[str]:
    """Countries with at least one OPEN, property-linked visa programme."""
    data = json.loads(VISA_JSON.read_text(encoding='utf-8'))
    routes: set[str] = set()
    for p in data.get('programs', []):
        status = str(p.get('status', '')).upper()
        # property_linked must AFFIRMATIVELY say YES (strip leading markdown first).
        # "No" / "**NO — RE removed" / "Generally no" / "Possibly" do NOT count —
        # a hard filter must not overclaim a residency route the data doesn't confirm.
        linked = re.sub(r'^\W+', '', str(p.get('property_linked', '')).strip().lower())
        if status.startswith('OPEN') and linked.startswith('yes'):
            routes.add(str(p.get('country', '')).lower())
    return routes


def _load_extracted() -> dict:
    """Curated tier data for the pending criteria that DO have a stored,
    citable per-country signal (currently: healthcare). Criteria absent here
    stay pending-extraction. Never fabricated — every band cites its source."""
    if not EXTRACTED_FILE.exists():
        return {}
    return json.loads(EXTRACTED_FILE.read_text(encoding='utf-8'))


def build_index() -> dict:
    text = COMPARE_MD.read_text(encoding='utf-8')

    # Per-criterion bands + provenance.
    scores: dict[str, dict[str, dict]] = {}
    fb_open_flags: dict[str, bool] = {}
    fx_stable: set[str] = set()

    for crit, (good_sub, bad_sub) in CRITERION_LISTS.items():
        good_body = _extract_section(text, good_sub)
        if good_body is None:
            raise SystemExit(f"❌ compare.md section not found: '{good_sub}'")
        good = _parse_ranked_codes(
            good_body, skip_re=VISA_ABSENCE if crit == 'visa' else None)
        kg = len(good)
        for r, code in enumerate(good, start=1):
            scores.setdefault(code, {})[crit] = {
                'band': _band_good(r, kg), 'rank': r, 'k': kg,
                'src': f'compare.md:{good_sub}#{r}',
            }
        if crit == 'fx':
            fx_stable.update(good)
            # Eurozone is one "no FX risk" tier in compare.md — don't let the
            # list-expansion order spread its members across ranks; pin to top.
            for code in good:
                if code in FX_NO_FX_RISK:
                    scores[code]['fx'] = {
                        'band': 100, 'rank': 1, 'k': kg,
                        'src': f'compare.md:{good_sub}# no-FX-risk (EUR) tier',
                    }

        if bad_sub:
            bad_body = _extract_section(text, bad_sub)
            if bad_body is None:
                raise SystemExit(f"❌ compare.md section not found: '{bad_sub}'")
            bad = _parse_ranked_codes(bad_body)
            kb = len(bad)
            for r, code in enumerate(bad, start=1):
                # A country only in the bad list (not already scored good).
                if crit not in scores.get(code, {}):
                    scores.setdefault(code, {})[crit] = {
                        'band': _band_bad(r, kb), 'rank': r, 'k': kb,
                        'src': f'compare.md:{bad_sub}#{r}',
                    }
            if crit == 'foreign-buyer':
                fb_open_flags = _parse_friction_open_flags(bad_body)

    visa_routes = _load_visa_routes()
    extracted = _load_extracted()

    def _hard(code: str) -> dict:
        return {
            'foreign-buyer-open': fb_open_flags.get(code, True),
            'no-fx-risk': code in fx_stable,
            'property-residency-route': code in visa_routes,
        }

    # Assemble per-country records over the union of codes seen in the
    # deterministic compare.md lists + the curated extracted file.
    extracted_codes = {
        code
        for block in extracted.get('criteria', {}).values()
        for code in block.get('countries', {})
    }
    all_codes = sorted(set(scores) | extracted_codes)
    countries: dict[str, dict] = {}
    for code in all_codes:
        crit_scores = dict(scores.get(code, {}))
        for c in PENDING_CRITERIA:
            crit_scores.setdefault(c, {'status': 'pending-extraction'})
        countries[code] = {
            'hard': _hard(code),
            'entry_eur_m2': None,        # pending — live playbook read for budget gate
            'confidence': 'MEDIUM',      # deterministic core HIGH; pending criteria MEDIUM
            'scores': crit_scores,
        }

    # Merge curated extracted criteria — override the pending cell, with provenance.
    for crit, block in extracted.get('criteria', {}).items():
        src = block.get('source', '')
        for code, cell in block.get('countries', {}).items():
            countries[code]['scores'][crit] = {
                'band': cell['band'],
                'tier': cell.get('tier'),
                'src': f'{src}#{crit}',
                'evidence': cell.get('evidence'),
                'conf': 'MEDIUM',
            }

    return {
        '_comment': (
            'AUTO-GENERATED by scripts/render-match-index.py — do not edit by hand. '
            'Source of truth: shared/compare.md ranked lists + config/_visa-programs.json. '
            'Bands are rank-based with src provenance; the 7 pending-extraction criteria '
            '(yield/climate/healthcare/schools/safety/connectivity/cost-of-living) are '
            'populated by a separate grounded research+audit pass, never fabricated here. '
            'Regenerate with ./scripts/render-match-index.py; CI runs --check.'
        ),
        'schema_version': SCHEMA_VERSION,
        'criteria': list(CRITERION_LISTS.keys()) + PENDING_CRITERIA,
        'pending_criteria': PENDING_CRITERIA,
        'country_count': len(countries),
        'countries': countries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--check', action='store_true',
                        help='Exit 1 if config/_match-index.json is stale; do not write')
    parser.add_argument('--diff', action='store_true',
                        help='Print a summary of what would change; do not write')
    args = parser.parse_args()

    index = build_index()
    new_text = json.dumps(index, indent=2, ensure_ascii=False) + '\n'

    old_text = OUT_FILE.read_text(encoding='utf-8') if OUT_FILE.exists() else ''

    # Coverage report (always printed).
    covered = {c: 0 for c in CRITERION_LISTS}
    for rec in index['countries'].values():
        for c in CRITERION_LISTS:
            if c in rec['scores'] and 'band' in rec['scores'][c]:
                covered[c] += 1
    print(f'Countries indexed: {index["country_count"]}')
    print('Deterministic criterion coverage (countries with a band):')
    for c, n in covered.items():
        print(f'  {c:18s} {n:>3d}')
    ext_cov = {c: 0 for c in PENDING_CRITERIA}
    for rec in index['countries'].values():
        for c in PENDING_CRITERIA:
            if 'band' in rec['scores'].get(c, {}):
                ext_cov[c] += 1
    print('Pending-criteria curated coverage (0 = live-by-design, no static index):')
    for c, n in ext_cov.items():
        print(f'  {c:18s} {n:>3d}')

    if new_text == old_text:
        print('\n✓ config/_match-index.json is up to date.')
        return 0

    if args.check:
        print('\n❌ config/_match-index.json is stale.')
        print('   Run ./scripts/render-match-index.py to regenerate, then commit.')
        return 1
    if args.diff:
        print('\n(diff mode) config/_match-index.json WOULD change '
              f'({len(old_text)} → {len(new_text)} bytes).')
        return 0

    OUT_FILE.write_text(new_text, encoding='utf-8')
    print('\n✓ Wrote config/_match-index.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
