# Roadmap — Coverage Backlog

Working document for additions beyond the current 103 countries. Captures completed batches, future country candidates, section-level extensions, and skip rationale.

## Current coverage

103 countries fully populated across 13 regions (`_regions.json`). Tiered refresh cadence in `_tiers.json` (A=16 quarterly · B=38 semi-annual · C=49 annual + 1 unified moved by #113).

## Completed batches

### Tier-1 (PR #111 — 2026-05-07)

8 countries: mu (Mauritius), kz (Kazakhstan), cv (Cape Verde), sc (Seychelles), cn (China), jm (Jamaica), bs (Bahamas), sm (San Marino). Created `caribbean` region (do/bs/jm). 26 regulatory-watch entries added.

### Tier-2 (PR #113 — 2026-05-07/08)

8 countries: bb (Barbados), bz (Belize), lk (Sri Lanka), kh (Cambodia), mv (Maldives), gh (Ghana), rw (Rwanda), uz (Uzbekistan). Created `south-asia` (in/lk/mv) + `central-asia` (kz/uz) regions. 34 regulatory-watch entries added.

## Coverage extensions — post-103 backlog

Sourced from Reddit gap-analysis 2026-05-08. Cross-validated across 6+ subreddits + adjacent expat forums.

### NEW sections

| Flag | Why | Effort |
|---|---|---|
| `--permits` | ✅ **Shipped 2026-05-08** (#116). Building-works regime: declaration vs full permit thresholds, listed-building overlays, post-completion conformity certs, retention rules. Was scattered across `--notary` / `--type=heritage` / `--journey=renovation` / integrity-checks in only 46/103 playbooks. Name-collision risk vs `--work=<profession>` documented. Canonical: `shared/permits.md`. | shipped |
| `--agent` | ✅ **Shipped 2026-05-08** (#118). Buyer-side agency landscape & commission structure (commission rate, who pays, licensing regime, MLS y/n, dual-agency legality, exclusivity-contract risk, EBA availability). Captures 2024+ reforms: US NAR settlement (eff. 17 Aug 2024), DE Bestellerprinzip §§656a-d BGB, CZ Zákon 39/2020, TR Yetki Belgesi 2018, VN Law 29/2023. Canonical: `shared/agent.md`. | shipped |
| `--scams` | ✅ **Shipped 2026-05-08** (#119). Country-specific transaction-fraud register with regulator advisories / prosecutions. 7 cross-cutting traps (BEC at closing, title forgery, off-plan disappearance, foreign-restricted-zone nominee, golden-visa price-inflation, customary-tenure/restitution-lien, concession-vs-freehold). Captures 2024-2026 enforcement waves (FBI IC3 $2.77B BEC, NY/FL/TX deed-theft statutes, GR Circular 1/2026, TR "Bona Fide" Sept 2025, ZA Hawarden v ENS, etc.). Canonical: `shared/scams.md`. | shipped |
| `--language` | ✅ **Shipped 2026-05-08** (#120). Foreign-buyer language requirements: deed-language rule, sworn-translator-at-signing mandate, POA / Hague Apostille chain, mandatory diagnostic-document language, sworn-translation cost band. Captures 2024-2026 Apostille status changes (VN in force 11 Sept 2026, TH approved Dec 2025, CN Nov 2023, AE non-member, RW Jun 2024, CA Jan 2024). Canonical: `shared/language.md`. | shipped |
| `--connectivity` | ✅ **Shipped 2026-05-08** (#121). Foreign-buyer broadband profile: address-level fibre availability checker (regulator URL), dominant ISPs, tariff bands (entry/mid/gigabit), FTTH urban %, rural fallback, **calendar-actionable Starlink licence registry** (AE Mar 2026, JO Feb 2026, CO Apr 2024, ZA grey 2026-27 BEE-blocker, BA only major-EU absence, CN/IR/SY/RU/BY banned, IN/SA/MA/EG/IL pending), build-era / strata trap, country-specific quirk (ZA load-shedding ISP-UPS premium, LB EDL outages, CN GFW + IPLC). Reframes earlier "Internet/fiber granularity disconfirmed" entry — depth meaningfully exceeds `--mains`. Canonical: `shared/connectivity.md`. | shipped |
| `--home-tax` | Buyer-nationality tax overlay: US FATCA Form 8938 + FBAR + PFIC + FIRPTA-equivalent, UK non-dom abolition 2025, CA worldwide reporting. Indexed by buyer nationality, not property country. | ~200-300 lines |
| `--remote` | Buying without being there: POA + remote signing + e-conveyancing. AU PEXA, FR notary-eIDAS POA, IT remote-procura, US RON state-by-state, NL DigiD overlay. Pairs strongly with `--language`. | ~200-250 lines + country matrix |
| `--relocation` | Pets + driving licence + vehicle import + utility setup. All "surprise cost / surprise timeline" 90-day post-completion. ≥3 subreddits. | ~300-400 lines, country-tagged |
| `--schools` | International + local school cost / waitlists / residency-priority. Shapes intra-country location decisions. ≥3 subreddits. | ~250-350 lines, country-tagged |

### Section extensions (existing flags)

- `--finance` — add banking sub-section (NIE/NIF/CURP order, FATCA rejection workarounds, expat-banking-arm minimums)
- `--rental` — neighborhood-level STR moratorium tracking via `regulatory-watch.md`
- `--notary` — forced-heirship sub-section (EU 650/2012, French Aug 2021 amendment, Italian quota legittima)
- `--risks` / `--type=off-plan` — build-quality + new-build defect-rate flags (Spain ~95%, Cyprus damp construction)
- `--digital-nomad` (or new sub-flag) — working-age healthcare carve-out (currently only retirement-age covered under `--retirement`)
- `--mains` — utilities-reliability extension (EC 8-14hr blackouts 2024, DR rolling outages, BR drought rationing, LB collapsed grid, ZA load-shedding). Distinct from connection cost. ~80-120 lines.

### TCO calculator additions

- Community/HOA charges line + reserve-fund-health flag
- Insurance line (already implicit; surface explicitly)
- Country-specific lines (e.g., fideicomiso renewal for Mexico restricted-zone)

### Disconfirmed (already adequately covered)

- ~~Internet/fiber neighborhood granularity — `--mains` is sufficient~~ (reframed and shipped as `--connectivity` #121 — broadband checker + ISP roster + tariff bands + Starlink registry + strata trap meaningfully exceeds the `--mains` one-liner)
- Customary-tenure / nominee structures — `compare.md` + `finance.md` cover (Bali nominee voidness, Mexico fideicomiso 50/100km, Thailand 49% condo, Philippines 60/40)
- Foreign-buyer mortgages — `--finance` matrix is dense
- Visa/Golden-Visa lifecycle — `visa-programs.md` ENDED registry adequate
- Capital-controls + FET-form — `--currency` strong
- EV chargers — low signal, single-line under `--mains` enough

## Schema-blocked: Crown Dependencies + territories

The project's country-ISO2 model doesn't cleanly accommodate sub-sovereign jurisdictions. **Required first: schema decision PR** answering: territory classifier? sibling-of-parent (uk-je, uk-im, dk-fo, dk-gl, fr-yt, fr-re, nl-aw, nl-cw)? Sub-region under parent's playbook?

Once schema is settled, three batches are unlocked:

### Batch A — UK Crown Dependencies (4)

| Code | Jurisdiction | Why |
|---|---|---|
| **je** | Jersey | Major offshore finance centre; HVR + 2(1)(e) housing licence; SoCT regime |
| **gg** | Guernsey | Open vs Local market split; "Inscribed" property tier 5 entry |
| **im** | Isle of Man | Distinct tax regime (no CGT, no inheritance); finance sector |
| **gi** | Gibraltar | UK overseas territory (not Crown Dep but same schema problem); EU/Schengen interaction post-Brexit |

### Batch B — DK territories (2)

| Code | Jurisdiction | Why |
|---|---|---|
| **fo** | Faroe Islands | Distinct legal regime; Faroese-language primary sources; salmon-economy property dynamics |
| **gl** | Greenland | Self-government in 2009; Inuit property-law overlay; geopolitical / mineral-rights interest |

### Batch C — FR overseas + NL Caribbean (deferred pending demand signal)

- French overseas (Martinique, Guadeloupe, Réunion, Mayotte, French Guiana, etc.) — applies metropolitan French law with overlays; foreign-buyer demand modest
- Caribbean Netherlands (Aruba, Bonaire, Curaçao, Sint Maarten) — different legal status: Aruba/Curaçao/Sint Maarten are constituent countries; Bonaire/Saba/St Eustatius are special municipalities. Heterogeneous schema mess on its own.

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
- **2026-05-07**: Tier-1 batch landed (#111). New caribbean region.
- **2026-05-08**: Tier-2 batch landed (#113). New south-asia + central-asia regions. Tier-1 + Tier-2 backlog exhausted within current schema.
- **2026-05-08**: Reddit gap-analysis surfaced 7 strong-signal coverage gaps. Backlog item for post-103 work.
- **2026-05-08**: `--permits` greenlit and implemented in same session — see CHANGELOG. Triggered by user follow-up flagging the building-permits coverage gap (no dedicated flag, ~45% scattered coverage).
- **2026-05-08**: Reddit/expat-forum gap-analysis #2 surfaced 6 additional candidates: `--agent`, `--scams`, `--language`, `--home-tax`, `--remote`, plus `--mains` utilities-reliability extension. Top-2 (`--agent`, `--scams`) clear cross-validation bar most decisively.
