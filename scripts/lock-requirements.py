#!/usr/bin/env python3
"""Regenerate the hash-pinned requirements.txt from requirements.in.

Wraps `uv pip compile` for one reason: the raw command **destroys the header**.
`requirements.txt` opens with an 18-line comment block explaining what the file
is for, that the skill itself needs none of it, and — the part that matters —
how to regenerate it. Running the documented command with `-o requirements.txt`
overwrites all of that, so the file silently loses its own instructions the
first time anyone follows them.

This script reads the existing leading comment block, regenerates the body, and
writes them back together. Hand edits to the header survive.

Resolution deliberately targets the CI runner rather than the machine you are
sitting at: `--python-version` matches `python-version:` in source-verify.yml and
url-liveness.yml, and `--python-platform` pins the Linux runners. Hashes still
cover every platform wheel of each resolved version, so the lock installs fine
on macOS too.

Version bumps are normally Dependabot's job, not yours — it edits requirements.in
and regenerates the hashes in place. Reach for this when you ADD or REMOVE a
package, or change a constraint by hand.

Usage:
    ./scripts/lock-requirements.py           # regenerate in place
    ./scripts/lock-requirements.py --check   # fail if the lock is stale (CI-safe)
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'requirements.in'
LOCK = ROOT / 'requirements.txt'

# Keep in step with `python-version:` in source-verify.yml + url-liveness.yml.
PYTHON_VERSION = '3.12'
PLATFORM = 'x86_64-unknown-linux-gnu'


def header_of(path: Path) -> str:
    """Leading comment block, up to the first non-comment, non-blank line."""
    if not path.exists():
        return ''
    kept: list[str] = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or not line.strip():
            kept.append(line)
        else:
            break
    return '\n'.join(kept).rstrip('\n')


def compile_body() -> str:
    if not shutil.which('uv'):
        sys.exit("ERROR: `uv` not found. Install it (https://docs.astral.sh/uv/) "
                 "or regenerate with `pip-compile --generate-hashes`.")
    with tempfile.NamedTemporaryFile(suffix='.txt') as tmp:
        subprocess.run(
            ['uv', 'pip', 'compile', str(SRC), '--generate-hashes', '--no-header',
             '--python-version', PYTHON_VERSION, '--python-platform', PLATFORM,
             '-o', tmp.name],
            check=True, capture_output=True, text=True,
        )
        return Path(tmp.name).read_text(encoding='utf-8').strip('\n')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true',
                    help='exit 1 if requirements.txt is not what requirements.in produces')
    args = ap.parse_args()

    if not SRC.exists():
        sys.exit(f'ERROR: {SRC} not found')

    rendered = header_of(LOCK) + '\n\n' + compile_body() + '\n'

    if args.check:
        if LOCK.exists() and LOCK.read_text(encoding='utf-8') == rendered:
            print('✓ requirements.txt is in sync with requirements.in')
            return 0
        print('❌ requirements.txt is stale — requirements.in has changes that were '
              'never compiled in.\n   Run ./scripts/lock-requirements.py and commit the result.')
        return 1

    LOCK.write_text(rendered, encoding='utf-8')
    pins = [l for l in rendered.splitlines() if l and not l.startswith((' ', '#'))]
    print(f'✓ regenerated {LOCK.name} — {len(pins)} pinned package(s), '
          f'header preserved ({len(header_of(LOCK).splitlines())} lines)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
