# Universal `--currency` Section

Currency code, peg status, FX volatility, capital controls, hedging market depth, 2025-26 currency reforms across all 44 supported countries.

**Snapshot**: April 2026.

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

### Latin America (MX, BR, AR, CR, PA)
MX free float (Banxico), deep market. BR free float with **IOF tax** on incoming foreign transfers. **AR's CEPO cambiario was largely dismantled 14 April 2025** — ARS now floats inside a **1,000–1,400 ARS/USD band with 1%/mo edge adjustments**, "dólar blend" abolished; "cepo individual" partial reinstatement appeared late 2025. CR managed float / managed-band, BCCR holds CRC near ₡500/USD via interventions. PA fully USD-dollarized since 1904 (balboa = coins only, 1:1 fixed by Article 262 constitution).

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

---

## Cross-cutting risks to flag

1. **FX-loan / income mismatch** (cross-reference `--finance` for FX-loan rules)
2. **Eurozone-accession transitions** (live: BG 2026; recent: HR 2023)
3. **AR cepo individual partial reinstatement** — verify whether buyer / seller routes are affected
4. **CHF safe-haven appreciation** — 2025 +12.7% vs USD; affects mortgage burden of CHF-denominated old loans

## Confidence labels

- **HIGH**: peg / regime confirmed via central-bank or ECB source; reform with effective date verified
- **MEDIUM**: source <12 months old; secondary aggregator (e.g., FocusEconomics, Trading Economics)
- **LOW**: unverified specific or estimate

## Status

Last refreshed: 2026-04-26. Next refresh: monthly (rates), per-event (regime change, peg adjustment).
