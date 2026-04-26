# Security policy

## Scope of this skill

`property-deep-dive` ships only Markdown text — there is no executable code in the published artifact, no server, no auth flow, and no user data is collected or stored. The skill runs inside [Claude Code](https://docs.claude.com/claude-code), and the only outbound network calls it makes are when the user (or a maintainer running `--update`) asks it to verify URLs or pull primary-source data.

This narrows the meaningful security surface to:

| Surface | Risk | Treatment |
|---|---|---|
| **Factual content** | A wrong tax rate or "ENDED programme listed as active" could lead a user to make a costly real-world decision | Anti-hallucination contract + `regulatory-watch.md` — report via the **factual-correction** issue template |
| **Broken URLs** | A dead URL could redirect to a malicious or impersonating domain | Weekly `url-liveness.yml` workflow — report via the **broken-url** issue template |
| **Dispatch logic in `SKILL.md`** | A crafted address or argument could make the router select the wrong country playbook or section | Report privately via Security Advisory (below) if exploitable |
| **GitHub Actions workflows** | The 3 workflows in `.github/workflows/` run scheduled HTTP requests against public URLs and read repo files | They use `permissions:` blocks scoped to `contents: read` + `issues: write`, no secrets, no third-party actions outside `actions/*` and `actions/github-script` |

## What to report privately vs publicly

**Report privately** via [GitHub Security Advisory](https://github.com/soreavis/property-deep-dive/security/advisories/new) if you discover:

- A dispatch-logic flaw that could mis-route an address to the wrong jurisdiction's tax / regulatory advice
- A way to make the workflows execute attacker-controlled content
- A vulnerability in a workflow that could leak repo metadata or token scope
- A supply-chain risk in the actions referenced in `.github/workflows/`
- An account / impersonation issue (e.g. someone forking and republishing under a confusingly similar name)

**Report publicly** via the regular issue templates if you find:

- A wrong tax rate, fee, threshold (use **factual-correction**)
- A dead URL (use **broken-url**)
- A regulatory reform that should be tracked (use **regulatory-watch**)
- An ENDED programme still listed as active (use **factual-correction** with the "ENDED" annotation)

## Disclosure timeline

For privately reported security issues:

- We aim to acknowledge within **72 hours**
- Where a fix requires re-research (e.g. a dispatch-logic correction that affects multiple country playbooks), expect **2-4 weeks** to land a verified fix
- Coordinated disclosure preferred; please do not file a public issue or PR with a working exploit until the maintainer has had a chance to patch

## Versions covered

Only the latest tagged release on the `main` branch is actively maintained. There is no LTS branch.

## Out of scope

The following are explicitly NOT security issues for this skill:

- "The skill ran slowly" — performance is governed by the LLM runtime, not this skill
- "An external primary-source government portal returned an error" — that's the upstream's reliability, not ours; report it via **broken-url** if persistent
- "The skill said `verify with a local notary` instead of giving a definitive answer" — that's the anti-hallucination contract working as designed
- "A specific listing platform blocks the skill" — if a listing aggregator blocks our `User-Agent`, that's documented in `skills/property-deep-dive/shared/test-fixtures.md` (~21 of 44 known bot-protected as of last audit)

## Acknowledgement

If you report a vulnerability that leads to a fix, you'll be credited in `CHANGELOG.md` (or in the GitHub release notes if no changelog yet) under "Security", unless you prefer to remain anonymous.
