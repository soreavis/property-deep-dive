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
  - 2,757 sčítacích miest covered
  - Traffic increased +14 % since 2015 census across all road types
- **Open data ArcGIS Hub**: `https://hub.arcgis.com/datasets/3fce14460a694592b06641d67d83d6c3`
- **CDB (Cestná databanka)**: `https://www.cdb.sk/sk/Vystupy-CDB/Mapy-cestnej-siete-SR.alej`
  - Maps by správca (D + I + II + III triedy)
- **NDS (Národná diaľničná spoločnosť)** — autostrade live + counts: `https://ndsas.sk/`
- **Pan-European E-Road Census** (UN ECE / Eurostat) — Slovakia participant since 1980; conducted every 5 years (years ending in 0, 5)

### Key terms

- **TGM (Priemerná denná intenzita dopravy)** — Average Daily Traffic — same as Czech TGM
- Road categories: D (diaľnice), R (rýchlostné cesty), I/II/III triedy (state roads), miestne komunikácie

### Verdict bands

- 🟢 < 1,000 v/d (rural III. triedy, miestna komunikácia)
- 🟡 1,000–5,000 v/d (II. triedy, peripheral urban)
- 🟠 5,000–20,000 v/d (busy II/I. triedy, urban arterial)
- 🔴 > 20,000 v/d (D, R, urban core, major I. triedy)

### Bratislava extreme

- Bypass section between Gagarinova–Galvaniho intersections: **>100,000 vehicles/day** (per SSC Celoštátne sčítanie dopravy 2022-2023, listed above — among the busiest counted segments in SK)
- Bratislava ring D1/D2: 50,000–80,000 v/d typical
- City centre: heavy congestion at peak hours

### CSD 2022-2023 highlights

- +14 % vs 2015 across all road types
- D-network growth most pronounced
- Heavy vehicles +16 %, cars +13 %

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
- Sadzby per m² per VZN obce (est. ranges for smaller obce — unsourced; the Bratislava row is the sourced benchmark; check the obec's VZN):
  - Stavby na bývanie (rodinný dom): **~0.10 – 1.00 €/m²/rok**
  - Stavby na poľnohospodársku produkciu: ~0.05 – 0.20 €/m²/rok
  - Záhradné chaty / chaty na rekreáciu: ~0.30 – 2.00 €/m²/rok
  - Garáže: ~0.50 – 3.00 €/m²/rok
  - Priemyselné stavby: ~1.00 – 7.00 €/m²/rok
  - Bratislava is above these ranges: stavby na bývanie 1.20–1.35, chaty 3.40–5.25, garáže 2.25–3.00, priemyselné stavby 8.40–10.20 €/m²/rok by pásmo A–D, plus €0.33 per extra floor (2026 data, source bratislava.sk sadzby dane z nehnuteľností)

#### 3. Daň z bytov a nebytových priestorov

```
Daň = ročná sadzba/m² × výmera bytu/m²
```

- Statutory base **0.033 €/m²** of podlahová plocha (§ 16 ods. 1); the obec may change it by VZN, capped at 10× its lowest VZN byt rate (§ 16 ods. 2) (2026 data, source Slov-Lex 582/2004)
- VZN sadzba est. ~0.20 – 1.50 €/m²/rok (unsourced range; check the obec's VZN)
- Bratislava: **1.20 €/m²** (pásmo A and B), **1.25** (pásmo C: Nové Mesto, Vinohrady, Ružinov, Trnávka, Petržalka), **1.35** (pásmo D: Staré Mesto, Nivy) (2026 data, source bratislava.sk sadzby dane z nehnuteľností)

### Example (Bratislava 100 m² byt at the 2026 rates of 1.20–1.35 €/m²/rok)

- 100 × 1.20 = **120 €/rok** (pásmo A / B) up to 100 × 1.35 = **135 €/rok** (pásmo D: Staré Mesto, Nivy)

### Example (small obec ≤ 1,000 obyv., rodinný dom with 150 m² zastavaná plocha on a 600 m² parcel)

- Stavba (illustrative VZN rate 0.20 €/m², est.): 150 × 0.20 = 30 €/rok
- Pozemok: only the 450 m² not built over is taxed (§ 6 ods. 2 písm. a); hodnota €1.32/m² (príloha č. 2) × statutory 0.25 %: 450 × 1.32 × 0.0025 = 1.49 €/rok
- **Total: ~31 €/rok** (computed; the obec's VZN rates set the real figure)

→ **Daň z nehnuteľností in Slovakia is among the lowest in Europe** — est. ~€30–€300/year for residential (calibration: the worked examples above give ~€31 for a small-obec house and €120–€135 for a 100 m² Bratislava byt).

### Transaction taxes (one-time at purchase)

- **Nadobúdacia daň: ABOLISHED 2005** — buyer pays no transfer tax; the former daň z prevodu a prechodu nehnuteľností (3 %, Zákon 554/2003 Z. z. § 5) applies only where the tax liability arose by the end of 2004 (§ 18, source Slov-Lex)
- Buyer pays:
  - **Notár / advokát**: typically 0.5–1.5 % of price
  - **Kataster registration fee** (návrh na vklad): **€100**, or **€50** if filed electronically; decision within 15 days on request **€300** (**€150** if filed electronically) — Zákon 145/1995 Z. z., sadzobník položka 11, amounts in force since 1 Apr 2024 (2026 data, source Slov-Lex)
  - **Znalecký posudok** (appraisal, often required by bank): €100–€300
- Seller may pay **daň z príjmu na kapitálový zisk** (§ 8 ZDP) if sold within **5 years** of acquisition (or of removal from obchodný majetok); exempt after 5 years (§ 9 ods. 1 písm. a ZDP). Inherited in the direct line or from a spouse: the 5 years run from the decedent's acquisition (§ 9 ods. 1 písm. b). The gain falls in the § 4 ods. 1 písm. a base, taxed for 2026 at **19 %** up to €43,983.32, **25 %** up to €60,349.21, **30 %** up to €75,010.32 and **35 %** above (§ 15 písm. a bod 1: 154.8× / 212.4× / 264× the životné minimum of €284.13 valid on 1 Jan 2026 per Opatrenie 168/2025 Z. z. — thresholds computed). The former **2-year trvalý pobyt exemption** for a byt / rodinný dom applies only to property acquired by **31 Dec 2010** (§ 52j ods. 2). (2026 data, source Slov-Lex ZDP 595/2003, version in force from 1 Jan 2026)
- **Realitný maklér**: usually 3–5 % paid by seller

### Total transaction cost

- **Buyer side: ~1–2 % of price** (similar to CZ; far cheaper than IT/DE/UK)

### DPH (VAT) on new builds

**MAJOR 2025 reform** (konsolidačný balíček; effective 1 Jan 2025, source Zákon 222/2004 § amend + Grant Thornton SK + financnasprava.sk, 2026-05-27 verified):
- **23 %** standard rate (up from 20 %)
- **19 %** reduced — NEW from 2025, replaces old 10 % bracket (food non-basic, electricity, restaurant non-alcoholic beverages)
- **5 %** super-reduced applies to **accommodation services (ubytovanie)**, restaurant food services, fitness centres, sports events, books — NEW from 2025; plus basic foodstuffs, medicines, medical devices, and supply / renovation of buildings in state-supported rental housing projects (štátom podporované nájomné bývanie, Zákon 222/2004 Z. z. § 27 ods. 3 písm. d / e, Finančná správa rates page, verified 2026-10-21). **Not** a new first-time-buyer bracket.
- Old rules (to 31 Dec 2024): 20 % standard, 10 % reduced (abolished 1 Jan 2025; accommodation moved from 10 % to 5 %), 5 % reduced (retained and widened) — Finančná správa 8/DPH/2024/IM and 5/DPH/2024/I

### Future risk

- VZN changes by obec are common (annual review possible)
- **Konsolidačný balíček** (zákon č. 278/2024 Z. z.) raised DPH from 1 Jan 2025; from 1 Jan 2026 zákon č. 261/2025 Z. z. and 385/2025 Z. z. moved high-sugar / high-salt foods from 19 % to 23 % (Finančná správa); neither the Finančná správa rates page nor the 1 Jan 2027 consolidated version of Zákon 222/2004 Z. z. § 27 on Slov-Lex shows a rate change for 2027 (verified 2026-10-23)
- Re-introduction of nadobúdacia daň occasionally proposed (currently rejected)

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
  - 2025 tax year: 19 % up to €48,441.43 (176.8× životné minimum), 25 % above
- Reportable annually (DAP fyzickej osoby)
- No social/health insurance contributions (unless registered as živnostník)

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
- **EU base reg 2024/1028: applies 20 May 2026** across EU for data-sharing infrastructure

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

- Local tax: the obec sets the rate in € per person per night by VZN and may set different rates for parts of the obec (§ 40 zákon 582/2004 Z. z.); the base is capped at 60 nights per guest per operator per calendar year (§ 39); the operator must notify the obec of its capacity no later than the day accommodation starts (§ 41a) (2026 data, source slov-lex)
- Bratislava: **€3.50**/person/night in Staré Mesto, **€3.00** in the other mestské časti (city-wide VZN hl. m. SR Bratislavy č. 4/2023, in force 1 Jul 2023, administered by the Magistrát) (2026 data, source bratislava.sk)
- Other tourist destinations: €0.50–€2.00/night — rates/figures may have changed since (check each obec's VZN)
- Collected from the guest by the operator; settlement frequency set by each obec's VZN (Bratislava: monthly settlement, payment by the 15th of the following month)

#### Bratislava-specific

- No night cap in national law — zákon č. 133/2026 Z. z. sets registration duties only; a 60-days/yr cap proposal could not be traced to a primary source (verify with Magistrát hl. m. SR Bratislavy)
- Some MČ stricter than others
- National register from 1 Jan 2027 (zákon č. 133/2026 Z. z.) enables enforcement: unregistered listings can be ordered off platforms

### Strategic notes

- **Bratislava + Vysoké Tatry + spa towns (Piešťany, Bardejov)**: highest yields but biggest regulatory pressure
- **Eastern Slovakia (Košice + okolie)**: lower yields, less regulation
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
| **SVP MPO/MPR** (Mapy povodňového ohrozenia + rizika) | `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/` | Q10/Q100/Q1000 flood hazard + risk maps for all SK rivers |
| **SVP MP-T portál** | `https://mpt.svp.sk/svp_vmapportal/` | Map portal supplementary |
| **SHMÚ Hydro stupne aktivity** | `https://www.shmu.sk/sk/?page=1&id=hydro_stpa` | Real-time flood activity stages 1-3 |
| **Minzp.sk povodňové mapy** | `https://www.minzp.sk/voda/ochrana-pred-povodnami/manazment-povodnovych-rizik/povodnove-mapy.html` | Ministry environment flood policy + maps |
| **ŠGÚDŠ Geofyzikálne mapy radon** | `https://apl.geology.sk/radio/` | Radon natural radioactivity maps 1:50k–1:500k |
| **ŠGÚDŠ map portal** | `https://www.geology.sk/maps-and-data/mapovy-portal/geophysical-maps/maps-of-natural-radioactivity/?lang=en` | Direct access to scaled radon maps |
| **Geoportal.gov.sk radon** | `https://geoportal.gov.sk/articles/radonove-riziko` | Aggregated radon risk |
| **GFÚ SAV (Geofyzikálny ústav SAV) seizmicita** | `https://www.seismology.sk/Maps/` | Seismic hazard map (475-yr return period PGA) |
| **Ústav vied o Zemi SAV** | `https://geo.sav.sk/` | Earthquake research + recent activity |
| **Geoportal KSK povodne** | `https://www.geoportalksk.sk/home/povodnove-ohrozenie-uzemia-ksk/` | Košický kraj specific |

### Flood zones (záplavové územia)

SVP publishes maps for 3 probability levels:
- **Q10**: high probability (every 10 yrs) — frequent flooding, major restrictions
- **Q100**: medium probability (every 100 yrs) — insurance / building restrictions
- **Q1000**: low probability (every 1,000 yrs) — extreme event reference

Verify parcel-level via SVP's flood-hazard and flood-risk maps (MPO/MPR, scale **1:10,000**, prepared under Directive 2007/60/EC) — `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/`. **The page has no municipality or parcel search; open the linked *Mapový portál* and locate the parcel on the map** (2026-09-18 verified).

### Radon zones (radónové riziko)

ŠGÚDŠ classifies into:
- **Nízke** (low) — most of lowland Slovakia
- **Stredné** (medium) — transitional zones
- **Vysoké** (high) — primary problem areas:
  - **Strážovské vrchy** (Trenčiansky kraj)
  - **Považský Inovec** (Trenčín / Nitra)
  - **Malá Fatra** (Žilinský kraj)
  - **Spišsko-gemerské rudohorie** parts (Košický + Prešovský kraje)
  - **Hornádska kotlina** (Spiš region)
  - **Veporské vrchy** (granite belt central SK)

**Slovakia has elevated radon overall** (similar pattern to CZ), but slightly less severe than CZ on average. Granite-substrate areas always require **measurement** before purchase.

**Mitigation cost**: €1,500–€7,000 — VMC, sealing, sub-floor ventilation

### Seismicity

Slovakia is **more seismically active than CZ** — five recognized active zones:

| Zone | Notable events |
|---|---|
| **Dobrá Voda (Malé Karpaty, north)** | Ongoing microseismicity |
| **Komárno** | **1763 M 6.5** — historical major; 1783 aftershocks |
| **Žilina** | **1858 M 5.7** — recent reminder |
| **Stredné Slovensko (B. Bystrica)** | Ongoing low-level |
| **Východné Slovensko (Vihorlat / Humenné / Vranov / Michalovce)** | Recent Zemplín 2023 quake |

For most properties: 🟡 LOW–MEDIUM (zone-dependent). For Komárno + Vihorlat areas: 🟠 MEDIUM concern; for the rest: 🟢 negligible.

Map: `https://www.seismology.sk/Maps/` (475-year return period PGA map, 2012 GFÚ SAV).

### Build-era hazards

| Era | Hazards |
|---|---|
| **< 1948** | Lead, asbestos in roofing, weak foundations |
| **1948–1989 panelové domy** | Asbestos in joints + insulation, low-quality concrete (similar to CZ panelák problem) |
| **1948–1989 cihlové domy** | Better quality but asbestos + lead pipes likely |
| **1990–2000 "kvalitná privátna výstavba"** | DIY craftsmanship variability; possible no-permit work |
| **2000–2008** | Building boom — uneven quality |
| **Post-2008** | Modern energy + fire standards |
| **Post-2013 nZEB** | Energy efficiency standards tightening |

**Asbestos**: pre-1995 likely; obligatory remediation if friabile; cost €30–€80/m² roof.

### Mandatory diagnostics at sale

| Document | Required because | Penalty |
|---|---|---|
| **Energetický certifikát budovy (EC)** | All sales (with limited exceptions) | Up to **€2,000** |
| **List vlastníctva aktuálny** | All sales (verify owner + ťarchy) | Free via katasterportal |
| **Snímok z katastrálnej mapy** | All sales | Free via ZBGIS |
| **Geometrický plán** | If parcela split / new build | Per-case |
| **Znalecký posudok** | Often required by bank for mortgage | €100–€300 |
| **Potvrdenie SVB o nedoplatkoch** | If apartment in SVB | At signing |
| **PPV (potvrdenie o platených úhradách)** | If apartment | At signing |

**EC platnosť**: 10 years.
**EC obligation at sale / lease since 2013** under Zákon 555/2005 Z. z. § 7, § 8 (not 1 April 2025 — that date is the new Stavebný zákon 201/2022 effective date; see below). Pokuta **€500–€3,000** under § 12. (2026-05-27 verified, source SIEA)

**Stavebný zákon transition (1 April 2025)**: Zákon 50/1976 Zb. zrušený; replaced by **Zákon 201/2022 Z. z. o výstavbe** and **Zákon 200/2022 Z. z. o územnom plánovaní** (effective 1 April 2025). Late-2024 bridge novela Zákon 46/2024. Source: Úrad pre územné plánovanie a výstavbu SR `https://uupv.sk/`.

### Climate change projections (SHMÚ)

- +1.5–3.0 °C by 2050 vs 1981–2010 baseline (RCP scenario)
- More droughts (esp. Žitný ostrov, lowland SK)
- Vysoké Tatry snow → less reliable lower altitudes
- Heat waves: longer + more intense
- Extreme rain events: more frequent
- Wildfires: rising in Tatras + East SK forests

---

## Section: `--mains`

### Major water operators (regional)

| Operator | Coverage |
|---|---|
| **BVS (Bratislavská vodárenská spoločnosť)** | Bratislavský kraj |
| **TAVOS (Trnavská vodárenská spoločnosť)** | Trnava + okolie |
| **ZsVS (Západoslovenská vodárenská spoločnosť)** | Nitriansky kraj parts: Dunajská Streda, Galanta, Šaľa, Levice, Nové Zámky, Nitra, Zlaté Moravce, Topoľčany, Bánovce nad Bebravou, Partizánske |
| **StVS / StVPS (Stredoslovenská vodárenská spoločnosť / prevádzková)** | Banskobystrický kraj |
| **SEVAK (Severoslovenské vodárne a kanalizácie)** | Žilinský kraj |
| **VVS (Východoslovenská vodárenská spoločnosť)** | Košický + Prešovský kraje (>2,000 employees) |
| Smaller obecné/mestské | Some smaller obce on local water utilities |

### Verification

- ZsVS-style coverage portal: `https://www.zsvs.sk/sluzby/zivotna-situacia/pripojenie-na-verejny-vodovod-a-kanalizaciu`
- Or directly via obec website
- **Most populated obce > 1,000 obyv have mains**; **vesnice < 500 obyv often lack mains sewer**
- Listing language:
  - "verejný vodovod" / "obecný vodovod" = mains water
  - "verejná kanalizácia" / "obecná kanalizácia" = mains sewer
  - "studňa" = own well (groundwater)
  - "žumpa" = cesspit / vault (no treatment)
  - "domová ČOV" = domestic wastewater treatment
  - "septik" = septic tank

### Costs

| Scenario | Cost |
|---|---:|
| Connection where available | €1,000–€3,000 |
| Mains drains construction (per parcel) if obec has trunk line | €2,000–€8,000 |
| Septik to mains conversion | €4,000–€10,000 |
| Domová ČOV (modern compliant) install | €4,000–€10,000 |
| Žumpa replacement | €2,000–€6,000 |
| Vŕtaná studňa (well) | €3,000–€8,000 |

---

## Cost benchmarks (SK 2026)

| Work | Cost (€) |
|---|---:|
| Energetický certifikát (rodinný dom) | €150–€350 |
| Energetický certifikát (bytový dom) | €300–€800 |
| Notár / advokát | 0.5–1.5 % of price |
| Cadastre registration fee (Kataster) | €100 (€50 e-filed); 15-day decision €300 (€150 e-filed) — 2026 data, source Zákon 145/1995 položka 11 |
| Znalecký posudok | €100–€300 |
| **Daň z nehnuteľností (annual, residential)** | €30–€300 typical |
| Septik to mains | €4,000–€10,000 |
| Roof (terracotta tile, 200 m²) | €8,000–€18,000 |
| Asbestos removal (200 m² roof) | €4,000–€12,000 |
| Energy retrofit (Class C → A) | €25,000–€80,000 |
| Radon retrofit (VMC + sealing) | €1,500–€7,000 |
| Building inspection (independent) | €300–€800 |
| **Total transaction cost (buyer side)** | **~1–2 %** of price |

## Active fiscal incentives (2025)

- **Zelená domácnostiam II** (SIEA, Program Slovensko, EU co-financed) — PV panels, solar collectors, heat pumps, biomass boilers, wind turbines: contribution up to **50 %** of eligible costs, reserved first and paid to the household's account after installation (replacing the earlier vouchers); registration from 26 Oct 2026, reservation requests from 2 Nov 2026, €28.6M available. **Zelená solidarita**: vouchers up to **90 %** for low-income households / ZŤP (2026 data, source zelenadomacnostiam.sk)
- **Plyn-out** kotlíkové dotácie — unverified: no programme of this name appears on obnovdom.sk or zelenadomacnostiam.sk (checked 2026-10-23); boiler replacement (výmena kotla) and heat pumps are eligible measures under Obnov dom mini+ (below)
- **Obnov dom mini+** (SAŽP / MŽP SR, Modernizačný fond, €186M for 16,940 rodinné domy) — up to **€11,000** per rodinný dom for insulation, windows / doors, roof covering replaced with roof insulation, boiler replacement, heat pumps and heating controls; income test: household equivalised disposable income for 2024 ≤ €12,990 per member, except the eligible groups; 2nd round planned for January 2027. The earlier Plán obnovy calls are listed under „Archív plánu obnovy“ (2026 data, source obnovdom.sk)
- **Refundácia DPH** for first-time buyers — no primary source located (checked 2026-10-23); the 5 % DPH rate on buildings is limited to state-supported rental housing (Zákon 222/2004 Z. z. § 27 ods. 3 písm. d / e), so verify any refund scheme with Finančná správa before relying on it
- **Daňový bonus na zaplatené úroky** (§ 33a ZDP, úver na bývanie concluded from 1 Jan 2024): borrower aged 18–35 at application, average monthly income ≤ 1.6× the prior-year average wage; **50 %** of the interest paid, max **€1,200/yr**, for 5 consecutive years; own permanent housing only (2026 data, source Slov-Lex ZDP 595/2003)
- **5 % DPH** for accommodation services (FROM 2025) — major win for short-let (2026 data, source Finančná správa sadzby dane)
- **Obnova budov programu** Plán obnovy a odolnosti — €630M over 2024-2026 (not re-verified: planobnovy.sk returned 404 on 2026-10-23; the family-house calls are listed under „Archív plánu obnovy“ on obnovdom.sk)

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
| **Kataster** (Okresný úrad — odbor katastrálny) | LV verification, parcela verification, vlastník/ťarchy |
| **Obec / mesto / mestská časť** | Územný plán, daň z nehnuteľností (sadzby per VZN), kolaudácia |
| **Notár / advokát** | Final compravendita, escrow, ťarchy check |
| **Provozovateľ vodovodu** (regional water co.) | Mains drains verification |
| **Okresný úrad — odbor životného prostredia** | Záplavové územia, povolenia |
| **SHMÚ** | Hydrology + meteorology |
| **ŠGÚDŠ** | Geological / radon information |
| **GFÚ SAV** | Seismic information |
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
| Katasterportal (free download) | `https://www.katasterportal.com/` |
| Nehnutelnosti search | `https://www.nehnutelnosti.sk/<region>/<okres>/<obec>/` |
| Reality.sk | `https://www.reality.sk/byty-na-predaj/<region>/<obec>/` |
| Realitný barometer | `https://www.realitnaunia.sk/realitny-barometer` |
| NBS prices by region | `https://nbs.sk/en/statistics/selected-macroeconomics-indicators/residential-property-prices/residential-property-prices-by-regions/` |
| SSC sčítanie dopravy | `https://www.ssc.sk/sk/cinnosti/rozvoj-cestnej-siete/dopravne-inzinierstvo/celostatne-scitanie-dopravy-v-roku-2022-a-2023.ssc` |
| SVP povodňové mapy | `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/` |
| SHMÚ povodne aktivita | `https://www.shmu.sk/sk/?page=1&id=hydro_stpa` |
| ŠGÚDŠ radon mapy | `https://apl.geology.sk/radio/` |
| Geoportal radon | `https://geoportal.gov.sk/articles/radonove-riziko` |
| GFÚ SAV seismika | `https://www.seismology.sk/Maps/` |
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
| Health insurance | Terminate verejné zdravotné poistenie per [Zákon 580/2004 Z. z.](https://www.slov-lex.sk/) — VšZP / Dôvera / Union; **Union and Dôvera are merging: the purchase agreement was signed 14 Jul 2026 and takes effect once the required institutional approvals are obtained, with Union's insureds transferring automatically to Dôvera from 1 January 2027 unless they file a change-of-insurer application by 30 September** (2026-09-18 verified); if EU/EEA/CH destination, S1 form bridges coverage | All-payor framework (**two payors from 1 Jan 2027 if the merger completes**) | [vszp.sk](https://www.vszp.sk/) · [dovera.sk](https://www.dovera.sk/) · [union.sk](https://www.union.sk/) |
| Social security | Sociálna poisťovňa coordination via S1 if EU/EEA/CH destination per [Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883); bilateral totalisation outside coordination zone | Sociálna poisťovňa | [socpoist.sk](https://www.socpoist.sk/) |
| **s.r.o. owner-manager** | If owner-manager moving abroad — **POEM / PE risk** under destination DTA Art. 4(3) + Art. 5; effective-management migration can make the s.r.o. treaty-resident in destination → destination corporate tax + SK exit-tax event. Engage **corporate-tax counsel BEFORE move**. | Slovenská komora daňových poradcov + destination tax counsel | [skdp.sk](https://www.skdp.sk/) |
| Slovakia-treaty register (DTA lookup) | Find the relevant SK-destination ZZDP + tie-breaker article + MLI matches | Ministerstvo financií SR — Zmluvy o zamedzení dvojitého zdanenia | [mfsr.sk — ZZDP](https://www.mfsr.sk/sk/dane-cla-uctovnictvo/priame-dane/dane-z-prijmu/zmluvy-zamedzeni-dvojiteho-zdanenia/zmluvy-zamedzeni-dvojiteho-zdanenia/) |

**Cross-link**: invoke `--cross-border` for the framework (DTA tie-breaker pointer + POEM/PE check + EU/EEA/CH free-movement clarification per [AFMP](https://www.fedlex.admin.ch/eli/cc/2002/243/en) / [EEA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)) / [Dir 2004/38/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0038)) and `--home-tax` for Slovakia-side detail.

## Status

✅ **Fully populated** as of 2026-04-25 (health-insurance payor row corrected 2026-09-18 — the Union / Dôvera merger is conditional on approvals and has not completed; the Zákon 580/2004 and S1 limbs were not re-verified). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + cadastre + risk sources (all primary state agencies, multi-source corroborated). MEDIUM for short-let regulation (in transition: EU 2024/1028 SK transposition + 5 % DPH adjustment 2025 + Bratislava-specific rules pending).

## Extension TODOs (deepen on first real run)

- [ ] Per-obec daň z nehnuteľností sadzby from VZN (need scraping per ~2,890 obec — start with top 50 mestá)
- [ ] CSD2022-2023 ArcGIS Hub data extraction workflow
- [ ] EU 2024/1028 SK national register walkthrough once portal launches
- [ ] Bratislava MČ Airbnb / krátkodobý prenájom rules per MČ
- [ ] Asbestos detection workflow for panelové domy (1948-1989)
- [ ] Predkupné právo + susedské vzťahy detection from LV
- [ ] Žitný ostrov + národné parky construction limits
- [ ] Hungarian-language listings (south Slovakia) — bilingual extraction
