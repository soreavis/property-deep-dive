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

Resolution preserves the versions already pinned in requirements.txt. The check
answers "does this lock match requirements.in", never "has anything newer shipped"
— otherwise an upstream release inside an existing range (`pypdf>=6.14.2,<7`)
would turn main red with no commit behind it. Use --upgrade to take the bumps.

Usage:
    ./scripts/lock-requirements.py             # regenerate in place, keeping pins
    ./scripts/lock-requirements.py --upgrade   # ...and take newer allowed versions
    ./scripts/lock-requirements.py --check     # fail if the lock is stale (CI-safe)
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


def compile_body(upgrade: bool = False) -> str:
    if not shutil.which('uv'):
        sys.exit("ERROR: `uv` not found. Install it (https://docs.astral.sh/uv/) "
                 "or regenerate with `pip-compile --generate-hashes`.")
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir) / 'requirements.txt'
        # Seed the output with the current lock. Without existing pins to read, uv
        # resolves every RANGE in requirements.in (`pypdf>=6.14.2,<7`) to whatever
        # the index serves *today*, so the first upstream release inside the range
        # makes --check fail on a tree nobody touched — main goes red repo-wide and
        # every PR blocks. Seeding makes the pins the preference set, so this only
        # reports stale when requirements.in actually changed. `--upgrade` is the
        # documented way to opt into bumps.
        if LOCK.exists() and not upgrade:
            out.write_text(LOCK.read_text(encoding='utf-8'), encoding='utf-8')
        cmd = ['uv', 'pip', 'compile', str(SRC), '--generate-hashes', '--no-header',
               '--python-version', PYTHON_VERSION, '--python-platform', PLATFORM,
               '-o', str(out)]
        if upgrade:
            cmd.append('--upgrade')
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return out.read_text(encoding='utf-8').strip('\n')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true',
                    help='exit 1 if requirements.txt is not what requirements.in produces')
    ap.add_argument('--upgrade', action='store_true',
                    help='also pull newer versions allowed by requirements.in '
                         '(otherwise existing pins are preserved)')
    args = ap.parse_args()

    if not SRC.exists():
        sys.exit(f'ERROR: {SRC} not found')

    rendered = header_of(LOCK) + '\n\n' + compile_body(args.upgrade) + '\n'

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
