# Documentation index

Full documentation for **property-deep-dive**. Most content lives at the repo root for discoverability — this directory holds focused entry points for installation, usage, and safe operation.

## Getting started

- **[Install](./install.md)** — clone the repo and symlink into Claude Code's skills directory
- **[Usage](./usage.md)** — six worked invocation examples of `/property-deep-dive`
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

## Skill internals

| File | Role |
|---|---|
| [SKILL.md](../SKILL.md) | Master router — argument-hint, section catalog, country matrix |
| [shared/anti-hallucination.md](../shared/anti-hallucination.md) | The 7 mandatory pre-output checks the skill enforces |
| [shared/regulatory-watch.md](../shared/regulatory-watch.md) | Date-stamped tracker of ENDED programmes + recent reforms + transposition deadlines |
| [shared/sections.md](../shared/sections.md) | Universal section contract |
| [shared/output-template.md](../shared/output-template.md) | Canonical section formatting |
| [shared/verdict-bands.md](../shared/verdict-bands.md) | 🟢 🟡 🟠 🔴 severity contract |

## Country playbooks

44 fully-populated country playbooks live in [`countries/<iso2>/playbook.md`](../countries/) — open the directory to browse them.
