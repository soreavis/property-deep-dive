# Portugal 🇵🇹 — Property Due-Diligence Playbook

ISO2: `pt`. Status: ✅ Fully populated (researched 2026-04). **Last refreshed**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged).

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
- **Confidencial Imobiliário SIR (Sistema de Informação Residencial)**: `https://www.confidencialimobiliario.com/`

### Listing platforms

- **Idealista PT**: `https://www.idealista.pt/<distrito>/<municipio>/`
- **Imovirtual**: `https://www.imovirtual.com/`
- **Casa Sapo**: `https://casa.sapo.pt/`
- **CenturyTwentyOne, Engel & Völkers, Remax** — agency networks
- **OLX** (privates)

### Price benchmarks (2025-2026)

- **INE Índice Preços Habitação (IPHab)**: official quarterly
- **Confidencial Imobiliário** SIR + indices
- **INE IPHab YoY**: +18.9 % YoY Q4 2025 (full-year 2025 +17.6 %); Q1 2026 +17.8 % YoY — first deceleration since Q2 2024 (2026-07-03 verified, INE IPHab). €/m² ranges below predate this run-up — treat as indicative floors, re-price against INE município data.

| City/Region | Apartamentos €/m² (2024-2025 — pre-run-up; verify against current INE IPHab) |
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

- **AIMI (Adicional ao IMI)** wealth tax surcharge: 0.7-1.5 % on properties summed VPT > €600k (€1.2M for couples) (2026 rates confirmed unchanged; source PwC Guia Fiscal 2026; 2026-07-03 verified)

### Transaction taxes — IMT (Imposto Municipal sobre Transmissões)

**2026 progressive rates for primary residence** (OE2026 ~2 % indexation, AT practical tables per Ofício-circulado n.º 40129/2026 de 06/01/2026; cross-checked PwC Guia Fiscal 2026; 2026-07-03 verified):

| VPT bracket (€) | Rate (primary residence) | Rate (other) |
|---|---:|---:|
| 0 – 106,346 | **0 %** (exempt) | 1.0 % |
| 106,346 – 145,470 | 2 % | 2 % |
| 145,470 – 198,347 | 5 % | 5 % |
| 198,347 – 330,539 | 7 % | 7 % |
| 330,539 – 660,982 | 8 % | 8 % to 633,931; 6 % (taxa única) above |
| 660,982 – 1,150,853 | 6 % (taxa única) | 6 % (taxa única; band starts at 633,931) |
| > 1,150,853 | **7.5 % flat** | **7.5 % flat** |

*'Rate (other)' column per the AT consolidated CIMT art. 17.º n.º 1 c) (bracket values from Lei 73-A/2025, de 30 de dezembro): the non-HPP 8 % band ends at €633,931 and the 6 % taxa única runs €633,931–1,150,853 ([AT CIMT art. 17.º](http://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cimt/Pages/cimt17.aspx); 2026-10-23 verified).*

**OE2027 — PROPOSED, NOT ADOPTED**: Proposta de Lei n.º 110/XVII/2.ª (Orçamento do Estado para 2027, delivered 8 Oct 2026) art. 65.º would index every CIMT art. 17.º n.º 1 bracket by 2.3 % for 2027 — HPP 0 % to €108,792 / 2 % to 148,816 / 5 % to 202,909 / 7 % to 338,141 / 8 % to 676,185 / 6 % taxa única to 1,177,323 / 7.5 % above; other habitational 1 % to 108,792, the same 2 / 5 / 7 % bands to 338,141, 8 % to 648,511, 6 % taxa única to 1,177,323, 7.5 % above; IMT Jovem 0 % to 338,141 and 8 % on the excess to 676,185 ([EY Tax Alert OE2027](https://www.ey.com/content/dam/ey-unified-site/ey-com/pt-pt/services/tax/documents/ey-taxalert2027.pdf) + [DN/Lusa 8 Oct 2026](https://www.dn.pt/pol%C3%ADtica/oe2027-leia-aqui-as-principais-medidas-includas-na-proposta-do-governo), secondary). Final global vote scheduled 24 Nov 2026; the 2026 table above applies until the LOE 2027 is published and in force (intended 1 Jan 2027). See `shared/regulatory-watch.md` (PT).

**IMT Jovem** (Lei 30-A/2024 + DL 48-A/2024, in force 1 Aug 2024): buyers aged ≤35 (not an IRS dependent that year; not owner of another habitational urban property — 3-year lookback per Santander 2026 explainer, verify condition wording with AT) making their FIRST acquisition of an urban property exclusively for own-permanent residence pay **€0 IMT and €0 Imposto do Selo** up to **€330,539** (2026 Continente value; €324,058 in 2025; RAs higher — €396,647); between €330,539 and €660,982 only the excess is taxed at 8 % marginal IMT while the IS exemption remains in full; no benefit above €660,982 (OE2027 proposes €338,141 / €676,185 for 2027 — not adopted, see above). One-time use. Land-for-construction excluded. (2026-07-03 verified; sources: Portal das Finanças IMT Jovem + PwC Guia Fiscal 2026 + ECO)

**Non-resident IMT surcharge — ENACTED**: DL 97/2026 (20 May 2026, under authorization Lei 9-A/2026) adds CIMT Art. 17.º/10 — flat **7.5 % IMT** on acquisition of urban habitational property by non-residents, **no exemption or reduction applies** (incl. no HPP brackets, no IMT Jovem). Exceptions (Art. 17.º/10 a-c): buyer has at **any earlier time** been PT tax resident under CIRS Art. 16.º (past residence suffices), or becomes resident within 2 years of purchase (refund), or lets the property at a moderate rent (within the DL 97/2026 Art. 2.º(2)-(3) limits — 2.5 × RMMG, 2.5 × EUR 920 RMMG 2026 (DL 139/2025) = EUR 2,300/month, updatable by portaria per the NRAU art. 24 factor — none found as of 2026-10-21) under a lease signed within 6 months and running ≥36 months within the first 5 years; refunds under the last two run through annulment (Art. 17.º/11) by reclamação graciosa within 6 months (Art. 17.º/12). **AT guidance — Ofício Circulado n.º 40131/2026 (4 Sep 2026)**: for spouses in a community-of-property regime the 7.5 % applies only where both are non-resident and neither has ever been PT-resident; co-owners are tested individually. **Effective 25 May 2026** — the IMT amendment is in Art. 6.º and Art. 18.º sets no special date for it (5th-day default; DL 97/2026 has no entrada-em-vigor article, so the Lei 74/98 art. 2(2) default applies; Art. 18.º read 2026-10-21 in the AT-published consolidated text: n.º 1 dates only the DL 68/2019 + 69/2019 revocation, CIA and RSAA to 1 Sep 2026, n.º 2 the CIRS / EBF 24.º-A / 45.º-C changes to 1 Jan 2026, nos. 4–8 the IVA provisions); the 1 Sep 2026 date in some summaries belongs to the CIA / RSAA provisions. Same diploma extends the IMT payment deadline to 30 days from liquidation. (2026-10-21 verified; sources [AT consolidated DL 97/2026](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/decreto-lei-97-2026.pdf) + [AT CIMT Art. 17.º consolidated](http://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cimt/Pages/cimt17.aspx) + [Ofício Circulado 40131/2026](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio-circulado-40131-2026.pdf) + [DR DL 97/2026](https://diariodarepublica.pt/dr/detalhe/decreto-lei/97-2026-1124493227))

**IS (Imposto do Selo)**: **0.8 %** of price

**Notário + Registo**: **0.5–1.5 %**

### Total transaction cost (buyer side)

- Primary residence: **2–8 %** depending on price bracket
- Other (second home, investment): **5–10 %**

### IVA on new builds

- 6 % AL (continental, accommodation services)
- 6 % residential under specific schemes (incl. the DL 97/2026 regime for homes built or rehabilitated for sale as the buyer's own permanent residence, sale price capped at €660,982 — the upper limit of the 2nd bracket of CIMT art. 17.º n.º 1 b) in its Lei 73-A/2025 (OE2026) wording, fixed by DL 97/2026 art. 2.º n.º 2 b) and updatable by portaria (n.º 3); the OE2027 bill re-indexes the IMT tables but does not amend DL 97/2026, so it would not by itself move the cap to the €676,185 EY Tax Alert cites; 2026-10-28 verified, source [AT consolidated DL 97/2026](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/decreto-lei-97-2026.pdf) art. 2.º + art. 8.º)
- 13 % AIM/IRC (Algarve etc., reduced)
- 23 % standard

### IRS on rental + capital gains

- **Categoria F (rental)**: housing leases **25 %** autonomous rate (CIRS art. 72.º n.º 2, Lei 56/2023), cut by 10 / 15 / 20 points for permanent-housing leases of ≥ 5 / ≥ 10 / ≥ 20 years (art. 72.º n.os 3–5), cuts that do not apply to leases signed from 1 Jan 2024 whose rent exceeds the Portaria 176/2019 limits by 50 % (n.º 23); **10 %** for housing leases whose monthly rent stays within the DL 97/2026 art. 2.º(2)-(3) limits (EUR 2,300/month in 2026, computed — see the IMT exception above), income earned up to 31 Dec 2029, effects from 1 Jan 2026, unless a more favourable rate applies (EBF art. 45.º-C, added by DL 97/2026 art. 9.º; the article sets no residence condition); other rental income 28 % (art. 72.º n.º 1 e)); residents may opt to aggregate with general IRS (2026-10-23 verified; sources [AT CIRS art. 72.º](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx) + [AT EBF art. 45.º-C](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/EBF45C.aspx))
- **Capital gains**: 50 % of gain added to IRS at progressive rates — residents and, since 1 Jan 2023, non-residents too (a non-resident's rate is set by reference to worldwide income); the old **28 % flat** non-resident rate no longer applies (CIRS art. 72.º n.º 1 a) revoked and art. 43.º n.º 2 reworded by Lei 24-D/2022 — [AT CIRS art. 72.º](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx); rate mechanics per [PwC Tax Summaries](https://taxsummaries.pwc.com/portugal/individual/income-determination), secondary; 2026-10-23 verified)
- Primary residence reinvestment: capital gains exempt under conditions

### Future risk

- Non-resident 7.5 % IMT surcharge — **ENACTED, in force 25 May 2026** (DL 97/2026 Art. 6.º; AT Ofício Circulado 40131/2026 of 4 Sep 2026 on married / co-owner cases); see Transaction taxes above (2026-09-17 verified)
- AIMI thresholds may adjust
- Mais Habitação package (Lei 56/2023) partially **repealed by Decreto-Lei 76/2024 (23 Oct 2024, in force 1 Nov 2024)** — repealed: (a) 5-yr AL registration term with mandatory renewal; (b) general suspension of new AL registrations in apartments (national); (c) mandatory condominium consent for AL in autonomous fractions; (d) expiry of inactive registrations; (e) non-transferability of registration on sale. Município-level Áreas de Contenção (Lisbon RMAL, Porto Reg. 1462/2024) remain in force and were reinforced by DL 76/2024. (2026-05-27 verified; source [DR DL 76/2024](https://diariodarepublica.pt/dr/detalhe/decreto-lei/76-2024-892301177)) **Decreto-Lei n.º 151/2026 (30 Jul 2026, DR n.º 146/2026 Série I; approved by the Council of Ministers on 11 Jun 2026; in force 31 Jul 2026, effects until 31 Dec 2026)**: municipalities with more than 1,000 AL registrations by 31 Dec 2025 that have not yet done so must decide by 31 Dec 2026 whether to regulate AL (DL 128/2014 art. 4.º n.º 6); a suspension of new AL registrations (DL 128/2014 art. 15.º-B n.º 2) still running may be extended once, and one that lapsed at its 1-yr maximum may be re-imposed once, by assembleia municipal deliberation, never beyond 31 Dec 2026; registrations validly made before the deliberation are unaffected (art. 6.º n.º 2) — check the município's current position before buying for AL (2026 data, source [DR DL 151/2026](https://diariodarepublica.pt/dr/detalhe/decreto-lei/151-2026-1153221700)) The current Lisbon RMAL is its **2nd amendment (Aviso n.º 29926-A/2025/2, in force 6 Dec 2025)**, which re-imposes **sale-triggered caducidade** of *moradia*/*apartamento* AL registrations in containment zones at municipal level — municipal caducidade survives despite DL 76/2024 restoring national transferability of registrations on sale. (2026-07-02 verified; source [DR Aviso 29926-A/2025/2](https://diariodarepublica.pt/dr/detalhe/aviso/29926-a-2025-964380181))

---

## Section: `--rental`

### Long-term residential

- **NRAU (Novo Regime do Arrendamento Urbano)**: tenant protection moderate
- Standard contract: 5-year minimum (loose)
- **Pacto de preferência** (preemption rights for tenants under conditions)
- Recent reforms 2023-2026: trying to encourage long-let supply — rental-income rate 25 % for habitational leases (Lei 56/2023) and 10 % for moderate-rent housing leases on income earned 2026-2029 (EBF art. 45.º-C, DL 97/2026); see IRS on rental under `--tax`

### Short-let — Alojamento Local (AL)

**Mandatory registration via município**:
- Categories: Apartamento, Moradia, Estabelecimento de Hospedagem
- License fee per município
- VPT compatibility check

**LISBON — RMAL 2nd amendment (Aviso n.º 29926-A/2025/2, DR n.º 235/2025 Supl. 2.ª série, in force 6 Dec 2025)**:
- Replaced the 2024–25 ad-hoc AL suspension with a **permanent monthly ratio-based containment system**: **contenção absoluta** where AL ≥ 10 % of dwellings (threshold cut from 20 %), **contenção relativa** where 5–10 % (cut from 10 %) — current bands per Aviso 29926-A/2025/2 text; prior 20 %/10 % thresholds corroborated by CML, which states the alteration halves both ratios (CML news 27 Nov 2025), and by a law-firm note (secondary)
- **Sale-triggered caducidade**: transmission (sale) of a *moradia*/*apartamento* AL registration in a containment zone triggers automatic **caducidade** (expiry) — the registration is **non-transferable** to the buyer; a fresh registration must be requested, subject to the zone's rules, except RJEEAL legal exceptions. (2026-07-02 verified; source [DR Aviso 29926-A/2025/2](https://diariodarepublica.pt/dr/detalhe/aviso/29926-a-2025-964380181))
- Post-Apr-2026 freguesias — **absolute**: Santa Maria Maior (66.9 %, Nov-2025 data), Misericórdia, Santo António; **relative**: São Vicente, Arroios (moved absolute→relative), Estrela; Avenidas Novas left containment; plus 22 bairros absolute + 11 relative *(freguesia list per Público via ECO, 6 Apr 2026 + AL industry guides; ECO 30 Jul 2026 gives a different list — absolute Santa Maria Maior, Misericórdia, Alcântara, Estrela, São Vicente; relative Arroios, Santo António, Campo de Ourique — same-tier secondary conflict; the Anexo IV map and bairro list exist only as images in DR Aviso 29926-A/2025/2 and are updated by CML deliberation on monthly ratio monitoring, and no post-Apr-2026 update was found in a primary source as of 2026-10-21 — bairro tiers: data not publicly available in text form, verify at CML)*
- **Feb-2026 insurance cull**: 6,765 Lisbon AL registrations cancelled for missing compulsory civil-liability insurance; 11,774 remain active
- **Porto**: Regulamento Municipal para o Crescimento Sustentável do AL (Reg. 495-A/2023, back in force via Regulamento n.º 1462/2024, in force 20 Dec 2024) — áreas de contenção (pressure ratio ≥15 %): Vitória, São Nicolau, Sé, Santo Ildefonso, Miragaia, where new AL needs exceptional authorisation (Reg. art. 5) except 'quartos' mode; the other 10 freguesias, incl. Cedofeita, are sustainable-growth areas with a per-freguesia numerus clausus (CM Porto AL map read 2026-10-21: Cedofeita 10.1 %, numerus clausus 775)
- **Algarve coast**: regulated but largely still possible

### Tax on AL

- **IRS**: AL income is **category B by default**, with an option to be taxed under category F rules:
  - Cat. F (by option): whether the 25 % habitational rate or the 28 % rate (CIRS art. 72.º n.º 2 / n.º 1 e)) applies to AL under this option was not verified as of 2026-10-23 — verify with AT; AL does not qualify for the 10 % EBF art. 45.º-C rate (housing-only leases)
  - Cat. B (default): taxed as business income
- **IVA**: 6 % accommodation services (continental); 4 % Açores, 9 % Madeira
- **Taxa turística**: per município (Lisboa €4/night/person, Porto €3, Faro €2 — confirm current rate with each Câmara Municipal)

### Strategic notes

- **Algarve season concentration** — est. 60-70 % of revenue in Apr-Oct (based on Algarve seasonal-occupancy patterns — verify with Turismo de Portugal / INE occupancy data)
- **Lisboa AL** under RMAL containment regime (since 6 Dec 2025) — sale triggers caducidade in containment zones — verify per freguesia/Anexo IV before buying for AL strategy
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
- **SMN (Salário Mínimo Nacional) 2026**: €920/mo Continente (DL 139/2025; 14 payments = €12,880/yr; net €818.80 after 11 % SS); Açores €966 (+5 % regional rule); Madeira €980 (DLR 1/2026/M, effects 1 Jan 2026). Tripartite accord path: €970 (2027), €1,020 (2028). (2026-07-03 verified; sources DGERT/DL 139/2025 + DR DLR 1/2026/M)

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
| **DGT (Direção-Geral do Território)** — Carta de Perigosidade de Incêndio Rural, five hazard classes («muito baixa» to «muito alta») under DL 82/2021 of 13 Oct as amended by DL 49/2022 of 19 Jul (SIGFR); «alta» and «muito alta» form the **APPS**, mandatorily carried into the *plantas de condicionantes* of territorial plans. Methodology published by **ICNF** | `https://www.dgterritorio.gov.pt/atividades/paisagem/ptp/carta-perigosidade-incendio-rural` | Wildfire hazard — buildability-relevant (2026-09-18 verified) |

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

- **ERSAR (Entidade Reguladora dos Serviços de Águas e Resíduos)**: `https://www.gov.pt/entidades/entidade-reguladora-dos-servicos-de-aguas-e-residuos` — national regulator
- **Águas de Portugal Group** (state-owned multi-region utility): `https://www.adp.pt/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
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
| **IMT (primary, €300k bracket)** | **€10,542** (computed, 2026 HPP table) |
| **IMT (other, same)** | **€11,605** (computed, 2026 non-HPP table; a non-resident buyer pays the flat 7.5 % unless a CIMT art. 17.º n.º 10 exception applies) |
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
- **NHR/IFICI (Incentivo Fiscal à Investigação Científica e Inovação)**: NHR closed to new entrants by **Lei n.º 82/2023 (OE 2024) Art. 236.º** (transitional 2024 entry under specified conditions). IFICI established by **EBF Art. 58.º-A** and regulated by **Portaria n.º 352/2024/1 de 23 de dezembro** — narrower successor for scientific research, qualified jobs in productive investment, technology, startups (NOT pensions; NHR pension exemption eliminated). IFICI is single-use: not applicable to prior NHR or "Regressar" beneficiaries. Portaria 352/2024/1 was amended by **Portaria n.º 52-A/2025/1 (de 25 de fevereiro de 2025, in force 26 Feb 2025)** — procedural only: adds Art. 4.º/4 routing the inscription request and communication of alterations through the Portal das Finanças; eligible activities and benefits (20 % flat on qualified PT-source income, foreign-income exemption, 10 years non-renewable, pensions excluded) unchanged. (2026-07-03 verified; sources [Portaria 352/2024/1 — sgeconomia.gov.pt](https://www.sgeconomia.gov.pt/destaques/portaria-n-35220241-de-23-de-dezembro-regulamenta-o-regime-de-incentivo-fiscal-a-investigacao-cientifica-e-inovacao-previsto-no-artigo-58-a-do-estatuto-dos-beneficios-fiscais.aspx...) + DR Portaria 52-A/2025/1)

## Common listing platforms

- **Idealista PT** — biggest, full extraction
- **Imovirtual, Casa Sapo** — major
- **Engel & Völkers PT, Sotheby's, Predibisa** — premium
- **OLX, CustoJusto** — privates

## Caveats unique to PT

- **Golden Visa (ARI) real-estate routes abolished Oct 2023** (Lei 56/2023, in force 7 Oct 2023) — residential AND commercial property routes are gone; the remaining routes (non-real-estate funds ≥500k EUR, research ≥500k EUR, culture ≥250k EUR, company capital + 5 jobs, 10 jobs) may not be directed, directly or indirectly, at real estate (2023 law, source Lei 23/2007 art. 3.º n.º 5 + AIMA ARI page)
- **NHR/IFICI 2024** restructured — no longer the broad 10-yr exemption regime
- **AL containment Lisbon** (RMAL 2nd amendment, in force 6 Dec 2025 — sale triggers caducidade in containment zones) — verify per freguesia/Anexo IV before buying for AL
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
| Confidencial Imobiliário | `https://www.confidencialimobiliario.com/` |
| ANEPC | `https://prociv.gov.pt/` |
| APA | `https://apa.pt/` |
| IPMA | `https://www.ipma.pt/` |
| ERSAR | `https://www.gov.pt/entidades/entidade-reguladora-dos-servicos-de-aguas-e-residuos` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-09-17 (non-resident IMT surcharge re-verified against AT consolidated CIMT + Ofício Circulado 40131/2026 — effective date settled at 25 May 2026, exception (a) corrected to past residence; balance unchanged) · previously 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; wildfire-hazard authority (DGT) corrected 2026-09-18 per dgterritorio.gov.pt). Rental / visa tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md). Rental / tax / visa tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Rental-income IRS rates (CIRS art. 72.º 25 % / EBF art. 45.º-C 10 %) and the 2026 non-HPP IMT bands corrected 2026-10-23 per the AT consolidated codes; OE2027 IMT indexation proposal logged as not adopted. IRS-on-rental rates re-verified 2026-10-23 against AT CIRS art. 72.º and EBF art. 45.º-C (10 % moderate-rent housing-lease rate added).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (Cadastro modernization ongoing but Finanças stable; APA + IPMA well-maintained). MEDIUM-HIGH for AL regulation (Lisbon RMAL containment in force since 6 Dec 2025; Porto + Algarve evolving).

## Extension TODOs

- [ ] Per-município IMI rate tables + current AL availability map
- [ ] Per-distrito wildfire risk classification (post-2017 reform)
- [ ] Tsunami zone Algarve detail (parcel-level)
- [ ] Direito de preferência triggers per ARU
- [ ] Erosão costeira projections per município
- [ ] NHR/IFICI 2024 eligibility decision tree
- [ ] AL license availability per Lisboa freguesia (changing)
- [ ] Caderneta vs Registo mismatch detection
