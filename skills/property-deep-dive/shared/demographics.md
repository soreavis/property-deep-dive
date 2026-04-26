# Universal `--demographics` Section

Population, aging, schools, family-friendly metrics across 44 supported countries. Useful for relocation/family decisions and long-term valuation outlook.

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

## Aging & dependency cliffs

Countries already past the demographic peak (population declining), highest concern:
- 🇮🇹 IT (median 47.3, TFR 1.20) — accelerating decline
- 🇧🇬 BG (45.4, 1.65) — emigration overlay
- 🇭🇷 HR (44.3, 1.46)
- 🇵🇹 PT (46.0) — rural depopulation severe
- 🇱🇻 LV (44.5) — emigration to Western EU
- 🇱🇹 LT (45.0) — emigration to Western EU
- 🇷🇸 RS (44.4) — emigration

Countries with stable / growing demographics:
- 🇮🇪 IE (38.6, 1.54) — strong inbound migration + native growth
- 🇮🇸 IS (37.8, 1.59) — youngest median in skill
- 🇨🇭 CH (42.7, 1.39) — net migration positive
- 🇱🇺 LU (39.7, 1.30) — cross-border + EU staff inflow
- 🇲🇽 MX (30.5, 1.81) — youngest in skill
- 🇵🇦 PA (31.4, 2.18) — TFR above replacement!
- 🇨🇦 CA (41.9, 1.30) — large immigration uplift

## English-proficiency tiers (EF EPI 2025-ish)

- **Native**: UK, IE, AU, NZ, CA, US (not in skill yet)
- **Very High**: NL, AT, BE, FI, SE, NO, DK, DE, LU, IE, EE, MT
- **High**: PT, GR, CY, SI, HR, LT, LV, AR
- **Moderate**: FR, IT, ES, PL, CZ, SK, HU, RO, RS, ME, BA, MK, MX, BR, CR, PA
- **Lower**: AL, BG (improving), MK (lower)

## PISA rank distinction (2022 results published Dec 2023; 2025 cycle results expected late 2026)

Top tier (>500 reading):
- 🇮🇪 IE (516), 🇪🇪 EE (511), 🇨🇦 CA (507), 🇳🇿 NZ (501)

Strong tier (480-500):
- 🇸🇬 SG (not in skill), most Nordic + DE/AT/CH/UK

Mid (440-480):
- Most other EU + Anglo non-EU

Lower (<440):
- 🇮🇹 IT, 🇪🇸 ES, 🇬🇷 GR, 🇨🇾 CY, 🇲🇹 MT (small systems), 🇧🇬 BG, 🇷🇴 RO, 🇽🇰 (not in skill), all Balkans except SI

## Family-friendliness composite signals

Strongest (parental leave, free childcare, school quality, work-life balance):
- 🇸🇪 SE, 🇫🇮 FI, 🇩🇰 DK, 🇳🇴 NO, 🇮🇸 IS — Nordic model
- 🇩🇪 DE, 🇦🇹 AT, 🇧🇪 BE, 🇳🇱 NL, 🇫🇷 FR — Continental Europe strong
- 🇮🇪 IE, 🇨🇦 CA, 🇦🇺 AU, 🇳🇿 NZ — Anglo-sphere with social-democratic streak
- 🇸🇮 SI, 🇨🇿 CZ — Surprising Eastern strength

Weakest:
- LatAm (excluding strong middle-class urban areas)
- Western Balkans (improving)

## Anti-hallucination

- **Cite Eurostat / OECD / World Bank** as primary; date-stamp data
- **PISA cycle is 3-year**; 2022 results are still authoritative until late 2026
- **Population projections** are uncertain — use UN WPP medium variant
- **TFR varies substantially by year** — use latest single-year data, not multi-year
- **EF EPI** is non-government and methodology-disputed — use as a relative ranking, not absolute

## Status

Last refreshed: 2026-04-26.
