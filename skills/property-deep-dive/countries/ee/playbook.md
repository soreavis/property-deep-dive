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

### Annual property tax — Maamaks (LAND ONLY)

**Estonia has NO annual property tax on buildings — only on LAND.**

#### Maamaks reform 2024-2026

- **2024**: max +10% increase per cadastral unit, or +€5 floor
- **2025**: max +50% increase or +€20 floor
- **2026**: limit set by **each local government** at 10–100%; €5 floor; **homeowner relief €0–1,000** per property (amount-based, also municipality-set; replaces the 2025 area-based exemption of up to 0.15 ha in densely populated areas) (2026 data, sources [EMTA — Land tax](https://www.emta.ee/en/private-client/taxes-and-payment/other-taxes/land-tax) + Maamaksuseadus § 8¹(1)–(2) and § 11(1), [Riigi Teataja](https://www.riigiteataja.ee/akt/130062024005); 2024 +10 %/€5 and 2025 +50 %/€20 caps confirmed on the EMTA page)
- **2027**: same mechanism — each council sets the cap by 1 Oct of the preceding year (Maamaksuseadus § 8¹); e.g. Tartu 50 % cap + homeowner relief up to €850 (city regulations nos. 17 and 16 of 18 Jun 2026), Pärnu homeowner relief €1,000 (2027 data, sources tartu.ee + parnu.ee + [EMTA 2027 rate and relief table](https://ncfailid.emta.ee/s/8gyxyJd9eTRnmga))

#### Rate ranges (set per municipality by 1 Oct of the preceding year; 2026 data, sources Maamaksuseadus § 5(1), [Riigi Teataja](https://www.riigiteataja.ee/akt/130062024005) + EMTA land-tax page)

| Land type | Rate range |
|---|---|
| Residential / yard land | 0.1–1% |
| Profit-yielding land | 0.1–0.5% |
| Other land | 0.1–2% |

#### Typical bills

These three ranges are **est.**, not published bill figures. A plot's bill is its assessed land value × the council rate, raised by no more than the council's annual cap over the previous year's amount, minus the homeowner relief where the owner's registered residence is in a building on that land (Maamaksuseadus §§ 8¹, 11). Calibration: the ranges are not drawn from real bills; dividing each by the council rate gives the assessed land value it implies (shown per line), to compare with the plot's value on minu.kataster.ee › "Maa väärtuse info" (Maa- ja Ruumiamet); the actual bill is on the EMTA land-tax notice. Council inputs: 2026 and 2027 data, sources [EMTA 2026 rate and relief table](https://ncfailid.emta.ee/s/WwXEaoCW9sLAobm) + [EMTA 2027 table](https://ncfailid.emta.ee/s/8gyxyJd9eTRnmga) + tallinn.ee.

- Tallinn 100m² apt with land share: **~€100–€500/yr** before relief (est. — at Tallinn's 0.50 % residential rate this implies a €20,000–€100,000 assessed value for the apartment's land share; 10 % annual cap; homeowner relief €1,000 per property, so a registered-resident owner whose computed tax is €1,000 or less pays €0)
- Tartu single-family with 1,000m² plot: **~€200–€600/yr** before relief (est. — at Tartu's 1.00 % rate this implies a €20,000–€60,000 assessed value, €20–€60/m²; 50 % annual cap; homeowner relief €500 in 2026, €850 in 2027)
- Pärnu coastal villa with 2,000m² plot: **~€500–€1,500/yr** before relief (est. — at Pärnu's 1.00 % rate this implies a €50,000–€150,000 assessed value, €25–€75/m²; 10 % annual cap; homeowner relief €600 in 2026, €1,000 in 2027)
- Spread of assessed values in the 2022 valuation (basis for land tax 2024–2027): residential land above €300/m² in central Tallinn and Tartu, mostly €0.3–€1.0/m² in the lowest of eight location classes, which covers most of Estonia (2022 data, source [Maa- ja Ruumiamet 2022 valuation brochure](https://maaruum.ee/sites/default/files/documents/2024-12/Maa%20korraline%20hindamine%20voldik%202022.pdf)) — rates/figures may have changed since; the 2026 valuation, used from 2028, raised the national residential-land total by 35 % (see Future risk)

### Transaction taxes

- **NO transfer tax** — no real-property transfer tax and no tax on building value (2025 data, sources IMF Selected Issues Paper 2025/102 + PwC Worldwide Tax Summaries — secondary); land tax is levied on the assessed value of the land only (Maamaksuseadus § 1(1)) and the valuation excludes buildings and growing forest (2026 data, source [Maa- ja Ruumiamet](https://maaruum.ee/maa-korraline-hindamine-2026)). Not unique in the EU: Czechia abolished its acquisition tax for cadastre entries effective from 26 Sep 2020 (Act No. 386/2020 Coll., source [Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-nabyti-nemovitych-veci))
- **Notary fee (notari tasu)**: statutory and identical at every notary — a two-party sale costs **2 × the full fee** from the Notari tasu seadus § 22 value table **+ 24 % VAT**. Computed: €50k → 2 × €83.70 = €167.40 + VAT = **€207.58**; €100k → **€397.79**; €150k → **€588.01**; €200k → **€778.22**; €300k → **€1,134.85**. Incl. VAT the fee stays under €500 only up to a ~€128k transaction value. Who pays is agreed between the parties (2026 data, sources [Notarite Koda — fee calculation](https://www.notar.ee/ametitoimingud/notari-tasu-arvestamine) worked example + NotTS § 22–23 table, [Riigi Teataja — NotTS](https://www.riigiteataja.ee/akt/128012026008), redaction in force since 7 Feb 2026)
- **Notary fee schedule changing from 1 Jan 2027**: the Riigikogu adopted bill **941 SE** (Notary Fees Act amendments) on **21 Oct 2026** (67 for, 1 against) and sent it to the President on 23 Oct 2026; the President proclaimed it on 6 Nov 2026 and it is published as [RT I, 12.11.2026, 1](https://www.riigiteataja.ee/akt/112112026001), with the [NotTS redaction in force from 1 Jan 2027](https://www.riigiteataja.ee/akt/112112026003) (sources [Riigikogu bill page](https://www.riigikogu.ee/tegevus/eelnoud/f5631762-476d-40cc-9124-7dfcb2730c0f/notari-tasu-seaduse-ja-teiste-seaduste-muutmise-seadus/) + [riigikogu.ee press release, 21 Oct 2026](https://www.riigikogu.ee/pressiteated/jargmise-aasta-riigieelarve-eelnou-labis-esimese-lugemise-2)). Per the [adopted text](https://www.riigikogu.ee/wp-json/riigikogu/v1/files/7e2d4a2c-df77-4037-9987-22d321d62679/download) it enters into force **1 Jan 2027** (§ 5), raises the § 22 full fees (e.g. **€140** up to €50k vs €83.70 now, **€212** up to €100k, **€522** up to €300k), sets the minimum transaction value of an immovable at **€10,000** (§ 4(1); €6,391 now) and abolishes the remote-authentication fee; § 23 (double fee for a contract) is not amended. Computed for a two-party sale from 1 Jan 2027, incl. 24 % VAT ([EMTA](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate) standard rate since 1 Jul 2025, open-ended): €50k → **€347.20**; €100k → **€525.76**; €150k → **€699.36**; €200k → **€897.76**; €300k → **€1,294.56**; incl. VAT the fee stays under €500 only up to a €90k transaction value. The computed fees above are the pre-2027 table
- **Land Register state fee (riigilõiv, owner entry)**: full rate from the Riigilõivuseadus Annex 2 value table (RLS § 74), no VAT; 50 % for a spouse, registered partner or direct-line relative, 75 % for a sibling or a sibling's descendant (RLS § 76(2)–(3)): €50k → **€53**; €100k → **€110**; €150k → **€175**; €200k → **€235**; €300k → **€350**; above €639,120 0.16 % of value, max **€2,560** (2026 data, source [RLS Annex 2](https://www.riigiteataja.ee/aktilisa/1211/0202/6010/RLS_lisa2.pdf), [Riigi Teataja — RLS](https://www.riigiteataja.ee/akt/121102026010) redaction in force from 1 Nov 2026; §§ 74–76 and Annex 2 unchanged in the published redaction from 1 Jan 2027; same values as the [RIK state-fee guide](https://www.rik.ee/sites/default/files/2024-05/Riigiloiv_juhend.pdf), PDF dated 2022)
- **e-Notar remote authentication (kaugtõestamine)**: same fee scale **+ €20** surcharge (NotTS § 2(2¹), in force since 1 Feb 2020; 2026 data, source [Riigi Teataja — NotTS](https://www.riigiteataja.ee/akt/128012026008)); repealed from 1 Jan 2027 by 941 SE § 1 p. 1 (RT I, 12.11.2026, 1; see above)

### VAT (käibemaks)

- **20 % → 22 %** on 1 Jan 2024 (applied until 30 Jun 2025)
- **24 % standard from 1 July 2025** (Security Tax Act; raised from 22 %; made **open-ended** when the Riigikogu passed bill 645 SE on **18 Jun 2025** — VAT will NOT revert to 22 % from 2029) — Käibemaksuseadus (KMS) § 15(1), unchanged in the KMS redaction published for 1 Jan 2027 ([Riigi Teataja — KMS](https://www.riigiteataja.ee/akt/130062026130)). (2026 data, sources [EMTA — Käibemaks](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks) + [Rahandusministeerium, 18 Jun 2025](https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused))
- **Accommodation reduced VAT**: **9 % → 13 % from 1 Jan 2025** on accommodation and accommodation with breakfast, not on goods or services supplied with it (KMS § 15(1¹)); accommodation is carved out of the VAT exemption for letting immovable property (KMS § 16(2)(2)), so ordinary residential letting stays exempt. KMS sets no hotel-classification test and does not define where a short-let stops being a lease — verify the treatment of a specific let with EMTA (2026 data, sources [Riigi Teataja — KMS](https://www.riigiteataja.ee/akt/130062026129), rate unchanged in the redaction published for 1 Jan 2027, + EMTA VAT page)
- New builds (sold before first use, or — since 1 Jan 2025 — first sold within 1 year after first use), significantly improved buildings (improvement costs ≥ 10 % of the prior acquisition cost; same timing rule) + building land (ehitusmaa): **24 % VAT applies** (KMS § 16(2)(3), wording in force since 1 Jan 2025; 2026 data, sources [Riigi Teataja — KMS](https://www.riigiteataja.ee/akt/130062026129) + EMTA VAT handbook, updated 8 Jan 2025)
- Resale: generally **VAT-exempt** (same source)

### Capital gains — Tulumaks (Tulumaksuseadus)

- **Tulumaks 22 % from 1 Jan 2025 and still 22 % in 2026** (EMTA tax-rates page, 2026 block: "The rate of withheld income tax is 22%"; corporate distributed profit 22/78; CGT integrated into general Tulumaks; TuMS § 4(1) 22 % also in the redaction published for 1 Jan 2027, [Riigi Teataja — TuMS](https://www.riigiteataja.ee/akt/109072026067)). (2026 data, source [EMTA — Tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))
- **Primary residence exempt** if the dwelling was the seller's residence until the sale — no minimum ownership period, but usable for **one disposal per 2 years** (TuMS § 15(5)(1) + (6)); a summer house / garden house is exempt if owned > 2 years on a plot ≤ 0.25 ha (§ 15(5)(4)) (2026 data, sources TuMS § 15(5)–(6), Riigi Teataja + EMTA income-tax handbook — Kinnisvara võõrandamine, updated 27 Jun 2026)

### Total transaction cost (buyer side)

- Resale primary: **~0.5 %** of price without a mortgage — computed, buyer paying the full notary fee + owner-entry state fee: €100k → €397.79 + €110 = **€507.79 (0.51 %)**; €300k → €1,134.85 + €350 = **€1,484.85 (0.49 %)** (pre-2027 tables, see above). From 1 Jan 2027 under the 941 SE notary table (state fee unchanged): €100k → €525.76 + €110 = **€635.76 (0.64 %)**; €300k → €1,294.56 + €350 = **€1,644.56 (0.55 %)** (computed). A hypothec signed in the same deed adds its own notary + state fees (secondary calculator example: €150k purchase + €180k hypothec → €1,092.02 ≈ 0.73 %, hüpoteek.ee)
- New build: 24 % VAT included in the developer's price + the same notary / state fees (~0.5 %, computed above)

### Future risk

- **Maamaks**: councils may set the annual increase cap anywhere from 10 % to 100 % (Maamaksuseadus § 8¹(1)) — for 2027 Kohtla-Järve, Ruhnu and Tori set 100 % and Tartu 50 % (2027 data, source [EMTA 2027 rate and relief table](https://ncfailid.emta.ee/s/8gyxyJd9eTRnmga); also reported by ERR News, secondary). The **2026 regular land valuation** was published on 30 Oct 2026: total assessed land value €44.1bn vs €33.2bn in 2022 (+33 %), residential land €22.2bn vs €16.5bn (+35 %); the residential-land total (incl. yard land, units valued in both years) rose 24.0 % in Tallinn, 27.6 % in Tartu city and 35.3 % in Pärnu city — municipality totals, not parcel values, so check the plot on minu.kataster.ee. The new values are used for land tax **from 1 Jan 2028** (Maamaksuseadus § 1(2)), with each council's annual cap still applying (2026 data, sources [Maa- ja Ruumiamet, 30 Oct 2026](https://maaruum.ee/uudised/eesti-maa-vaartus-44-miljardit-eurot) + [results summary](https://maaruum.ee/sites/default/files/documents/2026-10/Maa_v%C3%A4%C3%A4rtused_2026.pdf) + [municipality table](https://maaruum.ee/sites/default/files/documents/2026-11/Maa%20v%C3%A4%C3%A4rtused%202026.html))
- **VAT**: standard rate 24 %, open-ended. Pending on 2026-11-03: the 2027 State Budget bill (**1037 SE**, submitted 29 Sep 2026, first reading passed 21 Oct 2026, sent to second reading on 27 Oct 2026) and the government VAT Act bill **992 SE** (initiated 14 Sep 2026, second reading completed 28 Oct 2026, third reading on the 11 Nov 2026 plenary agenda, entry into force 1 Jan 2027 if adopted; its Riigikogu summary covers EU OSS extension and platform-service place-of-supply rules; the second-reading text leaves the 24 % and 13 % rates unchanged) (sources riigikogu.ee + api.riigikogu.ee, Sep–Nov 2026); the KMS redaction published for 1 Jan 2027 keeps 24 % and 13 %, and the KMS redaction list showed no later amendment on 2026-11-03 ([Riigi Teataja — KMS](https://www.riigiteataja.ee/akt/130062026130))
- E-government efficiency continues — record-time transactions

---

## Section: `--rental`

### Long-term residential

- **Võlaõigusseadus § 271 ff** (Law of Obligations Act § 271+) governs lease
- **Tenant protection moderate** (less strict than DE/AT — qualitative comparison, wisdom, not data). Statutory anchors: VÕS sets no rent cap, but in an open-ended lease the landlord is presumed entitled to raise the rent once each year after the contract date, with ≥ 30 days' reasoned notice in a form reproducible in writing (§ 299); the tenant can challenge an excessive rise within 30 days, and a rise is not excessive if economically justified (§§ 301, 303); deposit max **3 months' rent**, which the tenant may pay in equal parts over 3 months and which the landlord must hold at a credit institution separately from own assets (§ 308); either party may end an open-ended dwelling lease with **≥ 3 months'** notice (§ 312(1)); the tenant may contest a bad-faith termination and ask the rent committee or court to extend the lease by up to **3 years** for serious hardship (§ 326); terms that deviate from the Act to the tenant's detriment are void (§ 275) (2026 data, source Riigi Teataja VÕS, redaction in force from 1 Sep 2026)
- **Indekseerimine** (periodic, e.g. CPI-linked, rent increase): valid in a dwelling lease only if the term is ≥3 years, the rent rises at most once a year and the increase or its calculation basis is precisely set (VÕS § 300, source Riigi Teataja)

### Short-let

**EU Reg (EU) 2024/1028** (STR data-collection) applies EU-wide **from 20 May 2026** (Art. 19) — harmonising registration-number rules wherever a Member State runs a registration procedure (Art. 4(1)) + platform data-transmission/verification obligations that attach only where such a procedure exists (a Member State requiring platform data must run one, Art. 4(2); only such a Member State sets up a single digital entry point, Art. 10(1)); it does **not** harmonise substantive limits (local night-caps stay national). (2026-10-23, source EUR-Lex Reg (EU) 2024/1028 Art. 4, 10, 19). Estonia runs no such registration procedure — the Tourism Act (TurS, redaction in force from 1 May 2026) does not separately define short-term rental and MKM's 18 Jun 2026 VTK proposes no STR register (sources Riigi Teataja TurS, mkm.ee 2026-06-18, ERR News 2026-06-25).

Estonia has **NO national mandatory STR-registration regime** in force. The Ministry of Economic Affairs (**MKM**) put a Tourism Act amendment VTK (legislative intent) out for consultation on 18 Jun 2026: short, repeated, paid letting of a dwelling, incl. via platforms, could be treated as an accommodation service — the host would then have to meet accommodation-service rules, e.g. a fire-safety memo and guest registration — and the VTK does **not** propose an STR register in the near term (cost); MKM also asks local governments whether they need extra tools, naming Tallinn Old Town and Pärnu as pressure areas; feedback by 1 Sep 2026, bill to be drafted during 2026 (source mkm.ee 2026-06-18). MKM estimates the STR market at over €100m in 2025, with nearly 1.9 million overnight stays a year (2025 data, source mkm.ee 2026-06-18 — ministry estimate). Per ERR, MKM expects entry into force in **2027-2028** (ERR News 2026-06-25, secondary) and hopes to send the draft for approval in Q4 2026 (ERR News 2026-09-03, secondary). Külli Kraner (Estonian Hotel and Restaurant Association) writes that residents, municipalities, hotels and STR operators back a nationwide accommodation database "but the Ministry of Economic Affairs and Communications is not listening" (ERR opinion 2026-02-04 — interest-group view, not data) — i.e. no such database exists yet. In Sep 2026 MKM said it sees **no need for new national STR limits** despite a European Commission proposal letting local governments restrict short-term rentals; the government is still developing its position (source ERR News 2026-09-13, secondary — verify with MKM).

- **Tulumaks** (income tax) 22 % on rental earnings (2025 and 2026 — EMTA tax-rates page; TuMS § 4(1), Riigi Teataja redaction in force from 1 Oct 2026); short-term letting via Airbnb / Booking.com is declared as "other rental income" and taxed on the gross amount — the 20 % deduction (TuMS § 39¹) covers only rent under a VÕS dwelling lease, so it does not apply (sources EMTA income-tax-return guidance for 2025 + Riigi Teataja TuMS)
- **VAT registration required once Estonian turnover exceeds €40,000 in a calendar year** (KMS § 19(1); 2026 data, sources EMTA + Riigi Teataja KMS); short-let accommodation (ajutise ööbimisvõimaluse pakkumine, TurS § 17(2)) is taxable — KMS § 16(2)(2) exempts letting of immovables but not accommodation services — and is charged at the **13 % accommodation rate** (KMS § 15(1¹), since 1 Jan 2025), not the 24 % standard rate; since 2025 exempt residential rent also counts toward the threshold once there is any taxable turnover (source EMTA VAT handbook + threshold page, updated 05.02.2026)
- **No Tallinn night-cap or STR limit**: the **Old Town (Vanalinn) development plan 2035** — Tallinn city government regulation no. 29 of 17 Jun 2025 (RT IV, 21.06.2025, 17 = Riigi Teataja 421062025017; in force 24 Jun 2025 – 31 Dec 2035) — sets the goal that short-term letting of apartments is "sufficiently regulated" to support permanent-resident growth, but its action 1.3 only analyses the problems and develops possible solutions, and the plan itself lists as a risk that the city lacks the legal power to regulate private property use, e.g. to restrict short-term rental. Its indicator (share of Old Town apartments let short-term, surveyed every 3 years) has baseline and target "to be set in 2025" in the adopted text; the plan cites an estimated up to one third of Old Town apartments let short-term in the pre-COVID peak tourism years (pre-2020 estimate, EKA 2023 study — rates/figures may have changed since) (2025 data, source Riigi Teataja 421062025017 + annex)
- **Guest registration** (TurS § 24): an accommodation-service provider registers each guest before the stay, as a rule from a travel document or ID card (name, date of birth, citizenship, country of residence, dates of stay, purpose of trip, number of accompanying minors; other foreigners also travel-document type, number and issuing state), keeps the data **2 years** and passes it to the Police and Border Guard Board (PPA) and security authorities **on their request** — the Act sets no routine report to PPA and no 24-hour deadline (2026 data, source Riigi Teataja TurS, redaction in force from 1 May 2026). Lets under a VÕS dwelling lease are not an accommodation service (TurS § 17(3)(2)), and whether a private host's short let is one is currently unclear (mkm.ee 2026-06-18); under the VTK, short, repeated, paid lets could become an accommodation service with guest registration (same source), and the Interior Ministry wants the duty to cover all providers, with an adviser suggesting a central guest-data portal (ERR News 2026-09-03, secondary)

### Tax on rental

- Residential lease (VÕS dwelling lease) by a private individual: 22 % income tax on 80 % of the rent — the flat 20 % expense deduction (TuMS § 39¹) is applied automatically in the return and the individual makes no further deduction ("füüsiline isik ise ei tohi üüritulust mahaarvamist teha") (source EMTA rental-income page, updated 05.12.2025)
- Short-let / sub-letting: no 20 % deduction — taxed on the gross amount (source EMTA)
- **Housing-loan (mortgage) interest NOT deductible** for individuals from 1 Jan 2024 — tax year 2023 was the last (source EMTA, updated 10.02.2025; TuMS § 25 repealed from 1 Jan 2024 by RT I, 30.06.2023, 107, Riigi Teataja)

---

## Section: `--work=<profession>`

### Sources

- **Töötukassa (Estonian Unemployment Insurance Fund)**: `https://www.tootukassa.ee/`
- **CV.ee** (CV-Online; cvonline.ee redirects there) + **CV Keskus** (`https://www.cvkeskus.ee/`) — the most popular job portals per EURES Estonia (eures.ee, Töötukassa); **Work in Estonia** (`https://workinestonia.com`) for English-language offers; LinkedIn
- **Riigi Tugiteenuste Keskus** for state jobs

### Self-employment

- **FIE (Füüsilisest isikust ettevõtja)** = sole trader
- **OÜ (Osaühing)** = limited; **no €2,500 minimum since 1 Feb 2023** — share capital from **€0.01 per shareholder**, paid in on formation (2026 data, source e-resident.gov.ee; 1 Feb 2023 Commercial Code change per Grant Thornton Estonia, secondary); corporate income tax only on distributed profit (22/78 in 2026, source EMTA)
- **Käibemaksu** registration: once turnover from the start of the calendar year exceeds €40,000 (KMS § 19(1); 2026 data, sources EMTA + Riigi Teataja KMS)
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
| **Keskkonnaportaal** (Keskkonnaagentuur) | `https://keskkonnaportaal.ee/` | Environmental data portal, linked from ilmateenistus.ee; content unverified — the site could not be read for verification on 2026-11-03, check it directly |
| **Keskkonnaagentuur open-water (flood) map** | `https://www.ilmateenistus.ee/siseveed/uleujutuste-kaart/` | Operational Sentinel-1 snapshot of open-water extent at the latest satellite pass (coast, 90 largest lakes, river floodplains; ~5×20 m resolution, unreliable under snow / ice; water-frequency statistics for April–October only) — not a hazard-zone map (2026 data, source ilmateenistus.ee flood-map page) |
| **Flood hazard & risk maps (Floods Directive)** | `https://xgis.maaamet.ee/xgis2/page/app/yleujutusalad` | Flood extents for 10 / 50 / 100 / 1000-yr return periods (P = 10 / 2 / 1 / 0.1 %), coast + inland waters; 34 significant flood-risk areas confirmed 3 Apr 2025; maps updated by Keskkonnaagentuur, published Jun 2025 in the Maa- ja Ruumiamet geoportal (2025 data, source Keskkonnaagentuur 2025-07-14) |
| **EGT (Eesti Geoloogiateenistus)** | `https://www.egt.ee/en` | Geology, **radon**, geohazards |
| **Päästeamet (Rescue Board)** | `https://www.rescue.ee/` | Emergency response |

### Specific risks

- **Flood**: Pärnu (storm surge worst-case), coastal Hiiumaa/Saaremaa. Pärnu record: 294 cm above EH2000 at ~06:00 on 9 Jan 2005 (Gudrun/Erwin), ~8 km² of the city flooded (2005 event, source Keskkonnaagentuur 2025-01-09). Significant flood-risk areas include Pärnu, Haapsalu, Kuressaare, Kärdla, Paide, Põhja-Tallinn / Kesklinn / Pirita, Tartu, Võru, Kunda and Narva-Jõesuu (2025 data, source Keskkonnaagentuur 2025-07-14) — area-level maps; overlay the parcel on the Floods Directive map
  - **Sentinel-1 open-water map** = live observation only; the statutory hazard zones are the Floods Directive maps above
- **Storms**: Baltic winter storms (Gudrun 2005 type — gusts 38 m/s on Kihnu, 33 m/s on Ruhnu and Vilsandi on 9 Jan 2005; 2005 event, source Keskkonnaagentuur 2025-01-09)
- **Radon**: highest in the **North Estonian Klint zone** (graptolitic argillite + phosphorite deposits); risk also high in parts of Central and Southern Estonia (source EGT natural-radon-risk page). North coast / Viimsi / Harjumaa / Lääne-Viru sit on the klint belt (geographic reading — not named on the EGT page); check the parcel on the EGT map
  - EGT radon risk map ("Eesti pinnase radooniriski kaart" — soil-air radon risk, not indoor levels): `https://gis.egt.ee/portal/apps/experiencebuilder/experience/?id=f4363bc3bae34fe19e04458dc875375e` (workplace indoor-radon reference levels: Minister of the Environment regulation no. 28 of 30 Jul 2018, per EGT)
  - National indoor-radon survey means (dwellings, arithmetic mean): Estonia **120 Bq/m³** vs Czech Republic 140, Slovakia 87, Netherlands 23, UK 20 — higher than NL / UK and SK, lower than CZ (2000 data, source [UNSCEAR 2000 Report, Annex B, Table 24](https://www.unscear.org/unscear/uploads/documents/publications/UNSCEAR_2000_Annex-B.pdf); CZ / SK / NL / UK values repeated in the WHO Handbook on Indoor Radon 2009, Table 4 — rates/figures may have changed since)
- **Climate**: warming + Baltic sea-level rise; permafrost not relevant
- **Earthquake**: very low (qualitative rating — wisdom, not data; Fennoscandian Shield setting). Calibration event: 25 Oct 1976, NW Estonia (59.21 N 23.52 E), ISC Bulletin mb 4.6 / Uppsala ML 4.7 (1976 event, source ISC Bulletin, isc.ac.uk). EGT runs the national seismic monitoring; its seismic page gives no hazard rating — verify at `https://www.egt.ee/en/fields-activity-and-objectives/geology-and-environment/seismic-research-and-monitoring`
- **Wildfire**: low-moderate (qualitative rating — wisdom, not data; peat bog + boreal forest). Keskkonnaagentuur publishes a daily fire-danger map (tuleohukaart; Canadian FWI method since 2025, as used by EFFIS): `https://www.ilmateenistus.ee/ilm/prognoosid/tuleohukaart/` (source ilmateenistus.ee)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990 (Soviet era)** | Asbestos common, lead paint, dated heating |
| **Khrushchyovka + Brezhnev panel** | Energy-inefficient, asbestos |
| **1990s–2000s** | Improving insulation |
| **Post-2008** | Modern energy code |
| **Post-2020** | nZEB (A-class) minimum for new buildings; LEED/BREEAM on some commercial, growing residential |

Curated era guide (wisdom, not data) — confirm with a building survey. Anchors: first energy certificates issued 2008–2009; nZEB (A-class) minimum energy requirement for new buildings from the start of 2020, major renovations must reach class C (2025 data, source TTJA energy-efficiency page, updated 1 Dec 2025); asbestos works need a start notice to and a permit from Tööinspektsioon (source ti.ee — asbestitööd).

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energiamärgis** (energy certificate) | Sale + lease: listings must state the energy-performance figure and class; the buyer / tenant must be able to review it and receives it (or a copy) at signing — met if it can be viewed in the ehitisregister (EHR) (Ehitusseadustik § 67); issued only via EHR (TTJA) | 10 years for an actual-consumption certificate; 2 years from completion (occupancy permit) for a design-based one (EhS § 66(3)). Scale **A–G** since 1 Jun 2025 — worst class G, was H (energy-certificate regulation § 14(2), as amended by RT I, 19.03.2024, 1); EPBD recast 2024/1275 Art. 19(2) obliges Member States to use an A–G scale by 29 May 2026 (2026 data, sources Riigi Teataja, TTJA energy-efficiency page updated 1 Dec 2025, Official Journal L 2024/1275) |
| **Notarised sale contract** (at the notary or by remote notarisation via e-Notar) | Every sale of an immovable: the obligation contract and the real-right contract transferring ownership must be notarially authenticated (Asjaõigusseadus §§ 119(1), 120(1)) | At signing (2026 data, source Riigi Teataja — AÕS) |
| **Kinnistusraamat extract** (land register) | Title check: ownership passes on the land-register entry, not at signing (AÕS § 64¹); entries are presumed correct and protect a good-faith buyer unless an objection is entered or the buyer knew or should have known the entry was wrong (AÕS §§ 56, 56¹) — check the current entry before signing | Current entry at signing (2026 data, source Riigi Teataja — AÕS) |

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
- Coverage: **85 %** of residents on a public water supply and **84 %** on a public (urban) wastewater collecting system in 2024 (2024 data, source Eurostat env_wat_pop + env_ww_con) — rates/figures may have changed since; the other ~15–16 % (computed) use private wells and individual systems — **kogumiskaev** (sealed holding tank), septic tank or small treatment plant. Eurostat gives no urban / rural split: "near-universal in cities, individual systems common in rural areas" is a curated reading, not data

### Costs

Septic and well rows: est. indicative ranges set in the 2026-04 research — inputs not recorded and not from an official price source; depth (wells) and soil / treatment capacity (septic) drive the spread, so get installer quotes:

| Scenario | Cost (€) |
|---|---:|
| Mains connection (Tallinn) | data not publicly available — the liitumistasu is the actual cost of the pipes and connection point built for the property plus any development cost (Konkurentsiamet methodology), quoted per property: verify at `https://www.tallinnavesi.ee/teenused/liitumine-vee-ja-kanalisatsiooniga`. Tallinn refunds eligible owners (Tallinn residence ≥ 12 months, building permitted before 31 Dec 2011, 100 % residential land, first connection) 50 % (plot acquired before 31 Dec 2011) or 30 % (acquired after) of the fee, max €5,000 / €3,000 where a pipe exists and €15,000 / €9,000 where none does (2026 data, source Tallinn City Council regulation, RT IV, 26.06.2021, 21) |
| Septic / individual treatment | ~€4,000–€10,000 (est.) |
| Bored well | ~€5,000–€12,000 (est.) |
| Tallinna Vesi household water + sewer tariff (Tallinn + Saue, pollution group 1, incl. VAT) | €2.87/m³ = 1.48 water + 1.39 sewer (from 1 Jul 2026, approved by Konkurentsiamet decision no. 9-3/2026-014 of 26 May 2026; 2026 data, source Tallinna Vesi hinnakiri) |

---

## Cost benchmarks (EE 2026)

Notary and land-register fees computed from the 2026 statutory tables (NotTS §§ 22–23 and RLS Annex 2, Riigi Teataja; the notary table changes on 1 Jan 2027 under 941 SE (RT I, 12.11.2026, 1) — see `--tax`). The energy-certificate and construction / retrofit rows are **est.** quote bands (energy auditor / contractor) set at the Apr 2026 initial population; they carry no primary-source or price-survey basis, so get written quotes. Drift calibration: Statistikaamet's repair and reconstruction work price index (1997 = 100) was 283.19 in Q3 2026 vs 282.36 in Q2 2026 (+0.3 %) and 274.52 in Q3 2025 (+3.2 % YoY), so the bands are not re-indexed (2026 data, source [Statistikaamet table IA13](https://andmed.stat.ee/api/v1/en/stat/majandus/hinnad/IA13.PX)):

| Work | Cost (€) |
|---|---:|
| Energiamärgis (energy performance certificate; est. auditor quote band) | ~150–400 |
| Notary fee incl. 24 % VAT (2 × full fee, €50k–€300k sale; computed) | 208–1,135 |
| Notary fee from 1 Jan 2027 (941 SE table, same basis; computed) | 347–1,295 |
| Land Register state fee (owner entry, €50k–€300k; RLS table) | 53–350 |
| **Total transaction cost (buyer)** | **~0.5 %** of price without a mortgage on the 2026 tables; 0.64 % at €100k and 0.55 % at €300k from 1 Jan 2027 under 941 SE (computed; no transfer tax) |
| Roof renovation (est.) | ~8,000–20,000 |
| Asbestos abatement (est.) | ~2,000–10,000 |
| Energy retrofit (Class E → A) (est.) | ~25,000–60,000 |
| Insulation upgrade (est.) | ~5,000–15,000 |
| Heat pump (est.) | ~8,000–18,000 |
| Solar PV (5kW) (est.) | ~5,000–10,000 |

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

- **e-government / e-Notar digital property contracts** — real-estate deals can be notarised remotely by video bridge at the notary's discretion (laptop/desktop required), signing with ID-card, digi-ID, Mobile-ID, Smart-ID, residence-permit card or e-resident digi-ID (2026 data, source notar.ee — kaugtõestamine); €20 remote surcharge (NotTS § 2(2¹)) until 941 SE takes effect on 1 Jan 2027 (RT I, 12.11.2026, 1)
- **NO annual tax on buildings** — only land (maamaks, levied on the assessed land value; Maamaksuseadus § 1(1))
- **NO transfer tax** — only notary + land register fee (not unique in the EU: Czechia abolished its acquisition tax in 2020, Finanční správa); together ~0.5 % of price without a mortgage on the 2026 tables, 0.64 % at €100k and 0.55 % at €300k from 1 Jan 2027 under 941 SE (computed, see `--tax`)
- **Maamaks reform 2024-2026** — rates rising, municipality discretion expanded (caps 10–100 %, homeowner relief €0–1,000; EMTA); the 2026 land revaluation feeds land tax from 1 Jan 2028 (Maa- ja Ruumiamet)
- **VAT 20% → 22% (1 Jan 2024) → 24% (1 Jul 2025; open-ended since the Riigikogu passed 645 SE on 18 Jun 2025)** — major rise (2026 data, sources EMTA + Rahandusministeerium)
- **Tulumaks (income tax + CGT integrated) 22 % from 1 Jan 2025, unchanged in 2026** (2026 data, source EMTA tax-rates page)
- **Currency: EUR since 2011** (no FX risk for eurozone buyers)
- **Apartment prices flat in 2026**: MaRu apartment price index unchanged YoY in Q2 2026 (−2.2% QoQ); Tallinn secondary +4.3% YoY, new +1.1% (2026 data, source Maa- ja Ruumiamet)
- **Soviet-era panel buildings**: Khrushchyovka + Brezhnev — many in Tallinn Lasnamäe, Mustamäe, Õismäe — energy-inefficient + asbestos
- **No national short-let registration regime yet** — EU Reg (EU) 2024/1028 (registration-number rules where a Member State runs a registration procedure + platform data-sharing in those areas only) applies from 20 May 2026; MKM's Jun 2026 Tourism Act VTK proposes no STR register; MKM expects entry into force in 2027-2028 (ERR News 2026-06-25, secondary)
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

✅ **Fully populated**; fast-changing sections re-verified as of 2026-10-23, figures with no current primary source labelled est., secondary, curated wisdom or verify-at, and older-source figures marked 'may have changed since' (initial population 2026-04-25). Rental: Sep 2026 MKM STR position added 2026-09-24 in the October regwatch wave from ERR News (secondary); EU Reg 2024/1028 Art. 4/19, the MKM VTK and the Tallinn Old Town plan status re-read 2026-10-21 (December regwatch wave, run early). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry 941 SE (Notary Fees Act) re-checked 2026-10-28 against the adopted text on riigikogu.ee; see shared/regulatory-watch.md. Gap-closing pass (sources read 2026-11-03) closed `--tax`, `--rental`, `--risks`, `--mains` and Cost benchmarks against Riigi Teataja statute texts plus EMTA, riigikogu.ee, Eurostat, Statistikaamet and utility pages.
**Coverage check**: pricing (Statistikaamet + Maa- ja Ruumiamet + KV.ee), traffic (Transpordiamet), tax (maamaks reform 2024-2026 + VAT 22%→24% + 22% CGT), rental (EU Reg 2024/1028 from 20 May 2026; no national STR reg yet), work, risks (flood + radon + Baltic storms), mains all have primary government sources + cost benchmarks.
**Confidence**: HIGH for 2026 price benchmarks (Maa- ja Ruumiamet Q2 2026 review + statistics query, retrieved 2026-10-23; Narva / Kuressaare / Tartu-county rows are computed municipality-level medians); HIGH for work (Statistikaamet Q2 2026 wages + county medians, minimum wage €946 from 1 Apr 2026); HIGH for maamaks caps + homeowner relief (EMTA land-tax page); HIGH for VAT 24 % from 1 Jul 2025, open-ended since the Riigikogu vote of 18 Jun 2025, and 13 % accommodation VAT from 1 Jan 2025 (EMTA + Rahandusministeerium); HIGH for Tulumaks 22 % in 2026 (EMTA); HIGH for the pre-2027 notary fee computation (notar.ee worked example + NotTS § 22 table); HIGH for the Land Register state-fee table (RLS Annex 2 and §§ 74–76 on Riigi Teataja, unchanged in the 1 Jan 2027 redaction); HIGH for the post-2027 notary table under 941 SE (table and 1 Jan 2027 start read in the adopted text on riigikogu.ee and, on 2026-11-11, in the NotTS redaction in force from 1 Jan 2027, RT I, 12.11.2026, 3; proclaimed 6 Nov 2026); HIGH for e-government / cadastre sources (Maa- ja Ruumiamet + RIK); MEDIUM for short-let specifics (Reg (EU) 2024/1028 Art. 4/10/19 re-read on EUR-Lex 2026-10-23, no national regime; ERR 2027-2028 timing and the Sep 2026 MKM position secondary); MEDIUM for risks (flood, storm, radon and climate lines sourced to Keskkonnaagentuur / EGT / TTJA; radon comparison from UNSCEAR 2000 national survey means, older than 12 months; earthquake / wildfire ratings and build-era table are curated wisdom with sourced anchors; energy-certificate and sale-document rows sourced to Riigi Teataja; Keskkonnaportaal content unverified); MEDIUM for traffic (AKÖL examples from Transpordiamet 2025 counts; band cutoffs are calibration heuristics); LOW for the est. ranges (Tallinn / Tartu / Pärnu maamaks bills — est. with rate and implied-value inputs; septic / well, energy-certificate and construction / retrofit bands — no primary source); the Tallinn mains-connection fee is quoted per property (data not publicly available).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | 78 municipalities (agri.ee); Maa- ja Ruumiamet + geoportaal URL; e-Notar remote notarisation (notar.ee); example postcodes not checked |
| `--price` | 2026-10-23 | 2026-10-23 refresh wave | Benchmark table rebuilt from Maa- ja Ruumiamet Q2 2026 review + statistics query; Maa365.ee deprecated; agency-network list unranked |
| `--tax` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Maamaks, notary, land-register, VAT and Tulumaks lines checked against MaaMS, NotTS, RLS, KMS and TuMS (Riigi Teataja) + EMTA 2026 / 2027 tables; 941 SE adopted text, not yet in Riigi Teataja; typical bills est. with inputs; transfer-tax 'UNIQUE' corrected (Czechia) |
| `--rental` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | VÕS, TurS, TuMS, KMS and Tallinn Old Town plan (reg. no. 29) read on Riigi Teataja; MKM VTK (mkm.ee); ERR timing and MKM STR position kept secondary; PPA 24 h claim replaced by the TurS § 24 duty; tenant-protection comparison labelled wisdom |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Statistikaamet Q2 2026 wages + county medians; minimum wage €946 (1 Apr 2026); OÜ capital rule; VAT-registration citation corrected to KMS § 19(1) (Riigi Teataja); RTK state-jobs line unverified |
| `--risks` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Radon comparison corrected (UNSCEAR 2000 means); energy-certificate scale A–G since 1 Jun 2025 (energy-certificate regulation) and validity / disclosure rules (EhS §§ 66–67), Riigi Teataja; sale-document rows sourced to AÕS; earthquake / wildfire and build-era lines labelled curated with anchors; Keskkonnaportaal content unverified |
| `--climate` (projections under `--risks`) | 2026-10-23 | 2026-10-23 refresh wave | Four projection lines re-sourced to Keskkonnaagentuur 2014 national scenarios; rest of `--risks` in its own row |
| `--mains` | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Tallinna Vesi tariff (Konkurentsiamet decision) and utility names confirmed; coverage from Eurostat 2024; Tallinn connection fee data not publicly available (city refund rules sourced); septic / well ranges est. |
| Cost benchmarks (EE 2026) | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Notary rows computed from NotTS §§ 22–23 (2026 table) and the 941 SE adopted table (2027), land-register row from RLS Annex 2; energy-certificate and six construction / retrofit rows est., drift checked against Statistikaamet IA13 |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | KV.ee time-on-site lead (BCG / Similarweb, Apr 2026); City24 No.2; Maa365.ee deprecated |
| Caveats unique to EE | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | Price, short-let, tax and legal lines re-sourced (MaRu, EUR-Lex, EMTA, notar.ee, Riigi Teataja); 'UNIQUE' superlatives removed or corrected; panel-building, Ida-Virumaa, Korteriühistu and Pärnu-market lines not re-checked |

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
- **2026-10-23** — Refresh wave + audit corrections (facts changed / confirmed / unverifiable). Re-verified: Country profile 3 / 4 / 2; `--price` 18 / 5 / 1; `--work` 6 / 4 / 2; Common listing platforms 3 / 0 / 1; Caveats unique to EE 6 / 3 / 0 (price, short-let, tax and legal lines); `--climate` projections 4 / 0 / 0 (counted in `--risks`). Partly re-verified: `--tax` 14 / 12 / 4; `--rental` 6 / 6 / 4; `--risks` 11 / 4 / 5; `--traffic` 6 / 1 / 2; `--mains` 2 / 1 / 4; Cost benchmarks 3 / 0 / 7; Active fiscal incentives 3 / 0 / 1; Verification authorities 1 / 3 / 3; Source URL templates 2 / 6 / 1; Reddit / forum sources 0 / 2 / 3. Main changes: price table rebuilt from Maa- ja Ruumiamet Q2 2026 data (the earlier 2025 values could not be traced to a source); minimum wage €820 → €946 (from 1 Apr 2026); 78 municipalities after the Jõhvi–Toila merger; Maa-amet → Maa- ja Ruumiamet and Maanteeamet → Transpordiamet; Maa365.ee deprecated; VAT 24 % open-ended since 18 Jun 2025 (replaces the wrong "made permanent April-May 2026" date); notary and land-register fees computed from the pre-2027 statutory tables (buyer cost ~0.5 % without a mortgage), with bill 941 SE (passed 21 Oct 2026) changing the notary table; mortgage interest not deductible since 2024; short-let accommodation at 13 % VAT and taxed on gross income; traffic examples and calibration sourced to Transpordiamet 2025 AKÖL counts; flood hazard maps and climate projections sourced to Keskkonnaagentuur. Playbook-level date re-stamped to 2026-10-23 after a gap-closing pass closed `--tax`, `--rental`, `--risks`, `--mains` and Cost benchmarks; figures with no current primary source are labelled est., secondary, curated wisdom or verify-at, and older-source figures marked 'may have changed since'
  - Gap-closing pass (sources read 2026-11-03; facts confirmed / changed / relabelled): `--tax` 13 / 6 / 2; `--rental` 13 / 2 / 2; `--risks` 0 / 5 / 2; `--mains` 1 / 0 / 3; Cost benchmarks 2 / 2 / 7; Caveats unique to EE (tax / legal lines) 1 / 1 / 2 — total 30 / 16 / 18. Statute texts read on Riigi Teataja (MaaMS, NotTS, RLS, KMS, TuMS, VÕS, TurS, AÕS, EhS); 941 SE adopted text confirmed (1 Jan 2027 start, not yet proclaimed); 'UNIQUE' superlatives removed or corrected; radon comparison corrected (UNSCEAR 2000); energy-certificate scale A–G since 1 Jun 2025; PPA 24 h guest-registration claim replaced by the TurS § 24 duty; Tallinn mains-connection fee now data not publicly available; `--work` VAT-registration citation corrected to KMS § 19(1); maamaks typical bills, energy-certificate, septic / well and construction / retrofit bands kept est. with inputs or provenance
