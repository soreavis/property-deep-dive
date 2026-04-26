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

### Recovery / cutting
- AU (RBA cutting 4.10%)
- NZ (RBNZ cutting 3.50%)
- IS (CBI cutting 7.50%)
- MX (Banxico paused after 300 bps cuts)

### Active tightening / hold high
- HU (MNB 6.50% — HUF volatility)
- BR (BCB 14.75% — Selic on hold post-cuts)
- TR (not in skill — extreme)
- AR (volatile peso band)

### Stable / pegged
- BG (joined eurozone Jan 2026)
- HR (eurozone since 2023)
- ME (unilateral euroisation)
- BA (currency board)
- DK (ERM-II)

## Inflation trajectory (Apr 2026, recent quarter)

EU rough YoY: 2.2-2.8% (post-2022 peak)
UK: 2.5-3.0%
US: 2.5-3.0%
HU: 4-5% (HUF volatility)
PL: 3-4%
RO: 4-5% (post-VAT-hike)
TR (not in skill): 30%+
AR: 30%+ (post-Milei normalization)
BR: 4-5% (Selic on hold)

## Quality bar for `--macro`

- **Cite source within last 90 days** for HIGH confidence
- **Use Eurostat HICP / OECD / IMF WEO** as cross-reference for HIGH confidence
- **Flag if data >12 months old** as MEDIUM
- **For Western Balkans + LatAm**: IMF WEO is often the cleanest comparable source

## Status

Last refreshed: 2026-04-26. Next refresh: monthly (rates/inflation), quarterly (GDP).
