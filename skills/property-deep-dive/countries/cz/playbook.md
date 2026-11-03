# Czech Republic 🇨🇿 — Property Due-Diligence Playbook

ISO2: `cz`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **PSČ (postcode)**: 5 digits in `NNN NN` format (e.g., `110 00`, `602 00`)
  - First 3 digits: regional cluster
  - Last 2: local (no `0` after space typically)
- **Admin levels**: 14 kraje → 76 okresy → 6,258 obce (municipalities; count at 31 Dec 2025, source ČSÚ Struktura území podle počtu obyvatel) → katastrální území
- **Currency**: CZK (Czech koruna), floating. ČNB fixing 22 Oct 2026: 1 EUR = 24.265 CZK (2026 data, source ČNB denní kurz)
- **Languages**: Czech (official); German/Polish/Slovak minority pockets
- **Cadastre**: **ČÚZK** (Český úřad zeměměřický a katastrální) — public viewer Nahlížení do KN **FREE, no registration** (ČÚZK, 2026); automated harvesting of the viewer is prohibited, use ČÚZK's free REST API instead
- **Identifier**: parcela číslo + katastrální území + obec (LV = list vlastnictví = title deed)
- **Major reform 2014**: New Civil Code (NOZ) merged building + land parcel; old separate registers consolidated.
- **CRITICAL 2020 change**: nabývací daň (transfer tax for buyers) **ABOLISHED** by zákon č. 386/2020 Sb., effective 26 Sep 2020, retroactively covering cadastre entries (vklad) from December 2019 onwards (source: Finanční správa, Daň z nabytí nemovitých věcí page).

## Section: `--price`

### Primary sources

- **ČÚZK Nahlížení do KN** (FREE, official):
  - Portal: `https://nahlizenidokn.cuzk.gov.cz/`
  - Search by parcela / building / unit / address (fixed CAPTCHA for owner reveal without login)
  - Returns: short LV with vlastník, výměra, list vlastnictví číslo, zatížení (encumbrances)
  - Login via Identita občana for full LV
- **ČÚZK Dálkový přístup pro neregistrované**: `https://dpn.cuzk.gov.cz/`
- **ČÚZK Dálkový přístup do KN** (paid pro tier): `https://cuzk.gov.cz/aplikace-dp` — prior registration with ČÚZK required, outputs invoiced at agreed intervals (source: ČÚZK Dálkový přístup do KN page, read 2026-10-23)

### Price benchmarks (Q2 2026 reference)

- **ČSÚ Indexy realizovaných cen bytů** (quarterly; Q2 2026 edition released 14 Sep 2026): `https://csu.gov.cz/produkty/indexy-realizovanych-cen-bytu-2-ctvrtleti-2026`
- **ČSÚ Indexy cen nemovitostí**: `https://csu.gov.cz/produkty/icn_cr`
- **ČNB residential property price data**: `https://www.cnb.cz/cs/financni-stabilita/`
- Q2 2026 trend, realized prices of older flats: ČR +14.0 % YoY, Praha +11.9 %, mimo Prahu +14.5 %; new flats (Praha only) +3.1 %; asking prices ČR +10.7 %, Praha +9.0 % (2026 data, source ČSÚ Vývoj ekonomiky ČR 1. pololetí 2026)
- Full-year 2025: flat prices +10.6 % YoY, family houses +6.7 % (2025 data, source ČSÚ Ceny nemovitostí, published 15 Jul 2026)

### Listing platforms

- **Sreality.cz** — largest, includes **Cenová mapa** (atlas of sold prices): `https://www.sreality.cz/cenova-mapa`
  - URL: `https://www.sreality.cz/hledani/prodej/byty/<region>` or `/<okres>` or `/<obec>`
  - Filters: cena, dispozice (1+kk to 6+1), výměra, lokalita
- **Bezrealitky.cz** — privates, no agency fees: `https://www.bezrealitky.cz/`
- **Reality.idnes.cz**, **ČeskéReality.cz** (agency-listing aggregator), **UlovDomov.cz** (rentals)
- **REMAX, M&M, Sting** — agency networks

### Average €/m² benchmarks (2025 realized, ČSÚ)

| Region | Realized €/m² (avg byty) |
|---|---:|
| ČR (whole country) | 72,410 CZK ≈ €2,984 |
| Praha (hl. m.) | 131,520 CZK ≈ €5,420 |
| Jihomoravský kraj, obce ≥ 50,000 obyv. (includes Brno) | 99,713 CZK ≈ €4,109 |
| Jihomoravský kraj (whole kraj) | 81,652 CZK ≈ €3,365 |
| Moravskoslezský kraj (whole kraj / obce ≥ 50,000 obyv., includes Ostrava) | 51,694 / 59,499 CZK ≈ €2,130 / €2,452 |
| Ústecký / Karlovarský | 42,375 / 41,915 CZK ≈ €1,746 / €1,727 |
| Vysočina / Pardubický / Zlínský | 56,720 / 58,557 / 56,354 CZK ≈ €2,338 / €2,413 / €2,322 |
| Středočeský (whole kraj) | 64,911 CZK ≈ €2,675 |

Source: ČSÚ Veřejná databáze CEN13A "Průměrné kupní ceny nemovitostí – územní srovnání", byty Kč/m², 2025 (data ČÚZK; ČSÚ release of 15 Jul 2026). EUR figures computed at the ČNB fixing of 22 Oct 2026 (24.265 CZK/EUR). Kraj averages mix villages and cities; CEN13A also splits each kraj by obec size band. Never read a kraj or size-band average as the value of a specific parcel.

### Compute

1. Listing price/m² = listing CZK / m² (clarify: užitná plocha = Carrez-equivalent, vs zastavěná plocha for taxes)
2. Compare to ČSÚ realized price for the kraj
3. Compare to Sreality cenová mapa (more granular, by city district)
4. **Trap**: byty in Praha priced in CZK or EUR — clarify which currency on listing
5. **Trap**: některé novostavby exclude DPH (advertise net price); check if "cena bez DPH" or "vč. DPH"

---

## Section: `--traffic`

### Primary source

- **ŘSD Sčítání dopravy** (Ředitelství silnic a dálnic):
  - Portal: `https://scitani.rsd.cz/`
  - Most recent: **CSD 2025** (data collected in 2025; contractor IPSOS with EDIP). Preliminary results published 19 Mar 2026; the "Výsledná sestava V2" table (XLSX, file V2_CSD_2025_20260826) and preliminary PDF intensity maps are at `https://www.rsd.cz/silnice-a-dalnice/scitani-dopravy` (2026 data, source ŘSD + Ministerstvo dopravy press release 19 Mar 2026)
  - Coverage CSD 2025: more than 6,800 úseků counted on motorways, all road classes and some city streets, plus 400 automatic counters (2026 data, source MD press release 19 Mar 2026); the V2 table lists 9,549 úseků, of which 2,630 take over a neighbouring úsek's intensity (computed from the ŘSD V2 XLSX, 2026-10-23)
  - Display: the interactive web map `https://scitani.rsd.cz/CSD_2020/pages/informations/default.aspx` still shows **CSD2020** as of 2026-10-23 (CSD2020 counted in the second half of 2020 and spring 2021, per ŘSD) — for 2025 values per úsek, use the V2 XLSX
- **CDV — Centrum dopravního výzkumu**: `https://cdv.gov.cz/` (methodology + supplementary research)
- **Silniční databanka ŘSD + NDIC**: `https://www.rsd.cz/rsd/silnicni-databanka-a-ndic`

### Key term

**RPDI (roční průměr denních intenzit dopravy, vozidla/24 h)** — Average Daily Traffic over the year, similar to AADT (term used in ŘSD CSD2020 and CSD 2025 results).

### Verdict bands

- 🟢 < 1,000 v/d (rural III. třída)
- 🟡 1,000–5,000 v/d (small II. třída, urban side street)
- 🟠 5,000–20,000 v/d (busy II. třída, urban arterial, smaller I. třída)
- 🔴 > 20,000 v/d (D/dálnice, major I. třída, urban core)

### Coarse fallback

OSM `highway` class:
- motorway/trunk = D + R + I. třída major
- primary = I. třída
- secondary = II. třída
- tertiary = III. třída
- residential = obytná zóna

### CSD 2025 highlights (preliminary)

- Motorway average intensity +12 % vs 2020, average 34,400 vehicles/24 h; busiest úsek D1 near Průhonice 106,976 vehicles/24 h, up by a third vs 2020 (2026 data, source MD press release 19 Mar 2026)
- I. třída average 9,600 vehicles/24 h, up almost 6 % vs CSD2020 (2026 data, source MD press release 19 Mar 2026)

### CSD2020 highlights

- Total traffic performance +10 % vs CSD2016
- D-network +15 %, road network +9 %
- Heavy vehicles +16 %, cars +9 %
- Average intensity: motorways 30,700, I. třída 9,100, II. třída 2,900 vehicles/24 h (2020 data, source ŘSD Sčítání dopravy page) — rates/figures may have changed since

---

## Section: `--tax`

### Annual property tax — Daň z nemovitých věcí

**Major 2024 reform** (Konsolidační balíček, zákon č. 349/2023 Sb.) raised rates by ~80 % (~1.8×) from 1 Jan 2024 and introduced the inflační koeficient, set at 1.0 for 2024; building rates went from 2.00 / 6.00 / 8.00 / 10.00 Kč/m² in 2023 to 3.50 / 11.00 / 14.50 / 18.00 Kč/m² (2024 data, source: Finanční správa — Novela zákona o DNV, stručný popis významných změn na rok 2024).
**Major 2025 reform**: zrušení koeficientu 1.5; changes to the local and population koeficienty; local koeficient now 0.5–5.0 (§ 12) (2026-10-23 verified, source: Finanční správa — Novela zákona o DNV (konsolidační balíček); zákon č. 338/1992 Sb. znění 01.10.2025, zakonyprolidi.cz).

**Formula**:
```
Daň = Plocha (m²) × Základní sazba × Základní koeficient × Místní koeficient × Inflační koeficient
```

| Item | Sazba 2026 |
|---|---|
| Obytné domy (rodinný dům, bytový dům) | **3.50 Kč/m² zastavěné plochy** (+1.40 Kč/m² for each further above-ground floor whose area exceeds ⅔ of the built-up area, § 11 odst. 2) |
| Byty (jednotky in the skupina ostatních zdanitelných jednotek) | **3.50 Kč/m² of upravená podlahová plocha** = podlahová plocha × 1.22 (unit in a bytový dům with a land share) or × 1.20 (other cases) (§ 10 odst. 3) |
| Stavby pro rodinnou rekreaci (incl. a rodinný dům used for rodinná rekreace, § 1a odst. 1 písm. b) | 11.00 Kč/m² |
| Garáže | 14.50 Kč/m² |
| Stavby pro podnikání (průmysl, stavebnictví, doprava, energetika, ostatní podnikání) | 18.00 Kč/m² (3.50 Kč/m² for zemědělská prvovýroba, lesní a vodní hospodářství) |
| Pozemky (orná půda, zahrada, vinice, sad, chmelnice) | **1.35 % z ceny pozemku** (raised from 0.75 % in 2023 by konsolidační balíček Act 349/2023 Sb. effective 1 Jan 2024; 2023 rate per Finanční správa stručný popis změn 2024) |
| Trvalé travní porosty + lesní pozemky | **0.45 % z ceny pozemku** (raised from 0.25 % in 2023, effective 1 Jan 2024; 2023 rate per Finanční správa stručný popis změn 2024) |
| **Stavební pozemek** | 3.50 Kč/m² (× population koeficient, § 6 odst. 3) |
| **Inflační koeficient 2026 / 2027** | **1.0** / **1.0** |

Rates: zákon č. 338/1992 Sb. § 6 odst. 1–3, § 10, § 11 odst. 1–2 (2026 data, source: consolidated znění 01.10.2025 on zakonyprolidi.cz, no later amendment shown). Inflační koeficient: MF press release 14 Jul 2026 — "pro rok 2027 zůstává na hodnotě 1,0 a tedy stejně jako v roce 2026".

**Základní koeficient** by population:
- Obec ≤ 1,000 obyv: **1.0**
- 1,001–6,000: **1.4**
- 6,001–10,000: **1.6**
- 10,001–25,000: **2.0**
- 25,001–50,000: **2.5**
- > 50,000 + statutární města + Františkovy Lázně, Luhačovice, Mariánské Lázně, Poděbrady: **3.5**
- Praha: **4.5**
- The obec may raise its koeficient by one category for a katastrální území or městská část (Praha up to 5.0) (§ 11 odst. 5); recreational buildings in a národní park or CHKO zone I use 2.0 (§ 11 odst. 6) (2026-10-23 verified, source: zákon č. 338/1992 Sb. § 6 odst. 3, § 11 odst. 4–6, zakonyprolidi.cz)

**Místní koeficient** (set by the obec via obecně závazná vyhláška, or opatření obecné povahy for named properties): 0.5–5.0 in 0.1 steps, for the whole obec, a katastrální území, a městská část, a group of properties or named properties; selected agricultural land, TTP and nevyužitelné ostatní plochy only 0.5–1.5; 1.0 where none is set (§ 12 odst. 1–3). A vyhláška counts for a tax year only if valid by 1 October of the preceding year (§ 16a odst. 1) (2026-10-23 verified, source: zákon č. 338/1992 Sb., zakonyprolidi.cz). Per-obec koeficienty: Finanční správa search tool `https://adisspr.mfcr.cz/dpr/adis/idpr_reg/dne/koef/vyhledani.faces`.

### Example calculation

A 100 m² (zastavěná plocha) single-storey rodinný dům in Praha:
- 100 × 3.50 Kč × 4.5 (Praha basic) × 1.0 (no local mult) × 1.0 (inflation) = **1,575 CZK/rok** (~€65/yr)
- Same footprint with a full second above-ground floor: 100 × (3.50 + 1.40) Kč × 4.5 × 1.0 × 1.0 = **2,205 CZK/rok** (~€91/yr)

A 200 m² rodinný dům in obci 5,000 obyv:
- 200 × 3.50 Kč × 1.4 × 1.0 × 1.0 = **980 CZK/rok** (~€40/yr)

A 60 m² byt (podlahová plocha) in a Praha bytový dům with a land share:
- 60 × 1.22 × 3.50 Kč × 4.5 × 1.0 × 1.0 = **1,153 CZK/rok** (~€48/yr)

(Computed from the 2026 rates above; EUR at the CNB rate of 24.265 CZK/EUR, 22 Oct 2026.)

**Daň z nemovitých věcí is therefore very low compared to W. Europe** — ~€9–€238/yr for the two example flats (computed: 50 m² byt × 1.20 in an obec ≤ 1,000 at místní koeficient 1.0 = 210 CZK; the 60 m² Praha byt above at místní koeficient 5.0 = 5,765 CZK); larger flats and houses in high-koeficient obce pay more (computed: the two-floor Praha house above at místní koeficient 5.0 = 11,025 CZK ≈ €454).

### Transaction taxes (one-time at purchase)

- **Daň z nabytí nemovitých věcí (transfer tax)**: **ABOLISHED 26 September 2020** by zákon č. 386/2020 Sb. (liabilities whose filing deadline ended on or after 31 Mar 2020 lapsed) (2026-10-23 verified, source: zakonyprolidi.cz 2020-386).
- **Buyer pays**: only notary/lawyer fees + cadastre registration fee (**2,000 CZK** per návrh na vklad, položka 120 zákona č. 634/2004 Sb.; 20 % discount when filed online after an Identita občana login = 1,600 CZK, computed) + survey (2026 data, source: ČÚZK — Zápisy do KN; nv.cuzk.gov.cz)
- **Seller pays**: daň z příjmů (15 % up to 36× the average wage / 23 % above, § 16 ZDP) on the capital gain if sold within **5 years** (acquisitions before 1 Jan 2021 — zákon č. 386/2020 Sb. Čl. IV bod 2) or **10 years** (acquisitions from 1 Jan 2021 onwards — § 4 odst. 1 písm. b ZDP). Exempt instead: the seller's own rodinný dům / byt where the seller had bydliště for at least 2 years immediately before the sale (§ 4 odst. 1 písm. a), or proceeds used for own bytová potřeba (§ 4 odst. 1 písm. a / b + § 4b) — spent by the end of the tax year after the year of sale, or in the year before it (§ 4b odst. 2), and the receipt notified to the správce daně by the tax-return deadline for the year of sale (§ 4b odst. 3); verify with a daňový poradce (2026-10-23 verified, source: zákon č. 586/1992 Sb. znění 01.08.2026, zakonyprolidi.cz)

**Notary / advokát**: est. 0.5–1.5 % of price (market practice, no primary source — verify quotes). Notarial acts are priced by the notářský tarif (§ 1 odst. 1 vyhlášky č. 196/2001 Sb.; the notary may raise the fee by up to 100 % for complex, time-consuming, foreign-law or foreign-language matters, § 9); an advokát charges the agreed smluvní odměna, the tarif applying only where none was agreed (§ 1 odst. 1 vyhlášky č. 177/1996 Sb.). Tarif reference for a CZK 5,000,000 purchase, excluding any DPH (computed): notářský zápis o kupní smlouvě 13,200 CZK = ⅔ × Položka A (2,000 + 4,800 + 3,000 + 6,000 + 4,000) ≈ 0.26 %; notářská úschova 13,600 CZK = Položka C (1,200 + 2,400 + 2,000 + 8,000) ≈ 0.27 %, or 1,360 CZK when the same notary wrote the zápis; advokát mimosmluvní odměna 28,300 CZK per úkon = 9,100 + 480 × 40 (§ 7 bod 6) ≈ 0.57 % (2026 data, source: vyhláška č. 196/2001 Sb. znění 14.03.2025, příloha; vyhláška č. 177/1996 Sb. znění 15.01.2026; zakonyprolidi.cz)
**Realitní makléř**: est. 3–5 %, usually paid by seller (market practice, no primary source; secondary: finance.cz, 2 May 2018 — "obvykle ve výši 4 až 5 % z ceny nemovitosti", "nejčastěji hradí prodávající" — rates/figures may have changed since). No statutory fee level: the smlouva o realitním zprostředkování must state the provize or how it is set, or the zájemce can claim it is invalid (§ 10 odst. 1 písm. c, odst. 3 zákona č. 39/2020 Sb.) (2026 data, source: zákon č. 39/2020 Sb. znění 01.07.2021, zakonyprolidi.cz)
**Total transaction cost** (buyer side): est. ~1–2 % of price (market estimate, no primary source). Computed tarif reference for a CZK 5,000,000 purchase, excluding DPH and expenses: vklad fee 2,000 CZK + notářský zápis and úschova by the same notary 14,560 CZK = 16,560 CZK ≈ 0.33 %; vklad fee + an advokát-drafted contract at the tarif (28,300 CZK) + a separate notářská úschova (13,600 CZK) = 43,900 CZK ≈ 0.88 %; agreed fees, DPH and a bank valuation come on top. Comparison: est. ~10–13 % for a prima casa and ~13–17 % for a seconda casa in IT (market estimates, see `countries/it/playbook.md`)

### Future risk

- **No tax rises pledged**: the programové prohlášení vlády approved 5 Jan 2026 states "Zavazujeme se nezvyšovat žádné daně" and "Zastavíme automatické valorizace daně z nemovitostí prostřednictvím inflačních koeficientů" — intent only, no amending bill found as of 2026-10-23; the inflační koeficient is 1.0 for 2027 regardless (2026 data, source: vlada.gov.cz programové prohlášení; MF press release 14 Jul 2026)
- **Main driver of year-to-year bill changes = the obec**: místní koeficient 0.5–5.0 (see above) — re-check the obec's vyhláška each year
- **Re-introduction of nabývací daň**: not in the programové prohlášení vlády (January 2026), which pledges "nezvyšovat žádné daně" (2026 data, source: vlada.gov.cz programové prohlášení) — verify any new tax bill at psp.cz
- **Mortgage-interest deduction (watch — announced, no bill)**: the current cap is CZK 150,000/yr per household for housing financed from 1 Jan 2021 (§ 15 odst. 4 ZDP; housing obtained before 1 Jan 2021 keeps the pre-2021 rules, zákon č. 386/2020 Sb. Čl. IV bod 3) (2026 data, source: zákon č. 586/1992 Sb. znění 01.08.2026). On 7 Oct 2026 Finance Minister Alena Schillerová said on TV Nova that MF has a draft raising the cap by up to CZK 50,000 for people up to age 36, for existing and new mortgages, possibly from tax period 2027 (secondary: energozrouti.cz 10 Oct 2026; hn.cz 8 Oct 2026); earlier reports gave 2028 for the coalition's mortgage-support changes (secondary: ČT24 14 Jun 2026; finance.cz 7 Jul 2026) — no bill found as of 2026-10-23; verify at mf.gov.cz / psp.cz. If enacted, worth at most CZK 7,500/yr in tax at the 15 % rate (computed: 50,000 × 15 %). The 2026 programme also pledges state support for mortgage interest on a young family's first home (vlada.gov.cz, 5 Jan 2026)

---

## Section: `--rental`

### Long-term residential

**Daň z příjmů z pronájmu (FO)** — § 9 Zákona o daních z příjmů:
- Two cost methods, one choice for all § 9 rental income: the 30 % paušál is taken on all rent under § 9 odst. 1 and then covers every rental expense, so the methods cannot be mixed between properties; the choice cannot be changed retroactively (§ 9 odst. 4–5 zákona č. 586/1992 Sb., znění 01.08.2026; the no-mixing reading also in finance.cz, 19 Feb 2016, secondary):
  - **Skutečné výdaje** (actual expenses)
  - **Paušální výdaje 30 %** (deduction capped at 600,000 CZK, reached at 2 mil. CZK of rent; computed: 600,000 / 30 %) (2026 data, sources: Finanční správa, Pronajímatel page; § 9 odst. 4 ZDP, znění 01.08.2026)
- Sazba 2026: **15 %** up to 36× average wage = ZD 1,762,812 CZK; **23 %** above (§ 16 ZDP, znění 01.08.2026) (2026 data, source Finanční správa; computed: average wage = všeobecný vyměřovací základ 2024 of 46,278 CZK × přepočítací koeficient 1.0581 = 48,966.75, rounded up to 48,967 CZK per § 23b odst. 4 zákona č. 589/1992 Sb., inputs from nařízení vlády č. 365/2025 Sb.; 36 × 48,967 = 1,762,812)
- Reportable on daňové přiznání (DAP) annually
- No social/health insurance contributions on § 9 rent (unlike OSVČ) (source: Veřejný ochránce práv leaflet, Sep 2026)
- Filing and payment deadlines for tax year 2025: 1 Apr 2026 (paper), 4 May 2026 (electronic), 1 Jul 2026 (via daňový poradce / advokát); the tax is due by the same date (2026 data, source Finanční správa)

### Short-term rentals (krátkodobé ubytování / Airbnb / Booking)

**Status**: in transition. No national STR registration and no statutory day cap in force as of 2026-11-03 (MMR eTurista page; psp.cz); an MMR government bill and two MPs' bills, sněmovní tisk 106 and 107, are pending (details below).

#### Current obligations (2026)

- **Trade licence**: volná živnost "Výroba, obchod a služby neuvedené v přílohách 1 až 3", obor **55 Ubytovací služby**; no qualification required, filing fee 1,000 CZK. Platform hosting offered systematically for profit is podnikání, and hosting without the licence is illegal business with the same tax and insurance duties (2026 data, sources Veřejný ochránce práv leaflet "Sdílená ekonomika", Sep 2026; GFŘ information č. j. 10352/23/7100-30118-012884)
- **DPH (VAT)**: accommodation services (CZ-CPA 55) take the **12 % reduced rate** (příloha č. 2 zákona o DPH, since 1 Jan 2024). Registration is mandatory once turnover exceeds 2,000,000 CZK in a calendar year (payer from 1 Jan of the next year) or 2,536,500 CZK within the year (payer from the next day). A non-payer who pays a service fee to a platform established outside ČR becomes an identified person and owes Czech VAT on that fee (2026 data, sources § 6 zákona č. 235/2004 Sb., version in force 2026; Finanční správa easy-to-read DPH guide; GFŘ information on VAT rates from 1 Jan 2024; Veřejný ochránce práv leaflet, Sep 2026)
- **Místní poplatek z pobytu** (local stay fee, not a tax): collected from each guest for stays of up to 60 days where the obec has introduced it by obecně závazná vyhláška; statutory maximum 50 CZK per person per day (§ 3d zákona č. 565/1990 Sb.). Praha charges the 50 CZK maximum per person per started day, excluding the arrival day (raised from 21 CZK by ZHMP resolution 32/81 of 16 Dec 2021; going higher needs a change to zákon o místních poplatcích) (sources: Veřejný ochránce práv leaflet, Sep 2026; Rada HMP materials on eud.praha.eu)
- **Hlášení cizinců**: every paying foreign guest, EU citizens included, must be reported to the cizinecká policie within 3 working days of arrival, via Ubyport (mandatory for businesses) or a paper form; keep a domovní kniha for 6 years; fine up to 50,000 CZK (2026 data, source Veřejný ochránce práv leaflet, Sep 2026)
- **Building use**: ubytovací služby are lawful in a building whose permitted use is "stavba ubytovacího zařízení"; running them in a "stavba pro bydlení" (bytový or rodinný dům) breaches the stavební zákon, fine up to 1,000,000 CZK; a change of use needs the stavební úřad (2026 data, source Veřejný ochránce práv leaflet, Sep 2026)
- **eTurista** (planned national register of accommodation and guests): **not live and not mandatory**. The enabling amendment to zákon č. 159/1999 Sb. (sněmovní tisk 761) stalled before third reading in 2025; without legislation, use of the system stays voluntary (source: MMR, Vyhodnocení AP 2024–2025). MMR's eTurista page says a new amendment is prepared for the Chamber and the system is in internal testing, with no launch date given (read 2026-10-23). The amendment had been due to take effect on 1 July 2025; that date was missed while the bill waited for its third reading (secondary: finance.cz, 30 Jun 2025). In the Chamber's 10th term a group of MPs filed the register bill again as sněmovní tisk 106 (10 Feb 2026), partly based on the former government bill (tisk 761) but without its municipal-regulation part; it proposes effect from 1 Jul 2026, host registration under Regulation 2024/1028 from 1 Oct 2026 and full effect from 1 Jan 2027, so its first two dates have already passed; the government's opinion is disagreement (tisk 106/1, 10 Mar 2026) and the bill awaits first reading (sources: psp.cz tisk 106 record, status at 3 Nov 2026; bill text and důvodová zpráva t010600)

#### EU Regulation 2024/1028

- Applies since **20 May 2026** in opt-in/opt-out mode: Member States are not obliged to introduce STR registration, but any registration system or platform-data request they introduce must go through the Regulation, with a national Single Digital Entry Point (2026 data, source European Commission DG GROW news, 20 May 2026)
- **Czechia: no registration procedure in force.** MMR's notice under Art. 13(1)(a)-(b) states that ČR applies no registration procedure anywhere on its territory and requests no activity data from STR platforms, adding that this may change (source: MMR eTurista page, read 2026-10-23)
- So there is no Czech STR registration number for platforms to require yet; one would arrive only with the pending amendment to zákon č. 159/1999 Sb.

#### Praha and local rules

- Praha 1 local referendum, 3–4 Oct 2025: question 3 (omezení krátkodobého ubytování) passed with 6,850 votes / 72.26 % of participants (turnout 9,480 of 20,997 eligible voters), declared valid and binding on the městská část (sources: praha1.cz results page; ZMČ Praha 1 minutes, 4 Nov 2025; praha1.cz, 17 Jul 2026)
- Positions, not law (no Praha day cap or zone ban is in force):
  - **Day cap**: in Apr 2025 Praha deputy mayor Jiří Pospíšil said Praha would want to regulate Airbnb-type accommodation once the law allows it, citing the Amsterdam model in which a flat can be used this way "e.g. two months a year or another limited time" (secondary: echo24.cz, 3 Apr 2025); no figure has been adopted, and a fixed 60-day Praha cap is unsourced — verify with MHMP (praha.eu)
  - **Praha 1** (ZMČ Praha 1 stanovisko, praha1.cz, 17 Jul 2026): issue a registration number only after checking that the use matches building rules and the permitted (kolaudovaný) purpose of the building; platforms to verify numbers against a register; authorities to compare platform data with what hosts report (guests, length of stay, unit); open zákon o místních poplatcích so each obec can set the stay fee by tourism intensity, with 0–200 CZK per person per night named as appropriate
- **SVJ consent through stanovy (case law)**: the Nejvyšší soud held that an SVJ that limits owners' use of their units through its stanovy, here a clause making repeated short-term letting (under 3 months) or ubytovací služby subject to the consent of all members, decides outside its competence, and the decision is treated as never adopted (§ 245 OZ) (usnesení NS sp. zn. 26 Cdo 854/2022 of 15 Mar 2023, Sbírka soudních rozhodnutí a stanovisek č. 98/2023, decided under the OZ as in force to 30 Jun 2020; source sbirka.nsoud.cz, archived 2025-02-08)
- No statutory STR cap yet; two pending bills would give obce that power, neither enacted:
  - **MMR government bill**: MMR says its prepared amendment to zákon č. 159/1999 Sb. would let obce regulate short-term-rental conditions (source: MMR eTurista page). The government's legislative plan of 23 Mar 2026 set submission to the government for 06.26 and entry into force for 01.27 (Plán legislativních prací vlády na zbývající část roku 2026, příloha č. 1 k usnesení vlády č. 175); the current draft's own proposed effective date is unverified — verify at odok.gov.cz (VeKLEP). Per novinky.cz (6 Oct 2026, secondary), the draft is in připomínkové řízení and would allow day caps, guest limits, seasonal bans and mandatory host registration; each obec's rules would have to be notified to the European Commission and could not take effect until any Commission objections are resolved
  - **Sněmovní tisk 107** (MPs' bill, filed 10 Feb 2026): a new § 9e would let an obec, by nařízení obce for the whole obec or for individual ucelené zastavěné oblasti, set for accommodation (ubytování) provided in flats in bytové domy a period of the year in which none may be provided, a maximum number of days per year on which it may be provided, or a maximum number of guests by the flat's living area; each draft nařízení must be notified to the European Commission under Art. 15(7) of Directive 2006/123/EC through MPO, and any Commission comments must be taken into account before it is issued; proposed effective date 1 Jan 2027; government opinion neutral (tisk 107/1, 31 Mar 2026); awaits first reading, on the agenda of the 34th schůze (from 13 Oct 2026) (sources: psp.cz tisk 107 record, status at 3 Nov 2026; bill text t010700)
- Local enforcement under existing law (Praha 1 is the městská část with sourced actions): in the Růžová street case its stavební úřad found a flat approved (kolaudovaný) for housing let short-term against its approved use, called on the owner to stop that use by 31 Jul 2020 and then opened přestupek proceedings; the MHMP odbor stavebního řádu, in its opinion of 29 Jul 2021, found this a change of use needing the stavební úřad's approval and dismissed the owner's appeal (praha1.cz, 17 Sep 2021). In Feb 2021 ZMČ Praha 1 required its representatives in SVJs where the MČ co-owns units to put permanent residents' interests first and to vote for motions that would ban short-term accommodation in the building or make it as hard or as costly as possible (praha1.cz, 15 Feb 2021; seznamzpravy.cz, 14 Feb 2021); under the 2023 NS ruling above, a stanovy clause restricting how owners use their units is treated as never adopted. Other městské části: no sourced STR rules found — verify with the ÚMČ

#### Tax regime for Airbnb

- **With the trade licence (ubytovací služby)**: income under § 7 odst. 1 písm. b) ZDP, paušál 60 % (max 1,200,000 CZK), plus OSVČ social and health insurance (sources: GFŘ information č. j. 10352/23/7100-30118-012884; Veřejný ochránce práv leaflet, Sep 2026; cap per § 7 odst. 7 písm. b) ZDP, znění 01.08.2026)
- **Without the licence** (still podnikání): § 7 odst. 1 písm. c), paušál 40 % (max 800,000 CZK; § 7 odst. 7 písm. d) ZDP, znění 01.08.2026). GFŘ treats platform accommodation as podnikání under § 420 OZ taxed under § 7, not § 9; per the ombudsman, platform letting is only exceptionally a nájem (same sources)
- **Paušální daň 2026**, I. pásmo: **9,162 CZK/month** all-in (100 CZK tax + 5,756 CZK pension insurance + 3,306 CZK health insurance), cut retroactively from 9,984 CZK with effect from 1 Jan 2026 and first due at the new amount on 20 Jul 2026. I. pásmo covers prior-year self-employment income up to 1 mil. CZK from any activity, more if most income qualifies for the 60 % / 80 % paušál (see `--work`) (2026 data, source Finanční správa)

### Strategic notes

The first three bullets are curated heuristics (wisdom, not data), not drawn from a primary source; check demand in ČSÚ accommodation statistics (`https://csu.gov.cz/cestovni-ruch`) and the obec's own rules before relying on them.

- **Praha + Český Krumlov + Karlovy Vary + Brno + spa towns**: highest yields but biggest regulatory risk
- **South Bohemia, Šumava, Krkonoše**: tourist demand, less regulation
- **Wholly-rural / vesnice**: limited demand outside ski resorts
- **eTurista not live** as of 2026-10-23: no national registration duty or eTurista penalty yet; watch the MMR amendment to zákon č. 159/1999 Sb. and sněmovní tisk 106 / 107 (see above)
- **EU regulation 2024/1028**: platform checks of registration numbers apply only where a Member State runs a registration procedure; ČR runs none as of 2026-10-23 (MMR), so delisting of unregistered units is a future risk, not a current rule

---

## Section: `--work=<profession>`

### Job platforms

- **Jobs.cz**, **Práce.cz**, **Profesia.cz**, **StartupJobs.cz**
- **LinkedIn CZ** (very active in IT, finance, big-corp)
- **Úřad práce ČR**: `https://up.gov.cz/` (the old uradprace.cz address redirects there) — official labour office; vacancy database at `https://up.gov.cz/volna-mista-v-cr`
- **Hyperinzerce, Annonce** — older classifieds

### Self-employment regimes

- **OSVČ (osoba samostatně výdělečně činná)**: standard self-employed
  - Paušální výdaje 40 / 60 / 80 % depending on činnost
  - Sociální pojištění + zdravotní pojištění mandatory
- **Paušální daň** (2026, monthly all-in; 2026 data, source Finanční správa):
  - I. pásmo: 9,162 CZK/měsíc (cut retroactively from 9,984 CZK with effect from 1 Jan 2026; 2025: 8,716 CZK). Prior-year income ≤ 1 mil. CZK from any activity, ≤ 1.5 mil. if ≥ 75 % qualifies for the 80 % / 60 % paušál, or ≤ 2 mil. if ≥ 75 % qualifies for the 80 % paušál
  - II. pásmo: 16,745 CZK/měsíc. ≤ 1.5 mil. from any activity, or ≤ 2 mil. if ≥ 75 % qualifies for the 80 % / 60 % paušál
  - III. pásmo: 27,139 CZK/měsíc. ≤ 2 mil. from any activity
- **Volná živnost** (free trade): no qualifications (full legal capacity and a clean record suffice), file at any Živnostenský úřad; filing fee 1,000 CZK (2026 data, source Veřejný ochránce práv leaflet, Sep 2026)
- **Vázaná / koncesovaná živnost**: requires education / experience / license

### Salaried benchmarks

- Median monthly gross wage 2025 (CZK; 2025 data, source ČSÚ Struktura mezd zaměstnanců, released 22 May 2026 and ČSÚ Praha 25 Jun 2026):
  - ČR: 44,337
  - Praha: 52,793 (the only kraj above 50,000)
  - Other kraje: 40,900 (Karlovarský) to 46,400 (Středočeský)
- Average gross wage Q2 2026: 51,966 CZK, +6.4 % YoY (2026 data, source ČSÚ, 3 Sep 2026)
- **Minimální mzda 2026**: 22,400 CZK/měsíc (134.40 CZK/h); **2027**: 24,900 CZK/měsíc (148.30 CZK/h), approved by the government (sources: MPSV)
- Registered unemployment: 5.0 % in September 2026 (2026 data, source Úřad práce ČR press release, 8 Oct 2026)

### Catchment heuristics

- Within 30 min of okresní město: decent catchment
- Within 60 min of kraj capital: full salaried opportunity
- Mountainous border regions (Šumava, Krušné hory, Jeseníky): thin labor markets, English-speaking expats common in tourism

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Záplavová území** (national flood map) | `https://voda.gov.cz/?page=zaplavova-uzemi-mapa` | Q5/Q20/Q100 flood zones |
| **Digitální povodňový plán ČR** | `https://webmap.dppcr.cz/dpp_cr/dppcr.dll?MU=001` | Flood plans, hlásné profily |
| **ČHMÚ Hlásná a předpovědní povodňová služba** | `https://hydro.chmi.cz/hppsoldv/` | Real-time hydrology |
| **MŽP povodňové nebezpečí Q100** | `https://cds.mzp.cz/mapy/?MAP=mpn_100` (🟡 offline on 2026-10-23 and still on 2026-11-03, with an MŽP notice that the system was paused after a critical security vulnerability — retry, or use voda.gov.cz meanwhile) | Hazard zones |
| **ČAP (Česká asociace pojišťoven) povodňové mapy** | `https://www.cap.cz/povodnove-mapy` | Insurance-grade flood zones (1-4) |
| **EDPP.cz online povodňová mapa** | `https://www.edpp.cz/online-povodnova-mapa-cr/` | Aggregated commercial map |
| **ČGS Svahové nestability (landslides)** | `https://mapy.geology.cz/svahove_nestability/` | Landslide registry + susceptibility |
| **ČGS Geofond sesuvy** | `https://mapy.geology.cz/arcgis/rest/services/Geohazardy/sesuvy_Geofond/MapServer` | API access |
| **ČGS / SÚRO Radon mapa** | `http://www.geology.cz/demo/CD_RADON50/index/info.htm` + `https://www.suro.cz/cz/prirodnioz/radonove-mapy` | Radon index 1-3 of geological substrate |
| **ČGS Radon web map** | `https://mapy.geology.cz/radon/` (updated 2026-10-23: replaces `http://www.geologicke-mapy.cz/radon/`, HTTP 404; linked from SÚRO) | Updated 1:50 000 radon maps of the geological subsoil (per SÚRO) |
| **Geofyzikální ústav AV ČR seismicita** | `https://www.ig.cas.cz/vyzkum-a-vyuka/observatore/ceska-regionalni-seismicka-sit/` (updated 2026-10-23: old `/observatorie/` path redirects to an image) | Earthquake monitoring |
| **SeismickaMapa.cz** | `https://seismickamapa.cz/` (⚠️ operator not identified, tier unverified; could not be read for verification on 2026-11-03 — rely on the GFÚ AV ČR pages above) | Aggregated hazard map |
| **WEBNET West Bohemia swarms** | `https://www.ig.cas.cz/vyzkum-a-vyuka/observatore/lokalni-seismicka-sit-webnet/` (updated 2026-10-23: old `/observatorie/` path redirects to an image) | West-Bohemia microseism |

### Flood zones (záplavová zóna 1-4)

| Zóna | Riziko | Notes |
|---|---|---|
| **1** | Zanedbatelné | est.: standard flood cover expected — each insurer decides |
| **2** | Nízké | est.: possible insurance surcharge — each insurer decides |
| **3** | Střední | est.: insurance can be expensive or refused — each insurer decides |
| **4** | Vysoké | est.: often uninsurable for flood — each insurer decides |

Zone labels and notes are est.: the ČAP page does not define zones 1–4; it says the zones show flood risk for a location from the insurance market's view and that member insurers use them as one input to property-insurance pricing (source: ČAP Povodňové mapy page). Calibration (secondary, before the RZ2023 maps): a 2022 press article described zone 1 as land above the 500-year flood with practically negligible risk, zone 2 as elevated risk (100- to 500-year flood), zone 3 as medium (50-year flood) and zone 4 as high (10-year flood); insurers quoted there reported no surcharge in zone 1, zone 2 mostly up to 50 % dearer and multiples in zone 3 (Slavia), flood generally not insured in zone 4 (Kooperativa), and ~70 % of CZ properties in zone 1 and ~3–4 % in zone 4 (Generali) (2022 data, source novinky.cz, 18 Jun 2022 ⚠️ secondary) — rates/figures may have changed since. NEMO Report (commercial, Propea solutions s.r.o. ⚠️), the address check the ČAP page links to (`http://www.nemoreport.cz/proverit-nemovitost-cap`), applies the ČAP methodology per address, names the risk levels nízké / střední / vysoké (neither the ČAP nor the NEMO page shows the zone-number mapping), and states that more than 25 % of CZ addresses face low, medium or high flood risk (2026 page, source nemoreport.cz ⚠️). The zone is an address-point insurance indicator, not a parcel survey. These are ČAP insurance tariff zones from the RZ2023 map set (built 2022–2023, 5th generation, Intermap Technologies); insurers may deviate from them (source: ČAP Povodňové mapy page). They are **not** the statutory záplavové území. Building limits come from the statute: no new buildings in the aktivní zóna záplavového území except water works and essential infrastructure (§ 67 odst. 1 zákona č. 254/2001 Sb.), and elsewhere in a záplavové území the vodoprávní úřad sets limits by opatření obecné povahy (§ 67 odst. 3). Check both layers: ČAP for insurability, voda.gov.cz for the statutory zone.

### Radon zones (radonový index podloží)

- Categories of the radonový index pozemku: nízký / střední / vysoký (source: SÚJB; ČGS)
- **Nízký** (low) — prevails on younger sediments (křídové pískovce, paleogenní and neogenní písky, pískovce, jílovce) (source: ČGS, Radon a geologie)
- **Střední** (medium) — prevails on the metamorphic crystalline rocks (pararuly, ortoruly) that cover a substantial part of the Bohemian Massif; metamorphic and magmatic rocks make up more than two thirds of the CZ geological substrate (source: ČGS, Radon a geologie)
- **Vysoký** (high) — prevails on magmatic rocks (granity, granodiority, durbachity, syenity) and silurské sedimenty (source: ČGS, Radon a geologie)
- **Commune-level list**: příloha č. 25 vyhlášky č. 422/2016 Sb. names 711 obce where the probability of exceeding the 300 Bq/m³ workplace reference level (§ 93 odst. 1) is above 30 % (count computed from the annex, text in force since 1 Feb 2026): Jihočeský 159, Středočeský 137 (okres Příbram 77), Vysočina 130, Plzeňský 103, Karlovarský 41, Olomoucký 38, Jihomoravský 31, Pardubický 29, Liberecký 22; Ústecký, Královéhradecký, Moravskoslezský and Praha 21 together (source: zakonyprolidi.cz 2016-422). These obce are the areas of increased radon risk defined in legislation; the explicit duties attached to them fall on operators of workplaces in underground or ground floors (source: SÚJB, RANAP revize 01). Commune-level only, never a plot value: the radon maps are a probability indicator for the geological subsoil (source: SÚJB, RANAP revize 01), and a plot's radonový index needs an on-site expert measurement (source: SÚJB)
- **CZ, owing to its geological substrate, is among the countries with higher radon exposure in the world**; SÚRO estimates that more than 4.5 % of the housing stock is excessively burdened by radon (2025 data, source SÚJB, Národní akční plán pro regulaci ozáření obyvatel z radonu, revize 01, in force 1 Jul 2025)
- New buildings: legislative radon requirements since 1991, with mandatory protective measures on plots with a higher radon index (source: SÚJB); today anyone applying for a permit for a new building or extension with obytné or pobytové místnosti must have the radonový index pozemku determined (§ 98 odst. 1 zákona č. 263/2016 Sb., atomový zákon)
- Indoor reference level: 300 Bq/m³ in obytné místnosti (source: SÚJB)
- Older buildings: SÚJB recommends an indoor radon measurement when buying an older house, at reconstruction, and where the local radon index is high (source: SÚJB)

**Mitigation cost**: est. 50,000–200,000 CZK (≈ €2,050–€8,220 at 24.340 CZK/EUR, ČNB rate 3 Nov 2026) — VMC, sealing, sub-floor ventilation. No official cost statistic was found; the range is a contractor estimate (verify with quotes). Calibration: the state subsidy for a flat or family house in permanent use, built under a permit issued by 28 Feb 1991, with a long-term average above 1,000 Bq/m³, is at most 150,000 CZK and is paid only if the measure brings radon below 300 Bq/m³ or cuts it by at least 75 % (2026 data, source MF Výzva č. 9/2026); in 2024 the state budget spent 725,230 CZK on radon measures, with 5 houses and no schools or water mains granted one, ≈ 145,000 CZK per house (computed: 725,230 ÷ 5; 2024 data, source SÚJB Zpráva o plnění RANAP za rok 2024) — rates/figures may have changed since

### Seismicity

- **Est. low overall** — calibration: the strongest West-Bohemian event of the last 100 years was ML 4.6 (below). Design seismic action follows ČSN EN 1998-1 and its national annex; ČSN EN 1998-1-1, issued 1 Oct 2025 and effective 1 Oct 2027, replaces ČSN EN 1998-1 (2006), ČSN EN 1998-1 ed. 2 (2013) and ČSN EN 1998-1 NA ed. A (2016) (source: ČAS, ČSN online catalogue) — data not publicly available: no free public source for the CZ seismic-zone values was found; verify at ČAS `https://csnonline.agentura-cas.cz/` or with a structural engineer
- **Active microseismic zones**:
  - **Western Bohemia / Vogtland** — Kraslicko, Nový Kostel: strongest West-Bohemian event of the last 100 years ML 4.6 on 21 Dec 1985 near Nový Kostel (MSK-64 intensity 6.5–7°, cracked walls and fallen chimneys up to 20 km from the epicentre); later swarms 2008 (ML 3.8), 2011 (ML 3.6), 2014 (ML 4.4), 2017 (ML 3.5), 2018 (ML 3.8); events above ML 4 can cause minor building damage (source: Geofyzikální ústav AV ČR, WEBNET pages)
  - **Hronovsko-poříčský zlom** (Královéhradecký kraj) — in NE Bohemia, the increased seismic activity of the marginal parts of the Bohemian Massif is concentrated in this fault zone; a strong NE-Bohemian earthquake in 1901 affected local mineral springs (source: Ústav struktury a mechaniky hornin AV ČR); tectonic earthquakes there are monitored by the Česká regionální seismická síť (source: GFÚ AV ČR); neither source grades the hazard
  - **Northern Moravia and Silesia** — tectonic earthquakes monitored by the Česká regionální seismická síť (source: GFÚ AV ČR); the source does not grade the hazard
- For most properties, seismicity is **🟢 negligible**

### Build-era hazards

*Qualitative build-era heuristics (wisdom, not data) — confirm with a building survey; the legal dates are sourced (zakonyprolidi.cz).*

| Era | Hazards |
|---|---|
| **< 1948** (předválečné, válečné) | Lead, asbestos in roofing, weak foundations |
| **1948–1989 panelové domy** | Asbestos in joints + insulation, variable concrete quality, aging utility lines |
| **1948–1989 cihlové domy** | Better quality but asbestos + lead pipes likely |
| **1990–2000 "kvalitní privátní"** | DIY craftsmanship variability; possible no permit work |
| **2000–2008** | Building boom — uneven quality |
| **Post-2008** | Fire-safety rules vyhláška č. 23/2008 Sb. (from 1 Jul 2008); technical requirements vyhláška č. 268/2009 Sb. (26 Aug 2009 – 31 Dec 2023, repealed by zákon č. 283/2021 Sb.), now vyhláška č. 146/2024 Sb. o požadavcích na výstavbu (from 1 Jul 2024); energy-performance rules vyhláška č. 148/2007 Sb. (from 1 Jul 2007), č. 78/2013 Sb. (from 1 Apr 2013), č. 264/2020 Sb. (from 1 Sep 2020) (source: zakonyprolidi.cz) |
| **Post-2014 NOZ** | Zákon č. 89/2012 Sb. (effective 1 Jan 2014): a building is part of the land (§ 506); a pre-2014 building owned by someone other than the land owner stays a separate nemovitá věc, with mutual předkupní právo (§ 3055–3056) — check the LV for split land / building ownership (source: zakonyprolidi.cz) |

**Asbestos**: est. likely in older stock (asbestos-cement roofing and pipes, panel-joint sealants); no official cut-off year was found — confirm with a laboratory-tested sample before renovation. Calibration: KHS Moravskoslezského kraje issues several dozen binding opinions a year on asbestos work, e.g. replacing asbestos-cement (eternit) roofing on public buildings and family houses and asbestos waste pipes in older apartment buildings (2019 data, source KHS MSK, Azbest leaflet) — rates/figures may have changed since. Removal is práce s azbestem: an employer must notify the krajská hygienická stanice at least 30 days ahead, unless exposure is sporadic and short, and the KHS issues a decision permitting the work after the protective measures are discussed with it; outside an employment relationship, the zadavatel stavby, the zhotovitel or anyone taking part in the building work (§ 12 písm. d zákona č. 309/2006 Sb.) who intends to do asbestos work must notify at least 3 days ahead, again unless exposure is sporadic and short (§ 41 odst. 1, 3 and 7 zákona č. 258/2000 Sb., text in force 1 Nov 2026); no general owner duty to remove intact asbestos was found in that statute — verify with the KHS. Removal est. 1,500–4,000 CZK/m² roof (≈ €62–€164 at 24.340 CZK/EUR, ČNB rate 3 Nov 2026; 2026 contractor ranges — no official price statistic was found, verify with abatement quotes).

### Mandatory diagnostics at sale

| Document | Required because | Validity / penalty |
|---|---|---|
| **PENB (Průkaz energetické náročnosti budovy)** | All sales and rentals (with limited exceptions) — § 7a zákona č. 406/2000 Sb. | 10 yrs validity, or until a major change or a change of the heating, cooling or hot-water system; **penalty up to 200k CZK for FO and PO alike** if missing (§ 12 odst. 2 písm. a + § 12a odst. 4 písm. a, text in force 1 Nov 2026, source zakonyprolidi.cz) |
| **List vlastnictví aktuální** | All sales (verify owner + zatížení) | Selected data free via Nahlížení do KN (no registration); ověřený výpis at Czech POINT 100 CZK first page + 50 CZK each further page (2026 data, source: DIA Czech POINT service sheet v1.1, 1 Jul 2026; ČÚZK Nahlížení) |
| **Snímek z katastrální mapy** | All sales | Map view free via Nahlížení do KN; ověřený snímek at Czech POINT 100 CZK first page + 50 CZK each further page (2026 data, source: DIA Czech POINT service sheet v1.1) |
| **Bezdlužnost SVJ** | If apartment in SVJ | At signing |
| **Geometrický plán** | If parcel split / new build | Per-case |
| **BPEJ** (bonita půdy) | Agricultural land sales | Per-case |
| **Souhlas věřitele/banky** | If pre-existing zástava | At signing |

**PENB exceptions** (§ 7a odst. 5 and 10 zákona č. 406/2000 Sb., text in force 1 Nov 2026):
- Buildings with total energeticky vztažná plocha < 50 m²
- Stavby pro rodinnou rekreaci used only part of the year, with estimated energy use < 25 % of year-round use
- Kulturní památka, or a building inside a památková rezervace
- Places of worship; industrial, workshop and agricultural buildings using up to 195 MWh a year
- Buildings built and last majorly changed before 1 Jan 1947: no PENB at sale or rental only if both parties agree in writing

**Rentals already covered**: PENB must be obtained and shown for the rental of a whole building and, since 1 Jan 2016, of a unit or ucelená část budovy; the energy class must appear in listings, and an agent who has not received the graphic part must state the worst class (§ 7a odst. 2–3 zákona č. 406/2000 Sb.).

### Climate change projections (ČHMÚ)

- +1 °C in 2021–2040 vs 1981–2010, rising at a similar pace to 2050 whatever the emissions scenario; end of century +2.0 °C (RCP4.5) or +4.1 °C (RCP8.5) vs 1981–2010 (2021 data, source MŽP Strategie přizpůsobení se změně klimatu v podmínkách ČR, aktualizace 2021, ČHMÚ model ensemble) — rates/figures may have changed since
- +2 °C by mid-century vs 1981–2010 under the most probable emissions scenario (CMIP6 downscaled to 0.5 km; source klimatickazmena.cz, Ústav výzkumu globální změny AV ČR, page live 2026-11-03)
- Long-term drought: existing data suggest Jihomoravský and Olomoucký kraj and hl. m. Praha are most threatened, and partly Zlínský, Moravskoslezský, Vysočina, Pardubický, Královéhradecký, Středočeský, Plzeňský and Ústecký kraj (2021 data, source MŽP Strategie přizpůsobení se změně klimatu v podmínkách ČR, aktualizace 2021) — rates/figures may have changed since. Kraj-level only
- Warmer winters: more rain instead of snow and the snow line moving higher, which may affect Czech ski resorts (2021 data, source MŽP strategy 2021); winter precipitation is projected to rise slightly but fall mostly as rain at low and middle altitudes (source klimatickazmena.cz)
- Heat: the frequency of extreme-temperature periods and the severity of their impacts are expected to rise; the longest such periods so far were recorded in the lowlands and middle altitudes of western, north-western, central and eastern Bohemia and southern Moravia (2021 data, source MŽP strategy 2021)
- Heavy rain: climate scenarios generally project more frequent and more intense heavy rainfall; flash floods can occur practically anywhere in CZ, even away from permanent streams (2021 data, source MŽP strategy 2021)
- Vegetation fires: rising in number, with frequency and severity expected to keep rising (2021 data, source MŽP strategy 2021); the largest fire recorded in CZ burned ~1,060 ha of NP České Švýcarsko near Hřensko (Ústecký kraj), 24 Jul – 12 Aug 2022 (2022 data, source Správa NP České Švýcarsko, Ročenka 2022) — rates/figures may have changed since; before 2022, the May 2012 fire between Bzenec, Strážnice and Ratíškovice (~200 ha of forest, Jihomoravský kraj) was rated the most extensive of the previous 20 years (source MŽP strategy 2021)

---

## Section: `--mains`

### National database

- **SOVAK ČR** (Sdružení oboru vodovodů a kanalizací): `https://www.sovak.cz/`
- Statistical data per provider; not parcel-level
- National base rates: 95.6 % of residents supplied by public water mains, 90.8 % living in buildings connected to public sewers; lowest kraj coverage Plzeňský (water 87.5 %) and Liberecký (sewer 74.9 %); Praha 100 % for both (2025 data, source ČSÚ Tab. 02.07 and krajské správy; MZe VÚME/VÚPE administrative data, not comparable with pre-2024 series). Kraj-level only — never a parcel-level claim

### Major operators

| Operator | Coverage |
|---|---|
| **PVK (Pražské vodovody a kanalizace)** | Praha — 51 % Veolia Holding Česká republika, 49 % city-owned PVS since 20 Sep 2018; infrastructure owned by hl. m. Praha and leased to PVK (2025 data, source PVK výroční zpráva 2025) |
| **SčVK (Severočeské vodovody a kanalizace)** | Ústecký + Liberecký kraj + město Roztoky u Prahy (source: scvk.cz) — 100 % owned by the municipal Severočeská vodárenská společnost since 1 Jan 2019, not Veolia (source: severoceskavoda.cz) |
| **Středočeské vodárny** (Veolia) | Středočeský kraj parts |
| **Královéhradecká provozní** (Veolia) | former okres Hradec Králové + edges of neighbouring districts (source: veolia.cz) |
| **Moravská vodárenská** (Veolia) | okresy Olomouc + Prostějov, almost 227k residents supplied (source: veolia.cz) |
| **BVK** (Brněnské vodárny a kanalizace) | Brno — 51.004 % Statutární město Brno, 46.272 % SUEZ International, 2.724 % small shareholders (31 Dec 2024 data, source bvk.cz) — rates/figures may have changed since |
| **OVAK** (Ostravské vodárny a kanalizace) | Ostrava — 50.13 % SUEZ International, 40.60 % Statutární město Ostrava, 9.27 % others (2026 page, source ovak.cz) |
| **Vodárna Plzeň**, **VaK Mladá Boleslav** | regional |
| Many obecní/místní | Smaller obce, often public ownership |

Veolia ČR group = largest operator: 2.7 million residents supplied with drinking water in more than 600 towns and municipalities, 2.1 million connected to the sewers it operates (2025 data, source veolia.cz). That is ≈ 26 % of residents on public water mains (computed: 2.7 M ÷ (95.6 % × 10,915,839 residents at 31 Dec 2025), inputs veolia.cz + ČSÚ).

### Verification

1. Check **obec website** under "Životní prostředí > Vodovody a kanalizace"
2. Listing language:
   - "kanalizace" / "obecní kanalizace" = mains drains
   - "septik" / "domovní ČOV" / "žumpa" = individual / cesspit
   - "vodovod ano / kanalizace ne" = mains water but no mains sewer
3. **Est. heuristic, no official obec-size split found**: obce above ~500 obyv usually have mains; villages below ~200 obyv often lack a mains sewer. Calibration: 95.6 % of residents get public mains water and 90.8 % live in buildings on public sewers (2025 data, ČSÚ, above) — verify the specific address with the obec or the VaK operator

### Costs

*est. 2026 contractor ranges — no official statistic for these costs was found; verify with quotes. The odběratel (normally the owner of the connected land or building, § 2 odst. 6) pays for the vodovodní or kanalizační přípojka unless agreed otherwise; the operator repairs and maintains přípojky laid in land forming public space (§ 3 odst. 6–7 zákona č. 274/2001 Sb., text in force 1 Jul 2025).*

| Scenario | Cost |
|---|---:|
| Connection where available | est. 30,000–80,000 CZK |
| Mains drains construction (per parcel) if obec has trunk line | est. 50,000–150,000 CZK |
| Septik to mains conversion | est. 80,000–200,000 CZK |
| Domovní ČOV (modern compliant) install | est. 100,000–250,000 CZK |
| Žumpa replacement | est. 60,000–150,000 CZK |

---

## Cost benchmarks (CZ 2026)

*No primary source for contractor or market prices was found: rows marked est. are estimates (with inputs or a reference in the cell where one exists); rows marked ⚠️ quote provider price lists or secondary articles (read Nov 2026) — verify with written quotes. The cadastre-fee and property-tax rows and the tarif references are statutory / computed (see `--tax`).*

| Work | Cost (CZK) |
|---|---:|
| PENB (rodinný dům) | 4,700–7,500+ (provider price lists ⚠️, Nov 2026: energodum.cz from 4,700–5,000; budovyprukaz.cz 6,000–7,500 by size; energeticka-narocnost-budov.cz from 7,000) |
| PENB (bytový dům) | 7,500–20,000 (provider price lists ⚠️, Nov 2026: energodum.cz from 7,500–8,500; budovyprukaz.cz 8,500 for 2–5 units to 20,000 for 41–60 units) |
| Notary / advokát | est. 0.5–1.5 % of price (tarif reference ≈ 0.26–0.57 % per act on CZK 5,000,000, computed — see `--tax`) |
| Cadastre registration fee | 2,000 per návrh na vklad (1,600 online via Identita občana) (2026 data, source: ČÚZK) |
| **Daň z nemovitých věcí (annual, residential)** | 210–5,765 for the flats computed in `--tax`; 11,025 for the two-floor Praha house at místní koeficient 5.0 (computed) |
| Septik to mains | est. 80,000–200,000 (same contractor est. as `--mains` › Costs; no price source found — verify with quotes) |
| Roof (terracotta tile, 200 m²) | est. 250,000–500,000 (no price source found for a complete roof — verify with quotes; clay tiles from 170 CZK/m², secondary: ceskestavby.cz, published 28 Dec 2019, modified 20 Oct 2026 ⚠️ — rates/figures may have changed since) |
| Asbestos removal (200 m² roof) | est. 46,000–110,000 excl. DPH, removal and disposal only (computed: 200 m² × removal 150–350 CZK/m² + disposal 80–200 CZK/m², secondary: energozrouti.cz, 8 Mar 2026 ⚠️); new roofing extra, see the row above |
| Energy retrofit (Class C → A) | est. 800,000–2,500,000 (no price source found — verify with quotes; scale reference: the NZÚ bezúročný úvěr reaches CZK 2,000,000 per rodinný dům, see Active fiscal incentives) |
| Radon retrofit (VMC + sealing) | est. 50,000–200,000 (no price source found — verify with quotes; vyhláška č. 362/2016 Sb. § 2 allows a state dotace only for a byt or rodinný dům in permanent use, permitted by 28 Feb 1991, with average radon above 1,000 Bq/m³, and only if the measure brings it below 300 Bq/m³ or cuts it by ≥ 75 %) |
| Building inspection (independent) | 7,050–20,000+ for a rodinný dům (realitakroku.cz, 5 Sep 2026, summary of public price lists ⚠️: 8,000–10,000 and up for help at a viewing, 13,000 to over 20,000 for a detailed inspection, comprehensive variants over 30,000; stavnemovitosti.cz price list ⚠️, Nov 2026: dům ≤ 150 m² 7,050 basic viewing to 19,000 full inspection; a byt from 4,000 for help at a viewing per realitakroku.cz) |
| **Total transaction cost (buyer side)** | est. ~1–2 % of price (computed tarif reference ≈ 0.33–0.88 % on CZK 5,000,000 incl. the vklad fee, excl. DPH — see `--tax`) |

## Active fiscal incentives (2026)

- **Nová zelená úsporám 2026+ (NZÚ)** — now loan-based: owners of rodinné domy, SVJ and bytová družstva can get a **bezúročný úvěr** (NZÚ compensates the interest) up to **CZK 2,000,000 per rodinný dům** and **CZK 750,000 per flat in a bytový dům**, offered by banks and stavební spořitelny from autumn 2026; direct grants are reserved for vulnerable households; applications 25 Jun 2026 (10:00) – 31 Oct 2029 or until the allocation runs out (2026 data, source: MŽP press release 24 Jun 2026)
- **NZÚ Light** (vulnerable / lower-income households) — advance grant up to **CZK 400,000** for insulation and efficient heat sources; SVJ / družstva up to CZK 120,000 per flat owned by a vulnerable household (2026 data, source: MŽP press release 24 Jun 2026)
- **Heat pumps / biomass / FVE inside NZÚ Light** — fixed amounts per measure, e.g. tepelné čerpadlo vzduch-voda CZK 150,000, vzduch-vzduch CZK 100,000, kotel na biomasu CZK 120,000, FVE ≥ 3 kWp CZK 120,000 (2026 data, source: SFŽP NZÚ Light závazné pokyny — rodinné domy, May 2026); other owners finance the same measures through the NZÚ loan; some obce add their own subsidies
- **Oprav dům po babičce** (complex renovation, CZK 50,000–1,000,000) — intake temporarily closed, allocation exhausted (2026-10-23 verified, source: novazelenausporam.cz)
- **Kotlíkové dotace** — ❌ ENDED 31 Aug 2024; boiler replacement continued via NZÚ / NZÚ Light / Oprav dům po babičce (2026 data, source: SFŽP ČR)
- **No income-tax credit for retrofits** — zákon č. 586/1992 Sb. (znění 01.08.2026) contains no energy-retrofit sleva na dani; support runs through NZÚ only (2026-10-23 verified, source: zakonyprolidi.cz 1992-586)

## Common listing platforms

- **Sreality.cz** — full extraction, includes cenová mapa
- **Bezrealitky.cz** — privates, no agency
- **Reality.idnes.cz**, **UlovDomov.cz** (rentals aggregator), **ČeskéReality.cz** (agency-listing aggregator)
- **REMAX, M&M, Sting, Century 21** — agency networks
- **Hyperinzerce, Annonce** — older classifieds, sometimes hidden gems

## Caveats unique to CZ

- **Nabývací daň abolished 2020** — buyer-side costs are very low (est. ~1–2 %) compared to W. Europe (est. 10–13 %); both figures are market estimates with no primary source — verify with quotes (see `--tax`)
- **Daň z nemovitých věcí ~1.8× from 2024** + local koeficient 0.5–5.0 from 2025 — bills changing significantly; inflační koeficient 1.0 for 2026 and 2027, so year-to-year changes now come from the obec's koeficient (2026-10-23 verified, source: Finanční správa; MF press release 14 Jul 2026)
- **Among the highest-radon countries in Europe** (est. — verify radon-index data at suro.cz) — test before buying granite-substrate areas
- **Krátkodobé ubytování (Airbnb) heavily restricted in Praha**; eTurista national register NOT in force — zákon č. 159/1999 Sb. is still in its znění of 1 Mar 2021 with no eTurista provisions (2026-10-23 verified, source: zakonyprolidi.cz 1999-159), so the planned 1 Jul 2025 launch did not happen; new launch date unconfirmed — secondary sources disagree (e-turista.cz, update 19 Sep 2026: MMR draft novela proposes 1 Jan 2028; ubytovacka.cz: MMR plans 2027, no date set) — verify at mmr.gov.cz / psp.cz; EU reg 2024/1028 applies from 20 May 2026 in opt-in / opt-out mode — Member States need not run a registration scheme, but any scheme or platform-data request must follow the Regulation (European Commission DG GROW news, 20 May 2026)
- **Panelové domy** (1948–1989 socialistická panelová výstavba): variable quality; asbestos in joints common; check rekonstrukce status
- **NOZ 2014 reform** merged building+land registers; pre-2014 properties may have legal complexity
- **eTurista not yet mandatory** — until it launches, hosts keep the existing duties (guest book, foreigner reporting to Policie ČR via Ubyport, local poplatek z pobytu) (secondary: e-turista.cz, ubytovacka.cz, Sep 2026 — verify at mmr.gov.cz)
- **PENB mandatory at sale and at rental** (§ 7a odst. 2–3 zákona č. 406/2000 Sb.), fine up to **200,000 CZK** for a natural or legal person (§ 12 odst. 2 písm. a, § 12a odst. 4 písm. a) (2026-10-23 verified, source: zákon č. 406/2000 Sb. znění 01.08.2026, zakonyprolidi.cz)
- **PIT capital gain 15 % / 23 %** if sold within **5 yrs** (pre-2021 acquisitions) or **10 yrs** (from 1 Jan 2021 onwards) — exempt where the seller had bydliště in the home for 2+ yrs immediately before the sale (§ 4 odst. 1 písm. a ZDP), or where proceeds go to own bytová potřeba (§ 4 odst. 1 písm. a / b + § 4b ZDP) (2026-10-23 verified, source: zákon č. 586/1992 Sb. znění 01.08.2026, zakonyprolidi.cz)
- **VAT 21 % on novostavby**; **12 % reduced rate** (since 1 Jan 2024 — konsolidační balíček 349/2023 Sb. merged former 10 % + 15 % reduced rates into a single 12 %) for stavby pro sociální bydlení = rodinný dům ≤ 350 m² podlahové plochy / obytný prostor (byt) ≤ 120 m², or a bytový dům where more than half the floor area is such byty (§ 48a + § 49 zákona č. 235/2004 Sb., restructured by zákon č. 461/2024 Sb. from 1 Jul 2025). Since 1 Jul 2025 only the first supply of a completed building made by the end of the 23rd calendar month after the month of completion is taxed; other supplies are VAT-exempt (§ 56 odst. 1) (2026-10-23 verified, source: zákon č. 235/2004 Sb. znění 01.01.2026 and zákon č. 461/2024 Sb., zakonyprolidi.cz)
- **Polození bytového domu** (basement / shelter requirements) — varies by obec
- **Foreign buyers — residential parity, farmland reciprocity**: no nationality-based restriction on buying flats, houses or commercial property — the devizový-zákon limits (§ 17 zákona č. 219/1995 Sb.) lost effect when the EU-accession transition periods ended (residential 1 May 2009, farmland 1 May 2011; secondary: e15.cz) and the whole devizový zákon was repealed as of 18 Oct 2016 (zákon č. 323/2016 Sb.). **Since 1 Jul 2024**, however, § 3d zákona č. 334/1992 Sb. (inserted by zákon č. 183/2024 Sb.) bars a state, its citizens, residents and companies from acquiring **zemědělská půda** where that state's law does not let Czech citizens, residents or companies acquire farmland. Exempt: zahrada, a parcel < 2,000 m², a parcel forming one functional unit with the buyer's building, land tied to a jednotka; buyers from the EU, EEA, Switzerland or a treaty state; acquisition into a marital property regime where one spouse qualifies, by inheritance, from a direct relative / sibling / spouse, or by exchange. Same ČÚZK katastr filing otherwise; strategic-asset purchases (kritická infrastruktura) fall under FDI screening, zákon č. 34/2021 Sb. (účinnost 1 May 2021) (2026-10-23 verified, source: zakonyprolidi.cz 1992-334 § 3d, 2024-183, 1995-219, 2021-34).
- **Skrytá vada — § 2129 občanského zákoníku (zákon 89/2012 Sb.)**: buyer of a building joined to land by a solid foundation must notify (vytknout) the seller of a hidden defect within **5 years** of acquisition, or the court will not grant rights from defective performance if the seller objects (§ 2129 odst. 2); the seller has no such objection where the defect results from a fact the seller knew or must have known at handover (§ 2129 odst. 2). For **consumer buyers (B2C)**, **§ 2129 odst. 3 OZ** presumes that a defect manifesting within **2 years** of the passing of risk existed at that time, unless the nature of the defect rules this out (§ 2161 covers movable goods — § 2158) (2026-10-23 verified, source: zákon č. 89/2012 Sb. znění 01.01.2026, zakonyprolidi.cz).
- **Beneficial-ownership registration (zákon č. 37/2021 Sb., účinnost 1 Jun 2021, which repealed část pátá of zákon č. 304/2013 Sb.)**: if buying via Czech s.r.o. or other právnická osoba, **evidence skutečných majitelů** registration is **mandatory** (rejstříkový soud, or a notary — § 34) — penalty up to **CZK 500,000** where the entity fails to register even within the deadline set by the court (§ 55 odst. 1 písm. a, odst. 3). The advokátní tarif (vyhláška č. 177/1996 Sb.) governs the legal-services fee schedule (2026-10-23 verified, source: zakonyprolidi.cz 2021-37, 1996-177).

## Reddit / forum sources

- **r/czech** (country subreddit, mixed CZ/EN), **r/praha** (small)
- **r/Prague** (main English-language Prague subreddit), **r/praguecity**, **r/czechrepublic**
- **Bezrealitky blog** (platform articles, not a forum)
- **CenovaMapa.cz**: commercial valuation / price-map app, not a community; treat as a secondary aggregator
- Expat: **InYourPocket Prague** (city guide), **Expats.cz** (English-language news and guides; no forum found, `expats.cz/forum` returns 404 as of 2026-10-23)
- Facebook: "Bydlení v Praze", "Reality bez realitky"

## Verification authorities

| Authority | When to call |
|---|---|
| **ČÚZK / Katastrální úřad** | LV verification, parcela verification, vlastník/zatížení |
| **Obecní úřad / Stavební úřad** | Permit history (kolaudace), černá stavba (unpermitted build) check, územní plán |
| **Notář / advokát** | Final kupní smlouva, smluvní jistota, escrow |
| **Provozovatel VaK** (operator) | Mains drains verification |
| **Krajský úřad — odbor životního prostředí** | Záplavová zóna confirmation |
| **Katastrální pracoviště** | Walk-in for full LV with all encumbrances |
| **SVJ** (apartment owners' assoc.) | Bezdlužnost, fond oprav stav, poplatky |
| **Bytové družstvo** (if cooperative) | Different ownership rules — check carefully |

## Quirks to know

- **Parcela vs jednotka**: bytová jednotka has separate LV from the building's parcela; verify both
- **Lhůta na nahlížení**: free LV view is shortened (no historical owners or pohledávky); for full info → Czech Point or paid extract
- **Živnost vs nájem**: the same letting can fall under different tax and licence regimes depending on how systematic it is — get expert advice (see `--rental`); the eTurista register is not in operation yet (MMR: internal testing, enabling amendment to zákon č. 159/1999 Sb. not yet passed; MMR eTurista page, read 2026-10-23)
- **Praha 1**: extreme regulation pressure on Airbnb; pending change
- **BPEJ kód** for agricultural land — affects valuation + dotace
- **Plomba katastru**: red flag if "P" letter on LV — pending change
- **Územní plán** must allow intended use — verify at obec before any non-residential plans
- **Stavební uzávěra** rare but devastating — verify obec doesn't have one for the lokalita
- **2014 NOZ harmonization** — pre-2014 properties may still have separated building+land titles → unification recommended

## Source URL templates

| Source | URL pattern |
|---|---|
| ČÚZK Nahlížení | `https://nahlizenidokn.cuzk.gov.cz/` |
| ČÚZK DPN (unregistered) | `https://dpn.cuzk.gov.cz/` |
| ČÚZK Dálkový přístup do KN (paid, registered) | `https://cuzk.gov.cz/aplikace-dp` |
| Sreality search | `https://www.sreality.cz/hledani/prodej/byty/<region>/<obec>` |
| Sreality cenová mapa | `https://www.sreality.cz/cenova-mapa` (single-page map; `/cenova-mapa/<region>` paths return 404 on 2026-10-23) |
| Bezrealitky | `https://www.bezrealitky.cz/vypis/nabidka-prodej/<byt-dum-pozemek>/<obec>` (updated 2026-10-23: old `/<region>/<obec>` pattern returned 404 when tested with `/praha`) |
| ČSÚ ceny bytů | `https://csu.gov.cz/produkty/indexy-realizovanych-cen-bytu-<X>-ctvrtleti-<year>` |
| ŘSD sčítání dopravy (CSD2020 web map) | `https://scitani.rsd.cz/CSD_2020/pages/informations/default.aspx` |
| ŘSD CSD 2025 results (XLSX + PDF maps) | `https://www.rsd.cz/silnice-a-dalnice/scitani-dopravy` |
| Záplavová území | `https://voda.gov.cz/?page=zaplavova-uzemi-mapa` |
| ČHMÚ HPPS | `https://hydro.chmi.cz/hppsoldv/` |
| ČAP povodňové mapy | `https://www.cap.cz/povodnove-mapy` |
| ČGS svahové nestability | `https://mapy.geology.cz/svahove_nestability/` |
| ČGS radon | `http://www.geology.cz/demo/CD_RADON50/index/info.htm` |
| ČGS Radon web map | `https://mapy.geology.cz/radon/` (updated 2026-10-23: replaces dead `geologicke-mapy.cz/radon/`) |
| SÚRO radonové mapy | `https://www.suro.cz/cz/prirodnioz/radonove-mapy` |
| Geofyzikální ústav seismika | `https://www.ig.cas.cz/vyzkum-a-vyuka/observatore/ceska-regionalni-seismicka-sit/` (updated 2026-10-23) |
| eTurista (NOT in operation) | `https://eturista.gov.cz/` (HTTP 503 on 2026-10-23; no amendment to zákon č. 159/1999 Sb. enacting the register appears in the psp.cz Sbírka record) |
| Finanční správa daň z nemovitostí | `https://financnisprava.gov.cz/cs/dane/dane/dan-z-nemovitych-veci` |
| SOVAK (water operators) | `https://www.sovak.cz/` |
| MMR ČR (housing policy) | `https://mmr.gov.cz/` |
| MŽP (environment) | `https://mzp.gov.cz/` |

## Status

✅ **Fully populated**; fast-changing sections re-verified as of 2026-10-23, figures with no current primary source labelled est., by source tier and date, as curated wisdom or verify-at (initial population 2026-04-25).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (all primary state agencies, multi-source corroborated). MEDIUM for short-let regulation (in transition: the eTurista register is not in operation, MMR's amendment to zákon č. 159/1999 Sb. has not yet passed the Poslanecká sněmovna, and ČR runs no registration procedure under EU Regulation 2024/1028, which has applied since 20 May 2026 in opt-in / opt-out mode; Praha-specific rules pending) (sources: MMR eTurista page, read 2026-10-23; European Commission DG GROW news, 20 May 2026).

## Extension TODOs (deepen on first real run)

- [ ] Per-kraj traffic data extraction (CSD2020 has regional sub-pages)
- [ ] Per-obec daň z nemovitých věcí místní koeficient (need scraping per obec — 6,258 obcí at 31 Dec 2025, source ČSÚ — start with top 100)
- [ ] eTurista registration walkthrough once portal is live
- [ ] Praha městské části short-let rules (each MČ has own approach)
- [ ] BPEJ codes for agricultural land valuation
- [ ] Bytové družstvo vs SVJ distinction tooling
- [ ] Asbestos detection workflow for panelové domy (1948-1989)

## Update history

- **2026-04-25** — Initial population
- **2026-10-23** — Refresh wave plus a gap-closing pass: the playbook-level stamp moves to 2026-10-23 because every fast-changing section is now re-verified (`--price`, `--work` and `--traffic` in the refresh; `--tax`, `--rental`, `--risks`, `--mains` and Cost benchmarks in the gap-closing pass below). Facts changed / confirmed / unverifiable per section. Fully re-verified: `--price` 4 / 6 / 3, `--work` 5 / 5 / 2, `--traffic` 9 / 5 / 1, Active fiscal incentives 7 / 0 / 0, Common listing platforms 1 / 9 / 0, Source URL templates 8 / 14 / 0. Partly re-verified: Country profile 3 / 1 / 4, `--tax` 14 / 17 / 3, `--rental` 12 / 3 / 4, `--risks` 20 / 13 / 9, `--mains` 9 / 4 / 6, Cost benchmarks 2 / 0 / 10, Caveats 9 / 7 / 2, Quirks 0 / 1 / 1, Verification authorities 2 / 5 / 1, Reddit / forum sources 1 / 4 / 2. Main changes: property-tax building rates corrected to the post-2024 values (3.50 / 11.00 / 14.50 / 18.00 Kč/m²) and the cadastre fee to 2,000 CZK; eTurista recorded as not in operation, and EU Regulation 2024/1028 as opt-in / opt-out with no Czech registration procedure; Q2 2026 ČSÚ price trend and 2025 realized kraj prices; 2025 wages, the minimum wage and 2026 paušální daň; CSD 2025 traffic census; NZÚ 2026+ loans (Kotlíkové dotace ended, no retrofit tax credit); farmland reciprocity rule since 1 Jul 2024 (§ 3d zákona č. 334/1992 Sb.); PENB fine 200,000 CZK, with rentals already covered; radon categories, the seismic record and the meaning of the ČAP zones corrected; PVK / SčVK ownership updated and the Veolia share recomputed (≈ 26 %); dead URLs replaced (ČGS radon, GFÚ, Sreality and Bezrealitky patterns). Follow-up consistency fixes: eTurista wording in Status and Quirks, the ČÚZK Dálkový přístup label in `--price`, the obce count in the TODOs, est. labels on the buyer-cost caveat. Left open by the refresh: Praha short-let positions (60 days, SVJ consent, zone bans), notary / makléř percentages and contractor cost ranges (est.), the build-era table, the regional radon list, BVK / OVAK ownership, the Facebook groups; all but the Facebook groups were settled in the gap-closing pass below (sourced, or labelled est. / unsourced / wisdom).
  - Gap-closing pass (checks dated 2026-11-03): `--rental`, `--tax`, `--risks`, `--mains` and Cost benchmarks closed. Facts confirmed / changed / relabelled: `--rental` 6 / 6 / 2, `--tax` 3 / 2 / 4, `--risks` 3 / 8 / 5, `--mains` 0 / 2 / 2, Cost benchmarks 0 / 5 / 7 (total 12 / 23 / 20). Main changes: Praha short-let positions sourced or marked unsourced (60-day cap unsourced, SVJ consent at odds with NS 26 Cdo 854/2022, no zone ban in force), Praha 1 enforcement and sněmovní tisk 106 / 107 added; pre-2024 property-tax rates confirmed against Finanční správa; notary, makléř and buyer-side figures kept est., with computed tarif references for the notary and buyer-side totals and the provize rule of zákon č. 39/2020 Sb. for the makléř; PENB, building-inspection and asbestos rows re-based on dated provider or secondary price lists; the regional radon list replaced by the 711 obce of příloha č. 25 vyhlášky č. 422/2016 Sb.; the build-era table labelled as wisdom with its legal dates re-sourced; BVK / OVAK ownership sourced. Still est. with no price source: septik, complete roof, energy retrofit, radon retrofit and mains connection costs.
