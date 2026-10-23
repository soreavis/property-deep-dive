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
  - Free property search
- **Þjóðskrá Íslands** (national registry): `https://skra.is/`
- **Hagstofa Íslands (Statistics Iceland)** — Vísitala markaðsverðs íbúðarhúsnæðis (table VIS01106): `https://hagstofa.is/`
  - Monthly market-price index of residential housing, split capital-region flats / capital-region detached / outside capital region / whole country (latest month 2026M09 at 2026-10-23)
- **Seðlabanki Íslands (Central Bank)** — financial stability reports: `https://www.cb.is/`
- **HMS** publishes monthly Húsnæðismarkaðurinn (housing market) report

### Listing platforms

- **Mbl.is fasteignir**: `https://www.mbl.is/fasteignir/`
- **Fasteignir.is** (Vísir / Sýn): `https://fasteignir.visir.is/` (fasteignir.is redirects here)
- **Húsaleiga.is**, **Bland.is** for rentals
- **Remax IS**, **Eignamiðlun**, **Fasteignamarkaðurinn**, **Domus**, **Gimli**, **Brynja** — agency networks
- **fasteign.is** (HMS public listing)

### 2025 price benchmarks (Hagstofa + HMS) — 2025 data; figures may have changed since, re-check current Hagstofa íbúðaverðsvísitala

| Region | Avg ISK/m² (apt) | Avg total (einbýlishús) |
|---|---:|---:|
| **Reykjavík 101 (centro)** | 950,000–1,400,000+ | 110,000,000–250,000,000 |
| **Reykjavík 105/107 (Hlíðar/Vesturbær)** | 800,000–1,100,000 | 90,000,000–150,000,000 |
| **Greater Reykjavík (Kópavogur, Hafnarfjörður, Garðabær)** | 650,000–950,000 | 75,000,000–130,000,000 |
| **Akureyri** | 500,000–700,000 | 55,000,000–85,000,000 |
| **Reykjanesbær** | 450,000–650,000 | 50,000,000–75,000,000 |
| **Selfoss / Árborg** | 480,000–650,000 | 55,000,000–80,000,000 |
| **Westfjords / East fjords** | 250,000–500,000 | 25,000,000–55,000,000 |
| **Sumarbústaðir** (cottages) | varies | 15,000,000–80,000,000+ |

> Index movement since the table (nominal re-anchor, not a per-m² refresh): Hagstofa Vísitala markaðsverðs íbúðarhúsnæðis, Sep 2025 → Sep 2026: whole country 803.4 → 820.6 (+2.1%), capital-region flats 787.8 → 795.7 (+1.0%), capital-region detached 873.0 → 896.1 (+2.6%), outside capital region 799.6 → 833.9 (+4.3%), against 5.9% CPI inflation over the same 12 months — a real-terms decline (2026 data, source Hagstofa VIS01106 + VIS01000; % changes computed).

### Compute

1. ISK/m² = price / **Brúttóflatarmál** (gross floor area, BBR equivalent)
2. **Fasteignamat** ≈ 80–95% of market price typically (HMS conservative)
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
- **Fasteignasalalaun** (broker): est. **1–2%** paid by seller (negotiable; not from a published index)

### Total transaction cost (buyer side)

- **First-time buyer**: 0.4% × fasteignamat + ISK 3,800 per registered document (computed from the rates above)
- **Standard buyer**: 0.8% × fasteignamat + ISK 3,800 per registered document (computed); legal entity 1.6% × fasteignamat
- Lender fees and any buyer-side adviser fees come on top (not included)
- Seller: est. 1–2% (broker)

### Capital gains — Fjármagnstekjuskattur

- **22% flat** for individuals (22% since 1 January 2018; raised from 20% in effect 2011–2017) (2026 data, source skatturinn.is Helstu tölur 2026 + Fjármagnstekjuskattur)
- Statute: **Lög um tekjuskatt nr. 90/2003**
- **Residential property (íbúðarhúsnæði) sale exempt** if owned a full **2 years** and the seller's total residential holdings on the sale date are ≤**600 m³** (individual) / **1,200 m³** (couple); a home in the owners' own use is exempt regardless of volume (sales from 1 Jan 2016). Owned <2 years → gain fully taxable, with deferral over two year-ends or rollover into a replacement home's cost base (2026 data, source skatturinn.is Söluhagnaður)
- **Sumarbústaður / frístundahúsnæði** (cottage): gain tax-free (from income year 2020) only if owned ≥**7 years**, used by the owners and not let for payment, and cottage + residential holdings ≤600 m³ (individual) / 1,200 m³ (couple); otherwise taxable (2026 data, source skatturinn.is Söluhagnaður)
- Other property (commercial, land, lots, and residential volume above the limits when not in own use): 22% on the gain

### VAT (VSK) — Lög um virðisaukaskatt nr. 50/1988

- 24% standard
- 11% reduced (food, books, hotel / guest-room lets under one month, tourist services)
- **Sale of immovable property is EXEMPT from VSK** under Lög nr. 50/1988 — including new build (2026 data, source skatturinn.is Helstu tölur 2026 + Value Added Tax page). Developers reclaim input VSK via **Endurgreiðsla VSK** scheme — see below.
- Owner VAT-refund scheme: **35% refund of VSK on on-site labour** for new build, renovation and maintenance of residential housing via **Endurgreiðsla VSK**, claimable for 6 years — rate since 1 July 2023 (100% applied 1 Mar 2020–31 Aug 2022, 60% 1 Sep 2022–30 Jun 2023) (2026 data, source `https://island.is/endurgreidsla-vsk-vegna-ibudarhusnaedis` + skatturinn.is Helstu tölur 2026).

### Future risk

- **Stimpilgjald** stable
- **Fasteignamat** annual revision
- **Currency risk** — ISK volatile
- **Foreign-currency mortgages BANNED** post-2008 crisis

---

## Section: `--rental`

### Long-term residential

- **Húsaleigulög** (Tenancy Act): moderate protection
- **Tímabundinn leigusamningur** (fixed-term) common
- **Ótímabundinn leigusamningur** (open-ended) — termination notice 6 months for both landlord and tenant for flats (íbúðir); 12 months from the landlord where the landlord is a legal entity letting the flat commercially (í atvinnuskyni) and the tenant has rented it for more than 12 months; 3 months for single rooms; a non-profit landlord may give 3 months in the cases set out in art. 56(2) húsaleigulög (2026 data, source stjornarradid.is húsaleigumál — Uppsögn og riftun + Undanþágur fyrir lögaðila sem ekki eru reknir í hagnaðarskyni)
- Income tax on rental (individuals): letting of residential housing that falls under húsaleigulög, with no more than two flats let, is capital income (fjármagnstekjur) taxed at **22%** on **75%** of gross rent — the frítekjumark (tax-free share) fell from 50% to **25%** from income year 2026 — i.e. **16.5%** of gross rent (computed: 22% × 75%); no cost deductions except heating/electricity included in the registered lease, and island.is requires the lease to be registered in the national rental registry. Letting outside the exceptions is taxed as business income (atvinnurekstrartekjur) (2026 data, source skatturinn.is Leigutekjur + island.is/leigutekjur-af-husnaedi)
- **Leiga á móti leigu**: an owner who lets their own former home (under húsaleigulög) while renting another home for own use may deduct the rent paid from the rental income (rule in force since 1 Jan 2018) (2026 data, source skatturinn.is Leigutekjur)
- **Eignaskattfrelsi** for long-term tenants in primary owner residence (parts)

### Short-let (Airbnb / Heimagisting)

**Heimagisting (home accommodation registration) required nationally** under **Lög um veitingastaði, gististaði og skemmtanahald nr. 85/2007** (Heimagisting amendment effective 1 Jan 2017; scope narrowed by L. 25/2026, in force 9 Apr 2026) (2026-05-27 verified, source government.is + island.is):
- **National cap (NOT Reykjavík-specific)**: max **90 nights/year** AND **ISK 2,000,000 gross income/year** — whichever triggers first requires commercial licence (rekstrarleyfi) — inside þéttbýli (urban areas) open-ended (ótímabundin) licensed accommodation must be in approved commercial premises (rule inserted by L. 43/2024, in force 23 May 2024; limited to ótímabundin licences by L. 25/2026 art. 1a), while a rekstrarleyfi for accommodation in urban residential housing (íbúðarhúsnæði) is time-limited to five years at a time (L. 25/2026 art. 2); such licences valid on 1 Apr 2026 run to 1 Jan 2032 (L. 25/2026 art. 5 transitional provision) · **Scope narrowed by L. 25/2026 (in force 9 Apr 2026)**: heimagisting only at the owner's lögheimili (legal domicile) OR one other owned property OUTSIDE urban areas — a second urban flat can no longer be let under heimagisting; L. 82/2026 ch. IX (in force 1 Jan 2027) only replaces Act 85/2007's heilbrigðisnefnd references with Umhverfis- og orkustofnun and Stofnun atvinnuveganna, with no change to the heimagisting caps or scope (2026-10-21 verified, Stjórnartíðindi A nr. 82/2026) (2026 data, source Alþingi lagasafn 85/2007 útg. 157c + island.is/heimagisting)
- Beyond cap: requires **rekstrarleyfi** (operator licence) + accommodation services VSK
- Registration via **Sýslumaður** (district commissioner; island.is lists Sýslumaðurinn á höfuðborgarsvæðinu as the service provider); registration is valid to the end of the calendar year and must be renewed annually; registration fee **ISK 9,200** (2026 data, source island.is/heimagisting)
- Administrative fines (stjórnvaldssektir) up to **ISK 1,000,000** per violation for letting without registration or breaching the marketing rules; other sanctions include deregistration and refusal of registration the following year (2026 data, source island.is/heimagisting)
- **EU 2024/1028 STR**: not directly applicable in Iceland (not EU). EEA-Lex marks it EEA-relevant and under scrutiny by Iceland, Liechtenstein and Norway, with no EEA Joint Committee decision listed (2026 data, source `https://www.efta.int/eea-lex/32024R1028`).

### Tax on short-let

- Heimagisting income: capital income (fjármagnstekjur) taxed at 22% with no cost deductions, provided the letting is registered with Sýslumaður (skráningarnúmer) and total heimagisting rent is at most ISK 2,000,000 in the income year; above that, or if Sýslumaður cancels the registration, all the year's rent is taxed as business income (2026 data, source skatturinn.is Leigutekjur + island.is/heimagisting/skattar-og-gjold)
- License-required short-let: business income, VSK applies

---

## Section: `--work=<profession>`

### Sources

- **Vinnumálastofnun** (Directorate of Labour): `https://island.is/s/vinnumalastofnun` (vmst.is redirects here)
- **Alfred** job platform: `https://www.alfred.is/`
- **LinkedIn IS**, **Tvinna.is** (creative-sector jobs), **Mbl Atvinna**

### Self-employment

- **Einstaklingsrekstur** (sole proprietorship, run on the owner's kennitala; owner liable with all personal assets): no minimum capital
- **EHF.** (private limited): min share capital ISK 500,000
- **HF.** (public limited): min share capital ISK 4,000,000 (2026 data, source skatturinn.is Fyrirtækjaskrá + Stofna rekstur)
- **VSK registration** required once taxable sales exceed ISK 2,000,000 in a 12-month period (voluntary below; sellers of exempt goods/services only need not register) (2026 data, source skatturinn.is Skráning á VSK-skrá)
- **RSK (Skattur)** registration for tax

### Salary benchmarks (2025)

- Full-time employees, whole country — regluleg heildarlaun (regular pay + measured overtime): median **ISK 895,000/mo**, mean ISK 982,000, interquartile range ISK 728,000–1,110,000; heildarlaun (incl. irregular payments) median ISK 948,000 (2025 data, source Hagstofa VIN02004)
- Regional split (est. — VIN02004 publishes no regional breakdown; ranges calibrated against the national interquartile range above):
  - Reykjavík: ~ISK 800,000–1,100,000
  - Akureyri: ~ISK 700,000–950,000
  - Smaller towns: ~ISK 600,000–850,000
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

### Specific risks (one of the highest geological-hazard densities in Europe)

#### Volcanic + seismic — current activity

**Reykjanes peninsula 2023-2025 eruption series** (CRITICAL UPDATE):

- **9 eruptions since December 2023** on the Sundhnúkur crater row; no new eruption through 30 Sep 2026 (2026 data, source Veðurstofan news 5 Aug 2025 "The ninth eruption on the Sundhnúkur crater row has ended" + Svartsengi update 30 Sep 2026)
- **12 eruptions on the Reykjanes peninsula since 2021** = 3 in the Fagradalsfjall area 2021–2023 (Fagradalsfjall / Litli-Hrútur) + 9 on the Sundhnúkur crater row (computed from Veðurstofan's Reykjanes overview and its 5 Aug 2025 news; Visit Reykjanes, secondary, also counts the July 2025 eruption as "the twelfth" since 2021)
- **Most recent**: began 16 July 2025; crater activity stopped 4 August and Veðurstofan declared it over on 5 August 2025 (2025 data, source Veðurstofan)
- **Still active (Sep 2026)**: magma keeps accumulating under Svartsengi (≈ 29.1 million m³ by 18 Aug 2026, range 28.3–29.9); a new intrusion, possibly an eruption, on the Sundhnúkur crater row "remains the most likely scenario"; Reykjanes–Svartsengi system at alert level 2 (orange); Grindavík in the "considerable" and Svartsengi in the "moderate" hazard category; past warning times ≈ 20 minutes to just over 4 hours (2026 data, source Veðurstofan Svartsengi updates 18 Aug + 30 Sep 2026)
- **Grindavík evacuated 10 November 2023** (registered population 3,562 on 1 Jan 2023); registered population 819 on 1 Jan 2026 (registered domicile, not physical presence); in an Oct 2026 survey of pre-evacuation adult residents 15.3% lived in the town vs ~10% at the start of 2026; the town remains at civil-protection óvissustig (2026 data, sources Hagstofa MAN02005 + grindavik.is 16 Oct 2026)
- Volcanic dykes have penetrated protective barriers
- **"New Reykjanes Fires"** — volcanologists suggest a multi-century active period (parallel to 13th century)
- **Property risk in Reykjanes**:
  - **Grindavík properties**: state buyback via **Fasteignafélagið Þórkatla** under Act 16/2024 — 961 properties purchased, 969 applications since March 2024; Þórkatla's re-sale (endurkaup) plan awaits law changes; a new risk assessment for people's safety in Grindavík is on the municipality's website (2026 data, sources torkatla.is + grindavik.is 16 Oct 2026 + Veðurstofan news 1 Oct 2026)
  - **Reykjanesbær (Keflavík area)**: some risk, monitored
  - **Greater Reykjavík (40km north)**: indirect risk via gas, ash
- **Authority monitoring**: `https://www.vedur.is/skjalftar-og-eldgos/` (live)

#### Other volcanic zones

- **Hekla** — overdue (last eruption 2000)
- **Katla** — major dangerous; subglacial; jökulhlaup risk
- **Bárðarbunga** — major; Holuhraun 2014-15 longest in 230 yrs
- **Grímsvötn** — under Vatnajökull; jökulhlaup chronic
- **Öræfajökull** — historic catastrophe (1362)

#### Seismic

- Iceland sits on **Mid-Atlantic Ridge** — ~2,000–5,500 quakes/month recorded nationwide in 2026 (≈ 65–185/day computed: 2,000 ÷ 31, 5,500 ÷ 30), mostly small; Sep 2026 ≈ 2,500, of which 600+ on Reykjanesskagi (2026 data, source Veðurstofan monthly jarðskjálftayfirlit)
- **Suðurlandsskjálftar** (South Iceland zone): historic M 6.0+ events
- **Reykjanesskagi**: active swarm zone (current)
- **Tjörnesbeltið** (north): also active
- Eurocode 8 with Icelandic annex applies

#### Other geological hazards

- **Hraunrennsli** (lava flow) — direct property destruction risk
- **Jökulhlaup** (glacial outburst flood) — Skeiðará, Markarfljót, Súla — catastrophic
- **Snjóflóð** (avalanche): Westfjords + East fjords known fatal events
  - **Flateyri 1995** (20 dead), **Súðavík 1995** (14 dead) — 34 deaths combined per Veðurstofan, which counts 193 avalanche + landslide deaths in the 20th century; **Neskaupstaður 1974** (source Veðurstofan ofanflóð hættumat page)
- **Skriðuhætta** (landslide): Westfjords + Northern Iceland
  - **Seyðisfjörður 2020** mudslide
- **Strandrof** (coastal erosion) + sea-level rise
- **Stormflóð** (storm surge) — winter storms catastrophic
- **Veðuröfgar** (extreme weather) — winds 50+ m/s recorded

### Insurance via Náttúruhamfaratryggingar (NTÍ)

**MANDATORY natural disaster insurance** — automatic via property insurance:
- Covers: volcanic eruptions, earthquakes, landslides, avalanches, water floods (vatnsflóð) — NOT meltwater / rapid-thaw / cloudburst floods, storm or wind damage, snow-load damage (2026 data, source island.is NTÍ damage page)
- All buildings and contents fire-insured with an Icelandic-licensed insurer are covered; the premium is collected with the fire-insurance premium (2026 data, source island.is/en/o/nti)
- **Deductible (eigin áhætta)**: minimum ISK 400,000 per building, ISK 200,000 on contents / movables; report damage within 1 year of becoming aware of it (2026 data, source island.is NTÍ damage page)
- Payout based on rebuild value
- **NTÍ provides compulsory, broad natural-hazard cover bundled into property insurance** (volcano, earthquake, flood, avalanche, landslide)
- For Grindavík: state purchase via Þórkatla (Act 16/2024; 961 properties purchased — 2026 data, source torkatla.is) + NTÍ payouts for natural-hazard damage

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960** | Low seismic standards |
| **1960s onwards** | Gradually improved |
| **Post-2002** | ÍST EN 1998 seismic design |
| **Post-2010** | Modern energy + seismic |
| **Concrete + steel reinforcement** dominant |
| **Wood common in older buildings** | Fire risk |
| **Asbestos**: pre-1980s likely; banned 1990s |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Söluyfirlýsing** | Sale declaration of seller's known defects | At sale |
| **Fasteignamat** | Current valuation (HMS); base for fasteignagjöld, stamp duty and inheritance tax | Annual — owners notified in June, takes effect 31 Dec for the following year (2026 data, source island.is/fasteignamat) |
| **Veðbókarvottorð** (encumbrance certificate) | Title verification | At sale |
| **Energy performance certificate** | **Not required in Iceland** — EEA Joint Committee Decisions 135/2022 and 175/2025 exempt Iceland from the EPBD (temporary, until the 2024/1275 recast is incorporated); Iceland's declaration to JCD 175/2025 says it "has not implemented any previous versions of the EU energy performance in buildings acquis" (2025 data; JCD 175/2025 entry into force still pending in 2026, source EFTA EEA-Lex) | n/a |
| **Brunabótamat** (insurance valuation) | All buildings must be fire-insured; insured sum based on brunabótamat (rebuild cost less depreciation; excludes contents) | Recalculated at end of May each year, indexed monthly to the building-cost index; reassessment on request after renovation (2026 data, source island.is/brunabotamat) |

### Climate change projections (Veðurstofan)

- Warming 2091–2100 vs 1986–2005: **1.5–2.4 °C** in lower-emission scenarios, **> 4 °C** if emissions stay high; 2046–2055: 1.3–2.3 °C (2018 data, source Veðurstofan vísindanefnd report "Loftslagsbreytingar og áhrif þeirra á Íslandi" — rates/figures may have changed since)
- Sea-level rise is **coast-specific, not national**: rise near Iceland ≈ 30–40% of the global mean; relative sea level falls in the south-east (land uplift) but can rise by tens of cm where land subsides (west coast, central north coast) — check the property's coastal segment (2018 data, same source — rates/figures may have changed since)
- Glacier retreat: significant (Jökulsárlón growing) — glacier area down ≈ 2,000 km² since the late-19th-century maximum; Langjökull could lose 85% of its volume by 2100 (2018 data, same source — rates/figures may have changed since)
- Increased precipitation: ≥ 1.5% per °C of warming, up to 4.5% in some models (2018 data, same source — rates/figures may have changed since)
- Possible decline in ocean cooling effect

---

## Section: `--mains`

### Sources

- **Veitur** (capital-area utility: hot water, cold water, sewer, electricity distribution; tariffs at `https://www.veitur.is/verdskrar`): `https://www.veitur.is/`
- Per-sveitarfélag water utilities elsewhere
- **Hitaveita** (district heating co-operatives) per region

### Verification

- **Geothermal hot water (jarðhiti)** heats ~90% of the population — UNIQUE (Orkustofnun: jarðhiti "sér 90% landsmanna fyrir ... húshitun"; undated post-2022 article — rates/figures may have changed since)
  - Cheap energy, almost universal in populated areas
  - The other ~10% rely on electric heating, partly state-subsidised (same source); some Westfjords + East fjord settlements among them
- **Cold water** + **sewer** typically per municipality
- **Rotþrær / fráveitukerfi**: rural cottages on individual systems

### Costs

| Scenario | Cost (ISK) |
|---|---:|
| Hitaveita connection — Veitur area, urban heimæð < 50 m, 20–32 mm steel (25–40 mm PEX), incl. 11% VSK | 466,855–1,195,146 (Veitur tariff in force from 1 Dec 2025); rural lögbýli / year-round house, heimæð < 70 m: 675,411–1,729,044 |
| Cold water + sewer connection — Veitur area: cold water 32–40 mm (VAT-exempt) + sewer for a new-area plot in Reykjavík / Akranes / Borgarbyggð | ≈ 996,204–1,163,524 computed (cold water 389,962–557,282, tariff from 1 Oct 2026, + sewer 606,242 per plot, tariff from 1 Jan 2026); infill plots pay actual cost |
| Mains-line extension | est. 5,000,000–15,000,000+ |

> Connection rows are Veitur tariffs (2026 data, source veitur.is/verdskrar); cold-water and sewer fees are indexed to the building-cost index, so amounts drift. Other hitaveitur and municipal water/sewer utilities set their own tariffs — check the local one. The mains-line extension row is an indicative contractor range (est.), not from a published index — get quotes.

---

## Cost benchmarks (IS 2026)

| Work | Cost (ISK) |
|---|---:|
| Stimpilgjald | 0.8% of fasteignamat (0.4% FTB; 1.6% legal entity) |
| Þinglýsingargjald | 3,800 per document |
| Fasteignasalalaun | est. 1–2% of price (seller) |
| **Total transaction cost (buyer)** | **0.8% of fasteignamat + 3,800 per document** (0.4% FTB) |
| Söluyfirlýsing | est. 30,000–80,000 |
| Energy upgrade | est. 4,000,000–12,000,000 |
| Antiseismic retrofit | est. 3,000,000–8,000,000 |
| Roof (corrugated steel, 150 m²) | est. 2,000,000–4,000,000 |
| Asbestos abatement | est. 800,000–3,000,000 |
| Hitaveita connection | est. 1,000,000–3,000,000 |

> Construction/retrofit rows and the söluyfirlýsing row are indicative ranges (est.), not from a published index — get quotes. Stimpilgjald and þinglýsingargjald are sourced (island.is Þinglýsing skjala, 2026 data); the total is computed from them; fasteignasalalaun is a negotiable est.

## Active fiscal incentives (2025-2026)

- **Endurgreiðsla VSK** (35% VAT refund on on-site labour): for new build, renovation, maintenance of residential housing (2026 data, source island.is)
- **Séreignarsparnaður — fyrsta íbúð** (Lög nr. 111/2016): a first-time buyer (never registered owner of more than 30% of residential property in Iceland) holding ≥30% of the property may use voluntary pension savings tax-free toward the purchase or the mortgage, max **ISK 500,000/yr per person** for 10 consecutive years (ISK 5,000,000 total); apply within 12 months of signing the purchase contract. Someone who has owned no residential property (and was not jointly taxed with an owner) for 5 years also qualifies, but only if their combined income and capital-income tax base in the income year before the purchase does not exceed the third-bracket threshold (ISK 15,901,523 for income year 2025) (2026 data, source skatturinn.is Fyrsta íbúð)
- **Séreignarsparnaður inn á húsnæðislán** (any owner-occupier with ≥30% share, lögheimili in the home and a mortgage on it): up to **ISK 500,000** per person in 2026 paid tax-free into the mortgage, for up to 10 years in total (2026 data, source skatturinn.is Ráðstöfun inn á húsnæðislán)
- **Hlutdeildarlán** (HMS shared-equity loan): first-time buyer (or no home owned for 5 years) with a 5% down payment, HMS-approved flat, income ≤ISK 10,000,000 (single) / 15,000,000 (couple) over the last 12 months (+ISK 2,254,000 per child under 20) → loan of up to **25%** of the price (35% under lower income caps); no interest or instalments, the amount tracks the property's value and is repaid on sale or after 10 years (extendable to 25) (2026 data, source island.is Hlutdeildarlán)
- **Húsnæðisbætur** (HMS): monthly benefit for renters, means-tested on household size, income, assets and rent; **sérstakur húsnæðisstuðningur** on top from the municipality (2026 data, source island.is Húsnæðisbætur)
- **Vaxtabætur** (mortgage interest credit, owner-occupied home loans only, requires unlimited tax liability or tax domicile in Iceland): max **ISK 420,000** (single) / **525,000** (single parent) / **630,000** (couple) in the 2026 assessment for 2025 interest; cut by 8.5% of the income base, reduced above net wealth of ISK 7,500,000 / 12,000,000 and lost at ISK 12,000,000 / 19,200,000 (2026 data, source island.is Fjárhæðir vaxtabóta)

## Common listing platforms

- **Mbl.is fasteignir** — biggest
- **Fasteignir.is** (Vísir / Sýn) — `https://fasteignir.visir.is/`
- **Remax IS, Eignamiðlun, Fasteignamarkaðurinn, Domus, Brynja, Gimli** — agency networks

## Caveats unique to IS

- **VOLCANIC + SEISMIC RISK IS REAL AND ACTIVE**:
  - Reykjanes 2023-2025 series destroyed homes in Grindavík
  - **9 eruptions since Dec 2023** at Sundhnúkur
  - **"New Reykjanes Fires"** potentially multi-century period
  - Property in Reykjanes peninsula carries elevated risk
- **Mandatory natural-hazard insurance (NTÍ)** is automatic via property insurance — major buyer protection
- **Geothermal heating** universal in populated areas — extremely cheap energy, but check connection
- **Currency volatility** — ISK can swing 20–30% vs EUR
- **Foreign-currency mortgages BANNED** post-2008 crisis
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

✅ **Fully populated** as of 2026-04-25. Rental tracker entries re-checked 2026-09-24 in the October regwatch wave (see shared/regulatory-watch.md). Rental tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks (incl. live volcanic eruption series), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for country profile, `--traffic`, the foreign-buyer rules and the verification authorities (re-verified 2026-10-23 against Hagstofa, cb.is, EFTA EEA-Lex, Vegagerðin, government.is and skatturinn.is — see the per-section table). HIGH for the individual facts refreshed 2026-10-23 that carry an inline primary source: statutory tax rates and fees (skatturinn.is, island.is, samband.is, reykjavik.is), heimagisting caps, notice periods and rental-income tax (island.is, skatturinn.is), the Reykjanes eruption count, Grindavík buyback and NTÍ cover (Veðurstofan, torkatla.is, island.is), national wages and company capital (Hagstofa, skatturinn.is), Veitur connection tariffs and the Central Bank key rate (cb.is). `--price`, `--tax`, `--rental`, `--work`, `--risks` and `--mains` are not re-stamped: each still holds lines that could not be re-checked, so they keep the 2026-04-25 date. MEDIUM for the 2025 ISK/m² price table (HMS not reachable for re-check; only a Hagstofa index re-anchor to Sep 2026 was added), the fasteignamat-to-market ratio, the listing-platform and agency lines, the build-era table, the "New Reykjanes Fires" framing and the other hazard descriptions not re-checked, and the foreign-currency-mortgage ban. Est. only (no published index) for the broker fee, söluyfirlýsing, construction / retrofit and mains-extension ranges and the regional salary split. MEDIUM for currency-related advisories (ISK volatile).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | Postcodes, 8 landshlutar and EEA (not EU) status confirmed; municipalities 64 → 62 and EUR/ISK updated (Hagstofa, cb.is, EFTA EEA-Lex); HMS cadastre role not re-fetched |
| `--traffic` | 2026-10-23 | 2026-10-23 refresh wave | Vegagerðin URLs and ÁDU definition confirmed; verdict bands calibrated on Vegagerðin 2025 ÁDU key-counter tables |
| Foreign-buyer rules (Caveats) | 2026-10-23 | 2026-10-23 refresh wave | Act 19/1966 permit rules (government.is, Ministry of Justice) and Jarðalög 81/2004 art. 10 b reporting duty (skatturinn.is) |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | RSK renamed Skatturinn; Veðurstofan role extended; NTÍ and Þórkatla / Grindavíkurbær rows added |

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
  - Not re-stamped: `--price`, `--tax`, `--rental`, `--work`, `--risks` and `--mains` each keep unverified lines, so the playbook-level date stays 2026-04-25.
