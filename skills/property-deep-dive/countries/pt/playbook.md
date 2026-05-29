# Portugal 🇵🇹 — Property Due-Diligence Playbook

ISO2: `pt`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4-3 digits format `1100-001` Lisboa, `4000-001` Porto, `8000-001` Faro
- **Admin levels**: 18 distritos + 2 regiões autónomas (Açores, Madeira) + 308 municípios + 3,091 freguesias
- **Currency**: EUR (€)
- **Languages**: Portuguese (official); Mirandese (recognized minority, Trás-os-Montes)
- **Cadastre**: **Cadastro Predial** under DGT (Direção-Geral do Território) — modernization ongoing; **ePortugal** + **Conservatória do Registo Predial**
- **Identifier**: artigo matricial (matricial article) + freguesia
- **Civil-law tradition**: notário + registry critical
- Distinct ownership types: propriedade plena (freehold), propriedade horizontal (commonhold), usufruto

## Section: `--price`

### Primary sources

- **ePortugal Predial Online**: `https://www.predialonline.pt/` — official cadastre access
- **Portal das Finanças** (matricial article + valor patrimonial tributário): `https://www.portaldasfinancas.gov.pt/`
- **INE (Instituto Nacional de Estatística) Estatísticas dos Preços da Habitação**: `https://www.ine.pt/`
- **Confidencial Imobiliário SIR (Sistema de Informação Residencial)**: `https://www.ci-iberian.com/`

### Listing platforms

- **Idealista PT**: `https://www.idealista.pt/<distrito>/<municipio>/`
- **Imovirtual**: `https://www.imovirtual.com/`
- **Casa Sapo**: `https://casa.sapo.pt/`
- **CenturyTwentyOne, Engel & Völkers, Remax** — agency networks
- **OLX** (privates)

### Price benchmarks (2025-2026)

- **INE Índice Preços Habitação (IPHab)**: official quarterly
- **Confidencial Imobiliário** SIR + indices

| City/Region | Apartamentos €/m² (2024-2025) |
|---|---:|
| **Lisboa** | 4,000–7,500 (centro 6,000–10,000+) |
| **Porto** | 3,000–5,500 |
| **Cascais, Estoril** | 5,000–9,000 |
| **Sintra** | 2,500–4,500 |
| **Algarve (coast)** | 3,500–6,500 (Vilamoura/Quinta do Lago higher) |
| **Madeira (Funchal)** | 3,000–5,000 |
| **Açores (Ponta Delgada)** | 1,800–3,000 |
| **Coimbra** | 1,800–2,800 |
| **Braga** | 1,800–2,800 |
| **Évora, Beja** | 1,200–2,000 |
| Rural interior (Alentejo, Beira) | 600–1,500 |

### Compute

1. Listing €/m² = price / área bruta privativa (gross private area, includes walls)
2. **Trap**: área útil ≠ área bruta privativa ≠ área bruta de construção; clarify
3. **Trap**: VPT (valor patrimonial tributário) is ~30-60 % of market value, used for tax
4. Compare to INE IPHab for the município

---

## Section: `--traffic`

### Sources

- **IP (Infraestruturas de Portugal)**: `https://www.infraestruturasdeportugal.pt/`
- **Brisa** (autoestradas): `https://www.brisa.pt/`
- **Ascendi** (autoestradas concessionária)
- **Estradas de Portugal** historical data

### Key term

**TMD (Tráfego Médio Diário)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (estrada local, rua urbana periférica)
- 🟡 1,000–8,000 v/d (estrada nacional secundária, urban arterial)
- 🟠 8,000–30,000 v/d (EN/IC, urban core)
- 🔴 > 30,000 v/d (autoestrada, IP, urban centro Lisboa/Porto)

---

## Section: `--tax`

### Annual property tax — IMI (Imposto Municipal sobre Imóveis)

- Set per **município** within state-mandated bands
- **Urbano**: **0.3–0.45 %** of VPT (valor patrimonial tributário)
- **Rústico**: 0.8 %
- 195 municípios (incl. Lisboa, Faro, Coimbra) at minimum 0.3 % for 2025 (per municipal IMI-rate filings — verify current list with AT / DGAL)
- **Lisboa kept 0.3 %** for 2026 (confirmed Dec 2025)
- Bills typically May (split into 1-3 installments)

### IMI exemptions

- **Permanent dwelling** (HPP): exemption for 3 years if VPT < €125,000
- Low-VPT properties (VPT < €66,500): 5-year exemption first home
- Energy-efficient buildings: bonificações in some municípios

### Other annual

- **AIMI (Adicional ao IMI)** wealth tax surcharge: 0.7-1.5 % on properties summed VPT > €600k (€1.2M for couples) (2025 rates — verify current thresholds with Portal das Finanças; may have changed since)

### Transaction taxes — IMT (Imposto Municipal sobre Transmissões)

**2025 progressive rates for primary residence**:

| VPT bracket (€) | Rate (primary residence) | Rate (other) |
|---|---:|---:|
| 0 – 104,261 | **0 %** (exempt) | 1.0 % |
| 104,261 – 142,618 | 2 % | 2 % |
| 142,618 – 194,458 | 5 % | 5 % |
| 194,458 – 324,058 | 7 % | 7 % |
| 324,058 – 648,022 | 8 % | 8 % |
| 648,022 – 1,128,287 | 6 % avg | 6 % |
| > 1,128,287 | **7.5 % flat** | **7.5 % flat** |

**Non-resident IMT surcharge — PROPOSED, not yet in force as of 2026-05**: no enacted statute / Portaria / AT release identified. Tracked in `regulatory-watch.md` as proposed (impact tier 3). Do not rely on it for purchase modelling until enacted. (2026-05-27 verified — unsourced political announcement only)

**IS (Imposto do Selo)**: **0.8 %** of price

**Notário + Registo**: **0.5–1.5 %**

### Total transaction cost (buyer side)

- Primary residence: **2–8 %** depending on price bracket
- Other (second home, investment): **5–10 %**

### IVA on new builds

- 6 % AL (continental, accommodation services)
- 6 % residential under specific schemes
- 13 % AIM/IRC (Algarve etc., reduced)
- 23 % standard

### IRS on rental + capital gains

- **Categoria F (rental)**: 28 % flat (or option to add to general IRS)
- **Capital gains**: 50 % of gain added to IRS (for resident); **28 % flat for non-residents on PT-source gains**
- Primary residence reinvestment: capital gains exempt under conditions

### Future risk

- Non-resident IMT surcharge (Oct 2025) — under fiscal review
- AIMI thresholds may adjust
- Mais Habitação package (Lei 56/2023) partially **repealed by Decreto-Lei 76/2024 (23 Oct 2024, in force 1 Nov 2024)** — repealed: (a) 5-yr AL registration term with mandatory renewal; (b) general suspension of new AL registrations in apartments (national); (c) mandatory condominium consent for AL in autonomous fractions; (d) expiry of inactive registrations; (e) non-transferability of registration on sale. Município-level Áreas de Contenção (Lisbon RMAL, Porto Reg. 1462/2024) remain in force and were reinforced by DL 76/2024. (2026-05-27 verified; source [DR DL 76/2024](https://diariodarepublica.pt/dr/detalhe/decreto-lei/76-2024-892301177))

---

## Section: `--rental`

### Long-term residential

- **NRAU (Novo Regime do Arrendamento Urbano)**: tenant protection moderate
- Standard contract: 5-year minimum (loose)
- **Pacto de preferência** (preemption rights for tenants under conditions)
- Recent reforms 2023-2024: trying to encourage long-let supply

### Short-let — Alojamento Local (AL)

**Mandatory registration via município**:
- Categories: Apartamento, Moradia, Estabelecimento de Hospedagem
- License fee per município
- VPT compatibility check

**LISBON SUSPENSION (continuing)**:
- November 2024: 6-month suspension of new AL licenses in Lisbon
- May 2025: extended
- September 2025: still suspended in central Lisboa (Santa Maria Maior, Misericórdia, Santo António, Arroios)
- **2026**: pending RMAL changes
- **Porto Centro**: suspended in many freguesias since 2022
- **Algarve coast**: regulated but largely still possible

### Tax on AL

- **IRS Cat. F or B** depending on volume:
  - Cat. F: simple, **28 % flat** rate (or option for general IRS)
  - Cat. B (commercial): if 4+ properties or hotel-style services
- **IVA**: 6 % accommodation services (continental); 4 % Açores, 9 % Madeira
- **Taxa turística**: per município (Lisboa €4/night/person, Porto €3, Faro €2 — confirm current rate with each Câmara Municipal)

### Strategic notes

- **Algarve season concentration** — est. 60-70 % of revenue in Apr-Oct (based on Algarve seasonal-occupancy patterns — verify with Turismo de Portugal / INE occupancy data)
- **Lisboa AL suspended** in centro — verify before buying for AL strategy
- **Madeira** + **Açores**: Mais Habitação less restrictive
- **Coimbra, Braga, Aveiro**: smaller markets but viable
- **Cascais, Estoril**: high yields but high prices

---

## Section: `--work=<profession>`

### Job platforms

- **IEFP (Instituto do Emprego e Formação Profissional)**: `https://www.iefp.pt/`
- **Net-Empregos**, **LinkedIn PT**, **Sapo Emprego**, **Indeed.pt**
- **Empregos.online**

### Self-employment

- **Trabalhador independente / Recibos verdes**: register at Finanças
- **Segurança Social** + IRS (Categoria B)
- **Empresário em Nome Individual (ENI)**: simpler
- **Sociedade por Quotas (Lda.)**: min capital symbolic; from €1

### Salary benchmarks (2025)

- Median monthly gross:
  - Lisboa, Porto: ~€1,500-2,200
  - Coimbra, Braga: ~€1,200-1,700
  - Smaller cities: ~€1,000-1,400
- **SMN (Salário Mínimo Nacional) 2025**: €870/mo (14 payments) = €12,180/yr

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **ANEPC (Autoridade Nacional de Emergência e Proteção Civil)** | `https://prociv.gov.pt/` | Emergency planning + risk maps |
| **APA (Agência Portuguesa do Ambiente)** | `https://apa.pt/` | Floods + droughts + climate |
| **IPMA (Instituto Português do Mar e da Atmosfera)** | `https://www.ipma.pt/` | Meteorology + seismic + climate |
| **CCDR regional** (Comissões de Coordenação e Desenvolvimento Regional) | per region | Regional hazards |
| **ICNF (Instituto da Conservação da Natureza)** | `https://www.icnf.pt/` | Forest + fire + protected areas |
| **CNPGB (Comissão Nacional do Programa de Gestão de Riscos)** | `https://snrf.cnpcb.pt/` | Wildfire risk |

### Specific risks

- **Incêndios florestais (wildfires)**: HUGE in interior centro (Beira) + norte; 2017 Pedrógão Grande disaster (66 dead); annually severe
- **Sismo (earthquakes)**:
  - Algarve coast + Lisboa region significant; 1755 Lisbon megaquake reference (M ~8.5-9)
  - Faro, Algarve: zona sísmica 1A — highest seismic-hazard band in PT (per IPMA / Anexo Nacional EC8 seismic-zoning)
  - Lisboa, Setúbal: zona 1B
- **Tsunami**: Algarve + western coast — 1755 reminder, modern monitoring
- **Cheias (flooding)**: Tejo (Lisboa, Santarém), Douro (Porto), Mondego (Coimbra) basins
- **Seca (drought)**: intensifying esp. Alentejo + Algarve; Guadiana basin water restrictions
- **Erosão costeira**: significant Algarve + Costa de Caparica; receding ~1-3 m/yr in some areas (est., per APA coastal-erosion monitoring — verify per-município, parcel-level confirmation required)
- **Calor extremo**: heat waves rising

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1958** | Pre-seismic standards, lead pipes, asbestos likely |
| **1958–1983 RSCCS** | Basic seismic standards |
| **1983–2007 REBAP** | Modern seismic |
| **Post-2007 Eurocódigo** | Current standards |
| **Pre-1990** | Asbestos common (telhas, isolamento) |
| **Pre-2011** | Lead solder in plumbing possible |

**1755 Lisbon earthquake reference**: Anything pre-1958 in Lisboa-Setúbal zone is structurally questionable; verify ITE.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Certificado Energético (CE)** | All sales | 10 years |
| **Caderneta Predial Urbana** | All sales (matricial article) | At sale |
| **Ficha Técnica de Habitação (FTH)** | Post-2004 builds | At sale |
| **Licença de Utilização** | All sales | At sale |
| **Certidão Permanente do Registo Predial** | Title verification | At sale |
| **Recibo IMI** + clearance | At sale | At sale |
| **Estatutos do Condomínio** + actas | If condo | At sale |

### Climate change projections (APA / IPMA)

- +2.0–4.5 °C by 2050 vs 1971-2000 (RCP scenarios)
- Drought: Alentejo + Algarve severely affected
- Wildfires: rising risk centro + norte
- Sea-level rise: +20-60 cm by 2100; coastal erosion accelerating
- Heatwaves: longer + hotter
- Tropicalization of southern Iberia ecosystems

---

## Section: `--mains`

### Sources

- **ERSAR (Entidade Reguladora dos Serviços de Águas e Resíduos)**: `https://www.ersar.pt/` — national regulator
- **Águas de Portugal Group** (state-owned multi-region utility): `https://www.adp.pt/`
- Each município has **Câmara Municipal Águas e Saneamento** or contracts to AdP/Veolia/etc.
- Major: **EPAL** (Lisboa), **Águas do Porto** (Porto), **AGS, INDAQUA, Veolia PT**

### Verification

- Most centros urbanos + suburbs: mains universal
- Rural Alentejo, Beira interior: **fossa séptica** common
- New Mais Habitação policy: pushing rural mains expansion

### Costs

| Scenario | Cost (€) |
|---|---:|
| Ramal (mains connection) | 1,500–4,000 |
| Septic to mains | 4,000–10,000 |
| Fossa séptica modern | 3,000–8,000 |
| Cisterna (rainwater) | 2,000–5,000 |

---

## Cost benchmarks (PT 2026)

| Work | Cost (€) |
|---|---:|
| Certificado Energético | 100–400 |
| Notário + Registo | 0.5–1.5 % of price |
| **IMT (primary, €300k bracket)** | **~€10,000** |
| **IMT (other, same)** | **~€15,000** |
| **IS (Imposto do Selo)** | 0.8 % |
| **Total transaction cost (primary residence)** | **~3–8 %** of price |
| **Total transaction cost (other)** | **~5–10 %** |
| Septic to mains | 4,000–10,000 |
| Roof telha terracota (200 m²) | 6,000–15,000 |
| Earthquake retrofit | 20,000–80,000 |
| Wildfire-zone fortification | 5,000–15,000 |
| Energy retrofit (Class C → A) | 25,000–70,000 |

## Active fiscal incentives (2025-2026)

- **Programa Edifícios + Sustentáveis**: energy retrofit grants up to 70 %
- **IFRRU 2020**: urban regeneration — extends into 2024+
- **PRR (Plano de Recuperação e Resiliência)**: post-COVID retrofit funding
- **Reabilitação Urbana benefits**: ARU (Áreas de Reabilitação Urbana) — IMI/IMT reductions
- **NHR/IFICI (Incentivo Fiscal à Investigação Científica e Inovação)**: NHR closed to new entrants by **Lei n.º 82/2023 (OE 2024) Art. 236.º** (transitional 2024 entry under specified conditions). IFICI established by **EBF Art. 58.º-A** and regulated by **Portaria n.º 352/2024/1 de 23 de dezembro** — narrower successor for scientific research, qualified jobs in productive investment, technology, startups (NOT pensions; NHR pension exemption eliminated). IFICI is single-use: not applicable to prior NHR or "Regressar" beneficiaries. (2026-05-27 verified; source [Portaria 352/2024/1 — sgeconomia.gov.pt](https://www.sgeconomia.gov.pt/destaques/portaria-n-35220241-de-23-de-dezembro-...))

## Common listing platforms

- **Idealista PT** — biggest, full extraction
- **Imovirtual, Casa Sapo** — major
- **Engel & Völkers PT, Sotheby's, Predibisa** — premium
- **OLX, CustoJusto** — privates

## Caveats unique to PT

- **Golden Visa abolished for residential 2023** — only commercial / funds remain
- **NHR/IFICI 2024** restructured — no longer the broad 10-yr exemption regime
- **AL suspension Lisbon centre** (May 2025 ext) — verify per freguesia before buying for AL
- **Seismic zone Lisboa-Setúbal**: any pre-1958 build needs structural review
- **Algarve season concentration**: 4-month revenue window for AL
- **Wildfire zones**: post-2017 Pedrógão restrictions on rural land use
- **Direito de preferência** (preemption rights) — município/IHRU may have first-refusal in classified zones (ARU especially)
- **Erosão costeira** — coastal Algarve + Costa de Caparica retreating
- **Caderneta Predial vs Registo Predial** mismatch common — verify both
- **Madeira + Açores** different VAT/tax regimes (regional)
- **Pueblos rurales (interior)** depopulating; resale liquidity weak
- **Tropicalization** of agriculture and ecosystems

## Reddit / forum sources

- **r/Portugal**, **r/lisbon**, **r/porto**, **r/algarve**
- **r/PortugalExpats**, **r/AmerExit** (PT subforum)
- **The Portugal News**, **Algarve Daily News**
- **Portugal Resident**, **Sur in English** (south)
- **Lisbon Living Group** (FB)
- **NHR Forum, AL Tax Forum** professional groups

## Verification authorities

| Authority | When to call |
|---|---|
| **Conservatória do Registo Predial** | Title verification |
| **Câmara Municipal (Urbanismo)** | Permits, ARU, AL license |
| **Finanças** | IMI, IMT, NIF |
| **Notário** | Final transfer (escritura) |
| **ERSAR** | Mains drains regulation |
| **AdP / município operator** | Mains drains verification |
| **Bombeiros + ANEPC** | Wildfire zones |
| **IPMA** | Seismic + tsunami info |
| **Condomínio (administração)** | If condo: condomínio fees, status |

## Source URL templates

| Source | URL pattern |
|---|---|
| ePortugal Predial Online | `https://www.predialonline.pt/` |
| Portal das Finanças | `https://www.portaldasfinancas.gov.pt/` |
| Idealista PT | `https://www.idealista.pt/<distrito>/<municipio>/` |
| Imovirtual | `https://www.imovirtual.com/` |
| INE | `https://www.ine.pt/` |
| Confidencial Imobiliário | `https://www.ci-iberian.com/` |
| ANEPC | `https://prociv.gov.pt/` |
| APA | `https://apa.pt/` |
| IPMA | `https://www.ipma.pt/` |
| ERSAR | `https://www.ersar.pt/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (Cadastro modernization ongoing but Finanças stable; APA + IPMA well-maintained). MEDIUM-HIGH for AL regulation (Lisbon suspension confirmed May 2025; Porto + Algarve evolving).

## Extension TODOs

- [ ] Per-município IMI rate tables + current AL availability map
- [ ] Per-distrito wildfire risk classification (post-2017 reform)
- [ ] Tsunami zone Algarve detail (parcel-level)
- [ ] Direito de preferência triggers per ARU
- [ ] Erosão costeira projections per município
- [ ] NHR/IFICI 2024 eligibility decision tree
- [ ] AL license availability per Lisboa freguesia (changing)
- [ ] Caderneta vs Registo mismatch detection
