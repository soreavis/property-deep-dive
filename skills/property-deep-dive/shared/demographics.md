# Universal `--demographics` Section

Population, aging, schools, family-friendly metrics across 54+ supported countries (44 original + 10 Tier-1 + 8 Tier-2). Useful for relocation/family decisions and long-term valuation outlook.

**Snapshot**: April 2026.

## Universal contract

For the property's country, return:
1. **Population** (latest official; trend last 5 years)
2. **Median age + dependency ratio**
3. **Net migration rate** (per 1k pop)
4. **Fertility rate** (TFR, latest)
5. **PISA / school-system rank** (last assessment)
6. **English proficiency (EF EPI)** (where applicable)
7. **Family-friendliness composite** (parental leave, childcare cost, school quality)

## Output template

```markdown
## Demographics Profile

**Country**: <ISO2>
**Population**: <X> (trend: ↑↓→)
**Median age**: <X> yrs
**Net migration rate (per 1k)**: <X>
**Fertility rate (TFR)**: <X>
**PISA reading/math/science rank (latest)**: <X>
**EF EPI English proficiency rank**: <X>
**Family-friendliness composite**: <verdict>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Authoritative sources

- **Eurostat demography**: https://ec.europa.eu/eurostat/web/population-demography
- **OECD population stats**: https://data.oecd.org/pop/population.htm
- **World Bank Open Data**: https://data.worldbank.org/
- **UN World Population Prospects**: https://population.un.org/wpp/
- **PISA**: https://www.oecd.org/pisa/ (last cycle: 2022, published Dec 2023; next: 2025 results late 2026)
- **EF EPI English Proficiency Index**: https://www.ef.com/wwen/epi/

## Per-country snapshot (Apr 2026)

### Western Europe

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| FR | 68.4 | 42.0 | 1.79 | 474 | Moderate | Strong (free public childcare from age 3, generous parental leave) |
| IT | 58.8 | 47.3 | 1.20 | 482 | Moderate | Mid (childcare costs vary; Mezzogiorno underfunded) |
| ES | 48.5 | 44.5 | 1.16 | 474 | Moderate | Mid (free public schools, weak childcare 0-3) |
| PT | 10.5 | 46.0 | 1.43 | 477 | High | Mid (rising costs in Lisbon) |
| DE | 84.7 | 45.0 | 1.46 | 480 | Very High | Strong (Elterngeld, Kita expansion ongoing) |
| AT | 9.1 | 43.8 | 1.32 | 480 | Very High | Strong (Karenzgeld, kindergarten universal) |
| CH | 8.9 | 42.7 | 1.39 | 483 | Very High | Mid (school OK; childcare expensive) |
| NL | 17.9 | 42.3 | 1.49 | 459 (down) | Very High | Strong (kinderbijslag, kraamzorg, English-friendly) |
| BE | 11.8 | 41.9 | 1.55 | 467 | Very High | Strong (free childcare, language matters region-by-region) |
| LU | 0.66 | 39.7 | 1.30 | 465 | Very High | Strong (multilingual schools; high costs) |
| IE | 5.3 | 38.6 | 1.54 | 516 (top tier) | Native | Strong (English, strong public schools) |
| UK | 67.5 | 40.7 | 1.49 | 494 | Native | Strong public schools, expensive childcare |

### Iberia/Mediterranean

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| GR | 10.4 | 46.0 | 1.32 | 438 | High | Mid (crisis-impacted public schools) |
| MT | 0.55 | 41.4 | 1.13 | 448 | Very High | Mid (small system; English-medium top schools) |
| CY | 0.92 | 38.4 | 1.40 | 442 | High | Mid (private school dominant for English) |

### Northern Europe / Baltics

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| SE | 10.6 | 41.1 | 1.45 | 487 | Very High | Excellent (1+1yr parental leave, free childcare) |
| FI | 5.6 | 43.5 | 1.32 | 488 | Very High | Excellent (Finnish school model) |
| NO | 5.6 | 39.8 | 1.40 | 477 | Very High | Excellent (kontantstøtte, foreldrepermisjon) |
| DK | 5.96 | 42.1 | 1.50 | 489 | Very High | Excellent (barselsdagpenge, vuggestue universal) |
| IS | 0.39 | 37.8 | 1.59 | 460 | Very High | Excellent (highest TFR in Nordic; small population) |
| EE | 1.37 | 43.4 | 1.31 | 511 (top) | Very High | Strong (digital-native schools; vanemahüvitis) |
| LV | 1.85 | 44.5 | 1.36 | 475 | High | Mid (compulsory land lease + restitution affect family planning) |
| LT | 2.83 | 45.0 | 1.27 | 472 | High | Mid (declining pop; Vilnius growing) |

### CEE

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| PL | 38.2 | 42.0 | 1.16 | 489 | Moderate | Mid (500+ child benefit, Czyste Powietrze housing) |
| CZ | 10.6 | 43.4 | 1.71 | 492 | Moderate | Strong (3yr parental leave, mateřská) |
| SK | 5.4 | 41.7 | 1.61 | 466 | Moderate | Mid (rodičovský príspevok) |
| SI | 2.1 | 44.7 | 1.60 | 469 | High | Strong (porodniški dopust 1yr, free state preschool from age 1) |
| HR | 3.85 | 44.3 | 1.46 | 475 | High | Mid (declining pop esp. in interior) |
| HU | 9.6 | 43.4 | 1.59 | 473 | Moderate | Strong (CSOK Plusz, large-family bonuses) |
| RO | 19.0 | 43.6 | 1.81 | 428 | Moderate | Mid (rural schools weak; Bucharest/Cluj/Iași strong) |
| BG | 6.4 | 45.4 | 1.65 | 404 | Moderate | Mid (pop declining; Black Sea coast inflated by tourism) |

### Western Balkans

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| RS | 6.6 | 44.4 | 1.49 | 440 | Moderate | Mid |
| ME | 0.62 | 39.9 | 1.69 | 405 | Moderate | Mid (coast premium) |
| BA | 3.2 | 43.9 | 1.30 | 403 | Moderate | Mid (entity-level differences) |
| MK | 1.83 | 41.0 | 1.45 | 358 | Moderate | Lower (PISA bottom of EU candidate region) |
| AL | 2.7 | 36.9 | 1.32 | 358 | Lower | Lower (improving since 2020) |

### Anglo non-EU

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| US | 333 (2024 Census Bureau est.) | 38.9 (2023 ACS) | 1.66 (2023 NCHS, provisional) | 504 (PISA 2022) / math 465 | Native | Mid (no federal paid parental leave; childcare ~22% of median household income — Treasury 2023) |
| CA | 40.6 | 41.9 | 1.30 | 507 | Native | Strong (CCB, parental leave, universal healthcare) |
| AU | 26.7 | 38.0 | 1.50 | 498 | Native | Strong (paid parental leave, universal healthcare) |
| NZ | 5.3 | 38.0 | 1.52 | 501 | Native | Strong (universal early-childhood, paid leave) |

### Latin America

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| MX | 130.6 | 30.5 | 1.81 | 415 | Moderate | Mid (informal sector dominant; INFONAVIT housing benefits) |
| BR | 215.3 | 33.5 | 1.62 | 410 | Moderate | Mid (public schools weak; private dominant) |
| AR | 46.0 | 32.7 | 1.50 | 401 | High | Mid (post-Milei austerity affecting public services) |
| CR | 5.2 | 35.6 | 1.49 | 415 | Moderate | Strong public schools relative to LatAm; bilingual private exists |
| PA | 4.5 | 31.4 | 2.18 | 392 | Moderate | Mid (US-influenced bilingual private schools strong) |
| DO | ~11.3 (2024 ONE est.) | ~28 | 2.3 (2023 World Bank) | not in PISA — UNESCO LLECE 2019: below LatAm avg | Lower-Moderate | Mid (private bilingual schools dominant in Santo Domingo/Punta Cana; public underfunded) |
| CO | ~52.3 (2024 DANE) | ~31 | 1.7 (2023 DANE) | 409 reading (PISA 2022) | Moderate | Mid (public schools variable; Bogotá/Medellín private strong) |
| UY | ~3.4 (2024 INE) | ~36 | 1.5 (2023 MSP) | 430 reading (PISA 2022) | High | Strong (Plan Ceibal 1-laptop-per-child, free public university, 14-week paid maternity leave) |
| CL | ~19.6 (2024 INE) | ~36 | 1.5 (2023 INE, record-low) | 448 reading (PISA 2022, top in LatAm) | Moderate | Mid (school-quality gap public vs private severe; 24-week postnatal leave) |

### Caucasus

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| GE | ~3.7 (2024 Geostat) | ~38 | 1.7 (2023 Geostat, declining from 2.0 in 2019) | 374 reading (PISA 2022) | Moderate | Mid (730-day maternity leave on paper, low cash value; emigration steady — net migration negative since 2010s per Geostat) |

### Middle East / Levant / Gulf

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| TR | ~85.4 (2024 TÜİK) | ~33.5 (2023 TÜİK) | 1.51 (2023 TÜİK, record-low) | 456 reading (PISA 2022) | Lower | Mid (16-week maternity leave; declining TFR; private bilingual schools dominate top tier) |
| AE | ~10.2 (2024 FCSC est.) | ~33 (skewed by ~88% expat workforce, FCSC 2022) | 1.4 (2023 World Bank, Emirati TFR higher ~3) | 417 reading (PISA 2022) | Moderate | Mid (private international schools dominant — 60%+ of students per KHDA Dubai; childcare market-rate; positive net migration) |
| IL | ~9.84 (2024 CBS) | ~30.5 (2023 CBS) | 2.89 (2023 CBS, highest in OECD) | 474 reading (PISA 2022) | Very High | Strong (15-week paid maternity leave; ultra-Orthodox/Haredi TFR ~6.5 drives aggregate; Hebrew/Arabic public; English-medium private) |

### MENA — North Africa

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| MA | ~37.9 (2024 HCP census) | ~30 (2024 HCP) | 2.1 (2023 HCP, declining from 2.5 in 2010) | 339 reading (PISA 2022, near-bottom of participants) | Lower | Mid (14-week maternity leave; French/Arabic public schools; private French/American dominant in Casablanca/Rabat) |
| EG | ~110 (2024 CAPMAS) | ~25 (2024 CAPMAS) | 2.85 (2023 CAPMAS, declining from 3.5 peak 2014) | not in PISA — TIMSS 2019: below international median | Lower | Lower (4-month maternity leave; public schools severely under-resourced; private/IGCSE/American schools dominant in Cairo elite) |

### Sub-Saharan Africa

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| ZA | ~62.0 (2024 Stats SA mid-year est.) | ~28 (2024 Stats SA) | 2.3 (2023 Stats SA) | not in PISA — TIMSS 2019: bottom quartile | Moderate | Mid (4-month maternity leave at UIF rate; public schools highly variable, top quintile-5 strong; HIV-affected adult mortality skews age structure per Stats SA) |

### East Asia

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| JP | ~123.8 (2024 Stat Bureau) | 49.4 (2024 Stat Bureau, oldest globally) | 1.20 (2024 MHLW, record-low) | 516 reading (PISA 2022, top tier) | Lower | Strong (1-yr paid parental leave; universal childcare expanding under Kishida policy; population declining ~600k/year per MHLW) |

### South-East Asia

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| TH | ~71.7 (2024 NSO) | ~40 (2024 NSO) | 1.3 (2023 NSO, well below replacement) | 379 reading (PISA 2022) | Lower | Mid (98-day maternity leave; aging fastest in SE Asia; rural public schools weak, Bangkok international tier strong) |
| ID | ~281 (2024 BPS) | ~30 (2024 BPS) | 2.1 (2023 BPS, at replacement) | 359 reading (PISA 2022) | Lower | Mid (3-month maternity leave; demographic dividend window through ~2030 per BPS; quality gap urban-rural severe) |
| MY | ~34.1 (2024 DOSM) | ~30 (2024 DOSM) | 1.6 (2023 DOSM, declining) | 388 reading (PISA 2022) | High | Mid (60-day maternity leave; multi-ethnic system Malay/Chinese/Tamil-medium public; private international tier strong in KL/Penang) |
| VN | ~100.3 (2024 GSO) | ~33 (2024 GSO) | 1.95 (2023 GSO, declining toward replacement) | 462 reading (PISA 2022, strong relative to peers) | Lower | Mid (6-month paid maternity leave — generous regionally; aging from a young base, "old before rich" risk per GSO) |
| PH | ~115 (2024 PSA) | ~25.7 (2024 PSA, youngest in SE Asia) | 2.7 (2023 PSA) | 347 reading (PISA 2022) | High | Mid (105-day paid maternity leave; English-medium public schools but quality variable; OFW remittances structure family economics) |

## Aging & dependency cliffs

Countries already past the demographic peak (population declining), highest concern:
- 🇯🇵 JP (49.4, 1.20) — oldest median globally; ~600k pop loss/year (2024 MHLW)
- 🇮🇹 IT (median 47.3, TFR 1.20) — accelerating decline
- 🇧🇬 BG (45.4, 1.65) — emigration overlay
- 🇭🇷 HR (44.3, 1.46)
- 🇵🇹 PT (46.0) — rural depopulation severe
- 🇱🇻 LV (44.5) — emigration to Western EU
- 🇱🇹 LT (45.0) — emigration to Western EU
- 🇷🇸 RS (44.4) — emigration
- 🇹🇭 TH (~40, 1.3) — fastest-aging in SE Asia; record-low TFR (2023 NSO)
- 🇬🇪 GE (~38, 1.7) — emigration sustained (2024 Geostat)

Countries with stable / growing demographics:
- 🇮🇱 IL (30.5, 2.89) — highest TFR in OECD (2023 CBS)
- 🇪🇬 EG (~25, 2.85) — high TFR but declining (2023 CAPMAS)
- 🇵🇭 PH (25.7, 2.7) — youngest median in skill (2024 PSA)
- 🇩🇴 DO (~28, 2.3) — replacement-plus
- 🇿🇦 ZA (~28, 2.3) — high TFR but HIV-affected adult mortality (2024 Stats SA)
- 🇲🇦 MA (~30, 2.1) — at replacement
- 🇮🇩 ID (~30, 2.1) — demographic dividend window through ~2030 (2024 BPS)
- 🇻🇳 VN (~33, 1.95) — declining toward replacement
- 🇮🇪 IE (38.6, 1.54) — strong inbound migration + native growth
- 🇮🇸 IS (37.8, 1.59) — youngest median in skill
- 🇨🇭 CH (42.7, 1.39) — net migration positive
- 🇱🇺 LU (39.7, 1.30) — cross-border + EU staff inflow
- 🇲🇽 MX (30.5, 1.81) — youngest in skill (LatAm)
- 🇵🇦 PA (31.4, 2.18) — TFR above replacement!
- 🇨🇦 CA (41.9, 1.30) — large immigration uplift
- 🇺🇸 US (38.9, 1.66) — net migration positive (2024 Census Bureau)
- 🇦🇪 AE (~33, 1.4) — expat-driven, ~88% non-citizen workforce (2022 FCSC)

## English-proficiency tiers (EF EPI 2025 cycle — non-government, treat as relative ranking)

- **Native**: UK, IE, AU, NZ, CA, US
- **Very High**: NL, AT, BE, FI, SE, NO, DK, DE, LU, IE, EE, MT, IL
- **High**: PT, GR, CY, SI, HR, LT, LV, AR, MY, PH, UY
- **Moderate**: FR, IT, ES, PL, CZ, SK, HU, RO, RS, ME, BA, MK, MX, BR, CR, PA, GE, AE, ZA, CO, CL
- **Lower-Moderate**: DO
- **Lower**: AL, BG (improving), MK (lower), TR, MA, EG, TH, ID, VN

## PISA rank distinction (2022 results published Dec 2023; 2025 cycle results expected late 2026)

Top tier (>500 reading):
- 🇮🇪 IE (516), 🇯🇵 JP (516), 🇪🇪 EE (511), 🇨🇦 CA (507), 🇺🇸 US (504), 🇳🇿 NZ (501)

Strong tier (480-500):
- 🇸🇬 SG (not in skill), most Nordic + DE/AT/CH/UK

Mid (440-480):
- Most other EU + Anglo non-EU + 🇮🇱 IL (474), 🇻🇳 VN (462), 🇹🇷 TR (456), 🇨🇱 CL (448)

Lower-mid (400-440):
- 🇮🇹 IT, 🇪🇸 ES, 🇬🇷 GR, 🇨🇾 CY, 🇲🇹 MT (small systems), 🇧🇬 BG, 🇷🇴 RO, all Balkans except SI, 🇺🇾 UY (430), 🇦🇪 AE (417), 🇨🇴 CO (409)

Lower (<400):
- 🇲🇾 MY (388), 🇹🇭 TH (379), 🇬🇪 GE (374), 🇮🇩 ID (359), 🇵🇭 PH (347), 🇲🇦 MA (339)
- Not in PISA: 🇩🇴 DO, 🇿🇦 ZA, 🇪🇬 EG (TIMSS / LLECE alternatives only)

## Family-friendliness composite signals

Strongest (parental leave, free childcare, school quality, work-life balance):
- 🇸🇪 SE, 🇫🇮 FI, 🇩🇰 DK, 🇳🇴 NO, 🇮🇸 IS — Nordic model
- 🇩🇪 DE, 🇦🇹 AT, 🇧🇪 BE, 🇳🇱 NL, 🇫🇷 FR — Continental Europe strong
- 🇮🇪 IE, 🇨🇦 CA, 🇦🇺 AU, 🇳🇿 NZ — Anglo-sphere with social-democratic streak
- 🇸🇮 SI, 🇨🇿 CZ — Surprising Eastern strength
- 🇯🇵 JP — top-tier school quality + recent parental-leave expansion (Kishida policy)
- 🇮🇱 IL — strong family infrastructure + highest TFR in OECD
- 🇻🇳 VN — 6-month paid maternity leave (regionally generous)

Mid-tier:
- 🇺🇸 US — strong universities + suburban schools, weak federal family policy (no paid leave; childcare ~22% household income, 2023 Treasury)
- 🇦🇪 AE, 🇲🇾 MY, 🇹🇭 TH — strong international/private school options, public quality variable
- 🇺🇾 UY, 🇨🇱 CL — top in LatAm by school metrics; UY notable for Plan Ceibal

Weakest:
- LatAm informal urban (excluding strong middle-class enclaves)
- Western Balkans (improving)
- 🇪🇬 EG, 🇲🇦 MA, 🇵🇭 PH, 🇮🇩 ID, 🇩🇴 DO — public schools severely under-resourced; quality concentrated in private/international tier

## Anti-hallucination

- **Cite Eurostat / OECD / World Bank / UN DESA** as primary; date-stamp data
- **National stats offices** (Census Bureau US, TÜİK TR, FCSC AE, Stat Bureau JP, NSO TH, ONE DO, DANE CO, INE UY/CL, Stats SA, Geostat GE, BPS ID, DOSM MY, GSO VN, PSA PH, CBS IL, HCP MA, CAPMAS EG) are primary for in-country data
- **PISA cycle is 3-year**; 2022 results are still authoritative until late 2026 (next cycle 2025 results expected late 2026)
- **PISA participation is voluntary** — DO, ZA, EG do not participate; use TIMSS / UNESCO LLECE alternatives, do NOT extrapolate
- **Population projections** are uncertain — use UN WPP medium variant
- **TFR varies substantially by year** — use latest single-year data, not multi-year; flag record-lows (JP 2024, TR 2023, CL 2023, TH 2023)
- **EF EPI** is non-government and methodology-disputed — use as a relative ranking, not absolute
- **Expat-skewed populations** (AE: ~88% expat per 2022 FCSC) — citizen TFR and expat aggregate diverge sharply; quote both when relevant
- **Israel TFR** is heavily driven by ultra-Orthodox/Haredi sub-population (~6.5 vs secular ~2.0 per 2023 CBS) — aggregate masks composition

## Status

Last refreshed: 2026-05-01 (Tier-1 + Tier-2 expansion: +18 countries — US, TR, AE, JP, TH, DO, CO, UY, CL, ZA, GE, ID, MY, VN, PH, IL, MA, EG).
**Confidence**: MEDIUM-HIGH overall — primary national stats office citations for population/TFR; PISA 2022 cycle for school benchmarks where countries participate; TIMSS/LLECE alternatives flagged for non-PISA participants. Re-verify TFRs annually given record-low volatility in JP/TR/TH/CL.
