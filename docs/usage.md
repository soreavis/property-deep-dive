# Usage

`property-deep-dive` is invoked via slash command in Claude Code:

```
/property-deep-dive <address> [flags]
```

The full argument-hint and section catalog live in [SKILL.md](../skills/property-deep-dive/SKILL.md). This page shows seven worked examples covering common decision contexts.

## 1. Full audit on a French address

```
/property-deep-dive 1 Rue Principale, 86430 Adriers, France --all
```

The skill detects France by postcode, loads `skills/property-deep-dive/countries/fr/playbook.md`, runs all 31 default sections (price · traffic · tax · rental · work · risks · mains · crime · amenities · climate · finance · currency · visa · insurance · notary · permits · agent · scams · language · connectivity · home-tax · remote · relocation · compare · retirement · digital-nomad · macro · demographics · schools · esg · exit), and prints to terminal. `--cross-border` is the 32nd section — opt-in for buyers whose move triggers dual-residency / POEM / PE exposure (intra-EU movers, owners of third-country companies, retirees keeping origin-country residence ties).

## 2. Targeted facets, save report to file

```
/property-deep-dive --country=de Friedrichstraße 100, 10117 Berlin --tax --risks --save
```

Germany, tax + risks only. The `--save` flag writes the report to `_local/reports/property-de-berlin-tax-risks-<date>.md`.

## 3. From a listing URL

```
/property-deep-dive https://www.rightmove.co.uk/properties/<id> --integrity --journey=pre-offer
```

Detects the UK from the listing URL. `--integrity` runs the four data-honesty checks (dispute-resolver, photo OCR, listing-vs-cadastre cross-check, red-flag scanner). `--journey=pre-offer` reshapes the output as a pre-offer brief.

## 4. Retiree-specific filter

```
/property-deep-dive Calle Mayor 5, 28013 Madrid --retirement --visa
```

Pulls retirement-relevant tax + visa sections for Spain — including pension-tax regime, IFICI / NHR-equivalent eligibility, and Spain's residency pathways.

## 5. Heritage / foreign-buyer overlay

```
/property-deep-dive Athens 10556 --type=heritage --journey=foreign-buyer
```

Greek heritage / listed-property template overlaid on the foreign-buyer journey — covers AIP-equivalent permit needs, monument-classified restoration constraints, and conservation-grant eligibility.

## 6. Side-by-side three-country comparison

```
/property-deep-dive --compare=fr,it,pt --retirement
```

Renders a comparison matrix across France / Italy / Portugal for retiree-relevant facets (pension tax, healthcare access, residency thresholds, climate, cost-of-living).

## 7. Foreign-buyer family with school-age kids

```
/property-deep-dive Singapore 049145 --schools --digital-nomad --home-tax --journey=foreign-buyer
```

Singapore address with the working-age-family combo. `--schools` returns the international school landscape (SAS / UWC / Tanglin / Chatsworth fee bands USD 17-43k + waitlist horizons + Primary One Registration with parents-alumni priority + DSA pathway + catchment-area effects on property premium). `--digital-nomad` auto-loads the working-age healthcare carve-out sub-section (SG EP minimum salary thresholds raised 1 Jan 2025 / 1 Jan 2026 + private-insurance acceptance + tax-residency interaction with Singapore's territorial regime). `--home-tax` returns the buyer-nationality tax overlay (US FATCA Form 8938 + FBAR + § 988 *Quijano* phantom-currency-gain trap; UK FA 2025 FIG regime + 10/20 LTR IHT test; CA T1135 + § 128.1; etc. — indexed by *buyer's* tax residence). `--journey=foreign-buyer` reshapes the output as the foreign-buyer brief (visa pathway → financing → permits → completion → 90-day relocation).

## Argument quick reference

### Section flags

39 user-invocable section flags grouped by domain, plus 4 cross-cutting layers.

| Group | Flags |
|---|---|
| **Core (10)** | `--price` `--traffic` `--tax` `--rental` `--work=<profession>` `--risks` `--mains` `--crime` `--amenities` `--climate` |
| **Financial / process (7)** | `--finance` `--currency` `--visa` `--insurance` `--notary` `--home-tax` `--cross-border` |
| **Regulatory (1)** | `--permits` |
| **Transaction (3)** | `--agent` `--scams` `--title-monitoring` |
| **Process (4)** | `--language` `--connectivity` `--remote` `--relocation` |
| **Decision-context (8)** | `--compare=<iso2,...>` `--retirement` `--digital-nomad` `--macro` `--demographics` `--schools` `--esg` `--exit` |
| **Cross-cutting layers (4)** | `--integrity` `--journey=<type>` `--type=<kind>` `--update` |
| **Tooling (3)** | `--tco` `--mortgage` `--watch <url>` |

**Sub-section extensions** (11 — auto-loaded alongside the parent flag, no separate invocation): `shared/mains-reliability.md` loads with `--mains` (grid + SAIDI/SAIFI + outage band + load-shedding regime); `shared/finance-banking.md` loads with `--finance` (tax-ID prerequisite chain + FATCA acceptance bucket per country + expat-banking arms); `shared/notary-forced-heirship.md` loads with `--notary` (civil-law forced shares vs common-law testamentary freedom vs Sharia, Brussels IV); `shared/risks-build-quality.md` loads with `--risks` (statutory new-build warranty regimes + off-plan deposit-protection mechanisms — pairs strongly with `--type=off-plan`); `shared/digital-nomad-healthcare.md` loads with `--digital-nomad` (working-age 25-65 healthcare access for DN-visa holders — companion to `--retirement` for retirement-age 65+); `shared/rental-yield-delta.md` loads with `--rental` (gross-vs-net yield delta + neighborhood STR-zoning / moratorium overlay); `shared/scams-postcompletion.md` loads with `--scams` (post-completion fraud register — title hijack, utility/identity, equity-stripping); `shared/journey-sellrent.md` loads with `--journey=foreign-buyer` (sell-vs-rent decision overlay); `shared/integrity-remorse.md` loads with `--integrity` (buyer's-remorse / cooling-off cross-check); `shared/finance-crossborder.md` loads with `--finance` (cross-border mortgage / SPV / crypto-funding paths); `shared/exit-seller-withholding.md` loads with `--exit` (non-resident-seller withholding / tax-clearance completion-gate). The gap-#5 / gap-#4 fold-ins (strata-governance, right-of-way, leasehold, connect-from-scratch utilities, flood-insurability carve-out, JP universal 国土法/農地法 content) are in-file sub-blocks within existing section files (`property-management.md`, `property-types.md`, `insurance.md`, `countries/jp/playbook.md`), not separate auto-loaded extensions.

### Output flags

| Flag | Effect |
|---|---|
| `--all` | Run every section |
| `--save[=<path>]` | Save report to file (defaults to `_local/reports/`) |
| `--quick` / `--deep` | Trade speed for thoroughness |
| `--country=<iso2>` | Override country detection |
| `--listing=<url>` | Pull address from a listing URL |
| `--override-confidence=<HIGH|MEDIUM|LOW>` | Manual confidence override |

### Maintenance flags (skill author / CI)

| Flag | Effect |
|---|---|
| `--update` | Full re-research + URL replace for a country (or all populated) |
| `--update=<iso2>` | Re-research one specific country |
| `--update --tier=A\|B\|C` | Refresh by cadence tier (A: 16 quarterly · B: 38 semi-annual · C: 49 annual). Tier membership in `config/_tiers.json` |
| `--update --tier=A --include=<iso2>` | Force-include a non-canonical country in a tier run |
| `--update --tier=A --exclude=<iso2>` | Skip a canonical tier country for one cycle |
| `--update --validate-only` | URL liveness check only (no re-research) |
| `--update --refresh-only` | Re-research data without URL check |
| `--update --add=<iso2>` | Populate a scaffold country fully |
| `--update --diff` | Preview planned changes without writing |
| `--update --interactive` | Confirm each playbook before writing |
| `--health-report` | Decay matrix per country / section + cadence early-warning |

See [SKILL.md](../skills/property-deep-dive/SKILL.md) for the complete argument-hint string.

## Country support

103 fully-populated country playbooks. Browse [`skills/property-deep-dive/countries/`](../skills/property-deep-dive/countries/) or see the [country matrix in README](../README.md#country-support--103-fully-populated).
