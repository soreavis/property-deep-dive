# Greece 🇬🇷 — Property Due-Diligence Playbook

ISO2: `gr`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`105 57` Athens centro, `546 24` Thessaloniki, `711 10` Heraklion)
- **Admin levels**: 13 περιφέρειες (regions) + 332 δήμοι (municipalities) + 122 περιφερειακές ενότητες (regional units)
- **Currency**: EUR (€) — adopted 2002
- **Languages**: Greek (official); English widely used in tourism/business
- **Cadastre**: **Ktimatologio (Hellenic Cadastre, Ελληνικό Κτηματολόγιο)**: `https://www.ktimatologio.gov.gr/` — parcel-based system with **KAEK unique parcel numbers**
- **Identifier**: KAEK (12-digit cadastral ID per parcel)
- **Ownership types**:
  - **Πλήρης κυριότητα** (full ownership)
  - **Ψιλή κυριότητα + επικαρπία** (bare ownership + usufruct)
  - **Συγκυριότητα** (co-ownership)
  - **Διαμέρισμα + κοινόχρηστα** (apartment + commons)

## Section: `--price`

### Primary sources

- **Ktimatologio (Hellenic Cadastre)**: `https://www.ktimatologio.gov.gr/`
  - **Status (2025-2026)**: 60% complete; full activation slipped from Nov 2025 to **2026**
  - 201 of 392 legacy mortgage offices closed in 2024
  - Free 24-hr search of registered parcels
  - Buyer requests **Apospasma Ktimatologikou Diagrammatos** (cadastral excerpt) + **Ktimatologiko Fyllo** (property sheet)
- **gov.gr digital property registry** (launched 2025): `https://www.gov.gr/en/ipiresies/periousia-kai-phorologia/ktematographese`
  - Integrates cadastre + tax + utility + forestry + energy data
- **Bank of Greece RPPI** (the authoritative price index): `https://www.bankofgreece.gr/en/statistics/real-estate-market`
  - Quarterly index built from ~951k bank valuations
  - **Q3 2025**: apartments +7.7% YoY (Athens +6.6%, Thessaloniki +9.6%, other cities +8.9%, other areas +8.5%)
- **ELSTAT (Hellenic Statistical Authority)**: `https://www.statistics.gr` — building permits, construction cost
- **Hellenic Land Registry** for legacy mortgage records (where cadastre not yet operational)

### Listing platforms

- **Spitogatos.gr** — DOMINANT (consolidated Spitogatos + Spiti24 + Tospitimou + HomeGreekHome): `https://www.spitogatos.gr/en`
  - Has price index by area at /property-index
- **XE.gr** — second major aggregator: `https://www.xe.gr/property`
- **Indomio.gr**: `https://www.indomio.gr/`
- **Goldenhome.gr**: `https://www.goldenhome.gr/`
- **Plot.gr**, **Remax.gr**

### 2025 price benchmarks (Bank of Greece + Spitogatos)

| Region | Avg €/m² (apt) | Avg total (single-family) |
|---|---:|---:|
| **Athens centro (Plaka, Syntagma, Kolonaki)** | 3,500–6,000+ | 400,000–1,200,000+ |
| **Athens northern suburbs (Kifissia, Marousi)** | 2,800–4,500 | 380,000–800,000 |
| **Athens southern suburbs (Glyfada, Voula)** | 3,200–5,500 | 420,000–950,000 |
| **Athens western suburbs** | 1,500–2,500 | 180,000–350,000 |
| **Thessaloniki centro** | 1,800–2,800 | 200,000–400,000 |
| **Thessaloniki suburbs** | 1,500–2,200 | 180,000–320,000 |
| **Patras** | 1,200–1,800 | 130,000–250,000 |
| **Crete (Heraklion / Chania)** | 1,800–3,500 | 220,000–500,000 |
| **Mykonos / Santorini** | 5,000–15,000+ | 800,000–5,000,000+ |
| **Cyclades (other)** | 2,500–5,000 | 350,000–800,000 |
| **Rural Peloponnese / Epirus** | 800–1,500 | 100,000–250,000 |

### Compute

1. €/m² = price / **καθαρή ωφέλιμη επιφάνεια** (net usable area)
2. **Antikeimeniki Axia** (Objective Value) — official cadastral assessment, **frozen until 2027**
3. **Cross-check** Bank of Greece RPPI for area trend
4. **Settle objective value vs market**: market often 40-60% above objective

### Key terms

- KAEK = unique cadastral parcel number
- Antikeimeniki Axia = Objective (cadastral) Value
- Apospasma = cadastral excerpt
- Mihaniki Vevaiosi = engineer's statement
- PEA = energy certificate
- Authairesi = unauthorized construction

---

## Section: `--traffic`

### Sources

- **NEK** (Greek roads operator) for motorways
- **Hellenic Statistical Authority** for transport data
- **Ministry of Infrastructure** roads section
- **OpenStreetMap** + Google Maps Live for urban arterials

### Key term

**ΜΕΗΚ (Μέση Ετήσια Ημερήσια Κυκλοφορία)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (rural roads, small islands)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (Athens arterials, Egnatia)
- 🔴 > 35,000 v/d (Attiki Odos, Athens ring, Kifissou Avenue)

---

## Section: `--tax`

### Annual property tax — ENFIA

**Reformed annually since 2014; 2025-2026 reductions**:

#### ENFIA structure

- **Main ENFIA**: per m² × coefficients (location, age, floor, building type)
- **Supplementary ENFIA**: progressive on portfolio total value above €200k (individuals) / €30k (companies)

#### 2025-2026 reductions (CRITICAL)

- **Insured residences ≤ €500k taxable value**: **−20% ENFIA** (since 2025)
- **Insured residences > €500k**: **−10%**
- **Villages ≤ 1,500 inhabitants**: **−50% ENFIA from 2026** (excludes Attica except islands)
  - ~12,720 settlements affected
- **Historic buildings ≤ €400k**: exempt
- **Objective values frozen until 2027** — preserves base

#### Illustrative ENFIA bills (est.)

> **est. — not a quote.** Ranges below are modelled from the Main ENFIA per-m² × coefficient structure (line 109) with the 2025-2026 reductions above applied; they are NOT sourced bills. Verify the exact figure on the [AADE myPROPERTY / ENFIA](https://www.aade.gr/) statement for the specific parcel.

| Property type | Illustrative annual ENFIA (est., 2025-2026 basis) |
|---|---:|
| Athens 80 m² apt (€150k objective) | ~€300–€600 |
| Athens villa (€500k objective) | ~€1,500–€3,500 |
| Cyclades vacation home (€350k) | ~€1,000–€2,500 |
| Rural village house (≤1,500 pop) | ~€100–€300 (reflects −50% village cut from 2026, line 116) |

### Transaction taxes

- **Foros Metavivasis Akinitou (FMA)**: **3% + 0.09% municipal surcharge = 3.09%** on resale (confirmed PwC, multiple 2025-2026 sources)
- **VAT on new builds**: **24% statutory rate**, but **suspended through 31 Dec 2026** (Law 5246/2025, gazetted 11 Nov 2025)
  - During suspension, new builds attract 3.09% transfer tax instead
- **Notary fees**: ~1.0–1.5% sliding scale
- **Lawyer fees**: ~1% (recommended, sometimes mandatory for non-residents)
- **Realtor**: typically ~2% per side (buyer + seller)

### Total transaction cost (buyer side)

- Resale: ~6–8% of price (3.09% transfer + 1-1.5% notary + 1% lawyer + 2% realtor)
- New build (during VAT suspension): same as resale ~6–8%
- New build (post-VAT-suspension): 24% VAT + others

### Capital gains

- **15% statutory rate** (Law 4172/2013)
- **Suspended through 31 Dec 2026** — confirmed
- Caveat: if reclassified as "business activity" (intent, frequency, 3+ properties), normal income tax + VAT apply

### IRS / income tax on rental

- Up to 2 properties: "income from immovable property" (15% / 25% / 35% / 45% bands)
- **3+ properties → business activity** = 13% VAT + hotelier-style obligations (post-Law 5170/2025)

### VAT (FPA)

- 24% standard
- 13% reduced (food, tourist services)
- New residential property: 24% (suspended through 2026)

### Future risk

- **VAT suspension expires 31 Dec 2026** unless extended again
- **Capital gains 15% suspension expires 31 Dec 2026**
- **Antikeimeniki Axia frozen until 2027** — likely revaluation
- **Cadastre full activation 2026** — affects title clarity

---

## Section: `--rental`

### Long-term residential

- **Civil Code Article 574** governs lease
- Long-term rental (>3 years): notarized strongly recommended
- Tenant moderate protection
- Rent caps in some Athens neighborhoods (proposed 2025-2026)

### Short-let (Airbnb / Vrachychronia Misthosi)

**MAJOR REFORMS 2024-2025**:

#### Athens license freeze

- **From 1 Jan 2025**: NO new STR licenses in **1st, 2nd, 3rd municipal districts of Athens** (Plaka, Syntagma, Monastiraki, Koukaki, Exarchia, Pangrati area)
- Existing licenses keep operating
- **Extended through 2026**

#### Cyclades / oversaturated regions

- STR freeze announced for **5 additional regions** effective **1 Oct 2025**
- April 2026: **30% cut to tourist beds in Cyclades** announced

#### Law 5170/2025 (effective 1 Oct 2025)

- STR ONLY on properties with **"primary use" status** (not commercial, not basement)
- Mandatory: natural lighting, liability insurance, fire safety, certifications
- Fines up to **€5,000**
- AADE cross-checks **AMA (Property Registration Number)** — non-compliant listings auto-deleted from Airbnb/Booking/Vrbo

#### AMA (Arithmos Mitroou Akiniton)

- Mandatory registration number per property
- Issued by AADE (tax authority)
- Required to advertise on Airbnb/Booking/Vrbo
- **EFKA + AADE cross-checks** since 2023

### Tax on rental

- 1-2 properties: real estate income — **2026 reform** (effective 1 Jan 2026): **15% to €12k / 25% to €24k / 35% to €35k / 45% over €35k** (new €24k tier; pre-2026 was 15/25/35/45 without the €24k break) (2026-05-27 verified, source [Athens Times — 2026 Tax Reform](https://athens-times.com/rental-income-tax-enfia-tax-assumptions-and-benefits-for-uniformed-personnel-tax-bill-passed-what-it-includes/) + [PwC Tax Summaries Greece](https://taxsummaries.pwc.com/greece/individual/taxes-on-personal-income))
- 3+ properties: business activity (13% VAT)
- **Income tax credits** for property repairs (up to certain caps)
- **STR statute spine**: L.4446/2016 Art. 111 (AMA registry foundation) → L.4174/2013 Art. 54A (fines) → L.5073/2023 (refinements) → L.5170/2025 (2025 Aegean/Athens regime) (2026-05-27 verified, source [AADE Article 111 of Law 4446/2016 PDF](https://www.aade.gr/sites/default/files/2024-09/Article%20111%20of%20Law%204446_2016%20updated%20by%205073_2023%20-%20relevant%20provisions.pdf))

---

## Section: `--work=<profession>`

### Sources

- **OAED / DYPA** (Greek labour ministry job platform)
- **kariera.gr**, **Skywalker.gr**, **JobFind.gr**
- **LinkedIn GR**

### Self-employment

- **Atomiki epicheirisi** (sole trader): EFKA registration
- **Eteria periorismenis efthynis (EPE)**: limited liability
- **VAT (FPA)**: from €10,000 turnover (most sectors)
- **Personal tax** (2026 reform, effective 1 Jan 2026): **9% / 20% / 26% / 34% / 39% / 44%** (new 39% band at €40-60k; pre-2026 was 9/22/28/36/44; under-25s now 0% to €20k) (2026-05-27 verified, source [TaxRavens Greece Personal Income Tax 2026](https://taxravens.com/en/blog/greece-personal-taxation) + [Immigrant Invest 2026 Tax Guide](https://immigrantinvest.com/blog/taxes-in-greece/))
- **EFKA contributions** mandatory

### Salary benchmarks (2025)

- Median monthly gross:
  - Athens: ~€1,300–€2,000
  - Thessaloniki: ~€1,200–€1,800
  - Smaller cities: ~€1,000–€1,500
- **Minimum wage**: est. ~€910/mo (2025); rising — verify the gazetted statutory rate at the Greek Ministry of Labour (Υπουργείο Εργασίας, ypergasias.gov.gr)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **EPPO / OASP** (Earthquake Planning & Protection Organization) | `https://oasp.gr` | Seismic policy, code |
| **HSGME** (formerly IGME) — Hellenic Survey of Geology and Mineral Exploration | `https://www.hsgme.gr` | Geology, faults, **active faults DB**: `https://activefaults.eagme.gr/en/` |
| **Civil Protection** | `https://civilprotection.gov.gr/en/xartis` | **Daily fire risk map** May–Oct |
| **NOA** (National Observatory of Athens) | `http://hl-ntwc.gein.noa.gr/en/` | **Tsunami warnings**, seismicity |
| **ISMOSAV** (Santorini Volcano Monitoring Institute) | per NOA | Santorini + Kolumbo monitoring |
| **EYDAP** (Athens water): `https://www.eydap.gr` |
| **EYATH** (Thessaloniki water): `https://www.eyath.gr` |

### Specific risks

#### Seismic (HIGH)

- **Eurocode 8 Greek National Annex** uses 2003 zonation map: 3 zones, **PGA 0.16–0.36g**
  - Revision in progress proposes 5 zones (PGA 0.13–0.37g)
- **Recent significant events**:
  - **Athens 1999** (Mw 5.9, Parnitha)
  - **Lefkada 2003 + 2015**
  - **Samos-Izmir 2020** (Mw 7.0, generated tsunami alert)
  - **Crete 2021** (Heraklion)
  - **Santorini swarm Jan-Feb 2025** — UNESCO-IOC monitoring; mass exodus + emergency declaration

#### Volcanic — Hellenic Volcanic Arc

- **Methana, Milos, Santorini, Nisyros, Kolumbo** (submarine, 7 km NE of Santorini)
- **Santorini caldera** + **Kolumbo** monitored continuously
- **2025 Santorini swarm** caused mass exodus; emergency declared

#### Wildfire (CATASTROPHIC RISK)

- **Civil Protection daily fire risk map** May–Oct: `https://civilprotection.gov.gr/en/xartis`
- **Mati 2018**: 104 dead, 5,000 ha (Eastern Attica)
- **Recent**: Rhodes 2023, Evia 2021, Attica 2024
- **AntiNero programme**: 12,000 km of forest treated by end-2024 across 39 plans

#### Tsunami

- **HL-NTWC** (Hellenic National Tsunami Warning Centre, NOA): `http://hl-ntwc.gein.noa.gr/en/`
- Part of UNESCO-IOC NEAMTWS
- **High-risk zones**: Hellenic Arc (E and W), Aegean fault zones, Gulf of Corinth
- **Coastal Crete, Rhodes, Karpathos, Cyclades** flagged

#### Other risks

- **Floods**: Attica + Thessaloniki + Peloponnese; **EU Directive 2007/60/EC**: `http://floods.ypeka.gr`
- **Soil erosion** + landslide: Pindos mountains, Peloponnese
- **Coastal erosion** + sea-level rise — major Greek islands
- **Air pollution**: Thessaloniki winter PM10 (wood burning ~70%); Athens nephos summer

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1940s** | No DPC, lead, asbestos cement starts |
| **1950s-1980s "polykatoikia" boom** | Asbestos very common, weak seismic compliance, illegal additions (authairesia) |
| **Post-1985 EAK** | Earthquake code introduced |
| **Post-2003 EAK 2003** | Stricter seismic |
| **Post-2010 KENAK** | Energy efficiency required |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **PEA (Pistopoiitiko Energeiakis Apodosis)** | Energy certificate, mandatory since 2010 (Law 3851/2010, 4122/2013) | 10 years |
| **Mihaniki Vevaiosi** (engineer's statement) | Required since Law 4014/2011, currently Law 4495/2017 | At sale |
| **Topographic diagram** with EGSA '87 coordinates | Cadastre transactions | Per case |
| **ENFIA paid certificate** | Tax clearance | Annual |
| **TAP (municipal property duty) clearance** | Tax | At sale |
| **Authairesia** review (illegal construction regularization) | If applicable | Per case |

### Climate change projections

- +2.0–3.5 °C by 2050
- Sea-level rise: +20–60 cm by 2100
- More extreme heat events
- Increased wildfire risk + intensity
- Reduced water availability

---

## Section: `--mains`

### Sources

- **EYDAP** (Athens, Attica): `https://www.eydap.gr` — exclusive provider until 2040
- **EYATH** (Thessaloniki): `https://www.eyath.gr`
- **Elsewhere**: ~230 municipal **DEYA** (Demotiki Epicheirisi Hydreusis Apochetefsis) companies serve ~4M people
- No single national database — must contact local DEYA or municipality
- Rural / out-of-plan properties: cesspool/septic still common

### Verification

- Athens + Thessaloniki: universal mains
- Most provincial cities: DEYA mains
- Rural islands + remote: often **vothros** (cesspool); **mikros viologikos** (small biological treatment)

### Costs

| Scenario | Cost (€) |
|---|---:|
| EYDAP / DEYA connection | 2,500–8,000 |
| Mains-line extension | 8,000–25,000 |
| Vothros to compliant biological treatment | 4,000–10,000 |

---

## Cost benchmarks (GR 2026)

| Work | Cost (€) |
|---|---:|
| PEA (energy cert) | 200–500 |
| Mihaniki Vevaiosi | 300–800 |
| Topographic diagram | 400–1,200 |
| Notary | 1.0–1.5% of price |
| Lawyer | ~1% (recommended) |
| Realtor | ~2% per side |
| Foros Metavivasis | 3.09% |
| **Total transaction cost (resale, buyer)** | **~6–8%** of price |
| **Total transaction cost (new build during VAT suspension)** | **~6–8%** |
| Vothros to biological treatment | 4,000–10,000 |
| Antiseismic retrofit | 30,000–80,000 |
| Authairesia legalization | varies by amnesty |
| Roof renovation | 8,000–25,000 |
| Energy retrofit (Class C → A) | 25,000–60,000 |

## Active fiscal incentives (2025-2026)

- **Exoikonomo (Saving)** programme: energy retrofit grants
- **Spiti Mou** programme: subsidized mortgages for first-time buyers
- **VAT suspension on new builds** through 31 Dec 2026
- **Capital gains suspension** through 31 Dec 2026
- **Reduced ENFIA** for insured + village properties

## Common listing platforms

- **Spitogatos** — biggest
- **XE.gr** — second
- **Indomio**, **Goldenhome**, **Plot**, **Remax**

## Caveats unique to GR

- **Ktimatologio** (cadastre) still completing — full activation slipped to 2026
- **Ypothykofylakeio** (legacy mortgage register) for areas not yet operational cadastre
- **Authairesia (unauthorized construction)** widespread — Mihaniki Vevaiosi mandatory; amnesty regimes (L.4014/2011, L.4178/2013, L.4495/2017)
- **Antikeimeniki Axia** ≠ market value (often 40-60% below)
- **Mihaniki Vevaiosi** required for ALL sales since 2011
- **Athens STR license freeze** in central districts since 1 Jan 2025; extended through 2026
- **Cyclades 30% bed cap** announced April 2026
- **Mykonos + Santorini building permit freeze** through 31 Dec 2026 (Special Urban Plans pending)
- **Santorini caldera zone**: no new builds, additions, pools, water infrastructure on Thera/Thirassia
- **Out-of-plan construction** halted in many islands
- **Golden Visa** restructured 1 Sept 2024:
  - **€800k**: Attica (incl. Athens), Thessaloniki, **all Greek islands with registered population >3,100 (including Crete, Rhodes, Corfu, Kos, Mykonos, Santorini, Paros — full list at goldenvisas.gr)** (min 120 m², single unit) (2026-05-27 verified, source [Global Citizen Solutions Greece Golden Visa Map 2025-2026](https://www.globalcitizensolutions.com/greece-golden-visa-new-rules/))
  - **€400k**: all other regions (min 120 m², single unit)
  - **€250k**: only for heritage-building restoration or commercial-to-residential conversions
- **VAT 24%** on new builds suspended through 31 Dec 2026
- **Capital gains 15%** suspended through 31 Dec 2026
- **Eurocode 8** seismic compliance mandatory for new builds; older buildings highly variable
- **Wildfire risk extreme** May–Oct — evacuation zones critical
- **Tsunami coastal risk** for Hellenic Arc + Aegean
- **3+ properties = business activity** (13% VAT + obligations)
- **EFKA + AADE cross-checks** for short-let income
- **PEA** mandatory since 2010

## Reddit / forum sources

- **r/greece** — biggest community
- **r/Athens**, **r/Thessaloniki**
- **r/AskGreece**
- **r/expatsingreece** — expat-specific
- **Greek Reporter**, **Ekathimerini** (English)
- **Tornos News**, **GTP Headlines**

## Verification authorities

| Authority | When to call |
|---|---|
| **Ktimatologio Office** | Title verification |
| **Ypothykofylakeio** (where cadastre not operational) | Legacy title |
| **Notary** (mandatory for sale) | Final transfer |
| **DOY (tax office)** | ENFIA, transfer tax |
| **Engineer (mihanikos)** | Mihaniki Vevaiosi |
| **Civil Engineer for Authairesia regularization** | If applicable |
| **AADE** | Tax + AMA + STR registration |
| **EYDAP / EYATH / DEYA** | Mains drains |
| **EPPO/OASP** | Seismic risk |
| **Civil Protection** | Wildfire risk |
| **HL-NTWC** | Tsunami |

## Source URL templates

| Source | URL pattern |
|---|---|
| Ktimatologio | `https://www.ktimatologio.gov.gr/` |
| gov.gr property registry | `https://www.gov.gr/en/ipiresies/periousia-kai-phorologia/ktematographese` |
| Bank of Greece RPPI | `https://www.bankofgreece.gr/en/statistics/real-estate-market` |
| Spitogatos | `https://www.spitogatos.gr/en` |
| EPPO seismic | `https://oasp.gr` |
| HSGME active faults | `https://activefaults.eagme.gr/en/` |
| Civil Protection fire | `https://civilprotection.gov.gr/en/xartis` |
| HL-NTWC tsunami | `http://hl-ntwc.gein.noa.gr/en/` |
| EYDAP | `https://www.eydap.gr` |
| ELSTAT | `https://www.statistics.gr` |
| AADE | `https://www.aade.gr/` |
| Floods (EU dir.) | `http://floods.ypeka.gr` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax (incl. 2025-2026 ENFIA reforms + VAT/CGT suspensions), rental (incl. STR Law 5170/2025 + Athens freeze + Cyclades 30% cap), work, risks (seismic + volcanic + wildfire + tsunami), mains all have primary government sources + cost benchmarks.
**Confidence**: HIGH for STR reforms (Athens Times, GTP Headlines, ProtoThema, BNB News, Airbnb 2025 Greek tax guide all confirm); HIGH for ENFIA 2025-2026 cuts (multiple tax law firm sources confirm); HIGH for VAT/CGT suspension extensions through 2026 (Law 5246/2025 gazetted 11 Nov 2025, vatcalc + Elxis confirm); HIGH for Golden Visa restructuring (Global Citizen Solutions + multiple sources confirm 1 Sept 2024 effective). MEDIUM for Cyclades 30% cap (announced April 2026, implementation uncertain). MEDIUM for cadastre completion timeline (target slipping repeatedly).

## Extension TODOs

- [ ] Per-municipality ENFIA coefficient table
- [ ] Authairesia regularization decision tree (which amnesty applies)
- [ ] Mykonos / Santorini permit freeze zone overlay
- [ ] Athens STR-frozen district perimeter
- [ ] Cyclades 30% bed cut implementation rules
- [ ] EYDAP/DEYA per-municipality connection lookup
- [ ] Wildfire-vulnerable zone overlay (Civil Protection)
- [ ] Tsunami coastal hazard zoning per island
- [ ] Cadastre operational status per municipality
- [ ] Golden Visa eligibility decision tree
- [ ] PEA cost + energy class scoring for new + retrofit
