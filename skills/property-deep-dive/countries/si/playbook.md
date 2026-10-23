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
  - Aggregated stats free; per-transaction limited
- **e-Sodstvo Zemljiška knjiga**: `https://esodisce.si/` — land register lookup (updated 2026-10-23; the old evlozisce.sodisce.si address 301-redirects here)
- **SURS (Statistični urad RS)**: `https://www.stat.si/` — national stats

### Listing platforms

- **Nepremicnine.net** — DOMINANT: `https://www.nepremicnine.net/`
- **Bolha.com**: `https://www.bolha.com/nepremicnine`
- **Slonep.net** — secondary
- **Salomon.si** ❌ DEPRECATED — dead on 2026-10-23 (connection refused); verify listings on Nepremicnine.net / Bolha.com
- Agency networks: **Stoja Trade**, **Re/Max Slovenia**, **DODOMA**

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
- Total Slovenian property value: **€298 billion** (2025 data, secondary press: Bloomberg Adria / N24 — verify with GURS — rates/figures may have changed since)
- Average **+8% increase** vs 2020 values (2025 data, same secondary press — verify with GURS)
  - Apartments: +64% (2019-2024)
  - Houses: +54% (2019-2024)
  - Building land: +74% (2019-2024)
- Sets the base for any future davek na nepremičnine

### Compute

1. €/m² = price / **uporabna površina** (usable area)
2. **Posplošena vrednost** ≠ market value (typically lower, conservative)
3. **Etažna lastnina**: read **Pogodba o medsebojnih razmerjih** + **Zapisniki zborov etažnih lastnikov** + **Rezervni sklad** before buying flat

### Key terms

- Stanovanje = apartment
- Hiša = house
- Posplošena vrednost = generalized (mass-appraised) value — used for property tax base
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
  - Typical residential: **est. €100–€600/yr** (not verified against the odloki — the amount turns on zone, use and utility equipment; read the občina's odlok)
  - Assessed by FURS for the občina, municipal revenue; payable by the direct user (owner or tenant); a buyer of a new flat or builder of a new family house can claim a 5-year exemption from the občina where the land-servicing costs were paid in the price or directly (2026 data, source FURS Brošura o obdavčitvi nepremičnin, 8th ed., Sep 2026)
- **Davek od premoženja** (Zakon o davkih občanov): annual tax on individuals' buildings, flats, garages and recreational premises, payable whether owner-used or let; base = points-based value, reduced by the value of 160 m² where the owner or close family lived there permanently in the prior year, so a second home or vikend is assessed; 10-year exemption on application for the first owner of a new dwelling; assessed by 31 Mar, amounts valorised yearly; municipal revenue (2026 data, source FURS Brošura o obdavčitvi nepremičnin, Sep 2026 + FURS Sem lastnik ali uporabnik nepremičnine)
- **Davek na nepremičnine** (comprehensive property tax): ZDavNepr (Uradni list RS 101/13, in force 1 Jan 2014) was annulled by the Constitutional Court (U-I-313/13-86, 21 Mar 2014), which restored the previous regime (FURS davek od premoženja page); a successor was last proposed in Dec 2024 (below)

### Davek na nepremičnine reform 2025-2026 (NOT ENACTED)

- 2025 posplošena vrednost reform sets the base
- **Government izhodišča (23 Dec 2024)**: **1.45%** of the GURS posplošena vrednost on residential property, the first home the owner actually lives in fully exempt (MF gov.si, 2024-12-23) — **NOT ENACTED**, it never advanced past the izhodišča
- **Status**: no law; MF collected responses to 25 Jan 2025 and no successor bill was found in the sources read on 2026-09-24 (FURS page refreshed 29 Dec 2025; a secondary 8 Sep 2026 report says the proposal never became law); the 16th Government (appointed 4 Jun 2026) has not been shown to revive it — re-verify at MF gov.si before quoting a rate
- **No implementation date**: no enacted law
- The izhodišča went to public consultation with comments due 25 Jan 2025 (MF gov.si, 23 Dec 2024); no draft law followed (see Status)

### Transaction taxes

- **Davek na promet nepremičnin (DPN)**: **2%** of the sale price (2026 data, source FURS DPN page, refreshed 7 Oct 2026). The seller is the taxpayer and stays liable even where the contract shifts payment to the buyer; the seller files within 15 days of signing; without FURS's DPN confirmation the notary cannot certify the signatures and the land register cannot enter the buyer; not charged on a transfer on which DDV was charged (ZDPN-2 Art. 4); revenue goes to the občina where the property lies (2026 data, source FURS Brošura o obdavčitvi nepremičnin, Sep 2026 + FURS Nakup in prodaja nepremičnine)
- **DDV (VAT)**:
  - 9.5% reduced (residential new builds) only for dwellings for permanent living that count as social policy: a flat of up to 120 m² in a multi-dwelling building, or up to 250 m² usable area in a single-dwelling building; otherwise the 22% standard rate (2026 data, source FURS Stopnje DDV, 15th ed., Oct 2026 — ZDDV-1 Annex I pt 11)
  - 22% standard (commercial)
- **Notar fees**: est. ~1.0–1.5% — not verified against the Notarska tarifa; the notary must certify the signatures on the sale contract and can also draft it or execute it as a notarski zapis (notar-z.si) — get a quote
- **Realtor commission**: no statutory cap. The Constitutional Court's partial decision U-I-205/19, U-I-230/19 of **2 Sep 2025** annulled the 4% cap and the minimum fee in ZNPosr Art. 5(1)–(2) for residential sales and lettings to natural persons, together with Art. 5(4)–(5) insofar as they refer to them and Art. 5(6)–(7); its partial decision of 26 Oct 2023 had already annulled paras 1–2 for all other deals, and the final ruling followed the CJEU's Feb 2025 judgment on the Services Directive 2006/123/EC. Only the para-3 rule remains (no charging a party that did not engage the agency). The rate is negotiated in the mandate contract — no market-rate figure verified (2025 decision, source iusinfo.si 9 Oct 2025 + pfp.law 3 Dec 2025, secondary legal publishers; primary text at us-rs.si)

### Total transaction cost (buyer side)

- **From seller side**: 2% DPN (the contract can shift payment to the buyer, but the seller stays the taxpayer — FURS 2026) + agency commission (negotiated; the statutory cap was annulled by the Constitutional Court decision of 2 Sep 2025); the agency can charge only the party that engaged it, and a sale-contract clause to the contrary is void (ZNPosr Art. 5(3) and 5(5), per iusinfo.si — secondary)
- **Buyer side direct**: est. ~1.5–2.5% (notar + zemljiška knjiga + sodne takse; not verified against the Notarska tarifa or the court-fee tariff)

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

- **Davek na nepremičnine**: NOT ENACTED — the Dec 2024 1.45% izhodišča never advanced (see above); any revival by the 16th Government is unverified
- **NUSZ stays**: MF stated the proposed tax would NOT have replaced NUSZ (it would have abolished only the ZDO davek od premoženja)
- **Posplošena vrednost** revaluation cycles

---

## Section: `--rental`

### Long-term residential

- Standard income tax on rental: 25% final tax after a 10% flat cost allowance or documented actual maintenance costs (paid as akontacija dohodnine; 2026 data, source FURS); the ZIURS cut to 15% applies only if ZIURS survives the 6 Dec 2026 referendum (see Short-let)
- **Tenant protection moderate** (less strict than DE/AT)
- Standard contract: 1-3 yrs typical

### Short-let (kratkoročno oddajanje)

- **ZGos-1** (Zakon o gostinstvu, Uradni list RS 77/25; adopted by the DZ 25 Sep 2025, published 7 Oct 2025, in force 22 Oct 2025, **applies since 1 Jan 2026** — PISRS ZAKO9019) **is in force**. Day cap: under the ministers' Sklep published 8 May 2026 (PISRS SKLE14364), short-term letting of each dwelling is capped at **60 days per calendar year in 2027 and 2028** in 14 high-risk municipalities — Ankaran, Bled, Bohinj, Bovec, Cerklje na Gorenjskem, Gorje, Izola, Koper, Kranjska Gora, Ljubljana, Piran, Preddvor, Radovljica, Žirovnica — unless the municipality set a 30–270-day limit by a general act adopted by 31 Oct 2026; municipalities not on the list may set a limit of at least 60 days ([gov.si, 8 May 2026](https://www.gov.si/novice/2026-05-08-objavljen-sklep-o-dolocitvi-obcin-z-visokim-tveganjem-negativnih-vplivom-kratkotrajnega-najema)). The enacted law has no 150-day single- or two-unit tier (superseded). Owner consent (secondary source — verify in ZGos-1 on PISRS): more than 75% of etažni lastniki plus all owners of adjacent units in multi-unit buildings, 100% in two-unit buildings, valid 3 years; consents already held stay valid until 31 Dec 2026 or 3 years from when they were obtained, whichever is later.
- **ZIURS** (Zakon o interventnih ukrepih za razvoj Slovenije) — adopted by the DZ 11 May 2026, **NOT in force**: on 24 Jul 2026 the Constitutional Court annulled the DZ's 27 May ruling that a referendum was inadmissible; 42,694 signatures were filed (40,000 needed) and on 16 Oct 2026 the DZ called a subsequent legislative referendum (naknadni zakonodajni referendum) for **6 Dec 2026** (press: [mladipodjetnik.si](https://mladipodjetnik.si/novice-in-dogodki/novice/referendum-o-interventnem-zakonu), [Delo](https://www.delo.si/novice/slovenija/referendum-interventni-zakon-december-drzavni-zbor)). Only if ZIURS takes effect would it suspend ZGos-1 to 31 Dec 2026, drop the 2027 day cap, move the accommodation-register deadline to 30 Jun 2027, restore the old by-laws, extend neighbour consents and cut the tax on rental income from 25% to 15% (5% where the tenant is a young family) (press-tier). Until then ZGos-1 and the 2027 caps apply; the 31 Oct 2026 municipal deadline falls before the referendum.
- **Ljubljana** strict (similar to Praha/Wien direction)
- **Sobodajalec** (short-let provider) licensing per občina
- **EU 2024/1028** (directly applicable, opt-in): applies since 20 May 2026; a national Single Digital Entry Point is required only where Slovenia runs an STR registration procedure (Art. 10(1)) — Slovenian implementing measures and entry-point designation: verify at gov.si
- **AVRSK + STO** (tourist board) registration

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
| **URSZR (Uprava RS za zaščito in reševanje)** | `https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/` | Civil protection; national hazard assessments (earthquake v3.0 Jun 2018, flood v3.0 Aug 2026, ice storm v1.1 Sep 2026): `https://www.gov.si/teme/ocene-ogrozenosti-zaradi-naravnih-in-drugih-nesrec/` |
| **Direkcija RS za vode (DRSV)** | `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-vode/` | Water management |
| **eVode + Atlas voda (DRSV)** | `http://www.evode.gov.si/` · `https://geohub.gov.si/atlasvoda` | Flood hazard maps (Integralna karta poplavne nevarnosti, data updated 21 Aug 2026), water cadastre |

### Specific risks

- **Poplava (floods)**: Sava, Drava, Mura, Soča valleys; **August 2023 floods** (peak 4 Aug) — the worst in Slovenia's known history: 7 dead, 183 občine hit, damage just under €3 bn (official methodology) / > €5 bn (PDNA) — major reform driver; **ice storm (žled) end Jan–early Feb 2014** (largest in RS history) + floods Sep and Oct 2014; sea flooding on the coast — Koper, Izola and Piran are among the 104 areas of significant flood risk (OPVP) set in 2025; check the parcel on the Integralna karta poplavne nevarnosti (eVode / Atlas voda) (2026 data, source URSZR Ocena ogroženosti zaradi poplav v3.0, 24 Aug 2026 + Ocena ogroženosti zaradi žleda v1.1, 15 Sep 2026)
- **Potresna ogroženost (seismic)**: Slovenia lies in an area more exposed to earthquakes than most European countries (gov.si, URSZR Napotki prebivalcem ob potresu); URSZR rates it a country of moderate seismic hazard where relatively shallow foci can make effects fairly large (source URSZR Ocena ogroženosti RS zaradi potresov v3.0, Jun 2018)
  - Posočje (Soča valley): **12 Apr 1998 Krn–Lepena M 5.7** (VII–VIII EMS, > 4,000 buildings damaged) + **12 Jul 2004 Krn–Lepena ML 4.9** (VI–VII EMS, damage mainly around Bovec / Čezsoča) (source URSZR, 2018)
  - **Ljubljana 14 Apr 1895 ML 6.1** (VIII–IX EMS; ~10% of the city's ~1,400 buildings damaged); strongest recorded on Slovenian territory: **Idrija 26 Mar 1511, est. M 6.8** (source URSZR, 2018)
  - **Official design map**: ARSO *Potresna nevarnost Slovenije – projektni pospešek tal* (2021) — PGA on rock (EC8 ground type A), 475-year return period; valid since 1 May 2022 and the only official map (sole annex to the EC8 National Annex) since 1 May 2024, replacing Lapajne et al. 2001; 10 classes of 0.025 g from **0.100 g to 0.325 g**, not numbered zones; places on a class boundary take the higher value
  - **0.325 g** (highest): the Italian border west of Bovec; **0.300 g**: around Idrija and in SE Slovenia around Brežice; **0.275 g**: Ljubljana and surroundings; values are higher than on the 2001 map across most of Slovenia (up to +0.125 g in Bela krajina), comparable around Ljubljana / Kranj / Kamnik and in the SW, slightly lower only around Ptuj
  - **0.100 g** (lowest): NE Slovenia (Maribor, Ptuj, Prekmurje) and the Izola–Piran coast, with Koper town on the 0.100/0.125 class line (2021 map, source ARSO Tolmač karte potresne nevarnosti 2021, updated 29 Jul 2026, + map legend: `https://potresi.arso.gov.si/doc/dokumenti/potresna_nevarnost/`); read the class at the exact parcel in the ARSO pregledovalnik, not the municipality
- **Plaz / zemeljski plaz** (landslides): widespread in Karavanke + Kamniško-Savinjske Alpe + flysch areas
  - **Stože plaz 2000** (7 dead near Log pod Mangartom)
- **Suša + požar** (drought + fire) increasing climate risk
- **Karst hazards**: **Mali Krasovi** (small karst formations) widespread; cave/sinkhole risk
- **Radon**: URSVS lists 24 higher-radon občine — Bloke, Cerknica, Črnomelj, Divača, Dobrepolje, Dolenjske Toplice, Hrpelje - Kozina, Idrija, Ig, Ivančna Gorica, Kočevje, Komen, Logatec, Loška dolina, Loški Potok, Miren - Kostanjevica, Pivka, Postojna, Ribnica, Semič, Sežana, Sodražica, Vrhnika, Žužemberk — plus 27 občine under additional measurement; reference level **300 Bq/m³**, which new builds must stay below (TSG-1-007:2023 is the compliance route) (source URSVS, gov.si Zmanjševanje izpostavljenosti radonu, checked 2026-10-23)
  - **Radonski zemljevid Slovenije** (URSVS): municipality-level only — says nothing about a given parcel; measure in the dwelling (only measurements by URSVS-authorised providers count officially)
- **Klimatske spremembe**: mean temperature **+1.1 to +2.3 °C (RCP4.5) / +1.6 to +2.8 °C (RCP8.5) in 2041–2070** vs 1981–2010 (2019 data, source ARSO Ocena podnebnih sprememb v Sloveniji do konca 21. stoletja, dopolnjen povzetek) — rates/figures may have changed since

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1948** | No national seismic design rules (only Ljubljana's 1896 building code after the 1895 quake) |
| **1948–1963** | 1948 temporary rules (Ur. l. SFRJ 61/48) heavily underestimated seismic loads; buildings as a rule carried vertical loads only — treat as non-seismic, critical in the high-PGA classes |
| **1964–1981** | First serious seismic design rules: Odredba 1963 (Ur. l. SRS 18/63), Yugoslav Pravilnik 1964 (Ur. l. SFRJ 39/64) |
| **1982–2007** | 1981 Pravilnik o tehničnih normativih za graditev objektov visoke gradnje na seizmičnih področjih (Ur. l. SFRJ 31/81 + amendments) — higher seismic resistance |
| **2008+ (EC8)** | Eurocode 8 (SIST EN 1998); old rules allowed until 1 Jan 2008; design map Lapajne et al. 2001 until the 2021 ARSO map took over (valid from 1 May 2022, sole official map from 1 May 2024) (source URSZR Ocena ogroženosti zaradi potresov v3.0, 2018; ARSO Tolmač karte potresne nevarnosti 2021) |
| **Asbestos** | used intensively across Europe 1945–1990, all use banned since 1 Jan 2005 (gov.si Azbest) — pre-1990 builds most likely, pre-2005 possible |
| **PCB** | 1970s-1980s buildings |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetska izkaznica (EI)** | Energy certificate (ZURE, Ur. l. RS 158/20): hand over before signing a sale or a lease > 1 year; EI indicators must appear in ads | 10 years (source energetika-portal.si, checked 2026-10-23) |
| **Penalty for missing EI** | **€300** fine on the owner (no EI before the contract, or EI indicators missing from ads — ZURE Art. 31(2), (9)); €100 on the responsible person of a legal entity | n/a |
| **Zemljiškoknjižni izpisek** | Land register extract | At sale |
| **Posplošena vrednost (GURS)** | Not a sale document: owners were mailed a zbirno potrdilo in May–June 2025; values reflect the market at 1 Jan 2025 and are recalculated whenever property data change — print the current value from EV_JV (source GURS e-prostor, checked 2026-10-23) | Until data change |
| **Pogodba** + **notarska overitev** | Contract + notary verification | At sale |

### Climate change projections

- Mean temperature vs 1981–2010: **+1.1 to +2.3 °C (RCP4.5) / +1.6 to +2.8 °C (RCP8.5) in 2041–2070**; **+1.5 to +2.6 °C / +3.0 to +5.1 °C in 2071–2100** (2019 data, source ARSO OPS21 dopolnjen povzetek, `https://meteo.arso.gov.si/met/sl/climate/change/`) — rates/figures may have changed since
- Precipitation: the winter increase is the clearest signal (eastern SI up to +40% in winter by mid-century under RCP8.5); summer direction uncertain (RCP4.5 leans drier to mid-century); annual totals ~+10% by 2100 under RCP4.5 except the Julian Alps (ARSO OPS21, 2019)
- More intense and more frequent extreme precipitation (August 2023 type) (ARSO OPS21, 2019)
- Adriatic coast sea-level rise
- Karst water-supply stress

---

## Section: `--mains`

### Sources

- **Komunalne službe** per občina (municipal services)
- **JP VOKA SNAGA** (Ljubljana water + wastewater operator, Javni holding Ljubljana; formerly Vodovod-Kanalizacija Ljubljana): `https://www.vokasnaga.si/` — drinking-water supply and wastewater, incl. public reporting under Uredba o pitni vodi (Ur. l. RS, št. 61/23) (2026-10-23 verified)
- **Mariborski vodovod** (javno podjetje, drinking water): `https://www.mb-vodovod.si/` + regional public utilities
- Most občine have own komunala
- Universal in cities; rural Karst + Pohorje villages on greznica (cesspit)

### Verification

- Cities + most občine: javni vodovod + javna kanalizacija
- **Karst** villages (e.g., parts of Notranjska, Kras, Bela krajina): often on cesspit (greznica)
- **Mala komunalna čistilna naprava (MKČN, < 50 PE)**: the owner must provide individual treatment outside agglomerations (public sewer is the občina's duty inside them); an MKČN needs first measurements (prve meritve) reported to the komunala, and sludge / greznica emptying is a mandatory public-service job (source gov.si Odvajanje in čiščenje komunalne in padavinske odpadne vode, checked 2026-10-23)

### Costs

| Scenario | est. cost (€) — unsourced; get komunala + contractor quotes |
|---|---:|
| Priklop na javno kanalizacijo | 4,000–10,000 |
| MKČN namestitev | 5,000–12,000 |
| Greznica reorganizacija | 3,000–8,000 |
| Vodovodni priključek | 1,500–4,500 |

---

## Cost benchmarks (SI 2026)

| Work | Cost (€; construction and service rows are est., not verified against a primary source) |
|---|---:|
| Energetska izkaznica | est. 150–400 |
| Notar | est. 1.0–1.5% of price (Notarska tarifa not verified) |
| DPN (transfer tax) | 2% of price; seller is the taxpayer, the contract can shift payment to the buyer (FURS 2026) |
| Realtor (no statutory cap since 2 Sep 2025) | negotiated; no market-rate figure verified |
| Zemljiška knjiga + sodne takse | est. €100–€500 (court-fee tariff not verified) |
| **Total transaction cost (buyer)** | **est. ~1.0–1.5% + €100–€500**, or **est. ~3.0–3.5% + €100–€500** where the buyer takes over the DPN (sum of the notar, DPN and land-register rows above), plus any agency fee owed under the buyer's own mandate |
| Septik to mains | 4,000–10,000 |
| Roof (terracotta tile, 200 m²) | 15,000–25,000 |
| Energy retrofit (Class C → A) | 30,000–80,000 |
| Antiseismic retrofit (small house) | 25,000–60,000 |
| Asbestos removal | 1,500–8,000 |

## Active fiscal incentives (2025-2026)

- **Eko sklad** (ekosklad.si): grant and/or loan for heat pumps, façade, roof and floor insulation, windows and external joinery, biomass boilers, heat-recovery ventilation, solar heating, self-supply solar plants and whole-building renovation (current incentive list, read 2026-10-23)
- **Eko sklad loans only** (no grant): small wastewater plants (MČN), connection to the public sewer or water mains, asbestos-roof replacement (same list)
- **Stanovanjski sklad RS**: no open loan call for individual buyers on its javni pozivi page (read 2026-10-23); its current calls cover public rental housing, including Javni najem, a standing call for offers from dwelling owners (Razpis zbiranja ponudb najemodajalcev) — verify at ssrs.si before citing any buyer loan
- **Subvencije za mlade** (young families) per občina
- **MČN subsidies at občina level**: not verified — ask the občina (the Eko sklad MČN offer is a loan)

## Common listing platforms

- **Nepremicnine.net** — biggest
- **Bolha.com** — secondary
- **Slonep.net**
- **Salomon.si** ❌ DEPRECATED — dead on 2026-10-23 (connection refused); verify listings on Nepremicnine.net / Bolha.com
- Agency networks: Stoja Trade, Re/Max SI, DODOMA

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

✅ **Fully populated** as of 2026-04-25 (Ljubljana water / wastewater operator re-identified as JP VOKA SNAGA 2026-09-18; the si:286 connection-cost figures were not re-verified). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Short-let block (ZGos-1 day caps, ZIURS referendum) re-checked 2026-10-23 against gov.si and national press; see shared/regulatory-watch.md.
**Coverage check**: pricing, traffic, tax (with the not-enacted 1.45% proposal note), rental, work, risks (incl. ARSO seismic design-acceleration map + August 2023 flood reference), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for `--work` (normirani s.p. rules from the FURS Brošura o dohodku iz dejavnosti and gov.si of 16 Oct 2026; d.o.o. €7,500 on SPOT; SURS SiStat 2025 average wages; 2026 minimum wage on gov.si). HIGH for the H1 2026 GURS ETN price table (GURS polletno poročilo, Oct 2026) and the 13 May 2025 posplošena vrednost dates (gov.si GURS releases); for the DPN, capital-gains, primary-residence, DDV and NUSZ rules (FURS brochure Sep 2026, DPN page 7 Oct 2026, Stopnje DDV Oct 2026); for the 25% rental-income tax and the €60,000 sobodajalec VAT threshold (FURS); for the ZGos-1 2027-2028 day-cap mechanism and municipality list (gov.si, 8 May 2026); for the flood, ice-storm, radon and energetska izkaznica facts in `--risks` (URSZR assessments of Aug and Sep 2026, URSVS, energetika-portal.si); and for the mains operators and MKČN duties (VOKA SNAGA, Mariborski vodovod, gov.si). MEDIUM for the realtor-cap annulment (Constitutional Court decision of 2 Sep 2025, read via iusinfo.si and pfp.law, secondary legal publishers); the NOT-ENACTED status of the davek na nepremičnine 1.45% izhodišča (successor-bill and 16th Government check last run 2026-09-24; re-verify at MF gov.si before output); the ZIURS not-in-force status and 6 Dec 2026 referendum (press-tier); the seismic and climate text in `--risks` (URSZR 2018 earthquake assessment, ARSO 2021 design map, ARSO OPS21 projections with 2019 data; the qualitative climate bullets are unsourced); and `--traffic` (DRSI PLDP 2025 figures; the verdict bands are curated thresholds). LOW for the €298 bn aggregate, the +8% average and the 2019-2024 price changes (secondary press only, not found on GURS); the ZGos-1 gazette details and owner-consent rule; sobodajalec licensing per občina and AVRSK + STO registration; the listing-platform and agency claims; the Stože 2000 death toll, Mali Krasovi, the landslide and flood-valley lists and the PCB era; greznica prevalence by area; and every est. cost row (NUSZ amount, notary, land-register fees, transaction totals, mains connections, construction).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Normirani s.p. rules rebuilt from the FURS Brošura o dohodku iz dejavnosti + gov.si 16 Oct 2026 (the €60k / €30k exit rule was wrong); d.o.o. €7,500 on SPOT; SURS SiStat 2025 averages replace the unsourced median ranges; minimum wage gross on gov.si, uncalibrated net removed |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Roles corrected: seismic map ARSO, radon URSVS, GeoZS geology / landslides, land register at the okrajna sodišča (esodisce.si); Upravna enota, URSVS and DRSV / eVode rows added |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | Liveness and redirects checked: e-Sodstvo 301 → esodisce.si (replaced); nepremicnine.net answers 403 to scripts (kept); five rows added for URLs cited in the new risk / traffic text |

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
- **2026-10-23** — Refresh wave. Playbook-level date not re-stamped: `--price`, `--tax`, `--rental`, `--risks` and `--mains` were not fully re-verified. Counts per section (facts checked — changed / confirmed / unverifiable):
  - Re-verified: `--work` 16 — 5 / 11 / 0; Verification authorities 7 — 4 / 3 / 0; Source URL templates 10 — 1 / 8 / 1, plus five rows added
  - Refreshed, not re-verified: Country profile 4 — 0 / 4 / 1; `--price` 28 — 14 / 8 / 8; `--rental` 25 — 4 / 15 / 8; Common listing platforms 8 — 2 / 3 / 4; Reddit / forum sources 6 — 1 / 3 / 2; `--tax` 20 — 11 / 6 / 4; Cost benchmarks 11 — 6 / 1 / 9; Active fiscal incentives 5 — 4 / 1 / 2; Caveats unique to SI 6 — 3 / 2 / 1 (legal / fiscal only); `--traffic` 8 — 1 / 6 / 1; `--risks` 40 — 26 / 7 / 9; `--mains` 11 — 3 / 2 / 6
  - Main changes: GURS H1 2026 ETN medians replace the unsourced price ranges; posplošena vrednost dates corrected (applied 13 May 2025, owners mailed 26 May – 1 Jul 2025) and the €298 bn / +8% figures relabelled secondary press; e-Sodstvo moved to esodisce.si; Salomon.si and MojCG.com ❌ DEPRECATED, TopRealitet removed; rental tax rewritten as a 25% final tax after 10% normirani stroški or actual costs (cedolare-style alternative removed) and the sobodajalec VAT threshold raised from €50,000 to €60,000; normirani s.p. eligibility rebuilt on the two-year average-revenue test (the €60,000 / €30,000 exit rule was wrong); SURS 2025 average wages replace the median ranges; realtor 4% cap annulled by the Constitutional Court on 2 Sep 2025 and the "3–4% typical" figure removed; DPN taxpayer rule, DDV 9.5% conditions and primary-residence exemption re-sourced to FURS; NUSZ, notary, court-fee and transaction-total figures labelled est.; foreign-buyer reciprocity caveat added; the invented seismic cona 1/2/3 scheme replaced by the official design-acceleration map (seismic caveat aligned with ARSO's 2021 map, the only official design map since 1 May 2024), with the 1998 / 2004 Posočje magnitudes, the ice-storm date (end Jan – early Feb 2014, not June) and the PBAB81 era label corrected; radon re-sourced to URSVS; EI fine €300 (not €1,000); ARSO OPS21 climate ranges; MČN → MKČN and mains cost rows labelled est.
