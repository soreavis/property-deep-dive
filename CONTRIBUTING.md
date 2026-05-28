# Contributing

Thanks for considering a contribution. The most valuable contributions are **factual corrections** and **new countries**, in roughly that order — getting one wrong tax rate fixed is worth more than a stylistic refactor.

## Quick map of where to contribute

All paths below are relative to the repo root. The skill payload lives under `skills/property-deep-dive/` so that plugin hosts (Claude Code, Claude Cowork) ship the entire skill from a single folder.

| What | Where |
|---|---|
| Add or update a country playbook | `skills/property-deep-dive/countries/<iso2>/playbook.md` |
| Log a new tax/regulatory reform | `skills/property-deep-dive/shared/regulatory-watch.md` |
| Update a visa / RBI / CBI / DNV / golden-visa programme status | `config/_visa-programs.json` (source of truth — change `status`), then run `python3 scripts/render-visa-programs.py` to refresh `shared/visa-programs.md` |
| Fix a broken URL | the relevant `skills/property-deep-dive/countries/<iso2>/playbook.md` or `skills/property-deep-dive/shared/<topic>.md` |
| Add a universal section flag | new file in `skills/property-deep-dive/shared/`, register in `skills/property-deep-dive/SKILL.md` argument-hint + Sections table |
| Add a tooling doc | `skills/property-deep-dive/shared/<tool-name>.md`, register in `skills/property-deep-dive/SKILL.md` |
| Fix anti-hallucination behaviour | `skills/property-deep-dive/shared/anti-hallucination.md` |

## Adding a new country

The bar is **FR/IT/CZ/SK density** (~400-500 lines, all 40 sections covered with primary government sources — note: --crime/amenities/climate/permits/agent/scams/sanctions/language/connectivity/home-tax/cross-border/remote/relocation/schools inherit from `shared/`, country playbook implements 7 core sections). See `skills/property-deep-dive/countries/fr/playbook.md` as the canonical example.

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

### Sub-sovereign jurisdictions (Crown Dependencies, overseas territories, autonomous regions)

Sub-sovereign jurisdictions with their own tax authority, land registry, and court system get **standalone playbooks** under their actual ISO 3166-1 alpha-2 code — not compound codes (`uk-je`) and not sub-region overlays in a parent playbook.

| Jurisdiction | ISO 3166-1 alpha-2 | Status |
|---|---|---|
| Jersey | `je` | Crown Dependency — standalone playbook (queued) |
| Guernsey | `gg` | Crown Dependency — standalone playbook (queued) |
| Isle of Man | `im` | Crown Dependency — standalone playbook (queued) |
| Gibraltar | `gi` | UK Overseas Territory — standalone playbook (queued) |
| Faroe Islands | `fo` | DK autonomous territory — standalone playbook (queued) |
| Greenland | `gl` | DK autonomous territory — standalone playbook (queued) |

**Rationale**: each has its own legal regime (Royal Court of Jersey vs HMCS England; JFSC vs FCA; Lands Tribunal Isle of Man vs HM Land Registry; etc.). A "UK playbook with Jersey overlay" would either bloat UK with carve-outs that apply to 1% of readers, or underserve Jersey readers who need the HVR / 2(1)(e) / SoCT regime in depth. Precedent: the project already treats `sm` (San Marino), `mc` (Monaco), `ad` (Andorra), `li` (Liechtenstein), `mt` (Malta) as standalone micro-state playbooks for the same reason.

Each playbook adds the ISO code to `config/_regions.json` + `config/_tiers.json` (Tier-C 365d default for low-volume jurisdictions) + relevant entries in `config/_visa-programs.json` (Jersey HQ-1(1)(k) / 2(1)(e); Guernsey Open Market / Inscribed; Isle of Man T1 Investor; Gibraltar Cat-2; etc.) in the SAME PR as the playbook itself — never decouple config from playbook content.

### Update 2026-05-27 — Batch C decision (FR DROM + NL Caribbean)

The deferred Batch C jurisdictions are unblocked under a mixed-schema decision driven by a clean rule:

**Decision rule**: a jurisdiction gets a standalone ISO-3166-1 alpha-2 playbook iff it has its own primary tax authority + its own land registry + its own court system that publish in their own name. Otherwise the jurisdiction is covered as a **DROM-style overlay** — deltas-only content in a shared file (`shared/<region>-overlay.md`) cross-linked from the parent playbook.

**Applied to Batch C**:

| Jurisdiction | ISO | Schema | Primary-source anchor |
|---|---|---|---|
| Aruba | `aw` | Standalone | DIMP tax authority (`gobierno.aw`), own kadaster, AWG currency, eigendom + erfpacht |
| Curaçao | `cw` | Standalone | Own Kadaster Curaçao, 4% transfer tax |
| Sint Maarten | `sx` | Standalone | `tax.sx` + `kadaster.sx`, no property tax + no CGT (foreign-buyer hook), own court system |
| Caribbean Netherlands (Bonaire + Saba + St Eustatius) | `bq` | Standalone | `belastingdienst-cn.nl`, USD currency, vastgoedbelasting 0.7% national + 30% Bonaire surcharge → 0.91% effective, 5% overdrachtsbelasting |
| Guadeloupe | `gp` | DROM overlay in `shared/fr-drom-overlay.md` | Same `impots.gouv.fr` + French cadastre + French courts as FR; DROM-specific BOFiP entries |
| Martinique | `mq` | DROM overlay | Same FR infrastructure |
| French Guiana | `gf` | DROM overlay | Same + Cerema cadastre-deficit caveat |
| Réunion | `re` | DROM overlay | Same FR infrastructure |
| Mayotte | `yt` | DROM overlay | Same + Cerema-acknowledged "very deficient cadastre, absence of property titling" caveat |

**Rationale**: FR DROM are constitutionally integral parts of France (Code civil applies, euro, EU territory) — they share `impots.gouv.fr`, the French cadastre, and French courts; a standalone playbook would duplicate ~80% of `countries/fr/playbook.md`. NL Caribbean (AW / CW / SX / BQ) each have their own primary tax authority + own land registry + own court system — they pass the standalone test exactly like the Crown Dependencies (Batch A).

**Decision-rule generalisation** — the rule extends cleanly to likely future cases without contradiction:

| Future case | Decision under this rule |
|---|---|
| Canary Islands (ES) | overlay (IGIC sub-regime but shares ES tax authority + ES cadastre) |
| Azores / Madeira (PT) | overlay (autonomous region within PT) |
| Ceuta / Melilla (ES) | overlay (no VAT but ES infrastructure) |
| Åland Islands (FI) | overlay (tax-sub-regime, EU-derogation, FI courts) |
| Svalbard (NO) | standalone (Svalbard Treaty 1920 creates distinct regime) |
| US territories (PR / USVI / Guam / AS) | standalone (own Hacienda + own courts) |
| UK overseas territories (BM / KY / TC / VG / AI / MS) | standalone (matches Batch A `gi` precedent) |

**Implementation phases**:

- **Phase A** (this PR) — schema decision committed (CONTRIBUTING.md + ROADMAP.md only)
- **Phase B** — 4 NL Caribbean standalone playbooks (research-wave matching the Batch A/B precedent)
- **Phase C** — 1 FR DROM shared overlay file (`shared/fr-drom-overlay.md`)

Full research memo with per-jurisdiction primary-source verifiability scores + Reddit demand signal + pros/cons matrix lives at `_local/batch-c-schema-recommendation.md` (gitignored).

### Update 2026-05-28 — Batch D decision (UK Overseas Territories + CBI Caribbean + medium-signal)

Batch D is schema-decided under the same rule (own tax/fiscal authority + own land registry + own court system → standalone; else overlay). Every jurisdiction below was verified against primary government sources by a research pass and re-checked by an independent fabrication-audit pass.

**UK Overseas Territories — all 4 STANDALONE** (confirms the generalisation-table prediction above):

| Jurisdiction | ISO | Tax/fiscal authority | Land registry | Court |
|---|---|---|---|---|
| Cayman Islands | `ky` | Lands & Survey Dept (stamp duty; no income/CGT/property tax) + Customs | Lands & Survey Dept / Land Registry (Registration (Land) Law, 1996 Revision) | Grand Court of the Cayman Islands (NOT ECSC; appeals → Cayman Court of Appeal → JCPC) |
| Bermuda | `bm` | Office of the Tax Commissioner | Land Title Registry Office (Land Title Registration Act 2011) | Supreme Court of Bermuda |
| Turks & Caicos | `tc` | Lands Division / Valuation | Land Registry (Registered Land Ordinance Ch. 9.01) | Supreme Court of the Turks and Caicos Islands |
| British Virgin Islands | `vg` | Inland Revenue Dept | Dept of Land Registry | High Court of Justice (Virgin Islands), a division of the ECSC |

**ECSC shared-court note**: VG (like the sovereign ECSC members LC/GD/AG/KN already treated standalone) sits under the Eastern Caribbean Supreme Court — a 9-member federated court (6 sovereign: AG/DM/GD/KN/LC/VC + 3 UK OTs: AI/VG/MS). A shared appellate layer does NOT break the "own court system" test: each member has its own resident High Court division. **VG's court must be named "High Court of Justice (Virgin Islands)" — never a fabricated "BVI Supreme Court".** KY/BM/TC are non-ECSC with fully self-standing courts.

**CBI Caribbean + medium-signal — all sovereign UN-member states → STANDALONE (no schema ambiguity)**: `kn` / `ag` / `lc` / `gd` (Citizenship-by-Investment); `na` / `bw` / `vu` / `tt` / `pk` (medium-signal).

**Region placement**: 4 UK OTs → new `caribbean_ot` region (mirrors the `nl_caribbean` precedent; accommodates BM's North-Atlantic location; may later generalise to `uk_ot`). 4 CBI + `tt` → extend existing `caribbean`. `na`/`bw` → `africa`; `vu` → `apac`; `pk` → `south_asia`. Region IDs finalised per-playbook in Phase B.

**Phase-B content flags (verified by audit — carry into the playbooks)**: TT's apex court is the UK Privy Council (JCPC) — T&T joined only the CCJ *Original* Jurisdiction, NOT Appellate (do NOT write "CCJ is T&T's final court"). PK land records are PROVINCIAL not federal — per-province caveat like AU (e.g. Punjab Land Records Authority, Act 2017). VU is leasehold-only (1980 Constitution abolished freehold). KY land statute is the "Registration (Land) Law (1996 Revision)" (substance = Torrens-style registered title).

**Implementation phases**:

- **Phase A** (this PR) — schema decision committed (CONTRIBUTING.md + ROADMAP.md only); country count unchanged at 113.
- **Phase B** — 8 strong-signal Caribbean standalone playbooks (`ky`/`bm`/`tc`/`vg` + `kn`/`ag`/`lc`/`gd`), 113 → 121.
- **Phase C** — 5 medium-signal (`na`/`bw`/`vu`/`tt`/`pk`), 121 → 126.

Each Phase B/C playbook adds its ISO code to `config/_regions.json` + `config/_tiers.json` (Tier-C 365d default; CBI states may warrant Tier-B) + relevant `config/_visa-programs.json` entries in the SAME PR. Full research + independent-audit memos at `_local/wip-batchd/` + `_local/wip-audit/audit-batchd.md` (gitignored).

## Logging a regulatory-watch entry

`skills/property-deep-dive/shared/regulatory-watch.md` is the single source of truth for "what changed when". Format:

```markdown
- `<effective_date> | <topic> | <one-line summary> | <source name> | <verified_date> | <revisit_by> | <tier> | <sections>`
```

- `<topic>` ∈ tax / rental / visa / finance / ownership / esg / cadastre / eurozone / other
- `<tier>` ∈ 1 (CRITICAL — reverses prior assertion) / 2 (MAJOR — material number change) / 3 (MEANINGFUL — threshold tweak) / 4 (INCREMENTAL — indexation)
- `<sections>` = the `--<flag>` sections this reform affects in country playbooks

ENDED-program registry entries (Tier 1, anti-hallucination critical) go in the ENDED Programs table in the same file.

If the reform changes a **visa / RBI / CBI / DNV / golden-visa** programme, also update its record in `config/_visa-programs.json` (set `status` to `ENDED` / `SUSPENDED` / `OPEN — RESTRICTED` / etc., update `min_threshold` and `caveats` as needed), then run `python3 scripts/render-visa-programs.py` so `shared/visa-programs.md` region tables stay in sync. The `visa-programs-audit.yml` workflow's `claim-audit` job will fail CI if any country playbook still mentions the programme without an acknowledgement marker (`ENDED` / `CLOSED` / `~~strikethrough~~` / "grandfathered" / "not enacted" / etc.).

## Anti-hallucination contract

This is non-negotiable. Every claim must be one of:

- **Sourced** to a primary government / regulated entity / cited secondary aggregator
- **Computed** transparently (inputs visible)
- **Estimated** with a `~` or `est.` prefix and a calibration sentence

Forbidden phrasings: "approximately X", "in the area of", "typical for the region", "as of recent data", "industry average", "experts say", "studies show", "should be around", "is likely connected to".

If a number can't be sourced, write `data not publicly available — verify at <authoritative source>` rather than guessing.

The eight mandatory pre-output checks are documented in `skills/property-deep-dive/shared/anti-hallucination.md`.

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
