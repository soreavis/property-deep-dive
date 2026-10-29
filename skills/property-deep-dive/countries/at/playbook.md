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
  - Built from the purchase contracts lodged in the Grundbuch, private-household buyers only; quarterly. Q2 2026: 105.00 (2025 = 100), +5.1 % YoY, a new all-time high; next release (Q3 2026) on 18 Dec 2026 (2026 data, source Statistik Austria HPI page, updated 23 Sep 2026)
- **OeNB (Österreichische Nationalbank) Wohnimmobilienpreisindex**:
  - `https://www.oenb.at/daten-und-forschung/datenangebot/preise-wettbewerbsfaehigkeit/immobilien/6-6-wohnimmobilienpreisindex.html` (updated 2026-10-28; the old /Statistik/Standardisierte-Tabellen/ URL returns 404)
  - Quarterly, 2000 = 100, separate series for Wien and Österreich ohne Wien; data basis is the broker software JUSTIMMO (since Q3 2017, per OeNB metadata), not Grundbuch contracts, so it can diverge from the Statistik Austria HPI
- **Statistik Austria Immobilien-Durchschnittspreise** (annual; €/m² for houses and flats per Bezirk, plots also per Gemeinde, from Grundbuch contracts of private-household buyers; 2025 edition published 28 May 2026, next 28 May 2027; usable as the basis for Grunderwerbsteuer on unentgeltliche Erwerbe under the Grundstückswertverordnung):
  - `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/immobilien-durchschnittspreise`
- **Grundbuch (online via Justizportal)**:
  - `https://www.justiz.gv.at/service/datenbanken/grundbuch.96c.de.html` (updated 2026-10-28; the old grundbuch~36 URL now lands on an unrelated Erwachsenenvertretung page); online query via JustizOnline `https://justizonline.gv.at/jop/web/grundbuchabfrage` or a Verrechnungsstelle
  - Paid queries: aktueller Grundbuchsauszug (Vollabfrage einer EZ) **€4.89**, Teilauszug (A-, B- or C-Blatt) €2.60, Urkundensammlung €1.52 per document, Suche nach Kaufverträgen je Katastralgemeinde €2.44, plus the Verrechnungsstelle's own charge; since 1 Oct 2026 owners can pull the Grundbuchauszug of their own property free on JustizOnline (2026 data, source oesterreich.gv.at 'Grundbuchsabfrage über das Internet', BMJ, updated 1 Oct 2026)

### Listing platforms

- **Willhaben.at** — largest: `https://www.willhaben.at/iad/immobilien`
- **ImmobilienScout24.at**: `https://www.immobilienscout24.at/`
- **derStandard Immo**: `https://immobilien.derstandard.at/`
- **Bazar.at** — private classifieds with an Immobilien category (live 2026-10-28); **Quoka.at** now redirects to the German quoka.de (checked 2026-10-28)
- Premium: **EHL Immobilien**, **Engel & Völkers AT**, **JP Immobilien** Wien

### Price benchmarks — Statistik Austria median €/m² Wohnfläche, 2025

| City / Area | Wohnungen median €/m² (2025) | Häuser median €/m² (2025) |
|---|---:|---:|
| **Wien** (Gemeinde = Bundesland) | 5,212 | 5,376 |
| Wien inner Bezirke: 1. Innere Stadt / 4. Wieden / 7. Neubau / 8. Josefstadt / 9. Alsergrund | 11,576 / 7,243 / 6,110 / 6,028 / 6,096 (1. Bezirk volatile: 14,956 in 2024) | not published (under 10 transactions) |
| **Salzburg** (Stadt) | 5,114 | 6,167 |
| **Innsbruck** | 6,034 | 5,621 |
| **Graz** | 3,193 | 4,034 |
| **Linz** | 3,749 | 4,050 |
| **Klagenfurt am Wörthersee** | 3,352 | 3,313 |
| **Bregenz** (Gemeinde; Bezirk Bregenz 5,056 / 5,117) | 3,986 | 5,588 (no Gemeinde value published for 2024) |
| Niederösterreich / Burgenland / Kärnten (whole Land, towns included) | 3,089 / 1,859 / 3,260 | 2,653 / 1,889 / 2,609 |

(2025 data, source Statistik Austria Immobilien-Durchschnittspreise Sonderauswertung, created 28 May 2026: medians of € per m² Wohnfläche paid by private households, from Grundbuch purchase contracts. City rows are Gemeinde medians, inner-Bezirk rows Bezirk medians, the last row Land medians; no value is published where fewer than 10 transactions remain. Small-area medians mix price, quality and location effects. For a valuation use the Bezirk tables by build period and size in the Wohnungspreise / Häuserpreise 2025 files, which are geometric means.)

National medians 2025 (Statistik Austria, PM 28 May 2026; revised 2024 value in brackets):
- **Eigentumswohnung**: 4,162 €/m² (2024: 3,986)
- **Wohnhaus** (Häuser): 2,836 €/m² (2024: 2,711)
- **Bebaubares Grundstück**: 135 €/m² Grundfläche (geometric mean; 2024: 123)

### 2025–2026 trend (Statistik Austria HPI + OeNB)

- **Statistik Austria HPI** (Grundbuch contracts): 2025 annual average **+2.5 %** (revised; the PM of 26 Mar 2026 said +2.6 %), about −1.1 % real against 3.6 % CPI inflation (computed: 1.025 / 1.036 − 1); **H1 2026 +3.9 %** YoY (total index Q2 2026 +5.1 %), and Q2 2026 is a new all-time high above the Q3 2022 peak (PM 23 Sep 2026)
- **OeNB Wohnimmobilienpreisindex** (2000 = 100): 2025 annual average 266.9, **+1.0 %** (Wien +1.4 %, Österreich ohne Wien +0.7 %), about −2.5 % real against 3.6 % CPI (computed: 1.010 / 1.036 − 1). The OeNB release of 29 Jan 2026 reported +2.1 % for '2025' (Wien +2.9 %, rest of Austria +1.6 %): these equal the Q4 2025 year-on-year rates in OeNB table 6.6, and the 3.8 % inflation formerly paired with them is the December 2025 rate, not the 3.6 % annual average (release text not retrieved this run; figures per ORF, secondary)
- OeNB index **274.0 in Q2 2026** (+3.6 % YoY; Wien 307.8, Österreich ohne Wien 266.2; Q1 2026: 272.2): the Österreich total is still below its Q3 2022 peak of 278.3, so not a record on the OeNB headline series (Österreich ohne Wien is just above its Q3 2022 level of 265.4), while the Statistik Austria HPI is at a record; the two series use different data (JUSTIMMO broker data vs Grundbuch contracts) (OeNB table 6.6, read 2026-10-28)

### Compute

1. Listing €/m² = listing price / Nutzfläche (§ 2 Abs 7 WEG 2002); Statistik Austria benchmarks use the Wohnfläche from the purchase contract, supplemented from the Gebäude- und Wohnungsregister
2. **Trap**: under § 2 Abs 7 WEG 2002 the Nutzfläche excludes stairs, open balconies and terraces and Zubehörobjekte (separate Keller- or Dachbodenräume, Hausgärten, Lagerplätze, § 2 Abs 3); Keller- and Dachbodenräume count only if fitted out for living or business use — check what the listing counts
3. **Trap**: Quadratmeterpreis vs Pauschalpreis — Vienna Altbau often pauschal
4. Compare to Statistik Austria for the Bezirk
5. Grundbuchauszug needed for definitive ownership + encumbrances

---

## Section: `--traffic`

### Primary sources

- **ASFINAG** — Autobahnen + Schnellstraßen: `https://www.asfinag.at/`; counts at `https://www.asfinag.at/verkehr-sicherheit/verkehrszaehlung/` — about 300 automatic Dauerzählstellen, monthly Verkehrsstatistik plus annual files back to 2012, DTV in Kfz/24h by day type (Mo–So, Mo–Fr, Sa, Sonn- und Feiertage) and vehicle class (≤ / > 3.5 t) (read 2026-10-28)
- **Bundesländer Verkehrszählung**:
  - Wien Stadtinformation: `https://www.wien.gv.at/`
  - Tirol: `https://www.tirol.gv.at/`
  - OÖ: `https://www.land-oberoesterreich.gv.at/`
  - Each Bundesland has Verkehrsabteilung
- OSM `highway` class fallback

### Key term

**JDTV (Jährlicher durchschnittlicher täglicher Verkehr)** = AADT-equivalent; ASFINAG's annual Verkehrsstatistik uses the term and gives no JDTV for a counter with more than 100 days of a year lacking counted or estimated values (Verkehrsstatistik 2025, published 30 Mar 2026)

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
Grundsteuer = Einheitswert × Steuermesszahl × Hebesatz
```

- **Einheitswert**: very outdated valuation — Grundvermögen is still valued under the BewG 1955 rules in force from 1 Jan 1973 (BGBl 447/1972), raised by a flat 35 vH from 1 Jan 1983 (Art II Abs 1 BGBl 570/1982) — est. ~5–20 % of market value
- **Steuermesszahl**: 0.05 % – 0.2 % (§ 19 GrStG 1955: 2 v.T. in general; Einfamilienhaus 0.5 v.T. on the first €3,650 and 1 v.T. on the next €7,300 of Einheitswert; Mietwohn- and gemischtgenutzte Grundstücke 1 v.T. then 1.5 v.T. on the first two €3,650 bands)
- **Hebesatz**: set by the Gemeinde, **at most 500 %** (§ 17 Abs 1 FAG 2024; § 27 GrStG) — the USP worked example uses 500 %
- **No separate Bundeszuschlag factor**: the 35 vH uplift from 1 Jan 1983 (Art II Abs 1 BGBl 570/1982) is already in the Einheitswert on the Bescheid; the bill is Einheitswert × Steuermesszahl = Messbetrag, × Hebesatz (USP example: €50 × 500 % = €250/yr)

### Reform pending

Long-debated Grundsteuerreform (revaluation of the Einheitswerte). As of 28 Oct 2026: **not enacted** — the GrStG 1955 was last amended by BGBl I 135/2024 and the 500 % Hebesatz cap in § 17 Abs 1 FAG 2024 is unchanged (RIS consolidated versions of 28 Oct 2026).

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

- About 1–3 % of the price for contract drafting and the Grundbuch filing, set by the fee schedules of the respective chambers; a flat fee can be agreed (oesterreich.gv.at, BMJ, last update 1 Aug 2026). Notaries' statutory tariff is the Notariatstarifgesetz (NTG)

### Maklerprovision

- Purchase: capped at **3 %** of the price for prices above €48,448.51 (4 % up to €36,336.42; €1,453.46 in between), plus 20 % USt; the broker may charge both buyer and seller up to that cap each, and if no commission is agreed with the other side the one agreed may exceed the cap by up to 100 %, but not a commission agreed with the Wohnungssuchender (buyer) of a Wohnung or Einfamilienhaus (§§ 12 Abs 1–3, 15 Abs 2 Immobilienmakler-Verordnung; oesterreich.gv.at). The **Bestellerprinzip** (since **1 Jul 2023**, § 17a MaklerG, BGBl I 24/2023) covers residential **rental** contracts only — whoever first commissions the broker pays; it does not apply to purchases

### Total transaction cost (buyer side)

- 3.5 % GrESt + 1.1 % Eintragung + 1–3 % Notar/Anwalt + 3.6 % Makler (3 % + 20 % USt) = **~9.2–11.2 %** (computed); add 1.2 % of the registered Pfandrecht if mortgage-financed (TP 9 lit b Z 4 GGG)

### VAT (USt.)

- 20 % standard
- 10 % reduced (food, books, residential rent)
- Sale of land and buildings, new or existing: VAT-exempt (§ 6 Abs 1 Z 9 lit a UStG), but a business seller (e.g. a developer) may opt to charge 20 % (§ 6 Abs 2) — check whether the price is quoted 'zzgl. USt'; there is no automatic 20 % rate on new builds

### Future risk

- **Grundsteuerreform**: not enacted as of 28 Oct 2026 (see Reform pending above); a re-basing of the 1973-based Einheitswerte would raise bills most where the Einheitswert lags market value furthest — the size depends on the bill, so do not assume a multiple (the earlier '5–10×' had no source)
- **Erbschaftsteuer** abolished 2008, but periodic political resurfacing of reintroduction debate
- **Wegzugsbesteuerung** for emigrants (§ 27 Abs 6 Z 1 EStG) covers capital assets, derivatives and crypto — not privately held Austrian real estate, which stays taxable in Austria when sold (beschränkte Steuerpflicht, § 98 Abs 1 Z 7 EStG)

---

## Section: `--rental`

### Long-term residential — MRG categories

**Mietrechtsgesetz (MRG)** divides rentals:
- **Vollanwendung** (full application): rented flats in buildings built under a Baubewilligung before 1 Jul 1953 and in post-1953 buildings erected with public funds (e.g. many Gemeindewohnungen), unless a Teil- or Nichtanwendung case below applies (e.g. Eigentumswohnungen in buildings permitted after 8 May 1945, later Dachboden or Zubau units) → Richtwert / Kategorie rent caps (§ 16) + Kündigungsschutz. Genossenschafts- (GBV-) Wohnungen: the MRG applies only as § 20 WGG provides (§ 1 Abs 3 MRG)
- **Teilanwendung** (partial, § 1 Abs 4 MRG): buildings built without public funds under a Baubewilligung after 30 Jun 1953, Dachboden conversions permitted after 31 Dec 2001, Zubauten permitted after 30 Sep 2006, and Eigentumswohnungen in buildings permitted after 8 May 1945 → only §§ 14, 16b, 29–36, 45, 46, 49 apply: Kündigungsschutz, Befristung and Kaution rules, but **no rent cap** (free rent; index clauses capped by the MieWeG below)
- **Nichtanwendung** (§ 1 Abs 2 MRG): buildings with no more than two independent units (Ein-/Zweifamilienhäuser; later Dachboden units not counted), Beherbergung, Dienstwohnungen, holiday second homes, and fixed lets of up to six months of a category A/B flat as a work-related second home → ABGB only, free market. Eigentumswohnungen are **not** exempt as such — outside the cases above they fall under Voll- or Teilanwendung by permit date

### Vienna-specific (most regulated)

- **Wiener Wohnen** (Gemeindewohnungen): about 220,000 Gemeindewohnungen ("rund 220.000"), home to about 500,000 people, regulated rent (source Wiener Wohnen 'Über uns', read 2026-10-28)
- **Average rents** (Statistik Austria Mikrozensus, Hauptmietwohnungen, rents paid by tenant households under contracts of all ages, not asking rents): **€10.5/m²** incl. Betriebskosten in Q2 2026 (+3.3 % YoY; €7.9/m² net of Betriebskosten). Net rent by segment, Q2 2026: private Altbau (pre-1945) €8.5, private post-1945 €10.7, Genossenschaft €6.5, Gemeindewohnung €5.7 per m². 2025 incl. Betriebskosten by Bundesland: Salzburg 12.2 · Tirol 12.0 · Vorarlberg 11.8 · Wien 10.6 · Steiermark 9.8 · Oberösterreich 9.3 · Niederösterreich 9.2 · Kärnten 8.1 · Burgenland 7.7 €/m²; contracts under 2 years €12.4/m² vs €6.5/m² for 30+ years (2025/2026 data, sources Statistik Austria PM 8 Sep 2026, PM 10 Jun 2026 and Wohnkosten Mikrozensus table)
- **Genossenschaft** (cooperative): regulated rent + Eigenmittel
- **Privatmarkt** Vollanwendung: Richtwertmietzins per Bundesland (§ 16 Abs 2 MRG) plus or minus Zu- und Abschläge; the **Lagezuschlag** is not a fixed percentage — up to 0.33 vH per m² and month of the difference in Grundkostenanteil, only for an above-average Lage disclosed in writing at signing (§ 16 Abs 3–4); fixed-term leases: maximum rent **−25 %** (Befristungsabschlag, § 16 Abs 7)
- **2026 Richtwert Wien: €6.74/m²** (from €6.67; +1 %, the statutory cap for 1 Apr 2026, § 5 Abs 2 RichtWG; Statistik Austria publication, effective 1 Apr 2026); Lagezuschlag and Befristungsabschlag as above — no fixed % zone bonus. **Mieten-Wertsicherungsgesetz (MieWeG, BGBl I 114/2025), in force 1 Jan 2026** (via 5. Mietrechtliches Inflationslinderungsgesetz, 5. MILG): caps contractual Wertsicherungsklauseln in residential leases under the MRG incl. Teilanwendung (§ 1 Abs 1) — adjustments only on 1 April, by the prior year's average CPI change, with any part above 3 % passed on only by half (e.g. 4.5 % inflation → max 3.75 %, computed: 3 + 1.5 ÷ 2), for increases from 1 Jan 2026 (§ 1 Abs 2 Z 1, § 4 Abs 2) — this already covers free-market (Teilanwendung) rents; leases under MRG rent caps additionally count 2025 CPI at most 1 % and 2026 CPI at most 2 % (§ 1 Abs 3), and the Richtwerte rise at most 1 % on 1 Apr 2026 and 2 % on 1 Apr 2027, with the half-above-3 % rule from 1 Apr 2028 (§ 5 Abs 2 RichtWG). The new Richtwert itself takes effect on 1 Apr 2026, not 1 May; under a Vollanwendung (MRG rent-cap) lease with a Wertsicherung clause the raised rent is owed only from the Zinstermin after the index change, on a written request at least 14 days before (§ 16 Abs 9 MRG) — with the default Zinstermin on the 5th of the month (§ 15 Abs 3 MRG) that is 5 May 2026 at the earliest (computed). Excludes Ein-/Zweifamilienhäuser (outside the MRG, § 1 Abs 2 Z 5) and WGG/Genossenschaft rents (own regime — not re-verified 2026-10-28). (2026-10-28 verified, RIS MieWeG + RichtWG § 5 + MRG § 16 + Statistik Austria)

### Short-term rentals (Ferienwohnung / Airbnb)

**Wien**:
- **Wiener Bauordnungsnovelle 2023** (short-let limits city-wide from 1 Jul 2024): max 90 days per calendar year for temporary short-let of a dwelling without giving up one's residence (legal persons cannot use the 90-day allowance); above that, outside a Wohnzone only with an Ausnahmebewilligung under § 129 Abs 1a BO limited to five years, inside a Wohnzone only as a Beherbergungsstätte after an Umwidmung under § 7a Abs 5 BO (2026 data, source MA 37 Merkblatt Kurzzeitvermietung + Stadt Wien press release 2026-09-19); registration number from 1 Jan 2027 under the Wiener register law passed by the Landtag on 20 Oct 2026 (not yet in the LGBl as of 2026-10-28 — see STR-VO note below); the same law narrows the 90-day allowance to one dwelling per host (MA 37 Merkblatt, Stand Oct 2026)
- WEG approval typically required
- Penalty: up to €50,000 (§ 135 Abs 1 BO); each repeated short-let offence at least €2,000 under the 20 Oct 2026 amendment (MA 37 Merkblatt, Stand Oct 2026 — not yet in the RIS consolidated text)

**Salzburg (whole Land)**: using an existing Wohnung for touristische Beherbergung is a Zweckentfremdung (change of use) that needs a Bewilligung (§ 31b Abs 1 ROG 2009), except in designated Zweitwohnungsgebiete, pre-1973 Apartmentbauten, farm dwellings, Privatzimmervermietung and flats demonstrably already let to tourists before 1 Jan 2018 where that was lawful (§ 31b Abs 2). **Tirol / Innsbruck**: a Wohnung used only temporarily for holidays is a Freizeitwohnsitz (restricted, see caveats) unless it is a Gastgewerbebetrieb, Privatzimmervermietung or a small Ferienwohnung building (max three Wohnungen / twelve beds; for buildings permitted after 1 Feb 1996 only if the landlord has the Hauptwohnsitz there) (§ 13 Abs 1 TROG 2022). (2026-10-28 verified, RIS konsolidiertes Landesrecht)

**EU 2024/1028 (STR-VO)**: opt-in in Austria — the Wirtschaftsministerium (BMWET) says each Bundesland decides whether and from when the STR-VO applies; **Tirol and Wien** are expected ("voraussichtlich") to create the legal, organisational and technical prerequisites and start implementation **during Q1 2027**, with host registration and platform data duties there from a date still to be set; BMWET names no Land where it already applies and is building the Single Digital Entry Point; no national STR registration-number regime. Substantive rules (Gewerbeordnung, Privatzimmervermietung, Raumordnung) stay untouched by the regulation in every Land. **Wien — law passed, not yet gazetted**: the Wiener Landtag passed on **20 Oct 2026** (SPÖ, NEOS, FPÖ and Grüne for, ÖVP against; no Begutachtung) the law amending the Bauordnung für Wien and setting up a Wiener Register für Kurzzeitvermietungen (announced 19 Sep 2026 as the WKVRG); no LGBl Wien publication on RIS as of 2026-10-28 (latest LGBl Wien: No 38/2026 of 21 Oct 2026). Per Stadt Wien: register law in force **1 Jan 2027**; listings already online have until the **end of March 2027**; every unit registered separately and the number shown in every platform listing, even below 90 days; platforms must spot-check registrations, remove impermissible listings and pass information to the Magistrat; fines up to €50,000 per violation of the register law. Bauordnung side: each repeated short-let offence at least €2,000 (MA 37 Merkblatt, Stand Oct 2026); new § 7g BO — conversions into Beherbergungsstätten anywhere in Wien need at least 80 % of the building's Nutzflächen to stay residential, at least three Zimmereinheiten close together and a separate street entrance (only classic hotels exempt), applied to applications filed from 11 Oct 2026 (sources [Rathauskorrespondenz 2026-10-20](https://presse.wien.gv.at/presse/2026/10/20/15-wiener-landtag-14) + [Stadt Wien OTS 2026-10-20](https://www.ots.at/presseaussendung/OTS_20261020_OTS0019/verschaerftes-regulativ-fuer-kurzzeitvermietung-in-wien-stadt-wien-sichert-wohnraum-nachhaltig-ab); final wording to be checked in the LGBl). (2026-10-21 verified; source [BMWET STR-VO](https://www.bmwet.gv.at/Themen/Tourismus/kurzzeitvermietung.html))

### Tax treatment

- **§ 28 EStG (Vermietung & Verpachtung)** for non-commercial private rental
- **Gewerbliche Vermietung**: depending on the type of letting (e.g. hotel-style services), the income is Einkünfte aus Gewerbebetrieb instead of V&V (oesterreich.gv.at, updated 31 Aug 2026; the BMF treats tourist short-term platform letting as V&V 'grundsätzlich'); a Gewerbeberechtigung brings Wirtschaftskammer membership and GSVG insurance via the SVS (§ 2 Abs 1 Z 1 GSVG). Austria levies no Gewerbesteuer — the Gewerbesteuergesetz 1953 is not in force (RIS)
- VAT: 10 % reduced for short-stay accommodation (Beherbergung, § 10 Abs 2 Z 3 lit c UStG; residential long lets also 10 %, lit a); Kleinunternehmer turnover limit €55,000 (§ 6 Abs 1 Z 27 UStG)
- **Ortstaxe / Nächtigungsabgabe**: per stay, under each Land's tourism law (rates vary). **Wien**: Ortstaxe as a % of the accommodation charge excl. USt and breakfast (§ 12 WTFG) — 3.2 % until 30 Jun 2026, **5 % from 1 Jul 2026**, **8 % from 1 Jul 2027** (§ 14 WTFG as amended by LGBl 2/2026; RIS 2026-10-28) — not a flat per-night amount

---

## Section: `--work=<profession>`

### Job platforms

- **AMS (Arbeitsmarktservice)**: `https://www.ams.at/`
- **karriere.at**, **stepstone.at**, **LinkedIn AT**, **derStandard Jobs** (`https://jobs.derstandard.at/`; the old karriere.derstandard.at host no longer resolves, checked 2026-10-28)
- **Jobbörse der Republik Österreich** (federal public-sector vacancies): `https://www.jobboerse.gv.at/` (replaces the bka.gv.at pointer, which now redirects to the Bundeskanzleramt home page; checked 2026-10-28)

### Self-employment regimes

- **Selbstständig (Gewerbeschein)**: standard self-employed; **SVS** (Sozialversicherung der Selbstständigen) mandatory
  - 2026 Mindestbeitragsgrundlage **€551.10/month** in PV and KV (€6,613.20/yr, computed ×12); minimum contributions PV €101.95 (18.5 %) + KV €37.48 (6.8 %) + Selbständigenvorsorge €8.43 (1.53 %) + UV €12.95 flat = **€160.81/month** (€1,929.72/yr, computed ×12); provisional contributions in the first three years are charged on this minimum (2026 data, source SVS Beitragstabelle 2026 + WKO 'Gewerbliche Sozialversicherungsbeiträge', Stand 1 Jan 2026; one SVS page gives UV €12.96)
- **Neue Selbstständige**: compulsory insurance under § 2 Abs 1 Z 4 GSVG for self-employed income (§§ 22 Z 1–3 and 5, 23 EStG) not already insured under another law; pension + health via SVS. § 109a EStG is only the client's Mitteilung (reporting) duty for such fees
- **Freier Beruf** (liberal): doctors, lawyers, architects — own Kammern; Ärzte, Apotheker, Patentanwälte and Ziviltechniker are pension-insured with the SVS under the FSVG (PV 20 % in 2026); other professions' own schemes not re-verified
- **GmbH**: min Stammkapital €10,000 (§ 6 Abs 1 GmbHG), of which at least €5,000 of the cash contributions must be paid in (§ 10 Abs 1 GmbHG) (RIS, Fassung vom 28.10.2026)
- **EPU (Ein-Personen-Unternehmen)**: about 376,000 in 2025, **62.1 %** of all Austrian enterprises (WKO, Datenstand 12/2025, source WKO 'EPU: Zahlen, Daten, Fakten')
- **Pauschalierung**: simplified tax regime for small businesses

### Salary benchmarks (2024 data, Statistik Austria)

- Median monthly gross, all employees incl. part-time, incl. 1/12 of the 13th + 14th salary (2024 annual average, Statistik Austria Monatseinkommen table M4, created 11 Dec 2025): **Österreich €3,713**; full-time full-year employees: median **€55,678** gross per year (2024, Statistik Austria Jährliche Personeneinkommen)
  - Wien: €3,682
  - Salzburg (Land): €3,620 · Tirol (Land, incl. Innsbruck): €3,564
  - Steiermark: €3,612 · Oberösterreich: €3,707 · Niederösterreich: €3,869 · Vorarlberg: €3,913
  - Burgenland: €3,841 · Kärnten: €3,698 — Land (NUTS 2) values, not city values
- **Mindestkollektivvertragslöhne**: no statutory minimum wage; set per branch in the Kollektivvertrag — at least **€1,900 gross/month** in most KVs, about €2,217 on a 12-month basis because of 14 payments (Stand 2025, AMS citing WKO); look up the applicable KV at `https://www.kollektivvertrag.at/`

### Cultural quirks

- **13. + 14. Gehalt** standard (taxed at lower rate: as sonstige Bezüge within the Jahressechstel, the first €620 at 0 % and the next €24,380 at 6 %, then 27 % and 35.75 % bands — § 67 Abs 1 EStG, version in force from 17 Oct 2026)
- **Kollektivvertrag** governs about 98 % of employment relationships (WKO Steiermark, updated 11 Nov 2024 — a social-partner figure)

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
| Notar / Anwalt | 1–3 % of price (oesterreich.gv.at) |
| Grunderwerbsteuer | 3.5 % |
| Eintragungsgebühr Grundbuch | 1.1 % |
| Maklerprovision (3 % each side excl. VAT) | ~3.6 % typical |
| **Total transaction cost** | **~9.2–11.2 %** of price (computed from the rows above; +1.2 % of the Pfandrecht if financed) |
| Lawinenverbauung repair (alpine specific) | varies |
| Asbestsanierung (small house) | ~15,000–60,000 |
| Energetische Sanierung Klasse C → A | ~50,000–120,000 |
| Heizungstausch (Wärmepumpe) — incl. Förderung | ~25,000–40,000 |
| Dachsanierung Tiroler Schindel (200 m²) | ~30,000–60,000 |

*Construction/retrofit ranges are est. — verify with quotes; figures may have changed since 2026.*

## Active fiscal incentives (2025-2026)

- **Sanierungsoffensive** (federal, run by KPC; annual programme): the 2026 budget ran out on 10 Jul 2026 and the Sanierungsbonus (thermal renovation) is closed; a re-launched **Kesseltausch 2026** for Ein-/Zweifamilien- and Reihenhäuser takes registrations from 2 Nov to 31 Dec 2026 (works from 7 Oct 2026) with maximum grants of **€4,000** (Nah-/Fernwärme), **€5,000** (Wärmepumpe) and **€6,000** (Holzzentralheizung), plus €2,500 for solar thermal and €5,000 for a deep borehole or well with a brine- or water-source heat pump (Infoblatt Version 10/2026); the programme continues in 2027 with applications from 4 Jan 2027 and Kesseltausch amounts unchanged (sanierungsoffensive.gv.at). Länder run their own grants — verify per Bundesland
- **Wohnbauförderung** (per Bundesland) — varies massively
- **Beschleunigte AfA für Wohngebäude**: let residential buildings completed 1 Jan 2024 – 31 Dec 2026 that meet at least klimaaktiv 'Gebäudestandard Bronze' may deduct up to 3× the 1.5 % AfA (= 4.5 %) in the first year and the two following years — after a purchase only if the seller had not yet used the building to earn income (§ 124b Z 451 EStG); other buildings acquired or built after 30 Jun 2020: up to 3× in year one and 2× in year two (§ 16 Abs 1 Z 8 lit e EStG)
- **Öko-Zuschlag** (extra 15 % deduction for thermal renovation or replacing fossil heating in let residential buildings, § 124b Z 452 EStG) — EXPIRED for V&V landlords: it covered only costs incurred in 2024 and 2025; for business income only the first fiscal year starting after 31 Dec 2023 and the next one
- **Investitionsfreibetrag (IFB, § 11 EStG)**: 10 % (15 % for ökologische investments) of acquisition costs — raised to 20 % / 22 % for costs falling between 1 Nov 2025 and 31 Dec 2026 (§ 124b Z 480 EStG) — for business income only (not V&V letting); buildings are excluded (§ 11 Abs 3 Z 2) except heat pumps, biomass boilers, district-heating transfer stations and micro-grids for buildings — not a general retrofit deduction for private landlords
- **Erneuerbare-Wärme-Gesetz (EWG, BGBl I 8/2024)**: in force since the day after its publication, bans installing heating systems that can run on fossil fuels — and connections to non-quality-assured district heat — in **new buildings** only (§ 3 Abs 1); it replaced the Ölkesseleinbauverbotsgesetz 2019 (§ 6 Abs 1) and sets no phase-out for existing oil or gas heating

## Common listing platforms

- **Willhaben.at** — biggest, full extraction
- **ImmobilienScout24.at**
- **derStandard Immo**
- **Bazar.at** — privates (live 2026-10-28); **Quoka.at** now redirects to the German quoka.de (checked 2026-10-28)
- **EHL, JP Immobilien, Otto Immobilien** — premium agency Wien
- **immo.tt.com** Tirol-specific

## Caveats unique to AT

- **Ausländergrunderwerb** (foreign buyer rules): non-EU/EEA buyers need a **grundverkehrsbehördliche Genehmigung** in some Bundesländer (esp. Tirol, Salzburg, Vorarlberg), granted by the Bezirksverwaltungsbehörde in Tirol (§ 26 TGVG 1996), by the Grundverkehrsbeauftragte(r) in Salzburg (Grundverkehrskommission for farm/forest land; § 20 Abs 3 S.GVG 2023) and by the Grundverkehrs-Landeskommission in Vorarlberg (§ 13 Abs 2 GVG) — an **approval regime with no quota and no percentage cap**. Tirol equates EU/EEA nationals with Austrians outright (§ 3 TGVG); Salzburg and Vorarlberg exempt acquisitions made in exercise of EU/EEA freedoms, including free movement of capital (§ 22 S.GVG; § 3 Vbg GVG). Do not conflate it with the nationality-neutral second-home thresholds below — they are two distinct regimes. (2026-10-21 verified; source RIS konsolidiertes Landesrecht: TGVG 1996, S.GVG 2023, Vorarlberg GVG)
- **Zweitwohnsitz-/Freizeitwohnsitz-Schwellen** (nationality-neutral — NOT a foreign-buyer quota): **Tirol** — new Freizeitwohnsitze may not be declared permissible once the Freizeitwohnsitz share exceeds **8 v.H.** of total dwellings per the last Gebäude- und Wohnungszählung (§ 13 Abs 5 lit a TROG 2022, consolidated version in force 7 Jul 2026, LGBl 43/2022 as amended by LGBl 51/2026). **Salzburg** — Zweitwohnung-Beschränkungsgemeinden are communes where non-Hauptwohnsitz dwellings exceed **16 %** of the total stock (§ 31 Abs 1 Z 1 ROG 2009, in force 1 Mar 2023, LGBl 95/2022), designated by Landesregierung-Verordnung **every five years** on the five-year arithmetic mean at Stichtag 31 Oct — not annually; a Gemeinde may apply to have its percentage raised. No tightening verified through 21 Oct 2026 (Tirol LGBl 51/2026, kundgemacht 6 Jul 2026, is a building/energy-law omnibus whose TROG article also reworded § 13 Abs 1 and added a § 13 Abs 8 Ausnahmebewilligung ground for lifetime gifts to statutory heirs where the donor kept a residential servitude until death; the 8 v.H. cap is unchanged. Salzburg ROG amendment LGBl 79/2026 touches only §§ 5 Z 2, 53 Abs 2 Z 11, 60 Abs 1 und 5 and 88 Abs 9). (2026-10-21 verified; source [RIS ROG 2009 § 31](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=LrSbg&Gesetzesnummer=20000615&Paragraf=31) + RIS konsolidiertes Landesrecht Tirol)
- **Naturschutz** restrictions on alpine constructions — strict
- **MRG categories** make rental investment math depend heavily on building age
- **Mietkauf** model (rent-to-own via Genossenschaft) common
- **Mortgage lending rules (`--finance`)**: the binding KIM-Verordnung caps expired on **30 Jun 2025**; the FMA WIK-Rundschreiben (26 Jun 2025) keeps max **90 % Beleihungsquote**, max **40 %** of annual net income as debt service and max **35-year** term as the standard, but banks may now deviate where lending stays solid (FMA). FMSG monitoring of loans outside these criteria: see shared/regulatory-watch.md (AT finance entry; no FMSG press release after the 50th session of 14 Sep 2026 as of 2026-10-28)
- **HORA portal is free, all-hazards-in-one-place, with a HORA-Pass for any location** — use it as the first screen, not the single source of truth: BMLUK calls it a complement to the parcel-sharp Gefahrenzonenpläne, so also check the Gemeinde's Gefahrenzonenplan and the WISA RMP2027 flood maps
- **Erbenermittlung** can stall purchases for months if Grundbuch unclear
- **Bauernhof** (farm) special restrictions; Anerbenrecht
- **Schenkungsmeldepflicht** (§ 121a BAO as introduced by BGBl I 85/2008, for gifts after 31 Jul 2008): gifts of cash, receivables, shares, businesses, movables and intangibles must be notified to the Finanzamt (exempt up to €50,000 a year between relatives, €15,000 within five years otherwise); land is not on the list — a gift of land falls under the GrESt Stufentarif instead (see `--tax`)
- **Tourismusabgabe** per Gemeinde — affects rental margins
- **Grundverkehr** approval for non-EU/EEA buyers in some Bundesländer (esp. Tirol, Salzburg, Vorarlberg) — see Ausländergrunderwerb above; an approval regime, not a quota
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
- **Anerbenrecht**: the federal Anerbengesetz governs inheritance of Erbhöfe in every Land except Kärnten and Tirol (§ 21 AnerbenG), which have the Kärntner Erbhöfegesetz 1990 and the Tiroler Höfegesetz

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
