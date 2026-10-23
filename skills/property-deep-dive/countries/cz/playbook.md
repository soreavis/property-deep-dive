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

**Major 2024 reform** (Konsolidační balíček, zákon č. 349/2023 Sb.) raised rates by ~80 % (~1.8×) from 2024 and introduced the inflační koeficient.
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
| Pozemky (orná půda, zahrada, vinice, sad, chmelnice) | **1.35 % z ceny pozemku** (raised from 0.75 % by konsolidační balíček Act 349/2023 Sb. effective 1 Jan 2024) |
| Trvalé travní porosty + lesní pozemky | **0.45 % z ceny pozemku** (raised from 0.25 % since 1 Jan 2024) |
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

**Daň z nemovitých věcí is therefore very low compared to W. Europe** — est. ~€10–€240/yr for residential (computed: 50 m² byt × 1.20 in an obec ≤ 1,000 at místní koeficient 1.0 = 210 CZK; the 60 m² Praha byt above at místní koeficient 5.0 = 5,765 CZK).

### Transaction taxes (one-time at purchase)

- **Daň z nabytí nemovitých věcí (transfer tax)**: **ABOLISHED 26 September 2020** by zákon č. 386/2020 Sb. (liabilities whose filing deadline ended on or after 31 Mar 2020 lapsed) (2026-10-23 verified, source: zakonyprolidi.cz 2020-386).
- **Buyer pays**: only notary/lawyer fees + cadastre registration fee (**2,000 CZK** per návrh na vklad, položka 120 zákona č. 634/2004 Sb.; 20 % discount when filed online after an Identita občana login = 1,600 CZK, computed) + survey (2026 data, source: ČÚZK — Zápisy do KN; nv.cuzk.gov.cz)
- **Seller pays**: daň z příjmů (15 % up to 36× the average wage / 23 % above, § 16 ZDP) on the capital gain if sold within **5 years** (acquisitions before 1 Jan 2021 — zákon č. 386/2020 Sb. Čl. IV bod 2) or **10 years** (acquisitions from 1 Jan 2021 onwards — § 4 odst. 1 písm. b ZDP). Exempt instead: the seller's own rodinný dům / byt where the seller had bydliště for at least 2 years immediately before the sale (§ 4 odst. 1 písm. a), or proceeds used for own bytová potřeba (§ 4 odst. 1 písm. a / b + § 4b) — spent by the end of the tax year after the year of sale, or in the year before it (§ 4b odst. 2), and the receipt notified to the správce daně by the tax-return deadline for the year of sale (§ 4b odst. 3); verify with a daňový poradce (2026-10-23 verified, source: zákon č. 586/1992 Sb. znění 01.08.2026, zakonyprolidi.cz)

**Notary / advokát**: est. 0.5–1.5 % typical, negotiable (market practice — verify quotes)
**Realitní makléř**: est. 3–5 %, usually paid by seller (market practice — verify in the zprostředkovatelská smlouva)
**Total transaction cost** (buyer side): est. ~1–2 % of price (vs ~10–13 % in IT)

### Future risk

- **No tax rises pledged**: the programové prohlášení vlády approved 5 Jan 2026 states "Zavazujeme se nezvyšovat žádné daně" and "Zastavíme automatické valorizace daně z nemovitostí prostřednictvím inflačních koeficientů" — intent only, no amending bill found as of 2026-10-23; the inflační koeficient is 1.0 for 2027 regardless (2026 data, source: vlada.gov.cz programové prohlášení; MF press release 14 Jul 2026)
- **Main driver of year-to-year bill changes = the obec**: místní koeficient 0.5–5.0 (see above) — re-check the obec's vyhláška each year
- **Re-introduction of nabývací daň**: proposed periodically; the 2026 programme pledges no tax rises
- **Mortgage-interest deduction (watch — announced, no bill)**: the current cap is CZK 150,000/yr per household for housing financed from 1 Jan 2021 (§ 15 odst. 4 ZDP; housing obtained before 1 Jan 2021 keeps the pre-2021 rules, zákon č. 386/2020 Sb. Čl. IV bod 3) (2026 data, source: zákon č. 586/1992 Sb. znění 01.08.2026). On 7 Oct 2026 Finance Minister Alena Schillerová said on TV Nova that MF has a draft raising the cap by up to CZK 50,000 for people up to age 36, for existing and new mortgages, possibly from tax period 2027 (secondary: energozrouti.cz 10 Oct 2026; hn.cz 8 Oct 2026 — no bill found as of 2026-10-23; verify at mf.gov.cz / psp.cz). If enacted, worth at most CZK 7,500/yr in tax at the 15 % rate (computed: 50,000 × 15 %). The 2026 programme also pledges state support for mortgage interest on a young family's first home (vlada.gov.cz, 5 Jan 2026)

---

## Section: `--rental`

### Long-term residential

**Daň z příjmů z pronájmu (FO)** — § 9 Zákona o daních z příjmů:
- Two cost methods (must be uniform across all rentals):
  - **Skutečné výdaje** (actual expenses)
  - **Paušální výdaje 30 %** (deduction capped at 600,000 CZK, reached at 2 mil. CZK of rent) (source: Finanční správa, Pronajímatel page)
- Sazba 2026: **15 %** up to 36× average wage = ZD 1,762,812 CZK; **23 %** above (2026 data, source Finanční správa; average wage 48,967 CZK per nařízení vlády č. 365/2025 Sb.)
- Reportable on daňové přiznání (DAP) annually
- No social/health insurance contributions on § 9 rent (unlike OSVČ) (source: Veřejný ochránce práv leaflet, Sep 2026)
- Filing and payment deadlines for tax year 2025: 1 Apr 2026 (paper), 4 May 2026 (electronic), 1 Jul 2026 (via daňový poradce / advokát); the tax is due by the same date (2026 data, source Finanční správa)

### Short-term rentals (krátkodobé ubytování / Airbnb / Booking)

**Status**: in transition. No national STR registration and no statutory day cap in force as of 2026-10-23; an MMR amendment is pending (details below).

#### Current obligations (2026)

- **Trade licence**: volná živnost "Výroba, obchod a služby neuvedené v přílohách 1 až 3", obor **55 Ubytovací služby**; no qualification required, filing fee 1,000 CZK. Platform hosting offered systematically for profit is podnikání, and hosting without the licence is illegal business with the same tax and insurance duties (2026 data, sources Veřejný ochránce práv leaflet "Sdílená ekonomika", Sep 2026; GFŘ information č. j. 10352/23/7100-30118-012884)
- **DPH (VAT)**: accommodation services (CZ-CPA 55) take the **12 % reduced rate** (příloha č. 2 zákona o DPH, since 1 Jan 2024). Registration is mandatory once turnover exceeds 2,000,000 CZK in a calendar year (payer from 1 Jan of the next year) or 2,536,500 CZK within the year (payer from the next day). A non-payer who pays a service fee to a platform established outside ČR becomes an identified person and owes Czech VAT on that fee (2026 data, sources § 6 zákona č. 235/2004 Sb., version in force 2026; Finanční správa easy-to-read DPH guide; GFŘ information on VAT rates from 1 Jan 2024; Veřejný ochránce práv leaflet, Sep 2026)
- **Místní poplatek z pobytu** (local stay fee, not a tax): collected from each guest for stays of up to 60 days where the obec has introduced it by obecně závazná vyhláška; statutory maximum 50 CZK per person per day (§ 3d zákona č. 565/1990 Sb.). Praha charges the 50 CZK maximum per person per started day, excluding the arrival day (raised from 21 CZK by ZHMP resolution 32/81 of 16 Dec 2021; going higher needs a change to zákon o místních poplatcích) (sources: Veřejný ochránce práv leaflet, Sep 2026; Rada HMP materials on eud.praha.eu)
- **Hlášení cizinců**: every paying foreign guest, EU citizens included, must be reported to the cizinecká policie within 3 working days of arrival, via Ubyport (mandatory for businesses) or a paper form; keep a domovní kniha for 6 years; fine up to 50,000 CZK (2026 data, source Veřejný ochránce práv leaflet, Sep 2026)
- **Building use**: ubytovací služby are lawful in a building whose permitted use is "stavba ubytovacího zařízení"; running them in a "stavba pro bydlení" (bytový or rodinný dům) breaches the stavební zákon, fine up to 1,000,000 CZK; a change of use needs the stavební úřad (2026 data, source Veřejný ochránce práv leaflet, Sep 2026)
- **eTurista** (planned national register of accommodation and guests): **not live and not mandatory**. The enabling amendment to zákon č. 159/1999 Sb. (sněmovní tisk 761) stalled before third reading in 2025; without legislation, use of the system stays voluntary (source: MMR, Vyhodnocení AP 2024–2025). MMR's eTurista page says a new amendment is prepared for the Chamber and the system is in internal testing, with no launch date given (read 2026-10-23). The amendment had been due to take effect on 1 July 2025; that date was missed while the bill waited for its third reading (secondary: finance.cz, 30 Jun 2025)

#### EU Regulation 2024/1028

- Applies since **20 May 2026** in opt-in/opt-out mode: Member States are not obliged to introduce STR registration, but any registration system or platform-data request they introduce must go through the Regulation, with a national Single Digital Entry Point (2026 data, source European Commission DG GROW news, 20 May 2026)
- **Czechia: no registration procedure in force.** MMR's notice under Art. 13(1)(a)-(b) states that ČR applies no registration procedure anywhere on its territory and requests no activity data from STR platforms, adding that this may change (source: MMR eTurista page, read 2026-10-23)
- So there is no Czech STR registration number for platforms to require yet; one would arrive only with the pending amendment to zákon č. 159/1999 Sb.

#### Praha-specific (most restrictive)

- Praha 1 local referendum, 3–4 Oct 2025: question 3 (omezení krátkodobého ubytování) passed with 6,850 votes / 72.26 %, declared valid and binding on the městská část (sources: praha1.cz results page; ZMČ Praha 1 minutes, 4 Nov 2025)
- City wants (reported positions, not law; unsourced — verify with MHMP or ÚMČ Praha 1):
  - **Max 60 days/year** per byt for short-let
  - **SVJ (homeowners' association) approval** required
  - **Possibly ban** in worst-affected zones
- No statutory STR cap yet: MMR says its prepared amendment to zákon č. 159/1999 Sb. would let obce regulate short-term-rental conditions (source: MMR eTurista page). Per novinky.cz (6 Oct 2026, secondary), the draft is in připomínkové řízení and would allow day caps, guest limits, seasonal bans and mandatory host registration; each obec's rules would have to be notified to the European Commission and could not take effect until any Commission objections are resolved
- Some Pražské městské části: stricter local rules

#### Tax regime for Airbnb

- **With the trade licence (ubytovací služby)**: income under § 7 odst. 1 písm. b) ZDP, paušál 60 % (max 1,200,000 CZK), plus OSVČ social and health insurance (sources: GFŘ information č. j. 10352/23/7100-30118-012884; Veřejný ochránce práv leaflet, Sep 2026)
- **Without the licence** (still podnikání): § 7 odst. 1 písm. c), paušál 40 % (max 800,000 CZK). GFŘ treats platform accommodation as podnikání under § 420 OZ taxed under § 7, not § 9; per the ombudsman, platform letting is only exceptionally a nájem (same sources)
- **Paušální daň 2026**, I. pásmo: **9,162 CZK/month** all-in (100 CZK tax + 5,756 CZK pension insurance + 3,306 CZK health insurance), cut retroactively from 9,984 CZK with effect from 1 Jan 2026 and first due at the new amount on 20 Jul 2026. I. pásmo covers prior-year self-employment income up to 1 mil. CZK from any activity, more if most income qualifies for the 60 % / 80 % paušál (see `--work`) (2026 data, source Finanční správa)

### Strategic notes

- **Praha + Český Krumlov + Karlovy Vary + Brno + spa towns**: highest yields but biggest regulatory risk
- **South Bohemia, Šumava, Krkonoše**: tourist demand, less regulation
- **Wholly-rural / vesnice**: limited demand outside ski resorts
- **eTurista not live** as of 2026-10-23: no national registration duty or eTurista penalty yet; watch the MMR amendment to zákon č. 159/1999 Sb. (see above)
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
| **MŽP povodňové nebezpečí Q100** | `https://cds.mzp.cz/mapy/?MAP=mpn_100` (🟡 offline on 2026-10-23: MŽP maintenance notice after a security vulnerability — retry, or use voda.gov.cz meanwhile) | Hazard zones |
| **ČAP (Česká asociace pojišťoven) povodňové mapy** | `https://www.cap.cz/povodnove-mapy` | Insurance-grade flood zones (1-4) |
| **EDPP.cz online povodňová mapa** | `https://www.edpp.cz/online-povodnova-mapa-cr/` | Aggregated commercial map |
| **ČGS Svahové nestability (landslides)** | `https://mapy.geology.cz/svahove_nestability/` | Landslide registry + susceptibility |
| **ČGS Geofond sesuvy** | `https://mapy.geology.cz/arcgis/rest/services/Geohazardy/sesuvy_Geofond/MapServer` | API access |
| **ČGS / SÚRO Radon mapa** | `http://www.geology.cz/demo/CD_RADON50/index/info.htm` + `https://www.suro.cz/cz/prirodnioz/radonove-mapy` | Radon index 1-3 of geological substrate |
| **ČGS Radon web map** | `https://mapy.geology.cz/radon/` (updated 2026-10-23: replaces `http://www.geologicke-mapy.cz/radon/`, HTTP 404; linked from SÚRO) | Updated 1:50 000 radon maps of the geological subsoil (per SÚRO) |
| **Geofyzikální ústav AV ČR seismicita** | `https://www.ig.cas.cz/vyzkum-a-vyuka/observatore/ceska-regionalni-seismicka-sit/` (updated 2026-10-23: old `/observatorie/` path redirects to an image) | Earthquake monitoring |
| **SeismickaMapa.cz** | `https://seismickamapa.cz/` | Aggregated hazard map |
| **WEBNET West Bohemia swarms** | `https://www.ig.cas.cz/vyzkum-a-vyuka/observatore/lokalni-seismicka-sit-webnet/` (updated 2026-10-23: old `/observatorie/` path redirects to an image) | West-Bohemia microseism |

### Flood zones (záplavová zóna 1-4)

| Zóna | Riziko | Notes |
|---|---|---|
| **1** | Zanedbatelné | No restriction; insurance unaffected |
| **2** | Nízké | Possible insurance surcharge |
| **3** | Střední | Insurance can be expensive or refused, at each insurer's discretion |
| **4** | Vysoké | Often uninsurable for flood |

Source for address-level: ČAP map at `https://www.cap.cz/povodnove-mapy` (insurance-aligned). These are ČAP insurance tariff zones from the RZ2023 map set (built 2022–2023, 5th generation, Intermap Technologies); insurers may deviate from them (source: ČAP Povodňové mapy page). They are **not** the statutory záplavové území. Building limits come from the statute: no new buildings in the aktivní zóna záplavového území except water works and essential infrastructure (§ 67 odst. 1 zákona č. 254/2001 Sb.), and elsewhere in a záplavové území the vodoprávní úřad sets limits by opatření obecné povahy (§ 67 odst. 3). Check both layers: ČAP for insurability, voda.gov.cz for the statutory zone.

### Radon zones (radonový index podloží)

- Categories of the radonový index pozemku: nízký / střední / vysoký (source: SÚJB; ČGS)
- **Nízký** (low) — prevails on younger sediments (křídové pískovce, paleogenní and neogenní písky, pískovce, jílovce) (source: ČGS, Radon a geologie)
- **Střední** (medium) — prevails on the metamorphic crystalline rocks (pararuly, ortoruly) that cover a substantial part of the Bohemian Massif; metamorphic and magmatic rocks make up more than two thirds of the CZ geological substrate (source: ČGS, Radon a geologie)
- **Vysoký** (high) — prevails on magmatic rocks (granity, granodiority, durbachity, syenity) and silurské sedimenty (source: ČGS, Radon a geologie); regional examples: Vysočina, Krušné hory podhůří, Jižní Čechy granite belt, Krkonoše + Jizerské hory podhůří, Jeseníky (regional list not re-verified — the ČGS 1:50 000 map shows the prevailing category of the geological subsoil, not a plot value; a plot's radonový index needs an on-site measurement, per SÚJB)
- **CZ is among the highest-radon countries in Europe** (est., reflecting the granite-substrate geology of the high-index zones above — verify radon-index data at suro.cz)
- New buildings: legislative radon requirements since 1991, with mandatory protective measures on plots with a higher radon index (source: SÚJB); today anyone applying for a permit for a new building or extension with obytné or pobytové místnosti must have the radonový index pozemku determined (§ 98 odst. 1 zákona č. 263/2016 Sb., atomový zákon)
- Indoor reference level: 300 Bq/m³ in obytné místnosti (source: SÚJB)
- Older buildings (pre-1991): retrofit recommended in vysoký radon areas

**Mitigation cost**: est. 50,000–200,000 CZK (~€2,000–€8,000) (2026 contractor ranges — verify with quotes) — VMC, sealing, sub-floor ventilation

### Seismicity

- **Very low overall** — most of CZ in zone 1 (faible) per ČSN EN 1998-1
- **Active microseismic zones**:
  - **Western Bohemia / Vogtland** — Kraslicko, Nový Kostel: strongest West-Bohemian event of the last 100 years ML 4.6 on 21 Dec 1985 near Nový Kostel (MSK-64 intensity 6.5–7°, cracked walls and fallen chimneys up to 20 km from the epicentre); later swarms 2008 (ML 3.8), 2011 (ML 3.6), 2014 (ML 4.4), 2017 (ML 3.5), 2018 (ML 3.8); events above ML 4 can cause minor building damage (source: Geofyzikální ústav AV ČR, WEBNET pages)
  - **Hronovsko-poříčský zlom** (Královéhradecký kraj) — moderate
  - **Jeseníky** — minor
- For most properties, seismicity is **🟢 negligible**

### Build-era hazards

| Era | Hazards |
|---|---|
| **< 1948** (předválečné, válečné) | Lead, asbestos in roofing, weak foundations |
| **1948–1989 panelové domy** | Asbestos in joints + insulation, low-quality concrete (PVS issue), aging utility lines |
| **1948–1989 cihlové domy** | Better quality but asbestos + lead pipes likely |
| **1990–2000 "kvalitní privátní"** | DIY craftsmanship variability; possible no permit work |
| **2000–2008** | Building boom — uneven quality |
| **Post-2008** | Modern energy + fire standards (Vyhláška 268/2009) |
| **Post-2014 NOZ** | New civil code; older "anomalous" titles harmonized |

**Asbestos**: pre-1995 likely; obligatory removal if friabile; est. cost 1,500–4,000 CZK/m² roof (2026 ranges — verify with abatement quotes).

### Mandatory diagnostics at sale

| Document | Required because | Validity / penalty |
|---|---|---|
| **PENB (Průkaz energetické náročnosti budovy)** | All sales and rentals (with limited exceptions) — § 7a zákona č. 406/2000 Sb. | 10 yrs validity, or until a major change or a change of the heating, cooling or hot-water system; **penalty up to 200k CZK for FO and PO alike** if missing (§ 12 odst. 2 písm. a + § 12a odst. 4 písm. a, text in force 1 Aug 2026, source zákonyprolidi.cz) |
| **List vlastnictví aktuální** | All sales (verify owner + zatížení) | Free via Nahlížení |
| **Snímek z katastrální mapy** | All sales | Free via Nahlížení |
| **Bezdlužnost SVJ** | If apartment in SVJ | At signing |
| **Geometrický plán** | If parcel split / new build | Per-case |
| **BPEJ** (bonita půdy) | Agricultural land sales | Per-case |
| **Souhlas věřitele/banky** | If pre-existing zástava | At signing |

**PENB exceptions** (§ 7a odst. 5 and 10 zákona č. 406/2000 Sb., text in force 1 Aug 2026):
- Buildings with total energeticky vztažná plocha < 50 m²
- Stavby pro rodinnou rekreaci used only part of the year, with estimated energy use < 25 % of year-round use
- Kulturní památka, or a building inside a památková rezervace
- Places of worship; industrial, workshop and agricultural buildings using up to 195 MWh a year
- Buildings built and last majorly changed before 1 Jan 1947: no PENB at sale or rental only if both parties agree in writing

**Rentals already covered**: PENB must be obtained and shown for the rental of a whole building and, since 1 Jan 2016, of a unit or ucelená část budovy; the energy class must appear in listings, and an agent who has not received the graphic part must state the worst class (§ 7a odst. 2–3 zákona č. 406/2000 Sb.).

### Climate change projections (ČHMÚ)

- +1 °C in 2021–2040 vs 1981–2010, rising at a similar pace to 2050 whatever the emissions scenario; end of century +2.0 °C (RCP4.5) or +4.1 °C (RCP8.5) vs 1981–2010 (2021 data, source MŽP Strategie přizpůsobení se změně klimatu v podmínkách ČR, aktualizace 2021, ČHMÚ model ensemble) — rates/figures may have changed since
- +2 °C by mid-century vs 1981–2010 under the most probable emissions scenario (CMIP6 downscaled to 0.5 km; source klimatickazmena.cz, Ústav výzkumu globální změny AV ČR, page live 2026-10-23)
- More droughts (esp. Southern Moravia)
- Warmer winters → less snow → ski-resort impact (Krkonoše, Jeseníky, Šumava lower altitudes)
- Heat waves: longer + more intense
- Extreme rain events: increasing frequency
- Wildfires: rising in Šumava, South Moravia, North Bohemia forests

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
| **SčVK (Severočeské vodovody a kanalizace)** | Ústecký + Liberecký kraj + Roztoky — 100 % owned by the municipal Severočeská vodárenská společnost since 1 Jan 2019, not Veolia (source: severoceskavoda.cz) |
| **Středočeské vodárny** (Veolia) | Středočeský kraj parts |
| **Královéhradecká provozní** (Veolia) | former okres Hradec Králové + edges of neighbouring districts (source: veolia.cz) |
| **Moravská vodárenská** (Veolia) | okresy Olomouc + Prostějov, almost 227k residents supplied (source: veolia.cz) |
| **BVK** (Brněnské vodárny a kanalizace), **OVAK** (Ostravské vodárny a kanalizace) | Brno, Ostrava — regional (ownership not re-verified) |
| **Vodárna Plzeň**, **VaK Mladá Boleslav** | regional |
| Many obecní/místní | Smaller obce, often public ownership |

Veolia ČR group = largest operator: 2.7 million residents supplied with drinking water in more than 600 towns and municipalities, 2.1 million connected to the sewers it operates (2025 data, source veolia.cz). That is ≈ 26 % of residents on public water mains (computed: 2.7 M ÷ (95.6 % × 10,915,839 residents at 31 Dec 2025), inputs veolia.cz + ČSÚ).

### Verification

1. Check **obec website** under "Životní prostředí > Vodovody a kanalizace"
2. Listing language:
   - "kanalizace" / "obecní kanalizace" = mains drains
   - "septik" / "domovní ČOV" / "žumpa" = individual / cesspit
   - "vodovod ano / kanalizace ne" = mains water but no mains sewer
3. **Most populated obce > 500 obyv have mains**; **vesnice < 200 obyv often lack mains sewer**

### Costs

*est. 2026 contractor ranges — verify with quotes.*

| Scenario | Cost |
|---|---:|
| Connection where available | est. 30,000–80,000 CZK |
| Mains drains construction (per parcel) if obec has trunk line | est. 50,000–150,000 CZK |
| Septik to mains conversion | est. 80,000–200,000 CZK |
| Domovní ČOV (modern compliant) install | est. 100,000–250,000 CZK |
| Žumpa replacement | est. 60,000–150,000 CZK |

---

## Cost benchmarks (CZ 2026)

*est. 2026 contractor / market ranges — verify with quotes; the cadastre-fee and property-tax rows are statutory / computed (see `--tax`).*

| Work | Cost (CZK) |
|---|---:|
| PENB (rodinný dům) | 2,500–5,000 |
| PENB (bytový dům) | 5,000–15,000 |
| Notary / advokát | 0.5–1.5 % of price |
| Cadastre registration fee | 2,000 per návrh na vklad (1,600 online via Identita občana) (2026 data, source: ČÚZK) |
| **Daň z nemovitých věcí (annual, residential)** | est. 200–5,800 (computed range, see `--tax`) |
| Septik to mains | 80,000–200,000 |
| Roof (terracotta tile, 200 m²) | 250,000–500,000 |
| Asbestos removal (200 m² roof) | 200,000–500,000 |
| Energy retrofit (Class C → A) | 800,000–2,500,000 |
| Radon retrofit (VMC + sealing) | 50,000–200,000 |
| Building inspection (independent) | 8,000–25,000 |
| **Total transaction cost (buyer side)** | est. ~1–2 % of price |

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

✅ **Fully populated** as of 2026-04-25.
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
- **2026-10-23** — Refresh wave, partial: the playbook-level stamp stays at 2026-04-25 because `--tax`, `--rental`, `--risks` and `--mains` were not fully re-verified. Facts changed / confirmed / unverifiable per section. Fully re-verified: `--price` 4 / 6 / 3, `--work` 5 / 5 / 2, `--traffic` 9 / 5 / 1, Active fiscal incentives 7 / 0 / 0, Common listing platforms 1 / 9 / 0, Source URL templates 8 / 14 / 0. Partly re-verified: Country profile 3 / 1 / 4, `--tax` 14 / 17 / 3, `--rental` 12 / 3 / 4, `--risks` 20 / 13 / 9, `--mains` 9 / 4 / 6, Cost benchmarks 2 / 0 / 10, Caveats 9 / 7 / 2, Quirks 0 / 1 / 1, Verification authorities 2 / 5 / 1, Reddit / forum sources 1 / 4 / 2. Main changes: property-tax building rates corrected to the post-2024 values (3.50 / 11.00 / 14.50 / 18.00 Kč/m²) and the cadastre fee to 2,000 CZK; eTurista recorded as not in operation, and EU Regulation 2024/1028 as opt-in / opt-out with no Czech registration procedure; Q2 2026 ČSÚ price trend and 2025 realized kraj prices; 2025 wages, the minimum wage and 2026 paušální daň; CSD 2025 traffic census; NZÚ 2026+ loans (Kotlíkové dotace ended, no retrofit tax credit); farmland reciprocity rule since 1 Jul 2024 (§ 3d zákona č. 334/1992 Sb.); PENB fine 200,000 CZK, with rentals already covered; radon categories, the seismic record and the meaning of the ČAP zones corrected; PVK / SčVK ownership updated and the Veolia share recomputed (≈ 26 %); dead URLs replaced (ČGS radon, GFÚ, Sreality and Bezrealitky patterns). Follow-up consistency fixes: eTurista wording in Status and Quirks, the ČÚZK Dálkový přístup label in `--price`, the obce count in the TODOs, est. labels on the buyer-cost caveat. Not re-verified: Praha short-let positions (60 days, SVJ consent, zone bans), notary / makléř percentages and contractor cost ranges (est.), the build-era table, the regional radon list, BVK / OVAK ownership, the Facebook groups.
