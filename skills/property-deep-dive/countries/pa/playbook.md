# Panama 🇵🇦 — Property Due-Diligence Playbook

ISO2: `pa`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4-digit postal zones, written before the apartado (P.O. box) number: `0801` Panamá, `0426` David, `0413` Boquete (source youbianku postcode aggregator — secondary, undated; verify with Correos y Telégrafos de Panamá `https://www.correospanama.gob.pa`)
- **Admin levels**: 10 provinces + 82 districts + 699 corregimientos (2026 data, source INEC population projections by district and corregimiento, Census 2023 base); 3 comarcas indígenas with province rank (Kuna Yala, Emberá, Ngäbe Buglé — INEC) and 6 comarcas in total counting those inside provinces (2023 data, source educapanama.edu.pa — secondary; verify the current list with INEC) — rates/figures may have changed since
- **Currency**: **USD** (US dollar) + symbolic balboa 1:1 — UNIQUE economy fully USD-denominated
- **Languages**: Spanish (official — Constitución Política Art. 7, texto único GO 25176 of 2004); English widely used in business + expat zones
- **Cadastre**:
  - **Registro Público de Panamá**: `https://www.rp.gob.pa/`
  - **ANATI (Autoridad Nacional de Administración de Tierras)**: `https://www.anati.gob.pa/`
- **Identifier**: **Finca / Tomo / Folio** (or Documento Redi for newer digital filings)
- **Ownership types**:
  - **Titulado** (titled freehold)
  - **Derecho posesorio** (rights of possession; common rural/coastal — harder to mortgage)
  - **Ribera de playa (public beach strip)**: from the **línea de alta marea** (high-tide line) to **22 m inland on the Pacific coast / 10 m on the Caribbean (Atlantic) coast** — not titleable; only the zona costera adjudicable behind it (up to 200 m from the high-tide line) can be titled (Ley 80 of 31 Dec 2009 Art. 2, GO 26438-B; 2026 verification, source Gaceta Oficial text via FAOLEX) — concession rights on the strip: verify with AMP / ANATI
  - **Comarcas indígenas** (collectively owned; foreigners CANNOT buy)

## Section: `--price`

### Primary sources

- **INEC (Instituto Nacional de Estadística y Censo)**: `https://www.inec.gob.pa/`
- **Superintendencia de Bancos**: `https://www.superbancos.gob.pa/estadisticas-financieras/cartera-credito` — credit statistics, incl. Crédito a Vivienda Propia (Ley Preferencial) and new-loan series (2026 reports)
- **ACOBIR (Asociación Panameña de Corredores y Promotores de Bienes Raíces)** — semi-annual MLS closed-sale report: `https://www.acobir.com/indicadores-de-mercado/indicadores-economicos` (industry association — secondary tier; small closed samples)
- **TheLatinvestor**, **Global Property Guide** — aggregated benchmarks (secondary)

### Listing platforms

- **Encuentra24 Panama** — DOMINANT (largest portal self-count: 57,832 properties / 33,033 apartments for sale, 2026 data, encuentra24.com self-counts seen Oct 2026 — listing-platform tier): `https://www.encuentra24.com/panama`
- **CompreoAlquile**: `https://www.compreoalquile.com/` (18,284 apartments for sale, 2026 data, portal self-count seen Oct 2026)
- **InmoPanama** (`https://www.inmopanama.com/`, portal), **Panama Equity** (`https://www.panamaequity.com/`, brokerage listings + quarterly market reports), **MLS ACOBIR** (`https://www.mlsacobir.com`, brokers' MLS)
- **Realtor.com.pa** ❌ DEPRECATED — dead on 2026-10-23 (domain does not resolve); verify with Encuentra24 / InmoPanama
- USD economy = **listings stable in USD**

### 2026 price benchmarks (Panama City neighbourhood rows: Panama Equity Q1 2026 asking averages, data Galería Inmobiliaria, reproduced by Global Property Guide; closed-sale row: ACOBIR MLS; Albrook / Clayton and the rows outside Panama City: TheLatinvestor + Global Property Guide aggregator figures from the 2026-04 research — **secondary / listing tier per anti-hallucination contract**; verify with on-the-ground broker quotes before relying — INEC publishes no per-m² price series)

| Region | USD/m² (typical) | Notes |
|---|---:|---|
| **Panama City — closed apartment sales** | $1,726 (H1 2026; H1 2025 $1,756) | Closed prices (2026 data, source ACOBIR MLS I Semestre 2026 report) |
| **Punta Pacífica (Panama City)** | $2,200 resale – $4,300 pre-construction | Premium; asking averages (2026 data, Panama Equity Q1 2026) |
| **Costa del Este** | $2,500 resale – $3,800 pre-construction | Modern expat; asking (2026 data, Panama Equity Q1 2026) |
| **Santa María / Casco Viejo (premium)** | Santa María $2,900–$3,800; Casco Viejo $3,800–$4,300 (resale – pre-construction) | Heritage + golf; asking (2026 data, Panama Equity Q1 2026) |
| **El Cangrejo / Marbella** | El Cangrejo $1,770 resale – $2,800 pre-construction; Marbella not reported | Mid-range Panama City; asking (2026 data, Panama Equity Q1 2026) |
| **Albrook / Clayton** | $2,200–$3,000 | Former Canal Zone |
| **Boquete (mountain expat)** | $100k–$400k typical homes | Mountain expat market |
| **Coronado (beach 60-min west)** | $200k–$600k typical | Beach 6–9% yield |
| **Bocas del Toro (Caribbean)** | varies massively; 6–12% yield | Seasonal |
| **El Valle de Antón** | $200k–$500k | Crater valley |

**2026 trend**: closed apartment prices **−1.7% YoY** in Panama City (computed: $1,726 H1 2026 ÷ $1,756 H1 2025, ACOBIR MLS — small sample, 85 apartment sale closings nationwide in H1 2026); asking prices **+6.81% YoY** to $1,881/m² in Sep 2025 (2025 data, source RIAL Di Tella-Zonaprop via Global Property Guide, latest edition — rates/figures may have changed since); pre-construction asking up >15% over 12 months (2026 data, Panama Equity). Residential sales value **−13% YoY** to $695M in H1 2026 (homes ≤$120k −28.3%) while sales to foreign buyers rose 17.7% to $712M (2026 data, ACOBIR via TVN — secondary). INEC publishes no per-m² HPI; verify with on-the-ground broker quotes

### Compute

1. USD/m² = price / **área de construcción** (built area)
2. **Verify titulado vs derecho posesorio** — critical
3. **Check 10km border restriction** if near Costa Rica or Colombia
4. **No FX risk** for USD holders (USD economy)

### Key terms

- Finca / Tomo / Folio = title identifier
- Titulado = titled (full ownership)
- Derecho posesorio = rights of possession (lesser title)
- Concesión = government coastal lease
- Comarca indígena = indigenous collective land (off-limits to foreigners)
- Pensionado = retiree visa
- Friendly Nations Visa = expat-attracting program

---

## Section: `--traffic`

### Sources

- **MOP (Ministerio de Obras Públicas)**: `http://www.mop.gob.pa/`
- **ATTT (Autoridad de Tránsito y Transporte Terrestre)**
- **ENA (Empresa Nacional de Autopista)**: toll-corridor aforo datasets (Corredor Norte, Sur, Este) on `https://www.datosabiertos.gob.pa/`

### Key term

**TPDA (Tránsito Promedio Diario Anual)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural, comarcas)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, Panama City corridor)
- 🔴 > 35,000 v/d (Corredor Norte, Corredor Sur, Av Balboa, Cinta Costera) — calibration: Corredor Sur averaged 179,707 vehicles/day in 2025 (2025 data, ENA aforo statistics via nexo.la, Aug 2026 — secondary; toll-plaza transactions, not a single-section count)

---

## Section: `--tax`

### Annual property tax — Impuesto de Inmuebles (Family Patrimony — Ley 66/2017)

**Progressive scale for primary residence ("patrimonio familiar")** — each rate applies only to the slice of cadastral value inside its band (tarifa progresiva combinada); this scale needs a Patrimonio Familiar Tributario / Vivienda Principal request to the DGI, which must rule within 3 months (2026 data, source DGI Impuesto de Inmueble page):

| Value (USD) | Rate |
|---|---:|
| 0–$120,000 | **0%** |
| $120,000–$700,000 | **0.5%** |
| > $700,000 | **0.7%** |

**Non-primary scale** (general table — second homes, rentals, commercial, land; payable in 3 instalments by 30 April, 31 August and 31 December, 10% discount for paying the full year before 30 April with no arrears) (2026 data, source DGI Impuesto de Inmueble page):

| Value (USD) | Rate |
|---|---:|
| 0–$30,000 | 0% |
| $30,000–$250,000 | 0.6% |
| $250,000–$500,000 | 0.8% |
| > $500,000 | 1.0% |

### Transaction taxes

- **Impuesto de Transferencia de Bienes Inmuebles (ITBI) 2%** of the greater of the sale price or the cadastral value, plus a **3% income-tax advance** on the same base — both legally the seller's (Ley 106 of 1974 Art. 1: "La tasa del 2 % será pagada por el transmitente"; DGI Formulario 106) (2026 data, source PwC Worldwide Tax Summaries Panama, last reviewed 4 Aug 2026). Stamp duty is separate: USD 0.10 per USD 100 on certain commercial contracts only (same source)
- **Registro Público fees**: B/.10 calificación per finca + B/.3.00 per B/.1,000 (or fraction) of value to register the transfer, and the same again to register a mortgage (2013 tariff, source Registro Público Resolución 212 of 2013, Gaceta Oficial 27283-A; same B/.3.00 per B/.1,000 transfer rate in the Registro's Manual de Calificación, Gaceta Oficial 28786-A of 31 May 2019 — rates/figures may have changed since). **Notary fees**: data not publicly available — verify with the notario's written quote
- **ITBMS 7%** on real-estate leases; exempt only when the lease is exclusively for the tenant's dwelling AND the term exceeds 6 months (Código Fiscal Art. 1057-V, Contraloría-hosted text; DGI nota 201-01-0588-DGI of 21 Apr 2021, secondary reproduction) — shorter residential lets are taxed; hotel accommodation 10% (2026 data, source PwC Worldwide Tax Summaries Panama, last reviewed 4 Aug 2026)

### Capital gains

- **10%** on the resale gain. **2% transfer tax (ITBI) + 3% income-tax advance**, both on the greater of the gross price or the cadastral value, paid by the seller at closing. Seller may elect the **3% advance as DEFINITIVE tax** (no refund, no further CGT) **OR** compute 10% on actual gain and credit the 3% advance (any excess may be rebated). Election matters when actual gain is low — 3% on whole price can exceed 10% on small gain (2026 data, source PwC Worldwide Tax Summaries Panama, last reviewed 4 Aug 2026).

### Territorial tax — UNIQUE

**No Panamanian income tax on foreign-source income** — UNIQUE territorial system: residents and non-residents are taxed only on Panamanian-source income (2026 data, source PwC Worldwide Tax Summaries Panama, last reviewed 4 Aug 2026).

### Total transaction cost (buyer side)

- Resale: the 2% ITBI + 3% income-tax advance are the seller's; the buyer pays Registro Público fees (≈0.3% of value, computed from B/.3.00 per B/.1,000, plus the same on any mortgage), notary and lawyer — est. ~**1–2%** on a USD 200k purchase (computed: registry USD 600 + notary ~USD 300–500 + lawyer ~USD 1,000–2,500 per abogados.pa, a secondary lawyer-directory source = USD 1,900–3,600) — check the promesa de compraventa for any cost-shifting clause
- New build (first sale of a new home, formalised within 2 years of the occupancy permit): the first B/.120,000 of the ITBI base is exempt; a base of B/.120,000–200,000 pays a preferential 0.50–1.80% (rate set by the total base) on the part above B/.120,000; above B/.200,000 the general 2% applies to the part above B/.120,000; any clause making the buyer pay or reimburse this seller tax is void; homes whose occupancy permit predates the law qualify if the sale is formalised within 30 months of the permit (Ley 546 of 31 Aug 2026, Gaceta Oficial 30601-B, in force 1 Sep 2026). The earlier full exemption lapsed on 31 Dec 2025 (Ley 468 of 2025 / Ley 472 of 2025). Buyer-side registry, notary and lawyer as for resale

### Future risk

- **Pensionado visa stable** (B/.1,000/mo lifetime pension; **B/.750/mo if the applicant has bought property in Panama in their own name for more than B/.100,000**; pension paid by a foreign government, an international organisation or a private company and granted for life — not a term annuity) (2026 data, source SNM PRP-JP requirements sheet citing Decreto Ejecutivo 320 of 2008 Art. 200)
- **Friendly Nations Visa** — modified by **Decreto Ejecutivo 197 of 7 May 2021** and **Decreto Ejecutivo 226 of 20 July 2021**, both in force **7 August 2021** (DE 226 Art. 3 moved DE 197's start date): real estate ≥ B/.200,000 (may be bank-financed), a 3-year fixed deposit ≥ B/.200,000 at a general-licence bank, or a job with a Panamanian employer plus a MITRADEL work permit; Ecuador added to the list by Decreto Ejecutivo 16 of 31 Aug 2026 (2026 data, source Gaceta Oficial 29335 + SNM requirements sheet and decree list)
- **Qualified Investor Visa** — **restructured, not deferred**: Executive Decree 17 of 8 Sep 2026 (Gaceta Oficial 30613, 16 Sep 2026, in force on promulgation) replaced Decree 722/2020 as amended by Decrees 109/2022 and 193/2024. Real estate is now **B/.300,000 for a first-sale property** (new, unoccupied, from the developer) or an off-plan promesa de compraventa, but **B/.500,000 for a resale property** (previously sold, occupied or leased) — under Decree 193 every property qualified at B/.300,000. Investments or binding contracts perfected before 16 Sep 2026 may use the old rules if the application is filed within 6 months — ~16 Mar 2027 (computed) (2026 data, source Gaceta Oficial 30613 Arts. 4, 7, 19–21 + MICI 21 Sep 2026; see `shared/visa-programs.md` PA Qualified Investor row)

---

## Section: `--rental`

### Long-term residential

- **Ley 93 of 4 Oct 1973** (GO 17456), amended by **Ley 28 of 12 Mar 1974** (GO 17554) and later rules, still governs leases; administered by **MIVIOT Dirección General de Arrendamientos** (a MIVIOT reform is in preparation, no replacement law in force — 2026, source MoveIn Panama, secondary)
- Landlord must file a copy of every lease (and sub-lease) with the Dirección General de Arrendamientos within **5 business days** of signing (Ley 93 Art. 6, GO 17456). Housing leases: the agreed term and any extension bind the landlord, while the tenant may end the lease at any time by giving at least **30 calendar days'** notice; commercial, professional, industrial and teaching leases bind both parties unless the contract lets the tenant renounce the term (Art. 10 as replaced by Ley 28 of 1974 Art. 2; text via ACOBIR, secondary copy)
- Tenant protection moderate
- Standard 1-3 year contracts
- **Closed MLS rents, Panama City apartments**: **$12.57/m²/month** in H1 2026 vs $11.54 in H1 2025 (+8.9%, computed) (2026 data, source ACOBIR MLS I Semestre 2026 — small sample); MLS-wide average closed rent, all provinces: $1,639/month apartment (102 closings), $1,950 house (19 closings) (same report)
- **Gross yield**: est. ~8.7% (computed: $12.57 × 12 ÷ $1,726/m², ACOBIR MLS H1 2026 Panama City apartment averages — rent and sale samples are different units; before vacancy, HOA, tax)

### Short-let

- **City (Distrito de Panamá)**: **Ley 80 of 8 Nov 2012 Art. 21** prohibits any lease shorter than **45 days** without an ATP *permiso de alojamiento público turístico*; ATP fines **B/.5,000–50,000**, and the same fines apply to anyone advertising such stays, including online (Ley 80 text, GO 27159-A, via atp.gob.pa). ATP registration + municipal licence; **10% ITBMS** on hotel / lodging (hospedaje) services vs the general 7% (2026 data, source PwC Worldwide Tax Summaries Panama, reviewed 4 Aug 2026; DGI Form 430 instructions) + income tax
- **Pending, not law**: **Proyecto de Ley 713 of 2026** (MICI, filed 14 Sep 2026) would set a **15%** rate on short-stay tourist lodging in residential property, whether booked through a platform or directly; in first debate at the Comisión de Comercio since 23 Sep 2026 (2026 data, source Infobae 9 Oct 2026 + LeyClara / segLegis 21 Oct 2026 — secondary; check status at asamblea.gob.pa)
- **Boquete**: HOA-dependent
- **Bocas del Toro**: marine-zone overlay + ATP licence

### Tax on rental

- Resident: progressive income tax — 0% up to USD 11,000; 15% on USD 11,000–50,000; USD 5,850 + 25% above USD 50,000 (2026 data, source PwC Worldwide Tax Summaries Panama, reviewed 4 Aug 2026)
- Non-resident: taxed only on Panama-source income; the payer must withhold the tax on income paid to a non-resident (2026 data, source PwC) — PwC states no rent-specific rate; verify the rate and any DTT relief with DGI
- **10% ITBMS** on hotel / lodging (hospedaje) stays (2026 data, source PwC + DGI Form 430 instructions); **7% ITBMS** general rate, used for commercial rent (verify rent treatment with DGI); tobacco 15%

---

## Section: `--work=<profession>`

### Sources

- **MITRADEL (Ministerio de Trabajo)**: `https://www.mitradel.gob.pa/`
- **Konzerta** (`https://www.konzerta.com/`), **Computrabajo Panamá** (`https://pa.computrabajo.com/`), **EstasContratado** (`https://www.estascontratado.com/` — the Tecoloco group's Panama board; `tecoloco.com.pa` does not resolve), **LinkedIn PA**

### Self-employment

- **Persona natural** with Aviso de Operación
- **Sociedad Anónima (SA)** common for asset protection
- **ITBMS** 7%: registration required once prior-year gross income exceeds **B/.36,000** (average above B/.3,000/month) — Código Fiscal Art. 1057-V par. 4 (2026 data, source DGI e-Tax Form 430 instructions + Panamá Digital)

### Salary benchmarks (2026)

- Median monthly salary of employees, national (INEC Encuesta de Mercado Laboral Aug 2026, Cuadro 21): **B/.769.4** overall; financial + insurance B/.1,272.7; real-estate activities B/.859.6; information + communication B/.928.3; professional / scientific / technical B/.985.2; construction B/.762.8; hotels + restaurants B/.668.8; education B/.1,329.0; 3.9% of employees earn ≥B/.3,000/month (2026 data, source INEC)
  - Panama City vs elsewhere: the Aug 2026 survey publishes no salary table by province or district — do not read the national median as a Panama City figure
  - Boquete / Coronado expat zones: highly variable; no official series
- **Salario mínimo**: no single national rate — **Decreto Ejecutivo 13 of 31 Dec 2025** (GO 30438, in force 16 Jan 2026, repeals DE 1 of 2024) sets hourly rates by region, activity and firm size, from **B/.1.64/h** (small agricultural firms) to **B/.5.01/h** (international cabin crew); large retail firms Región 1 **B/.3.02/h** ≈ B/.628/month at 48 h/week (computed: 3.02 × 48 × 4.333); construction B/.3.51/h Región 1, B/.3.30/h Región 2; domestic workers **B/.350/month** Región 1, B/.320 Región 2. Región 1 includes the Panamá, San Miguelito, Arraiján, La Chorrera, Chame, David, Boquete and Bocas del Toro districts (2026 data, source Gaceta Oficial 30438)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SINAPROC (Sistema Nacional de Protección Civil)** | `https://www.sinaproc.gob.pa/` | Emergency response, hazards |
| **IMHPA — Instituto de Meteorología e Hidrología de Panamá** (successor to ETESA's Dirección de Hidrometeorología; created by Ley 209 of 22 Apr 2021, independent of ETESA since 2 Jan 2023 per IMHPA Informe de Gestión 2023) | `https://www.imhpa.gob.pa/es/` | Hydrometeorology |
| **IGN — Instituto Geográfico Nacional “Tommy Guardia”** (IGNTG, part of ANATI) | `https://ignpanama.anati.gob.pa/` | Geography |
| **IGC-UP — Instituto de Geociencias, Universidad de Panamá** | `https://sismosgeociencias.up.ac.pa/` | Seismic monitoring; events recorded in the last 7 days |

### Specific risks

- **Earthquake**: material hazard — Panama sits on the Panama microplate, bordered by the Cocos, Nazca, Caribbean and South America plates, and USGS describes earthquakes in the region as frequent (2026 data, source USGS event page us6000u18k, tectonic summary)
  - **Pacific Azuero peninsula** + **Bocas del Toro Caribbean** higher zones
  - **9 Oct 2026 Azuero earthquake — M7.7** (USGS; M7.6 per IGC-UP, cited by OCHA): epicentre 10 km WSW of Pitaloza Arriba; aftershocks M6.6 (9 Oct), M6.0 (10 Oct) and M6.1 (12 Oct); USGS PAGER orange alert for economic losses — [USGS event page](https://earthquake.usgs.gov/earthquakes/eventpage/us6000u18k) (2026 data, source USGS). SINAPROC preliminary balance No. 15 (cut-off 17 Oct 2026): 7,933 homes evaluated, 1,952 with total damage, 26,018 people affected (2026 data, SINAPROC via En Segundos, 19 Oct 2026 — secondary; check the latest SINAPROC balance). Damage concentrated in Los Santos, Veraguas, Coclé and Herrera; soil type partly explains why Chitré and Penonomé, farther from the epicentre, were hit harder than nearer areas (2026 data, OCHA Situation Report No. 03, 12 Oct 2026)
  - **USGS M≥6 count, Panama box (lat 7–10, lon −83 to −77)**: 2024 = 0, 2025 = 0, 1 Jan–23 Oct 2026 = 4 (all in the Oct 2026 sequence); M≥4 in the same box: 35 / 20 / 152 — [2024 count](https://earthquake.usgs.gov/fdsnws/event/1/count?format=geojson&starttime=2024-01-01&endtime=2024-12-31&minmagnitude=6&maxlatitude=10&minlatitude=7&maxlongitude=-77&minlongitude=-83) · [2026 count](https://earthquake.usgs.gov/fdsnws/event/1/count?format=geojson&starttime=2026-01-01&endtime=2026-10-23&minmagnitude=6&maxlatitude=10&minlatitude=7&maxlongitude=-77&minlongitude=-83) · [browsable search UI](https://earthquake.usgs.gov/earthquakes/search/?starttime=2024-01-01&endtime=2024-12-31&minmagnitude=6&maxlatitude=10&minlatitude=7&maxlongitude=-77&minlongitude=-83) (2026 data, source USGS FDSN; cross-check with IGC-UP) — the quiet years at ≥M6 (2024, 2025) preceded the 2026 M7.7
- **Flooding + landslide**: rainy season May–Nov, dry season Dec–Apr (central region: Veraguas, Coclé, Herrera — source Panama's Segunda Comunicación Nacional to the UNFCCC); Caribbean regions (Bocas del Toro, northern Ngäbe-Buglé, northern Veraguas, Colón, Guna Yala) get frequent rain all year with no marked dry-to-wet transition (2026 data, IMHPA via La Estrella de Panamá, 18 Apr 2026 — secondary)
  - **Nov 2024 rains**: SINAPROC COEN reported 199 landslides, most in Veraguas (92), Chiriquí (37) and Bocas del Toro (25), plus 80+ floods with close to 5,000 people affected (2024 data, source SINAPROC, 11 Nov 2024) — rates/figures may have changed since; the Cabinet declared a nationwide Estado de Emergencia Nacional (Resolución de Gabinete of 14 Nov 2024, Gaceta Oficial Digital No. 30159-A) — verify scope per address
- **Hurricanes**: **mostly outside hurricane belt** (Panama is south of typical paths)
- **Tsunami**: Caribbean coast residual risk; Pacific coast: a US tsunami-warning threat message followed the 9 Oct 2026 M7.7 and was later withdrawn (2026 data, BBC Mundo, 9 Oct 2026 — secondary; official bulletins at `https://www.tsunami.gov`)
- **Climate**: tropical wet — humidity year-round; rainfall variability increasing

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1980** | Asbestos common; older systems |
| **1980s–2000s** | Improving codes |
| **Post-2000** | Modern building standards |
| **From 30 Apr 2023** | REP-2021 structural design code in force (JTIA Resolución 020-2022 of 22 Jun 2022, Gaceta Oficial Digital No. 29594-A) |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Escritura pública at notario** | Mandatory closing |
| **Certificación del Registro Público** | Title verification (folio of finca) |
| **Paz y salvo de inmueble (finca)** — DGI (Impuesto de Inmuebles is national, not municipal) | DGI: required for transfer of a property |
| **DGI Formularios 106 + 107** (transfer tax + capital-gains declaration) | DGI: forms filed for the sale of a property |
| **Paz y salvo DGI of the company** (when seller or buyer is a persona jurídica) | Tax compliance (Notaría Duodécima de Panamá requirements list) |
| **IDAAN paz y salvo** (water, sewer, valorización charges) | Registro Público makes no property inscription without it where IDAAN serves (Ley 77 of 28 Dec 2001, Art. 49, per Panamá Digital) |
| **Paz y salvo de aseo** (waste-collection fees) | On the Notaría Duodécima requirements list; Ley 276 of 30 Dec 2021 ties it to Registro Público transactions (per Telemetro — secondary) |
| **Paz y salvo of the PH administration** (apartments) | On the Notaría Duodécima requirements list |
| **ENSA / Naturgy (EDEMET–EDECHI) electricity account** | Utilities — settle the final bill (not on the notary's transfer list) |
| **Survey (memoria descriptiva)** for newer fincas | Cadastre |

### Climate change projections

- **Warming (global reference, not downscaled to Panama)**: 2081–2100 vs 1850–1900, best estimate (very likely range) +1.8°C (1.3–2.4) under SSP1-2.6, +2.7°C (2.1–3.5) under SSP2-4.5, +4.4°C (3.3–5.7) under SSP5-8.5 (2021 data, source IPCC AR6 WGI SPM Table SPM.1 — rates/figures may have changed since); Panama-downscaled scenarios (SSP1-2.6 / SSP5-8.5; 2030 / 2050 / 2070) feed the Cuarta Comunicación Nacional (source MiAmbiente executive summary, 19 Jun 2023)
- **Sea-level rise**: global mean, 2100 vs 1995–2014, likely +0.32–0.62 m (SSP1-2.6), +0.44–0.76 m (SSP2-4.5), +0.63–1.01 m (SSP5-8.5) (2021 data, source IPCC AR6 WGI SPM B.5.3 — rates/figures may have changed since). Panama coasts by 2050 (median, medium confidence): mean permanent total water level 0.25 → 0.51 / 0.54 m on the Caribbean coast and 2.11 → 2.32 / 2.35 m on the Pacific coast vs 1993–2021 under SSP2-4.5 / SSP5-8.5, i.e. +0.26 / +0.29 m Caribbean and +0.21 / +0.24 m Pacific (computed; 2023 data, source MiAmbiente executive summary on sea-level-rise scenarios, 19 Jun 2023). Rise is larger on the Caribbean coast; Bocas del Toro, Costa Abajo de Colón and the Arco Seco coast are named as especially exposed (source CTCN marine-dynamics study for Panama, citing the Tercera Comunicación Nacional)
- **Increased rainfall variability** (drier El Niño / wetter La Niña)
- **Hurricane belt potential southward shift**

---

## Section: `--mains`

### Sources

- **IDAAN (Instituto de Acueductos y Alcantarillados Nacionales)**: `https://www.idaan.gob.pa/`
- **ASEP (Autoridad Nacional de los Servicios Públicos)** — regulator; publishes IDAAN tariffs and approves meter / installation charges: `https://asep.gob.pa/`
- **Electricity distribution**: ENSA (EPM holds 51%), EDEMET and EDECHI (Naturgy, 51%); the State holds 47.86–48.25%. The concessions expire in October 2028 and ASEP is preparing a public tender of the 51% private block, so the operator for an address may change (2025 data, TVN 18 Aug 2025 + BNamericas Jan 2026 — secondary; verify at ASEP)
- Universal in cities
- Rural cisterns + septic standard

### Costs

| Scenario | Cost (USD) |
|---|---:|
| IDAAN meter + installation charge (5/8"–3/4" residential, thermoplastic to bronze meter) | B/.73.47–200.16 (2023 data, source ASEP Res. AN 18168-Agua of 18 Jan 2023; stated validity to 31 Dec 2025 — rates/figures may have changed since) |
| IDAAN residential water + sewer, Panamá–Colón | B/.6.40 + B/.1.52 fixed per month, 30 m³ minimum consumption (source ASEP IDAAN tariff breakdown, undated, fetched 2026) |
| Mains connection | $500–$2,000 |
| Septic + cisterna | $2,500–$8,000 |
| Bored well | $3,000–$10,000 |

---

## Cost benchmarks (PA 2026)

| Work | Cost (USD) |
|---|---:|
| Survey (memoria descriptiva) | $500–$1,500 |
| Notario + escritura | data not publicly available — get the notario's quote (the 2% often quoted is the seller's ITBI, not a notary fee) |
| Registro Público fees | B/.10 per finca + B/.3.00 per B/.1,000 of value (0.3%), same again on a mortgage (2013 tariff, Resolución 212 — rates/figures may have changed since) |
| **Total transaction cost (buyer)** | **est. ~1–2%** of price on resale (registry + notary + lawyer, computed under `--tax`); the 2% ITBI + 3% income-tax advance are the seller's |
| Roof renovation | $2,500–$8,000 |
| Energy retrofit | $5,000–$20,000 |
| Solar PV (5kW) | $4,000–$8,000 |
| Hurricane retrofit (Bocas) | $5,000–$15,000 |

## Active fiscal incentives + visa programs (2025-2026)

### Residency programs

#### Pensionado (low pension threshold — USD 1,000/mo)

- **USD 1,000/month lifetime pension** (+ B/.250/mo per dependent). **B/.750/mo threshold if the applicant has bought property in Panama in their own name for more than B/.100,000**. Pension must be paid by a **foreign government, an international organisation or a private company** (private pensions need extra fund-manager proof) and **granted for life** (NOT a term annuity) (2026 data, source SNM PRP-JP requirements sheet citing Decreto Ejecutivo 320 of 2008 Art. 200).
- **Ley 6 of 16 June 1987 discounts** (Art. 1 as subrogated by Ley 15 of 1992, MICI-hosted text — rates/figures may have changed since): private hospitals and clinics 15% (when not covered by hospital insurance), doctor consultations 20%, dental and optometry 15%, prescription medicines 10%, interurban bus / train / boat 30%, air fares 25%, restaurants 25% (fast-food franchises 15%), hotels 50% Mon–Thu / 30% Fri–Sun, 50% of loan closing costs. Property-relevant: a 1-point cut in the interest rate on a mortgage for one's own home (not on statutory preferential-rate loans) and a freeze of impuesto de inmuebles on a sole home in the holder's name — confirm with the bank and the DGI how the freeze applies alongside Ley 66/2017
- Permanent residency
- Foreign-source income exempt (territorial)

#### Friendly Nations Visa

- **Modified by Decreto Ejecutivo 197 of 7 May 2021** and **Decreto Ejecutivo 226 of 20 July 2021** (Gaceta Oficial 29335), both in force **7 August 2021** — DE 226 Art. 3 moved DE 197's start date; Ecuador added to the list by Decreto Ejecutivo 16 of 31 Aug 2026 (SNM decree list)
- Three routes: **real estate ≥ B/.200,000** (own name, or a company / foundation of which the applicant is final beneficiary; may be financed by a local bank), **3-year fixed deposit ≥ B/.200,000** at a general-licence bank, or **employment** with a Panamanian employer + MITRADEL work permit (no investment) (2026 data, source SNM PPT-PE requirements sheet citing DE 226/2021)
- Provisional 2-year residence → permanent
- Operates under the **Decreto Ley 3 of 22 February 2008** migration framework (Servicio Nacional de Migración) — NOT "Ley 22/2006" (this is a misnumbering in some sources)

#### Qualified Investor Visa

- **Executive Decree 17 of 8 Sep 2026** (Gaceta Oficial 30613, 16 Sep 2026; in force on promulgation, Art. 21) subrogates Decree 722/2020 as amended by Decrees 109/2022 and 193/2024 (Art. 20). Real estate: **B/.300,000 first-sale** (new, unoccupied, transferred by the developer or its successor, Art. 4a; also off-plan via promesa de compraventa, Art. 7) or **B/.500,000 resale** (previously sold, occupied, leased or transferred to an unrelated third party, Art. 4b). Securities through an SMV-licensed Casa de Valores B/.500,000 (Art. 8); 5-year fixed deposit B/.750,000 at a private bank or B/.500,000 at Banco Nacional / Caja de Ahorros (Art. 9); funds must be the applicant's own and of foreign origin (Art. 2); hold at least 5 years (Art. 12); naturalisation possible after 5 consecutive years (Art. 14)
- Direct permanent residency; statutory maxima 15 business days for the MICI investment certificate (from admission of a complete file) + 30 business days for the SNM ruling (Art. 15)
- The earlier "planned USD 500k increase repeatedly deferred" framing is SUPERSEDED: B/.500,000 is now the resale-only tier. Transition: applications filed before 16 Sep 2026 keep the old rules; investments or binding contracts perfected before that date may use the old regime (B/.300,000 for any property) if filed within 6 months (Art. 19) — ~16 Mar 2027 (computed) (2026 data, source Gaceta Oficial 30613 + MICI 21 Sep 2026; `shared/visa-programs.md` row PA Qualified Investor)

### Tax incentives

- **Territorial tax**: no Panama income tax on foreign-source — UNIQUE
- **0% property tax up to USD 120k** cadastral value for a primary residence registered with the DGI as Patrimonio Familiar Tributario / Vivienda Principal (2026 data, source DGI)
- **No worldwide income tax** for territorial residents

## Common listing platforms

- **Encuentra24 Panama** — DOMINANT (largest portal self-count, 2026)
- **CompreoAlquile**, **InmoPanama**, **Panama Equity** (brokerage), **MLS ACOBIR** (brokers' MLS)
- **Realtor.com.pa** ❌ DEPRECATED — dead on 2026-10-23 (domain does not resolve); verify with Encuentra24 / InmoPanama
- USD economy = stable pricing

## Caveats unique to PA

- **USD economy** — no FX risk for USD holders; balboa is symbolic 1:1
- **Territorial tax** — no income tax on foreign-source income — UNIQUE in region
- **Pensionado visa** — low pension threshold (USD 1,000/mo lifetime)
- **Friendly Nations Visa** modified 2021 (in force 7 Aug 2021) — now B/.200,000 real estate or 3-year deposit, or a Panamanian job + work permit, with 2 years of provisional residence first; no longer "open" tourist-flip route
- **10-km international border restriction** — **CONSTITUTIONAL** (Constitución Art. 291) — foreign individuals and companies, **and Panamanian companies with any foreign capital**, cannot acquire national or private land less than 10 km from the borders, so an S.A. wrapper does not avoid it; the rule runs along the whole Costa Rica and Colombia frontiers (e.g. **parts of Bocas del Toro near Costa Rica + parts of Darién near Colombia**) — measure the parcel's distance. Island territory may be sold only for specific development purposes under Art. 291's conditions
- **Comarcas indígenas** (Guna Yala, Ngäbe-Buglé, Emberá-Wounaan, Naso Tjër Di): **collectively owned, foreigners cannot buy/lease titled land**. **San Blas islands fully off-limits to foreigners**
- **Rights of possession (derecho posesorio)** vs titulado — many rural/coastal parcels still derecho posesorio
- **Harder to mortgage and transact** with derecho posesorio
- **ANATI titling programs ongoing** (Land Registration + Titling Program)
- **Coastal concession (ROP — Restricted Public Zone)**: the public **ribera de playa** runs **22 m inland from the high-tide line (línea de alta marea) on the Pacific coast but only 10 m on the Atlantic / Caribbean coast, e.g. Bocas del Toro** (Ley 80 of 31 Dec 2009 Art. 2, Gaceta Oficial 26438-B); it is a municipal + **AMP (Autoridad Marítima de Panamá)**-administered government strip; concession-only, not freehold; foreigner access via concession is possible but discretionary (Decreto Ley 7 of 1998 / Código Agrario provisions). Behind it, the zona costera adjudicable (to 200 m from the high-tide line) can be titled under Ley 80; mangroves, indigenous / comarca land and protected areas cannot (Art. 10)
- **Banking secrecy + corporate-veil tradition** + use of S.A.s for property holding (common asset protection + estate)
- **Registro Público portal flaky** — recommend lawyer-mediated lookup
- **Earthquake risk** lower than CR; **Pacific Azuero + Caribbean Bocas higher zones**
- **Hurricane risk LOW** — Panama mostly south of typical Caribbean hurricane paths
- **Boquete + Coronado** = major expat retirees
- **Casco Viejo** = UNESCO heritage + premium pricing. **Régimen de incentivos**: **Decreto-Ley 9 of 27 August 1997**, updated by **Ley 136 of 31 December 2013** (Gaceta Oficial 27455-A), now amended by **Ley 519 of 27 April 2026** (Gaceta Oficial 30513, in force 29 April 2026), which repealed **Ley 53 of 4 July 2017** and extended the regime to the buffer zone including all of corregimiento **Santa Ana** and to Colón's Casco Antiguo (Art. 1). Current terms (articles of Ley 136 as amended): first transfer of a built / rebuilt / restored building exempt from ITBI if at least B/.50,000 was invested (Art. 20); transfers of unrestored buildings or land within 2 years of the law's entry into force exempt from ITBI (Art. 16 — counted from Ley 519's entry into force this runs to ~29 Apr 2028 (computed); confirm with the DGI); income-tax exemption on profits from commercial activities, sale or transfer of a restored building for 10 years from its occupancy permit (Art. 18); import-duty exemption on restoration materials / equipment not produced locally, with Dirección Nacional de Patrimonio Cultural certification (Art. 21); residential tenants may deduct rent for the first 5 years (Art. 22); incentives must be used within 20 years of entry into force (Art. 30) (2026 data, source Gaceta Oficial 30513). **30-year property-tax exemption** on the land and declared improvements of buildings built, rebuilt or restored that obtained their occupancy permit after Ley 136 took effect (Ley 136 Art. 19, Gaceta Oficial 27455-A, LEGISPAN text; Art. 19 is not among the articles Ley 519 Art. 35 amends).

## Reddit / forum sources

- **r/Panama**, **r/panamaexpats**, **r/expats**
- **r/MoveToPanama** (smaller; activity unverified in 2026)
- **The Panama News** (`https://www.thepanamanews.com/` — use the root only; old `/pn/v_*` archive URLs now serve casino spam), **Newsroom Panama** (`https://newsroompanama.com/`, publishing daily in 2026) (English)
- **Living in Panama** (expat forum)

## Verification authorities

| Authority | When to call |
|---|---|
| **Registro Público de Panamá** | Title verification |
| **ANATI** | Cadastre + titling programs (derecho posesorio) |
| **Notario público** | Mandatory closing |
| **Municipalidad** | Building permits (Panamá district: Dirección de Obras y Construcciones); Impuesto de Inmuebles is DGI, not municipal |
| **DGI (Dirección General de Ingresos)** | Impuesto de Inmuebles + paz y salvo de inmueble; sale forms 106 + 107 |
| **SNM (Servicio Nacional de Migración)** | Visa applications |
| **ATP** | If short-let |
| **IDAAN** | Water connection + paz y salvo (required for Registro Público inscriptions where IDAAN serves) |
| **SINAPROC** | Hazard zone + post-disaster damage balances |
| **IGC-UP (Instituto de Geociencias, Universidad de Panamá)** | Seismic record near the address |
| **ASEP (Autoridad Nacional de los Servicios Públicos)** | Water + electricity tariffs; IDAAN meter / installation charges |

## Source URL templates

| Source | URL pattern |
|---|---|
| Registro Público | `https://www.rp.gob.pa/` |
| ANATI | `https://www.anati.gob.pa/` |
| INEC | `https://www.inec.gob.pa/` |
| Encuentra24 PA | `https://www.encuentra24.com/panama` |
| CompreoAlquile | `https://www.compreoalquile.com/` |
| SINAPROC | `https://www.sinaproc.gob.pa/` |
| IMHPA — Instituto de Meteorología e Hidrología de Panamá (ex-ETESA) | `https://www.imhpa.gob.pa/es/` |
| IDAAN | `https://www.idaan.gob.pa/` |
| DGI (tax) | `https://dgi.mef.gob.pa/` |
| SNM (migration) | `https://www.migracion.gob.pa/` |
| IGC-UP seismic event list | `https://sismosgeociencias.up.ac.pa/` |
| USGS earthquake search | `https://earthquake.usgs.gov/earthquakes/search/` |
| ASEP (utility regulator) | `https://asep.gob.pa/` |
| Datos Abiertos (ENA corridor aforo) | `https://www.datosabiertos.gob.pa/` |
| Gaceta Oficial | `https://www.gacetaoficial.gob.pa/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Last verified**: 2026-05-27 (validation sweep — 10km border zone correct per Const. Art. 291; DGI URL → dgi.mef.gob.pa; Decreto-Ley 9/1997 + Ley 136/2013 + Ley 53/2017 Casco Antiguo incentives (Ley 53/2017 superseded: repealed by Ley 519 of 27 Apr 2026); Decreto Ejecutivo 197 of 7 May 2021 Friendly Nations; Decreto Ley 3/2008 migration framework; Pensionado $750 with $100k RE buy; Qualified Investor $300k retained (superseded: Executive Decree 17 of 8 Sep 2026 sets B/.300,000 first-sale / B/.500,000 resale); ITBMS 10% hotel-classed STR; CGT 3% advance may be elected DEFINITIVE; ROP 22 m from línea de pleamar máxima + AMP (superseded: Ley 80/2009 Art. 2 sets 22 m Pacific / 10 m Caribbean from the línea de alta marea)).
**Coverage check**: pricing (Panama Equity Q1 2026 asking averages + ACOBIR MLS H1 2026 closed sales for Panama City; Albrook / Clayton and provincial rows TheLatinvestor + Global Property Guide), traffic (MOP + ENA corridor aforo; bands curated), tax (Impuesto de Inmuebles DGI scales + ITBI 2% and 3% income-tax advance on the seller + Ley 546/2026 new-home ITBI regime + ITBMS 7% on leases + 10% CGT + territorial system), rental (Ley 93/1973 + Ley 80/2012 45-day rule + ATP + ITBMS + ACOBIR MLS rents), work (INEC EML Aug 2026 medians + DE 13/2025 minimum wages + ITBMS B/.36,000 threshold), risks (9 Oct 2026 M7.7 Azuero earthquake + Nov 2024 floods + IPCC AR6 / MiAmbiente projections + paz y salvo list), mains (IDAAN + ASEP tariffs + electricity distributors).
**Confidence**: HIGH for the residency programmes — Qualified Investor split B/.300,000 first-sale / B/.500,000 resale (Executive Decree 17 of 8 Sep 2026, Gaceta Oficial 30613 + MICI), Pensionado (SNM), Friendly Nations (Gaceta Oficial 29335 + SNM); HIGH for the Impuesto de Inmuebles scales (DGI), ITBI 2% + 3% advance on the seller (Ley 106 Art. 1), the Ley 546/2026 new-home ITBI regime and the ITBMS lease rule (Código Fiscal Art. 1057-V); HIGH for the territorial system and the 10% CGT / 3% definitive election (PwC Worldwide Tax Summaries, reviewed 4 Aug 2026); HIGH for the 10-km border rule (Const. Art. 291), comarca land generally not purchasable (MINGOB / ONPAR), the ribera de playa widths (Ley 80/2009) and the Casco Antiguo regime (Ley 519/2026, Ley 136 Art. 19); HIGH for the `--work` figures (INEC EML Aug 2026, DE 13/2025, DGI); HIGH for the US dollar as legal tender at par with the balboa (Código Fiscal Art. 1171 ¶2, quoted in Superintendencia de Bancos Circular 35-2000 of 27 Jul 2000). MEDIUM for `--price` (Panama City rows are Panama Equity Q1 2026 asking averages and small-sample ACOBIR MLS closed sales — secondary / industry tier; Albrook / Clayton, the provincial rows and the yields date from the 2026-04 research), `--rental` (Ley 93 and Ley 80/2012 Art. 21 primary-sourced; the municipal licence, Boquete HOA, Bocas overlay, 1–3 year norm and 7% ITBMS on commercial rent are unverified; PL 713/2026 is pending, not law) and `--risks` (USGS, SINAPROC, IPCC AR6 and MiAmbiente re-checked; hurricane-belt claims, build-era boundaries and Bocas as a higher seismic zone unverified). MEDIUM for the Finca / Tomo / Folio identifier (not re-checked against Registro Público documentation). LOW for the postcode examples (secondary aggregator only), `--traffic` volumes and bands (no public MOP TPDA dataset found; Corredor Sur calibration secondary; bands curated), the `--mains` connection / septic / well costs and the market-price rows in Cost benchmarks (no published source); notary fees are data not publicly available.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | INEC EML Aug 2026 median salaries (Cuadro 21), DE 13/2025 minimum-wage rates (Gaceta Oficial 30438) and the ITBMS B/.36,000 threshold (DGI) checked; TecoLoco → EstasContratado, CompTrabajo → Computrabajo; Aviso de Operación, SA and LinkedIn rows not re-checked |
| Active fiscal incentives + visa programs (2025-2026) | 2026-10-23 | 2026-10-23 refresh wave | Pensionado (SNM PRP-JP sheet, Ley 6/1987 text), Friendly Nations (DE 197 + DE 226, Gaceta Oficial 29335; SNM), Qualified Investor restructured by Executive Decree 17/2026 (Gaceta Oficial 30613; MICI) and the 0% Inmuebles band (DGI) checked; how the Ley 6 property-tax freeze applies alongside Ley 66/2017 is open |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Realtor.com.pa ❌ DEPRECATED (domain does not resolve); Panama Equity labelled a brokerage; MLS ACOBIR added; Encuentra24's lead rests on portal self-counts |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Property tax moved from Municipalidad to DGI; DGI and IDAAN roles made specific; IGC-UP and ASEP added; Registro Público, ANATI, Notario, SNM and ATP confirmed |

Sections without a row default to the Status footer date (2026-04-26). Country profile, `--price`, `--traffic`, `--tax`, `--rental`, `--risks`, `--mains`, Cost benchmarks, Caveats, Reddit / forum sources and Source URL templates were partly re-checked on 2026-10-23 but keep unverified items (see Update history), so they keep the footer date.

## Extension TODOs

- [ ] Per-province property tax variations
- [ ] 10-km border zone overlay (Costa Rica + Colombia frontiers)
- [ ] Comarcas indígenas perimeter map
- [ ] Derecho posesorio → titulado conversion flow (ANATI titling)
- [ ] Pensionado vs Friendly Nations vs Qualified Investor decision tree
- [ ] Ribera de playa per-parcel check (22 m Pacific / 10 m Caribbean from the línea de alta marea, Ley 80/2009 Art. 2; see Caveats)
- [ ] Casco Viejo heritage-restoration constraints
- [ ] Bocas del Toro hurricane vulnerability zoning
- [ ] SA property-holding structure for asset protection
- [ ] Foreign-source income territorial tax planning

## Update history

- **2026-04-26** — Initial population (researched 2026-04)
- **2026-05-27** — Validation sweep (Tier-1 corrections): 10-km border rule tied to Const. Art. 291, DGI URL, Casco Antiguo incentive laws, Friendly Nations DE 197/2021, Decreto Ley 3/2008 migration framework, Pensionado $750 with a property purchase, Qualified Investor $300k, ITBMS 10% on hotel-classed short lets, CGT 3% definitive election, ROP strip
- **2026-05-29** — Anti-hallucination sweep: est. labels on the price trend and climate projections; "most generous in LatAm" Pensionado wording removed
- **2026-06-04** — USGS 2024 line corrected to zero M≥6 events in the Panama box
- **2026-09-18** — Citation repair and source audit: MOP, IMHPA and IGN URLs re-pointed; USGS FDSN count link added; IMHPA named as ETESA's successor
- **2026-10-23** — Refresh wave (market, tax-legal, risk-infra) against primary sources where available, secondary sources labelled; playbook-level date not re-stamped because `--price`, `--tax`, `--rental`, `--risks` and `--mains` keep unverified items. Counts are changed / confirmed / unverifiable:
  - **Re-verified** (see Per-section verification): `--work` 4 / 4 / 3; Active fiscal incentives + visa programs 9 / 12 / 1; Common listing platforms 2 / 4 / 0; Verification authorities 4 / 5 / 0
  - **Refreshed, not fully re-verified**: Country profile 4 / 3 / 2; `--price` 9 / 6 / 6; `--rental` 5 / 5 / 5; Reddit / forum sources 1 / 3 / 3; `--tax` 10 / 13 / 2; Cost benchmarks 3 / 0 / 5; Caveats 4 / 4 / 3; `--traffic` 2 / 2 / 3; `--risks` 9 / 6 / 5; `--mains` 2 / 0 / 6; Source URL templates 1 / 7 / 3
  - Main changes: Qualified Investor Visa restructured by Executive Decree 17 of 8 Sep 2026 (B/.300,000 first-sale / B/.500,000 resale; the "USD 300k retained, increase deferred" framing superseded); Friendly Nations in force 7 Aug 2021 (DE 226) with Ecuador added in 2026; Pensionado thresholds and Ley 6/1987 discounts from the SNM sheet and the statute text; ITBI 2% + 3% advance placed on the seller (Ley 106 Art. 1), Ley 546/2026 new-home ITBI regime, ITBMS 7% on leases with the dwelling-over-6-months exemption, Registro Público tariff (Resolución 212/2013) and the buyer-side total recomputed to est. ~1–2% (was ~3–4%); notary fees marked data not publicly available; Panama City price rows re-sourced to Panama Equity Q1 2026 + ACOBIR MLS closed sales (−1.7% YoY, computed), replacing the ~+3% est.; Realtor.com.pa ❌ DEPRECATED; Ley 93 filing and term rules, the Distrito de Panamá 45-day rule (Ley 80/2012 Art. 21) and PL 713/2026 (pending); resident income-tax bands; the non-resident "25% withholding" line removed; INEC EML Aug 2026 salary medians and DE 13/2025 minimum wages; 82 districts + 699 corregimientos, Spanish official (Const. Art. 7), postcode examples (secondary); ribera de playa 22 m Pacific / 10 m Caribbean from the línea de alta marea (Ley 80/2009); Casco Antiguo regime updated for Ley 519/2026 (Ley 53/2017 repealed); the 9 Oct 2026 M7.7 Azuero earthquake replaces the "low-moderate" framing, USGS counts re-run for 2024–2026; Nov 2024 floods sourced to SINAPROC and the Gaceta; climate projections moved to IPCC AR6 + MiAmbiente 2050 coastal figures; paz y salvo de inmueble moved from municipal to DGI, IDAAN / aseo / PH paz y salvo rows and REP-2021 added; ASEP, IDAAN meter charges and the electricity concessions under `--mains`; ENA aforo source and a Corredor Sur calibration (secondary) under `--traffic`; IGC-UP, USGS, ASEP, Datos Abiertos and Gaceta Oficial URLs added
  - Follow-up consistency fixes: Status Coverage and Confidence lines recomputed; three superseded items in the 2026-05-27 sweep line marked; USD legal tender at par traced to Código Fiscal Art. 1171 (quoted in Superintendencia de Bancos Circular 35-2000 of 27 Jul 2000); ribera de playa Extension TODO aligned with Ley 80/2009; per-section verification table added
  - Not re-verified: Finca / Tomo / Folio + Documento Redi identifier, an official postcode list, Albrook / Clayton and the provincial price rows + yields, the "INEC publishes no per-m² series" negative, the short-let municipal licence, Boquete HOA and Bocas overlay lines, the 1–3 year contract norm, 7% ITBMS on commercial rent, lawyer fees (secondary only), the survey / roof / retrofit / solar / hurricane-retrofit cost rows, the San Blas and concession-discretion caveats, the earthquake (lower than CR) and hurricane caveats, MOP as a TPDA source + the Av Balboa / Cinta Costera volumes + the traffic bands, the hurricane-belt claims, build-era boundaries + pre-1980 asbestos, Bocas as a higher seismic zone, the mains connection / septic / well costs and coverage lines, r/MoveToPanama, r/expats and the "Living in Panama" forum, and the Encuentra24, CompreoAlquile and IDAAN URLs (could not be read for verification on 2026-10-23)
