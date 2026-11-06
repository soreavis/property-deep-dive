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
- **KTJ Kiinteistörekisteri** (cadastre records): lainhuutotodistus (certificate of title), rasitustodistus (mortgages and encumbrances) and kiinteistörekisteriote (cadastre extract) €16 each via the NLS e-service, €19 from customer service or the online form; huoneistotietojärjestelmä extracts and share lists for As Oy flats cost the same; no VAT (2026 data, source: Maanmittauslaitos price list, charges from 1 Jan 2026)
- **Maanmittauslaitos — Kiinteistökauppojen tilastopalvelu (REST)**: `https://khr.maanmittauslaitos.fi/tilastopalvelu/rest/1.1/` — open, no registration; sale counts, median and mean prices by kunta, maakunta and postcode for asuinpientalo, lomakiinteistö and other property types, from the kauppahintarekisteri; representative sales only, real property only (no As Oy shares, no houses on leased plots), no figure where a cell has fewer than 3 sales (source: Maanmittauslaitos service description)
- **Tilastokeskus — Osakeasuntojen hinnat** (StatFin `ashi`): old As Oy dwelling €/m² by kunta (table 13mx) and postcode (table 13mu), annual + quarterly — API `https://pxdata.stat.fi/PxWeb/api/v1/fi/StatFin/ashi/`
- **Tilastokeskus — Kiinteistöjen hinnat** (StatFin `kihi`): old detached-house €/m² and floor area by area class (table 15hw)

### Listing platforms

- **Etuovi.com** — self-described as Finland's largest property search with over 100,000 listings, while Oikotie calls itself Finland's most popular housing service; competing self-descriptions, not a market-share measure (sites, Nov 2026, listing platform ⚠️): `https://www.etuovi.com/`
  - Search by kunta + alueet + asunto-tyyppi
- **Oikotie**: `https://asunnot.oikotie.fi/`
- **Vuokraovi.com** (rentals)
- **Habita, Sp-Koti, OP Koti** (formerly OPKK; `opkk.fi` redirects to `op-koti.fi`) — agency networks
- **Kiinteistömaailma**, **Huoneistokeskus** — nationwide agency chains (self-described: Kiinteistömaailma agents in over 100 localities, Huoneistokeskus hundreds of professionals across Finland; agency sites, Nov 2026 ⚠️)

### 2025 price benchmarks (Tilastokeskus + Maanmittauslaitos)

As Oy column: old (resale) As Oy dwellings, 2025 annual average €/m², all house types (2025 data, source: Tilastokeskus StatFin tables 13mx by kunta and 13mu by postcode). Small-house column, city rows: median sale price of built asuinpientalo properties (own plot) in asemakaava areas, 2025, representative sales only; 65 (Mikkeli) to 255 (Vantaa) sales per city, so treat single-city medians as indicative; means run higher, e.g. Helsinki €535,186, Tampere €363,485 (2025 data, source: Maanmittauslaitos kauppahintarekisteri, Kiinteistökauppojen tilastopalvelu REST indicators 2311 / 2313 / 2314). The two municipality-size rows (Tilastokeskus 15hw) and the leisure row carry their own sources. Municipal / postcode figures, not a valuation of any specific property.

| Region | As Oy €/m² (2025 avg) | Asuinpientalo, asemakaava area (2025; city rows median) |
|---|---:|---:|
| **Helsinki** | 4,983 (kerrostalo flats 5,225; central postcodes 00100–00180 flats 6,493–9,653 by postcode and flat size) | median €468,500 |
| **Espoo** | 3,773 | median €612,500 |
| **Vantaa** | 2,675 | median €368,000 |
| **Tampere** | 2,979 | median €310,000 |
| **Turku** | 2,653 | median €272,500 |
| **Oulu** | 2,105 | median €254,000 |
| **Jyväskylä** | 2,038 | median €215,500 |
| **Kuopio** | 2,086 | median €207,000 |
| **Rovaniemi** | 1,953 | median €169,000 |
| **Lahti** / **Pori** | 1,675 / 1,325 | median €165,000 / €125,000 |
| Kouvola / Kotka / Mikkeli | 1,088 / 1,184 / 1,459 | median €97,500 / €91,000 / €152,000 |
| Municipalities 20,000–59,999 inhabitants (Tilastokeskus class) | — | est. ≈ €228,000 old detached house (1,810 €/m² × 125.7 m², 2025 sales-weighted, Tilastokeskus table 15hw) |
| Municipalities < 20,000 inhabitants (Tilastokeskus class) | — | est. ≈ €130,000 old detached house (1,128 €/m² × 114.9 m², 2025 sales-weighted, Tilastokeskus table 15hw) |
| Leisure property (lomakiinteistö, built, under 2 ha), whole country | — (MML gives whole-property prices for built leisure properties, not €/m²) | median €92,000 with own shore in yleis- or ranta-asemakaava areas (2,741 sales; Uusimaa €183,000 from 109 sales, Lappi €60,000 from 111), €74,000 with own shore in haja-asutusalue (851); without own shore €55,000 in yleis- or ranta-asemakaava areas (617) and €33,000 in haja-asutusalue (730); resort holiday flats held as As Oy shares are not included (2025 data, source: Maanmittauslaitos kauppahintarekisteri, REST indicators 5111–5513) |

**Trend**: old As Oy prices 2026 Q3 (preliminary) −3.2 % year on year nationally, −2.2 % Helsinki, −2.2 % Tampere, −0.8 % Oulu; Q3 average 2,432 €/m² nationally, 4,811 €/m² Helsinki (2026 data, source: Tilastokeskus StatFin table 15is, release of 28 Oct 2026). Preliminary quarters get revised: Q2 2026 nationally now reads −4.0 % (earlier release −3.9 %).

### Compute

1. Listing €/m² = price / **asuinpinta-ala** (area of the living spaces). A sale ad by an agent or other business must state it with the room count, and the brochure must split area into living spaces and other spaces (source: Finlex, Valtioneuvoston asetus asuntojen markkinoinnissa annettavista tiedoista 130/2001, 2 § and 7–8 §). Tilastokeskus measures a dwelling's area from the inner surfaces of its bounding walls, counting utility rooms, bathrooms and sauna but not garage, cellar, cold storage, balcony or porch (source: Tilastokeskus käsitteet, "Asunnon pinta-ala")
2. **Trap**: asuinpinta-ala vs huoneistoala vs **kerrosala** (gross floor area, bounded by the outer wall surfaces, so larger than the living area); for a kesämökki Tilastokeskus uses kerrosala as the area. Huoneistoala has no single meaning: Tilastokeskus defines it per statistic, so ask how a listing's figure was measured (source: Tilastokeskus käsitteet, "Kerrosala", "Asunnon pinta-ala", "Huoneistoala")
3. **As Oy math**: you buy **shares** (osake) in housing company; each share = € amount; **yhtiövastike** (monthly fee) covers building maintenance + sometimes shared mortgage
4. **Yhtiölaina** (housing company loan) tied to apartment — apartment carries portion of building debt

---

## Section: `--traffic`

### Primary sources

- **Väylävirasto** (Finnish Transport Infrastructure Agency; Liikennevirasto became Väylävirasto on 1 Jan 2019): `https://vayla.fi/` — road statistics (tietilastot) + open data (source vayla.fi; 2026-10-23 verified)
- **Fintraffic Liikennetilanne** (official real-time traffic situation service, linked from vayla.fi): `https://liikennetilanne.fintraffic.fi/`
  - LAM automatic traffic counts (volumes + speeds by vehicle class from road loops) as open data via Fintraffic Digitraffic: `https://www.digitraffic.fi/tieliikenne/` (source digitraffic.fi; 2026-10-23 verified)
  - `https://www.liikennetilanne.fi/` is a privately run site (Youlearn it Oy) that reuses Fintraffic weather-camera data — not an authority source
- **Traficom** (Finnish Transport and Communications Agency — licensing, registration, supervision): `https://www.traficom.fi/`

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

**Valuation reform**: at its 1 Sep 2026 budget session the Orpo government decided to keep studying the kiinteistövero valuation reform but not to take it forward in the 2023–2027 electoral term, citing too little time for owners to prepare; the study is left to the next government (2026 data, source: valtioneuvosto.fi budget-session release "Orpon hallitus: Talous kasvaa, ja hallitus vauhdittaa kasvua täsmätoimilla", 1 Sep 2026, archived 2026-09-01). The 2027 budget proposal (given 21 Sep 2026) lists no kiinteistövero change among its 2027 tax measures (budjetti.vm.fi). A kunta can still raise its rate within the bands above.

**Bills**: the decision is sent in March to whoever owned the property on 1 Jan; a tax of €170 or more is split automatically into two instalments, with due dates set by the month the owner's kiinteistöverotus ends — for most owners August + October (6 Aug / 6 Oct 2026) or September + November (7 Sep / 6 Nov 2026); every assessment ends by 31 Oct, so the latest pair is 7 Dec 2026 + 8 Feb 2027 (2026 data, source: vero.fi Kiinteistövero and Maksuohjeet pages, updated 24 Apr 2026 / 1 Jan 2026).

**Exemptions**: metsämaa, maatalousmaa and joutomaa can be exempt from kiinteistövero when they belong to a maatilakiinteistö (farm property); a property under 2 ha is generally not treated as a farm (vero.fi Maapohja page, updated 9 Feb 2026; Kiinteistöverolaki 654/1992 excludes forest and agricultural land from the tax).

### Transaction taxes — Varainsiirtovero (REFORM 2024)

**MAJOR REDUCTION 1 January 2024** (retroactive from 12 Oct 2023 — the rate follows the signing date of the final binding deed; real-estate transfers signed before 12 Oct 2023 stay at 4 %; vero.fi detailed guidance issued 29 Jan 2026):

| Asset | Old rate | **2024+ rate** |
|---|---:|---:|
| **Kiinteistö (real estate)** | 4.0 % | **3.0 %** |
| **Asunto-osakeyhtiö (As Oy) shares** | 2.0 % | **1.5 %** |
| **Kiinteistöyhtiö shares** (keskinäinen kiinteistöosakeyhtiö, other real-estate companies) / **other securities** (e.g. liikeosakkeet) | 2.0 % / 1.6 % | **1.5 %** for both (deeds signed from 12 Oct 2023; law in force 1 Jan 2024) (2026 data, source: vero.fi syventävä ohje "Varainsiirtovero arvopapereiden luovutuksessa", VH/6665/00.01.00/2025, issued 1 Jan 2026 — also the source for the As Oy 2.0 % → 1.5 % row) |

**First-time buyer exemption ABOLISHED** from 1 Jan 2024 — the 0 % treatment for 18–39-year-old first-time buyers now applies only where the binding deed was signed before 1 Jan 2024 (vero.fi first-time-buyer guidance).

### Notary / title

- **No notary** in Finland real estate; transactions handled by **kaupanvahvistaja** (purchase witness)
- Kaupanvahvistajan palkkio: **€143** per purchase or other conveyance; a deed made in MML's electronic Kiinteistövaihdannan palvelu instead costs a **€236** service fee that includes the lainhuuto fee (2026 data, source: MML price list, read 2026-10-23)
- Maanmittauslaitos lainhuuto (title registration, kiinteistö): **€172**, unchanged on 1 Jan 2026; kiinnitys (mortgage-deed confirmation) €47; As Oy purchase: ownership registration in MML's huoneistotietojärjestelmä **€92** per osakehuoneisto, up from €89 (2026 data, source: MML fee notice of 17 Dec 2025)
- Real estate agent (välittäjä) fee: no statutory tariff — the commission is agreed with the agency, must be reasonable (kohtuullinen) and can be charged only to the toimeksiantaja (Laki kiinteistöjen ja vuokrahuoneistojen välityksestä 1074/2000 § 20, Finlex), most often the seller (huoneistokeskus.fi). Example list price: Huoneistokeskus 4.95 % of the velaton hinta incl. 25.5 % ALV "or as agreed", minimum €3,765–€5,020 incl. ALV depending on region (2026 data, source: huoneistokeskus.fi price list ⚠️ — one agency, undated page, list price before negotiation); negotiated fees **est. 2.5–4.0 %** of price (curated range, wisdom, not data — not drawn from any published market average; VAT basis unstated)

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
- Among the **lower** in the EU after the 2024 reform (curated comparison — wisdom, not data)

### Future risk

- Kiinteistövero valuation reform: not taken forward in the 2023–2027 term (government decision at the 1 Sep 2026 budget session; source valtioneuvosto.fi release of 1 Sep 2026, archived 2026-09-01); any revival depends on the government formed after the Eduskunta election of 18 Apr 2027 (election day is the third Sunday of April under Vaalilaki 714/1998, Finlex; 18 Apr is that Sunday in 2027) — verify against the government programme agreed after that election
- ALV: the general rate rose 24 % → 25.5 % on 1 Sep 2024 and the reduced rate fell 14 % → 13.5 % on 1 Jan 2026 (vero.fi)
- Vapaa-ajan asunto: taxed in the muu asuinrakennus band (0.93–2.00 %), so a kunta can raise it up to 2.00 % without any change in the law (Kiinteistöverolaki 654/1992 § 13)

---

## Section: `--rental`

### Long-term residential

- **Laki asuinhuoneiston vuokrauksesta** (481/1995, Tenancy Act), amended with effect from 1 Oct 2026
- Tenant protection moderate (less strict than DE/SE/AT) — curated comparison, wisdom, not data
- **Toistaiseksi voimassa oleva** (indefinite term) common
- **Määräaikainen** (fixed-term): binds both parties for the whole term; early exit only on statutory grounds, otherwise damages are usually owed. Leases made from 1 Oct 2026 may run for an agreed fixed period and then continue as indefinite; notice given during the fixed period takes effect at the earliest at its end
- **Notice periods**: tenant 1 month. Landlord, leases made from 1 Oct 2026: 4 months if the tenancy has lasted ≥ 2 years, otherwise 3 months; leases made before 1 Oct 2026: 6 months if ≥ 1 year, otherwise 3 months (2026-10-23 verified, source: KKV "Vuokrasopimuksen irtisanominen")
- **Rent levels** — free-financed (vapaarahoitteinen) average rent €/m²/month, 2026 Q3: whole country 15.99 · Helsinki 21.37 · Espoo-Kauniainen 18.86 · Vantaa 17.78 · Tampere 16.98 · Turku 15.64 · Kuopio 14.97 · Jyväskylä 14.66 · Oulu 14.19 · Lahti 13.35 · Pori 10.89; Helsinki studios (yksiöt) 26.70; year on year +0.1 % nationally, −0.2 % Helsinki (2026 data, source: Tilastokeskus StatFin `asvu` table 15fa)
- Kunta / postcode rents: `https://asuntojen.hintatiedot.fi/` (Ympäristöministeriö; average rents paid by Kela general-housing-allowance recipients, updated Feb / May / Aug / Nov; source: asuntojen.hintatiedot.fi service page, 2026)

### Short-let (Airbnb / Booking)

- **Housing company (As Oy)**: the amended asunto-osakeyhtiölaki in force since 1 Oct 2026 does not ban short-letting, but lets the yhtiökokous take a flat into the company's possession (hallintaanotto) for up to 3 years if short-letting causes the company or shareholders extra costs or harm beyond ordinary residential use, unless the breach is only of minor significance, and only after a written warning from the hallitus that is also served on the tenant (source: Finlex, asunto-osakeyhtiölaki 1599/2009 8 luku 2 § 1 mom. 4 kohta and 3 §, as amended by 535/2026). Read the yhtiöjärjestys and ask the isännöitsijä about past short-let disputes before buying to short-let
- **Pending national 90-day rule — HE 83/2026 vp** (Rakentamislaki amendment, given 30 Apr 2026): short-letting = letting a furnished dwelling for under 28 days at a time; as given, short-letting a dwelling in an asemakaava area more than 90 days per calendar year would be a change of use needing a permit, but Ympäristövaliokunta's report YmVM 12/2026 vp (5 Nov 2026) rewrites this to meet PeVL 52/2026: up to 90 days per calendar year is not a substantial change of use, and above 90 days the need for a permit is decided case by case under Rakentamislaki 42 § 3 mom. 3 kohta; the kunta could raise the 90 days up to 180 for special local reasons; the holder must record short-let days and show them to building control on request. Excluded: ranta-asemakaava areas, vapaa-ajan asunnot anywhere, dwellings in residential use. The report also deletes the 1 Jan 2027 start of the 90-day rule and record duty, so they would start with the rest of the act on a date still blank, and proposes a resolution that the government prepare a short-let registration duty, in use by the end of 2027. Status: committee stage finished with a dissent (vas, vihr, sd, kesk), plenary readings still to come, NOT passed — final text may differ (source: eduskunta.fi HE 83/2026 vp, processing record of 5 Nov 2026, and YmVM 12/2026 vp)
- **EU Regulation 2024/1028** (STR data sharing): applies since 20 May 2026; as a Regulation it needs no transposition. Opt-in/opt-out: a Member State need not set up STR registration, but any registration scheme or platform-data request must go through the Regulation (European Commission DG GROW news, 20 May 2026). HE 83/2026 uses a day-count record duty, not a registration scheme

### Tax on rental

- **Pääomatulo (capital income)**: 30 % up to €30k, 34 % above (2026-10-23 verified, source: vero.fi Pääomatulot)
- **Vähennykset** (deductions): kunnossapito, korjaukset, hoitovastike (pääoma- / rahoitusvastike only where the As Oy books it as income, not where it is capitalised), korot on the loan taken to acquire the rental property (claimed under Velan korot, not under Vuokratulot); vuosikorjaus is deducted in the year paid; perusparannus the landlord pays on an As Oy flat goes in 10-year straight-line instalments, on a let building (kiinteistö) it is added to the building's acquisition cost and depreciated at 4 % a year of the undepreciated balance (residential building), or in either case deducted at sale (2026 data, source: vero.fi "Vähennykset", updated 26 May 2026)
- **Kalustevähennys** (furnished let — optional lump sum instead of actual furnishing costs): €40/month for a furnished room or studio, €60/month for a two-room or larger flat; occasional letting €1.30/day or €2.00/day (2026-10-23 verified, source: vero.fi syventävä ohje "Vuokratulojen verotus")
- **Sähkö- ja lämpömaksut** (electricity and heating charges) the landlord pays are deductible, like water, waste-water and road charges, kiinteistövero and vuosikorjausmenot; if only part of the home is let, only the let share counts, split by floor area or, for shared rooms, per occupant (2026 data, source: vero.fi syventävä ohje "Vuokratulojen verotus", VH/7418/00.01.00/2025 of 12 Jan 2026, § 3.2–3.3)
- **No de-minimis exemption for rental income** — all rent is capital income (30 %/34 %), reportable even when net is zero after deductions (2026 data, source: vero.fi "Ilmoitus- ja maksuohjeet": rental income and its costs must always be reported, even when no tax remains after deductions)

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

### Salary benchmarks (2024 data — latest Tilastokeskus palkkarakenne release) — rates/figures may have changed since

- Median total monthly earnings (kokonaisansio), full-time employees, by maakunta — regional, not city-level (2024 data, source: Tilastokeskus StatFin table 15b2) — rates/figures may have changed since:
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
| **Tulvakartta** (flood maps) | `https://www.vesi.fi/vesitieto/tulvakarttapalvelu/` | Flood hazard maps by return period (e.g. 1/100a = 1 % annual probability): hazard + risk maps for significant flood-risk areas drawn up by the elinvoimakeskukset, hazard maps for 100+ other areas and the whole coast; mostly exclude climate change, so not a basis for minimum building heights (source vesi.fi; 2026-10-23 verified) |
| **GTK (Geologinen tutkimuskeskus)** | `https://gtk.fi/` | Geology, radon |
| **STUK (Säteilyturvakeskus)** | `https://www.stuk.fi/` | Radon program |
| **STUK — Radon in Finland** | `https://stuk.fi/en/radon-in-finland` | Indoor radon — Finnish homes average ≈ 94 Bq/m³; higher than in most other countries (2026 data, source STUK; 2026-10-23 verified) |
| **Ilmatieteen laitos (FMI)** | `https://www.ilmatieteenlaitos.fi/` | Climate, weather |
| **Ymparisto.fi** (environmental administration web service; the ministry itself is at `https://ym.fi/`) | `https://www.ymparisto.fi/` | Aggregated environment portal |

### Specific risks

- **Tulva (flooding)** — 18 merkittävää tulvariskialuetta (significant flood-risk areas) for 2024–2030, named by the Ministry of Agriculture and Forestry (MMM) on 19 Dec 2024: 4 coastal (Hamina–Kotka, Helsinki–Espoo, Turku, Kemi) and 14 on rivers — lower Kymijoki; Kokemäenjoki (Huittinen, Pori); Lapväärtinjoki-Isojoki (Lapväärtti); Laihianjoki (Laihia-Tuovila-Runsor); Kyrönjoki (Ilmajoki-Seinäjoki, Ylistaro-Koivulahti); Kalajoki (Alavieska-Ylivieska); lower Pyhäjoki; Iijoki (Pudasjärvi); Tornionjoki-Muonionjoki (Tornio); Kemijoki (Rovaniemi, Kittilä); Ivalojoki (Ivalo). Pori (river delta + sea) is among the worst, Rovaniemi the worst inland; the Vuoksi basin is not on the list. Harmful floods can also happen outside these areas, and hulevesi (stormwater) flooding is managed by the kunta (2024 data, source vesi.fi / SYKE "Tulvariskialueet" + 2024–2030 map, vesi.fi "Tulvariskien hallinta"; 2026-10-23 verified) — rates/figures may have changed since
- **Radon — Finland has higher indoor radon than most other countries**; average in homes ≈ **94 Bq/m³** (2026 data, source STUK "Radon in Finland"; 2026-10-23 verified):
  - Highest bedrock/soil uranium: **Lahti region (Päijät-Häme), Itä-Uusimaa, Kymenlaakso**; lowest: Pohjois-Karjala, Kainuu, Pohjois-Pohjanmaa. Houses on gravel/sand ridges (harjut) read clearly higher than neighbours on other soils; STUK recommends measuring everywhere in Finland (source STUK)
  - Reference levels: **300 Bq/m³** for dwellings, **200 Bq/m³** for designing and building new buildings (STM decree 1044/2018; source STUK; 2026-10-23 verified). WHO recommends a national reference level of 100 Bq/m³, at most 300 Bq/m³ (2023 data, source WHO radon fact sheet) — rates/figures may have changed since
  - Share of homes above 300 Bq/m³: data not publicly available on the STUK pages checked — verify at stuk.fi
  - No measurement duty for private homes. Employers must measure workplaces in municipalities / postcodes where more than 10 % of earlier measurements exceed 300 Bq/m³; STUK's list includes e.g. Helsinki, Espoo, Vantaa, Tampere, Lahti, Hämeenlinna, Kouvola, Kotka, Lappeenranta, Jyväskylä (Radiation Act 859/2018; source STUK workplace-radon pages; 2026-10-23 verified). Municipality / postcode level only — never a parcel-level reading
- **Earthquake** — very low (stable Fennoscandian Shield) (qualitative — wisdom, not data)
- **Roudan aiheuttama vaurio** (frost heave) — ground freezing affects shallow foundations (qualitative — wisdom, not data)
- **Lumikuorma** (snow load) — heavy winters can cause roof collapse (esp. flat roofs) (qualitative — wisdom, not data)
- **Maaston eroosio** (coastal erosion) — Baltic Sea coastline (qualitative — wisdom, not data)
- **Luonnonpalo (wildfires)** — climate change raises forest-fire risk in Fennoscandia, although annual burned areas have stayed small in recent decades (2022 data, source FMI + Ministry for Foreign Affairs infographic on ilmasto-opas.fi, based on FMI Reports 2021:3) — rates/figures may have changed since
- **Sea-level rise** + **post-glacial rebound**: land uplift ~90 cm per century in Merenkurkku (Kvarken), ~40 cm per century in Helsinki. South-coast sea level is no longer falling and is turning to rise; in the northern Gulf of Bothnia land still rises faster than the sea. 2100 vs present, south coast: +5–15 cm (low emissions), +20–30 cm (medium), +50–60 cm (high); Perämeri: sea level falls 20–30 cm (medium) (2025 data, source FMI ilmasto-opas.fi) — rates/figures may have changed since

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, weak insulation |
| **1960s–1980s "betonilähiö"** (concrete suburbs) | Asbestos very common (joints, isolation), low energy efficiency |
| **1980s–2000s** | Improved insulation, modern wiring, formaldehyde from particleboard |
| **Permits from 1 Jul 2012 (E-luku)** | Whole-building energy limit (E-luku) for new buildings — YM decree 2/11 = RakMK D3 2012, given 30 Mar 2011, in force 1 Jul 2012; permit applications pending before 1 Jul 2012 could use the earlier rules (decree and date: Finlex regulation collection; in-force date: decree text, copy hosted by Pilkington ⚠️; 2026-10-23 verified) |
| **Permits from 1 Jan 2018 (nZEB)** | New buildings must be lähes nollaenergiarakennus (nearly zero-energy): MRL 117 g § as amended by 1151/2016 (earlier rules applied to 31 Dec 2017) + YM decree 1010/2017 (new E-luku limits) in force 1 Jan 2018; projects pending on that date stayed on the earlier rules (source Finlex; 2026-10-23 verified) |

**Asbestos**: used in Finnish construction 1922–1992, most commonly 1963–1979; manufacture/import of asbestos building materials banned from the start of 1993, sale/use from the start of 1994 (some stock may have been sold later) — treat every pre-1994 building as suspect (2026 data, source tyosuojelu.fi; 2026-10-23 verified); removal ~est. €30–€80/m² (see FI 2026 cost benchmarks below).

**Putkiremontti (pipe renovation)**: ~50-year cycle for stamb (vertical pipe runs); buildings 1960s-1970s coming due now or already done (rule of thumb — wisdom, not data). In 2025, 15 % of responding housing companies planned a domestic-water pipe renovation and 12 % a sewer renovation within the next 10 years (2025 data, source Tilastokeskus StatFin table 15ga; 2026-10-23 verified). **Cost per apartment ~est. €30,000-80,000+** for full renovation (curated range — wisdom, not data: no primary source publishes a per-flat figure; it scales with flat size, method (full linjasaneeraus vs pipe relining) and bathroom scope) — get the housing company's cost estimate per share before bidding.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energiatodistus** (energy certificate) | Required at sale or rental; energy class must appear in sale/rental ads (Act 50/2013; source ym.fi) | 10 years (source energiatodistusrekisteri.fi; 2026-10-23 verified) |
| **Kuntotutkimus** (condition study) | Strongly recommended; sometimes required | Per case |
| **Asbestikartoitus** (asbestos survey) | Pre-1994 buildings before removing or dismantling structures (new Government Decree on the Safety of Asbestos Work in force 21 Dec 2025, partly 21 Dec 2026; source tyosuojelu.fi; 2026-10-23 verified) | Per case |
| **Yhtiöjärjestys** + **isännöitsijän todistus** | If As Oy | At sale |
| **Yhtiön tilinpäätös** + **toimintakertomus** + **kunnossapitosuunnitelma** | If As Oy | At sale |
| **Kaupanvahvistajan todistus** (purchase-witness confirmation) | Kiinteistö sales on a paper deed: the kaupanvahvistaja confirms the sale with all signatories present; a deed made in the statutory electronic kaupankäyntijärjestelmä needs none, and the rule sits in Maakaari's kiinteistö chapter, so As Oy share sales are outside it (Maakaari 540/1995 2:1 §; source Finlex consolidated; 2026-10-23 verified) | At signing |

### As Oy diligence (CRITICAL)

Before buying any As Oy apartment, demand:
1. **Yhtiöjärjestys** — articles of association
2. **Isännöitsijän todistus** (manager's certificate) — content set by Asunto-osakeyhtiölaki 1599/2009 7:27 §: the company's finances, known condition of its buildings and of the flat, the owner's overdue unpaid charges, loan liabilities where they fall differently on different shares; the Act sets no validity period, so ask for a recently issued one (source Finlex consolidated; 2026-10-23 verified)
3. **3-vuoden tilinpäätös** + **toimintakertomus**
4. **PTS (Pitkän tähtäimen kunnossapitosuunnitelma)** — long-term maintenance plan; not named in the Act — the statutory minimum is the board's written report on maintenance needs for the next 5 years, plus a report on major works done, presented to every annual general meeting (AOYL 6:3 §; source Finlex consolidated; 2026-10-23 verified)
5. **Yhtiölaina** (building debt allocated to your share) — often ~est. €30k–€100k+ (curated range — wisdom, not data: no primary statistic publishes per-flat yhtiölaina; the figure scales with the company's outstanding loans and the flat's portion under the yhtiöjärjestys — read the share's portion in the isännöitsijäntodistus and the company's tilinpäätös)
6. **Tulevat hankkeet** — upcoming putkiremontti, julkisivu, katto

**Red flags**: yhtiölaina > €100k/apt without recent renovation, deferred putkiremontti for 1970s building, monthly yhtiövastike >€8/m² (thresholds are curated rules of thumb — wisdom, not data). For scale, residential hoitovastike averaged €4.49/m²/month across Finnish housing companies in 2025 — €4.88 in kerrostalo companies, €5.32 in buildings completed before 1960 — before any rahoitusvastike (loan charge) (2025 data, source Tilastokeskus StatFin table 15gi; 2026-10-23 verified).

### Climate change projections (FMI)

- Warming under SSP2-4.5, 2070–2099 vs 1981–2010: winters +2–7 °C, summers +1–5 °C; precipitation likely up in every season (best estimate winter +14 %, summer +7 %) (2022 data, source FMI release 30 Mar 2022) — rates/figures may have changed since
- More precipitation: winter rain increasing (less snow) (qualitative — wisdom, not data)
- Sea-level rise: south coast turning to rise as uplift no longer keeps pace; northern Gulf of Bothnia still emerging (figures in the sea-level bullet under Specific risks; 2025 data, source FMI ilmasto-opas.fi) — rates/figures may have changed since
- Drought: rare but increasing summer events (qualitative — wisdom, not data)
- Forest fires: rising risk (2022 data, source FMI infographic on ilmasto-opas.fi; see Luonnonpalo under Specific risks) — rates/figures may have changed since
- Permafrost retreat in Lapland (qualitative — wisdom, not data)

---

## Section: `--mains`

### Sources

- **Suomen Vesilaitosyhdistys (VVY)**: `https://vesilaitosyhdistys.fi/` (vvy.fi redirects here) — national water utility association (2026-10-23 verified)
- ~1,110 vesihuoltolaitokset (utilities) under the Water Services Act (2026 data, source SYKE via VVY "Vesihuolto Suomessa lyhyesti" ⚠️ industry association; 2026-10-23 verified); ~400 of them are municipally owned and the rest customer-owned cooperatives, and the ~80 largest supply nearly 80 % of water services (undated figures, source VVY ⚠️; read 2026-11-03)
- Major: **HSY** (Helsingin seudun ympäristöpalvelut — a kuntayhtymä whose member municipalities are Helsinki, Espoo, Vantaa and Kauniainen, with water services one of its units; drinking water for over 1 million residents per hsy.fi), **Tampereen Vesi Oy**, **Turun Vesihuolto Oy** (Turku), **Oulun Vesi** (city liikelaitos). **Turun Seudun Vesi Oy** is a wholesale artificial-groundwater company owned by 9 Turku-region kunnat — connections are made through each kunta's own utility (sources hsy.fi, tampereenvesi.fi, turunvesihuolto.fi, ouka.fi/oulun-vesi, turunseudunvesi.fi; 2026-10-23 verified)

### Verification

- Network coverage: ~90 % of Finns are on a utility water network and ~85 % on a sewer network (undated figures, source VVY "Vesihuolto Suomessa lyhyesti" ⚠️ industry association; read 2026-10-23). The owner or occupier is responsible for a property's water services; inside a utility's toiminta-alue (operating area, approved by the kunta) the property must connect to the water and sewer networks — no sewer connection is needed where there is no WC and wastewater is handled under Ympäristönsuojelulaki 527/2014, and the kunta's ympäristönsuojeluviranomainen can grant exemptions, which lapse when the property changes owner or holder or its use raises the need for the utility's services (Vesihuoltolaki 119/2001 §§ 6, 8, 10, 11; source Finlex consolidated; 2026-10-23 verified, § 11 lapse rule 2026-11-03). Ask the vesilaitos whether the parcel is inside the toiminta-alue
- Rural + mökki: own **porakaivo** (drilled well) + **saostuskaivot** (septic)
- **Haja-asutuksen jätevedet** (Ympäristönsuojelulaki 527/2014 §§ 154 b–156 d + Government Decree 157/2017): pre-2004 systems within 100 m of a water body / sea or on a water-supply groundwater area had to meet the basic treatment standard by 31 Oct 2019; elsewhere the standard applies when the system is renewed, a WC is built or permit-requiring renovation is done (156 b §); deviations possible (156 d §) (2026 data, source Finlex consolidated 527/2014; 2026-10-23 verified)

### Costs

| Scenario | Cost (€) |
|---|---:|
| Liittymismaksu (mains connection), HSY detached house, incl. 25.5 % ALV, plus separate connection-work fees | 9,538 (≤ 250 k-m²) / 16,346 (251–350 k-m²); from 1 Jan 2027: 10,213 / 17,507 (2026 data, source HSY vesihuollon hinnasto 2026 + 2027; 2026-10-23 verified) |
| Saostuskaivo upgrade compliant | ~est. 5,000–15,000 |
| Pienpuhdistamo (small treatment plant) | ~est. 8,000–18,000 |
| Porakaivo (drilled well) | ~est. 6,000–12,000 |

Connection fees are set by each kunta's utility (HSY figures apply only in its area). The other three rows are market estimates that vary with soil, depth and distance — get contractor quotes and check the kunta's ympäristönsuojelu rules.

---

## Cost benchmarks (FI 2026)

| Work | Cost (€) — est. market range unless a source is given |
|---|---:|
| Energiatodistus | ~est. 300–700 |
| Kuntotarkastus (condition survey) | ~est. 400–800 |
| Kuntotutkimus (deeper) | ~est. 1,000–3,000 |
| Asbestikartoitus | ~est. 200–500 |
| Kaupanvahvistaja (public purchase witness) | 143 (2026 data, source: MML price list) |
| Maanmittauslaitos lainhuuto (title registration, kiinteistö) | 172 (2026 data, source: MML) |
| MML ownership registration (As Oy osakehuoneisto) | 92 (from 1 Jan 2026, was 89; source: MML) |
| **Varainsiirtovero (kiinteistö)** | **3 % of price** (2026 data, source: vero.fi) |
| **Varainsiirtovero (As Oy shares)** | **1.5 % of price** (2026 data, source: vero.fi) |
| **Total transaction cost (kiinteistö)** | **est. ≈ 3.1–3.5 %** of price (3 % + €362 fixed fees, €250k → €80k; see `--tax`) |
| **Total transaction cost (As Oy)** | **est. ≈ 1.5–1.6 %** of price (1.5 % + €92, €250k → €80k; see `--tax`) |
| Saostuskaivo upgrade compliant | ~est. 5,000–15,000 |
| Roof (steel sheet, 150 m²) | ~est. 15,000–30,000 |
| Asbestos removal (200 m²) | ~est. 4,000–10,000 |
| Putkiremontti per apartment (As Oy) | ~est. 30,000–80,000 |
| Energy retrofit (Class C → A) | ~est. 40,000–90,000 |

The ~est. rows are curated 2026 ranges with no primary source behind them, not quotes; survey and contractor prices vary with region, building size, age and condition — use them as orders of magnitude and get written quotes that state whether 25.5 % ALV is included before budgeting.

## Active fiscal incentives (2026-2027)

- **Kotitalousvähennys** (household tax deduction), temporarily raised for 2026–2027: **40 %** of the labour share bought from a company (or 15 % of wages + employer costs if hiring directly); **max €2,100/yr per person** (€4,200 for a couple, 2 × €2,100; an excess over one spouse's cap moves automatically to the other); €150 self-pay per person. Oil-heating removal: **60 %** (company) / 30 % (wages), **max €3,500/yr per person**, until end-2027 (2026 data, source: vero.fi "Kotitalousvähennyksen määrä", updated 13 Oct 2026)
- **Asuntoremontin verovähennys**: included in kotitalousvähennys
- **Energia-avustus 2026–2027** (Varke — Valtion tukeman asuntorakentamisen keskus; ara.fi now redirects to varke.fi): for housing companies and owners of state-subsidised rental / right-of-occupancy housing, not individual homeowners; up to 50 % of approved costs, **max €4,000 per apartment**, for work raising energy efficiency ≥ 10 % beyond the legal minimum; applications open from 28 Sep 2026 (Varke news, updated 29 Sep 2026, quoting the draft terms of the decree issued 10 Sep 2026 — check final terms on varke.fi)
- **Lämpöpumppu-avustus** (heat-pump grant) for individual homeowners: none listed by Varke — its only open grant for individuals is the repair grant for elderly / disabled occupants, and the energy grant for individuals (2020–2023 work) has ended (varke.fi, read 2026-10-23); for oil-heating removal use the 60 % kotitalousvähennys rate above
- **Aurinkosähkö** (PV solar) support for individual homeowners: data not publicly available — no PV grant is listed by Varke (read 2026-10-23); verify at vero.fi (kotitalousvähennys) / varke.fi
- **ASP** (asuntosäästöpalkkio, first-home savings scheme; new legislation in force 1 Jun 2026): first-time buyers aged 18+ (15–17 under conditions) save ≥ **10 %** of the price on an ASP account; the ASP loan gets a free state guarantee of up to 25 % of outstanding capital (max €60,000) and an interest subsidy of 70 % of the rate above 3.8 % for up to 10 loan years; max term 25 years (29 with instalment-free periods) (2026 data, source: Valtiokonttori ASP page, updated 5 Aug 2026). Further changes (maximum loan amount, term up to 40 years) were decided in the spring 2026 spending-limits session; entry-into-force date not yet confirmed (Valtiokonttori ASP-reform page, read 2026-10-23) — draft bill YM013:00/2026, verify at ym.fi
- **Asuntolainan valtiontakaus** (state guarantee on an owner-occupied housing loan; any buyer, home in Finland outside Åland, year-round use): up to 20 % of outstanding capital, max €60,000 per home; one-off fee 2.5 % of the guarantee (none on ASP loans); max term 25 years (29 with instalment-free periods) (2026 data, source: Valtiokonttori, updated 2 Jun 2026)

## Common listing platforms

- **Etuovi.com** — self-described as Finland's largest property search (site, Nov 2026, listing platform ⚠️); full extraction
- **Oikotie** — major listings portal (`https://asunnot.oikotie.fi/`), self-described as Finland's most popular housing service (site, Nov 2026, listing platform ⚠️)
- **Vuokraovi** — rentals
- **OP Koti** (formerly OPKK), **Sp-Koti**, **Habita**, **Aktia LKV** — agency networks
- **Tori.fi** — private sellers; **Huutokaupat.com** — online auctions, incl. Ulosottolaitos (enforcement) sales of seized kiinteistöt and asunto-osakkeet (2026-10-23 verified, source: huutokaupat.com listings)

## Caveats unique to FI

- **As Oy ownership is share-based** — you own shares in a housing company, NOT the apartment directly. Yhtiövastike covers maintenance + utilities + sometimes mortgage of building.
- **Yhtiöjärjestys** (articles of association) defines share rights — must read before buying
- **Yhtiölaina** (allocated building debt) often hidden cost: total apartment "real cost" = listing price + share of yhtiölaina
- **Kuntotutkimus + isännöitsijän todistus** = key due-diligence documents for As Oy purchase
- **Putkiremontti** cycle ~50 years (rule of thumb — wisdom, not data) — 1970s buildings approaching this can have a ~est. €30-80k assessment per apartment (curated range — wisdom, not data; see `--risks`)
- **Higher indoor radon than most other countries** (STUK; see `--risks`) — no radon test is required at sale: under Säteilylaki 859/2018 the radon-measurement duties fall on employers (workplaces, § 155) and on premises open to the public (§ 156) in the places listed in § 155(1); for homes, § 158 obliges the building's owner and occupier to keep indoor radon as low as possible in the circumstances, judged against a reference value (viitearvo) (Finlex, read 2026-10-23). A pre-purchase radon measurement is still advisable, especially where the kunta or postcode is on STUK's workplace-measurement list, which spans many regions (see `--risks`; check the kunta at stuk.fi)
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
| **SYKE / elinvoimakeskus** (the 15 ELY-keskukset closed on 31 Dec 2025; 10 elinvoimakeskukset took over, environmental permits + supervision went to Lupa- ja valvontavirasto) | Floods, environment |

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
| Verohallinto Kiinteistövero | `https://www.vero.fi/henkiloasiakkaat/omaisuus/kiinteistovero/` (updated 2026-10-23) |
| Fintraffic Liikennetilanne | `https://liikennetilanne.fintraffic.fi/` (updated 2026-10-23) |

## Status

✅ **Fully populated**; fast-changing sections re-verified as of 2026-10-23, figures with no current primary source labelled est., curated wisdom or verify-at, and older-source figures marked 'may have changed since' (initial population 2026-04-25; `--price`, `--rental`, `--tax`, `--risks`, `--mains` and Cost benchmarks closed by a gap-closing pass on 2026-11-03). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for the cadastre and transaction-cost facts re-fetched 2026-10-23 (varainsiirtovero 3 % / 1.5 %, kiinteistövero statutory bands, MML fees, pääomatulo 30 % / 34 %; Maanmittauslaitos + Verohallinto definitive), for `--work`, for the Active fiscal incentives figures and for the kiinteistövero reform shelving (government decision of 1 Sep 2026, read in the valtioneuvosto.fi budget-session release through its 2026-09-01 archive). MEDIUM for `--price` (As Oy, small-house and leisure-property figures are Tilastokeskus / MML 2025 data; single-city small-house medians rest on 65–255 sales each, and the 2026 Q3 trend is preliminary) and for `--risks` + `--mains` (radon, flood maps and flood-risk areas, asbestos dates, AOYL / Maakaari / Vesihuoltolaki rules and HSY tariffs re-verified; putkiremontti, yhtiölaina and private-system cost ranges have no primary source and are labelled est. or curated). MEDIUM for short-let regulation: HE 83/2026 vp (90-day threshold, raisable by the kunta to 180 days, plus a record-keeping duty) is out of Ympäristövaliokunta: report YmVM 12/2026 vp of 5 Nov 2026 drops the automatic permit duty above 90 days and the 1 Jan 2027 start, a dissent would drop the short-let chapter, and the plenary readings are still to come, so the final text may differ (eduskunta.fi, read 2026-11-06); EU Reg 2024/1028 has applied since 20 May 2026 and is opt-in for Member States, so nothing is pending transposition (European Commission, 20 May 2026). LOW for the construction and survey rows in Cost benchmarks (est. market ranges).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Työmarkkinatori replaces TE-toimisto and MOL.fi; YEL threshold €9,423.09 (2026, ETK); Tilastokeskus 2024 maakunta medians; Oy / Oyj capital rule (Suomi.fi); "no statutory minimum wage" rests on secondary search results only |
| Active fiscal incentives | 2026-10-23 | 2026-10-23 refresh wave | Kotitalousvähennys 2026–2027 (vero.fi); energia-avustus (Varke); ASP and housing-loan state guarantee (Valtiokonttori); PV support marked data not publicly available |
| Foreign-buyer rule (non-EU/EEA permit bullet under Caveats only) | 2026-10-23 | 2026-10-23 refresh wave | Laki kiinteistöhankintojen valvonnasta 470/2019, amended by 328/2025 (Finlex); the rest of Caveats is not re-verified |
| `--price` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Small-house column re-sourced from Yle to MML kauppahintarekisteri 2025 medians (city cells relabelled median; Lahti, Pori, Kouvola, Kotka and Mikkeli added); est. mökki row replaced by MML leisure-property medians; KTJ extract fees (MML 2026 price list) and Compute area terms (Finlex VNA 130/2001, Tilastokeskus) sourced; trend moved to 2026 Q3 preliminary (15is); Etuovi, Oikotie and agency claims labelled self-descriptions |
| `--rental` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Landlord-paid electricity and heating corrected to deductible (vero.fi syventävä ohje § 3.3); perusparannus split into As Oy 10-year instalments vs kiinteistö depreciation; AOYL short-let ground re-sourced to Finlex (8:2 § 1 mom. 4 kohta and 8:3 §, as amended by 535/2026); HE 83/2026 status (last step 22 Oct 2026, no mietintö) and the no-de-minimis line re-read; tenant-protection comparison labelled wisdom |
| `--tax` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Reform shelving read in the valtioneuvosto.fi release of 1 Sep 2026 (archived 2026-09-01); pre-2024 rates confirmed in the vero.fi syventävä ohje and the row label corrected (real-estate-company shares 2.0 %, other securities 1.6 %); agent fee re-based on Laki 1074/2000 § 20 plus one agency list price ⚠️; "lower in the EU" labelled wisdom; buyer-side totals recomputed |
| Cost benchmarks (FI 2026) | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Fiscal rows confirmed (MML €143 / €172 / €92; vero.fi 3 % / 1.5 %); nine construction and survey rows labelled ~est. with a calibration sentence |
| `--risks` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | 18 significant flood-risk areas for 2024–2030 (MMM, 19 Dec 2024) replace the hotspot list; E-luku (1 Jul 2012) and nZEB (1 Jan 2018) era dates; kaupanvahvistaja scope (Maakaari 2:1 §); isännöitsijän todistus content (AOYL 7:27 §, no validity period) and the 5-year maintenance report (6:3 §); putkiremontti, yhtiölaina and red-flag figures labelled est. or curated, with StatFin 15ga / 15gi context; the renovation-loan guarantee proposal (YM013:00/2026) is not yet in As Oy item 5 |
| `--mains` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | HSY member municipalities confirmed (hsy.fi); "each kunta its own vesilaitos" and "mains universal" replaced by VVY utility counts and network coverage (⚠️ industry association) and Vesihuoltolaki §§ 6, 8, 10, 11 (Finlex); private-system cost rows stay ~est. |

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
  - Totals 103 changed / 65 confirmed / 60 unverifiable. Playbook-level date re-stamped 2026-10-23: every fast-changing section is now re-verified — `--work` in the refresh, `--price`, `--rental`, `--tax`, Cost benchmarks, `--risks` and `--mains` in the gap-closing pass below; re-verified sections are dated in the Per-section verification table.
  - Gap-closing pass, run 2026-11-03 (confirmed / changed / relabelled): `--price` 0 / 14 / 5; `--rental` 4 / 2 / 1; `--tax` 2 / 1 / 2; Cost benchmarks 2 / 0 / 2; `--risks` 0 / 5 / 6; `--mains` 1 / 2 / 0 — all six closed; total 9 / 24 / 16. Main changes: small-house column re-sourced to MML kauppahintarekisteri 2025 medians and the est. mökki row replaced by MML leisure-property medians; trend moved to 2026 Q3 (preliminary); landlord-paid electricity and heating corrected to deductible; pre-2024 transfer-tax row label corrected; 18 significant flood-risk areas for 2024–2030 replace the hotspot list; the isännöitsijän todistus '3 months' validity removed (AOYL 7:27 § sets none); VVY utility counts and Vesihuoltolaki duties replace 'mains universal'; construction, survey, putkiremontti and yhtiölaina figures labelled est. or curated
