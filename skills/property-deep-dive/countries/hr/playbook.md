# Croatia 🇭🇷 — Property Due-Diligence Playbook

ISO2: `hr`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`10000` Zagreb central, `21000` Split, `20000` Dubrovnik, `52100` Pula)
- **Admin levels**: 21 županije (20 counties + Grad Zagreb, which has the special status of both city and county) + 555 other cities/municipalities (428 općine + 127 gradovi; 2015 data, source Government bill P.Z. 919, sabor.hr — rates/figures may have changed since). 2026 cross-check: the Porezna uprava property-tax tally counts 556 cities/municipalities including Grad Zagreb (41 + 12 + 503 = 556, computed), i.e. 555 + Grad Zagreb
- **Currency**: **EUR (€)** — adopted 1 Jan 2023 (replaced HRK)
- **Languages**: Croatian (official); Italian, Hungarian, Serbian (regional minorities)
- **Cadastre**: **dual register** (Croatia famously has separate catastral + land registry — must reconcile both)
  - **DGU Geoportal**: `https://geoportal.dgu.hr/` — central spatial data
  - **OSS — Zajednički informacijski sustav zemljišnih knjiga i katastra**: `https://oss.uredjenazemlja.hr/` (also via e-Građani) — the official cadastre + land-register route. First copy of a _posjedovni list_ carries no cash charge; each further copy is **EUR 0.66** (2026 data, source gov.hr/hr/posjedovni-list/1312; 2026-10-23 verified). Replaces the former commercial katastar.hr
  - **OSS Uređena zemlja**: `https://oss.uredjenazemlja.hr/` — unified search (cadastre + ZK gruntovnica)
- **Identifier**:
  - Cadastral parcel number `broj čestice` within cadastral municipality `k.o.`
  - ZK title number `zk uložak` in gruntovnica
- **Ownership types**: vlasništvo (full); etažno vlasništvo (condominium); collective + co-ownership
- **EU member since 2013 + eurozone since 2023**

## Section: `--price`

### Primary sources

- **DZS (Croatian Bureau of Statistics)**: `https://podaci.dzs.hr/` — official residential price index (quarterly; Grad Zagreb / Jadran / Ostalo split) + prices of new flats sold (half-yearly; Zagreb vs other settlements)
- **HNB (Croatian National Bank)**: `https://www.hnb.hr/` — financial stability + housing market reports
- **OSS Uređena zemlja**: `https://oss.uredjenazemlja.hr/` — unified cadastre + ZK
- **MPGI — Pregled tržišta nekretnina Republike Hrvatske** (annual, published with Ekonomski institut Zagreb under Zakon o procjeni vrijednosti nekretnina Art. 20): recorded sale prices from the eNekretnine sale-price register (Zbirka kupoprodajnih cijena), as medians per m² by county, large city and JLS; units with fewer than 10 sales are suppressed. 2025 edition (presented Apr 2026): `https://mpgi.gov.hr/UserDocsImages/dokumenti/stambeno/Pregled-trzista-nekretnina-2025.pdf`

### Listing platforms

- **Njuškalo** (Njuškalo d.o.o., part of Styria Media Group AG) — general classifieds with a property section; self-reported 500,000+ visits and 10,000+ new ads a day (njuskalo.hr) and 4.8M monthly visitors across all categories (about.njuskalo.hr), no independent audit cited (2026 data, source Njuškalo ⚠️); publishes an annual asking-price analysis by county and city (latest 20 Feb 2026: `https://blog.njuskalo.hr/novosti/prosjek-trazenih-cijena-po-kvadratu-kuce-i-stana-za-cijelu-hrvatsku-i-u-prosloj-godini-rastao`): `https://www.njuskalo.hr`
- **Index Oglasi** — general classifieds; no measured ranking against Njuškalo: `https://www.index.hr/oglasi`
- **Crozilla** + **Indomio.hr** — both portals of Indomio Group (with Immobiliare.it, Spitogatos.gr, Nepremicnine.net); the group self-reports more than 90% of properties for sale in Croatia on its portals, no independent audit cited (2026 data, source Crozilla "O nama", archived 2026-10-21 ⚠️): `https://www.crozilla.com`, `https://www.indomio.hr`
- **Eurovilla.hr, dogma-nekretnine.com** — real-estate agencies with their own listings, not portals

### Price benchmarks

**Transaction data (primary — DZS, MPGI)**:
- **New flats sold, H1 2026**: €2,994/m² national, €3,518/m² Zagreb, €2,754/m² other settlements; +8.7% YoY national, +18.9% YoY Zagreb (2026 data, source DZS GRAD-2026-4-1/1, 7 Sep 2026)
- **House price index, Q2 2026 (provisional)**: +12.7% YoY national; Grad Zagreb +15.7%, Jadran (Adriatic) +9.0%, Ostalo (rest of country) +15.8%; new dwellings +9.2%, existing +14.1% (2026 data, source DZS CIJ-2026-2-1/2, 1 Oct 2026)
- **Recorded sale prices of flats/apartments, 2025**: national median €2,587/m² (+11.3% YoY), 5th–95th percentile €901–4,428/m²; 20,293 sales (−17.3%) worth €3.45bn; register extract of 14 Jan 2026, so late-filed 2025 sales are missing (2025 data, source MPGI / Ekonomski institut Zagreb, Pregled tržišta nekretnina RH 2025, §1.1, §3.1.1 and Table 3.1)

**Asking vs recorded sale prices, flats, 2025** — asking: average asking price per m² and change vs 2024 (2025 data, source Njuškalo annual asking-price analysis, 20 Feb 2026 — listing platform ⚠️, seller-controlled); sold: median contract price per m² and change vs 2024, county, city or municipality (JLS) level, never parcel level (2025 data, source MPGI / Ekonomski institut Zagreb, Pregled tržišta nekretnina RH 2025, Tables 3.2, 3.6, 3.7 and §3.1.4). An asking average and a sale median measure different things, so do not read the gap as a negotiation discount:

| Region | Avg asking €/m² (Njuškalo ⚠️) | Median sold €/m² + YoY (MPGI) |
|---|---:|---|
| **Zagreb** (Grad Zagreb) | 3,698 (+14.94%) | 2,917 (+8.7%) |
| **Split** (city) | 5,183 (+13.85%) | 4,067 (+14.1%), highest city median |
| **Dubrovnik** (city) | city not published; Dubrovačko-neretvanska county 3,834 (−1.06%) | 3,921 (+21.5%) on 142 sales; top 5% of sales at 6,615 or more |
| **Rijeka** | 3,319 (rising; % not published) | 2,808 (+13.8%) |
| **Pula** (Istria) | 3,283 (rising; % not published) | 2,456 (+13.3%) |
| **Zadar** (city) | city not published; Zadarska county 3,674 | 2,874 (+12.5%) |
| **Šibenik** (city) | city not published; Šibensko-kninska county 3,397 (−0.31%) | 2,436 (+37.0%) on 182 sales (−51.3%) |
| **Islands** | not published per island | no island-wide figure; JLS medians above 3,500: Malinska-Dubašnica 3,587, Punat 3,539, Baška 3,523 (all Krk); 3,000–3,500: Krk, Omišalj, Dobrinj (Krk), Bol (Brač), Cres, Mali Lošinj; Hvar and Korčula JLS in neither group (below 3,000, or fewer than 10 sales and not published) |
| **Slavonia** (5 counties) | county averages 1,315 (Vukovarsko-srijemska, −1.98%) to 1,979 (Brodsko-posavska) for four counties; Osječko-baranjska not published (2,000–3,000, computed by elimination: in neither the published under-2,000 nor the over-3,000 county list); Osijek city 2,465 (+17.54%) | county medians 1,092 (Požeško-slavonska) to 1,556 (Osječko-baranjska), all five up 8.6–23.0%; Osijek city 1,666 (+12.6%) |
| **National** | 3,636 (+6.5%) | 2,587 (+11.3%) |

### Compute

1. €/m² = price / **uporabna površina** (usable area)
2. Cross-check **OSS Uređena zemlja** for cadastre/ZK reconciliation
3. **HR dual register pitfall**: cadastre says one thing, ZK gruntovnica says another — common; must reconcile
4. **Adriatic premium** (computed from 2025 sale medians, MPGI Tables 3.2 + 3.6, county and city level): Splitsko-dalmatinska €3,333 ÷ Požeško-slavonska €1,092 = 3.1×; Split €4,067 ÷ Osijek €1,666 = 2.4×; lowest Adriatic county (Ličko-senjska €2,219) ÷ highest Slavonian county (Osječko-baranjska €1,556) = 1.4×
5. **Seafront/Old Town Dubrovnik**: the MPGI Pregled gives no sale median below city level outside Zagreb. The MPGI Plan približnih vrijednosti publishes an approximate flat value per price block (cjenovni blok) and floor-area class — flat layer as of 1 Jan 2025, i.e. 2024 average values — on the ISPU Geoportal (`https://ispu.mgipu.hr`, menu "Slojevi iz nadležnosti Ministarstva (MPGI)"; source MPGI / Ekonomski institut Zagreb, Pregled tržišta nekretnina RH 2025, ch. 7); check whether the flat's block carries a value. A block value is an average, not a valuation of the flat — have a certified appraiser (procjenitelj) pull recorded comparables. City-wide 2025 sales: median €3,921/m², top 5% at €6,615/m² or more (MPGI Table 3.7)

### Key terms

- Vlasništvo = ownership
- Etažno vlasništvo = condominium
- ZK uložak = land register title number
- Broj čestice = cadastral parcel number
- k.o. = cadastral municipality
- Energetski certifikat = energy certificate

---

## Section: `--traffic`

### Sources

- **HC (Hrvatske ceste)**: `https://hrvatske-ceste.hr/` — state roads + traffic counts; annual _Brojenje prometa na cestama Republike Hrvatske_ with PGDP + PLDP per counting site (2025 edition, published Jul 2026, under Promet i sigurnost → Brojenje prometa)
- **HAC (Hrvatske autoceste)**: `https://www.hac.hr/` — motorways (per-motorway PGDP / PLDP from toll counting is published in the HC annual count)
- **Local cities**: Zagreb GUP, Split urban data

### Key term

**PGDP (Prosječni godišnji dnevni promet)** = AADT-equivalent. **PLDP (Prosječni ljetni dnevni promet)** = average summer daily traffic — check it on coastal routes: across the A1 counting sites the 2025 PLDP ran 51% (Lučko-jug 74,330 vs PGDP 49,357) to 122% (Sveti Rok-jug 52,935 vs 23,888) above PGDP (2025 data, source HC Brojenje prometa 2025; % computed).

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural, islands)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (urban arterials, državne ceste; A6 Rijeka–Zagreb counting sites 15,761–20,697, A1 Bosiljevo 2–Šestanovac 13,658–25,372 — 2025 PGDP, source HC Brojenje prometa 2025)
- 🔴 > 35,000 v/d (A1 Zagreb–Bosiljevo 1 37,697–49,357; A3 Zagreb (istok)–Ivanić-Grad 37,638; D8 Solin 53,807 and Stobreč 59,470, the two busiest counting sites in HR; Zagreb ring — 2025 PGDP, source HC Brojenje prometa 2025)

---

## Section: `--tax`

### Annual property tax — Porez na nekretnine (NEW 2025)

**MAJOR REFORM 1 January 2025**: replaces the previous holiday-home tax (porez na kuće za odmor) (2026 data, source Porezna uprava). The communal fee (komunalna naknada) is a separate levy that continues: owed on residential space by the owner (or by a user who took it over in writing), and a buyer must report the new obligation to the grad / općina within 15 days of the purchase contract (Zakon o komunalnom gospodarstvu arts 91–94, NN 68/18, 110/18, 32/20, 145/24; 2026 data, source zakon.hr consolidation through NN 119/26).

#### Rate range

- **€0.60–€8.00/m²** of usable area per year; €0.60 applies where the grad / općina adopts no decision (ZLP art. 26 as amended by NN 152/24; 2026 data, source Narodne novine + Porezna uprava)
- Set by each municipality within range
- **Highest amount (€8 across the whole territory, 2026)**: 11 JLS — Umag, Fažana, Sveti Filip i Jakov, Biograd na Moru, Mali Lošinj, Nin, Lopar, Privlaka (ZD), Sutivan, Vir, Vrsi; Okrug, Opatija, Punat, Stari Grad and Vodnjan reach €8 in some zones only. Vis (to €6) and Baška Voda (to €3) cut their €8 amount for 2026 (2026 data, source Porezna uprava comparison table 2025/2026)
- **Major cities (2026)**: Zagreb €5 (€8 across the whole city from 1 Jan 2027 — Odluka o izmjenama Odluke o lokalnim porezima of 16 Oct 2026, Službeni glasnik Grada Zagreba 32/2026 of 19 Oct 2026, arts 3 + 6; assessments started before 1 Jan 2027 keep the old amount, art. 5; text at `https://www1.zagreb.hr/sluzbeni-glasnik/index.html#/app/akt?id=7a59dddf-3c72-4c50-9c9c-e008d93cafab`), Split €5 (€1.99 in 2025), Rijeka €5, Osijek €0.60, Dubrovnik zoned €0.60–€5.00 (2026 data, source Porezna uprava comparison table 2025/2026)
- 125 cities/municipalities at floor (€0.60); 84 at €5–€8; vs 2025: 41 raised, 12 lowered, 503 unchanged (2026 data, source Porezna uprava — JLS decisions submitted by 31 Dec 2025)
- _(Per-JLS amounts: Porezna uprava comparison table `https://porezna-uprava.gov.hr/UserDocsImages/Portal_porezne_konkurentnosti/Odluke_JLS/Porez_na_nekretnine/2026/Usporedba%20poreza%20na%20nekretnine%2025_26.xlsx`, compiled from JLS decisions received by 31 Dec 2025 — confirm against the municipality's own odluka. Zoned JLS (e.g. Dubrovnik €0.60–€5.00, Opatija €0.66–€8.00, Stari Grad €3.00–€8.00) set the amount per zone: a municipal range never fixes a parcel's amount without the zone map)_
- Revenue split 80% municipality / 20% county (ZLP art. 28 as amended by NN 152/24; 2026 data, source Porezna uprava)

#### Exemptions

- Homes used for permanent living (stalno stanovanje), whoever lives there — a registered prebivalište alone does not prove it, and the owner must prove permanent living when the tax office asks (ZLP art. 27(1)(1), (3))
- Homes let under a lease for permanent living for at least 10 months of the tax year (art. 27(1)(2), (5))
- Homes unfit for living after a declared natural disaster, or where residential use is impossible (no infrastructure connection or substitute equipment) (art. 27(1)(6)–(7), (6))
- Also exempt: a tourist-letting host's own permanent home, public-use and institutional housing, JLS-owned property, and company stock held for sale or homes taken over for unpaid debts for under 6 months at 31 March (art. 27(1)(3)–(5), (8)–(9)); councils may exempt socially vulnerable citizens (art. 27(2)) (source Narodne novine NN 152/24, in force 1 Jan 2025)

#### Typical bills

| Property | Annual |
|---|---:|
| Zagreb 80m² apt (€5/m², 2026) | €400 (80 × 5); from 1 Jan 2027 at €8/m²: €640 (80 × 8, computed) |
| Split 100m² apt (€5/m², 2026; €1.99 in 2025) | €500 (100 × 5, computed) |
| Dubrovnik 100m² (zoned €0.60–€5.00/m², 2026) | €60–€500 (100 × 0.60 to 100 × 5, computed — the zone decides) |
| Grad Hvar 100m² (€3/m², 2026) | €300 (100 × 3, computed); other Hvar-island JLS: Jelsa €3.50, Stari Grad zoned €3–€8, Sućuraj €1.99 |
| Sveti Filip i Jakov 80m² (€8/m², 2026) | €640 (80 × 8, computed) |
| Tisno 80m² (€7.50/m², 2026; €5 in 2025) | €600 (80 × 7.50, computed) |

_(2026 amounts: Porezna uprava comparison table 2025/2026. A bill applies only to a taxable home — not lived in permanently and not let long-term for 10+ months; see Exemptions)_

### Transaction taxes

- **Porez na promet nekretnina** (Real estate transfer tax, RETT): **3%** on resale (no VAT) — ZPPN art. 12; an acquisition on which VAT is charged is not a taxable transfer (art. 5(2)) (2026 data, source zakon.hr consolidation through NN 110/26)
- **PDV** (VAT): **25%** on new builds first sale (standard rate 25%; reduced rates 13% and 5% cover listed goods and services, none the supply of a dwelling — ZPDV art. 38(1)–(3); 2026 data, source Porezna uprava + zakon.hr consolidation through NN 119/26)
- **Javni bilježnik** (notary): fees fixed by the Pravilnik o privremenoj javnobilježničkoj tarifi, point value €2.00 (art. 40). Certifying one signature (ovjera potpisa): 3 points = €6 (art. 19(1)). Notarial deed (javnobilježnički akt) above €53,089.12: 255 points + 5 points per started €6,636.14 of the excess, max 4,000 points (art. 12(1)–(2)) — €590 at a €100,000 price (0.59%), €740 at €200,000 (0.37%), €890 at €300,000 (0.30%) (computed); solemnising a private contract costs 50% of that (art. 16(1)). Tariff award only — expenses and any PDV extra (2026 data, source zakon.hr consolidation through NN 119/26; last amended NN 139/24, in force 12 Dec 2024, computed)
- **Realtor commission**: est. 2–3% per side (market practice from the 2026-04 research, no published statistic — compare the agencies' price lists). No statutory cap: the fee is set in the written brokerage contract and the agency's price list (cjenik) and is earned only once the sale contract (or, if so agreed, the pre-contract) is signed, with no advance payment; a buyer who signed no brokerage contract with the agent owes nothing; where both sides pay, the two fees together may not exceed the price-list maximum, and where only one side pays under two contracts, at most half of it (Zakon o posredovanju u prometu nekretnina, NN 69/26 arts 28, 29(1)–(2), 29(7), 30(3)–(4); published 29 Jun 2026, in force 7 Jul 2026, computed; 2026 data, source Narodne novine)
- **First-home refund (contracts from 1 Jan 2025)** — since 7 May 2026 under the Zakon o priuštivom stanovanju (NN 45/26 of 29 Apr 2026, arts 62–66; in force on the 8th day after publication, computed), which replaced the Zakon o društveno poticanoj stanogradnji (arts 30.c–30.f added by NN 72/25; Pravilnik NN 86/25): refund of the full RETT paid on a resale (capped at 3% of the statutory base) OR 50% of the VAT paid on a new build (capped at 12.5% of the base). **Adult Croatian citizens only** — foreign buyers, EU nationals included, cannot claim it. Under 45 at application; price per m² not more than 50% above the local average and weighted area (vrijednosna površina) not more than 50% above the recognised area (50 m² for one person up to 120 m² for 7+, +50% for a single-family house); apply to **APN** within **24 months** of acquiring ownership; repay with default interest if sold, let, prebivalište deregistered or not lived in within 5 years of payment (2026 data, source Narodne novine NN 45/26). Excluded if the applicant or close family owns or has owned, alone or jointly, in Croatia or abroad, a residential property (art. 65(3)(1)) — unless that home does not count as suitable for the family (art. 12(3)–(4)) and is sold within 24 months of the purchase (art. 65(4)) — or has already had a state housing-loan or other state housing subsidy (art. 62(3)); applicant and close family must have registered prebivalište at, and live in, the property when applying (art. 65(1)(3))

### Capital gains

- **Disposal within 2 years** of acquisition (or of the building becoming fit for use, if built, reconstructed or converted): gain taxed at a flat **24%** porez na dohodak, assessed by Porezna uprava decision and payable within 15 days; gain = market-value proceeds − acquisition cost uplifted by industrial producer-price growth − documented improvement and sale costs (ZPD arts 58(1)–(2) + 62(3), as amended to NN 152/24; 2026 data, source zakon.hr consolidation through NN 110/26)
- **Not taxed after 2 years** — except where more than 3 properties of the same type are sold within 5 years of acquisition: the combined gain is then taxed at 24% (each flat, business unit or land parcel counts as one property; art. 58(3) + 62(4))
- **Exempt at any holding period**: a home that served as the residence of the seller or dependent close family (a registered prebivalište alone is not proof), expropriation, transfers between spouses / first-line relatives / close family or on divorce, and disposals directly linked to inheritance (art. 58(4)–(5))

### Total transaction cost (buyer side)

- Resale: ~5.0–6.6% at a price of €100,000 or more (computed: 3% RETT + notary from €6 for a signature certification to 0.59% for a notarial deed at €100,000 + est. 2–3% buyer-side realtor); lawyer drafting fees and land-register court fees not included
- New build: 25% VAT in price (no RETT where VAT is charged — ZPPN art. 5(2)) + other costs est. ~0–3.6% at a price of €100,000 or more (computed: notary €6 to 0.59% as above + est. 0–3% realtor, only where a broker is used)

### Future risk

- Porez na nekretnine: municipalities keep recalibrating — for 2026, 41 JLS raised and 12 lowered their amount (2026 data, source Porezna uprava); Zagreb goes from €5 to €8/m² on 1 Jan 2027 (Službeni glasnik Grada Zagreba 32/2026)
- VAT: no change to the 25% standard rate enacted — ZPDV art. 38(1) still reads 25% in the zakon.hr consolidation through NN 119/26; NN 48/26 lets the Government set a temporary rate on excise energy products by decree (art. 38.a), and the VAT bill sent to the Sabor on 10 Sep 2026 transposes the EU VAT-in-the-digital-age rules from 1 Jan 2027, with no rate change in the report (Hina via informator.hr, 10 Sep 2026, news-tier)
- **Construction-law package (in force 1 Jan 2026)**: Sabor adopted the Zakon o prostornom uređenju, Zakon o gradnji and Zakon o energetskoj učinkovitosti u zgradarstvu on 15 Dec 2025, all in force 1 Jan 2026, with a 30-day building-permit target (2025 data, source Hina via informator.hr, 29 Dec 2025; for the Zakon o gradnji, the 15 Dec 2025 adoption and 1 Jan 2026 entry into force are confirmed in Narodne novine NN 155/25 of 23 Dec 2025). **Criminal liability** for illegal building still covers only protected nature areas, cultural heritage and other areas of special state interest — 6 months to 5 years' prison (Kazneni zakon art. 212; the zakon.hr consolidation updated 1 Nov 2026 through NN 119/26 lists NN 136/25 as the last amendment). Wider criminalisation of building without a permit, through Kazneni zakon amendments, was announced by minister Bačić in Jan 2026 (Novi list, 15 Jan 2026, news-tier) and is not enacted in that consolidation. Starting work before the building permit is issued triggers a special fee (posebna naknada), not a fine: the permit authority notifies the building inspectorate and gives the investor 15 days to pay €4,000 for a less complex building, €15,000 for a multi-unit building or 1% of the estimated works value for other structures, payable to the local or regional unit, and the permit is issued only once it is paid (Zakon o gradnji NN 155/25 arts 72(1)–(3), 73(1)(7), 73(2)(9), 74(7); Novi list, 15 Jan 2026, reported these amounts as fines). Separately, an investor who starts building without a final or enforceable building permit, or deviates from it, is fined €20,000–€30,000 if a legal person plus €3,000–€6,000 for its responsible person, and €3,000–€6,000 if a natural person, all halved for a less complex building (art. 120(1), (4), (5), (7)) (in force 1 Jan 2026; 2026 data, source Narodne novine). **Legalizacija** (Zakon o postupanju s nezakonito izgrađenim zgradama, amended by NN 48/26 — adopted 30 Apr 2026, published 8 May 2026, in force 16 May 2026, the 8th day after publication, computed): a request, filed through eDozvola, needs a DGU certificate that the building is visible on the DOF5/2011 orthophoto or another DGU orthophoto from aerial survey up to 21 Jun 2011, or proof that it was recorded on the cadastral plan or another official map by that date (art. 11(1) as amended); the amended art. 10 sets no filing deadline, so the 30 Jun 2018 cut-off (art. 10(2) as amended by NN 65/17) no longer applies, but a request already finally refused cannot be filed again, except one refused for missing documents or an unpaid fee (art. 10(3) + NN 48/26 art. 26) (2026 data, source Narodne novine NN 48/26 + NN 65/17)
- **Pomorsko dobro** (Maritime Domain) is statutory **inalienable public good** under Zakon o pomorskom dobru i morskim lukama (land strip at least 6 m wide measured from the line of mean higher high water + territorial sea/seabed; out of legal commerce, no ownership or other real right can be acquired — NN 83/23 arts 4(1), 5(1), 6(3), source Narodne novine). Cannot be owned by anyone (HR or foreign) — only concessions available. Seafront listings promising "beach ownership" are selling something legally non-ownable.

---

## Section: `--rental`

### Long-term residential

- **Zakon o najmu stanova** (Tenancy Act; NN 91/96 … 68/18, 105/20; consolidated text in force since 26 Sep 2020, source zakon.hr): written contract (Art. 4), fixed or indefinite term (Arts 5, 25); a fixed-term contract renews tacitly for the same term unless either side gives written notice at least 30 days before expiry (Art. 25). The Act sets no minimum term (Art. 5 only requires the term to be stated); typical contract length: data not publicly available — 1–3 years is curated market practice, not measured
- **Termination**: the landlord may terminate for misuse (non-payment, unauthorised sublet, disturbance, non-residential use and other Art. 19 grounds) after a written 30-day warning to cure, or without a warning after more than two breaches (Art. 19), with 3 months' notice (Art. 22); ending an indefinite contract for the landlord's or close family's own use needs 6 months' notice and another suitable flat for the tenant (Arts 21–22); the tenant may end an indefinite contract on 3 months' notice (Art. 23)
- **Rent**: freely agreed (slobodno ugovorena najamnina, Art. 9); on an indefinite contract it cannot change in the first year, and a later increase is capped at 20% above the average freely agreed rent for comparable flats in the settlement or county (Arts 10–11). Exception: protected tenants (zaštićeni najmoprimci, former stanarsko pravo holders) pay a zaštićena najamnina set under Government criteria (Arts 7–8); for privately owned flats with a sitting protected tenant, the Statileo enforcement act (NN 36/24, in force 2 Apr 2024) provides for a register kept by the housing ministry (MPGI) and, from 1 Jan 2025, programme measures, including a transitional lease in which tenant and state each pay 50% of the average rent (Arts 4, 7) — ask the seller whether the flat is on that register (2026 data, source zakon.hr consolidated texts)

### Short-let — MAJOR 2025 CRACKDOWN

**Zakon o upravljanju i održavanju zgrada** (NN 152/24, 47/26; in force 1 Jan 2025) + **Zakon o ugostiteljskoj djelatnosti** amendment (NN 152/24):
- **Two-thirds co-owner consent** (prior, written) required to let a flat short-term in a multi-unit building (Art. 34); the MPGI model consent decision counts co-owners holding more than 66% of the total floor area of all special parts. The enacted text has no 80% threshold (2026 data, source Narodne novine NN 152/24 + zakon.hr consolidated text + mpgi.gov.hr model decision)
- **Plus consent of every owner of an adjoining flat** (sharing walls/floors/ceilings); consent runs for a fixed term of at least 5 years, binds later owners, and can be revoked by simple majority after 3+ house-rule breaches within 2 years (Art. 34)
- Flats already let short-term on 1 Jan 2025 must collect the consent within 5 years (Art. 63(2)); the household-accommodation approval requires it (Zakon o ugostiteljskoj djelatnosti Art. 34(2) point 4)
- **Registration number — PROPOSED, not in force**: the new Zakon o ugostiteljskoj djelatnosti (P.Z.E. 315; Sabor accepted the first reading 3 Jul 2026, 78 for / 14 against / 37 abstentions) implements Regulation (EU) 2024/1028 — one registration number per accommodation unit, requested through the integrated tourism information system and shown in every platform listing; the Government's final bill (Konačni prijedlog, second reading; in procedure since 21 Oct 2026, no plenary vote recorded as of 2026-11-04) puts the act in force on 1 Jan 2027 but the registration-number provisions (Arts 46–49) only on 1 May 2027 (Art. 92), keeps prior written co-owner consent as a condition of the household approval (Art. 35(2) point 4), and for hosts approved under the current act in a multi-unit or residential-commercial building ends the right to let by law, with the approval revoked ex officio, if that consent is not obtained within the Zakon o upravljanju i održavanju zgrada deadline (Art. 84) (2026 data, source sabor.hr P.Z.E. 315 first-reading and final bill texts). The consolidated act in force (NN 85/15 … 152/24, source zakon.hr) has no unit registration number
- **Supply**: ~7,000 STR beds reported removed in one Dalmatian county (single secondary report — county/year unconfirmed; anecdotal, not data). Nationally, permanent beds in holiday and other short-stay accommodation (NKD 55.2, which includes household lets) fell 1.9% to 718,375 in 2025 and all tourist beds 1.6% to 1,160,182, ending a multi-year rise; the release gives no county split and no cause (2025 data, source DZS TUR-2025-1-2, 26 Feb 2026)

#### Categories

_Approval (rješenje) and categorisation are issued by the county administrative office (in Zagreb, the Gradski ured za gospodarstvo), not by the Turistička zajednica (2026 data, source Porezna uprava — Iznajmljivač turistima)._

- **Apartman** (apartment)
- **Soba** (room)
- **Studio apartman** (studio)
- **Kuća za odmor** (holiday house)

#### Tax

- **Long-term letting** (porez na dohodak od imovine): **12%** on rent less a flat **30%** expense allowance = 8.4% of gross rent (computed 0.12 × 0.70) (2026 data, source Porezna uprava — Najmodavac stambenog prostora)
- **Tourist letting in a household** (owner-let, max 20 beds or 10 camp units, outside VAT): no % income tax — an annual **paušalni porez per bed** (tax = beds × per-bed amount), set by the local council by 15 Dec for the next year within ranges by tourism-development category (ITR): Cat I €100–300 (€200 if no decision), Cat II €70–200 (€135), Cat III €30–150 (€90), Cat IV/0 €20–100 (€60); paid quarterly (2026 data, source Porezna uprava — Iznajmljivač turistima)
- **PROPOSED from 1 Jan 2027, not adopted**: Government bill P.Z. 339 (sent to Sabor 10 Sep 2026; first reading accepted 25 Sep 2026, 79 for / 3 against / 37 abstentions; final bill sent to Sabor for second reading on 5 Nov 2026, figures unchanged; ZPD still cited as NN 115/16 … 152/24 in Narodne novine 120/2026 of 21 Oct 2026, and no amending act in issues 121–127 up to 4 Nov 2026) raises Cat I to €150–300 (default €225) and Cat II to €100–200 (default €150); Cat III and IV/0 unchanged; councils whose current amount falls outside the new range must adopt and file a new decision by 1 Mar 2027, otherwise the default applies (final bill Arts 6, 18, 21; source vlada.gov.hr 222nd session, 5 Nov 2026) — verify the enacted text in Narodne novine
- Above those household limits, or once inside the VAT system (threshold €60,000 since 1 Jan 2025), letting income is taxed as self-employment from business books

---

## Section: `--work=<profession>`

### Sources

- **HZZ (Hrvatski zavod za zapošljavanje)**: `https://www.hzz.hr/` — employment service
- **MojPosao** — biggest: `https://mojposao.hr/` (moj-posao.net 301-redirects here, checked 2026-10-23; operator Alma Career Croatia d.o.o.)
- **Posao.hr**, **Njuškalo Posao** (`https://www.njuskalo.hr/posao` — bika.net 301-redirects here, checked 2026-10-23), **LinkedIn HR**

### Self-employment

- **Obrt** = sole trader (registered at HOK)
- **D.o.o.** = limited; min €2,500 share capital; **j.d.o.o.** (simplified, max 5 members) min €1 (Zakon o trgovačkim društvima Arts 389(2), 390.a(3); 2026 data, source zakon.hr consolidated text)
- **PDV (VAT)** registration: above €60,000 annual domestic turnover, since 1 Jan 2025 (2026 data, source Narodne novine NN 152/24 Art. 90(1) + Porezna uprava)
- **Paušalni obrt**: flat-rate tax for obrtnici outside VAT with receipts up to €60,000/yr; 12% on a fixed bracket base, paid quarterly (2026 data, source Porezna uprava — Obrtnici paušalisti). **PROPOSED from 1 Jan 2027, not adopted** (P.Z. 339): recognised expenses cut from 85% to 70% for receipts €40,000.01–50,000 and to 55% for €50,000.01–60,000; brackets up to €40,000 unchanged (source sabor.hr P.Z. 339 bill text)

### Salary benchmarks (2026)

- **National** (employees of legal entities, June 2026): median gross **€1,850**/month, average gross €2,184; median net €1,345, average net €1,555 (2026 data, source DZS RAD-2026-1-1/6, 21 Aug 2026)
- **Grad Zagreb** (city, May 2026): median gross €2,110, average gross €2,528 (2026 data, source City of Zagreb statistics bulletin of 12 Aug 2026, DZS data)
- **County average gross, Q2 2026** (county of the employee's residence — county-level, not city-level): Grad Zagreb €2,604 (highest); Primorsko-goranska (Rijeka) €2,189; Splitsko-dalmatinska (Split) €2,085; Osječko-baranjska (Osijek) €2,034; Istarska €2,029; Dubrovačko-neretvanska €1,995; Virovitičko-podravska €1,865 (lowest) (2026 data, source DZS RAD-2026-1-6/2, 28 Aug 2026)
- **Minimum wage**: €1,050/month gross for 2026 (Uredba o visini minimalne plaće za 2026., NN 132/2025); the 2027 amount is set by government decree by 31 Oct 2026 and cannot be lower than the 2026 amount (Zakon o minimalnoj plaći Arts 5–6) — verify the 2027 decree in Narodne novine

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **DHMZ (Croatian Meteorological & Hydrological Service)** | `https://meteo.hr/` | Weather, climate, **CFFWIS fire index** — Canadian FWI method, computed daily Apr–Oct since 1981 (DHMZ, WMO/EUMETSAT 2017 presentation); daily station table at `https://meteo.hr/podaci.php?section=podaci_agro&param=pozarind` |
| **HGI-CGS (Croatian Geological Survey)** | `https://www.hgi-cgs.hr/en/` | Geology, **earthquake**, karst |
| **Seizmološka služba (PMF Zagreb)** | `https://www.pmf.unizg.hr/geof/en/seismological_survey` | Seismic monitoring |
| **Hrvatske vode** (national water-management agency) | `https://www.voda.hr/` | Flood + water management; flood hazard + flood risk maps (2019 cycle, high / medium / low probability) in the `https://preglednik.voda.hr/` viewer |

### Specific risks

#### Earthquake — CRITICAL

- **Zagreb area**: highest 475-yr reading among these continental town centres on the 2011 PGA map — central Zagreb (Ban Jelačić Square) 0.255 g, Samobor 0.251 g, then Koprivnica 0.220 g, Krapina 0.185 g, Karlovac 0.161 g, Varaždin 0.155 g, Petrinja 0.152 g, Bjelovar 0.138 g (2011 maps, source PMF Geofizički odsjek hazard-map reader `http://seizkarta.gfz.hr/hazmap/karta.php`, read at OpenStreetMap town-centre coordinates; ground type A, not parcel values; the reader labels its readings orientation only, not official)
- **22 March 2020 Zagreb (ML 5.5; USGS Mww 5.3)** — major damage; USGS epicentre 45.907 N 15.970 E, ~10 km N of Ban Jelačić Square (computed 10.5 km) (source MPGI seismic-data manual, 2023 + USGS event us70008dx7)
- **29 December 2020 Petrinja (ML 6.2 / Mw 6.4, PMF Geofizički odsjek)** — epicentre ~48 km SE of central Zagreb (computed: great-circle distance from the USGS epicentre 45.424 N 16.257 E, event us6000d3zh, Mww 6.4, to Ban Jelačić Square 45.813 N 15.977 E = 48.4 km); **still under reconstruction**: at 31 Dec 2025 works were finished on 14,284 buildings and under way on 1,949 across the Zagreb + Petrinja quake areas (1,245 structural renovations, 206 replacement houses, 15 multi-apartment buildings); 1,197 mobile housing units still stood beside damaged houses, while all classic container settlements were closed (2025 data, source Government report on the Reconstruction Act to the Sabor, 7 May 2026)
- **PGA hazard maps** (Karta potresnih područja RH 2011, PMF Geofizički odsjek; part of HRN EN 1998-1:2011/NA:2011) for 95- and 475-year return periods on ground type A (bedrock), with 225-yr values in the PMF reader app; e.g. central Zagreb (Frankopanska / Ilica) agR 0.256 g at 475 yr and 0.129 g at 95 yr — local soil layers can amplify these (2011 maps, source MPGI seismic-data manual, 2023); the PMF hazard-map reader `http://seizkarta.gfz.hr/hazmap/karta.php` gives 0.252–0.256 g at 475 yr, 0.182–0.184 g at 225 yr and 0.127–0.129 g at 95 yr for the grid cells around Frankopanska and Ban Jelačić Square — it labels its readings orientation only, not official, and states the maps with their Annex C are part of the National Annex to the HRN EN 1998 series
- **Slavonia** (E HR): lowest 475-yr readings in the east — Vukovar 0.089 g, Vinkovci 0.106 g, Osijek 0.111 g — but higher in central Slavonia: Đakovo 0.159 g, Našice 0.172 g, Slavonski Brod 0.178 g, Požega 0.185 g (2011 maps, same PMF hazard-map reader at OpenStreetMap town-centre coordinates)
- **Coastal Adriatic**: variable — strongest documented: Great Dubrovnik earthquake of 6 Apr 1667 (ML 7.1, estimated from intensity IX–X °MCS), Trilj 1898 (ML 6.7, estimated), Imotski 1942 (ML 6.2), Makarska 1962 (ML 6.1), Ston-Slano 5 Sep 1996 (ML 6.0) (source MPGI seismic-data manual, 2023); 475-yr PGA readings run from Pula 0.079 g and Poreč 0.090 g in Istria to Split 0.220 g, Dubrovnik 0.303 g, Imotski 0.323 g and Ston 0.347 g (2011 maps, same PMF hazard-map reader at OpenStreetMap town-centre coordinates); the 15 Apr 1979 M6.9 (Ms) earthquake had its epicentre in Montenegro, 6 km E of Stari Bar, not in Croatia (USGS ISC-GEM)

#### Wildfire

- **Adriatic / Dalmatia coast**: critical fire zone
- **DHMZ CFFWIS** (Canadian Forest Fire Weather Index System) since 1981, computed daily Apr–Oct (DHMZ, WMO/EUMETSAT 2017 presentation); based on 13:00 CET observations (14:00 summer time), with five Adriatic danger classes set from a 7-year statistical analysis (Dimitrov, 1982): FWI < 5 very low, 4 < FWI < 9 low, 8 < FWI < 17 moderate, 16 < FWI < 33 high, FWI > 32 very high (source DHMZ method page `https://meteo.hr/podaci.php?section=podaci_agro&param=pozarind&el=opis`)
- **2024 (national)**: 3,892 vegetation fires, +29% vs 2023 (computed: 3,892 vs 3,013); 23,410 ha burnt by HVZ estimate (procijenjena opožarena površina) (2024 data, source HVZ reports on the 2024 and 2025 Program aktivnosti, DVOC 193 data processed to 15 Feb 2025, `https://hvz.gov.hr/izdvojeno-11/program-aktivnosti-2026/izvjesca-programa-aktivnosti/2828`) — rates/figures may have changed since; the earlier DVOC 193 tally of 3,825 fires and 26,807 ha (via tportal, 3 Jan 2025 — secondary) is superseded
- **2025 (coastal + karst area)**: 2,821 vegetation fires, −10.2% vs the prior 5-yr average; 6,094 ha burnt, −70.1% (2025 data, source HVZ Program aktivnosti presentation, Feb 2026)
- Pinewood resin = high fire intensity
- Ferry-route disruption common Jul-Aug

#### Karst hazards

- **Dinaric karst**: sinkholes, doline, cave drainage
- **Coastal hinterland Adriatic** + Lika + Gorski Kotar
- **HGI-CGS** publishes geological maps
- HGI-CGS lists hazard processes in karst among its research topics, with landslides and rockfalls its current research priority; its geological-hazards page offers no sinkhole register (source HGI-CGS, `https://www.hgi-cgs.hr/geoloski-hazardi/`). Its landslide guide for homeowners warns that landslide damage is usually not covered by insurance (source HGI-CGS safEarth brochure, `https://www.hgi-cgs.hr/wp-content/uploads/2022/02/safEarth_brosura-klizista.pdf`)
- The Zakon o gradnji (NN 155/25, in force 1 Jan 2026) has no karst-specific rule; under its Art. 35(1) a geotechnical report (geotehnički elaborat) precedes the main design where a special law prescribes it or where it is needed — ask whether one was made for the house (2026 data, source zakon.hr consolidated text)

#### Other risks

- **Coastal storm + sea-level rise**: Adriatic
- **Flood**: inland Sava, Drava, Una — May 2014: Sava embankment breached at Rajevo Selo / Račinovci (southern Slavonia, Gunja evacuated) and Una flooding in Hrvatska Kostajnica / Dvor (secondary — Wikipedia, 2014 Southeast Europe floods); a disaster (katastrofa) was declared for the flooded area of Vukovar-Srijem County, with a special recovery act (Zakon o saniranju posljedica katastrofe na području Vukovarsko-srijemske županije, NN 77/14, promulgated 20 Jun 2014). For any address, Zagreb included, check the flood polygons in `https://preglednik.voda.hr/`
- **Bura (Adriatic strong NE wind)** — winter storms
- **Hrvatske vode** (`https://www.voda.hr/`) — flood hazard + flood risk map viewer (2019 cycle) at `https://preglednik.voda.hr/`

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead (curated era heuristic — wisdom, not data; confirm by building survey). Asbestos cement is not original pre-1900 fabric: it was patented in Austria in 1901, so any found came with later repairs (secondary — Wikipedia, Fiber cement siding) |
| **1900–1990 (Yugoslav era)** | Asbestos common, Yugoslav-era panel buildings (Novi Zagreb) (curated era heuristic — wisdom, not data; confirm by building survey) |
| **1981–2012** | 1981 seismic rulebook (Pravilnik o tehničkim normativima za izgradnju objekata visokogradnje u seizmičkim područjima); its intensity-based seismic map stayed the HR design basis until 2012. Yugoslav seismic design duties began after the 1963 Skopje quake (source MPGI seismic-data manual, 2023). The first seismic rulebook came in 1964, so buildings up to 1965 were in practice built without seismic rules; the 1981 rulebook replaced it and stayed in force for concrete and masonry buildings until 2007 and for steel and timber structures until 2012. MPGI expects most buildings designed under it in 1982–2007 to have adequate seismic resistance, but most pre-1965 buildings, and 1965–1982 buildings taller than ground + 3 floors in moderate- and high-intensity areas, to need strengthening (source MPGI, Smjernice za izradu analize postojećeg stanja zgrade — mehanička otpornost i stabilnost, 12 Sep 2024, `https://mpgi.gov.hr/UserDocsImages/dokumenti/EnergetskaUcinkovitost/Smjernice_APSZ/Smjernice%20za%20izradu%20analize_I_MEHANICKA%20OTPORNOST%20I%20STABILNOST_2024_09_12.pdf`). Current rules use 8 Oct 1964 as the cut-off: a reconstruction (rekonstrukcija) of a family house or residential / commercial building designed before that date must reach a significant-damage index (IZO) of at least 0.75 (Tehnički propis za građevinske konstrukcije NN 17/17 Art. 24(5) as amended by NN 7/22, kept in force by Zakon o gradnji NN 155/25 Art. 158; source Narodne novine + zakon.hr consolidated text) |
| **Post-2012 EC8** | Modern seismic — HRN EN 1998-1:2011/NA:2011 with the 2011 PGA hazard maps (source MPGI seismic-data manual, 2023) |
| **Post-2020 quake reconstruction** (Zagreb + Petrinja areas) | Not automatically full EC8: the Zakon o obnovi zgrada oštećenih potresom (NN 21/23, Arts 17, 18, 24) sends structural work to the Tehnički propis za građevinske konstrukcije, whose Annex III (NN 75/20, replaced by NN 7/22) sets levels — level 2 repair IZO ≥ 0.5, level 3 strengthening IZO ≥ 0.75, level 4 full structural renovation IZO ≥ 1.0 against the HRN EN 1998 series; IZO = design seismic resistance ÷ demand at the significant-damage limit state. Level 4 is set for importance-class IV buildings and for class II–III buildings with EMS-98 damage grade 4–5; owners renovating themselves may go above the prescribed level (Art. 24(2)). Ask which level a 'renovated' building reached (source Narodne novine) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetski certifikat** | Required before sale, rental or lease, and the energy class must appear in ads; exemptions incl. freestanding buildings < 50 m² and homes used < 4 months/yr (gov.hr, verified 2026-10-23). Sale duty since 1 Jul 2013, rental since 1 Jan 2016 (Pravilnik amendment NN 78/13) | 10 years from issue (gov.hr, verified 2026-10-23) |
| **Written contract + certified seller signature** | The sale contract must be in writing (Zakon o obveznim odnosima Art. 377; zakon.hr consolidated text to NN 69/26). Land-register entry (uknjižba) needs a public document, or a private one in which the seller's signature is certified (ovjera potpisa) and the seller expressly consents to registration (clausula intabulandi) (Zakon o zemljišnim knjigama NN 63/19 Arts 57, 59, 60; Art. 57 as amended by NN 128/22, 127/24). A full notarial deed (javnobilježnički akt) is one way to meet this, not a requirement. Entry requests are filed only electronically, through a notary or a lawyer; the notary who certifies the signature must file the request unless a party expressly objects (Art. 105 as replaced by NN 128/22 and amended by NN 127/24; source Narodne novine + zakon.hr consolidated text) | At signing; then the land-registry filing |
| **OSS Uređena zemlja extract** | Title verification | Current |

### Climate change projections

- **Temperature**: mean annual +1.0–1.2 °C in 2011–2040 and +1.9–2.0 °C in 2041–2070 vs 1971–2000 under RCP4.5, up to +2.2 °C on the Adriatic in summer and autumn of 2041–2070 (2020 data, source Strategija prilagodbe klimatskim promjenama, NN 46/2020 — rates/figures may have changed since)
- **Adriatic sea-level rise**: +32–65 cm by 2100, newer estimates up to 1.1 m; adding occasional extreme sea levels (+0.84–1.15 m) gives end-century peaks of ~1.4–2.2 m (2020 data, source NN 46/2020 — rates/figures may have changed since)
- **Reduced summer precipitation**: −10–15% in mountain areas and northern Dalmatia by 2041–2070 under RCP4.5 (−5–8% in northern Dalmatia under RCP8.5), while winter totals may rise in the north (2020 data, source NN 46/2020 — rates/figures may have changed since)
- **Increased wildfire risk**
- **More extreme rainfall events** (continental)

---

## Section: `--mains`

### Sources

- **Vodovod i kanalizacija** per municipality (e.g., Vodoopskrba i odvodnja d.o.o. — ViO, Zagreb, `https://www.vio.hr/`; Vodovod i kanalizacija d.o.o. Split, `https://www.vik-split.hr/`)
- **Tariff example (Grad Zagreb only — other service areas differ)**: households on sewer + treatment pay **€2.04/m³** all-in variable (13% PDV on the service parts plus the water-use, water-protection and development charges) + **€1.32/month** fixed, applying from 1 Mar 2026 (2026 data, source ViO price sheet; Službeni glasnik Grada Zagreba 07/2026)
- **Duty to connect**: the owner of an existing building must connect it within one year of the operator's notice that connection is possible; exempt are owners whose water supply is covered by a concession or water-rights permit, or whose wastewater is handled in line with the local wastewater decision or a water-rights permit (Art. 58). The operator or its contractor builds the connection and the owner pays the actual cost of the works and the meter unless the operator's general supply conditions say otherwise (Zakon o vodnim uslugama NN 66/19 Arts 55(2), 57, 58; source Narodne novine; no amendments listed in the zakon.hr consolidated text, 2026)
- Coastal islands: often septic / cisterns

### Costs

_Operator-published rows are for one service area each — other areas differ; ask the local operator for a quote._

| Scenario | Cost (€) |
|---|---:|
| Mains connection — Grad Zagreb household | Connection works paid by the City for natural persons who applied after 2 Aug 2016 (City Assembly decision of 13 Dec 2023); the internal installation, incl. the meter shaft, stays with the owner (2026 data, source ViO — Priključenje na komunalne vodne građevine) |
| Mains connection — elsewhere | Billed at the actual cost of works and meter unless the operator's general supply conditions say otherwise (Zakon o vodnim uslugama Art. 57; ViO: price depends on actual site costs, incl. road reinstatement). VIK Split bills connection works at unit rates, materials extra: €55.00/h excl. PDV (€68.75 incl.) for works in normal hours, plus hourly office, supervision and surveying rates (2026 data, source VIK Split Cjenik usluga (osim vodnih), rates applying from 1 Apr 2025). Some councils subsidise, e.g. Općina Stupnik reimburses up to €663.61 for a household water connection (2026 data, source ViO) |
| Septic upgrade | data not publicly available — get local contractor quotes and ask the local Vodovod i kanalizacija for its septic-tank rules |
| Septic / holding-tank emptying (Split area) | €7.12/m³ excl. PDV (Split, Podstrana, Solin) to €17.91/m³ (Marina); minimum 10 m³ billed; prices hold within 20 m of the truck and 3 m height difference (2026 data, source VIK Split price list from 1 Jun 2026) |
| Cistern (coastal) build | data not publicly available — get local contractor quotes |
| Cistern refill by tanker (Zagreb ViO area) | €101.80 delivery per 5 m³ household load + €6.37 water; 8 m³: €102.06 + €10.19; all prices incl. PDV (2026 data, source ViO Cjenik usluga from 1 Mar 2026) |

---

## Cost benchmarks (HR 2026, est. ranges — verify with local contractor quotes / current grant schedules; NPOO implementation ended 31 Aug 2026)

| Work | Cost (€) |
|---|---:|
| Energetski certifikat | 150–400 (est.; 2026 eMajstor contractor-offer aggregator ⚠️: indicative €106–€159 for a flat up to 50 m², €133–€286 for a house; 39 listed offers, from €90–€150 for renewing a 33.5 m² flat's certificate to €742.50–€1,237.50 for a 260 m² house) |
| Notary fee | €6 per certified signature; notarial deed €590 at a €100,000 price, €740 at €200,000; solemnisation half that (tariff point €2.00, arts 12, 16, 19, 40 — computed, see `--tax`) |
| RETT (resale) | 3% (ZPPN art. 12; 2026 data) |
| Realtor commission | est. 2–3% per side (market practice, no published statistic; no statutory cap — NN 69/26 art. 28) |
| **Total transaction cost (resale)** | **~5.0–6.6%** of a €100,000+ price (computed from the rows above; excl. lawyer and land-register fees) |
| **Total transaction cost (new build)** | 25% VAT included (no RETT) + est. ~0–3.6% other at a €100,000+ price (notary + any realtor, computed) |
| Roof renovation | 8,000–20,000 (est. for a ~100 m² roof; 2026 eMajstor aggregator ⚠️: replacing the covering with insulation €84–€104/m², i.e. €8,400–€10,400 per 100 m², computed; listed whole-roof replacement or new-roof offers (promjena / zamjena / izrada krova) for 80–135 m² €4,752–€23,100) |
| Asbestos abatement | 3,000–10,000 (est., 2026-04 research; no published price list — get contractor quotes) |
| Earthquake retrofit (older builds) | 25,000–80,000+ (est., 2026-04 research; no published cost survey — get a structural engineer's estimate) |
| Energy retrofit | 25,000–60,000 (est., 2026-04 research; calibration: the FZOEU 2024 family-house energy-renovation call EnU-1/24 capped eligible unit costs at €64/m² of external-wall insulation, €87/m² of pitched-roof insulation and €450/m² of replaced windows, and its grant at €62,120 per application (2024 data, source FZOEU — rates/figures may have changed since); get contractor quotes) |
| Karst soil study | 1,500–4,000 (est., 2026-04 research; no karst-specific price source located — 2026 eMajstor aggregator ⚠️ lists a standard geomechanical report for a family house at €240–€600 indicative, and listed offers at €360–€1,500 apart from one €2,475–€4,125 pipeline report; get a site quote) |
| Cistern installation | 2,000–8,000 (est.; 2026 eMajstor aggregator ⚠️: listed tank supply or install jobs €720–€7,500 (cleaning and repair jobs excluded), from a 1,000 L tank at €720–€3,000 (three jobs: €720–€1,200, €900–€1,500, €1,800–€3,000; a fourth, 1,000–2,000 L, at €2,700–€4,500) to a 30 m³ concrete tank at €4,500–€7,500) |

## Active fiscal incentives (2025-2026)

- **NPOO (Nacionalni plan oporavka i otpornosti 2021.–2026.)** — EU recovery funds that financed energy retrofit; implementation completed 31 Aug 2026 and the final (9th + 10th) payment request went to the Commission on 29 Sep 2026, so no new NPOO calls (2026 data, source planoporavka.gov.hr) — check the construction ministry and the environmental-protection and energy-efficiency fund for current retrofit grants
- **Petrinja reconstruction** subsidies (continuing)
- **First-home refund** — full RETT or 50% of VAT back for adult Croatian citizens under 45 (Zakon o priuštivom stanovanju, NN 45/26, arts 62–66; see `--tax`); foreign buyers cannot claim it

## Common listing platforms

- **Njuškalo** — general classifieds; self-reported 500,000+ visits a day, unaudited ⚠️ (see `--price`)
- **Index Oglasi** — general classifieds
- **Crozilla** + **Indomio.hr** — Indomio Group portals (group of Immobiliare.it and Spitogatos.gr)
- **Eurovilla, dogma-nekretnine** — agencies with their own listings, not portals

## Caveats unique to HR

- **NEW Porez na nekretnine 2025** — €0.60–€8/m²/yr (2026 data, source Porezna uprava); replaces the holiday-home tax (communal fee still levied separately); permanently lived-in homes and 10+-month long lets are exempt
- **Currency: EUR since 1 Jan 2023** — no FX risk for eurozone buyers
- **Dual register reconciliation** (cadastre vs ZK gruntovnica) — common HR pitfall
- **Earthquake risk CRITICAL**: Zagreb 2020 + Petrinja 2020; reconstruction ongoing
- **Karst hazards**: Dinaric coastal hinterland — sinkholes, drainage; no single risk register
- **Wildfire**: Adriatic critical Jul-Aug; DHMZ has applied the Canadian Fire Weather Index (CFFWIS) daily Apr–Oct since 1981 (source DHMZ presentation, WMO/EUMETSAT workshop, Budapest, 27 Apr 2017; verified 2026-10-23)
- **STR consent (since 1 Jan 2025)**: prior written consent of a two-thirds majority of co-owners plus every co-owner whose flat shares a wall, floor or ceiling with the let flat, given for at least 5 years and binding later owners — not 80% (Zakon o upravljanju i održavanju zgrada Art. 34; 2026 data, source zakon.hr consolidation through NN 110/26). A per-unit registration number is only proposed: new Zakon o ugostiteljskoj djelatnosti, P.Z.E. 315, first reading accepted by the Sabor 3 Jul 2026, planned entry into force 1 Jan 2027 (2026 data, source sabor.hr P.Z.E. 315)
- **~7,000 STR beds reported removed in one Dalmatian county** post-2025 reform (single secondary report — county/year unconfirmed)
- **Real estate transfer tax 3%** on resale; **VAT 25%** on new, with no RETT on a VAT-able purchase (2026 data, source ZPPN arts 5(2) + 12 / Porezna uprava)
- **Capital gains** on disposal within 2 years of acquisition taxed at a flat 24% (ZPD arts 58 + 62(3); 2026 data); untaxed after 2 years unless more than 3 same-type properties are sold within 5 years; exempt if it served as the seller's or dependent close family's residence (see `--tax`)
- **Reciprocity rule for non-EU buyers**: a foreign natural or legal person from outside the EU may buy only under reciprocity AND with the consent of the minister of justice (ZV art. 356(2); the consent is an administrative act); a contract without it is void (art. 357(1)), and after a refusal no new application for the same property for 5 years (art. 357(3)) (2026 data, source zakon.hr consolidation of the Zakon o vlasništvu i drugim stvarnim pravima). Nationalities listed as reciprocity-confirmed in the 2026-04 research (US, UK, AUS, JP, BRA, ARG, KOR, RUS, IL, CH, NO) are not re-checked against the ministry (Ministarstvo pravosuđa, uprave i digitalne transformacije) — confirm per nationality. **Pending**: ZV amendment NN 52/25 extends EU-equal treatment to EEA and OECD nationals from the day Croatia joins the OECD; not in force while Croatia remains an accession candidate (tertiary: en.wikipedia.org/wiki/OECD — confirm at oecd.org)
- **Non-reciprocity countries**: route is a Croatian-registered company — a legal person counts as foreign only if its registered seat is outside Croatia (ZV art. 355(3))
- **Agricultural land**: EU citizens can buy since July 2023 (moratorium ended); non-EU need special ministry approval
- **Agricultural land + protected parts of nature**: carved out of the EU equal-treatment rule (ZV art. 358.a(2); after OECD accession only agricultural land stays carved out), and no foreign person may own property in an area a law closes to foreigners (art. 358) — forest, pasture and coastal-zone parcels: check the land-use class on the cadastre / ZK extract and confirm eligibility with the ministry before an offer (per-category rules not re-verified)
- **Adriatic seafront premium**: 2-3× continental rates; up to €10,000/m² Old Town Dubrovnik (2025 asking-price data, listing platforms — secondary, seller-controlled; rates/figures may have changed since)
- **Etažno vlasništvo** (condominium) financial health critical
- **Petrinja reconstruction**: at 31 Dec 2025 all classic container settlements were closed and 3,315 people had been rehoused, but 1,197 mobile housing units still stood beside damaged houses across the Zagreb + Petrinja quake areas; when the rehousing programme was adopted (8 Feb 2023) 2,419 units housed 6,258 people (2025 data, source Government report on the Reconstruction Act to the Sabor, 7 May 2026)

## Reddit / forum sources

- **r/croatia** — biggest community
- **r/Zagreb**, **r/split**
- **Total Croatia News** (English)
- **Croatia Week** (English)
- **The Dubrovnik Times** (English)

## Verification authorities

| Authority | When to call |
|---|---|
| **OSS Uređena zemlja** | Cadastre + ZK reconciliation |
| **Katastarski ured** | Local cadastre |
| **Općinski sud (gruntovnica)** | Title verification |
| **Javni bilježnik** (notary) | Sale process |
| **Porezna uprava** | Porez na nekretnine + transfer tax |
| **County state-administration office** (Ured državne uprave / županijski ured; in Zagreb the Gradski ured za gospodarstvo) | Household STR approval (rješenje o odobrenju); the host then registers with Porezna uprava within 8 days and pays the tourist-board membership fee to the Turistička zajednica (2026 data, source Porezna uprava — Iznajmljivač turistima) |
| **Ministarstvo pravosuđa, uprave i digitalne transformacije** (`https://mpudt.gov.hr/`) | Non-EU buyer consent under reciprocity (Zakon o vlasništvu čl. 356–357; a refused buyer may not re-apply for the same property for 5 years). NN 52/25 extends EU-buyer treatment to EEA + OECD nationals from the day Croatia joins the OECD (čl. 358.a, per zakon.hr consolidation); Croatia was still an OECD accession candidate on 2026-10-23 (oecd.org) |

## Source URL templates

| Source | URL pattern |
|---|---|
| DGU Geoportal | `https://geoportal.dgu.hr/` |
| OSS Uređena zemlja | `https://oss.uredjenazemlja.hr/` |
| OSS — land register + cadastre (ex-katastar.hr) | `https://oss.uredjenazemlja.hr/` |
| Porezna uprava | `https://porezna-uprava.gov.hr/` |
| DZS | `https://podaci.dzs.hr/` |
| Njuškalo | `https://www.njuskalo.hr/nekretnine/` |
| DHMZ | `https://meteo.hr/` |
| HGI-CGS | `https://www.hgi-cgs.hr/en/` |
| Seizmološka služba | `https://www.pmf.unizg.hr/geof/en/seismological_survey` |
| eEnergetski certifikat | `https://eenergetskicertifikat.mpgi.hr/` |
| Hrvatske vode | `https://www.voda.hr/` |
| Hrvatske vode flood hazard / risk maps | `https://preglednik.voda.hr/` |
| HC traffic counts (PGDP / PLDP) | `https://hrvatske-ceste.hr/hr/stranice/promet-i-sigurnost/dokumenti/14-brojenje-prometa` |
| DHMZ fire-weather index | `https://meteo.hr/podaci.php?section=podaci_agro&param=pozarind` |
| ViO Zagreb water tariffs | `https://www.vio.hr/usluge/cjenik-vodnih-usluga/1517` |

## Status

✅ Fast-changing sections re-verified as of 2026-10-23; each section's date is in the Per-section verification table.

✅ **Fully populated** as of 2026-04-25 (cadastre access route and extract fee corrected 2026-09-18 per gov.hr). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (DZS transaction data + HNB; Njuškalo asking prices are secondary listing data), traffic (HC PGDP + PLDP), tax (Porez na nekretnine €0.60–€8/m² + 3% RETT + 25% VAT new + capital gains), rental (two-thirds + adjoining-owner STR consent; per-bed paušal), work, risks (earthquake CRITICAL Zagreb 2020 + Petrinja 2020 + wildfire + karst), mains — primary government sources, except the asking-price rows (listing platforms) and the est. cost ranges.
**Confidence**: HIGH for Porez na nekretnine amounts (Porezna uprava 2025/2026 comparison table covering all 556 JLS); HIGH for the STR consent rule (two-thirds of co-owners + every adjoining owner, Zakon o upravljanju i održavanju zgrada Art. 34) and for the per-unit registration number being a bill only (P.Z.E. 315); HIGH for 2020 earthquake reference + Petrinja reconstruction status (Government report to the Sabor, 31 Dec 2025 data); HIGH for currency EUR transition (1 Jan 2023). HIGH for `--work` and the climate projections (all material numbers re-verified 2026-10-23). HIGH for `--price` (DZS H1 2026 and Q2 2026 releases plus MPGI 2025 recorded sale medians by county and city; the Njuškalo asking figures are labelled listing-platform data) and `--rental` (long-let rules from the Zakon o najmu stanova, STR rules from the consolidated acts; contract length stated as not publicly available, the ~7,000-bed report labelled anecdotal). MEDIUM for `--tax` (the realtor commission is an est. 2–3% per side, so both buyer-side totals carry an estimated share; the 30-day permit target and the criminalisation announcement are news-tier), `--traffic` (HC 2025 counts; the Zagreb-ring example not re-checked), `--risks` (hazard comparisons are PMF hazard-map readings at town-centre coordinates, not parcel values; the 2014 flood breaches and the asbestos patent date are secondary; two build-era rows are curated heuristics) and `--mains` (connection duties from the Zakon o vodnim uslugama; operator-published rules and rates, each for one service area only; septic and cistern build costs not publicly available). LOW for the non-EU reciprocity country list (not re-checked against the ministry since the 2026-04 research), the Petrinja subsidy status and the est. contractor ranges in Cost benchmarks.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--tax` | 2026-10-23 | 2026-11-05 maintenance run | The 2026 amounts for Zagreb, Split, Rijeka, Osijek, Dubrovnik, the Hvar-island municipalities, Sveti Filip i Jakov and Tisno match Porezna uprava's 2025/2026 comparison table. Zagreb's €8 from 1 Jan 2027 is confirmed in the decision text in Službeni glasnik Grada Zagreba 32/2026. |
| `--rental` | 2026-10-23 | 2026-11-05 maintenance run | The registration-number bill (P.Z.E. 315) and the per-bed tax bill (P.Z. 339) match the Sabor bill texts and vote records. Sabor shows no final vote on P.Z.E. 315, and no act amending the income tax law appears in Narodne novine up to issue 127 of 4 Nov 2026. |
| `--work=<profession>` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--risks` | 2026-10-23 | 2026-11-05 maintenance run | The 2014 flood account matches the recovery act in Narodne novine 77/14 and, as a secondary source, Wikipedia, and Hrvatske vode's flood-map page links to the viewer. Art. 158 of the Zakon o gradnji (zakon.hr consolidated text) keeps the structural technical regulation in force. |
| `--mains` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (HR 2026, est. ranges — verify with local contractor quotes / current grant schedules; NPOO implementation ended 31 Aug 2026) | 2026-10-23 | 2026-11-05 maintenance run | The cistern line now gives the eMajstor aggregator's full spread for a 1,000 L tank, €720–€3,000 across three listed offers, and scopes the overall €720–€7,500 span to supply-and-install jobs. |

## Extension TODOs

- [ ] Per-municipality Porez na nekretnine rates table
- [ ] Petrinja reconstruction status + grants
- [ ] Adriatic vs continental price multiple by region
- [ ] Karst hazard zone overlay (HGI-CGS)
- [ ] STR consent decision tree (two-thirds of co-owners + every adjoining owner, Zakon o upravljanju i održavanju zgrada Art. 34)
- [ ] Non-EU buyer reciprocity verification per nationality
- [ ] Wildfire vulnerability per island
- [ ] Cadastre-vs-ZK reconciliation flow
- [ ] Earthquake retrofit cost estimator (post-2020 reforms)
- [ ] EC8 compliance for new builds

## Update history

- **2026-04-25** — Initial population (2026-04 research)
- **2026-09-18** — Cadastre access route and extract fee corrected per gov.hr
- **2026-09-24** — Tax tracker entries re-checked (November regwatch wave, run early)
- **2026-10-21** — Tax tracker entry re-checked (December regwatch wave, run early)
- **2026-10-23** — Refresh wave; playbook-level date not re-stamped: `--tax`, `--risks`, `--mains` and Cost benchmarks were patched in the gap-closing pass but remain open, while `--price` and `--rental` (with Common listing platforms) were closed by it and `--work` was re-verified in the refresh. Changed / confirmed / unverifiable per section: Country profile 1 / 3 / 0; `--price` 2 / 1 / 14; `--rental` 7 / 2 / 3; `--work` 7 / 2 / 2 (all material numbers re-verified); `--tax` 24 / 22 / 8; Cost benchmarks 3 / 2 / 8; Active fiscal incentives 2 / 0 / 1; Caveats 3 / 4 / 3 from the tax-legal check (foreign-buyer lines counted here) + 4 lines corrected or relabelled (wildfire index start year, STR consent, seafront asking-price label, Petrinja temporary housing); `--traffic` 5 / 1 / 2; `--risks` 13 / 2 / 6; climate projections 3 / 2 / 0 (re-verified); `--mains` 1 / 1 / 3; Verification authorities 1 / 0 / 2 + the STR approval row corrected; Source URL templates 1 / 10 / 1 (liveness only, 4 rows added); Common listing platforms 0 / 0 / 3; Reddit / forum sources 0 / 2 / 4. Main changes: capital-gains holding period 2 years, not 10; Split porez na nekretnine €1.99 (2025) → €5 (2026) and other per-JLS amounts from the Porezna uprava comparison table; STR consent is two-thirds of co-owners plus every adjoining owner, not 80%, and the per-unit registration number is a bill (P.Z.E. 315, planned from 1 Jan 2027); long-let tax and the per-bed paušal replace the 8% / 10% lines, with P.Z. 339 noted as proposed; first-home refund re-pointed to NN 45/26; NPOO closure noted; DZS new-flat prices (H1 2026) and house price index (Q2 2026) added and the asking-price rows relabelled secondary; 2026 wages and minimum wage; quake history, build-era and energy-certificate dates corrected; CFFWIS start year 1981; Petrinja status from the Government's 2025 report; climate projections from NN 46/2020; nationwide criminalisation of illegal building marked not enacted
  - Gap-closing pass (confirmed / changed / relabelled; sources read to 2026-11-03): `--price` 1 / 11 / 4, `--rental` 4 / 2 / 1 and Common listing platforms 0 / 1 / 0 — closed; `--tax` 6 / 5 / 2 plus 2 lead fixes, Cost benchmarks 0 / 2 / 9, `--risks` 4 / 5 / 6 and `--mains` 0 / 1 / 1 — patched, still open; total 15 / 27 / 23 plus 2 lead fixes. Main changes: each asking-price row paired with the MPGI 2025 recorded sale median, the Njuškalo 2025 asking figures checked against its 20 Feb 2026 release (Slavonia row and Split's "fastest growth" corrected) and the Adriatic multiple recomputed (1.4–3.1×); Indomio.hr and Crozilla are Indomio Group portals, not REA Group, and Njuškalo's traffic is self-reported; long-let rules sourced to the Zakon o najmu stanova, and the P.Z.E. 315 final bill would start the registration number on 1 May 2027; Zagreb's €8 from 1 Jan 2027 re-sourced to Službeni glasnik Grada Zagreba 32/2026; notary fees computed from the notary tariff and the buyer-side totals recomputed with them (resale ~5.0–6.6%, realtor share est.); the €4,000 / €15,000 amounts are the Zakon o gradnji posebna naknada (NN 155/25 art. 72(2)), not fines; "VAT may rise" replaced by the enacted position; contractor cost rows calibrated against eMajstor offers or labelled unsourced est., with the FZOEU EnU-1/24 unit-cost caps added; PMF hazard-map readings replace the unsourced Zagreb-fault and Slavonia ranking, the karst, notarial-deed and post-2020 reconstruction rows corrected, the 2024 national fire totals taken from HVZ (3,892 fires, 23,410 ha) and the unconfirmed Zagreb 2014 flood removed; `--mains` est. ranges replaced by Zakon o vodnim uslugama connection duties and operator-published rules and rates
- **2026-11-04** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`; still open Cost benchmarks (HR 2026, est. ranges — verify with local contractor quotes / current grant schedules; NPOO implementation ended 31 Aug 2026).
- **2026-11-05** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (HR 2026, est. ranges — verify with local contractor quotes / current grant schedules; NPOO implementation ended 31 Aug 2026). Playbook-level date now 2026-10-23.
