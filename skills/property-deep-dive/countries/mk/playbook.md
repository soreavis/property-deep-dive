# North Macedonia 🇲🇰 — Property Due-Diligence Playbook

ISO2: `mk`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1000` Skopje, `6000` Ohrid, `7000` Bitola, `2000` Štip)
- **Admin levels**: 8 statistical regions + 80 municipalities + Skopje (capital, special status with 10 sub-municipalities)
- **Currency**: **MKD** (Macedonian denar) — pegged to EUR at **~61.5** (highly stable)
- **Languages**: Macedonian (official); Albanian (co-official in municipalities >20% Albanian — Tetovo, Gostivar, Kičevo region)
- **Cadastre**: **AKN (Agencija za katastar na nedviznosti)**: `https://www.katastar.gov.mk/`
- **Identifier**: parcela + KO (cadastral municipality)
- **Ownership types**: pravo na sopstvenost (full ownership); etazna sopstvenost (condominium); slubuvanje (easement)
- **NATO since 2020**, **EU accession negotiations** ongoing

## Section: `--price`

### Primary sources

- **MAKSTAT (Drzaven zavod za statistika)**: `https://www.stat.gov.mk/`
- **NBRSM (National Bank)**: `https://www.nbrm.mk/` — housing market reports
- **Ministry of Finance**: `https://finance.gov.mk/`
- **FRED QMKN628BIS** for residential property
- **Investropa** — secondary aggregator

### Listing platforms

- **Reklama5**, **Pazar3**, **Skopjeshome**, **Domis.mk**
- Skopje primary market; Ohrid + Bitola secondary

### 2025-2026 price benchmarks (MAKSTAT Q4 2025)

| Region | EUR/m² (typical) | YoY |
|---|---:|---:|
| **Skopje city center (Centar)** | 1,800–2,300 | +3-5% |
| **Skopje Centar premium peak** | **2,960** (83 m² Q4 2025) | +5% |
| **Skopje Karpoš / Aerodrom** | 1,500–2,000 | +3-5% |
| **Skopje suburbs** | 900–1,400 | +2-4% |
| **Ohrid lakefront** (UNESCO buffer) | 1,800–3,500+ | +5-7% (premium) |
| **Bitola** | 700–1,100 | +2-4% |
| **Tetovo / Gostivar** (Albanian-majority) | 800–1,300 | +3-5% |
| **National YoY** | — | **+3.17% Q4 2025** (+2.89% inflation-adjusted) |

**Volume**: Skopje 304 apartments Q4 2025; Bitola 91 houses Q4 2025

### Compute

1. EUR/m² = price / **korisna povrshina** (usable area)
2. **Currency**: MKD-EUR peg 61.5 = predictable conversion
3. **Ohrid UNESCO** premium 1.5-2× over inland Bitola
4. Cross-check **AKN** cadastre data + **Reklama5/Pazar3** listings

### Key terms

- AKN = Agencija za katastar na nedviznosti
- KO = katastarska opština
- Vlasnicki list = ownership sheet (title)
- Energetski sertifikat = energy certificate
- DDV = Danok na dodadena vrednost (VAT)
- Danok na imot = property tax
- Danok na promet = transfer tax

---

## Section: `--traffic`

### Sources

- **JP za drzavni patishta**: `https://www.roads.org.mk/`
- City traffic data Skopje, Bitola, Ohrid

### Key term

**PGDS (Prosečen godišnen dneven soobrakaj)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (Skopje arterials, M-roads)
- 🔴 > 35,000 v/d (M-1 corridor, Skopje ring)

---

## Section: `--tax`

### Annual property tax — Danok na imot

- **0.10–0.20% of market value** (set per municipality)
- Typical Skopje 80m² apartment €100k: **~€100–€200/yr**
- Council of Skopje sets metro rates
- Quarterly or annual payment

### Transaction taxes

- **Danok na promet (transfer)**: **2–4%** (set by municipality / Council of Skopje)
- **DDV (VAT)**: **18% standard**; **5% reduced first-sale residential**
- **Notary fees**: ~0.5–1.0%
- **Cadastre registration**: ~0.3%

### Capital gains

- **10% PIT** (NOT 15% — common confusion); MK PIT is 10% flat
- **Exempt if ≥5 years ownership** OR **≥3 years + ≥1 year residence**

### Total transaction cost (buyer side)

- Resale: ~3-5% (2-4% transfer + 0.5-1% notary + 0.3% cadastre)
- New build: 5% VAT included + ~2-3% other costs

### Future risk

- **IMF Article IV Feb 2025**: recommends "gradually increasing property tax"
- **Skopje city tax reform** discussed (Law on the City of Skopje rate-setting)
- **Ohrid UNESCO regulation tightening**

---

## Section: `--rental`

### Long-term residential

- **Zakon za stanovanje + Zakon za zakup**
- Tenant protection moderate
- Standard 1-3 yr contracts

### Short-let (Airbnb)

- **Skopje + Ohrid**: license + tourist tax required
- **Ohrid** UNESCO restrictions tightening
- Tax: standard PIT on rental income

### Tax on rental

- Resident: 10% PIT (after 30% costs deduction = 7% effective on gross)
- Non-resident: 10% withholding

---

## Section: `--work=<profession>`

### Sources

- **AVRSM (Agencija za vrabotuvanje)**: `https://av.gov.mk/`
- **Vrabotuvanje.com**, **Mojabaza**, **LinkedIn MK**

### Self-employment

- **DOO** (limited): min MKD 5,000 capital
- **Pausalen danok** flat-rate small business
- **DDV** registration: from MKD 1M turnover

### Salary benchmarks (2025)

- Median monthly gross:
  - Skopje: ~MKD 38,000–60,000 (~€620–€975)
  - Bitola / Ohrid: ~MKD 28,000–45,000
  - Smaller cities: ~MKD 24,000–35,000
- **Minimalna plata**: ~MKD 24,000/month gross (2026) ~€390

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SUASZSM** (Seismological Observatory) | — | Seismic monitoring |
| **AKN** | `https://www.katastar.gov.mk/` | Cadastre |
| **UHMR (Uprava za hidrometeorološki raboti)** | — | Weather, hydrology |

### Specific risks

#### Earthquake — CRITICAL

- **1963 Skopje M6.1** — catastrophic event:
  - **1,070+ deaths**
  - 4,000 injured
  - 200,000 homeless
  - **80% of city destroyed**
  - Reconstructed via **Kenzo Tange masterplan**
  - **14,000+ prefab dwellings** by end 1964
  - UN aid from 78 countries
- **Ohrid + Bitola** seismic
- **Vardar valley** moderate
- **EC8 + national annex** modern code

#### Floods

- **Vardar river** (Skopje + central MK)
- 2016 Skopje flash flood (22 dead)
- Climate change increasing extreme events

#### Wildfires

- Increasing climate trend
- Macedonia mountainous + dry summer

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1963** | Pre-quake stock, mostly destroyed in Skopje |
| **1963-1970s post-quake reconstruction** | Tange-era prefab; some quality issues |
| **Yugoslav 1970s-1990** | Asbestos common; panel buildings |
| **Post-2008** | Modern seismic codes (EC8) |
| **Skopje 2014 reconstruction** | Government-led neoclassical reskinning (controversial) |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski sertifikat** | Mandatory |
| **Notar + dogovor** | Notarial deed |
| **Vlasnicki list (title sheet)** | AKN extract |

---

## Section: `--mains`

### Sources

- **JP Vodovod i kanalizacija Skopje** (Skopje water): `https://www.vodovod-skopje.com.mk/`
- Per-municipality elsewhere
- Rural: septic common

### Costs

| Scenario | Cost (EUR) |
|---|---:|
| Mains connection | 1,000–3,000 |
| Septic upgrade | 1,500–4,500 |
| Bored well | 2,500–6,000 |

---

## Cost benchmarks (MK 2026)

| Work | Cost (EUR) |
|---|---:|
| Energetski sertifikat | 100–250 |
| Notar fees | 0.5–1.0% |
| Transfer tax | 2–4% |
| **Total transaction cost (buyer)** | **~3–5%** of price |
| Roof renovation | 3,500–10,000 |
| Earthquake retrofit (older builds) | 15,000–60,000 |
| Energy retrofit | 8,000–25,000 |
| Solar PV (5kW) | 3,500–7,000 |

## Active fiscal incentives (2025-2026)

- **EU pre-accession funding** for energy retrofit
- **NATO infrastructure** investment
- **Skopje 2014 redevelopment** ongoing (controversial)

## Common listing platforms

- **Reklama5**, **Pazar3**, **Skopjeshome**, **Domis.mk**

## Caveats unique to MK

- **1963 Skopje earthquake** built much of modern Skopje (architectural significance + Tange masterplan)
- **Skopje 2014** reconstruction — controversial neoclassical reskinning of central Skopje
- **Ohrid UNESCO site** — strict construction limits, lakefront premium 1.5-2×
- **MKD-EUR peg 61.5** very stable (no FX risk for EUR holders)
- **CGT 10% with 5-year exemption** OR 3yr+1yr-resident exemption
- **PIT 10% flat** (NOT progressive) — UNIQUE in region
- **Macedonian-Albanian ethnic mix** — Tetovo + Western MK municipalities
- **NATO since 2020**, **EU candidate** since 2005 (long delays via Greece + Bulgaria veto disputes — both resolved 2018+ with Prespa Agreement)
- **Skopje air quality** winter PM2.5 severe (coal heating)
- **Vardar river floods** 2016 + climate change
- **EU pre-accession funding** for retrofit
- **Foreign-buyer freedom**: relatively open
- **Notarial system** strong
- **NBRSM** financial stability oversight

## Reddit / forum sources

- **r/macedonia** (community)
- **r/Skopje**, **r/MKD**
- **Balkan Insight**, **Macedonian Information Agency (MIA)**

## Verification authorities

| Authority | When to call |
|---|---|
| **AKN** | Title verification |
| **Notar** | Mandatory closing |
| **Lokalna samouprava** | Property tax + permits |
| **UJP (Uprava za javni prihodi)** | Tax compliance |
| **Council of Skopje** (if Skopje) | Special metro rates |

## Source URL templates

| Source | URL pattern |
|---|---|
| AKN | `https://www.katastar.gov.mk/` |
| MAKSTAT | `https://www.stat.gov.mk/` |
| NBRSM | `https://www.nbrm.mk/` |
| Ministry of Finance | `https://finance.gov.mk/` |
| Reklama5 | `https://www.reklama5.mk/` |
| Pazar3 | `https://www.pazar3.mk/` |
| UJP (tax) | `https://www.ujp.gov.mk/` |
| Vodovod Skopje | `https://www.vodovod-skopje.com.mk/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (MAKSTAT + NBRSM Q4 2025 + FRED), traffic (JP roads PGDS), tax (Danok na imot 0.10-0.20% + 2-4% transfer + 18% VAT (5% first-sale residential) + 10% CGT 5-yr OR 3yr+1yr-resident exemption), rental (license + 10% PIT), work (AVRSM + 10% flat PIT), risks (1963 Skopje M6.1 catastrophic + 2016 floods + winter air quality), mains (Skopje vodovod + per-municipality).
**Confidence**: HIGH for 1963 Skopje earthquake reference (1,070+ deaths, 80% destruction, Tange masterplan, 14k prefabs); HIGH for MKD-EUR peg 61.5; HIGH for CGT 10% (NOT 15%) with proper exemption rules; HIGH for AKN centralized cadastre; MEDIUM for IMF property tax recommendations (Feb 2025 Article IV); MEDIUM for "Skopje 2014" reconstruction controversy framing.

## Extension TODOs

- [ ] Per-municipality property tax + transfer tax rates table
- [ ] Skopje 10 sub-municipalities specific rates
- [ ] Ohrid UNESCO construction limits + buffer zone
- [ ] Tetovo / Gostivar Albanian-majority specifics
- [ ] CGT 5-year vs 3yr+1yr-resident exemption decision tree
- [ ] 1963 quake-zone overlay vs post-2008 EC8 builds
- [ ] Skopje 2014 reconstruction inventory
- [ ] Skopje winter air quality mitigation
- [ ] Vardar river flood-zone overlay
- [ ] EU accession reforms timeline (Bulgaria veto resolution)
