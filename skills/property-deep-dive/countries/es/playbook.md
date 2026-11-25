# Spain 🇪🇸 — Property Due-Diligence Playbook

ISO2: `es`. Status: ✅ Fully populated (researched 2026-04; Tier-A quarterly refresh 2026-07-03).

## Country profile

- **Postcode (CP)**: 5 digits (`28013` Madrid centro, `08001` Barcelona, `46001` Valencia)
- **Admin levels**: 17 CCAA (Comunidades Autónomas) + 2 ciudades autónomas (Ceuta, Melilla) + 50 provincias + 8,131 municipios
- **Currency**: EUR (€)
- **Languages**: Castilian (official); co-official: Català (Cataluña, Balears, Valencia), Galego (Galicia), Euskera (País Vasco, Navarra)
- **Cadastre**: **Catastro Nacional** (Ministerio de Hacienda) — FREE public viewer
- **Identifier**: Referencia Catastral (14-char alphanumeric) + Registro de la Propiedad (separate)
- **CRITICAL**: 17 CCAA mean **massive variation** in tax (ITP, ISD, wealth, VTV) across regions
- Distinct ownership types: pleno dominio (freehold), usufructo (usufruct), nuda propiedad (bare ownership), división horizontal (commonhold)

## Section: `--price`

### Primary sources

- **Catastro Sede Electrónica** (FREE consultation): `https://www.sedecatastro.gob.es/`
  - Search by Referencia Catastral, calle + número, or coordinates
  - Returns: valor catastral (cadastral value), surface, year built, use
- **Registro de la Propiedad Online** (paid notas simples): `https://www.registradores.org/`

### Listing platforms

- **Idealista** (largest by far): `https://www.idealista.com/<provincia>/<municipio>/`
- **Fotocasa**: `https://www.fotocasa.es/`
- **Habitaclia**: `https://www.habitaclia.com/`
- **Pisos.com**: `https://www.pisos.com/`
- **Wallapop, Milanuncios** — privates
- **Tinsa, Sociedad de Tasación, ST Tasaciones**: appraisal indices

### Price benchmarks (2025-2026)

- **INE Índice de Precios de Vivienda (IPV)**: `https://www.ine.es/`
- **Fomento estadística vivienda libre + protegida**: `https://www.mitma.gob.es/`
- **Idealista Informe de Precios** quarterly
- **Tinsa IMIE**
- **INE IPV national YoY: +12.2 %** (Q2 2026, published 2026-09-07; segunda mano +12.9 %, nueva +7.4 %; +3.4 % on the quarter; base 2025). Regional spread +9.5 % (Navarra) to +15.2 % (Ceuta); Asturias +15.0 % and Castilla y León +14.8 % next, País Vasco +10.0 % and Cataluña +10.1 % next-lowest. Source [INE IPV2T26](https://www.ine.es/dyngs/Prensa/IPV2T26.htm) — €/m² ranges below are 2024-2025 vintage and now run low; re-check Idealista zonal.

| Region/City | Resale €/m² (2024-2025 vintage, not updated for the INE IPV rises to Q2 2026) |
|---|---:|
| **Madrid (Comunidad)** | 4,000–6,500 (centro 7,000–10,000) |
| **Barcelona (provincia)** | 3,500–5,500 (Eixample/Gràcia 5,500–8,500) |
| **País Vasco (San Sebastián)** | 5,000–7,500 |
| **Bilbao** | 3,500–4,500 |
| **Costa del Sol (Marbella)** | 4,500–8,000 (luxury 10k+) |
| **Costa Brava** | 3,000–5,500 |
| **Mallorca** | 4,500–7,500 |
| **Valencia** | 2,500–4,000 |
| **Sevilla** | 2,500–3,500 |
| **Zaragoza** | 1,800–2,500 |
| Rural Castilla / Extremadura / Aragón | 600–1,500 |

### Compute

1. Listing €/m² = price / superficie útil (usable) or construida (built — includes walls)
2. **Trap**: Cataluña + Valencia + Andalucía coast often inflate by including terraza, ático
3. **Trap**: pueblos rurales sometimes price by **superficie construida** + sometimes **m² escritura** (deed-quoted) — can differ
4. Compare to Idealista zonal (per barrio) for accurate market view
5. Valor catastral (~50 % of market) for tax base — the market-reference coefficient RM of 0.50 (Orden de 14 de octubre de 1998) is applied when a municipio's ponencia de valores is revised, so values from an older ponencia can sit well below 50 % of today's prices (inference) (2026-11-25 verified; source [Orden EHA/1213/2005](https://www.boe.es/buscar/pdf/2005/BOE-A-2005-7254-consolidado.pdf))

---

## Section: `--traffic`

### Sources

- **Ministerio de Transportes y Movilidad Sostenible**: `https://www.mitma.es/`
- **DGT (Dirección General de Tráfico)**: `https://www.dgt.es/`
- **Provincial road services** (Diputaciones)
- CCAA-level (Cataluña, Madrid, Andalucía have own systems)

### Key term

**IMD (Intensidad Media Diaria)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (calle vecinal, carretera local)
- 🟡 1,000–8,000 v/d (carretera autonómica, calle urbana)
- 🟠 8,000–30,000 v/d (N-road, avenida, ronda urbana)
- 🔴 > 30,000 v/d (autovía/autopista, urban core)

---

## Section: `--tax`

> **⚠️ "100 % non-EU buyer gravamen" — NOT law; the bill LAPSED on 6 Oct 2026 (verified 2026-11-25).** The widely-reported January 2025 government announcement of a 100 % gravamen on non-EU non-resident property buyers was formalised by the Grupo Parlamentario Socialista as **[Proposición de Ley 122/000196](https://www.congreso.es/es/proyectos-de-ley?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=122/000196)** (BOCG B-229-1, 30/05/2025). It sat at **"Pleno - Toma en consideración" from 5 September 2025 to 6 October 2026** without a floor vote, was never assigned to a committee and never went through an amendments process; it has been **"Concluido - (Caducado)" since 6 October 2026**, when Real Decreto 806/2026, de 5 de octubre (BOE núm. 248, 6 Oct 2026) dissolved the Cortes Generales and called general elections for 29 Nov 2026 — under art. 207 of the Reglamento del Congreso, pending matters lapse on dissolution. Any revival needs a new initiative in the next legislature. Before lapsing it had been **quietly dropped from the government's January 2026 housing package**, and per Reuters parliamentary documents on 27 March 2026 it had no realistic path to passage (Junts withdrew government support; Podemos opposed it from the left as insufficient). The 6 Oct 2026 housing decrees (RDL 28/2026 + 29/2026) contain no non-EU or non-resident buyer tax (La Moncloa summary, 8 Oct 2026). **No BOE-published Ley exists.** Do NOT factor a 100 % gravamen into TCO models or buyer briefs as if enacted. Tracked at `shared/regulatory-watch.md` § Spain 122/000196. Original proposal scope (NOT law): 100 % on catastral reference value, second-hand residential only (new builds excluded under IVA), non-EU non-residents, foral PV+Navarra exempt, ITP deductible — flagged by PwC + multiple legal analyses as TFEU Art. 63 (free movement of capital) risk if enacted. (2026-11-25 verified, sources [Congreso 122/000196](https://www.congreso.es/es/proyectos-de-ley?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=122/000196) + [La Moncloa 13 Jan 2025](https://www.lamoncloa.gob.es/presidente/actividades/paginas/2025/130125-sanchez-foro-vivienda.aspx) + [La Moncloa 8 Oct 2026](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/vivienda-agenda-urbana/paginas/2026/decreto-vivienda-medidas.aspx) + [BOCG B-229-1 PDF](https://www.congreso.es/public_oficiales/L15/CONG/BOCG/B/BOCG-15-B-229-1.PDF) + [BOE Real Decreto 806/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20742) + [Reglamento del Congreso art. 207](https://www.boe.es/buscar/act.php?id=BOE-A-1982-5196) + [Reuters via US News 2026-03-27](https://www.usnews.com/news/world/articles/2026-03-27/spains-100-non-eu-property-tax-stalls-in-congress) + [PwC Periscopio Fiscal Jun 2025](https://periscopiofiscalylegal.pwc.es/nuevo-impuesto-sobre-la-transmision-de-muebles-a-no-residentes-en-la-ue/))

### Annual property tax — IBI (Impuesto sobre Bienes Inmuebles)

- Set by **ayuntamiento** (municipality)
- **Urbano**: **0.4–1.1 %** of valor catastral (statutory band; ~0.5–0.7 % est. central tendency — verify per-municipio at the ayuntamiento *ordenanza fiscal*)
- **Rústico**: 0.3–0.9 %
- **Características especiales**: 0.4–1.3 %
- Bills annually, often Q3-Q4
- Some bonificaciones available (large families, energy efficient, etc.)
- **Tourist-let IBI surcharge (optional, 2027 IBI at the earliest)**: Real Decreto-ley 29/2026 (BOE-A-2026-20823, in force 8 Oct 2026, convalidated 12 Nov 2026) adds TRLRHL art. 72.4 ter — in a declared zona de mercado residencial tensionado the ayuntamiento may, by ordenanza fiscal, surcharge the cuota líquida of residential property used as tourist lodging by up to 50 % (up to 100 % for owners of 2 or more such units, up to 150 % for 4 or more); check the municipio's ordenanza (2026-11-25 verified; source [BOE TRLRHL art. 72](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214) + [BOE convalidation](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-23755))

### Other annual taxes

- **Tasa de basura** (waste-collection fee): est. ~€40–€300/yr per dwelling (calibration: a compilation of the 2026 ordenanzas fiscales of 48 provincial capitals puts a model dwelling between €43.80 in León and €292.48 in València — [Guía Fiscal, Oct 2026](https://guiafiscal.es/patrimonio/tasa-basura/granada), secondary aggregator); each ayuntamiento sets the fee in its ordenanza fiscal, so check the municipio's ordenanza or the seller's last recibo
- **IIVTNU (plusvalía municipal)**: paid on sale (capital-gain-like, on land value)
- **Wealth tax (Impuesto sobre el Patrimonio)**: regional — varies massively:
  - **Madrid** (since 2009), **Andalucía**, **Extremadura**, **Cantabria**, **La Rioja** (from 2022, 2023, 2024 and 2025 respectively): 100 % bonificación of the cuota (effectively ZERO at CCAA level); while the ITSGF is in force, Madrid, Andalucía and La Rioja replace it with a bonificación equal to the difference between the Patrimonio cuota and the ITSGF cuota (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf))
  - **Cataluña**: 0.21–2.75 % progressive on wealth >€500k (mínimo exento); while the ITSGF is in force the scale adds a 3.48 % band above €20M (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. IV](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-iv-tributacion-autonomica-2026.pdf) + [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf))
  - **Comunidad Valenciana**: 0.25–3.5 %
- **ITSGF (Impuesto Temporal de Solidaridad de las Grandes Fortunas)**: federal top-up, **1.7–3.5 % progressive on net wealth >€3M**, made indefinite by RD-Ley 8/2023 (27 Dec 2023; original Ley 38/2022). Deducts what was paid under regional Patrimonio → neutralises the Madrid/Andalucía 100 % bonificación for HNW. (2026-11-25 verified; source [BOE Ley 38/2022, consolidated](https://www.boe.es/buscar/act.php?id=BOE-A-2022-22684) + [AEAT ITSGF page](https://sede.agenciatributaria.gob.es/Sede/declaraciones-informativas-otros-impuestos-tasas/impuesto-temporal-solidaridad-grandes-fortunas.html))

### Transaction taxes — ITP (Impuesto sobre Transmisiones Patrimoniales)

**MAJOR REFORM 2025**: Catalonia steepened its already-progressive ITP scale (from 10 % ≤€1M + 11 % above, to four brackets topping at 13 % >€1.5M) for taxable events from 27 Jun 2025 (2026-11-25 verified; source [ATC tarifes-tipus](https://atc.gencat.cat/ca/tributs/itpajd/tpo/tarifes-tipus))

| CCAA | ITP rate (resale) |
|---|---:|
| **Madrid** | **6.0 %** (lowest general rate among the régimen-común CCAA; 2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **Navarra** | 6.0 % |
| **País Vasco** | Bizkaia: **4 %** housing (with up to 2 garage spaces and annexes in the same building; **6 %** if the buyer already owns more than 5 dwellings with a stake above 50 % in each), **2.5 %** for a habitual home of up to 120 m² built, **7 %** other property (2026 data, source [Bizkaia NF 1/2011](https://www.bizkaia.eus/documents/880307/15187815/ca_1_2011.pdf/50b78491-3852-b68f-f9d5-2db574a48917?t=1777386142905) + [Bizkaia gastos fiscales 2027](https://www.bizkaia.eus/fitxategiak/05/ogasuna/presupuestos/otros/2027/1792596039668_2-IV-0-Ppto%20Gastos%20Fiscales%202027%20TRADUCIDO_ca.pdf)); Gipuzkoa and Araba set their own rates — verify at their Haciendas forales |
| **Andalucía** | 7.0 % |
| **Aragón** | 8.0–10.0 % progressive (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **Asturias** | 8.0–10.0 % progressive (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **Cantabria** | 9.0 % (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **Castilla y León** | 8.0–10.0 % |
| **Castilla-La Mancha** | 9.0 % |
| **Galicia** | 8.0 % |
| **Murcia** | 7.75 % (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **Comunidad Valenciana** | **9.0 %** general (≤€1M) · **11 %** >€1M (pre-existing band, retained) — general rate cut 10 %→9 % by Ley 5/2025 (BOE-A-2025-11959), eff. 1 Jun 2026; AJD 1.5 %→1.4 % same date; reduced TPO rates 8 % / 6 % (VPO régimen general, first home of buyers under 35, split at €180k) and 4 % / 3 % (VPO régimen especial, large or single-parent families, disability, gender-violence victims, split at €180k); AJD 0.1 % on vivienda habitual deeds (Ley 13/1997 arts. 13-14) (2026-11-25 verified; source [BOE Ley 13/1997, consolidated](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202) + [BOE Ley 5/2025](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-11959)) |
| **Baleares** | 8.0–13.0 % progressive (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **Cataluña** (Decret-llei 5/2025, eff. 27 Jun 2025) | **10 %** ≤€600k · **11 %** €600k–€900k · **12 %** €900k–€1.5M · **13 %** >€1.5M · **20 %** flat for grans tenidors (large holders: more than 10 urban residential units or more than 1,500 m² residential in Catalonia, or 5+ urban residential units in tensioned-market municipalities, counted across different tensioned zones for taxable events from 14 Jul 2026 under Llei 11/2026) and for whole residential buildings (TEH) · 5 % reduced rate (TUJ) for a habitual-residence buyer aged 35 or under at accrual (32 before 27 Jun 2025; income cap applies) (2026-11-25 verified; source [ATC tarifes-tipus](https://atc.gencat.cat/ca/tributs/itpajd/tpo/tarifes-tipus) + [BOE Llei 11/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-24007) + [Hacienda, Tributación Autonómica 2026, Cap. IV](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-iv-tributacion-autonomica-2026.pdf)) |
| **Canarias** | 6.5 % |
| **Extremadura** | 8.0–11.0 % progressive (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf)) |
| **La Rioja** | 7.0 % |
| **Ceuta, Melilla** | 6.0 % state rate with a 50 % bonificación on the TPO cuota for property there (computed: 6.0 % × 50 % = 3.0 % effective) (2026-11-25 verified; source [BOE TRLITPAJD arts. 11 + 57 bis](https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359)) |

### New build taxes

For obra nueva (new build, vendida by impresa):
- **IVA**: 10 % (residential) or 4 % (VPO de régimen especial or de promoción pública); from 1 Dec 2026 the 4 % rate (LIVA art. 91.Dos.1.6º) also covers developer sales of housing with permanent or indefinite protected status (Real Decreto-ley 29/2026, convalidated 12 Nov 2026; 2026-11-25 verified; source [BOE LIVA, consolidated](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) + [BOE RDL 29/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20823))
- **AJD (Actos Jurídicos Documentados)**: 0.75–1.5 % general rate in the régimen-común CCAA (Canarias and Madrid 0.75 %; La Rioja 1 %; Andalucía and Asturias 1.2 %; the rest 1.5 %, with the Comunitat Valenciana at 1.4 % from 1 Jun 2026); some CCAA charge higher rates on particular deeds, and Navarra and País Vasco set their own (2026 data, source [Hacienda, Tributación Autonómica 2026, Cap. I](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-i-tributacion-autonomica-2026.pdf) + [BOE Ley 5/2025](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-11959))
- No ITP on new builds

### Notario + Registro

- Notario: est. ~0.1–0.5 % of price (regulated by arancel; calibration: the arancel in [Real Decreto 1426/1989, número 2](https://www.boe.es/buscar/act.php?id=BOE-A-1989-28111) charges €90.15 up to €6,010.12 and then bands from 4.5‰ down to 0.3‰, less 5 %, which gives about €269 on a €100,000 deed and €388 on €300,000 (0.27 % and 0.13 %); copies, folios and IVA come on top)
- Registro de la Propiedad: est. ~0.05–0.3 % of price (calibration: the arancel in [Real Decreto 1427/1989, número 2](https://www.boe.es/buscar/act.php?id=BOE-A-1989-28112) charges €24.04 up to €6,010.12 and then bands from 1.75‰ down to 0.20‰, less 5 %, which gives about €127 on a €100,000 finca and €205 on €300,000 (0.13 % and 0.07 %); IVA, a second finca such as a garage, and notas simples come on top)
- Combined: est. ~0.15–0.8 % of price (sum of the two estimated ranges above); gestoría and tasación come on top

### Plusvalía municipal (capital gains-like)

- Reformed after 2021 Constitutional Court ruling
- Two methods (taxpayer chooses lower):
  1. Real-gain method
  2. Cadastral-coefficient method
- Set per ayuntamiento; varies wildly
- **New maximum coefficients from 1 Dec 2026** (Real Decreto-ley 29/2026, convalidated 12 Nov 2026): e.g. under 1 year 0.17 · 5 years 0.19 · 10 years 0.22 · 20 years or more 0.30 (2026-10-21 verified; source [BOE-A-2026-20823](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823))

### Total transaction cost (buyer side)

- Resale: est. **~6–14 %** of price (inputs: ITP 6–13 % general rates in the régimen-común CCAA, from Madrid at 6 % to the 13 % top bracket in Cataluña and Illes Balears, 2026 data, Hacienda; plus notary and registry est. ~0.15–0.8 %; gestoría, tasación and mortgage costs extra; the 20 % Catalan large-holder rate is excluded, and Bizkaia's 2.5–4 % housing rates and the 3 % effective rate in Ceuta and Melilla fall below this range)
- New build: est. **~11–12.5 %** of price (inputs: 10 % IVA + 0.75–1.5 % AJD general rate + notary and registry est. ~0.15–0.8 %)

### IRNR for non-residents

- **19 %** for EU/EEA residents on rental income
- **24 %** for non-EU/EEA on rental income
- 19 % on capital gains for any non-resident
- **Imputed income on a property that is not let** (TRLIRNR art. 24.5 applies the IRPF imputed-income rule; it still cites art. 87 of the 2004 IRPF text, now Ley 35/2006 art. 85): 2 % of valor catastral, or 1.1 % where revised cadastral values apply, taxed at the 19 % / 24 % rates above (Modelo 210). **From 1 Jan 2027**, under Real Decreto-ley 29/2026 (BOE-A-2026-20823, convalidated 12 Nov 2026), a progressive scale applies to the summed cadastral values of all non-let, non-habitual urban property — 1.1 % up to €100,000, rising by bracket to 3 % on the excess above €1,000,000; the decree does not amend the TRLIRNR and does not say how a summed scale fits per-property Modelo 210 filing (2026-11-25 verified; sources [AEAT renta imputada](https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/imputacion-rentas-inmobiliarias/calculo-renta-imputada.html) + [BOE IRPF art. 85](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) + [BOE TRLIRNR](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527); see `shared/home-tax.md` + `shared/regulatory-watch.md` ES)
- (IRNR rates — verify current year against AEAT before relying)

### Future risk

- Wealth tax political flux — depends on CCAA government changes
- Plusvalía in legal evolution post-2021
- Catalonia's 2025 steeper ITP scale (13 % top bracket >€1.5M) may inspire other CCAA
- **Oct 2026 housing decrees — split outcome**: on 12 Nov 2026 the Diputación Permanente (Cortes dissolved for the 29 Nov 2026 election) convalidated Real Decreto-ley 29/2026 (BOE-A-2026-23755) and derogated Real Decreto-ley 28/2026 (BOE-A-2026-23754), so the LAU art. 10 rewrite never took effect; their 29 Sep 2026 predecessors (RDL 26/2026, 27/2026) were derogated by the Congreso — check `shared/regulatory-watch.md` ES before modelling any of their measures

---

## Section: `--rental`

### Long-term residential

- Marco regulado: **LAU (Ley de Arrendamientos Urbanos)**
- Tenant protection moderate; eviction takes an est. 6-18 months (practitioner range, not an official statistic; calibration: a secondary compilation of CGPJ 2025 estimates puts the average juicio verbal de desahucio (CGPJ «verbales arrendaticios») at ≈5 months (Aragón) to ≈14 months (Castilla-La Mancha) by comunidad autónoma, median ≈9 months across comunidades ([lexdatalegal.com, secondary](https://lexdatalegal.com/datos/plazos-desahucio-por-comunidad)); the CGPJ's own [tiempos medios de duración](https://www.poderjudicial.es/cgpj/es/Temas/Transparencia/Estimacion-de-los-tiempos-medios-de-duracion-de-los-procedimientos-judiciales) table could not be read for verification on 2026-11-25 — check it directly); evictions of vulnerable occupants without a housing alternative are suspended until 31 Dec 2030 (Real Decreto-ley 29/2026 art. 2, convalidated 12 Nov 2026; 2026-11-25 verified; source [BOE-A-2026-20823](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823))
- **Mais Habitação-style controls**: rent caps in declared "zonas tensionadas" (Cataluña, Valencia, Bilbao introducing)
- **Real Decreto-ley 29/2026** (BOE-A-2026-20823, in force 8 Oct 2026, **convalidated** by the Diputación Permanente on 12 Nov 2026, BOE-A-2026-23755): a temporada lease needs a real, provable cause stated in the contract, must exceed 31 days and generally not exceed 12 months (new LAU art. 9 bis); tourist stays outside the LAU are capped at 31 days; simultaneous room lets cannot total more than the whole-unit rent; annual rent updates falling due by 31 Dec 2027 — none where rent is above the reference-index maximum, otherwise as newly agreed or capped at 2 %; tenants of leases in force on 8 Oct 2026 whose term ends before 31 Dec 2028, and who have paid monthly for the previous 8 months, may request an extraordinary extension of up to 2 years (the landlord may refuse only for own or family need, or where other terms or a new contract are agreed) (2026-10-21 verified)
- **Real Decreto-ley 28/2026** (BOE-A-2026-20822) — **DEROGATED by the Diputación Permanente on 12 Nov 2026** ([BOE-A-2026-23754](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-23754)), never in force; LAU art. 10 keeps the wording RDL 29/2026 art. 3.Ocho gave it from 8 Oct 2026, which only limits art. 10.1 to habitual-residence leases: after 5 years (7 for a legal-person landlord), mandatory annual extensions up to 3 more years unless the landlord gives at least 4 months' or the tenant at least 2 months' notice (2026-11-13 verified; source [LAU art. 10](https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003#a10)). It would have rewritten LAU art. 10 from 15 Nov 2026 — tacit, mandatory extensions in successive 5-year periods (7 years for a legal-person landlord), at least 6 months' notice of a landlord's non-renewal, and non-renewal compensation of the greater of 12 monthly payments at the upper value of the state rental reference index or 1 monthly payment per year resided (2026-10-23 verified; derogation 2026-11-13 verified; source [BOE-A-2026-20822](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20822))
- IRPF on rental income (residents, habitual-residence leases): the reduction on net positive rent depends on when the lease was signed (LIRPF art. 23.2 and DT 38ª) — **60 %** for leases signed before 26 May 2023; **50 %** as a rule (60-90 % where conditions are met) for leases signed from 26 May 2023 to 1 Dec 2026; for later leases the scale Real Decreto-ley 29/2026 introduced: for a landlord who is not a gran tenedor, 70-100 % on a new lease whose rent is cut by more than 5 %, 50 % where it is not raised, 15-40 % where it is raised (by the size of the rise) and 50-100 % on a first let; 70 % on a social or public-programme let and 60 % after a rehabilitation finished in the prior 2 years; and, whatever the signing date, 80 % during a tacit LAU art. 10.1 extension of a lease whose 5-year minimum term ends after 1 Dec 2026, where the initial rent is at or below the reference-index cap and the landlord is not a gran tenedor (2026-11-25 verified; sources [LIRPF art. 23](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23), [AEAT Manual IRPF 2025](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html))

### Short-let — VTV / VFT (Vivienda de Uso Turístico)

**Regional licensing (varies hugely)**:

| CCAA | Status |
|---|---|
| **Cataluña** | Strict; HUTV / HUT licenses; many municipios moratorium incl. Barcelona (BCN: all 10,101 HUT (2024 data, source [Ajuntament de Barcelona, 21 Jun 2024](https://ajuntament.barcelona.cat/premsa/2024/06/21/barcelona-impulsa-mesures-estructurals-per-fer-front-a-lemergencia-habitacional-i-augmentar-loferta-dhabitatge) — rates/figures may have changed since) lose their habilitation in November 2028 under the Generalitat's Decret llei 3/2023 DT2, which gives habilitated HUT in the listed municipios five years from its entry into force to obtain a llicència urbanística or cease — no calendar day is sourced; on 21 Jun 2024 the Ajuntament announced it will promote no new urban plan declaring tourist use compatible with habitual residence (a municipal announcement, not a municipal decree); DT2.2 allows one owner-requested extension of up to five years; the Constitutional Court dismissed the challenge to the Decret llei (STC 64/2025, 13 Mar 2025) (2026-11-25 verified; sources [BOE-A-2024-281](https://www.boe.es/buscar/doc.php?id=BOE-A-2024-281), [STC 64/2025](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-7430))) |
| **Baleares** | Mallorca + Ibiza near impossible to obtain new licenses |
| **Canarias** | Strict in Tenerife, Gran Canaria |
| **Madrid** | License + community approval; pressure from city hall |
| **Andalucía (Costa del Sol)** | License via VFT registration |
| **Comunidad Valenciana** | Easier than Cataluña; VTV registration |

**Tax**:
- **IRPF resident**: progressive on net rental income
- **IRNR non-resident** (TRLIRNR arts. 24-25): **19 %** for residents of another EU state or of an EEA state with effective tax-information exchange, who may deduct the IRPF expenses directly linked to the Spanish rental income (art. 24.6); **24 %** for everyone else, on the **gross** rent (art. 24.1) (2026-11-25 verified; source [TRLIRNR](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a24))
- **IVA** if hotel-style services (restaurant, cleaning, laundry or similar): 10 % VAT applies, treated as commercial. **From 1 Dec 2026** a furnished-dwelling let of **30 nights or fewer** to the same tenant also loses the VAT exemption and is taxed at **10 %**, unless it is in the dwelling that is the landlord's habitual residence — Real Decreto-ley 29/2026, de 6 de octubre, art. 7 (BOE-A-2026-20823), in force since 8 Oct 2026 and **convalidated** by the Diputación Permanente on 12 Nov 2026 (BOE-A-2026-23755) (2026-10-21 verified; convalidation 2026-11-13 verified; source [BOE-A-2026-20823](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823); tracked in shared/regulatory-watch.md)
- **Tasa turística — Cataluña (IEET: tarifa autonómica + recargo municipal)**: tariff schedule **REPLACED** by **Llei 2/2026 de 6 de març** (DOGC 9621, 10 Mar 2026), in force **1 Apr 2026** — all pre-2026 figures superseded. **Barcelona city totals per person per night, 1 Apr 2026–31 Mar 2027** (general tariff + €5.00 Ajuntament recàrrec): 5★/gran luxe €12.00 · 4★ €8.40 · habitatge d'ús turístic (HUT) €9.50 · albergs de joventut €6.00 (news-only: a September 2026 Plenari vote to hold the alberg recàrrec at €4.00, i.e. a €5.00 total, is not reflected in the ATC table read 2026-10-23 — verify with the ATC) · other establishments €7.00 · cruise call >12 h €9.00 / ≤12 h €11.00; the Ajuntament recàrrec steps up to €6.00 from 1 Apr 2027 and €7.00 from 1 Apr 2028. **Rest of Cataluña general tariff, 1 Apr 2026–31 Mar 2027**: 5★ €4.50 · 4★ €1.80 · HUT €1.75 · albergs €0.80 · other €0.90 — scheduled step-up from 1 Apr 2027 to 5★ €6.00 · 4★ €2.40 · HUT €2.50 · albergs €1.00 · other €1.20. **Municipal recàrrec outside Barcelona — in force since 1 Oct 2026 in seven municipios**: Castelldefels, Esplugues de Llobregat, L'Hospitalet de Llobregat, El Prat de Llobregat, Sabadell, Sant Cugat del Vallès and Sant Just Desvern (ATC convenis in DOGC 9758, 9760 and 9761, 25-30 Sep 2026). Recàrrec 1 Oct 2026–31 Mar 2027 (all but Esplugues): 5★ €4.00 · 4★ €1.80 · HUT €1.75 · albergs €0.80 · other €0.90; from 1 Apr 2027: 5★ €4.00 · 4★ €2.40 · HUT €2.50 (Castelldefels €2.40) · albergs €1.00 · other €1.20 (Sant Just publishes only the 1 Oct 2026 column). Computed HUT total there: €1.75 + €1.75 = **€3.50**, then **€5.00** from 1 Apr 2027 (Castelldefels €4.90). Esplugues rates only 4★ €1.80 · HUT €0.90 · other €1.75 (€2.40 / €1.20 / €2.50 from 1 Apr 2027); its "other" figure exceeds the regional tariff it is capped at, so the HUT and other rows look swapped — verify with the Ajuntament d'Esplugues / ATC. Every other non-Barcelona municipio charges the tariff only. Statutory rule (art. 34 ter): at most **€4** per category and never above the tariff, effective from the first semestral liquidation period after BOP publication of the ordinance once the ATC conveni is signed and published in the DOGC — computed, no further municipio can start before **1 Apr 2027**; check the ATC list for the property's municipio. Barcelona recàrrec statutory ceiling **€8/night** (art. 34 bis). Cap **7 stay-units per person**; persons aged **16 or under exempt** (2026 data, 2026-10-23 verified; source [ATC Quota tributària i tarifes](https://atc.gencat.cat/ca/tributs/ieet/quota-tributaria))
- **Tasa turística — Baleares (impuesto sobre estancias turísticas)**: **€1-4 per person per night** by establishment class — viviendas turísticas / vacation rentals **€2**; 5★ and 4★-superior hotels €4; 4★ and 3★-superior €3; 1-3★ €2; hostales, campings and albergues €1; a 75 % bonificación in low season (1 Nov–30 Apr; computed: €2 × 25 % = €0.50 for a vivienda turística) and 50 % off from the ninth night of a stay; under-16s exempt (Ley 2/2016 arts. 5 and 13, consolidated text last updated 17 May 2025; 2026-11-25 verified; source [BOE-A-2016-4175](https://www.boe.es/buscar/act.php?id=BOE-A-2016-4175#a13))

### Strategic notes

- **Mais Habitación / Ley de Vivienda 2023** declared zonas tensionadas allow rent caps
- **Cataluña + Baleares** = highest barriers; **Madrid** moderate; **Canarias** + **Andalucía** easier
- **Plusvalía + ITP at sale** eats long-term gains
- Wealth tax matters for high-value assets in Cataluña

---

## Section: `--work=<profession>`

### Job platforms

- **InfoJobs** (largest)
- **LinkedIn ES, Indeed.es, Tecnoempleo** (IT-focused)
- **SEPE (Servicio Público de Empleo Estatal)**: `https://www.sepe.es/`
- Profession-specific colegios profesionales (architects, doctors, lawyers)

### Self-employment

- **Autónomo regime**: monthly Seguridad Social minimum cuota **~€206–607** by income tramo (15 brackets, net ≤€670/mo → >€6,000/mo; computed: €653.59 × 31.50 % ≈ €205.88 at the lowest minimum base and €1,928.10 × 31.50 % ≈ €607.35 at the highest, where 28.30 % + 1.30 % + 0.90 % + 0.10 % + 0.90 % = 31.50 % for contingencias comunes, profesionales, cese de actividad, formación profesional and MEI) — voluntary higher bases allowed, so actual cuota can exceed €607 (2026 data, sources [Orden PJC/297/2026 art. 18](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7296) and [Seguridad Social RETA 2026](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537/36538?changeLanguage=es) — confirm at the importass simulator)
- **Tarifa plana** (cuota reducida, [Ley 20/2007 art. 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409)): a reduced quota for the first 12 full calendar months after an initial registration, or after 2 years without one, extendable 12 more months where net annual income stays below the SMI. **€80/mo** is the amount [Real Decreto-ley 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) fixed for 2023-2025, leaving later years to each Presupuestos law; [Real Decreto-ley 3/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548) records that no 2026 Presupuestos law was approved (the 2023 law is extended), and neither it nor Orden PJC/297/2026 sets a 2026 amount (2026-11-25 verified). A gestoría quotes the Seguridad Social's Importass guide as still applying €80 plus MEI, €88.64/mo in total, in 2026 (secondary, [Gestoría 24/7](https://gestoria247.com/blog/tarifa-plana-autonomos-2026); the Importass guide could not be read for verification on 2026-11-25 — check it directly at the importass simulator)
- **Sociedad Limitada (SL)**: min **€1 capital** since Ley 18/2022 "Crea y Crece" (in force Oct 2022; was €3,000 pre-reform). Creditor-protection conditions: 20 % of annual profits to legal reserve until reserve + capital reaches €3,000; shareholders jointly liable up to €3,000 in liquidation. (2026-05-27 verified; source [BOE Ley 18/2022](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-15818))
- **Trabajador por cuenta propia** straightforward

### Salary benchmarks (2025)

- Median monthly gross:
  - Madrid, Barcelona: ~€2,400-3,200 (est.; calibration: INE EAES 2024, published 28 May 2026, mean gross pay per worker — Comunidad de Madrid €34,410.01 ÷ 12 ≈ €2,867.50/mo, Cataluña €31,730.05 ÷ 12 ≈ €2,644.17/mo; the release gives no city figures and only a national median, €24,497.17 against a €29,540.26 mean (computed: 24,497.17 ÷ 29,540.26 ≈ 0.829); applied to these regional means, that ratio puts the medians below this band's floor (inference), so the band may run high; source [INE EAES 2024](https://www.ine.es/dyngs/Prensa/EAES2024.pdf))
  - Bilbao, Sevilla, Valencia: ~€1,900-2,500 (est.; calibration: INE EAES 2024 regional means — País Vasco €35,170.28 ÷ 12 ≈ €2,930.86/mo, the highest in Spain; Andalucía €26,089.70 ÷ 12 ≈ €2,174.14/mo; Comunitat Valenciana €26,816.98 ÷ 12 ≈ €2,234.75/mo; applied to these means, the 0.829 national median/mean ratio above puts País Vasco near the top of this band and Andalucía and the Comunitat Valenciana near or below its floor (inference))
  - Smaller cities: ~€1,600-2,000 (est.; calibration: INE EAES 2024 national median €24,497.17 ÷ 12 ≈ €2,041.43/mo and national mean €29,540.26 ÷ 12 ≈ €2,461.69/mo; lowest regional mean Extremadura €24,979.44 ÷ 12 ≈ €2,081.62/mo, and €2,081.62 × 0.829 ≈ €1,726 scaled by the national median/mean ratio (inference))
- **SMI (Salario Mínimo Interprofesional) 2026**: €1,221/mo (14 payments) = €17,094/yr (RD 126/2026, BOE-A-2026-3815, 18 Feb 2026; +3.1 % vs 2025; 2026-07-03 verified)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SNCZI / SNZI Sistema Nacional de Cartografía de Zonas Inundables** | `https://sig.mapama.es/snczi/` | Flood hazard maps Q10/Q100/Q500 |
| **MITECO Riesgos Naturales** | `https://www.miteco.gob.es/` | Aggregated environmental risks |
| **IGN (Instituto Geográfico Nacional) Sismicidad** | `https://www.ign.es/web/ign/portal/sis-area-sismicidad` | Earthquake hazard, real-time |
| **CSN (Consejo de Seguridad Nuclear) radón** | `https://www.csn.es/radon` | Radon maps |
| **AEMET** (national meteorology): `https://www.aemet.es/` | Climate + storm |
| **CCAA cartas de riesgos naturales** | per CCAA | Flood + landslide + fire |
| **CASIAS / Suelos Contaminados** | per CCAA | Brownfield contamination |
| **DGSCM (Protección Civil)** | `https://www.proteccioncivil.es/` | Emergency planning |

### Specific risks

- **Inundación / DANA (gota fría)**: Mediterranean coast, Costa del Sol, Valencia (2024 disaster), Barcelona; increasing flash floods
- **Incendios forestales**: huge concern Galicia, Asturias, Cataluña, Castilla-La Mancha, Andalucía interior
- **Sismo**: moderate-high Andalucía + Murcia (Lorca 2011 M 5.1 reminder); Cordillera Bética; Pirineos minor
- **Sequía**: Mediterranean Cataluña + Andalucía + Castilla — water restrictions
- **Aluminosis** (Spain-specific concrete failure): 1960s-1970s buildings esp. Cataluña/Tarragona — catastrophic
- **Costas**: 100m strip restriction (Ley de Costas 1988)
- **Volcán** (volcanic risk): Canarias only — La Palma 2021 Cumbre Vieja eruption

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1957** | Lead pipes, asbestos, weak structures |
| **1957–1981 ASCE pre-NCSE** | No seismic standards; AlumiNOSIS major risk in CAT/Tarragona |
| **1981–2003** | Improved standards; some asbestos |
| **2003–2007** | NCSE-02 + CTE (Código Técnico de Edificación 2006) |
| **Post-2007** | Modern energy + seismic; CTE 2019 nZEB |

**Aluminosis crisis**: Cataluña had massive failures in 1960s-70s buildings due to high-alumina cement (cemento aluminoso); structural collapse risk. **Specific to verify in Tarragona, Barcelona, Lleida properties pre-1980**.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Cédula de Habitabilidad** | All sales (varies by CCAA strictness) | 5–25 years per CCAA |
| **Certificado Energético (CEE)** | All sales | 10 years (5 years for a G rating); fines €300-600 leve, €601-1,000 grave, €1,001-6,000 muy grave, or the profit gained where that is higher (2026-11-25 verified; sources [RD 390/2021 art. 13](https://www.boe.es/buscar/act.php?id=BOE-A-2021-9176), [TRLSRU DA 12ª-13ª](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11723)) |
| **ITE (Inspección Técnica de Edificios)** | Buildings >50 yrs in many CCAA (45-50 in Cataluña, Madrid, Valencia) | 10 yrs |
| **Nota simple Registro de la Propiedad** | All sales | At sale |
| **Recibo IBI** + **certificado de ayuntamiento** | At sale | At sale |
| **Estatutos de comunidad de propietarios** | If condo | At sale |
| **Liquidación de gastos** (community fees) | If condo | At sale |

### Climate change projections (AEMET / CCAA)

- +1.5–4.5 °C by 2050 (RCP scenarios)
- Drought intensifying (south + east)
- Heat waves: longer, more lethal
- Extreme rainfall: DANA events more frequent
- Wildfires: Iberian peninsula at major risk
- Sea-level rise: Mediterranean + Cantábrico coasts

---

## Section: `--mains`

### Sources

- Each ayuntamiento or mancomunidad runs water + sewer
- Major: **Canal de Isabel II** (Madrid), **Aigües de Barcelona**, **Hidráulica de Cantabria**, **EMASESA** (Sevilla), **EMVISESA**, **EMASA Málaga**
- Universal in cities; rural Galicia, Aragón, Castilla often on pozo + fosa séptica

### Costs (est. ranges — get local quotes)

| Scenario | Cost (€) |
|---|---:|
| Acometida (mains connection) | 1,500–4,000 |
| Septic to mains | 5,000–15,000 |
| Fosa séptica (modern) | 4,000–10,000 |
| Pozo de agua (well drill) | 3,000–8,000 |

---

## Cost benchmarks (ES 2026)

| Work | Cost (€) |
|---|---:|
| Cédula de habitabilidad | 100–300 |
| Certificado Energético | 100–250 |
| ITE | 300–800 |
| Notario | 600–1,500 |
| Registro de la Propiedad | 200–800 |
| **Total transaction cost (resale)** | **~6–14 %** of price, est. (ITP 6–13 % + notary and registry; see `--tax`) |
| **Total transaction cost (new build)** | **~11–12.5 %** est. (10 % IVA + AJD + notary and registry; see `--tax`) |
| Aluminosis remediation (small house) | 30,000–100,000 |
| Septic to mains | 5,000–15,000 |
| Roof tile (200 m² teja árabe) | 8,000–18,000 |
| Energy retrofit (Class C → A) | 25,000–60,000 |
| Antiseismic retrofit | 20,000–60,000 |

## Active fiscal incentives (2026)

- **Plan Reno** energy retrofit: up to 60 % grants (Next Generation EU funds)
- **Deducciones IRPF for retrofit**: 20-60 % rebate over 5 yrs depending on energy class jump
- **MOVES Plan III**: heat pump + renewable heating
- **Ley de Vivienda 2023**: incentives in zonas tensionadas (long-let)
- **TU CASA** (Real Decreto-ley 29/2026, convalidated 12 Nov 2026): 0 % ICO loans for a first mortgaged habitual home, for the lower of 20 % of value or €50,000 (€10,000M extraordinary credit); the home carries a permanent CPI-linked maximum resale price; beneficiaries and limits are still to be set by Acuerdo de Consejo de Ministros (2026-10-21 verified)
- **Plan Estatal de Vivienda 2026-2030** (RD 326/2026, de 22 de abril, BOE-A-2026-8872): active state housing-aid framework (grants/rebates), in force 24 Apr 2026 (BOE 23 Apr 2026); first state plan under Ley 12/2023; 40 % of total allocation made available to CCAA for public/protected/affordable housing supply, mainly rental; €7,000M total, 60 % State / 40 % CCAA co-financing (2026-10-21 verified)

## Common listing platforms

- **Idealista** — biggest, full extraction
- **Fotocasa, Habitaclia, Pisos.com** — standard
- **Engel & Völkers, Sotheby's, Lucas Fox** — premium
- **Wallapop, Milanuncios** — privates

## Caveats unique to ES

- **Aluminosis** (Cataluña 1960s-70s): catastrophic concrete failure risk — verify with structural engineer
- **Costas Law 100m strip**: coastal restrictions on building/extending
- **Plusvalía municipal** still in legal evolution post-2021 ruling
- **Wealth tax** depends massively on CCAA — Madrid/Andalucía effectively zero, Cataluña/Valencia high
- **Cataluña ITP scale steepened 27 Jun 2025** (was already 10 %/11 % two-bracket) — affects high-value Barcelona purchases; top bracket 13 % >€1.5M + 20 % flat for grans tenidors (Decret-llei 5/2025)
- **Golden Visa abolished** by Ley Orgánica 1/2025 (3 Apr 2025) — the Ley 14/2013 art. 63 real-estate residency route is closed to new applicants (2026-05-27 verified; cross-ref `shared/visa-programs.md` ENDED registry)
- **VPO (vivienda protegida)** — subsidized housing, restrictions on resale
- **Cooperative housing (cooperativas)** — common form, specific rules
- **NIE/NIF** required for non-residents to buy
- **Pueblos rurales depopulating** — resale liquidity weak
- **Cédula de Habitabilidad** without it some purchases blocked (Cataluña strict)
- **Gota fría / DANA** (cold drop) flood events Mediterranean coast
- **Catastro vs Registro** mismatch common — verify both before buying
- **Cooperativa de viviendas** + **comunidad de propietarios** require diligence on financial state

## Reddit / forum sources

- **r/Spain**, **r/AskSpain**, **r/Madrid**, **r/Barcelona**, **r/Valencia**
- **r/SpainAuxiliares** (expat teaching)
- **InvertirEnLaBolsa** + **Rankia** (financial)
- **Idealista news** + comments
- **Real Estate Spain Telegram groups**
- Expat: **The Local Spain**, **Sur in English**, **Olive Press**

## Verification authorities

| Authority | When to call |
|---|---|
| **Catastro Sede Electrónica** | Cadastral verification — FREE |
| **Registro de la Propiedad** | Title verification (paid) |
| **Ayuntamiento Urbanismo** | Permits, planning, plusvalía |
| **Notario** | Final transfer, escrow |
| **Suministros** (gas/agua/luz) | Contracts after purchase |
| **Comunidad de propietarios** | If condo: gastos, deudas, derramas |
| **AEAT (Agencia Tributaria)** | IRPF/IRNR rules |

## Source URL templates

| Source | URL pattern |
|---|---|
| Catastro Sede Electrónica | `https://www.sedecatastro.gob.es/` |
| Idealista | `https://www.idealista.com/<provincia>/<municipio>/` |
| INE Vivienda | `https://www.ine.es/dynt3/inebase/es/index.htm?padre=2942` |
| SNCZI flood | `https://sig.mapama.es/snczi/` |
| IGN seismic | `https://www.ign.es/web/ign/portal/sis-area-sismicidad` |
| CSN radón | `https://www.csn.es/radon` |
| AEMET clima | `https://www.aemet.es/` |
| Registradores | `https://www.registradores.org/` |
| AEAT | `https://www.agenciatributaria.es/` |

## Status

✅ Fast-changing sections re-verified as of 2026-11-25; each section's date is in the Per-section verification table.

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-08-07 (Cataluña IEET tourist-tax tariff schedule re-verified against ATC — Llei 2/2026 rates in force 1 Apr 2026; prior Tier-A quarterly refresh 2026-07-03 — fast-moving claims re-verified; structural sections unchanged). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Rental / tax / visa tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Cataluña IEET municipal recàrrecs outside Barcelona (in force 1 Oct 2026) re-verified against ATC 2026-10-23; RDL 28/2026 + RDL 29/2026 housing decrees (BOE read 2026-10-21; on 12 Nov 2026 RDL 29/2026 convalidated and RDL 28/2026 derogated, BOE read 2026-11-13) and the 6 Oct 2026 lapse of Proposición de Ley 122/000196 carried into --tax / --rental (see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (Catastro free + comprehensive; SNCZI maintained). MEDIUM for short-let regulation (CCAA-specific, evolving — Cataluña tightening, Madrid moderate). HIGH for Cataluña 2025 ITP reform (27 Jun 2025 effective, Decret llei 5/2025).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-11-25 | 2026-11-25 maintenance run | INE IPV for Q2 2026 (published 7 Sep 2026): prices +12.2 % year on year, resale +12.9 %, new +7.4 %. The 0.50 market-reference coefficient behind the valor catastral was re-checked in the BOE (Orden EHA/1213/2005, citing the Orden of 14 Oct 1998). |
| `--tax` | 2026-11-25 | 2026-11-25 maintenance run | IBI bands and the tourist-let surcharge match TRLRHL art. 72 on BOE; ITP, AJD and regional wealth-tax rates were checked against the Ministerio de Hacienda's Tributación Autonómica 2026, which corrected Aragón, Asturias, Cantabria, Murcia, Baleares and Extremadura, plus the Bizkaia, Navarra, Catalan, Valencian and Ceuta-Melilla legislation. Non-resident rates, IVA and imputed income match TRLIRNR, LIVA, IRPF art. 85 and Real Decreto-ley 29/2026, and notary, registry and total-cost shares are now estimates calibrated on the national aranceles. |
| `--rental` | 2026-11-25 | 2026-11-25 maintenance run | Real Decreto-ley 29/2026 and its 12 Nov 2026 convalidation were re-checked in the BOE; the IRPF rental reduction now follows the LIRPF art. 23.2 scale it introduced, with older leases on the 60 % or 2023 scales (AEAT manual). IRNR rates and the expense rule (TRLIRNR), the Balearic tourist tax (Ley 2/2016) and the Barcelona HUT phase-out (Ajuntament release, Decret llei 3/2023, STC 64/2025) were checked; the 6-18 month eviction duration is a practitioner estimate. |
| `--work=<profession>` | 2026-11-25 | 2026-11-25 maintenance run | Autónomo minimum quotas recomputed from Orden PJC/297/2026 and the Seguridad Social 2026 rates; the 2026 SMI (RD 126/2026) and the SL €1 minimum capital (Ley 18/2022) re-checked in the BOE. The €80 tarifa plana for 2026 rests on a secondary report, and city salary bands are estimates calibrated against INE EAES 2024 regional means. |
| `--risks` | 2026-11-25 | 2026-11-25 maintenance run | Energy certificate validity (10 years, 5 for a G rating; RD 390/2021) and the €300-6,000 fine bands (TRLSRU) re-checked in the BOE. |
| `--mains` | 2026-11-25 | 2026-11-25 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (ES 2026) | 2026-11-25 | 2026-11-25 maintenance run | Total transaction cost rows are now estimates built from 2026 ITP, IVA and AJD rates (Ministerio de Hacienda, LIVA) plus notary and registry fees from the national aranceles. |

## Extension TODOs

- [ ] Per-CCAA wealth tax + ITP rate tables (deeper)
- [ ] Per-municipio plusvalía methodology
- [ ] VTV/VFT per CCAA licensing decision tree
- [ ] Aluminosis detection workflow (Cataluña/Tarragona pre-1980)
- [ ] Costas 100m strip parcel-level lookup
- [ ] Zonas tensionadas tracking (Mais Habitação areas)
- [ ] La Palma volcanic zone (Canarias) overlay
- [ ] Cooperativa housing red-flag detection

## Update history

- **2026-11-25** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (ES 2026). Playbook-level date now 2026-11-25.
