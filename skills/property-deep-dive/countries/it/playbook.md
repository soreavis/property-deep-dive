# Italy 🇮🇹 — Property Due-Diligence Playbook

ISO2: `it`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CAP)**: 5 digits
- **Admin levels**: 20 regioni → 100+ province → 7,900+ comuni → frazioni
- **Currency**: EUR (€)
- **Languages**: Italian + DE (Bolzano), FR (Aosta), SL (FVG), AL (Calabria/Sicilia)
- **Cadastre**: Catasto Nazionale (Agenzia delle Entrate) — visura catastale **FREE since 1 Jan 2025** via SPID/CIE
- **Identifier**: codice catastale comune (4-char alphanumeric, e.g., `H501` for Roma) — different from CAP
- **Massive North/South divide**: prices, services, risks, build quality vary enormously

## Section: `--price`

### Primary sources

- **OMI (Osservatorio del Mercato Immobiliare)** — Agenzia delle Entrate official quotations:
  - Search portal: `https://www1.agenziaentrate.gov.it/servizi/Consultazione/ricerca.htm`
  - Updated semestrally (1° / 2° semestre)
  - Search by: semester + provincia + comune + zona OMI + destinazione d'uso (residenziale, commerciale, etc.)
  - Returns €/m² min-max per zona for each property type
  - Direct dataset: `https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/omi/banche-dati`

- **Visura catastale online** (FREE since 2025) — for actual rendita catastale:
  - `https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/visura-catastale/visura-catastale-online`
  - Access: SPID, CIE, or CNS required
  - Returns: rendita catastale (€/yr base), categoria (A/1-A/11 residential), classe, vani, superficie

- **Sister platform** (paid, for professionals): `https://sister.agenziaentrate.gov.it`

### Listing platforms

- **Immobiliare.it** — largest, full coverage: `https://www.immobiliare.it/<vendita-case>/<provincia>/<comune>/`
- **Idealista.it**: `https://www.idealista.it/<comune>/`
- **Casa.it**: `https://www.casa.it/<comune>/`
- **Subito.it Immobili**: classifieds, smaller listings
- **Tecnocasa, Gabetti** quarterly market reports (PDF)
- **Borsino Immobiliare** valuations

### Compute

1. Listing €/m² = listing price / superficie commerciale (note: commerciale = lordo + balconi × coefficient, may differ from Carrez-equivalent)
2. OMI €/m² gives the official band for the zone — compare
3. Valore catastale = rendita catastale × 1.05 × 160 (residential coefficient) — used for tax calculations
4. **Trap**: superficie commerciale ≠ superficie utile ≠ rendita catastale "vani" — clarify which the listing uses

### Market context

- North (Milano, Bologna, Firenze, Torino): high €/m², high liquidity
- Centro (Roma, Pisa, Perugia): mixed
- Sud (Napoli, Palermo, Bari, Cagliari): lower €/m², lower liquidity
- **Borghi a 1 euro** schemes — run comune by comune, with no national register or standard terms: the comune's own bando sets the renovation deadline and any guarantee deposit or polizza fideiussoria (data not publicly available nationally — verify in the comune's bando on its albo pretorio)
- **Centro storico** premium — but heavy Soprintendenza restrictions on any work

---

## Section: `--traffic`

### Primary sources

- **ANAS Osservatorio del Traffico**: `https://www.stradeanas.it/it/osservatorio-del-traffico`
  - Covers strade statali (SS) + autostrade (A) of national interest
  - System: PANAMA (~1,200 sezioni di conteggio, ~1,450 impianti)
  - Reports: monthly, quarterly, annual TGM
- **MIT Open Data**: `https://dati.mit.gov.it/catalog/dataset/traffico-giornaliero-medio-anas`
  - Downloadable CSV/JSON for all ANAS-managed roads
- **Regional/Provincial roads**: each Regione has its own count (often less granular):
  - Piemonte: regione.piemonte.it
  - Lombardia: regione.lombardia.it
  - Toscana: regione.toscana.it
  - etc.
- **Highway operators** (Autostrade per l'Italia, ASPI): `https://www.autostrade.it` — for A-roads

### Compute

- TGM = Traffico Giornaliero Medio Annuo
- Coarse band from OSM `highway` if no count point nearby
- Heavy vehicles % via ANAS report

### Verdict bands (urban / rural Italy)

- 🟢 < 500 v/d (rural strada comunale)
- 🟡 500–2,000 v/d (small SP / SR)
- 🟠 2,000–10,000 v/d (busy SP / urban arterial)
- 🔴 > 10,000 v/d (SS, autostrada, urban core)

---

## Section: `--tax`

### Annual property taxes

**IMU (Imposta Municipale Unica)** — most important:
- **Abitazione principale** (residenza anagrafica + dimora abituale, L. 160/2019 art. 1 c. 740-741 lett. b): exempt, EXCEPT units in the luxury categories A/1, A/8, A/9, which stay taxable. The exemption follows abitazione-principale use, not 'prima casa' purchase status — a holiday home that is not the owner's abitazione principale pays IMU (source Gazzetta Ufficiale L. 160/2019)
- **Seconda casa**: aliquota base 8.6‰ (0.86%); il comune può azzerarla o aumentarla fino a 10.6‰ (1.06%), e fino a 11.4‰ nei soli comuni con ex-maggiorazione TASI (L. 160/2019 art. 1 c. 754-755). Verify the current rate on the comune's IMU page (2026-07-03 verified, source Gazzetta Ufficiale L. 160/2019)
- **Calcolo**: `IMU = rendita catastale × 1.05 × 160 × aliquota`
- Bills: 16 giugno (acconto) + 16 dicembre (saldo), or full payment by giugno
- Canone concordato (L. 431/1998): IMU ridotta al 75 % — the owner pays 75 % of the IMU computed at the comune's rate (L. 160/2019 art. 1 c. 760; 2026-11-25 verified, source [Dipartimento delle Finanze — IMU agevolazioni](https://www.finanze.gov.it/it/fiscalita/fiscalita-regionale-e-locale/Imposta-municipale-propria-IMU/disciplina-del-tributo/agevolazioni))
- Affitto: comune può abbassare al 4‰

**TASI**: merged into IMU since 2020 (no separate bill)

**TARI (rifiuti)**: communal, set by each comune on surface + household size. For a 3-person household in a 100 m² owned home the bill ran from €196 (Cremona) to €602 (Catania) across the provincial capitals, national average €340 (2025 data, source [Cittadinanzattiva — Osservatorio Prezzi & Tariffe](https://www.cittadinanzattiva.it/comunicati/17448-presentato-il-rapporto-2025-di-cittadinanzattiva-sui-rifiuti.html), secondary — the comune's TARI page has the actual tariff)

### Transaction taxes (one-time at purchase)

For **existing residential** (used homes):

| Buyer status | Imposta di registro | Ipotecaria | Catastale |
|---|---:|---:|---:|
| Prima casa | **2 %** of valore catastale (min €1,000) | €50 fixed | €50 fixed |
| Seconda casa / non resident | **9 %** of valore catastale | €50 fixed | €50 fixed |

For **new builds (vendita da impresa)**:
- IVA 4 % (prima casa) or 10 % (standard) or 22 % (lusso)
- Imposta di registro €200, ipotecaria €200, catastale €200

**Notaio fees**: est. 1.5–2.5 % of price — unsourced skill heuristic, no binding tariff: DL 1/2012 art. 9 abolished the tariffs of the regulated professions (ministerial parameters apply only when a judge settles the fee), so the fee is agreed and the notaio must give a written preventivo di massima listing every cost item in advance — use that figure (2026-11-25 verified, source [DL 1/2012 art. 9](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-01-24;1~art9))

**Total transaction cost**: no official figure — build it per deal. Taxes, computed on Agenzia delle Entrate's own example (rendita €900, price €200,000, prezzo-valore rule): prima casa registro 900 × 1.05 × 110 × 2 % = €2,079, then €2,079 + €50 + €50 = €2,179 with ipotecaria and catastale, and €2,179 ÷ €200,000 ≈ 1.1 % of price; seconda casa registro 900 × 1.05 × 120 × 9 % = €10,206, then €10,206 + €50 + €50 = €10,306, and €10,306 ÷ €200,000 ≈ 5.2 % of price. Add the notaio (above) and any agency fee (unregulated, set in the mandate) — data not publicly available, take both from written quotes (2026-11-25 verified, source [AdE — L'acquisto della casa, June 2024](https://www.agenziaentrate.gov.it/portale/documents/20143/3949367/Guida_acquisto__Casa_imposte_e_agevolazioni_5062024.pdf/2a30330e-bc04-b486-ba96-c870c60ac66f))

### Future risk

- **Riforma del catasto** (cadastral reform) on the political table for years; no revaluation enacted as of 2026-10-21. The DPB 2027 (CdM 13 Oct 2026) is programmatic only: unregistered-building mapping at 96% of the national territory, ~20,000 compliance letters planned in 2026 and ~21,600 invitations to publicly-funded renovated buildings 'in vista dell'aggiornamento dei valori catastali nel 2028' (2026 data, source [DPB 2027, RGS/MEF](https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Contabilit_e_finanza_pubblica/DPB/2027/DPB-2027.pdf)). Size of the gap, est.: market value ≈ 1.89× the IMU taxable value for main homes and ≈ 1.95× for other homes nationally, range 1.40 (Molise) to 3.31 (Trentino-Alto Adige) (tax-year 2020 data, source 'Gli immobili in Italia 2023', MEF Dipartimento Finanze / Agenzia delle Entrate — figures may have changed since). A market-aligned revaluation would raise IMU + transaction-tax bases; the actual uplift depends on a reform text that does not yet exist (see shared/regulatory-watch.md)
- **Imposta patrimoniale** periodically debated nationally; not yet enacted

---

## Section: `--rental`

### Short-term rentals (locazioni turistiche / affitti brevi ≤30 giorni)

**Mandatory: CIN (Codice Identificativo Nazionale) since 1 Jan 2025** (2026-08-07 verified, sources [Ministero del Turismo — Avviso di entrata in funzione della BDSR](https://www.ministeroturismo.gov.it/cin-pubblicato-lavviso-di-entrata-in-funzione-della-banca-dati-strutture-ricettive-e-del-portale-telematico-per-lassegnazione-del-codice); Ministero del Turismo BDSR FAQ, updated 11 May 2026):
- **Legal basis**: art. 13-ter DL 145/2023 conv. L. 191/2023 — became applicable 2 Nov 2024, the 60th day after the Avviso attesting entry into function of the BDSR and its telematic portal was published in Gazzetta Ufficiale (3 Sep 2024); the portal had already opened earlier region-by-region in a sanction-free pilot phase. Obligation to hold a CIN in force from 1 Jan 2025 (Ministero del Turismo notice 22 Oct 2024, cited in the BDSR FAQ; 2026-11-25 verified, sources [Ministero del Turismo](https://www.ministeroturismo.gov.it/cin-pubblicato-lavviso-di-entrata-in-funzione-della-banca-dati-strutture-ricettive-e-del-portale-telematico-per-lassegnazione-del-codice) + [BDSR FAQ](https://www.ministeroturismo.gov.it/faq-banca-dati-strutture-ricettive-bdsr/) + [DL 145/2023 art. 13-ter c. 15](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2023-12-18;145~art13ter))
- Does NOT replace regional/provincial codes (CIR etc.): where a regional or provincial code is required, both codes must be obtained and displayed (Ministero del Turismo BDSR FAQ 1.3, updated 11 May 2026; 2026-11-25 verified, source [Ministero del Turismo — FAQ BDSR](https://www.ministeroturismo.gov.it/faq-banca-dati-strutture-ricettive-bdsr/))
- Apply at: `https://bdsr.ministeroturismo.gov.it/` (BDSR — Banca Dati Strutture Ricettive)
- Login via SPID or CIE
- Required for: ALL short-term rentals, B&B, casa vacanze, locazione turistica
- Without CIN: cannot list on Airbnb / Booking / Vrbo (platforms must verify)
- **Sanctions applicable from 2 Jan 2025**: €800–€8,000 for absence of CIN; €500–€5,000 for non-display or non-indication of the code — per structure or unit — plus immediate removal of the irregular listing (DL 145/2023 art. 13-ter c. 9; 2026-11-25 verified, source [Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2023-12-18;145~art13ter))
- Does NOT replace or abolish regional licensing / codes (some regioni still need additional notice to comune)
- Free; alphanumeric code

**Tax regime — Cedolare secca (sostitutiva)** (2026-11-25 verified, sources [L. 199/2025 (Legge di Bilancio 2026) art. 1 c. 17](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199) modifying L. 178/2020 art. 1 c. 595; rate scheme set by L. 213/2023 art. 1 c. 63; underlying regime DL 50/2017 art. 4 commi 2-3; [Agenzia Entrate Locazioni Brevi e Cedolare Secca](https://www.agenziaentrate.gov.it/portale/le-locazioni-brevi-e-la-cedolare-secca)):
- **1° immobile**: 21 % flat (cedolare ridotta) on the income of the one unit the taxpayer names in the tax return — also available when a second unit is let short-term at 26 % (L. 213/2023 art. 1 c. 63, per Agenzia delle Entrate); platforms and intermediaries always withhold 21 % as an advance (acconto), whatever regime the owner chooses (AdE circolare 10/E of 10 May 2024)
- **2° immobile**: 26 % flat (cedolare ordinaria)
- **Soglia dal 1 gen 2026**: max 2 immobili in cedolare secca per contribuente per periodo d'imposta (era 4 fino al 2025; ridotto da L. 199/2025 art. 1 c. 17). Il ≤2-cap e la presunzione di impresa ≥3 sono la **stessa soglia espressa in due modi**, non due limiti distinti
- **3°+ immobile**: presunzione di legge di attività imprenditoriale (L. 178/2020 art. 1 c. 595 as amended by L. 199/2025 art. 1 c. 17) → P.IVA obbligatoria, SCIA al SUAP del comune (DL 145/2023 art. 13-ter c. 8), tassazione come reddito d'impresa (non IRPEF ordinaria sul reddito da locazione), perdita del regime cedolare (2026-11-25 verified, sources [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/le-locazioni-brevi-e-la-cedolare-secca) + [DL 145/2023 art. 13-ter](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2023-12-18;145~art13ter))
- **Nessun rinvio**: la proroga di sei mesi al 1 lug 2026, circolata come emendamento al Milleproroghe, NON è stata approvata — il testo coordinato del DL 200/2025 conv. L. 26/2026 (GU 28 feb 2026) non contiene alcuna disposizione sulle locazioni brevi; la soglia dei 2 immobili si applica dal 1 gen 2026 (2026-08-07 verified, sources Agenzia delle Entrate + Gazzetta Ufficiale)
- Only for contracts ≤ 30 days
- Optional alternative: regime ordinario IRPEF on rental income

**Other obligations**:
- **Tassa di soggiorno**: collected from guests, set per comune — e.g. Milan 2026 €9.50/n per person for locazioni brevi / B&B (2026 data, source Confcommercio Milano, secondary — verify at the comune's imposta di soggiorno page)
- **Comunicazione alle autorità di PS** — ogni guest registered via Alloggiati Web (Polizia)
- **Ricevuta** issued to guest: €2 imposta di bollo when the amount exceeds €77.47 (DPR 642/1972 Tariffa parte I art. 13; 2026-11-25 verified, sources [AdE Risposta 491/2021](https://www.agenziaentrate.gov.it/portale/documents/20143/0/Risposta_491_20.07.2021.pdf/c0a023c7-7c30-1e11-8cf8-16460212d92a) + [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/aspetti-generali))

### Long-term residential

- **Cedolare secca canone libero**: 21 %
- **Cedolare secca canone concordato**: 10 % — in comuni con carenze di disponibilità abitative (DL 551/1988 art. 1 c. 1 lett. a-b) and comuni ad alta tensione abitativa individuati dal CIPE (2026-11-25 verified, source [Agenzia delle Entrate cedolare secca scheda](https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/cedolare-secca/scheda-informativa-cedolare-secca)). Watch: budget bill A.C. 3174-bis art. 5 (tabled 30 Oct 2026, in V Commissione since 12 Nov 2026) would cut this rate to 5 % for leases signed in 2027, on rents due 2027-2031, and to 1 % if the tenant is under 36 at signing — bill, not law; 10 % applies until the budget law is enacted (2026-11-25 verified, source [Camera — A.C. 3174-bis](https://www.camera.it/leg19/126?leg=19&idDocumento=3174-bis); see shared/regulatory-watch.md)
- **Regime ordinario IRPEF**: marginal rate

### Strategic notes

- North + tourist hotspots (lakes, Cinque Terre, Toscana, Amalfi, Dolomiti): highest yields
- South (Sicilia, Puglia coast, Sardegna): high seasonality (4-month season concentration)
- **Firenze centro storico STR ban IN FORCE** — regolamento (Del. C.C. 27/2025, in force 31 May 2025; underlying Variante al Piano Operativo Del. C.C. 19 & 20/2025) bans NEW short-term rentals in the UNESCO Nucleo Storico (Zona A): units legally let for tourism in 2024 may continue only under the Tuscan Testo Unico transitional derogation expiring 31 May 2028; adds 5-yr authorisations (lapsing after 12 months' inactivity unless let on contracts over 30 days), 28 sqm minimum apartment size, €1,000–€10,000 sanctions (2025 regolamento, source Comune di Firenze); authorisations are tied to both owner and unit and lapse on sale (Comune di Firenze press release 5 May 2025); the keybox/keypad ban sits in the Regolamento di Polizia Urbana (amended Feb 2025) and was upheld by the TAR on 14 May 2026 (Comune di Firenze press release 14 May 2026). UPHELD, not overturned: Corte Cost. sent. 186/2025 (16 Dec 2025) validated the framework, then TAR Toscana 14 May 2026 dismissed the appeals (18 per the Comune di Firenze press release, 19 per press reports; sent. 916 & 925/2026); TAR Toscana sent. 1028/2026 (May 2026) upheld the Ex Bufalini owner's appeal (~150 flats, via Bufalini / piazza Brunelleschi) for lack of coordination between the Variante's transitional saving clause and the regolamento, and the Comune has appealed to the Consiglio di Stato (per la Repubblica Firenze 6 Oct 2026, news-only); TAR Toscana Sez. I sent. 1752/2026 (9 Sep 2026) again rejected the challenge to the Variante but held a use 'insediato' from the formation of its building title (e.g. SCIA edilizia), so a title formed before the Variante's adoption escapes the ban (one SUAP refusal annulled). EXTENDED to A3/A4 subzones (Campo di Marte, San Jacopino, Gavinana, Statuto-Rifredi, Libertà, Bronzino and other first-ring districts — 67,780 homes / 11.21 km², 2026 data, source Comune di Firenze) by Del. C.C. 28 del 4 Jun 2026, in force 21 Jun 2026 (2026-07-02 verified, sources [Comune di Firenze](https://www.comune.firenze.it/novita/area-stampa/comunicati-stampa/modifica-al-regolamento-affitti-turistici-brevi-il-consiglio); [DirittoPA](https://www.dirittopa.it/it/interventi/urbanistica/affitti-turistici-e-poteri-di-regolazione-comunale))
- Venezia caps tightening
- **Venezia — Contributo di Accesso NOT applied until 26 Mar 2027**: the €5 day-tripper access fee (€10 if paid in the 3 days before the access day) applied to the **Città antica only** — minor lagoon islands excluded. Exempt: overnight guests in imposta-di-soggiorno accommodation, Venezia/Veneto residents, under-14s, and workers incl. commuters and students. The 2026 run was 60 non-consecutive days, 3 Apr–26 Jul (Fri–Sun plus the 24–30 Apr and 1–7 Jun blocks), under the new regolamento approved by Del. C.C. 190/2025. That sperimentazione **TERMINATED** — the contributo has **NOT been applied since 27 Jul 2026**, with no payment and no exemption request needed. It **returns in 2027** on 72 days, computed 4 + 17 + 15 + 15 + 14 + 7 = 72 (March to August), from 26 Mar to 15 Aug 2027, 08:30–16:30; the 2027 arrangements (modalità) are to be announced by 31 Dec 2026 (2026-11-25 verified, sources [Comune di Venezia — Contributo di Accesso](https://cda.ve.it/it/) + [2027 calendar](https://www.comune.venezia.it/it/content/contributo-accesso-cda))
- **Pool / view / parcheggio** = top revenue levers
- **CIR/CIN registration** is the gating step — start there

---

## Section: `--work=<profession>`

### Job platforms

- **InfoJobs.it**, **Indeed.it**, **Subito.it Lavoro**
- **LinkedIn IT** (very active in North + cadres)
- **Monster.it**, **Helpwiz**
- Profession-specific bodies (ordini): albo for lawyers, doctors, architects, engineers, journalists, etc.

### Self-employment

**Partita IVA**:
- **Regime forfettario**: 15 % flat (5 % first 5 yrs, for qualifying new activities) up to €85,000/yr revenue (2026-11-25 verified, source [Agenzia delle Entrate — regime forfetario](https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-))
- **Regime ordinario**: marginal IRPEF + INPS gestione separata
- Profession-specific casse (architects, ingegneri, avvocati, etc.)

### Healthcare / regulated professions

- Doctolib (medici, fisioterapisti)
- iscrizione albo + insurance mandatory

### Catchment

- Italy is more concentrated than France — most provinces have a clear capital with most services
- Within 30 min of a provincia capital = decent catchment
- Sub 1,000-pop comuni in Sud / Appennino are very thin markets

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **IdroGEO (ISPRA)** — hydrogeological dissesto | `https://idrogeo.isprambiente.it/app/` | Address-level rischio frane + alluvioni P1/P2/P3/P4 |
| **IdroGEO Hazard & Risk** | `https://idrogeo.isprambiente.it/app/pir` | Aggregated risk indicators |
| **ISPRA flood maps (PGRA)** | `https://www.isprambiente.gov.it/pre_meteo/idro/Mappe_peric.html` | River basin flood hazard maps |
| **INGV MPS04 sismicità** | `http://esse1-gis.mi.ingv.it/` | PGA per cell at 0.05° resolution |
| **INGV zone sismiche** | `http://zonesismiche.mi.ingv.it/` | Zona 1/2/3/4 per comune |
| **Istat Mappa dei rischi** | `https://www.istat.it/.../mappa-dei-rischi-dei-comuni-italiani/` | Aggregated risk dashboard per comune |
| **Protezione Civile rischio vulcanico** | `https://www.protezionecivile.gov.it` | Vulcanic risk Vesuvio/Etna/Stromboli/Campi Flegrei |
| **ARPA regionali** | varies (see below) | Air quality, water, waste, soil pollution |
| **SNPA** (national env. system) | `https://www.snpambiente.it/` | Aggregator of all 21 ARPAs |

### ARPA regional portals (verify pollution / contaminated sites)

| Regione | Portal |
|---|---|
| Lombardia | `https://www.arpalombardia.it` |
| Veneto | `https://www.arpa.veneto.it` |
| Emilia-Romagna | `https://www.arpae.it` |
| Toscana | `https://www.arpat.toscana.it` |
| Lazio | `https://www.arpalazio.it` |
| Sicilia | `https://www.arpa.sicilia.it` |
| Piemonte | `https://www.arpa.piemonte.it` |
| Sardegna | `https://www.arpa.sardegna.it` |
| Campania | `https://www.arpacampania.it` |
| (and 12 others — all linked via SNPA) | |

### Seismic zoning (CRUCIAL for Italy)

INGV MPS04 classifies every comune into:
- **Zona 1** — high (PGA > 0.25g) — most of Calabria, Sicilia centro-orientale, Friuli, Marche/Umbria interno, Abruzzo, central Appennini
- **Zona 2** — medium-high — most of Centre + South Italy
- **Zona 3** — medium — Po valley, Sardegna nord, parts of North
- **Zona 4** — low (only Sardegna and parts of Veneto, FVG, Liguria)

**Build-era hazards** depend on zone × age:
- **Pre-1974**: pre-seismic standards. **DANGEROUS** in zone 1/2.
- **1974–1996**: incremental improvements (Legge 64/1974, DM 03/03/1975)
- **1996–2003**: OPCM 3274/2003 transition
- **Post-2008**: NTC 2008 (proper modern seismic)
- **Post-2018**: NTC 2018 (current standard)

L'Aquila (2009), Amatrice/Norcia (2016) are the recent reminders.

### Other build-era hazards

- **Amianto (asbestos)**: pre-1992 builds very likely (eternit, copertura, tubazioni). Smaltimento mandatory if friabile. Cost: est. €15–€60/m² removal (verify with licensed smaltimento operator quote; cf. roof-removal benchmark below).
- **Aluminosis** (Italian variant): rare, but check 1960s–70s edilizia popolare
- **Vespasiano / Roma 1950s-70s**: scarce concrete, possible.

### Mandatory diagnostics at sale (NULLITY-RISK level)

| Document | Required because | Risk if missing |
|---|---|---|
| **APE (Attestato Prestazione Energetica)** | All sales (announcement must show class) | Sale cannot complete |
| **Conformità urbanistica** | Deed must state the building's titoli abilitativi: permesso di costruire or sanatoria if building began after 17 March 1985 (art. 46 DPR 380/2001); licenza, concessione or concessione in sanatoria for earlier builds, or a substitute declaration (dichiarazione sostitutiva di atto notorio) for works begun before 1 September 1967 (art. 40 L. 47/1985) (2026 data, source Normattiva) | **NULLITÀ DELL'ATTO** |
| **Conformità catastale** | DL 78/2010, all sales | **NULLITÀ** |
| **Certificato impianti** (elettrico, idrico, termico) | DM 37/2008, all installations after 1990 | Sale possible but acquirente liability |
| **Libretto impianto termico** | All boilers + AC | Mandatory transfer |
| **Visura catastale aggiornata** | All sales | Identifies any difformità |
| **Visura ipotecaria** | Mortgage / liens check | Sale risk |

### Abuso edilizio risk (Italy-specific, CRITICAL)

- Italy has chronic illegal-building issues, particularly in Sud + coastal
- Three condono windows expired (1985, 1994, 2003)
- Today: only **sanatoria ordinaria** with **doppia conformità** (current rules + rules at time of build)
- **If unresolved abuso**: atto può essere null; acquirente eredita l'obbligo di demolizione
- Pre-rogito: technician must verify conformità urbanistica vs catastale vs stato di fatto
- Common abusi: verandas, soppalchi, frazionamenti, cambi destinazione d'uso

**Always commission a tecnico (geometra/architetto)** for pre-rogito conformità check on any property >20 yrs old. Cost: est. €300–€2,000 (calibration: a trade guide puts a relazione tecnica at a few hundred euros for a simple property and over €1,000 when the records are complex ([Edilizia.com, 2026](https://www.edilizia.com/leggi-normative/relazione-tecnica-di-compravendita-cose-quando-e-obbligatoria-quanto-costa)); a Tuscan practice quotes €800–€2,000 for a flat ([Studio Madera, 2026](https://www.studiomadera.it/relazione-tecnica-notarile)); commercial estimates, so get a written quote).

### Climate change projections (CMCC / ISPRA)

- Drought intensifying esp. Po basin + Sardegna + Sicilia
- Sea-level rise: Venezia, Adriatico nord, Mar Tirreno coasts
- Glacial retreat: Alpi (impact on alpine real estate)
- Wildfires up: Sicilia, Sardegna, Calabria, Basilicata
- Mediterranean storms increasing

---

## Section: `--mains`

### Primary sources

- **ARERA ATID (Anagrafica Territoriale Servizio Idrico Integrato)**: `https://www.arera.it/area-operatori/atidrhtm`
  - Definitive list of which gestore covers which comune
  - ~2,399 gestori in IT (1,997 enti locali + 394 aziende + 8 multiutility quotate) — verify current count at arera.it (ATID portal above)
- **Comune** + **gestore idrico locale** (acquedotto + fognatura + depurazione typically same operator)

### Major water operators (regional/multiutility)

| Operator | Coverage |
|---|---|
| **Acea** | Roma + Lazio |
| **Iren** | Liguria, Piemonte, Emilia |
| **A2A / SAL** | Lombardia (Milano + Brescia areas) |
| **Hera** | Emilia-Romagna |
| **Smat** | Torino metropolitana |
| **Acqualatina** | Lazio sud |
| **Mediterranea delle Acque** | Genova |
| **Publiacqua** | Toscana centro |
| **GAIA / GORI / Acquedotto Lucano** | regional Sud |

### Verification

- Most centro storico + recent suburbs: mains universal
- Rural Sud + Appennino frazioni montane often on **fossa biologica / Imhoff**
- Listing keywords: "fognatura" / "scarico in pubblica fognatura" / "fossa biologica" / "vasca Imhoff" / "subirrigazione"

### Costs

| Scenario | Cost |
|---|---:|
| Connection to mains where available | est. €1,500–€4,000 (calibration: the gestori's own list prices for the public side up to a pozzetto at the boundary: Nuove Acque, Arezzo, 2026: €894.11 for the first 3 m under an asphalt road plus €113.92 per extra metre ([listino](https://nuoveacque.it/listino-allacciamenti)); Astea, Macerata, 2025: €1,000 up to 10 m plus a €70 connection right ([tariffario](https://www.asteaspa.it/wp-content/uploads/2025/01/Tariffario-prestazioni-accessorie-2025.pdf)); pipework inside the plot is extra and each gestore sets its own prices) |
| Septic to mains conversion | est. €2,000–€15,000 (calibration: the est. €1,500 low end of the connection row above plus emptying the old tank, priced in the Imhoff replacement row below; the upper end covers a long rural run at per-metre rates like Nuove Acque's €113.92 and re-routing the house drains, so get quotes) |
| New fossa biologica + filtro | est. €3,000–€8,000 for tank, dispersal or filter, project and discharge permit (calibration: the Piemonte 2026 regional price list, as cited by [Ristrutturalo, 2026](https://ristrutturalo.it/fossa-imhoff-regole-scarico-costi), prices a 5-person polyethylene Imhoff at €426.90 plus €245.97 for digging and laying, €672.87 before VAT, and a complete 5-person phytodepuration system, supplied and laid, at €5,163.23 where regional rules require one; the guide finds no list price for the dispersal trench, the project or the permit (D.Lgs. 152/2006 art. 124), so get quotes) |
| Imhoff replacement | from €1,119.95 before VAT (computed: €672.87 + €447.08 = €1,119.95, a 5-person polyethylene tank supplied and laid plus emptying the old tank, up to 8 m³ within 20 km, both on the Piemonte 2026 regional price list as cited by [Ristrutturalo, 2026](https://ristrutturalo.it/fossa-imhoff-regole-scarico-costi)); a larger tank, removing the old one, renewing the dispersal, the project and the permit are extra and often cost the most, so get quotes |

---

## Cost benchmarks (IT 2026)

| Work | Cost |
|---|---:|
| APE | est. €100–€300 (unsourced skill heuristic; no regulated fee since DL 1/2012 art. 9 — get 2–3 quotes from certified energy assessors) |
| Visura catastale online (free via SPID, CIE or CNS — D.Lgs. 139/2024 made many telematic catasto consultation services free; 2026-11-25 verified, sources [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/visura-catastale/visura-catastale-online) + [AdE Bilancio 2025](https://www.agenziaentrate.gov.it/portale/documents/20143/10180328/All.1+Bilancio_2025.pdf/13cbde69-c718-0946-3b8a-393f60474275?t=1782285298605)) | €0 |
| Notaio | est. 1.5–2.5 % of price (unsourced skill heuristic; no tariff since DL 1/2012 art. 9 — ask for the written preventivo) |
| Imposta di registro (prima casa) | 2 % of valore catastale |
| Imposta di registro (seconda casa) | 9 % of valore catastale |
| IVA new build (standard) | 10 % |
| Tecnico per conformità (geometra) | est. €300–€2,000 (see `--risks`; no tariff since DL 1/2012 art. 9 — ask for the written preventivo) |
| Septic to mains | est. €2,000–€15,000 (see `--mains`; get the gestore idrico's and a contractor's quote) |
| Roof (terracotta tiles, 200 m²) | est. €15,000–€30,000 (unsourced skill heuristic — get 2–3 contractor quotes) |
| Antiseismic retrofit (small house) | est. €30,000–€80,000 (unsourced skill heuristic — get 2–3 quotes); Sismabonus 50 % abitazione principale / 36 % other nel 2025-2026; 36 % / 30 % per spese 2027 under current law (2026-11-25 verified, source [L. 199/2025 art. 1 c. 22](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199)) |
| Asbestos removal (200 m² roof) | est. €5,000–€15,000 (unsourced skill heuristic — get 2–3 quotes from licensed removal firms) |
| Energy retrofit (Ecobonus 50 % abitazione principale / 36 % other 2025-2026; 36 % / 30 % per spese 2027 under current law — 2026-11-25 verified, source [L. 199/2025 art. 1 c. 22](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199)) | est. €20,000–€60,000 (unsourced skill heuristic — get 2–3 quotes) |
| **Total transaction cost (prima casa)** | taxes €2,179 ÷ €200,000 ≈ 1.1 % of price on AdE's example (registro €2,079 plus €50 ipotecaria and €50 catastale, computed in `--tax`); notaio + any agency fee on top — no official total, get written quotes |
| **Total transaction cost (seconda casa)** | taxes €10,306 ÷ €200,000 ≈ 5.2 % of price on AdE's example (registro €10,206 plus €50 ipotecaria and €50 catastale, computed in `--tax`); notaio + any agency fee on top — no official total, get written quotes |

## Active fiscal incentives (2026-2027)

- **Sismabonus** abitazione principale **50 %** / other units **36 %** (2025 e 2026 — decalage sospeso da [L. 199/2025 art. 1 c. 22](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199) modificante DL 63/2013 art. 16); 36 %/30 % programmato per 2027 salvo proroga; cap €96,000/unit; spread su 10 quote annuali; statute underlying: art. 16-bis TUIR (DPR 917/1986) + art. 16 c. 1-septies DL 63/2013 per acquisti (2026-05-27 verified, sources normattiva.it L. 199/2025 + DL 63/2013)
- **Ecobonus** energy retrofit (art. 14 DL 63/2013): 50 % abitazione principale / 36 % other units for spese 2025-2026; 36 % / 30 % for spese 2027 under current law (L. 199/2025 art. 1 c. 22 lett. a); stand-alone fossil-fuel boilers excluded since 2025 (2026-10-21 verified, source [Camera dei deputati — tassazione immobili](https://temi.camera.it/leg19/temi/19_tl18_tassazione_immobili.html))
- **Bonus Ristrutturazione** (art. 16-bis TUIR + art. 16 c. 1 DL 63/2013): spese 2026 **50 %** only when the unit is the abitazione principale of the owner or real-right holder, **36 %** in all other cases (second / holiday homes, tenants); spese 2027 **36 % / 30 %**; cap €96,000 per unit both years, 10 annual instalments; spese 2028-2033 30 % on €48,000; from 2034 36 % on €48,000. A foreign buyer's second home gets 36 % in 2026 and 30 % in 2027, not 50 % (2026-10-21 verified, sources [Agenzia delle Entrate — ristrutturazioni edilizie](https://www.agenziaentrate.gov.it/portale/aree-tematiche/casa/agevolazioni/agevolazioni-per-le-ristrutturazioni-edilizie) + AdE guida Feb 2026)
- **Superbonus 110 %** sostanzialmente concluso; trasceso a 65 % e poi a regime ordinario
- **Bonus Mobili** ed elettrodomestici: legato a ristrutturazione, 50 % on up to €5,000 per unit, 10 annual instalments, for purchases made **by 31 Dec 2026** linked to recupero edilizio works begun from 1 Jan of the previous year; only the taxpayer claiming the renovation deduction can use it. DL 63/2013 art. 16 c. 2 as extended by L. 199/2025 art. 1 c. 22 has no 2027 year — a 2027 purchase needs a proroga in the Legge di Bilancio 2027 (2026-10-21 verified, source [Agenzia delle Entrate — Bonus mobili ed elettrodomestici](https://www.agenziaentrate.gov.it/portale/aree-tematiche/casa/agevolazioni/bonus-mobili-ed-elettrodomestici))
- **Legge di Bilancio 2027 — bill before Parliament, NOT yet law**: CdM n. 195 (28 Oct 2026) approved the disegno di legge di bilancio 2027, tabled at the Camera on 30 Oct 2026 as A.C. 3174 (A.C. 3174-bis since 4 Nov 2026, V Commissione, first reading). Art. 4 would keep Bonus Ristrutturazione, Ecobonus and Sismabonus at 50 % (abitazione principale) / 36 % (other homes) for spese 2027, cap €96,000 per unit, and extend the Bonus Mobili (50 % on up to €5,000) to 2027 purchases; the 65 % Ecobonus on the prima casa is not in the text. Parliament can still amend it and must pass it by 31 Dec 2026. Until the law is in Gazzetta Ufficiale the 2027 rates above (36 % / 30 %, no Bonus Mobili) are the law in force (2026-11-06 verified, sources [Camera — A.C. 3174-bis](https://www.camera.it/leg19/126?leg=19&idDocumento=3174-bis) + [bill text](https://documenti.camera.it/apps/commonServices/getDocumento.ashx?sezione=lavori&tipoDoc=testo_pdl_pdf&idlegislatura=19&codice=leg.19.pdl.camera.3174-bis.19PDL0221760); see shared/regulatory-watch.md)

## Common listing platforms

- **Immobiliare.it** — largest, full extraction
- **Idealista.it** — modern, mobile-friendly
- **Casa.it** — good for Sud
- **Wikicasa, Bakeca** — secondary
- **Subito.it** — privates, attention to abusi
- **Tecnocasa, Gabetti, RE/MAX** — agency networks

## Caveats unique to IT

- **Conformità urbanistica + catastale = nullità rischio** — never sign without tecnico verification
- **Abuso edilizio** epidemic, especially Sud + coastal — pre-rogito audit is mandatory
- **Centro storico + paesaggistica vincolo**: any work requires Soprintendenza approval (3–12 month delays)
- **CIN obbligatorio dal 1 gen 2025** for any short-term rental — without it, cannot list; sanzioni dal 2 gen 2025: €800–€8,000 per assenza di CIN, €500–€5,000 per mancata esposizione o indicazione del codice (per struttura o unità), più rimozione immediata dell'annuncio irregolare
- **Cedolare secca limit 2 properties from 1 Jan 2026** (nessun rinvio: l'emendamento Milleproroghe al 1 lug 2026 non è stato approvato) — affects rental investment math
- **Nord/Sud disparity**: massive gap in services, tax, value, liquidity
- **Borghi a 1 euro** schemes: cheap entry but mandatory €20k–€50k renovation timeline + caution fund (often €5,000–€10,000)
- **Diritti reali**: usufrutto, servitù di passaggio, prelazione agraria — careful notaio review

## Reddit / forum sources

- **r/italy** (Italian-language)
- **r/AskItalia**, **r/ItalyExpat**
- **CodicePedone.it forum**, **Idealista.it news section**
- **Forum BastaBidaste** for real-estate insiders
- Expat communities: **The Local Italy**, **Italian Property Insider**, **InTuscany**

## Verification authorities

| Authority | When to call |
|---|---|
| **Comune** (Ufficio Tecnico) | Conformità urbanistica + IMU + permesso di costruire |
| **Agenzia delle Entrate** | Visura catastale + rendita + OMI |
| **Catasto comunale** | Conformità catastale |
| **Notaio** | Final compravendita + visure ipotecarie + sanity check |
| **Tecnico (geometra/architetto)** | Pre-rogito conformità audit (MANDATORY) |
| **Gestore idrico** (ARERA list) | Mains drains verification |
| **ARPA regionale** | Pollution / soil contamination |
| **Soprintendenza** | If centro storico / vincolo |

## Quirks to know

- **OMI quotations are zonal (per zona OMI within comune)** — listing might be in a different zona than the comune average; always check zone-specific OMI for accurate comparison
- **Superficie commerciale** (used in listings) ≠ superficie utile/Carrez ≠ rendita catastale "vani" — never compare €/m² across these naïvely
- **CAP can span multiple comuni** in Italy (unlike France 1 CAP = 1 comune typically); verify codice catastale comune for accurate lookup
- **Rendita catastale revaluation 1.05** dates from 1996; multiple political pushes for cadastre reform have stalled
- **Polizza Catastrofale (CatNat) obbligatoria per le imprese — in vigore per tutte le categorie tranne pesca/acquacoltura (termine prorogato al 31 dic 2026), entrata scaglionata**: grandi imprese entro 31 mar 2025, medie entro 30 set 2025, micro/piccole entro 31 dic 2025; micro/piccole turistico-ricettive e somministrazione prorogate al 31 mar 2026 (DL 200/2025 Milleproroghe, conv. L. 26/2026); pesca/acquacoltura prorogate al 31 dic 2026 (DL 25/2026 art. 9 c. 6, conv. L. 59/2026). Inadempienza = se ne tiene conto nell'assegnazione di contributi, sovvenzioni e agevolazioni pubbliche (L. 213/2023 art. 1 c. 102); il DM MIMIT 18 giu 2025 subordina all'adempimento l'accesso alle agevolazioni DGIAI elencate nel decreto. NON ancora residenziale, ma worth noting (2026-07-03 verified, source MIMIT polizze rischi catastrofali Cat Nat)

## Source URL templates

| Source | URL pattern |
|---|---|
| OMI search | `https://www1.agenziaentrate.gov.it/servizi/Consultazione/ricerca.htm` |
| Visura catastale (SPID) | `https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/visura-catastale/visura-catastale-online` |
| IdroGEO | `https://idrogeo.isprambiente.it/app/` |
| INGV MPS04 | `http://esse1-gis.mi.ingv.it/` |
| INGV zone sismiche | `http://zonesismiche.mi.ingv.it/` |
| ANAS open data | `https://dati.mit.gov.it/catalog/dataset/traffico-giornaliero-medio-anas` |
| BDSR Ministero Turismo (CIN) | `https://bdsr.ministeroturismo.gov.it/` |
| ARERA ATID | `https://www.arera.it/area-operatori/atidrhtm` |
| SNPA | `https://www.snpambiente.it/` |
| Immobiliare.it search | `https://www.immobiliare.it/vendita-case/<provincia>/<comune>/` |
| Idealista.it | `https://www.idealista.it/<comune>/` |
| Istat mappa rischi | `https://www.istat.it/statistiche-per-temi/focus/informazioni-territoriali-e-cartografiche/rappresentazioni-cartografiche-interattive/mappa-dei-rischi-dei-comuni-italiani/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-08-07 (`--rental` re-verified — CIN block against Ministero del Turismo BDSR, the cedolare secca property threshold, and the Venice Contributo di Accesso season; balance of playbook 2026-07-03 Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged). Insurance / rental tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Rental tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Fiscal-incentive, catasto, cedolare and IMU abitazione-principale exemption lines re-checked 2026-10-21 against Agenzia delle Entrate, the Dipartimento delle Finanze, the Camera dei deputati dossier and the DPB 2027 (Legge di Bilancio 2027 watch; see shared/regulatory-watch.md); the IMU seconda-casa rates keep their 2026-07-03 stamp. Legge di Bilancio 2027 lines (fiscal incentives, cedolare concordato watch) re-checked 2026-10-28 against governo.it CdM n. 195 — DDL approved, text not yet published (see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + rental sources (multi-source corroborated). MEDIUM for work catchment heuristics (region-dependent).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-11-25 | 2026-11-25 maintenance run | Borghi a 1 euro terms are set comune by comune in each bando; no national register lists them. |
| `--work=<profession>` | 2026-11-25 | 2026-11-25 maintenance run | Regime forfetario rates and the €85,000 threshold are confirmed against Agenzia delle Entrate. |
| `--risks` | 2026-11-25 | 2026-11-25 maintenance run | The deed-nullity rule now cites both laws on Normattiva: art. 46 DPR 380/2001 for builds begun after 17 March 1985 and art. 40 L. 47/1985 for earlier ones; Legge 64/1974 and the DM of 3 March 1975 were confirmed. The tecnico's fee is an estimate calibrated on 2026 trade and practice pages. |
| `--mains` | 2026-11-25 | 2026-11-25 maintenance run | Sewer and septic costs are estimates: connections are calibrated on the published tariffs of Nuove Acque (2026) and Astea (2025), tanks on the Piemonte 2026 regional price list and emptying on a commercial price list. The Imhoff replacement is now a computed floor, since a laid tank costs far less than the old figure. |
| Cost benchmarks (IT 2026) | 2026-11-25 | 2026-11-25 maintenance run | Registro and IVA rates are confirmed against Agenzia delle Entrate and the bonus rates against L. 199/2025; works and professional-fee ranges are labelled as unsourced estimates to calibrate with local quotes. |

## Extension TODOs (deepen on first real run)

- [ ] Per-regione CIN/short-let regional addenda (Veneto, Lombardia, Toscana, Lazio specifics)
- [ ] OMI zona-coding lookup for major comuni (Roma centro vs Roma periferia)
- [ ] Re-check Sismabonus / Ecobonus / Bonus Ristrutturazione / Bonus Mobili against the Legge di Bilancio 2027 text at Gazzetta Ufficiale publication (DDL tabled 30 Oct 2026 as A.C. 3174, art. 4 read 2026-11-06; tracked in shared/regulatory-watch.md)
- [ ] Sanatoria / abuso edilizio detection workflow (likely needs tecnico in person)
- [ ] Local IMU aliquota per comune (need scraping per ~7,900 comuni — start with top 100)
- [ ] Nord/Sud cost-benchmark differentiation (renovation prices differ ~30–50 %)

## Update history

- **2026-11-25** — Maintenance run: closed `--price`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (IT 2026); still open `--tax`, `--rental`.
