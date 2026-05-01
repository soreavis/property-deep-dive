# Regulatory Watch — Cross-Country Reform Tracker

A single date-stamped registry of property-relevant reforms, transposition deadlines, ENDED programs, and watchlist items. Maintained as the **single source of truth for "what changed when"** — playbooks reference this; this references playbooks.

**Why it exists**: At 87 countries × 22 sections, the highest-blast-radius hallucination is asserting that an ENDED program is still active or quoting a tax rate that was reformed last quarter. This file makes "did anything change?" a single-file lookup before any re-stamp.

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

### 🇺🇸 US

- `2025-07-04 | tax | OBBBA (PL 119-21) reset SALT cap to $40k (sunset 2030); MID $750k cap permanent; §§ 25C/25D Energy Credits TERMINATED 31 Dec 2025; NRA estate exempt $15M (2026) | IRS + Congress.gov | 2026-05-01 | 2026-12-15 | 1 | --tax --finance --visa`
- `2024-12-09 | risks | CFIUS 31 CFR Part 802 added 59 sites near military installations (foreign-buyer review) | Treasury OFAC | 2026-05-01 | 2026-11-01 | 2 | --risks --visa`
- `2024-10 | mains | EPA Lead and Copper Rule Improvements (LCRI) — full lead-service-line replacement compliance 1 Nov 2027 | EPA | 2026-05-01 | 2026-11-01 | 2 | --mains`
- `2025-09-01 | tax | Texas SB 17 foreign-buyer land restrictions effective | TX SOS | 2026-05-01 | 2026-11-01 | 2 | --visa --price`
- `2024-08 | rental | NAR settlement unbundled buyer-agent commissions nationwide | NAR + DOJ | 2026-05-01 | 2026-08-01 | 2 | --price --exit`
- `2023-04 | risks | NFIP Risk Rating 2.0 fully implemented | FEMA | 2026-05-01 | 2026-10-01 | 3 | --risks --insurance`

### 🇹🇷 TR

- `2024-01-01 | rental | Law 7464 Konut Hizmetleri Kanunu — STR licensing mandatory; post-31-Dec-2024 transition closed; fines 100k–1M TRY/property | Resmi Gazete + Kültür ve Turizm Bakanlığı | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2022-06-13 | visa | CBI threshold raised USD 250k → USD 400k; 3-year non-resale lock; some districts excluded | Cumhurbaşkanlığı kararı | 2026-05-01 | 2026-08-01 | 1 | --visa --price`
- `2023-02 | risks | Kahramanmaraş M7.8 + M7.5 earthquake → regulatory tightening (yapı denetim + Law 6306 kentsel dönüşüm acceleration + DASK enforcement); TBDY 2018 building code becoming effective baseline | AFAD + Çevre Bakanlığı | 2026-05-01 | 2026-09-01 | 1 | --risks --insurance`
- `2025-09 | tax | Land+Building Tax (Emlak Vergisi) reduction Cabinet resolution renewed annually — verify 2026 status | GİB + Resmi Gazete | 2026-05-01 | 2026-12-31 | 2 | --tax`
- `2026-2029 | tax | Rayiç bedel cycle — base values for Emlak Vergisi reset every 4 yrs; 2026-2029 cycle showing 3-5× nominal jumps under litigation | TKGM + Belediyeler | 2026-05-01 | 2027-01-01 | 2 | --tax`

### 🇦🇪 AE

- `2024-04 | risks | Record Dubai floods exposed drainage limits → Tasreef stormwater plan phased to 2033 (interim AED 277m completed Jun 2025) | Dubai Municipality | 2026-05-01 | 2026-11-01 | 2 | --risks --insurance`
- `2025 | finance | Dubai Law 2/2025 — DIFC Wills direct enforcement for non-Muslim expats | DIFC Courts | 2026-05-01 | 2026-10-01 | 2 | --finance --notary`
- `2023-06 | tax | Federal Corporate Tax 9% effective from Jun 2023 — applies to commercial property held in qualifying entities above AED 375k threshold; individual ownership unaffected | FTA UAE | 2026-05-01 | 2026-09-01 | 2 | --tax --finance`
- `2025 | rental | RERA Smart Rental Index expanded to A/B/C/D building-quality scoring; brackets refreshed | DLD + RERA | 2026-05-01 | 2026-09-01 | 2 | --rental`
- `2022-10 | visa | Cabinet Decision 65/2022 expanded Golden Visa RE route to AED 2M (single or aggregate); off-plan + escrow eligible | ICP + DLD | 2026-05-01 | 2026-08-01 | 1 | --visa`

### 🇯🇵 JP

- `2023-12 | tax | 空家特措法 (Vacant Houses Special Measures Act) 改正 — 管理不全空家 designation can revoke 1/6 land tax exemption (~6× annual fixed-asset bill on land portion) | MLIT | 2026-05-01 | 2026-09-01 | 2 | --tax --risks`
- `2024-04-01 | finance | 民法改正 (Civil Code reform) — mandatory inheritance registration within 3 yrs (¥50k fine), 2-yr address-change registration; foreign-heir traps | 法務省 | 2026-05-01 | 2026-09-01 | 2 | --finance --notary`
- `2024-2025 | finance | BoJ rate normalization (Mar 2024 NIRP exit → Jul 2024 0.25% → Jan 2025 0.5% → Dec 2025 ~0.75%); mortgage variable rates rising; Flat 35 applications +50% YoY Q3 2025 | BoJ | 2026-05-01 | 2026-08-01 | 1 | --finance --price`
- `2018-06 | rental | 民泊法 Minpaku law 180-night/yr cap; 2025 Tokyo + Kyoto + Osaka ward-level overlay restrictions intensifying | 観光庁 民泊ポータル | 2026-05-01 | 2026-09-01 | 2 | --rental`
- `2022-09-20 | risks | 重要土地等調査法 (Important Land Investigation Act) effective; 注視区域 around defense / border / nuclear facilities; reporting may apply to certain residential transactions | 内閣府 | 2026-05-01 | 2026-10-01 | 2 | --risks --visa`

### 🇹🇭 TH

- `2020-01 | tax | Land and Building Tax Act BE 2562 (2019) effective — first national property tax; rates 0.01–0.7% by use; annual Royal Decree reductions | Revenue Department | 2026-05-01 | 2026-08-01 | 1 | --tax`
- `2024-mid | visa | Destination Thailand Visa (DTV) launched — 5-yr multi-entry, 180 days/stay, THB 500k savings + freelance/remote-worker proof | MFA Thailand + Immigration Bureau | 2026-05-01 | 2026-08-01 | 2 | --visa --digital-nomad`
- `2024-2025 | rental | Hotel Act §4 STR enforcement intensifying — STR <30 nights without hotel license illegal; varies by province; Bangkok / Phuket leading enforcement | DBD + provincial governors | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2024-2025 | visa | Proposed 99-yr lease + 75% condo quota — under Cabinet discussion; NOT enacted as of May 2026 | Cabinet of Thailand | 2026-05-01 | 2026-09-01 | 2 | --visa --price`
- `2024 | tax | Foreign-source income remittance taxation — Revenue Dept interpretation evolving | Revenue Department | 2026-05-01 | 2026-08-01 | 2 | --tax --visa`

### 🇩🇴 DO

- `2017 | finance | AML Ley 155-17 + UAF — beneficial-owner disclosure + source-of-funds proof for property transactions | UAF | 2026-05-01 | 2026-12-01 | 3 | --finance --notary`
- `2022 | risks | Hurricane Fiona (Sept 2022) → MOPC R-007 amendments to track | MOPC | 2026-05-01 | 2026-10-01 | 3 | --risks --insurance`
- `2025 | tax | IPI threshold DOP 9,860,649 (2025) — indexed annually; CONFOTUR-registered tourism projects 100% IPI + transfer + ITBIS exempt ~15 yrs | DGII + MITUR | 2026-05-01 | 2027-01-01 | 2 | --tax`
- `ongoing | visa | Investor residency USD 200k → 2-3-yr citizenship — fast-track to passport; CONFOTUR-registered RE benefits stack | Migración + MITUR | 2026-05-01 | 2026-09-01 | 2 | --visa`

### 🇨🇴 CO

- `2020 | finance | Decreto 1339/2020 — Catastro multipropósito national rollout; closing avalúo-vs-comercial gap; some areas seeing 2-3× predial bills | IGAC + DNP | 2026-05-01 | 2026-09-01 | 2 | --tax --price`
- `2024 | rental | Bogotá Decreto 538/2024 — 10% STR lodging tax + RNT mandatory | Alcaldía Bogotá + MITUR | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2024 | rental | Medellín El Poblado Acuerdo 056/2024 — STR restrictions evolving | Concejo Medellín | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2022 | tax | Ley 2277/2022 reforma tributaria — gan. ocas. 15%, wealth tax above UVT threshold | DIAN + MinHacienda | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `ongoing | visa | Migratorio M visa real-estate route 350× SMLMV (~USD 125k 2026); 650× → PR-eligible after 5 yrs | Cancillería + Migración | 2026-05-01 | 2026-09-01 | 2 | --visa`

### 🇺🇾 UY

- `2021 | tax | Ley 19.937 — 11-year exemption on foreign interest+dividends for new tax residents (extends Ley 18.083); major wealth-relocation magnet from AR/BR | MEF + DGI | 2026-05-01 | 2026-12-01 | 1 | --tax --visa`
- `2020 | tax | Decreto 138/020 + 153/020 — lowered RE investment threshold to UI 3.5M (~USD 470k) for tax residency | MEF + DGI | 2026-05-01 | 2026-12-01 | 2 | --tax --visa`
- `2018 | finance | Ley 19.210 financial inclusion — cash-payment caps 40,000 UI for property AML | BCU + MEF | 2026-05-01 | 2026-12-01 | 3 | --finance --notary`
- `ongoing | rental | Maldonado STR Receptive Operator registration — STR municipal regulation in flux 2026 | Intendencia de Maldonado | 2026-05-01 | 2026-08-01 | 2 | --rental`

### 🇨🇱 CL

- `2020 | tax | Sobretasa Ley 21.210 — 0.275–0.425% on aggregate property > UF 670; ongoing tramo adjustments via Ley 21.713 reform | SII + MinHacienda | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2022-2024 | risks | Código de Aguas reform — water rights modifications; mega-drought central+north intensifying | DGA + MinAgricultura | 2026-05-01 | 2026-10-01 | 2 | --risks --mains`
- `2023 | finance | Condominio Ley 21.442 — replaced Ley 19.537; new HOA framework | MinVivienda + Conservadores | 2026-05-01 | 2026-11-01 | 3 | --finance --notary`
- `2011 | risks | NCh 433 Mod DS 61/2011 — post-2010 Maule earthquake building-code revision raised seismic standards | MINVU | 2026-05-01 | 2027-01-01 | 1 | --risks`
- `ongoing | rental | STR comuna ordinances evolving — Las Condes / Providencia / Vitacura tightening 2024-2026 | Municipios | 2026-05-01 | 2026-08-01 | 2 | --rental`

### 🇿🇦 ZA

- `2025-01 | finance | Expropriation Act 13 of 2024 assented Jan 2025 — Constitutional challenges pending; theoretical risk for residential land but practical urban risk remains low | Constitutional Court + DALRRD | 2026-05-01 | 2026-09-01 | 1 | --finance --visa`
- `2024-08 | rental | Tourism Amendment Bill regulating Airbnb pending; municipal rules vary (Cape Town requires temporary land-use rights for STR in some zones) | Tourism Dept + municipalities | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2024-02-28 | tax | Solar PV individual rebate (up to R15,000) expired 28 Feb 2024 — verify if extended in 2026/27 Budget | SARS + Treasury | 2026-05-01 | 2026-08-01 | 3 | --tax --esg`
- `2025-26 | tax | SARS Transfer Duty Schedule 8 — exempt below R1.1M, progressive to 13% above R12M; verify exact brackets each tax year | SARS | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2024-2025 | risks | Eskom load-shedding declined via Operation Vulindlela + private generation; backup power still common in upper-middle market | Eskom + DMRE | 2026-05-01 | 2026-09-01 | 3 | --risks --finance`
- `2022-02 | finance | Property Practitioners Act 22/2019 (PPRA) replaced EAAB Feb 2022 — new agent regulation + FFC requirements | PPRA | 2026-05-01 | 2027-01-01 | 3 | --finance --notary`

### 🇬🇪 GE

- `2023-12 | visa | EU candidate status granted Dec 2023 — accession process active; longer-term policy alignment may shift property-tax regime + capital controls | European Council + GoG | 2026-05-01 | 2026-11-01 | 2 | --visa --tax --currency`
- `2025-XX | tax | Tbilisi Sakrebulo Decision 14-69 sets 2025 property-tax schedule (income-threshold gated above GEL 40k household income); annual revisions expected | Tbilisi City Hall + Revenue Service | 2026-05-01 | 2026-09-01 | 3 | --tax`
- `ongoing | rental | No national STR statute as of 2025 — Tbilisi/Batumi enforcement varies, monitor for Sakrebulo ordinances | City Halls + Revenue Service | 2026-05-01 | 2026-08-01 | 3 | --rental`
- `2024-XX | finance | NBG mortgage rate normalization post-EUR rate cycle; LTV caps tightened for non-resident foreign-currency loans | National Bank of Georgia | 2026-05-01 | 2026-09-01 | 3 | --finance`

### 🇮🇩 ID

- `2021-02 | foreign-buyer | PP No. 18/2021 expanded foreigner rights — Hak Pakai 30+20+30=80 yr direct ownership w/ KITAS/KITAP, SHMRS strata-title condos foreigner-owned | Ministry of ATR/BPN | 2026-05-01 | 2026-11-01 | 1 | --tax --visa` ownership
- `2023-2025 | foreign-buyer | Bali Provincial Court voided multiple nominee-structure transactions 2023-2025 (UUPA Art. 26(2) violations) — pre-2023 expat-forum advice now actively dangerous | Bali Provincial Court | 2026-05-01 | 2026-09-01 | 1 | --tax ownership`
- `2023-XX | visa | Permenkumham 22/2023 Second Home Visa — qualifying IDR 2B asset can BE the property itself (Hak Pakai/SHMRS) | Imigrasi | 2026-05-01 | 2026-10-01 | 2 | --visa`
- `2022-01 | tax | UU HKPD Law 1/2022 reformed local taxation — BPHTB statutory ceiling 5%, kabupaten can set within ceiling; verify per-kabupaten | Ministry of Finance + DJP | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `ongoing | rental | Bali villa STR enforcement varies by kabupaten — Pondok Wisata licensing patchy; monitor Provincial regulations | Bali Provincial Govt + Imigrasi | 2026-05-01 | 2026-09-01 | 3 | --rental`

### 🇲🇾 MY

- `2024-06 | visa | MM2H relaunched 2024 — 3 tiers Silver/Gold/Platinum (MYR 1M-5M FD + MYR 40-50k/mo income); replaced 2021 framework | MOTAC + Immigration | 2026-05-01 | 2026-10-01 | 1 | --visa`
- `2025-26 | tax | RPGT remains 10% permanent for foreigners even after 5+ yrs (citizens drop to 0% from 2022); permanent foreign-buyer disadvantage at exit | LHDN | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2024-XX | foreign-buyer | State EXCO foreign-buyer minimum thresholds revised periodically (KL 1M / Selangor 2M / Penang Island 1-3M etc.); verify per-state circular at offer date | State EXCO + Land Office | 2026-05-01 | 2026-09-01 | 2 | --tax ownership`
- `2020-XX | rental | Penang Island STR ban (2020) for non-tourism residential strata + KL/PJ Management Corporation by-laws increasingly prohibit Airbnb | State + MC by-laws | 2026-05-01 | 2026-09-01 | 2 | --rental`
- `ongoing | tax | Foreign-buyer flat 4% MOT stamp duty surcharge vs progressive citizen scale — for MYR 1.5M condo this is ~36% more (60k vs 44k) | LHDN Stamp Duty | 2026-05-01 | 2026-12-01 | 3 | --tax`

### 🇻🇳 VN

- `2025-08-01 | foreign-buyer | 2024 Land Law (31/2024/QH15) + 2023 Housing Law (27/2023/QH15) effective 1 Aug 2025 — confirms 50-yr foreign leasehold + 50-yr renewal, 30%/250 quotas, expanded mortgage to foreign-owned banks | National Assembly + MOC + MONRE | 2026-05-01 | 2026-09-01 | 1 | --tax --finance ownership`
- `2025-08-01 | tax | Annual provincial land-price tables under 2024 Land Law replaced 5-yr tables — non-agricultural land tax base will track market more closely | MONRE + provincial PCs | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2017-XX | tax | Recurring property tax PROPOSED multiple times since 2017 — NOT enacted as of 2026-05-01; monitor Ministry of Finance consultation | Ministry of Finance | 2026-05-01 | 2026-09-01 | 3 | --tax`
- `ongoing | visa | NO Vietnam Golden Visa via real estate exists — DT investment visa requires capital injection into a Vietnamese enterprise, not RE; common foreign-buyer assumption is wrong | Ministry of Public Security | 2026-05-01 | 2026-12-01 | 2 | --visa`
- `2025-XX | rental | District-level STR enforcement varies; HCMC Ward People's Committees increasingly require Pink Book + business license for Airbnb | Provincial PCs + MOCST | 2026-05-01 | 2026-09-01 | 3 | --rental`

### 🇵🇭 PH

- `2024-2027 | tax | RA 12001 Real Property Valuation Reform — rolling LGU revaluation 2024-2027 may significantly raise RPT bills as schedules close gap to FMV | DOF + LGUs | 2026-05-01 | 2026-09-01 | 1 | --tax`
- `2025-26 | tax | PH "CGT" 6% on GROSS sale price (or zonal/FMV whichever higher) per NIRC §24(D) — transaction tax in substance, not gain-based; even loss-making sales taxed | BIR | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `ongoing | foreign-buyer | 1987 Constitution Art. XII §7 + Anti-Dummy Law (CA 108) criminal grade 5-15 yrs imprisonment + property forfeiture for nominee structures | DOJ + Constitutional | 2026-05-01 | 2027-01-01 | 1 | --tax ownership`
- `ongoing | visa | SRRV (PRA) USD 10-50k deposit by age category; SIRV (BOI) USD 75k qualifying assets — both permit long-term residence + condo ownership | PRA + BOI | 2026-05-01 | 2026-12-01 | 2 | --visa`
- `2009-XX | foreign-buyer | Matthews v. Taylor (2009) Supreme Court ruling — foreigners cannot reclaim funds used to buy land titled to a Filipino spouse; Path 4 spouse-titled is buy-at-own-risk | Supreme Court | 2026-05-01 | 2027-01-01 | 1 | --tax ownership`

### 🇮🇱 IL

- `2025-01-01 | tax | VAT raised from 17% → 18% on 1 Jan 2025 — affects new-build pricing AND attorney/broker/appraiser fees; common stale-data trap | Tax Authority | 2026-05-01 | 2026-09-01 | 1 | --tax`
- `2022-10-01 | tax | TAMA 38 (national earthquake retrofit incentive) sunset 1 Oct 2022 — many sources still reference it as active; new retrofit goes through TAMA 70 + local outline plans | Israel Land Authority + municipalities | 2026-05-01 | 2026-12-01 | 2 | --tax --risks`
- `2023-2024 | risks | Israel-Hamas (Oct 2023→ongoing) + Israel-Hezbollah (Sep-Nov 2024 ceasefire) wars disrupted insurance markets; Karnit (state war-damage compensation) central | IDF + Karnit Fund | 2026-05-01 | 2026-08-01 | 1 | --risks --insurance`
- `ongoing | foreign-buyer | RMI/Israel Land Authority manages ~93% state-owned land (state ~70% + KKL/JNF ~12-13% + Development Authority ~10%); KKL/JNF land restricted to Jewish lessees by charter — litigation ongoing | RMI + KKL | 2026-05-01 | 2026-12-01 | 1 | --tax ownership`
- `2009-XX | tax | Heskem Hadash post-2009 reform allows lessees to convert leasehold (חכירה) to freehold (חופשי) for capitalization fee on built-up land in many areas | RMI | 2026-05-01 | 2027-01-01 | 2 | --tax ownership`
- `ongoing | tax | Olim 7-year incentivized purchase-tax scale (0.5% on first ILS 1.92M / 5% above) vs non-resident scale (8% on first ILS 6.05M / 10% above) — saves ~ILS 207k on ILS 4M flat est. | Tax Authority + Aliyah Ministry | 2026-05-01 | 2026-12-01 | 2 | --tax --visa`

### 🇲🇦 MA

- `2023-09 | risks | Al Haouz earthquake M 6.8 Sep 2023 — materially changes pre-2024 building-stock risk profile in Marrakech + High Atlas valleys; structural assessment essential through at least 2027 for any pre-2011 build | RMI + High Commission for Reconstruction | 2026-05-01 | 2026-09-01 | 1 | --risks --insurance`
- `2024-XX | risks | RPS 2024 (Règles Parasismiques) strengthened building code post-Al Haouz — NOT retroactive | Ministry of Housing + RPS | 2026-05-01 | 2026-12-01 | 2 | --risks`
- `2017-XX | tax | CGT (TPI) 20% on net gain — exempt if held >6 yrs primary residence / >10 yrs secondary post-2017 reform | DGI | 2026-05-01 | 2027-01-01 | 3 | --tax`
- `ongoing | foreign-buyer | Office des Changes registration at purchase via authorised bank is ONLY legal repatriation gateway — skip and sale proceeds + rental income cannot leave dirham zone (non-convertible currency) | Office des Changes | 2026-05-01 | 2026-12-01 | 1 | --tax --currency`
- `ongoing | foreign-buyer | Title status decision tree: titré (immatriculé under ANCFCC) ✅ foreigner-buyable; non-titré (melkia) requires réquisition d'immatriculation; habous (religious endowment) cannot be sold to non-Muslims; collectif (tribal) requires conversion | ANCFCC + Ministry of Habous | 2026-05-01 | 2027-01-01 | 1 | --tax ownership`
- `ongoing | rental | National STR regulation fragmented; enforcement uneven; no single national Airbnb register as of 2026-05 — verify per-prefecture | Ministry of Tourism + prefectures | 2026-05-01 | 2026-09-01 | 3 | --rental`

### 🇪🇬 EG

- `2024-03-06 | currency | EGP free-float Mar 2024 (after IMF EFF approval) — devaluation history ~15.7→30→50/USD by Mar 2024 → ~50-51/USD by 2026-05-01 (managed float); foreign buyers face structural FX volatility | CBE + IMF | 2026-05-01 | 2026-08-01 | 1 | --currency --tax`
- `2023-XX | visa | Investment Law 160/2023 RBI/CBI tiers — USD 250k cash deposit (5-yr) → PR / USD 300k RE → citizenship / USD 350k investment → citizenship; thresholds have shifted multiple times since 2023, verify with GAFI in writing before transferring funds | GAFI + Ministry of Investment | 2026-05-01 | 2026-09-01 | 1 | --visa --tax`
- `2023-XX | tax | Law 175/2023 — CGT 2.5% of GROSS sale price (not net gain); even loss-making sales taxed; materially distorts IRR modeling | ETA | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `1996-XX | foreign-buyer | Law 230/1996 — max 2 properties/foreigner, max 4,000 m² each, NOT in protected/military/Sinai/border zones, NOT within 5 km of Suez Canal, agricultural land Egyptian-only, 5-yr resale lock (waivable Cabinet) | Ministry of Justice + REPA | 2026-05-01 | 2027-01-01 | 1 | --tax ownership`
- `ongoing | foreign-buyer | Form 4 paper trail at purchase via CBE-authorized bank is GATING procedural risk — without it future USD repatriation of sale proceeds structurally blocked, sellers stuck with EGP-only exit (catastrophic given EGP devaluation history) | CBE | 2026-05-01 | 2026-09-01 | 1 | --tax --currency`
- `ongoing | foreign-buyer | Sinai is usufruct-only 50-yr leasehold from TDA despite many Sharm El Sheikh sales offices marketing units as "freehold" — buyers regularly misled; deal-killer-class misrepresentation | TDA + REPA | 2026-05-01 | 2026-12-01 | 1 | --tax ownership`

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

*Last full audit: 2026-05-01 (added 25 Tier-3/4/5 country sections: SG/HK/KR/TW/LI/MO/AD/MC/MD + QA/SA/PE/EC/PY/AM/AZ/TN + IN/NG/KE/JO/OM/BH/KW/LB — total 87 countries tracked). Next mandatory full audit: 2026-07-26 (quarterly).*
