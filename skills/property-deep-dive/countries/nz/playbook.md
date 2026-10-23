# New Zealand 🇳🇿 — Property Due-Diligence Playbook

ISO2: `nz`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1010` Auckland CBD, `6011` Wellington CBD, `8013` Christchurch)
- **Admin levels**: Central government + 16 regions + 67 territorial authorities
- **Currency**: **NZD** (New Zealand dollar); 1 EUR = 1.9724 NZD (ECB reference rate, 22 Oct 2026; Jul–Oct 2026 range 1.9520–2.0121 — 2026 data, source [ECB — EUR/NZD reference rate](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-nzd.en.html))
- **Languages**: English (de facto) + Te Reo Māori (official)
- **Cadastre**: **Toitū Te Whenua / LINZ (Land Information NZ)** — fully unified national system
  - **Landonline**: `https://www.linz.govt.nz/` (lawyers/surveyors, paid)
  - **Public Land Record Search**: `https://lrs.linz.govt.nz/search/` — **$8 per record**
- **Identifier**: Record of Title (RT) reference (e.g. `WN12A/345`); supersedes older Certificate of Title
- **Ownership types**:
  - **Freehold (fee simple)** — most common
  - **Leasehold** — Cornwall Park (Auckland), Glasgow Crescent, Cashmere Hills; **99-year leases common on Māori land** under Te Ture Whenua Māori Act 1993
  - **Cross-lease** — ~10% of Auckland; clunky shared ownership of section + flat plan
  - **Unit title** — apartments, body corporate
- **Foreign-buyer ban**: Overseas Investment Amendment Act 2018 — still applies to most overseas persons. No consent needed for Australian or Singaporean citizens (residential or lifestyle land; must be ordinarily resident in NZ if the land is also otherwise sensitive) or for Australian / Singaporean permanent residents ordinarily resident in NZ ([LINZ — Buying residential property to live in](https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live), updated 6 Mar 2026). Off-the-plan apartments in large developments with a developer exemption certificate: overseas buyers may buy before construction is complete but cannot live in the apartment, and the developer may sell up to 60% to overseas people ([LINZ — Investing in apartments](https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/investing-apartments), updated 10 Sep 2025). **$5 million plus house pathway — in force since 6 Mar 2026** (Overseas Investment (National Interest Test and Other Matters) Amendment Act, Royal Assent 19 Dec 2025): Active Investor Plus (AIP), Investor 1 and Investor 2 resident-visa holders can apply for OIA consent to buy residential land with a dwelling for more than NZ$5,000,000, or land under NZ$5M where land + construction exceeds NZ$5M; the District Valuation Roll category must be residential or lifestyle (code starting R or L); land sensitive for other reasons (e.g. next to a beach, river, lake or reserve) is excluded; offers must be conditional on consent; fees NZ$2,040 (existing dwelling, price over $5M) / NZ$3,500 (all other cases); statutory timeframe 15 working days, LINZ aims to decide most within 5 (2026 data, sources: [LINZ — Investing in residential land over $5 million](https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/pathways-migrants-and-visa-holders/investing-residential-land-over-5-million), updated 27 Mar 2026; [LINZ — Reform of the Overseas Investment Act](https://www.linz.govt.nz/our-work/overseas-investment-regulation/reform-overseas-investment-act), updated 28 Aug 2026). One such property per visa holder (secondary, law firm: [Bell Gully OIA update](https://www.bellgully.com/insights/overseas-investment-act-update-door-opens-for-investor-visa-holders-buying-residential-land/), 23 Dec 2025)

## Section: `--price`

### Primary sources

- **REINZ (Real Estate Institute of New Zealand) HPI**: `https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx` — monthly, authoritative
- **Quotable Value (QV)**: `https://www.qv.co.nz/price-index/` — monthly QV House Price Index (average value + 3- and 12-month change by district); QV also carries out council rating revaluations (e.g. Kāpiti Coast, Mackenzie, Waitaki — Oct 2026 QV news), the CV basis for rates
- **Cotality NZ** (formerly CoreLogic NZ; corelogic.co.nz redirects to cotality.com): `https://www.cotality.com/nz` — separate private provider of dwelling-value and rent indices
- **Stats NZ**: `https://www.stats.govt.nz/` — house price + rental indices
- **OneRoof Property Report**: `https://www.oneroof.co.nz/` (NZ Herald)

### Listing platforms

- **Trade Me Property**: `https://www.trademe.co.nz/property` — ~39k listings
- **realestate.co.nz**: `https://www.realestate.co.nz` — industry-owned, ~35k listings
- **OneRoof** (NZ Herald) — secondary
- **Homes.co.nz** — sold-price specialty

### 2026 price benchmarks (REINZ + QV, September 2026)

| Region | Value (NZD) | Change |
|---|---:|---:|
| **National median (REINZ)** | $755,000 | -2.3% YoY |
| **National HPI (REINZ)** | 3,551 (index) | -1.5% YoY |
| **National average value (QV)** | $892,580 | -0.9% YoY; -1.5% qtr |
| **Auckland region (Tāmaki Makaurau)** | $1,159,440 (QV avg) | -2.9% YoY (QV); REINZ median -2.6% YoY |
| **Wellington City** | $872,174 (QV avg) | **-5.2% YoY** (QV); Wellington region HPI -4.5% YoY (REINZ) |
| **Christchurch (Ōtautahi)** | $805,275 (QV avg) | +4.3% YoY (QV) |
| **Canterbury region** | $715,000 (REINZ median) | +0.8% YoY; HPI +3.1% YoY (REINZ) |
| **Hamilton** | $776,357 (QV avg; release text prints $776,537) | -0.3% YoY (QV) |
| **Tauranga** | $1,050,221 (QV avg) | +2.5% YoY (QV) |
| **Dunedin** | $652,943 (QV avg) | +3.0% YoY (QV) |
| **Queenstown Lakes** | $1,994,461 (QV avg) | +5.7% YoY (QV) |

September 2026 data, sources: [REINZ — September 2026 property report release](https://www.reinz.co.nz/Web/Web/News/News-Articles/Market-updates/Measured_national_picture_continues_alongside_strong_regional_results.aspx) (14 Oct 2026); [QV House Price Index — September 2026](https://www.qv.co.nz/news/qv-house-price-index-september-2026-housing-market-showing-few-signs-of-spring-uplift/) (12 Oct 2026) + QV district series at `https://www.qv.co.nz/price-index/`. REINZ = median of the month's sales (regions); QV = average value from the QV House Price Index (cities / districts) — the two measures are not interchangeable.

### Compute

1. NZD/sqm = price / **floor area** (sqm dominant unit)
2. Cross-check **REINZ HPI** + **QV** + **Trade Me sold-price**
3. **HPI vs median**: REINZ HPI uses the SPAR (Sales Price to Appraisal Ratio) method, accounts for changes in the composition of homes sold (land area, floor area, bedrooms) and dates sales at unconditional; the raw median moves with the sales mix, so the two can diverge (Sep 2026: median -2.3% YoY vs HPI -1.5% YoY) (2026 data, source [REINZ HPI](https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx))
4. **Wellington City ~-30.6% (computed)** from its QV HPI peak: index 2,512.7 (Jan 2022, avg value $1,256,674) → 1,743.9 (Sep 2026, avg value $872,174); Auckland region ~-24.8% (computed) over the same window (2026 data, source [QV House Price Index](https://www.qv.co.nz/price-index/) district series)
5. **Convert NZD to EUR/USD** at current FX

### Key terms

- RT (Record of Title) = land title
- Cross-lease = shared title with flat plan (Auckland-specific quirk)
- Body Corporate = HOA for unit title
- LIM = Land Information Memorandum (council report)
- Bright-line = capital gains test

---

## Section: `--traffic`

### Sources

- **NZTA (Waka Kotahi) Traffic Counts**: `https://www.nzta.govt.nz/resources/state-highway-traffic-volumes`
- **AADT + heavy-vehicle %** per state-highway count site, with the last 5 years of AADT (fields `aadt1yearago`…`aadt5yearsago`, `percentheavy`): NZTA open data [State highway traffic monitoring sites](https://opendata-nzta.opendata.arcgis.com/datasets/b90f8908910f44a493c6501c3565ed2d) (CC BY 4.0, dataset updated 2026-10-09) + public map [State highway traffic monitoring – annual average daily traffic](https://experience.arcgis.com/experience/a09cd3ec9bdd4068b45c818a69601775/) (count sites + estimated traffic between sites); dual-loop counts carry a 2–5% error margin and AADT accuracy depends on sampling frequency (2026 data, source NZTA open data)
- **Council traffic data** for local roads

### Key term

**AADT** — same as US/UK.

### Verdict bands

- 🟢 < 1,000 v/d (residential, rural)
- 🟡 1,000–8,000 v/d (suburban arterial)
- 🟠 8,000–25,000 v/d (urban arterial, SH-routes)
- 🔴 > 25,000 v/d (motorways: SH1, SH16, SH20)

---

## Section: `--tax`

### Annual property tax — Council Rates

Rates = **general rate × Capital Value (CV) or Land Value (LV)** + targeted rates.

**No central property tax** — rates are local-authority-only.

| City | Annual rates (~2024-2025 est., typical — rates/figures may have changed since) |
|---|---:|
| Auckland Council | ~0.30% of CV (median ~$3,500) |
| Wellington | ~0.65% of CV (median ~$4,500) |
| Christchurch | ~0.60% (median ~$3,800) |
| Queenstown Lakes | ~0.45% (median ~$5,500) |

Figures are estimates — confirm the current year's rates demand against each council's rates schedule (Auckland Council / Wellington City Council / Christchurch City Council / Queenstown Lakes District Council).

**Rates frozen** in some councils 2024-2025 due to crisis politics — not matched to a named council annual plan; verify with the council — rates/figures may have changed since.

**Auckland — short-term letting shifts the rating category**: peer-to-peer STR moves the property onto a graduated business-rating share of general rates + CATTR once it is let 29+ nights in the 1 Jul – 30 Jun year; the Accommodation Provider Targeted Rate (APTR) itself has been suspended since 2020 and is NOT reinstated for 2026/2027. Bands and deadlines in `--rental` § Auckland (2026-08-07 verified, source: [Auckland Council — Accommodation Provider Targeted Rate](https://www.aucklandcouncil.govt.nz/en/property-rates-valuations/accommodation-provider-targeted-rate.html))

### Transaction taxes

- **NO STAMP DUTY** (abolished 1999) — UNIQUE in OECD; Te Pāti Māori proposes a 5% residential stamp duty (election proposal only — see § Future risk)
- Legal fees: $1,500–$3,000
- LIM report: $300–$500
- Building report: $500–$1,000

### Capital gains tax — BRIGHT-LINE TEST

**No general CGT in NZ** (Labour proposes a 28% CGT from 1 Jul 2027 — election proposal only, see § Future risk). But the **bright-line test** taxes residential property gains as ordinary income IF sold within the bright-line period:

| Bright-line period | When applicable |
|---|---|
| **2 years** | Property sold on/after 1 Jul 2024 (current; was 5/10) (2026-10-23 verified, source: [IRD — bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test)) |
| 5 years | Acquired 29 Mar 2018 – 26 Mar 2021, sold before 1 Jul 2024 (2024 data, source IRD) |
| 10 years (5 for qualifying new builds) | Acquired on/after 27 Mar 2021, sold before 1 Jul 2024 (2024 data, source IRD) |
| 2 years | Earlier regime for acquisitions before 29 Mar 2018 — start date not verified; verify at https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/property-sold-before-1-july-2024 |

- Bright-line period (standard purchase/sale) starts when title transfers to the buyer (generally settlement) and ends when the seller enters a binding sale and purchase agreement; off-the-plan and gifts follow different rules (2026-10-23 verified, source: [IRD — bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test))
- Main home exclusion (sales on/after 1 Jul 2024): applies only if the property was used as the main home for more than 50% of its area AND more than 50% of the bright-line period; not available if already used twice in the 2 years before the sale (2026-10-23 verified, source: [IRD — exclusions](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/exclusions-to-the-brightline-test), updated 11 Sep 2024)
- Inherited property excluded; relationship-property settlements get rollover relief, as do certain transfers to associated persons and trusts (2026-10-23 verified, source: [IRD — ownership transfers and rollover relief](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/ownership-transfers-and-rollover-relief), updated 1 Apr 2026)

### GST

- **15%** on new builds; resale exempt
- From **1 Apr 2024**: GST collected by online STR marketplaces at 15% (8.5% passed to non-GST-registered hosts) (2026-10-23 verified, source: [IRD — GST for listed services](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services), updated 14 Aug 2025)

### Interest deductibility (BTL)

**Fully restored 100% from 1 Apr 2025** (tax year ending 31 Mar 2026 onwards; 80% for 1 Apr 2024 – 31 Mar 2025) — major reversal of 2021 phase-out (2026-10-23 verified, source: [IRD — interest limitation rules](https://www.ird.govt.nz/property-interest-rules), updated 1 Apr 2026). Labour says it will not reinstate the interest denial; the Greens propose denying it again (election proposals only — see § Future risk).

### Foreign-buyer regime

**Overseas Investment Amendment Act 2018** — overseas persons need consent to buy residential land; holders of temporary, limited, interim or transit visas (student, work, visitor) and people with no visa cannot buy (2026-10-23 verified, source: [LINZ — Buying residential property to live in](https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live), updated 6 Mar 2026). Exceptions and pathways:
- AU + SG citizens — residential or lifestyle land without consent (treaty exemption); AU + SG permanent residents once ordinarily resident
- Residence class visa holders who are **ordinarily resident** (lived in NZ for at least the last 12 months + tax resident, present more than 183 days in the last 12 months); residence visa holders not yet ordinarily resident can apply for consent to buy or build one home
- Off-the-plan apartments in developments whose developer holds an exemption certificate (purchase before construction is complete) ([LINZ — Exemptions from the need for consent](https://www.linz.govt.nz/guidance/overseas-investment/apply-consent-variation-or-exemption/application-forms-and-information-sheets/exemptions-need-consent))
- **$5 million plus house pathway (in force 6 Mar 2026)**: Active Investor Plus, Investor 1 + Investor 2 resident visa holders can apply for consent to buy residential or lifestyle land (not otherwise sensitive — e.g. not on an island or beside a beach, river, lake or reserve) priced more than NZ$5m, or land + build where land + construction price exceeds NZ$5m; offer must be conditional on consent; interim fees NZ$2,040 (existing dwelling) / NZ$3,500 (all other cases); statutory timeframe 15 working days, LINZ aims for ~5 (2026-10-23 verified, sources: [LINZ — $5m pathway](https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/pathways-migrants-and-visa-holders/investing-residential-land-over-5-million), updated 27 Mar 2026; [LINZ — OIA reform](https://www.linz.govt.nz/our-work/overseas-investment-regulation/reform-overseas-investment-act), updated 28 Aug 2026; [Cabinet paper LEG-26-SUB-0001](https://www.treasury.govt.nz/sites/default/files/2026-05/cabinet-paper-leg-26-sub-0001.pdf)). One-property limit reported by [Bell Gully](https://www.bellgully.com/insights/overseas-investment-act-update-door-opens-for-investor-visa-holders-buying-residential-land/) (secondary) — not stated on the LINZ page

### Total transaction cost (buyer side)

- Resale primary: ~$3,000–$5,000 fixed (legal + searches + LIM) — **lowest in OECD**
- New build with GST: 15% + ~$3,000 fees

### Future risk

- **7 Nov 2026 general election — party proposals only**: none is government policy, introduced or legislated; any change needs coalition agreement + legislation (per [Nexia — 2026 election tax policies](https://www.nexia.co.nz/2026-election-tax-policies-new-zealand/), 28 Sep 2026, secondary; [KPMG Election 2026 party tax policy tracker](https://assets.kpmg.com/content/dam/kpmgsites/nz/pdf/2026/09/2026-election-policy-tracker-v4.pdf), updated 3 Sep 2026, secondary)
  - **Labour**: 28% CGT on profit made after 1 Jul 2027 when residential investment or commercial property is sold; family home, farms, inheritances / gifts, KiwiSaver, shares, businesses + personal items excluded; will not reinstate the interest-deduction denial
  - **Greens**: restore the 10-year bright-line + deny landlord interest deductibility; Capital Acquisitions Tax (33%) on assets / gifts received over $1,000,000 (family homes + farms exempt); 2.5% tax on net assets above $10m (family homes exempt)
  - **Te Pāti Māori**: 5% stamp duty on residential sales (first-home buyers under $1m exempt); 33% land-banking tax; 2% vacant-house tax; wealth tax 1.5–2.5% on net assets above $2m
  - **Opportunity (TOP)**: annual land value tax 1.75% urban / 0.5% rural on unimproved land value
  - **National + ACT**: no capital gains tax planned; National campaigning on no new taxes
- Foreign-buyer ban remains for most overseas persons; the $5m+ investor-visa pathway (in force 6 Mar 2026) is the carve-out — see § Foreign-buyer regime

---

## Section: `--rental`

### Long-term residential

- **Residential Tenancies Act 1986** (RTA) — tenant-protective
- **No-cause 90-day termination RESTORED 30 Jan 2025** by Residential Tenancies Amendment Act 2024 (passed 17 Dec 2024), reversing the 11 Feb 2021 abolition; also adds 42-day notice for owner/family (or employee) occupation or sale-with-vacant-possession, and 21-day tenant termination; fixed terms can be ended by either side with 90–21 days' notice before expiry; pet-related changes effective 1 Dec 2025 (written landlord consent, refusable only on reasonable grounds; pet bond up to 2 weeks' rent on top of the regular bond) (2026-10-23 verified, source: [Ministry for Cities, Environment, Regions and Transport (formerly HUD) — RTA Amendment Act 2024](https://www.hud.govt.nz/our-work/residential-tenancies-amendment-act-2024))
- **Rent increases** capped at once every 12 months (12 months after the tenancy start or the last increase), with at least 60 days' written notice (2026 data, source [Tenancy Services — Rent increases](https://www.tenancy.govt.nz/rent-bond-and-bills/rent/increasing-rent/))
- **Rental loss ring-fencing** — excess residential rental deductions cannot be offset against other income such as salary or wages; they carry forward to years with residential rental income (2026 data, source [IRD — Residential rental property deductions](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-property-deductions))
- **Healthy Homes Standards** mandatory for rentals (insulation, heating, ventilation, moisture, draught) — all rental properties must comply (2026 data, source [Tenancy Services — Healthy homes](https://www.tenancy.govt.nz/healthy-homes/))
- **Market rent data**: Tenancy Services market rent tool (bond data) — lower-quartile / median / upper-quartile weekly rent by area, dwelling type and bedrooms; updated monthly from bonds lodged over the previous six months, excluding the most recent month (2026 data, source [Tenancy Services — Market rent](https://www.tenancy.govt.nz/rent-bond-and-bills/market-rent/))

### Short-let (Airbnb, Bachcare)

#### Queenstown Lakes

- **Residential Visitor Accommodation registration** required
- **Night cap is zone-specific**: e.g. Lower Density Suburban Residential allows a cumulative 90 nights/yr from initial registration (PDP ch.7 std 7.5.18.1, Jun 2023 Decisions Version); operating beyond your zone's standards needs a resource consent - check the parcel's zone on QLDC ePlan (2026 data, source [QLDC STVA](https://www.qldc.govt.nz/services/rates-property/short-term-visitor-accommodation))
- **Rates**: no change if available to short-term guests for up to 28 days/yr cumulative; under 180 days = rated Mixed Use (+25-35%); 181-365 days = rated Accommodation (+50-80%); a Homestay = Mixed Use (+25-35%); changes apply from the next rating year beginning 1 Jul (2026 data, source [QLDC STVA](https://www.qldc.govt.nz/services/rates-property/short-term-visitor-accommodation))

#### Auckland

- Unitary Plan visitor accommodation rules
- **APTR (Accommodation Provider Targeted Rate) suspended since 2020 — NOT reinstated for 2026/2027.** The live cost is a **graduated general-rates + CATTR business uplift** on peer-to-peer STR, nights counted **1 Jul – 30 Jun** (2026-08-07 verified, source: [Auckland Council — Accommodation Provider Targeted Rate](https://www.aucklandcouncil.govt.nz/en/property-rates-valuations/accommodation-provider-targeted-rate.html))

| Nights let (1 Jul – 30 Jun) | Rating split |
|---|---|
| **up to 28** | stays 100% residential |
| **29–135** | 75% residential / 25% business |
| **136–180** | 50% residential / 50% business |
| **more than 180** | 100% business |

- **Declare before 1 Jul** to land on the first instalment bill; **remove the listing before 30 Jun** to stay residential
- Supreme Court upheld the original 2017/18–2018/19 APTR on **12 May 2023** ([2023] NZSC 53)

#### Other councils

- Wellington, Christchurch tightening discussions

### Tax on rental

- Marginal income tax on net rental
- BTL interest fully deductible (from 1 Apr 2025; the interest limitation rules applied 1 Oct 2021 – 31 Mar 2025) (2026 data, source [IRD — Rental property expenses](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it/rental-expense-deductions))
- Bright-line test on sale
- **GST $60k threshold** — register if turnover from all GST activities is over $60,000; since 1 Apr 2024 online marketplaces (e.g. Airbnb, Bookabach, Holiday Houses) collect and pay GST on short-stay accommodation booked through them (2026 data, source [IRD — GST and renting out residential property](https://www.ird.govt.nz/property/renting-out-residential-property/gst-and-renting-out-residential-property))
- **Rental loss ring-fencing** — losses cannot offset other income

---

## Section: `--work=<profession>`

### Sources

- **Work and Income (WINZ)**: `https://www.workandincome.govt.nz/`
- **Trade Me Jobs**: `https://www.trademe.co.nz/jobs`
- **Seek.co.nz** — biggest: `https://www.seek.co.nz/`
- **JobSpace** (`https://jobspace.co.nz/`; myjobspace.co.nz redirects here; NZ-owned since 2006), **Indeed NZ** (`https://nz.indeed.com/`; indeed.co.nz redirects here), **LinkedIn NZ**; JobAve ❌ DEPRECATED — jobave.co.nz does not resolve (dead on 2026-10-23); verify with Seek / Trade Me Jobs
- **Immigration New Zealand** (work visas for migrants): `https://www.immigration.govt.nz/`

### Self-employment

- **Sole trader**: IRD + GST (above $60k turnover)
- **Limited company**: Companies Office; min $1 capital
- **Working for Families** tax credits

### Salary benchmarks (2025 est.)

- Median annual gross (est. ranges, no primary source attached — verify against Stats NZ Labour market statistics (income) and current Seek / Trade Me Jobs salary data; 2025 data — rates/figures may have changed since):
  - Auckland: ~$80,000–$110,000
  - Wellington (govt): ~$85,000–$120,000
  - Christchurch / Hamilton / Tauranga: ~$70,000–$95,000
  - Smaller cities: ~$60,000–$80,000
- **Minimum wage**: **$23.95/hr from 1 Apr 2026** (previously $23.50, +45c); starting-out and training minimum wages $19.16/hr (2026-10-23 verified, source: [Employment NZ — Minimum wage rates and types](https://www.employment.govt.nz/pay-and-hours/pay-and-wages/minimum-wage/minimum-wage-rates-and-types); [MBIE — Minimum wage set for 2026](https://www.mbie.govt.nz/about/news/minimum-wage-set-for-2026))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **GeoNet** | `https://www.geonet.org.nz` | Earthquake / volcano / tsunami real-time |
| **Earth Sciences NZ** (GNS Science + NIWA merged 1 Jul 2025) | `https://www.earthsciences.nz` (legacy GNS site `https://www.gns.cri.nz` still linked from it) | National Seismic Hazard Model (2022 update raised hazard ~50% nationally; 2022 data, source GNS Science — rates/figures may have changed since) |
| **Natural Hazards Commission Toka Tū Ake** (formerly EQC) | `https://www.naturalhazards.govt.nz` | NHCover up to **$300,000 +GST** residential building cap per natural-hazard event (2026 data, source [NHC — About NHCover](https://www.naturalhazards.govt.nz/insurance-and-claims/about-nhcover/)) |
| **Natural Hazards Portal** (NHC Toka Tū Ake) | `https://www.naturalhazardsportal.govt.nz/` | Look up natural hazard insurance property claims across NZ (settled-claims map), incl. whether a home has had an NHC claim; natural hazard maps for Bay of Plenty only (pilot), more regions to be added as they become available (2026 data, source [Natural Hazards Portal](https://www.naturalhazardsportal.govt.nz/) + [settled.govt.nz — Natural hazards](https://www.settled.govt.nz/buying-a-home/researching-the-property/understanding-the-impact-of-natural-hazards/)) |
| **NIWA** (part of Earth Sciences NZ since 1 Jul 2025) | `https://niwa.co.nz` | Climate, flood, drought, sea-level rise |
| **Council hazard registers** | per council | Auckland Hazard Viewer, Wellington Hazards Mapper |

### Specific risks

#### Earthquake — EXTREME

- **NZ sits on Pacific Ring of Fire / plate boundary**
- **National Seismic Hazard Model 2022**: raised hazard estimates ~50% nationally (2022 data, source GNS Science — rates/figures may have changed since)
- **Historical major events**:
  - **Christchurch (Canterbury) 2010-11** (M7.1 Darfield 4 Sep 2010 + ML 6.3 Christchurch 22 Feb 2011 — 185 deaths, per [GeoNet](https://www.geonet.org.nz/earthquake/story/3468575); ~$40B total damage est. — verify cost with Treasury / Toka Tū Ake; insurer claims only, accumulated 2010-2011: NZ$22.9B excl. GST, NZ$32.0B inflation-adjusted (2026 data, source [ICNZ (insurance-industry body) — Cost of natural disasters](https://www.icnz.org.nz/industry/cost-of-natural-disasters/)))
  - **Kaikōura 2016** (M7.8, 14 Nov 2016 — fault rupture; local tsunami with 6.9 m run-up at Goose Bay, per [GeoNet](https://www.geonet.org.nz/earthquake/story/2016p858000); port damage; insured losses NZ$2.27B (2026 data, source [ICNZ (insurance-industry body) — Cost of natural disasters](https://www.icnz.org.nz/industry/cost-of-natural-disasters/)))
  - **Hawke's Bay 1931** (Mw 7.4–7.6 / Ms 7.8 — 256 killed, the largest loss of life of any NZ earthquake, per [GeoNet](https://www.geonet.org.nz/earthquake/story/2178228))
- **Wellington fault**: high probability of major event in coming decades
- **Auckland**: lower risk (volcanic field replaces tectonic faults)
- **NHCover** mandatory natural-disaster insurance via property insurance — covers up to **$300,000 +GST** building damage per event; land cover is limited (generally land within 8 m of the home + the main access way up to 60 m; retaining walls capped at $50,000 +GST, bridges/culverts at $25,000 +GST) (2026 data, source [NHC — About NHCover](https://www.naturalhazards.govt.nz/insurance-and-claims/about-nhcover/))

#### Volcanic

- **Taupō Volcanic Zone** — Taupō volcano last erupted ~1,800 years ago, "the most violent eruption in the world in the last 5,000 years" (2026 data, source [GeoNet — Taupō](https://www.geonet.org.nz/about/volcano/taupo))
- **Mount Ruapehu**: active stratovolcano (Whakapapa ski field); most recent eruption 25 Sep 2007; Crater Lake water ejected in eruptions causes lahars (2026 data, source [GeoNet — Ruapehu](https://www.geonet.org.nz/about/volcano/ruapehu))
- **Auckland Volcanic Field**: 53 volcanic centres; most recent eruption Rangitoto ~600 years ago; existing volcanoes are unlikely to reactivate but the field itself is young and still active — an eruption is low-probability, high-consequence (2026 data, source [GeoNet — Auckland Volcanic Field](https://www.geonet.org.nz/about/volcano/aucklandvolcanicfield))
- **Whakaari/White Island 2019** eruption (22 dead — tourists)

#### Tsunami

- Pacific Ocean origin; Kaikoura 2016 generated local tsunami
- Risk: East Coast, Cook Strait, Bay of Plenty
- Council tsunami evacuation zones mandatory

#### Flood + landslip

- Auckland Anniversary Weekend floods, 27 Jan – 2 Feb 2023 (state of emergency; insured losses NZ$1.98B over 59,189 claims, excl. GST; claims to 1 Mar 2024, source [ICNZ (insurance-industry body) — Cost of natural disasters](https://www.icnz.org.nz/industry/cost-of-natural-disasters/), table as published 2026)
- Cyclone Gabrielle, 11–17 Feb 2023 (Hawke's Bay, Tairāwhiti; insured losses NZ$1.84B over 58,848 claims, excl. GST; claims to 1 Mar 2024, source ICNZ)
- Sub-tropical climate: heavy rainfall events increasing
- Steep terrain landslip risk (Kaikoura, Wellington)

#### Coastal erosion + sea-level rise

- +20-80 cm by 2100 (NIWA SLR)
- Coastal Hazards Susceptibility (per council mapping)
- Site-specific sea-level rise projections to 2300 for every 2 km of coast, combined with vertical land movement (subsidence / uplift): NZ SeaRise programme ([searise.nz](https://searise.nz/), online tool by Takiwā) (2026 data, source [NIWA — Sea-level rise](https://niwa.co.nz/hazards/sea-level-rise))

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Lead paint, lead pipes |
| **Mid-1940s–mid-1980s** (any pre-2000 build) | Asbestos: popular building material mid-1940s to mid-1980s (settled.govt.nz); a building built before 1 Jan 2000 probably contains some asbestos materials (2026 data, source [WorkSafe — Where asbestos can be found](https://www.worksafe.govt.nz/topic-and-industry/asbestos/where-asbestos-can-be-found/)) |
| **Late 1970s–early 1980s** | Dux Quest plumbing (built or re-plumbed late 1970s–early 1980s; prone to leaking) + Weatherside cladding (popular early 1980s; prone to swelling and rot — the only full fix is replacing the cladding) (2026 data, source [settled.govt.nz — Problem building materials](https://www.settled.govt.nz/buying-a-home/researching-the-property/learning-about-problem-building-materials/)) |
| **Late 1980s–mid-2000s** | **Leaky homes crisis** — high-risk builds are mostly plaster-style monolithic cladding, especially Mediterranean style without eaves and with flat roofs: water ingress + rot (2026 data, source [settled.govt.nz — Leaky buildings](https://www.settled.govt.nz/buying-a-home/researching-the-property/learning-about-leaky-buildings/)); ~$11B+ national damage est. — verify with PwC / Dept of Building & Housing estimate |
| **Post-2003 H1** | Tightened weathertightness rules |
| **Post-2018** | Updated insulation + Healthy Homes |
| **Cross-lease titles** | ~10% Auckland — shared ownership complications |

### Mandatory at sale

| Document | Notes |
|---|---|
| **LIM (Land Information Memorandum)** | From council; ~$300-500; mandatory in practice |
| **Project Information Memorandum (PIM)** | For consents (build/extension) |
| **Body Corporate disclosure** | Unit title only |
| **Vendor warranty re weathertightness** | Leaky-building disclosure expected |
| **Healthy Homes Compliance Statement** | If letting out |

### Climate change projections

- **+1.5–4.0°C** by 2100
- **Sea-level rise**: +20–80 cm by 2100
- **Heavy rainfall**: ~+20-30% est. by 2100 (verify against NIWA / MfE projection scenario); extreme rainfall from ex-tropical cyclones up to ~30–35% higher by end of century under a high-emissions scenario (~3°C warming) (2025 data, source [Earth Sciences NZ, 7 Aug 2025](https://www.earthsciences.nz/news/rain-from-tropical-cyclones-to-increase-under-warmer-climate))
- **Drought**: increasing eastern regions
- **Insurance premiums rising** for high-risk zones

---

## Section: `--mains`

### Sources

- **Watercare** (Auckland): `https://www.watercare.co.nz/`
- **Tiaki Wai** (Wellington metro — Wellington, Hutt, Upper Hutt and Porirua; council-owned, absorbed Wellington Water from 1 Jul 2026): `https://www.tiakiwai.co.nz/` — water services charges are removed from council rates bills and billed separately by Tiaki Wai (quarterly; councils run the billing in the first year) (2026 data, source [Tiaki Wai](https://www.tiakiwai.co.nz/) + [Upper Hutt City Council, 30 Oct 2025](https://www.upperhutt.govt.nz/News/New-chapter-for-water-services-in-metropolitan-Wellington))
- **Christchurch City Council Water**, **DCC Water (Dunedin)**
- Universal in cities; rural may have rainwater tanks + septic

### Costs

| Scenario | Cost (NZD, est. — unsourced) |
|---|---:|
| Mains connection | $5,000–$15,000 |
| Septic upgrade | $15,000–$30,000 |
| Rainwater tank | $3,000–$8,000 |
| Bored well | $10,000–$25,000 |

---

## Cost benchmarks (NZ 2026)

| Work | Cost (NZD, est. — contractor-quote ranges, no primary source; verify with local quotes) |
|---|---:|
| Building report | $500–$1,000 |
| LIM report | $300–$500 |
| Solicitor / conveyancer | $1,500–$3,000 |
| Body Corporate disclosure | $300–$700 |
| **Total transaction cost (buyer)** | **~$3,000–$5,000 (lowest in OECD)** |
| Roof restoration | $5,000–$15,000 |
| Earthquake strengthening (older builds) | $30,000–$200,000+ |
| Asbestos abatement | $5,000–$30,000 |
| Leaky home remediation | $100,000–$500,000+ |
| Insulation upgrade | $5,000–$15,000 |
| Heat pump | $2,500–$5,000 |
| Solar PV (5kW) | $10,000–$15,000 |

## Active fiscal incentives (2025-2026)

- **First Home Loan**: 5% deposit via Kāinga Ora — Kāinga Ora underwrites the loan so a bank or lender can accept a 5% deposit; eligibility criteria apply (2025 data, source: [govt.nz — Financial help for first-home buyers](https://www.govt.nz/browse/housing-and-property/buying-or-selling-a-home/buying-your-first-home/), updated 11 Mar 2025) — rates/figures may have changed since; verify current criteria and participating lenders with Kāinga Ora (`https://kaingaora.govt.nz/`)
- **First Home Grant**: ❌ ENDED — finished May 2024 and no longer available (was up to $5,000, or $10,000 for a new build) (2026-10-23 verified, source: [govt.nz — Financial help for first-home buyers](https://www.govt.nz/browse/housing-and-property/buying-or-selling-a-home/buying-your-first-home/))
- **KiwiSaver First Home Withdrawal**: all KiwiSaver savings (including the government contribution) except $1,000 that must stay in the account; funds transferred from an Australian complying superannuation scheme cannot be withdrawn; at least 3 years' KiwiSaver membership required (2026-10-23 verified, source: [IRD — Getting my KiwiSaver for my first home](https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/getting-my-kiwisaver-funds-early/getting-my-kiwisaver-for-my-first-home), updated 28 May 2024)
- **Healthy Homes incentives**: insulation grants — verify current eligibility with EECA
- **Warmer Kiwi Homes**: Energy retrofit subsidy — verify current eligibility and funding with EECA

## Common listing platforms

- **Trade Me Property** — biggest
- **realestate.co.nz** — industry-owned
- **OneRoof** (NZ Herald)
- **Homes.co.nz** — sold-prices

## Caveats unique to NZ

- **NO STAMP DUTY** (abolished 1999) — UNIQUE in OECD; transaction cost ~$3-5k
- **NO general CGT** but **bright-line test 2 years** (property sold on/after 1 Jul 2024) — sells within 2 years = ordinary income
- **7 Nov 2026 election proposals** (none legislated): Labour 28% CGT from 1 Jul 2027 on residential investment + commercial property; Greens 10-year bright-line + interest denial; Te Pāti Māori 5% residential stamp duty — see `--tax` § Future risk
- **Foreign-buyer ban (2018)** — AU + SG citizens exempt; off-the-plan apartments only in developments with a developer exemption certificate; **since 6 Mar 2026** AIP / Investor 1 / Investor 2 resident visa holders can seek consent for a home priced more than NZ$5m (see `--tax` § Foreign-buyer regime)
- **NHCover (Toka Tū Ake)**: automatic with any home insurance policy that includes fire; building cover cap generally $300,000 + GST per natural-hazard event; max levy $480 + GST/yr (2026-10-23 verified, source: [Natural Hazards Commission — About NHCover](https://www.naturalhazards.govt.nz/insurance-and-claims/about-nhcover/)) — UNIQUE coverage
- **Earthquake risk extreme** — NSHM 2022 raised hazard ~50%; Christchurch + Wellington high
- **Wellington City ~-30.6% (computed)** from its Jan 2022 QV HPI peak to Sep 2026; still the weakest REINZ HPI series YoY (-4.5%, Sep 2026) — see `--price` § Compute
- **Cross-lease titles** (~10% Auckland) — shared ownership of section, flat plan; clunky for renovations
- **Leaky homes crisis** (1990s-early 2000s) — monolithic cladding pre-2003 vulnerable
- **Healthy Homes Standards** mandatory for rentals
- **Interest deductibility 100% restored 1 Apr 2025** for residential investment (2026-10-23 verified, source: [IRD](https://www.ird.govt.nz/property-interest-rules)); Greens propose denying it again (election proposal only)
- **GST on STR via platforms** since 1 Apr 2024
- **Cyclone Gabrielle 2023** + Auckland floods 2023 — major recent reform drivers
- **NHCover building cap $300k+GST** — high-value houses need top-up insurance
- **LIM report ~$300-500** mandatory in practice
- **Māori land** (Te Ture Whenua Māori Act 1993) — unique constraints, often 99-year leases
- **Rating valuations** (CV/LV) at least every 3 years per council (source: [LINZ — Property valuation in NZ](https://www.linz.govt.nz/guidance/property-valuation/property-valuation-new-zealand)); not market value
- **Rental loss ring-fencing** — cannot offset other income

## Reddit / forum sources

- **r/PersonalFinanceNZ** — biggest community
- **r/auckland**, **r/wellington**, **r/chch**
- **r/newzealand**
- **PropertyTalk forums**
- **Stuff Property** (news)

## Verification authorities

| Authority | When to call |
|---|---|
| **LINZ Toitū Te Whenua** | Title verification |
| **Local council** | LIM report, rates, zoning |
| **Earth Sciences NZ** (formerly GNS Science + NIWA) / **GeoNet** | Hazard zone status — GeoNet is a partnership of NHC Toka Tū Ake, Earth Sciences NZ and LINZ (2026 data, source [GeoNet — About](https://www.geonet.org.nz/about)) |
| **Toka Tū Ake (NHC)** | Natural-disaster cover specifics; prior NHC / EQC claim history on the home (Natural Hazards Portal, or request claim information from NHC) |
| **REINZ** | Market data |
| **Body Corporate** | If unit title |
| **Lawyer or registered conveyancer** | Conveyancing + settlement — both can carry out property transactions (2026 data, source [settled.govt.nz — Support team](https://www.settled.govt.nz/buying-a-home/thinking-of-buying/building-your-support-team-when-buying/)) |

## Source URL templates

| Source | URL pattern |
|---|---|
| LINZ Public Land Record Search | `https://lrs.linz.govt.nz/search/` |
| Trade Me Property | `https://www.trademe.co.nz/property/` |
| realestate.co.nz | `https://www.realestate.co.nz/` |
| REINZ HPI | `https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx` |
| QV / Cotality NZ | `https://www.qv.co.nz/price-index/` |
| GeoNet | `https://www.geonet.org.nz/` |
| Earth Sciences NZ (GNS Science + NIWA, merged 1 Jul 2025; legacy GNS site `https://www.gns.cri.nz/`) | `https://www.earthsciences.nz/` |
| Toka Tū Ake (Natural Hazards Commission) | `https://www.naturalhazards.govt.nz/` |
| NIWA (Earth Sciences NZ) | `https://niwa.co.nz/` |
| NZTA Traffic Counts | `https://www.nzta.govt.nz/resources/state-highway-traffic-volumes` |
| NZTA SH traffic monitoring (open data: AADT + % heavy) | `https://opendata-nzta.opendata.arcgis.com/datasets/b90f8908910f44a493c6501c3565ed2d` |
| Natural Hazards Portal (NHC) | `https://www.naturalhazardsportal.govt.nz/` |
| Tiaki Wai (Wellington metro water) | `https://www.tiakiwai.co.nz/` |
| IRD (**Te Tari Taake**) | `https://www.ird.govt.nz/` (2026-10-23 verified bilingual masthead: "Inland Revenue - Te Tari Taake") |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing (REINZ HPI + QV + Trade Me), traffic, tax (rates + bright-line + GST + zero stamp duty), rental (RTA + Healthy Homes), work, risks (NSHM 2022 + Cyclone Gabrielle 2023 + leaky homes), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for REINZ + QV September 2026 price benchmarks + bright-line 2-yr (property sold on/after 1 Jul 2024) + interest deductibility 100% from 1 Apr 2025 + foreign-buyer ban (AU+SG exempt) with the $5m+ investor-visa pathway in force since 6 Mar 2026 + NHCover $300k+GST cap + STR GST collection from 1 Apr 2024 + minimum wage $23.95/hr from 1 Apr 2026 (each re-checked 2026-10-23 against REINZ / QV / IRD / LINZ / NHC / Employment NZ); MEDIUM for the Auckland APTR night bands (last re-checked 2026-08-07), the $5m pathway's one-property limit (secondary source only) and the 7 Nov 2026 election proposals (secondary sources; party proposals, not law); LOW for the council rates table + "rates frozen" line, listing-platform counts, city salary ranges, cost and mains-cost benchmarks (est., unsourced), the leaky-homes damage est. and the climate / sea-level projections (not re-verified).
**Last verified**: 2026-08-07 (Auckland APTR suspension since 2020 + graduated general-rates/CATTR STR business uplift re-verified against Auckland Council; other sections unchanged). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs

- [ ] Per-council rates table
- [ ] Per-council STR rules detail
- [ ] Cross-lease conversion to fee simple flow
- [ ] Leaky-home identification + remediation decision tree
- [ ] Earthquake strengthening NSEC rating verification
- [ ] Bright-line transition rules per acquisition date
- [ ] Healthy Homes Standards compliance checklist
- [ ] Māori land (Te Ture Whenua) constraint check
- [ ] NHCover top-up insurance for high-value homes
- [ ] AU/SG resident exemption verification flow

## Update history

- **2026-04-25** — Initial population.
- **2026-08-07 to 2026-10-21** — Auckland APTR re-check (2026-08-07) and rental / tax regwatch tracker re-checks (2026-09-24, 2026-10-21); details in the Status footer.
- **2026-10-23** — Refresh wave, partial: the playbook-level date is not re-stamped because `--price`, `--tax`, `--rental`, `--work`, `--risks` and `--mains` each still hold claims that could not be re-checked against a fetched source. Facts checked / changed / confirmed / unverifiable per section:
  - **Country profile** — 10 / 2 / 1 / 7: EUR/NZD set to the ECB reference rate (22 Oct 2026); foreign-buyer line rewritten against LINZ (9 / 6 / 3 / 0 for that line alone) — the $5m+ investor-visa pathway is in force since 6 Mar 2026, replacing "Order in Council expected early 2026"; the one-property limit stays, sourced to Bell Gully (secondary). Unverified: postcode examples, 16 regions / 67 TAs, LRS $8 fee, leasehold place names, cross-lease ~10% of Auckland.
  - **`--price`** — 19 / 14 / 2 / 3: benchmark table (all 9 rows) moved to REINZ + QV September 2026; QV / Cotality source lines and Compute steps 3–4 rewritten (Wellington City ~-30.6% computed from the Jan 2022 QV HPI peak, replacing ~-26% est.). Unverified: Trade Me ~39k and realestate.co.nz ~35k listing counts, "industry-owned", a Stats NZ house price index.
  - **`--traffic`** — 3 / 1 / 0 / 1: NZTA open-data AADT + heavy-vehicle source added; the NZTA traffic-volumes page is bot-walled (kept); verdict bands are curated thresholds, not sourced facts.
  - **`--tax`** — 36 / 9 / 9 / 18: bright-line, interest deductibility, STR GST and the foreign-buyer regime re-checked against IRD / LINZ; 7 Nov 2026 election proposals added under Future risk (party proposals only, secondary sources). Unverified: council rates table and "rates frozen" (both now carry the may-have-changed suffix), legal / LIM / building-report fees, total transaction cost, stamp-duty abolition 1999 / "UNIQUE in OECD", the pre-2018 2-year bright-line row.
  - **`--rental`** — 24 / 2 / 16 / 6: RTA amendment dates and notice periods, the 12-month rent rule, ring-fencing, Healthy Homes, interest deductibility, the GST $60k threshold and the QLDC rating bands confirmed. Unverified: Auckland APTR night bands (Auckland Council unreachable; last re-checked 2026-08-07), [2023] NZSC 53, the QLDC 90-night cap, "other councils tightening".
  - **`--work`** — 14 / 4 / 5 / 5: minimum wage confirmed ($23.95/hr from 1 Apr 2026, Employment NZ); job boards updated (JobSpace, Indeed NZ; JobAve dead); MIQ replaced by Immigration New Zealand; salary block labelled est. Unverified: "Seek — biggest", the Trade Me Jobs URL, "min $1 capital", city salary ranges.
  - **`--risks`** — 32 / 9 / 11 / 12, plus climate projections 5 / 1 / 0 / 4: GNS Science and NIWA updated to Earth Sciences NZ (merged 1 Jul 2025); earthquake and volcano lines re-sourced to GeoNet; ICNZ insured-loss figures added for Canterbury 2010-11, Kaikōura 2016, the 2023 Auckland floods and Cyclone Gabrielle; Taupō, Auckland Volcanic Field, asbestos-era and leaky-homes-era rows corrected; NZ SeaRise pointer and an Earth Sciences NZ ex-tropical-cyclone rainfall data point added. Unverified: Whakaari death toll, sea-level rise +20-80 cm, leaky-homes ~$11B, Canterbury ~$40B total, lead-paint / H1 / post-2018 rows, LIM fee, +1.5–4.0°C, drought and premium trends.
  - **`--mains`** — 8 / 1 / 1 / 6: Wellington Water replaced by Tiaki Wai (council-owned, from 1 Jul 2026); Watercare confirmed; cost table labelled est. (unsourced). Unverified: Christchurch / Dunedin water arrangements, the four cost ranges.
  - **Cost benchmarks** — 12 / 0 / 0 / 12: header labelled est. (contractor-quote ranges, no primary source); values unchanged.
  - **Active fiscal incentives** — 5 / 1 / 0 / 4: First Home Loan re-sourced to govt.nz; KiwiSaver first-home withdrawal corrected against IRD. Unverified: EECA programmes (insulation grants, Warmer Kiwi Homes).
  - **Caveats unique to NZ** — 12 / 5 / 5 / 2: Wellington line aligned with `--price` Compute; foreign-buyer, NHCover and rating-revaluation lines corrected; election-proposal pointer added. Unverified: "NO STAMP DUTY — UNIQUE in OECD" with ~$3-5k transaction cost, LIM ~$300-500.
  - **Common listing platforms** — 4 / 0 / 1 / 3 and **Reddit / forum sources** — 7 / 0 / 0 / 7: unchanged; only Homes.co.nz confirmed, subreddit URLs checked for liveness only.
  - **Verification authorities** — 7 / 3 / 4 / 0 (fully re-verified): Earth Sciences NZ / GeoNet partnership, NHC claim-history checks, lawyer or registered conveyancer (settled.govt.nz).
  - **Source URL templates** — 11 / 3 / 7 / 1: GNS re-pointed to earthsciences.nz and NIWA to niwa.co.nz; NZTA open data, Natural Hazards Portal and Tiaki Wai added; the NZTA traffic-volumes page could not be checked (bot wall).
