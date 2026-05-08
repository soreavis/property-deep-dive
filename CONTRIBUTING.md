# Contributing

Thanks for considering a contribution. The most valuable contributions are **factual corrections** and **new countries**, in roughly that order — getting one wrong tax rate fixed is worth more than a stylistic refactor.

## Quick map of where to contribute

All paths below are relative to the repo root. The skill payload lives under `skills/property-deep-dive/` so that plugin hosts (Claude Code, Claude Cowork) ship the entire skill from a single folder.

| What | Where |
|---|---|
| Add or update a country playbook | `skills/property-deep-dive/countries/<iso2>/playbook.md` |
| Log a new tax/visa/regulatory reform | `skills/property-deep-dive/shared/regulatory-watch.md` |
| Fix a broken URL | the relevant `skills/property-deep-dive/countries/<iso2>/playbook.md` or `skills/property-deep-dive/shared/<topic>.md` |
| Add a universal section flag | new file in `skills/property-deep-dive/shared/`, register in `skills/property-deep-dive/SKILL.md` argument-hint + Sections table |
| Add a tooling doc | `skills/property-deep-dive/shared/<tool-name>.md`, register in `skills/property-deep-dive/SKILL.md` |
| Fix anti-hallucination behaviour | `skills/property-deep-dive/shared/anti-hallucination.md` |

## Adding a new country

The bar is **FR/IT/CZ/SK density** (~400-500 lines, all 26 sections covered with primary government sources — note: --crime/amenities/climate/permits/agent/scams/language inherit from `shared/`, country playbook implements 7 core sections). See `skills/property-deep-dive/countries/fr/playbook.md` as the canonical example.

Required structure:

1. **Cadastre + listing platforms** (1-2 primary, 2-3 listing aggregators)
2. **Traffic data sources** (where available)
3. **Tax structure** — annual + transaction taxes, with current-year rates
4. **Rental regulations** — short-let regime, recent reforms (2025-2026 specifics)
5. **Risk registries** — flood / earthquake / radon / landslide as applicable
6. **Mains drains / utilities** — operators, connection check process
7. **Mandatory diagnostics** — what's required pre-sale
8. **Country-specific quirks** — legal forms, ownership types, build-era hazards
9. **Source URL templates table** at the bottom
10. **Status footer** with confidence label and `**Last verified**: YYYY-MM-DD`

Before submitting:

- Run `--update --validate-only --country=<iso2>` to confirm URL liveness
- Cite **primary government sources** for tax rates, not aggregator sites
- Date-stamp every numeric fact with `(<year> data)`
- Match the section headers used in existing playbooks
- Add the country to `SKILL.md` country support matrix
- If you find an error in another country during research, fix it in the same PR with a separate commit

## Logging a regulatory-watch entry

`skills/property-deep-dive/shared/regulatory-watch.md` is the single source of truth for "what changed when". Format:

```markdown
- `<effective_date> | <topic> | <one-line summary> | <source name> | <verified_date> | <revisit_by> | <tier> | <sections>`
```

- `<topic>` ∈ tax / rental / visa / finance / ownership / esg / cadastre / eurozone / other
- `<tier>` ∈ 1 (CRITICAL — reverses prior assertion) / 2 (MAJOR — material number change) / 3 (MEANINGFUL — threshold tweak) / 4 (INCREMENTAL — indexation)
- `<sections>` = the `--<flag>` sections this reform affects in country playbooks

ENDED-program registry entries (Tier 1, anti-hallucination critical) go in the ENDED Programs table in the same file.

## Anti-hallucination contract

This is non-negotiable. Every claim must be one of:

- **Sourced** to a primary government / regulated entity / cited secondary aggregator
- **Computed** transparently (inputs visible)
- **Estimated** with a `~` or `est.` prefix and a calibration sentence

Forbidden phrasings: "approximately X", "in the area of", "typical for the region", "as of recent data", "industry average", "experts say", "studies show", "should be around", "is likely connected to".

If a number can't be sourced, write `data not publicly available — verify at <authoritative source>` rather than guessing.

The seven mandatory pre-output checks are documented in `skills/property-deep-dive/shared/anti-hallucination.md`.

## URL hygiene

- All URLs must be reachable as of the PR date
- For URLs behind bot protection (Cloudflare / DataDome), tag them as `(bot-protected; browser-OK)`
- For redirects, prefer the canonical destination URL
- For dead URLs, find the replacement on the same primary source domain — do not silently delete

## CI conventions (for PRs that touch `.github/workflows/`)

- **Third-party actions must be pinned to commit SHA** with a trailing `# <tag>` comment, e.g. `uses: ossf/scorecard-action@62b2cac…  # v2.4.0`. Run `./scripts/pin-actions.sh` after editing a workflow to refresh SHAs (Dependabot tracks the trailing tag comment so updates still arrive automatically)
- **First-party actions** (`actions/*`, `github/*`) stay on major-version tags (`@v4`, `@v5`) — these orgs maintain their tag history carefully, and pinning to SHA produces unnecessary Dependabot churn
- **Permissions block required** — every workflow declares an explicit `permissions:` block scoped to least-privilege (`contents: read` by default, `issues: write` / `pull-requests: write` only where needed)
- **Timeouts required** — every job sets `timeout-minutes:` (default budget: 5 min for PR-validate, 30 min for url-liveness)
- **No secrets in workflows** — the skill ships markdown only; all data sources are public. Workflows that try to read a secret fail review

## PR checklist

```
- [ ] Anti-hallucination contract followed (forbidden phrasings absent; numbers sourced/computed/hedged)
- [ ] All URLs validated (HEAD or GET 2xx; bot-protected exceptions tagged)
- [ ] Country support matrix updated in SKILL.md (if new country)
- [ ] regulatory-watch.md updated (if reform-driven change)
- [ ] Status footer present with confidence label + Last verified date
- [ ] No personal addresses or identifiers (use generic worked examples)
- [ ] No `_local/` or `*.bak-*` artifacts staged
- [ ] If touching universal logic in skills/property-deep-dive/shared/, all affected country playbooks remain consistent
```

## Commit message style

Follow conventional commits:

- `feat(<iso2>): add <country> playbook` — new country
- `fix(<iso2>): correct <topic> rate from X to Y` — factual correction
- `docs(regulatory-watch): log <reform>` — new regulatory entry
- `chore(urls): replace <count> dead URLs across <countries>` — URL maintenance
- `feat(shared): add <section-name> universal section` — new universal layer
- `refactor(shared): <change>` — structural change to shared logic

## Review philosophy

Maintainers prioritise:

1. **Accuracy over completeness** — a half-populated playbook with verified facts beats a full one with guesses
2. **Citation quality** — primary government > secondary aggregator > listing
3. **Current-year specificity** — 2026 reforms surface dated; 2024 figures flagged as `(<year> data)`
4. **Anti-hallucination compliance** — calibrated hedging, no forbidden phrasings
5. **Source-decay awareness** — reform dates surface, ENDED programs flagged, EPC ban schedules dated

Everything else (formatting, prose polish, structural reorganisation) is welcome but secondary.

## Release process (maintainer-only)

When cutting a new release tag:

1. **Bump `.claude-plugin/plugin.json` `version`** to match the new tag (e.g., `2026.05.0`).
   - Plugin users only get updates when this field changes — keep it in sync with the latest CalVer git tag.
   - End-of-month `auto-tag.yml` cron creates the git tag automatically; manual bump of `plugin.json` is part of the same PR or a follow-up.
2. **Confirm `CHANGELOG.md` `[Unreleased]` is rolled into a `[YYYY.0M.MICRO]` section** for the new tag.
3. **Push the tag** (or let `auto-tag.yml` do it). `release-notes.yml` and `sign-release.yml` fire on the tag push (sigstore + SLSA L3 attestations).
4. **Optionally update the plugin manifest description / keywords** if the release adds new countries or sections.

The plugin manifest lives at `.claude-plugin/plugin.json`. The marketplace stub at `.claude-plugin/marketplace.json` makes the repo self-installable via `/plugin marketplace add github:soreavis/property-deep-dive`.
