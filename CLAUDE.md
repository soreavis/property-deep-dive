# Working on `property-deep-dive`

Project-scoped instructions for any Claude Code session operating in this repo. For *what the skill does*, see [README.md](./README.md). For *how to contribute*, see [CONTRIBUTING.md](./CONTRIBUTING.md). This file is about *how to do the work itself*.

## Non-negotiable: the anti-hallucination contract

This skill drives six- to seven-figure property decisions. **Every claim must be one of**:

1. **Sourced** to a primary government / regulated entity (with link)
2. **Computed** transparently (inputs visible inline)
3. **Estimated** with `~` / `est.` / `≈` prefix and a calibration sentence

If a number can't satisfy any of those, write `data not publicly available — verify at <authoritative source>` rather than guessing.

The 8 mandatory pre-output checks are in [`shared/anti-hallucination.md`](./skills/property-deep-dive/shared/anti-hallucination.md). They are non-negotiable for any output the skill produces.

**Forbidden phrasings** (these phrases generate fabrication pressure):

> "approximately X" · "in the area of" · "typical for the region" · "as of recent data" · "industry average" · "experts say" · "studies show" · "should be around" · "is likely connected to"

Replacement table is in `skills/property-deep-dive/shared/anti-hallucination.md` under "Forbidden phrasings".

## Source ranking — never silently upgrade

```
Primary government       ✅ citable as fact
Primary regulated entity ✅ citable as fact
Secondary aggregator     ⚠️ quote but cross-check
Listing platform         ⚠️ seller-controlled, often outdated
Forum / Reddit / blog    🟡 anecdotal, never as basis for verdict
Model inference          🔴 must be labelled `est.` with inputs shown
```

When two same-tier sources disagree → output BOTH, explain the gap, name which one you used and why. When higher-tier contradicts lower-tier → higher tier wins; lower gets `(superseded)`.

## When editing country playbooks

- **Density target**: ~400-500 lines, FR/IT/CZ/SK as the canonical examples
- **Date-stamp every numeric fact**: `(<year> data, source <X>)`. If >12 months old, append `— rates/figures may have changed since`
- **Parcel vs commune**: never silently elevate commune-level data to parcel-level claims (see `skills/property-deep-dive/shared/anti-hallucination.md` § Address-vs-commune trap)
- **Listing claims**: tag with `(per listing — verify with cadastre / on visit)`
- **Status footer**: every playbook ends with `## Status` + `**Confidence**: HIGH/MEDIUM/LOW` + ideally `**Last verified**: YYYY-MM-DD`

## When a regulation changes

The flow is: **regulatory-watch.md FIRST, then playbook patch**.

1. Add a date-stamped entry to [`shared/regulatory-watch.md`](./skills/property-deep-dive/shared/regulatory-watch.md) with: country, topic, effective date, source URL, verified date, revisit cadence, impact tier (1-4), affected sections
2. Patch every affected country playbook (the entry's `playbook_sections_touched` field is the lookup)
3. Re-stamp the section's `**Last verified**` date in each patched playbook
4. If the reform ENDED a program (visa / CBI / NHR), edit `config/_visa-programs.json` (source of truth — change the matching record's `status` field), then run `python3 scripts/render-visa-programs.py` to refresh `shared/visa-programs.md`. ALSO update the ENDED narrative registry at the top of `shared/visa-programs.md` (hand-written, outside the AUTOGEN block) and the ENDED registry table at the top of `regulatory-watch.md`. The `visa-programs-audit.yml` workflow will fail CI if any country playbook still mentions the programme without an ENDED/SUSPENDED/etc. acknowledgement marker.

The auto-downgrade rule (in [`shared/updater.md`](./skills/property-deep-dive/shared/updater.md) § Auto-downgrade) will surface stale claims at render time even if you forget step 3 — but the goal is to never let it.

## Maintenance commands you'll actually use

```
/property-deep-dive --update --validate-only --country=<iso2>     # URL liveness for one country
/property-deep-dive --update --refresh-only --country=<iso2>      # data refresh, no URL check
/property-deep-dive --update=<iso2>                               # full re-research
/property-deep-dive --health-report                               # decay matrix, plan next batch
/property-deep-dive --update --diff                               # preview changes before write
```

Always run `--diff` first if you're uncertain. `--interactive` is the safest mode for batch updates.

## File map (where things live)

```
skills/property-deep-dive/                # the skill payload (everything plugin hosts ship)
├── SKILL.md                              # master router — argument-hint, section catalog, country matrix
├── shared/
│   ├── anti-hallucination.md             # 7 mandatory checks (read first when editing output logic)
│   ├── regulatory-watch.md               # date-stamped reform tracker (read first when fixing tax/visa)
│   ├── updater.md                        # maintenance mode + auto-downgrade rule
│   ├── verdict-bands.md                  # 🟢🟡🟠🔴 severity contract
│   ├── output-template.md                # canonical section formatting
│   ├── sections.md                       # universal section contract
│   ├── preflight.md                      # country detection + listing parse
│   ├── visa-programs.md                  # ENDED registry source of truth
│   ├── <24 section implementations>      # one per --<flag> (or grouped where shared)
│   ├── <6 sub-section extensions>        # mains-reliability / finance-banking / notary-forced-heirship / risks-build-quality / digital-nomad-healthcare / rental-yield-delta
│   └── <9 tooling docs>                  # tco / mortgage / fixtures / diff-watcher / etc.
└── countries/<iso2>/playbook.md          # 109 country playbooks
.github/workflows/                        # weekly URL liveness, monthly health report, 6h feed watcher
config/_regions.json                      # docs-build input (README country matrix grouping) — NOT loaded by the skill at runtime
config/_tiers.json                        # refresh-cadence tier membership (A 90d / B 180d / C 365d) — read by audit/refresh CI
```

References inside SKILL.md / shared/*.md / countries/*/playbook.md use *relative* paths (`shared/X.md`, `countries/<iso2>/playbook.md`) — they resolve correctly because the skill is self-contained under `skills/property-deep-dive/`. References from outside the skill folder (CI workflows, docs, scripts) use the full repo-relative path.

## What NOT to do

- ❌ Don't commit personal data (specific street addresses, names, listing-specific data tied to a real person). Worked examples should use placeholder addresses.
- ❌ Don't fabricate URL replacements during `--update`. If a broken URL has no clean replacement, mark `❌ DEPRECATED — primary source removed; verify with <fallback authority>` and surface in the run-quality notes.
- ❌ Don't bypass `--diff` in batch updates — always preview before writing.
- ❌ Don't re-stamp `Last verified` based on URL-200 alone. URL-liveness ≠ data-still-current. Re-verify the actual numbers against the source content.
- ❌ Don't add a new universal section without registering it in `skills/property-deep-dive/SKILL.md` argument-hint AND the Sections table.
- ❌ Don't `git add _local/` or `*.bak-*` artifacts. They're gitignored locally; if you see them on `git status`, something's off.

## When in doubt

1. **Verify before recommending**: a memory or assumption that names a specific function/file/flag is a claim it existed when written. Grep the current state before acting.
2. **Ask if the user's request collides with the anti-hallucination contract**: e.g., "fill in tax rates for all 103 countries quickly" without sources — that's slot-filling. Push back, propose research-first.
3. **Default to surfacing limitations explicitly**: "Confidence: MEDIUM because…" beats vague enthusiasm.

## Memory

If you're using Claude Code's auto-memory, project memory lives at `~/.claude/projects/<encoded-cwd>/memory/` (the encoding turns the absolute project path into a single dash-separated directory name). Useful files to seed there:

- `property-deep-dive-skill-state.md` — full architecture checkpoint with verified file/line counts
- `feedback-property-skill-style.md` — collaboration patterns from prior sessions

Read those first if resuming work without context.
