# Switzerland 🇨🇭 — Property Due-Diligence Playbook

ISO2: `ch`. Status: ✅ Fully populated (researched 2026-04; Tier-A quarterly refresh 2026-07-03 — fast-moving claims re-verified, structural sections unchanged).

## Country profile

- **Postcode (PLZ/NPA)**: 4 digits (`8001` Zürich, `1201` Genève, `4001` Basel)
- **Admin levels**: 26 cantons (high autonomy) + 2,100+ communes (Gemeinden / communes)
- **Currency**: **CHF** (Swiss franc); 1 EUR ≈ 0.95 CHF (variable, often near parity)
- **Languages**: German (62 %), French (23 %), Italian (8 %), Romansh (0.5 %); 4 official
- **Cadastre**: cantonal Grundbuch + **swisstopo** (Bundesamt für Landestopografie)
- **Identifier**: Grundbuchblatt-Nummer + Liegenschafts-Nr. per commune
- **Federal structure** — most rules are cantonal; **massive variation** across 26 systems
- **Switzerland is NOT in EU** (just EEA-adjacent through bilateral agreements)
- Distinct ownership types: **Eigentum** (freehold), **Stockwerkeigentum** (commonhold apartment, since 1965), **Bauernrecht/Baurecht** (leasehold ground)

## Section: `--price`

### Primary sources

- **Comparis** (consumer aggregator): `https://en.comparis.ch/immobilien`
- **Homegate** (largest listings): `https://www.homegate.ch/`
- **ImmoScout24.ch**: `https://www.immoscout24.ch/`
- **Wüest Partner Marktanalysen**: `https://www.wuestpartner.com/`
- **Fahrländer Partner**: `https://www.fpre.ch/`
- **Newhome.ch**, **RealAdvisor**
- **BFS (Bundesamt für Statistik)** Wohnkostenindex + Immobilienpreisindex: `https://www.bfs.admin.ch/`
- **SNB (Swiss National Bank)** financial stability reports + quarterly monetary-policy assessments (policy rate 0% since Jun 2025, held 18 Jun 2026 and 24 Sep 2026): `https://www.snb.ch/en/publications/communication/press-releases-restricted/pre_20260924` (2026-09-24 verified)
- **Cantonal Grundbuchämter** for actual sale-price extracts (paid)

### Listing/agency networks

- **UBS, ZKB, Raiffeisen**: bank-affiliated brokerage
- **Engel & Völkers Schweiz, Sotheby's**: premium
- **Properstar**, **ApartHotel**

### Price benchmarks (2025-2026)

> est. ranges aggregated from Comparis / Homegate / ImmoScout24 asking-price listings 2025-2026 (see Primary sources, L21-29) — asking, not transaction; verify with cantonal Grundbuchamt sale-price extracts.
>
> Market direction (BFS IMPI Q3 2026, Q4-2019 = 100): +4.4 % YoY, +1.7 % QoQ to 129.8 points; single-family houses +2.1 % and flats +1.3 % QoQ; urban communes of small or non-agglomerations rose most (+3.4 % QoQ), intermediate communes least (+0.6 %). Asking ranges below trend upward. (2026 data, source [BFS Medienmitteilung 27 Oct 2026](https://www.bfs.admin.ch/de/newnsb/zEeBMwJlPOBh))

| Region | EFH €/m² (CHF) | Wohnung €/m² (CHF) |
|---|---:|---:|
| **Zürich City** | 14,000–22,000 | 14,000–25,000 |
| **Genève** | 13,000–20,000 | 13,000–22,000 |
| **Zug** | 14,000–20,000 | 14,000–22,000 |
| **Basel** | 9,000–14,000 | 9,000–15,000 |
| **Bern** | 7,000–11,000 | 7,500–12,000 |
| **Lausanne** | 9,500–14,000 | 10,000–15,000 |
| **Lugano** | 7,500–12,000 | 8,000–14,000 |
| **St. Gallen** | 6,000–9,000 | 6,500–10,000 |
| Rural alpine | 4,000–8,000 | 4,500–10,000 (resort towns higher) |

### Compute

1. Price/m² = listing CHF / Wohnfläche (per Bauberufe)
2. **Trap**: NWF (Nettowohnfläche) vs BGF (Bruttogeschossfläche) vs HNF (Hauptnutzfläche)
3. **Trap**: Stockwerkeigentum has Wertquote (share %) determining Hauseigentum-Beteiligung — important
4. Compare to canton-specific Wüest Partner / Comparis index

---

## Section: `--traffic`

### Sources

- **ASTRA (Bundesamt für Strassen)** — federal roads + autobahnen: `https://www.astra.admin.ch/`
- Cantonal Tiefbauämter — state roads
- Major cities: Zürich Gemeinde Verkehrsamt, Genève direction des routes, etc.

### Key term

**DTV (Durchschnittlicher täglicher Verkehr)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (Wohnstrasse, Bergstrasse)
- 🟡 1,000–8,000 v/d (Kantonsstrasse, Stadtstrasse)
- 🟠 8,000–30,000 v/d (Hauptstrasse, urban arterial)
- 🔴 > 30,000 v/d (Autobahn N1/A1, urban core, Stadtumfahrung)

---

## Section: `--tax`

### MAJOR REFORM 2025: Eigenmietwert ABOLISHED

**Federal popular vote 28 September 2025 → 57.7 % YES** to abolish Eigenmietwert (imputed rental value taxation on owner-occupied homes).

- **Implementation: FIXED 1 January 2029** — the Federal Council set the entry-into-force date at its **1 April 2026** session; a 2028 start is off the table (2029 was chosen so cantons *can* introduce the linked second-home Objektsteuer simultaneously). Owner-occupied maintenance deductions + federal energy/environment deductions fall away from the same date; rented/leased property keeps the maintenance deduction; time- and amount-limited Ersterwerberabzug (mortgage-interest deduction) for first-time buyers. (2026-07-03 verified, source [admin.ch Medienmitteilung 1 Apr 2026](https://www.admin.ch/de/newnsb/yGTqBPowRqyVh0zPokW-q))
- Applies to **primary AND secondary residences**
- Owner-occupiers no longer declare notional rental income
- **BUT**: deductions for maintenance/renovations also eliminated
- **Cantons can introduce special property tax on second homes** (constitutional change passed alongside)
- Regional split: French-speaking cantons all voted NO; German-speaking (except Basel-Stadt) voted YES

### Annual property tax — before + from 2029

**Until 31 Dec 2028 (current)**:
- **Eigenmietwert** (imputed rental income): about 60–70 % of the rent a comparable home would fetch (2026-11-25 verified, source [ch.ch](https://www.ch.ch/de/steuern-und-finanzen/steuerarten/immobiliensteuer)) → added to taxable income → taxed at the owner's marginal income-tax rate (federal + cantonal + communal), which depends on canton, commune and income — run your case in the [ESTV tax calculator](https://swisstaxcalculator.estv.admin.ch/)
- **Liegenschaftssteuer** (cantonal property tax) — exists in some cantons:
  - **Genève**: 1 ‰ of valeur fiscale for private owners, cut to 0.2 ‰ if it is your main residence; companies 1–2 ‰ (impôt immobilier complémentaire; 2026-11-25 verified, source [ge.ch](https://www.ge.ch/impot-proprietaires-immobiliers/impot-immobilier-complementaire))
  - **Vaud**: up to 1.5 ‰ of the estimation fiscale (communal impôt foncier under the LICom; 2026-11-25 verified, source [vd.ch](https://www.vd.ch/etat-droit-finances/impots/impots-pour-les-individus/les-impots-les-differents-types-dimpots/impot-foncier))
  - **Tessin/Ticino**: 1 ‰ of the official valore di stima, no debt deduction (communal imposta immobiliare, Art. 291 ff. LT; source: older [Gran Consiglio report](https://m4.ti.ch/fileadmin/POTERI/GC/allegati/rapporti/9193_6133R-magg.pdf) — rates/figures may have changed since; verify with the commune)
  - **Zürich, Bern, Aargau, Schwyz**: NO Liegenschaftssteuer
  - Most cantons: low to moderate
- **Vermögenssteuer** (wealth tax): cantonal + communal; the property's value is declared as wealth and mortgage debt is deducted (2026-11-25 verified, source [ch.ch](https://www.ch.ch/de/steuern-und-finanzen/steuerarten/immobiliensteuer)); rates vary hugely by canton and commune — run your case in the [ESTV tax calculator](https://swisstaxcalculator.estv.admin.ch/)
- **Eigenmietwert + Vermögenssteuer** combined **est. ~0.5–1.5 %** of property value/yr for owner-occupiers (model composite of the Eigenmietwert income-tax effect (L97) + Vermögenssteuer (L104) — illustrative, canton- and income-dependent; verify per canton)

**From 1 Jan 2029 (after Eigenmietwert abolition)**:
- No more Eigenmietwert imputed income
- Vermögenssteuer continues
- New **cantonal property tax on second homes** likely (each canton decides)
- Many alpine cantons (Wallis, Graubünden, Tessin) likely introduce strong second-home tax

### Transaction taxes

**Handänderungssteuer** (transfer tax) — cantonal, varies massively:

> Rates per the ESTV Steuerinformation [«Handänderungssteuer»](https://www.estv2.admin.ch/stp/ds/d-handaenderungssteuer-de.pdf) (2022 data, state of law 1 Jan 2022 — rates/figures may have changed since); Vaud re-verified 2026-11-25 against vd.ch. Zürich and a few other cantons levy only a land-register fee instead of a transfer tax; Schwyz levies neither. Notary, land-register and mortgage-deed fees come on top — verify per canton (cantonal Steuerverwaltung / Grundbuchamt).

| Canton | Rate |
|---|---:|
| **Zürich** | **0 %** (abolished 2005) |
| **Schwyz** | **0 %** |
| **Bern** | **1.8 %** |
| **Basel-Land** | 2.5 % (owed half each by seller and buyer) |
| **Basel-Stadt** | 3.0 % |
| **Genève** | **3.0 %** (collected by the notary and passed on to the buyer; land-register fee extra — rate not confirmed, verify at https://www.ge.ch/impot-proprietaires-immobiliers) |
| **Vaud** | **2.2 % cantonal + up to 1.1 % communal Zuschlag** (max 3.3 % combined; varies by commune) (2026-11-25 verified, source [vd.ch](https://www.vd.ch/etat-droit-finances/impots/impots-pour-les-individus/les-impots-les-differents-types-dimpots)) |
| **Neuchâtel** | **3.3 %** (buyer-paid; reduced rate if the buyer uses the home as main residence for at least two years) |
| **Wallis** | 1.0–1.5 % cantonal (progressive with property value; buyer-paid); communes may add a surcharge of up to 50 % of the cantonal tax |
| **Ticino** | 1.1 % (1.3 % above two million francs; one levy, 1/8 land-register fee and 7/8 tax) |

**Notarkosten + Grundbuchgebühr**: set by each canton — Zürich charges a 1 ‰ land-register fee + 1 ‰ notarisation fee = 2 ‰ = 0.2 % of market value (computed, 2022 data, source ESTV — rates/figures may have changed since); mortgage-deed fees come on top if financed — get the notary's quote
**Maklerprovision**: 2–3 %, usually paid by seller — freely negotiated (listing-portal guidance, source [Homegate](https://www.homegate.ch/c/de/ratgeber/verkaufen/makler/maklerprovision), read 2026-11-25; the same guide's FAQ puts it at 3–5 %); agree it in the Maklervertrag

### Total transaction cost (buyer side)

- Depends heavily on canton: no transfer tax in Zürich and Schwyz, up to 3.3 % in Vaud and Neuchâtel (see table), plus notary fees, land-register fees where charged and, if financed, mortgage-deed fees
- Vaud, Genève, BS: the transfer tax alone is 3.0 % in Genève and Basel-Stadt and up to 3.3 % in Vaud (see table); notary, land-register and mortgage-deed fees come on top — get the notary's estimate
- Zürich, Schwyz: no Handänderungssteuer; Zürich charges a 1 ‰ land-register fee + 1 ‰ notarisation fee = 2 ‰ = 0.2 % of value (computed, 2022 data, source ESTV — rates/figures may have changed since), plus mortgage-deed fees if financed; Schwyz charges no land-register fees either, so notary costs dominate

### MwSt. (VAT)

- 8.1 % standard (raised from 7.7 % in 2024)
- 3.8 % special rate (Beherbergung / hotel + short-let accommodation) — set in Art. 25 Abs. 4 MWSTG only to 31 Dec 2027; Parliament voted on 2 Oct 2026 to extend it to 31 Dec 2031 (BBl 2026 2723), in force 1 Jan 2028 if no referendum is lodged by the 21 Jan 2027 deadline; if the extension fails, accommodation pays the standard rate from 2028. (2026-10-28 verified, source [BBl 2026 2723](https://www.fedlex.admin.ch/eli/fga/2026/2723/de) + [Erläuterungen des Bundesrates, vote of 29 Nov 2026](https://www.admin.ch/dam/de/sd-web/HXhFMFWOaa6u/BAR_Erlaeuterungen_Nov26_DE_v10.pdf))
- 2.6 % reduced (food, books)
- Real estate: sale and rental are exempt from VAT (Art. 21 Abs. 2 Ziff. 20–21 MWSTG); the owner may opt to charge VAT (then 8.1 %), but not where the buyer or tenant uses the property exclusively for housing (2026-11-25 verified, source [ESTV MWST-Steuerpflicht](https://www.estv.admin.ch/de/mwst-steuerpflicht))
- **Pending increase** to part-fund the 13th AHV pension (Parliament final vote 19 Jun 2026): standard 8.1 → 8.5 %, Beherbergung 3.8 → 4.0 %, reduced 2.6 % unchanged; subject to the mandatory popular vote fixed for 29 Nov 2026 (Bundesbeschluss vom 19. Juni 2026; Federal Council and Parliament recommend yes); can enter into force at the earliest at the start of 2028. (2026-10-21 verified, source [admin.ch AHV-Zusatzfinanzierung](https://www.admin.ch/de/ahv-zusatzfinanzierung) + [BSV abstimmung-13-ahv-rente](https://www.bsv.admin.ch/de/abstimmung-13-ahv-rente))

### Capital gains — Grundstückgewinnsteuer

- **Cantonal**, varies by holding period
- est. ~25–50 % at short holding, tapering to ~5–10 % after 20+ years (cantonal — illustrative range, varies widely by canton; verify with the cantonal Steueramt)
- Owner-occupied + reinvestment within 2 yrs often exempt

### Future risk

- **Eigenmietwert abolition** active implementation (1 January 2029, fixed 1 Apr 2026 — see L87 for canonical dates + source) (2026-07-03 verified)
- Cantonal second-home property taxes coming
- Wealth tax rates stable

---

## Section: `--rental`

### Long-term residential

- **Mietrechtliche Vorschriften** (rental law): tenant-protective, esp. Zürich + Genève
- **Mietrecht des OR** (Code of Obligations): caps initial rent in tense markets
- **Anfechtung**: tenants can challenge rent increases
- **Kündigungsschutz**: limited eviction grounds

### Short-let (Ferienwohnung / Airbnb)

**Lex Koller** (Federal Act on the Acquisition of Real Estate by Persons Abroad):
- **Foreign nationals (non-CH residents) face restrictions** on second-home + investment property
- Each canton has annual quota
- **Foreign-law legal entities — Transparency Register precondition (in force 1 Oct 2026)**: a foreign-law legal entity acquiring land within the meaning of Art. 4 BewG must prove its entry in the federal Transparency Register when the purchase is filed with the Grundbuch; without it the land registry suspends the entry, sets a 10-day deadline and then rejects it (Art. 40 TJPG, SR 955.3) (2026 data, source [admin.ch Medienmitteilung 1 Oct 2026](https://www.admin.ch/de/newnsb/L0rkU9ZvCFSw) + [Fedlex SR 955.3](https://www.fedlex.admin.ch/eli/cc/2026/323/de))
- **Zweitwohnungsgemeinden** (>20 % second homes) face additional restrictions under the **Zweitwohnungsgesetz (ZWG, in force 1 Jan 2016)**, implementing **Art. 75b BV** (2012 initiative); ARE publishes each commune's second-home share every March — 331 Zweitwohnungsgemeinden in the ARE release of 31 Mar 2026, and from 2027 ARE computes the shares directly from the federal building and dwelling register (GWR). Lex Koller / BewG quotas: **national annual ceiling 1,500 holiday-home authorisations** to persons abroad; living area normally max **200 m²** and, for holiday homes not held as Stockwerkeigentum (condominium), plot max **1,000 m²** (Art. 10 BewV; up to 250 m² / 1,500 m² with proven need); Wallis (Valais) 330/yr (highest); smallest cantons 20/yr. Swiss citizens, EU/EFTA nationals living in Switzerland (B or C permit) and other foreign nationals with a C permit are not persons abroad and need no authorisation. (2026 data, source [ARE Zweitwohnungen](https://www.are.admin.ch/de/zweitwohnungen) + [ARE Medienmitteilung 31 Mar 2026](https://www.admin.ch/de/newnsb/Hqdc7I9fzT_q-r_RJkn85) + [BewV Anhang 1, SR 211.412.411](https://www.fedlex.admin.ch/eli/cc/1984/1164_1164_1164/de) + [BJ Fragen und Antworten](https://www.bj.admin.ch/de/fragen-und-antworten))
- **PENDING (consultation CLOSED, not yet law):** On **15 April 2026** the Federal Council opened a Vernehmlassung (consultation CLOSED **15 July 2026**) to *tighten* Lex Koller (BewG) — make main-residence purchases by third-country (non-EU/EFTA) nationals permit-liable (with a duty to sell within 2 years of moving away), restrict holiday-home purchases by persons abroad, ban business-real-estate purchases intended for renting/leasing out (own-use stays permit-free), and for the first time bar persons abroad from buying listed housing-company shares and regularly-traded real-estate fund / SICAV units; the draft also contains one easing — hotels' staff housing (Motion 22.4413 Schmid; staff flats no longer needed must be resold within 2 years). Part of the accompanying-measures package the Federal Council adopted in January 2025 alongside its rejection (recommendation to reject) of the «Keine 10-Millionen-Schweiz» initiative — the initiative itself was rejected at the popular vote of 14 June 2026 (45.2 % yes; 8 full cantons yes / 12 no — 2026 data, source BFS OGD federal vote results); the BewG revision is a separate bill and continues. Separately, the Nationalrat adopted point 1 of SVP motion 24.3961 (broader rollback of BewG relaxations; Federal Council proposed rejection) on 22 Sep 2026 (123 yes / 54 no / 17 abstentions — source parlament.ch vote record, Herbstsession 2026) and the motion now sits with the Ständerat Legal Affairs Committee RK-S, assigned 22 Sep 2026 (source parlament.ch Curia Vista 24.3961) — motion only, no bill. **Consultation closed on schedule 15 Jul 2026; submissions (Kantone/Parteien/Organisationen) published 27 Jul 2026; Federal Council now evaluating — no Ergebnisbericht/Botschaft yet.** Consultation → Botschaft → Parliament → optional referendum: NOT enacted; monitor. (2026-08-05 verified, source [admin.ch Medienmitteilung 15 Apr 2026](https://www.admin.ch/de/newnsb/4mzivVX5Ko4dpap06YtuI) + [bj.admin.ch Revision Lex Koller](https://www.bj.admin.ch/de/revision-lex-koller))

**Cantonal patente cantonale** required in many cantons (Genève, Vaud, Zürich):
- Application + tourism tax + safety inspection
- Geneva: max 90 days/yr without commercial license
- Zürich: tightening 2024-2025

**Tax treatment**:
- Income tax + MWST once taxable turnover reaches CHF 100,000/yr: short-let accommodation is taxed at the 3.8 % special rate for Beherbergung (standard rate 8.1 %; pending changes: see MwSt. (VAT) under `--tax`) (2026 data, source [ESTV MWST-Steuersätze](https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz) + [ESTV MWST-Steuerpflicht](https://www.estv.admin.ch/de/mwst-steuerpflicht))
- Tourist tax (Kurtaxe / taxe de séjour), set by each commune or canton: est. ~CHF 3-5 per adult per night in resort communes, children less — e.g. Adelboden CHF 3.00–5.00 per night incl. holiday flats and Airbnb, Goms and Obergoms CHF 4.00 per adult and CHF 2.00 for children 6–16 from 1 Nov 2026 (calibration: two Alpine-resort rate sheets; cities and other communes set their own rates — check the commune's Kurtaxenreglement) (2026 data, source [Kurtaxenreglement Adelboden](https://www.3715.ch/public/upload/assets/1810/Kurtaxenreglement%20EG%20Adelboden%2001.05.2026.pdf?fp=1) + [Goms Tourismus](https://www.goms.ch/artikel/informationsschreiben-neue-kurtaxensaetze-per-01112026))

### Strategic notes

- **Lex Koller restricts foreign buyers** of second homes — major regulatory hurdle
- **Zweitwohnungsinitiative** (accepted 11 Mar 2012): second homes capped at 20 % of each Gemeinde's housing stock — above that share, new flats are in principle allowed only as primary residences or tourist-managed flats (Art. 75b BV; ZWG in force 1 Jan 2016) (2026 data, source [ARE Zweitwohnungen](https://www.are.admin.ch/de/zweitwohnungen) + [ARE Wirkungsanalyse ZWG](https://www.are.admin.ch/dam/de/sd-web/sTXdVFWwgVTT/wirkungsanalyse-zweitwohnungsgesetzbericht-br-de.pdf))
- **Imputed rent abolition** (1 January 2029, fixed 1 Apr 2026 — see L87) changes investment math significantly
- High purchase costs (Vaud, Genève) eat margins

---

## Section: `--work=<profession>`

### Job platforms

- **jobs.ch** (largest)
- **jobup.ch** (French-speaking CH)
- **LinkedIn CH**, **Indeed.ch**, **JobScout24**, **Stepstone.ch**
- **Bundeskanzlei Karriere** (federal): `https://www.admin.ch/`
- Cantonal employment offices

### Self-employment

- **Selbstständigerwerbende** (sole trader): register at AHV-Ausgleichskasse
- **AHV/IV/EO** contributions mandatory
- **Pensionskasse** (BVG) typically not for self-employed
- **GmbH**: min CHF 20,000 capital
- **AG (Aktiengesellschaft)**: min CHF 100,000 capital, 50,000 paid

### Salary benchmarks (2024 wage data)

- Median monthly gross:
  - Zürich: CHF 7,502 for the Zürich region (Swiss median CHF 7,024); jobs in the city of Zürich pay more — CHF 11,164 for men and CHF 8,640 for women (2024 data, source [BFS Lohnstrukturerhebung 2024](https://www.admin.ch/de/newnsb/CzozNgBTCJOrNyvwsItyp) + [Stadt Zürich Statistik](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/statistik-und-daten/daten/bevoelkerung/gleichstellung/erwerbsarbeit/lohn.html) — figures may have changed since)
  - Genève: ~CHF 7,000-8,500 (est. — calibration: BFS 2024 puts the Swiss median at CHF 7,024 and the Zürich region at CHF 7,502, and the Lake Geneva region's top-decile threshold (CHF 12,636) below the Zürich region's (CHF 13,970); verify the Lake Geneva region median at [BFS Löhne](https://statistik.admin.ch/de/themen/arbeit-erwerb/loehne-erwerbseinkommen-arbeitskosten))
  - Bern, Basel: ~CHF 6,500-7,500 (est. — calibration: the 2024 Swiss median of CHF 7,024 sits inside this range; verify the Espace Mittelland and Northwestern Switzerland medians at [BFS Löhne](https://statistik.admin.ch/de/themen/arbeit-erwerb/loehne-erwerbseinkommen-arbeitskosten))
  - Smaller cities: ~CHF 5,700-7,000 (est. — calibration: from the Ticino regional median of CHF 5,708, the lowest BFS region, up to about the Swiss median of CHF 7,024 (BFS 2024); verify regional medians at [BFS Löhne](https://statistik.admin.ch/de/themen/arbeit-erwerb/loehne-erwerbseinkommen-arbeitskosten))
- **Mindestlohn**: no national floor; statutory cantonal minima (1 Jan 2026, indexed annually — verify at cantonal source): Genève ~CHF 24.59/hr, Basel-Stadt ~CHF 22.20, Jura ~CHF 21.40, Neuchâtel ~CHF 21.35, Ticino ~CHF 20.00–20.50 (tiered by sector); Stadt Luzern city-level minimum since 2026 (est. ~CHF 22.00–22.75 — sources disagree, verify); other cantons none (sectoral GAV minima may still apply)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **GUNA Naturgefahrenkarte** (federal) | `https://www.naturgefahren.ch/` | Aggregated alpine + general hazards |
| **swisstopo** | `https://www.swisstopo.admin.ch/` | Geological + topographic + cadastre |
| **swisseo Earthquake hazard** | `https://www.seismo.ethz.ch/` | ETH Zürich Schweizer Erdbebendienst |
| **GIRRES Bundesamt für Umwelt** | `https://www.bafu.admin.ch/` | Environment + flood + landslide |
| **Lawinen** SLF (Institut für Schnee- und Lawinenforschung) | `https://www.slf.ch/` | Avalanche zones |
| **Cantonal Naturgefahrenkarten** | per canton geoportal | Detailed parcel-level hazards |
| **GEOview** (Berner Oberland, etc.) | per canton | Alpine specifics |

### Specific risks

- **Lawinen** (avalanches) — major risk in alpine areas (VS, GR, BE, GL, UR, OW, NW, TI)
  - SLF zones: red (high), blue (medium), white (none)
- **Hochwasser** — Rhein, Aare, Rhone, Reuss, Limmat valleys
- **Erdrutsch / Murgang** (landslide / mudflow) — widespread in mountainous regions
- **Steinschlag** (rockfall) — alpine slopes
- **Permafrost-Schmelze** — alpine foundations affected by permafrost retreat
- **Earthquake** — moderate:
  - **Wallis** + **Basel** highest seismic hazard
  - **Engadin, Ticino, Graubünden** elevated
  - 1356 Basel quake M 6.2 historical reference
- **Hagel** (hail) — increasing damage Mittelland
- **Sturm** — Atlantic + Föhn (alpine wind)

### Build-era hazards

- Pre-1945: lead, asbestos, no thermal envelope, slate roofs
- 1945–1989: asbestos very common, low insulation
- 1990–2010: improving; **MuKEn** (Mustervorschriften der Kantone im Energiebereich) phasing in
- Post-2014 MuKEn 2014: stricter
- Post-2020 MuKEn 2020: nZEB-equivalent

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **GEAK (Gebäudeenergieausweis der Kantone)** | All sales since 2018-2025 (varies canton); some cantons strictly require | 10 years |
| **Grundbuchauszug** | Verify owner + Lasten | At sale |
| **Pläne (Lageplan, Grundriss, Schnitte)** | Standard | At sale |
| **Stockwerkeigentumsreglement + Hausordnung** | If condo | At sale |
| **Schadstoffbericht** | If pre-1990 building (asbestos, PCB, radon) | Recommended |
| **Servitut-Auszug** | Easements | At sale |

### Climate change projections

- +1.0–4.5 °C by 2050 (CH-2018, NCCS scenarios)
- Glacial retreat: significant loss of Alpine ice
- Snow line rising: skiing affected at lower altitudes
- More extreme rainfall + flood events
- Heat waves: Mittelland affected

---

## Section: `--mains`

### Sources

- Each Gemeinde has Wasserversorgung + Abwasserentsorgung
- Major: Wasserversorgung Zürich (WVZ), Industrielle Werke Basel (IWB), SIG Genève (Services Industriels)
- Universal in populated areas; alpine huts on independent systems

### Verification

- Most populated areas: kommunale mains universal
- Alpine Maiensässe / Berghütten: Hauskläranlage / Senkgrube
- **Anschlussbescheid** required at sale

---

## Cost benchmarks (CH 2026, indicative)

| Work | Cost (CHF) |
|---|---:|
| GEAK | 800–1,500 |
| Notar + Grundbuch | cantonal tariffs; Zürich 0.2 % of price (see `--tax`) |
| Handänderungssteuer | 0–3.3 % (cantonal) |
| Maklerprovision (seller-paid typically) | 2–3 % (portal guidance, same guide's FAQ says 3–5 %; negotiable) |
| **Total transaction cost (buyer)** | transfer tax (0–3.3 %, above) + notary and land-register fees + mortgage-deed fees if financed (see `--tax`) |
| Asbestsanierung (small house) | 30,000–80,000 |
| Energetische Sanierung (Klasse C → A) | 80,000–200,000 |
| Erdbebenverstärkung | 50,000–150,000 |
| Lawinenschutz alpine | varies massively |
| Permafrost foundation upgrade | 100,000–300,000 |
| Roof in Alpine zone (slate) | 30,000–80,000 |

## Active fiscal incentives (2025-2026)

- **Gebäudeprogramm** (federal energy retrofit subsidies)
- **Förderprogramm Klima- und Energiefonds** per canton — varies massively
- **Steuerabzug Energetische Sanierung**: deductible from cantonal income tax
- **Wärmepumpe Förderung** per canton
- **Mietkredit** in some cantons for eligible buyers

## Common listing platforms

- **Homegate** — biggest, full extraction
- **ImmoScout24.ch** — premium + standard
- **Comparis** — aggregator across platforms
- **Newhome** — agency-driven
- **Acheter-Louer.ch** — French-speaking CH
- **Immobilien Tessin / Immobiliare.ch** — Italian-speaking

## Caveats unique to CH

- **Lex Koller restricts foreign buyers** of residential second homes — major issue for non-CH/EU residents
- **Zweitwohnungsinitiative 20 % cap** in many alpine + tourist Gemeinden
- **Eigenmietwert ABOLITION** (1 January 2029, fixed 1 Apr 2026 — see L87) changes ROI math for owner-occupiers
- **Stockwerkeigentum** since 1965 — most apartments; verify Wertquote + Reglement
- **Bauernhof + Bäuerliches Bodenrecht** (BGBB): special restrictions on agricultural property
- **Permafrost-Risiko** for high-alpine builds
- **MuKEn 2020/2025** drives thermal renovation mandates
- **Cantonal patchwork**: 26 different tax + planning systems
- **Federal popular vote** can change rules quickly (Eigenmietwert 2025 example)
- **Erbrecht** different per canton + family law
- **CHF currency** strong but volatile vs EUR; affects foreign-buyer purchasing power
- **No EU but EEA-adjacent** — bilateral agreements complex

## Reddit / forum sources

- **r/Switzerland**, **r/Zurich**, **r/Geneva**, **r/SwissPersonalFinance**
- **20 Minuten forum**, **Cash.ch**
- Expat: **The Local Switzerland**, **English Forum Switzerland**
- **Comparis Tipps + Tricks** community

## Verification authorities

| Authority | When to call |
|---|---|
| **Cantonal Grundbuchamt** | Title verification, encumbrances |
| **Gemeinde Bauamt** | Permits, Zonenplan, Bauakt history |
| **Steueramt (kantonal + Gemeinde)** | Liegenschaftssteuer, Eigenmietwert (until abolition — 1 Jan 2029, fixed 1 Apr 2026) |
| **Notar (Notariat) per canton** | Final transfer, Grundbuch eintragung |
| **Wasserwerk Gemeinde** | Mains drains verification |
| **Schweizerischer Erdbebendienst (SED)** | Seismic info |
| **SLF** | Avalanche zones |
| **Cantonal Naturgefahrenfachstelle** | Hazard verification |
| **STWE-Verwaltung (condo)** | Hausgeld, Erneuerungsfonds, Beschlüsse |

## Quirks to know

- **Wertquote in Stockwerkeigentum** allocates Erneuerungsfonds + voting rights
- **Grundbuchauszug Hauptregister + Stammgrundbuch + Tagebuch** — different parts
- **Servitut** (easements) common; Wegrecht, Wohnrecht, Niessbrauch
- **Vorkaufsrecht** (preemption) sometimes attached
- **Nutzniessung** (usufruct) often in inheritance situations
- **NABEG** (Nutzungsbeschränkungen) cantonal restrictions
- **Notar role**: in CH, notar handles Grundbuch directly (no separate solicitor)
- **Bauernhöfe** require agricultural-residence proof (BGBB)
- **Almhütten + Maiensässe** usually with Bauernrecht

## Source URL templates

| Source | URL pattern |
|---|---|
| Comparis | `https://en.comparis.ch/immobilien` |
| Homegate | `https://www.homegate.ch/` |
| ImmoScout24.ch | `https://www.immoscout24.ch/` |
| swisstopo | `https://www.swisstopo.admin.ch/` |
| Naturgefahren.ch | `https://www.naturgefahren.ch/` |
| swisseo Earthquake | `https://www.seismo.ethz.ch/` |
| SLF Avalanche | `https://www.slf.ch/` |
| BFS Wohnungsdaten | `https://www.bfs.admin.ch/` |
| Wüest Partner | `https://www.wuestpartner.com/` |
| Gebäudeprogramm | `https://www.dasgebaeudeprogramm.ch/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-08-05 (Lex Koller BewG consultation re-verified — closed 15 Jul 2026, submissions published 27 Jul, not enacted; balance of 2026-07-03 Tier-A refresh unchanged). SNB 24 Sep 2026 policy-rate hold re-verified 2026-09-24 in the October regwatch wave. Rental / foreign-buyer tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Finance / foreign-buyer / rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early — 13th-AHV VAT vote confirmed as fixed for 29 Nov 2026; Lex Koller consultation status, motion 24.3961 (with RK-S) and SNB hold re-checked; see shared/regulatory-watch.md). Transparency Act (TJPG) and revised GwG entry into force 1 Oct 2026 verified 2026-10-21 against admin.ch, bj.admin.ch and Fedlex SR 955.3; Art. 40 TJPG land-register precondition for foreign-law legal entities added under Lex Koller (see shared/regulatory-watch.md). MwSt re-checked 2026-10-28: 13th-AHV VAT vote (29 Nov 2026) confirmed against the Federal Council's Erläuterungen; 3.8 % accommodation-rate expiry (end-2027) and its extension to 2031 (BBl 2026 2723, referendum deadline 21 Jan 2027) added (see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (post-2025 Eigenmietwert vote definitive; SLF + Naturgefahren well-maintained). MEDIUM for short-let regulation (Lex Koller stable but cantonal patente updates ongoing); HIGH for the 2029 Eigenmietwert implementation roadmap (fixed 1 Apr 2026).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-11-25 | 2026-11-25 maintenance run | Market direction now follows the BFS residential property price index for Q3 2026 (release of 27 Oct 2026: +1.7 % on the quarter, +4.4 % on the year, 129.8 points). The SNB policy rate of 0 % (cut on 19 Jun 2025, held on 18 Jun and 24 Sep 2026) was re-checked against the SNB press releases. |
| `--risks` | 2026-11-25 | 2026-11-25 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--mains` | 2026-11-25 | 2026-11-25 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |

## Extension TODOs

- [ ] Per-canton Liegenschaftssteuer + Vermögenssteuer rate tables
- [ ] Lex Koller cantonal quotas + foreign-buyer eligibility per residence status
- [ ] Zweitwohnungsinitiative quota per Gemeinde (alpine focus)
- [ ] Per-canton Handänderungssteuer + notar fee structures
- [ ] Eigenmietwert 2029 implementation tracking (each canton's adaptation)
- [ ] Cantonal second-home property tax adoption tracking
- [ ] STWE Reglement + Erneuerungsfonds health check heuristics

## Update history

- **2026-11-25** — Maintenance run: closed `--price`, `--risks`, `--mains`; still open `--tax`, `--rental`, `--work=<profession>`, Cost benchmarks (CH 2026, indicative).
