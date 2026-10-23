# Belgium 🇧🇪 — Property Due-Diligence Playbook

ISO2: `be`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1000` Bruxelles, `2000` Antwerpen, `4000` Liège, `8000` Brugge)
- **Admin levels**: 3 régions (Wallonie, Vlaanderen, Bruxelles-Capitale) + 10 provinces + 565 communes (581 until 31 Dec 2024; Bastogne + Bertogne merged on 2 Dec 2024 and 28 Flemish communes on 1 Jan 2025; Statbel publishes figures for the merged communes from reference period 1 Jan 2025) (2025 data, source Statbel 'Découpages géographiques')
- **Currency**: EUR (€)
- **Languages**: French (Wallonie), Dutch (Vlaanderen), German (Eastern Cantons), bilingual (Bruxelles)
- **Significant regional autonomy** on housing/tax/environment — three different regimes for almost everything
- **Cadastre**: **AGDP / FOD Financiën** (federal) + regional registers
- **Identifier**: kadastraal nummer / matricule cadastral (`<commune> <section> <numéro>`)
- **Ownership types**: **pleine propriété** (freehold), **emphytéose** (long lease), **superficie** (right to build), **VME / co-propriété** (apartment)

## Section: `--price`

### Primary sources

- **STATBEL** (Belgian statistics): `https://statbel.fgov.be/en/themes/housing/real-estate` — median sale prices from deeds registered by FPS Finances (resale only, new builds excluded), per quarter / semester / year down to municipality; beSTAT tables give per-municipality medians and quartiles (2026 data, source Statbel real-estate page)
- **Notaires.be / Notaris.be** — sale-price barometer: `https://www.notaire.be/` / `https://www.notaris.be/`
  - Quarterly **Baromètre immobilier** (Fednot) — regional and provincial **average** prices, new and existing stock, so not comparable with Statbel medians; latest release covers the first nine months of 2026, published 13 Oct 2026 (2026 data, source notaire.be)
- **CIB Vlaanderen** + **Federia** + **Beroepsinstituut van Vastgoedmakelaars (BIV)** — agent body data
- **Cadastre** (FOD Financiën): `https://finances.belgium.be/fr/particuliers/habitation/cadastre`

### Listing platforms

- **Immoweb** — DOMINANT: `https://www.immoweb.be`
- **Zimmo**: `https://www.zimmo.be/` — absorbed **Logic-Immo.be** in June 2023; `logic-immo.be` now redirects to Zimmo (per Zimmo's own page, platform tier; redirect checked 2026-10-23)
- **Realo**: `https://www.realo.be/`
- **Immovlan** (FR/NL): `https://immovlan.be/` — the property portal linked from Vlan; `vlan.be` now redirects to a Sudinfo newspaper section (checked 2026-10-23)
- Agency networks: **Era**, **Century 21**, **Engel & Völkers**

### Price benchmarks — Statbel median sale prices, H1 2026

| Area | Median apartment (€) | Median house, 2-3 façades (€) |
|---|---:|---:|
| **Belgium** | 257,000 | 285,000 |
| **Brussels-Capital Region** | 275,000 | 550,000 |
| **Flemish Region** | 268,000 | 325,000 |
| **Walloon Region** | 195,000 | 195,000 |
| **Prov. Antwerp** (Antwerpen) | 268,000 | 365,000 |
| **Prov. East Flanders** (Gent) | 270,000 | 319,500 |
| **Prov. Flemish Brabant** (Leuven, Brussels periphery) | 295,000 | 378,500 |
| **Prov. West Flanders** (Brugge, coast) | 255,000 | 277,250 |
| **Prov. Limburg** (Hasselt) | 250,000 | 282,750 |
| **Prov. Walloon Brabant** | 270,000 | 355,000 |
| **Prov. Liège** | 185,000 | 208,000 |
| **Prov. Namur** | 200,000 | 223,000 |
| **Prov. Hainaut** (Charleroi, Mons) | 170,000 | 170,000 |
| **Prov. Luxembourg** | 215,000 | 220,000 |
| **Knokke-Heist** (municipality, coast) | 615,000 | 825,000 (all house types) |

(H1 2026 data, source Statbel 'House prices – first semester 2026': medians from deeds registered by FPS Finances, resale only, new builds excluded. Province rows are province-wide figures and do not describe the city named in brackets.)

- **Detached houses (4+ façades), H1 2026 medians**: Belgium 402,400 · Brussels 1,230,000 · Flanders 449,000 · Wallonia 331,000 (2026 data, source Statbel)
- **Full-year 2025 medians** (apartment / 2-3 façades / detached): Flanders 260,000 / 317,100 / 430,000 · Brussels 270,000 / 510,000 / 1,060,000 · Wallonia 190,000 / 198,000 / 325,000 (2025 data, source Statistiek Vlaanderen 'Woningprijs', from Statbel, updated 19 May 2026)
- **Fednot averages, first nine months of 2026** (new + existing): house 360,613 (Brussels 609,227 · Flanders 398,182 · Wallonia 270,239); apartment 287,616 (Brussels 301,666 · Flanders 300,349 · Wallonia 216,239) (2026 data, source notaire.be Baromètre immobilier, 13 Oct 2026)
- **€/m²** is not published by Statbel or Fednot: compute it from the listing's habitable area; portal €/m² figures are listing-tier

### Compute

1. €/m² = price / **superficie habitable / bewoonbare oppervlakte**
2. **Revenu cadastral (RC) / kadastraal inkomen (KI)**: critical reference value for tax — pre-1975 baseline indexed
3. **VME / co-propriété**: must read **assemblées générales** + **état descriptif** + **règlement**

### Key terms

- Pleine propriété / volle eigendom = freehold
- Revenu cadastral (RC) / Kadastraal inkomen (KI) = cadastral income (1975 baseline + index)
- VME (Vereniging van Mede-Eigenaars) / ACP (association de copropriétaires) = HOA
- PEB / EPC = energy certificate

---

## Section: `--traffic`

### Sources

- **SPW Mobilité** (Wallonie): `https://mobilite.wallonie.be/`
- **MOW (Mobiliteit en Openbare Werken Vlaanderen)**: `https://mobiliteit.vlaanderen.be/`
  - **Verkeerstellingen op Vlaamse gewestwegen**: open data
- **Bruxelles Mobilité**: `https://mobilite-mobiliteit.brussels/`

### Key term

- **PJM (Pays Jour Moyen)** / **GMD (Gemiddelde Daagse Verkeersintensiteit)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,500 v/d (rue résidentielle, voirie communale)
- 🟡 1,500–10,000 v/d (voirie communale principale, route régionale tranquille)
- 🟠 10,000–30,000 v/d (route régionale, axe urbain)
- 🔴 > 30,000 v/d (autoroute, ring, axe central)

---

## Section: `--tax`

### Annual property tax — Précompte immobilier / Onroerende voorheffing

**Three regional regimes** (base = RC/KI × indexation coefficient **2.3000** for 2026 — 2026 data, source vlaanderen.be / be.brussels):

#### Wallonie

- Base: indexed RC × **1.25%** (régional SPW Fiscalité) + opcentimes provinciales + opcentimes communales (2026-05-27 verified, source: finances.wallonie.be)
- SPW Fiscalité has collected Wallonia précompte since 1 Jan 2021 (previously SPF Finances)
- Effective rate ~30–60% of indexed RC depending on commune
- Typical residential: **~€600–€2,500/yr est.** (indexed RC × ~30–60% effective rate above — verify on your own RC)
- **Réductions** (2026 data, source wallonie.be): habitation modeste 25% of the précompte (50% for the first 5 yrs of a new home built or bought without a Walloon premium) if total non-indexed RC ≤ €745; €125 per dependent child (min. 2 children); €250 per disabled dependent

#### Vlaanderen

- Base: indexed KI × **3.97%** (basisheffing VLABEL) + opcentiemen provincie + opcentiemen gemeente (2026-05-27 verified, source: VLABEL belastingen.vlaanderen.be — highest regional base rate in BE)
- Effective rate ~35–65% of indexed KI
- Typical residential: **~€700–€2,800/yr est.** (indexed KI × ~35–65% effective rate above — verify on your own KI)
- **Vermindering** for primary residence + dependents

#### Bruxelles-Capitale

- Base: indexed RC × **1.25%** (régional) + **989** centimes additionnels de l'Agglomération (= 12.3625% of indexed RC) + centimes communaux (2026: **2,440** Auderghem to **4,191** Schaerbeek; regional average 3,599) (2026 data, source Bruxelles Fiscalité fiche précompte immobilier, updated 2 Mar 2026)
- Effective rate **~44–66% of indexed RC** in 2026 (computed: 1.25% × (1 + 9.89 + 24.40…41.91); regional average ~58.6%)
- Typical residential: **~€1,000–€3,500/yr est.** (indexed RC × ~44–66% effective rate above, before reductions — verify on your own RC)
- **Reductions** (2026 data, source be.brussels): **BE HOME prime €164** (exercice 2026) deducted from the bill for Brussels residents who own the home they live in; habitation modeste 25% (non-indexed RC ≤ €745, only Brussels property); 10% per child with family allowance (min. 2 children); 20% per disabled person; ten communes add a housing prime (2026: €100–€212.24)
- **BE HOME doubling — announced, not enacted**: €164 → **€328 from exercice d'imposition 2027**; first draft approved by the Brussels Government (be.brussels, 13 Aug 2026; first reading 18 Jun 2026 per Forum for the Future — secondary); still needs Conseil d'État and social-partner opinions and the Brussels Parliament's vote

### Transaction taxes — Droits d'enregistrement / Registratierechten

**MAJOR REFORM 1 January 2025** — both Vlaanderen + Wallonie cut for primary residence:

#### Vlaanderen (effective 1 Jan 2025)

- **Enige eigen woning (own home, primary)**: **2%** for authentic deeds from 1 Jan 2025 (down from 3%) (2026 data, source vlaanderen.be — Vlaamse Belastingdienst)
  - Conditions: sole home (no other dwelling or building plot in full ownership, in BE or abroad); a dwelling, not a building plot; new homes sold with 21% VAT excluded (2026 data, source vlaanderen.be)
  - **Tightening for sale agreements from 1 Jan 2026** (2026 data, source vlaanderen.be — Vlaamse Belastingdienst): register at the property within 3 yrs of the deed and keep it **≥1 uninterrupted year**; **natural persons only** (a legal-entity co-buyer puts every buyer on 12%); full ownership only (no bare-ownership / usufruct-only purchases); trigger date = compromis (not deed)
- **3% from 1 Jan 2027 — announced, decree pending** (status 2026-10-23): Septemberverklaring 30 Sep 2026; voorontwerp Programmadecreet bij de begrotingsopmaak 2027 approved in principle 9 Oct 2026 (VR 2026 0910 DOC.1079 — art. 2 replaces 2% by 3% in art. 2.9.4.2.11 §1 VCF, art. 136 in force 1 Jan 2027; MvT: applies to agreements concluded from 1 Jan 2027, +€230m/yr); not yet adopted by the Vlaams Parlement. VLABEL SP 26021 (1 Oct 2026, onder voorbehoud of the decree): a compromis signed before 1 Jan 2027 keeps 2%; the notary adds a fiscal declaration to the deed; VLABEL always asks for proof for deeds passed after 30 Apr 2027; a gekruiste optie (mutual purchase/sale promise) is dated by the deed
- **Andere woning (other / second / BTL)**: **12%** (since 1 Jan 2022, up from 10%; 2026 data, source vlaanderen.be — unchanged by the 2027 draft decree, which amends only the reduced rate)

#### Wallonie (effective 1 Jan 2025)

- **Habitation propre et unique (own home, primary)**: **3%** (down from 12.5%) for authentic deeds from 1 Jan 2025; also for a building plot or a dwelling on plan / under construction (2026 data, source fin.belgium.be / wallonie.be FAQ)
  - Conditions: buy the whole property in full ownership; own no other dwelling outright in full ownership (BE or abroad) unless it is sold within 3 yrs; establish main residence within 3 yrs (5 yrs for a building plot) and keep it ≥3 yrs — otherwise the 12.5% − 3% difference is due (2026 data, source fin.belgium.be / wallonie.be FAQ)
  - **Trade-off**: chèque-habitat abolished for homes acquired or built from 2025 (existing beneficiaries keep it — wallonie.be FAQ); the abattement première habitation (art. 46bis C. enr.) and the 6% / 5% modest-housing rates also abolished (décret wallon 5 Dec 2024, circulaire 2025/C/42 of 5 Jul 2025 — per Nisaba commentary, secondary)
- **Other (second home / BTL)**: **12.5%** (2026 data, source fin.belgium.be / wallonie.be FAQ)

#### Bruxelles-Capitale

- **Standard**: **12.5%** (2026 data, source fin.belgium.be / be.brussels)
- **Abattement**: first **€200,000** exempt (saving up to €25,000 = 12.5% × €200,000) when price + charges ≤ **€600,000**; natural person buying the whole in full ownership, owning no other dwelling in full ownership at the compromis, main residence within 3 yrs, kept 5 uninterrupted yrs (2026 data, source be.brussels)
- **Building plot**: first €100,000 exempt (price cap €300,000); **energy-renovation top-up** since 1 Apr 2023: +€25,000 abattement per PEB class gained (min. 2 classes, within 5 yrs) (2026 data, source be.brussels)

### Frais de notaire / notariskosten

- ~1.5–2% est. on top of registration duties (notary honoraria + admin costs + 21% VAT + disbursements; a mortgage deed adds more)
- Honoraria fixed by royal decree as a degressive % of price — the notary may charge neither more nor less: ~1.3% at €125,000, ~1% at €200,000, 0.057% on the slice above €250,095 (2022 data, source notaire.be — rates/figures may have changed since)

### TVA / BTW (new builds)

- **21%** on a new dwelling bought from a promoter (or from a private seller who opts for VAT) — replaces droits d'enregistrement; a dwelling is 'new' until 31 Dec of the 2nd year after first occupation (2026 data, source fin.belgium.be)
- Land sold with the new dwelling: in principle also 21% VAT when three cumulative conditions are met; otherwise registration duty on the land at 12% (Vlaanderen) or 12.5% (Wallonie, Bruxelles) (2026 data, source fin.belgium.be)
- **6% demolition + reconstruction — permanent regime from 1 Jul 2025, Belgium-wide** (2026 data, source fin.belgium.be): (1) owner-builder natural person, sole own home ≤**200 m²**, domicile ≥5 yrs (unchanged since 1 Jan 2024); (2) social rental ≥15 yrs via a social letting agency / social housing body (no surface cap); (3) private rental ≥15 yrs to a person domiciled there, ≤200 m²; (4) new from 1 Jul 2025: **sale** of the reconstructed dwelling at 6% to a natural person who lives there (≤**175 m²**, sole own home), or for 15-yr social or private rental (private: ≤175 m²); above 175 m² at first occupation → 21%

### Total transaction cost (buyer side)

| Region | Primary residence | Second home / BTL |
|---|---:|---:|
| **Vlaanderen** | ~3.5–4.5% (~4.5–5.5% est. for compromis from 1 Jan 2027, decree pending) | ~13.5–14.5% |
| **Wallonie** | ~5–6% | ~14.5–16% |
| **Bruxelles** | ~8–11% est. at €400k–600k with the abattement (duty alone: 6.25% at €400k, 8.33% at €600k; no abattement above €600k) | ~14.5–16% |

### Capital gains

- **Own-home sale**: exempt if it was the seller's own home for ≥12 uninterrupted months right before the month of sale (2026 data, source fin.belgium.be — explications déclaration 2026)
- **Buildings held >5 yrs**: exempt — taxable only if sold within 5 yrs of a purchase for value (new builds: construction started within 5 yrs of buying the land and the whole sold within 5 yrs of first occupation or letting) (2026 data, source fin.belgium.be)
- **Buildings sold within 5 yrs**: 16.5% (+ communal surcharges) (SPF Finances Mémento fiscal 2017 — rates/figures may have changed since). The 10% capital-gains tax in force from 1 Jan 2026 covers financial assets, not real estate (law published in the Moniteur belge 21 Apr 2026, per RSM Belgium — secondary)
- **Land sold within 8 yrs**: **33%** if sold ≤5 yrs after purchase, **16.5%** if sold after 5 yrs (+ communal surcharges) (2026 data, source fin.belgium.be — explications déclaration 2026)

### Future risk

- **Vlaanderen 2% → 3%** for compromis signed from 1 Jan 2027 — announced, decree pending (see Transaction taxes above)
- **Wallonie 3% rate** kept in the 2027 regional budget, with an evaluation and an a-posteriori check of 2025–2026 acquisitions announced (Forum for the Future regional-budget grid, Oct 2026 — secondary)
- **Bruxelles**: abattement stays €200,000 in the 2027 budget; raising the €600,000 price ceiling to €800,000 is a 2029 objective subject to available funds (DPR 13 Feb 2026, per Forum for the Future — secondary); BE HOME prime doubling to €328 from exercice 2027 announced, not enacted (be.brussels, 13 Aug 2026)
- **RC reform**: long-discussed at federal level; the 1 Jan 1975 reference period still applies in 2026 (Bruxelles Fiscalité fiche, updated 2 Mar 2026)

---

## Section: `--rental`

### Long-term residential

- **Bail de résidence principale / Hoofdverblijfsovereenkomst**: presumed 9 yrs, renewed for 3 yrs at a time if the landlord gives no notice 6 months before expiry; in Vlaanderen the landlord may end it without reason at the end of the 1st or 2nd 3-year period on 6 months' notice plus 9 or 6 months' rent as compensation, unless the lease excludes or limits this (2026 data, source Vlaams Woninghuurdecreet art. 16 + 19, codex.vlaanderen.be) — termination rules differ per région, read the region's text
- **Indexation**: at most once a year, at the earliest on the lease anniversary, on the **health index** (indice santé / gezondheidsindex), not the CPI (2026 data, source Wallonie décret 15 Mar 2018 art. 26; be.brussels 'Indexation des loyers'; vlaanderen.be). Wallonie: only if the lease provides for indexation (art. 26 §1). Bruxelles: indexation needs a registered lease and a valid PEB given to the tenant; for leases that took effect before 14 Oct 2022, a correction factor cuts it for PEB E, F and G homes (Code bruxellois du Logement art. 224/2, ordonnance 13 Oct 2023; be.brussels)
- **Vlaanderen Woninghuurdecreet** — applies to leases signed from 1 Jan 2019 (2026 data, source vlaanderen.be)
- **Wallonie Décret du 15 mars 2018 relatif au bail d'habitation** — in force 1 Sep 2018; the Code wallon de l'habitation durable is the separate housing-policy code (2026 data, source wallex.wallonie.be)
- **Bruxelles Code bruxellois du logement** — regional lease rules in force since 1 Jan 2018 (ordonnance 27 Jul 2017), amended by the ordonnance of 4 Apr 2024 (in force 1 Nov 2024; some changes apply only to leases signed or renewed from that date); regional lease registration since 1 Jan 2025 (ordonnance 25 Apr 2024) (2026 data, source be.brussels lease brochure Jan 2025 + Bruxelles Logement activity report 2025)
- Tenant rights moderate (less strict than DE/AT)

### Short-let (Airbnb / hébergement touristique)

**Three regional regimes**:

#### Bruxelles-Capitale

- **Prior registration** with **Bruxelles Économie et Emploi** is required before any paid tourist let of 1 night to 90 days, for individuals and companies alike; operating unregistered is illegal (2026 data, source economie-emploi.brussels)
- The registration file includes a commune attestation that the tourist use complies with urban-planning rules (ordonnance 8 May 2014 art. 4 + arrêté 24 Mar 2016 art. 7 — secondary summary, droitbelge.be)
- **Ordonnance of 1 Feb 2024** on tourist accommodation repeals and replaces the 2014 ordonnance once in force; its entry-into-force date is left to the Government (art. 45, etaamb.openjustice.be) — verify at economie-emploi.brussels which regime applies on the purchase date
- **EU Reg 2024/1028** is a directly applicable regulation, applying since 20 May 2026 — nothing to transpose; Member States are not obliged to apply it, but any registration scheme or platform-data request must go through it (2026 data, source European Commission DG GROW, 20 May 2026)

#### Wallonie

- **Code wallon du Tourisme (CWT)** — décret of 8 Feb 2024 + arrêté of 16 May 2024, in force 1 Jul 2025: every hébergement touristique must be **registered with Tourisme Wallonie**; registration replaced the declaration duty in force since 2017 (2026 data, source Data Protection Authority opinion 113/2026 of 4 Jun 2026)
- Registration needs a fire-safety attestation (ASI) from the mayor of the commune (Arius law firm, secondary); Tourisme Wallonie issues a unique registration number, which platforms such as Airbnb and Booking.com ask for (CPDT/IGEAT methodological note, Dec 2024)
- **Pending**: an avant-projet de décret aligning the CWT with EU Reg 2024/1028 (immediate registration with ex-post checks, platform verification of numbers, activity data to Tourisme Wallonie) was before the Data Protection Authority in Jun 2026; adoption not confirmed on 2026-10-23 — verify at wallex.wallonie.be

#### Vlaanderen

- **Logiesdecreet** (decree of 5 Feb 2016, applicable since 1 Apr 2017) — **aanmelding** (registration) at **Toerisme Vlaanderen** is mandatory and gives a unique registration number, which booking platforms ask for (2026 data, source Vlaanderen Vakantieland / Toerisme Vlaanderen, updated 19 Aug 2026)
- **Brandveiligheidsattest** + fire and civil-liability insurance required; **erkenning** (recognition) and comfort classification are voluntary (2026 data, source Flemish Government memorie van toelichting VR 2026 2905 DOC.0530/3; Vlaanderen Vakantieland)
- **EU Reg 2024/1028** (applies since 20 May 2026; a regulation, not a directive): the Logiesdecreet amendment naming Toerisme Vlaanderen as competent authority and setting sanctions got final Flemish Government approval and was sent to the Vlaams Parlement on 17 Jul 2026; the minister ties enforceability to that decree plus a central digital entry point, both expected in force in 2026 (2026 data, source answer to Vlaams Parlement written question 482 of 4 Jun 2026; vlaanderen.be government decision of 17 Jul 2026) — verify adoption at vlaamsparlement.be

### Tax on rental

- **Residential rental to a private tenant who does not use it professionally**: taxed on indexed RC/KI × 1.40, not on the rent received; often substantially below market — **major tax-optimization advantage**; indexation coefficient 2.2446 for 2025 income (2025 data, source Keytrade Bank / Accountable — secondary; fin.belgium.be 'Un bien immobilier que je mets en location' sets the treatment by tenant type)
- **Furnished let**: the furniture share of the rent is movable income — 40% of the rent if the lease sets no split, then a 50% flat cost deduction, taxed at 30% (2026 data, source Viseeon accountants — secondary)
- **Professional tenant / company**: actual rent minus a 40% flat cost allowance (capped at 2/3 of the revalorised RC/KI), never below indexed RC/KI × 1.40, taxed at progressive rates (2026 data, source Viseeon, Accountable — secondary)
- **Short-let**: VAT on furnished accommodation with hotel-type services (reception, linen or daily breakfast) rose from **6% to 12% on 1 Mar 2026** (2026 data, source SPF Finances VAT FAQ as reproduced by Forum for the Future). Income tax for a private host: KI-based property income on the let part + movable income on the furniture share + miscellaneous income if extra services such as cleaning or linen are provided (Airbnb Belgium tax guide 2026 — platform tier, verify with an accountant)

---

## Section: `--work=<profession>`

### Sources

- **Forem** (Wallonie): `https://www.leforem.be/`
- **VDAB** (Vlaanderen): `https://www.vdab.be/`
- **Actiris** (Bruxelles): `https://www.actiris.brussels/`
- **LinkedIn BE**, **StepStone**, **Indeed**, **References.be**

### Self-employment

- **Statut indépendant**: BCE (Banque Carrefour des Entreprises) / KBO registration
- **TVA** (VAT): small-business franchise (no VAT charged) for annual turnover up to €25,000 excl. VAT (2026 data, source SPF Finances 'Régimes TVA')
- **INASTI / RSVZ social contributions** (main occupation): 20.5% of net professional income up to €75,024.54, 14.16% from €75,024.54 to €110,562.42, nothing above; minimum €890.42 per quarter (2026 data, source INASTI FAQ + SPF Sécurité sociale 'Cotisations sociales 2026')
- **Personal income tax**: progressive 25% / 40% / 45% / 50%; income-year 2026 bands €0–16,720 / 16,720–29,510 / 29,510–51,070 / above 51,070 (2026 data, source fin.belgium.be 'Taux d'imposition' + Pyxis & Co table)
- **Régime forfaitaire** (VAT flat-rate scheme for small traders): closed to new entrants since 1 Jan 2022, abolished on 1 Jan 2028 (2026 data, source SPF Finances 'Régime forfaitaire')

### Salary benchmarks

- **Average gross monthly pay, full-time employees, by region of workplace** (firms with 10+ staff; October pay, excl. 13th month and holiday pay): Bruxelles €4,748 · Vlaanderen €4,028 · Wallonie €3,794 · Belgium €4,076 (2022 data, source Statbel 'Gemiddelde bruto maandlonen' / beSTAT, latest year published — rates/figures may have changed since)
  - Computed × 12 (still excl. 13th month and holiday pay): Bruxelles €56,976 · Vlaanderen €48,336 · Wallonie €45,528
- **Median gross monthly pay, full-time, private sector, January 2026**: Brussel €4,200 · Vlaanderen €3,585 (provinces: Antwerpen €3,605, Limburg €3,600, Oost-Vlaanderen €3,595, Vlaams-Brabant €3,580, West-Vlaanderen €3,515) (2026 data, source SD Worx payroll barometer, 12 Mar 2026 — secondary, 400,000+ payslips; the release gives no Wallonia figure)

---

## Section: `--risks`

### Primary regional sources

| Source | URL | What it gives |
|---|---|---|
| **Geopunt Vlaanderen** | `https://www.geopunt.be/` | Vlaanderen geo-data, hazard layers |
| **WalOnMap** | `https://geoportail.wallonie.be/` | Wallonie geoportal |
| **BruGIS** | `https://gis.urban.brussels/brugis` | Bruxelles geoportal |
| **CIRGT Wallonie** | `https://environnement.wallonie.be/` | Risk maps Wallonie |
| **OVAM** (Vlaanderen bodempolluties) | `https://www.ovam.be/` | Soil pollution Vlaanderen |
| **Bruxelles Environnement** | `https://environnement.brussels/` | Bruxelles env data |
| **IRM (Institut Royal Météorologique)** | `https://www.meteo.be/` | Climate, weather |
| **AwAC** Wallonie air quality | `https://www.awac.be/` | Wallonie air |
| **VMM** Vlaamse Milieumaatschappij | `https://www.vmm.be/` | Vlaanderen environment |
| **CELINE** | `https://www.irceline.be/` | National air quality |

### Specific risks

- **Inondation / overstroming (flooding)** — major risk:
  - July 2021 catastrophic floods (Wallonie): ~40 dead, ~€2B damage; Liège, Verviers, Pepinster, Theux
  - Vesdre, Meuse, Ourthe basins
  - **Plan PARGI / Bekkenbeheerplan** for adaptation
- **Bodemverontreiniging / pollution du sol**: extensive industrial legacy in Wallonie + Antwerpen + Charleroi
- **Aardbeving / séisme**: low-moderate (Roer Valley fault); 1992 Roermond M 5.4 (felt in BE)
- **Mijnverzakkingen** (mining subsidence): Limburg (coal), Wallonie (Borinage); historic
- **Asbestos**: pre-1998 buildings extensively contaminated
- **Loodleidingen** (lead pipes) — pre-1960 buildings
- **Pollution de Charleroi-Mons-Liège axe**: heavy metal soil contamination
- **Klimaatverandering**: +2.0–4.0 °C by 2100; precipitation +20% winter

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, damp, asbestos cement starts |
| **1900–1945** | Asbestos common, lead, weak insulation |
| **1945–1990** | Asbestos very common (banned 1998); cuves à mazout (oil tanks) |
| **1990s+** | Improved insulation; PEB phasing in |
| **2014+** | PEB strict; Q-ZEN / BEN energy standards |

### Mandatory at sale

| Document | Region | Required because | Validity |
|---|---|---|---|
| **PEB** (FR) / **EPC** (NL) | All | Energy cert | 10 years |
| **Bodemattest** | Vlaanderen | Soil report | At sale (sale BLOCKED without it) |
| **Asbestattest** | Vlaanderen | Mandatory since **23 Nov 2022** for sales | 10 years |
| **Attestation du sol / bodemcertificaat** | Bruxelles | Mandatory | At sale |
| **Pollution du sol** | Wallonie | Banque de Données de l'État des Sols | At sale |
| **Contrôle électrique** | All | If wiring >25 yrs | 25 years |
| **Citerne mazout** | Where applicable | Permit | Ongoing |
| **CIGT** (Wallonie certificat) | Wallonie | If applicable | Per case |

### Climate change projections

- +2.0–4.0 °C by 2100
- +20% winter precipitation, -20% summer
- More extreme rainfall (Vesdre 2021 type)
- Sea-level rise + coastal management Vlaamse Kust

---

## Section: `--mains`

### Sources

- **SWDE** (Société wallonne des eaux): `https://www.swde.be/` — Wallonie water
- **IECBW** (Intercommunale eaux Centre Brabant wallon)
- **IDEA** (Intercommunale développement économique Mons-Borinage)
- **CILE** (Compagnie intercommunale liégeoise eaux)
- **De Watergroep**, **Pidpa**, **Aquaduin** — Vlaanderen water
- **Vivaqua / Hydrobru**: `https://www.vivaqua.be/` — Bruxelles
- **Aquafin** (Vlaanderen wastewater): `https://www.aquafin.be/`

### Verification

- Universal in urban areas across all three régions
- Some rural Wallonie / Eifel border on individual systems (fosses septiques)
- Vlaanderen ~97% mains coverage (est.)
- Wallonie ~85% mains coverage

### Costs

| Scenario | Cost (€) |
|---|---:|
| Aansluiting riool / raccordement égout | 6,000–15,000 |
| Septique / IBA installation | 8,000–15,000 |
| Cuve mazout removal | 1,500–4,000 |

---

## Cost benchmarks (BE 2026) — est. ranges, verify with contractor quotes

| Work | Cost (€) |
|---|---:|
| PEB / EPC | 150–350 |
| Asbestattest (Vlaanderen) | 350–600 |
| Bodemattest (Vlaanderen) | 73.05 per full parcel; 275.05 per part of a parcel (since 1 Jan 2026, source vlaanderen.be) |
| Notaris fees | ~1.5–2% of price est. (honoraria + admin + 21% VAT; honoraria alone ~1% at €200,000 — 2022 data, notaire.be — rates/figures may have changed since) |
| Registration duties (primary, Vlaanderen) | 2% (since 1 Jan 2025); 3% for compromis from 1 Jan 2027 (decree pending) |
| Registration duties (primary, Wallonie) | 3% (since 1 Jan 2025) |
| Registration duties (Bruxelles) | 12.5% (first €200,000 exempt for an own home priced ≤ €600,000) |
| **Total transaction cost (Vlaanderen primary)** | **~3.5–4.5%** (~4.5–5.5% est. from 1 Jan 2027, decree pending) |
| **Total transaction cost (Wallonie primary)** | **~5–6%** |
| **Total transaction cost (Bruxelles primary)** | **~8–11%** est. at €400k–600k with abattement |
| **Total transaction cost (second home)** | **~13.5–16%** |
| Septic to mains | 6,000–15,000 |
| Cuve mazout removal | 1,500–4,000 |
| Roof renovation | 15,000–30,000 |
| Asbestos removal | 1,000–10,000 |
| Energy retrofit (Class C → A) | 25,000–60,000 |

## Active fiscal incentives (2025-2026)

- **Wallonie**: chèque-habitat ABOLISHED for homes acquired or built from 2025 (replaced by the 3% rate; existing beneficiaries keep it — wallonie.be FAQ)
- **Vlaanderen**: woonbonus phased out; 2% rate now, 3% for compromis from 1 Jan 2027 (decree pending)
- **Bruxelles**: abattement €200,000 still in force (price ≤ €600,000); BE HOME prime €164/yr off the précompte (exercice 2026; €328 from 2027 announced, not enacted) (source be.brussels)
- **Régionalisation aides**: rénovation énergétique grants per région
- **Federal EE-loan**: ❌ DEPRECATED — dead on 2026-10-23 (no federal scheme traceable; energy-renovation loans are regional, see Mijn VerbouwLening and the Wallonie regime below); verify with VEKA / SPW Énergie / Bruxelles Environnement
- **Mijn VerbouwLening** (Vlaanderen): up to €60,000 over ≤25 yrs at 1.5% / 0.5% / 0% by income category; highest income category excluded (2026 data, source vlaanderen.be — VEKA)
- **Wallonie renovation support (from 1 Oct 2026)**: loan-based — Rénopack (0%, with a 15–50% repayment reduction for income categories C1–C3) and Rénoprêt; reserved to PEB G/F homes renovated to ≥D or PEB E homes renovated to ≥C; up to €75,000 per house, €60,000 per apartment (2026 data, source wallonie.be)

## Common listing platforms

- **Immoweb** — DOMINANT
- **Zimmo** (NL + FR; absorbed Logic-Immo.be in June 2023)
- **Realo** (NL)
- **Immovlan** (FR/NL; `vlan.be` itself now redirects to a Sudinfo newspaper section)

## Caveats unique to BE

- **Régionalisation extreme** — three different regimes for almost everything (transfer tax, energy, planning, environment)
- **2025 transfer tax reform** — Vlaanderen 3→2%, Wallonie 12.5→3%; major affordability boost — Vlaanderen back to 3% for compromis from 1 Jan 2027 (decree pending, see `--tax`)
- **Bodemattest / asbestattest** mandatory in Vlaanderen — sale BLOCKED without these
- **Asbestattest mandatory since 23 Nov 2022** (Vlaanderen) for sales of buildings built before 2001; valid 10 yrs (source vlaanderen.be)
- **PEB E/F/G** increasingly restricted in Wallonie — minimum standards tightening
- **Cuve à mazout** strict regulations
- **RC/KI 1975 baseline** — wildly outdated; reform proposed for years
- **VME health** mandatory pre-purchase (apartment): assemblées + comptes + état
- **Régionalisation** of stamp duty since 2002 — complete divergence
- **Wallonie Vesdre flood 2021** memory shapes flood disclosure rules
- **Brussels Code du Logement** — strict tenant protections + minimum standards
- **3 régions, 3 EPC formats, 3 grant systems** — read region-specific rules

## Reddit / forum sources

- **r/belgium**, **r/Brussels**, **r/AskBelgium**
- **r/BEFire** — Belgian personal finance and investing, incl. tax and buy-vs-rent threads; companion **r/BEFinance** (created Aug 2024) for general money questions (forum tier, seen via Reddit mirrors 2026)
- **Tweakers BE Forum**
- Expat: **The Bulletin**, **Expatica BE**, **Brussels Times**

## Verification authorities

| Authority | When to call |
|---|---|
| **AGDP / FOD Financiën cadastre** | Title verification, RC/KI |
| **Notaris** (mandatory for sale) | Final transfer + searches |
| **Commune urbanisme** | Permits, planning history |
| **Region-specific environment agency** (OVAM/SPW/Bruxelles Env) | Pollution, asbestos |
| **VME / ACP secretary** | If apartment: financials |
| **Région tax services** | Précompte, registration |

## Source URL templates

| Source | URL pattern |
|---|---|
| Cadastre FOD Fin | `https://finances.belgium.be/fr/particuliers/habitation/cadastre` |
| Notaires.be barometer | `https://www.notaire.be/` |
| STATBEL housing | `https://statbel.fgov.be/en/themes/housing/real-estate` |
| Geopunt Vlaanderen | `https://www.geopunt.be/` |
| WalOnMap | `https://geoportail.wallonie.be/` |
| BruGIS | `https://gis.urban.brussels/brugis` |
| OVAM Vlaanderen | `https://www.ovam.be/` |
| Bruxelles Environnement | `https://environnement.brussels/` |
| Immoweb | `https://www.immoweb.be/` |
| MOW Vlaanderen traffic | `https://mobiliteit.vlaanderen.be/` |
| SPW Mobilité | `https://mobilite.wallonie.be/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax (3 régions), rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for 2025 transfer tax reform (Beobank, Argenta, S-Team Law, ABM-Altos, Lexunion all confirm Vlaanderen 2% + Wallonie 3% from 1 Jan 2025), HIGH for asbestattest mandate (23 Nov 2022 Vlaanderen), HIGH for July 2021 flood as reform driver. MEDIUM for Bruxelles short-let (rapidly evolving + EU 2024/1028 transposition pending).

## Extension TODOs

- [ ] Per-commune précompte / onroerende voorheffing rates table
- [ ] Asbestattest detailed inspection checklist
- [ ] PEB regulations per région timetable (FR / NL / DE versions)
- [ ] Logies / hébergement licensing per région (Logiesdecreet, CGT)
- [ ] Vesdre 2021 flood-affected zones (rebuilding rules)
- [ ] Bodemattest decision tree (clean/contaminated/in-progress)
- [ ] Per-commune renovation premium eligibility
- [ ] EU 2024/1028 short-let transposition tracker (3 régions)
- [ ] Brussels heritage building constraints per zone
- [ ] German-speaking Eastern Cantons specific rules
