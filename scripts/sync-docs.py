#!/usr/bin/env python3
"""Auto-sync counts and AUTOGEN-marked blocks in community markdown files.

Idempotent: running the script twice produces the same result.

Used by:
- .github/workflows/doc-sync-check.yml in --check mode on every PR
- Manually after content changes (new country, new section flag)

Sources of truth:
- skills/property-deep-dive/countries/   directory contents → country count
- skills/property-deep-dive/shared/*.md  → shared file count
- .github/workflows/*.yml                → workflow count
- skills/property-deep-dive/SKILL.md     → section flag count (argument-hint)
- config/_regions.json                   → region grouping for country matrix

Examples:
    ./scripts/sync-docs.py            # write changes
    ./scripts/sync-docs.py --check    # exit 1 if changes would be made
    ./scripts/sync-docs.py --diff     # print what would change, no writes
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / 'skills' / 'property-deep-dive'
SHARED_DIR = SKILL_DIR / 'shared'
COUNTRIES_DIR = SKILL_DIR / 'countries'
SKILL_MD = SKILL_DIR / 'SKILL.md'
REGIONS_FILE = ROOT / 'config' / '_regions.json'
# Local-only / cache dirs that must never count toward the doc totals. These
# are absent in a clean CI checkout, so counting them locally would diverge the
# `--check` gate from CI (e.g. a stray scripts/.pytest_cache/README.md inflating
# total_md by 1). Do NOT add dotted dirs that hold real docs (e.g. .github holds
# pull_request_template.md).
EXCLUDE_DIRS = {'_local', '.git', 'node_modules',
                '.pytest_cache', '__pycache__', '.ruff_cache', '.mypy_cache'}

# ── Fact computation ──────────────────────────────────────────────────────

def _all_md_files():
    for f in ROOT.rglob('*.md'):
        if any(p in EXCLUDE_DIRS for p in f.parts):
            continue
        yield f

def count_country_dirs() -> int:
    return sum(1 for d in COUNTRIES_DIR.iterdir() if d.is_dir()) if COUNTRIES_DIR.exists() else 0

def count_shared_files() -> int:
    return len(list(SHARED_DIR.glob('*.md'))) if SHARED_DIR.exists() else 0

def count_workflows() -> int:
    wf = ROOT / '.github' / 'workflows'
    return len(list(wf.glob('*.yml'))) if wf.exists() else 0

def count_issue_forms() -> int:
    """All .yml files in .github/ISSUE_TEMPLATE/ — includes config.yml since
    the README counts it as one of the issue forms historically."""
    d = ROOT / '.github' / 'ISSUE_TEMPLATE'
    return len(list(d.glob('*.yml'))) if d.exists() else 0

def count_root_github_yaml() -> int:
    """dependabot.yml + labeler.yml + labels.yml in .github/ root."""
    d = ROOT / '.github'
    return len([p for p in d.glob('*.yml')]) if d.exists() else 0

def count_total_md() -> int:
    return sum(1 for _ in _all_md_files())

def count_total_md_lines() -> int:
    total = 0
    for f in _all_md_files():
        try:
            total += sum(1 for _ in f.open(encoding='utf-8'))
        except OSError:
            continue  # unreadable file — skip from line count
    return total

def count_skill_md_files() -> int:
    n = 1 if SKILL_MD.exists() else 0
    n += count_shared_files()
    n += len(list(COUNTRIES_DIR.glob('*/playbook.md')))
    return n

def count_skill_md_lines() -> int:
    paths = []
    if SKILL_MD.exists():
        paths.append(SKILL_MD)
    paths.extend(SHARED_DIR.glob('*.md'))
    paths.extend(COUNTRIES_DIR.glob('*/playbook.md'))
    total = 0
    for p in paths:
        try:
            total += sum(1 for _ in p.open(encoding='utf-8'))
        except OSError:
            continue  # unreadable file — skip from line count
    return total

def count_section_flags() -> int:
    if not SKILL_MD.exists():
        return 0
    text = SKILL_MD.read_text(encoding='utf-8')
    m = re.search(r'argument-hint:\s*"([^"]+)"', text)
    if not m:
        return 0
    flags = set(re.findall(r'--([a-z][a-z0-9-]*)', m.group(1)))
    # Output / control flags that aren't user-invocable sections.
    output_only = {
        # Output controls
        'save', 'quick', 'deep', 'override-confidence', 'listing', 'all', 'country',
        # Translation flags (output controls)
        'lang', 'lang-scope',
        # Maintenance mode flags
        'update', 'add', 'diff', 'interactive', 'test',
        'validate-only', 'refresh-only', 'health-report',
        'tier', 'include', 'exclude',
        # Cross-cutting layers — counted separately from the section flags
        'integrity', 'journey', 'type',
        # Discovery mode — reverse of --compare; not a per-address section
        'match',
        # Tooling helpers (TCO calc, mortgage calc, listing watcher) — not sections
        'tco', 'mortgage', 'watch',
    }
    return len(flags - output_only)

def load_regions() -> dict:
    if not REGIONS_FILE.exists():
        return {'regions': []}
    return json.loads(REGIONS_FILE.read_text(encoding='utf-8'))

def _round_100(n: int) -> int:
    """Round to a granularity that survives an ordinary PR: nearest 1,000 from
    10k up, nearest 100 below. README line counts use rounded values to stay
    human-readable; the exact value is volatile and a precise number in a
    'roughly N lines' context misleads. The step is magnitude-aware because a
    flat 100 made the six-figure repo total flip on a 6-line PR, failing the
    doc-sync gate for contributors who had touched nothing related."""
    step = 1000 if n >= 10_000 else 100
    return ((n + step // 2) // step) * step

def compute_facts() -> dict[str, int]:
    total_lines = count_total_md_lines()
    skill_lines = count_skill_md_lines()
    workflows  = count_workflows()
    issue_forms = count_issue_forms()
    root_yaml  = count_root_github_yaml()
    return {
        'countries':       count_country_dirs(),
        'sections':        count_section_flags(),
        'shared':          count_shared_files(),
        'workflows':       workflows,
        'issue_forms':     issue_forms,
        'total_yaml':      workflows + issue_forms + root_yaml,
        'total_md':        count_total_md(),
        'total_lines':     total_lines,
        'total_lines_rnd': _round_100(total_lines),
        'skill_md':        count_skill_md_files(),
        'skill_lines':     skill_lines,
        'skill_lines_rnd': _round_100(skill_lines),
    }

# ── Country matrix rendering ──────────────────────────────────────────────

# The repo uses some non-ISO-3166 country codes for directory / SoT alignment
# with how the wider community refers to them. The Unicode regional-indicator
# encoding strictly follows ISO 3166, so we override here:
#   - "uk" (project convention) → 🇬🇧 (Great Britain), NOT 🇺🇰 (Ukraine)
FLAG_OVERRIDES = {
    'uk': '🇬🇧',
}

def iso2_to_flag(iso2: str) -> str:
    """Render a country code as a regional-indicator flag emoji.

    Honours FLAG_OVERRIDES for project-specific code conventions; otherwise
    falls back to ISO 3166 alpha-2 → regional-indicator mapping.
    """
    if iso2.lower() in FLAG_OVERRIDES:
        return FLAG_OVERRIDES[iso2.lower()]
    base = 0x1F1E6
    return ''.join(chr(base + ord(c) - ord('a')) for c in iso2.lower())

def render_country_matrix(regions: dict) -> str:
    parts = []
    for region in regions.get('regions', []):
        codes = region.get('codes', [])
        label = region.get('label', region.get('id', ''))
        flag_strs = [f"{iso2_to_flag(c)} {c}" for c in codes]
        parts.append(f"**{label} ({len(codes)})** — {' · '.join(flag_strs)}")
    return '\n\n'.join(parts)

# ── Replacements ──────────────────────────────────────────────────────────

# Inline regex replacements: (file, regex_pattern, format_string)
# `format_string` is .format()-applied to facts. Each entry is idempotent —
# regex matches both old and current values, replacement is the current one.
INLINE_REPLACEMENTS: list[tuple[str, str, str]] = [
    # README headline
    ('README.md',
     r'\*\*\d+ countries\*\* fully populated',
     '**{countries} countries** fully populated'),
    # README "Country support" heading
    ('README.md',
     r'## Country support — \d+ fully populated',
     '## Country support — {countries} fully populated'),
    # README "user-invocable sections"
    ('README.md',
     r'\*\*\d+ user-invocable sections\*\*',
     '**{sections} user-invocable sections**'),
    # README architecture comment for skills/property-deep-dive/shared/
    ('README.md',
     r'(\d+) top-level universal layer files \(~[\d,]+ lines\)',
     '{shared} top-level universal layer files (~{shared_lines_rnd:,} lines)'),
    # README architecture comment for workflows count
    ('README.md',
     r'\(\d+ in total — see CHANGELOG',
     '({workflows} in total — see CHANGELOG'),
    # README "Skill content" line
    ('README.md',
     r'(?<=\*\*Skill content\*\*: )\d+ markdown files, ~[\d,]+ lines',
     '{skill_md} markdown files, ~{skill_lines_rnd:,} lines'),
    # README "Repo total" line
    ('README.md',
     r'(?<=\*\*Repo total\*\*: )\d+ markdown files, ~[\d,]+ lines',
     '{total_md} markdown files, ~{total_lines_rnd:,} lines'),
    # README config-file inventory inside Repo total parenthetical
    ('README.md',
     r'\d+ YAML config files \(\d+ workflows \+ \d+ issue forms \+ dependabot \+ labels \+ labeler\)',
     '{total_yaml} YAML config files ({workflows} workflows + {issue_forms} issue forms + dependabot + labels + labeler)'),
    # CONTRIBUTING country count
    ('CONTRIBUTING.md',
     r'(\d+) countries currently',
     '{countries} countries currently'),
]

# Block replacements: (file, block_id) — renderer comes from BLOCK_RENDERERS.
BLOCK_REPLACEMENTS: list[tuple[str, str]] = [
    ('README.md', 'country-matrix'),
]

def get_block_renderer(block_id: str, facts: dict, regions: dict):
    if block_id == 'country-matrix':
        return lambda: render_country_matrix(regions)
    raise KeyError(f"No renderer for block '{block_id}'")

def apply_inline(text: str, file_name: str, facts: dict) -> str:
    # `shared_lines` derived once for the inline replacements that need it
    shared_lines = sum(
        sum(1 for _ in p.open(encoding='utf-8'))
        for p in SHARED_DIR.glob('*.md')
    ) if SHARED_DIR.exists() else 0
    fmt_facts = {**facts, 'shared_lines': shared_lines, 'shared_lines_rnd': _round_100(shared_lines)}
    new = text
    for f, pattern, template in INLINE_REPLACEMENTS:
        if f != file_name:
            continue
        replacement = template.format(**fmt_facts)
        new = re.sub(pattern, replacement, new)
    return new

def apply_blocks(text: str, file_name: str, facts: dict, regions: dict) -> str:
    new = text
    for f, block_id in BLOCK_REPLACEMENTS:
        if f != file_name:
            continue
        start = f'<!-- AUTOGEN:{block_id}:start -->'
        end = f'<!-- AUTOGEN:{block_id}:end -->'
        if start not in new or end not in new:
            continue
        renderer = get_block_renderer(block_id, facts, regions)
        content = renderer()
        pattern = re.escape(start) + r'.*?' + re.escape(end)
        replacement = f'{start}\n{content}\n{end}'
        new = re.sub(pattern, replacement, new, flags=re.DOTALL)
    return new

# ── Sanity checks ─────────────────────────────────────────────────────────

def check_regions_consistency(regions: dict) -> list[str]:
    warnings: list[str] = []
    region_codes = []
    for r in regions.get('regions', []):
        for c in r.get('codes', []):
            region_codes.append(c)
    duplicates = {c for c in region_codes if region_codes.count(c) > 1}
    for c in sorted(duplicates):
        warnings.append(f"Country '{c}' appears in multiple regions in config/_regions.json")

    fs_codes = {d.name for d in COUNTRIES_DIR.iterdir() if d.is_dir()} if COUNTRIES_DIR.exists() else set()
    region_code_set = set(region_codes)
    only_regions = region_code_set - fs_codes
    only_fs = fs_codes - region_code_set
    if only_regions:
        warnings.append(f"In config/_regions.json but no playbook directory: {sorted(only_regions)}")
    if only_fs:
        warnings.append(f"Has playbook but missing from config/_regions.json: {sorted(only_fs)}")
    return warnings

# ── Main ──────────────────────────────────────────────────────────────────

def process_file(file_name: str, facts: dict, regions: dict, write: bool) -> tuple[bool, str, str]:
    p = ROOT / file_name
    if not p.exists():
        return False, '', ''
    text = p.read_text(encoding='utf-8')
    new = apply_inline(text, file_name, facts)
    new = apply_blocks(new, file_name, facts, regions)
    changed = new != text
    if changed and write:
        p.write_text(new, encoding='utf-8')
    return changed, text, new

def render_diff(file_name: str, old: str, new: str) -> str:
    return ''.join(difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile=f'{file_name} (current)',
        tofile=f'{file_name} (would-be)',
        n=2,
    ))

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--check', action='store_true', help='Exit 1 if changes would be made; do not write')
    parser.add_argument('--diff', action='store_true', help='Print diff of planned changes; do not write')
    args = parser.parse_args()
    write = not (args.check or args.diff)

    facts = compute_facts()
    regions = load_regions()

    print('Computed facts:')
    for k, v in facts.items():
        if isinstance(v, int):
            print(f'  {k:15s} {v:>8,}')
        else:
            print(f'  {k:15s} {v}')

    warnings = check_regions_consistency(regions)
    for w in warnings:
        print(f'  ⚠️  {w}')

    files = ['README.md', 'CONTRIBUTING.md', 'SECURITY.md']
    drift = 0
    for f in files:
        changed, old, new = process_file(f, facts, regions, write)
        verb = 'updated   ' if (changed and write) else (
            'would-edit' if changed else 'in-sync   '
        )
        print(f'  {verb}  {f}')
        if changed and args.diff:
            sys.stdout.write(render_diff(f, old, new))
        if changed:
            drift += 1

    print()
    if drift and not write:
        print(f'❌ Doc drift detected ({drift} file(s)).')
        print('   Run ./scripts/sync-docs.py to refresh, then commit.')
        return 1
    if drift:
        print(f'✓ Synced {drift} file(s).')
    else:
        print('✓ All in sync.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
