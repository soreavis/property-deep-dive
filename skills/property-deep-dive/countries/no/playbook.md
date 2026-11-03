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
- **SSB (Statistics Norway) Boligprisindeks** (prisindeks for brukte boliger): `https://www.ssb.no/priser-og-prisindekser/boligpriser-og-boligprisindekser/statistikk/prisindeks-for-brukte-boliger`
- **Norges Bank** Financial Stability Report, H1 and H2 editions (latest 2026 H1, 12 May 2026; before it 2025 H2, 12 Nov 2025): `https://www.norges-bank.no/en/news-events/publications/Financial-Stability-report/` (2026 data, source Norges Bank publications list)
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
| **Rural / hytte** | not covered by the SSB kr/m² series | fritidseiendom med bygning, fritt salg: average NOK 2,719,000 per sale nationally in 2025 (computed: NOK 30,877,779,000 / 11,358 sales, of which 2,411 on festet grunn); fylke averages from NOK 1,015,000 (Finnmark, 152 of 251 sales on festet grunn) to NOK 4,624,000 (Vestfold) (2025 data, source SSB table 11694, updated 27 Aug 2026 — `https://www.ssb.no/statbank/table/11694`); averages per sale, not per m² and not parcel values, and SSB notes that the mix of size, standard and location of the cabins sold varies (table 09332) — verify per listing |

- **12-month change**, SSB price index for resales, Q3 2025 → Q3 2026: Norway +3.3 %, Oslo med Bærum +0.1 %, Bergen +11.2 %, Stavanger +5.7 %, Trondheim +2.8 %, Nord-Norge +6.6 % (computed from SSB table 07221 index values, e.g. Bergen 147.9 → 164.4; 2026 data, source SSB).
- **Villa total price**: compute = enebolig kr/m² × the listing's BRA-i (e.g. 150 m² in Trondheim × NOK 38,078 ≈ NOK 5.7M); these SSB tables publish no average total price per villa.

### Compute

1. Listing NOK/m² = price (for borettslag: innskudd + andel fellesgjeld, as SSB computes it) / **BRA-i (internt bruksareal)**
2. **Trap**: **BRA-i** (NS 3940:2023) = usable area inside the unit's enclosing walls, including internal storage rooms and closets; the older **P-rom (primærrom)** = primary rooms only (excl. storage); **S-rom (sekundærrom)** = secondary. SSB computed kr/m² on P-rom for 2008–2024 and on BRA-i from Q1 2025, so kr/m² before and after are not directly comparable (2026 data, source SSB prisindeks for brukte boliger)
3. **Borettslag math**: the asking price (prisantydning) does not include the unit's share of **fellesgjeld** (cooperative shared debt): the broker's salgsoppgave must list prisantydning, andel fellesgjeld and all fees and costs separately, plus their sum (totalpris) (eiendomsmeglingsloven § 6-7 (2) nr. 13; source: Lovdata, 2026); SSB records kjøpesum and fellesgjeld separately (table 11504). The TRUE total cost = innskudd + fellesgjeld + felleskostnader future stream
4. **Eierseksjon math**: an eierseksjon is an ownership share in the whole seksjonert property with the exclusive right to use one bruksenhet (eierseksjonsloven § 4 bokstav a); felleskostnader are split by sameiebrøk as the main rule and paid as an akontobeløp set by the årsmøte or the styre (§ 29); the salgsoppgave must state the fellesgjeld loan terms and monthly felleskostnader, the sameie's relevant rights and obligations under law, vedtekter, vedtak and agreements, and essential budget and accounts information (eiendomsmeglingsloven § 6-7 (4), applying (3) nr. 1, 5 and 6) (source: Lovdata, 2026)

### Borettslag specific (CRITICAL)

For borettslag, always compute:
- **Innskudd** (your share value, like down payment) — what listing typically shows; SSB average kjøpesum per borettslag sale in fritt salg NOK 3,571,000 nationally / NOK 5,031,000 in Oslo (2026 Q2 data, source SSB table 11504)
- **Fellesgjeld** (cooperative shared building debt) — SSB average NOK 402,000 per sale nationally / NOK 373,000 in Oslo (2026 Q2; NOK 420,000–459,000 per quarter nationally in 2025) (2026 data, source SSB table 11504); est. NOK 500,000–3,000,000 per apartment for newer borettslag (wisdom, not data: no published source; the SSB averages above mix old and new borettslag, so they do not calibrate this range — the unit's andel fellesgjeld is in the salgsoppgave, eiendomsmeglingsloven § 6-7 (2) nr. 12–13)
- **Felleskostnader** (monthly common costs; the styre sets each andelseier's monthly amount, shared by the value of the homes or per the building and financing plan — borettslagslova § 5-19; source: Lovdata, 2026) — SSB survey average for andels- or aksjeeier households that pay fellesutgifter NOK 72,077 a year in 2025 ≈ NOK 6,006/month (computed: 72,077 / 12; 698 households answered, data collected Jan–May 2025); selveiere paying fellesutgifter to a sameie or similar NOK 34,089 a year (2025 data, source SSB table 14065, levekårsundersøkelsen — `https://www.ssb.no/statbank/table/14065`); a national survey mean, not a figure for any one borettslag — the unit's amount is in the salgsoppgave (spesifikasjon over faste løpende kostnader, eiendomsmeglingsloven § 6-7 (2) nr. 11)
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
- Bergen 2.6 ‰ (bunnfradrag NOK 750,000); Trondheim 2.65 ‰ (bunnfradrag NOK 700,000); Stavanger 1.0 ‰, reintroduced on boliger in 2026 after a 2025 pause (whole-kommune eiendomsskatt in 2023–2024, only næringseiendom / kraftanlegg etc. in 2025), no bunnfradrag (2023–2026 data, source: SSB table 14674)
- Many smaller kommuner: yes
- Bærum, Asker (Oslo wealthy suburbs): NO eiendomsskatt at all — also none in Drammen, Lier, Nordre Follo, Sandefjord, Tønsberg, Larvik, Færder, Sola (28 kommuner in total) (2026 data, source: SSB Kommuner uten eiendomsskatt)

### Transaction taxes — Dokumentavgift (MAJOR)

**2.5 % of the property's market value at tinglysing** — the sales value incl. buildings, not the price paid where they differ, e.g. gift or debt takeover (2026 check, source: Kartverket — Dokumentavgift ved overføring av fast eigedom, page dated 2023-09-27; rate set by Stortinget's dokumentavgift resolution, dokumentavgiftsloven § 1) — significant! Buyer (erverver of grunnbokshjemmel, § 6) pays.

**New-build rule**: on the first transfer of a wholly new building not yet taken into use, and on a transfer of a building under construction, dokumentavgift is charged on the plot's (tomt) sales value only; conversion, rehabilitation and extensions of an existing building pay on the full value of tomt + bygg (2026 data, source: Prop. 1 LS (2026–2027) ch. 20.2, citing Stortinget's dokumentavgift resolution § 3 for 2026, which moves to særavgiftsforskriften from 1 Jan 2027; regjeringen.no, archived 2026-10-21)

**CRITICAL EXEMPTION**: **Borettslag NOT subject to dokumentavgift** (only selveier + eierseksjon).
- Saving = 2.5 % of value — e.g. NOK 125,000 on a NOK 5,000,000 purchase (computed: 5,000,000 × 2.5 %)
- **Borettslag transfer**: only **NOK 545** flat fee per overføring of andel, and no dokumentavgift (2026 data, source: Kartverket — Tinglysingsgebyr "Gebyr 2026" + Borettslag page)

**Tinglysningsgebyr** (registration fee): **NOK 545** per document — skjøte and pantedokument each charged separately (2026 data, source: Kartverket — Tinglysingsgebyr, "Gebyr 2026", updated 2026-01-05)

### Other transaction costs

- **Megler** (broker): the fee is set by agreement. Finanstilsynet's broker statistics give NOK 8,577,346,971 in meglervederlag on NOK 539,002,605,001 of homes sold through eiendomsmeglingsforetak in 2023 ≈ **1.59 %** of price (computed; NOK 62,996 per sale; county averages computed from the same file run from 1.28 % in Oslo to 2.27 % in Innlandet); the newest file, first half 2024, gives 2.13 % (computed: NOK 6,935,200,200 / NOK 325,544,730,927; its Rogaland row alone is 6.11 %) (2023–2024 data, source: Finanstilsynet — Statistikk for eigedomsmekling, "Totalt 2023" and første halvår 2024 files) — rates/figures may have changed since. The figure to rely on is the specified total cost estimate the written oppdragsavtale must contain (eiendomsmeglingsloven § 6-4 (1) nos. 4–6). Paid by the seller as oppdragsgiver: the fee and outlays cannot be agreed to be paid by anyone else, e.g. the buyer (§ 7-2 (4)); a commission whose percentage rises with the price is banned (§ 7-2 (1)), and the megler must also offer an hourly-rate quote (§ 7-2 (2)) (2026 data, source: Lovdata — eiendomsmeglingsloven, as amended to LOV-2025-06-20-106)
- **Legal/conveyancing**: most use megler + standard contracts; full lawyer rare
- **Boligkjøperforsikring** (buyer insurance): voluntary; est. ~NOK 5,000–15,000 — insurer pricing, not from an official price statistic; check the insurer's written price and terms before bidding — **highly recommended**

### Total transaction cost (buyer side)

- **Selveier / eierseksjon (resale)**: ≈ 2.6–2.8 % on a NOK 5,000,000 purchase (computed: 2.5 % dokumentavgift = NOK 125,000 + 2 × NOK 545 tinglysing for skjøte + pantedokument + est. NOK 5,000–15,000 boligkjøperforsikring); a new build pays dokumentavgift on the plot value only (see Dokumentavgift), so its total is lower
- **Borettslag**: ≈ 0.2–0.5 % on a NOK 3,000,000 andel (computed: 2 × NOK 545 + est. NOK 5,000–15,000 boligkjøperforsikring; no dokumentavgift; fees charged by the borettslag's forretningsfører not included)

### Capital gains

- **22 %** as alminnelig inntekt (18.5 % in the Troms og Finnmark tiltakssone) (2026 data, source: Skatteetaten — satser, alminnelig inntekt)
- **Primary residence exemption**: owned **more than 1 year** when the sale is made or agreed + whole property used as own home **at least 1 of the last 2 years** → fully exempt; covers selveier, andel in borettslag and aksjeleilighet (2026 data, source: Lovdata — skatteloven § 9-3 (2))
- **Fritidsbolig exemption**: owned more than 5 years (and more than 5 years since it was taken into use or completed) + used as own fritidsbolig at least 5 of the last 8 years (2026 data, source: Lovdata — skatteloven § 9-3 (4))
- Investment property: full 22 % on gain

### VAT (mva)

- 25 % standard
- 15 % reduced (food)
- 12 % reduced (passenger transport, accommodation, public broadcasting, admission to cinema, sports events, amusement parks, experience centres); 15 % also on water + sewerage services (2026 rates, source: Skatteetaten — satser, merverdiavgift)
- Sale and letting of fast eiendom: **exempt from the VAT act** (merverdiavgiftsloven § 3-11 (1)); § 3-11 (2) brings back in e.g. hotel-type room letting, parking in a parking business and letting under a voluntary registration (§ 2-3). A business building or renovating for sale or letting on its own account must compute uttak VAT on the goods and services it uses (§ 3-26) (2026 data, source: Lovdata — merverdiavgiftsloven, as amended to LOV-2025-12-22-121)

### Future risk

- Eiendomsskatt residential cap at **4 ‰ (0.4 %)** (eskl. § 11, last amended from tax year 2021); Prop. 1 LS (2026–2027) restates the 4 ‰ maximum for bolig and fritidsbolig in 2026 and none of its Del II proposals changes eiendomsskatt (source: Prop. 1 LS (2026–2027) ch. 2.3.4 + contents, regjeringen.no, archived 2026-10-21; Estate Nyheter, 7 Oct 2026 — secondary)
- **Formueskatt (wealth tax) — 2026**: no tax below **NOK 1,900,000 single / NOK 3,800,000 couples** taxed jointly; above that 0.35 % kommune + 0.65 % state = 1.0 %; state rate 0.75 % above NOK 21,500,000 → 1.1 % (2026 data, source: Skatteetaten — satser, formuesskatt). Boligverdsetting: primærbolig 25 % of market value up to **NOK 14,000,000** and 70 % above (raised from NOK 10M, Prop. 95 LS (2025–2026)); sekundærbolig 100 % (2026 data, source: Skatteetaten — satser, formuesverdi bolig). Fritidsbolig is not valued, as primær- and sekundærbolig are, at a share of Skatteetaten's estimated market value: a new one is valued at 30 % of kostpris incl. tomt (or 30 % of market value); an earlier value can carry over to a new owner and rises with nybygg / påkostning, but never above 30 % of market value — the owner can claim it down to 30 % of documented market value; no annual adjustment was adopted for income year 2025 (2026 check, source: Skatteetaten — Formuesverdi av fritidseiendom; Prop. 1 LS (2026–2027) ch. 2.3.4, regjeringen.no, archived 2026-10-21). Updated valuation model from the 2026 income year uses sales data per grunnkrets instead of per kommune (source: Skatteetaten — formuesverdi). The 2025 return still uses NOK 1,760,000 / 3,520,000, 0.525 % kommune + 0.475 % state (0.575 % above NOK 20,700,000) and the NOK 10M primærbolig threshold (source: Skatteetaten — satser, year 2025). **2027 (proposal only, not adopted)**: Prop. 1 LS (2026–2027) raises the bunnfradrag by NOK 90,000 to **NOK 1,990,000 single / NOK 3,980,000 couples** and keeps the rates (0.35 % kommune maximum + 0.65 % state, 0.75 % state above NOK 21,500,000), the NOK 21.5M trinn-2 threshold, the NOK 14M primærbolig threshold and the 25 / 70 / 100 % valuation shares unchanged (source: Prop. 1 LS (2026–2027) table 1.5, ch. 4.2 and draft skattevedtak 2027 §§ 2-1, 2-3, regjeringen.no, archived 2026-10-21); final figures: Stortinget's skattevedtak for income year 2027
- **Utflyttingsskatt (2024 exit-tax reform)** — latent gains on shares, aksjesparekonto and similar holdings when leaving Norway, not real property (§ 10-70 (2)): applies to exits from 20 Mar 2024 (further changes from 7 Oct 2024); **NOK 3M basic allowance** — only net gain above NOK 3,000,000 is taxed on exit; transfers to a person or entity abroad are taxed once the year's net gain exceeds NOK 100,000; pay at exit or defer for up to 12 years (security required — for moves within the EEA only where collection is at real risk), either 1/12 a year interest-free or in full at the end of the period with interest; the deferral ends after 12 years even without a sale, and earlier on realisation (2026 data, source: Lovdata — skatteloven § 10-70 (2), (4), (7), (8), as amended by lov 20 des 2024 nr. 86; Prop. 1 LS (2026–2027) ch. 2.3.1, regjeringen.no, archived 2026-10-21)
- **Borettslag exemption from dokumentavgift** — in force: the avgift attaches to tinglysing of a document transferring hjemmel to fast eiendom, and the draft 2027 resolution keeps 2.5 % plus NOK 1,000 per transfer when a borettslag or boligaksjeselskap is dissolved. Prop. 1 LS (2026–2027) proposes no dokumentavgift change for 2027: Skattekommisjonen (NOU 2026: 9) asked for a review of the new-build rule (plot value only) and the ministry declined (source: Prop. 1 LS (2026–2027) ch. 10.22, ch. 20 + draft dokumentavgift resolution 2027 §§ 1–2, regjeringen.no, archived 2026-10-21)
- **Inherited / gifted homes (2027 proposal, not adopted)**: a bolig or fritidsbolig the deceased or giver could have sold tax-free would give neither taxable gain nor deductible loss if the heir or recipient sells within one year of the inheritance or gift (new skatteloven § 9-7 (5) fifth sentence, from income year 2027) (source: Prop. 1 LS (2026–2027) ch. 3.3, regjeringen.no, archived 2026-10-21)
- **Tax reform pending**: the government is assessing Skattekommisjonen's NOU 2026: 9 (consultation closed 24 Sep 2026) and will report to Stortinget on its follow-up early in 2027 (a white paper on comprehensive tax reform), so it proposes only minor formuesskatt changes for 2027 (source: Prop. 1 LS (2026–2027) ch. 1.1 + 4.1, regjeringen.no, archived 2026-10-21)

---

## Section: `--rental`

### Long-term residential

- **Husleieloven** (Tenancy Act): tenant-protective
- **Tidsbestemt** (fixed-term) lease for bolig: minimum **3 years**; 1 year allowed for a loft or basement unit in an enebolig / tomannsbolig where the landlord lives in the same house; no minimum where the landlord or a household member will use the home, or the landlord has another objective reason, stated in writing at signing; a lease breaching the rule counts as tidsubestemt (husleieloven § 9-3; source: Lovdata, 2026)
- **Husleieloven** rent changes: KPI indexation at most once a year with at least 1 month's written notice (§ 4-2); adjustment to gjengs leie (market rent) once the lease has run 2 years 6 months with no other change (§ 4-3) (source: Lovdata, 2026)
- **Boligbyggelagene** (BBL): NBBL's 36 member boligbyggelag have over 1,350,000 members and manage just over 650,000 homes in over 17,500 boligselskap (housing companies) (2026 data, source NBBL, industry body ⚠️ — `https://www.nbbl.no/om-oss/`)

### Short-let (Airbnb / Booking)

**Letting rules** (significant):
- **Sekundærbolig** (secondary housing): no fixed day limit marks when short-letting becomes næringsvirksomhet — the kommune weighs the whole (how often, how it is organised, services offered, effects on neighbours), and hotel-like use can require a søknad om bruksendring under plan- og bygningsloven (source: Kommunal- og distriktsdepartementet press release, 24 Mar 2026, archived 2026-04-20 — `https://www.regjeringen.no/no/aktuelt/lanserer-veileder-om-kortidsutleie/id3153968/`); letting within the eierseksjon 90-day cap below can still require one (source: KDD veileder «Korttidsutleie: Når går boligen fra å være et hjem til å bli næringsvirksomhet?», Mar 2026, archived 2026-08-31 — `https://www.regjeringen.no/contentassets/725a26fdd68f4009b3cc069b0109e0d5/no/pdfs/veileder-kortidsutleie.pdf`). A hjemmel for local day limits, and one for limiting short-let of sekundærboliger, are among the new legal bases kommuner ask for; one local example: Stryn kommune decided in Dec 2025 that homes on kommunale boligtomter may be short-let at most 30 days a year without the kommune's consent (source: Husbanken, «Korttidsutleie som styringsutfordring», oppdrag 11/2025, Mar 2026 — `https://biblioteket.husbanken.no/arkiv/dok/Komp/Korttidsutleie%20som%20styringsutfordring%20kommunenes%20erfaringer%20og%20behov%20for%20regulering.pdf`)
- **Oslo**: per Oslo kommune, 3 % of the city's dwelling stock — ca. 12,000 homes in June 2025, most in the city centre — was listed for short-let, and reports of illegal short-letting are rising (9 new cases in January 2026 alone) (2025–2026 data, per Oslo kommune as reported in the Husbanken report above). Nationally, Stortingsvedtak nr. 1221 (2024–2025) asks the government to study during 2026 powers for kommuner to ban short-letting in all or part of the kommune, and for borettslag and sameier to limit and enforce short-let rules better (source: Husbanken report above); KDD is studying plan- og bygningsloven changes, among them powers to require data from platforms and landlords on the number of lets and nights when illegal short-letting is suspected, and tools for local regulation (source: KDD press release, 22 Dec 2025, archived 2026-08-14 — `https://www.regjeringen.no/no/aktuelt/det-skal-bli-enklere-a-regulere-og-folge-opp-ulovlig-korttidsutleie/id3144320/`) — status of any bill: verify at `https://www.regjeringen.no/no/dep/kdd/id504/`
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
  - **Kvikkleireskred** (quick clay slide) — devastating; quick clay can occur anywhere below the marine limit (source NVE, page updated 2026-04-30), which lies 0–220 m above today's sea level depending on location (source NGU); triggered by stream/river erosion or by excavation at the slope toe / fill on the slope top (source NVE)
  - Where: quick clay is most common in **Trøndelag + Østlandet**, and occurs in many smaller areas of valley, fjord and shore landscapes (source NGU); for snø-, stein- and jordskred, screen the address on NVE's skred i bratt terreng map (above)
  - **Fjellskred + flodbølge** (rock avalanche into a fjord): Loen 1905 + 1936 cost 134 lives; the 1934 Tafjorden slide sent waves up to 61 m above sea level onto land (17 m in Tafjord itself), 22 dead in Tafjord + 18 in Fjørå (source NVE fjellskred veileder, revised 2024-05-07). NVE monitors 10 unstable mountainsides continuously and 23 periodically (source NVE, page updated 2026-04-17); the continuous ones are in Møre og Romsdal (Åknes, Mannen, Hegguraksla), Vestland (Joasetbergi, Tussafoten, Stiksmoen), Kåfjord kommune (Gámanjunni 3, Jettan, Indre Nordnes) and Vang (Skutshorn) (source NVE, list updated 2026-06-19)
  - **Gjerdrum quick-clay slide, 30 Dec 2020** (11 dead, source NVE): kvikkleire reminder
- **Flom (flooding)**:
  - River floods: ekstremværet Hans (Aug 2023) broke historic water-level records in several places, with the longest-lasting impact in the lower Drammensvassdraget + Glommavassdraget (source NVE, Tørke-, flom- og jordskredåret 2023, updated 2024-01-09); for the address, use NVE's aktsomhetskart for flom / faresonekart flom (above)
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
| **Pre-1960s** | Asbestos possible (see Asbestos row); old facade paint may contain lead — some buildings have paint high in heavy metals such as bly and sink, banned substances still found on older buildings (source Bergen kommune, page updated 2025-05-27; Bergen guidance, not a national survey) — test before sanding or stripping old paint; little insulation by today's standards — curated wisdom, not data |
| **1960s–1980s panelhus + concrete** | Asbestos possible — the period of heaviest use ran from after WWII to c. 1980 (source Arbeidstilsynet; see Asbestos row) |
| **1990s–2000s** (byggeforskrift 1987 until TEK97, FOR-1997-01-22-33, in force 1 Jul 1997) | Better insulation and wiring than older stock — curated wisdom, not data |
| **Post-2010 TEK10** (FOR-2010-03-26-489, in force 1 Jul 2010) | Energy requirements in kap. 14 (§ 14-2 krav til energieffektivitet); § 14-4 as amended by FOR-2015-11-12-1290 (in force 1 Jan 2016) bars installing heating for fossil fuel (source Lovdata) |
| **Post-2017 TEK17** (in force 1 Jul 2017, FOR-2017-06-19-840) | Energy requirements in kap. 14 (no fossil-fuel heating installations, § 14-4) + tilgjengelig boenhet in buildings that must have a heis, where for units up to 50 m² BRA at least 50 % of them suffice (§ 12-2) (source Lovdata) |
| **Wood construction** | Common — fire risk + moisture; brannsmitte — curated wisdom, not data |
| **Asbestos** | Used c. 1920–1985, heaviest post-WWII to 1980; total ban 1985 — survey any building erected before 1985 (source Arbeidstilsynet, checked 2026-10-23) |

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energimerking** (energiattest) | Mandatory at sale + letting; owner duty since 1 Jul 2010; shown to buyer before contract, else buyer may order one at seller's cost within 1 year (energimerkeforskriften §§ 5, 23) | Up to 10 years (§ 4) |
| **Tilstandsrapport** (condition report) | **Not legally mandatory** (DiBK) — voluntary, but since 1 Jan 2022 the buyer is deemed to know what an approved report clearly shows (avhendingslova § 3-10), so a seller without one is more easily liable for defects (DiBK) | Max 1 year old when the buyer commits (forskrift § 1-6) |
| **Egenerklæring** (seller's declaration) | Not required by avhendingslova, eiendomsmeglingsloven, eiendomsmeglingsforskriften or FOR-2021-06-08-1850; the duty behind it is statutory — the property is defective if the buyer was not told something the seller knew or ought to have known and the buyer had reason to expect to be told (avhendingslova § 3-7), or if it differs from what the seller stated (§ 3-8), in both cases only where this can be assumed to have affected the contract | At sale |
| **Egenmelding skadedyr** (pest declaration) | No statutory basis found (checked 2026-10-23) — verify with megler; an approved tilstandsrapport must look for spor etter skadedyr in våtrom, takkonstruksjon and rom under terreng (forskrift §§ 2-2, 2-9, 2-15) | At sale |
| **Eierskifteforsikring** (seller's insurance) | Optional — no statutory duty found; meglere may not broker it for a fee (eiendomsmeglingsforskriften § 5-1 (2) a) | Per case |
| **Boligsalgsrapport** (older format) | Pre-2022 report format with no statutory definition (curated wisdom, not data); since 1 Jan 2022 a tilstandsrapport counts as approved for avhendingslova § 3-10 if it meets FOR-2021-06-08-1850, and ubetydelige deviations from the forskrift's kap. 2 do not remove that effect (forskrift § 1-5) | n/a for new |

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
- Kommunal vann og avløp is run by the kommune itself or through an inter-municipal company (IKS, e.g. IVAR below)
- Major: **Oslo VAV** (Vann- og avløpsetaten), **Bergen Vann** (Bergen kommune), **Trondheim kommune** (contact: Trondheim bydrift), **Stavanger kommune** (vann og avløp); **IVAR IKS** (Stavanger-based) delivers drinking water to 12 kommuner — check whether it supplies the target kommune (checked 2026-10-23)

### Verification

- Kommunal vannforsyning reaches 85.2 % of the population (2025 data, source SSB, updated 2026-06-15) and kommunal avløp 86.4 % (2025 data, source SSB, updated 2026-10-23). Innlandet fylke ≈73.2 % on kommunal vann, computed from SSB table 11787 (kommune-reported connected inhabitants, 2025: 277,901) ÷ SSB table 07459 (population on 1 Jan 2026: 379,488). City figures in table 11787 are rounded and repeated year to year (Bergen 264,230 for 2020–2025, Trondheim 182,000 for 2021–2025), so they give no current city share. Fylke-level shares are not proof that a given address is connected: ask the kommune
- **Hytter (cabins) + rural**: own **brønn** (well) + **slamavskiller** (septic) — 738,298 inhabitants are on one of 321,207 small avløpsanlegg under 50 pe (2025 data, source SSB tables 05272 + 05274, updated 2026-10-23)
- **Private avløpsanlegg** (bolig, hytte, < 50 pe) fall under forurensningsforskriften kap. 12: the kommune is the pollution authority (§ 12-2); discharges established before 1 Jan 2007 stay lawful unless the kommune sets a deadline by forskrift or enkeltvedtak (§ 12-16) → ask the kommune about any pålegg om oppgradering

### Costs

| Scenario | Cost (NOK, est.) |
|---|---:|
| Tilkobling to mains | 50,000–150,000 |
| Mains-line extension via kommune | 100,000–500,000+ |
| Slamavskiller upgrade | 100,000–250,000 |
| Pre-renseanlegg / minirenseanlegg | 150,000–400,000 |
| Borebrønn (drilled well) | 80,000–150,000 |

Unsourced est. ranges (contractor-market prices) — get contractor quotes. The kommunal part is published: the one-off tilknytningsgebyr (forurensningsforskriften kap. 16, § 16-3) for a standard 120 m² bolig, ekskl. mva, is NOK 10,957 for vann + NOK 11,656 for avløp in SSB's national ('Landet') figure for the one-rate (én sats) fee, but NOK 114,870 + 76,518 in Oslo, 3,540 + 3,540 in Bergen, 6,886 + 6,886 in Trondheim and 5,112 + 7,644 in Stavanger (2026 data, source SSB table 12842, updated 2026-06-15). Oslo's two fees alone (NOK 191,388) exceed the Tilkobling row's range, so take the target kommune's gebyrregulativ.

---

## Cost benchmarks (NO 2026)

| Work | Cost (NOK) |
|---|---:|
| Energimerking (energiattest) | 0 when the owner self-registers an existing home (Enova, 2026); hired expert est. ~5,000–12,000 |
| Tilstandsrapport | est. ~15,000–35,000 |
| Megler (paid by the seller, eiendomsmeglingsloven § 7-2 (4)) | ≈ 1.59 % of price on average, NOK 62,996 per sale (2023, Finanstilsynet; computed in `--tax`) |
| **Dokumentavgift (selveier + eierseksjon; borettslag exempt)** | **2.5 % of market value** (Kartverket) |
| Tinglysningsgebyr | 545 per document (2026, Kartverket) |
| Boligkjøperforsikring (recommended) | est. ~5,000–15,000 |
| **Total transaction cost (selveier, resale)** | **≈ 2.6–2.8 %** on NOK 5,000,000 (computed in `--tax`; new builds pay dokumentavgift on the plot value only) |
| **Total transaction cost (borettslag)** | **≈ 0.2–0.5 %** on NOK 3,000,000 (computed in `--tax`) |
| Slamavskiller upgrade | est. ~100,000–250,000 |
| Roof (concrete tile, 150 m²) | est. ~250,000–500,000 |
| Asbestos abatement (small house) | est. ~100,000–400,000 |
| Energy retrofit (Class C → A) | est. ~600,000–1,500,000 |
| Radon mitigation | 20,000–49,999 for 44 % of households that acted (DSA survey, 2023 data — see note) |
| Brann + lyd retrofit (apartment) | est. ~50,000–200,000 |

*Energimerking: the owner may register an existing home in Enova's energimerkesystem (energimerkeforskriften § 12) and receives the energiattest free; new homes must be marked by an expert (2026 data, source: Enova — Energimerk din bolig; Lovdata — energimerkeforskriften). Attests issued from 1 Jan 2026 use a new A–G scale with a new calculation method (NS 3031:2025), so a pre-2026 attest's letter is on a different scale from a 2026 one; attests under the old model stay valid until their expiry date; the energy-retrofit row's C → A does not say which scale it uses (source: Enova — Ny karakterskala, scale documents dated 2025-12-19; Enova — Om energimerkeordningen 2026). Radon (computed): DSA's autumn-2023 survey of 582 respondents who had measured above 100 Bq/m³ in the previous ten years — of those that had acted, 11 % reported NOK 20,000–29,999, 21 % NOK 30,000–39,999 and 12 % NOK 40,000–49,999 (11 + 21 + 12 = 44 %), and 11 % NOK 1,000–4,999; DSA-info reports no other brackets; the sample is not representative (72 % from Østlandet, mostly eneboliger) (2023 data, source: DSA-info 11/2024) — rates/figures may have changed since. Megler: Finanstilsynet broker statistics, computed in `--tax` (2023 data) — rates/figures may have changed since. The expert-energimerking, tilstandsrapport, boligkjøperforsikring, slamavskiller, roof, asbestos, energy-retrofit and brann + lyd ranges are order-of-magnitude estimates, not taken from a published Norwegian tariff, price book or survey; calibrate against written quotes. Dokumentavgift and tinglysingsgebyr: 2026 data, source Kartverket; totals computed in `--tax`.*

## Active fiscal incentives (2025-2026)

- **Enova** home grants (2026 data, source: enova.no — Støtte til tiltak i hjemmet): luft-til-vann + væske-til-vann varmepumpe, varmepumpebereder, etterisolering (tak/loft, vegg), energieffektive vinduer + ytterdører, oppgradering av bygningskroppen, balansert ventilasjon, solcelleanlegg, solfanger, energirådgivning; e.g. solcelleanlegg 25 % of approved invoiced costs capped at NOK 2,500 per kW, luft-til-vann varmepumpe 25 % capped at NOK 20,000; luft-til-luft varmepumpe is not on the list
- **Husbanken** (2026 data, source: husbanken.no — Lån fra Husbanken + Startlån): loans to build a miljøvennlig or livsløpsbolig, to upgrade an existing home with extensive measures that cut energy use, or to buy a new home in a Husbanken-approved project; **startlån** via the kommune for people with long-term difficulty getting a bank loan — no general first-purchase energy loan
- **Boligsparing for ungdom (BSU)**: savers under 34 (contributions through the year they turn 33); NOK 27,500/yr cap, NOK 300,000 total; tax deduction 10 % of the amount saved; no deduction for a year in which the saver owns (directly or via borettslag) a primary or secondary home on 31 Dec (2026 data, source: Skatteetaten — satser, BSU)
- **Rentefradrag**: mortgage interest is deductible in alminnelig inntekt, worth 22 % of the interest (18.5 % in the Troms og Finnmark tiltakssone) (computed from the 2026 Skatteetaten rate for alminnelig inntekt + Skatteetaten — Lån og renter) — significant subsidy
- **Skatteloven § 6-1**: retrofit and maintenance costs are deductible only against taxable income (e.g. taxable letting); § 6-1 (2) bars deductions for private housing costs, so owner-occupiers get no tax deduction for retrofit (2026 data, source: Lovdata — skatteloven § 6-1)

## Common listing platforms

- **Finn.no** — DOMINANT (market-share figure: data not publicly available; per SSB, FINN.no-advertised homes make up ≈ 70 % of housing transactions in fritt salg — see `--price`), full extraction
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
**Confidence**: HIGH for the country profile, `--work`, active fiscal incentives, the legal + fiscal caveats, quirks, verification authorities and source URL templates (re-verified 2026-10-23 against SSB, Kartverket, Norges Bank, Brønnøysundregistrene, Arbeidstilsynet, Lovdata, Skatteetaten, Enova, Husbanken, NVE and DSA). HIGH for `--price`: every material number is confirmed on SSB, Norges Bank or Lovdata pages, computed with inputs shown, or labelled (Finn.no share: data not publicly available, beside SSB's ≈ 70 % coverage statement; fellesgjeld range for newer borettslag: est., wisdom not data). HIGH for the figures re-sourced on 2026-10-23 inside `--tax` (dokumentavgift incl. the new-build rule, tinglysingsgebyr, eiendomsskatt cap + SSB kommune counts, capital-gains and formuesskatt rates, the VAT exemption, fritidsbolig valuation, the 2027 Prop. 1 LS proposal, the megler fee from Finanstilsynet's 2023 statistics), `--risks` (Gjerdrum toll, radon, earthquake zones, Klima i Norge 2025, NGU + NVE skred and flood material, TEK97 / TEK10 / TEK17, asbestos, sale-document rules; tilstandsrapport not legally mandatory per DiBK) and `--mains` (SSB connection shares + tilknytningsgebyr, forurensningsforskriften kap. 12 + 16), but MEDIUM for those sections overall: they are not yet confirmed as fully re-verified, boligkjøperforsikring stays est., and several build-era and sale-document rows carry curated wisdom, not data. MEDIUM for the `--traffic` verdict bands (curated heuristic, no published threshold). LOW for the est. cost ranges (`--mains`, Cost benchmarks, tilstandsrapport cost) and for the subreddit list (not fetchable). HIGH for `--rental`: the statutory letting and short-let tax rules were re-sourced on 2026-10-23 (Lovdata, Skatteetaten); the sekundærbolig and Oslo short-let lines rest on KDD (regjeringen.no, archived) and Husbanken material, the BBL line on NBBL (industry body ⚠️). EU Regulation 2024/1028 applies in the EU since 20 May 2026 in opt-in/opt-out mode — Member States are not obliged to apply it (2026 data, source European Commission DG GROW, 20 May 2026) — and is not yet part of the EEA Agreement: EEA-Lex lists it as under scrutiny for incorporation by Iceland, Liechtenstein and Norway, with no Joint Committee decision (2026 data, source EFTA EEA-Lex 32024R1028), so it does not bind Norway until incorporated.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| Country profile | 2026-10-23 | 2026-10-23 refresh wave | EUR/NOK, Nynorsk share, selveier + borettslag household shares re-sourced (Norges Bank, SSB); postcodes, 15 fylker / 357 kommuner, gnr/bnr identifier and EEA status confirmed; 3 qualitative ownership-form lines unverified |
| `--price` | 2026-10-23 | 2026-10-23 refresh wave + gap-closing pass | Price table (SSB 14545 / 14310 / 07221), borettslag kjøpesum + fellesgjeld (SSB 11504), hytte averages (SSB 11694), felleskostnader (SSB 14065), Norges Bank FSR editions and the salgsoppgave, eierseksjon and borettslag cost rules (Lovdata) confirmed or re-sourced; Finn.no share "data not publicly available"; newer-borettslag fellesgjeld range labelled est. (wisdom, not data) |
| `--rental` | 2026-10-23 | 2026-10-23 refresh wave + gap-closing pass | husleieloven, borettslagslova, eierseksjonsloven and skatteloven § 7-2 rules re-confirmed on Lovdata, 22 % / 50.6 % rates per Skatteetaten; the unsourced 31-day kommune cap and Oslo 30/60/90-day debate replaced with KDD (archived) + Husbanken material; BBL line re-sourced to NBBL (industry body) |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | AS NOK 30,000 (Brønnøysundregistrene) and 2025 median earnings (SSB 12852) re-sourced; minimum-wage regime per Arbeidstilsynet; Karriereguiden deprecated; platform rankings and the NUF line unverified |
| Active fiscal incentives (2025-2026) | 2026-10-23 | 2026-10-23 refresh wave | Enova programmes + grant caps, Husbanken products, BSU limits, 22 % interest-deduction value and skatteloven § 6-1 checked on primary pages |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave + gap-closing pass | Finn.no share relabelled "data not publicly available" beside SSB's ≈ 70 % coverage statement; Næringseiendom.no → NE.no; agency networks + Hjem.no confirmed |
| Caveats unique to NO (legal + fiscal lines) | 2026-10-23 | 2026-10-23 refresh wave | Dokumentavgift, avhendingslova 2022 reform, konsesjon + boplikt thresholds, foreign-buyer rule and 100 m building limit checked (Lovdata, Kartverket); fellesgjeld EUR range, NOK swing and the kvikkleire line not re-checked |
| Quirks to know | 2026-10-23 | 2026-10-23 refresh wave | Konsesjon (§§ 4, 7, 15), strandsone (pbl § 1-8) and oppdragsavtale (eiendomsmeglingsloven § 6-5) checked on Lovdata; the Kvikkleirefare-soner line not re-checked |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Eiendomsskatt reassigned to the kommune (Skatteetaten); VA, NVE and DSA rows refined; role-only rows not re-checked |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | All 13 URLs checked; Se Eiendom + Skrednett rows replaced (301 redirects); DSA + Skatteetaten deepened; Temakart, NGU radon, Klima i Norge 2025, Vegkart and Trafikkdata rows added |

Sections without a row (`--traffic`, `--tax`, `--risks`, `--mains`, Cost benchmarks, Reddit / forum sources) were refreshed on 2026-10-23 but are not confirmed as fully re-verified (`--traffic` verdict bands and the subreddit list stay unverified), so they keep the playbook-level date 2026-04-25.

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
- **2026-10-23** — Refresh wave (market, tax-legal and risk-infra clusters) plus audit patches and a gap-closing pass; playbook-level date kept at 2026-04-25 because `--tax`, Cost benchmarks, `--risks` and `--mains` remain open (not confirmed as fully re-verified); `--price`, `--rental` and Common listing platforms are closed:
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
  - Gap-closing pass (confirmed / changed / relabelled) — 21 / 27 / 13: `--price` 5 / 4 / 1 (Norges Bank FSR editions, hytte averages SSB 11694, eierseksjon rules, felleskostnader SSB 14065; newer-borettslag fellesgjeld range est.), `--rental` 5 / 3 / 1 (31-day kommune cap + Oslo debate replaced with KDD + Husbanken material, BBL line per NBBL), `--tax` 3 / 8 / 1 (VAT exemption, fritidsbolig valuation, 2027 bunnfradrag proposal NOK 1,990,000 / 3,980,000, megler ≈ 1.59 % per Finanstilsynet 2023, new-build dokumentavgift rule, exit-tax deferral rules; boligkjøperforsikring est.), Cost benchmarks 0 / 3 / 2 (energimerking self-registration, radon DSA survey), `--risks` 7 / 7 / 6 (NGU + NVE skred and flood, TEK97 / TEK10 / TEK17, sale-document rows), `--mains` 1 / 2 / 1 (SSB connection shares, SSB 12842 tilknytningsgebyr), Common listing platforms 0 / 0 / 1 (Finn.no share); Status Confidence and per-section rows updated
