# North Macedonia 🇲🇰 — Property Due-Diligence Playbook

ISO2: `mk`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1000` Skopje, `6000` Ohrid, `7000` Bitola, `2000` Štip)
- **Admin levels**: 8 statistical regions + 80 municipalities; 10 of the 80 make up the **City of Skopje** (capital, a separate unit of local self-government with special status) *(2026 data, source MAKSTAT NTES territorial units)*
- **Currency**: **MKD** (Macedonian denar) — de facto pegged to EUR at **~61.5** (NBRSM monetary strategy targets a stable denar/euro rate; middle rate 61.6177 MKD/EUR on 22 Oct 2026) *(2026 data, source NBRSM exchange-rate list web service + NBRSM Monetary Policy Executive Board release 28 Jul 2026)*
- **Languages**: Macedonian (official); **Albanian also official nationwide** since the Law on the Use of Languages took effect in January 2019 (Art. 1(2): the language spoken by at least 20% of citizens); any other language spoken by ≥20% of a municipality's citizens is co-official there (Art. 1(4)); Albanian-majority areas: Tetovo, Gostivar, Kičevo region. Constitutional Court review of parts of the law still pending *(source Law on the Use of Languages, English text on iuj.gov.mk + European Commission North Macedonia 2025 Report)*
- **Cadastre**: **AKN (Agencija za katastar na nedviznosti)**: `https://www.katastar.gov.mk/`
- **Identifier**: parcela + KO (cadastral municipality)
- **Ownership types**: pravo na sopstvenost (full ownership); etazna sopstvenost (condominium); pravo na službenost (servitude / easement — Zakon za sopstvenost i drugi stvarni prava Art. 4)
- **NATO since 27 March 2020** (30th Ally, source nato.int); **EU accession negotiations** opened 2022 and screening is complete, but no cluster is open yet — opening the first ("fundamentals") cluster awaits the constitutional amendments agreed in 2022 *(2026 data, sources: European Commission President statement in Skopje, 2 Oct 2026; European Council President Costa, 2 Jun 2026)*

## Section: `--price`

### Primary sources

- **MAKSTAT (Drzaven zavod za statistika)**: `https://www.stat.mk/` (current site; `stat.gov.mk` now serves the archive)
- **NBRSM (National Bank)**: `https://www.nbrm.mk/` — quarterly hedonic apartment price index (Skopje) + Financial Stability Report
- **Ministry of Finance**: `https://finance.gov.mk/`
- **FRED QMKN628BIS** — BIS residential property prices for Skopje (index 2010 = 100; latest Q1 2026 = 199.09, updated 31 Jul 2026, so it trails the NBRSM release by two quarters)
- **AKN Register of Prices and Leases** (Registar na ceni i zakupnini): quarterly transaction prices and rents by municipality — `https://www.katastar.gov.mk/registar-ceni-zakupnini-nedviznostite`
- **Investropa** — secondary aggregator

### Listing platforms

- **Reklama5**, **Pazar3**, **Imotko.mk** (sale + rent portal, live 2026-10-23)
- Skopjeshome, Domis.mk: ❌ DEPRECATED — dead on 2026-10-23 (no DNS record); verify with AKN Register of Prices and Leases
- Skopje primary market; Ohrid + Bitola secondary

### 2025-2026 price benchmarks (NBRSM Skopje index + AKN Register of Prices and Leases)

| Region | EUR/m² | YoY |
|---|---:|---:|
| **Skopje city center (Centar)** | est. 1,800–2,300; resale average 119,914 MKD/m² ≈ €1,946 (computed: 119,914 ÷ 61.6177 ≈ 1,946; racin.mk, 31 Aug 2026, which names no source for this average and credits AKN only for its Q1 2026 Skopje figure — verify at https://www.katastar.gov.mk/registar-ceni-zakupnini-nedviznostite) | +10.3% Q3 2026 (NBRSM index, all Skopje) |
| **Skopje Centar premium peak** | **3,360** (206,640 MKD/m², 50 m² new build sold by the developer, Q2 2026; AKN report as quoted by press24.mk and republika.mk — verify at https://www.katastar.gov.mk/registar-ceni-zakupnini-nedviznostite) | — (single transaction) |
| **Skopje Karpoš / Aerodrom** | est. 1,500–2,000; resale average Karpoš 111,806 / Aerodrom 108,081 MKD/m² ≈ €1,815 / €1,754 (AKN, reported Aug 2026) | +10.3% Q3 2026 (NBRSM index, all Skopje) |
| **Skopje suburbs** | est. 900–1,400 | no sub-city index published |
| **Ohrid lakefront** (UNESCO buffer) | est. 1,800–3,500+; resale peak **3,200** (197,408 MKD/m², 66 m² flat, Q2 2026) | no official Ohrid index — verify with AKN |
| **Bitola** | est. 700–1,100 | no official Bitola index — verify with AKN |
| **Tetovo / Gostivar** (Albanian-majority) | est. 800–1,300 | no official index — verify with AKN |
| **NBRSM Skopje apartment price index** | — | **+10.3% Q3 2026** (+1.3% QoQ), down from +25.0% in Q4 2025 |

*(2026 data. Sources: NBRSM apartment price index, Q3 2026 release (Oct 2026; SeeNews 5 Oct 2026 reports the same +10.3%); Q4 2025 YoY computed from BIS/FRED QMKN628BIS (199.00 vs 159.20 a year earlier). The NBRSM index is a hedonic index of asking prices in real-estate-agency sale notices for Skopje, not of registered transactions (NBRSM Quarterly Reports 2025). Peaks: AKN Register of Prices and Leases Q2 2026 report as reported by republika.mk and press24.mk (Aug 2026); resale averages: racin.mk, 31 Aug 2026, citing AKN data (reference quarter not stated) — press coverage, cross-check at katastar.gov.mk. Peak EUR figures are as reported; ≈ conversions use the NBRSM middle rate 61.6177. `est.` ranges are unsourced planning ranges carried over from the 2026-04 research pass; no fetched source backs them.)*

**Volume**: Q2 2026 — 8,369 registered transactions (sales + leases, +7.9% QoQ); 943 new-build apartments sold by developers; most apartments sold in Aerodrom (297), most houses in Bitola (64) *(2026 data, source AKN Register of Prices and Leases Q2 2026 report as reported by republika.mk / press24.mk, Aug 2026)*

### Compute

1. EUR/m² = price / **korisna povrshina** (usable area) — this playbook's working formula, not a published rule; the area a quoted price per m² rests on: data not publicly available — verify at https://www.katastar.gov.mk/registar-ceni-zakupnini-nedviznostite
2. **Currency**: MKD-EUR de facto peg ≈ 61.5 = predictable conversion (NBRSM middle rate 61.6177 on 22 Oct 2026)
3. **Ohrid UNESCO** premium est. ~2.9× over inland Bitola (computed from the table's est. ranges: Ohrid lakefront 1,800–3,500+, midpoint 2,650; Bitola 700–1,100, midpoint 900; 2,650 ÷ 900 ≈ 2.9. Lakefront against all of Bitola, so not like for like, and the open top end makes it a floor; both ranges are unsourced planning figures with no official Ohrid or Bitola index)
4. Cross-check **AKN** cadastre data + **Reklama5/Pazar3** listings

### Key terms

- AKN = Agencija za katastar na nedviznosti
- KO = katastarska opština
- Imoten list (имотен лист) = title sheet (AKN extract; see `--risks`)
- Energetski sertifikat = energy certificate
- DDV = Danok na dodadena vrednost (VAT)
- Danok na imot = property tax
- Danok na promet = transfer tax

---

## Section: `--traffic`

### Sources

- **JP za državni patišta (ЈПДП, Public Enterprise for State Roads)**: `https://roads.org.mk/` — state roads are A-roads (A1–A4) and R1 / R2 regional roads under the Odluka za kategorizacija na državnite patišta (Sl. vesnik 133/2011), which repealed the 1994 magistral / regional road list; the A1 Tabanovce–Kumanovo–Veles–Gevgelija corridor is the former Yugoslav M-1 (secondary, Wikipedia)
- **TDPS traffic-count portal** (ЈПДП): `https://tdps.roads.org.mk/` — 71 fixed vehicle counters on state roads; per-counter PGDS reports and API access on request (2026 data, source tdps.roads.org.mk)
- City traffic data Skopje, Bitola, Ohrid

### Key term

**PGDS (ПГДС, Prosečen godišen dneven soobraḱaj)** = AADT-equivalent; the headline figure of the TDPS annual counter reports.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets; Corridor 8 east of Kumanovo — Stracin–Kriva Palanka 2,694 PGDS)
- 🟠 10,000–35,000 v/d (Skopje arterials; the busiest counted state-road sections — Hipodrom–Kadino Skopje entrance 18,406 PGDS, Skopje ring Stenkovec–Saraj 16,931 PGDS; average daily traffic Tetovo–Gostivar 17,428 and A1 Petrovec–Veles 10,795 vehicles)
- 🔴 > 35,000 v/d (no state-road section in the published 2022 ЈПДП figures reaches this band — the busiest was 18,406 PGDS; check the TDPS counter for the segment, and city counts for central Skopje boulevards)

*Example figures: 2022 data, source ЈПДП counts as reported by Meta.mk (11 May 2023; secondary report of primary data) — rates/figures may have changed since.*

---

## Section: `--tax`

### Annual property tax — Danok na imot

- **0.10–0.20 % of market value** (statutory band, Zakon za danocite na imot Art. 6(1)); the exact rate is set by decision of the municipal council, the councils of the Skopje municipalities and the Council of the City of Skopje (Art. 6(6)). Base = market value under the Government valuation methodology, revised every 4 years (Art. 5(1), (4), (7)), not necessarily the purchase price *(2026 data, source MF-hosted consolidated Zakon za danocite na imot through Sl. vesnik 151/21, linked from finance.gov.mk)*
- **50 % reduction** for the house or flat (and yard) the taxpayer lives in (Art. 9). Rate **×3** for property left unused (not used by the owner or not let) for more than 6 months in a year, and **×5** if that non-use is not reported (Art. 6(4)–(5)) — relevant for a holiday home left empty
- Illustrative 80 m² flat with a €100k tax base: est. **€100–€200/yr** before the Art. 9 reduction, **€50–€100/yr** if lived in, **€300–€600/yr** if left unused (computed: €100k × 0.10–0.20 %, then × 0.5 or × 3)
- Return by 31 January, or within 15 days of acquisition, and no new return while the data are unchanged (Art. 29); the mayor's decision by 31 March (Art. 30); paid **quarterly**, due mid-quarter or within 15 days of the decision (Art. 37)

### Transaction taxes

- **Danok na promet (transfer)**: **2–4%** (set by each municipal council / the Skopje councils, Zakon za danocite na imot Art. 22). **Statutorily owed by the SELLER** (Art. 20(1)) — buyer becomes the taxpayer **only if the sale contract (dogovor) explicitly stipulates so** (Art. 20(2)). Default-silent contracts → seller pays. Base = market value under the Government methodology, or the contract price where that is higher (Art. 21(1)–(2)); return due within 15 days of signing (Arts 23(1), 34), and no notarisation or cadastre entry without proof of payment (Art. 35). The Notary Law's 2016 text adds a deposit route: the notary keeps a separate account into which the parties pay the transfer tax, computed on an authorised appraiser's valuation, and passes it at once to the municipality (Zakon za notarijatot Art. 12(11), Sl. vesnik 72/2016 — rates/figures may have changed since); how that fits the municipal return and decision (Arts 34, 36) is not verified, so confirm with the notary. Read the dogovor carefully — a buyer modelling 3–5 % closing costs can be €2–4 k off on a €100 k flat if the contract is silent *(2026 data, source MF-hosted consolidated Zakon za danocite na imot through Sl. vesnik 151/21, linked from finance.gov.mk)*
- **DDV (VAT)**: **18 % standard**; **5 % reduced on first sale of newly built residential** within 5 years of construction (mixed-use → proportional; commercial portion = 18 %). **Sunset 31 December 2028** (extended Dec 2025 from prior 31 Dec 2025 sunset — Parliament amendment to Zakon za DDV); that VAT-charged first sale owes no danok na promet (Zakon za danocite na imot Art. 25(9)) *(2026 data, source MF press release 25 Dec 2025 + PwC Tax Summaries reviewed 23 Jul 2026 + MF-hosted Zakon za danocite na imot)*
- **Notary fees**: fixed MKD reward by value band, not a percentage — Notarska tarifa (Sl. vesnik 226/16) Art. 11: notarial act MKD 10,000 for a value of MKD 3–5 million, MKD 12,000 for MKD 5–9 million, MKD 20,000 for MKD 9–20 million; solemnisation of a private contract = 50 % of that (Art. 12); plus expenses (Art. 2(3)). Est. ~0.1–0.3 % of price for a €50k–€200k flat (computed at 61.5 MKD/EUR). A 2024 amendment raising the fees from 1 Sep 2024 was withdrawn before it applied (Ministry of Justice, 31 Jul 2024); whether the 33/19 amendment changed these bands is not verified — confirm the fee with the notary *(2016 data, source Notarska tarifa 226/16 text via Notary Chamber nkrm.org.mk + pravda.gov.mk 31 Jul 2024 — rates/figures may have changed since)*
- **Cadastre registration (AKN)**: flat **MKD 1,250 per legal basis in one cadastral municipality**, whatever the number of ownership sheets (flat, parking space, common parts), from 24 Oct 2024 — previously MKD 1,250 per sheet (MKD 5,000 for four sheets); ~€20 (computed at 61.5 MKD/EUR) *(2024 data, source AKN announcement as reported by Faktor.mk and A1on, 24 Oct 2024 — secondary; rates/figures may have changed since)*

### Capital gains

- **10 % PIT** (NOT 15 % — common confusion); MK PIT is 10 % flat. **Tax base = sale price − purchase price** (PIT Law Art. 60(1)); **10 % normed costs** are recognised only for property the seller lived in ≥1 year before the sale (Art. 60(2)), which gives est. **9 % of the gain** (10 % × 90 %). Otherwise the rate is 10 % of the gain, less documented actual investment costs if the seller claims them (Art. 60(3)) *(2026 data, source UJP — Zakon za danokot na licen dohod, consolidated to Sl. vesnik 274/2022, Arts 11 / 60 / 63 + PwC Tax Summaries reviewed 23 Jul 2026)*
- 15 % rate applies only to gambling winnings, not real-estate gains
- **Exempt if ≥5 years ownership** OR **≥3 years ownership + ≥1 year lived-in residence** OR **acquired by first-order inheritance** (PIT Law Art. 63, consolidated text through Sl. vesnik 274/22). PwC's summary ties inherited property to the same 5- or 3-year periods, but the law text sets no period for first-order inheritance and it governs; a first-order gift received from 1 Jan 2023 does keep them, counted from the donor's acquisition (a gift received before that date stays under the earlier text, 274/22 Art. 24). Confirm with UJP on an inherited or gifted sale

### Total transaction cost (buyer side)

- Resale: est. **~0.1–0.3 %** + MKD 1,250 cadastre when the seller pays the transfer tax (statutory default), or est. **~2.1–4.3 %** when the dogovor shifts the 2–4 % transfer tax to the buyer (transfer tax + notary est. 0.1–0.3 % + cadastre MKD 1,250); agency and lawyer fees not included
- New build (first sale within 5 yrs of construction, VAT charged): 5 % VAT (check whether the quoted price includes it), no transfer tax (Art. 25(9)), other costs est. ~0.1–0.3 % (notary + cadastre)

### Future risk

- **IMF** (Selected Issues Paper SIP/2026/049 "Tax Potential in North Macedonia", June 2026, background to the 2026 Article IV): recurrent property taxation "remains underutilized" — low statutory rates, exemptions "particularly for owner-occupied housing" and weak valuation practices; it points to gradual reform. A recommendation, not a legislated change *(2026 data, source IMF eLibrary)*
- **Skopje city tax reform** discussed (Law on the City of Skopje rate-setting)
- **Ohrid UNESCO regulation tightening**

---

## Section: `--rental`

### Long-term residential

- **Zakon za domuvanje** (Law on Housing — its subject includes lease relations in housing; latest amendment Sl. vesnik 160/2025) + **Zakon za obligacionite odnosi** (general lease rules) *(2025 data, source Zakon za domuvanje consolidated text on dki.gov.mk + Sl. vesnik 160/2025)*
- Tenant protection moderate
- Standard 1-3 yr contracts
- Average monthly rent per m² of residential space, Q2 2026 (registered leases): Centar 408 MKD (≈ €6.6), Aerodrom 375 MKD (≈ €6.1), Karpoš 354 MKD (≈ €5.7), Kisela Voda 326 MKD, Štip 266 MKD *(2026 data, source AKN Register of Prices and Leases Q2 2026 report as reported by emagazin.mk, Aug 2026 — press coverage, cross-check at katastar.gov.mk)*

### Short-let (Airbnb)

- **Skopje + Ohrid**: license + tourist tax required
- **Ohrid** UNESCO restrictions tightening
- Tax: standard PIT on rental income

### Tax on rental

- Resident: **10 % PIT on net rental**, with **10 % standard deduction (unfurnished)** OR **15 % deduction (furnished)** of gross income (PIT Law Art. 53(1)–(2)). Effective: **9 % of gross (unfurnished) / 8.5 % of gross (furnished)**. *(2026 data, source Zakon za danokot na licen dohod Art. 53, consolidated text through Sl. vesnik 274/22, as published by UJP (https://www.ujp.gov.mk/-/regulativa/opis/425) + PwC Tax Summaries — income determination, last reviewed 23 Jul 2026 — a 30 % deduction figure has circulated for MK, but the law sets 10/15 %)*
- Non-resident: taxed on MK-source rental income at the same flat **10 %**; the payer withholds the PIT where the tenant is a domestic company or other book-keeping taxpayer *(2026 data, source PwC Tax Summaries — taxes on personal income + tax administration, last reviewed 23 Jul 2026)*

---

## Section: `--work=<profession>`

### Sources

- **AVRSM (Agencija za vrabotuvanje)**: `https://av.gov.mk/`
- **Vrabotuvanje.com.mk**, **e-Rabota** (AVRSM vacancy board: `https://e-rabota.av.gov.mk/OglasSearch.aspx`), **LinkedIn MK**

### Self-employment

- **DOO / DOOEL** (limited liability): min share capital **EUR 5,000 in MKD equivalent** at the NBRSM middle rate (Zakon za trgovskite društva Art. 172(2)); **simplified DOO** from **EUR 1** (Art. 172-a) *(2021 data, source unofficial consolidated text of the Law on Trade Companies on sec.gov.mk — rates/figures may have changed since; verify with the Central Registry)*
- **Pausalen danok** flat-rate small business
- **DDV** registration: mandatory once total turnover exceeds **MKD 2,000,000** in the previous calendar year, or is expected to / does exceed it in the current year (Zakon za DDV Art. 51(1)); voluntary below *(2026 data, source UJP consolidated VAT law to Sl. vesnik 267/2025 + UJP form DDV-01 + PwC Tax Summaries, last reviewed 23 Jul 2026)*

### Salary benchmarks (2024-2026)

- National average, Aug 2026: **MKD 73,336 gross / MKD 48,733 net** per month (computed at the NBRSM middle rate: 73,336 ÷ 61.6177 ≈ €1,190 and 48,733 ÷ 61.6177 ≈ €791); net +7.6% YoY *(2026 data, source MAKSTAT average gross and net wage releases, published 22 Oct 2026)*
- Average **net** wage by statistical region (latest regional release):
  - Skopje Region: MKD 46,515 (≈ €755)
  - Pelagonia (Bitola): MKD 38,657 (≈ €627); Southwest (Ohrid): MKD 36,755 (≈ €597); Polog (Tetovo / Gostivar): MKD 36,673 (≈ €595)
  - Lowest, Southeast: MKD 33,502 (≈ €544); national: MKD 41,239
  - *(2024 data, source MAKSTAT "Regions of North Macedonia, 2025" — rates/figures may have changed since)*
- **Minimalna plata**: **MKD 38,507 gross / MKD 26,046 net** per month (≈ €625 / €423), payable from the March 2026 payroll; re-indexed each March *(2026 data, source Government session minutes citing Sl. vesnik 63/26, portal.mdt.gov.mk)*
- EUR at the NBRSM middle rate 61.6177 (22 Oct 2026); MAKSTAT's monthly and regional wage releases give averages, not medians

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Seizmološka opservatorija** (Seismological Observatory, Faculty of Natural Sciences and Mathematics, Ss. Cyril and Methodius University — PMF-UKIM) | `https://seismobsko.pmf.ukim.edu.mk/` | Seismic monitoring, felt-earthquake reports; draws up and updates the national earthquake-zoning map |
| **AKN** | `https://www.katastar.gov.mk/` | Cadastre |
| **UHMR (Uprava za hidrometeorološki raboti)** | `https://uhmr.gov.mk/` | Weather, hydrology |

### Specific risks

#### Earthquake — CRITICAL

- **1963 Skopje M6.1** — catastrophic event:
  - 26 July 1963, 05:17 local time; Mw 6.1, depth ~6 km, max. intensity MMI X
  - **~1,070 deaths** (sources range 1,000–1,100)
  - 3,000–4,000 injured
  - 200,000+ homeless
  - **~80% of city destroyed** (sources range 75–80%)
  - City-centre plan from the 1965 UN-backed competition — **Kenzo Tange** team 60% of the first prize, Zagreb team Miščević & Wenzler 40%; only parts were built (City Wall housing, new railway station)
  - **~14,000 prefab single-family houses** within ~8 months (by late 1964), donated by many countries
  - Aid offered from 78 countries
  - *(historical data; sources: Wikipedia "1963 Skopje earthquake" citing USGS ComCat + MRT; MoMA post + Spomenik Database on the Tange plan; UC eScholarship thesis on the prefab programme — secondary)*
- **Ohrid + Bitola** seismic
- **Vardar valley** moderate
- **Design codes**: Eurocodes incl. EC8 were adopted as national design codes on 2 Sep 2020 (Sl. vesnik 211/2020) with a coexistence period alongside the existing national rules — for seismic design the Yugoslav rulebook **PIOVS-81** (Sl. list SFRJ 31/81). The coexistence period was set at 3 years, extended to 4 (Sl. vesnik 183/2023), 5 (178/2024) and 7 years (181/2025), est. to ~Sep 2027. ISRSM has adopted EC8 national annexes (e.g. MKS EN 1998-3:2012/NA:2012, assessment and retrofitting of buildings). A recent build may be designed to either code — ask which one the structural design used (2025 data, source EU JRC Eurocodes portal + Ministry of Transport rulebooks via dejure.mk + ISRSM)

#### Floods

- **Vardar river** (Skopje + central MK)
- 6–7 Aug 2016 Skopje flash flood: 22 dead, ~3,500 homes flooded, ~93 mm of rain overnight; worst hit Stajkovci, Aračinovo, Butel and the ring road near Stajkovci (2016 data, sources AP via VOA / RFE/RL 9 Aug 2016 + Copernicus EMS EMSR174 maps via ReliefWeb) — rates/figures may have changed since
- Climate change increasing extreme events

#### Wildfires

- Increasing climate trend
- Macedonia mountainous + dry summer

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1963** | Pre-quake stock, mostly destroyed in Skopje |
| **1963-1970s post-quake reconstruction** | Tange-era prefab; some quality issues; first Yugoslav seismic code (temporary, 1964) |
| **Yugoslav 1970s-1990** | Asbestos common; panel buildings; designs from 1981 on follow PIOVS-81 (Sl. list SFRJ 31/81) |
| **2020+** | Eurocodes (incl. EC8) adopted 2 Sep 2020 but applied in parallel with PIOVS-81 during the transition (7 yrs per Sl. vesnik 181/2025, est. to ~Sep 2027) — a new build is not automatically EC8-designed |
| **Skopje 2014 reconstruction** | Government-led neoclassical reskinning (controversial) |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski sertifikat** (Sertifikat za energetski karakteristiki, EPC) | Mandatory for any building or unit sold or let (Zakon za energetska efikasnost Art. 33(2)); issued by a licensed energy auditor, valid 10 years, noted in the cadastre (Art. 33(3)); the seller must show it before the sale, hand the original or a certified copy to the buyer within 5 days after it, and state the energy class in the listing (Art. 33(10)); fine for a natural person €100–500 (Art. 51(3)) (2026 data, source consolidated Law on Energy Efficiency incl. Sl. vesnik 134/26, portal.mdt.gov.mk) |
| **Solemniziran dogovor za kupoprodažba** (sale contract confirmed — solemnised — by a notary; a full notarski akt is optional, required by the Notary Law only for deaf or mute parties who cannot read / write, Art. 52) | Mandatory: a private contract transferring real-estate rights must be solemnised by a notary (Zakon za notarijatot Art. 55(1)) and, above €10,000, drafted, stamped and signed by an advokat (Art. 55(2), 56(3)); the notary files it with AKN electronically (Art. 99(3)); the rights holder must apply to register the change with AKN within 30 days of it (Zakon za katastar na nedvižnosti Art. 202, consolidated May 2025) (Notary Law: 2016 base text, source Notary Chamber nkrm.org.mk, since amended by Sl. vesnik 142/2016 and 233/2018 — verify the consolidated text at slvesnik.com.mk; the €10,000 rule is also stated in 2022–2025 law-office guides) |
| **Imoten list** (имотен лист, title sheet) | AKN extract — the official record of owner, area, use and registered encumbrances (Zakon za katastar na nedvižnosti, consolidated May 2025); issued by AKN, or by a notary or lawyer with e-access to AKN (per law-office guides) |

---

## Section: `--mains`

### Sources

- **JP Vodovod i kanalizacija Skopje** (Skopje water): `https://www.vodovod-skopje.com.mk/` — new connections go through its "Барање за хидротехнички услови" and "Барање за издавање на решенија за приклучоци" request forms
- Per-municipality elsewhere
- Rural: septic common

### Costs

| Scenario | Cost (EUR) |
|---|---:|
| Mains connection | ~1,000–3,000 |
| Septic upgrade | ~1,500–4,500 |
| Bored well | ~2,500–6,000 |

*Est. planning ranges (illustrative) — confirm with a JP Vodovod / local installer quote.*

---

## Cost benchmarks (MK 2026)

| Work | Cost (EUR) |
|---|---:|
| Energetski sertifikat | 100–250 |
| Notar fees | fixed MKD band; est. ~0.1–0.3% of price |
| Cadastre registration (AKN) | MKD 1,250 per legal basis (~20) (2024 data, source AKN announcement as reported by Faktor.mk and A1on — rates/figures may have changed since; verify at https://www.katastar.gov.mk/) |
| Transfer tax | 2–4% (seller by default) |
| **Total transaction cost (buyer)** | est. **~0.1–0.3%** (seller pays transfer tax) or **~2.1–4.3%** (dogovor shifts it to buyer) |
| Roof renovation | 3,500–10,000 |
| Earthquake retrofit (older builds) | 15,000–60,000 |
| Energy retrofit | 8,000–25,000 |
| Solar PV (5kW) | 3,500–7,000 |

*Notary, cadastre and transfer-tax rows: sources and computation in `--tax`. Energetski sertifikat and works rows: est. planning ranges (illustrative, no primary source) — confirm with a licensed assessor or contractor quote.*

## Active fiscal incentives (2025-2026)

- **5 % DDV on the first sale of new-build residential** (vs 18 % standard) until 31 Dec 2028, with no danok na promet on that sale — see `--tax`
- **Municipal energy subsidies are local, not national** — e.g. Opština Gazi Baba (Skopje) 2026 call: 50 % of the cost of a solar thermal collector system, max MKD 15,000 per household, for residents with the system installed at their ID-card address, open until 30 Nov 2026 or until funds run out *(2026 data, source gazibaba.gov.mk call of 11 Mar 2026)*; check the call of the municipality where the property is
- **EU pre-accession funding** for energy retrofit
- **NATO infrastructure** investment
- **Skopje 2014 redevelopment** ongoing (controversial)

## Common listing platforms

- **Reklama5**, **Pazar3**, **Imotko.mk**
- Skopjeshome, Domis.mk: ❌ DEPRECATED — dead on 2026-10-23 (no DNS record); verify with AKN Register of Prices and Leases

## Caveats unique to MK

- **1963 Skopje earthquake** built much of modern Skopje (architectural significance + Tange city-centre plan, only partly implemented)
- **Skopje 2014** reconstruction — controversial neoclassical reskinning of central Skopje
- **Ohrid UNESCO site** — strict construction limits, lakefront premium est. ~2.9× over Bitola (table midpoints, see `--price` Compute)
- **MKD-EUR peg 61.5** very stable (no FX risk for EUR holders)
- **CGT 10% with 5-year exemption** OR 3yr+1yr-resident exemption
- **PIT 10% flat** (NOT progressive; 15 % only on gambling winnings) — not unique in the region: Bulgaria also levies a flat 10 % *(2026 data, source PwC Tax Summaries MK reviewed 23 Jul 2026 + BG reviewed 2 Aug 2026)*
- **Macedonian-Albanian ethnic mix** — Tetovo + Western MK municipalities
- **NATO since 2020**, **EU candidate** since 2005 (long delays via Greece + Bulgaria veto disputes — Greece naming dispute resolved by the 2018 Prespa Agreement; separate Bulgaria veto over identity/language only partly addressed by the 2022 negotiating framework and still contested)
- **Skopje air quality** winter PM2.5 severe (coal heating)
- **Skopje flash flood** 6–7 Aug 2016 (22 dead; see `--risks`) + Vardar flood risk + climate change
- **EU pre-accession funding** for retrofit
- **Foreign-buyer rules** (Zakon za sopstvenost i drugi stvarni prava Arts 244–247): natural and legal persons resident in EU / OECD states acquire flats, residential and commercial buildings and building land on the same terms as citizens; others only under reciprocity, which the Minister of Justice determines; no foreigner may own agricultural land (long-term lease only, under reciprocity and with Minister of Justice consent) *(2026 data, source gov-hosted consolidated text through Sl. vesnik 35/10 (portal.mdt.gov.mk); the dejure.mk current consolidation lists no later amendment)*
- **Notarial system** strong
- **NBRSM** financial stability oversight

## Reddit / forum sources

- **r/macedonia** (community)
- **r/Skopje**, **r/mkd** (unofficial; "the subreddit for people from or interested in Macedonia")
- **Balkan Insight**, **Macedonian Information Agency (MIA)**

## Verification authorities

| Authority | When to call |
|---|---|
| **AKN** | Title verification |
| **Notar** | Mandatory closing — solemnises the sale contract and files it with AKN electronically (Zakon za notarijatot Art. 55, 99) |
| **Advokat** | Must draft, stamp and sign any real-estate contract above €10,000 before the notary can solemnise it (Zakon za notarijatot Art. 55(2)) |
| **Licensed energy auditor** | Issues the EPC required for the sale (Zakon za energetska efikasnost Art. 33) |
| **Lokalna samouprava** | Property tax + permits |
| **UJP (Uprava za javni prihodi)** | Tax compliance |
| **Council of Skopje** (if Skopje) | Special metro rates |

## Source URL templates

| Source | URL pattern |
|---|---|
| AKN | `https://www.katastar.gov.mk/` |
| MAKSTAT | `https://www.stat.mk/` (old site `stat.gov.mk` not updated since 7 Apr 2025) |
| NBRSM | `https://www.nbrm.mk/` |
| Ministry of Finance | `https://finance.gov.mk/` |
| Reklama5 | `https://www.reklama5.mk/` |
| Pazar3 | `https://www.pazar3.mk/` |
| UJP (tax) | `https://www.ujp.gov.mk/` |
| Vodovod Skopje | `https://www.vodovod-skopje.com.mk/` |
| JP za državni patišta | `https://roads.org.mk/` |
| TDPS traffic counts | `https://tdps.roads.org.mk/` |
| Seismological Observatory PMF-UKIM | `https://seismobsko.pmf.ukim.edu.mk/` |
| UHMR (hydromet) | `https://uhmr.gov.mk/` |

## Status

✅ **Fully populated** as of 2026-04-26. **Last verified**: 2026-05-27. CGT rate / base / exemptions re-verified 2026-09-24 against the UJP consolidated PIT Law in the October regwatch wave. Tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (NBRSM Skopje hedonic index Q3 2026 + AKN Register of Prices and Leases + FRED / BIS Skopje series; EUR/m² ranges are est.), traffic (ЈПДП TDPS PGDS counts), tax (Danok na imot 0.10-0.20% + 2-4% transfer, seller by default + 18% VAT (5% first-sale residential to 31 Dec 2028) + 10% CGT 5-yr OR 3yr+1yr-resident exemption), rental (Zakon za domuvanje + 10% PIT with 10 / 15% deductions + AKN registered rents; short-let licence and tourist tax not verified), work (AVRSM + MAKSTAT wages + 10% flat PIT), risks (1963 Skopje M6.1 catastrophic + 2016 floods + EC8 / PIOVS-81 transition + winter air quality), mains (Skopje vodovod + per-municipality; connection costs est.).
**Confidence**: HIGH for the MKD-EUR peg ~61.5 (NBRSM middle rate 61.6177 on 22 Oct 2026) and for AKN as the centralised cadastre; HIGH for the statutory tax rules re-checked 2026-10-23 against the law texts (Danok na imot 0.10–0.20 % band, 2–4 % transfer tax owed by the seller unless the dogovor shifts it, 5 % / 18 % DDV, CGT 10 % (NOT 15 %) with the Art. 63 exemptions); HIGH for `--work` (MAKSTAT Aug 2026 wages, the Mar 2026 minimum wage, DOO capital EUR 5,000, DDV threshold MKD 2,000,000; re-verified 2026-10-23); HIGH for the 1963 Skopje earthquake core figures (M6.1, ~1,070 deaths, 200,000+ homeless, ~80 % of the city destroyed); MEDIUM for notary fees (2016 tariff bands; the 33/19 amendment not seen) and the AKN MKD 1,250 fee (secondary news reports); HIGH for the rental PIT deductions of 10 / 15 % (PIT Law Art. 53 text + PwC Tax Summaries); MEDIUM for the `--price` index figures (NBRSM Q3 2026 Skopje index taken from NBRSM's announcement as quoted by SeeNews, not from nbrm.mk itself; AKN resale averages via press); LOW for the est. EUR/m² ranges, the Ohrid est. ~2.9× premium and price trends outside Skopje (no primary source, no official regional index); MEDIUM for IMF property tax recommendations (IMF Selected Issues Paper SIP/2026/049, June 2026 — a staff recommendation, not legislated); LOW for short-let rules (licence, tourist tax and Ohrid UNESCO restrictions not verified); MEDIUM for `--risks` (authority URLs, 1963 figures, the EC8 / PIOVS-81 transition and sale documents re-checked; seismic zoning outside Skopje and the climate, wildfire and build-era rows are curated, not verified); MEDIUM for `--traffic` verdict bands (curated thresholds, calibrated to 2022 ЈПДП counts); LOW for the works rows in Cost benchmarks and the mains connection costs (est., no primary source); MEDIUM for "Skopje 2014" reconstruction controversy framing.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | 4 changed, 3 confirmed, 2 unverifiable (katastar.gov.mk refused connections; "parcela + KO" not checked); admin units, Law on the Use of Languages (2019), servitude term and EU accession status corrected; peg confirmed (NBRSM 61.6177 on 22 Oct 2026) |
| `--work=<profession>` | 2026-11-05 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--traffic` | 2026-10-23 | 2026-10-23 refresh wave | 5 changed, 1 confirmed, 1 unverifiable (city traffic data for Skopje, Bitola, Ohrid); ЈПДП name + URL, TDPS counters, 2011 road categorisation; band examples recalibrated to 2022 counts (busiest counted state-road section 18,406 PGDS); thresholds are curated, not data |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | 2 changed, 2 confirmed; Reklama5 + Pazar3 live; Skopjeshome + Domis.mk deprecated (no DNS record); Imotko.mk added |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | 1 changed, 2 confirmed; Notar role rewritten; Advokat (> €10,000) and licensed energy auditor rows added; UJP and Council of Skopje rows not re-checked |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | 8 confirmed (katastar.gov.mk and nbrm.mk confirmed only indirectly); 4 rows added (ЈПДП, TDPS, Seismological Observatory, UHMR); MAKSTAT row moved to stat.mk (checked 2026-11-03) |
| `--tax` | 2026-10-23 | 2026-11-05 maintenance run | The Ministry of Finance and PwC confirm 10 % on all income except 15 % on gambling winnings. The Art. 63 exemptions and the 1 Jan 2023 gift rule match UJP's consolidated text of the Personal Income Tax Law. |
| `--rental` | 2026-10-23 | 2026-11-05 maintenance run | The 10 % and 15 % normed deductions in Art. 53 are confirmed in the Personal Income Tax Law as published by UJP (consolidated to Sl. vesnik 274/22) and by PwC, reviewed 23 Jul 2026. The attribution of the 30 % figure to Serbia was removed. |
| `--risks` | 2026-10-23 | 2026-11-05 maintenance run | The 1965 competition result (Tange 60%, Miščević and Wenzler 40%) and the partial build-out are confirmed in Spomenik Database, Wikipedia and MoMA post, all secondary sources. |
| `--mains` | 2026-11-05 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (MK 2026) | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |

Sections without a row default to the Status footer date. `--price`, `--tax`, `--rental`, `--risks`, `--mains`, Cost benchmarks, Active fiscal incentives, Caveats unique to MK and Reddit / forum sources were partly refreshed on 2026-10-23 but keep unverified items (see Update history), so they keep the footer date.

## Extension TODOs

- [ ] Per-municipality property tax + transfer tax rates table
- [ ] Skopje 10 sub-municipalities specific rates
- [ ] Ohrid UNESCO construction limits + buffer zone
- [ ] Tetovo / Gostivar Albanian-majority specifics
- [ ] CGT 5-year vs 3yr+1yr-resident exemption decision tree
- [ ] 1963 quake-zone overlay vs EC8-designed builds (Eurocodes adopted 2020; PIOVS-81 transition est. to ~Sep 2027)
- [ ] Skopje 2014 reconstruction inventory
- [ ] Skopje winter air quality mitigation
- [ ] Vardar river flood-zone overlay
- [ ] EU accession reforms timeline (Bulgaria veto resolution)

## Update history

- **2026-04-26** — Initial population
- **2026-05-27** — Tier-1 validation sweep: transfer tax owed by the seller by default, 5 % first-sale DDV regime, CGT notes and rental deductions (10 / 15 %, not 30 %) corrected; notarial-act row added
- **2026-05-29** — Anti-hallucination consistency sweep: mains cost rows labelled est.
- **2026-09-24** — October regwatch wave: CGT base and exemptions (incl. first-order inheritance) re-verified against the UJP consolidated PIT Law
- **2026-10-21** — December regwatch wave (run early): tax tracker entries re-checked
- **2026-10-23** — Refresh wave. Playbook-level date not re-stamped: `--price`, `--tax`, `--rental`, `--risks` and `--mains` keep unverified items. Counts per section (changed / confirmed / unverifiable):
  - Re-verified: Country profile 4 / 3 / 2; `--work` 6 / 4 / 0; `--traffic` 5 / 1 / 1; Common listing platforms 2 / 2 / 0; Verification authorities 1 / 2 / 2 (Advokat and energy-auditor rows added); Source URL templates 0 / 8 / 0 (4 URLs added)
  - Partly refreshed, not re-verified: `--price` 11 / 6 / 7; `--rental` 3 / 2 / 5; Reddit / forum sources 1 / 3 / 1; `--tax` 8 / 13 / 2; Cost benchmarks 2 / 1 / 5; Active fiscal incentives 0 / 0 / 3 (2 sourced bullets added); Caveats unique to MK, legal / fiscal lines 2 / 1 / 1; `--risks` 13 / 5 / 6; `--mains` 1 / 1 / 3
  - Main changes: price table rebuilt on the NBRSM Skopje hedonic index (+10.3 % YoY, Q3 2026) and the AKN Register of Prices and Leases — the old "+3.17 % Q4 2025 national YoY" was the QoQ change of the Skopje index and was credited to MAKSTAT; EUR/m² ranges relabelled est.; MAKSTAT moved to stat.mk; Skopjeshome and Domis.mk deprecated, Imotko.mk added; Albanian official nationwide under the 2019 Law on the Use of Languages; EU accession status restated (screening complete, no cluster open); rental law names corrected (Zakon za domuvanje + Zakon za obligacionite odnosi), AKN Q2 2026 rents per m² added, non-resident rental PIT 10 % with payer withholding; DOO capital EUR 5,000 (was MKD 5,000), DDV registration threshold MKD 2,000,000 (was MKD 1M), MAKSTAT Aug 2026 wages and the Mar 2026 minimum wage, Mojabaza → AVRSM e-Rabota; property and transfer tax restated from Zakon za danocite na imot; notary fees are fixed MKD bands under the 2016 tariff (was ~0.5–1.0 %) and the AKN fee a flat MKD 1,250 per legal basis (was ~0.3 %), so the buyer's transaction cost becomes est. ~0.1–0.3 % with the seller paying the transfer tax or ~2.1–4.3 % when the dogovor shifts it (was ~3–5 %); IMF reference → Selected Issues Paper SIP/2026/049 (June 2026); PIT "unique in region" corrected (Bulgaria also levies 10 % flat); foreign-buyer rules restated from Arts 244–247 of the Zakon za sopstvenost i drugi stvarni prava; ЈПДП road categorisation (former M-1 → A1), TDPS counters and band examples recalibrated; Seismological Observatory (PMF-UKIM) and UHMR URLs added; 1963 figures given with source ranges and the Tange city-centre plan restated (1965 UN-backed competition); EC8 adopted 2020 with the PIOVS-81 transition est. to ~Sep 2027 (was "Post-2008 EC8"); sale documents restated (solemnised contract, Advokat above €10,000, EPC duty, imoten list)
  - Not verified, left as curated or est.: EUR/m² ranges, the Ohrid 1.5–2× premium and regional price trends outside Skopje; short-let licence, tourist tax and Ohrid UNESCO restrictions; tenant protection and contract length; the Skopje city tax reform and Ohrid UNESCO Future-risk lines; the three original fiscal-incentive bullets; seismic zoning for Ohrid, Bitola and the Vardar valley; climate, wildfire and build-era rows; works and mains cost ranges; MIA liveness
  - Status and consistency: Coverage check and Confidence recomputed; per-section verification table added; `--price` key term "Vlasnicki list" → imoten list and MAKSTAT URL template → stat.mk, matching the refreshed sections (checked 2026-11-03)
- **2026-11-04** — Maintenance run: closed `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (MK 2026); still open `--price`.
- **2026-11-05** — Maintenance run: closed `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (MK 2026); still open `--price`.
