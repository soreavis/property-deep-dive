# Serbia 🇷🇸 — Property Due-Diligence Playbook

ISO2: `rs`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`11000` Belgrade, `21000` Novi Sad, `18000` Niš, `34000` Kragujevac)
- **Admin levels**: 5 statistical regions (Beogradski, Vojvodina, Šumadija i Zapadna Srbija, Južna i Istočna Srbija, Kosovo i Metohija; RGZ and RZS publish no data for the last) + 29 upravni okruzi (administrative districts; Grad Beograd belongs to none) + 174 local self-government units by law (145 opština + 28 gradova + Grad Beograd, Kosovo included) + Vojvodina autonomous province + Kosovo (disputed) *(2026-11-03 verified, source MDULS register (174 units) + Government Uredba on regional development (regions) + sr.wikipedia (145/28 split, 29 districts; secondary))*
- **Currency**: **RSD** (Serbian dinar); 1 EUR = 117.3892 RSD (NBS official middle rate, 14 Oct 2026); managed float regime *(2026 data, source NBS kursna lista + NBS Monetary Policy Programme 2026)*
- **Languages**: Serbian (official); Hungarian (Vojvodina), Albanian, Bosnian, Romanian, Croatian (regional minorities)
- **Cadastre**:
  - **RGZ (Republički Geodetski Zavod)**: `https://www.rgz.gov.rs/`
  - **eKatastar public portal**: `https://katastar.rgz.gov.rs/eKatastarPublic/PublicAccess.aspx`
- **Identifier**: parcela + KO (cadastral municipality)
- **Ownership types**: pravo svojine (full ownership); etažna svojina (condominium for apartments); pravo zakupa (lease)
- **EU candidate** since March 2012; accession negotiations opened 21 January 2014, 22 of 35 chapters opened and 2 provisionally closed *(2026-11-03 verified, source European Commission enlargement page)*

## Section: `--price`

### Primary sources

- **RGZ (Republički geodetski zavod)**: `https://www.rgz.gov.rs/` — quarterly *RGZ indeks cena stanova* and half-yearly *Statistika cena nepokretnosti* (closed-sale prices from the Registar cena nepokretnosti; Kosovo not covered)
- **NBS (National Bank of Serbia)**: `https://www.nbs.rs/en/indeks/index.html` — official dinar middle rate + key policy rate (the homepage carries no house-price index; use RGZ)
- **RZS (Republički Zavod za Statistiku)**: `https://www.stat.gov.rs/`
- **FRED `QRSN628BIS`** (BIS nominal residential property prices for Serbia, 2010=100; real series `QRSR628BIS`) — secondary aggregator
- **Investropa, Global Property Guide** — secondary aggregators

### Listing platforms

- **HaloOglasi** — DOMINANT *(wisdom, not data — no published market-share figure)*: `https://www.halooglasi.com/`
- **Nekretnine.rs**: `https://www.nekretnine.rs/` (self-reports 80,000+ listings — per listing site)
- **4zida.rs**: `https://www.4zida.rs/`; **KupujemProdajem** (general classifieds with a Nekretnine category): `https://www.kupujemprodajem.com/`
- **Sasomange** — ❌ DEPRECATED — dead on 2026-11-03 (sasomange.rs no longer loads; closure from 2 June 2025 announced in forum and LinkedIn posts, forum-tier); use HaloOglasi / 4zida
- **BeoBuild** (`https://beobuild.rs/`) — Belgrade construction and urban-development news (project pipeline), not a listing portal
- All portals show seller-controlled asking prices; RGZ shows closed sales

### 2026 price benchmarks (RGZ closed-sale apartment prices, H1 2026)

| Region | EUR/m² (avg) | YoY |
|---|---:|---:|
| **Belgrade Savski venac** (KO) | 4,210 (median 4,117) | +9.86% |
| **Belgrade Stari grad** (KO) | 4,030 (median 4,015) | +10.15% |
| **Belgrade Vračar** (KO) | 3,639 (median 3,619) | +11.79% |
| **Belgrade Novi Beograd** (KO) | 3,385 (median 3,431) | +15.74% |
| **Belgrade Waterfront** (new-build complex, Savski venac) | 5,821 (median 5,528; 55 sales) | — |
| **Belgrade** (10 inner-urban KO) | 3,219 (median 3,169) | +13.94% |
| **Novi Sad** | 2,359 (median 2,356) | +10.16% |
| **Niš** | 1,765 (median 1,771) | +14.52% |
| **Kragujevac** | 1,575 (median 1,542) | +13.07% |
| **Serbia** (excl. Kosovo) | 1,918 (median 1,800) | — |
| **National YoY (RGZ index)** | — | **+5.25% Q2 2026** (Belgrade region +5.65%) |

*(2026 data, source RGZ Statistika cena nepokretnosti za I polugodište 2026, Aug 2026 + RGZ index release 14 Aug 2026)*. The YoY in the city and KO rows is RGZ's change in the H1 average against H1 2025, which RGZ states is not a price index; the index row is RGZ's price-index measure. KO (katastarska opština) averages are not a valuation of a specific apartment: pull comparable sales from the RGZ Registar cena nepokretnosti.

**RGZ indeks cena stanova**: 200.98 Q2 2026 (+1.19% QoQ; existing +5.98% YoY, new-build +3.86% YoY) *(2026 data, source RGZ release 14 Aug 2026)*
**BIS residential property prices** (FRED, 2010=100): nominal `QRSN628BIS` 259.83, real `QRSR628BIS` 122.94, Q1 2026 *(2026 data, source FRED, updated 25 Jun 2026)*

### Compute

1. EUR/m² = price / **korisna površina** (usable area). Serbia's design norms define a flat's size as its neto korisna površina, computed under SRPS U.C2.100:2002 (Pravilnik o uslovima i normativima za projektovanje stambenih zgrada i stanova, Art. 2); RGZ's Statistika cena does not say which area its EUR/m² divides by *(2026-11-04 verified, source Pravilnik consolidated text on paragraf.rs + RGZ Statistika cena nepokretnosti za I polugodište 2026)*
2. **Currency**: residential typically transacted in RSD or EUR-equivalent; commercial often EUR-denominated
3. **Belgrade Waterfront** ongoing development — premium tier
4. Cross-check the **RGZ index / Statistika cena** (closed sales) against **HaloOglasi** / **4zida** asking prices (seller-controlled)

### Key terms

- Pravo svojine = ownership right
- Etažna svojina = condominium (apartment)
- KO = katastarska opština (cadastral municipality)
- Energetski pasoš = energy passport
- List nepokretnosti = property sheet (cadastre extract)

---

## Section: `--traffic`

### Sources

- **Putevi Srbije d.o.o.** (state-road operator, a JP until the Government decision changing its legal form, Sl. glasnik RS 115/2025): `https://www.putevi-srbije.rs/` — PGDS by section for state roads IA, IM, IB, IIA and IIB, latest year 2025 (preliminary results)
- **Sekretarijat za saobraćaj Belgrade**: city traffic data

### Key term

**PGDS (Prosečan godišnji dnevni saobraćaj)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (Belgrade arterials, državni putevi)
- 🔴 > 35,000 v/d (autoput A1/E75 and A3/E70 around Belgrade — A1 Tranšped–Vrčin 60,928, A3 Dobanovci–Beograd 51,278, A1 bypass section Ostružnica–Orlovača 39,547; Boulevard Vojvode Stepe is a city street outside the state-road tables, verify with the Sekretarijat za saobraćaj). Far from Belgrade the same motorways fall to 🟡/🟠: A1 at the Horgoš border 6,728, A3 at Batrovci 8,081 *(2025 preliminary PGDS, source Putevi Srbije d.o.o. table for state roads IA)*

---

## Section: `--tax`

### Annual property tax — Porez na imovinu (statutory maxima, ZPI Art. 11 — each local self-government sets its own rate up to these caps; verify its current odluka)

**Local self-government (progressive)**:

| Property value | Rate (max) |
|---|---:|
| Up to RSD 10M (≈ €85k at RSD 117.37/EUR, NBS middle rate 9 Oct 2026, computed) | **0.4%** |
| RSD 10–25M | **0.6%** |
| RSD 25–50M | **1.0%** |
| > RSD 50M | **2.0%** |

Bands are marginal: each rate applies only to the part of the base above the band floor; land held by taxpayers who keep no business books is taxed at up to 0.30% *(2026-11-03 verified, source Zakon o porezima na imovinu Art. 11, paragraf.rs consolidated text to Sl. glasnik RS 94/2024)*

- **Threshold**: RSD 400,000 — no tax when the total base of all the owner's property in that municipality does not exceed it (Art. 12)
- **50% reduction** for the house or apartment where the taxpayer lives and has registered residence (max RSD 20,000 reduction, Art. 13)
- **Quarterly payment**: within 45 days of the start of each quarter (Art. 39) — mid-Feb, mid-May, mid-Aug, mid-Nov

### Transaction taxes

- **Porez na prenos apsolutnih prava** (transfer): **2.5%** on resale (ZPI Art. 30). **Seller is statutorily liable** (Art. 25); the buyer is a subsidiary guarantor by law and becomes jointly liable once the contract puts the tax on them (Art. 42). Contracts can shift it to the buyer and, per one agency blog, often do — read the ugovor carefully *(2026-11-04 verified, source paragraf.rs consolidated ZPI; practice is lower tier, not official: CMS Expert Guide to commercial real estate, updated 24 Apr 2018 — rates/figures may have changed since — and City Expert agency blog, 25 Jul 2025)*
- **First-apartment exemption** (transfer tax): adult RS citizen with permanent residence, first apartment ≤40 m² → exempt from transfer tax; +15 m² per qualifying family member who hasn't owned since 1 July 2006. Above the cap, tax due on excess area only. The buyer must not have owned a flat in Serbia since 1 July 2006; citizenship is a condition, so foreign buyers do not qualify *(2026-11-04 verified, source ZPI Art. 31a, paragraf.rs)*
- **PDV (VAT)**: **20%** standard; **10% on first-sale residential** (transfer of the right of disposal on residential buildings and economically divisible units, ZPDV Art. 23; replaces transfer tax). Refund for a first-apartment buyer — adult Serbian citizen resident in Serbia who has not owned a flat in Serbia since 1 July 2006 and has paid the full price to the seller's account: VAT on up to 40 m² + 15 m² per household member who also has not owned one (ZPDV Art. 56a) *(2026-11-03 verified, source paragraf.rs consolidated ZPDV to Sl. glasnik RS 80/2026)*
- **Notary fees** (solemnizacija of the sale contract): a value scale, not a percentage — RSD 25,920 incl. VAT for a RSD 5–7M deal, RSD 36,288 for RSD 10–14M, then +RSD 1,296 (60% of RSD 2,160) per started RSD 1M above 14M; the scale fee is capped at RSD 864,000, so solemnizacija tops out at RSD 518,400 (60%, computed) *(Javnobeležnička tarifa in force since 19 Jul 2025, source paragraf.rs tabular tariff)*. Computed at RSD 117.37/EUR (NBS middle rate 9 Oct 2026): €50k ≈ 0.44%, €100k ≈ 0.31%, €200k ≈ 0.21% of price
- **Cadastre registration** (RGZ): the notary sends the solemnised contract to the cadastre ex officio via e-šalter (Zakon o postupku upisa u katastar nepokretnosti i katastar infrastrukture Art. 22) and the buyer, in whose favour the entry is made, pays the fee (Art. 30) — RSD 7,010 for a change of owner on one document + RSD 2,100 per further document in the chain + RSD 430 request fee (Zakon o republičkim administrativnim taksama TB 215b + TB 1, dinar amounts adjusted by Sl. glasnik RS 54/2026) ≈ €63 *(2026 data, source paragraf.rs consolidated texts)*

### Personal income tax (PIT) framework

- **Employment income**: 10% flat (ZPDG Art. 16) on salary above the monthly non-taxable amount — RSD 34,221 in 2026, rising to RSD 37,369 from 1 Jan 2027 (Art. 15a as amended by Sl. glasnik RS 80/2026) *(2026 data, source paragraf.rs consolidated ZPDG + Cekos In and Bilans Control, Oct 2026)*
- **Annual PIT top-up (synthetic on global net)**: **10% on taxable income up to RSD 10,878,192** (6× the 2025 average annual salary of RSD 1,813,032); **15% above** that threshold (ZPDG art. 89). Filing threshold 2025 net: RSD 5,439,096 (3×). *(2025 income, Poreska uprava brochure Apr 2026, verified 2026-10-21; RSD 9,749,016 was the 2024-income 6× band)*
- **Other categories** flat 10–20% (royalties 20%, capital gains 15%, rental 20% gross or 15% effective after 25% normative deduction). Young taxpayers <40 receive an extra allowance of RSD 5,439,096. *(2026-11-03 verified, source paragraf.rs consolidated ZPDG Arts 16, 65g, 65v, 77, 87 + Poreska uprava annual PIT brochure Apr 2026; earlier KPMG RS Annual PIT alert Feb 2026 + PwC Tax Summaries)*

### Capital gains

- **15% PIT** on real-estate capital gains (ZPDG Art. 77, consolidated to Sl. glasnik RS 80/2026)
- **Exempt after 10-year continuous holding** (CRITICAL; Art. 72a item 5 — real-estate rights count as rights under Art. 72)
- **Also not taxed**: rights acquired by first-line inheritance; transfers between spouses and between direct-line blood relatives; transfers between ex-spouses tied to the divorce (Art. 72a). **Exempt**: proceeds reinvested within 90 days in the taxpayer's own or family housing in Serbia (Art. 79; refund if reinvested within 12 months, proportional if only part is reinvested, Art. 80). The ZPDG has no standalone primary-residence exemption *(2026-11-03 verified, source paragraf.rs consolidated ZPDG + PwC Tax Summaries, last reviewed 7 Aug 2026)*

### Total transaction cost (buyer side)

- Resale: ~3% before agency and attorney fees (computed: 2.5% transfer tax where the contract puts it on the buyer + notary ≈ 0.21–0.44% + RGZ ≈ €63, which gives 2.7–3.1% on a €50k–€200k price)
- New build: 10% VAT included in the price, no transfer tax + notary ≈ 0.21–0.44% + RGZ ≈ €63, which gives 0.24–0.57% on top of a €50k–€200k price (computed as above)

### Future risk

- EU candidate accession reforms continuing
- NBS key rate 5.75% since the 25 bp cut of 12 Sep 2024, kept unchanged on 8 Oct 2026; next rate-setting meeting 12 Nov 2026 *(2026 data, source NBS decision of 12 Sep 2024 + NBS press release 8 Oct 2026)*
- Belgrade Waterfront ongoing

---

## Section: `--rental`

### Long-term residential

- **Zakon o stanovanju i održavanju zgrada**
- Tenant protection moderate
- Standard 1-3 yr contracts

### Short-let (Airbnb)

- **Tourist tax (boravišna taksa)**: **RSD 240/person/day in Belgrade from 15 October 2026** (was RSD 160 since 2020; ≈ €2.04 at the NBS middle rate of 117.3892 RSD/EUR, 14 Oct 2026). Belgrade is a category-I tourist place; the Government Uredba o najvišem i najnižem iznosu boravišne takse (Sl. glasnik RS 90/2026) sets RSD 190–240 for that category and the city chose the maximum. Guests aged 7–15 pay 50% (Zakon o ugostiteljstvu). A natural-person host in domaća radinost pays the tax as an annual lump sum instead (Art. 71) *(2026 data, source Grad Beograd draft Odluka o izmeni Odluke o boravišnoj taksi Oct 2026 + Paragraf 13 Oct 2026 + Zakon o ugostiteljstvu consolidated text on paragraf.rs)*
- **Categorisation**: the host needs a rešenje o kategorizaciji from the local self-government before the first guest (Zakon o ugostiteljstvu Arts 20 + 31; valid three years, Art. 20) and must post name + phone at the entrance (Art. 31); guests are registered through E-turista, the central information system (Arts 2 + 15). That law has no provision requiring a registration number on listings; the rešenje's number goes into the host's contract with an intermediary (Art. 33). Other laws, bylaws and local rules may add one — verify with the local tourism inspectorate *(2026 data, source Zakon o ugostiteljstvu consolidated text on paragraf.rs)*
- **Belgrade tightening 2024-2025** *(wisdom, not data — verify with Grad Beograd)*

### Tax on rental

- Resident: **effective 15% on gross rental** after the 25% normative-cost deduction (20% × 75% = 15%); actual costs may be claimed instead, on proof (ZPDG Arts 65v + 65g) *(2026 data, source ZPDG consolidated text on paragraf.rs + PwC Tax Summaries reviewed 7 Aug 2026)*
- Letting a flat or room for more than 30 days without hospitality services is rental income; accommodation for up to 30 days is excluded and taxed under ZPDG Art. 84b (Art. 65v st. 2)
- Non-resident individual: the same tax as a resident on Serbian rent, 20% after the 25% normative-cost deduction, effective 15% of gross (20% × 75% = 15%) (ZPDG Arts 8, 65v + 65g; Ministry of Finance opinion 430-00-274/2017-04 of 26 Feb 2018). The tax is withheld only when the tenant is a legal entity or entrepreneur (ZPDG Art. 99 st. 1 tač. 4). With a private tenant the non-resident self-assesses and files a return (ZPDG Arts 96 + 100a) and must name a resident tax proxy (poreski punomoćnik) to the Tax Administration within 10 days of the first income (ZPPPA Art. 14 st. 2); no proxy is needed for income taxed at source with no return to file (ZPPPA Art. 14 st. 3). On withheld tax, treaty relief needs proof of treaty residence and beneficial ownership (ZPDG Art. 107a) *(2026 data, source ZPDG + ZPPPA consolidated texts on paragraf.rs; 2018 opinion reproduced on aktivasistem.com, secondary — rates/figures may have changed since)*
- Non-resident company: 20% withholding on rent for Serbian real estate paid by a resident legal entity, unless a tax treaty provides otherwise; 25% for a recipient in a preferential-tax jurisdiction (ZPDPL Art. 40 st. 1 + 4). Where the payer need not withhold, the company pays the 20% by assessment, filing through a tax proxy within 30 days (ZPDPL Art. 40 st. 8 + 10) *(2026 data, source ZPDPL consolidated text on paragraf.rs + PwC Tax Summaries reviewed 7 Aug 2026)*

---

## Section: `--work=<profession>`

### Sources

- **NSZ (Nacionalna služba za zapošljavanje)**: `https://www.nsz.gov.rs/`
- **Poslovi.infostud.com**, **HelloWorld.rs**, **LinkedIn RS**

### Self-employment

- **Preduzetnik** (sole trader)
- **DOO** (limited): min RSD 100 capital (Zakon o privrednim društvima Art. 145) *(2026-11-03 verified, source Paragraf Lex consolidated text)*
- **Paušalna obaveza** (flat rate) for small business
- **PDV** registration: mandatory once turnover in the previous 12 months exceeds RSD 8,000,000 (ZPDV Art. 38) *(2026 data, source ZPDV consolidated text through Sl. glasnik RS 80/2026 on paragraf.rs)*

### Salary benchmarks (RZS, August 2026)

- Average monthly gross / net (RZS, by area):
  - Serbia: RSD 161,953 / 117,282 (≈ €1,380 / €999); **median net RSD 93,325** (≈ €795; 79.6% of the average net, computed 93,325 ÷ 117,282)
  - Beogradski region: RSD 198,684 / 143,965 (≈ €1,693 / €1,226)
  - Grad Novi Sad: RSD 183,261 / 132,537
  - Grad Niš: RSD 157,844 / 114,121; Kragujevac: RSD 158,107 / 114,351
  - Region Šumadije i Zapadne Srbije: RSD 139,670 / 101,130; Region Južne i Istočne Srbije: RSD 142,465 / 103,112
  - *(2026 data, source RZS saopštenje "Prosečne zarade po zaposlenom, avgust 2026"; regional rows are averages, not medians; EUR at the NBS middle rate of 117.3892, 14 Oct 2026)*
- **Minimalna cena rada**: **RSD 371 net per working hour** in 2026 (Sl. glasnik RS 78/2025), i.e. RSD 65,296 net in a 176-hour month (computed 371 × 176; ≈ €556); **RSD 405 net per hour from 1 January 2027** (Sl. glasnik RS 75/2026) *(2026 data, source Socijalno-ekonomski savet RS)*

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Republički seizmološki zavod (RSZ)** | `https://www.seismo.gov.rs/` | Seismic monitoring, earthquake catalogue (Mw ≥ 3.5), seismic hazard maps for 95/475/975-year return periods (2018 revision; informative only, design uses the maps of the regulations in force) |
| **RHMZ (Republički Hidrometeorološki Zavod)** | `https://www.hidmet.gov.rs/` | Weather, hydrology, floods |
| **Ministarstvo unutrašnjih poslova — Sektor za vanredne situacije** | `https://www.mup.gov.rs/` | Civil protection, emergency response |
| **SEPA (Agencija za zaštitu životne sredine)** | `https://vazduh.sepa.gov.rs/` | Live air-quality data; annual air-quality report |

### Specific risks

#### Earthquake — moderate

- **2010 Kraljevo** (3 Nov 2010): **Mw 5.5** (RSZ catalogue; RSZ local magnitude 5.4), epicentral intensity 7–8 *(RSZ report of 1 Dec 2010)*. About 16,000 damage reports for as many objects, more than 1,500 objects unusable and 400–500 houses to be demolished (minister for public administration and local self-government, RTV/Tanjug 22 Nov 2010; secondary); damage estimated at more than EUR 100 million (IFRC 31 Aug 2011 via ReliefWeb; secondary)
- **1922 Lazarevac Mw 5.7** (24 Mar; the 6.0 often quoted is the catalogue's surface-wave Ms), **1927 Rudnik Mw 5.8** (15 May), **1980 Kopaonik Mw 5.9** (18 May), **1998 Mionica Mw 5.5** (29 Sep) *(homogenised Mw, source RSZ Katalog zemljotresa Mw ≥ 3.5, entries to Aug 2017)*
- Belgrade felt intensity 4 during the 2010 Kraljevo quake *(RSZ field survey, report of 1 Dec 2010)*
- **Vlasinsko / Pirot** zone elevated; Belgrade lower

#### Floods

- **2014 catastrophic floods** (May 2014): in Serbia the Sava, Tamnava, Kolubara, Jadar, Zapadna Morava, Velika Morava, Mlava and Pek rose; the **Bosna** flooded in BiH and fed the Sava (NOT Drava — common confusion). Disaster effects EUR 1.5 billion in the 24 assessed municipalities, EUR 1.7 billion including the other affected municipalities *(2014 data, source Government of Serbia / EU / UN / World Bank Recovery Needs Assessment, July 2014) — rates/figures may have changed since*
- Obrenovac (a Belgrade city municipality) was flooded when Kolubara and Tamnava dikes failed; the Kolubara rose about 7 m on 14–16 May and the Sava about 3.5 m on 14–20 May, receding over 2–3 weeks *(same RNA; dike breaches per MDPI Sustainability 2020, secondary)*
- Climate change increasing extreme rainfall

#### Air quality

- **Belgrade agglomeration air was category II (polluted) in 2025**: PM10, PM2.5 and NO2 limit values exceeded, benzo(a)pyrene and ground-level ozone above target values; Novi Sad, Niš, Pančevo, Smederevo, Bor, Kosjerić and Užice also category II. Category II is now the worst class: the Zakon o zaštiti vazduha (Sl. glasnik RS 51/2025, Art. 20) keeps only two categories, so the step down from category III (over-polluted), which these same eight agglomerations had in 2024, is a change of scale, not by itself cleaner air. Particulate concentrations are far higher in the heating season *(2025 data, source SEPA Godišnji izveštaj o stanju kvaliteta vazduha 2025, `https://sepa.gov.rs/wp-content/uploads/2026/10/Vazduh2025.pdf`; 2024 category and heating-season pattern from the 2024 report) — rates/figures may have changed since*
- Main particulate source nationally: small heating plants (< 50 MW) and household stoves, mostly firewood (per SEPA's 2024 report) — 83% of PM2.5 and 64% of PM10 emissions; road traffic gives 25% of NOx *(2024 emissions data, source SEPA Godišnji izveštaj o stanju kvaliteta vazduha 2025) — rates/figures may have changed since*

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **Yugoslav era 1945-1990** | Asbestos common, panel buildings (paneli) |
| **Pre-1964** | Designed before the provisional seismic rules of Sl. list SFRJ 39/64 (30 Sep 1964); the earlier 1948 provisional loading regulations came with a seismic zoning map (Sl. list FNRJ 61/48, per a 1CroCEE conference paper, secondary). A public-use building designed before 39/64 must meet current seismic rules after reconstruction |
| **1964 – Jun 1982** | Provisional seismic rules, Sl. list SFRJ 39/64 |
| **Jun 1982 – Dec 2019** | Buildings (visokogradnja): Pravilnik o tehničkim normativima za izgradnju objekata visokogradnje u seizmičkim područjima, Sl. list SFRJ 31/81 (published 5 Jun 1981, in force one year later), 49/82, 29/83, 21/88, 52/90; it replaced the 39/64 rules for buildings *(source: its Art. 116–117 via paragraf.rs; publication date per the reprint on the University of Belgrade Faculty of Civil Engineering site, and Frontiers in Built Environment 2020, secondary)* |
| **Since 26 Dec 2019** | Eurocode-based Pravilnik za građevinske konstrukcije (Sl. glasnik RS 89/2019, 52/2020, 122/2020; seismic design per SRPS EN 1998) repealed both; permit files lodged within 3 months could still use the old rules *(source: Pravilnik Art. 24, 99, 100 via paragraf.rs + Institut za standardizaciju Srbije)* |
| **Belgrade Waterfront 2014+** | Premium new-build standards |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski pasoš** (sertifikat o energetskim svojstvima, issued via CREP) | New buildings: part of the use-permit file. Existing buildings: the law requires it at notarisation of a sale or lease, but it is not attached until the owners' deadlines run out, counted from 4 Aug 2023: residential 10 years (Aug 2033), commercial 5 years (Aug 2028), public-use buildings in public ownership 3 years (Aug 2026). Building under construction: attached after the use permit and cadastre entry *(source: Zakon o planiranju i izgradnji Art. 4 + Art. 84 of Sl. glasnik RS 62/2023, consolidated text to 80/2026 on paragraf.rs; in-force date per JPM law-firm note, secondary)* |
| **Notar + ugovor o kupoprodaji** | Mandatory — the sale contract must be a notarially solemnised deed (Zakon o prometu nepokretnosti Art. 4, Sl. glasnik RS 93/2014, 121/2014, 6/2015) |
| **Geodetski snimak** (survey) | Cadastre |
| **List nepokretnosti** | Title verification |

---

## Section: `--mains`

### Sources

- **JKP Beogradski vodovod i kanalizacija** (BVK, Belgrade): `https://www.bvk.rs/` — household tariff from 1 Jan 2026: water RSD 95.52/m³, wastewater RSD 38.60/m³, fixed system-readiness charge RSD 209.96/month incl. VAT (+9.5% for all user categories) *(2026 data, source BVK Cene page)*
- Per-municipality elsewhere
- Belgrade supply: groundwater from 149 wells plus treated river water — five production plants (three river-water, including Makiš 1 from 1987 and Makiš 2 from Sept 2014; two groundwater), 3,955 km of raw- and clean-water mains, about 550,000 m³/day *(BVK Istorijat page, undated — figures may have changed since)*; aging infrastructure

### Costs

| Scenario | Cost (EUR) |
|---|---:|
| Mains connection | est. 1,500–4,000 |
| Septic upgrade | est. 2,500–6,000 |
| Bored well | est. 3,000–8,000 |

The est. ranges are planning figures with no published tariff behind them; calibrate against the operator's price list and two written contractor quotes. Belgrade (BVK) fee items alone, excl. VAT: water-connection participation incl. a Ø20 meter RSD 44,937.94 urban / RSD 56,173.99 suburban; sewer-connection participation RSD 67,996.37; the price list's "Registracija V urbana – I kategorija" item RSD 62,557.04 *(2026 data, source BVK Cenovnik radova i usluga 2026)*

---

## Cost benchmarks (RS 2026)

| Work | Cost (EUR) |
|---|---:|
| Energetski pasoš | 100–250 |
| Notar fees (solemnizacija) | ≈0.21–0.44% (computed from the tariff scale, €50k–€200k) |
| Transfer tax | 2.5% |
| **Total transaction cost (buyer)** | **~3%** of price before agency/attorney fees (computed for a resale with the transfer tax on the buyer, adding the RGZ fee ≈ €63 from `--tax`: 2.7–3.1% at €50k–€200k) |
| Roof renovation | 4,000–12,000 |
| Energy retrofit | 8,000–25,000 |
| Heat pump | 5,000–10,000 |
| Solar PV (5kW) | 3,500–7,000 |

Energetski pasoš and works rows are est. contractor ranges from the 2026-04 research with no primary source — verify with local quotes.

## Active fiscal incentives (2025-2026)

- **Youth first-home loan programme** (Government, not NBS): Zakon o utvrđivanju garantne šeme i subvencionisanju dela kamate kao mera podrške mladima u kupovini prve stambene nepokretnosti (Sl. glasnik RS 19/2025, 51/2025, 109/2025 i 56/2026) — Serbian citizens resident in Serbia aged 20–35 at application who have never owned a home; 1% minimum down payment; loan up to €100,000 in RSD; fixed rate up to 3.5% for the first 72 months with a 2 pp state subsidy; 40% state guarantee for 10 years; scheme capped at €900M of loans; the borrower must live in the property and may not let it for 6 years; the programme runs four years from the law's start (Arts 2, 3, 5–8). Foreign buyers do not qualify *(2026 data, source paragraf.rs consolidated text)*
- **Energy-renovation subsidies** for houses and apartments (Ministarstvo rudarstva i energetike with local self-governments and World Bank support, project "Čista energija i energetska efikasnost za građane" — not EU pre-accession funding): up to 50% per measure, up to 65% for a package, up to 90% for socially vulnerable households; insulation, windows/doors, boilers, solar collectors/panels; calls are published by each municipality *(2026 data, source mre.gov.rs 12 Oct 2026)*
- **Expo 2027 Belgrade** (15 May – 15 Aug 2027, on 25 ha in a brand-new urban zone) — state-hosted event, not a buyer incentive *(source expobelgrade2027.org)*

## Common listing platforms

- **HaloOglasi** — DOMINANT *(wisdom, not data)*
- **Nekretnine.rs**, **4zida.rs**, **KupujemProdajem** (Nekretnine category)
- **Sasomange** — ❌ DEPRECATED — dead on 2026-11-03 (site no longer loads; closure announced for 2 June 2025, forum-tier)
- **BeoBuild** — Belgrade construction and urban-development news, not a listing portal

## Caveats unique to RS

- **EU candidate since 1 March 2012** — accession negotiations opened 21 January 2014 and are ongoing *(source European Commission enlargement page)*
- **Foreign-buyer reciprocity rules** (Zakon o osnovama svojinskopravnih odnosa Arts 82a–82v) — every foreign natural person, EU or not, may buy an apartment or residential building on the same terms as a Serbian citizen only where reciprocity exists with their state; foreigners cannot own agricultural land except as the Zakon o poljoprivrednom zemljištu allows under the SAA. Where reciprocity is in doubt, the court or cadastre — or the buyer — may ask the Ministarstvo pravde for an explanation (objašnjenje), not an approval; request fee (republička administrativna taksa) RSD 2,510 for a natural person or RSD 17,340 for a legal person, entrepreneur or attorney, per the Ministry's two payment slips; processing time not published *(2026 data, source Ministarstvo pravde reciprocity page + payment slips, mpravde.gov.rs)*
- **Reciprocity list** (Ministarstvo pravde, read 2026-11-03): treaty reciprocity for purchases only with the UK, US, Netherlands and Japan; the Ministry also lists 84 states and territories where it established reciprocity from their law or an exchange of notes (the UK, US and Netherlands appear again, and the British Virgin Islands are listed), incl. Australia, Canada, Switzerland, Norway, New Zealand, China, Korea, Türkiye, UAE, Russia and 26 of the 27 EU states (Estonia not listed). For an unlisted state the determination is pending — ask the Ministry before signing. Inheritance needs only factual reciprocity, presumed until disproved
- **EUR-denominated commercial** market; residential typically RSD or EUR-equivalent
- **2014 floods** = Sava + Bosna (NOT Drava — common confusion)
- **Capital gains 10-year exemption** — CRITICAL planning point
- **Belgrade Waterfront** controversial mega-project; ongoing
- **Belgrade records elevated winter PM2.5** — verify current ranking with IQAir / EEA
- **NBS key rate 5.75%** since 12 Sep 2024, kept unchanged on 8 Oct 2026 *(2026 data, source NBS)*
- **Currency RSD** managed float vs EUR
- **Vojvodina autonomous province** has separate provincial regulations
- **Kosovo property** disputed — separate jurisdictional issues
- **Zakon o posebnim uslovima za evidentiranje i upis prava na nepokretnostima** ("Svoj na svome", Sl. glasnik RS 91/2025 i 80/2026, in force **24 October 2025**, when the Zakon o ozakonjenju objekata stopped applying and its pending cases were discontinued, Art. 27) — one-time legalizacija framework (houses, apartments, commercial, extensions, garages); ~2.7 million applications in total, 2,527,000 in the statutory window and just under 200,000 late (Minister Sofronijević, Tanjug 21 Oct 2026 via RTV; secondary) — applications are not buildings. **MAIN FILING WINDOW IS NOW CLOSED** — it ran **8 December 2025 → 8 February 2026 24.00** (extended past the statutory ~60-day cut-off by government notice of 4 February 2026 after platform overload). The late-filing window (only on proof of an objective impediment, Art. 20(2)) **CLOSED at midnight on 24 October 2026** with no extension, so no new application is possible and legalizacija of an unfiled object can no longer be assumed at purchase. Authority: Agencija za prostorno planiranje i urbanizam RS → potvrda → RGZ priority registration. **Fee (Art. 8)**: the local doprinos za uređivanje građevinskog zemljišta by default; family houses, and apartments whose investor is unknown or unavailable, pay a one-off flat fee by zone instead — €1,000 (Belgrade ekstra zona) down to €100 (municipalities under 50,000 and villages); since the 80/2026 amendment (in force the day after publication, its Art. 7) a family house pays the doprinos for each m² above 400 m²; ancillary and production buildings pay nothing up to 500 m² and €10/m² above; owner-occupiers who are persons with disabilities, veterans, families with 3+ children, single parents or social-assistance recipients are exempt. The fee is due within 30 days of the Agency's notice and the potvrda goes to RGZ only after payment — **an unpaid fee blocks registration**; apartment owners may pay in a defaulting investor's place to clear the unpaid-fee note; objects registered under the 2013/2014 law (Sl. glasnik RS 25/13 i 145/14) are treated as registered under this law, with no fee. **Constitutional review pending**: the Ustavni sud confirmed four initiatives against certain provisions (Newsmax Balkans, Oct 2026, repeated by Euronews Srbija 7 Oct 2026; secondary); no decision in the Court's session releases through 13 Oct 2026, no deadline applies, and the law stays in force meanwhile. **Post-24-Oct-2025 illegal construction is NOT eligible** — the building inspector orders works stopped and the object removed (Art. 20(3)–(5)). Buyers of older non-cadastre-conform property inherit any failure to file within the window *(2026-11-03 verified, source paragraf.rs consolidated text Sl. glasnik RS 91/2025 i 80/2026 + paragraf.rs amending law 80/2026 + RGZ 24 Oct 2026 + Tanjug 21 Oct 2026 via RTV + ustavni.sud.rs session releases; earlier CT Legal + Lexology + VMT Attorneys + Tasić & Partners + `https://svojnasvome.gov.rs`)*
- **RGZ digital-only filings** since 4 November 2023 — cadastre applications routed via professional users (attorneys + licensed geodetic organisations). **Partial walk-in since 12 October 2026**: 10 request types can be filed in person at the cadastre counter, with no appointment or intermediary — deletion of a minority or usufruct note, conversion of a right of use into ownership of construction land, change of a registered holder's name/surname/residence (or a legal person's name and seat), correction of holder data or of a technical error, registration of a dispute note, and the two extraordinary remedies (reopening, annulment of a final decision); prescribed administrative fees apply to some. **Every other registration still goes through a professional user** until the rules are amended under an RGZ initiative (no date given) *(2026-10-28 verified, source RGZ notice on rgz.gov.rs + Tanjug 12 Oct 2026 + law-firm.rs)*

## Reddit / forum sources

- **r/serbia**, **r/Belgrade**
- **B92** (Belgrade English news)
- **N1 Serbia**, **Balkan Insight**
- **Forum.krstarica.com**

## Verification authorities

| Authority | When to call |
|---|---|
| **RGZ + eKatastar** | Title verification |
| **Javni beležnik (notar)** — Javnobeležnička komora Srbije `https://www.beleznik.org/` | Mandatory closing (solemnised sale contract, Zakon o prometu nepokretnosti Art. 4) |
| **Lokalna samouprava** | Property tax + permits |
| **Poreska uprava** | Tax compliance |
| **Ministarstvo pravde** | Foreign-buyer reciprocity explanation (objašnjenje) when the buyer's state is not on its list |

## Source URL templates

| Source | URL pattern |
|---|---|
| RGZ | `https://www.rgz.gov.rs/` |
| eKatastar | `https://katastar.rgz.gov.rs/eKatastarPublic/PublicAccess.aspx` |
| NBS price index | `https://www.nbs.rs/en/indeks/index.html` |
| RZS | `https://www.stat.gov.rs/` |
| HaloOglasi | `https://www.halooglasi.com/` |
| Republički seizmološki zavod | `https://www.seismo.gov.rs/` |
| RSZ seismic hazard maps | `https://www.seismo.gov.rs/Seizmicnost/Karte_hazarda.htm` |
| RHMZ | `https://www.hidmet.gov.rs/` |
| Poreska uprava | `https://www.purs.gov.rs/` |
| Putevi Srbije PGDS | `https://www.putevi-srbije.rs/index.php/%D0%B1%D1%80%D0%BE%D1%98%D0%B0%D1%9A%D0%B5-%D1%81%D0%B0%D0%BE%D0%B1%D1%80%D0%B0%D1%9B%D0%B0%D1%98%D0%B0` |
| SEPA air quality | `https://vazduh.sepa.gov.rs/` |
| BVK (Belgrade water) | `https://www.bvk.rs/` |
| Javnobeležnička komora | `https://www.beleznik.org/` |

## Status

✅ Fast-changing sections re-verified as of 2026-11-04; each section's date is in the Per-section verification table.

✅ **Fully populated** as of 2026-04-26. **Last verified**: 2026-10-28 (RGZ counter filing re-verified — 10 request types walk-in since 12 Oct 2026, every other registration still via professional users; Svoj na svome legalizacija window re-verified 2026-10-27 — main filing window closed 8 Feb 2026, late-filing window closed 24 Oct 2026 with no extension; balance of the 2026-05-27 verification unchanged). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (RGZ closed-sale statistics H1 2026 + RGZ index; FRED / BIS and Investropa / Global Property Guide secondary), traffic (Putevi Srbije PGDS 2025), tax (porez na imovinu progressive 0.4-2% + 2.5% transfer + 20% VAT (10% first-sale residential) + 15% CGT 10-year exemption), rental (boravišna taksa + license), work (NSZ + Paušalna), risks (Kraljevo 2010 + 2014 Sava+Bosna floods + Belgrade winter PM2.5), mains (Belgrade vodovod + per-municipality).
**Confidence**: HIGH for `--price` benchmarks (RGZ closed-sale apartment prices H1 2026 + RGZ index Q2 2026; KO / city averages, never parcel values), for the `--tax` statutory rates and caps (ZPI, ZPDV and ZPDG consolidated texts, notary tariff, Poreska uprava 2026 PIT brochure, NBS; each local self-government sets its own property-tax rate up to the caps), for the 10-year CGT exemption (ZPDG Art. 72a), for `--work` (ZPD Art. 145, ZPDV Art. 38, RZS August 2026 salaries), for Active fiscal incentives (youth first-home guarantee-scheme law), for the foreign-buyer reciprocity rule (ZOSPO Arts 82a–82v), for the 2014 flood correction (Sava + Bosna, not Drava) and for the BVK 2026 tariff. MEDIUM for `--rental` (Belgrade boravišna taksa, 20% rate and 25% normative costs re-verified; non-resident withholding mechanics, the listing-number duty, "Belgrade tightening" and the long-term tenancy lines not verified), for `--risks` (RSZ magnitudes, 2014 flood figures, SEPA 2025 air-quality category, seismic-code eras, energetski pasoš and notary rules re-sourced; Vlasinsko / Pirot zone naming, the rainfall trend, three build-era rows and the geodetski snimak / list nepokretnosti rows not verified), for `--traffic` (PGDS 2025 values and operator re-verified; verdict bands curated, no published Boulevard Vojvode Stepe count), for the transfer-tax burden-shifting practice (CMS Expert Guide updated 24 Apr 2018 and City Expert agency blog 25 Jul 2025, lower tier) and for the Svoj na svome caveat (91/2025 i 80/2026 citation, Art. 8 fees, windows and application count re-checked; the 4 Feb 2026 extension notice, "RGZ priority registration" and the 80/2026 implementing bylaws not re-verified). LOW for the `--mains` connection / septic / well ranges and for the energetski pasoš and works rows in Cost benchmarks (est., no published tariff).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | Admin levels, NBS middle rate (14 Oct 2026), managed float and EU dates re-checked; languages list not re-checked; eKatastar URL kept (could not be read for verification, still linked from RGZ) |
| `--price` | 2026-11-04 | 2026-11-04 maintenance run | Seven city and KO rows match Tables 1 and 2 of the RGZ H1 2026 PDF; national +5.25% and Belgrade region +5.65% match the RGZ release, with no Q3 index published by 27 Oct 2026. Sasomange stays deprecated. |
| `--tax` | 2026-11-04 | 2026-11-04 maintenance run | ZPI, ZPDV and ZPDG consolidated texts, cadastre registration law, notary tariff, administrative fee tariff, Poreska uprava PIT brochure (Apr 2026) and NBS press release (8 Oct 2026) re-read; all rates, caps and fees unchanged. Transfer-tax shifting relabelled lower tier (CMS 2018, City Expert 2025) and the PwC attribution dropped; first-apartment exclusion of foreigners now tied to citizenship; buyer cost ranges recomputed |
| `--work=<profession>` | 2026-11-04 | 2026-11-04 maintenance run | RZS release of 26.10.2026: 161,953 / 117,282, median 93,325 and Beogradski region 198,684 / 143,965; euro values computed at 117.3892. Minimum wage from the Socijalno-ekonomski savet page. |
| Active fiscal incentives | 2026-10-23 | 2026-10-23 refresh wave | Youth first-home guarantee-scheme law, MRE / World Bank energy subsidy and Expo 2027 dates replace three stale bullets |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Sasomange deprecated, KupujemProdajem added, BeoBuild relabelled a news site; HaloOglasi "DOMINANT" remains wisdom, not data |
| Reddit / forum sources | 2026-10-23 | 2026-10-23 refresh wave | Subreddits and news sites live; no change |
| `--rental` | 2026-11-04 | 2026-11-04 maintenance run | Tourist tax confirmed: RSD 240 from 15 Oct 2026 (Sl. glasnik 90/2026). The final Belgrade decision's gazette number was not found, so the tag keeps the draft plus Paragraf. |
| `--risks` | 2026-11-04 | 2026-11-04 maintenance run | SEPA's 2025 report supersedes both air-quality lines; the drop from category III to II comes from a new two-category law, not a reported improvement. |
| `--mains` | 2026-11-04 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (RS 2026) | 2026-11-04 | 2026-11-04 maintenance run | Transfer tax re-read at ZPI Art. 30; notary and buyer-total rows recomputed from the tariff at RSD 117.37/EUR, the total now stating that it assumes a resale with the tax on the buyer; energetski pasoš and works rows remain est. |

## Extension TODOs

- [ ] Per-municipality property tax rates table
- [ ] Foreign-buyer reciprocity country list (verified)
- [ ] Belgrade Waterfront premium zone
- [ ] CGT 10-year holding clock optimization
- [ ] Energetski pasoš class verification flow
- [ ] Vojvodina autonomous province specific rules
- [ ] Belgrade winter PM2.5 mitigation
- [ ] EU pre-accession funding eligibility
- [ ] CHF/EUR mortgage scandal (post-2015 reforms)
- [ ] Kraljevo 2010 + 2014 flood-affected zones

## Update history

- **2026-04-26** — Initial population (researched 2026-04)
- **2026-05-27** — Tier-1 corrections: transfer-tax liability, first-apartment exemption, VAT refund, PIT framework and CGT exemptions; Svoj na svome and RGZ digital-only filing caveats added
- **2026-08-07** — Svoj na svome filing windows re-verified
- **2026-10-21** — Tax tracker entry re-checked (December regwatch wave, run early): annual PIT 6× band RSD 10,878,192 for 2025 income
- **2026-10-23** — Refresh wave across market, tax-legal and risk-infra sections (counts are changed / confirmed / unverifiable):
  - **Re-verified** (see Per-section verification): Country profile 3 / 5 / 1 — admin levels restated (5 statistical regions, 29 upravni okruzi, 174 local self-government units), NBS middle rate 117.3892 RSD/EUR (14 Oct 2026), EU negotiations opened 21 Jan 2014; `--price` 15 / 4 / 2 — benchmark table rebuilt from RGZ closed-sale apartment prices H1 2026 with the RGZ index, "NBS price index" label corrected; `--tax` 10 / 28 / 0 — property-tax cap for RSD 25–50M 0.8% → 1.0% with marginal bands, payment dates, transfer-tax liability (ZPI Arts 25, 42), non-taxable amount RSD 34,221 (2026) / 37,369 (2027), primary-residence CGT exemption removed (not in the law), notary ≈0.2–0.45% and RGZ ≈ €63 recomputed (resale ~3% before agency and attorney fees), NBS key rate dated from 12 Sep 2024; `--work` 4 / 5 / 0 — DOO and PDV thresholds cited, RZS August 2026 salaries, minimum wage RSD 371/h net (2026) and RSD 405/h (2027); Active fiscal incentives 3 / 0 / 0 — youth first-home guarantee-scheme law (Government, not NBS), MRE / World Bank energy subsidy and Expo 2027 dates replace three stale bullets, "Vučić government" label removed; Common listing platforms 3 / 3 / 1 — Sasomange deprecated, KupujemProdajem added, BeoBuild relabelled a news site; Reddit / forum sources 0 / 6 / 0
  - **Refreshed, not fully re-verified**: `--rental` 3 / 3 / 4 — Belgrade boravišna taksa RSD 240 from 15 Oct 2026 (the ~159 figure was wrong), 20% rate and 25% normative costs confirmed, non-resident withholding mechanics not verified; Cost benchmarks 2 / 1 / 5 — notary and buyer total recomputed, energetski pasoš and works rows labelled est.; Caveats unique to RS 7 / 20 / 3 — EU dates, reciprocity rule (ZOSPO Arts 82a–82v), NBS rate date, Svoj na svome citation (91/2025 i 80/2026), Art. 8 fee rule and application count; `--traffic` 3 / 3 / 2 — operator Putevi Srbije d.o.o., PGDS 2025 examples for the 🔴 band, državni putevi; `--risks` 13 / 5 / 7 — RSZ name and products, homogenised Mw for the four historic quakes, Kraljevo 2010 damage, 2014 flood rivers and figures, Savski Nasip claim replaced, SEPA 2024 air-quality category III and PM sources, seismic-code era rows, energetski pasoš rule, notary citation; `--mains` 4 / 1 / 4 — BVK 2026 tariff added, Danube-source claim dropped, cost ranges labelled est.; Verification authorities 2 / 2 / 1 — Javni beležnik (notar) row and Ministarstvo pravde role corrected (an explanation on request, not an approval); Source URL templates 1 / 6 / 2 — RSZ renamed, hazard-map, Putevi Srbije PGDS, SEPA and BVK rows added
  - Totals 73 changed / 92 confirmed / 32 unverifiable. Status footer date unchanged: `--rental`, `--risks` and `--mains` are not fully re-verified
- **2026-10-27** — Svoj na svome late-filing window re-verified (closed 24 Oct 2026, no extension)
- **2026-10-28** — RGZ counter filing re-verified (10 walk-in request types since 12 Oct 2026)
- **2026-11-04** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (RS 2026). Playbook-level date now 2026-11-04.
