# Installation

`property-deep-dive` is a [Claude Code](https://docs.claude.com/claude-code) skill. It runs inside Claude Code as a slash command (`/property-deep-dive`) and ships only Markdown text — no compilation, no runtime dependencies beyond Claude Code itself.

## Prerequisites

- macOS, Linux, or WSL
- Git
- [Claude Code](https://docs.claude.com/claude-code) installed and authenticated

## Install

```bash
# 1. Clone the repo wherever you keep code
git clone https://github.com/soreavis/property-deep-dive ~/code/property-deep-dive

# 2. Symlink into Claude Code's user skills directory
ln -s ~/code/property-deep-dive ~/.claude/skills/property-deep-dive

# 3. Verify Claude Code finds it
ls -la ~/.claude/skills/property-deep-dive
```

The skill is now invocable via `/property-deep-dive` in any Claude Code session.

## Verify

Open a Claude Code session and type `/p` — `/property-deep-dive` should appear in the slash-command picker. Or invoke directly:

```
/property-deep-dive --help
```

If the command is not recognised, double-check that the symlink resolves:

```bash
readlink ~/.claude/skills/property-deep-dive
# expected: /Users/<you>/code/property-deep-dive
```

## Updating

```bash
cd ~/code/property-deep-dive
git pull
```

The symlink stays in place; updates are visible to Claude Code immediately.

## Uninstalling

```bash
rm ~/.claude/skills/property-deep-dive
# Optionally also remove the cloned source:
rm -rf ~/code/property-deep-dive
```

The skill leaves no other artefacts on your system.

## Pinning to a specific release

If you'd rather use a tagged release than `main`:

```bash
cd ~/code/property-deep-dive
git fetch --tags
git checkout 2026.04.0     # or any later tag
```

Tags follow CalVer (`YYYY.0M.MICRO`) — see [CHANGELOG.md](../CHANGELOG.md) for release notes per tag.

## Verifying release authenticity

Releases are sigstore-signed. To verify the tarball:

```bash
gh release download 2026.04.0 --repo soreavis/property-deep-dive \
  --pattern 'property-deep-dive-2026.04.0.tar.gz' \
  --pattern 'property-deep-dive-2026.04.0.tar.gz.sigstore'

cosign verify-blob \
  --bundle property-deep-dive-2026.04.0.tar.gz.sigstore \
  --certificate-identity-regexp 'https://github\.com/soreavis/property-deep-dive/\.github/workflows/sign-release\.yml@.*' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  property-deep-dive-2026.04.0.tar.gz
```

Expected output: `Verified OK`. Anything else means the tarball doesn't match what was signed at that tag.
