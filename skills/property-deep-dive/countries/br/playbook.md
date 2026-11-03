# Brazil 🇧🇷 — Property Due-Diligence Playbook

ISO2: `br`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CEP)**: 8 digits in `XXXXX-XXX` format (`01310-100` Avenida Paulista, `22070-000` Copacabana, `30130-000` BH centro)
- **Admin levels**: 26 states + DF (Brasília) + 5,569 municípios, plus the Distrito Estadual de Fernando de Noronha — IBGE territorial structure at 30 Apr 2025 (2025 data, source [IBGE Áreas Territoriais](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/15761-areas-dos-municipios.html))
- **Currency**: **BRL** (Brazilian real); BCB PTAX selling rate at the 23 Oct 2026 close: 1 USD = R$5.0377, 1 EUR = R$5.6422; 1–23 Oct 2026 range USD R$4.97–5.22, EUR R$5.58–5.88 (2026 data, source [BCB PTAX](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao))
- **Languages**: Portuguese (official); regional indigenous languages
- **Cadastre — decentralized + transitioning to national**:
  - **Cartórios de Registro de Imóveis** (per-município; ownership only transfers when escritura registered)
  - **Matrícula** = unique property ID (life-of-property record)
  - **CIB (Cadastro Imobiliário Brasileiro) "CPF dos Imóveis"** — national single property identifier, 7 alphanumeric characters + check digit. Instituted by **IN RFB 2.030/2021**; Sinter under **Decreto 11.208/2022**; notarial/registry adoption under **IN RFB 2.275/2025**. **In force from Jan 2026** for federal administration, notarial/registry services and state capitals + DF (LC 214/2025 art. 266 I — 12-month deadline); **state administration + all remaining municipalities from Jan 2027** (art. 266 II — 24 months). Inscription is mandatory for all urban and rural properties and BICE (art. 265), but per the Receita Federal FAQ only urban properties in capitals/DF are obliged during 2026 — other municipalities from Jan 2027; all rural properties must already hold a CIB (via CNIR/Cafir). **Does NOT replace the cartórios** — deeds, land registration and certificate issuance stay with the cartórios, and cadastre upkeep stays with prefeituras (urban) / INCRA (rural); cartórios and municipalities must merely carry the CIB code in their documents (2026 data, 2026-08-07 verified, source: [Receita Federal CIB FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib) + Planalto LC 214/2025)
  - **SINTER** (Sistema Nacional de Gestão de Informações Territoriais)
  - **INCRA** (`https://www.gov.br/incra/pt-br`) — rural land registry
- **Identifier**: matrícula (per-cartório); CIB (national, rolling out)
- **Foreign buyer needs CPF** before any transaction
- **Ownership types**: pleno domínio (full); usufruct; multipropriedade (timeshare, Lei 13.777/2018)

## Section: `--price`

### Primary sources

- **FipeZAP Index** (Fipe + Grupo OLX): `https://www.fipe.org.br/en-us/indexes-and-indicators/fipezap` (PT: `https://www.fipe.org.br/pt-br/indices/fipezap`) — asking prices of ready apartments (apartamentos prontos) listed on the Grupo OLX portals (ZAP, Viva Real, OLX), 56 cities incl. 22 capitals; the 22 capital samples summed to 1,332,233 listings in Sep 2026 (computed from the per-city "Amostra" figures) (2026 data, source [FipeZAP Sep 2026 report](https://downloads.fipe.org.br/indices/fipezap/fipezap-202609-residencial-venda.pdf) + Fipe FipeZAP page)
- **IBGE**: `https://www.ibge.gov.br/` — census (Censo 2022) + household surveys (PNAD Contínua)
- **BCB (Banco Central) Real Estate Market Report**: `https://www.bcb.gov.br/`
- **CBIC (Câmara Brasileira da Indústria da Construção)**

### Listing platforms

- **ZAP Imóveis + VivaReal** — DOMINANT; part of Grupo OLX (OLX Brasil) since it completed the Grupo ZAP purchase on 30 Oct 2020, when OLX Brasil was a 50/50 Adevinta–Prosus joint venture (source: Adevinta press release 30 Oct 2020); their listings feed the FipeZAP index: `https://www.zapimoveis.com.br`, `https://www.vivareal.com.br`
- **Imovelweb** (QuintoAndar group since it bought Navent's real-estate portals, Dec 2021 — secondary: O Globo, CB Insights), **OLX Imóveis** (Grupo OLX): `https://www.olx.com.br/imoveis`
- **Quinto Andar** (rental + sales innovator): `https://www.quintoandar.com.br`
- **DataZAP** (Grupo OLX real-estate data unit, `https://imoveis.grupoolx.com.br/datazap`; datazap.com.br 301-redirects there) for analytics
- **Loft** — proptech expanding into financial products: home equity, a mortgage-credit platform for developers launched May 2026, and rental guarantees (fiança, 20k+ individual contracts a month); 338k purchase, sale and rental transactions in H1 2026, up from 218k in H1 2025, per the company (2026 data, source [Bloomberg Línea Aug 2026](https://www.bloomberglinea.com.br/startups/loft-entra-em-incorporadoras-e-fianca-pj-e-mira-aquisicao-apos-crescer-55-no-semestre/) — secondary, company-reported figures)

### 2026 price benchmarks (FipeZAP, Sep 2026)

| Region | BRL/m² (apt) | YoY |
|---|---:|---:|
| **FipeZAP national (56 cities)** | 10,015 | +5.51% (≈ +1.0% real) |
| **São Paulo avg** | 12,206 | +3.64% (≈ -0.8% real) |
| **São Paulo Itaim Bibi** | 19,989 | +3.4% |
| **São Paulo Pinheiros** | 18,260 | -0.3% |
| **São Paulo Jardins** | 18,028 | +6.7% |
| **São Paulo Santana** | 9,288 | +5.9% |
| **São Paulo Vila Nova Conceição** | not in FipeZAP's published bairro list — verify with DataZAP / listing comps | — |
| **Rio de Janeiro avg** | 11,302 | +5.57% (≈ +1.1% real) |
| **Rio de Janeiro Leblon** | 28,837 | +13.2% |
| **Rio de Janeiro Ipanema** | 26,996 | +10.3% |
| **Brasília avg** | 10,453 | +9.80% |
| **Brasília Sudoeste / Asa Norte / Asa Sul** | 14,672 / 12,706 / 9,354 | +13.4% / +13.1% / +10.0% |
| **Belo Horizonte avg** | 10,686 | +1.97% |
| **Belo Horizonte Savassi** | 17,281 | -1.4% |
| **Curitiba avg** | 11,766 | +1.86% |
| **Florianópolis avg** | 13,607 | +8.31% |
| **Vitória avg** (highest of the 22 capitals) | 15,905 | +11.93% |

FipeZAP measures average **asking** prices of ready apartments listed on the Grupo OLX portals, not transaction prices. YoY is the 12-month change to Sep 2026; "real" deflates it by the inflation proxy the report uses (IPCA for the 11 months to Aug + IPCA-15 for Sep = +4.45%; computed). Bairro rows are FipeZAP's "most representative" bairros: a bairro-wide average, not a value for any given building or unit, and Fipe does not publish full bairro tables (2026 data, source [FipeZAP Sep 2026 report](https://downloads.fipe.org.br/indices/fipezap/fipezap-202609-residencial-venda.pdf))

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
- CIB = national property identifier, phased in Jan 2026 (federal administration + notarial/registry + state capitals & DF) → Jan 2027 (state administration + remaining municipalities)

---

## Section: `--traffic`

### Sources

- **DNIT (Departamento Nacional de Infraestrutura de Transportes)**: `https://www.gov.br/dnit/pt-br` — federal highways (BR-roads); its **PNCT (Plano Nacional de Contagem de Tráfego)** estimates the VMDa for the whole federal road network from traffic counts, origin-destination surveys and a traffic model (source: DNIT PNCT presentation, 2016)
- **DERSP (SP), DER-RJ, DER-MG, etc.** — state-level
- **CET-SP** (`https://www.cetsp.com.br/`) and **CET-Rio** (`https://cetrio.prefeitura.rio/`) — municipal traffic-engineering companies (traffic operations, studies, city traffic data)

### Key term

**VMD (Volume Médio Diário)** = AADT-equivalent; DNIT's annual figure is the **VMDa** — the mean of all daily volumes recorded at a road section over a year (DNIT traffic-count manual, 2008).

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
| **São Paulo** | ~0.7–1.5% | ~1.1–1.9% |
| **Rio de Janeiro** | ~0.6–1.2% | ~1.0–1.5% |
| **Brasília** | ~0.3–1.0% | ~1.0–1.5% |
| **Belo Horizonte** | ~0.6–1.2% | ~1.0–1.5% |

- Rates above are **indicative ranges (est., c. 2025)** — verify the current rate against each município's IPTU legislation and annual reajuste decree (e.g. São Paulo via prefeitura.sp.gov.br) — rates/figures may have changed since. São Paulo residential checked: 1.0% base rate plus a per-bracket desconto/acréscimo on the valor venal (−0.3% up to R$150k, −0.1% R$150k–300k, +0.1% R$300k–600k, +0.3% R$600k–1.2M, +0.5% above R$1.2M), so marginal rates run 0.7–1.5% (computed); non-residential built property 1.5% base (Lei 6.989/1966 arts. 7-8 + Lei 15.889/2013 table as consolidated in Decreto 57.516/2016; later amendments not checked; source: [Prefeitura SP — Decreto 57.516/2016 annex](https://legislacao.prefeitura.sp.gov.br/decreto-57516-de-08-de-dezembro-de-2016/anexo/63c04df614119226dfe7582c/Anexo%20do%20Decreto%20n%C2%BA%2057.516_2016.pdf))
- Base = **valor venal** (typically 30-60% below market)
- Annual or 10x monthly installments
- **Early payment 4-10% discount**

### Transaction taxes — ITBI

**Imposto sobre Transmissão de Bens Imóveis** — municipal:

| Município | ITBI rate |
|---|---:|
| **São Paulo** | **3%** (Lei Municipal SP 11.154/1991 Art. 10) of declared transaction value; SFH / PAR / HIS / consórcio purchases of properties up to R$725,808 pay 0.5% on the financed part up to R$120,968 and 3% on the rest (limits for financing contracted from 1 Jan 2026) (2026-11-03 verified, source: [Prefeitura SP — Cálculo do ITBI](https://prefeitura.sp.gov.br/web/fazenda/w/servicos/itbi/2513)) |
| **Rio de Janeiro** | **3%** for instruments executed from 1 Jan 2018 (Lei Municipal RJ 1.364/1988 art. 19 II as reworded by Lei 6.250/2017; 2% before) (2026-11-03 verified, source: [SMF Rio — Cálculo do ITBI](https://fazenda.prefeitura.rio/calculo-itbi)); reduced rates or exemptions for financed housing not confirmed — verify at Carioca Digital › ITBI › Imunidade, Isenção e Não Incidência |
| Other municípios | 2–3% |

- **STJ Tema Repetitivo 1.113 (REsp 1.937.821/SP, Feb 2022)**: ITBI base = the **declared transaction value** (presumption of truth). The "valor venal de referência" (VVR) used unilaterally by São Paulo is unlawful as an automatic basis; municipality must challenge via administrative procedure. Buyers in SP routinely seek refunds where ITBI was paid on VVR rather than price (2026-05-27 verified, source: STJ Tema 1.113 / REsp 1.937.821/SP). The São Paulo prefeitura's ITBI page still states the base as the higher of transaction value and VVR (2026-11-03 verified, source: [Prefeitura SP — Cálculo do ITBI](https://prefeitura.sp.gov.br/web/fazenda/w/servicos/itbi/2513)). **LC 227/2026** added CTN art. 38 §§ 1-3: valor venal is the price the property would fetch for cash in normal market conditions, estimated by technical criteria each município must publish, and the taxpayer can contest it with a counter-valuation in a specific procedure (2026-11-03 verified, source: [Planalto CTN compilado](https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm)). Municípios argue this overrides Tema 1.113. In the TJSP rulings reported by ConJur, São Paulo's VVR was not upheld: the 14ª Câmara de Direito Público held that LC 227/2026 does not allow automatic use of VVR without an administrative procedure, while the 18ª Câmara read §§ 2-3 as partly superseding Tema 1.113 but still decided against the município because São Paulo's VVR articles had been declared unconstitutional (secondary: ConJur, 8 Oct 2026) — the point is disputed.

### Other taxes

- **ITR (Imposto Territorial Rural)**: rural; federal; INCRA-administered
- **ITCMD (Imposto sobre Transmissão Causa Mortis e Doação)** — state-level inheritance + lifetime-gift tax (separate from ITBI which is municipal + onerous-transfer-only). Constitutional ceiling **8%** (Resolução Senado Federal nº 9/1992). Indicative 2025 rates: SP 4% flat (Lei 10.705/2000); RJ 4–8% progressive (Lei 7.174/2015); MG 5% flat (Lei 14.941/2003); DF 4–6% progressive. **EC 132/2023 amended CF Art. 155 §1º VI to make ITCMD progressivity MANDATORY** (previously optional under STF RE 562.045/2013); EC 132/2023 Art. 23 III imposes a transitional immediate-implementation rule — flat-rate states face pending constitutional-incompatibility litigation risk (2026-05-27 verified, source: Senado Federal Resolução 9/1992 + EC 132/2023 text via Planalto + ConJur "Adesão dos estados às regras de ITCMD" May 2024). **LC 227/2026 art. 156** (13 Jan 2026) requires progressive ITCMD rates by the value of the quinhão, legado or doação, applied slice by slice, within the Senate ceiling; under art. 158 I, ITCMD on real estate in Brazil is due to the state where the property lies even if the deceased or donor lived abroad (2026-11-03 verified, source: [Planalto LC 227/2026](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm)). Flat rates still applied in Oct 2026 include SP 4% (PL 409/2025 pending at ALESP), MG 5% (PL 2.881/2024 pending), PR 4% and ES 4% (secondary: law-firm surveys of state laws, Jul–Oct 2026; verify with the state Sefaz).
- **IR (Imposto de Renda) ganho de capital**:
  - Residents AND non-residents: progressive **15% / 17.5% / 20% / 22.5%** at gains ≤ R$5M / R$5M–R$10M / R$10M–R$30M / > R$30M (Lei 13.259/2016 — progressivity extended to non-residents from 2017; "flat 15%" is the pre-2017 rule) (2026-05-27 verified, source: Planalto Lei 13.259/2016)
  - **R$35k small-value exemption** (Lei 9.250/1995 art. 22 II, as reworded by Lei 11.196/2005) covers gains on any bens e direitos, real estate included, when the sale price of the asset — or of all assets of the same nature sold in the same month (Receita groups urban property with bare land) — is ≤ R$35,000; for an SFH-financed property only the amount received counts, not the debt transferred to the buyer (2026-11-03 verified, source: [Planalto Lei 9.250/1995](https://www.planalto.gov.br/ccivil_03/leis/l9250.htm) + [Receita Federal — Operações não sujeitas ao ganho de capital](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/ganhos-de-capital/operacoes-nao-sujeitas) + Receita IRPF Perguntas e Respostas 2024 q. 655)
  - **R$440k "isenção do único imóvel"** (Lei 9.250/1995 art. 23) — the only property the seller owns (the article does not limit it to residential), sale price ≤ R$440,000, and no other alienação in the previous 5 years (2026-11-03 verified, source: [Planalto Lei 9.250/1995](https://www.planalto.gov.br/ccivil_03/leis/l9250.htm))
  - **180-day rollover (Lei 11.196/2005 art. 39)** — the gain of an individual **resident in Brazil** on the sale of residential property is exempt if the proceeds buy residential property located in Brazil within 180 days of the sale contract; partial reinvestment is taxed pro rata on the part not applied (§ 2); once every 5 years (§ 5); the article covers residents only (2026-11-03 verified, source: [Planalto Lei 11.196/2005](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11196.htm))
- **IRPF 2026 filing window**: 23 March – 29 May 2026 (IN RFB 2.312/2026; closed); each year's window is set by a new Instrução Normativa (2026-11-03 verified, source: [Receita Federal — Prazo de entrega](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/prazo))

### Cartório fees

- **Escritura**: ~0.5–2% of price (est. — set per-state; verify against the relevant tabela de emolumentos)
- **Registro**: ~0.5–1% of price (est. — set per-state; verify against the relevant tabela de emolumentos)
- **Combined**: ~1–2% mandatory closing

### Total transaction cost (buyer side)

- São Paulo standard: **~4–5%** (3% ITBI + 1-2% cartório)
- Rio standard: **~4–5%** (3% ITBI + 1-2% cartório; computed)
- Plus optional valuation, lawyer, mortgage costs

### Future risk — REFORMA TRIBUTÁRIA

**Emenda Constitucional 132/2023** + **Lei Complementar 214/2025** (implementing statute, sanctioned January 2025) — major tax reform:
- **2026: TEST YEAR** — CBS **0.9%** + IBS **0.1%** = **1.0% combined test rate** (amounts paid are offset against PIS/COFINS under ADCT art. 125 § 1, and LC 214/2025 art. 348 § 1 waives payment of 2026 IBS/CBS for taxpayers who meet the ancillary obligations, who stay liable for full PIS/COFINS)
- **2027: CBS** goes live; CBS replaces **PIS + COFINS** (federal contributions) — **NOT IPI** (IPI is preserved but its rates are reduced to zero from 2027 except for products whose industrialisation is incentivised in the Zona Franca de Manaus — ADCT art. 126 III, inserted by EC 132/2023 art. 2; EC 132 does not amend CF art. 153 § 3); the TCU calculated the 2027 CBS reference rate at **11.3%** on 28 Oct 2026, pending the Senate resolution due 15 Dec 2026 (LC 214/2025 art. 349 § 1 II as extended by art. 353 § 2); if 11.3% stands, the CBS charged in 2027 is 11.2% (that rate minus 0.1 pp, art. 347; computed), and the 2028 rate is fixed separately (2026-10-28 verified, source: [TCU — CBS 2027](https://sites.tcu.gov.br/reforma-tributaria/visao-cbs-2027.html))
- **2029: IBS** (state+municipal, replaces ICMS/ISS) takes over as ICMS/ISS rates fall to 9/10 (2029), 8/10 (2030), 7/10 (2031) and 6/10 (2032) of their own statutory rates, both extinct from 2033 (ADCT arts. 128-129); IBS is already charged at 0.1% state in 2026 and at 0.05% state + 0.05% municipal in 2027-2028 (ADCT arts. 125 and 127)
- **2033: full system in place** — the 26.5% combined CBS+IBS figure is a review trigger, not a hard ceiling: if the five-year evaluation estimates 2033 reference rates summing above it, the Executive must send Congress a complementary-law bill to bring them down (LC 214/2025 art. 475 §§ 10-11) (2026-10-28 verified)
- **Real estate sector reductions (LC 214/2025 Art. 261)** (2026-11-03 verified, source: [Planalto LC 214/2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm)):
  - **50% reduction** on standard rate for compra/venda + cessão de direitos sobre imóveis (art. 261 caput); in 2027-2028 the CBS part is 50% × (CBS rate − 0.1 pp), i.e. 5.6% if the TCU's 11.3% stands (computed: 50% × 11.2%; art. 347 § 1 I), plus the IBS test rate (art. 344); the full rate from 2033 is 50% of the combined CBS+IBS reference rates, not yet fixed
  - **70% reduction** for locação, cessão onerosa, arrendamento (art. 261 sole para.); in 2027-2028 the CBS part is 30% × (CBS rate − 0.1 pp), i.e. 3.36% if the TCU's 11.3% stands (computed: 30% × 11.2%), plus the IBS test rate (art. 344); the full rate from 2033 is 30% of the combined reference rates, not yet fixed
  - **40% reduction** for residential lets of no more than 90 consecutive days by a regular-regime taxpayer, taxed under the hotelaria rules (arts. 253 and 281); an individual is caught only if they meet the art. 251 letting tests, and these short lets count toward those limits (art. 253 §§ 1-2, added by LC 227/2026)
- **Pessoa-física threshold** (LC 214/2025 art. 251 §§ 1-3): an individual becomes a regular IBS/CBS taxpayer on lettings when prior-year letting receipts exceed R$240,000 (IPCA-indexed) **and** cover more than 3 distinct properties — both are required; on sales, when in the prior year they sold more than 3 properties held under 5 years, or more than 1 self-built property within 5 years of building it; and within the current year once sales pass those limits or letting receipts exceed the R$240,000 limit by 20% (art. 251 § 2); for the sales test, property received by inheritance, gift or meação counts its 5 years from the earlier owner's acquisition (art. 251 §§ 3-4) (2026-11-03 verified)
- **Redutor social** (regular-regime taxpayers only): R$100,000 per new residential unit or R$30,000 per residential lot deducted from the IBS/CBS base on sale (art. 259); R$600 per month per property on residential lettings, IPCA-indexed monthly (art. 260 as reworded by LC 227/2026) (2026-11-03 verified, source: Planalto LC 214/2025)
- **IPTU/ITBI/IR rates NOT changed** by the IBS/CBS reform (LC 227/2026 did rewrite the CTN ITBI chapter, including the art. 38 valor-venal rule above) — and the **CIB is an identifier layer, not a valuation authority**: cadastre upkeep stays with the prefeituras (urban) / INCRA (rural), and cartórios and municipalities merely carry the CIB code in their documents, so any IPTU/ITBI base movement still depends on each município updating its own outdated valor venal (2026-08-07 verified, source: [Receita Federal CIB FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib))

---

## Section: `--rental`

### Long-term residential

- **Lei do Inquilinato (Lei 8.245/1991)** — federal, governs all rental
- **Tenant protection moderate** (less strict than Argentina, more than US)
- **Tenant** may end an indefinite-term lease on 30 days' written notice (art. 6). **Landlord**: a written lease of 30+ months ends at term; if the tenant stays on, the landlord may end it at any time with 30 days to vacate (art. 46 § 2). A lease under 30 months rolls over indefinitely and the landlord can retake only on art. 47 grounds (e.g. own or family use, art. 47 III, or once the lease has run 5 years uninterrupted, art. 47 V). A buyer of a let property may end the lease with 90 days to vacate unless it is fixed-term with a sale-continuation clause registered on the matrícula (art. 8) (source: Planalto Lei 8.245/1991)
- **Guarantees**: caução, fiança (**fiador** — common), seguro-fiança or assignment of investment-fund quotas — only one per lease (art. 37)
- **Caução** in cash capped at 3 months' rent, held in a poupança account with the yield going to the tenant (art. 38 § 2)

### Short-let (Airbnb)

- **Lei do Inquilinato** defines "locação para temporada" as a lease of up to **90 days**, furnished or not (art. 48); the landlord may take the rent up front (art. 49)
- Federally legal; **no national permit**
- **STJ — condomínio consent is the dominant restriction**: on 7 May 2026 the Segunda Seção (REsp 2.121.055) held that where units are designated residential, short stays via Airbnb-type platforms need the destination changed by an assembly vote of at least two-thirds of the condôminos (Código Civil arts. 1.336 IV and 1.351); the convenção need not ban STR expressly, and the ruling unifies the line of the 2021 decisions (4ª Turma, REsp 1.819.075, 20 Apr 2021). In Sep 2026 the Segunda Seção took REsps 2.272.537 and 2.272.536 as repetitive appeal **Tema 1.443** (does a residential-destination clause suffice, or is an express ban needed?) and suspended related cases nationwide — binding thesis pending (2026 data, source: [STJ 7 May 2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/07052026-Oferta-de-imovel-em-plataformas-como-Airbnb-exige-aprovacao-do-condominio--define-Segunda-Secao.aspx) + [STJ 17 Sep 2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/17092026-Airbnb-afetacao-de-repetitivo-sobre-locacao-de-curta-temporada-em-condominios-suspende-processos-em-todo-o-pais.aspx))
- **Rio de Janeiro**: no specific municipal STR regulation in force; a bill filed at the Câmara Municipal in May 2026 (vereador Salvino Oliveira) would create a host cadastre at the Prefeitura, require platforms to supply data for tax enforcement and charge ISS (2026 data, source: Diário do Rio May 2026 + G1 28 Jul 2026 — secondary; verify status at the Câmara Municipal do Rio)
- **Florianópolis**: no official listing count, and third-party trackers disagree by scope and definition — BnBCalc: 14,458 active Airbnb + Vrbo listings (12-month average to Sep 2026); GuestFavorites: 19,753 active Airbnb listings in the city and 33,259 across its 17-municipality Florianópolis region incl. São José and Palhoça (page updated 2 Nov 2026) (2026 data, secondary aggregators — verify with AirDNA); only Lei do Inquilinato + condomínio rules
- **No federal residency requirement**; secondary-home owners can legally STR
- **Federal STR bills** in Congress pull in opposite directions: one lets condomínios ban STR through the convenção, the other bars such bans and limits state and municipal rules (2026 data, source G1 28 Jul 2026 — secondary)

### Tax on rental

- **IR (income tax)** progressive on net rental — the 2026 monthly table tops out at 27.5% above a R$4,664.68 base; Lei 15.270/2025 adds a monthly reduction that zeroes the tax on monthly taxable income up to R$5,000 and phases out at R$7,350 (2026 data, source [Receita Federal — Tributação de 2026](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026))
- Non-residents: 15% IRRF withheld on rent from property in Brazil (RIR/2018, Decreto 9.580/2018, art. 763); 25% where the beneficiary is resident in a tax-favoured jurisdiction (Lei 9.779/1999 art. 8 — verify its application to rent at Receita Federal)
- IPTU falls on the landlord unless the lease expressly shifts it to the tenant (Lei 8.245/1991 art. 22 VIII) — shifting it is common
- From 2027 a landlord who meets the LC 214/2025 art. 251 test also owes IBS/CBS on lettings — see `--tax` › Reforma Tributária

---

## Section: `--work=<profession>`

### Sources

- **MTE (Ministério do Trabalho e Emprego)**: `https://www.gov.br/trabalho-e-emprego/pt-br` (the old `gov.br/trabalho/` path redirects there)
- **Catho** — biggest job board: `https://www.catho.com.br/vagas`
- **Indeed** (`br.indeed.com`; indeed.com.br 301-redirects there), **Vagas.com.br**, **InfoJobs**, **LinkedIn BR**
- **CRECI** for realtors; **CONFEA/CREA** for engineering

### Self-employment

- **MEI (Microempreendedor Individual)**: simplified regime; annual gross revenue cap **R$81,000 in 2026**, rising to **R$110,000 for 2027** (LC 238/2026 art. 2) and **R$140,000 from 2028** (LC 123/2006 art. 18-A § 1 as reworded by LC 238/2026, in effect from 1 Jan 2028 per art. 10 I); from 1 Jan 2027 a MEI may also employ up to 2 people paid the minimum wage or the category floor (LC 123 art. 18-C as amended; LC 238 art. 10 II) (2026 data, source [Planalto LC 238/2026](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp238.htm) + Senado Notícias 21 Oct 2026)
- **Simples Nacional**: small business, annual gross revenue up to R$4.8M (LC 123/2006 art. 3 II, as amended by LC 155/2016)
- **CPF** required for foreigners
- **CNPJ** for business
- **PIS/COFINS** federal contributions — extinguished from 2027 and replaced by the **CBS** (ADCT art. 126 II, inserted by EC 132/2023); the 2027 CBS rate depends on the Senate resolution — see `--tax` › Reforma Tributária

### Salary benchmarks (2026)

- **IBGE average real monthly income from all jobs** (PNAD Contínua, employed people aged 14+, habitual earnings; survey averages that include informal work — not medians, not pay for a given profession): **R$3,738** national in Q2 2026; Sul R$4,238, Centro-Oeste R$4,362, Nordeste R$2,645 (2026 data, source [IBGE PNAD Contínua trimestral, Q2 2026](https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/47774-pnad-continua-trimestral-desocupacao-cai-em-13-das-27-ufs-no-2-trimestre-de-2026))
- **Distrito Federal** had the highest state average in Q1 2026, R$6,720 against R$3,722 national; Maranhão the lowest, R$2,240 (2026 data, source Agência Brasil 14 May 2026, reporting IBGE PNAD Contínua — secondary). São Paulo and Rio de Janeiro state averages are not in the release text — verify at IBGE SIDRA (PNAD Contínua trimestral)
- City pay ranges carried from the 2025 pass (unsourced estimates, not medians; verify per profession on the job boards above) — rates/figures may have changed since:
  - São Paulo: ~R$5,000–R$10,000 (≈ €890–€1,770 at the 23 Oct 2026 PTAX of R$5.6422/€; computed)
  - Rio de Janeiro: ~R$4,500–R$9,000
  - Brasília (govt): ~R$6,000–R$12,000
  - Smaller cities: ~R$3,000–R$5,500
- **Salário mínimo**: **R$1,621/month (2026)** (R$54.04/day, R$7.37/hour), set under Lei 14.663/2023 and Lei 15.077/2024 by Decreto nº 12.797 of 23 Dec 2025 (DOU 24 Dec 2025), in force 1 Jan 2026; the 2025 value was R$1,518, so the rise is 6.79% (computed) (2026 data, source: [Planalto Decreto 12.797/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12797.htm))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **CEMADEN** | `https://www.gov.br/cemaden/pt-br` | Flood + landslide early warning (created by Decreto 7.513/2011, operational since 2 Dec 2011); monitors 1,295 municipalities with 3,800+ automatic rain gauges, public on its Mapa Interativo (2026 data, source: Cemaden + MCTI) |
| **SGB — Serviço Geológico do Brasil (CPRM)** | `https://www.sgb.gov.br/` | Geology, geological hazards, hydrological alert bulletins (river levels) |
| **INMET** | `https://portal.inmet.gov.br/` | Weather, climate |
| **IBAMA** | `https://www.ibama.gov.br/` | Environmental |
| **ANA (Agência Nacional de Águas e Saneamento Básico — renamed by Lei 14.026/2020)** | `https://www.gov.br/ana/pt-br` | Water management; reference norms for sanitation regulation |

### Specific risks

- **Flooding + landslide** — major risk:
  - **Petrópolis 15 Feb 2022**: 250 mm in 3 hours (16:20–19:20; 259.8 mm over the day) per Cemaden; 233 deaths with 4 still missing in the Prefeitura's 4 Mar 2022 bulletin — the deadliest disaster recorded in the city's history (2022 data, secondary: UOL Tilt citing Cemaden; G1 citing the Prefeitura) — rates/figures may have changed since
  - **Rio Grande do Sul May 2024 floods** — 478 municipalities and 2,398,255 people affected, 185 confirmed deaths, 23 missing; displaced people peaked at 581,638 on 19 May 2024 (2024 data, source: Defesa Civil RS final balance, last updated 2025-08-19, sosenchentes.rs.gov.br) — rates/figures may have changed since
  - **Feb 2026 Zona da Mata floods**: Juiz de Fora logged 752.4 mm in February 2026, 342% above the climatological mean (≈4.4× the February normal of 170.3 mm; computed) — the wettest month of the INMET series begun in 1961 (previous record Jan 1985, 714 mm); 65 deaths and 8,500+ people made homeless or displaced in the city (2026 data, source: INMET February 2026 note, 11 Mar 2026; series record, normal and toll per G1 1 Mar 2026 citing INMET, secondary)
  - 17 rain gauges in Petrópolis since 2015 (CEMADEN) — figures may have changed since
- **Drought**: Northeast (sertão) — chronic
- **Rainforest fire**: Amazonas — volatile: a record 25,499 heat spots in 2024, then 4,545 in 2025 (−82.2%), the lowest of the 2003–2025 series (2025 data, source: SEMA-AM PPCDQ-AM 2026-2028, from INPE satellite data)
- **Cyclones**: tropical cyclones are very rare in the South Atlantic — Catarina (28 Mar 2004, Santa Catarina coast) is the only hurricane-strength storm on record there; subtropical and extratropical cyclones are common in the South Atlantic (secondary: Wikipedia "Ciclones do Atlântico Sul"; Wikinotícias 2024)
- **Earthquake risk LOW** (stable Brazilian shield)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990** | Asbestos common (chrysotile banned nationwide by the STF in 2017: art. 2 of Lei 9.055/1995 struck down Aug 2017, binding on all Nov 2017, upheld Feb 2023); lead paint (federal cap 600 ppm from Lei 11.762/2008; Lei 15.441/2026, DOU 29 Jun 2026, cuts it to 90 ppm from 12 months after publication and revokes the 2008 law) |
| **Pre-1990 informal tenure** | Many favela properties without title |
| **1980s–2000s "casa-grande" reforma** | Variable construction quality |
| **Post-2000** | NBR codes tightened; the NBR 15575 performance standard (acoustics, thermal comfort, durability) sets a mandatory minimum level for new residential buildings not legally started before 19 Jul 2013 (renovations and retrofits excluded) — a technical norm without force of law, usable as the benchmark in court claims (2013 data, source: CBIC, industry body) — rates/figures may have changed since |
| **Post-2017 asbestos ban** | Modern materials |

### Mandatory at sale

| Document | Required because | Notes |
|---|---|---|
| **Certidão de matrícula atualizada** | Title (≤30 days) | Cartório de Registro de Imóveis; the deed needs the registry's certidões of ônus reais and of ações reais e pessoais reipersecutórias, valid 30 days (Decreto 93.240/1986 art. 1 IV) |
| **Certidão negativa de ônus reais** | No-liens | Same |
| **Certidão negativa de débitos** | Federal (RFB), estadual, municipal (IPTU paid) | Multiple authorities |
| **Certidão de regularidade do condomínio** | No condo arrears | If apartment |
| **Habite-se** | Occupancy permit | Municipal |
| **IPTU + valor venal certificate** | Tax base | Municipal |
| **Personal certidões on seller** | CND federal, criminal, trabalhista, civil, tributária | Multiple — court-distribution certidões (forenses) are not required for the sale's validity or the buyer's good faith (Lei 13.097/2015 art. 54 § 2 II, inserted by Lei 14.382/2022), so requesting them is a buyer choice |
| **Escritura pública** | At Tabelionato de Notas | Notary |
| **Registration at Cartório de Registro de Imóveis** | ONLY step that transfers ownership | CRITICAL |

### Climate change projections

- **~+2.0–4.0°C** by 2100 (est. — projection range; verify against IPCC AR6 / PBMC regional scenario for the relevant SSP/RCP pathway)
- **Amazon deforestation** + drying — global tipping point concern
- **Coastal sea-level rise**: **~+30–80 cm** by 2100 (Recife, Santos, Fortaleza vulnerable) (est. — projection range; verify against IPCC AR6 / PBMC regional scenario)
- **Drought intensification**: Northeast + Cerrado
- **Increased extreme rainfall** (Petrópolis 2022 type)

---

## Section: `--mains`

### Sources

- **SABESP** (SP): `https://www.sabesp.com.br/`
- **CEDAE** (Rio state): `https://www.cedae.com.br/` — since the 2021 concession auctions (4 blocks: Águas do Rio blocks 1 and 4, Iguá block 2, Águas do Brasil block 3) the private concessionaires run distribution, sewage and billing; CEDAE keeps water production for the metropolitan region (Guandu and other systems) and full service in the 15 interior municipalities that stayed out (source: CEDAE "O que mudou?")
- **COPASA** (MG — privatized in 2026: Grupo Equatorial's Gerais Saneamento bought 30% in the desestatização, cleared by CADE on 5 Aug 2026), **SANEPAR** (PR), state operators
- **ANA** — federal agency that issues reference norms for sanitation regulation; the services themselves are regulated by the titulares' state / municipal regulatory agencies (Lei 9.984/2000 as amended by Lei 14.026/2020)
- **Marco Legal do Saneamento (Lei 14.026/2020)**: service contracts must target 99% of the population with drinking water and 90% with sewage collection and treatment by 31 Dec 2033; regionalised provision may extend to 1 Jan 2040 where universalization by 2033 is shown economically unviable, with the regulator's prior consent (Lei 11.445/2007 art. 11-B caput and § 9) (2026-11-03 verified, source: Planalto Lei 11.445/2007)

### Verification

- **Sewage gap**: 62.3% of the population is served by a sewage collection network (117.3 M people) and 51.8% of the sewage generated is treated; water network coverage is 84.1% (2024 data, source: Ministério das Cidades SINISA 2025 Esgotamento Sanitário and Abastecimento de Água reports; SINISA-Esgoto participants cover 81.7% of the population) — rates/figures may have changed since. Instituto Trata Brasil's own national calculation from the same SINISA data gives 56.7% collection — about 90 million people (43.3%) without sewage collection (2024 data, secondary: Trata Brasil Ranking do Saneamento 2026) — rates/figures may have changed since
- RJ ~15% unconnected; CEDAE-contracted municípios only 39.2% actually connected (unsourced, year unknown — figures may have changed since; verify against SINISA municipal indicators)
- **SABESP** (privatized 2024): the concession plan budgets ~R$70bn of investment to 2029 (R$68bn at Dec-2022 prices) and brings the universalization targets forward from 2033 to 2029 (2023 data, source: São Paulo state desestatização presentation to CONSEMA, Mar 2024 — rates/figures may have changed since); SABESP restated the 2029 target in 2026 (secondary: Estadão, Fórum Estadão Loteamento Urbano 2026)
- **Favelas**: fossas (cesspits) common; informal connections widespread
- **Per-município coverage extremely uneven**

### Costs

| Scenario | Cost (BRL, est.) |
|---|---:|
| Mains connection | 5,000–25,000 |
| Septic upgrade | 8,000–30,000 |
| Cisterna installation | 15,000–60,000 |
| Bored well | 25,000–80,000 |

Costs above are indicative ranges (est., c. 2026) with no national price source — get the concessionária's connection quote and local contractor quotes.

---

## Cost benchmarks (BR 2026)

| Work | Cost (BRL) |
|---|---:|
| Vistoria (inspection) | 1,000–3,000 |
| Avaliação | 2,000–6,000 |
| Cartório fees (escritura + registro) | 1–2% of price |
| ITBI (SP) | 3% (prefeitura applies the higher of price and VVR; STJ Tema 1.113 sets the declared price — see `--tax`) |
| ITBI (Rio) | 3% (since 1 Jan 2018, Lei 6.250/2017) |
| **Total transaction cost (buyer SP)** | **~4–5%** |
| **Total transaction cost (buyer Rio)** | **~4–5%** (computed: 3% ITBI + 1–2% cartório) |
| Roof renovation | 30,000–100,000 |
| Asbestos abatement (post-2017 ban) | 20,000–80,000 |
| Earthquake retrofit | not standard (low risk) |
| Energy retrofit | 50,000–200,000 |
| Solar PV (5kW) | 25,000–45,000 |
| Reforma completa (apt) | 80,000–250,000 |

Inspection, valuation and works rows are est. (no published tariff; quotes vary by city and specification) — verify with local quotes.

## Active fiscal incentives (2025-2026)

- **MCMV (Minha Casa Minha Vida) extension April 2026** (2026-11-03 verified, source: [Ministério das Cidades — MCMV Classe Média](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/habitacao/programa-minha-casa-minha-vida/minha-casa-minha-vida-classe-media/minha-casa-minha-vida-classe-media-1) + [Agência Brasil, 15 Apr 2026](https://agenciabrasil.ebc.com.br/politica/noticia/2026-04/aportes-para-mcmv-sao-ampliados-para-r-200-bilhoes)):
  - **R$200B total / +R$20B Social Fund**
  - New ceiling (Faixa 4 / Classe Média): families up to **R$13k/month gross income** (Portaria MCID 333 of 30 Mar 2026) can finance new or used homes up to **R$600k** at 10.00% nominal a year; buyers must not own another property or hold an active housing loan; used homes in the South and Southeast are capped at 60% of value
  - Maximum term **420 months (35 years)**
  - **Target: 3M units contracted by end-2026** (election year); more than 2.7M contracted per a 2026 Ministério das Cidades release
- **CHF mortgage** — none specific to BR
- **Pró-Cotista FGTS** for FGTS-paying workers
- **SFH / poupança funding model** (Res. CMN 5.254 + 5.255 of 10 Oct 2025): the SFH property-value ceiling rose from R$1.5M to R$2.25M in Oct 2025; from 1 Jan 2027 the share of poupança deposits banks must lend for housing rises gradually from 65% towards 100% as the pre-2027 portfolio amortises, with 80% of it in SFH loans under the 12% a year interest cap (source: [Voto CMN 64/2025](https://normativos.bcb.gov.br/Votos/CMN/202564/Voto_do_CMN_64_2025.pdf) + [Casa Civil, 10 Oct 2025](https://www.gov.br/casacivil/pt-br/assuntos/noticias/governo-anuncia-novo-modelo-de-credito-imobiliario)). In Aug 2026 banks said they would ask the BCB for a one-year deferral and a review of the 12% cap (secondary: Valor Econômico via Let's Money, 20 Aug 2026); no deferral decision found as of 2026-11-03. Relevant to buyers financing through SFH or FGTS
- **Casa Verde Amarela** archived (replaced by MCMV)

## Common listing platforms

- **ZAP Imóveis + VivaReal** — DOMINANT (Grupo OLX since Oct 2020)
- **Imovelweb** (QuintoAndar group since Dec 2021), **OLX Imóveis** (Grupo OLX)
- **Quinto Andar** (no-broker model)
- **DataZAP** analytics (Grupo OLX)
- **Loft** (property credit + rental guarantees)

## Caveats unique to BR

- **Cartório system**: decentralized + sometimes corrupt + expensive; ownership ONLY transfers on registration
- **Matrícula** = property "birth certificate" with full history
- **CIB ("CPF dos Imóveis") phased in Jan 2026 → Jan 2027** — in force Jan 2026 for federal administration, notarial/registry services and state capitals + DF; state administration + all remaining municipalities from Jan 2027 (LC 214/2025 art. 266 I / II); all rural properties must already hold a CIB (via CNIR/Cafir). It is a national *identifier* only — it does **NOT** replace the cartórios (deeds, land registration and certidões unchanged) and cadastre upkeep stays with prefeituras (urban) / INCRA (rural) (2026-08-07 verified, source: [Receita Federal CIB FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib) + Planalto LC 214/2025)
- **Reforma Tributária** 2027 (CBS) → 2029 (IBS) → 2033 (full)
- **MCMV extension April 2026**: R$200B, R$13k/mo income, R$600k cap, 35-year term
- **Multipropriedade** (Brazilian timeshare) — large legal market (Lei 13.777/2018)
- **Foreign rural land caps** (statute: **Lei 5.709/1971** + Decreto 74.965/1974):
  - Foreign-owned rural land ≤ 25% of any município's surface; one nationality ≤ 40% of that limit, i.e. 10% of the município (computed) (Art. 12 + § 1); holdings under 3 MEI are excluded from these caps (Art. 12 § 2 I)
  - **Módulo de Exploração Indefinida (MEI, Lei 5.709/1971 Art. 3º — NOT to be confused with Microempreendedor Individual)**: foreign natural persons can buy up to **3 MEIs** freely, without authorization (Art. 3 § 1); 3–50 MEIs under Executive rules (Art. 3 § 2); **50 MEIs maximum** per foreign natural person, contiguous or not (Art. 3 caput); per-município MEI size set by INCRA Normative Instructions (varies by zone; verify the município's figure with INCRA)
  - Foreign legal entities may acquire rural land only for agricultural, livestock, industrial or colonisation projects tied to their statutory objects, with the project approved by the Ministry of Agriculture (Art. 5 + § 1)
  - **Border strip 150 km** (Lei 6.634/1979 art. 1 + CF art. 20 § 2): any rural-property transaction giving a foreigner ownership, possession or another real right needs the prior assent (assentimento prévio) of the national-security council's secretariat (art. 2 V + § 1); without it the act is void and a fine of up to 20% of the declared value applies (art. 6)
  (2026-11-03 verified, source: [Planalto Lei 5.709/1971](https://www.planalto.gov.br/ccivil_03/leis/l5709.htm) + [Planalto Lei 6.634/1979](https://www.planalto.gov.br/ccivil_03/leis/l6634.htm) + CF art. 20 § 2)
- **Pre-1990 informal tenure**: many favela properties without title
- **Usucapião** (adverse possession) common path
- **Lei 6.815/80** repealed by **Lei de Migração 13.445/2017**
- **STJ condomínio consent — biggest practical Airbnb constraint**: economic or professional short-stay use of units in a condomínio designated residential needs the destination changed by an assembly vote of at least two-thirds of the condôminos (Segunda Seção, REsp 2.121.055, 7 May 2026); Tema 1.443 (repetitive appeals on whether the residential clause alone bars platform short lets) is pending, with cases suspended nationwide (2026 data, source: [STJ 7 May 2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/07052026-Oferta-de-imovel-em-plataformas-como-Airbnb-exige-aprovacao-do-condominio--define-Segunda-Secao.aspx) + [STJ 17 Sep 2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/17092026-Airbnb-afetacao-de-repetitivo-sobre-locacao-de-curta-temporada-em-condominios-suspende-processos-em-todo-o-pais.aspx)) — see `--rental`
- **Petrópolis 2022 + RS 2024 + Juiz de Fora 2026**: recent flood disaster reference
- **Sewage gap**: only 62.3% of the population is served by a sewage collection network (2024 data, source: [SINISA 2025 Esgotamento Sanitário](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/009_RELATORIO_SINISA_ESGOTAMENTO_SANITARIO_2025_defeso.pdf)) — rates/figures may have changed since — massive infrastructure gap; see `--mains`
- **Asbestos banned 2017** nationally — earlier buildings likely contain it
- **Currency volatility** — BRL can swing 15-25% vs USD/EUR
- **Terreno de marinha / laudêmio / foro (CRITICAL for coastal buyers)** (2026-05-27 verified, source: Planalto Decreto-Lei 9.760/1946 + Lei 9.636/1998): **terreno de marinha** = coastal land within 33 m of the 1831 high-water line, titled to the **União** (federal government), administered by **SPU (Secretaria do Patrimônio da União)**. Holders have **enfiteuse (aforamento)** or **ocupação**, not domínio pleno; an aforado holder can in some cases buy out the União's 17% domínio direto (remição) — verify with SPU. Affected sweeps: Copacabana, Ipanema, Leblon, Botafogo, Flamengo, central Salvador, central Recife, Santos waterfront, much of Florianópolis. **Laudêmio = 5% of the updated domínio pleno value of the land, excluding improvements**, paid by the seller to SPU before any onerous inter vivos transfer of an aforado or ocupação holding (DL 2.398/1987 art. 3 as reworded by Lei 13.465/2017; the former 5% on land plus improvements under DL 9.760/1946 arts. 102 § 1 and 130 was revoked by DL 2.398/1987); **foro = 0.6%/yr of the domínio pleno value**, updated annually, on aforado land (DL 9.760/1946 art. 101); occupants pay an annual taxa de ocupação instead (2026-11-03 verified, source: [Planalto DL 2.398/1987](http://www.planalto.gov.br/CCIVIL_03/Decreto-Lei/1965-1988/Del2398.htm) + [Planalto DL 9.760/1946](https://www.planalto.gov.br/ccivil_03/decreto-lei/del9760.htm) + SPU Painel Transparência Ativa). Verify via SPU portal `https://www.gov.br/spu/` or via Certidão Autorizativa de Transferência (CAT). **PEC 3/2022** (Câmara approved two-round vote Feb 2022; at the Senado CCJ since Feb 2022, collective pedido de vista 4 Dec 2024, Emenda nº 1 (Sen. Plínio Valério) received 9 Dec 2024, relator's report on it received 31 Mar 2025 — still "em tramitação" with no later action listed as of 2026-11-03, source: [Senado — PEC 3/2022](https://www25.senado.leg.br/web/atividade/materias/-/materia/151923)) seeks to revoke União ownership and transfer to current occupants — **laudêmio + foro REMAIN IN FORCE 2026-11**; do NOT pre-emptively assume PEC will pass.
- **Indivisão / condomínio pro indiviso**: heirs who never completed partilha leave property in fractional undivided shares; requires extrajudicial inventário (Lei 11.441/2007 + CPC 13.105/2015) before any sale.

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
| **Estado (Secretaria da Fazenda)** | ITCMD (inheritance / gift tax) + other state taxes |
| **Síndico do Condomínio** | If apartment |
| **CEMADEN** | Flood/landslide risk |
| **SPU (Secretaria do Patrimônio da União)** | Terreno de marinha — laudêmio, foro, CAT (coastal property) |

## Source URL templates

| Source | URL pattern |
|---|---|
| FIPE-ZAP HPI | `https://www.fipe.org.br/en-us/indexes-and-indicators/fipezap` |
| ZAP Imóveis | `https://www.zapimoveis.com.br/` |
| VivaReal | `https://www.vivareal.com.br/` |
| Quinto Andar | `https://www.quintoandar.com.br/` |
| BCB Real Estate | `https://www.bcb.gov.br/` |
| IBGE | `https://www.ibge.gov.br/` |
| CEMADEN | `https://www.gov.br/cemaden/pt-br` |
| SGB (ex-CPRM) | `https://www.sgb.gov.br/` |
| INMET | `https://portal.inmet.gov.br/` |
| ANA | `https://www.gov.br/ana/pt-br` |
| INCRA | `https://www.gov.br/incra/pt-br` |
| Receita Federal — CIB FAQ | `https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib` |
| Receita Federal (CIB/SINTER) | `https://www.gov.br/receitafederal/` |
| ONR (cartório integration) | `https://www.onr.org.br/` |
| SINISA (sanitation indicators) | `https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa` |
| SPU (terreno de marinha) | `https://www.gov.br/gestao/pt-br/assuntos/patrimonio-da-uniao` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (FipeZAP Sep 2026), traffic (DNIT PNCT VMDa), tax (IPTU + ITBI per município + IR + Reforma Tributária 2026-2033, incl. LC 214/2025 real-estate rules and the TCU 2027 CBS calculation), rental (Lei do Inquilinato + STJ Segunda Seção 2026 condomínio-consent ruling), work (MTE + MEI + Simples + PNAD Contínua), risks (CEMADEN + Petrópolis 2022 + RS 2024 + Juiz de Fora 2026), mains (Marco Legal Saneamento 2033 target + SINISA 2025), incentives (MCMV + SFH / poupança 2027 model).
**Confidence**: MEDIUM overall — the 2026-10-23 refresh wave did not fully re-verify any fast-changing section (see Per-section verification and Update history). HIGH for the primary-sourced lines re-read in that wave: Lei do Inquilinato notice, guarantee and temporada rules (Lei 8.245/1991), the 2026 IR table and 15% non-resident withholding, the STJ Segunda Seção condomínio-consent ruling (REsp 2.121.055, 7 May 2026; Tema 1.443 pending, cases suspended nationwide), the Reforma Tributária timeline and LC 214/2025 real-estate rules (arts. 251, 253, 259-261, 281, 343-347, 475), ITBI 3% in São Paulo and Rio (prefeitura pages), the IR capital-gains exemptions (Lei 9.250/1995 arts. 22-23, Lei 11.196/2005 art. 39), the MCMV April 2026 parameters (R$200B + R$20B Fundo Social, R$13k income, R$600k cap, 420 months) and the SFH / poupança 2027 model (Res. CMN 5.254 and 5.255 of 10 Oct 2025), the foreign rural-land and border-strip rules (Lei 5.709/1971, Lei 6.634/1979), terreno de marinha laudêmio (DL 2.398/1987 art. 3) and the PEC 3/2022 status, the MEI caps (LC 238/2026), the salário mínimo and PNAD Contínua averages, SINISA 2024 sanitation coverage and the RS 2024 flood balance; HIGH that the price table matches the FipeZAP Sep 2026 release (asking prices of listed ready apartments, not transaction prices); HIGH for CIB phasing per the Receita Federal FAQ (instituting instruments carried from the 2026-08-07 check). MEDIUM for the 2027 CBS rate (TCU calculated 11.3% on 28 Oct 2026; Senate resolution due 15 Dec 2026) and the effective real-estate rates computed from it, the Petrópolis 2022 figures and platform ownership (secondary), and the Florianópolis and Rio STR lines (third-party trackers and press). LOW / est. for IPTU ranges beyond São Paulo residential, cartório fees, the cost-benchmark works rows, the mains cost table, city pay ranges, 'valor venal 30-60% below market' and the climate projections; the RJ sewage-connection figures are unsourced and the ITR administration line was not re-checked.

**Last verified**: 2026-08-07 (CIB cadastre re-verified — LC 214/2025 art. 265/266 two-phase rollout, Jan 2026 federal administration + notarial/registry + capitals & DF → Jan 2027 state administration + remaining municipalities; CIB does not replace the cartórios; instituting instrument corrected to IN RFB 2.030/2021. No playbook-level re-stamp since the 2026-04-26 population date.) Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md) and 2026-10-28 (TCU calculated the 2027 CBS reference rate at 11.3% on 28 Oct 2026, Senate resolution pending; Reforma Tributária 2027 line, the 26.5% figure and the pessoa-física test patched; see shared/regulatory-watch.md). Refresh wave 2026-10-23 (market, tax-legal, risk-infra): facts changed or confirmed in most sections, but `--price`, `--tax`, `--rental`, `--work`, `--risks` and `--mains` are not fully re-verified, so the playbook-level date is not re-stamped; see Per-section verification and Update history.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Active fiscal incentives (2025-2026) | 2026-10-23 | 2026-10-23 refresh wave | MCMV April 2026 parameters re-checked against Ministério das Cidades and Agência Brasil (R$200B + R$20B Fundo Social, R$13k income, R$600k cap, 420 months, 3M target, more than 2.7M contracted); Pró-Cotista confirmed on Caixa's FAQ; SFH / poupança 2027 model added from Res. CMN 5.254 and 5.255 (Voto CMN 64/2025); inline checks dated 2026-11-03 |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | No numeric facts; SEFAZ row corrected from ICMS to ITCMD, SPU row added, CEMADEN and Receita Federal rows confirmed |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | All 14 rows load; CEMADEN, SGB (ex-CPRM) and ANA moved to their canonical URLs; SINISA and SPU rows added |

## Extension TODOs

- [ ] CIB rollout tracker (Jan 2027 phase — state administration + all remaining municipalities, LC 214/2025 art. 266 II)
- [ ] Per-município IPTU rates table
- [ ] Per-município ITBI rates table
- [ ] Reforma Tributária real-estate sector rates 2027-2033
- [ ] MCMV eligibility decision tree (R$13k income, R$600k cap)
- [ ] Foreign rural land cap calculation per município (25% + 10% rules)
- [ ] Petrópolis + Rio Grande do Sul flood-zone overlay
- [ ] Favela property regularization (usucapião + REURB)
- [ ] STJ condomínio STR ban tracker
- [ ] Sewage connection per município (Marco Legal target 2033)

## Update history

- **2026-10-23** — Refresh wave (market, tax-legal, risk-infra; tax-legal inline stamps dated 2026-11-03); playbook-level date not re-stamped because none of `--price`, `--tax`, `--rental`, `--work`, `--risks` and `--mains` is fully re-verified
  - Checked, not fully verified (facts checked — changed / confirmed / unverifiable): Country profile 11 — 2 / 6 / 3; `--price` 32 — 27 / 3 / 2; `--traffic` 6 — 3 / 1 / 2; `--tax` 42 — 17 / 13 / 12; `--rental` 17 — 11 / 4 / 2; `--work` 16 — 9 / 4 / 3; `--risks` 24 — 12 / 4 / 4; `--mains` 12 — 8 / 2 / 6; Climate change projections 5 — 0 / 0 / 2; Cost benchmarks (BR 2026) 15 — 4 / 2 / 9; Common listing platforms 5 — 4 / 0 / 1; Caveats unique to BR 24 — 8 / 8 / 8; Reddit / forum sources 9 — 0 / 0 / 5 (Reddit login-walled; news hosts checked for liveness only)
  - Fully re-verified (rows in the verification table): Active fiscal incentives (2025-2026) 10 — 4 / 6 / 0; Verification authorities 8 — 2 / 2 / 0; Source URL templates 14 — 4 / 10 / 0
  - Totals: 250 facts checked — 115 changed / 65 confirmed / 59 unverifiable (per-section counts as reported; those for `--risks`, `--mains`, Climate change projections, Verification authorities and Reddit / forum sources do not sum to their totals); 89 applied edits (market 23, tax-legal 35, risk-infra 31); the playbook has no `--crime` or `--amenities` section
  - Main changes, market: 5,569 municípios + DF + Fernando de Noronha (IBGE 2025) and BCB PTAX FX at the 23 Oct 2026 close; price table rebuilt from FipeZAP Sep 2026 (national R$10,015/m², +5.51% YoY), replacing 'Q1 2026' figures that matched neither the Mar nor the Sep 2026 release; FipeZAP credited to Fipe + Grupo OLX; ZAP + VivaReal in Grupo OLX since 30 Oct 2020, Imovelweb in the QuintoAndar group since Dec 2021; Lei do Inquilinato notice rules corrected (arts. 6 and 46) and temporada wording aligned with art. 48; STJ Segunda Seção REsp 2.121.055 (7 May 2026, two-thirds assembly vote) replaces the 2021 'condomínios can ban STR' line, with Tema 1.443 pending; the unsourced Florianópolis '~40k' replaced by tracker counts that disagree (BnBCalc 14,458; GuestFavorites 19,753 in the city); 2026 IR table with the Lei 15.270/2025 reduction; MEI cap R$81k in 2026, R$110k for 2027 and R$140k from 2028 (LC 238/2026); PIS/COFINS extinguished from 2027 (ADCT art. 126 II); salary block re-based on IBGE PNAD Contínua Q2 2026 (R$3,738 national average)
  - Main changes, tax-legal: Rio ITBI 3% since 1 Jan 2018 (Lei 6.250/2017), not 2%, so the Rio buyer total is ~4–5% (computed); the R$35k exemption covers real estate (Lei 9.250/1995 art. 22 II), reversing the 'moveables only' line; único-imóvel and 180-day rollover conditions reworded to the statute (the rollover is for residents only); LC 214/2025 art. 261 reductions with the 2027-2028 CBS parts computed at 5.6% / 3.36% if the TCU's 11.3% stands, the 40% short-let rule tied to arts. 251 and 253, and the R$600/month redutor social on lettings (art. 260); LC 227/2026 ITCMD and CTN ITBI changes; works rows in Cost benchmarks labelled est.; MCMV parameters confirmed and the SFH / poupança 2027 model added (BR-03); foreign rural-land caps, MEI tiers, legal-entity and border-strip rules corrected to Lei 5.709/1971 and Lei 6.634/1979; laudêmio = 5% of the updated land value excluding improvements (DL 2.398/1987 art. 3 as reworded by Lei 13.465/2017); PEC 3/2022 status re-dated
  - Main changes, risk-infra: DNIT PNCT / VMDa and CET-Rio; CEMADEN, SGB and ANA source rows; Petrópolis 2022 (250 mm in 3 hours, 233 deaths and 4 missing; secondary), the RS 2024 final balance (185 deaths, 478 municipalities) and Juiz de Fora Feb 2026 (752.4 mm); Amazonas heat spots (25,499 in 2024, 4,545 in 2025); cyclone line corrected; lead-paint cap cut to 90 ppm by Lei 15.441/2026; NBR 15575 scope; certidão validity and Lei 13.097/2015 art. 54 § 2; SINISA 2024 (62.3% on a sewage collection network, 51.8% treated, 84.1% water) replaces '47% unassisted (2020)'; CEDAE concession blocks, COPASA's 2026 privatization, ANA's role, and the SABESP concession plan (~R$70bn to 2029) replacing the untraceable R$47.4B; mains cost table labelled est.; SEFAZ row ICMS → ITCMD; SPU and SINISA rows added
  - Footer pass: Coverage check and Confidence recomputed; Caveats STJ and sewage lines aligned with `--rental` and `--mains` (STJ news pages of 7 May and 17 Sep 2026; SINISA 2025 Esgotamento Sanitário report)
