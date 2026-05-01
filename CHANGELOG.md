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

### Removed / Deprecated — workflow audit (2026-05-01, 27 → 22)

Audit pruned 5 workflows + tightened 4 cron schedules. None of the removals were required-status checks per branch protection. Net effect: identical CI / security / anti-hallucination coverage with materially fewer GHA-minutes/year.

- **Deleted**: `welcome.yml` (cosmetic first-PR/issue greeter), `pr-size.yml` (cosmetic size-band labels nobody reads), `source-tier-audit.yml` (per-PR advisory comment — `source-tier-ratchet.yml` already gates regressions project-wide).
- **Folded into `pr-validate.yml`**: `matrix-consistency.yml` (`Country matrix ↔ countries/* audit` is now a job in pr-validate; standalone deleted).
- **Folded into `url-liveness.yml`**: `test-fixtures-check.yml` deleted — `url-liveness.yml` already greps `**/*.md` so test-fixtures listings get checked weekly Mon at the global 85% threshold; the dedicated 75% listings-only threshold + monthly cadence dropped (re-add as a focused step if listing-rot signal degrades).

### Changed — workflow cron tightening (2026-05-01)

- `feed-watcher.yml` — `0 */6 * * *` (every 6h, 1,460 runs/yr) → `0 9 * * *` (daily, 365 runs/yr). Regulatory feeds don't move fast enough for 4× daily polling.
- `transposition-alerts.yml` — `30 6 * * *` (daily) → `30 6 * * 1` (weekly Mon). T-90/30/14/0 threshold ladder doesn't need daily granularity; mid-week threshold crossings are caught by the next Monday.
- `stale.yml` — `0 3 * * *` (daily) → `0 3 * * 1` (weekly Mon). Issue/PR volume is low enough that daily was burning GHA-minutes on no-ops.
- `link-check.yml` — dropped per-PR + per-push triggers; weekly Friday cron + manual dispatch only. The per-push runs duplicated url-liveness coverage; weekly is sufficient for internal-link rot.
- chore(ci): workflow audit — 27 → 22 (delete cosmetic + fold redundant + tighten cron) ([#60](https://github.com/soreavis/property-deep-dive/pull/60)) — by @soreavis

### Added — 10 new country playbooks (Tier 1 expansion)

- **🇺🇸 US** — federal overview only (state/county tax + transfer/recording fees vary materially; verification path provided). Covers OBBBA (PL 119-21, 4 Jul 2025) reset of SALT/MID/§§ 25C-D + estate exemption, FIRPTA, NFIP Risk Rating 2.0, CFIUS Part 802 +59 sites Dec 2024, EPA LCRI, 36-state foreign-buyer laws, NAR settlement Aug 2024. ~666 lines, ~50 primary sources, HIGH confidence on federal constants. (`countries/us/playbook.md`)
- **🇹🇷 TR** — TKGM cadastre + Web Tapu + e-Devlet, TÜİK Konut Fiyat Endeksi (Q4 2025: İstanbul TRY 74,101/m² ≈ $1,755, +26% YoY), TCMB, AFAD seismic, sahibinden.com. CBI USD 400k (raised from $250k Jun 2022) + 3-yr non-resale lock; Law 7464 STR licensing eff 1 Jan 2024; Emlak Vergisi 0.1–0.6% (Büyükşehir 2×); Tapu Harcı 4%; DASK mandatory; TBDY 2018 building code watershed; post-Kahramanmaraş 2023 regulatory wave. ~574 lines, ~35 primary sources. (`countries/tr/playbook.md`)
- **🇦🇪 UAE** — foreign-buyer-restricted framing as LEAD section. Per-emirate cadastre (DLD/ADREC/SRERD/RAK/Ajman/Fujairah); designated freehold zones only for non-GCC; Sharjah 100-yr usufruct only; Golden Visa property route AED 2M (10-yr) / AED 750k (2-yr); Retirement Visa AED 1M property; NO income tax / NO annual property tax (DLD 4% transfer + 5% housing fee on rental); Federal Corporate Tax 9% from Jun 2023 on commercial entities; RERA Smart Rental Index brackets; Apr 2024 record floods → Tasreef stormwater plan to 2033; Dubai Law 2/2025 DIFC Wills direct enforcement. ~624 lines, 15+ primary sources. (`countries/ae/playbook.md`)
- **🇯🇵 JP** — foreigners may own freehold (no nationality restriction); 法務局 Hōmukyoku registry + 登記情報提供サービス, MLIT 不動産価格指数 + 公示地価 + 路線価, J-SHIS earthquake hazard, JMA. 固定資産税 1.4% + 都市計画税 0.3%; 不動産取得税 3%/4% (residential reduced to 2027-03-31); 39.63%/20.315% short/long capital gains; 相続税 progressive 10–55%; ~9M akiya (2023 housing survey); 民法改正 2024 mandatory inheritance reg within 3 yrs; 空家特措法 2023 改正 管理不全空家 designation can revoke 1/6 land tax exemption; BoJ rate normalization Mar 2024 NIRP exit → Jan 2025 0.5% → Dec 2025 ~0.75%; 民泊 Jun 2018 180-night cap; 重要土地等調査法 effective 2022-09-20. ~548 lines, ~35 primary sources. (`countries/jp/playbook.md`)
- **🇹🇭 TH** — foreign-buyer-restricted framing as LEAD section. Foreigners CANNOT own land freehold (Land Code §86); condo 49% foreign quota; 30-yr leasehold (renewals not enforceable); Thai company nominee enforced under §96bis; Chanote-only for foreigners; FX FET form mandatory. Land+Building Tax 0.01–0.7% (effective 2020); Hotel Act §4 STR <30 nights illegal without license; Thailand Privilege restructured 2023 (THB 900k–5M); LTR Visa 10-yr (4 categories); DTV Visa launched mid-2024 (5-yr multi-entry, THB 500k); proposed 99-yr lease + 75% condo quota under discussion 2024-25, NOT enacted. ~730 lines, 128 source URLs. (`countries/th/playbook.md`)
- **🇩🇴 DR** — foreigners freehold w/ same rights (Constitución art. 51, Ley 195-69); Tribunal Superior de Tierras + Jurisdicción Inmobiliaria (Ley 108-05); CONFOTUR (Ley 158-01 + 195-13) registered tourism projects: 100% IPI + transfer + ITBIS exempt ~15 yrs; IPI 1% above DOP 9.86M (2025); transfer 3%; investor residency USD 200k → 2-3-yr citizenship; AML Ley 155-17 + UAF beneficial-owner disclosure; pre-2007 title chain weakness → ALWAYS use lawyer (NOT just notario); USD parallel pricing in resort zones. ~533 lines, ~25 primary sources. (`countries/do/playbook.md`)
- **🇨🇴 CO** — foreigners freehold (Ley 9/1989); IGAC catastro multipropósito + ORIP + SNR; Migratorio M visa real-estate route ≥350× SMLMV (~USD 125k 2026), ≥650× → PR after 5 yrs; Predial Unificado per-municipio (Bogotá 5–15‰) on avalúo catastral; multipurpose cadastre rollout closing avalúo-vs-comercial gap; NSR-10 seismic code post-Quindío 1999 baseline; Bogotá Decreto 538/2024 10% STR lodging tax + RNT mandatory; Medellín El Poblado Acuerdo 056/2024 STR restrictions; Ley 2277/2022 reforma tributaria; estrato 1-6 system controls utility tariffs hugely. ~545 lines, ~50 primary sources. (`countries/co/playbook.md`)
- **🇺🇾 UY** — foreigners freehold w/ same rights; tax-residency 11-yr exemption on foreign interest+dividends (Ley 19.937 / 18.083) — wealthy-immigrant magnet from AR/BR; UYU + USD parallel pricing; ITP 4% transfer (2+2 customary); Contribución Inmobiliaria 0.25–1.4% per Intendencia; IRPF cat I 12% rental; Patrimonio above UYU exempt; condominio horizontal Ley 14.261; Ley 19.210 cash-payment caps 40,000 UI for property AML; Decreto 138/020 + 153/020 lowered RE investment threshold to UI 3.5M; Maldonado STR Receptive Operator. ~603 lines, ~30 primary sources. (`countries/uy/playbook.md`)
- **🇨🇱 CL** — foreigners freehold (DL 1939/1977 border-zone restriction for PE/BO/AR within 10km land border + 5km coast); Conservador de Bienes Raíces (territorial) + SII avalúo fiscal; UF (Unidad de Fomento) inflation-indexed daily by BCCh — most property priced in UF NOT CLP; Contribuciones de Bienes Raíces ~0.98% (above UF 11,000–32,000 exempt); semi-annual; sobretasa 0.275–0.425% above UF 670 (Ley 21.210 reform); NCh 433 building code post-1985 watershed + 2010 Maule revision DS 61/2011; SENAPRED + SHOA + SERNAGEOMIN hazard sources; mega-drought central+north + Código de Aguas reform 2022/2024; condominio Ley 21.442 (2023). ~559 lines, 42 primary sources. (`countries/cl/playbook.md`)
- **🇿🇦 ZA** — foreigners freehold (Expropriation Act 13/2024 assented Jan 2025 — Constitutional challenges pending); Deeds Registry (DALRRD) + Surveyor-General per-city; SARS Transfer Duty Schedule 8 (exempt below R1.1M, 13% above R12M); CGT 40% inclusion at marginal (max 18% effective); Section 35A withholding 7.5% on price >R2M for non-resident sellers; Estate Duty 20% above R3.5M; foreign mortgage typically 50% LTV cap; conveyancer mandatory; Sectional Titles Schemes Mgmt Act 8/2011 + Property Practitioners Act 22/2019; FICA AML; Beetle/Electrical/Plumbing/Gas CoCs at sale + Body Corporate Levy + Rates Clearance Cert; Tourism Amendment Bill (Aug 2024) regulating Airbnb pending; Eskom load-shedding declined 2024-25. ~531 lines, ~50 primary sources. (`countries/za/playbook.md`)

### Changed

- `_regions.json` — added 3 new region groupings (Türkiye & Middle East, Asia-Pacific, Africa); expanded Anglo non-EU (now 4) and Latin America (now 9). Total: 54 countries across 8 regions.
- `SKILL.md` — argument-hint description updated 44 → 54 countries; country matrix table extended with 10 new entries; file tree updated.
- `README.md` — auto-synced via `scripts/sync-docs.py`; 44 → 54 country count; country-gaps section refreshed (TR/JP/AE/US/CL/UY/CO/ZA/TH removed; SG/HK/KR/TW/IN/ID/MY/VN/PH/PE/EC/PY/MA/EG/TN/KE/NG/IL/SA/QA/GE/AM/AZ added).
- `shared/visa-programs.md` — added 3 new region tables (Türkiye & Middle East, Asia-Pacific, Africa) + extended Anglo non-EU (US: EB-5/E-2/E-1/EB-1A/E-3/H-1B/L-1) and Latin America (DO/CO/UY/CL); updated NEW/CHANGED registry (TR CBI threshold history, TH DTV/LTR launches, AE Golden Visa Cabinet Decision 65/2022, JP J-Find/J-Skip 2023, ZA Remote Work Visa 2024, US OBBBA Jul 2025); updated government portals row + Class A/B/C cross-cutting decision-helper.
- `shared/regulatory-watch.md` — added 10 new country sections (US/TR/AE/JP/TH/DO/CO/UY/CL/ZA) with date-stamped reform tracker entries spanning Tier 1–3 across `--tax`, `--visa`, `--rental`, `--risks`, `--mains`, `--finance` sections.
- chore(release): cut 2026.04.2 ([#45](https://github.com/soreavis/property-deep-dive/pull/45)) — by @soreavis
- chore(deps): Bump actions/github-script from d746ffe35508b1917358783b479e04febd2b8f71 to 3a2844b7e9c422d3c10d287c895573f7108da1b3 ([#48](https://github.com/soreavis/property-deep-dive/pull/48)) — by @dependabot[bot]
- chore(deps): Bump dependabot/fetch-metadata from 2.5.0 to 3.1.0 ([#50](https://github.com/soreavis/property-deep-dive/pull/50)) — by @dependabot[bot]
- chore(deps): Bump sigstore/cosign-installer from 3.9.1 to 4.1.1 ([#51](https://github.com/soreavis/property-deep-dive/pull/51)) — by @dependabot[bot]
- chore(deps): Bump github/codeql-action from 3.35.2 to 4.35.2 ([#52](https://github.com/soreavis/property-deep-dive/pull/52)) — by @dependabot[bot]
- feat: add 10 Tier-1 country playbooks (US/TR/AE/JP/TH/DO/CO/UY/CL/ZA) ([#57](https://github.com/soreavis/property-deep-dive/pull/57)) — by @soreavis
- chore(deps): Bump actions/labeler from 5.0.0 to 6.0.1 ([#49](https://github.com/soreavis/property-deep-dive/pull/49)) — by @dependabot[bot]

## [2026.04.2] - 2026-04-26

### Fixed — OpenSSF Scorecard Token-Permissions (2026-04-26)

- `changelog-on-merge.yml` — moved `contents: write` + `pull-requests: write` from top-level to the `append` job. Top-level write was the sole reason Scorecard's `Token-Permissions` check scored 0/10 (HIGH severity). Other workflows (`auto-tag`, `dependabot-auto-merge`, `release-notes`) already use this pattern. Expected score lift: 0 → 9.

### Changed — Cowork install accuracy (2026-04-26)

- README — separated the install flow into Claude Code (slash commands) vs Claude Cowork (in-app plugin browser, "upload your own plugin" path). Earlier copy claimed the slash-command path worked identically in both, which was overclaim — Cowork's user-facing install is GUI-driven per [Anthropic's launch post](https://claude.com/blog/cowork-plugins). Also flagged that Cowork plugin scope is per-user / local today (not workspace-wide), with org-wide sharing pending. Plugin format itself remains identical between products.
- docs(cowork): split install flow Claude Code vs Cowork; correct scope ([#41](https://github.com/soreavis/property-deep-dive/pull/41)) — by @soreavis
- fix(ci): scope changelog-on-merge write permissions to job level ([#43](https://github.com/soreavis/property-deep-dive/pull/43)) — by @soreavis

### Changed — plugin payload co-location (2026-04-26)

- **Plugin payload co-located** under `skills/property-deep-dive/`. Moved `shared/` (34 files) and `countries/<iso2>/playbook.md` (44 files) into the skill folder so plugin hosts (Claude Cowork, Claude Code) ship the entire payload from a single self-contained directory. Without this, post-PR-#33 plugin installs only received `SKILL.md` and every `shared/*` reference inside it resolved to nothing — Cowork agents fell back to live research without the anti-hallucination contract. Path references inside SKILL.md / shared/*.md / countries/*/playbook.md remain relative and resolve unchanged. Outside-the-skill references (13 workflows, `scripts/sync-docs.py`, labeler/labels/PR template, 3 issue templates, README/CONTRIBUTING/CLAUDE/DISCLAIMER/SECURITY, docs/) updated to the new path.
- `_regions.json` stays at repo root — it's a docs-build input for the README country matrix and is never read by the skill at runtime.
- `pr-validate.yml` — fixed `docs/` allowlist regex that only matched the `./docs/` form emitted by push-time `find`, missing the `docs/` form emitted by PR-time `git diff --name-only`. The forbidden-phrasings scanner now consistently exempts the docs folder (which quotes forbidden phrases by design).
- fix(plugin): co-locate shared/ + countries/ under skills/property-deep-dive/ ([#39](https://github.com/soreavis/property-deep-dive/pull/39)) — by @soreavis

### Added — doc-sync autogen (2026-04-26)

- `scripts/sync-docs.py` — autogen for community markdown drift. Computes counts from filesystem (countries / sections / shared / workflows / issue forms / total YAML configs / total markdown lines) and applies idempotent regex inline replacements + `<!-- AUTOGEN:country-matrix -->` block regeneration. Run as `--check` in CI, plain `python3 scripts/sync-docs.py` to write.
- `_regions.json` — single source of truth for country-region grouping (5 regions, 44 codes). Order determines render order in the README country matrix.
- `.github/workflows/doc-sync-check.yml` — PR-time gate plus Tuesday cron. Fails the PR if `--check` would write changes; opens an issue if scheduled drift is detected on `main`.
- README country matrix wrapped in AUTOGEN markers; previously-stale "25 YAML / JSON config files (17 workflows…)" tally now auto-derived from the filesystem.
- Robustness: `FLAG_OVERRIDES` map in `iso2_to_flag()` so the project-internal `uk` code renders as 🇬🇧 (Great Britain) rather than 🇺🇰 (the regional-indicator default for that pair, which is Ukraine's flag).

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

- `transposition-alerts.yml` — fixed shell redirect that overwrote the JSON payload with print output (`SyntaxError: Unexpected non-whitespace character` on every dispatch). Now relies on Python's `json.dump`.
- `.claude-plugin/plugin.json` — added `displayName: "Property Deep Dive (your property-buying co-pilot)"` (untested if the marketplace UI honours it — JSON parsers ignore unknown fields, so worst case is no-op). Expanded `keywords` from 10 → 19 with facet-specific terms (`property-tax`, `flood-risk`, `rental-yield`, `golden-visa`, `mortgage-calculator`, `crime-rate`, `retirement-property`, `foreign-buyer`, `cadastre`, etc.) for marketplace-search discoverability.
- `README.md` — added a "Try asking…" section right after Install with 5 concrete copy-paste invocations (visa+retirement, listing-URL integrity, country compare, heritage type, maintenance refresh). The community-plugin spec doesn't expose a manifest field for the styled "Try asking" cards Anthropic's curated plugins display, so README copy is the path.
- `docs/usage.md` + `docs/README.md` — fixed broken `../SKILL.md` links missed in the restructure PR (Lychee was red on main; advisory check didn't block auto-merge).
- `.claude-plugin/plugin.json` — removed bullet markers from the "Try asking" example list (was rendering as `• /property-deep-dive ...`; cleaner as plain lines per maintainer feedback once the marketplace card was visible). Bumped version `2026.04.1` → `2026.04.2` to push the change to existing installs.
- **Plugin restructure**: moved `SKILL.md` from repo root to `skills/property-deep-dive/SKILL.md` so the marketplace card renders the "Skills 1" section (matches the documented Claude plugin layout — auto-discovers from `skills/<name>/`). Plugin install path unchanged; manual-symlink path now needs `ln -s ~/code/property-deep-dive/skills/property-deep-dive ~/.claude/skills/property-deep-dive` instead of symlinking the whole repo. README updated.
- **Plugin description expanded** with embedded "Try asking" examples for marketplace card. Bumped `plugin.json` version `2026.04.0` → `2026.04.1` to push the update to existing installs.
- **CI path updates**: `pr-validate.yml`, `matrix-consistency.yml`, `doc-sync-check.yml`, `release-notes.yml`, `.github/labeler.yml`, and `scripts/sync-docs.py` updated to read `SKILL.md` from the new location.
- Marketplace-facing description rewrite — `.claude-plugin/plugin.json` `description` field, README intro paragraph, and GitHub repo description now share a plain-English headline ("Pre-purchase property due diligence across 44 countries — tax, risks, rental yield, visa, mortgage, and 17 other facets per address. Sourced from primary government data, every claim dated and confidence-labelled."). The previous copy leaned on internal jargon ("anti-hallucination contract", "date-stamped regulatory-watch governance") which doesn't land for marketplace browsers.
- `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` — Claude Code / Claude Cowork plugin manifest. Repo is now self-installable via `/plugin marketplace add github:soreavis/property-deep-dive` then `/plugin install property-deep-dive@property-deep-dive`. Version pinned to `2026.04.0`; manual bump per release per `CONTRIBUTING.md` § Release process. README install section restructured to lead with plugin install (works in both Code and Cowork) and keep the manual symlink path for skill development.
- `auto-merge-docs.yml` — same PAT swap as `changelog-on-merge.yml`. The `enablePullRequestAutoMerge` GraphQL mutation rejects `GITHUB_TOKEN` with "Resource not accessible by integration", so auto-merge enrolment was silently failing on every bot PR. With `PR_BOT_TOKEN`, auto-merge fires immediately and the PR squash-merges as soon as required checks pass. Also surface the real gh CLI error in logs (was swallowed by `if/else`).
- `changelog-on-merge.yml` — swap default `GITHUB_TOKEN` for fine-grained PAT (`PR_BOT_TOKEN`, `Contents:RW` + `Pull-requests:RW` on this repo only). Reason: GitHub's safety rule says PRs created via `GITHUB_TOKEN` do not trigger downstream workflows. The bot's PRs were sitting with 0 CI checks and never auto-merging. With the PAT, the bot's PR triggers `auto-merge-docs.yml` + `pr-validate.yml` immediately.
- `changelog-on-merge.yml` — sanitize source PR title before writing it into CHANGELOG.md. Defangs `[link](url)` and `![img](tracker)` injection plus raw `<script>` tags. Backslash escape first; truncation at 200 chars; newlines collapsed.
- `codeql.yml` — added `python` language to the matrix now that `scripts/sync-docs.py` is committed (was deferred during initial setup). CodeQL will SAST-scan all .py files for code-injection / unsafe-path-traversal patterns each Wed + on every PR.
- `year-roll-reminder.yml` — fixed broken flag rendering in the auto-generated issue (was hardcoded `🇨{iso2}` — single regional indicator + literal letters → `🇨AL` instead of `🇦🇱 AL`). Now uses the same `iso2_to_flag` + `FLAG_OVERRIDES` pattern as `scripts/sync-docs.py`.
- `year-roll-reminder.yml` — broadened regex from strict `(YYYY data...)` to any `(YYYY)` / `(YYYY context)` parenthetical with a `[\s,)]` terminator. Catches the 96 year stamps actually in use today (mostly `(2025)` and `(2025 reform)` forms) without false-positives on `(€2,025)`, `(1 Aug 2025)`, etc.
- `source-tier-ratchet.yml` — guarded `GITHUB_BASE_REF` against the empty-string case that occurs on `workflow_dispatch` (was failing with `git rev-parse origin/`).
- All Node-20 GitHub Actions bumped to Node-24-compatible versions (deprecation warning emitted by GitHub on April 26, 2026): `actions/checkout` v4 → v6.0.2, `actions/setup-python` v5 → v6.2.0, `actions/cache` v4 → v5.0.5, `actions/github-script` v9 → v9.0.0 (fresh SHA), `actions/upload-artifact` v7 → v7.0.1 (comment refresh).
- `sign-release.yml` — added `workflow_dispatch` with required `tag` input so `auto-tag.yml` can chain into it.
- `changelog-enforcer.yml` — dropped `expectedLatestVersion: Unreleased` config. The action's logic treats `versions[1]` as the "latest" once a real release exists, so the setting only works on pre-1.0 repos.
- README architecture diagram updated to reflect the 16-workflow set + `scripts/` folder
- feat(ci): tier-1+2 follow-up workflows · SLSA L3 · Node 24 bump ([#7](https://github.com/soreavis/property-deep-dive/pull/7)) — by @soreavis
- feat(ci): doc-sync autogen for community markdown drift ([#9](https://github.com/soreavis/property-deep-dive/pull/9)) — by @soreavis
- fix(ci): changelog-on-merge — use PR_BOT_TOKEN instead of GITHUB_TOKEN ([#23](https://github.com/soreavis/property-deep-dive/pull/23)) — by @soreavis
- fix(ci): auto-merge-docs — use PR_BOT_TOKEN (GITHUB_TOKEN can't auto-merge) ([#25](https://github.com/soreavis/property-deep-dive/pull/25)) — by @soreavis
- feat(plugin): Claude plugin manifest — installable in Claude Code + Cowork ([#27](https://github.com/soreavis/property-deep-dive/pull/27)) — by @soreavis
- docs(plugin): rewrite the marketplace description in plain English ([#29](https://github.com/soreavis/property-deep-dive/pull/29)) — by @soreavis
- docs(plugin): displayName + keyword expansion + README "Try asking…" ([#31](https://github.com/soreavis/property-deep-dive/pull/31)) — by @soreavis
- feat(plugin): restructure to skills/\<name>/ + longer description with examples ([#33](https://github.com/soreavis/property-deep-dive/pull/33)) — by @soreavis
- fix(docs): update SKILL.md links after move ([#35](https://github.com/soreavis/property-deep-dive/pull/35)) — by @soreavis
- docs(plugin): drop bullets from "Try asking" — bump 2026.04.1 → 2026.04.2 ([#37](https://github.com/soreavis/property-deep-dive/pull/37)) — by @soreavis

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
