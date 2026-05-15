# property-deep-dive

[![Release](https://img.shields.io/github/v/release/soreavis/property-deep-dive?label=release&sort=semver)](https://github.com/soreavis/property-deep-dive/releases)
[![License: MIT](https://img.shields.io/github/license/soreavis/property-deep-dive)](./LICENSE)
[![URL liveness](https://github.com/soreavis/property-deep-dive/actions/workflows/url-liveness.yml/badge.svg)](https://github.com/soreavis/property-deep-dive/actions/workflows/url-liveness.yml)
[![PR validate](https://github.com/soreavis/property-deep-dive/actions/workflows/pr-validate.yml/badge.svg)](https://github.com/soreavis/property-deep-dive/actions/workflows/pr-validate.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/soreavis/property-deep-dive/badge)](https://scorecard.dev/viewer/?uri=github.com/soreavis/property-deep-dive)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/12655/badge)](https://www.bestpractices.dev/projects/12655)

**Runs in [Claude Code](https://docs.claude.com/claude-code) and [Claude Cowork](https://www.anthropic.com/product/claude-cowork)** — same plugin format and same `/property-deep-dive` invocation in both. Install UX differs: Claude Code uses slash commands, Cowork uses its in-app plugin browser (see [Install](#install)).

**Pre-purchase property due diligence across 103 countries** — tax, risks, rental yield, visa, mortgage, broadband, buyer-nationality home-country tax overlay, foreign-buyer remote-execution mechanisms, 90-day post-completion relocation logistics, international schools + catchment areas, and 16 other facets per address. Sourced from primary government data, every claim dated and confidence-labelled. **38 user-invocable sections**, **4 cross-cutting layers** (integrity / journey / type / update), and a regulatory-watch system that surfaces reforms before they invalidate the data.

> **Decision-support, not legal/tax/financial advice.** Property purchases are six- to seven-figure decisions; this skill helps you ask the right questions and surface risks early. See [DISCLAIMER.md](./DISCLAIMER.md) for full scope.

> **Stability**: production-ready content. Versioned with [CalVer](#versioning) — each tag encodes the release month (e.g. `2026.04.0`).

## What it does

Given an address — `1 Rue Principale, 86430 Adriers, France`, `https://www.rightmove.co.uk/properties/<id>`, or coordinates — the skill:

1. Detects the country (postcode pattern, country name, or `--country=<iso2>` flag)
2. Loads the country's playbook from `skills/property-deep-dive/countries/<iso2>/playbook.md`
3. Runs the requested sections (or `--all`)
4. Applies the anti-hallucination guard
5. Outputs to terminal or saves a Markdown report

### Sections (32 user-invocable)

**Core (10)** — `--price` `--traffic` `--tax` `--rental` `--work=<profession>` `--risks` `--mains` `--crime` `--amenities` `--climate`

**Financial / process (7)** — `--finance` `--currency` `--visa` `--insurance` `--notary` `--home-tax` (buyer-nationality tax overlay: home-country exposure when buying / owning / disposing of foreign property — 20+ buyer cohorts incl. US FATCA/PFIC/§988 · UK FA 2025 FIG/LTR · CA T1135 + § 128.1 · DE/FR/IT/ES/NL · Nordics · CH · JP/KR/SG/HK/CN · IL · IN/BR/MX/ZA/GCC + 7 cross-cutting traps) · `--cross-border` (opt-in cross-border-residency / cross-border-business framework layer — DTA Art. 4(2) tie-breaker pointer, POEM/PE flag for company owners, origin-country deregistration entry points, EU/EEA/CH free-movement clarification; framework + linkage only with mandatory professional-advisor call-out — does NOT compute liability)

**Regulatory (1)** — `--permits` (building-works permit thresholds, heritage overlays, conformity-at-completion)

**Transaction (2)** — `--agent` (buyer-side agency landscape: commission, licensing, MLS, dual-agency, exclusivity, EBA, off-plan) · `--scams` (country-specific transaction-fraud register: BEC, deed forgery, off-plan disappearance, nominee structures, golden-visa price-inflation)

**Process (4)** — `--language` (foreign-buyer deed-language rule + sworn-translator regime + Hague Apostille / POA chain + diagnostic-doc language + sworn-translation cost bands) · `--connectivity` (broadband-checker URL + dominant ISPs + tariff bands + FTTH urban % + rural fallback + Starlink licence registry + strata trap) · `--remote` (foreign-buyer remote-execution: POA + RON + e-conveyancing + eIDAS QES + mortgage-bank residual wet-ink + Hawarden v ENS BEC trap; PT/BE fully-remote-property-deed; US RON 46 states + DC + PR; CA SB 696 effective 1 Jan 2030 backstop) · `--relocation` (foreign-buyer 90-day post-completion onboarding: pets + DL exchange + vehicle import + utility setup + healthcare gap; FAVN-rabies-titer 7-month flow for AU/NZ/JP/SG-Schedule-III/MY; CDC dog import 1 Aug 2024; AU EDR removed; LEZ landscape; foreign-buyer Catch-22)

**Decision-context (8)** — `--compare=<iso2,...>` `--retirement` `--digital-nomad` `--macro` `--demographics` `--schools` (foreign-buyer schools / education-access layer for working-age families with school-age dependents — international school landscape per major city + IB/British/American/French Lycée AEFE/German Schule + Nord Anglia/Cognita/GEMS/ISP/Globeducate/Inspired/QSI networks; annual fee bands USD 3-80k; waitlist horizons weeks-to-decade; local public school landscape + language-of-instruction; catchment-area / residency-priority rules driving 30-300% property-value premium in CN xuequ + US public-school-district + AU NSW selective + NZ Auckland Grammar zone + UK London catchment; UK 1 Jan 2025 20% VAT shock + AE KHDA/ADEK ratings + post-disaster crisis disruption) `--esg` `--exit`

### Cross-cutting layers (4)

`--integrity` (4 data-honesty checks) · `--journey=<type>` (7 templates: pre-offer / post-offer / foreign-buyer / investor / renovation / gite-bnb / inheritance) · `--type=<kind>` (6 specialised templates: off-plan / auction / probate / plot-only / heritage / apartment-vs-house — additional flags `mixed`, `agricultural`, `coastal`, `commercial` are recognised by the dispatcher but currently render only standard sections) · `--update` (maintenance mode with auto-downgrade rule)

### Tooling (9 docs)

TCO calculator · mortgage calculator · test fixtures · listing-diff watcher · comparable-transactions DB · auto-validate cron · price-index feeds · listing aggregators · photo OCR

## Country support — 103 fully populated

<!-- AUTOGEN:country-matrix:start -->
**Europe core (24)** — 🇫🇷 fr · 🇮🇹 it · 🇨🇿 cz · 🇸🇰 sk · 🇩🇪 de · 🇦🇹 at · 🇨🇭 ch · 🇪🇸 es · 🇵🇹 pt · 🇸🇪 se · 🇫🇮 fi · 🇳🇴 no · 🇬🇧 uk · 🇳🇱 nl · 🇧🇪 be · 🇩🇰 dk · 🇮🇸 is · 🇸🇮 si · 🇮🇪 ie · 🇬🇷 gr · 🇵🇱 pl · 🇪🇪 ee · 🇭🇷 hr · 🇭🇺 hu

**Anglo non-EU (4)** — 🇨🇦 ca · 🇦🇺 au · 🇳🇿 nz · 🇺🇸 us

**Latin America (11)** — 🇲🇽 mx · 🇧🇷 br · 🇦🇷 ar · 🇨🇷 cr · 🇵🇦 pa · 🇨🇴 co · 🇺🇾 uy · 🇨🇱 cl · 🇵🇪 pe · 🇪🇨 ec · 🇵🇾 py

**Caribbean (5)** — 🇧🇸 bs · 🇩🇴 do · 🇯🇲 jm · 🇧🇧 bb · 🇧🇿 bz

**Western Balkans (5)** — 🇷🇸 rs · 🇲🇪 me · 🇧🇦 ba · 🇲🇰 mk · 🇦🇱 al

**EU completion (7)** — 🇱🇹 lt · 🇱🇻 lv · 🇷🇴 ro · 🇧🇬 bg · 🇱🇺 lu · 🇨🇾 cy · 🇲🇹 mt

**Türkiye & Middle East (10)** — 🇹🇷 tr · 🇦🇪 ae · 🇮🇱 il · 🇶🇦 qa · 🇸🇦 sa · 🇯🇴 jo · 🇴🇲 om · 🇧🇭 bh · 🇰🇼 kw · 🇱🇧 lb

**Asia-Pacific (13)** — 🇯🇵 jp · 🇰🇷 kr · 🇹🇼 tw · 🇭🇰 hk · 🇲🇴 mo · 🇸🇬 sg · 🇹🇭 th · 🇲🇾 my · 🇮🇩 id · 🇻🇳 vn · 🇵🇭 ph · 🇨🇳 cn · 🇰🇭 kh

**South Asia (3)** — 🇮🇳 in · 🇱🇰 lk · 🇲🇻 mv

**Africa (11)** — 🇿🇦 za · 🇲🇦 ma · 🇪🇬 eg · 🇹🇳 tn · 🇳🇬 ng · 🇰🇪 ke · 🇲🇺 mu · 🇨🇻 cv · 🇸🇨 sc · 🇬🇭 gh · 🇷🇼 rw

**Caucasus & Eastern non-EU (4)** — 🇬🇪 ge · 🇲🇩 md · 🇦🇲 am · 🇦🇿 az

**Central Asia (2)** — 🇰🇿 kz · 🇺🇿 uz

**European Microstates (4)** — 🇱🇮 li · 🇦🇩 ad · 🇲🇨 mc · 🇸🇲 sm
<!-- AUTOGEN:country-matrix:end -->

## Install

Works as a plugin in both **[Claude Code](https://docs.claude.com/claude-code)** and **[Claude Cowork](https://www.anthropic.com/product/claude-cowork)**. The plugin format is identical — `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` + `skills/property-deep-dive/SKILL.md` — so the same skill bundle ships to both products. The install UX differs.

### Claude Code (slash commands)

```bash
# Add this repo as a plugin marketplace, then install the plugin
/plugin marketplace add github:soreavis/property-deep-dive
/plugin install property-deep-dive@property-deep-dive
```

The skill is now invocable via `/property-deep-dive`. The plugin manifest pins to a specific [CalVer](#versioning) release — you'll get updates only when a new version is published, not on every commit.

### Claude Cowork (in-app)

Cowork installs plugins from its own in-app plugin browser. Per [Anthropic's launch post](https://claude.com/blog/cowork-plugins) (2026-01-30): _"Easily install these directly from Cowork, browse the full collection on our website, or upload your own plugin."_

To install this third-party plugin, follow Cowork's "upload your own plugin" path with the GitHub URL `github:soreavis/property-deep-dive`. The exact UI steps may evolve — defer to the [linked blog post](https://claude.com/blog/cowork-plugins) and [Anthropic's curated plugin repo](https://github.com/anthropics/knowledge-work-plugins) for the current flow.

> **Cowork install scope (as of 2026-04)**: plugins save **locally per user**, not workspace-wide. Each teammate installs their own copy. Anthropic notes _"better support for org-wide sharing and management … coming in the weeks ahead"_ — this README will be updated when that lands.

### Manual symlink (for skill development / contributing — Claude Code only)

If you want to hack on the skill locally, clone the repo and symlink **the skill subdirectory** (not the whole repo) into Claude Code's skills directory:

```bash
git clone https://github.com/soreavis/property-deep-dive ~/code/property-deep-dive

# Symlink the skill subdirectory — Claude Code expects SKILL.md at the symlink's root
ln -s ~/code/property-deep-dive/skills/property-deep-dive ~/.claude/skills/property-deep-dive
ls -la ~/.claude/skills/property-deep-dive
```

The skill is now invocable via `/property-deep-dive` in Claude Code, with edits picked up immediately. SKILL.md, `shared/`, and `countries/` all live under `skills/property-deep-dive/`, so the skill is fully self-contained — every plugin host ships the entire payload from a single folder.

Cowork has no `~/.claude/skills/` equivalent; for Cowork local development use the "upload your own plugin" path described above.

## Try asking…

Paste any of these into Claude Code or Claude Cowork after installing:

```bash
# Visa + retirement options for a Spanish address
/property-deep-dive Calle Mayor 5, 28013 Madrid --visa --retirement

# Integrity scan + pre-offer brief from a UK listing URL
/property-deep-dive https://www.rightmove.co.uk/properties/<id> --integrity --journey=pre-offer

# Three-country side-by-side for retirees
/property-deep-dive --compare=fr,it,pt --retirement

# Greek heritage property for a foreign buyer
/property-deep-dive Athens 10556 --type=heritage --journey=foreign-buyer

# Maintenance — refresh URL liveness for France's playbook
/property-deep-dive --update --validate-only --country=fr
```

See [Usage](#usage) below for the full flag reference and more examples.

## Usage

```
/property-deep-dive 1 Rue Principale, 86430 Adriers, France --all
→ detects FR by postcode, runs all 31 default sections (`--cross-border` is opt-in), prints to terminal

/property-deep-dive --country=de Friedrichstraße 100, 10117 Berlin --tax --risks --save
→ Germany, tax + risks only, save to _local/reports/

/property-deep-dive https://www.rightmove.co.uk/properties/<id> --integrity --journey=pre-offer
→ detects UK from URL, integrity scan + pre-offer brief

/property-deep-dive Calle Mayor 5, 28013 Madrid --retirement --visa
→ retiree-specific filter for Spain

/property-deep-dive Athens 10556 --type=heritage --journey=foreign-buyer
→ Greek heritage property, foreign-buyer journey

/property-deep-dive --compare=fr,it,pt --retirement
→ side-by-side three-country comparison for retirees
```

See `skills/property-deep-dive/SKILL.md` for the full argument-hint and `skills/property-deep-dive/shared/sections.md` for the section contract.

## Token consumption

Running this skill in Claude Code (or Cowork) consumes tokens proportional to which sections you invoke and how big the country playbook is. The numbers below are **estimates with significant variance** — the actual cost in any one session depends on Claude's context-loading heuristics, on whether you also use other tools/sub-agents in the same session, and on which model you're on. They're calibrated against a 12-tokens-per-line conversion for table-heavy markdown and the actual line counts in this repo as of the most recent release.

### What gets loaded

| Component | Size | Loaded when |
|---|---:|---|
| `SKILL.md` (router + argument-hint + country matrix) | ~7,100 tokens | Always |
| `shared/preflight.md` (country detection) | ~2,100 tokens | Always |
| `shared/anti-hallucination.md` (7 mandatory checks) | ~3,500 tokens | Always |
| `shared/sections.md` (universal section contract) | ~8,100 tokens | Any section flag |
| `shared/output-template.md` | ~1,600 tokens | Any output |
| **Always-on subtotal** | **~16-22K tokens** | |

**Country playbook** (loaded once per address): **3,500 – 14,500 tokens**
- Smallest (RO, BG, LV, LU, LT — ~290-310 lines): ~3,500 tokens
- Median (~516 lines): ~6,200 tokens
- p90 (~1,090 lines): ~13,000 tokens
- Largest (PY, KE, SA, PE — ~1,150-1,210 lines): ~14,500 tokens

**Per-section flag — additional shared file** (loaded only when flag is invoked):

| Flag | Shared file size | Tokens |
|---|---:|---:|
| `--price` `--traffic` `--tax` `--rental` `--work` `--risks` `--mains` | (logic embedded in country playbook — no extra shared file) | 0 |
| `--amenities` | `shared/amenities-osm.md` (178 lines) | ~2,100 |
| `--climate` | `shared/climate-projections.md` (189 lines) | ~2,300 |
| `--insurance` | `shared/insurance.md` (195 lines) | ~2,300 |
| `--notary` | `shared/notary-process.md` (225 lines) | ~2,700 |
| `--language` | `shared/language.md` (227 lines) | ~2,700 |
| `--scams` | `shared/scams.md` (237 lines) | ~2,800 |
| `--currency` | `shared/currency.md` (303 lines) | ~3,600 |
| `--finance` | `shared/finance.md` (317 lines) | ~3,800 |
| `--connectivity` | `shared/connectivity.md` (335 lines) | ~4,000 |
| `--integrity` | `shared/integrity-checks.md` (352 lines) | ~4,200 |
| `--visa` | `shared/visa-programs.md` (356 lines) | ~4,300 |
| `--permits` | `shared/permits.md` (385 lines) | ~4,600 |
| `--agent` | `shared/agent.md` (412 lines) | ~4,900 |
| `--type=<kind>` | `shared/property-types.md` (585 lines) | ~7,000 |
| `--update` | `shared/updater.md` (588 lines) | ~7,100 |
| `--journey=<type>` | `shared/journeys.md` (589 lines) | ~7,100 |
| `--compare=<iso2,...>` | `shared/compare.md` (741 lines) | ~8,900 + extra playbooks |
| `--retirement` | `shared/retirement.md` (758 lines) | ~9,100 |
| `--crime` | `shared/crime-sources.md` (901 lines) | ~10,800 |
| `--exit` | `shared/exit.md` (100-line index) + region file (43-143 lines, loaded on demand) | ~1,200 + ~600-1,700 per region |

### Common invocation patterns

Realistic per-invocation totals on **Claude Sonnet 4.6** (default in Claude Code) at $3/MTok input + $15/MTok output. Multiply by 5× for **Opus 4.6** ($15/$75) or divide by 3× for **Haiku 4.5** ($1/$5).

| Pattern | Example | Input tokens | Output tokens | Cost (Sonnet) | Cost (Opus) |
|---|---|---:|---:|---:|---:|
| **Single section** (no shared file) | `--country=fr --tax` | ~21K | ~500 | **$0.07** | $0.35 |
| **Single section** (with shared file) | `--country=es --visa` | ~24K | ~600 | **$0.08** | $0.40 |
| **Three flags** | `--country=de --tax --rental --visa` | ~29K | ~2K | **$0.12** | $0.59 |
| **Address + listing URL** | `<address> --integrity --journey=pre-offer` | ~37K | ~3K | **$0.16** | $0.78 |
| **Full audit** | `<address> --all` | ~70-90K | ~6-10K | **$0.30-0.42** | $1.50-2.10 |
| **Heritage / specialised type** | `<address> --type=heritage --journey=foreign-buyer` | ~36K | ~3K | **$0.15** | $0.77 |
| **Three-country compare** | `--compare=fr,it,pt --retirement` | ~58K | ~4K | **$0.23** | $1.17 |
| **Save full audit to file** | `<address> --all --save` | ~70-90K | ~10-15K | **$0.36-0.49** | $1.80-2.50 |
| **Watch a listing (initial)** | `--watch <url>` | ~15K | ~500 | **$0.05** | $0.25 |
| **`--update --validate-only` (1 country)** | URL liveness, no re-research | ~25K | ~1K | **$0.09** | $0.43 |
| **`--update=<iso2>` (1 country full refresh)** | re-research + URL replace | ~150-200K | ~10-15K | **$0.60-0.83** | $3.00-4.13 |
| **`--update --tier=A` (15 countries)** | quarterly cycle | ~1.5-3M | ~150-300K | **$6.75-13.50** | $33.75-67.50 |

**Notes on the high end**

- `--update` modes invoke WebFetch (and sometimes parallel sub-agents) per country. The token spend is dominated by HTTP responses being read into context — typically ~30 URLs per playbook × 1.5-5K tokens per fetched page.
- `--all` may not load all 16 section-shared files simultaneously — Claude Code reads them on demand as each section renders, so the practical cost is often lower than the worst-case estimate. The range above accounts for this.
- The `--update --tier=*` figures assume a single-shot run. In practice, you'd typically run `--diff` first, review, then apply — that doubles input but skips half the output.

### What changes the cost

- **Country size**: PY/KE/SA/PE/KW playbooks are ~4× larger than RO/BG/LV/LU. A `--all` audit on PE costs ~50% more than on RO purely from playbook size.
- **WebFetch usage**: any flag that pulls live data (`--integrity` listing URL parse, `--update --refresh-only`, `--watch`) adds 1.5-5K tokens per URL fetched. Free-form addresses without a listing URL skip this entirely.
- **`--save` writes a full report** to `_local/reports/`, which doubles output tokens vs terminal-only render.
- **Sub-agent dispatch**: some maintenance flows (the regulatory-watch auto-promotion logic, parallel country research during batch refresh) spawn sub-agents. Each sub-agent has its own context window. Reported costs above are aggregated across the parent + sub-agents.

### How to measure your own usage

Claude Code shows per-session token counts via `/usage`. Track a few invocations to calibrate against your typical addresses + flag combinations — your real usage may be ±30% from the table above depending on how Claude routes the request.

For batch / CI / scheduled runs, the GitHub Actions workflows in `.github/workflows/` (url-liveness, health-report, tier-refresh) **do not consume Claude tokens** — they're plain bash + Python doing local file analysis and HTTP HEAD checks. Token spend only kicks in when a human invokes `/property-deep-dive` interactively to act on what those workflows surface.

## Anti-hallucination + regulatory watch

This skill drives major financial decisions, so it's built around the contract that **every claim is either sourced, computed transparently, or labelled as uncertain**. Three layers enforce this:

1. **Anti-hallucination guard** (`skills/property-deep-dive/shared/anti-hallucination.md`) — 7 mandatory pre-output checks, source-tier ranking, forbidden-phrasing list, calibrated hedging
2. **Regulatory watch** (`skills/property-deep-dive/shared/regulatory-watch.md`) — single date-stamped registry tracking ENDED programs (golden visas, MEIN, NHR), recently enacted reforms (last 24 months), EU directive transposition deadlines, watchlist
3. **Auto-downgrade rule** (`skills/property-deep-dive/shared/updater.md` § Auto-downgrade) — confidence labels decay over time without re-verification (HIGH → MEDIUM at 6 months, LOW at 12 months, STALE at 18 months); regulatory-watch entries can force STALE regardless of age

Together: a 14-month-old playbook never silently displays "Confidence: HIGH", and a tax reform logged in regulatory-watch.md flags every affected playbook section until it's re-stamped.

## Maintenance

The skill ships with a maintenance mode (`--update`) and tiered refresh GitHub Actions:

```
/property-deep-dive --update                       # full re-research + URL replace (all 103)
/property-deep-dive --update --validate-only       # URL liveness only (weekly)
/property-deep-dive --update --refresh-only        # data refresh, no URL check
/property-deep-dive --update --tier=A              # 16 high-velocity markets (quarterly)
/property-deep-dive --update --tier=B              # 38 mid-volume markets (semi-annual)
/property-deep-dive --update --tier=C              # 49 stable/frontier markets (annual)
/property-deep-dive --update --tier=A --include=ge # force-include a non-canonical country
/property-deep-dive --update --tier=A --exclude=fr # skip a canonical Tier-A country this cycle
/property-deep-dive --health-report                # decay matrix per country/section (monthly)
```

Tier membership lives in `config/_tiers.json`. See `skills/property-deep-dive/shared/updater.md` § Refresh tiers for full semantics including auto-promotion via `regulatory-watch.md`.

The GitHub Actions in `.github/workflows/` automate the read-only parts:

| Workflow | Cadence | What it does |
|---|---|---|
| `url-liveness.yml` | **paused** (manual `workflow_dispatch` only) | curl HEAD on every URL in every Markdown file in the repo; opens issue if score <85%. Schedule disabled 2026-05-08 — serial bash checker times out at 90 min after Tier-1+2 country sprint pushed URL set past the bash-loop budget; awaiting Python rewrite (aiohttp + per-host semaphore + Retry-After + result cache) |
| `health-report.yml` | monthly | parses `Last verified` dates, renders decay matrix with cadence-tier column, posts to pinned issue |
| `tier-a-refresh.yml` | quarterly | opens tracking issue listing the 16 Tier-A countries due for refresh |
| `tier-b-refresh.yml` | semi-annual | opens tracking issue listing the 38 Tier-B countries due for refresh |
| `tier-c-refresh.yml` | annual | opens tracking issue listing the 49 Tier-C countries due for refresh |
| `feed-watcher.yml` | every 6h | EU Official Journal + ECJ press RSS → opens issue when property-relevant directives land |

These are **detection-only**; the fix step (re-research, URL replacement, regulatory-watch entry) still requires human + Claude in the loop.

## Architecture

```
property-deep-dive/
├── README.md
├── LICENSE                           # MIT
├── DISCLAIMER.md                     # decision-support, not legal/tax/financial advice
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md                # Contributor Covenant 2.1
├── SECURITY.md                       # scope + vulnerability reporting
├── CHANGELOG.md                      # CalVer-shaped, per release
├── CLAUDE.md                         # repo-specific notes for Claude Code sessions
├── config/
│   ├── _regions.json                 # docs-build input — country region grouping
│   ├── _tiers.json                   # refresh-cadence tier membership (A 90d / B 180d / C 365d)
│   └── _visa-programs.json           # source of truth for --visa (192 records, 13 regions; shared/visa-programs.md auto-renders from this)
├── .editorconfig                     # cross-editor consistency
├── .markdownlint.json                # markdown lint rules used by pr-validate
├── .gitignore
├── .claude-plugin/
│   ├── plugin.json                   # plugin manifest (CalVer version)
│   └── marketplace.json              # marketplace stub
├── .github/
│   ├── CODEOWNERS
│   ├── dependabot.yml                # monthly action-version updates
│   ├── labels.yml                    # repository labels managed as code
│   ├── labeler.yml                   # path → label mapping for auto-labeler
│   ├── pull_request_template.md
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml                # disables blank issues, links to docs
│   │   ├── factual-correction.yml    # primary contribution channel
│   │   ├── broken-url.yml
│   │   ├── new-country.yml
│   │   └── regulatory-watch.yml
│   └── workflows/  (28 in total — see CHANGELOG.md for the full set; selection below)
│       ├── pr-validate.yml              # markdownlint + forbidden-phrasings + Last verified + density + arg-hint drift
│       ├── source-tier-ratchet.yml      # advisory: primary-vs-aggregator URL ratio per changed playbook (sticky PR comment)
│       ├── link-check.yml               # lychee internal links (PR + weekly schedule)
│       ├── changelog-enforcer.yml       # require [Unreleased] entry unless skip-labelled
│       ├── changelog-on-merge.yml       # batches merged PRs into chore/changelog-digest, weekly Monday flip
│       ├── url-liveness.yml             # URL check (cron paused 2026-05-08; manual workflow_dispatch only — see Maintenance §)
│       ├── health-report.yml            # monthly decay matrix → pinned issue
│       ├── feed-watcher.yml             # 6-hourly EU/ECJ feed → opens issue when relevant
│       ├── transposition-alerts.yml     # EU directive transposition deadline tracker
│       ├── regulatory-watch-revisit.yml # surface regulatory-watch entries past their revisit_by
│       ├── confidence-audit.yml         # check Confidence label vs primary-source URL count per playbook
│       ├── doc-sync-check.yml           # PR check that scripts/sync-docs.py would not change anything
│       ├── tier-a-refresh.yml           # quarterly Tier-A tracking issue (uses _tier-refresh.yml)
│       ├── tier-b-refresh.yml           # semi-annual Tier-B tracking issue (uses _tier-refresh.yml)
│       ├── tier-c-refresh.yml           # annual Tier-C tracking issue (uses _tier-refresh.yml)
│       ├── _tier-refresh.yml            # reusable workflow (workflow_call) shared by tier-a/b/c
│       ├── visa-programs-audit.yml      # render-check + claim-audit on config/_visa-programs.json
│       ├── codeql.yml                   # GitHub CodeQL static analysis (Actions + Python)
│       ├── scorecard.yml                # OpenSSF Scorecard, weekly + on push to main
│       ├── labels-sync.yml              # syncs labels.yml on changes
│       ├── labeler.yml                  # path-based PR labels
│       ├── stale.yml                    # mark stale at 60d, close at 90d (with exemptions)
│       ├── dependabot-auto-merge.yml    # auto-merge patch + minor dep updates after CI green
│       ├── auto-merge-docs.yml          # auto-merge docs-only PRs after CI green
│       ├── auto-tag.yml                 # end-of-month auto-tag YYYY.0M.0 if main has changes since last tag
│       ├── release-notes.yml            # auto-classify on tag push, draft release body
│       ├── sign-release.yml             # sigstore keyless signing of release tarball
│       └── year-roll-reminder.yml       # December reminder to update year-stamped references
├── scripts/
│   ├── audit-confidence.py           # primary-source URL count vs declared Confidence per playbook
│   ├── audit-visa-programs.py        # lint country playbook claims against config/_visa-programs.json status
│   ├── pin-actions.sh                # idempotent SHA-pin third-party actions
│   ├── primary-source-allowlist.txt  # central banks + statistics agencies for confidence-audit allowlist
│   ├── regwatch_promotions.py        # parses regulatory-watch.md for Tier-1/2 entries → auto-promotion list
│   ├── render-visa-programs.py       # JSON → AUTOGEN block in shared/visa-programs.md (idempotent; --check / --diff)
│   └── sync-docs.py                  # auto-sync counts + AUTOGEN blocks across community markdown
└── skills/property-deep-dive/        # the skill payload (everything plugin hosts ship)
    ├── SKILL.md                      # master router (~590 lines)
    ├── shared/                       # 48 top-level universal layer files (~17,500 lines)
    │   │                             #   + shared/exit/ subdirectory (14 region files, ~1,000 lines, loaded on demand)
    │   ├── preflight, sections, output-template, verdict-bands, anti-hallucination
    │   ├── 24 section implementations (universal logic + per-country tables/overlays)
    │   │   # core: amenities-osm, climate-projections, crime-sources
    │   │   # financial/process: finance, currency, visa-programs, insurance, notary-process, home-tax
    │   │   # transaction/process: permits, agent, scams, language, connectivity
    │   │   # process: remote, relocation
    │   │   # decision-context: compare, retirement, digital-nomad, macro, demographics, schools, esg, exit (+ exit/ subdir)
    │   │   # cross-cutting: integrity-checks, journeys, property-types
    │   ├── 6 sub-section extensions  # mains-reliability, finance-banking, notary-forced-heirship, risks-build-quality, digital-nomad-healthcare, rental-yield-delta
    │   ├── regulatory-watch.md       # single source of truth for reform tracking
    │   ├── updater.md                # maintenance mode + auto-downgrade rule
    │   └── 9 tooling docs            # tco/mortgage calculators, fixtures, diff-watcher, comparable-transactions, auto-validate, price-index-feeds, listing-aggregators, photo-ocr
    └── countries/                    # 103 country playbooks (~63,200 lines)
        └── <iso2>/playbook.md        # see Country support § above for the full ISO2 list
```

**Skill content** (under `skills/property-deep-dive/`): 166 markdown files, ~83,500 lines (SKILL.md + 48 top-level shared/ + 14 shared/exit/ region files + 103 country playbooks).
**Repo total**: 190 markdown files, ~88,600 lines (skill content + community / governance files + CHANGELOG) · 36 YAML / JSON config files (28 workflows + 5 issue forms + dependabot + labels + labeler).

## Contributing

Factual corrections, URL fixes, and section extensions are the most valuable contributions. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the bar (~400-500 lines per country, primary government sources, anti-hallucination contract).

All 103 in-scope countries are populated as of 2026-05-08 (Tier-1 + Tier-2 batches: PRs [#111](https://github.com/soreavis/property-deep-dive/pull/111) + [#113](https://github.com/soreavis/property-deep-dive/pull/113)). The country backlog is now schema-blocked rather than country-blocked — see [`ROADMAP.md`](./ROADMAP.md):

- **Crown Dependencies** (🇯🇪 je · 🇬🇬 gg · 🇮🇲 im · 🇬🇮 gi) — need a "territory classifier" PR first to handle non-sovereign jurisdictions cleanly
- **Danish territories** (🇫🇴 fo · 🇬🇱 gl) — same blocker
- **FR overseas + NL Caribbean** — deferred pending demand signal

In the meantime, the most valuable contributions are:

- **Factual corrections** — wrong tax rate, fee threshold, or "ENDED programme listed as active" (use the [factual-correction issue template](https://github.com/soreavis/property-deep-dive/issues/new?template=factual-correction.yml))
- **Broken URL replacements** — particularly when a primary government portal moves
- **Regulatory-watch entries** — recent reform / EU directive transposition / ENDED programme that supersedes a Tier-1 source
- **Section extensions** — Reddit gap-analysis 2026-05-08 backlog **fully exhausted**: `--home-tax` (#127), `--remote` (#128), `--relocation` (#129) shipped 2026-05-09; `--mains` utilities-reliability extension (#134) shipped 2026-05-09; 4-extension wave 2026-05-10 — `--finance` banking-access (#137), `--notary` forced-heirship (#138), `--risks` build-quality + off-plan (#139), `--digital-nomad` working-age healthcare carve-out (#140); `--schools` NEW section #31 (#141) shipped 2026-05-10; `--rental` yield-delta + neighborhood STR-zoning (#148, 6th sub-section extension) shipped 2026-05-11 combining the original 2026-05-08 STR-moratorium TODO with the 2026-05-10 Tier-2 yield-delta enrichment. 6-section wave shipped 2026-05-15 — Reddit gap-analysis #3 Tier-1 (`--property-management` #153, `--renovation` #154, `--surveyor` #155) plus Reddit gap-analysis #4 Tier-1 (`--inherited-noncompliance` #156, `--squatter`, `--latent-defect`). **Current backlog** (held for a later wave): 4 Tier-2 enrichments — `--scams` post-completion, `--finance` cross-border mortgage broker, `--integrity` buyers-remorse alerts, `--journey=foreign-buyer` sell-vs-rent — plus Reddit gap-analysis #4 Tier-2 fold-in candidates. See [`ROADMAP.md`](./ROADMAP.md) § Coverage extensions for the full list.

## Versioning

This repo uses **CalVer** (`YYYY.0M.MICRO`), not SemVer. Each tag encodes the release month, with a per-month patch counter:

| Component | Meaning |
|---|---|
| `YYYY` | Four-digit year (`2026`) |
| `0M` | Zero-padded month (`04` for April) |
| `MICRO` | In-month patch counter — `0` for the monthly cycle release; `1+` for factual corrections, URL fixes, regulatory-watch entries that landed mid-month |

**Why CalVer instead of SemVer**: this is a content repo, not an API. The "version" tracks how recently the _content_ was reviewed against primary sources, not API stability. Monthly grain aligns with how regulations actually drop — Finance Acts at fiscal year, ECJ rulings, EU Official Journal monthly L-series. The 30-day Tier-1 revisit cadence in `skills/property-deep-dive/shared/regulatory-watch.md` matches the same cadence.

**Tag triggers**:
- `YYYY.0M.0` (monthly) — automated; tags the end of each month if any change landed on `main` since the previous tag
- `YYYY.0M.1`, `.2`, … — manual; for material factual corrections / URL fixes / regulatory-watch entries that land mid-month
- **Not tagged**: typo fixes, formatting, internal refactors, README polish without skill content change

**Breaking changes** (flag rename, output schema change, removed section) are flagged under `### Breaking` in [CHANGELOG.md](./CHANGELOG.md) for the release in which they ship.

## Credits

- **Maintained by**: [Julian Soreavis](https://github.com/soreavis)
- **Built with**: [Claude Code](https://claude.com/claude-code)

Copyright © 2026 Julian Soreavis. Licensed under [MIT](./LICENSE). See [DISCLAIMER.md](./DISCLAIMER.md) for the no-warranty / verification-required clauses specific to property due diligence.

Factual contributions and country playbooks from the community are credited in [CHANGELOG.md](./CHANGELOG.md) under the release in which they ship; the `release-notes.yml` workflow attributes each merged PR's author when it builds the GitHub release body.

## License

[MIT](./LICENSE) — see also [DISCLAIMER.md](./DISCLAIMER.md) for the no-warranty / verification-required clauses specific to property due diligence.

## Acknowledgments

Built as a Claude Code skill. The architecture (master router + per-country playbooks + universal shared layer + anti-hallucination guard + regulatory watch) is reusable for any other domain that combines per-jurisdiction local rules with cross-cutting decision support.
