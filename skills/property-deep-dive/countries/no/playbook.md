# Norway 🇳🇴 — Property Due-Diligence Playbook

ISO2: `no`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`0150` Oslo central, `5003` Bergen, `7012` Trondheim, `4012` Stavanger)
- **Admin levels**: **15 fylker** (counties — NO reverted from 11 to 15 on 1 Jan 2024, dissolving Viken / Vestfold og Telemark / Troms og Finnmark back to Akershus, Buskerud, Østfold, Vestfold, Telemark, Troms, Finnmark) + 357 kommuner (municipalities) (2026-10-23 verified, source: SSB Klass standard for kommuneinndeling / fylkesinndeling valid on that date; history per Kartverket / regjeringen.no — 2022 Storting vote undid the 2020 consolidation)
- **Currency**: **NOK** (Norwegian krone); 1 EUR = 10.49 NOK on 22 Oct 2026; 12-month range 10.49–11.99 NOK (high 17 Dec 2025, low 22 Oct 2026) (2026 data, source Norges Bank daily exchange rates — `https://www.norges-bank.no/en/topics/Statistics/exchange_rates/`) — volatile
- **Languages**: Norwegian, with two official written standards — Bokmål and Nynorsk; Nynorsk is hovudmål for 11.1 % of grunnskole pupils (2025 data, source SSB — a share of pupils, not of speakers); Sámi minority (north)
- **Cadastre**: **Kartverket** (Norwegian Mapping Authority) + **Matrikkelen** (national property register)
- **Identifier**: gnr/bnr (gårdsnummer/bruksnummer) + festenr (lease number) per kommune; format `<kommune>/<gnr>/<bnr>/<fnr>`
- Distinct ownership types:
  - **Selveier** (freehold) — 59.2 % of households own as selveier (Oslo 35.3 %); 27.3 % rent (2025 data, source SSB table 14891 — households, not dwelling stock)
  - **Borettslag** (housing cooperative — major form) — 13.5 % of households are andels- or aksjeeier (Oslo 30.9 %) (2025 data, source SSB table 14891)
  - **Aksjeleilighet** (old-style share apartment, rare)
  - **Eierseksjon** (condominium / commonhold — most modern apartments)
- **Norway is NOT in EU** — but EEA member; some buyer restrictions apply

## Section: `--price`

### Primary sources

- **Kartverket Matrikkelen** (cadastre): `https://eiendomsregisteret.kartverket.no/`
- **Eiendomsregisteret** (Kartverket consumer portal; the old Se eiendom address `https://seeiendom.kartverket.no/` now redirects here): `https://eiendomsregisteret.kartverket.no/`
  - FREE lookup of any property in Norway by address, road name or gnr/bnr; login via ID-porten (MinID, BankID) required (2026 data, source kartverket.no/eiendom/eiendomsinformasjon)
- **Eiendom Norge** (industry body) — monthly market reports: `https://eiendomnorge.no/`
- **SSB (Statistics Norway) Boligprisindeks**: `https://www.ssb.no/`
- **Norges Bank** financial stability reports
- **Realkredittforeningen** mortgage data — ❌ DEPRECATED — dead on 2026-10-23 (realkredittforeningen.no does not resolve; no Norwegian body of this name could be confirmed); verify with SSB
- **SSB table 10748** — renter på nye boliglån (new mortgage rates), monthly: `https://www.ssb.no/statbank/table/10748`

### Listing platforms

- **Finn.no** — DOMINANT (market-share figure: data not publicly available; per SSB, homes advertised on FINN.no, which form the sample for its house-price statistics, make up ≈ 70 % of housing transactions in fritt salg, and FINN.no has been SSB's data source for both selveier and borettslag since 2009; source SSB prisindeks for brukte boliger, page updated 12 Oct 2026): `https://www.finn.no/realestate` (redirects to `/realestate/homes/search.html`)
  - URL: `https://www.finn.no/realestate/homes/search.html?location=<id>`
  - Includes both selveier + borettslag in one feed
- **DNB Eiendom**, **EiendomsMegler 1**, **Privatmegleren**, **Krogsveen**, **Aktiv** — agency networks
- **Hjem.no** (alternative)

### 2025 price benchmarks (SSB, kr/m² BRA-i)

Average kr/m² BRA-i for resales, selveier + borettslag combined (borettslag price includes innskudd + andel fellesgjeld); 2025 full year, 2026 Q3 in brackets (2026 data, source SSB tables 14545 / 14310 — `https://www.ssb.no/statbank/table/14310`). Kommune averages, not parcel values; quarterly enebolig figures rest on small samples (e.g. 83 sales in Tromsø, 99 in Bærum in 2026 Q3).

| Region | NOK/m² blokkleilighet — 2025 (2026 Q3) | NOK/m² enebolig — 2025 (2026 Q3) |
|---|---:|---:|
| **Oslo** | 101,613 (101,568) | 68,862 (71,030) |
| **Bærum / Asker** (Oslo suburbs) | 85,279 / 70,359 (85,026 / 69,542) | 62,065 / 45,426 (64,253 / 47,301) |
| **Bergen** | 65,713 (73,406) | 40,954 (45,982) |
| **Trondheim** | 59,858 (61,301) | 38,078 (39,614) |
| **Stavanger / Sandnes** | 61,832 / 53,744 (67,206 / 59,451) | 41,684 / 34,129 (44,834 / 37,998) |
| **Tromsø** | 67,506 (76,243) | 39,220 (43,591) |
| **Drammen / Sandefjord** | 55,062 / 45,209 (54,686 / 43,854) | 32,352 / 30,917 (33,704 / 31,674) |
| **Norway (all kommuner)** | 70,168 (71,644) | 29,590 (29,924) |
| **Rural / hytte** | not covered by the SSB kr/m² series | est. from NOK 1,500,000 (mountain cabin) to NOK 20,000,000+ (coastal/luxury) — unsourced, verify per listing |

- **12-month change**, SSB price index for resales, Q3 2025 → Q3 2026: Norway +3.3 %, Oslo med Bærum +0.1 %, Bergen +11.2 %, Stavanger +5.7 %, Trondheim +2.8 %, Nord-Norge +6.6 % (computed from SSB table 07221 index values, e.g. Bergen 147.9 → 164.4; 2026 data, source SSB).
- **Villa total price**: compute = enebolig kr/m² × the listing's BRA-i (e.g. 150 m² in Trondheim × NOK 38,078 ≈ NOK 5.7M); these SSB tables publish no average total price per villa.

### Compute

1. Listing NOK/m² = price (for borettslag: innskudd + andel fellesgjeld, as SSB computes it) / **BRA-i (internt bruksareal)**
2. **Trap**: **BRA-i** (NS 3940:2023) = usable area inside the unit's enclosing walls, including internal storage rooms and closets; the older **P-rom (primærrom)** = primary rooms only (excl. storage); **S-rom (sekundærrom)** = secondary. SSB computed kr/m² on P-rom for 2008–2024 and on BRA-i from Q1 2025, so kr/m² before and after are not directly comparable (2026 data, source SSB prisindeks for brukte boliger)
3. **Borettslag math**: the asking price (prisantydning) does not include the unit's share of **fellesgjeld** (cooperative shared debt): the broker's salgsoppgave must list prisantydning, andel fellesgjeld and all fees and costs separately, plus their sum (totalpris) (eiendomsmeglingsloven § 6-7 (2) nr. 13; source: Lovdata, 2026); SSB records kjøpesum and fellesgjeld separately (table 11504). The TRUE total cost = innskudd + fellesgjeld + felleskostnader future stream
4. **Eierseksjon math**: own apartment + share in common parts (sameie); separate sameieavgift

### Borettslag specific (CRITICAL)

For borettslag, always compute:
- **Innskudd** (your share value, like down payment) — what listing typically shows; SSB average kjøpesum per borettslag sale in fritt salg NOK 3,571,000 nationally / NOK 5,031,000 in Oslo (2026 Q2 data, source SSB table 11504)
- **Fellesgjeld** (cooperative shared building debt) — SSB average NOK 402,000 per sale nationally / NOK 373,000 in Oslo (2026 Q2; NOK 420,000–459,000 per quarter nationally in 2025) (2026 data, source SSB table 11504); est. NOK 500,000–3,000,000 per apartment for newer borettslag (unsourced — check the salgsoppgave)
- **Felleskostnader** (monthly common costs) — typically NOK 3,000–10,000+/mo
- **Total acquisition** = Innskudd + Fellesgjeld (SSB national average 2026 Q2: NOK 3,571,000 + 402,000 = NOK 3,973,000 'totalpris inkludert fellesgjeld', source SSB table 11504)
- **Forretningsfører** + årsmøte protokoller for due-diligence

---

## Section: `--traffic`

### Primary sources

- **Statens vegvesen** (Public Roads Administration): `https://www.vegvesen.no/`
- **NVDB (Nasjonal vegdatabank)**: `https://nvdb.atlas.vegvesen.no/`
  - ÅDT per road section: Vegkart layer "ÅDT på strekning" — `https://vegkart.atlas.vegvesen.no/` (source Statens vegvesen, checked 2026-10-23)
- **Trafikkdataportalen**: `https://trafikkdata.atlas.vegvesen.no/` — traffic data for the state + county (fylkesvei) road network incl. ferries (source Statens vegvesen, checked 2026-10-23); for kommunale veger ask the kommune

### Key term

**ÅDT (årsdøgntrafikk)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (boligvei, lokalvei)
- 🟡 1,000–8,000 v/d (fylkesvei, urban arterial)
- 🟠 8,000–30,000 v/d (riksvei, urban core)
- 🔴 > 30,000 v/d (E6/E18/E39, central Oslo Ring)

---

## Section: `--tax`

### Annual property tax — Eiendomsskatt (OPTIONAL per kommune)

**329 of 357 kommuner** levy eiendomsskatt in 2026 (28 do not; 322 → 329 over 2023–2026), but only **249** levy it on boliger — the rest tax only næringseiendom and/or kraftanlegg, vindkraft and petroleum installations. Lørenskog, Sande (Møre og Romsdal) and Stavanger introduced it on boliger in 2026; Fitjar, Herøy (Nordland) and Leka dropped it. 123 kommuner value boliger with Skatteetaten's formuesgrunnlag (2026 data, source: SSB Eiendomsskatt, tables 14155 + 14674, updated 15 Jun 2026). Not nationwide.

- **Rates**: general range 1–7 ‰; max **4 ‰ (0.4 %)** for bustader + fritidsbustader (housing cap added to § 11 from tax year 2020, amended from tax year 2021); first year max 1 ‰, then max +1 ‰ per year (2026 data, source: Lovdata — eigedomsskattelova §§ 11, 13). SSB average rate for boliger + fritidsboliger: **3.3 ‰** (2026 data, source: SSB table 14155)
- **Bunnfradrag** (basic deduction): optional, set by kommunestyret per selvstendig bustaddel (eskl. § 11); only **79 kommuner** use one in 2026 — e.g. Oslo NOK 4,900,000, Bergen NOK 750,000, Trondheim NOK 700,000, Stavanger none (2026 data, source: SSB Kommuner med eiendomsskatt, table 14674)
- **Reduction**: the tax base for bustader + fritidsbustader is value × 0.7 (eskl. § 8 A-2 (1); same factor on Skatteetaten's formuesgrunnlag, § 8 C-1 (2)); a local reduksjonsfaktor replaces it only when higher, never on top (§ 8 A-2 (4)) (2026 data, source: Lovdata — eigedomsskattelova as amended to LOV-2025-06-20-60)
- **Effectively low**: SSB average eiendomsskatt per bolig NOK 3,867 (2025) and NOK 3,811 for a 120 m² enebolig (2024, last year published) (source: SSB table 14155) — national averages; the bill for one address depends on the kommune's rate, bunnfradrag and valuation
- **Bills**: in terminar set by each kommunestyre (eskl. § 25) — count varies by kommune

**Major kommuner with eiendomsskatt**:
- Oslo: yes (on all fixed property since 2017); 2026 rate **1.7 ‰** for boliger/fritidsboliger (down from 2.35 ‰ in 2025), bunnfradrag up to NOK 4,900,000, base 70 % of Skatteetaten's market value (2026 data, source: Oslo kommune — Om eiendomsskatt i Oslo)
- Bergen 2.6 ‰ (bunnfradrag NOK 750,000); Trondheim 2.65 ‰ (bunnfradrag NOK 700,000); Stavanger 1.0 ‰, on boliger from 2026, no bunnfradrag (2026 data, source: SSB table 14674)
- Many smaller kommuner: yes
- Bærum, Asker (Oslo wealthy suburbs): NO eiendomsskatt at all — also none in Drammen, Lier, Nordre Follo, Sandefjord, Tønsberg, Larvik, Færder, Sola (28 kommuner in total) (2026 data, source: SSB Kommuner uten eiendomsskatt)

### Transaction taxes — Dokumentavgift (MAJOR)

**2.5 % of the property's market value at tinglysing** — the sales value incl. buildings, not the price paid where they differ, e.g. gift or debt takeover (2026 check, source: Kartverket — Dokumentavgift ved overføring av fast eigedom, page dated 2023-09-27; rate set by Stortinget's dokumentavgift resolution, dokumentavgiftsloven § 1) — significant! Buyer (erverver of grunnbokshjemmel, § 6) pays.

**CRITICAL EXEMPTION**: **Borettslag NOT subject to dokumentavgift** (only selveier + eierseksjon).
- Saving = 2.5 % of value — e.g. NOK 125,000 on a NOK 5,000,000 purchase (computed: 5,000,000 × 2.5 %)
- **Borettslag transfer**: only **NOK 545** flat fee per overføring of andel, and no dokumentavgift (2026 data, source: Kartverket — Tinglysingsgebyr "Gebyr 2026" + Borettslag page)

**Tinglysningsgebyr** (registration fee): **NOK 545** per document — skjøte and pantedokument each charged separately (2026 data, source: Kartverket — Tinglysingsgebyr, "Gebyr 2026", updated 2026-01-05)

### Other transaction costs

- **Megler** (broker): est. ~1.5–3 % of price, paid by seller (or split in negotiation) — compare quotes; the written oppdragsavtale must state the fee and a total cost estimate (eiendomsmeglingsloven § 6-4)
- **Legal/conveyancing**: most use megler + standard contracts; full lawyer rare
- **Boligkjøperforsikring** (buyer insurance): voluntary; ~NOK 5,000–15,000 — **highly recommended**

### Total transaction cost (buyer side)

- **Selveier / eierseksjon**: ≈ 2.6–2.8 % on a NOK 5,000,000 purchase (computed: 2.5 % dokumentavgift = NOK 125,000 + 2 × NOK 545 tinglysing for skjøte + pantedokument + est. NOK 5,000–15,000 boligkjøperforsikring)
- **Borettslag**: ≈ 0.2–0.5 % on a NOK 3,000,000 andel (computed: 2 × NOK 545 + est. NOK 5,000–15,000 boligkjøperforsikring; no dokumentavgift; fees charged by the borettslag's forretningsfører not included)

### Capital gains

- **22 %** as alminnelig inntekt (18.5 % in the Troms og Finnmark tiltakssone) (2026 data, source: Skatteetaten — satser, alminnelig inntekt)
- **Primary residence exemption**: owned **more than 1 year** when the sale is made or agreed + whole property used as own home **at least 1 of the last 2 years** → fully exempt; covers selveier, andel in borettslag and aksjeleilighet (2026 data, source: Lovdata — skatteloven § 9-3 (2))
- **Fritidsbolig exemption**: owned more than 5 years + used as own fritidsbolig at least 5 of the last 8 years (skatteloven § 9-3 (4))
- Investment property: full 22 % on gain

### VAT (mva)

- 25 % standard
- 15 % reduced (food)
- 12 % reduced (passenger transport, accommodation, public broadcasting, admission to cinema, sports events, amusement parks, experience centres); 15 % also on water + sewerage services (2026 rates, source: Skatteetaten — satser, merverdiavgift)
- Residential property sales: **VAT-exempt** (excl. specific commercial)

### Future risk

- Eiendomsskatt residential cap at **4 ‰ (0.4 %)** (eskl. § 11, last amended from tax year 2021); the 2027 budget proposal (7 Oct 2026) adds no new eiendomsskatt (source: Estate Nyheter, 7 Oct 2026 — secondary)
- **Formueskatt (wealth tax) — 2026**: no tax below **NOK 1,900,000 single / NOK 3,800,000 couples** taxed jointly; above that 0.35 % kommune + 0.65 % state = 1.0 %; state rate 0.75 % above NOK 21,500,000 → 1.1 % (2026 data, source: Skatteetaten — satser, formuesskatt). Boligverdsetting: primærbolig 25 % of market value up to **NOK 14,000,000** and 70 % above (raised from NOK 10M, Prop. 95 LS (2025–2026)); sekundærbolig 100 %; fritidsbolig separate lower regime (2026 data, source: Skatteetaten — satser, formuesverdi bolig). Updated valuation model from the 2026 income year uses sales data per grunnkrets instead of per kommune (source: Skatteetaten — formuesverdi). The 2025 return still uses NOK 1,760,000 / 3,520,000, 0.525 % kommune + 0.475 % state (0.575 % above NOK 20,700,000) and the NOK 10M primærbolig threshold (source: Skatteetaten — satser, year 2025). **2027 (proposal only)**: Prop. 1 LS (2026–2027), presented 7 Oct 2026, raises the bunnfradrag slightly and keeps housing thresholds, incl. the NOK 14M primærbolig threshold, nominally unchanged (source: Huseierne + Estate Nyheter, 7 Oct 2026 — secondary); not adopted — exact 2027 figures: verify at regjeringen.no Prop. 1 LS (2026–2027) or Stortinget's skattevedtak for 2027 (December 2026)
- **Utflyttingsskatt (2024 exit-tax reform)** — latent gains on shares, aksjesparekonto and similar holdings when leaving Norway, not real property (§ 10-70 (2)): applies to exits from 20 Mar 2024 (further changes from 7 Oct 2024); 12-year limit on deferred payment regardless of realisation; **NOK 3M basic allowance** — only net gain above NOK 3,000,000 is taxed; pay now, or defer up to 12 years incl. a 1/12-per-year instalment option (2026 data, source: Lovdata — skatteloven § 10-70 (2), (4), (7), as amended by lov 20 des 2024 nr. 86)
- **Borettslag exemption from dokumentavgift** — periodically debated but stable

---

## Section: `--rental`

### Long-term residential

- **Husleieloven** (Tenancy Act): tenant-protective
- **Tidsbestemt** (fixed-term) lease for bolig: minimum **3 years**; 1 year allowed for a loft or basement unit in an enebolig / tomannsbolig where the landlord lives in the same house; no minimum where the landlord or a household member will use the home, or the landlord has another objective reason, stated in writing at signing; a lease breaching the rule counts as tidsubestemt (husleieloven § 9-3; source: Lovdata, 2026)
- **Husleieloven** rent changes: KPI indexation at most once a year with at least 1 month's written notice (§ 4-2); adjustment to gjengs leie (market rent) once the lease has run 2 years 6 months with no other change (§ 4-3) (source: Lovdata, 2026)
- **Boligbyggelagene** (BBL) cooperatives manage many borettslag

### Short-let (Airbnb / Booking)

**Skatteetaten rules** (significant):
- **Sekundærbolig** (secondary housing): **31-day rental cap** for short-let in some kommuner without commercial license (unverified, no source cited — check with the kommune; the national statutory caps are the borettslag and eierseksjon rules below)
- **Oslo**: ongoing debate about 30/60/90-day caps
- **Borettslag**: an andelseier who lives in the home may let parts of it, and may let the whole home for up to **30 days a year** (borettslagslova § 5-4); any other letting needs the board's consent (§ 5-3) (in force since 1 Jan 2020; source: Lovdata)
- **Eierseksjon**: korttidsutleie (lets of up to 30 consecutive days) of a whole boligseksjon is capped at **90 days a year**; the vedtekter can move the cap to between 60 and 120 days by a two-thirds majority at the årsmøte; the cap does not apply in sameier where all units are fritidsboliger (eierseksjonsloven § 24; in force since 1 Jan 2020; source: Lovdata)

### Tax on short-let

- **Skatteetaten**: a taxable rental surplus is normally taxed at **22 %**; if the letting counts as næringsvirksomhet, the surplus is taxed at up to 50.6 % (2026 data, source: Skatteetaten)
- **Short-let (< 30 days) of your own home, and a fritidseiendom let partly or for part of the year**: 85 % of rental income above **NOK 15,000**/yr is taxable income (skatteloven § 7-2 (2), text in force from income year 2025, last amended by lov 20 Dec 2024 nr. 86; source: Lovdata); costs of short-letting your own home or a fritidseiendom you use yourself are not deductible (source: Skatteetaten)
- **Long-term letting (≥ 30 days continuous) of your own home**: tax-free if you use at least half of it yourself (by rental value), or if the whole / greater part is let for at most NOK 20,000 in the income year (skatteloven § 7-2 (1); source: Lovdata)
- § 7-2 does not cover flermannsboliger, utleiehytter, or own-home letting that counts as virksomhet (skatteloven § 7-2 (3); source: Lovdata)
- **Sekundærbolig**: full taxation
- **Hyttekultur** (cabin culture): ulikt regelverk per kommune
- **EU Regulation 2024/1028** (short-term rental data): applies in the EU since 20 May 2026 but is NOT yet part of the EEA Agreement — EEA-Lex lists it as "under scrutiny for incorporation into the EEA Agreement by Iceland, Liechtenstein and Norway", with no EEA Joint Committee decision (2026 data, source EFTA EEA-Lex 32024R1028); it does not bind Norway until incorporated and implemented in Norwegian law

---

## Section: `--work=<profession>`

### Job platforms

- **Finn Jobb** — biggest: `https://www.finn.no/job`
- **NAV (Arbeids- og velferdsetaten)**: `https://www.nav.no/` — its job board **arbeidsplassen.no** ("Alle ledige jobber, samlet på én plass"): `https://arbeidsplassen.nav.no/`
- **LinkedIn NO**, **Indeed.no**, **Jobb.no** (`https://jobb.no/`)
- **Karriereguiden** — ❌ DEPRECATED — dead on 2026-10-23 (karriereguiden.no refuses connections); verify with arbeidsplassen.nav.no
- **Statens lønnsstatistikk** for civil service salaries

### Self-employment

- **Enkeltpersonforetak (ENK)**: sole trader; no min capital; the owner has full personal liability for the business's debts and obligations (source: Brønnøysundregistrene, 2026)
- **Aksjeselskap (AS)**: limited company, **min NOK 30,000** share capital (source: Brønnøysundregistrene / aksjeloven; 2026)
- **NUF (Norwegian-registered foreign company)**: niche
- **Brønnøysundregistrene** (registration agency)
- **Folketrygd** + **Næringsdrivende** social contributions

### Salary benchmarks (2025)

- Median monthly gross earnings, full-time employees, by workplace kommune (November 2025; 2025 data, source SSB table 12852 — `https://www.ssb.no/statbank/table/12852`):
  - Oslo: NOK 64,780 (Bærum NOK 68,480)
  - Stavanger NOK 62,510 · Bergen NOK 60,000 · Trondheim NOK 59,110
  - Tromsø NOK 56,840 · Drammen NOK 55,980 · Sandefjord NOK 55,160
  - Norway: NOK 57,970
- **No general statutory minimum wage**: minimum wages apply only where a tariff agreement has been made generally applicable (allmenngjort) — Arbeidstilsynet lists nine sectors: bilbransjen (from 15 Jun 2026), bygg, elektro, godstransport på vei, jordbruk og gartnerier, overnatting / servering / catering, persontransport med turbil, renhold, skips- og verftsindustrien; the fiskeindustri regulation was repealed on 3 Aug 2026 and a new one is out for Tariffnemnda consultation (2026 data, source Arbeidstilsynet)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **NVE (Norges vassdrags- og energidirektorat)** | `https://www.nve.no/` | Floods, landslides, dams |
| **Skredhendelser / NSDB** (ex-Skrednett; skrednett.no 301-redirects here, updated 2026-10-23) | `https://www.nve.no/naturfare/laer-om-naturfare/om-skred/skredhendelser/` | National landslide-event database; per-event detail on `https://www.skredregistrering.no/` |
| **NVE Temakart** | `https://temakart.nve.no/` | NVE's "anbefalte inngang til fagdata": kvikkleire (`/tema/kvikkleire`), skred i bratt terreng (`/tema/skredbrattterreng_tilpasset`), flomaktsomhet (`/tema/flomaktsomhet`) |
| **NVE Atlas** | `https://atlas.nve.no/` | Map viewer "først og fremst brukt av forvaltningen" (NVE) |
| **NGI (Norwegian Geotechnical Institute)** | `https://www.ngi.no/` | Quick clay + slope research |
| **Aktsomhetskart for flom** | `https://temakart.nve.no/tema/flomaktsomhet` | Screening map of areas that may be flood-exposed; faresonekart flom only for mapped river stretches (`https://temakart.nve.no/link/?link=flomsone`) |
| **NGU (Norges geologiske undersøkelse)** | `https://www.ngu.no/` | Geology, geohazards; radon aktsomhetskart with DSA (`https://www.ngu.no/geologi-og-risiko/radon`, updated Oct 2026) |
| **DSA (Direktoratet for strålevern og atomsikkerhet)** | `https://www.dsa.no/radon` | Radon — recommends that every homeowner measure; only 20 % report having done so (source DSA, page updated 2026-10-05) |
| **MET (Meteorologisk institutt)** | `https://www.met.no/` | Climate, weather |
| **NORSAR** (seismic monitoring) | `https://www.norsar.no/` + `https://www.jordskjelv.no/` | Earthquakes (national seismic network; historical catalogue) |

### Specific risks

- **Skred (landslides + avalanches) — MAJOR risk**:
  - **Snøskred** (snow avalanche)
  - **Jordskred** (mud / earth slide)
  - **Steinskred** (rockfall)
  - **Kvikkleireskred** (quick clay slide) — devastating; quick clay can occur anywhere below the marine limit (0–220 m a.s.l.); triggered by stream/river erosion or by excavation at the slope toe / fill on the slope top (source NVE, checked 2026-10-23)
  - Especially: **fjordmark + western Norway + Trøndelag + arctic regions**
  - **Gjerdrum quick-clay slide, 30 Dec 2020** (11 dead, source NVE): kvikkleire reminder
- **Flom (flooding)**:
  - River plains: Glomma, Drammenselva, Otra
  - Fjord communities
  - Snowmelt (spring) + rain floods — spring floods have come earlier in recent decades; rain floods have increased, especially in Sør-Norge + Vestlandet (2025 data, source Norsk klimaservicesenter — Klima i Norge 2025)
- **Kystflom + havnivåstigning** (coastal flood + sea-level rise)
- **Radon — DSA recommends that every homeowner measure** (only 20 % report having measured; source DSA, page updated 2026-10-05):
  - "Norge er spesielt utsatt for radon" — geology + cold climate; DSA estimates radon in homes causes ≈400 lung-cancer cases per year
  - High-uranium rocks: alunskifer, granitt, granittiske gneiser — NGU + DSA aktsomhetskart (updated Oct 2026) at `https://www.ngu.no/geologi-og-risiko/radon` is area-level screening, not a measurement of the house
  - DSA levels: tiltaksgrense 100 Bq/m³, grenseverdi 200 Bq/m³ — recommendations for owner-occupied homes, binding for utleieboliger, schools + kindergartens (strålevernforskriften; utleieboliger § 6); measure mid-Oct → mid-Apr for ≥ 2 months (source DSA, checked 2026-10-23)
- **Earthquake**: low probability — "Norge er ikke veldig utsatt for jordskjelv", yet has the most earthquakes in Northern Europe (source NORSAR jordskjelv.no, checked 2026-10-23)
  - Most active zones: Vestlandet + the North Sea; the Nordland coast is prone to earthquake swarms
  - Historical M5+ include: 1819 Lurøy (Nordland) M5.8 per NORSAR's catalogue page (5.9 on its overview page) — largest in historical time; 1931 Doggerbanken (North Sea) 5.5; 1904 Oslofjord 5.4 (damage in Oslo); 1988 offshore Nordvestlandet 5.3; 1892 Sunnfjord 5.2 (source NORSAR jordskjelv.no)
- **Climate change**: rising precipitation (see sourced MET + NVE projections below); permafrost retreat in north; sea-level rise

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, no thermal envelope |
| **1960s–1980s panelhus + concrete** | Asbestos very common |
| **1990s–2000s** | Better insulation, modern wiring |
| **Post-2010 TEK10** | Low-energy standards |
| **Post-2017 TEK17** (in force 1 Jul 2017, FOR-2017-06-19-840) | Strict energy + accessibility |
| **Wood construction** | Common — fire risk + moisture; brannsmitte |
| **Asbestos** | Used c. 1920–1985, heaviest post-WWII to 1980; total ban 1985 — survey any building erected before 1985 (source Arbeidstilsynet, checked 2026-10-23) |

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energimerking** (energiattest) | Mandatory at sale + letting; owner duty since 1 Jul 2010; shown to buyer before contract, else buyer may order one at seller's cost within 1 year (energimerkeforskriften §§ 5, 23) | Up to 10 years (§ 4) |
| **Tilstandsrapport** (condition report) | **Not legally mandatory** (DiBK) — voluntary, but since 1 Jan 2022 the buyer is deemed to know what an approved report clearly shows (avhendingslova § 3-10), so a seller without one is more easily liable for defects (DiBK) | Max 1 year old when the buyer commits (forskrift § 1-6) |
| **Egenerklæring** (seller's declaration) | All sales | At sale |
| **Egenmelding skadedyr** (pest declaration) | No statutory basis found (checked 2026-10-23) — verify with megler | At sale |
| **Eierskifteforsikring** (seller's insurance) | Recommended — protects seller from buyer claims | Per case |
| **Boligsalgsrapport** (older format) | Replaced by tilstandsrapport for 2022+ | n/a for new |

### Tilstandsrapport (CRITICAL post-2022)

The tilstandsrapport is **not legally mandatory** — "Selgeren av en bolig har ikke plikt til å innhente en tilstandsrapport" (source DiBK, page updated 2026-02-25) — but since 1 Jan 2022 the buyer is deemed to know whatever clearly appears in an approved report (avhendingslova § 3-10 (1); Forskrift til avhendingslova (tryggere bolighandel), FOR-2021-06-08-1850 § 1-5, covering consumer sales of helårs- and fritidsbolig), so a seller who skips it is more easily liable for defects (DiBK):
- Prepared by an independent **bygningssakkyndig** (forskrift § 1-3)
- Cost: est. NOK 15,000–35,000 (unsourced range; `shared/surveyor.md` carries NOK 8,000–20,000 from a 2025 aggregator) — get quotes; commissioned by the seller
- Must not be older than 1 year when the buyer commits (forskrift § 1-6)
- Visual + technical inspection; stricter checks of våtrom, rom under terreng + krypkjeller since 2022 (source DiBK)
- Specifies **TG (tilstandsgrad) 0-3** for each building component (forskrift § 2-23)
  - **TG2** = vesentlige avvik (needs maintenance or tiltak in the near future); **TG3** = store eller alvorlige avvik (repair immediately or shortly) and carries a repair-cost estimate (forskrift § 2-22) — a defect clearly described in an approved report cannot later be claimed as a mangel, so price it in before bidding
- **2022 reform** (lov 7 juni 2019 nr. 20, in force 1 Jan 2022): «som han er» clauses have no effect in consumer sales (avhendingslova § 3-9 (2)); the buyer bears defect losses up to NOK 10,000 (§ 3-1 (4))

### Climate change projections (MET + NVE)

Source for every bullet: Norsk klimaservicesenter, *Klima i Norge 2025* summaries (2025 data; summaries updated 2025-10-27) — national/regional projections, not parcel-level.

- Temperature: +1.4 °C observed 1901–2024; a further ~3.4 °C toward 2100 if emissions keep rising — larger in the north and east, larger in winter
- Precipitation: +21 % observed 1901–2024; a further ~11 % toward 2100 if emissions keep rising, largest in autumn; the daily amount normally exceeded once a year +10–30 %
- Sea level: relative rise ≈36 cm national average by 2100 (SSP3-7.0); 1–1.5 m in a low-probability, high-impact case (SSP5-8.5 + rapid Antarctic ice loss). Land uplift means 1960–2022 relative sea level fell around Oslofjorden and parts of Trøndelag/Nordland but rose on parts of Vest- and Sørlandet; the whole coast will likely see relative rise by 2100
- Floods: if emissions keep rising, middle and 200-year floods grow in every region except Finnmark; the 200-year flood rises by 30 %+ (water volume) in Sørøst-Norge, Vestlandet and Nordland
- Skred: more jord- og flomskred (cloudbursts); fewer snow avalanches in the lowlands but more natural releases at altitude; more rockfall where permafrost thaws
- Permafrost (≈4 % of mainland area, mostly mountains): the top layer in southern Norway's high mountains fully thawed by 2050 (medium-emission scenario)
- Glaciers: area −70 % in Breheimen + Jotunheimen and −40 % for Jostedalsbreen if emissions keep rising; Jostedalsbreen ice volume halved by 2100 under a medium-emission scenario

---

## Section: `--mains`

### Sources

- **Norsk Vann**: `https://www.norskvann.no/` — national water utility association
- Each kommune manages own vannverk + avløpssystem
- Major: **Oslo VAV** (Vann- og avløpsetaten), **Bergen Vann** (Bergen kommune), **Trondheim kommune**, **Stavanger kommune** (vann og avløp); **IVAR IKS** (Stavanger-based) delivers drinking water to 12 kommuner — check whether it supplies the target kommune (checked 2026-10-23)

### Verification

- Most populated areas: kommunal mains universal
- **Hytter (cabins) + rural**: own **brønn** (well) + **slamavskiller** (septic)
- **Private avløpsanlegg** (bolig, hytte, < 50 pe) fall under forurensningsforskriften kap. 12: the kommune is the pollution authority (§ 12-2); discharges established before 1 Jan 2007 stay lawful unless the kommune sets a deadline by forskrift or enkeltvedtak (§ 12-16) → ask the kommune about any pålegg om oppgradering

### Costs

| Scenario | Cost (NOK, est.) |
|---|---:|
| Tilkobling to mains | 50,000–150,000 |
| Mains-line extension via kommune | 100,000–500,000+ |
| Slamavskiller upgrade | 100,000–250,000 |
| Pre-renseanlegg / minirenseanlegg | 150,000–400,000 |
| Borebrønn (drilled well) | 80,000–150,000 |

Unsourced est. ranges — the one-off connection fee (engangsgebyr for tilknytning) is a kommunal VA-gebyr (forurensningsforskriften kap. 16, § 16-3): take the target kommune's gebyrregulativ plus contractor quotes.

---

## Cost benchmarks (NO 2026)

| Work | Cost (NOK) |
|---|---:|
| Energimerking | est. ~5,000–12,000 |
| Tilstandsrapport | est. ~15,000–35,000 |
| Megler (seller-paid typically) | est. ~1.5–3 % of price |
| **Dokumentavgift (selveier + eierseksjon; borettslag exempt)** | **2.5 % of market value** (Kartverket) |
| Tinglysningsgebyr | 545 per document (2026, Kartverket) |
| Boligkjøperforsikring (recommended) | est. ~5,000–15,000 |
| **Total transaction cost (selveier)** | **≈ 2.6–2.8 %** on NOK 5,000,000 (computed in `--tax`) |
| **Total transaction cost (borettslag)** | **≈ 0.2–0.5 %** on NOK 3,000,000 (computed in `--tax`) |
| Slamavskiller upgrade | est. ~100,000–250,000 |
| Roof (concrete tile, 150 m²) | est. ~250,000–500,000 |
| Asbestos abatement (small house) | est. ~100,000–400,000 |
| Energy retrofit (Class C → A) | est. ~600,000–1,500,000 |
| Radon mitigation | est. ~30,000–80,000 |
| Brann + lyd retrofit (apartment) | est. ~50,000–200,000 |

## Active fiscal incentives (2025-2026)

- **Enova** home grants (2026 data, source: enova.no — Støtte til tiltak i hjemmet): luft-til-vann + væske-til-vann varmepumpe, varmepumpebereder, etterisolering (tak/loft, vegg), energieffektive vinduer + ytterdører, oppgradering av bygningskroppen, balansert ventilasjon, solcelleanlegg, solfanger, energirådgivning; e.g. solcelleanlegg 25 % of approved invoiced costs capped at NOK 2,500 per kW, luft-til-vann varmepumpe 25 % capped at NOK 20,000; luft-til-luft varmepumpe is not on the list
- **Husbanken** (2026 data, source: husbanken.no — Lån fra Husbanken + Startlån): loans to build a miljøvennlig or livsløpsbolig, to upgrade an existing home with extensive measures that cut energy use, or to buy a new home in a Husbanken-approved project; **startlån** via the kommune for people with long-term difficulty getting a bank loan — no general first-purchase energy loan
- **Boligsparing for ungdom (BSU)**: savers under 34 (contributions through the year they turn 33); NOK 27,500/yr cap, NOK 300,000 total; tax deduction 10 % of the amount saved; no deduction for a year in which the saver owns (directly or via borettslag) a primary or secondary home on 31 Dec (2026 data, source: Skatteetaten — satser, BSU)
- **Rentefradrag**: mortgage interest is deductible in alminnelig inntekt, worth 22 % of the interest (18.5 % in the Troms og Finnmark tiltakssone) (computed from the 2026 Skatteetaten rate for alminnelig inntekt + Skatteetaten — Lån og renter) — significant subsidy
- **Skatteloven § 6-1**: retrofit and maintenance costs are deductible only against taxable income (e.g. taxable letting); § 6-1 (2) bars deductions for private housing costs, so owner-occupiers get no tax deduction for retrofit (2026 data, source: Lovdata — skatteloven § 6-1)

## Common listing platforms

- **Finn.no** — DOMINANT (~95 %), full extraction
- **DNB Eiendom, Krogsveen, Aktiv, EiendomsMegler 1, Privatmegleren** — agency networks
- **Hjem.no** — alternative
- **NE.no** — commercial premises to let and commercial property for sale (naeringseiendom.no redirects here): `https://ne.no/`

## Caveats unique to NO

- **Dokumentavgift 2.5 %** is the major buyer-side cost — **borettslag avoids it** (huge structural advantage); affects whether to choose freehold or coop
- **Borettslag vs selveier vs eierseksjon** distinction CRUCIAL; borettslag has fellesgjeld (shared debt of building) often €50k–€300k+ tied to apartment
- **Avhendingslova reform in force 1 Jan 2022** — in consumer sales «som han er» clauses have no effect (§ 3-9 (2)), and the buyer is deemed to know what clearly appears in a tilstandsrapport that meets the forskrift's requirements (§ 3-10 (1)); the act itself sets no duty to commission a tilstandsrapport (2026 data, source: Lovdata — avhendingslova) — one of the strongest buyer-protection regimes in Europe
- **Kvikkleire (quick clay)** zones — Trøndelag, Oslo region — Gjerdrum 2020 disaster; NVE Skrednett verification ESSENTIAL for any new build or extension
- **Boligkjøperforsikring** strongly recommended — covers buyer post-sale claims
- **Konsesjon** (konsesjonsloven) — not needed for bebygd eiendom ≤ 100 dekar with ≤ 35 dekar fulldyrka + overflatedyrka jord (§ 4 (1) nr. 4) or approved ubebygde enkelttomter ≤ 2 dekar built on within 5 years (§ 4 (1) nr. 1); larger farm / forest parcels need konsesjon, and a kommune can request a forskrift on nedsatt konsesjonsgrense (§ 7) so that buying a helårsbolig needs konsesjon unless the buyer commits to year-round residential use, with bosetting within 1 year. No nationality criterion in the act's text — the same rules apply to foreign and Norwegian buyers (2026 data, source: Lovdata — konsesjonsloven, last amended LOV-2025-06-20-107)
- **Bo- og driveplikt** in some rural areas (residence + cultivation duty for agricultural): relatives / odelsberettigede taking over bebygd eiendom with > 35 dekar fulldyrka + overflatedyrka jord or > 500 dekar produktiv skog without konsesjon must move in within 1 year and live there at least 5 years (konsesjonsloven § 5 (2)); other buyers can get boplikt as a konsesjon condition (§ 11) (2026 data, source: Lovdata — konsesjonsloven)
- **Allemannsretten** (right of public access) over uncultivated land — affects neighbouring privacy
- **Norway is NOT in EU but EEA** — konsesjonsloven has no nationality criterion, so non-EEA buyers face the same konsesjon rules as Norwegians (2026 data, source: Lovdata — konsesjonsloven); a residence permit (UDI) is a separate question; any national-security acquisition controls sit outside konsesjonsloven — verify with Nasjonal sikkerhetsmyndighet (NSM) for parcels near defence or critical infrastructure
- **Hyttekultur** — fjellhytte (mountain cabin) and sjøhytte (sea cabin) major secondary-home market
- **Strict building permits** in fjords + coast: no new tiltak (other than façade changes) within **100 m** of the shoreline at normal high water unless the kommuneplan or reguleringsplan sets another byggegrense; along vassdrag the kommune considers a limit of up to 100 m (2026 data, source: Lovdata — plan- og bygningsloven § 1-8)
- **Folketrygd** + **Skatteetaten** make tax for residents straightforward
- **Currency volatility**: NOK can swing 15-25 % vs EUR; affects foreign-buyer purchasing power
- **Petroleum wealth fund**: keeps NOK supported; long-term outlook depends on oil price
- **Allmenningsrett** (commons rights) for some forest properties

## Reddit / forum sources

- **r/Norge**, **r/Oslo**, **r/Bergen**, **r/Trondheim**
- **r/AskNorway**, **r/PersonalFinanceNorge**
- **r/Norwegen** (German-speaking expat angle)
- Expat: **The Local Norway**, **Life in Norway**

## Verification authorities

| Authority | When to call |
|---|---|
| **Kartverket** | Title verification, Matrikkelen lookup |
| **Kommune byggesak / planavdelingen** | Permits, reguleringsplan, byggesak history |
| **Skatteetaten** | Capital gains; beregnet markedsverdi + formuesverdi (a kommune may take its eiendomsskatt basis from Skatteetaten's beregnet markedsverdi) |
| **Kommune (eiendomsskatt)** | Eiendomsskatt — "Eiendomsskatt er en kommunal skatt" (source Skatteetaten, checked 2026-10-23) |
| **Megler** | Final transfer, escrow |
| **Kommunal VA** (e.g. Oslo VAV, Bergen Vann) | Mains/drains connection, VA-ledningskart, pålegg for private avløp (kommune = pollution authority, forurensningsforskriften § 12-2) |
| **NVE / NGI** | Skred / kvikkleire / flom check (NVE Temakart; event history in NSDB) |
| **DSA** (+ NGU radon map) | Radon — utleieboliger must be measured: < 200 Bq/m³, tiltak above 100 Bq/m³ (strålevernforskriften § 6) |
| **Borettslag forretningsfører** | If borettslag: financials, fellesgjeld details |
| **Sameieforvaltning** | If eierseksjon: sameieavgift, planned projects |

## Quirks to know

- **Gnr/Bnr/Fnr** — Norwegian way to identify property
- **Matrikkelnummer** = combined identifier
- **Hjemmel** = legal title; **rettigheter** = rights/easements
- **Heftelser** (encumbrances) on title — read all sections
- **Borett** (right to occupancy) in borettslag — different from ownership
- **Sameievedtekter** + **borettslagsvedtekter** must be read pre-purchase
- **TG2/TG3** flags in tilstandsrapport reduce buyer power
- **Festetomt** (leasehold ground) — separate festeavgift; check remaining lease
- **Konsesjon-pliktig** parcels: agricultural / forest above the konsesjonsloven § 4 (1) nr. 4 limits, plus helårsboliger in kommuner with a nedsatt konsesjonsgrense forskrift (§ 7); an erverv that needs konsesjon cannot be tinglyst until it is granted (§ 15) (2026 data, source: Lovdata — konsesjonsloven)
- **Kvikkleirefare-soner** (NVE Skrednett) — never build without geotechnical study
- **Strandsoneforbud**: 100 m coastal setback for new construction (plan- og bygningsloven § 1-8; a kommuneplan or reguleringsplan can set another byggegrense)
- **Oppdragsavtale** (broker engagement): max 6 months, renewable in writing for up to 6 months at a time, and either party can end it without notice (eiendomsmeglingsloven § 6-5); the megler still earns its fee on a sale agreed within 3 months after expiry with a buyer it negotiated with or informed during the term (§ 7-3 (2)) (2026 data, source: Lovdata — eiendomsmeglingsloven)

## Source URL templates

| Source | URL pattern |
|---|---|
| Kartverket Eiendomsregisteret (ex-Se Eiendom; seeiendom.kartverket.no 301-redirects here, updated 2026-10-23) | `https://eiendomsregisteret.kartverket.no/` |
| Finn.no | `https://www.finn.no/realestate/homes/search.html?location=<id>` |
| Eiendom Norge market | `https://eiendomnorge.no/` |
| SSB Boligprisindeks | `https://www.ssb.no/priser-og-prisindekser/boligpriser-og-boligprisindekser/statistikk/prisindeks-for-brukte-boliger` |
| NVE Atlas | `https://atlas.nve.no/` |
| NVE skredhendelser / NSDB (ex-Skrednett; skrednett.no 301-redirects here, updated 2026-10-23) | `https://www.nve.no/naturfare/laer-om-naturfare/om-skred/skredhendelser/` |
| NVE Temakart kvikkleire | `https://temakart.nve.no/tema/kvikkleire` |
| NVE Temakart skred i bratt terreng | `https://temakart.nve.no/tema/skredbrattterreng_tilpasset` |
| NVE Temakart flomaktsomhet | `https://temakart.nve.no/tema/flomaktsomhet` |
| NGU geo | `https://www.ngu.no/` |
| DSA Radon | `https://www.dsa.no/radon` |
| NGU radon aktsomhetskart | `https://www.ngu.no/geologi-og-risiko/radon` |
| Skatteetaten Eiendomsskatt | `https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bolig-og-eiendeler/bolig-eiendom-tomt/eiendomsskatt/` |
| MET Klima | `https://www.met.no/` |
| Klima i Norge 2025 (Norsk klimaservicesenter) | `https://klimaservicesenter.no/kss/rapporter/klima-i-norge-2025/oppsummeringer-fra-klima-i-norge-2025` |
| Statens vegvesen Vegkart (ÅDT på strekning) | `https://vegkart.atlas.vegvesen.no/` |
| Statens vegvesen Trafikkdataportalen | `https://trafikkdata.atlas.vegvesen.no/` |
| NORSAR | `https://www.norsar.no/` |
| Husbanken | `https://www.husbanken.no/` |
| Enova | `https://www.enova.no/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for the country profile, `--work`, active fiscal incentives, the legal + fiscal caveats, quirks, verification authorities and source URL templates (re-verified 2026-10-23 against SSB, Kartverket, Norges Bank, Brønnøysundregistrene, Arbeidstilsynet, Lovdata, Skatteetaten, Enova, Husbanken, NVE and DSA). HIGH for the figures re-sourced on 2026-10-23 inside `--price` (SSB price tables), `--tax` (dokumentavgift, tinglysingsgebyr, eiendomsskatt cap + SSB kommune counts, capital-gains and formuesskatt rates) and `--risks` (Gjerdrum toll, radon, earthquake zones, Klima i Norge 2025; tilstandsrapport not legally mandatory per DiBK), but MEDIUM for those sections overall: megler %, boligkjøperforsikring, the residential VAT exemption, fritidsbolig wealth valuation, felleskostnader, the Finn.no share, the skred / flood regional emphasis and the build-era rows are not source-verified. MEDIUM for the `--traffic` verdict bands (curated heuristic, no published threshold). LOW for the est. cost ranges (`--mains`, Cost benchmarks, tilstandsrapport cost) and for the subreddit list (not fetchable). MEDIUM for short-let regulation: the statutory letting and short-let tax rules were re-sourced on 2026-10-23 (Lovdata, Skatteetaten), but the 31-day kommune cap and the Oslo 30/60/90-day debate rest on no source. EU Regulation 2024/1028 applies in the EU since 20 May 2026 in opt-in/opt-out mode — Member States are not obliged to apply it (2026 data, source European Commission DG GROW, 20 May 2026) — and is not yet part of the EEA Agreement: EEA-Lex lists it as under scrutiny for incorporation by Iceland, Liechtenstein and Norway, with no Joint Committee decision (2026 data, source EFTA EEA-Lex 32024R1028), so it does not bind Norway until incorporated.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | EUR/NOK, Nynorsk share, selveier + borettslag household shares re-sourced (Norges Bank, SSB); postcodes, 15 fylker / 357 kommuner, gnr/bnr identifier and EEA status confirmed; 3 qualitative ownership-form lines unverified |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | AS NOK 30,000 (Brønnøysundregistrene) and 2025 median earnings (SSB 12852) re-sourced; minimum-wage regime per Arbeidstilsynet; Karriereguiden deprecated; platform rankings and the NUF line unverified |
| Active fiscal incentives (2025-2026) | 2026-10-23 | 2026-10-23 refresh wave | Enova programmes + grant caps, Husbanken products, BSU limits, 22 % interest-deduction value and skatteloven § 6-1 checked on primary pages |
| Caveats unique to NO (legal + fiscal lines) | 2026-10-23 | 2026-10-23 refresh wave | Dokumentavgift, avhendingslova 2022 reform, konsesjon + boplikt thresholds, foreign-buyer rule and 100 m building limit checked (Lovdata, Kartverket); fellesgjeld EUR range, NOK swing and the kvikkleire line not re-checked |
| Quirks to know | 2026-10-23 | 2026-10-23 refresh wave | Konsesjon (§§ 4, 7, 15), strandsone (pbl § 1-8) and oppdragsavtale (eiendomsmeglingsloven § 6-5) checked on Lovdata; the Kvikkleirefare-soner line not re-checked |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Eiendomsskatt reassigned to the kommune (Skatteetaten); VA, NVE and DSA rows refined; role-only rows not re-checked |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | All 13 URLs checked; Se Eiendom + Skrednett rows replaced (301 redirects); DSA + Skatteetaten deepened; Temakart, NGU radon, Klima i Norge 2025, Vegkart and Trafikkdata rows added |

Sections without a row (`--price`, `--traffic`, `--tax`, `--rental`, `--risks`, `--mains`, Cost benchmarks, Common listing platforms, Reddit / forum sources) were refreshed on 2026-10-23 but still carry unverified claims, so they keep the playbook-level date 2026-04-25.

## Extension TODOs

- [ ] Per-kommune eiendomsskatt + bunnfradrag specifics
- [ ] Borettslag fellesgjeld red-flag detection (debt %, repair backlog)
- [ ] Kvikkleire zone parcel-level lookup via NVE
- [ ] Konsesjon requirements per kommune
- [ ] Finn.no extraction patterns + sold prices
- [ ] Radon zones (NGU + DSA) overlay
- [ ] Hytte vs bolig tax distinctions
- [ ] EEA buyer rules (Norway non-EU but EEA)
- [ ] Festetomt remaining lease length lookup
- [ ] Tilstandsrapport TG-grade severity heuristics

## Update history

- **2026-04-25** — Initial population
- **2026-05-27** — Tier-1 corrections: fylker 11 → 15, eiendomsskatt kommune count and 4 ‰ residential cap, formuesskatt 2025 bands and the 2024 exit-tax reform added
- **2026-05-29** — Anti-hallucination sweep: source + year tags added to tax, rental and work figures
- **2026-10-23** — Refresh wave (market, tax-legal and risk-infra clusters) plus audit patches; playbook-level date kept at 2026-04-25 because `--price`, `--tax`, `--rental`, `--risks` and `--mains` still carry unverified claims:
  - Country profile — 12 checked: 4 changed (EUR/NOK 10.49 on 22 Oct 2026, Nynorsk share, selveier + borettslag household shares), 5 confirmed, 3 unverifiable
  - `--price` — 22 checked: 9 changed (price table re-sourced to SSB 14545 / 14310 / 07221; borettslag kjøpesum + fellesgjeld from SSB 11504; BRA-i area measure; Se eiendom → Eiendomsregisteret; Realkredittforeningen deprecated, SSB 10748 added), 8 confirmed, 5 unverifiable (Finn.no share — now "data not publicly available" beside SSB's ≈ 70 % coverage statement; felleskostnader range; hytte range — now est.; Norges Bank reports line; ownership-form math)
  - `--traffic` — 10 checked: 2 changed (NVDB ÅDT layer in Vegkart, Trafikkdataportalen), 3 confirmed, 5 unverifiable (verdict bands are a curated heuristic; ÅDT gloss)
  - `--tax` — 44 checked: 24 changed (eiendomsskatt 329 of 357 kommuner, 249 on boliger, 0.7 base factor, Oslo 1.7 ‰ for 2026; dokumentavgift on market value; tinglysingsgebyr NOK 585 → 545; capital-gains exemption wording; 12 % VAT list; formuesskatt 2026 bands; exit-tax scope; megler % now est.), 13 confirmed, 7 unverifiable (megler %, boligkjøperforsikring, residential VAT exemption, fritidsbolig wealth valuation, prior exit-tax allowance, 2027 bunnfradrag, borettslag-exemption debate)
  - `--rental` — 13 checked: 7 changed (tidsbestemt minimum, rent adjustment, borettslag 30-day rule, eierseksjon 90-day cap, 22 % / 50.6 % rates, short-let threshold NOK 10,000 → 15,000 with 85 % taxable, 2024/1028 not yet in the EEA Agreement), 1 confirmed, 3 unverifiable (31-day kommune cap, Oslo 30/60/90-day debate, BBL line)
  - `--work` — 14 checked: 5 changed (incl. SSB 12852 2025 median earnings, minimum-wage regime per Arbeidstilsynet, arbeidsplassen.no added, Karriereguiden deprecated), 4 confirmed, 5 unverifiable (platform rankings, Indeed.no, LinkedIn, "Statens lønnsstatistikk", NUF line)
  - `--risks` — 49 checked: 29 changed (Gjerdrum toll 10 → 11; tilstandsrapport not legally mandatory per DiBK; radon per DSA; earthquake zones per NORSAR; Klima i Norge 2025 projections; Skrednett → NVE skredhendelser / NSDB; NVE Temakart; asbestos ban 1985; energiattest rules), 9 confirmed, 11 unverifiable (skred regional emphasis, flood rivers, build-era rows, sale-document rows, tilstandsrapport cost — now est.)
  - `--mains` — 14 checked: 3 changed (Bergen Vann; Stavanger + IVAR IKS; forurensningsforskriften kap. 12 for private avløp), 2 confirmed, 9 unverifiable (5 cost ranges now est.)
  - Cost benchmarks — 14 checked: 4 changed (dokumentavgift on market value, tinglysingsgebyr 545, totals recomputed), 1 confirmed, 9 unverifiable (ranges now est.)
  - Active fiscal incentives — 12 checked: 4 changed (incl. the Enova programme list), 8 confirmed, 0 unverifiable
  - Caveats unique to NO — 9 checked: 6 changed (avhendingslova 2022 reform, konsesjon + boplikt thresholds, 100 m building limit), 3 confirmed, 0 unverifiable; foreign-buyer lines 2 checked, 2 changed (konsesjonsloven has no nationality criterion)
  - Quirks to know — 4 checked: 2 changed (konsesjon-pliktig parcels, oppdragsavtale term), 2 confirmed
  - Common listing platforms — 4 checked: 1 changed (Næringseiendom.no → NE.no), 2 confirmed, 1 unverifiable (Finn.no ~95 %)
  - Reddit / forum sources — 9 checked: 0 changed, 2 confirmed (The Local Norway, Life in Norway), 7 unverifiable (subreddits not fetchable)
  - Verification authorities — 9 checked: 4 changed (eiendomsskatt → kommune; VA, NVE, DSA rows), 1 confirmed, 4 unverifiable (role-only rows)
  - Source URL templates — 13 checked: 4 changed (Se Eiendom + Skrednett rows replaced after 301 redirects; DSA + Skatteetaten deepened; rows added), 9 confirmed
  - Status — short-let confidence line corrected (EU 2024/1028 is opt-in/opt-out in the EU and under scrutiny for EEA incorporation, not "transposition pending"); Confidence recomputed
