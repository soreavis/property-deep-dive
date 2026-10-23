# Ireland 🇮🇪 — Property Due-Diligence Playbook

ISO2: `ie`. Status: ✅ Fully populated (researched 2026-04; Tier-A refresh 2026-07-03).

## Country profile

- **Postcode (Eircode)**: 7-character format `D02 X285` (Dublin) — first 3 chars routing key, last 4 unique identifier per address. Launched 2015.
- **Admin levels**: 4 provinces (historical) → 26 counties → **31 local authorities** (post-2014 reform)
- **Currency**: EUR (€)
- **Languages**: English (de facto); **Irish/Gaeilge** (constitutional first official language; **Gaeltacht** regions: parts of Donegal, Mayo, Galway, Kerry, Cork, Waterford, Meath)
- **Cadastre**: **Tailte Éireann** (formed 2023 by merger of Property Registration Authority + Ordnance Survey Ireland + Property Services Regulatory Authority)
- **Identifier**:
  - **Folio number** (Land Registry — modern system, 95% of country)
  - **Deed** (Registry of Deeds — older system, mostly older Dublin titles)
- **Ownership types**: **freehold** + **leasehold** (common in apartments + Dublin city)

## Section: `--price`

### Primary sources

- **Tailte Éireann**: `https://tailte.ie/`
- **Property Price Register (PPR)** (FREE, official sales register since 2010): `https://www.propertypriceregister.ie/`
  - Every residential sale since 2010 recorded; searchable by Eircode/town/county
- **Daft.ie** (largest listings): `https://www.daft.ie/`
  - Quarterly Daft Reports (rent + sales)
- **MyHome.ie**: `https://www.myhome.ie/` — second-largest
- **CSO (Central Statistics Office) RPPI** quarterly: `https://www.cso.ie/`
- **BPFI (Banking & Payments Federation Ireland)** — mortgage indices: `https://bpfi.ie/`
- **Revenue.ie** for tax + LPT data

### Listing platforms

- **Daft.ie** — DOMINANT
- **MyHome.ie** — second
- **Sherry FitzGerald**, **DNG**, **Savills**, **REA**, **Lisney**, **Hooke & MacDonald**, **Coonan** — agency networks

### 2025 price benchmarks (PPR + Daft + CSO)

| Region | Avg €/m² (apt) | Avg total (semi-detached) |
|---|---:|---:|
| **Dublin City Centre** | 5,500–9,000+ | 700,000–1,500,000+ |
| **Dublin South County** | 5,000–7,500 | 600,000–1,100,000 |
| **Dublin North County** | 4,500–6,500 | 480,000–800,000 |
| **Dublin commuter (Kildare/Wicklow/Meath)** | 3,500–5,000 | 380,000–600,000 |
| **Cork city** | 3,500–5,000 | 380,000–650,000 |
| **Galway city** | 3,500–5,000 | 380,000–650,000 |
| **Limerick / Waterford** | 2,500–3,500 | 250,000–420,000 |
| **Smaller cities** | 1,800–2,800 | 180,000–320,000 |
| **Rural Connemara / Donegal / Mayo** | 1,200–2,200 | 150,000–280,000 |

- **CSO RPPI (latest)**: national prices **+6.2% YoY to April 2026** (April 2026 data, source CSO RPPI April 2026 release). From the March 2026 release: Dublin +5.7%, outside Dublin +7.2%; national median dwelling price **€390,461** (12 months to March 2026, source CSO, published 13 May 2026). (2026-07-03 verified)

### Compute

1. €/m² = price / **GIA (Gross Internal Area)** — Irish standard
2. **PPR cross-check**: official sale prices since 2010 (every sale)
3. **Folio vs Deed** affects conveyancing speed + cost
4. **BER (Building Energy Rating)** A-G: B-rated minimum for many lenders 2026

### Key terms

- Folio = Land Registry title (modern system)
- Deed = Registry of Deeds title (older, mostly Dublin)
- BER = Building Energy Rating
- Eircode = postcode
- LPT = Local Property Tax
- HTB = Help-to-Buy

---

## Section: `--traffic`

### Sources

- **TII (Transport Infrastructure Ireland)**: `https://www.tii.ie/` — motorways + national roads
- **National Traffic Monitoring (NTM)** counts
- **OpenStreetMap** + Local authorities for regional/local roads

### Key term

**AADT** (same as UK) — Annual Average Daily Traffic.

### Verdict bands

- 🟢 < 1,000 v/d (boreens, residential)
- 🟡 1,000–8,000 v/d (R-roads, regional)
- 🟠 8,000–25,000 v/d (urban arterial, N-road)
- 🔴 > 25,000 v/d (M-road, M50, urban core)

---

## Section: `--tax`

### Annual property tax — LPT (Local Property Tax)

**MAJOR REVALUATION 2026-2030 cycle**:
- **Valuation date**: 1 November 2025
- **Filing deadline**: 7 November 2025 (extended to 12 Nov 2025)
- Applies to LPT charges 2026–2030
- **Bands widened by 20%** to soften impact of price rises
- **96% of properties remain in their existing band**
- **New base rate**: **0.0906%** (was 0.10286%)

#### LPT bands (2026-2030 cycle)

19 bands for properties valued up to €2.1M:

| Band | Value range | Annual LPT charge |
|---|---:|---:|
| 1 | €1–€240,000 | €95 |
| 2 | €240,001–€315,000 | €235 |
| 3 | €315,001–€420,000 | €333 |
| 4 | €420,001–€525,000 | €428 |
| 5 | €525,001–€630,000 | €523 |
| ... | ... | ... |
| 19+ | up to €2.1M | progressive |

**Above €2.1M**: 0.0906% on first €1.26M + 0.25% on €1.26M-€2.1M + 0.30% above

- Properties under €525k pay **€5–€25 extra**
- **LAVL** (Local Authority Variation): each county can adjust **±15%**
- Significantly lower than UK Council Tax
- (2026-07-03 verified; source [Revenue.ie LPT valuation bands and rates](https://www.revenue.ie/en/property/local-property-tax/valuing-your-property/valuation-bands-rates.aspx))

### Vacant Homes Tax (VHT)

- Additional charge on dwellings occupied <30 days in a chargeable period. **2026 rate = 7× the base LPT** (Finance Act 2024; was 3× 2022-23, 5× 2023-24). Self-assessed; separate from LPT. (2026-07-03 verified; source [Revenue.ie VHT rate](https://www.revenue.ie/en/property/vacant-homes-tax/apply/rate.aspx))

### Residential Zoned Land Tax (RZLT)

- Annual self-assessed tax (Part 22A TCA 1997) at **3% of market value** on serviced land zoned for residential development that appears on the local authority's annually revised RZLT map. Liability date **1 February** each year from 2025; return and payment by **23 May**. For 2025 and 2026, owners who requested rezoning between 1 Feb and 1 Apr could claim exemption for that year. **Finance (No. 2) Bill 2026 s.75** (initiated 19 Oct 2026, **NOT enacted as of 2026-10-23**) would add a 2027 window: land on the revised map due by 31 Jan 2027 could be exempted from the 1 Feb 2027 liability if the owner requests rezoning, unless the land has a current planning application proposing, or an extant permission allowing, residential development. Check the RZLT map before buying a zoned site. (2026-10-23 verified; sources [Revenue TDM Part 22A-01-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-22a/22a-01-01.pdf), [Finance (No. 2) Bill 2026 Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))

### Derelict Property Tax (DPT) — Bill, not yet law

- **Finance (No. 2) Bill 2026 s.76** (new Part 22C TCA 1997; initiated 19 Oct 2026, **NOT enacted as of 2026-10-23**; needs a ministerial commencement order after enactment): annual **7% of market value** of property on a local authority's **final derelict-property register** plus its appurtenant land, charged on **1 March**, self-assessed, pay and file with Revenue by **23 June**. Scope: property not in use as, or suitable for use as, a dwelling or business premises, in built-up areas of **4,000+** people (2027 registers), widening to **2,000+** from the 2028 registers. Timeline: first preliminary registers by **1 Sep 2027**, first final registers by **28 Feb 2028**, first liability date **1 Mar 2028**, first pay-and-file **23 Jun 2028**. Paid LPT and VHT are credited against DPT (capped at the DPT due). Unpaid DPT and interest become a **charge on the property**; up to **30% surcharge** for significant undervaluation; deferral after a recent change of ownership, during remediation and during appeals. Government policy is for DPT to replace the local-authority Derelict Sites Levy, but the Bill as initiated does not repeal it. Buying a derelict property: check its register status with the local authority. (2026-10-23 verified; sources [Finance (No. 2) Bill 2026 as initiated](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf), [Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))

### Transaction taxes — Stamp Duty

**Residential** (revised 2024-2025):

| Band | Rate |
|---|---:|
| Up to €1,000,000 | **1%** |
| €1,000,001–€1,500,000 | **2%** |
| Above €1,500,000 | **6%** (from 2 October 2024; not charged on 3+ apartments in the same block, which pay 1% to €1M and 2% above) |
| Bulk-purchase (10+ residential properties in any 12 months, **apartments excluded**; s.31E SDCA 1999) | **15%** (raised from 10% w.e.f. 2 Oct 2024; 10% rate dated from 2021) |

- (2026-07-03 verified; source [Revenue.ie stamp duty rates](https://www.revenue.ie/en/property/stamp-duty/property/stamp-duty-property/rates.aspx))
- **First-time buyers**: same standard rates; **Help-to-Buy (HTB)** scheme provides a separate rebate of up to €30k (contracts 23 Jul 2020 – 6 Oct 2026), raised to **up to €35k for contracts or first self-build drawdowns from 7 Oct 2026 to 31 Dec 2029** (Budget 2027; Finance (No. 2) Bill 2026 s.17, NOT enacted as of 2026-10-23; Revenue's HTB page already shows €35k)
- **Commercial / non-residential**: **7.5% flat** (since 9 October 2019)

### Conveyancing

- **Solicitor fees**: **€1,500–€2,500** typical
- **Searches**: ~€100–€300
- **Land Registry fees**: €20–€910 (sliding scale)
- **Engineer's report**: €300–€600 (recommended)
- **VAT 23%** on professional fees

### Total transaction cost (buyer)

- Resale primary residence: ~**2–4%** typical (low compared to W. Europe)
- Commercial: ~9–10%
- High-value (>€1.5M): up to ~9%

### VAT

- New build houses: **13.5%**
- New/completed **apartments**: **9%** (second reduced rate, temporary to 31 Dec 2030; Finance Act 2025 s.70) only for apartments in a multi-storey building with ≥3 apartments sharing grouped or common access, and whole apartment blocks; from 26 Nov 2025 also student-accommodation blocks, qualifying sites and construction services until completion. A single apartment above a shop or under a duplex stays at **13.5%** (2025 data, source Revenue TDM *Supply and Construction of Qualifying Apartments and Apartment Blocks* + Finance Act 2025; 2026-10-21 verified)
- Existing: VAT-exempt; Commercial new builds: 23%

### Capital gains

- **CGT**: **33%** standard rate (s.28(3) TCA 1997). **Budget 2027**: Finance (No. 2) Bill 2026 s.36 (initiated 19 Oct 2026, **NOT enacted as of 2026-10-23**) cuts it to **31% for disposals on or after 7 Oct 2026** once enacted; development-land gains stay at **33%** (s.649A, not amended by the Bill; per Deloitte, secondary). (2026-10-23 verified; source [Finance (No. 2) Bill 2026 Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))
- **Principal Private Residence (PPR) relief**: full exemption for owner-occupied primary
- **Annual personal exemption**: €1,270

### Capital Acquisitions Tax (CAT)

- **Inheritance/gift tax**: 33% above thresholds
- Group A (parent-child): **€420,000** threshold for gifts and inheritances taken on or after 7 October 2026 (Budget 2027; Finance (No. 2) Bill 2026 s.66, **NOT enacted as of 2026-10-23**; Revenue's thresholds page already applies it); **€400,000** from 2 October 2024 to 6 October 2026 (Budget 2025; Finance Act 2024 s.99; was €335,000)
- Group B (sibling, niece/nephew): **€44,000** from 7 October 2026 (same Bill); €40,000 from 2 October 2024 to 6 October 2026 (was €32,500)
- Group C (other): **€22,000** from 7 October 2026 (same Bill); €20,000 from 2 October 2024 to 6 October 2026 (was €16,250)
- (2026-10-23 verified; sources [Revenue.ie CAT thresholds](https://www.revenue.ie/en/gains-gifts-and-inheritance/cat-thresholds-rates-and-aggregation-rules/cat-thresholds.aspx), [Finance (No. 2) Bill 2026 Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))

### Local Authority charges

- **NPPR** (Non-Principal Private Residence) — abolished
- **Household Charge** (2012) — abolished, replaced by LPT
- Various commercial rates apply

### Future risk

- **LPT 2026-2030** locked
- **HTB scheme** extended through **31 December 2029** (Budget 2025); cap raised to €35,000 from 7 Oct 2026 (Budget 2027, Finance (No. 2) Bill 2026, NOT enacted) (2026-10-23 verified; source [Revenue.ie Help-to-Buy — how much can you claim](https://www.revenue.ie/en/property/help-to-buy-incentive/how-much-can-you-claim.aspx))
- **Stamp Duty** 6% above €1.5M relatively recent (2024)
- **Finance (No. 2) Bill 2026** (Budget 2027; initiated 19 Oct 2026, **NOT enacted as of 2026-10-23**): CGT 31%, HTB €35k, CAT thresholds, Rent Tax Credit, Rent-a-Room €16k, a 2027 RZLT exemption window and the new Derelict Property Tax (each labelled above and below); recheck each once the Finance (No. 2) Act 2026 is signed

---

## Section: `--rental`

### Long-term residential

- **RTB (Residential Tenancies Board)**: `https://www.rtb.ie/` — registration mandatory within 1 month of new tenancy
- **Rent controls — nationwide since 20 June 2025**: the Residential Tenancies (Amendment) Act 2025 extended Rent Pressure Zones to the whole country. **From 1 March 2026, RPZs are replaced by a permanent national rent-control system** (Residential Tenancies (Miscellaneous Provisions) Act 2026, No. 3 of 2026) covering all private + student-specific tenancies. Annual increase cap: **2% or CPI, whichever is lower**. **New-build apartments and student-specific accommodation** (commencement notice or 7-day notice lodged with the building control authority on or after 10 June 2025; also extensions of 25%+ of floor area and change-of-use conversions) are exempt from the 2% cap — CPI-linked only (RTA 2004 s.19(4)(aa) inserted by Act 3 of 2026 s.8; 2026-10-21 verified). New tenancies from 1 Mar 2026 run as **6-year "tenancies of minimum duration"**; landlords may reset to market rent only at the start of a new tenancy (not after a no-fault termination) or at the end of the 6-year cycle. **Large landlords** (4+ tenancies or a company) are barred from no-fault evictions for tenancies beginning on/after 1 Mar 2026 once the first six months have passed (RTB: all landlords can end a tenancy in the first six months for any reason). (2026-07-03 verified; source [RTB rental law changes from 1 March 2026](https://rtb.ie/renting/rental-law-changes-from-1-march-2/))
- **Cost Rental** scheme: state-subsidized below-market
- **Tenancy types**:
  - Tenancies of unlimited duration (since 11 June 2022)
  - Pre-existing fixed-term tenancies grandfathered
- **Notice periods strict**

### Short-let (Airbnb / tourist accommodation)

**Irish short-let tax framework** (NOT UK FHL — there is no Irish FHL regime; Revenue does not treat short-term guest accommodation as Case V rental income):
- **Case IV (other income) vs Case I (trading)**: guests are licensees, not tenants with exclusive possession, so short-term guest income (e.g. via an online booking site) is not Case V rental income. It is taxed under **Case IV** when the letting is occasional, even with extra services, and under **Case I** when it is a trade (let frequently and regularly on a commercial basis with a view to profit); Case V applies only where a genuine tenancy exists. Case I allows wear-and-tear capital allowances of **12.5% a year over 8 years** on fixtures and fittings (s.284(1) TCA 1997). Under Case IV no capital allowances are available and only direct costs of the accommodation service (e.g. booking commission, cleaning) are deductible, not insurance, general maintenance or pre-letting costs. Rent-a-Room relief does not apply to short-term guests. (2026-10-23 verified; sources [Revenue Irish rental income](https://www.revenue.ie/en/property/rental-income/irish-rental-income/index.aspx), [Revenue TDM Part 04-01-20](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-04/04-01-20.pdf))
- **DAC7 platform reporting**: Airbnb/Booking/Vrbo report host earnings to Revenue from 2024 onward.
- **Short-Term Letting Register (STLR)**: planned via the Short-Term Letting and Tourism Bill (General Scheme approved 15 Apr 2025). The Government **published the Bill on 6 Oct 2026** (DETE): it gives full effect to EU Reg 2024/1028, gives Fáilte Ireland registration and inspection powers, and requires platforms to display registration numbers, run random checks, share data and remove non-compliant listings. The Bill **has not been initiated in the Oireachtas as of 2026-10-23** (2026 bill register complete to Bill No. 100). DETE (press releases 13 May and 6 Oct 2026 + its STL page) announces that the register **opens 1 Dec 2026** and all hosts **must register by 31 Dec 2026** (platform obligations also from 31 Dec 2026; annual renewal; nominal annual fee, structure not yet published). These are announced targets, not yet law: Fáilte Ireland's own page still says registration "will open once the necessary legislation has been passed" and gives no dates. Both are primary sources, and the gap is the missing Bill. Hosts letting for ≤21 nights will have to register each unit and display a unique STL number. Currently no operational national register. (2026-10-23 verified; sources [DETE short-term letting page](https://enterprise.gov.ie/en/what-we-do/trade-investment/tourism/short-term-letting/), [DETE release 6 Oct 2026](https://enterprise.gov.ie/en/news-and-events/department-news/2026/october/20261006.html), [Fáilte Ireland STLR page](https://www.failteireland.ie/registration-and-grading/short-term-letting-register-(STLR).aspx), [Oireachtas bill register](https://api.oireachtas.ie/v1/legislation?limit=400&bill_year=2026))

### Local short-let rules

- **Short-let planning rules (post-RPZ)**: RPZ designations ended 1 Mar 2026. PDA 2000 s.3A, as amended by the Residential Tenancies (Miscellaneous Provisions) Act 2026 s.30 (in force 1 Mar 2026, S.I. 67/2026), makes short-term letting (≤21 consecutive nights) of a house, part of a house or unit a material change of use **nationwide**. S.I. 130/2026 extended the principal-private-residence exemption nationwide: not more than 4 bedrooms, subject to conditions, or the whole PPR for up to 90 days cumulative while temporarily absent (per DETE). S.I. 500/2026 (in operation 29 Sep 2026) adds a simplified retention application (Form 24). Confirm the property's planning status with the local authority. The 1 Dec 2026 STLR opening is a DETE-announced target (see above). (2026-10-21 verified; sources [S.I. 67/2026](https://www.irishstatutebook.ie/eli/2026/si/67/made/en/print), [S.I. 130/2026](https://www.irishstatutebook.ie/eli/2026/si/130/made/en/print), [DETE STL page](https://enterprise.gov.ie/en/what-we-do/trade-investment/tourism/short-term-letting/))
- **EU Regulation 2024/1028**: short-term rental data-sharing — applicable from 20 May 2026

### Tax on rental

- **Income tax**: progressive 20-40%
- **USC (Universal Social Charge)** + **PRSI** Class S (**4.1 % from Jan 2025; 4.2 % from 1 Oct 2025; 4.35 % from 1 Oct 2026** — gradual pension-funding increase)
- **NLWT (Non-Resident Landlord Withholding Tax)**: tenant or designated collection agent must withhold **20%** of gross rent under the NLWT system, in force since **1 July 2023** (collection agent remits within 21 days via ROS/myAccount). (2026-05-27 verified; source [Revenue.ie NLWT](https://www.revenue.ie/en/property/rental-income/nlwt/index.aspx))
- **Revenue.ie eForm 11** for self-assessment
- **Rent-a-Room scheme** (s.216A TCA 1997): up to **€14,000/yr** (2026) exempt from income tax, PRSI and USC for rooms let long-term in your sole or main residence; if gross receipts exceed the limit, the whole amount is taxed. Short-term stays via B&Bs, guesthouses or online booking sites do not qualify. Budget 2027 (Finance (No. 2) Bill 2026 s.16, **NOT enacted as of 2026-10-23**) would raise the limit to **€16,000 from 1 Jan 2027** (main residence and any auxiliary dwelling combined) and extend the relief, for 27 Jul 2026 – 31 Dec 2030, to rooms in an **auxiliary dwelling** in the grounds of the main residence (32–45 m², installed after 27 Jul 2026, per the Department of Finance). (2026-10-23 verified; sources [Revenue Rent-a-Room — what type of residence qualifies](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/land-and-property/rent-a-room-relief/what-type-of-residence-qualifies.aspx), [Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))

---

## Section: `--work=<profession>`

### Sources

- **Jobs.ie**, **Indeed.ie**, **LinkedIn IE**, **IrishJobs.ie**
- **Department of Social Protection** — INTREO offices: `https://www.gov.ie/en/organisation/department-of-social-protection/`
- **Profession bodies**: Engineers Ireland, RIAI, Law Society of Ireland, RICS Ireland, Medical Council, etc.

### Self-employment

- **Sole trader**: register at **Revenue** + Companies Registration Office (if business name)
- **Limited company**: min €1 capital
- **PRSI Class S** for self-employed
- **VAT registration**: from **€42,500 services / €85,000 goods** (2025-2026)
- **Tax return Form 11** annual

### Salary benchmarks (2025)

- Median annual gross:
  - Dublin: ~€48,000–€68,000
  - Cork / Galway: ~€42,000–€58,000
  - Smaller cities: ~€36,000–€48,000
- **National minimum wage**: €14.15/hr (from 1 Jan 2026); €13.50 (2025); €12.70 (2024) (2026-07-03 verified; source gov.ie / DETE)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **OPW (Office of Public Works) Flood Maps** | `https://www.floodinfo.ie/` | Interactive flood hazard maps |
| **Climate Ireland (EPA)** | `https://www.climateireland.ie/` | Climate adaptation |
| **Met Éireann** (meteorology) | `https://www.met.ie/` | Climate, weather, **storm naming** |
| **GSI (Geological Survey Ireland)** | `https://www.gsi.ie/` | Geology, **radon, sinkholes** |
| **EPA Radon Map** | `https://www.epa.ie/environment-and-you/radon/` | Radon affected areas |
| **MeteAlarm + Storm Naming** | per Met Éireann | Severe weather warnings |
| **Defective Concrete Block Scheme (DCBS)** | `https://www.gov.ie/en/department-of-housing-local-government-and-heritage/campaigns/defective-concrete-blocks-grant-scheme/` | Mica/pyrite remediation |

### Specific risks

- **Flooding**: significant — Cork (2009 + 2024), Limerick, Galway, Athlone (Shannon basin)
  - **Storm Éowyn 24 January 2025**: record damage; Met Éireann red warnings; M50 closed; 1M+ without power
  - **Storm Bert** + **Storm Babet** 2023-2024
- **Coastal erosion**: west coast (Atlantic), east coast (storm surges)
- **Storms**: Atlantic depressions; **Storm Éowyn 2025** record damage; storm naming since 2015
- **Earthquake**: very low — Ireland on stable shield
- **Radon**: SIGNIFICANT — Galway, Sligo, Mayo, parts of Donegal, Wicklow have **High Radon Areas**
  - **EPA reference level**: 200 Bq/m³ (homes)
  - **Mandatory testing zones** progressively expanding
- **Pyrite + Mica**: **Defective Concrete Block scandal**:
  - 2017 onwards
  - **~5,000+ homes affected** in Mayo, Donegal, parts of Sligo (and Limerick, Clare)
  - **DCBS scheme**: state-funded remediation up to €420,000 per home; 2024-2025 expansions
- **Bog subsidence**: peat-soil areas (Midlands, parts of West)
- **Coastal flooding** + sea-level rise

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Solid-wall construction, no DPC, lead, no insulation |
| **1900–1960s** | Cavity-wall variability, asbestos cement |
| **1970s–1990s** | Standard cavity-wall, some asbestos |
| **2000s+** | Building Regulations strict |
| **2005-2017 (mica era)** | **Defective concrete blocks** — Mayo/Donegal/Sligo specifically |
| **Post-2014** | Strict; **NZEB (Near Zero Energy Buildings)** since 2021 |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **BER** (Building Energy Rating) | Required since 2009 | 10 years |
| **Title (Folio or Deed)** documentation | At sale | Per case |
| **LPT clearance** | Tax compliance | Annual |
| **Survey** strongly recommended | Pyrite/Mica check in Mayo/Donegal especially | Per case |
| **Engineer's report** | Recommended for older + suspected defective block | Per case |
| **PSDP / safety file** | Buildings post-2006 | Per case |

### Climate change projections (Climate Ireland)

- +1.5–3.5 °C by 2050 (RCP scenarios)
- Sea-level rise: +20–80 cm by 2100
- Increased winter rainfall + summer drying
- More extreme storm events
- Coastal flooding risk elevated

---

## Section: `--mains`

### Sources

- **Uisce Éireann (Irish Water)**: `https://www.water.ie/` — national water utility (since 2014, formerly Irish Water; renamed 2023)
- Local authority sewer/drainage support
- **Group Water Schemes (GWS)** — rural community water supply systems (~7% of population)

### Verification

- Most populated areas: **Uisce Éireann mains** universal
- Rural west coast / Connemara / Mayo / Donegal: often **GWS or own well + septic**
- **Septic Tank Inspection Scheme** since 2013 — registered + inspected
- **DBO concerns** (septic discharge to surface water) — must be compliant under Water Services Acts 2007-2017

### Costs

| Scenario | Cost (€) |
|---|---:|
| Uisce Éireann connection | 5,000–15,000 |
| Mains-line extension | 15,000–60,000+ |
| Septic compliant replacement | 6,000–18,000 |
| Group Water Scheme connection | 3,000–10,000 |
| Bored well | 5,000–12,000 |

---

## Cost benchmarks (IE 2026)

| Work | Cost (€) |
|---|---:|
| BER cert | 150–300 |
| Solicitor (conveyancing) | 1,500–2,500 |
| Searches + Land Registry | 100–910 |
| Engineer's report | 300–600 |
| Stamp duty (residential, €400k) | 4,000 |
| **Total transaction cost (residential primary, ≤€1M)** | **~2–4%** of price |
| **Total transaction cost (residential >€1.5M)** | **~7–9%** |
| **Total transaction cost (commercial)** | **~9–10%** |
| **Pyrite/Mica remediation** | **100,000–420,000+** (DCBS-eligible) |
| Septic to mains | 5,000–15,000 |
| Roof slate (200 m²) | 25,000–50,000 |
| Energy retrofit (Class C → A) | 30,000–80,000 |
| Radon mitigation | 1,500–5,000 |
| Asbestos removal | 1,500–8,000 |

## Active fiscal incentives (2025-2026)

- **Help-to-Buy (HTB)**: rebate for first-time buyers of a new home, the lesser of **€35,000**, 10% of the price (completion value for self-builds) and income tax + DIRT paid over the prior 4 years, for contracts or first self-build drawdowns **7 Oct 2026 – 31 Dec 2029** (€30,000 cap 23 Jul 2020 – 6 Oct 2026). The €35,000 cap is Budget 2027, in Finance (No. 2) Bill 2026 s.17 (amending s.477C TCA 1997), **NOT enacted as of 2026-10-23**. (2026-10-23 verified; sources [Revenue.ie HTB — how much can you claim](https://www.revenue.ie/en/property/help-to-buy-incentive/how-much-can-you-claim.aspx), [Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))
- **First Home Scheme** (shared equity): up to 30% of price; reduces mortgage burden
- **Local Authority Affordable Purchase (LAAP)**: discounted home purchase
- **SEAI Better Energy Homes**: heat pump, insulation, solar grants
- **Better Energy Warmer Homes**: free upgrades for low-income
- **Defective Concrete Blocks Scheme (DCBS)**: up to €420,000 remediation
- **Rent Tax Credit**: €1,000 (single) / €2,000 (jointly assessed) for 2026 — extended to end of 2028 (Budget 2026). Budget 2027 proposes **€1,150 / €2,300 for 2027 and 2028**, other conditions unchanged (Finance (No. 2) Bill 2026 s.4, amending s.473B TCA 1997; **NOT enacted as of 2026-10-23**). (2026-10-23 verified; sources [Revenue.ie Rent Tax Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/land-and-property/rent-credit/index.aspx), [Explanatory Memorandum](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf))
- **Mortgage Interest Tax Credit**: relief on 2025-2026 interest increase vs 2022; 2025 max €1,250/property, 2026 max €625/property (tapering out; per Citizens Information Budget 2026 — confirm at Revenue.ie). (2026-07-03 verified)

## Common listing platforms

- **Daft.ie** — biggest
- **MyHome.ie** — second
- **Sherry FitzGerald, DNG, Savills, REA, Lisney, Hooke & MacDonald, Coonan**

## Caveats unique to IE

- **Eircode** (since 2015) — most reliable address identifier; many older systems still use townland+county
- **Tailte Éireann merger 2023** — consolidated Property Registration Authority + Ordnance Survey + PSRA — historic landings under different systems
- **No Irish FHL regime** — short-term guest income is not Case V rental income: Revenue taxes it under Case IV (occasional) or Case I (trade); DAC7 platform reporting from 2024; Short-Term Letting Register (STLR): DETE announces opening 1 Dec 2026 with registration by 31 Dec 2026, but the enabling Bill, published by the Government on 6 Oct 2026, was not initiated in the Oireachtas as of 2026-10-23 (see Short-let section)
- **LPT revaluation 2026-2030** — new bands, base rate 0.0906%, 96% stay in band
- **Pyrite/Mica defective blocks scandal** — Mayo, Donegal, parts of Sligo, Clare, Limerick
  - DCBS up to €420,000 remediation
  - Some properties uninhabitable
  - Engineer survey strongly recommended in affected counties
- **Folio vs Deed registration** — Dublin city often Deed; rest of country Folio. Different processes.
- **Group Water Schemes**: rural water often community-managed (separate from Uisce Éireann)
- **Capital Acquisitions Tax (CAT)** on inheritance/gifts — important for family transfers
- **Help-to-Buy (HTB)** scheme for first-time buyers (€30k rebate cap to 6 Oct 2026; €35k from 7 Oct 2026 under Finance (No. 2) Bill 2026, not enacted)
- **First Home Scheme + LAAP** combined creates complex affordability math
- **Ribbon development restrictions** in many counties (rural one-off houses)
- **An Bord Pleanála** appeals process can stall sales/extensions
- **Storm Éowyn 24 January 2025** as recent reform-driver event
- **No NPPR / Household Charge anymore** — recurring charges are LPT, plus VHT on vacant dwellings and RZLT on in-scope zoned serviced land (Derelict Property Tax proposed in Finance (No. 2) Bill 2026, not enacted)
- **Rent-a-Room scheme** €14,000/yr tax-free (2026; €16,000 from 2027 proposed in Finance (No. 2) Bill 2026, not enacted) — long-term lodgers only, not short-term guests
- **Stamp duty 6% above €1.5M** introduced 2024
- **Bulk-purchase 15% stamp duty** anti-investor measure (10+ residential properties, apartments excluded)

## Reddit / forum sources

- **r/ireland** — biggest community
- **r/AskIreland**, **r/IrishTrucks**
- **r/PersonalFinanceIreland** — mortgage + tax discussion
- **r/Galway**, **r/Cork**, **r/Dublin**
- **Boards.ie** forum — Property + AAM
- **AskAboutMoney.com** — financial advice
- **Daft Reports** — quarterly market analysis

## Verification authorities

| Authority | When to call |
|---|---|
| **Tailte Éireann** | Title verification, Folio/Deed |
| **Local authority planning** | Permits, planning history |
| **Local authority building control** | Building regs compliance |
| **Local authority LPT** | Property charge |
| **Uisce Éireann** | Mains drains |
| **OPW** | Flood risk |
| **GSI** | Radon, geology |
| **Revenue.ie** | LPT, CGT, CAT |
| **RTB** | Tenancy registration |

## Source URL templates

| Source | URL pattern |
|---|---|
| Tailte Éireann | `https://tailte.ie/` |
| Property Price Register | `https://www.propertypriceregister.ie/` |
| Daft.ie | `https://www.daft.ie/<county>/` |
| MyHome.ie | `https://www.myhome.ie/` |
| OPW Flood Maps | `https://www.floodinfo.ie/` |
| Climate Ireland | `https://www.climateireland.ie/` |
| GSI (radon, geology) | `https://www.gsi.ie/` |
| EPA Radon | `https://www.epa.ie/environment-and-you/radon/` |
| Revenue.ie LPT | `https://www.revenue.ie/en/property/local-property-tax/` |
| RTB rental register | `https://www.rtb.ie/` |
| Uisce Éireann | `https://www.water.ie/` |
| Met Éireann | `https://www.met.ie/` |
| BER register | `https://ndber.seai.ie/PASS/BER/Search.aspx` |
| TII traffic | `https://www.tii.ie/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; the STLR row and the `--rental` IE row were fully re-verified and re-stamped 2026-09-18 per the Failte Ireland STLR page + the Oireachtas bill register — the rest of the playbook keeps the 2026-07-03 date). Rent-control and STR-register (rental) and apartment-VAT (tax) tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Budget 2027 / Finance (No. 2) Bill 2026 measures (CGT, HTB, CAT thresholds, Rent Tax Credit, Rent-a-Room, RZLT, Derelict Property Tax; all NOT enacted as of 2026-10-23), the short-let income classification and the STLR Bill publication re-verified 2026-10-23 against the Bill as initiated, its Explanatory Memorandum, Revenue.ie and DETE.
**Coverage check**: pricing, traffic, tax (LPT 2026 + stamp duty + VHT + RZLT; Derelict Property Tax and Budget 2027 measures labelled as Bill), rental, work, risks (incl. mica/pyrite + Storm Éowyn), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for LPT 2026-2030 cycle (gov.ie + Revenue.ie + irishtaxhub all confirm 0.0906% rate, 1 Nov 2025 valuation, 20% band widening, 96% stay-in-band); HIGH for stamp duty 6% above €1.5M from 2024; HIGH for DCBS €420k cap. MEDIUM for Storm Éowyn long-term insurance/property pricing impact (still emerging).

## Extension TODOs

- [ ] Per-county LPT LAVL adjustments (post-2026 revaluation)
- [ ] Pyrite/Mica defective block scheme (DCBS) eligibility per address
- [ ] Per-county RPZ maps + rent caps
- [ ] Group Water Scheme verification per address
- [ ] STLR registration workflow (Fáilte Ireland register: DETE-announced opening 1 Dec 2026, deadline 31 Dec 2026; Bill published 6 Oct 2026, not initiated in the Oireachtas as of 2026-10-23)
- [ ] Folio vs Deed system per county
- [ ] EU 2024/1028 Irish implementation (Regulation directly applicable since 20 May 2026; national register via the Short-Term Letting and Tourism Bill)
- [ ] Help-to-Buy + LAAP + First Home Scheme decision tree
- [ ] Storm Éowyn 2025 affected property zones
- [ ] Tailte Éireann post-merger lookup workflows
