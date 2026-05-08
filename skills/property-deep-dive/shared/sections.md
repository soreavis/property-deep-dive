# Universal Section Contract

Every country playbook implements these ten core + one regulatory sections with a consistent interface. The data sources differ; the interface and output structure don't.

Three core sections are **fully universal** (no country-specific implementation needed):
- `--amenities` (OSM Overpass — see `shared/amenities-osm.md`)
- `--climate` (Copernicus + IPCC — see `shared/climate-projections.md`)
- `--crime` (universal output, country-specific URLs — see `shared/crime-sources.md`)

The regulatory and transaction-buyer sections are also **fully universal** (single canonical doc with regional patterns + per-country tables):
- `--permits` (building-works permit thresholds, heritage overlays, conformity-at-completion — see `shared/permits.md`)
- `--agent` (buyer-side agency landscape: commission, licensing, MLS, dual-agency, EBA — see `shared/agent.md`)
- `--scams` (country-specific transaction-fraud register: BEC, deed forgery, off-plan disappearance, nominee structures, golden-visa price-inflation — see `shared/scams.md`)
- `--language` (foreign-buyer deed-language rule + sworn-translator mandate + Hague Apostille / POA chain + diagnostic-doc language + sworn-translation cost bands — see `shared/language.md`)

## Section: `--price`

**Goal**: Is the asking price fair vs the local market?

**Interface contract** — country playbook must provide:
- 1+ data source for local €/m² (or local currency/m²) average
- Range of prices for the locality (min/max)
- Trend indicator if available (up / flat / down over recent years)
- Method to find 3–5 comparable listings on the same locality
- Confidence note (high/medium/low — based on transaction sample)

**Output structure**:
```markdown
## Price Assessment

**Listing**: <price> (<currency>), <surface>, built <year> → **<price/area>**
**Local average**: <avg> (<range>) per <unit>, source: <source>
**Position**: <%> below/above average — **Verdict**: bargain | fair | aggressive | overpriced

| Comp | Surface | Price/area | Condition |
|---|---|---|---|

**Confidence**: <high/medium/low>
**Walk-away price**: <amount> if inspection reveals significant work
```

---

## Section: `--traffic`

**Goal**: How busy is the road? Noise/safety implications?

**Interface contract**:
- Method to identify the road's official designation (D-road, B-Straße, A-road, etc.)
- 1+ official traffic count source (national/regional government)
- Fallback: OSM `highway` class → coarse band

**Output structure**:
```markdown
## Traffic Profile

**Road**: <name> (<class>: <ref>, <highway>, maxspeed <maxspeed>)

| Road | Where | TMJA / AADT / DTV | % heavy vehicles |
|---|---|---:|---:|

**This property's road**: ~<X> v/d (estimated/measured)
- ≈ <Y> cars/hour daylight
- ≈ <Z> cars/hour at night

**Comparison**: <relative to nearby roads or country averages>

**Noise verdict**: 🟢 silent / 🟡 light / 🟠 audible / 🔴 nuisance
```

Country-specific data terms:
- **FR**: TMJA (Trafic Moyen Journalier Annuel) — Conseil Départemental
- **DE**: DTV (Durchschnittlicher täglicher Verkehr) — Bundesländer
- **UK**: AADT — Department for Transport
- **IT**: TGM (Traffico Giornaliero Medio) — ANAS / Regione
- **ES**: IMD (Intensidad Media Diaria) — Ministerio de Transportes / CCAA

---

## Section: `--tax`

**Goal**: Annual property tax + one-time purchase costs

**Interface contract**:
- Communal/local tax rate(s) for residential property
- Transaction tax rate (stamp duty / DMTO / Grunderwerbsteuer / IBI / etc.)
- Notary/legal fee structure
- Future revaluation/reform risk if any

**Output structure**:
```markdown
## Tax Estimate

**Local rates**: <table of rates>
**Estimated assessment base**: <local taxable value formula>

| Scenario | Annual tax |
|---|---:|
| Primary residence | <range> |
| Secondary residence | <range> |

**One-time at purchase**: ≈ <amount> in transaction taxes + legal fees

**Future risk**: <upcoming reform impact>

⚠️ Verification: request seller's last property tax bill.
```

Country-specific tax terms:
- **FR**: Taxe foncière, Taxe d'habitation RS, frais de notaire, DMTO 5.81%
- **DE**: Grundsteuer (post-2025 reform), Grunderwerbsteuer (3.5–6.5%), Notarkosten 1.5–2%
- **UK**: Council Tax band, Stamp Duty Land Tax (SDLT), legal fees ~£1–2k
- **IT**: IMU (seconda casa), TASI, imposta di registro 2–9%
- **ES**: IBI, ITP/AJD 6–11%, notario+registro 1–2.5%
- **NL**: OZB (gemeentelijk), overdrachtsbelasting 2–10.4%
- **BE**: Précompte immobilier, droits d'enregistrement 6–12.5%
- **CH**: Impôt foncier (cantonal), valeur locative imputed
- **AT**: Grundsteuer, Grunderwerbsteuer 3.5%
- **PT**: IMI, IMT progressive

---

## Section: `--rental`

**Goal**: Realistic short-let / vacation rental income + tax-optimised net

**Interface contract**:
- Local existing competition (3–8 nearest comparable units)
- Country-typical occupancy rates (rural / urban / coastal)
- Country tax regime for short lets (with thresholds and abatements)
- Classification benefits if any (e.g., FR meublé classé, IT CIR, ES VTV)

**Output structure**:
```markdown
## Rental Income Analysis

**Existing competition** (locality): <N> short-lets

| Unit | Sleeps | Weekly tariff |
|---|---:|---:|

### Realistic configurations

| Option | Year-3 gross | Net (low tax bracket) | Net (high tax bracket) |
|---|---:|---:|---:|

### Tax regime
- **Best regime**: <name + decision>
- Thresholds: <country-specific>
- Special status to claim: <e.g. classement, CIR, VTV>

### Strategic notes
- <pool / view / wifi differentiators>
- <regulatory traps: zone tendue, mandatory registration>
```

Country-specific regimes:
- **FR**: Micro-BIC classé/non-classé, URSSAF 6%/21.2%, plafonds 15k/83.6k
- **DE**: Vermietung & Verpachtung Einkommensteuer; commercial threshold; gewerbesteuer if hotel-style
- **UK**: Furnished Holiday Let (FHL) rules + new abolition 2025; income tax + property income allowance £1,000
- **IT**: Cedolare secca 21% short-let; CIR registration mandatory
- **ES**: VTV/VFT regional license; IRNR 19/24% for non-residents
- **NL**: Box 3 imputed; B&B regulated by gemeente
- **BE**: Régional licence (Brussels strict, Wallonia/Flanders moderate); IPP barème
- **CH**: Cantonal patente; valeur locative impacts taxe
- **AT**: Gewerbeschein if professional; ESt-Pauschalierung option
- **PT**: AL (Alojamento Local) registration; IRS Cat. F or B

---

## Section: `--work=<profession>`

**Goal**: Can the user earn a living locally with their profession?

**Interface contract**:
- Catchment population within 30 / 60 minute drive
- Country-specific employment platforms (Pôle Emploi, Bundesagentur, Job Centre Plus, etc.)
- Profession-specific licensing/certification requirements
- Country self-employment regime options (auto-entrepreneur, Kleinunternehmer, sole trader, autónomo, partita IVA, ZZP, etc.)

**Output structure**:
```markdown
## Local Work Options for <Profession>

### Catchment
| Place | Distance | Population | Notes |
|---|---|---:|---|

### Competition
| Player | Offer | Pricing |
|---|---|---:|

### Revenue options ranked
1. <Salaried at local institution>
2. <Independent>
3. <Online/hybrid>

### Legal status
| Status | When | Tax | Social charges |
|---|---|---|---|

### Realistic year-3 net
| Scenario | Net annual |
|---|---:|

### How to build it in 12 months
1. Month 0–1: ...
2. Month 1–2: ...
```

---

## Section: `--risks`

**Goal**: Every officially declared + climate + property-specific risk

**Interface contract**:
- 1+ official risk register (DICRIM / Hochwasserkarte / Risk register / Carta del Rischio)
- Address-level risk lookup if available (ERRIAL / equivalent)
- Climate projections to 2050 (DRIAS or country equivalent)
- Build-year hazards based on national construction-era patterns
- Mandatory diagnostics matrix at sale

**Output structure**:
```markdown
## Risk Map

### Officially declared
| Risk | Severity | Specific to property |
|---|---|---|

### High-attention items
🔴 **<Risk 1>** — explanation, mitigation cost, action
🟠 **<Risk 2>** — ...
🟡 **<Risk 3>** — ...

### Climate to 2050
- <temp change>
- <drought / flood / wildfire trends>

### Build-era mandatory diagnostics
| Diagnostic | Required because | Validity |
|---|---|---|

### Risk dashboard
| Class | Severity | Action priority |
|---|---|---|

### Pre-purchase checklist
1. ...
2. ...
```

---

## Section: `--mains`

**Goal**: Is the property on mains drains/sewer? Cost implications.

**Interface contract**:
- 1+ national/regional registry confirming sewer service exists for the locality
- Method to identify likely connection status (zoning plan / cadastre overlay / listing language)
- Verification path (which authority to call)
- Cost ranges for both connected and non-connected scenarios

**Output structure**:
```markdown
## Mains Drains Verification

### What the records confirm
- Locality has collective sewer: yes/no
- Operator: <name>
- Property location: bourg / outlying / hamlet / urban core

### Likely connection status
**Probability connected**: <%>

### Why probably yes
- <signal 1>

### Why uncertain
- <gap 1>

### Verification path (must do)
1. Call <authority>: <phone>
2. Ask: <country-specific question>
3. Request from seller: <country-specific document>

### Cost implications
| Scenario | Cost |
|---|---:|
| On collective, conform | <annual fee> |
| On collective, non-conform | <upgrade cost> |
| Outside collective, septic | <full system cost> |
```

Country-specific authorities:
- **FR**: Mairie / SPANC (commune-level)
- **DE**: Stadtwerke / Abwasserzweckverband
- **UK**: Water company (Thames Water / Severn Trent / etc.)
- **IT**: Comune / gestore idrico
- **ES**: Ayuntamiento / mancomunidad
- **NL**: Gemeente / waterschap
- **BE**: Commune / société wallonne/flamande des eaux
- **CH**: Commune / SIG / IWB
- **AT**: Gemeinde / Verband
- **PT**: Câmara Municipal / Águas de Portugal

---

## Section: `--crime`

**Goal**: Commune-level crime rate + national/regional comparison + trend.

**Universal contract**:
- Use the **per-country crime data source registry** in `shared/crime-sources.md`
- Pull latest year published by national police statistics or stat office
- Compute rate per 1,000 (or 100k) inhabitants
- Compare vs national + regional average
- Note 5-year trend if available
- Surface methodology breaks (e.g., FR CSI 2022, DE PKS revision)

**Output structure** (full template in `shared/crime-sources.md`):
```markdown
## Crime & Safety

**Locality**: <name>, <region>
**Population**: <pop>
**Data year**: <YYYY> (latest)
**Source**: <national police / stat office>

| Metric | Locality | National | Regional | 5-yr trend |
|---|---:|---:|---:|---|

### Verdict
🟢/🟡/🟠/🔴 — one-line justification

### Walking-around safety
<one-line qualitative note>

### Confidence
<HIGH/MEDIUM/LOW> — <reason>
```

**Verdict bands**:
- 🟢 < 50 % national average across all categories
- 🟡 50–110 % of national average
- 🟠 110–200 % for one+ category
- 🔴 > 200 % national average; multiple categories elevated

**Caveats to surface every time**:
- Recorded vs actual (under-reporting varies)
- Tourist destinations have inflated rates (transient population)
- Small communes: absolute numbers volatile; statistical noise
- Methodology changes: 2022-2023 reforms (esp. FR CSI, DE PKS) make 5-year comparisons tricky

---

## Section: `--amenities`

**Goal**: Distance to nearest essential services from the property.

**Universal logic** (works in every country): full OSM Overpass query patterns in `shared/amenities-osm.md`.

**What to look up** (single combined Overpass call):
- Supermarket / grocery (`shop=supermarket|convenience|grocery`)
- DIY / hardware / brico (`shop=hardware|doityourself|trade|garden_centre`)
- Pharmacy (`amenity=pharmacy`)
- General Practitioner (`amenity=doctors`, `healthcare=doctor|general_practitioner`)
- Hospital (`amenity=hospital`)
- Schools (`amenity=school|kindergarten`)
- Public transport (bus, train, tram, metro)

**Compute per amenity**:
- Closest by Haversine distance
- Walking time @ 5 km/hr
- Driving time @ 25/50/80 km/hr (urban / rural / motorway)

**Output structure**:
```markdown
## Local Amenities

| Service | Closest | Distance | Walk | Drive |
|---|---|---:|---:|---:|
| Supermarket | <name> | <km> | <min> | <min> |
| DIY / hardware | <name> | <km> | <min> | <min> |
| Pharmacy | <name> | <km> | <min> | <min> |
| General Practitioner | <name> | <km> | <min> | <min> |
| Hospital | <name> | <km> | <min> | <min> |
| Primary school | <name> | <km> | <min> | <min> |
| Bus stop | <name> | <km> | <min> | — |
| Train station | <name> | <km> | <min> | <min> |

### Verdict
🟢/🟡/🟠/🔴 — convenience band

### Walkability score
<X / 10>

### Medical access
🟢/🟡/🟠/🔴 — <one-line>

⚠️ OSM caveat: cross-check rural results via Google Maps before signing.
```

**Verdict bands**:
- 🟢 < 1 km / < 12 min walk: convenient urban
- 🟡 1–3 km / 12–36 min walk: suburban
- 🟠 3–10 km: transport-dependent
- 🔴 > 10 km: very rural; bulk-shopping concerns; medical access flag

**Country-specific quirks** (full table in `shared/amenities-osm.md`):
- DE: `shop=chemist` (Drogerie like dm/Rossmann) is NOT a pharmacy
- IT: tabacchi sometimes function as mini-marts
- FR: tabacs double as small convenience
- Each country has dominant brand chains worth recognizing

---

## Section: `--permits`

**Goal**: Can the buyer legally do the works the listing implies? What unauthorised works might already exist? What is the post-purchase enforcement risk?

**Universal logic** (works in every country): full implementation in `shared/permits.md`. Single canonical doc with regional patterns + per-country tables for all 103 supported countries — country playbook does NOT need a separate permits section.

**Disambiguation**: `--permits` ≠ `--work=<profession>`. The latter is local employment for a profession at the address. The former is permits for **building works** on the property.

**What to look up** (universal):
- Permit hierarchy: which works require nothing / declaration / full permit (country-specific 2-tier or 3-tier system)
- Numeric thresholds (m² creation, m² extension, height, façade modification) where statute defines them
- Listed-building / heritage overlay (separate parallel consent regime)
- Indicative timeline (declaration vs full permit, weeks/months)
- Conformity certificate at completion (DAACT FR / SCAGI IT / licencia de primera ocupación ES / autorização de utilização PT / Schlussabnahme DE / etc.)
- Retention / amnesty / regularization path for unauthorised existing works
- Post-purchase enforcement risk (limitation period for prior-owner unauthorised works)

**Output structure** (full template in `shared/permits.md`):
```markdown
## Permits & Building-Works Regime

**Country**: <ISO2>
**Permit hierarchy**: <none → declaration → full permit>
**Key thresholds**: <new build / extension / façade / internal-only / demolition / pool>
**Heritage overlay**: <authority + separate consent>
**Timeline (typical)**: declaration <weeks>; full permit <weeks/months>
**Conformity at completion**: <required / optional / not used>
**Retention / amnesty path**: <country-specific>
**Post-purchase enforcement risk**: <limitation period>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/permits.md`):
- The "tolerated" extension trap — passage of time does NOT legalise unauthorised structures in most civil-law jurisdictions
- Heritage overlay invisibility — Listed Buildings (UK), Monuments Historiques + ABF (FR), vincolo paesaggistico (IT), BIC (ES), Denkmalschutz (DE/AT) often unsignaled in listings
- Conformity-at-completion gap — properties sold without DAACT / agibilità / licencia de primera ocupación carry hidden time bombs
- Amnesty / condono windows close — historic regularization paths are rarely re-opened

---

## Section: `--scams`

**Goal**: Country-specific transaction-fraud register — what documented buyer-side scams target this country's market in 2024-2026, with regulator advisories, prosecutions, or investigative-journalism evidence.

**Universal logic** (works in every country): full implementation in `shared/scams.md`. Single canonical doc with 7 cross-cutting traps + regional patterns + per-country one-liners for all 103 supported countries — country playbook does NOT need a separate scams section.

**Disambiguation**: `--scams` ≠ `--integrity` ≠ `--risks`. `--scams` = country-specific **transaction-fraud** patterns targeting buyers (deed forgery, wire fraud, off-plan disappearance, nominee structures, golden-visa inflation). `--integrity` = data-honesty checks on the listing/cadastre output itself. `--risks` = natural + technological hazards.

**What to look up** (universal):
- Top 3-5 scam patterns documented for the country in 2022-2026
- Per pattern: scheme name (with native term), mechanism, victim profile, documented evidence (regulator advisory / prosecution / embassy / investigative-journalism URL), mitigation (which authority/registry to verify with)
- Confidence per pattern: HIGH (regulator advisory + prosecution) / MEDIUM (multi-source forum + practitioner) / LOW (anecdotal)

**Output structure** (full template in `shared/scams.md`):
```markdown
## Transaction Fraud Register

**Country**: <ISO2>
**Headline patterns** (top 3-5 by buyer-loss evidence):

### <Scheme name>
**Mechanism**: <one sentence>
**Victim profile**: <demographic>
**Evidence**: <regulator URL / prosecution case>
**Mitigation**: <verification path>
**Confidence**: <HIGH/MEDIUM/LOW>

### Universal mitigations
1. Voice-verify wire instructions on independently-sourced number
2. Pull cadastre/registry document yourself the day of signing
3. Engage independent buyer's lawyer (not seller's)
4. Verify agent license at country's registry
5. For foreign-restricted zones: pre-clear eligibility before signing
```

**Cross-cutting traps to surface every time** (from `shared/scams.md`):
- Wire-fraud at closing (BEC) — biggest by $ volume universally; voice-verify IBAN on independently-sourced number
- Title fraud / deed forgery / impersonated owner — UK HMLR Property Alert + ON LTAF backstop are the model defenses
- Off-plan developer disappearance — bank-guaranteed escrow only; existing-stock preference for non-residents
- Foreign-restricted-zone confusion / nominee structure — illegal in TH/ID/MX/MA/KW; courts unwind consistently
- Golden-visa / RBI price-inflation — independent statutory-licensed appraisal; ENDED programs cannot be "still available"
- Customary-tenure / restitution-lien — chain-of-title back to pre-disruption baseline (PL 1939, RO 1947/1989, BA pre-conflict)
- Concession-vs-freehold tourism-zone — zone-status verification BEFORE deposit (CR ZMT, BR marinha, BS Crown, CV ZDTI)

---

## Section: `--language`

**Goal**: Foreign-buyer language requirements — what language must the deed be in, when is a sworn translator mandatory at signing, what's the apostille / POA chain, what does sworn translation cost.

**Universal logic** (works in every country): full implementation in `shared/language.md`. Single canonical doc with 7 cross-cutting traps + regional patterns + per-country one-liners for all 103 supported countries — country playbook does NOT need a separate language section.

**Disambiguation**: `--language` ≠ `--notary` ≠ `--visa`. `--language` = deed-language rule + sworn-translator regime + POA-translation chain. `--notary` = transaction-completion process. `--visa` = residency programs.

**What to look up** (universal):
- Closing-deed language; bilingual permitted; which version controls
- Sworn interpreter at signing: mandatory / on demand / not used
- POA / apostille chain: Hague Apostille member status; chain from foreign-language POA → apostille / consular legalisation → sworn translation → notary acceptance
- Mandatory diagnostic / disclosure document language (DPE/APE/CEE/Energieausweis/EPC/BER/PEA — local-language-only or bilingual)
- Sworn-translation cost band (industry-reported or statutory tariff)
- Confidence: HIGH / MEDIUM / LOW

**Output structure** (full template in `shared/language.md`):
```markdown
## Language & Sworn-Translation Profile

**Country**: <ISO2>
**Closing-deed language**: <local language(s); which version controls if bilingual>
**Sworn interpreter at signing**: <mandatory / on demand / not used>
**POA chain**: <Hague Apostille y/n → apostille or consular legalisation → sworn translation → notary acceptance>
**Diagnostic docs language**: <local-only / bilingual standard>
**Sworn-translation cost**: <range, industry-reported or statutory>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/language.md`):
- Hague Apostille membership confusion — non-members (AE, EG, JO, KW, LB, QA, NG, KE, GH, TW, KH, LK, MV, MY, TH-until-late-2026, VN-until-Sept-2026) require full consular legalisation chain (4-8 weeks)
- "Sworn translator" means three different regimes — statutory profession (FR/DE/ES/IT/...), court-admitted (ZA/JP/KR/IN), or notary-public-certified (IL/US/UK/IE/AU/NZ + most common-law)
- Bilingual deeds — local-language version always controls (IT, DE, ID, MX, HU)
- Diagnostic documents universally local-language-only — buyer pays own translation
- State / regional variation breaks single-country assumptions — CA Quebec Bill 96, US CA Civ. Code § 1632, CH cantonal, BE language regions, IN state language, ES regional
- Consular POA bypass — civil-law consulates abroad can draft local-language POA directly, bypassing both apostille and sworn-translation steps
- Sworn-translator cost varies 10× across region — US/UK/AU/NZ ~$50-150/page market vs NO statutory NOK 1,200-2,500/page (~€100-220) vs full POA chain $1,500-3,500 in non-Hague jurisdictions

---

## Section: `--climate`

**Goal**: Long-term climate-change projections specific to the property's coordinates — temperature, sea-level rise, heatwaves, drought, wildfire, degree-day shift.

**Universal logic** (works in every country): full implementation in `shared/climate-projections.md`. Pulls from Copernicus Climate Data Store (CDS), IPCC AR6 Interactive Atlas, Climate Central Coastal Risk Screening Tool (coastal only), and national downscaled models where available (DRIAS FR, DKRZ DE, NCCS CH, SMHI SE, KNMI NL, etc.).

**What to look up** (universal):
- Köppen-Geiger climate classification (current baseline)
- Distance to coast (via Overpass `natural=coastline`)
- Temperature trajectory: now → 2050 → 2100 (SSP2-4.5 + SSP5-8.5)
- Hot days (TX≥30°C / TX≥35°C / TX≥40°C) per year
- Tropical nights (TN≥20°C) per year
- Sea-level rise (cm by 2050, 2100) — coastal only
- Drought / SPEI projection
- Wildfire FWI projection
- HDD / CDD shift (heating vs cooling degree-days)
- Precipitation pattern (winter wetter / summer drier typical for EU)

**Output structure**:
```markdown
## Climate & Long-term Resilience

**Coordinates**: <lat>, <lon>
**Climate zone**: <Köppen-Geiger code>
**Coastal**: <yes — distance X km / no>
**Elevation**: <m a.s.l.>
**Reference**: 1981–2010 baseline → 2050 / 2100

### Temperature trajectory
| Metric | Baseline | 2050 SSP2-4.5 | 2050 SSP5-8.5 | 2100 SSP5-8.5 |

### Sea-level rise (coastal)
| Year | RCP4.5 | RCP8.5 | High-end |

### Drought / wildfire / degree-days
- SPEI: <↑↓→>
- FWI: <% change>
- HDD shift: <X → Y> · CDD shift: <X → Y>

### Verdict
🟢/🟡/🟠/🔴 — <one-line>

### Confidence
<HIGH | MEDIUM | LOW>
```

**Verdict bands** (full criteria in `shared/climate-projections.md`):
- 🟢 Resilient — minimal impact, low exposure to acute climate events
- 🟡 Watch — moderate warming, some adaptation needed
- 🟠 Adapt — meaningful long-term cost or risk
- 🔴 Avoid or fortify — high exposure to multiple acute events

**Acute-event flags** (red flags):
- Coastal property < 5m elevation + SLR > 80 cm by 2100
- Wildland-urban interface (within 100 m of forest/scrub) in fire zone
- Within 100 m of river floodplain with flood multiplier > 2x by 2050
- Permafrost zone with thaw projected during ownership horizon
- Glacial outburst flood (jökulhlaup) zone

**Country-specific override** (when finer-resolution model exists):
- 🇫🇷 DRIAS · 🇩🇪 DKRZ + DWD Klimaatlas · 🇨🇭 NCCS · 🇸🇪 SMHI Klimatscenarier · 🇫🇮 Climateguide.fi · 🇳🇴 Klimaservicesenter · 🇩🇰 DMI Klimaatlas · 🇳🇱 KNMI Klimaatscenario's

---

## Implementation guidelines for country playbooks

When you write `countries/<iso2>/playbook.md`:

1. Implement the 7 country-specific sections (price, traffic, tax, rental, work, risks, mains). The 3 universal sections (crime, amenities, climate) inherit from `shared/`.
2. For each section, list:
   - Specific data source URLs (with patterns)
   - Extraction quirks (PDF size, OCR needed, login walls)
   - Compute formulas (specific to the country's tax/cost structure)
   - Country-specific output template (extending the universal one above)
3. For `--crime`: country-specific portal URLs go in the country playbook OR can be inherited from `shared/crime-sources.md`
4. For `--amenities`: the universal OSM logic in `shared/amenities-osm.md` applies; country playbook only needs to note brand-chain conventions
5. For `--climate`: universal Copernicus/IPCC always available; if country has finer-resolution model (DRIAS, DKRZ, etc.), country playbook should reference it as an override
6. Add a "Cost benchmarks" section with renovation costs typical to that country.
7. Add a "Mandatory diagnostics" section with the country's required-at-sale documents.
8. Reference the country's most-used real estate platforms for listing extraction.

## Cross-cutting layers (apply on top of section output)

When `--integrity`, `--journey=<type>`, or `--type=<kind>` is requested, additional cross-cutting analysis is layered onto the standard section output. See:
- `shared/integrity-checks.md` — 4 data-honesty checks
- `shared/journeys.md` — 7 buyer-journey templates
- `shared/property-types.md` — 11 specialized property-type templates

If a section is genuinely not applicable for a country (e.g., `--mains` in a country where mains drains are universal in the urban areas), still produce the section but say "universal in <country> — no individual verification needed unless rural/remote."
