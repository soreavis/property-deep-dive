# Changelog

All notable changes to this project are documented here.

## Versioning scheme — CalVer (`YYYY.0M.MICRO`)

This project uses **CalVer** (calendar versioning), not SemVer. Each tag encodes the release month, with a per-month patch counter:

| Component | Meaning |
|---|---|
| `YYYY` | Four-digit year |
| `0M` | Zero-padded month (01–12) |
| `MICRO` | In-month patch counter (0 = monthly cycle release; 1+ = factual corrections, URL fixes, regulatory-watch entries that landed mid-month) |

Examples: `2026.04.0`, `2026.04.1`, `2026.05.0`, `2027.01.0`.

### What triggers a new tag

- **`.0` (monthly cycle)** — at end-of-month, an automated workflow tags `YYYY.0M.0` if any change landed on `main` since the previous tag. No-ops silently when nothing changed.
- **`.1`, `.2`, …** — manual, on factual corrections / URL replacement batches / regulatory-watch entries that supersede a Tier-1 ENDED programme.
- **What does NOT trigger a tag** — typo fixes, formatting, internal refactors, README polish without skill content change.

### Format of each entry

This file follows [Keep a Changelog](https://keepachangelog.com/) adapted for CalVer:

```
## [YYYY.0M.MICRO] - YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Fixed
- ...

### Removed / Deprecated
- ...

### Breaking
- ... (use sparingly — schema or flag-rename changes)

### Security
- ...
```

When a release ends a programme (golden visa scrapped, NHR-style regime closed), it's documented under both `### Removed / Deprecated` AND surfaced in `shared/regulatory-watch.md` ENDED registry.

---

## [Unreleased]

### Added — Tier-1+2 follow-up workflows (2026-04-26)

- `regulatory-watch-revisit.yml` — daily cron, opens (or updates) a single tracking issue listing every regulatory-watch entry whose `revisit_by` date has passed. Auto-closes when the queue empties.
- `auto-tag.yml` — last-day-of-month cron creates `YYYY.0M.0` if commits accumulated since last tag, then dispatches `sign-release.yml` + `release-notes.yml` (works around the GITHUB_TOKEN-pushed-tag silence rule).
- `changelog-on-merge.yml` — on PR merge, opens a sibling PR appending a `### Bucket` line under `[Unreleased]` with title + author + link. Auto-merge handles the bot PR via `auto-merge-docs.yml`.
- `year-roll-reminder.yml` — Jan 1 cron lists every `(YYYY data ...)` stamp dated before the current year, grouped by country.
- `matrix-consistency.yml` — PR + push gate that audits SKILL.md country matrix ↔ `countries/*/playbook.md` directories two-way (no orphans, no missing).
- `transposition-alerts.yml` — daily cron parses `regulatory-watch.md` `effective_date` fields and fires one issue per entry per threshold at T-90/30/14/0 days (idempotent via title).
- `auto-merge-docs.yml` — enables `gh pr merge --auto --squash` on PRs labelled `documentation` from the maintainer or known automation bots (changelog-on-merge, dependabot).
- `source-tier-ratchet.yml` — measures project-wide primary-government URL share at HEAD vs main; sticky PR comment with delta; hard-fails on >5pp regression.
- `sign-release.yml` — added SLSA Level 3 provenance via `slsa-framework/slsa-github-generator` (Scorecard `Signed-Releases` 8 → 10). Now ships **two** independent attestations per release: sigstore keyless + SLSA L3 multiple.intoto.jsonl. Release-notes template documents both verification paths.

### Added — extended community / CI tooling (2026-04-26 prep)

- `pr-validate.yml` — added 2 new jobs: section-completeness (changed playbooks ≥250 lines + key markers) and argument-hint-drift (SKILL.md ↔ README sync)
- `source-tier-audit.yml` — new advisory PR comment showing primary-government vs aggregator URL ratio per changed country playbook
- `link-check.yml` — lychee internal-link check on PR + weekly schedule
- `changelog-enforcer.yml` — require entry under `[Unreleased]` (skippable via labels: `skip changelog`, `documentation`, `ci`, `dependencies`)
- `test-fixtures-check.yml` — monthly check that listing URLs in `shared/test-fixtures.md` still resolve
- `dependabot-auto-merge.yml` — auto-merge patch + minor dependency updates once CI green
- `welcome.yml` — first-PR / first-issue greeter with anti-hallucination contract reminder
- `stale.yml` — mark stale at 60 days, close at 90 (exempts: `health-report`, `url-liveness`, `security`, `regulatory-watch`, `blocked`, `good-first-issue`, `help-wanted`, `new-country`)
- `pr-size.yml` — auto-apply `size/xs` … `size/xl` labels with content-repo-tuned bands
- `labeler.yml` + `.github/labeler.yml` — path-based PR labels (region, country, shared, router, governance, ci, config, anti-hallucination)
- `sign-release.yml` — sigstore keyless signing of release tarball + sha256 + manifest, posted as release assets with a verification snippet appended to the release notes
- `scripts/pin-actions.sh` — idempotent helper that pins third-party action references to commit SHA via `gh api`. First-party (`actions/*`, `github/*`) are kept on major-version tags
- `.github/labels.yml` — added 17 labels: 5 region, country, shared, router, governance, ci, config, anti-hallucination, 5 size, skip-changelog, stale
- Pinned existing third-party action references in `pr-validate.yml`, `scorecard.yml`, `labels-sync.yml` to commit SHA (with `# version` trailing comment so dependabot keeps tracking)

### Changed

- All Node-20 GitHub Actions bumped to Node-24-compatible versions (deprecation warning emitted by GitHub on April 26, 2026): `actions/checkout` v4 → v6.0.2, `actions/setup-python` v5 → v6.2.0, `actions/cache` v4 → v5.0.5, `actions/github-script` v9 → v9.0.0 (fresh SHA), `actions/upload-artifact` v7 → v7.0.1 (comment refresh).
- `sign-release.yml` — added `workflow_dispatch` with required `tag` input so `auto-tag.yml` can chain into it.
- `changelog-enforcer.yml` — dropped `expectedLatestVersion: Unreleased` config. The action's logic treats `versions[1]` as the "latest" once a real release exists, so the setting only works on pre-1.0 repos.
- README architecture diagram updated to reflect the 16-workflow set + `scripts/` folder
- feat(ci): tier-1+2 follow-up workflows · SLSA L3 · Node 24 bump ([#7](https://github.com/soreavis/property-deep-dive/pull/7)) — by @soreavis

## [2026.04.0] - 2026-04-26

### Added

- **Initial public release** — multi-country property due-diligence skill for Claude Code.
- **44 country playbooks** at FR/IT/CZ/SK density (~400-500 lines each, ~26.5k lines total):
  - Europe core (24): FR · IT · CZ · SK · DE · AT · CH · ES · PT · SE · FI · NO · UK · NL · BE · DK · IS · SI · IE · GR · PL · EE · HR · HU
  - Anglo non-EU (3): CA · AU · NZ
  - Latin America (5): MX · BR · AR · CR · PA
  - Western Balkans (5): RS · ME · BA · MK · AL
  - EU completion (7): LT · LV · RO · BG · LU · CY · MT
- **22 user-invocable sections**:
  - Core (10): `--price`, `--traffic`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, `--crime`, `--amenities`, `--climate`
  - Financial / process (5): `--finance`, `--currency`, `--visa`, `--insurance`, `--notary`
  - Decision-context (7): `--compare=<iso2,...>`, `--retirement`, `--digital-nomad`, `--macro`, `--demographics`, `--esg`, `--exit`
- **4 cross-cutting layers**: `--integrity` (4 data-honesty checks), `--journey=<type>` (7 templates: pre-offer / post-offer / foreign-buyer / investor / renovation / gite-bnb / inheritance), `--type=<kind>` (6 specialised templates: off-plan / auction / probate / plot-only / heritage / apartment-vs-house), `--update` (maintenance mode).
- **9 tooling docs** in `shared/`: TCO calculator, mortgage calculator, test fixtures, listing-diff watcher, comparable-transactions DB, auto-validate, price-index feeds, listing aggregators, photo OCR.
- **Governance**: `shared/regulatory-watch.md` (single date-stamped registry of ENDED programmes + recently enacted reforms + EU directive transposition deadlines), `shared/anti-hallucination.md` (7 mandatory pre-output checks, source-tier ranking, forbidden phrasings).
- **Auto-downgrade rule** (`shared/updater.md` § Auto-downgrade): confidence labels decay over time without re-verification — HIGH → MEDIUM at 6 months, LOW at 12 months, STALE at 18 months. Computed at render time, not only during `--update`.
- **Maintenance CI**:
  - `.github/workflows/url-liveness.yml` (weekly) — curl HEAD on every URL across the repo; opens issue if score <85%.
  - `.github/workflows/health-report.yml` (monthly) — parses `Last verified` dates, renders decay matrix, posts to pinned issue.
  - `.github/workflows/feed-watcher.yml` (every 6h) — EU Official Journal + ECJ press RSS → opens issue when property-relevant directives land.
- **PR validation CI** (`.github/workflows/pr-validate.yml`):
  - markdownlint across all `.md`
  - Forbidden-phrasing scan (anti-hallucination contract)
  - Status footer + `**Last verified**` stamp check on changed playbooks
  - Personal-data leak guard
- **OpenSSF Scorecard** (`.github/workflows/scorecard.yml`) — weekly + on push to `main`.
- **Release automation** (`.github/workflows/release-notes.yml`) — on tag push matching `YYYY.0M.MICRO`, classify changed files into Country / Shared / Regulatory-watch / Router buckets and draft release notes.
- **Label sync** (`.github/labels.yml` + `.github/workflows/labels-sync.yml`) — repository labels managed as code.
- **Dependabot** (`.github/dependabot.yml`) — monthly action-version PRs, grouped.
- **CODEOWNERS** — defaults to `@soreavis`, governance files (anti-hallucination, regulatory-watch, updater, sections, output-template, verdict-bands, SKILL.md) explicit.
- **Issue templates**: factual-correction, broken-url, new-country, regulatory-watch + config that disables blank issues.
- **Pull request template** mirroring CONTRIBUTING.md PR checklist.
- **CODE_OF_CONDUCT.md** — Contributor Covenant 2.1 with project-specific factual-rigor + honest-hedging norms.
- **SECURITY.md** — vulnerability scope, public-vs-private channels, disclosure timeline.
- **DISCLAIMER.md** — decision-support framing, parcel-level verification checklist, scope of "publicly accessible data".

### Security

- Anti-hallucination contract enforced as CI: forbidden-phrasings grep + Status footer stamp check on every PR.
- All workflows scoped via `permissions:` block to least-privilege (`contents: read`, `issues: write` only where needed).
- No secrets used in any workflow — all data sources are public.
