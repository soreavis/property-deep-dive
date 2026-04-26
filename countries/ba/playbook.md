# Bosnia and Herzegovina 🇧🇦 — Property Due-Diligence Playbook

ISO2: `ba`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`71000` Sarajevo, `78000` Banja Luka, `88000` Mostar, `75000` Tuzla)
- **DUAL-ENTITY STATE** (post-Dayton 1995):
  - **Federacija BiH (FBiH)** — Bosniak + Croat majority; 10 cantons
  - **Republika Srpska (RS entity)** — Serb majority
  - **Brčko District** — separate self-governing
- **Currency**: **BAM (Konvertibilna marka)** — pegged to EUR at **1 EUR = 1.95583 BAM** via currency board (since 1998); EXTREMELY stable
- **Languages**: Bosnian, Croatian, Serbian (all three official)
- **Cadastre — DUAL ENTITY**:
  - **FBiH**: Federalna uprava za geodetske i imovinsko-pravne poslove `https://fgu.com.ba/en/`
    - Public portal: `https://katastar.ba/`
    - Geoportal: `https://www.katastar.ba/geoportal`
    - 79 FBiH municipalities, centralized DB Sarajevo
  - **RS entity**: **RGURS** (Republička uprava za geodetske i imovinsko-pravne poslove) `https://www.rgurs.org/sr-lat`
    - eKatastar: `https://ekatastar.rgurs.org/`
    - Geoportal: `https://geoportal.rgurs.org/`
    - HQ Banja Luka, 48 regional units, 16 regional offices
  - **Brčko District**: separate (less digitized)
- **Identifier**: parcela + KO + entity selector (CRITICAL — must specify FBiH/RS-entity/Brčko)
- **EU candidate** since Dec 2022 (post-Dayton legacy slows reforms)

## Section: `--price`

### Primary sources

- **CBBH (Centralna banka BiH)**: `https://www.cbbh.ba/` — Financial Stability Reports
- **Agencija za statistiku BiH (BHAS)**: `https://www.bhas.ba/`
- **Entity statistics**: Federalni zavod za statistiku FBiH + Republički zavod za statistiku RS
- **Global Property Guide**, **Investropa** — secondary aggregators

### Listing platforms

- **Olx.ba**, **Sasomange.ba**, **Nekretnine.ba**, **Pojdimo.ba**
- Sarajevo + Banja Luka primary markets

### 2024-2025 price benchmarks (Global Property Guide)

| Region | EUR/m² (avg new build) | YoY |
|---|---:|---:|
| **Sarajevo (FBiH)** | 1,980 (2024); 2025 €1,280–€1,550 new / €900–€1,200 secondary | +7.6% |
| **Banja Luka (RS entity)** | **1,991** new build | **+9.5%** |
| **Mostar (FBiH)** | **1,179** | **+27.2%** (strongest growth) |
| 2025 Mostar: €660–€850 new / €500–€700 secondary | | |
| **Tuzla (FBiH)** | 700–1,100 | +5-7% |
| **Bijeljina (RS entity)** | 600–900 | +5% |
| **Zenica (FBiH)** | 700–1,000 | +5% |

### Compute

1. EUR/m² = price / **korisna površina** (usable area)
2. **Currency**: BAM-EUR peg 1.95583 = predictable conversion (no FX risk)
3. **Cross-check entity**: FBiH vs RS entity has DIFFERENT taxes/laws
4. Cross-check **Olx.ba** asking + **CBBH** index

### Key terms

- BAM = Konvertibilna marka (pegged to EUR)
- FBiH = Federacija Bosne i Hercegovine
- RS entity = Republika Srpska entitet
- KO = katastarska opština
- Energetski certifikat = energy certificate
- ZK izvadak = land register extract

---

## Section: `--traffic`

### Sources

- **Federalni hidrometeorološki zavod**, **Direkcija cesta FBiH**, **JP Putevi RS**
- Sarajevo + Banja Luka city traffic data

### Key term

**PGDS (Prosječan godišnji dnevni saobraćaj)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional, urban side streets)
- 🟠 10,000–35,000 v/d (Sarajevo arterials, M-roads)
- 🔴 > 35,000 v/d (autoput A1, Sarajevo ring)

---

## Section: `--tax`

### Annual property tax — DUAL ENTITY DIFFERENT SYSTEMS

#### FBiH (Federacija)

- **BAM 0.5–3 per m²** (FLAT per-sqm, NOT percentage)
- Set by canton/municipality
- Typical Sarajevo apartment: BAM 50–250/yr (~€25–€130)

#### RS entity

- **0.2% of market value** (percentage-based, unlike FBiH)
- Typical Banja Luka apartment €100k: ~€200/yr

### Transaction taxes — MAJOR DIVERGENCE

| Tax | FBiH | RS entity |
|---|---|---|
| **Transfer tax (porez na promet nepokretnosti)** | **0.05–5%** (varies by municipality) | **0% — NO transfer tax** |
| **VAT (PDV)** | 17% on first-sale new builds | 17% |
| **Notary fees** | ~0.5–1.5% | ~0.5–1.5% |

**VAT 17%** = lowest in Europe (one of); applies to first-sale new builds only

### 2024 VAT refund reform (FBiH)

- **First-time buyers** can refund **17% VAT** on new residential up to **40 m² (+15 m² per household member)**
- Adopted FBiH House of Representatives late 2024
- Major Sarajevo + Mostar construction boost

### Capital gains — DUAL ENTITY DIFFERENCE

| Entity | CGT |
|---|---|
| **FBiH** | **NOT taxable for individuals** (UNIQUE) |
| **RS entity** | **13%** |

### Total transaction cost (buyer side)

- FBiH resale: ~2-7% (depends on cantonal transfer tax 0.05-5%)
- RS entity resale: ~1.5-2.5% (no transfer tax — significant savings)
- New build: 17% VAT in price + ~2% other costs

### Future risk

- EU accession reforms may align entities (slowly)
- Sarajevo VAT refund reform expanding

---

## Section: `--rental`

### Long-term residential

- Tenancy laws differ by entity
- FBiH cantonal variation
- Tenant protections moderate

### Short-let

- **Sarajevo + Mostar**: registration required, low enforcement
- **Mostar UNESCO** stricter
- 2026 Slovenia/Croatia-style consent rules **not confirmed** for BA

### Tax on rental

- Resident: marginal income tax
- Non-resident: 10% withholding (FBiH) / 13% (RS entity)

---

## Section: `--work=<profession>`

### Sources

- **JU Služba za zapošljavanje FBiH** + **JU Zavod za zapošljavanje RS**
- **Posao.ba**, **Olx Posao**, **Kolektiv**, **LinkedIn BA**

### Self-employment

- **Obrt** (sole trader)
- **D.o.o.** (limited): min capital 1 BAM in some cantons
- **PDV** registration: from BAM 50,000 turnover

### Salary benchmarks (2025)

- Median monthly gross:
  - Sarajevo: ~BAM 1,800–2,800 (~€920–€1,430)
  - Banja Luka: ~BAM 1,500–2,400
  - Smaller cities: ~BAM 1,200–1,800
- **Minimum wages**: BAM 619 FBiH / BAM 750 RS entity (2026)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Seizmološki zavod RS** | — | Seismic monitoring |
| **Federalni meteorološki zavod** | — | Weather, climate |
| **BHMAC (Mine Action Centre)** | `https://www.bhmac.org/` | **Mine contamination from 1992-95 war** |

### Specific risks

#### Earthquake

- **1969 Banja Luka M6.6** (catastrophic, ~20 dead, major damage)
- Regular minor quakes
- Sarajevo + Banja Luka moderate seismic
- **Mostar/Herzegovina** lower

#### Floods

- **2014 catastrophic floods**: Sava + Bosna rivers (same Tamara/Yvette cyclone as Serbia, 120-year heaviest rainfall)
- Major damage RS entity + parts FBiH

#### Mine contamination — UNIQUE

- **Legacy from Yugoslav Wars 1992-1995**
- **Republika Srpska + Federation** rural areas affected
- **BHMAC verification mandatory** for rural/peri-urban properties
- Insurance + mortgage may require demining certificate

#### Other

- **Landslides**: Bosnian highlands
- **Wildfires**: Herzegovina karst
- **Air quality**: Sarajevo + Tuzla winter (coal heating)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **Yugoslav 1945-1990** | Asbestos common, panel buildings |
| **War-damaged 1992-1995** | **Reconstruction quality variable**; some "fast rebuild" structures problematic |
| **Post-2000** | Improved codes; EU funding driving modernization |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski certifikat** | Mandatory |
| **Notar + ugovor (entity-specific notary law)** | Mandatory |
| **ZK izvadak** (land register extract) | Title verification |
| **Demining certificate (rural)** | Where applicable; BHMAC |

---

## Section: `--mains`

### Sources

- **Vodovod per municipality**: Sarajevo (KJKP Vodovod i kanalizacija), Banja Luka, Mostar all separate
- **Many post-war repairs ongoing** — infrastructure variable
- Rural: septic + cesspits common

### Costs

| Scenario | Cost (EUR) |
|---|---:|
| Mains connection | 1,500–5,000 |
| Septic upgrade | 2,500–6,000 |
| Bored well | 3,000–8,000 |

---

## Cost benchmarks (BA 2026)

| Work | Cost (EUR) |
|---|---:|
| Energetski certifikat | 100–250 |
| Notar fees | 0.5–1.5% |
| Transfer tax (FBiH) | 0.05–5% (varies) |
| Transfer tax (RS entity) | **0%** |
| **Total transaction cost (FBiH)** | **~2–7%** of price |
| **Total transaction cost (RS entity)** | **~1.5–2.5%** |
| Roof renovation | 3,500–10,000 |
| Demining (rural property) | 5,000–25,000+ |
| War-damage retrofit | varies massively |
| Energy retrofit | 8,000–25,000 |

## Active fiscal incentives (2025-2026)

- **2024 VAT refund reform** for first-time FBiH buyers (17% on first 40 m²)
- **EU pre-accession funding** (post-candidate-status Dec 2022)
- **2025-2027 EU-aligned economic reform programme** (adopted Sept 2025)
- **Sarajevo construction boom** post-VAT-refund

## Common listing platforms

- **Olx.ba** — DOMINANT
- **Sasomange.ba**, **Nekretnine.ba**, **Pojdimo.ba**

## Caveats unique to BA

- **DUAL-ENTITY STATE**: FBiH vs RS entity have **different cadastres, different taxes, different laws** — must specify entity throughout DD
- **Brčko District** separate (less digitized)
- **Currency BAM** pegged to EUR 1.95583 via currency board (1998+) — extremely stable
- **17% VAT** = lowest in Europe
- **FBiH transfer tax 0.05-5%** (cantonal) vs **RS entity NO transfer tax (0%)** — major divergence
- **FBiH CGT not taxable for individuals** (UNIQUE) vs **RS entity 13%**
- **Mine contamination from Yugoslav Wars 1992-1995** — verify BHMAC for rural properties
- **2014 floods** Sava + Bosna rivers (massive event)
- **EU candidate Dec 2022** — slow reform pace
- **2024 VAT refund** for FBiH first-time buyers (40 m² + 15 m² per family member)
- **2025 EU-aligned reforms** programme adopted
- **Banja Luka 1969** earthquake reference (M6.6)
- **Mostar UNESCO** Old Bridge area = strict construction
- **Foreign-buyer freedom**: relatively open (no reciprocity barriers)
- **Sarajevo Stari Grad** UNESCO buffer
- **War-damaged properties** require careful inspection

## Reddit / forum sources

- **r/bosnia**, **r/Sarajevo**, **r/BanjaLuka**
- **Balkan Insight**, **Sarajevo Times**, **Banja Luka News**

## Verification authorities

| Authority | When to call |
|---|---|
| **FBiH Federalna uprava** or **RGURS (RS)** | Title verification (entity-specific) |
| **Notar** | Mandatory closing (entity-specific notary law) |
| **Općina/opština** | Local tax + permits |
| **BHMAC** | If rural — demining verification |
| **Poreska uprava** entity | Tax compliance |
| **Etažni zajednički predstavnik** | If apartment building |

## Source URL templates

| Source | URL pattern |
|---|---|
| FBiH cadastre | `https://fgu.com.ba/en/` |
| FBiH public portal | `https://katastar.ba/` |
| FBiH geoportal | `https://www.katastar.ba/geoportal` |
| RS entity cadastre | `https://www.rgurs.org/sr-lat` |
| RS entity eKatastar | `https://ekatastar.rgurs.org/` |
| RS entity geoportal | `https://geoportal.rgurs.org/` |
| CBBH | `https://www.cbbh.ba/` |
| BHAS (statistics) | `https://www.bhas.ba/` |
| BHMAC (mine action) | `https://www.bhmac.org/` |
| Olx.ba | `https://olx.ba/nekretnine` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (CBBH + BHAS + GPG 2024-2025), traffic (entity divisions), tax (DUAL ENTITY: FBiH BAM 0.5-3/m² + 0.05-5% transfer + 17% VAT first-sale + CGT NOT TAXABLE individuals; RS entity 0.2% market value + 0% transfer + 17% VAT + 13% CGT), rental (entity-specific), work (entity-specific), risks (Banja Luka 1969 + 2014 Sava+Bosna floods + BHMAC mine contamination + war-damage), mains.
**Confidence**: HIGH for BAM-EUR peg 1.95583 currency board; HIGH for entity divergence (FBiH vs RS taxes); HIGH for mine contamination as ongoing diligence concern; HIGH for 2024 VAT refund reform; MEDIUM for "Russian buyer ban" claims (could not verify English-language source); MEDIUM for cantonal transfer tax 0.05-5% (varies by canton).

## Extension TODOs

- [ ] Cantonal transfer tax table (FBiH 10 cantons)
- [ ] BHMAC demining verification flow per parcel
- [ ] War-damage assessment rubric
- [ ] FBiH cantonal property tax (BAM 0.5-3/m²) per canton
- [ ] RS entity property tax (0.2% market) verification
- [ ] Brčko District separate process documentation
- [ ] CGT optimization: FBiH (no CGT individuals) vs RS entity (13%)
- [ ] 2024 VAT refund eligibility for first-time FBiH buyers
- [ ] Sarajevo + Mostar UNESCO construction limits
- [ ] EU candidate accession reforms tracker
