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
- **Croatia Week property reports** + **Bilten nekretnina** (Eurofast)

### Listing platforms

- **Njuškalo** — DOMINANT (~500k daily visits): `https://www.njuskalo.hr`
- **Index Oglasnik** — #2: `https://www.index.hr/oglasi`
- **Crozilla** — coastal specialist: `https://www.crozilla.com`
- **Indomio.hr** (REA Group): rising specialist
- **Eurovilla.hr, dogma-nekretnine.com** — niche

### Price benchmarks

**Transaction data (primary — DZS)**:
- **New flats sold, H1 2026**: €2,994/m² national, €3,518/m² Zagreb, €2,754/m² other settlements; +8.7% YoY national, +18.9% YoY Zagreb (2026 data, source DZS GRAD-2026-4-1/1, 7 Sep 2026)
- **House price index, Q2 2026 (provisional)**: +12.7% YoY national; Grad Zagreb +15.7%, Jadran (Adriatic) +9.0%, Ostalo (rest of country) +15.8%; new dwellings +9.2%, existing +14.1% (2026 data, source DZS CIJ-2026-2-1/2, 1 Oct 2026)

**Asking prices** (listing platforms — secondary, seller-controlled; 2025 data, source Njuškalo — rates/figures may have changed since):

| Region | Avg €/m² (apt asking) | Trend |
|---|---:|---|
| **Zagreb** (capital) | 3,000–3,698 | rising |
| **Split** | 5,183 | **+13.85% YoY** (fastest growth) |
| **Dubrovnik** | 4,150–6,967 (standard); **prime seafront/Old Town up to 10,000** | high tourist premium |
| **Rijeka** | 2,800–3,500 | rising |
| **Pula** (Istria) | 3,283 | rising |
| **Zadar** | 3,500–4,200 | rising |
| **Šibenik** | 2,800–3,800 | rising |
| **Coastal islands (Hvar, Brač, Korčula)** | 4,500–8,000+ | premium |
| **Continental (Slavonia)** | 700–1,200 | flat/declining |
| **National avg asking** | 3,636 (+6.5% YoY) | |

### Compute

1. €/m² = price / **uporabna površina** (usable area)
2. Cross-check **OSS Uređena zemlja** for cadastre/ZK reconciliation
3. **HR dual register pitfall**: cadastre says one thing, ZK gruntovnica says another — common; must reconcile
4. **Adriatic premium**: factor 2-3× over continental
5. **Seafront/Old Town Dubrovnik**: up to €10,000/m²

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

**MAJOR REFORM 1 January 2025**: replaces the previous holiday-home tax (porez na kuće za odmor); the communal fee (komunalna naknada) continues to be levied separately (2026 data, source Porezna uprava).

#### Rate range

- **€0.60–€8.00/m²** of usable area per year; €0.60 applies where the grad / općina adopts no decision (ZLP art. 26 as amended by NN 152/24; 2026 data, source Narodne novine + Porezna uprava)
- Set by each municipality within range
- **Highest amount (€8 across the whole territory, 2026)**: 11 JLS — Umag, Fažana, Sveti Filip i Jakov, Biograd na Moru, Mali Lošinj, Nin, Lopar, Privlaka (ZD), Sutivan, Vir, Vrsi; Okrug, Opatija, Punat, Stari Grad and Vodnjan reach €8 in some zones only. Vis (to €6) and Baška Voda (to €3) cut their €8 amount for 2026 (2026 data, source Porezna uprava comparison table 2025/2026)
- **Major cities (2026)**: Zagreb €5 (€8 from 1 Jan 2027 — Gradska skupština vote 16 Oct 2026, news-tier via Hina; verify publication in the Službeni glasnik Grada Zagreba), Split €5 (€1.99 in 2025), Rijeka €5, Osijek €0.60, Dubrovnik zoned €0.60–€5.00 (2026 data, source Porezna uprava comparison table 2025/2026)
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
- **PDV** (VAT): **25%** on new builds first sale (standard rate 25%; reduced rates 13% and 5% — 2026 data, source Porezna uprava)
- **Javni bilježnik** (notary): ~0.5–1.5% (est. — notary fees are set by the Pravilnik o privremenoj javnobilježničkoj tarifi (2026 data, source HJK); the % range is not taken from the tariff, so get the notary's quote)
- **Realtor commission**: 2–3% per side
- **First-home refund (contracts from 1 Jan 2025)** — since 7 May 2026 under the Zakon o priuštivom stanovanju (NN 45/26 of 29 Apr 2026, arts 62–66; in force on the 8th day after publication, computed), which replaced the Zakon o društveno poticanoj stanogradnji (arts 30.c–30.f added by NN 72/25; Pravilnik NN 86/25): refund of the full RETT paid on a resale (capped at 3% of the statutory base) OR 50% of the VAT paid on a new build (capped at 12.5% of the base). **Adult Croatian citizens only** — foreign buyers, EU nationals included, cannot claim it. Under 45 at application; price per m² not more than 50% above the local average and usable area not more than 50% above the recognised area (50 m² for one person up to 120 m² for 7+); apply to **APN** within **24 months** of acquiring ownership; repay with default interest if sold, let, prebivalište deregistered or not lived in within 5 years of payment (2026 data, source Narodne novine NN 45/26). No-prior-ownership rule (applicant and close family must not own or have owned a suitable home) is from art. 30.c NN 72/25 — confirm its NN 45/26 wording

### Capital gains

- **Disposal within 2 years** of acquisition (or of the building becoming fit for use, if built, reconstructed or converted): gain taxed at a flat **24%** porez na dohodak, assessed by Porezna uprava decision and payable within 15 days; gain = market-value proceeds − acquisition cost uplifted by industrial producer-price growth − documented improvement and sale costs (ZPD arts 58(1)–(2) + 62(3), as amended to NN 152/24; 2026 data, source zakon.hr consolidation through NN 110/26)
- **Not taxed after 2 years** — except where more than 3 properties of the same type are sold within 5 years of acquisition: the combined gain is then taxed at 24% (each flat, business unit or land parcel counts as one property; art. 58(3) + 62(4))
- **Exempt at any holding period**: a home that served as the residence of the seller or dependent close family (a registered prebivalište alone is not proof), expropriation, transfers between spouses / first-line relatives / close family or on divorce, and disposals directly linked to inheritance (art. 58(4)–(5))

### Total transaction cost (buyer side)

- Resale: ~5.5–7.5% (computed: 3% RETT + est. 0.5–1.5% notary + est. 2–3% buyer-side realtor)
- New build: 25% VAT in price (no RETT where VAT is charged — ZPPN art. 5(2)) + ~3% other costs (est.)

### Future risk

- Porez na nekretnine: municipalities keep recalibrating — for 2026, 41 JLS raised and 12 lowered their amount (2026 data, source Porezna uprava); Zagreb goes from €5 to €8/m² on 1 Jan 2027 (adopted 16 Oct 2026, news-tier)
- VAT may rise post-eurozone integration
- **Construction-law package (in force 1 Jan 2026)**: Sabor adopted the Zakon o prostornom uređenju, Zakon o gradnji and Zakon o energetskoj učinkovitosti u zgradarstvu on 15 Dec 2025, all in force 1 Jan 2026, with a 30-day building-permit target (2025 data, source Hina via informator.hr, 29 Dec 2025). **Criminal liability** for illegal building still covers only protected nature areas, cultural heritage and other areas of special state interest — 6 months to 5 years' prison (Kazneni zakon art. 212; the zakon.hr consolidation through NN 110/26 of 20 Oct 2026 lists no 2026 amendment). Wider criminalisation of building without a permit, through Kazneni zakon amendments, was announced by minister Bačić in Jan 2026 (Novi list, 15 Jan 2026, news-tier) and is not enacted in that consolidation. Fines for starting work without a permit — €4,000 (less complex buildings) to €15,000 (multi-unit) — are reported as set by the new Zakon o gradnji (Novi list, 15 Jan 2026, news-tier; not verified in the Zakon o gradnji text). **Legalizacija** (Zakon o postupanju s nezakonito izgrađenim zgradama, amended by NN 48/26 — adopted 30 Apr 2026, published 8 May 2026): a request needs proof that the building is visible on the 21 Jun 2011 DGU orthophoto or was recorded on the cadastral plan or another official map by that date (art. 11(1) as amended), and the amended art. 10 sets no filing deadline, so the old 30 Jun 2018 cut-off no longer applies (2026 data, source zakon.hr text of NN 48/26; 2018 cut-off per Novi list, 15 Jan 2026)
- **Pomorsko dobro** (Maritime Domain) is statutory **inalienable public good** under Zakon o pomorskom dobru i morskim lukama (land strip at least 6 m wide measured from the line of mean higher high water + territorial sea/seabed; out of legal commerce, no ownership or other real right can be acquired — NN 83/23 arts 4(1), 5(1), 6(3), source Narodne novine). Cannot be owned by anyone (HR or foreign) — only concessions available. Seafront listings promising "beach ownership" are selling something legally non-ownable.

---

## Section: `--rental`

### Long-term residential

- **Zakon o najmu stanova** (Tenancy Act) — moderate tenant protection
- Standard 1-3 yr contracts
- Rent control limited

### Short-let — MAJOR 2025 CRACKDOWN

**Zakon o upravljanju i održavanju zgrada** (NN 152/24, 47/26; in force 1 Jan 2025) + **Zakon o ugostiteljskoj djelatnosti** amendment (NN 152/24):
- **Two-thirds co-owner consent** (prior, written) required to let a flat short-term in a multi-unit building (Art. 34); the MPGI model consent decision counts co-owners holding more than 66% of the total floor area of all special parts. The enacted text has no 80% threshold (2026 data, source Narodne novine NN 152/24 + zakon.hr consolidated text + mpgi.gov.hr model decision)
- **Plus consent of every owner of an adjoining flat** (sharing walls/floors/ceilings); consent runs for a fixed term of at least 5 years, binds later owners, and can be revoked by simple majority after 3+ house-rule breaches within 2 years (Art. 34)
- Flats already let short-term on 1 Jan 2025 must collect the consent within 5 years (Art. 63(2)); the household-accommodation approval requires it (Zakon o ugostiteljskoj djelatnosti Art. 34(2) point 4)
- **Registration number — PROPOSED, not in force**: the new Zakon o ugostiteljskoj djelatnosti (P.Z.E. 315; Sabor accepted the first reading 3 Jul 2026, 78 for / 14 against / 37 abstentions) implements Regulation (EU) 2024/1028 — one registration number per accommodation unit, requested through the integrated tourism information system and shown in every platform listing; planned entry into force 1 Jan 2027 (2026 data, source sabor.hr P.Z.E. 315 bill text). The consolidated act in force (NN 85/15 … 152/24, source zakon.hr) has no unit registration number
- **Result**: ~7,000 STR beds reported removed in one Dalmatian county (single secondary report — county/year unconfirmed); Adriatic supply contracting

#### Categories

_Approval (rješenje) and categorisation are issued by the county administrative office (in Zagreb, the Gradski ured za gospodarstvo), not by the Turistička zajednica (2026 data, source Porezna uprava — Iznajmljivač turistima)._

- **Apartman** (apartment)
- **Soba** (room)
- **Studio apartman** (studio)
- **Kuća za odmor** (holiday house)

#### Tax

- **Long-term letting** (porez na dohodak od imovine): **12%** on rent less a flat **30%** expense allowance = 8.4% of gross rent (computed 0.12 × 0.70) (2026 data, source Porezna uprava — Najmodavac stambenog prostora)
- **Tourist letting in a household** (owner-let, max 20 beds or 10 camp units, outside VAT): no % income tax — an annual **paušalni porez per bed** (tax = beds × per-bed amount), set by the local council by 15 Dec for the next year within ranges by tourism-development category (ITR): Cat I €100–300 (€200 if no decision), Cat II €70–200 (€135), Cat III €30–150 (€90), Cat IV/0 €20–100 (€60); paid quarterly (2026 data, source Porezna uprava — Iznajmljivač turistima)
- **PROPOSED from 1 Jan 2027, not adopted**: Government bill P.Z. 339 (sent to Sabor 10 Sep 2026; ZPD still cited as NN 115/16 … 152/24 in Narodne novine 120/2026 of 21 Oct 2026) raises Cat I to €150–300 (default €225) and Cat II to €100–200 (default €150); Cat III and IV/0 unchanged; councils whose current amount falls outside the new range must adopt and file a new decision by 1 Mar 2027, otherwise the default applies (bill Arts 4, 13, 16; source sabor.hr P.Z. 339) — verify the enacted text in Narodne novine
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

- **Zagreb fault zone**: highest hazard in continental HR
- **22 March 2020 Zagreb (ML 5.5; USGS Mww 5.3)** — major damage (source MPGI seismic-data manual, 2023 + USGS)
- **29 December 2020 Petrinja (ML 6.2 / Mw 6.4, PMF Geofizički odsjek)** — epicentre ~48 km SE of central Zagreb (computed from the USGS epicentre 45.42 N 16.26 E); **still under reconstruction**: at 31 Dec 2025 works were finished on 14,284 buildings and under way on 1,949 across the Zagreb + Petrinja quake areas (1,245 structural renovations, 206 replacement houses, 15 multi-apartment buildings); 1,197 mobile housing units still stood beside damaged houses, while all classic container settlements were closed (2025 data, source Government report on the Reconstruction Act to the Sabor, 7 May 2026)
- **PGA hazard maps** (Karta potresnih područja RH 2011, PMF Geofizički odsjek; part of HRN EN 1998-1:2011/NA:2011) for 95- and 475-year return periods on ground type A (bedrock), with 225-yr values in the PMF reader app; e.g. central Zagreb (Frankopanska / Ilica) agR 0.256 g at 475 yr and 0.129 g at 95 yr — local soil layers can amplify these (2011 maps, source MPGI seismic-data manual, 2023 — rates/figures may have changed since)
- **Slavonia** (E HR): lower risk
- **Coastal Adriatic**: variable — strongest documented: Great Dubrovnik earthquake of 6 Apr 1667 (ML 7.1, estimated from intensity IX–X °MCS), Trilj 1898 (ML 6.7, estimated), Imotski 1942 (ML 6.2), Makarska 1962 (ML 6.1), Ston-Slano 5 Sep 1996 (ML 6.0) (source MPGI seismic-data manual, 2023); the 15 Apr 1979 M6.9 (Ms) earthquake had its epicentre in Montenegro, 6 km E of Stari Bar, not in Croatia (USGS ISC-GEM)

#### Wildfire

- **Adriatic / Dalmatia coast**: critical fire zone
- **DHMZ CFFWIS** (Canadian Forest Fire Weather Index System) since 1981, computed daily Apr–Oct (DHMZ, WMO/EUMETSAT 2017 presentation)
- **2024 (national)**: 3,825 vegetation fires, +29% vs 2023; 26,807 ha burnt (2024 data, source DVOC 193 figures via tportal, 3 Jan 2025 — secondary)
- **2025 (coastal + karst area)**: 2,821 vegetation fires, −10.2% vs the prior 5-yr average; 6,094 ha burnt, −70.1% (2025 data, source HVZ Program aktivnosti presentation, Feb 2026)
- Pinewood resin = high fire intensity
- Ferry-route disruption common Jul-Aug

#### Karst hazards

- **Dinaric karst**: sinkholes, doline, cave drainage
- **Coastal hinterland Adriatic** + Lika + Gorski Kotar
- **HGI-CGS** publishes geological maps
- No single statutory sinkhole risk register
- Construction on karst requires soil study

#### Other risks

- **Coastal storm + sea-level rise**: Adriatic
- **Flood**: inland Sava, Drava, Una — May 2014: Sava embankment breached at Rajevo Selo / Račinovci (southern Slavonia, Gunja evacuated) and Una flooding in Hrvatska Kostajnica / Dvor (secondary — Wikipedia, 2014 Southeast Europe floods); a Zagreb 2014 flood event is unconfirmed
- **Bura (Adriatic strong NE wind)** — winter storms
- **Hrvatske vode** (`https://www.voda.hr/`) — flood hazard + flood risk map viewer (2019 cycle) at `https://preglednik.voda.hr/`

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **1900–1990 (Yugoslav era)** | Asbestos common, Yugoslav-era panel buildings (Novi Zagreb) |
| **1981–2012** | PBAB 81 seismic rulebook (Pravilnik o tehničkim normativima za izgradnju objekata visokogradnje u seizmičkim područjima); its intensity-based seismic map stayed the HR design basis until 2012. Yugoslav seismic design duties began after the 1963 Skopje quake (source MPGI seismic-data manual, 2023) |
| **Post-2012 EC8** | Modern seismic — HRN EN 1998-1:2011/NA:2011 with the 2011 PGA hazard maps (source MPGI seismic-data manual, 2023) |
| **Post-2020 Zagreb earthquake** | Reconstruction with EC8 mandatory |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetski certifikat** | Required before sale, rental or lease, and the energy class must appear in ads; exemptions incl. freestanding buildings < 50 m² and homes used < 4 months/yr (gov.hr, verified 2026-10-23). Sale duty since 1 Jul 2013, rental since 1 Jan 2016 (Pravilnik amendment NN 78/13) | 10 years from issue (gov.hr, verified 2026-10-23) |
| **Javnobilježnička isprava** | Notarial deed | At sale |
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
- Coastal islands: often septic / cisterns

### Costs

_Est. ranges — vary by municipal vodovod tariff; confirm with local Vodovod i kanalizacija._

| Scenario | Cost (€) |
|---|---:|
| Mains connection | ~€3,000–€8,000 |
| Septic upgrade | ~€4,000–€10,000 |
| Cistern (coastal) | ~€2,000–€8,000 |

---

## Cost benchmarks (HR 2026, est. ranges — verify with local contractor quotes / current grant schedules; NPOO implementation ended 31 Aug 2026)

| Work | Cost (€) |
|---|---:|
| Energetski certifikat | 150–400 |
| Notary fee | 0.5–1.5% of price (est.; fees follow the HJK tariff — get a quote) |
| RETT (resale) | 3% (ZPPN art. 12; 2026 data) |
| Realtor commission | 2–3% per side |
| **Total transaction cost (resale)** | **~5.5–7.5%** of price (computed from the rows above) |
| **Total transaction cost (new build)** | 25% VAT included (no RETT) + ~3% other |
| Roof renovation | 8,000–20,000 |
| Asbestos abatement | 3,000–10,000 |
| Earthquake retrofit (older builds) | 25,000–80,000+ |
| Energy retrofit | 25,000–60,000 |
| Karst soil study | 1,500–4,000 |
| Cistern installation | 2,000–8,000 |

## Active fiscal incentives (2025-2026)

- **NPOO (Nacionalni plan oporavka i otpornosti 2021.–2026.)** — EU recovery funds that financed energy retrofit; implementation completed 31 Aug 2026 and the final (9th + 10th) payment request went to the Commission on 29 Sep 2026, so no new NPOO calls (2026 data, source planoporavka.gov.hr) — check the construction ministry and the environmental-protection and energy-efficiency fund for current retrofit grants
- **Petrinja reconstruction** subsidies (continuing)
- **First-home refund** — full RETT or 50% of VAT back for adult Croatian citizens under 45 (Zakon o priuštivom stanovanju, NN 45/26, arts 62–66; see `--tax`); foreign buyers cannot claim it

## Common listing platforms

- **Njuškalo** — DOMINANT
- **Index Oglasnik** — secondary
- **Crozilla** — coastal specialist
- **Indomio.hr** — REA Group entrant
- **Eurovilla, dogma-nekretnine** — niche

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

✅ **Fully populated** as of 2026-04-25 (cadastre access route and extract fee corrected 2026-09-18 per gov.hr). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (DZS transaction data + HNB; Njuškalo asking prices are secondary listing data), traffic (HC PGDP + PLDP), tax (Porez na nekretnine €0.60–€8/m² + 3% RETT + 25% VAT new + capital gains), rental (two-thirds + adjoining-owner STR consent; per-bed paušal), work, risks (earthquake CRITICAL Zagreb 2020 + Petrinja 2020 + wildfire + karst), mains — primary government sources, except the asking-price rows (listing platforms) and the est. cost ranges.
**Confidence**: HIGH for Porez na nekretnine amounts (Porezna uprava 2025/2026 comparison table covering all 556 JLS); HIGH for the STR consent rule (two-thirds of co-owners + every adjoining owner, Zakon o upravljanju i održavanju zgrada Art. 34) and for the per-unit registration number being a bill only (P.Z.E. 315); HIGH for 2020 earthquake reference + Petrinja reconstruction status (Government report to the Sabor, 31 Dec 2025 data); HIGH for currency EUR transition (1 Jan 2023). HIGH for `--work` and the climate projections (all material numbers re-verified 2026-10-23). MEDIUM for `--price` (DZS transaction data current; the asking-price rows are 2025 listing data), `--rental` (long-let practice lines and the ~7,000-bed caveat not re-checked), `--tax` (notary %, realtor % and new-build other costs are estimates), `--traffic` (HC 2025 counts; the Zagreb-ring example not re-checked) and `--risks` (Zagreb-fault and Slavonia ranking, karst rules and the notarial-deed row not re-checked). LOW for the non-EU reciprocity country list (not re-checked against the ministry since the 2026-04 research), the Petrinja subsidy status and the est. ranges in `--mains` and Cost benchmarks.

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
- **2026-10-23** — Refresh wave; playbook-level date not re-stamped because `--price`, `--tax` and `--rental` still carry unverified rows. Changed / confirmed / unverifiable per section: Country profile 1 / 3 / 0; `--price` 2 / 1 / 14; `--rental` 7 / 2 / 3; `--work` 7 / 2 / 2 (all material numbers re-verified); `--tax` 24 / 22 / 8; Cost benchmarks 3 / 2 / 8; Active fiscal incentives 2 / 0 / 1; Caveats 3 / 4 / 3 from the tax-legal check (foreign-buyer lines counted here) + 4 lines corrected or relabelled (wildfire index start year, STR consent, seafront asking-price label, Petrinja temporary housing); `--traffic` 5 / 1 / 2; `--risks` 13 / 2 / 6; climate projections 3 / 2 / 0 (re-verified); `--mains` 1 / 1 / 3; Verification authorities 1 / 0 / 2 + the STR approval row corrected; Source URL templates 1 / 10 / 1 (liveness only, 4 rows added); Common listing platforms 0 / 0 / 3; Reddit / forum sources 0 / 2 / 4. Main changes: capital-gains holding period 2 years, not 10; Split porez na nekretnine €1.99 (2025) → €5 (2026) and other per-JLS amounts from the Porezna uprava comparison table; STR consent is two-thirds of co-owners plus every adjoining owner, not 80%, and the per-unit registration number is a bill (P.Z.E. 315, planned from 1 Jan 2027); long-let tax and the per-bed paušal replace the 8% / 10% lines, with P.Z. 339 noted as proposed; first-home refund re-pointed to NN 45/26; NPOO closure noted; DZS new-flat prices (H1 2026) and house price index (Q2 2026) added and the asking-price rows relabelled secondary; 2026 wages and minimum wage; quake history, build-era and energy-certificate dates corrected; CFFWIS start year 1981; Petrinja status from the Government's 2025 report; climate projections from NN 46/2020; nationwide criminalisation of illegal building marked not enacted
