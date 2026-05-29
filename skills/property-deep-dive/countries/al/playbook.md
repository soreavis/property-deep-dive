# Albania 🇦🇱 — Property Due-Diligence Playbook

ISO2: `al`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1001` Tirana, `2001` Durrës, `9401` Vlorë, `9701` Sarandë)
- **Admin levels**: 12 qarqe (counties) + 61 bashki (municipalities)
- **Currency**: **ALL** (Albanian lek) — floating (BoA inflation-targeting), 2023-2025 range EUR/ALL ~98–110 (NOT pegged; see Caveats)
- **Languages**: Albanian (official); Greek minority (south coast); Italian + English widely used in business
- **Cadastre**: **ASHK (Agjencia Shtetërore e Kadastrës)** — `https://www.ashk.gov.al/`
  - **e-Albania portal**: `https://e-albania.al/` (applications via service code 9473)
  - **iKadaster**: `https://kadaster.al/en/` — World Bank-supported registration program
  - **ASIG Geoportal**: `https://geoportal.asig.gov.al/en` — national spatial data
- **Identifier**: parcela + ZK (zona kadastrale) + nr. pasurie (property number)
- **EU candidate** since 2014; **negotiations advancing** 2024-2026
- **2025-2026 milestone**: target **fully digital cadastre by end of 2026**

## Section: `--price`

### Primary sources

- **INSTAT (National Statistics)**: `https://www.instat.gov.al/` — Housing Price Index
- **Bank of Albania**: `https://www.bankofalbania.org/` — Fischer HPI; Financial Stability Reports

### Listing platforms

- **MerrJep**: `https://www.merrjep.al/`
- **Realting.com/albania**
- **AlbaniaProperties**, **VivaAlbania**, **Real Estate Albania** — secondary
- Tirana primarily; coastal markets Durrës, Vlorë, Sarandë growing

### 2025-2026 price benchmarks (INSTAT + BoA)

| Region | EUR/m² (typical) | YoY |
|---|---:|---:|
| **National** | — | **+18% (Jan 2025–Jan 2026)** |
| **National peak** | — | **+41.7% YoY peak** early 2025 (moderating) |
| **Tirana center (Bllok, Komuna e Parisit)** | 1,800–3,500 | +14-22% |
| **Tirana suburbs** | 800–1,500 | +12% |
| **Durrës (port)** | 1,000–1,400 | moderating |
| **Vlorë (coast)** | 1,000–2,200 | **+25-58% YoY** (Vlora airport-anticipation effect — airport DELAYED to mid-2026 per Dec 2025 PM statement) |
| **Sarandë (Adriatic)** | 1,500–2,800+ | **+25-58% YoY** speculative |
| **Sarandë 1-bed apt** | €150,000–200,000 | high |
| **Shkodër** | 600–1,200 | +5-10% |
| **Korçë** | 600–1,000 | +5% |

### Compute

1. EUR/m² = price / **sipërfaqe banimi** (residential area)
2. **Currency volatility** ALL fluctuates 5-15% vs EUR
3. **Cross-check**: ASHK extract + MerrJep asking + BoA Fischer HPI
4. **Adriatic coast booming** (Sarandë especially) — speculative

### Key terms

- ASHK = Agjencia Shtetërore e Kadastrës
- ZK = zona kadastrale
- Nr. pasurie = property number
- Çertifikatë e pronësisë = ownership certificate
- Çertifikatë energjetike = energy certificate
- Akti notarial = notarial deed
- DIVA = Albanian digital tax platform (NEW 2026)

---

## Section: `--traffic`

### Sources

- **ARRSH (Autoriteti Rrugor Shqiptar)**: `https://www.arrsh.gov.al/`
- City traffic data Tirana

### Key term

**Trafiku mesatar ditor (TMD)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (Tirana arterials, A1 corridor)
- 🔴 > 35,000 v/d (Tirana ring, Rinas airport corridor)

---

## Section: `--tax`

### Annual property tax — Tatim mbi pasurinë e paluajtshme

- **0.05 % of cadastral / reference value** for **residential** apartments / dwellings (post-2018 reform)
- **0.2 % of cadastral / reference value** for **commercial / business-use** property (post-2018 reform) *(2026-05-27 verified, source Tax-Checker AL + ALTAX + HLB)*
- Cadastral / reference value per m² set by Cadastre Office (ASHK); collected via water bill in most bashki
- Typical Tirana apartment: ~€50–€150/yr est. (very low) — derived from the 0.05 % rate × cadastral/reference value above; verify cadastral value per m² with ASHK
- (The ALL 100–2,000/m² fixed-fee figure belongs under transfer taxes for commercial buildings, NOT this annual tax — see Transaction taxes below)

### Personal income tax (PIT) framework — post-2024 reform (Law 29/2023)

Progressive employment-income brackets, in force from 1 January 2024:

| Annual employment income | Rate |
|---|---:|
| Up to ALL 600,000 (~€5,940) | **0 %** |
| ALL 600,001 – ALL 3,000,000 (~€29,700) | **13 %** |
| Above ALL 3,000,000 | **23 %** |

Flat-rate carve-outs for property-relevant income: **rental 15 %**, **CGT 15 %**, **dividends 8 %**. Cite Law 29/2023 + [tatime.gov.al](https://www.tatime.gov.al/eng/c/4/96/108/tax-on-personal-income). *(2026-05-27 verified, source PwC + tatime.gov.al + Eurofast Tax Card 2025)*

### Transaction taxes

| Tax | Residential | Commercial |
|---|---|---|
| **Transfer (one-time)** | **2 % of sale price** for individuals | **ALL 100 – ALL 2,000/m²** fixed fee (municipality-set + building-class) |
| **Annual property tax** | 0.05 % cadastral | 0.2 % cadastral |
| **Capital gains (PIT)** | 15 % on profit | 15 % on profit |

- **TVSh (VAT)**: **20 % standard**. **0 % on newly built residential** sold by the developer (zero-rated supply, no VAT for new-apartment buyer). **No VAT on second-hand residential resales between individuals** (only 2 % transfer + 15 % CGT apply). Commercial supplies → 20 % standard *(2026-05-27 verified, source PwC + tatime.gov.al + Folie Village)*
- **Family transfers**: exempt
- **Notary**: sliding scale per Chamber of Notaries tariff — **0.35 %** (€714–€43k) / **0.30 %** (€43k–€107k) / **0.28 %** (€107k–€357k) / **0.25 %** (€357k–€714k) / **0.23 %** (>€714k); plus stamp duty up to ALL 1,000 (~€10). Typical €200 k Tirana apartment → notar fee ~€560 (0.28 %) *(2026-05-27 verified, source Access Albania + Eurofast)*
- **Legalization fees** if title needs regularization (variable)

### One-time property revaluation window (eff. 1 Jan 2026 – 31 Dec 2026)

- **Law 85/2025 "Për rivlerësimin e pasurisë së paluajtshme"** opens a 12-month window during which individuals and businesses may revalue immovable property to market value, paying **5 % tax on the uplift** between previous registered value and new market value
- Finance Minister Malaj clarified the 5 % rate applies specifically to **newly built residential** (verify final regulation before assuming broader scope)
- **Material for any seller carrying a low-historical-cost basis**: revaluing now at 5 % means the future 15 % CGT is computed off the newer (higher) basis *(2026-05-27 verified, source HLB Albania + Balkanweb + RTSH)*

### Total transaction cost (buyer side)

- Resale: ~3-5% (transfer tax + notary + legalization checks)
- New build: 20% VAT in some cases + ~3% other costs
- **Note**: actual rates highly municipality-dependent + legalization-status-dependent

### Property-tax reform timeline (2026-2030)

- **End-2026**: all bashki integrated into Fiscal Cadastre System (mandatory)
- **2026-2027**: transition period for market-based property valuation
- **2027**: nationwide property assessment / valuation
- **2028**: market-based valuations for buildings + tax-rate adjustments + exemptions structure introduced
- **2030**: land-tax rollout via fully integrated EU-model system
- Revenue target: lift property tax from 0.3 % → 1 % of GDP by 2028 *(2026-05-27 verified, source Albanian Times + ALTAX + HLB)*

### Future risk

- **NEW 1 Jan 2026 DIVA platform**: short-term rental income must be declared via Albanian digital tax system (15% flat tax). Pre-DIVA pressure: from **1 November 2025**, Booking.com hosts must either declare NIPT or pay **20 % VAT on the platform commission** — driving hosts onto NIPT or off Booking
- **Council of Ministers Decision 153/2026 (11 Mar 2026)**: accommodation-structure certification conditions for tourism beach stations
- **iKadaster fully digital end-2026**

---

## Section: `--rental`

### Long-term residential

- **Kodi Civil**
- Tenant protection moderate
- Standard 1-3 yr contracts

### Short-let (Airbnb) — MAJOR NEW REFORM 2026

**1 Jan 2026 DIVA platform**:
- Short-term rental income **must be declared via DIVA** (Albanian digital tax system)
- **No NIPT (business tax number) required for individuals**
- **15% flat tax** on rental income
- Penalties for underreporting

**Tourism license + classification** under Tourism Ministry rules (March 2026 decision 153)

### Tax on rental

- 15% flat tax on rental income (DIVA declared)
- 15% withholding non-residents

---

## Section: `--work=<profession>`

### Sources

- **ZK (Zyra e Punësimit) / SHKP (Shërbimi Kombëtar i Punësimit)**: `https://www.shkp.gov.al/`
- **Duapune.al**, **njofta.com**, **MerrJep Punë**, **LinkedIn AL**

### Self-employment

- **Person Fizik Tregtar** (sole trader)
- **Sh.p.k.** (limited): min ALL 100 capital
- **TVSh** registration: from ALL 10M turnover

### Salary benchmarks (2025)

- Median monthly gross:
  - Tirana: ~ALL 75,000–130,000 (~€720–€1,250)
  - Durrës: ~ALL 60,000–100,000
  - Smaller cities: ~ALL 45,000–75,000
- **Minimum wage**: ALL 40,000/month (~€385) (2025)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **IGEWE** (Institute of Geosciences, Energy, Water and Environment) | — | Seismic, hydromet, energy |
| **INSTAT** | `https://www.instat.gov.al/` | Hazard/event statistics |

### Specific risks

#### Earthquake — CRITICAL

- **2019 Durrës M6.4 earthquake**: 51 dead, **€985m losses (~7.5% of 2018 GDP)**, residential damage extensive
- **Vore fault near Tirana** flagged for **future seismic hazard** by post-event studies
- **Albanian Alps** ongoing seismic
- **Coastal Adriatic** moderate seismic

#### Floods

- **Shkumbin, Mat, Drin** rivers
- **Lake Shkodër** + hydropower risks
- **Coastal storm + sea-level rise** (Adriatic)

#### Mine contamination

- Less than BA, but post-Communist era **legacy remains in some rural areas**
- Inspect rural properties

#### Karst hazards

- **Albanian Alps** karst
- Sinkholes, drainage

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990 (Communist era)** | Asbestos common, dated systems, weak insulation, panel buildings |
| **1990s-2010s informal construction** | **No permits, structural quality variable**; legalization process required |
| **Post-2010** | Improving codes |
| **Post-2019 quake** | EC8 mandatory, rebuilding standards strict |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Çertifikatë energjetike** | Mandatory |
| **Akti notarial** | Notarial deed mandatory |
| **Çertifikatë e pronësisë** (ASHK) | Ownership certificate; via e-Albania |
| **Legalization status verification** | Critical for 1990s-2010s builds |

---

## Section: `--mains`

### Sources

- **UKT (Ujësjellës Kanalizime Tirana)**: `https://www.ukt.al/` — capital
- Per-municipality water/sewer companies elsewhere
- Rural: **septic + cisterna** very common

### Costs

*est. — indicative cost bands; varies by bashki and distance to network. Verify with local quotes.*

| Scenario | Cost (EUR) |
|---|---:|
| Mains connection | ~800–2,500 |
| Septic + cisterna | ~1,500–4,500 |
| Bored well | ~2,500–6,000 |

---

## Cost benchmarks (AL 2026)

*Renovation/build rows are est. — indicative cost bands, verify with local contractor quotes.*

| Work | Cost (EUR) |
|---|---:|
| Çertifikatë energjetike | ~80–250 |
| Notar fees | ~1.0% |
| Transfer tax / CGT | ~2% reference value + 15% on profit |
| Realtor commission | 2-3% per side typical |
| **Total transaction cost (buyer)** | **~3–5%** of price |
| Roof renovation | ~2,500–8,000 |
| Earthquake retrofit (post-2019) | ~12,000–50,000 |
| Energy retrofit | ~6,000–20,000 |
| Solar PV (5kW) | ~3,000–6,000 |
| Legalization fees (informal builds) | varies massively |

## Active fiscal incentives (2025-2026)

- **EU accession sprint**: all 33 negotiating chapters opened by 17 Nov 2025 (Clusters 1-6 in 13 months); **IBAR adopted by COELA 21 May 2026**; IGC marking final phase 26 May 2026; government targets conclusion 2027 + membership 2030 (Commission estimate ~2029) — **fastest accession sprint in EU history**, material for 5-10-yr exit modelling *(2026-05-27 verified, source Consilium + European Western Balkans + Balkan Insight)*
- **EU pre-accession funding** for energy retrofit + infrastructure
- **Vlora International Airport — DELAYED**: construction largely complete but certification + shareholder dispute have pushed opening; PM Rama stated **mid-2026** target (Dec 2025) with no summer-2026 flights scheduled, charter contracts cancelled, 2A Group consortium in legal dispute, extension request to September 2026. Property-value impact already booked into 2024-2025 Sarandë/Vlorë +25–58 % YoY surge — further upside conditional on actual opening *(2026-05-27 verified, source SeeNews + Albanian Daily News + CAPA + Two Continents)*
- **One-time 5 % property revaluation window 1 Jan – 31 Dec 2026** (Law 85/2025 — Rivlerësimi i pasurisë së paluajtshme); 5 % tax on uplift between previous registered value and new market value — material for sellers carrying low-historical-cost basis *(2026-05-27 verified, source HLB Albania + Balkanweb + RTSH)*
- **Strategic Investor Status (Statusi i Investitorit Strategjik, eff. through 31 Dec 2026)** — Law on Strategic Investments 2015 amended Jan 2025 to extend deadline; ≥ **EUR 5,000,000** in tourism creating ≥ **80 new jobs** (lower thresholds for energy/agriculture); fast-track AIDA channel; **access to state-owned immovable property for symbolic EUR 1** for up to **99 years**; 60+ approved projects, > €3.09 bn committed, > 17,000 jobs *(2026-05-27 verified, source Oracle Law Global + UNCTAD Investment Laws Navigator + US State 2025 ICS)*
- **iKadaster fully digital end-2026** — World Bank-supported
- **Tirana 2030 Master Plan** + city redevelopment
- **Massive EU-funded infrastructure** (highways, airports, ports)

## Common listing platforms

- **MerrJep**, **Realting.com/albania**
- **AlbaniaProperties**, **VivaAlbania**, **Real Estate Albania**

## Caveats unique to AL

- **Title legalization risk CRITICAL**: many properties built without permits 1990-2010s
- **Buyer must verify legalization status** — do not assume valid title
- **2021-2024**: 347 de-legalization decisions in Tirana, **656 nationally**
- **Legalization narrowing not expanding** (protected areas, coastline buffers, public land **no longer eligible**)
- **NEW 1 Jan 2026 DIVA platform**: STR income mandatory declaration + 15% flat tax
- **Vlora International Airport — DELAYED** (mid-2026 target per Dec 2025 PM Rama statement; certification + shareholder dispute pending; no summer-2026 flights scheduled — see Active fiscal incentives)
- **iKadaster fully digital cadastre** target end of 2026 (World Bank program)
- **2019 Durrës M6.4 earthquake**: €985m losses (~7.5% of 2018 GDP); residential damage extensive
- **Vore fault near Tirana** — future seismic hazard flagged
- **Tirana Bllok premium** (former Communist Party district = trendy upscale)
- **Adriatic coast booming** (Sarandë +25-58% YoY) — speculative
- **Currency ALL** — **floating** (BoA inflation-targeting); 2023-2025 range EUR/ALL ~98–110 with secular ALL appreciation (`leku i fortë`). 5–15 % FX volatility vs EUR realistic. Buyer carries FX risk if income is in EUR. (NOT pegged.)
- **Foreign-buyer rules — Ligji 7980/1995 "Për shitblerjen e trojeve"** *(2026-05-27 verified, source Investropa + Vivaview + Alba Legal)*:
  - **Apartments / houses / commercial buildings**: foreigners own outright, identical rights to Albanian citizens
  - **Agricultural land**: prohibited for direct foreign ownership; workaround = Albanian Sh.p.k. company (€500-1,000 setup, ~2 weeks) OR long-term lease (up to 99 years)
  - **Construction land** (urban building plots): only purchasable when linked to a building investment whose value is **at least 3× the land value** ("3x rule" per Ligji 7980)
  - **Coastal land within 200 m of Adriatic/Ionian shoreline**: special restrictions; foreign buyer typically uses SPV / Albanian company
- **EU accession sprint** — all 33 chapters opened by Nov 2025; IBAR adopted 21 May 2026; target conclusion 2027, membership 2030 (Commission ~2029)
- **Family transfers exempt** from transfer tax
- **Pre-1990 panel buildings + 1990s-2010s informal construction** = main due-diligence concerns
- **e-Albania portal** for cadastre extracts (service code 9473)

## Reddit / forum sources

- **r/albania**, **r/Tirana**
- **Balkan Insight**, **Albania Daily News**, **Tirana Times** (English)
- **Citizens.al** (legalization tracking)

## Verification authorities

| Authority | When to call |
|---|---|
| **ASHK** | Title verification + legalization status |
| **e-Albania** | Online cadastre extract |
| **Notar** | Mandatory closing |
| **Bashki** (municipality) | Property tax + permits |
| **DPT (Drejtoria e Përgjithshme e Tatimeve)** | Tax compliance + DIVA |
| **Ministria e Turizmit** | If short-let |
| **IGEWE** | Hazard zone status |

## Source URL templates

| Source | URL pattern |
|---|---|
| ASHK | `https://www.ashk.gov.al/` |
| e-Albania (cadastre service) | `https://e-albania.al/` |
| iKadaster | `https://kadaster.al/en/` |
| ASIG Geoportal | `https://geoportal.asig.gov.al/en` |
| INSTAT | `https://www.instat.gov.al/` |
| Bank of Albania | `https://www.bankofalbania.org/` |
| MerrJep | `https://www.merrjep.al/` |
| ARRSH (roads) | `https://www.arrsh.gov.al/` |
| UKT (Tirana water) | `https://www.ukt.al/` |
| DPT (tax) | `https://www.tatime.gov.al/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (INSTAT + BoA Fischer HPI 2025-26), traffic (ARRSH), tax (Tatim 0.05% cadastral apartments + ~2% transfer reference + 20% VAT + 15% CGT + DIVA STR Jan 2026), rental (DIVA platform NEW Jan 2026 + 15% flat), work (SHKP), risks (2019 Durrës M6.4 €985m losses + Vore fault + Albanian Alps karst), mains (UKT + per-bashki).
**Last verified**: 2026-05-27.
**Confidence**: HIGH for ASHK + iKadaster + e-Albania (World Bank-backed); HIGH for 2019 Durrës earthquake reference + losses; HIGH for DIVA STR 1 Jan 2026 + 15 % flat tax (HLB Albania confirmed); HIGH for property tax 0.05 % residential / 0.2 % commercial split (post-2018 reform); HIGH for PIT 0/13/23 % framework (Law 29/2023); HIGH for foreign-buyer Ligji 7980/1995 (apartments OK / agri prohibited / construction-land 3× rule / 200 m coastal); HIGH for EU accession (all 33 chapters opened, IBAR 21 May 2026); HIGH for Strategic Investor Status (EUR 5M + 80 jobs + €1 state land); HIGH for 5 % revaluation window 1 Jan – 31 Dec 2026 (Law 85/2025); MEDIUM for Vlora airport status (in flux — revisit quarterly); MEDIUM for legalization process specifics (system changing).

## Extension TODOs

- [ ] Per-bashki property tax + transfer tax rates table
- [ ] Legalization status verification flow (informal 1990s-2010s builds)
- [ ] De-legalization risk per protected zone (656 nationally)
- [ ] Vlora airport corridor speculative zones
- [ ] DIVA platform integration + STR declaration workflow
- [ ] iKadaster digital migration tracker (end-2026 target)
- [ ] Vore fault seismic zone overlay (Tirana future risk)
- [ ] Tirana 2030 Master Plan zoning changes
- [ ] EU candidate accession reforms timeline
- [ ] Albanian Riviera (Sarandë + Vlorë) +25-58% YoY tracking
