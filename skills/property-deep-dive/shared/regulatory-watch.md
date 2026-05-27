# Regulatory Watch — Cross-Country Reform Tracker

A single date-stamped registry of property-relevant reforms, transposition deadlines, ENDED programs, and watchlist items. Maintained as the **single source of truth for "what changed when"** — playbooks reference this; this references playbooks.

**Why it exists**: At 109 countries × 39 sections, the highest-blast-radius hallucination is asserting that an ENDED program is still active or quoting a tax rate that was reformed last quarter. This file makes "did anything change?" a single-file lookup before any re-stamp.

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

- `2024-11-19 | rental | Loi Le Meur — short-let (meublé tourisme) tightened: classement obligation expanded, communes may reduce primary-residence cap | LégiFrance | 2026-04-26 | 2026-10-01 | 2 | --rental --tax`
- `2024-11-19 | rental | Loi Le Meur primary-residence default cap reduced 120 → 90 nights/yr nationwide; civil fine €15,000; national STR registration mandatory by 20 May 2026; co-ownership prohibition threshold lowered from unanimity to 2/3 majority where bourgeois habitation clause exists | LégiFrance | 2026-05-11 | 2026-08-20 | 1 | --rental`
- `2026-01-01 | rental | Paris taxe de séjour 2026 — 5% pre-tax/n/pp capped €15.93 for unclassified furnished tourist accommodation + 200% Île-de-France regional surcharge; Q1 2026 enforcement ~€1M fines, 150-person brigade, record €585k fine 9e arrondissement SCI | Paris.fr + Service Public | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-01-01 | esg | DPE G banned for rental on new contracts | LégiFrance | 2026-04-26 | 2027-01-01 | 1 | --rental --esg`
- `2028-01-01 (pending) | esg | DPE F to be banned for rental | LégiFrance | 2026-04-26 | 2027-06-01 | 2 | --rental --esg`
- `2034-01-01 (pending) | esg | DPE E to be banned for rental | LégiFrance | 2026-04-26 | 2028-01-01 | 3 | --rental --esg`
- `2026-2028 (in flight) | tax | RVLLH cadastral revaluation rolling — +20-40% TFPB rural expected | DGFiP | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇮🇹 IT

- `2026-01-01 | rental | Cedolare secca limit dropped from 5 → 2 properties (above which standard IRPEF) | Legge di Bilancio 2026 | 2026-04-26 | 2026-09-01 | 2 | --rental --tax`
- `2025-01-01 | rental | National CIN (Codice Identificativo Nazionale) mandatory display from 1 Jan 2025 (portal opened 1 Sep 2024); fines €800-€8,000 no CIN + €500-€5,000 non-display | Ministero del Turismo | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2023-10-XX → OVERTURNED | rental | Florence centro storico new-STR ban (Sindaco Nardella Oct 2023 town-planning variant decree) was OVERTURNED by TAR Toscana — lapsed because not confirmed in new operational plan; appeals dismissed. NO REPLACEMENT ORDINANCE IN FORCE at 2026-05-11; new municipal administration signalling re-pursuit | TAR Toscana + Il Sole 24 Ore | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2026-XX-XX | rental | Milan 2026 Winter Olympics tourist tax spike — €9.50/n for accommodation within 30km of Olympic venues, 2026 only (vs €6.30/n standard); 14-night cap | Comune di Milano | 2026-05-11 | 2026-11-01 | 3 | --rental`
- `2024-XX-XX | rental | Venice Contributo di Accesso €5 day-tripper access fee (€10 if within 3 days), 2026 dates 3 Apr–26 Jul on Fri-Sun + special weeks; hotel guests/residents/workers/students exempt | Comune di Venezia | 2026-05-11 | 2026-09-01 | 3 | --rental`
- `2024-01-01 | tax | Southern Italy 7% pensioner regime — re-confirmed annually; expires after 9 yrs of residency | Agenzia delle Entrate | 2026-04-26 | 2027-01-15 | 2 | --tax (pension regime)`

### 🇪🇸 ES

- `2025-04-03 | visa | Golden Visa programme abolished | Ley 1/2025 | 2026-04-26 | 2026-10-01 | 1 | --visa`
- `2025-06-XX | tax | Cataluña ITP made progressive (replacing flat 10%) — top bracket 13% for >€1.5M | Generalitat de Catalunya | 2026-04-26 | 2026-10-01 | 2 | --tax`
- `2024-06-01 | rental | Madrid + Barcelona STR licensing freeze (de facto) | Municipal ordinances | 2026-04-26 | 2026-09-01 | 2 | --rental`
- `2024-06-XX | rental | BCN universal HUT expiry — ALL 10,101 HUT licences citywide expire Oct 2028 (Collboni decree Jun 2024); PEUAT Zone 1 Ciutat Vella + Eixample-stress remain frozen for new HUTs; Zone 2 transferable-only; Zone 4 prohibited | Ajuntament de Barcelona | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-05-01 | rental | Catalonia IEET tourist tax — €7.40/n 1-4★ apartments / €11/n 5★ + Catalonia €4 municipal surcharge rising €1/yr to max €8 by 2029; cap 7 nights; under-16 exempt | Generalitat de Catalunya ATC | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `2018-XX-XX | rental | Madrid PEH Distrito Centro — STR >90 nights/yr classed as commercial use; independent entrance + portal/lift separation from residents required (de-facto STR ban in shared-building residential) | Ayuntamiento de Madrid | 2026-05-11 | 2026-09-01 | 2 | --rental`

### 🇵🇹 PT

- `2024-03-22 | tax | NHR replaced by IFICI/NHR 2.0 — **pensions NO LONGER exempt** (only specified scientific/innovation activities) | Decreto-Lei 21-A/2024 | 2026-04-26 | 2026-10-01 | 1 | --visa --tax (pension)`
- `2023-10-06 | visa | Golden Visa — residential real estate route closed; funds/research routes remain | Mais Habitação law | 2026-04-26 | 2026-09-01 | 1 | --visa`
- `2024-11-01 | rental | Decree-Law 76/2024 in force 1 Nov 2024 — repealed Mais Habitação AL nationwide freeze and 5-yr renewal requirement; max 27 guests/9 rooms per AL unit (down from 30); municipalities retain "áreas de contenção" power | gov.pt + Diário da República | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2024-09-XX | rental | Lisbon Áreas de Contenção Absoluta — Santa Maria Maior (68.8% AL ratio), Bairro Alto, Madragoa: no new AL registrations; SALE-TRIGGERED EXPIRY — selling apartment-mode AL in containment zone = automatic licence death, NON-TRANSFERABLE to buyer | Câmara Municipal de Lisboa | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2024-09-XX | rental | Lisbon Áreas de Contenção Relativa — Misericórdia, Príncipe Real, Graça, Bica (2.5-5% AL ratio): one-for-one transfer only | Câmara Municipal de Lisboa | 2026-05-11 | 2026-08-01 | 2 | --rental`
- `2024-09-XX | rental | Lisbon TMT raised to €4/pp/n (from €2 Sept 2024), cap 7 nights, ≥13 years old | Câmara Municipal de Lisboa | 2026-05-11 | 2026-09-01 | 3 | --rental`
- `2024-12-XX | rental | Porto Áreas de Contenção — Vitória (60.5% pressure), São Nicolau (48.3%), Sé (44.1%), Santo Ildefonso (38.3%), Miragaia (21.8%): containment freeze; Cedofeita (9.8%) reclassified as sustainable-growth (new AL permitted) | Câmara Municipal do Porto | 2026-05-11 | 2026-09-01 | 1 | --rental`

### 🇮🇸 IS

- `2024-XX-XX | rental | STR cap of 90 nights/yr without licence remains; tightened enforcement post-Reykjanes eruptions | Sýslumaður | 2026-04-26 | 2026-10-01 | 3 | --rental`

### 🇸🇪 SE / 🇫🇮 FI / 🇳🇴 NO

- `2024-01-01 | tax | FI varainsiirtovero (transfer tax) reduced 4% → 3% (real estate) and 2% → 1.5% (housing co-op shares) | Vero.fi | 2026-04-26 | 2026-09-01 | 2 | --tax (FI)`

### 🇬🇧 UK

- `2025-04-06 | tax | Non-dom regime abolished, replaced by 4-yr FIG (Foreign Income & Gains) regime | HMRC | 2026-04-26 | 2026-09-01 | 2 | --tax --visa`
- `2025-04-01 | tax | SDLT additional dwelling supplement increased 3% → 5% | HMRC | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇯🇪 JE

- `2024-08-01 | rental | Rented Dwellings Licensing Law 2023 mandatory enforcement begins | gov.je | 2026-05-27 | 2026-11-01 | 2 | --rental --notary (JE)`
- `2026-01-01 | tax | Mandatory independent taxation for all married couples including HVRs (Comptroller of Revenue HVR page explicit) | gov.je/taxesmoney | 2026-05-27 | 2026-09-01 | 2 | --tax --home-tax (JE)`
- `2026-XX-XX (PENDING — P.93/2025) | tax | 2026 Budget: one-year reduction in higher-rate Stamp Duty/LTT/EPTT surcharge +3pp → +2pp; reverts +3pp from 2027 | States Assembly | 2026-05-27 | 2026-08-01 | 2 | --tax --finance (JE)`
- `pending (P.19/2026) | visa | HVR (2(1)(e)) statutory cap proposed — 15/yr or 75 per 5-yr period (legislative proposal) | States Assembly | 2026-05-27 | 2026-08-01 | 1 | --visa --foreign-buyer (JE)`
- `2025-XX-XX (phased) | tax | Mortgage interest relief phased out post-2025 | Comptroller of Revenue | 2026-05-27 | 2026-09-01 | 3 | --tax --finance (JE)`

### 🇬🇬 GG

- `2024-11-08 | tax | Document Duty 2024 reform — post-8 Nov 2024 bands 2.25%→7% (2.5M-5M = 5.50%; 5M+ = 7%) + 2% non-PPR surcharge effective 2 Nov 2022 | parliament.gg 2026-16 | 2026-05-27 | 2026-09-01 | 2 | --tax --finance (GG)`
- `2026-XX-XX | tax | Standard Charge rises £40k (2024 baseline) → £50k from year-of-charge 2026 (P.2025-121 proposition 2) | parliament.gg | 2026-05-27 | 2026-09-01 | 2 | --tax --home-tax (GG)`
- `2025-01-01 | tax | Alderney Property Tax Cap: legacy £65k (2024 only, withdrawn end-2025) → new £60k from 1 Jan 2025 with £50k trigger | gov.gg | 2026-05-27 | 2026-09-01 | 2 | --tax --foreign-buyer (GG-Alderney)`
- `2025-01-01 | tax | TRP 5× derelict surcharge + 3.2% 2025 uplift; 2026 tariffs published (parliament.gg id=196847) | gov.gg | 2026-05-27 | 2026-10-01 | 3 | --tax (GG)`
- `2016-XX-XX (active) | visa | Population Management (Guernsey) Law 2016 — 8yrs Established Resident → 14yrs Permanent Resident ladder (10-of-20 retention rule) | gov.gg | 2026-05-27 | 2026-12-01 | 2 | --visa --foreign-buyer (GG)`

### 🇮🇲 IM

- `2023-05-01 | tax | Land, Deeds & Probate Registries Fees & Duties Order 2023 (SD 2023/0077) — tiered Land Registry duty: Owner-Occupier 0/1/2%, Resident Non-Owner 2/2.5%, Non-Resident 4/4.5% (single biggest practical buyer-cost item) | tribunals.gov.im | 2026-05-27 | 2026-11-01 | 2 | --tax --notary (IM)`
- `2025-04-11 | tax | FERSA (UK-IM customs/VAT revenue-sharing) re-signed; supersedes 2020 agreement; IoM share YE Mar 2025 = £439.2M (86.51% VAT / 13.49% other duties) | treasury.gov.im | 2026-05-27 | 2026-10-01 | 2 | --tax --finance (IM)`

### 🇬🇮 GI

- `2024-12-23 | tax | Stamp Duties (Amendment) Act No. 37 of 2024 effective 23 Dec 2024 (FTB threshold £300k since 11 Jul 2023; Affordable Housing 7.5% on resale-within-10yr; mortgage stamp duty 0.13% / 0.20%) | Gibraltar Income Tax Office | 2026-05-27 | 2026-09-01 | 2 | --tax --finance (GI)`
- `2026-07-15 (PROVISIONAL) | visa | EU-UK Frontier Treaty provisional application — does NOT override Gibraltar immigration; Gibraltar press 148/2026 explicit | Consilium press release 01 Apr 2026 | 2026-05-27 | 2026-08-01 | 1 | --visa --foreign-buyer --remote (GI)`
- `pending | visa | Cat-2 reform expected (community signal r/gibraltar 1tkeoa5, no primary date) — tier-4 anecdotal, revisit Q3 2026 | r/gibraltar 1tkeoa5 | 2026-05-27 | 2026-10-01 | 4 | --visa (GI)`

### 🇨🇭 CH

- `2028-01-01 (pending) | tax | Eigenmietwert (imputed rental value tax) abolition — referendum approved Sep 2025; phased | Federal Council | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇩🇪 DE

- `2025-01-01 | tax | Grundsteuer reform — new property values applied (regional models: Bundesmodell vs Bayern/Baden-W. variants) | BFH | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇦🇹 AT

- `2024-XX-XX | tax | Tirol/Salzburg/Vorarlberg foreign-buyer quotas tightened (annual review) | Land governments | 2026-04-26 | 2026-09-01 | 2 | --tax (ownership)`

### 🇳🇱 NL

- `2025-01-01 | rental | Affordable Rent Act (Wet betaalbare huur) — points-based cap extended to mid-segment; affects rental yield | Rijksoverheid | 2026-04-26 | 2026-09-01 | 1 | --rental`
- `2026-04-01 | rental | Amsterdam vakantieverhuur 30-night → 15-night cap in 8 stress neighborhoods (7 Centrum stadsdelen + Oude Pijp in Zuid) from 1 Apr 2026; city council final vote Dec 2025; permit €73.30 + 12.5% per-room tourist tax (vs ~€22/n on €176 avg) | Gemeente Amsterdam | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2026-01-01 | tax | Box 3 reform — actual return basis (replacing notional yield) | Belastingdienst | 2026-04-26 | 2026-07-01 | 1 | --tax`

### 🇧🇪 BE

- `2024-XX-XX | tax | Flanders registratierechten — 3% main residence, 12% other; refinements quarterly | Vlaamse Belastingdienst | 2026-04-26 | 2026-10-01 | 3 | --tax`

### 🇩🇰 DK

- `2024-01-01 | tax | New ejendomsskat (property value tax) regime live — based on 2020-vintage public valuations | Vurderingsstyrelsen | 2026-04-26 | 2026-10-01 | 2 | --tax`

### 🇫🇴 FO

- `2021-12-XX | ownership | Løgtingslóg on real-estate purchase passed by Løgting December 2021 — permit-free for FO residents, ex-residents (5+ yrs), DK citizens 5+ yrs in Kingdom, FO-HQ companies; all other foreigners incl. EU/EEA + non-DK Nordic need government permit (verify exact passing date at logir.fo) | local.fo / Justismálið | 2026-05-27 | 2026-11-01 | 1 | --foreign-buyer --notary (FO)`
- `1948-03-23 (foundational) | ownership | Faroe Islands NOT in EU (Hjemmestyret since 1948; explicit OECD + state.gov re-affirmation) — no EU free-movement override for property acquisition or tax | OECD / state.gov | 2026-05-27 | 2026-12-01 | 2 | --foreign-buyer --tax --visa (FO)`

### 🇬🇱 GL

- `2026-01-01 | ownership | Inatsisartutlov nr. 78 af 21. november 2025 om erhvervelse af adkomst eller brugsret til fast ejendom — eff. 1 Jan 2026 (§ 15 transition); 6 eligibility classes §§ 3-8: Danish citizens, foreign nationals (2-yr residence + 2-yr tax residency), regulated financial institutions, 100%-locally-owned capital companies, licensed sectoral operators, GL associations; § 9 dispensation channel (box909@nanoq.gl) | nalunaarutit.gl | 2026-05-27 | 2026-09-01 | 1 | --foreign-buyer --notary --remote (GL)`
- `2026-XX-XX (pending) | rental | Inatsisartutlov om leje af boliger (Greenland-specific rental law, NOT Danish Lejeloven) — 2026 reform in public consultation; Boligklagenævnet disputes | Naalakkersuisut høring portal | 2026-05-27 | 2026-09-01 | 3 | --rental (GL)`
- `2010-XX-XX (foundational) | ownership | NO PRIVATE LAND OWNERSHIP in Greenland (govmin.gl Mineral Resources Authority verbatim: "all rights to any use of land is administered by the Government of Greenland"); buyers acquire BUILDING title + arealtildeling (brugsret) only — fundamentally different from any other ISO entry | govmin.gl / Mineral Resources Act 2010 | 2026-05-27 | 2027-01-01 | 4 | --foreign-buyer --notary (GL)`

### 🇨🇿 CZ

- `2024-01-01 | tax | DPH (VAT) reduced rates consolidated 12% / 21%; building-supply VAT changes | Finanční správa | 2026-04-26 | 2026-09-01 | 3 | --tax`

### 🇸🇰 SK

- `2025-01-01 | tax | DPH (VAT) raised 20% → 23% standard; reduced rates restructured | Finančná správa | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇸🇮 SI

- `2026-01-01 (in flight) | tax | Davek na nepremičnine (annual property tax) reform — replacing NUSZ; phased | MF SI | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇦🇱 AL

- `2026-01-01 | tax | One-time property revaluation window — Law 85/2025 "Për rivlerësimin e pasurisë së paluajtshme"; 1 Jan 2026 – 31 Dec 2026; 5% on uplift between previous registered value and market value (newly built residential per Finance Min. Malaj clarification); material for sellers carrying low historical basis | HLB Albania + Albanian Daily News + Balkanweb + RTSH | 2026-05-27 | 2026-12-31 | 2 | --tax --exit --finance`
- `2025-11-17 | macro | EU accession sprint — all 33 chapters opened by 17 Nov 2025 (Clusters 1-6 in 13 months); IBAR adopted by COELA 21 May 2026; target conclusion 2027 + membership 2030 (Commission estimate ~2029) | Consilium + European Western Balkans + Balkan Insight | 2026-05-27 | 2026-09-01 | 1 | --macro --finance --price`
- `2026 (delayed) | macro | Vlora International Airport — PM Rama Dec 2025 statement pushed commissioning to mid-2026; certification pending, no summer-2026 flights scheduled, 2A Group shareholder dispute, extension request to September 2026 | SeeNews + Albanian Daily News + CAPA + Two Continents | 2026-05-27 | 2026-09-01 | 3 | --price --traffic`
- `2024-XX-XX | tax | PIT progressive brackets (Law 29/2023) — 0% up to ALL 600k; 13% ALL 600k-3M; 23% above; flat-rate carve-outs (rental 15%, CGT 15%, dividends 8%) | tatime.gov.al + PwC | 2026-05-27 | 2026-12-01 | 2 | --tax`
- `ongoing | foreign-buyer | Ligji 7980/1995 "Për shitblerjen e trojeve" — apartments OK; agricultural land prohibited (workaround Albanian Sh.p.k. company); construction land 3× rule; 200m coastal buffer | Investropa + Vivaview + Alba Legal | 2026-05-27 | 2027-01-01 | 1 | --visa --tax`
- `2026-12-31 | visa | Strategic Investor Status (Statusi i Investitorit Strategjik) — Law on Strategic Investments 2015 (amended Jan 2025); ≥€5M tourism + 80 jobs; €1 state-land for up to 99 yrs; AIDA fast-track; deadline 31 Dec 2026 | Oracle Law Global + UNCTAD Investment Laws Navigator + US State 2025 ICS | 2026-05-27 | 2026-09-01 | 2 | --visa --tax`
- `2025-11-01 | rental | Booking.com Albania VAT/NIPT rule — from 1 Nov 2025 hosts must declare NIPT or pay 20% VAT on platform commission; pre-DIVA pressure driving hosts onto NIPT or off Booking | Tiranapost + HLB Albania | 2026-05-27 | 2026-09-01 | 2 | --rental`
- `2026-03-11 | rental | Council of Ministers Decision 153/2026 — accommodation-structure certification conditions for tourism beach stations | AlProfit Consult | 2026-05-27 | 2026-09-01 | 3 | --rental`
- `2026-2030 | tax | Property-tax reform phased timeline — end-2026 fiscal cadastre integration; 2026-2027 transition; 2027 nationwide property assessment; 2028 market-based valuations + new rates; 2030 land-tax rollout; target lift property tax 0.3% → 1% of GDP by 2028 | Albanian Times + ALTAX + HLB | 2026-05-27 | 2027-01-01 | 2 | --tax`

### 🇭🇷 HR

- `2023-01-01 | currency | Eurozone accession (HRK → EUR) | ECB | 2026-04-26 | 2027-01-01 | 1 | --currency --tax`
- `2025-01-01 | tax | Porez na nekretnine — annual property tax on second/empty homes implemented | Porezna uprava | 2026-04-26 | 2026-09-01 | 2 | --tax`
- `ongoing | ownership | 10-yr lock on agricultural land for non-EU buyers | MPGI | 2026-04-26 | 2027-01-01 | 2 | --tax (ownership)`

### 🇬🇷 GR

- `ongoing | tax | 7% flat on foreign-source income for foreign pensioners — 15-yr regime, application open | AADE | 2026-04-26 | 2026-12-01 | 2 | --tax (pension regime)`
- `2024-XX-XX | rental | STR registration tightening; AADE Property Number mandatory | AADE | 2026-04-26 | 2026-09-01 | 3 | --rental`
- `2025-01-01 | rental | Climate Resilience Levy raised 1 Jan 2025 — STR €8/n high season (Apr-Oct) / €2 low season; villas €8 (<80m²) or €15 (≥80m²) high / €2 / €4 low; per room/unit/night not per person | AADE | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-01-01 | rental | Athens 1st/2nd/3rd Municipal Districts AMA freeze — no new STR initial registrations 1 Jan 2025–31 Dec 2025; EXTENDED through 2026 by ministerial decision; re-registration of pre-2024-12-31 properties allowed under conditions; ~8% AMA drop (29,500 → 27,000 central area) | AADE + Ministry of Tourism | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2025-10-01 | rental | National STR standards (safety, fire, civil liability) in force 1 Oct 2025 under Law 4276/2014 + Art. 111 Law 4446/2016 + 2025 amendments | AADE | 2026-05-11 | 2026-08-01 | 2 | --rental`
- `2026-04 (proposed, decision due 30 Jun 2026) | rental | Cyclades 20-30% tourist-bed reduction proposal — Tourism Min. Kefalogianni announcement 6-7 Apr 2026; STR freeze Mykonos drafted; under public consultation | Ministry of Tourism | 2026-05-11 | 2026-07-01 | 1 | --rental`

### 🇭🇺 HU

- `2026-01-01 | rental | Budapest District VI (Terézváros) STR zero-day cap — Decree 26/2024 (X.31), referendum 2-15 Sep 2024 (20.52% turnout, 54% in favor), upheld by Hungarian Supreme Court; STR allowable days/yr = ZERO in force 1 Jan 2026 | Terézváros + hungarytoday.hu | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2025-09-XX | rental | Budapest District VII (Erzsébetváros — "party quarter" / Jewish Quarter) — caps new commercial accommodations at 10% of any residential building's floor area (different mechanism from VI); national 2-year moratorium on new STR registrations announced 2025 | Budapest VII district | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2024-01-01 | rental | Airbnb flat tax per room quadrupled in 2024 (~+290%) | NAV | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`

### 🇪🇪 EE

- `2024-01-01 | tax | Land tax indexation cap raised 10% → 50% annual change | Maksu- ja Tolliamet | 2026-04-26 | 2026-10-01 | 3 | --tax`
- `2025-01-01 | tax | Income tax 20% → 22% (touches rental income) | Maksu- ja Tolliamet | 2026-04-26 | 2026-09-01 | 2 | --tax --rental`
- `2025-07-XX | rental | Mandatory STR registration from Jul 2025 (EU Reg 2024/1028 alignment); unique listing ID required; guest registration to Police & Border Guard within 24h; Tallinn Vanalinn (Old Town) STR cap announced (mechanism not finalized at 2026-05) | Maksu- ja Tolliamet + Tallinn | 2026-05-11 | 2026-08-01 | 2 | --rental`

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

### 🇲🇨 MC

- `2024-XX-XX | visa | Monaco citizen portal renamed `service-public-particuliers.gouv.mc` → `monservicepublic.gouv.mc`; all sub-domain content (residence applications, Étrangers/Vivre-en-Principauté/Conditions-de-residence flows, online forms) migrated; 301 redirects confirmed via WebFetch but the deep-link tree restructured — verify current path before citing | Gouvernement Monaco | 2026-05-27 | 2027-12-31 | 4 | --visa --relocation (MC)`

### 🇨🇾 CY

- `2026-01-01 | tax | Comprehensive Tax Reform — CGT principal-residence exemption €17,086 → €30,000; agricultural €25,629 → €50,000; other €17,086 → €150,000; SDC on rental abolished | Ministry of Finance | 2026-04-26 | 2026-09-01 | 1 | --tax --rental`
- `2025-XX-XX | ownership | Trapped Buyers Amendment Law 110(I)/2025 — title-deed transfer protections strengthened | DLS | 2026-04-26 | 2026-10-01 | 2 | --tax (ownership)`

### 🇲🇹 MT

- `2025-04-29 | visa | MEIN (Investor Citizenship) ENDED by ECJ Case C-181/23 | ECJ + Identità | 2026-04-26 | 2026-10-01 | 1 | --visa`
- `2025-2035 | cadastre | LRA reform target — full compulsory registration phase-in | Land Registration Agency | 2026-04-26 | 2027-01-01 | 3 | --tax (cadastre) --mains`

### 🇧🇭 BH

- `2024-05-01 | rental | Tourist Levy BHD 3 per room per day on hotel accommodation, effective 1 May 2024 (supersedes prior BD 0.5/n) | KPMG Bahrain GCC Tax News May 2024 + BTEA | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`

### 🇨🇦 CA

- `2027-01-01 (pending end) | ownership | Foreign-buyer Prohibition Act extended through 1 Jan 2027 | CMHC | 2026-04-26 | 2026-10-01 | 1 | --tax (ownership)`

### 🇦🇺 AU

- `2025-04-01 → 2027-03-31 | ownership | Established-homes ban on foreign purchase | FIRB | 2026-04-26 | 2026-10-01 | 1 | --tax (ownership)`
- `2024-07-31 | visa | SIV (Significant Investor Visa) closed | Home Affairs | 2026-04-26 | 2026-09-01 | 1 | --visa`
- `2025-01-01 | rental | VIC Short Stay Levy 7.5% on total booking fee for stays <28 days; principal-residence + hotels exempt; 25% of revenue to regional VIC for social/affordable housing | State Revenue Office VIC | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `ongoing | rental | NSW STRA Code of Conduct — STRA Register $65; Greater Sydney 180-day non-hosted cap (Eastern Harbour / Central River / Western Parkland districts); fines up to $1.1M (corp) / $220k (individual) | NSW Planning + Fair Trading | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2024-09-23 | rental | NSW Byron Shire 60-day non-hosted cap (most LGA); 365-day mapped precincts only in Byron Bay Town Centre + Brunswick Heads carve-outs; hosted STRA unaffected (365 days) | NSW Planning | 2026-05-11 | 2026-08-01 | 1 | --rental`

### 🇳🇿 NZ

- `2018-10-22 | ownership | Overseas Investment Amendment Act — permanent ban on foreign purchase of existing residential | LINZ | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`
- `2024-07-01 | tax | Bright-line test reduced 10 yr → 2 yr | IRD | 2026-04-26 | 2026-10-01 | 2 | --tax`
- `2024-04-01 | rental | Marketplace GST 15% collected by Airbnb / Bachcare on behalf of all hosts (even <NZD 60k/yr); 8.5% flat-rate credit for non-GST-registered hosts | IRD | 2026-05-11 | 2026-09-01 | 1 | --rental --tax`
- `ongoing | rental | Auckland APTR (Accommodation Provider Targeted Rate) — STR >28 nights/yr triggers commercial-rated uplift; Supreme Court validated 2022; declaration deadline 3 Jul annual | Auckland Council | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`
- `ongoing | rental | Queenstown Lakes District 90 nights/yr whole-house cap without resource consent + 25% rates uplift on registered properties | QLDC | 2026-05-11 | 2026-09-01 | 1 | --rental`

### 🇲🇽 MX

- `ongoing | ownership | Fideicomiso (bank trust) required within 50 km coast / 100 km border for foreign buyers | SRE | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`
- `2024-04-04 | rental | CDMX Tourism Law Reform published Gaceta Oficial 4 Apr 2024 (NOT 2022 as some references cite); implementing Reglamento 25 Sep 2024 + further reforms 3 Oct 2024; 50% ANNUAL OCCUPANCY CAP on STR units registered via digital platforms (loss of registration if exceeded); host + platform registries mandatory; social-housing + post-2017 quake reconstruction prohibited from STR | Congreso CDMX + Gaceta Oficial | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2025-XX-XX | rental | Q-Roo ISH 5% traditional + 6% via digital platforms (eff 2025) + VISITAX $5 USD/visitor one-time | Congreso Q-Roo | 2026-05-11 | 2026-09-01 | 2 | --rental`

### 🇧🇷 BR

- `2026-XX-XX (in flight) | cadastre | CIB (national cadastral identifier) rolling out — replacing fragmented Cartórios | Ministério da Fazenda + Receita | 2026-04-26 | 2026-09-01 | 3 | --tax (cadastre)`
- `2024-XX-XX | tax | Tributary Reform Constitutional Amendment 132/2023 — IBS/CBS replacing PIS/Cofins/ICMS/ISS, transition through 2033 | Receita Federal | 2026-04-26 | 2026-10-01 | 1 | --tax`

### 🇦🇷 AR

- `2024-XX-XX | tax | Bienes Personales — decreasing schedule 1.10% / 1.00% / 0.50% (Ley 27.743 consolidation) | AFIP | 2026-04-26 | 2026-09-01 | 2 | --tax`

### 🇨🇷 CR / 🇵🇦 PA

- `ongoing | tax | Both territorial-ish for non-resident foreign-source; PA Pensionado $1,000/mo lifetime requirement | DGI CR / DGI PA | 2026-04-26 | 2027-01-01 | 2 | --tax (pension regime)`

### 🇲🇪 ME

- `2024-01-01 | tax | RETT made progressive 3% / 5% / 6% (replacing flat 3%) | MFA ME | 2026-04-26 | 2026-10-01 | 1 | --tax`
- `2025-01-01 | tax | VAT restructure — new 15% reduced bracket added (hotels/restaurants/books); 21% standard unchanged; 7% essentials-only; 0% export | KPMG ME Tax Alert Oct 2024 + Eurofast Tax Card 2025 | 2026-05-27 | 2026-09-01 | 2 | --tax --rental`
- `2024-10-01 | tax | Europe Now 2 — employee pension-and-disability contribution 15% → 10%; employer pension-and-disability contribution eliminated (was 5.5%); minimum wage €600 (low-qualification) / €800 (high-qualification) | China-CEE Institute briefing + Government of Montenegro | 2026-05-27 | 2026-09-01 | 2 | --rental --work`
- `2026-01-17 | visa | Investor residency — amendments to Zakon o strancima (adopted Parliament 31 Dec 2025); €150k minimum property; 1-yr renewable temp → permanent after 5 yrs → citizenship after 10 yrs (verify path against consolidated Zakon o strancima + Zakon o crnogorskom državljanstvu); pre-2026 property-based residents grandfathered | IMI Daily + Monte.business | 2026-05-27 | 2026-08-01 | 1 | --visa`

### 🇲🇰 MK

- `ongoing | tax | CGT 10% (NOT 15% — common error) with 5-yr OR 3yr+1yr-resident exemption; effective rate 9% of realised gain (90% tax base) | UJP + PwC | 2026-05-27 | 2026-10-01 | 1 | --tax`
- `2025-12-XX | tax | 5% VAT first-sale residential extended to 31 December 2028 (was sunsetting 31 Dec 2025); applies within 5 yrs of construction; mixed-use proportional | Parliament amendment to Zakon za DDV + KPMG TaxNewsFlash Jan 2026 + VATupdate 27 Dec 2025 | 2026-05-27 | 2026-09-01 | 2 | --tax`
- `ongoing | tax | Danok na promet (transfer tax) statutorily owed by SELLER per finance.gov.mk — buyer-pays clause must be EXPLICIT in the dogovor or seller pays; default-silent contracts can swing 2–4% (~€2–4k on €100k flat) | finance.gov.mk | 2026-05-27 | 2026-09-01 | 2 | --tax`

### 🇧🇦 BA

- `ongoing | cadastre | Dual-entity (FBiH / RS-entity / Brčko) — different cadastres + tax regimes | Entity-level authorities | 2026-04-26 | 2027-01-01 | 1 | --tax --mains`
- `2024-10-22 | tax | BiH state-level VAT refund for first new-residential — passed by Predstavnički dom 22 Oct 2024; covers FBiH + RS + Brčko (NOT FBiH-only); 40 m² buyer + 15 m² per household member at 17%; upper-house (Dom naroda) ratification + UINO implementing rulebook still pending as of 2026-05 | KPMG TaxNewsFlash + VATupdate + UINO | 2026-05-27 | 2026-09-01 | 1 | --tax`
- `ongoing | foreign-buyer | Statutory reciprocity regime under Zakon o stvarnim pravima FBiH (Sl. novine FBiH 66/13, 100/13) — FBiH MoJ publishes annual no-reciprocity list by 31 Jan; arable land + protected areas barred regardless of reciprocity; d.o.o. workaround available; inheritance excepted | FBiH MoJ + DLA Piper REALWORLD + Multilaw + Prnjavorac | 2026-05-27 | 2027-01-31 | 1 | --visa --tax`
- `ongoing | tax | PIT flat by entity: FBiH 10% / RS 8% / Brčko 10% (NOT progressive) — personal allowances materially higher in RS + Brčko | PwC BA Individual taxes (last reviewed 19 Feb 2026) | 2026-05-27 | 2026-12-01 | 2 | --tax`

### 🇷🇸 RS

- `2014-05 | risks | Sava + Bosna river floods (NOT Drava — common error; Drava is HR/SI) | RHMZ | 2026-04-26 | 2027-01-01 | 4 | --risks`
- `2025-10-24 | permits | Zakon o posebnim uslovima za evidentiranje i upis prava na nepokretnostima — one-time legalizacija framework (~2M unpermitted buildings); filing window 8 Dec 2025 + ~60 days; certifikat from Agencija za prostorno planiranje → RGZ priority registration; cost €100–€1,000; post-24-Oct-2025 illegal construction NOT eligible | CT Legal + Lexology + VMT Attorneys + Tasić & Partners | 2026-05-27 | 2026-09-01 | 2 | --permits --risks`
- `2023-11-04 | cadastre | RGZ filings exclusively electronic via professional users (attorneys + licensed geodetic organisations); direct walk-in no longer possible | law-firm.rs + RGZ | 2026-05-27 | 2027-01-01 | 3 | --notary`
- `ongoing | tax | PIT — employment 10% flat + annual top-up 10%/15% above RSD 9,749,016 (2025); other categories 10–20%; capital gains 15%; first-apartment transfer-tax exemption 40 m² + 15 m² per family member | KPMG RS Feb 2026 + PwC Tax Summaries | 2026-05-27 | 2026-12-01 | 2 | --tax`

### 🇺🇸 US

- `2025-07-04 | tax | OBBBA (PL 119-21) reset SALT cap to $40k (sunset 2030); MID $750k cap permanent; §§ 25C/25D Energy Credits TERMINATED 31 Dec 2025; NRA estate exempt $15M (2026) | IRS + Congress.gov | 2026-05-01 | 2026-12-15 | 1 | --tax --finance --visa`
- `2023-03-06 → 2023-09-05 | rental | NYC Local Law 18 of 2022 — Final Rules effective 6 Mar 2023; platform-verification enforcement began 5 Sep 2023; <30-day stays require host-present + city registration; listings ↓83% citywide, outer boroughs ↓~92% post-enforcement; effectively eliminates non-resident STR | NYC OSE + Mayor's Office | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-08-XX | rental | Miami Beach STR ban struck by Miami-Dade Circuit Court (Hanzman J., Aug 2025) as conflicting with state law — enforcement status uncertain pending appeal | Miami-Dade Circuit Court + Haber Law | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2022-04-26 → 2022-10-23 | rental | Honolulu Bill 41 (CO 22-7) — signed 26 Apr 2022, eff 23 Oct 2022 raising STR min stay to 90 days outside resort zones; 2023 court ruling partially REVERSED back to 30 days in non-resort | Honolulu Council + Hawaii Living | 2026-05-11 | 2026-08-01 | 2 | --rental`
- `ongoing | rental | LA Home-Sharing Ordinance (HSO, Ord 185,931) — 120-day cap primary residence only, registration mandatory, enforcement since Nov 1 2019 | LA Planning | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `ongoing | rental | SF 90-day unhosted cap; STR registration mandatory; Planning Dept enforcement | SF Planning + STR Office | 2026-05-11 | 2026-09-01 | 2 | --rental`
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
- `2026-04-01 | connectivity | 5G commercial launch (BTK schedule) — fibre rollout continues to lead; foreign-buyer broadband still depends on FTTH not 5G FWA | BTK | 2026-05-08 | 2026-07-01 | 3 | --connectivity --digital-nomad`
- `pending | connectivity | Starlink ❌ NOT licensed — SpaceX applied 2023, BTK rejected 2024-2025, "security concerns" cited; Türksat-6A 2024 competing satellite; no approval timeline | BTK + Resmi Gazete | 2026-05-08 | 2026-08-01 | 2 | --connectivity`

### 🇦🇪 AE

- `2024-04 | risks | Record Dubai floods exposed drainage limits → Tasreef stormwater plan phased to 2033 (interim AED 277m completed Jun 2025) | Dubai Municipality | 2026-05-01 | 2026-11-01 | 2 | --risks --insurance`
- `2025 | finance | Dubai Law 2/2025 — DIFC Wills direct enforcement for non-Muslim expats | DIFC Courts | 2026-05-01 | 2026-10-01 | 2 | --finance --notary`
- `2023-06 | tax | Federal Corporate Tax 9% effective from Jun 2023 — applies to commercial property held in qualifying entities above AED 375k threshold; individual ownership unaffected | FTA UAE | 2026-05-01 | 2026-09-01 | 2 | --tax --finance`
- `2025 | rental | RERA Smart Rental Index expanded to A/B/C/D building-quality scoring; brackets refreshed | DLD + RERA | 2026-05-01 | 2026-09-01 | 2 | --rental`
- `2022-10 | visa | Cabinet Decision 65/2022 expanded Golden Visa RE route to AED 2M (single or aggregate); off-plan + escrow eligible | ICP + DLD | 2026-05-01 | 2026-08-01 | 1 | --visa`
- `2026-03 | connectivity | Starlink ✅ licensed Mar 2026 (TDRA approval) — UAE residential roaming previously grey-market; Etisalat-du duopoly remains, but Starlink rural/villa fallback now legal | TDRA | 2026-05-08 | 2026-09-01 | 2 | --connectivity`

### 🇯🇵 JP

- `2023-12 | tax | 空家特措法 (Vacant Houses Special Measures Act) 改正 — 管理不全空家 designation can revoke 1/6 land tax exemption (~6× annual fixed-asset bill on land portion) | MLIT | 2026-05-01 | 2026-09-01 | 2 | --tax --risks`
- `2024-04-01 | finance | 民法改正 (Civil Code reform) — mandatory inheritance registration within 3 yrs (¥50k fine), 2-yr address-change registration; foreign-heir traps | 法務省 | 2026-05-01 | 2026-09-01 | 2 | --finance --notary`
- `2024-2025 | finance | BoJ rate normalization (Mar 2024 NIRP exit → Jul 2024 0.25% → Jan 2025 0.5% → Dec 2025 ~0.75%); mortgage variable rates rising; Flat 35 applications +50% YoY Q3 2025 | BoJ | 2026-05-01 | 2026-08-01 | 1 | --finance --price`
- `2018-06 | rental | 民泊法 Minpaku law 180-night/yr cap; 2025 Tokyo + Kyoto + Osaka ward-level overlay restrictions intensifying | 観光庁 民泊ポータル | 2026-05-01 | 2026-09-01 | 2 | --rental`
- `2025-09-01 | rental | Osaka hotel tax tiered shift from 1 Sep 2025 — ¥200 for ¥5k-15k; ¥400 for ¥15k-20k; ¥500 for ≥¥20k per pp/n | Osaka Prefecture | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`
- `2026-03-01 | rental | Kyoto hotel tax 9× hike from 1 Mar 2026 — new tiered structure ¥200 / ¥400 / ¥1,000 / ¥4,000 / ¥10,000 (up to 9× prior top tier); top tier targets premium ¥100k+/n stays | Kyoto City | 2026-05-11 | 2026-08-15 | 1 | --rental --tax`
- `2027-XX-XX (announced 2025-11-27) | rental | Tokyo to shift to 3% lodging tax from FY2027 (replacing tiered ¥100-200/pp/n) | Tokyo Metropolitan Govt + Japan Times | 2026-05-11 | 2026-12-01 | 2 | --rental --tax`
- `2022-09-20 | risks | 重要土地等調査法 (Important Land Investigation Act) effective; 注視区域 around defense / border / nuclear facilities; reporting may apply to certain residential transactions | 内閣府 | 2026-05-01 | 2026-10-01 | 2 | --risks --visa`
- `n/a (no statute identified) | other | r/japanlife thread 1oz5mvf (2025) alleges a municipality-required pre-deed "justification hearing" with foreigner-specific framing on a rural plot — SINGLE-THREAD ANECDOTE ONLY; a foreigner-specific gate is NOT established in primary law (agent-attributed talking points, single-sourced, uncorroborated, no statute/ordinance identified). The closest REAL regimes are universal and NOT nationality-gated: 国土利用計画法 事後届出 (Act 92/1974 — buyer files use-purpose + price within 2 weeks via the 市町村長 to the prefectural governor, who may issue a 勧告; thresholds ≥2,000/5,000/10,000 m² by zone) and 農地法 §3 農業委員会 permission (Act 229/1952 — farmland only, contract void without it); 開発許可 近隣説明会 (都市計画法 §29/33 + 市町村開発条例) is a development-conditioned community-meeting practice (meetings yes, statutory resident-veto generally no); 重要土地等調査法 (Act 84/2021) is a universal-scope security NOTIFICATION regime — does NOT match the anecdote. Nationality-recording added to 農地法 §3 (since 2023-09-01) / 国土利用計画法 施行規則 (corporate acquirers, from 2026-04-01) is data capture, NOT a foreigner approval gate. | MLIT 土地取引規制制度 https://www.mlit.go.jp/totikensangyo/totikensangyo_tk2_000019.html + 内閣府 重要土地等調査法 https://www.cao.go.jp/tochi-chosa/ + r/japanlife 1oz5mvf https://www.reddit.com/r/japanlife/comments/1oz5mvf/ (anecdote) | 2026-05-15 | 2027-05-15 | 4 | --permits --buying-process --scams --remote`

### 🇹🇭 TH

- `2020-01 | tax | Land and Building Tax Act BE 2562 (2019) effective — first national property tax; rates 0.01–0.7% by use; annual Royal Decree reductions | Revenue Department | 2026-05-01 | 2026-08-01 | 1 | --tax`
- `2024-mid | visa | Destination Thailand Visa (DTV) launched — 5-yr multi-entry, 180 days/stay, THB 500k savings + freelance/remote-worker proof | MFA Thailand + Immigration Bureau | 2026-05-01 | 2026-08-01 | 2 | --visa --digital-nomad`
- `2024-2025 | rental | Hotel Act §4 STR enforcement intensifying — STR <30 nights without hotel license illegal; varies by province; Bangkok / Phuket leading enforcement | DBD + provincial governors | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2024-2025 | visa | Proposed 99-yr lease + 75% condo quota — under Cabinet discussion; NOT enacted as of May 2026 | Cabinet of Thailand | 2026-05-01 | 2026-09-01 | 2 | --visa --price`
- `2024 | tax | Foreign-source income remittance taxation — Revenue Dept interpretation evolving | Revenue Department | 2026-05-01 | 2026-08-01 | 2 | --tax --visa`

### 🇹🇼 TW

- `2023-XX-XX | rental | Taiwan Tourism Bureau reorganised into **Tourism Administration MOTC** at `admin.taiwan.net.tw`; legacy `dot.gov.tw` URLs retired; same authority chain under the Ministry of Transportation and Communications; STR analytics + tourism statistics still published at the new portal | MOTC Taiwan | 2026-05-27 | 2027-12-31 | 4 | --rental (TW)`

### 🇩🇴 DO

- `2017 | finance | AML Ley 155-17 + UAF — beneficial-owner disclosure + source-of-funds proof for property transactions | UAF | 2026-05-01 | 2026-12-01 | 3 | --finance --notary`
- `2022 | risks | Hurricane Fiona (Sept 2022) → MOPC R-007 amendments to track | MOPC | 2026-05-01 | 2026-10-01 | 3 | --risks --insurance`
- `2025 | tax | IPI threshold DOP 9,860,649 (2025) — indexed annually; CONFOTUR-registered tourism projects 100% IPI + transfer + ITBIS exempt ~15 yrs | DGII + MITUR | 2026-05-01 | 2027-01-01 | 2 | --tax`
- `ongoing | visa | Investor residency USD 200k → 2-3-yr citizenship — fast-track to passport; CONFOTUR-registered RE benefits stack | Migración + MITUR | 2026-05-01 | 2026-09-01 | 2 | --visa`

### 🇨🇴 CO

- `2020 | finance | Decreto 1339/2020 — Catastro multipropósito national rollout; closing avalúo-vs-comercial gap; some areas seeing 2-3× predial bills | IGAC + DNP | 2026-05-01 | 2026-09-01 | 2 | --tax --price`
- `2024 | rental | Bogotá STR — 10% lodging tax + RNT mandatory CLAIM UNVERIFIED — "Decreto 538/2024" not retrievable; closest match Decreto 236/2024 (different subject). Data not publicly available as stated — verify at alcaldiabogota.gov.co/sisjur | Alcaldía Bogotá + MITUR | 2026-05-11 | 2026-08-01 | 2 | --rental`
- `2024 | rental | Medellín El Poblado STR enforcement — RNT-driven closures of unlicensed units (1,700+ identified 2024); specific "Acuerdo 056/2024" reference NOT verified in primary source — verify at concejodemedellin.gov.co | Concejo Medellín | 2026-05-11 | 2026-08-01 | 2 | --rental`
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

### 🇪🇨 EC

- `2024-04-01 | tax | IVA raised from 12% → 15% (NOT 13%) — Decreto Ejecutivo 198/2024 (11 Mar 2024) + Ley Orgánica para Enfrentar el Conflicto Armado Interno; standard rate effective 1 Apr 2024; emergency security funding; potential revert to 12% remains political possibility | SRI + Decreto Ejecutivo 198/2024 | 2026-05-27 | 2026-09-01 | 1 | --tax`
- `ongoing | tax | CGT 0% on habitual residence after 1-year holding (NOT 5 years) — UNIQUE LATAM exemption; LRTI art. 8 + reglamento, as amended by Ley Orgánica de Reforma Tributaria | SRI + Ley Orgánica Reforma Tributaria | 2026-05-27 | 2026-12-01 | 1 | --tax --exit`
- `ongoing | visa | Visa de Inversionista USD 47,000 (= 100 × SBU at SBU 2026 USD 470/mo) in Ecuadorian real estate or fixed-term productive activity; verify current SBU multiple at Cancillería; Ley Orgánica de Movilidad Humana 2017 + reglamento | decreto Ministerio del Trabajo Dec 2025 + Cancillería | 2026-05-27 | 2026-12-01 | 2 | --visa`

### 🇿🇦 ZA

- `2025-01 | finance | Expropriation Act 13 of 2024 assented Jan 2025 — Constitutional challenges pending; theoretical risk for residential land but practical urban risk remains low | Constitutional Court + DALRRD | 2026-05-01 | 2026-09-01 | 1 | --finance --visa`
- `2024-08 | rental | Tourism Amendment Bill regulating Airbnb pending; municipal rules vary (Cape Town requires temporary land-use rights for STR in some zones) | Tourism Dept + municipalities | 2026-05-01 | 2026-08-01 | 2 | --rental`
- `2024-02-28 | tax | Solar PV individual rebate (up to R15,000) expired 28 Feb 2024 — verify if extended in 2026/27 Budget | SARS + Treasury | 2026-05-01 | 2026-08-01 | 3 | --tax --esg`
- `2025-26 | tax | SARS Transfer Duty Schedule 8 — exempt below R1.1M, progressive to 13% above R12M; verify exact brackets each tax year | SARS | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2024-2025 | risks | Eskom load-shedding declined via Operation Vulindlela + private generation; backup power still common in upper-middle market | Eskom + DMRE | 2026-05-01 | 2026-09-01 | 3 | --risks --finance`
- `2022-02 | finance | Property Practitioners Act 22/2019 (PPRA) replaced EAAB Feb 2022 — new agent regulation + FFC requirements | PPRA | 2026-05-01 | 2027-01-01 | 3 | --finance --notary`
- `2026-2027 (in flight) | connectivity | Starlink GREY-MARKET — ICASA requires 30% local-ownership (BEE); Musk equity-equivalent proposal not approved; imports via roaming reseller (Mauritius/Mozambique SIMs) widely used; **earliest legal launch est. 2026-2027** | ICASA + DCDT | 2026-05-08 | 2026-08-01 | 1 | --connectivity`

### 🇬🇪 GE

- `2025-06-01 | regulatory | Foreign Agents Registration Act (FARA) — passed Parliament 1 Apr 2025, in force 1 Jun 2025; criminal liability for non-registration; affects foreign-funded NGOs/JVs/advisors but NOT private residential foreign property purchase | Parliament of Georgia + Venice Commission CDL-AD(2025)034 + Andersen 2025 | 2026-05-27 | 2026-08-01 | 2 | --tax --rental --scams`
- `2026-03-01 | visa | Investment residence permit real-estate threshold rises from US$100k → US$150k (1-year renewable); US$300k 5-year unchanged; transition rule requires completed purchase + full payment by 28 Feb 2026 to lock legacy threshold | Government of Georgia + sda.gov.ge | 2026-05-27 | 2026-04-01 | 2 | --tax --rental`
- `2026-03-01 | visa | Labor migration amendments (adopted 26 Jun 2025) require work permits for foreign workers incl. remote workers, self-employed, entrepreneurs beyond visa-free year | Parliament of Georgia | 2026-05-27 | 2026-04-01 | 2 | --work --rental`
- `2026-01-01 | regulatory | Decree #602 of 26 Dec 2025 mandates travel medical insurance (min GEL 30,000 coverage) for all foreign entrants for duration of stay | Government of Georgia + matsne.gov.ge | 2026-05-27 | 2026-12-01 | 3 | --price --rental`
- `2025-04-17 | visa | Ordinance #122 amended Government Decree #256 visa-free list — 17 nationalities (Afghanistan, Bangladesh, Eritrea, Ethiopia, Ghana, Yemen, Cameroon, Côte d'Ivoire, DRC, Morocco, Nigeria, Pakistan, Somalia, Syria, Sudan, Tanzania, Uganda) lose Gulf-state-permit visa-free route | matsne.gov.ge/en/document/view/2867361 | 2026-05-27 | 2026-10-01 | 3 | --rental --scams`
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
- `2024-02-14 | rental | Bali Provincial Levy IDR 150,000 per foreign visitor (one-time per arrival) under Perda Bali No. 6/2023, effective 14 Feb 2024 | Bali Provincial Govt + lovebali.baliprov.go.id | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `2026-XX-XX | rental | Bali Perda No. 4/2026 — nominee land-holdings CRIMINALIZED (up to 5 years prison + IDR 1bn fine); OTA platforms (Airbnb / Booking / Agoda) must verify NIB (business ID) of every listing by Mar 2026 deadline; foreigners cannot hold Pondok Wisata licence (Permenpar 18/2016) — compliant path = PT PMA + Villa licence KBLI 55193 | Bali Provincial Govt | 2026-05-11 | 2026-08-01 | 1 | --rental`

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
- `2024-08-01 | rental | HCMC residential STR BAN — Decision 26/2024/QD-UBND of HCMC People's Committee, in force 1 Aug 2024, interpreting 2023 Housing Law: residential apartment buildings cannot operate STR; only mixed-use condotels permitted as tourism accommodation. Hanoi has no specific STR regulation as of 2026; business registration with DoF still required | HCMC People's Committee + Vietnamlawmagazine | 2026-05-11 | 2026-08-01 | 1 | --rental`
- `2026-09-11 | connectivity | Hague Apostille convention enters into force for VN — POA chain shifts from full consular legalisation to apostille; calendar-actionable re-stamp of shared/connectivity.md + shared/language.md | HCCH + Vietnam MFA | 2026-05-08 | 2026-09-15 | 2 | --connectivity --language`
- `pending | connectivity | Starlink licence still under review — SpaceX received conditional pilot approval 2024 but no commercial-licence as of 2026-05-08; verify on SpaceX availability map | MIC | 2026-05-08 | 2026-08-01 | 2 | --connectivity`
- `2025-03-01 | cadastre | MONRE (Ministry of Natural Resources and Environment, Bộ Tài nguyên và Môi trường) merged with MARD (Ministry of Agriculture and Rural Development) to form **MAE (Ministry of Agriculture and Environment)** effective 1 March 2025; Department of Land Administration + Office for Land Use Rights Registration (VPĐKĐĐ) re-housed under MAE; cadastre web-portal moved to `en.mae.gov.vn`; existing 2024 Land Law and 2023 Housing Law authorities unchanged in substance, only the parent ministry's name + URL | Vietnam National Assembly Resolution 176/2025/QH15 + en.mae.gov.vn confirmation | 2026-05-27 | 2027-03-01 | 2 | --notary --remote (VN)`

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

### 🇲🇺 MU

- `pending (gazette publication vs 2026-07-01 contested across sources) | tax | Finance Act 2025 — registration duty + LTT for non-citizens raised 5%→10% on EDB-scheme acquisitions; effective date contested across sources (some sections from gazette publication, others from 1 Jul 2026) — verify in gazetted Act before transaction | mof.govmu.org + mra.mu | 2026-05-07 | 2026-08-01 | 1 | --tax ownership --visa`
- `2025-07-01 | tax | New 0/10/20% PIT brackets effective 1 Jul 2025 (Finance Act 2025) — replacing prior 15% flat | MRA Mauritius Revenue Authority | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2025-XX-XX (Finance Act 2025) | visa | Retirement Permit threshold raised USD 1,500/mo → USD 2,000/mo (Non-Citizen Retiree route — passport.govmu.org) | EDB + Passport Office | 2026-05-07 | 2026-09-01 | 2 | --visa`
- `2025-02-XX | foreign-buyer | EDB published Amendments to IRS/RES/IHS/PDS/SCS regulations Feb 2025 — new mandatory requirements for non-citizens | EDB Mauritius (FAQ-Amendments document) | 2026-05-07 | 2026-09-01 | 2 | --tax ownership --visa`
- `2024-XX-XX | tax | Mauritius statutes consolidated to **lawsofmauritius.govmu.org** (Attorney-General's Office portal); legacy mra.mu /download/*.pdf URL tree for the Land (Duties & Taxes) Act, Registration Duty Act + Finance (Misc Provisions) Acts retired; MRA retains tax administration but the AG portal is now the canonical primary source for statutes | Attorney-General's Office Mauritius — lawsofmauritius.govmu.org | 2026-05-27 | 2027-12-31 | 4 | --tax --notary (MU)`

### 🇰🇿 KZ

- `2026-01-01 | tax | New Tax Code effective 1 Jan 2026 — progressive PIT 10%/15% above 8,500 MCI (replacing prior 10% flat above thresholds) + VAT rate change | Adilet (adilet.zan.kz) — Ministry of Justice legal database | 2026-05-07 | 2026-08-01 | 2 | --tax --rental --finance`
- `2026-04-01 | mains | Utility-tariff moratorium ENDED 1 Apr 2026 (MEKS — Ministry of Energy modernization plan, 13.5T KZT through 2029) — electricity + heat + water tariff increases phased through 2029 | Ministry of Energy KZ + KEGOC | 2026-05-07 | 2026-09-01 | 2 | --mains --tax`
- `2025-05-10 | visa | Investor Visa "Golden Visa" launched 10 May 2025 — US$300,000 qualifying investment (KZ securities / AIFC participants / productive business) → 10-yr residence permit; **REAL ESTATE EXPLICITLY EXCLUDED** as qualifying investment; applications open 1 Jun 2025 | citizenx.com + goldenvisas.com (program guides); MFA KZ | 2026-05-07 | 2026-09-01 | 1 | --visa`
- `2021-05-XX | ownership | Agricultural land BANNED for foreigners — Law signed May 2021 by Tokayev post-2016 land protests; pre-2021 leases grandfathered to expiry | Land Code amendments — Adilet | 2026-05-07 | 2027-01-01 | 1 | --tax ownership`

### 🇨🇻 CV

- `2026-01-01 | tax | Lei n.º 55/X/2025 of 6 June 2025 — IUP (Imposto Único sobre o Património) REPEALED, replaced by IPI (Imposto sobre a Propriedade de Imóveis, 0.1% annual ownership) + ITI (Imposto sobre a Transmissão de Imóveis, 1% transfer); Boletim Oficial I Série n.º 46 | boe.incv.cv (Bulletin n.º 46 / 2025) | 2026-05-07 | 2026-09-01 | 1 | --tax`
- `2025-01-01 | tax | IRPC corporate-income-tax rate cut 22%→20% (2025 Budget) — tourism-zone preferential regimes maintained | DGCI | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2026-02-XX | macro | IMF Seventh ECF Review + Third RSF Review concluded Feb 2026 — real GDP +7.2% 2024 / +5.2% 2025; CVE-EUR peg credibility reaffirmed | IMF (PR26036) | 2026-05-07 | 2026-09-01 | 3 | --macro --currency`

### 🇸🇨 SC

- `2025-03-20 | foreign-buyer | SPA (Sanction Permit Act) MORATORIUM LIFTED for non-Seychellois — residential acquisition permitted under new floors (SCR 10M dwelling minimum + SCR 4,000/m² bare-land); Sanction Duty raised 11%→12% | Government of Seychelles (Ministry of Investment, Entrepreneurship and Industry) | 2026-05-07 | 2026-08-01 | 1 | --tax ownership --visa`
- `2024-01-01 | tax | IPT (Immovable Property Tax) doubled 0.25%→0.5% — foreigner-only annual tax on non-Seychellois-owned residential property (raised eff. 1 Jan 2024) | SRC Seychelles Revenue Commission | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2026-01-15 | mains | PUC tariff revisions effective 15 Jan 2026 — electricity + water tariffs adjusted | Public Utilities Corporation (puc.sc) | 2026-05-07 | 2026-09-01 | 3 | --mains`
- `2023-08-01 → 2026-01-01 | rental | Tourism Environmental Sustainability Levy (TESL) — eff 1 Aug 2023: small (1-24 rooms) SCR 25/pp/n; medium (25-50) SCR 75; large (51+) + yachts SCR 100; charged on invoice NOT advertised price. FROM 1 JAN 2026: small establishments (1-24 rooms) NO LONGER subject to levy — yield-positive for foreign-owned villas | Tourism Seychelles | 2026-05-11 | 2026-09-01 | 1 | --rental --tax`

### 🇨🇳 CN

- `2026-01-01 | tax | VAT cut to 3% for residential resale held <2 years (replacing prior 5.6% within 2 years) — material reduction in flipping-tax-stack | MoF + State Taxation Administration (chinatax.gov.cn) | 2026-05-07 | 2026-08-01 | 2 | --tax`
- `2025-09-XX | currency | SAFE September 2025 cross-border FX-reform — HK/Macao settlement framework extended NATIONWIDE; non-self-use residential restriction REMOVED for cross-border purchases (US$50k individual quota retained) | SAFE State Administration of Foreign Exchange | 2026-05-07 | 2026-08-01 | 1 | --currency --tax ownership`
- `2024-12-01 | tax | Deed-tax restructure — first-home <140m² 1% / first-home ≥140m² 1.5% / second-home <140m² 1.5% / second-home ≥140m² 2-3% (city-tier-dependent); replaces prior structure | MoF + State Taxation Administration | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2024-09-XX | foreign-buyer | Tier-1 social-security overlay easing September 2024 — Beijing 5-yr / Shanghai 1-yr / Shenzhen 3-yr / Guangzhou abolished (purchase-restriction Hukou-linked threshold periods relaxed) | Local Housing Bureaux Beijing/Shanghai/Shenzhen/Guangzhou | 2026-05-07 | 2026-09-01 | 1 | --tax ownership`

### 🇯🇲 JM

- `2025-10-28 | risks | Hurricane Melissa Cat 5 landfall 28 Oct 2025 (Westmoreland Parish) — strongest Atlantic hurricane in Jamaican recorded history; widespread Westmoreland + Hanover + St James property damage; insurance market hardening + BSJ JNBC building-code review expected through 2026-2027 | NOAA NHC AL132025 + ODPEM | 2026-05-07 | 2026-08-01 | 1 | --risks --insurance --finance`
- `2025-04-01 | tax | Income-tax personal-allowance threshold raised to JMD 1.8M effective 1 Apr 2025 (was JMD 1.5M) — material PIT relief; rental + business income unaffected if held in personal name | TAJ Tax Administration Jamaica | 2026-05-07 | 2026-09-01 | 2 | --tax --rental`
- `2019-XX-XX | tax | Transfer Tax + Stamp Duty stack reformed — 2% Transfer Tax + JMD 5,000 flat Stamp Duty (was 5% transfer + 4% stamp pre-2019) — material reduction in transaction costs | TAJ + Ministry of Finance JM | 2026-05-07 | 2027-01-01 | 2 | --tax`

### 🇧🇸 BS

- `2022-01-01 | tax | VAT raised 7.5%→10% effective 1 Jan 2022 (Government Budget Communication) — broad consumption-tax increase touching property-related expenditures | DIR Department of Inland Revenue | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `ongoing | tax | RPT (Real Property Tax) bands budget-revisable annually via Budget Communication — verify current bands at DIR before any transaction-cost computation | DIR — inlandrevenue.finance.gov.bs/real-property-tax | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `ongoing | risks | Hurricane Dorian (Sep 2019) calibration event — destroyed ~75%+ of homes on parts of Abaco + Grand Bahama; insurance market hardening continues 6+ years post-event; remains baseline for foreign-buyer DD on insurance availability + cost | NOAA NHC AL052019 + Government of The Bahamas | 2026-05-07 | 2027-01-01 | 1 | --risks --insurance --finance`

### 🇸🇲 SM

- `2018-12-24 | foreign-buyer | Legge 24 dicembre 2018 n.173 + Decreto Delegato implementation — prior authorization regime ABOLISHED for foreign acquisition; replaced with **2-property cap per foreign individual** (vs unlimited Sammarinese citizens / pre-2018 1-property cap) | Bollettino Ufficiale RSM | 2026-05-07 | 2027-01-01 | 1 | --tax ownership`
- `pending 2026 (verify gazette) | tax | IGR (Imposta Generale sui Redditi — main income tax) 2026 reform — major restructure pending; verify gazetted text before relying on rate brackets | Repubblica di San Marino — Bollettino Ufficiale | 2026-05-07 | 2026-08-01 | 2 | --tax --rental --finance`

### 🇧🇧 BB

- `2026-12-31 (renewed) | visa | Welcome Stamp 12-month digital-nomad visa — Cabinet renewed to 31 Dec 2026 (USD 50,000+ income threshold; tax-exempt on Barbados-sourced foreign-employer income); track next renewal cycle | Visit Barbados — Welcome Stamp portal `https://www.visitbarbados.org/barbados-welcome-stamp` | 2026-05-08 | 2026-12-01 | 2 | --visa`
- `2026 income year | tax | Personal Income Tax band reduction announced for income year 2026 (BRA Policy Note 20 Apr 2026 — verify exact bands when gazetted in Income Tax Act schedule); 2025 schedule remained 12.5% / 28.5% with BBD 25,000 personal allowance | Barbados Revenue Authority — `https://bra.gov.bb/` | 2026-05-08 | 2026-08-01 | 2 | --tax`
- `2024-07-01 | risks | Hurricane Beryl Cat 3 passed ~150 km south of Barbados — first major-hurricane impact in modern memory (~70 yrs since Janet 1955); ECLAC-assessed effects ~BBD 193M (~0.15% of GDP); insurance market re-rating ongoing 2024-2026 | ECLAC 2024 — `https://www.cepal.org/en/publications/82157-assessment-effects-and-impacts-hurricane-beryl-barbados-2024` | 2026-05-08 | 2026-11-01 | 1 | --risks --insurance`
- `2025-04-01 | tax | Resilience and Regeneration Fund employee contribution raised 0.10% → 0.25% of gross earnings (2025 Budget) | KPMG TaxNewsFlash 2025-03 — `https://assets.kpmg.com/content/dam/kpmg/bb/pdf/Barbados%20budget%20review%202025.pdf` | 2026-05-08 | 2027-04-01 | 3 | --tax`
- `2025-04-XX | tax | PTT removed for deeds of gift to children/dependants for land <1 acre (gifts only — does not affect arm's-length sales) — 2025 Budget | KPMG TaxNewsFlash 2025-03 | 2026-05-08 | 2027-04-01 | 3 | --tax`

### 🇧🇿 BZ

- `2024-12-XX | tax | Stamp Duties (Amendment) Act 2024 (Act No. 33 of 2024) — clarified treatment of share transfers in IBC-held property + other technical updates; verify consolidated current text with attorney for any 2025-2026 transaction | National Assembly of Belize — `https://www.belizelaw.org/` | 2026-05-08 | 2026-09-01 | 2 | --tax --notary`
- `2025-01-01 | tax | Income Tax exemption raised BZD 26,000 → BZD 29,000 effective 1 January 2025 | Belize Tax Service / Government of Belize budget measures | 2026-05-08 | 2026-09-01 | 3 | --tax --rental`
- `2024-XX-XX (in consultation) | foreign-buyer | Government 2024 draft Maya Customary Land Tenure Policy — intended to formalise village-level communal title in Toledo District (~41 Maya villages); recognised by CCJ 2015 ruling Maya Leaders Alliance v Attorney General of Belize as legally equal to Western property ownership; verify current statutory progression before any Toledo-District deal | Belmopan-published policy framework — verify at Government of Belize | 2026-05-08 | 2026-09-01 | 1 | --visa ownership --notary`
- `2023-XX-XX (current) | visa | QRP age threshold lowered 45 → 40 — Belize Tourism Board Qualified Retirement Programme | Belize Tourism Board — `https://www.belizetourismboard.org/programs-events/retirement-program/` | 2026-05-08 | 2026-12-01 | 3 | --visa`

### 🇱🇰 LK

- `2025-11-28 | risks | Cyclone Ditwah landfall — Cat-equivalent storm; USD 4.1bn damage; 1.1M ha flooded; Central Highlands tea-country property repricing; disrupted IMF EFF fifth review | Department of Disaster Management Sri Lanka + IMF Sri Lanka EFF reviews | 2026-05-08 | 2026-08-01 | 1 | --risks --insurance --price`
- `2025-04-01 | tax | Stamp Duty (Amendment) Act 2025 — doubled stamp duty on rental/lease agreements from Rs.10 → Rs.20 per Rs.1,000 of total rental value, effective 1 April 2025 | Inland Revenue Department Sri Lanka — `https://www.ird.gov.lk/` | 2026-05-08 | 2026-09-01 | 2 | --rental --tax`
- `2025-XX-XX | tax | Inland Revenue Act Amendment 2025 — CGT 10% statutory; 15% proposed (verify gazetted text before quoting) | Parliament of Sri Lanka — `https://www.parliament.lk/uploads/acts/gbills/english/6379.pdf` | 2026-05-08 | 2026-08-01 | 1 | --tax --exit`
- `2024-XX-XX (current) | foreign-buyer | Apartment Ownership Law amendments (Act No. 21 of 2018) — foreigners may purchase condominium on any floor (post-2018 reform — full purchase price must be remitted from abroad up-front under inward-remittance rule) | Lanka Law consolidated PDF + SriLankaLaw.lk | 2026-05-08 | 2026-12-01 | 2 | --visa ownership --finance`
- `2024-XX-XX | visa | Golden Paradise Residence Visa — launched 2024 (USD 200k bank deposit OR USD 75k condominium); replaces Resident Guest Scheme + pre-2022 schemes paused during crisis | Department of Immigration & Emigration Sri Lanka — `https://eservices.immigration.gov.lk/golden-paradise-visa.html` | 2026-05-08 | 2026-12-01 | 2 | --visa`
- `2024-01-01 | tax | VAT raised 15% → 18% effective 1 January 2024 (developer first-sale apartments only) | Sri Lanka Inland Revenue Department | 2026-05-08 | 2027-01-01 | 2 | --tax`

### 🇰🇭 KH

- `pending (deferred multiple times) | tax | CGT activation under Prakas 346/2020 + Law on Taxation 2023 (NS/RKM/0523/004) — when activated: 20% on gain for individuals — track activation; deferred multiple times since 2020 | General Department of Taxation (GDT) Cambodia — `https://www.tax.gov.kh/` | 2026-05-08 | 2026-09-01 | 1 | --tax --exit`
- `2020-10-XX (ongoing rollout) | currency | Bakong digital-riel rollout (NBC) + USD/KHR de-dollarization signal — National Bank of Cambodia long-term policy objective; foreign-buyer transactions remain USD-dominant ~80-90% urban | National Bank of Cambodia — `https://www.nbc.gov.kh/english/` | 2026-05-08 | 2026-12-01 | 3 | --currency --finance`
- `2024-2026 (intensifying) | foreign-buyer | Anti-nominee enforcement intensity — Cambodian-majority-company workaround under enforcement pressure; nominee-Cambodian-spouse arrangements increasingly challenged | MLMUPC + General Department of Cadastre and Geography (GDCG) | 2026-05-08 | 2026-09-01 | 1 | --visa ownership --integrity`
- `2019-XX-XX (untested) | foreign-buyer | Trust Law 2019 over land — constitutionally untested; unclear whether trust structure circumvents Article 44 prohibition on foreign land ownership; do NOT rely until tested in Constitutional Council | Royal Government Council of Jurists | 2026-05-08 | 2026-12-01 | 2 | --visa ownership --integrity`

### 🇲🇻 MV

- `2025-12-06 to 2026-06-05 | tax | 16th Tourism Act Amendment 2025-12 — discounted lease-extension window (head-lease-extension cost reduced one-time; window 2025-12-06 to 2026-06-05); affects resort head-lease economic value | Ministry of Tourism Maldives — `https://www.tourism.gov.mv/dms/document/23d485632704b30cf178db46d41f0bff.pdf` | 2026-05-08 | 2026-06-05 | 1 | --tax --exit`
- `2025-01-01 | tax | TGST (Tourism Goods and Services Tax) raised to 17% + Green Tax USD 12/bednight, both effective 1 January 2025 — affect resort + guesthouse operating economics | MIRA Maldives Inland Revenue Authority — `https://www.mira.gov.mv/` | 2026-05-08 | 2026-08-01 | 2 | --tax --rental`
- `2019-04-23 | foreign-buyer | Article 251 round-trip — 2015 amendment (briefly opened freehold for ≥USD 1bn projects with ≥70% reclaimed land) REPEALED 23 April 2019 by 19th People's Majlis; only legal pathway for foreign exposure remains leasehold ≤99 years | Constitution Net + CTL Strategies + Maldives Independent | 2026-05-08 | 2027-01-01 | 1 | --visa ownership`

### 🇬🇭 GH

- `2022-XX-XX | tax | VAT raised 12.5% → 15% via Value Added Tax (Amendment) Act 2022 (Act 1082) | Ghana Revenue Authority — `https://gra.gov.gh/` | 2026-05-08 | 2027-01-01 | 2 | --tax`
- `2023-05-17 (ongoing) | macro | IMF Extended Credit Facility approved 17 May 2023, USD 3 billion 36-month programme — milestones quarterly through 2026; affects GHS managed-float dynamics + sovereign-debt restructuring + structural reform pace | IMF Country Page Ghana — `https://www.imf.org/en/Countries/GHA` | 2026-05-08 | 2026-08-01 | 1 | --macro --currency --finance`
- `2022-XX-XX | tax | Electronic Transfer Levy 1% on electronic transactions (Act 1075/2022 reduced from 1.5% → 1% via Act 1089 in 2023) — verify current rate at GRA | Ghana Revenue Authority | 2026-05-08 | 2026-12-01 | 3 | --tax`
- `2020-XX-XX | foreign-buyer | Lands Act 2020 (Act 1036) consolidated 6 prior land statutes — entered into force 2020; constitutional 50-year leasehold cap for non-Ghanaians (Art. 266) PRESERVED; customary tenure (stool / skin / family / clan) overlays ~78% of total land area per Lands Commission classification | Lands Commission Ghana — `https://lc.gov.gh/` | 2026-05-08 | 2027-01-01 | 1 | --visa ownership --notary`

### 🇰🇪 KE

- `2024-XX-XX | tax | Stamp Duty payment workflow for property transfers migrated from the Kenya Revenue Authority (KRA) eService portal to the **Ministry of Lands & Physical Planning Ardhi Sasa platform** (`ardhisasa.lands.go.ke`); KRA retains the Stamp Duty Act Cap 480 statute interpretation + advisory role but stamp duty calculation + e-payment + receipt now under Min of Lands; buyers must register on Ardhi Sasa to pay the duty before LSK can register the transfer; some KRA `kra.go.ke/business/*` and `kra.go.ke/individual/individual-pin-taxes/*` legacy paths still 404 | Ministry of Lands & Physical Planning Kenya + KRA | 2026-05-27 | 2027-06-30 | 2 | --tax --notary --remote (KE)`

### 🇷🇼 RW

- `2023-04-20 | tax | Property Tax Reform — Cabinet-approved 20 Apr 2023, effective Feb 2024, first declaration 20 Aug 2024 — Land Tax compressed FRW 0-300/m² → FRW 0-80/m² band (district/use-set); Building Tax 0.5%/0.3%/0.1% residential/commercial/industrial-SME of market value; Sale levy 2% registered / 2.5% unregistered (RWF 5M exempt floor on commercial sale value) | gov.rw Cabinet press release + RRA + Law on Sources of Revenue for Decentralized Entities | 2026-05-27 | 2026-09-01 | 2 | --tax`
- `2022-10-20 | tax | Capital Gains Tax — Law N° 027/2022 of 20/10/2022 (amended by Law N° 051/2023 of 05/09/2023): shares 10% / commercial immovable property 30%; residential individual sales captured through 2%/2.5% sale levy. The historical "5% flat" framing does NOT match primary statute | RRA Tax Handbook + PwC Worldwide Tax Summaries 2026 + Law 027/2022 + Law 051/2023 | 2026-05-27 | 2026-09-01 | 1 | --tax`
- `2025-07-01 | rental | Tourism Levy 3% — Law N° 015/2025 of 27 May 2025 (Parliament unanimous 28 Apr 2025); applies to hotels, motels, lodges, guest houses, apartments, similar accommodation services; 3% of room cost; declare + pay within 15 days of month-end | Law 015/2025 + RDB + Parliament Plenary 28 Apr 2025 + travelnews.africa | 2026-05-27 | 2026-09-01 | 2 | --rental --tax`
- `2024-06-05 | foreign-buyer | e-Apostille launch — MINAFFET + Irembo partnership; Rwanda 126th HCCH Convention member (deposit 6 Oct 2023); first country to launch e-Apostille from day-one of accession; 1-3 day processing via irembo.gov.rw | MINAFFET + ktpress.rw 4 Jun 2024 + Schmidt-Export | 2026-05-27 | 2027-06-01 | 3 | --notary --integrity foreign-buyer-journey`
- `2021-02-05 | visa | Investor visa Law N° 006/2021 of 05/02/2021 Art. 14 — USD 250,000 registered-investor permit (USD 100,000 for EAC + COMESA citizens); clarify "USD 500k luxury property" route is secondary-aggregator only — flag for primary-source verification with Rwanda Development Board | UNCTAD Investment Laws Navigator + RDB | 2026-05-08 | 2026-12-01 | 2 | --visa --integrity`
- `2021-06-10 | foreign-buyer | Law N° 27/2021 of 10/06/2021 (Land Law) — extended emphyteutic / leasehold term to 99 years for both residential + investment use (was 49 yrs investment / 20 yrs residential); foreigners get leasehold only; freehold reserved Rwandan citizens | Official Gazette + RLMUA | 2026-05-08 | 2027-01-01 | 1 | --visa ownership --notary`
- `2024-XX-XX | tax | Electronic Land Title rollout 2024 — all titles paperless via LAIS (ESRI ArcGIS-based, version 4.0); FRW 5,000 physical printout fee abolished by default | RLMUA — `https://www.lands.rw/` | 2026-05-08 | 2026-12-01 | 3 | --notary --integrity`

### 🇺🇿 UZ

- `2025-06-01 | visa | Golden Visa launch — 5-year Investor Residence Permit per Presidential Decree UP-89 of April 2025, entered into force 1 June 2025; thresholds USD 300k Tashkent city / USD 200k Samarkand+Bukhara+Namangan+Andijan+Fergana+Khorezm regions / USD 100k other regions; **INCLUDES real estate** (vs KZ which excludes RE); capital-injection alternative US$250k equity + US$150k per accompanying family member | Astana Times Apr 2025 + Library of Congress Global Legal Monitor 27 Jun 2025 + e-visa.gov.uz / mfa.uz | 2026-05-08 | 2026-08-01 | 1 | --visa`
- `2026-XX-XX | tax | 2026 +7% land/property/water indexation (per EY) — annual indexation of land tax + property tax + water tax + similar | EY Tax Alert Uzbekistan | 2026-05-08 | 2026-09-01 | 2 | --tax`
- `2022-07-16 | foreign-buyer | Cabinet of Ministers Resolution No. 384 of 16 July 2022 (PQ-384) — expanded eligibility to citizens of 108 countries to acquire built real estate (apartments / houses / commercial premises) WITHOUT residence permit; pre-2022 regime required residence permit first — gate now removed for EU/UK/US/CA/AU/NZ/JP/KR + GCC + most Asia; Land Code Articles 17-18 PROHIBITION on foreign land ownership PRESERVED | Kun.uz coverage of PQ-384 + Azizov & Partners legal memo | 2026-05-08 | 2027-01-01 | 1 | --visa ownership`
- `2017-09-XX | currency | Dual-rate "black market" gap closed September 2017 under Mirziyoyev liberalisation (Decree UP-5177); pre-2017 official ~3,000 UZS/USD vs unofficial ~8,000/USD (~2.5× spread); since Sep 2017 managed-float with active CBU intervention; cumulative depreciation 2017→2026 ~3,200 → ~12,500 UZS = ~290% nominal devaluation over ~9 years | Central Bank of Uzbekistan — `https://cbu.uz/en/` | 2026-05-08 | 2026-12-01 | 2 | --currency --finance`
- `2024-XX-XX | mains | Tashkent water utility "Suvsoz" rebranded **Toshkent shahar suv ta'minoti MCHJ** under O'zsuvta'minot AJ; new web portal `toshkent.uzsuv.uz` (legacy `suvsoz.uz` offline); operational responsibilities unchanged | Agency for the Operation of Water Management Facilities UZ + my.gov.uz/en/authority/844 | 2026-05-27 | 2027-12-31 | 4 | --mains (UZ)`

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
- ECJ press releases: https://curia.europa.eu/juris/recherche.jsf?language=en
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

*Last full audit: 2026-05-08 (added Tier-2 batch: BB/BZ/LK/KH/MV/GH/RW/UZ — total 109 countries tracked). Prior batch 2026-05-07 added Tier-1 (MU/KZ/CV/SC/CN/JM/BS/SM). Next mandatory full audit: 2026-07-26 (quarterly).*
