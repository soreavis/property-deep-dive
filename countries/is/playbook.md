# Iceland 🇮🇸 — Property Due-Diligence Playbook

ISO2: `is`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 3 digits (`101` Reykjavík central, `200` Kópavogur, `600` Akureyri, `400` Ísafjörður)
- **Admin levels**: 8 regions + 64 sveitarfélög (municipalities)
- **Currency**: **ISK** (Icelandic króna); 1 EUR ≈ 145–155 ISK (volatile)
- **Languages**: Icelandic (official); English widely understood
- **Cadastre**: **HMS (Húsnæðis- og mannvirkjastofnun)** + **Þjóðskrá Íslands** (national registry)
- **Identifier**: **fasteignanúmer** (property number) + **landnúmer** (land number)
- **Ownership types**:
  - **Eignaríbúð** (freehold apartment)
  - **Einbýlishús** (single-family house)
  - **Parhús** (semi-detached)
  - **Raðhús** (terraced/townhouse)
  - **Fjölbýlishús** (apartment building, with húsfélag = building association)
- **Volcanic + seismic country** — ALL property analysis must factor in active geological hazards
- **Iceland is NOT in EU** — but EEA member; some property buying restrictions apply

## Section: `--price`

### Primary sources

- **HMS Fasteignaskrá** (cadastre + valuation): `https://www.hms.is/`
  - Free property search
- **Þjóðskrá Íslands** (national registry): `https://skra.is/`
- **Hagstofa Íslands (Statistics Iceland)** — Vísitala íbúðaverðs: `https://hagstofa.is/`
  - Monthly housing price index
- **Seðlabanki Íslands (Central Bank)** — financial stability reports: `https://www.cb.is/`
- **HMS** publishes monthly Húsnæðismarkaðurinn (housing market) report

### Listing platforms

- **Mbl.is fasteignir**: `https://www.mbl.is/fasteignir/`
- **Visir.is**: `https://www.fasteignir.is/`
- **Húsaleiga.is**, **Bland.is** for rentals
- **Remax IS**, **Eignamiðlun**, **Fasteignamarkaðurinn**, **Domus**, **Gimli**, **Brynja** — agency networks
- **fasteign.is** (HMS public listing)

### 2025 price benchmarks (Hagstofa + HMS)

| Region | Avg ISK/m² (apt) | Avg total (einbýlishús) |
|---|---:|---:|
| **Reykjavík 101 (centro)** | 950,000–1,400,000+ | 110,000,000–250,000,000 |
| **Reykjavík 105/107 (Hlíðar/Vesturbær)** | 800,000–1,100,000 | 90,000,000–150,000,000 |
| **Greater Reykjavík (Kópavogur, Hafnarfjörður, Garðabær)** | 650,000–950,000 | 75,000,000–130,000,000 |
| **Akureyri** | 500,000–700,000 | 55,000,000–85,000,000 |
| **Reykjanesbær** | 450,000–650,000 | 50,000,000–75,000,000 |
| **Selfoss / Árborg** | 480,000–650,000 | 55,000,000–80,000,000 |
| **Westfjords / East fjords** | 250,000–500,000 | 25,000,000–55,000,000 |
| **Sumarbústaðir** (cottages) | varies | 15,000,000–80,000,000+ |

### Compute

1. ISK/m² = price / **Brúttóflatarmál** (gross floor area, BBR equivalent)
2. **Fasteignamat** ≈ 80–95% of market price typically (HMS conservative)
3. **Krónaverðbólga** factor — high inflation 2022-2024 distorts longitudinal data
4. Compare ISK price to EUR using current FX (ISK volatile)

### Key terms

- Eignarheimild = title deed
- Fasteignamat = official property valuation (annual, used for tax)
- Söluverð = sale price
- Fermetraverð = price per m²
- Húsfélag = building association (apt buildings)
- Heitt vatn = hot water (geothermal)

---

## Section: `--traffic`

### Sources

- **Vegagerðin** (Iceland Road Administration): `https://www.vegagerdin.is/`
- **Kort vegagerdin** — count map
- Ring Road (Hringvegur, Route 1) and main routes traffic data

### Key term

**ÁDU (Ársdagsumferð)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,000 v/d (rural Westfjords / interior)
- 🟡 1,000–8,000 v/d (regional routes, Ring Road in north/east)
- 🟠 8,000–25,000 v/d (Reykjavík periphery, Ring Road south)
- 🔴 > 25,000 v/d (Reykjavík main arteries, Miklabraut)

---

## Section: `--tax`

### Annual property tax — Fasteignagjöld

- Set per sveitarfélag
- Based on **fasteignamat** (annual official valuation by HMS)
- Typical rates:
  - Residential (A-skattflokkur): **0.18–0.45%** of fasteignamat
  - Commercial (C-skattflokkur): **1.32%** (federal max)
  - Bare land (B-skattflokkur): 1.0% typical
- Reykjavík residential: **0.18%**
- Reduced rates often for retirees, low-income
- **Sorphirðugjald** (waste collection) added separately
- **Vatnsgjald + Holræsagjald** (water + sewer) per sveitarfélag

### Transaction taxes

- **Stimpilgjald** (stamp duty): **0.8%** of property purchase price (one of lowest in Europe)
  - Half-rate **0.4%** for first-time buyers
- **Þinglýsingargjald** (registration fee): ~ISK 30,000 flat
- **Fasteignasalalaun** (broker): typically **1–2%** paid by seller (negotiable)

### Total transaction cost (buyer side)

- **First-time buyer**: ~0.5–1% of price
- **Standard buyer**: ~1–2% of price (very low)
- Seller: ~1–2% (broker)

### Capital gains

- **22% flat** for individuals (since 2021)
- **Primary residence sale exempt** under conditions: ownership 2+ years OR 7+ years used residence
- **Sumarbústaður** (cottage): less generous exemption
- Investment property: full 22% on gain

### VAT (VSK)

- 24% standard
- 11% reduced (food, books, hotels, tourist services)
- New residential property: **11% VSK reduced rate** (since 2010)
- Builder VAT-refund scheme: 35% refund on labour for new build/extension/maintenance via **endurgreiðsla VSK**

### Future risk

- **Stimpilgjald** stable
- **Fasteignamat** annual revision
- **Currency risk** — ISK volatile
- **Foreign-currency mortgages BANNED** post-2008 crisis

---

## Section: `--rental`

### Long-term residential

- **Húsaleigulög** (Tenancy Act): moderate protection
- **Tímabundinn leigusamningur** (fixed-term) common
- **Ótímabundinn leigusamningur** (open-ended) — termination notice 6 months
- Standard income tax on rental: progressive **24.5% to 46.25%**; some flat-rate options
- **Eignaskattfrelsi** for long-term tenants in primary owner residence (parts)

### Short-let (Airbnb / Heimagisting)

**Heimagisting (home accommodation registration) required**:
- Reykjavík: **max 90 nights/year** for primary residence without commercial license
- Beyond 90 days: requires **rekstrarleyfi** (operator license) + **VSK 11%**
- **VSK 11% on rental services**
- **Borgarvíking** registration required for short-let in Reykjavík
- **EU 2024/1028 STR**: not directly applicable (NOT in EU); EEA agreement may extend

### Tax on short-let

- Heimagisting income: standard income tax
- License-required short-let: business income, VSK applies

---

## Section: `--work=<profession>`

### Sources

- **Vinnumálastofnun** (Directorate of Labour): `https://vmst.is/`
- **Alfred** job platform: `https://www.alfred.is/`
- **LinkedIn IS**, **Tvinna.is**, **Mbl Atvinna**

### Self-employment

- **Einyrkjarekstur** (sole trader): no min capital
- **EHF.** (private limited): min ISK 500,000
- **HF.** (public limited): min ISK 4,000,000
- **VSK registration** mandatory at any turnover for some sectors
- **RSK (Skattur)** registration for tax

### Salary benchmarks (2025)

- Median monthly gross:
  - Reykjavík: ~ISK 800,000–1,100,000
  - Akureyri: ~ISK 700,000–950,000
  - Smaller towns: ~ISK 600,000–850,000
- **Lágmarkslaun** (minimum wage): ~ISK 425,000/mo (varies by union)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Veðurstofan Íslands (IMO)** | `https://www.vedur.is/` | Meteorology, hydrology, **seismology, volcanology** |
| **Náttúruvársjóður / Náttúruhamfaratryggingar (NTÍ)** | `https://nti.is/` | National natural disaster insurance |
| **HMS** | `https://www.hms.is/` | Housing standards |
| **Almannavarnir** (Civil Protection) | `https://www.almannavarnir.is/` | Emergency response |
| **ÍSOR (Iceland GeoSurvey)** | `https://www.isor.is/` | Geology, geothermal |
| **Veitur** | `https://www.veitur.is/` | Reykjavík utility (district heating) |

### Specific risks (HIGHEST geological hazard density in Europe)

#### Volcanic + seismic — current activity

**Reykjanes peninsula 2023-2025 eruption series** (CRITICAL UPDATE):

- **9 eruptions since December 2023** at Sundhnúkur fissure (as of mid-2025 data)
- **11 eruptions south of Reykjavík since 2021** (Fagradalsfjall + Sundhnúkur + Litli-Hrútur)
- **Most recent**: 16 July 2025 (slowed by 5 August)
- **Grindavík mostly abandoned** since November 2023; 4,000 residents evacuated
- Volcanic dykes have penetrated protective barriers
- **"New Reykjanes Fires"** — volcanologists suggest a multi-century active period (parallel to 13th century)
- **Property risk in Reykjanes**:
  - **Grindavík properties**: most uninhabitable; government buyback scheme
  - **Reykjanesbær (Keflavík area)**: some risk, monitored
  - **Greater Reykjavík (40km north)**: indirect risk via gas, ash
- **Authority monitoring**: `https://www.vedur.is/skjalftar-og-eldgos/` (live)

#### Other volcanic zones

- **Hekla** — overdue (last eruption 2000)
- **Katla** — major dangerous; subglacial; jökulhlaup risk
- **Bárðarbunga** — major; Holuhraun 2014-15 longest in 230 yrs
- **Grímsvötn** — under Vatnajökull; jökulhlaup chronic
- **Öræfajökull** — historic catastrophe (1362)

#### Seismic

- Iceland sits on **Mid-Atlantic Ridge** — ~500 quakes/day mostly small
- **Suðurlandsskjálftar** (South Iceland zone): historic M 6.0+ events
- **Reykjanesskagi**: active swarm zone (current)
- **Tjörnesbeltið** (north): also active
- Eurocode 8 with Icelandic annex applies

#### Other geological hazards

- **Hraunrennsli** (lava flow) — direct property destruction risk
- **Jökulhlaup** (glacial outburst flood) — Skeiðará, Markarfljót, Súla — catastrophic
- **Snjóflóð** (avalanche): Westfjords + East fjords known fatal events
  - **Flateyri 1995** (20 dead), **Súðavík 1995** (14 dead), **Neskaupstaður 1974**
- **Skriðuhætta** (landslide): Westfjords + Northern Iceland
  - **Seyðisfjörður 2020** mudslide
- **Strandrof** (coastal erosion) + sea-level rise
- **Stormflóð** (storm surge) — winter storms catastrophic
- **Veðuröfgar** (extreme weather) — winds 50+ m/s recorded

### Insurance via Náttúruhamfaratryggingar (NTÍ)

**MANDATORY natural disaster insurance** — automatic via property insurance:
- Covers: volcanic eruptions, earthquakes, floods, avalanches, landslides
- Funded via property insurance premiums (compulsory iðgjald)
- Payout based on rebuild value
- **One of the most comprehensive natural-hazard insurance schemes globally**
- For Grindavík: state-purchase scheme + NTÍ payouts active 2024-2025

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960** | Low seismic standards |
| **1960s onwards** | Gradually improved |
| **Post-2002** | ÍST EN 1998 seismic design |
| **Post-2010** | Modern energy + seismic |
| **Concrete + steel reinforcement** dominant |
| **Wood common in older buildings** | Fire risk |
| **Asbestos**: pre-1980s likely; banned 1990s |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Söluyfirlýsing** | Sale declaration of seller's known defects | At sale |
| **Fasteignamat** | Current valuation (HMS) | Annual |
| **Veðbókarvottorð** (encumbrance certificate) | Title verification | At sale |
| **Energy declaration (Orkumerki)** | Phased in; **mandatory since 2013** for all new sales of new builds; gradually retroactive | Per case |
| **Brunabótamat** (insurance valuation) | Mandatory for buildings | Annual |

### Climate change projections (Veðurstofan)

- +1.5–4.0 °C by 2100
- Sea-level rise: +20–60 cm by 2100
- Glacier retreat: significant (Jökulsárlón growing)
- Increased precipitation
- Possible decline in ocean cooling effect

---

## Section: `--mains`

### Sources

- **Veitur** (Reykjavík utility, district heating + water): `https://www.veitur.is/`
- Per-sveitarfélag water utilities elsewhere
- **Hitaveita** (district heating co-operatives) per region

### Verification

- **Geothermal hot water (jarðhiti)** for ~90% of households — UNIQUE
  - Cheap energy, almost universal in populated areas
  - Some Westfjords + East fjord settlements use electric/oil heating
- **Cold water** + **sewer** typically per municipality
- **Rotþrær / fráveitukerfi**: rural cottages on individual systems

### Costs

| Scenario | Cost (ISK) |
|---|---:|
| Hitaveita connection | 1,000,000–3,000,000 |
| Cold water + sewer connection | 800,000–2,500,000 |
| Mains-line extension | 5,000,000–15,000,000+ |

---

## Cost benchmarks (IS 2026)

| Work | Cost (ISK) |
|---|---:|
| Stimpilgjald | 0.8% of price (0.4% FTB) |
| Þinglýsingargjald | ~30,000 ISK flat |
| Fasteignasalalaun | 1–2% of price (seller) |
| **Total transaction cost (buyer)** | **~1–2%** of price |
| Söluyfirlýsing | 30,000–80,000 |
| Energy upgrade | 4,000,000–12,000,000 |
| Antiseismic retrofit | 3,000,000–8,000,000 |
| Roof (corrugated steel, 150 m²) | 2,000,000–4,000,000 |
| Asbestos abatement | 800,000–3,000,000 |
| Hitaveita connection | 1,000,000–3,000,000 |

## Active fiscal incentives (2025-2026)

- **Endurgreiðsla VSK** (35% labour VAT refund): for new build, extension, maintenance
- **Fyrstu kaup** (first-time buyer) tax-deductible savings program
- **Almenna lánasjóðurinn** (public housing fund) loans
- **Húsnæðisstuðningur**: rental subsidy
- **Vaxtabætur** (mortgage interest tax credit): up to ISK 400,000-600,000/yr depending on income/family

## Common listing platforms

- **Mbl.is fasteignir** — biggest
- **Visir.is**
- **Remax IS, Eignamiðlun, Fasteignamarkaðurinn, Domus, Brynja, Gimli** — agency networks

## Caveats unique to IS

- **VOLCANIC + SEISMIC RISK IS REAL AND ACTIVE**:
  - Reykjanes 2023-2025 series destroyed homes in Grindavík
  - **9 eruptions since Dec 2023** at Sundhnúkur
  - **"New Reykjanes Fires"** potentially multi-century period
  - Property in Reykjanes peninsula carries elevated risk
- **Mandatory natural-hazard insurance (NTÍ)** is automatic via property insurance — major buyer protection
- **Geothermal heating** universal in populated areas — extremely cheap energy, but check connection
- **Currency volatility** — ISK can swing 20–30% vs EUR
- **Foreign-currency mortgages BANNED** post-2008 crisis
- **Foreigner restrictions**: non-EEA buyers need approval from Justice Ministry for residential
- **Sumarbústaður** (summer cottage) — different regime, often in privately-owned summer-cottage zones
- **Sjálandseyjar** (community lands) — some properties on lease from sveitarfélag
- **Reykjavík dominates** — 65% of population in capital region
- **Build quality varies** — older buildings concrete-clad; newer have improved seismic
- **Inflation 2022–2024** spiked sharply; central bank rate elevated; cooling 2025-2026
- **Population growth via immigration** has tightened housing market
- **Iceland is NOT in EU** — but EEA member; some property buying restrictions apply
- **Landfilling permits** restrictive in earthquake-prone zones
- **Brunabótamat** (fire insurance valuation) mandatory annual
- **Westfjords avalanche risk** — Flateyri, Súðavík, Neskaupstaður all had fatal events
- **Húsfélag** (building association) — read meeting minutes + financials before apt purchase

## Reddit / forum sources

- **r/Iceland** — active, English-friendly
- **r/VisitingIceland** — tourism but useful
- **r/iceland** (lower-case)
- **r/nordiccountries**
- Expat: **Iceland Review**, **Iceland Monitor**, **The Reykjavík Grapevine**

## Verification authorities

| Authority | When to call |
|---|---|
| **HMS Fasteignaskrá** | Title verification, fasteignamat |
| **Sveitarfélag** | Permits, planning, fasteignagjöld |
| **Skattur (RSK)** | Tax calculations, capital gains |
| **Veitur or local hitaveita** | Heating + water connection |
| **Almannavarnir** | Hazard zone status |
| **Veðurstofan** | Volcanic + seismic risk |
| **Húsfélagsstjórn** | If apartment building |

## Source URL templates

| Source | URL pattern |
|---|---|
| HMS Fasteignaskrá | `https://www.hms.is/` |
| Skra.is | `https://skra.is/` |
| Mbl Fasteignir | `https://www.mbl.is/fasteignir/` |
| Veðurstofan IMO | `https://www.vedur.is/` |
| Almannavarnir (Civil Protection) | `https://www.almannavarnir.is/` |
| Hagstofa (Statistics) | `https://hagstofa.is/` |
| Náttúruhamfaratryggingar (NTÍ) | `https://nti.is/` |
| Vegagerðin | `https://www.vegagerdin.is/` |
| RSK (tax) | `https://www.rsk.is/` |
| Veitur (Reykjavík utility) | `https://www.veitur.is/` |
| Reykjanes volcanic monitoring | `https://www.vedur.is/skjalftar-og-eldgos/jardskjalftar/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks (incl. live volcanic eruption series), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for HMS + Þjóðskrá + RSK (gold-standard sources); HIGH for NTÍ mandatory insurance; HIGH for Reykjanes 2023-2025 eruption series (Wikipedia, Iceland gov, Al Jazeera, CBS, ABC, Reykjanes tourism office all confirm 9 eruptions, Grindavík evacuation, "New Reykjanes Fires" framing). MEDIUM for currency-related advisories (ISK volatile).

## Extension TODOs

- [ ] Per-sveitarfélag fasteignagjöld rates
- [ ] Reykjanes volcanic risk monitoring (live eruption series)
- [ ] Foreigner buying restrictions decision tree
- [ ] Geothermal connection verification per address
- [ ] Sumarbústaður zone vs residential zone
- [ ] Currency hedging for foreign buyers (ISK volatility)
- [ ] Avalanche zone overlay (Westfjords, East fjords)
- [ ] Húsfélag financial health check rubric (apartment buildings)
- [ ] Brunabótamat verification process
- [ ] Endurgreiðsla VSK eligibility flow
