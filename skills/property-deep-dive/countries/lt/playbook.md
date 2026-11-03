# Lithuania (LT) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: EUR (eurozone since 1 Jan 2015)
**Lang**: Lithuanian; English broadly available in major banks/legal firms

---

## Country profile

Lithuania is a small Baltic state (2,887,592 pop. on 1 Jan 2026 — 2026 data, source Eurostat tps00001) with a unified land/cadastre system (Registrų centras) — making title checks materially simpler than in Latvia. EU + eurozone + Schengen. Most foreign buyers transact in Vilnius (€3,197/m² apt avg, +12.2% YoY, Sep 2026 — 2026 data, source Ober-Haus OHBI); secondary cities (Kaunas, Klaipėda) trail. Major 2026 reforms: progressive PIT (20/25/32%) + new immovable-property tax structure for non-main residences. Lithuania disconnected from the Russia-controlled IPS/UPS (BRELL) grid on 8 Feb 2025 and synchronized with the Continental Europe Synchronous Area on 9 Feb 2025 (Litgrid) — energy-security upgrade, a macro context relevant to utility-cost stability (see `--mains`).

---

## Section: `--price`

**Primary index**: **Ober-Haus Apartment Price Index (OHBI)** — the most-cited monthly series; covers the 5 largest cities (Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys). Private-agency series (Ober-Haus is a brokerage) — secondary tier; cross-check with the Statistics Lithuania HPI.
- Page: https://www.ober-haus.lt/en/rinkos_apzvalgos/lithuanian-price-index/
- Annual Market Report PDF: https://www.ober-haus.lt/wp-content/uploads/Ober-Haus-Market-Report-Lithuania-2026.pdf
- **Sep 2026 Vilnius**: €3,197/m² apt avg, +0.9% MoM, **+12.2% YoY**; Kaunas €2,339, Klaipėda €2,103, Šiauliai €1,457, Panevėžys €1,432; five-city index +1.2% MoM, +13.7% YoY (2026 data, source Ober-Haus OHBI release, 12 Oct 2026: https://www.ober-haus.lt/en/buyers-are-paying-e20000-more-for-standard-apartments-than-a-year-ago/)
- **End-2025 Vilnius**: €2,930/m², +10.7% vs end-2024 (2025 data, source Ober-Haus Market Report 2026)

**Eurostat-aligned HPI**:
- **Statistics Lithuania (OSP)**: https://osp.stat.gov.lt/ (bot-blocked on HEAD, browser-OK)
- **Bank of Lithuania**: https://www.lb.lt/ (bot-blocked, browser-OK) — Real Estate Market Review + stress indicators
- **BIS / FRED**: https://fred.stlouisfed.org/series/QLTN628BIS — quarterly residential property price index

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| Aruodas | https://www.aruodas.lt/ | #1 by its own description ("No.1 real estate portal"), all property types, English site at https://en.aruodas.lt/ |
| Domoplius | https://www.domoplius.lt/ | sale + rent, all property types incl. new projects; filter for listings without intermediaries (be tarpininkų) |
| Skelbiu | https://www.skelbiu.lt/ | classifieds incl. RE |
| Kampas | https://www.kampas.lt/ | general listings (flats, houses, premises, plots); describes itself as LT's second most-visited real-estate portal |
| Ober-Haus | https://www.ober-haus.lt/ | premium agency + market reports |

**Verdict bands** (cmd: `--price`):
- 🟢 within ±10% of OHBI city avg for comparable district + condition
- 🟡 within ±20%
- 🟠 within ±30%
- 🔴 >±30% — investigate (could be: deferred maintenance, restitution flag, encumbrance, or genuine bargain — verify with Registrų centras extract)

**⚠️ Caveat**: Ober-Haus publishes nominal apt €/m² level for 5 cities (level series); Eurostat HPI is a quality-adjusted index (base=100). **Use whichever fits the question; don't compare growth rates across the two.**

---

## Section: `--traffic`

**Sources**:
- **AB „Via Lietuva"** — the state road authority (the former Lietuvos automobilių kelių direkcija / LAKD): https://vialietuva.lt/ — publishes traffic volumes (*eismo intensyvumas*) (2026-09-18 verified); road-condition info at https://eismoinfo.lt/ and open-data maps at https://maps.eismoinfo.lt/ (both linked from vialietuva.lt, 2026-10-23)
- **Trafi** — Vilnius public-transport app (journey planning, live directions, tickets); not a road-congestion feed: https://www.trafi.com/vilnius-app
- **OSM Overpass** for road class + maxspeed (universal — see `shared/preflight.md`)

**Output**: road class (magistraliniai A1–A21 / krašto / rajoniniai — A21 added to the state road list by Government Resolution No. 95 of 3 Feb 2016), maxspeed, AADT if available from Via Lietuva, noise translation (dB(A) inferred from OSM `highway=*` tag + maxspeed).

---

## Section: `--tax`

### Transfer / acquisition costs (individual buyer)

**No transfer tax / stamp duty** ("There are no stamp duties applied in Lithuania" — 2026 data, source PwC Worldwide Tax Summaries, last reviewed 1 Oct 2026). Lithuania is unusually clean here.

| Item | Amount |
|---|---|
| Notary fee | 0.37% of the price stated in the contract, min €76, max €5,000, listed excl. VAT (Government Resolution No. 498 of 28 Jun 2023, tariff item 25.1; 2026 data, source Vilnius 12th notary office tariff page); ≈0.45% of price if 21% VAT is charged (0.37% × 1.21, computed) |
| Registrų centras registration | ~€50–€200 standard (~0.03–0.5% of value) |
| **Total round-trip cost** | **under ~1% buyer side, est.** — notary ≈0.45% incl. VAT (computed above) plus Registrų centras registration and register-check fees (amounts not re-verified); excludes agent, legal, valuation and mortgage-notary costs |

Sources: notary tariff list — https://www.paupionotaras.lt/index.php/ikainiai (Vilnius 12th notary office, regulated entity); Lithuanian Notary Chamber — https://www.notarurumai.lt/en/ (no fee schedule on that page)

### Annual immovable property tax (NTM) — **MAJOR REFORM 1 Jan 2026**

**Pre-2026 (now historical)**: residents tax-exempt up to €150,000 total residential value (€200k for families w/ 3+ children); above that 0.5–2% municipal. Most owner-occupiers paid €0.

**From 1 Jan 2026** (NTMĮ art. 6, as published by VMI), marginal bands on the **total** taxable value of an individual's **non-main** residential (plus garages, gardens and other listed non-commercial) property:
- 0% up to €50,000
- 0.2% €50k–€200k
- 0.4% €200k–€400k
- 0.6% €400k–€600k
- 0.8% €600k–€1,000,000
- 1% above €1,000,000 (2026 data, source VMI NTM page; same bands in the Seimas press release of 26 Jun 2025 and the VMI 2026-changes summary updated 2026-01-15)

**Main dwelling**: municipal-set rate 0.1–1% on portion above municipal threshold (min €450,000); councils may differentiate by tax value and the owner's economic/social situation. Where a council set no threshold or rate by 1 Dec 2025, 0.1% applies in 2026 to the value above €450,000 (2026 data, source Seimas press release 26 Jun 2025 — https://www.lrs.lt/sip/portal.show?p_r=35403&p_k=1&p_t=292208). Per-person or large-family credits: none stated in the Seimas release or the VMI 2026-changes summary — check the council decision and https://www.vmi.lt/evmi/nekilnojamojo-turto-mokestis2. Main dwelling = the property where the owner has declared residence on the last day of the calendar month (VMI).

Sources:
- Ministry of Finance: https://finmin.lrv.lt/en/news/amendments-to-tax-laws-adopted-by-the-seimas/
- KPMG: https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2025/12/tnf-lithuania-dec-4-2025.pdf
- Seimas press release, 26 Jun 2025: https://www.lrs.lt/sip/portal.show?p_r=35403&p_k=1&p_t=292208
- VMI, *Mokesčių įstatymų pakeitimai nuo 2026-01-01* (updated 2026-01-15; covers GPM, NTM and VAT): https://www.vmi.lt/evmi/documents/20142/391071/Mokes%C4%8Di%C5%B3+%C4%AFstatymo+pakeitimai+nuo+2026-01-01.pdf

### Capital gains on property sale — GPM (Gyventojų pajamų mokestis)

**2025 schedule (pre-reform — now historical from 1 Jan 2026)**:
- **15% standard** (with two key exemptions):
  - **Owned >10 years** → fully exempt (10-year clock for income received before 1 Jan 2026, cut to 5 years from 2026 — see 2026 rules below; historical PwC summaries also noted a pre-2011-acquisition wrinkle)
  - **Declared primary residence ≥2 years** → exempt; OR proceeds reinvested in another residence (within 1 year before / 1 year after sale)
- Above €253,065 (2025 threshold) → **20%**

**2026 rules** (GPMĮ amended by Law No. XV-343 of 26 Jun 2025 and Law No. XV-680 of 16 Dec 2025, in force 1 Jan 2026):
- **Taxable gain** = sale price − acquisition price − other costs deductible under GPMĮ art. 19; it counts as non-employment income
- **15%** on the part that, together with other non-employment income, stays within **12 VDU (€27,745.80)** a year; the excess is taxed at **20%** up to 36 VDU (€83,237.40), **25%** from 36 to 60 VDU (€83,237.40–€138,729), **32%** above 60 VDU, with the 36/60 VDU bands counted on total annual taxable income including the 15% part (2026 data, source VMI 2026-changes summary; 2026 VDU = €2,312.15/month, so the euro thresholds move every year)
- **Exempt**: LT or other EEA real estate acquired **more than 5 years** before the sale (10 years before 2026); housing with declared residence for the last 2 years before the sale (unchanged in 2026, VMI); declared residence under 2 years but the proceeds used within 1 year from the sale to acquire another EEA home in which residence is then declared (GPMĮ art. 17(1)(54); PwC: "in one year after the sale")

Sources: PwC Worldwide Tax Summaries (last reviewed 1 Oct 2026) — https://taxsummaries.pwc.com/lithuania/individual/income-determination ; VMI 2026-changes summary (link under NTM sources above)

### Rental income — GPM

- **2025**: 15% on amounts up to €253,065/yr; above → 20% (pre-reform)
- **2026**: rent is non-employment income — **15%** on the part that, together with other non-employment income (incl. property-sale gains), stays within 12 VDU (€27,745.80); the excess joins annual income at 20% / 25% / 32% (36 VDU €83,237.40 / 60 VDU €138,729) (2026 data, source VMI; PwC, last reviewed 1 Oct 2026)
- **Or** via an **individual activity certificate** for short-term lets: a tax credit gives an effective **5%** on taxable profit up to €20,000, rising to 20% at €42,500; above €42,500 no credit, and the whole amount joins the 20/25/32% scale (2026 data, source VMI) / **business certificate** for personal-use properties: from 2026 the fixed-amount tax covers rental income up to **€50,000/yr**; the excess is non-employment income (15% within 12 VDU, then 20/25/32%) (2026 data, source VMI)
- **Bank of Lithuania (Lietuvos bankas) macroprudential** Responsible Lending Regulations (Board Resolution No 03-144 of 1 Sep 2011, as amended), for new housing loans from **1 Aug 2026** (Resolution No 03-146 of 22 Oct 2025): **LTV ≤90%** for first-time homebuyers (no real estate owned in the 5 years before applying), **85%** baseline for other first housing loans, **≤70%** for second and subsequent housing loans (≤85% if more than 50% of the principal of each previous mortgage is repaid); **DSTI ≤50%** of net income calculated at an interest rate of at least 6% (replacing 40% at the actual rate + 50% at ≥5%); **max maturity 30 years** (no maturity change notified with the 2026 amendment) (2026 data, source Bank of Lithuania notification to the ESRB, published 24 Oct 2025 — https://www.esrb.europa.eu/pub/pdf/other/Esrb.notification251024_BBMs_LT~1ed213ffce.pt.pdf ; https://www.lb.lt/)

### VAT new-build

- Standard 21% (2026 data, source PwC, last reviewed 1 Oct 2026)
- **New build sold within 24 months of completion → 21%**; resale of older buildings → exempt (seller can opt to charge VAT B2B)
- Accommodation services: reduced rate **12%** from 1 Jan 2026 (was 9%) (2026 data, source VMI 2026-changes summary; PwC)

---

## Section: `--rental`

### Long-term rental
- Two tax routes (VMI): (a) annual declaration: 15% on rental plus other listed non-employment income up to 12 average wages (€27,745.80 in 2026); the excess is taxed at 20% up to 36 AW (€83,237.40), 25% from 36 to 60 AW (to €138,729) and 32% above, the band depending on total annual taxable income with the first 12 AW counted too (2026 data, source VMI; PwC Worldwide Tax Summaries, reviewed 1 Oct 2026); or (b) a residential-letting business certificate (gyvenamosios paskirties patalpų nuoma): fixed tax set by the municipal council and paid separately for each property, tenants must be individuals, income cap €50,000/yr from 1 Jan 2026 (€45,000 to end-2025); income above the cap is taxed as in route (a): 15% within 12 AW together with other non-employment income, 20/25/32% beyond (2026 data, source VMI)
- No expense deduction on either route (secondary: financiallithuanians.lt, Dec 2025 — verify at vmi.lt); VMI does not treat property letting as individual activity, so the individual-activity expense deduction does not apply to plain letting (2026 data, source VMI)
- Vilnius secondary-market rents +3% in 2025, after +3% in 2024 and +10% in 2023 (2025 data, source Ober-Haus Market Report 2026 — private agency, secondary)

### STR / Airbnb

**Vilnius city tax**: **€2 per person per night** from 1 Jan 2024 (was €1 since 1 Jul 2018); stays of 30+ days exempt (2026 data, source Go Vilnius). Airbnb collects it and transfers it to Vilnius City Municipality directly; from 15 Jun 2026 Booking.com also collects it from guests on new bookings and pays it to the provider with the payout, and the provider still declares and remits it (2026 data, source Go Vilnius). Vilnius was the first Baltic city with an Airbnb auto-collection deal, from 1 Feb 2020 (per BNS via Delfi, 15 Jan 2020 — secondary).
- https://www.govilnius.lt/plan-your-trip/city-tax
- https://www.airbnb.com/help/article/2702

**Host tax routes** (VMI distinguishes letting — *nuoma* — from accommodation services — *apgyvendinimo paslaugos*; which applies depends on the services provided):
- **Residential-letting business certificate (verslo liudijimas)**: fixed municipal tax per property, guests must be individuals, letting period of the owner's choice; owner-run Booking.com/Airbnb listings qualify, listings run by a rental-management or intermediary company do not (those only via annual declaration at 15% / progressive bands); income cap €50,000/yr from 1 Jan 2026 (2026 data, source VMI)
- **Accommodation services**: a separate business-certificate type, or registered **individual activity** — 20% PIT less a tax credit, effective ~5% up to €20,000 taxable income, rising to 20% at €42,500; above €42,500 aggregated at 20/25/32% (2026 data, source PwC Worldwide Tax Summaries, reviewed 1 Oct 2026 — secondary)

**All rental income taxable — no exemption threshold.**

**Residential-use rule**: when residential premises in practice become dedicated to guest accommodation, the activity can count as accommodation services, i.e. use not according to the registered purpose under the Government's Description of cases and procedure for using a building (its premises) not according to its purpose (Statinio (jo patalpų) naudojimo ne pagal paskirtį atvejų ir tvarkos aprašas); fines for individuals €280–€3,000, repeat €400–€6,000 (Sorainen commentary via infolex.lt — law firm, secondary; verify against the Code of Administrative Offences)

**2025-2026 reform watch**:
- Regulation (EU) 2024/1028 on STR data collection applies from 20 May 2026 in opt-in/opt-out mode: Member States are not obliged to apply it, but any STR registration procedure or platform-data request they introduce must go through it, with registration fully online and platform data shared via a national Single Digital Entry Point (European Commission DG GROW, 20 May 2026). Lithuania: no national STR registration-number scheme or implementing act found as of 2026-10-21 (LOW — see `shared/regulatory-watch.md` § LT); a host-practitioner blog (Modernus svetingumas, 17 Jun 2026, anecdotal) reports that a separate STR registration was discussed but not introduced, and that the number Booking.com asks LT hosts for is the Registrų centras unique property number (unikalus daikto numeris), not an STR registration number — verify at e-tar.lt / eimin.lrv.lt
- Government draft (Ministry of Environment) re-regulating use of buildings and premises not according to their purpose, with a planned entry into force of 1 Nov 2026 (Kauno diena, 7 Oct 2026 — secondary); per the Lithuanian Business Confederation's comments of 18 Sep 2026 (stakeholder submission — secondary), the draft would require consent from the owners in the stairwell and of adjoining units for accommodation in apartments. Adoption not confirmed as of 2026-11-03 — verify at e-tar.lt / am.lrv.lt
- No Vilnius-wide cap or zoning ban found as of 2026-11-03 (unlike Lisbon/Barcelona) — verify at vilnius.lt

Sources: https://single-market-economy.ec.europa.eu/news/new-rules-bring-increased-transparency-short-term-rentals-sector-2026-05-20_en (European Commission) + EUR-Lex CELEX 32024R1028: https://eur-lex.europa.eu/eli/reg/2024/1028/oj/eng

---

## Section: `--work=<profession>`

Standard universal `--work=<profession>` resolution. Strongest demand: tech (Vilnius hub, fintech post-Brexit migration), bio-tech (Kaunas, Vilnius), logistics (Klaipėda port + Free Economic Zone), shared-services (Vilnius). Remote/hybrid common.

---

## Section: `--risks`

### Flood
- **Aplinkos apsaugos agentūra (EPA) flood hazard and risk map** (*Potvynių grėsmės ir rizikos žemėlapis*): https://potvyniai.aplinka.lt/ (redirects to the EPA ArcGIS app). Old mirror `vanduo.gamta.lt/info/potvyniai.aplinka.lt`: ❌ DEPRECATED — dead on 2026-10-23 (TLS certificate mismatch); verify with Aplinkos apsaugos agentūra
- Significant high-risk flood phenomena form on **56 larger rivers** plus the Baltic Sea and Curonian Lagoon coasts (2026 data, EPA figures in an organisation release of 25 Feb 2026 via 15min.lt — secondary). The EPA's Jan 2026 release of the same title (via BNS Spaudos centras, 27 Jan 2026 — secondary) gave **54 rivers**, without the 'significant, high-risk' and 'larger' qualifiers; the later 56 is used — verify the current count with Aplinkos apsaugos agentūra. EPA 2018–2024 preliminary flood risk assessment review: https://aaa.lrv.lt/lt/veiklos-sritys/vanduo/upes-ezerai-ir-tvenkiniai/potvyniu-rizikos-valdymas/preliminaraus-potvyniu-rizikos-vertinimo-atnaujinimas-2018-2024-m
- Highest exposure: **Nemunas Delta** (Šilutė, Rusnė), **Klaipėda coast** (storm-surge + Curonian Lagoon), Telšiai/Tauragė/Kėdainiai/Panevėžys/Kaunas districts
- ThinkHazard river-flood level: **High** — damaging river floods expected at least once in the next 10 years (country-level, not parcel-level; 2026 data, source ThinkHazard): https://thinkhazard.org/en/report/147-lithuania/FL

### Coastal
- Klaipėda + Curonian Spit (Neringa) — sea-level rise + storm surge; compound coastal-river risk documented (MDPI Water 2022)

### Seismic
- Negligible. Baltic Shield craton — peak ground acceleration ~<0.04g est. for 475-year return (European seismic hazard maps — verify at ESHM); ThinkHazard earthquake level **Very low** — under 2% chance of potentially-damaging shaking in 50 years (2026 data, source ThinkHazard https://thinkhazard.org/en/report/147-lithuania/EQ); **no building seismic code requirement**

### Forest fire
- Highest in **Dzūkija** (SE LT — Varėna, Alytus, Lazdijai, Druskininkai districts) — Scots pine on infertile sandy soils + Čepkeliai peatland
- Source: https://www.mdpi.com/2073-445X/11/2/260

### Geoportal layers
- https://www.geoportal.lt/ — overlay flood, environmental, protected, cadastre

### Mandatory diagnostics

- **Energy Performance Certificate (Pastato energinio naudingumo sertifikatas)**: mandatory for sale, rental, new construction. Classes A++ to G (9 classes). Validity 10 years (2026 data, source namupridavimas.lt, a private certifier — secondary; that page still cites the older STR 2.01.09:2005). STR 2.01.02:2016 governs. Certificate register: VšĮ Statybos sektoriaus vystymo agentūra (SSVA) https://www.ssva.lt/cms/veiklos-sritys/pastatu-energinis-naudingumas/pastatu-energinio-naudingumo-sertifikatu-registras
  - https://www.namupridavimas.lt/en/services/certification-of-the-energy-performance/
- **Radon**: national avg 55 Bq/m³ in dwellings and public premises (Radiation Protection Centre (RSC), citing the EC JRC radon-survey overview, via 15min.lt Mar 2024 — secondary; same figure as the 400-house survey in Gasiūnas, Mastauskas & Morkūnas, *Journal of Civil Engineering and Management* 4(4), 1998 — rates/figures may have changed since), well below the **300 Bq/m³** indoor reference level (HN 73:2018, Euratom 2013/59 transposed; 2025 data, source RSC). **Karst region in N Lithuania (Biržai, Pasvalys, Pakruojis)** averaged 125 Bq/m³ in that survey (1998 data, source Gasiūnas et al. — rates/figures may have changed since), with localized hot-spots. No radon risk zones designated in Lithuania (2025 data, source RSC radon page). **No statutory pre-sale radon test required.** RSC: https://rsc.lrv.lt/lt/informacija-gyventojams/radono-skleidziama-apsvita · radon map: https://gis.rsc.lt/portal/apps/dashboards/fa282e107529424fa0a0da99d0916ed6
- **Asbestos**: no mandatory pre-sale survey for residential. Soviet-era apartment blocks (1960s–80s) commonly contain asbestos (slate roofing, pipe insulation, wall panels) — material risk on retrofits

---

## Section: `--mains`

### Cadastre / Land Registry — UNIFIED

**VĮ Registrų centras** (State Enterprise Centre of Registers):
- https://www.registrucentras.lt/ (the old `/en/` path now redirects to the contract-customer portal, `usr/paslaugos.php` → ipasas.lt — 2026-10-23)
- Single national register: cadastre + Real Property Register + addresses + legal persons
- Search by cadastral number, address, or unique ID
- Real Property Register extract (*NTR išrašas*): **€2.64** electronic (3 working days, 10 for non-owners; instant in self-service for owners), **€5.28** within 1 working day; paper **€3.04** + printing (2026 data, source Registrų centras https://www.registrucentras.lt/paslauga/nekilnojamojo-turto-registro-israsas). Non-owners must state the purpose and legal basis and get the extract only if Registrų centras staff approve; a depersonalised extract (no owner name or personal code) is also offered. In person: passport, ID card or EU/EEA driving licence
- **Encumbrances/mortgages NOT visible online for free** — must buy the extract

**Spatial portal**: https://www.geoportal.lt/ (INSPIRE-compliant national SDI)

### District heating

Soviet-built; substantially modernized. Network heat losses dropped from **33% → 15%** on average (1996–2018 series, source LSTA — rates/figures may have changed since); ~46% of the 2,700 km DH pipe network replaced with pre-insulated pipes; DH serves over 700,000 customers and heats over half the population (2025 data, source IEA Energy Policy Review Lithuania 2025).
- **LSTA stats**: https://lsta.lt/en/about-dh-sector/ (browser-OK)
- **IEA Lithuania 2025 review**: https://iea.blob.core.windows.net/assets/0f37fbed-856d-4fde-8f2b-4db10d9bfd2a/Lithuania2025.pdf
- Bioenergy share of national DH production: over 70% in 2023, up from ~7% in 2005; target 90% renewable DH by 2030 (2023 data, source IEA Energy Policy Review Lithuania 2025) — rates/figures may have changed since. National figure — verify the Vilnius/Kaunas/Klaipėda share with the local DH supplier

**Soviet-era multi-apartment quirk**: Many old blocks have **single-pipe vertical heating risers** — no per-apartment metering or shut-off; bills allocated by m². "Renovated" (apkainotas) blocks have horizontal distribution + individual meters.

### Water/sewage
- Municipal utilities: Vilniaus vandenys, Kauno vandenys, etc.
- Rural areas: well + septic (~60% of rural households — est., re-verify with osp.stat.gov.lt household water-supply census)
- No nationwide single registry — check connection per-property via the municipal utility

### Electricity
- **ESO (AB Energijos skirstymo operatorius)** — dominant DSO serving 1.6 million customers; one of three active distribution system operators (2025 data, source IEA Energy Policy Review Lithuania 2025)
- **Lithuania exited BRELL grid 8 Feb 2025** and synchronised with the Continental European Synchronous Area on 9 Feb 2025 (IEA Energy Policy Review Lithuania 2025) — landmark energy-security event. The IEA reports electricity prices surged after the February 2025 desynchronisation (500 MW of Polish capacity kept in reserve; Estlink 2 damaged Dec 2024) (2025 data, source IEA) — verify current tariffs at ESO / VERT

---

## Section: `--crime`

See `shared/crime-sources.md` for the per-country contract. Lithuania uses:
- **Informatikos ir ryšių departamentas (IRD) prie Vidaus reikalų ministerijos** (Ministry of the Interior): https://www.ird.lt/ — keeps the criminal-offences register (NVŽR); open data *Nusikalstamumas pagal savivaldybes* gives registered offences per 100,000 residents by municipality, 2004–2026, CSV export: https://ird.lt/lt/atviri-duomenys-2/nusikalstamumas-pagal-savivaldybes — municipality-level, never a street- or parcel-level rating
- **Statistics Lithuania crime tables**

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

---

## Cost benchmarks (Apr 2026)

| Item | Range / typical |
|---|---|
| Vilnius apt €/m² avg | €3,197 (OHBI Sep 2026) |
| Kaunas / Klaipėda | €2,339 / €2,103 (OHBI Sep 2026), i.e. 27% / 34% below Vilnius (computed: 1 − 2,339/3,197; 1 − 2,103/3,197) |
| Notary fee | 0.37% of price, min €76, max €5,000, excl. VAT (2026 data, Government Resolution No. 498 tariff) |
| Registration fee | ~€50–€200 |
| Total acquisition costs | under ~1% est. (notary ≈0.45% incl. 21% VAT + Registrų centras fees — see `--tax`) |
| Annual property tax (main, ≤€450k) | €0 (statutory non-taxable value ≥€450,000; 2026 data, source Seimas / VMI) |
| EPC certificate | ~€150–€400 |

---

## Active fiscal incentives

- **No transfer tax** — already a structural incentive
- **Declared-residence ≥2yr CGT exemption** OR **>5yr holding exemption** for any LT/EEA real estate (10 years for sales before 1 Jan 2026) (2026 data, source VMI; PwC)
- **Reinvestment relief**: declared residence under 2 years, proceeds reinvested within 1 year in another EEA home (timing detail: see `--tax`)
- **5% individual-activity flat tax** for STR if registered

---

## Foreign-buyer rules

- **EU/EEA citizens**: buildings and premises on the same terms as LT citizens (ELRA contact-point contribution, undated). Land, inland waters and forests: open to them under the 'European and transatlantic integration' criteria of the Constitutional Law implementing Constitution Art. 47(3) (art. 4), on the same terms as LT citizens (art. 6(1)), subject also to the Land, Agricultural Land Acquisition, Water and Forest Laws for the plot's main use (Nacionalinė žemės tarnyba press release, 22 May 2019 — https://sc.bns.lt/view/item/uzsienieciu-teise-isigyti-zemes-lietuvoje-306603; same criteria in the Lithuanian Notary Chamber article of 30 Apr 2026 — https://www.notarurumai.lt/naujienos/uzsienieciu-galimybes-isigyti-turta-lietuvoje-ka-numato-lietuvos-istatymai/1027). Agricultural-land buyer conditions under the Law on Acquisition of Agricultural Land not re-verified — verify with the notary / NŽT. The art. 9 list of land foreigners may not acquire (agricultural land, most forestry land, border strips, Curonian Spit, free-economic-zone land and others), still quoted by the ELRA contribution, sits in the Constitutional Law's transitional third section, which applied only until EU accession (art. 17(1), 2003 text via https://www.infolex.lt/teise/DocumentSinglePart.aspx?AktoId=97702&StrNr=1) (superseded)
- **Non-EU**: can buy residential and commercial urban property freely; **CANNOT buy agricultural / forest land** unless holding LT residency permit + meeting activity criteria. https://www.elra.eu/contact-point-contribution/lithuania/limitations-to-foreigners-10/
- **Border-zone / restricted land**: the ELRA contribution quotes art. 9 of the Constitutional Law barring foreigners from land in border sections, national-defence and security-restricted territories, free-economic-zone land, the Curonian Spit and Lagoon (except towns without resort status), state parks and reserves, and protected heritage sites, among others — check the plot's status in the Registrų centras extract and with the notary. The Constitutional Law's art. 9 list barring foreigners from border-strip, Curonian Spit, free-economic-zone and other land (still quoted by the ELRA contribution) applied only until EU accession (transitional third section, art. 17(1)) (superseded) — check the plot's status in the Registrų centras extract and with the notary
- **Russian/Belarusian nationals (post-2022)**: residence permits heavily restricted → indirectly blocks land/agricultural purchases requiring residency. Bank account opening (KYC) and notarial AML checks now near-blocking even for residential

---

## Country-specific quirks

- **Vilnius land readjustment**: Soviet-era blocks often sit on land never properly cadastralized at parcel-by-parcel level. Many condominiums have **shared/undivided parcel** (bendrojo naudojimo žemės sklypas) — affects renovation, easements, additions. Confirm cadastral parcel matches building footprint via Registrų centras
- **Klaipėda Free Economic Zone** (412 ha): 0% real estate tax in free economic zones; 0% income tax for 10 years, then 8% for the next 6 years (2026 data, source Klaipėda FEZ — https://www.fez.lt/explore-the-free-zone/). Industrial only — not residential. https://www.fez.lt/
- **Denationalization legacy**: 1991 restitution applied **only to LT citizens at time of nationalization**, excluding most diaspora. Largely concluded; **no restitution exists yet for heirless Jewish property**. Some urban plots in Vilnius/Kaunas have unresolved historic-claim flags — pull "Ownership history" in Registrų centras extract
- **Curonian Spit (Neringa) UNESCO**: strict heritage rules; new construction effectively banned in protected zone. Buy resale only; expect renovation permit complexity. Foreigners may not acquire Curonian Spit land except in towns without resort status (Constitutional Law art. 9, per ELRA); buildings and premises stay open to them
- **Old Town Vilnius (UNESCO 1994)**: demolition forbidden, exterior changes need Heritage Commission consent
- **Banking**: 3 Scandinavian banks dominate (Swedbank, SEB, Luminor). Mortgage to non-residents possible but typically requires LT income source or a larger deposit (non-resident LTVs commonly capped well below the Responsible Lending Regulations ceilings at `--tax` — 85% baseline, 90% for first-time homebuyers from 1 Aug 2026 — verify with the specific bank)

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre + title | Registrų centras | https://www.registrucentras.lt/ |
| Tax | VMI (State Tax Inspectorate) | https://www.vmi.lt/ |
| Notary | Lithuanian Notary Chamber | https://www.notarurumai.lt/en/ |
| Flood | EPA / Aplinka | https://potvyniai.aplinka.lt/ |
| Radon | Radiation Protection Centre (Radiacinės saugos centras) | https://rsc.lrv.lt/ |
| Foreign land purchase (residence permit) | Migration Department (Migracijos departamentas) | https://migracija.lrv.lt/ |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastral extract | https://www.registrucentras.lt/paslauga/nekilnojamojo-turto-registro-israsas |
| Tax rules (PIT/CGT) | https://taxsummaries.pwc.com/lithuania/individual/income-determination |
| Property tax 2026 | https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2025/12/tnf-lithuania-dec-4-2025.pdf |
| Flood map | https://potvyniai.aplinka.lt/ |
| Radon | https://gis.rsc.lt/portal/apps/dashboards/fa282e107529424fa0a0da99d0916ed6 |
| Vilnius city tax | https://www.govilnius.lt/visit-vilnius/plan-your-trip/city-tax |

---

## Status

**Confidence**: HIGH on the 2026 statutory tax rules re-read in the 2026-10-23 refresh wave: NTM bands for non-main property and the €450,000 main-dwelling floor (VMI NTM page; Seimas release of 26 Jun 2025; VMI 2026-changes summary), GPM 15% up to 12 VDU then 20% / 25% / 32% and the 2-year declared-residence / 5-year holding CGT exemptions (VMI 2026-changes summary; PwC, last reviewed 1 Oct 2026); HIGH on the Vilnius city tax (€2 from 1 Jan 2024, Go Vilnius; re-verified 2026-09-24). MEDIUM on no transfer tax / stamp duty (secondary sources only: PwC, last reviewed 1 Oct 2026, and a VLO law-firm buyer guide read 2026-11-03), the notary tariff (Government Resolution No. 498, read on one notary office's tariff page), the Bank of Lithuania LTV / DSTI limits for housing loans from 1 Aug 2026 (Bank of Lithuania resolutions cited in `--tax`; lb.lt not readable to bots), 12% accommodation VAT from 1 Jan 2026 (VMI 2026-changes summary) and the `--rental` tax routes (VMI page text as returned by a search index, cross-checked against PwC; vmi.lt blocks bots). MEDIUM on price levels: Ober-Haus OHBI to Sep 2026 is a brokerage series (secondary); the BIS / FRED quarterly index runs to Q1 2026 and the Statistics Lithuania HPI could not be read. MEDIUM on 2026 main-dwelling NTM in the three largest city municipalities (not the surrounding district municipalities): Vilnius, Kaunas and Klaipėda set no main-dwelling threshold or rate, so the statutory 0.1% on value above €450,000 applies in 2026 (Klaipėda City Municipality release of 27 Nov 2025; Vilnius per LRT and Delfi / ELTA, Kaunas per LRT / ELTA, Nov 2025 — secondary; read 2026-11-03); other councils' rates not checked. MEDIUM on `--risks` and `--mains`: flood portal, ThinkHazard levels, radon figures, Real Property Register extract fees and district-heating figures re-sourced; the flood-exposure district list, the MDPI coastal and forest-fire claims, the seismic PGA wording, the EPC rule STR 2.01.02:2016, the asbestos line and the Soviet-block riser and rural water claims not re-fetched. MEDIUM on foreign-buyer land rules (NŽT and ELRA read, readings partly conflicting; agricultural-land buyer conditions and Russia / Belarus rules not verified). LOW on the Lithuanian STR registration outcome: Reg (EU) 2024/1028 has applied since 20 May 2026 in opt-in/opt-out mode, so Member States are not obliged to run a registration scheme (European Commission, 20 May 2026); no Lithuanian scheme, implementing act or single-digital-entry-point designation was found in the 2026-10-21 searches of e-tar.lt, e-seimas.lrs.lt and eimin.lrv.lt, and a host-practitioner blog (Modernus svetingumas, 17 Jun 2026, forum tier) reports that a separate registration was discussed but not introduced — verify at e-tar.lt / eimin.lrv.lt. LOW on the 'no exemption threshold' rental claim (2018 Airbnb / PwC guide only), the adoption of the Government draft on use of premises not according to purpose (secondary only), Registrų centras registration fees, the 30-year maximum loan maturity, the VAT 24-month new-build rule, the EPC certificate cost and the `--work` demand claims (qualitative, unsourced); the playbook gives no per-locality rents or yields. Tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)
- 2026-10-21: Tax tracker entry re-checked (December regwatch wave, run early; see shared/regulatory-watch.md).
- 2026-10-23: refresh wave (market, tax-legal, risk-infra) plus audit corrections; per section, facts changed / confirmed / unverifiable. Re-verified (see the per-section table): Country profile 4 / 1 / 1 (population 2,887,592 on 1 Jan 2026, Eurostat; Vilnius €3,197/m², +12.2% YoY, OHBI Sep 2026; BRELL disconnection 8 Feb 2025 and synchronisation 9 Feb 2025, Litgrid); `--price` 3 / 6 / 0 (OHBI Sep 2026 figures replace Dec 2025; Ober-Haus labelled a brokerage series, secondary; 2026 market-report URL); `--price` listings 3 / 2 / 0 (rank claims marked as portal self-descriptions, Domoplius '#2' dropped); Active fiscal incentives 3 / 1 / 0 (holding exemption 5 years from 2026, 10 before; reinvestment timing detail moved to `--tax`); Source URL templates 3 / 3 / 0 (cadastral and radon templates replaced); `--amenities` / `--climate` pointers confirmed. Partly re-verified, still on the 2026-04-26 playbook date: `--tax` 12 / 7 / 6 (2026 GPM 15% up to 12 VDU then 20% / 25% / 32%; notary tariff 0.37% excl. VAT, min €76, max €5,000, replacing 0.45% / ~€5,800; main-dwelling NTM default 0.1% above €450,000; Bank of Lithuania LTV 90% for first-time buyers from 1 Aug 2026; accommodation VAT 9% → 12%); `--rental` 9 / 4 / 3 (VMI tax routes; Booking.com collects the Vilnius city tax from 15 Jun 2026; Reg (EU) 2024/1028 described as an opt-in regulation applying since 20 May 2026, replacing the 'Lithuania will introduce' prediction); `--work` 1 / 0 / 1 (Klaipėda 'free port' → Free Economic Zone); Cost benchmarks 5 / 0 / 2 (price, notary, total-cost and main-dwelling tax rows; registration and EPC rows unverified; heading '(Apr 2026)' unchanged); Foreign-buyer rules 4 / 1 / 4 (land criteria re-read against NŽT and ELRA); Country-specific quirks 4 / 3 / 3 (FEZ 0% income tax for 10 years, then 8% for 6 years; non-resident LTV reference updated); `--traffic` 3 / 1 / 1 (lakd.lt replaced by Via Lietuva; Trafi is a transit app, not a congestion feed; A1–A21); `--risks` 6 / 7 / 7 (vanduo.gamta.lt mirror ❌ DEPRECATED; 54 flood areas → 56 rivers; ThinkHazard flood High / earthquake Very low; radonas.lt, a radiator firm, replaced by the Radiation Protection Centre); `--mains` 6 / 5 / 7 (NTR extract €2.64 / €5.28 / €3.04; ESO one of three DSOs; DH bioenergy over 70% nationally in 2023; post-synchronisation price surge per IEA); `--crime` 1 / 1 / 1 (IRD under the Ministry of the Interior); Verification authorities 2 / 3 / 1 (radon and Migration Department rows → rsc.lrv.lt / migracija.lrv.lt). Status footer (sources read 2026-11-03): STR-registration limb restated as LOW with no Lithuanian scheme found, and the 2026 main-dwelling NTM limb settled for the Vilnius, Kaunas and Klaipėda city municipalities (statutory 0.1% above €450,000); Confidence line recomputed. Playbook-level date not re-stamped: `--tax`, `--rental`, `--risks`, `--mains` and `--work` still hold claims not re-fetched.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | Eurostat population (1 Jan 2026); OHBI Sep 2026 Vilnius figures; BRELL disconnection / synchronisation dates (Litgrid); PIT 20 / 25 / 32% (PwC); "most foreign buyers in Vilnius" unsourced |
| `--price` (incl. listings) | 2026-10-23 | 2026-10-23 refresh wave | OHBI Sep 2026 (Ober-Haus release of 12 Oct 2026, brokerage series, secondary); BIS / FRED index to Q1 2026; OSP and Bank of Lithuania sites not readable to bots; listing ranks marked as portal self-descriptions |
| Active fiscal incentives | 2026-10-23 | 2026-10-23 refresh wave | 2-year residence and 5-year holding exemptions and the reinvestment window checked against VMI and PwC; reinvestment timing detail in `--tax` |
| `--amenities` | 2026-10-23 | 2026-10-23 refresh wave | Pointer only — `shared/amenities-osm.md` |
| `--climate` | 2026-10-23 | 2026-10-23 refresh wave | Pointer only — `shared/climate-projections.md` |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | Cadastral template → NTR extract service; radon → RSC radon map; Vilnius city-tax URL follows its redirect; PwC, KPMG and flood-map URLs live (no figures in this table) |

---

## Extension TODOs

- Per-municipality 2026 NTM main-dwelling rate table beyond the three largest cities: the Vilnius, Kaunas and Klaipėda city municipalities set no main-dwelling threshold or rate, so the statutory 0.1% on value above €450,000 applies there in 2026 (2026 data, source Klaipėda City Municipality release of 27 Nov 2025; Vilnius and Kaunas per LRT / ELTA, Nov 2025 — secondary); other councils may set 0.1–1% above a threshold of at least €450,000
- Specific per-district Vilnius €/m² rents (currently only sale prices)
- LV/LT/EE Baltic comparison primer for cross-border investors
