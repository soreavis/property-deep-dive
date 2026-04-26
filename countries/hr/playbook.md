# Croatia 🇭🇷 — Property Due-Diligence Playbook

ISO2: `hr`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`10000` Zagreb central, `21000` Split, `20000` Dubrovnik, `52100` Pula)
- **Admin levels**: 21 županije (counties) + 555 cities/municipalities
- **Currency**: **EUR (€)** — adopted 1 Jan 2023 (replaced HRK)
- **Languages**: Croatian (official); Italian, Hungarian, Serbian (regional minorities)
- **Cadastre**: **dual register** (Croatia famously has separate catastral + land registry — must reconcile both)
  - **DGU Geoportal**: `https://geoportal.dgu.hr/` — central spatial data
  - **Katastar.hr**: `https://katastar.hr/` — paid cadastral data
  - **OSS Uređena zemlja**: `https://oss.uredjenazemlja.hr/` — unified search (cadastre + ZK gruntovnica)
- **Identifier**:
  - Cadastral parcel number `broj čestice` within cadastral municipality `k.o.`
  - ZK title number `zk uložak` in gruntovnica
- **Ownership types**: vlasništvo (full); etažno vlasništvo (condominium); collective + co-ownership
- **EU member since 2013 + eurozone since 2023**

## Section: `--price`

### Primary sources

- **DZS (Croatian Bureau of Statistics)**: `https://podaci.dzs.hr/` — official residential price index
- **HNB (Croatian National Bank)**: `https://www.hnb.hr/` — financial stability + housing market reports
- **OSS Uređena zemlja**: `https://oss.uredjenazemlja.hr/` — unified cadastre + ZK
- **Croatia Week property reports** + **Bilten nekretnina** (Eurofast)

### Listing platforms

- **Njuškalo** — DOMINANT (~500k daily visits): `https://www.njuskalo.hr`
- **Index Oglasnik** — #2: `https://www.index.hr/oglasi`
- **Crozilla** — coastal specialist: `https://www.crozilla.com`
- **Indomio.hr** (REA Group): rising specialist
- **Eurovilla.hr, dogma-nekretnine.com** — niche

### 2025 price benchmarks (DZS + Njuškalo)

| Region | Avg €/m² (apt asking) | Trend |
|---|---:|---|
| **Zagreb** (capital) | 3,000–3,698 | rising |
| **Split** | 5,183 | **+13.85% YoY** (fastest growth) |
| **Dubrovnik** | 4,150–6,967 (standard); **prime seafront/Old Town up to 10,000** | high tourist premium |
| **Rijeka** | 2,800–3,500 | rising |
| **Pula** (Istria) | 3,283 | rising |
| **Zadar** | 3,500–4,200 | rising |
| **Šibenik** | 2,800–3,800 | rising |
| **Coastal islands (Hvar, Brač, Korčula)** | 4,500–8,000+ | premium |
| **Continental (Slavonia)** | 700–1,200 | flat/declining |
| **National avg asking** | 3,636 (+6.5% YoY) | |

### Compute

1. €/m² = price / **uporabna površina** (usable area)
2. Cross-check **OSS Uređena zemlja** for cadastre/ZK reconciliation
3. **HR dual register pitfall**: cadastre says one thing, ZK gruntovnica says another — common; must reconcile
4. **Adriatic premium**: factor 2-3× over continental
5. **Seafront/Old Town Dubrovnik**: up to €10,000/m²

### Key terms

- Vlasništvo = ownership
- Etažno vlasništvo = condominium
- ZK uložak = land register title number
- Broj čestice = cadastral parcel number
- k.o. = cadastral municipality
- Energetski certifikat = energy certificate

---

## Section: `--traffic`

### Sources

- **HC (Hrvatske ceste)**: `https://hrvatske-ceste.hr/` — state roads + traffic counts
- **HAC (Hrvatske autoceste)**: motorways
- **Local cities**: Zagreb GUP, Split urban data

### Key term

**PGDP (Prosječni godišnji dnevni promet)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural, islands)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (urban arterials, državne ceste)
- 🔴 > 35,000 v/d (autoceste A1, A6, Zagreb ring)

---

## Section: `--tax`

### Annual property tax — Porez na nekretnine (NEW 2025)

**MAJOR REFORM 1 January 2025**: replaces previous communal fee + holiday-home tax.

#### Rate range

- **€0.60–€8.00/m²** of usable area per year
- Set by each municipality within range
- **Highest rate (€8)**: Umag, Vis, Sveti Filip i Jakov, Fažana, Baška Voda
- **Major cities**: Zagreb €5, Split €1.99, Rijeka €5, Osijek €0.60
- 119 municipalities at floor (€0.60); 73 at €5–€8
- Revenue split 80% municipality / 20% county

#### Exemptions

- Primary residence (where owner lives)
- Family homes (where family lives — not just registered owner)
- Long-term rentals (≥10 months/year)

#### Typical bills

| Property | Annual |
|---|---:|
| Zagreb 80m² apt (€5/m²) | €400 |
| Split 100m² apt (€1.99/m²) | €199 |
| Dubrovnik 100m² (max €8/m² — but city is €5) | €500 |
| Hvar 100m² coastal (premium) | €500–€800 |
| Tisno 80m² (€8/m² Sveti Filip) | €640 |

### Transaction taxes

- **Real estate transfer tax (RETT)**: **3%** on resale (no VAT)
- **VAT (PDV)**: **25%** on new builds first sale
- **Notary**: ~0.5–1.5%
- **Realtor commission**: 2–3% per side

### Capital gains

- **24% on disposal within 10 years** (gain = sale - indexed purchase)
- **Exempt if held >10 years** OR if **primary residence**

### Total transaction cost (buyer side)

- Resale: ~5-7% (3% RETT + 1-1.5% notary + 2-3% realtor)
- New build: 25% VAT in price + ~3% other costs

### Future risk

- Porez na nekretnine: rate changes likely as municipalities recalibrate 2025-2027
- VAT may rise post-eurozone integration

---

## Section: `--rental`

### Long-term residential

- **Zakon o najmu stanova** (Tenancy Act) — moderate tenant protection
- Standard 1-3 yr contracts
- Rent control limited

### Short-let — MAJOR 2025 CRACKDOWN

**2025 Hospitality Activities Act** (effective May 2025):
- **80% co-owner consent** required to operate STR in multi-unit building (raised from 66% earlier in 2025 under Building Management Act)
- **Plus immediate-neighbour approval** (units sharing walls/floors/ceilings)
- **Mandatory unique national registration number** for all STRs
- **Result**: ~7,000 beds removed in one Dalmatian county; Adriatic supply contracting

#### Categories (ATA classification via local Turistička zajednica)

- **Apartman** (apartment)
- **Soba** (room)
- **Studio apartman** (studio)
- **Kuća za odmor** (holiday house)

#### Tax

- Long-term rentals: 8% income tax
- Short-term rentals: 10% income tax
- Both with applicable indexation

---

## Section: `--work=<profession>`

### Sources

- **HZZ (Hrvatski zavod za zapošljavanje)**: `https://www.hzz.hr/` — employment service
- **MojPosao.net** — biggest: `https://www.moj-posao.net/`
- **Posao.hr**, **Bika.net**, **LinkedIn HR**

### Self-employment

- **Obrt** = sole trader (registered at HOK)
- **D.o.o.** = limited; min €2,500 capital
- **PDV (VAT)** registration: from €40,000 turnover
- **Paušalni obrt**: flat-rate up to €40,000 turnover (preferential)

### Salary benchmarks (2025)

- Median monthly gross:
  - Zagreb: ~€1,700–€2,400
  - Split / Rijeka / Osijek: ~€1,400–€1,900
  - Smaller cities: ~€1,200–€1,600
- **Minimum wage**: €970/month gross (2025)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **DHMZ (Croatian Meteorological & Hydrological Service)** | `https://meteo.hr/` | Weather, climate, **CFFWIS fire index** (since 1982) |
| **HGI-CGS (Croatian Geological Survey)** | `https://www.hgi-cgs.hr/en/` | Geology, **earthquake**, karst |
| **Seizmološka služba (PMF Zagreb)** | `https://seizmo.hr` | Seismic monitoring |
| **Voda.hr (river basin authorities)** | `https://www.voda.hr/` | Flood + water management |

### Specific risks

#### Earthquake — CRITICAL

- **Zagreb fault zone**: highest hazard in continental HR
- **March 2020 Zagreb (M5.5)** — major damage
- **December 2020 Petrinja (M6.4)** — ~50 km SE Zagreb; **still under reconstruction 2026**
- **PGA hazard maps** for 95/225/475-year return periods on bedrock A
- **Slavonia** (E HR): lower risk
- **Coastal Adriatic**: variable (Dubrovnik 1979 M7.0)

#### Wildfire

- **Adriatic / Dalmatia coast**: critical fire zone
- **DHMZ CFFWIS** (Canadian Forest Fire Weather Index System) since 1982
- **+1,000 fires in 2024** vs prior year
- Pinewood resin = high fire intensity
- Ferry-route disruption common Jul-Aug

#### Karst hazards

- **Dinaric karst**: sinkholes, doline, cave drainage
- **Coastal hinterland Adriatic** + Lika + Gorski Kotar
- **HGI-CGS** publishes geological maps
- No single statutory sinkhole risk register
- Construction on karst requires soil study

#### Other risks

- **Coastal storm + sea-level rise**: Adriatic
- **Flood**: inland Sava, Drava (Zagreb 2014, Slavonia 2014)
- **Bura (Adriatic strong NE wind)** — winter storms
- **River basin authorities** (`https://www.voda.hr/`)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **1900–1990 (Yugoslav era)** | Asbestos common, Yugoslav-era panel buildings (Novi Zagreb) |
| **1980–2008** | PBAB81 standards (post-1981 Skopje quake reforms) |
| **Post-2008 EC8** | Modern seismic |
| **Post-2020 Zagreb earthquake** | Reconstruction with EC8 mandatory |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetski certifikat** | Mandatory since 2014 at sale + lease | 10 years |
| **Javnobilježnička isprava** | Notarial deed | At sale |
| **OSS Uređena zemlja extract** | Title verification | Current |

### Climate change projections

- **+2.0–4.0°C** by 2100
- **Adriatic sea-level rise**: +20–60 cm by 2100
- **Reduced summer precipitation**: -10–25% (Mediterranean drying)
- **Increased wildfire risk**
- **More extreme rainfall events** (continental)

---

## Section: `--mains`

### Sources

- **Vodovod i kanalizacija** per municipality (e.g., Vodoopskrba i odvodnja Zagreb d.o.o., Vodovod i kanalizacija Split)
- Coastal islands: often septic / cisterns

### Costs

| Scenario | Cost (€) |
|---|---:|
| Mains connection | €3,000–€8,000 |
| Septic upgrade | €4,000–€10,000 |
| Cistern (coastal) | €2,000–€8,000 |

---

## Cost benchmarks (HR 2026)

| Work | Cost (€) |
|---|---:|
| Energetski certifikat | 150–400 |
| Notary fee | 0.5–1.5% of price |
| RETT (resale) | 3% |
| Realtor commission | 2–3% per side |
| **Total transaction cost (resale)** | **~5–7%** of price |
| **Total transaction cost (new build)** | 25% VAT included + ~3% other |
| Roof renovation | 8,000–20,000 |
| Asbestos abatement | 3,000–10,000 |
| Earthquake retrofit (older builds) | 25,000–80,000+ |
| Energy retrofit | 25,000–60,000 |
| Karst soil study | 1,500–4,000 |
| Cistern installation | 2,000–8,000 |

## Active fiscal incentives (2025-2026)

- **NPSR (Nacionalni plan oporavka i otpornosti)** — EU recovery funds for energy retrofit
- **Petrinja reconstruction** subsidies (continuing)
- **First-home reduction** under specific conditions

## Common listing platforms

- **Njuškalo** — DOMINANT
- **Index Oglasnik** — secondary
- **Crozilla** — coastal specialist
- **Indomio.hr** — REA Group entrant
- **Eurovilla, dogma-nekretnine** — niche

## Caveats unique to HR

- **NEW Porez na nekretnine 2025** — €0.60–€8/m²/yr; replaces communal fee + holiday-home tax
- **Currency: EUR since 1 Jan 2023** — no FX risk for eurozone buyers
- **Dual register reconciliation** (cadastre vs ZK gruntovnica) — common HR pitfall
- **Earthquake risk CRITICAL**: Zagreb 2020 + Petrinja 2020; reconstruction ongoing
- **Karst hazards**: Dinaric coastal hinterland — sinkholes, drainage; no single risk register
- **Wildfire**: Adriatic critical Jul-Aug; DHMZ CFFWIS since 1982
- **2025 Hospitality Act**: 80% co-owner consent for STR; mandatory unique reg number
- **~7,000 STR beds removed in one Dalmatian county** post-2025 reform
- **Real estate transfer tax 3%** on resale; **VAT 25%** on new
- **Capital gains 24% within 10 years**, exempt after
- **Reciprocity rule for non-EU buyers**: nationals of countries that allow Croatians to buy (US, UK, AUS, JP, BRA, ARG, KOR, RUS, IL, CH, NO confirmed) can purchase as natural persons + Ministry of Justice permission required
- **Non-reciprocity countries**: must form Croatian company
- **Agricultural land**: EU citizens can buy since July 2023 (moratorium ended); non-EU need special ministry approval
- **Forest, pasture, protected coastal zones**: off-limits to all foreign buyers
- **Adriatic seafront premium**: 2-3× continental rates; up to €10,000/m² Old Town Dubrovnik
- **Etažno vlasništvo** (condominium) financial health critical
- **Petrinja reconstruction**: tens of thousands still in temporary accommodation 2026

## Reddit / forum sources

- **r/croatia** — biggest community
- **r/Zagreb**, **r/split**
- **Total Croatia News** (English)
- **Croatia Week** (English)
- **The Dubrovnik Times** (English)

## Verification authorities

| Authority | When to call |
|---|---|
| **OSS Uređena zemlja** | Cadastre + ZK reconciliation |
| **Katastarski ured** | Local cadastre |
| **Općinski sud (gruntovnica)** | Title verification |
| **Javni bilježnik** (notary) | Sale process |
| **Porezna uprava** | Porez na nekretnine + transfer tax |
| **Local Turistička zajednica** | STR registration |
| **Ministarstvo pravosuđa** | Non-EU buyer approval |

## Source URL templates

| Source | URL pattern |
|---|---|
| DGU Geoportal | `https://geoportal.dgu.hr/` |
| OSS Uređena zemlja | `https://oss.uredjenazemlja.hr/` |
| Katastar.hr | `https://katastar.hr/` |
| Porezna uprava | `https://porezna-uprava.gov.hr/` |
| DZS | `https://podaci.dzs.hr/` |
| Njuškalo | `https://www.njuskalo.hr/nekretnine/` |
| DHMZ | `https://meteo.hr/` |
| HGI-CGS | `https://www.hgi-cgs.hr/en/` |
| Seizmološka služba | `https://seizmo.hr` |
| eEnergetski certifikat | `https://eenergetskicertifikat.mpgi.hr/` |
| Voda.hr | `https://www.voda.hr/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing (DZS + Njuškalo + HNB), traffic (HC PGDP), tax (NEW Porez na nekretnine 2025 €0.60-€8/m² + 3% RETT + 25% VAT new), rental (2025 Hospitality Act 80% consent), work, risks (earthquake CRITICAL Zagreb 2020 + Petrinja 2020 + wildfire + karst), mains all have primary government sources.
**Confidence**: HIGH for Porez na nekretnine 2025 reform (rates confirmed via Croatia Week + Eurofast); HIGH for 2020 earthquake reference + Petrinja reconstruction; HIGH for 2025 Hospitality Act 80% consent rule + mandatory STR registration; HIGH for currency EUR transition (1 Jan 2023). MEDIUM for non-EU reciprocity list (changes periodically).

## Extension TODOs

- [ ] Per-municipality Porez na nekretnine rates table
- [ ] Petrinja reconstruction status + grants
- [ ] Adriatic vs continental price multiple by region
- [ ] Karst hazard zone overlay (HGI-CGS)
- [ ] STR 80% consent decision tree
- [ ] Non-EU buyer reciprocity verification per nationality
- [ ] Wildfire vulnerability per island
- [ ] Cadastre-vs-ZK reconciliation flow
- [ ] Earthquake retrofit cost estimator (post-2020 reforms)
- [ ] EC8 compliance for new builds
