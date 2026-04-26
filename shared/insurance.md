# Universal `--insurance` Section

Per-country property insurance landscape across all 44 supported countries: catastrophic-risk reinsurance schemes, flood/earthquake availability, ballpark premium %, mortgage-mandatory rules, 2025-26 climate-risk reforms.

**Snapshot**: April 2026.

**Anti-hallucination**: every premium percentage is a broker-rule-of-thumb range; should not be quoted as authoritative for a specific transaction. `[verify]` flags figures that could not be confirmed against a primary source.

## Universal contract

For the property's country, return:
1. **Catastrophic-risk reinsurance scheme** if any
2. **Flood-policy availability**: universal? optional? denied in zones
3. **Earthquake-policy availability**: who must / who optional / who denied
4. **Average homeowner premium** as % of insured value (rebuild cost basis)
5. **Mortgage-mandatory or owner-optional**
6. **2025-26 climate-risk reforms**
7. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Insurance Profile

**Country**: <ISO2>
**Catastrophic scheme**: <name + mandatory surcharge if any>
**Flood**: <universal | optional | denied in zones>
**Earthquake**: <universal | optional | denied>
**Premium % insured value**: <range>
**Mortgage-mandatory**: <yes | no>
**2025–26 reforms**: <list>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Standing caveats**:
- "Mortgage-mandatory" universally means lenders require fire/building cover at minimum; contents and liability are owner-optional
- "Insured value" = reconstruction cost basis in most civil-law jurisdictions; "sum insured" in common-law
- Climate reforms move quickly — 2026 figures are as of April 2026 and several are pending implementing decrees

---

## Europe

| Country | Cat-risk scheme | Flood | Earthquake | Premium % insured value | Mortgage-mandatory | 2025-26 reforms |
|---|---|---|---|---|---|---|
| **FR** | CCS Catnat — mandatory ~12% surcharge on multi-risk premium, **rising to 20% from 1 Jan 2025** per arrêté 22 Dec 2023 (ccr.fr, legifrance) | Universal via Catnat once commune declared "état de catastrophe naturelle" | Universal via Catnat | ~0.15-0.30% [verify ballpark] | Yes — assurance habitation required by lender; co-ownership mandates building cover under loi ALUR | Catnat surcharge raised to 20% (drought) / 12% (other) Jan 2025; PPRN risk-zone expansion ongoing; "Loi Baudu" 2025 strengthens insurer obligations on uninsurable zones [verify] |
| **IT** | No federal scheme historically; **Legge di Bilancio 2024 (L. 213/2023) art. 1 c. 101-111** mandates natural-catastrophe cover for businesses (originally 31 Dec 2024, postponed by Decreto Milleproroghe to 31 Mar 2025 / 1 Oct 2025 / 1 Jan 2026 by company size) | Optional for individuals; private market; flood (alluvione) extension | Optional individuals; mandatory businesses from 2025; high-risk seismic zones 1-2 (south, central Apennines) | ~0.20-0.40% [verify] | Yes — fire (incendio/scoppio) required by mortgage law | Business cat-cover phase-in throughout 2025; **individual mandate proposed but NOT yet enacted** as of Apr 2026 [verify]; sismabonus/ecobonus tax credits continue |
| **CZ** | No central scheme; private reinsurance via Munich Re/Swiss Re | Optional, broadly available; 2024 Storm Boris floods prompted ČAP industry review | Optional; low seismic risk | ~0.10-0.20% [verify] | Yes — pojištění nemovitosti standard with mortgage | ČNB monitoring post-Boris underinsurance; no major reform announced [verify] |
| **SK** | No central scheme | Optional | Optional; low risk | ~0.10-0.20% [verify] | Yes | None major announced [verify] |
| **DE** | No federal scheme; **Elementarschadenversicherung** optional but uptake ~54% as of 2024 (GDV); **Bundesrat motion June 2024** for mandatory Elementarschaden but stalled | Optional via Elementarschaden rider; insurers use ZÜRS Geo zoning (zones 1-4); zone 4 often denied or surcharged | Optional via Elementarschaden; low-moderate risk | ~0.10-0.30% (Wohngebäude); Elementar surcharge varies | Yes — Wohngebäude (fire) required by Pfandbriefgesetz | Mandatory Elementarschaden bill stalled in Bundestag as of early 2026 [verify]; GDV/Bundesländer continuing risk-zoning updates; BaFin guidance 2025 on climate-stress |
| **AT** | No central scheme; partial state aid via **Katastrophenfonds** — not insurance | Optional; flood often capped (€7-15k typical sublimit per VVO) | Optional; low-moderate risk in south | ~0.15-0.25% [verify] | Yes — Eigenheimversicherung standard | Katastrophenfondsgesetz amendments 2024 increased federal share; **no mandatory cat-insurance** despite 2024 floods debate [verify] |
| **CH** | **19 cantonal monopoly insurers (KGV / ECA / AGI)** — mandatory building insurance covering fire + natural perils in those cantons; remaining 7 ("GUSTAVO": GE, TI, VD, VS, OW, AI, UR partly) use private market via **Schweizerische Pool für Erdbebenversicherung** voluntary pool | Universal via cantonal scheme or private elementary perils; premium and cap regulated nationally | Earthquake **NOT covered** by standard scheme; voluntary Pool Suisse (~CHF 2bn capacity, 2024); referendum on mandatory EQ cover failed 2023 | Cantonal: ~0.04-0.08% (subsidised); private: ~0.10-0.20% | Yes for mortgages; cantonal scheme makes it automatic in 19 cantons | EQ pool capacity raised 2024 [verify]; cantonal premiums under review post-2024 floods |
| **ES** | **Consorcio de Compensación de Seguros (CCS)** — mandatory surcharge on every property policy funds extraordinary risks (flood, EQ, terrorism, atypical wind >135 km/h) (consorseguros.es) | Universal via CCS once event qualifies as "extraordinary"; ordinary flood via private | Universal via CCS for "extraordinary" EQ events | ~0.20-0.35% [verify]; CCS surcharge ~€0.09 per €1k for dwellings (2024) | Yes — seguro de hogar / incendios required by Ley Hipotecaria | Post-DANA Valencia 2024: CCS paid >€4bn claims; **CCS surcharge tariff under review for 2026** [verify] |
| **PT** | No central scheme; **seguro multirriscos habitação** mandatory only for condominium common parts (Lei 8/2022) | Optional individuals; state aid ad-hoc post-event | Optional; **mandatory EQ cover proposed 2023, not enacted** [verify]; high risk Algarve/Lisbon | ~0.15-0.30% [verify] | Yes — fire cover mandatory for mortgages and condos | ASF (regulator) consultation on mandatory seismic cover ongoing [verify] |
| **SE** | No central scheme; comprehensive private homeowner (villa-/hemförsäkring) standard | Universal in standard hem/villa policies | Optional; very low risk | ~0.10-0.20% [verify] | Yes — villaförsäkring required | Finansinspektionen climate-stress guidance 2025 [verify] |
| **FI** | No central scheme | Universal in kotivakuutus | Optional; very low risk | ~0.10-0.20% [verify] | Yes | None major announced |
| **NO** | **Norsk Naturskadepool (NNP)** — every fire-policy automatically funds the pool; covers landslide, storm, flood, avalanche, EQ (naturskade.no, lov om naturskadeforsikring) | Universal via NNP | Universal via NNP | ~0.10-0.25% [verify]; NNP premium ~0.07‰ of fire-sum (2024) | Yes — fire cover required by mortgage; auto-includes NNP | NNP capacity reviewed annually; no structural reform 2025-26 [verify] |
| **UK** | **Flood Re** — reinsurance pool for high-flood-risk homes built before 2009; funded by £180m levy on home insurers (floodre.co.uk); planned wind-down by 2039 | Optional but Flood Re ensures availability for eligible homes; "Build Back Better" up to £10k resilience grants | Optional; low risk | ~0.15-0.30% (ABI: avg £396 buildings 2024 [verify]) | Yes — buildings insurance required | Flood Re mid-term review 2024 published; **transition planning to free market 2039**; ABI/government Property Flood Resilience roundtable ongoing |
| **NL** | No central scheme; **Wet tegemoetkoming schade bij rampen (WTS)** = ad-hoc state aid | River flooding **largely uninsurable** historically (dyke-protection); pluvial/local flood usually included in opstal; 2021 Limburg floods reignited debate | Optional; low risk | ~0.10-0.20% [verify] | Yes — opstalverzekering required | Verbond van Verzekeraars voluntary primary-flood cover initiative 2024-25; **no mandatory scheme** [verify] |
| **BE** | **Caisse de Compensation/Tariferingsbureau (TB)** + obligatory natural-disaster cover bundled in fire policy since 2007 (loi 17 sept 2005) (assuralia.be) | Universal — natural perils mandatory in fire/multi-risk policies | Universal via mandatory bundle | ~0.20-0.35% [verify] | Yes — incendie/brandverzekering required | Post-July 2021 floods: regional caps raised; **Walloon flood-zone PPR-style mapping 2024**; insurer-of-last-resort role for TB strengthened [verify] |
| **DK** | **Stormrådet / Stormflodsordning** — state-administered storm-surge and freshwater-flood pool funded by mandatory DKK 60/yr levy on every fire policy (stormraadet.dk) | Universal via Stormrådet for storm surge / flood / unusual rain since 2010 | Optional; very low risk | ~0.10-0.20% [verify] | Yes — bygningsforsikring required | Stormflodsordning levy reviewed periodically; no structural reform 2025-26 [verify] |
| **IS** | **Náttúruhamfaratrygging Íslands (NTÍ)** — mandatory natural-disaster insurance bundled with fire policy; covers EQ, volcanic, landslide, avalanche, flood (nti.is) | Universal via NTÍ | Universal via NTÍ | NTÍ premium ~0.025% of insured value (2024) | Yes — fire cover mandatory by law (Lög um brunatryggingar) | Post-Reykjanes/Grindavík eruptions 2023-24: NTÍ paid extensive claims; **government bought out Grindavík homes 2024** via Þórkatla agency; NTÍ capacity review ongoing |
| **SI** | No central scheme | Optional; 2023 floods exposed underinsurance | Optional; moderate seismic | ~0.15-0.25% [verify] | Yes | Post-2023 floods: government solidarity contribution and reconstruction scheme; **no mandatory cat-insurance** [verify] |
| **IE** | No central scheme; insurers use OPW flood maps; **Insurance Ireland** memorandum on demarcation areas | Optional; high-risk areas often denied or surcharged; "demarcation" practice contentious | Optional; very low risk | ~0.20-0.35% [verify]; CSO 2024 avg ~€500/yr | Yes — buildings cover required | OPW / DECC flood-relief schemes ongoing; **Programme for Government 2024 commits to flood-insurance review** [verify] |
| **GR** | No central scheme | Optional | Optional; **mandatory EQ cover for properties >€500k or in high-risk zones proposed 2024** [verify, not enacted Apr 2026]; high seismic | ~0.20-0.40% [verify] | Yes — fire cover required for mortgaged property; many GR homes unmortgaged + uninsured (estimated ~15% penetration, EIOPA 2023) | **Law 5108/2024** updated insurance code; Bank of Greece consultation on mandatory cat-cover 2025 [verify] |
| **PL** | No central scheme; **mandatory farm-building insurance** under 2005 act | Optional residential; universal for insured farms | Optional; low risk | ~0.10-0.20% [verify] | Yes — fire cover required by mortgage | KNF guidance on climate-risk 2025 [verify] |
| **EE** | No central scheme | Optional | Optional; very low risk | ~0.10-0.20% [verify] | Yes | None major announced |
| **HR** | No central scheme; post-2020 Petrinja EQ state reconstruction fund | Optional | Optional; high seismic Zagreb/Petrinja | ~0.15-0.30% [verify] | Yes | Post-Petrinja reconstruction law amendments 2023-24; mandatory cat-cover debated [verify] |
| **HU** | No central scheme | Optional | Optional; low risk | ~0.10-0.20% [verify] | Yes — lakásbiztosítás required for mortgage | MNB "Otthon biztosítás" comparison portal 2024-25 |
| **LT** | No central scheme | Optional | Optional; very low risk | ~0.10-0.20% [verify] | Yes | None major |
| **LV** | No central scheme | Optional | Optional; very low risk | ~0.10-0.20% [verify] | Yes | None major |
| **RO** | **PAID (Pool de Asigurare Împotriva Dezastrelor Naturale)** — mandatory dwelling cat-policy (PAD) covering EQ, flood, landslide; flat premium €10 (type B masonry/wood) or €20 (type A reinforced concrete) for €10k/€20k cover (paidromania.ro, Law 260/2008) | Universal via PAID up to PAD limit; supplemental private | Universal via PAID; high seismic Vrancea | PAD: €10-20/yr fixed; voluntary multi-risk additional ~0.15-0.30% | PAD compulsory by law for ALL dwellings; mortgage requires additional voluntary cover | **Law 260/2008 amended 2023** to raise PAD limits and digitise distribution via insurers; ASF enforcement campaigns 2024-25; uptake still only ~20% despite legal mandate [verify] |
| **BG** | No central scheme | Optional | Optional; moderate seismic | ~0.10-0.20% [verify] | Yes | None major announced |
| **LU** | No central scheme | Optional; small market, broadly available | Optional; low risk | ~0.15-0.25% [verify] | Yes | None major |
| **CY** | No central scheme | Optional | Optional; **EQ recommended** by Insurance Association of Cyprus, high seismic | ~0.15-0.30% [verify] | Yes — fire required for mortgage | None major announced [verify] |
| **MT** | No central scheme | Optional | Optional; moderate seismic | ~0.15-0.25% [verify] | Yes | None major |

## Western Balkans

| Country | Cat-risk scheme | Flood | Earthquake | Premium % | Mortgage-mandatory | 2025-26 reforms |
|---|---|---|---|---|---|---|
| **RS** | **Europa Re** regional facility participation (with BA, MK, AL); voluntary household micro-cat product distributed via local insurers | Optional via Europa Re or private | Optional; moderate seismic | ~0.15-0.30% [verify] | Yes — fire required | Europa Re product expansion 2024-25 [verify] |
| **ME** | Europa Re participation | Optional | Optional; high seismic coastal | ~0.15-0.30% [verify] | Yes | None major announced |
| **BA** | Europa Re participation | Optional | Optional; high seismic | ~0.15-0.30% [verify] | Yes | None major announced |
| **MK** | Europa Re participation | Optional | Optional; high seismic Skopje | ~0.15-0.30% [verify] | Yes | None major announced |
| **AL** | Europa Re participation; post-2019 Durrës EQ reconstruction | Optional | Optional; high seismic | ~0.20-0.35% [verify] | Yes | Post-2019 reconstruction law; mandatory cat-cover debated, not enacted [verify] |

## Anglo non-EU

| Country | Cat-risk scheme | Flood | Earthquake | Premium % | Mortgage-mandatory | 2025-26 reforms |
|---|---|---|---|---|---|---|
| **CA** | No federal scheme historically; **Federal Flood Insurance Program (FFIP)** announced Budget 2023, **operational target 2025-26** via Public Safety Canada / CMHC | Overland flood optional since 2015 (most insurers); historically unavailable; high-risk often denied → FFIP target | Optional; **EQ cover separate** in BC/Quebec; low uptake (~60% BC, ~5% QC, IBC 2024) | ~0.15-0.30% (IBC avg ~CAD 960 home 2023 [verify]) | Yes — homeowners insurance required | **FFIP launch slated 2025**; OSFI B-15 climate-risk guidance 2024; BC EQ retrofit incentives [verify] |
| **AU** | **Cyclone Reinsurance Pool (ARPC)** — operational since July 2022 for cyclone + cyclone-related flood, mandatory participation by insurers (large insurers fully phased in by Dec 2023, smaller by Dec 2024) (arpc.gov.au) | Flood standardised in home policies post-2012 reforms (Insurance Contracts Act); availability variable in Northern QLD/floodplains | Optional; moderate-low | ~0.5-2% in cyclone zones; ~0.2-0.4% elsewhere [verify] (ICA data) | Yes — building insurance required | Cyclone Pool full implementation 2024; **Treasury review of pool 2025**; ICA "Building a more resilient Australia" 2024 |
| **NZ** | **Toka Tū Ake EQC (Earthquake Commission)** — mandatory natural-hazard cover bundled with home fire policy, **cap raised to NZD 300k from 1 Oct 2022** (Natural Hazards Insurance Act 2023, in force 1 July 2024) (naturalhazards.govt.nz) | Universal via Toka Tū Ake for landslip/storm-related land damage; building flood via private insurer | Universal via Toka Tū Ake | EQC levy NZD 480/yr max (=20c/$100 to NZD 300k cap); private home ~0.20-0.40% [verify] | Yes — home insurance required | **Natural Hazards Insurance Act 2023 in force 1 July 2024** — replaces 1993 EQC Act; risk-based pricing increasingly used by private insurers post-Auckland 2023 floods |

## Latin America

| Country | Cat-risk scheme | Flood | Earthquake | Premium % | Mortgage-mandatory | 2025-26 reforms |
|---|---|---|---|---|---|---|
| **MX** | No central household scheme; **FONDEN** disaster fund abolished 2020, replaced by ad-hoc budget; cat-bonds via World Bank (Pacific Alliance) | Optional via seguro de daños / multi-amparo | Optional; **mandatory for mortgaged homes** (CONDUSEF guidance); high seismic | ~0.20-0.50% [verify] | Yes — seguro de daños required for INFONAVIT/bank mortgages | CNSF climate-risk circular 2024 [verify] |
| **BR** | No central household scheme; **SUSEP** regulator | Optional | Optional; very low risk | ~0.15-0.30% [verify] | Yes — seguro habitacional MIP/DFI required for SFH mortgages | SUSEP Resolution 407/2021 modernised compreensivo residencial; climate-risk circular 2024 [verify] |
| **AR** | No central household scheme; SSN regulator | Optional; high inflation distorts sums insured | Optional; moderate-high in west (Mendoza/San Juan) | Highly variable due to inflation [verify] | Yes when mortgages exist (rare in current market) | Macroeconomic dollarisation debate dominates; no specific cat-insurance reform [verify] |
| **CR** | **INS (Instituto Nacional de Seguros)** historic monopoly until 2008 demonopolisation; voluntary cat cover via INS Hogar Comprensivo | Optional | Optional but strongly recommended; high seismic | ~0.15-0.30% [verify] | Yes — póliza de incendio required for bank mortgages | SUGESE supervision; no major reform announced [verify] |
| **PA** | No central scheme | Optional | Optional; moderate seismic | ~0.15-0.30% [verify] | Yes — fire required for mortgage | Superintendencia de Seguros y Reaseguros climate guidance 2024 [verify] |

---

## Insurance gaps surfaced (cannot verify with primary source as of Apr 2026)

- Exact Catnat surcharge effective dates for 2025 in FR (arrêté wording vs CCR communications) — confirm with legifrance.gouv.fr
- Italian individual cat-cover mandate timeline beyond business phase-in
- German Elementarschaden Bundestag bill status (multiple 2024 motions, none enacted as of last verifiable point)
- Greek mandatory EQ cover bill — proposed 2024, not enacted
- Romanian PAID effective uptake percentage (varies between 18-22% across 2023-2024 reports)
- Canadian FFIP exact launch date — slated 2025-26, no confirmed go-live as of cutoff
- All "ballpark premium %" figures for non-headline markets — broker-rule-of-thumb ranges, NOT to be quoted as authoritative

---

## Confidence labels

- **HIGH**: cat-risk scheme name and statutory basis confirmed via official authority URL
- **MEDIUM**: industry-association reports, KPMG/PwC summaries, insurer-published material
- **LOW**: ballpark premium % only, or regulatory consultation not yet enacted

## Status

Last refreshed: 2026-04-26. Next refresh: per-event (each cat-risk scheme reform); annually otherwise.
