# Australia 🇦🇺 — Property Due-Diligence Playbook

ISO2: `au`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`2000` Sydney CBD, `3000` Melbourne CBD, `4000` Brisbane, `6000` Perth)
- **Admin levels**: 6 states + 2 territories + 537 LGAs (Local Government Areas)
- **Currency**: **AUD** (Australian dollar); 1 EUR = 1.5830 AUD (ECB euro reference rate, 28 Oct 2026; ECB range over the 12 months to that date 1.583–1.788)
- **Finance**: RBA cash rate target **4.60%** (+0.25 pp effective 30 Sep 2026; 3.60% in Dec 2025); APRA mortgage serviceability buffer **3 percentage points**; APRA debt-to-income limit since 1 Feb 2026 — banks may write at most 20% of new mortgage lending at debt of six times income or more (2026 data, source [RBA cash rate](https://www.rba.gov.au/statistics/cash-rate/) + [APRA DTI limit, 27 Nov 2025](https://www.apra.gov.au/news-and-publications/apra-limit-high-debt-income-home-loans-constrain-riskier-lending) + [APRA Corporate Plan 2026-27](https://www.apra.gov.au/apra-corporate-plan-2026-27/our-strategic-objectives); 2026-10-28 verified)
- **Languages**: English (de facto)
- **Cadastre**: **Torrens system** — state-administered (no national portal)
  - **NSW**: NSW Land Registry Services `https://www.nswlrs.com.au` (Vol/Folio)
  - **VIC**: Landata `https://www.landata.vic.gov.au`
  - **QLD**: Titles Queensland `https://www.titlesqld.com.au`
  - **WA**: Landgate `https://www.landgate.wa.gov.au`
  - **SA**: SAILIS `https://sailis.lssa.com.au`
  - **TAS**: LIST `https://www.thelist.tas.gov.au`
- **Identifier**: Title reference (Vol/Folio); paid lookup ~$15-30/title
- **Ownership types**: freehold (Torrens), strata (apt), community title, **old-system title** (pre-Torrens, tiny pockets NSW)
- **Foreign-buyer ban**: established dwellings **1 Apr 2025 – 30 Jun 2029** (FIRB — extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset; 2026-07-03 verified, source ATO / foreigninvestment.gov.au)

## Section: `--price`

### Primary sources

- **Cotality (formerly CoreLogic) Home Value Index**: `https://www.cotality.com/au/our-data/indices` (the old corelogic.com.au URL redirects here) — daily index for the major capitals and the combined capitals (Canberra, Hobart, Darwin in the monthly series only); monthly HVI report, e.g. the Oct 2026 edition with data to 30 Sep released 1 Oct 2026; hedonic, revised for 12 months — secondary aggregator
- **ABS Total Value of Dwellings** (quarterly; cat. 6432.0 per its table files): `https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/total-value-dwellings/latest-release` — mean dwelling price by state and median transfer prices by capital city and rest of state; successor to the **Residential Property Price Indexes: Eight Capital Cities** (cat. 6416.0), which ceased with the Dec qtr 2021 issue; latest Jun qtr 2026 (released 8 Sep 2026), next Sep qtr 2026 on 1 Dec 2026
- **Domain House Price Report**: quarterly (`https://www.domain.com.au/research/house-price-report/`; the site blocks scripted access, contents not read on 2026-10-28; no monthly Domain price series confirmed) — listing-platform data, secondary
- **REIA Real Estate Market Facts (REMF)**: `https://www.reia.com.au/research/remf` — quarterly report on residential markets across major cities; Sep qtr 2026 edition due 16 Dec 2026; underlying data sold separately
- **Cotality Property Reports** (formerly CoreLogic) — paid, per property or suburb: `https://www.cotality.com/au/products/property-report`
- **NSW Rent and Sales Report** (NSW Department of Communities and Justice): `https://dcj.nsw.gov.au/about-us/families-and-communities-statistics/housing-rent-and-sales/rent-and-sales-report.html` — sales tables (latest Mar qtr 2026) and new-bond rent tables (latest Jun qtr 2026) (primary, NSW only)

### Listing platforms

- **realestate.com.au** — DOMINANT (REA Group): reached 11.8 million Australians in Aug 2026, 4.4 million more than its nearest competitor, #1 portal in every state and territory (REA Group release of 14 Oct 2026 citing Ipsos iris — the platform's own claim; Ipsos iris trend break from Jul 2026): `https://www.realestate.com.au`
- **Domain.com.au** — #2; owned by **CoStar Group** since 27 Aug 2025 (no longer Nine Entertainment), 'an average of 7 million Australians each month' per CoStar's completion release (Aug 2025, platform owner's claim — figures may have changed since): `https://www.domain.com.au`
- Coverage near-universal across both

### Price benchmarks — ABS (Jun qtr 2026) and Cotality (30 Sep 2026)

| Capital (Greater Capital City) | ABS established house median, Jun qtr 2026 | ABS attached dwelling median, Jun qtr 2026 | Cotality house median value, 30 Sep 2026 | Cotality unit median value, 30 Sep 2026 | Cotality annual change, dwellings |
|---|---:|---:|---:|---:|---:|
| **Sydney** | $1,487,600 | $840,000 | $1,466,060 | $867,597 | -7.0% |
| **Melbourne** | $850,000 | $590,000 | $915,119 | $624,740 | -6.2% |
| **Brisbane** | $1,155,000 | $830,100 | $1,146,078 | $834,627 | +5.9% |
| **Adelaide** | $975,000 | $725,000 | $990,531 | $674,188 | +6.5% |
| **Perth** | $1,010,000 | $730,000 | $1,017,734 | $714,265 | +10.1% |
| **Hobart** | $750,000 | $600,000 | $790,406 | $591,795 | +7.0% |
| **Darwin** | $752,500 | $445,500 | $747,252 | $480,748 | +11.9% |
| **Canberra** | $1,030,000 | $615,000 | $1,006,269 | $582,245 | -1.6% |
| **Combined regional** | — | — | $775,024 | $669,770 | +5.6% |
| **National** | — | — | $979,193 | $727,818 | 0.0% |

(ABS columns: [Total Value of Dwellings, Jun qtr 2026, Table 2](https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/total-value-dwellings/jun-quarter-2026/643202.xlsx) — unstratified medians of established house and attached dwelling transfers by Greater Capital City, released 8 Sep 2026; current-quarter figures are preliminary and revised in later releases; ABS publishes rest-of-state medians per state but no combined regional figure. Cotality columns: [Home Value Index, Oct 2026](https://discover.cotality.com/hubfs/Article-Reports/COTALITY%20HVI%20OCT%202026%20FINAL.pdf) — hedonic modelled median values as at 30 Sep 2026, secondary aggregator, revised for 12 months. Sources disagree because they differ in date (Jun qtr vs 30 Sep), method (median of recorded transfers vs hedonic model) and dwelling split (ABS 'attached dwellings' vs Cotality 'units'); neither values a specific property.)

- **Direction (Cotality, secondary)**: national values -1.1% in Sep 2026, the sixth straight monthly fall, 5.2% below the Mar 2026 peak; Sydney 8.6% below its Feb 2026 peak; Jul–Sep quarter Sydney -4.9%, Melbourne -3.4%, Brisbane and Perth -4.7%; combined regionals +5.6% over the year vs combined capitals -1.8% (Cotality HVI, 1 Oct 2026)
- **ABS annual change, established houses, Jun qtr 2026 vs Jun qtr 2025** (computed from the ABS medians, Jun qtr 2026 preliminary): Sydney -2.1%, Melbourne +1.2%, Brisbane +18.8%, Adelaide +13.2%, Perth +18.8%, Hobart +4.9%, Darwin +21.4%, Canberra +3.0% — these end in June, before the Jul–Sep falls above
- **ABS mean dwelling price, Jun qtr 2026** (all dwellings, by state): NSW $1,304,900 · VIC $918,400 · QLD $1,130,600 · SA $979,600 · WA $1,123,700 · TAS $733,200 · NT $614,400 · ACT $981,700 · Australia $1,100,400 (2026 data, source [ABS Total Value of Dwellings](https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/total-value-dwellings/latest-release), released 8 Sep 2026; next release 1 Dec 2026)

### Compute

1. AUD/sqm = price / **internal area sqm** (or per sq ft in some markets)
2. Cross-check **Cotality** modelled values against the ABS capital-city transfer medians above and the Domain House Price Report
3. **Strata levies** for units add est. ~$3-15k/yr (est., no primary source; levies are set per scheme — read the admin fund + sinking / capital works fund budgets in the strata report)
4. Foreign purchaser surcharge on top of state stamp duty: rate set per state (see the `--tax` foreign owner surcharges table; it is not a flat ~8%)

### Key terms

- Torrens title = freehold, registered
- Strata = apt complex with body corporate
- Community title = master-planned estate
- BMC = Building Management Committee (mixed-use)
- Off-the-plan = pre-construction purchase

---

## Section: `--traffic`

### Sources

- **State DOT traffic counts**:
  - NSW: **TfNSW Traffic Volume Viewer** `https://maps.transport.nsw.gov.au/egeomaps/traffic-volumes/index.html` (selected permanent and sample counting stations; API and hourly counts since 2006 on `https://opendata.transport.nsw.gov.au/data/dataset/nsw-roads-traffic-volume-counts-api`; TfNSW warns of data-quality and sensor-availability issues and a rebuild with no completion date — checked 2026-10-28)
  - VIC: **Department of Transport and Planning open data** `https://opendata.transport.vic.gov.au/dataset/historical-annual-average-daily-traffic-volume` — AADT per declared-road segment for 2001–2019 only; later years only as raw telemetry, TIRTL and traffic-signal counts on `https://opendata.transport.vic.gov.au/` (checked 2026-10-28)
  - QLD: **TMR traffic census** for the state-declared road network (annual average traffic and heavy-vehicle counts; 2025 data published 6 Aug 2026): `https://www.data.qld.gov.au/dataset/traffic-census-for-the-queensland-state-declared-road-network`
  - WA: **Main Roads WA trafficmap** `https://trafficmap.mainroads.wa.gov.au/` — short-term samples and continuous counts on state roads, significant local roads and cycle paths over the past six years (checked 2026-10-28)
- **City open-data portals**: no AADT layers found — City of Melbourne's traffic counts cover 2014–2017 only, Brisbane City Council publishes key-corridor traffic volume reports, and a search of the City of Sydney portal returned no traffic-count dataset (checked 2026-10-28); use the state datasets above

### Key term

**AADT** (annual average daily traffic) — term used in Victoria's DTP datasets; TfNSW and TMR publish 'annual average' traffic counts (same concept as US/UK AADT).

### Verdict bands

- 🟢 < 1,500 v/d (residential)
- 🟡 1,500–10,000 v/d (collector road, suburban)
- 🟠 10,000–35,000 v/d (urban arterial)
- 🔴 > 35,000 v/d (motorway, M-roads, urban core)

---

## Section: `--tax`

### Annual property tax — Land Tax (state-based)

Land tax = **rate × land value** above threshold.

| State | 2026 threshold | Rate (above threshold) |
|---|---:|---|
| NSW | $1,075,000 (fixed at the 2024 value from the 2025 land tax year — freeze announced in the 2024-25 NSW Budget) | $100 + 1.6% above $1,075,000 (+ premium: $88,036 + 2% above **$6,571,000**, also frozen) (2026-10-28 verified, source [Revenue NSW thresholds and rates](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/thresholds-and-rates), updated 16 Mar 2026 — the earlier '2025-26 budget' attribution was wrong) |
| VIC | **$50,000** (temp. COVID-debt threshold cut from $300k, land tax years 2024–2033) | $500 flat ($50k–<$100k), $975 flat ($100k–<$300k), then $1,350 + 0.3% above $300k rising to $31,650 + 2.65% above $3M (the flat amounts carry the COVID Debt Repayment Plan surcharge, legislated to 30 Jun 2033; trusts have their own scale) (2026-10-28 verified, source [SRO VIC land tax current rates](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/land-tax-current-rates), updated 29 Sep 2026 + [SRO VIC COVID Debt Repayment Plan](https://www.sro.vic.gov.au/about-us/rates-and-statistics/covid-debt-repayment-plan)) |
| QLD | $600,000 (individuals) | $500 + 1% above $600,000; marginal 1.65% from $1M, 1.25% from $3M, 1.75% from $5M, top 2.25% above $10M; absentees: $350,000 threshold, own scale (marginal 1.7% from $350,000, 1.5% from $2.25M, 2% from $5M, top 2.5% above $10M) + 3% absentee surcharge (2026 data, source [QRO individual rates](https://qro.qld.gov.au/land-tax/calculate/individual/) + [QRO absentee rates](https://qro.qld.gov.au/land-tax/calculate/absentee/); 2026-10-28 verified — the individual scale has no 2.75% band) |
| WA | $300,000 | $300 flat to $420,000, then 0.25% marginal rising to 2.67% above $11M (2025-26 scale, source [WA DTF Overview of State Taxes and Royalties 2025-26](https://www.wa.gov.au/system/files/2025-11/ostr-2025-26.pdf), Nov 2025; 2026-27 scale not re-read — verify at RevenueWA) |
| SA | $936,000 (2026-27; indexed each year to site values — $833,000 in 2025-26) | 0.5% above $936,000, 1% above $1,504,000, 2% above $2,188,000, 2.4% above $3,504,000 (general rates; trust scale from $25,000) (2026 data, source [RevenueSA rates and thresholds](https://www.revenuesa.sa.gov.au/land-tax/rates-and-thresholds), read via its 21 Jun 2026 Wayback capture — the live page blocks scripted access) |
| TAS | $125,000 (since 1 Jul 2024) | $50 + 0.45% above $125,000; $1,737.50 + 1.5% above $500,000 (rates from 1 Jul 2025, source [SRO TAS rates of land tax](https://www.sro.tas.gov.au/land-tax/rates-of-land-tax); 2026-10-28 verified) |

**Principal place of residence (PPR)**: typically exempt.

### Council rates

Per LGA — est. **~0.2-0.4%** of land value annually + waste/water/services (set per-LGA and varies; verify with the relevant council's current rates notice).

### Transaction taxes (Stamp Duty)

State-based, varies hugely:

#### NSW (sliding to 5.5%; 7% premium duty)

- Up to $18,000: $1.25 per $100 (min $20) — 2026-27 brackets (by contract date), CPI-indexed each 1 Jul
- ... $11,602 + 4.5% above $387,000 to $1,290,000; $52,237 + 5.5% above $1,290,000; **premium duty** on residential property $194,137 + 7% above $3,870,000 — a $1M purchase pays $39,187 (2026 data, source [Revenue NSW calculate transfer duty](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/transfer-duty/understanding-transfer-duty/calculate-transfer-duty), updated 6 Oct 2026; 2026-10-28 verified)
- **FHB Assistance Scheme (FHBAS)**: full exemption up to $800k, concessional up to $1M — **in place since 1 July 2023**; no public Revenue NSW statement that thresholds are annually indexed — verify at [Revenue NSW FHBAS guide](https://www.revenue.nsw.gov.au/property-professionals-resource-centre/duties-guides/first-home-buyers-assistance-scheme-guide) (2026-05-27 verified)

#### VIC (sliding to 6.5%)

- Up to $25k: 1.4%
- ... $2,870 + 6% above $130,000 to $960,000; **5.5% of the whole dutiable value** from $960,000 to $2M; top tier $110,000 + 6.5% above $2M (general rates, contracts from 1 Jul 2021; 2026 data, source [SRO VIC non-PPR duty rates](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/land-transfer-duty-non-principal-place-residence-current-rates), updated 29 Sep 2026)
- **Off-the-plan duty concession** (not an abolition): construction / refurbishment costs incurred on or after the contract date are subtracted from the dutiable value. **Temporary version** for contracts 21 Oct 2024 – 20 Apr 2027: all buyers incl. investors, companies and trusts, strata lots with common property only (apartments, units, townhouses), no value threshold, no owner-occupation — extended 6 months by the Building Legislation and Treasury Legislation (Tax Relief) Amendment Act 2026 (Royal Assent 23 Jun 2026); does NOT reduce foreign purchaser additional duty (FPAD is calculated on the pre-concession value). From 21 Apr 2027 (unless extended again) only the standard concession: individuals who qualify for the PPR concession or the first home buyer exemption / concession, post-concession dutiable value ≤ $750,000 (first home buyers) / ≤ $550,000 (other PPR), move in within 12 months and live there 12 months; the old $1M threshold covered contracts 1 Jul 2021 – 30 Jun 2023 only. SRO's 'Help to buy' page still shows a 20 Oct 2026 end — superseded by the Act (2026 data, source [SRO VIC off-the-plan concession](https://www.sro.vic.gov.au/buying-property/land-transfer-stamp-duty/concessions-exemptions-and-waivers/plan-duty-concession-0/understanding-plan-duty-concession) + [SRO VIC Tax Relief Amendment Act 2026 news](https://www.sro.vic.gov.au/about-us/news-and-events/news/building-legislation-and-treasury-legislation-tax-relief-amendment-act-2026); 2026-10-21 verified)
- **Vacant Residential Land Tax (VRLT)**: 1% → 2% → 3% of capital improved value by consecutive years liable (residential land with a home vacant more than 6 months of the previous year); **statewide from 2025** (before 2025, only 16 Melbourne council areas, at a flat 1%); **from 1 Jan 2026** also land in metropolitan Melbourne undeveloped for 5+ years and capable of residential development, at a flat 1% (2026 data, source [SRO VIC VRLT](https://www.sro.vic.gov.au/owning-property/vacant-residential-land-tax/understanding-vacant-residential-land-tax), updated 22 Oct 2026 + [VRLT current rates](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/vacant-residential-land-tax-current-rates))
- **VIC Short-Stay Levy 7.5%** (from 1 Jan 2025) of the total booking fee for each stay of less than 28 consecutive days (see `--rental` and `shared/regulatory-watch.md`)

#### QLD (sliding to 5.75%)

- **Home concessions limited to specified residents from 1 Aug 2026**: the home, first home, first home (new home) and first home vacant land concessions apply only to Australian citizens, permanent residents and specified foreign retirees (legacy subclass 405/410, already AFAD-exempt) for transactions signed on or after 1 Aug 2026 (contracts signed on or before 31 Jul 2026 unaffected whenever they settle); other temporary residents pay standard rates + the 8% AFAD where they are foreign acquirers — Revenue (Cost of Living Relief Locked-In Law) and Other Legislation Amendment Act 2026, Royal Assent 29 Jun 2026 (2026 data, source [QRO changes to home concessions](https://qro.qld.gov.au/event/changes-to-home-concessions) + [QLD Budget Paper No. 4 2026-27](https://budget.qld.gov.au/files/2026-27-budget-bp4-budget-measures.pdf); 2026-10-21 verified)
- **First home concession** (established home, eligible buyers): no duty at or below $700,000, partial concession under $800,000; **first home (new home)** and **first home vacant land** concessions reduce duty to nil with no value cap for contracts from 1 May 2025 (2026 data, source [QRO first home concession](https://qro.qld.gov.au/duties/transfer-duty/concessions/homes/first-home); 2026-10-21 verified)

### Foreign owner surcharges (state)

| State | Foreign buyer surcharge (duty) + annual foreign-owner land tax surcharge |
|---|---:|
| NSW | **+9%** surcharge purchaser duty + **5%** surcharge land tax a year on residential land, no threshold (2025 land tax year onward; 4% in 2023–24) |
| VIC | **+8%** foreign purchaser additional duty (contracts from 1 Jul 2019) + **4%** absentee owner surcharge on land tax |
| QLD | **+8%** AFAD + **3%** absentee land tax surcharge (land ≥ $350,000); from 1 Aug 2026 temporary residents (other than specified foreign retirees) also lose the home concessions |
| WA | +7% foreign buyers duty |
| SA | +7% foreign ownership surcharge (on top of duty) |
| TAS | **+8%** foreign investor duty surcharge (residential, agreements from 1 Apr 2020; 1.5% primary production) + **2%** foreign investor land tax surcharge (land acquired from 1 Jul 2022; payable even below the land tax threshold) |
| ACT | no duty surcharge; **0.75%** a year land tax surcharge on residential land owned by foreign persons (on Average Unimproved Value, from 1 Jul 2018) |
| NT | no duty surcharge; no land tax |

(2026 data; sources: Revenue NSW, SRO VIC, QRO, RevenueWA and SRO TAS pages read 2026-10-28; RevenueSA ([Mar 2025 Wayback capture](https://web.archive.org/web/20250331003923/https://www.revenuesa.sa.gov.au/stamp-duty-land/FOS/calculation-of-surcharge)) and ACT Revenue ([Dec 2025 Wayback capture](https://web.archive.org/web/20251206000812/https://www.revenue.act.gov.au/land-tax/foreign-ownership-surcharge)) because both live sites block scripted access; ACT / NT duty and NT land tax from the [WA DTF interstate comparison, Nov 2025](https://www.wa.gov.au/system/files/2025-11/ostr-2025-26.pdf); that table's footnote exempting citizens of eight treaty countries from the NSW surcharge is out of date — Revenue NSW says the treaty relief applied only from 21 Feb 2023 to 8 Apr 2024 ([Revenue NSW surcharge purchaser duty guide](https://www.revenue.nsw.gov.au/property-professionals-resource-centre/guides-rulings-cpns/topics/surcharge-purchaser-duty-guide/overview), updated 29 May 2026; 2026-10-29 verified))

### FIRB approval (federal)

**Foreign Investment Review Board** — required for foreign buyers:
- **Established dwelling ban: 1 Apr 2025 – 30 Jun 2029** (cannot buy resale homes; extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset; 2026-07-03 verified, source ATO / foreigninvestment.gov.au)
- **New dwelling / vacant land**: allowed with FIRB approval + fees; vacant land is generally conditional on construction being completed within 4 years (FIRB residential land guidance, updated 1 Jul 2026)
- **Fees scaled by value** (`https://foreigninvestment.gov.au/guidance/general/fees` — re-indexed each 1 Jul). FY2026-27 (applications 1 Jul 2026 – 30 Jun 2027), new dwellings / vacant land: $4,600 under $75,000; **$15,600** up to $1M; $31,300 up to $2M; $62,600 up to $3M, then +$31,300 per further $1M (max $1,245,500 over $40M); established dwellings (only the ban's exception categories): $13,800 under $75,000, $46,800 up to $1M (2026 data, source [FIRB Schedule of Fees v8, 1 Jul 2026](https://foreigninvestment.gov.au/sites/foreigninvestment.gov.au/files/2026-06/schedule-of-fees-v8.pdf); 2026-10-28 verified)
- **Vacancy fee**: annual, if the dwelling is occupied for fewer than 183 days in a vacancy year; **double the original application fee** for vacancy years starting on or after 9 Apr 2024 (equal to it before); a vacancy fee return is due to the ATO within 30 days of the end of each vacancy year, and a late return triggers the fee even if the dwelling was occupied (source [FIRB Guidance Note 10 v12, 19 Sep 2026](https://foreigninvestment.gov.au/sites/foreigninvestment.gov.au/files/2026-09/guidance-note-10-fees-v12.pdf); 2026-10-28 verified)

### Capital gains tax

- Marginal income tax + **50% discount** for >12-month hold — **legislated change from 1 Jul 2027**: for individuals, trusts and partnerships the 50% discount is replaced by cost-base indexation + a 30% minimum tax on gains accruing from 1 Jul 2027; gains accrued before then keep the 50% discount; new-build investors may choose either regime; treatment of foreign, mixed and temporary residents is left to later tranches — Treasury Laws Amendment (Tax Reform No. 1) Act 2026, Act No. 49 of 2026, assent 26 Jun 2026 (2026 data, source [APH bill r7493](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7493) + [ATO](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax); 2026-10-21 verified)
- **Main residence exemption** — full exemption owner-occupied
- **Foreign residents**: no main residence exemption for property sold after 30 Jun 2020 unless the life events test is met; no full 50% CGT discount for foreign or temporary residents on gains made after 8 May 2012 (apportioned for periods of Australian residency) (2026 data, source [ATO main residence exemption for foreign residents](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents), updated 22 Jun 2026 + [ATO CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount), updated 29 Jun 2026; read via Oct 2026 Wayback captures — ato.gov.au blocks scripted access)
- **FRCGW (vendor side)**: on every sale of Australian real property, no threshold (contracts from 1 Jan 2025), the buyer withholds 15% of the price at settlement unless the vendor hands over an ATO clearance certificate — a route open only to Australian-resident vendors (a foreign-resident vendor cannot get one; see the variation route in `shared/exit-seller-withholding.md`); regime broadened from 1 Oct 2026 by Act No. 86 of 2026 ('real property' definition, 365-day principal asset test, purchaser must consider whether a vendor declaration is false) (2026 data, source [ATO](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime); 2026-10-21 verified)

### GST

10% on new builds (margin scheme common).

### Total transaction cost (buyer side)

- NSW domestic ($1M): ~4.1–4.2% (= $39,187 transfer duty 2026-27 + est. $1,500–$3,000 legal), plus LMI if the deposit is under 20%
- VIC domestic ($1M): ~5.7–5.8% (= $55,000 duty — 5.5% of the whole value in the $960k–$2M band — + est. $1,500–$3,000 legal)
- VIC foreign ($1M new dwelling — established dwellings banned to 30 Jun 2029): ~15.2–15.4% (= $55,000 duty + $80,000 FPAD 8% + $15,600 FIRB fee FY2026-27 + est. legal; before any off-the-plan concession, which does not reduce FPAD)
- NSW foreign ($1M new dwelling): ~14.6–14.8% (= $39,187 transfer duty + $90,000 surcharge purchaser duty 9% + $15,600 FIRB fee + est. legal)

### Future risk

- FIRB ban extended to 30 Jun 2029 (realised — announced 2026-27 Federal Budget, from the original 31 Mar 2027 sunset; 2026-07-03 verified)
- VIC VRLT expansion realised: metropolitan Melbourne land undeveloped for 5+ years is liable from 1 Jan 2026 (flat 1% of capital improved value)
- State stamp duty reform proposals (NSW First Home Buyer Choice repealed 2023; replaced by FHBAS)
- **2027 negative-gearing + CGT reform** (legislated — Act No. 49 of 2026, applies from 1 Jul 2027; see `--rental` and the CGT block above): 'new residential dwelling' is defined by ministerial instrument; Treasury states the final definition will go into primary legislation via the Tax Reform No. 3 Bill 2026 (introduced 14 Oct 2026, not passed), whose 4 Aug 2026 exposure draft counts a dwelling as new if acquired within 24 months of its certificate of occupancy (12 months in the Budget) (2026 data, source [APH bill r7554](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554) + [Treasury exposure-draft release](https://ministers.treasury.gov.au/ministers/jim-chalmers-2022/media-releases/consultation-next-tranche-tax-reform-legislation); 2026-10-21 verified)

---

## Section: `--rental`

### Long-term residential

- **State Residential Tenancies Acts** govern (RTA NSW, RTA VIC, RTA QLD, etc.)
- **No-grounds evictions ended**: NSW from 19 May 2025 (landlords must give a valid reason, incl. for tenancies that began earlier — [NSW Fair Trading](https://www.nsw.gov.au/departments-and-agencies/fair-trading/news/changes-to-rental-laws)); VIC from 25 Nov 2025 (no notice to vacate without a valid reason, even at the end of a fixed term; the lease rolls to periodic — [Consumer Affairs Victoria](https://www.consumer.vic.gov.au/housing/renting/new-changes-to-rental-laws), updated 14 Oct 2026); other states — verify with the state tenancy authority
- **Rent increases**: NSW (all lease types, from 31 Oct 2024 — [NSW Fair Trading](https://www.nsw.gov.au/departments-and-agencies/fair-trading/news/changes-to-rental-laws)), VIC (in most cases — agreements from 19 Jun 2019; [CAV](https://www.consumer.vic.gov.au/housing/renting/rent-bond-bills-and-condition-reports/rent/rent-increases)) and QLD ([RTA QLD](https://www.rta.qld.gov.au/rental-law-changes)) allow at most one increase every 12 months; the ACT also caps the amount — generally no more than 10% above the growth in Canberra's rents CPI (the 'prescribed amount' — [ACT Government, Oct 2025 Wayback capture](https://web.archive.org/web/20251027123524/https://www.act.gov.au/housing-planning-and-property/renting/rent-increases)); no CPI-linked amount cap appears on the NSW Fair Trading, CAV or RTA QLD pages read 2026-10-28 — verify other states with their tenancy authority
- **Bond board**: state-administered (RTBA, etc.)

### Rental market benchmarks

- **ABS CPI Rents**: +3.6% in the 12 months to Sep 2026 (2026 data, source [ABS CPI, Sep 2026](https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/consumer-price-index-australia/latest-release), released 28 Oct 2026); the CPI measures rents paid by new and existing tenants, while advertised-rent measures track asking rents for new tenancies only ([ABS](https://www.abs.gov.au/articles/latest-insights-rental-market)), so the two diverge
- **NSW new-bond median weekly rent, Apr–Jun 2026**: Greater Sydney $780 (houses $800, flats/units $760; +5.4% YoY) · Rest of State $540 · NSW $720 (+5.9% YoY) (2026 data, source [NSW Rent and Sales Report](https://dcj.nsw.gov.au/about-us/families-and-communities-statistics/housing-rent-and-sales/rent-and-sales-report.html), DCJ, from bonds lodged; per-LGA and per-postcode tables)
- **Cotality, Sep 2026 (secondary)**: national rents +5.5% YoY; national vacancy rate 2.0% (Hobart 3.0%, Adelaide 1.4%); gross rental yields, dwellings, 3.9% nationally, from 3.4% in Sydney to 6.5% in Darwin (source [Cotality HVI Oct 2026](https://discover.cotality.com/hubfs/Article-Reports/COTALITY%20HVI%20OCT%202026%20FINAL.pdf))

### Short-let (Airbnb)

#### NSW

- 180-night cap on non-hosted STRA (exempt development pathway) in Greater Sydney, Ballina, certain land in Clarence Valley and certain land in Muswellbrook ([NSW Planning](https://www.planning.nsw.gov.au/the-planning-system/housing/short-term-rental-accommodation))
- STRA Property ID via NSW Planning Portal ($65 first 12 months; renewed annually, renewal fee $25 — [Planning Portal](https://www.planningportal.nsw.gov.au/stra))
- **Byron Shire 60 nights** from 23 Sep 2024 (tighter than statewide), except two 365-day mapped precincts in and around Byron Bay Town Centre and at Brunswick Heads

#### VIC

- 7.5% Short-Stay Levy from 1 Jan 2025
- No statewide night cap: the Short Stay Levy Act 2024 (No. 40 of 2024) sets the levy and no night limit (the 90-night cap costed by the Parliamentary Budget Office in Apr 2024 was a Greens proposal, not adopted); it also lets an owners corporation adopt a rule banning short stays in lots, except where the owner or tenant lives there as their principal place of residence; the Government said councils would get planning powers to regulate short stays — check the council's planning scheme for local limits ([Short Stay Levy Act 2024](https://content.legislation.vic.gov.au/sites/default/files/2024-10/24-040aa-authorised.pdf) + [Premier, 27 Aug 2024](https://premier.vic.gov.au/sites/default/files/2024-08/240827-More-Long-Term-Rentals-And-More-Social-Homes.pdf); 2026-10-29 verified)
- Mornington Peninsula moving to 90 nights — not confirmed by a primary source in the 2026-10-28 check — verify with Mornington Peninsula Shire

#### QLD

- Council-by-council (Brisbane, Gold Coast, Sunshine Coast register required — registration requirements not re-checked against council sources on 2026-10-28; verify with the council)

### Tax on rental

- Marginal income tax on net rental
- **Negative gearing**: net rental losses deductible against other income up to the 2026-27 income year; from the **2027-28 income year**, for established dwellings acquired on or after 7:30pm AEST 12 May 2026 (contract date counts, not settlement), losses are deductible only against residential property income incl. capital gains, excess carried forward, never against salary, wages or business income (s 26-155 ITAA97, Act No. 49 of 2026); dwellings held before the cutoff are grandfathered and genuinely new dwellings bought on first sale stay negatively gearable, but later buyers of that dwelling lose both negative gearing and the 50% CGT discount (2026 data, source [ATO](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax); 2026-10-21 verified)
- BTL mortgage interest deductible against rental income; for established dwellings bought from 7:30pm AEST 12 May 2026, net losses incl. interest are quarantined to residential property income from the 2027-28 income year (see above)
- Capital gains 50% discount (replaced for gains accruing from 1 Jul 2027 by indexation + 30% minimum tax — see `--tax`) + foreign-resident exemption loss

---

## Section: `--work=<profession>`

### Sources

- **Workforce Australia** (replaced jobactive from 1 Jul 2022): `https://www.workforceaustralia.gov.au/` (connection timed out from outside Australia on 2026-10-28; DNS resolves)
- **Seek.com.au** — biggest: `https://www.seek.com.au/`
- **Indeed.com.au**, **LinkedIn AU**, **CareerOne**, **Adzuna**
- **AHPRA** for healthcare, **Engineers Australia** for engineering, etc.

### Self-employment

- **Sole trader**: ABN registration via ABR
- **Pty Ltd**: ASIC registration — share structure, number and class of shares issued, and at least one member; ASIC's registration and shares pages set no minimum capital amount (checked 2026-10-28)
- **GST**: register at $75,000 GST turnover ($150,000 for non-profits; taxi and ride-sourcing drivers regardless of turnover) (2026 data, source [business.gov.au](https://business.gov.au/registrations/register-for-taxes/register-for-goods-and-services-tax-gst))
- **PAYG instalments**: ATO collects

### Salary benchmarks (ABS)

- **Median weekly earnings, full-time employees, main job, Aug 2025** (ABS Employee Earnings, released 12 Dec 2025, latest edition — figures may have changed since; annual figures computed as weekly × 52):
  - Greater Sydney: $1,846/wk (~$96,000/yr)
  - Greater Melbourne: $1,701/wk (~$88,500/yr)
  - Greater Brisbane: $1,750/wk (~$91,000/yr) · Greater Perth: $1,923/wk (~$100,000/yr)
  - Greater Adelaide: $1,646/wk (~$85,600/yr) · Greater Hobart: $1,700/wk (~$88,400/yr) · ACT: $1,818/wk (~$94,500/yr) · NT (whole territory): $1,750/wk (~$91,000/yr)
  - Australia: $1,741/wk (~$90,500/yr); all employees incl. part-time: $1,425/wk (source [ABS Employee Earnings](https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/employee-earnings/latest-release), Table 2)
- **Average weekly ordinary time earnings, full-time adults, May 2026** (a mean, so above the median): Australia $2,083.70/wk seasonally adjusted, +3.7% YoY (~$108,400/yr); by state (original): NSW $2,108.80 · VIC $2,041.10 · QLD $2,039.70 · SA $1,970.20 · WA $2,227.40 · TAS $1,846.30 · NT $1,984.10 · ACT $2,290.20 (2026 data, source [ABS Average Weekly Earnings](https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/average-weekly-earnings-australia/latest-release), released 13 Aug 2026)
- **Federal minimum wage**: $26.44/hr ($1,004.90/38-hr week) from 1 Jul 2026 — FWC *Annual Wage Review 2026* **[2026] FWCFB 3500** (2 Jun 2026): **modern award minimum wages +4.75%**, with a structural adjustment that lifts the lowest ongoing-employment award rate to the same $1,004.90 / $26.44 and the six-month entry-level rate to **$978.10/wk ($25.74/hr)**; the NMW figure is set to maintain alignment with the C13 classification rate rather than by a stated percentage (2026 data, source [FWC decision [2026] FWCFB 3500](https://www.fwc.gov.au/documents/decisionssigned/pdf/2026fwcfb3500.pdf) + [Fair Work Ombudsman](https://www.fairwork.gov.au/about-us/workplace-laws/annual-wage-review/annual-wage-review-2026); 2026-09-18 verified)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Bureau of Meteorology (BoM)** | `https://www.bom.gov.au` | Fire Danger Ratings, flood maps, climate |
| **Geoscience Australia** | `https://www.ga.gov.au` | Australian Flood Risk Information Portal (AFRIP) — a catalogue of council / state flood studies contributed up to 2018, now served through the Digital Atlas of Australia; not a current flood map, so get current mapping from the state tools below or the council (source [GA AFRIP page](https://www.ga.gov.au/scientific-topics/community-safety/projects/afrip), updated 12 Jan 2026; 2026-10-28 verified); earthquake catalogue |
| **NSW Rural Fire Service** | `https://www.rfs.nsw.gov.au` | Bush Fire Prone Land mapping (mandatory disclosure trigger) |
| **Climate Council Climate Risk Map** | `https://www.climatecouncil.org.au/resources/climate-risk-map/` | Six hazards (riverine flooding, surface-water flooding, coastal inundation, bushfire, extreme wind, tropical-cyclone wind) by area — NGO tool on Climate Valuation modelling, data as of Jan 2025; secondary, not a government overlay (2026-10-28 verified) |
| **AFAC Seasonal Bushfire Outlook** | `https://www.afac.com.au/seasonal-outlook` | Pre-season risk forecast |
| **CSIRO National Bushfire Intelligence Capability** | `https://research.csiro.au/nbic` | Research + projections |
| **ARPANSA** | `https://www.arpansa.gov.au/` | Radon — generally lower than the worldwide average in Australia (ARPANSA, read via a 10 Jul 2026 web-archive copy because the live site refuses scripted requests; 2026-10-28 verified) |
| **NSW Planning Portal Spatial Viewer** | `https://www.planningportal.nsw.gov.au/spatialviewer/` | NSW Government planning map viewer (loads 2026-10-28; layer content not checked from a scripted fetch); the formal disclosure is the s 10.7(2) planning certificate (Environmental Planning and Assessment Act 1979), a mandatory part of NSW conveyancing (source [DPHI practice note, 1 Jul 2026](https://www.planningportal.nsw.gov.au/sites/default/files/documents/2026/Practice%20Note%20-%20Guidance%20on%20section%2010.7%20planning%20certificate%20notations%20%281%29.pdf); 2026-10-28 verified) |
| **VicPlan** | `https://mapshare.vic.gov.au/vicplan/` | Victorian Government planning map viewer (loads 2026-10-28; zone / overlay content not checked from a scripted fetch) |
| **FloodCheck Queensland** | `https://floodcheck.information.qld.gov.au/` | Historic QLD flood studies and data; FloodCheck itself says it should not be used to determine the potential for flooding at the property level, and a replacement FloodCheck Information Portal is in development; current flood information comes from the local council (2026-10-28 verified) |

### Specific risks

- **Bushfire** — extreme + increasing:
  - Black Saturday, 7 Feb 2009 (173 dead, VIC) (source [2009 Victorian Bushfires Royal Commission summary](https://knowledge.aidr.org.au/media/4457/vbrc_summary.pdf) + [BoM](https://media.bom.gov.au/social/blog/2025/remembering-black-saturday-the-extraordinary-weather-behind-victorias-2009-bushfires/); 2026-10-28 verified)
  - Black Summer 2019-20 (33 dead, over 24M ha burned, over 3,000 homes destroyed) (source [Royal Commission into National Natural Disaster Arrangements report](https://www.royalcommission.gov.au/natural-disasters/report), 28 Oct 2020; 2026-10-28 verified — the old 18.6M ha figure is below the Royal Commission's)
  - **NSW Bush Fire Prone Land** mapping triggers building/disclosure rules — Bush Fire Attack Level runs BAL-LOW, BAL-12.5, BAL-19, BAL-29, BAL-40, BAL-FZ (flame zone); construction standard AS 3959 (source [NSW RFS](https://www.rfs.nsw.gov.au/plan-and-prepare/building-on-bush-fire-prone-land/building-after-bush-fire/your-level-of-risk), read via 2026 web-archive copies because rfs.nsw.gov.au refuses scripted requests; 2026-10-28 verified)
  - Insurance premiums rising for high BAL ratings
- **Flood** — major risk:
  - **NSW + QLD 2022** floods (Lismore, Brisbane) (source [BoM Special Climate Statement 76](https://www.bom.gov.au/climate/current/statements/scs76.pdf), 25 May 2022; 2026-10-28 verified)
  - **Tropical North**: cyclone-driven
  - **Murray-Darling basin**: river flooding
- **Cyclone**: QLD, NT + WA tropical north (Cyclone Tracy, Darwin, 21–25 Dec 1974; Yasi, QLD, 30 Jan – 3 Feb 2011) (source BoM [Tracy](https://www.bom.gov.au/cyclone/history/tracy.shtml) + [Yasi](https://www.bom.gov.au/cyclone/history/yasi.shtml); 2026-10-28 verified)
- **Drought**: severe + long-duration (Millennium Drought 1997–2009, peak 2001–2009; BoM puts the dry period at late 1996 to mid-2010) (source [BoM](https://www.bom.gov.au/climate/updates/articles/a010-southern-rainfall-decline.shtml); 2026-10-28 verified)
- **Earthquake**: low-moderate; Newcastle 28 Dec 1989 (ML 5.6 / Mw 5.4, 13 dead) (source [Geoscience Australia](https://www.ga.gov.au/news/30-years-on-commemorating-the-1989-newcastle-earthquake); 2026-10-28 verified); Adelaide hill faults (not re-verified)
- **Storm surge** + sea-level rise: coastal communities (Gold Coast, Sunshine Coast)
- **Heatwaves**: increasing; records Melbourne 46.4°C (7 Feb 2009) and Sydney basin 48.9°C at Penrith Lakes AWS (4 Jan 2020; replaces the old 47.3°C figure) (source BoM [Black Saturday](https://media.bom.gov.au/social/blog/2025/remembering-black-saturday-the-extraordinary-weather-behind-victorias-2009-bushfires/) + [Sydney Jan 2020](https://www.bom.gov.au/climate/current/month/nsw/archive/202001.sydney.shtml); 2026-10-28 verified)
- **Coastal erosion**: NSW, Gold Coast

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1970** | Lead-based paint (NSW EPA names houses built before 1970); some old plumbing solder contained lead (2024 data, source NSW EPA [1](https://www.epa.nsw.gov.au/sites/default/files/24p4541-lead-gardening-and-home-renovations.pdf) + [2](https://www.epa.nsw.gov.au/sites/default/files/24p4542-lead-your-health-around-the-home.pdf); 2026-10-28 verified) |
| **1940s–1980s** | Asbestos very common — peak residential use mid-1940s to late 1980s; crocidolite (blue) and amosite (brown) bans phased in from the late 1970s; asbestos mining stopped by 1983; total ban on all forms, incl. chrysotile (white), from 31 Dec 2003; asbestos is in 1 in 3 homes (2025 data, source [ASSEA facts and figures guidance](https://www.asbestossafety.gov.au/sites/default/files/2025-11/ASSEA_Asbestos_Facts_and_Figures_Guidance_2025.pdf), read via web-archive copy; 2026-10-28 verified — the old 'white until 1987, blue/brown until 1985' dates are not in it) |
| **1980s–2003** | Phased out of building products by 1990; a home built or renovated before 1990 might contain asbestos, a building constructed after 2003 is not expected to (ASSEA, same source + [householder guide](https://web.archive.org/web/20260912165204/https://www.asbestossafety.gov.au/about-asbestos/practical-guidance/householders-and-home-renovators)) |
| **2000s+** | Modern code; energy improvements |
| **2023+ (NCC 2022)** | New homes: thermal performance equivalent to 7 stars NatHERS plus a whole-of-home annual energy budget; state adoption varies — NSW Enhanced BASIX 1 Oct 2023, ACT 15 Jan 2024, VIC 1 May 2024, SA 1 Oct 2024, WA 1 May 2025, NT limited to 5-star, TAS housing provisions not adopted, QLD via Queensland Modern Homes (source ABCB [overview](https://www.abcb.gov.au/news/2022/overview-changes-energy-efficiency-and-condensation) + [adoption dates](https://www.abcb.gov.au/ncc-2022-state-and-territory-adoption-dates), table correct as at 22 Sep 2023 — dates may have changed since; 2026-10-28 verified) |
| **AAC blocks (post-2000)** | Performance issues some buildings (unverified — no primary source found 2026-10-28) |
| **Building defects (NSW)** | Home Building Act 1989 statutory warranties: 6 years for major defects, 2 years for other defects, from completion of the work, plus 6 months if the breach appears in the last 6 months; Building Commission NSW handles complaints (2026 data, source [Building Commission NSW](https://www.nsw.gov.au/departments-and-agencies/building-commission/about-us/building-defect-complaints); 2026-10-28 verified) |
| **Aluminium composite cladding (post-Grenfell)** | Some buildings flagged — NSW Project Remediate is a voluntary (opt-in) program to replace flammable cladding on eligible class 2 apartment buildings confirmed by the Cladding Taskforce as high-risk, with a 10-year interest-free loan; registrations have closed and new registration enquiries are no longer accepted (2026 data, source [Building Commission NSW](https://www.nsw.gov.au/departments-and-agencies/building-commission/replace-flammable-cladding-through-project-remediate), updated 29 Jun 2026; 2026-10-28 verified); other states not re-verified |

### Mandatory at sale

| Document | State | Required because |
|---|---|---|
| **Section 32 / Vendor Statement** | VIC | Sale of Land Act 1962 s 32 — given to the buyer before the buyer signs (source [Consumer Affairs Victoria](https://www.consumer.vic.gov.au/housing/buying-and-selling-property/selling-property/conveyancing-and-contracts-for-sellers); 2026-10-28 verified) |
| **Contract for Sale + s 10.7 planning certificate + drainage diagram + title search + smoke-alarm and loose-fill asbestos notice (+ for a pool: certificate of compliance, occupation certificate with evidence of pool registration, or certificate of non-compliance — except strata / community schemes of more than two lots and off-the-plan)** | NSW | Conveyancing Act 1919 s 52A + Conveyancing (Sale of Land) Regulation 2022 Sch 1; if a document is missing the buyer may rescind within 14 days of exchange (source [NSW Government — sales contracts](https://www.nsw.gov.au/housing-and-construction/property-professionals/working-as-an-agent/sales-contracts); 2026-10-28 verified) |
| **Form 2 (Seller Disclosure Statement)** under Property Law Act 2023 (Qld) (effective 1 Aug 2025) + prescribed certificates | QLD | Given before the buyer signs; flooding history, structural soundness and past approvals are not required, so check flood risk separately (source [Queensland Government](https://www.qld.gov.au/housing/buying-owning-home/seller-disclosure-scheme); 2026-10-28 verified); replaces old contract warranties (per [Holding Redlich](https://www.holdingredlich.com/queensland-s-property-law-act-new-seller-disclosure-requirements-from-1-august-2025), law firm, 2026-05-27) |
| **Strata search report + s 184 certificate** (buyer's own checks, not a vendor disclosure) | NSW | Strata Schemes Management Act — NSW Government tells buyers to get a strata report and building inspection before buying; the s 184 certificate comes from the owners corporation (source [NSW Government](https://www.nsw.gov.au/housing-and-construction/strata/buying-a-strata-property); 2026-10-28 verified) |
| **Owners corporation certificate (s 151)** | VIC | Owners Corporations Act 2006 s 151; goes in the Section 32 statement; issued within 10 business days of a written request and fee (source [Consumer Affairs Victoria](https://www.consumer.vic.gov.au/housing/owners-corporations/finance-insurance-and-record-keeping/records) + [Act version 024](https://www.legislation.vic.gov.au/in-force/acts/owners-corporations-act-2006); 2026-10-28 verified) |
| **Pool safety certificate or Form 36** | QLD | With a current certificate the seller gives the buyer a copy before settlement; without one the seller lodges a Form 36 (notice of no pool safety certificate) with QBCC and gives the buyer a copy before settlement (before the contract at auction), and the buyer must get a certificate within 90 days of settlement (body corporate for shared pools) (source [QBCC](https://www.qbcc.qld.gov.au/home-owner-hub/swimming-pools/buy-sell-lease-property-pool); 2026-10-28 verified) |
| **Interconnected photoelectric smoke alarms** | QLD | Required once an agreement to transfer the land is made after 31 Dec 2021 (Fire Services Act 1990 s 147Z, prev s 104RBA); every dwelling by 1 Jan 2027 (source [Queensland legislation](https://www.legislation.qld.gov.au/view/whole/html/current/act-1990-010) + [qld.gov.au](https://www.qld.gov.au/emergency/safety/fire/smoke-alarms); 2026-10-28 verified) |

### Climate change projections

- **Temperature**: Australia has warmed 1.51 ± 0.23 °C since national records began in 1910; more extremely hot days projected, with larger warming inland than near the coast (source [BoM/CSIRO State of the Climate 2024](https://www.bom.gov.au/sites/default/files/2024-10/state-of-the-climate-2024.pdf); 2026-10-28 verified). City figures 'Sydney/Melbourne +2.0–3.5°C by 2050; +3-6 hot days >35°C' unverified — not in that report
- **Sea-level rise**: global mean sea level up over 22 cm since 1900, now rising close to 4 cm per decade (1993–2023); extreme sea levels that were 1-in-100-year events projected to become annual by 2100 under lower emissions and by mid-century under higher emissions (same source). '+20–80 cm by 2100' unverified
- **Bushfire**: dangerous fire weather days (FFDI above the 90th percentile) more frequent across most regions over the last 75 years; longer fire season and more dangerous fire weather days projected for much of the south and east (same source). 'FFDI +20-50% by 2050' unverified
- **Drought**: more time in drought likely across many regions of southern and eastern Australia as cool-season rainfall falls (same source)
- **Cyclone**: fewer tropical cyclones but a greater proportion of high intensity, with heavier rain and higher seas amplifying impacts (same source); 'poleward shift; Brisbane increasingly cyclone-vulnerable' unverified

---

## Section: `--mains`

### Sources

- **Sydney Water**, **Hunter Water**, **Yarra Valley Water (Melbourne)**, **Melbourne Water**, **Urban Utilities (QLD)**, **SA Water**, **Water Corporation (WA)**
- Universal in metro areas; rural may have rainwater tanks + septic
- **Electricity price caps 2026-27** (1 Jul 2026 – 30 Jun 2027; standing-offer / reference prices, not the cheapest market deal): AER Default Market Offer (DMO 8, published 26 May 2026), residential flat rate per year — Ausgrid $1,899 (3,900 kWh), Endeavour $2,328 (4,900 kWh), Essential $2,604 (4,600 kWh), Energex (SE QLD) $1,988 (4,600 kWh), SA Power Networks $2,334 (4,000 kWh); the DMO covers only those five networks. Victoria: ESC Victorian Default Offer, average $1,591/yr on a flat tariff at 4,000 kWh, 5% lower (2026 data, source [AER final determination](https://www.aer.gov.au/system/files/2026-05/AER%20-%20Final%20determination%20-%20Default%20market%20offer%202026%E2%80%9327.pdf) Table 2.1, read via a 26 Oct 2026 web-archive copy because aer.gov.au refused scripted requests, + [ESC](https://www.esc.vic.gov.au/media-centre/regulator-reduces-victorian-default-electricity-prices), 25 May 2026; 2026-10-28 verified); elsewhere check the state regulator

### Costs

| Scenario | Cost (AUD) |
|---|---:|
| Mains connection | est. $5,000–$15,000 |
| Septic upgrade | est. $15,000–$35,000 |
| Rainwater tank | est. $2,000–$8,000 |
| Bored well | est. $10,000–$30,000 |

---

## Cost benchmarks (AU 2026)

| Work | Cost (AUD) |
|---|---:|
| Building + pest inspection | est. $500–$1,000 |
| Strata report | est. $300–$500 |
| Conveyancer / solicitor | est. $1,500–$3,000 |
| Stamp duty (varies massively) | see above |
| LMI (if <20% deposit) | est. $5,000–$30,000 |
| **Total transaction cost (NSW $1M)** | **~$40.7–42.2k (~4.1–4.2%)** = $39,187 duty 2026-27 + est. legal; + LMI if deposit < 20% |
| **Total transaction cost (VIC $1M)** | **~$56.5–58k (~5.7–5.8%)** = $55,000 duty + est. legal |
| **Total transaction cost (foreign NSW $1M, new dwelling)** | **~$146.3–147.8k (~14.6–14.8%)** = $39,187 duty + $90,000 surcharge + $15,600 FIRB fee + est. legal |
| Roof restoration | $5,000–$15,000 |
| Re-paint | $5,000–$15,000 |
| Bushfire-resilient retrofit | $10,000–$50,000 |
| Asbestos abatement | $3,000–$30,000 |
| Solar PV (5kW) | $4,000–$8,000 (with rebates) |
| Battery storage | $8,000–$15,000 |

## Active fiscal incentives (2025-2026)

- **First Home Buyer Assistance Scheme (FHBAS)**: NSW exempt up to $800,000, concessional under $1M (vacant land exempt up to $350,000, concessional under $450,000; contracts from 1 Jul 2023) (no public Revenue NSW statement confirming annual indexation — verify at Revenue NSW FHBAS guide)
- **Help to Buy Scheme**: federal (2024+) — equity contribution up to 40% (new) / 30% (existing); 10,000 places a year, minimum 2% deposit, property price caps by location ([firsthomebuyers.gov.au](https://firsthomebuyers.gov.au/australian-government-help-buy-scheme), 2026-10-28 verified)
- **First Home Owner Grant (FHOG)**: set per state — QLD $30,000 for new homes valued under $750,000 (contracts from 20 Nov 2023; $15,000 before), continued by the 2026-27 QLD Budget for four years beyond its scheduled 30 Jun 2026 end (2026 data, source [QLD Budget Paper No. 4 2026-27](https://budget.qld.gov.au/files/2026-27-budget-bp4-budget-measures.pdf); 2026-10-21 verified); NSW $10,000 (new homes up to $600,000; land + build up to $750,000 — [Revenue NSW](https://www.revenue.nsw.gov.au/grants-schemes/first-home-owner-new-homes-grant)); VIC $10,000 (new homes up to $750,000 — [SRO VIC](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/first-home-owner-grant-current-rates)); WA cap raised to $800,000 south of the 26th parallel for transactions from 7 May 2026 ([RevenueWA](https://www.wa.gov.au/government/announcements/2026-27-housing-taxation-package)); other states — verify at the relevant State Revenue Office
- **First Home Super Saver (FHSS)**: voluntary super contributions of up to $15,000 a financial year and $50,000 in total can be withdrawn, with associated earnings, for a first-home deposit ([firsthomebuyers.gov.au](https://firsthomebuyers.gov.au/first-home-super-saver-scheme))
- **Australian Government 5% Deposit Scheme** (formerly the Home Guarantee Scheme): first home buyers with a 5% deposit (single parents / legal guardians 2%); from 1 Oct 2025 no income caps, no waitlists and no LMI; property price caps by location ([firsthomebuyers.gov.au](https://firsthomebuyers.gov.au/australian-government-5-percent-deposit-scheme), 2026-10-28 verified)
- **Stamp duty concessions**: state-specific (QLD home concessions limited to citizens / PRs / specified foreign retirees from 1 Aug 2026, QLD first home (new home) and vacant land concessions uncapped from 1 May 2025; VIC off-the-plan concession — temporary all-buyer version for contracts to 20 Apr 2027, not an abolition; WA first home owner rate from 7 May 2026: no duty up to $600,000, concessional up to $800,000, vacant land nil up to $450,000 / concessional up to $550,000, and WA off-the-plan concession extended to 30 Jun 2028 ([RevenueWA](https://www.wa.gov.au/government/announcements/2026-27-housing-taxation-package)); see `--tax`)
- **Solar/Battery rebates**: federal STCs + state schemes

## Common listing platforms

- **realestate.com.au** — biggest
- **Domain.com.au** — second (CoStar Group since 27 Aug 2025)
- **Allhomes.com.au** (ACT focus; a Domain brand, so CoStar Group since Aug 2025)
- **Property.com.au** (an REA Group site), **Homely**

## Caveats unique to AU

- **Foreign-buyer established-dwelling ban 1 Apr 2025 – 30 Jun 2029** (FIRB — extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset; 2026-07-03 verified)
- **State-by-state divergence is extreme** — stamp duty, land tax, foreign surcharges, RTA all differ massively
- **Foreign owner surcharges**: duty NSW 9%, VIC 8%, QLD 8%, TAS 8%, WA 7%, SA 7% (none in ACT / NT); annual land tax surcharges NSW 5%, VIC 4% (absentee owners), QLD 3% (absentees), TAS 2%, ACT 0.75%; QLD temporary residents (other than specified foreign retirees) also lose the home / first home transfer-duty concessions for transactions signed from 1 Aug 2026
- **VIC VRLT statewide from 1 Jan 2025** + metro Melbourne land undeveloped for 5+ years from 1 Jan 2026
- **VIC Short-Stay Levy 7.5%** from 1 Jan 2025
- **NSW FHBAS** (annual indexation not confirmed by Revenue NSW — verify) (was First Home Buyer Choice 2022, repealed 2023)
- **FIRB fees + vacancy fee** for foreign-owned dwellings
- **Negative gearing** + **CGT 50% discount** both curtailed from 1 Jul 2027 (Act No. 49 of 2026): losses on established dwellings bought from 7:30pm AEST 12 May 2026 are quarantined to residential property income from the 2027-28 income year; the 50% discount is replaced by indexation + 30% minimum tax on gains accruing from 1 Jul 2027 (grandfathering and new-build carve-outs — see `--tax` / `--rental`)
- **Bushfire BAL ratings** drive insurance + building code; high-BAL means $50k+ retrofit
- **QLD pool sale**: a current pool safety certificate, or a Form 36 lodged with QBCC and given to the buyer before settlement (the buyer then has 90 days to get the certificate) — see the sale-documents table
- **NSW Bush Fire Prone Land** triggers special construction
- **Section 32 (VIC)** + **Form 2 Seller Disclosure Statement (QLD, new 1 Aug 2025)** + **Contract for Sale (NSW)** — mandatory pre-sale disclosures
- **Strata vs community title vs old-system title** — title quality varies
- **Aluminium composite cladding (post-Grenfell)** — some buildings flagged for remediation
- **Negative gearing** — from the 2027-28 income year deductible against other income only for grandfathered dwellings (held before 7:30pm AEST 12 May 2026) or new dwellings bought on first sale
- **AHPRA + ABS data** drive professional registration verification
- **AML/CTF Tranche 2 in force since 1 Jul 2026** — real-estate agents, conveyancers and lawyers are AUSTRAC reporting entities (AML/CTF program, CDD incl. PEP / targeted-financial-sanctions checks, suspicious-matter reporting); an agent brokering a sale treats both buyer and seller as customers, a conveyancer or lawyer screens only its own client — expect identity checks, and in a private sale screen the seller yourself against DFAT's Consolidated List (2026 data, source [AUSTRAC](https://www.austrac.gov.au/news-and-media/news/anti-money-laundering-and-counter-terrorism-laws-cover-thousands-more-businesses); 2026-10-21 verified)

## Reddit / forum sources

- **r/AusFinance** — biggest community
- **r/AusProperty**, **r/AustralianRealEstate**
- **r/sydney**, **r/melbourne**, **r/brisbane**
- **PropertyChat** forums
- **Domain Newsletter**, **realestate.com.au Insights**

## Verification authorities

| Authority | When to call |
|---|---|
| **State Land Registry / Titles Office** | Title verification |
| **State Revenue Office (SRO)** | Stamp duty + land tax |
| **Local Council** | Rates + zoning + permits |
| **Owner Corporation / Strata** | If apartment |
| **FIRB** | Foreign-buyer eligibility |
| **NSW RFS / VIC CFA** | Bushfire risk |
| **State conveyancer/solicitor** | Final closing |

## Source URL templates

| Source | URL pattern |
|---|---|
| realestate.com.au | `https://www.realestate.com.au/<region>` |
| Domain | `https://www.domain.com.au/` |
| Cotality (formerly CoreLogic) | `https://www.cotality.com/au/our-data/indices` (the old corelogic.com.au URL redirects here; checked 2026-10-28) |
| ABS Total Value of Dwellings | `https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/total-value-dwellings` (successor to the Residential Property Price Indexes: Eight Capital Cities, which ceased after the Dec 2021 release; latest Jun qtr 2026; checked 2026-10-28) |
| FIRB | `https://foreigninvestment.gov.au` |
| BoM | `https://www.bom.gov.au/` |
| Geoscience Australia | `https://www.ga.gov.au/` |
| NSW RFS BFP Land | `https://www.rfs.nsw.gov.au/plan-and-prepare/building-on-bush-fire-prone-land` (the old building-in-a-bush-fire-area path redirects here per a Dec 2025 web-archive capture; the live site refuses scripted requests; checked 2026-10-28) |
| Climate Council | `https://www.climatecouncil.org.au/resources/climate-risk-map/` |
| ATO | `https://www.ato.gov.au/` |
| AER Default Market Offer 2026-27 | `https://www.aer.gov.au/system/files/2026-05/AER%20-%20Final%20determination%20-%20Default%20market%20offer%202026%E2%80%9327.pdf` (NSW / SE QLD / SA electricity reference prices; aer.gov.au refused scripted requests 2026-10-28, PDF read via web archive) |
| ESC Victorian Default Offer 2026-27 | `https://www.esc.vic.gov.au/electricity-and-gas/prices-tariffs-and-benchmarks/victorian-default-offer/victorian-default-offer-price-review-2026-27` |
| nbn address check | `https://www.nbnco.com.au/check-address` (the old check-your-address path redirects here; checked 2026-10-28) |
| NSW crime statistics (BOCSAR) | `https://bocsar.nsw.gov.au/` |
| VIC crime statistics (Crime Statistics Agency) | `https://www.crimestatistics.vic.gov.au/` |
| Building Commission NSW | `https://www.nsw.gov.au/departments-and-agencies/building-commission` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Coverage check**: pricing (ABS Total Value of Dwellings + Cotality), traffic, tax (extreme state divergence), rental (state RTA), work, risks (bushfire + flood + cyclone + earthquake), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for the ABS Total Value of Dwellings Jun qtr 2026 medians and mean prices (preliminary, revised in later releases) + ABS CPI rents and NSW new-bond rents + foreign-buyer ban (1 Apr 2025 - 30 Jun 2029 confirmed — extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset) + FY2026-27 FIRB fees and vacancy-fee rules (Schedule of Fees v8, Guidance Note 10 v12) + RBA cash rate and APRA buffer / DTI limit + foreign owner surcharges for NSW, VIC, QLD, WA and TAS (NSW 9%, VIC 8%, QLD 8%, TAS 8%, WA 7%) + NSW, VIC, QLD and TAS land tax scales + NSW 2026-27 and VIC transfer duty + VIC VRLT + Short-Stay Levy 7.5% + NSW and VIC no-grounds eviction rules, rent-increase limits and NSW short-let rules + QLD Form 2 Seller Disclosure Statement (1 Aug 2025) and the other sale documents in `--risks` (NSW s 52A, VIC s 32 / s 151, QLD Form 36, QLD smoke alarms) + the bushfire, heat, drought, earthquake, lead and asbestos facts (Royal Commission, BoM, Geoscience Australia, NSW EPA, ASSEA) and the State of the Climate 2024 statements + AER DMO and ESC VDO 2026-27 electricity prices + the `--work` figures (ABS earnings, FWC minimum wage, GST thresholds) + 2027 negative-gearing / CGT reform (Act No. 49 of 2026, legislated) + QLD home-concession residency rule (from 1 Aug 2026) + VIC temporary off-the-plan concession (contracts to 20 Apr 2027) + AML/CTF Tranche 2 (in force since 1 Jul 2026); MEDIUM for the final 'new residential dwelling' definition (Tax Reform No. 3 Bill 2026 not passed), for the Cotality 30 Sep 2026 values, direction and rent / vacancy / yield figures (secondary aggregator, hedonic, revised for 12 months), for the SA, ACT and NT surcharge lines and the SA land tax threshold (web-archive captures of 2025 and Jun 2026 or the WA DTF Nov 2025 comparison, because the live sites block scripted access) and the WA land tax scale (2025-26; 2026-27 not re-read), for the GST and main-residence lines (ATO text not readable by script), for the NCC 2022 state adoption dates (ABCB table correct as at 22 Sep 2023), for the listing-platform audience figures (REA's and CoStar's own claims; Domain's #2 rank unverifiable) and for the unsourced qualitative hazard lines in `--risks` (BAL insurance premiums, tropical-north cyclones, Murray-Darling flooding, storm surge, coastal erosion, Adelaide hill faults); LOW for Mornington Peninsula 90 nights and QLD council registers (no primary source found; labelled in the body), the legacy climate figures and the AAC-block row (labelled unverified), and the est. strata levies, council-rate band, conveyancer / inspection / strata-report / LMI ranges (so the legal part of the buyer-cost totals is est.), mains cost rows and Cost benchmarks contractor rows (no primary price source; the roof, re-paint, retrofit, asbestos, solar and battery rows were not checked).
**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; the federal-minimum-wage line was fully re-verified and re-stamped 2026-09-18 against the FWC Annual Wage Review 2026 decision [2026] FWCFB 3500 — sections without a row in the per-section table below keep the 2026-07-03 date). Rental / visa tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Tax lines (2027 negative-gearing / CGT reform, VIC off-the-plan concession, QLD home-concession residency rule and FHOG, FRCGW 1 Oct 2026 changes) and the AML/CTF Tranche 2 caveat re-verified 2026-10-21 against APH / ATO / SRO VIC / QRO / AUSTRAC primary sources (see the AU entries in shared/regulatory-watch.md).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-28 | 2026-10-28 Tier-A refresh | EUR/AUD at the ECB reference rate of 28 Oct 2026 and the foreign-buyer ban dates re-verified; finance bullet added (RBA cash rate 4.60%, APRA buffer and DTI limit); LGA count, title-search fee and cadastre URLs not checked |
| `--price` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: benchmark table rebuilt from ABS Total Value of Dwellings Jun qtr 2026 (primary, preliminary) and Cotality HVI 30 Sep 2026 (secondary, labelled); the ceased RPPI (Dec qtr 2021) replaced; REA audience and Domain's CoStar ownership re-sourced; strata levies est.; Domain's monthly series (site blocks scripted access) and #2 rank unverifiable |
| `--traffic` | 2026-10-28 | 2026-10-28 Tier-A refresh | TfNSW viewer and data-quality notice, DTP VIC AADT (2001–2019 only), TMR census (2025 data) and Main Roads WA trafficmap checked; no city AADT layers found; verdict bands are skill thresholds, not source data |
| `--tax` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: NSW, VIC, QLD and TAS land tax, NSW 2026-27 and VIC transfer duty, VRLT, Short-Stay Levy, foreign surcharges for every state and territory, FIRB FY2026-27 fees and vacancy fee, foreign-resident CGT and the recomputed buyer-cost totals; WA land tax is the 2025-26 scale, SA and ACT read from web-archive captures, council-rate band est., GST and main-residence lines not readable (ato.gov.au); NG / CGT reform, FRCGW, QLD concessions and VIC off-the-plan rest on the 2026-10-21 re-verification |
| `--rental` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: NSW and VIC no-grounds eviction dates, rent-increase limits (NSW, VIC, QLD; ACT amount cap) and NSW short-let rules on primary sources; ABS CPI rents and NSW new-bond rents (primary) and Cotality rents, vacancy and yields (secondary) added; Mornington 90 nights, QLD council registers and the bond-board line not confirmed; VIC statewide night cap checked 2026-10-29 — none (Short Stay Levy Act 2024); negative-gearing lines rest on the 2026-10-21 re-verification |
| `--work` | 2026-10-28 | 2026-10-28 Tier-A refresh | ABS Employee Earnings Aug 2025 and AWE May 2026 replace the unsourced salary ranges; FWC minimum wage, GST thresholds and ASIC company rules re-verified; jobactive → Workforce Australia; Seek's 'biggest' claim, the PAYG line (ato.gov.au blocked) and the Workforce Australia URL (timed out) unverifiable |
| `--risks` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: source table (GA AFRIP, ARPANSA, Climate Council; NSW Spatial Viewer, VicPlan and FloodCheck added), Black Summer, heat, drought, cyclone and Newcastle figures, BAL scale, lead and asbestos eras, NCC 2022, NSW warranties, Project Remediate and the sale-documents table; climate lines re-sourced to State of the Climate 2024 with five legacy figures labelled unverified; BoM 'flood maps', six qualitative hazard lines and the AAC and 2000s+ rows not confirmed; NCRA 2025 unreachable |
| `--mains` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: AER DMO 2026-27 (five networks, read via web-archive copy) and ESC VDO 2026-27 added; water-utility names checked (SA Water behind a bot challenge); the four cost rows est., no primary price source; the metro / rural supply line not confirmed |
| Active fiscal incentives | 2026-10-28 | 2026-10-28 Tier-A refresh | FHBAS bands, Help to Buy places and deposit, FHOG for NSW and VIC and the WA cap, FHSS limits and the 5% Deposit Scheme re-verified; QLD FHOG and the QLD / VIC duty-concession items rest on the 2026-10-21 re-verification; Help to Buy start year not confirmed |
| Common listing platforms | 2026-10-28 | 2026-10-28 Tier-A refresh | Domain and Allhomes under CoStar Group (since 27 Aug 2025), property.com.au an REA Group site; all five sites live; Domain's #2 rank and Allhomes' ACT focus unverifiable (sites block scripted access) |
| Caveats unique to AU | 2026-10-28 | 2026-10-28 Tier-A refresh | Legal / fiscal lines only: foreign surcharges (TAS and land-tax surcharges added), VRLT wording and the QLD pool line (Form 36 route, aligned with `--risks`); NG / CGT, QLD concession and AML/CTF caveats rest on the 2026-10-21 re-verification; the disclosure-document caveat rests on the `--risks` sale-documents table; BAL retrofit, cladding and Bush Fire Prone Land caveats not checked |
| Source URL templates | 2026-10-28 | 2026-10-28 Tier-A refresh | 10 rows checked, 3 changed (Cotality, ABS Total Value of Dwellings replacing the ceased RPPI, NSW RFS path); 6 rows added (AER DMO, ESC VDO, nbn, BOCSAR, CSA VIC, Building Commission NSW); realestate.com.au, Domain and ATO block scripted checks |

## Extension TODOs

- [ ] Per-LGA council rates table
- [ ] State-by-state stamp duty calculator
- [ ] State-by-state foreign surcharge specifics
- [ ] BAL bushfire rating verification flow
- [ ] Strata vs Owners Corp regulations per state
- [ ] FIRB application flow (new dwelling vs vacant land)
- [ ] Negative gearing optimization decision tree
- [ ] CGT main residence + foreign-resident transition
- [ ] State-by-state RTA tenant protections
- [ ] Bushfire BAL retrofit cost estimator

## Update history

- **2026-10-29** — Tier-A refresh (market, tax-legal, risk-infra; sources read 2026-10-28, corrections re-checked 2026-10-29); playbook-level date not re-stamped because `--price`, `--tax`, `--rental`, `--risks` and `--mains` each keep secondary, est. or unverifiable figures
  - Re-verified (facts checked — changed / confirmed / unverifiable): Country profile 2 — 1 / 1 / 0, plus a finance bullet added; `--traffic` 10 — 3 / 3 / 4 (the 4 are skill verdict bands)
  - Checked, not fully verified: `--price` 56 — 48 / 3 / 5; `--tax` 58 — 15 / 34 / 3, plus 6 held on the 2026-10-21 regwatch re-verification; `--rental` legal rules 13 — 3 / 3 / 4, plus 3 held, and 3 market-benchmark bullets added; `--work` 17 — 6 / 8 / 3; `--risks` 43 — 16 / 13 / 14, plus 5 rows added; `--mains` 12 — 4 / 7 / 1, plus an electricity-price bullet added; Active fiscal incentives 6 — 1 / 3 / 0, plus 2 held; Common listing platforms 7 — 2 / 3 / 2; Caveats unique to AU 11 — 2 / 4 / 2, plus 3 held (legal / fiscal only), and the QLD pool line aligned with `--risks`; Cost benchmarks (transaction rows only) 7 — 3 / 0 / 4; Source URL templates 10 — 3 / 4 / 3, plus 6 rows added
  - Totals: 252 facts checked — 107 changed / 86 confirmed / 45 unverifiable / 14 held on the 2026-10-21 re-verification
  - Main changes: ABS Total Value of Dwellings Jun qtr 2026 replaces the ceased RPPI and the stale benchmark table, with Cotality 30 Sep 2026 values as a labelled secondary source; Domain under CoStar Group since 27 Aug 2025; rental benchmarks added (ABS CPI rents, NSW new-bond rents, Cotality); ABS earnings replace the salary ranges; jobactive → Workforce Australia; RBA cash rate, APRA buffer and DTI limit added; NSW land tax freeze dated to the 2024-25 Budget, QLD top rate 2.25% (not 2.75%), SA threshold $936,000 (2026-27), TAS $125,000 / 0.45%; NSW 2026-27 duty with 5.5% above $1,290,000 and 7% premium duty; foreign surcharges for every state and territory, incl. TAS 8% duty + 2% land tax; FIRB FY2026-27 fees and vacancy-fee rules; buyer-cost totals recomputed (NSW $1M ~4.1–4.2%, was 5–6%); NSW and VIC no-grounds eviction dates; Black Summer over 24M ha, Sydney basin 48.9°C, Millennium Drought 1997–2009; lead pre-1970 and ASSEA asbestos eras; NCC 2022 and NSW warranty rows added; QLD pool sale via Form 36; climate lines re-sourced to State of the Climate 2024; AER DMO and ESC VDO 2026-27 added; cost rows without a primary price source labelled est.
