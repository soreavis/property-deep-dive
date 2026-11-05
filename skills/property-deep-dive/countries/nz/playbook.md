# New Zealand 🇳🇿 — Property Due-Diligence Playbook

ISO2: `nz`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1010` Auckland CBD, `6011` Wellington CBD, `8013` Christchurch)
- **Admin levels**: Central government + 16 regions + 67 territorial authorities
- **Currency**: **NZD** (New Zealand dollar); 1 EUR = 1.9724 NZD (ECB reference rate, 22 Oct 2026; Jul–Oct 2026 range 1.9520–2.0121 — 2026 data, source [ECB — EUR/NZD reference rate](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-nzd.en.html))
- **Languages**: English (de facto) + Te Reo Māori (official)
- **Cadastre**: **Toitū Te Whenua / LINZ (Land Information NZ)** — fully unified national system
  - **Landonline**: `https://www.linz.govt.nz/` (lawyers/surveyors, paid)
  - **Public Land Record Search**: `https://lrs.linz.govt.nz/search/` — **$8 per record**
- **Identifier**: Record of Title (RT) reference (e.g. `WN12A/345`); supersedes older Certificate of Title
- **Ownership types**:
  - **Freehold (fee simple)** — most common
  - **Leasehold** — Cornwall Park (Auckland), Glasgow Crescent, Cashmere Hills; **99-year leases common on Māori land** under Te Ture Whenua Māori Act 1993
  - **Cross-lease** — ~10% of Auckland; clunky shared ownership of section + flat plan
  - **Unit title** — apartments, body corporate
- **Foreign-buyer ban**: Overseas Investment Amendment Act 2018 — still applies to most overseas persons. No consent needed for Australian or Singaporean citizens (residential or lifestyle land; must be ordinarily resident in NZ if the land is also otherwise sensitive) or for Australian / Singaporean permanent residents ordinarily resident in NZ ([LINZ — Buying residential property to live in](https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live), updated 6 Mar 2026). Off-the-plan apartments in large developments with a developer exemption certificate: overseas buyers may buy before construction is complete but cannot live in the apartment, and the developer may sell up to 60% to overseas people ([LINZ — Investing in apartments](https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/investing-apartments), updated 10 Sep 2025). **$5 million plus house pathway — in force since 6 Mar 2026** (Overseas Investment (National Interest Test and Other Matters) Amendment Act, Royal Assent 19 Dec 2025): Active Investor Plus (AIP), Investor 1 and Investor 2 resident-visa holders can apply for OIA consent to buy residential land with a dwelling for more than NZ$5,000,000, or land under NZ$5M where land + construction exceeds NZ$5M; the District Valuation Roll category must be residential or lifestyle (code starting R or L); land sensitive for other reasons (e.g. next to a beach, river, lake or reserve) is excluded; offers must be conditional on consent; fees NZ$2,040 (existing dwelling, price over $5M) / NZ$3,500 (all other cases); statutory timeframe 15 working days, LINZ aims to decide most within 5 (2026 data, sources: [LINZ — Investing in residential land over $5 million](https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/pathways-migrants-and-visa-holders/investing-residential-land-over-5-million), updated 27 Mar 2026; [LINZ — Reform of the Overseas Investment Act](https://www.linz.govt.nz/our-work/overseas-investment-regulation/reform-overseas-investment-act), updated 28 Aug 2026). Only one property per visa holder may be bought in reliance on the visa — any other such property must first be sold; where a partner also holds the visa, each visa may be relied on (2026 data, source: [LINZ — Detailed information for investor visa holders buying a house](https://www.linz.govt.nz/sites/default/files/doc/guidance-investor-visa-holders-long-form-march2026-v3.pdf), 26 Mar 2026)

## Section: `--price`

### Primary sources

- **REINZ (Real Estate Institute of New Zealand) HPI**: `https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx` — monthly, authoritative
- **Quotable Value (QV)**: `https://www.qv.co.nz/price-index/` — monthly QV House Price Index (average value + 3- and 12-month change by district); QV also carries out council rating revaluations (e.g. Kāpiti Coast, Mackenzie, Waitaki — Oct 2026 QV news), the CV basis for rates
- **Cotality NZ** (formerly CoreLogic NZ; corelogic.co.nz redirects to cotality.com): `https://www.cotality.com/nz` — separate private provider of dwelling-value and rent indices
- **Stats NZ**: `https://www.stats.govt.nz/` — its Housing topic lists no house price index (use REINZ / QV for prices); it publishes rental price indexes (stock and flow measures of rental property, monthly in Selected price indexes — Sep 2026: stock +0.1% YoY, flow +0.9% YoY, released 16 Oct 2026), property transfer statistics (transfers by New Zealanders and overseas people) and building consents (2026 data, sources [Stats NZ — Housing](https://www.stats.govt.nz/topics/housing/); [Stats NZ — Selected price indexes: September 2026](https://www.stats.govt.nz/information-releases/selected-price-indexes-september-2026/))
- **OneRoof Property Report**: `https://www.oneroof.co.nz/` — NZME, publisher of the NZ Herald (OneRoof footer "powered by nzme"; NZ Herald © 2026 NZME Publishing Limited; Oct 2026); media-company data, not official statistics

### Listing platforms

- **Trade Me Property**: `https://www.trademe.co.nz/a/property/residential` (trademe.co.nz/property redirects here) — ~39k listings (2026-04 research figure, no source attached, not re-confirmed — listing platform ⚠️; the archived search page below shows no total count, so read the live search count; for scale, REINZ national inventory from realestate.co.nz month-end data was 34,001 at end-Sep 2026, see below); self-described "New Zealand's largest range of houses and properties for sale" (listing platform ⚠️, [Trade Me — Houses & properties for sale](https://www.trademe.co.nz/a/property/residential/sale), archived 2026-10-26)
- **realestate.co.nz**: `https://www.realestate.co.nz` — industry-owned: launched in 1996 as a 50/50 joint venture between REINZ and the Auckland Multiple Listed Bureau; in 2005 PPL (Property Page Limited — Bayleys, Barfoot & Thompson, Ray White, Harcourts, LJ Hooker) joined the shareholding (self-described, [realestate.co.nz — About us](https://realestate.co.nz/about/about-us), archived 2026-07-06; the current shareholding split is not stated there). National inventory 34,001 listings at end-Sep 2026 (+10.7% YoY), from realestate.co.nz month-end data (Sep 2026 data, source [REINZ — September 2026 property report release](https://www.reinz.co.nz/Web/Web/News/News-Articles/Market-updates/Measured_national_picture_continues_alongside_strong_regional_results.aspx))
- **OneRoof** (NZME, publisher of the NZ Herald) — secondary
- **Homes.co.nz** — sold-price specialty

### 2026 price benchmarks (REINZ + QV, September 2026)

| Region | Value (NZD) | Change |
|---|---:|---:|
| **National median (REINZ)** | $755,000 | -2.3% YoY |
| **National HPI (REINZ)** | 3,551 (index) | -1.5% YoY |
| **National average value (QV)** | $892,580 | -0.9% YoY; -1.5% qtr |
| **Auckland region (Tāmaki Makaurau)** | $1,159,440 (QV avg) | -2.9% YoY (QV); REINZ median -2.6% YoY |
| **Wellington City** | $872,174 (QV avg) | **-5.2% YoY** (QV); Wellington region HPI -4.5% YoY (REINZ) |
| **Christchurch (Ōtautahi)** | $805,275 (QV avg) | +4.3% YoY (QV) |
| **Canterbury region** | $715,000 (REINZ median) | +0.8% YoY; HPI +3.1% YoY (REINZ) |
| **Hamilton** | $776,357 (QV avg; release text prints $776,537) | -0.3% YoY (QV) |
| **Tauranga** | $1,050,221 (QV avg) | +2.5% YoY (QV) |
| **Dunedin** | $652,943 (QV avg) | +3.0% YoY (QV) |
| **Queenstown Lakes** | $1,994,461 (QV avg) | +5.7% YoY (QV) |

September 2026 data, sources: [REINZ — September 2026 property report release](https://www.reinz.co.nz/Web/Web/News/News-Articles/Market-updates/Measured_national_picture_continues_alongside_strong_regional_results.aspx) (14 Oct 2026); [QV House Price Index — September 2026](https://www.qv.co.nz/news/qv-house-price-index-september-2026-housing-market-showing-few-signs-of-spring-uplift/) (12 Oct 2026) + QV district series at `https://www.qv.co.nz/price-index/`. REINZ = median of the month's sales (regions); QV = average value from the QV House Price Index (cities / districts) — the two measures are not interchangeable.

### Compute

1. NZD/sqm = price / **floor area** (sqm dominant unit)
2. Cross-check **REINZ HPI** + **QV** + **Trade Me sold-price**
3. **HPI vs median**: REINZ HPI uses the SPAR (Sales Price to Appraisal Ratio) method, accounts for changes in the composition of homes sold (land area, floor area, bedrooms) and dates sales at unconditional; the raw median moves with the sales mix, so the two can diverge (Sep 2026: median -2.3% YoY vs HPI -1.5% YoY) (2026 data, source [REINZ HPI](https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx))
4. **Wellington City ~-30.6% (computed)** from its QV HPI peak: index 2,512.7 (Jan 2022, avg value $1,256,674) → 1,743.9 (Sep 2026, avg value $872,174); Auckland region ~-24.8% (computed) over the same window (2026 data, source [QV House Price Index](https://www.qv.co.nz/price-index/) district series)
5. **Convert NZD to EUR/USD** at current FX

### Key terms

- RT (Record of Title) = land title
- Cross-lease = shared title with flat plan (Auckland-specific quirk)
- Body Corporate = HOA for unit title
- LIM = Land Information Memorandum (council report)
- Bright-line = capital gains test

---

## Section: `--traffic`

### Sources

- **NZTA (Waka Kotahi) Traffic Counts**: `https://www.nzta.govt.nz/resources/state-highway-traffic-volumes`
- **AADT + heavy-vehicle %** per state-highway count site, with the last 5 years of AADT (fields `aadt1yearago`…`aadt5yearsago`, `percentheavy`): NZTA open data [State highway traffic monitoring sites](https://opendata-nzta.opendata.arcgis.com/datasets/b90f8908910f44a493c6501c3565ed2d) (CC BY 4.0, dataset updated 2026-10-09) + public map [State highway traffic monitoring – annual average daily traffic](https://experience.arcgis.com/experience/a09cd3ec9bdd4068b45c818a69601775/) (count sites + estimated traffic between sites); dual-loop counts carry a 2–5% error margin and AADT accuracy depends on sampling frequency (2026 data, source NZTA open data)
- **Council traffic data** for local roads

### Key term

**AADT** — same as US/UK.

### Verdict bands

- 🟢 < 1,000 v/d (residential, rural)
- 🟡 1,000–8,000 v/d (suburban arterial)
- 🟠 8,000–25,000 v/d (urban arterial, SH-routes)
- 🔴 > 25,000 v/d (motorways: SH1, SH16, SH20)

---

## Section: `--tax`

### Annual property tax — Council Rates

Rates = **general rate × Capital Value (CV) or Land Value (LV)** + targeted rates.

**No central property tax** — rates are local-authority-only.

| City | Council rates, residential — 2026/27 rating year unless the row says otherwise |
|---|---:|
| Auckland Council | $4,375.12 for the average-value home (CV $1,281,500) — ≈0.34% of CV (computed: 4,375.12 / 1,281,500); +7.9% on 2025/26 ($4,054.96; computed: 4,375.12 - 320.16 = 4,054.96) |
| Wellington City Council | 0.341964 cents per $ of CV incl. GST (general 0.313034 + sector targeted 0.02893) — $3,419.64 on a $1,000,000 CV; excludes the sludge levy, Greater Wellington Regional Council rates (+9.7% average, collected on the WCC invoice) and water (billed by Tiaki Wai from 1 Jul 2026); WCC rates +5.9% average, which includes a 2% average sludge-levy increase |
| Christchurch City Council | $4,547.11 incl. GST for the average-value home in the draft plan (+7.4% on $4,231.84); $5,307.12 on a $1,000,000 2025 CV (≈0.53%, computed: 5,307.12 / 1,000,000); excludes Environment Canterbury rates; adopted: 7.35% for homeowners (secondary) |
| Queenstown Lakes | ~0.45% (median ~$5,500) — 2024-2025 est., not re-verified — rates/figures may have changed since; verify at `https://www.qldc.govt.nz/services/rates` |

2026 data, sources: Auckland — [AK Have Your Say — Changes to rates, fees and charges](https://akhaveyoursay.aucklandcouncil.govt.nz/annual-plan-2026-2027/changes-rates-fees-charges) (Annual Plan 2026/2027 consultation figure) + [OurAuckland — final rates increase adopted](https://ourauckland.aucklandcouncil.govt.nz/news/2026/07/auckland-council-secures-sustainable-rates-pathway-while-funding-crucial-infrastructure/) (1 Jul 2026: 7.9% for the average-value residential property, as proposed; archived 2026-07-02); Wellington — [WCC — Rates for 2026/2027](https://wellington.govt.nz/property-rates-and-building/rates/rates-explained/rates-for-current-rating-year) + its rates-in-the-dollar PDF (2026/27 rates use the 1 Sep 2024 revaluation; next city-wide revaluation 2027); Christchurch — [CCC Draft Annual Plan 2026/27 — rates proposal](https://letstalk.ccc.govt.nz/annualplan/how-we-propose-fund-activities-services-and-projects) (draft, Feb 2026) + adopted 7.35% per [Chris Lynch Media](https://www.chrislynchmedia.com/news-items/christchurch-homeowners-face-7-35-percent-rates-rise-as-council-backs-cathedral-funding/) (24 Jun 2026, secondary). Fixed per-property charges make the effective % of CV fall as CV rises (CCC draft: $1,874.81 on a $300,000 CV = 0.62% vs $24,920.30 on $5,000,000 = 0.50%); a specific property's rates are on the council's property search.

**Rates rising, not frozen, at the three city councils above for 2026/27**: average increases Auckland +7.9% (average-value residential), Wellington City +5.9% (WCC rates only, incl. the sludge-levy rise), Christchurch +7.35% for homeowners as adopted (secondary; +7.4% in the draft) (2026 data, sources above). Other councils: check the council's annual plan.

**Auckland — short-term letting shifts the rating category**: peer-to-peer STR moves the property onto a graduated business-rating share of general rates + CATTR once it is let 29+ nights in the 1 Jul – 30 Jun year; the Accommodation Provider Targeted Rate (APTR) itself has been suspended since 2020 and is NOT reinstated for 2026/2027. Bands and deadlines in `--rental` § Auckland (2026-08-07 verified, source: [Auckland Council — Accommodation Provider Targeted Rate](https://www.aucklandcouncil.govt.nz/en/property-rates-valuations/accommodation-provider-targeted-rate.html))

### Transaction taxes

- **NO STAMP DUTY**: stamp duty, including conveyance duty on land transfers (Part 2 of the Stamp and Cheque Duties Act 1971), was repealed on 20 May 1999 by s 6 of the Stamp Duty Abolition Act 1999 (1999 No 61) (sources: [legislation.govt.nz — Stamp and Cheque Duties Act 1971](https://legislation.govt.nz/act/public/1971/0051/latest/whole.html), version as at 1 Apr 2025, archived 2025-11-19; [Stamp Duty Abolition Act 1999](https://www.legislation.govt.nz/act/public/1999/61/en/latest/), archived 2026-08-04). The Real Estate Authority's list of additional buying costs names lawyer / conveyancer fees, LIM + building inspection reports, bridging finance and moving costs — no transfer duty among them (2026 data, source: [settled.govt.nz — Thinking about your finances](https://www.settled.govt.nz/buying-a-home/thinking-of-buying/thinking-about-your-finances-when-buying/)). Te Pāti Māori proposes a 5% residential stamp duty (election proposal only — see § Future risk)
- Legal fees: ~$1,500–$3,000 est. (2026-04 research range, no primary source; calibration: a listing-platform guide gives "Lawyer's fees ($800+)" — Trade Me ⚠️, 2024 data, updated 29 Oct 2024 — rates/figures may have changed since); get quotes from a lawyer or registered conveyancer
- LIM report: set by each council — e.g. $575.50 residential at Wellington City Council (2026/27, incl. GST; fast-track +$288) (2026 data, source: [WCC Annual Plan 2026/27 — fees and user charges](https://wellington.govt.nz/-/media/news-and-events/news-and-information/news/files/2026/annual-plan-2026-27-fees-and-user-charges.pdf)); other councils differ — check the council's fees schedule
- Building report: ~$400–$1,000 est. for a standard home (no primary source; inspection firms publish $299–$800 ⚠️ ([Alert Building Inspections](https://alertbuildinginspections.co.nz/building-inspection-costs-explained), 26 Oct 2026), $400–$800 ⚠️ ([Jim's Building Inspections](https://jimsbuildinginspections.co.nz/blog/importance-of-pre-purchase-building-inspection-in-new-zealand), 17 Jun 2025) and $450–$1,000 ⚠️ ([NZ Building Inspections](https://nzbuildinginspections.com/common-building-defects-found-in-nz-homes), undated); price varies with size, age and location; Trade Me guides give around $550 for a standard report, within $350 to over $1,000 ⚠️ ([Trade Me — building report costs](https://www.trademe.co.nz/c/property/article/Building-report-cost-in-nz-)), and "from $400" ⚠️, 2024 data, updated 29 Oct 2024 — rates/figures may have changed since)

### Capital gains tax — BRIGHT-LINE TEST

**No general CGT in NZ** (Labour proposes a 28% CGT from 1 Jul 2027 — election proposal only, see § Future risk). But the **bright-line test** taxes residential property gains as ordinary income IF sold within the bright-line period:

| Bright-line period | When applicable |
|---|---|
| **2 years** | Property sold on/after 1 Jul 2024 (current; was 5/10) (2026-10-23 verified, source: [IRD — bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test)) |
| 5 years | Acquired 29 Mar 2018 – 26 Mar 2021, sold before 1 Jul 2024 (2026 data, source: [IRD — property sold before 1 July 2024](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/property-sold-before-1-july-2024), updated 21 Aug 2025) |
| 10 years (5 for qualifying new builds) | Acquired on/after 27 Mar 2021, sold before 1 Jul 2024 (2026 data, same IRD page) |
| 2 years | Acquired 1 Oct 2015 – 28 Mar 2018 — the first bright-line test, in force from 1 Oct 2015 (source: [IRD Tax Technical — QB 17/02](https://www.taxtechnical.ird.govt.nz/questions-we-ve-been-asked/2017/qb-1702-income-tax-date-of-acquisition-of-land-and-start-date-for-2-year-bright-line-test), issued 30 Mar 2017; replaced by QB 25/10 + QB 25/11 for disposals on/after 1 Jul 2024) |

- Bright-line period (standard purchase/sale) starts when title transfers to the buyer (generally settlement) and ends when the seller enters a binding sale and purchase agreement; off-the-plan and gifts follow different rules (2026-10-23 verified, source: [IRD — bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test))
- Main home exclusion (sales on/after 1 Jul 2024): applies only if the property was used as the main home for more than 50% of its area AND more than 50% of the bright-line period; not available if already used twice in the 2 years before the sale (2026-10-23 verified, source: [IRD — exclusions](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/exclusions-to-the-brightline-test), updated 11 Sep 2024)
- Inherited property excluded; relationship-property settlements get rollover relief, as do certain transfers to associated persons and trusts (2026-10-23 verified, source: [IRD — ownership transfers and rollover relief](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/ownership-transfers-and-rollover-relief), updated 1 Apr 2026)

### GST

- **15%** when a GST-registered seller sells land as part of its taxable activity (IRD's example: a property developer selling a house); no GST when the seller is not GST-registered (e.g. a private owner reselling); generally no GST on the seller's main residence and its curtilage (unless GST was claimed on them); no GST on a dwelling used only as a residential rental for 5+ years (exempt supply); a sale between GST-registered parties is zero-rated (0%) only when the buyer will use the land to make taxable supplies and neither the buyer nor a relative intends to use it as their main residence (2026 data, sources: [IRD — GST on property transactions](https://www.ird.govt.nz/gst/charging-gst/gst-on-property-transactions) + flowchart IR730, May 2025; [IRD — exempt supplies](https://www.ird.govt.nz/gst/charging-gst/exempt-supplies), updated 1 Apr 2026)
- From **1 Apr 2024**: GST collected by online STR marketplaces at 15% (8.5% passed to non-GST-registered hosts) (2026-10-23 verified, source: [IRD — GST for listed services](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services), updated 14 Aug 2025)

### Interest deductibility (BTL)

**Fully restored 100% from 1 Apr 2025** (tax year ending 31 Mar 2026 onwards; 80% for 1 Apr 2024 – 31 Mar 2025) — major reversal of 2021 phase-out (2026-10-23 verified, source: [IRD — interest limitation rules](https://www.ird.govt.nz/property-interest-rules), updated 1 Apr 2026). Labour says it will not reinstate the interest denial; the Greens propose denying it again (election proposals only — see § Future risk).

### Foreign-buyer regime

**Overseas Investment Amendment Act 2018** — overseas persons need consent to buy residential land; holders of temporary, limited, interim or transit visas (student, work, visitor) and people with no visa cannot buy (2026-10-23 verified, source: [LINZ — Buying residential property to live in](https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live), updated 6 Mar 2026). Exceptions and pathways:
- AU + SG citizens — residential or lifestyle land without consent (treaty exemption); AU + SG permanent residents once ordinarily resident
- Residence class visa holders who are **ordinarily resident** (lived in NZ for at least the last 12 months + tax resident, present more than 183 days in the last 12 months); residence visa holders not yet ordinarily resident can apply for consent to buy or build one home
- Off-the-plan apartments in developments whose developer holds an exemption certificate (purchase before construction is complete) ([LINZ — Exemptions from the need for consent](https://www.linz.govt.nz/guidance/overseas-investment/apply-consent-variation-or-exemption/application-forms-and-information-sheets/exemptions-need-consent))
- **$5 million plus house pathway (in force 6 Mar 2026)**: Active Investor Plus, Investor 1 + Investor 2 resident visa holders can apply for consent to buy residential or lifestyle land (not otherwise sensitive — e.g. not on an island or beside a beach, river, lake or reserve) priced more than NZ$5m, or land + build where land + construction price exceeds NZ$5m; offer must be conditional on consent; interim fees NZ$2,040 (existing dwelling) / NZ$3,500 (all other cases); statutory timeframe 15 working days, LINZ aims for ~5 (2026-10-23 verified, sources: [LINZ — $5m pathway](https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/pathways-migrants-and-visa-holders/investing-residential-land-over-5-million), updated 27 Mar 2026; [LINZ — OIA reform](https://www.linz.govt.nz/our-work/overseas-investment-regulation/reform-overseas-investment-act), updated 28 Aug 2026; [Cabinet paper LEG-26-SUB-0001](https://www.treasury.govt.nz/sites/default/files/2026-05/cabinet-paper-leg-26-sub-0001.pdf)). Only one property per visa holder may be bought in reliance on the visa — any other such property must be sold first; where a partner also holds the visa, each visa may be relied on (2026 data, source: [LINZ — Detailed information for investor visa holders buying a house](https://www.linz.govt.nz/sites/default/files/doc/guidance-investor-visa-holders-long-form-march2026-v3.pdf), Mar 2026)

### Total transaction cost (buyer side)

- Resale: ~$2,500–$4,600 est. (computed, rounded to $100: legal ~$1,500–$3,000 est. + building report ~$400–$1,000 est. + LIM $575.50 at Wellington City Council; other councils' LIM fees differ) — no stamp duty on top (see § Transaction taxes)
- New build from a GST-registered developer: GST at 15% applies to the sale (see § GST) + the same fees

### Future risk

- **7 Nov 2026 general election** (Saturday 7 November 2026, source: [Electoral Commission — vote.nz](https://vote.nz/), archived 2026-10-23) **— party proposals only**: none is government policy, introduced or legislated; any change needs coalition agreement + legislation (per [Nexia — 2026 election tax policies](https://www.nexia.co.nz/2026-election-tax-policies-new-zealand/), 28 Sep 2026, secondary; [KPMG Election 2026 party tax policy tracker](https://assets.kpmg.com/content/dam/kpmgsites/nz/pdf/2026/09/2026-election-policy-tracker-v4.pdf), updated 3 Sep 2026, secondary)
  - **Labour**: 28% CGT on profit made after 1 Jul 2027 when residential investment or commercial property is sold; family home, farms, inheritances / gifts, KiwiSaver, shares, businesses + personal items excluded; will not reinstate the interest-deduction denial
  - **Greens**: restore the 10-year bright-line + deny landlord interest deductibility; Capital Acquisitions Tax (33%) on assets / gifts received over $1,000,000 (family homes + farms exempt); 2.5% tax on net assets above $10m (family homes exempt)
  - **Te Pāti Māori**: 5% stamp duty on residential sales (first-home buyers under $1m exempt); 33% land-banking tax; 2% vacant-house tax; wealth tax 1.5–2.5% on net assets above $2m
  - **Opportunity (TOP)**: annual land value tax 1.75% urban / 0.5% rural on unimproved land value
  - **National + ACT**: no capital gains tax planned; National campaigning on no new taxes
- Foreign-buyer ban remains for most overseas persons; the $5m+ investor-visa pathway (in force 6 Mar 2026) is the carve-out — see § Foreign-buyer regime

---

## Section: `--rental`

### Long-term residential

- **Residential Tenancies Act 1986** (RTA) — tenant-protective
- **No-cause 90-day termination RESTORED 30 Jan 2025** by Residential Tenancies Amendment Act 2024 (passed 17 Dec 2024), reversing the 11 Feb 2021 abolition; also adds 42-day notice for owner/family (or employee) occupation or sale-with-vacant-possession, and 21-day tenant termination; fixed terms can be ended by either side with 90–21 days' notice before expiry; pet-related changes effective 1 Dec 2025 (written landlord consent, refusable only on reasonable grounds; pet bond up to 2 weeks' rent on top of the regular bond) (2026-10-23 verified, source: [Ministry for Cities, Environment, Regions and Transport (formerly HUD) — RTA Amendment Act 2024](https://www.hud.govt.nz/our-work/residential-tenancies-amendment-act-2024))
- **Rent increases** capped at once every 12 months (12 months after the tenancy start or the last increase), with at least 60 days' written notice (2026 data, source [Tenancy Services — Rent increases](https://www.tenancy.govt.nz/rent-bond-and-bills/rent/increasing-rent/))
- **Rental loss ring-fencing** — excess residential rental deductions cannot be offset against other income such as salary or wages; they carry forward to years with residential rental income (2026 data, source [IRD — Residential rental property deductions](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-property-deductions))
- **Healthy Homes Standards** mandatory for rentals (insulation, heating, ventilation, moisture, draught) — all rental properties must comply (2026 data, source [Tenancy Services — Healthy homes](https://www.tenancy.govt.nz/healthy-homes/))
- **Market rent data**: Tenancy Services market rent tool (bond data) — lower-quartile / median / upper-quartile weekly rent by area, dwelling type and bedrooms; updated monthly from bonds lodged over the previous six months, excluding the most recent month (2026 data, source [Tenancy Services — Market rent](https://www.tenancy.govt.nz/rent-bond-and-bills/market-rent/))

### Short-let (Airbnb, Bachcare)

#### Queenstown Lakes

- **Residential Visitor Accommodation registration** required
- **Night cap is zone-specific**: e.g. Lower Density Suburban Residential allows a cumulative 90 nights/yr from initial registration (PDP ch.7 std 7.5.18.1, Jun 2023 Decisions Version; non-compliance = restricted discretionary); QLDC's rule sheet applies the same 90-night limit in the Medium Density Residential, Arrowtown Residential Historical Management and Large Lot Residential zones; operating beyond your zone's standards needs a resource consent - check the parcel's zone on QLDC ePlan (2026 data, sources [QLDC STVA](https://www.qldc.govt.nz/services/rates-property/short-term-visitor-accommodation); [QLDC — RVA rules, LDSR / MDR / ARHM / LLR zones](https://www.qldc.govt.nz/media/jj4hluqj/lower-density-suburban-residential-zone.pdf); [QLDC PDP ch.7, Decisions Version Jun 2023](https://www.qldc.govt.nz/media/jqvcbekq/pdp-chapter-07-lower-density-suburban-residential-jun-2023.pdf))
- **Rates**: no change if available to short-term guests for up to 28 days/yr cumulative; under 180 days = rated Mixed Use (+25-35%); 181-365 days = rated Accommodation (+50-80%); a Homestay = Mixed Use (+25-35%); changes apply from the next rating year beginning 1 Jul (2026 data, source [QLDC STVA](https://www.qldc.govt.nz/services/rates-property/short-term-visitor-accommodation))

#### Auckland

- Unitary Plan visitor accommodation rules
- **APTR (Accommodation Provider Targeted Rate) suspended since 2020 — NOT reinstated for 2026/2027.** The live cost is a **graduated general-rates + CATTR business uplift** on peer-to-peer STR booked for more than 28 nights, nights counted **1 Jul – 30 Jun** of the previous year (2026/2027 rates use nights booked 1 Jul 2025 – 30 Jun 2026); new providers who do not declare are assessed at the 29–135-night level (75% residential / 25% business) (2026 data, sources: [Auckland Council — Accommodation Provider Targeted Rate](https://www.aucklandcouncil.govt.nz/en/property-rates-valuations/accommodation-provider-targeted-rate.html); suspension year: [OurAuckland — Auckland Council welcomes APTR decision](https://ourauckland.aucklandcouncil.govt.nz/news/2023/05/auckland-council-welcomes-aptr-decision/), 12 May 2023, archived 2026-05-20)

| Nights let (1 Jul – 30 Jun) | Rating split |
|---|---|
| **up to 28** | stays 100% residential |
| **29–135** | 75% residential / 25% business |
| **136–180** | 50% residential / 50% business |
| **more than 180** | 100% business |

- **Declare before 1 Jul** to land on the first instalment bill (changes apply from 1 Jul and show on the August bill); **permanently stop operating and remove the listing before 30 Jun** to stay residential for the coming rating year (2026 data, source: Auckland Council APTR page above)
- Supreme Court upheld the original 2017/18–2018/19 APTR on **12 May 2023** (*Auckland Council v C P Group Ltd* [2023] NZSC 53, SC 158/2021: appeal allowed unanimously, Court of Appeal decision set aside and High Court decision reinstated; source [Supreme Court — media release](https://www.courtsofnz.govt.nz/assets/cases/2023/MR-2023-NZSC-53.pdf))

#### Other councils

- **Wellington City**: the 2026/27 Annual Plan (adopted 25 Jun 2026) adds a short-term accommodation general-rates differential of 2.6× the base rate (commercial differential: 3.7×); as consulted, it covers houses or units let, or available, for stays under one month for more than 60 days in the financial year, other commercial targeted rates still apply, and single rooms, granny flats, sleepouts and dual-key homes that do not meet the criteria are excluded (2026 data, sources [WCC — Annual Plan adopted](https://wellington.govt.nz/news-and-events/news-and-information/our-wellington/2026/06/wellington-city-confirms-lowest-rates-increase-in-six-years), 25 Jun 2026; [Let's Talk Wellington — Key proposal 1: Short-term accommodation](https://www.letstalk.wellington.govt.nz/mahere-tau-annual-plan-202627/key-proposal-1-short-term-accommodation)). Start date: 1News reports "from July next year" (read against its 12 Jul 2026 date: Jul 2027; secondary ⚠️, [1News](https://www.1news.co.nz/2026/07/12/short-term-accommodation-rate-hike-pressures-airbnb-owners-in-wellington/)); WCC's Rates for 2026/27 sheet shows no short-term accommodation category and no general rate at 2.6× the base ([WCC — Rates for 2026/27](https://wellington.govt.nz/-/media/property-rates-and-building/rates-and-property/rates/files/wellington-city-council-rates-2026-2027.pdf)) — verify with Wellington City Council rates
- **Christchurch**: District Plan Plan Change 4, rules effective 24 Jul 2023 — hosted visitor accommodation for up to 8 guests generally permitted in most residential and rural zones (notify Council, keep records); unhosted in residential zones up to 60 nights/yr without resource consent (max 8 guests, notify Council, keep records, appoint a local manager), more nights or guests need a resource consent; unhosted in rural zones up to 180 nights/yr; other rules apply in the airport noise contour and to heritage buildings (2023 rules, source [CCC Newsline — Final rules released for short-term visitor accommodation](https://newsline.ccc.govt.nz/news/story/final-rules-released-for-short-term-visitor-accommodation), 26 Jul 2023, archived 2025-05-15 — rates/figures may have changed since; verify at `https://www.ccc.govt.nz/consents-and-licences/resource-consents/residential-and-housing/providing-guest-accommodation`)

### Tax on rental

- Marginal income tax on net rental
- BTL interest fully deductible (from 1 Apr 2025; the interest limitation rules applied 1 Oct 2021 – 31 Mar 2025) (2026 data, source [IRD — Rental property expenses](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it/rental-expense-deductions))
- Bright-line test on sale
- **GST $60k threshold** — register if turnover from all GST activities is over $60,000; since 1 Apr 2024 online marketplaces (e.g. Airbnb, Bookabach, Holiday Houses) collect and pay GST on short-stay accommodation booked through them (2026 data, source [IRD — GST and renting out residential property](https://www.ird.govt.nz/property/renting-out-residential-property/gst-and-renting-out-residential-property))
- **Rental loss ring-fencing** — losses cannot offset other income

---

## Section: `--work=<profession>`

### Sources

- **Work and Income (WINZ)**: `https://www.workandincome.govt.nz/`
- **Trade Me Jobs**: `https://www.trademe.co.nz/a/jobs` (trademe.co.nz/jobs redirects here)
- **SEEK** — self-described "New Zealand's no. 1 Employment, Career and Recruitment site" (company claim ⚠️, no independent market-share source attached; archived 2026-09-29): `https://nz.seek.com/` (www.seek.co.nz redirects here, archived 2026-10-05)
- **JobSpace** (`https://jobspace.co.nz/`; myjobspace.co.nz redirects here; NZ-owned since 2006), **Indeed NZ** (`https://nz.indeed.com/`; indeed.co.nz redirects here), **LinkedIn NZ**; JobAve ❌ DEPRECATED — jobave.co.nz does not resolve (dead on 2026-10-23); verify with Seek / Trade Me Jobs
- **Immigration New Zealand** (work visas for migrants): `https://www.immigration.govt.nz/`

### Self-employment

- **Sole trader**: IRD + GST (registration required once turnover was at least $60,000 in the last 12 months or is expected to reach it in the next 12) (2026 data, source: [IRD — Registering for GST](https://www.ird.govt.nz/gst/registering-for-gst), updated 13 Feb 2025)
- **Limited company**: Companies Office; must have at least one shareholder and issue at least one share — no minimum capital amount is stated (2026 data, source [Companies Office — Issuing shares in a company](https://companies-register.companiesoffice.govt.nz/help-centre/starting-a-company/issuing-shares-in-a-company/))
- **Working for Families** tax credits

### Salary benchmarks (2025 est.)

- Median annual gross (est. ranges, no primary source for the city splits — verify against Stats NZ Labour market statistics (income) and current Seek / Trade Me Jobs salary data; 2025 data — rates/figures may have changed since). Calibration anchor: national median weekly earnings from wages and salaries (all wage and salary earners, part-time included) were $1,419 in the June 2026 quarter (+2.8% YoY), ≈ $73,800/yr (computed: $1,419 × 52); median hourly earnings $35.96 (full-time $38.00, part-time $28.49) (2026 data, source [Stats NZ — Labour market statistics (income): June 2026 quarter](https://www.stats.govt.nz/information-releases/labour-market-statistics-income-june-2026-quarter/)). Full-time median hourly earnings of $38.00 give ≈ $79,040/yr (computed: $38.00 × 40 × 52 = $79,040, assuming a 40-hour week). Regional medians, part-time included, as MoneyHub reports them from Stats NZ's New Zealand Income Survey, June 2025 release: Wellington $76,544, Auckland $72,800, Canterbury $69,836, Bay of Plenty $66,924, Waikato $66,560 ([MoneyHub](https://www.moneyhub.co.nz/average-salary-new-zealand.html) ⚠️, updated 11 Jan 2026, 2025 data — rates/figures may have changed since). MoneyHub says its table covers employees and the self-employed, a wider group than the wages-and-salaries medians above, so the two series do not compare directly. Its national median of $69,836 equals Stats NZ's June 2024 quarter wages-and-salaries median (computed: $1,343 × 52 = $69,836), but that does not show these figures are a year older than labelled: MoneyHub's figure for 2024, $68,068 (computed: $1,309 × 52 = $68,068), matches neither Stats NZ's June 2024 quarter ($1,343) nor its June 2023 quarter ($1,273) ([Stats NZ — Labour market statistics (income): June 2024 quarter](https://www.stats.govt.nz/information-releases/labour-market-statistics-income-june-2024-quarter), 2024 data — rates/figures may have changed since). Stats NZ's own regional table (Aotearoa Data Explorer, "Earnings for people in paid employment by region, sex, age groups and ethnic groups") could not be read for verification on 2026-11-05 — check it directly. MoneyBalance gives lower figures (Auckland $68,000, Wellington $75,000, Canterbury $63,000, Waikato $60,000, Bay of Plenty $62,000), but by its own note they are approximate and not tied to a named published dataset, so MoneyHub's are used here ([MoneyBalance](https://moneybalance.co.nz/income/average-salary-new-zealand) ⚠️, updated Oct 2026). The city ranges below are unsourced est. positions, not published regional medians; the three main-centre ranges sit above these regional medians:
  - Auckland: ~$80,000–$110,000 est.; regional median $72,800 ⚠️ (MoneyHub, from Stats NZ)
  - Wellington (govt): ~$85,000–$120,000 est.; regional median, all sectors, $76,544 ⚠️ (MoneyHub, from Stats NZ)
  - Christchurch / Hamilton / Tauranga: ~$70,000–$95,000 est.; regional medians $66,560–$69,836 ⚠️ (MoneyHub, from Stats NZ)
  - Smaller cities: ~$60,000–$80,000 est.; other regions' medians $63,232–$72,800 ⚠️ (MoneyHub, from Stats NZ)
- **Minimum wage**: **$23.95/hr from 1 Apr 2026** (previously $23.50, +45c); starting-out and training minimum wages $19.16/hr (2026-10-23 verified, source: [Employment NZ — Minimum wage rates and types](https://www.employment.govt.nz/pay-and-hours/pay-and-wages/minimum-wage/minimum-wage-rates-and-types); [MBIE — Minimum wage set for 2026](https://www.mbie.govt.nz/about/news/minimum-wage-set-for-2026))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **GeoNet** | `https://www.geonet.org.nz` | Earthquake / volcano / tsunami real-time |
| **Earth Sciences NZ** (GNS Science + NIWA merged 1 Jul 2025) | `https://www.earthsciences.nz` (legacy GNS site `https://www.gns.cri.nz` still linked from it) | National Seismic Hazard Model (2022 revision: shaking hazard up throughout most of the country — on average by 50% or more vs previous modelling, from almost no change to more than doubling in some areas; source [GNS Science — NSHM](https://www.gns.cri.nz/research-projects/national-seismic-hazard-model/), archived 2026-10-05) |
| **Natural Hazards Commission Toka Tū Ake** (formerly EQC) | `https://www.naturalhazards.govt.nz` | NHCover up to **$300,000 +GST** residential building cap per natural-hazard event (2026 data, source [NHC — About NHCover](https://www.naturalhazards.govt.nz/insurance-and-claims/about-nhcover/)) |
| **Natural Hazards Portal** (NHC Toka Tū Ake) | `https://www.naturalhazardsportal.govt.nz/` | Look up natural hazard insurance property claims across NZ (settled-claims map), incl. whether a home has had an NHC claim; natural hazard maps for Bay of Plenty only (pilot), more regions to be added as they become available (2026 data, source [Natural Hazards Portal](https://www.naturalhazardsportal.govt.nz/) + [settled.govt.nz — Natural hazards](https://www.settled.govt.nz/buying-a-home/researching-the-property/understanding-the-impact-of-natural-hazards/)) |
| **NIWA** (part of Earth Sciences NZ since 1 Jul 2025) | `https://niwa.co.nz` | Climate, flood, drought, sea-level rise |
| **Council hazard information** | per council | The local council should have hazard information for the property — some may be free of charge, or order a LIM; some councils may provide flood maps (2026 data, source [settled.govt.nz — Natural hazards](https://www.settled.govt.nz/buying-a-home/researching-the-property/understanding-the-impact-of-natural-hazards/)); council map-tool names (curated: Auckland Hazard Viewer, Wellington Hazards Mapper) not confirmed — check the council's website |

### Specific risks

#### Earthquake — EXTREME

- **NZ sits on Pacific Ring of Fire / plate boundary**
- **National Seismic Hazard Model, 2022 revision**: likelihood of future earthquake shaking increased throughout most of the country — on average by 50% or more vs previous modelling, ranging from almost no change to more than doubling in some areas; the NSHM does not describe impact or assess risk (source [GNS Science — NSHM](https://www.gns.cri.nz/research-projects/national-seismic-hazard-model/), archived 2026-10-05; model outputs freely available at `https://nshm.gns.cri.nz`)
- **Historical major events**:
  - **Christchurch (Canterbury) 2010-11** (M7.1 Darfield 4 Sep 2010 + ML 6.3 Christchurch 22 Feb 2011 — 185 deaths, per [GeoNet](https://www.geonet.org.nz/earthquake/story/3468575); rebuild cost $40B — Treasury estimate announced by the Prime Minister on 28 Apr 2013 for Budget 2013, covering capital costs incurred by the Government and private business (2013 data, source [RNZ, 28 Apr 2013](https://www.rnz.co.nz/news/emergencies_national/133745/christchurch-rebuild-cost-put-at-$40b) — secondary, not confirmed on a Treasury page; rates/figures may have changed since; verify with Treasury `https://www.treasury.govt.nz`); insurer claims only, accumulated 2010-2011: NZ$22.9B excl. GST, NZ$32.0B inflation-adjusted (2026 data, source [ICNZ (insurance-industry body) — Cost of natural disasters](https://www.icnz.org.nz/industry/cost-of-natural-disasters/)))
  - **Kaikōura 2016** (M7.8, 14 Nov 2016 — fault rupture; local tsunami with 6.9 m run-up at Goose Bay, per [GeoNet](https://www.geonet.org.nz/earthquake/story/2016p858000); port damage; insured losses NZ$2.27B (2026 data, source [ICNZ (insurance-industry body) — Cost of natural disasters](https://www.icnz.org.nz/industry/cost-of-natural-disasters/)))
  - **Hawke's Bay 1931** (Mw 7.4–7.6 / Ms 7.8 — 256 killed, the largest loss of life of any NZ earthquake, per [GeoNet](https://www.geonet.org.nz/earthquake/story/2178228))
- **Wellington Fault** (Wellington–Hutt Valley segment): estimated rupture probability ~11% in the next 100 years (sensitivity results 4–15%) and ~5% in the next 50 years; the new data cut earlier estimates by ~50% or more (2011 data, source [NZSEE Bulletin Vol. 44 No. 2 — Rhoades, Van Dissen et al. (GNS Science)](https://bulletin.nzsee.org.nz/article/view/238), peer-reviewed — rates/figures may have changed since); curated wording "high probability of a major event in coming decades" (superseded); for the location's shaking likelihood see the NSHM (`https://nshm.gns.cri.nz`)
- **Auckland**: lower earthquake risk (curated — volcanic field replaces tectonic faults; not confirmed against a primary source; check site-specific shaking likelihood in the NSHM)
- **NHCover** natural-disaster cover, automatic with a home insurance policy that includes fire — covers up to **$300,000 +GST** building damage per event; land cover is limited (generally land within 8 m of the home + the main access way up to 60 m; retaining walls capped at $50,000 +GST, bridges/culverts at $25,000 +GST) (2026 data, source [NHC — About NHCover](https://www.naturalhazards.govt.nz/insurance-and-claims/about-nhcover/))

#### Volcanic

- **Taupō Volcanic Zone** — Taupō volcano last erupted ~1,800 years ago, "the most violent eruption in the world in the last 5,000 years" (2026 data, source [GeoNet — Taupō](https://www.geonet.org.nz/about/volcano/taupo))
- **Mount Ruapehu**: active stratovolcano (Whakapapa ski field); most recent eruption 25 Sep 2007; Crater Lake water ejected in eruptions causes lahars (2026 data, source [GeoNet — Ruapehu](https://www.geonet.org.nz/about/volcano/ruapehu))
- **Auckland Volcanic Field**: 53 volcanic centres; most recent eruption Rangitoto ~600 years ago; existing volcanoes are unlikely to reactivate but the field itself is young and still active — an eruption is low-probability, high-consequence (2026 data, source [GeoNet — Auckland Volcanic Field](https://www.geonet.org.nz/about/volcano/aucklandvolcanicfield))
- **Whakaari/White Island**: fatal explosive eruption at 2:11pm on 9 Dec 2019 — some visitors and guides on the island were killed (source [GeoNet — Whakaari](https://www.geonet.org.nz/about/volcano/whiteisland)); of the 47 people on the island, 22 were killed and 25 harmed (source [WorkSafe, 30 Nov 2020](https://www.worksafe.govt.nz/about-us/news-and-media/13-parties-charged-by-worksafe-new-zealand-over-whakaariwhite-island-tragedy/) + [WorkSafe statement on sentencing, 1 Mar 2024](https://www.worksafe.govt.nz/about-us/news-and-media/statement-on-sentencing-of-whakaari-defendants/))

#### Tsunami

- About 10 tsunami higher than 5 m have hit NZ since 1840 — some from distant earthquakes, most from seafloor earthquakes not far from the coast; people who see the sea recede may have as little as 5 minutes to reach higher ground (2026 data, source [GeoNet — Tsunami FAQ](https://www.geonet.org.nz/tsunami/faq)); Kaikōura 2016 generated a local tsunami (see Earthquake)
- Higher-exposure coasts (curated: East Coast, Cook Strait, Bay of Plenty) — not confirmed against a national primary source; check the regional Civil Defence tsunami evacuation maps
- Tsunami evacuation zones: check the property against the council / regional Civil Defence tsunami evacuation zone map; the curated claim that the zones are "mandatory" is not confirmed against a primary source — verify with NEMA (`https://getready.govt.nz`)

#### Flood + landslip

- Auckland Anniversary Weekend floods, 27 Jan – 2 Feb 2023 (state of emergency; insured losses NZ$1.98B over 59,189 claims, excl. GST; claims to 1 Mar 2024, source [ICNZ (insurance-industry body) — Cost of natural disasters](https://www.icnz.org.nz/industry/cost-of-natural-disasters/), table as published 2026)
- Cyclone Gabrielle, 11–17 Feb 2023 (Hawke's Bay, Tairāwhiti; insured losses NZ$1.84B over 58,848 claims, excl. GST; claims to 1 Mar 2024, source ICNZ)
- The frequency and severity of storms and cyclones bringing heavy rainfall, damaging winds, waves and storm surge to NZ has increased (2026 data, source [settled.govt.nz — Natural hazards](https://www.settled.govt.nz/buying-a-home/researching-the-property/understanding-the-impact-of-natural-hazards/))
- Steep terrain landslip risk (Kaikoura, Wellington)

#### Coastal erosion + sea-level rise

- Projected sea-level rise 0.55 m (RCP4.5) to 0.79 m (RCP8.5) by 2090, 1.05 m under RCP8.5+ allowing for ice-sheet instability (IPCC AR5-era projections on an undated page, identical in all 7 NIWA regional zone snapshots; source [NIWA — Climate Change Adaptation Toolbox, Zone 1](https://niwa.co.nz/climate-change-adaptation-toolbox/projected-regional-climate-change-hazards/regional-projections-zone-1) — rates/figures may have changed since)
- Coastal Hazards Susceptibility (per council mapping)
- Site-specific sea-level rise projections to 2300 for every 2 km of coast, combined with vertical land movement (subsidence / uplift): NZ SeaRise programme ([searise.nz](https://searise.nz/), online tool by Takiwā) (2026 data, source [NIWA — Sea-level rise](https://niwa.co.nz/hazards/sea-level-rise))

### Build-era hazards

| Era | Hazards |
|---|---|
| **1980s or earlier** | Lead-based paint: presume a building built in the 1980s or earlier has been painted with lead-based paint; no abrasive blasting of properties built or painted before 1970 (2026 data, source [Health NZ — Lead-based paint](https://www.healthnz.govt.nz/health-topics/keeping-healthy/healthy-homes-environments/hazardous-substances/lead/lead-based-paint)); lead pipes: no NZ primary source confirmed — ask the building inspector / plumber |
| **Mid-1940s–mid-1980s** (any pre-2000 build) | Asbestos: popular building material mid-1940s to mid-1980s (settled.govt.nz); a building built before 1 Jan 2000 probably contains some asbestos materials (2026 data, source [WorkSafe — Where asbestos can be found](https://www.worksafe.govt.nz/topic-and-industry/asbestos/where-asbestos-can-be-found/)) |
| **Late 1970s–early 1980s** | Dux Quest plumbing (built or re-plumbed late 1970s–early 1980s; prone to leaking) + Weatherside cladding (popular early 1980s; prone to swelling and rot — the only full fix is replacing the cladding) (2026 data, source [settled.govt.nz — Problem building materials](https://www.settled.govt.nz/buying-a-home/researching-the-property/learning-about-problem-building-materials/)) |
| **Late 1980s–mid-2000s** | **Leaky homes crisis** — high-risk builds are mostly plaster-style monolithic cladding, especially Mediterranean style without eaves and with flat roofs: water ingress + rot (2026 data, source [settled.govt.nz — Leaky buildings](https://www.settled.govt.nz/buying-a-home/researching-the-property/learning-about-leaky-buildings/)); a review of the size and cost of the problem estimated 42,000 homes likely to be leaky, with a total economic cost (repair + transaction costs) to remediate them that could be $11.3B — the Department of Building and Housing commissioned PricewaterhouseCoopers to study the problem (2010 data, source [DBH Regulatory Impact Statement — leaky homes financial assistance package](https://regulation.govt.nz/assets/RIS-Documents/ris-dbh-faplh-nov10.pdf) — rates/figures may have changed since) |
| **Building Code E2 / H1** | Weathertightness is clause E2 External moisture (E2/AS1 4th edition effective 28 Jul 2025), not H1; H1 is energy efficiency — MBIE flagged new roof, window, wall and underfloor insulation requirements in Oct 2022; H1/AS1 6th edition effective 27 Nov 2025, 5th edition (from 4 Aug 2022) usable until 26 Nov 2026 (source [building.govt.nz — E2](https://www.building.govt.nz/building-code-compliance/e-moisture/e2-external-moisture/) + [H1](https://www.building.govt.nz/building-code-compliance/h-energy-efficiency/h1-energy-efficiency/), archived 2026-01-13 / 2026-06-23); the date the post-leaky-homes E2 rules took effect is not confirmed — verify at building.govt.nz |
| **Rentals (any era)** | Ceiling and underfloor insulation compulsory in all rental homes since 1 Jul 2019; all private rentals must meet the healthy homes standards (heating, insulation, ventilation, moisture ingress and drainage, draught stopping) from 1 Jul 2025 (2026 data, source [Tenancy Services — Healthy homes compliance](https://www.tenancy.govt.nz/healthy-homes/healthy-homes-compliance/)) |
| **Cross-lease titles** | Buyer becomes part owner of every building on the plot with the other leaseholders; leases usually 999 years; structural changes need all owners' agreement; check the title's footprint plan matches the buildings (source [settled.govt.nz — Cross lease ownership](https://www.settled.govt.nz/blog/what-you-need-to-know-about-cross-lease-ownership/), 1 Nov 2018 article); cross leases were 18% of all Auckland titles (100,148 titles, 47% of NZ's 215,958) and 18% of Christchurch titles, on LINZ title data as at 15 Mar 2016 (2016 data, source [Auckland Council technical report TR2017/025](https://knowledgeauckland.org.nz/media/xigdqs5h/tr2017-025-arrested-redevelopment-cross-lease-unit-titles-auckland.pdf), Oct 2017 — rates/figures may have changed since); curated ~10% Auckland (superseded) |

### Mandatory at sale

| Document | Notes |
|---|---|
| **LIM (Land Information Memorandum)** | From council; fee set by each council (fast-tracking may cost extra), processing may take several days; does not show issues the council has not been told about, e.g. an unreported weathertightness problem (source [settled.govt.nz — What is a LIM report](https://www.settled.govt.nz/blog/what-is-a-lim-report/), 4 Apr 2019 article); e.g. Tauranga City Council residential LIM $395 (10-day email service) or $680 (5-day), incl. GST (2026 data, source [Tauranga City Council — LIM fees, as at 1 Jul 2026](https://www.tauranga.govt.nz/council/fees-and-charges/land-information-memoranda-fees)); ~$300–500 est. for a standard residential LIM elsewhere — calibrated on Tauranga's $395 only, fees vary by council and urgency; check the council's fees and charges; mandatory in practice |
| **Project Information Memorandum (PIM)** | For consents (build/extension) |
| **Body Corporate disclosure** | Unit title only |
| **Vendor warranty re weathertightness** | Leaky-building disclosure expected |
| **Healthy Homes Compliance Statement** | If letting out |

### Climate change projections

- **Temperature**: annual average air temperature +1.3–1.4°C (RCP4.5) to +2.8–3.1°C (RCP8.5) by 2090 (IPCC AR5-era downscaled projections, identical in all 7 NIWA regional zone snapshots; source [NIWA — Climate Change Adaptation Toolbox, Zone 1](https://niwa.co.nz/climate-change-adaptation-toolbox/projected-regional-climate-change-hazards/regional-projections-zone-1)); NIWA completed updated CMIP6-based national projections (SSP1-2.6 to SSP5-8.5, to 2100) in mid-2024, data published by MfE — newer figures may differ, verify at [NIWA — Updated national climate projections](https://niwa.co.nz/climate-and-weather/updated-national-climate-projections-new-zealand)
- **Sea-level rise**: 0.55 m (RCP4.5) / 0.79 m (RCP8.5) / 1.05 m (RCP8.5+, allowing for ice-sheet instability) by 2090; 0.24 / 0.28 / 0.37 m by 2040 (IPCC AR5-era projections on an undated page, source [NIWA — Climate Change Adaptation Toolbox, Zone 1](https://niwa.co.nz/climate-change-adaptation-toolbox/projected-regional-climate-change-hazards/regional-projections-zone-1) — rates/figures may have changed since); site-specific figures incl. vertical land movement: NZ SeaRise (see Coastal erosion above)
- **Heavy rainfall**: short-duration extremes (1-in-100-year, 1-hour) +13.6% and long-duration events (1-in-2-year, 120-hour) +4.8% per 1°C of warming (source [NIWA — Climate Change Adaptation Toolbox, Zone 1](https://niwa.co.nz/climate-change-adaptation-toolbox/projected-regional-climate-change-hazards/regional-projections-zone-1)); est. at the 2090 warming above, linear scaling: ≈ +18–19% (RCP4.5: 13.6% × 1.3–1.4°C) to ≈ +38–42% (RCP8.5: 13.6% × 2.8–3.1°C) for 1-hour 1-in-100-year rainfall — local changes vary; extreme rainfall from ex-tropical cyclones up to ~30–35% higher by end of century under a high-emissions scenario (~3°C warming) (2025 data, source [Earth Sciences NZ, 7 Aug 2025](https://www.earthsciences.nz/news/rain-from-tropical-cyclones-to-increase-under-warmer-climate))
- **Drought**: NIWA's regional snapshots give two different figures — time spent in drought in eastern and northern NZ projected to double or triple by 2040 (RCP4.5, ~2050) (Zone 1 notes), but +5–20% time spent in drought, with drought probability up 50–70% (Zone 1 at 2090 under RCP8.5; Zone 3, eastern lower North Island, notes); the pages do not explain the gap (IPCC AR5-era projections, source [NIWA — Zone 1](https://niwa.co.nz/climate-change-adaptation-toolbox/projected-regional-climate-change-hazards/regional-projections-zone-1) + [Zone 3](https://niwa.co.nz/climate-change-adaptation-toolbox/projected-regional-climate-change-hazards/regional-projections-zone-3) — rates/figures may have changed since)
- **Insurance premiums rising** for high-risk zones

---

## Section: `--mains`

### Sources

- **Watercare** (Auckland): `https://www.watercare.co.nz/`
- **Tiaki Wai** (Wellington metro — Wellington, Hutt, Upper Hutt and Porirua; council-owned, absorbed Wellington Water from 1 Jul 2026): `https://www.tiakiwai.co.nz/` — water services charges are removed from council rates bills and billed separately by Tiaki Wai (quarterly; councils run the billing in the first year) (2026 data, source [Tiaki Wai](https://www.tiakiwai.co.nz/) + [Upper Hutt City Council, 30 Oct 2025](https://www.upperhutt.govt.nz/News/New-chapter-for-water-services-in-metropolitan-Wellington))
- **Christchurch City Council** and **Dunedin City Council** keep water supply, wastewater and stormwater in-house (in-house business units) under Local Water Done Well; water services delivery plans accepted by the Secretary for Local Government on 28 Oct 2025 (CCC) and 10 Nov 2025 (DCC) (2026 data, source [Ministry for Cities, Environment, Regions and Transport — Water services delivery plans](https://www.mcert.govt.nz/our-work/local-government/water-services/water-services-delivery-plans/) + [CCC — Local Water Done Well](https://ccc.govt.nz/services/water-and-drainage/local-water-done-well), archived 2025-11-27)
- Universal in cities; rural may have rainwater tanks + septic

### Costs

| Scenario | Cost (NZD, est. — unsourced) |
|---|---:|
| Mains connection | ~$5,000–$15,000 est. (no primary all-in figure found; council fee alone e.g. $1,800 or $2,470 for a 20mm water connection, 2026 data, source [Waikato District Council — Service connections](https://www.waikatodistrict.govt.nz/services-facilities/water/building-development-and-tradewaste/service-connections), and a development contribution may apply) |
| Septic upgrade | ~$15,000–$30,000 est. (calibration: one drainlayer's guide lists system $14,000–$22,000 + wastewater report $900–$1,800 + consent fees $1,000–$3,000, all + GST; computed: 14,000 + 900 + 1,000 = 15,900 and 22,000 + 1,800 + 3,000 = 26,800 + GST ⚠️, undated guide filed under Jul 2024, 2024 data, source [Woods Drainage — Septic Tank Guide](https://woodsdrainage.co.nz/wp-content/uploads/2024/07/Septic-Tank-Guide.pdf) — rates/figures may have changed since) |
| Rainwater tank | ~$3,000–$8,000 est. (calibration: 25,000-litre plastic tank on sale at $3,295, was $3,495, or $4,895 with accessories, was $5,845.80 ⚠️ vendor prices, 2026 data, source [Big Water Tanks](https://bigwatertanks.co.nz); upper end unsourced; check what delivery and installation add) |
| Bored well | $10,000–$25,000 |

est. — unsourced ballpark ranges; no primary source confirmed. Actual cost depends on site access, ground conditions, distance to the network, tank size / well depth, and council consent and development-contribution fees. In Auckland a new connection (or an existing connection that increases its use) also pays Watercare's one-off Infrastructure Growth Charge, which funds bulk infrastructure, not local network upgrades (2026 data, source [Watercare — Infrastructure Growth Charge](https://www.watercare.co.nz/builders-and-developers/tools-fees-and-resources/infrastructure-growth-charge)). Verify with 2–3 local contractor quotes and the council / water provider's current fees.

---

## Cost benchmarks (NZ 2026)

| Work | Cost (NZD; est. = contractor / practitioner quote range from the 2026-04 research, no primary source — verify with 2–3 local quotes) |
|---|---:|
| Building report | ~$400–$1,000 est. (see `--tax` § Transaction taxes; Trade Me guide: from $400 ⚠️, 2024 data, updated 29 Oct 2024 — rates/figures may have changed since) |
| LIM report | council fee — e.g. $575.50 Wellington City Council residential, 2026/27 incl. GST (see `--tax` § Transaction taxes) |
| Solicitor / conveyancer | ~$1,500–$3,000 est. (Trade Me guide: $800+ ⚠️, 2024 data, updated 29 Oct 2024 — rates/figures may have changed since) |
| Body Corporate disclosure | ~$300–$700 est. |
| **Total transaction cost (buyer)** | **~$2,500–$4,600 est.** (computed in `--tax` § Total transaction cost) |
| Roof restoration | ~$5,000–$15,000 est. |
| Earthquake strengthening (older builds) | ~$30,000–$200,000+ est. |
| Asbestos abatement | ~$5,000–$30,000 est. |
| Leaky home remediation | ~$100,000–$500,000+ est. |
| Insulation upgrade | ~$5,000–$15,000 est. |
| Heat pump | ~$2,500–$5,000 est. |
| Solar PV (5kW) | ~$10,000–$15,000 est. |

Calibration: est. rows have not been re-quoted since the 2026-04 research — rates/figures may have changed since; the one row checked against a primary fee schedule (LIM, $575.50 at Wellington City Council for 2026/27) came in above the earlier $300–$500 range.

## Active fiscal incentives (2025-2026)

- **First Home Loan**: 5% deposit via Kāinga Ora — Kāinga Ora underwrites the loan so a bank or lender can accept a 5% deposit; eligibility criteria apply (2025 data, source: [govt.nz — Financial help for first-home buyers](https://www.govt.nz/browse/housing-and-property/buying-or-selling-a-home/buying-your-first-home/), updated 11 Mar 2025) — rates/figures may have changed since; verify current criteria and participating lenders with Kāinga Ora (`https://kaingaora.govt.nz/`)
- **First Home Grant**: ❌ ENDED — finished May 2024 and no longer available (was up to $5,000, or $10,000 for a new build) (2026-10-23 verified, source: [govt.nz — Financial help for first-home buyers](https://www.govt.nz/browse/housing-and-property/buying-or-selling-a-home/buying-your-first-home/))
- **KiwiSaver First Home Withdrawal**: all KiwiSaver savings (including the government contribution) except $1,000 that must stay in the account; funds transferred from an Australian complying superannuation scheme cannot be withdrawn; at least 3 years' KiwiSaver membership required (2026-10-23 verified, source: [IRD — Getting my KiwiSaver for my first home](https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/getting-my-kiwisaver-funds-early/getting-my-kiwisaver-for-my-first-home), updated 28 May 2024)
- **Healthy Homes incentives**: insulation grants — verify current eligibility with EECA
- **Warmer Kiwi Homes**: Energy retrofit subsidy — verify current eligibility and funding with EECA

## Common listing platforms

- **Trade Me Property** — biggest
- **realestate.co.nz** — industry-owned
- **OneRoof** (NZ Herald)
- **Homes.co.nz** — sold-prices

## Caveats unique to NZ

- **NO STAMP DUTY** since 20 May 1999 (Stamp Duty Abolition Act 1999); buyer transaction cost ~$2,500–$4,600 est. (computed in `--tax` § Total transaction cost)
- **NO general CGT** but **bright-line test 2 years** (property sold on/after 1 Jul 2024) — sells within 2 years = ordinary income
- **7 Nov 2026 election proposals** (none legislated): Labour 28% CGT from 1 Jul 2027 on residential investment + commercial property; Greens 10-year bright-line + interest denial; Te Pāti Māori 5% residential stamp duty — see `--tax` § Future risk
- **Foreign-buyer ban (2018)** — AU + SG citizens exempt; off-the-plan apartments only in developments with a developer exemption certificate; **since 6 Mar 2026** AIP / Investor 1 / Investor 2 resident visa holders can seek consent for a home priced more than NZ$5m (see `--tax` § Foreign-buyer regime)
- **NHCover (Toka Tū Ake)**: automatic with any home insurance policy that includes fire; building cover cap generally $300,000 + GST per natural-hazard event; max levy $480 + GST/yr (2026-10-23 verified, source: [Natural Hazards Commission — About NHCover](https://www.naturalhazards.govt.nz/insurance-and-claims/about-nhcover/)) — UNIQUE coverage
- **Earthquake risk extreme** — NSHM 2022 raised hazard ~50%; Christchurch + Wellington high
- **Wellington City ~-30.6% (computed)** from its Jan 2022 QV HPI peak to Sep 2026; still the weakest REINZ HPI series YoY (-4.5%, Sep 2026) — see `--price` § Compute
- **Cross-lease titles** (~10% Auckland) — shared ownership of section, flat plan; clunky for renovations
- **Leaky homes crisis** (1990s-early 2000s) — monolithic cladding pre-2003 vulnerable
- **Healthy Homes Standards** mandatory for rentals
- **Interest deductibility 100% restored 1 Apr 2025** for residential investment (2026-10-23 verified, source: [IRD](https://www.ird.govt.nz/property-interest-rules)); Greens propose denying it again (election proposal only)
- **GST on STR via platforms** since 1 Apr 2024
- **Cyclone Gabrielle 2023** + Auckland floods 2023 — major recent reform drivers
- **NHCover building cap $300k+GST** — high-value houses need top-up insurance
- **LIM report** (council-set fee, e.g. $575.50 residential at Wellington City Council, 2026/27 incl. GST; see `--tax` § Transaction taxes) mandatory in practice
- **Māori land** (Te Ture Whenua Māori Act 1993) — unique constraints, often 99-year leases
- **Rating valuations** (CV/LV) at least every 3 years per council (source: [LINZ — Property valuation in NZ](https://www.linz.govt.nz/guidance/property-valuation/property-valuation-new-zealand)); not market value
- **Rental loss ring-fencing** — cannot offset other income

## Reddit / forum sources

- **r/PersonalFinanceNZ** — biggest community
- **r/auckland**, **r/wellington**, **r/chch**
- **r/newzealand**
- **PropertyTalk forums**
- **Stuff Property** (news)

## Verification authorities

| Authority | When to call |
|---|---|
| **LINZ Toitū Te Whenua** | Title verification |
| **Local council** | LIM report, rates, zoning |
| **Earth Sciences NZ** (formerly GNS Science + NIWA) / **GeoNet** | Hazard zone status — GeoNet is a partnership of NHC Toka Tū Ake, Earth Sciences NZ and LINZ (2026 data, source [GeoNet — About](https://www.geonet.org.nz/about)) |
| **Toka Tū Ake (NHC)** | Natural-disaster cover specifics; prior NHC / EQC claim history on the home (Natural Hazards Portal, or request claim information from NHC) |
| **REINZ** | Market data |
| **Body Corporate** | If unit title |
| **Lawyer or registered conveyancer** | Conveyancing + settlement — both can carry out property transactions (2026 data, source [settled.govt.nz — Support team](https://www.settled.govt.nz/buying-a-home/thinking-of-buying/building-your-support-team-when-buying/)) |

## Source URL templates

| Source | URL pattern |
|---|---|
| LINZ Public Land Record Search | `https://lrs.linz.govt.nz/search/` |
| Trade Me Property | `https://www.trademe.co.nz/property/` |
| realestate.co.nz | `https://www.realestate.co.nz/` |
| REINZ HPI | `https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx` |
| QV / Cotality NZ | `https://www.qv.co.nz/price-index/` |
| GeoNet | `https://www.geonet.org.nz/` |
| Earth Sciences NZ (GNS Science + NIWA, merged 1 Jul 2025; legacy GNS site `https://www.gns.cri.nz/`) | `https://www.earthsciences.nz/` |
| Toka Tū Ake (Natural Hazards Commission) | `https://www.naturalhazards.govt.nz/` |
| NIWA (Earth Sciences NZ) | `https://niwa.co.nz/` |
| NZTA Traffic Counts | `https://www.nzta.govt.nz/resources/state-highway-traffic-volumes` |
| NZTA SH traffic monitoring (open data: AADT + % heavy) | `https://opendata-nzta.opendata.arcgis.com/datasets/b90f8908910f44a493c6501c3565ed2d` |
| Natural Hazards Portal (NHC) | `https://www.naturalhazardsportal.govt.nz/` |
| Tiaki Wai (Wellington metro water) | `https://www.tiakiwai.co.nz/` |
| IRD (**Te Tari Taake**) | `https://www.ird.govt.nz/` (2026-10-23 verified bilingual masthead: "Inland Revenue - Te Tari Taake") |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing (REINZ HPI + QV + Trade Me), traffic, tax (rates + bright-line + GST + zero stamp duty), rental (RTA + Healthy Homes), work, risks (NSHM 2022 + Cyclone Gabrielle 2023 + leaky homes), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for REINZ + QV September 2026 price benchmarks + bright-line 2-yr (property sold on/after 1 Jul 2024) + interest deductibility 100% from 1 Apr 2025 + foreign-buyer ban (AU+SG citizens exempt) with the $5m+ investor-visa pathway in force since 6 Mar 2026 + NHCover $300k+GST cap + STR GST collection from 1 Apr 2024 + minimum wage $23.95/hr from 1 Apr 2026 (each re-checked 2026-10-23 against REINZ / QV / IRD / LINZ / NHC / Employment NZ); MEDIUM for the Auckland APTR night bands (last re-checked 2026-08-07), the $5m pathway's one-property limit (secondary source only) and the 7 Nov 2026 election proposals (secondary sources; party proposals, not law); LOW for the council rates table + "rates frozen" line, listing-platform counts, city salary ranges, cost and mains-cost benchmarks (est., unsourced), the leaky-homes damage est. and the climate / sea-level projections (not re-verified).
**Last verified**: 2026-08-07 (Auckland APTR suspension since 2020 + graduated general-rates/CATTR STR business uplift re-verified against Auckland Council; other sections unchanged). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Rental / tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-23 | 2026-11-05 maintenance run | Stats NZ's housing topic and September 2026 selected price indexes confirm the rental measures (stock +0.1%, flow +0.9%, released 16 Oct 2026), and its building-consents metadata confirms price per square metre as value divided by floor area. |
| `--rental` | 2026-10-23 | 2026-11-05 maintenance run | Queenstown Lakes District Council confirms its 28-day threshold and rating bands (Mixed Use +25-35%, Accommodation +50-80%), and Auckland Council confirms all four night bands for 2026/27. |
| `--risks` | 2026-10-23 | 2026-11-05 maintenance run | Earth Sciences NZ confirms the 1 Jul 2025 merger, the archived GNS page confirms the 2022 National Seismic Hazard Model finding, and the Natural Hazards Commission confirms NHCover's $300,000 +GST cap and land limits. |
| `--mains` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (NZ 2026) | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--tax` | 2026-10-23 | 2026-11-05 maintenance run | The building report stays ~$400–$1,000 est. on inspection firms' published ranges and Trade Me's guides, which keeps the buyer transaction total at ~$2,500–$4,600 est. IRD confirms the interest rules and the 5-year bright-line row; Labour's 28% CGT proposal and the parties' interest stances rest on Nexia and KPMG (secondary). |

## Extension TODOs

- [ ] Per-council rates table
- [ ] Per-council STR rules detail
- [ ] Cross-lease conversion to fee simple flow
- [ ] Leaky-home identification + remediation decision tree
- [ ] Earthquake strengthening NSEC rating verification
- [ ] Bright-line transition rules per acquisition date
- [ ] Healthy Homes Standards compliance checklist
- [ ] Māori land (Te Ture Whenua) constraint check
- [ ] NHCover top-up insurance for high-value homes
- [ ] AU/SG resident exemption verification flow

## Update history

- **2026-04-25** — Initial population.
- **2026-08-07 to 2026-10-21** — Auckland APTR re-check (2026-08-07) and rental / tax regwatch tracker re-checks (2026-09-24, 2026-10-21); details in the Status footer.
- **2026-10-23** — Refresh wave, partial: the playbook-level date is not re-stamped because `--risks` still holds curated qualitative lines with no fetched source (insurance premiums rising for high-risk zones, steep-terrain landslip risk, Coastal Hazards Susceptibility per council mapping, vendor warranty re weathertightness); `--price`, `--tax`, `--rental`, `--work`, `--mains` and Cost benchmarks were closed in the follow-up gap-closing pass (last sub-bullet). Facts checked / changed / confirmed / unverifiable per section:
  - **Country profile** — 10 / 2 / 1 / 7: EUR/NZD set to the ECB reference rate (22 Oct 2026); foreign-buyer line rewritten against LINZ (9 / 6 / 3 / 0 for that line alone) — the $5m+ investor-visa pathway is in force since 6 Mar 2026, replacing "Order in Council expected early 2026"; the one-property limit stays, sourced to Bell Gully (secondary). Unverified: postcode examples, 16 regions / 67 TAs, LRS $8 fee, leasehold place names, cross-lease ~10% of Auckland.
  - **`--price`** — 19 / 14 / 2 / 3: benchmark table (all 9 rows) moved to REINZ + QV September 2026; QV / Cotality source lines and Compute steps 3–4 rewritten (Wellington City ~-30.6% computed from the Jan 2022 QV HPI peak, replacing ~-26% est.). Unverified: Trade Me ~39k and realestate.co.nz ~35k listing counts, "industry-owned", a Stats NZ house price index.
  - **`--traffic`** — 3 / 1 / 0 / 1: NZTA open-data AADT + heavy-vehicle source added; the NZTA traffic-volumes page could not be read for verification (kept); verdict bands are curated thresholds, not sourced facts.
  - **`--tax`** — 36 / 9 / 9 / 18: bright-line, interest deductibility, STR GST and the foreign-buyer regime re-checked against IRD / LINZ; 7 Nov 2026 election proposals added under Future risk (party proposals only, secondary sources). Unverified: council rates table and "rates frozen" (both now carry the may-have-changed suffix), legal / LIM / building-report fees, total transaction cost, stamp-duty abolition 1999 / "UNIQUE in OECD", the pre-2018 2-year bright-line row.
  - **`--rental`** — 24 / 2 / 16 / 6: RTA amendment dates and notice periods, the 12-month rent rule, ring-fencing, Healthy Homes, interest deductibility, the GST $60k threshold and the QLDC rating bands confirmed. Unverified: Auckland APTR night bands (Auckland Council unreachable; last re-checked 2026-08-07), [2023] NZSC 53, the QLDC 90-night cap, "other councils tightening".
  - **`--work`** — 14 / 4 / 5 / 5: minimum wage confirmed ($23.95/hr from 1 Apr 2026, Employment NZ); job boards updated (JobSpace, Indeed NZ; JobAve dead); MIQ replaced by Immigration New Zealand; salary block labelled est. Unverified: "Seek — biggest", the Trade Me Jobs URL, "min $1 capital", city salary ranges.
  - **`--risks`** — 32 / 9 / 11 / 12, plus climate projections 5 / 1 / 0 / 4: GNS Science and NIWA updated to Earth Sciences NZ (merged 1 Jul 2025); earthquake and volcano lines re-sourced to GeoNet; ICNZ insured-loss figures added for Canterbury 2010-11, Kaikōura 2016, the 2023 Auckland floods and Cyclone Gabrielle; Taupō, Auckland Volcanic Field, asbestos-era and leaky-homes-era rows corrected; NZ SeaRise pointer and an Earth Sciences NZ ex-tropical-cyclone rainfall data point added. Unverified: Whakaari death toll, sea-level rise +20-80 cm, leaky-homes ~$11B, Canterbury ~$40B total, lead-paint / H1 / post-2018 rows, LIM fee, +1.5–4.0°C, drought and premium trends.
  - **`--mains`** — 8 / 1 / 1 / 6: Wellington Water replaced by Tiaki Wai (council-owned, from 1 Jul 2026); Watercare confirmed; cost table labelled est. (unsourced). Unverified: Christchurch / Dunedin water arrangements, the four cost ranges.
  - **Cost benchmarks** — 12 / 0 / 0 / 12: header labelled est. (contractor-quote ranges, no primary source); values unchanged.
  - **Active fiscal incentives** — 5 / 1 / 0 / 4: First Home Loan re-sourced to govt.nz; KiwiSaver first-home withdrawal corrected against IRD. Unverified: EECA programmes (insulation grants, Warmer Kiwi Homes).
  - **Caveats unique to NZ** — 12 / 5 / 5 / 2: Wellington line aligned with `--price` Compute; foreign-buyer, NHCover and rating-revaluation lines corrected; election-proposal pointer added. Unverified: "NO STAMP DUTY — UNIQUE in OECD" with ~$3-5k transaction cost, LIM ~$300-500.
  - **Common listing platforms** — 4 / 0 / 1 / 3 and **Reddit / forum sources** — 7 / 0 / 0 / 7: unchanged; only Homes.co.nz confirmed, subreddit URLs checked for liveness only.
  - **Verification authorities** — 7 / 3 / 4 / 0 (fully re-verified): Earth Sciences NZ / GeoNet partnership, NHC claim-history checks, lawyer or registered conveyancer (settled.govt.nz).
  - **Source URL templates** — 11 / 3 / 7 / 1: GNS re-pointed to earthsciences.nz and NIWA to niwa.co.nz; NZTA open data, Natural Hazards Portal and Tiaki Wai added; the NZTA traffic-volumes page could not be read for verification.
  - **Gap-closing pass** (sources read by 2026-11-03) — confirmed / changed / relabelled: `--price` 2 / 2 / 1, `--rental` 4 / 1 / 0, `--work` 0 / 2 / 2, `--tax` 4 / 7 / 4, Cost benchmarks 0 / 2 / 10, `--mains` 1 / 0 / 1 — all six closed; `--risks` 3 / 10 / 9, still open (curated lines above); totals 14 / 24 / 27. Council rates table rebuilt for 2026/27 from Auckland, Wellington City and Christchurch sources (Queenstown Lakes stays est.); LIM fee now given as set by each council (e.g. Wellington City Council $575.50, 2026/27) and the buyer total recomputed to ~$2,600–$4,600 est.; Auckland APTR bands, [2023] NZSC 53 and the QLDC 90-night cap confirmed; NIWA (AR5-era) climate and sea-level figures replace the unsourced ranges; the $5m pathway's one-property limit (Country profile and `--tax`) re-sourced from Bell Gully (secondary) to LINZ investor-visa guidance (26 Mar 2026).
- **2026-11-04** — Maintenance run: closed `--price`, `--rental`, `--risks`, `--mains`, Cost benchmarks (NZ 2026); still open `--tax`, `--work=<profession>`.
- **2026-11-05** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--risks`, `--mains`, Cost benchmarks (NZ 2026); still open `--work=<profession>`.
