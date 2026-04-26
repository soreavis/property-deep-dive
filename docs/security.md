# Security and safe usage

This skill helps with property due-diligence — decisions worth six to seven figures. Use it as **decision-support**, not legal / tax / financial advice. This page covers safe operation; for vulnerability reporting see [SECURITY.md](../SECURITY.md) at repo root.

## What this skill does NOT do

- Provide legal, tax, or financial advice
- Replace a qualified surveyor / notary / tax advisor
- Bypass authentication walls or robots.txt
- Cache or redistribute primary-source content beyond extracted, cited facts
- Process personally identifiable information beyond the address being analysed

If a section needs a guarantee that only a regulated professional can give (e.g. a parcel-level title check by a notary), the skill **says so explicitly** rather than guessing.

## Anti-hallucination contract

Every numeric / factual claim the skill outputs must be one of:

1. **Sourced** to a primary government / regulated entity (with a link)
2. **Computed** transparently (with the inputs visible inline)
3. **Estimated** with `~` / `est.` / `≈` prefix and a calibration sentence

If a number can't satisfy any of those, the skill writes `data not publicly available — verify at <authoritative source>` rather than guessing.

The seven mandatory pre-output checks are documented in [`shared/anti-hallucination.md`](../skills/property-deep-dive/shared/anti-hallucination.md). Forbidden phrasings (e.g. "approximately X", "industry average", "experts say") are blocked at CI.

## What you must verify before signing anything

Every report ends with a verification footer listing parcel-level checks the buyer must run independently. The most common ones:

| Step | What to check | Where |
|---|---|---|
| 1 | Tax figures | Request the seller's most recent annual tax bill (avis de taxe foncière in FR, Grundsteuerbescheid in DE, Council Tax bill in UK, etc.) |
| 2 | Risk disclosures | Pull the official parcel-level risk document (ERRIAL in FR, Risikoauskunft in DE, Energy & Environmental Search in UK, similar elsewhere) |
| 3 | Sewer / utility connection | Telephone the local authority for parcel-level confirmation |
| 4 | Building condition | Commission an independent surveyor for any pre-1990 build |
| 5 | Listing claims | Anything from the seller's listing (surface, year built, energy rating, condition) must be re-verified with cadastre and a physical visit |
| 6 | Tax / visa / pension regimes | The regulatory landscape changes; confirm with a local tax advisor before relying on any benefit |

Even when the skill labels confidence HIGH, **you still verify with the cited source on the day of signature.** AI-assisted aggregations can be wrong, and regulations can change between the skill's last verification stamp and your viewing.

## Reporting issues

| Issue type | Channel |
|---|---|
| Wrong tax rate / fee / threshold | [Factual-correction issue template](https://github.com/soreavis/property-deep-dive/issues/new?template=factual-correction.yml) |
| Dead URL | [Broken-URL issue template](https://github.com/soreavis/property-deep-dive/issues/new?template=broken-url.yml) |
| ENDED programme listed as active | Use Factual-correction template; tag with `regulatory-watch` |
| New regulatory reform to track | [Regulatory-watch entry template](https://github.com/soreavis/property-deep-dive/issues/new?template=regulatory-watch.yml) |
| New country proposal | [New-country template](https://github.com/soreavis/property-deep-dive/issues/new?template=new-country.yml) |
| Dispatch-logic / supply-chain vulnerability | [GitHub Security Advisory](https://github.com/soreavis/property-deep-dive/security/advisories/new) |

## Confidence + decay

Each playbook section carries a `**Confidence**` label (HIGH / MEDIUM / LOW / STALE) and a `**Last verified**` (or `as of`) date stamp. The auto-downgrade rule applies at render time:

- HIGH → MEDIUM after 6 months without re-verification
- MEDIUM → LOW after 12 months
- Anything ≥ 18 months → STALE

If a regulatory-watch entry of Tier 1 (CRITICAL) post-dates the playbook's stamp, the affected section is forced to STALE regardless of calendar age. **Treat STALE labels as "must re-verify before relying on".**

## Scope of "publicly accessible data"

The skill consults publicly accessible primary sources (cadastres, statistics offices, central banks, tax authorities, risk authorities), aggregator sites where listed, and listing platforms where listed.

It does **not**:

- Scrape behind authentication walls
- Bypass robots.txt
- Cache or redistribute primary-source content
- Process PII beyond the address being analysed

Distribution is via GitHub HTTPS (TLS); releases are sigstore-signed and verifiable with cosign — see [docs/install.md](./install.md#verifying-release-authenticity).

## Liability

This software is provided "as is" without warranty of any kind. See [LICENSE](../LICENSE) (MIT). Property-purchase decisions are six- to seven-figure commitments; the user assumes full responsibility for due diligence performed using this skill's output. See [DISCLAIMER.md](../DISCLAIMER.md) for the full disclaimer.
