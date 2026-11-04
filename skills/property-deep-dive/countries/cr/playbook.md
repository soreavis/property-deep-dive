# Costa Rica 🇨🇷 — Property Due-Diligence Playbook

ISO2: `cr`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits = province + canton + district code (`10101` San José, `20101` Alajuela, `30101` Cartago, `40101` Heredia; province codes 1 San José, 2 Alajuela, 3 Cartago, 4 Heredia, 5 Guanacaste, 6 Puntarenas, 7 Limón) (2026 data, source Correos de Costa Rica `https://correos.go.cr/codigo-postal` + Registro Nacional IGN *División Territorial Administrativa 2022*)
- **Admin levels**: 7 provinces + 84 cantones + 492 distritos (2022 data, source Registro Nacional IGN *División Territorial Administrativa 2022* — district count changes by decree; rates/figures may have changed since)
- **Currency**: **CRC** (Costa Rican colón); 1 USD ≈ 449–456 CRC (BCCR reference buy/sell rate, 1–3 Nov 2026; the rate fell 9.5% year on year to 23 Oct 2026 per BCCR *Informe de Política Monetaria*, Oct 2026); 1 EUR ≈ 500–515 CRC (computed: BCCR USD rate × EUR/USD 1.12 from the BCCR euro table, 20–22 Oct 2026) — rates fluctuate, check BCCR *tipo de cambio* `https://sdd.bccr.fi.cr/es/IndicadoresEconomicos/Inicio/Contenedor/6?Cuadro=1`
- **Languages**: Spanish (official — Constitución Política art. 76, which also commits the State to national indigenous languages); English widely used in tourist + expat zones
- **Cadastre — CENTRALIZED (strongest digital infra in LatAm)**:
  - **Registro Nacional**: `https://www.rnpdigital.com/`
  - **SIRI** (Sistema de Información del Registro Inmobiliario) — online property study; integrated cadastral map + registry data, in production since 30 Apr 2015 (source Registro Nacional, Registro Inmobiliario): `https://siri.rnp.go.cr/SIRI/index.jsp`
  - **Ventanilla Digital** — document e-filing
  - Certificación literal + plano catastrado online
- **Identifier**: **Folio Real** (provincia-finca-derecho format) + **plano catastrado** (province prefix-number-year, e.g. `SJ-123456-2019`, per listing-agency guide realestategrupo.com — verify on the Registro Nacional plano certificate)
- **Ownership types**: dominio pleno (freehold); usufructo; servidumbre; **concesión marítimo-terrestre** (Maritime Zone, **Ley 6043 / 1977**)

## Section: `--price`

### Primary sources

- **BCCR (Banco Central de Costa Rica)**: `https://www.bccr.fi.cr/` — quarterly construction indicators: IPi-CTR construction-input price index by building type (incl. middle- and upper-class housing) + ETAPCP private-construction survey (2026 data, source BCCR CP-BCCR-018-2026 + IPi-CTR methodology note); for sale prices use listing aggregates — Costa Rica has no public sold-price registry (per Realty ONE Group CR market-report methodology, 2026)
- **INEC**: `https://www.inec.cr/` — Encuesta Nacional de Hogares housing data
- **CCSS housing surveys**

### Listing platforms

- **Encuentra24** — DOMINANT: `https://www.encuentra24.com/costa-rica`
- **MLS Costa Rica**: ❌ DEPRECATED — dead on 2026-10-23 (`mlscostarica.com` serves a domain-parking page); verify with Registro Nacional (SIRI) for any listing
- **CRPropertyExpert**: ❌ DEPRECATED — dead on 2026-10-23 (`crpropertyexpert.com` does not resolve); verify with Registro Nacional (SIRI)
- **Properties in Costa Rica** (`https://www.propertiesincostarica.com/`), **Coldwell Banker CR** (`https://www.coldwellbankercostarica.com/`)
- **Realty ONE Group CR market report**: `https://realtyonegroup.cr/en-US/market-report` — median asking prices by zone, de-duplicated across 17 listing sources (broker-published, listing tier)
- High **English-language presence** (expat-driven market)

### Price benchmarks (2026 data — median ASKING price per m² of published area, source Realty ONE Group CR market report, listings de-duplicated across 17 sources, 3 Nov 2026 snapshot; listing tier, not sold prices. † = early-2026 broker-aggregate figure, not re-verified — figures may have changed since)

| Region | USD/m² (typical) | Notes |
|---|---:|---|
| **Escazú/Santa Ana houses** | $1,662 median (n=4,033) | Premium Central Valley; median asking price $590,000 |
| **Escazú/Santa Ana condos** | $2,168 median (n=841); apartments $2,409 (n=2,082) | Premium condos; 4 Nov 2026 snapshot |
| **Gran San José (Heredia · Alajuela · Cartago) houses** | $1,414 median (n=5,851); apartments $2,513 (n=1,738) | GAM outside Escazú/Santa Ana; 4 Nov 2026 snapshot |
| **San José central** † | mixed (older stock) | $800–$1,500 |
| **Tamarindo / Nosara / Coco condos** | $3,083–$3,756 median by zone (Coco · Papagayo · Liberia $3,083, n=379; Nosara · Sámara $3,238, n=63; Tamarindo $3,756, n=340) | Pacific coast premium |
| **Tamarindo / Nosara / Coco houses** | $2,798–$3,229 median by zone (Coco · Papagayo · Liberia $2,798; Nosara · Sámara $2,973; Tamarindo $3,229) | median asking price $650,000 (Nosara · Sámara) to $987,500 (Tamarindo); varies hugely |
| **Jacó / Manuel Antonio** | $2,147–$2,295 (houses: Jacó · Los Sueños · Playa Hermosa $2,147, n=1,163; Manuel Antonio · Quepos $2,295, n=575) | Pacific |
| **Atenas / Grecia hills** | lots $240/m² median (n=193); houses $1,500 (n=1,997) — Atenas · Grecia · San Ramón zone; verify any lot with plano catastrado + comparable transactions | Inland mountain |
| **Liberia / Guanacaste interior** † | $700–$1,200 | Lower coast; Liberia is pooled with Coco · Papagayo in the Realty ONE report |
| **Limón Caribbean** † | $400–$900 | Underdeveloped; the Puerto Viejo · Cahuita tourist enclave lists far higher (houses $2,400/m² median, n=276, Nov 2026) |

**GAM land**: vacant-lot asking prices average US$358/m² (1,546 listings, June 2026; range $30–$2,340; 72% under $500/m²) (2026 data, source Observatorio Inmobiliario de la GAM, Escuela de Economía UCR, in *Balance y Tendencias del Sector Vivienda 2025* — listing-based, not sold prices).

**2026 outlook**: est. +7-12% in premium areas (inference, not a sourced forecast — verify against listing-trend data; there is no public sold-price index to check it against).

### Compute

1. USD/m² = price / **área de construcción** (built area)
2. Cross-check **SIRI literal certificate** + listing asking prices (Encuentra24; Realty ONE Group CR zone medians)
3. **Maritime Zone properties**: confirm titulado vs concesión (HUGE difference)

### Key terms

- Folio Real = title identifier (provincia-finca-derecho)
- Plano catastrado = registered cadastre plan
- Zona Marítimo-Terrestre = Maritime Zone (50m public + 150m concession)
- Pensionado / Rentista / Inversionista = residency programs
- Sociedad Anónima (SA) = corporación commonly used to hold property
- Pura vida = "pure life" (national motto + lifestyle)

---

## Section: `--traffic`

### Sources

- **MOPT (Ministerio de Obras Públicas y Transportes)**: `https://www.mopt.go.cr/` — Secretaría de Planificación Sectorial TPDA portal `https://tpda.mopt.go.cr/transito/tpd.php` (historic TPDA per counting station, searchable by route, sección de control or station; PDF + Excel export) and the yearly *Anuario de Información de Tránsito* (2023 edition published 2024)
- **CONAVI** (Consejo Nacional de Vialidad): `https://www.conavi.go.cr/`
- **Lanamme UCR**: `https://www.lanamme.ucr.ac.cr/` — road counting + research

### Key term

**TPDA (Tránsito Promedio Diario Anual)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, Carretera Interamericana segments)
- 🔴 > 35,000 v/d (San José Circunvalación — Ruta 39 temporary-station TPDA 50,944–69,582 v/d in 2017–2022 counts, one 2021 count 34,910; Ruta 27 Próspero Fernández — station PK 0+500 TPDA 36,616 v/d in 2023; Ruta 1) (2023 data, source MOPT *Anuario de Información de Tránsito 2023* — rates/figures may have changed since)

---

## Section: `--tax`

### Annual property tax — Impuesto sobre Bienes Inmuebles (**Ley 7509, 1995**)

- **0.25% of registered value** (Ley 7509 art. 23); annual tax, paid annually, semi-annually or in four quarterly instalments as each municipalidad decides (art. 22)
- **VERY LOW** (one of lowest in Americas)
- Exemption: an individual's only property (*bien único*) up to 45 salarios base, tax due on the excess (art. 4(e)) — computed CRC 20,799,000 at the 2026 salario base of CRC 462,200 (2026 data, source Poder Judicial)
- Municipalities administer collection; owners must declare the property value at least every 5 years (art. 16)
- ZMT and border-strip concessionaires, permit holders and occupants pay this tax only on buildings and fixed installations; the land pays the municipal canon instead (art. 6(c))
- Source: Ley 7509 arts. 4(e), 6(c), 16, 22, 23 — SINALEVI (art. 23) + Ministerio de Hacienda consolidated text via FAOLEX (2026-10-23 verified)

### Transaction taxes

- **Impuesto de Traspaso**: **1.5%** (Ley 6999 art. 8); seller and buyer owe it in equal parts and are jointly liable (art. 6) — who finally bears it is a contract point
- **Registry fee** (arancel de Registro, Ley 4564 art. 2(b)): **0.5%** of the higher of declared and registered value
- **Timbre municipal** (Código Municipal art. 93): **0.2%**
- **Timbre agrario** (Ley 5792 art. 14(e)): **0.15%**; housing up to the Impuesto Solidario exempt value (CRC 143M in 2026) **0.125%**; social-interest housing 0.1%
- **Colegio de Abogados stamp**: fixed tiers, CRC 55,000 above CRC 500M (Decreto 41457-JP art. 108); archive stamp CRC 20; no timbre fiscal on testimonios issued from 4 Dec 2024 (Ley 10586) (2025 data, source Registro Nacional — Guía de Calificación Registral Inmobiliaria v1.17, Oct 2025)
- **Notary fees** (escritura, Decreto 41457-JP art. 74): marginal scale — 2% to CRC 11M, 1.5% to CRC 16.5M, 1.25% to CRC 33M, 1% above, minimum CRC 60,500; the arancel is a floor, and its colón brackets are indexed every two years (art. 113) — confirm the current table with the notary
- **Total mandatory**: **≈3.4–3.5%** at CRC 100M–500M (computed: 1.5% + 0.5% + 0.2% + 0.125–0.15% = 2.33–2.35%, plus notary ≈1.18% at CRC 100M / ≈1.04% at CRC 500M)

### Other taxes

- **IVA 13%** (Ley 6826 art. 10, as replaced by **Ley 9635** of 3 Dec 2018, effective 1 Jul 2019) does **not** apply to the sale of real estate: transfers taxed under Ley 6999 are outside IVA (Ley 6826 art. 9(3)). New builds carry it through **construction services**, at 13% since 1 Sep 2023 after the Transitorio V Bis phase-in (CFIA), so it sits inside developer pricing; commercial rent is taxed at 13% (micro / small MEIC- or MAG-registered tenants exempt up to 1.5 salarios base, art. 8(10)) (2026 data, source Ley 6826 consolidated text via vLex + CFIA help centre).
- **Impuesto Solidario** (Ley 8683, luxury home tax) — **2026 exempt threshold CRC 143M**, tested on the fiscal value of the construction incl. fixed and permanent installations; above it the base is the fiscal value of the dwelling property — per **Decreto Ejecutivo 45358-H (9 Dec 2025, Alcance 164 a La Gaceta 239 del 19 dic 2025)**; marginal (progressive) schedule:
  - ≤ CRC 359M: 0.25%
  - CRC 359M – 720M: 0.30%
  - CRC 720M – 1,081M: 0.35%
  - CRC 1,081M – 1,443M: 0.40%
  - CRC 1,443M – 1,800M: 0.45%
  - CRC 1,800M – 2,162M: 0.50%
  - > CRC 2,162M: 0.55%
  - Filing and payment deadline 15 January (15 Jan 2026 for the 2026 period); threshold and brackets are re-indexed to CPI every December, so the 2027 decree is due December 2026 (2026 data, source SINALEVI — Decreto 45358-H art. 1 + considerandos + EY Tax Alert).

### Capital gains (Ley 9635, CGT 15% effective 1 Jul 2019)

- **CGT rate: 15%** on the net gain (Ley 7092 art. 31 ter, introduced by Ley 9635, eff. 1 Jul 2019).
- **Primary-residence exemption (vivienda habitual)**: sale of the habitual residence is EXEMPT, provided this can be evidenced (Ley 7092 art. 28 bis(7)) — also when the home is held by a company indubitably used as the owners' habitual home.
- **Assets acquired before 1 Jul 2019** — on the **first sale** only, the seller may opt for **2.25% of the sale price** instead of 15% on the net gain (Ley 7092 art. 31 ter).
- **Property held in a business activity** (habitual trader, developer, company) — gain taxed inside the profits tax (Ley 7092 arts. 1, 27 bis), NOT the 15% CGT: **30%** general corporate rate; small companies with gross income ≤ CRC 119,174,000 use a 5% / 10% / 15% / 20% scale (2026 data, source PwC Tax Summaries, reviewed 30 Jun 2026).
- **Non-domiciled seller** — buyer must **withhold 2.5% of the total agreed price** (Ley 7092 art. 28 ter; form 129 under MH-DGT-RES-0051-2025, 30 Sep 2025). RES-0051 also repealed MH-DGT-RES-0039-2025, so the 2% withholding it had set for domiciled sellers does not apply.

(2026-10-23 verified, source Ley 7092 arts. 28 bis, 28 ter, 31 ter — PGR Ley 9635 text + SINALEVI MH-DGT-RES-0051-2025 + PwC Tax Summaries CR, reviewed 30 Jun 2026. Prior playbook framing inverted the rule — sporadic individual sellers pay 15% CGT; only the vivienda habitual is exempt; traders pay 30%, not the other way around.)

### Total transaction cost (buyer side)

- Resale: **≈3.4–3.5%** in taxes, stamps and notary at CRC 100M–500M (computed: 1.5% traspaso + 0.5% registro + 0.2% timbre municipal + 0.125–0.15% timbre agrario + ≈1.04–1.18% notary scale), before title-study / lawyer fees; split between the parties per contract (traspaso legally 50/50, Ley 6999 art. 6)
- New build from a developer: same transfer costs; no IVA on the sale itself, but 13% IVA on construction services is built into the developer price

### Future risk

- **Investor visa threshold CONTESTED after 14 Jul 2026**: Ley 9996 art. 8 set US$150k (down from US$200k) "por el plazo que establece la presente ley", and art. 12 let applicants opt into the art. 5 incentives only during the first five years — a window that closed 14 Jul 2026 (computed from publication in La Gaceta 135 of 14 Jul 2021). Reglamento 43926 art. 4 states US$150k with no end date, and its art. 31 repealed Reglamento de Extranjería art. 87, where the US$200k floor sat; CR lawyers disagree on whether US$150k survives (AG Legal / PropScan: yes, DGME web page showing it on 6 Oct 2026 per PropScan; Mora Yglesias, Aug 2026: open question). Confirm in writing with DGME before committing capital (2026-10-23 verified, source Ley 9996 text via vLex + Reglamento 43926 Gaceta text + named secondary opinions).
- **CGT framework stable for property in CR** (Ley 9635 reform retained — primary residence exempt, 15% on other gains or 2.25% of price on the first sale of pre-Jul-2019 assets, business-held property inside the profits tax at the 30% general corporate rate, with lower scales for small companies and self-employed sellers) (2026 data, source PGR Ley 9635 text + PwC Tax Summaries CR, reviewed 30 Jun 2026). **Bill to watch**: expediente 25.796, filed by the Executive on 22 Sep 2026 and published 30 Sep 2026, would tax CR tax residents on passive foreign-source income, including rents and capital gains from assets abroad; no enactment found as of 2026-11-04, so check its status with the Asamblea Legislativa (2026 data, source KPMG Costa Rica + PwC tax alerts).

---

## Section: `--rental`

### Long-term residential

- **Ley General de Arrendamientos Urbanos y Suburbanos** (**Ley 7527**, 10 Jul 1995)
- **Tenant protection moderate**
- **Minimum term 3 years**: housing leases agreed for less, or with no term, are deemed 3-year leases; tacit renewal for a further 3 years unless the landlord gives ≥3 months' notice before expiry (Ley 7527 arts. 70–71, statute text via bufetedecostarica.com, 2026)
- **Annual rent-increase cap** (Ley 7527 art. 67, reformed by Ley 9354/2016): housing leases priced in colones may rise once per contract year by at most the 12-month CPI inflation (MIVAH sets the rate when inflation exceeds 10%); MIVAH publishes the index to apply — **0.34%** for September 2026 (2026 data, source MIVAH *Reajuste Precio Alquiler de Vivienda* `https://www.mivah.go.cr/Reajuste_Precio_Alquileres_Vivienda.shtml`). Housing leases priced in a foreign currency (e.g. USD) keep the agreed rent for the whole term, with no annual increase (art. 67 last paragraph, statute text via bufetedecostarica.com)
- **Asking rents** (median, listing aggregate): Gran San José $1,450/mo (n=4,807); Jacó · Los Sueños $1,800/mo (n=102); Tamarindo $2,200/mo (n=108) (2026 data, source Realty ONE Group CR market report, 4 Nov 2026 snapshot — asking, not contracted rents)

### Short-let

- **ICT (Instituto Costarricense de Turismo)** registration **mandatory** under **Ley 9742** (Ley Marco para la Regularización del Hospedaje no Tradicional, 29 Oct 2019) arts. 10–11; operating unregistered, or without updating the registry data, is illegal operation under art. 14 (2026 data, source ICT *Registro de Hospedaje No Tradicional*): `https://www.ict.go.cr/es/servicios-institucionales/registro-de-hospedaje-no-tradicional.html`
- Some HOAs prohibit
- **Tax**: 13% IVA on lodging stays under one month + income tax — see *Tax on rental* below

### Tax on rental

- **Individuals (default)**: *rentas de capital inmobiliario* — 15% on gross rent after a flat 15% deduction (effective 12.75% of gross), declared monthly on TRIBU-CR form 116 (formerly ATV D-125) (Ley 7092 arts. 27 ter, 29, 31 ter; source Hacienda *Deberes Tributarios sobre Hospedajes No Tradicionales*, 2024 guide, + Hacienda *Nueva codificación de declaraciones en TRIBU-CR*; 12.75% effective rate reconfirmed by a 2026 accountancy guide)
- **Profits-regime option**: real expenses deductible, progressive individual scale up to 25% (2026 data, Decreto 45333-H per Deloitte + EY tax alerts); requires at least one employee reported to CCSS and a 5-year minimum (2021 data, source Hacienda *Rentas de capital inmobiliario* presentation — rates/figures may have changed since)
- **Non-residents**: 15% withholding (not re-verified; Ley 7092 art. 28 excludes from the capital-income tax any income taxed as *remesas al exterior* — confirm the regime with a CR contador)
- **IVA 13%** on lodging stays under one month, charged by the host and declared monthly on TRIBU-CR form 150 (formerly ATV D-104) (source Hacienda guide + TRIBU-CR codification above; 13% reconfirmed 2026)

---

## Section: `--work=<profession>`

### Sources

- **MTSS (Ministerio de Trabajo y Seguridad Social)**: `https://www.mtss.go.cr/`
- **Encuentra24 Empleos**, **Computrabajo CR**, **LinkedIn CR**, **Elempleo.com**

### Self-employment

- **Régimen General / Régimen Simplificado (RTS)** for tax (Hacienda terminology)
- **CCSS** social security mandatory
- **Profesión Liberal** for licensed professionals

### Salary benchmarks (2025)

- **National median labour income**: ₡420,000/month (≈ $925 at ₡454/USD, computed) (2025 data, source Programa Estado de la Nación, *Informe Estado de la Nación 2025*)
- Median monthly gross (est. — regional ranges unsourced, figures may have changed since; verify against INEC ECE *Promedio del ingreso mensual en el empleo principal*, quarterly XLSX at `https://inec.cr/estadisticas-fuentes/encuestas/encuesta-continua-empleo`):
  - San José: ~$700–$1,200 (USD)
  - Escazú / Heredia: ~$900–$1,500
  - Coastal tourist zones: ~$500–$1,000
- **Salario Mínimo**: set per occupation by an annual MTSS decree — 2026 monthly *genérico* minimums ₡373,092 (unskilled) / ₡405,711 (semi-skilled) / ₡419,756 (skilled) / ₡487,335 (specialised), **Decreto 45303-MTSS**, +1.63%, in force 1 Jan 2026 (2026 data, figures per ECIJA + G-Talent summaries of the decree; cross-check: MTSS 2025 list ₡367,108.55 × 1.0163 = ₡373,092) — verify the exact occupation in the MTSS *Lista de Salarios Mínimos*

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **OVSICORI-UNA** (Volcanic Observatory) | `https://www.ovsicori.una.ac.cr/` | Volcanic monitoring |
| **RSN (Red Sismológica Nacional)** UCR/ICE | `https://rsn.ucr.ac.cr/` | Seismic |
| **CNE (Comisión Nacional de Prevención de Riesgos y Atención de Emergencias)** | `https://www.cne.go.cr/` | Hazard management |
| **IMN (Instituto Meteorológico Nacional)** | `https://www.imn.ac.cr/` | Weather, climate |
| **MINAE (Ambiente y Energía)** | `https://www.minae.go.cr/` | Environment |

### Specific risks

#### Earthquake — CRITICAL

- **Cocos plate subducts NE beneath the Caribbean plate at the Middle America Trench — convergence 8–9 cm/yr** (2012 data, source RSN *El Terremoto de Sámara del 5 de setiembre del 2012* — rates/figures may have changed since)
- **Seismic design code**: **Código Sísmico de Costa Rica 2010 (revisión 2014)** is the binding standard (Ley 6119; made official by Decreto 37070-MIVAH-MICIT-MOPT, La Gaceta 13 Jul 2012 — per Cimenta, secondary, checked against SINALEVI 12 Oct 2026). **CSCR 2025**: final text approved by the CFIA Asamblea de Representantes on 24 Nov 2025, editing under way (source CFIA Comisión Permanente del Código Sísmico, `https://www.codigosismico.or.cr/`); it binds only once its executive decree is published in La Gaceta — no decree as of 12 Oct 2026 (per Cimenta, secondary)
- **Recent significant events** (Mw per RSN *Sismos históricos* catalogue):
  - **Cinchona 2009 Mw 6.2** (42 deaths)
  - **Nicoya 2012 Mw 7.6** (Cocos-Caribbean subduction, Middle America Trench, Nicoya Peninsula; RSN also calls it the Sámara earthquake)
  - **Limón 1991 Mw 7.7** (Caribbean; 48 deaths in CR)
  - **Jacó 2017 Mw 6.5** (3 deaths, Pacífico Central damage); the catalogue lists eight more Mw 6.0–6.7 events from 2018 to 2025, most recently Tamarindo 2024 Mw 6.2 (felt strongly in Guanacaste) and Quepos 2025 Mw 6.1 (felt nationwide)

#### Volcanic

RSN lists five active volcanoes: Rincón de la Vieja, Arenal, Poás, Irazú and Turrialba (source RSN volcano pages + *Los principales volcanes activos de Costa Rica*, 2010).

- **Arenal** — eruptive phase from 29 Jul 1968; activity fell from Jul–Oct 2010 and the volcano has been in repose since Jan 2011 — main present hazards landslides or reactivation (RSN)
- **Poás** — major phreatomagmatic eruptions Apr 2017 destroyed the crater dome (RSN); renewed unrest from 1 Mar 2025, OVSICORI alert level 3 of 4 in Mar 2025 (DW/AFP, 24 Mar 2025, secondary); eruption recorded 4 Jul 2026, level 'Advertencia' (Diario Extra citing OVSICORI, secondary) — check OVSICORI's current alert level and park status
- **Turrialba** — new eruptive vent opened 5 Jan 2010, phreatic eruptions 2010–2017; earlier historic eruptions 1864–66 (RSN)
- **Rincón de la Vieja** — hot crater lake with frequent phreatic / phreatomagmatic eruptions (2011–2017 series) and hot lahars down the Pénjamo, Azul and Quebrada Azufrosa rivers (RSN)
- **Irazú** — fumarolic activity; last eruptive cycle 1962–65 (ash fall on the Valle Central, lahars that damaged western Cartago), 1994 phreatic explosion on the north flank (**Cartago province, 30 km NE of Cartago city per RSN**)

#### Flooding + landslide

- **Rainy season — Pacific slope: May–October, November transitional** (dry Dec–Mar, April transitional; wettest Sep–Oct) (source IMN *El clima y las regiones climáticas de Costa Rica*) — critical
- **Caribbean slope (Limón)**: no defined dry season; wettest Nov–Jan (peak December, cold-front driven), relatively drier Feb–Mar and Sep–Oct on the coast (same IMN source) — chronic flooding
- **Tropical cyclones**: Hurricane Otto (Nov 2016, first hurricane to hit CR territory directly, 17 deaths) and Tropical Storm Nate (Oct 2017, 16 deaths; costliest disaster of the previous 25 years at 1 % of 2017 GDP, CNE figure) (2021 data, source IMN *Cuarta Comunicación Nacional* — rates/figures may have changed since)

#### Climate

- Costa Rica is **tropical wet/dry**, with two rainfall regimes — Pacific and Caribbean slopes (IMN); projected change in *Climate change projections* below

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990** | Asbestos common; older systems; pre-1974 stock predates the first seismic code (CSCR-74), later stock built to CSCR-74 / CSCR-86 (CFIA code history) |
| **1990s–2000s** | CSCR-86, then CSCR-2002, which drew on the 1990–91 Cóbano, Piedras Negras and Limón earthquakes (CFIA code history) |
| **Post-2010** | CSCR-2010 (revisión 2014), binding since Decreto 37070 (2012); CSCR 2025 approved by CFIA 24 Nov 2025, pending its decree (see Earthquake above) |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Estudio de Registro** | Title study by lawyer/notary |
| **Plano catastrado** | Registered cadastre plan, must match Folio Real |
| **Certificación literal del Registro Nacional** | Title certificate |
| **No-debt certificates** | CCSS; electricity distributor (ICE / CNFL / ESPH / JASEC / rural co-op); water operator (AyA / ESPH / ASADA / municipal system); Municipalidad — ARESEP is the regulator, not a biller |
| **Notario** | Mandatory closing |

### Climate change projections

- **Temperature**: +1.5–1.8 °C (RCP2.6) to +3.8–4.8 °C (RCP8.5) for 2070–2099 vs 1961–1990; largest warming along Talamanca – Valle Central – Pacífico Norte (Tempisque basin) (2021 data, source IMN *Proyecciones de Cambio Climático regionalizadas para Costa Rica* — rates/figures may have changed since)
- **Rainfall (RCP8.5, 2070–2099 vs 1970–2000)**: drier centre/north Guanacaste (up to −20 %), Valle Central and its cordillera (up to −15 %) and Talamanca (up to −25 %); wetter Nicoya peninsula (up to +40 %), Pacífico Sur (up to +30 %), Pacífico Central and Zona Norte (up to +20 %) and the low Caribbean (up to +15 %); IMN notes this rainfall output is not bias-corrected (2021 data, same IMN source — rates/figures may have changed since)
- **Sea-level rise** (coastal property risk): SSP3-7.0 projection +0.24 m by 2050 and +0.75 m by 2100 at Puntarenas, +0.25 m / +0.76 m at Limón; a moderate El Niño adds 0.30 m and a strong one up to 0.60 m on top (2024 data, source IMN–AECID *Estudios y proyecciones de aumento en el nivel del mar y erosión costera para las dos costas de Costa Rica*, Dec 2024 — rates/figures may have changed since). Global mean rise by 2100 vs 1995–2014: 0.28–0.55 m (SSP1-1.9) to 0.63–1.01 m (SSP5-8.5) (2021 data, source IPCC AR6 WG1 SPM B.5.3) — rates/figures may have changed since
- **More variable rainfall**: larger year-to-year swings after 2060 in the Pacífico Norte; late-century Caribe Norte has the wettest years but also some dry ones (2021 data, IMN RCP8.5 run — rates/figures may have changed since)

---

## Section: `--mains`

### Sources

- **AyA (Acueductos y Alcantarillados)**: `https://www.aya.go.cr/` — largest operator, 47.2 % of the population served; municipal systems 13.9 %; ESPH and others 4.9 % (2016 data, source AyA presentation at the ARESEP congress, 5 Oct 2016 — rates/figures may have changed since)
- **ASADAS** — community associations that run AyA-owned rural water / sewer systems under delegation and bill ARESEP-approved tariffs (ARESEP glossary); ~1,600 ASADAS ("cerca de 1.600") serving 26.0 % of the population (2016 data, same AyA source — rates/figures may have changed since)
- **ESPH S.A.** (Empresa de Servicios Públicos de Heredia) — Heredia-area operator; a public-utility *sociedad anónima* whose shares belong to the Municipalidad de Heredia and the member municipalities, **not a private company**; supplies water, sanitary + storm sewer, electricity and street lighting (Ley 7789 of 1998, arts. 1 and 6, text via vLex)

### Verification

- Piped in-home water reaches 94.5 % of the population from official operators, 98.4 % counting unauthorised systems; wastewater is 73 % tanque séptico vs 24 % sewer nationally (2016 data, source AyA presentation at the ARESEP congress — rates/figures may have changed since) — expect a septic tank even in towns; rural pozos common
- **ARESEP**: `https://aresep.go.cr/` — regulator; its glossary lists AyA, ESPH and ASADAS as the water operators it regulates (municipal systems are not on that list)
- **Electricity**: 8 distributors authorised by law, by area — ICE (rural areas nationwide), CNFL (San José), ESPH (Heredia), JASEC (Cartago), Coopeguanacaste (Guanacaste), Coopelesca (San Carlos), Coopesantos (Zona de los Santos), Coopealfaro Ruiz (Alfaro Ruiz); service covers 99.5 % of the territory; ARESEP regulates generation, transmission, distribution and street lighting (source ARESEP *El servicio de electricidad*, page undated)

### Costs

| Scenario | Cost (USD, est.) |
|---|---:|
| Mains connection | est. ~$500–$2,000 hookup fee with the main at the boundary, pipe from meter to house extra; est. ~$5,000–$15,000 if the line must be extended |
| Pozo + bomba | hand-dug est. ~$470/m (10 m ≈ $4,700); drilled est. ~$160/m at 40–180 m, total est. ~$30,000 with permit, mobilization, pump test and concession, depending on depth; pump itself not priced |
| Tanque séptico | est. ~$3,000–$8,000 installed (standard biodigester system); est. ~$8,000–$15,000 with poor percolation or a high water table |

*Est. ranges from secondary sources, not a national tariff: connection and septic from the Build Tropical builder guide (2026 data, trade site, written for coastal lots); wells from a Langston Realty broker post (2023 data — rates/figures may have changed since). One operator's published charge sits below the guide's low end: ASADA Playa Potrero's meter connection fee of CRC 138,798 (2022 data, source ASADA requirements sheet — rates/figures may have changed since), ≈ $304 at CRC 456 per USD (computed: 138,798 ÷ 456 ≈ 304). AyA's own connection tariff could not be read for verification on 2026-11-04 — check it directly. Get the availability letter and connection charge from the AyA or ASADA office and a contractor quote before budgeting; the same guide says AyA has frozen new connections in some areas.*

---

## Cost benchmarks (CR 2026)

| Work | Cost (USD) |
|---|---:|
| Estudio de Registro (title study) | est. $300–$700 |
| Notary + escritura | ≈1.0–1.2% of price at CRC 100M–500M (computed from Decreto 41457-JP art. 74 marginal scale: 2% to CRC 11M, 1.5% to 16.5M, 1.25% to 33M, 1% above; minimum CRC 60,500) |
| Traspaso + timbres + registro | ≈2.33–2.35% (computed: 1.5% traspaso + 0.5% registro + 0.2% municipal + 0.125–0.15% agrario) + fixed lawyer / archive stamps |
| **Total transaction cost (seller + buyer, before lawyer / title study)** | **≈3.4–3.5%** of price at CRC 100M–500M (computed) |
| Roof renovation | est. $3,000–$10,000 |
| Anti-seismic retrofit | est. $15,000–$60,000 (depends on structure/size — verify with structural engineer quote) |
| Energy retrofit | est. $5,000–$25,000 |
| Solar PV (5kW) | est. $4,000–$8,000 |

*Works/professional-service rows above are est. ranges from contractor/notary quotes — verify per quote. Traspaso/timbres/notary % rows are anchored to the sourced `--tax` section.*

## Active fiscal incentives + visa programs (2025-2026)

### Residency programs

- **Pensionado**: lifetime pension from abroad ≥ **US$1,000/month** (Ley 8764 art. 81); the same amount covers spouse, children under 25 and adult children with disabilities (Reglamento de Extranjería art. 100) — no per-dependent add-on in those texts
- **Rentista**: stable income ≥ **US$2,500/month** for at least 24 months, certified by a bank (Ley 8764 art. 82; Reglamento de Extranjería art. 99(1) as amended by Decreto 43926-MGP-H-TUR, 2023). The commonly quoted **US$60k bank-deposit** route is uncertain: Decreto 43926 also added to Reglamento art. 2 that a bank deposit paid back in monthly instalments is not 'renta' — verify with DGME before relying on a deposit
- **Inversionista (Investor Visa)**: **US$150k** in real estate, registrable assets, shares, securities, productive / national-interest projects, venture-capital funds, sustainable tourism infrastructure or reforestation (Ley 9996 art. 8; Reglamento 43926 arts. 4, 7); forestry is also US$150k — the US$100k forestry rule (Reglamento de Extranjería art. 92) was repealed by Reglamento 43926 art. 31; real estate must be registered in the applicant's **personal name**, company-held title is not accepted (art. 7(A)(1)); 2-year permit, renewable on proof the investment was kept. ⚠️ Threshold contested after 14 Jul 2026 — see `--tax` › Future risk (2026-10-23 verified, source Ley 9996 text via vLex + Reglamento 43926 Gaceta text)
- **2-year temp residency (renewable) → permanent after 3 consecutive years (Ley 8764 art. 78) → naturalisation after 7 years' official residence, 5 for Central Americans, Spaniards and Ibero-Americans by birth (TSE — Ley 1155)**
- **Absence limit**: temporary residence is cancelled after more than 2 consecutive years outside CR, permanent residence after more than 4, barring proven health / study / family reasons (Ley 8764 art. 129(5)–(6)); an 'at least one entry per year' rule does not appear in the Ley 8764 or Reglamento texts read 2026-10-23 — verify with DGME

### Tax incentives

- **CGT exemption only for the vivienda habitual** (Ley 7092 art. 28 bis(7)); other gains 15%, or 2.25% of price on the first sale of pre-1 Jul 2019 assets (art. 31 ter)
- **Territorial income tax**: income earned abroad while CR tax resident is not taxable if not related to the country's economic structure (PwC Tax Summaries, reviewed 30 Jun 2026); Ley 9996 residents are not automatically tax resident (Ley 9996 art. 6)
- **Ley 9996 art. 5 incentives** (one-time duty-free household goods, up to 2 vehicles free of import duties and IVA, income-tax exemption on the declared qualifying income, 20% cut in the traspaso tax on property bought in the beneficiary's name) — **window CLOSED 14 Jul 2026** for new applicants; those granted keep them 10 years (art. 12)
- Bienes Inmuebles exemption for an individual's only property up to 45 salarios base (Ley 7509 art. 4(e))

## Common listing platforms

- **Encuentra24** — DOMINANT
- **MLS Costa Rica** — ❌ DEPRECATED — dead on 2026-10-23 (domain parked); verify with Registro Nacional (SIRI)
- **CRPropertyExpert** — ❌ DEPRECATED — dead on 2026-10-23 (domain does not resolve); verify with Registro Nacional (SIRI)
- **Properties in Costa Rica, Coldwell Banker CR**
- **Realty ONE Group CR** — publishes zone-level median asking prices (market report)
- High English-language coverage

## Caveats unique to CR

- **Strongest digital cadastre infra in LatAm** — Registro Nacional + SIRI + Ventanilla Digital online
- **Hold via corporación SA** common (estate planning + liability) — but **investor visa requires personal-name title** (Reglamento 43926 art. 7(A)(1): company-registered property is not accepted)
- **CGT 15% since 1 Jul 2019** (Ley 9635) — the old 'no CGT for individuals' rule is gone; only the *vivienda habitual* is exempt (Ley 7092 art. 28 bis(7)), and a non-domiciled seller faces a 2.5% withholding on the price (art. 28 ter)
- **Maritime Zone Law 6043** (CRITICAL):
  - **First 50m public** — no construction (Zona Pública)
  - **Next 150m restricted** (Zona Restringida) — municipal concession only, granted for 5–20 years (Ley 6043 art. 48)
  - **No concession to** foreigners with under 5 years' residence, or to companies with more than 50% foreign capital, bearer shares, foreign domicile or formed by foreigners; shares may not be passed to foreigners (Ley 6043 art. 47) — structures commonly keep a 51% qualifying holder as a safety margin (secondary — Papagayo Design Center guide)
  - **Annual canon** on the appraised land value, set by municipal regulation within caps — residential up to 3%, hotel / tourism / recreational up to 4%, commercial / industrial up to 5%, agricultural up to 2%, floor 0.25% (Reglamento Decreto 7841-P art. 49 as reformed by Decreto 37882, 2013 — secondary summary, Corporación GC); the pre-2013 fixed table (3% / 4% / 5% / 2%) applies until the municipality issues its rule. The canon replaces the land tax, but buildings still pay the 0.25% Bienes Inmuebles (Ley 6043 art. 48; Ley 7509 art. 6(c))
  - **Many advertised "beachfront" titles are CONCESSION, not titled** — critical diligence point
- **2 km inalienable border strip** (2,000 m) along the Nicaragua and Panama borders (Ley 2825 art. 7(f)) — state land, held only by concession / permit; occupants pay Bienes Inmuebles on buildings (Ley 7509 art. 6(c))
- **Utilities are not one monopoly**: electricity from 8 distributors authorised by law (ICE, CNFL, ESPH, JASEC + 4 rural co-ops), water from AyA, ESPH, an ASADA or the municipality; ARESEP regulates and sets tariffs, municipal water excepted (2026 data, source ARESEP electricity + water service pages) — the no-debt certificate comes from the actual provider
- **Pensionado USD 1,000/mo** = generous LatAm threshold
- **Investor visa US$150k (Ley 9996 art. 8)** — Ley 9996's art. 5 incentive window closed 14 Jul 2026; whether US$150k still applies to new filings is contested (see `--tax` › Future risk) — confirm with DGME
- **Earthquake risk CRITICAL** — Cocos subduction + Nicoya 2012 reference
- **5 active volcanoes** per RSN (Rincón de la Vieja, Arenal, Poás, Irazú, Turrialba) — activity per volcano in `--risks` (2019 data, source RSN weekly volcano bulletins + *Los principales volcanes activos de Costa Rica*, 2010 — figures may have changed since)
- **Tropical climate** — rainy May-Nov; landslide + flooding risk
- **Limón Caribbean** = different climate + higher flood
- **English-language market** — expat-driven, particularly Pacific coast
- **Pura vida** lifestyle marketing premium

## Reddit / forum sources

- **r/CostaRica** — biggest community
- **r/expats**, **r/expatsincosta**
- **r/MoveToCostaRica**
- **The Tico Times** (English)
- **A.M. Costa Rica**
- **Q Costa Rica**

## Verification authorities

| Authority | When to call |
|---|---|
| **Registro Nacional** | Title verification (online via SIRI) |
| **Catastro Nacional** | Cadastre verification |
| **Notario público** | Mandatory closing |
| **Municipalidad** | Property tax + permits |
| **CCSS / electricity distributor (ICE, CNFL, ESPH, JASEC, co-op) / water operator (AyA, ESPH, ASADA, municipality)** | No-debt certificates |
| **ARESEP** | Utility tariffs + service-quality complaints (water: AyA, ESPH, ASADAS; electricity: all 8 distributors) |
| **ICT** | If short-let |
| **DGME (Migración)** | Residency visa |
| **OVSICORI / RSN / CNE** | Hazard zone status |
| **MOPT Planificación Sectorial** | Traffic counts (TPDA) per station |

## Source URL templates

| Source | URL pattern |
|---|---|
| Registro Nacional | `https://www.rnpdigital.com/` |
| BCCR | `https://www.bccr.fi.cr/` |
| INEC | `https://www.inec.cr/` |
| Encuentra24 CR | `https://www.encuentra24.com/costa-rica` |
| MLS Costa Rica | ❌ DEPRECATED — dead on 2026-10-23 (domain parked); verify with Registro Nacional (SIRI) |
| OVSICORI volcanic | `https://www.ovsicori.una.ac.cr/` |
| RSN seismic | `https://rsn.ucr.ac.cr/` |
| CNE emergencies | `https://www.cne.go.cr/` |
| IMN weather | `https://www.imn.ac.cr/` |
| AyA water | `https://www.aya.go.cr/` |
| ARESEP utility regulator | `https://aresep.go.cr/` |
| MOPT TPDA traffic counts | `https://tpda.mopt.go.cr/transito/tpd.php` |
| Código Sísmico (CFIA commission) | `https://www.codigosismico.or.cr/` |
| ICT tourism | `https://www.ict.go.cr/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (Realty ONE Group CR zone asking medians + Encuentra24 + BCCR construction indicators), traffic (MOPT TPDA), tax (Bienes Inmuebles 0.25% + Traspaso 1.5% + registro 0.5% + IVA on construction services, not on the sale + 15% CGT with the vivienda habitual exemption + Solidario luxury), rental (Ley 7527 + mandatory ICT registration under Ley 9742 + 13% IVA on stays under one month), work (MTSS 2026 minimum wages + CCSS), risks (Cocos subduction + Nicoya 2012 + 5 active volcanoes per RSN), mains (AyA + ESPH + ASADAS + municipal systems).
**Confidence**: HIGH for the facts re-read against statute, decree or official sources on 2026-10-23: Registro Nacional / SIRI, the Correos postcode scheme and the BCCR exchange rate; the `--tax` rates (Ley 7509 0.25% + *bien único* exemption, Ley 6999 traspaso 1.5%, Ley 4564 registro 0.5%, IVA outside the sale under Ley 6826 art. 9, Impuesto Solidario 2026 threshold CRC 143M under Decreto 45358-H, CGT 15% / vivienda habitual / 2.25% first-sale option / 2.5% non-domiciled withholding under Ley 7092 + MH-DGT-RES-0051-2025); Ley 6043 (50 m public + 150 m restricted zone, 5–20-year concessions, foreign-ownership limits) and the 2 km border strip (Ley 2825 art. 7(f)); Pensionado US$1,000 and Rentista US$2,500 for 24 months (Ley 8764); 2026 minimum wages (Decreto 45303-MTSS); the climate projections (IMN 2021, IMN-AECID 2024, IPCC AR6); and the utility operators (ARESEP: 8 electricity distributors; AyA, ESPH, ASADAS or municipal water). MEDIUM for the investor-visa threshold after the Ley 9996 window closed on 14 Jul 2026 (contested, secondary readings only; confirm with DGME), the notary arancel brackets (2019 Decreto 41457-JP; biennial indexation not checked), the Folio Real format (partly checked), `--price` zone medians (Realty ONE Group CR asking prices: listing tier, not sold prices), `--rental` (non-resident withholding rate not confirmed), `--risks` (earthquake, volcano and rain-season facts re-sourced to RSN / IMN / CFIA; CNE and MINAE pages unreadable; current Poás alert level, asbestos line and mandatory-at-sale rows not re-verified), `--traffic` (MOPT 2023 TPDA counts; Ruta 1 and the band cut-offs unsourced) and `--mains` (AyA operator and coverage shares are 2016 data). LOW for the Rentista US$60k deposit route (no primary text found), the † price rows (San José central, Liberia / Guanacaste interior, Limón), the 2026 outlook est., the `--work` regional salary ranges (est.) and the contractor and mains cost rows (est., no primary source).
**Last verified**: 2026-05-27.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | Registro Nacional portal, SIRI (in production since 30 Apr 2015) and Ley 6043 confirmed; Correos postcode scheme, IGN 2022 territorial division, BCCR exchange rate and Constitución art. 76 updated; plano format from a listing-agency guide (secondary); Folio Real components only partly checked |
| `--tax` (except Future risk) | 2026-10-23 | 2026-10-23 refresh wave | Ley 7509, 6999, 4564, 6826 / 9635, 8683 and 7092 re-read on statute texts, plus Decreto 45358-H and MH-DGT-RES-0051-2025; seller + buyer total recomputed at ≈3.4–3.5%; notary arancel brackets from the 2019 decree (later indexation not checked); CFIA construction-services IVA date seen only in a search snippet; 'VERY LOW' comparative kept as curated wisdom |
| Climate + Climate change projections (in `--risks`) | 2026-10-23 | 2026-10-23 refresh wave | IMN 2021 regionalised projections, IMN-AECID Dec 2024 sea-level study and IPCC AR6 SPM B.5.3 |
| Active fiscal incentives — Tax incentives | 2026-10-23 | 2026-10-23 refresh wave | CGT exemption limited to the vivienda habitual; territorial rule (PwC Tax Summaries); Ley 9996 incentives marked CLOSED; Ley 7509 art. 4(e) *bien único* exemption |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Encuentra24, Properties in Costa Rica and Coldwell Banker CR live; MLS Costa Rica (parked domain) and CRPropertyExpert (no DNS) ❌ DEPRECATED; Realty ONE Group CR added |
| `--rental` | 2026-10-23 | 2026-11-04 maintenance run | Asking-rent medians come from the Realty ONE Group CR zone reports of 4 Nov 2026: Tamarindo rose to $2,200/mo, while Gran San José and Jacó held at $1,450 and $1,800. |
| `--work=<profession>` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--risks` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (CR 2026) | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |

Other sections were partly refreshed on 2026-10-23 but keep unverified items, so they default to the Status footer date: `--price`, `--traffic`, `--tax` › Future risk, `--rental`, `--work`, `--risks`, `--mains`, Cost benchmarks, Residency programs, Caveats unique to CR, Reddit / forum sources, Verification authorities, Source URL templates (see Update history).

## Extension TODOs

- [ ] Per-canton property tax rates
- [ ] SA holding structure for property + tax implications
- [ ] Maritime Zone concession verification flow (titulado vs concesión)
- [ ] 2 km border strip overlay (Ley 2825 art. 7(f); land privately held under legitimate title is excepted)
- [ ] Investor visa $150k personal-name compliance
- [ ] Pensionado/Rentista comparison decision tree
- [ ] Volcanic hazard overlay per canton (5 active volcanoes per RSN)
- [ ] Cocos subduction earthquake retrofit cost estimator
- [ ] AyA vs ASADAS rural water verification
- [ ] CCSS/ICE no-debt certificate flow

## Update history

- **2026-04-26** — Initial population
- **2026-05-27** — Tier-1 corrections (LATAM batch): Ley 7509 and Ley 6043 citations, Ley 9635 IVA + CGT framing (only the vivienda habitual is exempt), Impuesto Solidario 2026 schedule (Decreto 45358-H), investor visa US$150k re-dated to Ley 9996 (2021), Cocos subduction and Irazú lines (stamps in the body)
- **2026-05-29** — Anti-hallucination sweep: est. labels on the 2026 price outlook, the Atenas land row, the mains and the cost-benchmark rows; date stamps on the FX line and the price benchmarks
- **2026-10-23** — Refresh wave (market, tax-legal, risk-infra). Playbook-level stamp not advanced: `--price`, `--rental`, `--work`, `--risks` and `--mains` keep unverified items. Facts checked — changed / confirmed / unverifiable per section:
  - Re-verified: Country profile 11 — 6 / 4 / 1; `--tax` annual property tax 6 — 3 / 2 / 1, transaction taxes 7 — 6 / 1 / 0, IVA + Impuesto Solidario 13 — 6 / 7 / 0, capital gains 6 — 3 / 3 / 0, total transaction cost 3 — 2 / 0 / 1; Climate + Climate change projections 5 — 5 / 0 / 0; Tax incentives 3 — 3 / 0 / 0; Common listing platforms 5 — 3 / 3 / 0
  - Refreshed, not re-verified: `--price` 19 — 11 / 4 / 5; `--rental` 9 — 7 / 0 / 2; `--work` 12 — 4 / 5 / 4; `--tax` future risk 3 — 2 / 1 / 1; `--traffic` 8 — 4 / 2 / 2; `--risks` 29 — 16 / 5 / 8; `--mains` 8 — 5 / 1 / 3; Cost benchmarks 8 — 2 / 1 / 5; Residency programs 10 — 6 / 4 / 2; Caveats unique to CR 9 — 5 / 4 / 1 (legal / fiscal only); Reddit / forum sources 7 — 0 / 5 / 2; Verification authorities 8 — 1 / 2 / 5; Source URL templates 11 — 1 / 9 / 2, plus 3 rows added; no `--crime` or `--amenities` section exists
  - Main changes: price table rebuilt on Realty ONE Group CR zone asking medians, with the San José central, Liberia / Guanacaste interior and Limón rows marked † (not re-verified); MLS Costa Rica and CRPropertyExpert ❌ DEPRECATED; FX 1 USD ≈ 449–456 CRC (BCCR); IVA restated (the sale is outside IVA; 13% on construction services); four Impuesto Solidario bracket limits corrected; the 2.25% option limited to the first sale and the non-domiciled 2.5% withholding re-sourced to MH-DGT-RES-0051-2025; seller + buyer transaction cost recomputed at ≈3.4–3.5%; investor-visa threshold contested after the Ley 9996 window closed on 14 Jul 2026; the Pensionado per-dependent add-on, the US$100k forestry tier and the annual-entry rule removed (not in the statute texts); ZMT concession limits (more than 50% foreign capital, under 5 years' residence) and the 2 km border strip replace the 51% / 49% and 10 km lines; Ley 7527 3-year minimum lease term and mandatory ICT registration under Ley 9742; 2026 minimum wages (Decreto 45303-MTSS); RSN's five active volcanoes, CSCR code history and the IMN rain-season regimes; climate projections from IMN 2021 + IPCC AR6; no-debt certificates attributed to the actual utility (ARESEP is the regulator); Caveats, the Status coverage line and Extension TODOs aligned with the five-volcano, 2 km border-strip and utility-operator corrections
- **2026-11-04** — Maintenance run: closed `--rental`, `--work=<profession>`, `--risks`, Cost benchmarks (CR 2026); still open `--price`, `--tax`, `--mains`.
