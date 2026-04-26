# Germany 🇩🇪 — Property Due-Diligence Playbook

ISO2: `de`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (PLZ)**: 5 digits (e.g., `10117` Berlin Mitte, `80331` München, `60311` Frankfurt)
- **Admin levels**: 16 Bundesländer → 401 Landkreise (rural districts) + kreisfreie Städte → 10,786 Gemeinden
- **Currency**: EUR (€)
- **Languages**: German (with Sorbian, Frisian, Danish minority pockets)
- **Cadastre**: **Liegenschaftskataster** + **ALKIS database** (Bundesländer-managed; not centralized)
- **Identifier**: Flurstücksnummer per Gemarkung
- **CRITICAL**: Federal structure — **every Bundesland has different rules** for tax + planning + flood zoning. Always check the specific state.
- Distinct ownership types: **Eigentumswohnung (Wohnungseigentum)** = condominium with common parts; **Sondereigentum** + **Miteigentumsanteil**; **Erbbaurecht** (leasehold ground) common in older cities

## Section: `--price`

### Primary sources

- **BORIS-D (Bodenrichtwertinformationssystem für Deutschland)** — FREE federal portal:
  - Portal: `https://www.bodenrichtwerte-boris.de/`
  - Aggregates Bodenrichtwerte (official land values, set every 2 yrs by Gutachterausschüsse) from 12 of 16 Bundesländer
  - Data License Germany — free for any use
- **State-specific BORIS portals** (often more detailed):
  - Berlin: `https://fbinter.stadt-berlin.de/boris/`
  - Bayern: `https://www.boris-bayern.de/`
  - NRW: `https://www.boris.nrw.de/borisplus/`
  - Hamburg: `https://geoportal-hamburg.de/boris/`
  - Brandenburg: `https://boris.brandenburg.de`
  - Hessen: `https://www.bodenrichtwerte-hessen.de/`
- **Gutachterausschüsse Marktberichte** (annual Bundesländer reports — sometimes paid)
- **Vergleichswertverfahren databases** for comp sales

### Listing platforms

- **ImmobilienScout24** — largest: `https://www.immobilienscout24.de/Suche/de/<bundesland>/<stadt>/haus-kaufen` or `/wohnung-kaufen`
- **Immowelt**: `https://www.immowelt.de/`
- **Kleinanzeigen.de** (formerly eBay Kleinanzeigen): `https://www.kleinanzeigen.de/s-haus-kaufen/c208`
- **Engel & Völkers, von Poll** — premium agency networks
- **Immonet, Immowelt-Group**

### Price benchmarks (Q4 2025 / Q1 2026 reference)

- **Destatis Häuserpreisindex** (HPI): `https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Baupreise-Immobilienpreisindex/_inhalt.html`
- **Bundesbank Wohnimmobilienpreise**: `https://www.bundesbank.de/`
- **vdp Immobilienpreisindex**: `https://www.pfandbrief.de/`
- 2025 typical (€/m² for Wohnungen):
  - München: 9,000–12,000 €/m²
  - Frankfurt am Main: 6,500–8,500 €/m²
  - Hamburg: 6,000–8,000 €/m²
  - Berlin: 5,500–7,500 €/m²
  - Stuttgart: 5,500–7,000 €/m²
  - Köln: 5,000–6,500 €/m²
  - Düsseldorf: 5,000–6,500 €/m²
  - Smaller cities: 2,500–4,500 €/m²
  - Rural East Germany: 1,000–2,500 €/m²

### Compute

1. Listing €/m² = listing price / Wohnfläche (legal definition: WoFlV — Wohnflächenverordnung)
2. **Trap**: Wohnfläche calculation includes balconies/terraces at 25–50 % weighting; varies by listing
3. **Trap**: Nutzfläche ≠ Wohnfläche; Bruttogrundfläche different again
4. Compare to local Bodenrichtwert (BORIS) for the Gemarkung — but BORIS is land-only, not building
5. Vergleichswertverfahren = comparable-sales method; common appraisal route

---

## Section: `--traffic`

### Primary sources

- **BASt (Bundesanstalt für Straßenwesen)** — federal trunk roads (Autobahnen + Bundesstraßen):
  - Portal: `https://www.bast.de/`
  - Data: `https://www.bast.de/DE/Publikationen/Statistik/Verkehrsdaten/Manuelle-Zaehlung.html`
  - Annual SVZ (Straßenverkehrszählung) every 5 yrs (2010, 2015, 2021, etc.)
- **Bundesländer Verkehrszählung** (state roads):
  - Bayern: `https://www.lfv.bayern.de/`
  - NRW: `https://www.strassen.nrw.de/`
  - Berlin: SenStadt `https://www.berlin.de/sen/uvk/`
  - All states have own portals
- OSM `highway` class fallback

### Key term

**DTV (Durchschnittlicher täglicher Verkehr)** = AADT-equivalent
**SV-Anteil** = heavy vehicle share %

### Verdict bands

- 🟢 < 1,000 v/d (Wohnstraße, kleine Landstraße)
- 🟡 1,000–8,000 v/d (Kreis-/Landstraße, Hauptstraße im Wohngebiet)
- 🟠 8,000–30,000 v/d (Bundesstraße, urban arterial)
- 🔴 > 30,000 v/d (Autobahn, urban core, Stadtringe)

---

## Section: `--tax`

### Annual property tax — Grundsteuer (MAJOR REFORM 2025)

**As of 1 January 2025** the new Grundsteuerreform took effect. Existing property tax assessments invalid; all properties revalued.

**Patchwork of 6 calculation models** across the 16 Bundesländer:

| Model | Bundesländer | Method |
|---|---|---|
| **Bundesmodell** (federal) | Berlin, Brandenburg, Bremen, MV, NRW, RLP, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Property tax value × Steuermesszahl × Hebesatz |
| **Flächenmodell** (Bayern) | Bayern only | Flat per-m² rate × usage type × Hebesatz |
| **Wohnlagenmodell** (Hamburg) | Hamburg | Federal model + location bonus/malus |
| **Bodenwertmodell** (Baden-Württemberg) | BW only | Pure land value × Steuermesszahl × Hebesatz |
| **Flächen-Faktor-Verfahren** (Hessen) | Hessen | Bayern model + location factor |
| **Flächen-Lage-Modell** (Niedersachsen) | NS | Modified Bayern + location |

### Federal model formula

```
Grundsteuer = Grundsteuerwert × Steuermesszahl × Hebesatz
```

- **Grundsteuerwert** (property tax value): determined by Finanzamt based on Grundsteuererklärung (filed 2022-2023 deadline)
- **Steuermesszahl** (basic federal rate): 0.031 % (3.1 ‰) residential / 0.034 % (3.4 ‰) non-residential
- **Hebesatz** (municipal multiplier): set by each Gemeinde, range 200–1,050 % (typical residential 350–500 %)

### Example (Berlin, federal model)

100 m² Wohnung in Mitte, Grundsteuerwert ~250,000 €:
- 250,000 × 0.00031 × 4.70 (Berlin Hebesatz 470 %) = **364 €/yr**

### Transaction taxes — Grunderwerbsteuer

| Bundesland | Rate |
|---|---:|
| **Bayern** | **3.5 %** (lowest) |
| **Sachsen** | **3.5 %** |
| Hamburg | 4.5 % |
| Bremen | 5.0 % |
| Niedersachsen, RLP | 5.0 % |
| Baden-Württemberg | 5.0 % |
| **Berlin** | **6.0 %** |
| Sachsen-Anhalt, Hessen, Thüringen, Saarland | **6.5 %** |
| **Brandenburg, NRW, Schleswig-Holstein** | **6.5 %** (highest) |

### Notarkosten + Grundbucheintrag

- **Notarkosten**: ~1.0–1.5 % (set by GNotKG fee schedule)
- **Grundbucheintragung**: ~0.5 % (court fee per GKG)
- Combined: **~1.5–2.0 %**

### Maklerprovision

Since 23 Dec 2020 (Bestellerprinzip): typically split 50/50 between buyer + seller in residential:
- **3.57 % × 2 = 7.14 %** total (incl. 19 % VAT) for typical residential, paid 50/50

### Total transaction cost (buyer side)

**~9–13 %** typical:
- 3.5–6.5 % Grunderwerbsteuer
- 1.5–2.0 % notary + Grundbuch
- 3.57 % Makler (often)

→ One of the **highest transaction-cost countries in Europe**.

### VAT (USt.)

- 19 % standard
- 7 % reduced (food, books — not real estate)
- New residential property usually exempt; commercial: 19 %

### Future risk

- 2024-2025 Grundsteuerreform results uncertain — many landlords face higher bills, some lower
- Solidaritätszuschlag (no longer applies to most income tax payers)
- Discussions about Erbschaftsteuer on real estate periodically resurface

---

## Section: `--rental`

### Long-term residential

**Mietspiegel** (rent index) — official benchmark per city:
- Berlin: `https://www.stadtentwicklung.berlin.de/wohnen/mietspiegel/`
- München: `https://stadt.muenchen.de/service/`
- Most major cities have qualifizierter Mietspiegel (legally binding)
- Smaller cities have einfacher Mietspiegel (advisory)

**Mietpreisbremse** (rent control):
- Active in ~400 communities (gespannte Wohnungsmärkte)
- Applies in Berlin, Hamburg, München, Köln, Frankfurt, Stuttgart, Düsseldorf
- Cap: max 110 % of local Mietspiegel for new contracts (with exceptions)
- Extended to 2029 (Bundesregierung 2025)

**Mietendeckel** Berlin (2020-2021): unconstitutional, abolished 2021.

**Tenant rights extreme**:
- Eviction extremely difficult (Kündigungsschutz)
- Indexmieten (CPI-linked) and Staffelmieten (step-rent) regulated
- Mietminderung if defects

### Short-term rentals (Ferienwohnung / Airbnb)

**Zweckentfremdungsverbot** (anti-misuse) increasingly strict:
- **Berlin**: Zweckentfremdungsgenehmigung required since 2014; max 90 days/yr without permit
- **München**: similar permit + Wohnsitz registration required
- **Hamburg**: Zweckentfremdungsverbot, registration mandatory
- **Frankfurt am Main**: Wohnraumversorgungsgesetz Hessen
- Penalty: up to €500,000 in Berlin

**Tax treatment**:
- **§ 21 EStG (Vermietung & Verpachtung)** for non-commercial private rental
- **§ 15 EStG (Gewerbe)** if hotel-style services or 3+ properties — Gewerbesteuer applies
- VAT: short-let < 6 months is **VAT-eligible at 7 %** (reduced) since 2010
- **EU Regulation 2024/1028** transposition expected by May 2026

### Strategic notes

- Mietspiegel + Mietpreisbremse make long-let yields modest in major cities
- Short-let permits hard to obtain in Großstädte
- WEG (Wohnungseigentumsgemeinschaft) often bans short-let in Teilungserklärung
- B&B style under threshold = simpler

---

## Section: `--work=<profession>`

### Job platforms

- **Bundesagentur für Arbeit Jobbörse**: `https://www.arbeitsagentur.de/jobsuche/`
- **StepStone**, **Indeed.de**, **LinkedIn DE**, **XING** (DE-specific business network)
- **Gehalt.de**, **Kununu** for salary benchmarks
- Profession-specific: Doctolib (medical), Hochschulen.de (academic), Handwerkskammer (trades)

### Self-employment regimes

- **Kleinunternehmer** (small business): < €22,000 revenue/yr, no VAT (since 2025: €25,000)
- **Freiberufler** (liberal profession): doctors, lawyers, architects, engineers, journalists, artists — simpler bookkeeping, no Gewerbesteuer
- **Gewerbe** (trade): requires Gewerbeanmeldung at Gewerbeamt; Gewerbesteuer applies
- **GmbH** (limited): min €25,000 capital, half paid up
- **UG (haftungsbeschränkt)**: mini-GmbH, min €1 capital
- **Sozialversicherung**: KSK (Künstlersozialkasse) for arts; Pflicht: Kranken-/Pflege-/Renten-/Arbeitslosenversicherung mostly mandatory; Selbstständige choose private vs gesetzliche Krankenversicherung

### Salary benchmarks (2025)

- Median monthly gross:
  - München: ~€5,500
  - Berlin: ~€4,400
  - Hamburg: ~€4,700
  - Stuttgart, Frankfurt: ~€5,200
  - Smaller cities: ~€3,500–€4,200
  - Eastern rural: ~€3,000–€3,800
- **Mindestlohn 2025**: €12.82/hr (€2,221/mo full-time)

---

## Section: `--risks`

### Primary national + state sources

| Source | URL | What it gives |
|---|---|---|
| **BfG geoportal** Hochwassergefahren+risiko-karten (federal) | `https://geoportal.bafg.de/karten/HWRM_Aktuell/` | All 16 Bundesländer flood maps unified |
| **Hochwasserzentralen.de** | `https://hochwasserzentralen.de/` | Real-time flood warnings |
| **NRW Starkregengefahrenhinweise** | `https://geoportal.de/Info/tk_04-starkregengefahrenhinweise-nrw` | Flash-flood maps |
| **RLP Sturzflutgefahrenkarten** | `https://wasserportal.rlp-umwelt.de/auskunftssysteme/sturzflutgefahrenkarten` | Flash-flood RLP |
| **BBK GeoInformation für Bevölkerungsschutz** | `https://www.bbk.bund.de/` | Civil-protection risk |
| **BfS Radon-Karte** | `https://www.bfs.de/DE/themen/ion/umwelt/radon/karten/` | Radon potential per Gemeinde |
| **DWD Klimaatlas** | `https://www.dwd.de/klimaatlas` | Climate change projections |
| **Erdbebenkarte DIN EN 1998-1** | various Bundesländer geoportals | Seismic zoning (low overall in DE) |
| **BImSchG-Anlagen registry** | per Bundesland Umweltämter | Industrial emissions sites |
| **Altlasten-Kataster** (legacy contaminated sites) | per Bundesland | Brownfield risk |

### Specific risks

- **Hochwasser**: Rhein, Donau, Elbe, Oder valleys — recurring (2002, 2013, 2021 Ahrtal disaster)
- **Starkregen / Sturzflut**: increasing nationally (climate change) — esp. NRW, Rheinland, Saarland
- **Erdbeben** (low overall):
  - **Niederrhein** + **Köln-Bonn area**: moderate (M 5+ historical)
  - **Schwäbische Alb**: moderate
  - Most of Germany: zone 0-1 (very low)
- **Sturm/Orkan** (storms): Atlantic depressions, esp. NW Germany
- **Hagel** (hail): increasing damage, esp. Süddeutschland
- **Bergbau-Folgeschäden** (mining subsidence): Ruhrgebiet, Saarland — long-term subsidence risk
- **Radon**: significant in Erzgebirge, Thüringer Wald, Schwarzwald, Bayerischer Wald, parts of Niedersachsen
- **Borkenkäfer + Waldsterben** (forest pests): rural property neighboring damaged forests

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1949 (Vorkriegsbauten)** | Lead paint, asbestos in Putz/Heraklith, Holzwurm, no thermal insulation |
| **1949–1965 (Nachkriegsbauten)** | Asbestos roof tiles + Eternit, lead pipes, Spannbeton |
| **1965–1979** | Hochbau-Asbest very common (insulation, ceiling tiles, vinyl floors), formaldehyde from Spanplatten |
| **1979–1995** | Asbestos phased out (banned 1993); PCB in Fugendichtmasse, Mineralfaser issues |
| **1995–2002** | EnEV thermal standards begin; better materials |
| **2002–2014** | EnEV revisions tightening; modern materials |
| **Post-2014** | EnEV/GEG strict; nZEB approaching |
| **Post-2024 (GEG)** | 65 % renewable energy mandate for new heating systems |

**Asbestos**: pre-1995 buildings highly likely; remediation cost €30–€100/m² for friable; €15,000–€80,000 typical for small house

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energieausweis** (GEG/EnEV) | All sales | 10 years |
| **Grundbuchauszug** | Verify owner + Belastungen | Free for owner; €10 for current |
| **Flurkarte** (Liegenschaftskarte) | Boundaries | per state |
| **Teilungserklärung + Aufteilungsplan** | If WEG (apartments) | At sale |
| **Wohnflächenberechnung** | Residential | at sale |
| **WEG-Protokolle + Wirtschaftsplan** (last 3 yrs) | If apartment | At sale |

### Climate change projections (DWD)

- +1.4–4.7 °C by 2100 vs 1971–2000 (RCP scenarios)
- Heat waves: massively up, esp. urban
- Precipitation: drier summers, wetter winters; +Starkregen events
- Flood risk +20–40 % in Mittelgebirge regions
- Hagelrisiko increasing in Süddeutschland
- Coast: Nordsee + Ostsee sea-level rise affecting Schleswig-Holstein, Niedersachsen, MV

---

## Section: `--mains`

### Sources

- **Bundesverband der Deutschen Gas- und Wasserwirtschaft (BDEW)**: `https://www.bdew.de/`
- **DVGW** (Deutscher Verein des Gas- und Wasserfaches): `https://www.dvgw.de/`
- Each Gemeinde has own Stadtwerke or contracts to Veolia/Berliner Wasserbetriebe/Energie & Wasser/etc.
- Major operators: BWB Berlin, Hamburg Wasser, MVV Mannheim, Rheinenergie Köln, REWAG Regensburg

### Verification

- Most städtische Bebauungsgebiete: mains universal
- Rural Bayern, MV, Brandenburg outskirts: some Sammelgrube / Kleinkläranlage
- **Anschlussbescheid** required at sale (proof of public sewer connection)

### Costs

| Scenario | Cost (€) |
|---|---:|
| Anschluss to mains (where available) | 2,000–8,000 |
| Trunk line extension if needed | 5,000–25,000+ (usually not buyer-borne) |
| Kleinkläranlage compliant (BImSchV) | 8,000–18,000 |
| Sammelgrube replacement | 3,000–10,000 |

---

## Cost benchmarks (DE 2026)

| Work | Cost (€) |
|---|---:|
| Energieausweis Verbrauchsausweis | 50–150 |
| Energieausweis Bedarfsausweis | 250–600 |
| Notarkosten + Grundbuch | 1.5–2.0 % of price |
| Grunderwerbsteuer | 3.5–6.5 % (varies Bundesland) |
| Maklerprovision (50/50 buyer side) | 3.57 % typical |
| **Total transaction cost** | **9–13 %** of price |
| Asbestsanierung (small house) | 15,000–80,000 |
| Energetische Sanierung Klasse C → A | 60,000–120,000 |
| Heizungstausch (Wärmepumpe) — incl. BAFA Förderung | 25,000–40,000 |
| Dachsanierung (200 m²) | 25,000–50,000 |
| Fenster komplett (15 Stück) | 12,000–25,000 |

## Active fiscal incentives (2025-2026)

- **BAFA Förderung Wärmepumpe**: up to 70 % of cost (cap €30k)
- **KfW Kredit + Tilgungszuschuss** (Effizienzhaus 40/55): zinsgünstige Kredite
- **BEG (Bundesförderung effiziente Gebäude)**: comprehensive retrofit grants
- **GEG 65-%-Erneuerbare-Pflicht**: from 2024 for new heating systems
- **Sonder-AfA für Mietwohnungsbau** (special depreciation): 5 %/yr × 4 yrs for new builds in Wohnraum-Mangelgebieten

## Common listing platforms

- **ImmobilienScout24** — biggest, full extraction
- **Immowelt + Immonet** (same group)
- **Kleinanzeigen.de** — privates, lower commission
- **Engel & Völkers, von Poll, Sotheby's** — premium agency
- **Maklerverbund-IVD, AfP** — networks

## Caveats unique to DE

- **Federal patchwork**: every Bundesland has different rules — always check state-specific
- **Grundsteuerreform 2025**: live now; many owners face changed bills
- **Mietpreisbremse + Kündigungsschutz** make landlord-friendly investments harder than US/UK
- **Zweckentfremdungsverbot** kills short-let in major cities
- **Erbbaurecht** common in Berlin, Hamburg, München (90-99 yr leasehold) — affects valuation
- **WEG (Wohnungseigentumsgemeinschaft)** for any Eigentumswohnung — Hausgeldkalkulation + Rücklagenbestand mandatory due-diligence
- **Sondereigentum vs Gemeinschaftseigentum** distinction critical
- **Altlasten-Kataster** (contaminated land registry) — check at Bundesland Umweltamt
- **Erdbeben Köln-Bonn / Niederrhein** zone — newer than perceived
- **2024 GEG**: 65 % renewable for new heating + retrofit when boiler dies — major retrofit cost
- **Solidaritätszuschlag** mostly abolished but still applies for high earners
- **Tax-secrecy is strong** — getting Grundsteuerwert before purchase difficult; ask seller

## Reddit / forum sources

- **r/Finanzen**, **r/germany**, **r/de** (German-language)
- **r/AskGermany**, **r/expat_to_Germany**
- **WG-Gesucht** for rental market reality
- **Selbstständig.de**, **Existenzgründer.de** for business
- Expat: **The Local Germany**, **Expatica DE**, **Berlin Spectator**

## Verification authorities

| Authority | When to call |
|---|---|
| **Grundbuchamt** (district court) | Title verification, encumbrances |
| **Stadtplanungsamt / Bauamt** | Bebauungsplan, permits, Bauantrag history |
| **Finanzamt** | Grundsteuer assessment |
| **Notar** | Final transfer, escrow, due-diligence on Belastungen |
| **Stadtwerke** (local utility) | Mains drains verification |
| **Untere Wasserbehörde** (Bundesland) | Flood zone verification |
| **Untere Bodenschutzbehörde** | Altlasten check |
| **Hausverwaltung + WEG** | If apartment: Hausgeld, Rücklagen, ToP-Liste |

## Quirks to know

- **Bebauungsplan vs RNU vs FNP**: 3-tier planning; check at Bauamt
- **Bestandsschutz**: existing structure may be grandfathered; modifications trigger current rules
- **Erschließungskosten** (development charges): one-time per Gemeinde when streets/sewers added
- **Grundbuchblatt**: structured Abteilung I (owner), II (encumbrances), III (mortgages) — read in order
- **Sondernutzungsrecht**: parking/garden assigned to specific Wohnung in Teilungserklärung
- **Verkehrswert** vs **Beleihungswert**: market value vs lendable value (banks use latter)
- **Spekulationsfrist**: 10-yr capital gain holding period for non-owner-occupied
- **Eigenbedarf**: only legal eviction reason for tenants
- **Grundbuchsperre** can freeze sales in Erbbaurecht situations

## Source URL templates

| Source | URL pattern |
|---|---|
| BORIS-D federal | `https://www.bodenrichtwerte-boris.de/` |
| BORIS Berlin | `https://fbinter.stadt-berlin.de/boris/` |
| BORIS NRW | `https://www.boris.nrw.de/borisplus/` |
| BORIS Bayern | `https://www.boris-bayern.de/` |
| ImmobilienScout24 search | `https://www.immobilienscout24.de/Suche/de/<bundesland>/<stadt>/<typ>` |
| BfG Hochwasserportal | `https://geoportal.bafg.de/karten/HWRM_Aktuell/` |
| BfS Radon-Karte | `https://www.bfs.de/DE/themen/ion/umwelt/radon/karten/` |
| Destatis HPI | `https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Baupreise-Immobilienpreisindex/_inhalt.html` |
| BAFA Förderung | `https://www.bafa.de/` |
| KfW Förderung | `https://www.kfw.de/` |
| BBK | `https://www.bbk.bund.de/` |
| DWD Klimaatlas | `https://www.dwd.de/klimaatlas` |
| Bundesagentur Jobs | `https://www.arbeitsagentur.de/jobsuche/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (post-2025 Grundsteuerreform stable; BORIS-D + BfG well-maintained). MEDIUM for short-let regulation (EU 2024/1028 transposition expected May 2026; city-by-city rules evolving).

## Extension TODOs

- [ ] Per-Bundesland Grundsteuer model details + Hebesatz tables for top 100 Gemeinden
- [ ] Mietspiegel extraction patterns per major city
- [ ] Zweckentfremdungsverbot rules per major city (deeper)
- [ ] Erbbaurecht detection from Grundbuch
- [ ] Per-Bundesland Hochwasserkarte URL specifics (Bayern, Hessen, Baden-Württemberg)
- [ ] WEG-Gesundheitscheck heuristics (Hausgeld, Rücklagen, Streitigkeiten)
- [ ] Altlasten-Kataster regional access patterns
