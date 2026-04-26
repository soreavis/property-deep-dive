# TCO Calculator — 30-Year Total Cost of Ownership

Bridges `--tax`, `--finance`, `--insurance`, `--notary`, and `--mains` into one usable number. Computes the 30-year total carrying cost of owning a property, in the local currency.

## Universal contract

For a given property + buyer profile, return:
1. **Initial outlay** (purchase price + closing costs + setup costs)
2. **Year-by-year operating cost** (mortgage P&I + property tax + insurance + maintenance + utilities + management fees)
3. **30-year cumulative outlay** (nominal)
4. **30-year cumulative outlay** (real, inflation-adjusted to today's currency)
5. **Imputed sale value at exit** (asking - capex - CGT - notary - agent commission)
6. **Net cost of ownership** = (Year 30 outlay) - (sale proceeds)

## Inputs

```yaml
country: <ISO2>
purchase_price: <amount in local currency>
ownership_type: primary_residence | rental_investment | second_home
buyer_residency: resident | non_resident_eu | non_resident_non_eu
deposit_pct: <0.20 typical for resident, 0.30+ for non-resident>
mortgage_term_years: 25  # standard
mortgage_rate_fixed_pct: <from --finance>  # e.g., 3.5
mortgage_type: fixed | variable | tracker
local_inflation_rate_pct: <from --macro>  # e.g., 2.5
expected_property_appreciation_pct_yoy: <from --price trajectory>  # e.g., 2.0
hold_period_years: 30  # default for "buy & hold" analysis
```

## Cost components

### A. Initial outlay (year 0)

```
purchase_price
+ transfer_tax (% from per-country playbook)
+ notary_fee (% from per-country playbook)
+ registration_fee (% from per-country playbook)
+ property_inspection / diagnostics (€500-2,000)
+ mortgage_setup_costs (1-3% of loan)
+ furniture / immediate_capex (estimate: 2-5% of price)
= TOTAL_INITIAL
```

### B. Annual operating costs (years 1-30)

```
mortgage_P&I (computed from rate, term, principal)
+ property_tax (annual, from per-country playbook §tax)
+ home_insurance (annual, from --insurance, ~0.15-0.30% insured value)
+ maintenance_capex (1-2% of property value/year, real)
+ utility_costs (heating, electric, water — varies wildly by country)
+ HOA_fees / condominium_dues (where applicable, ~1-3% of price/year for apartments)
+ rental_management_fees (if rental investment, 8-15% of gross rent)
+ rental_income_tax (if rental, see per-country --tax)
- rental_income (if rental, see per-country --rental)
= ANNUAL_NET_CASH_FLOW
```

### C. Sale costs at year N

```
gross_sale_value (= purchase_price * (1 + appreciation_yoy)^N)
- capital_gains_tax (per-country playbook §tax — primary residence often exempt; rental almost never)
- agent_commission (from --exit, typically 3-7% in EU, 5-6% in US/CA)
- notary_seller_fees (from --notary)
- pre-sale capex (refresh costs ~1-2% of sale value)
= NET_SALE_PROCEEDS
```

### D. Net cost of ownership (Year 30)

```
TOTAL_INITIAL + Σ(ANNUAL_NET_CASH_FLOW for 30 years) - NET_SALE_PROCEEDS = NET_TCO
```

Adjust to real terms using local inflation.

## Worked example: rural Adriers, FR — €145,000 listing

```yaml
country: fr
purchase_price: 145000
ownership_type: primary_residence
buyer_residency: resident
deposit_pct: 0.20
mortgage_term_years: 25
mortgage_rate_fixed_pct: 3.5  # from --finance
local_inflation_rate_pct: 2.0  # from --macro
expected_property_appreciation_pct_yoy: 1.5  # rural FR conservative
hold_period_years: 30
```

**Year 0 initial outlay**:
- Purchase: €145,000
- Frais de notaire (~7-8% existing): €11,000
- Furniture + immediate capex: €5,000
- Mortgage setup: ~€1,500
- = **€162,500 initial**

**Annual operating** (year 1):
- Mortgage P&I (€116k loan, 3.5% fixed, 25y): ~€7,000/yr
- Taxe foncière (Adriers commune-typical): ~€500/yr
- Assurance habitation (Catnat 20% surcharge from Jan 2025): ~€450/yr
- Maintenance (1.5% of price): ~€2,200/yr
- Utilities (rural, oil/wood heating): ~€1,800/yr
- = **~€11,950/yr**

**Year 30 cumulative (nominal)**:
- Initial: €162,500
- 25 yrs mortgage: €175,000 (P&I)
- 5 yrs no-mortgage: €0 P&I
- 30 yrs taxe foncière + insurance + maintenance + utilities: ~€155,000 (with 2% inflation)
- = **~€492,500 cumulative outlay**

**Year 30 sale**:
- Property at 1.5%/yr: €145k * 1.015^30 ≈ €227,000
- CGT exempt (primary residence)
- Notary seller: 0% (buyer pays)
- Agent commission ~5% (FR FNAIM): -€11,400
- = **Net sale: €215,600**

**Net TCO**:
- €492,500 - €215,600 = **€276,900 net 30-yr cost**
- Inflation-adjusted (real €): ~€176,000 in today's purchasing power

**Implication**: 30-yr "cost of housing yourself" in this Adriers property = ~€176k real (vs ~€500/mo rent equivalent for 30 yrs = ~€180k). Roughly break-even rent vs buy at this scale, with appreciation upside if FR rural prices recover.

## Comparison output

The TCO calculator can be combined with `--compare` to show TCO across countries for the same nominal property value:

```
/property-deep-dive --compare=fr,it,es,pt,gr --tco --price=200000 --hold=30
```

→ Outputs a 5-country TCO comparison table.

## Confidence + sensitivity

The calculator output is sensitive to:
1. **Mortgage rate** (±0.5% changes 30-yr P&I by ~10-15%)
2. **Inflation rate** (real vs nominal divergence)
3. **Appreciation rate** (most volatile — back-test against `--price` history)
4. **Maintenance assumption** (1-2% range — older buildings need more)
5. **CGT regime** (varies — check primary-residence exemptions)

Always run a sensitivity table on rate + appreciation + maintenance.

## Anti-hallucination

- **Don't quote a single TCO number** — always show 3 scenarios (pessimistic / central / optimistic)
- **Pull rates from `--finance` per-country**, not generic
- **Pull tax/CGT from per-country `--tax` section** — don't extrapolate
- **Surface what the user can't predict** (rate path, inflation path, appreciation path) and let them set the dial
- **Real vs nominal**: always show both; many users only think in nominal and underestimate

## Implementation notes

This is a calculator pattern — the values come from per-country playbooks. The skill should:
1. Pull `--tax`, `--finance`, `--insurance`, `--notary` from the country playbook
2. Default unknown maintenance / utilities to country averages
3. Allow overrides via flags (`--rate=3.0`, `--appreciation=1.5`)
4. Output both nominal + real
5. Show sensitivity table

## Status

Last refreshed: 2026-04-26.
