# Finland 🇫🇮 — Property Due-Diligence Playbook

ISO2: `fi`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`00100` Helsinki, `33100` Tampere, `20100` Turku)
- **Admin levels**: 19 maakuntaa (regions, incl. Ahvenanmaa / Åland) + 308 kuntaa (municipalities) (2026 data, source: Tilastokeskus kunta + maakunta classifications 2026)
- **Currency**: EUR (€) — adopted 1999/2002
- **Languages**: **Finnish + Swedish (both official)**; Sámi minority (Lapland)
- **Cadastre**: **Maanmittauslaitos (NLS Finland)** + **KTJ (Kiinteistötietojärjestelmä)** national property register
- **Identifier**: kiinteistötunnus 4-section format (e.g., `091-018-0118-0006` = `<kunta>-<kylä/kaupunginosa>-<rekisterinumero>-<rekisteriyksikkö>`)
- Distinct ownership types: **kiinteistö** (real-estate freehold — land + building together), **asunto-osakeyhtiö (As Oy)** (housing company — share-based, MAJOR form), **käyttöoikeus** (right of use)

## Section: `--price`

### Primary sources

- **Maanmittauslaitos e-services**: `https://www.maanmittauslaitos.fi/en/e-services` — Property Transaction Service (convey own property, apply for mortgages; strong authentication; some parts charged), free real-estate transaction price statistics (kauppahintatilasto), MapSite (property identifiers + boundaries) (2026-10-23 verified, source: NLS e-services page)
- **KTJ Kiinteistörekisteri** (cadastre records): paid extracts
- **Tilastokeskus — Osakeasuntojen hinnat** (StatFin `ashi`): old As Oy dwelling €/m² by kunta (table 13mx) and postcode (table 13mu), annual + quarterly — API `https://pxdata.stat.fi/PxWeb/api/v1/fi/StatFin/ashi/`
- **Tilastokeskus — Kiinteistöjen hinnat** (StatFin `kihi`): old detached-house €/m² and floor area by area class (table 15hw)

### Listing platforms

- **Etuovi.com** — largest: `https://www.etuovi.com/`
  - Search by kunta + alueet + asunto-tyyppi
- **Oikotie**: `https://asunnot.oikotie.fi/`
- **Vuokraovi.com** (rentals)
- **Habita, Sp-Koti, OP Koti** (formerly OPKK; `opkk.fi` redirects to `op-koti.fi`) — agency networks
- **Kiinteistömaailma**, **Huoneistokeskus** — premium agencies

### 2025 price benchmarks (Tilastokeskus + Maanmittauslaitos)

As Oy column: old (resale) As Oy dwellings, 2025 annual average €/m², all house types (2025 data, source: Tilastokeskus StatFin tables 13mx by kunta and 13mu by postcode). Small-house column: built asuinpientalo on own plot in asemakaava areas, Maanmittauslaitos kauppahintatilasto 2025 as reported by Yle on 25 Feb 2026 (secondary) — capital-region figures are medians, the others averages. Municipal / postcode averages, not a valuation of any specific property.

| Region | As Oy €/m² (2025 avg) | Asuinpientalo, asemakaava area (2025) |
|---|---:|---:|
| **Helsinki** | 4,983 (kerrostalo flats 5,225; central postcodes 00100–00180 flats 6,493–9,653 by postcode and flat size) | median €468,500 |
| **Espoo** | 3,773 | median €612,500 |
| **Vantaa** | 2,675 | median €368,000 |
| **Tampere** | 2,979 | avg €310,000 |
| **Turku** | 2,653 | avg €272,500 |
| **Oulu** | 2,105 | avg €254,000 |
| **Jyväskylä** | 2,038 | avg €215,500 |
| **Kuopio** | 2,086 | avg €207,000 |
| **Rovaniemi** | 1,953 | avg €169,000 |
| **Lahti** / **Pori** | 1,675 / 1,325 | not in source |
| Kouvola / Kotka / Mikkeli | 1,088 / 1,184 / 1,459 | not in source |
| Municipalities 20,000–59,999 inhabitants (Tilastokeskus class) | — | est. ≈ €228,000 old detached house (1,810 €/m² × 125.7 m², 2025 sales-weighted, Tilastokeskus table 15hw) |
| Municipalities < 20,000 inhabitants (Tilastokeskus class) | — | est. ≈ €130,000 old detached house (1,128 €/m² × 114.9 m², 2025 sales-weighted, Tilastokeskus table 15hw) |
| Rural / mökki (vapaa-ajan asunto) | ~700–1,500 €/m² (est., unsourced — rates/figures may have changed since) | ~€80,000–€200,000; Lapland resort mökit can exceed €500k (est., unsourced — rates/figures may have changed since; verify at Maanmittauslaitos kauppahintatilasto) |

**Trend**: old As Oy prices 2026 Q2 (preliminary) −3.9 % year on year nationally, −4.3 % Helsinki, −3.3 % Tampere, −0.9 % Oulu (2026 data, source: Tilastokeskus StatFin table 15is).

### Compute

1. Listing €/m² = price / **asuinpinta-ala** (residential area, includes interior walls)
2. **Trap**: asuinpinta-ala vs huoneistoala (apartment area, slightly different) vs kerrosala (gross floor)
3. **As Oy math**: you buy **shares** (osake) in housing company; each share = € amount; **yhtiövastike** (monthly fee) covers building maintenance + sometimes shared mortgage
4. **Yhtiölaina** (housing company loan) tied to apartment — apartment carries portion of building debt

---

## Section: `--traffic`

### Primary sources

- **Väylävirasto** (Finnish Transport Infrastructure Agency): `https://vayla.fi/`
  - Open data via Liikennevirasto
- **Liikennevirasto Open data portal**: `https://www.liikennetilanne.fi/` (real-time)
- **Traficom** (traffic safety agency): `https://www.traficom.fi/`

### Key term

**KVL (keskimääräinen vuorokausiliikenne)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (paikallistie, residential katu)
- 🟡 1,000–8,000 v/d (kantatie, urban arterial)
- 🟠 8,000–30,000 v/d (valtatie, major urban)
- 🔴 > 30,000 v/d (moottoritie, central Helsinki/Tampere ring)

---

## Section: `--tax`

### Annual property tax — Kiinteistövero

**Set by each kunta within state-mandated bands**:

| Property type | 2026 statutory band (kunta sets its rate within it) |
|---|---:|
| **Maapohja** (land, general rate) | 1.30–2.00 % |
| **Rakennukset, yleinen** (buildings, general rate) | 0.93–2.00 % |
| **Vakituinen asuinrakennus** (permanent residence) | **0.41–1.00 %** |
| **Muu asuinrakennus** (other residential, incl. vapaa-ajan asunto) | **0.93–2.00 %** — significantly higher |
| **Rakentamaton rakennuspaikka** (undeveloped building plot, optional separate rate) | 2.00–6.00 % (Helsinki region: ≥ 3.00 pp above the general rate) |
| **Voimalaitos** (power plant) / **yleishyödyllinen yhteisö** | ≤ 3.10 % / may be set below the lower limit, down to 0.00 % |

(2026 data, source: vero.fi "Kiinteistön arvo ja kiinteistöveroprosentit", updated 31 Mar 2026; Kiinteistöverolaki 654/1992 §§ 11–14, Finlex)

**Calculation base**: Verohallinto's verotusarvo — buildings from jälleenhankinta-arvo (replacement cost, on yearly VM decree bases), land from its area and type (vero.fi, updated 31 Mar 2026).

**Valuation reform**: at its 1 Sep 2026 budget session the Orpo government decided to keep studying the kiinteistövero valuation reform but not to take it forward in the 2023–2027 electoral term, citing too little time for owners to prepare; the study is left to the next government (valtioneuvosto.fi budget-session release, 1 Sep 2026). The 2027 budget proposal (given 21 Sep 2026) lists no kiinteistövero change among its 2027 tax measures (budjetti.vm.fi). A kunta can still raise its rate within the bands above.

**Bills**: the decision is sent in March to whoever owned the property on 1 Jan; a tax of €170 or more is split automatically into two instalments, with due dates set by the month the owner's kiinteistöverotus ends — for most owners August + October (6 Aug / 6 Oct 2026) or September + November (7 Sep / 6 Nov 2026); every assessment ends by 31 Oct, so the latest pair is 7 Dec 2026 + 8 Feb 2027 (2026 data, source: vero.fi Kiinteistövero and Maksuohjeet pages, updated 24 Apr 2026 / 1 Jan 2026).

**Exemptions**: metsämaa, maatalousmaa and joutomaa can be exempt from kiinteistövero when they belong to a maatilakiinteistö (farm property); a property under 2 ha is generally not treated as a farm (vero.fi Maapohja page, updated 9 Feb 2026; Kiinteistöverolaki 654/1992 excludes forest and agricultural land from the tax).

### Transaction taxes — Varainsiirtovero (REFORM 2024)

**MAJOR REDUCTION 1 January 2024** (retroactive from 12 Oct 2023 — the rate follows the signing date of the final binding deed; real-estate transfers signed before 12 Oct 2023 stay at 4 %; vero.fi detailed guidance issued 29 Jan 2026):

| Asset | Old rate | **2024+ rate** |
|---|---:|---:|
| **Kiinteistö (real estate)** | 4.0 % | **3.0 %** |
| **Asunto-osakeyhtiö (As Oy) shares** | 2.0 % | **1.5 %** |
| **Other securities (incl. real-estate-company shares)** | 1.6 % / 2.0 % | **1.5 %** (unified from 1 Jan 2024) (2026 data, source: vero.fi varainsiirtovero page, updated 1 Jan 2026) |

**First-time buyer exemption ABOLISHED** from 1 Jan 2024 — the 0 % treatment for 18–39-year-old first-time buyers now applies only where the binding deed was signed before 1 Jan 2024 (vero.fi first-time-buyer guidance).

### Notary / title

- **No notary** in Finland real estate; transactions handled by **kaupanvahvistaja** (purchase witness)
- Kaupanvahvistajan palkkio: **€143** per purchase or other conveyance; a deed made in MML's electronic Kiinteistövaihdannan palvelu instead costs a **€236** service fee that includes the lainhuuto fee (2026 data, source: MML price list, read 2026-10-23)
- Maanmittauslaitos lainhuuto (title registration, kiinteistö): **€172**, unchanged on 1 Jan 2026; kiinnitys (mortgage-deed confirmation) €47; As Oy purchase: ownership registration in MML's huoneistotietojärjestelmä **€92** per osakehuoneisto, up from €89 (2026 data, source: MML fee notice of 17 Dec 2025)
- Real estate agent (välittäjä) fee: **est. 2.5–4.0 %** of price (market practice; negotiable), paid by seller

### Capital gains — Luovutusvoittovero

- **30 %** for gain ≤ €30,000/yr
- **34 %** above threshold
- Rates/threshold per pääomatulo (capital-income) schedule — same as the `--rental` entry below (2026 data, source: vero.fi guidance "Verotettavan tulon laskeminen henkilöverotuksessa", issued 15 Jan 2026)
- **Primary residence exemption**: gain fully exempt after ≥ 2 years of ownership during which the seller (or family) used it continuously as a permanent home (vero.fi guidance "Verovapaa oman asunnon luovutus", issued 9 May 2022)
- **Vapaa-ajan asunto** (secondary): full tax applies — second homes such as vapaa-ajan asunnot fall outside the permanent-home concept (same vero.fi guidance)

### VAT (ALV)

- 25.5 % standard (raised from 24 % on 1 Sep 2024) — also the rate on construction services (VAT rates in this list: 2026 data, source: vero.fi "Rates of VAT", updated 1 Jan 2026)
- **13.5 %** reduced (groceries, restaurant and meal services; since 1 Jan 2025 also books, pharmaceuticals, passenger transport, accommodation incl. cottage rental, sports and cultural services) — lowered from 14 % effective 1 Jan 2026
- 10 % reduced (newspapers and magazines only)
- New residential property: the sale itself is VAT-exempt (kiinteistö and As Oy shares alike), but construction services carry 25.5 % ALV, so VAT sits inside a new-build price; existing: VAT-exempt (2026 data, source: vero.fi Arvonlisäverovelvollisen opas § 6.1 and § 6.2.1, issued 1 Jan 2026)
- Commercial: sale VAT-exempt; letting is VAT-exempt (AVL 27 § 1 mom.) unless the lessor registers voluntarily (hakeutuminen) for premises used in VAT-deductible business, then 25.5 %

### Total transaction cost (buyer side)

- Real estate freehold: est. 3 % varainsiirtovero + €362 fixed fees (€143 kaupanvahvistus + €172 lainhuuto + €47 for one kiinnitys) — €250,000 → €7,862 ≈ 3.1 %; €80,000 → €2,762 ≈ 3.5 % (before optional kuntotarkastus, legal review and loan fees)
- As Oy shares: est. 1.5 % varainsiirtovero + €92 MML ownership registration — €250,000 → €3,842 ≈ 1.5 % (before optional surveys and loan fees)
- Among the **lower** in EU (after 2024 reform)

### Future risk

- Kiinteistövero valuation reform: not taken forward in the 2023–2027 term (government decision at the 1 Sep 2026 budget session, valtioneuvosto.fi); any revival depends on the government formed after the Eduskunta election of 18 Apr 2027 (third Sunday of April, Vaalilaki 714/1998) — verify against the government programme agreed after that election
- ALV: the general rate rose 24 % → 25.5 % on 1 Sep 2024 and the reduced rate fell 14 % → 13.5 % on 1 Jan 2026 (vero.fi)
- Vapaa-ajan asunto: taxed in the muu asuinrakennus band (0.93–2.00 %), so a kunta can raise it up to 2.00 % without any change in the law (Kiinteistöverolaki 654/1992 § 13)

---

## Section: `--rental`

### Long-term residential

- **Laki asuinhuoneiston vuokrauksesta** (481/1995, Tenancy Act), amended with effect from 1 Oct 2026
- Tenant protection moderate (less strict than DE/SE/AT)
- **Toistaiseksi voimassa oleva** (indefinite term) common
- **Määräaikainen** (fixed-term): binds both parties for the whole term; early exit only on statutory grounds, otherwise damages are usually owed. Leases made from 1 Oct 2026 may run for an agreed fixed period and then continue as indefinite; notice given during the fixed period takes effect at the earliest at its end
- **Notice periods**: tenant 1 month. Landlord, leases made from 1 Oct 2026: 4 months if the tenancy has lasted ≥ 2 years, otherwise 3 months; leases made before 1 Oct 2026: 6 months if ≥ 1 year, otherwise 3 months (2026-10-23 verified, source: KKV "Vuokrasopimuksen irtisanominen")
- **Rent levels** — free-financed (vapaarahoitteinen) average rent €/m²/month, 2026 Q3: whole country 15.99 · Helsinki 21.37 · Espoo-Kauniainen 18.86 · Vantaa 17.78 · Tampere 16.98 · Turku 15.64 · Kuopio 14.97 · Jyväskylä 14.66 · Oulu 14.19 · Lahti 13.35 · Pori 10.89; Helsinki studios (yksiöt) 26.70; year on year +0.1 % nationally, −0.2 % Helsinki (2026 data, source: Tilastokeskus StatFin `asvu` table 15fa)
- Kunta / postcode rents: `https://asuntojen.hintatiedot.fi/` (Ympäristöministeriö; average rents paid by Kela general-housing-allowance recipients, updated Feb / May / Aug / Nov)

### Short-let (Airbnb / Booking)

- **Housing company (As Oy)**: the amended asunto-osakeyhtiölaki in force since 1 Oct 2026 does not ban short-letting, but lets the yhtiökokous take a flat into the company's possession (hallintaanotto) for up to 3 years if short-letting causes the company or shareholders extra costs or harm beyond ordinary residential use, of more than minor significance (secondary: Lakitoimisto KPF quoting new AOYL 8:2 § 1 mom. 4 kohta; Suomen Kiinteistölehti partner content 12 Oct 2026 — verify at finlex.fi). Read the yhtiöjärjestys and ask the isännöitsijä about past short-let disputes before buying to short-let
- **Pending national 90-day rule — HE 83/2026 vp** (Rakentamislaki amendment, given 30 Apr 2026): short-letting = letting a furnished dwelling for under 28 days at a time; in asemakaava areas, short-letting a dwelling more than 90 days per calendar year would be a change of use needing a permit; the kunta could raise the limit up to 180 days for special local reasons; the holder must record short-let days and show them to building control on request. Excluded: ranta-asemakaava areas, vapaa-ajan asunnot anywhere, dwellings in residential use. Proposed start of the 90-day limit and record duty: 1 Jan 2027. Status: still in Ympäristövaliokunta, committee statements TaVL 20/2026 and PeVL 52/2026 issued, no committee report (mietintö); last recorded step 22 Oct 2026, when the committee asked the Ministry of the Environment for a supplementary response — final text may differ (source: eduskunta.fi HE 83/2026 vp)
- **EU Regulation 2024/1028** (STR data sharing): applies since 20 May 2026; as a Regulation it needs no transposition. Opt-in/opt-out: a Member State need not set up STR registration, but any registration scheme or platform-data request must go through the Regulation (European Commission DG GROW news, 20 May 2026). HE 83/2026 uses a day-count record duty, not a registration scheme

### Tax on rental

- **Pääomatulo (capital income)**: 30 % up to €30k, 34 % above (2026-10-23 verified, source: vero.fi Pääomatulot)
- **Vähennykset** (deductions): kunnossapito, korjaukset, hoitovastike (pääoma- / rahoitusvastike only where the As Oy books it as income, not where it is capitalised), korot on the loan taken to acquire the rental property
- **Kalustevähennys** (furnished let — optional lump sum instead of actual furnishing costs): €40/month for a furnished room or studio, €60/month for a two-room or larger flat; occasional letting €1.30/day or €2.00/day (2026-10-23 verified, source: vero.fi syventävä ohje "Vuokratulojen verotus")
- **Sähkölämmitys** (electric heating) typically not deductible separately
- **No de-minimis exemption for rental income** — all rent is capital income (30 %/34 %), reportable even when net is zero after deductions (2026-05-27 verified, source: vero.fi rental-income guidance)

---

## Section: `--work=<profession>`

### Job platforms

- **Työmarkkinatori** (national public job-market service, © KEHA-keskus): `https://tyomarkkinatori.fi/` — TE-toimistot were abolished when public employment services moved to municipalities on 1 Jan 2025 (45 työllisyysalueet); `te-palvelut.fi` and `mol.fi` now redirect here (2026-10-23 verified, sources: Kuntaliitto "TE-palvelut 2024 -uudistus"; tyomarkkinatori.fi)
- **LinkedIn FI**, **Duunitori**, **Oikotie työpaikat**, **Indeed.fi**
- **Monster.fi**

### Self-employment

- **Toiminimi (sole trader)**: simplest
- **Osakeyhtiö (Oy / Ltd)**: **no minimum share capital since 1 Jul 2019** (previously €2,500); Oyj (public Ltd) still €80,000 (2026-10-23 verified for the current rule, source: Suomi.fi company-formation guide; 2019 date per Waselius)
- **YEL** (yrittäjän eläkevakuutus) pension insurance mandatory once the YEL työtulo (assessed value of the entrepreneur's work input, not taxable earnings) exceeds **€9,423.09/yr**; YEL työtulo ceiling €214,000 (2026 data, source: Eläketurvakeskus ETK)
- **Sairausvakuutus** + **TyEL/YEL** social
- **Verohallinto Y-tunnus** business ID needed

### Salary benchmarks (2024 data — latest Tilastokeskus palkkarakenne release)

- Median total monthly earnings (kokonaisansio), full-time employees, by maakunta — regional, not city-level (2024 data, source: Tilastokeskus StatFin table 15b2):
  - Whole country: €3,615
  - Uusimaa (incl. Helsinki): €3,967
  - Pirkanmaa (incl. Tampere): €3,558; Varsinais-Suomi (incl. Turku): €3,435
  - Lowest maakunnat: Etelä-Pohjanmaa €3,286, Pohjois-Karjala €3,315, Etelä-Savo €3,348
- **No statutory minimum wage** (set per industry by union agreement)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SYKE (Suomen ympäristökeskus)** | `https://www.syke.fi/` | Environment institute |
| **Tulvakartta** (flood maps) | `https://www.vesi.fi/vesitieto/tulvakarttapalvelu/` | Q10/Q100/Q1000 flood hazard |
| **GTK (Geologinen tutkimuskeskus)** | `https://gtk.fi/` | Geology, radon |
| **STUK (Säteilyturvakeskus)** | `https://www.stuk.fi/` | Radon program |
| **STUK Radonkartta** | `https://stuk.fi/en/radon-in-finland` | Indoor radon levels — Finland highest in EU |
| **Ilmatieteen laitos (FMI)** | `https://www.ilmatieteenlaitos.fi/` | Climate, weather |
| **Ympäristöministeriö** | `https://www.ymparisto.fi/` | Aggregated environment portal |

### Specific risks

- **Tulva (flooding)** — coastal Helsinki + Espoo, lake/river plains; Vuoksi basin (East FI)
- **Radon — HIGHEST INDOOR LEVELS IN EU** on average:
  - **Pirkanmaa, Päijät-Häme, Itä-Uusimaa, Etelä-Karjala, Kanta-Häme** worst-affected
  - ~est. 7-9 % of single-family houses exceed the WHO 100 Bq/m³ reference level (per STUK radon program — see source table above; verify specific figure/year at stuk.fi)
  - Mandatory testing in some kunnat
- **Earthquake** — very low (stable Fennoscandian Shield)
- **Roudan aiheuttama vaurio** (frost heave) — ground freezing affects shallow foundations
- **Lumikuorma** (snow load) — heavy winters can cause roof collapse (esp. flat roofs)
- **Maaston eroosio** (coastal erosion) — Baltic Sea coastline
- **Luonnonpalo (wildfires)** — increasing climate risk
- **Sea-level rise** + **post-glacial rebound**: net effect varies (positive uplift in Lapland, negative on south coast)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, weak insulation |
| **1960s–1980s "betonilähiö"** (concrete suburbs) | Asbestos very common (joints, isolation), low energy efficiency |
| **1980s–2000s** | Improved insulation, modern wiring, formaldehyde from particleboard |
| **Post-2010 (E-luokka)** | Energy efficiency standards |
| **Post-2017 nZEB** | Strict |

**Asbestos**: pre-1994 buildings highly likely (banned 1994); removal ~est. €30–€80/m² (see FI 2026 cost benchmarks below).

**Putkiremontti (pipe renovation)**: ~50-year cycle for stamb (vertical pipe runs); buildings 1960s-1970s coming due now or already done; **cost per apartment €30,000-80,000+** for full renovation.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energiatodistus** (energy certificate) | All sales since 2009 | 10 years |
| **Kuntotutkimus** (condition study) | Strongly recommended; sometimes required | Per case |
| **Asbestikartoitus** (asbestos survey) | Pre-1994 buildings during renovation | Per case |
| **Yhtiöjärjestys** + **isännöitsijän todistus** | If As Oy | At sale |
| **Yhtiön tilinpäätös** + **toimintakertomus** + **kunnossapitosuunnitelma** | If As Oy | At sale |
| **Kaupanvahvistajan todistus** | All sales | At signing |

### As Oy diligence (CRITICAL)

Before buying any As Oy apartment, demand:
1. **Yhtiöjärjestys** — articles of association
2. **Isännöitsijän todistus** (manager's certificate, valid 3 months)
3. **3-vuoden tilinpäätös** + **toimintakertomus**
4. **PTS (Pitkän tähtäimen kunnossapitosuunnitelma)** — long-term maintenance plan
5. **Yhtiölaina** (building debt allocated to your share) — often €30k–€100k+
6. **Tulevat hankkeet** — upcoming putkiremontti, julkisivu, katto

**Red flags**: yhtiölaina > €100k/apt without recent renovation, deferred putkiremontti for 1970s building, monthly yhtiövastike >€8/m².

### Climate change projections (FMI)

- +2.0–4.0 °C by 2050 (RCP scenarios)
- More precipitation: winter rain increasing (less snow)
- Sea-level rise (south coast): partial offset by isostatic rebound (north)
- Drought: rare but increasing summer events
- Forest fires: rising
- Permafrost retreat in Lapland

---

## Section: `--mains`

### Sources

- **Vesilaitosyhdistys (VVY)**: `https://www.vvy.fi/` — national water utility association
- Each kunta manages own vesilaitos + viemärilaitos
- Major: **HSY** (Helsinki region — Helsinki + Espoo + Vantaa + Kauniainen), **Tampereen Vesi**, **Turun Seudun Vesi**, **Oulun Vesi**

### Verification

- Most populated areas: kunnan mains universal
- Rural + mökki: own **porakaivo** (drilled well) + **saostuskaivot** (septic)
- **Hajajätevesiasetus** (Government Decree 157/2017): strict requirements for cottages — must comply by 31 Oct 2019 (extensions possible)

### Costs

| Scenario | Cost (€) |
|---|---:|
| Liittymismaksu (mains connection) | 5,000–15,000 |
| Saostuskaivo upgrade compliant | 5,000–15,000 |
| Pienpuhdistamo (small treatment plant) | 8,000–18,000 |
| Porakaivo (drilled well) | 6,000–12,000 |

---

## Cost benchmarks (FI 2026)

| Work | Cost (€) — est. market range unless a source is given |
|---|---:|
| Energiatodistus | 300–700 |
| Kuntotarkastus (condition survey) | 400–800 |
| Kuntotutkimus (deeper) | 1,000–3,000 |
| Asbestikartoitus | 200–500 |
| Kaupanvahvistaja (public purchase witness) | 143 (2026 data, source: MML price list) |
| Maanmittauslaitos lainhuuto (title registration, kiinteistö) | 172 (2026 data, source: MML) |
| MML ownership registration (As Oy osakehuoneisto) | 92 (from 1 Jan 2026, was 89; source: MML) |
| **Varainsiirtovero (kiinteistö)** | **3 % of price** |
| **Varainsiirtovero (As Oy shares)** | **1.5 % of price** |
| **Total transaction cost (kiinteistö)** | **est. ≈ 3.1–3.5 %** of price (3 % + €362 fixed fees, €250k → €80k; see `--tax`) |
| **Total transaction cost (As Oy)** | **est. ≈ 1.5–1.6 %** of price (1.5 % + €92, €250k → €80k; see `--tax`) |
| Saostuskaivo upgrade compliant | 5,000–15,000 |
| Roof (steel sheet, 150 m²) | 15,000–30,000 |
| Asbestos removal (200 m²) | 4,000–10,000 |
| Putkiremontti per apartment (As Oy) | 30,000–80,000 |
| Energy retrofit (Class C → A) | 40,000–90,000 |

## Active fiscal incentives (2026-2027)

- **Kotitalousvähennys** (household tax deduction), temporarily raised for 2026–2027: **40 %** of the labour share bought from a company (or 15 % of wages + employer costs if hiring directly); **max €2,100/yr per person** (€4,200 for a couple, 2 × €2,100; an excess over one spouse's cap moves automatically to the other); €150 self-pay per person. Oil-heating removal: **60 %** (company) / 30 % (wages), **max €3,500/yr per person**, until end-2027 (2026 data, source: vero.fi "Kotitalousvähennyksen määrä", updated 13 Oct 2026)
- **Asuntoremontin verovähennys**: included in kotitalousvähennys
- **Energia-avustus 2026–2027** (Varke — Valtion tukeman asuntorakentamisen keskus; ara.fi now redirects to varke.fi): for housing companies and owners of state-subsidised rental / right-of-occupancy housing, not individual homeowners; up to 50 % of approved costs, **max €4,000 per apartment**, for work raising energy efficiency ≥ 10 % beyond the legal minimum; applications open from 28 Sep 2026 (Varke news, updated 29 Sep 2026, quoting the draft terms of the decree issued 10 Sep 2026 — check final terms on varke.fi)
- **Lämpöpumppu-avustus** (heat-pump grant) for individual homeowners: none listed by Varke — its only open grant for individuals is the repair grant for elderly / disabled occupants, and the energy grant for individuals (2020–2023 work) has ended (varke.fi, read 2026-10-23); for oil-heating removal use the 60 % kotitalousvähennys rate above
- **Aurinkosähkö** (PV solar) support for individual homeowners: data not publicly available — no PV grant is listed by Varke (read 2026-10-23); verify at vero.fi (kotitalousvähennys) / varke.fi
- **ASP** (asuntosäästöpalkkio, first-home savings scheme; new legislation in force 1 Jun 2026): first-time buyers aged 18+ (15–17 under conditions) save ≥ **10 %** of the price on an ASP account; the ASP loan gets a free state guarantee of up to 25 % of outstanding capital (max €60,000) and an interest subsidy of 70 % of the rate above 3.8 % for up to 10 loan years; max term 25 years (29 with instalment-free periods) (2026 data, source: Valtiokonttori ASP page, updated 5 Aug 2026). Further changes (maximum loan amount, term up to 40 years) were decided in the spring 2026 spending-limits session; entry-into-force date not yet confirmed (Valtiokonttori ASP-reform page, read 2026-10-23) — draft bill YM013:00/2026, verify at ym.fi
- **Asuntolainan valtiontakaus** (state guarantee on an owner-occupied housing loan; any buyer, home in Finland outside Åland, year-round use): up to 20 % of outstanding capital, max €60,000 per home; one-off fee 2.5 % of the guarantee (none on ASP loans); max term 25 years (29 with instalment-free periods) (2026 data, source: Valtiokonttori, updated 2 Jun 2026)

## Common listing platforms

- **Etuovi.com** — biggest, full extraction
- **Oikotie** — major listings portal (`https://asunnot.oikotie.fi/`)
- **Vuokraovi** — rentals
- **OP Koti** (formerly OPKK), **Sp-Koti**, **Habita**, **Aktia LKV** — agency networks
- **Tori.fi** — private sellers; **Huutokaupat.com** — online auctions, incl. Ulosottolaitos (enforcement) sales of seized kiinteistöt and asunto-osakkeet (2026-10-23 verified, source: huutokaupat.com listings)

## Caveats unique to FI

- **As Oy ownership is share-based** — you own shares in a housing company, NOT the apartment directly. Yhtiövastike covers maintenance + utilities + sometimes mortgage of building.
- **Yhtiöjärjestys** (articles of association) defines share rights — must read before buying
- **Yhtiölaina** (allocated building debt) often hidden cost: total apartment "real cost" = listing price + share of yhtiölaina
- **Kuntotutkimus + isännöitsijän todistus** = key due-diligence documents for As Oy purchase
- **Putkiremontti** cycle ~50 years — 1970s buildings approaching this can have €30-80k assessment per apartment
- **Highest indoor radon in EU** — no radon test is required at sale: under Säteilylaki 859/2018 the radon-measurement duties fall on employers (workplaces, § 155) and on premises open to the public (§ 156) in the places listed in § 155(1); for homes, § 158 obliges the building's owner and occupier to keep indoor radon as low as possible in the circumstances, judged against a reference value (viitearvo) (Finlex, read 2026-10-23). A pre-purchase radon measurement is still advisable, especially in Pirkanmaa / Etelä-Karjala (regional emphasis not re-verified — check the kunta at stuk.fi)
- **Mökkikulttuuri** (cottage culture) — secondary-home market huge; **vapaa-ajan asunto kiinteistövero up to 2 %** (significant)
- **Rauhoitusalueet** (protected areas) — strict construction limits
- **Sähkölämmitys** (electric heating) common in older houses — high running costs vs heat pump retrofit
- **Varainsiirtovero reduced 2024** — buyer-side costs now lower
- **No notary** in real estate transactions — handled by kaupanvahvistaja
- **Two official languages**: documents may need Swedish translation in bilingual kunnat (Helsinki/Espoo + Pohjanmaa coast)
- **Kotipaikkavaatimus** (residence requirement): some As Oy require permanent residence — affects investment buyers
- **AOYL (asunto-osakeyhtiölaki 1599/2009, in force 1 Jul 2010)** governs As Oy; its consolidated text (latest amendment 535/2026, in force 1 Oct 2026) lets the company take a flat into its own possession (hallintaanotto, ch. 8) when short-letting causes the company or shareholders extra costs or nuisance beyond residential use (Finlex, read 2026-10-23)
- **Non-EU/EEA buyers need a permit for a kiinteistö** — under Laki kiinteistöhankintojen valvonnasta 470/2019 (in force 1 Jan 2020) a non-EU/EEA citizen, an entity domiciled outside the EU/EEA, or an EU/EEA entity in which such a person holds ≥ 10 % of the votes may acquire a kiinteistö in Finland only with a puolustusministeriö (Ministry of Defence) permit, applied for before the transfer or within 2 months of it; if refused, the property must be sold within 6 months of the decision becoming final. Since 15 Jul 2025 § 5 a adds absolute bars to a permit tied to states named by government decree, with a carve-out for holders of a Finnish permanent residence permit or a Finnish-issued EU long-term resident permit. The Act does not apply in Åland (Finlex 470/2019, read 2026-10-23)

## Reddit / forum sources

- **r/Finland**, **r/AskFinland**, **r/Helsinki**
- **r/Suomi** (Finnish-language)
- **Vauva.fi forum** (Finnish discussion incl. property)
- **Oikotie investor guides** (asunnot.oikotie.fi "Vinkit ja oppaat" — listing-platform tier, not independent)
- Expat: **r/Finland**; English-language news: **Yle News** `https://yle.fi/news` (public broadcaster — news, not a forum)

## Verification authorities

| Authority | When to call |
|---|---|
| **Maanmittauslaitos** | Title verification, kiinteistö data |
| **Kunta rakennusvalvonta** | Permits, asemakaava |
| **Verohallinto** | Kiinteistövero, varainsiirtovero |
| **Kaupanvahvistaja** | Final transfer (purchase witness) |
| **Vesilaitos kunta** | Mains drains verification |
| **As Oy isännöitsijä** | If apartment: financials, planned projects |
| **STUK** | Radon information |
| **GTK** | Geology |
| **SYKE / ELY-keskus** | Floods, environment |

## Quirks to know

- **Kiinteistö vs As Oy** distinction is fundamental (freehold vs share-based)
- **Lainhuutotodistus** (title certificate) for kiinteistö
- **Osakekirja** (share certificate) for As Oy — being replaced by electronic ownership records in Maanmittauslaitos's huoneistotietojärjestelmä, the register of housing companies, ownership and pledges (MML)
- **Hallinnanjakosopimus** (subdivided occupancy agreement) for split apartments
- **Tonttioikeusvuokrasopimus** (ground lease) — common in Helsinki city land
- **Asunnon hallintaoikeus** transfers to buyer once kauppa finalised
- **Asuntokauppalaki 843/1994** (housing-trade act) protects buyers of new As Oy flats during the construction phase (RS-järjestelmä) (Finlex)
- **Vakuutus pakollinen** (insurance mandatory) for mortgage holders typically

## Source URL templates

| Source | URL pattern |
|---|---|
| Maanmittauslaitos | `https://www.maanmittauslaitos.fi/` |
| Etuovi | `https://www.etuovi.com/<kaupunki>` |
| Oikotie | `https://asunnot.oikotie.fi/<kaupunki>` |
| Tilastokeskus | `https://stat.fi/` |
| Tulvakartta | `https://www.vesi.fi/vesitieto/tulvakarttapalvelu/` |
| GTK | `https://gtk.fi/` |
| STUK Radon | `https://stuk.fi/en/radon-in-finland` |
| Verohallinto Kiinteistövero | `https://www.vero.fi/henkiloasiakkaat/asuminen/kiinteistovero/` |
| Liikennetilanne | `https://www.liikennetilanne.fi/` |

## Status

✅ **Fully populated** as of 2026-04-25. Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for the cadastre and transaction-cost facts re-fetched 2026-10-23 (varainsiirtovero 3 % / 1.5 %, kiinteistövero statutory bands, MML fees, pääomatulo 30 % / 34 %; Maanmittauslaitos + Verohallinto definitive), for `--work` and for the Active fiscal incentives figures. MEDIUM for `--price` (As Oy and small-house figures are Tilastokeskus / MML 2025 data; mökki row est.), for `--risks` + `--mains` (radon, flood maps, asbestos dates and HSY tariffs re-verified; putkiremontti, yhtiölaina and private-system cost ranges unsourced) and for the kiinteistövero reform shelving (government decision of 1 Sep 2026; the valtioneuvosto.fi release could not be re-read on 2026-10-23). MEDIUM for short-let regulation: HE 83/2026 vp (90-day permit threshold, raisable by the kunta to 180 days, plus a record-keeping duty, both proposed from 1 Jan 2027) is still in Ympäristövaliokunta with no committee report — on 22 Oct 2026 the committee asked the Ministry of the Environment for a supplementary response — so the final text may differ (eduskunta.fi, read 2026-10-23); EU Reg 2024/1028 has applied since 20 May 2026 and is opt-in for Member States, so nothing is pending transposition (European Commission, 20 May 2026). LOW for the construction and survey rows in Cost benchmarks (est. market ranges).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Työmarkkinatori replaces TE-toimisto and MOL.fi; YEL threshold €9,423.09 (2026, ETK); Tilastokeskus 2024 maakunta medians; Oy / Oyj capital rule (Suomi.fi); "no statutory minimum wage" rests on secondary search results only |
| Active fiscal incentives | 2026-10-23 | 2026-10-23 refresh wave | Kotitalousvähennys 2026–2027 (vero.fi); energia-avustus (Varke); ASP and housing-loan state guarantee (Valtiokonttori); PV support marked data not publicly available |
| Foreign-buyer rule (non-EU/EEA permit bullet under Caveats only) | 2026-10-23 | 2026-10-23 refresh wave | Laki kiinteistöhankintojen valvonnasta 470/2019, amended by 328/2025 (Finlex); the rest of Caveats is not re-verified |

## Extension TODOs

- [ ] Per-kunta kiinteistövero rate tables
- [ ] As Oy yhtiöjärjestys red-flag detection (kotipaikkavaatimus, short-let restrictions) + the statutory short-let hallintaanotto ground (AOYL 8 luku 2 § 1 mom. 4 kohta: the yhtiökokous can take a flat into the company's possession for up to 3 years; in force 1 Oct 2026 via amendment 535/2026, Finlex)
- [ ] Putkiremontti cycle estimate per building age + region
- [ ] Tulvakartta address-level lookup
- [ ] Radon zone overlay per kunta
- [ ] Yhtiölaina / debt-tied-to-shares calculation tooling
- [ ] Mökki-specific tax + utility decision tree
- [ ] Bilingual kunnat (Swedish-required documents)

## Update history

- **2026-04-25** — Initial population
- **2026-10-23** — Refresh wave; per section, facts changed / confirmed / unverifiable:
  - Country profile 1 / 5 / 2 — 309 → 308 kuntaa (Tilastokeskus 2026)
  - `--price` 24 / 7 / 5 — As Oy €/m² and small-house figures replaced with Tilastokeskus (13mx, 13mu, 15hw) and MML 2025 data; OmaKiinteistö and Hintaseuranta sources removed, Bjäkari dropped, OPKK → OP Koti; mökki row kept as est.
  - `--rental` 10 / 3 / 3 — Tenancy Act amendment of 1 Oct 2026; As Oy short-let hallintaanotto ground (AOYL, 1 Oct 2026); HE 83/2026 vp 90-day cap recorded as pending; pääomatulo 30 % / 34 % reconfirmed
  - `--work` 6 / 5 / 2 — Työmarkkinatori replaces TE-toimisto / MOL.fi; YEL threshold €9,423.09; Tilastokeskus 2024 maakunta medians
  - Common listing platforms 4 / 4 / 1 — OPKK → OP Koti, Bjäkari and the Hintaseuranta claim removed; Reddit / forum sources 3 / 2 / 3 — The Local Finland and two dead blogs removed
  - `--tax` 17 / 11 / 4 — 2026 kiinteistövero bands, valuation basis and instalments; valuation reform not taken forward this term (1 Sep 2026 decision); kaupanvahvistaja €143, lainhuuto €172, As Oy registration €92; buyer-side totals recomputed; VAT list corrected
  - Cost benchmarks 4 / 2 / 9 — fiscal rows updated; construction and survey rows labelled est.
  - Active fiscal incentives 5 / 0 / 1 — kotitalousvähennys 40 % / €2,100 for 2026–2027; energia-avustus via Varke; ASP and housing-loan state guarantee; unsourced PV deduction replaced with "data not publicly available"
  - Caveats 2 / 3 / 1, plus foreign-buyer rule 1 / 0 / 0 — radon-test claim corrected against Säteilylaki 859/2018; AHL → AOYL 1599/2009 with amendment 535/2026; non-EU/EEA permit rule (470/2019) added
  - Quirks 2 / 1 / 2 — ASREK → MML huoneistotietojärjestelmä; Pakettilaki → Asuntokauppalaki 843/1994
  - `--traffic` 3 / 1 / 2 — Liikennevirasto → Väylävirasto (2019); Fintraffic Liikennetilanne
  - `--risks` 9 / 6 / 14 — STUK radon (home average ≈ 94 Bq/m³), Tulvakartta, land uplift and sea level, asbestos dates, energiatodistus and asbestikartoitus rows; FMI climate projections 2 / 1 / 3 (2022 SSP2-4.5 figures)
  - `--mains` 7 / 3 / 4 — VVY URL, Turku utilities, hajajätevesi scope, HSY 2026 / 2027 connection fees
  - Verification authorities 1 / 6 / 2 — ELY-keskus → elinvoimakeskus; Source URL templates 2 / 5 / 2 — vero.fi path, Fintraffic URL
  - Totals 103 changed / 65 confirmed / 60 unverifiable. Playbook-level date left at 2026-04-25: `--price`, `--tax`, `--rental`, `--risks` and `--mains` still carry unverified items (mökki prices, agent fee, putkiremontti / yhtiölaina and private-system cost ranges); re-verified sections are dated in the Per-section verification table.
