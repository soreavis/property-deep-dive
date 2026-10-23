# Sweden 🇸🇪 — Property Due-Diligence Playbook

ISO2: `se`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits with space `NNN NN` (e.g., `111 29` Stockholm centro, `411 18` Göteborg, `211 22` Malmö)
- **Admin levels**: 21 län (counties) + 290 kommuner (municipalities) + ~2,500 distrikt (registration districts based on the parish division of 31 Dec 1999; församlingar were used in folkbokföring until end-2015) (2026 data, source: SCB geografiska indelningar; Skatteverket)
- **Currency**: **SEK** (Swedish krona); 1 EUR = 11.11 SEK on 22 Oct 2026; monthly averages 10.64–11.23 in Jan–Sep 2026, after annual averages of 11.43 (2024) and 11.07 (2025) — the krona strengthened into Feb 2026, then weakened again through Sep 2026 (2026 data, source: ECB euro reference rates)
- **Languages**: Swedish (principal language, Språklag 2009:600 § 4); national minority languages Finnish, Yiddish, Meänkieli, Romani chib and Sami (§ 7) (source: riksdagen.se, SFS 2009:600)
- **Cadastre**: **Lantmäteriet** (national land survey + registration agency)
- **Identifier**: fastighetsbeteckning (e.g., `Stockholm Vasastaden 1:1` = `<kommun> <traktnamn> <blocknr:enhetsnr>`)
- Distinct ownership types: **äganderätt** (freehold villa/townhouse), **bostadsrätt** (cooperative apartment — most apartments), **hyresrätt** (rental apartment, regulated), **tomträtt** (leasehold ground from kommun, common in older Stockholm/Göteborg)

## Section: `--price`

### Primary sources

- **Lantmäteriet "Min fastighet"**: `https://www.lantmateriet.se/sv/fastighet-och-mark/information-om-fastigheter/Min-fastighet/` — own-property full extracts, requires BankID
- **Lantmäteriet open data**: `https://geotorget.lantmateriet.se/`
- **SCB (Statistiska centralbyrån) Fastighetspriser**: `https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/fastigheter/fastighetspriser-och-lagfarter/` — småhus price index Q3 2026 (preliminary) 986 (1981=100), +4 % y/y and +2 % q/q (2026 data, source: SCB, published 23 Oct 2026)
- **Svensk Mäklarstatistik**: `https://www.maklarstatistik.se/` — sales reported daily by brokers from ~1,500 offices (secondary aggregator, per maklarstatistik.se 2026)
- **Värderingsdata** + **Booli Pris** valuation tools

### Listing platforms

- **Hemnet** — dominant: 82 % of 2025 home sales (139,063 of SCB's 170,415) were advertised on Hemnet, down from 86–90 % in 2019–2024 (2025 data, preliminary until Jul 2027; source: Hemnet Group press release 3 Jul 2026, company-reported against SCB): `https://www.hemnet.se/`
  - Includes "Salda objekt" (sold prices) searchable per kommun + område
  - URL: `https://www.hemnet.se/bostader?location_ids[]=<id>&item_types[]=bostadsratt|villa|...`
- **Booli** (part of SBAB's services; operated by Booli Search Technologies AB, per booli.se 2026): `https://www.booli.se/` — sold prices map + valuation
- **Blocket Bostad**: `https://www.blocket.se/bostad` — rentals only, now merged into **Qasa** (`https://qasa.com/se/sv`); not a for-sale channel (per blocket.se/bostad, 2026)
- Agency networks: **Fastighetsbyrån** (largest), **Svensk Fastighetsförmedling**, **Mäklarhuset**, **Notar** (Stockholm, central Sweden + Skåne), **SkandiaMäklarna**

### Price benchmarks (bostadsrätt: Svensk Mäklarstatistik, rolling 12 months, update of 8 Oct 2026; villa: SCB 2025)

| Region | Bostadsrätt SEK/m² | Villa avg total (SEK) |
|---|---:|---:|
| **Stockholm inner city** (Kungsholmen → Vasastan-Norrmalm) | 110,000–131,000 | n/a |
| Stockholm kommun overall | 90,815 | 8,850,000 |
| Stockholm suburbs (other kommuner in Stockholms län) | 25,000–67,000 | 3,574,000 (Norrtälje) – 13,813,000 (Danderyd) |
| **Göteborg** | 51,948 | 7,154,000 |
| **Malmö** | 36,364 | 6,284,000 |
| Uppsala, Lund | 40,000–45,000 | 5,042,000–5,782,000 |
| Linköping, Västerås, Örebro | 22,000–32,000 | 3,850,000–4,425,000 |
| Smaller cities (Gävle, Karlstad, Sundsvall) | 16,000–28,000 | 2,669,000–3,543,000 |
| Norrland (rural inland/border kommuner, Norrbotten + Jämtland) | 2,700–7,300 (1–51 sales per kommun) | 642,000–1,434,000 |
| Sommarstuga (fritidshus) | n/a | 1,565,000 (Övre Norrland) – 4,401,000 (Stockholms län); national avg 2,519,000 |

Kommun / district averages, not parcel values. Bostadsrätt = broker-reported sales over a rolling 12 months (2026 data, secondary aggregator; Svensk Mäklarstatistik area pages updated 8 Oct 2026); Stockholm suburbs span Nynäshamn 25,317 – Lidingö 66,107. Rural Norrland bostadsrätt values rest on 1–51 sales per kommun in 12 months; Svensk Mäklarstatistik treats fewer than 25 sales as too few for statistical relevance. Villa = SCB average köpeskilling for permanent småhus excl. tomträtt; fritidshus = SCB regional averages (2025 data, source: SCB Statistikdatabasen TAB1169 + TAB1152). Ski resorts break the Norrland pattern (Åre bostadsrätt 60,152 SEK/m², rolling 12 months, update of 8 Oct 2026).

### Compute

1. Listing SEK/m² = price / **boarea (BOA)**, the legal living area definition
2. **Trap**: BOA + biarea (BIA: basement, garage, attic) = useful total but not for €/m² comparison
3. **Trap**: Bostadsrätt has **andelstal** (share %) determining BRF voting rights + monthly avgift portion
4. **Bostadsrätt math**: monthly **avgift** (€100–€800/mo typical) covers BRF mortgage + maintenance — affects "true" cost
5. Tomträtt apartments: separate **tomträttsavgäld** (ground rent, increases periodically)

---

## Section: `--traffic`

### Primary sources

- **Trafikverket**: `https://www.trafikverket.se/` — federal road authority
- **NVDB (Nationell vägdatabas)**: `https://nvdb.trafikverket.se/` — open data, all road counts
- City traffic: Stockholm `https://www.stockholm.se/`, Göteborg, Malmö city portals

### Key term

**ÅDT (årsdygnstrafik)** = AADT-equivalent; sometimes "**ÅMDT**" (årsmedeldygnstrafik) — daily-average for the year

### Verdict bands (SE coastal/urban-typical)

- 🟢 < 1,000 v/d (residential gata, lokal väg)
- 🟡 1,000–8,000 v/d (länsväg, urban arterial)
- 🟠 8,000–30,000 v/d (motorväg/E-road, inner ring)
- 🔴 > 30,000 v/d (E4/E6/E18, central Stockholm/Göteborg/Malmö)

---

## Section: `--tax`

### Annual property charge — Fastighetsavgift (CAPPED)

**Sweden has a unique CAP-based property charge** (replaced traditional property tax for residential in 2008):

**Småhus (villa, 2025–2026)**:
- 0.75 % of taxeringsvärde (assessed value, set at 75 % of the probable market value in the property's värdeområde two years before the taxation year; next småhus taxering 2027, at the 2025 price level) (2026 data, source: Skatteverket)
- **Cap: SEK 10,074/year (2025) / SEK 10,425/year (2026)** — index-linked to inkomstbasbelopp annually (2026 data, source: Skatteverket)
- New builds with värdeår 2012 or later: no fastighetsavgift at all for the first 15 years (no taper); värdeår 2011 or earlier had 5 years free + 5 years at half (2026 data, source: Skatteverket)

**Bostadsrätt** (apartment in BRF):
- BRF pays 0.3 % of the taxeringsvärde (building + land), capped at **SEK 1,724 per apartment (2025) / SEK 1,784 (2026)** — a BRF building is taxed as a hyreshus (2026 data, source: Skatteverket)
- **Included in monthly avgift** to BRF
- Individual owner doesn't pay separately

**Hyreshus** (apartment building):
- 0.3 % of taxeringsvärde, capped at SEK 1,724/yr per residential unit (2025) / SEK 1,784 (2026); new residential units with värdeår 2012 or later pay nothing for 15 years (2026 data, source: Skatteverket)

**Effectively very low** — for a SEK 5M villa, est. taxeringsvärde ~SEK 3.75M (75 % × 5M) × 0.75 % = ~SEK 28,125, capped at SEK 10,425/yr (2026) — so you pay the cap (≈ €940 at the ECB reference rate of SEK 11.112/EUR on 22 Oct 2026), regardless of value. A capped charge rather than an ad-valorem tax, so high-value homes pay far less proportionally than under classical property tax.

### Transaction taxes

- **Stämpelskatt** (stamp duty on lagfart, canonical Lantmäteriet/Skatteverket term): **1.5 % of price for privatpersoner / bostadsrättsföreningar / kommuner; 4.25 % for juridiska personer** (AB, HB, ekonomiska föreningar) + **expeditionsavgift SEK 825** (lagfart application fee, separate from stamp duty, charged even when no stamp duty is due). Tax base = the higher of the purchase price and the previous year's taxeringsvärde, rounded down to whole thousands (2026 data, source: Lantmäteriet)
  - For real estate (fastighet)
  - For bostadsrätt: no lagfart and no stämpelskatt; the BRF may charge an överlåtelseavgift (and a pantsättningsavgift) only if its stadgar provide for it, at the level the stadgar set — read them before signing (Bostadsrättslag 1991:614, 7 kap. 14 §; a later wording, Lag 2026:486, in force on a date the government sets, drops the pantsättningsavgift) (2026 data, source: riksdagen.se)
- **Pantbrev** (mortgage deed): **2 % stämpelskatt on the new inteckning amount** (whole thousands, rounded down) + expeditionsavgift SEK 375 per inteckning (only on new pantbrev; existing pantbrev pass with the property) (2026 data, source: Lantmäteriet)
- **No general transfer tax** beyond lagfart
- **Mäklare** (broker): **2–4 %** typical, paid by seller; negotiable

### Capital gains

- **Reavinstskatt 22 %** on profit (gain) — effective rate = 30 % capital-income tax on 22/30 of the gain for a privatbostad; a loss is 50 % deductible (2026 data, source: Skatteverket)
- **Uppskov** (deferral): can defer if buying a replacement primary residence (Sweden / EEA); a new uppskovsbelopp is min SEK 50,000 and max SEK 3,000,000; for a 2026 sale the replacement must be bought between 1 Jan 2025 and 31 Dec 2027 and moved into by 2 May 2028. **Interest-free from income year 2021** (the ~0.5 %/yr uppskovsränta was abolished) — no annual cost, but the deferred gain is taxed at the rate in force when the uppskov is reversed, which Skatteverket warns may differ from 22 % (2026 data, source: Skatteverket)
- **Undersökningsplikt — Jordabalken 4 kap. 19 § andra stycket** (canonical caveat-emptor anchor): buyer loses right to price reduction / rescission for any defect they should have detected through ordinary inspection — duty is *långtgående* (far-reaching) per SE doctrine + case law. Besiktning is the only practical defence (source: riksdagen.se / lagen.nu).
- **Privatbostad** (primary residence) deduction methods + reno tracking

### VAT (moms)

- 25 % standard
- 12 % reduced (restaurant / café service, hotel room letting)
- 6 % super-reduced (food incl. takeaway from 1 Apr 2026; books; domestic passenger transport)
- Sale or letting of property, residential or commercial: VAT-exempt
- Commercial letting: 25 % on the rent only where the landlord opts in (frivillig beskattning, tenant running a VAT-liable business) (2026 data, source: Skatteverket)

### Future risk

- Periodic political debate about reintroducing classical property tax (would hit Stockholm/Göteborg homeowners hard)
- Pantbrev system stable
- No transfer tax changes pending

---

## Section: `--rental`

### Long-term residential

- **Hyresreglering** (rent control) — STRICT especially in major cities
- **Bruksvärdesystem**: rent set by negotiation between Hyresgästföreningen + Fastighetsägarna; newbuilds can use **presumtionshyra** (negotiated rent set for the first 15 years), and since 1 Jan 2026 landlords have more room to adjust it during that period (2026 data, source: Riksdag decision 2025/26:CU5, 19 Nov 2025)
- **First-hand contract (förstahandskontrakt)** in regulated rental: hard to obtain — Stockholm's Bostadsförmedlingen let 20,861 homes in 2025, with an average queue time of 9.0 years for ordinary rentals and 12.4 years within Stockholms stad (2025 data, source: Bostadsförmedlingen i Stockholm)
- **Andrahandsuthyrning** (subletting your own bostadsrätt): still needs consent from the BRF board or hyresnämnden and a reason for subletting; before the reform most BRFs granted one year and then often refused further sublets; since 1 Jul 2026 hyresnämnden can grant permission for longer periods than were normally given, and earlier sublets count against a new application only if they were substantial (bostadsrättslagen 7 kap. 11 §; Prop. 2025/26:187; Riksdag decision 2025/26:CU31, 20 May 2026)
- **Privatuthyrningslag (2026:772)**, in force 1 Jul 2026, replaced lagen (2012:978) om uthyrning av egen bostad, which still governs contracts made under it: covers a private person or dödsbo letting a house or part of a house (e.g. an apartment) as a home, up to two lettings outside their own home; not a hyresrätt sublet and not leisure lets. Rent is agreed freely, but hyresnämnden can cut a rent that is *väsentligt högre* than for comparable homes; 3-month notice for both sides on open-ended contracts (source: SFS 2026:772 via data.riksdagen.se; Riksdag decision 2025/26:CU31, 20 May 2026)

### Short-let (Airbnb, Booking)

- **Hemförsäkring** disclosure required
- **BRF approval** typically required for cooperative apartments — most BRFs ban or strictly limit short-let
- **Stockholm + Göteborg**: no city-level cap yet but BRF rules + tax authority tightening
- **EU Regulation 2024/1028** (short-term-rental data sharing): an EU regulation applying since 20 May 2026, so nothing to transpose. A Member State needs a registration procedure only if it requires platforms to transmit data; Sweden has introduced none, and has no rules restricting short-let supply on housing-supply grounds (2026 data, source: Regeringskansliet faktapromemoria 2026/27:FPM1, 14 Oct 2026). Watch: the Commission's proposed affordable-housing regulation COM(2026) 599 (9 Sep 2026) would set an EU framework for local short-let limits; Swedish remiss runs to 14 Nov 2026 (same source)
- Income tax: standard deduction (schablonavdrag) **SEK 40,000/yr per dwelling** (not per person), plus 20 % of the rent for a villa/ägarlägenhet or the BRF avgift for the let period of a bostadsrätt; rent below that total is effectively tax-free, and any surplus is capital income (2026, source: Skatteverket "Hyra ut privatbostad")

### Tax on rental

- Surplus after the deductions: 30 % tax on capital income (2026 data, source: Skatteverket Belopp och procent 2026)
- Computed example: villa let for SEK 50,000/yr → deduction 40,000 + 20 % × 50,000 = 50,000 → taxable surplus SEK 0 (rules: Skatteverket "Hyra ut privatbostad")
- Residential commercial-style rental: subject to standard tax + sometimes moms

---

## Section: `--work=<profession>`

### Job platforms

- **Arbetsförmedlingen Platsbanken** (state): `https://arbetsformedlingen.se/`
- **LinkedIn SE**, **Indeed.se** (Monster ceased its European operations, including Sweden, in Jul–Aug 2025 — source: Eurofound restructuring event 203161)
- **Saco Lönesök** (academic salary database; open search gives a rough estimate, simple and advanced search only for members of a Saco union — source: saco.se, 2026)
- Profession unions (SACO, LO, TCO confederations)

### Self-employment regimes

- **Enskild firma** (sole trader): simplest, no min capital
- **Aktiebolag (AB)**: min SEK 25,000 share capital for a privat AB, lowered from 50,000 on 1 Jan 2020 (Prop. 2019/20:21) (2026, source: Bolagsverket)
- **F-skattsedel** registration via Skatteverket
- **Egenavgifter** (self-employed social): 28.97 % of the business surplus (full rate, born 1959 or later; same total in 2025 and 2026) (2026 data, source: Skatteverket)
- **A-kassa** unemployment fund (voluntary)

### Salary benchmarks (2025)

- National monthly gross (full-time equivalent, all sectors): **median SEK 38,300**, average 42,900; 10th percentile 28,000, 90th percentile 61,700 (2025 data, source: SCB lönestrukturstatistik, table TAB5709)
- Average (not median) monthly gross by NUTS2 region:
  - Stockholm: SEK 48,300
  - Västsverige (incl. Göteborg): SEK 42,300; Sydsverige (incl. Malmö): SEK 41,700
  - Östra Mellansverige: SEK 40,500; Övre Norrland: SEK 40,100; Småland med öarna: SEK 39,500
  - Norra Mellansverige: SEK 39,200; Mellersta Norrland: SEK 39,100 (2025 data, source: SCB table TAB5881)
- No statutory minimum wage (set per industry by union agreement)
- Non-EU work permits: salary of at least 90 % of the median, SEK 34,470/month from 16 Jun 2026 (2026 data, source: Migrationsverket)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SMHI** (meteorology + hydrology) | `https://www.smhi.se/` | Real-time + forecasts + hist. floods |
| **MSB (Myndigheten för samhällsskydd och beredskap)** | `https://www.msb.se/` | Risk maps, civil protection |
| **MSB Översvämningskartor** | `https://www.msb.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/` | Flood hazard maps |
| **SGU (Sveriges geologiska undersökning)** | `https://www.sgu.se/` | Geology, radon, sinkhole maps |
| **SSM (Strålsäkerhetsmyndigheten)** | `https://www.stralsakerhetsmyndigheten.se/` | Radon program |
| **Boverket** | `https://www.boverket.se/` | Building regulations, BBR/BEN |
| **Klimatanpassning (SMHI)** | `https://www.klimatanpassning.se/` | Climate adaptation portal |
| **SGI (Statens geotekniska institut)** | `https://www.sgi.se/` | Landslide + slope stability |

### Specific risks

- **Skred (landslides)** — Vänern + Vättern shores, **Göta älv valley** (severe quick-clay zones, similar to Norway), west coast
- **Översvämning (flooding)** — coastal + lake-shore + river plains; Mälaren risk for Stockholm
- **Stigande havsnivå** (sea-level rise) — south + west coast (Skåne, Halland, Bohuslän)
- **Skogsbrand (forest fire)** — increasing climate risk; Sala 2014, Ljusdal 2018 disasters
- **Radon** — significant in granite areas (Småland, Bergslagen, Uppland, Stockholm bedrock); Sweden's measurement program is comprehensive
- **Earthquake** — very low (Sweden on stable Baltic Shield)
- **Storm/strong wind** — Atlantic depressions Skåne, Halland; Storm Hans (2023), Storm Eowyn (2025) reminders
- **Strandskyddszon** (shoreline protection): 100m default, can be 300m sensitive — restricts construction near waters
- **Saltvattensinträngning** (saltwater intrusion) — coastal wells affected

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, weak insulation |
| **1965–1974 "miljonprogrammet"** | Panel concrete, asbestos in joints, energy-inefficient — major retrofit cost |
| **1974–1989** | Asbestos still common, improving insulation |
| **1989–2000** | Better insulation, modern wiring; some PCB issues in fugemassa (sealants) |
| **Post-2008** | BBR + BEN energy standards; BBR 2020 stricter |
| **Post-2017 nZEB** | Low-energy required for new builds |

**Asbestos**: pre-1992 likely; **PCB in fugemassa** (caulking, expansion joints) banned 1973 but present in 1955-1973 builds.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energideklaration** (energy declaration) | All sales since 2009 | 10 years; penalty up to SEK 10,000 |
| **Lagfartsbevis** | Title verification | At sale |
| **Fastighetsutdrag** (property extract) | All sales | At sale |
| **Besiktning** (independent survey) | NOT mandatory but strongly recommended | Per case |
| **Stadgar + årsredovisning + senaste årsmöte protokoll** (BRF) | If bostadsrätt | At sale |
| **Underhållsplan** (maintenance plan, BRF) | If bostadsrätt | At sale |

### BRF financial health (CRITICAL for bostadsrätt buyers)

Before buying any bostadsrätt, demand:
1. **Senaste tre årsredovisningar** (last 3 annual reports)
2. **Underhållsplan** with cost projections
3. **Belåningsgrad** (BRF mortgage % of property value) — high = risk
4. **Skuldkvot** + **låneförhållande** trends
5. **Avgift per m² historisk** (avgift trend)
6. **Stora kommande projekt** (planned major repairs — stamb, fasad, tak)

**Red flags**: BRF debt > 70 % of property value, deferred maintenance, multi-year avgift increases, < 10 % own capital.

### Climate change projections (SMHI)

- +1.5–4.5 °C by 2050 (RCP scenarios)
- More precipitation: winter floods, summer drought
- Sea-level rise affecting south + west coasts (+30-70 cm by 2100)
- Heat waves: Skåne + central SE more frequent
- Forest fire risk rising sharply
- Permafrost retreat: Norrland

---

## Section: `--mains`

### Sources

- **Svenskt Vatten** (national association): `https://www.svensktvatten.se/`
- Each kommun manages own water + sewer
- Major: **Stockholm Vatten och Avfall**, **Göteborg Kretslopp och Vatten**, **NSVA** (Nordvästra Skånes Vatten och Avlopp), **VA SYD** (Malmö-Lund)

### Verification

- Most populated areas: kommunal mains universal
- **Glesbygd (rural) + sommarstugor**: often **enskilt avlopp** (BDT + 3-chamber tank + filter)
- **EU Urban Wastewater Directive 2026** may tighten rural requirements

### Costs

| Scenario | Cost (SEK) |
|---|---:|
| Anslutning to mains | 30,000–80,000 |
| Mains-line extension via kommun | 50,000–250,000+ |
| Enskilt avlopp 3-chamber + filter | 80,000–250,000 |
| Markbädd renovation | 60,000–150,000 |
| Borrad brunn (drilled well) | 80,000–150,000 |

---

## Cost benchmarks (SE 2026)

| Work | Cost (SEK) |
|---|---:|
| Energideklaration | 4,000–10,000 |
| Mäklare (seller-paid typically) | 2–4 % of price |
| **Lagfart (buyer): stämpelskatt + expeditionsavgift** (juridisk person: 4.25 % + 825) | **1.5 % + 825** |
| Pantbrev (new mortgage) | 2 % of new pantbrev amount + 375 |
| Besiktning | 5,000–15,000 |
| **Total transaction cost (buyer, new mortgage at 70 % LTV, no reusable pantbrev)** | **est. ~3 %** of price (1.5 % + 2 % × 0.70 = 2.9 %, plus fees + besiktning) |
| **Total transaction cost (cash buyer)** | **est. ~2 %** of price (1.5 % + SEK 825 + besiktning) |
| Enskilt avlopp installation | 80,000–250,000 |
| Roof concrete tile (150 m²) | 250,000–500,000 |
| Energy retrofit (Class C → A, classes as defined before the 1 Oct 2026 energideklaration rules) | 600,000–1,500,000 |
| Asbestos abatement (small house) | 100,000–400,000 |
| BRF stamb-renovation per apartment | 100,000–300,000 |

## Active fiscal incentives (2025-2026)

- **ROT-avdrag**: renovation labour, max 30 % of the labour cost (incl. moms) deducted on the invoice, max SEK 50,000/yr/person (2026 data, source: Skatteverket)
- **RUT-avdrag**: cleaning + household services, max 50 % of the labour cost; ROT + RUT together max SEK 75,000/yr/person (2026 data, source: Skatteverket)
- **Grön teknik** skattereduktion (replaces the old solcellsstöd): 15 % of labour + material for a grid-connected solar PV system, 50 % for home battery storage and for an EV charging point, max SEK 50,000/yr/person (2026 data, source: Skatteverket)
- **Bidrag för energieffektivisering i småhus** (Förordning 2023:402; Boverket + länsstyrelsen): max 30 % of material costs, max SEK 60,000 per småhus, minimum grant SEK 10,000; owner-occupied permanent home with värdeår before 1990 and not on district heating; measures started from 17 Oct 2025; planned to run to end-2030 with SEK 300M/yr (2026 data, source: Boverket, page updated 5 Oct 2026)
- **Bank green-mortgage discounts**: SBAB and Nordea give 0.10 pp off the mortgage rate for energy class A, and for class B only on an energideklaration issued before 1 Oct 2026, when new energideklaration rules took effect (2026 data, sources: sbab.se, nordea.se lender pages; Boverket for the 1 Oct 2026 rules)

## Common listing platforms

- **Hemnet** — dominant (82 % of 2025 sales were advertised there, per Hemnet Group 3 Jul 2026); full extraction
- **Booli** (SBAB) — sold prices + valuation
- **Blocket Bostad** — rentals only, merged into Qasa (2026)
- **Fastighetsbyrån, Svensk Fastighetsförmedling, Mäklarhuset** — agency networks
- **Länsförsäkringar Fastighetsförmedling** — bank-affiliated (`https://www.lansfast.se/`)

## Caveats unique to SE

- **Bostadsrätt vs äganderätt**: bostadsrätt is share in BRF housing cooperative; ~60 % of urban dwellings in major cities
- **BRF financial health audit MANDATORY** — bad BRF can wipe out apartment value
- **BRF stamb-renovation cycle** ~50 years — buildings approaching this can have €25-50k assessment per apartment
- **Hyresreglering** kills long-let yield in major cities
- **Strandskydd** (shoreline protection): 100 m from the shoreline by default, extendable by länsstyrelsen to max 300 m; no new buildings inside the zone (Miljöbalken 7 kap. 14–15 §§). Since Lag 2025:512, no strandskydd by default at lakes of 1 ha or less or streams 2 m wide or narrower (länsstyrelsen can reinstate it, max 100 m), nor at waters created after 30 Jun 1975 (7 kap. 13 a–13 c §§) (2026 data, source: riksdagen.se)
- **Tomträtt** apartments (Stockholm, Göteborg older areas): separate ground rent that increases
- **Bolånetak (belåningstak) 90 %** of market value for a new housing credit such as a purchase loan, up from 85 %, and **tilläggslån** (top-up on an existing mortgage) capped at 80 %, for loans taken from 1 Apr 2026 under lag (2026:226) om begränsning av bostadskrediter, which replaced Finansinspektionen's föreskrifter and allmänna råd (repealed 31 Mar 2026). **Amorteringskrav**: at least 2 %/yr above 70 % LTV, 1 %/yr above 50 % up to 70 %, none at or below 50 %; the extra 1 pp for housing debt above 4.5× gross income is abolished, but on existing loans it ends only when the borrower agrees new terms with the bank. Revaluing the home to change the amortisation pace, or now to raise borrowing room, is as a rule allowed only once every five years (2026 data, sources: Finansinspektionen 2026-03-19, regeringen.se 2026-03-05)
- **Sommarstuga** (summer cottage) often has different regime + utilities + strandskydd
- **Fjällstugor** (mountain cabins): even stricter restrictions + reindeer-husbandry concerns (Sami)
- **Hög radon** especially Stockholm + Småland — measurement before buying recommended
- **Quick clay (kvicklera)** along Göta älv valley + west coast — Skredkommissionen
- **Andelsboende** rare; common is BRF cooperative
- **Tax-free first-time buyer schemes** — none currently
- **Fastighetsskatt vs Fastighetsavgift**: the capped municipal avgift is for finished homes; statlig fastighetsskatt is for lokaler (1 %), unbuilt plots (1 % småhus plot, 0.4 % hyreshus plot) and homes under construction (1 % småhus) (2026 data, source: Skatteverket)
- **Deklaration bilaga K5 (småhus / ägarlägenhet) or K6 (bostadsrätt)** — gain computation mandatory in the return for the year of sale; bilaga K2 to claim uppskov (2026 data, source: Skatteverket)

## Reddit / forum sources

- **r/sweden**, **r/svenskpolitik**, **r/SwedishPersonalFinance**
- **Hemnet community + blog**, **Fastighet-bidrag forum**
- **Bostadsrätterna** resources — a service and interest organisation for BRFs (10,000+ member associations), not a consumer body (source: bostadsratterna.se, 2026)
- Expat: **r/sweden** + **The Local Sweden**

## Verification authorities

| Authority | When to call |
|---|---|
| **Lantmäteriet** | Title verification, lagfart, fastighetsutdrag |
| **Kommun byggnadsnämnd** | Permits, detaljplan, strandskydd |
| **Kronofogden** | Pending lawsuits, encumbrances |
| **Skatteverket** | Lagfartsskatt, capital gains |
| **BRF styrelse + förvaltning** | If bostadsrätt: financial state, assessments |
| **VA-bolag (kommunalt)** | Mains drains verification |
| **Länsstyrelse** | Strandskydd, naturreservat |
| **SGU** | Radon mapping |

## Quirks to know

- **Andelstal vs insats vs månadsavgift** distinctions in BRF
- **Pantbrev** can be reused but must be transferred properly
- **Tomträtt** ground rent often re-negotiated periodically — surprise increases possible
- **Servitut** (easements) common in tomträttsavtal
- **Förenade Hyresgäster** + **Hyresgästföreningen** for tenant disputes
- **Rotavdrag** paperwork via tradesperson, not buyer
- **Klimatdeklaration** for new buildings where bygglov was applied for from 1 Jan 2022 (lag om klimatdeklaration för byggnader; source: Boverket)
- **SBC (Sveriges BostadsrättsCentrum AB)** + **Riksbyggen** + **HSB** are major BRF management orgs
- **Bostadsmarknad i Norden tax differential**: SE much lower property tax than DK/FI/NO

## Source URL templates

| Source | URL pattern |
|---|---|
| Lantmäteriet | `https://www.lantmateriet.se/` |
| Hemnet | `https://www.hemnet.se/bostader?location_ids[]=<id>` |
| Booli | `https://www.booli.se/` |
| SCB Fastighetspriser | `https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/fastigheter/fastighetspriser-och-lagfarter/` |
| Mäklarstatistik | `https://www.maklarstatistik.se/` |
| Skatteverket Fastighetsskatt | `https://www.skatteverket.se/privat/fastigheterochbostad/fastighetsavgiftochfastighetsskatt.html` |
| MSB Översvämningskartor | `https://www.msb.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/` |
| SGU Radonkarta | `https://www.sgu.se/produkter-och-tjanster/kartor/kartvisaren/` |
| Boverket | `https://www.boverket.se/` |
| Trafikverket | `https://www.trafikverket.se/` |
| Klimatanpassning | `https://www.klimatanpassning.se/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for cadastre + admin geography (Lantmäteriet, SCB), for the fiscal and statutory figures re-checked on primary sources on 2026-10-23 — fastighetsavgift caps, stämpelskatt + expeditionsavgift, pantbrev, capital gains + uppskov, VAT rates (the food-VAT end date: secondary source only), ROT/RUT and the lag (2026:226) mortgage caps (Skatteverket, Lantmäteriet, regeringen.se, Finansinspektionen) — and for the `--work` figures (SCB, Skatteverket, Bolagsverket). MEDIUM for `--price` (bostadsrätt benchmarks come from a secondary aggregator, Svensk Mäklarstatistik; the Hemnet share is company-reported; the avgift range is unverified), `--rental` (the 2026 statutory changes are primary-sourced; the short-let insurance and tax-enforcement bullets are unverified; EU 2024/1028 has applied directly since 20 May 2026, so there is nothing to transpose — source: European Commission), `--risks` + `--mains` (authority sources re-checked; the regional radon list, part of the build-era table, the BRF red-flag thresholds and the est. mains build costs are unverified) and `--traffic` (verdict bands are curated thresholds). LOW for the market-price rows in Cost benchmarks (energideklaration, mäklare, besiktning, avlopp, roof, retrofit, asbestos, stamb), which have no published source.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | AB share capital, egenavgifter 28.97 % and SCB 2025 salary figures re-checked; Monster removed; job-board, F-skatt, A-kassa and union rows not re-checked |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Hemnet share, Booli owner (SBAB), Blocket Bostad (rentals, Qasa) and the Länsförsäkringar name + URL corrected; agency sites live |
| Active fiscal incentives (2025-2026) | 2026-10-23 | 2026-10-23 refresh wave | ROT 30 %, RUT 50 % with the SEK 75,000 combined cap, grön teknik, Boverket småhus energy grant and the 0.10 pp bank discount checked against Skatteverket, Boverket, SBAB + Nordea |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Kronofogden, Skatteverket and SGU roles corrected; other rows confirmed |

Sections without a row default to the Status footer date (2026-04-25). Country profile, `--price`, `--traffic`, `--tax`, `--rental`, `--risks`, `--mains`, Cost benchmarks, Caveats, Quirks, Source URL templates and Reddit / forum sources were partly re-checked on 2026-10-23 but keep unverified items (see Update history), so they keep the footer date.

## Extension TODOs

- [ ] Per-kommun strandskyddsmättning (some kommuner extend default 100m to 300m)
- [ ] BRF financial health red-flag detection (belåningsgrad, underhållsplan, etc.)
- [ ] Tomträtt remaining lease length lookup
- [ ] Quick clay (kvicklera) zone overlay along Göta älv
- [ ] Per-kommun avgiftsuttag (ROT-eligible) tracking
- [ ] Sommarstuga vs permanentbostad distinction patterns
- [ ] Hemnet API extraction patterns (limited)
- [ ] Booli sold-prices API

## Update history

- **2026-04-25** — Initial population
- **2026-10-23** — Refresh wave: fast-changing sections + audit findings re-checked against primary sources (secondary sources labelled). Counts per section are changed / confirmed / unverifiable. The playbook-level date is not re-stamped because `--price`, `--tax`, `--rental`, `--risks` and `--mains` keep unverified items.
  - Country profile (3 / 3 / 2): parish unit → distrikt; EUR/SEK re-based on ECB reference rates; minority languages per Språklag (2009:600). Unverified: postcode examples, fastighetsbeteckning pattern.
  - `--price` (28 / 3 / 5): benchmark table rebuilt (bostadsrätt: Svensk Mäklarstatistik, secondary; villa: SCB 2025); Hemnet share ~90 % → 82 % of 2025 sales (company-reported); Booli owner Schibsted → SBAB; Blocket Bostad now rentals only (Qasa); SCB småhus price index Q3 2026 added. Unverified: avgift range, Fastighetsbyrån "(largest)", Hemnet sold-search feature + URL pattern, Min fastighet BankID login, "Booli Pris" name.
  - `--traffic` (3 / 2 / 2): Trafikverket remit; dead NVDB URL → Lastkajen + Vägtrafikflödeskartan; ÅDT definition. Unverified: verdict bands (curated thresholds), E-road anchor.
  - `--tax` (7 / 13 / 4): BRF + hyreshus fastighetsavgift cap corrected to SEK 1,724 (2025) / 1,784 (2026), was ~1,510 / 1,562; taxeringsvärde 75 % basis; villa example re-based on the 2026 cap; bostadsrätt överlåtelseavgift tied to the stadgar; uppskov limits + replacement window; VAT rows (food 6 % from 1 Apr 2026). Confirmed: stämpelskatt 1.5 % / 4.25 % + SEK 825, pantbrev 2 % + SEK 375, capital gains 22/30, Jordabalken 4:19. Unverified: mäklare 2–4 %, the 2008 origin, Future-risk bullets.
  - `--rental` (8 / 2 / 4): Privatuthyrningslag (2026:772) + longer bostadsrätt sublets (1 Jul 2026); presumtionshyra reform (1 Jan 2026); Stockholm queue times (2025); EU 2024/1028 corrected from "transposition pending" to a directly applicable regulation (audit); schablonavdrag SEK 50,000 → 40,000 per dwelling. Unverified: hemförsäkring disclosure, tax-authority tightening, moms on commercial-style letting.
  - `--work` (5 / 4 / 5): Monster removed (ceased European operations 2025); egenavgifter 28.97 %; SCB 2025 national median SEK 38,300 + percentiles + regional averages; AB share capital SEK 25,000 confirmed; Saco Lönesök access. Unverified: job boards, F-skatt term, A-kassa, union confederations.
  - `--risks` (20 / 9 / 15): MSB → MCF (1 Jan 2026) incl. flood-map URL; Boverket BFS 2026:9 (1 Oct 2026); SGU radon drivers; SMHI storm list (Gudrun, Ingunn, Johannes); strandskydd small-water exemption; asbestos to the 1982 ban (was pre-1992) + PCB dates; energideklaration rules; SMHI temperature projections (2015 report) + IPCC AR6 sea-level range. Unverified: regional radon list, Ljusdal 2018, nZEB start date, pre-1960s row, BRF red-flag thresholds, qualitative climate bullets.
  - `--mains` (2 / 4 / 5): recast UWWTD (EU) 2024/3019 replaces the "2026 directive" line; mains connection fee → Svenskt Vatten 2025 mean SEK 196,290 / median 184,779 (was 30,000–80,000); other cost rows labelled est. Unverified: VA SYD + NSVA coverage, the est. cost rows.
  - Cost benchmarks (3 / 2 / 7): lagfart + pantbrev rows confirmed; both transaction totals recomputed and labelled est.; retrofit row tied to the pre-1 Oct 2026 classes. Unverified: market-price rows.
  - Active fiscal incentives (5 / 0 / 0): ROT 50 % → 30 %; RUT with the SEK 75,000 combined cap; solcellsbidrag → grön teknik; "Boverket Klimatpremie" (no such programme) → Boverket småhus energy-efficiency grant (Förordning 2023:402); bank green discount 0.10 pp.
  - Caveats unique to SE (4 / 0 / 1): LTV cap 85 % → 90 % + tilläggslån 80 % under lag (2026:226) from 1 Apr 2026 (audit SE-LTV-01); strandskydd (Lag 2025:512); fastighetsskatt scope; bilaga K5/K6 (was K6/K10). Unverified: "no first-time buyer schemes".
  - Quirks to know (2 / 1 / 2): klimatdeklaration basis; SBC = Sveriges BostadsrättsCentrum (was "Specialfastigheter"). Unverified: Riksbyggen/HSB, Förenade Hyresgäster.
  - Common listing platforms (4 / 3 / 0); Verification authorities (3 / 5 / 0); Source URL templates (3 / 7 / 2: MSB → MCF, SGU row relabelled, Trafikverket ÅDT + Lastkajen rows added; Hemnet + Booli return 403 to automated requests); Reddit / forum sources (1 / 1 / 5: Bostadsrätterna described as a BRF organisation; subreddits blocked, two forum names untraced).
  - Status: EU 2024/1028 wording corrected (audit); Confidence recomputed; per-section verification table added.
