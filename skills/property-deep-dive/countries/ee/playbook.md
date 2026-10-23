# Estonia 🇪🇪 — Property Due-Diligence Playbook

ISO2: `ee`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`10115` Tallinn central, `50050` Tartu, `80010` Pärnu)
- **Admin levels**: 15 maakond (counties) + 78 omavalitsus (municipalities: 15 linna + 63 valda; 79 until Jõhvi vald and Toila vald merged at the Oct 2025 local elections) (2026 data, source Regionaal- ja Põllumajandusministeerium agri.ee)
- **Currency**: **EUR (€)** — adopted 1 Jan 2011
- **Languages**: Estonian (official); Russian minority (Northeast); English widely used in business
- **Cadastre**: **Maa- ja Ruumiamet** (MaRu, Land and Spatial Development Board — successor to Maa-amet from 1 Jan 2025) + **e-Kinnistusraamat** (RIK e-Land Register)
  - Geoportaal: `https://geoportaal.maaruum.ee/eng/services/cadastral-register-query-p302.html` (old geoportaal.maaamet.ee links redirect here, checked 2026-10-23)
  - e-Land Register: `https://www.rik.ee/en/e-land-register/e-land-register-portal`
- **Identifier**: `kinnistu number` (registered immovable number) + cadastral parcel code
- **Ownership types**:
  - **Kinnisasja omandi** (full ownership)
  - **Hoonestusõigus** (right of superficies)
  - **Korteri-omand** (apartment ownership with land share)
- **e-Notar**: remote notarisation by video call (kaugtõestamine) — parties may be at home or abroad; property transactions and mortgages can be done remotely by agreement with the notary, marriage and divorce cannot (source Notarite Koda notar.ee); identity check uses Veriff biometric facial recognition against the ID-document photo — e-Estonia called it the first state service of its kind in **Europe** (e-Estonia, 17 Nov 2021)
- **EU member since 2004 + eurozone since 2011**

## Section: `--price`

### Primary sources

- **Statistikaamet (Statistics Estonia)**: `https://stat.ee/en/` — official housing price + transactions
- **Maa- ja Ruumiamet (MaRu) transaction statistics**: `https://statistika.kataster.ee/kinnisvara/` — free aggregate deal counts + price levels by region / property type / period, with a statistics API (opened 15 Oct 2026, replacing the old price-statistics query). Individual transactions are NOT published: access to per-transaction data is restricted by law (Maakatastriseadus § 6 — appraisers, credit institutions, others on legitimate interest) (source maaruum.ee, 2026-10-15)
- **e-Kinnistusraamat (RIK)**: `https://www.rik.ee/en/e-land-register/e-land-register-portal` — title + owner (with eID)
- **Eesti Pank** (central bank) housing market reports

### Listing platforms

- **KV.ee** — DOMINANT: market leader by time on site (Baltic Classifieds Group / Similarweb, April 2026): `https://www.kv.ee/en/`
- **City24.ee** — No.2 in Estonia (also Baltic Classifieds Group, BCG): `https://www.city24.ee/`
- **Maa365.ee** — ❌ DEPRECATED — dead on 2026-10-23 (domain not found in the .ee registry WHOIS); verify land-market levels with Maa- ja Ruumiamet transaction statistics (forest / arable / unbuilt-land categories)
- Agency networks: **Pindi Kinnisvara**, **Domus Kinnisvara**, **Uus Maa**

### 2026 apartment price benchmarks (Maa- ja Ruumiamet transaction data)

| Region | Avg €/m² (apt secondary) | Avg €/m² (apt primary/new) |
|---|---:|---:|
| **Tallinn (city)** | 2,997 (+4.3% YoY) | 4,635 (+1.1% YoY) |
| **Tallinn Kesklinn (2-room, 40–55 m²)** | 3,734 | 5,005 |
| **Tartu linn (2-room, 40–55 m²)** | 2,518 | 3,595 |
| **Pärnu linn (2-room, 40–55 m²)** | 2,254 | 3,031 |
| **Narva linn** | median 402 (all apt sales; −4.9% YoY, computed) | — |
| **Kuressaare linn (Saaremaa vald)** | median 1,601 (all apt sales; +1.5% YoY, computed) | — |
| **Tartu maakond outside cities** | median 2,519 (all apt sales incl. suburban new builds; +9.9% YoY, computed) | — |

Rows 1–4: free-market apartment (eluruum) sales in Q2 2026, YoY vs Q2 2025 (2026 data, source Maa- ja Ruumiamet, "Kinnisvaraturg ja hinnaindeks 2026. aasta II kvartalis"). Rows 5–7: median unit price of all apartment transactions — new + secondary combined, not free-market-filtered — Oct 2025–Sep 2026 vs Oct 2024–Sep 2025; municipality / town level (rows 5–6) and MaRu's "all counties excl. cities" grouping (row 7), never parcel-level (2026 data, source MaRu statistics query statistika.kataster.ee, retrieved 2026-10-23 — recent months may still be revised).

### Compute

1. €/m² = price / **kasulik pind** (usable area)
2. Cross-check **MaRu transaction statistics** (free, aggregate only — no individual deals) + **KV.ee asking prices** (seller-controlled)
3. **Tallinn districts vary** (2-room 40–55 m² apartments, Q2 2026): secondary from €2,571/m² (Lasnamäe) and €2,693/m² (Mustamäe) to €3,734/m² (Kesklinn); new builds from €4,131/m² (Haabersti) to €5,005/m² (Kesklinn), €5,171/m² (Kristiine) and €5,399/m² (Põhja-Tallinn) (2026 data, source Maa- ja Ruumiamet Q2 2026 review)
4. **2026 market flat**: MaRu apartment price index unchanged YoY in Q2 2026 (−2.2% QoQ); all-apartment medians Oct 2025–Sep 2026 vs a year earlier: Tallinn €2,920/m² (+2.4%), Tartu linn €2,465/m² (+2.0%), Pärnu linn €2,001/m² (−2.2%) (computed from MaRu statistics query, retrieved 2026-10-23)

### Key terms

- Kinnistu = registered immovable
- Korteriomand = apartment ownership
- Korteriühistu = apartment association (HOA)
- Maamaks = land tax
- Energiamärgis = energy certificate

---

## Section: `--traffic`

### Sources

- **Transpordiamet (Estonian Transport Administration)**: `https://www.transpordiamet.ee/` — formed 1 Jan 2021 as legal successor of Maanteeamet, Lennuamet and Veeteede Amet (source transpordiamet.ee)
- **Liiklusloendus** (traffic counts) — previous year's results published annually in Q1 (2025 report ERC/01/2026 dated 21 Mar 2026; 118 permanent + 23 periodic stationary count points at 31 Dec 2025, plus 7-day short-term counts at 1,030 points in 2025): `https://www.transpordiamet.ee/liiklussageduse-statistika`; map `https://www.transpordiamet.ee/liiklussagedus` (2025 data, source Transpordiamet liiklusloendus 2025 report)
- Noise map (**Mürakaart**, Maa- ja Ruumiamet geoportal): road / rail / tram / air + industrial noise, Lden + Lnight; latest strategic round 2022 (2020–2021 data): `https://xgis.maaamet.ee/xgis2/page/app/myrakaart` (source geoportaal.maaruum.ee noise-map description)
- Estonian data gateway (**Andmete teabevärav**, created 2025 from the former open-data gateway — RIA): `https://andmed.eesti.ee/` (old `avaandmed.eesti.ee` redirects here)

### Key term

**AKÖL (aasta keskmine ööpäevane liiklussagedus)** = AADT — Transpordiamet's term (2025 count report keywords: "AKÖL" / "AADT").

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban arterial)
- 🟠 10,000–25,000 v/d (Tallinn arterials; T1 / T2 beyond the Tallinn fringe — e.g. T1 km 13.9–26.5 = 20,298, T2 Kose-Risti km 44.3 = 12,026)
- 🔴 > 25,000 v/d (Pärnu mnt, Narva mnt, ring road). State-road peaks: T1 Tallinn–Narva km 10.5–11.2 = 50,458 (2025 national maximum, modelled), T11 ring road km 11.1–15.1 = 31,921, T1 km 11.2–13.9 = 31,395, T2 km 5.7–8.5 = 30,880, T4 Laagri km 13.0 = 28,213. Pärnu mnt / Narva mnt inside Tallinn are city streets outside the state-road count — verify with Tallinn city

Calibration (2025 data, source Transpordiamet liiklusloendus 2025 + Lisa 5): weighted AKÖL on all state roads 1,136 v/d (+4.4 % YoY); main roads 6,181, basic roads 1,746, secondary roads 371; ~76 % of secondary-road sections carry ≤ 500 v/d (computed: 2,387 of 3,157 sections in Lisa 5).

---

## Section: `--tax`

### Annual property tax — Maamaks (LAND ONLY — UNIQUE)

**Estonia has NO annual property tax on buildings — only on LAND.**

#### Maamaks reform 2024-2026

- **2024**: max +10% increase per cadastral unit, or +€5 floor
- **2025**: max +50% increase or +€20 floor
- **2026**: limit set by **each local government** at 10–100%; €5 floor; **homeowner relief €0–1,000** per property (amount-based, also municipality-set; replaces the 2025 area-based exemption of up to 0.15 ha in densely populated areas) (2026 data, source [EMTA — Land tax](https://www.emta.ee/en/private-client/taxes-and-payment/other-taxes/land-tax); 2024 +10 %/€5 and 2025 +50 %/€20 caps confirmed on the same page)
- **2027**: same mechanism — each council sets the cap by 1 Oct of the preceding year (Maamaksuseadus § 8¹); e.g. Tartu 50 % cap + homeowner relief up to €850 (city regulations nos. 17 and 16 of 18 Jun 2026), Pärnu homeowner relief €1,000 (2027 data, sources tartu.ee + parnu.ee)

#### Rate ranges (set per municipality; 2026 data, source EMTA land-tax page)

| Land type | Rate range |
|---|---|
| Residential / yard land | 0.1–1% |
| Profit-yielding land | 0.1–0.5% |
| Other land | 0.1–2% |

#### Typical bills

- Tallinn 100m² apt with land share: **~€100–€500/yr** before relief (est. — Tallinn applies 0.5 % on residential land × assessed land value with a 10 % annual cap; a registered-resident owner pays only the part above Tallinn's homeowner relief of up to €1,000 per property — 2026 data, source tallinn.ee; confirm on the EMTA maamaks notice)
- Tartu single-family with 1,000m² plot: **~€200–€600/yr** (est.)
- Pärnu coastal villa with 2,000m² plot: **~€500–€1,500/yr** (est.)

### Transaction taxes

- **NO transfer tax** (UNIQUE in EU) — no real-property transfer tax and no tax on building value (2025 data, sources IMF Selected Issues Paper 2025/102 + PwC Worldwide Tax Summaries — secondary)
- **Notary fee (notari tasu)**: statutory and identical at every notary — a two-party sale costs **2 × the full fee** from the Notari tasu seadus § 22 value table **+ 24 % VAT**. Computed: €50k → 2 × €83.70 = €167.40 + VAT = **€207.58**; €100k → **€397.79**; €150k → **€588.01**; €200k → **€778.22**; €300k → **€1,134.85**. Incl. VAT the fee stays under €500 only up to a ~€128k transaction value. Who pays is agreed between the parties (2026 data, sources [Notarite Koda — fee calculation](https://www.notar.ee/ametitoimingud/notari-tasu-arvestamine) worked example + NotTS § 22–23 table via the [estlex.ee mirror](https://estlex.ee/oigusakt/notari-tasu-seadus/para-22), redaction in force 7 Feb 2026)
- **Notary fee schedule changing**: the Riigikogu passed bill **941 SE** (Notary Fees Act amendments) on **21 Oct 2026** (67 for, 1 against) — it updates fees unchanged for years, with the largest changes to company and real-estate fees, and abolishes the remote-authentication fee (source [riigikogu.ee press release, 21 Oct 2026](https://www.riigikogu.ee/pressiteated/jargmise-aasta-riigieelarve-eelnou-labis-esimese-lugemise-2)). Per Eesti Kaubandus-Tööstuskoda (22 Oct 2026, secondary) it enters into force **1 Jan 2027** and raises the minimum transaction value for immovables from €6,391 to **€10,000**. The adopted real-estate fee table is not yet published in Riigi Teataja (the initial text's memorandum showed e.g. a €140 full fee at €50k vs €83.70 now — initial text, secondary mirror, LOW); the computed fees above are the pre-2027 table
- **Land Register state fee (riigilõiv, owner entry)**: full rate from the Riigilõivuseadus value table, no VAT; 50 % for a spouse or direct-line relative (RLS § 76): €50k → **€53**; €100k → **€110**; €150k → **€175**; €200k → **€235**; €300k → **€350**; above €639,120 0.16 % of value, max **€2,560** (source [RIK state-fee guide](https://www.rik.ee/sites/default/files/2024-05/Riigiloiv_juhend.pdf) table, PDF dated 2022; the €100k / €150k values match a secondary calculator checked against Riigi Teataja on 14 Oct 2026, hüpoteek.ee)
- **e-Notar remote authentication (kaugtõestamine)**: same fee scale **+ €20** surcharge (NotTS § 2(2¹), in force 1 Feb 2020; source legalwise.ee NotTS mirror); abolished by 941 SE (see above)

### VAT (käibemaks)

- **20 % → 22 %** on 1 Jan 2024 (applied until 30 Jun 2025)
- **24 % standard from 1 July 2025** (Security Tax Act; raised from 22 %; made **open-ended** when the Riigikogu passed bill 645 SE on **18 Jun 2025** — VAT will NOT revert to 22 % from 2029) — Käibemaksuseadus (KMS). (2026 data, sources [EMTA — Käibemaks](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks) + [Rahandusministeerium, 18 Jun 2025](https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused))
- **Accommodation-services reduced VAT** (hotel-classified short-let): **9 % → 13 % from 1 Jan 2025** (separate from standard rate; applies where the host provides hotel-like services) (2025 data, source EMTA VAT page)
- New builds (sold before first use, or — since 1 Jan 2025 — first sold within 1 year after first use), significantly improved buildings (improvement costs ≥ 10 % of the prior acquisition cost; same timing rule) + building land (ehitusmaa): **24 % VAT applies** (KMS § 16(2)(3); 2025 data, source EMTA VAT handbook, updated 8 Jan 2025)
- Resale: generally **VAT-exempt** (same source)

### Capital gains — Tulumaks (Tulumaksuseadus)

- **Tulumaks 22 % from 1 Jan 2025 and still 22 % in 2026** (EMTA tax-rates page, 2026 block: "The rate of withheld income tax is 22%"; corporate distributed profit 22/78; CGT integrated into general Tulumaks). (2026 data, source [EMTA — Tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))
- **Primary residence exempt** if the dwelling was the seller's residence until the sale — no minimum ownership period, but usable for **one disposal per 2 years** (TuMS § 15(5)(1) + (6)); a summer house / garden house is exempt if owned > 2 years on a plot ≤ 0.25 ha (§ 15(5)(4)) (2026 data, source EMTA income-tax handbook — Kinnisvara võõrandamine, updated 27 Jun 2026)

### Total transaction cost (buyer side)

- Resale primary: **~0.5 %** of price without a mortgage — computed, buyer paying the full notary fee + owner-entry state fee: €100k → €397.79 + €110 = **€507.79 (0.51 %)**; €300k → €1,134.85 + €350 = **€1,484.85 (0.49 %)** (pre-2027 tables, see above). A hypothec signed in the same deed adds its own notary + state fees (secondary calculator example: €150k purchase + €180k hypothec → €1,092.02 ≈ 0.73 %, hüpoteek.ee)
- New build: 24 % VAT included in the developer's price + the same notary / state fees (~0.5 %, computed above)

### Future risk

- **Maamaks**: councils may set the annual increase cap anywhere up to 100 % — ERR News (secondary, citing EMTA-published 2027 rates) reports 100 % caps in Kohtla-Järve, Ruhnu and Tori and 50 % in Tartu for 2027. The **2026 regular land valuation** results are published by 31 Oct 2026 and are used for land tax **from 1 Jan 2028** (source Maa- ja Ruumiamet, 14 Aug 2026)
- **VAT**: standard rate 24 %, open-ended. Pending in Oct 2026: the 2027 State Budget bill (**1037 SE**, submitted 29 Sep 2026, first reading passed 21 Oct 2026) and the government VAT Act bill **992 SE** (initiated 14 Sep 2026, at second reading; its Riigikogu summary covers EU OSS extension and platform-service place-of-supply rules, no rate change) (sources riigikogu.ee, Sep–Oct 2026)
- E-government efficiency continues — record-time transactions

---

## Section: `--rental`

### Long-term residential

- **Võlaõigusseadus § 271 ff** (Law of Obligations Act § 271+) governs lease
- **Tenant protection moderate** (less strict than DE/AT)
- **Indekseerimine** (periodic, e.g. CPI-linked, rent increase): valid in a dwelling lease only if the term is ≥3 years, the rent rises at most once a year and the increase or its calculation basis is precisely set (VÕS § 300, source Riigi Teataja)

### Short-let

**EU Reg (EU) 2024/1028** (STR data-collection) applies EU-wide **from 20 May 2026** (Art. 19) — harmonising registration-number rules wherever a Member State runs a registration procedure (Art. 4(1)) + platform data-transmission/verification obligations that attach only where such a procedure exists (a Member State requiring platform data must run one, Art. 4(2); only such a Member State sets up a single digital entry point, Art. 10(1)); it does **not** harmonise substantive limits (local night-caps stay national). (2026-10-23, source EUR-Lex Reg (EU) 2024/1028 Art. 4, 10, 19). Estonia runs no such registration procedure — the current Tourism Act does not single out short-term rental and MKM's 18 Jun 2026 VTK proposes no STR register (sources ERR, mkm.ee 2026-06-18).

Estonia has **NO national mandatory STR-registration regime** in force. The Ministry of Economic Affairs (**MKM**) put a Tourism Act amendment VTK (legislative intent) out for consultation on 18 Jun 2026: short, repeated, paid letting of a dwelling, incl. via platforms, could be treated as an accommodation service, and the VTK does **not** propose an STR register in the near term (cost); feedback by 1 Sep 2026, bill to be drafted during 2026 (source mkm.ee 2026-06-18). ERR reports entry into force targeted **2027-2028** and the draft going to inter-ministerial coordination in Q4 2026 (ERR 2026-06-25 and ~2026-09-03, secondary); market participants want a nationwide accommodation database "but the Ministry of Economic Affairs and Communications is not listening" (ERR opinion, 2026-02) — i.e. no such requirement exists yet. In Sep 2026 MKM said it sees **no need for new national STR limits** despite a European Commission proposal letting local governments restrict short-term rentals; the government is still developing its position (source ERR News 2026-09-13, secondary — verify with MKM).

- **Tulumaks** (income tax) 22 % on rental earnings (2025 and 2026 — EMTA tax-rates page) (Tulumaksuseadus); short-term letting via Airbnb / Booking.com is declared as "other rental income" and taxed on the gross amount — the 20 % residential-lease deduction does not apply (source EMTA income-tax-return guidance for 2025)
- **VAT registration required once Estonian turnover exceeds €40,000 in a calendar year** (2026 data, source EMTA); short-let accommodation (ajutise ööbimisvõimaluse pakkumine, TurS § 17(2)) is taxable, not exempt letting, and is charged at the **13 % accommodation rate** (since 1 Jan 2025), not the 24 % standard rate; since 2025 exempt residential rent also counts toward the threshold once there is any taxable turnover (source EMTA VAT handbook + threshold page, updated 05.02.2026)
- **No Tallinn citywide night-cap** as of early 2026; the **Old Town (Vanalinn) development plan 2035** was adopted by the Tallinn city government on 17 Jun 2025 (regulation no. 29, Riigi Teataja 421062025017) and aims to cut guest-apartment numbers, but it sets no binding cap and the mechanism is not defined (source ERR, Riigi Teataja)
- Guest-registration to **Politsei- ja Piirivalveamet (PPA)** within 24h — *unverified for Estonia* (guest data historically routes to Statistikaamet, not PPA; verify with PPA before relying); the Interior Ministry wants the accommodation guest-registration duty extended, with data shared with security authorities on request (ERR ~2026-09-03, secondary)

### Tax on rental

- Residential lease (VÕS dwelling lease) by a private individual: 22 % income tax on 80 % of the rent — the flat 20 % expense deduction (TuMS § 39¹) is applied automatically in the return and the individual makes no further deduction ("füüsiline isik ise ei tohi üüritulust mahaarvamist teha") (source EMTA rental-income page, updated 05.12.2025)
- Short-let / sub-letting: no 20 % deduction — taxed on the gross amount (source EMTA)
- **Housing-loan (mortgage) interest NOT deductible** for individuals from 1 Jan 2024 — tax year 2023 was the last (source EMTA, updated 10.02.2025)

---

## Section: `--work=<profession>`

### Sources

- **Töötukassa (Estonian Unemployment Insurance Fund)**: `https://www.tootukassa.ee/`
- **CV.ee** (CV-Online; cvonline.ee redirects there) + **CV Keskus** (`https://www.cvkeskus.ee/`) — the most popular job portals per EURES Estonia (eures.ee, Töötukassa); **Work in Estonia** (`https://workinestonia.com`) for English-language offers; LinkedIn
- **Riigi Tugiteenuste Keskus** for state jobs

### Self-employment

- **FIE (Füüsilisest isikust ettevõtja)** = sole trader
- **OÜ (Osaühing)** = limited; **no €2,500 minimum since 1 Feb 2023** — share capital from **€0.01 per shareholder**, paid in on formation (2026 data, source e-resident.gov.ee; 1 Feb 2023 Commercial Code change per Grant Thornton Estonia, secondary); corporate income tax only on distributed profit (22/78 in 2026, source EMTA)
- **Käibemaksu** registration: once turnover from the start of the calendar year exceeds €40,000 (KMS § 19¹; 2026 data, source EMTA)
- **e-Residency** program for non-residents

### Salary benchmarks (2026)

- Average gross monthly wage: **€2,243** (Q2 2026, +5.5% YoY); people working in Tallinn **€2,611** (2026 data, source Statistikaamet, published 3 Sep 2026)
- Median monthly gross, county level (Q2 2026): Estonia **€1,840**; Harju **€2,033**; Tartu **€1,918**; Pärnu **€1,530**; Ida-Viru **€1,500**; Saare **€1,493**; Valga **€1,438** (lowest) (2026 data, source Statistikaamet)
- **Minimum wage**: **€946/month** (€5.67/hour) from 1 Apr 2026, up from €886 in 2025 (Government regulation no. 36 of 23 Mar 2026) (2026 data, source EMTA / Riigi Teataja); 2027 rate under negotiation — no figure agreed at the first round on 12 Oct 2026 (source Eesti Tööandjate Keskliit)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Keskkonnaagentuur (Environment Agency)** | `https://www.ilmateenistus.ee/` | Climate, weather, hydrology |
| **Keskkonnaportaal** | `https://keskkonnaportaal.ee/en/` | Environmental hazard maps |
| **Keskkonnaagentuur open-water (flood) map** | `https://keskkonnaportaal.ee/en/topics/remote-sensing/flood-map` | Operational Sentinel-1 snapshot of open-water extent at the latest satellite pass (coast, 90 largest lakes, river floodplains; ~5×20 m resolution, unreliable under snow / ice) — not a hazard-zone map (source ilmateenistus.ee flood-map page) |
| **Flood hazard & risk maps (Floods Directive)** | `https://xgis.maaamet.ee/xgis2/page/app/yleujutusalad` | Flood extents for 10 / 50 / 100 / 1000-yr return periods (P = 10 / 2 / 1 / 0.1 %), coast + inland waters; 34 significant flood-risk areas confirmed 3 Apr 2025; maps updated by Keskkonnaagentuur, published Jun 2025 in the Maa- ja Ruumiamet geoportal (2025 data, source Keskkonnaagentuur 2025-07-14) |
| **EGT (Eesti Geoloogiateenistus)** | `https://www.egt.ee/en` | Geology, **radon**, geohazards |
| **Päästeamet (Rescue Board)** | `https://www.rescue.ee/` | Emergency response |

### Specific risks

- **Flood**: Pärnu (storm surge worst-case), coastal Hiiumaa/Saaremaa. Pärnu record: 294 cm above EH2000 at ~06:00 on 9 Jan 2005 (Gudrun/Erwin), ~8 km² of the city flooded (2005 event, source Keskkonnaagentuur 2025-01-09). Significant flood-risk areas include Pärnu, Haapsalu, Kuressaare, Kärdla, Paide, Põhja-Tallinn / Kesklinn / Pirita, Tartu, Võru, Kunda and Narva-Jõesuu (2025 data, source Keskkonnaagentuur 2025-07-14) — area-level maps; overlay the parcel on the Floods Directive map
  - **Sentinel-1 open-water map** = live observation only; the statutory hazard zones are the Floods Directive maps above
- **Storms**: Baltic winter storms (Gudrun 2005 type — gusts 38 m/s on Kihnu, 33 m/s on Ruhnu and Vilsandi on 9 Jan 2005; 2005 event, source Keskkonnaagentuur 2025-01-09)
- **Radon**: highest in the **North Estonian Klint zone** (graptolitic argillite + phosphorite deposits); risk also high in parts of Central and Southern Estonia (source EGT natural-radon-risk page). North coast / Viimsi / Harjumaa / Lääne-Viru sit on the klint belt (geographic reading — not named on the EGT page); check the parcel on the EGT map
  - EGT radon risk map: `https://gis.egt.ee/portal/apps/experiencebuilder/experience/?id=f4363bc3bae34fe19e04458dc875375e` (workplace indoor-radon reference levels: Minister of the Environment regulation no. 28 of 30 Jul 2018, per EGT)
  - Higher risk than NL/UK; lower than CZ/SK
- **Climate**: warming + Baltic sea-level rise; permafrost not relevant
- **Earthquake**: very low (Fennoscandian shield)
- **Wildfire**: low-moderate (peat bog + boreal forest)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990 (Soviet era)** | Asbestos common, lead paint, dated heating |
| **Khrushchyovka + Brezhnev panel** | Energy-inefficient, asbestos |
| **1990s–2000s** | Improving insulation |
| **Post-2008** | Modern energy code |
| **Post-2020 LEED/BREEAM** | Some commercial; growing residential |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energiamärgis** (energy certificate) | Sale + lease: buyer / tenant must be able to review it and listings must state the energy class; issued only via the ehitisregister (EHR) | 10 years for an actual-consumption (KEK) certificate from EHR entry; 2 years from the occupancy permit for a design-based (ETA) one (2025 data, source TTJA + Kliimaministeerium). A–H scale to become A–G under EPBD recast 2024/1275 (transposition deadline 29 May 2026) |
| **e-Notar contract** | All sales | At sale |
| **Kinnistusraamat extract** | Title verification | At sale |

### Climate change projections

- **Annual mean temperature +2.7 °C (RCP4.5) / +4.3 °C (RCP8.5)** for 2071–2100 vs 1971–2000; largest rise in spring and winter (EURO-CORDEX ensemble; 2014 report data, source Keskkonnaagentuur "Eesti tuleviku kliimastsenaariumid aastani 2100" — AR5/RCP-based, still Estonia's established national scenario on EEA Climate-ADAPT, 2026)
- **Sea-level rise**: global mean +32–63 cm (RCP4.5) / +45–82 cm (RCP8.5) for 2081–2100 (IPCC AR5), up to 52–98 cm by 2100 under RCP8.5; on the west coast local relative change and land uplift (~1 mm/yr Pärnu, > 2 mm/yr Hiiumaa) roughly cancel, so the global mean applies — combined with storm surges a significant danger for Pärnu even under RCP4.5 (2014 report data, source Keskkonnaagentuur national climate scenarios)
- **More precipitation in every season**: annual +16 % (RCP4.5) / +19 % (RCP8.5), winter +16 % / +22 % (2071–2100 vs 1971–2000); > 30 mm/day downpours more frequent; snow cover sharply reduced — under RCP4.5 practically no persistent Jan–Feb snow cover (2014 report data, source Keskkonnaagentuur national climate scenarios)
- **Wind**: mean winter (partly spring) wind speed +3–18 % (more Atlantic cyclones); extreme-wind projections are not considered reliable enough to use, so "more extreme storms" stays unquantified (2014 report data, source Keskkonnaagentuur national climate scenarios)

---

## Section: `--mains`

### Sources

- **Tallinna Vesi**: `https://www.tallinnavesi.ee/` (Tallinn water/sewer)
- **Per-omavalitsus** (municipality) utilities: AS Tartu Veevärk (Tartu, `https://tartuvesi.ee/`), AS Pärnu Vesi (Pärnu city + Tori parish, `https://www.parnuvesi.ee/`)
- Universal in cities; rural **kogumiskaev** (cesspits) common

### Costs

Indicative installer/connection ranges (est. — confirm with a current utility tariff or installer quote):

| Scenario | Cost (€) |
|---|---:|
| Mains connection (Tallinn) | ~€3,000–€8,000 (est.) |
| Septic / individual treatment | ~€4,000–€10,000 (est.) |
| Bored well | ~€5,000–€12,000 (est.) |
| Tallinna Vesi household water + sewer tariff (Tallinn + Saue, pollution group 1, incl. VAT) | €2.87/m³ = 1.48 water + 1.39 sewer (from 1 Jul 2026; 2026 data, source Tallinna Vesi hinnakiri) |

---

## Cost benchmarks (EE 2026)

Notary and land-register fees computed from the pre-2027 statutory tables (notary table changes under 941 SE — see `--tax`); all construction/retrofit figures are **est. indicative ranges** (contractor quote bands — verify on quote):

| Work | Cost (€) |
|---|---:|
| Energiamärgis | 150–400 |
| Notary fee incl. 24 % VAT (2 × full fee, €50k–€300k sale; computed) | 208–1,135 |
| Land Register state fee (owner entry, €50k–€300k; RLS table) | 53–350 |
| **Total transaction cost (buyer)** | **~0.5 %** of price without a mortgage (computed; no transfer tax) |
| Roof renovation | 8,000–20,000 |
| Asbestos abatement | 2,000–10,000 |
| Energy retrofit (Class E → A) | 25,000–60,000 |
| Insulation upgrade | 5,000–15,000 |
| Heat pump | 8,000–18,000 |
| Solar PV (5kW) | 5,000–10,000 |

## Active fiscal incentives (2025-2026)

- **Apartment-building renovation grant** (korterelamute rekonstrueerimistoetus 2022–2027, run by **EIS** — Ettevõtluse ja Innovatsiooni Sihtasutus, formerly KredEx): housing associations of pre-2000 buildings with 3+ flats; 30–50 % depending on location and works (lowest in Tallinn / Tartu); €330m EU structural funds for 2022–2027; latest round 15 Sep–15 Oct 2025 (€80m) — **closed**, no open round listed (2026 data, sources eis.ee + Kliimaministeerium)
- **Housing-loan guarantee** (eluasemelaenu käendus, EIS, applied for through a partner bank): lets target groups buy with **10 % own funds** (large families **5 %**); guarantee up to 24 % of collateral value / €20,000, up to €50,000 for energy-efficient homes and for large families (up to 40 %); one-off fee 3 % of the guarantee (2 % for large families). Target groups include young families (parent ≤ 35 with a child ≤ 16, or ≤ 40 with 2+ children), young specialists ≤ 35, energy-efficient home buyers and large families (3+ children ≤ 19); all but large families must own no other dwelling (or sell it within 12 months); owner-occupied, no letting. Rural home-loan guarantee: up to €150,000 / 80 % (2026 data, source eis.ee)
- **Small houses (väikeelamu)**: no renovation-grant round open; heating-device renewal grant round III listed as open, up to 70 % by region (2026 data, source EIS household-financing page)
- **Solar PV**: no stand-alone solar grant for private persons on EIS's household scheme list (2026); an EIS solar-panel grant for housing associations (30–40 %, max €150,000 per applicant) is described in a 2025 Kliimaministeerium housing analysis (current status not verified)
- **District heating connection** subsidies in Tallinn

## Common listing platforms

- **KV.ee** — biggest (market leader by time on site, Baltic Classifieds Group / Similarweb, April 2026)
- **City24.ee** — No.2; better UX, expat-friendly
- **Maa365.ee** — ❌ DEPRECATED — dead on 2026-10-23 (domain not found in the .ee registry WHOIS); verify with Maa- ja Ruumiamet transaction statistics (land categories)

## Caveats unique to EE

- **e-government / e-Notar digital property contracts** — UNIQUE globally; real-estate deals can be notarised remotely by video bridge at the notary's discretion (laptop/desktop required), signing with ID-card, digi-ID, Mobile-ID, Smart-ID, residence-permit card or e-resident digi-ID (2026 data, source notar.ee — kaugtõestamine); €20 remote surcharge until 941 SE takes effect
- **NO annual tax on buildings** — only land (maamaks) — UNIQUE in EU
- **NO transfer tax** — only notary + land register fee — UNIQUE; together ~0.5 % of price without a mortgage (computed, see `--tax`)
- **Maamaks reform 2024-2026** — rates rising, municipality discretion expanded (caps 10–100 %, homeowner relief €0–1,000; EMTA); the 2026 land revaluation feeds land tax from 1 Jan 2028 (Maa- ja Ruumiamet)
- **VAT 20% → 22% (1 Jan 2024) → 24% (1 Jul 2025; open-ended since the Riigikogu passed 645 SE on 18 Jun 2025)** — major rise (2026 data, sources EMTA + Rahandusministeerium)
- **Tulumaks (income tax + CGT integrated) 22 % from 1 Jan 2025, unchanged in 2026** (2026 data, source EMTA tax-rates page)
- **Currency: EUR since 2011** (no FX risk for eurozone buyers)
- **Apartment prices flat in 2026**: MaRu apartment price index unchanged YoY in Q2 2026 (−2.2% QoQ); Tallinn secondary +4.3% YoY, new +1.1% (2026 data, source Maa- ja Ruumiamet)
- **Soviet-era panel buildings**: Khrushchyovka + Brezhnev — many in Tallinn Lasnamäe, Mustamäe, Õismäe — energy-inefficient + asbestos
- **No national short-let registration regime yet** — EU Reg (EU) 2024/1028 (registration-number rules where a Member State runs a registration procedure + platform data-sharing in those areas only) applies from 20 May 2026; MKM's Jun 2026 Tourism Act VTK proposes no STR register; entry into force targeted 2027-2028
- **e-Residency**: foreign nationals can register Estonian companies remotely
- **Bordering Russia (Ida-Virumaa)**: geopolitical tail risk; Narva primarily Russian-speaking
- **Korteriühistu** financial health critical for apt purchase
- **Pärnu coastal market**: tourist-driven + EU-buyer demand growing

## Reddit / forum sources

- **r/Estonia** — biggest community
- **r/Tallinn**
- **e-Estonia.com** (gov info)
- **Estonian World** (English news)
- **The Baltic Times**

## Verification authorities

| Authority | When to call |
|---|---|
| **Maa- ja Ruumiamet (MaRu; Maa-amet until 31 Dec 2024)** | Cadastre verification, geoportal (flood + noise maps) |
| **e-Kinnistusraamat (RIK)** | Title + owner verification |
| **e-Notar** | Sale process |
| **EMTA (tax authority)** | Maamaks + VAT |
| **Local omavalitsus** | Local maamaks rate + permits |
| **Korteriühistu** | If apartment |
| **EGT** | Radon |
| **Keskkonnaagentuur** | Flood hazard / risk maps, sea-level + storm-surge warnings, climate scenarios |
| **Transpordiamet** | State-road traffic counts (AKÖL) |

## Source URL templates

| Source | URL pattern |
|---|---|
| Maa- ja Ruumiamet Geoportaal | `https://geoportaal.maaruum.ee/` (old `geoportaal.maaamet.ee` redirects) |
| Flood hazard & risk map (X-GIS) | `https://xgis.maaamet.ee/xgis2/page/app/yleujutusalad` |
| e-Kinnistusraamat (RIK) | `https://www.rik.ee/en/e-land-register/e-land-register-portal` |
| Statistikaamet | `https://stat.ee/en/` |
| KV.ee | `https://www.kv.ee/en/` |
| EMTA (tax) | `https://www.emta.ee/en/` |
| Keskkonnaportaal | `https://keskkonnaportaal.ee/en/` |
| EGT (geology + radon) | `https://www.egt.ee/en` |
| EGT radon risk map | `https://gis.egt.ee/portal/apps/experiencebuilder/experience/?id=f4363bc3bae34fe19e04458dc875375e` |
| Transpordiamet traffic counts | `https://www.transpordiamet.ee/liiklussageduse-statistika` |
| Eesti Pank | `https://www.eestipank.ee/en/` |

## Status

✅ **Fully populated** as of 2026-04-25. Rental: Sep 2026 MKM STR position added 2026-09-24 in the October regwatch wave from ERR News (secondary); EU Reg 2024/1028 Art. 4/19, the MKM VTK and the Tallinn Old Town plan status re-read 2026-10-21 (December regwatch wave, run early). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (Statistikaamet + Maa- ja Ruumiamet + KV.ee), traffic (Transpordiamet), tax (maamaks reform 2024-2026 + VAT 22%→24% + 22% CGT), rental (EU Reg 2024/1028 from 20 May 2026; no national STR reg yet), work, risks (flood + radon + Baltic storms), mains all have primary government sources + cost benchmarks.
**Confidence**: HIGH for 2026 price benchmarks (Maa- ja Ruumiamet Q2 2026 review + statistics query, retrieved 2026-10-23; Narva / Kuressaare / Tartu-county rows are computed municipality-level medians); HIGH for work (Statistikaamet Q2 2026 wages + county medians, minimum wage €946 from 1 Apr 2026); HIGH for maamaks caps + homeowner relief (EMTA land-tax page); HIGH for VAT 24 % from 1 Jul 2025, open-ended since the Riigikogu vote of 18 Jun 2025, and 13 % accommodation VAT from 1 Jan 2025 (EMTA + Rahandusministeerium); HIGH for Tulumaks 22 % in 2026 (EMTA); HIGH for the pre-2027 notary fee computation (notar.ee worked example + NotTS § 22 table); MEDIUM for the Land Register state-fee table (RIK guide PDF dated 2022 + secondary calculator; not confirmed against Riigi Teataja); LOW for the post-2027 notary table under 941 SE (passed 21 Oct 2026; table and 1 Jan 2027 start from secondary sources only); HIGH for e-government / cadastre sources (Maa- ja Ruumiamet + RIK); MEDIUM for short-let specifics (Reg (EU) 2024/1028 Art. 4/10/19 re-read on EUR-Lex 2026-10-23, no national regime; ERR 2027-2028 timing and the Sep 2026 MKM position secondary); MEDIUM for risks (flood, storm, radon and climate lines re-sourced to Keskkonnaagentuur / EGT / TTJA; radon comparison, earthquake / wildfire ratings and build-era table not re-sourced; keskkonnaportaal.ee URLs unconfirmed); MEDIUM for traffic (AKÖL examples from Transpordiamet 2025 counts; band cutoffs are calibration heuristics); LOW for the est. ranges (Tartu / Pärnu maamaks bills, mains connection / septic / well, construction / retrofit bands — no primary source).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | 78 municipalities (agri.ee); Maa- ja Ruumiamet + geoportaal URL; e-Notar remote notarisation (notar.ee); example postcodes not checked |
| `--price` | 2026-10-23 | 2026-10-23 refresh wave | Benchmark table rebuilt from Maa- ja Ruumiamet Q2 2026 review + statistics query; Maa365.ee deprecated; agency-network list unranked |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Statistikaamet Q2 2026 wages + county medians; minimum wage €946 (1 Apr 2026); OÜ capital rule; RTK state-jobs line unverified |
| `--climate` (projections under `--risks`) | 2026-10-23 | 2026-10-23 refresh wave | Four projection lines re-sourced to Keskkonnaagentuur 2014 national scenarios; rest of `--risks` not fully re-verified |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | KV.ee time-on-site lead (BCG / Similarweb, Apr 2026); City24 No.2; Maa365.ee deprecated |
| Caveats unique to EE | 2026-10-23 | 2026-10-23 refresh wave | Price, short-let, tax and legal lines re-sourced (MaRu, EUR-Lex, EMTA, notar.ee); panel-building, Ida-Virumaa, Korteriühistu and Pärnu-market lines not re-checked |

## Extension TODOs

- [ ] Per-omavalitsus maamaks rates table
- [ ] Korteriühistu financial health rubric
- [ ] e-Notar digital signing flow for non-residents
- [ ] e-Residency property purchase flow
- [ ] Soviet-era panel building inventory (Lasnamäe, Mustamäe)
- [ ] Pärnu coastal market vs inland comparison
- [ ] Radon zone overlay (EGT) per parish
- [ ] Geopolitical risk assessment (Ida-Virumaa)
- [ ] District heating connection availability
- [ ] KredEx grant eligibility decision tree

## Update history

- **2026-04-25** — Initial population
- **2026-09-24** — October / November regwatch waves (November run early): Sep 2026 MKM STR position added (ERR News, secondary); tax tracker entries re-checked
- **2026-10-21** — December regwatch wave (run early): EU Reg 2024/1028 Art. 4/19, MKM VTK and Tallinn Old Town plan re-read; rental / tax tracker entries re-checked
- **2026-10-23** — Refresh wave + audit corrections (facts changed / confirmed / unverifiable). Re-verified: Country profile 3 / 4 / 2; `--price` 18 / 5 / 1; `--work` 6 / 4 / 2; Common listing platforms 3 / 0 / 1; Caveats unique to EE 6 / 3 / 0 (price, short-let, tax and legal lines); `--climate` projections 4 / 0 / 0 (counted in `--risks`). Partly re-verified: `--tax` 14 / 12 / 4; `--rental` 6 / 6 / 4; `--risks` 11 / 4 / 5; `--traffic` 6 / 1 / 2; `--mains` 2 / 1 / 4; Cost benchmarks 3 / 0 / 7; Active fiscal incentives 3 / 0 / 1; Verification authorities 1 / 3 / 3; Source URL templates 2 / 6 / 1; Reddit / forum sources 0 / 2 / 3. Main changes: price table rebuilt from Maa- ja Ruumiamet Q2 2026 data (the earlier 2025 values could not be traced to a source); minimum wage €820 → €946 (from 1 Apr 2026); 78 municipalities after the Jõhvi–Toila merger; Maa-amet → Maa- ja Ruumiamet and Maanteeamet → Transpordiamet; Maa365.ee deprecated; VAT 24 % open-ended since 18 Jun 2025 (replaces the wrong "made permanent April-May 2026" date); notary and land-register fees computed from the pre-2027 statutory tables (buyer cost ~0.5 % without a mortgage), with bill 941 SE (passed 21 Oct 2026) changing the notary table; mortgage interest not deductible since 2024; short-let accommodation at 13 % VAT and taxed on gross income; traffic examples and calibration sourced to Transpordiamet 2025 AKÖL counts; flood hazard maps and climate projections sourced to Keskkonnaagentuur. Playbook-level date kept at 2026-04-25: `--tax`, `--rental`, `--risks` and `--mains` still carry unsourced est. ranges or claims not re-fetched
