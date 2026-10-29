# United Kingdom 🇬🇧 — Property Due-Diligence Playbook

ISO2: `uk` (or `gb`). Status: ✅ Fully populated (researched 2026-04). **Last refreshed**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged).

## Country profile

- **Postcode**: alphanumeric (`SW1A 1AA`, `EC1A 1BB`); reliable address identifier
- **4 nations with separate land-registration regimes**:
  - England + Wales: HM Land Registry
  - Scotland: Registers of Scotland
  - Northern Ireland: Land Registry NI
- **Currency**: **GBP (£)**; volatile vs EUR (post-Brexit)
- **Languages**: English (de facto); Welsh (Wales co-official); Gaelic (Scotland minority)
- **Identifier**: Title number (England/Wales: `SY123456`); folio (NI); search sheet (Scotland)
- **Ownership types**:
  - **Freehold** — own land + building outright (most houses)
  - **Leasehold** — lease (typically 99–999 yrs) over a unit; ground rent + service charges (most flats)
  - **Share of freehold** — leasehold + collective freehold ownership via management co
  - **Commonhold** — rare today; draft Commonhold and Leasehold Reform Bill (Jan 2026) would make it the default for new flats — announced in the King's Speech 13 May 2026; final Bill not yet introduced as of 21 Oct 2026 (no Commonhold bill on the Parliament Bills register); the PM has said it will be introduced before Christmas 2026 (per Leasehold Advisory Service news)
  - **Heritable** (Scotland) — outright ownership of land (≈ freehold)

## Section: `--price`

### Primary sources

- **HM Land Registry Price Paid Data** (FREE; sales in England and Wales lodged for registration, 1 Jan 1995 onwards, updated monthly — Scotland and NI not covered): `https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads` (2026-10-28 verified)
- **HM Land Registry — Search for land and property information** (England and Wales): `https://search-property-information.service.gov.uk/` — title summary viewable online (title number, owner, price paid, tenure, lender); title register and title plan cost £7 each as online copies, £11 each as official copies (2026-10-28 verified; source [gov.uk Search the register](https://www.gov.uk/get-information-about-property-and-land/search-the-register))
- **Office for National Statistics (ONS) — Private rent and house prices, UK** (monthly; successor to the ONS "UK House Price Index" bulletin; carries UK HPI house prices and Price Index of Private Rents (PIPR) rents): `https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/privaterentandhousepricesuk/latest`
- **HM Land Registry — UK House Price Index** (monthly data by region, local authority and property type; joint HM Land Registry / LPS NI / ONS / Registers of Scotland production; Northern Ireland quarterly): `https://www.gov.uk/government/collections/uk-house-price-index-reports` — interactive search: `https://landregistry.data.gov.uk/app/ukhpi` (2026-10-28 verified)
- **Registers of Scotland** sale prices: `https://www.ros.gov.uk/`
- **Land & Property Services NI** (LPS): `https://www.nidirect.gov.uk/articles/valuation-domestic-properties-rates`
- **Bank of England** mortgage statistics. Macroprudential limit on high loan-to-income mortgages (4.5x income or more): from 28 Oct 2026 the 15% limit applies to aggregate new lending only — the firm-level cap is removed, so one lender may exceed 15% while the market stays within it; whether a lender offers 4.5x+ loans remains its own decision (2026 data, source [Bank of England PRA PS19/26](https://www.bankofengland.co.uk/prudential-regulation/publication/2026/october/high-loan-to-income-lending-policy-statement))
- **Council Tax band lookup** (England and Wales; Scotland via the Scottish Assessors website): `https://www.gov.uk/council-tax-bands`

### Listing platforms

- **Rightmove** — self-described "UK's number one property portal" (Rightmove plc); sold-price history from HM Land Registry / Registers of Scotland: `https://www.rightmove.co.uk`
- **Zoopla** — sold prices from HM Land Registry data + Zoopla house-price estimates: `https://www.zoopla.co.uk`
- **OnTheMarket**: `https://www.onthemarket.com`
- **PrimeLocation** (high-end)
- **PropertyData** (paid analytics)

### Price benchmarks (UK House Price Index, August 2026 data; Northern Ireland Q2 2026)

| Area (UK HPI geography) | Average price, all types | Semi-detached | Flat / maisonette | 12-month change (all types) |
|---|---:|---:|---:|---:|
| **United Kingdom** | £273,037 | £278,675 | £194,148 | +0.9% |
| **England** | £293,525 | £291,962 | £218,563 | +0.4% |
| **Inner London** (statistical area E13000001, not TfL fare zones) | £624,824 | £1,126,078 | £522,200 | -6.6% |
| Kensington and Chelsea (prime end) | £1,204,072 | £2,995,521 | £947,855 | -13.8% |
| **Outer London** (E13000002) | £510,931 | £689,402 | £334,010 | -0.1% |
| **Manchester** | £256,760 | £334,231 | £199,005 | +2.1% |
| **Birmingham** | £234,867 | £276,268 | £143,861 | +1.5% |
| **City of Edinburgh** | £301,313 | £454,000 | £244,953 | +2.8% |
| **City of Bristol** | £353,596 | £448,153 | £242,445 | +0.9% |
| **City of Glasgow** | £194,382 | £304,427 | £163,643 | +1.8% |
| **Liverpool** | £188,427 | £238,914 | £128,941 | +4.7% |
| **Leeds** | £246,385 | £269,544 | £151,317 | +2.4% |
| Smaller cities — e.g. City of Kingston upon Hull | £136,593 | £159,857 | £79,470 | +6.6% |
| Smaller cities — e.g. York | £311,865 | £335,176 | £180,669 | +0.7% |
| **South West** (region) | £304,139 | £325,573 | £173,470 | 0.0% |
| Rural South West — e.g. Cornwall | £274,570 | £275,595 | £144,637 | -2.9% |
| **Wales** | £216,363 | £215,812 | £130,206 | +3.1% |
| Rural Wales — e.g. Powys | £237,042 | £214,384 | £95,706 | +1.4% |
| **Scotland** | £198,397 | £226,592 | £138,886 | +2.9% |
| Rural Scotland — e.g. Highland | £224,574 | £215,076 | £126,614 | +7.4% |
| **Northern Ireland** (Q2 2026) | £202,487 | £204,283 | £148,475 | +9.2% |

Source: UK House Price Index (UK HPI), August 2026 — HM Land Registry / ONS release of 21 Oct 2026 ([data downloads](https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-august-2026--2): `Average-prices-2026-08.csv`, `Average-prices-Property-Type-2026-08.csv`); Northern Ireland is quarterly (Q2 2026). UK HPI averages come from completed, registered sales (not asking prices) through a hedonic, mix-adjusted model; below regional level they are 3-month moving averages, and the latest months are provisional (the first estimate uses around 40% of the transactions eventually registered), so local-authority figures revise. The UK HPI publishes no £/m² figure — compute £/m² per comparable as the HM Land Registry Price Paid sale price ÷ the floor area on its EPC. ONS headline: "Average UK house prices increased by 0.9%, to £273,000, in the 12 months to August 2026 (provisional estimate)". Rents (ONS PIPR, provisional): UK average £1,406/month, +3.8% in the 12 months to September 2026; England £1,466, Wales £848, Scotland £1,011; Northern Ireland £879 (July 2026, advertised new lets); local-authority rents are in the bulletin's local-area data. (2026-10-28 verified; sources [ONS Private rent and house prices, UK: October 2026](https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/privaterentandhousepricesuk/october2026) + [About the UK HPI](https://www.gov.uk/government/publications/about-the-uk-house-price-index/about-the-uk-house-price-index))

Est. £/m² for flats — UNVERIFIED (no primary source; kept from the 2026-04 population for orientation only, on its older area definitions): London Zone 1-2 ~8,000–18,000+ · Zone 3-6 ~5,000–10,000 · Manchester / Birmingham core ~3,200–5,000 · Edinburgh / Bristol ~4,000–6,500 · Glasgow / Liverpool / Leeds ~2,500–4,000 · smaller cities ~1,800–3,200 · rural England (S/SW) ~2,500–4,500 · rural Wales / Scotland / NI ~1,200–2,500.

### Compute

1. £/m² = price / **GIA (Gross Internal Area)** — UK standard; check EPC for verified m²
2. **Leasehold trap**: once a flat lease has 80 years or less unexpired, marriage value is payable on a statutory lease extension (LRHUDA 1993 Sch 13 para 4(2A): marriage value is nil only where the unexpired term "exceeds eighty years"; LAFRA 2024 abolishes marriage value but is not yet commenced — see `--tax` Future risk); value hit est. 10–30% (unsourced est.); est. hard to mortgage below 60 years (lender minimum unexpired terms vary)
3. **Ground rent doubling clauses** (pre-2017 leases) — major value killer
4. Cross-check sold-price history on Rightmove + Land Registry PPD

### Key terms

- Freehold vs leasehold vs commonhold
- GIA = Gross Internal Area
- Title number = Land Registry identifier
- EPC = Energy Performance Certificate

---

## Section: `--traffic`

### Sources

- **Department for Transport (DfT) — Road Traffic Statistics**: `https://roadtraffic.dft.gov.uk` — street-level Annual Average Daily Flow (AADF) at count points on Great Britain's roads (England, Scotland, Wales; every major-road link plus a sample of minor roads), count-point downloads 2000–2025; figures marked "Counted" are more reliable than "Estimated" ones (2026-10-28 verified)
- **TfL open data** (London: Tube and bus journeys and station footfall, PTAL public-transport-access grid at 100 m intervals, road network and live disruptions; London road traffic counts are in the DfT data above): `https://tfl.gov.uk/info-for/open-data-users/our-open-data` (2026-10-28 verified)
- **Transport Scotland**, **Transport for Wales** (their roads are already in the DfT data), **NI Department for Infrastructure** — Northern Ireland is not in the DfT data; DfI publishes its own traffic census reports in AADT ([Traffic and Travel Information 2023](https://www.infrastructure-ni.gov.uk/sites/default/files/publications/infrastructure/traffic-and-travel-information-report-2023.pdf): 67 census points; latest edition found on 2026-10-29)
- OSM `highway`: `motorway`; `trunk` (A-roads with primary status, green signs) / `primary` (other A-roads); `secondary` (B-roads); `tertiary` / `unclassified` (minor roads) — UK convention per the OSM wiki "Roads in the United Kingdom"

### Key term

**AADF (Annual Average Daily Flow)** — DfT's measure: "The average over a full year of the number of vehicles passing a point in the road network each day" (both directions). NI DfI reports use AADT for the same idea.

### Verdict bands

- 🟢 < 500 v/d (residential lanes, rural unclassified)
- 🟡 500–5,000 v/d (B-roads, suburban)
- 🟠 5,000–25,000 v/d (urban A-road, primary route)
- 🔴 > 25,000 v/d (motorway, urban core arterial)

---

## Section: `--tax`

### Annual property tax — Council Tax

- **8 bands** in England + Scotland (A–H); **9 bands** Wales (A–I); 8 in NI (different system: domestic rate based on capital value)
- Set per local council; varies widely
- Lookup band: `https://www.gov.uk/council-tax-bands`
- 2026-27 average bills by band (the exact bill varies by council — confirm via the gov.uk band lookup above and the council's own band-charge table):
  - Band A: England average ~£1,595/yr (computed: £2,392 Band D × 6/9 — LGFA 1992 s.5 sets bands A–H in the proportion 6:7:8:9:11:13:15:18); Scotland average gross bill £1,102 (2026-27 data)
  - Band D: England average **£2,392**/yr incl. adult social care and parish precepts (+4.9% on 2025-26; London area average £2,068), Wales average £2,283, Scotland average gross bill £1,653 (2026-27 data, sources [MHCLG Council Tax levels 2026-27](https://www.gov.uk/government/statistics/council-tax-levels-set-by-local-authorities-in-england-2026-to-2027/council-tax-levels-set-by-local-authorities-in-england-2026-to-2027) + [Welsh Government Council Tax levels 2026-27](https://www.gov.wales/council-tax-levels-april-2026-march-2027-html) + [Scottish Government consultation, band table](https://www.gov.scot/publications/consultation-council-tax-high-value-property-bands-mansion-tax/pages/2/))
  - Band H: England average ~£4,784/yr (computed: £2,392 × 18/9); Scotland average gross bill £4,051; Wales has a ninth band (I) above H (2026-27 data)
- **NI**: domestic rate = capital value (1 January 2005 values, capped at £400,000) × (district + regional rate); 2026-27 total domestic poundage runs from 0.9525% (Lisburn & Castlereagh) to 1.2214% (Derry City & Strabane) of capital value (2026-27 data, sources [Finance NI rate poundages](https://www.finance-ni.gov.uk/articles/rate-poundages) + [nidirect](https://www.nidirect.gov.uk/articles/how-rate-bills-are-calculated))
- Single-person discount: 25% (must apply)
- **England**: empty-home premium up to **+100%** once a home has been empty for 1 year (from **1 April 2024**; qualifying period was 2 years), up to +200% after 5 years and +300% after 10 years; second-home premium up to **+100%** since **1 April 2025** (Levelling-up & Regeneration Act 2023; council discretion; a council must decide at least 1 year ahead, so by 31 Mar 2024 for 2025-26). **Wales**: councils may charge up to **+300%** on second homes and long-term empty homes since 1 April 2023. (2026-10-28 verified; sources [gov.uk Council Tax premiums guidance](https://www.gov.uk/government/publications/long-term-empty-homes-and-second-homes-council-tax-premiums-and-exceptions/guidance-on-the-implementation-of-the-council-tax-premiums-on-long-term-empty-homes-and-second-homes) + [gov.wales Council Tax on empty and second homes](https://www.gov.wales/council-tax-empty-and-second-homes-html))
- **High Value Council Tax Surcharge ("mansion tax")** — announced Autumn Budget 2025 (26 Nov 2025): from **April 2028** (operative date 1 Apr 2028), England only, annual owner-paid charge on homes valued (in 2026) at £2M or more: £2,500 (£2M–£2.5M) / £3,500 (£2.5M–£3.5M) / £5,000 (£3.5M–£5M) / £7,500 (>£5M), CPI-uprated from 2029-30. Valuation Office targeted valuation exercise (April 2026 valuation date) to identify homes in scope; owners see draft bands in autumn 2027, first bills March 2028; revaluation 5-yearly (next 2033); challenge, then appeal to the Valuation Tribunal for England. Government response to the design consultation published at Budget 2026 (28 Oct 2026): deferral until change of ownership **confirmed** for owners with household income of £35,000 or less, savings of £16,000 or less, or a household member meeting disability criteria (interest charged, rate to be set in regulations); exemptions and discounts of up to 100% for e.g. care homes, student halls, registered social housing, working farmhouses and developer-owned new builds (full list in secondary legislation); a **100% premium** on homes left substantially unfurnished and unoccupied for 12 months or more; **no non-UK-resident premium** (considered, not adopted). Not yet law — to be legislated in Finance Bill 2026-27 (not yet published on 2026-10-28), secondary legislation in 2027. (2026-10-28 verified; sources [gov.uk HVCTS consultation outcome](https://www.gov.uk/government/consultations/high-value-council-tax-surcharge) + [HMT HVCTS guidance](https://www.gov.uk/government/publications/high-value-council-tax-surcharge/high-value-council-tax-surcharge) + [HMRC TIIN](https://www.gov.uk/government/publications/high-value-council-tax-surcharge-on-residential-properties/additional-council-tax-charge-on-high-value-properties))

### Transaction taxes

#### Stamp Duty Land Tax (SDLT) — England + NI

**MAJOR REFORM 1 April 2025** — nil-rate band reduced; surcharges raised October 2024:

| Band | Rate (single home) | Additional dwelling surcharge |
|---|---:|---:|
| £0–£125,000 | 0% | 5% |
| £125,001–£250,000 | 2% | 5% (+ standard) |
| £250,001–£925,000 | 5% | 5% (+ standard) |
| £925,001–£1,500,000 | 10% | 5% (+ standard) |
| £1,500,001+ | 12% | 5% (+ standard) |

- **First-time buyer relief**: 0% up to £300,000 (was £425,000); only on properties ≤£500,000
- **Additional dwelling (second home / BTL) surcharge**: **5%** on top of standard rates (raised from 3% on 31 October 2024)
- **Non-UK resident surcharge**: +2% on top (since 1 Apr 2021; an individual buyer is non-UK resident if not present in the UK for at least 183 days in the 12 months before purchase — nationality is irrelevant; companies have their own test) (2026-10-28 verified; source [HMRC SDLT rates for non-UK residents](https://www.gov.uk/guidance/rates-of-stamp-duty-land-tax-for-non-uk-residents))
- **Bulk purchases** (6+ dwellings in one transaction): can be taxed at non-residential rates; Multiple Dwellings Relief is abolished for transactions completing on or after 1 June 2024 (2026-10-28 verified; sources [gov.uk SDLT non-residential rates](https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates) + [HMRC SDLT reliefs](https://www.gov.uk/guidance/stamp-duty-land-tax-relief-for-land-or-property-transactions))
- **Mixed-use property**: non-residential rates — 0% to £150,000, 2% on £150,001–£250,000, 5% above (2026-10-28 verified; source [gov.uk SDLT non-residential and mixed rates](https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates))

#### Land and Buildings Transaction Tax (LBTT) — Scotland

| Band | Rate | ADS surcharge (additional dwelling) |
|---|---:|---:|
| £0–£145,000 | 0% | 8% |
| £145,001–£250,000 | 2% | 8% |
| £250,001–£325,000 | 5% | 8% |
| £325,001–£750,000 | 10% | 8% |
| £750,001+ | 12% | 8% |

- ADS raised to **8%** of the whole purchase price for transactions on or after **5 December 2024** (from 6%); first-time buyer relief raises the LBTT nil-rate band to £175,000 (2026-10-28 verified; sources [Revenue Scotland ADS](https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads) + [Revenue Scotland residential rates](https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property))

#### Land Transaction Tax (LTT) — Wales

- Main residential rates (since 10 Oct 2022): 0% to £225,000, 6% on £225,001–£400,000, 7.5% to £750,000, 10% to £1.5M, 12% above (2026-10-28 verified; source [Welsh Revenue Authority LTT rates and bands](https://www.gov.wales/land-transaction-tax-rates-and-bands))
- Higher residential rates (additional dwellings; companies buying residential property): a separate table, not a flat surcharge — since **11 Dec 2024** 5% to £180,000, 8.5% to £250,000, 10% to £400,000, 12.5% to £750,000, 15% to £1.5M, 17% above (each band 1 point up on the 4–16% table in force from 22 Dec 2020) (2026-10-28 verified; source [Welsh Revenue Authority LTT rates and bands](https://www.gov.wales/land-transaction-tax-rates-and-bands))

### Conveyancing fees

- **Solicitor / licensed conveyancer**: est. £1,000–£2,500 (2026 market range)
- **Searches** (Local, Drainage & Water, Environmental, Chancel): est. £200–£500 (2026 market range)
- **Land Registry fee** (England and Wales): Scale 1, £20 (portal, up to £80,000) to £1,105 (by post, over £1M; £500 via the portal) (2026-10-28 verified; source [HM Land Registry Registration Services fees](https://www.gov.uk/guidance/hm-land-registry-registration-services-fees))
- **Survey** (Level 2 HomeBuyers / Level 3 Building): est. £400–£1,500 (2026 market range)
- **Mortgage broker / lender fees**: est. £0–£1,000 (2026 market range)

### Total transaction cost (buyer side)

- **First-time buyer at £300k (England)**: ~0.6–1.9% of price (computed: £0 SDLT + est. £1,600–£5,500 conveyancing, searches, survey and broker fees from the ranges above + Land Registry fee £150 = £1,750–£5,650); a higher share on cheaper homes because the fees are largely fixed (~0.85–2.8% at £200k, where the Land Registry fee is £100)
- **Mover, single home, £300k–£500k**: ~2.2–4.1% (computed: SDLT £5,000–£15,000 + est. £1,600–£5,500 conveyancing, searches, survey and broker fees from the ranges above + Land Registry fee £150)
- **Second home / BTL, £300k–£500k**: ~7.2–9.1% (computed: SDLT incl. the 5% surcharge £20,000–£40,000 + est. £1,600–£5,500 conveyancing, searches, survey and broker fees from the ranges above + Land Registry fee £150)
- **High-value (£1M+)**: ~4.6% (£1M, only home) to ~17.4% (£5M additional dwelling bought by a non-UK resident) (computed: SDLT £43,750–£863,750 + est. £1,600–£5,500 conveyancing, searches, survey and broker fees from the ranges above + Land Registry fee £295–£1,105); an additional dwelling at £1M is ~9.6–10.0% (SDLT £93,750)

### Capital gains tax (CGT)

- **Principal Private Residence (PPR) relief**: full exemption for owner-occupied primary
- Investment property: 18% (basic-rate band) / **24%** (higher-rate band) — higher rate cut from 28 % → 24 % on **6 April 2024** (Finance (No. 2) Act 2024 s.6); the 30 Oct 2024 alignment was for non-residential / general CGT, not residential. Budget 2026 keeps 18% / 24% for 2027-28. (2026-10-28 verified; sources [gov.uk CGT rates and allowances](https://www.gov.uk/capital-gains-tax/rates) + [Budget 2026 OOTLAR Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances))
- Annual allowance: £3,000 (2024-25 through 2026-27; unchanged at £3,000 for 2027-28 per [Budget 2026 OOTLAR Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances); 2026-10-28 verified)
- **FA 2025 — Non-dom abolition + IHT residence-based (LTR test)**: from **6 April 2025**, the non-domiciled tax regime is abolished. New 4-year Foreign Income & Gains (FIG) regime for new arrivals. IHT shifts from domicile-based to residence-based: a UK-resident individual is a Long-Term Resident (within scope of IHT on worldwide assets) once UK-resident for ≥10 of the previous 20 tax years. Tail period on departure: 3 years (10–13 yr residency) up to 10 years (20+ yr residency). LTR status resets after 10 consecutive non-resident years. (2026-10-28 verified; sources [Finance Act 2025 — legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2025/8) + [HMRC IHT long-term resident guidance](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident))

### VAT

- Standard 20%
- Residential resale: VAT-exempt
- New build: zero-rated for buyer (developer recovers VAT)
- Conversions to residential: the builder's work converting a non-residential building into a dwelling, and renovating a home empty for 2+ years, is reduced-rated at 5%; the converter's first sale or long lease of a converted non-residential building can be zero-rated (2026-10-28 verified; source [VAT Notice 708](https://www.gov.uk/guidance/buildings-and-construction-vat-notice-708) ss.5, 7, 8)

### Future risk

- **Council Tax revaluation**: England still bands on 1 April 1991 values with no revaluation date (HVCTS above is a separate surcharge); Wales legislated revaluation years of 2028 and every fifth year after (Local Government Finance (Wales) Act 2024 s.20, amending LGFA 1992 s.22B; Welsh Ministers can change the year by order) — DEFERRAL ANNOUNCED 20 Oct 2026: the Welsh Government will bring forward legislation in November 2026 to defer the revaluation to the next Senedd term, no new year given (not yet law; 2026-10-29 verified, source [gov.wales](https://www.gov.wales/council-tax-revaluation-paused-in-difficult-budget-context); tracked in shared/regulatory-watch.md 🇬🇧 UK); Scotland plans new Bands I (£1M–£2M) and J (over £2M) from 1 April 2028, subject to primary legislation in the Scottish Parliament (consultation published 6 Jul 2026, closed 24 Aug 2026) (2026-10-28 verified; sources [VOA](https://www.gov.uk/guidance/understand-how-council-tax-bands-are-assessed) + [legislation.gov.uk](https://www.legislation.gov.uk/asc/2024/6/section/20) + [Scottish Government consultation](https://www.gov.scot/publications/consultation-council-tax-high-value-property-bands-mansion-tax/pages/1/))
- **Leasehold reform** — LAFRA 2024's valuation reforms (incl. **marriage-value abolition**) are enacted but NOT yet commenced (High Court dismissed freeholders' JR 24 Oct 2025; Court of Appeal granted permission to appeal 1 Apr 2026; MHCLG (2 Jul 2026) says the reformed valuation regime comes into force only after drafting flaws are fixed in the Commonhold and Leasehold Reform Bill; the deferment and capitalisation rates must also be set — MHCLG valuation-rates consultation published 15 Jul 2026, extended to close 21 Oct 2026, rates then need secondary legislation). Separately, the draft **Commonhold and Leasehold Reform Bill** was published 27 Jan 2026 (Written Statement HCWS1278) for pre-legislative scrutiny; Bill announced in the King's Speech **13 May 2026**, not yet introduced as of 21 Oct 2026 (the PM has said before Christmas 2026, per Leasehold Advisory Service news; govt told the HCLG Committee it would miss the 27 Jul 2026 deadline to respond to the Committee's report) — caps existing-flat ground rents at **£250/yr** (falling to a peppercorn after 40 years — govt position restated 2 Jul 2026; HCLG Committee asked govt to justify 40 yrs over a 20-yr transition and judged a late-2027 cap commencement possible vs govt estimate of late 2028), makes commonhold the default tenure for new flats and abolishes forfeiture (making commonhold the default outcome of collective enfranchisement and creating an independent managing-agent regulator are HCLG Committee recommendations, not draft-Bill provisions). (2026-07-03 verified; source [Commons Library CBP-10653](https://commonslibrary.parliament.uk/research-briefings/cbp-10653/); King's Speech, Court of Appeal permission, commencement dependency, 40-yr / late-2027 vs late-2028 positions and Bill non-introduction re-verified 2026-10-21 against the MHCLG quid-pro-quo consultation (2 Jul 2026), the HCLG Committee report, the MHCLG valuation-rates consultation (15 Jul 2026), Leasehold Advisory Service news and the Parliament Bills register)
- **CGT**: Budget 2026 left the main CGT rates unchanged — Annex A keeps 18% / 24% and the £3,000 annual exempt amount for 2027-28 (2026-10-28 verified; source [Budget 2026 OOTLAR Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances))
- **Stamp duty**: Budget 2026 (28 Oct 2026) made no change to residential SDLT rates, surcharges or first-time buyer relief — the [OOTLAR Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances) tables still carry the 1 April 2025 rates, the 5% additional-dwelling and 2% non-resident surcharges and first-time buyer relief to £300,000 (homes ≤£500,000); its only SDLT measures are technical (no SDLT on rent under assured tenancies from 1 May 2026, group relief, Local Government Pension Scheme relief) (2026-10-28 verified)

---

## Section: `--rental`

### Long-term residential

- **Tenancy type**: England — assured periodic tenancies replaced assured shorthold tenancies (ASTs) on **1 May 2026**; Wales — occupation contracts ('standard' in the private sector) replaced tenancy agreements on 1 Dec 2022 (Renting Homes (Wales) Act 2016); Scotland — the open-ended private residential tenancy since 1 Dec 2017 (Private Housing (Tenancies) (Scotland) Act 2016) (2026-10-28 verified; sources [gov.uk tenancy deposit protection](https://www.gov.uk/tenancy-deposit-protection) + [gov.wales Renting Homes](https://www.gov.wales/housing-law-changed-renting-homes) + [gov.scot PRT guide](https://www.gov.scot/publications/private-residential-tenancies-landlords-guide/))
- **Renters' Rights Act 2025** — Royal Assent **27 October 2025**; s21 "no-fault" evictions **abolished 1 May 2026** ("big bang" main commencement, SI 2026/421 reg 2(a); existing ASTs converted to assured periodic tenancies). Possession claims on a pre-1-May-2026 s21 notice had to be issued by the **earlier of the time left on the notice or 31 July 2026** — that window **closed 31 Jul 2026** (MHCLG guidance updated 1 Aug 2026: no new claims on pre-1-May s21/s8 notices; claims issued on or before 31 Jul continue) (2026 data, source [gov.uk](https://www.gov.uk/guidance/giving-notice-of-possession-to-tenants-before-1-may-2026)); Commencement No. 3 (SI 2026/638) brought local-authority financial penalties for category 1 hazards into force 22 Jun 2026; remaining provisions commence in later phases (MHCLG roadmap) — next is the PRS Database: draft Private Rented Sector Database Regulations 2026 (laid 9 Sep 2026, draft affirmative, not yet made as of 2026-10-21) bring landlord and dwelling registration in region by region from 15 Dec 2026 (West Midlands) to 15 Aug 2027 (South West) (2026-10-21 verified, source [draft PRS Database Regulations](https://www.legislation.gov.uk/ukdsi/2026/9780348286861)). (2026-07-03 verified; sources [Renters' Rights Act 2025](https://www.legislation.gov.uk/ukpga/2025/26) + [SI 2026/421](https://www.legislation.gov.uk/uksi/2026/421/contents/made))
- **Tenancy deposit scheme** mandatory: in England and Wales the deposit goes into TDS, DPS or mydeposits within 30 days; Scotland and NI have separate schemes (2026-10-28 verified; source [gov.uk tenancy deposit protection](https://www.gov.uk/tenancy-deposit-protection))
- **Right to Rent** (immigration check) mandatory in England
- **MEES (private rented sector, England and Wales)** — all PRS tenancies must meet **EPC C by 1 Oct 2030** (single compliance date, new + existing; Warm Homes Plan / DESNZ response 21 Jan 2026). Cost cap **£10,000** per property (exemption then registrable, valid 10 yrs; qualifying spend since 1 Oct 2025 counts). **Property Value Adjustment**: homes valued <£100k → cap is the lower of £10k or 10% of value. EPC C (EER) on an EPC issued before **1 Oct 2029** stays compliant until that EPC expires/is replaced; the Home-Energy-Model dual-metric standard applies thereafter. Not yet law: needs new powers by Act of Parliament plus an SI the govt aims to bring into force in 2027; reformed Home-Energy-Model EPCs now launch in the second half of 2027 (moved from Oct 2026, gov.uk 9 Mar 2026). Until 1 Oct 2030 the current standard stays EPC E with a £3,500 cap. (2026-10-21 verified; source [gov.uk PRS MEES consultation response](https://www.gov.uk/government/consultations/improving-the-energy-performance-of-privately-rented-homes-2025-update))

### Short-let (Airbnb / holiday let)

**FHL (Furnished Holiday Lettings) regime ABOLISHED**:
- **Abolition: 1 April 2025** (companies) / **6 April 2025** (individuals)
- Old reliefs gone: exemption from the finance-cost restriction (mortgage interest is now only a basic-rate credit, not fully deductible), capital allowances for new spend, CGT reliefs for trading assets (BADR, rollover, gift hold-over), pension relevant-earnings status, and free profit splits between spouses (now equal shares unless a Form 17 declaration) (2026-10-28 verified; sources [HMRC TIIN](https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/abolition-of-the-furnished-holiday-lettings-tax-regime) + [HMRC clarification](https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/clarification-on-abolition-of-the-furnished-holiday-lettings-tax-regime))
- Now treated as **standard property income** — same as long-let

### Local short-let rules

- **London**: a home can be short-let for up to **90 nights per calendar year** without planning permission if the host is liable for council tax on it; beyond that it is a material change of use needing permission (Deregulation Act 2015 s.44, inserting s.25A into the Greater London Council (General Powers) Act 1973; can be disapplied locally) (2026-10-28 verified; source [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/20/section/44))
- **Scotland / Edinburgh**: a council short-term let licence is mandatory for all short lets in Scotland (new hosts since 1 Oct 2022; existing hosts had to apply before 1 Oct 2023); the whole of Edinburgh has been a short-term let control area since **5 Sep 2022**, so letting a whole dwelling that is not the host's principal home needs planning permission (Badenoch and Strathspey designated 4 Mar 2024) (2026-10-28 verified; sources [gov.scot short-term lets](https://www.gov.scot/publications/short-term-lets/) + [City of Edinburgh Council](https://www.edinburgh.gov.uk/planning-13/short-term-lets-planning))
- **Wales**: anyone charging for overnight visitor stays (short lets included) must register with the Welsh Revenue Authority by **31 Mar 2027**, even where the council has no visitor levy (Visitor Accommodation (Register and Levy) Etc. (Wales) Act 2025, Royal Assent 18 Sep 2025); a licensing scheme, starting with self-catering accommodation, is ENACTED by the Development of Tourism and Regulation of Visitor Accommodation (Wales) Act 2026 (Royal Assent 27 Apr 2026) but NOT yet in force — legal default March 2030, regulations still to be consulted on (2026-10-29 verified; sources [gov.wales register](https://www.gov.wales/register-visitor-accommodation-wales) + [gov.wales Act page](https://www.gov.wales/visitor-accommodation-register-and-levy-etc-wales-act-2025) + [gov.wales licensing](https://www.gov.wales/licensing-visitor-accommodation-wales))
- **Northern Ireland**: a Tourism NI certificate must be in force before tourist accommodation, self-catering short lets included, is offered (Tourism (NI) Order 1992 art 14; 'tourist accommodation' is any overnight sleeping accommodation for tourists provided by way of trade or business, art 2) (2026-10-29 verified; sources [legislation.gov.uk art 14](https://www.legislation.gov.uk/nisi/1992/235/article/14) + [legislation.gov.uk art 2](https://www.legislation.gov.uk/nisi/1992/235/article/2) + [Tourism NI](https://www.tourismni.com/business-guidance/sector/accommodation/accommodation-getting-started/what-do-you-need-to-consider/))
- **EU 2024/1028 STR regulation**: NOT applicable (UK post-Brexit)

### Tax on rental

- **From 6 April 2027**: property income taxed at dedicated property rates, **ENACTED** by Finance Act 2026 s.6 (new ITA 2007 s.6D, effect for 2027-28 and later years per s.6(8)) + s.7 at basic 22% / higher 42% / additional 47% (2pp above main rates; announced at Autumn Budget 2025). **Budget 2026 (28 Oct 2026) announced a further 2pp: basic 24% / higher 44% / additional 49% from 6 April 2027** (England, Wales and NI; Scotland and Wales have been given the ability to set their own property rates), to be legislated in Finance Bill 2026-27 — **not yet law** (Bill text not published as of 2026-10-28), so the statute still reads 22/42/47 until it passes. Finance-cost (mortgage-interest) relief is tied to the property basic rate (FA 2026 Sch 1 para 40; see below). (2026-10-28 verified; sources [Budget 2026 OOTLAR 1.2](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar) + [legislation.gov.uk FA 2026 s.7](https://www.legislation.gov.uk/ukpga/2026/11/section/7); Autumn Budget 2025 announcement: [gov.uk technical note](https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note))
- Property income allowance £1,000/yr (de minimis)
- Mortgage interest restricted to a basic-rate tax credit (since 2020): 20% through 2026-27; from 2027-28 given at the property basic rate — FA 2026 Sch 1 para 40 substitutes PBR for BR in ITTOIA 2005 ss.274AA(5) and 274C(2) ([legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2026/11/schedule/1/paragraph/40), 2026-10-28 verified): 22% as enacted, **24%** if the Budget 2026 rise is enacted — the [Budget 2026 policy costings](https://assets.publishing.service.gov.uk/media/6ae1883fe4367e5c8b0467df/AB26_Policy_Costing.pdf) (p.74) say finance cost relief "will continue to be aligned to the property basic rate" (24% is derived from that alignment, not printed as a relief rate)
- ATED (company-owned UK dwellings worth over £500,000): annual charge from **£4,600** (£500,001–£1M) to £303,450 (over £20M) for 2026-27, rising 3.5% from 1 Apr 2027 (£4,750–£314,050); valuation date 1 Apr 2022. Companies buying a dwelling over £500,000 pay SDLT at a flat **17%** of the whole price in certain cases (since 31 Oct 2024; +2% if non-UK resident) (2026-10-28 verified; sources [Budget 2026 OOTLAR Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances) + [gov.uk ATED](https://www.gov.uk/guidance/annual-tax-on-enveloped-dwellings-the-basics))
- VAT: holiday accommodation (e.g. a house, flat or chalet let for holidays) is standard-rated at 20% whatever the length of stay (VAT Notice 709/3 para 5.2), except an off-season let of more than 28 days as residential accommodation where the local holiday trade is clearly seasonal, which is exempt (para 5.6); VAT is charged only once the provider is VAT-registered (compulsory above £90,000 taxable turnover) (2026-10-28 verified; sources [VAT Notice 709/3](https://www.gov.uk/guidance/hotels-holiday-accommodation-and-vat-notice-7093) + [gov.uk Register for VAT](https://www.gov.uk/register-for-vat))

---

## Section: `--work=<profession>`

### Sources

- **gov.uk Find a Job**: `https://findajob.dwp.gov.uk/`
- **Indeed** (`uk.indeed.com`; indeed.co.uk redirects there), **LinkedIn UK**, **Reed.co.uk**, **Totaljobs**, **CV-Library**
- **Profession bodies**: RIBA, GMC, NMC, ACCA, Bar Council, etc.
- **Salary benchmark — ONS ASHE 2026** (April 2026, provisional; final figures October 2027): median gross weekly earnings for full-time employees £811.20 (+5.8% on April 2025); median gross annual earnings £40,911 for full-time employees in the same job for at least a year; London had the fastest full-time growth (8.2%). Occupation and local-authority medians are in the ASHE datasets (2026-10-28 verified; source [ONS Employee earnings in the UK: 2026](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2026))

### Self-employment

- **Sole trader**: HMRC Self Assessment + Class 4 NI at 6% on profits £12,570–£50,270 and 2% above (2026-27). Class 2 is no longer compulsory: with profits of £7,105 or more it is treated as paid; below that, voluntary Class 2 is £3.65/wk (2026-27). Budget 2026 announced 2027-28 voluntary Class 2 at £3.80/wk and the Small Profits Threshold at £7,355, with Class 4 limits unchanged (announced, set by the annual NICs regulations) (2026-10-28 verified; sources [gov.uk self-employed NI rates](https://www.gov.uk/self-employed-national-insurance-rates) + [Budget 2026 Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances) + [OOTLAR](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar))
- **Limited company**: Companies House registration; Corporation Tax 19% small profits rate (profits £50,000 or less), 25% main rate (over £250,000), Marginal Relief in between (thresholds cut for short accounting periods and associated companies); Budget 2026 keeps 25% / 19% for the financial year from 1 Apr 2028 (Finance Bill 2026-27) (2026-10-28 verified; sources [gov.uk Corporation Tax rates](https://www.gov.uk/corporation-tax-rates) + [OOTLAR 1.38](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar))
- **VAT registration**: compulsory once taxable turnover goes over £90,000 in the last 12 months (or is expected to in the next 30 days); deregistration threshold £88,000; both unchanged for April 2027 per Budget 2026 Annex A (2026-10-28 verified; sources [gov.uk Register for VAT](https://www.gov.uk/register-for-vat) + [Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances))
- **Personal allowance**: £12,570, frozen through 2030-31 (Finance Act 2026 s.10 extends the FA 2021 freeze to 2028-29, 2029-30 and 2030-31); reduced by £1 for every £2 of adjusted net income over £100,000 (2026-10-28 verified; sources [legislation.gov.uk FA 2026 s.10](https://www.legislation.gov.uk/ukpga/2026/11/section/10) + [gov.uk Income Tax rates](https://www.gov.uk/income-tax-rates))
- **IR35** (off-payroll working) rules for contractors via PSC

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Environment Agency long-term flood risk** (England) | `https://check-long-term-flood-risk.service.gov.uk` | Long-term flood risk by postcode from rivers and the sea and surface water (both on the new NaFRA data published 28 Jan 2025) and from reservoirs — "the flood risk of an area, not a specific property" (gov.uk, read 2026-10-28) |
| **SEPA (Scotland) flood maps** | `https://map.sepa.org.uk/floodmaps` | Long-term flood risk for an area in Scotland from rivers, the sea and surface water — not for a specific property; the older viewer at `https://map.sepa.org.uk/floodmap/map.htm` is SEPA's flood risk management maps, "for responsible authorities" (SEPA, read 2026-10-28) |
| **Natural Resources Wales — Flood Risk Assessment Wales map** | `https://naturalresources.wales/flooding/check-your-flood-risk-on-a-map-flood-risk-assessment-wales-map/?lang=en` | Wales flood risk from rivers, the sea, surface water and small watercourses, and reservoirs, plus flood defences and coastal erosion; no official status for planning (use the Flood Map for Planning) (NRW, read 2026-10-28) |
| **DfI Rivers (NI) — Flood Maps NI** | `https://www.infrastructure-ni.gov.uk/topics/flood-maps-ni` | NI flood hazard map viewer — "the latest flood hazard information available from government" (DfI, read 2026-10-28) |
| **Mining Remediation Authority** (the Coal Authority until 28 Nov 2024) | `https://www.gov.uk/check-if-property-is-affected-by-coal-mining` | Free check whether a property is in a former coal mining area, then a paid coal mining report from £27 + VAT (mine entries within 20 m of the boundary, mine gas, other hazards, future mining); the old `www2.groundstability.com` address now redirects to `www.miningremediation.co.uk`, which blocks automated checks (gov.uk, read 2026-10-28) |
| **HSE COMAH** | `https://www.hse.gov.uk/comah/comah-establishments.htm` | Search public information on major-hazard establishments in your area under the COMAH Regulations 2015, which implement the EU Seveso III Directive 2012/18/EU (HSE + SI 2015/483 explanatory note, read 2026-10-28) |
| **UK Health Security Agency Radon** | `https://www.ukradon.org` | Radon affected areas postcode lookup |
| **British Geological Survey** | `https://www.bgs.ac.uk/` | Geology, sinkholes, ground stability |
| **Met Office** | `https://www.metoffice.gov.uk/` | Weather, climate |
| **DEFRA air quality** | `https://uk-air.defra.gov.uk/` | Air pollution |

### Specific risks

- **Flooding** — major risk: 6.3 million properties in England are in areas at risk of flooding from rivers, the sea or surface water (about 4.6 million from surface water, about 2.4 million from rivers and the sea); with climate change the total could reach about 8 million — one in four properties — by mid-century (2024 data, source [Environment Agency NaFRA, 17 Dec 2024](https://www.gov.uk/government/news/environment-agency-publishes-major-update-to-national-flood-and-coastal-erosion-risk-assessment)). These are area-level counts — check the address on the national maps above:
  - Tidal: Thames, Severn, Humber estuaries; East Anglian coast
  - River: Yorkshire (2007, 2015, 2019), Cumbria (Storm Desmond 2015)
  - Surface water: urban areas, storm drains
- **Subsidence**: clay soils (London, SE England) (not re-verified); subsidence claims rise after dry summers (not re-verified). The Environment Agency declared drought in parts of England in Aug 2022, in 2025 (Yorkshire became the second region on 12 Jun 2025) and again in 2026 — "a second consecutive summer drought", half of England by 29 Jul 2026 and Yorkshire from 9 Oct 2026 (sources [EA 12 Aug 2022](https://www.gov.uk/government/news/environment-agency-chairs-national-drought-group-as-parts-of-country-move-into-drought), [EA 12 Jun 2025](https://www.gov.uk/government/news/yorkshire-second-region-in-england-to-move-into-drought-status), [EA 29 Jul 2026](https://www.gov.uk/government/news/drought-declared-in-half-of-england), [EA 9 Oct 2026](https://www.gov.uk/government/news/environment-agency-declares-drought-status-in-yorkshire))
- **Coastal erosion**: in England, East Riding of Yorkshire (Holderness coast, e.g. Aldbrough, Skipsea), North Norfolk and Cornwall have some of the highest numbers of properties at risk; 3,500 properties are in areas at risk to 2055 and 10,100 to 2105 if Shoreline Management Plans are delivered (present-day climate; 5,200 and 19,700 with climate change; 32,800 and 65,100 without the plans) (2024 data, source [EA National assessment of flood and coastal erosion risk in England 2024](https://www.gov.uk/government/publications/national-assessment-of-flood-and-coastal-erosion-risk-in-england-2024/national-assessment-of-flood-and-coastal-erosion-risk-in-england-2024)); Wales: see NRW's coastal erosion risk map (North Wales not re-verified)
- **Radon**: Cornwall + Devon + Derbyshire + parts of Aberdeenshire (regions not re-verified) — check the UKHSA/BGS Affected Area map at ukradon.org (launched 1 Dec 2022; Isle of Man added 22 Oct 2025); radon is "attributed to 1,100 lung cancer deaths per year" in the UK; the map does not apply to basements or cellars, which should be treated as higher risk (sources [UKradon maps](https://www.ukradon.org/information/ukmaps) + [UKHSA/BGS, 2 Dec 2022](https://www.gov.uk/government/news/ukhsa-and-bgs-publish-updated-radon-map-for-great-britain)); the seller discloses radon tests and remedial work on TA6 q.8.3–8.4
- **Coal mining subsidence**: South Wales valleys, Yorkshire, Notts, Durham, Lanarkshire (coalfield list not re-verified) — "property near to past mining activities may be at risk of being on unstable ground"; a conveyancer usually orders a coal mining search in affected areas (Mining Remediation Authority check, see table above; gov.uk, read 2026-10-28)
- **Japanese knotweed**: disclosed by the seller on the TA6 (6th edition) property information form, q.8.6–8.7 (presence, survey report, management plan); the Law Society notes a property is usually considered at risk if knotweed grows on it or within 3 m of its boundary, and many sellers answer "not known" because a rhizome can be present with no visible growth (2026 data, source [Law Society TA6 explanatory notes](https://www.lawsociety.org.uk/topics/property/ta6-6th-edition-explanatory-notes)); effect on mortgage lending not re-verified — check the lender's policy
- **Storms**: Atlantic depressions; Storm Éowyn (24 Jan 2025) — "the UK’s most powerful windstorm for over a decade", with red warnings and fatalities; Storm Babet (18–21 Oct 2023) — the main impacts came from rain, 150–200 mm in the wettest parts of eastern Scotland and two red rain warnings (sources [Met Office storm season 2024/25](https://weather.metoffice.gov.uk/warnings-and-advice/uk-storm-centre/uk-storm-season-2024-25) + [2023/24](https://weather.metoffice.gov.uk/warnings-and-advice/uk-storm-centre/uk-storm-season-2023-24))

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Damp, no DPC, lead paint, lath-and-plaster, single-skin walls |
| **1900–1939** | Shallow foundations, lath-and-plaster, asbestos cement starts |
| **1945–1965** | Prefab/non-traditional concrete (Cornish, Wates, Airey — some condemned), asbestos |
| **1960s–1980s** | Asbestos very common (garages, soffits, AIB); High-Alumina Cement (HAC) concern; **RAAC** (reinforced autoclaved aerated concrete) — major scandal in schools/hospitals 2023-2024; for homes, the Regulator of Social Housing wrote on 7 Sep 2023 that RAAC failure is a risk in some public buildings constructed between the 1950s and 1980s, that it "is not widespread in social housing" but may be present in a small number of buildings, "particularly in flat roof and panel structures" ([RSH letter](https://www.gov.uk/government/publications/letter-to-registered-providers-about-raac)) |
| **1980s–2000s** | Cavity wall insulation issues (damp bridging); modern wiring; some asbestos remains |
| **Post-2010** | Building Regs Part L energy; Part E acoustic |
| **Post-Grenfell (2017)** | Cladding crisis — the EWS1 form was first designed for buildings over 18 m but can be asked for on blocks of any height (see Mandatory at sale); remediation ongoing: at end-Sep 2026, 4,732 residential buildings 11 m+ in England with unsafe cladding were monitored, 55% started or completed and 40% completed (2026 data, source [MHCLG Building Safety Remediation data release, Sep 2026](https://www.gov.uk/government/publications/building-safety-remediation-monthly-data-release-september-2026)) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **EPC** (Energy Performance Certificate) | Required on sale or let in England and Wales — phased in from 1 Jun 2007, all remaining cases from 1 Oct 2008 (SI 2007/991 Sch 1); rated A–G; reformed EPCs with four new headline metrics now launch in the second half of 2027 (gov.uk, 9 Mar 2026) | 10 years (gov.uk) |
| **Property Information Form (TA6, 6th edition 2025)** | Standard pre-contract enquiry (Law Society form); mandatory for Conveyancing Quality Scheme members on instructions from 30 Mar 2026 | At sale |
| **Fittings & Contents Form (TA10, 3rd edition 2013)** | What's included | At sale |
| **Leasehold Information Form (TA7, 5th edition 2025)** | Leasehold only; mandatory for Conveyancing Quality Scheme members on instructions from 30 Mar 2026 | At sale |
| **Searches**: Local, Drainage & Water (CON29DW), Environmental, Chancel | Solicitor-ordered | Per case |
| **EWS1** | Asked for by the lender's valuer on flats in multi-storey, multi-occupancy buildings with cladding; RICS's 2nd-edition standard (published 12 May 2026, effective 1 Nov 2026) sets when, with thresholds for over 6, 5–6 and 4-or-fewer storeys, and lets a PAS 9980 FRAEW summary replace it in some cases; "not a fire safety certificate" — ask for the building's fire risk assessment (RICS) | 5 years, whole building — in Scotland it can be flat by flat (RICS FAQ) |
| **Cavity wall insulation guarantee** | If installed | Per case |

- **MEES (private rented sector, England and Wales)** — proposed: a let property must reach **EPC C by 1 Oct 2030** (single compliance date; Warm Homes Plan / DESNZ response 21 Jan 2026). Cost cap **£10,000** per property (exemption valid 10 yrs); homes valued <£100k → cap is the lower of £10k or 10% of value; short-term lets out of scope. Not yet law (see shared/regulatory-watch.md 🇬🇧 UK) — until the higher standard applies on 1 Oct 2030, landlords must keep meeting the current EPC E standard with a £3,500 cap ([gov.uk landlord guidance](https://www.gov.uk/guidance/domestic-private-rented-property-minimum-energy-efficiency-standard-landlord-guidance), updated 5 May 2026). Sub-EPC-C stock faces upgrade cost or unlettability — see `--rental`. (2026-10-28 verified; source [gov.uk PRS MEES consultation response](https://www.gov.uk/government/consultations/improving-the-energy-performance-of-privately-rented-homes-2025-update))

### Climate change projections (UKCP18)

- Seasonal warming by 2070 under the high-emission scenario (UK average, 10–90% range): **+1.3 to +5.1 °C in summer**, **+0.6 to +3.8 °C in winter** (source [UKCP18 Headline Findings v4.0, Aug 2022](https://www.metoffice.gov.uk/binaries/content/assets/metofficegovuk/pdf/research/ukcp/ukcp18_headline_findings_v4_aug22.pdf) — still the Met Office's current headline summary, read 2026-10-28)
- Sea-level rise by 2100 vs 1981–2000: **London 0.29–0.70 m** (low emissions) / **0.53–1.15 m** (high); Edinburgh 0.08–0.49 m / 0.30–0.90 m — larger in the south than the north (UKCP18 Headline Findings v4.0, §4.1–4.3)
- An increased chance of warmer, wetter winters and hotter, drier summers, with more frequent and more intense extremes (UKCP18 Headline Findings v4.0, §3); properties in England in areas at flood risk could rise from 6.3 million to about 8 million by mid-century (EA NaFRA, 17 Dec 2024)
- Hot summers more frequent: the chance of a summer as hot as 2018 is already 12–25% and rises to about 50–60% by mid-century (UKCP18 §3.1.3); UK record 40.3 °C at Coningsby, Lincolnshire, 19 Jul 2022 — still the record in the [Met Office UK climate extremes table](https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-climate-extremes) (read 2026-10-28)

---

## Section: `--mains`

### Sources

- **Drainage & Water search (CON29DW)** — solicitor-ordered, est. ~£60–£90 (not re-verified — no water-company price list could be read on 2026-10-28); specifies sewer connection
- **Local water company**:
  - **Thames Water** (London + Thames Valley)
  - **Severn Trent** (Midlands)
  - **Anglian Water** (East)
  - **Yorkshire Water**, **United Utilities** (NW), **Northumbrian Water** (NE)
  - **Welsh Water (Dŵr Cymru)**, **South West Water**, **Wessex Water**, **Southern Water**
  - **Scottish Water** (Scotland)
  - **NI Water** (Northern Ireland)
  - Full list of England and Wales water companies (incl. Affinity, Bristol, Hafren Dyfrdwy, Portsmouth, SES, South East) at [CCW Find your water company](https://www.ccw.org.uk/advice-and-support/households/water-companies/); a new-build site may be served by a NAV company approved by Ofwat "to provide water and/or sewerage services to specific sites instead of the usual water company" (CCW, read 2026-10-28) — ask the seller who supplies the property
- **Energy (England, Scotland and Wales) — Ofgem price cap, 1 Oct–31 Dec 2026**: **£1,723/yr** for typical consumption paid by Direct Debit (+4% on the previous period); average Direct Debit rates — electricity 26.32p/kWh + 54.83p/day standing charge, gas 7.97p/kWh + 29.68p/day; no VAT on electricity from 1 Oct 2026 to 31 Mar 2027, 5% on gas. The cap covers standard variable tariffs only — not fixed deals, heat networks or heating oil. Ofgem resets it every 3 months and standing charges vary by region (2026 data, source [Ofgem](https://www.ofgem.gov.uk/your-energy-supply/your-energy-bill/energy-price-cap-unit-rates-and-standing-charges))

### Verification

- Most urban / suburban UK = **mains drains universal**
- Rural may be **septic tank**, **cesspool**, or **package treatment plant**
- **General Binding Rules** (England; which rules apply depends on whether the discharge started before 1 Jan 2015, before 2 Oct 2023 or later): a septic tank must not discharge directly to a watercourse — "as soon as possible" connect to the public foul sewer, replace it with a small sewage treatment plant or install a drainage field, with plans in place to do the work "within a reasonable timescale, usually 12 months"; on a sale, buyer and seller should agree who will be responsible for replacing or upgrading the system, as a condition of sale (gov.uk GBR guidance). Scotland, Wales and NI have their own rules (gov.uk)
- **Environmental permit** (England): needed only if the system cannot meet the General Binding Rules — e.g. a discharge over 2 m³ (2,000 l)/day to ground or 5 m³ (5,000 l)/day to surface water — and the EA will not issue one where connecting to the public foul sewer is reasonable (gov.uk 'Septic tanks and sewage treatment plants', updated 29 Jan 2025)

### Costs

| Scenario | Cost (est. £, 2026 indicative ranges — confirm with contractor quote) |
|---|---:|
| Connection to mains (where available) | 8,000–20,000 |
| Mains-line extension via water co | 15,000–60,000+ |
| Septic compliant replacement (sewage treatment plant) | 4,000–12,000 |
| Cesspool emptying | £200–£500 per visit |

---

## Cost benchmarks (est., UK 2026)

| Work | Cost (est. £, 2026 indicative ranges — confirm with quote) |
|---|---:|
| EPC | 60–120 |
| Level 2 HomeBuyer survey | 400–700 |
| Level 3 Building survey | 600–1,500 |
| Conveyancing | 1,000–2,500 |
| Searches + Land Registry fees | 220–1,605 (searches est. 200–500 + HM Land Registry Scale 1 fee 20–1,105) |
| **Total transaction cost (FTB at £300k)** | **~0.6–1.9%** (computed — see `--tax` Total transaction cost) |
| **Total transaction cost (mover, single home, £300k–£500k)** | **~2.2–4.1%** (computed — see `--tax` Total transaction cost) |
| **Total transaction cost (BTL/2nd home, £300k–£500k)** | **~7.2–9.1%** (computed — see `--tax` Total transaction cost) |
| Septic to mains conversion | 8,000–20,000 |
| Septic compliant replacement | 4,000–12,000 |
| Damp-proof course | 2,000–5,000 |
| Re-roof (slate, semi-detached) | 8,000–18,000 |
| Cavity wall insulation | 1,000–3,500 |
| Insulation upgrade EPC D → B | 10,000–25,000 |
| RAAC removal (where applicable) | 30,000–200,000+ |
| Knotweed treatment | 2,500–10,000 |
| Cladding remediation (post-Grenfell) | varies massively (developer-paid) |

## Active fiscal incentives (2025-2026)

- **Help to Buy**: ended 2023 in England (applications closed end-Oct 2022); Help to Buy – Wales takes applications until 31 Mar 2027 (2026 data, source [gov.wales](https://www.gov.wales/help-buy-wales))
- **Your First Home** — ANNOUNCED 26 Sep 2026, details confirmed at Budget 2026 (28 Oct 2026), NOT yet open: England-only equity loan for first-time buyers of a new-build home (main home) from a participating developer; deposit of at least 2.5% (max 15%) + repayment mortgage from a participating lender + 20% government equity loan, interest-free for 5 years, then 1.5% in year 6 and 3% from year 7; the loan is repaid as 20% of the home's value at the time (normally on sale); household income cap £110,000 (£140,000 in London); local price caps based on local-authority median prices (Inner London £650,000, Outer London £500,000; full list to follow); pre-registration by end-Dec 2026, first applications Feb 2027, first sales Apr 2027 (2026 data, sources [gov.uk Your First Home](https://www.gov.uk/government/publications/your-first-home/your-first-home) + [Budget 2026](https://www.gov.uk/government/publications/budget-2026-document/budget-2026-html); tracked in shared/regulatory-watch.md 🇬🇧 UK)
- **First Homes scheme**: new-build homes sold at least 30% below market value (councils can require 40% or 50% where they show need) to first-time buyers in England; councils may prioritise key workers, but the scheme is not limited to them; the requirement that 25% of s106 affordable homes be First Homes no longer applies, though the option remains (2025 data, sources [gov.uk First Homes guidance](https://www.gov.uk/guidance/first-homes) + [government response to the NPPF consultation](https://www.gov.uk/government/consultations/proposed-reforms-to-the-national-planning-policy-framework-and-other-changes-to-the-planning-system/outcome/government-response-to-the-proposed-reforms-to-the-national-planning-policy-framework-and-other-changes-to-the-planning-system-consultation) — figures may have changed since)
- **Lifetime ISA** (UK residents aged 18–39 to open): save up to £4,000 a year with a 25% government bonus (max £1,000 a year), withdrawn charge-free towards a first home costing £450,000 or less, bought with a mortgage at least 12 months after the first payment. **From 29 Oct 2026** (ENACTED, SI 2026/1130) using the savings for an otherwise eligible first home above £450,000 costs a 20% withdrawal charge instead of 25%; other unauthorised withdrawals stay at 25%. ANNOUNCED, not yet legislated: a First Time Buyer ISA replaces the Lifetime ISA for new savers from April 2029 (25% government bonus "on the final account balance up to a maximum of £20,000", first home worth up to £450,000); existing Lifetime ISA holders keep the current rules (2026 data, sources [gov.uk Lifetime ISA](https://www.gov.uk/lifetime-isa) + [legislation.gov.uk SI 2026/1130](https://www.legislation.gov.uk/uksi/2026/1130/made) + [HMRC Lifetime ISA withdrawal guidance](https://www.gov.uk/guidance/lifetime-isa-withdrawal-charges-and-charge-free-withdrawals) + [Budget 2026 OOTLAR 2.3–2.4](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar); tracked in shared/regulatory-watch.md 🇬🇧 UK)
- **ECO4** (Energy Company Obligation, Great Britain): low-income energy-efficiency upgrades through energy suppliers; runs until **31 Dec 2026** after a nine-month extension (2026-10-28 verified; source [Ofgem](https://www.ofgem.gov.uk/environmental-and-social-schemes/energy-company-obligation-eco))
- **Boiler Upgrade Scheme** (England and Wales): £7,500 towards an air-source or ground-source heat pump, £5,000 biomass boiler, £2,500 air-to-air heat pump; an extra £1,500 until March 2027 for oil/LPG-heated homes with no mains gas (2026-10-28 verified; source [gov.uk](https://www.gov.uk/apply-boiler-upgrade-scheme))
- **GBIS** (Great British Insulation Scheme): **ENDED 31 Mar 2026** (2026-10-28 verified; source [Ofgem](https://www.ofgem.gov.uk/environmental-and-social-schemes/great-british-insulation-scheme))

## Common listing platforms

- **Rightmove** — self-described "UK's number one property portal" (Rightmove plc); sold prices from HM Land Registry / Registers of Scotland
- **Zoopla** — sold-price history from HM Land Registry data + Zoopla house-price estimates
- **OnTheMarket** — alternative
- **PrimeLocation** — high-end
- **PropertyData** — paid analytics

## Caveats unique to UK

- **Leasehold trap** (flats + some new houses) — a lease of 80 years or less brings marriage value into the extension premium (LRHUDA 1993 Sch 13 para 4(2A)) and cuts value; ground rent doubling clauses scandals
- **Cladding crisis** (post-Grenfell): lenders can ask for an EWS1 form on a block of any height (RICS standard from 1 Nov 2026; it is not a fire safety certificate); remediation ongoing — see `--risks`; some flats remain hard to sell or mortgage
- **RAAC concrete** (1960s–1980s) — major scandal 2023-2024 in schools, hospitals, some residential
- **Japanese knotweed** — disclosed by the seller on the TA6 form (q.8.6–8.7), not recorded by HM Land Registry; lenders may want a treatment plan; treatment 5-yr programme (est.)
- **SDLT additional dwelling 5% surcharge** (since Oct 2024) — punitive on BTL
- **FHL abolition April 2025** — major change for short-let economics
- **Council Tax based on 1991 values** in England/Scotland, 2003 values in Wales — wildly outdated; the Welsh revaluation legislated for 2028 (then every 5 years) is to be deferred to the next Senedd term (announced 20 Oct 2026, not yet law; no new year given) and Scotland plans two bands above £1M from April 2028 (not yet legislated) — see `--tax` Future risk
- **Empty/second home premium**: England up to +100% on homes empty 1 year+ (since April 2024; up to +300% after 10 years) and on second homes (since April 2025); Wales up to +300% since April 2023
- **Renters' Rights Act 2025** — Section 21 abolished (1 May 2026)
- **Help to Buy ended** (England, 2023) — successor **Your First Home** equity loan confirmed at Budget 2026 (28 Oct 2026) but applications not open until Feb 2027 (pre-registration by end-Dec 2026, first sales Apr 2027); the local price-cap list and full eligibility rules are not yet published — do not price it into an offer until they are (see Active fiscal incentives)
- **Northern Ireland** uses domestic rate system (capital value-based) — distinct from rest of UK
- **Scotland LBTT + ADS 8%** — punitive on additional dwelling
- **Non-UK-resident SDLT surcharge 2%** (England / NI, since 1 Apr 2021) — for an individual it turns on days spent in the UK (at least 183 in the 12 months before purchase), not nationality, so EU and non-EU buyers are treated alike

## Reddit / forum sources

- **r/HousingUK** — general housing discussion
- **r/UKPersonalFinance** — mortgage + tax
- **r/AskUK**, **r/unitedkingdom**
- **MoneySavingExpert forum** (Martin Lewis)
- **PropertyTribes** (BTL-focused)

## Verification authorities

| Authority | When to call |
|---|---|
| **HM Land Registry** | Title verification, title plan |
| **Local council planning** | Permits, planning history, listed building |
| **Local council building control** | Building regs compliance |
| **Local council Council Tax** | Band, exemptions |
| **Water company** | Mains drains, sewer maps |
| **Environment Agency** | Flood, environmental |
| **Mining Remediation Authority** (the Coal Authority until 28 Nov 2024) | Mining search |
| **HMRC** | SDLT, CGT, FHL transition |

## Source URL templates

| Source | URL pattern |
|---|---|
| Land Registry PPD | `https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads` |
| Find Title | `https://search-property-information.service.gov.uk/` |
| Council Tax bands | `https://www.gov.uk/council-tax-bands` |
| Long-term flood risk | `https://check-long-term-flood-risk.service.gov.uk` |
| SEPA flood maps (Scotland) | `https://map.sepa.org.uk/floodmaps` |
| NRW Flood Risk Assessment Wales map | `https://naturalresources.wales/flooding/check-your-flood-risk-on-a-map-flood-risk-assessment-wales-map/?lang=en` |
| Flood Maps NI (DfI) | `https://www.infrastructure-ni.gov.uk/topics/flood-maps-ni` |
| EPC register (England + Wales) | `https://www.gov.uk/find-energy-certificate` (the old service address redirects here, 2026-10-28) |
| Mining Remediation Authority (ex-Coal Authority) property check | `https://www.gov.uk/check-if-property-is-affected-by-coal-mining` |
| UK Radon | `https://www.ukradon.org` |
| BGS Geology Viewer | `https://www.bgs.ac.uk/map-viewers/bgs-geology-viewer/` |
| HSE COMAH establishments search | `https://www.hse.gov.uk/comah/comah-establishments.htm` |
| Ofgem price cap rates by region | `https://www.ofgem.gov.uk/your-energy-supply/your-energy-bill/energy-price-cap-unit-rates-and-standing-charges` |
| CCW Find your water company | `https://www.ccw.org.uk/advice-and-support/households/water-companies/` |
| Police crime map | `https://www.police.uk/` (blocks automated checks; open data at `https://data.police.uk/`, latest month August 2026 per its API on 2026-10-28) |
| ONS Crime in England and Wales | `https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/bulletins/crimeinenglandandwales/latest` |
| Ofcom broadband checker | `https://checker.ofcom.org.uk/en-gb/broadband-coverage` |
| DfT traffic counts | `https://roadtraffic.dft.gov.uk` |
| Companies House | `https://www.gov.uk/government/organisations/companies-house` |
| HMRC SDLT | `https://www.gov.uk/stamp-duty-land-tax` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged). Later re-checks (regwatch waves of 2026-09-24, 2026-10-21 and 2026-10-28, see shared/regulatory-watch.md; Tier-A refresh of 2026-10-28) are listed per section below and in the Update history; the date stays because `--price`, `--tax`, `--risks` and `--mains` still carry est. or unverified figures.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for the transaction taxes — SDLT 2025 rates, surcharges and first-time buyer relief, LBTT with the 8% ADS and the Welsh LTT main and higher-rate tables (gov.uk, Budget 2026 Annex A, Revenue Scotland, Welsh Revenue Authority), HIGH for 2026-27 Council Tax averages and premiums and the NI rate poundages (MHCLG, Welsh and Scottish Governments, Finance NI), HIGH for the `--price` benchmark table and rents (UK HPI August 2026, HM Land Registry / ONS release of 21 Oct 2026; ONS PIPR), HIGH for `--work` (2026-27 NI, Corporation Tax, VAT and personal-allowance figures on gov.uk and legislation.gov.uk; ONS ASHE 2026), HIGH for FHL abolition (HMRC TIIN and clarification), HIGH for Renters' Rights Act 2025 (in force; s21 abolished 1 May 2026) and the short-let rules of the four nations (legislation.gov.uk, gov.scot, gov.wales, Tourism NI), HIGH for the flood-map sources, NaFRA flood counts and UKCP18 projections (EA, SEPA, NRW, DfI, Met Office), the cladding remediation data (MHCLG, end-Sep 2026), the RAAC note (RSH letter, 7 Sep 2023) and the Ofgem cap for 1 Oct–31 Dec 2026; MEDIUM for HVCTS implementation detail (announced Autumn Budget 2025; government response published at Budget 2026, 28 Oct 2026 — not yet legislated, Finance Bill 2026-27 pending), the 24% / 44% / 49% property income rates from 6 Apr 2027 (announced at Budget 2026, not yet law), MEES EPC C by 2030 (proposed, not yet law), the leasehold-reform timetable (LAFRA 2024 valuation reforms not commenced; Commonhold and Leasehold Reform Bill not introduced at the 2026-10-21 re-check) and the later phased Renters’ Rights commencements (MHCLG roadmap); MEDIUM for Your First Home parameters (confirmed at Budget 2026 on gov.uk; applications not open until Feb 2027 — local price-cap list and full eligibility rules not yet published); MEDIUM for the rest of `--risks` and `--mains` (radon, coalfield, clay-soil and tidal-estuary region lists, knotweed effect on lending, five build-era rows and the searches / CWI rows not re-verified; no water-bill figure, as the Ofwat and Water UK pages could not be read); LOW for the est. £/m² ranges (UNVERIFIED), the leasehold value hit (est. 10–30%) and 60-year mortgage floor, the conveyancing, search, survey and broker fee ranges and the transaction-cost totals computed from them, and the CON29DW, mains and works cost rows (est., no primary price source).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: benchmark table rebuilt from UK HPI Aug 2026 (HM Land Registry / ONS, 21 Oct 2026; NI Q2 2026), ONS PIPR rents, PPD scope and title-copy fees; high-LTI note re-checked 2026-10-28 (regwatch, PRA PS19/26); est. £/m² ranges UNVERIFIED, leasehold value-hit and 60-year figures est., GIA and the pre-2017 ground-rent cut-off not checked, Registers of Scotland unreadable (403) |
| `--traffic` | 2026-10-28 | 2026-10-28 Tier-A refresh | DfT AADF coverage, TfL open data and OSM road classes re-read; NI DfI census report updated to the 2023 edition (found 2026-10-29); verdict bands are skill thresholds, not source data |
| `--tax` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: 2026-27 Council Tax averages, premiums and NI poundages, SDLT, LBTT / ADS, LTT main and higher-rate tables, HM Land Registry fee scale, CGT / IHT, VAT and Council Tax revaluation; HVCTS and the stamp-duty Budget note re-checked 2026-10-28 (regwatch); leasehold-reform line last re-checked 2026-10-21 (regwatch); conveyancing, search, survey and broker ranges stay est., so the computed totals are est.; the prior 28% CGT rate not re-read |
| `--rental` | 2026-10-28 | 2026-10-28 Tier-A refresh | Tenancy types per nation, deposit schemes, FHL reliefs, short-let rules (London, Scotland, Wales register and licensing Act 2026, NI), ATED and holiday-let VAT re-verified; property income rates and finance-cost relief re-checked 2026-10-28, Renters' Rights and MEES lines 2026-10-21 (regwatch); the section holds no rent or yield figures (rents are under `--price`) |
| `--work` | 2026-10-28 | 2026-10-28 Tier-A refresh | 2026-27 Class 2 / Class 4 NI, Corporation Tax, VAT thresholds and personal allowance (gov.uk, legislation.gov.uk, Budget 2026 Annex A); ONS ASHE 2026 salary benchmark added; job boards checked live |
| `--risks` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: flood and hazard source table (EA, SEPA, NRW, DfI, Mining Remediation Authority, HSE), NaFRA counts, drought years, coastal erosion, radon map facts, knotweed disclosure, storms, RAAC, cladding data, EPC, TA forms, EWS1 and MEES; radon, coalfield, clay-soil and tidal region lists, knotweed effect on lending, five build-era rows and the searches / CWI rows not re-verified |
| Climate projections (UKCP18, in `--risks`) | 2026-10-28 | 2026-10-28 Tier-A refresh | Warming, sea-level and hot-summer figures from UKCP18 Headline Findings v4.0; 40.3 °C record confirmed (Met Office); NaFRA mid-century flood projection |
| `--mains` | 2026-10-28 | 2026-10-28 Tier-A refresh | Partly re-verified: General Binding Rules and permit limits (gov.uk), water-company list (CCW), Ofgem cap for 1 Oct–31 Dec 2026 added; no water-bill figure (Ofwat and Water UK unreadable); CON29DW price, the urban-mains line and the four cost rows stay est. or not re-verified |
| Active fiscal incentives | 2026-10-28 | 2026-10-28 Tier-A refresh | ECO4 end date, BUS grants and GBIS closure (Ofgem, gov.uk); Your First Home, Help to Buy – Wales and Lifetime ISA re-checked 2026-10-28 against Budget 2026 publications and SI 2026/1130 (regwatch); First Homes last re-checked 2026-10-21 (regwatch) |
| Common listing platforms | 2026-10-28 | 2026-10-28 Tier-A refresh | Rightmove (own claim), Zoopla, OnTheMarket and PropertyData live; PrimeLocation "high-end" positioning not verified (site returns 403) |
| Caveats unique to UK | 2026-10-28 | 2026-10-28 Tier-A refresh | Legal / fiscal lines only; premium dates, the 1991 / 2003 base years (with the 2028 Welsh and Scottish reforms) and the non-resident surcharge corrected; leasehold, cladding, RAAC and knotweed caveats not checked — the cladding and knotweed lines still carry wording `--risks` has since corrected |
| Source URL templates | 2026-10-28 | 2026-10-28 Tier-A refresh | 11 rows checked, 3 changed (EPC register, Mining Remediation Authority, BGS Geology Viewer); 10 rows added; police.uk and Find Title block automated checks |

## Extension TODOs

- [ ] Per-council Council Tax band rates (96k entries)
- [ ] Per-council short-let licensing rules table
- [ ] Mortgage product trade-offs (FTB / mover / BTL / portfolio)
- [ ] Conveyancing search interpretation guide
- [ ] Leasehold reform timeline implementation tracker
- [ ] EWS1 cladding remediation status by building
- [ ] RAAC affected building register (where public)
- [ ] Section 21 abolition transition rules
- [ ] Northern Ireland rates calculator
- [ ] Scotland LBTT scenarios + ADS rules
- [ ] Wales LTT scenarios

## Update history

- **2026-04-25** — Initial population
- **2026-05-27** — Tier-1 corrections: empty- and second-home Council Tax premiums, residential CGT higher rate 28% → 24% from 6 Apr 2024, FA 2025 non-dom abolition and the IHT long-term-residence test, Renters' Rights Act 2025 (Royal Assent 27 Oct 2025)
- **2026-05-29** — Anti-hallucination sweep: est. labels on the price benchmarks, Council Tax bill ranges, conveyancing fees and cost tables
- **2026-06-04** — Council Tax premiums and Renters' Rights Act source URLs re-pointed
- **2026-07-03** — Tier-A quarterly refresh, playbook re-stamped 2026-07-03: ONS bulletin rename, HVCTS added, LAFRA 2024 commencement status and the draft Commonhold and Leasehold Reform Bill, Renters' Rights commencement, MEES EPC C by 2030, property income rates from 6 Apr 2027
- **2026-09-24** — October and November regwatch waves (November run early): leasehold, rental and tax tracker entries re-checked
- **2026-10-21** — December regwatch wave (run early): leasehold, rental and tax tracker entries re-checked; Active fiscal incentives (Your First Home, Help to Buy – Wales, First Homes) and the Bank of England / PRA high-LTI note re-checked
- **2026-10-23** — 21 Oct 2026 audit applied: Bank of England / PRA high-LTI note and Your First Home (announced 26 Sep 2026) added, Help to Buy – Wales and First Homes rewritten; property income rates and finance-cost relief marked ENACTED (FA 2026 s.6–7, Sch 1 para 40)
- **2026-10-28** — Budget 2026 regwatch waves: Your First Home, Help to Buy – Wales, HVCTS and the high-LTI note re-checked (Budget 2026 publications, PRA Rulebook); property income rates (a further 2pp to 24% / 44% / 49% from 6 Apr 2027, announced), finance-cost relief and the stamp-duty future-risk note re-checked (OOTLAR, Annex A, policy costings); Lifetime ISA bullet added (SI 2026/1130)
- **2026-10-29** — Tier-A refresh (market, tax-legal, risk-infra; sources read 2026-10-28, corrections re-checked 2026-10-29); playbook-level date not re-stamped because `--price`, `--tax`, `--risks` and `--mains` are not fully re-verified
  - Re-verified (facts checked — changed / confirmed / unverifiable): `--work` 17 — 5 / 12 / 0, plus an ASHE bullet added; `--traffic` 10 — 4 / 2 / 4 (the 4 are skill verdict bands); `--rental` legal rules 16 — 9 / 7 / 0; climate projections (in `--risks`) 5 — 4 / 1 / 0; Active fiscal incentives (ECO4, BUS, GBIS) 3 — 2 / 1 / 0; Caveats unique to UK 7 — 3 / 4 / 0 (legal / fiscal only); Source URL templates 11 — 3 / 8 / 0, plus 10 rows added
  - Refreshed, not re-verified: `--price` 38 — 24 / 8 / 6; Common listing platforms 5 — 2 / 2 / 1; `--tax` 72 — 22 / 44 / 6 (incl. the Cost benchmarks transaction rows); `--risks` excl. climate 50 — 22 / 15 / 13; `--mains` 12 — 4 / 2 / 6
  - Totals: 246 facts checked — 104 changed / 106 confirmed / 36 unverifiable
  - Main changes: UK HPI August 2026 price table replaces the unsourced est. ranges (est. £/m² kept, labelled UNVERIFIED); ONS PIPR rents and ASHE 2026 earnings added; Class 2 NI and the personal-allowance freeze (through 2030-31) corrected; AADT → AADF; 2026-27 Council Tax averages (England Band D £2,392) and NI poundages; Welsh LTT higher rates shown as their own table, not a +5% surcharge; Multiple Dwellings Relief abolished from 1 Jun 2024; HM Land Registry fee scale to £1,105 and transaction-cost totals recomputed (mover £300k–£500k ~2.2–4.1%, was 3–5%); assured periodic tenancies replaced ASTs on 1 May 2026; London 90-night rule sourced to the Deregulation Act 2015 s.44; Wales visitor-accommodation register by 31 Mar 2027 and licensing Act 2026 (not in force); Coal Authority → Mining Remediation Authority; EWS1 RICS 2nd edition (effective 1 Nov 2026); UKCP18 figures re-sourced to the v4.0 Headline Findings; septic-tank General Binding Rules corrected; Ofgem cap for Oct–Dec 2026 added
