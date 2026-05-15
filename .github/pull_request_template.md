<!--
Thanks for the PR. Below mirrors the checklist in CONTRIBUTING.md — please tick what applies.
For factual corrections + new countries, complete the relevant section.
-->

## What this PR does

<!-- One paragraph. What changed and why. -->

## Type of change

- [ ] Factual correction (wrong tax rate / fee / threshold / ENDED programme listed as active)
- [ ] Broken URL replacement
- [ ] New country playbook (must hit FR/IT/CZ/SK density: ~400-500 lines, 34 sections, primary sources)
- [ ] Regulatory-watch entry (recent reform, ENDED programme, EU directive transposition)
- [ ] New universal section flag (`skills/property-deep-dive/shared/<section>.md` + SKILL.md registration)
- [ ] New tooling doc (`skills/property-deep-dive/shared/<tool>.md` + SKILL.md registration)
- [ ] Anti-hallucination behaviour fix (`skills/property-deep-dive/shared/anti-hallucination.md`)
- [ ] Documentation / README / CONTRIBUTING / structural
- [ ] Other (explain above)

## Anti-hallucination contract

- [ ] Every numeric claim is **sourced** to a primary government / regulated entity, **computed** transparently, or **labelled** with `~` / `est.` / `≈` + calibration sentence
- [ ] No forbidden phrasings used: "approximately X", "in the area of", "typical for the region", "as of recent data", "industry average", "experts say", "studies show", "should be around", "is likely connected to"
- [ ] Where a number could not be sourced, the playbook says `data not publicly available — verify at <authoritative source>` rather than guessing

## URL hygiene

- [ ] All new / changed URLs return 2xx (or are tagged `(bot-protected; browser-OK)` if behind Cloudflare/DataDome)
- [ ] Redirects use the canonical destination URL
- [ ] No silently deleted dead URLs — replaced on the same primary-source domain or marked `❌ DEPRECATED`

## Section / playbook hygiene

- [ ] Every numeric fact is date-stamped: `(<year> data, source <X>)`
- [ ] If facts are >12 months old, suffix `— rates/figures may have changed since`
- [ ] Listing-derived claims are tagged `(per listing — verify with cadastre / on visit)`
- [ ] Parcel-vs-commune granularity respected (no silent elevation of commune-level data to parcel-level claims)
- [ ] Status footer present at the end of any touched playbook with `**Confidence**: HIGH/MEDIUM/LOW` + `**Last verified**: YYYY-MM-DD`

## Cross-cutting consistency

- [ ] If a new country was added, `SKILL.md` country support matrix updated
- [ ] If a regulatory-watch entry was added, every affected country playbook section was re-stamped (use the entry's `playbook_sections_touched` field)
- [ ] If skills/property-deep-dive/shared/ logic was changed, all affected country playbooks remain consistent
- [ ] If a programme ENDED, `config/_visa-programs.json` is updated (source of truth — change `status`), `shared/visa-programs.md` regenerated via `python3 scripts/render-visa-programs.py`, and the ENDED registry in `shared/regulatory-watch.md` is also updated

## Privacy + repo hygiene

- [ ] No personal addresses, names, or listing-specific data tied to a real person (worked examples use placeholder addresses)
- [ ] No `_local/`, `*.bak-*`, `*.scaffold-*`, or `_ci/` artifacts staged
- [ ] No secrets, API keys, or credentials in the diff

## For factual corrections

- **Country / file / line**:
- **Current claim**:
- **Correct value**:
- **Primary source URL**:
- **Verified date** (YYYY-MM-DD):

## For new countries

- **ISO2**: 
- **Population coverage / why this country**: 
- **Lines added**: <should be ~400-500 to match FR/IT/CZ/SK>
- **Section coverage**: all 23? Any deferred? List them.
- **Source-tier audit**: % of facts sourced to primary government vs aggregator vs listing
