# Argentina 🇦🇷 — Property Due-Diligence Playbook

ISO2: `ar`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CPA)**: 4 digits + letter prefix + 3 chars (`C1414BFE` Buenos Aires, `M5500AAB` Mendoza, `R8400CBO` Bariloche)
- **Admin levels**: 23 provincias + CABA (Ciudad Autónoma de Buenos Aires) + more than 2,300 gobiernos locales — municipios, comunas, comisiones de fomento etc., whose form and autonomy vary by province (2026 data, source Ministerio del Interior ReFeGLo `https://gobiernoslocales.mininterior.gob.ar/`; IGN ANIDA counted 2,273 in 2017)
- **Currency**: **ARS** (Argentine peso) + **USD billete** (real-estate market is USD-denominated)
- **Languages**: Spanish (de facto)
- **Cadastre — provincial fragmentation**:
  - **Registro de la Propiedad Inmueble** per province (CABA + 23 provinces)
  - **Catastro** also provincial (e.g., **ARBA** in PBA, **ATM** Mendoza)
  - **ARCA (ex-AFIP) — Agencia de Recaudación y Control Aduanero** (created by **Decreto 953/2024**, which dissolved AFIP — issued 2024-10-24, B.O. 2024-10-25, in force the day it was issued per art. 12; art. 6 makes ARCA the legal successor keeping AFIP's responsibilities, competencies + functions; source ARCA Biblioteca Electrónica `https://biblioteca.afip.gob.ar/dcp/DEC_C_000953_2024_10_24`) — federal tax integration via CDI/CUIT for foreigners. `afip.gob.ar` and `arca.gob.ar` both resolve (2026-10-23 verified).
- **Identifier**: matrícula (per provincial registry)
- **Escribano público (notary)** — buyer-chosen and **mandatory**; pulls certificado de dominio + inhibiciones
- **Ownership types**: dominio pleno (freehold); usufructo; condominio; PH (propiedad horizontal — apartments)

## Section: `--price`

### Primary sources

- **INDEC** (national stats): `https://www.indec.gob.ar/` — limited housing detail due to currency volatility
- **Reporte Inmobiliario** monthly market reports
- **Banco Nación + BCRA** for new mortgage data (mortgages restarted 2024)
- **TheLatinvestor** aggregated data

### Listing platforms

- **Zonaprop** — DOMINANT national portal: `https://www.zonaprop.com.ar`
- **Argenprop**: `https://www.argenprop.com`
- **MercadoLibre Inmuebles**: `https://inmuebles.mercadolibre.com.ar`
- **Inmoclick** (regional): `https://inmoclick.com` (legacy `www.inmoclick.com.ar` redirects there, 2026-10-23)
- **Reporteinmobiliario.com** — market data

**USD vs ARS**: Sale listings overwhelmingly in **USD billete**; rentals in ARS but with USD/CER/UVA adjustment clauses now allowed post-DNU.

### 2026 price benchmarks (Zonaprop Index / Índice M² Real / TuLugar / TheLatinvestor)

| Region | USD/m² (typical) | Trend |
|---|---:|---|
| **CABA average — asking** (Zonaprop Index, apartments) | avg $2,484 (Sep 2026) | +1.4% YTD 2026; 11.3% below series peak |
| **CABA average — closing** (Índice M² Real: RE/MAX + UCEMA + Reporte Inmobiliario, used apartments) | $2,097 (Sep 2026) | −0.4% YoY; asking-to-closing gap −4.75% |
| **CABA Puerto Madero** | avg $6,165 (Sep 2026) | most expensive barrio |
| **CABA Palermo** | avg $3,454 (Sep 2026) | 2nd most expensive barrio |
| **CABA Recoleta** | $2,636–$2,837 (Sep 2026; ranked between Chacarita and Villa Ortúzar, exact value not labelled) | +2.0% YoY |
| **CABA Belgrano** | $2,837–$3,409 (Sep 2026; ranked between Núñez and Chacarita, exact value not labelled) | n/a |
| **CABA Caballito** | avg $2,428 (Sep 2026) | n/a |
| **Tigre municipio, incl. Nordelta** (GBA Norte) | avg $2,771 (Sep 2026) | +4.2% YoY |
| **Pilar municipio** (GBA Norte) | avg $1,940 (Sep 2026) | −0.7% YoY |
| **Mendoza city** | median $1,092 (TuLugar, Nov 2026); by sección $538–$2,179 | $1,091 Sep vs $1,118 Aug 2026; no YoY series |
| **Córdoba city** | avg $1,474 (Zonaprop, Mar 2026, latest quarterly); median $1,420 (TuLugar, Oct 2026) | +8.8% YoY USD to Mar 2026 |
| **Bariloche apartments** | portal medians $3,051–$3,398 (TuLugar $3,398 Sep 2026; TheLatinvestor Oct 2026 compilation: TuLugar $3,067, Roomix $3,051, PubliqueInmuebles $3,300) | n/a — thin, volatile samples |
| **Bariloche premium** (Carihue, Melipal, Villa Catedral, Arelauquen; lake-view Playa Bonita / Llao Llao / along Bustillo) | medians $3,571 (Arelauquen) – $4,060 (Carihue) (TuLugar via TheLatinvestor, Oct 2026); lake-view units ask est. $3,500–$6,500 (TheLatinvestor estimate from Zonaprop + Properati listings) | n/a |
| **Bariloche value** (Las Victorias, Dina Huapi, Ñireco, Alto Bariloche, El Frutillar) | medians Las Victorias $1,867 (Oct 2026), Dina Huapi $2,133 (Sep 2026); Ñireco / Alto Bariloche / El Frutillar ask est. $1,400–$2,600 (no portal median; TheLatinvestor estimate) | n/a |
| **Bariloche houses** | $1,482/m² (TuLugar, Oct 2026) vs about $2,000/m² built (TheLatinvestor, Oct 2026); 56% of all listings ask < $200k | n/a — sources disagree |
| **Mar del Plata** | median $1,902 (TuLugar, Oct 2026) | $1,901 Sep vs $1,912 Aug 2026; no YoY series |

Sources (2026 data): Zonaprop Index CABA + GBA Norte September 2026 reports and Córdoba Q1 2026 report (`https://www.zonaprop.com.ar/blog/zpindex`) — listing platform, asking prices, apartments; Índice M² Real September 2026 (`https://www.reporteinmobiliario.com/`) — closing prices from concluded sales; TuLugar market pages October–November 2026 (`https://tulugar.com/es/mercado/argentina/<city>`) — listing aggregator medians; TheLatinvestor Bariloche guides (updated October 2026; area medians quoted from TuLugar, lake-view and outer-barrio ranges are its own estimates from listings) — secondary aggregator. Asking prices are seller-controlled and run above closings (CABA gap −4.75%, Sep 2026). Barrio / municipio / city figures are area-level averages or medians, not a valuation of any specific parcel.

### Compute

1. USD/m² = price / **superficie cubierta** (covered area)
2. **USD-denominated**: most listings + transactions in USD billete
3. Cross-check **Zonaprop asking** against the **Índice M² Real** closing-price series (RE/MAX + UCEMA + Reporte Inmobiliario): CABA asking-to-closing gap −4.75% in Sep 2026 (2026 data, source Reporte Inmobiliario)
4. **CABA premium** (Zonaprop asking ranking, Sep 2026): Puerto Madero > Palermo > Núñez > Belgrano > Recoleta

### Key terms

- Matrícula = title identifier
- Escribano público = notary (mandatory + buyer-chosen)
- Certificado de dominio = title certificate
- Inhibiciones = encumbrances
- Boleto de compraventa = pre-escritura agreement
- COTI = former **ARCA (ex-AFIP)** pre-listing transfer code — ❌ ABOLISHED from 2025-05-23 (RG 5697/2025, B.O. 2025-05-23, abrogated RG 2371; source Colegio de Escribanos CABA `https://www.colegio-escribanos.org.ar/2025/05/23/eliminacion-del-coti-y-del-regimen-citi-escribanos-plazo-para-que-la-uif-adecue-su-normativa-contra-el-lavado-de-activos/`)

---

## Section: `--traffic`

### Sources

- **DNV (Dirección Nacional de Vialidad)**: `https://www.argentina.gob.ar/transporte/vialidad-nacional/` — still operating under Ministerio de Economía › Transporte (2026-10-23 verified); the dissolution ordered by Decreto 461/2025 was rejected under Ley 26.122 (Senado Res. 55/2025, B.O. 2025-08-25, source Infoleg; Diputados vote reported 2025-08-07, press-sourced). TMDA data: `https://www.argentina.gob.ar/transporte/vialidad-nacional/institucional/informacion-publica/tmda`
- **DPV provincial vialidad** (Vialidad Buenos Aires, etc.)
- **CABA Movilidad**: `https://buenosaires.gob.ar/movilidad` (redirects to the archived `gcaba_historico/movilidad-e-infraestructura/movilidad` path as of 2026-10-23)

### Key term

**TMDA (Tránsito Medio Diario Anual)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural Patagonia)
- 🟡 1,500–10,000 v/d (suburban arterial, provincial roads)
- 🟠 10,000–35,000 v/d (Buenos Aires arterials, RP-2, autopistas)
- 🔴 > 35,000 v/d (General Paz, Panamericana, 9 de Julio, Riccheri)

---

## Section: `--tax`

### Annual property tax — Impuesto Inmobiliario

**Provincial — varies by province:**

| Province | Rate (annual on fiscal value) |
|---|---:|
| CABA (Inmobiliario + ABL) | Inmobiliario 0.60–1.20% marginal scale on Valuación Fiscal Homogénea + ABL tasa 0.80% × (1 + 0.5 × barrio coefficient 0.00–2.00) = 0.80–1.60% (computed); each 2026 instalment capped at the previous one + IPCBA (2026 data, source CABA Ley 6927 Anexo arts. 41–44) |
| PBA (urbano edificado) | 0.028–2.363% marginal scale on fiscal valuation; 2026 increase over the 2025 tax capped by the IPC GBA variation Feb 2024–Nov 2025 (2026 data, source PBA Ley 15.558 art. 6) |
| Mendoza (urbano e interfaz) | 0.70–1.70% marginal scale on avalúo fiscal, minimum ARS 43,645 (2026 data, source Mendoza Ley 9680 art. 2) |
| Córdoba (urbano edificado) | 0.156–0.850% marginal scale on base imponible (2026 data, source Córdoba Ley 11.090 art. 6) |

- Fiscal value typically below market (similar to LatAm)
- Annual or quarterly installments
- Scales are province-wide; a property's bill depends on its own partida valuation — verify on the partida's AGIP / ARBA / ATM / Rentas Córdoba account

### Transaction taxes

#### Sellos (stamp duty) — provincial

| Province | Rate |
|---|---:|
| CABA | 3.5%; 2.7% when the price, Valuación Fiscal Homogénea or VIR (whichever is highest) is ≤ ARS 226,100,000; vivienda única familiar exempt up to ARS 226,100,000, 3.5% on the excess (2026 data, source CABA Ley 6927 Anexo arts. 34 + 37) |
| PBA | 2.0% (20‰) on deeds transferring dominio; vivienda única exemption keyed to fiscal valuation ≤ ARS 1,154,400 (2026 data, source PBA Ley 15.558 arts. 39 + 43; exemption reading per Colegio de Escribanos CABA 2025-12-18) |
| Mendoza | 2.0% on acts over inmuebles in 2026, set at 1.75% for 2027 (2026 data, source Mendoza Ley 9680 art. 7 b) |
| Córdoba | 1.0% (10‰) on deeds transferring dominio; 0.70% (7‰) when registered through the Registro General's digital channels (2026 data, source Córdoba Ley 11.090 art. 45 pts 8.2 + 5.2) |

- Who bears sellos is agreed between the parties; a 50/50 buyer-seller split is customary in CABA and PBA (secondary: notarial and broker guides, 2026) — confirm in the boleto

#### ITI (Impuesto a la Transferencia de Inmuebles) — **DEROGATED 2024-07-08**

- **REPEALED by Ley 27.743 (Medidas Fiscales Paliativas y Relevantes), Título IV art. 67**, in force from B.O. publication **8 Jul 2024**. The 1.5% transfer tax **no longer applies** to any property transfer regardless of acquisition date (2026-10-23 verified against the Ley 27.743 text in the ARCA library — art. 67 sits in Título IV and takes effect on B.O. publication; earlier sources ARCA novedad 3808 + Colegio Escribanos PBA Ficha #01 2024-09-16 + argentina.gob.ar).
- **Capital gains 15% (cedular Impuesto a las Ganancias)** applied to inmuebles acquired from 2018-01-01 and sold up to 2025-12-31; sales by individuals from **2026-01-01 are exempt** (Ley 27.802 art. 192 — see Capital gains below). Pre-2018 acquisitions transferred after 2024-07-08 owe no federal transfer tax.
- COTI (Código de Oferta de Transferencia de Inmuebles) **ABROGATED** by ARCA RG 5697/2025 (B.O. 2025-05-23, in force on publication) — see COTI below.

### Bienes Personales (wealth tax) — current 2026 schedule (Ley 27.743 + IPC-indexed thresholds)

**Per ARCA, FY 2025 (filed 2026)** (amounts IPC-indexed each year; FY 2026 amounts not yet shown on ARCA's Bienes Personales pages as of 2026-10-23):
- **Mínimo no imponible (non-taxable threshold)**: **ARS 384,728,044.57** (≈ USD 252k, computed at the BCRA wholesale reference rate, Com. A 3500, of ARS 1,527.85/USD on 2026-10-22)
- **Casa-habitación exemption (primary residence)**: **ARS 1,346,548,155.99** (≈ USD 881k at the same rate)
- **Rate schedule (FY 2025 filed 2026)** — three tramos on assets above the mínimo; cumplidores (compliant taxpayers) get 0.50 points off for FY2023–2025 (Ley 27.743 art. 64):
  - Up to ARS 52,664,283.73: **0.50%** general / **0%** cumplidores
  - ARS 52,664,283.73–114,105,948.16: **0.75%** general / **0.25%** cumplidores
  - Above ARS 114,105,948.16: **1.00%** general / **0.50%** cumplidores
  - **Top bracket steps down every fiscal year** under **Ley 27.743 art. 63** (B.O. 2024-07-08), which rewrote art. 25 of Ley 23.966: FY2023 **0.50–1.50%** → FY2024 **0.50–1.25%** → FY2025 **0.50–1.00%** → FY2026 **0.50–0.75%** → flat **0.25%** from FY2027. The FY2025 scale declared in 2026 therefore tops out at **1.00%** (2026-10-23 verified, source [Ley 27.743 texto](https://biblioteca.afip.gob.ar/dcp/LEY_C_027743_2024_06_27) art. 25 items a–e + ARCA alícuotas FY2025 scale).
- **Foreign-asset surcharge eliminated retroactively to FY 2023** by Ley 27.743 (sanctioned June 2024) — unified schedule for foreign + domestic assets
- **REIBP (Régimen Especial de Ingreso del Impuesto sobre los Bienes Personales, Ley 27.743 Título III)** — one-off prepayment covering FY2023–2027: individuals paid **0.45%** on the FY2023 base × 5 (arts. 50 + 52); adhesion window to 31 Jul 2024, extendable by the Executive to 30 Sep 2024 (art. 48); regime runs to 31 Dec 2027 (art. 45)
- **Cash at the deed** — Ley 27.826 (B.O. 2026-10-09): taxpayers on the simplified Ganancias return must route operations through BCRA/CNV-authorised channels; cash paid at an escritura that constitutes, modifies, declares or extinguishes real rights on inmuebles counts as compliant, and for Bienes Personales those funds count as incorporated into the estate on the day of the operation (2026 data, source B.O. Ley 27.826)

(2026-10-23 verified, source [ARCA alícuotas](https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/alicuotas.asp) for the FY2025 scales + [ARCA ¿Qué es?](https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/que-es.asp) for the FY2025 mínimo and casa-habitación amounts + [Ley 27.743 texto](https://biblioteca.afip.gob.ar/dcp/LEY_C_027743_2024_06_27) for REIBP.)

### Capital gains

- **Individuals exempt for sales from 2026-01-01**: Ley 27.802 (Modernización Laboral, B.O. 2026-03-06) art. 192 rewrote Ganancias art. 26 inc. n) to exempt the result of selling inmuebles, or transferring rights over them, covered by art. 99 when the sale or transfer takes place from 2026-01-01; Decreto 406/2026 (B.O. 2026-06-01) applies it to personas humanas and sucesiones indivisas resident in Argentina or abroad, including cession of a boleto without possession (2026 data, source [Ley 27.802 texto](https://www.argentina.gob.ar/normativa/nacional/norma-423680/texto) + [Decreto 406/2026](https://biblioteca.afip.gob.ar/dcp/DEC_C_000406_2026_05_29)).
- **Sales up to 2025-12-31** of inmuebles acquired from 2018-01-01: **15%** cedular rate (Ganancias art. 99) on price minus inflation-indexed acquisition cost minus related expenses; the casa habitación sale was exempt under the former art. 26 inc. n).
- The exemption reaches only results covered by art. 99; companies and habitual real-estate dealing stay taxable (secondary: Reporte Inmobiliario 2026-03-04).

### Capital-gains rate for non-residents

- **Sales from 2026-01-01**: exempt for non-resident individuals and sucesiones indivisas (Decreto 406/2026).
- **Sales up to 2025-12-31**: **15%** on the art. 99 net gain, deducting only expenses incurred in Argentina; a resident buyer withholds it as pago único y definitivo, and when both parties are non-resident the seller pays directly (Decreto 862/2019 art. 258) — verify per transaction with the escribano.

### COTI

**COTI ABROGATED**: ARCA RG 5697/2025 art. 1 abrogated RG 2371 (COTI) together with RGs 2415, 2439, 2506 and 3101, in force from B.O. publication on 2025-05-23 (art. 3); no COTI is needed to list, offer or deed a property (2025 data, source [argentina.gob.ar RG 5697/2025](https://www.argentina.gob.ar/normativa/nacional/norma-413101/texto)).

### Total transaction cost (buyer side) — post-ITI repeal

Computed with the 2026 sellos rates above, assuming a 50/50 sellos split (custom in CABA and PBA, not law), est. ~1–2% escribano and est. ~0.5–1% other (certificates, registry); broker commission excluded:
- CABA: **est. ~2.85–4.75%** (1.35% or 1.75% sellos half-share at the 2.7% / 3.5% rate + 1–2% + 0.5–1%); **est. ~1.5–3%** for an exempt vivienda única up to ARS 226,100,000 (≈ USD 148k at ARS 1,527.85/USD)
- PBA: **est. ~2.5–4%** (1.0% sellos half-share + 1–2% + 0.5–1%)
- Mendoza: **est. ~2.5–4%** (1.0% sellos half-share + 1–2% + 0.5–1%)
- Córdoba: **est. ~2–3.5%** (0.5% sellos half-share + 1–2% + 0.5–1%)
- No federal transfer or capital-gains tax on individuals' sales from 2026-01-01 (ITI repealed 2024-07-08; cedular exempt from 2026-01-01)

---

## Section: `--rental`

### Long-term residential — DNU 70/2023 LIBERALIZED

**MAJOR REFORM**:
- **DNU 70/2023 (Milei, B.O. 2023-12-21, in force from 2023-12-29)** repealed Ley 27.551
- **NOT ratified by Congress — the regime still rests on the DNU.** Ley Bases (Ley 27.742, B.O. 2024-07-08) contains no residential-lease chapter and does not ratify DNU 70/2023 (InfoLEG text `https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401266/norma.htm`, checked 2026-10-23). The Senate rejected the DNU on 2024-03-14 (42–25–4); under Ley 26.122 it stays in force unless Diputados also rejects it — the 2026-10-15 Diputados special session to reject it failed for lack of quorum (121 present, 129 needed) (2026 data, source Bacap Noticias / Infobae — secondary press). A future Diputados rejection could change the rules for new contracts — check status before signing.
- New contracts: **free duration, free currency** (USD/UVA/CER/IPC), **free deposit**
- **Pre-existing Ley 27.551 contracts** continue under Ley 27.551 — only new contracts post-DNU use the new liberalized regime (grandfathering, CCyC art. 7); the last 3-year contracts signed before 2023-12-29 run out by end-2026 (computed: signing date + 3 years) (2026-10-23 verified, source Chequeado).
- **Pending, not law**: *Ley de Inviolabilidad de la Propiedad Privada* — Senate half-sanction, then approved with changes by Diputados 2026-10-21 (124–119–6) and returned to the Senate; for residential leases it would require a formal payment demand giving at least 10 calendar days to pay, then an eviction action processed within 10 further business days (2026 data, source Infobae / La Nación — secondary press). Check its status before relying on it.

### Short-let

- **CABA**: stays of 1 night to 3 months in residential units require free, digital registration in the Registro de Propiedades de Alquileres Temporarios Turísticos — Ley 6255 (BOCBA 2019-12-26, in force 2020-12-01, abrogated Ley 4632; Ley 4631 is the separate hotel-lodging law); authority Ente de Turismo (Res. 138-ENTUR/20); the registration number must appear in every listing and booking. Non-resident tourists pay the **Derecho de Uso Urbano** (Ley 6278, Res. 6/AGIP/2025), collected by the platform or the owner (2026 data, source CEDOM `https://www.cedom.gob.ar/legislacion/normas/leyes/RepoLeyes/ley6255.html` + `https://turismo.buenosaires.gob.ar/es/alquileres-temporarios`)
- **DNU 70/2023** liberalized the rental market — landlord-favorable (not ratified by Congress; see above)

### Tax on rental

- **Residential lets — Ganancias exemption from 2026**: rent that a persona humana or sucesión indivisa earns as landlord from a home let as the tenant's casa-habitación (single, family, permanent dwelling) is exempt from Impuesto a las Ganancias for gains accruing from 2026-01-01, whatever the contract date (2026 data, source Ley 27.802 art. 192, which replaced LIG art. 26 inc. n, + Decreto 406/2026 art. 1, new DR art. 83 — ARCA Biblioteca Electrónica `https://biblioteca.afip.gob.ar/dcp/LEY_C_027802_2026_02_27` + `https://biblioteca.afip.gob.ar/dcp/DEC_C_000406_2026_05_29`, checked 2026-11-03). The decree sets no residence condition; that non-resident landlords are covered is stated by legal commentary (secondary: Abeledo Gottheil on Decreto 406/2026). Companies are outside it, and a tourist stay is not the tenant's permanent dwelling under the DR art. 83 definition — verify per contract with a contador; the lines below apply to rent outside the exemption
- Residents: progressive income tax on rent outside the exemption
- Non-residents: **21%** final withholding on gross rent — computed: 60% presumed net income (LIG art. 104 inc. g) × 35% (art. 103) (2026 data, source ARCA Biblioteca Electrónica, LIG t.o. 2019 `https://biblioteca.afip.gob.ar/dcp/LEY_C_020628_2019_12_05`)
- Currency: ARS or USD (depending on contract)

---

## Section: `--work=<profession>`

### Sources

- **Bumeran** — national job board: `https://www.bumeran.com.ar`
- **ZonaJobs**, **Computrabajo**, **LinkedIn AR**, **Indeed.com.ar**
- **Secretaría de Trabajo, Empleo y Seguridad Social** (Ministerio de Capital Humano; ex-Ministerio de Trabajo): `https://www.argentina.gob.ar/capital-humano/trabajo` (old `/trabajo` path redirects there, 2026-10-23); labour statistics (SIPA, OEDE): `https://www.argentina.gob.ar/trabajo/estadisticas`

### Self-employment

- **Monotributo** simplified regime — cap (category K, highest) **ARS 126,610,838.75/year** from 2026-08-01 (+16.8% IPC re-indexation for H1 2026; the Feb–Jul 2026 cap was ARS 108,357,084.05); category A ceiling ARS 12,009,410.45; semestral indexation (Feb/Aug) by ARCA (2026 data, source ARCA `https://www.arca.gob.ar/monotributo/categorias.asp`)
- **Responsable Inscripto** for higher revenue + IVA registration
- **IIBB** provincial gross-receipts tax

### Salary benchmarks (2026)

- Registered private-sector employees, gross monthly — national **median ARS 1,689,227**, mean ARS 2,256,861 (July 2026); ≈ USD 1,140 / 1,520 at the BCRA reference rate of ARS 1,485/USD on 2026-07-31 (2026 data, source Secretaría de Trabajo SIPA report Jul 2026 + BCRA)
- Mean gross by province of employment (May 2026; the June figure includes the aguinaldo): CABA ARS 2,565,444 (≈ USD 1,820); Córdoba province ARS 1,809,788 (≈ USD 1,285); Mendoza province ARS 1,728,036 (≈ USD 1,230), at BCRA ARS 1,408/USD on 2026-05-29 (2026 data, source OEDE provincial wage series `https://www.argentina.gob.ar/trabajo/estadisticas/oede-estadisticas-provinciales`). These are provincial means, not city medians; nationally the mean runs 34% above the median.
- **Salario Mínimo Vital y Móvil**: **ARS 391,200/month** from 2026-10-01 (Resolución 4/2026, Consejo Nacional del Empleo, la Productividad y el SMVM, B.O. 2026-09-02) — cronograma: Sep ARS 383,800, Oct ARS 391,200, Nov ARS 398,800, Dic ARS 406,400; the schedule runs to April 2027 (2026 data, source Boletín Oficial + `https://www.argentina.gob.ar/trabajo/consejodelsalario`).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **INPRES (Instituto Nacional de Prevención Sísmica)** — merged into SEGEMAR by Decreto 396/2025 (B.O. 2025-06-18) | `https://www.inpres.gob.ar/` | Seismic monitoring + INPRES-CIRSOC 103 building code + seismic-zone lookup by coordinates |
| **SEGEMAR** | `https://www.argentina.gob.ar/economia/segemar` (legacy `www.segemar.gov.ar` fails over HTTPS and HTTP-redirects here, 2026-10-23) | Geology + geohazards; performs INPRES functions since Decreto 396/2025 |
| **OAVV — Observatorio Argentino de Vigilancia Volcánica (SEGEMAR)** | `https://oavv.segemar.gob.ar/` | Volcanic alerts; monitors Copahue, Domuyo, Laguna del Maule, Lanín, Maipo, Planchón-Peteroa, San José, Tromen, Tupungatito, Isla Decepción; 2024 volcanic-risk ranking |
| **OVDAS Chile** (cross-border Patagonia) | — | Volcanic monitoring |
| **SMN (Servicio Meteorológico Nacional)** | `https://www.smn.gob.ar/` (could not be read for verification on 2026-11-04 — check it directly; institutional page `https://www.argentina.gob.ar/smn`) | Weather, climate |
| **INA (Instituto Nacional del Agua)** — an organizational unit of the Secretaría de Obras Públicas since Decreto 396/2025 | `https://www.argentina.gob.ar/ina` (legacy `www.ina.gob.ar` redirects here) | Hydrology, flood; Alerta Hidrológico Cuenca del Plata |

### Specific risks

#### Earthquake — significant

- **INPRES seismic zones** 0-4: 0 muy reducida · 1 reducida · 2 moderada · 3 elevada · 4 muy elevada (Reglamento INPRES-CIRSOC 103 Parte I, July 2018 edition, Tabla 2.1). Zones are assigned per department in its Anexo A — department level, not parcel level, so check the exact site with INPRES's coordinate lookup
- **Zone 4 (muy elevada)**: Mendoza's Capital, Godoy Cruz, Guaymallén, Las Heras, Luján de Cuyo, Maipú, San Martín, Junín and part of Lavalle; every San Juan department except Iglesia, Jáchal and Valle Fértil, with Caucete split between Zones 3 and 4 (2018 data, source INPRES-CIRSOC 103 Anexo A) — rates/figures may have changed since
- **Zone 3 (elevada)**: Mendoza's Tupungato, Tunuyán, San Carlos, Rivadavia, Santa Rosa + parts of San Rafael, La Paz, Lavalle; San Juan's Iglesia, Jáchal, Valle Fértil; western La Rioja (Gral. Sarmiento, Gral. Lamadrid, Gral. Lavalle); Salta capital, Cerrillos, Chicoana, Metán; Jujuy capital, El Carmen, San Pedro, Ledesma, Tilcara; parts of Río Grande and Ushuaia (2018 data, source INPRES-CIRSOC 103 Anexo A) — rates/figures may have changed since
- **Zone 2 (moderada)**: La Rioja capital + Chilecito; all of Catamarca and Tucumán; Bariloche; Neuquén's Lácar and Los Lagos; San Luis capital; Cafayate (2018 data, source INPRES-CIRSOC 103 Anexo A) — rates/figures may have changed since
- **Zone 0-1 (muy reducida / reducida)**: all of Buenos Aires province, Santa Fe, Entre Ríos, Corrientes and Misiones are Zone 0; Córdoba capital and Neuquén's Confluencia are Zone 1; CABA is not listed separately in Anexo A — confirm with the INPRES lookup (2018 data, source INPRES-CIRSOC 103 Anexo A) — rates/figures may have changed since
- **INPRES-CIRSOC 103** building code sets requirements by zone, strictest in Zone 4; INPRES lists Parte I (general, 2018), Parte II (reinforced concrete, 2005), Parte III (masonry, 2018), Parte IV (steel, 2005) and Parte V (steel welding, 2018) as in legal force nationally (2026-10-23 verified)

#### Volcanic

- **Highest hazard among volcanoes wholly or partly in AR**: Planchón-Peteroa, then Laguna del Maule and Cerro Blanco, then Copahue, Tupungatito and Lanín; Mendoza has the highest-hazard volcanoes, then Neuquén (2024 data, source SEGEMAR/OAVV volcanic-risk ranking) — rates/figures may have changed since
- **Andes Patagonia**: Lanín (border), Copahue (Neuquén border) — both OAVV-monitored; Llaima, Villarrica (Chile-side affecting AR)
- **Mendoza area**: Maipo, Tupungatito, Planchón-Peteroa, San José (OAVV-monitored)
- **Chile-side eruptions reach AR**: OAVV cites Quizapu 1932, Hudson 1991 and Cordón Caulle 2011; the **2011 Cordón Caulle** tephra fell on Bariloche, Villa La Angostura and Ingeniero Jacobacci, 50–240 km from the vent (source Elissondo et al., NHESS 16:675, 2016, peer-reviewed, SEGEMAR co-authors)

#### Other

- **Flood**: Buenos Aires province, Tigre delta (chronic)
- **Drought**: generalized drought episodes since 2019 across the centre, east and north (source IGN, from SMN data); in the September 2026 national drought monitor the area in drought was 4,337,101 ha nationwide, at historic-minimum levels, and the Centro monitoring region was below the drought-duration threshold (2026 data, source Mesa Nacional de Monitoreo de Sequías / MAGyP, report published 2026-10-15)
- **Patagonia warming** + glacier retreat
- **Wildfire**: Patagonia + Cuyo summer

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **1900–1980 (modernist boom)** | Asbestos common, dated wiring |
| **1980–2010** | INPRES-CIRSOC 103 seismic code first in force 1983, updated 1991 (INPRES); reinforced-concrete Parte II 2005; amphibole asbestos banned by Res. MS 845/2000 and chrysotile from 2003-01-01 by Res. MS 823/2001 — fibre-cement fitted before 2003 can contain asbestos |
| **Post-2010** | INPRES-CIRSOC 103 Parte I (general) and Parte III (masonry) 2018 editions in legal force nationally (INPRES, 2026-10-23 verified) |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Escritura pública + escribano** | Mandatory closing |
| **Certificado de dominio + inhibiciones** | Valid 15, 25 or 30 days from issue, depending on whether the authorizing escribano is domiciled in the registry's city, elsewhere in the province, or outside it (Ley 17.801 art. 24) |
| **Plano de mensura registered** | Cadastre |
| **Libre deuda municipal/ABL + provincial + AySA/EDENOR** | No-debts certificates |
| **ARCA (ex-AFIP) retentions / tax checks** | Tax compliance — COTI no longer required: ARCA RG 5697/2025 abrogated the COTI regime (RG 2371 and complementary rules), in force 2025-05-23 (source RG text via Colegio de Escribanos CABA) |

### Climate change projections

- **Temperature**: +0.5–1 °C over almost the whole country in 2015–2039 under both RCP4.5 and RCP8.5; by 2075–2099 warming is largest in the northwest (above 3.5 °C under RCP8.5) and smaller in Patagonia and Buenos Aires province, which are more exposed to ocean air (2015 data, source CIMA UBA-CONICET modelling for Argentina's Third National Communication, CMIP5) — rates/figures may have changed since
- **Glacier retreat** in the Andes and Patagonia
- **Precipitation**: changes within ±10% except RCP8.5 in 2075–2099: −10 to −20% over western northern/central Patagonia and a moderate decline in the Mendoza Andes, with a similar increase in the centre and east (2015 data, source CIMA for the Third National Communication) — rates/figures may have changed since
- **Cuyo irrigation water**: the projected Andean decline would reduce the irrigation water that sustains current viticulture and fruit growing in the Cuyo oases (2015 data, source CIMA for the Third National Communication) — rates/figures may have changed since

---

## Section: `--mains`

### Sources

- **AySA** (CABA + 26 partidos of the Buenos Aires conurbano; 3,363 km² concession, 14,305,580 inhabitants in the concession area) (2025 data, source AySA Nuestros números / Reporte de Sustentabilidad 2025): `https://www.aysa.com.ar/` — **privatization in progress**: Ministerio de Economía Res. 1818/2026 (signed 2026-10-20, B.O. 2026-10-22) awarded the State's 90% stake to the consortium Rowing SA / Arcos Saneamento e Participações SA / PHX Aqua AR BV / Transclor SA for USD 340,200,000 ex-VAT, with the share-purchase contract due by 2026-11-13 (Decreto 494/2025; tender called by Res. 704/2026) — confirm the operator after closing
- **ABSA** (95 localities in 53 PBA municipalities, 2.6 million people served — not the whole rest of the province; check the operator for the specific locality) (2026 data, source ABSA): `https://www.aguasbonaerenses.com.ar/`
- **Aguas Cordobesas**, **AYSAM — Aguas Mendocinas** (Mendoza), **Aguas Rionegrinas** (state-owned, Río Negro) etc.
- Rural Patagonia + Cuyo: cisterns + pozos negros / cámara séptica + lecho nitrificante

### Costs

| Scenario | Cost (USD) |
|---|---:|
| Mains connection | AySA area, operator's charge only: water ≈ USD 453–679, sewer ≈ USD 710–1,129 per connection (2026 data, computed: 284.25 × 2,432.5294 = ARS 691,446 and 426.53 × 2,432.5294 = ARS 1,037,547 for DN 13–32 mm water; 445.81 × 2,432.5294 = ARS 1,084,446 and 709.34 × 2,432.5294 = ARS 1,725,490 for sewer; lower figure in the near pavement, higher in the opposite pavement or roadway; RANT art. 17 base tariffs `https://www.argentina.gob.ar/sites/default/files/anexo_7095631_2.pdf` × ERAS coefficient K of 2026-11-01 `https://www.argentina.gob.ar/argentina.gob.ar/eras/institucional/informacion-tecnica/regimen-tarifario-eras`, at ARS 1,527.85/USD); other operators: data not publicly available — get the operator's written quote |
| Septic + cámara | data not publicly available — get local quotes |
| Pozo negro | data not publicly available — get local quotes |
| Bored well (Patagonia) | est. ~$4,000–$10,000: no Patagonia price found; 2026 national guide gives USD 2,500–6,000 for a domestic well to 60 m, USD 8,000–25,000 for a farm or medium irrigation well of 60–150 m (secondary: GEXPLO) — depth and rock set the bill, get a local driller's quote |

---

## Cost benchmarks (AR 2026)

| Work | Cost (USD typical) |
|---|---:|
| Inspection (relevamiento) | CABA suggested fee by time: ARS 192,021 for the first 5 hours (≈ USD 126), then ARS 38,404 per extra hour (≈ USD 25) at ARS 1,527.85/USD (2026 data, source CPAU Art. 1.13, July 2026 table `https://static.cpau.org/.newsite/ejercicio_profesional/honorarios_sugeridos/2026/julio/CUADROS-ICC-JUNIO-2026.pdf`); architects in CABA only, elsewhere data not publicly available — get a written quote from a registered architect or engineer |
| Escribano fees | est. ~1–2% of price: national-jurisdiction tariff 2% of the deed amount (1987 data, source Decreto 1208/87 art. 2 via Colegio de Escribanos CABA — rates/figures may have changed since); a 2026 guide gives 1–1.5% in CABA, Córdoba and Mendoza, 1–2% in PBA (listing platform: Roomix, Apr 2026) — get the escribano's written quote |
| Sellos provincial | 1.0–3.5% (2026: Córdoba 1.0%, PBA 2.0%, Mendoza 2.0%, CABA 2.7–3.5%) |
| ITI federal | REPEALED 2024-07-08 (Ley 27.743 art. 67) — no longer applies |
| Realtor commission | CABA freely agreed (Ley 2340 art. 11 inc. 2); PBA 1.5–3% per party (Ley 10.973 art. 54); est. ~3–4% buyer side in CABA market use (secondary: broker guides 2026) |
| **Total transaction cost (buyer CABA)** | **est. ~6.25–8.75%** of price = 1.75% sellos half-share (3.5% rate) + 1–2% escribano + 0.5–1% other + 3–4% broker |
| Roof renovation | est. ~$4,000–$16,000 for a 100 m² house: ARS 6–14 million with new sheets on a sound structure, ARS 15–25 million or more if the structure is rebuilt (Los Andes, Jul 2026, secondary press); July ARS prices converted at the later BCRA rate of ARS 1,527.85/USD of 2026-10-22, so the USD range is indicative; no official price series — get ≥3 quotes |
| Asbestos abatement | data not publicly available — no public price source (secondary: CAEDE guide `https://caede.com.ar/demolicion/demolicion-con-asbesto`, checked 2026-11-02); get written quotes from firms licensed for asbestos work, with removal, packing, transport and disposal itemised |
| Earthquake retrofit (Cuyo) | data not publicly available — get a structural engineer's assessment against INPRES-CIRSOC 103 first, then quotes (verify at `https://www.inpres.gob.ar/`) |
| Energy retrofit | data not publicly available — scope it per house and get ≥3 quotes |
| Solar PV (5kW) | est. ~$5,000–$10,000: 2026 installer list shows on-grid 4.6–5.8 kW from USD 5,200–5,900, 10 panels + 5 kWh battery from USD 7,700 (secondary: TodoEnergías); no official price series — get ≥3 quotes |

## Active fiscal incentives (2025-2026)

- **Mortgage market reopening 2024-2025**: 30+ banks offering UVA loans + USD-linked
- **Cepo cambiario partial lift effective 2025-04-14** (BCRA Phase 3, announced 2025-04-11): natural persons can buy USD in the official or securities market with no amount or purpose limit; the exchange-rate band started at **ARS 1,000–1,400/USD** on 2025-04-11 and moved ±1% monthly to 2025-12-31; from 2026-01-01 floor and ceiling slide each month by the latest INDEC monthly CPI (t-2) — band **ARS 715.12–1,943.56/USD** on 2026-10-23; an IMF EFF of USD 20bn backs the programme. Since Com. "A" 8336 (2025-09-26) individuals accessing the official FX market sign a 90-day commitment not to buy FX-settled securities, and Com. "A" 8417 (2026-04-09) asks the same 90-day commitment of individuals transferring FX abroad. Dividends for fiscal years from 2025-01-01 can be paid abroad (Com. "A" 8226); retained dividends to Dec 2024 + commercial debt to 2023-12-12 were channelled via BOPREAL Serie 4 (2026 data, source [BCRA régimen de bandas](https://www.bcra.gob.ar/regimen-de-bandas-cambiarias) + BCRA Evolución del Mercado de Cambios, Aug 2026).
- **PROCREAR** trust fund **DISSOLVED** by Decreto 1018/2024 (Nov 2024); existing PROCREAR loans continue to be managed by Banco Hipotecario under a Ministerio de Economía contract (source [argentina.gob.ar](https://www.argentina.gob.ar/noticias/el-gobierno-dispuso-la-disolucion-del-fondo-fiduciario-publico-procrear))
- **Ganancias exemptions from 2026** (Ley 27.802 art. 192): individuals' gains on property sales or transfers of rights from 2026-01-01, and rental income from casa-habitación lets for fiscal years from 2026-01-01 (source [Ley 27.802 texto](https://www.argentina.gob.ar/normativa/nacional/norma-423680/texto))
- **Zonas Francas** for commercial

## Common listing platforms

- **Zonaprop** — DOMINANT
- **Argenprop**, **MercadoLibre Inmuebles**, **Inmoclick**
- **Reporteinmobiliario.com** — market data

## Caveats unique to AR

- **USD-denominated market** — listings + transactions in USD billete, NOT pesos
- **Currency controls (cepo cambiario)** — partially lifted April 2025; company-level FX rules remain (BCRA Exterior y Cambios text, Com. "A" 8481, in force 2026-09-15), and individuals buying at the official market sign a 90-day no-FX-securities commitment since Com. "A" 8336 (2025-09-26)
- **Currency arbitrage** (oficial / blue / MEP / CCL) historically — gap narrowing since 2024
- **High inflation** (peso depreciation) makes ARS-denominated investments meaningless
- **Capital gains**: individuals' property sales from 2026-01-01 are exempt (Ley 27.802 art. 192 + Decreto 406/2026); the 15% cedular rate applied to post-2018 acquisitions sold 2018–2025
- **Bienes Personales** wealth tax — major issue for foreigners; reformed by **Ley 27.743 art. 63** (B.O. 2024-07-08) into a single scale over Argentine + foreign assets whose top bracket drops each year: FY2024 0.50–1.25% → FY2025 0.50–1.00% → FY2026 0.50–0.75% → flat **0.25%** from FY2027 (2026-10-23 verified, Ley 27.743 art. 63 text — new art. 25 of Ley 23.966)
- **DNU 70/2023** — rental market liberalized (art. 249 repealed Ley 27.551); the regime rests on the DNU: Ley Bases (Ley 27.742) has no residential-lease chapter and does not ratify it (InfoLEG texts, checked 2026-11-03) — see `--rental`
- **Boleto de compraventa** pre-escritura common
- **Foreign ownership of rural land (Ley 26.737) — status in flux, 2026-10**:
  - DNU 70/2023 art. 154 repealed the law; the Cámara Federal de La Plata (Sala III) declared art. 154 unconstitutional on 2024-03-21 in the CECIM amparo; the CSJN revoked that ruling for lack of standing on 2026-09-29; on 2026-10-09 the CSJN, in "Asociación Civil Árbol de Pie y otros c/ PEN s/ amparo colectivo" (FGR 20213/2023/CS1), suspended the effects of art. 154 on an interim basis until the Bariloche federal judge rules on standing and the cautelar, so the Ley 26.737 limits apply again provisionally
  - A bill restoring Ley 26.737 (arts. 38–39 of the Ley de Inviolabilidad de la Propiedad Privada) passed Diputados with amendments on 2026-10-22 and returns to the Senate — not law
  - Sources: legal and parliamentary press, secondary (Parlamentario 2026-09-29, Chequeado, Palabras del Derecho 2026-10-22, Pensamiento Penal 2026-10-16) — verify the rulings at csjn.gov.ar and the bill at hcdn.gob.ar / senado.gob.ar before relying on either state
  - Limits when in force (InfoLEG text): **15%** of rural land for all foreign holders, computed nationally and also per province, municipio or equivalent (art. 8); **30%** of that share per foreign nationality (art. 9); **1,000 ha** in the zona núcleo or equivalent area per foreign holder (art. 10); foreign holding barred on land containing or bordering large permanent water bodies and in zonas de seguridad de frontera (art. 10)
- **Zonas de seguridad de frontera** — foreigners need **Previa Conformidad** before acquiring, leasing or taking possession of property in the border security zone (Decreto-Ley 15.385/44 art. 4 as replaced by Ley 23.554 art. 42; Comisión Nacional de Zonas de Seguridad), processed by the Dirección Nacional de Asuntos Técnicos de Fronteras (Vicejefatura de Gabinete del Interior); the strip runs up to 150 km inland along land borders and 50 km along the coast (secondary: CFNA notarial forum 2018) — check the parcel against the official zone delimitation
- **COTI no longer required** — abrogated by ARCA RG 5697/2025 (in force 2025-05-23)
- **Escribano público mandatory + buyer-chooses** — UNIQUE
- **23 provincias + CABA different sellos rates**
- **Mortgage market restarted 2024** after long hiatus
- **Cepo lift April 2025** — can now hold USD officially as natural person
- **Bariloche** USD-denominated tourism + lifestyle premium

## Reddit / forum sources

- **r/argentina** — biggest community
- **r/BuenosAires**, **r/AskArgentina** (rental + relocation Q&A threads); r/PERSONAL_FINANCE_AR ❌ DEPRECATED — dead on 2026-10-23 (not found); verify with r/AskArgentina
- **r/Bariloche**, **r/Mendoza**, **r/Cordoba**
- **Buenos Aires Times** (English)
- **Reporte Inmobiliario** monthly newsletters
- **TheLatinvestor** market analysis

## Verification authorities

| Authority | When to call |
|---|---|
| **Registro de la Propiedad Inmueble (provincial)** | Title verification |
| **Catastro provincial** | ARBA / ATM cadastre |
| **Escribano público** (buyer-chosen) | Mandatory closing |
| **ARCA (ex-AFIP)** | Federal taxes + CDI (Decreto 953/2024 of 2024-10-24, B.O. 2024-10-25, in force from its dictation per art. 12; COTI abrogated by ARCA RG 5697/2025, in force 2025-05-23) |
| **Dirección Nacional de Asuntos Técnicos de Fronteras** (Jefatura de Gabinete › Vicejefatura de Gabinete del Interior) | Border-zone *Previa Conformidad*: required for transfers, leases or any hand-over of possession of property in the Zona de Seguridad de Fronteras; filed via TAD (`https://www.argentina.gob.ar/interior/asuntos-tecnicos-de-fronteras/solicitud-de-previa-conformidad`, 2026-10-23 verified) |
| **Municipal** | ABL + permits |
| **Ente de Turismo CABA** — Registro de Propiedades de Alquileres Temporarios Turísticos | If short-let: free, mandatory registration before listing (Ley CABA 6.255; procedure Res. 8/ENTUR/2025) |
| **INPRES** (within SEGEMAR since Decreto 396/2025) | Seismic risk — zone lookup by coordinates |
| **OAVV (SEGEMAR)** | Volcanic risk + alerts (Andes) |

## Source URL templates

| Source | URL pattern |
|---|---|
| Zonaprop | `https://www.zonaprop.com.ar/` |
| Argenprop | `https://www.argenprop.com/` |
| MercadoLibre Inmuebles | `https://inmuebles.mercadolibre.com.ar/` |
| Reporte Inmobiliario | `https://www.reporteinmobiliario.com/` |
| INDEC | `https://www.indec.gob.ar/` |
| BCRA | `https://www.bcra.gob.ar/` |
| ARCA (ex-AFIP) | `https://www.arca.gob.ar/` (legacy `https://www.afip.gob.ar/` also resolves) |
| INPRES seismic | `https://www.inpres.gob.ar/` (zone lookup by coordinates: `https://www.inpres.gob.ar/desktop/zonas.html`) |
| DNV TMDA (national-road traffic) | `https://www.argentina.gob.ar/transporte/vialidad-nacional/institucional/informacion-publica/tmda` |
| SEGEMAR | `https://www.argentina.gob.ar/economia/segemar` (legacy `www.segemar.gov.ar` HTTP-redirects here) |
| OAVV volcano observatory | `https://oavv.segemar.gob.ar/` |
| SMN | `https://www.smn.gob.ar/` (could not be read for verification on 2026-11-04; institutional page `https://www.argentina.gob.ar/smn`) |
| AySA (CABA water) | `https://www.aysa.com.ar/` |
| ARBA (PBA cadastre) | `https://www.arba.gov.ar/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Last verified**: 2026-08-07. Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (Zonaprop Index + Índice M² Real + TuLugar + TheLatinvestor 2026), traffic (DNV TMDA), tax (2026 provincial Impuesto Inmobiliario + sellos scales for CABA, PBA, Mendoza and Córdoba + **ITI federal REPEALED 2024-07-08** by Ley 27.743 art. 67 + Bienes Personales reformed by Ley 27.743 art. 63 (single scale over Argentine + foreign assets, top bracket stepping down FY2025 1.00% → FY2026 0.75% → flat 0.25% from FY2027) with FY2025 ARCA thresholds + individuals' property sales exempt from Ganancias from 2026-01-01 (Ley 27.802 art. 192 + Decreto 406/2026) + **COTI abrogated** by RG 5697/2025 + **AFIP→ARCA** Decreto 953/2024), rental (DNU 70/2023 liberalized regime, not ratified by Ley Bases; CABA short-let registry Ley 6255; Ganancias exemption for casa-habitación rent from 2026), work (ARCA Monotributo scale from 2026-08-01, category K cap ARS 126,610,838.75; SIPA + OEDE salary data; SMVM), risks (INPRES-CIRSOC 103 seismic zoning by department + SEGEMAR/OAVV volcanic ranking + flood Tigre), foreign-buyer rules (Ley 26.737 repealed by DNU 70/2023 art. 154, status in flux in the courts and Congress — see Caveats; border-zone Previa Conformidad), mains (AySA + ABSA + provincial), cepo (Phase 3 lift 2025-04-14; band opened at ARS 1,000–1,400/USD and has moved since — see Active fiscal incentives).
**Confidence**: HIGH for items re-read against statute, gazette or official pages on 2026-10-23: the 2026 provincial Impuesto Inmobiliario and sellos scales (Leyes Impositivas of CABA, PBA, Mendoza and Córdoba), the ITI repeal (Ley 27.743 art. 67), the Bienes Personales step-down (Ley 23.966 art. 25 as replaced) and FY2025 ARCA amounts, the COTI abrogation (RG 5697/2025), the DNU 70/2023 lease regime, the CABA short-let registry (Ley 6255), the non-resident 21% rent rate (computed from LIG arts. 103 + 104 g), the `--work` figures (ARCA, Secretaría de Trabajo SIPA + OEDE, SMVM), the AFIP→ARCA change (Decreto 953/2024) and the April 2025 cepo lift (BCRA); HIGH for the Ganancias exemptions for individuals' property sales and casa-habitación rent from 2026-01-01 (Ley 27.802 art. 192 + Decreto 406/2026 texts, re-read 2026-11-03), with non-resident coverage of the rent exemption resting on secondary legal commentary. MEDIUM for `--price` (CABA, GBA Norte, Córdoba and Mar del Plata rows and the Índice M² Real asking-to-closing gap re-checked, but these are asking-price and broker-index series, not registry prices; Belgrano and Recoleta bands read from chart order; several trends n/a), for the Ley 26.737 status (DNU 70/2023 art. 154 repeal on InfoLEG; the 2026 CSJN rulings and the Diputados vote rest on legal and parliamentary press only), for `--risks` and `--mains` (seismic zoning, volcanic ranking, drought monitor, certificate validity, AySA and ABSA facts re-sourced; flood, wildfire, glacier retreat, pre-1980 build-era rows and three mandatory-at-sale rows not verified) and for provincial registry URL stability (varies). LOW for the Bariloche and Mendoza price rows (not confirmed in the cross-check), the `--traffic` verdict bands and road examples (the DNV TMDA tool could not be read for verification on 2026-10-23), the border-zone widths (secondary only), the unsourced lines 'mortgages restarted 2024', 'Zonaprop DOMINANT', '30+ banks' and the currency-gap trend, the USD cost-benchmark and `--mains` cost rows and the escribano and other-cost shares inside the transaction-cost totals (est., no fee schedule fetched), and the forum sources (not re-checked).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--tax` | 2026-10-23 | 2026-11-04 maintenance run | Mendoza's 2026 inmobiliario scale and ARS 43,645 minimum (Ley 9680 art. 2), PBA's 2.0% sellos (Ley 15.558), ARCA's FY2025 Bienes Personales scale and the Ley 27.743 provisions (ITI repeal, rate step-down, single scale for foreign and domestic assets) were re-read at source and are unchanged. |
| `--rental` | 2026-10-23 | 2026-11-04 maintenance run | InfoLEG's text of DNU 70/2023 shows the 2023-12-21 publication and the art. 249 repeal of Ley 27.551; Dentons (secondary) gives 2023-12-29 as its entry into force under the eighth-day rule. |
| `--work=<profession>` | 2026-10-23 | 2026-11-04 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | ARCA date per Decreto 953/2024 art. 12; INTRA replaced by the Dirección Nacional de Asuntos Técnicos de Fronteras; PRT replaced by the Ente de Turismo registry (Ley 6.255); registry, escribano and municipal rows not re-checked |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | All 12 URLs checked; SEGEMAR replaced; SMN and Zonaprop could not be read for verification (kept); OAVV and DNV TMDA rows added |
| `--risks` | 2026-10-23 | 2026-11-04 maintenance run | The SMN institutional page on argentina.gob.ar was read; SMN's own site could not be read for verification on 2026-11-04 and should be checked directly. |

## Extension TODOs

- [ ] Per-province registry URL + lookup flow
- [ ] Per-province sellos rates table
- [ ] Bienes Personales calculator with the Ley 27.743 art. 63 step-down scale (FY2025 0.50–1.00% / FY2026 0.50–0.75% / flat 0.25% from FY2027)
- [ ] Cepo cambiario lift impact on transactions
- [ ] Mortgage product comparison (UVA vs USD-linked)
- [ ] DNU 70/2023 rental contract templates
- [ ] Border-zone Previa Conformidad flow (Dirección Nacional de Asuntos Técnicos de Fronteras)
- [ ] CABA short-let registry tracker (Ley 6255, Registro de Propiedades de Alquileres Temporarios Turísticos)
- [ ] Bariloche USD-denominated market specifics
- [ ] CABA neighborhood premium tracker (Puerto Madero/Palermo/Recoleta)

## Update history

- **2026-04-26** — Initial population
- **2026-05-27** — Tier-1 corrections (LATAM validation batch): AFIP→ARCA (Decreto 953/2024), ITI repeal (Ley 27.743 art. 67), Bienes Personales FY2025 schedule, DNU 70/2023 lease reform, Monotributo and SMVM 2026 figures, April 2025 cepo lift
- **2026-05-29** — Anti-hallucination sweep: `~` markers on provincial Impuesto Inmobiliario rates; ITI cost-benchmark row marked repealed
- **2026-08-07** — Bienes Personales step-down scale (Ley 27.743 art. 63, FY2023–FY2027) re-verified
- **2026-10-21** — Tax tracker entry re-checked (December regulatory-watch wave, run early)
- **2026-10-23** — Refresh wave (market, tax-legal, risk-infra). Playbook-level date not re-stamped: `--price`, `--risks` and `--mains` were not fully re-verified, nor were the `--tax` transaction-cost totals. Counts per section (changed / confirmed / unverifiable):
  - Re-verified: `--rental` 4 / 6 / 1; `--work` 5 / 3 / 2; `--tax` Impuesto Inmobiliario 4 / 0 / 1, Sellos 4 / 0 / 0, ITI 2 / 1 / 0, Bienes Personales 7 / 3 / 0, Capital gains 3 / 0 / 0, COTI 1 / 0 / 0; Verification authorities 4 / 1 / 3; Source URL templates 3 / 8 / 1 (2 rows added)
  - Refreshed, not re-verified: Country profile 2 / 4 / 4; `--price` 17 / 6 / 2; `--tax` total transaction cost 3 / 0 / 2; Cost benchmarks 3 / 1 / 7; Active fiscal incentives 3 / 0 / 2; Caveats unique to AR 5 / 3 / 2; `--traffic` 2 / 2 / 4; `--risks` 14 / 4 / 11; `--mains` 3 / 4 / 6; Common listing platforms 0 / 5 / 1 (URL liveness only); Reddit / forum sources 1 / 6 / 2
  - Main changes: gobiernos locales 2,259 → more than 2,300 (ReFeGLo) and Decreto 953/2024 in force on its 2024-10-24 issue (art. 12), not 2024-11-05; price table rebuilt from Zonaprop Index Sep 2026, Índice M² Real, TuLugar and TheLatinvestor (12 rows replaced, 4 added; unsourced trends → n/a); 2026 Impuesto Inmobiliario scales; sellos PBA 3.6% → 2.0%, Mendoza 3.0% → 2.0%, Córdoba "varies" → 1.0% / 0.70%, CABA 3.5% plus a 2.7% tier and the vivienda-única exemption; FY2025 Bienes Personales mínimo, casa-habitación and tramo bounds corrected (ARCA) and REIBP restated as a fixed 0.45% × 5; individuals' property sales exempt from Ganancias from 2026-01-01 (Ley 27.802 art. 192 + Decreto 406/2026), replacing the 15% / 13.5% lines for later sales; COTI abrogated (RG 5697/2025); "consolidated by Ley Bases" corrected — the lease regime rests on DNU 70/2023; CABA short-let rewritten from Ley 6255; Monotributo category K cap ARS 108,357,084.05 → ARS 126,610,838.75 (from 2026-08-01); SIPA and OEDE salary data replace unsourced ranges; INPRES merged into SEGEMAR and INA made a unit (Decreto 396/2025); seismic zoning per INPRES-CIRSOC 103 (2018) Anexo A at department level; volcanic list per the SEGEMAR/OAVV 2024 ranking; 2008 Chaitén line replaced by Cordón Caulle 2011; certificate validity 15 / 25 / 30 days (Ley 17.801 art. 24); AySA privatization award and ABSA coverage (95 localities, 53 municipalities); PROCREAR trust fund dissolved (Decreto 1018/2024); Ley 26.737 status rewritten (CSJN 2026, secondary press); "INTRA" and "PRT" replaced by the Dirección Nacional de Asuntos Técnicos de Fronteras and the Ente de Turismo registry; r/PERSONAL_FINANCE_AR ❌ DEPRECATED; SEGEMAR URL replaced; OAVV and DNV TMDA sources added
- **2026-11-03** — Follow-up checks: Ganancias exemption for casa-habitación rent from 2026-01-01 added to `--rental` (Ley 27.802 art. 192 + Decreto 406/2026); Ley Bases "now permanent" caveat and short-let line corrected (Ley 27.742 text has no lease chapter); Extension TODOs: INTRA and Ley 4631 references replaced; Status Coverage check and Confidence recomputed; per-section verification table added
- **2026-11-04** — Maintenance run: closed `--tax`, `--rental`, `--work=<profession>`, `--risks`; still open `--price`, `--mains`, Cost benchmarks (AR 2026).
