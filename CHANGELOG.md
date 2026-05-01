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

### Fixed
- **20 dead URLs replaced + 7 false-positive template URLs filtered.** The 2026-04-27 url-liveness scan flagged 27 DEAD URLs. Of these, ~7 were false positives — the URL extractor truncated template patterns like `https://example.gov/path/<INSEE>` into a stub `https://example.gov/path/` that 404'd. Switched URL extraction in `url-liveness.yml` from grep to Python with template-aware skipping (`<` or `{` after URL = template), plus a per-file exclusion list (`test-fixtures.md`). The remaining 20 genuinely-dead URLs were researched and replaced with verified canonical successors on the same source authority (BE Statbel theme rename, Sreality price-map flatten, NL stat.ee taxonomy refresh, EE Maa-amet → Maaruum domain migration, NZ NZTA / Waka Kotahi reorg, ECJ jcms→JSF portal, etc.). Country playbooks affected: BE, BR, CZ, DE, ES, FI, LT, MX, NZ. Shared docs affected: `crime-sources.md`, `comparable-transactions.md`, `listing-aggregators.md`, `price-index-feeds.md`, `regulatory-watch.md`. All replacement URLs verified 200 (or browser-OK behind known WAF challenges).

### Removed
- **`auto-pr-redirects.yml` and `scripts/find_redirects.py` deleted entirely.** The original implementation (PR #85) re-scanned all 3,228 country-playbook URLs from scratch every Tuesday with no throttling, risking IP-banning the GitHub Actions egress range from primary government sources. The cron was disabled in PR #88. After deciding the value-vs-complexity tradeoff didn't justify a refactor, the workflow + script were removed. URL maintenance stays manual via `url-liveness.yml`'s weekly Monday scan + human-driven URL refresh during `--update` runs.

### Added
- **Maintenance automation Tier-1 batch** — two improvements that turn detection-only workflows into proactive ones:
  - **Regulatory-watch auto-promotion** — `tier-a-refresh.yml` now parses `regulatory-watch.md` for Tier-1/2 entries enacted in the last 90 days and surfaces affected countries as 🆕 promotions in the Tier-A tracking issue. Closes the loop on the documented `_tiers.json § promotion_rules` design. Logic in `scripts/regwatch_promotions.py`.
  - **Stamp-drift early warning** — `health-report.yml` adds an "Early warning" section listing countries within 30 days of crossing a decay threshold (HIGH→MEDIUM at 180d, MEDIUM→LOW at 360d, LOW→STALE at 540d) OR within 30 days of cadence-tier off-cadence. Issue summary line gains `⏱️N 🟡N` counters.
- **`ROADMAP.md`** — country-addition backlog at repo root. 8 Tier-1 candidates (mu/kz/cv/sc/cn/jm/bs/sm), 8 Tier-2 (bb/bz/lk/kh/mv/gh/rw/uz), Crown Dependencies as a deferred schema-design item, and skip-list with reasoning. No commitment to schedule.
- **Tiered refresh cadence** — `_tiers.json` defines A/B/C tiers (15/30/42 countries) at 90/180/365 day cadences, replacing the flat "annually" cadence. New `--tier=<A|B|C>` flag plus `--include`/`--exclude` overrides for ad-hoc inclusion. Tier-A is high-velocity foreign-buyer markets (fr/it/es/de/uk/us/pt/ie/nl/at/gr/tr/ae/au/ch); Tier-B is stable mid-volume (30 countries); Tier-C is microstates + frontier (42 countries).
- **3 cron workflows** for tier reminders — `tier-a-refresh.yml` (quarterly), `tier-b-refresh.yml` (semi-annual), `tier-c-refresh.yml` (annual). Each opens a tracking issue listing countries due for refresh. Cron jobs do NOT modify playbooks — humans run `--update --tier=X` to execute.
- **Health-report cadence column** — `health-report.yml` decay matrix now shows cadence tier (A/B/C) and an off-cadence flag when a country exceeds its tier window. Issue summary line now reports off-cadence A/B/C counts alongside HIGH/MEDIUM/LOW/STALE.
- `shared/updater.md` § Refresh tiers replaces old § Frequency recommendations with new cadence-by-country breakdown plus auto-promotion + manual-override semantics.
- `SKILL.md` argument-hint extended with `--tier=<A|B|C>` `--include=<iso2>` `--exclude=<iso2>`; cadence table now references tier counts.
- Stamp-grep robustness: `health-report.yml` and tier-refresh workflows now extract `**Last verified**: YYYY-MM-DD` in addition to `as of YYYY-MM-DD` — the new playbook format wasn't being detected by the existing grep.

### Changed

- chore(docs): refresh stale 62-countries refs → 87 + cut \[2026.05.1\] CHANGELOG entry ([#76](https://github.com/soreavis/property-deep-dive/pull/76)) — by @soreavis
- feat(updater): tiered refresh cadence (A/B/C — 15/30/42 countries) ([#78](https://github.com/soreavis/property-deep-dive/pull/78)) — by @soreavis
- docs: add ROADMAP.md country backlog ([#83](https://github.com/soreavis/property-deep-dive/pull/83)) — by @soreavis
- feat(maintenance): Tier-1 automation batch — regwatch promotion + drift warning + auto-PR redirects ([#85](https://github.com/soreavis/property-deep-dive/pull/85)) — by @soreavis
- fix(workflow): disable auto-pr-redirects cron until refactor lands ([#88](https://github.com/soreavis/property-deep-dive/pull/88)) — by @soreavis
- chore: remove auto-pr-redirects workflow + script entirely ([#91](https://github.com/soreavis/property-deep-dive/pull/91)) — by @soreavis

## [2026.05.1] - 2026-05-01

Mid-month sprint adding **25 new country playbooks** in three tiers (62 → 87 countries) plus matching cross-cutting `shared/` table backfill. Same parallel-subagent research methodology as Tier-1/Tier-2; every playbook ends with a `## Status` footer (Confidence: HIGH, bare-date `**Last verified**: 2026-05-01`) and is fully sourced to primary government / regulated entity URLs.

**Headline**:
- 🌍 **25 new country playbooks** across 3 tiers (PR #69 Tier-3 EASY, PR #70 Tier-4 MEDIUM, PR #74 Tier-5 HARD — original Tier-5 PR #71 was retargeted)
- 🧱 **13 cross-cutting `shared/` tables backfilled** for the 25 new countries (~+1,909 lines net)
- 📍 **3 region buckets added / extended**: APAC (6 → 12), MENA (3 → 10), Africa (3 → 6); Caucasus renamed to "Caucasus & Eastern non-EU" (1 → 4); NEW "European Microstates" region (LI/AD/MC); Latin America (9 → 12)
- 📈 **+22,690 country-playbook lines** + 1,909 shared/ lines = **+24,599 net skill content**

### Added — Tier-3 (🟢 EASY, 9 countries — PR [#69](https://github.com/soreavis/property-deep-dive/pull/69))

Open or near-open foreign-buyer regimes; mostly East Asia + European microstates + Moldova.

- **🇸🇬 SG — Singapore** (632L) — ABSD 60% foreigner / 65% entity (eff. 27 Apr 2023), HDB closed to foreigners, RPA condo + Sentosa LDAU only, GIP S$10M/S$25M, STR <90d BANNED, SORA-only since 1 Jan 2025
- **🇭🇰 HK — Hong Kong** (1,022L) — ALL cooling measures abolished 28 Feb 2024, 2047 Crown-lease question, rates 5% + Govt Rent 3%, CIES reactivated Mar 2024, STR <28d illegal
- **🇰🇷 KR — South Korea** (640L) — Foreign Land Acquisition notification (reciprocity-based), RTMS real-price 실거래가 since 2006, jeonse fraud crisis 2022-24 + HUG insurance reform, F-2 Investor ₩600M 5yr, KRW free-float
- **🇹🇼 TW — Taiwan** (652L) — 房屋稅 2.0 multi-home reform 1 Jul 2024, 房地合一稅 2.0 (foreigners flat 35-45%), Cross-Strait Act §69 PRC restrictions, NO golden-visa via RE, 2024 Hualien M7.4
- **🇱🇮 LI — Liechtenstein** (510L) — GVG LR 214.11 effectively BANS non-residents, quota-based residency Auslosung lottery (NO investment-track), CHF currency union with CH since 1923, Sollertrag property-tax formula
- **🇲🇴 MO — Macao SAR** (947L) — Land Law 10/2013 ALL state-leasehold, Stamp Duty stack ~12-15% non-resident all-in, Investment Residence SUSPENDED since 2007, Talent Programme 2024 NOT property-linked
- **🇦🇩 AD — Andorra** (805L) — Llei 36/2024 òmnibus ~10% non-resident RE surcharge, parish-level cadastre (NO national), IRPF 0/5/10% (lowest WE), naturalization 20yr (NOT investment-pegged)
- **🇲🇨 MC — Monaco** (450L) — OPEN to all nationalities, Loi n° 1.560 (Dec 2024) closed SCI 7.5% loophole — uniform 4.5%, NO annual property tax / NO CGT / NO PIT (UNIQUE — French nationals carved out via 1963 Convention)
- **🇲🇩 MD — Moldova** (989L) — agri/forest BANNED to foreigners, MDL volatility 2022-24, Investor Residency Law 200/2010 €250k 5yr, CBI ENDED Law 100/2020, EU candidate Jun 2022, **Transnistria OUT OF SCOPE**

Plus shared/ backfill for 9 Tier-3 countries: finance.md +25 · currency.md +25 · notary-process.md +9 · insurance.md +9 · retirement.md +117 · digital-nomad.md +32 · compare.md +133 · exit.md +94 · macro.md +67 · demographics.md +33 · esg.md +52 · crime-sources.md +67 · price-index-feeds.md +16 ≈ **+679 lines**.

### Added — Tier-4 (🟡 MEDIUM, 8 countries — PR [#70](https://github.com/soreavis/property-deep-dive/pull/70))

Mix of regulated GCC + Andean LATAM + Caucasus + North Africa.

- **🇶🇦 QA — Qatar** (631L) — Law 16/2018: 9 freehold zones + 16 leasehold-99yr zones; QAR pegged USD 3.64 since 2001; NO recurring property tax / NO PIT / NO VAT yet (UNIQUE); PR Law 10/2018 ≥QAR 1M (capped ~100/yr); Investor Residency Law 21/2018 ≥QAR 730k; FIFA 2022 legacy + Lusail metro; NO citizenship-by-investment
- **🇸🇦 SA — Saudi Arabia** (1,199L) — NEW Foreign Real Estate Ownership Law 7 Jan 2025 (eff. Jan 2026); Mecca/Medina BANNED non-Muslim (constitutional/religious — UNIQUE); NO recurring property tax (UNIQUE) BUT White Land Tax 2.5% idle urban; RETT 5%; VAT 15%; Premium Residency Vision 2030
- **🇵🇪 PE — Peru** (1,164L) — Border Zone 50km BANNED non-citizens (Const. Art. 71); IGV 18% effective ~9% (50/50 terreno-construcción split); Pacific Ring of Fire HIGH seismic + tsunami + 2017/2023 El Niño catastrophic floods; USD ~30% Lima/coast pricing
- **🇪🇨 EC — Ecuador** (848L) — CGT 0% if held >5 yrs (UNIQUE); USD officially adopted Sep 2000 (NO FX risk); IVA raised 12→13% from 1 Apr 2024 (security funding under Decreto Ejecutivo 110); 2024 Internal Armed Conflict Declaration; Censo 2022 final 16.9M
- **🇵🇾 PY — Paraguay** (1,209L) — Border Zone Ley 2.532/2005 RURAL only (urban CDE/Encarnación OK); CGT effective ~2.4% (Ley 6.380/2019 30% taxable design — among LOWEST in S.America); territorial-source PIT; 2023 RBI tightening (Resolución SET 1186); Itaipú/Yacyretá #2 net electricity exporter
- **🇦🇲 AM — Armenia** (1,075L) — HO-185-N Real Estate Tax phased reform 2021-2026 (2026 first FULL effect); HO-105-N IT 1% turnover regime extended to 31 Dec 2031 (UNIQUE); 1988 Spitak M6.8 baseline; Russian-relocant wave 2022-24; Karabakh out of cadastral scope post-2023
- **🇦🇿 AZ — Azerbaijan** (1,087L) — Property tax m²-BASED not %-based (Tax Code Art. 198); AZN de-facto pegged USD 1.70 since 2017 (NOT formal currency-board, breached 2015 twice); 2020+2023 Karabakh + East Zangezur reintegration **out-of-scope for ordinary foreign-buyer DD**; SOFAZ FX-buffer ~US$60bn
- **🇹🇳 TN — Tunisia** (757L) — GOVERNOR'S AUTHORIZATION required (6-12mo, no statutory appeal — Code des Droits Réels 1957) UNLESS in ONTT-designated Zone Touristique; BCT/Office des Changes FX gateway mandatory; titré-only safe; IMF EFF SUSPENDED Mar 2024

Plus shared/ backfill for 8 Tier-4 countries: finance.md +8 · currency.md +8 · notary-process.md +8 · insurance.md +8 · retirement.md +99 · digital-nomad.md +28 · compare.md +131 · exit.md +80 · macro.md +70 · demographics.md +44 · esg.md +52 · crime-sources.md +65 · price-index-feeds.md +14 ≈ **+619 lines**.

### Added — Tier-5 (🟠 HARD, 8 countries — PR [#74](https://github.com/soreavis/property-deep-dive/pull/74))

Mix of populous emerging market (IN), highest-friction Africa (NG, KE), full GCC remainder (OM, BH, KW + JO Levant), and unique crisis context (LB).

- **🇮🇳 IN — India** (1,421L) — DECENTRALIZED state cadastres (28 states + 8 UTs); NRI/OCI freely buy NOT agri/plantation/farmhouse; Foreign Nationals BANNED except inheritance + RBI permission; PK/BD/SL/AF/CN/IR/NP/BT need RBI approval EVEN for inheritance; **Finance Act 2024 LTCG 12.5% flat WITHOUT INDEXATION** (down from 20% with indexation — major structural reform); RERA 2016 mandatory; NO golden-visa via RE (UNIQUE)
- **🇳🇬 NG — Nigeria** (1,066L) — Land Use Act 1978 abolished freehold (only 99yr leasehold via C of O); State Consent Fee 8-15% Lagos = transaction cost gateway; Naira float Jun 2023 + USD informal pricing; security risk Boko Haram+ISWAP+IPOB+banditry; energy autonomy mandatory (generators ubiquitous)
- **🇰🇪 KE — Kenya** (1,201L) — 2010 Constitution Art. 65 non-citizens ONLY 99yr leasehold (auto-converted from freehold 27 Aug 2010); title fraud MAJOR risk; dual legacy cadastre RTA/RLA/GLA/LTA being unified via LIMS 2019-26; AHL 1.5% gross under judicial review; NO golden-visa via RE
- **🇯🇴 JO — Jordan** (708L) — RECIPROCITY-based foreign-buyer; Property Sales Tax 9% (unified 2019) ~10-12% all-in HIGHEST MENA; **CGT 0% individuals on RE (UNIQUE)**; JOD pegged USD 0.7080 since 1995; **CBI Jordan since 2018** (JOD 750k bond — passport WEAK ~50 visa-free)
- **🇴🇲 OM — Oman** (1,140L) — Royal Decree 12/2006 ITC-only freehold (Al Mouj/Muscat Hills/Hawana Salalah/Jebel Sifah/Saraya Bandar Jissah/The Wave + 2023-24 expansions); **Investor Residency Royal Decree 89/2021** OMR 250k 5yr / OMR 500k 10yr; Cyclone Gonu 2007+Mekunu 2018+Shaheen 2021 catastrophic
- **🇧🇭 BH — Bahrain** (656L) — MOST OPEN GCC (Law 27/2017 extensive designated areas); VAT 10% (raised 2022); **0% PIT/CGT/CT (UNIQUE GCC even vs UAE 9% CT)**; BHD pegged USD 0.376 since 2001 (highest face-value globally); Bahrain Property Visa Decree 6/2017 BHD 200k 10yr + Golden Residency Decree 16/2022
- **🇰🇼 KW — Kuwait** (1,154L) — MOST RESTRICTIVE GCC (Decree-Law 74/1979 non-GCC effectively BANNED); GCC reciprocity only; NO VAT yet (with Qatar last GCC holdouts); KWD basket-managed since 2007 (highest face-value globally ~USD 3.25); NO golden-visa via RE (UNIQUE GCC absence)
- **🇱🇧 LB — Lebanon** (727L) — Decree-Law 11614/1969 + Law 296/2001 LAYERED CAPS (3,000 m² national + 3% territory cumulative + 3% per-district + 5yr build-or-forfeit); **POST-2019 BANKING CRISIS** (Lollar vs fresh USD); 2024 Israel-Hezbollah war Sep-Nov 2024; de-facto USD-dollarization 80%+ prime; Beirut Central District (Solidere) separate permissive regime

Plus shared/ backfill for 8 Tier-5 countries: finance.md +25 · currency.md +24 · notary-process.md +16 · insurance.md +11 · retirement.md +98 · digital-nomad.md +35 · compare.md +101 · exit.md +82 · macro.md +70 · demographics.md +41 · esg.md +48 · crime-sources.md +72 · price-index-feeds.md +11 ≈ **+611 lines**.

### Changed

- `_regions.json` — APAC 6 → 12 (added SG/HK/KR/TW/MO + IN); MENA 3 → 10 (added QA/SA/JO/OM/BH/KW/LB); Africa 3 → 6 (added TN/NG/KE); Latin America 9 → 12 (added PE/EC/PY); Caucasus renamed to "Caucasus & Eastern non-EU" 1 → 4 (added MD/AM/AZ); NEW "European Microstates" region (LI/AD/MC). Total: 87 countries across 10 regions.
- `skills/property-deep-dive/SKILL.md` — country count 62 → 87, country matrix table extended with 25 rows, file map updated, country-name list in description extended.
- `README.md` — auto-synced via `scripts/sync-docs.py`: country count 62 → 87, AUTOGEN country-matrix block re-rendered, skill-content / repo-total counts refreshed.
- `.claude-plugin/plugin.json` — marketplace-facing description "62 countries" → "87 countries".
- `CLAUDE.md` — example "fill in tax rates for all 62 countries" updated to 87.
- `.github/ISSUE_TEMPLATE/new-country.yml` — pre-flight checkbox label "(62 countries currently)" → "(87 countries currently)".
- `shared/regulatory-watch.md` — header "62 countries × 22 sections" → "87 countries × 22 sections"; last-audit footer updated to reflect Tier-3/4/5 additions.
- `shared/auto-validate.md` — sample report "62 countries validated" → "87 countries validated".

### Fixed

- Anti-hallucination NEAR_NUMBER trigger in `mo/playbook.md` — `circa 2001` → `c.2001` (CI guard rejects `circa +[0-9]`).
- Markdown lint — MD058 in `mc/playbook.md` (blank line before quartier table); MD007 in `ke/playbook.md` (nested list 2sp → 4sp indent).

## [2026.05.0] - 2026-05-01

Major monthly cycle release. Country count **44 → 62** (+18 across two batches), 13 cross-cutting `shared/` tables backfilled to HIGH confidence for the new countries, workflow audit (27 → 22 workflows), `health-report.yml` decay-matrix bug fix, and accumulated Dependabot bumps.

**Highlights**:
- 🌍 **18 new country playbooks**: Tier-1 (US/TR/AE/JP/TH/DO/CO/UY/CL/ZA, PR #57) + Tier-2 (GE/ID/MY/VN/PH/IL/MA/EG, PR #62)
- 🧱 **13 cross-cutting `shared/` tables backfilled** to cover the 18 new countries on universal flags (`--finance` `--currency` `--insurance` `--macro` `--demographics` `--esg` `--exit` `--retirement` `--digital-nomad` `--compare` `--notary` `--crime` `--price-index-feeds`) — PR #65
- 🔧 **Workflow audit** (27 → 22): deleted cosmetic workflows, folded matrix-consistency + test-fixtures-check into pr-validate / url-liveness, tightened 4 cron schedules — PR #60
- 🛡️ **`health-report.yml` decay-matrix fix**: `set -euo pipefail` + grep-empty-match was aborting the scheduled job; defensive `|| true` + bare-date stamp normalization on CO/TR/EG — PR #62
- 📍 **9 regions** (was 5 pre-Apr): added `mena`, `apac`, `africa`, `caucasus` — `_regions.json` extended

### Changed — cross-cutting `shared/` tables backfill for Tier-1 + Tier-2 (2026-05-01)

Universal-section `shared/` files extended to cover the **18 new countries** added in PR #57 (Tier-1: US/TR/AE/JP/TH/DO/CO/UY/CL/ZA) + PR #62 (Tier-2: GE/ID/MY/VN/PH/IL/MA/EG). Before this change, the 18 new countries inherited MEDIUM confidence on universal flags (`--finance` `--currency` `--insurance` etc.) because the per-country tables in `shared/` ended at the original 44. Now they're explicit. **+1,427 lines net across 13 files**, all primary-source URLs + date-stamped, zero forbidden phrasings.

- `shared/finance.md` (+83) — foreign-buyer mortgage availability, LTV cap (non-resident), 10-yr fixed rate, FX-loan rules, banks with NR desks per country. Surfaced **CL/UY/CO CPI-indexed mortgage trap** (UF/UI/UVR — modeling as nominal fixed understates payments by full inflation rate); **AE LTV step at AED 5M** (75%/65% NR 1st prop — buying at AED 4.95M vs 5.05M shifts deposit by ~AED 500k); **EG Form 4 + MA Office des Changes** as dominant exit-liquidity risks (must be filed at purchase, not later).
- `shared/notary-process.md` (+61) — civil-law notary vs common-law solicitor, mandatory professional, days offer→deed, closing-cost %. Highlights: **GE 1-hour express transfer at PSDA** (~0.1-0.5% all-in, lowest tracked); **TR Tapu same-day** (registration is constitutive, no separate notarial deed); **IL dual title system** (Tabu + RMI — verifying both registries mandatory because parcel can be missing from one).
- `shared/currency.md` (+67) — currency code, peg/float regime, FX volatility band, capital controls, hedging market depth. Cross-cutting risk #5 added: **mandatory FX-form regimes are the binding constraint, not capital controls per se** — EG Form 4, MA Office des Changes, TH FET (Tor Tor 3), TR MASAK dekont, VN SBV documentation must be obtained at purchase or repatriation is permanently blocked. Risk #6 added: **dual-unit pricing** (CL UF, UY USD billete + UI for mortgages, DO USD-parallel) — confirm denomination in writing before signing.
- `shared/crime-sources.md` (+138) — per-country primary police/justice ministry stats URL + granularity + cadence + methodology caveats. **AE / VN / EG / TH-tourist-zones** flagged with explicit "data not publicly available at parcel level — verify with local police district" framing (transparency-poor regimes routed through Tourist Police channels create blind spots). **South Africa SAPS** uniquely granular (~1,150 station-level quarterly) but precinct boundaries don't match suburb boundaries (Sandton vs Alexandra — needs precinct-suburb caveat). Series-break flags embedded for US (NIBRS 2021+), CL (Tren de Aragua 2022-2024), MY (Crime Index methodology change 2014/2020), IL (2023+ security reclass), PH (2016-2022 drug-war period).
- `shared/insurance.md` (+41) — national catastrophic-risk reinsurance scheme, flood/EQ/wildfire policy availability, mortgage-mandatory rules. **IL Property Tax & Compensation Fund (1961 statute)** uniquely funds **war-damage** (missile/rocket/drone) compensation as primary cover — currently absorbing ₪10bn+ in Hamas/Hezbollah-era claims; private market excluding war risk on top. **MA Loi 110-14 (Jan 2020)** one of few low/middle-income mandatory-bundled cat-cover regimes globally — **Al Haouz EQ Sep 2023** was first major real-world test. **TR DASK** paid ~₺27bn against ~₺1+ trillion Kahramanmaraş losses — buyers should not treat DASK as adequate stand-alone (₺1.36m cap structurally insufficient).
- `shared/macro.md` (+143) — CPI YoY, GDP growth, central-bank policy rate, 10-yr sovereign yield (USD eurobond ref for EM markets). New cyclical bucket: **JP "Normalization"** — BoJ moved from NIRP (2016-2024) to active hiking 0.50% Jan 2025 → 0.75% Dec 2025 (first sustained tightening since 2007). New rule: EM countries (TR, EG) cite **USD eurobond as foreign-buyer reference yield** (TRY/EGP local-currency yields are FX/inflation premiums, not investment yields).
- `shared/demographics.md` (+79) — population, median age, TFR, net migration, PISA tier, family-friendliness composite. Highlights: **JP and IE tied at 516 PISA reading** (top tier despite oldest median age 49.4 — top schools + collapsing demographics is a stark combo); **IL TFR 2.89 = highest in OECD** but masks ultra-Orthodox/Haredi ~6.5 vs secular ~2.0 (composition-driven); **AE population ~88% expat** (citizen TFR ~3 vs aggregate 1.4 diverge so sharply that any single-number TFR claim is misleading).
- `shared/esg.md` (+119) — non-EU energy-rating regimes (HERS/BELS/Pearl/Estidama/SANS/GREENSHIP — explicitly NOT comparable to EU A-G axis), climate-exposure tiers, carbon-tax/energy-levy rows, grid-mix renewable share. Highlights: **UY carbon tax on petroleum (~USD 137/tonne)** highest in Latin America, exceeds EU averages; **US IRA §25C/§25D residential credits TERMINATED 31 Dec 2025 per OBBBA Jul 2025** (many summaries still treat them as active); **JP Tax for Climate Change Mitigation JPY 289/tonne (~USD 2)** — among lowest carbon prices in OECD despite emissions profile (GX-ETS phasing in from 2026 will change this).
- `shared/exit.md` (+195) — DOM by city, agent commissions, sell-side closing costs, foreign-seller withholding, foreign-buyer-pool depth. New cross-country pattern: **GROSS-revenue CGT regimes** (EG 2.5%, PH 6%, ID 2.5%, VN 2%, TH 3.3% if <5yr) are an underappreciated exit trap — they tax sale price not gain, so loss-making sales still owe tax. **MY RPGT 10% PERMANENT for foreigners** vs 0% for citizens after 5 yrs is the most asymmetric foreign-seller drag in the dataset.
- `shared/retirement.md` (+227) — pension taxation, healthcare access, climate suitability, expat density, special programs (LTR, MM2H, SRRV, etc.). Highlights: **TH 2024 remittance reform** materially erodes LTR Wealthy Pensioner advantage (foreign-source income remitted to TH may now be assessable, flipping historical "remit-only-needed" calculus); **MA's 80% pension abatement (Art. 76 CGI) when remitted in DH** one of most generous globally and under-marketed vs PT/GR/IT; **PH SRRV materially more generous than TH/MY** (USD 10k–50k deposit, age 35+ in some classes) but country gets less retirement-press coverage than Thailand.
- `shared/digital-nomad.md` (+58) — DNV availability + threshold, internet quality tier, time-zone overlap, coworking density, cost-of-living tier. Highlights: **TH 2024 reform reverses 40-year-old workaround** (foreign-source income brought into TH in same/later year is now taxed — was previously exempt if remitted in next calendar year); **UY 11-year tax holiday** for new residents (or alternative 7% rate) competitive with PT-NHR (now ended) and ES-Beckham, largely unknown; **AE has no formal DNV** but Dubai Virtual Working Programme + federal Green Visa (5-yr) functionally equivalent and arguably better than most "named" 1-yr DNVs.
- `shared/compare.md` (+150) — region shortcuts extended (latam +DO/CO/UY/CL, anglo-non-eu +US, mediterranean +MA/IL/EG/TR; new shortcuts gcc-mena, southeast-asia, caucasus-eu-adjacent); precomputed verdict shortcuts updated; 22 new structural red-flags; 4 worked-example trios (JP/TH/PH retirement, AE/IL/CY tax-residence, CO/MX/PA LATAM digital-nomad, GE/PT/CY EU-adjacent low-tax). Highlights: **GE has lowest acquisition cost globally tracked** (~0.1-0.5%, beats EE/LT by an order of magnitude); **ID has highest acquisition cost** (~17-19% combined BPHTB+PPh+PPN on PMA new-build, exceeds even BE Brussels); **AE's "no property tax" headline misleading** — 5% Dubai housing fee on rental value via DEWA is structurally an annual carry, just routed through utility billing.
- `shared/price-index-feeds.md` (+53) — per-country HPI source registry for `--update --refresh-only`. Highlights: **DO and EG have no transaction-grade public HPI** — flagged plainly with verification path (3+ active listings + DGII or notarised deed comps); **VN 2024 Land Law replaced 5-year provincial land-price tables with annual ones** (meaningful methodological shift propagated to country playbook); **US needed 5 distinct rows** (FHFA + Case-Shiller = repeat-sales, NAR = transaction median, Zillow ZHVI = automated/asking-side, Redfin = MLS-derived) — none can substitute, ZHVI explicitly NOT a transaction index despite common misuse.

This sweep retires the "MEDIUM-on-universal-flags" debt that accumulated as Tier-1 + Tier-2 country playbooks landed faster than the cross-cutting tables could absorb. All 62 countries now render HIGH-confidence universal sections.
- feat(shared): backfill 13 cross-cutting tables for Tier-1 + Tier-2 (18 countries) ([#65](https://github.com/soreavis/property-deep-dive/pull/65)) — by @soreavis

### Added — 8 new country playbooks (Tier 2 expansion, 2026-05-01)

Tier-2 batch — second wave of Asia-Pacific + Caucasus + Africa + Middle East coverage. Same parallel-subagent research methodology as Tier-1 (PR #57). Country count: **54 → 62**. Five of the eight are foreign-buyer-restricted and lead with a `## Foreign buyer eligibility` section before `--price`.

- **🇬🇪 GE — Georgia** — most permissive in the region. NAPR cadastre with 1-hour express transfer at PSDA; foreigners freely own residential freehold (Constitution Art. 19); 1-yr visa-free for ~95 nationalities. Tax Code: 5% PIT flat on rental (small-business status), no CGT after 2-yr ownership, property tax only above GEL 40k household income (~USD 14.8k); buyer-side transaction cost ~0.1-0.5% of price (lowest in region tracked); EU candidate Dec 2023; Lari managed-float; Tbilisi Sakrebulo Decision 14-69 sets 2025 property-tax schedule. ~516 lines, primary sources NAPR/Geostat/NBG/rs.ge/Tbilisi City Hall/GNERC. (`countries/ge/playbook.md`)
- **🇮🇩 ID — Indonesia** — heavily restricted. Foreigners CANNOT own freehold (Hak Milik) — only Hak Pakai (PP No. 18/2021, 30+20+30=80yr direct ownership w/ KITAS/KITAP), SHMRS strata-title condos, HGB-via-PT-PMA, or Hak Sewa lease. Nominee structures (Hak Milik via Indonesian friend) ILLEGAL under UUPA Art. 26(2) — Bali Provincial Court has voided multiple 2023-2025; pre-2023 expat-forum advice now actively dangerous. BPHTB 5% transfer + PPh Final 2.5% seller + 11% PPN on new builds = 17-19% all-in for foreign new-build (materially higher than Thailand 3-5% or Czech 1-2%). Permenkumham 22/2023 Second Home Visa uniquely lets the qualifying IDR 2B asset BE the property itself. ~763 lines, primary sources BPN/atrbpn.go.id/BPS/DJP/BI/Imigrasi. (`countries/id/playbook.md`)
- **🇲🇾 MY — Malaysia** — moderately restricted. State-set foreign-buyer minimum thresholds (KL MYR 1M / Selangor MYR 2M / Penang Island MYR 1-3M / Johor MYR 1-2M tiered — verify per-state EXCO circular at offer date). Cannot buy Malay Reserved Land (Tanah Rizab Melayu), low-cost housing, agricultural smallholder. Foreigners pay flat **4% MOT stamp duty** vs progressive citizen scale (~36% more on RM 1.5M condo); RPGT permanent **10% for foreigners** even after 5+ yrs (citizens drop to 0% from 2022) — permanent foreign-buyer disadvantage at exit. MM2H relaunched 2024 — 3 tiers Silver/Gold/Platinum (MYR 1M-5M FD + MYR 40-50k/mo income). Sabah Cap. 68 + Sarawak Cap. 81 INDEPENDENT land regimes; locally-admitted lawyer required there. Penang Island STR ban (2020) + KL/PJ MC by-laws increasingly prohibit Airbnb. ~653 lines, primary sources JKPTG/LHDN/NAPIC/BNM/MOTAC/DOSM. (`countries/my/playbook.md`)
- **🇻🇳 VN — Vietnam** — heavily restricted. **2024 Land Law (Law No. 31/2024/QH15)** + **2023 Housing Law (Law No. 27/2023/QH15)** effective 1 Aug 2025: foreigners can own residential houses + apartments (NOT land) on 50-year lease + 50-yr renewal; quotas 30% per apartment block + 250 landed houses per ward; cannot buy in defense/security areas. Pink Book (Sổ Hồng) = LURC + ownership cert with 50-yr notation. **2024 Land Law expanded mortgage rights** to foreign-owned credit institutions (was domestic-only — material for foreign buyers needing leverage). Annual provincial land-price tables under 2024 Land Law replaced 5-yr tables (will track market more closely). PIT 5% rental (gross), 2% transfer (gross sale), VAT 10% new builds, **NO recurring property tax enacted as of 2026-05-01** (Ministry of Finance has consulted multiple times since 2017). **NO Vietnam Golden Visa via real estate exists** — DT investment visa requires enterprise capital, not RE; common foreign-buyer assumption is wrong. ~728 lines, primary sources GSO/SBV/GDT/MOC/MONRE/Vietnam Immigration. (`countries/vn/playbook.md`)
- **🇵🇭 PH — Philippines** — heavily restricted. **1987 Constitution Art. XII §7**: only Filipino citizens or 60% Filipino-owned corporations can own LAND. Foreigners CAN own condominium units (RA 4726 Condominium Act 1966) provided condo's foreign equity ≤40%; buildings on long-term-leased land (RA 7652 Investors' Lease Act 1993, 50+25yr); inheritance via succession. **Anti-Dummy Law (CA 108)** criminalizes nominee structures: 5–15 yrs imprisonment + property forfeiture for both Filipino dummy AND foreign inducer. SRRV (PRA) USD 10–50k deposit by age + classic/smile/courtesy categories; SIRV (BOI) USD 75k qualifying assets. **PH "CGT" is a misnomer**: 6% on the **GROSS sale price** (or zonal/FMV whichever higher) per NIRC §24(D) — transaction tax in substance, not gain-based; even loss-making sales taxed. Tax stacking: 6% CGT + 1.5% DST + 0.5–0.75% LTT + ~0.25% reg + 1–2% notarial = ~10% all-in. **English-language records** = major DD advantage vs Thailand/Vietnam/Indonesia. **Matthews v. Taylor (2009)** SC ruling: foreigners cannot reclaim funds used to buy land titled to a Filipino spouse — Path 4 spouse-titled is buy-at-own-risk. ~660 lines, primary sources LRA/BIR/BSP/PSA/DHSUD/PRA/BOI/DOJ. (`countries/ph/playbook.md`)
- **🇮🇱 IL — Israel** — de facto restricted via state-land monopoly + Olim privilege. **RMI / Israel Land Authority (Reshut Mekarkei Yisrael)** manages **~93% of land in Israel** (state ~70% + KKL/JNF ~12-13% + Development Authority ~10%). KKL/JNF land restricted to Jewish lessees by charter (litigation ongoing). Lease (חכירה) typical 49+49yr; **Heskem Hadash** post-2009 reform allows lessees to convert to freehold (חופשי) for capitalization fee on built-up land. Mas Rechisha non-resident scale 8% on first ILS 6.05M / 10% above; **Olim 7-year incentivized scale** 0.5% on first ILS 1.92M / 5% above — saves ~ILS 207k on a ILS 4M flat est. (single biggest financial lever a foreign buyer can pull). **Karnit (Property Tax & Compensation Fund)** state-funded war/missile damage compensation — Oct 2023 Israel-Hamas + Sep-Nov 2024 Israel-Hezbollah wars disrupted insurance markets, Karnit central. **VAT raised 17% → 18% on 1 Jan 2025** — common stale-data trap. **TAMA 38** (national earthquake retrofit incentive) **sunset 1 Oct 2022** — many sources online still reference it as active. Settlement-area Area C deeds out-of-scope for commodity DD. ~674 lines, primary sources RMI/Tabu/Tax Authority/BoI/CBS/Karnit/Aliyah Ministry. (`countries/il/playbook.md`)
- **🇲🇦 MA — Morocco** — permissive in most areas with specific exclusions. Foreigners CAN own freehold (mulk) most urban + tourism property — but **only on titré property** (immatriculé under ANCFCC Torrens-style cadastre). Cannot own agricultural land outside urban perimeters (Vivendi authorization or SCI structure required), habous (religious endowment) lands, collectif (tribal) lands without conversion. **Title status decision tree**: titré ✅ foreigner-buyable; non-titré (melkia) requires réquisition d'immatriculation; habous cannot be sold to non-Muslims; collectif requires conversion. **Office des Changes registration at purchase via authorised bank is the ONLY legal repatriation gateway** — skip and sale proceeds + rental income cannot leave dirham zone (non-convertible currency). Registration duty 4% + notarial 0.5–1% + conservation foncière 1.5% + broker 2.5% +VAT. CGT (TPI) 20% net gain, exempt if held >6 yrs primary res / >10 yrs secondary post-2017. **Mosque proximity** (adhan 200–500m audible pre-dawn) deal-breaker variable unique to MA, often missed by foreign buyers. **Al Haouz 2023 M 6.8 quake** materially changes pre-2024 building-stock risk in Marrakech + High Atlas valleys; RPS 2024 strengthened code (NOT retroactive — structural assessment essential through at least 2027 for any pre-2011 build). ~631 lines, primary sources ANCFCC/DGI/Bank Al-Maghrib/HCP/Office des Changes/Habous Ministry/SMIT/CFC. (`countries/ma/playbook.md`)
- **🇪🇬 EG — Egypt** — partially restricted + currency-volatile. **Law 230/1996**: max 2 properties/foreigner, max 4,000 m² each, NOT in protected/military/Sinai/border zones, NOT within 5 km of Suez Canal, agricultural land Egyptian-only, 5-yr resale lock (waivable Cabinet). **EGP devaluation history**: ~15.7→30→50/USD by Mar 2024 (IMF EFF approval, free-float Mar 2024) → ~50-51/USD by 2026-05-01 (managed float). Capital controls via CBE Form 4: foreign currency repatriation requires CBE-authorized bank + proof of original USD inflow. **Form 4 paper trail at purchase is the GATING procedural risk** for foreign USD-cash buyers — without it future USD repatriation of sale proceeds is structurally blocked, sellers stuck with EGP-only exit (catastrophic given EGP devaluation history). **CGT is 2.5% of GROSS sale price** (Law 175/2023) — even loss-making sales are taxed; materially distorts IRR modeling. **Investment Law 160/2023** RBI/CBI tiers: USD 250k cash deposit (5-yr) → PR / USD 300k RE → citizenship / USD 350k investment → citizenship; thresholds shifted multiple times since 2023. **Sinai is usufruct-only 50-yr leasehold from TDA** despite many Sharm El Sheikh sales offices marketing units as "freehold" — buyers regularly misled (deal-killer-class misrepresentation). New Administrative Capital + North Coast (Sahel) + Red Sea Riviera main foreign-buyer markets. ~610 lines, primary sources REPA/ETA/CBE/CAPMAS/GAFI/Ministry of Justice/MoH/IDA. (`countries/eg/playbook.md`)

### Changed — Tier-2 cross-cutting updates (2026-05-01)

- `_regions.json` — extended to **9 regions** (was 8): added new **`caucasus`** region (currently `ge` only — room to grow with AM/AZ in Tier-3); extended `mena` (`+il`), `apac` (`+id, my, vn, ph`), `africa` (`+ma, eg`).
- `SKILL.md` — argument-hint description updated 54 → **62 countries**; country matrix table extended with 8 new entries (GE/ID/MY/VN/PH/IL/MA/EG) after `za`; file tree updated; "all 54 supported countries are fully populated" → "all 62"; references to "44 countries" / "54 countries" in `crime-sources.md` and `finance.md` filemap comments bumped to 62.
- `README.md` — auto-synced via `scripts/sync-docs.py`; 54 → **62 country count** (+ 22 workflows / 109 markdown files / 39,300 lines); country-gaps section refreshed (GE/ID/MY/VN/PH/IL/MA/EG removed; Tier-3 deferred backlog now LI/SG/HK/KR/TW/IN/PE/EC/PY/TN/KE/NG/SA/QA/AM/AZ).
- `shared/visa-programs.md` — added new **Caucasus** region table (GE: visa-free 1-year for ~95 nationalities, Remotely from Georgia digital nomad, Investor Residence USD 300k, Work Permit); extended **Türkiye & Middle East** with IL (Aliyah, Investor B/5, retirement); **Asia-Pacific** with ID (Second Home Visa Permenkumham 22/2023 + KITAS Investor + Indonesia Golden Visa 2023), MY (MM2H Silver/Gold/Platinum tiers + PVIP 2022 + Sarawak/Sabah variants), VN (DT Investment + LD/DH Labour), PH (SRRV + SIRV + 13(a)/9(g) + Quota); **Africa** with MA (Carte de Séjour + CFC corporate) + EG (Investment Law 160/2023 RBI cash USD 250k / RE CBI USD 300k / investment CBI USD 350k + Golden Residency Decree 2024 USD 100k/200k/400k tiers). Updated Class A/B/C decision-helper (added GE Investor / EG RE-CBI / EG Golden / ID Second-Home to Class A; MY MM2H + PH SRRV + MA Carte de Séjour to Class B; VN Golden Visa via RE + IL RBI/CBI to Class C as "NEVER OFFERED"). Government portals row extended with 8 new countries.
- `shared/regulatory-watch.md` — added 8 new country sections (GE/ID/MY/VN/PH/IL/MA/EG) with date-stamped Tier 1–3 reform entries: 2024 Land Law + 2023 Housing Law VN effective 2025-08-01, PP 18/2021 ID Hak Pakai expansion, Bali nominee voidance precedents 2023-2025, Permenkumham 22/2023 ID Second Home Visa, EU candidate GE Dec 2023, MM2H 2024 relaunch MY, RA 12001 PH valuation revaluation 2024-2027, Anti-Dummy Law CA 108 PH criminal-grade nominee enforcement, IL VAT 17→18% Jan 2025, IL TAMA 38 sunset Oct 2022, Israel-Hamas/Hezbollah war insurance disruption Oct 2023→ongoing, MA Al Haouz 2023 M 6.8 quake + RPS 2024 code, MA Office des Changes mandatory FX gateway, EG EGP free-float Mar 2024 + Form 4 mandatory + Investment Law 160/2023 RBI/CBI + Law 230/1996 + Sinai usufruct-only misrepresentation. "44 countries × 22 sections" rationale bumped to 62.
- `CLAUDE.md` — file-map comment "44 country playbooks" → "62 country playbooks"; "fill in tax rates for all 44 countries" example → "all 62 countries".
- `.claude-plugin/plugin.json` — marketplace-facing description "Pre-purchase property due diligence across 44 countries" → "62 countries"; bottom summary "44 countries fully populated" → "62 countries fully populated".
- `.github/ISSUE_TEMPLATE/new-country.yml` — pre-flight check label "(44 countries currently)" → "(62 countries currently)".
- `shared/auto-validate.md` — sample report header "44 countries validated" → "62 countries validated".
- `shared/compare.md` — opening "Leverages all 44 country playbooks at once" → "all 62".
- feat: add 8 Tier-2 country playbooks (GE/ID/MY/VN/PH/IL/MA/EG) + fix decay-matrix workflow ([#62](https://github.com/soreavis/property-deep-dive/pull/62)) — by @soreavis

### Fixed — health-report decay-matrix workflow (2026-05-01)

`health-report.yml` decay-matrix scheduled job was failing on main with `exit code 1` because:
- `set -euo pipefail` + grep returning no match (exit 1) propagated through the `| head | awk` pipeline (pipefail) → command-substitution exit 1 → errexit aborted the job.
- 3 country playbooks didn't have a bare `as of YYYY-MM-DD` line in their Status footer for grep to match: `co/playbook.md` and `tr/playbook.md` had `as of **2026-05-01**` (bold around date — same regex gotcha as pr-validate's last-verified-stamp check); `eg/playbook.md` was missing the line entirely.

Fixed in two layers:
- Defensive: appended `|| true` to the `grep | head | awk` pipeline so empty-grep is now handled by the existing `tier="UNKNOWN"` branch instead of aborting the run.
- Stamp normalization: re-stamped CO + TR Status footers with bare `as of 2026-05-01`; added the missing line to EG. All 62 country playbooks now have a bare-date `as of` stamp the workflow can read.

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

- **Plugin payload co-located** under `skills/property-deep-dive/`. Moved `shared/` (34 files) and `countries/<iso2>/playbook.md` (44 files) into the skill folder so plugin hosts (Claude Cowork, Claude Code) ship the entire payload from a single self-contained directory. Without this, post-PR-#33 plugin installs only received `SKILL.md` and every `shared/*` reference inside it resolved to nothing — Cowork agents fell back to live research without the anti-hallucination contract. Path references inside `SKILL.md` / `shared/*.md` / `countries/*/playbook.md` remain relative and resolve unchanged. Outside-the-skill references (13 workflows, `scripts/sync-docs.py`, labeler/labels/PR template, 3 issue templates, README/CONTRIBUTING/CLAUDE/DISCLAIMER/SECURITY, docs/) updated to the new path.
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
