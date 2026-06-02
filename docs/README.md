# Documentation index

Full documentation for **property-deep-dive**. Most content lives at the repo root for discoverability — this directory holds focused entry points for installation, usage, and safe operation.

## Getting started

- **[Install](./install.md)** — plugin install for Claude Code (slash commands) or Claude Cowork (in-app), plus manual symlink for development
- **[Usage](./usage.md)** — six worked invocation examples of `/property-deep-dive` plus full flag reference
- **[Security and safe usage](./security.md)** — what must be verified before signing any contract; reporting errors

## Project documentation (at repo root)

| File | What it covers |
|---|---|
| [README.md](../README.md) | Feature overview, country matrix, badges, architecture diagram |
| [DISCLAIMER.md](../DISCLAIMER.md) | Decision-support scope; **not** legal/tax/financial advice |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Contributor Covenant 2.1 + project-specific norms |
| [SECURITY.md](../SECURITY.md) | Vulnerability scope, public vs private channels, disclosure timeline |
| [CHANGELOG.md](../CHANGELOG.md) | CalVer scheme details + per-release notes |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | PR checklist, anti-hallucination contract, source-tier ranking |
| [CLAUDE.md](../CLAUDE.md) | Repo-specific working notes for Claude Code sessions |
| [ROADMAP.md](../ROADMAP.md) | Country-addition backlog (Tier-1 + Tier-2 candidates), Crown Dependencies deferred, skip-list with reasoning |

## Skill internals

| File | Role |
|---|---|
| [SKILL.md](../skills/property-deep-dive/SKILL.md) | Master router — argument-hint, section catalog, country matrix |
| [shared/anti-hallucination.md](../skills/property-deep-dive/shared/anti-hallucination.md) | The 8 mandatory pre-output checks the skill enforces |
| [shared/regulatory-watch.md](../skills/property-deep-dive/shared/regulatory-watch.md) | Date-stamped tracker of ENDED programmes + recent reforms + transposition deadlines |
| [shared/updater.md](../skills/property-deep-dive/shared/updater.md) | Maintenance mode (`--update`), refresh tiers (A/B/C), auto-downgrade rule, scheduling |
| [shared/sections.md](../skills/property-deep-dive/shared/sections.md) | Universal section contract |
| [shared/output-template.md](../skills/property-deep-dive/shared/output-template.md) | Canonical section formatting |
| [shared/verdict-bands.md](../skills/property-deep-dive/shared/verdict-bands.md) | 🟢 🟡 🟠 🔴 severity contract |
| [config/_tiers.json](../config/_tiers.json) | Refresh-cadence tier membership (Tier-A 90d / B 180d / C 365d) — single source of truth |
| [config/_regions.json](../config/_regions.json) | Region-grouping for country matrix in README — single source of truth |
| [config/_visa-programs.json](../config/_visa-programs.json) | Visa / RBI / CBI / DNV / golden-visa registry (192 records, 13 regions) — source of truth for the `--visa` section; `shared/visa-programs.md` region tables auto-render via `scripts/render-visa-programs.py` |

## Country playbooks

121 fully-populated country playbooks live in [`skills/property-deep-dive/countries/<iso2>/playbook.md`](../skills/property-deep-dive/countries/) — open the directory to browse them.
