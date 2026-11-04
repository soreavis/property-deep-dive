# Latvia (LV) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: EUR (eurozone since 1 Jan 2014 — joined a year before LT)
**Lang**: Latvian; English available at top 4 banks + Lursoft commercial gateway

---

## Country profile

Latvia is the middle Baltic state (1.845M pop at the start of 2026; 2026 data, source CSP). **Cadastre and Land Book are SEPARATE registers** (unlike Lithuania's unified Registrų centras) — VZD = physical/fiscal description; Zemesgrāmata = legal title. Both must be checked. Riga apartment €/m² is structurally lower than Vilnius — slower post-2008 recovery + supply mix dominated by Soviet "khrushchyovkas". Riga standard-type (Soviet-series) apartments averaged €978/m² (asking-vs-transaction basis not stated) in Sep 2026, still ~40% below the 1 Sep 2007 peak of €1,620/m² (2026 data, source Arco Real Estate). No like-for-like Vilnius figure verified — compare the same segment at Ober-Haus / Registrų centras. Critical Latvia-specific gotcha: **compulsory land lease (dalītais īpašums)** — many Soviet-era blocks in Riga have apartments owned separately from underlying land (often pre-1940 owner via restitution). EU + eurozone + Schengen. Major 2025 reform (in force 1 Jan 2025, rates unchanged for 2026): PIT to 25.5%/33% + capital-income to 25.5% (was 20%) (2026 data, source VID).

---

## Section: `--price`

**Primary index**: **CSP (Central Statistical Bureau)** — Eurostat-aligned HPI quarterly
- https://www.csp.gov.lv/ + EN https://stat.gov.lv/en
- **Q2 2026 LV HPI** (provisional): +3.9% QoQ, +11.4% YoY; new dwellings +1.7% YoY, existing +13.3% YoY; 9.1% above the 2025 average (2026 data, source CSP release 14 Sep 2026). Q3 2026 due 14 Dec 2026
  - https://stat.gov.lv/lv/statistikas-temas/valsts-ekonomika/paterina-cenas/preses-relizes/28655-majoklu-cenu-parmainas-2026

**Latvijas Banka**: https://www.bank.lv/ — Financial Stability Report (2026 edition 22 Jul 2026): https://www.macroeconomics.lv/financial-stability-report/financial-stability-report-2026
- **Under-declared prices**: in non-mortgaged apartment deals the gap between last listed price and declared transaction value is ~11 percentage points larger than in comparable mortgaged deals, and ~4 pp more when the seller held the flat ≤60 months (2021–2025 data, source Latvijas Banka Discussion Paper 1/2026). Treat cash-deal declared prices as a floor, not a comparable. https://www.macroeconomics.lv/discussion-papers/estimating-under-reported-real-estate-transaction-value-evidence-latvia

**BIS / FRED**: https://fred.stlouisfed.org/series/QLVN628BIS — Q1 2026 = 280.99 (2010 = 100, all dwellings, whole country; 2026 data, source BIS via FRED, updated 25 Jun 2026)

**Verified figures (Arco Real Estate — agency data, secondary tier)**:
- **Riga standard-type apartments** (Soviet-series, lower segment): €978/m² average price in Sep 2026 (asking-vs-transaction basis not stated), +0.6% m/m and >10% since the start of 2026; cheapest Bolderāja €728/m², dearest Teika €1,163/m² (2026 data). Nearby: Ogre €977, Salaspils €913, Kauguri (Jūrmala) €887, Jelgava €807/m²
- **Riga centre**: 2025 average transaction price €1,874/m² (+4% YoY); quiet centre €2,505, Old Riga €1,942; end-2025 average prices for flats in very good condition ~€3,500 (close centre) / ~€3,700 (quiet centre) / ~€3,000 (Old Riga); top central deal almost €6,000/m² (2025 data)
- **Riga new projects**: centre end-2025 average transaction €2,466/m² (−9% YoY; ~70% of deals €1,800–3,400); housing estates 2025 average €2,202/m² (+6% YoY) (2025 data)
- **Jūrmala / coastal premium**: significant uplift, wooden-architecture protected (qualitative, not from the Arco data — verify locally)
- Sources: https://www.arcoreal.lv/lv/zinas/2026/tirgus-parskats-serijveida-dzivokli-riga-un-apkartne-2026-gada-septembri-2028/ · https://www.arcoreal.lv/lv/zinas/2026/tirgus-parskats-dzivokli-rigas-centra-2025-gada-1983/ · https://www.arcoreal.lv/lv/zinas/2026/tirgus-parskats-dzivokli-jaunajos-projektos-riga-2025-gada-1978/

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| SS.lv / SS.com | https://www.ss.lv/ + https://www.ss.com/ | #1, all classifieds, RE dominant |
| City24 | https://www.city24.lv/ | Pan-Baltic agency listings |
| Varianti | https://www.varianti.lv/ | Real-estate classifieds portal (agency + private listings, new-projects directory) |
| Realto | https://www.realto.lv/ | Owner-operator site — leases/sells its own commercial property (13 business quarters); not a residential aggregator |

**Verdict bands** (est.: this skill's screening heuristic, not a published statistic or legal threshold; calibrate each deal on like-for-like local comparables):
- 🟢 within ±10% of CSP/local-segment €/m²
- 🟡 ±20%, possibly compulsory-land-lease (dalītais īpašums) discount
- 🟠 ±30%, investigate land-ownership / encumbrance
- 🔴 >±30% — likely a Latvia-specific structural issue

---

## Section: `--traffic`

**Sources**:
- **Latvijas Valsts ceļi (LVC)** — state road manager: https://lvceli.lv/ — public map of traffic intensity (satiksmes intensitāte), current traffic events, accidents, short-term roadworks and weight / size restrictions on state roads: https://map.transportdata.gov.lv/public
- **Riga real-time**: Waze (crowd-sourced, commercial). Mobills.lv ❌ DEPRECATED — dead on 2026-10-23 (domain does not resolve); verify with LVC. The similarly named Mobilly (https://www.mobilly.lv/) is a parking and ticket payment app, not a traffic feed
- **OSM Overpass** for road class + maxspeed (universal)

---

## Section: `--tax`

### Stamp duty (transfer tax) — Zemesgrāmata registration

- **Individual buyer**: **1.5%** of the property value — the highest of the contract price, the cadastral value (the fiscal cadastral value since 2025) and the other valuations listed in pt 8 — capped at **€50,000** (Cabinet Regulation No. 1250 pt 5.1, version in force 13 Dec 2025; 2026 data, source likumi.lv)
- **Legal entity buyer**: **2%**, same €50,000 cap (pt 5.2)
- **Gift**: 3%, same cap (pt 5.3); **close relatives** (children, spouses, parents, siblings, grandchildren, grandparents and others listed in pt 6): 0.5%, same cap, for a purchase or gift
- **Buyers supported by state housing aid** (mortgage with a lender's confirmation of state support for a person raising at least one child or expecting one): 0.5% of value up to €100,000, then €500 + 1.5% of the excess (pts 7.1–7.2) (2026 data, source likumi.lv)
- Plus Land Book office fees (kancelejas nodeva): €15 per person for registering the new ownership right (90% of that when filed electronically) + €8 for a Land Book certificate (Zemesgrāmatu likums Art. 107, version in force 1 Jan 2022; 2026 data, source likumi.lv)
- **Notary fee** for a notarial purchase deed: **0.5% of the deal sum, minimum €140**, plus VAT; the tariff includes filing the right at the Land Book (Cabinet Regulation No. 737 pts 5–6, as amended by Regulation No. 200 of 14 Apr 2026; 2026 data, source likumi.lv). https://likumi.lv/ta/id/259604-noteikumi-par-zverinatu-notaru-atlidzibas-taksem-un-to-noteiksanas-kartibu

**Total acquisition cost, individual buyer**: ≈2.1% with a notarial deed (computed for a €100,000 deal: €1,500 + €605 + €23 = €2,128, where duty is 1.5%, the notary €500 × 1.21 = €605 with 21% VAT and office fees €15 + €8 = €23; legal, agent and mortgage costs excluded)

Sources:
- State fee: https://likumi.lv/ta/id/200087-noteikumi-par-valsts-nodevu-par-ipasuma-tiesibu-un-kilas-tiesibu-nostiprinasanu-zemesgramata
- Office fees: https://likumi.lv/ta/id/60460-zemesgramatu-likums
- Secondary overview: https://taxsummaries.pwc.com/latvia/corporate/other-taxes

### Annual immovable property tax (NĪN — Nekustamā īpašuma nodoklis)

- **Default rate**: **1.5%** of cadastral value for land, buildings and engineering structures where the municipality has not set its own rate; municipal rate rules are published by 1 November of the preceding year (law "Par nekustamā īpašuma nodokli" Art. 3; 2026 data, source likumi.lv + VID)
- **Residential buildings**: progressive **0.2% / 0.4% / 0.6%** of cadastral value
  - Statutory default brackets: 0.2% up to €56,915, 0.4% on the part €56,915–€106,715, 0.6% above €106,715 (law Art. 3(1)(2); 2026 data, source likumi.lv)
  - Municipalities may set rates of 0.2%–3.0% within the statutory band, and a rate above 1.5% only where the property is not maintained as the rules require (law Art. 3(1); 2026 data, source likumi.lv)
- Local councils set actual rates in binding regulations. **Riga**: 0.2% up to €57,000, 0.4% on the part €57,000–€107,000, 0.6% above €107,000 for an apartment or single-dwelling house not used for business — only if on 1 January (00:00) of the tax year at least one person who is a Latvian citizen or non-citizen, an EU/EEA/Swiss citizen or a Latvian permanent-residence-permit holder has declared residence there; otherwise **1.5%** for the whole year (a declaration by a non-EU temporary-residence-permit holder alone does not qualify). Companies get the reduced rate only for a dwelling let for living with the lease registered in the Land Book. **3%** for degrading, collapsed or unsafe buildings, unmaintained land or property, and construction past its legal time limit (Riga Council binding regulations No. 148, version in force 1 Jun 2023, source likumi.lv; reduced-rate rule confirmed for 2026 by the Riga Finance Department, 16 Dec 2025)

**2025 cadastral value reform**: since 1 Jan 2025 two cadastral values exist — **fiscal** (used for taxes incl. NĪN, state fees and other payments to the state or municipal budget, except the fee for statutory land use; calculated on the 2024 cadastral-value base, which reflects 2012 market data) and **universal** (2022 market level from transactions between 2012 and mid-2022, capped at 80% of the average price level on 1 Jul 2022; used for ground rent under forced divided ownership and other non-fiscal purposes such as accounting). Tax still uses fiscal value, so NĪN remains low relative to actual prices (Cadastre Law transitional pts 43.1–43.3, 2026 data, source likumi.lv; 2012 market basis per Ministry of Justice, 22 Nov 2024; fiscal value still the NĪN base in 2026 per kadastra.lv, Jul 2026 — secondary).

Sources:
- https://www.vid.gov.lv/en/immovable-property-tax
- https://www.fm.gov.lv/en/tax-rates-2
- Law: https://likumi.lv/ta/id/43913-par-nekustama-ipasuma-nodokli
- Riga: https://likumi.lv/ta/id/275681-par-nekustama-ipasuma-nodokli-riga
- Cadastral values: https://www.tm.gov.lv/lv/jaunums/aktualizejot-kadastralas-vertibas-nekustama-ipasuma-nodoklis-nepieaugs

### Capital gains on property sale (LV individuals)

- **Standard rate 25.5%** from 1 Jan 2025 (2026 data, source VID PIT-rates page, updated 31 Dec 2025) — 20% applies in 2025-2027 only to gains on capital-asset deals initiated by 31 Dec 2024 but not completed by then, with a capital-gains declaration filed
- **From 2025 onwards**: **25.5%** capital-gains rate (2025 PIT reform; unchanged on the VID rates page updated 31 Dec 2025)
- **Exemption**: held **>60 months** (counted from Land Book registration) AND the seller's declared residence (not an additional address) for **≥12 consecutive months** within the last 60 months before the sale contract → fully exempt (BOTH conditions, not OR). Other exempt routes: held >60 months and the seller's only Land-Book-registered property for the last 60 months; or the only registered property, with the proceeds invested in a functionally similar property within 12 months before or after the sale (2026 data, source VID capital-gains page)
- **Non-resident seller**: a buyer with registered economic activity (company, sole trader, farm, association) withholds 3% PIT from the price; when selling to a private individual, the non-resident declares the gain by the 15th of the month after receiving the income and pays the tax (2026 data, source VID FAQ)

Sources: https://www.vid.gov.lv/lv/ienakuma-nodoklis-no-kapitala-pieauguma + https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes + https://taxsummaries.pwc.com/latvia/individual/income-determination (secondary)

### Rental income (individual)

- **10% PIT on gross rental income**, with no expense deduction except the NĪN paid on the let property, no annual non-taxable minimum or reliefs, and no social contributions — if the landlord notifies VID within 5 working days of signing the lease that they use the right not to register the economic activity (2026 data, source VID) — cleanest route for landlords
- Without that notification: full progressive **PIT (Iedzīvotāju ienākuma nodoklis, IIN)** 25.5% up to €105,300 / 33% above + additional **3% surcharge above €200,000** total annual income (2025 PIT reform, in force 1 Jan 2025; 2026 data, source VID)

### VAT new-build

- **Standard 21%** (2026 data, source VID VAT-rates page, updated 30 Sep 2026)
- **Unused property (nelietots nekustamais īpašums, VAT Law Art. 1(12))**: a new or renovated building not used since commissioning, or used and first sold within 1 year of commissioning, or not yet commissioned — 21% VAT, charged together with the land under it; building land (apbūves zeme) is also taxable (VID)
- Resale of "used" buildings: VAT-exempt (VAT Law Art. 52(1)(24)); the option to charge VAT exists only where a registered VAT payer sells to a registered VAT payer (Art. 144(1)) (VID)
- 12% reduced rate does NOT apply to property sales; it does apply to accommodation services in tourist accommodation, which matters for VAT-registered short-let hosts (VAT Law Art. 42(10); 2026 data, source VID VAT-rates page, updated 30 Sep 2026) sales; it does apply to accommodation services in tourist accommodation, which matters for VAT-registered short-let hosts (VAT Law Art. 42(10); 2026 data, source VID VAT-rates page, updated 30 Sep 2026)

---

## Section: `--rental`

### Long-term rental
- 10% PIT on rental income for individuals who notify VID instead of registering economic activity (notify within 5 working days of signing the lease): no expense deduction except the immovable property tax (NĪN) paid; no social contributions, no personal allowance (2026 data, source VID). Registered economic activity is taxed at the progressive 25.5%/33% rates instead; VID also lists a micro-enterprise tax route (25% of turnover)
  - https://www.vid.gov.lv/lv/pirmie-soli-nekustama-ipasuma-iziretajam
- **DAC7 platform reporting**: digital platform operators report their active sellers, including real-estate rental hosts, and the platform transactions to VID once a year, by 31 January for the previous calendar year; first deadline 31 Jan 2024. It adds reporting only, no new tax (law "Par nodokļiem un nodevām" Art. 15(11) + Cabinet Regulation No. 97 of 7 Mar 2023; source VID)
  - https://www.vid.gov.lv/lv/starptautiskie-ligumi-un-administrativa-sadarbiba
- **Rents** (2025 data, source Arco Real Estate rental review — agency tier, asking-vs-agreed basis not stated): rents +5–10% on average in 2025; average apartment rent a record €938/month excl. utilities; the most sought budget option was a 1–2-room flat at €400–600/month excl. utilities; new-project 2-room rents €14–20/m² (Āgenskalns) down to €6–11/m² (Pļavnieki). https://www.arcoreal.lv/lv/zinas/2026/tirgus-parskats-dzivojamo-telpu-ires-tirgus-2025-gada-1990/

### STR / Airbnb

**2026 state**: **No national STR registration-number scheme found.** The Tourism Law amendments (adopted 11 Jun 2026, Latvijas Vēstnesis 119, in force **10 Jul 2026**) contain no STR register and do not refer to Regulation (EU) 2024/1028. They redefine `tūristu mītne` as any publicly bookable group of dwelling rooms, part of a building or building where a person provides overnight tourist accommodation, so STR units now count as tourist accommodation. Hosts must make foreign guests personally fill in and sign a guest declaration form (Art. 11(7)); LV portāls reports the data can also be submitted electronically (2026 data, source likumi.lv id 369280). Riga has no city-wide ban, no licensing limit, no zoning prohibition (Apr 2026 research, not re-checked against a Riga City Council source). Operators must register economic activity with VID and pay applicable PIT (Apr 2026 research; whether the 10% notified-rental route covers short-term tourist lets is not confirmed — verify with VID).
- https://likumi.lv/ta/id/369280-grozijumi-turisma-likuma

**EU Regulation 2024/1028**: applies since **20 May 2026** on an opt-in/opt-out basis. Member States are not obliged to introduce STR registration, but any registration scheme they run must follow the Regulation, and a Member State with a registration procedure must set up a single digital entry point for platform data (Regulation text, EUR-Lex CELEX 32024R1028; EU Construction Platform, DG GROW, 8 Jun 2026). The Ministry of Economics told the Cabinet on 12 Sep 2023 that Latvia should set up an STR register; no register, implementing act or Latvian single digital entry point found as of Oct 2026 (LOW — verify at em.gov.lv / likumi.lv). Trigger event: 2021 fire at Merķeļa iela 8, Riga, in an arbitrarily set-up hostel.
- https://www.em.gov.lv/en/article/latvia-along-other-eu-countries-there-plan-establish-short-term-rental-regulations-reduce-shadow-economy
- https://eur-lex.europa.eu/legal-content/EN/ALL?uri=CELEX%3A32024R1028 · https://transition-pathways.europa.eu/construction/news-publications/short-term-rentals-eu-transparency-rules-now-force

**Tourist tax** (Riga): **€0.89/night per guest + VAT (≈€1 per riga.lv)**, capped at €8.90 per continuous stay; guests under 18 exempt; levied since **1 Jan 2023** (Riga regulation RD-22-173-sn, version in force 1 Nov 2023 – 31 Dec 2026). From **1 Jan 2027**: **€1.78/night + VAT (≈€2)**, capped at €17.80 per continuous stay (amending regulation RD-26-54-sn, adopted by Riga City Council 8 Jul 2026, Latvijas Vēstnesis 139 of 23 Jul 2026). Vilnius, Kaunas and Palanga already charge €2/night (per riga.lv, 19 May 2026). (2026 data, source likumi.lv id 337264 / 369811)
- https://likumi.lv/ta/id/337264-par-pasvaldibas-nodevu-par-atputnieku-un-turistu-uznemsanu-riga · https://likumi.lv/ta/id/369811

---

## Section: `--work=<profession>`

Riga financial-services hub (post-2018 ABLV scandal still recovering — ECB declared ABLV failing or likely to fail on 23 Feb 2018); Daugavpils/Rēzekne (Latgale) lower demand; Liepāja/Ventspils ports + manufacturing. Remote/hybrid common.

**Wages**: average gross full-time monthly wage €1,886 in Q2 2026 (+4.3% YoY; net €1,401). Highest in the Rīga region (€2,068), lowest in Latgale (€1,365), a 34.0% gap (2026 data, source CSP release 2 Sep 2026). https://stat.gov.lv/lv/statistikas-temas/darbs/alga/preses-relizes/28686-darba-samaksas-parmainas-2026-gada-2-ceturksni

**Job portals**: CV.lv (https://www.cv.lv/) · State Employment Agency (NVA) vacancy portal (https://cvvp.nva.gov.lv/)

---

## Section: `--risks`

### Flood
- **LVĢMC (Latvian Environment, Geology and Meteorology Centre)**: https://videscentrs.lvgmc.lv/ (updated 2026-10-23)
- Flood Risk Information System (PRIS): https://pris.lvgmc.lv/ (updated 2026-10-23) — flood maps for the national-significance flood-risk territories identified in LVĢMC's Preliminary Flood Risk Assessment 2025–2030: https://videscentrs.lvgmc.lv/files/Udens/SPRN_2025.pdf
- Three Riga flood drivers (LVĢMC names coastal storm surges plus snowmelt and rain floods in rivers and lakes as Latvia's flood causes — SPRN 2025):
  1. Storm-surge in Gulf of Riga (westerly-sector storms, whose winter dominance is rising — SPRN 2025)
  2. Daugava spring snowmelt discharge maxima
  3. Urban pluvial (densely-populated low-lying districts)
- **Coast — highest storm-surge levels 2019–2023** (m LAS): Mērsrags 1.82 (8 Oct 2023), Skulte 1.62, Salacgrīva 1.61, Liepāja 1.47, Daugavgrīva (Riga) 1.47, Ventspils 1.45 (25 Feb 2022, about 60 ha of the city flooded), Lielupes grīva (Jūrmala) 1.44, Kolka 1.18; on the Daugava in Riga, Andrejosta 1.66 (17 Jan 2022) (2019–2023 data, source LVĢMC SPRN 2025–2030). Records: Daugavgrīva **2.39 m LAS** in 1969 (1-in-333-year level; series 1875–1916 and 1923–2020); Andrejosta 2.29 m LAS in 2007 (source LVĢMC Daugava RBD management plan 2022–2027). The 2100 flood-risk-map scenario runs to 2.40 m LAS at Daugavgrīva and, under RCP4.5, 2.25 m LAS at the Lielupe mouth / Babīte lake (source LVĢMC SPRN 2025, citing the 2nd-cycle flood risk management plans). Station levels, not plot levels

### Seismic
- Low: Baltic Sea region seismicity is low, maximum magnitudes well below 6 (source Gregersen et al. 2007, Phys. Earth Planet. Inter., doi 10.1016/j.pepi.2007.06.005 — peer-reviewed). The 21 Sep 2004 Kaliningrad earthquakes (largest M5.2) were felt up to 800 km away; a Latvian study reports a maximum intensity of 5–5.5 EMS-98 in southern Latvia (Saldus district), with cracks in walls (academic paper "Kaliningrad earthquakes of 2004 and their manifestation in Latvia", abstract only)

### Forest fire
- Lower than LT (more deciduous + bog mix); inland sandy pinelands of Latgale + parts of Vidzeme have moderate exposure
- **National layer**: VMD (State Forest Service) forest fire-danger class map — forest stands and clearings classed per Cabinet Reg. No. 238 of 19 Apr 2016 (INSPIRE, continuously updated; published 24 Feb 2025): https://data.gov.lv/dati/dataset/mea-ugunsbstambas-klau-karte-inspire — stand-level, not a parcel-level score. LVĢMC can compute the 5-class meteorological fire-danger index (source VUGD forest and peat fire manual)

### Mandatory diagnostics

- **Energy Performance Certificate (Ēkas energosertifikāts)** — required to commission or sell a building being designed, reconstructed or renovated, and to sell, rent or lease a building in use. In a building in use, an apartment (building part) needs its own EPC to be sold, rented or leased only if it is >50 m² **and** has its own energy / heat metering, and a valid EPC or temporary EPC for the whole building also lets a unit be sold, rented or leased without its own; in a building being designed, reconstructed or renovated, a unit with its own energy / heat metering needs one to be sold, whatever its size (Ēku energoefektivitātes likums Art. 7(1)–(2¹); 2026 data, source likumi.lv)
  - Residential buildings must be certified anyway unless every unit has its own heating: multi-apartment by 31 Dec 2040, single-family by 31 Dec 2050 (Art. 7(1)(9), Transitional Provision 11)
  - Two types: **Temporary** (pagaidu — planned performance of a building being designed, reconstructed or renovated → 3-year validity); **Permanent** (building in use → 10-year validity) (Art. 8(7))
  - Public registry: https://bis.gov.lv/bisp/lv/epc_documents
  - Rules: Cabinet Reg. No. 222 of 8 Apr 2021 (https://likumi.lv/ta/id/322436), amended by Reg. No. 481 (in force 15 Aug 2025 — "assumed system" assessment allowed when measured consumption data are missing, for buildings designed before 1 Jan 1992 and not thermally upgraded) and Reg. No. 349 (in force 19 Jun 2026 — measured-data and calculation-interval rules) (2026 data, source likumi.lv)
- **Radon**: reference level **300 Bq/m³** annual average in a building — above it the owner informs the tenant and the Radiation Safety Centre (RDC, State Environmental Service) when an accredited laboratory measured it, and RDC decides with the owner or tenant on protective measures; above **600 Bq/m³** annual average (or 1,000 Bq/m³ during measurement) the owner or tenant must act at once; new buildings must not exceed 300 Bq/m³; workplaces 300 Bq/m³ (Cabinet Reg. No. 149 of 9 Apr 2002, points 125, 126, 128 and 135, as amended by Reg. No. 292 in force 22 May 2025; 2026 data, source likumi.lv). The 200 / 400 Bq/m³ levels still quoted by Veselības inspekcija and the European Radon Association ERD2024 country return predate that amendment. RDC 2016 survey of 447 households: mean **74 Bq/m³** (European average 98); 30 households above 200 Bq/m³ (≈6.7%, computed 30 ÷ 447) (2016 data, source Veselības inspekcija — rates/figures may have changed since). A national survey mean is not a reading for any one dwelling. **No mandatory pre-sale radon test**
- **Asbestos**: no mandatory pre-sale survey. Soviet-era blocks common; assume risk in 1960s-80s buildings

---

## Section: `--mains`

### Cadastre + Land Book — SEPARATE INSTITUTIONS

- **Cadastre (VZD — Valsts zemes dienests)**: https://www.vzd.gov.lv/ + EN https://www.vzd.gov.lv/en
  - Public cadastre interface: https://www.kadastrs.lv/
- **Land Book (Zemesgrāmata)** — separate institution under Ministry of Justice
  - https://www.zemesgramata.lv/ + EN https://www.zemesgramata.lv/?lang=en
  - **Encumbrances live in the Land Book** — must check both
- **Spatial portal**: https://geolatvija.lv/
- **Lursoft commercial gateway**: https://www.lursoft.lv/en/land-register — paid extracts in EN

### District heating

In Riga 76% of apartment buildings are connected to district heating, according to a reply in the Riga Energy Agency's REK2030 consultation report (consultation 22 Nov 2021–20 Jan 2022). The reply gives no data year or base, so reading it as Riga's whole apartment stock is an inference — rates/figures may have changed since. https://rea.riga.lv/wp-content/uploads/2024/03/bdf163da5b991590d5a806b580470c3204d0061b.pdf SPRK-regulated operators also serve Daugavpils (Daugavpils siltumtīkli), Liepāja (Liepājas enerģija) and Jelgava (Gren Jelgava); no share verified for those cities (2026 data, source SPRK tariff decisions for May and September 2026). https://www.sprk.gov.lv/events/maija-siltumenergijas-tarifu-izmainas-apstiprinatas-deviniem-regulejamiem-komersantiem https://www.sprk.gov.lv/lv/jaunums/septembri-siltumenergijas-tarifu-izmainas-apstiprinatas-divpadsmit-regulejamiem-komersantiem **Rīgas siltums (RS)**: https://rs.lv/ (updated 2026-10-23)

**EIB programme**: 4-year €135M rehabilitation of Riga DH network (€47M EIB finance; signed 15 Apr 2026) (2026 data, source EIB). https://www.eib.org/en/projects/all/20240344

**Riga DH split**: two networks, not yet connected. Left bank + Vecmīlgrāvis = self-produced by RS; **Right bank (2/3 of Riga heat consumption) = bought from other producers, mainly Latvenergo**, partly through an RS-run heat purchase market — explains tariff complexity (2025 data, source LETA via apollo.lv — secondary)

**Tariff** (excl. VAT, regulator SPRK): from 1 Oct 2025 **€83.01/MWh** after SPRK review (RS had requested €88.10; LSM calculated +11.9% against the €74.17/MWh residents were then paying) (2025 data, source LSM 28 Aug 2025). Tariff in force in Oct 2026: €80.96/MWh. RS has filed a draft with SPRK for **€96.33/MWh from 1 Dec 2026** (+19% vs the tariff in force, +16% vs the previous heating season), pending SPRK approval (2026 data, source LSM / LETA 30 Oct 2026). https://eng.lsm.lv/article/economy/economy/28.08.2025-riga-heating-tariff-rise-will-be-less-than-initially-suggested.a612119/ + https://eng.lsm.lv/article/economy/economy/30.10.2026-rigas-central-heating-tariff-to-rise-significantly-in-december.a669807

**Apr 2026 audit**: the State Audit Office (Valsts kontrole) found Riga heat supply could be organised "better and cheaper". In 1 Jul 2024–30 Jun 2025 Latvenergo's CHPs released 532,052 MWh of cogeneration heat into the atmosphere; by the auditors' calculation, using more of it would have saved RS €7.8M, or 2.6% (€2.1/MWh) off the final tariff (2026 data, source LSM 21 Apr 2026 report of the audit)

### Electricity / Water
- **Latvenergo** (SOE generation + retail; the group trades under the **Elektrum** brand across the Baltics from 29 Oct 2026, and latvenergo.lv redirects to elektrumgroup.com — 2026 data, source Elektrum group news, company source), **Sadales tīkls** (DSO, Latvenergo subsidiary — source Latvenergo Group audited 2025 results, 29 Apr 2026)
- **Rīgas ūdens** (Riga); separate municipal utilities elsewhere. Rural well + septic common
- **Same BRELL exit**: Latvia, with LT and EE, disconnected from the Russian-controlled IPS/UPS (BRELL) system on 8 Feb 2025 and synchronised with the Continental European grid on 9 Feb 2025, 14:05 EET (source ENTSO-E 9 Feb 2025; AST)

---

## Section: `--crime`

See `shared/crime-sources.md`. Latvia uses:
- **Iekšlietu ministrija (MoI) — State Police**: https://www.vp.gov.lv/
- **CSP crime tables**: NOR023 — recorded crimes and crime rates per 10,000 population by state city and municipality, 2021–2025 (published 2 Jun 2026): https://data.stat.gov.lv/pxweb/en/OSP_PUB/START__POP__NO__NOR/NOR023/ — municipality-level, never a street- or parcel-level figure

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

---

## Cost benchmarks (Nov 2026)

| Item | Range / typical |
|---|---|
| Riga apt €/m² (standard segment) | €978 average, asking-vs-transaction basis not stated (Sep 2026, Arco Real Estate — agency data, secondary) |
| Riga centre €/m² (2025 transactions) | €1,874 avg; top deal almost €6,000 (Arco) |
| Stamp duty (individual) | 1.5% of the higher of price or cadastral value (cap €50k; 2026 data, source likumi.lv) |
| Notary fee | 0.5% of the deal sum, min €140, plus VAT, for a notarial deed (2026 data, source likumi.lv) |
| Total acquisition costs | ≈2.1% with a notarial deed (computed in `--tax`: €2,128 on a €100,000 deal) |
| Annual NĪN (residential) | 0.2–0.6% of fiscal cadastral value (Riga, qualifying declared resident on 1 Jan; otherwise 1.5%) |
| EPC certificate | ~€280–380 est. for an independent expert's conclusion on a certificate (BAU Fonds temporary-certificate page, undated); ~€300–1,500 est. for a multi-apartment building (2026 data, source Alteko blog, 23 Jun 2026). Provider prices, not an official tariff: the quote depends on building size, location and complexity |

---

## Active fiscal incentives

- **5-year + 12-month declared-residence CGT exemption** (>60 months from Land Book registration + ≥12 consecutive months declared residence; 2026 data, source VID)
- **10% PIT on gross rental income less NĪN** (notified non-registered economic activity; no expense deduction; 2026 data, source VID)
- **NĪN uses the fiscal cadastral value (2012 market data)** — much lower than current market (Ministry of Justice, Nov 2024)

---

## Foreign-buyer rules

- **Who can acquire land without the foreign-buyer consent**: in rural areas, citizens of Latvia, other EU and EEA states, Switzerland and OECD Capital-Movements-Code states, plus qualifying companies (law "Par zemes privatizāciju lauku apvidos" Art. 28(1)); in cities, Latvian and other EU citizens plus qualifying companies (law "Par zemes reformu Latvijas Republikas pilsētās" Art. 20). **Agricultural land** also requires (Rural law Art. 28.1, version in force 18 Jul 2024): registration as an economic operator in Latvia, a written undertaking to start farming it within 1 year (land claimed for direct payments in the current or previous year) or 3 years (not claimed), and tax debts ≤€150; the municipal commission must consent, and pre-emption rights apply (co-owner, registered tenant, then the Latvian Land Fund) (Art. 30.1–30.2). These agricultural-land conditions do not apply where the buyer's agricultural land after the deal totals ≤10 ha (individual) or ≤5 ha (legal person), to land in planned building areas, or to deals between spouses and 1st/2nd-degree relatives (Art. 30.3). Cap 2,000 ha of agricultural land per person (Art. 29) (2026 data, source likumi.lv)
- **Other foreign buyers** (non-EU citizens in cities; outside the EU/EEA/Swiss/OECD group in rural areas): can buy buildings; land only with the municipal council chairman's consent, decided within 20 days where the intended use fits the municipal plan, and the deed is registrable in the Land Book only with that consent certificate attached (Cities law Art. 22; Rural law Art. 30). Barred: land in the state border zone; agricultural and forest land (rural areas: except planned building areas, up to 5 ha of agricultural and forest land in total); the Baltic Sea / Gulf of Riga dune protection zone (in cities, unless the city plan designates the land for building) and public-water protection zones outside planned building areas; in rural areas also nature reserves and state-significance mineral deposits. Inheritance is exempt from these bars (Cities law Art. 21; Rural law Art. 29) (2026 data, source likumi.lv)
- **CRITICAL — Russian/Belarusian nationals (national-security statute in force 3 Jul 2025)**:
  - **Acquisition of Latvian real estate or a share of it is void and cannot be registered in the Land Book** for Russia, Belarus, their citizens, entities registered there, entities at least 25% held by RU/BY-registered entities or (directly or indirectly) by RU/BY nationals or with RU/BY-citizen beneficial owners, and legal arrangements set up in RU/BY or with RU/BY-citizen beneficial owners; no auction bids, pre-emption or buy-out rights (Art. 2–3)
  - **Exceptions, RU/BY citizens only** (Art. 4(1)): a final court ruling settling an ownership dispute (not a court-approved settlement); inheritance by a spouse or relatives up to the 4th degree (other heirs receive the sale proceeds via a notary-appointed curator); ending compulsory divided ownership (dalītais īpašums) by adding the land share of their apartment; a deal fulfilling Latvia's international obligations; one sole dwelling for a holder of EU long-term-resident status or a permanent residence permit issued before 3 Jul 2025
  - Deals and inheritance cases opened before 3 Jul 2025 had 3 months to be registered or became void; the Cabinet reviews the restriction at least once a year (transitional provisions)
  - Existing properties retainable but disposal scrutinized
  - Statute: Nacionālo drošību apdraudošu darījumu ierobežošanas likums (adopted 19 Jun 2025, in force 3 Jul 2025; no amendments listed, 2026 data, source likumi.lv): https://likumi.lv/ta/id/361619-nacionalo-drosibu-apdraudosu-darijumu-ierobezosanas-likums — sanctions context: https://www.mfa.gov.lv/en/sanctions
  - LV has explicit purchase prohibitions in force (harder than LT, which relies on residency/AML chokepoints)
- **Border zone + coast**: foreign buyers outside the groups above cannot acquire land in the state border zone (pierobežas josla) at all, nor in the Baltic Sea / Gulf of Riga dune protection zone (in cities the dune-zone bar does not apply where the city plan designates the land for building) (Cities law Art. 21; Rural law Art. 29; 2026 data, source likumi.lv). Affects Latgale (E border with RU/BY) and the coast. National-defence-area permit rules: verify with the municipality and the Land Book
- **Investor residence permit (Golden Visa equivalent) — real-estate route ENDED 15 Sep 2026**: the new Immigration Law (Imigrācijas likums, adopted by the Saeima 20 Aug 2026, in force 15 Sep 2026; likumi.lv id 370622) replaced the 2002 law and no longer grants temporary residence permits to real-estate purchasers (the old ≥€250,000 route) or to investors in credit institutions' subordinated liabilities (PMLP, 15 Sep 2026). A purchase from that date grants no permit. Applications filed before 15 Sep 2026 are decided under the old law (transitional pt 4); permits already issued stay valid to the end of their registration or validity period (pt 6); renewal by old-law permit holders follows transitional pts 7–10 (in some cases with payments to the "Ekonomikas attīstības programma" budget programme topped up to €5,000 in total). The annual registration obligation is abolished (PMLP). **Remaining investor routes**: company share capital €50,000 (small company) or €100,000, plus €10,000 to the state budget, permit up to 2 years (Art. 27(1)(10)); €150,000 through a state-established alternative investment fund manager plus €10,000, permit up to 5 years (Art. 27(1)(36)) — unusable until the fund is established (PMLP). Russian and Belarusian citizens cannot use either route (Art. 27(7)–(8)); the Cabinet may suspend both routes for named nationalities for up to 5 years (Art. 28) (2026 data, source PMLP + likumi.lv): https://www.pmlp.gov.lv/en/article/new-immigration-law-takes-effect-key-changes-and-regulations

---

## Country-specific quirks

- **Compulsory land lease (`dalītais īpašums`)** — Iconic LV problem: many Soviet-era apartment blocks in Riga sit on land owned by **a different party** (often pre-1940 owner via restitution). Residents own the apartment but **pay forced ground rent** to land owner. **Reform: Piespiedu dalītā īpašuma privatizētajās daudzdzīvokļu mājās izbeigšanas likums** (adopted 25 Nov 2021, in force 1 Jan 2023; https://likumi.lv/ta/id/328166-piespiedu-dalita-ipasuma-privatizetajas-daudzdzivoklu-majas-izbeigsanas-likums) — gives the building's apartment owners a unilateral right to buy out the land attached to the house at its cadastral value (Ministry of Justice). Since 2025 the ground rent under forced divided ownership is set from the universal cadastral value (2022 market data), not the lower fiscal value (Ministry of Justice, Nov 2024). **Verify on EVERY Riga deal.** No LT equivalent.
- **Restitution legacy**: 1990s land reform restored property to pre-1940 owners or heirs (citizens AND citizenship-eligible heirs from emigration — broader than LT). 30-year reform formally completed 2020; residual claims continue to surface, especially in Riga urban land
- **Riga Old Town (Vecrīga) UNESCO 1997**: strict heritage rules. Heritage Inspection (NKMP) approval for any external change
- **Latgale (E Latvia)**: border zone (RU + BY), Russian-speaking-majority; lower prices, but the **RU/BY buyer ban (in force 3 Jul 2025) + the border-zone land bar for non-qualifying foreign buyers** are most relevant here. Latgale rural land cheap but harder to liquidate
- **Jūrmala**: premium coastal market (Riga Beach). Wooden architecture protected. Heritage demolition controls; flood/storm surge exposure
- **Latvian banking — non-EU pain point**: Following 2018 ABLV scandal + ongoing AML enforcement, opening LV bank accounts as non-EU non-resident is **very difficult**; cross-border purchase often routed via EU bank

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre | VZD | https://www.vzd.gov.lv/ |
| Land Book | Zemesgrāmata | https://www.zemesgramata.lv/ |
| Tax | VID (State Revenue Service) | https://www.vid.gov.lv/en/ |
| Min of Finance | FM | https://www.fm.gov.lv/en/ |
| Min of Economics | EM | https://www.em.gov.lv/en/ |
| Flood / weather | LVĢMC | https://videscentrs.lvgmc.lv/ (updated 2026-10-23) |
| EPC public registry | BIS | https://bis.gov.lv/bisp/lv/epc_documents |
| Migration | PMLP | https://www.pmlp.gov.lv/en |
| Heating / utility tariffs | SPRK (Public Utilities Commission) | https://www.sprk.gov.lv/ |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastre lookup | https://www.kadastrs.lv/ |
| Land Book | https://www.zemesgramata.lv/?lang=en |
| HPI / RPPI | https://www.csp.gov.lv/ + https://stat.gov.lv/en |
| NĪN rules | https://www.vid.gov.lv/en/immovable-property-tax |
| EPC rules (Cabinet Reg. No. 222) | https://likumi.lv/ta/id/322436 |
| EPC law (Ēku energoefektivitātes likums) | https://likumi.lv/ta/id/253635 |
| Flood maps (PRIS) | https://pris.lvgmc.lv/ |
| MFA sanctions | https://www.mfa.gov.lv/en/sanctions |
| RU/BY real-estate acquisition ban (in force 3 Jul 2025) | https://likumi.lv/ta/id/361619 |

---

## Status

✅ Fast-changing sections re-verified as of 2026-10-23; each section's date is in the Per-section verification table.

**Confidence**: HIGH for the `--tax` statutory rules re-checked on primary sources on 2026-10-23 (stamp duty 1.5% / 2% with the €50,000 cap plus the gift, close-relative and housing-aid rates, Land Book office fees, the NĪN default rate, statutory brackets and Riga's declared-residence condition, the 2025 fiscal / universal cadastral-value split, PIT 25.5% / 33% + 3%, CGT 25.5% and the 60-month + 12-month exemption, the 10% rental route, VAT — likumi.lv, VID, Ministry of Justice); for the foreign-buyer statutes (land-acquisition consent rules, the RU/BY acquisition ban in force 3 Jul 2025, and the investor-permit real-estate route ENDED 15 Sep 2026 under the new Immigration Law — PMLP, likumi.lv id 370622); for the cadastre + Land Book separation and the forced-divided-ownership buyout law (likumi.lv); and for the `--work` wages (CSP Q2 2026), `--mains` (SPRK tariff, State Audit Office, EIB, ENTSO-E), `--crime` (CSP NOR023) and `--traffic` (LVC) sources. MEDIUM for `--price` (CSP Q2 2026 HPI, BIS/FRED and the Latvijas Banka Financial Stability Report 2026 are primary; the Riga €/m² figures are Arco Real Estate agency data; the SS.lv ranking, the City24 description and the Jūrmala premium line are unverified), `--rental` (the VID 10% route, the 2026 Tourism Law amendments, the opt-in status of Regulation (EU) 2024/1028 and the Riga tourist fee are primary-sourced; rents are agency data; Riga's no-ban / licensing / zoning line and whether the 10% route covers short lets are unverified), `--risks` (flood, seismic, fire-map, EPC and radon rules re-sourced; the LT forest-fire comparison, the pre-sale radon-test line and the asbestos line are unverified) and the lines carried from the initial population without re-verification (RU/BY disposal scrutiny, the LT comparison, defence-area permits, the restitution completion year, the UNESCO year, NKMP approval and the qualitative `--mains` lines). HIGH for the notary tariff (0.5%, minimum €140, plus VAT; likumi.lv). LOW for the EPC price row (provider prices only, no official tariff) and per-locality rental yield benchmarks. Regulatory-watch LV entries (PIT reform, RU/BY ban, investor permit) last re-checked 2026-10-21 (see shared/regulatory-watch.md).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)
- 2026-10-21: Tax tracker entry re-checked (December regwatch wave, run early; see shared/regulatory-watch.md).
- 2026-10-23: Refresh wave (market, tax-legal, risk-infra) plus audit findings. Playbook-level date not re-stamped: `--price`, `--tax`, `--rental` and `--risks` keep unverified items. Counts per section (changed / confirmed / unverifiable):
  - Re-verified: Country profile 2 / 2 / 1; `--traffic` 2 / 1 / 0; `--work` 2 / 1 / 1; `--mains` 6 / 7 / 4; `--crime` 1 / 1 / 0; `--amenities` 0 / 1 / 0; `--climate` 0 / 1 / 0; Active fiscal incentives 2 / 1 / 0; Verification authorities 1 / 7 / 0 (SPRK row added); Source URL templates 2 / 5 / 0 (EPC-law and RU/BY-statute rows added)
  - Refreshed, not re-verified: `--price` 12 / 3 / 2 (Listings table 2 / 1 / 2); `--tax` 11 / 7 / 2; `--rental` 9 / 3 / 2; `--risks` 11 / 2 / 3; Cost benchmarks: price rows 2 / 0 / 0, tax rows 2 / 1 / 4; Foreign-buyer rules 6 / 0 / 3; Country-specific quirks 2 / 0 / 3. The playbook has no Reddit / forum section
  - Main changes: CSP Q2 2026 HPI, BIS/FRED Q1 2026 and the Latvijas Banka Financial Stability Report 2026 replace the Q4 2025 Trading Economics figure and the "Real Estate Market Surveillance Reports" (no publication of that name found); Riga standard segment ~€865 → €978/m² (Arco, Sep 2026) and Arco 2025 centre and new-project figures added; Realto and Varianti rows corrected; unsourced Vilnius comparison removed; stamp-duty base restated and the gift, close-relative and housing-aid rates added (Cabinet Reg. No. 1250); Land Book certificate fee €7 → €8; NĪN default rate and Riga's declared-residence condition (otherwise 1.5%); CGT exemption counted from Land Book registration, with ≥12 consecutive months of declared residence; the 10% rental route allows no expense deduction except NĪN (was "deduction-allowed"); VAT unused-property rule; Tourism Law amendments in force 10 Jul 2026; Regulation (EU) 2024/1028 described as opt-in and applying since 20 May 2026 (was "mandatory by May 2026"); Riga tourist fee €0.89 + VAT capped at €8.90 (was €1 / €10), €1.78 + VAT from 1 Jan 2027; RU/BY acquisition ban restated from the 2025 national-security statute (was "post-2022 sanctions"); investor-permit real-estate route ENDED 15 Sep 2026 under the new Immigration Law, unsourced approval counts dropped; forced-divided-ownership law cited (likumi.lv 328166); flood figures from LVĢMC SPRN 2025 and PRIS; seismic "negligible" → low, with a peer-reviewed source; VMD fire-danger map; EPC apartment rule; radon reference level 200 → 300 Bq/m³; Rīgas siltums tariff and the State Audit Office 2026 finding; Elektrum brand; BRELL synchronisation 9 Feb 2025 (was 8 Feb); Mobills.lv ❌ DEPRECATED; CSP crime table NOR023
  - Status: Confidence recomputed, with the investor-permit limb (audit); per-section verification table added; Extension TODOs STR line reworded to the opt-in status (audit, re-checked 2026-11-03)
- **2026-11-04** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (Nov 2026). Playbook-level date now 2026-10-23.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | 2 changed, 2 confirmed, 1 unverifiable; CSP 2026 population, Arco Sep 2026 Riga standard segment, VID 2026 rates; unsourced Vilnius comparison removed |
| `--traffic` | 2026-10-23 | 2026-10-23 refresh wave | 2 changed, 1 confirmed; LVC traffic map added; Mobills.lv ❌ DEPRECATED; Waze and OSM not re-checked |
| `--work=<profession>` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--mains` | 2026-10-23 | 2026-11-04 maintenance run | The district-heating line now rests on a Riga Energy Agency figure (76% of apartment buildings, 2022) and 2026 SPRK tariff decisions naming the regulated operators in Daugavpils, Liepāja and Jelgava. No comparable share was verified for those three cities. |
| `--crime` | 2026-10-23 | 2026-10-23 refresh wave | 1 changed, 1 confirmed; CSP table NOR023 (municipality level) |
| `--amenities` | 2026-10-23 | 2026-10-23 refresh wave | Pointer to `shared/amenities-osm.md` confirmed |
| `--climate` | 2026-10-23 | 2026-10-23 refresh wave | Pointer to `shared/climate-projections.md` confirmed |
| Active fiscal incentives | 2026-10-23 | 2026-10-23 refresh wave | 2 changed, 1 confirmed; CGT exemption, 10% rental route and fiscal cadastral value per VID and the Ministry of Justice |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | 1 changed, 7 confirmed; LVĢMC URL replaced; SPRK row added |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | 2 changed, 5 confirmed; flood maps moved to PRIS; EPC-law and RU/BY-statute rows added |
| `--price` | 2026-10-23 | 2026-11-04 maintenance run | Arco Real Estate's Sep 2026 standard-type apartment prices were re-confirmed on its market review. The verdict bands are labelled as this skill's screening heuristic, not a published statistic. |
| `--tax` | 2026-10-23 | 2026-11-04 maintenance run | The notary tariff is corrected to 0.5% of the deal sum, minimum €140, plus VAT (Cabinet Regulation No. 737, likumi.lv), which puts a notarial-deed purchase at ≈2.1% in total. PIT, capital-gains and reduced-VAT rules were re-confirmed on VID pages and the NĪN municipal rate band on likumi.lv. |
| `--rental` | 2026-10-23 | 2026-11-04 maintenance run | The 2025 rent figures were re-confirmed on Arco Real Estate's rental market review (agency tier), including the €938/month average and the new-project €/m² ranges. |
| `--risks` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Foreign-buyer rules | 2026-04-26 | initial population | Refreshed 2026-10-23 (6 changed, 3 unverifiable); investor-permit real-estate route ENDED 15 Sep 2026 per PMLP + likumi.lv; not re-verified: RU/BY disposal scrutiny, LT comparison, defence-area permits |
| Country-specific quirks | 2026-04-26 | initial population | Refreshed 2026-10-23 (2 changed, 3 unverifiable), not re-verified: restitution completion year, UNESCO year, NKMP approval rule |
| Cost benchmarks (Nov 2026) | 2026-10-23 | 2026-11-04 maintenance run | Notary and total-cost rows now follow the likumi.lv tariffs and a computed €100,000 example. The EPC row shows provider prices (BAU Fonds, Alteko) because no official tariff was found, and the Riga €978/m² row states that Arco Real Estate does not give its price basis. |

---

## Extension TODOs

- National STR register — Regulation (EU) 2024/1028 has applied since 20 May 2026 in opt-in/opt-out mode, so Member States are not obliged to set one up (European Commission, 20 May 2026); the Tourism Law amendments in force 10 Jul 2026 add none (likumi.lv id 369280). Track any Latvian register, implementing act or single digital entry point (see `--rental`)
- Compulsory-land-lease (dalītais īpašums) buyout calculator pattern
- LV/LT/EE Baltic comparison primer
