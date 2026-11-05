# Slovakia 🇸🇰 — Property Due-Diligence Playbook

ISO2: `sk`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **PSČ (postcode)**: 5 digits in `NNN NN` format (e.g., `811 01` Bratislava, `040 01` Košice)
- **Admin levels**: 8 kraje → 79 okresy → 2,890 obce, of which 141 hold town status (mestá), plus 3 vojenské obvody (kraje / okresy per ŠÚ SR STATdata geography, 2026 data; obec / mesto counts per sk.wikipedia — secondary, verify at ŠÚ SR)
- **Currency**: **EUR (€)** — adopted 1 January 2009 (no FX risk vs CZ which still uses CZK)
- **Languages**: Slovak (official); Hungarian minority (south, ~9 % of population), small Rusyn / Ukrainian / Roma
- **Cadastre**: **ÚGKK SR** (Úrad geodézie, kartografie a katastra Slovenskej republiky)
- **Identifier**: parcela číslo + katastrálne územie + obec; LV (list vlastníctva) = title deed
- **CRITICAL note**: **No transfer tax (nadobúdacia daň) since 2005** — buyer-side costs very low like CZ
- **Civil code**: based on the older Czechoslovak Občiansky zákonník; reformed but no NOZ-style overhaul like CZ 2014
- **Bratislava-centric market**: Bratislavský kraj averaged 3,882 €/m² in 2Q 2026, 1.4–2.3× the other seven kraje (1,674 €/m² Nitriansky – 2,796 €/m² Košický) (2026 data, source NBS; ratio computed from kraj averages, flats + houses)

## Section: `--price`

### Primary sources (cadastre + price)

- **ÚGKK SR ZBGIS Mapa** (FREE, official map application):
  - Portal: `https://zbgis.skgeodesy.sk/mapka/sk/kataster`
  - Search parcels + buildings directly on the map
  - Layer toggling for cadastral data
- **CICA Portal** (informative LV viewing, free):
  - `https://kataster.vugk.sk` — the standard Public Cadastre System
  - For quick check of LV / parcela / building data
- **eSKN Portal** (electronic LV for legal proceedings):
  - `https://kataster.skgeodesy.sk/eskn-portal/`
  - Login via Slovensko.sk (eID)
- **Katasterportal.sk** (free informative LV download):
  - `https://www.katasterportal.com/`
  - Free LV PDF; not legally binding

**CRITICAL distinction**: CICA viewing is **informative only**. For mortgage, court, or notary purposes you need the **official electronic LV from eSKN** (paid via slovensko.sk eID).

### Price benchmark sources

- **Realitný barometer** (Realitná únia) — monthly market index: `https://www.realitnaunia.sk/realitny-barometer`
- **Realitymap.sk** — cenová mapa SK: `https://realitymap.sk`
- **NBS (Národná banka Slovenska)** — Residential property prices by region: `https://nbs.sk/en/statistics/selected-macroeconomics-indicators/residential-property-prices/residential-property-prices-by-regions/`
- **trh.sk štatistiky cien**: per okres breakdowns
- **Reality Radar cenová mapa**: `https://realityradar.eu/cenova-mapa-slovenska`

### Price benchmarks by kraj (NBS, 2Q 2026)

(Average price of residential property in €/m², flats + houses combined, per NBS "Ceny nehnuteľností na bývanie podľa krajov" (2026 data, source NBS — primary); YoY computed from the NBS 2Q 2025 figures. Kraj-level averages only, NOT obec- or parcel-level values. National split 2Q 2026: flats 3,430 €/m², houses 2,163 €/m².)

| Kraj | €/m² (2Q 2026) | YoY vs 2Q 2025 |
|---|---:|---:|
| **Bratislavský** | **3,882** | +9.4 % |
| Košický | 2,796 | +11.5 % |
| Prešovský | 2,310 | +6.1 % |
| Žilinský | 2,303 | +13.0 % |
| Trnavský | 2,064 | +6.6 % |
| Trenčiansky | 1,908 | +12.9 % |
| Banskobystrický | 1,841 | +7.4 % |
| Nitriansky | 1,674 | +11.4 % |
| **Slovensko** | **3,041** | **+9.5 %** |

### Asking prices for flats by okres (Reality Radar)

(Median asking price of flats for sale in €/m² per okres, Reality Radar cenová mapa, updated daily from 25,135 listings (2026 data, snapshot 2026-10-23, source realityradar.eu — listing-derived aggregator, seller-controlled asking prices; cross-check with NBS). Okres-level medians, NOT parcel-level values.)

| Okres (byty) | Median asking €/m² |
|---|---:|
| Bratislava I–V | 4,023–5,000 |
| Košice I–IV | 3,154–3,750 |
| Trnava | 3,213 |
| Žilina | 3,192 |
| Banská Bystrica | 3,125 |
| Prešov | 2,903 |
| Nitra | 2,702 |
| Trenčín | 2,641 |
| Lowest okresy (Medzilaborce / Poltár / Revúca) | 793 / 891 / 1,019 |
| **Slovensko** (median; mean 3,121) | **2,897** |

### Trend (2025–2026)

- Realitný barometer, September 2026: **3,479 €/m²** — flat prices in the 8 krajské mestá, from listing-portal asking prices plus Realitná únia's member transaction-price register (MoM −0.5 %, YoY +8.4 %; May 2025: 3,070 €/m², YoY +13.2 %) (2026 data, source Realitná únia — agents' association index, secondary; cross-check with NBS). A regional-capital flat index, NOT a national mean and NOT a Bratislava figure
- NBS national residential price YoY: +12.0 % in 4Q 2025, +11.3 % in 1Q 2026, +9.5 % in 2Q 2026 (2026 data, source NBS)

### Listing platforms

- **Nehnutelnosti.sk** — largest, full coverage: `https://www.nehnutelnosti.sk/`
- **Reality.sk**: `https://www.reality.sk/`
- **Topreality.sk**: `https://www.topreality.sk/`
- **Bazoš.sk** — privates, no agency: `https://reality.bazos.sk/`
- **Zoznam Realit** (agency listings): `https://www.zoznamrealit.sk/`
- **Realtbilliard** ❌ DEPRECATED — dead on 2026-10-23 (no realtbilliard.sk / .com domain resolves); verify listing coverage on Nehnutelnosti.sk / Reality.sk
- Agency networks: Bond Reality, M&M Reality, AVENUE (rebranded from Lexxus Reality — avenue.sk shows "AVENUE by team LEXXUS"), RE/MAX Slovakia (`https://www.remax-slovakia.sk/`; remax.sk redirects to an unrelated parcel-delivery site, checked 2026-10-23)

### Compute

1. Listing €/m² = listing price / úžitková plocha (or zastavaná plocha for non-byt)
2. Compare to NBS regional benchmark for the kraj
3. Compare to Realitná únia barometer monthly value
4. **Trap**: úžitková plocha (usable) vs zastavaná plocha (built-up footprint) vs podlahová plocha (floor area) — clarify which the listing uses
5. **Trap**: novostavby often advertise **bez DPH** (without VAT); the 5 % DPH rate on building supply is a retained pre-2025 rate limited to state-supported rental-housing projects — not a first-time-buyer rate (Finančná správa); verify the DPH applicable with the developer

---

## Section: `--traffic`

### Primary sources

- **SSC Celoštátne sčítanie dopravy 2022-2023**: `https://www.ssc.sk/sk/cinnosti/rozvoj-cestnej-siete/dopravne-inzinierstvo/celostatne-scitanie-dopravy-v-roku-2022-a-2023.ssc`
  - 2,752 sčítacích profilov on D, R, I. + II. triedy and part of III. triedy (2022-2023 data, source SSC)
  - Traffic increased +14.3 % since the 2015 census across all road types (2022-2023 data, source SSC press release 9 Nov 2023)
  - Latest national census: the SSC dopravné inžinierstvo page (updated 7 May 2025) lists CSD 2000, 2005, 2010, 2015 and 2022-2023, none later
- **Open data ArcGIS Hub** (CSD 2022-2023 shapefile published 15 Feb 2024 by Trnavský samosprávny kraj, CC BY 4.0): `https://hub.arcgis.com/datasets/3fce14460a694592b06641d67d83d6c3`
- **CDB (Cestná databanka)**: `https://www.cdb.sk/sk/Vystupy-CDB/Mapy-cestnej-siete-SR.alej`
  - Maps by správca (D + I + II + III triedy)
- **NDS (Národná diaľničná spoločnosť)** — autostrade live + counts: `https://ndsas.sk/`
- **Pan-European E-Road Census** (UN ECE / Eurostat) — Slovakia participant since 1980; conducted every 5 years (years ending in 0, 5)

### Key terms

- **RPDI (ročná priemerná denná intenzita dopravy)** — annual average daily traffic, in voz/24h (the term used in the SSC CSD 2022-2023 tables)
- Road categories: D (diaľnice), R (rýchlostné cesty), I/II/III triedy (state roads), miestne komunikácie

### Verdict bands

- 🟢 < 1,000 v/d (rural III. triedy, miestna komunikácia)
- 🟡 1,000–5,000 v/d (II. triedy, peripheral urban)
- 🟠 5,000–20,000 v/d (busy II/I. triedy, urban arterial)
- 🔴 > 20,000 v/d (D, R, urban core, major I. triedy)

### Bratislava extreme

- Highest RPDI in the eight SSC CSD 2022-2023 regional tables: D1 sčítací úsek 87023 (okres Bratislava II) — **101,407 voz/24h**, of which 18,284 nákladné vozidlá + autobusy (2022-2023 data, source SSC CSD table, Bratislavský kraj: `https://www.ssc.sk/files/documents/dopravne-inzinierstvo/csd_2022/ba/csd_tabulka_ba_2022_2023.pdf`); TASR via Startitup (secondary press, 15 Nov 2023) places the busiest stretch on the D1 bypass between the Gagarinova and Galvaniho junctions
- D1 sections in okresy Bratislava II / III / V: 64,482–101,407 voz/24h; D2 sections in okresy Bratislava IV / V: 16,801–94,387 voz/24h (2022-2023 data, same SSC table)
- City centre: heavy congestion at peak hours

### CSD 2022-2023 highlights

- **+14.3 %** average traffic intensity vs CSD 2015, all road types
- By class: I. triedy +13 % (avg 7,913 voz/deň), III. triedy +12.7 % (2,048), II. triedy +9.5 % (3,700), diaľnice + rýchlostné cesty +8.2 % (23,490) — D/R carry the highest volumes but grew the least
- Nákladná doprava +16.3 %, osobná +13.8 %, motocykle +35.3 %; mix 82.2 % osobné, 17.1 % nákladné, 0.7 % motocykle
- (2022-2023 data, source SSC press release 9 Nov 2023: `https://www.ssc.sk/files/documents/tlacove_spravy/ts_09_11_2023_dopravne_intenzity.pdf`)

---

## Section: `--tax`

### Annual property tax — Daň z nehnuteľností

**Set by each obec via VZN (Všeobecne záväzné nariadenie)** — extreme variation between obce.

Three components:

#### 1. Daň z pozemkov (land tax)

```
Daň = (hodnota pozemku za 1 m² × výmera pozemku v m²) × ročná sadzba
```

- Hodnota pozemku za m² per the annexes of Zákon 582/2004 Z. z.: príloha č. 1 for orná pôda / TTP (per katastrálne územie); príloha č. 2 for záhrady, zastavané plochy a nádvoria and ostatné plochy (**€1.32/m²** in obce ≤ 1,000 obyv. up to **€5.97/m²** in Bratislava) and for stavebné pozemky (**€13.27–€59.74/m²**); lesy / rybníky per znalecký posudok; the obec may substitute VZN values only in the cases of § 7 ods. 5–7 (2026 data, source Slov-Lex 582/2004)
- Land built over by a stavba or byt that is itself taxed is not subject to land tax (§ 6 ods. 2 písm. a)
- Statutory sadzba **0.25 %** (§ 8 ods. 1); the obec may raise or lower it by VZN, capped at 5× the statutory rate (1.25 %) for orná pôda / TTP, 10× (2.5 %) for lesy / rybníky, and 5× its own lowest VZN land rate for záhrady / zastavané plochy / stavebné pozemky (§ 8 ods. 2). Bratislava: 1.40–1.60 % záhrady / zastavané plochy / ostatné plochy, 1.30–1.50 % stavebné pozemky, 0.40 % orná pôda / TTP / lesy (2026 data, source bratislava.sk sadzby dane z nehnuteľností)

#### 2. Daň zo stavieb (building tax)

```
Daň = ročná sadzba/m² × výmera zastavanej plochy/m²
```

- Statutory base **0.033 €/m²** of zastavaná plocha (§ 12 ods. 1); the obec may change it by VZN and set different rates per druh stavby, capped at 10× the lowest building rate the VZN sets for the same area (§ 12 ods. 2), plus a príplatok za podlažie of up to **€0.33** for each floor above the first (§ 12 ods. 3) (2026 data, source Slov-Lex 582/2004)
- Sadzby per m² per VZN obce — rates differ by obec and no national dataset of VZN rates located, so check the obec's VZN. Rates in a sample, €/m²/rok (2026 data, sources VZN obce Veľké Pole č. 1/2025, VZN obce Bzovík č. 2/2025 and VZN obce Kamenica č. 2/2025, each in force from 1 Jan 2026, and the nitra.sk daň z nehnuteľností page, updated 4 Jul 2026, citing VZN Mesta Nitry č. 10/2014):
  - Stavby na bývanie (rodinný dom): **0.04** Veľké Pole, **0.067** Bzovík, **0.10** Kamenica, **0.75** Nitra
  - Stavby na poľnohospodársku produkciu: 0.07 Veľké Pole, 0.067 Bzovík, 0.10 Kamenica, 1.00 Nitra
  - Chaty a stavby na individuálnu rekreáciu: 0.30 Veľké Pole, 0.228 Bzovík, 0.20 Kamenica (the nitra.sk page gives no chata rate)
  - Samostatne stojace garáže: 0.17 Veľké Pole, 0.228 Bzovík, 0.25 Kamenica, 1.30 Nitra
  - Priemyselné stavby: 0.25 Veľké Pole, 0.228 Bzovík, 0.50 Kamenica, 6.00 Nitra
  - Príplatok za podlažie: 0.04 Veľké Pole and Kamenica, 0.0576 Bzovík, 0.30 Nitra
  - Bratislava is above these ranges: stavby na bývanie 1.20–1.35, chaty 3.40–5.25, garáže 2.25–3.00, priemyselné stavby 8.40–10.20 €/m²/rok by pásmo A–D, plus €0.33 per extra floor (2026 data, source bratislava.sk sadzby dane z nehnuteľností)

#### 3. Daň z bytov a nebytových priestorov

```
Daň = ročná sadzba/m² × výmera bytu/m²
```

- Statutory base **0.033 €/m²** of podlahová plocha (§ 16 ods. 1); the obec may change it by VZN, capped at 10× its lowest VZN byt rate (§ 16 ods. 2) (2026 data, source Slov-Lex 582/2004)
- VZN sadzba in the same sample: **0.04** Veľké Pole, **0.0634** Bzovík, **0.75** Nitra €/m²/rok (2026 data, sources as for daň zo stavieb above; check the obec's VZN)
- Bratislava: **1.20 €/m²** (pásmo A and B), **1.25** (pásmo C: Nové Mesto, Vinohrady, Ružinov, Trnávka, Petržalka), **1.35** (pásmo D: Staré Mesto, Nivy) (2026 data, source bratislava.sk sadzby dane z nehnuteľností)

### Example (Bratislava 100 m² byt at the 2026 rates of 1.20–1.35 €/m²/rok)

- 100 × 1.20 = **120 €/rok** (pásmo A / B) up to 100 × 1.35 = **135 €/rok** (pásmo D: Staré Mesto, Nivy)

### Example (small obec ≤ 1,000 obyv., rodinný dom with 150 m² zastavaná plocha on a 600 m² parcel)

- Stavba at Veľké Pole's 2026 rate for stavby na bývanie (0.04 €/m²; its VZN applies the príloha č. 2 land values for obce ≤ 1,000 obyv.): 150 × 0.04 = 6.00 €/rok
- Pozemok: only the 450 m² not built over is taxed (§ 6 ods. 2 písm. a); hodnota €1.32/m² (príloha č. 2) × Veľké Pole's 0.70 % for záhrady / zastavané plochy: 450 × 1.32 × 0.0070 = 4.16 €/rok (at the statutory 0.25 %: 1.49 €/rok)
- **Total: ~10 €/rok** (computed; 2026 data, source VZN obce Veľké Pole č. 1/2025; each obec's VZN sets the real figure — at Kamenica's 0.10 €/m² the stavba alone is 15 €/rok)

→ **Recurrent taxes on immovable property raised 0.41 % of GDP in Slovakia in 2023** — under half the OECD average of 0.95 %, and the 8th lowest of the 22 EU members of the OECD (Luxembourg, Estonia, Czechia, Austria, Lithuania, Hungary and Germany were lower); 0.48 % in 2024 (2023–2024 data, source OECD Revenue Statistics, dataset DF_RSOECD, tax code 4100). Residential bills: est. ~€4–€300/year (calibration, computed from the 2026 rates above: a 70 m² byt in Bzovík 70 × 0.0634 = €4.44; the Veľké Pole house ~€10; a 100 m² Bratislava byt €120–€135; a two-floor Bratislava rodinný dom with 150 m² zastavaná plocha on a 600 m² parcel 150 × (1.20–1.35 + 0.33) + 450 × 5.97 × 1.40–1.60 % = €267–€295).

### Transaction taxes (one-time at purchase)

- **Nadobúdacia daň: ABOLISHED 2005** — buyer pays no transfer tax; the former daň z prevodu a prechodu nehnuteľností (3 %, Zákon 554/2003 Z. z. § 5) applies only where the tax liability arose by the end of 2004 (§ 18, source Slov-Lex)
- Buyer pays:
  - **Notár / advokát**: est. 0.5–1.5 % of price (curated estimate). Calibration at a €200,000 price, before DPH (added at 23 % if the notár / advokát is a VAT payer): a notárska zápisnica of the purchase contract costs €900 (1 % of the first €20,000, 0.5 % up to €100,000, 0.3 % up to €200,000 — sadzobník Položka A bod 1, computed) and an osvedčenie pravosti podpisu €4 per signature (Položka C bod 3) (2026 data, source vyhláška 31/1993 Z. z., version in force from 17 Aug 2026, Slov-Lex); an advokát's fee is agreed with the client (§ 1 ods. 2 and § 2 vyhlášky 655/2004 Z. z.), and only without an agreement does the tarifná odmena apply — €824.93 per úkon at a €200,000 tarifná hodnota (§ 10 ods. 1: €486.29 + €6.64 × 51 started €3,319.39 steps above €33,193.92, computed), i.e. €2,474.79 for prevzatie a príprava, the contract and the návrh na vklad (§ 13a ods. 1 písm. a, i, c) (2026 data, source vyhláška 655/2004 Z. z., version in force from 1 Jan 2024, Slov-Lex)
  - **Kataster registration fee** (návrh na vklad): **€100**, or **€50** if filed electronically; decision within 15 days on request **€300** (**€150** if filed electronically) — Zákon 145/1995 Z. z., sadzobník položka 11, amounts in force since 1 Apr 2024 (2026 data, source Slov-Lex)
  - **Znalecký posudok** (appraisal, often required by bank): est. €100–€300 (curated estimate). Calibration: a znalec may agree the fee with a private client (§ 3 ods. 1 zákona 382/2004 Z. z.); without an agreement the tarifná podielová odmena for one stavba is PO = 0.2235 × VH^0.56, rounded up — €142 at a východisková hodnota of €100,000, €208 at €200,000 and €261 at €300,000 (§ 4 ods. 2–3 vyhlášky 491/2004 Z. z., computed); pozemky and príslušenstvo count as separate predmety, and the paušálna odmena and expenses come on top (2026 data, source Slov-Lex 382/2004 version in force from 1 Jul 2022 and 491/2004 version in force from 1 Aug 2018)
- Seller may pay **daň z príjmu na kapitálový zisk** (§ 8 ZDP) if sold within **5 years** of acquisition (or of removal from obchodný majetok); exempt after 5 years (§ 9 ods. 1 písm. a ZDP). Inherited in the direct line or from a spouse: the 5 years run from the decedent's acquisition (§ 9 ods. 1 písm. b). The gain falls in the § 4 ods. 1 písm. a base, taxed for 2026 at **19 %** up to €43,983.32, **25 %** up to €60,349.21, **30 %** up to €75,010.32 and **35 %** above (§ 15 písm. a bod 1: 154.8× / 212.4× / 264× the životné minimum of €284.13 valid on 1 Jan 2026 per Opatrenie 168/2025 Z. z. — thresholds computed). The former **2-year trvalý pobyt exemption** for a byt / rodinný dom applies only to property acquired by **31 Dec 2010** (§ 52j ods. 2). (2026 data, source Slov-Lex ZDP 595/2003, version in force from 1 Jan 2026)
- **Realitný maklér**: est. 3–5 % of price (curated market-practice estimate; no regulated tariff). Calibration: a Slovak law firm's guide gives 2–4 % of the property value as the usual sale commission, €2,000 on a €100,000 property (2022 data, source akmv.sk, law-firm article, secondary — rates/figures may have changed since), so the low end may sit below 3 %. The commission is payable by the záujemca who signed the sprostredkovateľská zmluva, in the agreed amount, if the result was achieved through the sprostredkovateľ (Občiansky zákonník 40/1964 Zb. § 774–775, in force until 30 Jun 2027); from 1 Jul 2027 the agreed provízia, otherwise the customary one, applies (§ 1053 of the new Občiansky zákonník 260/2026 Z. z.) (2026 data, source Slov-Lex)

### Total transaction cost

- **Buyer side: est. ~0.5–2 % of price** (calibration, computed at a €200,000 price before DPH from the figures above, taking the východisková hodnota as the price for the znalec: cadastre €100 + znalec podielová odmena €208 + either a notárska zápisnica €900 = €1,208 (0.6 %) or the advokát tariff for three úkony €2,474.79 = €2,782.79 (1.4 %); with 23 % DPH on the notár / advokát fee 0.7–1.7 %; agreed fees replace the tariffs, and no transfer tax applies)

### DPH (VAT) on new builds

**MAJOR 2025 reform** (konsolidačný balíček, zákon č. 278/2024 Z. z. čl. VII, promulgated 25 Oct 2024, effective 1 Jan 2025; 2026 data, source Slov-Lex 222/2004 § 27 and prílohy č. 7 / 7a, version in force 1 Jan–31 Dec 2026):
- **23 %** standard rate (up from 20 %)
- **19 %** reduced — NEW from 2025, replaces old 10 % bracket (food non-basic, electricity, restaurant non-alcoholic beverages)
- **5 %** super-reduced applies to **accommodation services (ubytovanie)**, restaurant food services, fitness centres, sports events, books — NEW from 2025; plus basic foodstuffs, medicines, medical devices, and supply / renovation of buildings in state-supported rental housing projects (štátom podporované nájomné bývanie, Zákon 222/2004 Z. z. § 27 ods. 3 písm. d / e, Finančná správa rates page, verified 2026-10-21). **Not** a new first-time-buyer bracket.
- Old rules (to 31 Dec 2024): 20 % standard; 10 % reduced for the goods of príloha č. 7 and the services of príloha č. 7a, including ubytovacie služby (abolished 1 Jan 2025; accommodation moved from 10 % to 5 %); 5 % only for state-supported rental housing (retained and widened) (2024 data, source Slov-Lex 222/2004 § 27 and príloha č. 7a, version in force 1 Jul–31 Dec 2024) — rates/figures may have changed since

### Future risk

- The obec can change daň z nehnuteľností rates, hodnota pozemku, the príplatok za podlažie and exemptions by VZN only with effect from 1 January (§ 98 Zákona 582/2004 Z. z.); some obce re-issue the VZN every year (Kamenica's VZN 2/2025 for 2026 replaced VZN 1/2024 for 2025), and Bratislava's VZN 13/2019 o dani z nehnuteľností has been amended by VZN 4/2020, 16/2023 and 6/2025 (2026 data, sources Slov-Lex 582/2004, kamenica.sk, bratislava.sk) — check the VZN in force for the year of purchase
- **Konsolidačný balíček** (zákon č. 278/2024 Z. z.) raised DPH from 1 Jan 2025; from 1 Jan 2026 zákon č. 261/2025 Z. z. and 385/2025 Z. z. moved high-sugar / high-salt foods from 19 % to 23 % (Finančná správa); neither the Finančná správa rates page nor the 1 Jan 2027 consolidated version of Zákon 222/2004 Z. z. § 27 on Slov-Lex shows a rate change for 2027 (verified 2026-10-23)
- Transfer tax: none applies to acquisitions since 2005 (Zákon 554/2003 Z. z. § 18: the act applies only where the tax liability arose by the end of 2004); taxes can be imposed only by or on the basis of a zákon (Ústava SR čl. 59 ods. 2, source Slov-Lex), so any re-introduction would need legislation — check pending bills on the NR SR site at https://www.nrsr.sk/

---

## Section: `--rental`

### Long-term residential

**Daň z príjmu z prenájmu (FO)**:
- Income from prenájom nehnuteľností is "príjem z prenájmu" under § 6 ods. 3 ZDP (a § 6 category, not § 8 "ostatné príjmy")
- First **€500/yr** of rental income (together with § 8 ods. 1 písm. a) income) is tax-exempt; above it only the excess is taxed (§ 9 ods. 1 písm. g) ZDP)
- **No paušálne výdavky** on rent: the 60 % / max €20,000 flat-rate expense (§ 6 ods. 10) covers only § 6 ods. 1–2 (and ods. 4) income — rental income takes documented (preukázateľné) expenses
- Rental income sits in the § 4 ods. 1 písm. a) base and is taxed progressively; the **15 %** rate applies only to § 6 ods. 1–2 (business and other self-employment) income ≤ €100,000, not to rent
- Tax brackets 2026 (ZDP § 15 as in force 1 Jan 2026; životné minimum €284.13 per opatrenie 168/2025 Z. z.; € thresholds computed) (2026 data, source slov-lex):
  - **19 %** up to **€43,983.32** ZD (154.8× životné minimum)
  - **25 %** up to **€60,349.21** (212.4×)
  - **30 %** up to **€75,010.32** (264×)
  - **35 %** above €75,010.32
  - 2025 tax year: 19 % up to €48,441.43 (176.8× životné minimum €273.99 per opatrenie 149/2024 Z. z.; ZDP § 15 as in force 1 Jan 2025), 25 % above
- Reportable annually (DAP fyzickej osoby)
- No social or health insurance contributions on § 6 ods. 3 rental income: it is not zárobková činnosť under § 3 ods. 1 zákon 461/2003 Z. z. (only § 5 and § 6 ods. 1–2 ZDP income) or § 10b ods. 1 zákon 580/2004 Z. z.; letting run under a živnosť is § 6 ods. 1 income (§ 6 ods. 3 ZDP covers rent only where it is not § 6 ods. 1 or § 5 income) and counts as SZČO income under both laws (2026 data, source slov-lex — 461/2003 as in force 1 Sep 2026, 580/2004 as in force 1 Jul 2026)

### Short-term rentals (krátkodobý prenájom / Airbnb / Booking)

**Status**: national short-term-rental register in force from 1 Jan 2027 (zákon č. 133/2026 Z. z.); no national night cap.

#### EU Regulation 2024/1028 → SK national law (zákon č. 133/2026 Z. z.)

(2026 data, source slov-lex — 133/2026 Z. z. vyhlásené znenie)
- **Register enacted**: zákon č. 133/2026 Z. z. o registri jednotiek pre poskytovanie služieb krátkodobého prenájmu ubytovania — adopted 2 Jun 2026, promulgated 18 Jun 2026, in force **1 Jan 2027**; the Ministerstvo cestovného ruchu a športu SR (MCRŠ) runs the register. Short-term rental = renting accommodation for less than one year (§ 1 ods. 2)
- **Registration**: the host registers each unit before first offering it via an online platform (§ 5 ods. 1), free of charge (§ 5 ods. 10); the record includes the LV number, katastrálne územie and parcela (§ 4 ods. 1 písm. b); a unit without a valid registration number may not be offered (§ 5 ods. 2); the ministry can order the platform to remove a non-compliant listing (§ 5 ods. 3); changes must be entered within 30 days (§ 5 ods. 4)
- **Existing hosts**: hosts offering via platforms until 31 Dec 2026 must register by **28 Feb 2027**; §§ 5, 10 and 11 do not apply to them until then (§ 14)
- **Public register fields**: unit address, unit type, start / end of platform provision and the registration number (§ 3 ods. 3); the maximum number of beds and guests is recorded (§ 4 ods. 1 písm. f) but not public
- **Fines**: natural persons €100–€1,000 (§ 10); entrepreneur or legal-entity hosts €1,000–€3,000 and platforms €3,000–€30,000 (§ 11); a repeat offence within 5 years can be fined up to twice the upper limit
- **Implementing vyhláška** (register structure, unit types) is delegated to MCRŠ under § 13 — check Zbierka zákonov for its promulgation
- **EU base reg 2024/1028: applies since 20 May 2026** across the EU and is directly applicable in all Member States (Art. 19) — rules on data collection and sharing for short-term rental services (2026 data, source EUR-Lex — Regulation (EU) 2024/1028, OJ L of 29 Apr 2024)

#### Živnosť (trade licence) for short-term letting

Renting property is a živnosť when services other than the basic ones tied to the rental are provided (§ 4 ods. 1 zákon 455/1991 Zb.) → **živnostenské oprávnenie** required (2026 data, source slov-lex — Živnostenský zákon as in force 17 Aug 2026):
- **Voľné živnosti** (príloha 4a): "Ubytovacie služby bez poskytovania pohostinských činností"; "Ubytovacie služby s poskytovaním prípravy a predaja jedál, nápojov a polotovarov ubytovaným hosťom v ubytovacích zariadeniach s kapacitou do 10 lôžok"; "Prenájom nehnuteľností spojený s poskytovaním iných než základných služieb spojených s prenájmom"
- **Viazaná živnosť** (príloha 2, qualification needed): "Ubytovacie služby v ubytovacích zariadeniach s prevádzkovaním pohostinských činností v týchto zariadeniach"
- Operating without the licence: fine up to **€1,659** for a voľná živnosť (§ 63), up to **€3,319** for a remeselná or viazaná živnosť (§ 64)
- Most professional Airbnb operations qualify as živnosť

#### DPH thresholds (2026; unchanged in the version in force from 1 Jan 2027)

- **€50,000** turnover in a calendar year → DPH platiteľ from 1 Jan of the following year (§ 4 ods. 1 písm. a) zákon 222/2004 Z. z.)
- **€62,500** turnover within the running calendar year → DPH platiteľ from the supply that crosses it (§ 4 ods. 1 písm. b))
- DPH rate for ubytovanie: **5 %** (accommodation services, CPA 55 — § 27 ods. 3 písm. b) + príloha 7a bod 2; reduced rate for accommodation from 2025) (2026 data, source slov-lex + Finančná správa)

#### Daň za ubytovanie (accommodation tax)

- Local tax: the obec sets the rate in € per person per night by VZN and may set different rates for parts of the obec (§ 40 zákon 582/2004 Z. z.); the base is capped at 60 nights per guest per operator per calendar year (§ 39); the operator must notify the obec of its capacity no later than the day accommodation starts (§ 41a) (2026 data, source slov-lex — 582/2004 as in force 1 Sep 2026; §§ 39–41a unchanged in the version in force from 1 Jan 2027)
- Bratislava: **€3.50**/person/night in Staré Mesto, **€3.00** in the other mestské časti (city-wide VZN hl. m. SR Bratislavy č. 4/2023, in force 1 Jul 2023, administered by the Magistrát) (2026 data, source bratislava.sk)
- Other obce set their own rate (2026 data, source each obec's VZN): Vysoké Tatry **€3.50** city-wide (VZN č. 5/2023, in force 1 Mar 2024, vysoketatry.sk); Košice **€3.50** (VZN č. 229, úplné znenie with the amendment in force 1 Jan 2025, kosice.sk); Liptovský Mikuláš **€1.50** (VZN č. 3/2025/VZN, in force 1 Jan 2026, mikulas.sk); Zuberec **€1.00**, or, if the operator agrees in writing, a flat €35 per bed per year, reduced to €15 per bed for priváty and family houses with an entrance shared with the household and €20 per bed for family-house annexes with their own entrance, family houses not permanently lived in that share a yard with the operator, and tourist hostels (VZN č. 02/2024 §§ 7, 11–12, in force 1 Jan 2025, zuberec.sk); rates differ by obec and change by VZN, so check the obec's current VZN
- Collected from the guest by the operator; settlement frequency set by each obec's VZN (Bratislava: monthly settlement, payment by the 15th of the following month)

#### Bratislava-specific

- No night cap in national law — zákon č. 133/2026 Z. z. sets registration duties only; a 60-days/yr cap proposal could not be traced to a primary source (verify with Magistrát hl. m. SR Bratislavy)
- No mestská časť-specific STR rule traced to a primary source: the verified MČ difference is the accommodation-tax rate set by the city (Staré Mesto €3.50, other MČ €3.00, city-wide VZN č. 4/2023) (2026 data, source bratislava.sk); verify any MČ rule with the miestny úrad and the Magistrát hl. m. SR Bratislavy
- National register from 1 Jan 2027 (zákon č. 133/2026 Z. z.) enables enforcement: unregistered listings can be ordered off platforms

### Strategic notes

- **Bratislava + Vysoké Tatry + spa towns (Piešťany, Bardejov)**: highest yields but biggest regulatory pressure (wisdom, not data — neither the yield ranking nor the regulatory-pressure ranking is sourced; STR registration rules are national, and one verified local difference is the obec's accommodation-tax rate: Bratislava €3.00–€3.50, Vysoké Tatry €3.50 — 2026 data, source bratislava.sk, vysoketatry.sk)
- **Eastern Slovakia (Košice + okolie)**: lower yields (wisdom, not data); the national STR register (from 1 Jan 2027, zákon č. 133/2026 Z. z.) applies here too, and Košice's accommodation tax (€3.50, VZN č. 229) equals Staré Mesto's (2026 data, source kosice.sk, bratislava.sk)
- **High Tatras** seasonal — winter ski + summer hiking; year-round demand
- **National STR register from 1 Jan 2027** (zákon č. 133/2026 Z. z.) — hosts already on platforms must register by 28 Feb 2027; new hosts register before listing
- **5 % DPH for accommodation from 2025** — significant tax win for accommodation operators

---

## Section: `--work=<profession>`

### Job platforms

- **Profesia.sk** — largest SK job board: `https://www.profesia.sk/`
- **Kariera.sk** (served at `https://kariera.zoznam.sk/`)
- **LinkedIn SK** (active in IT, finance, automotive); Indeed runs no Slovak country site (no sk.indeed.com on indeed.com/worldwide; indeed.sk is a parked domain — checked 2026-10-23)
- **ÚPSVaR** (Ústredie práce, sociálnych vecí a rodiny): `https://www.upsvr.gov.sk/` — official labour office

### Self-employment regimes

- **SZČO (samostatne zárobkovo činná osoba)**: standard self-employed (similar to CZ OSVČ)
- **Paušálne výdavky 60 %** of § 6 ods. 1–2 income, max €20,000/yr (ZDP § 6 ods. 10; 2026 data, source slov-lex) — NOT available for rental income
- Mandatory **sociálne poistenie** + **zdravotné poistenie**:
  - Min. odvody 2026: €121.92/mo zdravotné (16 % of the minimum base; €129.60/mo in 2027) + €303.11/mo sociálne (33.15 % of the €914.40 minimum base) (2026 data, source VšZP + Sociálna poisťovňa)
  - Sociálne poistenie arises only from 1 July (or 1 October) of the year after the income year, and only if that year's income before expenses exceeded 12× the minimum base (2024 income > €8,580 → insured from 1 Jul / 1 Oct 2025) (source Sociálna poisťovňa)
- **Voľná živnosť** (free trade): no qualifications, register at Živnostenský úrad
- **Viazaná / koncesovaná živnosť**: requires education / experience / license

### Salaried benchmarks (2025)

- Average gross monthly wage by kraj — workplace method, ISCP-based; averages run above medians (2025 data, source ŠÚ SR STATdata np3110rr):
  - Bratislavský €2,331 (okres Bratislava I €2,455)
  - Košický €1,793 (okres Košice I €1,915) · Žilinský €1,761 (okres Žilina €1,900)
  - Trnavský €1,738 · Trenčiansky €1,731 · Nitriansky €1,682 · Banskobystrický €1,645 · Prešovský €1,565
  - Slovensko €1,864
- **Minimálna mzda**: €915/mo gross in 2026 (€816 in 2025), **€972/mo from 1 Jan 2027** — set by the statutory automat at 60 % of the average nominal monthly wage two years earlier (2026 data, source MPSVR SR)
- 13. + 14. plat traditions vary by employer

### Catchment heuristics

- Within 30 min of okresné mesto: decent catchment
- Within 60 min of kraj capital: full salaried opportunity
- Eastern Slovakia (Prešov, Košice areas): lower wages but lower cost of living
- High Tatras + Liptov + Orava: thin labor markets, tourism-driven

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SVP MPO/MPR** (Mapy povodňového ohrozenia + rizika) | `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/` | Q10/Q100/Q1000 flood hazard + risk maps, 1:10,000, for areas with potentially significant flood risk (zákon 7/2010 § 6 ods. 1) — not every watercourse |
| **SVP MP-T portál** | `https://mpt.svp.sk/svp_vmapportal/` | Map portal supplementary |
| **SHMÚ Hydro stupne aktivity** | `https://www.shmu.sk/sk/?page=1&id=hydro_stpa` | Real-time flood activity stages 1-3 |
| **Minzp.sk povodňové mapy** | `https://www.minzp.sk/voda/ochrana-pred-povodnami/manazment-povodnovych-rizik/povodnove-mapy.html` | Ministry environment flood policy + maps |
| **ŠGÚDŠ Mapy prírodnej rádioaktivity** | `https://app.geology.sk/radio/` | Natural-radioactivity + radon-risk map application, 1:500,000 and 1:200,000 (ŠGÚDŠ; the former `apl.geology.sk/radio/` host was unreachable on 2026-10-23) |
| **ŠGÚDŠ map portal** | `https://www.geology.sk/maps-and-data/geophysical-maps/maps-of-natural-radioactivity/?lang=en` | Description + link to the natural-radioactivity / radon-risk maps (old `/mapovy-portal/` path 301-redirects here, 2026-10-23) |
| **Geoportal.gov.sk radon** | `https://geoportal.gov.sk/articles/radonove-riziko` | Mapa radónového rizika SR 1:500,000 — indicative overview (Národný geoportál) |
| **ÚVZ SAV seizmicita** (Ústav vied o Zemi SAV; Geofyzikálny ústav SAV merged into it 1 Jul 2015) | `https://www.seismology.sk/Maps/` | Seismic hazard maps for a 475-yr return period (PGA, GFÚ SAV 2012; macroseismic intensity) + epicentre map 1034–present |
| **Ústav vied o Zemi SAV** | `https://geo.sav.sk/` | Earthquake research + recent activity |
| **Geoportal KSK povodne** | `https://www.geoportalksk.sk/home/povodnove-ohrozenie-uzemia-ksk/` | Košický kraj specific |

### Flood zones (záplavové územia)

SVP publishes flood-hazard maps for the 3 statutory probability levels (zákon 7/2010 Z. z. § 6 ods. 2, version effective 1 Apr 2025):
- **Q10**: high probability (every 10 yrs) — frequent flooding, major restrictions
- **Q100**: medium probability (every 100 yrs) — insurance / building restrictions; the Q100 flood line delimits the inundačné územie (§ 20)
- **Q1000**: low probability (every 1,000 yrs or rarer, or a flood with an exceptionally dangerous course) — extreme event reference

Verify parcel-level via SVP's flood-hazard and flood-risk maps (MPO/MPR, scale **1:10,000**, prepared under Directive 2007/60/EC) — `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/`. **The page has no municipality or parcel search; open the linked *Mapový portál* and locate the parcel on the map** (2026-10-23 verified). The law describes hazard-map flood extents as indicative (*orientačne*, zákon 7/2010 § 6 ods. 3) — confirm parcel-level exposure with SVP / the okresný úrad.

### Radon zones (radónové riziko)

ŠGÚDŠ's radon-risk prognosis maps (1:500,000 and 1:200,000) are built from soil-gas radon measurements on 9,219 reference areas that cover Slovakia very unevenly, compiled from state-funded data up to 2008 (2008 data, source ŠGÚDŠ explanatory text *Mapa prognózy radónového rizika*, current published edition: `https://app.geology.sk/mapportal/img/pdf/gf500/Radiometria%20-%20Prirodna%20radioaktivita%20-%20Podny%20vzduch.pdf`) — figures may have changed since. Shares of Slovakia's area:
- **Nízke** (low) — 36.7 % (17,999 km²); mainly in the east, less in southern central and western SK (younger Quaternary / Tertiary basin sediments, flysch, central-SK andesites, Mesozoic carbonates)
- **Stredné** (medium) — 63.0 % (30,907 km²); mapped in most rock types
- **Vysoké** (high) — 0.3 % (130 km²), found in almost all geological units; areas named by ŠGÚDŠ:
  - **Spišsko-gemerské rudohorie** between Spišská Nová Ves, Rožňava and Košice — the most extensive (uranium mineralisation, Gemeric granites, past mining and undermining)
  - **Bratislava surroundings** (Záhorská Bystrica, Lamač, Rača; Pezinok–Pernek crystalline)
  - **Brezová and Vrbové** ("uranium dolomites")
  - **Považský Inovec** (wider Kálnica area)
  - **Levice surroundings**; central SK: Nová Baňa rhyolites, Malá Magura (Chvojnica), Dúbrava, Banská Bystrica and Švermovo
  - **Žilina** (Budatín–Zádubie) and **Liptovský Mikuláš**
  - East: **Trebišov**, **Michalovce**, **Zemplínske vrchy**

**Medium or high prognosis covers 63.3 % of Slovakia by area** (63.0 % + 0.3 %, computed). The map is a regional prognosis from soil gas, not a parcel or building measurement: **measure indoor radon** before purchase wherever it shows medium or high risk.

**Mitigation cost**: est. €1,500–€7,000 — VMC, sealing, sub-floor ventilation (2026-04 desk estimate; no official SK price source — get a contractor quote after the indoor measurement)

### Seismicity

Slovakia is seismically **more active than the Czech Republic and Poland** but less active than Hungary, Austria and Ukraine; 80 earthquakes a year on SK territory (rounded figure in the source), most recorded only by instruments. The most active areas are the Malé Karpaty, the Komárno area, central Slovakia (Horehronie), the Žilina area and Vihorlat (2021 data, source ÚVZ SAV seismologist Lucia Fojtíková interviewed by Webnoviny.sk / SITA, 8 May 2021 — press ⚠️, listed on ÚVZ SAV's `https://www.seismology.sk/Articles/`: `https://www.webnoviny.sk/na-slovensku-sposobili-zemetrasenia-velke-skody-hrozby-prichadzaju-aj-od-susednych-krajin/`) — figures may have changed since:

| Zone | Notable events |
|---|---|
| **Dobrá Voda (Malé Karpaty, north)** | **9 Jan 1906**, M ≈ 5.7 — the strongest instrumentally recorded earthquake on SK territory (Webnoviny 2021 ⚠️, quoting ÚVZ SAV); the last M ≥ 5.0 event in SK was here in 1930 (SAV news *Geovedci o zemetrasení v Turecku a Sýrii*, Feb 2023); Dobrá Voda and Komárno are named the most active zones (ÚVZ SAV via Denník N, Oct 2021 ⚠️) |
| **Komárno** | **1763** — strongest historical earthquake in SK, magnitude estimated 6.2–6.5, dozens of victims; a further earthquake twenty years later (1783) and aftershocks into the mid-19th century (ÚVZ SAV-hosted interview, 2026) |
| **Žilina** | **15 Jan 1858**, epicentral intensity 7–8° EMS-98; damaged all houses in Žilina (ESC 2016 abstract, Kysel / Labák / Hammerl); magnitude 5.1 per ÚVZ SAV (Webnoviny 2021 ⚠️) |
| **Stredné Slovensko (Horehronie / B. Bystrica)** | **5 Jun 1443**, M 5.7 — destroyed Banská Štiavnica and its mines, damage in Kremnica, Ľubietová and Prievidza (Webnoviny 2021 ⚠️, quoting ÚVZ SAV); further earthquakes expected mainly in the Vihorlat area and in central Slovakia (SAV geophysicist Peter Moczo, RTVS, 10 Oct 2023 ⚠️) |
| **Východné Slovensko (Vihorlat / Humenné / Vranov / Michalovce)** | **9 Oct 2023 Ďapalovce (okres Vranov nad Topľou)**: ML 4.9, depth 17.8 km, building damage (ÚVZ SAV-hosted interview, 2026) |

**21 Feb 2026, Rohovce (near Šamorín)**: ML 4.3, depth ~4–4.5 km, 50 aftershocks located by 13 Mar 2026; a steep fault zone parallel to the Malé Karpaty, separate from the Komárno focal zone (2026 data, source ÚVZ SAV-hosted interview with RNDr. Ján Madarás: `https://geo.sav.sk/files/2026/Tema-2026-ked-sa-trasie-slovensko.pdf`).

For most properties: 🟡 LOW–MEDIUM (zone-dependent). For Komárno + Vihorlat areas: 🟠 MEDIUM concern; for the rest: 🟢 negligible. These bands are a playbook judgment, not an official zoning (wisdom, not data). Calibration: ÚVZ SAV director general RNDr. Ján Madarás calls Slovakia a relatively very safe country, where a destructive earthquake like Komárno 1763 (M 6.2–6.5) may recur once in ~500 years against every 15–20 years in Greece or Italy, and says buildings built to the building standards should be designed for such an event (2026 data, source the ÚVZ SAV-hosted interview cited above).

Map: `https://www.seismology.sk/Maps/` (475-year return period PGA map, 2012 GFÚ SAV). For building design, seismology.sk says the map prepared for STN EN 1998-1/NA/Z2 (Eurokód 8) must be used instead.

### Build-era hazards

| Era | Hazards |
|---|---|
| **< 1948** | Lead, asbestos in roofing, weak foundations |
| **1948–1989 panelové domy** | Asbestos in joints + insulation, low-quality concrete (similar to CZ panelák problem) |
| **1948–1989 cihlové domy** | Better quality but asbestos + lead pipes likely |
| **1990–2000 "kvalitná privátna výstavba"** | DIY craftsmanship variability; possible no-permit work |
| **2000–2008** | Building boom — uneven quality |
| **Post-2008** | Modern energy + fire standards |
| **Post-2013** | Energy-efficiency standards tightening toward nZEB; nZEB (budova s takmer nulovou potrebou energie) mandatory for all new buildings from 31 Dec 2020 (public-authority buildings after 31 Dec 2018) — zákon 555/2005 § 4b ods. 1 (2025 data, source Slov-Lex) |

Rows other than Post-2013 are curated building-stock observations (wisdom, not data), not checked against a primary source; confirm on the actual building with a statik or znalec.

**Asbestos**: assume it may be present in pre-1995 buildings (curated heuristic, wisdom, not data; have suspect material sampled). Removal from buildings may be done only by a FO-podnikateľ or legal person holding an asbestos-removal oprávnenie from the public-health authority (or an equivalent EU / EEA / Swiss document), and ÚVZ SR publishes the list of authorised firms on its website (zákon 355/2007 Z. z. § 41 ods. 1 and § 5 ods. 4 písm. o–p; 2026 data, source Slov-Lex versions effective 1 Aug 2026 and 1 Jan 2027). Cost: est. €30–€80/m² of roof (2026-04 desk estimate; no official price source — get quotes from authorised firms).

### Mandatory diagnostics at sale

| Document | Required because | Penalty |
|---|---|---|
| **Energetický certifikát budovy (EC)** | All sales (with limited exceptions) | Up to **€2,000** (natural-person owner, § 12); €500–€3,000 (legal person / FO-podnikateľ, § 11 ods. 3) |
| **List vlastníctva aktuálny** | All sales (verify owner + ťarchy) | Informative view via ÚGKK `kataster.vugk.sk` / ZBGIS; legal-purpose LV via eSKN (katasterportal.com is a private map index, not an LV source) |
| **Snímok z katastrálnej mapy** | All sales | Free via ZBGIS |
| **Geometrický plán** | If parcela split / new build | Per-case |
| **Znalecký posudok** | Often required by bank for mortgage | est. €100–€300 (2026-04 desk estimate; no official price list — ask the znalec for a quote) |
| **Potvrdenie SVB o nedoplatkoch** | If apartment in SVB | At signing |
| **PPV (potvrdenie o platených úhradách)** | If apartment | At signing |

**EC platnosť**: max. 10 years; lapses earlier after construction works affecting energy performance (zákon 555/2005 § 7 ods. 7).
**EC obligation at sale / lease**: certification mandatory for buildings sold or leased after 1 Jan 2008 (Zákon 555/2005 Z. z. § 5 ods. 2 + § 14, original text); since 1 Jan 2013 (zákon 300/2012 Z. z.) § 8 requires the owner to hold an EC by the day the sale / lease contract is concluded (§ 8 ods. 1 písm. c) and to hand the valid EC to the new owner (§ 8 ods. 2 písm. c) (not 1 April 2025 — that date is the effective date of the new Stavebný zákon 25/2025 Z. z.; see below). Pokuta: natural-person owner up to **€2,000** (priestupok, § 12 ods. 2); legal person / FO-podnikateľ **€500–€3,000** (§ 11 ods. 3); both unchanged in the version effective 1 Jan 2027 (2025 data, source Slov-Lex 555/2005 versions effective 1 Jan 2006, 1 Jan 2013, 1 Apr 2025 and 1 Jan 2027, verified 2026-10-23).

**Stavebný zákon transition (1 April 2025)**: Zákon 50/1976 Zb. (old stavebný zákon) applied until 31 March 2025. From 1 April 2025 building regulation is **Zákon 25/2025 Z. z. (Stavebný zákon)**, which repealed the never-effective **Zákon 201/2022 Z. z. o výstavbe** (§ 86); obec remains the stavebný úrad (§ 15). Land-use planning: **Zákon 200/2022 Z. z. o územnom plánovaní** (core provisions effective 1 April 2024, remainder 1 April 2025). Zákon 46/2024 Z. z. (adopted 13 Feb 2024) amended 50/1976 for the transition. (2025 data, source Slov-Lex, verified 2026-10-23.) Authority: Úrad pre územné plánovanie a výstavbu SR `https://uupv.sk/`.

### Climate change projections (SHMÚ)

- Annual mean temperature, southern Slovakia: +0.7–0.9 °C by 2030, ~+2.0–3.0 °C by 2050, +3.5–6.0 °C by 2100 vs 1991–2020, depending on RCP scenario (EURO-CORDEX ensemble, RCP2.6–RCP8.5; source SHMÚ *Scenáre budúcej klímy* `https://www.shmu.sk/sk/?page=1069`, read 2026-10-23)
- More droughts, mainly in the southern half of SK (incl. Žitný ostrov lowlands) — spring + summer precipitation falling while temperatures rise (SHMÚ)
- Snow: fewer days with snow cover + lower mean snow depth (SHMÚ) → Vysoké Tatry snow less reliable at lower altitudes
- Heat waves: more frequent, longer + more intense; waves like 2003 / 2007 / 2015 expected 3–5× more often around 2050 (SHMÚ)
- Extreme rain events: more frequent + more intense; totals and intensities of short-duration heavy rainfall +3 % to +35 % depending on RCP and horizon (RCP2.6 2051–2100: +3 to +5 %; RCP8.5 2051–2100: +25 to +35 %) (SHMÚ)
- Wildfires: the MŽP SR adaptation strategy lists a rising forest-fire risk for the continental region (citing EEA 2017) and fires among forest-damage risks, but gives no projection for the Tatras, East SK or any other SK region; SHMÚ's scenarios page does not quantify fire risk for SK (2018 data, source MŽP SR *Stratégia adaptácie SR na zmenu klímy — aktualizácia 2018*: `https://www.minzp.sk/files/odbor-politiky-zmeny-klimy/strategia-adaptacie-sr-zmenu-klimy-aktualizacia.pdf`) — rates/figures may have changed since. A TU Zvolen methods paper expects areas prone to forest fires to spread to higher altitudes under the CCCM climate scenario, with marked changes south of the Zlatník climatic dividing line (Škvarenina & Vida, *Acta Facultatis Forestalis Zvolen* 51(3): 17–33, 2009, citing Balajka et al. 2005 — academic ⚠️: `https://lf.tuzvo.sk/sites/default/files/acta_51_3_2009_ce_ale.pdf`). Current fire danger: SHMÚ *Index požiarneho nebezpečenstva* `https://www.shmu.sk/sk/?page=2940`

---

## Section: `--mains`

### Major water operators (regional)

| Operator | Coverage |
|---|---|
| **BVS (Bratislavská vodárenská spoločnosť)** | Bratislava + western Slovakia: drinking water in 118 obcí, ~740,000 permanent customers (2026 data, source bvsas.sk *O spoločnosti*) |
| **TAVOS (Trnavská vodárenská spoločnosť)** | 66 cities and obce in Trnavský, Trenčiansky and Bratislavský kraje, ~51,000 supply points, ~180,000 inhabitants (figures as rounded by TAVOS); shareholders are 98 obce from okresy Trnava, Hlohovec, Piešťany and Nové Mesto nad Váhom; seat Piešťany (2026 data, source tavos.sk *O spoločnosti* + *Územné rozdelenie akcionárov*) |
| **ZsVS (Západoslovenská vodárenská spoločnosť)** | 11 okresy across Nitriansky, Trnavský + Trenčiansky kraje: Dunajská Streda, Galanta, Šaľa, Levice, Nové Zámky, Nitra, Zlaté Moravce, Topoľčany, Bánovce nad Bebravou, Partizánske, Komárno; drinking water to nearly 800,000 inhabitants (2026 data, source zsvs.sk *O spoločnosti*) |
| **StVS / StVPS (Stredoslovenská vodárenská spoločnosť / prevádzková)** | StVS owns the infrastructure in all okresy of Banskobystrický kraj + okres Prievidza; StVPS operates it (2026 data, source stvs.sk) |
| **SEVAK (Severoslovenské vodárne a kanalizácie)** | Okresy Žilina, Bytča, Kysucké Nové Mesto, Čadca (2026 data, source sevak.sk); the rest of Žilinský kraj has other operators, e.g. Liptovská vodárenská spoločnosť (Liptovský Mikuláš) |
| **VVS (Východoslovenská vodárenská spoločnosť)** | Košický + Prešovský kraje — the okresy listed under PVS below are served by PVS; VVS supplies nearly 1 million inhabitants, >2,000 employees (2026 data, source vodarne.eu *Spoločnosť*) |
| **PVS (Podtatranská vodárenská spoločnosť)** + operator PVPS | Okresy Poprad, Kežmarok, Stará Ľubovňa, Spišská Nová Ves, Levoča, Gelnica (2026 data, source pvsas.sk) |
| **TVK (Trenčianske vodárne a kanalizácie)** | Okresy Trenčín, Nové Mesto nad Váhom, Myjava (2026 data, source tvkas.sk *Pôsobnosť*) |
| Smaller obecné/mestské | Some smaller obce on local water utilities |

### Verification

- ZsVS connection guide (pripojenie na verejný vodovod): `https://www.zsvs.sk/sluzby/zivotna-situacia/pripojenie-na-verejny-vodovod-a-kanalizaciu`
- Or directly via obec website
- **Public water**: 2,420 of 2,890 obce (83.7 %) had a public vodovod in at least part of the obec at 31 Dec 2018; the other 470 rely on household wells. Lowest shares: Prešovský kraj (66.8 % of obce), okresy Snina (29.4 %), Medzilaborce (43.5 %) and Stropkov (44.2 %); in okresy Košice-okolie and Vranov nad Topľou almost half of inhabitants drink from household wells (2018 data, source MŽP SR *Plán rozvoja verejných vodovodov pre územie SR na roky 2021–2027*, `https://www.minzp.sk/voda/verejne-vodovody-verejne-kanalizacie/`) — figures may have changed since. Population on public water: 90.7 % (2024 data, source Eurostat `env_wat_pop`, `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_wat_pop?geo=SK&unit=PC`) — rates/figures may have changed since
- **Public sewer**: in operation in 1,128 obce (39.03 % of all obce) at 31 Dec 2018. Share of obce with sewer in operation by size, computed from the plan's Príloha č. 1 (leaving out 37 Bratislava / Košice city-district rows with no sewer flag): < 500 obyv. 141 / 1,126 = 12.5 %; 500–999 266 / 760 = 35.0 %; 1,000–1,999 337 / 570 = 59.1 %; ≥ 2,000 384 / 434 = 88.5 % (2018 data, source MŽP SR *Plán rozvoja verejných kanalizácií pre územie SR na roky 2021–2027*, same page) — figures may have changed since. Population on the public sewer: 72.2 % (2024 data, source Eurostat `env_ww_con`, category URB_CS *urban wastewater collecting system*, `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_ww_con?geo=SK&unit=PC`) — rates/figures may have changed since
- Obec-level coverage says nothing about the parcel: confirm the street has the network on the operator's network map or with the obec
- **Žumpa / domová ČOV rules**: in agglomerations over 2,000 EO municipal wastewater must go to the public sewer, except where a sewer brings no environmental benefit or would cost disproportionately much — there a watertight žumpa or small ČOV may be permitted; permits for a žumpa or small ČOV are issued only for a fixed term and are not extended once a public sewer is in operation; whoever stores wastewater in a žumpa must have it emptied to a ČOV by the sewer operator, the obec or an authorised hauler and show the receipts for up to the last two years when the obec or water authority asks (zákon 364/2004 Z. z. § 36 ods. 2 and 4; 2025 data, source Slov-Lex, version in force from 14 Oct 2025)
- Listing language:
  - "verejný vodovod" / "obecný vodovod" = mains water
  - "verejná kanalizácia" / "obecná kanalizácia" = mains sewer
  - "studňa" = own well (groundwater)
  - "žumpa" = cesspit / vault (no treatment)
  - "domová ČOV" = domestic wastewater treatment
  - "septik" = septic tank — septic tanks have not been permitted as an individual treatment system (MŽP SR sewer plan 2021–2027); check the permit

### Costs

| Scenario | Cost |
|---|---:|
| Operator charge for connecting to the public sewer (cena za pripojenie), ZsVS area | max €963.35 excl. DPH up to DN 200 (€1,184.92 with 23 % DPH, as listed by ZsVS); €1,285.63 excl. DPH for DN 250 and above (ÚRSO decision 0011/2024/V-KA of 13 Feb 2024, valid to 31 Dec 2027 unless ÚRSO approves a change) |
| Connection where available | est. €1,000–€3,000 |
| Mains drains construction (per parcel) if obec has trunk line | est. €2,000–€8,000 |
| Septik to mains conversion | est. €4,000–€10,000 |
| Domová ČOV (modern compliant) install | est. €4,000–€10,000 |
| Žumpa replacement | est. €2,000–€6,000 |
| Vŕtaná studňa (well) | est. €3,000–€8,000 |

The est. rows are 2026-04 desk estimates of contractor prices, not checked against any price list or primary source. They scale with prípojka and trench length, ground conditions and, for wells, drilling depth — get the operator's connection conditions and contractor quotes. Outside the ZsVS area, check the local operator's cenník for any connection charge.

---

## Cost benchmarks (SK 2026)

| Work | Cost (€) |
|---|---:|
| Energetický certifikát (rodinný dom) | est. €150–€350 |
| Energetický certifikát (bytový dom) | est. €300–€800 |
| Notár / advokát | est. 0.5–1.5 % of price (at €200,000 before DPH: notárska zápisnica €900; advokát default tariff €2,474.79 for three úkony — see `--tax`) |
| Cadastre registration fee (Kataster) | €100 (€50 e-filed); 15-day decision €300 (€150 e-filed) — 2026 data, source Zákon 145/1995 položka 11 |
| Znalecký posudok | est. €100–€300 (default podielová odmena for one stavba €142–€261 at a východisková hodnota of €100,000–€300,000 — see `--tax`) |
| **Daň z nehnuteľností (annual, residential)** | est. ~€4–€300 (computed examples in `--tax`) |
| Septik to mains | est. €4,000–€10,000 |
| Roof (terracotta tile, 200 m²) | est. €8,000–€18,000 |
| Asbestos removal (200 m² roof) | est. €4,000–€12,000 (the `--risks` figure of €30–€80/m² gives €6,000–€16,000 for 200 m²) |
| Energy retrofit (Class C → A) | est. €25,000–€80,000 |
| Radon retrofit (VMC + sealing) | est. €1,500–€7,000 |
| Building inspection (independent) | est. €300–€800 |
| **Total transaction cost (buyer side)** | **est. ~0.5–2 %** of price (computed at €200,000 in `--tax`) |

Rows marked est. without a tariff calibration are curated market estimates from the 2026-04 research, with no primary source located for certifier, contractor or inspection prices; treat them as order-of-magnitude figures and get written quotes. The cadastre fee is statutory; the notár, advokát and znalec calibrations use the statutory default tariffs, which an agreed fee replaces.

## Active fiscal incentives (2025)

- **Zelená domácnostiam II** (SIEA, Program Slovensko, EU co-financed) — PV panels, solar collectors, heat pumps, biomass boilers, wind turbines: contribution up to **50 %** of eligible costs, reserved first and paid to the household's account after installation (replacing the earlier vouchers); registration from 26 Oct 2026, reservation requests from 2 Nov 2026, €28.6M available. **Zelená solidarita**: vouchers up to **90 %** for low-income households / ZŤP (2026 data, source zelenadomacnostiam.sk)
- **Plyn-out** kotlíkové dotácie — unverified: no programme of this name appears on obnovdom.sk or zelenadomacnostiam.sk (checked 2026-10-23); boiler replacement (výmena kotla) and heat pumps are eligible measures under Obnov dom mini+ (below)
- **Obnov dom mini+** (SAŽP / MŽP SR, Modernizačný fond, €186M for 16,940 rodinné domy) — up to **€11,000** per rodinný dom for insulation, windows / doors, roof covering replaced with roof insulation, boiler replacement, heat pumps and heating controls; income test: household equivalised disposable income for 2024 ≤ €12,990 per member, except the eligible groups; 2nd round planned for January 2027. The earlier Plán obnovy calls are listed under „Archív plánu obnovy“ (2026 data, source obnovdom.sk)
- **Refundácia DPH** for first-time buyers — no primary source located (checked 2026-10-23); the 5 % DPH rate on buildings is limited to state-supported rental housing (Zákon 222/2004 Z. z. § 27 ods. 3 písm. d / e), so verify any refund scheme with Finančná správa before relying on it
- **Daňový bonus na zaplatené úroky** (§ 33a ZDP, úver na bývanie concluded from 1 Jan 2024): borrower aged 18–35 at application, average monthly income ≤ 1.6× the prior-year average wage; **50 %** of the interest paid, max **€1,200/yr**, for 5 consecutive years; own permanent housing only (2026 data, source Slov-Lex ZDP 595/2003)
- **5 % DPH** for accommodation services (FROM 2025) — major win for short-let (2026 data, source Finančná správa sadzby dane)
- **Obnova budov programu** Plán obnovy a odolnosti — €630M over 2024-2026 (not re-verified: planobnovy.sk could not be read for verification on 2026-10-23; the family-house calls are listed under „Archív plánu obnovy“ on obnovdom.sk)

## Common listing platforms

- **Nehnutelnosti.sk** — full extraction, largest market share
- **Reality.sk** — standard
- **Topreality.sk** — standard
- **Bazoš.sk** — privates, lowest commission (no agency)
- **Zoznam Realit** — secondary (agency listings); **Realtbilliard** ❌ DEPRECATED — dead on 2026-10-23 (no domain resolves); verify coverage on Nehnutelnosti.sk / Reality.sk
- **Bondreality, M&M, RE/MAX Slovakia (remax-slovakia.sk), AVENUE (ex-Lexxus)** — agency networks
- **NBS kraj prices + Realitymap.sk + Realitný barometer + Reality Radar** — for benchmarking, not listings

## Caveats unique to SK

- **No nadobúdacia daň since 2005** — buyer-side costs very low (~1–2 %); the cheapest-to-buy of the V4 + Western European countries
- **Daň z nehnuteľností very low** — typically €30–€300/yr (similar to CZ but EUR-denominated)
- **DPH reform 2025**: standard rate 20 % → 23 %, reduced rates 19 % and 5 % (2026 data, source Finančná správa); the 5 % rate on supply of buildings is a RETAINED pre-2025 rate limited to projects of state-supported rental housing (štátom podporované nájomné bývanie) — it is not a general housing rate, so verify the DPH applicable to a new-build purchase with the developer / Finančná správa
- **No NOZ-style major civil reform** — older Občiansky zákonník still applies; some "predkupné právo" surprises possible
- **Bratislava market is 1.5–2.5× the rest of SK** — extreme price gradient
- **Eastern Slovakia (Prešovský/Košický)** — much cheaper but lower liquidity + higher emigration
- **Tatry chaty** — special restrictions (TANAP National Park rules)
- **Energetický certifikát mandatory at sale**, penalty up to €2,000 for a private owner (Zákon 555/2005 Z. z. § 12 ods. 2) and €500–€3,000 for a company or FO-podnikateľ (§ 11 ods. 3) (2026 data, source Slov-Lex) — lower than CZ's cap of 200,000 CZK for a natural person (Zákon 406/2000 Sb. § 12 odst. 2 písm. a), 2026 consolidated text per zakonyprolidi.cz — secondary aggregator)
- **Bratislava + Komárno + Žilina seismicity** — higher than CZ; verify zone before buying older buildings
- **Hungarian-speaking south Slovakia** — listings often in Hungarian on local platforms
- **Panelové domy 1948–1989**: same hazards as CZ — asbestos in joints, low-quality concrete

## Reddit / forum sources

- **r/Slovakia** (English-friendly), **r/Bratislava**
- Slovak: **/r/Slovensko** equivalent forums
- **Refresher.sk**, **Profesia.sk komunita**
- Facebook: "Bývanie na Slovensku", "Reality bez realitky SK"
- **InYourPocket Bratislava, Slovakia.travel** — expat info
- **Spectator.sme.sk** — English-language SK news incl. property

## Verification authorities

| Authority | When to call |
|---|---|
| **Kataster** (Okresný úrad, katastrálny odbor) | LV verification, parcela verification, vlastník/ťarchy |
| **Obec / mesto / mestská časť** | Územný plán, daň z nehnuteľností (sadzby per VZN), kolaudácia (obec is the stavebný úrad and issues the kolaudačné osvedčenie — zákon 25/2025 § 15) |
| **Notár / advokát** | Final kúpna zmluva, escrow (notárska / advokátska úschova), ťarchy check |
| **Prevádzkovateľ verejného vodovodu** (regional water co.) | Mains drains verification |
| **Okresný úrad — odbor životného prostredia** | Záplavové územia, povolenia |
| **SHMÚ** | Hydrology + meteorology |
| **ŠGÚDŠ** | Geological / radon information |
| **ÚVZ SAV** (Ústav vied o Zemi SAV, Geofyzikálny odbor; GFÚ SAV merged into it 1 Jul 2015) | Seismic information |
| **SVB** (apartment owners' assoc.) | Bezdlžnosť, fond opráv stav |
| **Bytové družstvo** (if cooperative) | Different ownership rules |

## Quirks to know

- **Parcela registra "C" vs "E"**: registra C = current state, registra E = original (pre-collectivization). Some properties only on E — may need Registračné konanie to harmonize
- **CICA viewing free + informative**; eSKN = legally binding (paid via slovensko.sk)
- **Predkupné právo**: pre-emption rights common in inherited / cooperative properties — verify before signing; co-owners hold a statutory predkupné právo when a spoluvlastnícky podiel is transferred, except to a blízka osoba (Občiansky zákonník § 140, source Slov-Lex)
- **Susedské vzťahy** (neighbour rights / disputes) — CZ-similar legal framework
- **Vyznámenie zákazu zaťaženia** (encumbrance freeze) on LV = red flag
- **LV parts**: časť A = majetková podstata (parcely, stavby), časť B = vlastník / iná oprávnená osoba (incl. poznámky), časť C = ťarchy (vecné bremená, záložné práva, predkupné práva with in-rem effect; the debt amount is not shown) — check both B (poznámky) and C (Zákon 162/1995 Z. z. § 8 ods. 1 písm. b bod 2, source Slov-Lex)
- **Geodet vs notár roles**: geodet creates GP (geometric plan), notár handles transfer — both needed for parcela split
- **Land vs building**: separate legal objects in SK generally, not only in pre-1990 properties — "Stavby ... nie sú súčasťou pozemku" (Občiansky zákonník § 120 ods. 2, source Slov-Lex); check on the LV that the stavba and the parcel under it have the same owner (unlike post-NOZ CZ)
- **Žitný ostrov** groundwater protection zone — restrictions on industrial use
- **TANAP / NAPANT / Slovenský raj** national parks — strict construction limits

## Source URL templates

| Source | URL pattern |
|---|---|
| ÚGKK CICA (informative LV) | `https://kataster.vugk.sk` |
| ÚGKK eSKN (electronic LV, login) | `https://kataster.skgeodesy.sk/eskn-portal/` |
| ÚGKK ZBGIS map | `https://zbgis.skgeodesy.sk/mapka/sk/kataster` |
| Katasterportal.com (private index of cadastral-map links per obec, not ÚGKK; no LV download) | `https://www.katasterportal.com/` |
| Nehnutelnosti search | `https://www.nehnutelnosti.sk/vysledky/<obec>` · byty na predaj: `https://www.nehnutelnosti.sk/vysledky/byty/<obec>/predaj` (the old `/<region>/<okres>/<obec>/` path redirects to kraj-level results, 2026-10-23) |
| Reality.sk | `https://www.reality.sk/byty/<obec>/predaj/` (the old `/byty-na-predaj/<region>/<obec>/` path redirects to an all-types page; the slugs `bratislava` / `kosice` resolve to a single okres — Bratislava IV / Košice III — 2026-10-23) |
| Realitný barometer | `https://www.realitnaunia.sk/realitny-barometer` |
| NBS prices by region | `https://nbs.sk/en/statistics/selected-macroeconomics-indicators/residential-property-prices/residential-property-prices-by-regions/` |
| SSC sčítanie dopravy | `https://www.ssc.sk/sk/cinnosti/rozvoj-cestnej-siete/dopravne-inzinierstvo/celostatne-scitanie-dopravy-v-roku-2022-a-2023.ssc` |
| SVP povodňové mapy | `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/` |
| SHMÚ povodne aktivita | `https://www.shmu.sk/sk/?page=1&id=hydro_stpa` |
| ŠGÚDŠ radon mapy | `https://app.geology.sk/radio/` |
| Geoportal radon | `https://geoportal.gov.sk/articles/radonove-riziko` |
| ÚVZ SAV seismika (maps by former GFÚ SAV) | `https://www.seismology.sk/Maps/` |
| Slovensko.sk daň pozemkov | `https://www.slovensko.sk/sk/zivotne-situacie/zivotna-situacia/_dan-z-pozemkov/` |
| Finančná správa SR | `https://www.financnasprava.sk/` |
| ZsVS (water W. SK) | `https://www.zsvs.sk/` |
| BVS (water Bratislava) | `https://www.bvsas.sk/` |
| VVS (water E. SK) | `https://www.vodarne.eu/` |

## Leaving Slovakia — origin-country deregistration entry points

For SK-resident buyers moving abroad. **Doorway only** — see [`shared/cross-border.md`](../../shared/cross-border.md) for the framework + [`shared/home-tax.md`](../../shared/home-tax.md) for tax detail. Mandatory call-out: engage cross-border tax counsel in BOTH jurisdictions before moving the centre of vital interests.

| Register | Action | Authority | URL |
|---|---|---|---|
| Tax residence | Final-year daňové priznanie with foreign address per [Zákon 595/2003 Z. z.](https://www.slov-lex.sk/) o dani z príjmov § 2 písm. d); verify DTA tie-breaker if dual residence claimed by destination | Finančná správa SR | [financnasprava.sk](https://www.financnasprava.sk/) |
| Civil register (trvalý pobyt) | **Odhlásenie z trvalého pobytu** via municipal *ohlasovňa pobytu* per [Zákon 253/1998 Z. z. § 6](https://www.slov-lex.sk/) — required if no longer resident in SR | Obecný / mestský úrad | [minv.sk — ohlasovne pobytu](https://portal.minv.sk/wps/wcm/connect/sk/site/main/zivotne-situacie/Cudzinci/Hlasenie-pobytu-cudzincov) |
| Health insurance | Terminate verejné zdravotné poistenie per [Zákon 580/2004 Z. z.](https://www.slov-lex.sk/) — VšZP / Dôvera / Union; **Union and Dôvera are merging: the share purchase agreement signed 14 Jul 2026 was to take effect once the required approvals were obtained (union.sk). ÚDZS gave its prior consent on 30 Sep 2026 for Dôvera to acquire 100 % of Union's shares and voting rights (zákon 581/2004 Z. z.; ÚDZS press release 30 Sep 2026). The European Commission sent its opinion at the end of October 2026 with no objections, and Dôvera has been Union's 100 % shareholder since 30 Oct 2026; Union zdravotná poisťovňa still operates as a separate insurer and its insureds remain Union insureds until the two insurers merge (Dôvera, 29 Oct 2026; union.sk FAQ). The merger is expected by the end of June 2027 per union.sk, or approximately in summer 2027 per Dôvera — the parties' own estimates, not a fixed date. Union's insureds then become Dôvera insureds; anyone who does not want that can apply to another insurer by 30 Sep 2027, with the change effective 1 Jan 2028 (union.sk FAQ). The 2026 change-of-insurer window (application by 30 Sep 2026 for cover from 1 Jan 2027, per union.sk) has closed** (checked 2026-11-03); if EU/EEA/CH destination, S1 form bridges coverage | All-payor framework (**three payors — VšZP, Dôvera, Union (owned by Dôvera since 30 Oct 2026) — until the two insurers merge, expected by end-June 2027 per union.sk or summer 2027 per Dôvera; two after**) | [vszp.sk](https://www.vszp.sk/) · [dovera.sk](https://www.dovera.sk/) · [union.sk](https://www.union.sk/) |
| Social security | Sociálna poisťovňa coordination via S1 if EU/EEA/CH destination per [Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883); bilateral totalisation outside coordination zone | Sociálna poisťovňa | [socpoist.sk](https://www.socpoist.sk/) |
| **s.r.o. owner-manager** | If owner-manager moving abroad — **POEM / PE risk** under destination DTA Art. 4(3) + Art. 5; effective-management migration can make the s.r.o. treaty-resident in destination → destination corporate tax + SK exit-tax event. Engage **corporate-tax counsel BEFORE move**. | Slovenská komora daňových poradcov + destination tax counsel | [skdp.sk](https://www.skdp.sk/) |
| Slovakia-treaty register (DTA lookup) | Find the relevant SK-destination ZZDP + tie-breaker article + MLI matches | Ministerstvo financií SR — Zmluvy o zamedzení dvojitého zdanenia | [mfsr.sk — ZZDP](https://www.mfsr.sk/sk/dane-cla-uctovnictvo/priame-dane/dane-z-prijmu/zmluvy-zamedzeni-dvojiteho-zdanenia/zmluvy-zamedzeni-dvojiteho-zdanenia/) |

**Cross-link**: invoke `--cross-border` for the framework (DTA tie-breaker pointer + POEM/PE check + EU/EEA/CH free-movement clarification per [AFMP](https://www.fedlex.admin.ch/eli/cc/2002/243/en) / [EEA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)) / [Dir 2004/38/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0038)) and `--home-tax` for Slovakia-side detail.

## Status

✅ **Fully populated**; fast-changing sections re-verified as of 2026-10-23, figures with no current primary source labelled est., curated wisdom or verify-at (initial population 2026-04-25; health-insurance payor row corrected 2026-09-18 and updated 2026-10-23 and 2026-11-03 — ÚDZS gave prior consent on 30 Sep 2026, the European Commission raised no objection and Dôvera has owned 100 % of Union since 30 Oct 2026, but the two insurers have not merged yet; the Zákon 580/2004 and S1 limbs were not re-verified). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for cadastre sources, statutory tax rules (Slov-Lex texts of zákony 582/2004, 595/2003, 145/1995, 222/2004), kraj-level price benchmarks (NBS) and work figures (ŠÚ SR wages, Sociálna poisťovňa / VšZP minimum contributions). MEDIUM for short-let regulation: the national register under zákon č. 133/2026 Z. z. (adopted 2 Jun 2026, in force 1 Jan 2027; existing platform hosts register by 28 Feb 2027) applies EU Regulation 2024/1028 — an EU regulation in opt-in/opt-out mode per the European Commission, not a directive awaiting transposition — but the register is not running yet, no mestská časť-specific rule and no primary source for the Bratislava 60-day cap proposal were found, and daň za ubytovanie is set by each obec (Bratislava and four sampled obce read in their VZN). MEDIUM for per-obec daň z nehnuteľností rates (a sample of 2026 VZN plus Bratislava and Nitra, not a national dataset — check the obec's VZN) and for `--risks` (flood, radon and climate rest on SVP, ŠGÚDŠ, SHMÚ and MŽP SR; the radon data go up to 2008; part of the seismic history rests on press quoting ÚVZ SAV; the seismic bands are a playbook judgment and the build-era rows curated wisdom). LOW for the est. cost rows — Cost benchmarks, mains connection works, radon mitigation, asbestos removal, the `--risks` znalecký posudok row and the maklér commission (curated 2026-04 estimates or market practice, no primary source located); notár / advokát and znalec fees in `--tax` stay est. ranges calibrated against the statutory tariffs, and the ZsVS sewer-connection charge is ÚRSO-regulated.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-23 | 2026-10-23 refresh wave | NBS kraj series (2Q 2026) replaces the city table; listing-derived okres table labelled; cadastre + benchmark URLs checked; 5 % DPH compute step confirmed (Finančná správa) |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | ŠÚ SR 2025 kraj wages; minimum wage 2026 / 2027; SZČO minimum contributions (Sociálna poisťovňa, VšZP); ZDP § 6 ods. 10 flat-rate expenses; job-board URLs |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Portals live; Lexxus → AVENUE; RE/MAX at remax-slovakia.sk; Realtbilliard deprecated; "largest" share claim not verified |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | All 20 URLs fetched with content checked; listing templates re-derived; radon map host → app.geology.sk |
| `--tax` | 2026-10-23 | 2026-10-23 gap-closing pass | Estimated VZN ranges replaced by sourced 2026 rates (Veľké Pole, Bzovík, Kamenica, Nitra, Bratislava); small-obec example recomputed on a real VZN (~€10, was ~€31); "among the lowest in Europe" replaced by OECD Revenue Statistics (0.41 % of GDP, 2023); notár / advokát, znalec and buyer-side total stay est., calibrated against the statutory tariffs; maklér stays est. (market practice, no regulated tariff; secondary law-firm calibration); DPH old-rules and transfer-tax lines re-sourced to 222/2004 and 554/2003 |
| `--rental` | 2026-10-23 | 2026-10-23 gap-closing pass | No social / health contributions on § 6 ods. 3 rent (461/2003, 580/2004), EU 2024/1028 date (Art. 19), 582/2004 §§ 39–41a and the 2025 bracket inputs confirmed; the €0.50–€2.00 accommodation-tax range replaced by the VZN rates of Vysoké Tatry, Košice, Liptovský Mikuláš and Zuberec; MČ-rule and yield lines relabelled; 60-day cap stays labelled not traced |
| `--risks` | 2026-10-23 | 2026-10-23 gap-closing pass | Radon list and shares replaced from the ŠGÚDŠ explanatory text (2008 data) — rates/figures may have changed since; seismic history and active areas sourced to SAV and press quoting ÚVZ SAV (⚠️), bands labelled judgment; seismology.sk design-map note confirmed; build-era rows and asbestos heuristic labelled curated, removal-licence rule confirmed (355/2007 § 41); energy-certificate duty from 1 Jan 2008 confirmed; mitigation, roof and posudok costs est. |
| Climate projections (SHMÚ, in `--risks`) | 2026-10-23 | 2026-10-23 gap-closing pass | SHMÚ scenarios re-read (temperature, heat waves, heavy rain, snow cover, drought); the Tatras / East SK wildfire claim replaced by the MŽP SR adaptation strategy's continental-region risk; neither source gives an SK-regional projection |
| `--mains` | 2026-10-23 | 2026-10-23 gap-closing pass | TAVOS coverage confirmed on tavos.sk; obec-size heuristic replaced by MŽP SR plan counts (31 Dec 2018) and Eurostat 2024 shares; žumpa and small-ČOV rules from 364/2004 § 36; ÚRSO-regulated ZsVS sewer-connection charge added; contractor cost rows est. |
| Cost benchmarks (SK 2026) | 2026-10-23 | 2026-10-23 gap-closing pass | Kataster fee statutory (confirmed in the refresh); every other row labelled est.; notár / advokát, znalec, daň z nehnuteľností and buyer-side rows calibrated against tariffs or computed examples in `--tax`; contractor, certifier and inspection rows are curated 2026-04 estimates with no primary source located |

## Extension TODOs (deepen on first real run)

- [ ] Per-obec daň z nehnuteľností sadzby from VZN (need scraping per ~2,890 obec — start with top 50 mestá)
- [ ] CSD2022-2023 ArcGIS Hub data extraction workflow
- [ ] EU 2024/1028 SK national register walkthrough once portal launches
- [ ] Bratislava MČ Airbnb / krátkodobý prenájom rules per MČ
- [ ] Asbestos detection workflow for panelové domy (1948-1989)
- [ ] Predkupné právo + susedské vzťahy detection from LV
- [ ] Žitný ostrov + národné parky construction limits
- [ ] Hungarian-language listings (south Slovakia) — bilingual extraction

## Update history

- **2026-04-25** — Initial population
- **2026-10-23** — Refresh wave; `--price`, `--work`, Common listing platforms and Source URL templates re-verified (see Per-section verification). `--tax`, `--rental`, `--risks` and `--mains` were refreshed but not fully re-verified; the gap-closing pass (sub-bullet below) closed them, and the playbook-level date is re-stamped 2026-10-23: every fast-changing section is re-verified — `--price` and `--work` in the refresh, `--tax`, `--rental`, Cost benchmarks, `--risks` (with Climate projections) and `--mains` in the gap-closing pass — with figures that have no current primary source labelled est., curated wisdom or verify-at. Refresh counts (changed / confirmed / unverifiable): Country profile 2 / 2 / 4; `--price` 5 / 13 / 0; `--rental` 9 / 8 / 4; `--work` 8 / 4 / 0; Common listing platforms 1 / 7 / 1; Reddit / forum sources 0 / 3 / 5; `--tax` 10 / 9 / 14; Cost benchmarks 1 / 0 / 12; Active fiscal incentives 3 / 1 / 3; Caveats unique to SK 1 / 3 / 2; Quirks to know 3 / 1 / 2; `--traffic` 9 / 3 / 3; `--risks` 17 / 9 / 19; Climate projections (SHMÚ) 1 / 4 / 1; `--mains` 7 / 2 / 9; Verification authorities 5 / 2 / 1; Source URL templates 5 / 15 / 0. Main changes: NBS 2Q 2026 kraj price table replaces the 2025 city table; national short-term-rental register under zákon č. 133/2026 Z. z. from 1 Jan 2027 (registration by 28 Feb 2027 for existing platform hosts); rental income taxed under § 6 ods. 3 ZDP with the €500 exemption and the 2026 19 / 25 / 30 / 35 % brackets; kataster fee €100 (€50 e-filed), 15-day decision €300 (€150 e-filed); Bratislava daň z bytov 1.20–1.35 €/m²; Zelená domácnostiam II, Obnov dom mini+ and the § 33a bonus; energy-certificate duty at sale / lease dated to 1 Jan 2008 and Stavebný zákon 25/2025 Z. z. from 1 Apr 2025; SSC CSD 2022-2023 figures (2,752 profiles, +14.3 % vs 2015); SHMÚ temperature projections vs 1991–2020; water-operator coverage incl. PVS and TVK; Realtbilliard marked DEPRECATED; Union / Dôvera row updated with the ÚDZS consent of 30 Sep 2026 and the pending European Commission opinion; Confidence line no longer frames EU Regulation 2024/1028 as a transposition. Not verified and left as curated or est.: Hungarian minority share, radon high-zone list, seismic-zone descriptions, build-era rows, cost-benchmark rows, mains connection costs, VZN tax ranges, the Bratislava 60-day short-let cap proposal, Plyn-out, first-buyer Refundácia DPH, the Plán obnovy €630M figure and the Caveats "1.5–2.5×" Bratislava gradient.
  - Gap-closing pass, sources read 2026-11-03 (confirmed / changed / relabelled): `--rental` 4 / 1 / 3; `--tax` 1 / 5 / 6; Cost benchmarks 0 / 0 / 2; `--risks` 5 / 5 / 4; Climate projections (SHMÚ) 1 / 0 / 1; `--mains` 0 / 3 / 1 — all closed; total 11 / 14 / 17. Main changes: the €0.50–€2.00 accommodation-tax range replaced by four obec VZN rates, and the absence of social / health contributions on § 6 ods. 3 rent and the EU 2024/1028 date confirmed; the estimated VZN tax ranges replaced by sourced 2026 rates from sampled obce, the small-obec example recomputed on a real VZN (~€10, was ~€31), "among the lowest in Europe" replaced by the OECD figure (0.41 % of GDP in 2023), notár / advokát and znalec fees calibrated against the statutory tariffs and the buyer-side total re-based to est. ~0.5–2 %; radon shares and areas taken from ŠGÚDŠ, the seismic history sourced to SAV and press quoting ÚVZ SAV, and the seismic bands, build-era rows and asbestos heuristic labelled; the Tatras / East SK wildfire line replaced by the MŽP SR adaptation strategy's continental-region risk; TAVOS coverage confirmed, the obec-size mains heuristic replaced by MŽP SR 2018 counts and Eurostat 2024 shares, and the ÚRSO-regulated ZsVS sewer-connection charge added; Union / Dôvera payor row brought up to date (European Commission no objection, Dôvera 100 % shareholder of Union since 30 Oct 2026, merger expected by end-June 2027 per union.sk or summer 2027 per Dôvera).
