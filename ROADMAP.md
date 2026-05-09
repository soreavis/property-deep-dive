# Roadmap — Coverage Backlog

Working document for additions beyond the current 103 countries. Captures completed batches, future country candidates, section-level extensions, and skip rationale.

## Current coverage

103 countries fully populated across 13 regions (`config/_regions.json`). Tiered refresh cadence in `config/_tiers.json` (A=16 quarterly · B=38 semi-annual · C=49 annual + 1 unified moved by #113).

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
| `--home-tax` | ✅ **Shipped 2026-05-09** (#127). Buyer-nationality tax overlay indexed by buyer's tax-residence country (NOT property country) — uniquely orthogonal to all other sections. Covers 20+ buyer cohorts: US (citizenship-based; FATCA Form 8938 + FBAR FinCEN 114 + PFIC § 1297 + § 988 phantom-currency-gain mortgage trap anchored by *Quijano v. US* + § 877A expat MTM + OBBBA $15M estate exemption permanent from 2026), UK (FA 2025 — non-dom abolished 6 Apr 2025, 4-y FIG regime, IHT residence-based via 10/20 LTR test, FHL abolition, *Bentley v Pike* sterling CGT), CA (T1135 personal-use carve-out, § 128.1 departure tax INCLUDES foreign RE, 66.67% inclusion-rate reform CANCELLED 21 Mar 2025), AU (Div 855, FRCGW 15% from 1 Jan 2025, MRE removed for foreign residents post-30 Jun 2020), NZ (FIF on foreign-property holding entities, ring-fenced rental losses § EL 4, foreign property OUTSIDE bright-line), DE (§ 23 EStG 10y Spekulationsfrist, § 6 AStG ATAD reform), FR (IFI worldwide RE > €1.3M + Form 3916 + PLF 2026 exit-tax extension in flux), IT (IVIE 1.06% from 2024, Quadro RW, 24-bis €200k from 10 Aug 2024 / PLF 2026 → €300k), ES (Modelo 720 post-ECJ, Patrimonio + ITSGF > €3M, Beckham 24% extended), NL (Box 3 Hoge Raad 2024 crisis, Wet WRBox3 → 1 Jan 2028, 30%-ruling → 27% from 2027), Nordics (DK Ejendomsværdiskat uniquely on foreign property, NO 12-y exit-tax cap 2024), CH (Eigenmietwert abolished by 28 Sept 2025 vote effective 1 Jan 2029), JP/KR/SG/HK/CN (territorial vs worldwide; JP 5y PR cliff; KR 5y foreign-shield; CN 6-y rule resetting on 30+ day exit; CN inheritance still NOT enacted), IL (Olim 10y + 1 Jan 2026 reporting reform), emerging markets (IN LRS USD 250k + TCS 20%, BR Lei 14.754/2023, MX, ZA SDA/FIA/AIT + § 9H exit tax INCLUDES foreign RE, AE/SA/GCC). 7 cross-cutting traps (phantom currency-gain, PFIC, wealth-tax overlap, estate-tax patchwork, exit-tax events, structural decisions, treaty FTC vs exemption). Canonical: `shared/home-tax.md` (1086 lines). | shipped |
| `--remote` | ✅ **Shipped 2026-05-09** (#128). Foreign-buyer remote-execution mechanisms: POA + apostille / consular legalisation, remote video-conference signing at notary, eIDAS QES / equivalent, digital land-register filing, mortgage-bank residual wet-ink. **Fully remote property deeds**: PT (DL 126/2021 since Apr 2022), BE (8 Apr 2024), EE (since 1 Feb 2020 — global benchmark), LT (since 1 Jul 2021), LV (resident-only), TR (consulate vekaletname), BR (e-Notariado), GE (PSH + e-Apostille), RW (Irembo + e-Apostille from 5 Jun 2024). **Excluded for property**: DE BeurkG § 16a-d (Auflassung), AT § 31 GBG, IT (rogito requires *contestualità fisica*), NL DOBV (BV-only), ES Ley 11/2023 catalogue (compraventa excluded), CH cantonal mosaic, MT physical simultaneity. **PL** actively REJECTING foreign remote POAs per *iNPN 1(98)/2025*. **US RON** ~46 states + DC + PR; **CA SB 696 effective 1 Jan 2030 backstop** (regulations pending); **SECURE Notarization Act HR 1777/S 1561** NOT enacted. **AU PEXA + Sympli interoperability SUSPENDED** 2024. **ZA e-DRS launched 1 Apr 2025**; ***Hawarden v ENS* [2024] ZASCA 90** SCA REVERSED — BUYER bears BEC risk. **VN Hague in force 11 Sept 2026**; TH cabinet approval Dec 2025 deposit pending. **eIDAS-2 Reg 2024/1183** in force 20 May 2024; EUDI Wallet rollout target end of 2026. 7 cross-cutting traps (eIDAS recognition asymmetry; mortgage-bank residual wet-ink; time-zone collision; state/canton fragmentation; identity-verification Catch-22; apostille chain still required; AML/KYC gatekeepers). Canonical: `shared/remote.md` (542 lines). | shipped |
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
- **2026-05-09**: `--home-tax` shipped (#127, plugin 2026.05.8). 28th section. Buyer-nationality tax overlay covering 20+ buyer cohorts; 1086-line canonical doc. *Quijano v. United States* anchors the § 988 phantom-currency-gain trap; OBBBA 4 Jul 2025 made TCJA estate exemption permanent at $15M from 2026; UK FA 2025 abolished non-dom regime + introduced 4-y FIG regime + IHT residence-based via 10/20 LTR test from 6 Apr 2025; CH Eigenmietwert abolition by 28 Sept 2025 vote effective 1 Jan 2029; CA 66.67% inclusion-rate reform CANCELLED 21 Mar 2025 by PM Carney; CN inheritance tax still NOT enacted as of 2026.
- **2026-05-09**: `--remote` shipped (#128, plugin 2026.05.9). 29th section. Foreign-buyer remote-execution mechanisms; 542-line canonical doc covering 5 mechanisms (POA + apostille / remote video-deed / eIDAS QES / digital land-register / mortgage residual wet-ink). PT + BE genuinely fully remote for property; EE/LT/LV operational e-notar; PL actively REJECTING foreign remote POAs per *iNPN 1(98)/2025*. US RON 46 states + DC + PR; CA SB 696 effective 1 Jan 2030 backstop. *Hawarden v ENS* SCA reversal: BUYER bears BEC risk. AU PEXA + Sympli interoperability suspended 2024. eIDAS-2 EUDI Wallet rollout target end of 2026.
