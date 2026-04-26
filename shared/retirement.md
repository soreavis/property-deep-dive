# Universal `--retirement` Section

Retiree-specific filter overlay: pension taxation, healthcare access, climate, expat communities. Combines with `--all` or `--compare` to surface retirement-relevant facets.

**Snapshot**: April 2026.

## Universal contract

For the property's country, return:
1. **Pension taxation** (foreign-source pension treatment)
2. **Healthcare access** (EU EHIC vs S1 form vs private)
3. **Climate suitability** (heatwaves, mild winters, humidity)
4. **Expat retiree community size** (English-speaking density)
5. **Cost of living** (relative to base country)
6. **Language barrier** (English availability in healthcare/admin)
7. **Special retirement programs** (where they exist)

## Output template

```markdown
## Retirement Profile

**Country**: <ISO2>
**Pension taxation (foreign-source)**: <regime>
**Healthcare access**: <EU S1 / private / dual / state>
**Climate suitability**: <evaluation>
**Expat retiree community**: <size>
**Cost of living vs <base>**: <ratio>
**English in healthcare/admin**: <high | mixed | low>
**Special programs**: <list>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Pension-taxation regimes

### Most favourable (low/no tax on foreign-source pension)

| Country | Regime | Threshold / conditions |
|---|---|---|
| **PT** | **IFICI / NHR 2.0** (replaced classic NHR Mar 2024) — research/innovation only; **pensions NO LONGER exempt under IFICI** (must pay PT progressive PIT) | EQF L6+ degree, scientific research / certified tech startup / export co only |
| **GR** | **Foreign Pensioner Tax Regime** — 7% flat on foreign-source income for 15 years for new tax residents who haven't been GR tax resident in 5 of last 6 years | Application via AADE; 7% covers worldwide income |
| **IT** | **Southern Italy 7% regime** — flat 7% for 9 years on foreign-source income for retirees moving to municipalities <20,000 pop in S Italy | First-time tax residency in IT in last 5 years |
| **CY** | **17-year non-dom regime** — exempt SDC; foreign pension may be taxed at 5% flat (over €3,420 pa) OR Cyprus marginal rate | Choose annually |
| **MT** | **MPRP residency** + flat 15% on foreign-remitted income (Maltese non-dom rule) | Min stay requirements |
| **PA** | **Pensionado program** (most generous LatAm) — US$1,000/mo lifetime pension qualifies; no PA tax on foreign-source income (territorial system) | |
| **MX** | **Temporary/Permanent residency** — no foreign-source pension tax under territorial principles for non-residents-tax (be cautious — verify per-program) | |
| **CR** | **Rentista visa** — US$2,500/mo income; CR doesn't tax foreign-source income for non-residents | |

### Less favourable (foreign pension taxed at marginal/progressive)

| Country | Regime |
|---|---|
| FR | Worldwide income; tax-treaty avoids double taxation but progressive rates apply |
| ES | Worldwide; pensions taxed at general scale (post-Beckham Law sunset) |
| DE | Worldwide; pensions partially taxable (rising portion until 100% by 2058) |
| UK | Worldwide for tax residents; double-tax treaty with most |
| US | Citizenship-based taxation — worldwide regardless of residency (unique) |
| CA | Worldwide for residents |

### Pension tax special cases

- **CY 5% pension regime**: optional alternative — flat 5% on foreign pension income above €3,420 (effectively a 5% marginal once threshold passed)
- **DK borgerservice**: tax law treats foreign pensions as taxable but with credit for foreign tax paid
- **NL Box 1 pension treatment**: foreign pensions usually taxed at progressive rates; treaty-based exemption case-by-case

## Healthcare access

### EU/EEA (S1 form for retirees from another EU country)
S1 form lets you access host-country state healthcare while it's billed back to your home country. Available throughout EU+EEA+CH for state-pension recipients.

| Country | Public healthcare quality (2025 ranking-style) | Notes |
|---|---|---|
| FR | Excellent (universal Sécu) | English in major cities limited |
| ES | Excellent (SNS) | English coastal/expat areas |
| PT | Good (SNS); waiting lists | English coastal/Algarve |
| IT | Good (SSN) regional variation | English Tuscany/major cities |
| GR | Mid (EOPYY) — private gap-cover common | English in tourist areas |
| MT | Good (state hospitals); English-speaking | English everywhere |
| CY | Good (GeSY 2019); English-speaking | English everywhere |
| LU | Excellent (CNS) | French/German/Lëtzebuergesch |
| DE | Excellent (multi-payer GKV/PKV) | German required for admin |
| AT | Excellent (ÖGK) | German required |
| CH | Excellent (LAMal mandatory private) | Multilingual incl. English in cities |
| NL | Excellent (Zvw) | English widely spoken |
| BE | Excellent (mutuelles/ziekenfonds) | French/Dutch/German |
| DK | Excellent (universal) | Danish required |
| SE | Excellent (universal) | English widely spoken |
| FI | Excellent (Kela) | English widely spoken |
| NO | Excellent (HELFO) | English widely spoken |
| IS | Excellent (state) | English widely spoken |
| IE | Mixed (HSE waiting lists; private gap) | English |

### Non-EU
- **UK NHS**: free for residents; non-resident must pay or use private; post-Brexit S1 still available for some pre-2021 retirees
- **AU Medicare**: residents/PR; reciprocal agreements with UK/IE/NL/SE/FI/NO/IT/MT/SI/BE
- **NZ**: residents; reciprocal with UK/AU
- **CA**: provincial residency required (typically 3-month waiting period)
- **US**: Medicare available at 65 if 10+ years payroll contributions; otherwise private
- **MX/BR/AR/CR/PA**: state healthcare exists but expat retirees commonly use private (much cheaper than US, comparable to EU)

## Climate suitability for retirement

### Mild winters + manageable summers (preferred)
1. **PT (Algarve, Lisbon, Madeira)** — 18-23°C winter days; coastal cooling
2. **ES (Costa del Sol, Costa Blanca, Canarias)** — 17-22°C winter
3. **GR (Crete, Cyprus, southern Peloponnese)** — 15-20°C winter
4. **IT (Sicily, Calabria, Puglia)** — 12-18°C winter; rising heatwave concern
5. **MT, CY** — 14-20°C winter; **water scarcity rising** (CY 2025 worst drought)

### Cold but stable, indoor-life-friendly
1. **DE, AT, CH, FR, BE, NL, LU, IE, UK, DK, SE, FI, NO, IS** — heating-cost concern; northern long darkness
2. **CZ, SK, PL, HU, BG, RO** — colder; cheaper

### Hot summers — emerging concern
- **ES interior, S Italy, GR mainland**: 40°C+ summer days increasingly common (2003, 2022, 2023, 2024 heatwaves)
- **PT interior**: similar; coastal milder
- **CY, MT, S IT**: water-scarcity overlay

### Avoid for climate-sensitive retirees
- 🇮🇸 IS: harsh winters, volcanic ash episodes, Reykjanes eruption series 2023+
- 🇸🇪🇫🇮🇳🇴 SE/FI/NO N: long dark winters, mood-affective concern
- 🇫🇷🇮🇹 inland mountain valleys: severe winter
- ME / AL coastal: high summer humidity + tourism crowds

## Expat retiree community density

### Established / largest
1. 🇪🇸 ES (Costa del Sol, Costa Blanca, Mallorca) — UK + DE + NL + Scandinavian retiree clusters; English+German+Dutch services pervasive
2. 🇵🇹 PT (Algarve, Lisbon, Madeira, Cascais) — UK + DE + FR + NL retirees; English-medium businesses
3. 🇫🇷 FR (Provence, Dordogne, Languedoc, Côte d'Azur) — UK + NL + DE retirees
4. 🇮🇹 IT (Tuscany, Umbria, Puglia, Sicily) — UK + DE + US retirees
5. 🇨🇾 CY (Paphos especially) — UK + Russian retirees
6. 🇲🇹 MT — UK + DE + IT retirees; English-medium

### Growing
- 🇲🇽 MX (San Miguel de Allende, Lake Chapala, Mérida, Playa del Carmen) — US/CA retirees
- 🇵🇦 PA (Boquete, Coronado, Panama City) — US/CA retirees
- 🇨🇷 CR (Atenas, Tamarindo, Manuel Antonio) — US/CA retirees
- 🇭🇺 HU (Budapest) — UK/DE retirees post-2020
- 🇲🇪 ME (Coastal Budva, Tivat) — RU pre-2022 historically; rebalancing
- 🇦🇱 AL (Saranda, Vlora) — IT/UK retirees post-2020

### Limited / language-barrier
- 🇩🇪🇦🇹🇨🇭 DE/AT/CH inland: German required for admin
- Nordics: limited expat retiree community due to cost
- Eastern EU + Balkans: smaller communities

## Cost of living rough ranking (cheapest → expensive for retirees)

| Tier | Countries |
|---|---|
| **Cheap** | AL, BA, RS, MK, ME, BG, RO, HU |
| **Mid-low** | PL, CZ, SK, GR, PT, ES (interior), IT (S), CR, PA, MX |
| **Mid** | ES (coast), PT (Lisbon/Algarve), IT (TC/Umbria), HR, CY, MT, EE, LV, LT |
| **Mid-high** | FR, DE, AT, NL, BE, IE, UK, FI, SE, DK |
| **Expensive** | CH, NO, IS, LU, MC (not in skill), SG (not in skill) |

## Special retirement programs

| Country | Program | Threshold |
|---|---|---|
| GR | Foreign Pensioner Tax Regime | 7% flat on foreign-source for 15 yrs |
| IT | Southern Italy 7% regime | 7% flat for 9 yrs (S municipalities <20k pop) |
| PT | IFICI (NHR 2.0) | Pensions NO LONGER exempt — narrower scope |
| PA | Pensionado | $1,000/mo pension; massive discounts on services |
| CR | Pensionado | $1,000/mo (lifetime pension); Rentista $2,500/mo |
| MX | Temp/Permanent residency | Income/savings thresholds (UMA-based) |
| MY (not in skill) | MM2H | suspended/restricted post-2021; verify if added |
| TH (not in skill) | Long-Term Resident (LTR) Visa | $80k income / $1m wealth thresholds — verify if added |

## Decision framework for retirees

```
1. CITIZENSHIP CHECK → which countries does your passport let you settle in?
   - EU citizen: 27 EU + EEA freely; UK requires visa post-Brexit
   - UK citizen: post-Brexit visa for EU; FOM remains for IE
   - US/CA citizen: visa-free tourism most; settlement requires visa
   - LatAm: most allow visa-free 90 days; settlement easier than EU

2. PENSION TAX → where will your pension be most tax-efficient?
   - Filter: GR 7%, IT 7% (S), PT IFICI (narrow), CY 5%, PA territorial, MX territorial, CR territorial

3. HEALTHCARE → where will your healthcare be best/cheapest?
   - EU pensioner with S1: any EU member state (PT/ES/IT/GR/MT/CY popular)
   - Non-EU: private insurance + state where reciprocal exists
   - Quality + access: PT > ES > IT > GR > MT > CY (public-system rough order)

4. CLIMATE → can you tolerate the climate year-round?
   - Mild winter: PT, ES, IT (south), GR, MT, CY, MX, PA, CR
   - Cool summer: NL, BE, IE, UK, FR (Brittany/Normandy), DE (north), Nordics
   - Both (rare): PT (Lisbon), ES (Galicia/N coast), FR (Atlantic coast)

5. LANGUAGE → can you live in the language?
   - English-friendly: NL, IE, UK, MT, CY, PT (Algarve coast), some SE/FI/NO/DK
   - Dual: BE, CH, LU, DE/AT (English in cities), ES coastal, IT (some)
   - Required learning: rest

6. BUDGET → does the cost align?
   - <€1,500/mo: AL, BA, RS, MK, ME, BG, RO
   - €1,500-2,500: PT (interior), ES (interior), IT (S), HR, GR, MT, CY, EE/LV/LT, MX, PA, CR
   - €2,500-4,000: PT/ES/IT (coastal), FR (provincial), DE/AT (provincial), NL, BE
   - €4,000+: CH, NO, IS, LU; major capitals (Paris, London, Amsterdam, Munich)
```

## Anti-hallucination

- **Pension tax regimes change** — IT 7%, GR 7%, PT NHR all reformed in 2023-2024 cycle. Always verify with home + host-country tax adviser
- **Healthcare reciprocity rules change post-Brexit, post-2024 EU directives** — verify S1 eligibility before committing
- **Climate ranking is current-decade snapshot** — climate trajectory (`--climate`) is the forward-looking view
- **Cost-of-living tier is broad-stroke** — actual costs vary 2-3× between provincial and capital within most countries

## Status

Last refreshed: 2026-04-26.
