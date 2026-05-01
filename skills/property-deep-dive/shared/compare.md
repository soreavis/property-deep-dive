# Universal `--compare` Mode

Side-by-side multi-country comparison for relocation, investment, and "where should I move/buy?" decisions. Leverages all 62 country playbooks at once.

**Snapshot**: April 2026.

## When to use

Trigger `--compare` when the user is **not committing to a single address** but instead asking:
- "Where should I move from FR?" — compare candidate countries
- "Spain or Portugal for golden-visa replacement?" — compare 2-5 countries head-to-head
- "Cheapest entry market in EU for €200k?" — compare on a metric
- "Where can I retire on €2,500/mo?" — compare with `--retirement` overlay

## Invocation

```
/property-deep-dive --compare=es,pt,it [--criteria=<list>] [--journey=<type>] [--budget=<amount>]
/property-deep-dive --compare=eu --top=10 --criteria=tax,price,visa
/property-deep-dive --compare --rank=tax-friendly --rank=climate-stable
```

## Universal contract

For each country in the comparison set, return:
1. **One row per country** with the requested criteria
2. **Highlighted leaders/laggards** per criterion (best 🟢 / worst 🔴)
3. **Overall verdict per user-stated objective**
4. **Ranked shortlist** (top 3 by composite score)
5. **Anti-hallucination disclaimer**: comparison is structural, not predictive

## Output template

```markdown
## Multi-Country Comparison

**Comparison set**: <ISO2 list>
**Criteria**: <list>
**Date**: <YYYY-MM-DD>

### Headline metrics

| Metric | <C1> | <C2> | <C3> | … |
|---|---|---|---|---|
| Capital city €/m² (segment-typical) | … | … | … | … |
| Annual property tax (% / formula) | … | … | … | … |
| Transfer tax / acquisition cost | … | … | … | … |
| CGT regime | … | … | … | … |
| Foreign-buyer access | … | … | … | … |
| Mortgage LTV (non-resident) | … | … | … | … |
| Currency / FX volatility | … | … | … | … |
| Visa pathway (RBI/CBI status) | … | … | … | … |
| Climate trajectory (RCP4.5 to 2050) | … | … | … | … |
| Notary / closing-cost % | … | … | … | … |
| Time offer→deed (days) | … | … | … | … |

### Per-criterion leader

| Criterion | Best | Worst |
|---|---|---|
| Lowest acquisition cost | <C> | <C> |
| Lowest annual carry | <C> | <C> |
| Strongest CGT exemption | <C> | <C> |
| Most foreign-buyer-friendly | <C> | <C> |
| Most stable currency | <C> | <C> |
| Most accessible visa | <C> | <C> |
| Best climate (cooler / less drought / less wildfire) | <C> | <C> |
| Fastest closing | <C> | <C> |

### Composite ranking

🥇 1. <C> — <one-line rationale>
🥈 2. <C> — <one-line rationale>
🥉 3. <C> — <one-line rationale>

### Decision-context overlay

<if --journey=retiree, --journey=foreign-buyer, --journey=investor — apply that filter>

### Confidence
<HIGH | MEDIUM | LOW> — <one-sentence justification>
```

## Available criteria flags

| Flag | What it pulls |
|---|---|
| `--criteria=tax` | Annual + transfer + CGT + rental income tax + VAT |
| `--criteria=price` | Capital + secondary city €/m², HPI YoY |
| `--criteria=visa` | RBI/CBI status, property thresholds, language requirement |
| `--criteria=finance` | LTV non-resident, 10-yr fixed rate, FX-loan rules |
| `--criteria=climate` | Temperature trajectory, sea-level rise, drought, wildfire risk |
| `--criteria=foreign-buyer` | Restrictions, permits, surcharges, RU/BY rules |
| `--criteria=str` | Short-term rental regime, registration, taxes |
| `--criteria=closing` | Notary requirement, closing cost %, days offer→deed |
| `--criteria=insurance` | Cat-risk scheme, mortgage-mandatory, premium % |
| `--criteria=process` | Cadastre access, foreigner-self-serve, language requirement |
| `--criteria=all` | All of the above |

## Comparison set shortcuts

| Shortcut | Resolves to |
|---|---|
| `eu` | All 27 EU members in skill |
| `eea` | EU + IS, NO, LI (when populated) |
| `eurozone` | All 21 eurozone members |
| `western-balkans` | RS, ME, BA, MK, AL |
| `latam` | MX, BR, AR, CR, PA, DO, CO, UY, CL |
| `anglo-non-eu` | CA, AU, NZ, US |
| `mediterranean` | ES, PT, IT, GR, CY, MT, FR, HR, SI, MA, IL, EG, TR |
| `nordic` | SE, FI, NO, DK, IS |
| `dach` | DE, AT, CH |
| `gcc-mena` | AE, IL, MA, EG, TR |
| `southeast-asia` | TH, ID, MY, VN, PH, JP |
| `caucasus-eu-adjacent` | GE, TR |
| `top-10-foreign-buyer-friendly` | precomputed list (see below) |

## Precomputed verdict shortcuts (Apr 2026 snapshot)

These are computed from the per-country playbooks and refreshed on `--update`. They are commentary, not authoritative — use as a starting point.

### Most foreign-buyer-friendly (no AIP/permit beyond standard)
1. PT (open, NIF only)
2. ES (open, NIE only)
3. LU (no nationality restriction, same 7%)
4. IT (Codice Fiscale only)
5. FR (no permit, simple notarial)
6. GE (open, registration <1 day, no permit)
7. US (open, ITIN/SSN only; FIRPTA on resale)
8. TR (open subject to reciprocity + military-zone clearance)

### Highest acquisition friction (permit / restriction-heavy)
1. CA (foreign-buyer ban through 1 Jan 2027)
2. AU (established-homes ban 1 Apr 2025–31 Mar 2027)
3. NZ (most existing homes banned since 2018)
4. TH (no land freehold for foreigners; condo 49% quota)
5. PH (no land for foreigners; condo 40% quota)
6. VN (no land; 50-yr leasehold + 30%-per-building / 250-houses-per-ward quotas — 2024 Land Law)
7. ID (no Hak Milik freehold for foreigners; Hak Pakai leasehold only)
8. CH (Lex Koller cantonal permit)
9. DK (non-EU + 5y residence requirement)
10. AE (foreign ownership restricted to designated freehold zones)
11. EG (max 2 properties × 4,000 m² total; Sinai/Suez excluded)

### Lowest acquisition cost (% of price)
1. GE (~0.1-0.5% — lowest tracked globally; Public Service Hall registration GEL 50-200)
2. EE (~1-2% no transfer tax)
3. LT (~1-1.5% no transfer tax)
4. CZ (~2-4% transfer tax abolished 2020)
5. SK (~2-4% no transfer tax since 2005)
6. NO (~3-4% dokumentavgift 2.5%)
7. CL (~3-4% notarial + Conservador de Bienes Raíces)
8. VN (~3-5% registration + notary)
9. US (~3-6% varies by state — CA escrow vs NY mansion-tax extremes)

### Highest acquisition cost (% of price)
1. ID (~17-19% combined BPHTB 5% + PPh 2.5% + PPN 11% on new-build via PMA)
2. BE (~12-17% Brussels/Wallonia)
3. ES (~10-13% existing)
4. PH (~10% — CGT 6% gross + DST 1.5% + transfer + LTT)
5. IL (~6-10% Mas Rechisha tiered + non-resident surcharge)
6. AT (~10-12%)
7. GR (~10-12%)
8. UK (~10-15% with SDLT non-res surcharge)
9. UY (~7-9%)
10. ZA (~7-9% transfer duty tiered)
11. DO (~7-8% — 3% transfer + 1% IPI + notary + registry)
12. AE (~6-8% — DLD 4% + agent + NOC + housing-fee 5% annual)
13. TR (~6-8% — 4% tapu + notary + agent)
14. JP (~6-7% — registration + acquisition tax + agent up to 3% + 6万円)

### Lowest annual carry (no/minimal annual property tax)
1. MT (no annual property tax)
2. AE (no annual property tax; only 5% housing fee on rentals via DEWA)
3. VN (no recurring residential property tax — non-agri land-use fee only)
4. CY (national IPT abolished 2017; municipal small)
5. LU (impôt foncier near-trivial currently — reform 2030)
6. GE (income-gated annual tax — 1% only above GEL 40k household income threshold)
7. IE (LPT modest, 0.0906% base rate)
8. LT (NTM exemption ≤€150k for residents)
9. DO (1% IPI only on portion above DOP 9.86M, ~USD 165k)

### Highest annual carry
1. FR (taxe foncière + redevance audiovisuelle, dependent on commune)
2. UK (council tax bands)
3. US (state-by-state; 0.5-2.5%, NJ/NH/IL on the heavy end, HI/AL on the light)
4. JP (1.4% kotei-shisan-zei + 0.3% toshi-keikaku-zei on assessed value)
5. ZA (Municipal Rates 0.6-1% — Cape Town/Joburg)
6. CH (cantonal Eigenmietwert until 2028 + cantonal property tax)
7. DK (boligskat 2024-reform unified ejendomsværdiskat + grundskyld)
8. UY (Contribución Inmobiliaria 0.25-1.4% + ITP 2% on transactions)
9. CL (Contribuciones ~0.98% above UF 49.5M exemption)

### Most stable currency / lowest FX risk for €-buyers
1. **Eurozone** (21 countries — no FX risk)
2. BG (just joined 1 Jan 2026)
3. HR (joined 2023)
4. DK (DKK ERM-II ±2.25%)
5. BA (currency board 1.95583)

### Highest FX risk for €-buyers
1. AR (managed band 1,000–1,400 ARS/USD; capital controls history)
2. EG (EGP devaluation cycles; March 2024 float halved value vs USD; Form 4 repatriation gate)
3. TR (TRY chronic high inflation; 2021-2025 cumulative loss vs EUR >70%)
4. UY (USD-parallel pricing for property — UYU not used at scale; FX exposure is USD/EUR)
5. ZA (ZAR EM-volatility; load-shedding-correlated swings)
6. CL (UF-indexed property contracts mute FX risk *internally* but UF→EUR conversion still volatile)
7. HU (HUF most volatile EU currency)
8. IS (small market, 10%+ annual range typical)
9. UK (GBP political-uncertainty premium)
10. CH (CHF safe-haven appreciation 2024-26 — actually a *gain* for buyers but unhedged exit risk)
11. AE (AED pegged to USD 3.6725 — stable vs USD, but EUR-buyers carry USD/EUR risk)

### Most golden-visa-friendly (Apr 2026, post-ES/IE/MT closures)
1. GR (€800k/€400k tiers, property-linked)
2. AE Golden Visa (AED 2M / ~USD 545k property — 10-year, renewable)
3. TR CBI (USD 400k property — citizenship, retain 3y)
4. GE Investor Residency (USD 300k property — 5-yr, path to permanent)
5. DO Investor Residency (USD 200k property; CONFOTUR zones can shave taxes)
6. PH SRRV (USD 10-50k deposit depending on age — retiree visa, not strictly RBI)
7. TH LTR — 4 categories (no fixed property threshold; passive-income or wealth route)
8. MY MM2H (post-2024 reform: tiers MYR 1M / 2M / 5M deposit + property req)
9. CY (€300k PR — distinct from ended CBI)
10. MT MPRP (€375k lease/€750k purchase + fees)
11. PA (Friendly Nations $200k / Qualified Investor $300k)
12. LV (€250k Riga radius, built only)
13. ID 2nd Home Visa (IDR 2B funds, 5-10 yr; not strictly property-tied)
14. EG (Investment Law 160/2023 — residency tied to property purchase, USD threshold updated 2023)
15. CO Migratorio M (350× SMLMV ~USD 100k+ property route)
16. UY (no formal RBI; tax-residency 11-yr exemption is the actual draw)
17. CL (no formal RBI; investor-visa via Sociedad)

### Cleanest 2026 tax reforms (helpful for buyers)
1. CY (Comprehensive Tax Reform 1 Jan 2026 — CGT exemptions raised, SDC abolished)
2. LU (Bëllegen Akt €40k credit per person made permanent)
3. MT (UCA / vacant 0% on first €750k Jan 2025–Dec 2026)
4. PT (IFICI replaced NHR — narrower but operational)
5. LT (NTM 2026 progressive on non-main with main-dwelling threshold ≥€450k)

### Steepest 2026 tax reforms (less helpful for buyers)
1. RO (VAT 19→21% Aug 2025; local property tax baseline +167% Jan 2026)
2. NL (Box 3 forfait 6% 2026)
3. UK (SDLT thresholds reverted 1 Apr 2025)
4. SI (davek na nepremičnine 1.45% pending 2026)
5. CH (Eigenmietwert abolition 2028 — net depending on profile)

## Cross-cutting red-flag flags

When comparing, surface country-level structural flags:
- 🚩 BA: dual-entity (FBiH/RS-entity) — buyer must understand
- 🚩 CY: TRNC north title risk
- 🚩 LV: compulsory land lease (`dalītais īpašums`) Riga gotcha
- 🚩 MX: fideicomiso restricted zone (50km coast/100km border)
- 🚩 RO: AMCCRS pre-1977 Bucharest Rs I class — insurance/mortgage refusal
- 🚩 PA: 10km border restriction (constitutional)
- 🚩 GR: Golden Visa thresholds vary by zone; "where" matters more than "how much"
- 🚩 BG: non-EU cannot own ANY land directly
- 🚩 RO: non-EU cannot own land (buildings only)
- 🚩 IT: non-resident purchase tax 9% vs resident 2% (cadastral)
- 🚩 TH: condo 49% foreign-quota cap per building — title verification at Land Office mandatory
- 🚩 PH: condo 40% foreign-quota cap per project — Master Deed must show available foreign allocation
- 🚩 VN: 50-yr leasehold + 30%-units-per-building / 250-houses-per-ward foreign quotas (2024 Land Law)
- 🚩 ID: Hak Milik freehold not available to foreigners — Hak Pakai or PMA structures only; nominee arrangements legally void
- 🚩 MY: state-level minimum thresholds for foreigners (MYR 1M-3M depending on state) + 4% MOT surcharge
- 🚩 IL: ~93% land is state-owned (RMI / Israel Land Authority) — most "purchases" are 49/98-yr capitalised leaseholds, not freehold
- 🚩 IL: war-zone insurance via Karnit (state-backed compensation fund) — privates not always reachable for missile-impact zones
- 🚩 TR: military-restricted-zone clearance required — title transfer can be blocked even after deposit
- 🚩 TR: reciprocity list — buyer's nationality determines eligibility (some nationalities barred)
- 🚩 AE: foreign ownership only in designated freehold zones (Dubai/Abu Dhabi-specific lists); leaseholds elsewhere
- 🚩 AE: no annual property tax but 5% Dubai housing fee on rental value via DEWA bills
- 🚩 EG: Sinai + Suez Canal zones excluded for foreigners; max 2 properties × 4,000 m² total nationally
- 🚩 EG: Form 4 (or successor regulation) — currency-repatriation evidence at time of sale, retain bank import certificate
- 🚩 MA: only `titré` (registered) properties safely transferable to foreigners; `melkia`/`habous` titles risk-prone; agricultural land barred without permit
- 🚩 ZA: 50% LTV typical cap for non-resident mortgage; SARB approval may be required for capital introduction
- 🚩 GE: ultra-fast registration (<1 day Public Service Hall) — but title-search depth shallow vs EU; commission independent lawyer pre-signing
- 🚩 JP: foreign mortgage extremely limited (Shinsei/SBI only; large down-payment); cash-buy is the norm
- 🚩 JP: shakkan / akiya (vacant-house) stock can carry undisclosed cleanup/demolition liabilities — pre-1981 builds also fail current seismic code
- 🚩 DO: CONFOTUR (tourism-zone) properties can waive transfer + IPI taxes for 15 yr — verify project's CONFOTUR registration before closing
- 🚩 CO: predial varies by municipio + estrato (socio-economic strata 1-6); dual cadastre (catastro multipropósito) rollout mid-2026
- 🚩 UY: property contracts often denominated in USD, not UYU — confirm currency clause and parallel-rate mechanism
- 🚩 CL: PE/BO/AR border 10-km restriction (Decree 1939/1977 + DL 1.939); foreigners need presidential authorisation
- 🚩 US: FIRPTA — non-resident sellers face 15% withholding on gross sale price (not gain) at closing; refund via 1040-NR
- 🚩 US: state-by-state divergence is the dominant variable — TX no income tax + 2.5% property tax vs CA 1% Prop-13 cap + 13.3% income tax

## Anti-hallucination

- **Only compare countries already in the skill** (`countries/<iso2>/playbook.md` exists). Refuse to compare unsupported countries.
- **Use the playbook values as authoritative** — do not retrieve fresh data per-country during a `--compare` run; trust the latest playbook refresh
- **Date-stamp every cell** — comparison output must show "as of <playbook last-update>" per row
- **Surface playbook confidence** — if any country has LOW confidence, flag it in the row

## Worked-example comparisons (new-country trios)

These illustrate how the matrix is used. Numbers are from individual playbooks at last refresh; check each playbook's `**Last verified**:` stamp before quoting.

### Example A — JP vs TH vs PH for retirement (Pacific-rim retiree)

| Metric | JP | TH | PH |
|---|---|---|---|
| Foreign access to land | Yes (freehold) | NO (condo 49% quota only) | NO (condo 40% quota only) |
| Total acquisition cost | ~6-7% | ~6-8% | ~10% |
| Annual carry | 1.4% + 0.3% on assessed | 0.01-0.7% L+B | RPT munisipal — modest |
| Retiree visa | None RBI; "Investor" requires active business | LTR (4 cat — passive-income route) | SRRV (USD 10-50k deposit by age) |
| English usability | LOW outside Tokyo/Osaka | MEDIUM (tourist zones) | HIGH (lingua-franca) |
| Currency stability | JPY weak vs USD/EUR 2024-26 — buyer tailwind | THB managed | PHP EM-volatile |
| Climate trajectory | Rising heat + typhoon north-shift | Rising heat + flood (BKK) | Typhoon-belt + sea-rise |

🥇 **PH** for English-fluent retiree on USD income who accepts condo-only ownership and tropical-storm risk
🥈 **TH** for retiree who wants LTR-tier tax structure and is comfortable with leasehold-house workaround (30-yr renewable)
🥉 **JP** for retiree wanting freehold ownership + rule-of-law, with capital base willing to absorb low rental yield + ageing-society demographic headwind

**Confidence**: MEDIUM — visa thresholds + tax rates verified per individual playbooks Q2 2026; long-term retirement viability is a 20-year bet that no playbook can fully de-risk.

### Example B — AE vs IL vs CY for tax-residence pivot

| Metric | AE | IL | CY |
|---|---|---|---|
| Personal income tax | 0% (corporate 9% above AED 375k) | Progressive to 47% + 3% surtax | Progressive to 35%; SDC abolished 1 Jan 2026 |
| CGT on resale | 0% | 25-50% Mas Shevach (NR uplift) | Exempt above raised thresholds (2026 reform) |
| Property tax annual | None (5% housing fee on rental only) | Arnona muni | Municipal small (national IPT abolished 2017) |
| Foreign ownership | Designated freehold zones only | de-facto leasehold (RMI 93% state land) | Full freehold |
| Visa pathway | Golden Visa AED 2M property, 10y | Aliyah (Jewish-only) — closed pathway for non-Jews | PR €300k property |
| Geopolitical risk | Regional but low-impact internally | High (war + missile risk) | Cyprus problem: TRNC north title trap |

🥇 **CY** for clean tax-residence pivot with EU-passport upside (after long stay) + post-2026 reform clarity
🥈 **AE** for fast-track 10-yr Golden Visa + zero income tax — at cost of EU access and lower liquidity in resale
🥉 **IL** only for Jewish applicants (Aliyah-eligible) willing to accept war-zone insurance via Karnit + leasehold dominant tenure

**Confidence**: MEDIUM — CY 2026 tax-reform details still being clarified by Inland Revenue; AE Golden Visa thresholds stable since 2022; IL war-risk is dynamic.

### Example C — CO vs MX vs PA for LATAM digital-nomad/investor

| Metric | CO | MX | PA |
|---|---|---|---|
| Foreign-buyer access | Open | Fideicomiso required in 50km coast / 100km border | Open except 10km border (constitutional) |
| Total acquisition cost | ~5-6% | ~6-8% (incl. fideicomiso setup) | ~5-6% |
| Annual carry | Predial municipio + estrato | Predial municipio | IBI escalating brackets |
| CGT | 15% ganancia ocasional | 25-35% on gain (or 25% gross option) | 3% + 10% capital gains structure |
| Digital-nomad/RBI route | Migratorio M (350× SMLMV) | RNE / Temporary Resident | Friendly Nations USD 200k / Qualified Investor USD 300k |
| Climate | Andean mild | Coastal hurricane belt (Pacific + Caribbean) | Caribbean+Pacific dual-coast hurricane fringe |
| FX risk | COP EM-volatile | MXN EM-volatile | USD-denominated economy (no FX risk for USD buyers) |

🥇 **PA** for USD-base investor wanting simplest visa + zero FX risk + Friendly Nations or Qualified Investor pathway
🥈 **CO** for cheaper entry, moderate climate, but 2026 catastro-multipropósito rollout creates assessed-value uncertainty
🥉 **MX** for buyer accepting fideicomiso friction in exchange for deeper market and proximity to US

**Confidence**: MEDIUM — PA Qualified Investor program threshold verified Q1 2026; CO catastro reform cadence per municipio is uneven.

### Example D — GE vs PT vs CY for EU-adjacent low-tax base

| Metric | GE | PT | CY |
|---|---|---|---|
| EU member? | NO (EU-adjacent / candidate) | YES | YES |
| Foreign-buyer access | Open, fastest registration globally (<1 day) | Open (NIF only) | Open |
| Acquisition cost | ~0.1-0.5% | ~7-8% (IMT + stamp + notary) | ~8-10% |
| Annual property tax | Income-gated (only above GEL 40k household income) | IMI 0.3-0.45% | Municipal small |
| CGT | None after 2-yr hold | 28% non-residents (50% inclusion residents) | Exempt above raised 2026 thresholds |
| Tax residency draw | Territorial — 1% small-business / 20% personal | IFICI replaced NHR (narrower) 2024+ | 60-day rule + non-dom 17 years |
| Visa | Investor USD 300k property | D7/D8 (income-based, not property) | PR €300k property |
| Risk | Russia border + currency exposure (GEL) | EU stability | TRNC title trap; banking-sector overhang |

🥇 **CY** for EU-passport-track tax-residence with strongest 2026 reform tailwind
🥈 **PT** for EU base prioritising rule-of-law over tax minimisation (post-NHR closure)
🥉 **GE** for ultra-fast non-EU base with lowest acquisition friction and territorial-tax structure — at cost of EU access and proximity to active conflict zone

**Confidence**: MEDIUM — GE political stability and visa-program continuity carry higher-than-EU uncertainty; PT IFICI implementation still settling; CY 2026 reform clarifications ongoing.

## Limitations

- **Not predictive**: comparison is current-state, not 5-year-forward
- **Not personalized**: doesn't know user's age, citizenship, financial profile — those go via `--journey=<type>` overlay
- **Doesn't replace local advice**: every shortlist needs a local notary/lawyer/tax adviser before committing

## Status

Last refreshed: 2026-04-26.
