# Universal `--currency` Section

Currency code, peg status, FX volatility, capital controls, hedging market depth, 2025-26 currency reforms across all 62 supported countries.

**Snapshot**: April–May 2026.

**Anti-hallucination**: pegs and adoption dates verified to ECB / central-bank / BIS sources where possible. Live exchange rates are point-in-time and can move.

## Universal contract

For the property's country, return:
1. **Currency code + peg status**
2. **FX volatility 2024-2026**: stable / moderate / high
3. **Capital controls**: status
4. **Hedging market depth**: deep / moderate / thin
5. **2025-2026 reforms**: relevant changes with effective dates
6. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Currency Profile

**Country**: <ISO2>
**Currency code + peg status**: <code> (<peg or float regime, conversion rate if pegged>)
**FX volatility 2024–26**: <stable | moderate | high>
**Capital controls**: <status>
**Hedging market depth**: <deep | moderate | thin>
**2025–26 currency reforms**: <changes with effective dates>
**Confidence**: <HIGH/MEDIUM/LOW>
**Sources**: <URLs>
```

---

## Regional patterns

### Eurozone (FR, IT, ES, PT, DE, AT, NL, BE, LU, IE, GR, MT, CY, FI, SI, EE, LV, LT, SK, HR, BG)
All EUR. Fully convertible, deep hedging market, no capital controls. Conversion rates locked at adoption. Latest accessions: SI (2007), CY+MT (2008), SK (2009), EE (2011), LV (2014), LT (2015), HR (1 Jan 2023), **BG (1 Jan 2026)**. **BGN→EUR conversion is the live story for the Apr 2026 due-diligence cycle** — verify exact dual-display deadline (~8 Aug 2026) and contract-repricing terms.

### Eurozone-pegged (DK, ME-de-facto, BA-currency-board, MK-de-facto)
DK is the **last ERM-II member** post-BG accession; DKK pegged to EUR at **7.46038 ±2.25%** (narrower than standard ±15%). BA runs a **currency board** at **1.95583 BAM/EUR** since 2002. ME is unilateral euroisation (2002, no central-bank issuance). MK has de-facto stabilised peg at ~61.5 MKD/EUR ±1% (formal IMF classification varies; not in ERM II).

### Floating EU non-euro (CZ, PL, HU, RO, SE)
CZK, PLN, HUF, RON, SEK all float with central-bank inflation targets. SE Riksbank rate **1.75%** (Apr 2026, paused after Sept 2025 cut). HUF most volatile of the bunch; PLN strengthened on cyclical catch-up. RON is a managed float (BNR intervenes more visibly than the others).

### Floating non-EU Europe (CH, NO, IS, UK)
CHF safe-haven status produced 12.7% USD strength in 2025 and an 11-year high vs USD Jan 2026 → SNB stated readiness to intervene. NOK/SEK driven by oil and rate differentials. ISK volatile on small-market dynamics; capital controls lifted Mar 2017. GBP under political-uncertainty premium 2026 with BoE expected to cut further.

### Western Balkans (RS, ME, BA, MK, AL)
Mix of managed-float-tight-to-EUR (RSD), unilateral euro (ME since 2002), currency board (BAM 1.95583), de-facto EUR peg ~61.5 (MKD), and free float (ALL). RS NBS amendments March 2025 strengthened oversight (AML/CTF); speculative FX trading prohibited. Hedging markets thin everywhere except RS for EUR/RSD.

### Anglo non-EU (CA, AU, NZ)
All free float; deep hedging. CAD ~oil-driven, AUD/NZD ~commodity + China, all G10.

### Latin America (MX, BR, AR, CR, PA, DO, CO, UY, CL)
MX free float (Banxico), deep market. BR free float with **IOF tax** on incoming foreign transfers. **AR's CEPO cambiario was largely dismantled 14 April 2025** — ARS now floats inside a **1,000–1,400 ARS/USD band with 1%/mo edge adjustments**, "dólar blend" abolished; "cepo individual" partial reinstatement appeared late 2025. CR managed float / managed-band, BCCR holds CRC near ₡500/USD via interventions. PA fully USD-dollarized since 1904 (balboa = coins only, 1:1 fixed by Article 262 constitution). **DO** managed-float (BCRD); USD parallel pricing universal in resort markets. **CO** free float (BanRep), COP swung 3,800–4,900/USD 2022–26. **UY** managed-float UYU but property transactions almost universally in USD billete; mortgages in **UI** (Unidad Indexada, CPI-linked unit, Ley 17.761). **CL** runs a dual-unit system — CLP for daily / salaries, **UF (Unidad de Fomento)** for property prices, mortgages and notarial sums (UF is a daily-indexed inflation unit set by Banco Central de Chile).

### Middle East / North Africa (AE, IL, EG, MA, TR)
**AE** AED USD-pegged at **3.6725 since 1997** (Central Bank of UAE) — zero structural FX risk vs USD, deep DFM/DIFC hedging. **IL** ILS free-float; Bank of Israel intervenes only in extreme moves; no capital controls but FX volatile during wartime (Oct-2023 onward). **EG** EGP managed-float since **6 March 2024** (IMF EFF USD 8 bn) — trajectory ~15.7 → 30 → 50/USD by Mar 2024 → ~50–51/USD May 2026. **CBE Form 4 (نموذج 4) is the binding mechanism**: USD inflows for property must transit a CBE-authorized bank with Form 4 issued, otherwise future repatriation is structurally blocked. **MA** MAD basket-pegged **60% EUR / 40% USD** since 2018 (band widened to ±5% in 2020); Bank Al-Maghrib gradually moving toward more flexible regime; **non-convertible — Office des Changes registration mandatory** at purchase via authorised bank to preserve repatriation rights. **TR** TRY managed-float with hyperinflation backdrop (TÜFE CPI ~64% YoY late 2024 → ~40% YoY late 2025 per TÜİK; TCMB one-week repo peaked 50% Mar 2024, cut through 2025). Foreign-buyer transactions widely quoted in USD/EUR; **MASAK** rules require all property purchases > 75k TRY to flow through a Turkish bank with FX dekont.

### Asia-Pacific (JP, TH, ID, MY, VN, PH)
**JP** JPY free-float, **BoJ NIRP exit Mar 2024 → policy rate 0.5% Jan 2025 → ~0.75% Dec 2025**; deep hedging market. **TH** THB managed-float (BoT); **FET form (Foreign Exchange Transaction, formerly Tor Tor 3 / ธ.ต.3)** mandatory at DOL transfer for any inbound transfer ≥ USD 50,000 — without FET, foreign condo purchase cannot register. **ID** IDR managed-float (Bank Indonesia); BI FX reporting for amounts ≥ USD 10,000; foreign-currency repatriation requires evidence of original inbound transfer. **MY** MYR managed-float (BNM); BNM FX rules generally permit repatriation with documentation. **VN** VND managed-float with daily SBV reference rate and **±5% trading band**; capital controls under the 2005 Ordinance on FX (amended 2013) and SBV Circular 06/2019/TT-NHNN — original-investment basis can be repatriated, but profit/gain in excess requires explicit SBV approval. **PH** PHP free-float (BSP); no FET-style form requirement (unlike Thailand) but BSP Manual on FX governs inward-remittance reporting ≥ USD 50,000.

### Caucasus (GE)
**GE** GEL Lari managed-float with NBG intervention. EU candidate status since Dec 2023; rate cycle now linked to ECB more visibly than to Fed. NBG operates inflation targeting; FX hedging market is thin (NDF availability via international counterparties only).

### Sub-Saharan Africa (ZA)
**ZA** ZAR free-float (SARB); regular EM volatility (typical 1 USD ≈ R18–R19 / 1 EUR ≈ R20 in 2025); deep hedging via JSE-listed FX derivatives. SARB Exchange Control via Authorised Dealers; foreign nationals' inward funds must be tagged at deposit to preserve repatriation route on resale.

---

## Country tables

### Eurozone members

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **FR** | EUR | Eurozone founder | stable | none | deep | — |
| **IT** | EUR | Eurozone founder | stable | none | deep | — |
| **ES** | EUR | Eurozone founder | stable | none | deep | — |
| **PT** | EUR | Eurozone founder | stable | none | deep | — |
| **DE** | EUR | Eurozone founder | stable | none | deep | — |
| **AT** | EUR | Eurozone founder | stable | none | deep | — |
| **NL** | EUR | Eurozone founder | stable | none | deep | — |
| **BE** | EUR | Eurozone founder | stable | none | deep | — |
| **LU** | EUR | Eurozone founder | stable | none | deep | — |
| **IE** | EUR | Eurozone founder | stable | none | deep | — |
| **GR** | EUR | Joined 2001 | stable | none (post-2018 lifted) | deep | Capital controls fully lifted Sep 2019 |
| **MT** | EUR | Joined 2008 | stable | none | deep | — |
| **CY** | EUR | Joined 2008 | stable | none (post-2015 lifted) | deep | — |
| **FI** | EUR | Eurozone founder | stable | none | deep | — |
| **SI** | EUR | Joined 2007 | stable | none | deep | — |
| **EE** | EUR | Joined 2011 | stable | none | deep | — |
| **LV** | EUR | Joined 2014 | stable | none | deep | — |
| **LT** | EUR | Joined 2015 | stable | none | deep | — |
| **SK** | EUR | Joined 2009 | stable | none | deep | — |
| **HR** | EUR | Joined **1 Jan 2023** at 7.53450 HRK/EUR | stable | none | deep (now) | Kuna coins exchangeable at HNB until end-2025; banknotes no time limit |
| **BG** | EUR | Joined **1 Jan 2026** | stable (post-conversion) | none | deep (now) | Pre-2026: BGN was pegged to EUR at **1.95583** since 1999 currency board; conversion locked at same rate; dual-display through ~8 Aug 2026 |

### EU non-euro

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **CZ** | CZK | floating, CNB inflation target | moderate | none | deep | CNB tightening macroprudential mortgage rules Apr 2026 |
| **PL** | PLN | floating, NBP inflation target | moderate | none | deep | CHF retail mortgage ban legacy ongoing in courts |
| **HU** | HUF | floating, MNB inflation target | high | none formally; MNB FX intervention frequent | moderate | HUF among most volatile EU FX; FX retail loan ban ongoing |
| **RO** | RON | managed float, BNR | moderate | none | moderate | BNR visibly intervenes more than CZK/PLN/HUF peers |
| **SE** | SEK | floating, Riksbank | moderate | none | deep | Riksbank rate **1.75%** Apr 2026 (paused after Sept 2025 cut) |
| **DK** | DKK | **ERM II ±2.25%** at 7.46038 DKK/EUR (narrowest band) | very stable | none | deep | **Last ERM II member** post-BG eurozone accession |

### Non-EU Europe

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **CH** | CHF | floating, SNB | low (but safe-haven appreciation) | none | deep | SNB policy rate **0.00%** Mar 2026; CHF +12.7% vs USD 2025; 11-yr high vs USD Jan 2026; SNB stated readiness to intervene |
| **NO** | NOK | floating, Norges Bank | moderate | none | deep | Norges Bank policy 4.0%; commodity-driven (oil) |
| **IS** | ISK | floating, Sedlabanki | high (small market) | **lifted Mar 2017** | thin–moderate | Post-2008 capital controls fully removed; ISK 10%+ annual range typical |
| **UK** | GBP | floating, BoE | moderate | none | deep | BoE Bank Rate **3.75%** held since Dec 2025 (Iran-conflict energy shock); markets price 2 further cuts in 2026 |

### Western Balkans

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **RS** | RSD | managed float, NBS (tight to EUR informally) | low–moderate | scrutiny on cross-border; speculative FX trading prohibited | moderate (EUR/RSD) | Mar 2025 amendments to Foreign Exchange Operations Law strengthened NBS oversight + new admin penalties (AML/CTF) |
| **ME** | EUR | **unilaterally adopted 2002** (no central-bank issuance) | n/a | none formal | deep (it's EUR) | Goal of EU + formal eurozone accession by 2028; ECB historically dissatisfied with unilateral use |
| **BA** | BAM | **currency board** at **1.95583 BAM/EUR** since 2002 (DEM peg before) | very stable | none formal | thin (BAM); deep (EUR pass-through) | CBBH currency board operates simple-rule purchase mechanism |
| **MK** | MKD | de-facto stabilised peg at ~**61.5 MKD/EUR ±1%** | very stable | none formal | thin | Live spot ~61.55–61.63 |
| **AL** | ALL | **floating**, Bank of Albania | moderate (sustained appreciation 2024–26) | gradually relaxed since 1990s | thin | IMF 2025 SVAR analysis: lek appreciation driven by fundamentals; BoA may intervene |

### Anglo non-EU

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **US** | USD | floating, Federal Reserve — **global reserve currency** | low (vs DXY basket) | **none** (FinCEN AML/BSA reporting only; FBAR for US persons' foreign accounts ≥ USD 10k); **OFAC sanctions** are the binding constraint, not capital controls | deepest in the world | Fed funds target **range 4.25–4.50%** held since the Dec 2024 cut cycle — verify at next FOMC; FATCA + CRS-equivalent reporting for non-resident buyers via FIRPTA withholding (15% of gross sale price) on disposition (IRS Form 8288) |
| **CA** | CAD | floating, Bank of Canada | moderate | none | deep | Commodity (oil) sensitivity |
| **AU** | AUD | floating, RBA | moderate | none | deep | China + commodity sensitivity |
| **NZ** | NZD | floating, RBNZ | moderate | none | deep | Trade-weighted basket of 17 partners |

### Latin America

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **MX** | MXN | floating, Banxico | moderate (but +11% vs USD YoY March 2026) | none | deep | Banxico cut 300 bps in 2025 (10→7%); USMCA review + carry-trade unwind = 2026 risk |
| **BR** | BRL | floating, BCB | moderate–high | **IOF tax on incoming foreign transfers** | deep (large EM) | Selic **14.75%** Mar 2026 (cuts paused on Iran-conflict energy shock); BRL strongest since Mar 2024 |
| **AR** | ARS | **managed band 1,000–1,400 ARS/USD with 1%/mo edge adjustments** since 14 Apr 2025 | high | **Most CEPO cambiario lifted 14 Apr 2025**; "dólar blend" abolished; "cepo individual" partial reinstatement late 2025 for individuals' dollar purchases | thin (improving post-reform) | Milei reforms — currency liberalisation; properties priced in USD; "blue dollar" still tracks |
| **CR** | CRC | managed float / managed-band, BCCR | low (BCCR maintains ~₡500/USD) | none formal | thin | Strong colón becoming policy problem; BCCR 2026 active intervention |
| **PA** | USD (PAB coins only, 1:1 fixed) | **fully dollarized since 1904** (Article 262 constitution) | n/a (= USD volatility) | none | deep (it's USD) | No competing currency authorized as of 2026 |
| **DO** | DOP (USD parallel) | managed-float, BCRD; ~60–63 DOP/USD (2025) | moderate | none formal | thin (DOP); deep (USD pass-through) | **USD parallel pricing universal** in Punta Cana / Cap Cana / Las Terrenas / Casa de Campo resort markets; non-tourist housing typically priced in DOP; 60-day-escrow FX shifts can move deal 2–3% |
| **CO** | COP | floating, BanRep | high (3,800–4,900/USD swing 2022–26) | none formal | moderate | BanRep policy 9.25% Apr 2026 (cuts through 2024–25 as inflation eased toward 3% target); dollarizing the deal pre-signing protects USD savings but is non-standard for sellers |
| **UY** | UYU + USD billete + UI | managed-float UYU; **property transactions almost universally in USD billete**; mortgages historically in **UI (Unidad Indexada, CPI-linked, Ley 17.761)** | moderate (UYU); none (USD) | none formal | thin (UYU); deep (USD) | Tax-residency threshold lowered by Decreto 138/020 + 153/020 (2020) to **UI 3,500,000** (~USD 525k at 2026 UI value — verify peg) with 60+ days physical presence; **trap**: USD billete (cash) vs USD wire — slight cash premium historically due to AML friction |
| **CL** | CLP + UF | floating CLP (BCCh); **UF (Unidad de Fomento) is the price-of-record unit for property + mortgages + notarial sums** — UF set daily by BCCh inflation-indexation rule | moderate (CLP); n/a (UF) | none formal | deep (CLP); n/a (UF, accounting unit) | **Convert UF→CLP at transaction date** (not signing date); USD sometimes used in commercial / luxury Santiago listings — confirm denomination in writing; UF mechanics at `https://www.bcentral.cl/inicio/-/asset_publisher/8Ki7yegxnFpW/content/uf-1` |

### Middle East / North Africa

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **AE** | AED | **USD-pegged at 3.6725 since 1997** (Central Bank of UAE) | very low (vs USD); meaningful vs EUR/GBP | none formal (sanctions / OFAC compliance only) | deep (DFM, DIFC, ADGM derivatives + bank desks) | Peg has held through 1997 Asian crisis, 2008 GFC, 2014–16 oil collapse, 2020 COVID, 2022 commodity spike — institutionally stable; VAT 5% on commercial property + STR turnover ≥ AED 375k/yr |
| **IL** | ILS | floating, Bank of Israel; intervention only in extreme moves | high (wartime volatility Oct 2023 onward) | none on residents/non-residents for property; AML KYC under Order 5761-2000 | deep (TASE-listed FX derivatives + bank NDFs) | BoI representative rates at `https://www.boi.org.il/he/Markets/ExchangeRates/`; non-resident mortgages typically in ILS but some banks offer USD/EUR with FX conversion at drawdown — wartime emergency tax orders since Oct 2023 |
| **EG** | EGP | **managed-float since 6 March 2024** (post-IMF EFF USD 8 bn) | very high (~15.7→30→50/USD by Mar 2024 → ~50–51/USD May 2026) | **CRITICAL — CBE Form 4 (نموذج 4) mandatory** for foreign-buyer USD inflow via authorised bank; without Form 4, future USD repatriation is structurally blocked or severely restricted | thin (NDF only via international banks); EGP-denominated liquidity limited | Pre-Mar 2024: heavy CBE intervention + parallel-market premium 50%+; post-float: parallel market collapsed but premium can re-emerge during EGP stress; rates at `https://www.cbe.org.eg/en/economic-research/statistics/exchange-rates`; **EGP depreciated ~70%+ vs USD 2021–24** — USD-cash buyers exposed if selling in EGP without Form 4 paper trail |
| **MA** | MAD | **basket-pegged 60% EUR / 40% USD** since Jan 2018 (Bank Al-Maghrib); fluctuation **band widened to ±5% in 2020** (gradual move toward floating) | low (intra-band) | **non-convertible for residents/foreigners — Office des Changes registration via authorised bank mandatory at purchase** (Instruction 02 du foreign-investment regime) for future repatriation rights | thin (BAM-mediated only; MAD NDFs limited) | Repatriation timing: dirham ≠ freely convertible — large sale-proceed repatriations take weeks of Office des Changes file processing; 1 EUR ≈ 10.8–11.0 MAD (2025 range); skipped registration at purchase = no future repatriation right (the **garantie de transfert** is documentation-driven) |
| **TR** | TRY | managed-float; **TÜFE CPI ~64% YoY late 2024 → ~40% YoY late 2025** (TÜİK); TCMB one-week repo peaked 50% Mar 2024, cut through 2025 | very high | **MASAK rules** require all property purchases > 75k TRY to flow through a Turkish bank with **FX dekont** if foreign-funded; foreign-buyer KDV exemption requires FX bring-in proof + 3-yr holding period (raised from 1 yr by Law 7456 of Jul 2023) | moderate (TRY NDFs deep; onshore deep but volatile) | Foreign-buyer transactions widely quoted in USD/EUR because of TRY hyperinflation — **verify TRY vs FX pricing on every listing**; Web Tapu enables online transfers but in-person at TKGM still standard for foreign-currency transactions |

### Asia-Pacific

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **JP** | JPY | floating, Bank of Japan | moderate–high (¥-yen weakness through 2022–24, ¥-yen recovery 2025–26 as BoJ tightens) | none | deep (G10) | **BoJ NIRP exit March 2024** ended -0.1% policy rate; **policy rate 0.5% (Jan 2025) → ~0.75% (Dec 2025)** — first hiking cycle since 2007; foreign-denominated buyers should hedge purchase + ongoing tax bills against JPY recovery |
| **TH** | THB | managed-float, Bank of Thailand | moderate (≈35–37/USD; 38–40/EUR Apr 2026) | **FET (Foreign Exchange Transaction Form, formerly Tor Tor 3 / ธ.ต.3) mandatory at DOL transfer** for inbound transfers ≥ USD 50,000 — without FET, foreign condo purchase cannot register | deep (offshore THB NDFs + onshore) | Outbound repatriation requires same FET evidence — not automatic; rates + rules at `https://www.bot.or.th/en/financial-markets/foreign-exchange-regulations.html`; foreign-quota mechanics interact with FX rule — both must be satisfied |
| **ID** | IDR | managed-float, Bank Indonesia (≈15,500–16,500/USD Apr 2026) | moderate–high | minimal — **BI FX reporting required for amounts ≥ USD 10,000**; foreign-currency repatriation needs evidence of original inbound transfer | moderate (NDFs offshore; onshore liquidity good) | Tax residency triggers at 183 days/12 months under UU PPh §2 — global income taxable; rates at `https://www.bi.go.id/` |
| **MY** | MYR | managed-float, Bank Negara Malaysia (≈4.4–4.7/USD; 4.8–5.1/EUR Apr 2026) | moderate | generally permissive — **BNM FX rules permit repatriation with proper documentation**; foreign-buyer property transactions must clear BNM FX policies | deep (MYR NDFs + onshore MYR-denominated derivatives) | RPGT 10% flat above year 5 for foreign sellers; verify BNM FX rules at `https://www.bnm.gov.my/exchange-rates` before signing |
| **VN** | VND | managed-float, **daily SBV reference rate with ±5% trading band** | moderate (high vs USD strength episodes) | **CRITICAL — SBV approval required for repatriation beyond original-investment basis**; original capital can be repatriated with bank documentation, profit/gain in excess requires explicit SBV licensing (2005 Ordinance on FX amended 2013 + SBV Circular 06/2019/TT-NHNN) | thin (NDFs offshore only; onshore VND derivatives limited) | Foreign-buyer purchase funds must be remitted from abroad in foreign currency, converted to VND in Vietnam via commercial bank (Circular 06/2019/TT-NHNN) — cash or third-party payments **block Pink Book issuance** |
| **PH** | PHP | floating, Bangko Sentral ng Pilipinas (≈56–59/USD; 60–64/EUR Apr 2026) | moderate (long-tail USD-policy correlation despite float regime) | none for property — **no FX-form requirement equivalent to Thailand's FET**; BSP Manual of Regulations on FX governs inward-remittance reporting ≥ USD 50,000 | moderate–deep (PHP NDFs + onshore; PSE-listed FX derivatives) | All Torrens TCT/CCT/OCT, Deed of Absolute Sale and Contract to Sell drafted in English (rare among SE-Asian markets — no sworn translation typically needed); rates at `https://www.bsp.gov.ph/SitePages/Statistics/ExchangeRate.aspx` |

### Caucasus

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **GE** | GEL (Georgian Lari) | managed-float, NBG with intervention; ~2.95–3.05/EUR; ~2.65–2.75/USD | moderate | none formal | thin (NDF availability via international counterparties only) | EU candidate status since **Dec 2023** (European Council); accession effectively paused mid-2024 after the "foreign agents" law and contested 2024 election (per EU Council conclusions Dec 2024) — rate-cycle linkage to ECB more visible than to Fed; **EU-accession trajectory drives medium-term GEL/EUR convergence narrative** |

### Sub-Saharan Africa

| ISO | Currency | Peg/regime | FX vol 2024–26 | Capital controls | Hedging | Reforms / notes |
|---|---|---|---|---|---|---|
| **ZA** | ZAR | floating, SARB | high (regular EM volatility; 1 USD ≈ R18–R19 / 1 EUR ≈ R20 typical 2025 — verify on day) | **SARB Exchange Control via Authorised Dealers** — foreign nationals' inward funds must be tagged at deposit to preserve repatriation route on resale; SARB regulations under Currency and Exchanges Act 1933 + Manual | deep (JSE-listed FX derivatives + bank desks) | 11 official languages but English dominates commerce/contracts/conveyancing; deeds offices per major city + Surveyor-General per province |

---

## Cross-cutting risks to flag

1. **FX-loan / income mismatch** (cross-reference `--finance` for FX-loan rules)
2. **Eurozone-accession transitions** (live: BG 2026; recent: HR 2023)
3. **AR cepo individual partial reinstatement** — verify whether buyer / seller routes are affected
4. **CHF safe-haven appreciation** — 2025 +12.7% vs USD; affects mortgage burden of CHF-denominated old loans
5. **Mandatory FX-form regimes — get them at purchase or lose repatriation rights**:
   - **EG** CBE Form 4 (نموذج 4) — without it, USD repatriation on resale is structurally blocked
   - **MA** Office des Changes registration via authorised bank — without it, no garantie de transfert
   - **TH** FET / Tor Tor 3 (ธ.ต.3) for inbound ≥ USD 50k — without it, DOL transfer cannot register
   - **TR** MASAK FX dekont for purchases > 75k TRY — required for KDV exemption + AML compliance
   - **VN** SBV bank documentation; profit/gain repatriation beyond original basis needs SBV licence
   - **ID** BI FX reporting for amounts ≥ USD 10k
   - **PH** BSP inward-remittance reporting ≥ USD 50k (no specific form like Thailand's FET)
6. **Dual-unit pricing markets** — confirm denomination in writing before signing:
   - **CL** UF (Unidad de Fomento) is the price-of-record unit — convert UF→CLP at transaction date
   - **UY** USD billete dominant for property; mortgages in UI (Unidad Indexada)
   - **DO** USD parallel pricing universal in tourist zones; non-tourist DOP
   - **AE / PA** USD-denominated by design (peg / dollarization)
   - **TR / EG / MA** USD or EUR quotes common in foreign-buyer segments — TRY/EGP/MAD often listed only for show
7. **JPY normalisation cycle** — BoJ NIRP exit Mar 2024 → 0.5% Jan 2025 → ~0.75% Dec 2025; the first hiking cycle since 2007 is reshaping the carry trade and yen-denominated debt economics
8. **EGP devaluation risk on USD-cash foreign buyer** — EGP depreciated ~70%+ vs USD 2021–24; buying with USD and selling in EGP exposes to potentially severe FX loss without Form 4 paper trail

## Confidence labels

- **HIGH**: peg / regime confirmed via central-bank or ECB source; reform with effective date verified
- **MEDIUM**: source <12 months old; secondary aggregator (e.g., FocusEconomics, Trading Economics)
- **LOW**: unverified specific or estimate

## Status

Last refreshed: 2026-05-01 (Tier-1 expansion: US, TR, AE, JP, TH, DO, CO, UY, CL, ZA + Tier-2: GE, ID, MY, VN, PH, IL, MA, EG). Next refresh: monthly (rates), per-event (regime change, peg adjustment, mandatory-FX-form rule changes).

**Confidence**: HIGH for peg / regime status (verified to central-bank sources — CBE, BAM, BoT, SBV, BI, BNM, BSP, NBG, SARB, BoJ, BoI, CBUAE, BCRD, BCCh, BCU, BCU UI, BanRep). MEDIUM for live point-in-time FX rates (verify daily before transaction); MEDIUM for capital-control fine-print (verify per-deal with authorised bank + lawyer).
