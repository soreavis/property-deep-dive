# Usage

`property-deep-dive` is invoked via slash command in Claude Code:

```
/property-deep-dive <address> [flags]
```

The full argument-hint and section catalog live in [SKILL.md](../skills/property-deep-dive/SKILL.md). This page shows six worked examples covering common decision contexts.

## 1. Full audit on a French address

```
/property-deep-dive 1 Rue Principale, 86430 Adriers, France --all
```

The skill detects France by postcode, loads `skills/property-deep-dive/countries/fr/playbook.md`, runs all 26 sections (price · traffic · tax · rental · work · risks · mains · crime · amenities · climate · finance · currency · visa · insurance · notary · permits · agent · scams · language · compare · retirement · digital-nomad · macro · demographics · esg · exit), and prints to terminal.

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

## Argument quick reference

### Section flags

| Group | Flags |
|---|---|
| **Core (10)** | `--price` `--traffic` `--tax` `--rental` `--work=<profession>` `--risks` `--mains` `--crime` `--amenities` `--climate` |
| **Financial / process (5)** | `--finance` `--currency` `--visa` `--insurance` `--notary` |
| **Decision-context (7)** | `--compare=<iso2,...>` `--retirement` `--digital-nomad` `--macro` `--demographics` `--esg` `--exit` |
| **Cross-cutting layers (4)** | `--integrity` `--journey=<type>` `--type=<kind>` `--update` |

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
| `--update --tier=A\|B\|C` | Refresh by cadence tier (A: 15 quarterly · B: 30 semi-annual · C: 42 annual). Tier membership in `_tiers.json` |
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
