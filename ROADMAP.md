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
| `--relocation` | ✅ **Shipped 2026-05-09** (#129). Foreign-buyer 90-day post-completion onboarding: pets + driving licence + vehicle import + utility setup + healthcare gap. FAVN/RFFIT-titer 7-month flow for AU/NZ/JP/SG-Schedule-III/MY; CDC dog-import form 1 Aug 2024; AU EDR removed Apr 2025-Feb 2026; LEZ landscape (UK ULEZ / FR ZFE-m / DE Umweltzone / ES Madrid 360 / PL Warsaw + Kraków / NL zero-emission); foreign-buyer Catch-22 on utility setup (SCHUFA + Anmeldung + Steuer-ID). Canonical: `shared/relocation.md`. | shipped |
| `--schools` | ✅ **Shipped 2026-05-10** (#141). Foreign-buyer schools / education-access layer for working-age families with school-age dependents. International school landscape per major city (IB / British / American / French Lycée AEFE / German Schule + Nord Anglia / Cognita / GEMS / ISP / Globeducate / Inspired / QSI emerging-markets franchise); annual fee bands USD 3-80k; waitlist horizons weeks-to-decade (AU Sydney top private 5-10y from birth, ZA St John's 3-7y, FR Paris Lycée International 5+y, NL Amsterdam capacity crisis 2+y); local public school landscape + language-of-instruction; catchment-area / residency-priority rules driving 30-300% property-value premium (CN xuequ Beijing/Shanghai/Shenzhen, US public-school-district, AU NSW Selective High Schools, NZ Auckland Grammar zone, UK London catchment); UK 1 Jan 2025 20% VAT shock; AE KHDA/ADEK ratings; post-disaster crisis disruption (IL post-7-Oct-2023, LB ongoing, UA post-Feb-2022, TR post-6-Feb-2023, CN post-2024 expat repatriation, BNO HK emigration aftermath). Canonical: `shared/schools.md` (507 lines). | shipped |

### Section extensions (existing flags)

- `--finance` — ✅ **Shipped 2026-05-10** (#137). Banking-access extension (`shared/finance-banking.md`, 515 lines): tax-ID prerequisite chain (NIE/NIF/CURP/CPF/Iqama/PESEL/CPR ordering), FATCA acceptance bucket per country (Standard/Restricted/Refused), named expat-banking arms with minimums (HSBC Expat Jersey universal fallback, Charles Schwab International, UBS WM, Lombard Odier, LGT, Citi IPB SG), 7 cross-cutting traps, 100-country one-liners across 6 region blocks, 120+ dated reform-calendar entries.
- `--rental` — neighborhood-level STR moratorium tracking via `regulatory-watch.md` (still TODO)
- `--notary` — ✅ **Shipped 2026-05-10** (#138). Forced-heirship sub-section (`shared/notary-forced-heirship.md`, 489 lines): civil-law forced shares vs common-law testamentary freedom vs Sharia, EU 650/2012 Brussels IV, FR 24 Aug 2021 prélèvement compensatoire, CH 1 Jan 2023 Pflichtteil reform, KR 25 Apr 2024 sibling yuryubun unconstitutional ruling.
- `--risks` / `--type=off-plan` — ✅ **Shipped 2026-05-10** (#139). Build-quality + new-build defect-rate sub-section (`shared/risks-build-quality.md`, 511 lines): statutory warranty regimes (FR garantie décennale, ES Ley 38/1999 LOE, IT Codice Civile Art. 1669, UK NHBC Buildmark), off-plan deposit-protection (FR GFA, ES aval bancario, IT polizza fideiussoria, DE MaBV, PL DFG), high-impact incidents (TR 6 Feb 2023, CN Evergrande, AU Opal Tower, US Surfside, UK Grenfell, NZ leaky homes). Pairs with `--type=off-plan`.
- `--digital-nomad` — ✅ **Shipped 2026-05-10** (#140). Working-age healthcare carve-out sub-section (`shared/digital-nomad-healthcare.md`, 523 lines): DN-visa healthcare requirements, public-system enrollment timelines (DE day-1 / CH 3-month / NL 4-mo / FR PUMA 3-mo / KR 6-mo / JP 14 days / TW 6-mo / IL 6-mo / ES Convenio Especial 1-yr), private insurance options, EHIC/GHIC reciprocity, 100-country coverage. Companion to per-country `--retirement` healthcare layer.
- `--mains` — ✅ **Shipped 2026-05-09** (#134). Utilities-reliability extension (`shared/mains-reliability.md`): EC 8-14hr blackouts 2024, DR rolling outages, BR drought rationing, LB collapsed grid, ZA load-shedding suspended Mar 2025, grid-type + SAIDI/SAIFI + outage band 🟢🟡🟠🔴 + load-shedding regime + 2024-2026 reform calendar + water-supply reliability.

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
- **2026-05-09**: `--relocation` shipped (#129, plugin 2026.05.10). 30th section. Foreign-buyer 90-day post-completion onboarding; 588-line canonical doc covering 4 subdomains (pets + driving licence + vehicle import + utility setup + healthcare gap). FAVN/RFFIT-titer 7-month pet-import flow for AU/NZ/JP/SG-Schedule-III/MY; CDC dog-import form 1 Aug 2024; AU EDR category removed Apr 2025-Feb 2026; LEZ landscape (UK ULEZ / FR ZFE-m / DE Umweltzone / ES Madrid 360 / PL Warsaw + Kraków / NL zero-emission); foreign-buyer Catch-22 on utility setup (SCHUFA + Anmeldung + Steuer-ID).
- **2026-05-09**: `config/` repo layout (#130, follow-up — no plugin bump). `_regions.json` + `_tiers.json` relocated from repo root to `config/` via `git mv` (blame preserved). 16 files updated in lockstep (3 Python scripts + 4 GitHub workflows + 7 docs + the JSON `_comment` field). Removes two underscore-prefixed top-level files; groups build-config under one folder. Pure refactor — no behaviour change.
- **2026-05-09**: `config/_visa-programs.json` shipped (#131). Machine-readable source of truth for the `--visa` section; 192 programme records across 13 regions × 103 countries. Region tables in `shared/visa-programs.md` now auto-render from JSON via `scripts/render-visa-programs.py` (idempotent, `--check` / `--diff` modes for CI). New `scripts/audit-visa-programs.py` lints country playbooks against JSON status (14 programme×country pairs in scope; all 14 already acknowledged). New workflow `visa-programs-audit.yml` runs both checks on PR + push to main. Closes the manual-sync drift channel where reforms previously required hand-editing `visa-programs.md` table + every affected country playbook + `regulatory-watch.md` ENDED registry in lockstep.
- **2026-05-09**: `--mains` utilities-reliability extension shipped (#134, plugin 2026.05.11 → 2026.05.12). New `shared/mains-reliability.md` loaded alongside per-country mains-connection layer. Grid-type + SAIDI/SAIFI + outage band 🟢🟡🟠🔴 + load-shedding regime + 2024-2026 reform calendar + water-supply reliability. ZA load-shedding suspended 12 Mar 2025; LB collapsed grid; EC 8-14hr blackouts 2024.
- **2026-05-10**: 4-extension wave shipped in single day — `--finance` banking-access (#137, plugin 2026.05.13), `--notary` forced-heirship (#138, plugin 2026.05.14), `--risks` build-quality + off-plan (#139, plugin 2026.05.15), `--digital-nomad` working-age healthcare carve-out (#140, plugin 2026.05.16). All four PRs merged sequentially same day with stops-between-for-review cadence; ~500 lines per extension; 6 parallel region agents per section; 15-30 anti-hallucination corrections per section surfaced (FR Conseil constitutionnel Decision 2023-1059 actually about police access not Art. 913 al. 4; QC abolished classical légitime in 1994 only Art. 684 food-support survives; BR doação clawback follows STJ 10-yr prescription not 4 years; MA seismic Decree 2.24.766 Sep 2024 not 2-23-755; SA M/43 not M/27; JO Art. 788 not Art. 798; CY DN visa quota 500→1,000 not 1,000→5,000; BG DN visa launched 20 Dec 2025; MD DN visa launched 20 Sep 2025; UY May 2023 not Aug 2023; DR has NO formal DN visa — recurring conflation with Dominica DM; KE NHIF→SHA 1 Oct 2024; SK Jul 2025 = TIGHTENING 700/yr quota not launch). Stacked-PR mechanics (#140 vs #139 plugin.json + CHANGELOG conflict) resolved via rebase + sed plugin.json + Python regex CHANGELOG-conflict strip + force-with-lease + auto-merge.
- **2026-05-10**: `--schools` shipped (#141, plugin 2026.05.16 → 2026.05.17). 31st user-invocable section. Foreign-buyer schools / education-access layer for working-age families with school-age dependents; 507-line canonical `shared/schools.md` companion to `--retirement` (retirement-age 65+) and `--digital-nomad-healthcare` (working-age healthcare). International school landscape per major city (IB / British / American / French Lycée AEFE / German Schule + Nord Anglia / Cognita / GEMS / ISP / Globeducate / Inspired / QSI emerging-markets franchise); annual fee bands USD 3-80k (NYC Trinity USD 50-65k highest globally; CV/SC USD 3-15k Africa lowest); waitlist horizons weeks-to-decade (AU Sydney top private 5-10 yr from birth, ZA St John's 3-7 yr, FR Paris Lycée International Saint-Germain 5+ yr, NL Amsterdam capacity crisis 2+ yr since 2023, CH Geneva Ecolint 18-24 mo, SG/HK 12-36 mo); catchment-area / residency-priority rules driving 30-300% property-value premium (CN xuequ Beijing/Shanghai/Shenzhen 30-300%, US Westchester/Marin/Palo Alto/Fairfield 30-100%, NZ Auckland Grammar zone Epsom + Mt Eden 20-40%, UK London catchment 15-30%); UK 1 Jan 2025 20% VAT shock + business-rates relief removal; AE Dubai KHDA + Abu Dhabi ADEK annual ratings; post-disaster + crisis disruptions (IL post-7-Oct-2023, LB ongoing, UA post-Feb-2022, TR post-6-Feb-2023, CN post-2024 expat repatriation, BNO HK emigration aftermath, NG Lagos AISL Victoria Island/Ikoyi tied to oil-expat demand). 7 cross-cutting traps + 7 universal mitigations + 100-country one-liners across 6 region blocks. Section count: 30 → 31. Section-extensions backlog from Reddit gap-analysis 2026-05-08 now exhausted EXCEPT `--rental` neighborhood-level STR moratorium tracking via regulatory-watch.md.
