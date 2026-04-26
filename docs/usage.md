# Usage

`property-deep-dive` is invoked via slash command in Claude Code:

```
/property-deep-dive <address> [flags]
```

The full argument-hint and section catalog live in [SKILL.md](../SKILL.md). This page shows six worked examples covering common decision contexts.

## 1. Full audit on a French address

```
/property-deep-dive 1 Rue Principale, 86430 Adriers, France --all
```

The skill detects France by postcode, loads `countries/fr/playbook.md`, runs all 22 sections (price · traffic · tax · rental · work · risks · mains · crime · amenities · climate · finance · currency · visa · insurance · notary · compare · retirement · digital-nomad · macro · demographics · esg · exit), and prints to terminal.

## 2. Targeted facets, save report to file

```
/property-deep-dive --country=de Friedrichstraße 100, 10117 Berlin --tax --risks --save
```

Germany, tax + risks only. The `--save` flag writes the report to `_local/reports/property-de-berlin-tax-risks-<date>.md`.

## 3. From a listing URL

```
/property-deep-dive https://www.rightmove.co.uk/properties/142857 --integrity --journey=pre-offer
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
| `--update` | Re-research mode for a country |
| `--update --validate-only` | URL liveness only |
| `--health-report` | Decay matrix per country / section |

See [SKILL.md](../SKILL.md) for the complete argument-hint string.

## Country support

44 fully-populated country playbooks. Browse [`countries/`](../countries/) or see the [country matrix in README](../README.md#country-support).
