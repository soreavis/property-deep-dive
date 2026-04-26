#!/usr/bin/env bash
# scripts/pin-actions.sh
#
# Pin third-party GitHub Actions to commit SHA in .github/workflows/*.yml.
#
# - First-party actions (`actions/*`, `github/*`) are kept on major-version tags.
# - Third-party actions are rewritten as `<owner>/<repo>@<sha>  # <tag>` so:
#   - Dependabot still updates them (it tracks the trailing `# <tag>` comment)
#   - Reviewers still see the human-readable version
#   - The actual fetch is SHA-pinned (supply-chain hardening)
#
# Requires: gh CLI authenticated, jq.
#
# Usage:
#   ./scripts/pin-actions.sh           # write changes in place
#   DRY_RUN=1 ./scripts/pin-actions.sh # just print the planned changes
#
# This script is idempotent. Re-running it after a tag change refreshes the SHAs.

set -euo pipefail

WORKFLOWS_DIR="${WORKFLOWS_DIR:-.github/workflows}"
DRY_RUN="${DRY_RUN:-0}"

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: gh CLI is required (https://cli.github.com)." >&2
  exit 1
fi

is_first_party() {
  case "$1" in
    actions/*|github/*) return 0 ;;
    *)                  return 1 ;;
  esac
}

is_sha() {
  [[ "$1" =~ ^[a-f0-9]{40}$ ]]
}

resolve_sha() {
  local action="$1" tag="$2"
  # Tag may be either a lightweight tag (returns commit SHA) or annotated tag (returns tag SHA → dereference).
  local sha
  sha=$(gh api "repos/${action}/commits/${tag}" --jq '.sha' 2>/dev/null || true)
  if [ -z "$sha" ]; then
    sha=$(gh api "repos/${action}/git/ref/tags/${tag}" --jq '.object.sha' 2>/dev/null || true)
  fi
  printf '%s' "$sha"
}

shopt -s nullglob
files=( "$WORKFLOWS_DIR"/*.yml "$WORKFLOWS_DIR"/*.yaml )
[ "${#files[@]}" -eq 0 ] && { echo "No workflow files found in $WORKFLOWS_DIR"; exit 0; }

total_pinned=0
total_skipped=0
total_failed=0

for wf in "${files[@]}"; do
  echo "Inspecting $wf"
  # Read entire file, replace each `uses: <owner>/<repo>@<tag>` line where applicable.
  tmp="$(mktemp)"
  while IFS= read -r line; do
    if [[ "$line" =~ ^([[:space:]]+uses:[[:space:]]+)([^/[:space:]]+/[^@[:space:]]+)@([^[:space:]#]+)(.*)$ ]]; then
      indent="${BASH_REMATCH[1]}"
      action="${BASH_REMATCH[2]}"
      ref="${BASH_REMATCH[3]}"
      trailing="${BASH_REMATCH[4]}"

      if is_sha "$ref"; then
        printf '%s\n' "$line" >> "$tmp"
        continue
      fi
      if is_first_party "$action"; then
        printf '%s\n' "$line" >> "$tmp"
        continue
      fi

      sha=$(resolve_sha "$action" "$ref")
      if [ -n "$sha" ]; then
        printf '%s%s@%s  # %s\n' "$indent" "$action" "$sha" "$ref" >> "$tmp"
        echo "  pin  $action@$ref → @${sha:0:7}…"
        total_pinned=$((total_pinned+1))
      else
        printf '%s\n' "$line" >> "$tmp"
        echo "  ✗    could not resolve $action@$ref"
        total_failed=$((total_failed+1))
      fi
    else
      printf '%s\n' "$line" >> "$tmp"
    fi
  done < "$wf"

  if [ "$DRY_RUN" = "1" ]; then
    if ! cmp -s "$wf" "$tmp"; then
      echo "(dry-run — diff would be:)"
      diff -u "$wf" "$tmp" || true
    fi
    rm -f "$tmp"
  else
    if cmp -s "$wf" "$tmp"; then
      rm -f "$tmp"
    else
      mv "$tmp" "$wf"
    fi
  fi
done

echo
echo "Summary:"
echo "  pinned:  $total_pinned"
echo "  failed:  $total_failed"
[ "$DRY_RUN" = "1" ] && echo "  (dry-run — no files changed)"
