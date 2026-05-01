# Universal `--macro` Section

Macroeconomic context for property decisions: inflation, GDP growth, central-bank policy rate, sovereign yield. Sets the cyclical backdrop for `--price`, `--finance`, and `--currency`.

**Snapshot**: April 2026.

## Universal contract

For the property's country, return:
1. **CPI inflation** (latest YoY)
2. **GDP growth** (latest YoY real)
3. **Central-bank policy rate** (current)
4. **10-yr sovereign yield**
5. **Eurostat HICP / IMF WEO cross-reference**
6. **Cyclical phase**: expansion / late-cycle / contraction / recovery
7. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Macro Profile

**Country**: <ISO2>
**CPI inflation (latest YoY)**: <%>
**GDP growth (latest YoY real)**: <%>
**Central-bank policy rate**: <%>
**10-yr sovereign yield**: <%>
**Cyclical phase**: <expansion | late-cycle | contraction | recovery>
**Sources**: <central bank + statistics office URLs>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Authoritative source registry

For each country, primary macro sources:

| Country | Central bank | Statistics office | Eurostat / OECD / IMF |
|---|---|---|---|
| FR | BdF (https://www.banque-france.fr/) | INSEE | Eurostat HICP |
| IT | BdI (https://www.bancaditalia.it/) | ISTAT | Eurostat HICP |
| ES | BdE (https://www.bde.es/) | INE | Eurostat HICP |
| PT | BdP (https://www.bportugal.pt/) | INE | Eurostat HICP |
| DE | Bundesbank (https://www.bundesbank.de/) | Destatis | Eurostat HICP |
| AT | OeNB (https://www.oenb.at/) | Statistik Austria | Eurostat HICP |
| CH | SNB (https://www.snb.ch/) | BFS | OECD |
| NL | DNB (https://www.dnb.nl/) | CBS | Eurostat HICP |
| BE | NBB (https://www.nbb.be/) | STATBEL | Eurostat HICP |
| LU | BCL (https://www.bcl.lu/) | STATEC | Eurostat HICP |
| IE | CBI (https://www.centralbank.ie/) | CSO | Eurostat HICP |
| UK | BoE (https://www.bankofengland.co.uk/) | ONS | OECD |
| GR | BdGr (https://www.bankofgreece.gr/) | ELSTAT | Eurostat HICP |
| MT | CBM (https://www.centralbankmalta.org/) | NSO | Eurostat HICP |
| CY | CBC (https://www.centralbank.cy/) | CyStat | Eurostat HICP |
| FI | SP (https://www.suomenpankki.fi/) | Tilastokeskus | Eurostat HICP |
| SE | Riksbank (https://www.riksbank.se/) | SCB | Eurostat HICP |
| NO | NB (https://www.norges-bank.no/) | SSB | OECD |
| DK | DN (https://www.nationalbanken.dk/) | DST | Eurostat HICP |
| IS | CBI (https://www.cb.is/) | Hagstofa | OECD |
| SI | BS (https://www.bsi.si/) | SURS | Eurostat HICP |
| PL | NBP (https://nbp.pl/) | GUS | Eurostat HICP |
| EE | EP (https://www.eestipank.ee/) | StatEE | Eurostat HICP |
| LV | LB (https://www.bank.lv/) | CSP | Eurostat HICP |
| LT | LB (https://www.lb.lt/) | OSP | Eurostat HICP |
| HR | HNB (https://www.hnb.hr/) | DZS | Eurostat HICP |
| HU | MNB (https://www.mnb.hu/) | KSH | Eurostat HICP |
| CZ | ČNB (https://www.cnb.cz/) | ČSÚ | Eurostat HICP |
| SK | NBS (https://www.nbs.sk/) | ŠÚ SR | Eurostat HICP |
| RO | BNR (https://www.bnr.ro/) | INS | Eurostat HICP |
| BG | BNB (https://www.bnb.bg/) | NSI | Eurostat HICP |
| RS | NBS (https://www.nbs.rs/) | RZS | IMF WEO |
| ME | CBCG (https://www.cbcg.me/) | MONSTAT | IMF WEO |
| BA | CBBH (https://www.cbbh.ba/) | BHAS | IMF WEO |
| MK | NBRSM (https://www.nbrm.mk/) | MAKSTAT | IMF WEO |
| AL | BoA (https://www.bankofalbania.org/) | INSTAT | IMF WEO |
| CA | BoC (https://www.bankofcanada.ca/) | StatCan | OECD |
| AU | RBA (https://www.rba.gov.au/) | ABS | OECD |
| NZ | RBNZ (https://www.rbnz.govt.nz/) | StatsNZ | OECD |
| MX | Banxico (https://www.banxico.org.mx/) | INEGI | OECD |
| BR | BCB (https://www.bcb.gov.br/) | IBGE | IMF WEO |
| AR | BCRA (https://www.bcra.gob.ar/) | INDEC | IMF WEO |
| CR | BCCR (https://www.bccr.fi.cr/) | INEC | IMF WEO |
| PA | INEC (https://www.inec.gob.pa/) | INEC | IMF WEO |
| US | Federal Reserve (https://www.federalreserve.gov/) | BLS / BEA | OECD |
| TR | TCMB (https://www.tcmb.gov.tr/) | TÜİK | IMF WEO |
| AE | CBUAE (https://www.centralbank.ae/) | FCSC | IMF WEO |
| JP | BoJ (https://www.boj.or.jp/) | e-Stat / MIC | OECD |
| TH | BoT (https://www.bot.or.th/) | NSO / NESDC | IMF WEO |
| DO | BCRD (https://www.bancentral.gov.do/) | ONE | IMF WEO |
| CO | BanRep (https://www.banrep.gov.co/) | DANE | IMF WEO |
| UY | BCU (https://www.bcu.gub.uy/) | INE | IMF WEO |
| CL | BCCh (https://www.bcentral.cl/) | INE | OECD |
| ZA | SARB (https://www.resbank.co.za/) | StatsSA | IMF WEO |
| GE | NBG (https://www.nbg.gov.ge/) | GeoStat | IMF WEO |
| ID | BI (https://www.bi.go.id/) | BPS | IMF WEO |
| MY | BNM (https://www.bnm.gov.my/) | DOSM | IMF WEO |
| VN | SBV (https://www.sbv.gov.vn/) | GSO | IMF WEO |
| PH | BSP (https://www.bsp.gov.ph/) | PSA | IMF WEO |
| IL | BoI (https://www.boi.org.il/) | CBS | OECD |
| MA | BAM (https://www.bkam.ma/) | HCP | IMF WEO |
| EG | CBE (https://www.cbe.org.eg/) | CAPMAS | IMF WEO |

## Apr 2026 snapshot — central-bank policy rates

| Country / region | Rate | Direction |
|---|---|---|
| **ECB Deposit Rate** | 2.50% | hold (post-2024 cuts paused on Iran energy shock) |
| **BoE Bank Rate** | 3.75% | hold (since Dec 2025) |
| **SNB Policy Rate** | 0.00% | held; CHF safe-haven appreciation 2024-26 |
| **Riksbank** | 1.75% | paused after Sep 2025 cut |
| **Norges Bank** | 4.00% | hold |
| **DNB** (DK) | 3.10% (effective via FX peg) | hold |
| **CBI Iceland** | 7.50% | gradually cutting |
| **CNB Czech** | 3.25% | held |
| **NBP Poland** | 4.50% | held; FX-loan legacy concerns |
| **MNB Hungary** | 6.50% | hold (HUF volatility-management) |
| **NBS Slovakia** | ECB-bound | ECB Deposit |
| **BNR Romania** | 6.50% | hold (RON managed float) |
| **BNB Bulgaria** | ECB-bound (since 1 Jan 2026) | ECB Deposit |
| **HNB Croatia** | ECB-bound (since 1 Jan 2023) | ECB Deposit |
| **NBS Serbia** | 5.50% | hold |
| **CBCG Montenegro** | n/a (EUR unilateral) | ECB Deposit indirect |
| **CBBH Bosnia** | n/a (currency board) | ECB Deposit indirect |
| **NBRSM N. Macedonia** | 5.50% | hold |
| **BoA Albania** | 2.75% | hold |
| **BoC Canada** | 2.75% | held; review 2026 considering AU-style FIRB post-2027 |
| **RBA Australia** | 4.10% | gradually cutting |
| **RBNZ NZ** | 3.50% | gradually cutting |
| **Banxico** | 7.00% | post-300bps-cut-in-2025; pausing |
| **BCB Brazil** | **14.75%** | cuts paused on Iran energy shock Mar 2026 |
| **BCRA Argentina** | n/a (volatile post-Milei) | currency-band managed; effective lending rates 25-38% UVA |
| **BCCR Costa Rica** | 3.50% | held |
| **PA (USD-dollarized)** | follows Fed Funds 4.25-4.50% | Fed-bound |
| **Fed Funds (US)** | 4.25-4.50% | hold (Fed paused after 2024 cuts; Q1 2026 print pending — verify FOMC) |
| **TCMB (Turkey)** | ~42.50% est. | easing from 50% peak (mid-2024) — verify against latest TCMB MPC |
| **CBUAE (UAE)** | ~4.40% (EIBOR-aligned) | Fed-bound via AED/USD peg 3.6725 |
| **BoJ (Japan)** | 0.75% est. | hiked from 0.50% (Jan 2025) → ~0.75% (Dec 2025); first hike cycle since 2007 — verify next BoJ MPM |
| **BoT (Thailand)** | 2.50% | hold; cut path debated as THB strengthens |
| **BCRD (DR)** | 6.00% est. | gradual easing; verify latest BCRD comunicado |
| **BanRep (Colombia)** | ~9.00% est. | mid-cycle cuts from 13.25% peak (Dec 2023) — verify |
| **BCU (Uruguay)** | 8.50% est. | hold; TPM in restrictive territory — verify |
| **BCCh (Chile)** | ~4.50% est. | cut cycle from 11.25% (Oct 2023) — verify against next IPoM |
| **SARB (South Africa)** | 7.50% est. | gradual cuts since 2024 — verify next MPC |
| **NBG (Georgia)** | 8.00% est. | hold; CPI near target — verify |
| **BI (Indonesia)** | 6.00% est. | BI-Rate; FX-defence stance — verify |
| **BNM (Malaysia)** | 3.00% (OPR) | held; CPI low — verify next MPC |
| **SBV (Vietnam)** | 4.50% (refi) est. | accommodative; managed VND — verify |
| **BSP (Philippines)** | 5.75% est. | cut path from 6.50% peak — verify |
| **BoI (Israel)** | 4.50% est. | war-affected; cautious cuts — verify |
| **BAM (Morocco)** | 2.50% est. | hold; CPI near target — verify |
| **CBE (Egypt)** | ~22-24% est. | held high post-Mar 2024 IMF devaluation; CPI declining from 30%+ — verify |

## Apr 2026 snapshot — sovereign 10-yr yields

Approximate (verify on FRED / Refinitiv / each central bank's website):

| Country | 10-yr yield | Spread vs Bund |
|---|---|---|
| DE | 2.40% | benchmark |
| FR | 2.85% | +45 bps |
| IT | 3.30% | +90 bps |
| ES | 3.05% | +65 bps |
| PT | 2.80% | +40 bps |
| GR | 3.15% | +75 bps |
| AT | 2.55% | +15 bps |
| NL | 2.50% | +10 bps |
| BE | 2.70% | +30 bps |
| IE | 2.65% | +25 bps |
| FI | 2.60% | +20 bps |
| CY | 3.10% | +70 bps |
| MT | 2.90% | +50 bps |
| LU | 2.45% | +5 bps |
| SK | 3.20% | +80 bps |
| SI | 2.90% | +50 bps |
| EE | 3.40% | +100 bps |
| LV | 3.50% | +110 bps |
| LT | 3.30% | +90 bps |
| HR | 3.00% | +60 bps |
| HU | 6.20% | (HUF) — non-eurozone |
| PL | 5.40% | (PLN) |
| RO | 7.50% | (RON) |
| CZ | 4.10% | (CZK) |
| SE | 2.55% | (SEK) |
| NO | 4.20% | (NOK) |
| DK | 2.70% | (DKK ERM-II) |
| IS | 7.00% | (ISK) |
| CH | 0.50% | safe-haven |
| UK | 4.20% | (GBP) |
| BG | 3.00% | (eurozone since 2026) |
| RS | 5.00% | (RSD) |
| ME | 4.50% | (EUR-effective) |
| BA | 3.50% | (BAM-currency-board) |
| MK | 5.00% | (MKD) |
| AL | 5.50% | (ALL) |
| CA | 3.50% | (CAD) |
| AU | 4.30% | (AUD) |
| NZ | 4.10% | (NZD) |
| US | 4.30% | (USD) |
| MX | 9.50% | (MXN) |
| BR | 14.20% | (BRL) — Selic-driven |
| AR | 30%+ | (ARS) — UVA-indexed |
| CR | 7.50% | (CRC) |
| PA | 4.30% | (USD-dollarized) |
| US | 4.30% est. | (USD) — benchmark for emerging-market USD-equivalent yields |
| TR | ~28-32% est. (TRY) / USD eurobond ~7.5% | TRY yield reflects hyperinflation; USD eurobond is the cleaner foreign-buyer reference — verify Hazine + ICE BofA |
| AE | ~4.40% (USD-linked) | AED pegged; sovereign USD eurobonds track UST + ~50-100 bps |
| JP | 1.50% est. | (JPY) — BoJ YCC fully unwound; verify MoF/JGB market |
| TH | 2.50% est. | (THB) |
| DO | 11.0% est. | (DOP); USD eurobonds ~7-8% — verify |
| CO | 11.5% est. | (COP); USD eurobonds ~7-8% |
| UY | 8.50% est. | (UYU); USD eurobonds ~6-7% (IG-rated) |
| CL | 5.80% est. | (CLP); USD eurobonds ~5-6% |
| ZA | 10.50% est. | (ZAR); R2032 generic — verify JSE |
| GE | 8.50% est. | (GEL); USD eurobonds ~7% |
| ID | 7.00% est. | (IDR); USD eurobonds ~5-5.5% |
| MY | 3.90% est. | (MYR); IG-rated |
| VN | 3.00% est. | (VND); USD eurobonds ~5-6% |
| PH | 6.30% est. | (PHP); USD eurobonds ~5-5.5% |
| IL | 4.80% est. | (ILS); war-risk premium ~50 bps over pre-Oct-2023 — verify |
| MA | 4.50% est. | (MAD); IG-rated; USD eurobonds ~5% |
| EG | ~25% est. | (EGP); USD eurobonds ~9-11% — distressed; verify post-IMF |

## Why macro context matters for property

1. **Mortgage rate environment** (cross-reference `--finance`)
   - 10-yr fixed mortgages closely track 10-yr sovereign yields + bank spread (~150-200 bps)
   - Higher policy rate → tighter mortgage origination

2. **Currency stability** (cross-reference `--currency`)
   - High inflation + weak FX = property price volatility in foreign-buyer terms
   - AR / TR / EG (not in skill) are extreme cases — properties priced in USD/EUR

3. **Cyclical timing**
   - Expansion + low rates + GDP growth → upward pressure on prices
   - Late-cycle + rising rates → cooling
   - Recession + rate cuts → price stabilization, possibly bounce

4. **Sovereign risk** for foreign buyers
   - Spreads >300 bps over Bund signal sovereign-risk premium
   - HU / PL / RO / TR / EG are cases — affect mortgage availability and currency

## Cyclical phase classification (Apr 2026)

### Late-cycle / soft landing
- Eurozone (ECB held 2.50% post-cuts)
- UK (BoE 3.75%)
- US (Fed 4.25-4.50%)
- CA (BoC 2.75%)
- IL (BoI cautious; war-recovery)

### Recovery / cutting
- AU (RBA cutting 4.10%)
- NZ (RBNZ cutting 3.50%)
- IS (CBI cutting 7.50%)
- MX (Banxico paused after 300 bps cuts)
- CL (BCCh ~4.5% from 11.25% peak)
- CO (BanRep ~9% from 13.25% peak)
- PH (BSP ~5.75% mid-cut path)
- ZA (SARB gradual cuts ~7.5%)

### Active tightening / hold high
- HU (MNB 6.50% — HUF volatility)
- BR (BCB 14.75% — Selic on hold post-cuts)
- TR (TCMB ~42.5% — easing from 50% mid-2024 peak; CPI still ~50%+)
- AR (volatile peso band)
- EG (CBE ~22-24% post-IMF Mar 2024 devaluation; CPI declining from 30%+)
- UY (BCU 8.5% — restrictive)

### Normalization (post-deflation / post-NIRP)
- JP (BoJ exited NIRP Mar 2024 → 0.5% Jan 2025 → ~0.75% Dec 2025; first sustained hike cycle in ~17 years)

### Expansion / loose
- VN (SBV accommodative; ~6% GDP)
- ID (BI 6% holding; ~5% GDP)
- MY (BNM OPR 3% steady; ~5% GDP)
- TH (BoT 2.5% steady; ~3% GDP)
- GE (NBG cutting; EU candidate)
- MA (BAM 2.5% stable)
- DO (BCRD easing)

### Stable / pegged
- BG (joined eurozone Jan 2026)
- HR (eurozone since 2023)
- ME (unilateral euroisation)
- BA (currency board)
- DK (ERM-II)
- AE (AED pegged to USD 3.6725 — Fed-bound monetary policy)
- PA (USD-dollarized — Fed-bound)

## Inflation trajectory (Apr 2026, recent quarter)

EU rough YoY: 2.2-2.8% (post-2022 peak)
UK: 2.5-3.0%
US: ~2.5% est. (Q1 2026 print pending — verify BLS CPI release)
HU: 4-5% (HUF volatility)
PL: 3-4%
RO: 4-5% (post-VAT-hike)
TR: ~50%+ (TÜFE — still hyperinflation regime, easing trajectory; verify TÜİK)
AR: 30%+ (post-Milei normalization)
BR: 4-5% (Selic on hold)
JP: ~2-3% (BoJ target met; first sustained 2%+ run since 1990s)
TH: ~1-2% (sub-target)
AE: ~2-3% (low; pegged regime)
DO: ~3-5%
CO: ~5%
UY: ~5-6%
CL: ~3-4% (within BCCh 3% target band)
ZA: ~4-5% (within SARB 3-6% band)
GE: ~2-3%
ID: ~3% (within BI 2.5±1% target)
MY: ~2-3%
VN: ~3-4% (within SBV 4.5% ceiling)
PH: ~3-4% (within BSP 2-4% target)
IL: ~3% (war-affected supply shocks)
MA: ~2%
EG: ~30%+ declining (post-Mar 2024 EGP devaluation; verify CAPMAS)

## Tier-1 + Tier-2 country macro snapshots (Apr 2026)

The 18 countries below were added to the skill in 2026-Q1/Q2 (Tier-1 PR #57; Tier-2 PR #60). Snapshots are 2025 H2 / Q1 2026 where published; figures stamped `est.` require verification against the next official print.

### Tier-1 (PR #57)

**US** — CPI ~2.5% YoY (Q1 2026 est., verify BLS https://www.bls.gov/cpi/); GDP ~2.5% (2025 BEA advance est., verify https://www.bea.gov); Fed Funds 4.25-4.50% (hold since Q4 2024); 10y UST ~4.30%; cyclical phase: late-cycle / soft-landing.

**TR** — TÜFE ~50%+ YoY (still hyperinflation regime, easing from 2023 peak ~85%; verify TÜİK https://www.tuik.gov.tr); GDP ~3-4% (2025 est., verify); TCMB policy rate ~42.50% (cut from 50% mid-2024 peak — verify against latest MPC https://www.tcmb.gov.tr); 10y TRY yield ~28-32%; USD eurobond ~7.5% — that's the cleaner foreign-buyer reference. Macro flag: **post-hyperinflation normalization, FX risk extreme** — TRY lost ~80% vs USD 2021-2024.

**AE** — CPI ~2-3% (low, pegged regime); GDP ~3-4% (2025); CBUAE EIBOR ~4.40% — Fed-bound via AED/USD peg 3.6725 (no independent monetary policy); USD-equivalent 10y ~4.40%. Macro flag: **stable / pegged**, USD-correlated.

**JP** — CPI ~2-3% (BoJ 2% target met first sustained period since 1990s); GDP ~1% (slow); BoJ policy rate 0.75% est. (NIRP exit Mar 2024 → 0.50% Jan 2025 → ~0.75% Dec 2025; verify next BoJ MPM https://www.boj.or.jp); 10y JGB ~1.50%. Macro flag: **post-NIRP normalization** — first sustained tightening cycle since 2007.

**TH** — CPI ~1-2% (sub-target); GDP ~3% (2025); BoT 2.50% (hold; cut path debated); 10y THB ~2.50%. Macro flag: **stable / soft expansion**, THB strengthening.

**DO** — CPI ~3-5%; GDP ~5% (2025 est.); BCRD ~6.00% est. (gradual easing); 10y DOP ~11%, USD eurobonds ~7-8%. Macro flag: **stable expansion**, BB-rated.

**CO** — CPI ~5%; GDP ~2-3%; BanRep ~9.00% est. (mid-cycle cuts from 13.25% peak Dec 2023); 10y COP ~11.5%, USD eurobonds ~7-8%. Macro flag: **cutting cycle**, BBB-/BB+ split rating.

**UY** — CPI ~5-6%; GDP ~3%; BCU TPM 8.50% est. (restrictive — top of LatAm IG); 10y UYU ~8.5%, USD eurobonds ~6-7%. Macro flag: **stable IG-rated**, restrictive.

**CL** — CPI ~3-4% (within target); GDP ~2-3%; BCCh ~4.50% est. (cut from 11.25% Oct 2023 peak — verify next IPoM https://www.bcentral.cl); 10y CLP ~5.80%; A-rated. Macro flag: **cutting cycle**, IG.

**ZA** — CPI ~4-5% (within SARB 3-6% band); GDP ~1% (Eskom drag easing post-2024); SARB 7.50% est. (gradual cuts from 8.25% peak); 10y ZAR ~10.50%. Macro flag: **slow recovery**, BB-rated, FX volatility.

### Tier-2 (PR #60)

**GE** — CPI ~2-3%; GDP ~5-6%; NBG ~8.00% est.; 10y GEL ~8.5%, USD eurobonds ~7%. Macro flag: **EU candidate, stable** — but watch geopolitical premium (Russia exposure, 2024 foreign-agent law tensions).

**ID** — CPI ~3% (within BI 2.5±1% target); GDP ~5%; BI-Rate 6.00% est. (FX-defence stance protecting IDR); 10y IDR ~7%, USD eurobonds ~5-5.5%. Macro flag: **stable expansion**, BBB-rated.

**MY** — CPI ~2-3%; GDP ~5%; BNM OPR 3.00% (held since 2023); 10y MYR ~3.90%; A-/BBB+. Macro flag: **stable expansion**, IG.

**VN** — CPI ~3-4% (within SBV 4.5% ceiling); GDP ~6% (top regional); SBV refinance rate 4.50% est. (accommodative); 10y VND ~3%, USD eurobonds ~5-6%. Macro flag: **expansion**, BB+ — managed VND.

**PH** — CPI ~3-4% (within BSP 2-4% target); GDP ~6%; BSP ~5.75% est. (cut path from 6.50% peak); 10y PHP ~6.30%, USD eurobonds ~5-5.5%. Macro flag: **expansion / cutting cycle**, BBB-rated.

**IL** — CPI ~3% (war-affected supply shocks); GDP recovery (2024 contracted, 2025 rebound est.); BoI ~4.50% est.; 10y ILS ~4.80% (war-risk premium ~50 bps over pre-Oct-2023 — verify). Macro flag: **war-recovery, sovereign risk premium elevated**.

**MA** — CPI ~2%; GDP ~3-4%; BAM 2.50% est. (hold); 10y MAD ~4.50%; BB+/IG-borderline. Macro flag: **stable expansion**.

**EG** — CPI ~30%+ declining from 2024 peak ~38%; GDP ~3-4% (devaluation drag); CBE ~22-24% est. (held high post-Mar 2024 IMF-conditioned EGP devaluation; verify https://www.cbe.org.eg); 10y EGP ~25%, USD eurobonds ~9-11% (distressed-trading); B-rated. Macro flag: **post-devaluation stabilization, FX crisis residual** — EGP devalued ~60% Mar 2024 under IMF/UAE/EU rescue package.

### What to verify before use

For any of the 18 above, the standard pre-output flow is:

1. Pull latest CPI print from the country's statistics office (named in the source registry above).
2. Check the central bank's most-recent MPC statement for current policy rate (the rate cycle moves faster than this snapshot).
3. For EM countries (TR, EG, AR-equiv): always cite the **USD eurobond** yield as the foreign-buyer reference, NOT the local-currency 10y — the local yield is an inflation/FX number, not a rate-of-return for a USD/EUR-paying buyer.
4. Stamp the section `**Last verified**: <YYYY-MM-DD>` and confidence band.

## Quality bar for `--macro`

- **Cite source within last 90 days** for HIGH confidence
- **Use Eurostat HICP / OECD / IMF WEO** as cross-reference for HIGH confidence
- **Flag if data >12 months old** as MEDIUM
- **For Western Balkans + LatAm**: IMF WEO is often the cleanest comparable source

## Status

Last refreshed: 2026-04-26. Next refresh: monthly (rates/inflation), quarterly (GDP).
