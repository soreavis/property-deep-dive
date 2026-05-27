# Universal `--cross-border` Section

Cross-border-residency / cross-border-business framework layer. Surfaces the personal-residency, corporate-residency, and DTA tie-breaker exposure a buyer faces when their *physical move* (to the property country) collides with *home-country tax-residence ties* and any *company they own / direct / shareholders of* in a third jurisdiction.

**Snapshot**: 2026-05-14. Treaties and exit-tax statutes move; numeric thresholds are deliberately NOT encoded here — every country pair is unique and per-pair encoding is exactly the slot-filling pressure `shared/anti-hallucination.md` warns against. This section ships **framework + linkage only**. Every claim is one of: an OECD Model Tax Convention article, a European Union directive / regulation, or a link to the authoritative treaty register / national authority.

**Anti-hallucination**: this section produces **no per-country tax rates, no per-pair tie-breaker outcomes, and no corporate-tax computations**. It produces a checklist of exposure flags + sourced pointers to the authoritative treaty / national authority. Every output ends with `Confidence: HIGH` (framework references) or `MEDIUM` (where regional pattern is summarised). All recommendations carry an explicit "engage cross-border tax counsel in BOTH jurisdictions before acting" call-out.

**Disambiguation — `--cross-border` vs `--home-tax` vs `--visa` vs `--relocation`**:

- `--cross-border` = **dual-jurisdiction exposure framework**. Tax-residence tie-breaker (DTA Art. 4), corporate POEM / PE risk for owner-managers (DTA Art. 4(3) + Art. 5), origin-country deregistration entry points, EU-citizen free-movement clarification. Neutral on the buyer's home country — it surfaces the *mechanism*, not the numbers.
- `--home-tax` = **buyer-residence-side** detail. What the buyer's home tax authority does annually + at disposal + at death + at emigration because they own foreign property. Indexed by buyer residence (`shared/home-tax.md` covers ~20 buyer cohorts).
- `--visa` = residence-permit programs (RBI, golden visa, DNV, retirement visa, work permit). EU/EEA/CH passport holders moving inside the bloc do NOT need a visa — see EU-citizen prelude in `shared/visa-programs.md` and the cross-link below.
- `--relocation` = **post-completion logistics** (pets, driving licence, vehicle import, utility setup, healthcare gap). Operational, not tax/residence.

Tax can fall due in BOTH countries simultaneously and DTAs allocate or apportion. `--cross-border` flags the allocation question; `--home-tax` and `--tax` quantify each side.

## Universal contract

For any buyer whose move triggers a residency change (or whose continued ties to the origin country could trigger dual residence), return:

1. **Tax-residence trigger inventory** — the legal tests that could make the buyer tax-resident in EITHER country (days, permanent home, centre of vital interests, habitual abode, nationality)
2. **DTA tie-breaker pointer** — the relevant treaty Article 4(2) cascade for the country pair, with a link to the official treaty register entry. NOT a tie-breaker outcome — that requires facts the skill does not have.
3. **POEM / PE flag for company owners** — if the buyer owns ≥ a meaningful interest in a company resident in a third country, surface the place-of-effective-management risk (DTA Art. 4(3)) and the permanent-establishment risk (DTA Art. 5). Mandatory call-out: this is a corporate-tax question requiring counsel.
4. **Origin-country deregistration entry point** — the authority the buyer must notify, with a link. NOT a how-to — a doorway.
5. **EU/EEA/CH free-movement check** — if buyer holds an EU/EEA/CH passport AND destination is in the same bloc, surface that the visa section does not apply and link to the optional declaratory residence card per destination country.
6. **Cross-bloc move disclaimer** — DTA cascade applies regardless of EU/non-EU status; surface that being an EU citizen does NOT eliminate dual-residence exposure.
7. **Mandatory professional-advisor call-out** — every output ends with "engage cross-border tax counsel in BOTH jurisdictions; this section flags exposure, does not compute liability"
8. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Cross-Border Residency & Business Profile (origin: <ISO2>, destination: <ISO2>)

**Tax-residence triggers (origin)**: <link to origin authority's residence test>
**Tax-residence triggers (destination)**: <link to destination authority's residence test>
**DTA in force**: <treaty short-title + entry-into-force date + register URL>
**Tie-breaker reference**: <Article 4(2) cascade — permanent home → centre of vital interests → habitual abode → nationality>
**EU/EEA/CH applicability**: <free-movement applies y/n + optional declaratory card link>

### Company-owner exposure (if applicable)
**Company resident in**: <ISO2>
**POEM risk**: <DTA Art. 4(3) — flag if buyer makes management decisions from destination country>
**PE risk**: <DTA Art. 5 — flag if buyer performs revenue-generating activity from destination country>
**Action**: corporate-tax counsel in BOTH jurisdictions; modelling required before move

### Origin-country deregistration entry points
- Tax-residence: <authority + URL>
- Civil registration: <authority + URL>
- Healthcare: <authority + URL>
- Social security (if not coordinated): <authority + URL>

### Mandatory professional advice
This section flags exposure. It does NOT compute liability. Engage cross-border tax counsel in BOTH the origin and destination country before:
- Moving the centre of vital interests
- Continuing to manage / direct any third-country company from the destination
- Triggering exit tax on shares / pensions / collective vehicles
- Deregistering from the origin civil / tax / social-security registers

**Confidence**: HIGH (framework references)
**Last verified**: <YYYY-MM-DD>
**Sources**: <OECD MTC + EU directives + treaty register URLs>
```

---

## 7 cross-cutting traps to surface every time

1. **Buying property does NOT establish tax residence — physical presence does.** Acquiring real estate abroad is, by itself, never the trigger; the buyer becomes tax-resident when the destination country's residence test is met (typically physical-presence days + permanent home availability + centre of vital interests). Surface this so buyers don't conflate "I bought a house in X" with "I am tax-resident in X". Source: [OECD Model Tax Convention on Income and Capital, Commentary on Art. 4](https://www.oecd.org/tax/treaties/model-tax-convention-on-income-and-on-capital-condensed-version-20745419.htm).

2. **Dual residence is the default until DTA tie-breaker resolves it.** Both countries can claim residence under their own domestic test simultaneously. The Double Tax Agreement (where one exists) resolves this via the Article 4(2) cascade: (a) permanent home → (b) centre of vital interests → (c) habitual abode → (d) nationality → (e) mutual agreement. Each step decides — earlier steps trump later. **Tie-breaker outcomes depend on facts the property skill does not have**; surface the cascade, not a verdict.

3. **POEM / "place of effective management" can drag a foreign company into the destination country.** Under [OECD MTC Art. 4(3)](https://www.oecd.org/tax/treaties/model-tax-convention-on-income-and-on-capital-condensed-version-20745419.htm), a company resident in Country A under domestic law can become **treaty-resident in Country B** if its place of effective management is in B. For owner-managers, "effective management" includes habitually making strategic decisions from the destination — board calls, contract execution, banking decisions, key-employee oversight. The result: destination-country corporate tax on worldwide profits + an exit-tax event on the origin side. This is the single most under-flagged corporate-tax risk for relocating SME owners.

4. **Permanent Establishment ([OECD MTC Art. 5](https://www.oecd.org/tax/treaties/model-tax-convention-on-income-and-on-capital-condensed-version-20745419.htm)) is a softer trigger than POEM and easier to fall into.** Even without full residence migration, working from a fixed place in the destination for the foreign company (the "home office PE" question) can constitute a PE — making the destination-attributable share of profits taxable in the destination. The 2017 OECD MTC update tightened the agency-PE rules (Art. 5(5)–(6)); BEPS Action 7 and the [Multilateral Instrument](https://www.oecd.org/tax/treaties/multilateral-convention-to-implement-tax-treaty-related-measures-to-prevent-beps.htm) have further narrowed the historic Art. 5(4) preparatory/auxiliary exemption for many country pairs. Confirm whether the relevant treaty has been modified by the MLI.

5. **Origin-country deregistration is a separate process from tax-residence break — and frequently misunderstood.** Civil-register deregistration (e.g., SK *trvalý pobyt*, DE *Abmeldung*, NL *uitschrijving*, ES *baja consular*) is administrative; tax residence is determined independently by the tax authority's residence test and the DTA tie-breaker. Buyers routinely assume that not deregistering = remaining home-country resident, OR that deregistering = breaking tax residence cleanly. Both assumptions are wrong. Surface the four parallel registers (tax / civil / health / social-security) as separate workstreams.

6. **EU/EEA/CH free movement does not eliminate dual-residence or DTA exposure.** Holding an EU passport removes the visa requirement under [Directive 2004/38/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0038) and the optional declaratory residence card replaces it — but tax, social-security coordination, and POEM/PE rules apply identically to EU and non-EU citizens. The DTA tie-breaker is not citizenship-sensitive (except as the final tie-breaker step). EU social-security coordination ([Regulation 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883)) prevents *double affiliation* but does NOT prevent dual *tax* residence — these are separate regimes.

7. **Exit-tax events trigger on the origin side independently of destination acceptance.** Several jurisdictions impose deemed-disposition or step-up taxes on the exiting individual's holdings (typically shareholdings ≥ a threshold; some include direct foreign RE). The exit tax is an *origin-country* event, governed by *origin-country statute*, separate from the destination-country welcome regime. Per-country exit-tax detail is in `shared/home-tax.md` § cohort tables (US § 877A, CA ITA § 128.1, AU CGT event I1, IL § 100A, ZA § 9H, DE § 6 AStG, FR Art. 167 bis, JP § 60-2, KR Art. 118-9). Surface that an exit-tax check is a non-negotiable pre-move item for any buyer with company shares, options, pensions in trusts, or collective-investment vehicles.

---

## Tax-residence framework (OECD MTC Art. 4 deep dive)

The OECD Model Tax Convention is the architecture underlying ~3,000 bilateral DTAs. Most modern treaties follow it. Per-treaty deviations exist — verify the actual treaty text, not the model.

### Domestic-law residence tests (typical patterns)

Every jurisdiction has its own residence test; pattern families:

| Pattern | Examples | Mechanism |
|---|---|---|
| Days + permanent home | Most EU civil-law (FR, IT, ES, DE, BE, NL, AT, PT) | ≥ 183 d in calendar year OR principal home in country OR centre of economic interests |
| Days + ordinary residence | UK Statutory Residence Test ([Sch 45 FA 2013](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45)) | Automatic UK / automatic overseas / sufficient-ties — multi-factor |
| Substantial-presence formula | US ([IRC § 7701(b)](https://www.law.cornell.edu/uscode/text/26/7701)) | 31 d current + 183 weighted over 3y |
| Domicile + days | UK pre-FA 2025 (now LTR) · IL · IN | Domicile of origin + physical-presence overlay |
| Citizenship-based | US (uniquely) | Citizen tax-resident regardless of physical presence |
| Territorial / source | SG · HK · MY · several Caribbean | Foreign-source income out of scope when remitted-only |

**Source for each country's residence test**: see authority links in `shared/home-tax.md` § Authority URLs.

### DTA Article 4(2) tie-breaker cascade

When both countries claim residence under domestic law, the DTA tie-breaker determines treaty residence. OECD MTC Art. 4(2) cascade — apply in strict order until one step decides:

1. **Permanent home available to him** — a dwelling continuously available (not necessarily owned; rented or held under any title). If permanent home in BOTH countries, go to step 2.
2. **Centre of vital interests** — closer personal AND economic relations. Family location, social ties, place of business, place from which property is administered. The "personal" criterion is weighted at least equally with "economic". If indeterminate, go to step 3.
3. **Habitual abode** — where the person more frequently dwells. Counted not over a single year but over a period sufficient to establish a pattern.
4. **Nationality** — if habitual abode in both or neither, citizenship of one of the contracting states resolves.
5. **Mutual agreement procedure (MAP)** — competent authorities of the two states settle by agreement.

Source: [OECD MTC + Commentary on Art. 4](https://www.oecd.org/tax/treaties/model-tax-convention-on-income-and-on-capital-condensed-version-20745419.htm).

### Companies — Art. 4(3)

Pre-2017 OECD MTC: place-of-effective-management (POEM) tie-breaks dual corporate residence. Post-2017 OECD MTC: MAP-by-default. Many existing treaties retain the POEM tie-breaker; the MLI may have replaced it. Verify per-pair via the [OECD MLI Matching Database](https://www.oecd.org/tax/treaties/mli-matching-database.htm).

### Where to find each treaty

| Region | Treaty register / source |
|---|---|
| Multilateral Instrument matches | [OECD MLI Matching Database](https://www.oecd.org/tax/treaties/mli-matching-database.htm) |
| Global treaty index | [IBFD Tax Research Platform](https://research.ibfd.org/) (paid) · [Wolters Kluwer CCH](https://www.wolterskluwer.com/en/solutions/cch-tagetik) (paid) |
| US treaty list | [IRS — United States income tax treaties A-Z](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z) |
| UK treaty list | [HMRC Tax Treaty Manual A-Z](https://www.gov.uk/government/collections/tax-treaties) |
| Canada treaty list | [Department of Finance — tax treaties](https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties.html) |
| Australia treaty list | [ATO international tax agreements](https://www.ato.gov.au/individuals-and-families/international-tax-for-individuals/international-tax-agreements) |
| France treaty list | [impots.gouv.fr — Conventions fiscales internationales](https://www.impots.gouv.fr/les-conventions-internationales/conventions-internationales) |
| Germany treaty list | [BMF — Stand der Doppelbesteuerungsabkommen](https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/staatenbezogene_info.html) |
| Italy treaty list | [Agenzia delle Entrate — Convenzioni internazionali](https://www.agenziaentrate.gov.it/portale/schede/rimborsi/convenzioni-contro-le-doppie-imposizioni/scheda-informativa-convenzioni-contro-le-doppie-imposizioni) |
| Spain treaty list | [AEAT — Convenios para evitar la doble imposición](https://www.hacienda.gob.es/es-ES/Normativa%20y%20doctrina/Normativa/CDI/Paginas/CDI_Alfa.aspx) |
| Netherlands treaty list | [Belastingdienst — Belastingverdragen](https://www.belastingdienst.nl/wps/wcm/connect/en/individuals/content/when-is-a-tax-treaty-concluded) |
| Switzerland treaty list | [SIF — Doppelbesteuerungsabkommen](https://www.sif.admin.ch/en/double-taxation-agreements-dtas) |
| Slovakia treaty list | [Ministerstvo financií SR — Zoznam ZZDP](https://www.mfsr.sk/sk/dane-cla-uctovnictvo/priame-dane/dane-z-prijmu/zmluvy-zamedzeni-dvojiteho-zdanenia/zmluvy-zamedzeni-dvojiteho-zdanenia/) |
| Czech Republic treaty list | [MF ČR — Přehled platných smluv](https://www.mfcr.cz/cs/legislativa/dvoji-zdaneni/prehled-platnych-smluv) |
| Poland treaty list | [Ministerstwo Finansów — Wykaz umów o unikaniu podwójnego opodatkowania](https://www.gov.pl/web/finanse/wykaz-umow-o-unikaniu-podwojnego-opodatkowania) |
| Japan treaty list | [MOF — Income Tax Treaties](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/index.htm) |
| Korea treaty list | [NTS — International Tax](https://www.nts.go.kr/english/cm/cntnts/cntntsView.do?mi=11195&cntntsId=8315) |
| Singapore treaty list | [IRAS — Avoidance of Double Taxation Agreements](https://www.iras.gov.sg/taxes/international-tax/list-of-dtas-limited-dtas-and-eoi-arrangements) |
| Hong Kong treaty list | [IRD — Comprehensive DTAs](https://www.ird.gov.hk/eng/tax/dta_inc.htm) |
| Brazil treaty list | [Receita Federal — Acordos Internacionais](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/acordos-internacionais/acordos-para-evitar-a-dupla-tributacao) |
| Mexico treaty list | [SAT — Tratados para evitar la doble tributación](https://www.sat.gob.mx/normatividad/63960/tratados-para-evitar-la-doble-tributacion-vigentes) |
| South Africa treaty list | [SARS — Double Taxation Agreements](https://www.sars.gov.za/legal-counsel/international-treaties-agreements/double-taxation-agreements/) |

For pairs not in the table above, start at the [OECD MLI Matching Database](https://www.oecd.org/tax/treaties/mli-matching-database.htm) — even non-OECD members are typically searchable via the destination authority's register.

---

## POEM / PE checklist for company owners

When the buyer owns or directs a company resident in a third country, surface this checklist verbatim. It does NOT compute exposure — it triggers the call to corporate-tax counsel.

### Place of Effective Management (POEM) red flags
- [ ] Board meetings habitually held / dialled-in from the destination country
- [ ] Major contracts signed from the destination
- [ ] Banking and treasury decisions executed from the destination
- [ ] Key-employee supervision performed from the destination
- [ ] CEO / managing director physically present in the destination > 183 d / yr
- [ ] Investment decisions, dividend declarations made from the destination

If ≥ 2 ticked → **destination POEM risk is real**. The company can become treaty-resident in the destination under DTA Art. 4(3) → destination corporate tax on worldwide profits + origin-side exit-tax event. **Engage corporate-tax counsel in BOTH jurisdictions before the move.**

### Permanent Establishment (PE) red flags
- [ ] Buyer regularly works from the destination property for the foreign company
- [ ] A "fixed place of business" (home office, dedicated room) is used habitually for the company's revenue-generating activity
- [ ] Buyer concludes contracts in the company's name from the destination
- [ ] Buyer plays the principal role in the conclusion of contracts (post-BEPS Action 7 agency-PE expansion)
- [ ] Inventory / equipment / goods of the company are stored at the destination
- [ ] Destination employees / contractors of the company report into the property location

If ≥ 1 ticked → **destination PE risk is real** under DTA Art. 5. Destination-attributable profits become taxable locally, the company may be required to register for VAT and corporate tax in the destination, and payroll obligations for any local activity may attach. Even where formal PE is avoided, the BEPS-aligned [agency-PE expansion (MTC 2017 Art. 5(5)–(6))](https://www.oecd.org/tax/treaties/) can pull in profits without a fixed place. **Engage corporate-tax counsel.**

### Mitigation patterns (each requires counsel)
- Substance in origin country — board members resident in origin, board meetings physically held there, keyspace decisions documented
- Director-shareholder separation — owner is shareholder but not sole director; resident-origin director carries fiduciary substance
- Professional management — appoint resident-origin licensed director or fiduciary
- Pre-move reorganisation — sale of shares before the move triggers origin CGT cleanly (vs deemed-disposition exit tax that can be more punitive)
- Revenue diversion — invoice the foreign company from a destination consultancy structure (creates separate destination tax point but isolates origin company)

None of the above are recommendations — they are patterns counsel will evaluate. **Do not adopt without engagement.**

---

## Origin-country deregistration framework

Four parallel registers must be addressed. Each is run by a different authority and carries independent consequences. Surface them as separate workstreams; do not bundle.

### 1. Tax-residence break
The tax authority decides residence by its own test + DTA tie-breaker. There is rarely a "deregistration" form — instead, file a final-year return with foreign address, surface DTA tie-breaker if applicable, and trigger exit-tax computation if statute requires. Some jurisdictions (DE, NL, ES, AT, BE) use a final-year *Wegzugsformular* / similar form. Pointer: each country's tax-authority "leaving the country" guidance — see `shared/home-tax.md` § Authority URLs and country playbooks' new "Leaving this country" stub (rolling out lazily).

### 2. Civil registration / municipal register
Administrative, separate from tax. Pointers (non-exhaustive — full per-country pointers in country playbooks):

| Country | Register | Process |
|---|---|---|
| DE | Einwohnermelderegister | *Abmeldung beim Einwohnermeldeamt* — within 2 weeks of move ([Bundesmeldegesetz § 17](https://www.gesetze-im-internet.de/bmg/__17.html)) |
| NL | Basisregistratie Personen | *Uitschrijving* via gemeente — at least 5 days before departure ([Wet BRP](https://wetten.overheid.nl/BWBR0033715)) |
| AT | Zentrales Melderegister | *Abmeldung* within 3 days of move ([Meldegesetz § 4](https://www.ris.bka.gv.at/Bundesrecht/)) |
| ES | Padrón Municipal | *Baja en el padrón* via ayuntamiento or *baja consular* via consulate abroad |
| FR | (no central register) | Civil register *not* mandatory; informal — but tax address change required |
| IT | Anagrafe della popolazione residente | *Cancellazione anagrafica* via comune; AIRE registration via consulate after departure ([Legge 470/1988](https://www.normattiva.it/)) |
| SK | Register obyvateľov SR | *Odhlásenie z trvalého pobytu* via *ohlasovňa pobytu* (municipal office) ([Zákon 253/1998 Z. z. § 6](https://www.slov-lex.sk/)) |
| CZ | Evidence obyvatel | *Ukončení trvalého pobytu* via municipal office ([Zákon 133/2000 Sb.](https://www.zakonyprolidi.cz/cs/2000-133)) |
| PL | Ewidencja ludności | *Wymeldowanie* via urząd gminy ([Ustawa o ewidencji ludności](https://isap.sejm.gov.pl/)) |
| HU | Lakcímnyilvántartás | *Lakcímváltozás* via okmányiroda |
| Nordic countries | Folkregister / Folkbokföring / Folkeregister | Notify Skatteverket / Skatteetaten / Skat / DVV; deregistration triggers personal-number consequences |
| UK | (no central register) | Tell HMRC via P85 + DWP + GP + electoral roll independently |
| US | (no central register) | Federal: form 1040 final-year + state-tax change-of-address; certain states (CA, NY) sticky |

### 3. Health insurance
Origin-country mandatory health insurance must typically be terminated when residence breaks. EU/EEA/CH coordination ([Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883)) handles transition via S1 form and EHIC overlap. Outside the EU/EEA/CH coordination zone, double-coverage is the trap: the new system enrolment may have a waiting period (DE day 1; FR 3-month residence; CH within 3 months; etc. — full table in `shared/relocation.md` § Healthcare). Pointer: notify origin sickness fund + enrol destination per `shared/relocation.md`.

### 4. Social security / pensions
EU/EEA/CH: governed by [Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883) — coordination prevents double affiliation. A1 certificate covers temporary postings. Bilateral agreements for non-EU pairs (US-EU bilateral totalisation, AU SAA agreements, CA SSA agreements) — see [SSA International Agreements](https://www.ssa.gov/international/agreements_overview.html) for US-side and the relevant origin-country social-security authority. Pension transfers, unrealised contribution years, and survivor benefits all carry separate notice obligations.

---

## EU/EEA/CH free-movement framework

If the buyer holds an EU, EEA (Iceland / Liechtenstein / Norway), or Swiss passport AND is moving inside the same bloc, the visa section does NOT apply.

**Legal basis**:
- [TFEU Art. 21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012E021) — free movement of citizens
- [TFEU Art. 45](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012E045) — free movement of workers
- [TFEU Art. 49](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012E049) — freedom of establishment (self-employed + companies)
- [Directive 2004/38/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0038) — Citizens' Rights Directive: residence rights, registration, family rights
- [EEA Agreement](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)) — extends free movement to IS / LI / NO
- [EU-CH Agreement on Free Movement of Persons (AFMP)](https://www.fedlex.admin.ch/eli/cc/2002/243/en) — extends to CH (in force 1 Jun 2002)

**Practical implications**:
- No visa requirement for stays > 90 days in destination
- Optional declaratory residence card per destination — see EU-citizen prelude in `shared/visa-programs.md` for the per-country card link table
- Right of residence beyond 3 months requires (per Dir 2004/38/EC Art. 7): worker / self-employed / sufficient resources + comprehensive sickness insurance / student / family member of any of the above
- Permanent residence after 5 years of continuous legal residence (Art. 16)

**Cross-link**: PR #2 in this skill's wave adds an EU/EEA/CH prelude to `shared/visa-programs.md` with the full per-country declaratory-card link table. Cross-border invocation should reference that prelude rather than duplicate it.

**What free movement does NOT do**:
- Does NOT eliminate dual tax residence (DTA tie-breaker still applies)
- Does NOT eliminate POEM/PE risk for company owners
- Does NOT bundle public health-insurance access (waiting periods + S1 transition)
- Does NOT eliminate origin-country exit-tax events (where statute applies)
- Does NOT auto-deregister buyer from origin civil / tax / social-security registers — those are separate notifications

---

## Mandatory professional-advisor call-out

Every output of this section ends with:

> **This section flags exposure. It does NOT compute liability.**
>
> Cross-border tax + corporate-residency questions are fact-intensive and per-country-pair specific. Engage **cross-border tax counsel in BOTH the origin and destination country** before:
>
> - Moving the centre of vital interests (changes DTA tie-breaker)
> - Continuing to manage / direct any third-country company from the destination (POEM / PE risk)
> - Triggering exit tax on shares / pensions / collective investment vehicles
> - Deregistering from the origin civil / tax / social-security registers
> - Exercising special inbound regimes (Beckham / 24-bis / FIG / Olim / RNOR / 30%-ruling — see `shared/home-tax.md`)
>
> A single advisor per country is the minimum; a coordinated cross-border practice (Big Four, [STEP](https://www.step.org/) members, [IBA](https://www.ibanet.org/) tax committee firms) is preferable for owner-managers with company exposure. Cost: typically EUR 1,500–10,000 per jurisdiction for an initial scoping memo; orders of magnitude cheaper than the cost of a wrong residency-break, an unanticipated POEM shift, or a missed exit-tax event.

---

## When to invoke

`--cross-border` is **opt-in** — it does NOT run under `--all`. Buyers who don't have multi-jurisdiction exposure (e.g., a French resident buying in France, or a UK resident retiring to UK after a long career there) don't need it. Invoke when ANY of:

- Buyer's stated origin country differs from the property country
- Buyer mentions owning a company in a third jurisdiction
- Buyer mentions "I'll keep my [origin] residence" or "I'll commute"
- Journey type is `--journey=foreign-buyer` or `--journey=investor`
- Buyer mentions "trvalý pobyt", "Anmeldung", "padrón", "AIRE", or any origin-country residency / civil-register concept

Pairs naturally with `--home-tax` (computes the buyer-side numbers), `--visa` (where required for non-EU pairs), and `--relocation` (operational layer).

---

## Status

**Confidence**: HIGH (framework references — OECD MTC + EU directives + national authority links)
**Last verified**: 2026-05-14
**Maintenance cadence**: review on OECD MTC update (next expected 2027 cycle), MLI matching-database refresh (continuous), or EU directive amendment affecting Dir 2004/38/EC, Reg 883/2004, or AFMP (rare; calendar-actionable when published).
**Out of scope by design**: per-country-pair tie-breaker outcomes; per-country corporate-tax rates; per-pair POEM verdicts; specific exit-tax computations. These are professional-advisor work — see § Mandatory professional-advisor call-out.

## Authority URLs

- **OECD Model Tax Convention**: https://www.oecd.org/tax/treaties/model-tax-convention-on-income-and-on-capital-condensed-version-20745419.htm
- **OECD MLI Matching Database**: https://www.oecd.org/tax/treaties/mli-matching-database.htm
- **OECD BEPS Action 7 (PE update)**: https://www.oecd.org/tax/beps/beps-actions/action7/
- **EU TFEU consolidated**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012E
- **EU Directive 2004/38/EC (Citizens' Rights)**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0038
- **EU Regulation 883/2004 (Social Security Coordination)**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883
- **EEA Agreement**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)
- **EU-CH Agreement on Free Movement of Persons**: https://www.fedlex.admin.ch/eli/cc/2002/243/en
- **EU Your Europe — Residence rights**: https://europa.eu/youreurope/citizens/residence/index_en.htm
- **EU Your Europe — Cross-border taxation**: https://europa.eu/youreurope/citizens/work/taxes/index_en.htm
- **STEP (Society of Trust and Estate Practitioners)**: https://www.step.org/
- **IBA Tax Committee**: https://www.ibanet.org/unit/Real+Estate+Section/committee/Real+Estate+Section/3101

Per-country tax authority URLs are in `shared/home-tax.md` § Authority URLs (US IRS, UK HMRC, CA CRA, AU ATO, NZ IRD, DE BMF, FR DGFiP, IT Agenzia Entrate, ES AEAT, NL Belastingdienst, Nordic, CH ESTV, JP NTA, KR NTS, SG IRAS, HK IRD, CN STA, IL ITA, IN IT, BR Receita, MX SAT, ZA SARS, AE FTA, SA ZATCA).
