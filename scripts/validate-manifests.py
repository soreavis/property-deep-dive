#!/usr/bin/env python3
"""Check the per-platform manifests against each other and against the Agent Skills spec.

The skill ships to Claude Code, Codex, Cursor, Gemini CLI, Grok, Copilot and anything
reading the agentskills.io standard — one skill tree, many thin manifests. Two things
rot silently:

1. **Version drift.** `.claude-plugin/plugin.json` is the CalVer source of truth
   (`scripts/next-version.py`). A manifest left behind advertises a stale version to
   that platform's updater, so users never get the release.

2. **Spec violations.** A `description` over 1024 chars is not degraded — the skill is
   *silently dropped* from the loader's skill list with no warning and no error
   (github/copilot-cli#3494). Nothing else in CI reads SKILL.md frontmatter.

Run: python3 scripts/validate-manifests.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = '.claude-plugin/plugin.json'

# manifest path -> path to its version value
MANIFESTS: dict[str, tuple] = {
    '.claude-plugin/plugin.json': ('version',),
    '.claude-plugin/marketplace.json': ('plugins', 0, 'version'),
    '.codex-plugin/plugin.json': ('version',),
    '.cursor-plugin/plugin.json': ('version',),
    '.grok-plugin/plugin.json': ('version',),
    '.grok-plugin/marketplace.json': ('plugins', 0, 'version'),
    '.agents/plugins/marketplace.json': ('plugins', 0, 'version'),
    'gemini-extension.json': ('version',),
}

# Agent Skills spec limits.
NAME_MAX = 64
DESCRIPTION_MAX = 1024
SPEC_FIELDS = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
# Claude Code extensions: fine to ship (conformant runtimes ignore unknown keys), but
# scripts/build-skill-zips.sh strips them so the claude.ai uploader never sees them.
KNOWN_EXTENSIONS = {'user-invocable', 'argument-hint', 'disable-model-invocation'}

failures: list[str] = []


def dig(obj, path):
    for key in path:
        obj = obj[key]
    return obj


def check_versions() -> str:
    version = json.loads((ROOT / SOURCE).read_text())['version']
    if not re.fullmatch(r'\d{4}\.(0[1-9]|1[0-2])\.\d+', version):
        failures.append(f'{SOURCE}: {version!r} is not CalVer YYYY.0M.MICRO')
    for path, keys in MANIFESTS.items():
        f = ROOT / path
        if not f.exists():
            failures.append(f'{path}: missing — every platform lane needs its manifest')
            continue
        try:
            found = dig(json.loads(f.read_text()), keys)
        except (KeyError, IndexError):
            failures.append(f'{path}: no version at {".".join(map(str, keys))}')
            continue
        if found != version:
            failures.append(
                f'{path}: version {found!r} != {version!r} from {SOURCE} — '
                f'run `python3 scripts/next-version.py --write` to resync')
    return version


def check_skills() -> None:
    for skill_md in sorted((ROOT / 'skills').glob('*/SKILL.md')):
        folder = skill_md.parent.name
        m = re.match(r'^---\n(.*?)\n---', skill_md.read_text(), re.S)
        if not m:
            failures.append(f'{skill_md.relative_to(ROOT)}: no YAML frontmatter')
            continue
        try:
            import yaml
            fm = yaml.safe_load(m.group(1))
        except Exception as exc:
            failures.append(f'{skill_md.relative_to(ROOT)}: frontmatter does not parse — {exc}')
            continue

        rel = skill_md.relative_to(ROOT)
        name = fm.get('name', '')
        if name != folder:
            failures.append(f'{rel}: name {name!r} must equal its folder name {folder!r} or the skill will not load')
        if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', str(name)):
            failures.append(f'{rel}: name {name!r} must be lowercase alphanumeric with single hyphens')
        if len(str(name)) > NAME_MAX:
            failures.append(f'{rel}: name is {len(str(name))} chars, cap is {NAME_MAX}')

        desc = fm.get('description', '')
        if not desc:
            failures.append(f'{rel}: description is required')
        elif len(desc) > DESCRIPTION_MAX:
            failures.append(
                f'{rel}: description is {len(desc)} chars, spec cap is {DESCRIPTION_MAX} — '
                f'over-cap skills are silently dropped from the loader, not warned about')

        unknown = set(fm) - SPEC_FIELDS - KNOWN_EXTENSIONS
        if unknown:
            failures.append(f'{rel}: unrecognised frontmatter field(s) {sorted(unknown)}')


def main() -> int:
    version = check_versions()
    check_skills()

    if failures:
        print(f'❌ {len(failures)} manifest/spec problem(s):\n')
        for f in failures:
            print(f'  {f}')
        return 1

    print(f'✓ {len(MANIFESTS)} manifests in lockstep at {version}; skills match the Agent Skills spec')
    return 0


if __name__ == '__main__':
    sys.exit(main())
