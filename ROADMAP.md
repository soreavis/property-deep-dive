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
| `--relocation` | Pets + driving licence + vehicle import + utility setup. All "surprise cost / surprise timeline" 90-day post-completion. ≥3 subreddits. | ~300-400 lines, country-tagged |
| `--schools` | International + local school cost / waitlists / residency-priority. Shapes intra-country location decisions. ≥3 subreddits. | ~250-350 lines, country-tagged |

### Section extensions (existing flags)

- `--finance` — add banking sub-section (NIE/NIF/CURP order, FATCA rejection workarounds, expat-banking-arm minimums)
- `--rental` — neighborhood-level STR moratorium tracking via `regulatory-watch.md`
- `--notary` — forced-heirship sub-section (EU 650/2012, French Aug 2021 amendment, Italian quota legittima)
- `--risks` / `--type=off-plan` — build-quality + new-build defect-rate flags (Spain ~95%, Cyprus damp construction)
- `--digital-nomad` (or new sub-flag) — working-age healthcare carve-out (currently only retirement-age covered under `--retirement`)

### TCO calculator additions

- Community/HOA charges line + reserve-fund-health flag
- Insurance line (already implicit; surface explicitly)
- Country-specific lines (e.g., fideicomiso renewal for Mexico restricted-zone)

### Disconfirmed (already adequately covered)

- Internet/fiber neighborhood granularity — `--mains` is sufficient
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
