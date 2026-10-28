# Slovenia 🇸🇮 — Property Due-Diligence Playbook

ISO2: `si`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1000` Ljubljana, `2000` Maribor, `3000` Celje, `4000` Kranj, `6000` Koper, `9000` Murska Sobota)
- **Admin levels**: 12 statistical regions + 212 občine (municipalities)
- **Currency**: **EUR (€)** — adopted 1 Jan 2007 (first new EU member to join eurozone)
- **Languages**: Slovenian (official); Italian + Hungarian (constitutional minorities along borders)
- **Cadastre**: **GURS (Geodetska uprava RS)** — Surveying and Mapping Authority
- **Identifier**: **parcelna številka** + **katastrska občina (KO)** (e.g., `123/4 k.o. Ljubljana`)
- **Ownership types**:
  - **Lastnina** (full ownership)
  - **Etažna lastnina** (condominium ownership for apartments)
  - **Solastnina** (co-ownership)
  - **Skupna lastnina** (joint ownership)
  - **Stavbna pravica** (right to build on someone else's land)
- **Zemljiška knjiga** (land register, e-Sodstvo) governs all real estate

## Section: `--price`

### Primary sources

- **GURS Javni vpogled v podatke o nepremičninah** (FREE official cadastre): `https://ipi.eprostor.gov.si/jv/`
- **GURS Vrednotenje** (mass valuation, free public viewer): `https://vrednotenje.gov.si/EV_JV/`
  - **MAJOR REFORM 13 May 2025**: Uredba o določitvi modelov vrednotenja nepremičnin applied and new posplošene vrednosti assigned; owners were mailed the new values 26 May – 1 Jul 2025 (2025 data, source gov.si GURS)
- **OPSI** open data: `https://podatki.gov.si/dataset/kataster-nepremicnin`
- **ETN (Evidenca trga nepremičnin)** — transactions register, GURS-managed
  - Raw per-transaction ETN data are public: downloadable through Javni geodetski podatki (JGP) and viewable for recent years in the Vpogled v aktualne cene nepremičnin app; contracting parties' personal data are excluded, and deals a company has marked as a business secret are withheld (source [e-prostor, Trg nepremičnin](https://www.e-prostor.gov.si/podrocja/trg-in-vrednosti-nepremicnin/trg-nepremicnin/), read 2026-10-23)
- **e-Sodstvo Zemljiška knjiga**: `https://esodisce.si/` — land register lookup (updated 2026-10-23; the old evlozisce.sodisce.si address 301-redirects here)
- **SURS (Statistični urad RS)**: `https://www.stat.si/` — national stats

### Listing platforms

- **Nepremicnine.net**: `https://www.nepremicnine.net/` — the main portal by reputation (wisdom, not data: no traffic or listing-share figures verified; the site could not be read for verification on 2026-10-23 — check it directly)
- **Bolha.com**: `https://www.bolha.com/nepremicnine`
- **Slonep.net** — listing portal; activity not verified (the site could not be read for verification on 2026-10-23 — check it directly)
- **Salomon.si** ❌ DEPRECATED — dead on 2026-10-23 (connection refused); verify listings on Nepremicnine.net / Bolha.com
- Agencies (agency-published ⚠️): **RE/MAX** (`https://www.re-max.si/` — 17 offices listed in its office sitemap, read 2026-10-23; remax.si is an unrelated pool company), **DODOMA** (`https://www.dodoma.si/` — a Maribor agency, read 2026-10-23); **Stoja Trade** not verified (the site could not be read for verification on 2026-10-23 — check it directly)

### H1 2026 price benchmarks (GURS ETN transacted prices, secondary market)

| Area (GURS analytical area) | Used apartment €/m² — median (25th–75th pct) | Used house total € — median (25th–75th pct) |
|---|---:|---:|
| **Ljubljana** | 5,630 (4,900–6,500) | 504,000 (390,000–640,000) |
| **Ljubljana okolica — north** | 4,580 (3,920–5,340) | 390,000 (304,000–488,000) |
| **Ljubljana okolica — south** | 4,170 (3,670–4,880) | 330,000 (261,000–448,000) |
| **Obala** (incl. Koper, Ankaran, Izola, Piran) | 5,070 (4,380–6,160) | 335,000 (253,000–502,000) |
| **Kranj in okolica** | 4,090 (3,330–4,630) | 322,000 (245,000–380,000) |
| **Maribor** | 3,010 (2,610–3,350) | 251,000 (211,000–342,000) |
| **Celje** | 2,980 (2,560–3,470) | 257,000 (186,000–290,000) |
| **Slovenia** (national) | 3,520 (2,580–5,050) | 210,000 (127,000–330,000) |
| **Bled / Bohinj, smaller towns, rural Štajerska / Prekmurje** | not published separately — verify per municipality at GURS ETN | not published separately — verify at GURS ETN |

€/m² is per m² of uporabna površina. H1 2026 vs H1 2025: national apartment median +€450/m², house median +€30,000. Most Obala house sales are in the hinterland; coastal towns price closer to Ljubljana. (2026 data, source [GURS polletno poročilo o trgu nepremičnin, H1 2026](https://www.e-prostor.gov.si/fileadmin/Podrocja/Trg_vrednosti_nep/Trg_nepremicnin/Porocila_o_trgu_nepremicnin/2026/Polletno_porocilo_za_leto_2026.pdf), Oct 2026)

### 2025 reform — posplošena vrednost (MAJOR)

- **13 May 2025**: new regulation on property valuation models (Uredba o določitvi modelov vrednotenja nepremičnin) applied ([gov.si, 13 May 2025](https://www.gov.si/novice/2025-05-13-pripis-novih-posplosenih-vrednosti-nepremicnin/))
- **26 May – 1 Jul 2025**: GURS mailed owners zbirna potrdila with the new generalized values, which reflect the market on 1 Jan 2025 ([gov.si, 1 Jul 2025](https://www.gov.si/novice/2025-07-01-geodetska-uprava-zakljucila-postopek-obvescanja-lastnikov-o-novih-posplosenih-vrednostih-nepremicnin/))
- Total posplošena vrednost of the Slovenian real-estate stock: **~€297 billion** (values as at 1 Jan 2025, stock at end-2025); houses ~€95 bn (32%), apartments in multi-dwelling buildings ~€65 bn (22%) (2025 data, source [GURS Poročilo o slovenskem nepremičninskem trgu za leto 2025](https://www.e-prostor.gov.si/fileadmin/Podrocja/Trg_vrednosti_nep/Trg_nepremicnin/Porocila_o_trgu_nepremicnin/2025/Letno_porocilo_za_leto_2025.pdf), Apr 2026)
- At the 13 May 2025 launch GURS gave a preliminary total of €298 billion, almost **+8%** above the October 2024 trial calculation (poskusni izračun: €277 billion on 10 Jun 2024 data) — not a change against the 2020 values (2024–2025 data; €298 bn and +8%: GURS director quoted by [RTV SLO, 13 May 2025](https://www.rtvslo.si/slovenija/koliko-je-vredna-vasa-nepremicnina/745500), press; €277 bn: [GURS javna predstavitev predloga modelov, Oct 2024](https://www.e-prostor.gov.si/fileadmin/Podrocja/Trg_vrednosti_nep/Poskusni_izracun_2024/Javna_predstavitev_predloga_modelov_oktober_2024.pdf))
- National transacted-price growth (GURS ETN price indices, not posplošena vrednost changes):
  - Apartments: +67% (2019-2024); +77% (2020-2025)
  - Houses: +54% (2019-2024); +65% (2020-2025)
  - Building land for housing: +72% (2019-2024); +69% (2020-2025 — the 2025 report's foreword gives "almost 60%" for land)
  - (2024 and 2025 data, source GURS letno poročilo [2024](https://www.e-prostor.gov.si/fileadmin/Podrocja/Trg_vrednosti_nep/Trg_nepremicnin/Porocila_o_trgu_nepremicnin/2024/Letno_porocilo_za_leto_2024.pdf) and [2025](https://www.e-prostor.gov.si/fileadmin/Podrocja/Trg_vrednosti_nep/Trg_nepremicnin/Porocila_o_trgu_nepremicnin/2025/Letno_porocilo_za_leto_2025.pdf), Preglednica 11 in each)
- Sets the base for any future davek na nepremičnine

### Compute

1. €/m² = price / **uporabna površina** (usable area)
2. **Posplošena vrednost** ≠ market value: GURS defines it as a model estimate of market value on the model date — 1 Jan 2025 for the current values; models are reviewed every two years ([e-prostor, Posplošene vrednosti](https://www.e-prostor.gov.si/podrocja/trg-in-vrednosti-nepremicnin/posplosene-vrednosti/), read 2026-10-23). National transacted prices kept rising after that date (2025 vs 2024: apartments +11%, houses +10%, source GURS letno poročilo 2025, Preglednica 10; H1 2026 vs H1 2025: apartment median +€450/m², house median +€30,000, source GURS polletno poročilo H1 2026), so est. 2026 transacted prices run above posplošene vrednosti on average (inputs: 1 Jan 2025 model date plus that growth); the gap for one property is not published
3. **Etažna lastnina**: read **Pogodba o medsebojnih razmerjih** + **Zapisniki zborov etažnih lastnikov** + **Rezervni sklad** before buying flat

### Key terms

- Stanovanje = apartment
- Hiša = house
- Posplošena vrednost = generalized (mass-appraised) value — GURS model estimate of market value; proposed base for the davek na nepremičnine (not enacted — see `--tax`)
- ETN = real estate market evidence
- Etažna lastnina = condominium ownership
- Zemljiška knjiga = land register

---

## Section: `--traffic`

### Sources

- **DRSI (Direkcija RS za infrastrukturo)**: `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-infrastrukturo/`
- **DARS** (motorway operator): `https://www.dars.si/`
- **Promet.si**: `https://www.promet.si/` — DARS traffic-information centre for state roads; DRSI traffic-counter data also shown there
- **DRSI Štetje prometa** (PLDP per counted state-road section; DRSI counts since 1954; yearly PLDP files 1997–2025 on OPSI): `https://www.gov.si/zbirke/storitve/stetje-prometa/` · `https://podatki.gov.si/dataset/pldp-karte-prometnih-obremenitev`

### Key term

**PLDP (Povprečni letni dnevni promet)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (občinska cesta, residential)
- 🟡 1,500–10,000 v/d (državna cesta, regional route)
- 🟠 10,000–30,000 v/d (urban arterial, državna I.)
- 🔴 > 30,000 v/d (avtocesta, hitra cesta, Ljubljana ring — ring sections 38,094–95,341 v/d; 92 of 164 counted AC sections and 14 of 34 counted HC sections exceed 30,000; median AC 32,100, median HC ~19,100 v/d) (2025 data, source DRSI PLDP 2025 on OPSI)

---

## Section: `--tax`

### Annual property charges (NUSZ + davek od premoženja; comprehensive property tax NOT ENACTED)

- **NUSZ (Nadomestilo za uporabo stavbnega zemljišča)** — compensation for use of building land — currently the main municipal property charge
  - Set per občina via odlok (ordinance)
  - Amount: no national figure — FURS assesses it on the dwelling's floor area from the občina's odlok (points for zone, use and utility equipment) times the point value in force on 1 January (2026 data, source FURS Brošura o obdavčitvi nepremičnin, Sep 2026). Computed Ljubljana (MOL) example for 2026: a 70 m² flat in zone I with every utility the odlok scores = (100 zone + 125 utility points) × 70 m² × €0.000641 per m² per month × 12 ≈ **€121/yr** (MOL Odlok o NUSZ, Uradni list RS 130/03 as amended by 120/05; 2026 point value, Uradni list RS 114/25); other zones and občine differ — read the občina's odlok
  - Assessed by FURS for the občina, municipal revenue; payable by the direct user (owner or tenant); a buyer of a new flat or builder of a new family house can claim a 5-year exemption from the občina where the land-servicing costs were paid in the price or directly (2026 data, source FURS Brošura o obdavčitvi nepremičnin, 8th ed., Sep 2026)
- **Davek od premoženja** (Zakon o davkih občanov): annual tax on individuals' buildings, flats, garages and recreational premises, payable whether owner-used or let; base = points-based value, reduced by the value of 160 m² where the owner or close family lived there permanently in the prior year, so a second home or vikend is assessed; 10-year exemption on application for the first owner of a new dwelling; assessed by 31 Mar, amounts valorised yearly; municipal revenue (2026 data, source FURS Brošura o obdavčitvi nepremičnin, Sep 2026 + FURS Sem lastnik ali uporabnik nepremičnine)
- **Davek na nepremičnine** (comprehensive property tax): ZDavNepr (Uradni list RS 101/13, in force 1 Jan 2014) was annulled by the Constitutional Court (U-I-313/13-86, 21 Mar 2014), which restored the previous regime (FURS davek od premoženja page); a successor was last proposed in Dec 2024 (below)

### Davek na nepremičnine reform 2025-2026 (NOT ENACTED)

- 2025 posplošena vrednost reform sets the base
- **Government izhodišča (23 Dec 2024)**: **1.45%** of the GURS posplošena vrednost on residential property, the first home the owner actually lives in fully exempt (MF gov.si, 2024-12-23) — **NOT ENACTED**, it never advanced past the izhodišča
- **Status**: no law; MF closed the consultation on 25 Jan 2025 with 521 comments (MF gov.si, 27 Jan 2025); on 4 Jul 2025 MF said rental-market legal-certainty and rental-contract registration measures must come first and that it would not continue work on property taxation until they are in place (MF gov.si, 4 Jul 2025); no draft law followed — no later MF news release up to 23 Oct 2026 is titled on a property tax (gov.si MF news, read 2026-10-23); the 16th Government (appointed by the Državni zbor on 4 Jun 2026) writes in its 2026-2030 coalition agreement "Namesto dodatnih obdavčitev vseh, ki so varčevali in vlagali v lastna stanovanja in hiše" (instead of additional taxation of all who saved and invested in their own flats and houses) and commits to no new taxes unless offset by relief elsewhere, while keeping the option to adjust or introduce taxes on individual activities (gov.si, read 2026-10-23) — re-verify at MF gov.si before quoting a rate
- **No implementation date**: no enacted law
- The izhodišča went to public consultation with comments due 25 Jan 2025 (MF gov.si, 23 Dec 2024); no draft law followed (see Status)

### Transaction taxes

- **Davek na promet nepremičnin (DPN)**: **2%** of the sale price (2026 data, source FURS DPN page, refreshed 7 Oct 2026). The seller is the taxpayer and stays liable even where the contract shifts payment to the buyer; the seller files within 15 days of signing; without FURS's DPN confirmation the notary cannot certify the signatures and the land register cannot enter the buyer; not charged on a transfer on which DDV was charged (ZDPN-2 Art. 4); revenue goes to the občina where the property lies (2026 data, source FURS Brošura o obdavčitvi nepremičnin, Sep 2026 + FURS Nakup in prodaja nepremičnine)
- **DDV (VAT)**:
  - 9.5% reduced (residential new builds) only for dwellings for permanent living that count as social policy: a flat of up to 120 m² in a multi-dwelling building, or up to 250 m² usable area in a single-dwelling building; otherwise the 22% standard rate (2026 data, source FURS Stopnje DDV, 15th ed., Oct 2026 — ZDDV-1 Annex I pt 11)
  - 22% standard (commercial)
- **Notar fees**: set by the Notarska tarifa per service and value band, not a percentage — certifying a signature on the sale contract €52 for a price of €68,850–150,000, +€11 per further €50,000, capped at €114 (+€16 where the notary also reviews the content); drafting the contract as a notarski zapis €166 for €22,950–114,750, €314 up to €367,200, €576 up to €750,000, then +€23 per further €50,000, capped at €1,140; drafting the land-register petition €42. The notary may raise a fee by 25% for each of foreign law, outside expertise, a foreign language or specialist legal knowledge (at most +100% in all), and by 25% for out-of-hours work done at the client's request; outlays come on top, at actual cost or 2% of the fees where they total up to €523, plus 1% of any excess (2026 data, source Notarska tarifa, Uradni list RS 59/19, 9/21 and 143/21, Arts 3 and 5 and Priloga 2, as published by the Notarska zbornica, read 2026-10-23 — check pisrs.si for later amendments). The land-register entry needs the seller's certified signature, and the notary can also draft the contract (notar-z.si; nasodiscu.si) — get a quote, including whether DDV is added
- **Realtor commission**: no statutory cap. The Constitutional Court's partial decision U-I-205/19, U-I-230/19 of **2 Sep 2025** (published in Uradni list RS 76/2025 on 3 Oct 2025) annulled the 4% cap and the minimum fee in ZNPosr Art. 5(1)–(2) for residential sales and lettings to natural persons, together with Art. 5(4)–(5) insofar as they refer to them and Art. 5(6)–(7); its partial decision of 26 Oct 2023 (Uradni list RS 116/23) had already annulled paras 1–2 for all other deals, and the 2025 ruling followed the CJEU's judgment C-674/23 of 27 Feb 2025 on the Services Directive 2006/123/EC. Para 3 stands (no charging a party that did not engage the agency). The rate is negotiated in the mandate contract — no market-rate figure verified (2025 decision, source Uradni list RS 76/2025, U-I-205/19-51, U-I-230/19-29; iusinfo.si 9 Oct 2025 + pfp.law 3 Dec 2025, secondary)

### Total transaction cost (buyer side)

- **From seller side**: 2% DPN (the contract can shift payment to the buyer, but the seller stays the taxpayer — FURS 2026) + agency commission (negotiated; the statutory cap was annulled by the Constitutional Court decision of 2 Sep 2025); the agency can charge only the party that engaged it (ZNPosr Art. 5(3), as restated in the decision, Uradni list RS 76/2025), and a sale-contract clause to the contrary is void (Art. 5(5), per iusinfo.si — secondary)
- **Buyer side direct** (computed for a €100,000 flat): **€174** if the buyer bears the notary's certification of the seller's signature (€52) and land-register petition (€42), plus the €80 court fee; **€288** with the contract as a notarski zapis (€166 + €42 + €80) — ~0.2–0.3% of the price, before notary outlays, any DDV and any Art. 3 surcharge (e.g. +25% for a foreign language). Notary amounts from the Notarska tarifa (above); court fee from the courts' worked example for a €100,000 flat filed via eSodstvo (tar. št. 91011 ZST-1; the fee can vary with the property's value; nasodiscu.si, read 2026-10-23). Contract drafting by a lawyer or agency and any agency fee under the buyer's own mandate come on top (not verified)

### Capital gains

- Reduced over time (held by individual; 2026 data, source FURS Brošura o obdavčitvi nepremičnin, 8th ed., Sep 2026 + FURS Nakup in prodaja nepremičnine):
  - **0–5 yrs ownership**: 25%
  - **5–10 yrs**: 20%
  - **10–15 yrs**: 15%
  - **>15 yrs**: 0% (exempt — no further brackets)
- **Primary residence**: exempt for a flat, or a house with at most two flats, with its land, where the seller had registered **permanent residence**, owned it and actually lived there for at least the last 3 years before the sale; only the 2% DPN is then due (2026 data, source FURS)
- **Pre-2002 acquisition**: already held >15 years, so exempt under the holding-period rule (computed)
- **Inheritance + gifting** (ZDDD): first heir class exempt — descendants, spouse or unmarried partner, plus zet, snaha, pastorek and a registered same-sex partner; other recipients pay progressive rates by class — 2nd class (parents, siblings and their descendants) 5–14%, 3rd class (grandparents, aunts and uncles and their descendants) 8–17%, all others 12–39%; the base is the comparable market value of the property; a gift can also trigger the donor's capital-gains tax, deferred for gifts to a spouse or child (2026 data, source FURS Brošura o obdavčitvi nepremičnin, Sep 2026)

### Future risk

- **Davek na nepremičnine**: NOT ENACTED — the Dec 2024 1.45% izhodišča never advanced (see above); the 16th Government's 2026-2030 coalition agreement rejects additional taxation of those who saved and invested in their own flats and houses, and new taxes without offsetting relief, while keeping the option to tax individual activities (gov.si, read 2026-10-23)
- **Capital gains and rents**: the same coalition agreement lists simplifying capital-gains taxation and lowering the tax on long-term residential rents, with no rates; no MF news release since the Government took office is titled on either (read 2026-10-23). The rental-income cut from 25% to 15% sits in ZIURS, which is not in force pending the 6 Dec 2026 referendum (see `--rental`); the 25 / 20 / 15 / 0% capital-gains schedule above applies until amended
- **NUSZ stays**: MF stated the proposed tax would NOT have replaced NUSZ (it would have abolished only the ZDO davek od premoženja)
- **Posplošena vrednost** revaluation cycles

---

## Section: `--rental`

### Long-term residential

- Standard income tax on rental: 25% final tax after a 10% flat cost allowance or documented actual maintenance costs (paid as akontacija dohodnine; 2026 data, source FURS); the ZIURS cut to 15% applies only if ZIURS survives the 6 Dec 2026 referendum (see Short-let)
- **Tenant protection moderate** (less strict than DE/AT — curated comparison, wisdom not data: no primary source ranks it; verify termination grounds in the Stanovanjski zakon (SZ-1) at `https://pisrs.si/`)
- Contract length: no reliable national figure — GURS states that ETN records are too incomplete to monitor the rental market, as private landlords do not report leases to FURS or report unrealistic rents (source [GURS letno poročilo 2025](https://www.e-prostor.gov.si/fileadmin/Podrocja/Trg_vrednosti_nep/Trg_nepremicnin/Porocila_o_trgu_nepremicnin/2025/Letno_porocilo_za_leto_2025.pdf), Apr 2026)

### Short-let (kratkoročno oddajanje)

- **ZGos-1** (Zakon o gostinstvu, [Uradni list RS 77/2025](https://www.uradni-list.si/_pdf/2025/Ur/u2025077.pdf); adopted by the DZ 25 Sep 2025, published 7 Oct 2025, in force 22 Oct 2025, **applies since 1 Jan 2026** — register articles from 1 Feb 2026, sobodajalec-registration articles from 1 Jan 2027, Art. 48–49) **is in force**. Day cap: under the ministers' Sklep published in Uradni list RS 546/2026 on 7 May 2026 (PISRS SKLE14364), short-term letting of each dwelling is capped at **60 days per calendar year in 2027 and 2028** in 14 high-risk municipalities — Ankaran, Bled, Bohinj, Bovec, Cerklje na Gorenjskem, Gorje, Izola, Koper, Kranjska Gora, Ljubljana, Piran, Preddvor, Radovljica, Žirovnica — unless the municipality set a 30–270-day limit by a general act adopted by 31 Oct 2026; municipalities not on the list may set a limit of at least 60 days ([gov.si, 8 May 2026](https://www.gov.si/novice/2026-05-08-objavljen-sklep-o-dolocitvi-obcin-z-visokim-tveganjem-negativnih-vplivom-kratkotrajnega-najema)). The enacted law has no 150-day single- or two-unit tier (superseded). Owner consent (ZGos-1 Art. 20, 44): written consent of the dwelling's owner or all its co-owners; in buildings with three or more dwellings, consent of co-owners holding more than three quarters of the co-ownership shares, including the etažni lastniki of every unit whose walls, floors or ceilings adjoin the let dwelling; all co-owners in a two-dwelling building; the consent is valid 3 years and lapses when the let dwelling changes owner; consents obtained under the Stanovanjski zakon stay valid until 31 Dec 2026 or 3 years from when they were obtained, whichever is later. Per dwelling: at most 15 guests and at least 8 m² of usable floor area per guest; no letting in buildings with oskrbovana stanovanja (Art. 20–21). Fines (Art. 36–37): exceeding the day cap or omitting the ID number in ads €1,000–4,500 for a sobodajalec, €1,500–6,000 for an s.p., €2,000–20,000 for a company; letting without registration or a valid ID, or without the required consents, €2,000–12,000, €3,000–20,000 and €5,000–50,000 respectively.
- **ZIURS** (Zakon o interventnih ukrepih za razvoj Slovenije) — adopted by the DZ 11 May 2026, **NOT in force**: on 24 Jul 2026 the Constitutional Court annulled the DZ's 27 May ruling that a referendum was inadmissible; 42,694 signatures were filed (40,000 needed) and on 16 Oct 2026 the DZ called a subsequent legislative referendum (naknadni zakonodajni referendum) for **6 Dec 2026** (press: [mladipodjetnik.si](https://mladipodjetnik.si/novice-in-dogodki/novice/referendum-o-interventnem-zakonu), [Delo](https://www.delo.si/novice/slovenija/referendum-interventni-zakon-december-drzavni-zbor)). Only if ZIURS takes effect would it defer the application of ZGos-1 to the end of 2026 and cut the tax on rental income from 25% to 15% (press: mladipodjetnik.si, updated 22 Oct 2026); the further changes attributed to it in press reports — dropping the 2027 day cap, moving the accommodation-register deadline to 30 Jun 2027, restoring the old by-laws, extending neighbour consents and a 5% rate where the tenant is a young family — are not verified against the adopted ZIURS text (verify at `https://www.dz-rs.si/`). Until then ZGos-1 and the 2027 caps apply; the 31 Oct 2026 municipal deadline falls before the referendum.
- **Ljubljana** is on the 14-municipality list: 60 days per dwelling in 2027–2028 unless the city adopts its own 30–270-day general act by 31 Oct 2026; the press found no adopted Ljubljana act in official sources ([mladipodjetnik.si](https://mladipodjetnik.si/novice-in-dogodki/novice/kratkorocno-oddajanje-stanovanj-omejitve), 6 Oct 2026) — verify the final odlok in the Uradni list or at ljubljana.si
- **Municipal limits adopted by 28 Oct 2026** (apply from 1 Jan 2027; a sobodajalec stays capped at 180 days): Bled 270 days, 30 in multi-dwelling buildings in its Annex 1 areas, sobodajalci 180 ([Uradno glasilo slovenskih občin 57/2026](https://www.lex-localis.info/UradnoGlasiloObcin/VsebinaDokumenta.aspx?SectionID=3a37b9a1-c5b8-4be9-97ed-f7a17157adc0)); Koper 270 ([Uradni list RS 1682/2026](https://pisrs.si/api/uradni-list/objava/u20261682.pdf)); Bovec 270 ([Uradni list RS 1633/2026](https://pisrs.si/api/uradni-list/objava/u20261633.pdf)); press-tier: Izola and Piran 270, Ankaran 180 ([RTV SLO, 14 Oct 2026](https://www.rtvslo.si/lokalne-novice/primorje/ankaran-omejil-kratkorocno-oddajanje-stanovanj-na-180-dni/796886)), Bohinj 30 in multi-dwelling buildings in Stara Fužina and Bohinjska Bistrica and 270 elsewhere, Kranjska Gora 60 / 180 / 270 by zone ([24ur, 23 Oct 2026](https://www.24ur.com/novice/slovenija/tudi-v-bohinju-sprejeli-strog-rezim-oddajanja-stanovanj-v-kratkotrajni-najem.html)). Cerklje na Gorenjskem, Gorje, Ljubljana, Preddvor, Radovljica and Žirovnica: no act located as of 28 Oct 2026 (deadline 31 Oct 2026) — re-check after it
- **Sobodajalec** (a natural person letting short-term): at most **180 days per calendar year** across all its dwellings — beyond that only an s.p. or a company may let (ZGos-1 Art. 5); registered in the AJPES Poslovni register (old rules until 31 Dec 2026, ZGos-1 Art. 24–25 from 1 Jan 2027, existing entries kept — Art. 41, 47–48). ZGos-1 has no municipal licence: municipalities set the day limit (Art. 22) and receive e-Turizem data from AJPES for the turistična taksa
- **EU 2024/1028** (directly applicable): applies since 20 May 2026 (Art. 19); a Member State that runs a registration procedure must set up a single digital entry point (Art. 10(1)) ([Regulation (EU) 2024/1028](http://publications.europa.eu/resource/celex/32024R1028)). ZGos-1 names the implementation of the Regulation as a purpose of the AJPES register nastanitvenih obratov (Art. 26); Slovenia's entry-point designation: verify at gov.si
- **Register nastanitvenih obratov** (AJPES): each let dwelling is entered as one nastanitveni obrat (accommodation establishment), whatever the number of accommodation units in it — online on the AJPES portal or at an AJPES branch — and gets an identification number that must appear in every ad and distance contract (ZGos-1 Art. 21, 23, 27); establishments already registered on 1 Feb 2026 had to complete their data by 30 Jun 2026 or have the ID temporarily revoked (Art. 40); days let are counted from e-Turizem guest-book reports (Art. 27). ZGos-1 has no tourist-board (STO) registration step (superseded: "AVRSK + STO" registration)

### Tax on rental

- 25% on rental income less **10% normirani stroški** (flat cost allowance, since 2022) **or** documented actual maintenance costs (dejanski stroški vzdrževanja); no cost deduction for agricultural / forest land or subletting. The tax is final — rental income is not added to the annual dohodnina base (2026 data, source [FURS](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/dohodnina_dohodek_iz_oddajanja_premozenja_v_najem_in_iz_prenosa_premozenjske_pravice/), page refreshed 13 Feb 2026). ZIURS 15% rate not in force — referendum 6 Dec 2026.
- **Sobodajalec status**: a sobodajalec's tourist-accommodation income is taxed as dohodek iz dejavnosti, not as rental income; VAT identification required above **€60,000** turnover in Slovenia (in-year tolerance to €66,000) (2026 data, source [FURS Brošura za sobodajalce](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Dohodek_iz_dejavnosti/Opis/Brosura_za_sobodajalce_-_fizicne_osebe.doc) + [FURS Davki za začetnike](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Dohodek_iz_dejavnosti/Opis/Davki_za_zacetnike_-_fizicne_osebe_ki_opravljajo_dejavnost.pdf))

---

## Section: `--work=<profession>`

### Sources

- **Zavod RS za zaposlovanje (ZRSZ)**: `https://www.ess.gov.si/`
- **MojeDelo.com**, **Optius.com**
- **LinkedIn SI**

### Self-employment

- **S.P. (samostojni podjetnik)** = sole trader
  - **Pavšalna obdavčitev** (normirani s.p. / flat-rate option, ZPZR + ZPZR-A): allowed while the average revenue of the two preceding years stays at or below **€120,000** (full-time self-employment insurance — at least 75% of the annual full-time hours or 9 continuous months — in both years), **€50,000** (part-time in both years) or **€85,000** (mixed); above that average the s.p. must switch to actual revenue and expenses with full books. Normirani odhodki: full-time 80% of revenue up to €60,000, 0% above (max €48,000); part-time 80% up to €12,500, 40% from €12,500 to €30,000, 0% above. Tax from tax year 2026: full-time 20% on a tax base ≤ €72,000 (= revenue ≤ €120,000) + **35% above**; part-time 20% ≤ €33,000 + 35% above. ZIURS would change the normirani rules from 1 Jan 2026 only if it survives the 6 Dec 2026 referendum. (2026 data, source [FURS Brošura o dohodku iz dejavnosti](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Dohodek_iz_dejavnosti/Opis/Brosura_o_dohodku_iz_dejavnosti.doc) + [gov.si, 16 Oct 2026](https://www.gov.si/novice/2026-10-16-ugotavljanje-davcne-osnove-z-normiranimi-odhodki-v-letu-2026-v-povezavi-z-interventnim-zakonom-ziurs/))
  - Mandatory ZZZS (health) + ZPIZ (pension) contributions
- **D.O.O.** (limited): min **€7,500 capital**, each member's contribution at least €50 (2026-10-23 verified, source [SPOT gov.si](https://spot.gov.si/sl/teme/druzba-z-omejeno-odgovornostjo/))

### Salary benchmarks (2025)

- Average monthly wage at legal persons, by municipality of workplace — SURS publishes averages here, not medians (2025 data, source [SURS SiStat 0701024S](https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/0701024S.px)):
  - Slovenia: €2,536 gross / €1,602 net
  - Ljubljana: €2,895 gross / €1,801 net
  - Maribor: €2,453 gross / €1,551 net; Celje: €2,448 gross / €1,554 net
  - Kranj: €2,520 gross; Koper: €2,543 gross
  - Lowest statistical regions: Primorsko-notranjska €2,206, Savinjska €2,316, Pomurska €2,329 gross ([SURS SiStat 0701023S](https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/0701023S.px))
- **Minimalna plača** (minimum wage): **€1,277.72 gross (2025)** → **€1,481.88 gross (2026)**, valid 1 Jan – 31 Dec 2026; gov.si publishes only the gross amount — net depends on the employee's dohodnina allowances (2026 data, source [gov.si — Minimalna plača](https://www.gov.si/teme/minimalna-placa/))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **ARSO (Agencija RS za okolje)** | `https://www.arso.gov.si/` | Official seismic hazard map, hydrology + flood warnings, climate projections, weather |
| **Atlas okolja** | `https://gis.arso.gov.si/atlasokolja/` | Environmental hazard maps |
| **GeoZS (Geološki zavod Slovenije)** | `https://www.geo-zs.si/` | Geology, **landslides** (pobočni masni premiki, landslide warnings), active-fault + seismic micro-zonation research |
| **URSVS (Uprava RS za varstvo pred sevanji)** | `https://www.gov.si/teme/zmanjsevanje-izpostavljenosti-radonu/` | **Radon** map, higher-radon občine, measurements |
| **URSZR (Uprava RS za zaščito in reševanje)** | `https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/` | Civil protection; national hazard assessments (earthquake v3.0 Jun 2018, flood v3.0 Aug 2026, ice storm v1.1 Sep 2026, wildfire v4.0 Mar 2026): `https://www.gov.si/teme/ocene-ogrozenosti-zaradi-naravnih-in-drugih-nesrec/` |
| **Direkcija RS za vode (DRSV)** | `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-vode/` | Water management |
| **eVode + Atlas voda (DRSV)** | `http://www.evode.gov.si/` · `https://geohub.gov.si/atlasvoda` | Flood hazard maps (Integralna karta poplavne nevarnosti, data updated 21 Aug 2026), water cadastre |

### Specific risks

- **Poplava (floods)**: URSZR puts six of its regions in the top flood class 5 — Gorenjska, Koroška, Obalna, Ljubljanska (the most exposed; largest OPVP on the Ljubljansko barje), Zahodnoštajerska, Zasavska — and 50 občine in class 5, home to 53.1% of the population (municipality-level classes, not parcel-level); flood types: torrential, lowland, karst-polje (settlements on polje edges), sea and urban; the 104 areas of significant flood risk (OPVP) set in 2025 (86 in 2019) lie in the Sava, Sora, Ljubljanica, Savinja, Krka, Kolpa, Drava, Mura, Idrijca and Vipava basins, among others, and on the coast at Koper, Izola and Piran; **August 2023 floods** (peak 4 Aug) — the worst in Slovenia's known history: 7 dead, 183 občine hit, damage just under €3 bn (official methodology) / > €5 bn (PDNA); the Predhodna ocena poplavne ogroženosti (2024) behind the 2025 OPVP set includes an analysis of the event; **ice storm (žled) end Jan–early Feb 2014** (the largest ice storm in RS to date; none as severe and extensive is known for the period after 1890) + floods Sep and Oct 2014; check the parcel on the Integralna karta poplavne nevarnosti (eVode / Atlas voda) (2026 data, source URSZR Ocena ogroženosti zaradi poplav v3.0, 24 Aug 2026 + Ocena ogroženosti zaradi žleda v1.1, 15 Sep 2026)
- **Potresna ogroženost (seismic)**: Slovenia lies in an area more exposed to earthquakes than most European countries (gov.si, URSZR Napotki prebivalcem ob potresu); URSZR rates it a country of moderate seismic hazard where relatively shallow foci can make effects fairly large (source URSZR Ocena ogroženosti RS zaradi potresov v3.0, Jun 2018)
  - Posočje (Soča valley): **12 Apr 1998 Krn–Lepena M 5.7** (VII–VIII EMS, > 4,000 buildings damaged) + **12 Jul 2004 Krn–Lepena ML 4.9** (VI–VII EMS, damage mainly around Bovec / Čezsoča) (source URSZR, 2018)
  - **Ljubljana 14 Apr 1895 ML 6.1** (VIII–IX EMS; ~10% of the city's ~1,400 buildings damaged); strongest recorded on Slovenian territory: **Idrija 26 Mar 1511, est. M 6.8** (source URSZR, 2018)
  - **Official design map**: ARSO *Potresna nevarnost Slovenije – projektni pospešek tal* (2021) — PGA on rock (EC8 ground type A), 475-year return period; valid since 1 May 2022 and the only official map (sole annex to the EC8 National Annex) since 1 May 2024, replacing Lapajne et al. 2001; 10 classes of 0.025 g from **0.100 g to 0.325 g**, not numbered zones; places on a class boundary take the higher value
  - **0.325 g** (highest): the Italian border west of Bovec; **0.300 g**: around Idrija and in SE Slovenia around Brežice; **0.275 g**: Ljubljana and surroundings; values are higher than on the 2001 map across most of Slovenia (up to +0.125 g in Bela krajina), comparable around Ljubljana / Kranj / Kamnik and in the SW, slightly lower only around Ptuj
  - **0.100 g** (lowest): NE Slovenia (Maribor, Ptuj, Prekmurje) and the Izola–Piran coast, with Koper town on the 0.100/0.125 class line (2021 map, source ARSO Tolmač karte potresne nevarnosti 2021, updated 29 Jul 2026, + map legend: `https://potresi.arso.gov.si/doc/dokumenti/potresna_nevarnost/`); read the class at the exact parcel in the ARSO pregledovalnik, not the municipality
- **Plaz / zemeljski plaz** (landslides): a quarter of Slovenia's territory is highly exposed to slope mass movements, with ~18% of the population living there (GeoZS rough estimate, leaflet Plazenje tal — no printed date, PDF file created 30 Aug 2017 — `https://www.geo-zs.si/wp-content/uploads/2025/03/Plazenje_tal_new.pdf`, linked from `https://www.geo-zs.si/priporocila-lastnikom-objektov-na-nestabilnih-tleh/`, checked 2026-10-23) — rates/figures may have changed since
  - Landslides are most likely on soft rock (polhribine): Slovenske gorice, Haloze, Goričko, Lendavske gorice, lower Kozjansko, small areas around Novo mesto and in Bela krajina, Tunjice, the northern rim of the Brežice–Krško basin; less so on medium-hard rock (lower Pohorje, parts of the Karavanke, Koprsko primorje, Brkine, the Vipava valley rim, Goriška brda and the Cerkno–Idrija, Polhov Gradec, Škofja Loka and Posavje hills, among others); karst, hard-rock areas and the big gravel plains (Mura, Drava, Savinja, Ljubljana and Krško basins, Ljubljansko barje) are little exposed; rockfalls (podori) are mostly confined to the Julian Alps, Karavanke and Kamnik Alps plus narrower zones elsewhere (2018 data, source URSZR Ocena ogroženosti zaradi potresov v3.0, citing the GeoZS 2012 landslide probability map) — rates/figures may have changed since; regional map only — commission a geotechnical survey for a slope parcel
  - **Stože (Stovže) debris flow, night of 17 Nov 2000**, Log pod Mangartom: 7 residents dead, 6 residential and farm buildings destroyed, direct + indirect damage estimated at SIT 7.6 bn / €31.7 m (source gov.si, Ministrstvo za okolje in prostor, 17 Nov 2020); a similar flow had hit the site at least once before (URSZR, 2018)
- **Suša + požar** (drought + wildfire): the submediterranean SW — 19 občine incl. Koper, Izola, Piran, Sežana, Divača, Komen, Nova Gorica, Ajdovščina, Postojna, Ilirska Bistrica (14.7% of the territory) — is the most fire-prone area; on the Kras the limestone holds little water, so drought conditions set in earlier and more often than elsewhere; largest fire on record: 15 Jul 2022 on the western Kras, 3,707 ha burned on Slovenian territory; URSZR expects fire numbers and extent to keep rising at first, the rise possibly slowing somewhat after 2040 and slowing further or stopping after 2070 as precipitation increases, so most of the rise in fire numbers is likely to come by 2040; the largest increase is most likely in the SW, which stays the most exposed (2026 data, source URSZR Ocena ogroženosti zaradi požarov v naravnem okolju in na prostem v4.0, 12 Mar 2026); no national drought hazard assessment is published on the URSZR assessments page
- **Karst hazards**: karst-polje floods reach settlements on the polje edges after long rain, snowmelt or ice storms (URSZR flood v3.0, 2026); karst areas hold 42% of Slovenia's protected water sources and 53% of its water-protection zones (2013/2017 data, source GeoZS Karta površinske razširjenosti in stopnje zakraselosti kraških območij v Sloveniji, map 2013 / tolmač 2017) — rates/figures may have changed since; check whether the parcel lies in a vodovarstveno območje before planning a greznica / MKČN; cave / collapse-sinkhole risk: no national primary source found — curated wisdom, not data; commission a geotechnical survey on karst plots
- **Radon**: URSVS lists 24 higher-radon občine — Bloke, Cerknica, Črnomelj, Divača, Dobrepolje, Dolenjske Toplice, Hrpelje - Kozina, Idrija, Ig, Ivančna Gorica, Kočevje, Komen, Logatec, Loška dolina, Loški Potok, Miren - Kostanjevica, Pivka, Postojna, Ribnica, Semič, Sežana, Sodražica, Vrhnika, Žužemberk — plus 27 občine under additional measurement; reference level **300 Bq/m³** (source URSVS, gov.si Zmanjševanje izpostavljenosti radonu, checked 2026-10-23); for new builds, interventions in existing buildings and anti-radon remediation of buildings with living or working rooms (not simple or non-demanding objects), the Pravilnik o zahtevah za novogradnje, posege v obstoječe stavbe in sanacijo obstoječih stavb zaradi varovanja zdravja ljudi pred škodljivimi učinki radona requires design, construction and maintenance that keep radon as low as possible and below the reference level (Ur. l. RS 14/22, 55/23 – popr., 76/23, Art. 3 and 5); a build that fully applies TSG-1-007:2023 is presumed to comply (Art. 18; URSVS)
  - **Radonski zemljevid Slovenije** (URSVS): municipality-level only — says nothing about a given parcel; measure in the dwelling (only measurements by URSVS-authorised providers count officially)
- **Klimatske spremembe**: mean temperature **+1.1 to +2.3 °C (RCP4.5) / +1.6 to +2.8 °C (RCP8.5) in 2041–2070** vs 1981–2010 (2019 data, source ARSO Ocena podnebnih sprememb v Sloveniji do konca 21. stoletja, dopolnjen povzetek Dec 2019 — still ARSO's current projection set, figures re-checked 2026-10-23)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1948** | No national seismic design rules (only Ljubljana's 1896 building code after the 1895 quake) |
| **1948–1963** | 1948 temporary rules (Ur. l. SFRJ 61/48) heavily underestimated seismic loads; buildings as a rule carried vertical loads only — treat as non-seismic, critical in the high-PGA classes |
| **1964–1981** | First serious seismic design rules: Odredba 1963 (Ur. l. SRS 18/63), Yugoslav Pravilnik 1964 (Ur. l. SFRJ 39/64) |
| **1982–2007** | 1981 Pravilnik o tehničnih normativih za graditev objektov visoke gradnje na seizmičnih področjih (Ur. l. SFRJ 31/81 + amendments) — higher seismic resistance |
| **2008+ (EC8)** | Eurocode 8 (SIST EN 1998); old rules allowed until 1 Jan 2008; design map Lapajne et al. 2001 until the 2021 ARSO map took over (valid from 1 May 2022, sole official map from 1 May 2024) (source URSZR Ocena ogroženosti zaradi potresov v3.0, 2018; ARSO Tolmač karte potresne nevarnosti 2021) |
| **Asbestos** | used intensively across Europe 1945–1990, all use banned since 1 Jan 2005 (gov.si Azbest) — pre-1990 builds most likely, pre-2005 possible |
| **PCB** | buildings built or reconstructed **1950–1980**: before reconstructing or demolishing one, the investor must have an inventory (popis) of built-in PCB materials made, with a kg estimate per material — joint sealants between concrete elements, window / glazing and sanitary-joint sealants, wall and ceiling paints, adhesives, ceiling boards with PCB plasticisers or flame retardants, plastic building elements, cable insulation; > 50 kg adds PCB separation and handover steps to the construction-waste plan, > 1,000 kg requires a decontamination plan and decontamination before works (Uredba o odstranjevanju PCB in PCT, Ur. l. RS 34/08, 9/09, 44/22 – ZVO-2, Art. 17.a–17.b, as quoted in the MOP forms Popis vgrajenih gradbenih materialov, ki vsebujejo PCB and Elaborat dekontaminacije stavbe, `https://www.gov.si/assets/ministrstva/MOP/Okolje/Odpadki/ob_popis_gradbenih_materialov.xlsx`, checked 2026-10-23) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetska izkaznica (EI)** | Energy certificate (ZURE, Ur. l. RS 158/20): hand over before signing a sale or a lease > 1 year; EI indicators must appear in ads | 10 years (source energetika-portal.si, checked 2026-10-23) |
| **Penalty for missing EI** | **€300** fine on the owner (no EI before the contract, or EI indicators missing from ads — ZURE Art. 31(2), (9)); €100 on the responsible person of a legal entity | n/a |
| **Zemljiškoknjižni izpisek** | Land register extract | At sale |
| **Posplošena vrednost (GURS)** | Not a sale document: GURS mailed owners a zbirno potrdilo from 26 May to 1 Jul 2025 (gov.si GURS, 1 Jul 2025); values reflect the market at 1 Jan 2025 and are recalculated whenever property data change — print the current value from EV_JV (source GURS e-prostor, checked 2026-10-23) | Until data change |
| **Pogodba** + **notarska overitev** | Contract + notary verification | At sale |

### Climate change projections

- Mean temperature vs 1981–2010: **+1.1 to +2.3 °C (RCP4.5) / +1.6 to +2.8 °C (RCP8.5) in 2041–2070**; **+1.5 to +2.6 °C / +3.0 to +5.1 °C in 2071–2100** (2019 data, source ARSO OPS21 dopolnjen povzetek, Dec 2019, `https://meteo.arso.gov.si/met/sl/climate/change/` — still ARSO's current projection set, figures re-checked 2026-10-23)
- Precipitation: the winter increase is the clearest signal (eastern SI up to +40% in winter by mid-century under RCP8.5); summer direction uncertain (RCP4.5 leans drier to mid-century); annual totals ~+10% by 2100 under RCP4.5 except the Julian Alps (ARSO OPS21, 2019)
- More intense and more frequent extreme precipitation (August 2023 type) (ARSO OPS21, 2019)
- Water balance: reference evapotranspiration ~+7% (RCP4.5) / ~+12% (RCP8.5) and annual groundwater recharge ~+20% (RCP4.5) / ~+10% (RCP8.5) by 2100 (baselines 1981/1982–2010); mean annual flood peaks +20–30% on average, 20–40% at almost all gauging stations under RCP8.5 by century end (ARSO OPS21, 2019) — no national karst water-supply projection found; on the Kras drought conditions set in earlier and more often than elsewhere (URSZR wildfire v4.0, Mar 2026)
- Adriatic coast: mean annual sea level at the Koper tide gauge rose ~10 cm between the 1961–1970 and 2014–2023 decadal means — no significant trend 1961–1995, +3.5 mm/yr on average since 1995; ARSO cites an estimated Mediterranean rise of 40–60 cm by the end of the 21st century and expects a 10-fold increase in the frequency of the 1-in-100-year extreme sea level in the northern Adriatic between 2040 and 2075 (1961–2023 data, source ARSO Kazalci okolja MR02 Višina morja, last updated 17 Jul 2025, archived 2026-03-12, `https://kazalci.arso.gov.si/sl/content/visina-morja-6`) — rates/figures may have changed since; sea floods come from high tide + low air pressure + jugo wind, and Obalna is one of URSZR's six class-5 flood regions (URSZR flood v3.0, 2026)

---

## Section: `--mains`

### Sources

- **Komunalne službe** per občina (municipal services)
- **JP VOKA SNAGA** (Ljubljana water + wastewater operator, Javni holding Ljubljana; formerly Vodovod-Kanalizacija Ljubljana): `https://www.vokasnaga.si/` — drinking-water supply and wastewater, incl. public reporting under Uredba o pitni vodi (Ur. l. RS, št. 61/23) (2026-10-23 verified)
- **Mariborski vodovod** (javno podjetje, drinking water): `https://www.mb-vodovod.si/` + regional public utilities
- Most občine have own komunala
- Nationally 70.5% of the population is on a public sewer (urban collecting system) and 28.6% on independent treatment (greznica / MKČN) — only 2.6% of the population has independent treatment of at least secondary level, and 4.4% has wastewater trucked from storage tanks to a treatment plant (2024 data, source Eurostat env_ww_con, `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_ww_con?geo=SI`); SURS dwelling statistics count more: 899,446 of 2,036,638 residents (44.2%) lived in dwellings without a public-sewer connection (2021 data, source SURS SiStat 0861240S, `https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/0861240S.px`) — rates/figures may have changed since; the two primary sources differ and neither explains the gap; the SURS series is used for the area shares below because it is the only one published per občina; check the parcel with the občina komunala

### Verification

- Cities: public sewer not universal — share of residents in dwellings without a public-sewer connection, whole municipality incl. its rural settlements: Ljubljana 12.3%, Maribor 11.9%, Velenje 16.4%, Celje 23.9%, Novo mesto 30.2%, Koper 32.2%, Kranj 34.4%, Nova Gorica 38.9% (computed: residents without connection ÷ all residents in dwellings, 2021 data, source SURS SiStat 0861140S, `https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/0861140S.px`) — rates/figures may have changed since
- **Karst** areas — share of residents in dwellings without a public-sewer connection, whole municipality: Kras — Komen 95.1%, Hrpelje - Kozina 76.0%, Sežana 62.7%, Divača 62.3%; Notranjska — Bloke 86.0%, Pivka 67.6%, Loška dolina 64.3%, Ilirska Bistrica 59.4%, Cerknica 57.8%, Postojna 40.7%; Bela krajina — Semič 79.7%, Črnomelj 63.0%, Metlika 54.6%; Pohorje občine are similar (Podvelka 79.7%, Oplotnica 74.7%, Ribnica na Pohorju 67.9%, Zreče 59.6%) (computed as above, 2021 data, source SURS SiStat 0861140S) — rates/figures may have changed since; municipality level only — says nothing about a given parcel
- **Mala komunalna čistilna naprava (MKČN, < 50 PE)**: the owner must provide individual treatment outside agglomerations (public sewer is the občina's duty inside them); an MKČN needs first measurements (prve meritve) reported to the komunala, and sludge / greznica emptying is a mandatory public-service job (source gov.si Odvajanje in čiščenje komunalne in padavinske odpadne vode, checked 2026-10-23)

### Costs

| Scenario | est. cost (€) — unsourced curated ranges (2026-04 research); get komunala + contractor quotes |
|---|---:|
| Priklop na javno kanalizacijo | 4,000–10,000 |
| MKČN namestitev | 5,000–12,000 |
| Greznica reorganizacija | 3,000–8,000 |
| Vodovodni priključek | 1,500–4,500 |

est. — no primary source found that publishes connection-works prices: they depend on trench length, terrain / rock and the contractor, and the občina's komunalni prispevek may apply on top (curated wisdom — check the občina's odlok). Calibration for the utility's own fees: in Ljubljana JP VOKA SNAGA charges €76.49 to inspect a stand-alone water or sewer connection, €323.91 (water) / €393.82 (sewer) for a house-connection design and €262.42 for the cadastre survey, incl. 22% DDV — €662.82 (water) / €732.73 (sewer) if all three are ordered for one stand-alone connection (computed: 76.49 + 323.91 + 262.42; 76.49 + 393.82 + 262.42); built-in material is billed on top at supplier price + 5%, and the list does not price the connection works themselves (2026 data, source JP VOKA SNAGA Cenik blaga in storitev, ki niso del izvajanja GJS, valid from 1 Jul 2026, `https://www.vokasnaga.si/pitna-odpadna-voda/ceniki-2/ceniki/`)

---

## Cost benchmarks (SI 2026)

| Work | Cost (€; DPN, notar and court-fee rows from FURS, the Notarska tarifa and the courts' portal; construction and service rows are curated est. with no Slovenian price source or index behind them — wisdom, not data; get at least two quotes) |
|---|---:|
| Energetska izkaznica | est. 150–400 |
| Notar | tariff bands, not a percentage: signature certification on the contract €52 at €68,850–150,000 (+€11 per further €50,000, max €114); contract as notarski zapis €166 at €22,950–114,750, €314 to €367,200, €576 to €750,000 (max €1,140); land-register petition €42; plus outlays, any DDV and any Art. 3 surcharge (+25% per ground such as a foreign language, max +100%) (2026 data, source Notarska tarifa 59/19, 9/21, 143/21 via notar-z.si, read 2026-10-23) |
| DPN (transfer tax) | 2% of price; seller is the taxpayer, the contract can shift payment to the buyer (FURS DPN page, refreshed 7 Oct 2026) |
| Realtor (4% cap annulled by the Constitutional Court decision of 2 Sep 2025, Uradni list RS 76/2025) | negotiated; no market-rate figure verified |
| Zemljiška knjiga — sodna taksa | €80 for a €100,000 flat filed via eSodstvo (tar. št. 91011 ZST-1; can vary with the property's value), +€32 if the petition is dictated on the court record (nasodiscu.si worked example, read 2026-10-23) |
| **Total transaction cost (buyer)** | **computed for a €100,000 flat: €174–€288 (~0.2–0.3%)** from the notar and court-fee rows, or **€2,174–€2,288 (~2.2–2.3%)** where the buyer takes over the €2,000 DPN; before notary outlays, any DDV and any Art. 3 surcharge, plus contract drafting by a lawyer or agency and any agency fee under the buyer's own mandate (not verified) |
| Septik to mains | est. 4,000–10,000 (same uncalibrated range as the `--mains` cost table; get the komunala's quote) |
| Roof (terracotta tile, 200 m²) | est. 15,000–25,000 |
| Energy retrofit (Class C → A) | est. 30,000–80,000 |
| Antiseismic retrofit (small house) | est. 25,000–60,000 |
| Asbestos removal | est. 1,500–8,000 |

## Active fiscal incentives (2025-2026)

- **Eko sklad** (ekosklad.si): grant and/or loan for heat pumps, façade, roof and floor insulation, windows and external joinery, biomass boilers, heat-recovery ventilation, solar heating, self-supply solar plants and whole-building renovation (current incentive list, read 2026-10-23)
- **Eko sklad loans only** (no grant): small wastewater plants (MČN), connection to the public sewer or water mains, asbestos-roof replacement (same list)
- **Stanovanjski sklad RS**: no open loan call for individual buyers on its javni pozivi page (read 2026-10-23); its current calls cover public rental housing, including Javni najem, a standing call for offers from dwelling owners (Razpis zbiranja ponudb najemodajalcev) — verify at ssrs.si before citing any buyer loan
- **Subvencije za mlade** (young families) per občina
- **MČN subsidies at občina level**: not verified — ask the občina (the Eko sklad MČN offer is a loan)

## Common listing platforms

- **Nepremicnine.net** — the main portal by reputation (wisdom, not data; no traffic or listing-share figures verified)
- **Bolha.com** — secondary
- **Slonep.net** — activity not verified (site could not be read for verification on 2026-10-23)
- **Salomon.si** ❌ DEPRECATED — dead on 2026-10-23 (connection refused); verify listings on Nepremicnine.net / Bolha.com
- Agencies: RE/MAX (re-max.si, 17 offices in its office sitemap, read 2026-10-23), DODOMA (dodoma.si, Maribor); Stoja Trade not verified (site could not be read for verification on 2026-10-23)

## Caveats unique to SI

- **Among the higher seismic-hazard countries in Central Europe** — no numbered zones: ARSO's 2021 design ground-acceleration map (475-year return period, rock), the only official map for earthquake-resistant design since 1 May 2024, uses 0.025 g classes from 0.1 g to 0.325 g — 0.325 g on the Italian border west of Bovec, 0.3 g around Idrija and Brežice, 0.275 g for Ljubljana and its surroundings; read the class at the exact parcel (2021 data, source [ARSO Potresna nevarnost](https://potresi.arso.gov.si/doc/dokumenti/potresna_nevarnost/) — Tolmač karte potresne nevarnosti 2021, updated 29 Jul 2026); pre-1963 builds dangerous
- **Posplošena vrednost reform 2025** — new mass-appraised values effective 13 May 2025
- **Davek na nepremičnine NOT ENACTED** — the Dec 2024 1.45% izhodišča never advanced; NUSZ + ZDO davek od premoženja remain payable
- **EU 2007 currency** — no FX risk (vs CZ/PL/HU)
- **Adriatic coast (Koper-Piran)**: tourist premium + sea-level rise concern
- **Karst** specific construction issues — caves, sinkholes
- **Triglav National Park** strict construction limits
- **Mali Krasovi** (small karst formations) widespread; cave/sinkhole risk
- **Yugoslav-era apartment buildings** (1960s-1980s): variable seismic compliance
- **DPN paid by seller** — the seller stays the taxpayer even where the contract shifts payment to the buyer (FURS 2026)
- **No statutory realtor-fee cap since 2 Sep 2025**: the Constitutional Court (U-I-205/19, U-I-230/19) annulled the 4% cap in ZNPosr Art. 5; only the bar on charging a party that did not engage the agency remains (iusinfo.si, pfp.law — secondary)
- **Foreign buyers**: EU, OECD and EFTA nationals and legal persons buy freely; nationals of EU candidate countries (North Macedonia, Serbia, Montenegro, Albania, Ukraine, Moldova, Bosnia and Herzegovina, Georgia) need a positive reciprocity decision from the Ministry of Justice (upravna taksa €22.60); nationals of all other states, including China and Russia, cannot acquire real estate, or only by inheritance where reciprocity exists — Constitution Art. 68 (source gov.si Ministrstvo za pravosodje, page last changed 13 Nov 2024, read 2026-10-23)
- **Italian + Hungarian linguistic minorities** along borders — bilingual signage + listings
- **Bovec earthquakes 1998 + 2004** as recent reference events
- **August 2023 catastrophic flood** as recent reform driver
- **Brez davka na nepremičnine**: the 1.45% proposal was NOT enacted and would not have replaced NUSZ — NUSZ (municipal) + the ZDO davek od premoženja remain the charges
- **Etažna lastnina**: rezervni sklad (reserve fund) requirements

## Reddit / forum sources

- **r/Slovenia** (active, English-friendly)
- **Slo-Tech.com** forums
- **Bolha.com** discussions
- **MojCG.com** ❌ DEPRECATED — dead on 2026-10-23 (parked domain); verify with r/Slovenia / Slo-Tech
- **Slovenia Times** (English news)
- **Total Slovenia News** (English)

## Verification authorities

| Authority | When to call |
|---|---|
| **GURS** | Cadastre, posplošena vrednost |
| **Občina** | NUSZ, zoning (prostorski izvedbeni akt), public sewer |
| **Upravna enota** | Gradbeno dovoljenje — e-uprava names občina, upravna enota and mnenjedajalci as the bodies to consult (e-uprava, page updated 9 Jul 2026) |
| **e-Sodstvo Zemljiška knjiga** (okrajna sodišča) | Title verification — portal `https://esodisce.si/` |
| **FURS** | Tax calculations, capital gains |
| **ARSO** | Seismic hazard map, climate projections, hydrology / weather |
| **GeoZS** | Geology, landslides, active faults |
| **URSVS** | Radon |
| **DRSV / eVode** | Flood hazard maps, water cadastre |
| **Notar** | Sale process |

## Source URL templates

| Source | URL pattern |
|---|---|
| GURS Javni vpogled | `https://ipi.eprostor.gov.si/jv/` |
| GURS Vrednotenje | `https://vrednotenje.gov.si/EV_JV/` |
| Zemljiška knjiga (e-Sodstvo) | `https://esodisce.si/` (old evlozisce.sodisce.si URLs 301-redirect here; updated 2026-10-23) |
| OPSI open data | `https://podatki.gov.si/` |
| ARSO Atlas okolja | `https://gis.arso.gov.si/atlasokolja/` |
| Nepremicnine.net | `https://www.nepremicnine.net/` |
| FURS (tax) | `https://www.fu.gov.si/` |
| GeoZS | `https://www.geo-zs.si/` |
| DRSI traffic | `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-infrastrukturo/` |
| URSZR (civil protection) | `https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/` |
| URSZR hazard assessments | `https://www.gov.si/teme/ocene-ogrozenosti-zaradi-naravnih-in-drugih-nesrec/` |
| eVode flood maps | `http://www.evode.gov.si/` |
| URSVS radon | `https://www.gov.si/teme/zmanjsevanje-izpostavljenosti-radonu/` |
| DRSI PLDP open data | `https://podatki.gov.si/dataset/pldp-karte-prometnih-obremenitev` |
| ARSO climate projections | `https://meteo.arso.gov.si/met/sl/climate/change/` |

## Status

✅ **Fully populated**; fast-changing sections re-verified as of 2026-10-23, figures with no current primary source labelled est., curated wisdom or verify-at, and older-source figures marked 'may have changed since' (initial population 2026-04-25; Ljubljana water / wastewater operator re-identified as JP VOKA SNAGA 2026-09-18; the `--mains` connection-cost ranges stay est.). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Short-let block (ZGos-1 day caps, ZIURS referendum) re-checked 2026-10-28 against the Uradni list (Sklep 546/2026, OdZIURS 1692/2026, Bovec and Koper odloki), the Bled odlok and national press (previous check 2026-10-23); see shared/regulatory-watch.md.
**Coverage check**: pricing, traffic, tax (with the not-enacted 1.45% proposal note), rental, work, risks (incl. ARSO seismic design-acceleration map + August 2023 flood reference), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for `--work` (normirani s.p. rules from the FURS Brošura o dohodku iz dejavnosti and gov.si of 16 Oct 2026; d.o.o. €7,500 on SPOT; SURS SiStat 2025 average wages; 2026 minimum wage on gov.si). HIGH for the H1 2026 GURS ETN price table (GURS polletno poročilo, Oct 2026), the 13 May 2025 posplošena vrednost dates (gov.si GURS releases), the ~€297 bn posplošena vrednost total and the 2019-2024 / 2020-2025 transacted-price growth (GURS letno poročilo 2024 and 2025); for the DPN, capital-gains, primary-residence, DDV and NUSZ rules (FURS brochure Sep 2026, DPN page 7 Oct 2026, Stopnje DDV Oct 2026), the notary tariff bands (Notarska tarifa), the €80 land-register court-fee example (nasodiscu.si), the computed NUSZ example (MOL odlok) and the computed buyer-side examples (Notarska tarifa plus that court fee); for the realtor-cap annulment (Constitutional Court decision of 2 Sep 2025, Uradni list RS 76/2025) and the NOT-ENACTED status of the davek na nepremičnine 1.45% izhodišča (MF releases of 27 Jan and 4 Jul 2025, MF news titles to 23 Oct 2026, 2026-2030 coalition agreement; re-verify at MF gov.si before output); for the 25% rental-income tax and the €60,000 sobodajalec VAT threshold (FURS); for ZGos-1 — gazette dates, owner-consent rule, 180-day sobodajalec cap and AJPES register (Uradni list RS 77/2025) — and the 2027-2028 day-cap mechanism and municipality list (gov.si, 8 May 2026); for the EU 2024/1028 dates (Regulation text); for the flood, ice-storm, wildfire, radon and energetska izkaznica facts in `--risks` (URSZR assessments of Mar, Aug and Sep 2026, URSVS, energetika-portal.si), the seismic design map (ARSO Tolmač karte potresne nevarnosti 2021, updated 29 Jul 2026), the Stože 2000 toll (gov.si MOP) and the PCB era (PCB Uredba via MOP forms); and for the mains operators and MKČN duties (VOKA SNAGA, Mariborski vodovod, gov.si). MEDIUM for the €298 bn / +8% launch figures (GURS director quoted by RTV SLO, press; the +8% is measured against the October 2024 trial calculation); the ZIURS not-in-force status, 6 Dec 2026 referendum, 15% rate and ZGos-1 deferral (press-tier); the RE/MAX and DODOMA entries (agency-published); the rest of `--risks` — seismic history and build-era rules (URSZR 2018 earthquake assessment), landslides (GeoZS leaflet, PDF created 2017; URSZR 2018 citing the GeoZS 2012 map), karst (GeoZS map 2013 / tolmač 2017), climate (ARSO OPS21, 2019 data) and sea level (ARSO MR02, live page unreachable, read via a 2026-03-12 archive) — and the `--mains` sewer-connection shares (Eurostat 2024 and SURS SiStat 2021, which disagree): re-verified on 2026-10-23, kept MEDIUM because these sources date from 2012–2019 or are read through an archive and the two sewer shares disagree; and `--traffic` (DRSI PLDP 2025 figures; the verdict bands are curated thresholds). LOW for the Nepremicnine.net, Slonep.net and Stoja Trade claims (wisdom or not verified; the sites could not be read for verification — check them directly); the further ZIURS changes reported in the press (not checked against the adopted text); tenant protection and contract length (curated wisdom, no primary figure); the 'Caveats unique to SI' lines on Mali Krasovi (dropped from `--risks` as unsupported) and the coastal sea-level-rise concern (not yet linked to the ARSO MR02 figures in `--risks`); and every est. cost row (mains connections, energetska izkaznica, construction).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Normirani s.p. rules rebuilt from the FURS Brošura o dohodku iz dejavnosti + gov.si 16 Oct 2026 (the €60k / €30k exit rule was wrong); d.o.o. €7,500 on SPOT; SURS SiStat 2025 averages replace the unsourced median ranges; minimum wage gross on gov.si, uncalibrated net removed |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Roles corrected: seismic map ARSO, radon URSVS, GeoZS geology / landslides, land register at the okrajna sodišča (esodisce.si); Upravna enota, URSVS and DRSV / eVode rows added |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | Liveness and redirects checked: e-Sodstvo 301 → esodisce.si (replaced); nepremicnine.net answers 403 to scripts (kept); five rows added for URLs cited in the new risk / traffic text |
| `--price` | 2026-10-23 | 2026-10-23 gap-closing pass | H1 2026 GURS table re-read in the polletno poročilo, every median and percentile unchanged; posplošena vrednost total re-sourced to the GURS 2025 report (~€297 bn) and price growth to GURS ETN indices (2019-2024, 2020-2025); €298 bn / +8% kept as a press quote, the +8% baseline corrected to the Oct 2024 trial calculation (not the 2020 values); ETN access corrected; listing and agency claims confirmed or labelled |
| `--rental` | 2026-10-23 | 2026-10-23 gap-closing pass | ZGos-1 read in Uradni list RS 77/2025: dates and day-cap rules confirmed, owner-consent threshold corrected, 180-day sobodajalec cap and AJPES register added, per-občina licensing and AVRSK + STO removed; EU 2024/1028 dates read in the Regulation; ZIURS press-tier, unverified sub-measures labelled; tenant protection and contract length relabelled |
| `--tax` | 2026-10-23 | 2026-10-23 gap-closing pass | FURS brochure, DPN, davek od premoženja and DDV pages re-read, rules unchanged; notary percentage and buyer-side total replaced by Notarska tarifa bands, the nasodiscu.si court-fee example and a computed €100,000 example; NUSZ shown as the FURS mechanism plus a computed Ljubljana example; realtor-cap ruling read in Uradni list RS 76/2025; NOT-ENACTED status re-checked against MF releases and the 2026-2030 coalition agreement |
| `--risks` | 2026-10-23 | 2026-10-23 second gap-closing pass | URSZR flood, earthquake, ice-storm and wildfire assessments, ARSO Tolmač 2021, GeoZS, URSVS, gov.si (Stože, Azbest), the PCB forms, OPS21, ZURE and MR02 (archived 2026-03-12) re-read: 24 facts confirmed; ice-storm superlative, wildfire trend, radon new-build scope and GURS mailing dates corrected; cave / sinkhole risk stays curated wisdom |
| `--mains` | 2026-10-23 | 2026-10-23 second gap-closing pass | Eurostat env_ww_con 2024 and SURS SiStat 0861240S / 0861140S (2021) re-read, all 25 per-občina shares recomputed with no mismatch; VOKA SNAGA fees (list valid from 1 Jul 2026) re-read and per-connection totals computed; connection-cost rows stay est.; 37 facts confirmed |
| Cost benchmarks (SI 2026) | 2026-10-23 | 2026-10-23 gap-closing pass | Notar, court-fee and total rows rebuilt from the Notarska tarifa and the nasodiscu.si example (computed for a €100,000 flat); DPN re-confirmed (FURS, 7 Oct 2026); construction rows est., labelled curated wisdom |
| Common listing platforms | 2026-10-23 | 2026-10-23 gap-closing pass | RE/MAX (re-max.si) and DODOMA confirmed; the Nepremicnine.net lead labelled wisdom; Slonep.net and Stoja Trade not verified (sites answer 403) |

## Extension TODOs

- [ ] Per-občina NUSZ rates from odlok
- [ ] Posplošena vrednost extraction patterns (post-May 2025)
- [ ] Seismic design-acceleration class overlay per parcela (ARSO 2021 map)
- [ ] Karst hazard detection
- [ ] Triglav NP construction limits
- [ ] Coastal sea-level rise (Koper-Piran-Portorož)
- [ ] Italian-language listings (border zones)
- [ ] August 2023 flood-affected zones
- [ ] Davek na nepremičnine final rate tracking
- [ ] Etažna lastnina rezervni sklad health

## Update history

- **2026-04-25** — Initial population
- **2026-05-27** — Tier-1 corrections: capital-gains holding-period bands (25 / 20 / 15 / 0%), annulment of the 4% realtor cap noted, normirani s.p. thresholds from 1 Jan 2026, 2025-2026 minimum wage, ZGos-1 short-let block
- **2026-05-29** — Anti-hallucination sweep: price-benchmark sourcing labelled (transacted vs asking), 2019-2024 period added to the GURS price changes
- **2026-09-18** — Ljubljana water / wastewater operator re-identified as JP VOKA SNAGA (URL re-pointed)
- **2026-09-24** — November regwatch wave: davek na nepremičnine 1.45% izhodišča re-labelled NOT ENACTED; NUSZ stays
- **2026-10-21** — December regwatch wave: tax tracker entry re-checked
- **2026-10-23** — 21 Oct 2026 audit applied: ZGos-1 in force with 2027-2028 day caps in 14 municipalities; ZIURS not in force pending the 6 Dec 2026 referendum
- **2026-10-23** — Refresh wave. Playbook-level date re-stamped 2026-10-23: every fast-changing section is now re-verified — `--work` in the refresh, `--price`, `--tax`, `--rental` and Cost benchmarks (with Common listing platforms) in the first same-day gap-closing pass, `--risks` and `--mains` in the second; Country profile, Reddit / forum sources, Active fiscal incentives, Caveats unique to SI and `--traffic` stay refreshed, not re-verified. Counts per section (facts checked — changed / confirmed / unverifiable):
  - Re-verified: `--work` 16 — 5 / 11 / 0; Verification authorities 7 — 4 / 3 / 0; Source URL templates 10 — 1 / 8 / 1, plus five rows added
  - Refreshed, not re-verified: Country profile 4 — 0 / 4 / 1; `--price` 28 — 14 / 8 / 8; `--rental` 25 — 4 / 15 / 8; Common listing platforms 8 — 2 / 3 / 4; Reddit / forum sources 6 — 1 / 3 / 2; `--tax` 20 — 11 / 6 / 4; Cost benchmarks 11 — 6 / 1 / 9; Active fiscal incentives 5 — 4 / 1 / 2; Caveats unique to SI 6 — 3 / 2 / 1 (legal / fiscal only); `--traffic` 8 — 1 / 6 / 1; `--risks` 40 — 26 / 7 / 9; `--mains` 11 — 3 / 2 / 6
  - Main changes: GURS H1 2026 ETN medians replace the unsourced price ranges; posplošena vrednost dates corrected (applied 13 May 2025, owners mailed 26 May – 1 Jul 2025) and the €298 bn / +8% figures relabelled secondary press; e-Sodstvo moved to esodisce.si; Salomon.si and MojCG.com ❌ DEPRECATED, TopRealitet removed; rental tax rewritten as a 25% final tax after 10% normirani stroški or actual costs (cedolare-style alternative removed) and the sobodajalec VAT threshold raised from €50,000 to €60,000; normirani s.p. eligibility rebuilt on the two-year average-revenue test (the €60,000 / €30,000 exit rule was wrong); SURS 2025 average wages replace the median ranges; realtor 4% cap annulled by the Constitutional Court on 2 Sep 2025 and the "3–4% typical" figure removed; DPN taxpayer rule, DDV 9.5% conditions and primary-residence exemption re-sourced to FURS; NUSZ, notary, court-fee and transaction-total figures labelled est.; foreign-buyer reciprocity caveat added; the invented seismic cona 1/2/3 scheme replaced by the official design-acceleration map (seismic caveat aligned with ARSO's 2021 map, the only official design map since 1 May 2024), with the 1998 / 2004 Posočje magnitudes, the ice-storm date (end Jan – early Feb 2014, not June) and the PBAB81 era label corrected; radon re-sourced to URSVS; EI fine €300 (not €1,000); ARSO OPS21 climate ranges; MČN → MKČN and mains cost rows labelled est.
  - Gap-closing pass (confirmed / changed / relabelled): `--price` 24 / 4 / 3; `--rental` 12 / 6 / 2; `--tax` 13 / 4 / 1; Cost benchmarks 2 / 3 / 6; Common listing platforms 1 / 1 / 1 — closed; `--risks` 3 / 5 / 1 and `--mains` 0 / 1 / 4 — patched, still open; total 55 / 24 / 18. Main changes: posplošena vrednost total and price growth re-sourced to GURS, the +8% baseline corrected to the Oct 2024 trial calculation; ZGos-1 read in the gazette (owner-consent threshold corrected, 180-day sobodajalec cap and AJPES register added, per-občina licensing and AVRSK + STO removed); notary, court-fee, NUSZ and buyer-side figures rebuilt from the Notarska tarifa, the courts' worked example and the MOL odlok as computed examples; realtor ruling read in Uradni list RS 76/2025; floods, landslides, the Stože 2000 toll, wildfire, karst, the PCB era and sea level re-sourced (URSZR, GeoZS, gov.si MOP, PCB Uredba, ARSO); greznica claims replaced by SURS 2021 per-občina shares and Eurostat 2024 national shares
  - Second gap-closing pass (confirmed / changed / relabelled): `--risks` 24 / 4 / 0 and `--mains` 37 / 0 / 0 — closed; total 61 / 4 / 0. Main changes: ice-storm superlative narrowed to the largest in RS to date (none as severe and extensive known after 1890); wildfire trend reworded (the rise may slow after 2040 and slow further or stop after 2070); radon new-build duty scoped to new builds, interventions and anti-radon remediation of buildings with living or working rooms; GURS zbirno potrdilo mailing dated 26 May – 1 Jul 2025; GeoZS leaflet and MR02 archive date tags refreshed; VOKA SNAGA per-connection fee totals computed (€662.82 water / €732.73 sewer)
