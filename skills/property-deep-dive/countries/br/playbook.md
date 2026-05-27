# Brazil 🇧🇷 — Property Due-Diligence Playbook

ISO2: `br`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CEP)**: 8 digits in `XXXXX-XXX` format (`01310-100` Avenida Paulista, `22070-000` Copacabana, `30130-000` BH centro)
- **Admin levels**: 26 states + DF (Brasília) + 5,570 municípios
- **Currency**: **BRL** (Brazilian real); 1 USD ≈ 5–6 BRL; 1 EUR ≈ 5.5–6.5 BRL
- **Languages**: Portuguese (official); regional indigenous languages
- **Cadastre — decentralized + transitioning to national**:
  - **Cartórios de Registro de Imóveis** (per-município; ownership only transfers when escritura registered)
  - **Matrícula** = unique property ID (life-of-property record)
  - **CIB (Cadastro Imobiliário Brasileiro) "CPF dos Imóveis"** — NEW unique national identifier under Receita Federal IN RFB 2.275/2025; rollout deadline mid-2026
  - **SINTER** (Sistema Nacional de Gestão de Informações Territoriais)
  - **INCRA** (`https://www.incra.gov.br/`) — rural land registry
- **Identifier**: matrícula (per-cartório); CIB (national, rolling out)
- **Foreign buyer needs CPF** before any transaction
- **Ownership types**: pleno domínio (full); usufruct; multipropriedade (timeshare, Lei 13.777/2018)

## Section: `--price`

### Primary sources

- **FIPE-ZAP Index** (FGV/Fipe): `https://www.fipe.org.br/en-us/indexes-and-indicators/fipezap` — most-cited; 500k+ valid listings/month
- **IBGE Vivienda**: `https://www.ibge.gov.br/` — census + housing surveys
- **BCB (Banco Central) Real Estate Market Report**: `https://www.bcb.gov.br/`
- **CBIC (Câmara Brasileira da Indústria da Construção)**

### Listing platforms

- **ZAP Imóveis + VivaReal** — DOMINANT (merged under Grupo OLX/Adevinta): `https://www.zapimoveis.com.br`, `https://www.vivareal.com.br`
- **Imovelweb**, **OLX Imóveis**: `https://www.olx.com.br/imoveis`
- **Quinto Andar** (rental + sales innovator): `https://www.quintoandar.com.br`
- **DataZAP** for analytics
- **Loft** (urban resale, fintech-backed)

### 2026 price benchmarks (FIPE-ZAP Q1 2026)

| Region | BRL/m² (apt) | YoY |
|---|---:|---:|
| **São Paulo Vila Nova Conceição** | 20,000–38,000 | +6.11% (+0.55% real) |
| **São Paulo Jardins** | 17,000–35,000 | +6.11% |
| **São Paulo Itaim Bibi** | 19,400 | +6.11% |
| **São Paulo Pinheiros** | 18,400 | +6.11% |
| **São Paulo Butantã/Santana** | 5,500–9,000 | +6.11% |
| **Rio de Janeiro Ipanema/Leblon** | 25,000–40,000 | +4.62% (-0.87% real) |
| **Rio de Janeiro avg** | 12,000–15,000 | +4.62% |
| **Brasília avg** | 9,750 | +5.5% |
| **Brasília Plano Piloto** | 10,000–12,000 | +5.5% |
| **Belo Horizonte avg** | 10,850 | +5.0% |
| **Belo Horizonte Savassi** | 7,000–9,000 | +5.0% |
| **Curitiba** | 6,500–8,100 | +5.5% |
| **Florianópolis** | 10,000–15,000 (beach 15,000–30,000) | +12% |

### Compute

1. BRL/m² = price / **área privativa** (private area, NOT including common parts)
2. Cross-check **FIPE-ZAP** + **DataZAP** + recent matrícula transactions
3. **Valor venal vs market**: valor venal typically 30-60% below market (intentional)
4. **Convert BRL to USD/EUR** at current FX

### Key terms

- Matrícula = property "birth certificate" + life record
- Valor venal = municipal cadastral value (basis for IPTU + ITBI)
- Habite-se = occupancy permit
- Escritura pública = notarized deed
- Cartório de Registro de Imóveis = land registry (per-município)
- CIB = new national property identifier (2026)

---

## Section: `--traffic`

### Sources

- **DNIT (Departamento Nacional de Infraestrutura)**: `https://www.dnit.gov.br/` — federal highways (BR-roads)
- **DERSP (SP), DER-RJ, DER-MG, etc.** — state-level
- **CET-SP, RioCard** — city traffic data

### Key term

**VMD (Volume Médio Diário)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, BR-roads secondary)
- 🔴 > 35,000 v/d (Marginais SP, Ponte Rio-Niterói, BR-101 metropolitan)

---

## Section: `--tax`

### Annual property tax — IPTU

**Imposto Predial e Territorial Urbano** — annual; municipal.

| Município | Residential rate | Commercial/vacant |
|---|---:|---:|
| **São Paulo** | 0.7–1.5% | 1.1–1.9% |
| **Rio de Janeiro** | 0.6–1.2% | 1.0–1.5% |
| **Brasília** | 0.3–1.0% | 1.0–1.5% |
| **Belo Horizonte** | 0.6–1.2% | 1.0–1.5% |

- Base = **valor venal** (typically 30-60% below market)
- Annual or 10x monthly installments
- **Early payment 4-10% discount**

### Transaction taxes — ITBI

**Imposto sobre Transmissão de Bens Imóveis** — municipal:

| Município | ITBI rate |
|---|---:|
| **São Paulo** | **3%** of higher-of price/valor venal de referência |
| **Rio de Janeiro** | **2%** |
| Other municípios | 2–3% |

### Other taxes

- **ITR (Imposto Territorial Rural)**: rural; federal; INCRA-administered
- **IR (Imposto de Renda) capital gains**:
  - Residents: progressive **15–22.5%** sliding by gain size
  - Non-residents: flat **15%**
  - **R$35k small-sale exemption**
  - Resident-only **R$440k primary residence exemption**
- **IRPF 2026 filing window**: March 23 – May 29, 2026

### Cartório fees

- **Escritura**: 0.5–2% of price
- **Registro**: 0.5–1% of price
- **Combined**: ~1–2% mandatory closing

### Total transaction cost (buyer side)

- São Paulo standard: **~4–5%** (3% ITBI + 1-2% cartório)
- Rio standard: **~3–4%** (2% ITBI + 1-2% cartório)
- Plus optional valuation, lawyer, mortgage costs

### Future risk — REFORMA TRIBUTÁRIA

**Emenda 132/2023** — major tax reform:
- **2026: TEST YEAR** — IBS/CBS rates piloted at low rates, no real collection
- **2027: CBS** (federal, replaces PIS/COFINS/IPI) goes live
- **2029: IBS** (state+municipal, replaces ICMS/ISS) phased in
- **2033: full system in place**
- **IPTU/ITBI/IR NOT directly changed** by reform — but **CIB registry will likely expand IPTU/ITBI tax base** as municipalities update outdated valor venal
- Real estate operations (sale, lease, intermediation) **WILL be taxed by IBS+CBS** — affects developers, large landlords, agencies

---

## Section: `--rental`

### Long-term residential

- **Lei do Inquilinato (Lei 8.245/1991)** — federal, governs all rental
- **Tenant protection moderate** (less strict than Argentina, more than US)
- 30-day notice tenant; 90-day notice landlord (or 30-day end-of-contract)
- **Fiador** (guarantor) common
- **Caução** (security deposit) up to 3 months

### Short-let (Airbnb)

- **Lei do Inquilinato** defines "locação por temporada" up to **90 days**
- Federally legal; **no national permit**
- **STJ ruling 2021**: condomínios CAN BAN STR entirely — dominant restriction
- **Rio de Janeiro**: municipal regulation in development (registration likely Copacabana/Ipanema)
- **Florianópolis**: ~40k active Airbnb listings; only Lei do Inquilinato + condomínio rules
- **No federal residency requirement**; secondary-home owners can legally STR

### Tax on rental

- **IR (income tax)** progressive on net rental
- Non-residents: 15% withholding
- IPTU paid by owner (tenant reimbursement common)

---

## Section: `--work=<profession>`

### Sources

- **MTE (Ministério do Trabalho)**: `https://www.gov.br/trabalho/`
- **Catho** — biggest job board: `https://www.catho.com.br/vagas`
- **Indeed.com.br**, **Vagas.com.br**, **InfoJobs**, **LinkedIn BR**
- **CRECI** for realtors; **CONFEA/CREA** for engineering

### Self-employment

- **MEI (Microempreendedor Individual)**: simplified, up to R$81k revenue
- **Simples Nacional**: small business, up to R$4.8M
- **CPF** required for foreigners
- **CNPJ** for business
- **PIS/COFINS** federal taxes (replaced by CBS in 2027)

### Salary benchmarks (2025)

- Median monthly gross:
  - São Paulo: ~R$5,000–R$10,000 (€900–€1,800)
  - Rio de Janeiro: ~R$4,500–R$9,000
  - Brasília (govt): ~R$6,000–R$12,000
  - Smaller cities: ~R$3,000–R$5,500
- **Salário mínimo**: R$1,518/month (2026) — €273

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **CEMADEN** | `https://www.cemaden.gov.br/` | Flood + landslide early warning (Decreto 7513/2011) |
| **CPRM (Serviço Geológico do Brasil)** | `https://www.cprm.gov.br/` | Geology, geological hazards |
| **INMET** | `https://www.inmet.gov.br/` | Weather, climate |
| **IBAMA** | `https://www.ibama.gov.br/` | Environmental |
| **ANA (Agência Nacional de Águas)** | `https://www.ana.gov.br/` | Water management |

### Specific risks

- **Flooding + landslide** — major risk:
  - **Petrópolis Feb 2022**: 252.8mm in 3 hours, 231 fatalities — deadliest landslide on record in city
  - **Rio Grande do Sul May 2024 floods** — extensive damage, statewide emergency
  - **Feb 2026 Zona da Mata floods**: Juiz de Fora wettest month on record (4× monthly avg)
  - 17 rain gauges in Petrópolis since 2015 (CEMADEN)
- **Drought**: Northeast (sertão) — chronic
- **Rainforest fire**: Amazonas — increasing
- **Tropical storms**: northeast coast (Bahia, Ceará)
- **Earthquake risk LOW** (stable Brazilian shield)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990** | Asbestos common (banned 2017 nationally); lead paint |
| **Pre-1990 informal tenure** | Many favela properties without title |
| **1980s–2000s "casa-grande" reforma** | Variable construction quality |
| **Post-2000** | NBR codes tightened |
| **Post-2017 asbestos ban** | Modern materials |

### Mandatory at sale

| Document | Required because | Notes |
|---|---|---|
| **Certidão de matrícula atualizada** | Title (≤30 days) | Cartório de Registro de Imóveis |
| **Certidão negativa de ônus reais** | No-liens | Same |
| **Certidão negativa de débitos** | Federal (RFB), estadual, municipal (IPTU paid) | Multiple authorities |
| **Certidão de regularidade do condomínio** | No condo arrears | If apartment |
| **Habite-se** | Occupancy permit | Municipal |
| **IPTU + valor venal certificate** | Tax base | Municipal |
| **Personal certidões on seller** | CND federal, criminal, trabalhista, civil, tributária | Multiple |
| **Escritura pública** | At Tabelionato de Notas | Notary |
| **Registration at Cartório de Registro de Imóveis** | ONLY step that transfers ownership | CRITICAL |

### Climate change projections

- **+2.0–4.0°C** by 2100
- **Amazon deforestation** + drying — global tipping point concern
- **Coastal sea-level rise**: +30–80 cm by 2100 (Recife, Santos, Fortaleza vulnerable)
- **Drought intensification**: Northeast + Cerrado
- **Increased extreme rainfall** (Petrópolis 2022 type)

---

## Section: `--mains`

### Sources

- **SABESP** (SP): `https://www.sabesp.com.br/`
- **CEDAE** (Rio — partially privatized): `https://www.cedae.com.br/`
- **COPASA** (MG), **SANEPAR** (PR), state operators
- **ANA** federal regulator
- **Marco Legal do Saneamento (Lei 14.026/2020)**: universal access target 2033

### Verification

- **47% of population unassisted by sewage collection/treatment** (2020 data, most recent national)
- RJ ~15% unconnected; CEDAE-contracted municípios only 39.2% actually connected
- **SABESP committed R$47.4B 2024-28**; universalization target 2029
- **Favelas**: fossas (cesspits) common; informal connections widespread
- **Per-município coverage extremely uneven**

### Costs

| Scenario | Cost (BRL) |
|---|---:|
| Mains connection | 5,000–25,000 |
| Septic upgrade | 8,000–30,000 |
| Cisterna installation | 15,000–60,000 |
| Bored well | 25,000–80,000 |

---

## Cost benchmarks (BR 2026)

| Work | Cost (BRL) |
|---|---:|
| Vistoria (inspection) | 1,000–3,000 |
| Avaliação | 2,000–6,000 |
| Cartório fees (escritura + registro) | 1–2% of price |
| ITBI (SP) | 3% of higher-of price/valor venal |
| ITBI (Rio) | 2% |
| **Total transaction cost (buyer SP)** | **~4–5%** |
| **Total transaction cost (buyer Rio)** | **~3–4%** |
| Roof renovation | 30,000–100,000 |
| Asbestos abatement (post-2017 ban) | 20,000–80,000 |
| Earthquake retrofit | not standard (low risk) |
| Energy retrofit | 50,000–200,000 |
| Solar PV (5kW) | 25,000–45,000 |
| Reforma completa (apt) | 80,000–250,000 |

## Active fiscal incentives (2025-2026)

- **MCMV (Minha Casa Minha Vida) extension April 2026**:
  - **R$200B total / +R$20B Social Fund**
  - New ceiling: families up to **R$13k/month income** can finance up to **R$600k** properties
  - Mortgage tenor extended to **420 months (35 years)**
  - **Target: 3M units by end-2026** (election year)
- **CHF mortgage** — none specific to BR
- **Pró-Cotista FGTS** for FGTS-paying workers
- **Casa Verde Amarela** archived (replaced by MCMV)

## Common listing platforms

- **ZAP Imóveis + VivaReal** — DOMINANT (merged)
- **Imovelweb**, **OLX Imóveis**
- **Quinto Andar** (no-broker model)
- **DataZAP** analytics
- **Loft** (urban fintech)

## Caveats unique to BR

- **Cartório system**: decentralized + sometimes corrupt + expensive; ownership ONLY transfers on registration
- **Matrícula** = property "birth certificate" with full history
- **CIB ("CPF dos Imóveis") rolling out 2026** — national integration; will expand IPTU tax base
- **Reforma Tributária** 2027 (CBS) → 2029 (IBS) → 2033 (full)
- **MCMV extension April 2026**: R$200B, R$13k/mo income, R$600k cap, 35-year term
- **Multipropriedade** (Brazilian timeshare) — large legal market (Lei 13.777/2018)
- **Foreign rural land caps**:
  - ≤25% of any município's rural land in foreign hands
  - ≤10% per single nationality
  - **MEI (Módulo de Exploração Indefinida) module**: 5-100 ha by ZTM; foreigners can buy up to 3 MEIs without INCRA authorization
  - **Border strip 150km + national-security zones**: presidential/congressional approval
- **Pre-1990 informal tenure**: many favela properties without title
- **Usucapião** (adverse possession) common path
- **Lei 6.815/80** repealed by **Lei de Migração 13.445/2017**
- **STJ 2021 ruling**: condomínios can ban STR — biggest practical Airbnb constraint
- **Petrópolis 2022 + RS 2024 + Juiz de Fora 2026**: recent flood disaster reference
- **47% of national population unassisted by sewage** — massive infrastructure gap
- **Asbestos banned 2017** nationally — earlier buildings likely contain it
- **Currency volatility** — BRL can swing 15-25% vs USD/EUR

## Reddit / forum sources

- **r/brasil** — biggest community
- **r/saopaulo**, **r/rio**, **r/Florianopolis**
- **r/PersonalFinanceBR**
- **InfoMoney**, **Valor Econômico Real Estate**
- **Exame Imóveis**, **G1 Economia**

## Verification authorities

| Authority | When to call |
|---|---|
| **Cartório de Registro de Imóveis** | Title verification, registration |
| **Tabelionato de Notas** | Escritura pública |
| **Município (Prefeitura)** | IPTU + Habite-se + valor venal |
| **Receita Federal (RFB)** | Federal taxes + CIB |
| **INCRA** | Rural land |
| **Estado (Secretaria da Fazenda)** | ICMS + state taxes |
| **Síndico do Condomínio** | If apartment |
| **CEMADEN** | Flood/landslide risk |

## Source URL templates

| Source | URL pattern |
|---|---|
| FIPE-ZAP HPI | `https://www.fipe.org.br/en-us/indexes-and-indicators/fipezap` |
| ZAP Imóveis | `https://www.zapimoveis.com.br/` |
| VivaReal | `https://www.vivareal.com.br/` |
| Quinto Andar | `https://www.quintoandar.com.br/` |
| BCB Real Estate | `https://www.bcb.gov.br/` |
| IBGE | `https://www.ibge.gov.br/` |
| CEMADEN | `https://www.cemaden.gov.br/` |
| CPRM | `https://www.cprm.gov.br/` |
| INMET | `https://www.inmet.gov.br/` |
| ANA | `https://www.ana.gov.br/` |
| INCRA | `https://www.incra.gov.br/` |
| Receita Federal (CIB/SINTER) | `https://www.gov.br/receitafederal/` |
| ONR (cartório integration) | `https://www.onr.org.br/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (FIPE-ZAP Q1 2026), traffic (DNIT VMD), tax (IPTU + ITBI per município + IR + Reforma Tributária 2026-2033), rental (Lei do Inquilinato + STJ 2021 condo STR ban), work (MTE + MEI + Simples), risks (CEMADEN + Petrópolis 2022 + RS 2024 + Juiz de Fora 2026), mains (Marco Legal Saneamento 2033 target).
**Confidence**: HIGH for FIPE-ZAP Q1 2026 figures + Reforma Tributária timeline (Emenda 132/2023 confirmed) + MCMV extension April 2026 (R$200B + R$13k income + R$600k cap + 35yr); HIGH for STJ 2021 condo STR ban; HIGH for CIB rollout 2026 (RFB IN 2.275/2025); MEDIUM for IBS/CBS final real-estate sector rates (pilot 2026, finalization pending).

## Extension TODOs

- [ ] CIB rollout tracker (mid-2026 deadline)
- [ ] Per-município IPTU rates table
- [ ] Per-município ITBI rates table
- [ ] Reforma Tributária real-estate sector rates 2027-2033
- [ ] MCMV eligibility decision tree (R$13k income, R$600k cap)
- [ ] Foreign rural land cap calculation per município (25% + 10% rules)
- [ ] Petrópolis + Rio Grande do Sul flood-zone overlay
- [ ] Favela property regularization (usucapião + REURB)
- [ ] STJ condomínio STR ban tracker
- [ ] Sewage connection per município (Marco Legal target 2033)
