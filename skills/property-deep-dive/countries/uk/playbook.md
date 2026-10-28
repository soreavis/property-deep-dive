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

- **HM Land Registry Price Paid Data** (FREE, official sales since 1995): `https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads`
- **Land Registry Search for Free**: `https://search-property-information.service.gov.uk/` — title summary
- **Office for National Statistics (ONS) — Private rent and house prices, UK** (formerly the "UK House Price Index" bulletin — renamed): `https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/privaterentandhousepricesuk/latest`
- **Registers of Scotland** sale prices: `https://www.ros.gov.uk/`
- **Land & Property Services NI** (LPS): `https://www.nidirect.gov.uk/articles/valuation-domestic-properties-rates`
- **Bank of England** mortgage statistics. Macroprudential limit on high loan-to-income mortgages (4.5x income or more): from 28 Oct 2026 the 15% limit applies to aggregate new lending only — the firm-level cap is removed, so one lender may exceed 15% while the market stays within it; whether a lender offers 4.5x+ loans remains its own decision (2026 data, source [Bank of England PRA PS19/26](https://www.bankofengland.co.uk/prudential-regulation/publication/2026/october/high-loan-to-income-lending-policy-statement))
- **Council Tax band lookup**: `https://www.gov.uk/council-tax-bands`

### Listing platforms

- **Rightmove** — biggest: `https://www.rightmove.co.uk`
- **Zoopla** — second + Zed-Index: `https://www.zoopla.co.uk`
- **OnTheMarket**: `https://www.onthemarket.com`
- **PrimeLocation** (high-end)
- **PropertyData** (paid analytics)

### Price benchmarks (≈ April 2026 data)

| Region | est. £/m² (apt) | est. £ (semi-detached house) |
|---|---:|---:|
| **London Zone 1-2** | ~8,000–18,000+ | ~800,000–2,500,000+ |
| **London Zone 3-6** | ~5,000–10,000 | ~500,000–1,200,000 |
| **Manchester / Birmingham core** | ~3,200–5,000 | ~280,000–550,000 |
| **Edinburgh / Bristol** | ~4,000–6,500 | ~400,000–800,000 |
| **Glasgow / Liverpool / Leeds** | ~2,500–4,000 | ~220,000–400,000 |
| **Smaller cities** | ~1,800–3,200 | ~180,000–320,000 |
| **Rural England (S/SW)** | ~2,500–4,500 | ~350,000–650,000 |
| **Rural Wales / Scotland / NI** | ~1,200–2,500 | ~150,000–300,000 |

Ranges are est. blended indicators triangulated from the ONS "Private rent and house prices, UK" bulletin (latest) + Rightmove/Zoopla asking data — verify per-postcode against HM Land Registry Price Paid Data. (ONS reports UK average house price ~£270,000, +3.8% in the 12 months to April 2026, provisional; 2026-07-03 verified.)

### Compute

1. £/m² = price / **GIA (Gross Internal Area)** — UK standard; check EPC for verified m²
2. **Leasehold trap**: lease <80 yrs reduces value 10–30% (marriage value); <60 yrs near unmortgageable
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

- **Department for Transport (DfT) — Road Traffic Statistics**: `https://roadtraffic.dft.gov.uk` — interactive AADT count points
- **TfL** (London transport flow + count maps): `https://tfl.gov.uk/info-for/open-data-users/our-open-data`
- **Transport Scotland**, **Transport for Wales**, **NI Department for Infrastructure**
- OSM `highway`: motorway / A-road / B-road / unclassified

### Key term

**AADT (Annual Average Daily Traffic)** — vehicles/day at count point.

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
- 2025-2026 est. bill ranges (exact bill varies by council — confirm via the gov.uk band lookup above and the council's own band-charge table):
  - Band A: est. £1,100–£1,800/yr
  - Band D (median): est. £1,800–£2,400/yr
  - Band H: est. £4,000–£8,000+/yr
- **NI**: domestic rate = capital value × (district + regional rate), typically 0.7–1.0% capital value
- Single-person discount: 25% (must apply)
- Empty-home premium up to **+100%** since **1 April 2024** (qualifying period reduced 2y → 1y); second-home premium up to **+100%** since **1 April 2025** (Levelling-up & Regeneration Act 2023; council discretion; councils had to resolve before 31 Mar 2024 to apply from 1 Apr 2025). (2026-05-27 verified; source [gov.uk Council Tax premiums guidance](https://www.gov.uk/government/publications/long-term-empty-homes-and-second-homes-council-tax-premiums-and-exceptions/guidance-on-the-implementation-of-the-council-tax-premiums-on-long-term-empty-homes-and-second-homes))
- **High Value Council Tax Surcharge ("mansion tax")** — announced Autumn Budget 2025 (26 Nov 2025): from **April 2028** (operative date 1 Apr 2028), England only, annual owner-paid charge on homes valued (in 2026) at £2M or more: £2,500 (£2M–£2.5M) / £3,500 (£2.5M–£3.5M) / £5,000 (£3.5M–£5M) / £7,500 (>£5M), CPI-uprated from 2029-30. Valuation Office targeted valuation exercise (April 2026 valuation date) to identify homes in scope; owners see draft bands in autumn 2027, first bills March 2028; revaluation 5-yearly (next 2033); challenge, then appeal to the Valuation Tribunal for England. Government response to the design consultation published at Budget 2026 (28 Oct 2026): deferral until change of ownership **confirmed** for owners with household income of £35,000 or less, savings of £16,000 or less, or a household member meeting disability criteria (interest charged, rate to be set in regulations); exemptions and discounts of up to 100% for e.g. care homes, student halls, registered social housing, working farmhouses and developer-owned new builds (full list in secondary legislation); a **100% premium** on homes left substantially unfurnished and unoccupied for 12 months or more; **no non-UK-resident premium** (considered, not adopted). Not yet law — to be legislated in Finance Bill 2026-27 (not yet published as of 2026-10-28), secondary legislation in 2027. (2026-10-28 verified; sources [gov.uk HVCTS consultation outcome](https://www.gov.uk/government/consultations/high-value-council-tax-surcharge) + [HMT HVCTS guidance](https://www.gov.uk/government/publications/high-value-council-tax-surcharge/high-value-council-tax-surcharge) + [HMRC TIIN](https://www.gov.uk/government/publications/high-value-council-tax-surcharge-on-residential-properties/additional-council-tax-charge-on-high-value-properties))

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
- **Non-UK resident surcharge**: +2% on top
- **Bulk purchases** (6+ units): 1% reverts to commercial rate option
- **Mixed-use property**: commercial rates (lower at top end)

#### Land and Buildings Transaction Tax (LBTT) — Scotland

| Band | Rate | ADS surcharge (additional dwelling) |
|---|---:|---:|
| £0–£145,000 | 0% | 8% |
| £145,001–£250,000 | 2% | 8% |
| £250,001–£325,000 | 5% | 8% |
| £325,001–£750,000 | 10% | 8% |
| £750,001+ | 12% | 8% |

- ADS raised to **8%** in December 2024 (from 6%)

#### Land Transaction Tax (LTT) — Wales

- 0% up to £225,000; progressive thereafter
- Higher rates (additional dwelling): +5% surcharge (since Dec 2024)

### Conveyancing fees

- **Solicitor / licensed conveyancer**: est. £1,000–£2,500 (2026 market range)
- **Searches** (Local, Drainage & Water, Environmental, Chancel): est. £200–£500 (2026 market range)
- **Land Registry fee**: £20–£910 sliding scale by price band — statutory; confirm current scale at HM Land Registry (Registration Services fees)
- **Survey** (Level 2 HomeBuyers / Level 3 Building): est. £400–£1,500 (2026 market range)
- **Mortgage broker / lender fees**: est. £0–£1,000 (2026 market range)

### Total transaction cost (buyer side)

- **First-time buyer ≤£300k (England)**: ~1–2% of price
- **Mover, single home, ≤£500k**: ~3–5%
- **Second home / BTL ≤£500k**: ~8–12%
- **High-value (£1M+)**: 8–18%

### Capital gains tax (CGT)

- **Principal Private Residence (PPR) relief**: full exemption for owner-occupied primary
- Investment property: 18% (basic-rate band) / **24%** (higher-rate band) — higher rate cut from 28 % → 24 % on **6 April 2024** (FA 2024); the 30 Oct 2024 alignment was for non-residential / general CGT, not residential. (2026-05-27 verified; source [gov.uk CGT rates and allowances](https://www.gov.uk/capital-gains-tax/rates))
- Annual allowance: £3,000 (2024-25 through 2026-27)
- **FA 2025 — Non-dom abolition + IHT residence-based (LTR test)**: from **6 April 2025**, the non-domiciled tax regime is abolished. New 4-year Foreign Income & Gains (FIG) regime for new arrivals. IHT shifts from domicile-based to residence-based: a UK-resident individual is a Long-Term Resident (within scope of IHT on worldwide assets) once UK-resident for ≥10 of the previous 20 tax years. Tail period on departure: 3 years (10–13 yr residency) up to 10 years (20+ yr residency). LTR status resets after 10 consecutive non-resident years. (2026-05-27 verified; source [Finance Act 2025 — legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2025/8))

### VAT

- Standard 20%
- Residential resale: VAT-exempt
- New build: zero-rated for buyer (developer recovers VAT)
- Commercial conversions to residential: 5% reduced rate

### Future risk

- **Council Tax revaluation** repeatedly proposed (still based on 1991 values in England) — no firm date
- **Leasehold reform** — LAFRA 2024's valuation reforms (incl. **marriage-value abolition**) are enacted but NOT yet commenced (High Court dismissed freeholders' JR 24 Oct 2025; Court of Appeal granted permission to appeal 1 Apr 2026; MHCLG (2 Jul 2026) says the reformed valuation regime comes into force only after drafting flaws are fixed in the Commonhold and Leasehold Reform Bill; the deferment and capitalisation rates must also be set — MHCLG valuation-rates consultation published 15 Jul 2026, extended to close 21 Oct 2026, rates then need secondary legislation). Separately, the draft **Commonhold and Leasehold Reform Bill** was published 27 Jan 2026 (Written Statement HCWS1278) for pre-legislative scrutiny; Bill announced in the King's Speech **13 May 2026**, not yet introduced as of 21 Oct 2026 (the PM has said before Christmas 2026, per Leasehold Advisory Service news; govt told the HCLG Committee it would miss the 27 Jul 2026 deadline to respond to the Committee's report) — caps existing-flat ground rents at **£250/yr** (falling to a peppercorn after 40 years — govt position restated 2 Jul 2026; HCLG Committee asked govt to justify 40 yrs over a 20-yr transition and judged a late-2027 cap commencement possible vs govt estimate of late 2028), makes commonhold the default tenure for new flats and abolishes forfeiture (making commonhold the default outcome of collective enfranchisement and creating an independent managing-agent regulator are HCLG Committee recommendations, not draft-Bill provisions). (2026-07-03 verified; source [Commons Library CBP-10653](https://commonslibrary.parliament.uk/research-briefings/cbp-10653/); King's Speech, Court of Appeal permission, commencement dependency, 40-yr / late-2027 vs late-2028 positions and Bill non-introduction re-verified 2026-10-21 against the MHCLG quid-pro-quo consultation (2 Jul 2026), the HCLG Committee report, the MHCLG valuation-rates consultation (15 Jul 2026), Leasehold Advisory Service news and the Parliament Bills register)
- **CGT rate increases** discussed at Spring 2025 Budget — currently stable
- **Stamp duty**: Budget 2026 (28 Oct 2026) made no change to residential SDLT rates, surcharges or first-time buyer relief — the [OOTLAR Annex A](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances) tables still carry the 1 April 2025 rates, the 5% additional-dwelling and 2% non-resident surcharges and first-time buyer relief to £300,000 (homes ≤£500,000); its only SDLT measures are technical (no SDLT on rent under assured tenancies from 1 May 2026, group relief, Local Government Pension Scheme relief) (2026-10-28 verified)

---

## Section: `--rental`

### Long-term residential

- **Assured Shorthold Tenancy (AST)** — England/Wales standard
- **Renters' Rights Act 2025** — Royal Assent **27 October 2025**; s21 "no-fault" evictions **abolished 1 May 2026** ("big bang" main commencement, SI 2026/421 reg 2(a); existing ASTs converted to assured periodic tenancies). Possession claims on a pre-1-May-2026 s21 notice had to be issued by the **earlier of the time left on the notice or 31 July 2026** — that window **closed 31 Jul 2026** (MHCLG guidance updated 1 Aug 2026: no new claims on pre-1-May s21/s8 notices; claims issued on or before 31 Jul continue) (2026 data, source [gov.uk](https://www.gov.uk/guidance/giving-notice-of-possession-to-tenants-before-1-may-2026)); Commencement No. 3 (SI 2026/638) brought local-authority financial penalties for category 1 hazards into force 22 Jun 2026; remaining provisions commence in later phases (MHCLG roadmap) — next is the PRS Database: draft Private Rented Sector Database Regulations 2026 (laid 9 Sep 2026, draft affirmative, not yet made as of 2026-10-21) bring landlord and dwelling registration in region by region from 15 Dec 2026 (West Midlands) to 15 Aug 2027 (South West) (2026-10-21 verified, source [draft PRS Database Regulations](https://www.legislation.gov.uk/ukdsi/2026/9780348286861)). (2026-07-03 verified; sources [Renters' Rights Act 2025](https://www.legislation.gov.uk/ukpga/2025/26) + [SI 2026/421](https://www.legislation.gov.uk/uksi/2026/421/contents/made))
- **Tenancy deposit scheme** (TDS / DPS / mydeposits) mandatory
- **Right to Rent** (immigration check) mandatory in England
- **MEES (private rented sector, England and Wales)** — all PRS tenancies must meet **EPC C by 1 Oct 2030** (single compliance date, new + existing; Warm Homes Plan / DESNZ response 21 Jan 2026). Cost cap **£10,000** per property (exemption then registrable, valid 10 yrs; qualifying spend since 1 Oct 2025 counts). **Property Value Adjustment**: homes valued <£100k → cap is the lower of £10k or 10% of value. EPC C (EER) on an EPC issued before **1 Oct 2029** stays compliant until that EPC expires/is replaced; the Home-Energy-Model dual-metric standard applies thereafter. Not yet law: needs new powers by Act of Parliament plus an SI the govt aims to bring into force in 2027; reformed Home-Energy-Model EPCs now launch in the second half of 2027 (moved from Oct 2026, gov.uk 9 Mar 2026). Until 1 Oct 2030 the current standard stays EPC E with a £3,500 cap. (2026-10-21 verified; source [gov.uk PRS MEES consultation response](https://www.gov.uk/government/consultations/improving-the-energy-performance-of-privately-rented-homes-2025-update))

### Short-let (Airbnb / holiday let)

**FHL (Furnished Holiday Lettings) regime ABOLISHED**:
- **Abolition: 1 April 2025** (companies) / **6 April 2025** (individuals)
- Old reliefs gone: capital allowances, mortgage interest deductibility, gift hold-over, BADR, profit-sharing flexibility for spouses
- Now treated as **standard property income** — same as long-let

### Local short-let rules

- **London**: 90-day cap per primary residence (Greater London Authority Act 2015)
- **Edinburgh**: short-let control areas — license required since Oct 2023
- **Wales**: licensing scheme proposed (Welsh Government 2025)
- **Northern Ireland**: registration required for tourism accommodation
- **EU 2024/1028 STR regulation**: NOT applicable (UK post-Brexit)

### Tax on rental

- **From 6 April 2027**: property income taxed at dedicated property rates, **ENACTED** by Finance Act 2026 s.6 (new ITA 2007 s.6D, effect for 2027-28 and later years per s.6(8)) + s.7 at basic 22% / higher 42% / additional 47% (2pp above main rates; announced at Autumn Budget 2025). **Budget 2026 (28 Oct 2026) announced a further 2pp: basic 24% / higher 44% / additional 49% from 6 April 2027** (England, Wales and NI; Scotland and Wales have been given the ability to set their own property rates), to be legislated in Finance Bill 2026-27 — **not yet law** (Bill text not published as of 2026-10-28), so the statute still reads 22/42/47 until it passes. Finance-cost (mortgage-interest) relief is tied to the property basic rate (FA 2026 Sch 1 para 40; see below). (2026-10-28 verified; sources [Budget 2026 OOTLAR 1.2](https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar) + [legislation.gov.uk FA 2026 s.7](https://www.legislation.gov.uk/ukpga/2026/11/section/7); Autumn Budget 2025 announcement: [gov.uk technical note](https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note))
- Property income allowance £1,000/yr (de minimis)
- Mortgage interest restricted to a basic-rate tax credit (since 2020): 20% through 2026-27; from 2027-28 given at the property basic rate — FA 2026 Sch 1 para 40 substitutes PBR for BR in ITTOIA 2005 ss.274AA(5) and 274C(2) ([legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2026/11/schedule/1/paragraph/40), 2026-10-28 verified): 22% as enacted, **24%** if the Budget 2026 rise is enacted — the [Budget 2026 policy costings](https://assets.publishing.service.gov.uk/media/6ae1883fe4367e5c8b0467df/AB26_Policy_Costing.pdf) (p.74) say finance cost relief "will continue to be aligned to the property basic rate" (24% is derived from that alignment, not printed as a relief rate)
- ATED (>£500k single dwellings owned by company): annual charge
- VAT 20% on furnished holiday let with serviced element

---

## Section: `--work=<profession>`

### Sources

- **gov.uk Find a Job**: `https://findajob.dwp.gov.uk/`
- **Indeed.co.uk**, **LinkedIn UK**, **Reed.co.uk**, **Totaljobs**, **CV-Library**
- **Profession bodies**: RIBA, GMC, NMC, ACCA, RIBA, Bar Council, etc.

### Self-employment

- **Sole trader**: HMRC self-assessment + Class 2 (£3.45/wk if profits >£12,570) + Class 4 NI (6% on £12,570–£50,270; 2% above) — 2024-25 HMRC rates; verify at HMRC (National Insurance rates and letters)
- **Limited company**: Companies House registration; corporation tax 19–25% (2024-2026)
- **VAT registration**: from £90,000 turnover (2024)
- **Personal allowance**: £12,570 (frozen until 2028)
- **IR35** (off-payroll working) rules for contractors via PSC

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Environment Agency long-term flood risk** | `https://check-long-term-flood-risk.service.gov.uk` | Postcode flood risk |
| **SEPA (Scotland) flood maps** | `https://map.sepa.org.uk/floodmap/map.htm` | Scotland flood |
| **Natural Resources Wales** | `https://naturalresources.wales/flooding/` | Wales flood |
| **DfI Rivers (NI)** | `https://www.infrastructure-ni.gov.uk/topics/rivers-and-flooding` | NI flood |
| **Coal Authority** | `https://www2.groundstability.com/` | Coal mining search (former mining areas) |
| **HSE COMAH** | `https://www.hse.gov.uk/comah/` | Seveso-equivalent industrial sites |
| **UK Health Security Agency Radon** | `https://www.ukradon.org` | Radon affected areas postcode lookup |
| **British Geological Survey** | `https://www.bgs.ac.uk/` | Geology, sinkholes, ground stability |
| **Met Office** | `https://www.metoffice.gov.uk/` | Weather, climate |
| **DEFRA air quality** | `https://uk-air.defra.gov.uk/` | Air pollution |

### Specific risks

- **Flooding** — major risk:
  - Tidal: Thames, Severn, Humber estuaries; East Anglian coast
  - River: Yorkshire (2007, 2015, 2019), Cumbria (Storm Desmond 2015)
  - Surface water: urban areas, storm drains
- **Subsidence**: clay soils (London, SE England); 2022 + 2023 + 2024 droughts elevated claims
- **Coastal erosion**: East Yorkshire (Holderness), Norfolk, North Wales
- **Radon**: Cornwall + Devon + Derbyshire + parts of Aberdeenshire — UK Radon affected area maps
- **Coal mining subsidence**: South Wales valleys, Yorkshire, Notts, Durham, Lanarkshire
- **Japanese knotweed**: identified in Land Registry; mortgage-blocking
- **Storms**: Atlantic depressions; Storm Éowyn Jan 2025 (record damage), Storm Babet 2023

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Damp, no DPC, lead paint, lath-and-plaster, single-skin walls |
| **1900–1939** | Shallow foundations, lath-and-plaster, asbestos cement starts |
| **1945–1965** | Prefab/non-traditional concrete (Cornish, Wates, Airey — some condemned), asbestos |
| **1960s–1980s** | Asbestos very common (garages, soffits, AIB); High-Alumina Cement (HAC) concern; **RAAC** (reinforced autoclaved aerated concrete) — major scandal in schools/hospitals 2023-2024 |
| **1980s–2000s** | Cavity wall insulation issues (damp bridging); modern wiring; some asbestos remains |
| **Post-2010** | Building Regs Part L energy; Part E acoustic |
| **Post-Grenfell (2017)** | Cladding crisis — EWS1 form for flats >18m; recladding programme ongoing |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **EPC** (Energy Performance Certificate) | Required since 2008 | 10 years |
| **Property Information Form (TA6)** | Standard pre-contract enquiry | At sale |
| **Fittings & Contents Form (TA10)** | What's included | At sale |
| **Leasehold Information Form (TA7)** | Leasehold only | At sale |
| **Searches**: Local, Drainage & Water (CON29DW), Environmental, Chancel | Solicitor-ordered | Per case |
| **EWS1** | Required for flats in tall buildings post-Grenfell | 5 years |
| **Cavity wall insulation guarantee** | If installed | Per case |

- **MEES (private rented sector, England and Wales)** — a let property must reach **EPC C by 1 Oct 2030** (single compliance date; Warm Homes Plan / DESNZ response 21 Jan 2026). Cost cap **£10,000** per property (exemption valid 10 yrs); homes valued <£100k → cap is the lower of £10k or 10% of value. Sub-EPC-C stock faces upgrade cost or unlettability — see `--rental`. (2026-07-03 verified; source [gov.uk PRS MEES consultation response](https://www.gov.uk/government/consultations/improving-the-energy-performance-of-privately-rented-homes-2025-update))

### Climate change projections (UKCP18)

- +1.5–4.4 °C by 2050s (RCP8.5)
- Sea-level rise: +20–70 cm by 2080
- Increased flood risk + storm intensity
- Hot summers more frequent (2022 record 40.3°C)

---

## Section: `--mains`

### Sources

- **Drainage & Water search (CON29DW)** — solicitor-ordered, ~£60–£90; specifies sewer connection
- **Local water company**:
  - **Thames Water** (London + Thames Valley)
  - **Severn Trent** (Midlands)
  - **Anglian Water** (East)
  - **Yorkshire Water**, **United Utilities** (NW), **Northumbrian Water** (NE)
  - **Welsh Water (Dŵr Cymru)**, **South West Water**, **Wessex Water**, **Southern Water**
  - **Scottish Water** (Scotland)
  - **NI Water** (Northern Ireland)

### Verification

- Most urban / suburban UK = **mains drains universal**
- Rural may be **septic tank**, **cesspool**, or **package treatment plant**
- **General Binding Rules** (since Sept 2020): all septic discharges to surface water must be replaced by compliant systems
- **Septic Tank Inspection** required for Environmental Permit if discharge >2,000 litres/day

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
| Searches + Land Registry fees | 220–1,400 |
| **Total transaction cost (FTB ≤£300k)** | **~1–2%** |
| **Total transaction cost (mover, single home)** | **~3–5%** |
| **Total transaction cost (BTL/2nd home)** | **~8–12%** |
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
- **ECO4** (Energy Company Obligation): low-income energy-efficiency upgrades
- **Boiler Upgrade Scheme**: £7,500 grant for heat pumps
- **GBIS** (Great British Insulation Scheme)

## Common listing platforms

- **Rightmove** — biggest, default
- **Zoopla** — second + sold-price history
- **OnTheMarket** — alternative
- **PrimeLocation** — high-end
- **PropertyData** — paid analytics

## Caveats unique to UK

- **Leasehold trap** (flats + some new houses) — short remaining lease (<80 yrs) hugely impacts value; ground rent doubling clauses scandals
- **Cladding crisis** (post-Grenfell): EWS1 form for flats; remediation programme ongoing; some buildings remain unsellable/unmortgageable
- **RAAC concrete** (1960s–1980s) — major scandal 2023-2024 in schools, hospitals, some residential
- **Japanese knotweed** — Land Registry & TA6 disclosure; mortgage-blocking; treatment 5-yr programme
- **SDLT additional dwelling 5% surcharge** (since Oct 2024) — punitive on BTL
- **FHL abolition April 2025** — major change for short-let economics
- **Council Tax based on 1991 values** in England/Scotland (1991), 2003 in Wales — wildly outdated
- **Empty/second home premium up to +100%** since April 2024
- **Renters' Rights Act 2025** — Section 21 abolished (1 May 2026)
- **Help to Buy ended** (England, 2023) — successor **Your First Home** equity loan confirmed at Budget 2026 (28 Oct 2026) but applications not open until Feb 2027 (pre-registration by end-Dec 2026, first sales Apr 2027); the local price-cap list and full eligibility rules are not yet published — do not price it into an offer until they are (see Active fiscal incentives)
- **Northern Ireland** uses domestic rate system (capital value-based) — distinct from rest of UK
- **Scotland LBTT + ADS 8%** — punitive on additional dwelling
- **Brexit**: removed EU-resident buyer benefits; 2% non-resident SDLT surcharge

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
| **Coal Authority** | Mining search |
| **HMRC** | SDLT, CGT, FHL transition |

## Source URL templates

| Source | URL pattern |
|---|---|
| Land Registry PPD | `https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads` |
| Find Title | `https://search-property-information.service.gov.uk/` |
| Council Tax bands | `https://www.gov.uk/council-tax-bands` |
| Long-term flood risk | `https://check-long-term-flood-risk.service.gov.uk` |
| EPC register (England + Wales) | `https://find-energy-certificate.service.gov.uk/` |
| Coal Authority search | `https://www2.groundstability.com/` |
| UK Radon | `https://www.ukradon.org` |
| BGS GeoIndex | `https://www.bgs.ac.uk/map-viewers/bgs-geology-viewer/` |
| DfT traffic counts | `https://roadtraffic.dft.gov.uk` |
| Companies House | `https://www.gov.uk/government/organisations/companies-house` |
| HMRC SDLT | `https://www.gov.uk/stamp-duty-land-tax` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged). Leasehold / rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Leasehold / rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Active fiscal incentives (Your First Home, Help to Buy – Wales, First Homes) and the Bank of England / PRA high-LTI note re-checked 2026-10-21 (see shared/regulatory-watch.md). Your First Home, Help to Buy – Wales, the HVCTS note and the Bank of England / PRA high-LTI note re-checked 2026-10-28 (Budget 2026 publications and the PRA Rulebook; see shared/regulatory-watch.md). Tax on rental (property income rates, finance-cost relief) and the stamp-duty future-risk note re-checked 2026-10-28 (Budget 2026 OOTLAR, Annex A and policy costings; see shared/regulatory-watch.md). Lifetime ISA bullet added to Active fiscal incentives 2026-10-28 (SI 2026/1130, HMRC Lifetime ISA withdrawal guidance updated 28 Oct 2026, Budget 2026 OOTLAR 2.3–2.4; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for SDLT 2025 reform (gov.uk, multiple solicitor sources confirm), HIGH for FHL abolition (HMRC + Deloitte tax briefings), HIGH for cladding/RAAC programmes, HIGH for Renters' Rights Act 2025 (in force; s21 abolished 1 May 2026); MEDIUM for HVCTS implementation detail (announced Autumn Budget 2025; government response published at Budget 2026, 28 Oct 2026 — not yet legislated, Finance Bill 2026-27 pending) and the later phased Renters’ Rights commencements (MHCLG roadmap); MEDIUM for Your First Home parameters (confirmed at Budget 2026 on gov.uk; applications not open until Feb 2027 — local price-cap list and full eligibility rules not yet published).

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
