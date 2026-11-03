# Mexico 🇲🇽 — Property Due-Diligence Playbook

ISO2: `mx`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (Código Postal)**: 5 digits (`06000` CDMX Centro, `64000` Monterrey, `44100` Guadalajara, `77780` Tulum, `37700` San Miguel de Allende)
- **Admin levels**: 32 federal entities (31 states + Mexico City) + 2,478 municipios and CDMX demarcaciones territoriales (alcaldías) (2025 data, source [INEGI CNGMD 2025 results, 19 Mar 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/cngmd/CNGMD_RR_25.pdf))
- **Currency**: **MXN** (Mexican peso); 1 USD = 18.7962 MXN (Banxico FIX as published in the DOF; DOF indicators dated 3 Nov 2026 — 2026 data, source [DOF indicadores](https://dof.gob.mx/indicadores.php)); 1 EUR ≈ 20.75–20.79 MXN (market quotes 27 Oct 2026, secondary — Diario del Yaqui; verify at Banxico SIE). Both move daily
- **Languages**: Spanish (de facto); 68 indigenous agrupaciones lingüísticas with 364 variantes, all recognised as lenguas indígenas nacionales (Náhuatl, Maya/Yucateco, Zapoteco) (2008 data — INALI Catálogo de las Lenguas Indígenas Nacionales, as cited in [INALI, 31 Mar 2015](https://www.inali.gob.mx/detalle/las-364-variantes-de-las-lenguas-indigenas-nacionales-con-algun-riesgo-de-desaparecer-inali); 68 agrupaciones and the Lenguas Indígenas Nacionales status still shown on the [INALI Atlas](https://atlas.inali.gob.mx/inicio), 2026-11-03 verified) — rates/figures may have changed since
- **Cadastre — fragmented per state (no national portal)**:
  - **RPP (Registro Público de la Propiedad)**: state-level (32 separate registries)
  - **Catastro**: municipal-level, separate from RPP, holds cadastral value
  - **Federal harmonisation law in force 24 Oct 2026**: the Ley General para el Fortalecimiento y Armonización Catastral y Registral (DOF 23 Oct 2026) leaves registries with the states and cadastres with the state or municipal authorities, but requires a **Clave Única Catastral** per property, a **Cédula Única Catastral y Registral** linking it to the folio real, and ATDT-run national platforms that those authorities must adopt by 31 Dec 2026 to operate from 1 Jan 2027 on an ATDT calendar; it sets no predial rates. Until then use folio real + cuenta catastral as below (2026-10-28 verified, source: [DOF 23 Oct 2026 via SIDOF](https://sidof.segob.gob.mx/notas/5802078); tracked in `shared/regulatory-watch.md`)
  - **RAN (Registro Agrario Nacional)** for ejido land: `https://www.gob.mx/ran`
- **Identifier**: **folio real** (per state) + **cuenta catastral** (municipal)
- **Ownership types**:
  - **Propiedad privada** (private freehold)
  - **Ejido** (collective; ejidos + comunidades agrarias (propiedad social) cover ~51% of MX territory — 99.6 M of 196.4 M ha, of which 82.6% is ejidal, so ejido land alone ≈ 42% of the territory (computed) (2023 data, source RAN via the Atlas de la propiedad social de la tierra en México 2024, `https://deas.inah.gob.mx/pdf/biblioteca/repositorio/repositorio(39757)-4724.pdf` — rates/figures may have changed since); cannot be sold to foreigners; "regularización" path to private title via ejido assembly + RAN release)
  - **Fideicomiso** (bank trust mandatory for foreigners in Restricted Zone)
- **CRITICAL: Foreign-buyer Restricted Zone**: 50 km along the beaches / 100 km along the borders — fideicomiso required (LIE art. 2 fr. VI, defining the zona restringida of Constitución art. 27 fr. I; LIE última reforma DOF 27-05-2024 — source [Cámara de Diputados LIE PDF](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIE.pdf))

## Section: `--price`

### Primary sources

- **SHF (Sociedad Hipotecaria Federal) HPI**: `https://www.gob.mx/shf` — quarterly, appraisals of homes bought with a mortgage only; latest release seen: Q2 2026 (boletín 05/2026, 10 Aug 2026)
- **INEGI Vivienda**: `https://www.inegi.org.mx/temas/viviendasat/` — census + cadastral
- **Banxico** financial system reports
- **Lamudi MX quarterly market reports** (free PDFs)

### Listing platforms

- **Inmuebles24** — owned by QuintoAndar since its Dec 2021 purchase of Navent's real-estate portals (QuintoAndar release, [PR Newswire 27 Dec 2021](https://www.prnewswire.com/news-releases/quintoandar-adquiere-navent-para-reforzar-su-oferta-inmobiliaria-en-latinoamerica-843076872.html)), not OLX; market-share ranking data not publicly available — Propiedades.com also bills itself as "el portal inmobiliario más grande de México" (its homepage, 2026): `https://www.inmuebles24.com`
- **Vivanuncios**: `https://www.vivanuncios.com.mx` (eBay heritage)
- **Lamudi MX**: `https://www.lamudi.com.mx`
- **Propiedades.com**: `https://www.propiedades.com`
- **Point2Homes** for English-speaking foreign buyers (Baja, Quintana Roo)
- **Mexlist** ❌ DEPRECATED — mexlist.com is a Mexican-railways discussion community (online since 1998), not a property portal (checked 2026-11-03); verify English-language listings with AMPI-member brokers
- **MLS systems** regional (AMPI national, CCIQR Quintana Roo) — patchy coverage

### 2025-2026 price benchmarks (Lamudi Q4 2025 asking ranges + SHF Q2 2026 YoY)

| Region | MXN/m² (Lamudi Q4 2025 asking, not re-verified) | USD at FIX 18.7962 (computed) | Índice SHF YoY, Q2 2026 |
|---|---:|---:|---:|
| **CDMX (Polanco/Roma/Condesa)** | 60,000–110,000 | $3,190–$5,850 | ZM Valle de México +4.21%; CDMX entidad +3.40% |
| **CDMX (suburbs)** | 30,000–50,000 | $1,600–$2,660 | ZM Valle de México +4.21%; Estado de México +5.50% |
| **Monterrey** | 60,000–90,000 (premium) | $3,190–$4,790 | ZM +7.55%; municipio +6.41% |
| **Guadalajara** | 35,000–55,000 | $1,860–$2,930 | ZM +9.99%; municipio +9.64% |
| **Puebla** | 25,000–40,000 | $1,330–$2,130 | municipio +8.06% |
| **Tulum / Playa del Carmen** | 50,000–90,000 | $2,660–$4,790 | Solidaridad (Playa) +9.96%; Quintana Roo +9.80%; Tulum not published |
| **Los Cabos** | 60,000–150,000+ | $3,190–$7,980+ | municipio +8.48% |
| **San Miguel de Allende** | 40,000–80,000 | $2,130–$4,260 | Guanajuato +8.06%; SMA not published |
| **Mérida** | 25,000–40,000 | $1,330–$2,130 | municipio +8.49% |

YoY = Índice SHF (appraisals of mortgage-financed homes), Q2 2026 vs Q2 2025, for the zona metropolitana (ZM), municipio or state named — not the neighbourhoods in column 1 and not asking prices; national +7.31%; state and municipal values read from the IIEG charts (2026 data, sources [IIEG ficha informativa 13 Aug 2026, SHF data](https://iieg.gob.mx/ns/wp-content/uploads/2026/08/reporte_indice_precios_vivienda_mexico_2doT_2026.pdf); [SHF boletín 05/2026, 10 Aug 2026](https://www.gob.mx/shf/articulos/indice-shf-de-precios-de-la-vivienda-en-mexico-segundo-trimestre-de-2026)). The earlier listing-based YoY figures (+14-15% Tulum / Los Cabos, +9-12% Monterrey, +7-9% Guadalajara) are (superseded). SHF Q2 2026 median appraisal: CDMX MXN 3,301,516; national MXN 1,299,580. Listing cross-check: propiedades.com data put the CDMX-wide average above MXN 57,000/m² (listing platform via Inmobiliare 12 Aug 2026, secondary).

### Compute

1. MXN/m² = price / **superficie construida** (built area)
2. Cross-check **SHF HPI** + **Lamudi quarterly** + **Inmuebles24** asking prices
3. **Cadastral value typically 30-60% below market** (intentionally) — affects predial calc, NOT market value
4. **USD-denominated listings** common in Restricted Zone (Tulum, Cabo, Vallarta)

### Key terms

- Folio real = state RPP title identifier
- Cuenta catastral = municipal cadastre identifier
- Predial = annual property tax
- Fideicomiso = bank trust (foreign in Restricted Zone)
- Ejido = collective rural land
- Notario público = mandatory closing notary

---

## Section: `--traffic`

### Sources

- **SICT (Secretaría de Infraestructura, Comunicaciones y Transportes**, formerly SCT) — federal highways; its annual **Datos Viales** gives TDPA and vehicle mix per count station (editions to 2026 listed; Datos Viales 2025 reports 2024 TDPA) (2026 data, source SICT DG Servicios Técnicos — `https://micrs.sct.gob.mx/infraestructura/direccion-general-de-servicios-tecnicos/datos-viales`)
- **CAPUFE** for toll roads
- City open-data: CDMX (`https://datos.cdmx.gob.mx/`), Monterrey, Guadalajara

### Key term

**TDPA (Tránsito Diario Promedio Anual)** = AADT-equivalent (the term SICT uses in Datos Viales).

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, libramiento)
- 🔴 > 35,000 v/d (Periférico, Anillo Vial, autopistas)

---

## Section: `--tax`

### Annual property tax — Predial

**Municipal — varies massively per state/municipio.**

- Rate: set by each municipio in its Ley de Ingresos / Ley de Hacienda — **0.05–0.3%** of cadastral value (residential), commercial up to 1.2% (est., 2026-04 research range; verify the municipio's tariff). **CDMX** (2026 bimonthly tariff, Código Fiscal CDMX art. 130: fixed fee plus a marginal 0.0208% to 0.30909% per bimester across rangos A–P), habitational property after the 2026 subsidy: a flat MXN 408–666 a year up to MXN 1,410,569.80 cadastral value (rangos A–D; ≈0.05% at the top of rango D), then **above that range** — ≈0.35% of cadastral value a year at MXN 1.5M, ≈0.49% at 2M, ≈0.85% at 3M, ≈0.97% at 5M and ≈1.25% at 10M (2026 data, source: Código Fiscal CDMX art. 130 tariff in the Jefatura de Gobierno 2026 initiative, enacted by the decree in Gaceta Oficial CDMX 19 Dec 2025 — the values equal the 2025 tariff uprated 3.91% per Ley de Ingresos CDMX 2026 art. 8; subsidy Acuerdo, Gaceta Oficial CDMX 16 Jan 2026)
- **Cadastral value typically 30-60% below market** (est., 2026-04 research; no national primary source) — under policy pressure: the federal Ley General para el Fortalecimiento y Armonización Catastral y Registral (DOF 23 Oct 2026) sets no predial rates, but its initiative states that collection will rise by updating cadastral values to reflect real land and construction values and by registering omitted parcels (Expansión 9 Sep 2026, secondary). In CDMX a purchase or new construction moves the predial base to the avalúo market value (Código Fiscal CDMX art. 127 para. 4); for 2026 the subsidy Acuerdo covers the difference back to the cadastral-value tax (Gaceta Oficial CDMX 16 Jan 2026)
- CDMX residential bill 2026 (computed from the art. 130 tariff after the subsidy Acuerdo, before any early-payment discount): flat **MXN 68 / 77 / 94 / 111 per bimester** in rangos A–D (cadastral value up to MXN 1,410,569.80, so MXN 408–666/yr); rangos E / F / G (up to MXN 2,821,139.60) get a 50% / 35% / 25% subsidy — ≈**MXN 5,300/yr at MXN 1.5M**, ≈9,800 at 2M, ≈15,200 at 2.5M; full tariff from rango H — ≈**MXN 25,500/yr at 3M** (≈USD 1,350 at FIX 18.7962, DOF 3 Nov 2026), ≈48,300 at 5M, ≈124,800 at 10M (2026 data, source: Acuerdo de subsidios al Impuesto Predial, Gaceta Oficial CDMX 16 Jan 2026 + Código Fiscal CDMX art. 130)
- Early-payment discount set by each municipio, 2026 examples: **CDMX 8% (full year paid in January) / 5% (February)**, and a flat MXN 68 per bimester for seniors and vulnerable groups on homes valued up to MXN 2,808,466 (2026 data, source: Secretaría de Administración y Finanzas CDMX, 1 Jan 2026); Naucalpan 8% in January plus 8% more for owners who paid on time in the previous two years (2026 data, source: Ayuntamiento de Naucalpan, 21 Dec 2025); Benito Juárez / Cancún 15% (7–21 Jan) and Guadalajara 10% (to 28 Feb) (2026 data, secondary — UnoTV, N+)
- **CDMX progressive rates** for high-value properties — 16 rangos, the top one (P) above MXN 35,629,332.12 cadastral value at MXN 87,939.33 per bimester plus 0.30909% of the excess (2026 data, source: Código Fiscal CDMX art. 130)

### Transaction taxes — ISAI / ISABI

**Per state or per municipio — varies massively** (Impuesto Sobre Adquisición de Inmuebles; set by each municipio in Quintana Roo, Jalisco, Baja California Sur and Baja California):

| State | ISAI/ISABI rate |
|---|---:|
| CDMX | progressive, 11 rangos, base = highest of price, cadastral value and avalúo (Código Fiscal CDMX arts. 113, 116): effective ≈4.35% at MXN 1M, ≈4.91% at 2M, ≈5.18% at 3M, ≈5.58% at 5M, ≈5.99% at 10M, ≈6.42% at MXN 55.06M; marginal **9.018%** above MXN 55,059,877.22 (8.679% in 2025) (computed, 2026 data, source: art. 113 tariff in the Jefatura de Gobierno 2026 initiative, enacted Gaceta Oficial CDMX 19 Dec 2025 — same values in Mudafy and Miranda Abogado, secondary) |
| Quintana Roo | set per municipio: **Playa del Carmen 4%** (from 10 Dec 2025), **Tulum 4%** (from POE 9 Dec 2024), **Benito Juárez / Cancún 3%**; Isla Mujeres 4%, Cozumel and Puerto Morelos 3%, Bacalar 2% (secondary) (2026 data, sources: Congreso Q.Roo consolidated Leyes de Hacienda — Playa del Carmen art. 23 Quinquies, Tulum art. 50, Benito Juárez art. 27, all to POE 10 Dec 2025; Reference Real Estate 24 Aug 2026 for the other municipios) |
| Jalisco | Impuesto sobre Transmisiones Patrimoniales, set in each municipio's Ley de Ingresos: **Guadalajara marginal 2.5% → 3.5%** (top above MXN 42,976,151.22; computed effective ≈2.59% at MXN 1M, ≈2.85% at 3M, ≈3.15% at 10M), **Puerto Vallarta marginal 2.65% → 3.55%** (2026 data, sources: Leyes de Ingresos 2026 of Guadalajara art. 28 and Puerto Vallarta art. 41) |
| Baja California Sur | 3% — Los Cabos on the value less 5× the annual UMA (≈MXN 214,100 at the 2026 UMA), 1.5% for family donations / successions; Los Cabos went 2% → 3% from 1 Jan 2025 and the other four municipios aligned at 3% from 1 Jan 2026 (Decree 3263, BOGE 24 Dec 2025) (2026 data, sources: Ley de Hacienda del Municipio de Los Cabos art. 35, última reforma BOGE 27 Dec 2024; Snell & Wilmer 20 Jan 2026, secondary) |
| Tijuana | marginal **1.5% → 4.677%** across 10 UMA-indexed rangos (top above 63,637.99 UMA ≈ MXN 7.47M at the 2026 UMA of MXN 117.31; computed effective ≈1.8% at MXN 1M, ≈2.3% at 3M, ≈4.0% at 10M) (2026 data, sources: Ley de Ingresos del Municipio de Tijuana 2026 art. 8, Periódico Oficial BC 30 Dec 2025; INEGI UMA, DOF 9 Jan 2026) |

### Other taxes

- **ISR (Impuesto Sobre la Renta) capital gains**: up to **35%** marginal — the top bracket of the art. 152 annual tariff, above MXN 5,107,703.93 of taxable income (2026 data, source: SAT Anexo 8 RMF 2026, DOF 28 Dec 2025)
- **Principal residence exemption (Mexican tax residents only)**: up to **700,000 UDIs** of sale price (≈MXN 6.22M ≈ USD 331k — computed: 700,000 × UDI 8.881762 ÷ FIX 18.7962, both DOF 3 Nov 2026; UDI ≠ MXN, it is an inflation-indexed unit), sale formalised before a notary; requires voter-ID, utility-bill or bank-statement proof that it is the seller's home (RLISR art. 155) and an RFC (per Connell & Associates, 2026-05-27); land ≤ 3× construction area (RLISR art. 154); usable once per 3 years (LISR art. 93 XIX a). Double exemption with co-titled resident spouse (per Connell & Associates, 2026-05-27). **Non-residents do NOT qualify** — 25% on the gross price with no deductions (withheld by the buyer if Mexican-resident or with a Mexican permanent establishment, otherwise paid by the seller within 15 days), OR by election the art. 152 top rate (35%) on the net gain when the sale is in a public deed, which waives the Mexican-representative requirement; the election is closed to sellers resident in a preferential-tax or territorial-tax jurisdiction (2026 data, source: LISR arts. 93 XIX and 160, Cámara de Diputados consolidated text, última reforma DOF 01-04-2024; RLISR arts. 154–155)
- **IVA**: 16% (LIVA art. 1) on the construction share of non-residential property; land and residential construction are exempt (LIVA art. 9 fr. I–II; hotels excluded) (2026 data, source: Cámara de Diputados LIVA consolidated text)
- **Notario público**: **0.75–2.5%** (varies by state; 2026 — see Cost benchmarks table)
- **Registration**: 0.5–1% (2026 — see Cost benchmarks table)
- **Avalúo (appraisal)**: ~MXN 5,000–15,000 (2026 — see Cost benchmarks table)

### Foreign-buyer fideicomiso (CRITICAL)

**Restricted Zone**: 50 km coast / 100 km border. **Statute chain**: Constitución Art. 27 fr. I (no direct foreign ownership "en una faja de cien kilómetros a lo largo de las fronteras y de cincuenta en las playas") → **Ley de Inversión Extranjera 1993 Arts. 10–14** (art. 11 SRE permit for the bank acting as trustee; art. 13 term up to 50 years, renewable at the beneficiary's request) → Reglamento LIE (2026 data — LIE consolidated text, última reforma DOF 27-05-2024; source: [Cámara de Diputados — Ley de Inversión Extranjera official PDF](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIE.pdf) + Cámara de Diputados CPEUM).

- **Fideicomiso required** for foreigners — bank trust 50-year renewable
- **Setup cost**: ~USD 2,000–3,000 (est. — per-bank fee comparison pending, see Extension TODOs)
- **Annual maintenance**: ~USD 350–1,000 (est. — per-bank fee comparison pending, see Extension TODOs)
- **SRE (Secretaría de Relaciones Exteriores)** permit required
- **Outside Restricted Zone**: foreigners can take direct title after filing an SRE escrito accepting Constitución art. 27 fr. I (the Calvo clause — treated as nationals for that property) and obtaining the SRE permit; in a municipio lying wholly outside the zone the permit is deemed granted unless SRE publishes a refusal in the DOF within the statutory period (LIE art. 10-A)
- **Non-residential use inside the zone**: a Mexican company without a foreigner-exclusion clause can hold direct title for non-residential activities, notifying SRE within 60 business days of the purchase; residential property inside the zone still goes through a fideicomiso (LIE art. 10 fr. I–II)

### Total transaction cost (buyer side)

- Outside Restricted Zone: **5–8%** of price
- Inside Restricted Zone (with fideicomiso): **7–12%** of price
- **ISAI is usually the biggest single line item** (computed 2026: CDMX ≈4.4–6.4% effective, Quintana Roo resort municipios 3–4%, Guadalajara ≈2.6–3.2%); the notario público collects ISAI, registration and its own fee at closing, so the notary's closing bill commonly totals 4–7% of price (est.)

### Future risk

- Sheinbaum administration housing initiatives (affordable housing focus)
- Increased predial collection in CDMX, Monterrey — and nationally: the Ley General para el Fortalecimiento y Armonización Catastral y Registral (DOF 23 Oct 2026) keeps predial municipal and changes no rates, but its initiative targets higher collection through updated cadastral values and registration of omitted parcels (Expansión 9 Sep 2026, secondary; see Country profile; tracked in `shared/regulatory-watch.md`)
- Restricted Zone rules unchanged: the LIE foreign-acquisition and fideicomiso articles (arts. 10, 10-A, 13) carry no amendment after DOF 24-12-1996 in the consolidated text (última reforma DOF 27-05-2024) (2026 data, source: Cámara de Diputados); no fideicomiso reform proposal advancing in 2026 (2026-04 research)

---

## Section: `--rental`

### Long-term residential

- Per-state Civil Code governs lease
- Tenant protections **moderate** (less strict than EU)
- **CDMX lease term**: one year minimum, binding on both parties (un año forzoso), extendable at the tenant's option for up to one more year if current on rent, salvo convenio en contrario (unless the parties agree otherwise) (Código Civil CDMX art. 2448-C; art. 2398 also bars casa-habitación leases shorter than one year — current text as quoted in the 14 Oct 2026 Gaceta Parlamentaria initiative below); other states set their own terms
- **Aval** (guarantor) common requirement
- **CDMX rent cap (in force)**: annual rent increases on casa-habitación may not exceed the prior year's inflation (Código Civil art. 2448-D, 2nd paragraph; the earlier cap was 10%) and landlords must register each lease in the government's Registro Digital within 30 days (art. 2448-F), per the decree in Gaceta Oficial CDMX of 28 Aug 2024; the SCJN denied an amparo against both provisions (Amparo en revisión 546/2025, Feb 2026) (2026 data, sources [SCJN AR 546/2025](https://www2.scjn.gob.mx/Juridica/Engroses/Cerrados/Publico/Proyecto/2026/02/AR546_2025.pdf); [Congreso CDMX, 22 Aug 2024](https://www.congresocdmx.gob.mx/comsoc-congreso-capitalino-modifica-legislacion-materia-renta-vivienda-5429-1.html); 10% prior cap per Villanueva Ortiz client alert, secondary)
- **CDMX pending (NOT law)**: Jefa de Gobierno initiative to reform the Civil Code and issue a Ley de Relaciones Inquilinarias y Rentas Justas, Razonables y Asequibles, published in Gaceta Parlamentaria No. 623 of 14 Oct 2026 and open to citizen proposals for at least 10 business days (parlamento abierto) (2026 data, sources [Congreso CDMX initiative text](https://www.congresocdmx.gob.mx/archivo-05658feef941be2b6b70662aaf2708e092e62e1e.pdf); El Informador 22 Oct 2026, secondary)

### Short-let (Airbnb)

#### CDMX (Mexico City)

- **Mexico City Airbnb Law Oct 2024**: mandatory **Host Registry** (Padrón de Anfitriones) + **Technology Platform Registry** (Padrón de Plataformas) under amended Tourism Law (April 2024) — **registries went live 21-22 May 2026** (accelerated ahead of the FIFA World Cup; Jefatura de Gobierno announced Reglamento additions for a Gaceta Oficial CDMX aviso of 22 May 2026 — publication not confirmed, verify at Gaceta Oficial CDMX); registration opened 21 May 2026 with a 30-day window, but on 19 Aug 2026 Gobierno CDMX **extended the host-registration deadline to December 2026** for hosts already operating (registration stays permanently open for new hosts, per the Gobierno CDMX communiqué reproduced 21 Aug 2026) (secondary — La Jornada 19 Aug 2026 + Gobierno CDMX social post; exact cutoff not confirmed from a primary page — verify at `https://estanciaeventual.cdmx.gob.mx`) (registry launch 2026-07-02 verified, sources: Jefatura de Gobierno CDMX 22 May 2026 + Ibarra, Del Paso y Gallego + Expansión Política)
- **50 % annual occupancy cap** (Art 61 Sexies — max 50 % of the year's nights) added as the 4th paragraph of Art 61 Sexies by the decree published in Gaceta Oficial CDMX on 3 Oct 2024 (NOT the April 2024 amendment, NOT the 25 Sep 2024 Reglamento), which also barred social / popular housing (art. 36 Bis Ley de Vivienda) and post-2017-quake reconstructed homes (art. 22 Ley para la Reconstrucción Integral) from STR; sanction if exceeded = non-renewal of registration + 1-year re-registration bar — **cap enforcement legally in flux pending amparo litigation**: Airbnb filed an amparo (Jan 2025) and individual hosts have too, with **suspensión definitiva granted in some cases** so the cap is not applied to those litigants pending trial; a Tribunal Colegiado has ordered a merits/constitutionality ruling (2026-07-02 verified, sources: El País 9 Jul 2025; Airbnb Newsroom Jan 2025; SMPS Legal); on 27 Nov 2025 the Pleno Regional en Materias Administrativa y Civil de la Región Centro-Norte settled contradicción de criterios 122/2025 with **jurisprudencia PR.A.C.CN. J/20 A (12a.): suspensión definitiva is improcedente against the effects of art 61 Sexies 4th paragraph** (binding under the Ley de Amparo; SJF 13 Feb 2026, [registro digital 2031768](https://sjf2.scjn.gob.mx/detalle/tesis/2031768); full text via Academia de Amparo, secondary); **merits now at the SCJN**: on 28 Oct 2026 the Pleno unanimously approved reasunción de competencia 173/2026 to decide recurso de revisión 182/2026 of the Primer Tribunal Colegiado en Materia Administrativa Especializado en Competencia Económica, Radiodifusión y Telecomunicaciones, on whether the Ley de Turismo CDMX and its Reglamento (50 % cap, rules on the number of properties per host) breach freedom of commerce, free competition, the right to housing and reserva de ley — not yet decided (listing: [SCJN lista oficial, 28 Oct 2026 session](https://www.scjn.gob.mx/sites/default/files/listas/documento/2026-10-27/28%20de%20octubre%20de%202026%20lista%20oficial%202.pdf); vote: Luces del Siglo + Grupo Animal 28 Oct 2026, secondary)
- Sheinbaum (former mayor, now president) reversed her earlier UNESCO/Airbnb partnership

#### Quintana Roo (Tulum, Cancún, Playa del Carmen)

- **RETUR-Q**: Registro Estatal de Turismo mandatory for prestadores de servicios turísticos, explicitly including those operating through plataformas digitales (Ley de Turismo reform, POE 5 Mar 2024); register within 60 natural days, omission fine 50–965 UMA (art. 52 Nonies) (2024 data, source Monlex Abogados commentary via [Hosteltur, 10 Apr 2024](https://www.hosteltur.com/comunidad/005695_novedades-en-la-ley-de-turismo-del-estado-de-quintana-roo.html), secondary — rates/figures may have changed since; verify the current text at Congreso Q-Roo)
- **6% Lodging Tax (ISH)** on private departments / houses / villas let by an Anfitrión or platform (Ley del Impuesto al Hospedaje art. 8 para 2, in force 1 Apr 2023); 5% general rate for other lodging (art. 8 para 1) — (2025 data, source Congreso Q-Roo ISH consolidation POE 16-12-2025)
- Every Anfitrión must register with the Registro Estatal de Contribuyentes and obtain a Constancia de Obligaciones Fiscales Estatales for each property; platforms register as retenedores and name a legal representative and a Q-Roo address before the SATQ (ISH art. 7, reformed POE 16-12-2025) (2025 data, source Congreso Q-Roo ISH consolidation POE 16-12-2025). A legal-residency + RFC requirement for foreign hosts is not in the ISH text — data not publicly available, verify with SATQ / SAT
- Reported municipal power to ban platforms locally: not found in the state ISH text or in the 2024 Ley de Turismo reform commentary — data not publicly available, verify with the municipio (Tulum, Solidaridad, Benito Juárez)

#### Jalisco / Puerto Vallarta

- State-level less strict
- **HOA bans rising** in resort condos

### Tax on rental

- Residents: marginal income tax up to 35% (top bracket from MXN 5,107,703.93 taxable income a year); rent is taxed net of actual expenses or of an optional 35% standard deduction plus real estate taxes (2026 data, source PwC Tax Summaries — Mexico, [rates](https://taxsummaries.pwc.com/mexico/individual/taxes-on-personal-income) and [income determination](https://taxsummaries.pwc.com/mexico/individual/income-determination), reviewed 6 Aug 2026)
- **Non-resident owners**: **25% on gross rent, no deductions** (LISR art. 158 — source [LISR, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf))
- IVA 16% on furnished lets and hospedaje: the LIVA art. 20 fr. II exemption covers unfurnished casa-habitación only (source [LIVA, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf))

---

## Section: `--work=<profession>`

### Sources

- **OCC Mundial** — biggest job board: `https://www.occ.com.mx/`
- **LinkedIn MX**, **Computrabajo**, **Indeed.com.mx**, **Bumeran**
- **STPS (Secretaría del Trabajo)**: `https://www.gob.mx/stps`

### Self-employment

- **Persona física con actividad empresarial**: SAT registration
- **RFC (Registro Federal de Contribuyentes)** mandatory
- **Régimen Simplificado de Confianza (RESICO)** preferential rates for individuals with annual income up to MXN 3.5 M (LISR art. 113-E — source [LISR, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf))
- **IVA**: 16% standard (LIVA art. 1 — source [LIVA, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf))

### Salary benchmarks (2025-2026)

- **Formal-employment benchmark**: IMSS average salario base de cotización MXN 666.0/day nationally at end-Sep 2026 (+MXN 42.9 YoY), ≈ MXN 20,260/month (computed ×365/12); CDMX MXN 805.13/day, ≈ MXN 24,490/month (computed), the highest of any state — an average across IMSS-registered posts, not a median (2026 data, sources [IMSS boletín 539/2026, 8 Oct 2026](https://www.imss.gob.mx/prensa/archivo/202610/539); [CDMX labour ministry, IMSS data](https://deet.trabajo.cdmx.gob.mx/panorama-laboral/empleo-registrado-en-el-instituto-mexicano-del-seguro-social-imss))
- Median monthly gross (est., 2025; source not recorded — rates/figures may have changed since):
  - CDMX: ~MXN 18,000–35,000 (€900–€1,750)
  - Monterrey: ~MXN 20,000–40,000 (nearshoring premium)
  - Guadalajara: ~MXN 18,000–30,000
- **Salario mínimo (2026)**: **MXN 315.04/day general; MXN 440.87/day Zona Libre de la Frontera Norte (ZLFN)** (CONASAMI Consejo de Representantes decision of 3 Dec 2025, resolution published DOF 9 Dec 2025; +13% general = MXN 17.01 MIR plus 6.5% fijación; +5% ZLFN, no MIR; effective 2026-01-01; Banxico SIE cuadro CL289 still shows both for Aug 2026). The ZLFN is **45 border municipios, not whole states** (computed from the DOF list): 7 in Baja California, 11 in Sonora, 8 in Chihuahua, 8 in Coahuila, 1 in Nuevo León (Anáhuac — Monterrey is in the general zone) and 10 in Tamaulipas (2026 data, sources [DOF 9 Dec 2025](https://dof.gob.mx/nota_detalle.php?codigo=5775534&fecha=09%2F12%2F2025); [CONASAMI, 3 Dec 2025](https://www.gob.mx/conasami/articulos/incremento-a-los-salarios-minimos-para-2026))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SSN (Servicio Sismológico Nacional)** | `https://www.ssn.unam.mx/` | Real-time seismicity |
| **CENAPRED** | `https://www.gob.mx/cenapred` + Atlas Nacional de Riesgos `http://www.atlasnacionalderiesgos.gob.mx/` | National risk atlas; Popocatépetl monitoring + Semáforo de Alerta Volcánica |
| **CONAGUA** | `https://www.gob.mx/conagua` | Flood, drought, hurricane |
| **Protección Civil federal** | `https://www.gob.mx/sspc/acciones-y-programas/coordinacion-nacional-de-proteccion-civil-357857` | Emergency response |
| **CFE seismic regionalisation** (Manual de Diseño de Obras Civiles — Diseño por Sismo; zone summary by SGM) | `https://www.sgm.gob.mx/Web/MuseoVirtual/Riesgos-geologicos/Sismologia-de-Mexico.html` | Design zones A (lowest; ground acceleration not expected above 10 % of g) to D (large historical quakes, very frequent; acceleration can exceed 70 % of g) |
| **Atlas de Riesgos CDMX** | `https://www.atlas.cdmx.gob.mx/` | CDMX hazard layers (seismic, flooding, slope susceptibility, ground fracturing), also as open data via SIGCDMX |

### Specific risks

#### Earthquake — CRITICAL

- **Pacific subduction zone** = highest hazard (CFE seismic Zone D)
- **Pacific southwest (Oaxaca/Chiapas/Guerrero)** = highest hazard
- **CDMX more than 350 km from the 1985 epicentre** (IRIS; BBC Mundo gives about 400 km — secondary) but **lake-bed amplification** — CDMX building rules split the city into geotechnical Zona I (Lomas), II (Transición) and III (Lago) (NTC Diseño por Sismo, Gaceta Oficial CDMX):
  - **1985 M8.1** (19 Sep 1985, Michoacán coast, 15 km deep; official toll 6,000 deaths, other estimates run from 9,500 (IRIS) to 40,000 (Gaceta UNAM) — secondary) (source: CENAPRED "Los sismos históricos de septiembre", 2022 — `https://www.gob.mx/cenapred/articulos/los-sismos-historicos-de-septiembre`)
  - **2017 M7.1** (19 Sep 2017; epicentre 8 km NW of Chiautla de Tapia, Puebla, 51 km deep, per CENAPRED; SSN's first report put it 12 km SE of Axochiapan, Morelos, 120 km from CDMX; **369 dead**, computed from CENAPRED's state counts: CDMX 228 + Morelos 74 + Puebla 45 + Edomex 15 + Guerrero 6 + Oaxaca 1)
  - **Recent**: M7.4 Ciudad Hidalgo, Chiapas (17 Jul 2026; 3,306 aftershocks by 2 Nov 2026) and M6.5 San Marcos, Guerrero (2 Jan 2026) (2026 data, source SSN special reports — `http://www.ssn.unam.mx/`)
- **Volcanic risk**:
  - **Popocatépetl** (~65 km SE of central CDMX per CENAPRED; 70 km in another CENAPRED publication) — active; Semáforo de Alerta Volcánica **Amarillo Fase 2**, 12 km exclusion radius (2026 data, source CENAPRED daily Popocatépetl report of 2 Nov 2026)
  - **Volcán de Colima** (Fuego de Colima) also active — "el volcán más activo de Norteamérica"; **Pico de Orizaba** (Citlaltépetl) "activo en estado de reposo" (active, at rest), last confirmed eruption 1846 (2025 data, source CENAPRED "Volcanes de México", 25 Apr 2025 — `https://www.gob.mx/cms/uploads/attachment/file/997664/Tema_2_Volcanes_Mexico.pdf`; 1846 per Smithsonian GVP)

#### Hurricane

- **Quintana Roo** (Riviera Maya, Cancún, Tulum) — Atlantic hurricanes
- **Pacific** (Baja California, Sinaloa) — Pacific hurricanes
- **Tabasco, Yucatán** — flooding
- Recent reference landfalls: **Otis** (Cat 5 near Acapulco, 25 Oct 2023; at least 52 deaths; costliest tropical cyclone on record for Mexico), **John** (Cat 3 in Guerrero, Sep 2024; 29 deaths), **Beryl** (Cat 1 just NE of Tulum, 5 Jul 2024), **Erick** (Cat 3 in far-western Oaxaca, Jun 2025) (2025 data, source NHC Tropical Cyclone Reports EP182023, EP102024, AL022024, EP052025 — `https://www.nhc.noaa.gov/data/tcr/`)

#### Other

- **Landslide + flooding**: CDMX hillsides, Tabasco
- **Drought**: CDMX water crisis — Cutzamala system **95.12 % full on 26 Oct 2026** (744.3 of 782.5 Mm³), against 97.40 % on 31 Oct 2025, 87.48 % on 31 Jan 2026 and a low of **26.01 % on 19 Jun 2024** (2026 data, source CONAGUA OCAVM daily storage reports — `https://www.gob.mx/conagua/documentos/almacenamiento-en-presas-del-sistema-cutzamala`); structural drought risk remains, though secondary reports in early 2026 put short-term supply as secured for ~2 years (Mexico News Daily, not re-verified)
- **Wildfire**: increasing northern + central
- **Cenotes / collapses**: Yucatán karst

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1985 (pre-Mexico City quake)** | Non-seismic standards — DANGEROUS in CDMX zones |
| **Post-1985** | Reformed seismic code |
| **Post-2017** | CDMX: Reglamento de Construcciones reform + updated Normas Técnicas Complementarias (Gaceta Oficial CDMX 15 Dec 2017); NTC Diseño por Sismo re-issued by acuerdo of 20 May 2020 |
| **Asbestos** | pre-2000 buildings likely; less regulated than EU |
| **Lead** | water pipes, paint pre-2000 |

### Mandatory at sale

| Document | Required because | Notes |
|---|---|---|
| **Cédula catastral** | Municipal cadastre | Catastro |
| **Constancia de no adeudo** | No-debts (predial + water) | Municipal |
| **Avalúo** | Appraisal for tax basis | Perito SHF certified |
| **Certificado de libertad de gravamen** | No-liens | RPP |
| **Boleta predial** | Property tax paid | Annual |
| **Notario público** | MANDATORY + EXPENSIVE | 4-7% of price total closing |
| **Fideicomiso permit (SRE)** | Restricted Zone foreign | Foreigners only |

---

## Section: `--mains`

### Sources

- **CONAGUA** federal regulator
- **SEGIAGUA** (Secretaría de Gestión Integral del Agua, CDMX) — created by decree in Gaceta Oficial CDMX 3 Oct 2024, with **SACMEX** (Sistema de Aguas, water + drainage) sectorised under it and legal references to SACMEX read as SEGIAGUA (2024 data, source Gaceta Oficial CDMX 3 Oct 2024 transitorios Décimo Tercero + Décimo Noveno, PAOT copy — `https://paot.org.mx/centro/leyes/df/pdf/2024/GOCDMX_03_10_2024_6_14.pdf`; later restructuring not re-verified — check segiagua.cdmx.gob.mx) — rates/figures may have changed since
- Municipal / state operators, e.g. **Agua de Hermosillo** (AguaH, Sonora), **JAPAY** (Junta de Agua Potable y Alcantarillado de Yucatán)

### Verification

- **CDMX water crisis ongoing**: cisterns + tinacos universal even with mains
- **Cutzamala system 95.12 % full on 26 Oct 2026** (744.3 of 782.5 Mm³; 97.40 % on 31 Oct 2025; 91.08 % on 1 Jan 2026 falling to 87.48 % on 31 Jan 2026; low of 26.01 % on 19 Jun 2024) (2026 data, source CONAGUA OCAVM daily storage reports — `https://www.gob.mx/conagua/documentos/almacenamiento-en-presas-del-sistema-cutzamala`); 2025 was one of the wettest years since 1982 (Mexico News Daily; Mexico Business News — secondary, not re-verified)
- **Rural**: cisterns + septic standard; only **12.3 % of rural localities** (under 2,500 inhabitants; 22,638 localities) have a public drainage network, home to **41.7 % of the rural population** — locality-level, not dwelling-level: confirm the property's own connection or septic tank on site (2020 data, source INEGI "¿Qué hay en las localidades rurales de México?" 2024 — `https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/nueva_estruc/889463915119.pdf`) — rates/figures may have changed since

### Costs

| Scenario | Cost (MXN) |
|---|---:|
| Mains connection | 15,000–50,000 |
| Septic upgrade (est. installed; Rotoplas Biodigestor Plus+ 1,300 L tank alone 18,516 — 2026 data, manufacturer online store) | ~30,000–80,000 |
| Cisterna installation (10,000L) (est.; the low end sits below the Rotoplas 10,000 L tank-only price of 37,904 sale / 50,539 list, 54,890 list equipped — 2026 data, manufacturer online store; other brands not checked; excavation + installation extra) | ~20,000–50,000 |
| Tinaco rooftop tank (est. installed; Rotoplas 1,100 L tank alone 3,330 sale / 4,440 list, 2,500 L 6,912 / 9,216 — 2026 data, manufacturer online store) | ~5,000–15,000 |

---

## Cost benchmarks (MX 2026)

| Work | Cost (MXN) |
|---|---:|
| Avalúo (perito SHF) | 5,000–15,000 |
| Notario público (varies by state) | 0.75–2.5% of price (est.); Jalisco 2026 arancel cap ≈2.5% at MXN 1M, ≈2.1% at 1.5M, ≈1.6% at 3M, plus 16% IVA (secondary — Tandacasa, citing Ley del Notariado de Jalisco art. 133 and the Colegio de Notarios de Jalisco 2026 cuotas) |
| Registration (RPP) | 0.5–1% (est., varies by state); CDMX 2026: flat **MXN 25,098** per inscription of a purchase above MXN 1,407,720, sliding MXN 2,505–17,535 below (2026 data, source: Consejería Jurídica CDMX — DGRPPC 2026 fee schedule, Código Fiscal CDMX art. 196) |
| Fideicomiso setup (foreign Restricted Zone) | USD 2,000–3,000 |
| Fideicomiso annual fee | USD 350–1,000 |
| **Total transaction cost (outside Restricted Zone)** | **~5–8%** of price |
| **Total transaction cost (Restricted Zone foreign)** | **~7–12%** |
| Roof renovation | 80,000–200,000 |
| Asbestos abatement | 30,000–150,000 |
| Energy retrofit | 100,000–400,000 |
| Earthquake retrofit (older builds) | 200,000–800,000+ |
| Tinaco + cisterna combo | 25,000–65,000 |

## Active fiscal incentives (2025-2026)

- **Sheinbaum Vivienda para el Bienestar**: sexennial target **1.8M homes** — 1.2M by INFONAVIT (affiliated workers), 500k by CONAVI (non-affiliated households), 100k by FOVISSSTE (2026 data, source: Segundo Informe de Gobierno, 1 Sep 2026); 667k contracted, 277k under construction and 89k assigned as of 14 Sep 2026, 37% of the target (Presidencia communiqué 14 Sep 2026, reproduced by Wikipol — secondary relay)
- **INFONAVIT Vivienda para el Bienestar homes** (about MXN 600,000 each) for affiliated workers earning 1–2.9 minimum wages, with at least 6 months in their job and no current mortgage; INFONAVIT credits carry a fixed rate set by salary level, not zero interest (2026 data, source: INFONAVIT); CONAVI's 500k homes go to non-affiliated households earning 1–2 minimum wages (2025 data, source: Presidencia de la República, 8 Jan 2025 — rates/figures may have changed since); the 0% rate announced in Dec 2024 was for that non-affiliated financing via CONAVI and Financiera para el Bienestar, for incomes up to 2 minimum wages (N+ 10 Dec 2024, secondary — rates/figures may have changed since)
- **2025: 390,983 homes in construction against a 386,000 target for the year** (Sedatu, as reported by El Economista 27 Dec 2025 and Centro Urbano — secondary)
- **INFONAVIT regulatory reform 2025** (Ley del INFONAVIT, DOF 21 Feb 2025): the institute can buy land and build housing for social rental or sale to affiliated workers through a subsidiary (empresa filial) (2026 data, source: Cámara de Diputados LIFNVT consolidated text, última reforma DOF 21-02-2025); first time in 30 years (2026-04 research)
- **Legacy 'impagable' INFONAVIT loans**: about 4,856,052 credits "saneados" through settlements, discounts and write-downs under the Programa Solución Integral Infonavit, Oct 2024 – Jul 2026 (2026 data, source: Segundo Informe de Gobierno, 1 Sep 2026)

## Common listing platforms

- **Inmuebles24** (QuintoAndar group since Dec 2021; share ranking data not publicly available)
- **Vivanuncios**, **Lamudi MX**, **Propiedades.com**
- **Point2Homes** — English-language for foreign buyers (Mexlist ❌ DEPRECATED — mexlist.com is a Mexican-railways community, not a property portal; checked 2026-11-03)

## Caveats unique to MX

- **Fideicomiso for foreigners in Restricted Zone (50 km coast / 100 km border)** — mandatory bank trust; constitutional Article 27
- **Ejido land** (~50% of MX territory together with comunidades; RAN registers ≈82.2M ha ejidal + ≈17.5M ha communal, 2022 data, source: RAN Indicadores básicos de la propiedad social — rates/figures may have changed since) — cannot be sold to foreigners: only Mexicans can be ejidatarios or avecindados, and parcel rights pass only within the ejido (Ley Agraria arts. 13, 15, 80; última reforma DOF 14-11-2025); "regularización" (dominio pleno) is a complex multi-step process
- **Closing through the notario público is EXPENSIVE** — the notary's closing bill (ISAI + registration + notary fee) commonly totals 4–7% of price (est.); ISAI is usually the single biggest line, the notary fee itself 0.75–2.5%
- **Cadastral value 30-60% below market** (est.) — intentionally; affects predial only — under pressure from the federal cadastral harmonisation law (DOF 23 Oct 2026; see `--tax` › Annual property tax)
- **State-by-state divergence extreme** — RPP, ISAI, predial, registration all differ per state, and ISAI and predial often per municipio (Quintana Roo ISAI 3% in Cancún vs 4% in Playa del Carmen and Tulum, 2026)
- **CDMX water crisis** — Cutzamala system stress; "Day Zero" fears
- **Earthquake risk**: 1985 + 2017 reference events; lake-bed amplification CDMX-specific
- **Popocatépetl** active volcano 50km from CDMX
- **CDMX Airbnb Law Oct 2024** — host + platform registries (Padrón de Anfitriones + Plataformas) went live 21-22 May 2026 (Gaceta Oficial CDMX aviso announced for 22 May 2026, publication not confirmed), original ~20-21 Jun 2026 folio deadline extended to December 2026 for hosts (announced 19 Aug 2026, secondary — verify at estanciaeventual.cdmx.gob.mx); 50 % annual occupancy cap (Art 61 Sexies 4th paragraph, Gaceta Oficial CDMX 3 Oct 2024) contested — Airbnb + host amparos; suspensión definitiva was granted in some cases (verified 2026-07-02), but jurisprudencia **PR.A.C.CN. J/20 A (12a.)** (Pleno Regional en Materias Administrativa y Civil de la Región Centro-Norte, contradicción de criterios 122/2025, 27 Nov 2025; obligatory from 16 Feb 2026) holds suspensión definitiva against the cap improcedente, and on 28 Oct 2026 the SCJN Pleno unanimously reassumed competence over amparo en revisión 182/2026 (reasunción 173/2026) to decide whether the cap and the three-inmueble limit breach libertad de comercio, libre competencia and vivienda digna — merits ruling pending (2026 data, sources: [Semanario Judicial de la Federación, registro 2031768](https://sjf2.scjn.gob.mx/detalle/tesis/2031768); [SCJN versión taquigráfica preliminar, 28 Oct 2026](https://www.scjn.gob.mx/sites/default/files/versiones-taquigraficas/documento/2026-10-28/Versi%C3%B3n%20preliminar%2028102026%20S.pdf); see `--rental`)
- **Quintana Roo RETUR-Q** + 6% ISH lodging tax
- **Sheinbaum housing initiatives** — Vivienda para el Bienestar targets 1.8M homes this sexenio; INFONAVIT credits are fixed-rate by salary level, not zero-interest (see Active fiscal incentives)
- **USD-denominated listings** common in Restricted Zone (Tulum, Cabo, Vallarta)
- **Mérida + Yucatán** — tourism + retiree market; cenote risk
- **Hurricane belts** affect Quintana Roo (Atlantic) + Baja/Pacific separately

## Reddit / forum sources

- **r/mexico**, **r/MexicoCity**
- **r/expats**, **r/expatsmexico**
- **r/MoveToMexico**
- **El Universal Inmobiliario**, **El Financiero Real Estate**

## Verification authorities

| Authority | When to call |
|---|---|
| **RPP estatal** | Title verification |
| **Catastro municipal** | Cadastral value + cuenta catastral; once the ATDT platforms operate (target 1 Jan 2027, on an ATDT calendar) also the **Clave Única Catastral**, linked to the RPP folio real through the Cédula Única Catastral y Registral (Ley General para el Fortalecimiento y Armonización Catastral y Registral, DOF 23 Oct 2026, art. 43 + Transitorio Quinto) |
| **RAN** | If ejido land |
| **SRE** | Fideicomiso permit (foreign Restricted Zone) |
| **Notario público** | Mandatory closing |
| **SAT** | Tax compliance |
| **Banco fiduciario** | If fideicomiso |
| **CENAPRED** (Atlas Nacional de Riesgos) + state / municipal Atlas de Riesgos (e.g. Atlas de Riesgos CDMX) | Risk maps |
| **Organismo operador de agua** (SEGIAGUA / SACMEX in CDMX, JAPAY in Yucatán, AguaH in Hermosillo) | Water connection + no-debt status |

## Source URL templates

| Source | URL pattern |
|---|---|
| SHF HPI | `https://www.gob.mx/shf` |
| INEGI Vivienda | `https://www.inegi.org.mx/temas/viviendasat/` |
| RPP CDMX | `https://data.consejeria.cdmx.gob.mx/index.php/rppyc` (Consejería Jurídica y de Servicios Legales — RPPyC microsite) |
| Catastro CDMX | `https://datos.cdmx.gob.mx/dataset/informacion-catastral-de-la-ciudad-de-mexico` (SAF per-predio dataset, by alcaldía; last updated 1 Sep 2026) + `https://sig.cdmx.gob.mx/datos/descarga` (SIGCDMX, by cuenta catastral; files labelled catastro2021) — valor unitario del suelo is valid only for predial |
| SICT Datos Viales (TDPA) | `https://micrs.sct.gob.mx/infraestructura/direccion-general-de-servicios-tecnicos/datos-viales` |
| Atlas Nacional de Riesgos | `http://www.atlasnacionalderiesgos.gob.mx/` |
| Atlas de Riesgos CDMX | `https://www.atlas.cdmx.gob.mx/` |
| CONAGUA Cutzamala storage | `https://www.gob.mx/conagua/documentos/almacenamiento-en-presas-del-sistema-cutzamala` |
| RAN (ejido) | `https://www.gob.mx/ran` |
| SSN seismic | `https://www.ssn.unam.mx/` |
| CENAPRED | `https://www.gob.mx/cenapred` |
| CONAGUA | `https://www.gob.mx/conagua` |
| SAT (tax) | `https://www.sat.gob.mx/` |
| SRE (foreign) | `https://www.gob.mx/sre` |
| Inmuebles24 | `https://www.inmuebles24.com` |
| Lamudi MX | `https://www.lamudi.com.mx` |

## Status

✅ **Fully populated** as of 2026-04-26. Rental tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Rental tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (SHF Q2 2026 YoY + Lamudi Q4 2025 asking ranges), traffic (SICT Datos Viales + CAPUFE + city portals), tax (predial + ISAI per state / municipio + ISR + IVA + fideicomiso), rental (CDMX Código Civil lease rules + CDMX Airbnb Law Oct 2024 + Quintana Roo RETUR-Q / ISH), work (CONASAMI minimum wage + IMSS salary benchmark + job boards + RFC / RESICO), risks (SSN + CENAPRED + CONAGUA + 1985 + 2017 quakes + Popocatépetl + hurricane), mains (CONAGUA Cutzamala storage + water operators).
**Confidence**: HIGH for the statute-based rules re-read against Cámara de Diputados / DOF texts in the 2026-10-23 refresh — the Restricted Zone and fideicomiso chain (Constitución art. 27 fr. I; LIE arts. 2 fr. VI and 10–14, última reforma DOF 27-05-2024), the ISR 35 % top rate, the 700,000-UDI casa-habitación exemption, non-resident 25 % on gross rent (LISR art. 158), IVA 16 % and the LIVA art. 20 fr. II furnished-let rule, and the 2026 salario mínimo (CONASAMI resolution, DOF 9 Dec 2025); HIGH for the five ISAI / ISABI rows (2026 municipal and CDMX law texts; CDMX enacted values corroborated by secondary sources; Tijuana rango 7 printed rate to verify; the other states are not covered), the SHF Q2 2026 YoY column, the INEGI 2025 municipio count, the Quintana Roo ISH 5 % / 6 % split, the CDMX lease-term and rent-cap rules (Código Civil CDMX arts. 2448-C, 2448-D) and the agency readings in `--risks` / `--mains` (CONAGUA Cutzamala storage 26 Oct 2026, CENAPRED Popocatépetl semáforo 2 Nov 2026). MEDIUM for the CDMX 2026 predial tariff and bills (read from the Jefatura de Gobierno initiative, not the enacted decree), the Vivienda para el Bienestar figures (Segundo Informe targets primary; the 2025 homes-in-construction count secondary; the INFONAVIT eligibility band differs between sources), the CDMX 50 % short-let cap (legal basis confirmed: art. 61 Sexies 4th paragraph, Gaceta Oficial CDMX 3 Oct 2024; suspensión definitiva against it improcedente under jurisprudencia PR.A.C.CN. J/20 A (12a.); constitutionality pending before the SCJN after reasunción 173/2026 of 28 Oct 2026) and the December 2026 host-registration cutoff (secondary only), the Lamudi Q4 2025 MXN/m² ranges (not re-verified), and the curated `--risks` rows (build-era hazards, Mandatory-at-sale notes, Volcán de Colima status). LOW for unsourced estimates: the national predial range and the 30–60 % cadastral-to-market gap, notary / registration / avalúo / fideicomiso fees, the total transaction-cost bands, renovation and mains connection costs, the 2025 salary ranges, the traffic verdict bands, the Jalisco short-let lines and the job-board ranking; Reddit / forum sources not checked (Reddit blocked every route).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--tax` › Transaction taxes — ISAI / ISABI | 2026-10-23 | 2026-10-23 refresh wave | All five rows checked against 2026 municipal / CDMX law texts; set per municipio in Quintana Roo, Jalisco, Baja California Sur and Baja California; Q. Roo 2 % → Cancún 3 % / Playa del Carmen and Tulum 4 %; CDMX marginal 9.018 % (8.679 % in 2025); Tijuana rango 7 printed rate unverified |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | RPP CDMX, RAN, SRE and SAT live with matching titles; CENAPRED row relabelled (Atlas Nacional de Riesgos + state / municipal atlases); organismo operador de agua row added; Catastro row adds the Clave Única Catastral (MX-01) |

## Extension TODOs

- [ ] Per-state ISAI rates table (32 states)
- [ ] Per-municipio predial rates
- [ ] Fideicomiso bank fee comparison (Banamex, Banorte, BBVA, Santander)
- [ ] Ejido regularización flow (assembly → parcelization → RAN → RPP)
- [ ] Earthquake zone overlay (CFE Zones A-D)
- [ ] Restricted Zone perimeter map
- [ ] Notario público fee comparison per state
- [ ] CDMX Airbnb cap amparo-litigation tracker (SCJN merits ruling pending after reasunción 173/2026 of 28 Oct 2026; suspensión definitiva improcedente under jurisprudencia PR.A.C.CN. J/20 A (12a.); registry live 22 May 2026)
- [ ] Cadastral vs market value reconciliation tool
- [ ] CDMX water crisis impact per delegación

## Update history

- **2026-04-26** — Initial population (researched 2026-04)
- **2026-10-23** — Refresh wave (sources read 23 Oct – 3 Nov 2026); `--tax` › Transaction taxes (ISAI / ISABI) and Verification authorities re-verified (see Per-section verification). Country profile, `--price`, `--rental`, `--work`, `--traffic`, the rest of `--tax`, `--risks` and `--mains` were refreshed but not fully re-verified, so the playbook-level date stays 2026-04-26. Counts (changed / confirmed / unverifiable): Country profile 4 / 3 / 4; `--price` 22 / 4 / 15; `--rental` 8 / 6 / 7; `--work` 3 / 6 / 6; Common listing platforms 2 / 2 / 2; Reddit / forum sources 0 / 0 / 7; `--tax` › Predial 3 / 1 / 2; ISAI / ISABI 5 / 1 / 0; Other taxes 2 / 6 / 3; Fideicomiso 2 / 3 / 2; Total transaction cost 1 / 0 / 2; Future risk 1 / 1 / 1; Cost benchmarks 2 / 0 / 10; Active fiscal incentives 4 / 1 / 1; Caveats unique to MX 3 / 5 / 1 (plus the CDMX short-let cap line, 1 changed); `--traffic` 2 / 2 / 2; `--risks` 11 / 8 / 4; `--mains` 7 / 2 / 2; Verification authorities 2 / 4 / 0; Source URL templates 1 / 10 / 1. Main changes: INEGI 2025 count of 2,478 municipios and demarcaciones; Banxico FIX 18.7962 MXN/USD (DOF 3 Nov 2026); ejidos + comunidades ≈51 % of the territory (RAN atlas); price table now carries SHF Q2 2026 YoY with Lamudi Q4 2025 ranges labelled not re-verified; Inmuebles24 owned by QuintoAndar (not OLX); Mexlist marked DEPRECATED (not a property portal); CDMX one-year forced lease term (art. 2448-C) and inflation rent cap with the Registro Digital (art. 2448-D); the 50 % short-let cap's litigation status (jurisprudencia PR.A.C.CN. J/20 A (12a.), SCJN reasunción 173/2026); RETUR-Q registration duty and fines; Quintana Roo host duties under ISH art. 7 replace 'residency + RFC'; the municipal platform-ban claim flagged as unsupported; salario mínimo from the DOF, with the ZLFN as 45 municipios rather than six states; IMSS salary benchmark; RESICO MXN 3.5 M threshold; CDMX 2026 predial tariff, subsidies and bills, early-payment discounts sampled at 8–16 % (no 25 % found); ISAI set per municipio, Quintana Roo 2 % corrected to 3–4 %; 700,000 UDI ≈ MXN 6.22 M at the DOF 3 Nov 2026 UDI; fideicomiso statute chain corrected (LIE arts. 10–14, art. 10-A SRE escrito outside the zone); the notary's 4–7 % reframed as its total closing bill, with ISAI the biggest line; CDMX RPP fee MXN 25,098 and the Jalisco notary arancel; MX-01 siblings on cadastral values; Vivienda para el Bienestar target 1.8 M homes, INFONAVIT credits fixed-rate rather than zero-interest, 390,983 = homes in construction rather than starts; SICT Datos Viales and the TDPA term; seismic zones via SGM, 1985 and 2017 quake details, Popocatépetl semáforo and distance, Pico de Orizaba at rest, recent hurricane landfalls, Cutzamala 95.12 % on 26 Oct 2026, post-2017 CDMX building rules; SEGIAGUA over SACMEX, AguaH = Agua de Hermosillo (not Hidalgo), rural drainage at locality level, septic / cisterna cost calibration; water-operator verification row and four source-URL rows added. Not verified and left as curated or est.: postcode examples, ejido sale rules, the Lamudi ranges, the cadastral 30–60 % gap, the Vivanuncios / Point2Homes / MLS lines, USD-denominated listings, the December 2026 host-registration cutoff, the Sheinbaum / UNESCO line, the Jalisco short-let lines, the job-board ranking, the 2025 salary ranges, the national predial range, notary / registration / avalúo / fideicomiso fees, the total-cost bands, renovation and mains connection costs, Volcán de Colima status, the ~2-year supply claim, the traffic verdict bands and the Reddit / forum sources (Reddit blocked)
- **2026-10-28** — Country profile: federal cadastre-law bullet (Ley General para el Fortalecimiento y Armonización Catastral y Registral, DOF 23 Oct 2026, in force 24 Oct 2026; tracked in `shared/regulatory-watch.md`)
