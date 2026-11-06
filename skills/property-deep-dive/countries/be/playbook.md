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

- **SPW Mobilité et Infrastructures** (Wallonie): `https://mobilite.wallonie.be/`
- **Departement MOW (Mobiliteit en Openbare Werken Vlaanderen)**: `https://www.vlaanderen.be/departement-mobiliteit-en-openbare-werken` (the old `mobiliteit.vlaanderen.be` now redirects to `mobielvlaanderen.be`; updated 2026-10-23)
  - **Vlaams Dataportaal Verkeersgegevens** (Vlaams Verkeerscentrum / AWV): `https://www.verkeerscentrum.be/data` — counts for snelwegen, gewestwegen, lokale wegen and fietspaden; free, login with a digital key such as itsme; AWV's fixed counting loops on gewestwegen were taken out of service end 2016 (sources: verkeerscentrum.be/data, wegenenverkeer.be/betrouwbaarheid/verkeerstellingen)
- **Bruxelles Mobilité**: `https://mobilite-mobiliteit.brussels/` now redirects to `https://be.brussels/fr/transport-mobilite` (updated 2026-10-23); traffic-counter open data (counting loops + cameras, CC0 licence) at `https://data.mobility.brussels/` (source: data.mobility.brussels)

### Key term

- **TJM (trafic journalier moyen)**, annual 0h–24h average = AADT-equivalent — term used in SPW mobility guidance (source: mobilite.wallonie.be Cémathèque n°23); Flemish count data are published as verkeersintensiteiten per kwartier / uur / dag per wegsegment (source: verkeerscentrum.be/data)

### Verdict bands

- 🟢 < 1,500 v/d (rue résidentielle, voirie communale)
- 🟡 1,500–10,000 v/d (voirie communale principale, route régionale tranquille)
- 🟠 10,000–30,000 v/d (route régionale, axe urbain)
- 🔴 > 30,000 v/d (autoroute, ring, axe central)

---

## Section: `--tax`

### Annual property tax — Précompte immobilier / Onroerende voorheffing

**Three regional regimes** (base = RC/KI × indexation coefficient **2.3000** for 2026 — 2026 data, source vlaanderen.be / be.brussels / wallonie.be):

#### Wallonie

- Base: indexed RC × **1.25%** (régional SPW Fiscalité) + opcentimes provinciales + opcentimes communales (2026 data, source wallonie.be)
- SPW Fiscalité has collected Wallonia précompte since 1 Jan 2021 (previously SPF Finances) (source interieur.wallonie.be, circulaire budgétaire 2027 des provinces)
- Effective rate (computed): indexed RC × 1.25% × (1 + (provincial + communal centimes)/100). Inputs: communal centimes 1,200–3,200, average 2,584 (2025 data, source UVCW fiche on the additionnels au précompte immobilier, updated 10 Oct 2025 — association of Walloon municipalities, secondary — rates/figures may have changed since); provincial centimes Hainaut **1,895** (2026 data, source Bulletin provincial du Hainaut, 16 Dec 2025), Liège **1,750** (2025 data, source Province de Liège resolution — rates/figures may have changed since); the provincial budget circular recommends at most **1,500** provincial centimes — a ceiling, not a floor (source interieur.wallonie.be, circulaire budgétaire 2027 des provinces) → at the average communal rate: **~52%** of indexed RC with a province at 1,500 (1.25% × (1 + 15.00 + 25.84)), **~55%** in Liège (1.25% × (1 + 17.50 + 25.84)), **~57%** in Hainaut (1.25% × (1 + 18.95 + 25.84)), less in a province below 1,500; **~65%** with the highest communal and provincial rates found (1.25% × (1 + 18.95 + 32.00)); Namur, Luxembourg and Brabant wallon provincial rates: verify with SPW Fiscalité (finances.wallonie.be) or on the avertissement-extrait de rôle
- Bill per €1,000 of non-indexed RC (computed, 2026, before reductions): €2,300 indexed RC × 52.3–57.2% = **~€1,200–€1,320/yr** at the average communal rate with 1,500–1,895 provincial centimes — scale to the property's own RC (on the deed or in MyMinfin)
- **Réductions** (2026 data, source wallonie.be): habitation modeste 25% of the précompte (50% for the first 5 yrs of a new home built or bought without a Walloon premium) if total non-indexed RC ≤ €745; €125 per dependent child (min. 2 children); €250 per disabled dependent

#### Vlaanderen

- Base: indexed KI × **3.97%** (basisheffing VLABEL) + opcentiemen provincie + opcentiemen gemeente (2026 data, source vlaanderen.be — Vlaamse Belastingdienst; highest regional base rate in BE)
- Effective rate (computed, 2026): indexed KI × 3.97% × (1 + (provincial + communal opcentiemen)/100). Provincial opcentiemen 2026: Antwerpen 160, Limburg 214.52, Oost-Vlaanderen 148.47, Vlaams-Brabant 171.75, West-Vlaanderen 186.22; communal 472 (Zaventem; also the lowest of Sint-Martens-Latem's three categories) to 1,417 (Alveringem), unweighted average 916.03 of the 285 communes' headline rates (the Vlaamse Belastingdienst overview gives 939.77 averaged over its category rows, and lists a 0 category in Antwerpen and Herk-de-Stad without saying which property types it covers) (2026 data, source vlaanderen.be — Vlaamse Belastingdienst opcentiemen overview and Lokaal Bestuur 'Aanslagvoeten per gemeente') → **~28.6% (Sint-Martens-Latem, lowest category) / ~29.5% (Zaventem) to ~67.6% (Alveringem)** of indexed KI; **~46–49%** at the 916.03 average communal rate, depending on the province
- Bill per €1,000 of non-indexed KI (computed, 2026, before reductions): €2,300 indexed KI × 28.6–67.6% = **~€660–€1,555/yr** (~€1,060–€1,125 at the average communal rate) — scale to the property's own KI; exact bill via the Vlaamse Belastingdienst simulator (belastingen.fenb.be/ui/public/simulaties/ov)
- **Verminderingen** (2026 data, source vlaanderen.be): bescheiden woning 25% for an owner domiciled in the home whose total non-indexed KI in Vlaanderen is ≤ €745; children with family allowance (min. 2 domiciled on 1 Jan): €8.80 base per child for aanslagjaar 2026, plus the provincial and communal opcentiemen on that amount; persons with a disability (≥66% or 9 points); war victims; energy-efficient new or renovated buildings (low E-peil)

#### Bruxelles-Capitale

- Base: indexed RC × **1.25%** (régional) + **989** centimes additionnels de l'Agglomération (= 12.3625% of indexed RC) + centimes communaux (2026: **2,440** Auderghem to **4,191** Schaerbeek; regional average 3,599) (2026 data, source Bruxelles Fiscalité fiche précompte immobilier, updated 2 Mar 2026)
- Effective rate **~44–66% of indexed RC** in 2026 (computed: 1.25% × (1 + 9.89 + 24.40…41.91); regional average ~58.6%)
- Bill per €1,000 of non-indexed RC (computed, 2026, before reductions): €2,300 indexed RC × 44.1–66.0% = **~€1,015–€1,520/yr** (~€1,350 at the regional average) — scale to the property's own RC; the reductions below come off this
- **Reductions** (2026 data, source be.brussels): **BE HOME prime €164** (exercice 2026) deducted from the bill for Brussels residents who own the home they live in; habitation modeste 25% (non-indexed RC ≤ €745, only Brussels property); 10% per child with family allowance (min. 2 children); 20% per disabled person; ten communes add a housing prime (2026: €100–€212.24)
- **BE HOME doubling — announced, not enacted**: €164 → **€328 from exercice d'imposition 2027**; first draft approved by the Brussels Government (be.brussels, 13 Aug 2026; first reading 18 Jun 2026 per Forum for the Future — secondary); second reading approved 22 Oct 2026 (BRUZZ 26 Oct 2026 — secondary; not verified to a primary source — 2026-11-06); Conseil d'État and social-partner opinions not confirmed; still needs the Brussels Parliament's vote

### Transaction taxes — Droits d'enregistrement / Registratierechten

**MAJOR REFORM 1 January 2025** — both Vlaanderen + Wallonie cut for primary residence:

#### Vlaanderen (effective 1 Jan 2025)

- **Enige eigen woning (own home, primary)**: **2%** for authentic deeds from 1 Jan 2025 (down from 3%) (2026 data, source vlaanderen.be — Vlaamse Belastingdienst)
  - Conditions: sole home (no other dwelling or building plot in full ownership, in BE or abroad); a dwelling, not a building plot; new homes sold with 21% VAT excluded (2026 data, source vlaanderen.be)
  - **Tightening for sale agreements from 1 Jan 2026** (2026 data, source vlaanderen.be — Vlaamse Belastingdienst): register at the property within 3 yrs of the deed and keep it **≥1 uninterrupted year**; **natural persons only** (a legal-entity co-buyer puts every buyer on 12%); full ownership only (no bare-ownership / usufruct-only purchases); trigger date = compromis (not deed)
- **3% from 1 Jan 2027 — announced, decree pending** (status 2026-11-06): Septemberverklaring 30 Sep 2026; ontwerp Programmadecreet bij de begrotingsopmaak 2027 given final government approval 28 Oct 2026 and sent to the Vlaams Parlement (VR 2026 2810 DOC.1163 — art. 2 replaces 2% by 3% in art. 2.9.4.2.11 §1 VCF, art. 106 in force 1 Jan 2027; MvT: applies to agreements concluded from 1 Jan 2027, +€230m); not yet adopted by the Vlaams Parlement. VLABEL SP 26021 (1 Oct 2026, onder voorbehoud of the decree): a compromis signed before 1 Jan 2027 keeps 2%; the notary adds a fiscal declaration to the deed; VLABEL always asks for proof for deeds passed after 30 Apr 2027; a gekruiste optie (mutual purchase/sale promise) is dated by the deed — but Raad van State advies 80.188/1-3-16 (19 Oct 2026) says this appears to misread art. 2.9.7.0.3 §1 VCF: unless the option says the sale arises only at the deed, an option exercised before 1 Jan 2027 keeps 2% (advice, not a ruling; the usual De Decker form has that clause, per the government's delegate; SP 26021 unchanged on 2026-11-06)
- **Andere woning (other / second / BTL)**: **12%** (since 1 Jan 2022, up from 10%; 2026 data, source vlaanderen.be — unchanged by the 2027 draft decree, which amends only the reduced rate)

#### Wallonie (effective 1 Jan 2025)

- **Habitation propre et unique (own home, primary)**: **3%** (down from 12.5%) for authentic deeds from 1 Jan 2025; also for a building plot or a dwelling on plan / under construction (2026 data, source fin.belgium.be / wallonie.be FAQ)
  - Conditions: buy the whole property in full ownership; own no other dwelling outright in full ownership (BE or abroad) unless it is sold within 3 yrs; establish main residence within 3 yrs (5 yrs for a building plot, a dwelling on plan or under construction) and keep it ≥3 yrs — otherwise the 12.5% − 3% difference is due (2026 data, source fin.belgium.be / wallonie.be FAQ; art. 44bis C. enr. in the décret wallon of 5 Dec 2024 — wallex.wallonie.be)
  - **Trade-off**: chèque-habitat abolished for homes acquired or built from 2025 (existing beneficiaries keep it — wallonie.be FAQ); the abattement première habitation (art. 46bis C. enr.; €40,000 of the price exempt below €350,000, tapering to €20,000 above €500,000, max saving €5,000) and the 6% modest-housing / 5% social-loan rates ended on 1 Jan 2025 (source fin.belgium.be 'Droit d'enregistrement en Région wallonne : réductions d'impôt supprimées', archived 2025-10-07; décret wallon of 5 Dec 2024, in force 1 Jan 2025: art. 10 repeals art. 46bis and art. 12 confines the 5% / 6% rates of art. 53 to rural property — wallex.wallonie.be; circulaire 2025/C/42 of 5 Jul 2025, SPF Finances text reproduced by Forum for the Future — secondary)
- **Other (second home / BTL)**: **12.5%** (2026 data, source fin.belgium.be / wallonie.be FAQ)

#### Bruxelles-Capitale

- **Standard**: **12.5%** (2026 data, source fin.belgium.be / be.brussels)
- **Abattement**: first **€200,000** exempt (saving up to €25,000 = 12.5% × €200,000) when price + charges ≤ **€600,000**; natural person buying the whole in full ownership, owning no other dwelling in full ownership at the compromis, main residence within 3 yrs, kept 5 uninterrupted yrs (2026 data, source be.brussels)
- **Building plot**: first €100,000 exempt (price cap €300,000); **energy-renovation top-up** since 1 Apr 2023: +€25,000 abattement per PEB class gained (min. 2 classes, within 5 yrs) (2026 data, source be.brussels)

### Frais de notaire / notariskosten

- Honoraria fixed by the tariff annexed to the AR of 16 Dec 1950 (as amended, most recently by the AR of 22 Nov 2022; amounts as consolidated after the 1 Jan 2026 indexation) — the notary may charge neither more nor less (2026 data, source notaire.be unofficial consolidation of 9 Feb 2026):
  - **Barème Jbis** (natural persons buying, in full ownership, their own and only home, domiciled there within 1 yr — otherwise the difference to barème J is due): fixed €257 + 2.5% to €17,500, 2% to €30,000, 1.5% to €45,495, 0.5% to €64,090, 0.485% to €250,095, 0.30% to €500,000, 0.20% above
  - **Barème J** (other purchases): fixed €285 + 2.5% to €17,500, 1.75% to €30,000, 1.71% to €45,495, 1.14% to €64,090, 0.57% to €250,095, 0.20% above
  - Plus a flat **€855** for administrative costs and non-individualisable disbursements (€627 per linked deed from the second one, e.g. the mortgage deed); honoraria and flat fee are set excl. VAT and carry 21% VAT (Chamber doc. 54 3060/001, 26 Apr 2018; 21% confirmed as the standard rate by fin.belgium.be 'Acheter avec TVA', archived 2026-04-18)
- Notary costs computed from the above (honoraria + €855, + 21% VAT): €200,000 → ~€3,370 (1.7%) under Jbis / ~€3,690 (1.8%) under J; €300,000 → ~€3,840 (1.3%) / ~€4,150 (1.4%); €400,000 → ~€4,210 (1.05%) / ~€4,400 (1.1%). Individualisable disbursements (searches, registry fees) and any mortgage deed come on top — the notary's provisional cost statement gives the exact figure

### TVA / BTW (new builds)

- **21%** on a new dwelling bought from a promoter (or from a private seller who opts for VAT) — replaces droits d'enregistrement; a dwelling is 'new' until 31 Dec of the 2nd year after first occupation (2026 data, source fin.belgium.be 'Acheter avec TVA', archived 2026-04-18)
- Land sold with the new dwelling: in principle also 21% VAT when three cumulative conditions are met; otherwise registration duty on the land at 12% (Vlaanderen) or 12.5% (Wallonie, Bruxelles) (2026 data, source fin.belgium.be 'Acheter avec TVA', archived 2026-04-18)
- **6% demolition + reconstruction — permanent regime from 1 Jul 2025, Belgium-wide** (2026 data, source fin.belgium.be): (1) owner-builder natural person, sole own home ≤**200 m²**, domicile ≥5 yrs (unchanged since 1 Jan 2024); (2) social rental ≥15 yrs via a social letting agency / social housing body (no surface cap); (3) private rental ≥15 yrs to a person domiciled there, ≤200 m²; (4) new from 1 Jul 2025: **sale** of the reconstructed dwelling at 6% to a natural person who lives there (≤**175 m²**, sole own home), or for 15-yr social or private rental (private: ≤175 m²); above 175 m² at first occupation → 21%

### Total transaction cost (buyer side)

| Region | Primary residence | Second home / BTL |
|---|---:|---:|
| **Vlaanderen** | ~3.1–3.7% (2% + notary Jbis); ~4.1–4.7% for compromis from 1 Jan 2027 (3%, decree pending) | ~13.1–13.8% (12% + notary J) |
| **Wallonie** | ~4.1–4.7% (3% + notary Jbis) | ~13.6–14.3% (12.5% + notary J) |
| **Bruxelles** | ~7.3% at €400k, ~9.1% at €600k with the abattement (duty alone: 6.25% at €400k, 8.33% at €600k; no abattement above €600k) | ~13.6–14.3% (12.5% + notary J) |

Computed at €400,000–€200,000 unless stated (2026 data): registration duty + notary costs as above (honoraria under barème Jbis or J + €855 flat fee, + 21% VAT). Excludes individualisable disbursements and any mortgage deed, so the real total is higher.

### Capital gains

- **Own-home sale**: exempt if it was the seller's own home for ≥12 uninterrupted months right before the month of sale (2026 data, source fin.belgium.be — explications déclaration 2026)
- **Buildings held >5 yrs**: exempt — taxable only if sold within 5 yrs of a purchase for value (new builds: construction started within 5 yrs of buying the land and the whole sold within 5 yrs of first occupation or letting) (2026 data, source fin.belgium.be)
- **Buildings sold within 5 yrs**: **16.5%** (+ communal surcharges) (source notaire.be 'Taxes sur les plus-values immobilières', undated page; same rate in SPF Finances Mémento fiscal 2017 — rates/figures may have changed since; verify the current CIR 92 text with SPF Finances, Fisconetplus). The 10% capital-gains tax in force from 1 Jan 2026 covers financial assets, not real estate (loi du 6 avril 2026 introduisant un impôt sur les plus-values sur les actifs financiers, Moniteur belge 21 Apr 2026, effective 1 Jan 2026 per its art. 35 — source ejustice.just.fgov.be)
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
- **Bruxelles Code bruxellois du logement** — regional lease rules in force since 1 Jan 2018 (ordonnance 27 Jul 2017), amended by the ordonnance of 4 Apr 2024 (in force 1 Nov 2024; some changes apply only to leases signed or renewed from that date); regional lease registration on Irisrent since 1 Jan 2025 (ordonnance 25 Apr 2024), for leases signed from that date and older ones not yet registered on MyRent; the Cour constitutionnelle (3 Apr 2025) annulled the provision that made the regional register the only one, so landlords must register on both Irisrent and the federal MyRent (2026 data, source be.brussels 'Enregistrement bail d'habitation', lease brochure Jan 2025 + Bruxelles Logement activity report 2025)
- Tenant rights moderate (less strict than DE/AT)

### Short-let (Airbnb / hébergement touristique)

**Three regional regimes**:

#### Bruxelles-Capitale

- **Prior registration** with **Bruxelles Économie et Emploi** is required before any paid tourist let of 1 night to 90 days, for individuals and companies alike, the host's own main residence included; operating unregistered is illegal (2026 data, source economie-emploi.brussels host pages and FAQ)
- The registration file needs an urban-planning attestation from the commune's urbanisme service (every category, the host's main residence included), a fire attestation from the mayor, renewed every 5 years (a simplified-check attestation when the operator runs fewer than 6 tourist accommodations at once and all tourist accommodation in the building together takes fewer than 10 guests, otherwise a fire-safety attestation) and, in a copropriété, the general assembly's written consent; the registration number is tied to one operator and one address, so a buyer must apply for a new one; administrative fines €416–€41,600 (décimes additionnels included) for offences found from 1 Feb 2026 (2026 data, source economie-emploi.brussels host pages and FAQ)
- **Ordonnance of 1 Feb 2024** on tourist accommodation repeals and replaces the 2014 ordonnance once in force; its entry-into-force date is left to the Government (art. 45, etaamb.openjustice.be) — verify at economie-emploi.brussels which regime applies on the purchase date
- **EU Reg 2024/1028** is a directly applicable regulation, applying since 20 May 2026 — nothing to transpose; Member States are not obliged to apply it, but any registration scheme or platform-data request must go through it (2026 data, source European Commission DG GROW, 20 May 2026)

#### Wallonie

- **Code wallon du Tourisme (CWT)** — décret of 8 Feb 2024 + arrêté of 16 May 2024, in force 1 Jul 2025: every hébergement touristique must be **registered with Tourisme Wallonie**; registration replaced the declaration duty in force since 2017 (2026 data, source Data Protection Authority opinion 113/2026 of 4 Jun 2026; entry into force on 1 Jul 2025 set by the arrêté of 16 May 2024 — wallex.wallonie.be); accommodation declared on 1 Jul 2025 is deemed registered without a new application as long as its fire-safety or simplified-check attestation is still valid, and attestations issued under the old code stay valid until they expire (2026 data, source decree of 8 Feb 2024 art. 22 as amended by the decree of 30 May 2025, consolidated text on wallex.wallonie.be)
- Registration needs a fire-safety attestation (ASI, issued by the mayor, valid 5 years) or, where applicable, a simplified-check attestation (ACS), plus a criminal-record extract under 6 months old; Tourisme Wallonie gives each accommodation a unique registration number, whose proof must be displayed (2026 data, source CWT art. D.III.21–D.III.24 and D.III.73–D.III.74, consolidated text on wallex.wallonie.be; wallonie.be 'Créer et gérer un hébergement touristique'); platforms such as Airbnb and Booking.com ask for the number (CPDT/IGEAT methodological note, Dec 2024). Since 2023 the Walloon planning code also requires some tourist accommodation to obtain an urban-planning permit from the commune (2026 data, source wallonie.be)
- **Pending**: an avant-projet de décret aligning the CWT with EU Reg 2024/1028 (immediate registration with ex-post checks, platform verification of numbers, activity data to Tourisme Wallonie) was before the Data Protection Authority in Jun 2026; not in the consolidated CWT on wallex.wallonie.be on 2026-11-04 (version in force from 1 Sep 2026, last amended by the decree of 18 Jun 2026, with no reference to EU Reg 2024/1028) — verify adoption at wallex.wallonie.be

#### Vlaanderen

- **Logiesdecreet** (decree of 5 Feb 2016, applicable since 1 Apr 2017) — **aanmelding** (registration) at **Toerisme Vlaanderen** is mandatory and gives a unique registration number, which booking platforms ask for (2026 data, source Vlaanderen Vakantieland / Toerisme Vlaanderen, updated 19 Aug 2026)
- **Brandveiligheidsattest** + fire and civil-liability insurance required; **erkenning** (recognition) and comfort classification are voluntary (2026 data, source Flemish Government memorie van toelichting VR 2026 2905 DOC.0530/3; Vlaanderen Vakantieland)
- **EU Reg 2024/1028** (applies since 20 May 2026; a regulation, not a directive): the Logiesdecreet amendment naming Toerisme Vlaanderen as competent authority and setting sanctions got final Flemish Government approval and was sent to the Vlaams Parlement on 17 Jul 2026; the minister ties enforceability to that decree plus a central digital entry point, both expected in force in 2026 (2026 data, source answer to Vlaams Parlement written question 482 of 4 Jun 2026; vlaanderen.be government decision of 17 Jul 2026) — verify adoption at vlaamsparlement.be

### Tax on rental

- **Residential rental to a private tenant who does not use it professionally**: taxed on indexed RC/KI × 1.40, not on the rent received, at the progressive income-tax rates; often substantially below market — **major tax-optimization advantage**; indexation coefficient 2.2446 for 2025 income (tax year 2026) and 2.3000 for 2026 income (2026 data, source SPF Finances 'Kadastraal inkomen: wat en waarvoor', fin.belgium.be, archived 2026-05-10; × 1.40 formula: SPF Finances 'Verhuur aan een persoon die het goed niet voor het beroep gebruikt', archived 2025-10-03 — rates/figures may have changed since)
- **Furnished let** (private tenant, outside a professional activity): the building is taxed as above; the furniture share is movable income — 40% of the total rent unless the lease sets another split, minus a 50% flat cost deduction (or actual costs, interest excluded), taxed at 30% in principle (2025 data, source SPF Finances 'Verhuur aan een persoon die het goed niet voor het beroep gebruikt', fin.belgium.be, archived 2025-10-03 — rates/figures may have changed since)
- **Professional tenant / company**: taxed on the higher of (a) gross rent minus a 40% flat cost deduction, the deduction capped at 2/3 × non-indexed RC/KI × revalorisation coefficient (5.63 for 2025 income, 5.75 for 2026 income), and (b) indexed RC/KI × 1.40 (2026 data, source SPF Finances 'Verhuur aan een persoon die het goed voor het beroep gebruikt of aan een rechtspersoon of vereniging', fin.belgium.be, archived 2026-05-17), at progressive rates (SPF Finances 'Verhuur aan een persoon die het goed niet voor het beroep gebruikt', archived 2025-10-03)
- **Short-let**: VAT on furnished accommodation let for less than 3 months in hotels and similar establishments that provide at least one hotel-type service (physical reception of guests, bed linen, daily breakfast) rose from **6% to 12% on 1 Mar 2026** (2026 data, source arrêté royal of 14 Feb 2026, Moniteur belge 23 Feb 2026, p. 9168 — ejustice.just.fgov.be). Income tax for a private host letting outside a professional activity: KI-based property income on the let part (pro rata to the area and days let) + movable income on the furniture share (as above) + miscellaneous income, taxed at 33% in principle, on paid extra services such as cleaning or breakfast; letting with services through a recognised sharing-economy platform may fall under the sharing-economy regime, and regular, professionally organised letting is taxed as professional income (2025 data, source SPF Finances 'Verhuur aan een persoon die het goed niet voor het beroep gebruikt', fin.belgium.be, archived 2025-10-03 — rates/figures may have changed since; verify with an accountant)

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
| **SPW ARNE — carte de l'aléa d'inondation** | `https://environnement.wallonie.be/home/gestion-environnementale/risques-climatiques/inondations/urbanisme/cartes-inondations/carte-alea-inondation.html` | Wallonie reference flood-hazard map (river overflow + runoff axes); approved by the Gouvernement wallon 4 Mar 2021, rolling revision decided 17 Apr 2025; high-hazard zones = insurance 'zones à risques' (source: environnement.wallonie.be) |
| **OVAM** (Vlaanderen bodempolluties) | `https://ovam.vlaanderen.be/` (updated 2026-10-23; `ovam.be` redirects) | Soil pollution, bodemattest, asbestattest Vlaanderen |
| **Bruxelles Environnement** | `https://environnement.brussels/` | Bruxelles env data |
| **IRM (Institut Royal Météorologique)** | `https://www.meteo.be/` | Climate, weather |
| **AwAC** Wallonie air quality | `https://www.awac.be/` | Wallonie air |
| **VMM** Vlaamse Milieumaatschappij | `https://vmm.vlaanderen.be/` (updated 2026-10-23; `vmm.be` redirects) | Vlaanderen environment, sewer and treatment indicators |
| **CELINE** | `https://www.irceline.be/fr` | National air quality |
| **Waterinfo — informatieplicht** | `https://www.waterinfo.be/informatieplicht` | Vlaanderen flood report per parcel: P-score (perceel) + G-score (gebouw) (source: integraalwaterbeleid.be) |

### Specific risks

- **Inondation / overstroming (flooding)** — major risk:
  - July 2021 catastrophic floods (Wallonie): 39 dead (per police), 209 of 262 Walloon communes hit, nearly 48,000 buildings (of which 45,000 dwellings) affected, cost to the Région wallonne €2.8bn at that stage (2022 data, source Gouvernement wallon communiqué 4 Jul 2022 — rates/figures may have changed since); insured damage est. €2.4bn at 31 Dec 2022 (2022 data, source Assuralia, insurers' federation — industry source — rates/figures may have changed since); Liège, Verviers, Pepinster, Theux
  - Vesdre, Meuse, Ourthe basins
  - Flood-risk plans: Wallonie **PGRI 2022-2027** (Plans de Gestion des Risques d'Inondation, approved by the Gouvernement wallon 19 Jan 2023; source environnement.wallonie.be); Vlaanderen overstromingsrisicobeheerplannen are integrated in the **stroomgebiedbeheerplannen 2022-2027** (adopted by the Vlaamse Regering 1 Jul 2022; source publicaties.vlaanderen.be)
- **Bodemverontreiniging / pollution du sol**: check the parcel in each region's register. Vlaanderen: on average 20% of risicogronden given a first oriënterend bodemonderzoek need a beschrijvend onderzoek, and about half of those then need remediation; typical risk sites include a large heating-oil tank, a garage workshop, a petrol station, a dry cleaner or a former gasworks (source: OVAM, ovam.vlaanderen.be/risicogronden, page undated). Wallonie: the BDES lists 46,888 'pêche' parcels subject to Décret sols obligations — in most cases because of an environmental permit for a soil-risk activity, so not necessarily polluted — of which 17,786 in Hainaut and 12,484 in Liège province (37.9% and 26.6%, computed: 17,786 / 46,888 and 12,484 / 46,888) (2026 data, source SPW ARNE BDES parcel list on ODWB, data processed 11 Mar 2026; colour meaning per environnement.wallonie.be). Bruxelles: inventaire de l'état du sol in 5 categories, searchable by address (source: environnement.brussels)
- **Aardbeving / séisme**: low-moderate (Roer Valley Graben); 13 Apr 1992 Roermond (NL) ML 5.8, intensity VII, and 8 Nov 1983 Liège ML 5.0, intensity VII (sources: KNMI, knmi.nl 'Zwaarste aardbeving in Nederland 30 jaar geleden', 13 Apr 2022 — 5.8 on the Richter scale, intensity just over VII; Observatoire royal de Belgique, astro.oma.be 'Commemoration of the Liège 1983 earthquake', 7 Nov 2023 — local magnitude 5.0, EMS-98 intensity VII); USGS catalogue: Roermond Mw 5.4, Liège mb 5.0 (source: earthquake.usgs.gov events usp00055q3 and usp0001zn0)
- **Mijnverzakkingen** (mining subsidence): Limburg (coal), Wallonie (Borinage); historic — in Wallonie the DRIGM subsoil information sheet covers mine shafts, karst, landslides and underground quarries per parcel (see Mandatory at sale)
- **Asbestos**: broad Belgian ban 1998, complete ban by arrêté royal 23 Oct 2001 in force 1 Jan 2002 (source: SPF Emploi, emploi.belgique.be); buildings built before 2001 are the risk construction years for the Flemish asbestattest (source: OVAM)
- **Loodleidingen** (lead pipes) — homes built before 1970 may still have lead plumbing; drinking-water limit 10 µg lead per litre since end 2013 (source: De Watergroep, dewatergroep.be); in Bruxelles no distribution main is lead but a small share of old lead service connections remains (source: vivaqua.be)
- **Charleroi–Mons–Liège industrial axis**: the communes with the most BDES 'pêche' parcels are Charleroi (1,888), Mons (1,654) and Liège (1,458) (2026 data, source SPW ARNE BDES parcel list on ODWB) — raw commune counts, not adjusted for commune size and not a statement about any single parcel. The highest cadmium concentrations in Walloon soils result mainly from historical atmospheric fallout, notably from non-ferrous metallurgy (zinc, lead, cadmium); most agricultural parcels are below 0.5 mg/kg outside historically impacted zones; probable-cadmium map for agricultural and forest topsoil (top 30 cm, 100 m grid) on the Géoportail de la Wallonie (source: environnement.wallonie.be, 8 Apr 2026)
- **Klimaatverandering**: +0.7 to +5 °C by end of century vs 1961-1990, depending on scenario (source: IRM/KMI meteo.be, CORDEX.be ALARO model); markedly wetter winters (climat.be: up to +22% by 2100); for summer the IRM model gives on average no or only a slight decrease (RCP8.5), while climat.be cites down to −25% by 2100 — the two federal sources differ, both shown (sources: meteo.be; climat.be, SPF Santé — Changements climatiques); see Climate change projections

### Build-era hazards

Curated wisdom, not data, except where a source is named.

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, damp; any asbestos cement is a later addition (process patented 1900; Eternit factories in Belgium by 1910 — secondary: Wikipedia 'Ludwig Hatschek' ⚠️) |
| **1900–1945** | Asbestos common, lead, weak insulation |
| **1945–1990** | Asbestos very common (broad ban 1998, complete ban 1 Jan 2002 — source SPF Emploi); cuves à mazout (oil tanks) |
| **1990s+** | Improved insulation; energy-performance requirements for permit applications from 1 Jan 2006 in Vlaanderen (source: vlaanderen.be EPB page) and 2 Jul 2008 in Bruxelles (source: Bruxelles Environnement fiche 'Exigences PEB 2008-2014'); Wallonie transitional PEB phase from 1 Sep 2008, second phase from 1 May 2010 (secondary: CMS Belgium article on lexgo.be, 31 May 2010 ⚠️) |
| **2021+** | Near-zero-energy new builds by permit-application year: BEN (max E30) in Vlaanderen, Q-ZEN in Wallonie (sources: publicaties.vlaanderen.be EPB-eisen 2026 brochure; energie.wallonie.be Q-ZEN guide 2026) |

### Mandatory at sale

| Document | Region | Required because | Validity |
|---|---|---|---|
| **PEB** (FR) / **EPC** (NL) | All | Energy cert (Bruxelles: required before marketing any dwelling >18 m²; source environnement.brussels) | 10 years maximum (Wallonie: required before a dwelling is put up for sale or rent, indicators in every advert; source wallonie.be démarche n° 2606, 2026. Vlaanderen: at sale or any other notarial transfer the EPC must be one drawn up from 2019 onward, an older one has to be renewed; source vlaanderen.be, 2026) |
| **Bodemattest** | Vlaanderen | OVAM soil certificate, required before the compromis for every land transfer; a risicogrond also needs an oriënterend bodemonderzoek (source: ovam.vlaanderen.be) | At sale (sale BLOCKED without it) |
| **Asbestattest** | Vlaanderen | Mandatory since **23 Nov 2022** for sales of buildings built before 2001; VME common parts by 2027; every pre-2001 building by 2032 (source: OVAM, ovam.vlaanderen.be/asbestattest) | 10 years standard, shorter if high-risk asbestos is present (source: OVAM) |
| **Overstromingsrapport / waterparagraaf** (P-score + G-score) | Vlaanderen | Flood-sensitivity information duty in adverts, compromis and deed (sale, lease >9 yrs, erfpacht / opstal); amended regime in force 1 Jan 2023 (source: integraalwaterbeleid.be, CIW) | Per transaction (report from waterinfo.be/informatieplicht) |
| **Attestation du sol / bodemcertificaat** | Bruxelles | Mandatory to sell land (Bruxelles Environnement); base fee €48, indexed every 2 years, next indexation 2027 (2025 data, source environnement.brussels page dated 27 Mar 2025 — rates/figures may have changed since) | At sale |
| **Extrait conforme BDES** (Banque de Données de l'État des Sols) | Wallonie | Required for land sales since 1 Jan 2019 (Décret sols art. 31); first extract €30, +€10 per extra parcel, capped at €320 (source: environnement.wallonie.be) | Up to 1 year for a notarial deed; void earlier if the parcel's BDES data change |
| **Contrôle électrique** (RGIE) | All | At sale of a dwelling, for installations that had no (complete) conformity examination after 1 Oct 1981; if infractions are found the buyer has 18 months from the deed to fix them and have a new inspection (source: SPF Economie, economie.fgov.be) | Periodic inspection every 25 years after a conformity check (source: SPF Economie) |
| **Citerne mazout / stookolietank** | All (rules differ by region) | Vlaanderen: no inspection certificate required at sale, but the latest inspection certificates and reports must be available to show; a tank under 6,000 L is inspected every 5 years if underground, and since 1 Mar 2009 only at installation if above ground (source: vlaanderen.be). Wallonie: 3,000–24,999 L is a classe 3 establishment (declaration + periodic inspection by an approved technician, AGW 17 Jul 2003), 25,000 L and more needs an environmental permit, and an unproven capacity counts as over 3,000 L (source: wallonie.be démarche n° 2514, 2026). Bruxelles: declaration for a buried tank up to 10,000 L or an above-ground tank of 3,000–10,000 L, environmental permit above 10,000 L (source: environnement.brussels, page dated 2 May 2022) | Wallonie, tanks of 3,000 L and more (and smaller ones in a drinking-water catchment prevention zone): leak test every 3 years (single wall) or 10 years (double protection) (source: environnement.wallonie.be 'Une citerne en règle'); Vlaanderen by volume and placement (see left) |
| **Fiche d'Informations du Sous-sol** (DRIGM, SPW ARNE) | Wallonie | Karst, landslide, mine-shaft, underground-quarry and Seveso major-accident information; the seller's notary must provide the available information at sale; free (source: wallonie.be démarche) | 6 months |

### Climate change projections

- +0.7 to +5 °C by end of century vs 1961-1990, depending on emissions scenario (RCP2.6 to RCP8.5); single-model estimate (source: IRM/KMI meteo.be 'Le climat à l'horizon 2100', CORDEX.be ALARO model)
- Precipitation seasonality: markedly wetter winters (climat.be: up to +22% by 2100); for summer the IRM model gives on average no or only a slight decrease (RCP8.5, end of century), while climat.be cites down to −25% by 2100 — the two federal sources differ, both shown (sources: meteo.be; climat.be, SPF Santé — Changements climatiques)
- More frequent and more intense heavy winter rain and violent summer storms, raising flood risk (source: climat.be) — Vesdre 2021 type
- Sea level: storm-surge level at the Belgian coast +30 cm by 2050 and +80 cm by 2100 in the VMM middle scenario; the Flemish long-term Kustvisie even takes a 3 m sea-level-rise scenario into account (source: VMM, vmm.vlaanderen.be stijging zeewaterspiegel)

---

## Section: `--mains`

### Sources

- **SWDE** (Société wallonne des eaux): `https://www.swde.be/` — Wallonie water
- **in BW** (Brabant wallon; the former IECBW domain `iecbw.be` is parked, checked 2026-10-23): `https://www.inbw.be/` — drinking-water production and distribution plus wastewater treatment in Brabant wallon (source: inbw.be)
- **IDEA** (agence de développement territorial des 27 communes du Cœur du Hainaut, Mons; water among its missions — source: idea.be)
- **CILE** (Compagnie Intercommunale Liégeoise des Eaux): `https://www.cile.be/` — drinking-water distributor in 24 communes of the province of Liège (source: cile.be)
- **De Watergroep**, **Farys**, **Pidpa**, **Water-link**, **Aquaduin**, **AGSO Knokke-Heist** — Vlaanderen drinking-water companies (2026 data, source VMM Waterregulator, vmm.vlaanderen.be)
- **Vivaqua**: `https://www.vivaqua.be/` — Bruxelles drinking-water distribution and maintenance of the regional sewer network (source: vivaqua.be)
- **Aquafin** (Vlaanderen wastewater): `https://www.aquafin.be/`

### Verification

- Bruxelles: every wastewater producer must connect to the sewer; the commune can exempt a building only where connection is not technically or economically feasible, and an individual treatment system is then required; treatment plants Nord (since 2006) and Sud (since 2000) (source: environnement.brussels, page dated 8 Nov 2023)
- Wallonie: about 180,000 dwellings — nearly 12% of Walloons potentially concerned — lie in a zone d'assainissement autonome, where a new dwelling must have an individual treatment system (SEI) instead of a sewer connection (2019 data, source État de l'environnement wallon fiche EAU 20 citing the PASH — rates/figures may have changed since)
- Vlaanderen: 94.2% of inhabitants connected to sewer (rioleringsgraad, Apr 2026); 88.6% collectively treated (zuiveringsgraad, end 2024); about 2% of residents live where an IBA (individual treatment unit) is required (2026 data, source VMM, vmm.vlaanderen.be indicator zuiveringsgraad)
- Wallonie: collective treatment-plant equipment rate 92.5% at 31 Dec 2023 (459 stations, 4,127,033 population-equivalent capacity) — a capacity-vs-target measure, not the share of homes on sewer (2023 data, source IWEPS fiche A009 citing SPGE — rates/figures may have changed since)

### Costs

| Scenario | Cost (€) |
|---|---:|
| Aansluiting riool — Vlaanderen, Fluvius areas (Fluvius Antwerpen, Limburg, West, Riobra) | standard connection: 1,144.25 incl. 21% VAT flat commissioning fee; complex connection (diam. 200): 1,896.59 incl. 21% VAT base fee plus trench reinstatement 187.44–458.76 per m in the roadway (2026 data, source Fluvius 'Aansluitingstarieven Riolering 2026') |
| Aansluiting riool / raccordement égout — all-in incl. works on the plot, other operators | est. 6,000–15,000 — unsourced contractor-quote range, order of magnitude only; works on the plot are not in the Fluvius tariff sheet; get the local sewer operator's tariff and contractor quotes |
| IBA — Vlaanderen, Fluvius areas | household IBA where no sewer will come (individueel te optimaliseren buitengebied): supplied and installed at the standard-connection fee, 1,144.25 incl. 21% VAT; IBA for a single-family house in collectief te optimaliseren buitengebied: 8,093.53 incl. 21% VAT (2026 data, source Fluvius 'Aansluitingstarieven Riolering 2026') |
| Septique / IBA / SEI installation — elsewhere | est. 8,000–15,000 — unsourced contractor-quote range; the Fluvius collectief-buitengebied fee above sits at its low end; in Wallonie an installation or rehabilitation prime exists under the SPGE's GPAA scheme (source: wallonie.be GPAA démarche, updated 23 Jul 2026) |
| Cuve mazout removal | est. 1,500–4,000 — unsourced contractor-quote range, no published tariff; depends on volume, underground vs above ground and extraction vs neutralisation in place |

---

## Cost benchmarks (BE 2026) — est. ranges, verify with contractor quotes

| Work | Cost (€) |
|---|---:|
| PEB / EPC | ~150–350 est. (no fixed price in Vlaanderen — set by the energy expert, source vlaanderen.be EPC page; range not from a price source — compare quotes) |
| Asbestattest (Vlaanderen) | ~350–600 est. (no legal price — set by the certified asbestos expert; includes the €59 OVAM retributie since 5 Feb 2025, source vlaanderen.be; range not from a price source — compare quotes) |
| Bodemattest (Vlaanderen) | 73.05 per full parcel; 275.05 per part of a parcel (since 1 Jan 2026, source vlaanderen.be) |
| Notaris fees | own and only home (barème Jbis): ~€3,370 at €200,000 (1.7%), ~€3,840 at €300,000 (1.3%), ~€4,210 at €400,000 (1.05%) — computed: honoraria + €855 flat fee + 21% VAT (2026 tariff, source notaire.be); disbursements extra |
| Registration duties (primary, Vlaanderen) | 2% (since 1 Jan 2025); 3% for compromis from 1 Jan 2027 (decree pending) |
| Registration duties (primary, Wallonie) | 3% (since 1 Jan 2025) |
| Registration duties (Bruxelles) | 12.5% (first €200,000 exempt for an own home priced ≤ €600,000) |
| **Total transaction cost (Vlaanderen primary)** | **~3.1–3.7%** at €400k–€200k (~4.1–4.7% for compromis from 1 Jan 2027, decree pending) — computed, excl. disbursements |
| **Total transaction cost (Wallonie primary)** | **~4.1–4.7%** at €400k–€200k — computed, excl. disbursements |
| **Total transaction cost (Bruxelles primary)** | **~7.3–9.1%** at €400k–€600k with abattement — computed, excl. disbursements |
| **Total transaction cost (second home)** | **~13.1–14.3%** at €400k–€200k (12% / 12.5% duty + notary barème J) — computed, excl. disbursements |
| Septic to mains | ~6,000–15,000 est. (contractor range, not from a price source — get ≥3 quotes) |
| Cuve mazout removal | ~1,500–4,000 est. (contractor range, not from a price source — get ≥3 quotes) |
| Roof renovation | ~15,000–30,000 est. (contractor range, not from a price source — get ≥3 quotes) |
| Asbestos removal | ~1,000–10,000 est. (contractor range, not from a price source; for a given property in Vlaanderen, OVAM's prijsramingstool gives a price fork from the asbestattest data — ovam.vlaanderen.be/asbest-prijsramingstool) |
| Energy retrofit (Class C → A) | ~25,000–60,000 est. (contractor range, not from a price source — get ≥3 quotes) |

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
| OVAM Vlaanderen | `https://ovam.vlaanderen.be/` (updated 2026-10-23) |
| Bruxelles Environnement | `https://environnement.brussels/` |
| Immoweb | `https://www.immoweb.be/` |
| Vlaams Verkeerscentrum traffic data | `https://www.verkeerscentrum.be/data` (replaces `mobiliteit.vlaanderen.be`, which now redirects to `mobielvlaanderen.be`; updated 2026-10-23) |
| SPW Mobilité | `https://mobilite.wallonie.be/` |
| Bruxelles Mobilité open data | `https://data.mobility.brussels/` |
| Waterinfo flood report (Vlaanderen) | `https://www.waterinfo.be/informatieplicht` |
| Wallonie flood-hazard map | `https://environnement.wallonie.be/home/gestion-environnementale/risques-climatiques/inondations/urbanisme/cartes-inondations/carte-alea-inondation.html` |

## Status

✅ Fast-changing sections re-verified as of 2026-10-23; each section's date is in the Per-section verification table.

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax (3 régions), rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for `--price` (benchmark table rebuilt from Statbel H1 2026 medians, Statistiek Vlaanderen 2025 and the Fednot barometer of 13 Oct 2026). HIGH for the registration-duty rates in force (Vlaanderen 2% and Wallonie 3% since 1 Jan 2025; Bruxelles 12.5% with the €200,000 abattement — vlaanderen.be, wallonie.be, be.brussels), the asbestattest mandate (23 Nov 2022, Vlaanderen — vlaanderen.be, OVAM) and the July 2021 flood figures (Gouvernement wallon communiqué of 4 Jul 2022). MEDIUM for the Vlaanderen return to 3% for compromis from 1 Jan 2027 (VLABEL SP 26021 of 1 Oct 2026, onder voorbehoud of the decree, which is pending). MEDIUM for `--work` (VAT franchise, INASTI and PIT 2026 bands re-verified; salary figures are Statbel 2022 and SD Worx Jan 2026, secondary). MEDIUM for `--rental`: lease law, the three short-let regimes and the rental-tax rules rest on primary sources (SPF Finances rental-tax pages read in archived copies of 2025-10-03, 2026-05-10 and 2026-05-17; short-let VAT in the arrêté royal of 14 Feb 2026), but neither the Bruxelles ordonnance of 1 Feb 2024 nor the Flemish and Walloon texts implementing EU Reg 2024/1028 (an EU regulation applying since 20 May 2026, not a directive to transpose) are confirmed in force. MEDIUM for `--risks`: source tables, flood, seismic (KNMI, Observatoire royal de Belgique), asbestos, lead and mandatory-at-sale rows re-sourced, the soil-pollution bullets rebuilt on OVAM and SPW ARNE BDES data (province and commune counts, not parcel-level), the citerne mazout row set out per région and Wallonie PEB validity confirmed on wallonie.be; the build-era rows are curated wisdom except where a source is named, and the 'low-moderate' seismic label and the mining-subsidence bullet are qualitative. MEDIUM for `--mains`: coverage statements sourced (Bruxelles Environnement, SPW fiche EAU 20 with 2019 data, VMM, IWEPS) and Fluvius 2026 connection and IBA tariffs for the Fluvius areas. MEDIUM for précompte effective rates and bills per €1,000 of RC/KI (computed from the 2026 Vlaamse Belastingdienst opcentiemen, the 2026 Bruxelles centimes and, for Wallonie, the 2025 UVCW communal centimes (secondary) with the Hainaut and Liège provincial centimes; Namur, Luxembourg and Brabant wallon provincial centimes not sourced) and for the all-in transaction-cost totals (computed from the 2026 notary tariff, excl. disbursements). LOW for the 16.5% capital-gains rate on buildings (undated notaire.be page and the 2017 Mémento fiscal only) and every est. cost row (contractor works, PEB / EPC, asbestattest, and mains connection, IBA and tank-removal costs outside the Fluvius tariff).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-11-05 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--work=<profession>` | 2026-10-23 | 2026-11-05 maintenance run | INASTI contribution bands confirmed on inasti.be and in the SPF Sécurité sociale 2026 table. Statbel's beSTAT series still ends at 2022, so the monthly pay figures and their × 12 values stand. |
| `--tax` | 2026-10-23 | 2026-11-05 maintenance run | Walloon conditions and abolished reliefs checked against fin.belgium.be and the décret of 5 Dec 2024 on wallex.wallonie.be: the 5-year residence deadline also covers dwellings on plan or under construction, and the repeal of art. 46bis now rests on the decree itself. Total-cost rows recomputed from the notary tariff; the Flemish 3% stays pending, with the draft Programmadecreet given final government approval on 28 Oct 2026 and sent to the Vlaams Parlement. |
| `--rental` | 2026-10-23 | 2026-11-05 maintenance run | Brussels lease rules and double registration on Irisrent and MyRent confirmed on be.brussels and in the Bruxelles Logement 2025 activity report. The Code wallon du Tourisme and its pending EU alignment confirmed on wallex.wallonie.be and in Data Protection Authority opinion 113/2026. |
| `--risks` | 2026-10-23 | 2026-11-05 maintenance run | Soil figures confirmed at OVAM, the ODWB BDES dataset (46,888 parcels, data processed 11 Mar 2026) and environnement.brussels; earthquake figures at KNMI, the Royal Observatory of Belgium and USGS. Energy-certificate rules confirmed on environnement.brussels, wallonie.be and vlaanderen.be. |
| Cost benchmarks (BE 2026) — est. ranges, verify with contractor quotes | 2026-11-05 | 2026-11-05 maintenance run | Wallonie's 3% primary-home rate since 1 Jan 2025 confirmed on fin.belgium.be and in the décret of 5 Dec 2024 on wallex.wallonie.be. |
| `--traffic` | 2026-10-23 | 2026-10-23 refresh wave | Source URLs re-checked; MOW and Bruxelles Mobilité URLs replaced; TJM replaces the unattested PJM / GMD terms; verdict bands are skill thresholds |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Immoweb, Zimmo, Realo live; Logic-Immo folded into Zimmo; Vlan replaced by Immovlan |
| Active fiscal incentives | 2026-10-23 | 2026-10-23 refresh wave | Chèque-habitat, abattement + BE HOME, Mijn VerbouwLening 2026 and the Wallonie 1 Oct 2026 regime on primary sources; federal EE-loan ❌ DEPRECATED |
| Caveats unique to BE | 2026-10-23 | 2026-10-23 refresh wave | Legal / fiscal caveats only (2025 reform + 2027 Vlaanderen 3%, asbestattest, RC 1975 reference period, 2002 regionalisation); PEB, flood and VME caveats not re-verified |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | All 11 URLs checked; OVAM and MOW replaced; 3 rows added; cadastre URL content behind a captcha |
| `--mains` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |

## Extension TODOs

- [ ] Per-commune précompte / onroerende voorheffing rates table
- [ ] Asbestattest detailed inspection checklist
- [ ] PEB regulations per région timetable (FR / NL / DE versions)
- [ ] Logies / hébergement licensing per région (Logiesdecreet, CGT)
- [ ] Vesdre 2021 flood-affected zones (rebuilding rules)
- [ ] Bodemattest decision tree (clean/contaminated/in-progress)
- [ ] Per-commune renovation premium eligibility
- [ ] EU Reg 2024/1028 implementation tracker per région (registration schemes, platform data, single digital entry point; a regulation, not a directive)
- [ ] Brussels heritage building constraints per zone
- [ ] German-speaking Eastern Cantons specific rules

## Update history

- **2026-04-25** — Initial population
- **2026-05-01** — Statbel URL re-pointed (dead-URL repair)
- **2026-05-27** — Tier-1 corrections: précompte base rates (Wallonie 1.25%, Vlaanderen 3.97%, Bruxelles 1.25%), Vlaanderen 1 Jan 2026 own-home conditions, 12% rate dated to 2022, 6% VAT demolition-reconstruction regime
- **2026-05-29** — Anti-hallucination sweep: est. labels on précompte bills and cost benchmarks, VAT building-vs-land split, capital-gains caveats
- **2026-09-18** — BruGIS URL re-pointed
- **2026-10-23** — Refresh wave (market, tax-legal, risk-infra) plus audit findings, then a gap-closing pass (corrections re-checked 2026-11-03); playbook-level date not re-stamped because `--mains` stays open: its coverage statements and the Fluvius-area connection and IBA tariffs are now sourced, but connection, IBA and tank-removal costs elsewhere stay est. (no Farys or Vivaqua tariff sourced); `--tax`, `--rental`, `--risks` and Cost benchmarks were closed by the gap-closing pass
  - Re-verified (facts checked — changed / confirmed / unverifiable): `--price` 36 — 25 / 10 / 1; `--work` 12 — 6 / 6 / 0; `--traffic` 5 — 4 / 1 / 0; Common listing platforms 5 — 2 / 3 / 0; Active fiscal incentives 7 — 6 / 1 / 0; Caveats unique to BE 5 — 2 / 3 / 0 (legal / fiscal only); Source URL templates 11 — 2 / 9 / 0, plus 3 rows added
  - Refreshed, not re-verified: `--tax` 52 — 31 / 12 / 9; Cost benchmarks 15 — 6 / 2 / 7; `--rental` 16 — 14 / 1 / 0; `--risks` 33 — 20 / 7 / 6; climate projections (in `--risks`) 4 — 4 / 0 / 0; `--mains` 14 — 7 / 2 / 5; Country profile 6 — 1 / 2 / 3; Reddit / forum sources 8 — 1 / 5 / 2; Verification authorities 6 — 0 / 2 / 2 (rows unchanged)
  - Main changes: Statbel H1 2026 median price table replaces the unsourced ranges; Vlaanderen own-home duty back to 3% for compromis from 1 Jan 2027 (VLABEL SP 26021, decree pending); 2026 indexation coefficient 2.3000 and the Bruxelles agglomeration and communal centimes; BE HOME prime (€164 for 2026; €328 from 2027 announced, not enacted); short-let regimes of the three régions rewritten from primary sources, with EU Reg 2024/1028 described as a regulation in application since 20 May 2026 rather than a pending transposition; short-let VAT 6% → 12% on 1 Mar 2026; 565 communes; federal EE-loan ❌ DEPRECATED; CIRGT, Plan PARGI and CIGT entries replaced (not found in any source); IECBW replaced by in BW; mains cost rows labelled est.
  - Gap-closing pass (confirmed / changed / relabelled): `--rental` 6 / 2 / 1; `--tax` 8 / 4 / 1; Cost benchmarks 1 / 2 / 2; `--risks` 1 / 4 / 4 — closed; `--mains` 0 / 0 / 3 — patched, still open; total 16 / 12 / 11. Main changes: rental-tax rules re-sourced to SPF Finances (archived pages) and short-let VAT to the arrêté royal of 14 Feb 2026; Bruxelles and Wallonie short-let registration rules read on economie-emploi.brussels, the consolidated CWT and wallonie.be (Wallonie: fire-safety ASI or ACS plus a criminal-record extract); précompte effective rates recomputed from the 2026 Flemish opcentiemen and the Walloon communal and provincial centimes, the 'typical residential' bills replaced by computed bills per €1,000 of RC/KI and the Flemish reductions line corrected; notary fees and buyer-side totals recomputed from the 2026 notary tariff; soil-pollution bullets rebuilt on OVAM and SPW ARNE BDES data, seismic values re-sourced to KNMI and the Observatoire royal de Belgique, the citerne mazout row set out per région, the pre-1900 asbestos-cement and 1990s PEB rows corrected; `--mains` coverage bullets sourced and Fluvius 2026 connection and IBA tariffs added; PEB / EPC, asbestattest and contractor rows labelled est.
- **2026-11-04** — Maintenance run: closed `--price`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (BE 2026) — est. ranges, verify with contractor quotes; still open `--tax`. Playbook-level date now 2026-10-23.
- **2026-11-05** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (BE 2026) — est. ranges, verify with contractor quotes.
