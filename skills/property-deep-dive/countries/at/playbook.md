# Austria 🇦🇹 — Property Due-Diligence Playbook

ISO2: `at`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (PLZ)**: 4 digits (`1010` Wien Innere Stadt, `4020` Linz, `5020` Salzburg, `6020` Innsbruck)
- **Admin levels**: 9 Bundesländer → 95 Bezirke → 2,093 Gemeinden
- **Currency**: EUR (€)
- **Languages**: German (Hochdeutsch + dialects); minorities: Slovene (Kärnten), Hungarian (Burgenland), Croatian (Burgenland), Czech (Wien)
- **Cadastre**: **BEV (Bundesamt für Eich- und Vermessungswesen)** + **Grundbuch** (Justice ministry)
- **Identifier**: Einlagezahl (EZ) + Katastralgemeinde + Grundstücksnummer
- **CRITICAL**: Federal structure — most rules harmonized but **Wohnbauförderung + Naturschutz vary by Bundesland**
- Distinct ownership types: **Eigentum** (freehold), **Wohnungseigentum** (condominium under WEG 2002), **Mietkauf**, **Baurecht** (leasehold ground)

## Section: `--price`

### Primary sources

- **Statistik Austria Häuserpreisindex (HPI) + OOH PI**:
  - `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/haeuserpreisindex-und-ooh-pi`
  - Calculated from Grundbuch contracts; gold-standard
- **OeNB (Österreichische Nationalbank) Wohnimmobilienpreisindex**:
  - `https://www.oenb.at/Statistik/Standardisierte-Tabellen/Preise-Wettbewerbsfaehigkeit/immobilien/wohnimmobilienpreisindex.html`
  - Vienna-specific separate series
- **Statistik Austria Immobilien-Durchschnittspreise**:
  - `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/immobilien-durchschnittspreise`
- **Grundbuch (online via Justizportal)**:
  - `https://www.justiz.gv.at/home/service/grundbuch~36.de.html`
  - Paid abrufs (~€14 for Grundbuchauszug per EZ)

### Listing platforms

- **Willhaben.at** — largest: `https://www.willhaben.at/iad/immobilien`
- **ImmobilienScout24.at**: `https://www.immobilienscout24.at/`
- **derStandard Immo**: `https://immobilien.derstandard.at/`
- **Bazar.at**, **Quoka.at** — privates
- Premium: **EHL Immobilien**, **Engel & Völkers AT**, **JP Immobilien** Wien

### 2025 price benchmarks (Statistik Austria + OeNB)

| City / Area | Wohnungen €/m² (2024-2025) | Häuser €/m² |
|---|---:|---:|
| **Wien (Gesamt)** | ~5,000–6,500 | ~4,000–5,500 |
| Wien Innere Bezirke (1./4./7./8./9.) | 8,000–14,000 | n/a (kaum Häuser) |
| **Salzburg** | 5,500–7,500 | 4,500–6,000 |
| **Innsbruck** | 6,000–8,500 | 5,000–7,000 |
| **Graz** | 3,500–5,500 | 3,000–4,500 |
| **Linz** | 3,500–5,000 | 2,800–4,000 |
| **Klagenfurt** | 3,000–4,500 | 2,500–3,500 |
| **Bregenz** | 4,500–6,500 | 3,800–5,500 |
| Rural Bundesländer (NÖ, Burgenland, Kärnten) | 1,500–3,500 | 1,200–2,500 |

National averages 2024 (Statistik Austria):
- **Eigentumswohnung**: 4,000 €/m²
- **Einfamilienhaus**: 2,709 €/m²

### 2025 trend (OeNB)

- 2025 full year (OeNB, press release 29 Jan 2026): nominal **+2.1 % YoY**; real (vs 3.8 % inflation) **≈ −1.7 %** — prices fell in real terms again
- Wien **+2.9 %** vs Austria-ex-Wien **+1.6 %**; new Wien apartments +3.8 %, used +2.8 %
- OeNB Wohnimmobilienpreisindex **272.2 in Q1 2026 (record high)** — market stabilizing/recovering after 2022-24 correction (2026-07-03 verified)

### Compute

1. Listing €/m² = listing price / Wohnnutzfläche (per WEG/Wohnungsgemeinnützigkeitsgesetz)
2. **Trap**: Nutzfläche includes Lager, Keller — check what's counted
3. **Trap**: Quadratmeterpreis vs Pauschalpreis — Vienna Altbau often pauschal
4. Compare to Statistik Austria for the Bezirk
5. Grundbuchauszug needed for definitive ownership + encumbrances

---

## Section: `--traffic`

### Primary sources

- **ASFINAG** — autobahnen + Schnellstraßen: `https://www.asfinag.at/`
- **Bundesländer Verkehrszählung**:
  - Wien Stadtinformation: `https://www.wien.gv.at/`
  - Tirol: `https://www.tirol.gv.at/`
  - OÖ: `https://www.land-oberoesterreich.gv.at/`
  - Each Bundesland has Verkehrsabteilung
- OSM `highway` class fallback

### Key term

**JDTV (Jährlicher durchschnittlicher täglicher Verkehr)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (Wohnstraße, Forststraße)
- 🟡 1,000–8,000 v/d (Landesstraße, Stadtstraße)
- 🟠 8,000–30,000 v/d (Bundesstraße, Stadteinfahrt)
- 🔴 > 30,000 v/d (Autobahn, Schnellstraße, Stadtring)

---

## Section: `--tax`

### Annual property tax — Grundsteuer

**Very low** compared to W. Europe — residential **~€100–€500/yr est.** (derived from the Einheitswert × Steuermesszahl × Hebesatz formula below; verify on the seller's Grundsteuerbescheid).

```
Grundsteuer = Einheitswert × Steuermesszahl × Hebesatz × 1.4 (Bundeszuschlag)
```

- **Einheitswert**: very outdated valuation (mostly 1973 base) — est. ~5–20 % of market value
- **Steuermesszahl**: 0.05 % – 0.2 %
- **Hebesatz**: set by Gemeinde, ~500 % est.
- **Bundeszuschlag**: factor 1.4

### Reform pending

Long-debated Grundsteuerreform — multiple political parties want full revaluation. As of 2026: **not yet enacted**.

### Transaction taxes — Grunderwerbsteuer (GrESt)

**3.5 % flat on price** — same across Austria, no Bundesland variation (§ 7 GrEStG).

**Stufentarif** for *unentgeltliche* / Familienverband transfers (§ 7 Abs 1 Z 2 lit a GrEStG; family transfers within the § 26a Abs 1 Z 1 GGG circle count as unentgeltlich under § 7 Abs 1 Z 1 lit c; basis = **Grundstückswert**, not Kaufpreis) — 3-band scale:
- **0.5 %** on first **€250,000**
- **2.0 %** on next **€150,000** (€250k–€400k)
- **3.5 %** on excess above **€400,000**

(2026-05-27 verified; source [BMF Steuersatz](https://www.bmf.gv.at/themen/steuern/immobilien-grundstuecke/grunderwerbsteuer/steuersatz.html) + [USP GrESt](https://www.usp.gv.at/themen/steuern-finanzen/weitere-steuern-und-abgaben/grunderwerbsteuer.html))

**Share-deal RETT reform (Budgetbegleitgesetz 2025, BGBl I 25/2025; tax liability arising after 30 Jun 2025)**: two rules in § 1 Abs 3 GrEStG, now for partnerships AND corporations. (a) **Gesellschafterwechsel**: ≥ **75 %** of shares pass directly to new shareholders within **7 years** (old § 1 Abs 2a: partnerships only, 95 % within 5 years). (b) **Anteilsvereinigung / -übertragung**: direct or indirect (chain) unification or transfer of ≥ **75 %** (was 95 %) in one acquirer or acquirer group, no observation period. Rate (§ 7 Abs 1 Z 2 lit c): **3.5 % of gemeiner Wert only for an Immobiliengesellschaft** (§ 4 Abs 4: focus on selling, letting or managing land); all other share deals **0.5 % of Grundstückswert** (pre-reform 0.5 % for all). Relevant for SPV/GmbH structures. (2026-10-21 verified on [RIS GrEStG § 1 Abs 3 / § 4 Abs 4 / § 7](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004531); earlier source [DLA Piper](https://www.dlapiper.com/en-de/insights/publications/2025/06/new-regime-on-austrian-real-estate-transfer-tax) + [Wolf Theiss](https://www.wolftheiss.com/insights/austria-to-introduce-stricter-real-estate-transfer-tax-rules-for-share-deals/))

### Eintragungsgebühr (Grundbuch entry fee)

**1.1 % of price** — separate fee for Grundbuch registration.

**Hauptwohnsitz-Befreiung (Grundbuch-Eintragungsgebühr) — EXPIRED 30 Jun 2026.** Ran 1 Jul 2024 – 30 Jun 2026 (the Grundbuch application had to reach the court after 30 Jun 2024 but before 1 Jul 2026, § 25a Abs 2 Z 2 GGG; a later Rechtfertigung of a Vormerkung or a Pfandrecht in a Rangordnung applied for before 1 Jul 2026 stays covered, § 25a Abs 3; no exemption at all from a EUR 2 million Bemessungsgrundlage): Eintragungsgebühr (1.1 %) + Pfandrechts-Eintragungsgebühr (1.2 %) waived up to **€500,000 Bemessungsgrundlage** for a Hauptwohnsitz purchase. **No extension enacted** — §§ 25a-25c GGG ceased 1 Jul 2026 (Art VI Z 82 GGG) and the RIS consolidated GGG of 21 Oct 2026 (last amended by BGBl I 62/2026) has no replacement — the standard 1.1 % + 1.2 % fees (TP 9 lit b Z 1 and Z 4) now apply again. (2026-10-21 verified; source [RIS GGG](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002667) + [BMJ Befreiung](https://www.bmj.gv.at/themen/Zivilrecht/Befreiung-von-der-Grundbuch-Eintragungsgeb%C3%BChr-bei-Erwerb-von-Wohnraum.html))

### Immobilienertragsteuer (ImmoESt)

Special-rate income tax of **30 %** on private property-sale gains (since 1 Jan 2016; was 25 % between 1 Apr 2012 – 31 Dec 2015) — § 30 EStG. No 10-year speculation period since 1 Apr 2012. **Umwidmungszuschlag** (§ 30 Abs 6a EStG, sales after 30 Jun 2025): the gain on land rezoned after 31 Dec 2024 is raised by **30 %** (capped at the sale proceeds) before the 30 % rate, i.e. ≈ 39 % of the gain where the cap does not bind (computed: 30 % × 1.3). Hauptwohnsitzbefreiung (2-yr or 5-of-10-yr tests under § 30 Abs 2 Z 1 EStG) and Herstellerbefreiung are the main relief paths. Altgrundstück (not steuerverfangen on 31 Mar 2012, i.e. acquired before 31 Mar 2002) vs Neugrundstück split applies: for Altvermögen § 30 Abs 4 EStG taxes proceeds minus flat-rate acquisition costs of **86 %** (after rezoning since 1988: **40 %**), an effective 4.2 % / 18 % of proceeds. For **sales after 31 Dec 2026** the Budgetbegleitgesetz 2027-2028 (BGBl I 62/2026; § 124b Z 498 EStG) cuts these to **80 % / 30 %**, giving an effective **6.0 % / 21 %** of proceeds (computed: 30 % × 20 % / 30 % × 70 %). (2026-10-21 verified, RIS EStG § 30) Selbstberechnung durch Parteienvertreter (Notar/Anwalt). (2026-05-27 verified; source [oesterreich.gv.at ImmoESt](https://www.oesterreich.gv.at/de/themen/steuern_und_finanzen/immobilienertragsteuer/Seite.2420002) + [USP ImmoESt](https://www.usp.gv.at/themen/steuern-finanzen/weitere-steuern-und-abgaben/immobilienertragsteuer.html))

### Notarkosten / Anwaltskosten

- 1.0–2.5 % typical (regulated by RATG)

### Maklerprovision

- Typically 3 % buyer + 3 % seller (excl. VAT 20 %); since 1 Sep 2023, **Bestellerprinzip** in residential — usually paid by who hired

### Total transaction cost (buyer side)

- 3.5 % GrESt + 1.1 % Eintragung + 1.0–2.5 % Notar + 3.6 % Makler = **~9–11 %**

### VAT (USt.)

- 20 % standard
- 10 % reduced (food, books, residential rent)
- New residential property: 20 %; existing: exempt

### Future risk

- **Grundsteuerreform** likely 2026–2028 — could 5–10× annual bills for properties with low Einheitswert
- **Erbschaftsteuer** abolished 2008, but periodic political resurfacing of reintroduction debate
- **Wegzugsbesteuerung** for emigrants

---

## Section: `--rental`

### Long-term residential — MRG categories

**Mietrechtsgesetz (MRG)** divides rentals:
- **Vollanwendung** (full application): pre-1953 buildings, Genossenschaftswohnungen, Gemeindewohnungen → strict rent control + protection
- **Teilanwendung** (partial): post-1953 mostly → indexed rent, max-rent rules
- **Nichtanwendung** (no application): Eigentumswohnungen, single-family homes → free market

### Vienna-specific (most regulated)

- **Wiener Wohnen** (Gemeindewohnungen): ~220,000 units est., regulated rent (verify at wienerwohnen.at)
- **Genossenschaft** (cooperative): regulated rent + Eigenmittel
- **Privatmarkt** Vollanwendung: Richtwertmietzins per Bundesland, max +25 % zone bonus
- **2026 Richtwert Wien: €6.74/m²** (from €6.67, ~+1 % valorization eff. 1 Apr 2026), max +25 % zone bonus. **Mieten-Wertsicherungsgesetz (MieWeG), in force 1 Jan 2026** (via 5. Mietrechtliches Inflationslinderungsgesetz, 5. MILG): caps existing contractual Wertsicherungsklauseln (creates no adjustment right of its own) — regulated MRG rents capped at **1 % (2026), 2 % (2027)**; from 2028, index-linked residential contracts in multi-unit buildings incl. free-market rents pass on only half of any inflation portion above 3 % (e.g. 4.5 % inflation → max 3.75 %); adjustment once/yr, earliest 1 April (Richtwert increases effective 1 May). Excludes Ein-/Zweifamilienhäuser and WGG/Genossenschaft rents (own regime). (2026-07-03 verified)

### Short-term rentals (Ferienwohnung / Airbnb)

**Wien**:
- **Wiener Bauordnungsnovelle 2023** (short-let limits city-wide from 1 Jul 2024): max 90 days per calendar year for temporary short-let of a dwelling without giving up one's residence (legal persons cannot use the 90-day allowance); above that, outside a Wohnzone only with an Ausnahmebewilligung under § 129 Abs 1a BO limited to five years, inside a Wohnzone only as a Beherbergungsstätte after an Umwidmung under § 7a Abs 5 BO (2026 data, source MA 37 Merkblatt Kurzzeitvermietung + Stadt Wien press release 2026-09-19); registration number from 1 Jan 2027 under the Wiener register law passed by the Landtag on 20 Oct 2026 (not yet in the LGBl as of 2026-10-21 — see STR-VO note below); the same law narrows the 90-day allowance to one dwelling per host (MA 37 Merkblatt, Stand Oct 2026)
- WEG approval typically required
- Penalty: up to €50,000 (§ 135 Abs 1 BO); each repeated short-let offence at least €2,000 under the 20 Oct 2026 amendment (MA 37 Merkblatt, Stand Oct 2026 — not yet in the RIS consolidated text)

**Salzburg, Innsbruck**: similar restrictions

**EU 2024/1028 (STR-VO)**: opt-in in Austria — the Wirtschaftsministerium (BMWET) says each Bundesland decides whether and from when the STR-VO applies; **Tirol and Wien** are expected ("voraussichtlich") to create the legal, organisational and technical prerequisites and start implementation **during Q1 2027**, with host registration and platform data duties there from a date still to be set; BMWET names no Land where it already applies and is building the Single Digital Entry Point; no national STR registration-number regime. Substantive rules (Gewerbeordnung, Privatzimmervermietung, Raumordnung) stay untouched by the regulation in every Land. **Wien — law passed, not yet gazetted**: the Wiener Landtag passed on **20 Oct 2026** (SPÖ, NEOS, FPÖ and Grüne for, ÖVP against; no Begutachtung) the law amending the Bauordnung für Wien and setting up a Wiener Register für Kurzzeitvermietungen (announced 19 Sep 2026 as the WKVRG); no LGBl Wien publication on RIS as of 2026-10-21. Per Stadt Wien: register law in force **1 Jan 2027**; listings already online have until the **end of March 2027**; every unit registered separately and the number shown in every platform listing, even below 90 days; platforms must spot-check registrations, remove impermissible listings and pass information to the Magistrat; fines up to €50,000 per violation of the register law. Bauordnung side: each repeated short-let offence at least €2,000 (MA 37 Merkblatt, Stand Oct 2026); new § 7g BO — conversions into Beherbergungsstätten anywhere in Wien need at least 80 % of the building's Nutzflächen to stay residential, at least three Zimmereinheiten close together and a separate street entrance (only classic hotels exempt), applied to applications filed from 11 Oct 2026 (sources [Rathauskorrespondenz 2026-10-20](https://presse.wien.gv.at/presse/2026/10/20/15-wiener-landtag-14) + [Stadt Wien OTS 2026-10-20](https://www.ots.at/presseaussendung/OTS_20261020_OTS0019/verschaerftes-regulativ-fuer-kurzzeitvermietung-in-wien-stadt-wien-sichert-wohnraum-nachhaltig-ab); final wording to be checked in the LGBl). (2026-10-21 verified; source [BMWET STR-VO](https://www.bmwet.gv.at/Themen/Tourismus/kurzzeitvermietung.html))

### Tax treatment

- **§ 28 EStG (Vermietung & Verpachtung)** for non-commercial private rental
- **Gewerbliche Vermietung**: Gewerbesteuer + Sozialversicherung (SVS) if hotel-style services
- VAT: 10 % reduced for short-stay accommodation
- **Tourismusabgabe**: per night, set by Gemeinde (Wien ~€3.50/night/person)

---

## Section: `--work=<profession>`

### Job platforms

- **AMS (Arbeitsmarktservice)**: `https://www.ams.at/`
- **karriere.at**, **stepstone.at**, **LinkedIn AT**, **derStandard Karriere**
- **Bundeskanzleramt Karriere** (public sector): `https://www.bka.gv.at/`

### Self-employment regimes

- **Selbstständig (Gewerbeschein)**: standard self-employed; **SVS** (Sozialversicherung der Selbstständigen) mandatory
  - 2025 min. Beitragsgrundlage: ~€7,824/yr → ~€1,680/yr SVS minimum
- **Neue Selbstständige**: § 109a EStG, pension+health via SVS
- **Freier Beruf** (liberal): doctors, lawyers, architects — own Kammern + own Sozialversicherung
- **GmbH**: min €10,000 capital (paid up €5,000)
- **EPU (Einzelpersonenunternehmen)**: ~70 % of OE-Selbstständige
- **Pauschalierung**: simplified tax regime for small businesses

### Salary benchmarks (2025)

- Median monthly gross:
  - Wien: ~€3,800
  - Salzburg, Innsbruck: ~€3,600
  - Steiermark, OÖ, NÖ: ~€3,200
  - Burgenland, Kärnten: ~€2,900
- **Mindestkollektivvertragslöhne**: vary by branch, typical €1,800–€2,200 für Einsteiger

### Cultural quirks

- **13. + 14. Gehalt** standard (taxed at lower rate)
- **Kollektivvertrag** governs ~95 % of salaried jobs

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **HORA** (Natural Hazard Overview & Risk Assessment Austria) | `https://hora.gv.at/` | Flood (incl. Starkregen surface runoff), earthquake, landslides (Rutschungen), storm, lightning, hail, snow and, since 2026, heat — a HORA-Pass for any location; a screening tool, not parcel-sharp |
| **HORA 3D** (interactive) | from `https://hora.gv.at/` | 3D flood simulations, 30- to 300-year events, along almost 40,000 river km (since 2023) |
| **WISA Hochwasser-Risiko** | `https://maps.wisa.bmluk.gv.at/rmp2027/` | 3rd-cycle (RMP2027) Hochwassergefahren- und -risikokarten (hazard maps dated 17 Mar 2026 in the map app): Überflutungsflächen for HQ30 / HQ100 / HQ300 plus Wassertiefen and Fließgeschwindigkeiten; defences are designed to HQ100, so protected settlements show no HQ30 / HQ100 area, only HQ300 (the 2nd-cycle RMP2021 set stays online at `maps.wisa.bmluk.gv.at/gefahren-und-risikokarten-zweiter-zyklus`) |
| **AGES Radonkarte** | `https://geogis.ages.at/GEOGIS_RADON.html` | Radonschutzgebiet / Radonvorsorgegebiet status per Gemeinde (Radonschutzverordnung, BGBl II 470/2020) |
| **GeoSphere Austria** (formerly ZAMG + GBA) | `https://www.geosphere.at/` | Earthquake + climate + geology |
| **Naturgefahren-Bundesländer** | per state geoportal | Lawinen, Mure, Steinschlag |
| **OEROK-Atlas Hochwasserrisiko** | `https://www.oerok-atlas.at/` | Aggregated indicators |

### HORA — the gold standard

Austria's **HORA** is a free, all-hazards-in-one-place natural-hazard portal (EU comparison not re-verified; BMLUK calls it an internationally recognised flagship project). The Wasserministerium and the Versicherungsverband Österreich (VVO) started it as a public-private partnership shortly after the August 2002 Jahrhunderthochwasser; it went live in 2006 and is run by BMLUK with VVO. A HORA-Pass can be generated for any location in Austria. HORA 3D (2023) adds 3D flood simulations; the 2026 update added a heat layer (Hitzetage, Tropennächte, Hitzeepisoden on 1991–2020 normals), an updated Starkregen surface-runoff map (new hydrodynamic model; 100-year, 30-minute rain), a hail map (largest hailstones for 10-, 20- and 30-year return periods) and a revised earthquake map (peak ground acceleration with a 10 % chance of being exceeded in 50 years). **Not parcel-sharp**: BMLUK calls HORA a complement to the parcel-sharp Gefahrenzonenpläne, and the runoff map is a first estimate that does not replace detailed analysis (BMLUK HORA pages, read 2026-10-28).

### Specific risks

- **Hochwasser**: recurring; large-scale events in August 2002, June 2013 and 12–20 September 2024 (Vb-type weather; NÖ and Wien hit hardest, 300 to over 400 mm in five days between the Mostviertel and the Wienerwald, many river peaks far above a 100-year event; on the Kamp the 7 Aug 2002 peak was a 1,000- to 1,500-year event) (BMLUK Hydrographie, September 2024 event page); river list (Donau, Drau, Mur, Inn, Salzach) not re-verified
- **Lawinen** (avalanche): Tirol, Salzburg, Vorarlberg alpine — zoning through the Gefahrenzonenpläne of the Wildbach- und Lawinenverbauung (die.wildbach), built on a 150-year design event: **Rote Zone** where permanent use for settlement or traffic is not possible, or only at disproportionate cost; **Gelbe Zone** building only under conditions set by an expert opinion of the Gebietsbauleitung in the building procedure (BMLUK Gefahrenzonenplan page, read 2026-10-28)
- **Mure** (mudslides): alpine + Pre-alpine
- **Erdrutsch** (landslide): widespread in Voralpen + Alpen
- **Steinschlag** (rockfall): alpine slopes
- **Earthquakes** — moderate seismicity (GeoSphere Austria): about 70 quakes a year are felt, light building damage is expected about every two to three years and heavily damaging quakes about every 100 years; most quakes occur in the Rheintal (Vorarlberg), the Inntal and its side valleys, the Mur- und Mürztal, the Semmering area and the Wiener Becken:
  - **Wienerwald / Wiener Becken** (NÖ): 15 Sep 1590 Ried am Riederberg — intensities VIII and IX, reconstructed M 5.8; 8 Oct 1927 Schwadorf — intensity VIII; 16 Apr 1972 Seebenstein — M 5.3
  - **Mur-Mürz-Tal + Semmering** (Steiermark / NÖ): 1267 Kindberg (less well documented); 27 Oct 1964 Semmering — M 5.3
  - **Kärnten**: 4 Dec 1690 north of Villach — intensity VIII, reconstructed M 6.4, the highest magnitude in GeoSphere's list of documented Austrian quakes; 1201 Katschberg (less well documented)
  - **Tirol / Vorarlberg**: 17 Jul 1670 Hall in Tirol — intensity VIII; 7 Oct 1930 Namlos — M 5.3; Rheintal and Inntal are among GeoSphere's most active zones
  - Recent felt quake: Semmering, 1 Feb 2024, M 4.5 (GeoSphere Austria)
- **Hagel** (hail): increasing damage Süden + Westen (trend not re-verified against a primary source); HORA's 2026 hail map gives the largest hailstones for 10-, 20- and 30-year return periods per location
- **Sturm/Orkan**: Atlantic + Mediterranean depressions
- **Radon**: "Österreich weist eine der höchsten Radonbelastungen weltweit auf" (Austria has one of the highest radon burdens worldwide) and high indoor levels can occur anywhere (radon.gv.at). Reference level 300 Bq/m³ annual mean in living rooms (§ 3 Abs 1 Radonschutzverordnung, RnV, BGBl II 470/2020). **104 Gemeinden are Radonschutzgebiete** (RnV Anlage 1 A: 37 in OÖ, e.g. Bad Leonfelden, Bad Zell; 30 in NÖ, e.g. Arbesbach, Weitra; 26 in Tirol; 4 in Salzburg, all in the Pinzgau, e.g. Krimml; 3 in Kärnten; 3 in the Steiermark; Schruns in Vorarlberg), where radon protection is mandatory in new builds and Generalsanierungen. **Radonvorsorgegebiete** (preventive measures in all new builds under Land law implementing OIB-Richtlinie 3) cover all of Kärnten, Salzburg and Tirol; Burgenland except Bezirke Güssing, Jennersdorf, Neusiedl am See and Oberwart; NÖ except Bezirk Bruck an der Leitha; OÖ except Bezirk Ried im Innkreis; the Steiermark except Bezirk Südoststeiermark; and Bezirk Bludenz in Vorarlberg; none in Wien. Check the Gemeinde on the AGES Radonkarte; BMLUK offers a free two-detector home measurement (order in calendar week 28 or 48)
- **Hangrutsch** (slope movements): post-storm + heavy rain

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1945 Gründerzeit** | Lead, asbestos, Holzbalkendecken, Holzwurm |
| **1945–1965 Wiederaufbau** | Asbestos common, lead pipes, energy-inefficient |
| **1965–1980** | "Plattenbau" Wien-style + Eternit asbestos roofs |
| **1980–2000** | Phasing out asbestos, basic insulation |
| **Post-2008** | OIB-Richtlinien strict; modern envelope |

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energieausweis (EAW)** — Energieausweis-Vorlage-Gesetz 2012 (EAVG 2012) | Sales and lettings (In-Bestand-Gabe; lease extensions too from 1 Jul 2026): shown before the buyer or tenant signs, handed over within 14 days of the contract (§ 4); ads published from 1 Jul 2026 must state Heizwärmebedarf, Endenergiebedarf and Gesamtenergieeffizienzklasse (§ 3 as amended by BGBl I 38/2026; Heizwärmebedarf + fGEE before, still allowed with an older certificate); exemptions in § 5 (e.g. detached buildings under 50 m², buildings only kept frost-free, demolition-ready buildings on sale) | At most 10 years old at signing (§ 4 Abs 1); fine up to €1,450 (§ 9); without an EAW, at least the energy performance usual for the building's age and type counts as agreed (§ 7 Abs 1) (RIS EAVG 2012, Fassung vom 28.10.2026) |
| **Grundbuchauszug** | Verify owner + Lasten | At sale |
| **Lageplan / Mappenkopie** | Boundaries | Per case |
| **Wohnungseigentumsvertrag (§ 3 Abs 1 Z 1 WEG 2002) + Nutzwertgutachten (§ 9 Abs 1 WEG 2002)** | If Wohnungseigentum | At sale |
| **Hausverwaltung Auskunft** (Rücklage, Hausgeld) | If apartment | At sale |
| **Gefahrenzonenplan** (die.wildbach under the Forstgesetz 1975; flood zones under § 42a WRG 1959 / WRG-GZPV, BGBl II 145/2014) | If alpine / flood-prone — a planning instrument; the die.wildbach plan is open to public inspection at the Gemeinde, the Bezirksverwaltungsbehörde, the Landesregierung and the die.wildbach office | Per case |

### Climate change projections (GeoSphere Austria)

- ÖKS15, the official national scenarios (2016), run about 1 °C below observed warming (klimaszenarien.at), so GeoSphere Austria's data hub says their direct use can no longer be recommended without reservation (editorial note May 2026); successor ÖKS26 expected during 2027. Example (ÖKS15, Wien, vs the 1971–2000 mean of 10.2 °C): +1.2 °C to +1.5 °C for 2021–2050 and +2.2 °C (climate-protection scenario) or +3.8 °C (business as usual) for 2071–2100 — 2016 data, figures may have changed since. Observed temperature in Austria is currently rising at almost 0.7 °C per decade (klimaszenarien.at ÖKS15 recommendations, July 2026, citing the AAR2 report)
- Heat waves: longer + more intense
- Precipitation: one-hour extreme rain now brings about 15 % more rain than before (vs 1981–2010), directly linked to warming (GeoSphere Austria); 12–16 Sep 2024 brought 25 % more rain almost area-wide in Wien, NÖ and OÖ than earlier five-day extremes, locally 120–160 % more (GeoSphere Austria)
- **Lawinen**: less reliable below 1,500m altitude
- **Wasser**: drought risk Pannonisches Becken (Burgenland, Niederösterreich)
- **Schnee**: ski-season decreasing in lower Alps

---

## Section: `--mains`

### Sources

- Drinking water: about 93 % of residents are on central supply systems run by about 5,500 Wasserversorgungsunternehmen (kommunale Anlagen, Wasserverbände, Genossenschaften); the other 7 % use their own Hausbrunnen or Quellen, which are not a public responsibility, so owners should test the water themselves (BMLUK, read 2026-10-28)
- **ÖVGW (Österreichische Vereinigung für das Gas- und Wasserfach)**: `https://www.ovgw.at/`
- Major operators: Wiener Wasser (MA 31), Linz AG, Salzburg AG, IKB (Innsbrucker Kommunalbetriebe)
- **Electricity / gas**: compare supplier offers with the **E-Control Tarifkalkulator** (`https://www.e-control.at/tarifkalkulator`). Electricity network charges (Systemnutzungsentgelte) are set by the E-Control Regulierungskommission in the Systemnutzungsentgelte-Verordnung (SNE-V), except the one-off Netzzutrittsentgelt, which covers the network operator's reasonable costs of a first connection or a capacity upgrade; a new connection also triggers the lump-sum Netzbereitstellungsentgelt (E-Control, read 2026-10-28)

### Verification

- Public sewers: 96.5 % of residents connected to a kommunale Kläranlage at end-2024, 91 % to almost 100 % by Bundesland; 100 % is not realistic given the many Streusiedlungen (BMLUK Lagebericht Kommunales Abwasser 2026) — national / Land rates only, never a parcel-level claim
- Almhütten + Maiensässe + Streusiedlungen alpine: Hauskläranlage / Senkgrube
- **Anschlussbescheid**: the Bau- und Kanalanschlussgesetze of the Länder oblige buildings to connect to an existing public sewer (BMLUK Lagebericht 2026); a statutory duty to hand over an Anschlussbescheid at sale is not verified — ask the seller or the Gemeinde for it

### Costs

| Scenario | Cost (€, est. 2026) |
|---|---:|
| Anschluss to mains (where available) | ~3,000–8,000 |
| Mains-line extension if needed | varies by Gemeinde |
| Hauskläranlage (4 EW) | ~6,000–15,000 |
| Senkgrube replacement | ~4,000–10,000 |

*Est. — verify with local installer / Gemeinde; figures may have changed since 2026.*

---

## Cost benchmarks (AT 2026)

| Work | Cost (€, est. 2026) |
|---|---:|
| Energieausweis | ~250–600 |
| Notar / Anwalt | 1.0–2.5 % of price |
| Grunderwerbsteuer | 3.5 % |
| Eintragungsgebühr Grundbuch | 1.1 % |
| Maklerprovision (3 % each side excl. VAT) | ~3.6 % typical |
| **Total transaction cost** | **9–11 %** of price |
| Lawinenverbauung repair (alpine specific) | varies |
| Asbestsanierung (small house) | ~15,000–60,000 |
| Energetische Sanierung Klasse C → A | ~50,000–120,000 |
| Heizungstausch (Wärmepumpe) — incl. Förderung | ~25,000–40,000 |
| Dachsanierung Tiroler Schindel (200 m²) | ~30,000–60,000 |

*Construction/retrofit ranges are est. — verify with quotes; figures may have changed since 2026.*

## Active fiscal incentives (2025-2026)

- **Sanierungsoffensive 2024–2030** (federal + Bundesländer): up to ~€15,000 est. for fossil → renewable heating (verify current cap at umweltfoerderung.at)
- **Wohnbauförderung** (per Bundesland) — varies massively
- **Sonder-AfA** for new Mietwohnungen
- **Klimaticket Effizienzhaus** subsidy
- **Investitionsfreibetrag (IFB)**: 10 % deduction for retrofit
- **Erneuerbare-Wärme-Gesetz (EWG)** from 2024: oil/gas heating bans phasing in

## Common listing platforms

- **Willhaben.at** — biggest, full extraction
- **ImmobilienScout24.at**
- **derStandard Immo**
- **Bazar.at, Quoka.at** — privates
- **EHL, JP Immobilien, Otto Immobilien** — premium agency Wien
- **immo.tt.com** Tirol-specific

## Caveats unique to AT

- **Ausländergrunderwerb** (foreign buyer rules): non-EU/EEA buyers need a **grundverkehrsbehördliche Genehmigung** in some Bundesländer (esp. Tirol, Salzburg, Vorarlberg), granted by the Bezirksverwaltungsbehörde in Tirol (§ 26 TGVG 1996), by the Grundverkehrsbeauftragte(r) in Salzburg (Grundverkehrskommission for farm/forest land; § 20 Abs 3 S.GVG 2023) and by the Grundverkehrs-Landeskommission in Vorarlberg (§ 13 Abs 2 GVG) — an **approval regime with no quota and no percentage cap**. Tirol equates EU/EEA nationals with Austrians outright (§ 3 TGVG); Salzburg and Vorarlberg exempt acquisitions made in exercise of EU/EEA freedoms, including free movement of capital (§ 22 S.GVG; § 3 Vbg GVG). Do not conflate it with the nationality-neutral second-home thresholds below — they are two distinct regimes. (2026-10-21 verified; source RIS konsolidiertes Landesrecht: TGVG 1996, S.GVG 2023, Vorarlberg GVG)
- **Zweitwohnsitz-/Freizeitwohnsitz-Schwellen** (nationality-neutral — NOT a foreign-buyer quota): **Tirol** — new Freizeitwohnsitze may not be declared permissible once the Freizeitwohnsitz share exceeds **8 v.H.** of total dwellings per the last Gebäude- und Wohnungszählung (§ 13 Abs 5 lit a TROG 2022, consolidated version in force 7 Jul 2026, LGBl 43/2022 as amended by LGBl 51/2026). **Salzburg** — Zweitwohnung-Beschränkungsgemeinden are communes where non-Hauptwohnsitz dwellings exceed **16 %** of the total stock (§ 31 Abs 1 Z 1 ROG 2009, in force 1 Mar 2023, LGBl 95/2022), designated by Landesregierung-Verordnung **every five years** on the five-year arithmetic mean at Stichtag 31 Oct — not annually; a Gemeinde may apply to have its percentage raised. No tightening verified through 21 Oct 2026 (Tirol LGBl 51/2026, kundgemacht 6 Jul 2026, is a building/energy-law omnibus whose TROG article also reworded § 13 Abs 1 and added a § 13 Abs 8 Ausnahmebewilligung ground for lifetime gifts to statutory heirs where the donor kept a residential servitude until death; the 8 v.H. cap is unchanged. Salzburg ROG amendment LGBl 79/2026 touches only §§ 5 Z 2, 53 Abs 2 Z 11, 60 Abs 1 und 5 and 88 Abs 9). (2026-10-21 verified; source [RIS ROG 2009 § 31](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=LrSbg&Gesetzesnummer=20000615&Paragraf=31) + RIS konsolidiertes Landesrecht Tirol)
- **Naturschutz** restrictions on alpine constructions — strict
- **MRG categories** make rental investment math depend heavily on building age
- **Mietkauf** model (rent-to-own via Genossenschaft) common
- **HORA portal is free, all-hazards-in-one-place, with a HORA-Pass for any location** — use it as the first screen, not the single source of truth: BMLUK calls it a complement to the parcel-sharp Gefahrenzonenpläne, so also check the Gemeinde's Gefahrenzonenplan and the WISA RMP2027 flood maps
- **Erbenermittlung** can stall purchases for months if Grundbuch unclear
- **Bauernhof** (farm) special restrictions; Anerbenrecht
- **Schenkungsmeldegesetz** since 2008 — mandatory disclosure for gifts
- **Tourismusabgabe** per Gemeinde — affects rental margins
- **Lex Koller-style** restrictions in some Bundesländer
- **Almhütten** + **Bauernhöfe** subject to special rural property law

## Reddit / forum sources

- **r/Austria**, **r/wien**
- **r/AustrianEconomy**
- **derStandard Forum** (active discussions)
- **Bauen-Wohnen.at**, **Energiesparhaus.at** forums
- Expat: **Vienna Würstelstand**, **The Local Austria**

## Verification authorities

| Authority | When to call |
|---|---|
| **Bezirksgericht Grundbuch** | Title verification, encumbrances |
| **Gemeinde / Bauamt** | Bauakt, Flächenwidmungsplan, permits |
| **Finanzamt** | Grundsteuer assessment, Einheitswert |
| **Notar** | Final transfer, escrow |
| **Wasserwerk Gemeinde** | Mains drains verification |
| **Bundesland Wasserrechtsbehörde** | Flood zone confirmation |
| **die.wildbach (Wildbach- und Lawinenverbauung) Gebietsbauleitung** | Wildbach / Lawinen Gefahrenzonenplan; building conditions in a Gelbe Zone |
| **AGES** | Radon, food safety |
| **GeoSphere Austria** | Seismic + climate |
| **Wohnungseigentumsverwaltung (WEG)** | Hausgeld, Rücklage, Beschlüsse |

## Quirks to know

- **Einlagezahl (EZ)** + **Katastralgemeinde** — the Austrian way to identify property; PLZ + address often insufficient
- **Grundbuchauszug A1/A2/B/C blätter** — read all 4 sections (rights, encumbrances, mortgages, etc.)
- **Wohnnutzwert** vs Nutzwert — share-allocation in WEG
- **Anteil + Tagsatz** allocate Hausgeld
- **Wohnungseigentumsvertrag** + **Nutzwertgutachten** at sale
- **Bestandschutz** for old buildings; new requirements only on changes
- **Schillingbescheid**: legacy 1995 property tax base in some files
- **Grundverkehr** restrictions in Tirol/Salzburg/Vorarlberg — approval (Genehmigungspflicht), not a quota
- **Pflegeregress** (since 2018, abolished — but check older estates)
- **Anerbenrecht**: peasant inheritance rules in Tirol, Salzburg, Kärnten

## Source URL templates

| Source | URL pattern |
|---|---|
| HORA | `https://hora.gv.at/` |
| WISA Hochwasser (RMP2027, 3rd cycle) | `https://maps.wisa.bmluk.gv.at/rmp2027/` |
| AGES Radon | `https://geogis.ages.at/GEOGIS_RADON.html` |
| GeoSphere Austria | `https://www.geosphere.at/` |
| Statistik Austria HPI | `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/haeuserpreisindex-und-ooh-pi` |
| OeNB Wohnimmobilienpreis | `https://www.oenb.at/daten-und-forschung/datenangebot/preise-wettbewerbsfaehigkeit/immobilien/6-6-wohnimmobilienpreisindex.html` (updated 2026-10-28) |
| Willhaben Immobilien | `https://www.willhaben.at/iad/immobilien/<typ>/<bundesland>/<bezirk>` |
| ImmobilienScout24.at | `https://www.immobilienscout24.at/regional/<bundesland>/<bezirk>/<typ>` (typ e.g. `wohnung-kaufen`, `haus-kaufen`, `wohnung-mieten`) |
| Justizportal Grundbuch | `https://www.justiz.gv.at/service/datenbanken/grundbuch.96c.de.html` (updated 2026-10-28) |
| BMF Finanzonline | `https://finanzonline.bmf.gv.at/` |
| E-Control Tarifkalkulator (electricity / gas) | `https://www.e-control.at/tarifkalkulator` |
| Breitbandatlas (broadband availability) | `https://breitbandatlas.gv.at/` |
| BKA Polizeiliche Kriminalstatistik (reported offences only) | `https://www.bundeskriminalamt.at/501/start.html` |

## Status

✅ **Fully populated** as of 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (HORA + Statistik Austria + Grundbuch all gold-standard). MEDIUM for short-let regulation (Wiener Bauordnung 2024 + EU 2024/1028 opt-in implementation by the Länder still evolving).
**Last verified**: 2026-08-07 — `--tax` ownership caveats only (Grundverkehr approval regime + Tirol/Salzburg second-home share thresholds re-verified against RIS konsolidiertes Landesrecht); all other sections remain at 2026-07-03. Rental / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Finance / rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early — short-let / STR-VO paragraph corrected: Wien register law passed by the Landtag 20 Oct 2026, not yet gazetted; BMWET: Tirol and Wien expected to start during Q1 2027; see shared/regulatory-watch.md).

## Extension TODOs

- [ ] Per-Bundesland Ausländergrunderwerb rules
- [ ] HORA 3D parcel-level extraction
- [ ] Per-Gemeinde Tourismusabgabe rates
- [ ] Wohnbauförderung per Bundesland decision tree
- [ ] MRG category detection from build year + Bezirk
- [ ] Anerbenrecht detection from Grundbuch
- [ ] Zweitwohnsitz quota per alpine Gemeinde
- [ ] Grundsteuerreform tracking (likely 2026-2028)
