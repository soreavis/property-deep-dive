# Romania (RO) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: RON (free-floating; ~4.97 EUR/RON Apr 2026; **not in eurozone**, no firm target — fiscal deficit blocks ERM-II entry)
**Lang**: Romanian; English at top banks/legal firms; AMCCRS Bucharest seismic data Romanian-only

---

## Country profile

Romania (~19.04M pop on 1 Jan 2026 — 2026 data, source Eurostat demo_gind, estimate) joined EU 2007 and **completed full Schengen integration 1 Jan 2025** (air/sea was 31 Mar 2024). Major 2025-26 reforms hit hard: **VAT 19% → 21% (1 Aug 2025)**, local property tax baseline +79% (1 Jan 2026, Lege 239/2025), special tax on high-value residential buildings 0.3% → 0.9% of the taxable value above RON 2,500,000 (1 Jan 2026; Codul fiscal art. 500^2 lit. a) as amended by Lege 239/2025 art. XII pt. 51 — 2026 data, source legislatie.just.ro consolidated Codul fiscal). **Bucharest seismic risk is the country-defining due-diligence concern** — Vrancea zone generates intermediate-depth M6.5–7.5 events; 415 buildings listed in class Rs I (highest collapse risk) on the AMCCRS register (2026 data, source AMCCRS https://amccrs-pmb.ro/lista-imobile-2/, counted 2026-10-23). District heating crisis (Termoenergetica, was RADET — bankrupt 2019) affects most Bucharest panel-block buyers.

---

## Section: `--price`

**Primary index**: **INS (Institutul Național de Statistică)** — quarterly HPI (IPL)
- https://www.insse.ro/ (**permanent** JavaScript browser-verification wall — returns HTTP 503 with a "Verifying your browser" proof-of-work body to every non-JS client, on http and https; the site is alive, this is not an outage — allowlist `insse.ro` in the URL-liveness workflow rather than re-chasing it each cycle. 2026-10-23 verified)
- **Q2 2026 HPI**: 182.04 (2015=100), **+12.1% YoY**; Q1 2026 174.41; Q4 2025 168.99; new dwellings 177.49 (+12.8% YoY), existing dwellings 177.65 (+11.8% YoY) (2026 data, source Eurostat prc_hpi_q, dataset updated 2026-10-01, https://ec.europa.eu/eurostat/databrowser/view/prc_hpi_q/default/table)

**Bucharest asking prices (Sep 2026)**: apartments **€2,312/m²** average, **+8.6% YoY** (+0.3% MoM; average unit €134,000, 58 m²); houses/villas €2,342/m² (+7.5% YoY) (2026 data, source Indicele Imobiliare.ro https://www.imobiliare.ro/indicele-imobiliare-ro/bucuresti — listing platform, owners' asking prices, not transactions; INS doesn't publish €/m² directly — cross-check the trend against the HPI above)

**BNR (Banca Națională a României)**: https://www.bnr.ro/ — Financial Stability Report (Raport asupra stabilității financiare), half-yearly June / December editions — latest June 2026, approved 6 Jul 2026, with a residential real-estate chapter (§2.3) (2026 data, source BNR https://www.bnr.ro/uploads/2026-07-06raportasuprastabilitatiifinanciare-iunie2026_documentpdf_545_1783339608.pdf)

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| Imobiliare.ro | https://www.imobiliare.ro/ | Largest; prices quoted in EUR (search filters and index in €); publishes the monthly "Indicele Imobiliare.ro" of asking prices per city (2026-10-23 checked) |
| Storia.ro | https://www.storia.ro/ | Grupul OLX (site footer "© 2026 Storia, Grupul OLX"; not Adevinta); aggregates many agencies |
| OLX Imobiliare | https://www.olx.ro/imobiliare/ | Strong on private-seller listings ("Privat" / "Firma" seller filter, 2026-10-23 checked) |

**Verdict bands**:
- 🟢 within ±10% of Imobiliare.ro segment for comparable district + condition + seismic class
- 🟡 ±20%
- 🟠 ±30% — investigate: Bucharest Rs class? Restitution? Informal-build? Termoenergetica connection?
- 🔴 >±30% — significant red flag

**Critical Bucharest cross-check**: Pre-1977 building? Check **AMCCRS list** for Rs I/II/III/IV class before any offer. https://amccrs-pmb.ro/ — searchable register https://amccrs-pmb.ro/lista-imobile-2/ (2,798 rows on 2026-10-23: 415 Rs I, 491 Rs II, 164 Rs III, 11 Rs IV, 118 consolidated, 1,453 placed in an emergency category without a risk class, 144 neither, 2 without a usable class value; 2026 data, source AMCCRS)

---

## Section: `--traffic`

**Sources**:
- **Compania Națională de Administrare a Infrastructurii Rutiere (CNAIR)** road authority — the look-alike domain cnair.ro is an unrelated commercial API-integration site (2026-10-23 check); do not cite it as CNAIR
- **Bucharest real-time** via Waze
- **OSM Overpass** universal

---

## Section: `--tax`

### Currency note
RON, EUR/RON 5.3485 (BNR reference rate of 22 Oct 2026, floating; 2026 data, source BNR https://curs.bnr.ro/nbrfxrates.xml). Not in eurozone. No firm target.

### Major 2025-2026 reforms

- **VAT**: Standard rate raised **19% → 21% (1 Aug 2025)** (Legea 141/2025 art. II; Codul fiscal art. 291(1); 2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026). User assumption "VAT 19%" is now outdated.
- **Reduced VAT**: former 5% and 9% rates merged to single **11% reduced rate** from 1 Aug 2025 (art. 291(3) 5% rate repealed and art. 291(2) set at 11% by Legea 141/2025 art. II pt. 42–43). Ordinary housing is **not** on the 11% list: it covers only housing delivered as social policy (buildings for old-age / pensioners' homes and for children's homes / recovery centres for disabled minors, art. 291(2) lit. l); other new-build homes take the 21% standard rate (2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026)
- **New-build housing transitional 9% — ENDED 30 Sep 2026**: Legea 141/2025 art. III let an individual (alone or jointly with other individuals) buy one home at 9% VAT from 1 Aug 2025; Legea 161/2026 (M.Of. 642 of 4 Aug 2026) art. I moved the end date from 31 Jul 2026 to **30 Sep 2026 inclusive**. Conditions: useful area ≤ 120 m² (outbuildings excluded); value incl. land ≤ RON 600,000 ex-VAT; habitable at delivery, which could not be later than 30 Sep 2026; no other reduced-VAT home bought since 1 Jan 2023 per the reduced-VAT housing-purchase register (a one-home test, not a first-home test); an advance-payment deed concluded by 1 Aug 2025 — and, only for deeds concluded 3–31 Jul 2025, a 20% advance (ex-VAT) paid in full by 31 Jul 2025. A separate 9% limb for buildings delivered to town halls for subsidised rent ran until 1 Oct 2026 (art. I(4)). Legea 161/2026 art. II lets a buyer who paid the standard rate on qualifying homes bought "between 1 August 2026 and the law's entry into force" reclaim the 21%→9% difference for one home (the one whose VAT chargeable event came first), claimable from 1 Oct 2026 under a procedure set by ANAF president's order (publication of that order not confirmed as of 2026-10-23 — check at ANAF). **From 1 Oct 2026 new homes sold by VAT-registered developers carry the 21% standard rate**; no extending act appears in the Codul fiscal consolidated to 25.10.2026, which still reproduces the 30 Sep 2026 limit. A further extension to July 2027 was included in a 2026–2028 governing programme but had not become law (Economedia, 1 Oct 2026, secondary) — announced, not legislated (2026 data, sources: legislatie.just.ro Codul fiscal consolidated 25.10.2026 reproducing Legea 161/2026 art. I–II; Ministerul Finanțelor / UNNPR notice https://mfinante.gov.ro/static/10/Mfp/infotva/comunicatTVA9_21092026.pdf; ANAF AJFP Argeș notice AGG_DEX-17243/18.08.2026; Economedia https://economedia.ro/tva-de-21-la-locuintele-noi-de-la-1-octombrie.html)
- **Local property tax — major reform 1 Jan 2026** (Lege 239/2025, M.Of. 1160 of 15 Dec 2025; the statutory values, rates, reductions and exemptions in this bullet re-verified 2026-10-23 against the Codul fiscal consolidated to 25.10.2026, https://legislatie.just.ro/Public/DetaliiDocument/171282, and the Ministerul Finanțelor explanatory memo https://mfinante.gov.ro/static/10/Mfp/transparenta/EMproiectlegeredresareficientizareRP_28082025.pdf; the RON 1,492 indexed 2025 level (DITL Sector 5 table) and the apartment-owner impact estimate at the end still carry the 2026-05-27 stamp, source ProTV / Europa Libera / juridice.ro): Taxable value baseline (residential, concrete/brick frame + full utilities) raised from **RON 1,492/m² → RON 2,677/m² (+79%)** — 1,492 is the 2025 inflation-indexed level applied by councils under Codul fiscal art. 491 (DITL Sector 5 Bucharest table); the Code's own pre-2026 table read 1,000 lei/m², and 2,677 is now written into the art. 457(2) table itself (Legea 239/2025 art. XII pt. 28; 2026-10-21 verified, source legislatie.just.ro Codul fiscal consolidated 18.10.2026). The notarial market-study basis (O.G. 16/2022), scheduled for 1 Jan 2026, **did not take effect** — the Codul fiscal Title IX consolidated at 18 Oct 2026 contains no studiile de piață reference (repealing provision not located; 2026-10-21 verified) — the Ministerul Finanțelor explanatory memo projected that the mass-valuation IT system could supply values in 2026 for the 2027 tax base, but Title IX consolidated to 25.10.2026 schedules no market-value switch for individuals, and on 19 Oct 2026 Finance Minister Alexandru Nazare said market-value property taxation will not apply in 2027, with 2027 measures to be set in the 2027 budget (Alba24, 19 Oct 2026, news — secondary; verify the 2027 basis at Ministerul Finanțelor / the local primărie). The pre-2026 age reductions (10% for 30–50 yrs, 30% for 50–100 yrs, 50% for >100 yrs; former art. 457(8)) were eliminated by Lege 239/2025, but **O.U.G. 9/2026 restores age cuts of 15% (50–100 yrs) and 25% (100+ yrs)** (O.U.G. 9/2026 art. VII pt. 3, M.Of. 157 of 27 Feb 2026, in force 27 Feb 2026, as new Codul fiscal art. 457(6^1); age taken at 1 Jan of the reference tax year; O.U.G. 9/2026 art. IX regularises local tax already overpaid; 2026-10-21 verified, source legislatie.just.ro Codul fiscal consolidated 18.10.2026). The −0.10 correction-coefficient cut for apartments in blocks with more than 3 levels and 8 apartments (former art. 457(7)) was **eliminated**. The full exemption for the home of owners with severe or marked disability or grade I invalidity (former art. 456(1) lit. t) was **removed** (Lege 239/2025 art. XII pt. 23 rewrote art. 456(1)); O.U.G. 9/2026 (art. VII pt. 2, M.Of. 157 of 27 Feb 2026, applied to the whole 2026 tax year) replaced it with a **50% cut** for the home of an owner with severe disability and a **25% cut** for marked disability, legal representatives caring for such a person included (new art. 456(2^5)–(2^6); no grade I invalidity limb). Statutory cota per Codul Fiscal art. 457–458: **0.08–0.2% residential / 0.2–1.3% non-residential** (set by hotărâre de consiliu local; art. 457(1^1) bars a council from setting a lower residential rate than its 2025 rate). Apartment owners typically see local tax up **70–80%**, in Bucharest Sector 1 close to doubled — not adjusted for the O.U.G. 9/2026 age-cut restoration; no revised impact figure is published in the source entry.
- **Special tax on high-value properties** (Codul fiscal art. 500^1–500^2): 0.3% → **0.9%** from 1 Jan 2026 (Legea 239/2025 art. XII pt. 51), charged on the part of a residential building's art. 457 taxable value (the statutory lei/m² value, not market price) above RON 2,500,000, and on the part of a car's purchase value above RON 375,000 (2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026)
- **Full market-value taxation**: **NOT legislated for 2027.** Codul fiscal art. 457 (consolidated 25.10.2026) still uses the statutory lei/m² value, and Title IX schedules no market-value switch. The reform was removed from the PNRR conditions in the June 2026 renegotiation (interim minister Dragoș Pîslaru, 22 Jun 2026, Economedia https://economedia.ro/breaking-impozitarea-proprietatilor-la-valoarea-de-piata-a-fost-eliminata-din-pnrr-pislaru-nu-era-neaparat-in-acest-moment-o-reforma-care-sa-corespunda-asteptarilor-societatii.html, news), and on 19 Oct 2026 Finance Minister Alexandru Nazare said it will not apply in 2027, with 2027 measures to be set in the 2027 budget; the government keeps a gradual, undated move to market value as a goal (Alba24 https://alba24.ro/impozitul-pe-case-apartamente-si-alte-proprietati-nu-se-va-calcula-la-valoarea-de-piata-din-2027-anuntul-ministrului-finantelor-1163344.html, news) — announced, not legislated; re-check when the 2027 budget / fiscal package is published
- **Securities / crypto gains** — *not* real estate: self-declared securities gains 10% → 16% from 2026 income (Codul fiscal art. 123(1^2), Legea 239/2025 art. XII pt. 16); gains through Romanian intermediaries are withheld at 3% (held ≥ 365 days) or 6% (< 365 days) (art. 97(8^1)); crypto gains 16% (art. 116) (2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026)

### Transfer / acquisition costs (individual buyer)

- **Notary fee**: progressive minimum-fee grid set by Ordinul ministrului justiției 177/C/2024 (M.Of. 70 of 26 Jan 2024; named as the applicable order by Camera Notarilor Publici București in 2026). Above RON 600,001: RON 6,405 + 0.6% on the amount above RON 600,001 (RON 200,001–600,000: RON 2,805 + 0.9% above RON 200,001), plus VAT at the 21% standard rate on the fee and a RON 10–20 archiving fee; computed on the declared value, or on the notarial-study minimum if that is higher (2026 data, source CNPB https://www.cnpb.ro/onorariul-notarial and the order text https://www.cnpb.ro/assets/2024/12/norme-onorarii-2024.pdf)
- **Land Registry intabulation (carte funciară)**: 0.15% of the declared value for individuals (0.5% for legal entities), minimum RON 60 per property, applied to the notarial-study value if the declared value is lower; collected by the notary for ANCPI (ANCPI Order 16/2019; 2026 data, source CNPB https://www.cnpb.ro/tarifele-de-carte-funciara)
- **Minimum reference value**: Notaries use published "studii de piață privind valorile minime imobiliare" (formerly grilele notariale) per locality. If declared sale price < grid minimum, taxes computed on grid minimum. Updated at least annually (Codul fiscal art. 111(5)); the CNPB page https://www.cnpb.ro/studiile-de-piata-privind-valorile-minime-imobiliare covers only Bucharest and Ilfov, Călărași, Giurgiu, Ialomița and Teleorman counties (2026 studies published there) — elsewhere use the regional Camera Notarilor Publici (2026 data, source CNPB)

### Capital gains tax — individual sale

- **3%** of the transaction value (the declared price — a tax on the gross value, not on the gain) if held **≤3 years inclusive** (Codul fiscal art. 111(1); 2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026)
- **1%** if held **>3 years**
- Calculated and collected by the notary before the deed is authenticated (art. 111(6))
- Computed on the declared value, or on the notarial-study minimum if the declared value is lower (art. 111(4)–(4^1))
- **No primary-residence exemption** — RO does NOT exempt main home, unlike many EU peers; art. 111(2) exempts only restitution, gifts between relatives up to the 3rd degree and between spouses, retroactive annulments, possession notation in the land book and one dare-în-plată (Law 77/2016) transfer
- **Note**: the 16% rate (2026) applies to self-declared securities gains and crypto gains, NOT real estate

### Rental income tax

- **10% flat** on net rental income (after 20% lump-sum deductible expense allowance; effective 8% of gross = 10% × 80%) (Codul fiscal art. 64(1), art. 84(3); 2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026)
- **CASS health-insurance contribution** of 10% (art. 156) once cumulative annual non-salary income such as rent, investment and other-source income reaches 6 gross minimum wages; the base is then fixed at 6, 12 or 24 minimum wages depending on the band reached (art. 170(2)–(3); 2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026)
- Hosts on Airbnb/Booking: ANAF in 2025 identified ~22,000 undeclared operators; only ~20% compliant. Enforcement sharply tightening

### AML / cash limits (Law 70/2015)

- Cash payments between professional entities and individuals: daily threshold RON 10,000
- Cash payments by professional entities: RON 5,000/day per person
- Mandatory ONPCSB reporting by reporting entities of cash transactions ≥ EUR 10,000 equivalent, linked operations included, within 3 working days (Legea 129/2019 art. 7(1), (7); 2025 data, source ONPCSB-published consolidated text to Legea 86/2025, https://onpcsb.ro/uploads/articole/attachments/6840001f7c620400832154.pdf)
- Real-estate agents and developers (Legea 129/2019 art. 5(1) lit. h) and notaries (lit. f) are AML reporting entities; standard customer due diligence applies to occasional transactions ≥ EUR 15,000 equivalent (art. 13(1) lit. b)

---

## Section: `--rental`

### STR / Airbnb

- **Mandatory**: "Certificat de clasificare" from the Ministerul Economiei, Digitalizării, Antreprenoriatului și Turismului (MEDAT), under the Order 65/2013 norms as amended by MEDAT Order 948/2026 (M.Of. 559 of 8 Jul 2026): documentation filed online on the dedicated platform (SITUR, https://situr.gov.ro/) or at the ministry's office; individual operators (persoane fizice) may classify at most **7 rooms / 14 places** as `apartamente` and/or `camere de închiriat în locuințe familiale` they own, whatever the number of homes; a copy of the certificate and its annex sheet (or the provisional operating authorisation) plus the phone number of the ministry's tourism-control unit must be displayed visibly at reception (or in the entrance hall where there is no reception) (2026 data, source M.Of. 559 bis of 8 Jul 2026, Order 948/2026 art. I pts. 3, 6, 23). Fee: earlier listed as free — not re-verified on 2026-10-23, confirm with MEDAT
- **Cash register obligation (2025)**: Airbnb hosts must issue receipts and use cash register for in-person payments (2025 data — rates/figures may have changed since; verify with ANAF)
- **Bucharest**: no specific Bucharest license layer beyond national classification; sectorial control by ANAF + the MEDAT tourism-control unit, whose phone number must be displayed with the classification certificate (Order 948/2026 art. I pt. 23; the specific number previously listed here could not be verified on 2026-10-23 — take it from MEDAT)
- **2025 enforcement**: Fines RON 10,000–40,000 (~EUR 2,000–8,000) for unlicensed operation; ANAF March 2025 sweep recovered tax on RON 260M of undeclared 2023-2024 income (2025 data — rates/figures may have changed since)
- **Tourist tax**: levied locally — the consolidated Codul fiscal (Oct 2026) has no national hotel tax; local councils, in Bucharest the Consiliul General al Municipiului București, may adopt a special tax for the locality's tourism promotion (`taxă specială pentru promovarea turistică a localității`, Codul fiscal art. 484(1),(4); 2026 data, source legislatie.just.ro). The Bucharest rate listed earlier (1% of the accommodation tariff per night) was not re-verified on 2026-10-23 — check the current HCGMB on local taxes
- **Tax regime (from 2026 income, Lege 239/2025 art. XII)**: short-term letting by an individual (uninterrupted stays by the same guest of max 30 days) of **1–7 rooms** in homes they own, whatever the number of homes, is rental income (`cedarea folosinței bunurilor`): net = gross − **30% lump-sum**, platform commission excluded from gross, **10% final tax** (≈7% of gross, computed 10% × 70%), plus a mandatory occupancy sheet (`fișa de ocupare a capacității de cazare`). From the tax year in which more than **7 rooms** are let short-term, the income is independent-activity income under art. 68^3 (same 30% lump-sum and 10% rate). 2025 income stays under the rules then in force (2026 data, source Codul fiscal art. 67(1^1), 68^3, 83(2)–(4), 85, 133(35) — legislatie.just.ro consolidated text, 2026-10-23)

---

## Section: `--work=<profession>`

Bucharest IT/services hub; Cluj tech hub ("Silicon Valley of Eastern Europe"); Timișoara, Iași, Sibiu/Brașov regional centers. Romania has substantial IT outsourcing and shared-services economy.

**Labour-market reference**: unemployment **6.4%** (Aug 2026, seasonally adjusted, https://ec.europa.eu/eurostat/databrowser/view/une_rt_m/default/table); national gross minimum wage **RON 4,325/month** at the July 2026 reference date (2026-S2), up from RON 4,050 in 2025 and H1 2026, ≈ €825 at Eurostat's conversion (https://ec.europa.eu/eurostat/databrowser/view/earn_mw_cur/default/table) (2026 data, source Eurostat)

---

## Section: `--risks`

### Seismic — CRITICAL for Bucharest

- **Vrancea zone** generates intermediate-depth (60-180 km) M6.5–7.5 events; the largest since 1700 in the INFP ROMPLUS catalogue are Mw 7.9 (26 Oct 1802) and Mw 7.7 (10 Nov 1940) (2026 data, source INFP https://www.infp.ro/data/romplus.txt, downloaded 2026-10-23)
- INFP statistical recurrence: M≥6 every ~10 years, M≥7 every ~33 years, M≥7.5 every ~80 years (attribution not located on infp.ro, 2026-10-23). Computed cross-check from the INFP ROMPLUS catalogue (https://www.infp.ro/data/romplus.txt, downloaded 2026-10-23; box 45.2–46.2°N / 25.9–27.3°E, depth ≥60 km): Mw ≥7.0 — 4 events 1900–2026 → 126 / 4 = 31.5-yr mean interval (13 since 1700 → 326 / 13 ≈ 25 yrs); Mw ≥7.5 — 4 since 1700 → 326 / 4 = 81.5 yrs; Mw ≥6.0 — 7 since 1950 → 76 / 7 ≈ 10.9 yrs (the catalogue also lists 26 Mw ≥6.0 entries for 1900–1949, all quality C/D, so the M≥6 rate depends on the window)
- **Last major: 4 Mar 1977, Mw 7.4, hypocentre 94 km depth** (source INFP ROMPLUS catalogue https://www.infp.ro/data/romplus.txt, downloaded 2026-10-23, and INFP tour brief https://www.infp.ro/doc/news/20240221/tur.pdf, 2024 — 90% of victims were in Bucharest, mainly from the partial or total collapse of 32 buildings); **1,578 dead, 90% of them in Bucharest** (source AOSR event note with INFP researchers, https://aosr.ro/en/45-years-since-the-1977-earthquake-lessons-learned); Lungu et al. 2004 give 1,574 dead including 1,424 in Bucharest (Acta Geodaetica et Geophysica Hungarica 39(2–3), https://real.mtak.hu/82025/); Alba24's press compilation gives 1,570 dead and **32,900 dwellings collapsed or severely damaged** (secondary, press) — totals differ between compilations
- **AMCCRS (Bucharest seismic consolidation administration)**: https://amccrs-pmb.ro/
- Building classes: **Rs I** (high collapse risk in design earthquake), Rs II (major structural damage), Rs III (moderate), Rs IV (no significant damage)
- AMCCRS online register (2,798 entries, expertise years up to 2026), counted by last classification: 415 Rs I, 491 Rs II, 164 Rs III, 11 Rs IV → 415 + 491 = 906 in classes I–II; a further 1,453 sit in an urgency category without an Rs class, 144 in neither, 118 are listed as consolidated (2026 data, source AMCCRS register table behind https://amccrs-pmb.ro/2022/06/clasa-i-de-risc-seismic-2/, exported and counted 2026-10-23). Not exhaustive: sector-hall seismic expertises done within thermal-rehabilitation programmes are mostly not forwarded to AMCCRS (per hartablocuri.ro — secondary)
- **Citizen map (volunteer-run)**: https://www.hartablocuri.ro/ — personal project, not associated with any company or state institution; estimated construction years, floor plans and seismic classes for 83,000+ blocks (Bucharest + 36 counties complete by July 2026); data ~80% own research, ~10% city halls, ~10% site visitors (2026 data, source hartablocuri.ro) — widely used by buyers, but not an official register: confirm any class with AMCCRS / the sector primărie
- **Homes in buildings expertised as Rs I are excluded from mandatory PAD disaster insurance until the consolidation works are received** (Legea 260/2008 art. 3(6), as amended by Legea 115/2023, M.Of. 403 of 11 May 2023, consolidated text 11 Nov 2023; 2026-10-23 verified, source legislatie.just.ro https://legislatie.just.ro/Public/DetaliiDocument/99019); voluntary cover stays legally possible without a PAD policy (art. 3(9)), but insurer appetite varies and **banks may refuse mortgages**

### Flood

- **Apele Române**: https://rowater.ro/
- 526 designated Areas of Potential Significant Flood Risk (APSFR), identified by the second-cycle (2019) preliminary flood risk assessment (2023 data, source World Bank results brief https://www.worldbank.org/en/results/2023/03/22/flood-hazard-and-risk-maps-development-and-use-of-flood-maps-to-strengthen-integrated-flood-risk-management-in-romania) — rates/figures may have changed since (third Floods Directive cycle; recheck at Apele Române)
- Second-cycle flood hazard + risk maps (World Bank–supported; results brief dated 22 Mar 2023) cover all 526 APSFRs. Public Web GIS viewer (MMAP / ANAR): https://harticiclul2.inundatii.ro/map — layers for mean exceedance periods of 3, 10, 100, 200 and 1,000 years, a 100-year climate-change scenario and dike-breach scenarios, plus first-cycle layers (2026 data, source viewer layer list, 2026-10-23)
- Annual expected damage: EUR 1.7 billion, affecting up to 150,000 citizens a year (2023 data, source World Bank results brief above — World Bank–supported national flood risk assessment; partners: Ministry of Environment, Waters and Forests, Apele Române, National Institute of Hydrology and Water Management) — rates/figures may have changed since. The MMAP / ANAR site inundatii.ro states a different measure: an average realised cost of EUR 140M/yr to the economy and >EUR 1 billion of damage avoided yearly by existing defences (undated, source https://inundatii.ro/)
- INSPIRE EU dataset record: https://inspire-geoportal.ec.europa.eu/srv/api/records/b275eed0-198b-11e5-b939-0800200c9a66 ❌ DEPRECATED — dead on 2026-10-23 (redirects to the data.europa.eu home page; the record ID resolves on data.europa.eu to Poland's MZP/MRP flood maps, catalogue geoportal-pl, not a Romanian dataset); verify with Apele Române https://rowater.ro/ and the viewer https://harticiclul2.inundatii.ro/map
- Flood-risk information site (MMAP / ANAR; Floods Directive implementation, river-basin pages, link to the map viewer): https://inundatii.ro/ — the `www.` host fails TLS (certificate covers inundatii.ro only, 2026-10-23)

### Forest fires
- Less affected than Mediterranean peers but Carpathian/Apuseni dry seasons rising
- AFM (Administrația Fondului pentru Mediu): https://www.afm.ro/ (JavaScript browser-verification wall — HTTP 503 "Verifying your browser" to non-JS clients, the same wall as insse.ro; 2026-10-23 check)

### Government risk hub
- https://inundatii.ro/ (MMAP / ANAR flood-risk site; map viewer https://harticiclul2.inundatii.ro/map; GET and HEAD both answered 200 on 2026-10-23, no browser check)

### Mandatory diagnostics

- **Energy Performance Certificate (Certificat de Performanță Energetică)**: mandatory under Law 372/2005. Valid 10 years from issue unless a major renovation changes the building's energy use (art. 21(2)); a certificate issued without the ministry's unique registration code is void (art. 21(8), added by Legea 238/2024). Seller must hand the buyer a copy **before** the contract; a sale concluded without it **is voidable** (relative nullity under the Civil Code, art. 22(1),(4)). Original transmitted to buyer at deed (art. 22(2)); when the contract is registered, the owner files a copy with the competent fiscal authority (art. 22(3)). Sale before completion: certificate without a unique code and not entered in the national database, with the full certificate due at reception (art. 23(3)) (source legislatie.just.ro https://legislatie.just.ro/Public/DetaliiDocument/66970, consolidated text of 25 Jul 2024 — the latest consolidation listed on 2026-10-23)
- **Seismic risk class**: NOT mandatory disclosure at sale legally, BUT Bucharest pre-1977 buildings publicly listed by AMCCRS in classes Rs I–IV. **Rs I homes are excluded from mandatory PAD insurance until consolidation is received (Legea 260/2008 art. 3(6)); banks may refuse mortgages.** Single largest "gotcha" in Bucharest property — always check pre-1977 buildings against AMCCRS list before any offer
- **Radon**: Order No. 153/2023 (effective Aug 2023) implements EU 2013/59/EURATOM; reference 300 Bq/m³. Mandatory testing in workplaces in radon-prone areas. **NOT yet mandatory for residential sale**, but advisable in Cluj/Bihor/Alba/Bistrița/Sibiu
- **No mandatory termite/asbestos/lead-paint diagnostic** at sale — Romania has no French-style DDT bundle. Buyer-beware regime

---

## Section: `--mains`

### Cadastre / Land Registry (eTerra3)

**ANCPI — Agenția Națională de Cadastru și Publicitate Imobiliară**:
- https://www.ancpi.ro/ — institutional (RO + EN)
- https://geoportal.ancpi.ro/ ❌ DEPRECATED — dead on 2026-10-21; verify with ANCPI https://www.ancpi.ro/ and the county OCPI — ANCPI's 20 Aug 2026 notice, still the ancpi.ro homepage on 2026-10-21, lists the public Geoportal among the platforms (with RTI, MyEterra, Registrul proprietarilor, Titluri de proprietate) to be brought back "etapizat"; no Geoportal restart notice on ancpi.ro as of 2026-10-21. Background: July 2026 ransomware attack (unauthorised access detected 14 Jul 2026, https://gov.ro/ro/media/comunicate/stadiul-repunerii-in-functiune-a-sistemului-informatic-e-terra-in-urma-incidentului-de-securitate-cibernetica); e-Terra restarted 11–12 Aug 2026 (https://gov.ro/ro/media/comunicate/aplicatia-e-terra-i-a-reluat-activitatea); payment-link function restored 20 Aug 2026. Before the outage the public parcel viewer ("Aplicație vizualizare imobile") was at `/imobile.html` (Wayback capture 2026-06-14; the older `/geoportal/imobile/Harta.html` path already redirected there by Dec 2024) — re-check the path once ANCPI announces the restart. Public. (2026 data, source ANCPI / gov.ro; 2026-10-21 verified)
- https://eterra.ancpi.ro/eterra/ — e-Terra (eTerra3), integrated cadastre + land book; replaces the dead eterra3.ancpi.ro host (NXDOMAIN 2026-10-21). **Auth-only**: since the 11–12 Aug 2026 restart, accounts are held by ANCPI/OCPI staff, notaries, authorised cadastral surveyors, court technical experts and bailiffs (https://gov.ro/ro/media/comunicate/aplicatia-e-terra-i-a-reluat-activitatea, 12 Aug 2026); the login host answered 403 "Acces restricționat — ANCPI" (maintenance notice) on 2026-10-21
- https://myeterra.ancpi.ro/ ❌ DEPRECATED — dead on 2026-09-18, still NXDOMAIN 2026-10-21; ANCPI said (per Alba24, 2 Oct 2026 — news-only) MyEterra is in security and performance testing and ePay functions will be folded into it; verify with ANCPI https://www.ancpi.ro/ and the county OCPI — citizen self-service portal that gave owners free CF-for-information and cadastral-plan extracts (ADR https://www.roeid.ro/w/ancpi). **Auth via ROeID** — foreign buyer without ROeID **cannot self-serve**. Until MyEterra is restored nobody can self-serve: the CF extract for information comes from the OCPI/BCPI counter or via a notary or authorised cadastral surveyor with an e-Terra account (https://gov.ro/ro/media/comunicate/aplicatia-e-terra-i-a-reluat-activitatea, 12 Aug 2026). Fees: `extras de carte funciară pentru informare` RON 25 at the counter (RON 20 online), `extras de carte funciară pentru autentificare` RON 40 (2019 data, ANCPI Order 16/2019, https://legislatie.just.ro/Public/DetaliiDocument/209916 — rates may have changed since)
- **CF (carte funciară) is the canonical identifier** for any parcel
- eTerra3 = production system (replaced legacy eTerra). All county OCPI offices route through it

### Bucharest district heating — major pain point

- **RADET went bankrupt in 2019**; municipal company **Termoenergetica** took over (DO NOT use "RADET" in 2026 docs)
- Serves >8,000 apartment blocks (~90% of city heating)
- Pipe network corroded — reported losses of est. >2,000 tons of hot water/hour in worst sections (press-sourced figure — verify with Termoenergetica)
- Termoenergetica's unpaid balance to ELCEN (generator) stood at RON 1.39 billion on 12 Oct 2026 (invoices for Dec 2025–Aug 2026 deliveries, oldest 255 days overdue); RADET's legacy claims in its insolvency creditor mass add RON 3.66 billion (registered 5 Oct 2016) + RON 0.16 billion (supplementary, to 30 Nov 2019) (2026 data, source ELCEN debt table https://www.elcen.ro/ — creditor-published)
- Bucharest mayor + EU funding (~EUR 260M) commenced rehabilitation of 210 km primary network (4-year programme)
- **Buyers in Bucharest district-heated blocks should expect periodic winter outages, scheduled 2026-2029 disruptions for pipe replacement, and ongoing tariff uncertainty.**

### Other mains
- **Other cities**: Cluj, Timișoara, Iași, Constanța — DH similarly aged but smaller-scale. Apartments with **centrală proprie** (individual gas boiler) vs **conectare la termoficare** is a major valuation differentiator
- **Gas**: Distrigaz Sud (Engie) for Bucharest/south, E.ON Gaz for north
- **Electricity**: Hidroelectrica + Nuclearelectrica generation; four concession distribution operators (2025 data, source ANRE https://anre.ro/consumatori/afla-care-este-distribuitorul-tau-de-energie-electrica/, page dated 18 Nov 2025): **Rețele Electrice România** (PPC group, per reteleelectrice.ro) — Bucharest, Ilfov, Giurgiu + Banat + Dobrogea; **Distribuție Energie Electrică Romania (DEER)** — Transilvania Nord, Transilvania Sud, Muntenia Nord; **Delgaz Grid** — Bacău, Botoșani, Iași, Neamț, Suceava, Vaslui; **Distribuție Energie Oltenia** — Argeș, Dolj, Gorj, Mehedinți, Olt, Teleorman, Vâlcea
- **Water/sewage**: Apa Nova (Veolia subsidiary) for Bucharest; municipal RAJA companies elsewhere. Rural areas: high % unconnected to mains sewage

---

## Section: `--crime`

See `shared/crime-sources.md`. Romania uses:
- **Inspectoratul General al Poliției Române (IGPR)**: https://www.politiaromana.ro/ (redirects to politiaromana.ro; served a "Site temporar indisponibil" maintenance page on 2026-10-23 — retry)
- **INS criminality data**

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

---

## Cost benchmarks (Oct 2026)

| Item | Range / typical |
|---|---|
| Bucharest €/m² asking, apartments (Sep 2026) | €2,312 (+8.6% YoY; 2026 data, source Indicele Imobiliare.ro — listing platform) |
| Cluj-Napoca | €3,316/m² asking, apartments (+5.0% YoY; Sep 2026 data, source Indicele Imobiliare.ro — listing platform) |
| Timișoara / Iași / Brașov | €1,984 / €2,000 / €2,309 per m² asking, apartments (YoY +8.2% / +6.7% / +4.6%; Sep 2026 data, source Indicele Imobiliare.ro — listing platform) |
| VAT new-build | 21% standard rate on new homes sold by developers since 1 Oct 2026 — the transitional 9% (extended by Legea 161/2026) applied only to deliveries up to 30 Sep 2026 inclusive and has expired; the 11% reduced rate covers only social-policy buildings (old-age/pensioner homes, children's homes, rehabilitation centres for disabled minors), not ordinary housing; an extension to July 2027 in the 2026–2028 governing programme had not become law on 1 Oct 2026 (2026 data, sources ANAF AJFP Argeș AGG_DEX-17243/18.08.2026; Codul fiscal art. 291(2) lit. l), legislatie.just.ro; economedia 1 Oct 2026, secondary) |
| CGT (>3 years held) | 1% of transaction value (3% if held ≤3 years; Codul fiscal art. 111(1)) |
| Local property tax baseline (1 Jan 2026) | RON 2,677/m² × locality/zone coefficient (0.90–2.60), less any age cut (15% / 25%), × council rate 0.08–0.2% (Codul fiscal art. 457) |
| Total acquisition costs (buyer) | est. 1.3% statutory on a RON 800,000 deed: notary minimum RON 7,605 + 21% VAT RON 1,597 + land-registry 0.15% RON 1,200 = RON 10,402; any agency commission, lawyer and translator fees come on top |

---

## Active fiscal incentives (Oct 2026)

- **9% VAT on qualifying new-build homes — ENDED 30 Sep 2026**, no longer active (Legea 161/2026 had extended it from 31 Jul 2026); 21% standard rate since 1 Oct 2026; a July 2027 extension in a 2026–2028 governing programme is announced, not legislated (see `--tax`)
- **1% CGT after 3 years** (vs 3% under)
- **Schengen full integration 1 Jan 2025** — EU buyer access uplift

---

## Foreign-buyer rules

- **EU/EEA citizens**: full equality with Romanian citizens since **1 January 2014** (end of 7-year derogation post-2007 accession). Includes agricultural land and forests
- **Non-EU/EEA individuals**: **Cannot own land directly** (Constitution Art. 44(2): foreigners and stateless persons acquire land only under EU-accession terms or international treaties on a reciprocity basis under organic law, or by legal inheritance). They CAN own buildings/apartments, just not the underlying land plot. Workaround: buy a building only (`drept de superficie`) or set up a Romanian SRL. **SRL holding cost from 2027**: Codul fiscal art. 460(1) — the 0.08–0.2% band for residential buildings owned by legal entities — and art. 460(4) are repealed from 1 Jan 2027 (Legea 239/2025 art. XII pt. 32, in force per art. XIII(1) lit. c inserted by O.U.G. 78/2025). The Ministerul Finanțelor explanatory memo states the intent that legal entities keep only the non-residential regime: art. 460(2) 0.2–1.3% on an art. 460(5) value (e.g. an authorised valuation, to be updated every 5 years under art. 460(6); 5% rate if not updated after notification, art. 460(8)). Art. 453 lit. f) still defines "residential" by use, not owner, so the 2027 rate for company-held homes is unconfirmed until the 2027 fiscal package (2026 data, source legislatie.just.ro Codul fiscal consolidated 25.10.2026 and Legea 239/2025 https://legislatie.just.ro/Public/DetaliiDocument/305208)
- **Reciprocity treaty**: some non-EU nationalities can own land if their state has a reciprocity agreement with RO — case-by-case via lawyer
- **Agricultural land**: right of preemption applies (co-owners, lessees, neighbors, young farmers, ANAF, RO state) — Law 17/2014. Foreigners face same preemption stack + ministry approval for plots >30 ha

---

## Country-specific quirks

- **Restitution Laws 18/1991, 1/2000, 10/2001, 247/2005, 165/2013**: Communist-era confiscated agricultural land (18/1991), forests (1/2000), and urban properties (10/2001) restituted in rem where possible, otherwise compensated. **Key risk**: if a property has unresolved restitution claim (uncommon now but possible for buildings sold without good-faith DD in 1990s/2000s), title can be voided years later. **Always demand `extras de carte funciară` showing clean title chain back to pre-1945 or to a clear post-restitution adjudication**
- **Informal/illegal builds**: 1990s saw widespread construction without permits, especially rural. "Carte funciară" must show building registered (intabulat) — if only land registered and structure isn't, it's an unauthorized build. Common around Bucharest commuter belt (Ilfov: Voluntari, Popești, Berceni). Legalization possible via court (Law 50/1991 amendments) but expensive and slow
- **Brașov/Sibiu/Sighișoara German Saxon heritage**: pre-1945 ethnic-German Saxon population largely emigrated post-1989 (Aussiedler). Old town Sibiu (UNESCO buffer) and Brașov have heritage protection — major renovations require Direcția Județeană pentru Cultură approval. Some properties restituted to Saxon heirs in Germany; chains of title sometimes complex
- **Rural land consolidation**: parcels micro-fragmented (post-1991 restitution divided land back to pre-collectivization owners' heirs). Buying a "10 ha plot" can mean assembling 30+ titles. Ministerial pre-emption stack (Law 17/2014) bites
- **Anti-mafia / source-of-funds**: Cash limit RON 10,000 daily. Notaries are AML reporting entities (Legea 129/2019 art. 5(1) lit. f): standard customer due diligence (identity, beneficial owner, purpose and, where applicable, source of funds — art. 11(1)) applies to occasional transactions ≥ EUR 15,000 equivalent (art. 13(1) lit. b), and cash transactions ≥ EUR 10,000 are reported to ONPCSB (art. 7(1)); bank-to-bank wire is standard above the cash threshold
- **Constitutional land rule for non-EU/EEA citizens** (citizenship-based, not residence-based; Constitution Art. 44(2)): Non-EU individuals cannot own land directly except by legal inheritance or under a reciprocity treaty. SRL workaround standard — budget for the 1 Jan 2027 repeal of the legal-entity residential band (see Foreign-buyer rules)

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre + title | ANCPI / OCPI | https://www.ancpi.ro/ |
| Tax authority | ANAF | https://www.anaf.ro/ |
| National Bank | BNR | https://www.bnr.ro/ |
| Notary minimum-value studies | CNPB (Bucharest chamber: București + Ilfov, Călărași, Giurgiu, Ialomița, Teleorman; 2026 study online, checked 2026-10-23 — other counties are not on this page) | https://www.cnpb.ro/studiile-de-piata-privind-valorile-minime-imobiliare |
| Bucharest seismic | AMCCRS | https://amccrs-pmb.ro/ |
| Citizen seismic map | hartablocuri.ro | https://www.hartablocuri.ro/ |
| Floods | Apele Române | https://rowater.ro/ |
| Risk maps hub | MMAP / ANAR (flood map viewer https://harticiclul2.inundatii.ro/map) | https://inundatii.ro/ |
| Nuclear / radon | CNCAN | https://www.cncan.ro/ |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastral extract (myeTerra) | https://myeterra.ancpi.ro/ ❌ DEPRECATED — dead on 2026-09-18, still NXDOMAIN 2026-10-21; verify with ANCPI https://www.ancpi.ro/ and the county OCPI — interim: OCPI/BCPI counter, or a notary / authorised cadastral surveyor with an e-Terra account (https://gov.ro/ro/media/comunicate/aplicatia-e-terra-i-a-reluat-activitatea, 12 Aug 2026) |
| Cadastre map | https://geoportal.ancpi.ro/ ❌ DEPRECATED — dead on 2026-10-21; verify with ANCPI https://www.ancpi.ro/ and the county OCPI — listed in ANCPI's 20 Aug 2026 notice (still the ancpi.ro homepage on 2026-10-21) among the platforms to be brought back "etapizat" after the July 2026 ransomware attack (https://gov.ro/ro/media/comunicate/stadiul-repunerii-in-functiune-a-sistemului-informatic-e-terra-in-urma-incidentului-de-securitate-cibernetica); no restart notice as of 2026-10-21 (2026 data, source ANCPI / gov.ro; 2026-10-21 verified) |
| HPI quarterly | https://www.insse.ro/ |
| Bucharest seismic class | https://amccrs-pmb.ro/ |
| Property-tax CGT | https://taxsummaries.pwc.com/romania/individual/income-determination |
| Flood maps | https://harticiclul2.inundatii.ro/map (MMAP / ANAR viewer; agency home https://rowater.ro/) |

---

## Status

**Confidence**: HIGH on the statutory tax figures re-checked 2026-10-23 against the Codul fiscal consolidated text on legislatie.just.ro (VAT 21% since 1 Aug 2025, art. 291(1); local property tax baseline RON 2,677/m², art. 457(2); CGT 3% if held ≤3 years / 1% if held >3 years, art. 111(1)) and on the end of the transitional 9% new-build VAT, which covered deliveries up to 30 Sep 2026 inclusive only (Legea 161/2026; ANAF AJFP Argeș notice AGG_DEX-17243/18.08.2026) — new homes sold by VAT-registered developers carry 21% since 1 Oct 2026. HIGH on Termoenergetica's debt to ELCEN (refreshed to Oct 2026) and the AMCCRS register class counts (counted 2026-10-23). MEDIUM on: no further 9% extension enacted (secondary news only, Economedia 1 Oct 2026); Bucharest and regional €/m² levels (Imobiliare.ro asking-price index, listing platform, Sep 2026) read against the Eurostat HPI (Q2 2026); per-municipality 2026 tax rates (set by each council); the 2027 local-tax basis — the Codul fiscal holds no market-value switch and Finance Minister Nazare said on 19 Oct 2026 it will not apply in 2027 (news-only, Alba24; confirm with the 2027 budget package); the Rs I–IV class definitions (OG 20/1994 not re-fetched). LOW on: the July 2027 9% extension (in a 2026–2028 governing programme, not legislated; revisit 2026-11-15); completeness of the AMCCRS register (see the `--risks` counts of entries without an Rs class); the `--rental` enforcement figures (fines range, ANAF RON 260M sweep, cash-register rule — unrefreshed 2025 data) and the `--mains` Termoenergetica network figures (not re-fetched). Cadastre / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)
- 2026-08-07: `--tax` local property tax — O.U.G. 9/2026 restores building-age cuts (15% for 50–100 yrs, 25% for 100+ yrs); O.G. 16/2022 notarial market-study basis repealed, market values deferred to the 2027 base (superseded: no 2027 switch legislated, see the 2026-10-23 entry); source re-pointed to Ministerul Finanțelor (regulatory-watch RO entry, verified 2026-08-07)
- 2026-10-21: Cadastre / tax tracker entries re-checked (December regwatch wave, run early; see shared/regulatory-watch.md).
- 2026-10-23: refresh wave. Re-verified (see the per-section table): `--price` with listings (7 changed, 1 confirmed, 2 unverifiable — Eurostat HPI to Q2 2026, Bucharest asking prices to Sep 2026, BNR stability report half-yearly, Storia under Grupul OLX), `--work` (1 added: Eurostat unemployment and minimum wage), Cost benchmarks (5 rows changed, 2 confirmed; heading → Oct 2026; total acquisition cost recomputed), `--crime` (1 changed, 1 confirmed), `--amenities` / `--climate` (pointers confirmed), Verification authorities (2 changed, 7 confirmed), Source URL templates (1 changed, 5 confirmed). Partly re-verified, still on the 2026-04-26 playbook date: `--tax` (17 changed, 20 confirmed, 5 unverifiable — transitional 9% new-build VAT ENDED 30 Sep 2026, 21% since 1 Oct 2026; market-value taxation not legislated for 2027; EUR/RON → BNR reference rate of 22 Oct 2026; AML customer due diligence from EUR 15,000), `--rental` (4 changed, 6 unverifiable — MEDAT Order 948/2026 classification, 2026 STR income-tax regime, tourist-tax basis Codul fiscal art. 484), `--risks` (15 changed, 9 confirmed, 7 unverifiable — 1977 event Mw 7.4 / 94 km per INFP, AMCCRS register recount, Rs I homes excluded from PAD insurance, dead INSPIRE record deprecated), `--mains` (2 changed, 4 confirmed, 8 unverifiable — ELCEN debt, ANRE distribution operators), `--traffic` (1 changed, 1 unverifiable), Country profile (3 changed, 3 confirmed, 3 unverifiable), Active fiscal incentives (9% VAT retired; 1 changed, 1 confirmed, 1 unverifiable), Foreign-buyer rules (1 changed, 2 confirmed, 2 unverifiable), Country-specific quirks (2 changed, 1 confirmed, 5 unverifiable). Confidence line recomputed. Playbook-level date not re-stamped: `--tax`, `--rental`, `--risks` and `--mains` still hold claims not re-fetched.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` (incl. listings) | 2026-10-23 | 2026-10-23 refresh wave | Eurostat HPI to Q2 2026; Bucharest asking €/m² to Sep 2026 (Imobiliare.ro index — listing platform); BNR stability report half-yearly; AMCCRS register counts; portal notes corrected (EUR pricing, Storia under Grupul OLX, OLX seller filter) |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Eurostat unemployment (Aug 2026) and minimum wage (2026-S2) added; hub descriptions curated, qualitative |
| `--crime` | 2026-10-23 | 2026-10-23 refresh wave | Pointer section, no figures; IGPR site identity confirmed (maintenance page served); INS crime data behind its JS wall |
| `--amenities` | 2026-10-23 | 2026-10-23 refresh wave | Pointer only — `shared/amenities-osm.md` present |
| `--climate` | 2026-10-23 | 2026-10-23 refresh wave | Pointer only — `shared/climate-projections.md` present |
| Cost benchmarks | 2026-10-23 | 2026-10-23 refresh wave | City rows → Sep 2026 Imobiliare.ro asking prices (listing platform); VAT row → 21% since 1 Oct 2026; CGT and RON 2,677/m² checked against the Codul fiscal; total acquisition cost recomputed from the notary grid and land-registry tariff |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | 9 URLs answered 200; content checked for CNPB, AMCCRS, ANAR, CNCAN, hartablocuri.ro and inundatii.ro; CNPB scope and flood-viewer link corrected |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | myeTerra / Geoportal still NXDOMAIN (DEPRECATED kept); PwC tax summary content checked (1% / 3% CGT, 10% rental tax); flood maps row → MMAP / ANAR viewer |

---

## Extension TODOs

- AMCCRS Rs I/II/III/IV list integration — expose as a Bucharest-specific cross-check inside `--integrity`
- Termoenergetica connection check by address (currently address → block → registry must be done manually)
- Market-value property-tax transition tracker (no switch legislated for 2027; watch the 2027 budget and fiscal package — see `--tax`)
- Restitution-claim red-flag scanner enhancement
