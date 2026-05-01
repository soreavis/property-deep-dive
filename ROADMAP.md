# Roadmap — Country Backlog

Working document for country additions beyond the current 87. Captures candidates, priority tiers, and skip rationale so future batches can pick up where prior research left off without re-litigating the analysis.

**Status**: backlog — no commitment to schedule. Drafted 2026-05-01 after the 62 → 87 sprint (PRs #69 + #70 + #74 + #76 + #78 tier system).

## Current coverage

87 countries fully populated across 10 regions (`_regions.json`). Tiered refresh cadence in `_tiers.json` (A=15 quarterly · B=30 semi-annual · C=42 annual).

## Tier-1 — high-signal candidates (8)

Foreign-buyer demand + regulatory activity + addressable data quality. Strongest candidates for the next batch.

| ISO2 | Country | Why now | Likely refresh tier |
|---|---|---|---|
| **mu** | Mauritius | Financial centre; IRS/PDS schemes for foreign property buyers; retirement-friendly tax regime; mature primary-source data | B |
| **kz** | Kazakhstan | Almaty/Astana booming post-2022 Russia exodus; 2024-25 fiscal reforms; active foreign-investor track | A or B |
| **cv** | Cape Verde | Active residency-by-investment programme; EUR-pegged tourism property; EU-aligned regulation | B |
| **sc** | Seychelles | Luxury second-home market; distinct land-leasing rules for non-residents; recent reforms | C |
| **cn** | China | Foreign-buyer rules unique (PRC residency requirements, tier-1 city restrictions) but immense addressable demand for Chinese-diaspora users | B |
| **jm** | Jamaica | Strong diaspora demand; retirement market; USD-denominated transactions common | C |
| **bs** | Bahamas | Retirement/second-home market; no-income-tax regime; high transaction volumes; BDR + economic-permanent-residence routes | B |
| **sm** | San Marino | Trivial effort; completes the microstate group (LI/AD/MC/SM) for symmetry | C |

**Region impact**: Mauritius/Cape Verde/Seychelles → expand Africa region (6 → 9). Kazakhstan → new "Central Asia" region or extend Caucasus & Eastern non-EU (4 → 5). China → APAC (12 → 13). Jamaica/Bahamas → new "Caribbean" region or extend Latin America (12 → 14). San Marino → European Microstates (3 → 4).

**Estimated effort**: ~2.5 hours via parallel subagents (single batch, similar to May 2026 sprint).

## Tier-2 — niche but real demand (8)

Worth doing eventually but lower signal/effort ratio than Tier-1.

| ISO2 | Country | Notes |
|---|---|---|
| **bb** | Barbados | DNV (Welcome Stamp) + retirement; smaller volumes than BS but distinct legal regime |
| **bz** | Belize | Retirement market + new RBI; primary-source data thin |
| **lk** | Sri Lanka | Post-2022 economic-crisis recovery; golden visa restored 2024 |
| **kh** | Cambodia | Sihanoukville/Phnom Penh foreign-buyer activity; strata title rules unique |
| **mv** | Maldives | Luxury private-island market; non-resident leasehold-only |
| **gh** | Ghana | Diaspora-driven; Akwaaba investor visa; Accra hot market |
| **rw** | Rwanda | Kigali emerging; investor visa; clean primary-source data |
| **uz** | Uzbekistan | Post-2017 opening; foreign-investor reforms 2023-25; thin English-language sources |

## Special case — Crown Dependencies & territories

Significant offshore property markets with their own legal regimes, but **schema doesn't cleanly accommodate sub-sovereign jurisdictions** under the country-ISO2 model:

- **je** (Jersey)
- **gg** (Guernsey)
- **im** (Isle of Man)
- **gi** (Gibraltar)

Each has high foreign-buyer demand, distinct property law, and is poorly covered under the parent state's playbook (uk). Adding them requires a design discussion: do we introduce a "territory" classifier? Add them as siblings of their parent state? Reuse the country slot with a sub-region distinction? **Defer until schema decision.**

Similar territory-level cases for future consideration: Faroe Islands (DK), Greenland (DK), French overseas (FR), Caribbean Netherlands (NL).

## Skip — not worth pursuing

| Bucket | Examples | Why skip |
|---|---|---|
| Sanctions / active conflict | RU, BY, IR, IQ, SY, YE, LY, KP, MM | Data integrity + ethical issues + no realistic foreign-buyer audience |
| War-affected (track via regwatch instead) | UA | Demand exists for tracking, but "buy now" guidance irresponsible until reconstruction stabilises. Better as a `regulatory-watch.md` entry than a full playbook |
| Sub-Saharan frontier (low signal) | TZ, UG, MZ, AO, CM, SN, ET | Thin foreign-buyer market; primary-source data sparse; returns mostly diaspora or development-finance |
| Smaller Latam | NI, HN, SV, HT, BO | Limited data quality + low foreign-buyer volume. SV's Bitcoin City pivot is the only news angle, not enough for a full playbook |
| Pacific micro-states | TO, WS, FJ, NC | Tiny markets, foreign-ownership often restricted, primary sources mostly French / vernacular |
| Tribal / unrecognised | XK (Kosovo) — political complexity | Recognition status complicates source-tier ranking; revisit if EU accession path activates |

## Decision log

- **2026-05-01**: backlog drafted post-87-country sprint; no batch scheduled. Tier-1 prioritised for next research cycle when the user greenlights.
