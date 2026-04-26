# Specialized Property Type Templates — `--type=<kind>`

Different property types need different due-diligence emphasis. The standard 9-section run is calibrated for "resale of an existing residential property". Specialized types overlay additional checks specific to the type.

## Available types

| Type | Use when |
|---|---|
| `off-plan` | New build / VEFA / VPF / off-plan / under construction |
| `auction` | Auction property (forced sale, judicial, bank repo) |
| `probate` | Estate / probate / succession sale |
| `plot-only` | Land only — buildability check needed |
| `heritage` | Listed / heritage / monument-classified property |
| `apartment` | Flat / condo / apartment in multi-unit building |
| `house` | Single-family detached or semi-detached |
| `mixed` | Mixed-use (residential + commercial) |
| `agricultural` | Farm / vineyard / agricultural with residence |
| `coastal` | Coastal / second-home / leisure property |
| `commercial` | Pure commercial (out of skill scope — flag) |

Combine: `/property-deep-dive <addr> --all --type=off-plan --journey=foreign-buyer`

---

## 1. Off-plan / new build

### Additional checks beyond standard

#### Developer due diligence

- **Companies House / RCS / KBIS / Handelsregister lookup** — incorporation date, capital, directors
- **Past project portfolio** — completed builds, on-time, quality, snagging
- **Court records** — past disputes / liquidation / liens
- **Online reviews** — buyer feedback, snagging community
- **Site visit** — existing-phase quality (if multi-phase)

#### Contract critical terms

- **Milestone payment schedule** — typical:
  - 5% reservation
  - 10-25% on signature
  - 25-30% foundation poured
  - 25-30% roof on (mise hors d'eau)
  - 25-30% completion (livraison)
  - 5% snagging hold-back
- **Late delivery penalties** (FR pénalités de retard, IT penalità per ritardo)
- **Buyer cancellation rights** — typically 10-day cooling-off
- **Specifications** (cahier des charges / Baubeschreibung) — what's included
- **Variations / extras** — pricing for changes
- **Defect period** — typically 1-2 years post-delivery

#### Insurance / guarantees by country

| Country | Required guarantees |
|---|---|
| 🇫🇷 | Garantie d'achèvement (GFA) - mandatory; Garantie biennale (2yr); Garantie décennale (10yr) |
| 🇮🇹 | Polizza fideiussoria mandatory; Garanzia decennale postuma (10yr) |
| 🇩🇪 | Bauträgerversicherung (insolvency cover); Gewährleistung 5yr (defects) |
| 🇪🇸 | Aval bancario or seguro de caución; Decenal (10yr); Trienal (3yr) |
| 🇵🇹 | Garantia 5yr (structural) + 2yr (other) |
| 🇨🇭 | SIA Norm 118 + Bauversicherung |
| 🇬🇧 | NHBC Buildmark or LABC warranty (10yr) |
| 🇮🇪 | Homebond or Premier Guarantee (10yr) |

#### Red flags specific to off-plan

- 🔴 **No completion guarantee** — walk away
- 🔴 **Developer < 3 years incorporated, no past projects**
- 🔴 **Cash-flow-funded** (no construction loan) — high insolvency risk
- 🔴 **Site stalled** for >3 months — financial issues
- 🔴 **Off-plan deposit > 25%** before construction starts → too much risk
- 🔴 **Promised features ("granite countertops") not in cahier des charges**

### Output add-on

```markdown
### Off-plan Specific

**Developer**: <name>
**Companies-house ID**: <X>
**Incorporated**: <date> · **Past projects**: <N> · **Reviews**: <average>

#### Project status
- Phase: <foundation / structure / finishes / completion>
- On schedule: <yes / X-month delay>
- Site visit: <date> — observations <…>

#### Contract
- Milestone schedule: <align with country standard?>
- Late delivery clause: €<X>/day after <date>
- Cancellation: <terms>

#### Guarantees
- ✅/❌ Completion guarantee (GFA / polizza / NHBC)
- ✅/❌ Decennial (10yr structural)
- ✅/❌ Defect period (1-2 yr)
- ✅/❌ Insolvency insurance

#### Verdict
- 🟢 Strong developer + full guarantees + on schedule
- 🟡 Minor delays or guarantees-light
- 🟠 Developer track record concerns
- 🔴 Insolvency risk OR missing completion guarantee
```

---

## 2. Auction property

### Context

- **Time pressure**: typical 2-21 days from listing to bid
- **No reps & warranties**: "as-is, where-is"
- **Reserve vs guide price**: guide may be marketing, reserve is what seller accepts
- **Buyer's premium**: typically 5-15% on top of hammer price
- **Possession**: vacant or tenanted (huge price difference)
- **Why sold at auction**: forced sale, divorce, bank repo, probate, title issues

### Pre-bid checklist

- [ ] **Title pack review** — typically published 1-2 weeks before
- [ ] **Independent solicitor review** of legal pack — non-negotiable
- [ ] **Pre-bid surveys** — at buyer's expense; rapid turnaround needed
- [ ] **Special conditions** (auction-specific) — e.g., 28-day completion vs 14
- [ ] **Vacant possession proven** — eviction status if tenanted
- [ ] **Encumbrances disclosed** — mortgage discharged at sale?
- [ ] **Search results in legal pack** — local, drainage, environmental, planning
- [ ] **Mortgage in principle** if not cash buyer (banks slow on auctions)
- [ ] **Chain of title clear**

### Common auction property issues

| Issue | Impact |
|---|---|
| Title defect (missing deed link) | Unsellable until fixed (months/years) |
| Adverse possession claim | Litigation risk |
| Unregistered land (UK) | Title fraud risk |
| Sitting tenant | Rent < market + can't evict easily |
| Squatters | Possession action needed |
| Outstanding mortgage > sale price | Need lender approval |
| Restrictive covenants | Limit use / development |
| Unknown easements | Right of way, light, etc. |
| Building defects (structural) | "As-is" — buyer absorbs |
| Pyrite / mica (IE) | DCBS possible but limited |
| Listed status not disclosed | Restoration obligations |
| Pre-emption rights (FR mairie, SE kommun, FR SAFER) | Could be exercised within 60-90 days |

### Output add-on

```markdown
### Auction Specific

**Auction**: <house>
**Auction date**: <date>
**Guide price**: €<X>
**Reserve**: <hidden / disclosed>
**Buyer's premium**: <%>
**Estimated completion timeline**: <14 / 28 days>
**Days to bid**: <N>

#### Why at auction (research)
<probate / repo / divorce / quick sale>

#### Legal pack review
- Title clean: ✅ / ❌
- Possession: vacant / tenanted (<term>)
- Encumbrances: <list>
- Special conditions: <list>
- Searches included: <list>

#### Pre-bid budget
- Independent solicitor: €<X>
- Survey: €<X>
- Searches: €<X>
- Insurance quote: €<X> (must be in place at completion)

#### Bidding ceiling
- Guide price: €<X>
- + Buyer's premium: €<Y>
- + Stamp duty / transfer: €<Z>
- + Estimated repair / clean-up: €<R>
- + Pre-emption risk: <not exercisable / 90 days>
- **Walkaway bid ceiling**: €<X+Y+Z+R - margin>

#### Verdict
- 🟢 Clean title + vacant + good guide → bid
- 🟡 Acceptable but tight margin
- 🟠 Multiple concerns; need premium discount
- 🔴 Title defect / adverse claim / large unknown
```

---

## 3. Probate / estate

### Specifics

- **Multiple owners** post-death (heirs in indivision / comunione / sukcesion)
- **Forced heirship** countries (FR/IT/ES/CH/PL): protected shares
- **All heirs must consent** to sale → one objector = no sale
- **Probate timeline**: 6-24 months
- **Estate frozen** during probate — no transfers
- **CGT recalculation** — basis is date-of-death value (step-up)
- **Inheritance tax** filed before sale in some jurisdictions

### Pre-purchase checks

- [ ] **All heirs identified** — genealogist if family tree unclear
- [ ] **All heirs sign** sale authorization (acte de mandat / vollmacht)
- [ ] **Probate complete** (or specific authorization to sell during probate)
- [ ] **No pending heir claims** (e.g., disinherited child suit)
- [ ] **Inheritance tax paid or contracted** by estate
- [ ] **Death certificate in legal pack**
- [ ] **Forced-heirship calculations correct**

### Common probate issues

| Issue | Impact |
|---|---|
| Indivision / comunione | One heir blocks → impasse |
| Disinherited child suit (FR action en réduction) | Sale void if successful |
| Foreign heir (cross-border) | Brussels IV applies, but adds complexity |
| Heir without ID / contact | Genealogist hunt; can take years |
| Tax owed by estate exceeding assets | Sale proceeds clawed back |
| Lifetime gift (donation) within 15 years | Reduce reserved share |
| Pre-deceased heir with descendants | Per stirpes division |

### Output add-on

```markdown
### Probate / Estate Specific

**Decedent**: <name (year of death)>
**Heirs**: <N> people, <list>
**Forced heirship**: ✅/❌ (jurisdiction)
**Probate status**: <opened / pending / closed>
**Estate tax filed**: <yes / no / pending>

#### Sale authorization
- All heirs identified: ✅/❌
- All heirs consenting: ✅/❌
- Genealogist required: <yes / no>
- Forced-share calculations validated: ✅/❌
- Pending litigation: <list>

#### Risks
- Indivision / co-ownership block: <low / med / high>
- Heir contesting: <low / med / high>
- Cross-border complications: <low / med / high>
- Pre-emption right exercise: <jurisdiction-specific>

#### Pre-purchase asks
- Power of attorney from all heirs (if remote)
- Apostille on cross-border heir signatures
- Notarial certification of forced-share calculation
- Confirmed estate-tax payment

#### Verdict
- 🟢 Probate closed, all heirs consenting, clean
- 🟡 Probate active but consensus among heirs
- 🟠 1+ heir holding back, negotiation needed
- 🔴 Litigation pending, indivision impasse
```

---

## 4. Plot-only (buildable land)

### Buildability checklist

- [ ] **Zoning** (PLU/PLUi/Bauleitplan/Piano Regolatore) — residential / mixed / agricultural
- [ ] **Constructability** — set-back, height, footprint, FAR (floor-area ratio)
- [ ] **Coefficient d'occupation des sols** (FR) / Geschossflächenzahl (DE) / similar
- [ ] **Building permit history** — has anything been refused? Why?
- [ ] **Survey** (bornage / Vermessung) — exact boundaries
- [ ] **Soil study** (étude G2 / Bodengutachten) — bearing, drainage, contamination
- [ ] **Utility connections**:
  - Water (public / well)
  - Sewer (mains / septic permit obtainable)
  - Electricity (3-phase / amperage)
  - Gas (mains available?)
  - Fiber / broadband
- [ ] **Access** — public road frontage / easement?
- [ ] **Servitudes** (right of way, electricity line, gas)
- [ ] **Pre-emption right** (mairie / SAFER / kommune)
- [ ] **Flood / landslide / seismic / fire zone**
- [ ] **Existing trees protected** (heritage tree / Natura 2000)
- [ ] **Archaeology** (e.g., FR archéologie préventive — costly redo)
- [ ] **Heritage designation** affecting buildability
- [ ] **CO2 / SDC** (development charges) per country

### Country-specific zoning lookups

| Country | URL pattern |
|---|---|
| 🇫🇷 | PLU per commune; cadastre + SIG locaux |
| 🇮🇹 | PRG/PGT per comune |
| 🇩🇪 | Bauleitplan / B-Plan per Gemeinde |
| 🇪🇸 | Plan General de Ordenación Urbana (PGOU) per municipio |
| 🇬🇧 | Local Plan + Planning Portal `https://www.planningportal.co.uk/` |
| 🇮🇪 | County Development Plan + `https://www.myplan.ie/` |
| 🇵🇹 | PDM Plano Diretor Municipal |
| 🇨🇭 | Zonenplan per Gemeinde |
| 🇦🇹 | Flächenwidmungsplan per Gemeinde |
| 🇸🇪 | Detaljplan per kommun |

### Output add-on

```markdown
### Plot-only Specific

**Plot area**: <m²>
**Zoning**: <residential / mixed / agricultural>
**Buildable footprint**: <m² × FAR>
**Max height**: <m / floors>
**Set-back from boundaries**: <m>

#### Buildability
- Building permit grantable: <high / med / low likelihood>
- Past refusals on this plot: <none / Y reason>
- Special restrictions: <heritage / Natura 2000 / coastal protection>

#### Utilities (km to nearest connection)
- Water mains: <0 / X km>
- Sewer: <0 / X km / septic only>
- Electricity: <connection cost €<X>>
- Gas: <available / not>
- Fiber: <available / not>

#### Soil
- Bearing capacity: <good / poor / requires special foundation>
- Drainage: <good / poor>
- Contamination check: ✅/❌ done
- Archaeology pre-emption: ✅/❌

#### Total cost to make buildable (beyond purchase)
- Soil study: €<X>
- Survey / bornage: €<X>
- Utility connections: €<X>
- Driveway / access: €<X>
- Permits + fees: €<X>
- **Subtotal pre-construction**: €<X>

#### Verdict
- 🟢 Permitted use, clean, all utilities available
- 🟡 Buildable but utility extension needed
- 🟠 Restricted use OR significant pre-construction cost
- 🔴 Effectively non-buildable OR archaeology / heritage block
```

---

## 5. Heritage / listed property

### Specifics

- **Restoration obligations** — original materials, traditional methods
- **Consent regime** for any change (interior + exterior)
- **Heritage authority approval** — slow (months to years)
- **Higher restoration costs** — specialist craftsmen, original materials
- **Tax incentives** — many jurisdictions offer relief for restoration
- **Insurance premium** — typically 50-100% above standard
- **Smaller buyer pool** at resale → liquidity discount

### Country-specific

| Country | Listing levels | Authority | Tax incentive |
|---|---|---|---|
| 🇫🇷 | ISMH (inscrit), MH (classé), patrimoine remarquable | DRAC + ABF | Loi Malraux: deduct 22-30% of works for 4 yrs; Monuments historiques: 100% deductible if open to public |
| 🇮🇹 | Vincolo + Beni culturali | Soprintendenza | Bonus 110% / Restauro 50% |
| 🇩🇪 | Denkmalschutz (per Bundesland) | Denkmalbehörde | §7i EStG: 9% × 8yrs + 7% × 4yrs depreciation on restoration |
| 🇪🇸 | BIC (Bien de Interés Cultural) | Cultura + CCAA | IRPF 30% reduction + ICIO exemption |
| 🇬🇧 | Grade I, II*, II | Historic England / Cadw / HES | VAT 5% on alterations, but full VAT on like-for-like repairs (post-2012) |
| 🇮🇪 | Protected Structure | Local Planning Authority | Heritage Council grants |
| 🇵🇹 | IIM / IIP / MN | Direção Geral do Património Cultural | IRS deduction up to €500/yr |
| 🇸🇪 | K-märkt / byggnadsminne | Länsstyrelse | Limited grants |
| 🇨🇭 | Per-canton | Kantonale Denkmalpflege | Various |

### Pre-purchase checks

- [ ] **Listing register entry** — print certificate
- [ ] **Restoration obligations document** (FR : arrêté de classement / inscription)
- [ ] **Past works approved / disapproved** — any pending complaints?
- [ ] **Roof, masonry, joinery condition** — heritage materials very expensive
- [ ] **Existing furniture / features listed** (some countries list interior elements)
- [ ] **Open-to-public obligations** (FR MH classé)
- [ ] **Insurance availability** at reasonable premium
- [ ] **Specialist craftsman availability** in region

### Output add-on

```markdown
### Heritage Property Specific

**Listing**: <country-specific level (e.g., FR MH classé / UK Grade II / DE Denkmal)>
**Date of listing**: <YYYY>
**Listed elements**: <façade, roof, interior, garden>
**Authority**: <DRAC + ABF / Soprintendenza / Historic England / etc.>

#### Restoration obligations
- Original materials required: ✅/❌
- Traditional methods required: ✅/❌
- Consent for: <list of restricted works>
- Open-to-public: <yes (X days/yr) / no>

#### Past works
- Approved: <list>
- Refused: <list>
- Pending complaints: <list>

#### Tax incentives applicable
- <country-specific scheme>
- Estimated value: €<X>/yr for <Y>yrs

#### Cost premium estimate
- Restoration premium vs standard: +30-100%
- Specialist craftsmen: <local availability>
- Insurance premium: +50-100%
- Liquidity discount at resale: -10-20%

#### Verdict
- 🟢 Well-restored, tax-relieved, niche buyer profile
- 🟡 Restoration backlog manageable
- 🟠 Major restoration required + slow consent
- 🔴 Crumbling + restrictive consent regime
```

---

## 6. Apartment vs House — what differs

### Apartment-specific checks

#### HOA / management body

- **VME / ACP / sameieforening / Eigentümergemeinschaft / etc.** — read AGM minutes (3 yrs)
- **Reserve fund** balance — minimum required by law in some countries
- **Maintenance plan** (MJOP NL / vedlikeholdsplan NO / piano di manutenzione IT)
- **Outstanding works** — assessment levies upcoming
- **Disputes** — neighbor / management / contractor

#### Building common parts

- **Roof, façade, common stairs, lift, garage, garden**
- **Last major works** date + cost
- **Lift maintenance contract**
- **Fire safety compliance**
- **Façade cleaning + repointing schedule**
- **Heating system** (collective vs individual)

#### Apartment-specific docs

- **Splitsingsakte** (NL) / **règlement de copropriété** (FR) / **Teilungserklärung** (DE) / **regolamento condominiale** (IT)
- **Number of units in building** + private vs communal
- **Voting rights** in HOA
- **House rules** (pets, short-let, noise, parking)

#### Country-specific apartment red flags

- 🇫🇷 **Charges de copropriété** in arrears (seller? other co-owners?)
- 🇮🇹 **Spese condominiali** unpaid > 2 months
- 🇩🇪 **WEG** (Wohnungseigentümergemeinschaft): Hausgeld + Sonderumlage
- 🇳🇴 **Borettslag fellesgjeld** — shared building debt; check ratio
- 🇸🇪 **Bostadsrättsförening** (BRF) — financial health critical
- 🇫🇮 **Asunto-Oy** — vastike (charge), planned putkiremontti (pipe renovation)
- 🇪🇸 **Comunidad de propietarios** — derramas (special levies)

### House-specific checks

- **Roof** — last replaced? Insulated? Tile/slate type?
- **Heating + DHW system** — type, age, efficiency
- **Plumbing** — material (lead?), main shut-off, septic vs mains
- **Electrical panel** — age, capacity, RCDs, smart meter
- **Garden boundaries** — bornage / Vermessung / fence agreement
- **Outbuildings** — garage, shed, pool — taxed?
- **Driveway access** — easement vs ownership
- **Neighbor disputes** — fence, hedge, boundary, noise
- **Trees** — protected, easement, branches over property
- **Drainage** — surface water, soakaway
- **Parking** — on-street, off-street, EV charging
- **Garden maintenance** — outdoor tap, irrigation, hose access

### Output add-on (apartment)

```markdown
### Apartment Specific

**Building**: <units>, built <year>, last major works <year>
**HOA**: <VME / ACP / etc.>
**Monthly charges**: €<X>
**Reserve fund**: €<Y> (= <Z> months of operating)

#### HOA health
- AGM attendance: <%>
- Vote splits: <consensus / contested>
- Outstanding levies: €<X> (next 3 yrs)
- Litigation: <list>

#### Building condition
- Roof age: <Xyr>
- Façade: <last cleaned / repointed>
- Lift: <maintained, no breakdowns>
- Common heating: ✅/❌ (collective / individual)

#### Verdict
- 🟢 Healthy HOA, well-maintained, no surprises
- 🟡 Some deferred maintenance, manageable
- 🟠 Significant assessment levies upcoming
- 🔴 HOA in financial distress / major works required
```

### Output add-on (house)

```markdown
### House Specific

**Type**: <detached / semi-detached / terraced>
**Roof**: <type, age, insulation>
**Heating**: <type, age>
**Plumbing**: <mains drains / septic, age>
**Electrical**: <panel age, RCD, capacity>

#### Boundaries + outdoor
- Bornage: ✅/❌ (date)
- Fence agreement with neighbors: ✅/❌
- Easements: <list>
- Trees protected: <list>

#### Major systems age
- Roof: <Xyr (life expectancy Y)>
- Boiler: <Xyr>
- Plumbing: <Xyr>
- Electrical: <Xyr>

#### Verdict
- 🟢 Modern systems, clean boundaries, no disputes
- 🟡 Minor system updates needed in 5yrs
- 🟠 Major systems aging, significant 5-yr capex
- 🔴 Systems failing + boundary disputes + pre-emption rights
```

---

## How to invoke

```
/property-deep-dive <addr> --all --type=off-plan
/property-deep-dive <addr> --all --type=heritage --journey=foreign-buyer
/property-deep-dive <addr> --all --type=apartment --integrity
/property-deep-dive <addr> --type=plot-only --price --tax
```

Type detection:
- Auto-detected from listing URL or address descriptor where possible
- Manually overridden with `--type=<kind>`

## Output integration

When `--type=<kind>` is requested, the output adds an "## <Type>-Specific Analysis" section after the standard sections.

Multiple types can stack:
- `--type=apartment,heritage` → both sections appear

## Confidence labels

- **HIGH**: Type-specific data accessible (developer registry, HOA documents, heritage register)
- **MEDIUM**: Type-specific check possible but limited (auction with partial legal pack, HOA without minutes)
- **LOW**: Type-specific data unavailable (off-plan with no developer history, plot with no zoning data)

## Forbidden hallucinations

- Never claim "buildable" for plot without checking zoning
- Never claim heritage tax incentive without verifying
- Never minimize off-plan risk without checking guarantees
- Never invent past auction sale prices
- Always surface jurisdictional caveats (consent regime, forced heirship)

## Cross-references

- `--type=off-plan` pairs strongly with `--integrity` (developer due diligence)
- `--type=auction` pairs strongly with `--integrity` (compressed timeline = higher fraud risk)
- `--type=probate` pairs with `--journey=inheritance`
- `--type=plot-only` pairs with `--risks` + `--mains` + `--climate`
- `--type=heritage` pairs with `--tax` (heritage incentives)
- `--type=apartment` pairs with `--rental` (HOA may restrict short-let)
