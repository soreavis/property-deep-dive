# Universal `--compare` Mode

Side-by-side multi-country comparison for relocation, investment, and "where should I move/buy?" decisions. Leverages all 62 country playbooks at once.

**Snapshot**: April 2026.

## When to use

Trigger `--compare` when the user is **not committing to a single address** but instead asking:
- "Where should I move from FR?" — compare candidate countries
- "Spain or Portugal for golden-visa replacement?" — compare 2-5 countries head-to-head
- "Cheapest entry market in EU for €200k?" — compare on a metric
- "Where can I retire on €2,500/mo?" — compare with `--retirement` overlay

## Invocation

```
/property-deep-dive --compare=es,pt,it [--criteria=<list>] [--journey=<type>] [--budget=<amount>]
/property-deep-dive --compare=eu --top=10 --criteria=tax,price,visa
/property-deep-dive --compare --rank=tax-friendly --rank=climate-stable
```

## Universal contract

For each country in the comparison set, return:
1. **One row per country** with the requested criteria
2. **Highlighted leaders/laggards** per criterion (best 🟢 / worst 🔴)
3. **Overall verdict per user-stated objective**
4. **Ranked shortlist** (top 3 by composite score)
5. **Anti-hallucination disclaimer**: comparison is structural, not predictive

## Output template

```markdown
## Multi-Country Comparison

**Comparison set**: <ISO2 list>
**Criteria**: <list>
**Date**: <YYYY-MM-DD>

### Headline metrics

| Metric | <C1> | <C2> | <C3> | … |
|---|---|---|---|---|
| Capital city €/m² (segment-typical) | … | … | … | … |
| Annual property tax (% / formula) | … | … | … | … |
| Transfer tax / acquisition cost | … | … | … | … |
| CGT regime | … | … | … | … |
| Foreign-buyer access | … | … | … | … |
| Mortgage LTV (non-resident) | … | … | … | … |
| Currency / FX volatility | … | … | … | … |
| Visa pathway (RBI/CBI status) | … | … | … | … |
| Climate trajectory (RCP4.5 to 2050) | … | … | … | … |
| Notary / closing-cost % | … | … | … | … |
| Time offer→deed (days) | … | … | … | … |

### Per-criterion leader

| Criterion | Best | Worst |
|---|---|---|
| Lowest acquisition cost | <C> | <C> |
| Lowest annual carry | <C> | <C> |
| Strongest CGT exemption | <C> | <C> |
| Most foreign-buyer-friendly | <C> | <C> |
| Most stable currency | <C> | <C> |
| Most accessible visa | <C> | <C> |
| Best climate (cooler / less drought / less wildfire) | <C> | <C> |
| Fastest closing | <C> | <C> |

### Composite ranking

🥇 1. <C> — <one-line rationale>
🥈 2. <C> — <one-line rationale>
🥉 3. <C> — <one-line rationale>

### Decision-context overlay

<if --journey=retiree, --journey=foreign-buyer, --journey=investor — apply that filter>

### Confidence
<HIGH | MEDIUM | LOW> — <one-sentence justification>
```

## Available criteria flags

| Flag | What it pulls |
|---|---|
| `--criteria=tax` | Annual + transfer + CGT + rental income tax + VAT |
| `--criteria=price` | Capital + secondary city €/m², HPI YoY |
| `--criteria=visa` | RBI/CBI status, property thresholds, language requirement |
| `--criteria=finance` | LTV non-resident, 10-yr fixed rate, FX-loan rules |
| `--criteria=climate` | Temperature trajectory, sea-level rise, drought, wildfire risk |
| `--criteria=foreign-buyer` | Restrictions, permits, surcharges, RU/BY rules |
| `--criteria=str` | Short-term rental regime, registration, taxes |
| `--criteria=closing` | Notary requirement, closing cost %, days offer→deed |
| `--criteria=insurance` | Cat-risk scheme, mortgage-mandatory, premium % |
| `--criteria=process` | Cadastre access, foreigner-self-serve, language requirement |
| `--criteria=all` | All of the above |

## Comparison set shortcuts

| Shortcut | Resolves to |
|---|---|
| `eu` | All 27 EU members in skill |
| `eea` | EU + IS, NO, LI (when populated) |
| `eurozone` | All 21 eurozone members |
| `western-balkans` | RS, ME, BA, MK, AL |
| `latam` | MX, BR, AR, CR, PA |
| `anglo-non-eu` | CA, AU, NZ |
| `mediterranean` | ES, PT, IT, GR, CY, MT, FR, HR, SI |
| `nordic` | SE, FI, NO, DK, IS |
| `dach` | DE, AT, CH |
| `top-10-foreign-buyer-friendly` | precomputed list (see below) |

## Precomputed verdict shortcuts (Apr 2026 snapshot)

These are computed from the per-country playbooks and refreshed on `--update`. They are commentary, not authoritative — use as a starting point.

### Most foreign-buyer-friendly (no AIP/permit beyond standard)
1. PT (open, NIF only)
2. ES (open, NIE only)
3. LU (no nationality restriction, same 7%)
4. IT (Codice Fiscale only)
5. FR (no permit, simple notarial)

### Highest acquisition friction (permit / restriction-heavy)
1. CA (foreign-buyer ban through 1 Jan 2027)
2. AU (established-homes ban 1 Apr 2025–31 Mar 2027)
3. NZ (most existing homes banned since 2018)
4. CH (Lex Koller cantonal permit)
5. DK (non-EU + 5y residence requirement)

### Lowest acquisition cost (% of price)
1. EE (~1-2% no transfer tax)
2. LT (~1-1.5% no transfer tax)
3. CZ (~2-4% transfer tax abolished 2020)
4. SK (~2-4% no transfer tax since 2005)
5. NO (~3-4% dokumentavgift 2.5%)

### Highest acquisition cost (% of price)
1. BE (~12-17% Brussels/Wallonia)
2. ES (~10-13% existing)
3. AT (~10-12%)
4. GR (~10-12%)
5. UK (~10-15% with SDLT non-res surcharge)

### Lowest annual carry (no/minimal annual property tax)
1. MT (no annual property tax)
2. CY (national IPT abolished 2017; municipal small)
3. LU (impôt foncier near-trivial currently — reform 2030)
4. IE (LPT modest, 0.0906% base rate)
5. LT (NTM exemption ≤€150k for residents)

### Highest annual carry
1. FR (taxe foncière + redevance audiovisuelle, dependent on commune)
2. UK (council tax bands)
3. US (state-by-state; varies 0.5-2.5%)
4. CH (cantonal Eigenmietwert until 2028 + cantonal property tax)
5. DK (boligskat 2024-reform unified ejendomsværdiskat + grundskyld)

### Most stable currency / lowest FX risk for €-buyers
1. **Eurozone** (21 countries — no FX risk)
2. BG (just joined 1 Jan 2026)
3. HR (joined 2023)
4. DK (DKK ERM-II ±2.25%)
5. BA (currency board 1.95583)

### Highest FX risk for €-buyers
1. AR (managed band 1,000–1,400 ARS/USD; capital controls history)
2. HU (HUF most volatile EU currency)
3. IS (small market, 10%+ annual range typical)
4. UK (GBP political-uncertainty premium)
5. CH (CHF safe-haven appreciation 2024-26 — actually a *gain* for buyers but unhedged exit risk)

### Most golden-visa-friendly (Apr 2026, post-ES/IE/MT closures)
1. GR (€800k/€400k tiers, property-linked)
2. CY (€300k PR — distinct from ended CBI)
3. MT MPRP (€375k lease/€750k purchase + fees)
4. PA (Friendly Nations $200k / Qualified Investor $300k)
5. LV (€250k Riga radius, built only)

### Cleanest 2026 tax reforms (helpful for buyers)
1. CY (Comprehensive Tax Reform 1 Jan 2026 — CGT exemptions raised, SDC abolished)
2. LU (Bëllegen Akt €40k credit per person made permanent)
3. MT (UCA / vacant 0% on first €750k Jan 2025–Dec 2026)
4. PT (IFICI replaced NHR — narrower but operational)
5. LT (NTM 2026 progressive on non-main with main-dwelling threshold ≥€450k)

### Steepest 2026 tax reforms (less helpful for buyers)
1. RO (VAT 19→21% Aug 2025; local property tax baseline +167% Jan 2026)
2. NL (Box 3 forfait 6% 2026)
3. UK (SDLT thresholds reverted 1 Apr 2025)
4. SI (davek na nepremičnine 1.45% pending 2026)
5. CH (Eigenmietwert abolition 2028 — net depending on profile)

## Cross-cutting red-flag flags

When comparing, surface country-level structural flags:
- 🚩 BA: dual-entity (FBiH/RS-entity) — buyer must understand
- 🚩 CY: TRNC north title risk
- 🚩 LV: compulsory land lease (`dalītais īpašums`) Riga gotcha
- 🚩 MX: fideicomiso restricted zone (50km coast/100km border)
- 🚩 RO: AMCCRS pre-1977 Bucharest Rs I class — insurance/mortgage refusal
- 🚩 PA: 10km border restriction (constitutional)
- 🚩 GR: Golden Visa thresholds vary by zone; "where" matters more than "how much"
- 🚩 BG: non-EU cannot own ANY land directly
- 🚩 RO: non-EU cannot own land (buildings only)
- 🚩 IT: non-resident purchase tax 9% vs resident 2% (cadastral)

## Anti-hallucination

- **Only compare countries already in the skill** (`countries/<iso2>/playbook.md` exists). Refuse to compare unsupported countries.
- **Use the playbook values as authoritative** — do not retrieve fresh data per-country during a `--compare` run; trust the latest playbook refresh
- **Date-stamp every cell** — comparison output must show "as of <playbook last-update>" per row
- **Surface playbook confidence** — if any country has LOW confidence, flag it in the row

## Limitations

- **Not predictive**: comparison is current-state, not 5-year-forward
- **Not personalized**: doesn't know user's age, citizenship, financial profile — those go via `--journey=<type>` overlay
- **Doesn't replace local advice**: every shortlist needs a local notary/lawyer/tax adviser before committing

## Status

Last refreshed: 2026-04-26.
