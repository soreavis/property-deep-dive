# Regulatory Watch — Cross-Country Reform Tracker

A single date-stamped registry of property-relevant reforms, transposition deadlines, ENDED programs, and watchlist items. Maintained as the **single source of truth for "what changed when"** — playbooks reference this; this references playbooks.

**Why it exists**: At 44 countries × 22 sections, the highest-blast-radius hallucination is asserting that an ENDED program is still active or quoting a tax rate that was reformed last quarter. This file makes "did anything change?" a single-file lookup before any re-stamp.

**Maintainer**: human + Claude. Each entry must have a primary-source URL, a verified date, and a next-revisit date.

---

## How to use this file

### Before producing any output

`--tax`, `--rental`, `--visa`, `--finance`, `--mains` (where regulated) sections must consult this file. If a relevant entry's `revisit_by` date has passed AND the playbook still asserts the pre-reform value, the section's confidence auto-downgrades (see `updater.md` § Auto-downgrade).

### Before re-stamping a section's `**Last verified**`

Check this file for entries touching the section since the prior stamp. If a reform is logged here that the playbook doesn't reflect, the section is **not yet re-verified** — patch the playbook first.

### When adding an entry

Required fields:
- `country` (ISO2)
- `topic` (one of: tax, rental, visa, finance, ownership, esg, cadastre, eurozone, other)
- `effective_date` (YYYY-MM-DD or "pending" + estimate)
- `enacted_date` (when the law/regulation was passed)
- `verified_date` (last time we confirmed status)
- `revisit_by` (next mandatory check)
- `source_url` (primary government / official journal preferred)
- `impact_tier` (1–4, see below)
- `playbook_sections_touched` (list of `--<flag>` flags)

---

## Impact tiers — how to rate a reform

The tier drives revisit cadence and anti-hallucination priority.

| Tier | Meaning | Revisit cadence | Example |
|---|---|---|---|
| **1 — CRITICAL** | Reverses a prior assertion the skill makes (e.g., visa program ENDED, tax rate inverted, ownership opened/closed). Stale claim is a confident lie. | 30 days | MT MEIN ECJ ENDED 29 Apr 2025 |
| **2 — MAJOR** | Material number change (>20% rate move), new mandatory diagnostic, EU directive transposition affecting many countries. | 90 days | RO VAT 19 → 21% Aug 2025; EPBD 2024/1275 |
| **3 — MEANINGFUL** | Threshold/credit/exemption tweak; parliamentary stage advance; rumored-to-draft transition. | 180 days | CY 2026 Comprehensive Tax Reform (CGT exemptions raised) |
| **4 — INCREMENTAL** | Indexation adjustment, fee tweak, technical correction, watchlist signal. | 365 days | LU Bëllegen Akt indexation; LV cadastral value rebase rumored |

---

## ENDED programs — anti-hallucination critical (Tier 1)

Every entry below is **CONFIRMED CLOSED**. Listing any of these as active is the highest-stakes failure mode for `--visa`. Cross-check before any visa-section output.

| Country | Program | Closed date | Source / mechanism | Successor (if any) |
|---|---|---|---|---|
| 🇲🇹 MT | MEIN (Investor citizenship) | 29 Apr 2025 | ECJ Case C-181/23 ruling | none |
| 🇪🇸 ES | Golden Visa | 03 Apr 2025 | Law 1/2025 (Justice efficiency act) | none |
| 🇮🇪 IE | IIP (Immigrant Investor Programme) | 15 Feb 2023 | Government press release | none |
| 🇨🇾 CY | Citizenship by Investment | 01 Nov 2020 | Council of Ministers decision | non-dom 17yr (residency only) |
| 🇧🇬 BG | CBI / fast-track | 18 Jun 2024 | Bulgarian parliament | none |
| 🇭🇺 HU | Residency Bond | 31 Mar 2017 | Programme expiration | Guest Investor 2024 (different) |
| 🇬🇧 UK | Tier 1 Investor | 17 Feb 2022 | Home Office | none (Innovator Founder different) |
| 🇦🇺 AU | Significant Investor Visa (SIV / 188C) | 31 Jul 2024 | Migration program 2024-25 | none |
| 🇵🇹 PT | NHR (original 10-yr scheme) | 31 Dec 2023 (last applications) | OE 2024 | IFICI / NHR 2.0 — narrower, **pensions excluded** |
| 🇵🇹 PT | Golden Visa — residential RE | 06 Oct 2023 | Mais Habitação law | GV via funds/research only |
| 🇲🇪 ME | Citizenship by Investment | 31 Dec 2022 | Programme expiration | none |
| 🇦🇱 AL | CBI (proposed but never operational) | n/a | Never enacted | n/a — do not list as available |

**Rule**: If a user asks "what visa programs are open in <country>", consult this table first; only entries NOT here are candidates for "open" status, and even those need a fresh `verified_date` ≤180 days.

---

## Recently enacted reforms (last 24 months)

Listed by country. Each entry: `effective | topic | summary | source | verified | revisit_by | tier | sections`.

### 🇫🇷 FR

- `2024-11-19 | rental | Loi Le Meur — short-let (meublé tourisme) tightened: classement obligation expanded, 30-day primary-residence cap option for communes | LégiFrance | 2026-04-26 | 2026-10-01 | 2 | --rental --tax`
- `2025-01-01 | esg | DPE G banned for rental on new contracts | LégiFrance | 2026-04-26 | 2027-01-01 | 1 | --rental --esg`
- `2028-01-01 (pending) | esg | DPE F to be banned for rental | LégiFrance | 2026-04-26 | 2027-06-01 | 2 | --rental --esg`
- `2034-01-01 (pending) | esg | DPE E to be banned for rental | LégiFrance | 2026-04-26 | 2028-01-01 | 3 | --rental --esg`
- `2026-2028 (in flight) | tax | RVLLH cadastral revaluation rolling — +20-40% TFPB rural expected | DGFiP | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇮🇹 IT

- `2026-01-01 | rental | Cedolare secca limit dropped from 5 → 2 properties (above which standard IRPEF) | Legge di Bilancio 2026 | 2026-04-26 | 2026-09-01 | 2 | --rental --tax`
- `2024-01-01 | tax | Southern Italy 7% pensioner regime — re-confirmed annually; expires after 9 yrs of residency | Agenzia delle Entrate | 2026-04-26 | 2027-01-15 | 2 | --tax (pension regime)`

### 🇪🇸 ES

- `2025-04-03 | visa | Golden Visa programme abolished | Ley 1/2025 | 2026-04-26 | 2026-10-01 | 1 | --visa`
- `2025-06-XX | tax | Cataluña ITP made progressive (replacing flat 10%) — top bracket 13% for >€1.5M | Generalitat de Catalunya | 2026-04-26 | 2026-10-01 | 2 | --tax`
- `2024-06-01 | rental | Madrid + Barcelona STR licensing freeze (de facto) | Municipal ordinances | 2026-04-26 | 2026-09-01 | 2 | --rental`

### 🇵🇹 PT

- `2024-03-22 | tax | NHR replaced by IFICI/NHR 2.0 — **pensions NO LONGER exempt** (only specified scientific/innovation activities) | Decreto-Lei 21-A/2024 | 2026-04-26 | 2026-10-01 | 1 | --visa --tax (pension)`
- `2023-10-06 | visa | Golden Visa — residential real estate route closed; funds/research routes remain | Mais Habitação law | 2026-04-26 | 2026-09-01 | 1 | --visa`
- `2025-XX-XX | rental | Lisbon AL (Alojamento Local) suspended in stress zones — confirm post-2024 election outcome | Camara Municipal de Lisboa | 2026-04-26 | 2026-07-01 | 2 | --rental`

### 🇮🇸 IS

- `2024-XX-XX | rental | STR cap of 90 nights/yr without licence remains; tightened enforcement post-Reykjanes eruptions | Sýslumaður | 2026-04-26 | 2026-10-01 | 3 | --rental`

### 🇸🇪 SE / 🇫🇮 FI / 🇳🇴 NO

- `2024-01-01 | tax | FI varainsiirtovero (transfer tax) reduced 4% → 3% (real estate) and 2% → 1.5% (housing co-op shares) | Vero.fi | 2026-04-26 | 2026-09-01 | 2 | --tax (FI)`

### 🇬🇧 UK

- `2025-04-06 | tax | Non-dom regime abolished, replaced by 4-yr FIG (Foreign Income & Gains) regime | HMRC | 2026-04-26 | 2026-09-01 | 2 | --tax --visa`
- `2025-04-01 | tax | SDLT additional dwelling supplement increased 3% → 5% | HMRC | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇨🇭 CH

- `2028-01-01 (pending) | tax | Eigenmietwert (imputed rental value tax) abolition — referendum approved Sep 2025; phased | Federal Council | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇩🇪 DE

- `2025-01-01 | tax | Grundsteuer reform — new property values applied (regional models: Bundesmodell vs Bayern/Baden-W. variants) | BFH | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇦🇹 AT

- `2024-XX-XX | tax | Tirol/Salzburg/Vorarlberg foreign-buyer quotas tightened (annual review) | Land governments | 2026-04-26 | 2026-09-01 | 2 | --tax (ownership)`

### 🇳🇱 NL

- `2025-01-01 | rental | Affordable Rent Act (Wet betaalbare huur) — points-based cap extended to mid-segment; affects rental yield | Rijksoverheid | 2026-04-26 | 2026-09-01 | 1 | --rental`
- `2026-01-01 | tax | Box 3 reform — actual return basis (replacing notional yield) | Belastingdienst | 2026-04-26 | 2026-07-01 | 1 | --tax`

### 🇧🇪 BE

- `2024-XX-XX | tax | Flanders registratierechten — 3% main residence, 12% other; refinements quarterly | Vlaamse Belastingdienst | 2026-04-26 | 2026-10-01 | 3 | --tax`

### 🇩🇰 DK

- `2024-01-01 | tax | New ejendomsskat (property value tax) regime live — based on 2020-vintage public valuations | Vurderingsstyrelsen | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇨🇿 CZ

- `2024-01-01 | tax | DPH (VAT) reduced rates consolidated 12% / 21%; building-supply VAT changes | Finanční správa | 2026-04-26 | 2026-09-01 | 3 | --tax`

### 🇸🇰 SK

- `2025-01-01 | tax | DPH (VAT) raised 20% → 23% standard; reduced rates restructured | Finančná správa | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇸🇮 SI

- `2026-01-01 (in flight) | tax | Davek na nepremičnine (annual property tax) reform — replacing NUSZ; phased | MF SI | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇭🇷 HR

- `2023-01-01 | currency | Eurozone accession (HRK → EUR) | ECB | 2026-04-26 | 2027-01-01 | 1 | --currency --tax`
- `2025-01-01 | tax | Porez na nekretnine — annual property tax on second/empty homes implemented | Porezna uprava | 2026-04-26 | 2026-09-01 | 2 | --tax`
- `ongoing | ownership | 10-yr lock on agricultural land for non-EU buyers | MPGI | 2026-04-26 | 2027-01-01 | 2 | --tax (ownership)`

### 🇬🇷 GR

- `ongoing | tax | 7% flat on foreign-source income for foreign pensioners — 15-yr regime, application open | AADE | 2026-04-26 | 2026-12-01 | 2 | --tax (pension regime)`
- `2024-XX-XX | rental | STR registration tightening; AADE Property Number mandatory | AADE | 2026-04-26 | 2026-09-01 | 3 | --rental`

### 🇪🇪 EE

- `2024-01-01 | tax | Land tax indexation cap raised 10% → 50% annual change | Maksu- ja Tolliamet | 2026-04-26 | 2026-10-01 | 3 | --tax`
- `2025-01-01 | tax | Income tax 20% → 22% (touches rental income) | Maksu- ja Tolliamet | 2026-04-26 | 2026-09-01 | 2 | --tax --rental`

### 🇱🇹 LT

- `2024-02-01 | tax | Vilnius city tourist tax €2/night (first Baltic capital) | Vilnius municipality | 2026-04-26 | 2026-10-01 | 3 | --rental --tax`
- `2025-02-XX | mains | BRELL grid synchronization exit — Baltic states joined Continental European grid | Litgrid | 2026-04-26 | 2027-02-01 | 2 | --mains`
- `2026-01-01 | tax | NTM (Real Estate Tax) made progressive — primary residence threshold + tiered rates | Valstybinė mokesčių inspekcija | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇱🇻 LV

- `2026-01-01 | tax | PIT progressive 25.5% / 33% (replacing 20/23/31 ladder) | VID | 2026-04-26 | 2026-09-01 | 2 | --tax --rental`
- `ongoing | ownership | RU/BY citizens cannot purchase real estate (sanctions extension) | Saeima | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`
- `ongoing | ownership | Compulsory land lease (`dalītais īpašums`) — Riga Soviet-era split-title gotcha | Zemesgrāmata | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`

### 🇷🇴 RO

- `2025-08-01 | tax | VAT raised 19% → 21% standard | ANAF | 2026-04-26 | 2026-09-01 | 2 | --tax`
- `2026-01-01 | tax | Local property tax baseline +167% (recalibration to market values) | Ministerul Finanțelor | 2026-04-26 | 2026-09-01 | 1 | --tax`

### 🇧🇬 BG

- `2026-01-01 | currency | Eurozone accession at 1.95583 (BGN → EUR) | ECB | 2026-04-26 | 2027-01-01 | 1 | --currency --tax`
- `ongoing | ownership | Non-EU citizens cannot own ANY land (only buildings); EU citizens unrestricted post-2014 | Ministry of Justice | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`

### 🇱🇺 LU

- `2025-07-01 | tax | Bëllegen Akt €40k credit per person made PERMANENT | AED | 2026-04-26 | 2027-01-01 | 2 | --tax`
- `2030-01-01 (pending) | tax | IFON (impôt foncier) phased reform — replacing current 1941-vintage values | AED + ACT | 2026-04-26 | 2026-12-01 | 2 | --tax`

### 🇨🇾 CY

- `2026-01-01 | tax | Comprehensive Tax Reform — CGT principal-residence exemption €17,086 → €30,000; agricultural €25,629 → €50,000; other €17,086 → €150,000; SDC on rental abolished | Ministry of Finance | 2026-04-26 | 2026-09-01 | 1 | --tax --rental`
- `2025-XX-XX | ownership | Trapped Buyers Amendment Law 110(I)/2025 — title-deed transfer protections strengthened | DLS | 2026-04-26 | 2026-10-01 | 2 | --tax (ownership)`

### 🇲🇹 MT

- `2025-04-29 | visa | MEIN (Investor Citizenship) ENDED by ECJ Case C-181/23 | ECJ + Identità | 2026-04-26 | 2026-10-01 | 1 | --visa`
- `2025-2035 | cadastre | LRA reform target — full compulsory registration phase-in | Land Registration Agency | 2026-04-26 | 2027-01-01 | 3 | --tax (cadastre) --mains`

### 🇨🇦 CA

- `2027-01-01 (pending end) | ownership | Foreign-buyer Prohibition Act extended through 1 Jan 2027 | CMHC | 2026-04-26 | 2026-10-01 | 1 | --tax (ownership)`

### 🇦🇺 AU

- `2025-04-01 → 2027-03-31 | ownership | Established-homes ban on foreign purchase | FIRB | 2026-04-26 | 2026-10-01 | 1 | --tax (ownership)`
- `2024-07-31 | visa | SIV (Significant Investor Visa) closed | Home Affairs | 2026-04-26 | 2026-09-01 | 1 | --visa`

### 🇳🇿 NZ

- `2018-10-22 | ownership | Overseas Investment Amendment Act — permanent ban on foreign purchase of existing residential | LINZ | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`
- `2024-07-01 | tax | Bright-line test reduced 10 yr → 2 yr | IRD | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇲🇽 MX

- `ongoing | ownership | Fideicomiso (bank trust) required within 50 km coast / 100 km border for foreign buyers | SRE | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`

### 🇧🇷 BR

- `2026-XX-XX (in flight) | cadastre | CIB (national cadastral identifier) rolling out — replacing fragmented Cartórios | Ministério da Fazenda + Receita | 2026-04-26 | 2026-09-01 | 3 | --tax (cadastre)`
- `2024-XX-XX | tax | Tributary Reform Constitutional Amendment 132/2023 — IBS/CBS replacing PIS/Cofins/ICMS/ISS, transition through 2033 | Receita Federal | 2026-04-26 | 2026-10-01 | 1 | --tax`

### 🇦🇷 AR

- `2024-XX-XX | tax | Bienes Personales — decreasing schedule 1.10% / 1.00% / 0.50% (Ley 27.743 consolidation) | AFIP | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇨🇷 CR / 🇵🇦 PA

- `ongoing | tax | Both territorial-ish for non-resident foreign-source; PA Pensionado $1,000/mo lifetime requirement | DGI CR / DGI PA | 2026-04-26 | 2027-01-01 | 2 | --tax (pension regime)`

### 🇲🇪 ME

- `2024-01-01 | tax | RETT made progressive 3% / 5% / 6% (replacing flat 3%) | MFA ME | 2026-04-26 | 2026-10-01 | 1 | --tax`

### 🇲🇰 MK

- `ongoing | tax | CGT 10% (NOT 15% — common error) with 5-yr OR 3yr+1yr-resident exemption | UJP | 2026-04-26 | 2026-10-01 | 1 | --tax`

### 🇧🇦 BA

- `ongoing | cadastre | Dual-entity (FBiH / RS-entity / Brčko) — different cadastres + tax regimes | Entity-level authorities | 2026-04-26 | 2027-01-01 | 1 | --tax --mains`

### 🇷🇸 RS

- `2014-05 | risks | Sava + Bosna river floods (NOT Drava — common error; Drava is HR/SI) | RHMZ | 2026-04-26 | 2027-01-01 | 4 | --risks`

---

## EU directive transposition deadlines

EU directives apply to all 27 member states. Transposition deadline is the date by which national law must reflect the directive.

| Directive | Topic | Transposition deadline | Status (Apr 2026) | Affected sections |
|---|---|---|---|---|
| **2024/1275** (EPBD recast) | Energy performance — zero-emission buildings, MEPS, mandatory renovation passports | **29 May 2026** | Approaching deadline; member states finalising national plans | `--esg` `--rental` |
| **2024/1028** | Short-let registration harmonisation | 20 May 2026 (registration system) → 20 May 2028 (full data-sharing) | First milestone passed; data-sharing pending | `--rental` |
| **2024/2831** (AMLD6) | Beneficial-ownership registers — single-access EU portal | 10 Jul 2027 | Pending national transposition | `--tax` (ownership) `--finance` |
| **2023/2226** (DAC8) | Crypto-asset reporting | 31 Dec 2025 transposition; first reports 2026 | Transposed; first reporting cycle live | `--tax` |
| **(EU) 2024/1689** (AI Act) | High-risk AI in mortgage scoring etc. | Phased through Aug 2026 | Phased rollout | `--finance` (indirect) |
| **2018/2002** (EED amendment) | Energy efficiency | Continuing transposition reviews | Ongoing | `--esg` |

**Rule**: For any EU country playbook's `--esg` or `--rental` section, EPBD recast 2024/1275 must be referenced if the section claims any energy-rating rental ban schedule. The deadline 29 May 2026 is **imminent** as of Apr 2026 — surface the deadline date in the playbook.

---

## Watchlist — rumored / proposed (Tier 4)

Things signalled but not enacted. Track for upgrade to Tier 1–3 when official.

| Country | Signal | Source signal | Last heard | Re-check |
|---|---|---|---|---|
| 🇦🇱 AL | DIVA STR registration system Jan 2026 launch | Albanian government press | 2026-01 | 2026-07 |
| 🇪🇸 ES | National 100% tax on non-EU buyers (Sánchez Jan 2025 floated) | Government press conference | 2025-01 | 2026-09 |
| 🇮🇪 IE | LPT (Local Property Tax) revaluation 2025 — bands shifted | Revenue.ie | 2025-11 | 2026-09 |
| 🇨🇭 CH | Cantonal Lex Koller permit caps tightening | SECO | 2026-01 | 2026-10 |
| 🇸🇪 SE | Capital gains rules on primary-residence sales — reform proposed | Skatteverket | 2026-02 | 2026-10 |
| 🇩🇪 DE | Bundesrat may reverse parts of Grundsteuer Bundesmodell | Bundesrat | 2026-03 | 2026-09 |
| 🇸🇮 SI | Davek na nepremičnine final shape — multiple drafts in flight | MF SI | 2026-04 | 2026-09 |

---

## Per-playbook impact map

When a Tier 1–2 entry is added here, these playbook sections need re-stamping:

| Topic | Sections to re-stamp |
|---|---|
| tax (rate/threshold) | `--tax`, `--rental` if rental-affecting, country playbook benchmark tables |
| visa (open/close) | `--visa`, country playbook `--work` if tied, `shared/visa-programs.md` |
| rental (regulation) | `--rental`, `--tax` if cedolare-style regime |
| esg (energy-rating) | `--esg`, `--rental` (rental-ban schedules) |
| ownership (foreign buyer) | country playbook `--tax` ownership block, `shared/exit.md` foreign-buyer-pool table |
| eurozone | `--currency`, `--tax`, all country benchmarks in local currency |
| cadastre | country playbook `--mains` + `--tax`, `shared/comparable-transactions.md` tier classification |
| pension regime | `shared/retirement.md`, country playbook `--tax` |

---

## Maintenance cadence

This file gets the same auto-validate treatment as country playbooks:

- **Weekly**: URL liveness on every entry (cron via `auto-validate.md`)
- **Monthly**: scan all entries with `revisit_by` ≤ 30 days from today; create review queue
- **Quarterly**: full re-research of all Tier 1 entries (visa programs especially); confirm ENDED programs haven't been resurrected
- **At-event**: when a regulatory news item lands (EU Official Journal, national gazette, ECJ ruling, central-bank decision), add or update an entry **before** it propagates errors into playbooks

Subscribe these feeds for at-event updates:
- EU Official Journal: https://eur-lex.europa.eu/oj/direct-access.html
- ECJ press releases: https://curia.europa.eu/jcms/jcms/Jo1_6308/en/
- Per-country gazettes (LégiFrance, Gazzetta Ufficiale, BOE, etc. — already in country playbooks)
- OECD Tax Policy Reforms annual report
- Tax Foundation Europe weekly digest

---

## Format for new entries

```markdown
- `<effective_date> | <topic> | <one-line summary> | <source name> | <verified_date> | <revisit_by> | <tier> | <sections>`
```

Multi-line is fine if the entry is complex; the seven-pipe format is the canonical machine-readable form.

---

## Related files

- `shared/anti-hallucination.md` — defines the confidence-label tiers this file's `revisit_by` feeds into
- `shared/updater.md` — auto-downgrade rule that uses this file's `revisit_by` to decay confidence
- `shared/visa-programs.md` — universal `--visa` section; ENDED registry above is the source of truth
- `shared/auto-validate.md` — cron infrastructure that re-checks URLs in this file weekly
- `shared/exit.md` — foreign-buyer-pool tables that depend on Tier 1 ownership entries

---

*Last full audit: 2026-04-26. Next mandatory full audit: 2026-07-26 (quarterly).*
