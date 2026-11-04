# Canada 🇨🇦 — Property Due-Diligence Playbook

ISO2: `ca`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: `A1A 1A1` (alphanumeric, 6 chars, space)
- **Admin levels**: 10 provinces + 3 territories; municipalities below
- **Currency**: **CAD** (Canadian dollar); 1 EUR = 1.5719 CAD, 1 USD = 1.4021 CAD (Bank of Canada daily rate, 22 Oct 2026; FX moves daily, convert at the current rate) (2026 data, source [Bank of Canada — daily exchange rates](https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/))
- **Languages**: English (official) + French (official); Quebec French-majority
- **Cadastre**: **fragmented by province** — no national portal
  - **Ontario**: Teranet OnLand `https://www.onland.ca` + ServiceOntario LRO
  - **British Columbia**: LTSA `https://ltsa.ca` + LOTR (free beneficial-owner search since Apr 2024)
  - **Alberta**: SPIN2 `https://spin.alt.alberta.ca`
  - **Quebec**: Registre foncier `https://www.registrefoncier.gouv.qc.ca` (only true cadastre system)
- **Identifier**:
  - ON: PIN (9 digits)
  - BC: PID (9 digits XXX-XXX-XXX)
  - AB: Linc (10 digits)
  - QC: cadastre lot number
- **Ownership types**:
  - **Freehold** — most houses
  - **Condo** (most provinces) / **Strata** (BC) / **Co-op** (rare ON/QC)
  - **Leasehold** — 99-year on Indigenous land (e.g., Musqueam, Squamish/Tsleil-Waututh leasehold lands, Vancouver)
- **Federal foreign-buyer ban**: extended to **1 Jan 2027** (Prohibition on the Purchase of Residential Property by Non-Canadians Act)

## Section: `--price`

### Primary sources

- **CREA MLS Home Price Index (HPI)**: `https://www.crea.ca/housing-market-stats/mls-home-price-index/` — national + regional benchmark
- **Teranet-NBC HPI**: `https://housepriceindex.ca` — repeat-sales index, monthly public release (2026 data, source [Teranet–National Bank methodology](https://housepriceindex.ca/about/our-methodology/))
- **CMHC Housing Market Information Portal**: `https://www03.cmhc-schl.gc.ca/hmip-pimh/`
- **Statistics Canada (StatCan)**: `https://www.statcan.gc.ca/en/subjects-start/housing` — house price index + rental
- **Provincial price boards**:
  - Toronto: TRREB `https://trreb.ca` (Toronto Regional Real Estate Board)
  - Vancouver: **Greater Vancouver REALTORS® (GVR)** — formerly the Real Estate Board of Greater Vancouver (REBGV) — `https://www.gvrealtors.ca/` (monthly benchmark price / HPI package under market intelligence) (2026 data, source GVR; 2026-09-18 verified)
  - Calgary: CREB `https://www.creb.com`
  - Montreal: QPAREB / APCIQ (Quebec Professional Association of Real Estate Brokers; Centris data) `https://apciq.ca` (2026 data, source [apciq.ca/en](https://apciq.ca/en/))

### Listing platforms

- **Realtor.ca** — CREA's consumer listing site, run since Jan 2025 by REALTOR.ca Canada Inc., a wholly owned CREA subsidiary (2026 data, source [CREA — REALTOR.ca for Canadians](https://www.crea.ca/technology/realtor-ca-for-canadians/)); share of MLS® listings it carries: data not publicly available — verify at [CREA](https://www.crea.ca/): `https://www.realtor.ca`
- **Centris.ca** — Quebec only (QPAREB): `https://www.centris.ca`
- **Royal LePage**, **RE/MAX**, **Zolo** — agency networks

### 2026 price benchmarks (September 2026 board data; Montreal Q3 2026)

| Region | Benchmark / price (CAD) | YoY change | Source (2026 data) |
|---|---:|---:|---|
| **National composite** | $651,400 (Composite MLS® HPI benchmark) / $666,538 (avg); both not seasonally adjusted | -3.4% (HPI) / -1.6% (avg) | [CREA release, 16 Oct 2026](https://creastats.crea.ca/en-CA/) + [CREA MLS® HPI data, Oct 2026 release (zip: Not Seasonally Adjusted (M).xlsx, sheet AGGREGATE)](https://assets.ctfassets.net/gm6df3h7p862/0UIFBeTwRyEBUSyDl4IcO/0a3e0152751219f93b4fcaa398480e5b/MLS_HPI_Oct_2026.zip) |
| **Toronto (TRREB, all areas)** | $917,600 (HPI composite) / $1,006,409 (avg) | -4.65% (HPI) / -5.1% (avg) | [TRREB MLS HPI tables, Sep 2026](https://trreb.ca/wp-content/files/market-stats/home-price-index/TRREB_MLS_HPI_Public_Tables_0926.pdf) + [TRREB Market Watch](https://trreb.ca/market-data/market-watch/) |
| **Vancouver (Metro, GVR)** | $1,075,900 (HPI composite) | -5.5% | [GVR stats package, 2 Oct 2026](https://members.gvrealtors.ca/news/GVR-Stats-Package-September-2026.pdf) |
| **Calgary (city, CREB)** | $566,700 (total residential benchmark) / $646,198 (avg) | -0.82% (benchmark) / +4.9% (avg) | [CREB release, 1 Oct 2026](https://www.creb.com/News/Media_Releases/2026/October/September_2026_Stats) + [CREB Calgary monthly stats package, Sep 2026](https://www.creb.com/Housing_Statistics/documents/09_2026_Calgary_Monthly_Stats_Package.pdf) |
| **Montreal (CMA, QPAREB)** | $645,500 (single-family median, Q3) / $435,000 (condo median, Q3) | +2% / +2% | [QPAREB Q3 release, 14 Oct 2026](https://apciq.ca/en/quebecs-residential-real-estate-market-continues-to-transition-yet-most-markets-remain-seller-friendly) (Centris data) |
| **Ottawa (OREB)** | $623,500 (HPI composite) / $685,640 (avg) | -0.3% (HPI) / -1.0% (avg) | [CREA stats — Ottawa board, Sep 2026](https://creastats.crea.ca/board/otta) |
| **Halifax-Dartmouth (NSAR)** | $541,700 (HPI composite, CREA's Halifax-Dartmouth series) / $585,650 (avg) | -4.1% (HPI, computed: $541,700 / $565,100 in Sep 2025) / +0.4% (avg) | [CREA MLS® HPI data, Oct 2026 release (zip: Not Seasonally Adjusted (M).xlsx, sheet HALIFAX_DARTMOUTH)](https://assets.ctfassets.net/gm6df3h7p862/0UIFBeTwRyEBUSyDl4IcO/0a3e0152751219f93b4fcaa398480e5b/MLS_HPI_Oct_2026.zip) + [NSAR MLS Statistical Report, Sep 2026](https://www.nsrealtors.ca/common/Uploaded%20files/NSAR%20PDF%20document/Web%20-%20Public/Stats/stats0926.pdf) |
| **Edmonton (RAE)** | $423,100 (HPI composite) / $466,080 (avg) | -0.3% (HPI) / +2.9% (avg) | [CREA stats — Edmonton board, Sep 2026](https://creastats.crea.ca/board/edmo) |
| **Winnipeg (WRREB)** | $467,687 (detached avg, YTD) / $288,751 (condo avg, YTD); HPI not shown on the board page | +3% / +2% (YTD) | [CREA stats — Winnipeg board, YTD to Sep 2026](https://creastats.crea.ca/board/winn) |

### Compute

1. CAD/sq ft = price / **square footage** (sq ft is the customary listing unit, not m²: a listing-platform convention, no official statistic found; Alberta's regulator has licensees report RMS size in square metres or square feet, source [RECA — Guide to the Residential Measurement Standard](https://www.reca.ca/wp-content/uploads/Residential-Measurement-Standard-Licensee-Guide-1-2.pdf), Fifth Edition, January 2024 — rates/figures may have changed since)
2. Cross-check **Realtor.ca** sold-price history + Teranet for closed sales
3. **HPI vs average**: HPI strips out luxury/distressed; average runs above HPI. Computed from the Sep 2026 table above: TRREB +9.7% ($1,006,409 / $917,600), Ottawa +10.0% ($685,640 / $623,500), Edmonton +10.2% ($466,080 / $423,100), Calgary +14.0% ($646,198 / $566,700), Halifax-Dartmouth +8.1% ($585,650 / $541,700), national +2.3% ($666,538 / $651,400). The gap moves with each market's sales mix, so compute it from the target board's own HPI and average instead of applying a fixed range
4. **Convert CAD to EUR/USD** at current FX

### Key terms

- PIN/PID/Linc = title identifier per province
- Strata (BC) = condo/townhouse with shared common property
- Co-op = corporate ownership, individual occupancy rights (rare)
- HPI = MLS Home Price Index (CREA)

---

## Section: `--traffic`

### Sources

- **Transport Canada national highway system**: `https://tc.canada.ca/`
- **Provincial DOT traffic counts**:
  - Ontario: **MTO Traffic Volumes** (AADT / SADT / SAWDT / WADT) — CSV 1988–2024 + 2024 AADT "Data on Demand" `https://www.library.mto.gov.on.ca/SydneyPLUS/TechPubs/Portal/tp/tvSplash.aspx` (2024 data, source MTO Technical Publications) — rates/figures may have changed since; the Ontario Data Catalogue "Traffic volume" dataset `https://data.ontario.ca/dataset/traffic-volume` stops at 2010 (last updated 2015-04-30)
  - BC: **Ministry of Transportation and Transit — Traffic Data Program** (interactive Traffic Data Map) `https://www.th.gov.bc.ca/trafficData/`; **DriveBC** `https://www.drivebc.ca/` shows real-time conditions, closures, webcams and delays, not counts
  - Alberta: **Highway traffic counts** — AADT + ASDT (May–Sep) from ~390 permanent automated traffic recorder sites, updated yearly by end of March `https://www.alberta.ca/highway-traffic-counts` (2026 data, source alberta.ca)
  - Quebec: **MTMD (ex-MTQ) Débit de circulation** — DJMA (= AADT), DJME (summer), DJMH (winter) estimated from 4,500+ collection sites `https://www.donneesquebec.ca/recherche/dataset/debit-de-circulation` (dataset updated 2026-10-17)
- **City open-data portals**: Toronto, Vancouver, Calgary all have AADT layers

### Key term

**AADT (Annual Average Daily Traffic)** — same as US/UK.

### Verdict bands

- 🟢 < 1,500 v/d (residential, suburban side streets)
- 🟡 1,500–10,000 v/d (urban arterial, suburban collector)
- 🟠 10,000–35,000 v/d (regional highway, urban core)
- 🔴 > 35,000 v/d (highway 401, ring roads, major arterials)

---

## Section: `--tax`

### Annual property tax — Provincial / Municipal

Property tax = **mill rate × assessed value** (assessed by MPAC in ON, BC Assessment in BC, and municipal assessors in AB, e.g. City of Calgary / City of Edmonton).

Residential rates are set annually by each municipality. Toronto, Vancouver, Calgary, Halifax and Edmonton rows show published 2026 rates; the Montreal row is computed from the city's 2026 billing open data for all 19 boroughs; the Ottawa row is an est. from draft-budget figures (verify the current year on the municipal tax bill / city budget):

| Province / City | Residential rate | Assessment basis |
|---|---:|---|
| Toronto | 0.767% total = 0.605% city + 0.009% City Building Fund + 0.153% education (2026 data, source toronto.ca property tax rates) | MPAC — 2026 taxes still use 1 Jan 2016 current values (province-wide reassessment postponed; source mpac.ca) |
| Vancouver (City) | 0.336% total ($3.36394 per $1,000, incl. $0.98001 provincial school tax) (2026 data, source vancouver.ca residential rates; City council report 28 Apr 2026, Appendix A) | BC Assessment annual (2026 roll = market value at 1 Jul 2025) |
| Calgary | 0.665% total = 0.389% city + 0.276% provincial (2026 data, source calgary.ca, Property Tax Bylaw 9M2026) | Annual (City of Calgary assessment) |
| Montreal | 0.623–0.740% municipal (residential, 5 dwellings or fewer), computed for all 19 boroughs from each borough's most common rate stack = city-wide 0.4631% general + 0.0831% water + 0.0070% ARTM + 0.0024% roads, plus borough services and investment taxes and the former-city debt tax; e.g. Ville-Marie 0.623% (lowest), Outremont 0.634%, Plateau-Mont-Royal 0.651%, Rosemont–La Petite-Patrie 0.659%, Rivière-des-Prairies–Pointe-aux-Trembles 0.710%, Montréal-Nord 0.738%, Anjou 0.740% (highest) (2026 data, source [Ville de Montréal open data — Imposition annuelle de taxes municipales](https://donnees.montreal.ca/dataset/0a912de3-9307-4b63-bf19-3a4594f87e1f), first 2026 billing, published 2026-02-20); school tax billed separately (see below) | Triennial roll 2026-2028, value change phased in by thirds (source montreal.ca) |
| Ottawa | ~1.26% total, est. = ~1.107% municipal (computed: $4,593 2026 taxation ÷ $415,000 average urban-home assessment, [City of Ottawa Draft Budget 2026](https://documents.ottawa.ca/sites/default/files/FINAL%202026%20Budget%20Magazine%20English.pdf), Table 1, Nov 2025 draft-stage figures; the table's increases are city-wide, police and transit only, so education is taken as excluded) + the province-set education rate (0.153% in Toronto's 2026 breakdown above); adopted 2026 rate table not reachable — verify at ottawa.ca/taxes. Residential bills also carry a $267/yr solid-waste fee for curbside homes (2026 data, source [City of Ottawa 2026 final tax bill insert](https://documents.ottawa.ca/sites/default/files/26-048_Ottawa_Property-taxes_E-print_EN.pdf)) | MPAC (1 Jan 2016 current values; reassessment still postponed per the City's Draft Budget 2026) |
| Halifax | 1.113% urban, computed: $0.687 general + $0.015 supplementary education + $0.016 climate action + $0.095 local transit (within 1 km walk of a transit stop) + $0.300 provincial per $100 (2026/27 data, source halifax.ca); fire protection ($0.014, within 1,200 ft of a hydrant), right-of-way ($0.008, mapped area) and community area rates extra | PVSC annual |
| Edmonton | 1.036% total = 0.774% municipal + 0.254% education + 0.008% requisition allowance (2026 data, source edmonton.ca) | Annual (City of Edmonton assessment) |

**Education portion**: included in the sourced totals above (2026: Ontario 0.153%, Vancouver provincial school tax 0.098%, Calgary provincial 0.276%, Edmonton 0.254% + 0.008%, Halifax provincial $0.300 per $100 incl. $0.290 education); Quebec school tax is billed separately at one province-wide rate: $0.07899 per $100 of standardized value for 2026-2027 (was $0.08423 in 2025-2026), first $25,000 of taxable value exempt (2026 data, source [Centre de services scolaire des Hautes-Rivières, 2 Jul 2026](https://www.cssdhr.gouv.qc.ca/wp-content/uploads/2026/07/2026-07-02_Comm_Pres_Taxe_Scol.pdf)); other municipalities — verify on the municipal tax bill.

### Transaction taxes (LTT — Land Transfer Tax)

#### Ontario LTT

Tiered 0.5% to 2.5% — provincial:
- Up to $55,000: 0.5%
- $55-250k: 1.0%
- $250-400k: 1.5%
- $400k-$2M: 2.0%
- > $2M: 2.5% — only on land with one or two single-family residences (2026 data, source [ontario.ca — calculating LTT](https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax), updated 2026-04-22)

**Toronto Municipal LTT (MLTT)**: graduated rates with **new high-value tier from 1 Apr 2026** (amendment passed by City Council on 17 Dec 2025): **4.4%** ($3M–$4M), **5.45%** ($4M–$5M), **6.5%** ($5M–$10M), **7.55%** ($10M–$20M), **8.6%** (>$20M) — properties with one or two single-family residences only (all other residential stays at 0.5–2.0%), on top of base 0.5–2.5%; MLTT administration fee $102.56 + HST per transaction (2026-11-03 verified, source: [toronto.ca — MLTT rates](https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/), modified 2026-04-07).

**FTB rebate**: up to $4,000 ON (LTT refund, transactions from 1 Jan 2017; source ontario.ca, updated 2026-02-10) + $4,475 Toronto (MLTT rebate; source toronto.ca, modified 2025-12-18).

**Foreign buyers (ON)**: provincial **Non-Resident Speculation Tax 25%** since 25 Oct 2022, province-wide, on residential land with 1–6 single-family residences (houses, condo units, duplex to sixplex), charged on the full price if any transferee is a foreign national, foreign corporation or taxable trustee (2026 data, source [ontario.ca — NRST](https://www.ontario.ca/document/non-resident-speculation-tax), updated 2026-05-04). **Toronto adds a Municipal NRST of 10%** of the purchase price on certain residential properties from 1 Jan 2025, on top of MLTT, with no grandfathering of earlier agreements (2026 data, source toronto.ca MLTT & MNRST pages).

#### BC Property Transfer Tax (PTT)

Tiered:
- Up to $200k: 1%
- $200k–$2M: 2%
- $2M+: 3%
- **+2% over $3M** (additional, residential portion only) (2026 data, source [gov.bc.ca — Property transfer tax](https://www2.gov.bc.ca/gov/content/taxes/property-taxes/property-transfer-tax), updated 2025-12-03)
- **Foreign buyer Additional Property Transfer Tax: 20%** in the specified Regional Districts: Capital (CRD), Fraser Valley, Metro Vancouver, Central Okanagan, Nanaimo, on the foreign national's, foreign corporation's or taxable trustee's proportionate share of fair market value; not on Tsawwassen First Nation treaty lands (2026-11-03 verified, source: [gov.bc.ca — Additional Property Transfer Tax](https://www2.gov.bc.ca/gov/content/taxes/property-taxes/property-transfer-tax/additional-property-transfer-tax), page last updated 2025-06-20)

#### Alberta — Land Title Transfer Fee

$50 + $5 per $5,000 (or portion) of value for a transfer of land; a mortgage registration is also $50 + $5 per $5,000 of principal (2026 data, source Service Alberta Land Titles common documents fee schedule, 1 Oct 2026). Computed example: $500,000 transfer = $50 + 100 × $5 = $550 (very low compared to ON/BC).

#### Quebec — Welcome Tax / Droit de mutation

Provincial scale (2026, indexed yearly): 0.5% to $62,900, 1% $62,900–$315,000, 1.5% above; a municipality may set a higher rate on the part above $500,000, capped at 3% except for Montréal (2026 data, source LégisQuébec D-15.1 s. 2). **Montréal 2026**: 0.5% to $62,900 / 1% to $315,000 / 1.5% to $552,300 / 2% to $1,104,700 / 2.5% to $2,136,500 / 3.5% to $3,113,000 / 4% above (2026 data, source montreal.ca — calcul des droits sur les mutations immobilières, updated 2026-01-12).

### Other taxes

- **Federal GST 5%** on new builds; HST provinces charge the harmonized rate instead — **13% ON, 14% NS** (cut from 15% on 1 Apr 2025), **15% NB / NL / PE**; BC is not an HST province (GST 5% applies; BC's 7% PST is a separate provincial sales tax) (2026 data, source CRA GST/HST rates page, last modified 2025-04-01)
- **Underused Housing Tax (UHT)**: **ELIMINATED for 2025 and later calendar years** by Bill C-15, Budget 2025 Implementation Act, No. 1 (S.C. 2026, c. 3, Royal Assent 26 Mar 2026): no tax payable and no return required for 2025+ (UHT Act ss. 1.1, 6.1); 2022-2024 returns and liabilities remain. Repeal of the UHT Act itself is enacted but not in force until 1 Jan 2035 (S.C. 2026, c. 3, s. 169) (sources: Justice Laws UHT Act, current to 2026-10-19, last amended 2026-03-26; Justice Laws S.C. 2026, c. 3; Finance Canada C-15 briefing binder)
- **BC Speculation & Vacancy Tax (SVT)**: **rates DOUBLED for 2026**:
  - Foreign owners + untaxed worldwide earners (incl. satellite families): **3%** (was 2%)
  - Canadian citizens / PRs who are not untaxed worldwide earners: **1%** (was 0.5%)
  - BC-resident credit raised $2k → $4k (offsets the tax on the first $400,000 of assessed value)
  - Declaration due 31 Mar of the following year; tax due in July (2025 tax was due 2 Jul 2026)
  - **2027+**: foreign / untaxed-worldwide-earner rate **4%** (Budget Measures Implementation Act, 2026, S.B.C. 2026, c. 5, Royal Assent 16 Apr 2026); $250 non-refundable late-declaration penalty from 1 Jan 2027 (sources: gov.bc.ca SVT tax rates page, updated 2026-07-03; gov.bc.ca Budget 2026 tax changes; BC 2025 Financial and Economic Review)
- **Vancouver Empty Homes Tax**: **3%** of assessed taxable value for the 2025 tax year, unchanged since the 2021 vacancy year (separate from BC SVT) (2025 reference year, source vancouver.ca Empty Homes Tax page, archived 2026-10-17: 3% of the 2025 assessed taxable value, declaration deadline 3 Feb 2026; City EHT annual report 2024 for the history; 2026 reference-year rate not shown — verify at vancouver.ca)
- **Toronto Vacant Home Tax**: **3%** of Current Value Assessment from the 2024 taxation year; declaration due 30 Apr (2026 data, source toronto.ca Vacant Home Tax, modified 2026-07-22)
- **Foreign buyer ban**: runs to **1 Jan 2027** — extension announced 4 Feb 2024 (CMHC) and enacted by S.C. 2024, c. 17, s. 149; the repeal (S.C. 2022, c. 10, s. 236) is still listed as not in force on Justice Laws (Act current to 2026-10-19). The Housing Minister confirmed a formal review of the post-2027 regime in Dec 2025 (secondary: MoneySense, 2 Oct 2026); Finance Minister Champagne said on 7 Oct 2026 "We're looking at all the options that we have in front of us" (news: [Global News, 7 Oct 2026](https://globalnews.ca/news/12091696/canada-foreign-home-buyer-ban-expiry/)); no extension, repeal or replacement located as tabled at 2026-11-03; Finance Canada set federal Budget 2026 for tabling on 5 Nov 2026 ([Finance Canada, 20 Oct 2026](https://www.canada.ca/en/department-finance/news/2026/10/government-of-canada-to-release-budget-2026-on-november-5-2026.html)) — flag as "in flux" and check Budget 2026 for any post-2027 measure

### Capital gains

- Federal: **50% inclusion rate** — a taxable capital gain is ½ of the gain (Income Tax Act s. 38(a), Justice Laws, Act current to 2026-10-19); the 2/3 inclusion proposal was **CANCELLED 21 Mar 2025** by PM Carney announcement (source: [PM news release](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase)). The $250,000 annual threshold, below which individuals' gains would have stayed at ½, existed only inside that proposal ([Finance Canada deferral release, 31 Jan 2025](https://www.canada.ca/en/department-finance/news/2025/01/government-of-canada-announces-deferral-in-implementation-of-change-to-capital-gains-inclusion-rate.html)), so it has no effect now that the hike is cancelled (2026-11-03 verified)
- Marginal rates (2026): federal 14% to 33%; provincial / territorial 4% (NU) to 21.8% (NL); Quebec rates are set by Revenu Québec (2026 data, source [CRA tax rates and income brackets](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html), modified 2026-06-25). Computed top combined rates: 54.8% NL (33% + 21.8%), 54% NS (33% + 21%), 53.5% BC (33% + 20.5%), 48% AB (33% + 15%) — Ontario surtax and the Quebec federal abatement not included (verify at canada.ca / revenuquebec.ca); with ½ inclusion, the tax on a capital gain is half the marginal rate (e.g. 26.75% at BC's top rate, computed)
- **Principal residence exemption** — full exemption for years owner-occupied
- **Non-residents**: only tax years in which the owner was resident in Canada count toward the principal residence exemption, and the "1 +" bonus year applies only if resident in Canada in the year of acquisition (dispositions on or after 3 Oct 2016) (source: CRA Income Tax Folio S1-F3-C2 ¶2.20, ¶2.50)
- **Non-resident disposition — Section 116 clearance**: when a non-resident DISPOSES of Canadian real property, the buyer is liable for **25% of the purchase price** (50% for depreciable taxable Canadian property such as a rental building, and for real property that is not capital property), reduced to the excess over the certificate limit once CRA issues a certificate of compliance (requested on Form T2062); the vendor must notify CRA no later than 10 days after the disposition (CRA recommends 30 days before a proposed one); CRA states no fixed processing time — certificates issue "at the earliest possible date" once documents and payment / security are validated, and appraisals "may take several months" (2026-10-23 verified, source: [CRA IC72-17R6 — Section 116](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html))

### Total transaction cost (buyer side)

Computed from the rates above; fees = lawyer / notary + title insurance + inspection from the Cost benchmarks est. rows ($2,100–$4,400, est.):

- ON resale $800k outside Toronto: ~1.8–2.1% (LTT $12,475 + fees)
- ON resale $800k in Toronto: ~3.4–3.7% (LTT $12,475 + MLTT $12,475 + fees)
- ON resale Toronto single-family, before fees: $3M ~4.1% (LTT $61,475 + MLTT $61,475); $5M ~5.4% ($111,475 + $159,975); $10M ~7.2% ($236,475 + $484,975)
- BC resale $1M: ~2.0–2.2% (PTT $18,000 + fees)
- BC foreign buyer in an APTT district: ~22% (PTT + 20% APTT; only where the buyer is exempt from the federal ban)
- ON foreign buyer: + 25% NRST (+10% MNRST in Toronto) on top of LTT
- AB: <1% (no LTT; $500k transfer fee $550 computed)

### Future risk

- Foreign buyer ban: the Act is repealed on 1 Jan 2027 unless Parliament acts; post-2027 regime under review, nothing located as tabled at 2026-11-03; federal Budget 2026 is due 5 Nov 2026 (see Other taxes above)
- BC SVT foreign / untaxed-worldwide-earner rate rises 3% → 4% for the 2027 tax year (enacted, S.B.C. 2026, c. 5)
- Federal capital-gains inclusion-rate 2/3 proposal **CANCELLED 21 Mar 2025** (no longer in policy pipeline)

---

## Section: `--rental`

### Long-term residential

- **Residential Tenancies Act** per province (RTA ON, RTB BC, RTDRS AB, Tribunal administratif du logement (TAL) QC — named Régie du logement until 31 Aug 2020, source [quebec.ca](https://www.quebec.ca/habitation-territoire/location/residences-privees-aines))
- **Rent control** (varies):
  - ON: units first occupied for residential purposes after 15 Nov 2018 exempt; others capped at the annual guideline (CPI-based, capped at 2.5%): **2.1% for 2026, 1.9% for 2027**; the guideline does not apply to the rent agreed with a new tenant on turnover (2026 data, source [ontario.ca — Rent increase guideline](https://www.ontario.ca/page/rent-increase-guideline))
  - BC: capped at the 12-month average BC CPI to July of the prior year: **2.3% for 2026, 2.2% for 2027** (effective 1 Jan 2027) (2026 data, source [BC Gov news release, 27 Aug 2026](https://news.gov.bc.ca/releases/2026HMA0085-000982))
  - AB: no limit on the amount of an increase; at most one increase per 365 days and none during a fixed term (2026 data, source [alberta.ca — During a tenancy](https://www.alberta.ca/during-a-tenancy))
  - QC: from 1 Jan 2026 the TAL rent-fixing criteria index rent to the 3-year average of Quebec all-items CPI, plus adjustments for tax / insurance increases above that base and for capital works (source [TAL — Augmentation de loyer](https://www.tal.gouv.qc.ca/fr/reconduction-du-bail-et-fixation-de-loyer/augmentation-de-loyer)); base **3.1%** for renewed leases starting 2 Apr 2026–1 Apr 2027 (2026 data, secondary: [Le Devoir](https://www.ledevoir.com/economie/949236/loyers-devraient-augmenter-moins-3-1-2026-selon-tal) reporting the TAL figure — verify on the TAL calculation tool)
- **Tenant protections strict** in ON/QC (tenant-favorable hearings)

### Short-let (Airbnb)

#### Vancouver

- **Principal-residence-only** (City of Vancouver Licence By-law No. 4450)
- BC provincial registry: registration number required on listings since **1 May 2025**; provincial fee **$100/yr** for a rental where the host lives, **$450/yr** where the host does not live (+$1.50 service fee) (2026 data, source [gov.bc.ca — Register as a host](https://www2.gov.bc.ca/gov/content/housing-tenancy/short-term-rentals/registry/host-registration))
- City of Vancouver STR business licence on top: **$77** application + **$1,108/yr** licence fee (2026 data, source [vancouver.ca — Short-term rental business licence](https://vancouver.ca/doing-business/short-term-rentals.aspx))
- City fines up to **$1,000 per offence**; provincial enforcement adds administrative monetary penalties, compliance orders and listing removal (no dollar amounts on the provincial page)

#### Toronto

- Principal residence only
- 180-night cap per calendar year on entire-unit rentals
- Registration / renewal **$390** for 2026 (subject to annual increase)
- Municipal Accommodation Tax **6%** on stays under 28 consecutive days
- Court fines up to **$100,000** or up to **$10,000/day**; ticketed offences up to $1,000 (2026 data, source [toronto.ca — Short-term rental operators/hosts](https://www.toronto.ca/community-people/housing-shelter/rental-housing-rights-information/short-term-rentals/short-term-rental-operators-hosts))

#### Quebec / Montreal

- **CITQ registration** mandatory; offers without a valid registration number are reported to Revenu Québec; Tourist Accommodation Regulation amendments phased in from spring 2026 and 1 Sep 2026 (2026 data, source [citq.qc.ca](https://citq.qc.ca/en))
- Numéro CITQ on listing required
- **Montreal — principal-residence rentals**: allowed only **10 June–10 September**, 31 days or less in total in that window, annual city operating permit; prohibited in Lachine, Saint-Laurent and Saint-Léonard; non-principal-residence STRs follow separate rules (check the borough) (2026 data, source [montreal.ca — Louer sa résidence principale à des touristes](https://montreal.ca/louer-sa-residence-principale-des-touristes))

### Tax on rental

- Rental income = federal+provincial marginal income tax
- Non-resident owners: **25% Part XIII withholding on gross rent**; with a CRA-approved Form NR6 the Canadian agent withholds 25% on net rent and the owner files a section 216 return (2026 data, source [CRA T4144](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4144/income-tax-guide-electing-under-section-216.html))
- Capital gains 50% inclusion at sale (the proposed 2/3 increase was cancelled — source [CRA — What's new for corporations](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/whats-new-corporations.html))
- Interest on money borrowed to buy or improve the rental property is deductible; interest on funds refinanced for personal use is not (source [CRA — Rental expenses you can deduct](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/rental-income/completing-form-t776-statement-real-estate-rentals/rental-expenses-you-deduct.html))

---

## Section: `--work=<profession>`

### Sources

- **Job Bank Canada**: `https://www.jobbank.gc.ca/`
- **Indeed.ca**, **LinkedIn CA**, **Glassdoor**, **Workopolis** (part of the Indeed site, per its footer; source workopolis.com, archived 2026-10-17), **Eluta**
- **Provincial workers' compensation boards**: WSIB ON `https://www.wsib.ca`, WorkSafeBC `https://www.worksafebc.com`; other provinces and territories via the Association of Workers' Compensation Boards of Canada `https://awcbc.org`

### Self-employment

- **Sole proprietorship**: register provincially (e.g., ServiceOntario)
- **Federal incorporation**: Corporations Canada (ISED); online incorporation **$200**, certificate within one business day (2026 data, source [ISED — Benefits of incorporating](https://ised-isde.canada.ca/site/corporations-canada/en/benefits-incorporating))
- **Provincial incorporation**: similar
- **GST/HST registration**: required once taxable supplies exceed **$30,000** in a single calendar quarter or over the last four consecutive calendar quarters (small-supplier threshold) (2026 data, source [CRA RC4022](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html))
- **Professional bodies**: per profession (CPA — the CA, CGA and CMA designations were unified under CPA; in BC the three legacy bodies were amalgamated into CPABC, source [CPABC legacy page](https://www.bccpa.ca/legacy/); MD, P.Eng, etc.)

### Salary benchmarks

- Median employment income, people aged 25–54 with employment income, by census metropolitan area (2024 data, 2024 constant dollars, source [StatCan Table 11-10-0239-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110023901), released 2026-04-29 — rates/figures may have changed since). It includes part-time and part-year earners, so it is not a full-time salary benchmark — check the occupation's regional wage data on [Job Bank](https://www.jobbank.gc.ca/):
  - Toronto $59,200 · Vancouver $58,200
  - Calgary $58,800 · Montréal $57,700 · Ottawa-Gatineau $70,800
  - Edmonton $57,500 · Winnipeg $53,200 · Québec City $65,300 · Canada $58,600
- Federal minimum wage: **$18.15/hr from 1 Apr 2026** (federally regulated private-sector employers only; where a provincial minimum is higher, the higher rate applies) (2026 data, source [ESDC news release, Mar 2026](https://www.canada.ca/en/employment-social-development/news/2026/03/government-of-canada-raises-the-federal-minimum-wage.html))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Earthquakes Canada (NRCan)** | `https://www.earthquakescanada.nrcan.gc.ca` | Seismic hazard calculator + 2020 National Building Code seismic hazard maps; recent-event feed. Earthquake risk scenarios: RiskProfiler `https://www.riskprofiler.ca/` (Geological Survey of Canada / NRCan + Global Earthquake Model) |
| **Public Safety Canada — National Risk Profile** | `https://www.publicsafety.gc.ca/cnt/mrgnc-mngmnt/ntnl-rsk-prfl/` | First report covers floods, wildland fires and earthquakes; next edition: heat events, hurricanes, space weather (page modified 2025-08-07) |
| **GEO.CA flood polygons** | `https://geo.ca/emergency/` | "Floods in Canada – Archive": NRCan satellite-derived flood-extent polygons for past floods; Canadian Disaster Database (events since 1900) |
| **BC PreparedBC hazard map** | `https://www2.gov.bc.ca/gov/content/safety/emergency-management/preparedbc/know-your-hazards/hazard-map` | BC hazards |
| **ECCC historical climate data** | `https://climate.weather.gc.ca/` | Historical hourly, daily and monthly weather data, extremes and Climate Normals (page modified 2026-10-22) |
| **Canadian Wildland Fire Information System** | `https://cwfis.cfs.nrcan.gc.ca/` | Daily national fire weather (Fire Weather Index System), fire behaviour and fire occurrence maps since 1994, from 2,500+ weather stations in Canada and the US; Fire M3 satellite detection of actively burning fires (source [NRCan — Current wildland fire activity: the CWFIS](https://natural-resources.canada.ca/forests-forestry/wildland-fires/current-wildland-fire-activity-cwfis), modified 2026-06-26) |
| **Health Canada radon** | `https://www.canada.ca/en/health-canada/services/health-risks-safety/radiation/radon.html` | Radon zones |

### Specific risks

- **Wildfire** — extreme + increasing:
  - BC, AB, ON (boreal), Atlantic
  - 2023 record fire season: >6,800 fires burned >14.6M ha of forest area and >230,000 people were evacuated; annual average >2.1M ha (2023 data, source [NRCan — Forest fires](https://natural-resources.canada.ca/forests-forestry/wildland-fires/forest-fires), National Burned Area Composite) — rates/figures may have changed since. ECCC's top 10 weather stories of 2023 states >18M ha without naming its dataset — the NRCan mapped figure is used here
  - 2023 evacuations included Yellowknife (20,000 residents), the West Kelowna and Bush Creek fire areas (22,000+ residents under orders or alerts; structures also lost in Kelowna) and Sept-Îles (2023 data, source [ECCC — Canada's top 10 weather stories of 2023](https://www.canada.ca/en/environment-climate-change/services/top-ten-weather-stories/2023.html)) — rates/figures may have changed since
  - **Insurance**: standard homeowner's and tenant's policies cover fire damage, including wildfire, plus additional living expenses from a mandatory evacuation; insurers may temporarily limit new policies, deductible and limit changes in areas under imminent threat, and more remote properties are generally more costly to insure (2026 data, source [IBC — Wildfires and insurance](https://www.ibc.ca/stay-protected/severe-weather-centre/wildfire-season) — insurer trade association ⚠️); FCAC lists fire, including wildfires, among events a home policy may cover (source [FCAC](https://www.canada.ca/en/financial-consumer-agency/services/insurance/unexpected-events-disasters.html), page modified 2026-07-14)
- **Flood** — major risk:
  - **Toronto**: urban flash flooding (2013, 2024)
  - **Calgary**: 2013 disaster
  - **Atlantic Canada**: storm surge + sea-level
  - **Montreal/Quebec**: spring snowmelt
  - GEO.CA satellite-derived flood maps
- **Earthquake**:
  - **BC West Coast — Cascadia Subduction Zone**: plates locked; a future offshore megathrust comparable to the 1964 M9.2 Alaska quake is expected, and geological evidence shows such events every 300–800 years; Canada's largest recorded quake was M8.1 on the Queen Charlotte fault (1949) (source [Earthquakes Canada — Seismic zones in Western Canada](https://www.earthquakescanada.nrcan.gc.ca/zones/westcan-en.php))
  - **Eastern Canada**: Charlevoix-Kamouraska seismic zone (1925 M6.2)
  - Vancouver/Victoria: high seismic preparedness required
- **Permafrost**: Yukon + NWT + northern BC/AB; thaw-triggered building damage
- **Ice storms**: Eastern (Quebec 1998 ice storm)
- **Hurricane**: Atlantic Canada (Fiona 2022)
- **Tornado**: recorded in every province and territory, most common in southern Alberta, Saskatchewan, Manitoba, Ontario, Quebec and western New Brunswick; Canada averages 97 tornadoes a year (Northern Tornadoes Project figure), the strongest generally May–August (2026 data, source Government of Canada Get Prepared — [Tornadoes](https://www.canada.ca/en/services/policing/emergencies/preparedness/get-prepared/hazards-emergencies/tornados.html), modified 2026-02-10, and [How to prepare](https://www.canada.ca/en/services/policing/emergencies/preparedness/get-prepared/hazards-emergencies/tornados/how-prepare.html), modified 2026-06-18)
- **Radon**: Health Canada guideline 200 Bq/m³; the 2024 Cross-Canada Survey (Evict Radon National Study with Health Canada, CAREX Canada and BCCDC) found 1 in 5 (17.8%) houses at or above it (2024 data, source [Health Canada](https://www.canada.ca/en/health-canada/services/environmental-workplace-health/reports-publications/radiation/cross-canada-survey-radon-concentrations-homes-final-report-health-canada-2012.html)). Highest shares of tested homes above 200 Bq/m³ in Health Canada's earlier survey: New Brunswick 24.8%, Manitoba 23.7%, Yukon 19.6%, Saskatchewan 16.3% (BC 7.9%, AB 6.6%) (2009–2011 data, source Health Canada Cross-Canada Survey final report, Mar 2012 — rates/figures may have changed since). Province-level shares only — test the specific home

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1950** | Asbestos (used before 1990 mainly to insulate buildings and homes) may be in older siding, cement and plaster, floor and ceiling tiles, roofing products and hot-water pipe insulation (source [Health Canada — Asbestos and your health](https://www.canada.ca/en/health-canada/services/air-quality/indoor-air-contaminants/health-risks-asbestos.html)); lead-based paint probable if built before 1960, exterior paint may contain lead if built 1960–1990 (source [Health Canada — Lead-based paint](https://www.canada.ca/en/health-canada/services/home-safety/lead-based-paint.html)); lead pipes allowed by the National Plumbing Code until 1975 and lead solder until 1986, and some homes may have a lead service line (source [Health Canada — Drinking water: what about lead?](https://www.canada.ca/en/health-canada/services/environmental-workplace-health/reports-publications/water-quality/what-about-lead.html)); knob-and-tube wiring (early 1900s–1940s) is safe if maintained by a licensed electrical contractor, but many insurers will not provide or renew coverage (source [ESA, Ontario's electrical safety regulator](https://esasafe.com/home-renovation-buying-and-selling/knob-and-tube/)) |
| **1950s–1970s** | Asbestos very common — federal ban on import, sale and use in force 30 Dec 2018 (SOR/2018-196); asbestos built into a structure before that date is not covered (source [ECCC](https://www.canada.ca/en/environment-climate-change/services/management-toxic-substances/list-canadian-environmental-protection-act/asbestos/information-prohibition-regulations.html)); UFFI insulation (widely used in the 1970s) — advertising, sale and import prohibited since Dec 1980 under the Hazardous Products Act (source [Health Canada](https://www.canada.ca/en/health-canada/services/consumer-product-safety/advisories-warnings-recalls/letters-notices-information-industry/canadian-prohibition-urea-formaldehyde-foam-insulation.html)) |
| **1980s–1990s** | Some asbestos in older renos; Poly-B (polybutylene) water piping — introduced to Alberta construction in the mid-1970s (not in a home built before 1975 unless re-plumbed), production stopped in 1998; no longer listed in current plumbing codes, but codes are not retroactive, so previously accepted products remain acceptable if they pose no health or safety hazard (source [Alberta Municipal Affairs — Safety Tips: Poly-B](https://open.alberta.ca/dataset/2e99ffe2-4810-413d-8a9f-c3cdb00f5951/resource/87384378-8df5-4f73-b2b4-3fd47e32ab38/download/2016-safety-tips-polybutylene-poly-b-pressure-water-piping-august-2016.pdf), reviewed Aug 2016, archived 2023-02-05 — rates/figures may have changed since); class actions in BC, ON and QC: DuPont settled first, then Shell ($20M settlement announced 11 Jun 2004; claim forms had to be postmarked by 18 Jun 2005, so that claim window has closed; proceedings continued against a remaining defendant) (source court-approved notice and press release posted by class counsel [Siskinds](https://www.siskinds.com/cmsfiles/PDF/Product/PolyPipe/Shell_Legal_Notice.pdf) — law firm ⚠️) |
| **2000s+** | Modern code; energy improvements |
| **Vermiculite / Zonolite attic insulation** | Pre-1990 — may contain asbestos (Libby-mine ore, 1920s–1990, mostly sold as Zonolite; not all pre-1990 vermiculite does); avoid disturbing it, flag for testing (source Health Canada advisory, Apr 2004) |
| **Cladding fires** (post-Grenfell era) | Which buildings carry combustible cladding: data not publicly available (no public register located, Oct 2026) — ask the condo corporation / strata for building-envelope and fire-inspection records; code rules at [NRC Codes Canada](https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada) (archived 2026-10-11) |

### Mandatory at sale

| Document | Province | Notes |
|---|---|---|
| **Property Disclosure Statement (PDS)** | BC voluntary (BCREA form; seller may give a "Property No Disclosure Statement" instead) | Known material latent defects must still be disclosed before contract; a no-disclosure form signals extra due diligence (source [BCFSA](https://www.bcfsa.ca/public-resources/real-estate/buying-home/search)) |
| **SPIS (Seller Property Information Statement)** | ON voluntary (some sellers prepare one; how often: data not publicly available) | If the seller gives the agent a statement meant for buyers, the agent must tell every interested buyer and give a copy on request (source [RECO](https://www.reco.on.ca/consumers/information-for-sellers/property-information-statements/), archived 2026-07-13) |
| **Real Property Report (RPR) + compliance** | AB standard-contract term (not statutory; conventional condo units generally exempt) | Survey of structures + municipal compliance; seller cannot swap in title insurance without buyer consent (2026 data, source Berjak Law RPR guide — secondary, law firm) |
| **Déclaration du vendeur** (DV; DVD for divided co-ownership) | QC mandatory in brokered sales by an individual of a chiefly residential immovable with <5 dwellings, since Jul 2012 | OACIQ form signed with the brokerage contract; seller declares to the best of their knowledge (source [OACIQ](https://www.oaciq.com/en/broker/brokerage-forms-clauses/how-to-use-the-mandatory-form-declarations-by-the-seller-of-the-immovable)) |
| **Title insurance** | ON optional — lawyers must advise it is not mandatory and not the only option (LSO Rules of Professional Conduct r. 3.2-9.4); uptake share: data not publicly available | Survey coverage may remove the need for a new survey and is acceptable to most lenders instead of a survey or RPR; exclusions include problems only a new survey or inspection would reveal (source [FSRA](https://www.fsrao.ca/consumers/property-and-other-insurance/understanding-title-insurance), archived 2026-09-04; [LSO](https://lso.ca/about-lso/legislation-and-rules/rules-of-professional-conduct/chapter-3), archived 2026-10-14) |
| **Strata documents (Form B / Form F)** | BC strata lots | Form B Information Certificate: strata fees, owner's arrears, contingency reserve fund balance, court proceedings, insurance summary — due within 7 days of a request, max $35 + up to 25¢ per page; Form F Certificate of Payment: required by the Land Title Office on transfer, max $15, current for 60 days (2026 data, source BC Government — [Form B](https://www2.gov.bc.ca/gov/content/housing-tenancy/strata-housing/renting-buying-selling/buying-and-selling-strata/paperwork-for-buyers-and-sellers/form-b-information-certificate), [Form F](https://www2.gov.bc.ca/gov/content/housing-tenancy/strata-housing/renting-buying-selling/buying-and-selling-strata/paperwork-for-buyers-and-sellers/form-f-certificate-of-payment)) |
| **Status Certificate** | ON condos (Condominium Act, 1998, s. 76) | Anyone can request it; the corporation must provide it within 10 days, for up to $100 incl. taxes; covers the current budget and last audited financial statements, reserve fund study and fund state, the unit's arrears, special assessments and ongoing litigation (2026 data, source [Condominium Authority of Ontario](https://www.condoauthorityontario.ca/condo-living/corporate-records/status-certificates/)) |

### Climate change projections

- BC + Prairies (AB/SK/MB) annual warming vs 1850–1900: 2021–2040 BC **+1.8°C** (0.9–2.6), Prairies **+2.3°C** (1.4–3.0); 2081–2100 under SSP2-4.5 BC **+3.6°C**, Prairies **+4.4°C**; under SSP3-7.0 BC **+4.8°C**, Prairies **+6.1°C**; Canada's North warms most (+6.0°C, SSP2-4.5, 2081–2100), BC least (2026 data, source [ECCC — Canada's Changing Climate Report 2026, Table 3.2](https://www.canada.ca/en/environment-climate-change/services/science-technology/changing-climate-report-2026/cccr-chapter-3-en.html))
- Wildfire: fire season already longer in most of Canada and fire weather up in AB + BC (medium confidence); frequency and intensity of extreme fire weather projected to rise in most regions (high confidence) (2026 data, source [CCCR 2026 ch. 8, Key Message 8.11](https://www.canada.ca/en/environment-climate-change/services/science-technology/changing-climate-report-2026/cccr-chapter-8-en.html))
- Permafrost: monitored northern sites have warmed and thawed since the 1980s; warming and thaw-driven landscape change continue with further warming (very high confidence), magnitude and timing low confidence because of local ground conditions (2026 data, source [CCCR 2026 ch. 6, Key Messages 6.13–6.14](https://www.canada.ca/en/environment-climate-change/services/science-technology/changing-climate-report-2026/cccr-chapter-6-en.html))
- Atlantic sea-level rise: Halifax median relative sea-level rise +0.28 m by 2050 and +0.68 m by 2100 under SSP2-4.5 (vs 1995–2014); sinking land pushes much of Atlantic Canada above the 0.56 m global average; a 1%-AEP extreme sea level in Halifax becomes a 14%-AEP event by 2050 (2026 data, source [ECCC — CCCR 2026 ch. 7](https://www.canada.ca/en/environment-climate-change/services/science-technology/changing-climate-report-2026/cccr-chapter-7-en.html))
- Increased insurance premiums for wildfire/flood

---

## Section: `--mains`

### Sources

- Per-municipality water utilities (Toronto Water, City of Calgary, Service de l'eau Montreal); in Metro Vancouver the regional district supplies treated bulk water and member municipalities run local distribution to homes (source [Metro Vancouver — The Regional System](https://metrovancouver.org/services/water/the-regional-system))
- Health Canada **Guidelines for Canadian Drinking Water Quality** (summary tables, Dec 2025 edition)
- Municipal water is the norm: 90% of households in the provinces had a municipal main water source and 9% a private well (2023 data, source [Statistics Canada — Table 38-10-0274-01, Households and the Environment Survey](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810027401), released 2025-12-09) — rates/figures may have changed since; Health Canada estimates ~4 million people in Canada rely on a private well, and the owner is responsible for its water quality (2025 data, source [Health Canada — Well water and health](https://www.canada.ca/en/health-canada/services/environment/drinking-water/well.html)). Rural homes off the municipal network may also rely on an on-site septic system — ask for its permit and pumping records

### Costs

Illustrative contractor estimates, not quoted figures — verify with local quotes. Only the urban-connection row is calibrated, against the City of Toronto 2026 fee schedule; no government cost figure for mains extensions, septic or wells was found (Nova Scotia's septic homeowner guide, Nov 2009, says only that replacing a system costs "thousands of dollars" and advises three written quotes):

| Scenario | Cost (CAD, est.) |
|---|---:|
| Water/sewer connection (urban), per service | ~$5,000–$15,000 (est.; Toronto 2026 City fees: new 25 mm water service + meter $6,818.29, new sanitary sewer connection in the road allowance $14,718.78 → $21,537.07 for both (computed); source [City of Toronto — Water rates & fees](https://www.toronto.ca/services-payments/property-taxes-utilities/utility-bill/water-rates-fees/), effective 1 Jan 2026) |
| Mains-line extension | ~$20,000–$60,000+ (est.; illustrative contractor range, no general government cost figure found: municipal charges are set per project, e.g. Peel Region splits 100% of the actual cost among benefiting properties by lot frontage, [Peel Region — Owner-initiated local improvements](https://peelregion.ca/construction/projects/owner-initiated-local-improvements), viewed 2026-11-04 — verify with local quotes) |
| Septic replacement | ~$15,000–$35,000 (est.; illustrative contractor range, no government cost figure found — verify with local quotes) |
| Bored well | ~$8,000–$20,000 (est.; illustrative contractor range, no government cost figure found — verify with local quotes) |

---

## Cost benchmarks (CA 2026)

Service and works rows are illustrative est. ranges, not quoted figures (no primary source publishes these ranges; contractor and professional fees vary by province, city and house size) — verify with local quotes; where CMHC's homebuyer guide gives a figure it is shown in the row ([CMHC — How much will my home really cost?](https://cmhc-schl.gc.ca/en/finance-and-investing/mortgage-loan-insurance/the-resource/how-much-will-my-home-really-cost), page undated; viewed 2026-11-04). FCAC tells buyers to budget 1.5–4% of the purchase price for upfront closing costs, naming home inspection, legal fees, property tax adjustments and title insurance as examples (land transfer tax not mentioned) ([canada.ca — Buying a home](https://www.canada.ca/en/financial-consumer-agency/services/buying-home.html), page dated 2025-10-20 — rates/figures may have changed since). Transaction-cost rows are computed from the `--tax` rates.

| Work | Cost (CAD, est.) |
|---|---:|
| Home inspection | $400–$700 (est.; CMHC: "around $500") |
| Title insurance | ~$200–$700 (est.; no single market price: FSRA says the one-time premium varies with property value and insurer and gives no figure, [FSRA — Understanding title insurance](https://www.fsrao.ca/consumers/property-and-other-insurance/understanding-title-insurance), archived 2026-09-04. Calibration, one Ontario insurer: TitlePLUS base premiums $175.00 new condo, $195.00 resale condo, $338.89 new house, $385.74 resale house, plus $0.90 per $1,000 of price over $500K, 8% PST extra; a $1M resale house is $385.74 + 500 × $0.90 = $835.74 before PST (computed), above this range, [TitlePLUS (LAWPRO) — Ontario Residential Premiums at a Glance](https://cdnc.heyzine.com/files/uploaded/3fb88f43468d2a6720f324d0d93dcf6beec4860b.pdf), effective 1 Mar 2025 — rates/figures may have changed since) |
| Real estate lawyer / notary | $1,500–$3,000 (est.; CMHC gives only a $500 minimum) |
| Survey / RPR / certificate of location | $700–$2,500 (est.; CMHC range $1,000–$2,000) |
| Land Transfer Tax (varies) | see above |
| **Total transaction cost (ON outside Toronto, $1M, FTB)** | **~$15–17k (1.5–1.7%)**, computed: LTT $16,475 − $4,000 refund + fees |
| **Total transaction cost (Toronto, $1M, FTB)** | **~$27–29k (2.7–2.9%)**, computed: LTT $16,475 − $4,000 + MLTT $16,475 − $4,475 + fees |
| **Total transaction cost (BC, $1.5M)** | **~$30–32k (2.0–2.2%)**, computed: PTT $28,000 + fees |
| **Total transaction cost (BC foreign, $1.5M, APTT district)** | **~$330–332k (22%)**, computed: PTT $28,000 + 20% APTT $300,000 + fees |
| Roof (asphalt shingle) | ~$8,000–$15,000 (est.; illustrative contractor range, no primary source — verify with local quotes) |
| Window replacement | ~$500–$1,200 each (est.; illustrative contractor range, no primary source — verify with local quotes) |
| Asbestos abatement | ~$5,000–$30,000+ (est.; illustrative contractor range, no primary source — verify with local quotes) |
| Vermiculite removal | ~$10,000–$40,000+ (est.; illustrative contractor range, no primary source — verify with local quotes) |
| Knob-and-tube re-wire | ~$8,000–$15,000 (est.; illustrative contractor range, no primary source — verify with local quotes) |
| Energy retrofit | ~$30,000–$80,000 (est.; illustrative contractor range, no primary source — verify with local quotes) |
| Heat pump installation | $8,000–$20,000 (est., stated as net of rebates; rebate basis unverified — federal Greener Homes Grant CLOSED, see Active fiscal incentives) |

## Active fiscal incentives (2025-2026)

- **First-Time Home Buyer Incentive (FTHBI)**: **CLOSED** — new submissions ended 21 Mar 2024, no new approvals after 31 Mar 2024; the 5% or 10% shared-equity mortgages already approved keep running (source CMHC FTHBI page)
- **First Home Savings Account (FHSA)**: $8,000 annual participation room (unused room carries forward), $40,000 lifetime; contributions deductible, saving tax-free for a qualifying first home (2026 data, source CRA FHSA pages)
- **HBP (Home Buyers' Plan)**: RRSP withdrawal up to $60,000 (from $35,000, for withdrawals after 16 Apr 2024 per Budget 2024); 15-year repayment, start deferred to the fifth year after the first withdrawal for first withdrawals 1 Jan 2022–31 Dec 2028 (2026 data, source CRA HBP page, modified 2026-02-17)
- **GST/HST New Housing Rebate**: rebate of part of the GST / federal HST on new builds, federal part only where fair market value is under $450,000; Ontario's provincial new housing rebate up to $24,000 regardless of value (2026 data, source CRA new housing rebate page, modified 2026-09-24)
- **First-time home buyers' GST/HST rebate**: up to **$50,000** (the full GST / federal HST) on a new home up to $1M, phased out between $1M and $1.5M, none at $1.5M+; builder agreements from 20 Mar 2025 and before 2031, construction started before 2031 and substantially completed before 2036 (enacted by Bill C-4, S.C. 2026, c. 2, Royal Assent 12 Mar 2026; source CRA GST/HST Memorandum 19-3-10, Oct 2026 + parl.ca LEGISinfo C-4)
- **Ontario new-home HST relief (temporary)**: the Ontario enhanced new housing rebate (ENHR) tops up the Ontario new housing rebate for homes bought from a builder 1 Apr 2026–31 Mar 2027 (owner-built: construction started in that window) (source CRA ENHR page, modified 2026-07-30; HST Relief Implementation Act, 2026, S.O. 2026, c. 5); the 5% federal part is relieved through the Ontario new home affordability payment (ONHAP), funded under Bill C-26 (S.C. 2026, c. 21, Royal Assent 18 Jun 2026; Finance Canada). Announced design: full 13% HST removed on new homes up to $1M for principal-residence or rental buyers, max $130,000, held to $1.5M and tapering to $24,000 at $1.85M+ (Ontario Newsroom) — verify amounts with CRA / ServiceOntario before relying on them
- **Provincial FTB rebates**: ON LTT refund up to $4,000 (+ Toronto MLTT rebate up to $4,475); BC PTT first-time buyer exemption on the first $500,000 for homes ≤ $835,000 (partial up to $860,000, since 1 Apr 2024) — max saving $8,000 computed (1% × $200k + 2% × $300k) (sources: ontario.ca, toronto.ca, gov.bc.ca first time home buyers' exemption page)
- **Canada Greener Homes Loan + Grant**: **CLOSED** — Grant took applications May 2021–Feb 2024 (final document upload 31 Dec 2025); Loan (up to $40,000) closed with funding fully committed (source NRCan program pages, loan page modified 2026-04-17); NRCan points to the Canada Greener Homes Affordability Program and provincial incentives instead
- **CMHC Multi-Unit Mortgage Loan Insurance**: lower down for purpose-built rentals

## Common listing platforms

- **Realtor.ca** — CREA's consumer listing site, run since Jan 2025 by REALTOR.ca Canada Inc., a wholly owned CREA subsidiary (2026 data, source [CREA — REALTOR.ca for Canadians](https://www.crea.ca/technology/realtor-ca-for-canadians/)); share of MLS® listings: data not publicly available — verify at [CREA](https://www.crea.ca/)
- **Centris.ca** — Quebec only
- **Royal LePage, RE/MAX, Sotheby's, Engel & Völkers** — agency networks
- **Zolo** — alternative
- **HonestDoor** — sold data + modelled value estimates ("not an official appraisal"); city pages listed for all 10 provinces + 3 territories (2026 data, source [honestdoor.com](https://www.honestdoor.com))

## Caveats unique to CA

- **Federal foreign-buyer ban** until **1 Jan 2027** (Prohibition Act in force 1 Jan 2023; repeal deferred to 1 Jan 2027 by Budget Implementation Act, 2024, No. 1, S.C. 2024, c. 17, s. 149)
- **Provincial fragmentation extreme** — each province has different cadastre, LTT, rent control, condo law
- **BC vs ON major divergence** — BC PTT 1-3% + 2% over $3M + 20% APTT on foreign buyers (5 regional districts); ON LTT 0.5-2.5% + Toronto MLTT (up to 8.6% above $20M) + 25% ON NRST on foreign buyers (+10% Toronto MNRST)
- **UHT eliminated for 2025+** — no tax payable and no return required for 2025 and later calendar years (UHT Act ss. 1.1 and 6.1, S.C. 2026, c. 3); 2022–2024 returns and liabilities remain; the repeal of the Act itself (S.C. 2026, c. 3, s. 169) is listed as not in force (2026 data, source [Justice Laws — Underused Housing Tax Act](https://laws-lois.justice.gc.ca/eng/acts/U-0.5/FullText.html), current to 2026-10-19)
- **BC SVT rates DOUBLED 2026** — foreign / untaxed worldwide earners 3%, Canadian citizens / PRs 1%; foreign rate 4% from the 2027 tax year (S.B.C. 2026, c. 5)
- **Vancouver Empty Homes Tax 3%** + **Toronto Vacant Home Tax 3%**
- **BC LOTR (Land Owner Transparency Registry)** — free public beneficial-owner search since Apr 2024 (UNIQUE in Canada)
- **Vermiculite / Zonolite attic insulation** — pre-1990 — common asbestos hazard
- **Knob-and-tube wiring** — pre-1950s; insurance-blocking
- **Poly-B plumbing** (1978-1995) — class-action; flagged
- **Mortgage stress test** = OSFI minimum qualifying rate: **greater of contract rate + 2% or 5.25% floor**; from **21 Nov 2024** uninsured-mortgage renewals switching lenders are exempt from re-stress-testing if loan + amortization unchanged (2026-05-27 verified, source: [OSFI MQR for uninsured mortgages](https://www.osfi-bsif.gc.ca/en/supervision/financial-institutions/banks/minimum-qualifying-rate-uninsured-mortgages))
- **Cross-border tax** — US/CA dual citizens face FATCA + complex CGT
- **Strata depreciation reports** mandatory in BC for stratas with 5+ lots, every 5 years, with no ¾-vote deferral since 1 Jul 2024 (secondary: BCREA Legally Speaking #599)
- **Indigenous land** — leasehold-only on reserve land (e.g., Musqueam, Squamish/Tsleil-Waututh leasehold lands, Vancouver)
- **CMHC mortgage insurance** mandatory if down payment <20%; insured loans only below a $1.5M purchase price, minimum down payment 5% of the first $500,000 + 10% of the rest, and the purchase must not be barred by the Prohibition Act (2026 data, source CMHC general requirements page)
- **Toronto MLTT graduated high-value rates** from 1 Apr 2026

## Reddit / forum sources

- **r/RealEstateCanada**
- **r/PersonalFinanceCanada** — mortgage + tax discussion
- **r/canadahousing**, **r/TorontoRealEstate**, **r/VancouverRealEstate**, **r/vancouverhousing**
- **Globe and Mail Real Estate**, **Financial Post Personal Finance**
- **Better Dwelling** (analysis)

## Verification authorities

| Authority | When to call |
|---|---|
| **Provincial Land Title Office** | Title verification |
| **Municipal property tax department** | Tax assessment + arrears |
| **MPAC (ON) / BC Assessment** | Assessed value |
| **Real estate lawyer** (mandatory in most provinces) | Final closing |
| **Strata/Condo board** | If apartment |
| **Health Canada Radon** | Testing |
| **CMHC** | Mortgage insurance + market data |

## Source URL templates

| Source | URL pattern |
|---|---|
| Realtor.ca | `https://www.realtor.ca/<prov>/<city>/real-estate` (e.g. `/on/toronto/real-estate`) |
| Centris.ca (QC) | `https://www.centris.ca/` |
| Teranet OnLand (ON) | `https://www.onland.ca/` |
| BC LTSA + LOTR | `https://ltsa.ca/` + `https://ltsa.ca/products-services/lotr/about-lotr/` (landtransparency.ca redirects here; updated 2026-10-23) |
| AB SPIN2 | `https://spin.alt.alberta.ca/` |
| QC Registre foncier | `https://www.registrefoncier.gouv.qc.ca/` |
| CREA HPI | `https://www.crea.ca/housing-market-stats/mls-home-price-index/` |
| Earthquakes Canada | `https://www.earthquakescanada.nrcan.gc.ca/` |
| Public Safety Canada | `https://www.publicsafety.gc.ca/` |
| Health Canada Radon | `https://www.canada.ca/en/health-canada/services/health-risks-safety/radiation/radon.html` |
| CRA tax | `https://www.canada.ca/en/revenue-agency.html` |

## Status

✅ Fast-changing sections re-verified as of 2026-10-23; each section's date is in the Per-section verification table.

✅ **Fully populated** as of 2026-04-25 (Vancouver board name (Greater Vancouver REALTORS) corrected 2026-09-18 per gvrealtors.ca). Ownership tracker entries re-checked 2026-09-24 in the October regwatch wave (see shared/regulatory-watch.md).
**Coverage check**: pricing (CREA + provincial boards), traffic, tax (extreme provincial divergence), rental (RTA per province), work, risks (wildfire + flood + earthquake + permafrost + radon), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for `--rental` (re-verified 2026-10-23), the Sep 2026 / Q3 2026 `--price` benchmark rows (each sourced to CREA or its board), the `--work` StatCan 2024 CMA medians and federal minimum wage, the `--risks` rows sourced to government and regulator pages, the climate projections (ECCC Canada's Changing Climate Report 2026) and the tax facts re-checked in the 2026-10-23 refresh and gap-closing pass: ON LTT + Toronto MLTT tiers from 1 Apr 2026, BC PTT / APTT, BC SVT 2026 doubling (S.B.C. 2026, c. 5), UHT eliminated for 2025+ (S.C. 2026, c. 3), 50% capital-gains inclusion (2/3 proposal cancelled 21 Mar 2025), CRA 2026 marginal-rate brackets, Montreal 2026 rates computed from the city's billing data, foreign-buyer ban to 1 Jan 2027 (S.C. 2024, c. 17, s. 149); MEDIUM for the post-2027 foreign-buyer regime (review under way, nothing tabled located by 2026-11-03), the Ottawa property-tax row (est. from draft-budget figures), the AB RPR row (law-firm source), the Cost benchmarks inspection / lawyer / survey ranges (est.; CMHC figures shown in the rows: inspection "around $500", lawyer $500 minimum, survey $1,000–$2,000), the `--mains` urban connection range (est., calibrated on Toronto 2026 fees) and `--traffic` city AADT layers (not re-verified); LOW for the contractor cost ranges with no primary price source (`--mains` extension, septic and well rows; Cost benchmarks title-insurance and works rows; est.).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-23 | 2026-11-04 maintenance run | Square feet is now described as a listing convention, not a measured fact; RECA's Residential Measurement Standard guide shows Alberta licensees report size in both square metres and square feet. |
| `--tax` | 2026-10-23 | 2026-11-04 maintenance run | Vancouver, Toronto, Calgary, Edmonton and Halifax rates, the Ontario, Toronto and BC transfer-tax scales and the first-time buyer rebates match the municipal and provincial pages. The Underused Housing Tax entry now cites the Act as current to 2026-10-19, and the foreign buyer ban still has no successor measure ahead of Budget 2026 on 5 Nov 2026. |
| `--rental` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--work=<profession>` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--risks` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Climate change projections (in `--risks`) | 2026-10-23 | 2026-10-23 refresh wave | Re-sourced to ECCC Canada's Changing Climate Report 2026; insurance-premium line carries no number |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | 11 templates checked by page content; LOTR redirect and Realtor.ca pattern updated |
| Country profile — foreign-buyer ban line only | 2026-10-23 | 2026-10-23 refresh wave | 1 Jan 2027 end date matches Justice Laws (current to 2026-09-30); rest of the profile not fully re-verified |
| Cost benchmarks (CA 2026) | 2026-10-23 | 2026-11-04 maintenance run | CMHC's homebuyer figures and FCAC's 1.5–4% closing-cost guide are unchanged. Title insurance and works rows are marked as est. because no primary source publishes them, and FSRA says title premiums vary by property value and insurer. |
| `--mains` | 2026-10-23 | 2026-11-04 maintenance run | Mains extension, septic and bored well rows are marked as illustrative contractor est. ranges, since no government cost figure was found; verify with local quotes. |

Other sections were partly refreshed on 2026-10-23 but keep unverified items, so they default to the Status footer date: Country profile, `--traffic`, `--mains`, Active fiscal incentives, Common listing platforms, Caveats unique to CA, Reddit / forum sources, Verification authorities (see Update history).

## Extension TODOs

- [ ] Per-municipality property tax mill rates table
- [ ] Per-province condo/strata law nuances
- [ ] BC LOTR beneficial-owner verification flow
- [ ] Indigenous land lease verification (Musqueam, Cowichan, etc.)
- [ ] Vermiculite/Zonolite testing decision tree
- [ ] Poly-B / Knob-and-tube remediation cost
- [ ] Stress test mortgage qualification calculator
- [ ] Cross-border US/CA tax decision tree
- [ ] Per-province RTA tenant protections summary
- [ ] BC SVT vs Vancouver EHT scenario optimization

## Update history

- **2026-04-25** — Initial population
- **2026-05-27** — Toronto MLTT high-value tiers, BC APTT, capital-gains inclusion, Section 116 and OSFI stress-test lines re-checked (stamps in the body)
- **2026-09-18** — Vancouver board name corrected to Greater Vancouver REALTORS (gvrealtors.ca)
- **2026-09-24** — Ownership tracker entries re-checked in the October regwatch wave (shared/regulatory-watch.md)
- **2026-10-23** — Refresh wave. Playbook-level stamp not advanced: `--mains` stays open after the gap-closing pass (wells line re-sourced to StatCan Table 38-10-0274-01, 2023 data, and the urban connection row calibrated on Toronto 2026 fees, but the section is not confirmed closed) and `--traffic` city AADT layers were not re-checked; `--price`, `--tax`, `--work`, `--risks` and Cost benchmarks were closed in the gap-closing pass and `--rental` was re-verified in the refresh. Facts changed / confirmed / unverifiable per section:
  - Country profile 1 / 5 / 3 — CAD rate updated to the Bank of Canada 22 Oct 2026 rate; foreign-buyer ban end date (1 Jan 2027) confirmed against Justice Laws; postcode, admin units, BC PID and Indigenous leasehold not re-checked
  - `--price` 11 / 3 / 1 — all 9 benchmark rows replaced with Sep 2026 board data (Montreal Q3 2026), each sourced; HPI-vs-average ratios computed; Realtor.ca ~95% MLS share unverified
  - `--traffic` 4 / 1 / 2 — provincial count sources re-pointed to MTO, BC Traffic Data Program, Alberta highway traffic counts and Quebec MTMD pages; city AADT layers and verdict bands (curated) not re-checked
  - `--tax` 29 / 34 / 4 — 2026 property-tax rates for Toronto, Vancouver, Calgary, Halifax and Edmonton; Toronto MLTT $10M–$20M tier 7.55%; Alberta fee $50 + $5 per $5,000; Quebec 2026 scale and Montréal tiers; NS HST 14%; UHT eliminated for 2025+; BC SVT 2026 rates and 4% foreign rate for 2027; Section 116 at 25% of the purchase price; Montreal and Ottawa rates, combined marginal-rate range and the $250k-threshold attribution unverified
  - `--rental` 10 / 11 / 1 — ON guideline 2.1% (2026) / 1.9% (2027); BC STR registry fees; Toronto $390 registration, 6% MAT and fines; CITQ amendments; Part XIII / NR6; TAL name
  - `--work` 2 / 2 / 3 — federal minimum wage $18.15 from 1 Apr 2026; federal incorporation $200; salary ranges kept as est.
  - `--risks` 13 / 9 / 11 — hazard sources re-pointed; 2023 fire season (NRCan 14.6M ha and ECCC 18M ha both shown); 2023 evacuations; Cascadia; radon 2024 survey; asbestos ban 30 Dec 2018; vermiculite; BC PDS / AB RPR / QC DV wording; build-era rows, sale-document rows, tornado and WUI insurance unverified
  - Climate change projections 4 / 0 / 1 — re-sourced to ECCC Canada's Changing Climate Report 2026
  - `--mains` 2 / 0 / 5 — Metro Vancouver bulk-water role; Health Canada guideline edition; cost table stays illustrative est.
  - Cost benchmarks 4 / 0 / 11 — transaction rows recomputed from `--tax` rates (ON split into Toronto and outside Toronto); service and works ranges labelled est.
  - Active fiscal incentives 6 / 2 / 1 — FTHBI and Greener Homes marked CLOSED; federal FTHB GST/HST rebate and Ontario's temporary rebate (1 Apr 2026–31 Mar 2027) added
  - Caveats unique to CA 5 / 6 / 0 — BC vs ON divergence, BC SVT, strata depreciation and CMHC lines updated; UHT line corrected (2025+ liability removed, repeal of the Act not in force); 'LOTR unique in Canada' not checked
  - Common listing platforms 1 / 1 / 3 — HonestDoor coverage corrected; Realtor.ca share, Zolo, Sotheby's and Engel & Völkers unverified
  - Reddit / forum sources 1 / 3 / 3 — r/VancouverRE replaced; claims rest on search listings
  - Source URL templates 2 / 9 / 0 — LOTR redirect, Realtor.ca pattern
  - Verification authorities 0 / 0 / 1 — no content change
  - Gap-closing pass (confirmed / changed / relabelled): `--price` 1 / 2 / 4, `--tax` 4 / 5 / 3, `--work` 3 / 2 / 0, `--risks` 1 / 11 / 1 and Cost benchmarks 4 / 0 / 5 — closed; `--mains` 0 / 1 / 2 — patched, still open; total 13 / 21 / 15. Main changes: national and Halifax-Dartmouth MLS® HPI levels from CREA's HPI data, Calgary YoY and average from the CREB stats package, HPI-vs-average ratios recomputed, Realtor.ca MLS share relabelled data not publicly available (also in Common listing platforms); city salary ranges replaced by StatCan 2024 CMA medians, Workopolis, WSIB, WorkSafeBC and AWCBC checked, CA designation updated to CPA; Montreal property tax computed for all 19 boroughs, Quebec school tax added, Ottawa est. with inputs shown, CRA 2026 marginal-rate brackets, $250k threshold re-attributed to Finance Canada, Bloomberg attribution replaced by Global News, Budget 2026 date added; CMHC figures added to three Cost benchmarks rows; tornado, WUI insurance, build-era, condo and strata document, title insurance, SPIS and CWFIS rows sourced, cladding register relabelled; `--mains` wells shares from StatCan 2023 data and the urban connection row calibrated on Toronto 2026 fees
- **2026-11-04** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (CA 2026). Playbook-level date now 2026-10-23.
