#!/usr/bin/env python3
"""Fail on private data that a later commit cannot take back.

A stale count gets corrected next PR. A machine path, a personal address or a
credential is scraped the moment it lands on a public repo, and rewriting the
history afterwards costs a force-push that every clone and fork has to follow.
So this runs on the PR, not on the release.

The leak this exists for was not hand-written. `pip-compile` records the path it
resolved from as a comment inside requirements.txt:

    # via -r <sandbox-root>/-Users-<name>-<project>/<uuid>/scratchpad/requirements.in

Note the shape: the home directory arrives DASH-MANGLED (`-Users-<name>-`), not as
`/Users/<name>/`. A guard that only looks for a leading slash sails straight past
it, which is exactly what happened — the line shipped to a public repo inside a
routine dependency bump and stayed for two commits.

Checks, in order of how quietly each one fails:

  MACHINE PATHS   home directories and sandbox roots, in both slash and dash form.
                  `/Users/<you>/` is the documented placeholder and is allowed.

  OPERATOR NAME   matched by SHA-256 of each path-ish token, never by literal.
                  A denylist written in plain text would republish, in the guard,
                  the exact string the guard exists to keep out of the repo.

  PERSONAL MAIL   free-mail providers only. This corpus cites hundreds of official
                  land-registry, school and police addresses as primary sources —
                  those are the reference data, not a leak. A personal inbox is.

  SECRET SHAPES   private keys, credentialed URLs, auth headers, assigned literals.
                  GitHub scans provider tokens on public repos for free; the generic
                  shapes need an org-owned repo on Team+ with Secret Protection,
                  which this is not.

Run locally with `python3 scripts/check-hygiene.py`; CI runs the same script.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# SHA-256 of operator identifiers that must never appear. Hashed, so this file
# never becomes the thing it is guarding against.
#
# That is not a stylistic preference. The guard this replaces grepped for the
# maintainer's real worked-example address as a plaintext literal, which meant
# the workflow file published, on a public repo, the exact address it existed to
# keep out — and the fork copied it. A guard must never be the disclosure.
BANNED_TOKENS = {"95aae01e3ad9faaf0679cff78c8948fd"}

# Multi-word values (addresses, names) can't be caught token-by-token without
# matching common words, so they are hashed as normalized word n-grams instead.
BANNED_PHRASES = {"03225ba2fa07feadb6bc7e4f63def253"}
PHRASE_LENGTHS = range(2, 7)

# `<you>` and `<user>` are the documented placeholders in install docs.
PLACEHOLDER = re.compile(r"/(Users|home)/<[a-z]+>/")

MACHINE_PATHS = [
    (r"/private/tmp/claude-[0-9]+/", "agent sandbox path"),
    (r"/Users/(?!<)[A-Za-z0-9._-]+/", "macOS home directory"),
    (r"(?<![\w-])-Users-[A-Za-z0-9._-]+-", "dash-mangled macOS home directory"),
    (r"/home/(?!<)[A-Za-z0-9._-]+/\.(cache|config|local)/", "Linux home directory"),
]

FREE_MAIL = re.compile(
    r"[a-zA-Z0-9._%+-]+@(gmail|googlemail|yahoo|hotmail|outlook|live|icloud|me|"
    r"proton|protonmail|gmx|web|seznam|aol|mail)\.[a-z.]{2,}",
    re.I,
)

SECRET_SHAPES = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
    (r"[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s:@]+@", "credentialed connection string"),
    (r"(?i)authorization\s*:\s*(bearer|basic)\s+[A-Za-z0-9._~+/=\-]{16,}",
     "auth header carrying a credential"),
    (r"(?i)\b(api[_-]?key|secret|token|password|passwd|credential)s?\b\W{0,3}[:=]\s*"
     r"[\"'][A-Za-z0-9/+_.\-]{16,}[\"']", "assigned credential literal"),
]

TEXT_SUFFIXES = {".md", ".py", ".sh", ".json", ".yml", ".yaml", ".txt", ".in", ".toml", ".cfg"}


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return [ROOT / p for p in out.split("\0") if p]


def main():
    failures = []
    for f in tracked_files():
        # This file carries every pattern by definition; scanning it would make
        # the guard fail on itself.
        if f.suffix not in TEXT_SUFFIXES or f.name == "check-hygiene.py" or not f.exists():
            continue
        rel = f.relative_to(ROOT)
        for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
            where = f"{rel}:{i}"
            for token in re.findall(r"[A-Za-z0-9._-]{4,}", line):
                if hashlib.sha256(token.lower().encode()).hexdigest()[:32] in BANNED_TOKENS:
                    failures.append(f"{where}: operator identifier — use a placeholder")
            words = re.sub(r"[^a-z0-9]+", " ", line.lower()).split()
            for n in PHRASE_LENGTHS:
                for start in range(len(words) - n + 1):
                    phrase = " ".join(words[start:start + n])
                    if hashlib.sha256(phrase.encode()).hexdigest()[:32] in BANNED_PHRASES:
                        failures.append(f"{where}: private worked-example value — use a placeholder")
            for pattern, what in MACHINE_PATHS:
                for m in re.finditer(pattern, line):
                    if not PLACEHOLDER.search(m.group(0)):
                        failures.append(f"{where}: {what} — write a placeholder instead")
            for m in FREE_MAIL.finditer(line):
                failures.append(f"{where}: personal email {m.group(0)}")
            for pattern, what in SECRET_SHAPES:
                if re.search(pattern, line):
                    failures.append(f"{where}: {what} — never commit a live credential")

    if failures:
        print(f"✘ {len(failures)} hygiene failure(s):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("✔ hygiene clean — no machine paths, operator identifiers, personal mail, or secrets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
