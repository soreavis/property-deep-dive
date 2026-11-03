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

- **Lantmäteriet "Min fastighet"**: `https://www.lantmateriet.se/sv/fastighet-och-mark/information-om-fastigheter/Min-fastighet/` — details of your own property (area, inteckningar, taxeringsvärde, plans, servitut); login needs a Swedish personnummer or samordningsnummer and BankID or Freja+ e-ID; documents (akter) are ordered separately (2026, source: Lantmäteriet)
- **Lantmäteriet open data**: `https://geotorget.lantmateriet.se/`
- **SCB (Statistiska centralbyrån) Fastighetspriser**: `https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/fastigheter/fastighetspriser-och-lagfarter/` — småhus price index Q3 2026 (preliminary) 986 (1981=100), +4 % y/y and +2 % q/q (2026 data, source: SCB, published 23 Oct 2026)
- **Svensk Mäklarstatistik**: `https://www.maklarstatistik.se/` — 1,500 reporting broker offices send contract data daily, covering over 95 % of home sales handled by brokers; SCB processes the monthly statistics; owned by the brokers' association Mäklarsamfundet since 2020 (secondary aggregator, per maklarstatistik.se 2026)
- Valuation tools: **Värderingsdata** (`https://www.varderingsdata.se/`) — AVM valuations, the Ortspris sold-price service and BRF information for brokers and banks, behind a login (per varderingsdata.se 2026); **Booli** — sold prices and an online home valuation ("värdera din bostad", per sbab.se 2026)

### Listing platforms

- **Hemnet** — dominant: 82 % of 2025 home sales (139,063 of SCB's 170,415) were advertised on Hemnet, down from 86–90 % in 2019–2024 (2025 data, preliminary until Jul 2027; source: Hemnet Group press release 3 Jul 2026, company-reported against SCB): `https://www.hemnet.se/`
  - Sold prices: the "Slutpriser" tab at `https://www.hemnet.se/salda/bostader`, filterable by area (source: hemnet.se, archived 2026-03-12)
  - URL (sold): `https://www.hemnet.se/salda/bostader?location_ids[]=<id>&item_types[]=bostadsratt` (pattern per Wayback Machine captures of 2026-05-04 and 2026-10-01); for-sale search `https://www.hemnet.se/bostader`, canonical `https://www.hemnet.se/till-salu` (archived 2026-03-12). The live site could not be read for verification — check it directly
- **Booli** (part of SBAB's services; operated by Booli Search Technologies AB, per booli.se 2026): `https://www.booli.se/` — sold prices map + valuation
- **Blocket Bostad**: `https://www.blocket.se/bostad` — rentals only, now merged into **Qasa** (`https://qasa.com/se/sv`); not a for-sale channel (per blocket.se/bostad, 2026)
- Agency networks: **Fastighetsbyrån** (Swedbank subsidiary; calls itself the leading chain, with ~270 offices, ~39,000 homes brokered in Sweden in 2025 and about one in four Swedish home sales — company-reported, per fastighetsbyran.com 2026), **Svensk Fastighetsförmedling**, **Mäklarhuset**, **Notar** (Stockholm, central Sweden + Skåne), **SkandiaMäklarna**

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

Kommun / district averages, not parcel values. Bostadsrätt = broker-reported sales over the last 12 months (the area pages' "12 månader" column; their 3-month column covers Jul–Sep 2026) (2026 data, secondary aggregator; Svensk Mäklarstatistik area pages updated 8 Oct 2026); Stockholm suburbs span Nynäshamn 25,317 – Lidingö 66,107. Rural Norrland bostadsrätt values rest on 1–51 sales per kommun in 12 months; Svensk Mäklarstatistik treats fewer than 25 sales as too few for statistical relevance. Villa = SCB average köpeskilling for permanent småhus excl. tomträtt; fritidshus = SCB regional averages (2025 data, source: SCB Statistikdatabasen TAB1169 + TAB1152). Ski resorts break the Norrland pattern (Åre bostadsrätt 60,152 SEK/m², rolling 12 months, update of 8 Oct 2026).

### Compute

1. Listing SEK/m² = price / **boarea (BOA)**, the legal living area definition
2. **Trap**: BOA + biarea (BIA: basement, garage, attic) = useful total but not for €/m² comparison
3. **Trap**: Bostadsrätt has **andelstal** (share %) determining BRF voting rights + monthly avgift portion
4. **Bostadsrätt math**: monthly **avgift** covers BRF mortgage + maintenance — affects "true" cost. Bostadsrätt households paid the BRF SEK 59,728/yr on average (± 1,508; ≈ SEK 4,977/mo = 59,728 / 12), from SEK 34,559/yr (≤ 50 m²) to SEK 90,436/yr (≥ 131 m²) (2024 data, source: SCB Hushållens boendeutgifter, table HE0202T15, sample survey — rates/figures may have changed since); new-build bostadsrätter completed in 2024 averaged SEK 865/m²/yr and SEK 5,115/mo per dwelling (10,250 dwellings, 846 of them småhus) (2024 data, source: SCB table BoRattLgh — rates/figures may have changed since). Compare the listing's avgift per m² with the BRF's årsredovisning
5. Tomträtt apartments: separate **tomträttsavgäld** (ground rent, increases periodically)

---

## Section: `--traffic`

### Primary sources

- **Trafikverket**: `https://www.trafikverket.se/` — national transport administration: plans road, rail, sea + air infrastructure and builds + runs state roads and railways (source: Trafikverket)
- **NVDB (Nationell vägdatabas)** road data via **Lastkajen**: `https://lastkajen.trafikverket.se/` — download after registration + licence acceptance (source: Trafikverket)
- **Vägtrafikflödeskartan** (ÅDT, MC + cycle flows, speeds; **state road network only**): `https://bransch.trafikverket.se/tjanster/trafiktjanster/Vagtrafik--och-hastighetsdata/fordonsfloden-och-hastigheter/`
- City traffic: Stockholm `https://www.stockholm.se/`, Göteborg, Malmö city portals

### Key term

**ÅDT (årsmedeldygnstrafik)** = AADT-equivalent — average vehicles per day over a year. On Trafikverket's flow map each road section shows the estimated ÅDT, the measurement year in brackets and an uncertainty value — check the measurement year before relying on the figure (source: Trafikverket)

### Verdict bands (SE coastal/urban-typical)

- 🟢 < 1,000 v/d (residential gata, lokal väg)
- 🟡 1,000–8,000 v/d (länsväg, urban arterial)
- 🟠 8,000–30,000 v/d (motorväg/E-road, inner ring)
- 🔴 > 30,000 v/d (E4/E6/E18, central Stockholm/Göteborg/Malmö)

---

## Section: `--tax`

### Annual property charge — Fastighetsavgift (CAPPED)

**Sweden has a unique CAP-based property charge** (the kommunal fastighetsavgift replaced the statlig fastighetsskatt on finished homes from 1 Jan 2008 — Lag 2007:1398 om kommunal fastighetsavgift, in force 1 Jan 2008; the statlig fastighetsskatt, Lag 1984:1052, still applies to e.g. homes under construction and unbuilt plots) (source: riksdagen.se, SFS 2007:1398 and SFS 1984:1052):

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
- **Mäklare** (broker): hired and paid by the seller; no set fee level — commission is negotiated, usually a % of the sale price (flat, tiered, or with a minimum) or a fixed price, quoted incl. moms to a consumer seller (2026 data, source: Fastighetsmäklarinspektionen). Seller-reported fees: 1.0–5.4 % of price / SEK 38,500–120,000 overall, villa 1.0–6.0 % / SEK 50,000–146,000, apartment 1.0–5.0 % / SEK 36,800–100,000 (5th–95th percentile of sales over the preceding two years) (2026 data, source: Hittamäklare by Booli/SBAB, secondary aggregator ⚠️ — compare written quotes)

### Capital gains

- **Reavinstskatt 22 %** on profit (gain) — effective rate = 30 % capital-income tax on 22/30 of the gain for a privatbostad; a loss is 50 % deductible (2026 data, source: Skatteverket)
- **Uppskov** (deferral): can defer if buying a replacement primary residence (Sweden / EEA); a new uppskovsbelopp is min SEK 50,000 and max SEK 3,000,000; for a 2026 sale the replacement must be bought between 1 Jan 2025 and 31 Dec 2027 and moved into by 2 May 2028. **Interest-free from income year 2021** (the ~0.5 %/yr uppskovsränta was abolished) — no annual cost, but the deferred gain is taxed at the rate in force when the uppskov is reversed, which Skatteverket warns may differ from 22 % (2026 data, source: Skatteverket)
- **Undersökningsplikt — Jordabalken 4 kap. 19 § andra stycket** (canonical caveat-emptor anchor): buyer loses right to price reduction / rescission for any defect they should have detected through ordinary inspection — duty is *långtgående* (far-reaching) per SE doctrine + case law. Besiktning is the only practical defence (source: riksdagen.se / lagen.nu).
- **Privatbostad** (primary residence) deduction methods + reno tracking

### VAT (moms)

- 25 % standard
- 12 % reduced (restaurant / café service, hotel room letting)
- 6 % super-reduced (food incl. takeaway, temporarily cut from 12 % for 1 Apr 2026 – 31 Dec 2027 by Lag 2026:118; 12 % returns on 1 Jan 2028 under Lag 2026:119 (source: riksdagen.se, SFS 2023:200 9 kap.; Prop. 2025/26:55); books; domestic passenger transport)
- Sale or letting of property, residential or commercial: VAT-exempt
- Commercial letting: 25 % on the rent only where the landlord opts in (frivillig beskattning, tenant running a VAT-liable business) (2026 data, source: Skatteverket)

### Future risk

- Property-tax debate continues in opposition motions: on 11 Mar 2026 the Riksdag rejected, after a vote, Vänsterpartiet's call for an inquiry to design a fastighetsskatt (motion 2025/26:2783 yrkande 4) and Miljöpartiet's call for an inquiry into a lower fastighetsavgift for owners who carried out energy-efficiency measures (motion 2025/26:3547 yrkande 10) (bet. 2025/26:SkU15 punkt 9, source: riksdagen.se). A tax tied to full value would weigh most on high-value Stockholm/Göteborg homes, which the cap now shields (inference from the cap mechanics above)
- Lagfart / pantbrev stamp duty: motions to review or cut it (M 2025/26:348; C 2025/26:3184 yrkande 34) were rejected in the same decision (bet. 2025/26:SkU15 punkt 9, source: riksdagen.se)
- Capital gains on home sales: motions to cut or review the tax (e.g. KD 2025/26:3457) were rejected on 11 Mar 2026 (bet. 2025/26:SkU15 punkt 10, source: riksdagen.se)
- No transfer-tax or fastighetsavgift change pending: no amendment awaits entry into force in Lag 1984:404 om stämpelskatt vid inskrivningsmyndigheter (consolidated to SFS 2025:391) or Lag 2007:1398 (consolidated to SFS 2012:743) (source: riksdagen.se); none of the tax proposals the government sent out for consultation ahead of the 2027 budget concerns property (source: regeringen.se, published 18 May 2026); the 2027 budget bill, due by 12 Nov 2026 in the election year, had not been tabled as at 2026-11-03 (sources: riksdagen.se, regeringen.se)

---

## Section: `--rental`

### Long-term residential

- **Hyresreglering** (rent control) — STRICT especially in major cities
- **Bruksvärdesystem**: rent set by negotiation between Hyresgästföreningen + Fastighetsägarna; newbuilds can use **presumtionshyra** (negotiated rent set for the first 15 years), and since 1 Jan 2026 landlords have more room to adjust it during that period (2026 data, source: Riksdag decision 2025/26:CU5, 19 Nov 2025)
- **First-hand contract (förstahandskontrakt)** in regulated rental: hard to obtain — Stockholm's Bostadsförmedlingen let 20,861 homes in 2025, with an average queue time of 9.0 years for ordinary rentals and 12.4 years within Stockholms stad (2025 data, source: Bostadsförmedlingen i Stockholm)
- **Andrahandsuthyrning** (subletting your own bostadsrätt): still needs consent from the BRF board or, if it refuses, time-limited permission from hyresnämnden, which requires a reason for subletting and no justified ground for the BRF to refuse; before the reform, permission was most often given for one year and then in many cases refused even when the reason remained (Prop. 2025/26:187, section 5.1); since 1 Jul 2026 hyresnämnden can grant permission for longer periods than were normally given, and earlier sublets count against a new application only if they were substantial (bostadsrättslagen 7 kap. 11 § as amended by Lag 2026:776; Riksdag decision 2025/26:CU31, 20 May 2026)
- **Privatuthyrningslag (2026:772)**, in force 1 Jul 2026, replaced lagen (2012:978) om uthyrning av egen bostad, which still governs contracts made under it: covers a private person or dödsbo letting a house or part of a house (e.g. an apartment) as a home, up to two lettings outside their own home; not a hyresrätt sublet and not leisure lets. Rent is agreed freely, but hyresnämnden can cut a rent that is *väsentligt högre* than for comparable homes; 3-month notice for both sides on open-ended contracts (source: SFS 2026:772 via data.riksdagen.se; Riksdag decision 2025/26:CU31, 20 May 2026)

### Short-let (Airbnb, Booking)

- **Hemförsäkring**: check with the insurer how cover applies during the let and whether an uthyrningsskydd add-on is needed; a standard policy normally does not cover theft by the guest or damage the guest does to your belongings, and regular letting can count as förvärvsmässig, which puts disputes with the guest outside the policy's rättsskydd (2026, source: Konsumenternas Försäkringsbyrå "Hyra, låna eller hyra ut – så gäller försäkringarna"; the bureau is a foundation whose board includes Konsumentverket, Finansinspektionen and the insurers' association Svensk Försäkring)
- **BRF consent** (styrelsens samtycke) is required to let a bostadsrätt in andra hand for independent use; since 1 Jul 2026, letting all or part of a flat the owner does not use as a permanent home (or otherwise to a considerable extent) always counts as independent use. If the board refuses, only hyresnämnden can grant permission, limited in time (bostadsrättslagen 7 kap. 10–11 §§ as amended by Lag 2026:776, source: riksdagen.se)
- **Stockholm + Göteborg**: no city-level cap — Sweden has no rules restricting short-let supply on housing-supply grounds (see EU 2024/1028 below); for a bostadsrätt the limit is BRF consent (above). Skatteverket can receive data from digital platforms on what hosts were paid and shows it in Mina inkomstuppgifter; the host must still declare any surplus (2026, source: Skatteverket "Hyra ut privatbostad")
- **EU Regulation 2024/1028** (short-term-rental data sharing): an EU regulation applying since 20 May 2026, so nothing to transpose. A Member State needs a registration procedure only if it requires platforms to transmit data; Sweden has introduced none, and has no rules restricting short-let supply on housing-supply grounds (2026 data, source: Regeringskansliet faktapromemoria 2026/27:FPM1, 14 Oct 2026). Watch: the Commission's proposed affordable-housing regulation COM(2026) 599 (9 Sep 2026) would set an EU framework for local short-let limits; Swedish remiss runs to 14 Nov 2026 (same source)
- Income tax: standard deduction (schablonavdrag) **SEK 40,000/yr per dwelling** (not per person), plus 20 % of the rent for a villa/ägarlägenhet or the BRF avgift for the let period of a bostadsrätt; rent below that total is effectively tax-free, and any surplus is capital income (2026, source: Skatteverket "Hyra ut privatbostad")

### Tax on rental

- Surplus after the deductions: 30 % tax on capital income (2026 data, source: Skatteverket Belopp och procent 2026)
- Computed example: villa let for SEK 50,000/yr → deduction 40,000 + 20 % × 50,000 = 50,000 → taxable surplus SEK 0 (rules: Skatteverket "Hyra ut privatbostad")
- Hotel-like letting (furnished, more than occasionally, short stays, priced per night or week or with cleaning / linen services): 12 % moms once annual turnover exceeds SEK 120,000 in the calendar year or either of the two years before, counted per co-owner. A home that does not count as a privatbostad (main test: owner or close family use more than half the floor area, 40 % for a tvåfamiljshus) is taxed as näringsverksamhet on bilaga NE (2026, source: Skatteverket "Hyra ut privatbostad")

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
| **MCF (Myndigheten för civilt försvar)** — replaced MSB on 1 Jan 2026; msb.se redirects | `https://www.mcf.se/` | Risk maps, civil protection |
| **MCF Översvämningskarteringar** + Översvämningsportalen | `https://www.mcf.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/oversvamningskarteringar/` | Flood hazard maps (rivers, coast, Vänern); GIS layers + reports in Översvämningsportalen |
| **SGU (Sveriges geologiska undersökning)** | `https://www.sgu.se/` | Geology + soil maps, gamma-radiation (uranium) maps as a radon proxy, wells archive (Brunnsarkivet) |
| **SSM (Strålsäkerhetsmyndigheten)** | `https://www.stralsakerhetsmyndigheten.se/` | Radon program |
| **Boverket** | `https://www.boverket.se/` | Building regulations (BBR, BFS 2011:6, repealed 1 Oct 2026 by BFS 2026:9; older rules allowed for bygglov applications filed before 1 Oct 2027), energy declarations |
| **Klimatanpassning (SMHI)** | `https://www.klimatanpassning.se/` | Climate adaptation portal |
| **SGI (Statens geotekniska institut)** | `https://www.sgi.se/` | Landslide + slope stability |

### Specific risks

- **Skred (landslides)** — Vänern + Vättern shores, **Göta älv valley** (severe quick-clay zones, similar to Norway), west coast. SGI rates the Göta älv area as Sweden's highest ras/skred risk because of kvicklera (source: SGI)
- **Översvämning (flooding)** — coastal + lake-shore + river plains; Mälaren risk for Stockholm
- **Stigande havsnivå** (sea-level rise) — mean water level rises mainly along Sweden's southern coasts, where land uplift is slower than sea-level rise; along the Norrland coast faster uplift still lowers it for now (source: SMHI)
- **Skogsbrand (forest fire)** — increasing climate risk; Västmanland 2014 (the burnt area includes the Hälleskogsbrännan reserve in Sala, Surahammar + Fagersta kommuner; source: Länsstyrelsen Västmanland); summer 2018 brought Sweden's most extensive fires in modern times: 25,000 ha burnt, nearly ten times the 2000s average, and the Ljusdal kommun fires (Gävleborg), which began on 14 Jul 2018 after a lightning strike, covered 9,500 ha (source: SOU 2019:7 Skogsbränderna sommaren 2018)
- **Radon** — per SGU the drivers are uranium-rich rock (some granites, pegmatites, alum shale), permeable ground (very high values on gravel eskers / grusåsar) and **blåbetong** (alum-shale concrete used 1929–1978); uranium-rich alum shale occurs in Skåne, Västergötland, Östergötland, Öland, Närke and along the mountain range. SGU's radon pages name no granite regions: check SGU's "Gammastrålning, uran" map viewer and the kommun's radonriskkarta (many kommuner publish one), and note that a house leaky against the ground can exceed the reference level even in a lågriskområde. Reference level **200 Bq/m³** in homes; radon is found only by measuring, over at least 2 months between 1 Oct and 30 Apr; SSM estimates close to 400,000 dwellings exceed the reference level (no data year given, SSM page updated 4 Sep 2026; sources: SGU; Strålsäkerhetsmyndigheten)
- **Earthquake** — very low (Sweden on stable Baltic Shield)
- **Storm/strong wind** — Atlantic depressions Skåne, Halland; the north is exposed too. SMHI storm list: Gudrun (7 Jan 2005, gusts 42.0 m/s), Ingunn (1 Feb 2024, gusts 58.7 m/s, return period >100 yrs), Johannes (27 Dec 2025, Gästrikland + Hälsingland, gusts 47.1 m/s, return period >50 yrs, long power cuts); Hans (6–11 Aug 2023) was an extreme-rain event (source: SMHI)
- **Strandskyddszon** (shoreline protection): 100 m from the shoreline on land + water by default; länsstyrelsen can extend it to 300 m (Miljöbalken 7 kap. 13–18 k §§) — restricts construction near waters. Since 1 Jul 2025 lakes ≤1 ha and watercourses ≤2 m wide have no general strandskydd, but länsstyrelsen can impose up to 100 m in individual cases; dispens via the kommun (some areas länsstyrelsen) (source: Boverket; Naturvårdsverket)
- **Saltvattensinträngning** (saltwater intrusion) — coastal wells affected; deep wells or large withdrawals raise the risk, and a rising sea worsens coastal well quality (source: SGU; SMHI)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint (unverified: no Swedish authority source located; test before sanding or stripping old paint), asbestos (assume present, see below), weak insulation; blåbetong possible from 1929 (source: SGU) |
| **1965–1974 "miljonprogrammet"** | Panel concrete, asbestos in joints, PCB in fogmassa (1956–1973 builds), energy-inefficient — major retrofit cost. 1,005,578 dwellings were built 1965–1974, close to a fifth of the housing stock, a third of them villas and other småhus (source: Boverket, page updated 2 Dec 2025) |
| **1974–1989** | Asbestos likely until the 1982 ban, occasionally later; improving insulation |
| **1989–2000** | Better insulation, modern wiring; PCB not expected (all new PCB use banned since 1978) |
| **Post-2008** | BBR energy rules (BFS 2011:6; energy use determined per BEN, BFS 2016:12) (source: Boverket) |
| **Post-2017** | Energy requirement as a primärenergital (EPpet, kWh/m² Atemp per year): BBR 25 (BFS 2017:5, in force 1 Jul 2017; older rules allowed for bygglov applications filed before 1 Jul 2018) set småhus 90, flerbostadshus 85, lokaler 80 with primärenergifaktorer; BBR 29 (BFS 2020:4, in force 1 Sep 2020; older section 9 rules allowed for bygglov applications filed before 1 Sep 2021) switched to viktningsfaktorer per energibärare and set småhus 90–100 by size, flerbostadshus 75, lokaler 70, with småhus Um 0.40 → 0.30 W/m²K (source: Boverket, BFS 2017:5 + BFS 2020:4) |
| **From 1 Oct 2026** | BFS 2026:9 energy rules (nZEB + zero-emission building definitions) replace BBR; older BBR still allowed for bygglov applications filed before 1 Oct 2027, provided all the older rules are applied (2026 data, source: Boverket, BFS 2026:9 transitional provisions) |

**Asbestos**: assume present in buildings built up to 1982, when Sweden banned it; stockpiled or imported products can turn up in later buildings (source: Arbetsmiljöverket). **PCB in fogmassa** (caulking, expansion joints) and anti-slip floor compound: owners of buildings built or renovated 1956–1973 must inventory them, but one- and two-dwelling houses owned by private individuals (småhus) are not covered by these rules; all new PCB use banned since 1978 (source: Naturvårdsverket). **Blåbetong** (alum-shale concrete, used 1929–1978) raises indoor radon (source: SGU).

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energideklaration** (energy declaration) | Before any sale of a building (Lag 2006:985 6 §); energy class must appear in the ad; for a bostadsrätt the BRF holds it and the seller shows it; new EPBD rules from 1 Oct 2026, class A0 since 25 May 2026 | 10 years; no fixed fine: Boverket can order it under vite, and a buyer refused one may commission it at the seller's cost within 6 months of tillträde (2026 data, source: Boverket) |
| **Lagfart** (title registration at Lantmäteriet) | Buyer applies with the original köpehandling; for purchases from 1 Jul 2026 the buyer needs a Swedish personnummer, samordningsnummer or organisationsnummer, and a legal-person buyer must show its verklig huvudman registration | Within 3 months of the purchase (2026 data, source: Lantmäteriet) |
| **Fastighetsutdrag** (extract from Lantmäteriet's fastighetsregistret) | Checks that the seller is the registered owner; also shows rights attached to the property, buildings, taxering and plans such as detaljplan or naturreservat; registerkarta boundaries can be imprecise and the förrättningsakt prevails (source: Lantmäteriet) | Order a fresh one before signing |
| **Besiktning** (independent survey) | NOT mandatory but strongly recommended | Per case |
| **Stadgar + årsredovisning + senaste årsmöte protokoll** (BRF) | If bostadsrätt — buyer's due-diligence request (curated practice; no statutory source located) | Before signing |
| **Underhållsplan** (maintenance plan, BRF) | If bostadsrätt — buyer's due-diligence request (curated practice; no statutory source located) | Before signing |

### BRF financial health (CRITICAL for bostadsrätt buyers)

Before buying any bostadsrätt, demand:
1. **Senaste tre årsredovisningar** (last 3 annual reports)
2. **Underhållsplan** with cost projections
3. **Belåningsgrad** (BRF mortgage % of property value) — high = risk
4. **Skuldkvot** + **låneförhållande** trends
5. **Avgift per m² historisk** (avgift trend)
6. **Stora kommande projekt** (planned major repairs — stamb, fasad, tak)

**Red flags** (curated buyer heuristics — wisdom, not data; thresholds unsourced): BRF debt > 70 % of property value, deferred maintenance, multi-year avgift increases, < 10 % own capital.

### Climate change projections (SMHI)

- Annual mean temperature ~+3 °C (RCP4.5) / ~+6 °C (RCP8.5) by 2100 vs 1961–1990, largest rise in the north; the scenarios differ little for 2021–2050 (2015 data, source: SMHI report for Dricksvattenutredningen, AR5/RCP basis — rates/figures may have changed since). Sweden's warming since the 1800s has been twice the global rise of just over 1 °C (source: SMHI)
- Precipitation: more across Sweden, most in the north, while some scenarios show no or only a slight rise in Götaland's summer rain; heavier extremes, both skyfall and multi-day rain. Days with low river flows fall in the north but rise in the south, most in eastern Götaland; summer soil moisture falls nationwide, milder winters raise winter flows in the north, and spring groundwater may drop, mainly in south-east Sweden (source: Klimatanpassning.se, run by SMHI; pages updated 9 Dec 2025)
- Sea-level rise: global mean +28–55 cm (SSP1-1.9) to +63–101 cm (SSP5-8.5) by 2100 vs 1995–2014, IPCC AR6 likely range; land uplift offsets it, so mean water level rises mainly in the south while parts of the Norrland coast still see it fall. Per-kustkommun projections adjusted for uplift: `https://www.smhi.se/klimat/framtidens-klimat/stigande-havsnivaer/framtida-medelvattenstand` (IPCC AR6 2021 data, current SMHI reference; source: SMHI)
- Heat waves: more frequent and stronger; SMHI calculates that extreme heat seen once in 20 years on average so far could occur every 3–5 years by the end of the century, and 40 °C could occur once in 20 years in southern Sweden. SMHI's definition: a daily maximum of at least 25 °C on at least five days in a row (source: Klimatanpassning.se, SMHI; page updated 22 Apr 2026)
- Forest fire risk rises in a warmer climate, most in the south and along the Norrland coast, and climate change makes it more likely that the high-risk season starts earlier and lasts longer; 2,000–8,000 fires in skog och mark each year, mostly human-caused (source: Klimatanpassning.se, SMHI; page updated 9 Sep 2026). Close to a doubling of days with high fire risk in south-east Sweden by 2100 (2019 data, source: SOU 2019:7 citing the national risk assessment — rates/figures may have changed since)
- Permafrost retreat: Norrland (qualitative, not confirmed against an SMHI or SGU source — verify at `https://www.klimatanpassning.se/`)

---

## Section: `--mains`

### Sources

- **Svenskt Vatten** (national association): `https://www.svensktvatten.se/`
- Public water + sewer is the kommun's responsibility under 6 § lag (2006:412) om allmänna vattentjänster (source: Naturvårdsverket). Neighbouring kommuner can share the work: NSVA runs operations as a jointly owned municipal company while each kommunfullmäktige still decides taxor, investments and the verksamhetsområde (source: nsva.se); VA SYD, a kommunalförbund, is huvudman and owner of the public VA facilities in its member kommuner (source: vasyd.se, archived 2026-01-20)
- Major: **Stockholm Vatten och Avfall**, **Göteborg Kretslopp och Vatten**, **NSVA** (Nordvästra Skånes Vatten och Avlopp, municipal company for Bjuv, Båstad, Helsingborg, Landskrona, Perstorp, Svalöv, Åstorp + Örkelljunga; source: nsva.se), **VA SYD** (kommunalförbund for Malmö, Lund, Burlöv, Eslöv, Lomma and, since 1 Jan 2025, Svedala; also household waste in Malmö + Burlöv; source: vasyd.se, archived 2026-01-20)

### Verification

- Most populated areas: kommunal mains universal
- **Glesbygd (rural) + sommarstugor**: often **enskilt avlopp** (BDT + 3-chamber tank + filter)
- **Recast EU Urban Wastewater Treatment Directive (EU) 2024/3019**: in force since 1 Jan 2025; requires collection + treatment in all urban areas of more than 1,000 inhabitants (source: European Commission DG ENV). Sweden must transpose it by 31 Jul 2027; Naturvårdsverket's proposal (29 Jan 2026, not yet law) extends the collecting-system duty from 2,000 to 1,000 pe agglomerations, first applied to those of 1,000–2,000 pe on 31 Dec 2035, and inside such an avloppstätort allows an individual system only if it protects health and the environment as well as secondary or tertiary treatment (2026 data, source: Naturvårdsverket). Whether a rural property lies inside such an avloppstätort decides the effect — verify with the kommun's miljöförvaltning

### Costs

| Scenario | Cost (SEK) |
|---|---:|
| Anslutning to mains (anläggningsavgift, villa) | 204,954 mean / 192,418 median (2026) |
| Mains-line extension via kommun | est. 50,000–250,000+ |
| Enskilt avlopp 3-chamber + filter | est. 80,000–250,000 |
| Markbädd renovation | est. 60,000–150,000 |
| Borrad brunn (drilled well) | est. 80,000–150,000 |

The connection fee is the one-off anläggningsavgift in each kommun's VA-taxa, so check the local taxa; highest for a villa in 2026: Sotenäs (SEK 422,890), Uddevalla, Vaxholm; lowest Överkalix (SEK 44,000). Mean annual VA usage fee for a villa: SEK 12,537/yr, +8 % on 2025 (2026 data, source: Svenskt Vatten "2026 års taxestatistik", report R2026-02 revised June 2026, industry association covering all 290 kommuner; villa = typhus A, 150 m² on an 800 m² plot, 150 m³ water/yr). The median is computed from Svenskt Vatten's per-kommun file for 2026 (290 kommuner), because the report's figure caption repeats the 2025 median of 184,779. `est.` rows: ranges carried from the 2026-04 research without a published source — get local quotes.

---

## Cost benchmarks (SE 2026)

| Work | Cost (SEK) |
|---|---:|
| Energideklaration | 1,500–4,000 for a villa; 5,000–15,000+ for larger buildings / BRF (Jan 2026 price guide, Offerta quote platform ⚠️, before the 1 Oct 2026 rules); Boverket publishes no price, which the certified energiexpert sets (2026, source: Boverket) |
| Mäklare (seller-paid; no set fee level, per FMI) | 1.0–5.4 % of price / SEK 38,500–120,000 (5th–95th percentile of seller-reported sales; 2026 data, Hittamäklare by Booli/SBAB ⚠️) |
| **Lagfart (buyer): stämpelskatt + expeditionsavgift** (juridisk person: 4.25 % + 825) | **1.5 % + 825** |
| Pantbrev (new mortgage) | 2 % of new pantbrev amount + 375 |
| Besiktning (överlåtelsebesiktning, villa) | ~7,000–15,000 (SBAB buyer guide updated 5 Feb 2026, lender guide ⚠️) |
| **Total transaction cost (buyer, new mortgage at 70 % LTV, no reusable pantbrev)** | **est. ~3 %** of price (1.5 % + 2 % × 0.70 = 2.9 %, plus fees + besiktning) |
| **Total transaction cost (cash buyer)** | **est. ~2 %** of price (1.5 % + SEK 825 + besiktning) |
| Enskilt avlopp installation | ~80,000–150,000, some higher: 80,000 is a low estimate and ~150,000 not unusual, depending on technique and site (Avloppsguiden FAQ updated 14 Sep 2026, secondary aggregator ⚠️) |
| Roof concrete tile (150 m²) | est. ~210,000–480,000 incl. moms (150 m² × SEK 1,400–3,200/m² for a new tiled roof, concrete or clay, materials + labour; the network mean of SEK 1,600/m² gives ~240,000) (2026 price guide, Byggstart contractor platform ⚠️) |
| Energy retrofit (Class C → A, classes as defined before the 1 Oct 2026 energideklaration rules) | data not publicly available — scope-dependent; price the energideklaration's recommended measures with contractor quotes (verify at https://www.boverket.se/sv/energideklaration/energideklaration/) |
| Asbestos abatement (small house) | ~5,000–20,000 for a small job such as pipe insulation; ~30,000–100,000+ for a whole roof or facade (Feb 2026 price guide, Offerta quote platform ⚠️); whole-house scope: data not publicly available — get written quotes |
| BRF stamb-renovation per apartment | ~150,000–400,000; most BRFs land at 250,000–300,000 with a standard bathroom (Sep 2026 price guide, Offerta quote platform ⚠️) |

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
- **BRF stamb-renovation cycle**: new pipes last ~50–70 years per the industry figures Offerta cites — a stambyte costs ~SEK 150,000–400,000 per apartment, most BRFs 250,000–300,000 with a standard bathroom (≈ €13,500–36,000 = SEK 150,000–400,000 / 11.112 per EUR, ECB 22 Oct 2026) (2026 data, Offerta quote platform ⚠️, guide dated 25 Sep 2026)
- **Hyresreglering** kills long-let yield in major cities
- **Strandskydd** (shoreline protection): 100 m from the shoreline by default, extendable by länsstyrelsen to max 300 m; no new buildings inside the zone (Miljöbalken 7 kap. 14–15 §§). Since Lag 2025:512, no strandskydd by default at lakes of 1 ha or less or streams 2 m wide or narrower (länsstyrelsen can reinstate it, max 100 m), nor at waters created after 30 Jun 1975 (7 kap. 13 a–13 c §§) (2026 data, source: riksdagen.se)
- **Tomträtt** apartments (Stockholm, Göteborg older areas): separate ground rent that increases
- **Bolånetak (belåningstak) 90 %** of market value for a new housing credit such as a purchase loan, up from 85 %, and **tilläggslån** (top-up on an existing mortgage) capped at 80 %, for loans taken from 1 Apr 2026 under lag (2026:226) om begränsning av bostadskrediter, which replaced Finansinspektionen's föreskrifter and allmänna råd (repealed 31 Mar 2026). **Amorteringskrav**: at least 2 %/yr above 70 % LTV, 1 %/yr above 50 % up to 70 %, none at or below 50 %; the extra 1 pp for housing debt above 4.5× gross income is abolished, but on existing loans it ends only when the borrower agrees new terms with the bank. Revaluing the home to change the amortisation pace, or now to raise borrowing room, is as a rule allowed only once every five years (2026 data, sources: Finansinspektionen 2026-03-19, regeringen.se 2026-03-05)
- **Sommarstuga** (summer cottage) often has different regime + utilities + strandskydd
- **Fjällstugor** (mountain cabins): even stricter restrictions + reindeer-husbandry concerns (Sami)
- **Hög radon**: per SGU the drivers are uranium-rich rock — alum shale, found in Skåne, Västergötland, Östergötland, Öland, Närke and along the fjällkedjan (mountain chain), and some granites and pegmatites, for which SGU names no regions — permeable ground such as gravel eskers (grusåsar), and blåbetong houses (1929–1978); many kommuner publish radonriskkartor; measurement before buying recommended (source: SGU)
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
| **Kronofogden** | Debt enforcement: seller's debts, utmätning, evictions, auctions of seized property (lawsuits sit with the tingsrätt; inteckningar + servitut are registered by Lantmäteriet) |
| **Skatteverket** | Taxeringsvärde, fastighetsavgift, capital gains (stämpelskatt on lagfart is calculated + invoiced by Lantmäteriet) |
| **BRF styrelse + förvaltning** | If bostadsrätt: financial state, assessments |
| **VA-bolag (kommunalt)** | Mains drains verification |
| **Länsstyrelse** | Strandskydd, naturreservat |
| **SGU** | Geology, gamma-radiation (uranium) maps, wells archive; radon-risk maps come from the kommun, indoor radon from measurement (SSM) |

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
| MCF Översvämningskarteringar (ex-MSB) | `https://www.mcf.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/oversvamningskarteringar/` |
| SMHI framtida medelvattenstånd (per kustkommun) | `https://www.smhi.se/klimat/framtidens-klimat/stigande-havsnivaer/framtida-medelvattenstand` |
| SGU Kartvisaren (gamma-radiation / uranium layers; no national radon map) | `https://www.sgu.se/produkter-och-tjanster/kartor/kartvisaren/` |
| Boverket | `https://www.boverket.se/` |
| Trafikverket | `https://www.trafikverket.se/` |
| Trafikverket Vägtrafikflöden (ÅDT) | `https://bransch.trafikverket.se/tjanster/trafiktjanster/Vagtrafik--och-hastighetsdata/fordonsfloden-och-hastigheter/` |
| Lastkajen (NVDB road data) | `https://lastkajen.trafikverket.se/` |
| Klimatanpassning | `https://www.klimatanpassning.se/` |

## Status

✅ **Fully populated**; fast-changing sections (`--price`, `--tax`, `--rental`, `--work`, `--risks`, `--mains`, Cost benchmarks) re-verified as of 2026-10-23; figures with no current primary source carry their source tier (secondary ⚠️, company-reported) or an est., curated, unverified, data-not-publicly-available or verify-at label (initial population 2026-04-25).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for cadastre + admin geography (Lantmäteriet, SCB), for the fiscal and statutory figures re-checked on primary sources on 2026-10-23 — fastighetsavgift caps, stämpelskatt + expeditionsavgift, pantbrev, capital gains + uppskov, VAT rates (the food-VAT cut to 31 Dec 2027 on the SFS texts, Lag 2026:118 + 2026:119), ROT/RUT and the lag (2026:226) mortgage caps (Skatteverket, Lantmäteriet, riksdagen.se, regeringen.se, Finansinspektionen) — for the `--rental` rules and figures (SFS 2026:772 + 2026:776, Prop. 2025/26:187, Riksdag decisions 2025/26:CU5 + CU31, Skatteverket, Bostadsförmedlingen, Regeringskansliet; the hemförsäkring bullet rests on Konsumenternas Försäkringsbyrå; EU 2024/1028 has applied directly since 20 May 2026, so there is nothing to transpose; the hyresreglering bullet is qualitative) and for the `--work` figures (SCB, Skatteverket, Bolagsverket). MEDIUM for `--price` (bostadsrätt benchmarks come from a secondary aggregator, Svensk Mäklarstatistik; the Hemnet share and the Fastighetsbyrån figures are company-reported; the Hemnet sold-price URL rests on archived captures), `--risks` + `--mains` (authority sources re-checked — SGU, SSM, Boverket BFS texts, SOU 2019:7, Klimatanpassning.se, Lantmäteriet, Naturvårdsverket; the VA fees come from Svenskt Vatten 2026, an industry association; lead paint and permafrost are labelled unverified, the BRF document rows and red-flag thresholds are curated practice, the four mains build-cost rows stay est. without a published source, and the Swedish UWWTD transposition rules rest on a Naturvårdsverket proposal that is not yet law) and `--traffic` (verdict bands are curated thresholds). LOW for the market-price rows in Cost benchmarks (energideklaration, mäklare, besiktning, avlopp, roof, asbestos, stamb): each rests on one secondary or commercial source (Offerta, Hittamäklare, SBAB, Avloppsguiden, Byggstart), not a primary source; the energy-retrofit row has no published figure.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | AB share capital, egenavgifter 28.97 % and SCB 2025 salary figures re-checked; Monster removed; job-board, F-skatt, A-kassa and union rows not re-checked |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Hemnet share, Booli owner (SBAB), Blocket Bostad (rentals, Qasa) and the Länsförsäkringar name + URL corrected; agency sites live |
| Active fiscal incentives (2025-2026) | 2026-10-23 | 2026-10-23 refresh wave | ROT 30 %, RUT 50 % with the SEK 75,000 combined cap, grön teknik, Boverket småhus energy grant and the 0.10 pp bank discount checked against Skatteverket, Boverket, SBAB + Nordea |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Kronofogden, Skatteverket and SGU roles corrected; other rows confirmed |
| `--price` | 2026-10-23 | 2026-10-23 gap-closing pass | SCB Q3 2026 index, the bostadsrätt figures (Svensk Mäklarstatistik, update of 8 Oct 2026; the rural Norrland row stays from the refresh) and the SCB 2025 villa averages re-read; avgift range replaced by SCB 2024 averages in SEK; Min fastighet login and valuation tools corrected; Hemnet sold-price URL (archived captures) and Fastighetsbyrån figures (company-reported) labelled |
| `--rental` | 2026-10-23 | 2026-10-23 gap-closing pass | SFS 2026:772 and bostadsrättslagen 7 kap. 10–11 §§ (Lag 2026:776) re-read; schablonavdrag SEK 40,000 and 30 % re-confirmed (Skatteverket); hemförsäkring, platform-reporting and 12 % moms (above SEK 120,000) bullets replace the unverified ones; pre-reform sublet benchmark aligned to Prop. 2025/26:187 |
| `--tax` | 2026-10-23 | 2026-10-23 gap-closing pass | 2008 origin (SFS 2007:1398) and food-VAT window (Lag 2026:118 + 2026:119) read in the SFS texts; mäklare 2–4 % replaced by FMI (no set fee level) plus a labelled Hittamäklare range; Future-risk bullets checked against bet. 2025/26:SkU15 |
| Cost benchmarks (SE 2026) | 2026-10-23 | 2026-10-23 gap-closing pass | Market-price rows sourced to Offerta, Hittamäklare + FMI, SBAB, Avloppsguiden and Byggstart (secondary ⚠️, 2026); energy retrofit is data not publicly available; lagfart + pantbrev (Lantmäteriet) and both est. totals hold |
| `--risks` | 2026-10-23 | 2026-10-23 gap-closing pass | Ljusdal 2018 (SOU 2019:7); radon regions replaced by SGU's alum-shale list; primärenergital start corrected to BBR 25 (BFS 2017:5); BFS 2026:9 transition confirmed; climate bullets from Klimatanpassning.se (SMHI); lagfart + fastighetsutdrag rows sourced to Lantmäteriet; lead paint, permafrost, BRF document rows and red-flag thresholds labelled |
| `--mains` | 2026-10-23 | 2026-10-23 gap-closing pass | VA SYD (archived 2026-01-20) and NSVA's member kommuner confirmed; Svenskt Vatten 2026 edition: mean 204,954 / median 192,418 (computed from the per-kommun file), usage fee 12,537; UWWTD transposition deadline 31 Jul 2027 (Naturvårdsverket); the Swedish rules are a proposal, not yet law; four build-cost rows stay est. |

Sections without a row default to the Status footer date, except Country profile, `--traffic` (5-year re-research cadence), Caveats, Quirks, Source URL templates and Reddit / forum sources: they were partly re-checked on 2026-10-23 but keep unverified items (see Update history), so they keep the initial-population date (2026-04-25).

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
- **2026-10-23** — Refresh wave: fast-changing sections + audit findings re-checked against primary sources (secondary sources labelled). Counts per section are changed / confirmed / unverifiable. Playbook-level date re-stamped 2026-10-23: every fast-changing section is now re-verified — `--work` in the refresh, `--price`, `--rental`, `--tax`, Cost benchmarks, `--risks` and `--mains` in the gap-closing pass; Country profile, `--traffic` (5-year re-research cadence), Caveats, Quirks, Source URL templates and Reddit / forum sources stay refreshed, not re-verified.
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
  - Gap-closing pass (confirmed / changed / relabelled): `--price` 29 / 3 / 2; `--rental` 8 / 4 / 0; `--tax` 2 / 2 / 0; Cost benchmarks 0 / 7 / 1; `--risks` 2 / 8 / 5; `--mains` 2 / 4 / 0 — all closed; total 43 / 28 / 8. Main changes: avgift range → SCB 2024 averages in SEK, Min fastighet login and valuation tools corrected, Hemnet sold-price URL (archived captures) and Fastighetsbyrån figures (company-reported) labelled; hemförsäkring, platform reporting, 12 % moms above SEK 120,000 and BRF consent (Lag 2026:776) re-sourced; 2008 origin and food-VAT window on the SFS texts, mäklare 2–4 % → FMI (no set fee level) + Hittamäklare range; market-price cost rows sourced to secondary price guides (⚠️), energy retrofit → data not publicly available; Ljusdal 2018 (SOU 2019:7), radon regions → SGU alum-shale list, primärenergital start corrected to BBR 25 (2017), climate bullets from Klimatanpassning.se, lead paint, permafrost and BRF rows labelled; VA SYD + NSVA confirmed, Svenskt Vatten 2026 figures (mean 204,954 / median 192,418), UWWTD transposition deadline 31 Jul 2027 (Naturvårdsverket proposal). Caveats: radon line aligned with SGU (alum-shale regions; no granite regions named) and stamb line with the Offerta 2026 range.
