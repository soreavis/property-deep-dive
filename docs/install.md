# Installation

`property-deep-dive` ships as a [Claude](https://claude.com) plugin that runs in both **[Claude Code](https://docs.claude.com/claude-code)** (slash commands) and **[Claude Cowork](https://www.anthropic.com/product/claude-cowork)** (in-app). The plugin format is identical for both — `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` + `skills/property-deep-dive/SKILL.md` — so the same skill bundle ships to both products. Only the install UX differs.

## Prerequisites

- macOS, Linux, or WSL
- A Claude Code or Claude Cowork session
- Git (only for the manual symlink path below)

## Claude Code (slash commands)

```
/plugin marketplace add github:soreavis/property-deep-dive
/plugin install property-deep-dive@property-deep-dive
```

The skill is now invocable via `/property-deep-dive` in any Claude Code session. The plugin manifest pins to a specific [CalVer](#pinning-to-a-specific-release) release — you'll get updates only when a new version is published, not on every commit.

## Claude Cowork (in-app)

Cowork installs plugins from its own in-app plugin browser. Per [Anthropic's launch post](https://claude.com/blog/cowork-plugins) (2026-01-30): _"Easily install these directly from Cowork, browse the full collection on our website, or upload your own plugin."_

To install this third-party plugin, follow Cowork's "upload your own plugin" path with the GitHub URL `github:soreavis/property-deep-dive`. The exact UI may evolve — defer to the [linked blog post](https://claude.com/blog/cowork-plugins) and [Anthropic's curated plugin repo](https://github.com/anthropics/knowledge-work-plugins) for the current flow.

> **Cowork install scope (as of 2026-04)**: plugins save **locally per user**, not workspace-wide. Each teammate installs their own copy. Anthropic notes _"better support for org-wide sharing and management … coming in the weeks ahead"_ — this page will be updated when that lands.

## Manual symlink (Claude Code only — for skill development / contributing)

If you want to hack on the skill locally and pick up edits immediately without going through the plugin marketplace:

```bash
# 1. Clone the repo wherever you keep code
git clone https://github.com/soreavis/property-deep-dive ~/code/property-deep-dive

# 2. Symlink the SKILL SUBDIRECTORY (not the whole repo) into Claude Code's skills directory
#    Claude Code expects SKILL.md at the symlink's root.
ln -s ~/code/property-deep-dive/skills/property-deep-dive ~/.claude/skills/property-deep-dive

# 3. Verify Claude Code finds it
ls -la ~/.claude/skills/property-deep-dive
```

The skill is now invocable via `/property-deep-dive` with edits picked up immediately. SKILL.md, `shared/`, and `countries/` all live under `skills/property-deep-dive/`, so the skill is fully self-contained.

Cowork has no `~/.claude/skills/` equivalent — for Cowork local development use the "upload your own plugin" path described above.

## Verify

Open a Claude Code session and type `/p` — `/property-deep-dive` should appear in the slash-command picker. Or invoke directly with a worked example:

```
/property-deep-dive Calle Mayor 5, 28013 Madrid --visa --retirement
```

If the command isn't recognised:
- **Plugin install path**: confirm the plugin loaded with `/plugin list`
- **Manual symlink path**: confirm the symlink resolves with `readlink ~/.claude/skills/property-deep-dive` (expected: `…/code/property-deep-dive/skills/property-deep-dive`)

## Updating

### Plugin install
The plugin manifest pins to a CalVer release. To update:

```
/plugin update property-deep-dive
```

### Manual symlink
```bash
cd ~/code/property-deep-dive
git pull
```

The symlink stays in place; updates are visible to Claude Code immediately.

## Uninstalling

### Plugin install
```
/plugin uninstall property-deep-dive
```

### Manual symlink
```bash
rm ~/.claude/skills/property-deep-dive
# Optionally also remove the cloned source:
rm -rf ~/code/property-deep-dive
```

The skill leaves no other artefacts on your system.

## Pinning to a specific release

If you'd rather pin to a tagged release than `main`:

```bash
cd ~/code/property-deep-dive
git fetch --tags
git checkout 2026.07.0     # or any later tag — see CHANGELOG.md
```

Tags follow CalVer (`YYYY.0M.MICRO`) — see [CHANGELOG.md](../CHANGELOG.md) for release notes per tag.

## Verifying release authenticity

Releases are sigstore-signed. To verify the tarball:

```bash
gh release download 2026.07.0 --repo soreavis/property-deep-dive \
  --pattern 'property-deep-dive-2026.07.0.tar.gz' \
  --pattern 'property-deep-dive-2026.07.0.tar.gz.sigstore'

cosign verify-blob \
  --bundle property-deep-dive-2026.07.0.tar.gz.sigstore \
  --certificate-identity-regexp 'https://github\.com/soreavis/property-deep-dive/\.github/workflows/sign-release\.yml@.*' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  property-deep-dive-2026.07.0.tar.gz
```

Expected output: `Verified OK`. Anything else means the tarball doesn't match what was signed at that tag.
