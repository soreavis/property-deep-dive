# Iceland 🇮🇸 — Property Due-Diligence Playbook

ISO2: `is`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 3 digits (`101` Reykjavík central, `200` Kópavogur, `600` Akureyri, `400` Ísafjörður)
- **Admin levels**: 8 regions (landshlutar) + 62 sveitarfélög (municipalities; municipal structure at 1 Jan 2026) (2026 data, source Hagstofa MAN03250 + MAN02005)
- **Currency**: **ISK** (Icelandic króna); 1 EUR ≈ 136 ISK (Central Bank official rate EUR 136.20, read 2026-10-23; volatile — re-check at `https://www.cb.is/`) (2026 data, source cb.is)
- **Languages**: Icelandic (official); English widely understood
- **Cadastre**: **HMS (Húsnæðis- og mannvirkjastofnun)** + **Þjóðskrá Íslands** (national registry)
- **Identifier**: **fasteignanúmer** (property number) + **landnúmer** (land number)
- **Ownership types**:
  - **Eignaríbúð** (freehold apartment)
  - **Einbýlishús** (single-family house)
  - **Parhús** (semi-detached)
  - **Raðhús** (terraced/townhouse)
  - **Fjölbýlishús** (apartment building, with húsfélag = building association)
- **Volcanic + seismic country** — ALL property analysis must factor in active geological hazards
- **Iceland is NOT in EU** — but EEA member; some property buying restrictions apply

## Section: `--price`

### Primary sources

- **HMS Fasteignaskrá** (cadastre + valuation): `https://www.hms.is/`
  - Public look-up of every property in the fasteignaskrá at `https://hms.is/fasteignaskra` (fasteignamat, brunabótamat, sizes, building materials); owners see their own properties on island.is Mínar síður (2026 data, source island.is/fasteignamat + hms.is Fasteignaskrá, archived 2026-01-19)
- **Þjóðskrá Íslands** (national registry of persons — lögheimili, civil status): `https://skra.is/` — its property division (fasteignaskrá, fasteignamat) moved to HMS on 1 Jul 2022 (source skra.is, notice of 27 Jun 2022)
- **Hagstofa Íslands (Statistics Iceland)** — Vísitala markaðsverðs íbúðarhúsnæðis (table VIS01106): `https://hagstofa.is/`
  - Monthly market-price index of residential housing, split capital-region flats / capital-region detached / outside capital region / whole country (latest month 2026M09 at 2026-10-23)
- **Seðlabanki Íslands (Central Bank)** — financial stability reports: `https://www.cb.is/`
- **HMS** publishes housing-market news (with a Mánaðarskýrsla — monthly report — news category), price and rent indices and Fasteignaskrá / Leiguskrá dashboards under Gögn og mælaborð, plus the daily-updated **Kaupskrá fasteigna** (registered (þinglýstir) purchase contracts: price, contract date, fasteignamat, floor area; open-data CSV under Gögn og mælaborð › Grunngögn til niðurhals) (source hms.is Gögn og mælaborð, Fréttir and Kaupskrá fasteigna, archived 2026-01-23, 2026-07-10 and 2026-07-13)

### Listing platforms

- **Mbl.is fasteignir**: `https://www.mbl.is/fasteignir/` (live, archived 2026-11-02)
- **Fasteignir.is** (Vísir / Sýn): `https://fasteignir.visir.is/` (fasteignir.is redirects here)
- **Húsaleiga.is** (rental brokerage / leigumiðlun) and **Bland.is** (classifieds, Fasteignir › Til leigu) for rentals (2026 data, source husaleiga.is; bland.is archived 2026-10-12)
- **RE/MAX**, **Eignamiðlun**, **Fasteignamarkaðurinn**, **Domus** (Blönduós), **Gimli** — estate agencies (fasteignasölur), all with agents on Félag fasteignasala's member list (2026 data, source ff.is Félagsmenn ⚠️ trade association)
- ~~**fasteign.is**~~ ❌ DEPRECATED — dead on 2026-11-03 (page not found; not linked from HMS's Fasteignaskrá or Gögn og mælaborð pages); verify with HMS Fasteignaskrá `https://hms.is/fasteignaskra` (property data) and Fasteignir.is / Mbl.is (listings)

### Price benchmarks — HMS kaupskrá, contracts signed Oct 2025–Sep 2026 (computed)

| Region | ISK/m² flats (fjölbýli), P25–P75 | Total price, detached houses (einbýli), P25–P75 |
|---|---:|---:|
| **Reykjavík 101 (city centre)** | 849,000–1,061,000 (median 948,000; n = 369) | 125,000,000–208,800,000 (median 152,500,000; n = 16, small sample) |
| **Reykjavík 105/107 (Hlíðar/Vesturbær)** | 796,000–975,000 (median 880,000; n = 668) | too few contracts (n = 2) |
| **Greater Reykjavík (Kópavogur, Hafnarfjörður, Garðabær)** | 738,000–904,000 (median 811,000; n = 1,823) | 132,100,000–184,000,000 (median 155,500,000; n = 180) |
| **Akureyri** | 581,000–786,000 (median 679,000; n = 379) | 74,000,000–119,800,000 (median 105,000,000; n = 51) |
| **Reykjanesbær** | 549,000–717,000 (median 646,000; n = 380) | 81,500,000–109,000,000 (median 94,500,000; n = 48) |
| **Selfoss / Árborg** | 597,000–710,000 (median 664,000; n = 145) | 73,000,000–102,500,000 (median 86,000,000; n = 60) |
| **Westfjords / East fjords** | 327,000–535,000 (median 413,000; n = 146) | 29,500,000–70,500,000 (median 48,500,000; n = 125) |
| **Whole country** | 673,000–887,000 (median 779,000; n = 6,219) | 64,000,000–140,000,000 (median 94,000,000; n = 967) |
| **Sumarbústaðir** (cottages, sumarhús) | — | 22,500,000–53,000,000 (median 33,000,000; n = 304) |

> Computed from HMS Kaupskrá fasteigna (HMS's record of registered (þinglýstir) purchase contracts; open-data CSV, file current to contracts signed 30 Oct 2026): contracts signed 1 Oct 2025–30 Sep 2026, excluding unfinished properties (fullbuid = 0) and contracts HMS marks unusable for comparison (onothaefur_samningur = 1: related parties, several properties in one contract, sales by or to a financial institution, payment in property or movables, partial sales, etc.); ISK/m² = kaupverð (published in thousand ISK) × 1,000 ÷ einflm (einingarflatarmál), flats of 20 m² or more; ranges are the interquartile range (P25–P75), rounded; Westfjords / East fjords = all Vestfirðir and Austurland municipalities (sveitarfélag numbers 4xxx / 7xxx). Postcode / municipality aggregates of contract prices — never a valuation of a specific parcel (2026 data, source HMS Kaupskrá fasteigna; computed).

> Price-index cross-check over the same 12 months: Hagstofa Vísitala markaðsverðs íbúðarhúsnæðis, Sep 2025 → Sep 2026: whole country 803.4 → 820.6 (+2.1%), capital-region flats 787.8 → 795.7 (+1.0%), capital-region detached 873.0 → 896.1 (+2.6%), outside capital region 799.6 → 833.9 (+4.3%), against 5.9% CPI inflation over the same 12 months — a real-terms decline (2026 data, source Hagstofa VIS01106 + VIS01000; % changes computed).

### Compute

1. ISK/m² = price / **Brúttóflatarmál** (gross floor area, BBR equivalent)
2. **Fasteignamat** vs price: in usable residential contracts (flats, detached and other houses) signed Jan–Sep 2026, fasteignamat (2026 valuation) was a median **96%** of the contract price (interquartile 89–101%); 1,685 of the 5,744 contracts (29%) sold for less than fasteignamat. In 2025 contracts the median was 89% (83–95%, n = 9,618) (2026 data, source HMS Kaupskrá fasteigna; computed per contract as fasteignamat ÷ kaupverð, unfinished and HMS-flagged unusable contracts excluded). Each year's fasteignamat reflects the price level of February of the preceding year (island.is example: fasteignamat 2024 → February 2023 prices) (source island.is/fasteignamat)
3. **Krónaverðbólga** factor — CPI inflation peaked at 10.2% y/y (Feb 2023), eased to 4.1% (Sep 2025) and was 5.9% in Sep 2026 (2026 data, source Hagstofa VIS01000); deflate longitudinal ISK prices by CPI before comparing
4. Compare ISK price to EUR using current FX (ISK volatile)

### Key terms

- Eignarheimild = title deed
- Fasteignamat = official property valuation (annual, used for tax)
- Söluverð = sale price
- Fermetraverð = price per m²
- Húsfélag = building association (apt buildings)
- Heitt vatn = hot water (geothermal)

---

## Section: `--traffic`

### Sources

- **Vegagerðin** (Iceland Road Administration): `https://www.vegagerdin.is/`
- **Umferðarkort** (Vegagerðin traffic-count map): `https://umferd.vegagerdin.is/`
- **Umferðartölur**: annual ÁDU/SDU/VDU averages for national roads since 2000, daily counter data since 2019, key-counter tables (Hringvegur, capital area): `https://www.vegagerdin.is/samgongukerfid/vegakerfid/umferdartolur`
- Ring Road (Hringvegur, Route 1) and main routes traffic data

### Key term

**ÁDU (Ársdagsumferð)** = AADT-equivalent ("meðalumferð á dag yfir árið"); **SDU** = summer average (Jun–Sep), **VDU** = winter average (Jan–Mar + Dec) (2026 data, source Vegagerðin umferðartölur).

### Verdict bands

- 🟢 < 1,000 v/d (rural Westfjords / interior; Ring Road on Mývatnsöræfi 785, Möðrudalsöræfi 675)
- 🟡 1,000–8,000 v/d (regional routes; Ring Road in north/east: Holtavörðuheiði 1,735, Öxnadalur 1,695, Kræklingahlíð by Akureyri 4,605; Ring Road west of Hvolsvöllur 4,880)
- 🟠 8,000–25,000 v/d (Reykjavík periphery: Ring Road on Hellisheiði 11,045, at Geitháls 14,470; Hvalfjörður tunnel 9,070)
- 🔴 > 25,000 v/d (Reykjavík main arteries: Reykjanesbraut at Dalvegur 70,300, Vesturlandsvegur above Ártúnsbrekka 64,700, Hafnarfjarðarvegur 47,300, Ring Road at Úlfarsfell 36,175; Miklabraut)

> Calibration figures are 2025 ÁDU (Vegagerðin "ÁDU nálgað", approximated) from the Hringvegur and capital-area key-counter tables (2025 data, source Vegagerðin umferðartölur). The bands are a curated heuristic, not an official classification.

---

## Section: `--tax`

### Annual property tax — Fasteignagjöld

- Set per sveitarfélag
- Based on **fasteignamat** (annual official valuation by HMS)
- Statutory bands (Lög nr. 4/1995 um tekjustofna sveitarfélaga): **A** (residential incl. land rights, sumarbústaðir, farm buildings) up to **0.5%** of fasteignamat, raisable to **0.625%**; **B** (public buildings — schools, hospitals, sports halls, libraries) **1.32%**; **C** (commercial, tourism buildings and all other property) up to **1.32%**, raisable to **1.65%** (2026 data, source samband.is Tekjustofnar + reykjavik.is Fasteignagjöld)
- 2026 A-rates across the 53 municipalities with a rate in Samband's Tafla 14 (covers municipalities with >300 residents): **0.149%** (Garðabær) to **0.625%** (Strandabyggð, Vopnafjarðarhreppur), median 0.40% (computed); capital area 0.149–0.199% (Garðabær 0.149, Kópavogur 0.151, Seltjarnarnes 0.166, Reykjavík 0.18, Mosfellsbær 0.19, Hafnarfjörður 0.199); Reykjanesbær 0.23, Akureyri 0.28, Árborg 0.44, Ísafjarðarbær 0.48; C-rates 1.154–1.65% (2026 data, source samband.is Tafla 14 Fasteignagjöld 2026) — municipality-level rates; a given property's bill follows its own fasteignamat and registered use
- Reykjavík 2026: A **0.18%**, B **1.32%**, C **1.60%** of fasteignamat (house + lot); **lóðarleiga** on leased lots 0.20% of lot valuation (residential) / 1.00% (commercial) (2026 data, source reykjavik.is Fasteignagjöld)
- Reduction or waiver for low-income old-age and disability pensioners at the municipality's discretion (e.g. Reykjavík) (2026 data, source reykjavik.is Fasteignagjöld)
- **Sorphirðugjald** (waste collection) added separately
- **Vatnsgjald + Holræsagjald** (fráveitugjald) (water + sewer) per sveitarfélag — in Reykjavík billed by Veitur since 2010, not on the fasteignagjöld bill (2026 data, source reykjavik.is Fasteignagjöld)

### Transaction taxes

- **Stimpilgjald** (stamp duty) under **Lög um stimpilgjald nr. 138/2013**, charged on the **fasteignamat** registered in fasteignaskrá when the deed is issued (construction stage at handover), not on the price (2026 data, source island.is Þinglýsing skjala, Sýslumenn):
  - **0.4%** — individual, first purchase of residential property (half rate; yfirlýsing um fyrstu kaup filed with the deed)
  - **0.8%** — individual, standard
  - **1.6%** — legal entity (company / business)
  - Deed not registered within 2 months of signing → stimpilsekt of up to 10% of the duty on top
- **Þinglýsingargjald** (registration fee under Lög nr. 88/1991 um aukatekjur ríkissjóðs; registration itself under **Lög nr. 39/1978** Þinglýsingalög): **ISK 3,800 per document** (2026 data, source island.is Þinglýsing skjala)
- **Fasteignasalalaun** (broker commission, paid by seller): **1.4–2.5%** of the sale price + 24% VSK for residential sales across five published agency price lists — the rate depends on exclusive (einkasala) vs general (almenn sala) listing and on who shows the property; Landmark's Westfjords rate is 2.25–2.75%; minimum fees from ISK 483,600 incl. VSK where stated. On top: a seller's document / listing fee (gagnaöflunargjald) of ISK 54,900–79,900 incl. VSK, and a buyer's handling fee (umsýslugjald / þjónustugjald kaupanda) of ISK 69,900–79,900 incl. VSK (2026 data, agency price lists ⚠️ RE/MAX, Gimli, Hraunhamar, Landmark, Heimili — indicative and negotiable; not a regulator figure or index)

### Total transaction cost (buyer side)

- **First-time buyer**: 0.4% × fasteignamat + ISK 3,800 per registered document (computed from the rates above)
- **Standard buyer**: 0.8% × fasteignamat + ISK 3,800 per registered document (computed); legal entity 1.6% × fasteignamat
- Agency buyer fee (umsýslugjald / þjónustugjald kaupanda), charged by all five agencies whose price lists are cited: ISK 69,900–79,900 incl. VSK (2026 data, agency price lists ⚠️ — see Transaction taxes); lender fees and any buyer-side adviser fees come on top (not included)
- Seller: broker commission 1.4–2.5% + 24% VSK, plus a document / listing fee of ISK 54,900–79,900 incl. VSK (2026 data, agency price lists ⚠️ — see Transaction taxes)

### Capital gains — Fjármagnstekjuskattur

- **22% flat** for individuals (22% since 1 January 2018; raised from 20% in effect 2011–2017) (2026 data, source skatturinn.is Helstu tölur 2026 + Fjármagnstekjuskattur)
- Statute: **Lög um tekjuskatt nr. 90/2003**
- **Residential property (íbúðarhúsnæði) sale exempt** if owned a full **2 years** and the seller's total residential holdings on the sale date are ≤**600 m³** (individual) / **1,200 m³** (couple); a home in the owners' own use is exempt regardless of volume (sales from 1 Jan 2016). Owned <2 years → gain fully taxable, with deferral over two year-ends or rollover into a replacement home's cost base (2026 data, source skatturinn.is Söluhagnaður)
- **Sumarbústaður / frístundahúsnæði** (cottage): gain tax-free (from income year 2020) only if owned ≥**7 years**, used by the owners and not let for payment, and cottage + residential holdings ≤600 m³ (individual) / 1,200 m³ (couple); otherwise taxable (2026 data, source skatturinn.is Söluhagnaður)
- Other property (commercial, land, lots, and residential volume above the limits when not in own use): 22% on the gain

### VAT (VSK) — Lög um virðisaukaskatt nr. 50/1988

- 24% standard
- 11% reduced (food, books, hotel / guest-room lets under one month, tourist services)
- **Sale of immovable property is EXEMPT from VSK** under Lög nr. 50/1988 — including new build (2026 data, source skatturinn.is Helstu tölur 2026 + Value Added Tax page). Builders of residential housing (byggjendur íbúðarhúsnæðis), including VSK-registered builders building for sale or rent, can claim the same 35% refund of VSK paid on on-site labour (form RSK 10.17); a VSK-registered builder is refunded only once the VSK return for the same period is filed, and the refund is set off against that period's VSK (2026 data, source island.is Endurgreiðsla VSK til byggingaraðila) — see below.
- Owner VAT-refund scheme: **35% refund of VSK on on-site labour** for new build, renovation and maintenance of residential housing via **Endurgreiðsla VSK**, claimable for 6 years — rate since 1 July 2023 (100% applied 1 Mar 2020–31 Aug 2022, 60% 1 Sep 2022–30 Jun 2023) (2026 data, source `https://island.is/endurgreidsla-vsk-vegna-ibudarhusnaedis` + skatturinn.is Helstu tölur 2026).

### Future risk

- **Stimpilgjald** stable
- **Fasteignamat** annual revision
- **Currency risk** — ISK volatile
- **Foreign-currency mortgages restricted, not banned**: a consumer mortgage counts as foreign currency-linked when it is denominated in or tied to a currency other than the borrower's income or the assets meant to repay it, or other than that of the EEA state the borrower lives in when borrowing — so an ISK loan to a borrower paid in euros is one. The lender may grant it only to a borrower who (1) has enough income in the loan's currency to pass the affordability assessment, (2) passes an assessment that assumes large exchange-rate moves and interest-rate rises, or (3) passes the assessment and provides financial hedges that substantially reduce the FX risk over the loan term (Lög nr. 118/2016 um fasteignalán til neytenda art. 4 and art. 21; 2025 data, source althingi.is consolidated text of 30 Apr 2025, archived 2025-08-28 — may have changed since). For route (2) the assessment must assume at least a **40%** rise in regular repayments (Reglugerð nr. 270/2017 um fasteignalán til neytenda art. 6; version in force since 12 Apr 2022) (2026 data, source reglugerd.is). The Central Bank may, with Financial Stability Committee approval, set rules on credit institutions' foreign currency-linked lending to borrowers unprotected against FX risk — maturities, collateral, portfolio caps (Foreign Exchange Act No. 70/2021 art. 5; 2021 text, source Ministry of Finance English translation — may have changed since) — whether such rules are in force: verify at `https://www.cb.is/`. Banks offer these loans to buyers with foreign-currency income or living abroad — Íslandsbanki: ISK mortgages for borrowers paid in foreign currency, up to 80% of the purchase price, payment burden tested at +40%; Arion: mortgages for people living abroad or earning foreign-currency income (2026 data, bank product pages, regulated entities)

---

## Section: `--rental`

### Long-term residential

- **Húsaleigulög nr. 36/1994** (Tenancy Act): moderate protection (wisdom, not data)
- **Tímabundinn leigusamningur** (fixed-term) widely used (wisdom, not data); in a fixed-term lease the parties may not agree to a rent change during the first 12 months (L. 72/2025 art. 2, amending art. 37(3); leases made, renewed or extended from 1 Jan 2026)
- **Leiguskrá registration**: from 1 Jan 2026 the landlord must register every residential lease in HMS's leiguskrá within 30 days of signing (L. 72/2025 art. 1, amending art. 5), leases in force on that date included (art. 3); HMS may fine landlords who do not let housing as a business for failing to register from 1 Jan 2027; from income year 2026 the 22% capital-income treatment of rent requires a registered lease (art. 4, amending art. 58 a of tekjuskattslög nr. 90/2003) (2026 data, source Stjórnartíðindi A 72/2025 + hms.is news "Ný húsaleigulög", archived 2026-02-11)
- **Ótímabundinn leigusamningur** (open-ended) — termination notice 6 months for both landlord and tenant for flats (íbúðir); 12 months from the landlord where the landlord is a legal entity letting the flat commercially (í atvinnuskyni) and the tenant has rented it for more than 12 months; 3 months for single rooms; a non-profit landlord may give 3 months in the cases set out in art. 56(2) húsaleigulög (2026 data, source stjornarradid.is húsaleigumál — Uppsögn og riftun + Undanþágur fyrir lögaðila sem ekki eru reknir í hagnaðarskyni)
- Income tax on rental (individuals): letting of residential housing that falls under húsaleigulög, with no more than two flats let, is capital income (fjármagnstekjur) taxed at **22%** on **75%** of gross rent — the frítekjumark (tax-free share) fell from 50% to **25%** from income year 2026 — i.e. **16.5%** of gross rent (computed: 22% × 75%); no cost deductions except heating/electricity included in the registered lease, and island.is requires the lease to be registered in the national rental registry. Letting outside the exceptions is taxed as business income (atvinnurekstrartekjur) (2026 data, source skatturinn.is Leigutekjur + island.is/leigutekjur-af-husnaedi)
- **Leiga á móti leigu**: an owner who lets their own former home (under húsaleigulög) while renting another home for own use may deduct the rent paid from the rental income (rule in force since 1 Jan 2018) (2026 data, source skatturinn.is Leigutekjur)
- **Wealth tax**: none listed by Skatturinn — declared assets and debts affect vaxtabætur, and gains on asset sales are taxable; the only wealth tax it mentions, the auðlegðarskattur, applied to assessment years 2010–2014 (temporary provision in the income-tax act); property is declared in the tax return at its fasteignamat value (2026 data, source skatturinn.is Eignir og skuldir)

### Short-let (Airbnb / Heimagisting)

**Heimagisting (home accommodation registration) required nationally** under **Lög um veitingastaði, gististaði og skemmtanahald nr. 85/2007** (Heimagisting amendment L. 67/2016, in force 1 Jan 2017; scope narrowed by L. 25/2026, published 8 Apr 2026, binding from 9 Apr 2026) (2026 data, source Stjórnartíðindi A 67/2016 + A 25/2026 + island.is/heimagisting):
- **National cap (NOT Reykjavík-specific)**: max **90 nights/year** AND **ISK 2,000,000 gross income/year** — whichever triggers first requires commercial licence (rekstrarleyfi) — inside þéttbýli (urban areas) open-ended (ótímabundin) licensed accommodation must be in approved commercial premises (rule inserted by L. 43/2024, in force 23 May 2024; limited to ótímabundin licences by L. 25/2026 art. 1a), while a rekstrarleyfi for accommodation in urban residential housing (íbúðarhúsnæði) is time-limited to five years at a time (L. 25/2026 art. 2); such licences valid on 1 Apr 2026 run to 1 Jan 2032 (L. 25/2026 art. 5 transitional provision) · **Scope narrowed by L. 25/2026 (in force 9 Apr 2026)**: heimagisting only at the owner's lögheimili (legal domicile) OR one other owned property OUTSIDE urban areas — a second urban flat can no longer be let under heimagisting; L. 82/2026 ch. IX (in force 1 Jan 2027) only replaces Act 85/2007's heilbrigðisnefnd references with Umhverfis- og orkustofnun and Stofnun atvinnuveganna, with no change to the heimagisting caps or scope (2026 data, source Stjórnartíðindi A 43/2024, A 25/2026 and A 82/2026 + island.is/heimagisting)
- Beyond cap: requires **rekstrarleyfi** (operator licence); accommodation (gistiþjónusta) is VSK-able at the reduced **11%** rate (standard 24%) once VSK registration is required (taxable sales above ISK 2,000,000 in 12 months), and accommodation with a class II–IV rekstrarleyfi charges **gistináttaskattur ISK 800** per unit per night; registered heimagisting within the 90-night / ISK 2,000,000 limits owes no gistináttaskattur (2026 data, source skatturinn.is Skattskylda og skattprósentur + Gistináttaskattur)
- Registration via **Sýslumaður** (district commissioner; island.is lists Sýslumaðurinn á höfuðborgarsvæðinu as the service provider); registration is valid to the end of the calendar year and must be renewed annually; registration fee **ISK 9,200** (2026 data, source island.is/heimagisting)
- Administrative fines (stjórnvaldssektir) up to **ISK 1,000,000** per violation for letting without registration or breaching the marketing rules; other sanctions include deregistration and refusal of registration the following year (2026 data, source island.is/heimagisting)
- **EU 2024/1028 STR**: not directly applicable in Iceland (not EU). EEA-Lex marks it EEA-relevant and under scrutiny by Iceland, Liechtenstein and Norway, with no EEA Joint Committee decision listed (2026 data, source `https://www.efta.int/eea-lex/32024R1028`).

### Tax on short-let

- Heimagisting income: capital income (fjármagnstekjur) taxed at 22% with no cost deductions, provided the letting is registered with Sýslumaður (skráningarnúmer) and total heimagisting rent is at most ISK 2,000,000 in the income year; above that, or if Sýslumaður cancels the registration, all the year's rent is taxed as business income (2026 data, source skatturinn.is Leigutekjur + island.is/heimagisting/skattar-og-gjold)
- License-required short-let: business income (atvinnurekstrartekjur); VSK 11% on the accommodation once VSK-registered, plus gistináttaskattur under a class II–IV licence (see above) (2026 data, source skatturinn.is)

---

## Section: `--work=<profession>`

### Sources

- **Vinnumálastofnun** (Directorate of Labour): `https://island.is/s/vinnumalastofnun` (vmst.is redirects here)
- **Alfred** job platform: `https://www.alfred.is/`
- **LinkedIn IS**, **Tvinna.is** (creative-sector jobs), **Mbl Atvinna** (`https://www.mbl.is/atvinna/`, live job board, archived 2026-11-02)

### Self-employment

- **Einstaklingsrekstur** (sole proprietorship, run on the owner's kennitala; owner liable with all personal assets): no minimum capital
- **EHF.** (private limited): min share capital ISK 500,000
- **HF.** (public limited): min share capital ISK 4,000,000 (2026 data, source skatturinn.is Fyrirtækjaskrá + Stofna rekstur)
- **VSK registration** required once taxable sales exceed ISK 2,000,000 in a 12-month period (voluntary below; sellers of exempt goods/services only need not register) (2026 data, source skatturinn.is Skráning á VSK-skrá)
- **Skatturinn** (ríkisskattstjóri) registration for tax: `https://www.skatturinn.is/`

### Salary benchmarks (2025)

- Full-time employees, whole country — regluleg heildarlaun (regular pay + measured overtime): median **ISK 895,000/mo**, mean ISK 982,000, interquartile range ISK 728,000–1,110,000; heildarlaun (incl. irregular payments) median ISK 948,000 (2025 data, source Hagstofa VIN02004)
- Regional split (est. — VIN02004 publishes no regional breakdown; each range = the national interquartile range above × the area's 2025 median atvinnutekjur ÷ the national median, from Hagstofa TEK01002: whole country ISK 8,582,000/yr, Reykjavík 8,648,000, Akureyri 8,329,000, the 19 municipalities outside the capital region other than Akureyri with 1,000+ earners 7,231,000 (Rangárþing eystra) to 9,679,000 (Fjarðabyggð), median ratio 0.93. Atvinnutekjur cover every earner, part-time included, so the ratio is a proxy for pay differences, not a measured regional wage) (2025 data, source Hagstofa VIN02004 + TEK01002; computed):
  - Reykjavík: ~ISK 735,000–1,120,000
  - Akureyri: ~ISK 705,000–1,075,000
  - Smaller towns: ~ISK 680,000–1,035,000 at the median town; ratios run from 0.84 (Rangárþing eystra) to 1.13 (Fjarðabyggð)
- **Lágmarkslaun** (set by collective agreement, varies by union): lowest SGS–SA general-labour tariff (launaflokkur 4, starting step) **ISK 476,379/mo** for 1 Apr–31 Dec 2026, rising to ISK 500,129 from 1 Jan 2027 (2026 data, source sgs.is Launatöflur SGS og SA 2024-2028)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Veðurstofan Íslands (IMO)** | `https://www.vedur.is/` | Meteorology, hydrology, **seismology, volcanology** |
| **Náttúruhamfaratrygging Íslands (NTÍ)** — named Viðlagatrygging Íslands until 1 Jul 2018 | `https://island.is/s/nti` (nti.is redirects here) | National natural disaster insurance |
| **HMS** (Húsnæðis-, mannvirkja- og skipulagsstofnun) | `https://www.hms.is/` | Housing + building standards, fasteignamat, brunabótamat |
| **Almannavarnir** (Civil Protection) | `https://www.almannavarnir.is/` | Emergency response |
| **ÍSOR (Iceland GeoSurvey)** | `https://isor.is/en` | Geology, geothermal |
| **Veitur** | `https://www.veitur.is/` | Capital-area utility (hot water, cold water, sewer, electricity distribution; also parts of West + South Iceland) |

### Specific risks (volcanic, seismic, glacial-flood, landslide and avalanche hazards)

#### Volcanic + seismic — current activity

**Reykjanes peninsula 2023-2025 eruption series** (CRITICAL UPDATE):

- **9 eruptions since December 2023** on the Sundhnúkur crater row; no new eruption through 27 Oct 2026 (2026 data, source Veðurstofan news 5 Aug 2025 "The ninth eruption on the Sundhnúkur crater row has ended" + Reykjanes situation update 27 Oct 2026)
- **12 eruptions on the Reykjanes peninsula since 2021** = 3 in the Fagradalsfjall area 2021–2023 (Fagradalsfjall / Litli-Hrútur) + 9 on the Sundhnúkur crater row (computed from Veðurstofan's Reykjanes overview and its 5 Aug 2025 news; Visit Reykjanes, secondary, also counts the July 2025 eruption as "the twelfth" since 2021)
- **Most recent**: began 16 July 2025; crater activity stopped 4 August and Veðurstofan declared it over on 5 August 2025 (2025 data, source Veðurstofan)
- **Still active (Oct 2026)**: ground uplift under Svartsengi continues at a relatively steady rate; latest published magma volume ≈ 29.1 million m³ accumulated 17 Jul 2025 – 16 Aug 2026 (range 28.3–29.9); a magma intrusion, possibly an eruption, on the Sundhnúkur crater row "remains the most likely scenario" and its timing cannot be predicted; Reykjanes–Svartsengi system at alert level 2 (orange); Grindavík in the "considerable" and Svartsengi in the "moderate" hazard category (Grindavík's overall hazard score lowered from 4.14 to 4.02 on 30 Sep 2026 after fracture repairs; hazard map valid until 5 Jan 2027 unless conditions change); past warning times ≈ 20 minutes to just over 4 hours (2026 data, source Veðurstofan Svartsengi updates 18 Aug, 30 Sep + 27 Oct 2026)
- **Grindavík evacuated 10 November 2023** (registered population 3,562 on 1 Jan 2023); registered population 819 on 1 Jan 2026 (registered domicile, not physical presence); in an Oct 2026 survey of pre-evacuation adult residents 15.3% lived in the town vs ~10% at the start of 2026; the town remains at civil-protection óvissustig (2026 data, sources Hagstofa MAN02005 + grindavik.is 16 Oct 2026)
- **Barriers do not stop dykes**: magma dykes formed under Grindavík itself on 10 Nov 2023 and again in January 2024, the second under the central part of the town, opening fractures and moving faults in town; Veðurstofan's scenarios include lava from a vent north of the protective barriers flowing into existing fissures and re-emerging inside the town limits, or a fissure opening within Grindavík; listed hazards also include ground collapse into fractures, earthquakes of about M 5 and above, gas and a higher sea-flood risk from land subsidence in Grindavík (2024 data, sources Veðurstofan Reykjanes overview 26 Feb 2024 + Veðurstofan Grindavík unrest news page, Aug 2024 updates — rates/figures may have changed since)
- **Long eruptive period** — eruptive periods on the Reykjanes peninsula recur every ≈ 800–1,000 years on average; the last one (Reykjaneseldar) lasted from ≈ 950 to 1240 (≈ 290 years, computed 1240 − 950); the current unrest began in December 2019, and Veðurstofan states that eruptive episodes here "can last for decades or centuries" with intervals between events — a long pause does not mean the episode has ended (sources Veðurstofan Reykjanes overview 26 Feb 2024 + Reykjanes situation updates 30 Sep + 27 Oct 2026)
- **Property risk in Reykjanes**:
  - **Grindavík properties**: state buyback via **Fasteignafélagið Þórkatla** under Act 16/2024 — 961 properties purchased, 969 applications since March 2024; Þórkatla's re-sale (endurkaup) plan awaits law changes; a new risk assessment for people's safety in Grindavík is on the municipality's website (2026 data, sources torkatla.is + grindavik.is 16 Oct 2026 + Veðurstofan news 1 Oct 2026)
  - **Reykjanesbær (Keflavík area)**: exposed through shared infrastructure and gas — when the Njarðvík pipeline carrying hot water from Svartsengi was cut in Feb 2024 the Suðurnes area was left without hot water; three exploration wells drilled since could keep Reykjanesbær, Vogar and Suðurnesjabær frost-free in the short term if the line is cut again (2024 data, source Stjórnarráðið news 10 Sep 2024 — rates/figures may have changed since); on 21 Nov 2024 lava reached the line, and gas pollution was forecast to affect Grindavík, Svartsengi and Reykjanesbær (2024 data, source Veðurstofan eruption updates 21 Nov 2024)
  - **Capital area (Reykjavík)**: indirect risk via volcanic gas — with south-westerly winds Veðurstofan has forecast gas pollution reaching Vatnsleysa and the capital area (2024 data, source Veðurstofan Grindavík unrest news page, update 5 Sep 2024)
- **Authority monitoring**: `https://www.vedur.is/skjalftar-og-eldgos/` (live)

#### Other volcanic zones

- **Hekla** — 23 eruptions in historical time; roughly decadal since 1970 (1970, 1980–81, 1991, Feb 2000) and none since; Veðurstofan described it as "overdue" in 2016, with ground inflation above its pre-2000-eruption level, and notes that pre-eruption signals have come only tens of minutes ahead (2016 data, sources Veðurstofan "Monitoring of Hekla" 7 Jul 2016 + Hekla page — rates/figures may have changed since)
- **Katla** — major dangerous; subglacial; jökulhlaup risk
- **Bárðarbunga** — Iceland's longest volcanic system and its second most active (≥ 26 eruptions in the last 11 centuries); last eruption the Holuhraun fissure eruption, Aug 2014 – Feb 2015, whose lava was the largest to flow in Iceland since Skaftáreldar (1783–1784) (sources Veðurstofan Bárðarbunga page + Vísindamannaráð almannavarna 3 Dec 2014)
- **Grímsvötn** — Iceland's most active volcano in the Holocene, mostly ice-covered; ≈ 1 eruption per decade over the last 1,100 years, last in 2011; jökulhlaups are common when it erupts, and Grímsvötn is one of Iceland's two commonest jökulhlaup sources (45+ floods in historical time) (sources Veðurstofan Grímsvötn page + "Jökulhlaup" article)
- **Öræfajökull** — historic catastrophe (1362)

#### Seismic

- Iceland sits on **Mid-Atlantic Ridge** — ~2,000–5,500 quakes/month recorded nationwide in 2026 (≈ 65–185/day computed: 2,000 ÷ 31, 5,500 ÷ 30), mostly small; Sep 2026 ≈ 2,500, of which 600+ on Reykjanesskagi (2026 data, source Veðurstofan monthly jarðskjálftayfirlit)
- **Suðurlandsskjálftar** (South Iceland Seismic Zone): in the transform zones in South Iceland and off North Iceland earthquakes are more frequent than in the rift zones and can reach M 7 or more; e.g. the damaging M 6.1 Ölfus earthquake of 29 May 2008 (sources Veðurstofan "Jarðskjálftavirkni á Íslandi" + IMO news 29–30 May 2008)
- **Reykjanesskagi**: active swarm zone (current)
- **Tjörnesbeltið** (north): also active
- Structural design follows the Eurocodes (seismic part EN 1998, Eurocode 8) with Icelandic national annexes, and foundations in earthquake zones must allow for seismic ground motion (2026 data, source byggingarreglugerð 112/2012 arts 8.2.1 + 8.1.4, last amended 1 May 2026, island.is)

#### Other geological hazards

- **Hraunrennsli** (lava flow) — direct property destruction risk
- **Jökulhlaup** (glacial outburst flood) — Grímsvötn and Grænalón are the two commonest sources, each with 45+ floods in historical time (a small 2003 Grænalón flood ran ≈ 13 km under Skeiðarárjökull into Súla); the last large damaging one, the Skeiðará flood of Nov 1996, carried icebergs that damaged bridges and power lines on Skeiðarársandur; a Katla flood from Mýrdalsjökull is one of the main jökulhlaup hazards today (source Veðurstofan "Jökulhlaup" article)
- **Snjóflóð** (avalanche): Westfjords + East fjords known fatal events
  - **Flateyri 1995** (20 dead), **Súðavík 1995** (14 dead) — 34 deaths combined per Veðurstofan, which counts 193 avalanche + landslide deaths in the 20th century; **Neskaupstaður, ≈ 20 Dec 1974** (12 dead in two avalanches) (sources Veðurstofan ofanflóð hættumat page + Snjóflóðasaga Neskaupstaðar, VÍ rit 97002)
- **Skriðuhætta** (landslide / debris flow): Veðurstofan has ofanflóð (avalanche + landslide) hazard zoning in force for towns from Reykjavík and Mosfellsbær through Snæfellsnes, the Westfjords, the North and the East Fjords to Kirkjubæjarklaustur and Vík — check the town's map (source Veðurstofan hættumat page)
  - **Seyðisfjörður, 15–18 Dec 2020**: landslides destroyed or damaged more than 10 buildings (no injuries) after 569.9 mm of rain on 14–18 Dec, the heaviest five-day rainfall measured in Iceland; Veðurstofan ranks it the most damaging landslide to hit an urban area in Iceland (sources Veðurstofan news 8 Jan 2021 + vísindanefnd 2023 climate report)
- **Strandrof** (coastal erosion) + sea-level rise
- **Sjávarflóð / stormflóð** (sea flood, storm surge) — Veðurstofan lists a higher sea-flood risk in Grindavík from land subsidence (source Veðurstofan Reykjanes overview 26 Feb 2024); see the sea-level projections below
- **Veðuröfgar** (extreme weather) — records: 62.5 m/s 10-minute mean wind (Skálafell við Esju, 20 Jan 1998), 74.2 m/s gust (Gagnheiðarhnúkur, 16 Jan 1995), 59.4 m/s gust in Reykjavík (15 Jan 1942) (source Veðurstofan "Íslensk veðurmet" page)

### Insurance via Náttúruhamfaratrygging Íslands (NTÍ)

**MANDATORY natural disaster insurance** — automatic via property insurance:
- Covers: volcanic eruptions, earthquakes, landslides, avalanches, water floods (vatnsflóð) — NOT meltwater / rapid-thaw / cloudburst floods, storm or wind damage, snow-load damage (2026 data, source island.is NTÍ damage page). Vatnsflóð means a sudden overflow of permanently flowing rivers or streams, a flood wave from the sea or a lake suddenly coming ashore, or a sudden glacier flood from melting ice (jökulhlaup); floods from rain or snowmelt and man-made failures (tanks, dams) are excluded, and ash that settled and is later blown onto the property is not an eruption loss (2026 data, source reglugerð 770/2023 art. 2, island.is)
- All buildings and contents fire-insured with an Icelandic-licensed insurer are covered; the premium is collected with the fire-insurance premium (2026 data, source island.is/en/o/nti)
- **Deductible (eigin áhætta)**: minimum ISK 400,000 per building, ISK 200,000 on contents / movables; report damage within 1 year of becoming aware of it (2026 data, source island.is NTÍ damage page)
- **Payout basis**: a building's insured sum is its brunabótamat (the policy amount for buildings under construction and for extra fire cover above brunabótamat) and is the ceiling; partial damage is paid at the cost of repairing it to the same or nearly the same condition (never more than the drop in value); a total loss is capped at the property's actual value at the time of loss, after depreciation for age, use and upkeep (vátryggingarverðmæti, art. 8), where that is at or below the insured sum; direct damage only — no consequential loss, no purely cosmetic damage, cheapest suitable materials and methods unless the valuation reflects special ones (2026 data, source reglugerð 770/2023 arts 7, 8 + 11, in force since 19 Jul 2023, island.is)
- **NTÍ provides compulsory natural-hazard cover bundled into property insurance** (volcano, earthquake, landslide, avalanche, water flood as defined above — not storm, snow-load or rain / snowmelt floods). Limits: NTÍ may reduce or refuse compensation under art. 16 of Act 55/1992 where a building was put up at a site known in advance to be exposed to the hazard, so full compensation there cannot be assumed (2026 data, source NTÍ notice 28 Aug 2026); no new cover may be taken out, or old cover changed, for property in an area already in danger once an insured event has begun or is imminent (2026 data, source reglugerð 770/2023 art. 6)
- For Grindavík: state purchase via Þórkatla (Act 16/2024; 961 properties purchased — 2026 data, source torkatla.is) + NTÍ payouts for natural-hazard damage

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960** | Low seismic standards (wisdom, not data — check the design basis on the approved drawings held by the municipal byggingarfulltrúi) |
| **1960s onwards** | Gradually improved (wisdom, not data) |
| **From 1 Jul 1992 at the latest** | Byggingarreglugerð 177/1992 art. 7.2.1: structural design to the load standard ÍST 12 and the seismic standard ÍST 13 (Jarðskjálftar, álag og hönnunarreglur); from Jul 1998 byggingarreglugerð 441/1998 art. 126.2: ÍST DS 409:1982, ÍST 12:1989 and ÍST 13:1989 (sources reglugerd.is 177/1992 + 441/1998) |
| **From 1 Jul 2002** | Amendment 425/2002: either Danish-based standards with Icelandic provisions or the European pre-standards (ENV Eurocodes) with Icelandic national documents once published — one set per structure (source reglugerd.is 425/2002) |
| **From Dec 2010** | Amendment 1016/2010 (signed 22 Dec 2010), then byggingarreglugerð 112/2012 (in force 9 Feb 2012): Eurocodes with Icelandic national annexes; 112/2012 Part 13 sets energy-saving and insulation (U-value) rules (sources reglugerd.is 1016/2010 + island.is 112/2012) |
| **Concrete + steel reinforcement** | Dominant structure type (wisdom, not data) |
| **Wood common in older buildings** | Fire risk (wisdom, not data) |
| **Asbestos** | Buildings built before 1983 may contain asbestos (e.g. in walls or pipes); its use has been banned since; demolition or repair of asbestos-containing parts only by certified workers with Vinnueftirlitið's permission (2026 data, source Vinnueftirlitið asbestos page, island.is) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Söluyfirlit** (sales prospectus) | Drawn up by the licensed estate agent (fasteignasali) and handed to a prospective buyer, who signs for it, before any offer; must state the property's condition including defects known to the seller and/or agent, fasteignamat, brunabótamat, and the mortgages and encumbrances per the veðbókarvottorð; the seller signs a declaration that its content is correct to the best of their knowledge (source lög nr. 70/2015 um sölu fasteigna og skipa arts 10–11, althingi.is, archived 2026-08-31) | Updated by the agent if older than 3 months, unless nothing in it has changed |
| **Fasteignamat** | Current valuation (HMS); base for fasteignagjöld, stamp duty and inheritance tax | Annual — owners notified in June, takes effect 31 Dec for the following year (2026 data, source island.is/fasteignamat) |
| **Veðbókarvottorð** (encumbrance certificate) | Title verification — lists what is registered on the property (loans, encumbrances, leases, lot leases, eignaskiptasamningar, powers of attorney); anyone can order one for any property from the sýslumenn, ISK 3,100 per certificate online (2026 data, source island.is Veðbókarvottorð) | At sale |
| **Energy performance certificate** | **Not required in Iceland** — EEA Joint Committee Decisions 135/2022 and 175/2025 exempt Iceland from the EPBD (temporary, until the 2024/1275 recast is incorporated); Iceland's declaration to JCD 175/2025 says it "has not implemented any previous versions of the EU energy performance in buildings acquis" (2025 data; JCD 175/2025 entry into force still pending in 2026, source EFTA EEA-Lex) | n/a |
| **Brunabótamat** (insurance valuation) | All buildings must be fire-insured; insured sum based on brunabótamat (rebuild cost less depreciation; excludes contents) | Recalculated at end of May each year, indexed monthly to the building-cost index; reassessment on request after renovation (2026 data, source island.is/brunabotamat) |

### Climate change projections (Veðurstofan)

- Warming vs 1986–2015: **1.0–1.7 °C** by mid-century in every emission scenario; by 2100 **2.0–2.8 °C** in the intermediate scenarios, 1.0 °C in the coldest and **3.5 °C** in the warmest (uncertainty brackets −1.1 to 2.6 °C mid-century, 0.0 to 5.4 °C for the intermediate 2100 scenarios) (2023 data, source Veðurstofan vísindanefnd 4th report "Umfang og afleiðingar hnattrænna loftslagsbreytinga og áhrif þeirra á Íslandi", which replaces the 2018 report, loftslagsskyrsla.is — rates/figures may have changed since)
- Sea-level change is **coast-specific, not national**: by 2100 relative sea level could rise by up to 1.2 m where land subsidence is greatest and fall by up to 1.5 m where land uplift is greatest; by 2150 the median rise near Iceland is 1–2 m, under 1 m in many places (2023 data, same source — rates/figures may have changed since). Glacial-rebound uplift is strongest on the south-east coast; the south-west has subsided, putting low-lying parts of the capital area and Reykjanesskagi at risk (source Veðurstofan "Líklegar breytingar á Íslandi" page, based on the 2008 report) — check the property's coastal segment
- Glacier retreat: glacier area down 19% since the late-19th-century maximum, some glaciers gone and proglacial lakes growing or forming; glacier shrinkage of ≈ 40–50% projected even if the Paris Agreement holds, more if it does not (2023 data, same source — rates/figures may have changed since)
- Precipitation: annual totals up by just over 1% per °C of warming; extreme precipitation up 5–15% (≈ 4–15 mm/day for most areas), and in the warmer scenarios today's 100-year rainfall event recurs every 12–17 years (2023 data, same source — rates/figures may have changed since)
- Ocean circulation (AMOC): the IPCC rates a weakening this century as very likely and an abrupt collapse before 2100 as unlikely; a large weakening would cool the sea around Iceland, now ≈ 2–3 °C warmer than the Pacific at the same latitude, but effects may show as shifts in sea conditions, weather patterns and variability rather than simple cooling (2026 data, sources Veðurstofan AMOC Q&A 27 Apr 2026 + vísindanefnd 2023 report)

---

## Section: `--mains`

### Sources

- **Veitur** (capital-area utility: hot water, cold water, sewer, electricity distribution; tariffs at `https://www.veitur.is/verdskrar`): `https://www.veitur.is/`
- Elsewhere, municipal water utilities (vatnsveitur sveitarfélaga) under Act 32/2004; the municipality levies vatnsgjald on owners of property that can draw water from its utility (source reglugerð 401/2005 on vatnsveitur sveitarfélaga, island.is)
- **Hitaveita** (district heating co-operatives) per region

### Verification

- **Geothermal hot water (jarðhiti)** heats ~90% of the population — UNIQUE (Orkustofnun: jarðhiti "sér 90% landsmanna fyrir ... húshitun"; undated post-2022 article — rates/figures may have changed since)
  - Cheap energy, almost universal in populated areas
  - The other ~10% rely on electric heating, partly state-subsidised (same source); some Westfjords + East fjord settlements among them (wisdom, not data — verify the address's heating with the local utility)
- **Cold water** + **sewer** typically per municipality
- **Rotþrær / fráveitukerfi**: a rural house or cottage that cannot connect to the municipal sewer must treat its wastewater in a septic tank with soakaway (rotþró með siturlögn) or an equivalent two-stage system, to ÍST EN 12566 where applicable; individual treatment systems and new or upgraded sewers need the local heilbrigðisnefnd's instructions and permit (2026 data, source reglugerð 1450/2025 art. 5, in force since 24 Dec 2025, island.is)

### Costs

| Scenario | Cost (ISK) |
|---|---:|
| Hitaveita connection — Veitur area, urban heimæð < 50 m, 20–32 mm steel (25–40 mm PEX), incl. 11% VSK | 466,855–1,195,146 (Veitur tariff in force from 1 Dec 2025); rural lögbýli / year-round house, heimæð < 70 m: 675,411–1,729,044; summer-cottage areas, heimæð < 100 m, 20 mm PEX: 979,144 (689,397 if laid in the same trench as Veitur's cold-water line) |
| Cold water + sewer connection — Veitur area: cold water 32–40 mm (VAT-exempt) + sewer for a new-area plot in Reykjavík / Akranes / Borgarbyggð | ≈ 996,204–1,163,524 computed (cold water 389,962–557,282, tariff from 1 Oct 2026, + sewer 606,242 per plot, tariff from 1 Jan 2026); infill plots pay actual cost |
| Mains-line extension | data not publicly available — priced per project cost estimate (kostnaðaráætlun); verify at `https://www.veitur.is/verdskrar` or the local utility |

> Connection rows are Veitur tariffs (2026 data, source veitur.is/verdskrar); cold-water and sewer fees are indexed to the building-cost index, so amounts drift. Other hitaveitur and municipal water/sewer utilities set their own tariffs — check the local one. Where the surface is already finished and adequate mains have not reached the plot boundary, Veitur's tariff prices do not apply and the applicant pays per cost estimate (Veitur hot-water tariff in force from 1 Dec 2025) — get the utility's estimate.

---

## Cost benchmarks (IS 2026)

| Work | Cost (ISK) |
|---|---:|
| Stimpilgjald | 0.8% of fasteignamat (0.4% FTB; 1.6% legal entity) |
| Þinglýsingargjald | 3,800 per document |
| Fasteignasalalaun | 1.4–2.5% of price + 24% VSK (seller; 2026 agency price lists ⚠️) |
| Umsýslugjald kaupanda (agency buyer fee) | 69,900–79,900 incl. VSK (2026 agency price lists ⚠️) |
| **Total transaction cost (buyer)** | **0.8% of fasteignamat + 3,800 per document** (0.4% FTB), plus the agency buyer fee where charged |
| Gagnaöflunargjald seljanda (seller's document / listing fee) | 54,900–79,900 incl. VSK (2026 agency price lists ⚠️) |
| Energy upgrade | est. 4,000,000–12,000,000 |
| Antiseismic retrofit | est. 3,000,000–8,000,000 |
| Roof (corrugated steel, 150 m²) | est. 2,000,000–4,000,000 |
| Asbestos abatement | est. 800,000–3,000,000 |
| Hitaveita connection (Veitur area, urban, heimæð < 50 m, 20–32 mm steel) | 466,855–1,195,146 incl. 11% VSK (rural lögbýli 675,411–1,729,044; Veitur tariff from 1 Dec 2025) |

> Stimpilgjald and þinglýsingargjald are sourced (island.is Þinglýsing skjala, 2026 data); the total is computed from them. Broker commission, buyer fee and the seller's document fee come from five published agency price lists (RE/MAX valid from 20 Oct 2026, Landmark from 1 Oct 2025, Gimli from 1 Jan 2025, Hraunhamar and Heimili undated; 2026 data, agency tier ⚠️): indicative and negotiable, not a regulator figure or index; Heimili's list includes the söluyfirlit (sales overview) in the commission. The hitaveita row is the Veitur tariff (2026 data, source veitur.is/verdskrar; see `--mains` › Costs) — other hitaveitur set their own. The energy-upgrade, antiseismic-retrofit, roof and asbestos rows are indicative contractor ranges (est.) carried unchanged since the first release (Apr 2026), not from a published index — get quotes; for scale, Hagstofa's building cost index rose 1.4% between Apr and Oct 2026 (computed: 128.6 → 130.4, base 2021 = 100; 3.6% y/y in Oct 2026) (2026 data, source Hagstofa VIS13000).

## Active fiscal incentives (2025-2026)

- **Endurgreiðsla VSK** (35% VAT refund on on-site labour): for new build, renovation, maintenance of residential housing (2026 data, source island.is)
- **Séreignarsparnaður — fyrsta íbúð** (Lög nr. 111/2016): a first-time buyer (never registered owner of more than 30% of residential property in Iceland) holding ≥30% of the property may use voluntary pension savings tax-free toward the purchase or the mortgage, max **ISK 500,000/yr per person** for 10 consecutive years (ISK 5,000,000 total); apply within 12 months of signing the purchase contract. Someone who has owned no residential property (and was not jointly taxed with an owner) for 5 years also qualifies, but only if their combined income and capital-income tax base in the income year before the purchase does not exceed the third-bracket threshold (ISK 15,901,523 for income year 2025) (2026 data, source skatturinn.is Fyrsta íbúð)
- **Séreignarsparnaður inn á húsnæðislán** (any owner-occupier with ≥30% share, lögheimili in the home and a mortgage on it): up to **ISK 500,000** per person in 2026 paid tax-free into the mortgage, for up to 10 years in total (2026 data, source skatturinn.is Ráðstöfun inn á húsnæðislán)
- **Hlutdeildarlán** (HMS shared-equity loan): first-time buyer (or no home owned for 5 years) with a 5% down payment, HMS-approved flat, income ≤ISK 10,000,000 (single) / 15,000,000 (couple) over the last 12 months (+ISK 2,254,000 per child under 20) → loan of up to **25%** of the price (35% under lower income caps); no interest or instalments, the amount tracks the property's value and is repaid on sale or after 10 years (extendable to 25) (2026 data, source island.is Hlutdeildarlán)
- **Húsnæðisbætur** (HMS): monthly benefit for renters, means-tested on household size, income, assets and rent; **sérstakur húsnæðisstuðningur** on top from the municipality (2026 data, source island.is Húsnæðisbætur)
- **Vaxtabætur** (mortgage interest credit, owner-occupied home loans only, requires unlimited tax liability or tax domicile in Iceland): max **ISK 420,000** (single) / **525,000** (single parent) / **630,000** (couple) in the 2026 assessment for 2025 interest; cut by 8.5% of the income base, reduced above net wealth of ISK 7,500,000 / 12,000,000 and lost at ISK 12,000,000 / 19,200,000 (2026 data, source island.is Fjárhæðir vaxtabóta)

## Common listing platforms

- **Mbl.is fasteignir** — `https://www.mbl.is/fasteignir/` (live, archived 2026-11-02); market share: data not publicly available
- **Fasteignir.is** (Vísir / Sýn) — `https://fasteignir.visir.is/`
- **RE/MAX, Eignamiðlun, Fasteignamarkaðurinn, Domus (Blönduós), Gimli** — estate agencies, all with agents on Félag fasteignasala's member list (2026 data, source ff.is Félagsmenn ⚠️ trade association)

## Caveats unique to IS

- **VOLCANIC + SEISMIC RISK IS REAL AND ACTIVE**:
  - Reykjanes 2023-2025 series destroyed homes in Grindavík
  - **9 eruptions since Dec 2023** at Sundhnúkur
  - **"New Reykjanes Fires"** potentially multi-century period
  - Property in Reykjanes peninsula carries elevated risk
- **Mandatory natural-hazard insurance (NTÍ)** is automatic via property insurance — major buyer protection
- **Geothermal heating** universal in populated areas — extremely cheap energy, but check connection
- **Currency volatility** — ISK can swing 20–30% vs EUR
- **Foreign-currency mortgages restricted, not banned** — a mortgage tied to a currency other than the borrower's income (an ISK loan to a euro earner counts) needs income in the loan's currency, a passed affordability test assuming large FX and rate moves (≥40% rise in repayments, Reglugerð nr. 270/2017 art. 6) or an FX hedge (Lög nr. 118/2016 art. 21, 2025 consolidated text, source althingi.is, archived 2025-08-28 — may have changed since); banks offer such loans to buyers with foreign-currency income or living abroad (2026 data, source reglugerd.is + Íslandsbanki / Arion product pages) — see `--tax` › Future risk
- **Foreigner restrictions** (**Lög um eignarrétt og afnotarétt fasteigna nr. 19/1966**; see also Lög nr. 74/2022): Icelandic citizens and foreign nationals domiciled in Iceland may own freely; EEA/EFTA nationals and entities and Faroese (Hoyvík Agreement) need no permit when they meet Regulation No. 702/2002 (arts 2–4) and file the declaration with the purchase contract; everyone else needs a **Minister of Justice (Dómsmálaráðuneytið) permit**, which may be granted only for direct business use, or to a natural person with a close connection to Iceland (e.g. marriage to a citizen) or for a home / leisure property on a rented lot — for one specific property of ≤**3.5 ha**, with no other property owned in Iceland (business use: up to 25 ha); the deed takes effect only once the minister has signed it; UK nationals need a permit since 31 Dec 2020; leases or use rights of ≤3 years (or terminable on <1 year's notice) need no permit (2026 data, source government.is Foreign nationals' real property rights). Land under **Jarðalög nr. 81/2004**: a legal person owning land covered by its art. 3 that is ≥1/3 foreign-owned or controlled, or foreign-based, must report its ownership chain and beneficial owners to Skatturinn's fyrirtækjaskrá by 1 Feb each year (art. 10 b) (2026 data, source skatturinn.is Eignarhald – jarðalög) — verify the ministry responsible for Jarðalög at stjornarradid.is
- **Sumarbústaður** (summer cottage) — different regime, often in privately-owned summer-cottage zones
- **Leigulóðir** (leased lots) — many plots are leased from the sveitarfélag under a lóðarleigusamningur, with annual lóðarleiga on top of fasteignaskattur (Reykjavík 2026: 0.20% of lot valuation residential / 1.00% commercial) (2026 data, source reykjavik.is Fasteignagjöld)
- **Reykjavík dominates** — 65% of population in capital region
- **Build quality varies** — older buildings concrete-clad; newer have improved seismic
- **Inflation** peaked at 10.2% y/y (Feb 2023), eased to 4.1% (Sep 2025) and re-accelerated to 5.9% (Sep 2026) against the 2.5% target; Central Bank key rate **8.00%** (valid from 7 Oct 2026, next decision 18 Nov 2026) — not a cooling phase (2026 data, source cb.is + Hagstofa VIS01000)
- **Population growth via immigration** has tightened housing market
- **Iceland is NOT in EU** — but EEA member; some property buying restrictions apply
- **Landfilling permits** restrictive in earthquake-prone zones
- **Brunabótamat** (fire insurance valuation, set by HMS) — fire insurance of every building is compulsory and its sum follows the brunabótamat; HMS recalculates it at the end of May each year and indexes it monthly to the building cost index; owners can request a revaluation after renovations (2026 data, source island.is Fire insurance value)
- **Westfjords avalanche risk** — Flateyri, Súðavík, Neskaupstaður all had fatal events
- **Húsfélag** (building association) — read meeting minutes + financials before apt purchase

## Reddit / forum sources

- **r/Iceland** — active, English-friendly
- **r/VisitingIceland** — tourism but useful
- **r/iceland** (lower-case)
- **r/nordiccountries**
- Expat: **Iceland Review**, **Iceland Monitor**, **The Reykjavík Grapevine**

## Verification authorities

| Authority | When to call |
|---|---|
| **HMS Fasteignaskrá** | Title verification, fasteignamat |
| **Sveitarfélag** | Permits, planning, fasteignagjöld |
| **Skatturinn (Ríkisskattstjóri, RSK)** | Tax calculations, capital gains |
| **Veitur or local hitaveita** | Heating + water connection |
| **Almannavarnir** | Hazard zone status |
| **Veðurstofan** | Volcanic + seismic risk, Grindavík / Svartsengi hazard map, avalanche + landslide hazard zoning (ofanflóðahættumat) |
| **NTÍ (Náttúruhamfaratrygging Íslands)** | Natural-hazard damage claims (report within 1 year) |
| **Þórkatla / Grindavíkurbær** | Grindavík buyback status, municipal risk assessment |
| **Húsfélagsstjórn** | If apartment building |

## Source URL templates

| Source | URL pattern |
|---|---|
| HMS Fasteignaskrá | `https://www.hms.is/` |
| Skra.is | `https://skra.is/` |
| Mbl Fasteignir | `https://www.mbl.is/fasteignir/` |
| Veðurstofan IMO | `https://www.vedur.is/` |
| Almannavarnir (Civil Protection) | `https://www.almannavarnir.is/` |
| Hagstofa (Statistics) | `https://hagstofa.is/` |
| Náttúruhamfaratrygging Íslands (NTÍ) | `https://island.is/s/nti` |
| Vegagerðin | `https://www.vegagerdin.is/` |
| Vegagerðin traffic-count map | `https://umferd.vegagerdin.is/` |
| Skatturinn (RSK, tax) | `https://www.skatturinn.is/` |
| Veitur (capital-area utility) | `https://www.veitur.is/` |
| Veitur tariffs (incl. connection fees) | `https://www.veitur.is/verdskrar` |
| Reykjanes volcanic monitoring | `https://www.vedur.is/skjalftar-og-eldgos/jardskjalftar/reykjanesskagi/` |
| Veðurstofan news (English; eruption + Svartsengi updates) | `https://en.vedur.is/about-imo/news/` |
| Veðurstofan avalanche hazard zoning | `https://www.vedur.is/ofanflod/haettumat/` |
| Þórkatla (Grindavík buyback) | `https://torkatla.is/` |

## Status

✅ **Fully populated**; fast-changing sections re-verified as of 2026-10-23, figures with no current primary source labelled by source tier (⚠️), est., curated wisdom, data not publicly available or verify-at, and older-source figures marked 'may have changed since' (initial population 2026-04-25). Rental tracker entries re-checked 2026-09-24 in the October regwatch wave (see shared/regulatory-watch.md). Rental tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks (incl. live volcanic eruption series), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for country profile, `--traffic`, the foreign-buyer rules and the verification authorities (re-verified 2026-10-23 against Hagstofa, cb.is, EFTA EEA-Lex, Vegagerðin, government.is and skatturinn.is — see the per-section table). HIGH for the individual facts refreshed 2026-10-23 that carry an inline primary source: statutory tax rates and fees (skatturinn.is, island.is, samband.is, reykjavik.is), heimagisting caps, notice periods and rental-income tax (island.is, skatturinn.is), the Reykjanes eruption count, Grindavík buyback and NTÍ cover (Veðurstofan, torkatla.is, island.is), national wages and company capital (Hagstofa, skatturinn.is), Veitur connection tariffs and the Central Bank key rate (cb.is). `--price`, `--tax`, `--rental`, `--work`, `--risks` and `--mains` are not re-stamped: each still holds lines that could not be re-checked, so they keep the 2026-04-25 date. MEDIUM for the 2025 ISK/m² price table (HMS not reachable for re-check; only a Hagstofa index re-anchor to Sep 2026 was added), the fasteignamat-to-market ratio, the listing-platform and agency lines, the build-era table, the "New Reykjanes Fires" framing and the other hazard descriptions not re-checked, and the foreign-currency-mortgage ban. Est. only (no published index) for the broker fee, söluyfirlýsing, construction / retrofit and mains-extension ranges and the regional salary split. MEDIUM for currency-related advisories (ISK volatile).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | Postcodes, 8 landshlutar and EEA (not EU) status confirmed; municipalities 64 → 62 and EUR/ISK updated (Hagstofa, cb.is, EFTA EEA-Lex); HMS cadastre role not re-fetched |
| `--traffic` | 2026-10-23 | 2026-10-23 refresh wave | Vegagerðin URLs and ÁDU definition confirmed; verdict bands calibrated on Vegagerðin 2025 ÁDU key-counter tables |
| Foreign-buyer rules (Caveats) | 2026-10-23 | 2026-10-23 refresh wave | Act 19/1966 permit rules (government.is, Ministry of Justice) and Jarðalög 81/2004 art. 10 b reporting duty (skatturinn.is) |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | RSK renamed Skatturinn; Veðurstofan role extended; NTÍ and Þórkatla / Grindavíkurbær rows added |
| `--price` | 2026-10-23 | 2026-10-23 gap-closing pass | ISK/m² and house-price table rebuilt from the HMS Kaupskrá fasteigna CSV (contracts signed Oct 2025–Sep 2026: 9,302 usable contracts of all types, the table using 6,219 flats of 20 m² or more, 967 detached houses and 304 cottages; interquartile ranges, computed); fasteignamat ratio computed per contract (median 96% in 2026, 89% in 2025); Hagstofa VIS01106 re-anchor and CPI path re-checked; Mbl.is, Húsaleiga.is and Bland.is confirmed; fasteign.is ❌ DEPRECATED, Brynja dropped; hms.is figures read from archived copies of its pages |
| Common listing platforms | 2026-10-23 | 2026-10-23 gap-closing pass | Mbl.is confirmed (archived 2026-11-02), its "biggest" claim → market share data not publicly available; agencies checked against Félag fasteignasala's member list ⚠️, Brynja dropped; Fasteignir.is from the refresh |
| `--rental` | 2026-10-23 | 2026-10-23 gap-closing pass | Heimagisting bullet re-read in Stjórnartíðindi (A 67/2016, A 43/2024, A 25/2026, A 82/2026); Eignaskattfrelsi line replaced by Skatturinn's wealth-tax position (auðlegðarskattur only 2010–2014); short-let VSK 11% and gistináttaskattur ISK 800 sourced (skatturinn.is); L. 72/2025 leiguskrá registration and no rent change in a fixed-term lease's first 12 months added; tenancy-protection and fixed-term judgements labelled wisdom |
| `--work` | 2026-10-23 | 2026-10-23 gap-closing pass | Regional salary split stays est., now computed from Hagstofa TEK01002 2025 municipal median atvinnutekjur; RSK (Skattur) → Skatturinn; Mbl Atvinna confirmed (archived 2026-11-02); VIN02004 wages, SGS tariff, company capital and VSK threshold from the refresh |
| `--tax` | 2026-10-23 | 2026-10-23 gap-closing pass | Broker commission 1.4–2.5% + 24% VSK and the agency buyer / seller fees from five agency price lists ⚠️; builder VSK refund limited to on-site labour (island.is); foreign-currency mortgages restricted, not banned (Reg. 270/2017 art. 6, Act 70/2021 art. 5, bank product pages); 35% refund history re-confirmed; other rates from the refresh |
| Cost benchmarks (IS 2026) | 2026-10-23 | 2026-10-23 gap-closing pass | Broker, buyer-fee and seller document-fee rows from agency price lists ⚠️; hitaveita row aligned with the Veitur tariff (from 1 Dec 2025); the unconfirmed söluyfirlýsing name dropped; energy, antiseismic, roof and asbestos rows stay est. with a Hagstofa VIS13000 calibration sentence |
| `--risks` | 2026-10-23 | 2026-10-23 gap-closing pass | Hazard lines re-sourced to Veðurstofan, island.is, reglugerd.is, Vinnueftirlitið, sýslumenn and the 2023 climate committee report; Reykjanes status extended to 27 Oct 2026; NTÍ payout basis and limits added; seismic-design era from Byggingarreglugerð 177/1992, older build-era rows labelled wisdom; Söluyfirlit (Act 70/2015, archived althingi.is text) replaces Söluyfirlýsing; Hekla "overdue" kept as IMO's 2016 wording |
| `--mains` | 2026-10-23 | 2026-10-23 gap-closing pass | Veitur hot-water, cold-water and sewer tariffs re-confirmed, frístundahús rate added; mains-extension cost → data not publicly available (priced per cost estimate); municipal water sourced to reglugerð 401/2005, rotþrær to reglugerð 1450/2025; Westfjords / East-fjords electric-heating line labelled wisdom |

## Extension TODOs

- [ ] Per-sveitarfélag fasteignagjöld rates
- [ ] Reykjanes volcanic risk monitoring (live eruption series)
- [ ] Foreigner buying restrictions decision tree
- [ ] Geothermal connection verification per address
- [ ] Sumarbústaður zone vs residential zone
- [ ] Currency hedging for foreign buyers (ISK volatility)
- [ ] Avalanche zone overlay (Westfjords, East fjords)
- [ ] Húsfélag financial health check rubric (apartment buildings)
- [ ] Brunabótamat verification process
- [ ] Endurgreiðsla VSK eligibility flow

## Update history

- **2026-04-25** — Initial population (researched 2026-04).
- **2026-05-27** — Stamp duty, capital gains, VAT, heimagisting and foreign-buyer lines verified (inline 2026-05-27 stamps).
- **2026-09-24** — Rental tracker entries re-checked in the October regwatch wave (see shared/regulatory-watch.md).
- **2026-10-21** — Rental tracker entry re-checked (December regwatch wave, run early): heimagisting scope under L. 25/2026, L. 43/2024 and L. 82/2026.
- **2026-10-23** — Refresh wave (market, tax-legal and risk-infra clusters). Counts are facts changed / confirmed / unverifiable per section.
  - Re-verified (per-section table in Status): country profile 2 / 3 / 1 (municipalities 64 → 62; 1 EUR ≈ 145–155 ISK → ≈ 136 ISK); `--traffic` 3 / 4 / 0 (Vegagerðin traffic-count map and umferðartölur, ÁDU / SDU / VDU definitions, bands calibrated on 2025 ÁDU counters); verification authorities 2 / 5 / 0 (RSK → Skatturinn; NTÍ and Þórkatla / Grindavíkurbær added); foreign-buyer rules 2 / 0 / 0 (Act 19/1966 permit rules, Jarðalög 81/2004 art. 10 b).
  - `--price` 4 / 3 / 8 — Hagstofa index renamed (Vísitala markaðsverðs íbúðarhúsnæðis, VIS01106) and a Sep 2025 → Sep 2026 index re-anchor added under the 2025 table (whole country +2.1%); Fasteignir.is URL; CPI path to 5.9% (Sep 2026). Not re-checked: the ISK/m² table, the HMS report and search, fasteign.is, the fasteignamat ratio, mbl.is and most agencies (hms.is and mbl.is block automated fetch).
  - `--tax` 13 / 17 / 2 — fasteignagjöld statutory bands; stimpilgjald charged on fasteignamat, not price; þinglýsingargjald ~ISK 30,000 flat → ISK 3,800 per document; buyer-side total recomputed; capital-gains exemption (full 2 years, 600 / 1,200 m³ cap); VSK scope and the 35% refund history. Not re-checked: broker fee (now est.) and the foreign-currency-mortgage ban.
  - Cost benchmarks 3 / 0 / 2 — stamp-duty and registration rows sourced, total computed from them; broker and söluyfirlýsing rows labelled est.
  - Active fiscal incentives 5 / 0 / 0 — every scheme re-sourced to skatturinn.is / island.is; "Almenna lánasjóðurinn" replaced by Hlutdeildarlán.
  - `--rental` 4 / 5 / 3 — rental-income tax 22% on 75% of gross rent (frítekjumark 25% from income year 2026) replaces the 24.5–46.25% range; notice periods detailed; heimagisting income taxed as 22% capital income within ISK 2,000,000; registration fee ISK 9,200; EU 2024/1028 EEA-Lex status. Not re-checked: the Eignaskattfrelsi line and VSK on licensed short-lets; the long heimagisting bullet keeps its 2026-10-21 verification.
  - `--work` 5 / 5 / 2 — Vinnumálastofnun URL; einstaklingsrekstur; VSK threshold ISK 2,000,000; Hagstofa VIN02004 2025 wages (median ISK 895,000/mo); lowest SGS–SA tariff ISK 476,379 (Apr–Dec 2026). Regional split labelled est.; Mbl Atvinna not re-checked.
  - `--risks` 19 / 11 / 22 — Reykjanes count (9 Sundhnúkur eruptions since Dec 2023, 12 on the peninsula since 2021, none through 30 Sep 2026); Grindavík buyback via Þórkatla (961 properties purchased); quake rate (~500/day → 2,000–5,500/month); NTÍ name, URL and cover (water floods only; not meltwater, storm or snow-load damage); fasteignamat and brunabótamat cycles; EPC row (Orkumerki "mandatory since 2013" → not required in Iceland, EEA JCD 135/2022 and 175/2025); climate projections (2018 IMO report). Not re-checked: build-era table, "New Reykjanes Fires" framing, Hekla "overdue", Holuhraun superlative, Grímsvötn, Eurocode 8, Seyðisfjörður, wind records, NTÍ payout basis.
  - `--mains` 5 / 2 / 3 — Veitur tariffs URL; geothermal heating share ~90% of the population (Orkustofnun); Veitur-area hitaveita and cold water + sewer connection tariffs replace est. ranges. Mains-extension range stays est.
  - Common listing platforms 1 / 2 / 1 — Visir.is → Fasteignir.is (Vísir / Sýn).
  - Reddit / forum sources 0 / 2 / 5 — Iceland Review and The Reykjavík Grapevine live; Reddit (bot challenge) and Iceland Monitor (403) not re-checked.
  - Source URL templates 4 / 5 / 2 — NTÍ → island.is/s/nti; RSK → skatturinn.is; Reykjanes row → Reykjanesskagi page; traffic map, Veitur tariffs, Veðurstofan news and avalanche-zoning and Þórkatla rows added; hms.is (429) and mbl.is (403) kept, content not re-checked.
  - Caveats unique to IS (legal / fiscal items) 5 / 1 / 2 — foreigner restrictions, leased lots (leigulóðir), inflation / key-rate bullet (key rate 8.00% valid from 7 Oct 2026, inflation 5.9%; cb.is), brunabótamat. Not re-checked: foreign-currency-mortgage ban, landfilling permits; the volcanic, population and currency caveats were outside these clusters.
  - Gap-closing pass (sources read 2026-11-03; confirmed / changed / relabelled): `--price` 2 / 4 (incl. 1 deprecation) / 3; Common listing platforms 0 / 0 / 2; `--rental` 2 / 4 / 1; `--work` 1 / 1 / 1; `--tax` 1 / 4 / 0; Cost benchmarks 0 / 5 / 4; `--risks` 5 / 20 / 2; `--mains` 1 / 2 / 3 — all closed; Caveats unique to IS 0 / 1 / 0 (foreign-currency-mortgage bullet), still open; total 12 / 41 / 16. Main changes: ISK/m² and house-price table rebuilt from HMS Kaupskrá fasteigna contracts signed Oct 2025–Sep 2026 (computed interquartile ranges) and the fasteignamat ratio computed per contract (median 96% in 2026); fasteign.is ❌ DEPRECATED and Brynja dropped, agencies checked against Félag fasteignasala's member list; heimagisting bullet re-read in Stjórnartíðindi, Eignaskattfrelsi line replaced by Skatturinn's wealth-tax position, VSK 11% and gistináttaskattur on licensed short-lets and the L. 72/2025 leiguskrá rule added; regional salary split computed from Hagstofa TEK01002; broker commission (1.4–2.5% + VSK) and agency buyer / seller fees from five agency price lists ⚠️; builder VSK refund limited to on-site labour; foreign-currency mortgages restricted, not banned (Reg. 270/2017, Act 70/2021); hitaveita cost row aligned with the Veitur tariff; hazard lines re-sourced to Veðurstofan, island.is and reglugerd.is, NTÍ payout basis and limits added, seismic-design era from Byggingarreglugerð 177/1992, Söluyfirlit (Act 70/2015) replaces Söluyfirlýsing, climate block moved to the 2023 committee report; mains-extension cost → data not publicly available, municipal water and rotþrær lines sourced to reglugerðir 401/2005 and 1450/2025
  - Playbook-level date re-stamped 2026-10-23: every fast-changing section is now re-verified — `--traffic` in the refresh above, `--price`, `--tax`, `--rental`, `--work`, `--risks`, `--mains` and Cost benchmarks (with Common listing platforms) in the gap-closing pass above; Caveats unique to IS (landfilling permits and the volcanic, population, currency and build-quality caveats), Reddit / forum sources and Source URL templates stay refreshed, not fully re-verified.
