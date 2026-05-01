# Universal `--retirement` Section

Retiree-specific filter overlay: pension taxation, healthcare access, climate, expat communities. Combines with `--all` or `--compare` to surface retirement-relevant facets.

**Snapshot**: May 2026 (extended to 54 countries — Tier-1 + Tier-2 expansion).

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
| **AE** | **Retirement Visa (5-yr renewable)** — NO income/pension tax; territorial system; Federal Decree-Law 47/2022 introduced 9% corporate tax but personal income (incl. foreign pensions) remains untaxed | Age 55+; AED 1M property OR AED 1M savings OR AED 20k/mo income (verify 2026 thresholds at GDRFA) |
| **TH** | **LTR Wealthy Pensioner** — flat 17% on assessable income (most categories); foreign-source income remitted to TH may be taxable post-2024 reform — verify with Revenue Dept | Age 50+; USD 80k/yr passive income OR USD 40-80k + USD 250k investment |
| **PH** | **SRRV (Special Resident Retiree's Visa)** — foreign pension NOT taxed by PH; territorial-style for non-resident-source income | Age 35+ (some classes); USD 10k–50k deposit depending on age/pension status |
| **MY** | **MM2H (Malaysia My Second Home)** — foreign-source income exempt under territorial principle (post-2022 amendments narrowed for residents — verify) | 3-tier (Silver/Gold/Platinum) post-2024; thresholds RM 500k–RM 5M deposit |
| **DO** | **Investor/Pensionado visa** — foreign pension exempt from DO tax; territorial system; 50% discount on transfer tax + property tax under retirement law | USD 1.5k/mo pension OR USD 200k investment route |
| **UY** | **Tax residency** — 11-yr exemption on foreign-source interest+dividends (Ley 19.937); pension itself not exempt but progressive PIT modest; territorial-leaning | Investment OR 60-day physical presence routes |
| **GE** | **Visa-free 1-year** for ~95 nationalities; territorial tax — foreign-source income not taxed | No formal retirement visa needed for most |
| **EG** | **Investment Law 160/2023 PR route** — foreign-source pension generally not taxed by EG (territorial application varies) | USD 250k cash deposit → permanent residency |

### Less favourable (foreign pension taxed at marginal/progressive)

| Country | Regime |
|---|---|
| FR | Worldwide income; tax-treaty avoids double taxation but progressive rates apply |
| ES | Worldwide; pensions taxed at general scale (post-Beckham Law sunset) |
| DE | Worldwide; pensions partially taxable (rising portion until 100% by 2058) |
| UK | Worldwide for tax residents; double-tax treaty with most |
| US | Citizenship-based taxation — worldwide regardless of residency (unique) |
| CA | Worldwide for residents |
| TR | Worldwide for tax residents; pensions taxed at progressive PIT (2026: 15%-40%); treaty network mitigates double-tax |
| JP | Worldwide for residents; foreign pension taxable but treaty-relief (US-JP, UK-JP, etc.) common; "non-permanent resident" 5-year carve-out for non-Japan-source income not remitted |
| CO | Worldwide for tax residents (>183 days); pensionado visa holders pay CO PIT; UVT-based progressive rates |
| CL | Worldwide post-3-yr (3-year exemption for new residents on foreign-source income — Art. 3 DL 824); pensions taxable thereafter at progressive PIT (2026: up to 40%) |
| ZA | Worldwide for tax residents; foreign pension may be exempt under s10(1)(gC) ITA if for services rendered abroad — verify per-case |
| ID | Worldwide for residents (>183 days); foreign pension taxable at progressive PIT; some treaty relief |
| VN | Worldwide for residents (>183 days); foreign pension taxable at progressive PIT (2026: up to 35%) |
| IL | Worldwide for residents BUT new immigrants (Olim) get **10-year tax holiday** on foreign-source income+capital gains (Amendment 168, 2008) |
| MA | Foreign-source pensions: **80% abatement** if transferred permanently to MA in DH (Art. 76 CGI); effective rate dramatically reduced |

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
- **US**: Medicare available at 65 if 10+ years payroll contributions; resident-only; ACA marketplace alternative for under-65 retirees; state-level variation (TX/FL no state income tax; CA/NY high)
- **MX/BR/AR/CR/PA**: state healthcare exists but expat retirees commonly use private (much cheaper than US, comparable to EU)
- **TR**: SGK universal scheme available to residents (incl. expat retirees with residence permit); private network strong (Acibadem, Memorial); cost ~30-50% of UK private
- **AE**: NO universal public system for expats; mandatory private health insurance via DHA (Dubai) / DOH (Abu Dhabi); high quality, premium pricing for retirees age 60+
- **JP**: National Health Insurance (NHI / Kokuho) covers all residents incl. expats; 30% co-pay; quality high but **language barrier severe**; English-speaking clinics concentrated in Tokyo/Yokohama/Osaka
- **TH**: Universal Coverage Scheme for citizens; expats use private (Bumrungrad, Bangkok Hospital — internationally accredited); LTR visa requires USD 50k health insurance OR USD 100k deposit
- **DO**: SeNaSa public + private SDSS; expats overwhelmingly use private (Hospiten, CEDIMAT); Medicare-style coordination with US insurance limited
- **CO**: EPS contributory system (residents pay ~12% income); private (Sanitas, Colsanitas) strong; Medellín/Bogotá quality compares to US private at fraction of cost
- **UY**: Mutualistas (private cooperatives) excellent — most expats join (~USD 80-150/mo); FONASA public for residents
- **CL**: Dual system — FONASA (public) OR Isapres (private); retirees often Isapres but premiums rise sharply with age (post-2023 Constitutional Court ruling reshaping pricing)
- **ZA**: Public healthcare overstretched; expats universally use private (Discovery Health, Bonitas) + medical aid scheme; quality-cost ratio strong but ZAR volatility risk
- **GE**: Universal Healthcare Program (state) for citizens/residents; private clinics (Mediclub, Medi) growing; Tbilisi quality fair but expats often medivac for serious conditions
- **ID**: BPJS Kesehatan (universal) for residents incl. KITAS/KITAP holders; quality variable; expats in Bali commonly use private (BIMC, Siloam); medivac to SG common for serious cases
- **MY**: Universal public system + strong private (Sunway, Pantai, Gleneagles); Penang/KL hospitals internationally accredited; **medical-tourism destination**
- **VN**: Universal Health Insurance for residents; expats use private (Vinmec, FV Hospital); Saigon/Hanoi quality fair-good but evac to TH/SG for complex cases
- **PH**: PhilHealth universal for residents; private (St. Luke's, Makati Med) strong in Metro Manila; provincial quality patchy
- **IL**: Universal via 4 Sick Funds (Kupot Holim — Clalit, Maccabi, Meuhedet, Leumit); excellent quality; **Olim entitled from arrival**; English support varies
- **MA**: AMO universal scheme being expanded (2024-2026 reform); expats use private (Cliniques Akdital, Cheikh Zaid); French-system standards
- **EG**: New Universal Health Insurance (2018 law, phased rollout); expats use private (Cleopatra, As-Salam International); Cairo quality fair; **medivac for serious cases recommended**

## Climate suitability for retirement

### Mild winters + manageable summers (preferred)
1. **PT (Algarve, Lisbon, Madeira)** — 18-23°C winter days; coastal cooling
2. **ES (Costa del Sol, Costa Blanca, Canarias)** — 17-22°C winter
3. **GR (Crete, Cyprus, southern Peloponnese)** — 15-20°C winter
4. **IT (Sicily, Calabria, Puglia)** — 12-18°C winter; rising heatwave concern
5. **MT, CY** — 14-20°C winter; **water scarcity rising** (CY 2025 worst drought)
6. **TR (Aegean coast — Bodrum, Antalya, Fethiye)** — 14-19°C winter; summer heatwaves rising
7. **MA (Marrakech, Essaouira, Tangier)** — 18-22°C winter; Atlantic coast cooler than interior
8. **CL (Coquimbo, Ñuble coast)** — 12-18°C winter; Mediterranean climate; arid trend (drought)
9. **UY (Punta del Este, Montevideo)** — 12-16°C winter; humid subtropical
10. **ZA (Cape Town, Garden Route)** — 12-18°C winter; Mediterranean climate; **water-scarcity overlay (Day Zero risk)**
11. **CO (Medellín "City of Eternal Spring")** — 18-22°C year-round; altitude-moderated
12. **MX (already listed)** — verify
13. **US (FL/AZ/TX/CA-S)** — 15-25°C winter; FL hurricane season + AZ extreme summer heat trade-offs

### Tropical / hot year-round
- **TH (Phuket, Chiang Mai, Hua Hin)** — 22-32°C; Chiang Mai cool-season Nov-Feb; **PM2.5 burning season Feb-Apr severe in N**
- **PH (Cebu, Bohol, Davao)** — 25-32°C; typhoon season Jun-Nov (Davao less typhoon-exposed)
- **MY (Penang, KL, Johor)** — 25-32°C year-round; humid; minimal seasonal variation
- **ID (Bali, Lombok)** — 26-30°C; wet/dry seasons; volcanic risk
- **VN (Da Nang, Hoi An, Saigon)** — 22-32°C; Da Nang/Hoi An typhoon Sep-Nov
- **DO (Las Terrenas, Punta Cana)** — 24-31°C; hurricane season Jun-Nov
- **EG (Hurghada, Sahel, Sharm)** — 18-35°C; very dry; summer extreme
- **AE (Dubai, Abu Dhabi)** — 18-42°C; **summer 45°C+ near-uninhabitable outdoors May-Sep**

### Cold but stable (added)
- **JP (Tokyo, Osaka, Fukuoka)** — 5-10°C winter; humid summers; well-heated indoors
- **GE (Tbilisi)** — 2-7°C winter, 25-30°C summer; continental
- **IL (Tel Aviv, Jerusalem, Haifa)** — 10-18°C winter; hot dry summers

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
- 🇹🇷 TR (Bodrum, Antalya, Fethiye, Alanya) — UK/DE/RU/Scandinavian retirees; large established community since 2000s
- 🇹🇭 TH (Chiang Mai, Hua Hin, Phuket) — UK/US/AU/DE/Scandinavian; Chiang Mai US/EU writer-retiree hub
- 🇲🇾 MY (Penang, KL, Johor Bahru) — UK/AU/SG/JP retirees via MM2H legacy + new tiers
- 🇵🇭 PH (Cebu, Dumaguete, Bohol, Davao) — US/AU/JP/KR retirees via SRRV (most generous SE-Asia program)
- 🇮🇩 ID (Bali — Ubud, Canggu, Sanur) — AU/EU/US retirees via KITAP
- 🇻🇳 VN (Da Nang, Hoi An, Saigon expat enclaves) — growing US/EU/AU; visa pathway thinner than TH/PH/MY
- 🇩🇴 DO (Las Terrenas FR/IT enclave; Punta Cana US/CA; Sosúa DE/Scandinavian) — diverse expat communities
- 🇨🇴 CO (Medellín — El Poblado, Laureles; Cartagena) — surge in US/CA digital-nomad-aging-into-retirement crowd
- 🇺🇾 UY (Punta del Este AR seasonal + permanent EU; Colonia) — moderate but high-quality
- 🇨🇱 CL (Viña del Mar, La Serena) — small but growing US/EU
- 🇿🇦 ZA (Cape Town, Plettenberg Bay, Knysna) — UK/DE/NL retirees; Garden Route established
- 🇬🇪 GE (Tbilisi, Batumi) — RU+UA post-2022 surge; growing US/EU crypto-retiree subsegment
- 🇮🇱 IL (Tel Aviv, Netanya, Ra'anana, Jerusalem) — US/FR/UK/RU Olim retirees; large established community
- 🇲🇦 MA (Marrakech, Essaouira, Tangier, Agadir) — FR retirees dominant; UK/DE growing
- 🇪🇬 EG (Hurghada, El Gouna, Sahel) — RU/UA/DE/UK retirees; **currency volatility risk material**
- 🇦🇪 AE (Dubai marinas, Abu Dhabi) — UK/IN/RU/EU; new Retirement Visa post-2018
- 🇯🇵 JP (Tokyo, Yokohama, Fukuoka) — small but established US/UK; **no formal retirement visa**, HSP/Investor route only

### Limited / language-barrier
- 🇩🇪🇦🇹🇨🇭 DE/AT/CH inland: German required for admin
- Nordics: limited expat retiree community due to cost
- Eastern EU + Balkans: smaller communities
- 🇯🇵 JP — Japanese required outside expat enclaves; admin almost exclusively JP-language
- 🇪🇬 EG — Arabic-dominant; French in some elite circles; English limited outside tourism
- 🇨🇴🇺🇾🇨🇱 CO/UY/CL — Spanish required for daily life
- 🇻🇳 VN — Vietnamese required; English limited outside tourism districts

## Cost of living rough ranking (cheapest → expensive for retirees)

| Tier | Countries |
|---|---|
| **Cheap** | AL, BA, RS, MK, ME, BG, RO, HU, GE, EG, VN, PH, ID, MA |
| **Mid-low** | PL, CZ, SK, GR, PT, ES (interior), IT (S), CR, PA, MX, TR, TH (provincial), CO, DO, ZA |
| **Mid** | ES (coast), PT (Lisbon/Algarve), IT (TC/Umbria), HR, CY, MT, EE, LV, LT, MY (KL/Penang), TH (Bangkok/Phuket), CL, UY |
| **Mid-high** | FR, DE, AT, NL, BE, IE, UK, FI, SE, DK, JP (regional), IL (peripheral), AE (mid-tier emirate) |
| **Expensive** | CH, NO, IS, LU, US (NYC/SF/Boston), JP (Tokyo central), IL (Tel Aviv), AE (Dubai prime) |

## Special retirement programs

| Country | Program | Threshold |
|---|---|---|
| GR | Foreign Pensioner Tax Regime | 7% flat on foreign-source for 15 yrs |
| IT | Southern Italy 7% regime | 7% flat for 9 yrs (S municipalities <20k pop) |
| PT | IFICI (NHR 2.0) | Pensions NO LONGER exempt — narrower scope |
| PA | Pensionado | $1,000/mo pension; massive discounts on services |
| CR | Pensionado | $1,000/mo (lifetime pension); Rentista $2,500/mo |
| MX | Temp/Permanent residency | Income/savings thresholds (UMA-based) |
| MY | **MM2H (3-tier post-2024 reform)** | Silver/Gold/Platinum tiers — RM 500k–RM 5M deposit + monthly income proof; verify with MoTAC |
| TH | **LTR Wealthy Pensioner** + Retirement (Non-O) | LTR: USD 80k/yr OR USD 40-80k + USD 250k investment; Non-O: age 50+, THB 800k bank or THB 65k/mo |
| PH | **SRRV (Special Resident Retiree's Visa)** | USD 10k–50k deposit (most generous SE-Asia); 4 sub-classes |
| ID | **Retirement KITAP** | Age 55+, USD 1.5k/mo pension proof, health insurance, hire local staff |
| AE | **Retirement Visa (5-yr renewable)** | Age 55+; AED 1M property OR AED 1M savings OR AED 20k/mo income |
| TR | **Turquoise Card / Long-stay residence** | No formal retirement program; Turquoise Card via investment route |
| ZA | **Retired Person Visa** | Pension/income ZAR 37,000/mo (~USD 2k/mo) — verify 2026 threshold at DHA |
| DO | **Pensionado / Rentista** | USD 1.5k/mo pension OR USD 2k/mo rentista; 50% discount on transfer + property tax |
| CO | **Migrante M Visa — Pensionado** | MOH-recognized pension >COP 3× SMLMV (~USD 1k/mo at 2026 SMLMV) |
| UY | **Tax residency** (no formal retirement visa) | 11-yr foreign interest+dividend exemption (Ley 19.937) |
| CL | Standard residency | No retirement-specific program; 3-yr foreign-income exemption from arrival |
| GE | **Visa-free 1 year** | ~95 nationalities; no retirement-specific scheme needed |
| IL | **Aliyah (Olim)** | Direct citizenship for Jewish ancestry; 10-year tax holiday on foreign income (Amendment 168) |
| MA | **Carte de Séjour (long-stay)** | Standard residence permit; pension 80% abatement if remitted in DH |
| EG | **Investment Law 160/2023 PR** | USD 250k cash deposit → permanent residency; verify currency-control / Form 4 risks |
| US | None federal; state-level | No US retirement visa for non-citizens (immigration via family/EB-5/marriage); domestic retirees: TX/FL/TN/NV/WA/SD/WY/AK no state income tax |
| JP | None retirement-specific | Highly Skilled Professional / Investor / Spouse routes; no pensioner-class visa |

## Decision framework for retirees

```
1. CITIZENSHIP CHECK → which countries does your passport let you settle in?
   - EU citizen: 27 EU + EEA freely; UK requires visa post-Brexit
   - UK citizen: post-Brexit visa for EU; FOM remains for IE
   - US/CA citizen: visa-free tourism most; settlement requires visa
   - LatAm: most allow visa-free 90 days; settlement easier than EU

2. PENSION TAX → where will your pension be most tax-efficient?
   - Filter EU/territorial: GR 7%, IT 7% (S), PT IFICI (narrow), CY 5%, PA territorial, MX territorial, CR territorial
   - Filter non-tax / favourable: AE (no PIT), UY (11-yr foreign-int+div), IL (10-yr Olim holiday), MA (80% abatement), GE (territorial), CL (3-yr new-resident exemption), DO/PA territorial-leaning
   - Caution: TH post-2024 remittance rules tightened — verify; JP has 5-yr "non-permanent resident" carve-out but limited

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
   - <€1,500/mo: AL, BA, RS, MK, ME, BG, RO, GE, EG, VN, PH (provincial), ID (provincial), MA (provincial)
   - €1,500-2,500: PT (interior), ES (interior), IT (S), HR, GR, MT, CY, EE/LV/LT, MX, PA, CR, TR (Aegean), TH (Chiang Mai/Hua Hin), CO (Medellín), DO (Las Terrenas), ZA (Garden Route)
   - €2,500-4,000: PT/ES/IT (coastal), FR (provincial), DE/AT (provincial), NL, BE, MY (KL/Penang), TH (Bangkok/Phuket prime), UY (Punta del Este), CL (coastal), JP (regional), IL (peripheral)
   - €4,000+: CH, NO, IS, LU, US (NYC/SF), JP (Tokyo central), IL (Tel Aviv), AE (Dubai prime); major capitals (Paris, London, Amsterdam, Munich)
```

## Tier-1 + Tier-2 country profiles (added 2026-05)

Each profile lists: pension-tax regime · healthcare access · climate/lifestyle · expat density · retirement-visa pathway. Cross-link each visa pathway to [`visa-programs.md`](./visa-programs.md) for thresholds and current status.

### 🇺🇸 US
- **Pension tax**: Worldwide PIT for residents; foreign-source pension taxable; treaty relief common (DTAA network)
- **Healthcare**: Medicare from age 65 (resident-only, requires 10+ yrs payroll contributions); ACA marketplace alternative for under-65; **state variation material** (TX/FL/TN/NV no state PIT)
- **Climate**: FL/AZ/CA-S/TX warm winters (FL hurricane Jun-Nov; AZ extreme summer)
- **Expat density**: N/A for inbound retirees (no retirement visa); retiree mobility is intra-state
- **Visa**: **No US retirement visa** — non-citizens enter via family/EB-5/spouse routes only

### 🇹🇷 TR
- **Pension tax**: Worldwide for tax residents; progressive PIT (2026: 15-40%); treaty mitigates double-tax
- **Healthcare**: SGK universal for residents incl. expats; private network strong (Acibadem, Memorial); ~30-50% of UK private cost
- **Climate**: Aegean coast (Bodrum, Antalya, Fethiye, Alanya) 14-19°C winter, 28-35°C summer; rising heatwave + water-stress concern
- **Expat density**: Large UK/DE/RU/Scandinavian retiree presence on Aegean coast since 2000s
- **Visa**: **Turquoise Card** (investment-route long-stay) or standard residence permit; no formal pension-class visa — see `visa-programs.md`

### 🇦🇪 AE
- **Pension tax**: **NO income/pension tax** for individuals; territorial system; corporate 9% (FDL 47/2022) doesn't reach personal pension income
- **Healthcare**: Mandatory private health insurance (DHA Dubai / DOH Abu Dhabi); high quality but **premiums spike post-60**
- **Climate**: 18-25°C winter (excellent); **summer 42-48°C May-Sep — outdoors near-uninhabitable**
- **Expat density**: Large UK/IN/RU/EU communities; Dubai marinas + Abu Dhabi
- **Visa**: **Retirement Visa (5-yr renewable, age 55+)** — AED 1M property OR AED 1M savings OR AED 20k/mo income — verify 2026 thresholds at GDRFA

### 🇯🇵 JP
- **Pension tax**: Worldwide for residents; foreign pension taxable but treaty-relief common; "non-permanent resident" 5-yr carve-out for non-JP-source income not remitted
- **Healthcare**: Universal NHI (Kokuho) for all residents incl. expats; 30% co-pay; **language barrier severe outside Tokyo/Yokohama/Osaka**
- **Climate**: 4-season; Tokyo 5-10°C winter, 28-32°C humid summer; Fukuoka/Okinawa milder
- **Expat density**: Small but established Western retiree community; concentrated in Tokyo/Yokohama/Fukuoka
- **Visa**: **No formal retirement visa** — Highly Skilled Professional / Investor / Spouse routes only; pathway thin for typical retirees

### 🇹🇭 TH
- **Pension tax**: LTR Wealthy Pensioner: flat 17% on most assessable income; **2024 remittance rule reform** — foreign-source income remitted to TH may now be taxable (verify with Revenue Dept / tax adviser)
- **Healthcare**: Universal Coverage Scheme for citizens; expats use private (Bumrungrad, Bangkok Hospital — JCI-accredited); LTR requires USD 50k health insurance OR USD 100k deposit
- **Climate**: Tropical 22-32°C; Chiang Mai cool-season Nov-Feb (best months); **PM2.5 burning season Feb-Apr severe in N TH**
- **Expat density**: UK/US/AU/DE/Scandinavian retirees; Chiang Mai writer/retiree hub, Hua Hin Royal-family adjacent, Phuket beach
- **Visa**: **LTR Wealthy Pensioner** (USD 80k/yr OR USD 40-80k + USD 250k investment) or **Non-O Retirement** (age 50+, THB 800k bank or THB 65k/mo) — see `visa-programs.md`

### 🇩🇴 DO
- **Pension tax**: Foreign pension exempt from DO tax; territorial system; **50% discount on transfer + property tax** under retirement law
- **Healthcare**: SeNaSa public + SDSS private; expats use private (Hospiten, CEDIMAT); coordination with US Medicare limited
- **Climate**: Tropical 24-31°C; **hurricane season Jun-Nov** (Atlantic exposure)
- **Expat density**: Las Terrenas FR/IT enclave; Punta Cana US/CA; Sosúa DE/Scandinavian — distinct national clusters
- **Visa**: **Pensionado (USD 1.5k/mo) / Rentista (USD 2k/mo) / Investor (USD 200k)** → 2-3 yr citizenship pathway

### 🇨🇴 CO
- **Pension tax**: Worldwide PIT for tax residents (>183 days); pensionado visa holders pay CO PIT at progressive UVT-based rates
- **Healthcare**: EPS contributory (residents pay ~12% income); private (Sanitas, Colsanitas) Medellín/Bogotá compares to US private at fraction of cost
- **Climate**: **Medellín "City of Eternal Spring"** 18-22°C year-round (altitude-moderated); Cartagena 26-32°C tropical
- **Expat density**: Surge in US/CA digital-nomad-aging-into-retirement; Medellín El Poblado/Laureles, Cartagena historic centre
- **Visa**: **Migrante M Visa Pensionado** — MOH-recognized pension >COP 3× SMLMV (~USD 1k/mo at 2026 SMLMV) — see `visa-programs.md`

### 🇺🇾 UY
- **Pension tax**: 11-year exemption on foreign interest+dividends (Ley 19.937, 2020+ reform); pension itself not exempt but progressive PIT modest; territorial-leaning
- **Healthcare**: Mutualistas (private cooperatives, ~USD 80-150/mo) excellent — most expats join; FONASA public for residents
- **Climate**: Humid subtropical; Punta del Este/Montevideo 12-16°C winter, 22-28°C summer
- **Expat density**: Moderate AR seasonal + permanent EU; Punta del Este, Colonia, Montevideo Carrasco
- **Visa**: **Tax residency** via investment OR 60-day physical presence; no formal retirement visa

### 🇨🇱 CL
- **Pension tax**: 3-yr foreign-source income exemption for new residents (DL 824 Art. 3); pensions taxable at progressive PIT thereafter (up to 40%)
- **Healthcare**: Dual FONASA / Isapres; retirees often Isapres but premiums rise sharply with age (post-2023 Constitutional Court ruling reshaping pricing)
- **Climate**: Mediterranean coast (Coquimbo, Ñuble) 12-18°C winter; arid trend / drought concern
- **Expat density**: Small but growing US/EU; Viña del Mar, La Serena
- **Visa**: Standard residency (no retirement-specific program); UF inflation-indexing protects real-asset purchases

### 🇿🇦 ZA
- **Pension tax**: Worldwide for tax residents; foreign pension may be exempt under s10(1)(gC) ITA if for services rendered abroad — verify per-case with SARS
- **Healthcare**: Public overstretched; expats universally on private (Discovery Health, Bonitas) + medical aid; **quality high but ZAR volatility risk**
- **Climate**: Cape Town/Garden Route Mediterranean 12-18°C winter; **Day Zero water-scarcity overlay** (2018 near-miss recurring)
- **Expat density**: UK/DE/NL retirees; Cape Town suburbs, Plettenberg Bay, Knysna
- **Visa**: **Retired Person Visa** — ZAR 37,000/mo pension/income (~USD 2k/mo) — verify 2026 threshold at DHA

### 🇬🇪 GE
- **Pension tax**: Territorial — foreign-source income not taxed; 1% small-business / favourable individual rates
- **Healthcare**: Universal Healthcare Program (state) for citizens/residents; private (Mediclub, Medi) Tbilisi growing; expats often medivac for serious conditions
- **Climate**: Continental — Tbilisi 2-7°C winter, 25-30°C summer; Batumi humid subtropical Black Sea
- **Expat density**: Major RU+UA surge post-2022; growing US/EU crypto-retiree subsegment; Tbilisi, Batumi
- **Visa**: **Visa-free 1-year for ~95 nationalities**; no retirement-specific scheme needed

### 🇮🇩 ID
- **Pension tax**: Worldwide for residents (>183 days); foreign pension taxable at progressive PIT; some treaty relief
- **Healthcare**: BPJS Kesehatan universal for residents incl. KITAS/KITAP holders; quality variable; Bali expats use private (BIMC, Siloam); **medivac to SG common**
- **Climate**: Tropical 26-30°C; Bali wet/dry seasons; volcanic risk (Agung, Merapi)
- **Expat density**: Bali — Ubud, Canggu, Sanur — large AU/EU/US community
- **Visa**: **Retirement KITAP** — age 55+, USD 1.5k/mo pension proof, health insurance, must hire local staff

### 🇲🇾 MY
- **Pension tax**: Foreign-source income exempt under territorial principle (post-2022 amendments narrowed for residents — verify with IRB)
- **Healthcare**: Strong universal public + private (Sunway, Pantai, Gleneagles); Penang/KL hospitals JCI-accredited; **medical-tourism destination**
- **Climate**: Tropical 25-32°C year-round; humid; minimal seasonal variation
- **Expat density**: UK/AU/SG/JP retirees via MM2H legacy + new tiers; Penang, KL, Johor Bahru
- **Visa**: **MM2H 3-tier (Silver/Gold/Platinum, post-2024 reform)** — RM 500k–RM 5M deposit; verify with MoTAC — see `visa-programs.md`

### 🇻🇳 VN
- **Pension tax**: Worldwide for residents (>183 days); foreign pension at progressive PIT (2026: up to 35%)
- **Healthcare**: Universal Health Insurance for residents; expats use private (Vinmec, FV Hospital); evac to TH/SG for complex cases
- **Climate**: Da Nang/Hoi An 22-32°C; **typhoon season Sep-Nov on central coast**; Saigon 25-32°C
- **Expat density**: Growing US/EU/AU; Da Nang, Hoi An, Saigon expat enclaves; **visa pathway thinner than TH/PH/MY**
- **Visa**: LD Labour visa or family-route only; **no formal retirement visa** — see `visa-programs.md`

### 🇵🇭 PH
- **Pension tax**: Foreign pension NOT taxed by PH for SRRV holders; territorial-style for non-resident-source income
- **Healthcare**: PhilHealth universal for residents; private (St. Luke's, Makati Med) strong in Metro Manila; provincial quality patchy
- **Climate**: Tropical 25-32°C; **typhoon season Jun-Nov** (Davao less typhoon-exposed); Cebu/Bohol mid-exposure
- **Expat density**: US/AU/JP/KR retirees; Cebu, Dumaguete, Bohol, Davao
- **Visa**: **SRRV (most generous SE-Asia)** — USD 10k–50k deposit depending on age/pension status; 4 sub-classes — see `visa-programs.md`

### 🇮🇱 IL
- **Pension tax**: New immigrants (Olim) get **10-year tax holiday** on foreign-source income+capital gains (Amendment 168, 2008); thereafter worldwide PIT
- **Healthcare**: Universal via 4 Sick Funds (Kupot Holim — Clalit, Maccabi, Meuhedet, Leumit); **Olim entitled from arrival**; English support varies
- **Climate**: 10-18°C winter, 28-35°C dry summer; Tel Aviv coastal humid
- **Expat density**: Large US/FR/UK/RU Olim retiree community; Tel Aviv, Netanya, Ra'anana, Jerusalem
- **Visa**: **Aliyah (Law of Return)** — direct citizenship for Jewish ancestry; purchase-tax incentives for Olim — see `visa-programs.md`

### 🇲🇦 MA
- **Pension tax**: Foreign pensions: **80% abatement if transferred permanently to MA in DH** (Art. 76 CGI); effective rate dramatically reduced
- **Healthcare**: AMO universal scheme being expanded (2024-2026 reform); expats use private (Cliniques Akdital, Cheikh Zaid); **French-system standards**
- **Climate**: Marrakech 18-22°C winter (35-40°C summer); Essaouira/Tangier Atlantic-cooled milder
- **Expat density**: FR retirees dominant; UK/DE growing; Marrakech, Essaouira, Tangier, Agadir
- **Visa**: **Carte de Séjour (long-stay)** — standard residence permit; no retirement-specific program

### 🇪🇬 EG
- **Pension tax**: Foreign-source pension generally not taxed by EG (territorial application varies — verify with ETA)
- **Healthcare**: New Universal Health Insurance (2018 law, phased rollout); expats use private (Cleopatra, As-Salam International); **medivac for serious cases recommended**
- **Climate**: Hurghada/Sahel/Sharm 18-35°C; very dry; summer extreme
- **Expat density**: RU/UA/DE/UK retirees; Hurghada, El Gouna, Sahel; **EGP currency volatility risk material** (post-2024 devaluations)
- **Visa**: **Investment Law 160/2023 PR** — USD 250k cash → permanent residency; verify currency-control / Form 4 repatriation risks before committing

## Anti-hallucination

- **Pension tax regimes change** — IT 7%, GR 7%, PT NHR all reformed in 2023-2024 cycle; **TH 2024 remittance reform** materially changes LTR economics; **CL 2023 Isapres ruling** reshaping retiree healthcare premiums; **MY MM2H** retiered multiple times since 2021. Always verify with home + host-country tax adviser.
- **Healthcare reciprocity rules change post-Brexit, post-2024 EU directives** — verify S1 eligibility before committing
- **Climate ranking is current-decade snapshot** — climate trajectory (`--climate`) is the forward-looking view; **water-scarcity overlays (CY, ZA, CL, MA)** worth checking against latest drought/aquifer data
- **Cost-of-living tier is broad-stroke** — actual costs vary 2-3× between provincial and capital within most countries; AE/IL/JP costs concentrate sharply in prime city centres
- **Currency-volatility risk** — TR, EG, AR, ZA, ID retirees should consider FX exposure on pension stream vs local-cost; cross-link `--currency` for hedging strategies
- **Visa thresholds drift** — every program above (LTR, MM2H, SRRV, Retirement Visa, Pensionado, Olim incentives) has been re-priced or restructured at least once 2021-2026; treat all numeric thresholds as *as-of date-stamp* and verify at issuing authority before applying

## Status

Last refreshed: 2026-05-01 (Tier-1 + Tier-2 expansion to 18 new countries).
**Confidence**: MEDIUM — high-level regimes and visa names are sourced from current law where named (e.g., IL Amendment 168, MA Art. 76 CGI, Ley 19.937 UY, FDL 47/2022 AE, DL 824 CL); specific thresholds (e.g., AED 1M, ZAR 37,000/mo, COP 3× SMLMV, USD 80k/yr LTR) should be re-verified at issuing authority before user action since visa thresholds drift on 12-24 month cadence.
