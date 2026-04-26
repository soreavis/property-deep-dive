# Disclaimer

`property-deep-dive` is **decision-support, not legal, tax, or financial advice.**

This skill aggregates publicly accessible data and produces clearly-labelled estimates. The output is intended to help you ask the right questions, surface risks early, and shorten the gap between "I saw a listing" and "I'm ready to make an offer." It is **not** a substitute for:

- A licensed real-estate lawyer / notary
- A qualified tax advisor
- An independent surveyor
- The official primary sources cited in each report

## What you must verify before signing anything

Every report ends with a verification footer listing the parcel-level checks the buyer must run independently. The most common ones:

1. **Tax figures** — request the seller's most recent annual tax bill (avis de taxe foncière in FR, Grundsteuerbescheid in DE, Council Tax bill in UK, etc.).
2. **Risk disclosures** — pull the official parcel-level risk document (ERRIAL in FR, Risikoauskunft in DE, Energy & Environmental Search in UK, similar elsewhere).
3. **Sewer / utility connection** — telephone the local authority for parcel-level confirmation.
4. **Building condition** — commission an independent surveyor for any pre-1990 build.
5. **Listing claims** — anything from the seller's listing (surface, year built, energy rating, condition) must be re-verified with cadastre and a physical visit.
6. **Tax / visa / pension regimes** — the regulatory landscape changes; confirm with a local tax advisor before relying on any benefit.

## Anti-hallucination guardrails

The skill includes a multi-layer anti-hallucination guard (see `skills/property-deep-dive/shared/anti-hallucination.md`):

- Source-tier ranking (primary government > secondary aggregator > listing > inference)
- Confidence labels on every section (HIGH / MEDIUM / LOW / STALE)
- Auto-downgrade of confidence over time (HIGH → MEDIUM at 6mo, LOW at 12mo, STALE at 18mo) — see `skills/property-deep-dive/shared/updater.md` § Auto-downgrade
- Regulatory-watch tracking for reforms that supersede claims (`skills/property-deep-dive/shared/regulatory-watch.md`)
- Mandatory pre-output checks (numeric citations, parcel-vs-commune granularity, listing-trust flagging, contradiction surfacing)

These reduce — but do not eliminate — the risk of error. **AI-assisted aggregations can still be wrong.** Critical figures must be confirmed with primary sources or qualified professionals.

## Liability

This software is provided "as is", without warranty of any kind. See `LICENSE` (MIT). Property-purchase decisions are six- to seven-figure commitments; the user assumes full responsibility for due diligence performed using this skill's output.

## Reporting errors

If you spot a factual error (wrong tax rate, dead URL, ENDED program listed as active, regulatory reform missed), please open an issue. Errors of fact are the most important contributions — they protect future users from acting on stale information.

## Scope of "publicly accessible data"

The skill consults publicly accessible primary government sources (cadastres, statistics offices, central banks, tax authorities, risk authorities), aggregator sites (where listed), and listing platforms (where listed). It does **not**:

- Scrape behind authentication walls
- Bypass robots.txt
- Cache or redistribute primary-source content (only links + extracted facts with citations)
- Process personally identifiable information beyond the address being analysed
