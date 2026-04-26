---
name: property-deep-dive
description: Universal property due-diligence skill. Pull any or all of twenty-two sections — ten core (price/traffic/tax/rental/work/risks/mains/crime/amenities/climate) + five financial/process (finance/currency/visa/insurance/notary) + seven decision-context (compare/retirement/digital-nomad/macro/demographics/esg/exit) — for any address worldwide. 44 countries fully populated (FR + IT + CZ + SK + DE + AT + CH + ES + PT + SE + FI + NO + UK + NL + BE + DK + IS + SI + IE + GR + PL + CA + AU + NZ + EE + HR + HU + MX + BR + AR + CR + PA + RS + ME + BA + MK + AL + LT + LV + RO + BG + LU + CY + MT) in countries/<iso2>/. Plus 4 cross-cutting layers: --integrity (data-honesty checks), --journey=<type> (decision templates: pre-offer/post-offer/foreign-buyer/investor/renovation/gite-bnb/inheritance), --type=<kind> (6 specialised property templates: off-plan/auction/probate/plot-only/heritage/apartment-vs-house). Plus tooling: TCO calculator, mortgage calculator, test fixtures, listing-diff watcher, comparable-transactions DB, auto-validate cron tracking. Outputs to terminal, MD file, or both.
user-invocable: true
argument-hint: "<address> [--country=<iso2>] [--all] [--price] [--traffic] [--tax] [--rental] [--work=<profession>] [--risks] [--mains] [--crime] [--amenities] [--climate] [--finance] [--currency] [--visa] [--insurance] [--notary] [--compare=<iso2,...>] [--retirement] [--digital-nomad] [--macro] [--demographics] [--esg] [--exit] [--tco] [--mortgage] [--watch] [--integrity] [--journey=<type>] [--type=<kind>] [--listing=<url>] [--save[=<path>]] [--quick|--deep] [--override-confidence=<HIGH|MEDIUM|LOW>] | --update[=<iso2>[,<iso2>...]] [--validate-only|--refresh-only] [--add=<iso2>] [--diff] [--interactive] [--test] | --health-report"
---

# Property Deep-Dive (`/property-deep-dive`)

Master router for property due-diligence across multiple countries. Parses the address, detects the country, loads that country's playbook from `countries/<iso2>/playbook.md`, and runs the requested sections.

## When to use

Trigger this skill when the user:
- Asks about a property: "check this house", "is X address worth Y?", "what are the risks at...", "tax estimate for..."
- Pastes a real-estate listing URL (SAFTI, SeLoger, Rightmove, ImmoScout24, Idealista, Funda, Otodom, Sreality, Zillow, Realtor.com, etc.)
- Mentions a specific address in a real-estate / due-diligence context
- Says `/property-deep-dive` or asks to "analyse this house"

Skip if it's a code question or a generic real-estate market question (no specific address).

## Arguments

`$ARGUMENTS` is the user's input. Parse as: `<address> [flags]`.

**Address forms** accepted:
- Full street address: `1 Rue Principale, 86430 Adriers, France`
- Partial: `Adriers 86430` or `Berlin Mitte 10115`
- Listing URL: any platform URL — fetch the address from the listing
- Coordinates: `46.2582, 0.8040`

**Country detection** — in this priority order:
1. `--country=<iso2>` flag (e.g., `--country=fr`, `--country=de`, `--country=uk`)
2. Country name in the address ("France", "Germany", "España", "United Kingdom")
3. Postcode pattern matching:
   - **FR**: 5 digits (`86430`), French commune/dept name nearby
   - **DE**: 5 digits (`10115`), German city/Bundesland name
   - **ES**: 5 digits (`28013`), Spanish city/CCAA
   - **IT**: 5 digits (`00100`), Italian comune/regione
   - **UK/GB**: alphanumeric (`SW1A 1AA`, `EC1A 1BB`)
   - **NL**: 4 digits + 2 letters (`1011 AA`)
   - **BE**: 4 digits (`1000`)
   - **CH**: 4 digits, Swiss canton/commune
   - **AT**: 4 digits, Austrian Bundesland
   - **PT**: 4-3 (`1100-001`)
   - **PL**: NN-NNN (`00-001`)
   - **CZ**: NNN NN (`110 00`)
4. Reverse-geocode lat/lon via Nominatim, take `address.country_code`
5. If still ambiguous, ask the user explicitly

**Section flags** (combine any, default = `--all`):

| Flag | What it produces |
|---|---|
| `--all` | All fifteen sections (default if no section flag specified) |
| `--price` | Listing price vs commune €/m² (or local currency), comp listings, fair-value verdict |
| `--traffic` | Traffic counts, road classification, noise translation |
| `--tax` | Property tax + transaction tax + future revaluations |
| `--rental` | Realistic short-let / gîte / Airbnb income, regulatory regime, net |
| `--work=<profession>` | Local employment options for the named profession |
| `--risks` | Natural + technological risks (acute hazards); build-year hazards |
| `--mains` | Mains drains / sewer connection check + verification path |
| `--crime` | Commune-level crime rates + trend + national/regional comparison (per-country source registry in `shared/crime-sources.md`) |
| `--amenities` | Distance to grocery / DIY / pharmacy / GP / hospital / schools / public transport via OSM Overpass (universal logic in `shared/amenities-osm.md`) |
| `--climate` | Climate change projections per coordinate: temperature trajectory, sea-level rise, heatwaves, drought, wildfire, degree-day shift (universal logic in `shared/climate-projections.md`) |
| `--finance` | Foreign-buyer mortgage availability, LTV cap (non-resident), 10-yr fixed rate, FX-loan rules, banks with non-res desks (universal logic in `shared/finance.md`) |
| `--currency` | Currency code, peg status, FX volatility, capital controls, hedging market depth, 2025-26 currency reforms (universal logic in `shared/currency.md`) |
| `--visa` | Residency-by-investment / citizenship-by-investment / property-linked visa programs and current status (open/restricted/ENDED) (universal logic in `shared/visa-programs.md`) |
| `--insurance` | Catastrophic-risk reinsurance scheme, flood/earthquake policy availability, mortgage-mandatory rules, climate-risk reforms (universal logic in `shared/insurance.md`) |
| `--notary` | Notary required (civil-law) vs solicitor (common-law), days from offer to deed, closing costs as % of price, title insurance norms, 2025-26 reforms (universal logic in `shared/notary-process.md`) |
| `--compare=<iso2,...>` | Side-by-side multi-country comparison for relocation/investment (universal logic in `shared/compare.md`) |
| `--retirement` | Retiree-specific filter: pension taxation, healthcare, climate, expat communities (`shared/retirement.md`) |
| `--digital-nomad` | DNV availability + thresholds, internet quality, coworking density, time-zone overlap (`shared/digital-nomad.md`) |
| `--macro` | Inflation, GDP growth, central-bank policy rate, sovereign yield context (`shared/macro.md`) |
| `--demographics` | Population, aging, schools, family-friendly metrics (`shared/demographics.md`) |
| `--esg` | EPC distribution, climate exposure, community impact, carbon-tax/energy levy (`shared/esg.md`) |
| `--exit` | Sell-side liquidity, time-on-market, agent commissions, sell-side closing costs (`shared/exit.md`) |
| `--tco` | 30-year total cost of ownership calculator bridging --tax / --finance / --insurance / --notary (`shared/tco-calculator.md`) |
| `--mortgage` | Monthly P&I + amortization + stress-test wired to live --finance rates (`shared/mortgage-calculator.md`) |
| `--watch <url>` | Add a listing URL to the watchlist for price-drop / status-change tracking (`shared/listing-diff-watcher.md`) |

**Cross-cutting layers** (combine with sections):

| Flag | What it produces |
|---|---|
| `--integrity` | 4 data-honesty checks on top of standard output: dispute resolver, listing photo OCR, listing-vs-cadastre cross-check, red-flag scanner (`shared/integrity-checks.md`) |
| `--journey=<type>` | Decision-context templates that re-shape findings into a workflow output. Types: `pre-offer`, `post-offer`, `foreign-buyer`, `investor`, `renovation`, `gite-bnb`, `inheritance` (`shared/journeys.md`) |
| `--type=<kind>` | Specialized property-type checks layered onto standard output. Full templates: `off-plan`, `auction`, `probate`, `plot-only`, `heritage`, `apartment-vs-house`. Additional flags `mixed`, `agricultural`, `coastal`, `commercial` are recognised by the dispatcher but currently render only standard sections (no specialised overlay yet) (`shared/property-types.md`) |

Multiple cross-cutting layers can stack: `--integrity --journey=pre-offer,foreign-buyer --type=off-plan`.

**Output flags**:

| Flag | Behaviour |
|---|---|
| `--save` | Save full report to MD. Default location logic below. |
| `--save=<path>` | Save to a specific path |
| `--quick` | Single-pass, ~2 min; minimal external lookups |
| `--deep` | Multi-pass with Tavily + agents + PDF extraction; ~10–15 min (default for `--all`) |
| `--listing=<url>` | Use this listing URL as primary source (auto-detected if URL present) |

### Save-path logic

When `--save` is used without a path:
1. If a git project is detected and `_local/reports/` exists → save there
2. Else if `_local/` exists → create `_local/reports/` and save there
3. Else if `.gitignore` contains `_local` → create `_local/reports/` and save there
4. Else → save to current working directory

Filename: `property-<country>-<commune-slug>-<section-or-all>-<YYYY-MM-DD>.md`. Example: `property-fr-adriers-all-2026-04-25.md`.

## Master execution flow

1. **Parse `$ARGUMENTS`** — extract address, country (if explicit), flags, listing URL.
2. **Country detection** — run the priority cascade above. If ambiguous, ask the user.
3. **Load country playbook** — read `countries/<iso2>/playbook.md` from this skill folder. If the file doesn't exist, see "Unsupported country" below.
4. **Pre-flight (universal)** — see `shared/preflight.md`:
   - Geocode address (Nominatim) → (lat, lon, postal code, admin units, OSM road `osm_id`)
   - Identify the road via Overpass (ref, highway class, maxspeed)
   - Fetch listing if URL given (universal extraction prompt)
   - Cache local admin facts: population, sub-admin, neighbouring localities
5. **Run requested sections** — for each requested section, execute the country playbook's section instructions (data sources, compute steps, output template). Run independent sections in parallel where possible.
6. **Assemble draft** — combine into MD per the shared template.
7. **🔒 Anti-hallucination validation gate (MANDATORY)** — before printing or saving, run the seven pre-output checks in `shared/anti-hallucination.md`. Any check that fails BLOCKS output until fixed. Failures must trigger fix-passes, not workarounds. If a fix-pass cannot satisfy a check, the offending claim must be removed or replaced with `data not publicly available — verify at <authoritative source>`.
8. **Inject quality footer** — append the mandatory verification footer + the run-quality notes block (if any source failed during the run).
9. **Output** — print to terminal and/or save to MD.
10. **One-line follow-up** — offer a `/schedule` agent if appropriate (skip for single-section or `--quick` runs).

## 🔧 Updater mode

The skill has a maintenance mode for keeping country playbooks fresh. Sources change, rates shift, regulations get added — the updater keeps everything current.

**Invocation**:

```
/property-deep-dive --update                              # update ALL populated countries
/property-deep-dive --update=fr                           # one country
/property-deep-dive --update=fr,it,cz,sk                  # selected list
/property-deep-dive --update --validate-only              # URL liveness only (~5 min)
/property-deep-dive --update --refresh-only               # re-research data only
/property-deep-dive --update --add=pl                     # populate a scaffold country fully
/property-deep-dive --update --diff                       # show planned changes; do not write
/property-deep-dive --update --interactive                # confirm each playbook before writing
```

**What the updater does**:

1. **Validates every URL** in each country playbook (HTTP HEAD/GET, classify 2xx / 3xx / 4xx / 5xx)
2. **Replaces broken URLs** by searching for current equivalents on the same primary source
3. **Re-researches fast-changing data** (price benchmarks, tax rates, regulatory changes)
4. **Applies the anti-hallucination guard** to all changes
5. **Backs up and logs** every change to `playbook.md.bak-<date>` and an "Update history" section
6. **Outputs a maintenance report** to `_local/reports/property-deep-dive-update-<date>.md`

**Recommended cadence**:

| Mode | Cadence | Time |
|---|---|---|
| `--validate-only` | Monthly | ~5 min |
| `--refresh-only` per country | Quarterly | ~10 min/country |
| `--update` (full) | Annually | ~30 min total |
| `--add=<iso2>` (populate scaffold) | As needed | ~30 min/country |

The full playbook is in `shared/updater.md`. **Always run `--diff` first** if uncertain; `--interactive` is the safest mode.

### Auto-downgrade — confidence decay over time

Every section's confidence label decays automatically:

| Original | After 6 mo | After 12 mo | After 18 mo |
|---|---|---|---|
| HIGH | MEDIUM | LOW | STALE |
| MEDIUM | LOW | STALE | STALE |

The decay is computed at **render time** (every section invocation), not only during `--update`. A 14-month-old playbook never displays "Confidence: HIGH" silently. See `shared/updater.md` § Auto-downgrade for the full spec, including:
- Per-section `**Last verified**: YYYY-MM-DD` stamp (defaults to playbook Status footer)
- `--override-confidence=<level>` flag for hand-verified single-section runs
- `regulatory-watch.md` Tier 1/2 entries that bypass the calendar entirely (e.g., a fresh tax reform makes a 4-month-old `--tax` stamp meaningless)
- `STALE` tier banner that suppresses output until `--update` re-stamps

`/property-deep-dive --health-report` produces a per-country / per-section decay matrix to plan the next `--update` batch.

### Regulatory watch

`shared/regulatory-watch.md` is the **single source of truth for "what changed when"** — date-stamped reform tracker covering:
- ENDED programs registry (golden visas, NHR, MEIN, CBI — anti-hallucination critical)
- Recently enacted reforms (last 24 months, all 44 countries)
- Pending / in-flight reforms with revisit dates
- EU directive transposition deadlines (EPBD recast 2024/1275 due 29 May 2026, AMLD6, DAC8, etc.)
- Watchlist (rumored / proposed)

Consult this file before any `--tax`, `--rental`, `--visa`, `--finance` output. A Tier 1 entry (e.g., MT MEIN ENDED) makes the corresponding playbook claim a confident lie if not yet patched.

**Trigger events** that warrant an immediate update:
- New EU regulation affecting property (e.g., short-let, EPBD recast)
- National tax reform announcement
- ECJ ruling affecting visa / ownership programs
- User reports a broken URL or stale data
- Major real-estate market shift (>15 % YoY change)
- New mandatory diagnostic requirement
- Any new entry added to `regulatory-watch.md` with Tier 1 or Tier 2 impact

**Pair with `/schedule`** for automation:

```
/schedule weekly: /property-deep-dive --update --validate-only       # URL liveness
/schedule monthly: /property-deep-dive --health-report               # decay matrix
/schedule quarterly: /property-deep-dive --update --refresh-only     # data refresh
/schedule annually: /property-deep-dive --update                     # full re-research
```

## Country support matrix

**44 countries fully populated** as of 2026-04-26.

| ISO2 | Country | Status | Key data sources |
|---|---|---|---|
| **fr** | France | ✅ Fully populated | Géorisques, DICRIM, Sispea, IRSN, DRIAS, IAL, BRGM, Conseil Départemental |
| **it** | Italy | ✅ Fully populated | OMI Agenzia Entrate, IdroGEO ISPRA, INGV MPS04, ANAS, BDSR (CIN), ARERA ATID, ARPA |
| **cz** | Czech Republic | ✅ Fully populated | ČÚZK Nahlížení, Sreality cenová mapa, ČSÚ, ČHMÚ povodně, ČGS radon/sesuvy, ŘSD sčítání, eTurista |
| **sk** | Slovakia | ✅ Fully populated | ÚGKK ZBGIS/CICA/eSKN, Realitný barometer, NBS, SVP MPO/MPR, SHMÚ, ŠGÚDŠ radon, GFÚ SAV, SSC CSD2022 |
| **de** | Germany | ✅ Fully populated | BORIS-D, ImmoScout24, Destatis HPI, BfG Hochwasserportal, BfS Radon-Karte, BAFA/KfW, Grundsteuerreform 2025 |
| **at** | Austria | ✅ Fully populated | HORA, Statistik Austria HPI, OeNB Wohnimmobilien, AGES Radon, GeoSphere, Grundbuch, BEV |
| **ch** | Switzerland | ✅ Fully populated | swisstopo, Comparis, Homegate, Wüest Partner, Naturgefahrenkarte, SLF, swisseo, GEAK, Lex Koller — **Eigenmietwert abolition 2028** |
| **es** | Spain | ✅ Fully populated | Catastro, Idealista, INE IPHab, SNCZI flood, IGN seismic, CSN radon, **Cataluña ITP progressive 2025** |
| **pt** | Portugal | ✅ Fully populated | ePortugal, Idealista PT, INE IPHab, ANEPC, APA, IPMA, Confidencial Imobiliário SIR, **Lisbon AL suspended 2025** |
| **se** | Sweden | ✅ Fully populated | Lantmäteriet, Hemnet, Booli, SCB, MSB Översvämning, SGU radon, **fastighetsavgift cap 9,525 SEK** |
| **fi** | Finland | ✅ Fully populated | Maanmittauslaitos/KTJ, Etuovi, Oikotie, SYKE Tulvakartta, GTK/STUK radon, **varainsiirtovero 3% / 1.5% (2024 reform)** |
| **no** | Norway | ✅ Fully populated | Kartverket/Matrikkelen, Finn.no, Eiendom Norge, NVE/Skrednett, NGU/DSA radon, **dokumentavgift 2.5% (borettslag exempt), tilstandsrapport mandatory 2022** |
| **uk** | United Kingdom | ✅ Fully populated | Land Registry PPD, Rightmove, gov.uk Flood Map, Council Tax bands, UK Radon, BGS — **SDLT nil-rate £125k April 2025, FHL abolished April 2025, additional dwelling 5% surcharge Oct 2024** |
| **nl** | Netherlands | ✅ Fully populated | Kadaster, Funda, WOZ-waardeloket, Risicokaart, NDW, KNMI, Klimaateffectatlas — **Box 3 forfait 6% 2026, overdrachtsbelasting 10.4% second home, Wet werkelijk rendement 2028** |
| **be** | Belgium | ✅ Fully populated | STATBEL, Notaires.be, Immoweb, Geopunt VL, WalOnMap, BruGIS, OVAM — **Vlaanderen 2% + Wallonie 3% registratierechten primary residence Jan 2025, asbestattest mandatory Vlaanderen Nov 2022** |
| **dk** | Denmark | ✅ Fully populated | OIS, Boliga, Vurderingsstyrelsen, BBR, Tinglysning, DMI, Klimatilpasning, GEUS — **boligskat 2024 reform unified ejendomsværdiskat + grundskyld, 20% precautionary deduction** |
| **is** | Iceland | ✅ Fully populated | HMS Fasteignaskrá, Þjóðskrá, Veðurstofan IMO, Náttúruhamfaratryggingar, ÍSOR, Almannavarnir — **Reykjanes "New Reykjanes Fires" 9 eruptions since Dec 2023, Grindavík evacuated, NTÍ mandatory natural-hazard insurance** |
| **si** | Slovenia | ✅ Fully populated | GURS, Nepremicnine.net, ARSO, Atlas okolja, GeoZS, e-Sodstvo, ETN — **posplošena vrednost reform 13 May 2025, davek na nepremičnine 1.45% pending 2026** |
| **ie** | Ireland | ✅ Fully populated | Tailte Éireann, Property Price Register, Daft.ie, OPW Floodinfo, GSI radon, EPA, RTB — **LPT revaluation 1 Nov 2025, base rate 0.0906%, FHL abolished April 2025, DCBS mica/pyrite €420k cap** |
| **gr** | Greece | ✅ Fully populated | Ktimatologio, Bank of Greece RPPI, Spitogatos, EPPO/OASP seismic, HSGME, HL-NTWC tsunami, AADE — **VAT/CGT suspended 2026, ENFIA -20% insured residences, Athens STR freeze, Cyclades 30% bed cap, Golden Visa €800k/€400k tiers** |
| **pl** | Poland | ✅ Fully populated | EKW, Geoportal2, NBP BaRN, AMRON-SARFiN, Otodom, Wody Polskie ISOK, PAA radon, GIOŚ — **PoN 2025 budynek/budowla reform, PCC first-home exempt Aug 2023, Storm Boris 2024, Czyste Powietrze gas-boiler exit Mar 2025, eternit deadline 2032** |
| **ca** | Canada | ✅ Fully populated | CREA HPI, Realtor.ca/Centris, Teranet OnLand (ON) + LTSA+LOTR (BC) + SPIN2 (AB), Earthquakes Canada, Public Safety Canada — **UHT REPEALED Mar 2026, foreign buyer ban extended to 1 Jan 2027, BC SVT rates DOUBLED 2026, Toronto MLTT graduated tier 1 Apr 2026** |
| **au** | Australia | ✅ Fully populated | CoreLogic + ABS RPPI, realestate.com.au + Domain, state Land Titles Office (NSW LRS, VIC Landata, QLD Titles QLD), BoM, Geoscience Australia, FIRB — **foreign-buyer established-dwelling ban 1 Apr 2025–31 Mar 2027, foreign owner surcharges NSW 9%/VIC 8%/QLD 8%, VIC VRLT statewide Jan 2025 + Short-Stay Levy 7.5%, QLD Form 1 from 1 Aug 2025** |
| **nz** | New Zealand | ✅ Fully populated | LINZ Toitū Te Whenua, REINZ HPI + QV, Trade Me Property, GeoNet, GNS Science NSHM 2022, Toka Tū Ake (Natural Hazards Commission) — **bright-line 2-yr from 1 Jul 2024, interest deductibility 100% restored 1 Apr 2025, NHCover $300k+GST, NO stamp duty, foreign-buyer ban (AU+SG exempt)** |
| **ee** | Estonia | ✅ Fully populated | Maa-amet Geoportaal, e-Kinnistusraamat (RIK), KV.ee + City24, Statistikaamet, EGT (radon), e-Notar UNIQUE — **maamaks reform 2024-2026 (rates rising, no building tax — UNIQUE), VAT 22%→24% (Jan 2025), CGT 22% from 2025, STR registration mandatory Jul 2025** |
| **hr** | Croatia | ✅ Fully populated | OSS Uređena zemlja (cadastre + ZK), DGU Geoportal, Njuškalo, DZS + HNB, DHMZ CFFWIS, HGI-CGS, Seizmološka služba — **NEW Porez na nekretnine 2025 (€0.60–€8/m²), 2025 Hospitality Act 80% co-owner consent for STR, EUR since Jan 2023, Petrinja 2020 reconstruction ongoing** |
| **hu** | Hungary | ✅ Fully populated | Földhivatal Online + TAKARNET, KSH + MNB, Ingatlan.com, OVF flood, MBFSZ, OMSZ — **Otthon Start 3% mortgage from 1 Sep 2025, Terézváros (Budapest VI) STR ban from 1 Jan 2026, 5% VAT new homes extended to 2026, Földforgalmi törvény agri-land restrictions** |
| **mx** | Mexico | ✅ Fully populated | RPP per estado + Catastro municipal, Inmuebles24, SHF HPI, INEGI, RAN ejido, SSN/CENAPRED/CONAGUA — **Fideicomiso for foreigners in Restricted Zone (50km coast/100km border), Sheinbaum Vivienda 2025 INFONAVIT zero-interest 30yr, CDMX Airbnb Law Oct 2024, Quintana Roo RETUR-Q + 6% ISH** |
| **br** | Brazil | ✅ Fully populated | Cartórios + matrícula + CIB national rollout 2026, ZAP+VivaReal, FIPE-ZAP, BCB, CEMADEN, INMET — **Reforma Tributária 2026-2033 (CBS 2027 → IBS 2029), MCMV extension Apr 2026 (R$200B + R$13k income + R$600k cap + 35yr), STJ 2021 condomínio can ban STR, foreign rural caps Lei 5.709/1971** |
| **ar** | Argentina | ✅ Fully populated | Registro Propiedad provincial, Zonaprop + Argenprop + MercadoLibre, Reporte Inmobiliario, INPRES, AFIP — **DNU 70/2023 + Ley Bases 27.742 (rental liberalization PERMANENT), Bienes Personales reform Ley 27.743 (1.10%→0.50% schedule 2025-2027), Cepo cambiario partial lift Apr 2025, USD-denominated market** |
| **cr** | Costa Rica | ✅ Fully populated | Registro Nacional rnpdigital.com (UNIQUE strong digital), Encuentra24 + MLS Costa Rica, BCCR, OVSICORI + RSN, IMN — **Investor visa $200k → $150k (2025), No CGT for individuals (UNIQUE), Maritime Zone Law 6043 (50m public + 150m concession 51% Tico), 4 active volcanoes + Cocos subduction** |
| **pa** | Panama | ✅ Fully populated | Registro Público + ANATI, Encuentra24 + CompreoAlquile, INEC, SINAPROC + IMHPA — **USD economy, Territorial tax (no foreign-source income tax UNIQUE), Pensionado USD 1,000/mo (most generous LatAm), Friendly Nations Visa modified 2021 ($200k investment), 10-km border restriction CONSTITUTIONAL, Comarcas indígenas off-limits to foreigners** |
| **rs** | Serbia | ✅ Fully populated | RGZ + eKatastar, HaloOglasi + Nekretnine.rs, NBS price index, Seizmološki zavod — **Foreign-buyer reciprocity rules, 2014 Sava+Bosna floods, CGT 15% with 10-year exemption, EU candidate since 2012, Belgrade Waterfront mega-project** |
| **me** | Montenegro | ✅ Fully populated | UzN + eKatastar (gov.me/uzn), MONSTAT, Realitica, Seizmološki zavod CG — **EUR informally adopted 2002 (UNIQUE no central-bank issuance), Progressive RETT 3/5/6% since Jan 2024, CBI ABOLISHED Dec 2022, NEW Jan 2026 Investor Residency €150k, EU accession 2026-2028 target** |
| **ba** | Bosnia & Herzegovina | ✅ Fully populated | DUAL ENTITY: FBiH (katastar.ba) + RS-entity (RGURS rgurs.org) + Brčko, BAM-EUR peg 1.95583, Sarajevo + Banja Luka + Mostar — **17% VAT (lowest EU), 2024 FBiH first-time-buyer VAT refund 17% on 40 m², FBiH NO CGT individuals vs RS-entity 13%, RS-entity NO transfer tax (0%) vs FBiH 0.05-5%, BHMAC mine contamination (1992-95 war legacy)** |
| **mk** | North Macedonia | ✅ Fully populated | AKN cadastre, MAKSTAT + NBRSM, Reklama5 + Pazar3 + Skopjeshome, SUASZSM seismic — **MKD-EUR peg 61.5, 1963 Skopje M6.1 earthquake (1,070+ dead, Tange masterplan reconstruction), CGT 10% with 5-yr OR 3yr+1yr-resident exemption, NATO since 2020, Ohrid UNESCO**  |
| **al** | Albania | ✅ Fully populated | ASHK + e-Albania (service code 9473) + iKadaster (World Bank end-2026 target), INSTAT + BoA Fischer HPI, MerrJep, IGEWE — **2019 Durrës M6.4 earthquake (€985m losses), DIVA STR platform NEW 1 Jan 2026 (15% flat), Vlora Airport 2026, +18% YoY national, EU candidate since 2014, Title legalization risk for 1990s-2010s informal builds** |
| **lt** | Lithuania | ✅ Fully populated | Registrų centras (UNIFIED cadastre + land-book), Ober-Haus OHBI (Vilnius +10.7% YoY Dec 2025), Aruodas/Domoplius — **NO transfer tax (1.0-1.5% all-in), NTM 2026 reform progressive on non-main residences, 2-yr/10-yr CGT exemptions, Vilnius €2/night city tax (Feb 2024 first Baltic), BRELL grid exit Feb 2025** |
| **lv** | Latvia | ✅ Fully populated | VZD cadastre + Zemesgrāmata Land Book (SEPARATE), CSP HPI Q4 2025: 224.02 (+8.4% YoY), SS.lv #1 — **Stamp duty 1.5%/2% cap €50k, NĪN frozen 2012-13 fiscal value, 2026 PIT 25.5%/33%, capital gains to 25.5% (was 20%), compulsory land lease (dalītais īpašums) Riga gotcha, RU/BY purchase ban (post-2022)** |
| **ro** | Romania | ✅ Fully populated | ANCPI eTerra3 + myeTerra (ROeID auth), INS HPI 168.99 Q4 2025, Imobiliare.ro Bucharest €2,204/m² — **VAT 19→21% (1 Aug 2025), local property tax baseline +167% (1 Jan 2026), CGT 1%/3% by holding (no primary-res exemption), AMCCRS Bucharest Rs I/II/III/IV seismic class (~350 Rs I), Termoenergetica (was RADET) DH crisis, Schengen full integration 1 Jan 2025** |
| **bg** | Bulgaria | ✅ Fully populated | AGCC KAIS cadastre + Registry Agency (SEPARATE), NSI HPI 256.71 Q4 2025, Imot.bg #1 — **Eurozone since 1 Jan 2026 at 1.95583 BGN/EUR, CGT 10% with 3yr/5yr exemptions (residents/EU/EEA only), VAT 20% no reduced rate housing, non-EU cannot own ANY land (EOOD workaround), Toplofikatsiya Sofia in active financial crisis, 2024 worst-recorded wildfire year (~600 fires)** |
| **lu** | Luxembourg | ✅ Fully populated | ACT cadastre + AED Bureaux des hypothèques (SPLIT), STATEC apt €8,094/m² Q1 2025 (+3.7% YoY), athome.lu — **Bëllegen Akt €40k credit per person PERMANENT (1 Jul 2025), 7% transfer tax standard, CGT 2-yr speculative + half-rate post-2yr (NOT 10-yr French rule), VAT 3% super-reduced (€50k cap, ≤400m²), IFON property-tax revaluation phased 2026/2030/2028, Esch-Belval CASIPO contamination zones** |
| **cy** | Cyprus | ✅ Fully populated | DLS portal RoC + ETEK seismic, CBC RPPI Q4 2025 +7.1% YoY house, Limassol apt 150.1 — **2026 Comprehensive Tax Reform (stamp duty largely abolished, CGT exemptions raised €17,086→€30,000 + €85,430→€150,000, SDC rental abolished), VAT 5% reduced to first 130m²/€350k cap (190m²/€475k cliff), Trapped Buyers Amendment Law 110(I)/2025, 2025 worst drought since 1901 (reservoirs 21.7%), TRNC north title risk** |
| **mt** | Malta | ✅ Fully populated | LRA hybrid (Public Registry deeds 1863 + Land Registry title 1982), NSO RPPI 177.36 Q4 2025 (+6.1% YoY), Frank Salt + djar.ai aggregator — **MEIN ECJ ruling 29 Apr 2025 (Case C-181/23 ENDED), MPRP residency continues, NO annual property tax + NO VAT residential UNIQUE, FTB 0% stamp duty first €200k, UCA/vacant 0% on first €750k (Jan 2025–Dec 2026), AIP permit + minimum thresholds €143k apt/€247k other, LRA 2025-2035 reform target full compulsory registration by 2035** |

A country playbook is "scaffolded" when it has the structure but data sources need filling. As of 2026-04-26, all 44 supported countries are fully populated. Master skill still detects scaffold status (for any future additions) and either (a) runs best-effort with placeholder warnings, or (b) tells the user the country is not yet fully supported and offers to populate it.

## Unsupported country

If a user passes an address from a country with no `countries/<iso2>/playbook.md`:
1. Tell them which countries are supported.
2. Offer to populate that country's playbook (it's a one-time investment for ~30 min of research; the structure is reusable).
3. As fallback, do a best-effort run using the **universal sections framework** in `shared/sections.md` and OpenStreetMap-only data — but warn the output is shallow.

## Universal section concepts

All countries' playbooks must implement the same twenty-two section interfaces, even if the underlying data sources differ. See `shared/sections.md` for the universal contract each section must satisfy.

**Fifteen sections are fully universal** (no country-specific implementation required):

Core data (3):
- `--amenities` → `shared/amenities-osm.md`
- `--climate` → `shared/climate-projections.md`
- `--crime` → `shared/crime-sources.md` (44-country registry)

Financial/process (5):
- `--finance` → `shared/finance.md`
- `--currency` → `shared/currency.md`
- `--visa` → `shared/visa-programs.md`
- `--insurance` → `shared/insurance.md`
- `--notary` → `shared/notary-process.md`

Decision-context (7):
- `--compare=<iso2,...>` → `shared/compare.md`
- `--retirement` → `shared/retirement.md`
- `--digital-nomad` → `shared/digital-nomad.md`
- `--macro` → `shared/macro.md`
- `--demographics` → `shared/demographics.md`
- `--esg` → `shared/esg.md`
- `--exit` → `shared/exit.md`

Cross-cutting layers (`--integrity`, `--journey=<type>`, `--type=<kind>`) overlay decision-shaped outputs on top of the standard sections.

## Output format

See `shared/output-template.md` for the canonical MD structure. Key elements:
- Frontmatter: address, date, listing URL, coordinates, admin context
- One section per `## H2` heading
- TL;DR at the end with top 3 findings (🟢 / 🟡 / 🟠 / 🔴)
- Sources block with all referenced URLs
- "Verify before signing" footer

## 🔒 Anti-hallucination guard (read before every run)

**This skill is non-negotiable about source-honesty.** Property due-diligence drives six- to seven-figure decisions; a fabricated tax rate or risk classification can mislead a buyer into real losses.

**The full guard is in `shared/anti-hallucination.md` and is mandatory reading.** Key non-negotiables:

1. **Source-tag every numeric claim** — inline citation, computation trace, or `est.` label. No naked numbers.
2. **Source ranking** — Primary government > Primary regulated > Secondary aggregator > Listing > Forum > Model inference. Never silently upgrade.
3. **Empty data ≠ guess** — when a source returns nothing, output `data not publicly available — verify at <authoritative source>` rather than fabricate.
4. **Commune-level ≠ parcel-level** — verbs must match the source's granularity. Many FR/EU sources are commune-level; do not silently elevate to parcel-level.
5. **Listing data is seller-controlled** — every field from a listing platform must be tagged `(per listing — verify with cadastre / on visit)`.
6. **Date stamps mandatory** — every external data point gets an "as of" date. Data >12 months old gets `— rates/figures may have changed`.
7. **Confidence label per section** — HIGH (2+ primary, <12mo, parcel-level) / MEDIUM (1 primary or 2 secondary, 12–36mo, locality) / LOW (computed only, >36mo, contradictory).
8. **Contradiction surfacing** — when sources disagree, name both with dates and explain the gap. Never silently pick one.
9. **TL;DR anchoring** — every TL;DR bullet must trace to a sourced claim earlier in the body.
10. **Forbidden phrasings** — no "approximately", "in the area of", "industry average", "experts say", "should be around" without sourced replacement.

The validation gate (step 7 of the master flow) **WILL** block output containing un-sourced numerics, fabricated cells, or unanchored TL;DR claims. This is enforcement, not advice.

## Quality bar (universal — additive to anti-hallucination guard)

- **Every numerical claim has a source** (URL, document name, or transparent computation)
- **Distinguish measured from estimated** — say `est.` when extrapolating
- **State confidence** per section — HIGH / MEDIUM / LOW with one-sentence justification
- **Don't fabricate** — if a data source returns nothing, say "data not publicly available; verify at <authoritative source>"
- **Always include a verification path** — what the user must do (call mairie/Bürgeramt/council, request seller diagnostics, etc.)
- **End each section with a one-line takeaway**
- **Append the verification footer** (mandatory, non-removable) — see `shared/anti-hallucination.md`

## Verdict bands (universal)

🟢 green — non-issue / actively positive
🟡 yellow — minor concern, watch
🟠 orange — meaningful issue, plan / budget
🔴 red — significant issue, action required before purchase

Always justify the colour with one sentence.

## Examples

```
/property-deep-dive 1 Rue Principale, 86430 Adriers
→ detects FR by postcode, runs --all, prints to terminal

/property-deep-dive --country=de Friedrichstraße 100, 10117 Berlin --save
→ Germany playbook, all sections, save to _local/reports/

/property-deep-dive https://www.rightmove.co.uk/properties/142857 --tax --risks
→ detects UK from URL, only tax + risks sections

/property-deep-dive Adriers 86430 --work=violinist --quick
→ FR, work-options only, quick mode

/property-deep-dive Calle Mayor 5, 28013 Madrid --country=es --all --save=madrid.md
→ Spain, all 10 sections, save to specific file

/property-deep-dive 1 Rue Principale, 86430 Adriers --journey=pre-offer
→ FR pre-offer brief: walkaway price + top 3 risks + hidden costs

/property-deep-dive Plaka 10556 Athens --integrity --type=heritage --journey=foreign-buyer
→ GR heritage property, full integrity scan + foreign-buyer journey + heritage-specific checks

/property-deep-dive <off-plan url> --type=off-plan --integrity --journey=foreign-buyer
→ Developer due diligence + integrity scan + foreign-buyer brief

/property-deep-dive <auction listing> --type=auction --integrity --journey=pre-offer --quick
→ Compressed-timeline auction prep: legal pack scan + bidding ceiling + red flags
```

## File map

```
property-deep-dive/
├── SKILL.md                   # this file (master router)
├── countries/                 # 44 countries, all fully populated as of 2026-04-26
│   ├── fr/playbook.md         # France
│   ├── it/playbook.md         # Italy
│   ├── cz/playbook.md         # Czech Republic
│   ├── sk/playbook.md         # Slovakia
│   ├── de/playbook.md         # Germany — Grundsteuerreform 2025
│   ├── at/playbook.md         # Austria
│   ├── ch/playbook.md         # Switzerland — Eigenmietwert abolition 2028
│   ├── es/playbook.md         # Spain — Cataluña ITP 2025
│   ├── pt/playbook.md         # Portugal — Lisbon AL suspended 2025
│   ├── se/playbook.md         # Sweden
│   ├── fi/playbook.md         # Finland — varainsiirtovero 2024 reform
│   ├── no/playbook.md         # Norway — tilstandsrapport mandatory 2022
│   ├── uk/playbook.md         # United Kingdom — SDLT/FHL April 2025
│   ├── nl/playbook.md         # Netherlands — Box 3 reform
│   ├── be/playbook.md         # Belgium — Vlaanderen/Wallonie transfer tax 2025
│   ├── dk/playbook.md         # Denmark — boligskat 2024 reform
│   ├── is/playbook.md         # Iceland — Reykjanes volcanic series
│   ├── si/playbook.md         # Slovenia — posplošena vrednost 2025
│   ├── ie/playbook.md         # Ireland — LPT revaluation 2026
│   ├── gr/playbook.md         # Greece — STR Athens freeze, Golden Visa €800k/€400k
│   ├── pl/playbook.md         # Poland — PoN 2025 reform, Storm Boris 2024
│   ├── ca/playbook.md         # Canada — UHT repealed Mar 2026, foreign buyer ban to 2027
│   ├── au/playbook.md         # Australia — FIRB established-dwelling ban Apr 2025–Mar 2027
│   ├── nz/playbook.md         # New Zealand — bright-line 2yr Jul 2024, NO stamp duty
│   ├── ee/playbook.md         # Estonia — e-Notar UNIQUE, no building tax, maamaks reform
│   ├── hr/playbook.md         # Croatia — Porez na nekretnine 2025 NEW, EUR since Jan 2023
│   ├── hu/playbook.md         # Hungary — Otthon Start Sep 2025, Terézváros STR ban Jan 2026
│   ├── mx/playbook.md         # Mexico — Fideicomiso Restricted Zone, Sheinbaum Vivienda 2025
│   ├── br/playbook.md         # Brazil — Reforma Tributária 2027-2033, MCMV ext Apr 2026, CIB rollout
│   ├── ar/playbook.md         # Argentina — DNU 70+Ley Bases (rental liberalization), Bienes Personales reform
│   ├── cr/playbook.md         # Costa Rica — Investor visa $150k 2025, No CGT individuals UNIQUE
│   ├── pa/playbook.md         # Panama — USD economy, Territorial tax UNIQUE, Pensionado $1,000/mo
│   ├── rs/playbook.md         # Serbia — RGZ + eKatastar, EU candidate, 10yr CGT exemption
│   ├── me/playbook.md         # Montenegro — EUR informally 2002, RETT 3/5/6% Jan 2024, NEW investor residency 2026
│   ├── ba/playbook.md         # Bosnia & Herzegovina — DUAL ENTITY (FBiH/RS-entity), BAM-EUR peg, BHMAC mines
│   ├── mk/playbook.md         # North Macedonia — AKN cadastre, 1963 Skopje quake legacy, MKD-EUR peg
│   ├── al/playbook.md         # Albania — ASHK + iKadaster, 2019 Durrës quake, DIVA STR Jan 2026, Vlora airport
│   ├── lt/playbook.md         # 🆕 Lithuania — UNIFIED cadastre, NO transfer tax, NTM 2026 progressive, Vilnius €2/night
│   ├── lv/playbook.md         # 🆕 Latvia — Cadastre + Land Book SEPARATE, compulsory land lease quirk, RU/BY purchase ban
│   ├── ro/playbook.md         # 🆕 Romania — VAT 19→21% (Aug 2025), AMCCRS Bucharest seismic class, Termoenergetica DH crisis
│   ├── bg/playbook.md         # 🆕 Bulgaria — Eurozone since 1 Jan 2026, KAIS cadastre, Toplofikatsiya Sofia crisis, 2024 worst wildfire year
│   ├── lu/playbook.md         # 🆕 Luxembourg — Bëllegen Akt €40k permanent, 7% transfer tax, IFON 2030 reform, Esch-Belval contamination
│   ├── cy/playbook.md         # 🆕 Cyprus — 2026 Tax Reform (CGT exemptions raised, stamp duty abolished), TRNC title risk, 2025 worst drought since 1901
│   └── mt/playbook.md         # 🆕 Malta — MEIN ECJ ENDED Apr 2025, NO annual property tax + NO VAT residential, AIP permit, LRA 2025-2035 reform
└── shared/
    ├── preflight.md             # universal pre-flight steps (geocode, road, listing)
    ├── sections.md              # universal contract for each of the 15 sections
    ├── output-template.md       # MD report template
    ├── verdict-bands.md         # 🟢🟡🟠🔴 conventions
    ├── anti-hallucination.md    # 🔒 mandatory: source-honesty rules + 7-check validator gate
    ├── updater.md               # 🔧 maintenance mode: --update flag, URL validation, scaffold population
    ├── amenities-osm.md         # universal OSM Overpass patterns for --amenities (works in every country)
    ├── crime-sources.md         # per-country crime data source registry for --crime (44 countries)
    ├── climate-projections.md   # universal --climate section: Copernicus + IPCC AR6 + Climate Central
    ├── integrity-checks.md      # --integrity layer: dispute resolver + photo OCR + cadastre cross-check + red-flag scanner
    ├── journeys.md              # --journey=<type> templates
    ├── property-types.md        # --type=<kind> specialized
    ├── finance.md               # 🆕 universal --finance: foreign-buyer mortgages across 44 countries
    ├── currency.md              # 🆕 universal --currency: peg / FX / capital controls
    ├── visa-programs.md         # 🆕 universal --visa: RBI / CBI / golden-visa current status (Apr 2026)
    ├── insurance.md             # 🆕 universal --insurance: cat-risk schemes + flood/EQ + climate reforms
    ├── notary-process.md        # universal --notary: notary vs solicitor + closing costs + timeline
    ├── compare.md               # 🆕 universal --compare: side-by-side multi-country mode
    ├── retirement.md            # 🆕 universal --retirement: pension tax + healthcare + climate + expat
    ├── digital-nomad.md         # 🆕 universal --digital-nomad: DNV + internet + coworking + TZ
    ├── macro.md                 # 🆕 universal --macro: inflation + GDP + central bank + sovereign yield
    ├── demographics.md          # 🆕 universal --demographics: pop + aging + schools + family-friendly
    ├── esg.md                   # 🆕 universal --esg: EPC distribution + climate exposure + carbon levy
    ├── exit.md                  # 🆕 universal --exit: DOM + commission + sell-side closing
    ├── price-index-feeds.md     # tooling: per-country HPI source registry for --update --refresh-only
    ├── listing-aggregators.md   # tooling: per-country listing portal API/scraping status
    ├── photo-ocr.md             # tooling: operational photo-OCR pipeline
    ├── tco-calculator.md        # 🆕 tooling: 30-yr TCO calculator (bridges tax/finance/insurance/notary)
    ├── mortgage-calculator.md   # 🆕 tooling: monthly P&I + amortization + stress-test
    ├── test-fixtures.md         # 🆕 tooling: 1 known-good listing per country (44 fixtures) for self-test
    ├── listing-diff-watcher.md  # 🆕 tooling: track price drops / status changes on watched URLs
    ├── comparable-transactions.md  # 🆕 tooling: per-country sold-price (transaction) source registry
    └── auto-validate.md         # 🆕 tooling: per-country pass/fail tracking + scheduled cron pattern
```

## Final step (always)

After completing the run, optionally offer:

> *Want me to `/schedule` an agent in 6 months to re-poll <specific changing data> (e.g., commune €/m², occupancy stats, new ICPE filings) and flag changes?*

Skip the offer for single-section runs or `--quick` mode.
