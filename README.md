# property-deep-dive

[![Release](https://img.shields.io/github/v/release/soreavis/property-deep-dive?label=release&sort=semver)](https://github.com/soreavis/property-deep-dive/releases)
[![License: MIT](https://img.shields.io/github/license/soreavis/property-deep-dive)](./LICENSE)
[![URL liveness](https://github.com/soreavis/property-deep-dive/actions/workflows/url-liveness.yml/badge.svg)](https://github.com/soreavis/property-deep-dive/actions/workflows/url-liveness.yml)
[![PR validate](https://github.com/soreavis/property-deep-dive/actions/workflows/pr-validate.yml/badge.svg)](https://github.com/soreavis/property-deep-dive/actions/workflows/pr-validate.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/soreavis/property-deep-dive/badge)](https://scorecard.dev/viewer/?uri=github.com/soreavis/property-deep-dive)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/12655/badge)](https://www.bestpractices.dev/projects/12655)

**Runs in [Claude Code](https://docs.claude.com/claude-code) and [Claude Cowork](https://www.anthropic.com/product/claude-cowork)** — same plugin format and same `/property-deep-dive` invocation in both. Install UX differs: Claude Code uses slash commands, Cowork uses its in-app plugin browser (see [Install](#install)).

**Pre-purchase property due diligence across 54 countries** — tax, risks, rental yield, visa, mortgage, and 17 other facets per address. Sourced from primary government data, every claim dated and confidence-labelled. **22 user-invocable sections**, **4 cross-cutting layers** (integrity / journey / type / update), and a regulatory-watch system that surfaces reforms before they invalidate the data.

> **Decision-support, not legal/tax/financial advice.** Property purchases are six- to seven-figure decisions; this skill helps you ask the right questions and surface risks early. See [DISCLAIMER.md](./DISCLAIMER.md) for full scope.

> **Stability**: production-ready content. Versioned with [CalVer](#versioning) — each tag encodes the release month (e.g. `2026.04.0`).

## What it does

Given an address — `1 Rue Principale, 86430 Adriers, France`, `https://www.rightmove.co.uk/properties/142857`, or coordinates — the skill:

1. Detects the country (postcode pattern, country name, or `--country=<iso2>` flag)
2. Loads the country's playbook from `skills/property-deep-dive/countries/<iso2>/playbook.md`
3. Runs the requested sections (or `--all`)
4. Applies the anti-hallucination guard
5. Outputs to terminal or saves a Markdown report

### Sections (22 user-invocable)

**Core (10)** — `--price` `--traffic` `--tax` `--rental` `--work=<profession>` `--risks` `--mains` `--crime` `--amenities` `--climate`

**Financial / process (5)** — `--finance` `--currency` `--visa` `--insurance` `--notary`

**Decision-context (7)** — `--compare=<iso2,...>` `--retirement` `--digital-nomad` `--macro` `--demographics` `--esg` `--exit`

### Cross-cutting layers (4)

`--integrity` (4 data-honesty checks) · `--journey=<type>` (7 templates: pre-offer / post-offer / foreign-buyer / investor / renovation / gite-bnb / inheritance) · `--type=<kind>` (6 specialised templates: off-plan / auction / probate / plot-only / heritage / apartment-vs-house — additional flags `mixed`, `agricultural`, `coastal`, `commercial` are recognised by the dispatcher but currently render only standard sections) · `--update` (maintenance mode with auto-downgrade rule)

### Tooling (9 docs)

TCO calculator · mortgage calculator · test fixtures · listing-diff watcher · comparable-transactions DB · auto-validate cron · price-index feeds · listing aggregators · photo OCR

## Country support — 79 fully populated

<!-- AUTOGEN:country-matrix:start -->
**Europe core (24)** — 🇫🇷 fr · 🇮🇹 it · 🇨🇿 cz · 🇸🇰 sk · 🇩🇪 de · 🇦🇹 at · 🇨🇭 ch · 🇪🇸 es · 🇵🇹 pt · 🇸🇪 se · 🇫🇮 fi · 🇳🇴 no · 🇬🇧 uk · 🇳🇱 nl · 🇧🇪 be · 🇩🇰 dk · 🇮🇸 is · 🇸🇮 si · 🇮🇪 ie · 🇬🇷 gr · 🇵🇱 pl · 🇪🇪 ee · 🇭🇷 hr · 🇭🇺 hu

**Anglo non-EU (4)** — 🇨🇦 ca · 🇦🇺 au · 🇳🇿 nz · 🇺🇸 us

**Latin America (12)** — 🇲🇽 mx · 🇧🇷 br · 🇦🇷 ar · 🇨🇷 cr · 🇵🇦 pa · 🇩🇴 do · 🇨🇴 co · 🇺🇾 uy · 🇨🇱 cl · 🇵🇪 pe · 🇪🇨 ec · 🇵🇾 py

**Western Balkans (5)** — 🇷🇸 rs · 🇲🇪 me · 🇧🇦 ba · 🇲🇰 mk · 🇦🇱 al

**EU completion (7)** — 🇱🇹 lt · 🇱🇻 lv · 🇷🇴 ro · 🇧🇬 bg · 🇱🇺 lu · 🇨🇾 cy · 🇲🇹 mt

**Türkiye & Middle East (5)** — 🇹🇷 tr · 🇦🇪 ae · 🇮🇱 il · 🇶🇦 qa · 🇸🇦 sa

**Asia-Pacific (11)** — 🇯🇵 jp · 🇰🇷 kr · 🇹🇼 tw · 🇭🇰 hk · 🇲🇴 mo · 🇸🇬 sg · 🇹🇭 th · 🇲🇾 my · 🇮🇩 id · 🇻🇳 vn · 🇵🇭 ph

**Africa (4)** — 🇿🇦 za · 🇲🇦 ma · 🇪🇬 eg · 🇹🇳 tn

**Caucasus & Eastern non-EU (4)** — 🇬🇪 ge · 🇲🇩 md · 🇦🇲 am · 🇦🇿 az

**European Microstates (3)** — 🇱🇮 li · 🇦🇩 ad · 🇲🇨 mc
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
/property-deep-dive https://www.rightmove.co.uk/properties/142857 --integrity --journey=pre-offer

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
→ detects FR by postcode, runs all 22 sections, prints to terminal

/property-deep-dive --country=de Friedrichstraße 100, 10117 Berlin --tax --risks --save
→ Germany, tax + risks only, save to _local/reports/

/property-deep-dive https://www.rightmove.co.uk/properties/142857 --integrity --journey=pre-offer
→ detects UK from URL, integrity scan + pre-offer brief

/property-deep-dive Calle Mayor 5, 28013 Madrid --retirement --visa
→ retiree-specific filter for Spain

/property-deep-dive Athens 10556 --type=heritage --journey=foreign-buyer
→ Greek heritage property, foreign-buyer journey

/property-deep-dive --compare=fr,it,pt --retirement
→ side-by-side three-country comparison for retirees
```

See `skills/property-deep-dive/SKILL.md` for the full argument-hint and `skills/property-deep-dive/shared/sections.md` for the section contract.

## Anti-hallucination + regulatory watch

This skill drives major financial decisions, so it's built around the contract that **every claim is either sourced, computed transparently, or labelled as uncertain**. Three layers enforce this:

1. **Anti-hallucination guard** (`skills/property-deep-dive/shared/anti-hallucination.md`) — 7 mandatory pre-output checks, source-tier ranking, forbidden-phrasing list, calibrated hedging
2. **Regulatory watch** (`skills/property-deep-dive/shared/regulatory-watch.md`) — single date-stamped registry tracking ENDED programs (golden visas, MEIN, NHR), recently enacted reforms (last 24 months), EU directive transposition deadlines, watchlist
3. **Auto-downgrade rule** (`skills/property-deep-dive/shared/updater.md` § Auto-downgrade) — confidence labels decay over time without re-verification (HIGH → MEDIUM at 6 months, LOW at 12 months, STALE at 18 months); regulatory-watch entries can force STALE regardless of age

Together: a 14-month-old playbook never silently displays "Confidence: HIGH", and a tax reform logged in regulatory-watch.md flags every affected playbook section until it's re-stamped.

## Maintenance

The skill ships with a maintenance mode (`--update`) and three GitHub Actions:

```
/property-deep-dive --update                       # full re-research + URL replace (annual)
/property-deep-dive --update --validate-only       # URL liveness only (weekly)
/property-deep-dive --update --refresh-only        # data refresh, no URL check (quarterly)
/property-deep-dive --health-report                # decay matrix per country/section (monthly)
```

The GitHub Actions in `.github/workflows/` automate the read-only parts:

| Workflow | Cadence | What it does |
|---|---|---|
| `url-liveness.yml` | weekly | curl HEAD on every URL in every Markdown file in the repo; opens issue if score <85% |
| `health-report.yml` | monthly | parses `Last verified` dates, renders decay matrix, posts to pinned issue |
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
├── _regions.json                     # docs-build input — country region grouping
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
│   └── workflows/  (22 in total — see CHANGELOG.md for the full set)
│       ├── pr-validate.yml           # markdownlint + forbidden-phrasings + Status footer + density + arg-hint drift
│       ├── source-tier-audit.yml     # advisory: primary-vs-aggregator URL ratio per changed playbook (sticky PR comment)
│       ├── link-check.yml            # lychee internal links (PR + weekly schedule)
│       ├── changelog-enforcer.yml    # require [Unreleased] entry unless skip-labelled
│       ├── url-liveness.yml          # weekly URL check, opens issue if score <85%
│       ├── test-fixtures-check.yml   # monthly check of skills/property-deep-dive/shared/test-fixtures.md listings
│       ├── health-report.yml         # monthly decay matrix → pinned issue
│       ├── feed-watcher.yml          # 6-hourly EU/ECJ feed → opens issue when relevant
│       ├── scorecard.yml             # OpenSSF Scorecard, weekly + on push to main
│       ├── labels-sync.yml           # syncs labels.yml on changes
│       ├── labeler.yml               # path-based PR labels
│       ├── pr-size.yml               # PR size/xs … size/xl labels
│       ├── welcome.yml               # first-PR / first-issue greeter
│       ├── stale.yml                 # mark stale at 60d, close at 90d (with exemptions)
│       ├── dependabot-auto-merge.yml # auto-merge patch + minor dep updates after CI green
│       ├── release-notes.yml         # auto-classify on tag push, draft release body
│       └── sign-release.yml          # sigstore keyless signing of release tarball
├── scripts/
│   └── pin-actions.sh                # idempotent SHA-pin third-party actions
└── skills/property-deep-dive/        # the skill payload (everything plugin hosts ship)
    ├── SKILL.md                      # master router (~470 lines)
    ├── shared/                       # 34 universal layer files (~11,600 lines)
    │   ├── preflight, sections, output-template, verdict-bands, anti-hallucination
    │   ├── 22 section implementations (universal logic + per-country overlays)
    │   ├── regulatory-watch.md       # single source of truth for reform tracking
    │   ├── updater.md                # maintenance mode + auto-downgrade rule
    │   └── 9 tooling docs
    └── countries/                    # 79 country playbooks (~43,200 lines)
        └── <iso2>/playbook.md        # FR / IT / CZ / SK / DE / AT / CH / ES / PT / SE / ... + US / TR / AE / JP / TH / DO / CO / UY / CL / ZA / GE / ID / MY / VN / PH / IL / MA / EG / SG / HK / KR / TW / LI / MO / AD / MC / MD / QA / SA / PE / EC / PY / AM / AZ / TN
```

**Skill content** (under `skills/property-deep-dive/`): 114 markdown files, ~55,300 lines (SKILL.md + 34 shared/ + 79 country playbooks).
**Repo total**: 126 markdown files, ~56,700 lines (skill content + community / governance files + CHANGELOG) · 30 YAML / JSON config files (22 workflows + 5 issue forms + dependabot + labels + labeler).

## Contributing

Factual corrections, URL fixes, and new country playbooks are the most valuable contributions. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the bar (~400-500 lines per country, primary government sources, anti-hallucination contract).

The country gaps that would be most valuable next:

- 🇱🇮 LI (only EEA non-EU missing)
- 🇸🇬 SG · 🇭🇰 HK · 🇰🇷 KR · 🇹🇼 TW · 🇮🇳 IN (Asia-Pacific extension)
- 🇮🇩 ID · 🇲🇾 MY · 🇻🇳 VN · 🇵🇭 PH (Southeast Asia)
- 🇵🇪 PE · 🇪🇨 EC · 🇵🇾 PY (LatAm tertiary)
- 🇲🇦 MA · 🇪🇬 EG · 🇹🇳 TN · 🇰🇪 KE · 🇳🇬 NG (Africa)
- 🇮🇱 IL · 🇸🇦 SA · 🇶🇦 QA (Middle East extension)
- 🇬🇪 GE · 🇦🇲 AM · 🇦🇿 AZ (Caucasus)

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
