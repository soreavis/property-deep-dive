# France 🇫🇷 — Property Due-Diligence Playbook

ISO2: `fr`. Status: ✅ Fully populated.

## Country profile

- Postcode pattern: 5 digits (`XXXXX`)
- INSEE code: 5-digit commune identifier (different from postcode)
- Geocode commune → INSEE: use `https://geo.api.gouv.fr/communes?codePostal=<postcode>` or address-api `https://data.geopf.fr/geocodage/search?q=<query>`
- Currency: EUR (€)
- Language: French (with German/Italian/Catalan/Basque regional pockets)
- Cadastre: free public via `cadastre.gouv.fr`

## DROM overlay (overseas départements)

If the address resolves to one of the five **DROM** — postcode prefix **971 Guadeloupe (`gp`) · 972 Martinique (`mq`) · 973 Guyane (`gf`) · 974 La Réunion (`re`) · 976 Mayotte (`yt`)** — this metropolitan playbook still applies as the baseline (same *Code civil*, euro, *impots.gouv.fr*, *notaire*, cadastre framework), **but you MUST also load [`shared/fr-drom-overlay.md`](../../shared/fr-drom-overlay.md) and apply its deltas**: DROM-specific TVA rates, *octroi de mer*, *taxe foncière* abattements, majored notary *émoluments*, the Letchimy indivision regime, and per-DROM cyclone/seismic hazard profiles. The overlay lists ONLY the deltas — anything it does not override follows this playbook.

## Section: `--price`

**Data sources** (priority order — primary first):

1. **DVF Etalab — canonical actual sale prices** (DGFiP open data via Etalab):
   - Map portal: `https://app.dvf.etalab.gouv.fr/` (form-based; search by commune)
   - Bulk dataset: [data.gouv.fr DVF](https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres/) — DGFiP publishes one national pipe-separated `.txt` file per year over a rolling five years, replaced in full every April and October (latest 12 Oct 2026, covering 2021 S2 to 2026 S1, so the lag is about one semester); Etalab's derived [DVF géolocalisées](https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/) gives clean geocoded CSV, one file per year plus a five-year file. **Not covered: Alsace (67, 68), Moselle (57) and Mayotte (976)** — no DVF comps there (2026 data, source DGFiP / data.gouv.fr; checked 2026-10-28)
   - Clean passthrough UI: [immo-dvf.fr](https://www.immo-dvf.fr/) (same DVF data, easier to read; commune-level page is `/prix-immobilier/<region>/<dept>/<commune>-<postcode>/`)
2. **Aggregator estimates** (cross-check only — methodology + freshness varies):
   - [meilleursagents.com](https://www.meilleursagents.com/prix-immobilier/) — €/m² + history
   - [journaldunet.com patrimoine](https://www.journaldunet.com/patrimoine/prix-immobilier/) — JDN aggregated
   - [orpi.com prix-immobilier](https://www.orpi.com/prix-immobilier/) — Orpi network estimate
   - [immobilier.lefigaro.fr prix-immobilier](https://immobilier.lefigaro.fr/prix-immobilier/)
   - [pap.fr](https://www.pap.fr/vendeur/prix-m2/) — backup
3. **WebSearch live listings**: `"<commune>" maison à vendre prix` for current comp listings
4. **Avoid for primary data**: third-party DVF API mirrors (e.g., `api.cquest.org`, which returned HTTP 502 on 2026-10-28) — unreliable or stale; prefer Etalab + immo-dvf.fr passthrough
5. **National / province trend (primary — context only, never a commune value)**: Notaires-INSEE index of existing-home prices, Q2 2026 (provisional): −1.0 % on the quarter (seasonally adjusted) and −0.8 % on the year for France excl. Mayotte; province −1.0 % on the year (houses −1.3 %, apartments −0.3 %); 958,000 existing-home sales in the 12 months to end-June 2026 ([INSEE Informations Rapides n° 216](https://www.insee.fr/fr/statistiques/9040119), 8 Sep 2026; Q3 release due 24 Nov 2026). City-level medians (apartment €/m², house price per agglomeration) are in the Notaires de France [quarterly price maps](https://www.notaires.fr/fr/article/marche-de-limmobilier-indices-et-cartes-de-prix-au-m2-2e-trimestre-2026) (Q2 2026, *Note de conjoncture immobilière* n° 73, Oct 2026) and on the [immobilier.notaires.fr price map](https://www.immobilier.notaires.fr/fr/prix-immobilier)

**Sparse-DVF fallback**: rural communes <1,000 pop typically have <10 transactions/year — computed for Vienne (86): of 173 communes under 1,000 inhabitants, the median recorded 6 house/apartment sales in 2025 and 124 (72 %) recorded fewer than 10 (DVF géolocalisées 2025, April 2026 delivery × geo.api.gouv.fr populations; one département, so an indication only) — DVF median for the commune is statistically noisy. **Use the nearest larger market town (sub-prefecture or chef-lieu de canton) as the reference** and apply a **0.7–0.85× rural correction factor (est. — skill heuristic, not a published coefficient)** for outlying lieu-dit (depends on distance + amenities). Document the extrapolation explicitly + flag confidence MEDIUM, NOT HIGH.

**Compute**:
- Price/m² = listing FAI / surface m² (Carrez)
- Discount/premium vs commune average: `(commune_avg - listing_psqm) / commune_avg`
- Walk-away price = listing × (1 − reasonable_discount). For 1970s-1990s rural homes "à rafraîchir," reasonable_discount = 5–10 % (est. — skill heuristic, not a measured negotiation margin).

**Caveats**:
- Rural communes have thin DVF samples (5–20 sales/yr; Vienne 2025: 112 of 173 communes under 1,000 inhabitants (65 %) recorded 5–20 house/apartment sales and 58 (34 %) fewer than 5 — computed from DVF géolocalisées); flag confidence as low if <10 transactions
- The "FAI" (Frais d'Agence Inclus) price includes the agency fee (~5–6 % est., agency-specific — read the actual fee in the listing or mandate); compute against the net seller price for notary fees

---

## Section: `--traffic`

**Data sources**:
- OSM Overpass for the way's `ref`, `highway`, `maxspeed` (already in pre-flight)
- Conseil Départemental traffic count PDF — search `"département <name>" comptage routier carte trafic <year>` and download
- Examples:
  - Vienne 86: the yearly maps are listed on [lavienne86.fr — Le réseau routier départemental](https://www.lavienne86.fr/au-quotidien/routes-deplacements/le-reseau-routier-departemental); latest `A1_Trafic_2025.pdf` (about 31 MB, one A1 page, file dated 27 Apr 2026). File names are not consistent (2021, 2024 and 2025 follow `A1_Trafic_<year>.pdf`; 2022 and 2023 do not), so start from the index page (checked 2026-10-28)
  - Only the Vienne product was checked (2025: a one-page A1 PDF exported from QGIS); check each département's own roads page rather than assuming the same format or frequency

**Extraction technique**:
1. `curl -sL -o trafic.pdf <url>`
2. `pdftotext -layout trafic.pdf - | grep "^.*D<road>"` → finds TMJA values in tabular form **only where labels are real text** — on the Vienne 2025 map it returns just the legend headings (TMJA labels and count tables are drawn, not text), so go straight to step 3
3. For map labels (village names): `pdftoppm -png -r 200 trafic.pdf p` then crop to the commune location and read images
4. Color legend (Vienne 2025 map — TMJA "tous véhicules et sens confondus"; labels in bold italic underlined were measured in 2025, the others were not measured that year; check each département's own legend):
   - 🟧 orange: < 500 v/d
   - 🟦 cyan: 500–1500 v/d
   - 🟩 green: 1500–3000 v/d
   - 🟪 magenta: > 3000 v/d

**Compute**:
- TMJA on property's road (or estimated from nearest measured)
- Vehicle/hour daylight ≈ TMJA × 0.06; night ≈ TMJA × 0.01 (est. — skill heuristic; no published coefficient found in this pass)
- Heavy vehicles (PL): the Vienne 2025 count tables (postes secondaires, postes permanents) give the PL count and % PL for each station they list (road, PR, TMJA, PL, % PL); the map labels themselves are TMJA only

**Verdict bands for rural FR** (skill thresholds, not an official classification):
- 🟢 < 200 v/d
- 🟡 200–800 v/d
- 🟠 800–3000 v/d
- 🔴 > 3000 v/d

---

## Section: `--tax`

**Data sources** (priority order — canonical first):

1. **DGFiP open data — communal tax rates** (canonical, all communes):
   - DGFiP fiscal data on data.economie.gouv.fr: [data.economie.gouv.fr — taux fiscalité directe locale](https://data.economie.gouv.fr/explore/?q=taux+fiscalit%C3%A9+directe+locale)
   - Service-Public.fr lookup tool overview: [service-public.gouv.fr A18426](https://www.service-public.gouv.fr/particuliers/actualites/A18426)
   - Délibérations fiscales votées par les collectivités: [collectivites-locales.gouv.fr — Taux votés](https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/acces-par-thematique/fiscalite/taux-de-fiscalite-directe-locale-votes-par-les-collectivites)
2. **Department-level reference** (rank + average): [DGFiP — Données générales sur les taux et les montants de la fiscalité directe locale](https://www.impots.gouv.fr/donnees-generales-sur-les-taux-et-les-montants-de-la-fiscalite-directe-locale) — "Répartition régionale et départementale du taux de prélèvement depuis 2018 : TF, TH, CFE (.xls)", updated 05/05/2026; latest bulletin "En 2025, la taxe foncière progresse de 2,4 %" (DGFiP Statistiques n°46, mai 2026). Primary publisher, replacing the former IndiceVille aggregator (2026 data, source DGFiP; 2026-09-18 verified)
3. **Third-party aggregator** (use only if DGFiP open data lookup fails for the specific commune): `https://www.impots-locaux.org/impots-locaux-<commune-slug>-<postcode>/`
4. **WebSearch fallback**: `"<commune>" taxe fonciere taux <year>` + TEOM rate

**Confidence note**: department-level data (e.g., Dordogne TFPB taux de prélèvement 61.38 % in 2025 — DGFiP ratio of taxes principales + taxes annexes + frais to bases nettes, not a voted rate; 2025 data, source DGFiP xlsx updated 05/05/2026) is HIGH; commune-specific extrapolation when DGFiP open data lookup is sparse is MEDIUM. State explicitly which you're using.

**Compute**:
1. Estimate VLC (Valeur Locative Cadastrale): for rural 1970s build, tarif est. €15–25/m²/yr after current revaluations (varies by commune category 5/6/7) — unsourced heuristic: take the real base from the seller's avis de taxe foncière.
2. Annual taxe foncière = `VLC × 50% × (taux_communal + taux_interco) + TEOM_amount`
3. Annual taxe d'habitation RS = `VLC × 100% × (taux_communal + taux_syndicat)`. Surcharge (majoration) of 5–60 % on the communal share, by council vote, only in eligible communes — for 2026 the TLV-list communes (3,689 eligible, 1,666 applied it, 688 at 60 % — DGFiP, Jul 2026); from 2027 impositions the communes in CGI art. 1406 bis I B (art. 1407 ter as rewritten by LFI 2026 art. 108) — check the commune's deliberation.
4. Frais de notaire on €P (FAI minus agency fee): 7–8 % for ancien per notaires.fr — on €145,000 in a 6.32 % département the DMTO, émoluments TTC and CSI alone come to 7.71 % (computed: 6.32 % + 1.29 % + 0.10 %, inputs below), before formalités and débours
   - DMTO: **6.32 %** in 87 of the 99 rate areas of the 1 June 2026 table (5.00 % département + 1.20 % commune + ~0.12 % frais d'assiette, computed as 2.37 % × dept rate) — the +0.5 pp département-share hike (art. 116, LOI n° 2025-127) applies **only to acts signed 1 Apr 2025 – 31 Mar 2028**; for acts from 1 Apr 2028 the rate in force on 31 Jan 2025 applies. **5.81 %** (4.50 % dept share) applies in 11 départements under the 1 June 2026 table (Hautes-Alpes, Alpes-Maritimes, Ardèche, Charente, Drôme, Lozère, Oise, Hautes-Pyrénées, Saône-et-Loire, Guadeloupe, Mayotte — Mayotte moved from 3.80 % to 4.50 % on 1 June 2026) — and only Indre keeps the 3.80 % dept share (**≈5.09 %** total). Ordinary art. 1594 D votes take effect on 1 June; art. 116 hikes notified 16 Apr–30 Nov 2026 apply to acts from 1 Jan 2027 (art. 116 III as rewritten by LFI 2026 art. 121) — **always pull the current [impots.gouv.fr DMTO PDF](https://www.impots.gouv.fr/sites/default/files/media/1_metier/3_partenaire/notaires/dmto/dmto_2026-06.pdf) edition for the live rate**. **Primo-accédants** (no main-residence ownership in the prior 2 years, buying as main residence) are statutorily exempt from the +0.5 pp hike and pay the art. 1594 D rate (4.50 % in most départements → ≈5.81 %); foreign residents qualify when the first-ownership test is met on French territory (BOFiP). (2026-10-28 verified; sources [BOFiP BOI-ENR-DMTOI-10-20-20260617](https://bofip.impots.gouv.fr/bofip/3311-PGP.html/identifiant=BOI-ENR-DMTOI-10-20-20260617) + [Légifrance LF 2025 art. 116](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051169081) + impots.gouv.fr DMTO PDF + [AN question n° 5129](https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE5129)) **PTZ (prêt à taux zéro) — pending**: PLF 2027 art. 7 I.A (bill, not adopted on 2026-10-28; Assemblée vote on the first part set for 3 Nov 2026) would let a household expecting a child or caring for a child under 3 take a PTZ without the first-ownership condition, once per beneficiary and under the PTZ income conditions; PTZ finances a primary residence only — see shared/regulatory-watch.md (FR) ([AN projet de loi n° 3210](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi)).
   - Émoluments notaire: barème proportionnel (Code de commerce art. A444-91, rates applicable since 1 Jan 2021) 3.870 % to €6,500, 1.596 % to €17,000, 1.064 % to €60,000, 0.799 % above, + 20 % TVA → €1,555.80 HT / €1,866.96 TTC on €145,000 (computed; about 0.84–1.20 % HT between €100,000 and €1M)
   - Contribution de sécurité immobilière 0.10 % of the price (CGI art. 881 K; €145 on €145,000) + émoluments de formalités and débours: est. €600–1,500 in total — unsourced range, ask the notaire for the état prévisionnel
5. Future risk: **Révision des Valeurs Locatives des Locaux d'Habitation (RVLLH)** ⚠️ postponed to **2028 declarations → 2030 new values → 2031 tax impact** by **LFI 2026** (art. 106 II, LOI n° 2026-103 du 19 février 2026, rewriting the years in art. 146 LF 2020 — CGI art. 1518 A quinquies A, created by the same art. 106, concerns professional premises, not housing) — *not* PLF 2024/2025; no official taxe foncière impact figure has been published — data not publicly available, verify at DGFiP (impots.gouv.fr); the Government's Sénat written answer of 14 May 2026 gives none, and the unofficial +20–40 % rural figure is withdrawn as unsourced. Nothing rolls in 2026–2028; the Government's report to Parliament is now due **1 Sept 2029** (was 1 Sept 2026), and Sénat rapport l25-312 notes this volet would not be fully executed before **c.2040** — parliamentary commentary, not statute, but it is the realistic horizon for any buyer treating this as a live cost. Dates per [ANIL — analyse LF 2026 art. 106](https://www.anil.org/aj-loi-finances-2026/) + [Légifrance art. 106](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053508773) (2026-10-21 verified — dates; the 1 Jul 2028 declaration deadline applies to owners of let-out dwellings, art. 146 VI)

**Decision tree for residence type**:
- Primary: only taxe foncière + TEOM
- Secondary (résidence secondaire): + taxe d'habitation RS
- Loi de finances may evolve thresholds annually — check current

---

## Section: `--rental` (gîte / Airbnb)

**Data sources**:
- Local tourism office hébergements guide PDF — search `"<département>" hébergements meublés tourisme PDF`
- `https://www.airbnb.fr/<commune>-france/stays`
- Gîtes de France: national site `https://www.gites-de-france.com` (gitesdefrance.fr redirects there); départemental sites use inconsistent domains (e.g. `gitesdefrance-vienne.com` but `gites-de-france-dordogne.com`; `gitesdefrance-dordogne.com` does not resolve) — search `Gîtes de France <département>` (checked 2026-10-28)
- Tourism observatoire PDF for occupancy rates: `<dept>.fr/.../tourisme/observatoire/`
- INSEE monthly survey of collective tourist accommodation (hotels, campsites, other collective accommodation such as résidences de tourisme) — a seasonality proxy only: gîtes and other meublés are outside its scope ([INSEE source s2287](https://www.insee.fr/fr/metadonnees/source/operation/s2287/presentation))
- Reddit/forums for honest operator income reports

**Compute**:
1. Map existing competition (5–10 nearest gîtes with capacity + weekly tariff)
2. Pick configuration:
   - Convert one wing/basement → smaller unit, sleeps 4–6
   - Whole-house gîte → sleeps 8–12
   - Chambres d'hôtes → up to 5 rooms with breakfast
3. Realistic year-3 stabilised gross: 16–22 weeks × commune-typical rate (est. — skill heuristic; INSEE's occupancy survey does not cover gîtes, so calibrate on the competition mapped in step 1)
4. Apply tax regime:
   - Below €15k AND non-classé → micro-BIC 30 % abatement
   - Classé (or chambres d'hôtes) → micro-BIC **50 %** abatement (a non-classé above the €15k plafond cannot use micro-BIC → régime réel; 2025 data, source Service-Public A17883) (classement by a COFRAC-accredited or agréé organisme) — plafond **€83,600 for 2026 income onward** (€77,700 applies to 2025 income declared in 2026; classé + chambres d'hôtes, per Loi Le Meur 2024-1039 en vigueur 1 Jan 2025 — was €188,700 pre-reform — then the 2026-2028 triennial revaluation). (2026-10-28 verified; sources [BOFiP ACTU-2025-00127](https://bofip.impots.gouv.fr/bofip/14765-PGP.html/ACTU-2025-00127) + [Légifrance Loi 2024-1039](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050612711) + [Service-Public entreprendre A18813](https://entreprendre.service-public.gouv.fr/actualites/A18813))
   - Social contributions: classé meublé de tourisme — micro-social 6 % of turnover, due once annual turnover exceeds €23,000; chambres d'hôtes — 21.2 % from 1 Jan 2026 (was 12.3 %), due once income exceeds 13 % of the PASS (€6,123 in 2025); a non-classé meublé de tourisme can no longer use the micro-entrepreneur regime from 1 Jan 2026 (régime réel des travailleurs indépendants, contributions due above €23,000) (2026 data, sources URSSAF 4 Nov 2025 + Service-Public F39451)
   - Above €83.6k (2026 income; €77.7k for 2025 income) two calendar years running → régime réel
   - **Pending, not law — PLF 2027 art. 7 (bill, not adopted on 2026-10-28; Assemblée vote on the first part set for 3 Nov 2026)**: in the régime réel (a non-classé above €15k, or any gîte above €83.6k) amortisation of a meublé de tourisme would be deductible at most at 1.5 % and €5,000/yr per foyer fiscal (2.5 % and €7,000 for other furnished lets); a commission amendment allowing none for meublés de tourisme acquired from 1 Jan 2027 is not in the text the Assemblée is debating — the commission rejected the whole first part on 9 Oct 2026, so the séance works on the government text, where art. 7 was still unexamined after the 27 Oct sittings. Keep projections on current law until LFI 2027 is promulgated — see shared/regulatory-watch.md (FR) ([AN projet de loi n° 3210](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi))

5. Subtract 35–45 % operating costs (cleaning, linen, utilities, commissions) (est. — skill heuristic, not a published benchmark)
6. Compute net at TMI 11 % and TMI 30 %
7. Note: classement = 50 % abatement + 6 % URSSAF + plafond €83,600 (2026 income onward; €77,700 for 2025 income) vs 30 % / no micro-social regime from 2026 / €15k unclassified (Loi Le Meur 2024-1039 + 2026-2028 triennial revaluation; URSSAF 4 Nov 2025)

**Strategic levers**:
- **Classify it** — voluntary, 1–5 étoiles, valid 5 years; the inspection visit is paid by the owner and done by a COFRAC-accredited or agréé organisme of their choice (DGE; Service-Public F39451) — fee example, one département only: €180 TTC per meublé at the Aude ADT (note of 16 Jan 2026; lower rates only for several meublés in the same commune); ask the chosen organisme or the ADT (Agence Départementale du Tourisme) for its fee
- **Pool / spa** — a candidate revenue lever (unquantified — compare the pool / no-pool tariffs of the competition mapped in step 1)
- **Service à la personne** registration if you also offer in-person services
- **Taxe foncière exonération** under CGI art. 1383 E bis — a commune or EPCI may exempt classé meublés de tourisme and chambres d'hôtes in a France Ruralités Revitalisation (ZFRR) zone by délibération taken before 1 October; not automatic and TEOM stays due (Service-Public F59)

**Caveats**:
- Loi Le Meur (Nov 2024) lowered non-classé thresholds drastically (was 77.7k → now 15k)
- National registration number via a single national téléservice operated by the DGE (art. L324-1-1 III in force since **20 May 2026**; called Declaloc in secondary sources; décrets n° 2026-196 and 2026-197 du 19 mars 2026 govern the API meublés data flow to communes / EPCI and name the DGE as operator — they do not open the lessor téléservice) — per the DGE API meublés page (updated 23 Jul 2026) the lessor téléservice opens only in **Q4 2026**, as a Démarche Numérique form on a public DGE page; until then the commune's existing procedure applies (communal registration where instituted, otherwise mairie declaration) and platforms cannot demand a number in communes without a registration procedure; once it opens, registration becomes mandatory in every commune and holders of a communal number get several months to renew via the national téléservice, after which old numbers become invalid (Service-Public A18880, 27 Jul 2026); apimeubles.finances.gouv.fr is the commune / EPCI / platform portal, not a lessor entry point — administrative fines pronounced by the commune up to **€10,000** (défaut d'enregistrement) / **€20,000** (fausse déclaration or faux numéro, art. 4 Loi Le Meur). (2026-10-21 verified, sources DGE API meublés page + Légifrance L324-1-1 / décret 2026-196 + Service-Public A18880)
- DPE for meublés de tourisme (Loi Le Meur art. 3): a change-of-use authorisation requires class A–E (F and G excluded) since 21 Nov 2024 and A–D from 1 Jan 2034, metropolitan France only (CCH L631-10); from 1 Jan 2034 every gîte that is not the lessor's primary residence must meet the décence energy levels — the mayor may demand its DPE (astreinte €100/day) and letting a non-compliant unit carries an administrative fine up to €5,000 per unit (code du tourisme L324-2-2) (2026-10-21 verified, source Légifrance)

---

## Section: `--work=<profession>`

**Data sources** (depending on profession):
- **Healthcare**: Doctolib, ARS, ordres professionnels (Conseil de l'Ordre)
- **Teaching**: France Travail (Pôle emploi until 1 Jan 2024), écoles de musique régionales, conservatoires CRR/CRD/CIOL, EMIG-style intercommunal schools
- **Trades**: Chambre de Métiers et de l'Artisanat, INSEE artisans, Pages Jaunes
- **Tech / cadres**: APEC, LinkedIn, Welcome to the Jungle
- **Tutoring / private**: Superprof, Aladom, Apprentus, Allegro Musique, Spectable
- **Salaries general**: INSEE *base Tous salariés* (built from employers' DSN declarations) — 2025 private-sector net salary in full-time equivalent: mean **€2,797/month**, median **€2,238** (excl. agriculture and household employers; [Insee Première n° 2132](https://www.insee.fr/fr/statistiques/9087193), 22 Oct 2026); Hellowork, Journal du Net salaire (secondary)

**Legal status options** (always include):
- **Auto-entrepreneur (BNC libéral)**: simple, social contributions **25.6 %** of turnover for BNC services outside the Cipav from 1 Jan 2026 (**23.2 %** for professions libérales réglementées affiliated to the Cipav), plus 0.2 % CFP (2026 data, source [URSSAF — l'essentiel du statut](https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html)), plafond **€83,600** (2026-2028 triennium; was €77,700 through 2025) — BIC services and BNC libéral share the €83,600 services plafond per [URSSAF seuils 2026](https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/toutes-les-actualites/2026--modification-des-seuils-de.html) (2026-10-28 verified — rate and plafond)
- **Service à la personne (SAP)**: clients get a 50 % income-tax credit on what they pay (service-public F12, vérifié 15 Apr 2026) only if the provider is declared — the declaration is made on the téléservice **NOVA** (nova.entreprises.gouv.fr), not with URSSAF, and quotes and invoices must carry the declaration reference (servicesalapersonne.gouv.fr, updated 18 Dec 2025)
- **CCN ÉCLAT (associative music schools)**: *professeur* = coefficient 265 on the grille spécifique, full time = 24 h of service a week → **€1,912.59/mo gross minimum from 1 Jan 2026** (computed: 257 group-A points × V1 €7.23 + 8 × V2 €6.81). Two point values since avenant n° 182 of 1 Oct 2020 (in force 1 Jan 2022); V1 / V2 per avenant n° 208 of 23 Jun 2025, extended by arrêté of 9 Oct 2025 ([Légifrance](https://www.legifrance.gouv.fr/conv_coll/id/KALITEXT000052447622)); the 257 / 265 / 24 h grid is per fiche-paie.fr (secondary, updated 11 Oct 2026). *Animateur technicien* (257 points, 26 h) computes to €1,858.11, below the SMIC (€1,867.02 since 1 Jun 2026, URSSAF), so the SMIC applies
- **Public conservatoire (fonction publique territoriale)**: titular posts go through a concours — the external concours sur titres for *assistant d'enseignement artistique principal de 2e classe* (musique) is a 30-minute interview on a professional dossier that includes the candidate's diplôme d'État de professeur de musique or DUMI, or an equivalence (décret n° 2012-437; CDG concours brochure, June 2025)
- **Association loi 1901**: for community projects, no income to self
- **Régime réel BNC**: above €83.6k (2026 income onward; €77.7k for 2025 income)
- **Profession libérale réglementée** (médecin, avocat, etc.): specific regimes

**Catchment formula**:
- Local population in 30-min drive
- 60-min for online or rare specialties
- Account for English-speaking expat communities (Vienne, Charente, Haute-Vienne, Dordogne) — significant for British/Dutch/German-speaking professions

**Output sections to include**:
1. Catchment + competition table
2. Salaried options (CCN / convention)
3. Independent options (auto-entrepreneur)
4. Online / hybrid options
5. Realistic year-3 net (3 scenarios)
6. 12-month build plan

---

## Section: `--risks`

**Data sources** (in order of recommended individual-query path):

1. **ERRIAL — parcel-level synthesis (PRIMARY for individual address lookup)**: [errial.georisques.gouv.fr](https://errial.georisques.gouv.fr/) — free state service (since Feb 2021): from an address or cadastral parcel number it generates a pre-filled état des risques, ready to download; the owner must check it, complete it from the préfecture's website where needed, and add any natural- or technological-disaster indemnity paid on the property (source: georisques.gouv.fr IAL page, checked 2026-10-28). **This is the canonical individual-buyer entry point**; use first before going to file/PDF or API.
2. **DICRIM (commune-level statutory doc)**: `https://files.georisques.fr/DICRIM/DICRIM_<INSEE>.pdf` — download with curl (verify file exists, not all communes publish), render with pdftoppm if scanned
3. **IAL (Information Acquéreurs Locataires) — préfecture arrêtés and commune information**: on the préfecture site `https://www.<dept>.gouv.fr/` (paths and file names vary by département — search the site for 'IAL'); Géorisques tells owners to complete the ERRIAL output from it
4. **Géorisques portal (general risk lookup)**: `https://www.georisques.gouv.fr/` — 'Connaître les risques près de chez moi' search by address, map or cadastral parcel on the home page (updated 2026-10-28: the old `/mes-risques/connaitre-les-risques-pres-de-chez-moi` URL now redirects to the generic 'M'informer sur un risque' page)
5. **Géorisques API** (developer): officially documented (OpenAPI) at [georisques.gouv.fr/doc-api](https://www.georisques.gouv.fr/doc-api) — `api/v1/...` open, limited to 5 calls/s (1 call/s for `resultats_rapport_risque` and `rapport_pdf`); `api/v2/...` needs a Bearer token, 20 calls/s (source: Géorisques API spec v1.12.2, checked 2026-10-28); **use the ERRIAL portal for individual queries** unless you need batch-scale extraction. If invoking the API: respect [robots.txt](https://www.georisques.gouv.fr/robots.txt) + add `User-Agent: <descriptive>` header.
5. **ASNR potentiel radon** (published by the ASNR, created 1 Jan 2025; the commune map is the cartography established by the IRSN): `https://recherche-expertise.asnr.fr/savoir-comprendre/environnement/connaitre-potentiel-radon-ma-commune`
6. **DRIAS climate**: `https://www.drias-climat.fr/`
7. **PPI nucléaire** (if any plant within 50 km): EDF site + préfecture — the PPI around nuclear power plants covers 20 km (extended from 10 km in 2019; source ASNR)
8. **OSM industrial overlay**: Overpass query within 5 km

**11 risk categories to evaluate** (skill checklist, not a statutory DICRIM list; Géorisques' own list also covers coastal, cyclone, avalanche, volcanic, glacial, mining and polluted-soil risks — source georisques.gouv.fr 'M'informer sur un risque'):
1. Inondation
2. Mouvement de terrain (RGA argiles) — the national RGA exposure map was replaced by the arrêté du 9 janvier 2026 (JO n° 26 du 31 Jan 2026) to take in recent claims; it applies to promesses / deeds for buildable land and to house-building contracts signed from 1 Jul 2026 (CCH L132-4 ff.: soil studies before building in medium / strong zones); covers metropolitan France except the city of Paris (sources: Géorisques 2026 map page; INERIS AIDA text)
3. Sismicité (zone 1-5)
4. Tempête / grand froid / canicule
5. Cavités souterraines
6. Feu de forêt
7. TMD (transport matières dangereuses)
8. Rupture de barrage
9. Risque nucléaire
10. Risque industriel (ICPE Autorisation/Seveso)
11. Sécheresse

**Build-era hazards**:
- < 1949: lead paint (CREP), often poor foundations
- 1949–1997: asbestos very likely (slates, flue, vinyl, fibrocement)
- 1949–1980: poor thermal envelope (first French thermal regulation: 1974 — ecologie.gouv.fr)
- 1975–1995: aluminum wiring potential (est. — no French primary source found; the électricité diagnostic is the check)
- After 2000: modern standards but check if RT2012 compliant for thermal (RT2012 attestations are drawn up at the permit application and at completion — ask for them); RE2020 in force for houses and apartment buildings from 1 Jan 2022 (source: ecologie.gouv.fr)

**Climate change to 2050** — national reference (TRACC adaptation trajectory; Météo-France 2024 figures in SDES Chiffres clés du climat 2025, national medians): metropolitan France +2.7 °C in 2050 vs 1900-1930 (+2.1 °C vs 1976-2005), annual rainfall +4 %, summer rainfall −8 %, +3.1 days with maximum above 35 °C (vs 1976-2005); +2 °C by 2030 and +4 °C by 2100. Per-commune TRACC indicators: Météo-France Climadiag Commune (`https://meteofrance.com/climadiag-commune`). The Vienne basin example below is unsourced (est.):
- +1.6 °C (RCP 4.5) to +2.2 °C (RCP 8.5) (est. — no source or baseline found; check DRIAS or Climadiag Commune)
- +5 to +10 drought days/summer (est. — no source found)
- Less summer rain, more winter rain
- More heatwaves (longer + hotter)
- Forest fire risk rising

**Verdict logic for radon**:
- Zone 1 / Faible: 🟢 negligible
- Zone 2 / Faible, but with geological factors (major faults, underground mine workings) that can ease radon's transfer into buildings — the official label is not 'moyen' (ASNR): 🟡 test recommended
- Zone 3 / Significatif: 🟠 test strongly advised (no legal test duty for a private home, but zone 3 must be disclosed in the état des risques); above 300 Bq/m³ works or measures are needed — mechanical ventilation or regular airing, sealing of basements and pipes (sources: service-public F20599; ASNR: over 10 % of buildings on these formations exceed 300 Bq/m³)

---

## Section: `--mains`

**Data sources**:
1. **Sispea** (national registry): `https://www.services.eaufrance.fr/commune/<INSEE>/<latest_year>` — confirms which services exist (checked 2026-10-28 on Poitiers: year 2025 showed 'Donnée non disponible', 2024 — prices at 1 Jan 2025 — was the latest with prices; step back a year when the latest is empty)
2. **Selectra** mirror: `https://eau.selectra.info/commune/<INSEE>` — operator details
3. **Listing language** for assainissement keywords ("tout-à-l'égout", "fosse septique", "assainissement individuel")
4. **PLU / Géoportail Urbanisme**: `https://www.geoportail-urbanisme.gouv.fr/` — for zonage assainissement when published
5. **Mairie phone** (always note this is the authoritative source)

**Compute**:
1. Does the commune have a collective sewer service at all?
2. Is the property in the bourg (likely connected) or hamlet (likely individual)?
3. What did the listing say (silence is itself a signal)?
4. Confidence level: high (listing explicit + Sispea + bourg) / medium / low

**Verification path**:
1. Call **Mairie de <commune>**: phone in DICRIM
2. Ask: « Est-ce que la parcelle au <address> est en zone d'assainissement collectif et raccordée au réseau ? »
3. Request from seller:
   - Collective: certificat de conformité du branchement (a connection check is compulsory at sale only where a municipal arrêté — or, in Île-de-France, certain listed territories — imposes it; the SPAC report then serves as the diagnostic, at most 10 years old at the deed — service-public F31685)
   - ANC: diagnostic ANC < 3 years old at the deed (mandatory at sale); if non-conform, works within 1 year of the deed — by the seller, or by the buyer if bought as is (source: service-public F31685)

**Cost ranges (rural FR 2026)**:
- On collective, conform: redevance ≈ €1.50–2.50/m³ + connection fixed (est. range; Sispea national average for assainissement collectif €2.37 TTC/m³ at 1 Jan 2025, on 120 m³/yr with the fixed part included — Vienne département €2.39; read the commune's own figure on Sispea)
- On collective, non-conform branchement (1975 build typical): €2,000–€5,000 upgrade (est., no primary price source)
- In collective zone, not connected: €2,500–€8,000 + PFAC fee (est., no primary price source)
- Outside collective (ANC septic to install or replace): €7,000–€15,000 (est., no primary price source)

---

## Mandatory diagnostics matrix at sale (2026)

| Diagnostic | Required because | Validity |
|---|---|---|
| DPE | All sales (a house under 50 m² of floor area, or a classé or inscrit monument historique, is exempt) | 10 years; DPEs made 1 Jan 2018–30 Jun 2021 are no longer valid since 1 Jan 2025 (service-public F16096, F10798) |
| Audit énergétique | House or single-owner building (not a flat in a copropriété) with DPE E, F or G; D added from 1 Jan 2034 (DROM: F/G, E from 1 Jan 2028) | 5 years (service-public F37110) |
| État des risques (ERRIAL; ex-ERP) | Property in a natural / mining / technological PPR zone (approved or prescribed), seismic zone 2–5, radon zone 3, coastal-retreat zone or brush-clearing (OLD) zone; hand it over at the first visit (service-public F12239) | 6 months; update it if its information is no longer accurate at signing |
| Amiante | Building permit issued before 1 July 1997 | Unlimited (a new report is advised before a sale if renovation works were done); list-A materials under periodic monitoring need a new assessment within 3 years (service-public F742) |
| Plomb (CREP) | Built before 1 Jan 1949 | 1 year if positive, indefinite if negative |
| Termites | Commune in arrêté préfectoral | 6 months |
| Électricité | Installation > 15 yrs old | 3 years |
| Gaz | Installation > 15 yrs old (if gas) | 3 years |
| Assainissement non-collectif | Not connected to the public sewer | 3 years |
| Mérule | Commune in a prefectoral mérule zone | Mention in the promesse / acte, not a diagnostic — no set validity (service-public F10798) |
| Bruit (aéroport) | Housing or buildable land in an airport PEB zone A–D (service-public F35266) | — |
| Carnet d'information du logement (CIL) | Permit or déclaration préalable filed from 1 Jan 2023, or renovation works since then (service-public F10798, F36759) | Handed over by the deed at the latest |

⚠️ **DPE recalculated from 1 Jan 2026** (arrêté du 13 août 2025, JO 26 Aug 2025): electricity primary-energy conversion coefficient lowered 2.3 → 1.9. Officially ~850,000 homes exit F/G with no works (base 1 Jan 2023, of 4.8M passoires; the SDES simulation published 12 Nov 2025 gives ~700,000 fewer passoires among principal residences — 3.2M, 10.4 % of them, on 1 Jan 2025 figures); no label is downgraded, and every home's primary-energy figure falls, but a better label is not systematic and is most likely where heating and/or hot water are electric (heat pump, thermodynamic or electric water heater, electric heating) — the label stays the worse of the energy and GES scales, and the GES label does not change. DPEs edited from 1 Jan 2026 auto-apply the new coefficient; pre-2026 DPEs stay valid and a re-labelling attestation is free (no new visit) via the ADEME Observatoire DPE-Audit. **Second cut from 1 Jan 2027**: arrêté du 19 août 2026 (JORF n°0198 du 26 Aug 2026) lowers the coefficient again, 1.9 → 1.7; electricity-heavy homes may gain one class (rarely two, in small homes) and none is downgraded; DPEs edited from 1 Jan 2027 apply it automatically; a DPE still valid can get an ADEME attestation with the new label, otherwise it stays valid to its end date; the ministry's press release of 31 Aug 2026 gives no count of homes affected (press figures of ~300,000, attributed to the draft's impact sheet, not found on a primary source). (2026-10-28 verified; sources Légifrance JORFTEXT000052134589 + JORFTEXT000054747079, [ecologie.gouv.fr DPE FAQ](https://www.ecologie.gouv.fr/actualites/evolutions-du-calcul-du-dpe-reponses-vos-questions) (updated 23 Jul 2025), [ecologie.gouv.fr press release 31 Aug 2026](https://www.ecologie.gouv.fr/presse/dpe-audits-energetiques-publication-larrete-abaissant-facteur-conversion-lelectricite-17-1er), SDES 12 Nov 2025, service-public F16096 + [A18446](https://www.service-public.gouv.fr/particuliers/actualites/A18446) (1 Sep 2026); [economie.gouv.fr](https://www.economie.gouv.fr/actualites/un-nouveau-dpe-au-1er-janvier-2026-pour-favoriser-le-chauffage-electrique) and notaires.fr not re-read — economie.gouv.fr returns 403 to automated checks)

## Cost benchmarks (rural FR, 2026)

| Work | Cost |
|---|---:|
| Asbestos removal (small) | €1,500–€5,000 |
| Septic tank replacement (est., no primary price source) | €7,000–€15,000 |
| Mains drains connection (est., no primary price source) | €2,500–€8,000 |
| Full electrical rewire (200 m²) | €12,000–€20,000 |
| Roof replacement (slate, 150 m²) | €18,000–€30,000 |
| Insulation upgrade DPE E→D | €15,000–€25,000 |
| Insulation upgrade DPE E→C | €30,000–€50,000 |
| Wood stove installation | €3,000–€7,000 |
| Heat pump installation | €12,000–€20,000 |
| Pool (above-ground 6×3) | €5,000–€10,000 |
| Pool (in-ground 8×4 with deck) | €25,000–€45,000 |
| Building inspection (independent surveyor) | €600–€1,200 |
| Notary fees on €145k ancien | est. €11,600–€12,500 at 6.32 % DMTO; €10,900–€11,800 at 5.81 % (computed: DMTO €9,162 / €8,420 + émoluments €1,867 TTC + CSI and débours est. €600–1,500) |

## Common listing platforms

- **SAFTI** — clean fields, full extraction
- **SeLoger** — JS-heavy and bot-protected (HTTP 403 to scripted requests); the old mobile host `m.seloger.com` no longer resolves (NXDOMAIN, checked 2026-10-28), so read listings in a normal browser
- **Leboncoin** — sparse, often need manual reading; also carries private sales (particulier à particulier)
- **ParuVendu, Logic-Immo, Bien'ici** — standard
- **Orpi, Century 21, IAD, Capifrance** — standard agency

## Reddit / forum sources for operator stories

- r/AskFrance, r/france (FR-language)
- r/AmerExit, r/IWantOut (expat moves)
- Mumsnet "living overseas" Vienne / Charente / Limousin
- FrenchEntrée, Complete France, The Good Life France
- Living Magazine, etcetera magazine (English-speaking Vienne / Charente)
- AngloInfo Poitou-Charentes / Limousin

## Caveats unique to FR

- RVLLH cadastral reform ⚠️ postponed by LFI 2026 (art. 106) to **2028 declarations → 2031 tax impact** → no official taxe foncière impact figure published — data not publicly available, verify at DGFiP (2026-10-21 verified — dates per Légifrance art. 106 LFI 2026 + ANIL LF 2026)
- DPE G (since 1 Jan 2025), F (from 1 Jan 2028) and E (from 1 Jan 2034) fall below the décence floor for residential leases in metropolitan France (calendar restated in the contrat-type annex in force since 1 Oct 2026)
- Loi Le Meur (Nov 2024) tightens short-let regime
- Service à la personne: clients get a 50 % income-tax credit (crédit d'impôt, CGI art. 199 sexdecies) on expenses up to €12,000/yr (+€1,500 per child or over-65 household member, max €15,000; sub-caps such as €5,000 small gardening) — a large competitive lever (2026 data, source Service-Public F12)
- Micro-entreprise plafonds by activity (2026–2028): €83,600 for services and BNC and for all furnished letting including classé meublés de tourisme and chambres d'hôtes; €15,000 for non-classé meublés de tourisme; €203,100 for sales and hotel-type lodging (BOFiP 19 Aug 2026 + Service-Public entreprendre F39451 + URSSAF 4 Nov 2025; Service-Public entreprendre A18813 still lists chambres d'hôtes under €203,100, which conflicts with them)

## Quirks to know

- The IAL "argiles faible" is for the village center; the DICRIM commune-level RGA map often shows wider areas as Moyen
- Rural communes' collective sewer often only covers Rue Principale + immediate adjacent streets
- Many small départements only count traffic on D-roads with > 500 v/d; smaller D-roads are absent from the count program
- Departmental TFPB rate was merged into communal in the 2021 reform — current rates already reflect this
- Termites zone in Vienne 86 covers 117 of 266 communes (arrêté 14 Oct 2020, per the Cerema national register of termite arrêtés, checked 2026-10-28; the map still on vienne.gouv.fr shows the earlier arrêté 2015-DDT-5, 115 communes) — but the diagnostic may still be common practice elsewhere

## Verification authorities

- Mairie of the commune (phone in DICRIM)
- Notaire (for tax + sale conformity)
- SPANC (Service Public d'Assainissement Non Collectif) at the communauté de communes level
- ADT / Office de tourisme (for classement meublé tourisme)
- DDT (Direction Départementale des Territoires) for risks

## Leaving France — origin-country deregistration entry points

For FR-resident buyers moving abroad. **Doorway only** — see [`shared/cross-border.md`](../../shared/cross-border.md) for the framework + [`shared/home-tax.md`](../../shared/home-tax.md) § France for tax detail. Mandatory call-out: engage cross-border tax counsel in BOTH jurisdictions before moving the centre of vital interests.

| Register | Action | Authority | URL |
|---|---|---|---|
| Tax residence | File final-year déclaration with foreign address; verify CGI Art. 4 B residence test against destination DTA tie-breaker; flag CGI Art. 167 bis exit-tax check (holdings worth over €800,000 or at least 50 % of a company's profits, for taxpayers French-resident in at least 6 of the 10 years before leaving) | DGFiP — Particulier international | [impots.gouv.fr/international-particulier](https://www.impots.gouv.fr/les-conventions-internationales) |
| Tax address change | Change adresse fiscale via espace particulier | DGFiP | [impots.gouv.fr](https://www.impots.gouv.fr/) |
| Civil register | No central FR civil register; tax-address change is the binding state notice. Mairie of last residence may also be informed (informal). | Mairie | (commune-level) |
| Health insurance | Notify CPAM; if EU/EEA/CH destination, request **S1 form** via [Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883) for transition coverage | Assurance Maladie / CPAM | [ameli.fr](https://www.ameli.fr/) |
| Social security coordination | S1 (EU/EEA/CH) or bilateral totalisation agreement | CLEISS — Centre des Liaisons Européennes et Internationales de Sécurité Sociale | [cleiss.fr](https://www.cleiss.fr/) |
| IFI (wealth tax) | If worldwide RE > €1.3M as FR resident — final-year IFI filing; first non-resident year, IFI scope reduces to French-situs RE only | DGFiP IFI | [impots.gouv.fr/IFI](https://www.impots.gouv.fr/particulier/calcul-de-lifi) |
| France-treaty register (DTA lookup) | Find the relevant FR-destination DTA + tie-breaker article + MLI matches | DGFiP — Conventions fiscales internationales | [impots.gouv.fr/conventions-internationales](https://www.impots.gouv.fr/les-conventions-internationales) |

**Cross-link**: invoke `--cross-border` for the framework (DTA tie-breaker pointer + POEM/PE check + EU/EEA/CH free-movement clarification) and `--home-tax` for France-side annual / disposal / death / emigration detail (Art. 167 bis, IFI, Form 3916, etc.).

## Status

✅ **Fully populated** as of 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; department-level tax reference re-pointed to DGFiP 2026-09-18 per impots.gouv.fr). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Building-code / rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). PLF 2027 tracker entries (LMNP amortisation cap, PTZ parentalité) re-checked 2026-10-28 (see shared/regulatory-watch.md).

**Confidence**: HIGH for the `--tax` rates and thresholds (DMTO from the impots.gouv.fr table of 1 June 2026, art. 116 dates, notary émoluments barème, CSI 0.10 %, THRS majoration — BOFiP / Légifrance / DGFiP), the `--rental` legal and tax rules (micro-BIC plafonds and abattements, URSSAF meublé de tourisme rules from 1 Jan 2026, owner-paid classement — BOFiP / URSSAF / DGE / Service-Public), the mandatory diagnostics matrix (every row on service-public; DPE electricity factor 1.9 → 1.7 from 1 Jan 2027 per the arrêté of 19 Aug 2026), the legal and fiscal caveats and the Leaving France tax rows. MEDIUM for `--price` (DVF and Notaires-INSEE Q2 2026 are primary; the rural factor, walk-away discount and agency fee are est. heuristics, and MeilleursAgents and PAP are behind bot walls), `--traffic` (Vienne 2025 map only; hourly coefficients est., verdict bands are skill thresholds), `--work` (URSSAF 2026 rates and INSEE 2025 pay primary; CCN ÉCLAT group coefficients from a secondary source; catchment heuristics département-dependent and unverified), `--risks` (Géorisques, ASNR, the RGA map of 9 Jan 2026, radon duties and the national TRACC 2050 figures primary; the Vienne climate figures and the aluminium-wiring era are est., the forest-fire line is qualitative) and `--mains` (Sispea national sewer average €2.37 TTC/m³ primary; Selectra is a secondary mirror). MEDIUM for the PLF 2027 art. 7 and PTZ lines (bill, not adopted; Assemblée vote on the first part set for 3 Nov 2026) and for the DPE note's ~850,000 F/G-exit figure (economie.gouv.fr returns 403, not re-read). LOW for the VLC tariff, the débours range and the all-in notary totals, the gîte occupancy weeks and operating-cost ratio, and the mains and contractor cost rows (est., no primary price source).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-28 | 2026-10-28 Tier-A refresh | DVF national annual file (12 Oct 2026 release; no data for Alsace-Moselle and Mayotte), Notaires-INSEE Q2 2026 and the Vienne sparse-sales counts on primary sources; rural factor, walk-away discount and agency fee est.; MeilleursAgents and PAP content behind bot walls |
| `--traffic` | 2026-10-28 | 2026-10-28 Tier-A refresh | Vienne A1 2025 map read from the rendered page (legend, PL columns, index URL); hourly coefficients est., verdict bands are skill thresholds; other départements not checked |
| `--tax` | 2026-10-28 | 2026-10-28 Tier-A refresh | DMTO from the 1 June 2026 table (Mayotte 4.50 %), art. 116 dates (BOFiP), émoluments barème, CSI 0.10 %, THRS and the Dordogne DGFiP ratio re-read; VLC tariff and débours est.; PTZ line is a pending bill |
| `--rental` | 2026-10-28 | 2026-10-28 Tier-A refresh | Micro-BIC plafonds (BOFiP), URSSAF meublé de tourisme rules from 2026, owner-paid classement (DGE), CGI 1383 E bis and the Gîtes de France URL template checked; occupancy weeks, cost ratio and pool lever est.; CCH L631-10 and the 2026 décrets rest on the 2026-10-21 Légifrance reads; PLF 2027 art. 7 pending |
| `--work` | 2026-10-28 | 2026-10-28 Tier-A refresh | URSSAF 2026 rates (BNC 25.6 %) and €83,600 plafond, INSEE 2025 pay, SAP on NOVA, France Travail and ÉCLAT 2026 point values (Légifrance) re-verified; ÉCLAT group coefficients secondary; CIOL, EMIG and catchment heuristics unverified |
| `--risks` | 2026-10-28 | 2026-10-28 Tier-A refresh | ERRIAL, Géorisques portal and API, ASNR radon map and zone duties, PPI 20 km, RGA map of 9 Jan 2026, RE2020 and the national TRACC 2050 figures on primary sources; Vienne climate figures and aluminium-wiring era est.; forest-fire line qualitative |
| `--mains` | 2026-10-28 | 2026-10-28 Tier-A refresh | Sispea template and national sewer average (€2.37 TTC/m³ at 1 Jan 2025), connection-check and ANC rules (F31685) re-verified; contractor cost ranges est.; Selectra secondary |
| Mandatory diagnostics matrix at sale (and DPE note) | 2026-10-28 | 2026-10-28 Tier-A refresh | Every row on service-public; Bruit and CIL rows added; DPE factor 1.9 → 1.7 from 1 Jan 2027 (arrêté 19 Aug 2026, Légifrance); the ~850,000 F/G-exit figure not re-read (economie.gouv.fr 403) |
| Caveats unique to FR | 2026-10-28 | 2026-10-28 Tier-A refresh | DPE rental calendar, SAP crédit d'impôt (F12) and micro plafonds (BOFiP) re-read; RVLLH dates from the 2026-10-21 Légifrance read |
| Quirks to know | 2026-10-28 | 2026-10-28 Tier-A refresh | TFPB merge (impots.gouv.fr, BOFiP) and the Vienne termite arrêté (117 communes, Cerema register) confirmed; argiles and sewer-coverage lines are unsourced field heuristics; D-road counting line not checked |
| Leaving France (deregistration) | 2026-10-28 | 2026-10-28 Tier-A refresh | Exit-tax thresholds and residence test (CGI 167 bis), IFI €1,300,000 and the non-resident scope (F563) re-verified; CPAM and CLEISS rows: URLs live, content not re-read |
| Common listing platforms | 2026-10-28 | 2026-10-28 Tier-A refresh | SeLoger mobile host gone (NXDOMAIN), Leboncoin entries merged, SAFTI, ParuVendu, Bien'ici, Orpi, Century 21 and IAD live; Logic-Immo and Capifrance content behind bot walls |
| Country profile | 2026-10-28 | 2026-10-28 Tier-A refresh | geo.api, Géoplateforme geocoder and cadastre.gouv.fr URL templates return valid output; descriptive bullets not checked |
| DROM overlay | 2026-10-28 | 2026-10-28 Tier-A refresh | Prefixes 971–974 and 976 confirmed via geo.api; the deltas in `shared/fr-drom-overlay.md` not checked |

## Update history

- **2026-10-29** — Tier-A refresh (market, tax-legal, risk-infra; facts checked 2026-10-28); playbook-level date not re-stamped because `--price`, `--tax`, `--rental`, `--risks` and `--mains` each keep est. or unverifiable figures
  - Fully primary-verified (facts checked — changed / confirmed / unverifiable): Caveats unique to FR 7 — 3 / 4 / 0; Leaving France (tax rows) 9 — 1 / 8 / 0; Country profile (URL templates) 5 — 0 / 5 / 0; DROM overlay (prefixes) 5 — 0 / 5 / 0
  - Checked, not fully verified: `--price` 16 — 3 / 8 / 5; `--traffic` 16 — 5 / 5 / 6; `--tax` 37 — 13 / 22 / 2; `--rental` 31 — 8 / 19 / 4; `--work` 20 — 6 / 9 / 5; `--risks` 26 — 13 / 9 / 4; `--mains` 9 — 2 / 4 / 3; Mandatory diagnostics matrix and DPE note 44 — 13 / 28 / 3, plus 2 rows added; Common listing platforms 11 — 3 / 6 / 2; Quirks to know 5 — 0 / 3 / 2; Cost benchmarks (notary, septic and mains-drain rows only) 3 — 1 / 0 / 2
  - Main changes: DVF described as a national annual file with no data for Alsace-Moselle and Mayotte, plus the Notaires-INSEE Q2 2026 trend; DMTO re-read from the 1 June 2026 table (Mayotte 3.80 % → 4.50 %, 11 départements at 5.81 %, Indre alone at the 3.80 % share) and art. 116 dates per LFI 2026 art. 121; émoluments barème and CSI 0.10 %; non-classé meublés de tourisme out of the micro-entrepreneur regime from 1 Jan 2026; auto-entrepreneur BNC rate 25.6 %; CCN ÉCLAT 2026 pay (the old example was below the SMIC); Pôle emploi → France Travail; SAP declared on NOVA; classement paid by the owner; DPE electricity factor 1.9 → 1.7 from 1 Jan 2027; état des risques limited to listed zones; amiante validity unlimited; mérule a deed mention, not a diagnostic; Bruit and CIL rows added; RGA exposure map of 9 Jan 2026 (applies from 1 Jul 2026); radon zone labels and duties corrected; Géorisques API documented; Sispea national sewer average added; heuristics without a primary source labelled est.
