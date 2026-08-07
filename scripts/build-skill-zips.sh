#!/usr/bin/env bash
# Build one zip per skill for runtimes that take skill folders rather than a plugin
# (claude.ai Customize → Skills, ChatGPT Skills → Upload).
#
# The zip root must be the skill folder itself, and that folder name must equal the
# SKILL.md `name` field, or the upload is rejected.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills="$root/skills"
dist="$root/dist"
rm -rf "$dist"
mkdir -p "$dist"

for skill in "$skills"/*/; do
  name="$(basename "$skill")"
  staging="$(mktemp -d)"
  cp -R "$skill" "$staging/$name"

  # user-invocable and argument-hint are Claude Code extensions, not part of the open
  # Agent Skills spec. Drop them so the claude.ai uploader never sees an unknown field.
  # Written portably: BSD and GNU sed disagree on in-place editing.
  sed -e '/^user-invocable:/d' -e '/^argument-hint:/d' \
    "$staging/$name/SKILL.md" > "$staging/SKILL.md.tmp"
  mv "$staging/SKILL.md.tmp" "$staging/$name/SKILL.md"

  # -x keeps macOS/editor droppings out of a published artifact.
  (cd "$staging" && zip -qr "$dist/$name.zip" "$name" \
    -x '*/.DS_Store' '*/__pycache__/*' '*/.git/*' '*.bak-*')
  rm -rf "$staging"
  echo "dist/$name.zip  ($(du -h "$dist/$name.zip" | cut -f1))"
done
