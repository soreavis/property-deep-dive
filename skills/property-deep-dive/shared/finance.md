# Universal `--finance` Section

Foreign-buyer mortgage availability, LTV caps for non-residents, current rate environment, FX-loan rules across all 44 supported countries.

**Snapshot**: April 2026. Rates move monthly — treat as point-in-time.

**Anti-hallucination**: every claim should be cross-checkable against the cited primary source. Where this section's value is not specific enough for a transaction, the per-country playbook + bank's published tariff is authoritative.

## Universal contract

For the property's country, return:
1. **Foreign-buyer access**: yes / restricted / effectively cash-only / banned
2. **LTV cap (non-resident)**: % vs resident benchmark + deposit needed
3. **Indicative 10-yr fixed rate** (Apr 2026)
4. **FX-loan rules** (post-2008 CHF crisis legacy where applicable)
5. **Banks with non-resident desks**
6. **Key caveats**: DTI cap, age limits, tax-ID requirement, min income, processing time
7. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Finance Profile (Foreign Buyer)

**Country**: <ISO2>
**Foreign-buyer access**: <yes | restricted | effectively cash-only | banned>
**LTV cap (non-resident)**: <%> — deposit <%>
**10-yr fixed rate (Apr 2026, indicative)**: <range>
**FX-loan rules**: <free | restricted | banned post-CHF-crisis>
**Banks with non-res desks**: <list>
**Key caveats**: <DTI cap, age limit, tax-ID, processing>
**Confidence**: <HIGH/MEDIUM/LOW>
**Sources**: <URLs>
```

---

## Regional patterns

### Western Europe (FR, IT, ES, PT, DE, AT, CH, NL, BE, LU, IE, UK, GR, MT, CY)
Mortgages broadly available to non-residents but LTV caps drop 10–30 ppts vs residents. Eurozone 10-yr fixed clusters in **3.0–4.5%** band Apr 2026 (ES at low end ~2.55–4.0%, DE 3.5–5%, FR 3.3–3.8%). UK BoE base **3.75%** (held since Dec 2025 after Iran-conflict energy shock); UK expat residential ~4.0–6.0%. Switzerland is the outlier — SNB policy rate **0.00%** Mar 2026; 10-yr CHF mortgages **~1.4–2.0%** but non-resident LTV capped 50–65%.

### CEE / Baltics (CZ, SK, PL, HU, RO, BG, SI, EE, LV, LT, HR)
All EU. EU nationals near-resident terms with local income; non-EU pure-non-residents face 50–70% LTV. **FX-loan history is dominant policy memory**: PL CHF ban + ~700k Frankowicze, HU 2014 forced conversion + retail FX ban since 2010, HR Sept 2015 forced CHF→EUR conversion (now eurozone since Jan 2023), RO Oct 2016 forced CHF conversion at issuance-date FX. SK and CZ never had material CHF retail crisis. Rates **3.5–7.5%** for foreigners; HU highest (6–9%).

### Nordics (SE, FI, NO, DK, IS)
Mortgages available but strongly biased toward local-employment income. SE legal LTV cap 85% but banks internally apply 60–80% non-resident. NO 60–75% non-resident vs 85–90% resident. DK has best-in-world mortgage-bond system but secondary-residence and bopælspligt (residence requirement) constrain non-EU buyers. IS post-2017 capital-controls lifted; ISK volatility means foreign-currency-indexed structures common.

### Western Balkans (RS, ME, BA, MK, AL)
Non-resident lending case-by-case, harder, more expensive than EU. **Most foreign buyers pay cash.** Serbia NBS rules limit non-residents (Banca Intesa/Raiffeisen/OTP cited as most foreigner-friendly). ME has CKB, Hipotekarna, Lovćen Banka (dedicated non-resident product), Universal Capital Bank. BA limited specialist desks. AL has explicit deposit minimums: 15% lek primary residence, 25% euro loan.

### Anglo non-EU (CA, AU, NZ)
All three have **explicit foreign-buyer purchase restrictions**, not just lending caps. CA Prohibition Act extended through **1 Jan 2027**. AU **temporary ban on established/pre-owned dwellings through 31 Mar 2027** plus FIRB fees from AUD 15,100 plus state surcharges. NZ Overseas Investment Act 2018 bans most non-residents from existing homes; AU + SG citizens/PRs exempt; new builds OK.

### Latin America (MX, BR, AR, CR, PA)
Mortgages exist but expensive and paperwork-heavy → practical reality is **cash market** for most international buyers. MX 9% MXN, 30–50% deposit non-resident. BR 9.5–14.5% (Selic **14.75%** Mar 2026, cuts paused after Iran shock); CPF + permanent residency (CRNM) effectively required. AR rates 25–38% UVA peso → properties priced in USD, foreigners pay cash. CR 6–9% USD/7–10% CRC, up to 65% LTV. PA USD-dollarized, 60–70% LTV non-resident.

---

## Country tables

### Western Europe

| ISO | Access | LTV (non-res) | 10-yr fixed (Apr 2026) | FX-loan rules | Banks for non-res | Key caveats |
|---|---|---|---|---|---|---|
| **FR** | yes | 70–80% EU/UK; 50% non-EU | ~3.3–3.8% (20-yr 3.50–4.25%) | free, EUR | BNP Paribas Int'l Buyers, CFF (BPCE), Crédit Agricole Britline, SocGen, HSBC France | HCSF DTI ≤35%, max 25y; assurance emprunteur required |
| **IT** | yes (restricted profile) | 50–60% (40–50% deposit) | ~3.5–4.5% fixed; 6.10–6.80% variable non-res | free, EUR | Intesa Sanpaolo, UniCredit, BNL BNPP, Banco BPM | Codice Fiscale; non-res higher purchase tax (9% vs 2%); 8–12 wk processing |
| **ES** | yes | 60–70% | ~2.55–4.0% (LTV>65% starts above 4%) | free, EUR | BBVA, Santander, CaixaBank, Sabadell, Bankinter, ING España | NIE; DTI ≤35%; max 20–25y; 30–40% deposit |
| **PT** | yes | 60–70% | ~3.0–4.5% | free, EUR | Caixa Geral de Depósitos, Millennium BCP, Novobanco, Santander Totta, BPI | NIF; max 30y non-res; spread +0.3–0.7 ppts vs resident |
| **DE** | yes (restricted) | 50–60% | ~3.5–5.0% | free, EUR | Sparkasse expat units, Hypothekenbank Frankfurt, DB private, Commerzbank, Interhyp | SCHUFA history; 3.5–6.5% Grunderwerbsteuer + Notar |
| **AT** | restricted (Bundesländer rules) | 65–75% | 3.2–4.2% (well-doc 3.4–3.8%) | free; FMA discouraged FX retail since 2008 | Erste, Raiffeisen, BAWAG, UniCredit Bank Austria | Grundverkehrsgesetz approval per Land for non-EU; secondary-residence restrictions Tirol/Salzburg/Vbg |
| **CH** | yes (residents); restricted (non-res Lex Koller) | 50–65% non-res | **~1.4–2.0%** (SNB policy 0.00%) | free, usually CHF | UBS, Raiffeisen, Migros Bank, Cantonal banks (ZKB, BCV) | Tragbarkeit ≤33% imputed at 5% theoretical rate; 20% min equity (10% non-pension); Lex Koller cantonal permit |
| **NL** | yes | 70–90% (vs 100% NHG ≤€470k 2026) | 3.51–4.79% fixed | free, EUR | ABN AMRO, ING, Rabobank, Expat Mortgages | BSN; Dutch employment contract preferred; max LTI 4–5x |
| **BE** | yes | 70–80% (no statutory cap; banks 80–90% rare) | ~3.1–3.7% [Statista 5–10y series] | free, EUR | BNP Paribas Fortis, KBC, Belfius, ING Belgium, Argenta | Region-dependent registration tax 3–12.5%; quotités d'emprunt rules |
| **LU** | yes | 80% typical | short-mid fixed falling, >25y rising (BCL Jan 2026) | free, EUR | Spuerkeess (BCEE), BGL BNP Paribas, BIL, ING LU, Banque de Luxembourg | High prices stress LTI; 7% notary+registration; cross-border-worker income often accepted |
| **IE** | yes | 50–80% | 3.4–5.0% (non-res +0.25–1 ppt) | free, EUR | Bank of Ireland, AIB, PTSB, Avant Money, Finance Ireland | Central Bank LTI rules (4x FTB / 3.5x sub); PPS number; Irish-source income preferred |
| **UK** | yes | 70–75% residential / 60% BTL >£1m | residential expat ~4.0–5.5%; BTL ~4.2–6%; BoE base **3.75%** | free; FX-income via expat specialists | HSBC Expat, NatWest Int'l, Barclays Int'l, Skipton Int'l, Santander Int'l (Jersey) | SDLT non-res surcharge **+2%** on top of additional-property +3%; max age ~75 |
| **GR** | yes | **50% of taxation value** (often 30–40% market) | 3.0–6.5% | free, EUR | Alpha Bank, NBG, Eurobank, Piraeus | AFM; Golden Visa thresholds €800k/€400k 2024; processing 3–6 mo |
| **CY** | yes | 60–70% non-EU; 80% primary | 4.15–4.75% variable; CB Cyprus avg Feb 2026 **3.45%** | free, EUR | Bank of Cyprus, Hellenic Bank, Eurobank Cyprus, Alpha Bank Cyprus | Council of Ministers permit non-EU (formality); "Green" mortgage discounts 0.10–0.25 ppts |
| **MT** | yes (AIP permit non-EU outside SDA) | **65% non-res (HSBC Malta)**; up to 80% strong profiles | ~3.5–4.5% [unverified specific 10-yr] | free, EUR | HSBC Malta, Bank of Valletta, APS, Lombard | AIP permit non-EU; SDA units exempt; max ~25y |

### CEE / Baltics

| ISO | Access | LTV (non-res) | 10-yr fixed (Apr 2026) | FX-loan rules | Banks for non-res | Key caveats |
|---|---|---|---|---|---|---|
| **CZ** | yes (EU near-resident) | 85% from non-risky countries; 60% investor | ~4.0–4.5% (CBA Hypomonitor avg <4.5% late 2025) | CZK; EUR retail rare | Česká spořitelna (Erste), ČSOB (KBC), KB (SocGen), Raiffeisenbank, Hypoteční banka | **CNB Apr 2026: 3rd+ property or pure-rental capped at 70% LTV**; <36yr FTB up to 90% |
| **SK** | yes (EU/EEA preferred) | 70–80% (90% rare quota) | ~3.8–4.6% (NBS lending rate Jan 2026 **3.79%**) | EUR (eurozone since 2009); never had CHF retail crisis | VÚB (Intesa), Slovenská sporiteľňa (Erste), Tatra (Raiffeisen), ČSOB SK, UniCredit SK | NBS rules — DSTI ≤60%, DTI ≤8x; >90% LTV ≤20% of new lending quarterly |
| **PL** | yes (EU; non-EU often need MSWiA permit) | 60–80%; foreign-income often 50–60% | ~6–8% [unverified specific 10-yr] | **CHF retail ban post-2015**; PLN only; ~700k "Frankowicze" households | PKO BP, mBank, Pekao, ING Bank Śląski, Santander Polska | "Bezpieczny Kredyt 2%" was domestic-only; foreign-income haircut 20–30% |
| **HU** | yes (NAV/local permit non-EU) | 50–70% [estimate] | **6–9% APR non-residents** | **FX retail ban 2010**; 2014 forced conversion; HUF only | OTP Bank, K&H (KBC), MBH Bank, Erste HU, Raiffeisen HU | CSOK Plusz subsidies resident-only; HUF volatility = real FX risk on EUR/USD income |
| **RO** | yes (EU; non-EU need SRL for land, buildings OK direct) | 60–75% non-EU; 75–85% EU+local | 5.5–7.5% RON | **CHF force-converted Oct 2016**; today RON or EUR | Banca Transilvania, BRD-SocGen, BCR-Erste, Raiffeisen RO, ING RO | Prima Casă successor scheme local-only; CNP/NIF required |
| **BG** | yes (EU; non-EU restricted on land) | 60–70% non-res [broker]; 80% residents | 3.5–5% foreigners (locals 2.7–3.2%) | EUR or BGN; **BGN→EUR conversion 1 Jan 2026** | UniCredit Bulbank, DSK Bank (OTP), Postbank (Eurobank), Raiffeisen BG, Fibank | Bulgaria entered eurozone **1 Jan 2026** — verify dual-display + contract repricing |
| **SI** | yes (EU) | 50–70% | 3.5–5.0% (foreigners +0.5–1.5 ppts) | EUR (eurozone since 2007) | NLB, NKBM (OTP), SKB (OTP), Sparkasse SI, Intesa Sanpaolo SI | BS regulator caps DSTI ~50%; non-EU reciprocity check on land |
| **EE** | yes (EU) | 60–80% | 4–6% (Euribor+margin) | EUR (eurozone since 2011) | Swedbank, SEB, LHV, Luminor, Coop Pank | e-Residency does NOT confer mortgage access |
| **LV** | yes (EU) | 60–80% | 4.8–6.5% (Euribor+margin) | EUR (eurozone since 2014) | Swedbank, SEB, Citadele, Luminor | English-language docs at top 4 banks |
| **LT** | yes (EU) | 60–85% (statutory cap 85%) | 3.5–4.5% all-in foreigners | EUR (eurozone since 2015); ESRB-notified macroprudential 85% LTV | Swedbank, SEB, Luminor, Citadele | Bank of Lithuania DSTI rules; clear purpose-of-purchase needed non-res |
| **HR** | yes (EU) | 60–70% | ~3–4.5% (mid-3% avg) | **2015 forced CHF→EUR/HRK conversion**; eurozone since **1 Jan 2023** | Zagrebačka banka (UniCredit), PBZ (Intesa), Erste HR, OTP HR, Raiffeisen HR | Certified translation often needed; max 25–30y; closing ~5% |

### Nordics

| ISO | Access | LTV (non-res) | 10-yr fixed (Apr 2026) | FX-loan rules | Banks for non-res | Key caveats |
|---|---|---|---|---|---|---|
| **SE** | yes (Swedish-employment biased) | 60–80% practical (legal cap 85%) | 2.9–4.0% (non-res +0.1–0.9 ppts) | SEK; FX retail rare | SEB, Handelsbanken, Swedbank, Nordea, SBAB, Länsförsäkringar | 2x amortisation rules (LTV>50% → 2%/yr; >70% → 3%/yr); DTI>4.5x triggers extra |
| **FI** | yes | 65–75% (vs ~85% resident) | 3.5–4.5% [unverified specific] | EUR (eurozone since 1999) | OP Financial Group, Nordea, Danske Bank FI, Handelsbanken FI, Aktia | FIN-FSA loan-cap 90% first-home (95% with state guarantee); 85% other |
| **NO** | yes | 60–75% (vs 85–90% resident) | ~5–6% [Norges Bank policy 4.0%] | NOK; FX retail rare | DNB, Nordea NO, Sparebanken Vest/Sør, Handelsbanken NO | Boliglånsforskriften — DTI ≤5x, stress-test +3 ppts, 5%/yr amortisation if LTV>60% |
| **DK** | EU residents only without permit; non-EU need Justitsministeriet permit + 5y residence | 80% mortgage-credit-institute portion; lower for non-res | 4–5% [unverified specific] | DKK (pegged narrow ±2.25% to EUR) | Danske Bank, Nordea DK, Jyske Bank, Sydbank, Nykredit | Bopælspligt residence requirement on many homes |
| **IS** | yes EEA/EFTA; non-EEA need Min Justice permit | 80% standard | 7–10% ISK; FX-indexed available | post-2008 capital controls **lifted Mar 2017** | Landsbankinn, Íslandsbanki, Arion banki, Kvika | Kennitala required; 10%/yr ISK volatility typical; small market |

### Western Balkans

| ISO | Access | LTV (non-res) | 10-yr fixed (Apr 2026) | FX-loan rules | Banks for non-res | Key caveats |
|---|---|---|---|---|---|---|
| **RS** | restricted (NBS rules; reciprocity) | 50–70% [broker] | 5.5–7% RSD or EUR-indexed [estimate] | EUR-indexed common; full FX restricted | Banca Intesa Beograd, Raiffeisen Serbia, OTP Bank Serbia, UniCredit Serbia, Erste RS | Most foreign buyers pay cash; diaspora with local banking history preferred |
| **ME** | yes | 50–80% (40–50% deposit common) | 5–7% EUR loans [estimate] | **EUR (unilaterally adopted 2002)** — no central-bank issuance | CKB (OTP), Hipotekarna Banka, Lovćen Banka (dedicated non-res), Universal Capital Bank, NLB ME, Erste ME | Title/cadastre due diligence weak; coastal-zone restrictions |
| **BA** | yes (reciprocity) | 50–70% [unverified] | 4.5–6.5% [unverified specific] | BAM-currency-board pegged to EUR (1.95583); BAM or EUR-indexed | UniCredit Bank BA, Raiffeisen BA, Intesa Sanpaolo Banka BA, Sparkasse BA, NLB Banka | Federation vs RS legal frameworks differ; cadastral inconsistencies |
| **MK** | yes (reciprocity) | 50–70% [unverified] | 4.5–6.5% [unverified specific] | MKD de-facto pegged to EUR ~61.5±1%; EUR-indexed common | Komercijalna Banka, Stopanska Banka (NBG), NLB Banka, ProCredit, Halkbank MK | Thin foreign-buyer market; docs in Macedonian; local lawyer essential |
| **AL** | yes (since 2016 reform; outside protected zones) | 60–75%; **deposit min 15% lek/25% euro** | 5–8% (lek loans higher than euro) | free; lek + euro both used | BKT, Credins Bank, Raiffeisen AL, Intesa Sanpaolo AL, OTP AL | Hard for pure non-residents w/o local ties; coastal-zone planning checks; informal-construction cadastre risk |

### Anglo non-EU

| ISO | Access | LTV (non-res, where exempt) | 10-yr fixed (Apr 2026) | FX-loan rules | Banks for non-res | Key caveats |
|---|---|---|---|---|---|---|
| **CA** | **Effectively banned through 1 Jan 2027** (Prohibition Act extended Dec 2025) | 50–65% (PR/work-permit/exempt) | 5.0–6.5% [unverified specific] | CAD; FX rare | RBC, TD, Scotiabank Int'l, BMO, CIBC, HSBC Canada (run-off post-RBC acq 2024) | Provincial NRSTs (BC 20%, ON 25%); review 2026 considering AU-style FIRB post-2027 |
| **AU** | **FIRB-required + ban on established homes through 31 Mar 2027** | 50–70% specialist lenders | 5y fixed common ~6.0–7.0% non-res (10y rare); +0.5–2 ppts vs resident | AUD; FX rare | Specialist brokers/Citadel; majors (CBA/Westpac/NAB/ANZ) tightened or exited post-2018 | FIRB fees from AUD 15,100; state surcharges (NSW +9%, VIC +8%, QLD +8%); absentee land-tax |
| **NZ** | **Banned for existing homes since 2018** (OIA Amendment Act); AU+SG citizens/PRs exempt; new builds OK | 60–70% (resident 80%) | 5.5–7% [unverified specific] | NZD; FX rare | ANZ NZ, ASB (CBA), BNZ (NAB), Westpac NZ, Kiwibank | OIO consent for sensitive land; resident test 183 days/yr; 30–40% deposit non-res |

### Latin America

| ISO | Access | LTV (non-res) | 10-yr fixed (Apr 2026) | FX-loan rules | Banks for non-res | Key caveats |
|---|---|---|---|---|---|---|
| **MX** | yes outside 50km coastal/100km border restricted zones (fideicomiso required) | 50–70% | ~9–11% MXN; USD private banking 7–9% | MXN typical; USD via private banking | BBVA México, Banamex (Citi), Santander México, HSBC México, Scotiabank Inverlat, MoXi/Global Mortgage cross-border | Fideicomiso ($600–800/yr) restricted-zone; CURP+RFC; max 30y |
| **BR** | yes (CPF; rural land Lei 5709 restricted) | 30–60% (40–50% deposit typical) | 9.5–14.5% (Selic 14.75% Mar 2026, cuts paused on Iran shock) | BRL; IOF tax incoming transfers | Caixa Econômica Federal, Itaú Unibanco, Bradesco, BB, Santander Brasil | Most foreign buyers cash; CPF mandatory; max 30y |
| **AR** | yes (no ban) but mortgages **practically unobtainable** for pure non-res | 50–70% UVA peso (where qualified) | **25–38% UVA peso** — most foreign buyers ignore and pay USD cash | **Capital controls largely lifted 14 Apr 2025** (see `--currency`) | Banco Nación, Galicia, Santander Río, BBVA AR, ICBC AR — UVA designed for residents | UVA index ties principal to inflation; "vivienda de uso permanente" excludes most foreign use |
| **CR** | yes (oceanfront 200m maritime concession rules) | up to **65%** (40–50% deposit) | USD **6–9%**; CRC **7–10%** | USD or CRC; managed-band currency | Scotiabank Costa Rica, BAC Credomatic, Banco Promerica, Banco Nacional CR, Davivienda CR | Titled vs concession critical; closing 3–4%; max often 20y |
| **PA** | yes (very few restrictions) | 60–70% | ~6–8% USD | USD (paper currency) | Banco General, Banistmo (Bancolombia), BAC Credomatic Panama, Scotiabank Panama, Multibank | Apostilled income docs; international credit reports; 30%+ deposit |

---

## Cross-cutting risks to flag

1. **FX-loan denomination vs income currency mismatch** — single biggest retail-borrower trap of last 20 years (CHF crisis). **Always cross-check `--finance` "FX-loan rules" against `--currency` "Currency code".**
2. **Foreign-buyer purchase bans dressed up as 'mortgages restricted'** — CA/AU/NZ rows make this explicit so a buyer doesn't conflate "70% LTV available" with "you can legally purchase".
3. **Eurozone accession transition (BG)** — contract repricing, dual-display deadlines, mortgage payment switchover are live April 2026 issues.
4. **Sanctions / PEP / AML overlay** in RS, AR, BR, BA, ME — non-resident mortgage approval depends on KYC/AML far more than rate.

## Confidence labels

- **HIGH**: rate band verified against bank or broker source within last 90 days
- **MEDIUM**: source 90 days–12 months old, or is a broker quote with regional plausibility
- **LOW**: source >12 months old or unverified specific rate

## Status

Last refreshed: 2026-04-26. Next refresh recommended: monthly (rates), quarterly (LTV/AML rules), per-event (regulatory reform).
