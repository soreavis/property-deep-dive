# United Arab Emirates 🇦🇪 — Property Due-Diligence Playbook

ISO2: `ae`. Status: ✅ Fully populated (researched 2026-04 / verified 2026-07-03 — Tier-A quarterly refresh).

> **Critical framing**: The UAE is a **foreign-buyer-restricted market**. Non-GCC nationals can only acquire **freehold** in **designated freehold / investment zones** that vary by emirate. Outside those zones the maximum interest is leasehold or usufruct (up to 100 years, Sharjah). Always confirm zone status with the relevant cadastre (DLD / ADREC / Sharjah Real Estate Reg.) **before** signing any reservation form. Currency risk vs USD is structurally zero — AED is pegged at **3.6725 to the USD since 1997** (Central Bank of the UAE).

## Country profile

- **Postal code system**: Traditionally none. Modern parcel-level identifiers:
  - **Makani** (Dubai) — 10-digit unique address code maintained by Dubai Municipality (`https://www.dm.gov.ae/open-data2/open-data-for-makani`)
  - **Onwani** (Abu Dhabi) — physical street-naming + addressing system maintained by the Department of Municipalities and Transport
  - **Plot number + community** is the cadastral identifier on Title Deeds
- **Admin levels**: Federation of **7 emirates** → municipalities → communities (sub-divisions)
- **Currency**: AED (UAE Dirham). Pegged USD 1 = AED 3.6725 since 1997 (Central Bank of UAE)
- **Languages**: Arabic (official, all formal contracts and Title Deeds in Arabic — bilingual EN/AR is universal in property sector); English is the de-facto business language
- **Cadastre** (per emirate — there is **no federal cadastre**):
  - **Dubai**: Dubai Land Department (DLD) — `https://dubailand.gov.ae/` + Dubai REST app
  - **Abu Dhabi**: Abu Dhabi Real Estate Centre (ADREC, formerly DMT-DGE) — `https://adrec.gov.ae/`
  - **Sharjah**: Sharjah Real Estate Registration Department — `https://www.shjrerd.gov.ae/`
  - **Ras Al Khaimah**: RAK Municipality / RAK Department of Economic Development for property — `https://mun.rak.ae/`
  - **Ajman**: Ajman Municipality and Planning Department — `https://www.ajman.ae/en/servicecatalog/service_categories/municipality-planning-department`
  - **Fujairah / Umm Al Quwain**: Municipal offices
- **Identifier(s)**:
  - **Title Deed (Sanad Mulkiyya)** — issued by relevant emirate cadastre at completion / handover
  - **Oqood** (عقد) — interim registration certificate for off-plan sales (Dubai), recorded in DLD's Oqood system, replaced by Title Deed at handover
  - **Initial Sale Contract (ISC)** — equivalent to oqood in Abu Dhabi / other emirates
- **Recent reforms** (12-month watchlist):
  - **Abu Dhabi Law 13/2019** (effective 16 Apr 2019, amending Abu Dhabi Law 19/2005) — non-GCC freehold ownership in Abu Dhabi designated investment areas (NB: there is no Federal Decree-Law 21/2021 on this topic; the reform is an emirate-level Abu Dhabi law, not federal) (2026-05-27 verified, source Al Tamimi & Co + Library of Congress Global Legal Monitor)
  - **Dubai 2040 Urban Master Plan** (effective 2021–2040) — zoning + density evolution
  - **Golden Visa** property route (10 yr, AED 2M): ICP accepts bank-loan financing from an approved local bank and off-plan units bought from an approved developer (ICP golden-residency guide, updated 10 Sep 2026); the "further easing 2024" date previously given here is unverified — not found in the primary sources read for the Oct 2026 refresh
  - **VAT** introduced 1 Jan 2018 at 5%; first supply of new residential (sale or lease) 0%-rated if made within 3 years of completion; subsequent residential supplies exempt; commercial standard-rated at 5% (MoF VAT page + FTA Real Estate Guide VATGRE1)
  - **Federal Corporate Tax** for financial years starting on or after **1 June 2023**: 0% up to AED 375,000 taxable income, 9% above (Cabinet Decision 116/2022). A natural person's Real Estate Investment income (sale, leasing or renting of UAE property not conducted, or required to be conducted, under a licence) is **not** a taxable business (Cabinet Decision 49/2023); non-resident juridical persons earning UAE immovable-property income have a nexus (Cabinet Decision 56/2023)
  - **Dubai Smart Rental Index** revamped Jan 2025 — every residential building rated **1–5 stars** by AI (~60 criteria: condition, finishes, maintenance, amenities, FM quality, location); star rating influences allowed rent increases at renewal (NOT A/B/C/D) (2026-05-27 verified, source DLD Smart Rental Index portal + Driven Properties + Kaizen AMS)
  - **Dubai Tasreef stormwater plan** (AED ~30 bn / USD 8 bn) approved post-Apr 2024 floods; phased to 2033
  - **Dubai Law No. 2 of 2025** — DIFC Courts Enforcement Judge has jurisdiction over enforcement of DIFC-registered non-Muslim wills inside or outside the DIFC (Art. 31(5)); for assets outside the DIFC (e.g. DLD-registered property) execution still runs through the Dubai Courts Enforcement Judge (Art. 32), which the DIFC Courts Wills FAQ calls a standard formality (2025 law, source DIFC Courts)

---

## 🇦🇪 Foreign buyer eligibility (READ FIRST)

This section determines whether a transaction is even legally possible. Confirm zone status BEFORE assessing price.

### Dubai

**Designated Freehold Areas** (DLD-maintained list — areas where non-GCC may own freehold):
- Dubai Marina, Downtown Dubai, Palm Jumeirah, Business Bay, Jumeirah Lake Towers (JLT), Jumeirah Village Circle (JVC), Jumeirah Beach Residence (JBR), Arabian Ranches, Damac Hills, Dubai Hills Estate, Emirates Hills, Meydan, MBR City, The Greens / The Views, Dubai Sports City, Dubai Silicon Oasis, International City, Discovery Gardens, Al Furjan, Town Square, Tilal Al Ghaf, Bluewaters Island, City Walk, Dubai Creek Harbour, and ~30+ more zones.
- Authoritative list: DLD eServices portal → "Designated Areas" lookup or Dubai REST app.
- **Outside designated areas**: non-GCC may obtain **leasehold up to 99 years** in some non-freehold districts (less common for residential investment).
- **2025 freehold-zone expansion**: DLD announced on 19 Jan 2025 that **private property owners** in the **Sheikh Zayed Road** area (Trade Centre Roundabout → Water Canal, 128 plots) and **Al Jaddaf** (329 plots), 457 plots in total, can convert their ownership status to **freehold available to all nationalities**. The DLD release does not describe the plots' existing tenure as leasehold (ValuStrat, quoted by The National, calls them areas that previously could only be owned by UAE and GCC nationals — secondary). Process per DLD: check eligibility on Dubai REST → apply to DLD for land assessment and valuation → common-area fees / service charges set per RERA guidelines → conversion fee of **30% of the property's valuation (based on Gross Floor Area)** → map + freehold title deed issued after payment; no deadline or application window stated. Legal instrument: BSA Law (secondary) says DLD amended Art. 3 of Regulation 3/2006 but names no amending instrument, and the DLD release cites none — data not publicly available — verify at dlp.dubai.gov.ae (Dubai Legislation Portal). (2026-10-21 verified, source DLD news release 19 Jan 2025; instrument limb secondary only)

### Abu Dhabi

**Investment Zones for non-GCC freehold** (ADREC):
- **Saadiyat Island**, **Yas Island**, **Al Reem Island**, **Al Raha Beach**, **Al Reef**, **Masdar City**, **Hidd Al Saadiyat**, **Mohammed Bin Zayed City** (selected zones), **Lulu Island** (selected), **Jubail Island**, **Ghantoot**.
- **Abu Dhabi Law 13/2019** (amending Abu Dhabi Law 19/2005) grants non-GCC the right to **freehold land + buildings** within designated investment areas; prior to Apr 2019 non-GCC were limited to musataha / usufruct / 99-yr lease. (NB: prior playbook attribution to "Federal Decree-Law 21/2021" was incorrect — that federal decree exists but covers a different subject; the real-estate ownership extension is emirate-level only.) (2026-05-27 verified, source Al Tamimi + Addleshaw Goddard 2021)
- Verify zone via ADREC's **Tamleek** lookup.

### Sharjah

- **Non-GCC nationals** (incl. non-Arab): freehold available **in designated zones only** per **Sharjah Law 2/2022 + Executive Council Decision 30/2022** (Aljada, Maryam Island, Al Mamsha and other approved projects). Outside designated zones, 100-year usufruct (intifa') is the maximum interest, renewable. (2026-05-27 verified, source Afridi & Angell + Lexology)
- **Arab nationals** (non-GCC, but holding Arab country passport): freehold permitted in selected designated zones.
- **GCC nationals**: freehold across most of the emirate.
- **Residency visa**: Khaleej Times reported on 6 May 2018 that Sharjah opened purchases to non-Arab investors without a UAE residence visa (secondary). The "June 2025" SRERD relaxation previously cited here could not be confirmed (no Sharjah government source found, and SRERD's site timed out in the Oct 2026 refresh) — UNVERIFIED; confirm current rules with SRERD. The ownership statute is Sharjah Law 2/2022.

### Other Northern Emirates

- **RAK**: Freehold for non-GCC in **Al Marjan Island**, **Al Hamra Village**, **Mina Al Arab**, **Dafan Al Nakheel** (RAK Municipality / RAK Properties communities).
- **Ajman**: Freehold for non-GCC in selected developments — **Ajman Corniche Residences**, **Emirates City**, **Al Ameera Village**, etc.
- **Fujairah / UAQ**: Limited freehold — verify per development with the local Municipality.

### Golden Visa property route (federal — applies UAE-wide)

| Item | Threshold |
|---|---|
| **Long-term Golden Visa (10 yr)** | Property worth ≥ AED 2,000,000 (single or aggregate properties, your name) |
| **2-year Property Investor Visa** | **Sole owners**: no minimum property value (completed property + registered title deed); **joint owners**: ≥ AED 400,000 each (DLD reform 29 Apr 2026 — the prior AED 750k floor was **abolished**) (2026-05-27 verified, source VisaHQ + LuxHabitat Journal + DLD announcement 29 Apr 2026) |
| **Mortgage financing allowed** | Yes — ICP: loan financing allowed if from an approved local bank; GDRFA Dubai: mortgaged property acceptable. DLD Golden Visa (Investor) e-service asks for a bank no-objection letter stating paid amount and balance, while its description asks for a bank letter showing AED 2M paid — confirm the paid-amount rule with DLD before relying on a mortgaged unit (2026-10-21 verified, ICP + GDRFA + DLD service pages) |
| **Off-plan eligible** | Yes per ICP golden-residency guide: one or more off-plan units totalling ≥ AED 2,000,000 bought from an approved local real estate company authorised by the competent local authority; no paid-percentage stated (2026-10-21 verified, source `https://icp.gov.ae/en/services/uae-golden-residency`). The GDRFA Dubai and DLD Golden Visa pages state no off-plan terms — confirm with DLD before relying |
| **Family inclusion** | Spouse and children regardless of age, plus parents; domestic workers may be sponsored under the applicable rules (ICP golden-residency guide, updated 10 Sep 2026). The unmarried-daughters / sons-under-25 limit is the standard resident-family rule, not the Golden rule |
| **Authority** | ICP (Federal Authority for Identity, Citizenship, Customs and Port Security) — `https://icp.gov.ae/` + GDRFA Dubai for Dubai applications |

**Retirement Visa (5 yr, renewable)** — ICP: at least 15 years' service before retirement (inside or outside the UAE) **or** age ≥ 55; GDRFA Dubai's service page and u.ae say 15 years **and** age 55 — confirm with the issuing authority:
- Property ≥ AED 1,000,000 (purchase or market value; a mortgaged title deed counts once AED 1M has been paid towards release) **or** a deposit ≥ AED 1,000,000 placed with a UAE financial institution within 60 days of issuance (ICP; GDRFA Dubai's terms and u.ae join property and savings with "and"), **OR**
- Fixed annual income ≥ AED 240,000 (= AED 20,000/month), from inside or outside the UAE, with 6 months of bank statements (ICP + GDRFA Dubai service pages read 2026-10-28). u.ae (updated 28 Jul 2026) gives AED 180,000 as the general floor and AED 240,000 for Dubai applications; the issuing authorities' AED 240,000 is used here.

### Compliance / AML

- Federal AML rules (Federal Decree by Law No. 10 of 2025 on Anti-Money Laundering and Combating the Financing of Terrorism and Proliferation Financing, which repealed Federal Decree-Law 20/2018; executive regulations Cabinet Resolution 134/2025 — MoET AML page) require **source-of-funds documentation** for every property transaction; DLD trustee offices enforce this at sale registration (source-of-funds and trustee-office limbs not re-verified in the Oct 2026 refresh).
- Freehold purchases paid in physical cash of **AED 55,000 or more** (one or several payments, for all or part of the price), or wholly or partly in virtual assets, oblige the broker or agent to keep ID and contract records and file a Real Estate Activity Report (REAR) on the FIU's goAML platform (Ministry of Economy Circular 05/2022, effective 1 Jul 2022; still listed on MoET's AML page; Art. 41(3) of Decree by Law 10/2025 keeps circulars issued under 20/2018 effective insofar as they do not conflict with it, until superseded).

**Verification path**:
1. Confirm property is in a designated zone for your nationality (DLD/ADREC/SRERD lookup).
2. Pull the seller's current Title Deed extract (DLD trustee office) to verify ownership + encumbrances.
3. If off-plan → verify project on DLD project register + escrow account active.

---

## Section: `--price`

### Primary sources

- **DLD Open Data Portal** (Dubai): `https://dubailand.gov.ae/en/open-data/` — transaction-level sales data, downloadable; DLD's official Residential Properties index (quarterly and annual; general / flats / villas) at `https://dubailand.gov.ae/en/open-data/indexes-home/` and annual research reports at `https://dubailand.gov.ae/en/open-data/research/` (checked 2026-10-28)
- **DLD Smart Rental Index** (rentals): `https://dubailand.gov.ae/en/eservices/rental-index/`
- **ADREC** open data: `https://adrec.gov.ae/`
- **Property Monitor** (consultancy aggregator using DLD data): `https://propertymonitor.com/`
- **Bayut Index**: `https://www.bayut.com/property-market-analysis/index/` (the old `/index/` path redirects here, checked 2026-10-28) — listing-based price index (listing-platform tier) per emirate, community and property type; latest month Sep 2026
- **Property Finder** market reports: `https://www.propertyfinder.ae/blog/`
- **REIDIN** Residential Market Sales Price Index (2014 Jan = 100): monthly *UAE Residential Property Price Report* at `https://reidin.com/category/reports` (Sep 2026 = edition 214; Dubai, Abu Dhabi, Sharjah, Ajman, RAK) — secondary aggregator; REIDIN prepared DLD's 2025 Annual Data Review with DLD

### Listing platforms

- **Bayut**: `https://www.bayut.com/`
- **Property Finder**: `https://www.propertyfinder.ae/`
- **Dubizzle Property**: `https://www.dubizzle.com/property-for-sale/`
- **Houza** — challenger portal; ceased operations Feb 2024 per trade press (`https://www.onlinemarketplaces.com/articles/emirati-challenger-portal-houza-folds-as-investors-lose-appetite/`, 4 Apr 2024 — secondary) and `houza.com` no longer serves a website (2026-10-21 verified); no successor — use Bayut / Property Finder / Dubizzle above
- **Luxhabitat**, **LuxuryProperty.com** (high-end)

### Dubai citywide benchmarks (verified 2026-10-28)

- **Citywide average residential price (DLD, primary)**: units **AED 20,666/sq m (≈ AED 1,920/sq ft = 20,666 ÷ 10.764)**, villas **AED 16,791/sq m (≈ AED 1,560/sq ft)** in 2025 — units +6%, villas +15% vs 2024 (DLD *Dubai Real Estate Market — Annual Data Review 2025*, 12 Oct 2026). DLD's official Residential Properties index: +8.90% YoY in Q4 2025 and +9.81% for 2025; no 2026 quarter published yet (DLD Open Data → Indexes, checked 2026-10-28). **2026 has turned negative**: REIDIN Residential Market Sales Price Index −1.27% YoY in Sep 2026 (+0.25% MoM), and ValuStrat's VPI 218.6 points in Q3 2026, −4.5% YoY, its first annual fall since the pandemic (ValuStrat via Global Property Guide) — both secondary. Global Property Guide (Oct 2026) names the regional war that began in late Feb 2026 as the turning point. The +19.8% for 2025 matches ValuStrat's figure (Dubai Outlook 2026); REIDIN printed +12.88% YoY for Dec 2025. Cross-check the current month on REIDIN / DLD before relying on any 2025 level.
- **Transaction volume (DLD, primary)**: 2025 — 270,328 real estate transactions worth AED 917 bn (+20% YoY), of which sales 217,889 worth AED 680 bn (DLD Annual Data Review 2025). **2026 by quarter (secondary)**: Q1 AED 137.3 bn of residential sales across 45,221 deals, +18.8% YoY in value, off-plan AED 103.4 bn (REIDIN Q1 2026 Market Overview); Q2 fewer than 37,000 residential sales worth AED 88 bn, about −43% YoY in value (CBRE via Global Property Guide); Q3 about 34,500 residential sales worth AED 70.8 bn (Savills from DLD data, via Global Property Guide). Property Monitor's Q1 figure (AED 143.1 bn) and the DXBinteract all-property figure were not re-verified and are dropped. (2026-10-28 verified — re-pull each quarter.)
- **Villas outperformed apartments**: villas **+15.16%** vs apartments **+12.52%** YoY in REIDIN's index (Dec 2025); DLD's official index shows the same split for Q4 2025 — villas +13.16% vs flats +6.73% YoY. By Sep 2026 REIDIN had villas +1.06% and apartments −1.65% YoY, so villas kept outperforming apartments as prices fell (2026-10-28 verified, REIDIN Dec 2025 + Sep 2026 reports; DLD Open Data → Indexes)

### Premium-zone benchmarks (REIDIN Q1 2026 transacted / Bayut Index Sep 2026 asking)

| Zone | Type | AED/sqft (avg) | Notes |
|---|---|---:|---|
| **Dubai Marina** | apartment | AED 2,001 transacted (REIDIN Q1 2026) · AED 2,435 asking (Bayut Index Sep 2026) | Asking runs above transacted; Bayut 12-month change −3.33% |
| **Downtown Dubai** | apartment | AED 2,959 transacted (REIDIN Q1 2026) · AED 3,468 asking (Bayut Index Sep 2026) | Burj Khalifa premium pulls avg up; Bayut 12-month −2.24%; CBRE Q2 2026 Downtown apartments about −7% QoQ (via Global Property Guide) |
| **Business Bay** | apartment | AED 2,211 transacted (REIDIN Q1 2026) · AED 2,516 asking (Bayut Index Sep 2026) | Bayut 12-month +1%; CBRE Q2 2026 about −7% QoQ (via Global Property Guide) |
| **Palm Jumeirah** | villa | AED 6,428 transacted (REIDIN Q1 2026) · AED 7,029 asking (Bayut Index Sep 2026) | Beachfront premium; Bayut 12-month +7.73% |
| **Palm Jumeirah** | apartment | AED 3,512 transacted (REIDIN Q1 2026) · AED 4,625 asking (Bayut Index Sep 2026) | Tier-dependent (Shoreline vs branded); CBRE Q2 2026 Palm apartments about −9% QoQ (via Global Property Guide) |
| **Emirates Hills / Dubai Hills** | villa | Emirates Hills AED 3,571 · Dubai Hills Estate AED 2,758 transacted (REIDIN Q1 2026); asking AED 5,195 / AED 3,114 (Bayut Index Sep 2026) | High-end suburban; CBRE Q2 2026 Dubai Hills villas −5% QoQ (via Global Property Guide) |
| **JVC / Damac Hills 2** | apartment | asking AED 1,488 (JVC) · AED 1,261 (DAMAC Hills 2) (Bayut Index Sep 2026) | Mid-market freehold; not in REIDIN's top-10 average-price tables — check DLD transactions for a transacted figure |
| **International City / Dubai Silicon Oasis** | apartment | asking AED 1,053 (International City) · AED 1,330 (DSO) (Bayut Index Sep 2026) | Entry-level freehold; Bayut 12-month +26.28% (IC) / −7.96% (DSO) — volatile listing mix |

(Sources: REIDIN *Dubai Residential Real Estate Q1 2026 Market Overview* top-10 community tables — transacted, secondary aggregator of DLD data, `https://reidin.com/wp-content/uploads/2026/04/Dubai-Residential-Real-Estate-Q1-2026-Market-Overview.pdf`; Bayut Index `https://www.bayut.com/property-market-analysis/index/` — asking prices, listing platform, Sep 2026; transacted figures rounded. Asking runs above transacted in every row, and the Q1 2026 transacted levels predate the Q2–Q3 2026 falls — *cross-check the current quarter on DLD transactions / REIDIN* (2026-10-28 verified))

### Abu Dhabi benchmarks

[ADREC (Abu Dhabi Real Estate Centre)](https://adrec.gov.ae/) is the primary regulator and publishes interactive dashboards at [adrec.gov.ae/en/property_and_index/adrec-dashboard](https://adrec.gov.ae/en/property_and_index/adrec-dashboard) (transaction volumes + price indices — interactive, no static export; manual dashboard visit required for definitive transactional values). Most reliable per-zone AED/sqft figures are aggregated by [Knight Frank H1 2025](https://www.knightfrank.ae/newsroom/article/2025/8/abu-dhabi-residential-market-review-h1-2025) and [Bayut FY 2025 / H1 2025 reports](https://www.bayut.com/mybayut/abu-dhabi-sales-market-report-2025/). ADREC's 2025 annual report (released 27 Feb 2026) confirms direction: **+19% apartments, +13% villas YoY 2024 → 2025**. Per [ADREC's H1 2025 Market Report](https://adrec.gov.ae/-/media/adrec/home/abu-dhabi-real-estate-market-report-2025-h1.pdf), H1 2025 residential unit sales hit a record **AED 25 Bn**, with ~82% of sales value concentrated in 8 key districts — Al Saadiyat Island led at ~33% of sales value (~AED 8.25B of the AED 25 Bn) and Yas Island ~15% (~AED 3.75B). (2025 data, source ADREC H1 2025 Market Report)

| Zone | Type | AED/sqft | Source · period | YoY |
|---|---|---:|---|---:|
| **Saadiyat Island** | villa (luxury slice — HIDD Al Saadiyat, Mamsha, beachfront) | ~AED 2,061 | Bayut FY 2025 report | +12.9% |
| **Saadiyat Island** | villa (whole-island incl. Reserve/Lagoons) | ~AED 1,764 | Bayut Index Sep 2026 (asking) | −3.68% |
| **Saadiyat Island** | apartment (luxury) | ~AED 2,932 | Bayut FY 2025 report | +27.0% |
| **Saadiyat Island** | apartment (whole-island) | ~AED 3,472 | Bayut Index Sep 2026 (asking) | −0.09% |
| **Yas Island** | villa | ~AED 1,528 | Bayut FY 2025 report | +10.9% |
| **Yas Island** | apartment | ~AED 1,818 | Bayut FY 2025 report | +24.3% |
| **Yas Island** | apartment (live index — branded/waterfront uplift) | ~AED 2,342 | Bayut Index Sep 2026 (asking) | +6.8% |
| **Al Reem Island** | apartment (mid-tier — Reem is overwhelmingly apartment stock) | ~AED 1,352 | Bayut FY 2025 report | +18.9% |
| **Al Reem Island** | apartment (live index) | ~AED 1,778 | Bayut Index Sep 2026 (asking) | +13.31% |
| **Abu Dhabi citywide** | apartment | ~AED 1,296 | Knight Frank Q2 2025 | +17.3% |
| **Abu Dhabi citywide** | villa | ~AED 1,103 | Knight Frank Q2 2025 | (+42.3% since Q1 2020) |
| **Abu Dhabi citywide** | blended (all stock, valuation-based VPI) | ~AED 1,005 | ValuStrat Q3 2025 (not re-verified 2026-10-28 — report gated) | +9.0% |

**Abu Dhabi citywide (H1 2026, ADREC — primary):** repeat-sales prices +20% YoY for apartments and +12% for villas; residential unit sales AED 70.4 bn vs AED 25.3 bn in H1 2025; off-plan 89% of sales value and 82% of deals; Hudayriyat Island AED 19 bn (27% of value), Saadiyat AED 13.3 bn, Al Reem + Al Maryah AED 10.5 bn, Yas AED 7.3 bn (ADREC H1 2026 market report release, 18 Aug 2026). Later, secondary: ValuStrat Q2 2026 index +17.8% YoY (apartments +24.1%, villas +12%), ready homes AED 1,442/sqft (≈ USD 393) (via Global Property Guide, Oct 2026); REIDIN sales index +11.17% YoY in Sep 2026, down from +27.76% in April. AD still outpaces Dubai, but growth is slowing. Pair with the Jun 2026 ADREC rent freeze (see `--rental`), which caps AD rental growth for any yield read-across. (2026-10-28 verified)

**Rental yields (Bayut FY 2025 — ROI on listed prices, gross):** Saadiyat villa 4.47% · Saadiyat apt 4.05% · Yas villa 5.43% · Yas apt 7.07% · Al Reem apt **7.49%** · Masdar City apt 8.45% (Masdar, not Al Reem, has the highest yield in Bayut's mid-tier apartment table; affordable Al Reef apt 9.68%). Market-wide gross yield (REIDIN, Sep 2026, secondary): Abu Dhabi 5.89%, Dubai 6.17%.

**Methodology notes:** (a) Knight Frank uses transaction-weighted close prices; ValuStrat's VPI is valuation-based (a marked-to-market sample of properties, per ValuStrat) — the AED 1,005 vs AED 1,296 citywide spread is methodology, not error. (b) Bayut "luxury segment" carves out the top tier; the live Bayut Index is a whole-zone figure including mid-tier sub-communities — for Saadiyat this pulls the villa figure below the luxury slice (AED 1,764 Sep 2026 vs AED 2,061 FY 2025). (c) ADREC per-zone AED/sqft is **not** exposed in static press releases. (d) Off-plan list price ≠ ready market — est. 5–15% off-plan-to-handover discount (rule of thumb, no primary source; calibrate per project).

*— 2025–Sep 2026 data; cross-check the current month on Bayut Index, the REIDIN monthly report or the ADREC dashboard. (2026-10-28 verified, sources [Knight Frank H1 2025](https://www.knightfrank.ae/newsroom/article/2025/8/abu-dhabi-residential-market-review-h1-2025) + [Bayut FY 2025](https://www.bayut.com/mybayut/abu-dhabi-sales-market-report-2025/) + [ADREC 2025 annual report](https://www.zawya.com/en/press-release/research-studies/adrec-releases-abu-dhabi-real-estate-market-report-2025-359182) (old Zawya URL redirects here) + [ADREC H1 2026 report release](https://adrec.gov.ae/en/news/press-29---adrec-releases-the-abu-dhabi-real-estate-market-report-for-h1-2026) + [Bayut Index](https://www.bayut.com/property-market-analysis/index/) Sep 2026; ValuStrat Q3 2025 row not re-verified)*

### Compute

1. Listing AED/sqft = listing AED ÷ BUA sqft (BUA = Built-Up Area; some listings show sellable area instead of BUA — clarify which)
2. Cross-check with Bayut Index for the same community + property type
3. Cross-check with **DLD transaction history** for the same building (DLD Dubai REST app shows recent sold prices building-by-building)
4. **Trap**: Off-plan list price ≠ ready market — est. 5–15% off-plan-to-handover discount when comparing (rule of thumb, no primary source)
5. **Trap**: Branded residences (Bulgari, Armani, Atlantis The Royal) carry est. 50–150% premiums vs peer non-branded (unsourced rule of thumb — calibrate on DLD / REIDIN comps for the same community) — don't average them in
6. **Trap**: Service-charge-included vs net rent for rental yield calcs — verify

---

## Section: `--traffic`

### Primary sources

- **RTA Dubai** (Roads and Transport Authority): `https://www.rta.ae/` — open data portal `https://www.rta.ae/wps/portal/rta/ae/home/open-data`
- **Department of Municipalities and Transport — Abu Dhabi (DMT)**: `https://www.tamm.abudhabi/` (TAMM is the unified Abu Dhabi services platform; transport open data via DMT)
- **Federal Ministry of Energy and Infrastructure** (federal road network): `https://moei.gov.ae/` ⚠️ did not load in the 2026-10-28 check (timeout from a script and from a browser) — may be reachable from the UAE only

### Coarse fallback

OSM `highway` class:
- motorway = Sheikh Zayed Road (E11), E311 Mohammed Bin Zayed Road, E611 Emirates Road
- trunk = major Dubai-Sharjah-Abu Dhabi arterials
- primary = intra-emirate boulevards
- residential = community internal roads

### Verdict bands (for UAE highway context)

- 🟢 < 5,000 v/d (community internal road)
- 🟡 5,000–25,000 v/d (urban arterial)
- 🟠 25,000–80,000 v/d (busy arterial / E-route side)
- 🔴 > 80,000 v/d (Sheikh Zayed Road, E311 mainlanes — chronic congestion)

### Notes

- Dubai-side Sheikh Zayed Road central segments: the 200,000+ v/d figure is unverified — no RTA count located in the 2026-10-28 check; RTA's open-data page sends specific data requests to Dubai Pulse (`https://www.dubaipulse.gov.ae/`). Treat as est.; adjacency means noise + congestion regardless of the exact count.
- Salik (Dubai toll) gantries: presence near a property often signals a major arterial.
- Metro Red + Green lines (RTA) and the **Blue Line** under construction — 30 km, 14 stations (9 elevated, 5 underground), interchanges at Creek (Green Line), Centrepoint (Red Line) and International City 1; RTA's project page reports 10% complete, 30% expected by end-2026 and 200,000 daily users expected in 2030 (checked 2026-10-28). Operations are set to start on 9 Sep 2029 per RTA's announcement (Gulf News, 19 Dec 2024 — secondary; the RTA project page itself gives no date). Stations within est. ~800 m materially affect catchment + price.

---

## Section: `--tax`

### Annual property tax

**There is NO annual real-estate property tax in the UAE** — neither federal nor (for residential held in personal name) emirate-level.

What residents do pay annually:

| Item | Rate / amount | Authority |
|---|---|---|
| **Dubai Municipality Housing Fee** | **5% of annual rental value**, billed monthly via DEWA in 12 instalments | Dubai Municipality (collected via DEWA) |
| Owner-occupier housing fee equivalent (Dubai) | 5% of RERA-assessed average rental value of comparable property | Dubai Municipality |
| Abu Dhabi municipality fee (tenants; UAE nationals exempt on residential leases) | **5% of annual rental value** (u.ae: rental value or rental index, whichever is higher), minimum AED 450, added to the monthly water and electricity bill over 12 months | Executive Council Chairman Resolution 49/2018 Art. 4 (ADREC-hosted text) + u.ae |
| **UAE nationals** | Exempt from housing fee on owner-occupied property | — |
| **Service charges** (HOA equivalent — mandatory) | **AED 3–70 / sqft / yr** depending on community/tier | DLD Mollak system regulates Dubai |
| **Chiller / district cooling** (often separate) | AED 10–18 / sqft / yr (residential, district cooling) OR AED 400–1,000 / month flat | Empower / Tabreed / Emicool (provider-dependent) |

(Sources: Dubai Municipality / DEWA; DLD Service Charge Index `https://dubailand.gov.ae/`; Empower / Tabreed tariffs)

### Service-charge tier reference (Dubai 2026)

| Tier | AED/sqft/yr | Examples |
|---|---:|---|
| **Entry** | 3–10 | International City, Discovery Gardens |
| **Mid** | 10–20 | JVC, JLT mid-tier, Dubai Hills mid |
| **Premium** | 20–35 | Marina, Downtown standard, Business Bay |
| **Luxury** | 35–55 | Palm Jumeirah Shoreline, Emirates Hills |
| **Ultra-luxury / branded** | 55–70+ | Bulgari Residences, Atlantis The Royal, One Za'abeel |

(Source: DLD Service Charge Index Dubai 2026 + LuxHabitat 2026 guide — verify current per Mollak per building)

### Transaction taxes (one-time at purchase)

| Item | Amount | Notes |
|---|---|---|
| **DLD Transfer Fee — Dubai** | **4% of purchase price** | Statutory split 2%+2% buyer/seller; market practice = buyer pays full 4% (verify in MOU) |
| **ADREC Transfer Fee — Abu Dhabi** | **2% of value** | ADREC fee schedule for off-plan sales: 2% split equally between seller and buyer, capped at AED 2M per transaction; Resolution 49/2018 lets the Executive Committee set the sale fee at 1–4%, split equally unless agreed — confirm the ready-property rate with ADREC. ADREC Trustee Office transfer fee AED 1,050 incl. VAT |
| **Sharjah / RAK / Ajman fees** | 2–4% (varies — confirm with local cadastre) | — |
| **DLD Title Deed issuance fee** | AED 250 title deed certificate + AED 250 map fee (villas and apartments; land: AED 225 Dubai Municipality unified map / AED 100 outside DM); off-plan initial (Oqood) sale page lists no title-deed fee; it lists an AED 1,000 self-registration fee for developers using the Oqood portal | DLD e-service pages (Property Sale Registration; Request to register the initial sale), site updated 14 Oct 2026 |
| **DLD Knowledge + Innovation fees** | AED 10 + AED 10 | DLD fixed |
| **Trustee office fee** (mandatory for secondary-market Dubai transfers) | AED 4,000 + VAT (sale value AED 500,000 or more) / AED 2,000 + VAT (below AED 500,000) | DLD Property Sale Registration page (service partner fees) |
| **Mortgage registration** (if mortgaged) | **0.25% of mortgage value** + AED 250 title deed + AED 10 knowledge + AED 10 innovation; service-partner fee AED 4,000 + VAT (AED 5,000 + VAT on an Oqood) | DLD Mortgage registration e-service |
| **Bank mortgage processing fee** | 0.5–1% of loan | Per bank |
| **Mortgage LTV caps** | Expats: 80% first home ≤ AED 5M, 70% above AED 5M, 60% second home or investment; UAE nationals: 85% first home ≤ AED 5M, 75% above, 65% second home or investment; off-plan 50% for every buyer; maximum tenor 25 years | CBUAE Regulations Regarding Mortgage Loans Art. 3 (Circular 31/2013; LTV bands as amended by Board Resolution 31/2/2020) |
| **Property valuation** (mortgaged) | AED 2,500–3,500 | Bank-appointed valuer |
| **Conveyancer / lawyer** (optional) | AED 5,000–15,000 typical | UAE has no notary system for property — DLD Trustee + lawyers handle conveyancing |
| **Real estate agent commission** | 2% of price + 5% VAT (typical Dubai) | Buyer-side or seller-side, negotiable |
| **VAT** | First sale of new residential **0%-rated**; subsequent residential **exempt**; commercial property **5%** standard-rated | Federal Tax Authority |

(Sources: DLD e-service pages under `https://dubailand.gov.ae/en/eservices/` (sale, initial sale, mortgage registration); FTA Real Estate VAT Guide VATGRE1 (19 Apr 2021) + MoF VAT page; CBUAE Rulebook for LTV caps)

### Federal Corporate Tax 2023+ — when it touches property

- **Real Estate Investment income** of a **natural person** — any sale, leasing, sub-leasing or renting of UAE land or property that is not conducted, and does not need to be conducted, under a licence from a Licensing Authority — is not a taxable Business (Cabinet Decision 49/2023 Art. 1 and 2(2)(c)); rentals and gains held in own name are out of scope on that condition.
- **Natural persons conducting business**: CT applies only where business turnover exceeds **AED 1,000,000** in a Gregorian calendar year (Cabinet Decision 49/2023 Art. 2(1)); Real Estate Investment income does not count towards that turnover, but a property activity run under, or requiring, a licence falls outside the exclusion.
- **Property held in a UAE company / juridical person**: 0% on taxable income up to AED 375,000, 9% above (Cabinet Decision 116/2022).
- **Non-resident juridical persons**: earning income from UAE immovable property creates a nexus → 9% CT applies (Cabinet Decision 56/2023).

(Source: FTA `https://tax.gov.ae/`, MoF Corporate Tax pages `https://mof.gov.ae/`)

### Inheritance

- **Non-Muslim expats**: Federal Decree-Law 41/2022 on Civil Personal Status (executive regulations Cabinet Resolution 122/2023) covers inheritance and wills for non-Muslim residents, who may instead opt for their home-country law; Abu Dhabi also has its own non-Muslim personal status law (u.ae, updated 30 Sep 2026). A registered **DIFC Will** or **ADGM Will** sets out how UAE assets pass.
  - DIFC Will registration: **AED 10,000** for a single Full Will (AED 15,000 for mirror Full Wills); a Property Will costs AED 7,500 single / AED 10,000 mirror — DIFC Courts Wills Service fee pages (read 2026-10-28).
  - ADGM Wills: equivalent framework in Abu Dhabi.
  - Dubai Law 2/2025 gives the DIFC Courts Enforcement Judge jurisdiction over DIFC-registered wills inside or outside the DIFC (Art. 31(5)); outside the DIFC the writ is executed via the Dubai Courts Enforcement Judge (Art. 32) — a standard formality per the DIFC Courts Wills FAQ, not a bypass (2025 law, source DIFC Courts).
- **Muslims**: Sharia inheritance applies as default; can be modified within Sharia limits (1/3 testamentary share max).
- **No federal inheritance tax** in either case.

### Future risk

- VAT standard rate still 5% (MoF VAT page read 2026-10-28); no rate change found in the MoF or FTA pages read for the Oct 2026 refresh — federal scope.
- Potential extension of corporate tax to passive real estate income for individuals above thresholds — speculative (no announcement).
- Dubai service charge cap discussion has surfaced periodically; no statutory cap yet.

---

## Section: `--rental`

### Long-term residential

- **Mandatory tenancy registration**:
  - **Dubai**: **Ejari** (RERA's tenancy registration system) — tenant or landlord registers contract; AED 220 at a real estate trustee centre or AED 177.75 via the Dubai REST app / DLD website (AED 100 + AED 10 knowledge + AED 10 innovation + service-partner fee and VAT; DLD e-service page, site updated 14 Oct 2026). Required for DEWA connection, school enrolment, visa renewals.
  - **Abu Dhabi**: **Tawtheeq** — the emirate's tenancy-contract register; landlords register the lease, which triggers the 5% municipality fee (u.ae); ADREC publishes the tenancy rules and the Tawtheeq fee schedule.
  - **Sharjah**: registered with the Sharjah Municipality Tenancy Contract section.
- **Rent increase cap (Dubai)** — RERA Smart Rental Index 2025 brackets:

| Current rent vs market index | Max increase allowed |
|---|---:|
| Within 10% of market | **0%** |
| 11–20% below | **5%** |
| 21–30% below | **10%** |
| 31–40% below | **15%** |
| > 40% below | **20%** |

- 2025 reform: **Smart Rental Index** assigns a **1–5 star rating** per residential building (DLD/RERA, Jan 2025) that feeds into the index value used for the Decree 43/2013 rent-increase brackets (DLD Smart Rental Index portal `https://dubailand.gov.ae/en/eservices/rental-index/`) (2026-05-27 verified).
- 90-day notice prior to renewal required for rent increases (**Dubai Law 26/2007 as amended by Law 33/2008** for renewal notice; rent-increase brackets per **Dubai Decree 43/2013** — Determining Rent Increase for Real Property). (Prior playbook reference to "Decree 26/2013" was incorrect — Decree 26/2013 established the Rental Disputes Settlement Centre, a different instrument.) (2026-05-27 verified, source Al Tamimi + DLP Dubai legislation portal)
- **Abu Dhabi rent freeze (Jun 2026)**: ADREC suspended all rent increases on renewals and new lettings (residential / commercial / industrial) **until further notice** — benchmark = rental rate in the property's last registered Tawtheeq contract; cap cut from 5% to 0% (2026 data, source ADREC press release 03 Jun 2026). Tamleek benchmark + ADGM carve-out per law-firm notes only (secondary) — verify at adrec.gov.ae. Model AD rental yields flat until lifted. (source ADREC press release 03 Jun 2026, adrec.gov.ae/en/news/press-release-26---rental-freeze-update — confirm current status on adrec.gov.ae)

### Short-term rentals (holiday homes)

- **Dubai**: **DET (Department of Economy and Tourism)** Holiday Home Permit — formerly called DTCM Holiday Home licence.
  - Property must be furnished + inspected; building NOC required (some OAs / towers prohibit short-let).
  - **Initial registration fee**: AED 1,520 (incl. AED 10 Knowledge + AED 10 Innovation); **Annual permit fee**: from AED 370 per unit (size-dependent for larger units) (2026-05-27 verified, source DET portal + Houst + KeyOne 2025/2026 schedules — prior AED 3,720 figure was stale).
  - **Tourism Dirham**: AED 10/bedroom/night (collected from guest, remitted to DET).
  - **Municipality fee**: 10% of booking revenue (separate from Tourism Dirham). (UNVERIFIED — DET pages returned HTTP 403 in the Oct 2026 refresh; confirm with DET)
  - **Guest registration**: every guest must be registered on DTCM portal within 3 hours of check-in. (UNVERIFIED — DET pages returned HTTP 403 in the Oct 2026 refresh; confirm with DET)
  - **VAT**: 5% applies to short-term rental revenue if total taxable supplies > AED 375k/yr (FTA mandatory registration threshold).
  - **Penalties**: AED 10,000–50,000+ for unlicensed operation; OTAs (Airbnb, Booking) audited by DET.
  - Owners may hold permits directly for up to **8 properties**; beyond that requires a licensed operator. (UNVERIFIED — DET pages returned HTTP 403 in the Oct 2026 refresh; confirm with DET)
- **Abu Dhabi**: **DCT Abu Dhabi** Holiday Home licence (Department of Culture and Tourism).
- **Sharjah / RAK / Ajman**: per-emirate tourism authority; less-developed STR market outside RAK Marjan Island.

### Yield benchmarks (per listing platforms — verify per building)

| Zone | Long-let gross yield | Short-let gross yield (high season) |
|---|---:|---:|
| Dubai Marina apartments | ~6–8% | ~10–14% |
| Palm Jumeirah | ~5–7% | ~9–12% (premium) |
| JVC / Damac Hills 2 | ~7–9% | ~9–12% |
| Downtown | ~5–7% | ~10–13% |
| Saadiyat (Abu Dhabi) | 4.05% apt · 4.47% villa (Bayut FY 2025, on listed prices) | ~7–10% (est., unsourced) |

(Dubai rows: Bayut + Property Finder yield indices, not re-verified 2026-10-28 — treat the ranges as est.; short-let column unsourced est. — *yields gross of service charge, chiller, OA fees, vacancy*. Calibration: DLD 2025 citywide averages give ≈ 5.5% gross for units (AED 1,141 rent ÷ AED 20,666 price per sq m) and ≈ 4.7% for villas (AED 791 ÷ AED 16,791) — computed, mixes rent and sale samples; REIDIN gross yield Sep 2026: Dubai 6.17%, Abu Dhabi 5.89%. Dubai rents are falling — REIDIN rent index −6.81% YoY in Sep 2026 — and Dubai hotel revenue per room fell 35.2% in H1 2026 (Global Property Guide, Oct 2026), so the short-let column is likely stale.)

### Strategic notes

- **Service charge + chiller can take est. 25–40% of gross yield** in many high-end towers (unsourced rule of thumb — pull the building's Mollak budget) — model NET yield, not gross
- **Building OA approval** for STR is the single biggest gate — confirm BEFORE buying if STR is the strategy
- **VAT on commercial leases (5%)** but residential is exempt
- **PIT = 0%** federally (no income tax) — but US/UK/EU tax residents will face their own home-country tax on UAE rental income; the UAE has concluded 137 double taxation agreements (MoF), so check whether your country has one and how it treats income from immovable property

---

## Section: `--work=<profession>`

### Job platforms

- **Bayt.com** — `https://www.bayt.com/` (largest MENA job board)
- **GulfTalent** — `https://www.gulftalent.com/`
- **LinkedIn UAE** — extremely active, especially for white-collar / tech / finance
- **Naukrigulf** — `https://www.naukrigulf.com/` (strong for South Asian diaspora networks)
- **Indeed UAE**, **foundit Gulf** (formerly Monster Gulf — `monstergulf.com` redirects to `https://www.founditgulf.com/`, checked 2026-10-28), **Dubizzle Jobs**

### Visa routes for working

| Visa | Eligibility | Authority |
|---|---|---|
| **Standard Work Permit** | Employment offer from UAE entity | MOHRE (Ministry of Human Resources & Emiratisation) |
| **Green Visa (5 yr)** | Skilled worker: UAE employment contract, MoHRE skill level 1–3, bachelor's degree, salary ≥ AED 15,000/month; freelancer / self-employed: MoHRE freelance or self-employment permit, bachelor's or specialised diploma, annual freelance income over the previous two years ≥ AED 360,000; investors and business partners also eligible (ICP Green Residence Guide, updated 12 Sep 2026) | ICP / GDRFA |
| **Golden Visa (10 yr)** | Property AED 2 M, OR investor/entrepreneur, OR specialised talent / scientist / doctor / outstanding student | ICP |
| **Freelance Permit** | Specific free zones (DMCC, TECOM, twofour54, Fujairah Creative City, etc.) | Per free zone authority |

### Free Zone vs Mainland

- **Mainland company** (DED licence) — can trade UAE-wide; historically required local 51% sponsor — **abolished for most activities since 1 June 2021** (Federal Decree-Law 26/2020); now 100% foreign ownership for ~1,000+ activities (not re-verified 2026-10-28 — the date, statute and activity count were not confirmed at a primary source in this pass; check the activity with the emirate's licensing authority).
- **Free Zone company** — 100% foreign ownership, 0% personal income tax, easier setup, but limited mainland trade (must use mainland distributor or open mainland branch).
- 9% Corporate Tax applies to free zone entities EXCEPT "Qualifying Free Zone Persons", which pay 0% on "Qualifying Income" (Cabinet Decision 100/2023, not an FTA decision; MoF CT page) — narrow conditions.

### Catchment heuristics

- Within 30 min drive of Sheikh Zayed Road / Downtown / DIFC: full white-collar opportunity
- Sharjah residents commuting to Dubai: 60–90 min peak — common but tiring
- Abu Dhabi: separate labour market from Dubai (est. 90 min between centres, light commute population)
- Northern Emirates (RAK / Fujairah): thin mainland labour markets; remote work + property as Golden Visa anchor more typical

### Income benchmarks

- Expatriate professional salary 2025–2026: est. AED 15,000–35,000/month (white-collar mainland; secondary salary guides, not a computed median) — varies massively by sector
- Tech / finance / law senior roles in DIFC / ADGM: AED 40,000–120,000/month + bonuses
- Free zone freelancers: variable; common AED 8,000–25,000/month equivalent invoicing

(Sources: Bayt.com salary guides, GulfTalent annual reports — secondary, not re-verified 2026-10-28; all three income figures above are est. Benchmark against the ICP Green Visa floor of AED 15,000/month for skilled workers)

---

## Section: `--risks`

### Officially declared risks

| Risk | Severity (UAE-wide) | Authority |
|---|---|---|
| **Sandstorms** | Recurrent (esp. shamal winds Mar-Aug) | NCM (National Center of Meteorology) `https://www.ncm.gov.ae/` |
| **Extreme heat (TX > 45°C)** | Increasing — annual occurrence Jun-Sep | NCM + IPCC AR6 Persian Gulf projections |
| **Flash floods / drainage failure** | Documented Apr 2024 record event | Dubai Municipality + NCM |
| **Seismicity** | Generally low; northern emirates closer to active Iranian Zagros fault zone | NCM Seismology Department (Seismic Monitoring Section; event map `https://earthquakes.ncm.gov.ae/`) — ncm.gov.ae lists no body called NCESI (checked 2026-10-28) |
| **Coastal SLR exposure** | Long-term (decades) for low-lying reclaimed islands | IPCC AR6 sea-level projections (see Climate to 2050) + Climate Central (secondary); the earlier "NCCS not formally federal" note cited no source and is withdrawn |
| **Subsidence** | Some reclaimed/coastal areas anecdotal | No federal cadastre — confirm geotechnical with developer / consultant |

### April 2024 flood event — what changed

- **16 Apr 2024**: 254 mm in less than 24 hours at Khatm Al Shakla (Al Ain), in the 24 hours to 9 pm on 16 Apr — the **heaviest rainfall since UAE data collection began in 1949** (NCM statement via WAM, as carried by Gulf News, 17 Apr 2024); at least four deaths in the UAE and at least 20 in Oman (World Weather Attribution, 25 Apr 2024 — secondary).
- **Cause / attribution** (scientific studies — secondary): World Weather Attribution (25 Apr 2024) finds from observations that the event was 10–40% more intense than it would have been in an El Niño year in a 1.2 °C cooler climate, but says model–observation disagreement prevents concluding with certainty that human-induced climate change was the main driver. The Met Office + Newcastle University study (Davies et al., *Weather and Climate Extremes* vol. 51, Mar 2026 issue, online 11 Dec 2025) traces the rainfall to mesoscale convective systems in a deeply saturated atmosphere and applies the Davies four-stage, three-layered conceptual model — it is not a *Nature* paper and gives no climate-attribution likelihood figure.
- **Reform — Dubai "Tasreef" stormwater plan**: AED 30 bn (≈ USD 8.2 bn at the 3.6725 peg, computed), approved 24 Jun 2024 by Sheikh Mohammed bin Rashid; drainage capacity +700%, completed in phases by **2033** (Dubai Media Office, 24 Jun 2024). Phase 3: Dubai Municipality awarded AED 3 bn of contracts for about 100 km of main stormwater lines in Jumeirah, Umm Suqeim, Al Safa, Al Manara, Al Quoz, Al Barsha, Al Wasl, Za'abeel, Al Bada'a, Al Satwa and Al Marmoom (Dubai Media Office, 25 Oct 2026).
- **Neighbourhood project (not emirate-wide)**: AED 277 m sewerage + rainwater drainage network in Nad Al Sheba 3 completed Jun 2025 (2025 data, source Dubai Media Office) — 24 km sewerage + 31 km gravity rainwater network; Dubai Municipality frames it within the Tasreef and sewerage programmes.
- **Implication for buyers**: low-lying communities (some Mirdif, Al Quoz, Sharjah border areas, IMPZ) experienced multi-day water-logging — verify drainage history with OA + developer.

### Build-quality / fire risk

- **Cladding fires** (press reports — secondary): The Torch, Dubai Marina (Feb 2015, again Aug 2017), The Address Downtown (New Year's Eve 2015 — a senior Dubai Civil Defence officer said its cladding did not meet fire safety standards), Sulafa Tower (Jul 2016), 8 Boulevard Walk, Downtown (Nov 2022). The earlier "23 Marina (2017)" entry is not confirmed by any source found and is dropped.
- **UAE Fire and Life Safety Code of Practice** (UAE Civil Defence), introduced Jan 2017: aluminium composite panel cladding prohibited and non-combustible cladding required on new buildings; further updates came into effect the following year. Dubai: retrofit is **not** mandatory for buildings built before the code, and existing cladding fitted before the updated standards is legal (Dubai Civil Defence as reported by The National, 24 Jan 2023 — secondary). Sharjah: Sharjah Civil Defence told existing buildings over 23 m to replace their cladding with non-flammable material (2016 orders), and the Ruler approved AED 100 m to re-clad 40 high-risk buildings, with 163 more to follow (Gulf News, 24 Apr 2023 — secondary). The earlier "2018 update mandated retrofits" claim is withdrawn — verify the current rule with the emirate's Civil Defence.
- Verify cladding certification + fire NOC (Civil Defence) for towers built 2000–2017.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-2000** | Older Sharjah / Dubai Bur Dubai stock — variable quality, occasional asbestos roofing |
| **2000–2008 boom** | Rapid construction phase — uneven quality, cladding risk (see above) |
| **2008–2014 GFC stalled** | Many off-plan projects cancelled or delayed years; verify Title Deed transferred + project completed |
| **2014–2020** | Modernised codes; better quality |
| **Post-2020** | Tightened fire standards (Fire and Life Safety Code of Practice, Jan 2017 + later updates), Dubai Building Code (approved by the Dubai Executive Council 7 Oct 2020, Dubai Media Office) and emirate green-building rules (e.g. Al Sa'fat – Dubai Green Building System, Dubai Municipality); federal green building codes from the Ministry of Energy and Infrastructure (launched Mar 2022) target government buildings (press — secondary); verify the applicable code with the emirate municipality |

### Climate to 2050 (IPCC AR6 Persian Gulf)

- UAE annual mean temperature, 2040–2059, CMIP6 multi-model median anomaly: +1.52 °C (SSP1-2.6), +1.72 °C (SSP2-4.5), +1.83 °C (SSP3-7.0), +2.24 °C (SSP5-8.5); 10th–90th percentile spread from +0.92 °C (SSP1-2.6) to +3.13 °C (SSP5-8.5) (World Bank Climate Change Knowledge Portal API, cmip6-x0.25, fetched 2026-10-28 — secondary data portal). Baseline not stated with the anomaly data: 1995–2014 is inferred (the portal's only historical reference period), not confirmed. The earlier "+1.5–3.0 °C vs 1981–2010" range had no source
- Extremes of wet-bulb temperature around the Arabian Gulf are likely to approach and exceed the **35 °C survivability threshold** under business-as-usual emissions (Pal & Eltahir, *Nature Climate Change* 6, 197–200, online 26 Oct 2015); the "by 2070+" timing is not stated in the abstract — verify in the paper
- More extreme rain events (April 2024 type) — drainage capacity planning is now policy priority
- Sea-level rise: IPCC AR6 global mean rise by 2050 vs 1995–2014 is a median of 0.18 m (SSP1-1.9) to 0.23 m (SSP5-8.5), likely range 0.15–0.29 m across scenarios (IPCC AR6 data as tabulated by the Hong Kong Observatory); local Gulf values may differ — the earlier "~30 cm by 2050 (median)" was above every scenario median → exposure for Palm Jumeirah outer fronds, Yas low-lying, Saadiyat coastal villas — verify elevation vs SLR projection at parcel level

### Mandatory diagnostics at sale

| Document | Required because | Issuing authority |
|---|---|---|
| **Title Deed (current)** | Verify owner + encumbrances | DLD / ADREC / etc. |
| **Mortgage Discharge Letter** (if mortgaged) | Bank confirms loan paid off | Lending bank |
| **NOC from Developer / OA** | Confirms service charges paid up + permits transfer | Master developer / OA |
| **Service charge clearance certificate (Mollak)** | Dubai — confirms no outstanding fees | Mollak via OA |
| **Affection Plan** | Cadastral plot info | Dubai Municipality / equivalent |
| **Building Completion Certificate** (off-plan completion) | Project legally complete | Master developer |
| **Fire NOC / Civil Defence certificate** | Cladding + fire compliance | Dubai Civil Defence / MoI General Command of Civil Defence |
| **DEWA / TAQA Distribution clearance** | No outstanding utility bills (DEWA sends the clearance certificate automatically once the final bill is settled) | DEWA / TAQA Distribution (ex-ADDC / AADC) |

(Note: The UAE has no mandatory energy performance certificate equivalent for resale yet; sustainability ratings exist for new builds (DM Green Building, Estidama Pearl) but are not retroactive.)

### Risk dashboard (UAE 2026)

| Class | Severity | Action priority |
|---|---|---|
| **Heat stress + cooling cost** | 🟠 increasing | Verify chiller economics; assume worsening to 2050 |
| **Cladding (towers 2000–2017)** | 🟠 era-dependent | Demand Civil Defence NOC + certification |
| **Flash flood (low-lying communities)** | 🟡 → 🟠 post-2024 | Check drainage history + Tasreef coverage |
| **Off-plan completion risk** | 🟠 always | Verify RERA project status + escrow + developer track record |
| **Service charge inflation** | 🟡 | Pull 5-year history + check Mollak |
| **Cyclone / coastal storm** | 🟢 (low frequency, increasing concern long-term) | — |
| **Earthquake** | 🟢 most of UAE; 🟡 in northern emirates near Zagros | Standard structural review |

---

## Section: `--mains`

### Universal in serviced areas

UAE urban property is essentially **always on mains** for water + electricity + sewer + cooling — the question is which provider and how the bills are structured.

| Emirate | Provider |
|---|---|
| **Dubai** | **DEWA** (Dubai Electricity & Water Authority) `https://www.dewa.gov.ae/` |
| **Abu Dhabi** | **TAQA Distribution** — ADDC (Abu Dhabi Distribution Company) and AADC brought under one brand, operating as a single entity serving customers throughout Abu Dhabi; new brand on bills from Jan 2025 (TAQA via Abu Dhabi Media Office, 16 Sep 2024) `https://taqadistribution.com/` |
| **Al Ain** | **TAQA Distribution** (formerly AADC, Al Ain Distribution Company — `aadc.ae` redirects to `taqadistribution.com`, checked 2026-10-28) |
| **Sharjah** | **SEWA** (Sharjah Electricity, Water & Gas Authority) `https://www.sewa.gov.ae/` |
| **Northern Emirates** (Ajman, RAK, UAQ, Fujairah) | **EtihadWE** (Etihad Water and Electricity — established 2020 under Federal Decree-Law No. 31 per EtihadWE's About page, earlier cited here as Federal Law No. 31 of 2020; builds on the former Federal Electricity & Water Authority, FEWA) `https://etihadwe.ae/en/Pages/default.aspx` |
| **District cooling** | **Empower** (Dubai dominant), **Tabreed** (UAE-wide), **Emicool** (Dubai) — separate bill |

### Verification

1. Pull existing **DEWA / TAQA Distribution (ex-ADDC / AADC) / SEWA / EtihadWE** account info from seller — confirms active mains + no overdue
2. Off-plan: confirm developer has utility connection on the master plan (verify NOC at handover)
3. Some compounds use **TSE (treated sewage effluent)** for landscape irrigation — separate cost line
4. Rural / undeveloped Northern Emirates plots: may not yet have utility connection; verify with EtihadWE + master developer

### Tariffs (residential indicative)

- **DEWA** (residential, per month): electricity AED 0.23/kWh for 0–2,000 kWh, 0.28 for 2,001–4,000, 0.32 for 4,001–6,000, 0.38 above 6,000; water AED 7.70/m³ for 0–27 m³, 8.80 for 27–54, 10.12 above 54; plus a fuel surcharge that DEWA publishes monthly (Sep 2026: AED 0.060/kWh and AED 1.100/m³, the same figures in every archived copy checked back to May 2025) and 5% VAT (DEWA slab-tariff page `https://www.dewa.gov.ae/en/consumer/billing/slab-tariff`, Sep 2026 — returns 403 to non-UAE automated requests)
- **District cooling**: split into a fixed **demand (capacity) charge** per contracted RT + a **consumption charge**. Empower (Dubai): demand charge AED 750 per RT per year billed monthly in advance; consumption AED 0.568 per RT-hour (page wording: "AED 0.568 fils per RT per hour"); meter maintenance AED 50 per quarter or AED 30 per month; 5% VAT (Empower Charges Explanation page, checked 2026-10-28). Tabreed / Emicool rates: verify with the provider. All-in cost per sqft: est. AED 10–18/sqft/year — no published source; depends on contracted RT and usage
- **Housing fee (Dubai)**: tenants pay 5% of the yearly rent to Dubai Municipality, added to the monthly electricity and water bill (u.ae, checked 2026-10-29); Dubai Municipality also applies it to owned units on the basis of rental value (DM "Adjust Housing Fees" service) — no primary source for how an owner's rental value is set (e.g. RERA index) was found in the Oct 2026 check; verify with Dubai Municipality

### Costs

| Scenario | Cost |
|---|---:|
| Connection (already serviced area, Dubai) | AED 2,155 flat / AED 4,155 villa = refundable DEWA security deposit AED 2,000 / 4,000 + AED 155 activation (small meters; large meters AED 300 + fees) (DEWA Move-in page, Oct 2026); other emirates: verify with the provider |
| Off-plan handover utility activation | Often included; verify with developer |
| Chiller "freeze" between tenants (capacity charge continues) | Empower: demand charge AED 750 per contracted RT per year, billed monthly by days in the month (≈ AED 62.50 per RT per month, computed) + meter maintenance (AED 50 per quarter or AED 30 per month, depending on location) + 5% VAT, still charged while disconnected — e.g. 6 RT ≈ AED 375 a month + meter maintenance before VAT (computed); voluntary disconnection AED 150 per instance (Empower, checked 2026-10-28); other providers: verify |
| Disconnection / clearance certificate (Dubai) | DEWA move-out AED 145 (small meters: 125 + 10 knowledge + 10 innovation fee) or AED 320 (large meters: 300 + 20), computed from DEWA's fee list; clearance certificate sent automatically once the final bill is settled (DEWA Move-out page, May 2026) |

---

## Cost benchmarks (UAE 2026)

| Item | Cost |
|---|---:|
| **DLD transfer fee (Dubai)** | **4% of price** |
| **ADREC transfer fee (Abu Dhabi)** | **2% of price** |
| **Title Deed issuance** | AED 250 (+ AED 250 map fee for villas and apartments) |
| **Trustee office fee** | AED 4,000 + VAT (sale value AED 500,000 or more); AED 2,000 + VAT below |
| **Mortgage registration (DLD)** | 0.25% of mortgage + AED 270 (AED 250 title deed + AED 10 + AED 10) + service-partner fee AED 4,000 + VAT |
| **Bank mortgage processing** | 0.5–1% of loan |
| **Property valuation (mortgage)** | AED 2,500–3,500 |
| **Real estate agent commission** | 2% + 5% VAT (typical) |
| **Conveyancer / lawyer** (optional) | AED 5,000–15,000 |
| **DIFC Will registration** (single) | AED 10,000 |
| **Holiday Home Permit (DET)** | initial registration AED 1,520; annual permit from ~AED 370/unit |
| **Service charges (annual)** | AED 3–70 / sqft / yr (tier-dependent) |
| **District cooling (annual)** | est. AED 10–18 / sqft / yr (residential; no published source — Empower bills AED 750 per contracted RT per year + AED 0.568 per RT-hour, see `--mains`) |
| **Annual housing fee (Dubai)** | 5% of annual rental value (via DEWA) |
| **Annual property tax** | **None** |
| **Total transaction cost (buyer side, Dubai cash secondary)** | **~6–8% of price** (est.: 4% DLD + 2% agent + 5% VAT on the commission + AED 4,200 trustee incl. VAT + AED 520 DLD title-deed, map, knowledge and innovation fees + optional lawyer; assumes the buyer pays the full 4%) |
| **Total transaction cost (Dubai with mortgage)** | ~8–10% of price |

## Active fiscal incentives (2026)

- **Golden Visa (10-year)**: property ≥ AED 2 M (single or aggregate)
- **Investor Visa (2-year)**: sole owners — no minimum property value; joint owners — ≥ AED 400,000 each (prior AED 750k floor abolished, DLD 29 Apr 2026)
- **Retirement Visa (5-year)**: 15 years' service or age ≥ 55 (ICP; GDRFA Dubai and u.ae say both); property ≥ AED 1 M or an AED 1 M deposit (ICP; GDRFA Dubai and u.ae join them with "and"), OR fixed income ≥ AED 240k/yr (ICP + GDRFA Dubai; u.ae gives AED 180k, AED 240k for Dubai)
- **Green Visa (5-year)**: skilled workers / freelancers
- **0% personal income tax** on rental income (federal — but check home-country tax residency obligations)
- **0% VAT first sale of new residential** (within 3 years of completion); subsequent residential exempt
- **0% capital gains tax** on individual property sales (a natural person's Real Estate Investment income is outside CT unless conducted, or required to be conducted, under a licence — Cabinet Decision 49/2023)
- **Free Zone "Qualifying Income"** 0% CT (narrow conditions; Cabinet Decision 100/2023)
- **Dubai First-Time Home Buyer Programme** (DLD): UAE residents of any nationality, 18+, owning no freehold residential property in Dubai, buying below AED 5M — priority access to new launches, preferential prices on off-plan units from participating developers, credit-card instalments for registration fees, and offers from 5 participating banks (DLD e-service page, site updated 14 Oct 2026)

## Common listing platforms

- **Bayut** — `https://www.bayut.com/` (blocks scripted requests with HTTP 503; loads in a browser, checked 2026-10-28)
- **Property Finder** (UAE-wide, strong analytics) — `https://www.propertyfinder.ae/`
- **Dubizzle Property** — `https://www.dubizzle.com/property-for-sale/`
- **Houza** — challenger portal; ceased operations Feb 2024 per trade press (`https://www.onlinemarketplaces.com/articles/emirati-challenger-portal-houza-folds-as-investors-lose-appetite/`, 4 Apr 2024 — secondary) and `houza.com` no longer serves a website (2026-10-21 verified); no successor — use Bayut / Property Finder / Dubizzle above
- **LuxHabitat** + **LuxuryProperty.com** + **Sotheby's UAE** (high-end)
- **JustProperty.com** — `justproperty.com` now 301-redirects to `https://www.propertyfinder.com` (checked 2026-10-28); no separate portal — use Property Finder
- Developer direct portals (Emaar, Damac, Aldar, Nakheel, Sobha) for off-plan

## Caveats unique to UAE

- **Freehold-zone-only restriction crucial** — non-GCC outside designated freehold zones cannot acquire freehold title; verify zone status before any reservation
- **Off-plan completion risk** — RERA escrow + Project Status register protects buyer funds, but **delays of 12–36+ months** are common; verify developer track record (Emaar / Aldar / Nakheel / Damac historically reliable; smaller developers higher variance)
- **Service charges + chiller can be 25–40% of gross rental yield** in high-end towers — model NET, never gross
- **Building OA short-term-rental policy is the single biggest STR gate** — verify BEFORE buying if STR is the strategy
- **No income tax personally; 9% corporate tax from Jun 2023** for property held in a juridical person above AED 375k profit
- **DIFC / ADGM Wills are critical for non-Muslim foreign owners** — without one, a non-Muslim resident's estate follows Federal Decree-Law 41/2022 or the home-country law they elected, and Abu Dhabi applies its own non-Muslim personal status law (u.ae, updated 30 Sep 2026, which covers residents only); a registered will removes that uncertainty, especially for non-resident owners — confirm with a UAE lawyer
- **Apr 2024 floods exposed drainage limits** — verify drainage history of low-lying communities; Tasreef plan phased to 2033
- **Cladding (towers 2000–2017)**: demand Civil Defence Fire NOC; multiple historical cladding fires
- **Federal AML rules require source-of-funds documentation** — bank statements, employment records, prior asset sale proof; freehold purchases paid with AED 55,000 or more in physical cash, or in virtual assets, must be reported by the broker on goAML (REAR, MoE Circular 05/2022)
- **Currency**: AED pegged to USD at 3.6725 — **no FX risk vs USD**; meaningful FX risk vs EUR / GBP / other floating currencies
- **No federal cadastre** — each emirate has its own register; cross-emirate portfolio requires multi-cadastre lookup
- **VAT 5% on commercial property** (and STR if turnover > AED 375k/yr) — easy to forget for foreign investors

## Reddit / forum sources

- **r/dubai** (largest active expat community)
- **r/UAE**
- **r/ADXfinance** (Abu Dhabi finance/investment)
- **Bayut Blog** (`https://www.bayut.com/mybayut/`) — community-style guides
- **ExpatWoman.com** forums — practical expat property + service-charge discussions
- **Dubizzle community pages**

## Verification authorities

| Authority | When to call |
|---|---|
| **Dubai Land Department (DLD)** | Title Deed verification; designated freehold zone confirmation; transfer registration |
| **DLD Trustee Offices** (RERA-licensed) | Mandatory venue for Dubai secondary-market transfers |
| **RERA** (under DLD) | Off-plan project status, escrow status, broker licence verification |
| **ADREC** | Abu Dhabi cadastre + Tamleek zone confirmation |
| **Sharjah Real Estate Registration Department** | Sharjah cadastre |
| **ICP** (Federal Authority for Identity, Citizenship, Customs and Port Security) | Golden Visa, Green Visa, Retirement Visa applications |
| **GDRFA Dubai** | Dubai-specific residency processing |
| **Federal Tax Authority (FTA)** | VAT clarifications, Corporate Tax registration |
| **MoET** (Ministry of Economy and Tourism, formerly Ministry of Economy / MOEC — `moet.gov.ae`) | AML/CFT supervisor for real estate agents and brokers (REAR filings on goAML) |
| **Dubai Police** | Off-plan / real estate fraud reports |
| **DIFC Wills Service Centre** | Non-Muslim wills (Dubai/UAE assets) |
| **ADGM Wills Service** | Non-Muslim wills (Abu Dhabi-anchored) |
| **Dubai Civil Defence / MoI General Command of Civil Defence** | Fire NOC, cladding compliance |
| **Dubai Municipality** | Makani address, building permits, drainage history |

## Quirks to know

- **Makani number** (Dubai) — 10-digit address code; required for utility setup, deliveries, emergency response
- **Title Deed (Sanad Mulkiyya)** issued in Arabic — bilingual EN/AR is standard but the Arabic prevails legally
- **Oqood** (off-plan) ≠ Title Deed — only the Title Deed at handover gives full ownership rights
- **Initial Sale Contract / SPA** — pre-handover binding agreement
- **Post-handover payment plans** common for off-plan (e.g., 50/50, 60/40, 80/20 over 2–5 years post-handover) — model the IRR carefully; effectively developer financing
- **Secondary-market freehold transfers** in Dubai must be done at a **DLD-registered Trustee Office** (not lawyer-only)
- **Mollak system** — DLD's centralised service-charge regulation portal (since 2018); each tower has a registered annual budget
- **Service-charge "owner committee"** — buyers should attend AGMs to influence budgets
- **Cooling provider lock-in** — district cooling contracts are often 25–30 years between developer and provider; tenants/owners cannot switch
- **Off-plan handover defects** — most contracts give 1-year defects liability period (developer warranty) + 10-year structural warranty (federal)
- **Courts**: civil disputes over property typically heard in **Rental Disputes Centre** (Dubai) for tenancy matters; Real Estate Court for ownership; DIFC Courts for opt-in English-law contracts; Dubai Courts for default

## Source URL templates

| Source | URL |
|---|---|
| DLD home | `https://dubailand.gov.ae/en/` |
| DLD eServices (transfer / oqood / etc.) | `https://dubailand.gov.ae/en/eservices/` |
| DLD Smart Rental Index | `https://dubailand.gov.ae/en/eservices/rental-index/` |
| DLD Open Data | `https://dubailand.gov.ae/en/open-data/` |
| Dubai REST app (mobile) | `https://dubailand.gov.ae/en/eservices/dubai-rest/` |
| ADREC | `https://adrec.gov.ae/` |
| Sharjah Real Estate Registration | `https://www.shjrerd.gov.ae/` ⚠️ timed out from outside the UAE (checked 2026-10-28) |
| ICP (Federal — visas) | `https://icp.gov.ae/` |
| GDRFA Dubai | `https://www.gdrfad.gov.ae/` |
| Federal Tax Authority | `https://tax.gov.ae/` |
| Ministry of Finance (Corporate Tax) | `https://mof.gov.ae/` |
| MOET — Ministry of Economy and Tourism, formerly MOEC (AML/CFT supervisor for real estate agents and brokers) | `https://www.moet.gov.ae/en/` (moec.gov.ae redirects here, checked 2026-10-28) |
| NCM (weather / climate) | `https://www.ncm.gov.ae/` |
| DEWA | `https://www.dewa.gov.ae/` ⚠️ returns 403 to non-UAE automated requests (checked 2026-10-28) |
| TAQA Distribution (ex-ADDC / AADC, Abu Dhabi) | `https://taqadistribution.com/` (addc.ae returns 403 to automated requests; aadc.ae redirects here — checked 2026-10-28) |
| SEWA | `https://www.sewa.gov.ae/` |
| EtihadWE (formerly FEWA) | `https://etihadwe.ae/en/Pages/default.aspx` |
| Dubai Municipality | `https://www.dm.gov.ae/` |
| Makani (Dubai address) | `https://www.dm.gov.ae/open-data2/open-data-for-makani` |
| TAMM (Abu Dhabi unified services) | `https://www.tamm.abudhabi/` |
| RTA Dubai | `https://www.rta.ae/` |
| Dubai Civil Defence (emirate-level; UAE federal body is the MoI General Command of Civil Defence) | `https://www.dcd.gov.ae/` ⚠️ reachable from the UAE only |
| DIFC Courts Wills Service | `https://www.difccourts.ae/difc-courts-wills/` |
| ADGM | `https://www.adgm.com/` |
| DET (holiday home permits, Dubai) | `https://www.dubaidet.gov.ae/` ⚠️ returns 403 to non-UAE automated requests (checked 2026-10-28) |
| Bayut Index | `https://www.bayut.com/property-market-analysis/index/` (old `/index/` path redirects here, checked 2026-10-28) ⚠️ answers scripted requests with a 503 bot check; loads in a browser |
| Property Finder | `https://www.propertyfinder.ae/` |
| Property Monitor | `https://propertymonitor.com/` |

## Status

✅ **Fully populated** (initially populated 2026-05-01).

**Coverage check**: foreign-buyer eligibility, price, traffic, tax, rental, work, risks, mains all have primary government / regulated entity sources + cost benchmarks + caveats; Golden Visa and Retirement Visa thresholds re-read on the ICP and GDRFA Dubai pages, and DLD fees on the DLD e-service pages, in the 2026-10-28 refresh, which corrected the retirement income floor (AED 180,000 → 240,000) and the title-deed, knowledge / innovation and mortgage-registration fees.

**Confidence**: **HIGH** for the federal rules re-read on primary sources on 2026-10-28 — Golden Visa AED 2M property route with its loan, off-plan and family terms and the Green Visa criteria (ICP guides, Sep 2026), VAT regime incl. the 3-year first-supply condition (MoF, FTA VATGRE1), Corporate Tax scope (Cabinet Decisions 116/2022, 49/2023, 56/2023 and 100/2023), the AED 3.6725 peg rate (CBUAE), the AML basis and REAR cash trigger (Decree by Law 10/2025, Cabinet Resolution 134/2025, MoE Circular 05/2022 — MoET AML page) and the CBUAE mortgage LTV caps; HIGH for the Dubai DLD 4% transfer fee, the title-deed, map, knowledge / innovation, trustee, mortgage-registration and Ejari fees and the First-Time Home Buyer Programme (DLD e-service pages, site updated 14 Oct 2026), the Abu Dhabi 5% tenant municipality fee (Resolution 49/2018, u.ae), the ADREC 2% off-plan fee, the Abu Dhabi Law 13/2019 framework (ADREC-hosted text; its 16 Apr 2019 date is secondary) and the Jun 2026 ADREC rent freeze, DIFC Wills fees, Federal Decree-Law 41/2022 for non-Muslim residents (u.ae) and Dubai Law 2/2025, and the Dubai rent-increase brackets and Smart Rental Index star rating (DLD portal, last verified 2026-05-27, not re-read in this refresh); HIGH for the DLD 2025 price, rent and transaction averages (Annual Data Review 2025), ADREC's H1 2026 market release, the Tasreef plan and its Phase 3 award (Dubai Media Office, 24 Jun 2024 and 25 Oct 2026), the DEWA slab tariff, fuel surcharge and move-in / move-out fees (DEWA pages read from Internet Archive captures of May–Oct 2026, as dewa.gov.ae returns 403 outside the UAE), Empower's published cooling rates and the ADDC / AADC merger into TAQA Distribution. **MEDIUM** for the Retirement Visa terms (ICP and GDRFA Dubai give the AED 240,000 income floor but differ on whether service and age, and property and deposit, are alternatives; u.ae still gives AED 180,000 — the conflict is shown in the body), the 2026 Dubai and Abu Dhabi price trend and community AED/sqft levels (REIDIN, ValuStrat and CBRE via Global Property Guide — secondary; Bayut Index asking prices — listing tier; DLD's official index has no 2026 quarter yet; Abu Dhabi has less granular open data than Dubai), the ADREC fee on ready property (Resolution 49/2018 allows 1–4%), emirate-by-emirate detail outside Dubai/Abu Dhabi (RAK/Ajman/Fujairah/UAQ less standardised — the Dubai "~30+ more" zones, the extra Abu Dhabi zones and the RAK and Ajman lists are unconfirmed, and transfer fees vary and need per-deal confirmation with the relevant municipality), Sharjah usufruct vs freehold-for-Arabs distinction (usufruct up to 100 years confirmed on u.ae; SRERD timed out, so the nationality rules and the 2025 residency-visa claim stay unverified — verify with SRERD per nationality), the April 2024 flood figures (NCM statement read in a Gulf News copy of the WAM report; deaths and attribution from World Weather Attribution — secondary), cladding and fire-code history (press — Dubai retrofit not mandatory, Sharjah re-cladding), climate projections (World Bank CCKP with an inferred 1995–2014 baseline; IPCC AR6 sea level via the Hong Kong Observatory) and the NCM hazard rows (pages render client-side), the DET holiday-home permit fees (last verified 2026-05-27; DET returned 403 in the Oct 2026 refresh), the Blue Line opening on 9 Sep 2029 (RTA announcement, press only), mainland 100% ownership (Decree-Law 26/2020, not re-verified) and utility fees outside Dubai (TAQA Distribution, SEWA and EtihadWE not fetched). **LOW** for figures the refresh could not verify or that are labelled est. — Dubai long-let and short-let yield ranges, service charges and the service-charge tier table, the service-charge share of yield, chiller and district-cooling per-sqft costs, Northern Emirates transfer fees, bank, valuation, conveyancer and agent fees and the transaction-cost totals, the DET short-let rules marked UNVERIFIED, the Sheikh Zayed Road traffic count, salary ranges and commute heuristics, the off-plan discount and branded-residence premium, and the ValuStrat Q3 2025 Abu Dhabi row.

**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; Northern Emirates utility (EtihadWE) corrected 2026-09-18 per u.ae). Connectivity / finance / rental / risks / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Connectivity / finance / price / rental / risks / tax / visa tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile (incl. header framing) | 2026-10-28 | 2026-10-28 Tier-A refresh | Peg rate (CBUAE) and the recent-reforms bullets re-read (VAT 3-year rule, Corporate Tax Cabinet Decisions, Golden Visa loan and off-plan terms) plus Sharjah usufruct up to 100 years (u.ae); peg start year and the Abu Dhabi Law 13/2019 date secondary only; postal, cadastre, identifier and Dubai 2040 lines not checked |
| Foreign buyer eligibility | 2026-10-28 | 2026-10-28 Tier-A refresh | Golden Visa (ICP, 10 Sep 2026), Retirement Visa (ICP and GDRFA Dubai; the u.ae AED 180,000 conflict is shown) and AML (Decree by Law 10/2025, AED 55,000 REAR trigger) re-verified; the Dubai "~30+ more" zones, extra Abu Dhabi zones, RAK and Ajman lists and the Sharjah nationality and visa rules unconfirmed (SRERD timed out) |
| `--price` | 2026-10-28 | 2026-10-28 Tier-A refresh | Dubai led by DLD 2025 averages and the DLD index (no 2026 quarter); premium-zone table rebuilt from REIDIN Q1 2026 transacted and Bayut Index Sep 2026 asking prices; ADREC H1 2026 release; the 2026 trend rests on REIDIN, ValuStrat and CBRE via Global Property Guide (secondary); ValuStrat Abu Dhabi Q3 2025 row, off-plan discount and branded premium unverified (est.) |
| `--traffic` | 2026-10-28 | 2026-10-28 Tier-A refresh | RTA Blue Line page re-read (no opening date on it; 9 Sep 2029 per press reports of the RTA announcement); Sheikh Zayed Road 200,000+ v/d labelled est.; E-route designations not re-checked; MoEI site timed out; verdict bands are skill thresholds |
| `--tax` | 2026-10-28 | 2026-10-28 Tier-A refresh | DLD fees, CBUAE LTV caps, Abu Dhabi 5% tenant fee, ADREC 2% off-plan fee, Corporate Tax decisions, Federal Decree-Law 41/2022, DIFC Will fees and VAT re-verified; service charges and the tier table, chiller, Northern Emirates fees, professional fees, the owner housing-fee basis and the Muslim one-third rule unverified |
| `--rental` | 2026-10-28 | 2026-10-28 Tier-A refresh | Ejari and Tawtheeq rules and fees, 137 tax treaties (MoF), Saadiyat yields (Bayut FY 2025) and the DLD-computed yield calibration re-verified; DET short-let figures blocked (403) and marked UNVERIFIED; Dubai yield ranges est.; Smart Rental Index brackets not re-read (last verified 2026-05-27) |
| `--work` | 2026-10-28 | 2026-10-28 Tier-A refresh | Green Visa criteria (ICP, 12 Sep 2026), Qualifying Free Zone 0% rate and Cabinet Decision 100/2023 (MoF) and job boards (Monster Gulf → foundit Gulf) re-verified; mainland-ownership date, statute and activity count, salary ranges and commute heuristics unverified |
| `--risks` | 2026-10-28 | 2026-10-28 Tier-A refresh | April 2024 rainfall (NCM via a WAM copy) and WWA attribution, the Met Office study, Tasreef incl. Phase 3 (Dubai Media Office), cladding fires and fire-code rules by emirate (press), NCM seismology and climate projections (World Bank CCKP, inferred baseline; IPCC AR6 sea level via HKO) re-checked; NCM hazard rows, subsidence, the low-lying list, pre-2020 build-era rows, the EPC note and the wet-bulb timing unverified |
| `--mains` | 2026-10-28 | 2026-10-28 Tier-A refresh | TAQA Distribution (ex-ADDC / AADC), EtihadWE statute (both citation forms shown), DEWA slabs, fuel surcharge and move-in / move-out fees (archived DEWA pages; 403 outside the UAE), Empower rates and the Dubai housing fee (u.ae) re-verified; cooling per-sqft cost est.; TAQA Distribution, SEWA and EtihadWE fees not fetched |
| Cost benchmarks | 2026-10-28 | 2026-10-28 Tier-A refresh | All 17 rows checked: title-deed, trustee and mortgage-registration rows corrected, cash total rebuilt as est.; bank, valuation, agent, conveyancer, DET permit, service-charge, cooling and mortgage-total rows unverified |
| Active fiscal incentives | 2026-10-28 | 2026-10-28 Tier-A refresh | Retirement Visa, VAT 3-year, capital-gains licence condition and Qualifying Free Zone (Cabinet Decision 100/2023) lines aligned with the body; Dubai First-Time Home Buyer Programme added (DLD); "0% PIT" has no positive primary statement |
| Common listing platforms | 2026-10-28 | 2026-10-28 Tier-A refresh | Property Finder, Dubizzle, LuxHabitat, LuxuryProperty.com and Sotheby's UAE live; JustProperty redirects to Property Finder; Houza still closed; developer portals not checked |
| Caveats unique to UAE | 2026-10-28 | 2026-10-28 Tier-A refresh | Legal / fiscal lines only: inheritance and AML-reporting caveats corrected; off-plan delays, the OA gate and the cadastre line unverified; flood and cladding caveats consistent with `--risks`; service-charge share (est.) not re-checked |
| Source URL templates | 2026-10-28 | 2026-10-28 Tier-A refresh | 28 URLs checked: MOEC → MOET, ADDC → TAQA Distribution, Bayut Index re-pointed to `/property-market-analysis/index/`; DEWA and DET return 403 and SRERD times out outside the UAE; DCD reachable from the UAE only |

## Extension TODOs (deepen on first real run)

- [ ] Per-emirate transfer fee + trustee fee schedule (Northern Emirates beyond Dubai/AD)
- [ ] Abu Dhabi citywide AED/sqft per-zone benchmarks comparable to Dubai's Bayut Index granularity
- [ ] Mollak per-building service-charge history extraction workflow
- [ ] DET Holiday Home Permit per-building NOC compatibility list (which towers permit STR)
- [ ] Tasreef rollout schedule per community (which neighbourhoods upgrade first 2025–2033)
- [ ] Cladding compliance lookup for towers built 2000–2017 (Civil Defence database)
- [ ] Free Zone vs mainland Corporate Tax decision tree for property-holding SPVs
- [ ] Sharjah / RAK / Ajman per-development freehold zone master list
- [ ] Branded residence premium calibration (Bulgari / Armani / Atlantis / etc.) per sqft
- [ ] DIFC vs ADGM Will choice decision tree for foreign owners

## Update history

- **2026-10-29** — Tier-A refresh (market, tax-legal, risk-infra; facts checked 2026-10-28, corrections re-checked 2026-10-29); playbook-level date not re-stamped because none of `--price`, `--tax`, `--rental`, `--risks` and `--mains` is fully primary-verified
  - Checked, not fully verified (facts checked — changed / confirmed / unverifiable): Country profile (incl. header) 14 — 4 / 8 / 2; Foreign buyer eligibility (zones, Golden / Retirement visa, AML) 25 — 7 / 10 / 8; `--price` 92 — 24 / 46 / 22; `--traffic` 9 — 1 / 3 / 5; `--tax` 33 — 14 / 5 / 14; `--rental` 32 — 4 / 9 / 19; `--work` 24 — 3 / 7 / 14; `--risks` excl. climate 38 — 11 / 19 / 8; climate projections (in `--risks`) 5 — 3 / 2 / 0; `--mains` 22 — 9 / 10 / 3; Cost benchmarks 18 — 4 / 4 / 10; Active fiscal incentives 8 — 4 / 3 / 1, plus 1 bullet added; Common listing platforms 9 — 1 / 7 / 1; Caveats unique to UAE (legal / fiscal only) 9 — 2 / 4 / 3; Source URL templates 28 — 6 / 22 / 0
  - Spot checks, no row in the verification table: Verification authorities 1 — 1 / 0 / 0 (MoET row); Quirks to know 2 — 0 / 2 / 0
  - Totals: 369 facts checked — 98 changed / 161 confirmed / 110 unverifiable (2 duplicate edits dropped)
  - Main changes: Dubai `--price` now leads with DLD 2025 averages (units AED 20,666/sq m, villas AED 16,791/sq m) and shows 2026 turning negative (REIDIN −1.27% YoY in Sep 2026, ValuStrat −4.5% in Q3 2026 — secondary); premium-zone table rebuilt from REIDIN Q1 2026 transacted and Bayut Index Sep 2026 asking prices; ADREC H1 2026 added; Retirement Visa income floor AED 180,000 → 240,000 (ICP, GDRFA Dubai; u.ae conflict shown); AML basis Federal Decree-Law 20/2018 → Decree by Law 10/2025, with the AED 55,000 REAR trigger; Abu Dhabi tenant fee 3% → 5%; DLD title deed AED 580 → 250 and knowledge + innovation AED 20 + 10 → 10 + 10; CBUAE LTV caps and the DLD First-Time Home Buyer Programme added; QFZP instrument corrected to Cabinet Decision 100/2023; ADDC / AADC → TAQA Distribution; April 2024 rainfall 254 mm in under 24 hours, WWA's 10–40% re-labelled as an intensity figure and the Met Office study re-cited to *Weather and Climate Extremes*; Tasreef Phase 3 (25 Oct 2026) added; cladding retrofit not mandatory in Dubai, Sharjah re-cladding noted; IPCC AR6 2050 sea-level medians 0.18–0.23 m replace ~30 cm; DEWA slabs, fuel surcharge and move-in / move-out fees added; Monster Gulf → foundit Gulf; MOEC → MOET; heuristics without a primary source labelled est.
