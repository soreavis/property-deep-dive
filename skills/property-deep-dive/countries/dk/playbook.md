# Denmark 🇩🇰 — Property Due-Diligence Playbook

ISO2: `dk`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1050` København K, `2000` Frederiksberg, `8000` Aarhus C, `5000` Odense, `9000` Aalborg)
- **Admin levels**: 5 regioner + 98 kommuner (post-2007 reform)
- **Currency**: **DKK** (Danish krone) — pegged to EUR via ERM II at a central rate of **7.46038 ± 2.25%** (krone in ERM II since 1 Jan 1999; 2026 data, source nationalbanken.dk Exchange rates + European Commission ERM II page); effectively stable
- **Languages**: Danish (official); German minority (Sønderjylland)
- **Cadastre**: **Geodatastyrelsen** (`https://gst.dk/` — matriklen, cadastral maps and data) + **Klimadatastyrelsen** (successor of Styrelsen for Dataforsyning og Effektivisering: renamed Styrelsen for Dataforsyning og Infrastruktur on 7 Jun 2022, now Klimadatastyrelsen — source klimadatastyrelsen.dk news archive) + **Tinglysning.dk** (national land register run by Tinglysningsretten, Hobro; fully digital since 8 Sep 2009 — source Tinglysningsretten, domstol.dk)
- **Identifier**: matrikelnummer + ejerlavskode (`12a, Roskilde Markjorder`)
- **Ownership types** (share of occupied dwellings, computed from DST BOL101: 2,872,738 dwellings with CPR-registered residents; 2026 data, stock at 1 Jan 2026, source DST statbank BOL101):
  - **Ejerbolig** (owner-occupied, ~47%)
  - **Andelsbolig** (cooperative — major form, ~7% national, ~28% in København kommune, ~26% in Frederiksberg) — you own a share, not the unit
  - **Almene boliger** (social housing, ~20%)
  - **Private lejeboliger** (rented from companies, private persons or other owners, ~24%); public-authority rentals ~1.6%

## Section: `--price`

### Primary sources

- **Vurderingsstyrelsen** (Property Assessment Agency): `https://vurdst.dk/` — official assessments
  - **Vurderingsportalen**: `https://www.vurderingsportalen.dk/` — consumer access
- **OIS (Den Offentlige Informationsserver)**: `https://www.ois.dk/` — state property-data server (BBR, vurderinger, historic sales prices); free look-ups for private persons, sales prices fed from the tinglysning of each trade (source ois.dk; Bolius — secondary)
- **Boligejer.dk**: BBR, lokalplaner, salgspriser, vurderinger, matrikel, energimærker and tilstandsrapporter in one place (per borger.dk)
- **BBR (Bygnings- og Boligregistret)**: `https://bbr.dk/forside` — all buildings + dwellings register
- **Tinglysning.dk**: `https://www.tinglysning.dk/` — land register; FREE viewer, paid certified extracts
- **Boliga**: `https://www.boliga.dk/` — sold prices map + listings (combines OIS + listings)
- **Boligsiden**: `https://www.boligsiden.dk/` — major listings
- **Danmarks Statistik (DST)** — `https://www.dst.dk/`; sales of real property EJEN77 (quarterly, by landsdel) and EJ131 (monthly, by region), price index EJ99, via `https://www.statbank.dk/`
- **Danmarks Nationalbank** — financial stability
- **Finans Danmark — Boligmarkedsstatistikken**: `https://rkr.statistikbank.dk/` — quarterly average kr/m² of realised free-market sales and sales counts for parcel-/rækkehuse, ejerlejligheder and fritidshuse since 1992, by region, landsdel, kommune and postnr (industry association — secondary). Realkreditrådet was dissolved as a separate association in April 2025 and fully integrated into Finans Danmark (source finansdanmark.dk/om-os/historie)

### Listing platforms

- **Boligsiden** — owned by estate agents and agent chains; receives listings directly from all professional agents and property lawyers; sold-price search: `https://www.boligsiden.dk/` (per boligsiden.dk "Om Boligsiden" — listing platform, seller-controlled)
- **Boliga** — self-described largest independent portal; sold prices back to 1992: `https://www.boliga.dk/` (per boliga.dk — listing platform)
- **home** (`home.dk`, Danske Bank group chain), **EDC** (`edc.dk`), **RealMæglerne** (`realmaeglerne.dk`), **Nybolig** (`nybolig.dk`), **danbolig** (`danbolig.dk`), **Estate** (`estate.dk`) — agency networks
- **Lokalbolig.dk** — alternative

### 2025–2026 price benchmarks (Finans Danmark Boligmarkedsstatistikken + DST)

| Area | Ejerlejlighed DKK/m² — 2025 Q1–Q4 range → 2026 Q2 | Parcel-/rækkehus DKK/m² — 2025 Q1–Q4 range → 2026 Q2 |
|---|---:|---:|
| **København K (postnr 1000–1499)** | 69,520–79,712 → 86,598 | too few sales (2025 Q2 65,323; Q3 77,039; other quarters suppressed) |
| **København kommune** | 57,331–68,180 → 75,120 | 56,649–60,802 → 65,642 |
| **Frederiksberg kommune** | 64,345–76,290 → 83,530 | 82,820–95,234 → suppressed (2026 Q1 87,689) |
| **Københavns omegn (landsdel)** | 38,266–42,126 → 48,247 | 39,968–43,524 → 47,011 |
| **Aarhus kommune** | 36,818–39,476 → 43,424 | 27,326–29,254 → 31,243 |
| **Odense kommune** | 23,028–24,871 → 26,005 | 17,898–19,598 → 21,029 |
| **Aalborg kommune** | 19,128–19,668 → 21,406 | 15,361–16,037 → 16,298 |
| **Vest- og Sydsjælland (landsdel)** | 15,364–17,012 → 18,081 | 11,092–11,582 → 12,168 |
| **Fyn / Sydjylland / Vestjylland / Nordjylland (landsdele)** | 13,657–22,579 → 16,270–22,839 | 9,287–13,134 → 9,612–13,964 |
| **Hele landet** | 36,754–40,835 → 44,816 | 17,445–18,401 → 19,521 |
| **Fritidshus (sommerhus), hele landet** | n/a | 22,287–23,335 → 25,164 (fritidshus category) |

_Source: Finans Danmark Boligmarkedsstatistikken — BM010 (kommune / landsdel) and BM011 (postnr), average kr/m² of realised free-market sales, quarterly (2025–2026 data, source rkr.statistikbank.dk; industry association — secondary, cross-check comparables on OIS / Boliga sold prices). Kommune, landsdel and postnr averages, never a parcel-level value. Average price per one-family house, ordinary free trade, 2025 Q1–Q4 (DST EJEN77, primary): Byen København DKK 7.41–8.37m; Københavns omegn 6.15–7.20m; Østjylland 2.97–3.19m; Fyn 2.17–2.23m; Nordjylland 1.81–1.93m; hele landet 2.97–3.22m (2026 Q2: 3.13m). Weekend cottages, hele landet: DKK 1.97–2.05m (2026 Q2: 2.12m) (2025–2026 data, source DST statbank EJEN77)._

### Compute

1. DKK/m² = price / **boligareal** (BBR-registered area)
2. **OIS sale prices** = official, post-completion
3. **Andelsbolig math**: andel pris (share value) ≠ market value; capped by the maksimalpris rules in Andelsboligforeningsloven § 5 and by the andelskrone the generalforsamling sets, typically when it approves the annual accounts (source danskelove.dk transcription of § 5 + abf-rep.dk — secondary; verify the current text at retsinformation.dk)
4. **Energimærke** — 9 steps A2020, A2015, A2010, B, C, D, E, F, G (A2020 best); valid 10 years (source ens.dk "Det viser energimærket" + sparenergi.dk). F–G flags high retrofit exposure; lender treatment varies — verify with the realkreditinstitut
5. Cross-check sold prices via Boliga + Vurderingsportalen

### Andelsbolig specific (CRITICAL)

For andelsbolig, you must check:
- **Andelskrone** — (property value + other assets − association debt) ÷ members' original indskud; your andel's ceiling = andelskrone × your indskud, within the § 5 cap — not a per-m² value (source taenk.dk + abf-rep.dk — secondary)
- **Generalforsamlingsreferat** (general assembly minutes) — financial health
- **Årsregnskab** + **vedligeholdelsesplan** — backlog repairs
- **Foreningens gæld** (cooperative debt) — high debt = repair backlog risk
- **Andelsforeningens vedtægter** — what you can/can't do
- **Belåningsgrad** (ratio of debt to value) — high = restructuring risk

### Key terms

- Ejerbolig = freehold
- Andelsbolig = cooperative
- Sommerhuse = summer cottage (different zone + tax)
- BBR-meddelelse = building register notice
- Boligskat = combined property tax
- Tinglysning = registration

---

## Section: `--traffic`

### Sources

- **Vejdirektoratet**: `https://www.vejdirektoratet.dk/` — road agency
- **Vejman.dk** — road-management system used jointly by Vejdirektoratet and the kommuner (for road authorities; 2026 data, source vejman.dk); kommuner can load Mastra counts into their Vejman traffic register (source mastra.vd.dk, "Hvad er Mastra")
- **Mastra** — Vejdirektoratet's shared IT system for processing and storing traffic counts (ÅDT, JDT, Æ10); its key-figure database holds counts from Vejdirektoratet and the kommuner that have bought kMastra access (source mastra.vd.dk, "Hvad er Mastra")
- **Public counts**: Vejdirektoratet "Trafiktællinger og statistikker på kort" — `https://www.vejdirektoratet.dk/viden-og-data/trafik-og-mobilitet/trafikkens-udvikling-i-tal/trafiktaellinger`; for kommune roads ask the kommune's vejmyndighed

### Key term

**ÅDT (Årsdøgntrafik)** = AADT-equivalent: 1/365 of the total two-way traffic on a road section over a full year (source Vejdirektoratet, "Trafiksikkerhedsberegninger og ulykkesbekæmpelse").

### Verdict bands

- 🟢 < 1,500 v/d (boligvej, residential street)
- 🟡 1,500–10,000 v/d (kommunal vej, urban arterial)
- 🟠 10,000–30,000 v/d (statsvej, motortrafikvej)
- 🔴 > 30,000 v/d (motorvej, urban core E-vej)

---

## Section: `--tax`

### Annual property tax — Boligskat (MAJOR REFORM 2024)

**1 January 2024 reform** combined two old taxes into single **boligskat**:

#### Components

1. **Grundskyld** (land tax):
   - Base: 80% of grundværdi (precautionary 20% deduction)
   - Rate: one flat **kommunal grundskyldspromille** on that base, no progression (the 0.51% / 1.4% rates belong to ejendomsværdiskat)
   - **Kommunale promille (ejerboliger)**: **3.1‰ (Frederiksberg) to 17.7‰ (Varde)** across the 98 kommuner; København 5.1‰, Aarhus 6.0‰, Odense 5.7‰, Aalborg 7.4‰ (2026 data, source vurderingsportalen.dk Kommunale grundskyldspromiller for ejerboliger)
   - Statutory ceiling **30‰** (Ejendomsskatteloven § 28); in 2024-2028 a kommune cannot raise its rate above the rate set for it in ESL bilag 1, and the pre-2024 16‰ minimum was not carried over (2026 data, source skm.dk Ejendomsskatteloven satser + info.skat.dk C.H.4.3.4.4)
2. **Ejendomsværdiskat** (property value tax):
   - Base: 80% of ejendomsværdi (full property value, also 20% reduction)
   - Rate: **0.51%** up to the progressionsgrænse / **1.4%** above (2026 data, source skm.dk Ejendomsskatteloven satser)
   - Progressionsgrænse (applied to the 80% beskatningsgrundlag): **DKK 9,200,000 in 2024-2025, DKK 9,007,000 in 2026 and 2027** — regulated every second year by an ejerboligværdiindeks, not by Personskattelovens § 20 (2026 data, source skm.dk Ejendomsskatteloven satser + vurderingsportalen.dk Ejendomsværdiskat af din ejerbolig + info.skat.dk C.H.4.2.5.2)
   - The 2024 reform lowered the general rate from 0.92% (in force from 2021) to 0.51% (source skm.dk Skatteøkonomisk Redegørelse 2021 + skm.dk Ejendomsskatteloven satser); the 20% forsigtighedsnedslag already applied to the current valuation from 2021, but most owners were then taxed on the lower 2001/2002 skattestop value (source skm.dk Skatteøkonomisk Redegørelse 2021, Boks 6.1)
   - Applies to ejerbolig + sommerhus only

#### Collection (NEW since 2024)

- Both collected via **statskat** (state tax) — pulled from your **forskudsopgørelse** (preliminary tax return)
- No longer kommune-direct
- 2025 + 2026 use **preliminary 2024 valuation**; final adjustment retroactive

#### Skatterabat + stigningsbegrænsning (transition)

- **Skatterabat**: natural persons who owned their ejerbolig before 1 Jan 2024 and whose combined boligskat for 2024 was higher under the new rules got a permanent rabat fixed in kroner on the 2024 årsopgørelse (2024 tax under the new rules minus the 2024 tax the old skattestop / grundskatteloft rules would have produced); most owners got a tax cut in 2024 and no rabat. The rabat runs while they own the home and **lapses on sale** (transfers between spouses excepted), so a buyer does not inherit it and can face a higher boligskat than the seller paid (source vurderingsportalen.dk Skatterabat + info.skat.dk C.H.4.5.1)
- **Stigningsbegrænsning for grundskyld**: grundskyld may rise at most **4.75%/yr** (**3.5%** for almene boliger) from 2025 (2026 data, source skm.dk Ejendomsskatteloven satser); it covers owners outside the rabat scheme (erhvervsejendomme, lejeboliger, legal-person owners), not natural persons who take over an ejerbolig on or after 1 Jan 2024, and it is phased out regardless of ownership change (source info.skat.dk C.H.4.6.1); the ministry projected most erhverv rabatter run off after ~20 years (2021 projection, source skm.dk Skatteøkonomisk Redegørelse 2021 — rates/figures may have changed since)

### Transaction taxes

- **Tinglysningsafgift** (registration fee): **0.6% + DKK 1,850** of the purchase price for the skøde (ejerskifte); **1.25% + DKK 1,825** per pantebrev on the secured amount — variable rate cut from 1.45% on 1 Jan 2026 (2026 data, source skm.dk Tinglysningsafgiftsloven satser + skat.dk notice 01-12-2025)
- **No general transfer tax** beyond tinglysning — **lowest in W. Europe**
- **Mæglersalær** (broker): est. **1.5–3%** of price, paid by seller and negotiable (no published tariff — compare brokers' written quotes)
- **Notar fees**: not mandatory in DK (advokat optional)

### Total transaction cost (buyer side)

- Cash purchase: **0.6% + DKK 1,850** tinglysningsafgift plus own adviser fee
- Financed purchase: add **1.25% + DKK 1,825** per pantebrev on the borrowed amount — e.g. DKK 3,000,000 price, 95% loans in two pantebreve: 0.6% × 3,000,000 + 1,850 = 19,850; 1.25% × 2,850,000 + 2 × 1,825 = 39,275; total **DKK 59,125 ≈ 2.0% of price** (computed, 2026 rates per skm.dk Tinglysningsafgiftsloven satser), before adviser, loan-establishment and ejerskifteforsikring costs

### Capital gains

- **Ejerbolig (Ejendomsavancebeskatningsloven §8 'parcelhusreglen', LBK nr 132 af 25/01/2019)**: capital gain on primary residence often **EXEMPT** if it served as home for the owner or household during part or all of the ownership and the total plot is **under 1,400 m²** (or a public authority bars subdivision, or Skattestyrelsen declares subdivision would cut the value of the rest by more than 20%); sommerhus → §8 stk. 2 (2026-10-23 verified, source [retsinformation.dk](https://www.retsinformation.dk/eli/lta/2019/132))
- **Sommerhus (sommerhusreglen)**: similar exemption if for personal use during ownership
- **Investment property**: gain taxed as kapitalindkomst for private individuals (classification per secondary sources Colliers / From Regnskab) — marginal up to **42%** (skatteloft on positive nettokapitalindkomst 42.0% in 2025 and 2026; lowest positive-kapitalindkomst marginal 37.1% in 2025, average kommune excl. kirkeskat) (2026 data, source skm.dk Centrale skattesatser); **22%** selskabsskat if held in a company (2025-niveau, source info.skat.dk C.D.10.4.9.1, SEL § 17; virksomhedsskat also 22% for 2026 per skm.dk Centrale skattesatser) — the 2027 finance bill proposes a 3-percentage-point selskabsskat cut from 2030, not legislated (secondary: Ritzau via berlingske.dk); systematic property dealing (næring) is taxed as personal income (secondary: From Regnskab)

### VAT (moms)

- 25% standard (2026 data, source skat.dk)
- Resale of buildings that are not new is exempt — as a rule, buildings older than 5 years with their land fall outside moms (source info.skat.dk)
- New buildings (with land) and byggegrunde sold by a business: 25% moms since 1 Jan 2011 (lov nr. 520 af 12. juni 2009), charged by the seller and included in the price (source info.skat.dk)

### Future risk

- **Skatterabat lapses on sale**: each resale moves a home onto full new-rule boligskat without the seller's rabat (source vurderingsportalen.dk Skatterabat)
- **Rentefradrag cap PROPOSED** in the 2027 finance bill (L 73), effect from 2028 only if a separate tax bill passes — see Active fiscal incentives
- **Andelsbolig taxation** debated periodically

---

## Section: `--rental`

### Long-term residential

- **Lejeloven** (Tenancy Act): tenant-protective; particularly strict in older buildings (pre-1992)
- **Boligreguleringsloven** (rent regulation in _regulerede kommuner_): **merged into the new Lov om leje, in force 1 July 2022** — § 205 repeals the old lejelov (LBK 927/2019) and boligreguleringsloven (LBK 929/2019), while the huslejeregulering rules for _regulerede kommuner_ carry over without substantive change; rent control was consolidated, not abolished (2021 bill data, source retsinformation.dk LSF 47 2021/1 + ft.dk L 47 hearing note); housing-standard rules sit in the companion Lov om boligforhold
- **Andelsbolig rules**: members of housing association; specific share-purchase rules
- **Tidsbegrænsede aftaler** common
- **Indekslejekontrakt** (NPI-linked rent): a temporary cap limited rent increases from the nettoprisindeks for 2022 and 2023 to **4% per year** (Lov om ændring af lov om leje og lov om boligforhold, 2022 — source retsinformation.dk LSF 210 2021/1); per ejendomsdrift.dk (secondary) the cap covered only those two index years and its § 53 a exception was repealed 1 Jan 2025 — verify against the current lejelov

### Short-let (Airbnb / udlejning)

- **Short-letting your own full helårsbolig** (Sommerhusloven, LBK nr. 400 af 12/04/2024; supervised by Plan- og Landdistriktsstyrelsen) — national rule, no København-specific cap:
  - **30 days/calendar year** unless let solely through a bureau/platform that reports the full rent to Skattestyrelsen
  - **70 days/calendar year** when let only through such a reporting bureau/platform (skatteindberetningslovens § 43)
  - The kommunalbestyrelse may raise the 70-day cap to at most **100 days**, never lower; plst.dk lists the kommuner that have done so (2026 data, source plst.dk "Egen fulde helårsbolig til feriegæster")
- **Moms (VAT)**: letting rooms, or a flat integrated in your own home, for < 1 month is VAT-liable once annual DK turnover exceeds **DKK 50,000** (register on virk.dk); a whole self-contained dwelling or a sommerhus is VAT-exempt whatever the letting period (2026 data, source skat.dk "Moms ved udlejning af værelser og boliger")
- **Sommerhuse** (summer cottages): private, non-commercial letting needs no permit, and letting 1–2 sommerhuse is normally not commercial when the owner also uses them; commercial letting, or letting for more than 1 year, needs PLST permission, which as a rule is not granted outside narrowly defined cases (source plst.dk "Ferieboliger, fleksboliger og værelser m.v." + PLST practice note)
- Platform income is reported to Skattestyrelsen (DAC7, since 1 Jan 2023) and shows in TastSelv under Skatteoplysninger (source skat.dk)

### Tax on rental

- **Bundfradrag, own home let short-term (< 4 months)**: **DKK 35,100** (2026; 33,500 in 2025) via a platform that reports to Skattestyrelsen; **DKK 13,800** (2026; 13,100 in 2025) without one (2026 data, source skat.dk)
- **Bundfradrag, sommerhus/fritidsbolig**: **DKK 50,200** (2026; 47,900 in 2025) via a reporting platform; **DKK 13,800** (2026) for private letting (2026 data, source skat.dk)
- **Above bundfradrag**: 40% of the excess is deducted and the remaining 60% is taxed (kapitalindkomst for an owner); a regnskabsmæssigt fradrag of documented costs can be chosen instead (source skat.dk)
- **Kapitalindkomst** if pure investment property

---

## Section: `--work=<profession>`

### Sources

- **Jobnet.dk** (state job platform, Styrelsen for Arbejdsmarked og Rekruttering): `https://www.jobnet.dk/`
- **Jobindex.dk**, **LinkedIn DK**, **Workindenmark.dk** (English-language vacancies via `workindenmark.jobnet.dk`; EURES advisers)
- ~~OfferOgEfterspørgsel.dk~~ ❌ DEPRECATED — dead on 2026-10-23 (domain does not resolve); verify with Jobnet.dk (STAR)
- **Brancheforeninger** for profession bodies

### Self-employment

- **Enkeltmandsvirksomhed** (sole trader): no min capital
- **ApS** (Anpartsselskab): limited company, **min DKK 20,000 capital** (cut from DKK 40,000; Erhvervsstyrelsen guidance updated 28 Feb 2025 — 2025 data, source erhvervsstyrelsen.dk)
- **A/S** (Aktieselskab): public limited, min DKK 400,000 (2025 data, source erhvervsstyrelsen.dk)
- **CVR registration** mandatory
- **Moms** (VAT): registration once annual DK turnover exceeds DKK 50,000 (2026 data, source skat.dk)
- **AM-bidrag** 8% (skat.dk) + kommuneskat + **bundskat 12.01%**, **mellemskat 7.5%** above DKK 641,200, **topskat 7.5%** above DKK 777,900, **toptopskat 5%** above DKK 2,592,700 (personal income after AM-bidrag; 2026 data, source skat.dk); marginal rate incl. AM-bidrag ~42% / ~49% / ~56% / ~60.5% across those bands (est., PwC 2025 press release using average kommuneskat — secondary)

### Salary benchmarks (2025)

- Standardised monthly earnings, all sectors — average / median (DST LONS30 _standardberegnet månedsfortjeneste_: base pay, nuisance bonuses, fringe benefits, irregular payments, pension contributions and holiday pay, excl. overtime and absence pay, on a 37-hour week; median computed as DST median standardised hourly earnings × 160.33 h):
  - Region Hovedstaden (København): DKK 57,773 / ~52,170
  - Region Midtjylland (Aarhus): DKK 50,316 / ~46,590
  - Region Syddanmark (Odense): DKK 49,835 / ~45,880
  - Region Nordjylland (Aalborg): DKK 48,209 / ~45,370
  - Region Sjælland: DKK 49,114 / ~46,380
  - Hele landet: DKK 52,846 / ~48,060
  - Region level only — LONS30 has no city or rural split; by occupation see DST LONS20 (2025 data, source DST statbank LONS30)
- **Ingen lovbestemt mindsteløn** (no statutory minimum wage); pay floors come from collective agreements. The CJEU (C-19/23, 11 Nov 2025) annulled the minimum-wage directive's criteria for statutory minimum wages and upheld the rest (source bm.dk press release 11-11-2025)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **DMI (Danmarks Meteorologiske Institut)** | `https://www.dmi.dk/` | Weather, climate |
| **Naturstyrelsen** | `https://naturstyrelsen.dk/` | Nature management |
| **Kystdirektoratet** (part of Miljøstyrelsen) | `https://mst.dk/erhverv/kyster-og-klimatilpasning` (kyst.dk redirects here, 2026-10-23) | Coastal erosion, coastal protection, dige map, højvandsstatistik |
| **Naturskaderådet** (Stormrådet until 1 Jul 2022) | `https://naturskaderaadet.dk/` | Declares stormflod / oversvømmelse / tørke events; complaints over insurers' naturskade decisions |
| **Klimatilpasning.dk** | `https://klimatilpasning.dk/` | Climate adaptation portal — kommune plans |
| **GEUS (Geological Survey)** | `https://www.geus.dk/` | Geology, radon |
| **Sundhedsstyrelsen radon** | `https://www.sst.dk/vidensbase/straalebeskyttelse/fakta-om-ioniserende-straaling/radon-i-boliger/kort-over-radon-i-danmark` | Radon map (2001 national survey, old-kommune level) |
| **Social- og Boligstyrelsen** | `https://www.sbst.dk/byggeri/sikre-og-sunde-bygninger/radon` | Radon rules for buildings + recommended action levels |
| **DCE (Aarhus Univ. environment)** | `https://dce.au.dk/` | Pollution |
| **HOFOR + provincial floodmaps** | per kommune | Local flood |

### Specific risks

- **Stormflod** (storm surge) — coastal regions, major + increasing:
  - **Stormflodsordningen** — state storm-surge scheme administered by **Naturskaderådet** (named Stormrådet until 1 Jul 2022); it pays only when the damaged building or contents is brandforsikret, the damage is not covered by ordinary insurance, and the council has declared stormflod for that coast stretch — a sea level statistically rarer than a 20-year event per Kystdirektoratet's højvandsstatistik (2026 data, source naturskaderaadet.dk)
  - Reference events (DMI): 11 Oct 1634 Vadehavet (6.3 m, Ribe); 12–14 Nov 1872 Baltic — Lolland, Falster, Sønderjylland east coast, over 3 m, about 250 dead; 24 Nov 1981 Esbjerg 4.3 m (DMI's highest reading in the harbour); 3 Dec 1999 Vadehavet (Ribe 5.1 m when the gauge failed); **20–21 Oct 2023** Baltic — 216 cm over daily water at Aabenraa, hardest on southern Lillebælt, also high south of Fyn, Lolland and Falster up to Køge; worst Danish Baltic surge since 1904 but 1–1.5 m below 1872 (DMI, 23 Oct 2023); largest total payout in the stormflod scheme's history (Naturskaderådet beretning 2023)
  - Naturskaderådet's published rules contain no property-level storm-surge rating; buyer checks are **BBR** (every building-damage payout from the stormflod / oversvømmelse / tørke schemes is registered there for future buyers — Naturskaderådet) and Kystdirektoratet's dige map (a property on the sea side of a dige gets no cover — Lov om visse naturskader § 4 stk. 2 nr. 6)
- **Oversvømmelse** (river/precipitation flooding) — primarily flat lowlands, river basins (Vidåen, Skjernåen)
- **Kysterosion** — Lodbjerg–Nymindegab (central Vestkyst) is Denmark's most erosion-exposed coast: average retreat **1–8 m/yr without protection** (Miljøstyrelsen / Kystdirektoratet), held by sand nourishment of 3.8m m³/yr under the state–kommune fællesaftale (DKK 1.3bn to 2029, signed 2 Feb 2026) (2026 data, source Miljøministeriet); Lønstrup Klint 1.25 m/yr as a 100-year average (2016 data, source GEUS Geoviden — rates/figures may have changed since) — check whether the property's stretch lies inside a protected section
- **Earthquake**: very low — Denmark lies inside a tectonic plate; strongest instrumentally recorded quake 4.7 ML (Kattegat, 15 Jun 1985), strongest on land 4.6 ML (Krik Vig, 1954) (GEUS, 2018); 20 May 2026 Køge Bugt 3.9, felt across Sjælland; GEUS knows of no personal injury from earthquakes in Denmark (GEUS, May 2026)
- **Radon**: highest shares in parts of Fyn and Bornholm — over 10% of single-family houses above 200 Bq/m³, against about 5% nationally and under 1% in Nordjylland (2001 data, source national survey by SIS / Risø / GEUS, old-kommune level, not parcel-level — rates/figures may have changed since); Sundhedsstyrelsen: only a measurement shows a home's level, also for buildings from after 1998; Social- og Boligstyrelsen recommends reducing above **100 Bq/m³** — simple, cheap fixes at 100–200, more effective measures above 200 — and new builds must stay below 100 Bq/m³, with radon protection required since 1998 (2026 data, source sbst.dk)
- **Skogsbrand** (wildfire): increasing in heath + dry summers (Vestjylland, Hedeområde)
- **Saltvandsindtrængning** (saltwater intrusion) — coastal wells, Sjælland
- **Skred (landslides)**: low nationally; cliff slumps at Stevns Klint, Møns Klint and Lønstrup Klint; damage from a collapsed klint or skrænt is NOT covered by the naturskade schemes (indirect loss — Naturskaderådet FAQ, Lov om visse naturskader § 4)

### Insurance

- **Naturskaderådet** (Stormrådet until 1 Jul 2022) administers the state schemes for stormflod, oversvømmelse from watercourses and lakes, tørke (drought, since 1 Jul 2022) and stormfald; insurers receive and decide stormflod / oversvømmelse / tørke claims, the council declares events, hears complaints and supervises insurers (source naturskaderaadet.dk)
- Ordinary insurance on ordinary terms does not cover stormflod; the state schemes are funded by a **naturskadeafgift of DKK 40/yr per fire-insurance policy** (DKK 30 stormflod / oversvømmelse / tørke + DKK 10 stormfald; a DKK 20 surcharge applies while the pool draws on the state guarantee and its equity is below DKK 500m) (2025 data, source Naturskaderådet Årsrapport 2025)
- Exclusions that matter to buyers: property on the sea side of a dige, contents in a basement not approved for habitation, soil wash-out, garden structures, and most garages and carports (negativlisten, Lov om visse naturskader § 4 stk. 2)
- The oversvømmelsesordning covers only declared floods from watercourses and lakes; Naturskaderådet's preliminary assessment of 4 Sep 2026 is that floods after the 31 Aug 2026 heavy rain are not covered (source naturskaderaadet.dk)
- Mårup Kirke (south of Lønstrup) was taken down because of the cliff-collapse threat (GEUS, 2016); ask the kommune whether any local support exists for erosion-threatened homes

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, weak insulation, asbestos cement starts, lead |
| **1900–1960** | Lead paint, asbestos, weak insulation |
| **1960s–1980s "betonbyggeri"** | Asbestos very common, energy-inefficient, **PCB in fugemasse and termoruder 1950–1977** (banned in building materials in 1977 — Miljøstyrelsen) |
| **1980s–2010** | Improving insulation, modern wiring |
| **Post-2010 BR15/BR18** | Strict |
| **Post-2018 BR18** (in force 1 Jan 2018) | Energy requirements largely the same as BR15 (new builds get energimærke A2015); the lavenergiklasse (former bygningsklasse 2020, energimærke A2020) stays voluntary after 2020 (bygningsreglementet.dk BR18 ch. 25 guidance; Energistyrelsen) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energimærke** | Required at sale or letting for buildings of 60 m² or more (flats: one label for the whole building); the seller must hand it to the buyer (2026 data, source Energistyrelsen) | 10 years (extended from 7 to 10 years retroactively in 2017 — SparEnergi) |
| **Tilstandsrapport** (condition report by a beskikket bygningssagkyndig) | Voluntary; the seller provides it to the buyer. The seller is freed of the 10-year seller liability for the building's physical condition only if, before the buyer's offer is accepted, the buyer has received the tilstandsrapport, an elinstallationsrapport and an ejerskifteforsikring offer, and the seller has promised in writing to pay at least half the premium (Lov om forbrugerbeskyttelse ved erhvervelse af fast ejendom § 2, LBK nr. 1123 of 22 Sep 2015, in force 2026; Sikkerhedsstyrelsen, part of Erhvervsstyrelsen since Jan 2026) | 6 months — made or renewed less than 6 months before the buyer receives it (same law § 4) |
| **Elinstallationsrapport** (electrical) | Required with the tilstandsrapport for the huseftersyn liability release and for ejerskifteforsikring | 12 months (2020 data, source Sikkerhedsstyrelsen — rates/figures may have changed since) |
| **BBR-meddelelse** | Building register notice | At sale |
| **Tinglysningsudskrift** | Land register extract | At sale |
| **Servitutter** (easements) review | Per case | At sale |

### Climate change projections (DMI)

Median change 2071–2100 vs 1981–2010 for low / medium / very high emissions (RCP2.6 / RCP4.5 / RCP8.5; sea level on SSP1-2.6 / SSP2-4.5 / SSP5-8.5) (2025 data, source DMI Klimaatlas v2025a national report):
- Annual mean temperature **+1.0 / +1.9 / +3.4 °C** (10th–90th percentile across the three scenarios 0.7–4.2 °C)
- Winter precipitation **+5.7 / +12.2 / +22.6%**; summer totals close to today but more often from heavy showers; number of cloudbursts +24 / +40 / +65%
- Mean sea level by coast stretch: Nordsjællands kyst +29 / +36 / +54 cm, Femern Bælt +39 / +47 / +64 cm, northern Vadehavskyst +40 / +48 / +66 cm; very-high-scenario 90th percentile up to +125 cm; rise smallest in Nordjylland and largest in SW Jylland (post-glacial land uplift)
- Today's 20-year storm surge can occur every second year (medium scenario)
- These are coast-stretch and national values, not parcel-level — use the kommune report in DMI Klimaatlas

---

## Section: `--mains`

### Sources

- **Danva** (national water utility assoc): `https://www.danva.dk/`
- **HOFOR** (København): `https://www.hofor.dk/`
- **Aarhus Vand**, **Aalborg Forsyning** (drinking water via its subsidiary Aalborg Vand A/S), **VandCenter Syd** (Odense + Nordfyn; water + wastewater DKK 65.98/m³ combined, 2026 data, source vandcenter.dk)
- Universal in urban; sommerhuse + rural may be on individual systems

### Verification

- Most populated areas: kommunal mains universal
- **Sommerhusområder**: many on **slamafskillere** (septic) + **nedsivning**
- **Tank tømning** (sludge collection): where the kommune runs a tømningsordning for bundfældningstanke, owners must use it (source Miljøstyrelsen)

### Costs

| Scenario | Cost (DKK), est. |
|---|---:|
| Tilkobling to mains | est. 80,000–250,000 |
| Mains-line extension | est. 200,000–800,000 |
| Slamafskiller upgrade | est. 80,000–150,000 |
| Mini-renseanlæg | est. 100,000–250,000 |
| Borebrønd (drilled well) | est. 60,000–120,000 |

_Ranges are order-of-magnitude estimates (not tied to a published tariff); actual cost depends on distance to mains, kommune VVS schedule, and ground conditions — confirm with a kloakmester quote + your kommune's tilslutningsbidrag tariff._

---

## Cost benchmarks (DK 2026)

| Work | Cost (DKK) |
|---|---:|
| Energimærke | est. 4,000–10,000 |
| Tilstandsrapport | est. 8,000–18,000 |
| Elinstallationsrapport | est. 4,000–8,000 |
| Tinglysningsafgift (køb / skøde) | 0.6% + 1,850 (2026) |
| Tinglysningsafgift (pant, per pantebrev) | 1.25% + 1,825 (2026; 1.45% until 31 Dec 2025) |
| Mæglersalær | est. 1.5–3% of price (seller) |
| **Total transaction cost (buyer)** | **~2.0%** of price in registration fees for a 95%-financed purchase (computed, see note), before adviser + loan fees |
| Septik to mains | est. 80,000–250,000 |
| Roof (slate, 150 m²) | est. 200,000–400,000 |
| Energy retrofit (Class C → A) | est. 500,000–1,200,000 |
| Asbestos abatement | est. 100,000–400,000 |
| Radon mitigation | est. 30,000–80,000 |
| PCB removal (fugemasse, apartment) | est. 200,000–500,000+ |

_Report-fee, mæglersalær and renovation/abatement ranges are order-of-magnitude estimates (not from a published tariff or price book); calibrate against a Bolius/Molio price book or contractor quotes for the specific property. Tinglysningsafgift rows: 2026 data, source skm.dk Tinglysningsafgiftsloven satser. Total (computed): DKK 3,000,000 price with 95% loans in two pantebreve → 0.6% × 3,000,000 + 1,850 = 19,850 plus 1.25% × 2,850,000 + 2 × 1,825 = 39,275 → DKK 59,125 ≈ 2.0% of price._

## Active fiscal incentives (2025-2026)

- **Bygningspuljen**: ❌ CLOSED — open 2020-2022 only; from 2023 split into Energirenoveringspuljen and Varmepumpepuljen (source sparenergi.dk, page updated 25.03.2026 + kefm.dk Puljer og omstillingsstøtte)
- **Energirenoveringspuljen** (insulation, windows, ventilation; fixed subsidy percentage; first come, first served): 2026 round opened 27 Jan 2026 with a DKK 51.5m budget; funds allocated through 2026 (2026 data, source sparenergi.dk + ens.dk press release 5 Feb 2026 + kefm.dk)
- **Skrotningsordningen**: up to DKK 25,000 when a gas, oil or wood-pellet boiler is scrapped for a heat pump on subscription (varmepumpe på abonnement); runs through 2026 (2026 data, source sparenergi.dk + kefm.dk)
- **Varmepumpepuljen**: fixed DKK 27,000 grant (air-to-water or ground-source) for a helårsbolig without district-heating access that replaces oil, gas, electric or biomass heating; 2026 budget DKK 116.9m plus DKK 200m added during 2026; funds allocated through 2026; open until 30 Nov 2026 or until funds run out (2026 data, source ens.dk press releases + kefm.dk; closing date per bolius.dk, secondary)
- **Rentefradrag** (deduction for negative net capital income, incl. mortgage interest): tax value ~33% (excl. kirkeskat) on the first DKK 50,000 (DKK 100,000 for couples) and ~25% above (2026 data, source Skatte- og Vækstministeriet factsheet, svmn.dk; 2025: 33.1% / 25.1% per skm.dk Centrale skattesatser), not a flat ~25.6%; no cap today. **PROPOSED, not legislated**: the 2027 finance bill (L 73, tabled 9 Oct 2026 by finance minister Peter Hummelgaard) would cap the deduction at **DKK 150,000/yr** for single people and **DKK 300,000/yr** for married and jointly taxed couples, covering all negative net capital income (mortgage, overdraft and SU-loan interest, bond price losses) regardless of when the loan was taken; the ministry books no 2027 revenue and DKK 600m in 2028, 700m in 2029 and 800m in 2030, so effect from 2028, and it needs a separate tax bill (source svmn.dk factsheet "Loft over fradrag for negativ nettokapitalindkomst" + FSR Danske Revisorer 13 Oct 2026 + lovguiden.dk L 73, secondary)
- **BoligJobordningen**: håndværkerfradrag (grøn istandsættelse) up to **DKK 9,000/yr per person** and servicefradrag up to **DKK 18,300/yr per person**, labour cost only; deduction value ~26% (2026 data, source skat.dk Håndværkerfradrag + Servicefradrag + skm.dk PSL § 20 beløbsgrænser)
- **Boliglån** for first-time buyers (kommune-specific in some cases)

## Common listing platforms

- **Boligsiden** — agent-owned portal fed directly by professional agents (per boligsiden.dk)
- **Boliga** — self-described largest independent portal; sold prices since 1992 (per boliga.dk)
- **home, EDC, RealMæglerne, Nybolig, danbolig, Estate** — agency networks

## Caveats unique to DK

- **Andelsbolig** (cooperative) is a major form, especially in København kommune — 94,824 of 331,766 dwellings with CPR-registered residents = 28.6% (Frederiksberg 14,599 / 55,371 = 26.4%; national 198,969 / 2,872,738 = 6.9%) owned by private andelsboligforeninger (computed, 2026 data, stock at 1 Jan 2026, source DST statbank BOL101; kommune-level, not building-level); you own **shares** in a housing association, not the apartment
  - Andelskrone caps share price; foreningens gæld = main risk
  - **Andelsforeningens financial health** audit critical before buying
  - **Bopælspligt** in some andelsforeninger — must live there
- **Boligskat reform 2024** combined ejendomsværdiskat + grundskyld; 2025-2026 use preliminary 2024 valuations with retroactive adjustment
- **Seller's boligskat ≠ buyer's**: the pre-2024 owner's skatterabat lapses on sale, and the 4.75%/yr grundskyld stigningsbegrænsning covers only owners outside the rabat scheme, not natural persons buying an ejerbolig from 2024 — budget on full new-rule boligskat (2026 data, source vurderingsportalen.dk Skatterabat + info.skat.dk C.H.4.6.1 + skm.dk Ejendomsskatteloven satser)
- **Parcelhusreglen** (primary-residence capital gain exemption) is generous — plot under 1,400 m² (or subdivision barred) + lived in by owner or household for part of the ownership (source retsinformation.dk EBL § 8)
- **Sommerhus rules** distinct: own zone; private, non-commercial holiday letting needs no permit, while commercial (erhvervsmæssig) or longer-than-1-year letting needs Plan- og Landdistriktsstyrelsen permission under sommerhusloven, judged case by case rather than by a fixed night count (2026 data, source planinfo.dk Ferieboliger, fleksboliger og værelser m.v.)
- **Short-let caps (own whole helårsbolig)**: 30 days/yr if the owner lets it directly; up to 70 days/yr if let solely through a bureau or platform that reports the rent to Skattestyrelsen (skatteindberetningsloven § 43); each kommune may raise 70 to at most 100 days and cannot go below 70 — the cap is national, not København-specific (2026 data, source planinfo.dk Egen fulde helårsbolig til feriegæster)
- **Stormflod cover is event-based, not a property rating**: the state stormflodsordning pays only when Naturskaderådet (formerly Stormrådet) declares stormflod — a sea level statistically rarer than once every 20 years — and the damaged property is brandforsikret and not covered by ordinary insurance; fast ejendom outside a dige gets no compensation; once a payout starts it is registered in BBR (check the BBR-meddelelse); Naturskaderådet's stormflod guidance and FAQ set out no property-level rating or risk class (2026 data, source naturskaderaadet.dk)
- **20 Oct 2023 storm surge** = recent reference event for southern coasts
- **Bornholm radon** distinct hotspot
- **PCB in fugemasse 1950–1977** — banned but still in many older buildings
- **MitID** required for tinglysning + tax + Skat services (NemID closed 30 Jun 2023, source digst.dk)
- **Tinglysning fully digital since 2009** — fast registration
- **Boligreguleringsloven repealed 1 July 2022** when lov nr. 341 (leje) and lov nr. 342 (boligforhold) af 22. marts 2022 entered into force (source retsinformation.dk); existing tenants protected via transitional rules
- **Foreign-buyer regime — Lov om erhvervelse af fast ejendom (Erhvervelsesloven)** (2026-10-23 verified, source: civilstyrelsen.dk): anyone who neither has bopæl in Denmark in the act's sense nor has lived in Denmark for 5 years in total needs **Civilstyrelsens tilladelse**; citizenship itself does not matter (permission moved Justitsmin → Civilstyrelsen 9 Jul 2018 — per the 2026-05-27 check, not re-verified). **EU/EEA + Swiss** citizens can buy a helårsbolig without permission when exercising free movement (employee, EU/EEA residence document, self-employed, or sufficient means) by filing a declaration under penalty with Tinglysningsretten that the home is not a fritidsbolig; UK citizens lost this route on 1 Jan 2021. A helårsbolig permission covers one named property, requires lawful residence and use as the year-round home, and moving out before 5 years of DK residence can trigger an order to sell within 6 months. **Sommerhus / any sekundærbolig**: EU/EEA citizens need permission too, granted only for a particularly strong connection to Denmark — mainly long-run holidays here, e.g. at least one week every year for the last 25 years; a forhåndstilsagn is valid 3 years; processing about 3 months (helårsbolig about 4 weeks). Basis: Protocol (No 32) on the acquisition of property in Denmark (TEU/TFEU) — Denmark may maintain its existing legislation on the acquisition of second homes (source eur-lex.europa.eu)
- **Sønderjylland German minority** — bilingual context

## Reddit / forum sources

- **r/Denmark** (active, English-friendly)
- **r/Aarhus**, **r/Copenhagen**, **r/international_denmark** (expats)
- **r/dkfinance** — mortgage + tax discussion
- ~~MyHusum.dk forums~~ ❌ DEPRECATED — dead on 2026-10-23 (domain does not resolve); no replacement identified
- Expat: **The Local Denmark**, **Wonderful Copenhagen**

## Verification authorities

| Authority | When to call |
|---|---|
| **Vurderingsstyrelsen** | Boligskat assessment, valuation |
| **Tinglysningsretten** | Title verification |
| **Kommune** | Permits, planning, BBR |
| **Skat** | Tax calculations, capital gains |
| **Naturskaderådet** (Stormrådet until 1 Jul 2022) | Whether stormflod / oversvømmelse / tørke was declared for the area; complaints over insurers' naturskade decisions |
| **Kystdirektoratet** (Miljøstyrelsen) | Coastal protection, dige map, højvandsstatistik |
| **Sundhedsstyrelsen** + **Social- og Boligstyrelsen** | Radon (map; building rules and action levels) |
| **Andelsforeningens bestyrelse** | If andelsbolig |
| **Mægler / advokat** | Sale process |

## Source URL templates

| Source | URL pattern |
|---|---|
| OIS (Den Offentlige Informationsserver — state property-data server) | `https://www.ois.dk/` |
| Boliga | `https://www.boliga.dk/` |
| Boligsiden | `https://www.boligsiden.dk/` |
| Vurderingsstyrelsen | `https://vurdst.dk/` |
| Vurderingsportalen | `https://www.vurderingsportalen.dk/` |
| Tinglysning | `https://www.tinglysning.dk/` |
| BBR | `https://bbr.dk/forside` |
| Vejdirektoratet | `https://www.vejdirektoratet.dk/` |
| Klimatilpasning | `https://klimatilpasning.dk/` |
| Skat (tax) | `https://www.skat.dk/` |
| GEUS | `https://www.geus.dk/` |
| Naturskaderådet (formerly Stormrådet; stormraadet.dk redirects) | `https://naturskaderaadet.dk/` |
| Kystdirektoratet (Miljøstyrelsen; kyst.dk redirects) | `https://mst.dk/erhverv/kyster-og-klimatilpasning` |
| DMI Klimaatlas national report | `https://download.dmi.dk/Research_Projects/klimaatlas/v2025a/kommune_reports/DMI_Klimaatlas_v2025a_Danmark_rapport.pdf` |
| Vejdirektoratet traffic counts map | `https://www.vejdirektoratet.dk/viden-og-data/trafik-og-mobilitet/trafikkens-udvikling-i-tal/trafiktaellinger` |

## Status

✅ **Fully populated** as of 2026-04-25. Tax tracker entry re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax (with 2024 boligskat reform), rental, work, risks (incl. stormflodsordning conditions + 20 Oct 2023 reference event), mains all populated. Primary government sources back tax, rental, work, risks and ownership data; price benchmarks pair Finans Danmark Boligmarkedsstatistikken (industry association — secondary) with DST EJEN77 (primary); traffic verdict bands and the mains, report-fee and renovation cost ranges are curated estimates (wisdom, not data).
**Confidence**: HIGH for price benchmarks (Finans Danmark BM010/BM011 + DST EJEN77, 2025 to 2026 Q2; kommune / landsdel / postnr averages, never parcel values), ownership shares (DST BOL101), short-let caps and rental bundfradrag (plst.dk, skat.dk), and the company-capital, tax-bracket and salary data in `--work` (Erhvervsstyrelsen, skat.dk, DST LONS30). HIGH for the boligskat rates, progressionsgrænse, grundskyld promille and tinglysningsafgift (skm.dk + vurderingsportalen.dk, 2026), but MEDIUM for `--tax` as a whole ('lowest in W. Europe' and 'notar not mandatory' unsourced, mæglersalær est.). HIGH for tinglysning (unified digital register since 8 Sep 2009, Tinglysningsretten); HIGH for andelsbolig structure, with the § 5 maximum-price mechanics from secondary transcriptions. MEDIUM for `--risks` (storm-surge, naturskadeafgift, radon, earthquake, PCB, energimærke and Klimaatlas figures re-checked; river-basin flood, wildfire, saltwater-intrusion and build-era rows unsourced; Lønstrup Klint erosion rate not refreshed), `--traffic` (verdict bands curated) and the investment-property tax line in `--rental` (not re-verified). MEDIUM for Boligreguleringsloven post-1 July 2022 transitional rules (merger into Lov om leje verified, transitional rules not re-checked). LOW for `--mains` cost ranges (est., no published tariff).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | Ownership shares recomputed from DST BOL101 (stock at 1 Jan 2026); cadastre agency names corrected; ERM II central rate confirmed |
| `--price` | 2026-10-23 | 2026-10-23 refresh wave | Benchmark table rebuilt from Finans Danmark BM010/BM011 + DST EJEN77 (2025 to 2026 Q2); OIS, Finans Danmark, energimærke scale and andelskrone corrected; tinglysning viewer/fee line and Vurderingsportalen not re-checked |
| `--rental` | 2026-10-23 | 2026-10-23 refresh wave | Short-let caps (30 / 70 / up to 100 days), room-let VAT, sommerhus letting and bundfradrag re-checked on plst.dk + skat.dk; investment-property tax treatment not verified |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | ApS / A/S capital, moms, AM-bidrag and 2026 brackets re-checked (Erhvervsstyrelsen, skat.dk); salaries from DST LONS30 2025; marginal rates est. |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | Portal self-descriptions and agency sites checked |
| Reddit / forum sources | 2026-10-23 | 2026-10-23 refresh wave | Subreddits and expat sites live; MyHusum.dk deprecated |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Naturskaderådet replaces Stormrådet; Kystdirektoratet and Social- og Boligstyrelsen added |

## Extension TODOs

- [ ] Per-kommune grundskyld promille (2024-2028 schedule per Vurderingsportalen)
- [ ] Andelsbolig financial health red-flag detection (foreningens gæld %, repair backlog)
- [ ] Sommerhus zone parcel-level lookup
- [ ] Coastal erosion projection per kommune
- [ ] Bornholm radon zone overlay
- [ ] Stormflod exposure overlay (Kystdirektoratet dige map + højvandsstatistik, BBR naturskade registrations)
- [ ] Boligreguleringsloven post-1 July 2022 transition rules
- [ ] PCB legacy building inventory
- [ ] Kommune VVS / kloak connection database
- [ ] Pendlerfradrag + boligjobordning eligibility

## Update history

- **2026-04-25** — Initial population (researched 2026-04)
- **2026-10-21** — Tax tracker entry re-checked (December regwatch wave, run early; see shared/regulatory-watch.md)
- **2026-10-23** — Refresh wave across market, tax-legal and risk-infra sections (counts are changed / confirmed / unverifiable):
  - **Re-verified** (see Per-section verification): Country profile 4 / 6 / 1 — ownership shares recomputed from DST BOL101 (ejerbolig ~63% → ~47%, private lejeboliger ~10% → ~24%, andelsbolig in København ~35% → ~28%), cadastre agency names corrected; `--price` 26 / 4 / 2 — benchmark table rebuilt from Finans Danmark BM010/BM011 + DST EJEN77, OIS name, Realkreditrådet → Finans Danmark, energimærke scale and andelskrone definition corrected; `--rental` 8 / 2 / 2 — short-let caps are national (30 days, 70 via a reporting platform, a kommune may raise 70 to 100), no DKK 70,000 CVR threshold, no sommerhus 70-night cap, bundfradrag DKK 31,200 → 35,100 (2026) / 33,500 (2025), Boligreguleringsloven merged into Lov om leje; `--work` 5 / 5 / 3 — ApS minimum capital DKK 40,000 → 20,000, 2026 bracket structure, DST LONS30 salaries, OfferOgEfterspørgsel.dk deprecated; Common listing platforms 3 / 3 / 0; Reddit / forum sources 2 / 5 / 0 (MyHusum.dk deprecated); Verification authorities 2 / 6 / 0 (Stormrådet → Naturskaderådet, Kystdirektoratet added)
  - **Refreshed, not fully re-verified**: `--tax` 13 / 9 / 3 — grundskyld had carried the ejendomsværdiskat rates (now a kommunal promille, 3.1–17.7‰), progressionsgrænse DKK 9,007,000 for 2026–2027, pantebrev tinglysningsafgift 1.45% → 1.25% + DKK 1,825, investment gains capped at 42% as kapitalindkomst (not 52.07%), skatterabat and stigningsbegrænsning rules corrected; Cost benchmarks 3 / 1 / 4 — report fees and mæglersalær relabelled est., buyer total computed (~2.0%); Active fiscal incentives 5 / 0 / 1 — Bygningspuljen closed, grant schemes refreshed, rentefradrag ~25.6% → ~33% / ~25% plus the proposed L 73 cap (audit DK-FFL27-01); Caveats 8 / 2 / 2 — short-let, sommerhus, stigningsbegrænsning, parcelhusreglen, MitID and Erhvervelsesloven items corrected, andelsbolig share recomputed (28.6% København kommune), false A–D storm-surge rating replaced by the stormflodsordning conditions; `--traffic` 3 / 1 / 4 — Vejman, Mastra and ÅDT corrected, verdict bands remain curated heuristics; `--risks` 24 / 11 / 9 — false A–D property rating, 'Ole 1825' and the 3.5 ML maximum removed, storm-surge events, erosion, earthquake, radon, naturskadeafgift, PCB and Klimaatlas v2025a figures refreshed; `--mains` 2 / 4 / 5 — VandCenter Syd 2026 tariff added, cost ranges remain est.; Source URL templates 3 / 8 / 3 — Naturskaderådet and Kystdirektoratet redirect targets, OIS label corrected, Klimaatlas and Vejdirektoratet count-map rows added, Boliga, Boligsiden and Vurderingsportalen bot-walled
  - Status footer date unchanged: `--tax`, `--risks` and `--mains` are not fully re-verified
