# Regulatory Watch — Cross-Country Reform Tracker

A single date-stamped registry of property-relevant reforms, transposition deadlines, ENDED programs, and watchlist items. Maintained as the **single source of truth for "what changed when"** — playbooks reference this; this references playbooks.

**Why it exists**: At 126 countries × 41 sections, the highest-blast-radius hallucination is asserting that an ENDED program is still active or quoting a tax rate that was reformed last quarter. This file makes "did anything change?" a single-file lookup before any re-stamp.

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
- `2026-01-01 | esg | DPE recalculated — electricity primary-energy conversion coefficient lowered 2.3 to 1.9 (arrete du 13 aout 2025, JO 26 Aug 2025); officially ~850,000 homes exit F/G passoire status with no works (base 1 Jan 2023, of 4.8M passoires; a Nov 2025 reassessment reported ~700,000 — secondary source, verify at ONRE); no label is downgraded; DPEs edited from 1 Jan 2026 auto-apply the new coefficient, pre-2026 DPEs stay valid and are updatable free without a new visit on the ADEME Observatoire DPE-Audit site | economie.gouv.fr new-DPE actualite + arrete 13 Aug 2025 + notaires.fr | 2026-07-03 | 2027-01-05 | 2 | --esg --rental --risks (FR)`
- `2026-05-20 | rental | National STR registration teleservice Declaloc IN FORCE — Loi Le Meur generalised one national registration channel for meuble-de-tourisme numbers (operated by DGE); decrets 2026-196 and 2026-197 du 19 mars 2026 (JO 20 Mar) finalised the architecture plus the communal control tool API Meubles; legal obligation since 20 May 2026 but the lessor-facing portal rolls out progressively H2 2026 (one source reports the portal at apimeubles.finances.gouv.fr — verify the entry point via DGE economie.gouv.fr when registering); art.4 fines pronounced by the maire up to 10000 EUR (defaut d'enregistrement) and up to 20000 EUR (fausse declaration or faux numero) | DGE (economie.gouv.fr) + decrets 2026-196 and 2026-197 + Legifrance | 2026-07-03 | 2026-11-01 | 1 | --rental (FR)`
- `2026-01-01 | tax | Micro-entreprise turnover thresholds revalued +7.6% for the 2026-2028 triennium (triennial indexation to the income-tax scale, CGI art. 50-0) — prestations de services and micro-BNC plafond rises 77700 to 83600 EUR (meuble-de-tourisme classe et chambres d'hotes follow this services plafond — aggregator-corroborated, BOFiP confirm recommended before HIGH); ventes de marchandises et fourniture de logement 188700 to 203100 EUR; applies to 2026 income onward (filed 2027); the Loi Le Meur 15000 EUR non-classe threshold is unchanged | Service-Public entreprendre actualite A18813 + autoentrepreneur.urssaf.fr seuils 2026 | 2026-07-03 | 2027-01-05 | 2 | --rental --tax --work (FR)`
- `2028-2031 (postponed by LFI 2026 art.106) | tax | RVLLH residential cadastral revaluation postponed 3 more years — owner declarations before 1 Jul 2028, report to Parliament before 1 Sept 2029, new values feed TFPB CFE THRS TEOM bases from 2031 (LOI 2026-103 du 19 fev 2026, art.106; CGI art.1518 A quinquies A); unofficial est. +20-40% rural TFPB circulates but no official figure published (unverified) | ANIL analyse LF 2026 + Legifrance art.106 | 2026-07-03 | 2026-12-01 | 2 | --tax (FR)`
- `2025-02-15 | tax | LMNP amortisation reintegration into resale plus-value — art.84 LFI 2025 (loi 2025-127 du 14 fev 2025) aligns non-professional furnished-let capital gains with LMP: previously-deducted amortisations now reduce the acquisition value so taxable plus-value rises on sale, for all cessions from 15 Feb 2025; confirmed to cover pre-2025 amortisations too (Reponse Mette, question AN n.10097, JOAN 24 mars 2026); managed residences services (student, senior, EHPAD) remain exempt; micro-BIC gites unaffected (no amortisation), only regime reel | Legifrance loi 2025-127 art.84 + Rep. Mette JOAN 24 Mar 2026 | 2026-07-03 | 2027-01-05 | 2 | --exit --home-tax --rental (FR)`

### 🇮🇹 IT

- `2026-01-01 | rental | Cedolare secca limit dropped from 5 → 2 properties (above which standard IRPEF) | Legge di Bilancio 2026 | 2026-04-26 | 2026-09-01 | 2 | --rental --tax`
- `2025-01-01 | rental | National CIN (Codice Identificativo Nazionale) mandatory display from 1 Jan 2025 (portal opened 1 Sep 2024); fines €800-€8,000 no CIN + €500-€5,000 non-display | Ministero del Turismo | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-05-31 (A3/A4 extension in force 2026-06-21) | rental | Florence STR regolamento (Del. CC 27/2025, in force 31 May 2025; underlying Variante al Piano Operativo Del. CC 19 & 20/2025) UPHELD not overturned — new-STR ban in UNESCO Nucleo Storico Zona A (only units let in 2024 may continue), 5-yr authorisations tied to owner+unit, 28 sqm min, keybox ban. Corte Cost. 186/2025 validated LRT Toscana 61/2024 art.59; TAR Toscana 14 May 2026 dismissed 19 appeals (sent. 916 & 925/2026). Ban extended to A3/A4 subzones (~67,780 homes, 504 streets) by Del. CC 28 del 4 Jun 2026, in force 21 Jun 2026 | Comune di Firenze + TAR Toscana sent. 916 & 925/2026 + Corte Cost. 186/2025 | 2026-07-02 | 2026-11-01 | 1 | --rental`
- `2026-XX-XX | rental | Milan 2026 Winter Olympics tourist tax spike — €9.50/n for accommodation within 30km of Olympic venues, 2026 only (vs €6.30/n standard); 14-night cap | Comune di Milano | 2026-05-11 | 2026-11-01 | 3 | --rental`
- `2024-XX-XX | rental | Venice Contributo di Accesso €5 day-tripper access fee (€10 if within 3 days), 2026 dates 3 Apr–26 Jul on Fri-Sun + special weeks; hotel guests/residents/workers/students exempt | Comune di Venezia | 2026-05-11 | 2026-09-01 | 3 | --rental`
- `2024-01-01 | tax | Southern Italy 7% pensioner regime — re-confirmed annually; expires after 9 yrs of residency | Agenzia delle Entrate | 2026-04-26 | 2027-01-15 | 2 | --tax (pension regime)`
- `2026-05-20 | rental | EU Short-Term Rental Regulation (EU) 2024/1028 fully applicable in Italy from 20 May 2026 — the registration number it mandates coincides with the CIN, and online platforms (Airbnb, Booking, Vrbo) transmit booking data monthly to the Ministero del Turismo via the BDSR. CIN also now required in Modello 730/2026, Redditi PF 2026 and Certificazione Unica 2026 (punto 22) | Regolamento (UE) 2024/1028 + Ministero del Turismo BDSR | 2026-07-03 | 2026-11-01 | 2 | --rental (IT)`
- `2025-03-31 (staggered by firm size; fully in force since 2026-03-31) | insurance | Mandatory catastrophe (CatNat) insurance for businesses phased in — grandi imprese entro 31 Mar 2025 (90-day transition to 30 Jun 2025), medie entro 30 Set 2025, micro e piccole entro 31 Dic 2025; pesca/acquacoltura + micro/piccole turistico-ricettive e somministrazione prorogate al 31 Mar 2026 by DL 31 dic 2025 n. 200 (Milleproroghe, conv. L. 26/2026). Introduced by L. 213/2023 (Legge di Bilancio 2024) art. 1 c. 101; NOT residential; non-compliance blocks access to public grants, subsidies and incentives (art. 1 c. 102) | MIMIT polizze rischi catastrofali (Cat Nat) + DL 200/2025 conv. L. 26/2026 | 2026-07-03 | 2026-10-01 | 3 | --insurance --risks (IT)`

### 🇪🇸 ES

- `2025-04-03 | visa | Golden Visa programme abolished | Ley 1/2025 | 2026-04-26 | 2026-10-01 | 1 | --visa`
- `2025-06-XX | tax | Cataluña ITP made progressive (replacing flat 10%) — top bracket 13% for >€1.5M | Generalitat de Catalunya | 2026-04-26 | 2026-10-01 | 2 | --tax`
- `2024-06-01 | rental | Madrid + Barcelona STR licensing freeze (de facto) | Municipal ordinances | 2026-04-26 | 2026-09-01 | 2 | --rental`
- `2024-06-XX | rental | BCN universal HUT expiry — ALL 10,101 HUT licences citywide expire 24 Nov 2028 (day per Ajuntament de Barcelona) (Collboni decree Jun 2024); PEUAT Zone 1 Ciutat Vella + Eixample-stress remain frozen for new HUTs; Zone 2 transferable-only; Zone 4 prohibited | Ajuntament de Barcelona | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-05-01 | rental | Catalonia IEET tourist tax — €7.40/n 1-4★ apartments / €11/n 5★ + Catalonia €4 municipal surcharge rising €1/yr to max €8 by 2029; cap 7 nights; under-16 exempt | Generalitat de Catalunya ATC | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `2018-XX-XX | rental | Madrid PEH Distrito Centro — STR >90 nights/yr classed as commercial use; independent entrance + portal/lift separation from residents required (de-facto STR ban in shared-building residential) | Ayuntamiento de Madrid | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `2026-06-01 | tax | Comunidad Valenciana general ITP cut 10 to 9 percent (immuebles up to 1M euros); 11 percent band above 1M retained (pre-existing); AJD 1.5 to 1.4 percent; reduced rates for habitual home/young/large-family/disability retained (ladder not re-verified — check hisenda.gva.es) | Ley 5/2025 de 30 de mayo (DOGV 31 May 2025; BOE-A-2025-11959) https://www.boe.es/buscar/doc.php?id=BOE-A-2025-11959 | 2026-07-03 | 2026-12-01 | 2 | --tax (ES)`
- `2026-04-22 | rental | Plan Estatal de Vivienda 2026-2030 approved (state housing-aid framework, grants/rebates) supersedes prior state plan | Real Decreto 326/2026 de 22 de abril BOE-A-2026-8872 https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8872 | 2026-07-03 | 2026-12-01 | 3 | --rental (ES)`
- `2026-03-22 | rental | RD-ley 8/2026 (extraordinary 2-yr rental prorroga plus 2 percent annual rent-update cap, in force 22 Mar 2026) NOT convalidated — Congreso derogation published 28 Apr 2026 (BOE-A-2026-9359); no longer available for new requests; prorrogas granted during 22 Mar-28 Apr 2026 validity window remain valid | RD-ley 8/2026 BOE-A-2026-6545 + Resolucion Congreso 28 Apr 2026 BOE-A-2026-9359 https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-9359 | 2026-07-03 | 2027-01-01 | 3 | --rental (ES)`
- `2026-01-01 | work | SMI 2026 set at 1,221 euros/month x 14 = 17,094 euros/yr (plus 3.1 percent vs 2025) | Real Decreto 126/2026 de 18 de febrero BOE-A-2026-3815 https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-3815 | 2026-07-03 | 2027-03-01 | 4 | --work (ES)`

### 🇵🇹 PT

- `2024-03-22 | tax | NHR replaced by IFICI/NHR 2.0 — **pensions NO LONGER exempt** (only specified scientific/innovation activities) | Decreto-Lei 21-A/2024 | 2026-04-26 | 2026-10-01 | 1 | --visa --tax (pension)`
- `2023-10-06 | visa | Golden Visa — residential real estate route closed; funds/research routes remain | Mais Habitação law | 2026-04-26 | 2026-09-01 | 1 | --visa`
- `2024-11-01 | rental | Decree-Law 76/2024 in force 1 Nov 2024 — repealed Mais Habitação AL nationwide freeze and 5-yr renewal requirement; max 27 guests/9 rooms per AL unit (down from 30); municipalities retain "áreas de contenção" power | gov.pt + Diário da República | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2025-12-06 | rental | Lisbon RMAL 2nd alteration (Aviso 29926-A/2025/2, in force 6 Dec 2025): SALE of moradia/apartamento AL in a containment zone = caducidade (auto expiry, NON-TRANSFERABLE) except RJEEAL legal exceptions; absolute threshold cut 20→10%, relative 10→5%. Santa Maria Maior (66.9%) stays absolute; after Feb-2026 insurance cull (6,765 cancelled) São Vicente/Arroios/Estrela dropped to relative (Apr-2026); bairro-level map pending official CML publication | Diário da República Aviso 29926-A/2025/2 (RMAL 2ª alteração) + Câmara Municipal de Lisboa | 2026-07-02 | 2026-10-01 | 1 | --rental`
- `2025-12-06 | rental | SUPERSEDED by RMAL 2nd amendment (Aviso 29926-A/2025/2, in force 6 Dec 2025): old relative-zone 'one-for-one transfer' gone — in BOTH absolute + relative áreas de contenção, transmission of house/apartment-mode AL registration now triggers caducidade. Misericórdia now ABSOLUTE; Príncipe Real/Graça/Bica bairro classification revised — verify Anexo IV. | DR Aviso 29926-A/2025/2 + CM Lisboa RMAL | 2026-07-02 | 2026-10-01 | 1 | --rental`
- `2024-09-XX | rental | Lisbon TMT raised to €4/pp/n (from €2 Sept 2024), cap 7 nights, ≥13 years old | Câmara Municipal de Lisboa | 2026-05-11 | 2026-09-01 | 3 | --rental`
- `2024-12-XX | rental | Porto Áreas de Contenção — Vitória (60.5% pressure), São Nicolau (48.3%), Sé (44.1%), Santo Ildefonso (38.3%), Miragaia (21.8%): containment freeze; Cedofeita (9.8%) reclassified as sustainable-growth (new AL permitted) | Câmara Municipal do Porto | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2024-08-01 | tax | IMT Jovem — buyers aged 35 or under (not an IRS dependent that year; not owner — 3-year lookback per Santander 2026 explainer — of another habitational urban property) buying their first own-permanent-residence urban property pay zero IMT and zero Imposto do Selo up to 330,539 EUR (2026 Continente value; RAs higher, 396,647 EUR; 324,058 in 2025); between 330,539 and 660,982 EUR only the excess is taxed at 8 percent marginal IMT while the IS exemption remains in full; no benefit above 660,982 EUR; one-time; land-for-construction excluded; legal basis Lei 30-A/2024 (20 Jun 2024) plus Decreto-Lei 48-A/2024 (25 Jul 2024); 2026 values per AT Oficio-circulado 40129/2026 (06/01/2026) | Portal das Financas IMT Jovem plus PwC Guia Fiscal 2026 plus ECO | 2026-07-03 | 2027-01-15 | 2 | --tax --finance (PT)`
- `2026-01-01 | tax | OE2026 indexed all IMT brackets up ~2 percent for inflation — HPP exemption threshold 104,261 to 106,346 EUR; top 7.5 percent flat rate now applies above 1,150,853 EUR (was 1,128,287); marginal rates unchanged (2/5/7/8 then 6 and 7.5 flat); AT practical tables per Oficio-circulado 40129/2026 (06/01/2026) | AT Oficio-circulado 40129/2026 plus ECO citing OE2026 proposal plus PwC Guia Fiscal 2026 | 2026-07-03 | 2027-01-15 | 3 | --tax (PT)`
- `2025-02-25 | tax | IFICI (NHR 2.0) regulating Portaria 352/2024-1 amended by Portaria 52-A/2025-1 (DR n.º 39/2025 Supl., Série I, 25 Feb 2025, in force 26 Feb 2025) — purely procedural: adds art. 4/4 routing the inscription request and communication of alterations through the Portal das Finanças (protocol between FCT/AT and the other verifying entities); does NOT change eligible activities or benefits (20 percent flat on qualified PT-source income, foreign-income exemption, 10 years non-renewable, pensions excluded, single-use all unchanged) | DR primary (files.diariodarepublica.pt 1s/2025/02 03901 PDF) plus FCT plus AT Oficio-circulado 20276/2025 | 2026-07-03 | 2027-01-15 | 4 | --visa --tax (PT)`
- `2026-01-01 | work | Salario Minimo Nacional (Continente) raised to 920 EUR per month (from 870) by DL 139/2025, 14 payments (net 818.80 after 11 percent SS); Acores 966 (+5 percent regional rule); Madeira 980 per DLR 1/2026/M de 3 de fevereiro (effects 1 Jan 2026, NOT 968); tripartite accord path 970 in 2027 and 1,020 in 2028 | DGERT plus DL 139/2025 plus DR DLR 1/2026/M plus DECO Proteste | 2026-07-03 | 2027-01-15 | 4 | --work (PT)`
- `2026-05-25 | tax | Non-resident IMT surcharge ENACTED — DL 97/2026 (20 May 2026, authorization Lei 9-A/2026) adds CIMT art. 17/10: flat 7.5 percent IMT, no exemption or reduction, on urban habitational purchases by non-residents; exceptions: PT tax resident per art. 16 CIRS, becomes resident within 2 years (refund), or moderate-rent lease 36+ months within first 5 years; effective-date conflict among professional sources (25 May 2026 per Cuatrecasas 5th-day default vs 1 Sept 2026 per other summaries) — model 7.5 percent now; diploma also extends IMT payment window to 30 days and creates IVA-6-percent-construction / RSAA / CIA / 10-percent-IRS-moderate-rent regimes | DR DL 97/2026 primary plus Cuatrecasas guide plus ECO | 2026-07-03 | 2026-09-15 | 1 | --tax --finance --rental (PT)`

### 🇮🇸 IS

- `2024-XX-XX | rental | STR cap of 90 nights/yr without licence remains; tightened enforcement post-Reykjanes eruptions | Sýslumaður | 2026-04-26 | 2026-10-01 | 3 | --rental`

### 🇸🇪 SE / 🇫🇮 FI / 🇳🇴 NO

- `2024-01-01 | tax | FI varainsiirtovero (transfer tax) reduced 4% → 3% (real estate) and 2% → 1.5% (housing co-op shares) | Vero.fi | 2026-04-26 | 2026-09-01 | 2 | --tax (FI)`

### 🇬🇧 UK

- `2025-04-06 | tax | Non-dom regime abolished, replaced by 4-yr FIG (Foreign Income & Gains) regime | HMRC | 2026-04-26 | 2026-09-01 | 2 | --tax --visa`
- `2025-04-01 | tax | SDLT additional dwelling supplement increased 3% → 5% | HMRC | 2026-04-26 | 2026-10-01 | 2 | --tax`
- `2028-04-01 | tax | High Value Council Tax Surcharge ("mansion tax") announced Autumn Budget 2025 — annual owner-paid charge on England homes valued (2026 prices) over 2M GBP; four bands 2,500 / 3,500 / 5,000 / 7,500 GBP, CPI-uprated; VOA targeted valuation exercise 2026; implementation details under consultation, not yet legislated | gov.uk HVCTS consultation — https://www.gov.uk/government/consultations/high-value-council-tax-surcharge/high-value-council-tax-surcharge | 2026-07-03 | 2026-12-01 | 2 | --tax --home-tax (UK)`
- `2027-04-06 | tax | Property income tax rates rise 2pp above main rates (basic 22 / higher 42 / additional 47 percent) for 2027-28 onward; finance-cost relief rises to 22 percent — Autumn Budget 2025 | gov.uk Change to tax rates for property savings and dividend income technical note | 2026-07-03 | 2027-01-01 | 2 | --rental --tax (UK)`
- `2026-05-01 | rental | Renters' Rights Act 2025 main commencement (SI 2026/421 reg 2(a)) — Section 21 no-fault evictions abolished 1 May 2026 (big-bang; existing ASTs converted to assured periodic tenancies); possession claims on pre-commencement s21 notices must be issued by the earlier of 6 months from service or 31 July 2026; remaining provisions commence in later phases (MHCLG roadmap) | legislation.gov.uk SI 2026/421 — https://www.legislation.gov.uk/uksi/2026/421/contents/made | 2026-07-03 | 2026-10-01 | 1 | --rental (UK)`
- `2026-01-27 | leasehold | Draft Commonhold and Leasehold Reform Bill published for pre-legislative scrutiny (Written Statement HCWS1278); final Bill due Autumn 2026 (Royal Assent aim mid-2027) — caps existing-flat ground rents at 250 GBP per year (peppercorn transition unsettled: govt draft ~40yr vs Committee ~20yr + late-2027 commencement), commonhold default on collective enfranchisement, new managing-agent regulator; LAFRA 2024 valuation reforms incl. marriage-value abolition still uncommenced (JR dismissed High Court 24 Oct 2025, appeal permitted) | House of Commons Library CBP-10653 | 2026-07-03 | 2026-11-01 | 2 | --price --tax (UK)`
- `2030-10-01 | rental | MEES PRS England — EPC C by single date 1 Oct 2030 (new and existing tenancies; Warm Homes Plan / DESNZ response 21 Jan 2026); cost cap 10,000 GBP (exemption valid 10 yrs; qualifying spend since 1 Oct 2025 counts); Property Value Adjustment exemption for homes valued under 100k GBP (cap = lower of 10k or 10 pct of value); pre-1 Oct 2029 EPC C (EER) stays compliant until EPC expiry, then Home Energy Model dual-metric standard | gov.uk DESNZ PRS consultation response — https://www.gov.uk/government/consultations/improving-the-energy-performance-of-privately-rented-homes-2025-update | 2026-07-03 | 2026-12-01 | 2 | --rental --risks (UK)`

### 🇮🇪 IE

- `2026-03-01 | rental | RPZ replaced by permanent nationwide rent control. Residential Tenancies (Amendment) Act 2025 extended RPZ nationwide from 20 Jun 2025; from 1 Mar 2026 (Residential Tenancies (Miscellaneous Provisions) Act 2026) all private + student-specific tenancies capped at 2 percent or CPI whichever lower. New-build apartments (construction commenced after 10 Jun 2025) exempt from 2 percent cap, CPI-linked only. New tenancies run 6-year minimum duration; market reset only at new tenancy start (not after no-fault) or end of 6-year cycle. Large landlords (4-plus tenancies or a company) barred from no-fault evictions. | RTB rental-law-changes-from-1-March-2026 + Residential Tenancies (Miscellaneous Provisions) Act 2026 (No. 3 of 2026, enacted 24 Feb 2026, irishstatutebook.ie) + RT(A) Act 2025 (oireachtas.ie bill 2025/35) | 2026-07-03 | 2026-12-01 | 1 | --rental (IE)`
- `2025-10-08 | tax | VAT on sale of completed apartments cut 13.5 to 9 percent, temporary 8 Oct 2025 to 31 Dec 2030 (Budget 2026). Houses stay 13.5 percent. Budget 2026 also announced apartment-construction corporation-tax reliefs (enhanced deduction + cost-rental exemption — per Citizens Information; verify figures at Revenue before citing). | Citizens Information Budget 2026 + Revenue | 2026-07-03 | 2026-12-01 | 2 | --tax --price (IE)`
- `2026-01-01 | tax | LPT 2026-2030 cycle live. Valuation date 1 Nov 2025; base rate 0.0906 percent; bands widened 20 percent; Band 1 to 5 charges 95/235/333/428/523 euro; above 2.1M 0.0906 percent first 1.26M + 0.25 percent to 2.1M + 0.30 percent above; Local Adjustment Factor plus or minus 15 percent. | Revenue.ie LPT valuation bands and rates | 2026-07-03 | 2027-01-01 | 2 | --tax (IE)`
- `2024-11-01 | tax | Vacant Homes Tax raised to 7x base LPT (Finance Act 2024) for chargeable periods from 1 Nov 2024 onward, was 5x (2023-24) and 3x (2022-23). Charged where dwelling occupied under 30 days in the 12-month period; separate from LPT. | Revenue.ie Vacant Homes Tax rate | 2026-07-03 | 2027-01-01 | 2 | --tax (IE)`
- `2024-10-02 | tax | Residential stamp duty bulk-purchase rate raised 10 to 15 percent for 10-plus residential properties (apartments excluded, s.31E SDCA 1999) in 12 months; top marginal residential rate 6 percent above 1.5M; both from instruments executed on or after 2 Oct 2024. Commercial 7.5 percent unchanged since 9 Oct 2019. | Revenue.ie stamp duty rates | 2026-07-03 | 2027-01-01 | 2 | --tax (IE)`
- `2027-01-01 | tax | New Derelict Property Tax (announced Budget 2026; government approved plans Jun 2026) to replace local-authority Derelict Sites Levy (7 percent of market value, widely uncollected). New tax at least 7 percent of market value, self-assessed, Revenue-collected; initial scope 107 urban areas with population over 4,000 (approx 19,000 properties); preliminary derelict-property list to be published 2027; not in force before 2027. | gov.ie Derelict property tax publication + Citizens Information Budget 2026 | 2026-07-03 | 2027-01-01 | 3 | --tax (IE)`
- `2026-01-01 | work | National minimum wage up 65 cent to 14.15 euro per hour from 1 Jan 2026 (was 13.50 in 2025). | gov.ie (DETE) National Minimum Wage increase 1 Jan 2026 | 2026-07-03 | 2027-01-01 | 3 | --work (IE)`
- `2026-01-01 | tax | Mortgage Interest Tax Credit extended to 2026 (tapering); relief on interest increase vs 2022, 2025 max 1,250 euro per property, 2026 max 625 euro per property. Rent Tax Credit (1,000 single / 2,000 joint) extended to end 2028. | Revenue.ie rent-credit (RTC 2022-2028, 1,000/2,000) + Citizens Information Budget 2026 (MITC) | 2026-07-03 | 2027-01-01 | 3 | --tax (IE)`

### 🇯🇪 JE

- `2024-08-01 | rental | Rented Dwellings Licensing Law 2023 mandatory enforcement begins | gov.je | 2026-05-27 | 2026-11-01 | 2 | --rental --notary (JE)`
- `2026-01-01 | tax | Mandatory independent taxation for all married couples including HVRs (Comptroller of Revenue HVR page explicit) | gov.je/taxesmoney | 2026-05-27 | 2026-09-01 | 2 | --tax --home-tax (JE)`
- `2026-01-01 | tax | 2026 Budget (P.93/2025) ADOPTED — higher rate of Stamp Duty / LTT / EPTT for 2026 reduced to +2pp above standard rate (from +3pp), one-year measure, reverts to +3pp from 2027; enacted position confirmed on the gov.je 2026 budget tax summary | gov.je 2026 budget tax summary + States Assembly P.93/2025 | 2026-07-02 | 2027-01-05 | 2 | --tax --finance (JE)`
- `2026-02-26 (REJECTED — P.19/2026) | visa | HVR (2(1)(e)) statutory cap proposal (15/yr on rolling 5-yr basis = 75 per 5-yr) DEBATED AND REJECTED by States Assembly 26 Feb 2026 — no cap enacted; 15/yr remains a non-binding aspiration. Proposer Dep. Renouf now Infrastructure Min. after Jun 2026 election; new govt signalled residential-status review — may revive | States Assembly | 2026-07-02 | 2026-10-01 | 3 | --visa --foreign-buyer (JE)`
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
- `2026-07-15 | visa | EU-UK Gibraltar Treaty PROVISIONALLY APPLIED since 15 Jul 2026 (Art. 336; ratification pending — EP consent expected autumn 2026 + UK CRAG): land-frontier immigration checks + barriers removed, dual Schengen checks at Gibraltar airport/port (Spanish officials for Schengen integrity), residents exempt EES/ETIAS/wet-stamping; Gibraltar immigration/residency law UNCHANGED (press 148/2026) though residence-permit approval gains an EU-facing coordination step (FCDO summary s.14) | Consilium 01 Apr 2026 + FCDO summary + HMGoG PR 148/234/517/2026 | 2026-07-02 | 2026-10-15 | 1 | --visa --foreign-buyer --remote (GI)`
- `2026-06-17 (announced — regulations pending) | visa | Residence Criteria framework announced (HMGoG press 466/2026): residency to require genuine economic contribution + regulatory compliance; residence alone does not grant social benefits reserved for Gibraltarian Status; new residence legislation published ahead of 15 Jul 2026 per HMGoG treaty portal; earlier community signal (r/gibraltar 1tkeoa5, was tier-4 anecdotal) now primary-confirmed in direction — Cat-2/HEPSS-specific changes still unconfirmed (law-firm secondary only) | HMGoG PR 466/2026 + treaty-gov.info | 2026-07-02 | 2026-10-01 | 2 | --visa (GI)`

### 🇨🇭 CH

- `2029-01-01 (fixed 1 Apr 2026) | tax | Eigenmietwert abolition — vote 28 Sep 2025 (57.7% YES); Federal Council FIXED entry-into-force at 1 Jan 2029 at its 1 Apr 2026 session (2028 no longer possible); cantons may introduce Objektsteuer on Zweitliegenschaften simultaneously; owner-occupied Unterhaltskosten + federal energy deductions drop, Ersterwerberabzug for first-time buyers | admin.ch Medienmitteilung 1 Apr 2026 | 2026-07-03 | 2027-01-01 | 2 | --tax (CH)`
- `2026-04-15 (consultation to 2026-07-15; not enacted) | rental foreign-buyer | Federal Council opened Vernehmlassung to tighten Lex Koller (BewG) — third-country nationals permit-liable for main residences (duty to sell within 2 yrs of moving away), holiday-home purchases restricted, business real estate barred if intended for rent/lease (own-use stays free), new ban on foreign acquisition of listed housing-company shares and regularly-traded real-estate fund/SICAV units; accompanying measure adopted Jan 2025 alongside Federal Council's recommendation to reject the Keine-10-Millionen-Schweiz initiative (initiative vote still pending) | admin.ch Medienmitteilung 15 Apr 2026 + bj.admin.ch Revision Lex Koller | 2026-07-03 | 2026-08-01 | 2 | --rental --visa --foreign-buyer (CH)`
- `2028 (earliest; popular vote expected 2026-11-29, per BSV) | tax | Planned VAT increase to part-fund 13th AHV pension — Parliament final vote 19 Jun 2026 (both chambers): standard 8.1 to 8.5 pct, accommodation special rate 3.8 to 4.0 pct, reduced 2.6 pct unchanged; subject to mandatory popular vote; unlikely in force before 2028 | bsv.admin.ch umsetzung-13-ahv-rente (19 Jun 2026) | 2026-07-03 | 2026-12-01 | 3 | --tax (CH)`
- `2026-06-18 | finance | SNB policy rate held at 0 pct (18 Jun 2026 assessment; unchanged); sight-deposit discount above threshold 0.25 pp — mortgage/SARON base near zero | snb.ch monetary policy assessment 18 Jun 2026 | 2026-07-03 | 2026-09-25 | 3 | --finance (CH)`

### 🇩🇪 DE

- `2025-01-01 | tax | Grundsteuer reform live; BFH held Bundesmodell verfassungskonform (judgments 12 Nov 2025, Az. II R 25/24 + II R 31/24 + II R 3/25, PM 10 Dec 2025) and BW Bodenwertmodell verfassungsgemaess (20 May 2026, II R 26/24 + II R 27/24); Verfassungsbeschwerde vs Bundesmodell PENDING at BVerfG (Az. 1 BvR 472/26, BdSt + Haus & Grund); VG Gelsenkirchen (4 Dec 2025, Az. 5 K 2074/25 u.a.) struck down split Grundsteuer-B Hebesaetze in Bochum/Essen/Dortmund/Gelsenkirchen — not final, appeals to OVG NRW/BVerwG opened | BFH PM 78/25 + VG Gelsenkirchen PM 04.12.2025 + LTO + BDO | 2026-07-03 | 2026-12-01 | 2 | --tax`
- `2026-11-01 (target) | energy | GEG Heizungsgesetz to be replaced by Gebaeudemodernisierungsgesetz (GModG/GMG) — 65% renewable-for-new-heating rule to be dropped for technology-open Bio-Treppe rising CO2-neutral fuel quota on new gas/oil heating (10% 2029, 15% 2030, 30% 2035, 60% 2040); Kabinettsbeschluss 13 May 2026, in-force target 1 Nov 2026, STILL DRAFT in parliament — GEG-2024 65% rule remains in force until then | Bundesregierung.de Kabinettsbeschluss + ADAC | 2026-07-03 | 2026-11-01 | 2 | --risks --tax`
- `2024-01-01 | subsidy | Heizungstausch/Waermepumpe grant (up to 70%, cap 30k EUR, max 21k EUR per Wohneinheit) administered by KfW programme 458 via Meine-KfW portal, moved from BAFA to KfW in 2024; funding pledged stable to at least 2029 | KfW 458 + Finanztip + ADAC | 2026-07-03 | 2027-01-05 | 3 | --tax`
- `2025-07-23 | rental | Mietpreisbremse extended to 31 Dec 2029, law in force 23 Jul 2025; cap unchanged at max 110% local Mietspiegel for new lets | Bundestag textarchiv kw26 + BMJV + Mieterbund | 2026-07-03 | 2029-01-05 | 3 | --rental`
- `2026-05-20 | rental | EU Reg 2024/1028 STR data-sharing applies from 20 May 2026; German transposition KVDG (Kurzzeitvermietung-Datenaustausch-Gesetz) ENACTED — Bundestag 23 Apr 2026, Bundesrat 8 May 2026, promulgated 18 May 2026 (BGBl. 2026 I Nr. 138); Bundesnetzagentur = single digital entry point platform-Kommune; opt-in regime — listing registration-number duty bites only where the Kommune runs an EU-compliant register | Bundestag textarchiv kw17-2026 + BGBl. 2026 I Nr. 138 + BMWE | 2026-07-03 | 2027-01-05 | 2 | --rental`

### 🇦🇹 AT

- `2024-XX-XX | tax | Tirol/Salzburg/Vorarlberg foreign-buyer quotas tightened (annual review) | Land governments | 2026-04-26 | 2026-09-01 | 2 | --tax (ownership)`
- `2026-01-01 | rental | Mieten-Wertsicherungsgesetz (MieWeG) via 5. Mietrechtliches Inflationslinderungsgesetz (5. MILG) in force 1 Jan 2026 (Nationalrat 11 Dec 2025) — caps existing contractual Wertsicherungsklauseln only (creates no adjustment right): regulated MRG residential capped 1% (2026) / 2% (2027); from 2028 index-linked residential contracts in multi-unit buildings incl. free-market rents pass on only half of any inflation portion above 3%; adjustment once/yr, earliest 1 April (Richtwert increases eff. 1 May); Ein-/Zweifamilienhäuser + WGG/Genossenschaft (own regime) excluded. Richtwert Wien eff. 1 Apr 2026 = EUR 6.74/m2 (from 6.67) | Parlament Österreich XXVIII SNME 1677 + RIS Gesetzesnummer 20013068 + WKO 5.-MILG note + Arbeiterkammer Mietpreisbremse | 2026-07-03 | 2027-01-15 | 1 | --rental --tax (AT)`
- `2026-06-30 (EXPIRED) | tax | Grundbuch-Eintragungsgebühr Hauptwohnsitz-Befreiung LAPSED — the 1 Jul 2024 to 30 Jun 2026 waiver of the 1.1% Eintragungsgebühr + 1.2% Pfandrechts-Eintragungsgebühr up to EUR 500,000 Bemessungsgrundlage for a primary-residence purchase ended (application had to reach the Grundbuch by 1 Jul 2026); no extension enacted or planned by the federal government (May 2026); standard 1.1% + 1.2% fees apply again | BMJ Befreiung-von-der-Grundbuch-Eintragungsgebuehr page | 2026-07-03 | 2026-10-01 | 1 | --tax (AT)`
- `2025-07-01 | finance | KIM-Verordnung (mortgage-lending caps) expired 30 Jun 2025 — OeNB found no remaining systemic risk so no legal basis to extend; replaced 1 Jul 2025 by the FMA WIK-Rundschreiben (published 26 Jun 2025), a NON-binding supervisory expectation keeping the same three benchmarks: max 90% loan-to-value, max 40% debt-service-to-income, max 35-year term; banks largely retain them in internal risk policy | FMA (fma.gv.at Wohnimmobilienkredite + KIM-V-Ende press release) + OeNB | 2026-07-03 | 2026-12-01 | 2 | --finance (AT)`
- `2025-07-01 | tax | 2025 Budgetbegleitgesetz real-estate package in force 1 Jul 2025 — GrESt share-deal Anteilsvereinigung threshold cut 95% to 75% with observation period extended 5 to 7 years and 3.5% on gemeiner Wert (fair-market value) for share transfers; ImmoESt 30% Umwidmungszuschlag surcharge added for re-zoned properties. Stufentarif Familienverband (0.5/2.0/3.5%) and 3.5% flat GrESt unchanged | BMF Grunderwerbsteuer Steuersatz + USP + DLA Piper/Wolf Theiss FA-2025 reviews | 2026-07-03 | 2026-12-01 | 2 | --tax (AT)`
- `2026-05-20 | rental | EU Reg 2024/1028 (STR data-collection) — Austria has NOT opted in: BMWET confirms the STR-VO is implemented in no Bundesland as of the 20 May 2026 start ("vorerst"); no national STR registration-number regime; individual Länder may opt in later (BMWET building the Single Digital Entry Point); short-let governed instead by each Land Bauordnung (Wien: 90-day platform cap, permit above, up to EUR 50,000 fine) | BMWET STR-VO page (bmwet.gv.at) + EUR-Lex 32024R1028 | 2026-07-03 | 2026-11-01 | 2 | --rental (AT)`

### 🇳🇱 NL

- `2025-01-01 | rental | Affordable Rent Act (Wet betaalbare huur) — points-based cap extended to mid-segment; affects rental yield | Rijksoverheid | 2026-04-26 | 2026-09-01 | 1 | --rental`
- `2026-04-01 | rental | Amsterdam vakantieverhuur 30→15-night cap IN FORCE since 1 Apr 2026 in 8 wijken (7 Centrum + Oude Pijp, Zuid) — Eerste aanwijzingsbesluit 15-nachtencriterium (Gemeenteblad 2026 nr.151001), enabled by Huisvestingsverordening escalatieladder eff. 1 Jan 2026, finalized 24 Mar 2026; ~€73 permit + 12.5% tourist tax; full ban possible if halving fails | Gemeente Amsterdam (Gemeenteblad 2026 nr.151001) | 2026-07-02 | 2026-10-01 | 1 | --rental`
- `2026 transitional → ~2028 structural | tax | Box 3 — tax year 2026 STILL on the forfaitaire (notional-yield) basis WITH the tegenbewijsregeling (pay tax on actual return if lower than the forfait; refund route live since 1 Jul 2025; 2026 heffingvrij vermogen EUR 59,357 pp, beleggingen forfait 6.00%, savings 1.28% provisional, 36% rate). The structural Wet werkelijk rendement (actual-return, wetsvoorstel 36.748) PASSED the Tweede Kamer 12 Feb 2026 but is STILL PENDING in the Eerste Kamer — targeted ~1 Jan 2028, NOT yet in force (do not assert actual-return is live before then) | Belastingdienst + Eerste Kamer 36748 `https://www.eerstekamer.nl/wetsvoorstel/36748_wet_werkelijk_rendement_box` | 2026-06-14 | 2026-09-15 | 1 | --tax`
- `2028-01-01 (pending) | tax | Wet werkelijk rendement box 3 — permanent actual-return capital tax (interest/dividend/rent taxed yearly) replacing the notional-yield system; passed Tweede Kamer 12 Feb 2026, intended eff. 1 Jan 2028. Eerste Kamer passage NOT yet secured — Minister of Finance has flagged necessary amendments + Senate-rejection risk, so the 1 Jan 2028 date is not certain | Belastingdienst (actual return) https://www.belastingdienst.nl/wps/wcm/connect/en/income-in-box-3/content/what-is-my-actual-return + Deloitte NL (Tweede Kamer adoption 12 Feb 2026) | 2026-05-28 | 2026-09-01 | 2 | --tax --home-tax`
- `proposed (Kamerbrief 10 Apr 2025; ontwerpbesluit voorhang in both Kamers 1 Oct 2025, extended to 18 Nov 2025; next Raad van State advice — NOT enacted; caretaker cabinet) | rental | Wet betaalbare huur optimisation package to stem rental sell-off — (1) WOZ-prijsopslag: homes hit by the WOZ-cap (WOZ capped at 33% of WWS points) may charge the pre-cap maximum price at new contracts without leaving regulation, (2) absence of outdoor space no longer a WWS minus (was -5 pts; ~€33/mo at new contracts, ministry estimate), (3) small rijksmonumenten weighted heavier (€40-70/mo at new contracts, ministry estimate), (4) all students eligible for one-time temporary contracts, (5) tijdelijke nieuwbouwopslag middenhuur extended 4 years (added in 2026 Kamerbrief); full Wet betaalbare huur evaluation due H1 2027; Kadaster (per Kamerstuk 36 496 nr. 74): ~29,400 net rental homes uitgepond within existing private stock in 2024, private rental market net -413 homes vs 2023 | [Rijksoverheid 10 Apr 2025 Maatregelen voor behoud middenhuurwoningen](https://www.rijksoverheid.nl/actueel/nieuws/2025/04/10/maatregelen-voor-behoud-middenhuurwoningen) + Eerste Kamer voorhang brief 1 Oct 2025 | 2026-07-03 | 2026-12-01 | 2 | --rental --price (NL)`

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
- `2025-01-01 | rental | Athens 1st/2nd/3rd Districts AMA freeze — no new STR registrations 1 Jan 2025–31 Dec 2026; pre-2024-12-31 hosts continue (two-tier market). STAMA + a 3rd-district owner filed a Council of State annulment petition Mar 2026 (no ruling as of Jul 2026). Reported from ~1 Jul 2026 (omnibus bill, enactment not independently confirmed): sale/donation/parental transfer of an AMA property in the frozen zones deletes its AMA so new owner loses STR right — contested by POMIDA + STAMA; inheritance treatment DISPUTED across sources (Jan ANA report: inheritance also deletes AMA; GCT 23 Jun 2026: inheritance exempt) | JMD Min. Finance/Development/Tourism; eKathimerini + news.gtp.gr + BnBNews + Greek City Times | 2026-07-02 | 2026-10-01 | 1 | --rental`
- `2025-10-01 | rental | National STR property standards in force 1 Oct 2025 under Law 5170/2025 Art. 3 (ΦΕΚ Α' 6), for AMA-registered STR per Art. 111 Law 4446/2016; requires civil-liability insurance, electrician safety decl., fire extinguisher, smoke detectors, RCD/escape signage, pest-control + first-aid; via Min. Tourism circular 19231/19.09.2025; fines €5k→€10k→€20k | Greek Ministry of Tourism + AADE | 2026-07-02 | 2027-01-05 | 2 | --rental`
- `2026-04 proposed; JMD signature targeted end-Jun 2026, NOT signed as of 1 Jun 2026 | rental | Cyclades 20-30% tourist-bed cut + STR/Airbnb conversion freeze in saturated red-zone islands (Mykonos/Santorini et al.) — provisions of the DRAFT Special Spatial Framework for Tourism (JMD by Tourism Min. Kefalogianni + Environment Min. Papastavrou); public consultation closed late May 2026; STILL UNENACTED — do NOT assert any live bed-cap or Mykonos STR freeze until the JMD is gazetted | Greek Ministry of Tourism / news.gtp.gr `https://news.gtp.gr/2026/05/26/ellet-calls-for-stricter-limits-in-greeces-revised-tourism-spatial-framework/` | 2026-06-14 | 2026-07-07 | 1 | --rental`
- `2024-04-05 | visa | Golden Visa properties acquired under the post-Law-5100/2024 regime may not be short-let or sub-let; breach → residence-permit revocation + €50,000 administrative fine on owners/holders (Law 5100/2024 Art. 64, adding para 7A to Art. 100 of Immigration Code Law 5038/2023). Ministry of Migration Circular 1/2026 (22 Apr 2026, 31 pp., SG K. Papakosta) narrowed scope: banned = lettings under 60 days without services beyond accommodation + bed linen; pre-reform-threshold and transitional-window acquisitions exempt; long-term and hotel-type-with-services leases permitted; sham/cash-back deals referred to AADE + Hellenic AML Authority | varnavas.gr + wfw.com + imidaily.com + high-net-worth-immigration.com | 2026-07-03 | 2026-12-01 | 1 | --visa --rental (GR)`
- `2026-04-01 | labour | Statutory minimum wage raised from €880 to €920 gross/month (+4.55%) by Ministerial Decision 8934/27.3.2026 (ΦΕΚ Β΄ 1759); blue-collar daily wage €39.30 → €41.09; government-stated target €950 by 2027 (news-tier) | ypergasias.gov.gr (primary) + bernitsaslaw.com + mondaq.com | 2026-07-03 | 2027-04-01 | 3 | --work (GR)`
- `2027-01-01 | tax | ENFIA for primary homes in villages under 1,500 residents — already cut 50% in 2026 (legislated, Law 5246/2025) — is announced for full abolition from 2027 (89th Thessaloniki International Fair, Sept 2025); 2027 abolition NOT yet verified as gazetted, revisit in the 2027 budget cycle. Qualifiers: main residence of GR tax residents, taxable value ≤ €400k, settlement ≤1,500 pop (Evros threshold 1,700) | elxis.com + ekathimerini.com + taxsummaries.pwc.com | 2026-07-03 | 2026-11-01 | 2 | --tax (GR)`

### 🇭🇺 HU

- `2026-01-01 | rental | Budapest District VI (Terézváros) STR zero-day cap — Decree 26/2024 (X.31), referendum 2-15 Sep 2024 (20.52% turnout, 54% in favor), upheld by Hungarian Supreme Court; STR allowable days/yr = ZERO in force since 1 Jan 2026; enforcement live from Jan 2026 (police + NAV inspections, fines to several million HUF); hotels/guesthouses exempt | Terézváros + hungarytoday.hu | 2026-07-02 | 2027-01-05 | 1 | --rental`
- `2025-09-25 | rental | Budapest District VII (Erzsébetváros) two-stage STR crackdown. Building decree 33/2025 (IX.24, amends 25/2018 XII.21) in force 25 Sept 2025 caps NEW commercial accommodation at 10% of a building's residential floor area, ground-floor only, min room sizes + en-suite bath per room, guesthouses ≥6 rooms; existing permits exempt. THEN decree 46/2025 (XII.10) sets STR usable days/yr to ZERO from 1 Jan 2026 UNLESS a condominium (társasház) agreement exists (then 365) — same zero-day mechanism as District VI, with a condo-consent carve-out; units registered by 31 Dec 2025 must file the társasház agreement by 31 Dec 2026. Budapest-wide STR-registration moratorium runs 1 Jan 2025–31 Dec 2026 | Erzsébetváros decrees 33/2025 (IX.24) + 46/2025 (XII.10) via net.jogtar.hu + Airbnb Hungary Help Center | 2026-07-02 | 2026-10-01 | 1 | --rental`
- `2024-01-01 | rental | Airbnb flat tax per room quadrupled in 2024 (~+290%) | NAV | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`

### 🇪🇪 EE

- `2024-01-01 | tax | Land tax indexation cap raised 10% → 50% annual change | Maksu- ja Tolliamet | 2026-04-26 | 2026-10-01 | 3 | --tax`
- `2025-01-01 | tax | Income tax 20% → 22% (touches rental income) | Maksu- ja Tolliamet | 2026-04-26 | 2026-09-01 | 2 | --tax --rental`
- `2026-05-20 | rental | EU Reg 2024/1028 STR data-collection in force EU-wide 20 May 2026 (registration number + platform data-sharing; local caps stay national). No Estonian national mandatory STR-registration regime confirmed pre-2026; prior Jul-2025 date + Police/Border-Guard 24h guest-report claim unverified. MKM only now proposing clearer Tourism Act rules, targeted 2027-2028; Tallinn Old Town cap still just proposed (2025-2035 dev plan, not enacted) | EUR-Lex Reg (EU) 2024/1028 + Estonian MKM + ERR News | 2026-07-02 | 2026-10-01 | 2 | --rental`

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

- `2025-04-01 → 2029-06-30 | ownership | Established-homes ban on foreign purchase EXTENDED in 2026-27 Federal Budget from original 31 Mar 2027 sunset to 30 Jun 2029 (implemented via FIRB screening policy; ATO operative guidance already states the 2029 window); limited exceptions unchanged in kind — housing-supply-increasing investments; existing exemptions preserved incl. PR, NZ citizens, and joint-tenant purchases with an AU-citizen / PR / NZ-citizen spouse | ATO + foreigninvestment.gov.au | 2026-07-03 | 2027-01-05 | 1 | --tax (ownership)`
- `2024-07-31 | visa | SIV (Significant Investor Visa) closed | Home Affairs | 2026-04-26 | 2026-09-01 | 1 | --visa`
- `2025-01-01 | rental | VIC Short Stay Levy 7.5% on total booking fee for stays <28 days; principal-residence + hotels exempt; 25% of revenue to regional VIC for social/affordable housing | State Revenue Office VIC | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `ongoing | rental | NSW STRA Code of Conduct — STRA Register $65; Greater Sydney 180-day non-hosted cap (Eastern Harbour / Central River / Western Parkland districts); fines up to $1.1M (corp) / $220k (individual) | NSW Planning + Fair Trading | 2026-05-11 | 2026-09-01 | 1 | --rental`
- `2024-09-23 | rental | NSW Byron Shire 60-day non-hosted cap (most LGA), via Housing SEPP; max 12-mo transition period complete Sep 2025 — cap now fully in force; 365-day mapped precincts only in Byron Bay Town Centre + Brunswick Heads carve-outs; hosted STRA unaffected (365 days) | NSW Planning | 2026-07-02 | 2027-01-05 | 1 | --rental`
- `2026-07-01 | tax | FIRB residential application fees re-indexed for FY2026-27 (fees update each 1 Jul; FY26-27 schedule applies to applications 1 Jul 2026 - 30 Jun 2027); FY25-26 reference points: new-dwelling/vacant-land application ~$15,100 per $1M-of-consideration tier, property-developer New/near-new dwelling exemption-certificate initial fee $65,200; FY26-27 amounts in Schedule of Fees PDF on FIRB fees page — verify there; annual vacancy fee 2x application fee (unchanged) | foreigninvestment.gov.au Fees page (updated 1 Jul 2026) + ATO residential fees page | 2026-07-03 | 2027-07-01 | 3 | --tax`
- `2025-01-01 | tax | NSW surcharge purchaser duty raised 8% to 9% for foreign persons (surcharge land tax also applies); rate continues in 2026, no 2026-27-Budget change | Revenue NSW | 2026-07-03 | 2027-01-05 | 2 | --tax`

### 🇳🇿 NZ

- `2018-10-22 | ownership | Overseas Investment Amendment Act — permanent ban on foreign purchase of existing residential | LINZ | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`
- `2024-07-01 | tax | Bright-line test reduced 10 yr → 2 yr | IRD | 2026-04-26 | 2026-10-01 | 2 | --tax`
- `2024-04-01 | rental | Marketplace GST 15% collected by Airbnb / Bachcare on behalf of all hosts (even <NZD 60k/yr); 8.5% flat-rate credit for non-GST-registered hosts | IRD | 2026-05-11 | 2026-09-01 | 1 | --rental --tax`
- `ongoing | rental | Auckland APTR (Accommodation Provider Targeted Rate) — STR >28 nights/yr triggers commercial-rated uplift; Supreme Court validated 2022; declaration deadline 3 Jul annual | Auckland Council | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`
- `ongoing | rental | Queenstown Lakes District 90 nights/yr whole-house cap without resource consent + 25% rates uplift on registered properties | QLDC | 2026-05-11 | 2026-09-01 | 1 | --rental`

### 🇲🇽 MX

- `ongoing | ownership | Fideicomiso (bank trust) required within 50 km coast / 100 km border for foreign buyers | SRE | 2026-04-26 | 2027-01-01 | 1 | --tax (ownership)`
- `2024-04-04 | rental | CDMX Tourism Law Reform (Gaceta 4 Apr 2024, not 2022) + Reglamento 25 Sep / Oct 2024: 50% ANNUAL OCCUPANCY CAP (Art 61 Sexies) on platform STR — non-renewal of registro + 1-yr re-registration bar if exceeded; social-housing (Art 36 Bis Ley de Vivienda) + post-2017 quake reconstruction (Art 22) barred from STR. UPDATE 2026: mandatory host + platform Padrón went LIVE (Gaceta CDMX 22 May 2026, pre-World Cup) — register for folio by ~20-21 Jun 2026 or barred from operating; 50% cap itself contested — Airbnb + host amparos, suspensión definitiva in some cases so cap not applied pending trials (El País 9 Jul 2025) | Congreso CDMX + Gaceta Oficial CDMX + Jefatura de Gobierno CDMX + El País | 2026-07-02 | 2026-10-01 | 1 | --rental`
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
- `2026-01-17 | visa | Investor residency — amendments to Zakon o strancima (Sl. list CG 003/26, publ. 9 Jan 2026) adopted Parliament 31 Dec 2025, in force 17 Jan 2026; €150k min tax-assessed property value (Art 56 transfer-tax base, not purchase price; EU/EEA/CH exempt); 50% min ownership share; 1-yr renewable temp → permanent at 5 yrs → citizenship at 10 yrs; pre-17-Jan-2026 property residents grandfathered | Sl. list CG 003/26 + IMI Daily | 2026-07-02 | 2027-01-05 | 1 | --visa`

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
- `ongoing | rental | Miami Beach STR restriction IN FORCE + enforced (City 'Practice Safe Renting' page, © 2026): Code Ch.142 §142-1111 bars rentals under 6 months + 1 day in single-family + many multifamily residential zones; Business Tax Receipt required to operate legally; violators evicted + fined. CORRECTION: prior entry is a phantom — NO Aug-2025 Miami-Dade ruling struck the ban. Real event = Nichols v City of Miami Beach (Judge Hanzman, Oct 2019), affirmed by 3d DCA Jul 2020 — struck the escalating $20k→$100k fine schedule for exceeding FL §162.09 code-fine caps ($1k first / $5k repeat / $15k irreparable, per day); appeal already decided, NOT pending. Current fine amount reported inconsistently by 2025–26 aggregators (state-cap $1k–$5k/day vs. $20k+) — verify with City. Source note: Goldwater + natlawreview read the 2020 ruling as voiding the prohibition entirely, but the City's 2026 page + Avalara show the restriction still enforced (primary source controls) | City of Miami Beach 'Practice Safe Renting' apps.miamibeachfl.gov + Nichols v City of Miami Beach 3d DCA Jul 2020 (Avalara MyLodgeTax) + Fla. Stat. §162.09 | 2026-07-02 | 2027-01-05 | 1 | --rental`
- `2022-10-23 → 2025-09-30 | rental | Bill 41 / Ord 22-7 (eff 23 Oct 2022) raised STR min stay 30→90 days outside resort zones; HILSTRA v. Honolulu injunctions (Watson: prelim 13 Oct 2022, permanent 21 Dec 2023) grandfather 30-89-day rentals lawfully operating at the 23 Oct 2022 effective date. Ord 25-2 / CO 25-02 (signed 3 Jan 2025, eff 30 Sep 2025) re-enacted 90-day min, no carve-outs; DPP still enforces only <30-day standard | Honolulu Board of REALTORS STR Update Apr 2025 + HILSTRA v Honolulu MSJ order 21 Dec 2023 + Hawaii Living | 2026-07-02 | 2026-10-01 | 2 | --rental`
- `ongoing | rental | LA Home-Sharing Ordinance (HSO, Ord 185,931) — 120-day cap primary residence only, registration mandatory, enforcement since Nov 1 2019 | LA Planning | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `ongoing | rental | SF 90-day unhosted cap; STR registration mandatory; Planning Dept enforcement | SF Planning + STR Office | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `2024-12-09 | risks | CFIUS 31 CFR Part 802 added 59 sites near military installations (foreign-buyer review) | Treasury OFAC | 2026-05-01 | 2026-11-01 | 2 | --risks --visa`
- `2024-10 | mains | EPA Lead and Copper Rule Improvements (LCRI) — full lead-service-line replacement compliance 1 Nov 2027 | EPA | 2026-05-01 | 2026-11-01 | 2 | --mains`
- `2025-09-01 | tax | Texas SB 17 foreign-buyer land restrictions effective | TX SOS | 2026-05-01 | 2026-11-01 | 2 | --visa --price`
- `2024-08 | rental | NAR Sitzer/Burnett $418M settlement — eff 17 Aug 2024 unbundled buyer-agent commissions nationwide (off MLS + written buyer-broker agmt pre-tour). Commissions did NOT fall (Redfin buyer-side 2.42% Q3-2025, up from 2.36% low; total mid-5% per agent surveys). CA AB 2992 codifies eff 1 Jan 2026. DOJ probe SEPARATE + still OPEN (SCOTUS denied NAR cert 13 Jan 2025). | NAR.realtor + Redfin + DOJ/SCOTUS + CA Leg (AB 2992) | 2026-07-02 | 2026-10-01 | 2 | --price --exit`
- `2023-04 | risks | NFIP Risk Rating 2.0 fully implemented | FEMA | 2026-05-01 | 2026-10-01 | 3 | --risks --insurance`
- `2025-11 | risks | Zillow MAINTAINS its 14 Nov 2025 de-emphasis of First Street climate-risk scores (removed from listings after the California Regional MLS inland-flood accuracy dispute; data still linked but easy to miss; map-view risk layer kept) — re-verified 14 Jun 2026: NOT restored + NOT further removed; Redfin + Realtor.com still display First Street data. Buyer DD must pull FEMA + RiskFactor.com (First Street) + state NHD directly, not rely on portal badges | CNN 2 Dec 2025 https://www.cnn.com/2025/12/02/climate/zillow-climate-data-extreme-weather-first-street-redfin (re-confirmed via HousingWire + Stocktonia Jan 2026) | 2026-06-14 | 2026-09-12 | 2 | --risks --climate`
- `2025-07-14 | finance | Fedwire Funds Service migrated to ISO 20022 message format — completed 14 Jul 2025 (rescheduled from the originally-announced 10 Mar 2025 per Fed announcement 13 Feb 2025). Closing-day USD wires now use ISO 20022 structured fields; bedding-in formatting/timing risk through 2026 | Federal Reserve Financial Services https://www.frbservices.org/resources/financial-services/wires/iso-20022-implementation-center | 2026-05-28 | 2027-05-01 | 3 | --remote --currency`
- `foundational | risks | California Natural Hazard Disclosure Statement (NHDS) — Civ. Code §§ 1103–1103.15 (statutory form at § 1103.2); seller + agent must disclose 6 mapped hazard zones: 2 seismic (Alquist-Priolo fault + seismic-hazard/landslide), 2 fire (state-responsibility-area + very-high fire-hazard-severity), 2 flood (FEMA SFHA + dam-inundation). Archetypal US state NHD; signed by all parties before close of escrow | California Legislative Information (Civ. Code §1103.2) https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1103.2. | 2026-05-28 | 2027-05-01 | 4 | --risks`
- `2026-02-03 (auth through 2026-09-30) | insurance | NFIP reauthorization cliff. After the longest lapse in program history (43-day gap during the Oct–Nov 2025 federal shutdown), HR 5371 restored NFIP retroactively to 1 Oct 2025; legislation signed 3 Feb 2026 extended authorization to 30 Sep 2026. Congress must reauthorize by 11:59 p.m. 30 Sep 2026 or new flood-insurance contracts halt (NAR est. ~1,300 sales/day, ~40,000 closings/month at risk). Buyers needing NFIP for a federally-backed-mortgage closing must confirm authorization on the closing date | FEMA Congressional Reauthorization page + Congress.gov CRS IN10835 | 2026-07-02 | 2026-09-15 | 1 | --risks --insurance --finance (US)`
- `2026 session | foreign-buyer | 2026 state foreign-ownership wave. Seven states enacted new or amended foreign-ownership real-estate restrictions in 2026 (Indiana SB 256; Louisiana SB 200, SB 466, HB 192, HB 816; Mississippi SB 2341; Oklahoma HB 3431; South Dakota SB 40 eff 1 Jul 2026; Tennessee SB 2233, SB 2424; Utah HB 291); 25 states considered legislation (per NALC FAQ). Counts vary by scope: ~29 states with enacted agricultural-land restrictions (Nat'l Ag Law Center) vs 38 states where broader foreign-adversary property bans were introduced/advanced in 2025, 15 of them enacting (MultiState). Playbook "~36 states end-2025" superseded by this hedged range + omitted the 2026 additions | National Ag Law Center foreign-investments FAQ + NALC SD SB 40 article + MultiState | 2026-07-03 | 2027-01-15 | 2 | --foreign-buyer --price (US)`

### 🇹🇷 TR

- `2024-01-01 | rental | Law 7464 (Konutların Turizm Amaçlı Kiralanmasına ve Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun, RG 32357 2-Nov-2023) — STR permit from Kültür ve Turizm Bakanlığı mandatory for lets ≤100 days, actively enforced 2026. Base fines 100k/500k/1M TRY revalued annually; 2026 applied 180,617/903,088/1,806,177 TRY. Airbnb blocks listings lacking the Ministry permit number | Resmi Gazete 7464 (RG 32357) + Kültür ve Turizm Bakanlığı (2026 ceza duyurusu) + Airbnb Türkiye | 2026-07-02 | 2027-01-05 | 2 | --rental`
- `2022-06-13 | visa | CBI threshold USD 250k → USD 400k; 3-year non-resale lock annotated on title deed; foreigner acquisition capped at 10% of a district's private-property area + military/special-security zones barred. Re-verified 2026-07 on invest.gov.tr: $400k still current, no change; $600k raise rumored since 2024 but NOT enacted | invest.gov.tr (Türkiye Investment Office) + Resmî Gazete (Presidential Decree, publ. 13 May 2022) | 2026-07-02 | 2026-10-01 | 1 | --visa --price`
- `2023-02 | risks | Kahramanmaraş M7.8 + M7.5 earthquake → regulatory tightening (yapı denetim + Law 6306 kentsel dönüşüm acceleration + DASK enforcement); TBDY 2018 building code becoming effective baseline | AFAD + Çevre Bakanlığı | 2026-05-01 | 2026-09-01 | 1 | --risks --insurance`
- `2025-09 | tax | Land+Building Tax (Emlak Vergisi) reduction Cabinet resolution renewed annually — verify 2026 status | GİB + Resmi Gazete | 2026-05-01 | 2026-12-31 | 2 | --tax`
- `2026-2029 | tax | Rayiç bedel cycle — base values for Emlak Vergisi reset every 4 yrs; 2026-2029 cycle showing 3-5× nominal jumps under litigation | TKGM + Belediyeler | 2026-05-01 | 2027-01-01 | 2 | --tax`
- `2026-04-01 | connectivity | 5G ENACTED on schedule — state ceremony 31 Mar 2026 + commercial launch 1 Apr 2026 across all 81 provincial centres, all three operators (Turkcell / Türk Telekom / Vodafone), urban-first with full-nationwide target ~2028; licences to 2042. Fibre still leads fixed home broadband; 5G FWA (Turkcell Superbox) is a live supplement but NOT yet a parcel-level FTTH substitute — foreign-buyer broadband guidance (verify FTTH, not 5G) unchanged. Downgraded tier-3→4 (enacted, now watchlist) | BTK + Daily Sabah `https://www.dailysabah.com/business/tech/erdogan-heralds-new-era-as-turkiye-launches-5g-services` | 2026-06-14 | 2027-06-14 | 4 | --connectivity --digital-nomad`
- `pending | connectivity | Starlink ❌ NOT licensed — SpaceX applied to BTK for GMPCS licence 2023; still not approved (data-localisation/security concerns). Transport Ministry Nov-2025 said 'not on the agenda' + denied April-2026 launch reports; Satellite-2026 talks (SpaceX + Amazon Kuiper) ongoing; no approval timeline; Türksat-6A domestic rival | BTK + Ulaştırma ve Altyapı Bakanlığı (via Daily Sabah) + Starlink availability map | 2026-07-02 | 2026-10-01 | 2 | --connectivity`
- `2026-01-01 | tax | Emlak Vergisi 2026 increase capped — Law 7566 (RG 2025-12-19 No. 33112) added EVK geçici mad. 23: 2026 vergi değeri = 2025 değeri × 1.12745 (half the 25.49% revaluation) and md-29-computed values from the new 2026–2029 takdir birim değerleri may not exceed 2× the 2025 vergi değeri; 2027–2029 matrahs chain off the capped 2026 values; 7566 md 11 separately raises the annual uplift in non-takdir years from half to the full yeniden değerleme oranı (verify effective year); rates unchanged (mesken binde 1/2). Implemented by Emlak Vergisi Genel Tebliğ Seri 89 | Law: RG 2025-12-19 No. 33112; Tebliğ: RG 2025-12-31 No. 33124 5. mükerrer (https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-27.pdf) | 2026-07-03 | 2027-01-15 | 2 | --tax (TR)`
- `2026-01-01 | tax | 2026 GİB annual revaluation figures set (yeniden değerleme oranı 25.49%): mesken kira geliri istisnası 47,000→58,000 TRY; taşınmaz değer artış kazancı istisnası 120,000→150,000 TRY; gelir vergisi dilimleri revalued (non-wage 190k/400k/1M/5.3M); DKV Seri 88; Veraset füruğ/eş istisnası 2,316,628→2,907,136 TL (Tebliğ 57 — the playbook's prior '2025' Veraset base was actually the 2024 figure) (GVK Tebliğ 332, EVK Tebliğ 88, Veraset Tebliğ 57) | Resmi Gazete 2025-12-31 No 33124 5. mükerrer + GİB | 2026-07-03 | 2027-01-15 | 3 | --tax --rental (TR)`
- `2026-06 | macro | TCMB one-week repo held at 37.0% (overnight lending 40.0%, borrowing 35.5%) at June 2026 PPK (Basın Duyurusu 2026-23) — eased from the 50% Mar-2024 peak; CPI disinflation to ~32.6% YoY (May 2026), house prices +24.5% nominal / -6.1% real YoY (TCMB KFE May 2026) | TCMB PPK June 2026 decision (2026-23) + TÜİK + TCMB KFE | 2026-07-03 | 2026-10-01 | 3 | --price --tax (TR)`
- `2024-07-01 | rental | Residential rent-increase cap reverted to the 12-month-average TÜFE ceiling (Türk Borçlar Kanunu mad. 344) after the temporary 25% cap expired 1 Jul 2024 — June 2026 legal ceiling = 32.24% (TÜFE 12-month avg). Now added to playbook §rental (was a genuine gap) | TÜİK TÜFE + TBK mad. 344 | 2026-07-03 | 2027-01-01 | 2 | --rental (TR)`

### 🇦🇪 AE

- `2024-04 | risks | Record Dubai floods exposed drainage limits → Tasreef stormwater plan phased to 2033 (interim AED 277m completed Jun 2025) | Dubai Municipality | 2026-05-01 | 2026-11-01 | 2 | --risks --insurance`
- `2025 | finance | Dubai Law 2/2025 — DIFC Wills direct enforcement for non-Muslim expats | DIFC Courts | 2026-05-01 | 2026-10-01 | 2 | --finance --notary`
- `2023-06 | tax | Federal Corporate Tax 9% effective from Jun 2023 — applies to commercial property held in qualifying entities above AED 375k threshold; individual ownership unaffected | FTA UAE | 2026-05-01 | 2026-09-01 | 2 | --tax --finance`
- `2025-01 | rental | Dubai Smart Rental Index rates every residential building 1 to 5 stars by AI (60+ criteria); 0/5/10/15/20 pct rent-increase slabs unchanged under Decree 43/2013; index updated annually (2026 update effective 1 Mar per Engel and Voelkers — secondary) | DLD + RERA + The National quoting DLD registration CEO Jan 2025 | 2026-07-03 | 2026-12-01 | 2 | --rental (AE)`
- `2022-10 | visa | Cabinet Decision 65/2022 (Exec Regs of Fed Decree-Law 29/2021) sets Golden Visa RE route at AED 2M (single/aggregate); off-plan + escrow eligible. AED 2M UNCHANGED, re-confirmed on GDRFA service page. Apr 2026: GDRFA-DLD MoU merged Golden/Retiree/2yr-property visas into one digital platform (~5-day target); 2yr-visa AED 750k floor dropped, Golden route unaffected | ICP + DLD + GDRFA Dubai golden-residence service page | 2026-07-02 | 2026-10-01 | 1 | --visa`
- `2026-03 | connectivity | Starlink ✅ licensed Mar 2026 (TDRA approval) — UAE residential roaming previously grey-market; Etisalat-du duopoly remains, but Starlink rural/villa fallback now legal | TDRA | 2026-05-08 | 2026-09-01 | 2 | --connectivity`
- `2026-06-02 | rental | Abu Dhabi ADREC suspended all rent increases on lease renewals and new lettings until further notice — residential, commercial and industrial; benchmark rent = value in most recent registered Tawtheeq or Tamleek contract; ADGM carved out | ADREC announcement via Gulf News 02 Jun 2026 + Baker McKenzie client note Jun 2026 — confirm on adrec.gov.ae | 2026-07-03 | 2026-10-01 | 2 | --rental (AE)`
- `2025-07-02 | finance | Dubai First-Time Home Buyer Program (DLD + DET) — open to UAE residents 18+ incl. expats who do not own a Dubai freehold residential property; benefits are priority access to new off-plan launches, preferential pricing on units up to AED 5M, flexible payment plans for DLD registration fees via eligible credit cards (press reports interest-free instalments of the 4 pct fee), and competitive mortgage offers from partner banks; 22 developers + 5 banks; 3,200+ first homes and AED 5B+ transactions by Jun 2026 | DLD launch release + DLD eServices first-time-home-buyer page + Dubai Media Office 08 Jun 2026 | 2026-07-03 | 2026-12-01 | 3 | --finance --price (AE)`
- `2025-01 | price | DLD amended Article 3 of Regulation 3 of 2006 enabling private plot owners in Sheikh Zayed Road (Trade Centre Roundabout to Water Canal, 128 plots) and Al Jaddaf (329 plots) to convert leasehold to freehold, open to all nationalities; conversion fee 30 pct of DLD valuation based on Gross Floor Area; eligibility check via Dubai REST | DLD news release dubailand.gov.ae + BSA Law (instrument) | 2026-07-03 | 2026-12-01 | 2 | --price (AE)`

### 🇯🇵 JP

- `2023-12 | tax | 空家特措法 (Vacant Houses Special Measures Act) 改正 — 管理不全空家 designation can revoke 1/6 land tax exemption (~6× annual fixed-asset bill on land portion) | MLIT | 2026-05-01 | 2026-09-01 | 2 | --tax --risks`
- `2024-04-01 | finance | 民法改正 (Civil Code reform) — mandatory inheritance registration within 3 yrs (¥50k fine), 2-yr address-change registration; foreign-heir traps | 法務省 | 2026-05-01 | 2026-09-01 | 2 | --finance --notary`
- `2024-2026 | finance | BoJ rate normalization: Mar 2024 NIRP exit → Jul 2024 0.25% → Jan 2025 0.5% → Dec 19 2025 0.75% → held Jan-Apr 2026 → Jun 16 2026 1.0% (31-yr high since 1995, 7-1 vote, Asada dissent; next mtg Jul 31 2026, further hikes flagged); mortgage variable rates rising; Flat 35 applications +50% YoY Q3 2025 | BoJ MPM k251219a + k260616a | 2026-07-02 | 2026-10-01 | 1 | --finance --price`
- `2018-06 | rental | 民泊法 Minpaku law 180-night/yr cap; 2025 Tokyo + Kyoto + Osaka ward-level overlay restrictions intensifying | 観光庁 民泊ポータル | 2026-05-01 | 2026-09-01 | 2 | --rental`
- `2025-09-01 | rental | Osaka hotel tax tiered shift from 1 Sep 2025 — ¥200 for ¥5k-15k; ¥400 for ¥15k-20k; ¥500 for ≥¥20k per pp/n | Osaka Prefecture | 2026-05-11 | 2026-09-01 | 2 | --rental --tax`
- `2026-03-01 | rental | Kyoto hotel tax 9× hike from 1 Mar 2026 — new tiered structure ¥200 / ¥400 / ¥1,000 / ¥4,000 / ¥10,000 (up to 9× prior top tier); top tier targets premium ¥100k+/n stays | Kyoto City | 2026-05-11 | 2026-08-15 | 1 | --rental --tax`
- `2027-XX-XX (announced 2025-11-27) | rental | Tokyo to shift to 3% lodging tax from FY2027 (replacing tiered ¥100-200/pp/n) | Tokyo Metropolitan Govt + Japan Times | 2026-05-11 | 2026-12-01 | 2 | --rental --tax`
- `2022-09-20 | risks | 重要土地等調査法 (Important Land Investigation Act) effective; 注視区域 around defense / border / nuclear facilities; reporting may apply to certain residential transactions | 内閣府 | 2026-05-01 | 2026-10-01 | 2 | --risks --visa`
- `n/a (no statute identified) | other | r/japanlife thread 1oz5mvf (2025) alleges a municipality-required pre-deed "justification hearing" with foreigner-specific framing on a rural plot — SINGLE-THREAD ANECDOTE ONLY; a foreigner-specific gate is NOT established in primary law (agent-attributed talking points, single-sourced, uncorroborated, no statute/ordinance identified). The closest REAL regimes are universal and NOT nationality-gated: 国土利用計画法 事後届出 (Act 92/1974 — buyer files use-purpose + price within 2 weeks via the 市町村長 to the prefectural governor, who may issue a 勧告; thresholds ≥2,000/5,000/10,000 m² by zone) and 農地法 §3 農業委員会 permission (Act 229/1952 — farmland only, contract void without it); 開発許可 近隣説明会 (都市計画法 §29/33 + 市町村開発条例) is a development-conditioned community-meeting practice (meetings yes, statutory resident-veto generally no); 重要土地等調査法 (Act 84/2021) is a universal-scope security NOTIFICATION regime — does NOT match the anecdote. Nationality-recording added to 農地法 §3 (since 2023-09-01) / 国土利用計画法 施行規則 (corporate acquirers, from 2026-04-01) is data capture, NOT a foreigner approval gate. | MLIT 土地取引規制制度 https://www.mlit.go.jp/totikensangyo/totikensangyo_tk2_000019.html + 内閣府 重要土地等調査法 https://www.cao.go.jp/tochi-chosa/ + r/japanlife 1oz5mvf https://www.reddit.com/r/japanlife/comments/1oz5mvf/ (anecdote) | 2026-05-15 | 2027-05-15 | 4 | --permits --buying-process --scams --remote`

### 🇹🇭 TH

- `2020-01 | tax | Land and Building Tax Act BE 2562 (2019) effective — first national property tax; applied rates 0.01–0.7% by use. Cabinet reductions were episodic not automatic-annual (90% 2020–2021 COVID, 15% 2023); NO across-the-board Royal Decree reduction for 2026 (BE 2569) — full statutory rates apply; verify next-year decree via Royal Gazette | Royal Gazette (Royal Decree) + local administrative orgs | 2026-07-02 | 2027-01-05 | 1 | --tax`
- `2024-mid | visa | Destination Thailand Visa (DTV) launched — 5-yr multi-entry, 180 days/stay (extendable once +180, up to ~360 days continuous), THB 500k savings (bank statement last 3 mo, ending balance) + freelance/remote-worker proof (Workcation category) | MFA Thailand DTV Checklist https://image.mfa.go.th/mfa/0/n3gTFT2TOE/Visa_Requirements/Checklist_DTV.pdf + Immigration Bureau | 2026-07-02 | 2027-01-05 | 2 | --visa --digital-nomad`
- `2024-2025 | rental | Hotel Act BE 2547 (2004) §4 — STR <30 nights without hotel licence still illegal; enforcement intensifying (joint DOPA/police/Immigration raids; Bangkok/Phuket/Pattaya). NEW: draft accommodation-reform bills under Council of State consultation would let condos register STR without a hotel licence — NOT yet enacted; 'already legalised' claims false | DOPA (Dept of Provincial Administration) + Bangkok Post + AMCHAM Thailand + Formichella & Sritawat | 2026-07-02 | 2026-10-01 | 2 | --rental`
- `2024-2025 | visa | Proposed 99-yr lease + 75% condo quota — under Cabinet discussion; NOT enacted as of May 2026 | Cabinet of Thailand | 2026-05-01 | 2026-09-01 | 2 | --visa --price`
- `2024 | tax | Por 161/2566 + 162/2566 (eff. 1 Jan 2024): Thai tax residents' remitted foreign income taxable in year of remittance regardless of when earned; pre-2024 income stays exempt. Mid-2025 Revenue Dept draft 2-yr grace period (remit same yr earned or next = exempt) still NOT enacted as of Jun 2026 — pending Cabinet approval + Council of State review + Royal Gazette publication | Thai Revenue Department (Por 161/2566, 162/2566) | 2026-07-02 | 2026-10-01 | 2 | --tax --visa`
- `2026-06-30 (Cabinet approval — Royal Gazette publication to verify) | tax | Transfer-fee stimulus EXTENSION: Cabinet approved extending the 0.01% transfer + 0.01% mortgage-registration fee reduction (residences ≤ THB 7M, Thai nationals only — foreign buyers unaffected) from 30 Jun 2026 to 30 Jun 2027, effective once published in the Royal Gazette — news-tier only, verify the Gazette notice before relying | The Thaiger / The Nation (news — Royal Gazette primary pending) | 2026-07-02 | 2026-10-01 | 2 | --tax --notary (TH)`

### 🇹🇼 TW

- `2023-XX-XX | rental | Taiwan Tourism Bureau reorganised into **Tourism Administration MOTC** at `admin.taiwan.net.tw`; legacy `dot.gov.tw` URLs retired; same authority chain under the Ministry of Transportation and Communications; STR analytics + tourism statistics still published at the new portal | MOTC Taiwan | 2026-05-27 | 2027-12-31 | 4 | --rental (TW)`

### 🇩🇴 DO

- `2017 | finance | AML Ley 155-17 + UAF — beneficial-owner disclosure + source-of-funds proof for property transactions | UAF | 2026-05-01 | 2026-12-01 | 3 | --finance --notary`
- `2022 | risks | Hurricane Fiona (Sept 2022) → MOPC R-007 amendments to track | MOPC | 2026-05-01 | 2026-10-01 | 3 | --risks --insurance`
- `2025 | tax | IPI threshold DOP 9,860,649 (2025) — indexed annually; CONFOTUR-registered tourism projects 100% IPI + transfer + ITBIS exempt ~15 yrs | DGII + MITUR | 2026-05-01 | 2027-01-01 | 2 | --tax`
- `ongoing | visa | Investor residency USD 200k → 2-3-yr citizenship — fast-track to passport; CONFOTUR-registered RE benefits stack | Migración + MITUR | 2026-05-01 | 2026-09-01 | 2 | --visa`

### 🇨🇴 CO

- `2020 | finance | Decreto 1339/2020 — Catastro multipropósito national rollout; closing avalúo-vs-comercial gap; some areas seeing 2-3× predial bills | IGAC + DNP | 2026-05-01 | 2026-09-01 | 2 | --tax --price`
- `2024 | rental | Bogotá STR 10% lodging tax + Decreto 538/2024 still UNVERIFIED — sisjur re-check 2026-07 finds no matching 2024 decree and no city 10% bed tax. RNT IS nationally mandatory (Ley 2068/2020, Decreto 1836/2021); real charges are the 0.25% tourism parafiscal + municipal ICA, not a 10% bed tax. Pending PL 190/2025 may let districts cap lodging. | Alcaldía Bogotá sisjur + MinCIT | 2026-07-02 | 2026-10-01 | 2 | --rental`
- `2024 | rental | Medellín STR enforcement intensifying — RNT + uso-del-suelo closures (1,700+ unlicensed identified 2024; 34 sin licencia + 93 informes técnicos in 6mo, El Poblado a top zone; 8,951 RNT May 2026). 'Acuerdo 056/2024' still NOT found — real basis is POT Acuerdo 48/2014 Art. 255; mediano-plazo POT revision underway for rentas-cortas uso del suelo | Alcaldía de Medellín (Secretaría de Turismo) + POT Acuerdo 48/2014 | 2026-07-02 | 2026-10-01 | 2 | --rental`
- `2022 | tax | Ley 2277/2022 reforma tributaria — gan. ocas. 15%, wealth tax above UVT threshold | DIAN + MinHacienda | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `ongoing | visa | Migratorio M visa real-estate route 350× SMLMV (~USD 125k 2026); 650× → PR-eligible after 5 yrs | Cancillería + Migración | 2026-05-01 | 2026-09-01 | 2 | --visa`

### 🇺🇾 UY

- `2021 | tax | Ley 19.937 — 11-year exemption on foreign interest+dividends for new tax residents (extends Ley 18.083); major wealth-relocation magnet from AR/BR | MEF + DGI | 2026-05-01 | 2026-12-01 | 1 | --tax --visa`
- `2020 | tax | Decreto 138/020 + 153/020 — lowered RE investment threshold to UI 3.5M (~USD 470k) for tax residency | MEF + DGI | 2026-05-01 | 2026-12-01 | 2 | --tax --visa`
- `2018 | finance | Ley 19.210 financial inclusion — cash-payment caps 40,000 UI for property AML | BCU + MEF | 2026-05-01 | 2026-12-01 | 3 | --finance --notary`
- `ongoing | rental | STR operator registration is NATIONAL not municipal — Ley 20.352 (2024) mandates Mintur Registro de Operadores Turísticos (unique number in every offer, guest data to Interior; triggers if let >5x/yr, stays ≤120 days). Reglamentary decree still DRAFT (Mintur proyecto Nov 2025, 180-day platform window); NOT in force for 2025-26 season, still pending mid-2026. Maldonado only reinforces informal-supply control | Ley 20.352 + Mintur + Intendencia de Maldonado | 2026-07-02 | 2026-10-01 | 2 | --rental`

### 🇨🇱 CL

- `2020 | tax | Sobretasa Ley 21.210 — 0.275–0.425% on aggregate property > UF 670; ongoing tramo adjustments via Ley 21.713 reform | SII + MinHacienda | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2022-2024 | risks | Código de Aguas reform — water rights modifications; mega-drought central+north intensifying | DGA + MinAgricultura | 2026-05-01 | 2026-10-01 | 2 | --risks --mains`
- `2023 | finance | Condominio Ley 21.442 — replaced Ley 19.537; new HOA framework | MinVivienda + Conservadores | 2026-05-01 | 2026-11-01 | 3 | --finance --notary`
- `2011 | risks | NCh 433 Mod DS 61/2011 — post-2010 Maule earthquake building-code revision raised seismic standards | MINVU | 2026-05-01 | 2027-01-01 | 1 | --risks`
- `ongoing | rental | No comuna-wide STR ban found: tightening runs via municipal patente comercial de hospedaje + uso-de-suelo enforcement (intensified 2026; Las Condes, Providencia confirmed; fines ≤5 UTM + clausura) and copropiedad bylaws barring short-stays under Ley 21.442 + Reglamento DS N°7 (D.O. 9-Jan-2025). Vitacura STR-specific curbs unverified; CS upheld hospedaje as permitted residential use (Lo Barnechea, OGUC 2.1.25) | MINVU Ley 21.442 + Reglamento DS N°7 + Municipios (patente hospedaje) | 2026-07-02 | 2026-10-01 | 2 | --rental`

### 🇪🇨 EC

- `2024-04-01 | tax | IVA raised from 12% → 15% (NOT 13%) — Decreto Ejecutivo 198/2024 (11 Mar 2024) + Ley Orgánica para Enfrentar el Conflicto Armado Interno; standard rate effective 1 Apr 2024; emergency security funding; potential revert to 12% remains political possibility | SRI + Decreto Ejecutivo 198/2024 | 2026-05-27 | 2026-09-01 | 1 | --tax`
- `ongoing | tax | CGT 0% on habitual residence after 1-year holding (NOT 5 years) — UNIQUE LATAM exemption; LRTI art. 8 + reglamento, as amended by Ley Orgánica de Reforma Tributaria | SRI + Ley Orgánica Reforma Tributaria | 2026-05-27 | 2026-12-01 | 1 | --tax --exit`
- `ongoing | visa | Visa de Inversionista USD 47,000 (= 100 × SBU at SBU 2026 USD 470/mo) in Ecuadorian real estate or fixed-term productive activity; verify current SBU multiple at Cancillería; Ley Orgánica de Movilidad Humana 2017 + reglamento | decreto Ministerio del Trabajo Dec 2025 + Cancillería | 2026-05-27 | 2026-12-01 | 2 | --visa`

### 🇿🇦 ZA

- `2025-01 | finance | Expropriation Act 13 of 2024 assented Jan 2025 — Constitutional challenges pending; theoretical risk for residential land but practical urban risk remains low | Constitutional Court + DALRRD | 2026-05-01 | 2026-09-01 | 1 | --finance --visa`
- `2024-08 | rental | National Tourism Amendment Bill still pending — interim non-binding draft Code of Good Practice for STRs gazetted 13 Mar 2026 (comment closed 12 May 2026); Bill estimated to Cabinet in 2026/27 FY per Min De Lille. Cape Town: 2026/27 Rates Policy amendment reclassifies property available for STR >50% of any 365-day period as commercial (tabled 31 Mar 2026, adoption by Council scheduled May 2026, implementation from 1 Jul 2026; commercial reclassification of identified properties foreseen from 1 Jul 2027 after grace period); mandatory STR registration via Short-Term Letting By-law due later 2026 | Dept of Tourism (PMG) + City of Cape Town STR FAQ/Rates Policy | 2026-07-02 | 2026-10-01 | 2 | --rental`
- `2024-02-29 | tax | Solar PV individual rebate (25% of cost, up to R15,000) applied only to panels brought into use 1 Mar 2023–29 Feb 2024; expired 29 Feb 2024 and NOT extended/replaced in 2025 or 2026/27 Budgets — no residential solar PV tax incentive currently available (Treasury reviewing 2023 renewable-energy incentives via survey, no successor enacted); business Sec 12BA 125% allowance separately lapsed 28 Feb 2025 | SARS (solar-tax-rebate page) + Treasury renewable-energy incentive review | 2026-07-02 | 2027-03-01 | 3 | --tax --esg`
- `2025-26 | tax | SARS Transfer Duty Schedule 8 — exempt below R1.1M, progressive to 13% above R12M; verify exact brackets each tax year | SARS | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `2024-2025 | risks | Eskom load-shedding declined via Operation Vulindlela + private generation; backup power still common in upper-middle market | Eskom + DMRE | 2026-05-01 | 2026-09-01 | 3 | --risks --finance`
- `2022-02 | finance | Property Practitioners Act 22/2019 (PPRA) replaced EAAB Feb 2022 — new agent regulation + FFC requirements | PPRA | 2026-05-01 | 2027-01-01 | 3 | --finance --notary`
- `2026-2027 (in flight) | connectivity | Starlink GREY-MARKET — ICASA requires 30% local BEE ownership under ECA; Dec-2025 Malatsi equity-equivalent (EEIP) policy direction rejected by ICASA 13 May 2026 as needing ECA amendment (now tied to slow ECA Amendment Bill); SpaceX filed NO application (confirmed mid-Jun 2026, still none 2 Jul 2026); ICASA 29 Jun 2026 gazette reaffirms 30% rule + 3 licence categories (I-ECS/I-ECNS/RFS), no ITA open so new entrants must buy an existing licence; grey imports via Mauritius/Mozambique SIMs; earliest legal launch est. 2027 | ICASA (13 May 2026 response + 29 Jun 2026 Govt Gazette) + DCDT | 2026-07-02 | 2026-10-01 | 1 | --connectivity`

### 🇬🇪 GE

- `2025-05-31 | regulatory | Foreign Agents Registration Act (GEOFARA, Law N399) — passed Parliament 1 Apr 2025, in force 31 May 2025; Criminal Code Art. 355² fines + imprisonment up to 5yr for non-registration; Constitutional Court challenge pending; grants-approval regime tightened Mar 2026; PACE (24 Jun 2026) urged full repeal; affects foreign-funded NGOs/JVs/advisors NOT private residential foreign property purchase | Parliament of Georgia Law N399 (ILO NATLEX) + Venice Commission CDL-AD(2025)034 + ICNL | 2026-07-02 | 2026-10-01 | 2 | --tax --rental --scams`
- `2026-03-01 | visa | Investment residence permit real-estate threshold rises from US$100k → US$150k (1-year renewable); US$300k 5-year unchanged; transition rule requires completed purchase + full payment by 28 Feb 2026 to lock legacy threshold | Government of Georgia + sda.gov.ge | 2026-06-03 | 2026-09-01 | 2 | --tax --rental`
- `2026-03-01 | visa | Labor migration amendments (adopted 26 Jun 2025) require work permits for foreign workers incl. remote workers, self-employed, entrepreneurs beyond visa-free year; labour immigrants registered by 1 Mar 2026 must obtain work authorisation + residence permit by 1 Jan 2027 (GEL 2,000/person fine); labour-market test waived for International-Company status / monthly salary >GEL 15k | Parliament of Georgia + Fragomen + US Embassy Tbilisi | 2026-06-03 | 2026-09-01 | 2 | --work --rental`
- `2026-01-01 | regulatory | Decree #602 of 26 Dec 2025 mandates travel medical insurance (min GEL 30,000 coverage) for all foreign entrants for duration of stay | Government of Georgia + matsne.gov.ge | 2026-05-27 | 2026-12-01 | 3 | --price --rental`
- `2025-04-17 | visa | Ordinance #122 amended Government Decree #256 visa-free list — 17 nationalities (Afghanistan, Bangladesh, Eritrea, Ethiopia, Ghana, Yemen, Cameroon, Côte d'Ivoire, DRC, Morocco, Nigeria, Pakistan, Somalia, Syria, Sudan, Tanzania, Uganda) lose Gulf-state-permit visa-free route | matsne.gov.ge/en/document/view/2867361 | 2026-05-27 | 2026-10-01 | 3 | --rental --scams`
- `2023-12 | visa | EU candidate status granted Dec 2023 — accession process active; longer-term policy alignment may shift property-tax regime + capital controls | European Council + GoG | 2026-05-01 | 2026-11-01 | 2 | --visa --tax --currency`
- `2025-XX | tax | Tbilisi Sakrebulo Decision 14-69 sets 2025 property-tax schedule (income-threshold gated above GEL 40k household income); annual revisions expected | Tbilisi City Hall + Revenue Service | 2026-05-01 | 2026-09-01 | 3 | --tax`
- `ongoing | rental | No national STR licensing statute as of mid-2026 — Tbilisi STR regulation remains low (AirROI 2026: ~0% licensed listings, minimal registration); enforcement varies by city, monitor for Sakrebulo ordinances | City Halls (Sakrebulo) + Revenue Service + AirROI 2026 | 2026-07-02 | 2027-01-05 | 3 | --rental`
- `2024-XX | finance | NBG mortgage rate normalization post-EUR rate cycle; LTV caps tightened for non-resident foreign-currency loans | National Bank of Georgia | 2026-05-01 | 2026-09-01 | 3 | --finance`

### 🇮🇩 ID

- `2021-02 | foreign-buyer | PP No. 18/2021 expanded foreigner rights — Hak Pakai 30+20+30=80 yr direct ownership w/ KITAS/KITAP, SHMRS strata-title condos foreigner-owned | Ministry of ATR/BPN | 2026-05-01 | 2026-11-01 | 1 | --tax --visa` ownership
- `2023-2025 | foreign-buyer | Bali Provincial Court voided multiple nominee-structure transactions 2023-2025 (UUPA Art. 26(2) violations) — pre-2023 expat-forum advice now actively dangerous | Bali Provincial Court | 2026-05-01 | 2026-09-01 | 1 | --tax ownership`
- `2023-XX | visa | Permenkumham 22/2023 Second Home Visa — qualifying IDR 2B asset can BE the property itself (Hak Pakai/SHMRS) | Imigrasi | 2026-05-01 | 2026-10-01 | 2 | --visa`
- `2022-01 | tax | UU HKPD Law 1/2022 reformed local taxation — BPHTB statutory ceiling 5%, kabupaten can set within ceiling; verify per-kabupaten | Ministry of Finance + DJP | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `ongoing | rental | Bali villa STR enforcement varies by kabupaten — Pondok Wisata licensing patchy; monitor Provincial regulations | Bali Provincial Govt + Imigrasi | 2026-05-01 | 2026-09-01 | 3 | --rental`
- `2024-02-14 | rental | Bali Provincial Levy IDR 150,000 per foreign visitor (one-time per arrival) under Perda Bali No. 6/2023, effective 14 Feb 2024 | Bali Provincial Govt + lovebali.baliprov.go.id | 2026-05-11 | 2026-09-01 | 2 | --rental`
- `2026-02-24 | rental | Bali Perda 4/2026 (signed 24 Feb 2026; alih-fungsi-lahan + larangan nominee) — nominee land transfers PROHIBITED; illegal LP2B rice-field conversion = 5yr prison + IDR 1bn (UU 41/2009, referenced by Perda); OTA NIB deadline was 31 Mar 2026, reportedly extended May 31/Aug 2026 (secondary sources, govt-unconfirmed, enforcement inconsistent); foreigners barred from Pondok Wisata (Permenpar 18/2016); compliant path = PT PMA + KBLI 55193 | Bali Provincial Govt (Perda 4/2026 via JDIH Bali) + UU 41/2009 + OTA platform notices | 2026-07-02 | 2026-10-01 | 1 | --rental`

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
- `2026-04-25 | rental | HCMC apartment STR rule REPLACED — Decision 19/2026/QĐ-UBND (HCMC People's Cttee, issued 11 Apr 2026, effective 25 Apr 2026, signed Bùi Xuân Cường) supersedes Decision 26/2025/QĐ-UBND (eff. 27 Feb 2025). New rule reframes short-term (day/week) apartment letting as tourist accommodation (căn hộ du lịch): permitted only if the owner registers a tourist-lodging operation and complies with housing/real-estate/tax/residence/security/tourism/fire-safety rules (Art. 12); scope widened to residential-only + mixed-use buildings — press frames it as both a loosening and a tightening. Superseded 26/2025 had barred STR in ordinary residential apartments (Art. 13), allowing only mixed-use condotels. Whether an ordinary residential unit now qualifies turns on approved function + registration — verify full text per building. Hanoi/Da Nang still have no specific STR rule as of 2026 | HCMC People's Committee (Decision 19/2026/QĐ-UBND, thuvienphapluat.vn + luatvietnam.vn full text) + Nhân Dân + Người Lao Động | 2026-07-02 | 2026-11-01 | 1 | --rental`
- `2026-09-11 | connectivity | Hague Apostille convention enters into force for VN — POA chain shifts from full consular legalisation to apostille; calendar-actionable re-stamp of shared/connectivity.md + shared/language.md | HCCH + Vietnam MFA | 2026-05-08 | 2026-09-15 | 2 | --connectivity --language`
- `2026-02 | connectivity | Starlink licence GRANTED ~Feb 2026 — Authority of Telecommunications (MOST, ex-MIC) licensed Starlink Services Vietnam for fixed+mobile LEO satellite telecom w/ network infra; Radio Frequency Dept approved spectrum; up to 600,000 terminals + 4 gateways under 5-yr pilot (PM Decision 659/QD-TTg, 26 Mar 2025, to Jan 2031); launch date TBA | MOST Authority of Telecommunications + Radio Frequency Dept + PM Decision 659/QD-TTg (VNA/VietnamPlus) | 2026-07-02 | 2027-01-05 | 2 | --connectivity`
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
- `2023-2026 | risks | Israel-Hamas (Oct 2023; fragile US-brokered Oct 2025 Gaza ceasefire) + Israel-Hezbollah (Nov 2024 ceasefire) + two Israel-Iran wars (Jun 2025 12-day war; 2026 war, Apr 2026 ceasefire) disrupted insurance; ~1M cumulative war-damage claims. Property Tax Compensation Fund (Israel Tax Authority) is the state compensator | Israel Tax Authority Property Tax Compensation Fund + gov.il | 2026-07-02 | 2026-10-01 | 1 | --risks --insurance`
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

- `2024-03-06 | currency | EGP free-float Mar 2024 (after IMF EFF approval) — devaluation ~15.7→30→50/USD by Mar 2024; hit all-time low ~54.9/USD Mar 2026 then appreciated to ~49/USD by Jul 2026 (CBE official 49.08 buy 1 Jul 2026); flexible float sustained (IMF EFF 5th/6th reviews completed Feb 2026); foreign buyers face structural FX volatility | CBE + IMF | 2026-07-02 | 2026-10-01 | 1 | --currency --tax`
- `2023-XX | visa | Investment Law 160/2023 RBI/CBI tiers — USD 250k cash deposit (5-yr) → PR / USD 300k RE → citizenship / USD 350k investment → citizenship; thresholds have shifted multiple times since 2023, verify with GAFI in writing before transferring funds | GAFI + Ministry of Investment | 2026-05-01 | 2026-09-01 | 1 | --visa --tax`
- `2023-XX | tax | Law 175/2023 — CGT 2.5% of GROSS sale price (not net gain); even loss-making sales taxed; materially distorts IRR modeling | ETA | 2026-05-01 | 2026-12-01 | 2 | --tax`
- `1996-XX | foreign-buyer | Law 230/1996 — max 2 properties/foreigner, max 4,000 m² each, NOT in protected/military/Sinai/border zones, NOT within 5 km of Suez Canal, agricultural land Egyptian-only, 5-yr resale lock (waivable Cabinet) | Ministry of Justice + REPA | 2026-05-01 | 2027-01-01 | 1 | --tax ownership`
- `ongoing | foreign-buyer | Form 4 paper trail at purchase via CBE-authorized bank is GATING procedural risk — without it future USD repatriation of sale proceeds structurally blocked, sellers stuck with EGP-only exit (catastrophic given EGP devaluation history) | CBE | 2026-05-01 | 2026-09-01 | 1 | --tax --currency`
- `ongoing | foreign-buyer | Sinai is usufruct-only 50-yr leasehold from TDA despite many Sharm El Sheikh sales offices marketing units as "freehold" — buyers regularly misled; deal-killer-class misrepresentation | TDA + REPA | 2026-05-01 | 2026-12-01 | 1 | --tax ownership`

### 🇲🇺 MU

- `2026-07-01 | tax | Finance Act 2025 (Act 18/2025) — non-citizen EDB-scheme residential: registration duty (buyer) + land transfer tax (seller) each 5%→10%; contested date RESOLVED — enacted Act §29 (LDTA) + §49 (RDA) both set trigger to transfers on/after 1 Jul 2026 (not gazette-publication), now in force. Resale LTT is FLAT 10% (Seventh Schedule Part III); proposed higher-of-10%-or-30%-of-gain formula NOT enacted — MU stays CGT-free. NB: 2026-27 Budget (Jun 2026) announced EDB-scheme transfer duties/taxes 'will be reviewed' — Finance Act 2026 may amend; watch gazette | Finance Act 2025 Act 18/2025 §29 LDTA + §49 RDA — mauritiusassembly.govmu.org; confirmed KPMG/EY/PwC FA-2025 reviews; 2026-27 Budget review per KPMG Budget Highlights 2026-27 | 2026-07-02 | 2026-10-01 | 1 | --tax ownership --visa`
- `2025-07-01 | tax | New 0/10/20% PIT brackets effective 1 Jul 2025 (Finance Act 2025) — replacing prior 15% flat | MRA Mauritius Revenue Authority | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2025-XX-XX (Finance Act 2025) | visa | Retirement Permit threshold raised USD 1,500/mo → USD 2,000/mo (Non-Citizen Retiree route — passport.govmu.org) | EDB + Passport Office | 2026-05-07 | 2026-09-01 | 2 | --visa`
- `2025-02-XX | foreign-buyer | EDB published Amendments to IRS/RES/IHS/PDS/SCS regulations Feb 2025 — new mandatory requirements for non-citizens | EDB Mauritius (FAQ-Amendments document) | 2026-05-07 | 2026-09-01 | 2 | --tax ownership --visa`
- `2024-XX-XX | tax | Mauritius statutes consolidated to **lawsofmauritius.govmu.org** (Attorney-General's Office portal); legacy mra.mu /download/*.pdf URL tree for the Land (Duties & Taxes) Act, Registration Duty Act + Finance (Misc Provisions) Acts retired; MRA retains tax administration but the AG portal is now the canonical primary source for statutes | Attorney-General's Office Mauritius — lawsofmauritius.govmu.org | 2026-05-27 | 2027-12-31 | 4 | --tax --notary (MU)`

### 🇰🇿 KZ

- `2026-01-01 | tax | New Tax Code (Law 214-VIII / K2500000214, signed 18 Jul 2025) effective 1 Jan 2026 — now IN FORCE — progressive PIT 10% up to 8,500 MCI/yr, 15% above (replacing prior 10% flat); VAT raised 12%→16% (reduced 5% medical, →10% in 2027); VAT registration threshold cut 20,000→10,000 MCI | Adilet (adilet.zan.kz) — Ministry of Justice legal database | 2026-07-02 | 2027-01-05 | 2 | --tax --rental --finance`
- `2026-01-01 | tax | Social tax (СН) cut from 11% to 6% under new Tax Code K2500000214 (Law 214-VIII ZRK signed 18 Jul 2025) — but the social-contributions offset is eliminated, and employer pension contribution ОПВР rises 2.5%→3.5% in 2026 (5% by 2028 per ENPF phased trajectory) → net employer payroll burden ≈ unchanged | State Revenue Committee Kostanay (kgd.gov.kz) + ENPF | 2026-05-27 | 2027-01-01 | 2 | --tax --finance --work`
- `2026-04-01 | mains | Utility-tariff moratorium ENDED 1 Apr 2026 (MEKS — Ministry of Energy modernization plan, 13.5T KZT through 2029) — electricity + heat + water tariff increases phased through 2029 | Ministry of Energy KZ + KEGOC | 2026-05-07 | 2026-09-01 | 2 | --mains --tax`
- `2025-05-10 | visa | Investor Visa "Golden Visa" launched 10 May 2025 — US$300,000 qualifying investment (KZ securities / AIFC participants / productive business) → 10-yr residence permit; **REAL ESTATE EXPLICITLY EXCLUDED** as qualifying investment; applications open 1 Jun 2025 | citizenx.com + goldenvisas.com (program guides); MFA KZ | 2026-05-07 | 2026-09-01 | 1 | --visa`
- `2021-05-XX | ownership | Agricultural land BANNED for foreigners — Law signed May 2021 by Tokayev post-2016 land protests; pre-2021 leases grandfathered to expiry | Land Code amendments — Adilet | 2026-05-07 | 2027-01-01 | 1 | --tax ownership`
- `2026-01-01 | tax | New Tax Code Art. 600/602/604 luxury property-tax band ENACTED — individuals aggregate all owned residential real estate at 31 Dec of the tax year; if combined government-assessed value exceeds KZT 450M, tax = KZT 2,946,600 + 2 percent of the excess (ADDITIVE formula, KGD-confirmed — NOT "2 percent with a 2,946,600 minimum"; maslikhats may raise up to +50 percent for housing; first applies to holdings at 31 Dec 2026, billed in 2027; below 450M the old per-object progressive cadastral schedule is unchanged). Separate 10 percent luxury excise applies to cars over 75M and yachts/jets over 100M, NOT to real estate. | Tax Code No. 214-VIII Art. 602 text via pro1c.kz + KGD via LS.kz (lsm.kz) + Krisha.kz explainer | 2026-07-03 | 2027-01-05 | 2 | --tax --exit --home-tax (KZ)`
- `2026-01-01 | tax | Residential CGT exemption holding period raised 1yr to 2yr under the new Tax Code — applies ONLY to properties ACQUIRED from 1 Jan 2026; properties acquired on/before 31 Dec 2025 keep the 1-year period. Gains, where any, taxed at progressive PIT 10 percent up to 8,500 MCI (approx KZT 36.8M for 2026) / 15 percent above; no gain means no tax regardless of holding period. Mortgage-interest PIT deduction abolished from 1 Jan 2026. | Krisha.kz 2026 rules explainer + Orda.kz + gov.kz East-KZ akimat | 2026-07-03 | 2027-01-05 | 2 | --tax --exit --finance (KZ)`
- `2026-06-05 | macro | NBK base rate cut 100 bps to 17.0 percent on 5 June 2026 (from 18.0 percent) — first reduction since mid-2024; instrument is officially the base rate (базовая ставка), not "refinancing rate"; ±1 pp corridor; NBK 2026 inflation forecast revised down to 9-11 percent; CPI eased to 10.3 percent June 2026 (from 10.6 Apr, 10.4 May); next rate decision 24 July 2026. | NBK Governor Suleimenov statement 5 Jun 2026 (primary, via BIS r260701i) + Astana Times + TradingEconomics | 2026-07-03 | 2026-08-01 | 3 | --currency --macro (KZ)`
- `2026-07-01 | permits | New Construction Code reported in force 1 Jul 2026 — tightened expertise + technical-supervision requirements for developments; possible new-build supply constraint — verify code number and scope against Adilet primary | Kursiv 22 Jun 2026 (secondary, developer interview) | 2026-07-03 | 2026-10-01 | 3 | --permits --price (KZ)`

### 🇨🇻 CV

- `2026-01-01 | tax | Lei n.º 55/X/2025 of 6 June 2025 — IUP (Imposto Único sobre o Património) REPEALED, replaced by IPI (Imposto sobre a Propriedade de Imóveis, 0.1% annual ownership) + ITI (Imposto sobre a Transmissão de Imóveis, 1% transfer); Boletim Oficial I Série n.º 46 | boe.incv.cv (Bulletin n.º 46 / 2025) | 2026-05-07 | 2026-09-01 | 1 | --tax`
- `2025-01-01 | tax | IRPC corporate-income-tax rate cut 22%→20% (2025 Budget) — tourism-zone preferential regimes maintained | DGCI | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2026-02-XX | macro | IMF Seventh ECF Review + Third RSF Review concluded Feb 2026 — real GDP +7.2% 2024 / +5.2% 2025; CVE-EUR peg credibility reaffirmed | IMF (PR26036) | 2026-05-07 | 2026-09-01 | 3 | --macro --currency`

### 🇸🇨 SC

- `2025-03-20 | foreign-buyer | Moratorium on residential-land purchase by non-Seychellois LIFTED 20 Mar 2025 — sanction now granted under the Immovable Property (Transfer Restriction) Act (Cap 95) under new floors: SCR 10M dwelling-house minimum + SCR 4,000/m² bare land; plot 2,000-4,000 m²; Sanction Duty raised 11%→12% of market value. No threshold/duty change found through mid-2026; Guidance Notes subject to periodic reviews. (SPA = Seychelles Planning Authority; no "Sanction Permit Act" exists) | Ministry of Lands & Housing Guidance Notes (20 Mar 2025) via Seychelles Planning Authority spa.gov.sc + Seychelles Investment Board investinseychelles.com | 2026-07-02 | 2027-01-05 | 1 | --tax ownership --visa`
- `2024-01-01 | tax | IPT (Immovable Property Tax) doubled 0.25%→0.5% — foreigner-only annual tax on non-Seychellois-owned residential property (raised eff. 1 Jan 2024) | SRC Seychelles Revenue Commission | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2026-01-15 | mains | PUC tariff revisions effective 15 Jan 2026 — electricity + water tariffs adjusted | Public Utilities Corporation (puc.sc) | 2026-05-07 | 2026-09-01 | 3 | --mains`
- `2023-08-01 → 2026-01-01 | rental | Tourism Environmental Sustainability Levy (TESL) — eff 1 Aug 2023: small (1-24 rooms) SCR 25/pp/n; medium (25-50) SCR 75; large (51+) + yachts SCR 100; charged on invoice NOT advertised price. FROM 1 JAN 2026: small establishments (1-24 rooms) NO LONGER subject to levy — yield-positive for foreign-owned villas | Tourism Seychelles | 2026-05-11 | 2026-09-01 | 1 | --rental --tax`

### 🇨🇳 CN

- `2026-01-01 | tax | VAT cut to 3% levy rate for individual resale of homes held <2yr (was 5% levy ≈5.6% all-in) — MoF & STA Announcement 2025 No.17 (issued 29 Dec 2025), in force 1 Jan 2026, repealing Cai Shui [2016] No.36 Annex 3 §5(1); ≥2yr holds VAT-exempt. Nationwide unification incl. Beijing/Shanghai/Guangzhou/Shenzhen ≥2yr exemption + ordinary/non-ordinary (普通/非普通) abolition were the EARLIER Announcement 2024 No.16 (eff. 1 Dec 2024), not No.17 | MoF + State Taxation Administration Announcement 2025 No.17 + 2024 No.16 (chinatax.gov.cn) | 2026-07-02 | 2027-01-05 | 2 | --tax`
- `2025-09-15 | currency | SAFE Notice Huifa [2025] No.43 (Deepening Cross-Border Investment/Financing FX Reform), publicly released/eff 15 Sep 2025 (SAFE branch cites nationwide implementation from 12 Sep) — GBA HK/Macao 'settle-first' home-purchase FX facilitation extended NATIONWIDE; capital-account income negative-list bar on non-self-use residential purchase REMOVED. SAFE clarified it only optimizes bank settlement procedure; foreign-individual purchase-qualification rules UNCHANGED | SAFE (safe.gov.cn) Notice + State Council policy Q&A (gov.cn) | 2026-07-02 | 2027-01-05 | 1 | --currency --tax ownership`
- `2024-12-01 | tax | Deed-tax restructure — first-home <140m² 1% / first-home ≥140m² 1.5% / second-home <140m² 1.5% / second-home ≥140m² 2-3% (city-tier-dependent); replaces prior structure | MoF + State Taxation Administration | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `2024-09-XX | foreign-buyer | Tier-1 social-security overlay easing September 2024 — Beijing 5-yr / Shanghai 1-yr / Shenzhen 3-yr / Guangzhou abolished (purchase-restriction Hukou-linked threshold periods relaxed) | Local Housing Bureaux Beijing/Shanghai/Shenzhen/Guangzhou | 2026-05-07 | 2026-09-01 | 1 | --tax ownership`

### 🇯🇲 JM

- `2025-10-28 | risks | Hurricane Melissa Cat 5 landfall 28 Oct 2025 (Westmoreland) — NHC final TCR (25 Feb 2026) confirms strongest hurricane on record to make landfall in Jamaica; US$8.8B direct physical damage (WB/IDB GRADE Nov 2025, costliest in Jamaican history; total economic loss higher); insurance hardening ongoing (FSC Melissa claims advisory 29 Jun 2026); BSJ hurricane-resilience draft standard DJS 385:2026 in public comment 14 Jun-13 Aug 2026 | NOAA NHC TCR AL132025 (25 Feb 2026) + World Bank/IDB GRADE (Nov 2025) + BSJ (bsj.org.jm) + FSC Jamaica | 2026-07-02 | 2026-10-01 | 1 | --risks --insurance --finance`
- `2025-04-01 | tax | Income-tax personal-allowance threshold raised to JMD 1.8M effective 1 Apr 2025 (was JMD 1.5M) — material PIT relief; rental + business income unaffected if held in personal name | TAJ Tax Administration Jamaica | 2026-05-07 | 2026-09-01 | 2 | --tax --rental`
- `2019-XX-XX | tax | Transfer Tax + Stamp Duty stack reformed — 2% Transfer Tax + JMD 5,000 flat Stamp Duty (was 5% transfer + 4% stamp pre-2019) — material reduction in transaction costs | TAJ + Ministry of Finance JM | 2026-05-07 | 2027-01-01 | 2 | --tax`

### 🇧🇸 BS

- `2022-01-01 | tax | VAT raised 7.5%→10% effective 1 Jan 2022 (Government Budget Communication) — broad consumption-tax increase touching property-related expenditures | DIR Department of Inland Revenue | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `ongoing | tax | RPT (Real Property Tax) bands budget-revisable annually via Budget Communication — verify current bands at DIR before any transaction-cost computation | DIR — inlandrevenue.finance.gov.bs/real-property-tax | 2026-05-07 | 2026-09-01 | 2 | --tax`
- `ongoing | risks | Hurricane Dorian (Sep 2019) calibration event — destroyed ~75%+ of homes on parts of Abaco + Grand Bahama; insurance market hardening continues 6+ years post-event; remains baseline for foreign-buyer DD on insurance availability + cost | NOAA NHC AL052019 + Government of The Bahamas | 2026-05-07 | 2027-01-01 | 1 | --risks --insurance --finance`

### 🇸🇲 SM

- `2018-12-24 | foreign-buyer | Legge 24 dicembre 2018 n.173 + Decreto Delegato implementation — prior authorization regime ABOLISHED for foreign acquisition; replaced with **2-property cap per foreign individual** (vs unlimited Sammarinese citizens / pre-2018 1-property cap) | Bollettino Ufficiale RSM | 2026-05-07 | 2027-01-01 | 1 | --tax ownership`
- `2026-01-01 | tax | IGR reform ENACTED — Legge 12 nov 2025 n.141 (amends L.166/2013), published in Bollettino Ufficiale, applies from tax year 2026: deductions shift to tax credits (detrazioni), progressive SMaC detrazione, resident rental detrazione 15% on 50% of canone up to €6,000; L.166/2013 progressive 9-35% bracket schedule retained (amended, not replaced); verify exact detrazione tables before quoting | Consiglio Grande e Generale — Legge 12 novembre 2025 n.141 (Bollettino Ufficiale) | 2026-07-02 | 2027-01-05 | 2 | --tax --rental --finance`

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

- `2025-11-28 | risks | Cyclone Ditwah landfall 28 Nov 2025 — catastrophic storm; USD 4.1bn direct damage (~4% GDP; World Bank GRADE Dec 2025); 1.1M ha (~20% of land) flooded; Central Highlands tea-country landslides/repricing. IMF deferred 5th EFF review + disbursed US$206M RFI (Dec 2025); combined 5th+6th EFF review COMPLETED 27 May 2026 (SDR508M/~US$695M) | World Bank GRADE report Dec 2025 + IMF PR26/172 combined 5th/6th EFF review 27 May 2026 | 2026-07-02 | 2026-11-01 | 1 | --risks --insurance --price`
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

- `2025-12-06 to 2026-06-05 | tax | 16th Tourism Act Amendment discounted resort head-lease-extension window LAPSED on its scheduled 5 Jun 2026 end date (ratified 6 Dec 2025; closure INFERRED — no extension or 17th Amendment found as of 14 Jun 2026, no Ministry post-deadline outcome statement located). The discounted ~USD 5M (49-yr) / USD 2.5M-3M (20/25-yr) rate reverts post-window to the higher default schedule (~USD 10M reference for a 49-yr extension) — verify the binding post-window fee with the Ministry implementing regulation. NB this was the 3rd serial re-opening of the discount (prior windows to ~Feb-2025, then Sep-2025) so a 17th-Amendment renewal is possible per precedent | Ministry of Tourism Maldives `https://www.tourism.gov.mv/dms/document/23d485632704b30cf178db46d41f0bff.pdf` + CTL Strategies `https://www.ctlstrategies.com/latest/tourism-act-16th-amendment/` | 2026-06-14 | 2026-07-14 | 1 | --tax --exit`
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

- `2025-06-01 | visa | Golden Visa — 5-yr residence permit per Presidential Decree No. 67 of 18 Apr 2025 (UP-67 Russian / PF-67 Uzbek; prior 'UP-89' was a wrong number), in force 1 Jun 2025. CORRECTED: it is a NON-REFUNDABLE DONATION — USD 250k main applicant + USD 150k per family member — NOT real estate (decree stipulates no property/business/job condition). The USD 300k Tashkent / 200k / 100k regional tiers belong to a SEPARATE pre-existing real-estate-for-residence route (UP-5611 app.6 / UP-101), not this decree. Implementing Cabinet/MIA resolution still NOT adopted as of Oct 2025 — banks cannot yet accept donations; verify operational status before relying. | Presidential Decree No. 67 of 18 Apr 2025 (lex.uz Uzbek original, per INVEXI) + IMI Daily + Fragomen + Astana Times + Azizov & Partners memo Oct 2025 (implementing-regulation status) | 2026-07-02 | 2026-10-01 | 1 | --visa`
- `2026-XX-XX | tax | 2026 +7% land/property/water indexation (per EY) — annual indexation of land tax + property tax + water tax + similar | EY Tax Alert Uzbekistan | 2026-05-08 | 2026-09-01 | 2 | --tax`
- `2022-07-16 | foreign-buyer | Cabinet of Ministers Resolution No. 384 of 16 July 2022 (PQ-384) — expanded eligibility to citizens of 108 countries to acquire built real estate (apartments / houses / commercial premises) WITHOUT residence permit; pre-2022 regime required residence permit first — gate now removed for EU/UK/US/CA/AU/NZ/JP/KR + GCC + most Asia; Land Code Articles 17-18 PROHIBITION on foreign land ownership PRESERVED | Kun.uz coverage of PQ-384 + Azizov & Partners legal memo | 2026-05-08 | 2027-01-01 | 1 | --visa ownership`
- `2017-09-XX | currency | Dual-rate "black market" gap closed September 2017 under Mirziyoyev liberalisation (Decree UP-5177); pre-2017 official ~3,000 UZS/USD vs unofficial ~8,000/USD (~2.5× spread); since Sep 2017 managed-float with active CBU intervention; cumulative depreciation 2017→2026 ~3,200 → ~12,500 UZS = ~290% nominal devaluation over ~9 years | Central Bank of Uzbekistan — `https://cbu.uz/en/` | 2026-05-08 | 2026-12-01 | 2 | --currency --finance`
- `2024-XX-XX | mains | Tashkent water utility "Suvsoz" rebranded **Toshkent shahar suv ta'minoti MCHJ** under O'zsuvta'minot AJ; new web portal `toshkent.uzsuv.uz` (legacy `suvsoz.uz` offline); operational responsibilities unchanged | Agency for the Operation of Water Management Facilities UZ + my.gov.uz/en/authority/844 | 2026-05-27 | 2027-12-31 | 4 | --mains (UZ)`

### 🇳🇦 NA

- `2025-10-08 (Bill — NOT enacted) | ownership | Consolidating Land Bill re-tabled in the National Assembly Oct 2025 (Min. Inge Zaamwani) — WOULD prohibit foreigners from acquiring communal AND commercial land (lease-only under job-/economy-benefit conditions); would replace the Agricultural (Commercial) Land Reform Act 6/1995 + the 2002 Communal Land Reform Act + ~12 laws; circumvention → fine up to N$50,000 / 10-yr prison. STATUS = BILL, awaiting debate as of 2026-06-13 — the only enacted foreign-ownership restriction remains farmland (ACLRA s.58); urban/residential freehold is NOT banned | Mail & Guardian 2025-10-08 (secondary) + NamibLII Act 6/1995 | 2026-06-13 | 2026-09-01 | 1 | --tax --visa (NA foreign-ownership)`

### 🇧🇼 BW

- `2025-12-17 (passed Parliament) | visa | Citizenship (Amendment) Bill 2025 passed Parliament 17 Dec 2025 — permits multiple citizenship; a CBI is announced but its threshold/regulations are NOT yet set (not operational as of Jun 2026). Already in force: Transfer Duty (Amendment) Act 2023 — non-citizen 10% on the first BWP 2m + 15% on the excess (the old flat 30% is STALE) | gov.bw / Parliament of Botswana + Orbitax (transfer duty) | 2026-06-13 | 2026-09-01 | 2 | --visa --tax (BW)`

### 🇻🇺 VU

- `2024-12-12 (in force) | visa | EU PERMANENTLY revoked Vanuatu's visa-free Schengen access — Reg (EU) 2025/11 (suspended 8 Nov 2022 / visa required 4 Feb 2023 / permanent revocation 12 Dec 2024); the first full EU revocation over an investor-citizenship scheme. The DSP/CIIP CBI (a donation to the National Development Fund, NOT property-linked) remains under sustained OECD/EU scrutiny | EU Council press release 2024-12-12 | 2026-06-13 | 2026-09-01 | 2 | --visa (VU)`

### 🇹🇹 TT

- `2024 (enforced) | tax | Property Tax reintroduced — residential 3% of Annual Rental Value (after a 10% deduction ≈ 2.7% effective); collection began 2024, first payment due 30 Sep 2024. The Property Tax (Amendment) Bill 2024 proposes a residential-rate reduction but is NOT enacted — 3% remains operative (a lone aggregator "now 2%" claim is uncorroborated) | tax.mygovtt.com + Ministry of Finance media release 18 Nov 2023 | 2026-06-13 | 2026-09-01 | 2 | --tax (TT)`

### 🇵🇰 PK

- `2025-11-13 (signed) | other | 27th Constitutional Amendment (signed 13 Nov 2025) created a Federal Constitutional Court (new Art. 175E); constitutional / fundamental-rights jurisdiction moved from the Supreme Court to the FCC — verify the operative allocation at na.gov.pk. SEPARATELY: FBR property advance tax (236C on sale / 236K on purchase) + CGT (§37(1A)) change with EVERY Finance Act — always re-verify current rates against the latest Finance Act | na.gov.pk (verify primary) + Business Recorder 2025-11 (secondary) | 2026-06-13 | 2026-09-01 | 3 | --tax (PK 236C/236K)`

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
| 🇪🇸 ES | National 100% gravamen on non-EU non-resident buyers — **STALLED**. PSOE Proposición de Ley 122/000196 (BOCG B-229-1, 30/05/2025) registered 22 May 2025, queued at "Pleno toma en consideración" since 5 Sep 2025, **never voted**; dropped from Jan 2026 housing package; Reuters 27/03/2026 confirms no parliamentary debate; no BOE-published Ley. Do NOT factor into TCO. | [Congreso 122/000196](https://www.congreso.es/es/proyectos-de-ley?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=122/000196) · [BOCG B-229-1](https://www.congreso.es/public_oficiales/L15/CONG/BOCG/B/BOCG-15-B-229-1.PDF) · [Reuters 2026-03-27](https://www.usnews.com/news/world/articles/2026-03-27/spains-100-non-eu-property-tax-stalls-in-congress) | 2025-05 reg.; 2026-03 stalled-confirmed; 2026-05-27 re-verified | 2026-11 |
| 🇮🇪 IE | LPT revaluation LANDED — 2026-2030 cycle live from 1 Jan 2026 (superseded by the ### 🇮🇪 IE country entry) | Revenue.ie | 2025-11 | 2026-09 |
| 🇨🇭 CH | Lex Koller tightening — federal Vernehmlassung opened 15 Apr 2026 (see ### 🇨🇭 CH entry; supersedes the earlier SECO-attributed row) | Bundesrat/BJ | 2026-04 | 2026-08 |
| 🇸🇪 SE | Capital gains rules on primary-residence sales — reform proposed | Skatteverket | 2026-02 | 2026-10 |
| 🇩🇪 DE | Bundesrat may reverse parts of Grundsteuer Bundesmodell — BFH upheld Bundesmodell 12 Nov 2025 (judicial track closed); watching legislative track only | Bundesrat | 2026-03 | 2026-09 |
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
