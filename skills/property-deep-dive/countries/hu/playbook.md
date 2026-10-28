# Hungary 🇭🇺 — Property Due-Diligence Playbook

ISO2: `hu`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1011` Budapest I, `1051` Budapest V Belváros, `4024` Debrecen, `6720` Szeged)
- **Admin levels**: 19 vármegye (counties) + Budapest (capital) + 23 districts in Budapest + **3,155 települések** (settlements) on 1 Jan 2026 — 26 county-rank cities incl. Budapest, 322 other towns, 133 nagyközségek, 2,674 községek (2026 data, source KSH STADAT 8.1.2.2, `https://www.ksh.hu/stadat_files/fol/hu/fol0007.csv`)
- **Currency**: **HUF** (Hungarian forint); 1 EUR = 366.43 HUF on 22 Oct 2026; ECB reference-rate range over the 12 months to 22 Oct 2026: 349.53–396.38 HUF (volatile) (2026 data, source ECB euro foreign exchange reference rates, `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml`)
- **Languages**: Hungarian (official); German, Slovak (regional minorities)
- **Cadastre**: **Földhivatal Online** (citizen) + **E-ING** (elektronikus ingatlan-nyilvántartás, phased rollout) + **TAKARNET** (B2B professional)
  - Földhivatal Online: `https://www.foldhivatal.hu/` — citizen login via KAÜ (central government identification); E-ING procedures via `https://landing.eing.foldhivatal.hu` (KAÜ login)
  - TAKARNET: `https://www.takarnet.hu/` — registered users (banks, notaries, law firms, municipalities, tax authority); live since 14 Apr 2003; since 1 Sep 2025 title-sheet (tulajdoni lap) copies are issued through E-ING, while TakarNet serves e-certified map copies and land-use sheets (2026 data, source takarnet.hu + foldhivatal.hu)
- **Identifier**: **helyrajzi szám (HRSZ)** — topographical lot number; unique parcel ID
- **Tulajdoni lap** = title deed extract (the document buyers/lawyers always pull)
- **Unified cadastre + legal data since 1971** (egységes ingatlan-nyilvántartási rendszer)
- **Ownership types**: tulajdon (full), közös tulajdon (co-ownership), albérlet (sublet)
- **EU member since 2004**; **HUF currency** (NOT in eurozone)

## Section: `--price`

### Primary sources

- **KSH (Központi Statisztikai Hivatal)**: `https://www.ksh.hu/` — official price index (STADAT 18.2.1.1 quarterly index; 18.1.2.9 average price per m² by region and settlement type)
- **Ingatlan.com aggregated data** widely cited in KSH commentary
- **MNB (Magyar Nemzeti Bank)** Housing Market Report: `https://www.mnb.hu/`
- **Pannonland, Investropa** — secondary aggregators

### Listing platforms

- **Ingatlan.com** — DOMINANT (primary source for benchmarks)
- **Otthonterkep.hu** — significant secondary
- **Otthonajánló**, **Ingatlannet** — niche

### 2025 price benchmarks (KSH annual averages, 2025)

| Region | HUF/m² (2025 avg) | EUR-equivalent (366.43 HUF/EUR) |
|---|---:|---:|
| **Budapest — used homes, all types** | 1,194,000 | ~€3,258 |
| **Budapest — used, multi-unit buildings (többlakásos)** | 1,258,000 | ~€3,433 |
| **Budapest — used, housing estates (lakótelep)** | 1,119,000 | ~€3,054 |
| **Budapest — new homes** | 1,610,000 | ~€4,394 |
| **County seats, Észak-Alföld (incl. Debrecen) — used** | 738,000 | ~€2,014 |
| **County seats, Dél-Alföld (incl. Szeged) — used** | 707,000 | ~€1,929 |
| **County seats, Nyugat-Dunántúl (incl. Győr) — used** | 743,000 | ~€2,028 |
| **County seats, Dél-Dunántúl (incl. Pécs) — used** | 658,000 | ~€1,796 |
| **All county seats — used** | 689,000 | ~€1,880 |
| **National avg** | 625,000 (used) / 1,293,000 (new) | ~€1,706 / ~€3,529 |

(2025 data, source KSH STADAT 18.1.2.9 + 18.1.2.12 + 18.1.1.14, `https://www.ksh.hu/stadat_files/lak/hu/lak0025.csv`; EUR computed at the ECB reference rate of 22 Oct 2026.) The county-seat rows are regional aggregates of three county seats each, not city-level prices. KSH combined house-price index: 106.3 in Q2 2026 against 96.5 in Q2 2025 (2025 = 100), computed +10.2% y/y (2026 data, source KSH STADAT 18.2.1.1, `https://www.ksh.hu/stadat_files/lak/hu/lak0029.csv`).

District and city levels below are est. Their source is not traced and they do not match the KSH tables above, so verify against ingatlan.com listings or KSH settlement data. Calibration, computed against the KSH 2025 used-home averages above: the city rows sit 14–35% above their region's county-seat average (Győr and Pécs +14%, Szeged +27% to +34%, Debrecen +35%). The Budapest district rows span −13% to +19% around the Budapest multi-unit average of 1,258,000 (Buda Hills: +19% or more).

| Area | HUF/m² (est.) | EUR-equivalent (est., ~395 HUF/EUR) |
|---|---:|---:|
| **Buda Hills (II, XII, III)** | ~1,500,000+ | ~€3,800+ |
| **Other Buda (XI, XXII)** | ~1,300,000 | ~€3,300 |
| **Budapest VI (Terézváros)** | ~1,200,000–1,500,000 | ~€3,000–€3,800 |
| **Pest inner districts (V, VI, VII, VIII, IX)** | ~1,100,000–1,400,000 | ~€2,800–€3,500 |
| **Debrecen** | ~998,000 (resale) / ~1,070,000 (brick) | ~€2,500–€2,700 |
| **Szeged** | ~900,000–950,000 | ~€2,300–€2,400 |
| **Győr** | ~850,000 | ~€2,150 |
| **Pécs** | ~750,000 | ~€1,900 |

### Compute

1. HUF/m² = price / **lakóterület** (residential area)
2. **Convert HUF to EUR** at current FX (HUF volatile)
3. **Cross-check** Ingatlan.com asking prices + KSH transaction data
4. **Buda Hills premium** factor 1.5-2× over outer Pest districts

### Key terms

- HRSZ = helyrajzi szám (topographical lot number)
- Tulajdoni lap = title deed extract
- Társasház = condominium / multi-unit residential
- Kataszter = cadastre
- Energetikai tanúsítvány = energy certificate

---

## Section: `--traffic`

### Sources

- **Magyar Közút (NIF Zrt.)**: `https://kozut.hu/` — state roads
- **Önkormányzati közlekedési adatok**: per local authority
- **BKK** (Budapesti Közlekedési Központ — Budapest transit organiser): `https://bkk.hu/`
- **Budapest Közút Zrt.**: `https://budapestkozut.hu/` — operates and maintains the capital-owned roads and handles traffic engineering across all of Budapest (nearly 5,000 km city road network), incl. traffic-counting cameras (2026 data, source budapestkozut.hu; 2026-10-23 verified)

### Key term

**ÁNF (Átlagos napi forgalom)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–30,000 v/d (Budapest arterials, M-roads)
- 🔴 > 30,000 v/d (M0 ring, Üllői út, Hungária körút)

---

## Section: `--tax`

### Annual property taxes — local

#### Építményadó (Building tax)

- **Local — set per municipality**
- Statutory maximum 2026: **3,059 HUF/m²/yr** (Htv. cap valorised by CPI; 2025 maximum 2,950) (2026 data, source Budapest IV district tax-rate proposal pkb-2025-11-27 + Budapest XIII decree 22/2025 (XI.11.) justification)
- Budapest XIII 2026: **3,059 HUF/m²** (2025: 2,950) — but a flat owned by a private individual is exempt except for floor area used for business (e.g. short-term letting), and any building of a private owner over 65 is exempt (decree 52/2011 (XII.16.) § 2, text in force from 1 Jan 2026, net.jogtar.hu)
- Many districts charge **0 for primary residences**

#### Telekadó (Land tax)

- **Local — set per municipality**
- Budapest XIII 2026: **556 HUF/m²** (decree 53/2011 (XII.16.) § 2 (3) a), text in force from 1 Jan 2026, net.jogtar.hu); a plot with a building on it is exempt when the owner is a private individual, unless the building serves the business of a vállalkozó (sole trader, company — Htv. 52. § 26.) (decree § 2 (1)); otherwise the plot part equal in size to the useful floor area of the building on it is exempt (Htv. 19. § a), per budapest13.hu)
- Statutory maximum 2026: **556 HUF/m²/yr** (556.2) (2026 data, source Budapest IV district tax-rate proposal pkb-2025-11-27)
- Wide variance by district / municipality

#### Other local taxes on property

- **Magánszemélyek kommunális adója** (communal tax on private owners, per property): set per municipality; statutory maximum 2026 **HUF 47,279 per property (adótárgy)** (2026 data, source Budapest IV district tax-rate proposal pkb-2025-11-27)
- **Települési adó** (settlement tax that some municipalities levied): **abolished from 1 Jan 2027** by Act XXXV of 2026 (2026 data, source NAV notice 2026-07-31, `https://nav.gov.hu/sajtoszoba/hirek/Matol_tobb_ado-_es_vamszabaly_valtozik`)

#### Typical annual tax bills

| Property | Annual (HUF) | EUR |
|---|---:|---:|
| Budapest XIII 80m² flat, private owner, own home (2026) | 0 (exempt) | 0 |
| Budapest XIII 80m² flat, private owner, used for accommodation services, e.g. short-term let (80 × 3,059, 2026) | 244,720 | ~€668 |
| Budapest XIII 80m² house owned by a company or sole trader (vállalkozó) + 250m² plot (building 80 × 3,059; land (250 − 80) × 556, 2026) | 244,720 + 94,520 = 339,240 | ~€926 |
| Debrecen 100m² | 80,000–150,000 | €200–€380 |

*Budapest XIII rows: rates from the district decrees in force in 2026, EUR at the ECB reference rate 366.43 HUF/EUR (22 Oct 2026). Debrecen row: source not stated — verify with Debrecen önkormányzat; rates/figures may have changed since.*

### Transaction taxes

#### Visszterhes vagyonátruházási illeték (transfer tax)

- **4%** of market value (standard)
- **2%** on the part of the market value above HUF 1bn per property
- Capped: HUF **200M per property**
- **First-home reduction**: a buyer under 35 acquiring a first home gets **up to 50%** off if the whole property is worth ≤ HUF 15M; first home = never owned a dwelling, a share of 50% or more in one, or a registered right over one (Itv. 26. § (6), (9))
- **New home bought from the developer**: exempt up to HUF 15M market value; up to HUF 30M only the duty on the part above HUF 15M is payable where the buyer does not prove the sale of another home (Itv. 26. § (1) f))
- **Home swap**: an individual who sells another home within 5 years before or 1 year after the purchase pays duty only on the difference in market values (Itv. 21. § (2) b))
- **Exempt**: home purchases made with the family home-creation allowance (CSOK) or a CSOK Plusz loan (Itv. 26. § (1a) f))
- *(2026 data, source Itv. (Act XCIII of 1990) consolidated text in force from 1 Oct 2026, net.jogtar.hu)*

### VAT (ÁFA)

- **27% standard** (highest in EU)
- **Reduced 5% on new homes** (new flat ≤150 m² in a multi-unit building / new single-dwelling house ≤300 m², Áfa tv. Annex 3 Part I rows 50–51) — the rows lapse on **31 Dec 2026**; supplies in **2027–2030** keep 5% only if the building permit became final by 31 Dec 2026, a simple notification was filed by 30 Sep 2024 (Étv.), or a simple notification under the Hungarian Architecture Act was acknowledged by 31 Dec 2026 (Áfa tv. 371. §, text in force from 1 Jan 2027) (2026 data, source Áfa tv. consolidated texts, net.jogtar.hu)
- **ANNOUNCED, NOT LEGISLATED**: in the 2027 budget speech to Parliament on 19 Oct 2026 the PM said the 5% new-home rate stays in 2027 (secondary: telex.hu 19 Oct 2026) — check the 2027 budget and tax bills before relying on it

### Capital gains (PIT)

- **15%** flat (Szja tv. 8. § (1))
- **5-year holding schedule** — one schedule for all real estate (Szja tv. 62. § (4)); taxable share of the computed gain: **100%** in the year of acquisition and the following year, **90%** in the 2nd year after the year of acquisition, **60%** in the 3rd, **30%** in the 4th, **0%** from the 5th; if the acquisition cost cannot be established, taxable income = 25% of the proceeds (62. § (3)) (2026 data, source Szja tv. (Act CXVII of 1995) consolidated text in force from 1 Oct 2026, net.jogtar.hu)

### Rental income — private accommodation (STR)

- **Fizetővendéglátó tételes átalányadó** (Szja tv. 57/A. § (4)): **HUF 150,000/habitable room/yr** in Budapest — the only settlement over the 2m guest-night trigger — and **HUF 38,400/room/yr** in every other settlement; raised from 38,400 on 1 Jan 2025, both rates unchanged for tax year 2026. Full conditions + NAV list timing in `--rental` (2026-08-07 verified, source: NAV)

### Total transaction cost (buyer side)

- Standard resale: ~5-6% (4% transfer + 1-2% legal/lawyer)
- First-home (under-35, ≤15M HUF): ~3-4% (transfer duty down to 2% + others)
- New build from the developer: price includes VAT (5% while the reduced rate applies); transfer duty 0 up to HUF 15M, reduced up to HUF 30M, full 4% above — est. ~2% other costs below HUF 15M, ~5–6% in total above HUF 30M (computed from the rates above)

### Future risk

- 5% new-home VAT lapses on 31 Dec 2026 under current law (to 2030 only for permits final / notifications acknowledged by then); a 2027 continuation was announced on 19 Oct 2026 but is not legislated
- **Wealth tax (vagyonadó) — PROPOSED, NOT ENACTED**: the Ministry of Finance published a draft act for public consultation on 6 Oct 2026 (closed 14 Oct 2026). Draft terms: annual tax on a person's net wealth above **HUF 1bn** (one allowance per person, spouses separately) at **1%** up to HUF 100bn and **1.5%** above; status taken on 31 Dec, self-assessed return and payment by 31 Aug of the following year. **Non-residents** are taxed only on Hungarian real estate, rights over or linked to it, shares in companies formed under Hungarian law and shares in companies holding Hungarian real estate (draft § 4 (2)); deductible debts include loans for acquiring, building or improving taxable assets. Hungarian property is valued by transaction value (or its indexed value where the act allows), the NAV national mass-valuation model, or an independent valuer; the summary names no main-residence exemption. NAV may grant deferral or instalments for liquidity hardship — normally up to 12 months, up to 24 months especially for housing property or company shares. Draft entry into force 15 Dec 2026, first status date 31 Dec 2026, first return and payment by 31 Aug 2027 (2026 data, source kormany.hu consultation page + MoF content summary and draft text, `https://kormany.hu/dokumentumtar/tarsadalmi-egyeztetes-a-vagyonadorol-szolo-torvenyjavaslatrol`). No parliamentary bill number (T/…) found as of 2026-10-23 — confirm the enacted text in Magyar Közlöny before relying on these figures
- Currency volatility (HUF can swing 10-20% vs EUR)

---

## Section: `--rental`

### Long-term residential

- **Lakástörvény** (Housing Act) — moderate tenant protection
- Standard 1-3 yr contracts
- **Bérleti szerződés** must be notarized for >1 year if applicable

### Short-let (Airbnb, Booking)

- **Registration**: a private host notifies the local **jegyző** (kereskedelmi hatóság), who registers the unit and issues a certificate showing the accommodation type; the host requests a tax number from NAV on form T101 (co-owners: T201), because commercial accommodation is a VAT-taxable service (2026 data, source NAV information booklet 10, published 2026-02-03)
- **Budapest VI District (Terézváros)**: **BAN on STRs from 1 January 2026** (decree 26/2024 (X.31.) after a two-week resident vote from 2 Sep 2024, held online or in person (telex.hu, secondary): 20.52% turnout, 54% for the ban (hvg.hu, secondary); the Kúria rejected the government office's challenge in Köf.5.023/2025/4, Nov 2025 (THT, secondary)) — enforcement live since Jan 2026 (Terézváros + police + NAV inspections; fines up to several million HUF); only hotels, guesthouses, and community accommodations may operate legally
- **Budapest VII District (Erzsébetváros)** — stage 1: building decree **33/2025 (IX.24)** (amends 25/2018 XII.21), in force **25 Sept 2025**, caps NEW commercial accommodation at **10% of a building's residential floor area**, ground-floor only, rooms min 8 m² single / 12 m² double / +4 m² per extra bed, en-suite bathroom (WC, washbasin, shower) per room, panzió only with ≥6 rooms + breakfast room; the decree has no transitional clause — per THT (secondary) it applies to new authorisation procedures, so operating units may continue
- **Budapest VII District** — stage 2: decree **46/2025 (XII.10)** sets STR usable days/yr to **ZERO from 1 Jan 2026** unless a **társasház** (condominium) agreement exists (then 365) — units registered by 31 Dec 2025 must file the agreement by 31 Dec 2026 (same zero-day mechanism as District VI, with a condo-consent carve-out)
- **Budapest city-wide STR/NTAK registration moratorium 1 Jan 2025 – 31 Dec 2026** (a national Act whose scope is limited to Budapest's administrative area — not a municipal decree) — the commercial authority may not register any new magánszálláshely or egyéb szálláshely (Kertv. 11/H (1), inserted by Act LVI of 2024, in force 1 Jan 2025), except where the classification request was filed by 31 Dec 2024 (11/H (2)); for units registered by 31 Dec 2024 a change of operator cannot be registered until 31 Dec 2026 (11/H (3)), so a buyer of a registered Budapest STR unit cannot be registered as its operator before 1 Jan 2027; **expires 31 Dec 2026 — the consolidated Kertv. text on njt.hu still says 31 Dec 2026 (read 2026-10-23); unless Parliament amends 11/H, registrations reopen 1 Jan 2027 subject to district rules. Host associations (MAKE) asked for a one-year extension on 11 Sep 2026; the MTÜ said its review is ongoing, and no decision or bill was reported (turizmus.com, secondary) — watch**
- **Other districts (checked 2026-10-23; VIII, XIII and I re-checked 2026-10-28)**: no zero-day rule adopted outside VI and VII; District I has a draft.
  - **District V (Belváros-Lipótváros)**: building code 6/2020 (I.30.) §75(3) and §76(4) cap accommodation units in existing residential buildings at **5% of the building's independent units** in the mixed city-centre zones. This is a cap, not a ban (source belvaros-lipotvaros.hu).
  - **District VIII (Józsefváros)**: concept adopted 25 Jun 2026. STRs are capped at **3.5% of the district's housing stock**; the district paper puts the current share at 3.52%, so in practice there would be no net new units. Sub-district caps run from 1% to 5% (5% in Palotanegyed and Corvin). The per-building cap is **15%**, cut from the concept's 20% in the JÓKÉSZ 4th amendment, and new units need condominium consent. The JÓKÉSZ amendment went to partnership consultation 7–19 Sep 2026, and a separate STR decree is still required. That decree (condominium consent, in a draft titled for nem lakás célú helyiségek, i.e. non-residential premises, in condominiums; consent presumed for units registered before 1 Jan 2027 but revocable by the condominium) was tabled for the 24 Sep 2026 council meeting and withdrawn by its proposers, and it was not on the 22 Oct 2026 agenda; the withdrawn proposal expected the KÉSZ amendment at the November 2026 meeting. Planned entry into force is 1 Jan 2027. PROPOSED, not yet adopted (source jozsefvaros.hu + Józsefvárosi Újság; meeting pages checked 2026-10-28).
  - **District XIII**: a draft decree would allow STRs only where the condominium or cooperative general assembly consents by resolution. The draft is published and survey responses are being processed; the district counts 1,100–1,200 STR flats (source budapest13.hu).
  - **District I (Budavár)**: after a non-binding online poll (58.6% of 4,503 respondents for a full ban), the municipality published a draft zero-day decree for 15-day consultation on 22 Oct 2026. STR usable days would be **0** district-wide from 1 Jan 2027, with exceptions: Várnegyed (Castle District) units registered by 31 Dec 2026 keep 365 days until 31 Dec 2027 only; outside the Várnegyed, units in non-condominium buildings keep 365 days, and units in condominium-type buildings registered by 31 Dec 2026 keep 365 days until 31 Dec 2027 and from 1 Jan 2028 only once condominium consent is filed with the jegyző. The draft gives units registered from 2027 in condominium-type buildings no exception. Fines HUF 200,000 (natural person / sole trader) or HUF 2,000,000 (legal person) plus a 45-day closure. Council decision expected in November 2026. PROPOSED, not yet adopted (source budavar.hu draft decree, 22 Oct 2026).
  - Revisit 2026-12-15 for the VIII, XIII and I decrees.
- STR stock grew **+80% Budapest 2020-2024**; **>hotel rooms** in city
- **Kata — check before relying on it for STR income**: kata (Kata tv., 2022. évi XIII. törvény) is open only to full-time (főfoglalkozású) sole traders. NAV ends kata status from the day before any revenue from real-estate letting, or from a kifizető (payer, incl. a foreign payer; taxi services excepted), is received. The tax is HUF 50,000/month tételes adó, plus a 40% különadó on kisadózói revenue above HUF 18M/yr. Confirm with NAV or an adótanácsadó before treating platform-paid STR income as kata revenue (2026 data, source NAV information booklet 99, published 2026-02-20)
- **Fizetővendéglátó tételes átalányadó** (itemised flat-rate tax on private accommodation, Szja tv. 57/A. § (4)) — **HUF 150,000 per habitable room per year** in settlements whose guest-nights exceeded **2 million in the second year before the tax year**; **HUF 38,400/room/yr everywhere else**. **Budapest is the only settlement on that list** (guest-nights above 2m in both 2023 and 2024). Rate rose 38,400 → 150,000 on **1 Jan 2025** (+290.6%) — NOT a 2024 change (NAV's 2024 information booklet still stated a flat HUF 38,400/room nationwide); both rates unchanged for tax year 2026. NAV republishes the qualifying-settlement list **by 31 January each year** — check it before assuming the low rate (2026-10-23 verified, source: NAV information booklet 10 published 2026-02-03 + NAV notice 2025-01-17, `https://nav.gov.hu/ado/szja/A_fizetovendeglatokat_erinto_valtozasok`)
- *Short-let rules re-verified 2026-10-23: Kertv. 11/H via njt.hu + belvaros-lipotvaros.hu; Terézváros 26/2024 + Kúria Köf.5.023/2025/4 via THT; Erzsébetváros 46/2025 via net.jogtar.hu; Józsefváros via jozsefvaros.hu; District XIII via budapest13.hu; registration + fizetővendéglátó tételes átalányadó via NAV information booklet 10. Erzsébetváros 33/2025 last re-verified 2026-07-02 (net.jogtar.hu). District I draft decree via budavar.hu, Józsefváros council pages via jozsefvaros.hu and District XIII via budapest13.hu re-checked 2026-10-28*

---

## Section: `--work=<profession>`

### Sources

- **NFSZ (Nemzeti Foglalkoztatási Szolgálat)**: `https://nfsz.munka.hu/`
- **Profession.hu** — biggest: `https://www.profession.hu/`
- **Jobline.hu**, **Karrier.hu**, **LinkedIn HU**

### Self-employment

- **EV (Egyéni vállalkozó)** = sole trader
- **Kft. (Korlátolt felelősségű társaság)** = limited; **min HUF 3M törzstőke**, each member's törzsbetét min HUF 100,000 (Ptk. 3:161 (1) and (4); 2026 data, source njt.hu, 2013. évi V. törvény)
- **ÁFA** alanyi adómentesség (small-business VAT exemption) threshold: **HUF 20M** annual domestic sales in 2026 (HUF 18M in 2025, HUF 12M in 2024); scheduled **HUF 22M in 2027** and **HUF 24M in 2028**; new electors must declare to NAV by 31 Dec (2026 data, source NAV press release 2025-12-10, `https://nav.gov.hu/sajtoszoba/hirek/Jo_hir_a_kkv-knak_tovabb_emelkedik_az_alanyi_adomentesseg_hatara`)
- **Kata** (Kata tv., 2022. évi XIII. törvény): HUF 50,000/month tételes adó for full-time (főfoglalkozású) sole traders; 40% különadó on kisadózói revenue above HUF 18M/yr (HUF 1.5M per taxed month if kata does not cover the whole year). Kata status ends on revenue from a kifizető (business payer, incl. a foreign payer; taxi services excepted) or from real-estate letting, so the limit is on who pays, not on a list of occupations (2026 data, source NAV information booklet 99, published 2026-02-20)

### Salary benchmarks (KSH)

- **National, full-time employees, 2025**: gross **median HUF 565,238/month** (~€1,543); gross **average HUF 705,014/month** (~€1,924) (2025 data, source KSH STADAT 20.1.1.39, `https://www.ksh.hu/stadat_files/mun/hu/mun0046.csv`)
- **Average gross by county of the employer's registered seat** (county level, not city level; multi-site employers are counted where they are registered):
  - Budapest: HUF 851,211 in 2025 (~€2,323); HUF 943,294 in H1 2026
  - Győr-Moson-Sopron (Győr): HUF 737,115; Hajdú-Bihar (Debrecen): HUF 620,449; Csongrád-Csanád (Szeged): HUF 612,368; Baranya (Pécs): HUF 607,525 (all 2025)
  - National: HUF 705,014 in 2025; HUF 772,751 in H1 2026
  - (2026 data, source KSH STADAT 20.2.2.9, `https://www.ksh.hu/stadat_files/mun/hu/mun0206.html`, updated 2026-08-27; EUR at the ECB reference rate of 366.43 HUF, 22 Oct 2026)
- **Minimum wage (minimálbér, from 1 Jan 2026)**: **HUF 322,800/month gross** (+11.0% vs HUF 290,800 in 2025; ~€881 at 366.43 HUF/EUR); guaranteed minimum wage (garantált bérminimum, skilled/diploma): **HUF 373,200/month gross** (~€1,018) (2026 data, source KSH STADAT 20.1.1.62, `https://www.ksh.hu/stadat_files/mun/hu/mun0190.html`, updated 2026-02-27)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **HungaroMet Nonprofit Zrt.** (took over the tasks of OMSZ, which was dissolved without legal successor on 31 Dec 2023 — 547/2023. (XII. 12.) Korm. rendelet 13. § (1)) | `https://www.met.hu/` · climate portal: `https://eghajlat.met.hu/` | Weather, climate observations + projections (2026 data, source net.jogtar.hu 547/2023 + met.hu; 2026-10-23 verified) |
| **OVF (Országos Vízügyi Főigazgatóság)** | `https://www.ovf.hu/` · flood hazard + risk maps (ÁKK 2nd review): `https://vizeink.hu/terkepek-es-tovabbi-kapcsolodo-dokumentumok/` · drought index: `https://aszalymonitoring.vizugy.hu/` | Water management, **flood maps**, drought monitoring (HDI index, 133 stations) (2026 data, source ovf.hu + vizeink.hu; 2026-10-23 verified) |
| **SZTFH Földtani Szolgálat** (successor to MBFSZ / MFGI / ELGI / MÁFI) | `https://sztfh.hu/tevekenysegek/foldtani-tevekenyseg` · maps: `https://map.hugeo.hu` | Geology, geophysics, hydrogeology; GeoBank borehole database (2026 data, source sztfh.hu; 2026-09-18 verified) |
| **VÁTI** ❌ DEPRECATED — dead on 2026-10-23 (vati.hu does not resolve; www.vati.hu refuses connections); verify with **Lechner Tudásközpont** (runs TeIR; regional-planning unit) | `https://lechnerkozpont.hu/` | Spatial planning |
| **HUN-REN Kövesligethy Radó Seismological Observatory** | `https://seismology.hu/` | Seismicity, historic damaging quakes, felt-quake reports (2026 data, source seismology.hu; 2026-10-23 verified) |

### Specific risks

- **Flood** — major risk:
  - **25% of national territory exposed to flood hazard** (undated, source OVF — vizugy.hu Árvízi direktíva page; 2026-10-23 verified); ármentesített (flood-protected) area **2,057 thousand ha** ≈ 22% of the 93,025 km² territory (computed: 20,570 ÷ 93,025) (2025 data, source KSH STADAT 15.1.1.40 + 8.1.1.1) — national figures, not a parcel-level claim; check the parcel on the OVF flood maps
  - **2,148,000 residents** in protected floodplains would be exposed without defence works; modelled property risk without defence HUF 606bn/yr (2025-corrected, source OVF ÁKK 2nd review 'Védett árterek kockázati statisztikai értékelése', dated 2026-01-14)
  - **Tisza + Duna + Tisza-Maros** primary
  - "Icy flood" (early spring) + "green flood" (early summer)
  - **4,484 km** árvízvédelmi fővédvonal (main flood-defence line) (2025 data, source KSH STADAT 15.1.1.40)
  - Tisza 2000 catastrophic flood; Tisza record at Szeged **1,009 cm on 21 Apr 2006** (source vizugy.hu OVF Tisza page); Duna June 2013 flood wave (Budapest)
- **Drought**: Great Plain (Alföld) — OVF reports drought frequency and intensity rising in measured values and long-term forecasts; live HDI drought index from 133 monitoring stations at `https://aszalymonitoring.vizugy.hu/` (2026 data, source ovf.hu Vízhiány elleni védekezés; 2026-10-23 verified)
- **Heat waves**: increasing — the national-average annual count of forró napok (Tmax ≥35 °C) rose by 3 and of fagyos napok (frost days) fell by 22 over the 124-year homogenised record (source HungaroMet, eghajlat.met.hu adatsorok elemzése; 2026-10-23 verified)
- **Earthquake**: Carpathian Basin seismicity moderate overall, lower in the inner (Hungarian) Pannonian Basin than at the basin margins; more active zones Komárom–Mór–Berhida, Eger, Kecskemét, Dunaharaszti, Jászság, Békés; largest recorded Komárom 1763 (est. M6.1 on the observatory's seismicity page; its past-quakes list gives M6.2 and also carries an uncertain Savaria 455 event, M6.6?); damaging M5.5–6 events statistically every 40–50 years, moderate-damage events every 15–20 years; most recent entry in the observatory's past-quakes list: Tenk 2013 (M4.8, building damage over HUF 600M); soft sediments + high groundwater amplify shaking (source HUN-REN Kövesligethy Radó Seismological Observatory, seismology.hu; 2026-10-23 verified)
- **Storm**: derecho 2022 (Budapest)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead paint, asbestos cement starts |
| **1900–1990 (Soviet/communist era)** | Asbestos common; dated heating; panel buildings (panelház) |
| **Panelház 1960s–1980s** | ~800k units; energy-inefficient; gradual refurbishment |
| **1990s–2000s** | Improving insulation |
| **Post-2008** | Modern energy code |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetikai tanúsítvány** (energy certificate) | Required for sale or lease of an existing building / unit (176/2008. (VI. 30.) Korm. rendelet 1. § (3) b)); for a unit's lease only where the lease was signed after 31 Dec 2015 (12. § (1)); mandatory for sales since 2012 (start year not re-verified — verify at net.jogtar.hu); seller shows it by contract signing and hands it over by handover (3. § (3)); energy class must appear in sale / rental ads (3. § (2a)) | **5 years** (8. § (1); shortened from 10 years by 200/2023. (V. 25.) Korm. rendelet with effect from 1 Nov 2023); if requirement values or the classification method change, an older certificate serves a sale / lease only until the 60th day after the change (8. § (2)) — term of certificates issued before 1 Nov 2023 not verified, check with the issuing tanúsító (2026 data, source net.jogtar.hu consolidated 176/2008, time-state from 2026-01-06; 2026-10-23 verified) |
| **Tulajdoni lap** | Title deed extract | Current |
| **Lawyer-countersigned deed** (ügyvédi ellenjegyzés) or notarial deed (közokirat) | Required for land-registry registration — a private deed qualifies only if countersigned by a lawyer or in-house counsel of a Hungarian regional bar (Inytv. = 2021. évi C. tv. 35. § (2); main provisions in force since 15 Jan 2025 per 92. § (2)) (2026 data, source net.jogtar.hu consolidated Inytv., time-state from 2026-10-01; 2026-10-23 verified) | At sale |

### Climate change projections

- **Summer warming** in HungaroMet's regional climate-model runs (SRES A1B + pessimistic RCP8.5): national average **+1.3–2.2 °C for 2021–2050** and **more than +4 °C** in the last decades of the century (source HungaroMet, met.hu klímamodellezés — modellkísérletek; 2026-10-23 verified)
- **Observed**: Budapest annual mean temperature **+1.7 °C** over its 124-year homogenised record (90% CI 1.4–2.1 °C) (source HungaroMet, eghajlat.met.hu; 2026-10-23 verified)
- **Reduced summer precipitation** (Pannonian basin drying) — summer decrease statistically significant by century-end in two of the runs; more autumn + winter precipitation, especially in the south (same HungaroMet source)
- **More frequent heatwaves**: hőségnapok (Tmax ≥30 °C) **+20 to +50 days/yr** by 2071–2100 vs 1971–2000 in all three HungaroMet simulations (source HungaroMet, met.hu klímamodellezés — éghajlati szélsőségek)
- **Tisza valley**: increasing flood frequency
- **Continental climate intensification**

---

## Section: `--mains`

### Sources

- **Víziközmű-szolgáltatók** — regional or municipal water + sewer operators (OVF list of 41), e.g. **Fővárosi Vízművek Zrt.** (Budapest water) + **Fővárosi Csatornázási Művek Zrt.** (Budapest sewer), **Debreceni Vízmű Zrt.**, DMRV, ALFÖLDVÍZ (source vizugy.hu Víziközmű üzemeltetők list, page © 2013–2021 — rates/figures may have changed since; named Budapest + Debrecen operators' sites live, 2026-10-23 verified)
- Sewer connection: **84.6% of population** connected to urban wastewater collecting systems (2024 data, source Eurostat env_ww_con, updated 2026-09-18); lower in villages
- Rural: **szippantós (cesspit)** common — **8.7% of population** relies on storage tanks emptied by truck to treatment plants (2024 data, source Eurostat env_ww_con, IND_TANK)

### Costs

| Scenario | Cost (HUF) |
|---|---:|
| Mains connection | 800,000–2,500,000 |
| Septic upgrade | 1,500,000–4,000,000 |
| Bored well | 1,500,000–3,500,000 |

---

## Cost benchmarks (HU 2026)

| Work | Cost (HUF) |
|---|---:|
| Energetikai tanúsítvány | 50,000–150,000 |
| Lawyer (ügyvéd) | 0.5–1% of price |
| Visszterhes illeték (transfer tax) | 4% (2% on the part above HUF 1bn; max HUF 200M per property) |
| Realtor commission | 3% (~paid by seller) |
| **Total transaction cost (buyer)** | **~5–6%** of price |
| Roof renovation | 3,000,000–8,000,000 |
| Asbestos abatement | 500,000–3,000,000 |
| Energy retrofit (Class E → A) | 8,000,000–20,000,000 |
| Panelház refurbishment | 5,000,000–12,000,000 (per unit) |
| Heat pump | 2,500,000–5,000,000 |
| Solar PV (5kW) | 1,800,000–3,500,000 |

## Active fiscal incentives (2025-2026)

- **Otthon Start Program** (Korm. rendelet 227/2025. (VII. 31.), applications from 1 Sep 2025): interest capped at **3%**, loan up to **HUF 50M**, term up to **25 years**, **10% minimum down payment** (unless extra collateral); price caps **HUF 100M flat / HUF 150M single-dwelling house** and **HUF 1.5M per m²**; a **2-year eligibility period** of Hungarian social-security insurance (or listed equivalents); applicants aged 18+ who are Hungarian citizens, EU/EEA nationals exercising residence in Hungary beyond 3 months, or third-country nationals with long-term residence status. **Not strictly first-time buyers**: no own dwelling in a built-up area (belterület) in the past 10 years, but earlier ownership of a share worth ≤ HUF 15M, or of at most a 50% share in one dwelling at a time, does not disqualify (§ 4); a state mortgage (for 20% of the loan) with a ban on sale and encumbrance is registered for 5 years after the loan contract (purchase) or the occupancy permit (build) (§ 9) (2026 data, source decree consolidated text in force from 6 Mar 2026, net.jogtar.hu)
- **Wekerle Plusz — ANNOUNCED, NOT LEGISLATED**: in the 2027 budget speech to Parliament on 19 Oct 2026 the PM said Wekerle Plusz replaces Otthon Start in 2027 — ages 18–41, fixed **3% for new homes / 5% for used homes**, a 5-year duty to move in and live there, and no share of 50% or more in another property for the applicant or spouse; Otthon Start contracts already signed stay valid. Loan cap, term, price limits, launch date and the Otthon Start closing date are not published, and no decree exists as of 2026-10-23 (secondary: telex.hu 19 Oct 2026) — check Magyar Közlöny
- **CSOK Plusz** (Korm. rendelet 518/2023. (XI. 30.)): subsidised loan for married couples (wife under 41, with pregnancy / adoption exceptions) at max **3%** during the subsidy period, up to **HUF 15M / 30M / 50M** by existing and committed children, plus a **HUF 10M non-refundable child-bearing support** for the second and each later child born or adopted after the application; purchases with the loan are exempt from transfer duty (2026 data, source decree consolidated text in force from 6 Mar 2026 + Itv. 26. § (1a) f), net.jogtar.hu)
- **5% VAT on new homes** to 31 Dec 2026; 2027–2030 only where the building permit became final or a simple notification was acknowledged by 31 Dec 2026 (Áfa tv. 371. §); a 2027 continuation was announced on 19 Oct 2026, not yet legislated — see `--tax`
- **Rezsicsökkentés** (utility cost cap): below-market household gas + electricity prices — the 19 Oct 2026 budget speech said its rules stay unchanged in 2027 (secondary: telex.hu, announcement)
- Bankmonitor forecasts 15-20% price rise in 2026 driven by Otthon Start

## Common listing platforms

- **Ingatlan.com** — DOMINANT
- **Otthonterkep.hu** — secondary
- **Otthonajánló**, **Ingatlannet** — niche

## Caveats unique to HU

- **Currency: HUF** (volatile vs EUR; can swing 10-20%) — material for non-HUF buyers
- **27% VAT** (highest in EU) — but new homes 5% to 31 Dec 2026, then to 2030 only for permits final by 31 Dec 2026 (2027 continuation announced, not legislated)
- **Otthon Start Program** (1 Sep 2025) — 3% capped-rate mortgage causing market distortion; price caps HUF 100M flat / HUF 150M house / HUF 1.5M per m²; replacement by Wekerle Plusz in 2027 announced on 19 Oct 2026, not yet legislated
- **Terézváros (Budapest VI) STR ban from 1 Jan 2026** — first major Hungarian STR ban
- **Other Budapest districts**: VII has a zero-day rule unless the condominium agrees (see `--rental`). V, VIII and XIII, checked 2026-10-23 (VIII and XIII again 2026-10-28), have caps or rules in preparation rather than bans: V caps accommodation units at 5% of a building's units in its mixed city-centre zones (KÉSZ 6/2020 (I.30.) §75(3), §76(4); source belvaros-lipotvaros.hu); VIII plans caps from 1 Jan 2027 (source jozsefvaros.hu consultation + infostart.hu, secondary); XIII has a draft decree allowing STRs only with condominium general-assembly consent (source budapest13.hu). I published a draft zero-day decree on 22 Oct 2026: 0 days district-wide from 1 Jan 2027 except in non-condominium buildings outside the Várnegyed; units registered by 31 Dec 2026 keep 365 days to the end of 2027, then none in the Várnegyed and, in condominium-type buildings elsewhere, only with condominium consent; PROPOSED, council vote expected November 2026 (source budavar.hu; see `--rental`)
- **Földforgalmi törvény** (Land Transfer Act):
  - Non-EU/EEA natural persons **prohibited** from acquiring agricultural land; legal persons too, save statutory exceptions (Földforgalmi tv. 9. § (1))
  - Hungarian and EU/EEA citizens who are not registered farmers (földműves) are capped at **1 ha** total holding, close relatives of the seller excepted (10. § (2)-(3)); registered farmers (agricultural qualification, or failing that at least 3 years of farming in Hungary on their own account) may hold up to **300 ha** (16. § (1)); every buyer pledges to farm the land personally and keep it in agricultural use for **5 years** (13. § (1)) (2025 data, source Act CXXII of 2013 consolidated text in force from 24 Dec 2025, net.jogtar.hu)
- **Non-agricultural property bought by a foreign (külföldi) natural or legal person** needs a permit from the capital / county government office (fővárosi és vármegyei kormányhivatal) where the property lies; statutory processing time 45 days; refused where public or municipal interest is harmed — since 3 Jan 2026 that includes ignoring the pre-emption tools of a local identity-protection decree (Korm. rendelet 251/2014. (X. 2.) §§ 2-6, text in force from 3 Jan 2026, net.jogtar.hu); whether an EU/EEA national needs the permit is not stated in the decree — verify with the kormányhivatal
- **Local identity protection (Act XLVIII of 2025, text in force from 1 Jul 2025)**: a municipality may by decree create a **pre-emption right** on sales to a 'betelepülő' (a natural person with no property, residence or stay address in the settlement) — ranked the municipality first, then the owner of an adjoining plot, then a property owner in the settlement (the last two only with title held for at least 5 years) — exercisable within 30 days; it may also restrict registering a residence there. Check the settlement's decree before signing (2025 data, source Act XLVIII of 2025 §§ 7-9, net.jogtar.hu)
- **Wealth tax (vagyonadó) draft** — HUF 1bn net-wealth allowance, 1% / 1.5%, non-residents taxed on Hungarian real estate; PROPOSED, NOT ENACTED — see `--tax` Future risk
- **Panelház** (~800k units) energy-inefficient Soviet-era panel buildings
- **Tisza + Duna flood risk** — 25% of national territory on floodplain
- **Capital gains 15% PIT** with 5-year holding schedule (taxable share 100% / 100% / 90% / 60% / 30% / 0% from the acquisition year on, Szja tv. 62. § (4))
- **First-home reduction**: under-35 first-home buyer + property ≤15M HUF = up to 50% transfer duty reduction (Itv. 26. § (6))
- **Visszterhes illeték cap**: HUF 200M per property
- **Társasház** (condominium) financial health critical
- **Földforgalmi törvény** amended by Act XCVII of 2025 (in force 24 Dec 2025): pre-emption procedure (incl. municipal pre-emption under the 2025 Local Identity Protection Act), lease (haszonbérlet) approval and rice-farm (rizstelep) lease rules; the consolidated text carries a further change in force from 15 Jan 2027 (2025 data, source Act CXXII of 2013 consolidated text and amendment notes, net.jogtar.hu)
- **Otthon Start is not strictly first-time-buyer** — prior owners of a share worth ≤ HUF 15M, or of at most a 50% share in one dwelling, still qualify (Korm. rendelet 227/2025. (VII. 31.) § 4); strong distortion expected on sub-HUF 50M stock
- **Buda Hills (II, XII)** premium 1.5-2× over outer Pest

## Reddit / forum sources

- **r/hungary** — biggest community
- **r/budapest**
- **r/PersonalFinanceHU** (smaller)
- **Hungarian Conservative**, **Daily News Hungary**, **Hungary Today** (English)
- **Portfolio.hu** (financial)

## Verification authorities

| Authority | When to call |
|---|---|
| **Földhivatal Online** (DÁP / Ügyfélkapu+ login) | Cadastral map copies, társasház (condominium) data, survey data |
| **E-ING** (e-land registry) + **TAKARNET** (B2B, via lawyer / bank) | Title verification — tulajdoni lap copies come from E-ING since 1 Sep 2025; TAKARNET keeps e-certified map + land-use sheet copies (2026 data, source takarnet.hu + foldhivatal.hu; 2026-10-23 verified) |
| **NAV (tax authority)** | Transfer tax + PIT |
| **Local önkormányzat** | Építményadó + telekadó rates + permits |
| **Ügyvéd** (lawyer) or **közjegyző** (notary) — registration needs a lawyer-countersigned or notarial deed (Inytv. 35. § (2)) | Closing process |
| **Társasházi képviselő** | If apartment |
| **OVF** + the regional **vízügyi igazgatóság** (12 VIZIG directorates) | Flood risk, dyke status, drought |
| **HUN-REN Kövesligethy Radó Seismological Observatory** | Seismic history of the locality |

## Source URL templates

| Source | URL pattern |
|---|---|
| Földhivatali Portál (Földhivatal Online) | `https://www.foldhivatal.hu/` |
| E-ING (tulajdoni lap, e-land registry) | `https://landing.eing.foldhivatal.hu/` |
| TAKARNET | `https://www.takarnet.hu/` |
| KSH | `https://www.ksh.hu/` |
| Ingatlan.com | `https://ingatlan.com/` |
| MNB | `https://www.mnb.hu/` |
| HungaroMet (took over OMSZ tasks 1 Jan 2024) | `https://www.met.hu/` |
| OVF | `https://www.ovf.hu/` |
| SZTFH Földtani Szolgálat (ex-MBFSZ) | `https://sztfh.hu/tevekenysegek/foldtani-tevekenyseg` |
| NAV (tax) | `https://nav.gov.hu/` |
| Magyar Közút (traffic) | `https://kozut.hu/` |
| Budapest Közút (Budapest city roads) | `https://budapestkozut.hu/` |
| OVF flood hazard + risk maps | `https://vizeink.hu/terkepek-es-tovabbi-kapcsolodo-dokumentumok/` |
| KSH flood-defence table (15.1.1.40) | `https://www.ksh.hu/stadat_files/kor/hu/kor0040.html` |
| HUN-REN seismology | `https://seismology.hu/` |
| Eurostat wastewater connection (env_ww_con) | `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_ww_con?geo=HU` |

## Status

✅ **Fully populated** as of 2026-04-25 (geological-survey body (SZTFH Foldtani Szolgalat) corrected 2026-09-18 per sztfh.hu). Rental tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (KSH + Ingatlan.com + MNB), traffic (Magyar Közút), tax (építményadó + telekadó local + 4% transfer + 27% VAT (5% new) + 15% CGT 5-yr exempt + fizetővendéglátó tételes átalányadó), rental (Terézváros STR ban from 1 Jan 2026), work, risks (flood 25% territory + drought + Soviet-era panelház), mains all have primary government sources.
**Confidence**: HIGH for items re-read against statute, decree or official statistics on 2026-10-23 — transfer duty (Itv.), 27% / 5% VAT and its 2027–2030 transition (Áfa tv.), CGT schedule (Szja tv. 62. §), Otthon Start + CSOK Plusz decree terms, Földforgalmi tv. limits + Act XCVII of 2025, the 251/2014 foreign-buyer permit, the Budapest registration moratorium (Kertv. 11/H), the Terézváros ban, the fizetővendéglátó rates, KSH 2025 price benchmarks + Q2 2026 index, ECB FX and the `--work` figures (Ptk., NAV, KSH); HIGH for the content of the draft wealth tax (MoF consultation text), which is PROPOSED, NOT ENACTED. MEDIUM for `--risks` + `--mains` (flood, climate, seismic and sewer figures re-sourced to OVF / HungaroMet / KSH / HUN-REN / Eurostat; panelház stock, derecho 2022, build-era and cost rows unsourced), District VIII / XIII / I STR rules (in preparation), whether EU/EEA nationals need the 251/2014 permit (not stated in the decree) and HUF FX volatility forecasts (rapidly changing). LOW for 2027 measures announced on 19 Oct 2026 but not legislated (Wekerle Plusz, 5% VAT continuation, rezsicsökkentés) and for untraced figures: district / city asking prices (est.), the Debrecen tax row, cost benchmarks, the Bankmonitor forecast, the Lakástörvény contract lines and STR-stock growth.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | Kft capital (Ptk. 3:161), AAM threshold HUF 20M (NAV), kata rules (NAV booklet 99), KSH earnings + 2026 minimum wages re-checked; job-board standing not verified |
| Caveats unique to HU (legal / fiscal items) | 2026-10-23 | 2026-10-23 refresh wave | VAT, Otthon Start, Földforgalmi tv. limits, Act XCVII of 2025, CGT, first-home duty and duty cap re-read on statute / decree texts; foreign-buyer permit (251/2014) + local identity-protection pre-emption added; FX, flood, panelház and Buda-premium items not re-verified |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | Földhivatal Online / E-ING / TAKARNET split, lawyer-or-notary rule (Inytv. 35. § (2)), OVF + VIZIG and seismology rows |

## Extension TODOs

- [ ] Per-district építményadó + telekadó rates table
- [ ] Otthon Start eligibility decision tree (first-time owner + SSN history)
- [ ] CSOK Plusz family home benefit eligibility
- [ ] Panelház refurbishment subsidy availability per district
- [ ] Föld Forgalmi Act non-EU agri-land prohibition flow
- [ ] Tisza + Duna flood zone overlay
- [ ] Társasház financial health rubric
- [ ] HUF FX hedging recommendation for non-HUF buyers
- [ ] Budapest district-by-district STR rules tracker (VI zero days; VII zero days without a társasház agreement; V 5% per-building cap; VIII / XIII / I rules pending — revisit 2026-12-15)
- [ ] Buda Hills vs Pest premium multiplier history

## Update history

- **2026-04-25** — Initial population
- **2026-05-27** — Tier-1 corrections: transfer duty, CGT schedule, ÁFA threshold, 2026 minimum wage
- **2026-07-02** — Short-let rules re-verified (Erzsébetváros decrees 33/2025 + 46/2025)
- **2026-08-07** — Fizetővendéglátó tételes átalányadó re-verified (NAV)
- **2026-09-18** — Geological-survey body corrected to SZTFH Földtani Szolgálat (sztfh.hu)
- **2026-10-21** — Rental tracker entries re-checked (December regulatory-watch wave, run early)
- **2026-10-23** — Refresh wave; counts are changed / confirmed / not verified. Status date kept at 2026-04-25 because `--price`, `--tax`, `--rental`, `--risks` and `--mains` still carry unverified items.
  - Country profile 4 / 2 / 5 — settlements 3,155 (KSH, 1 Jan 2026); EUR/HUF 366.43 (ECB, 22 Oct 2026) with its 12-month range; cadastre access via E-ING (title-sheet copies since 1 Sep 2025) + KAÜ login. Postcodes, 23 districts and "since 1971" not verified
  - `--price` 4 / 0 / 11 — benchmarks replaced with KSH 2025 annual averages + Q2 2026 index (+10.2% y/y); eight district / city rows untraced, kept and labelled est.; Buda Hills factor, MNB report and ingatlan.com ranking not verified
  - `--rental` 8 / 6 / 6 — registration route (jegyző + NAV T101); Terézváros vote + Kúria Köf.5.023/2025/4; moratorium restated as national law (Kertv. 11/H) incl. the operator-change bar and the 1 Jan 2027 reopening; districts V, VIII, XIII and I added; kata framing corrected. Lakástörvény lines, District VI fine levels and STR-stock growth not verified
  - `--work` 3 / 3 / 2 — Kft capital (Ptk. 3:161), AAM threshold HUF 20M in 2026 (NAV), kata rules (NAV booklet 99), KSH median / average earnings, 2026 minimum wages (KSH)
  - `--tax` 15 / 6 / 3 — 2026 local-tax maxima + Budapest XIII rates and exemptions; communal tax and settlement-tax abolition from 2027 added; transfer-duty detail (Itv.); 5% VAT lapse on 31 Dec 2026 with the 2027–2030 transition; single 5-year CGT schedule; draft wealth tax added (PROPOSED, NOT ENACTED). Debrecen row, "many districts charge 0", "highest in EU" and lawyer 1–2% not verified
  - `--traffic` 1 / 1 / 5 — Budapest Közút added; kozut.hu unreachable, so the NIF label, ÁNF term and road examples are not verified
  - `--risks` 13 / 3 / 10 — OMSZ replaced by HungaroMet; OVF flood + drought map links; VÁTI deprecated; flood exposure restated with OVF / KSH figures; main flood-defence line 4,484 km; Szeged 2006 record; earthquake rewritten (HUN-REN); energy-certificate validity 10 → 5 years; Inytv. 35. § (2) countersignature; HungaroMet climate projections. Tisza 2000, icy / green floods, derecho 2022, panelház ~800k and build-era rows not verified
  - `--mains` 3 / 0 / 3 — operators per the OVF list; sewer connection 84.6% + cesspit 8.7% (Eurostat 2024); cost rows unsourced
  - Cost benchmarks 0 / 1 / 10 — transfer-duty cap added; market cost rows unsourced
  - Active fiscal incentives 5 / 6 / 1 — Otthon Start + CSOK Plusz decree terms; Wekerle Plusz, the 2027 VAT continuation and rezsicsökkentés marked announced, not legislated; Bankmonitor forecast not verified
  - Caveats unique to HU 8 / 3 / 1 (legal / fiscal items) — VAT, Otthon Start, Földforgalmi tv. limits, Act XCVII of 2025, CGT, first-home duty; foreign-buyer permit (251/2014), local identity-protection pre-emption + wealth-tax pointer added; other-districts STR caveat and the district item under Extension TODOs corrected (V has a 5% per-building cap, not a ban)
  - Verification authorities 4 / 1 / 2; Source URL templates 3 / 6 / 1 (E-ING, HungaroMet, Budapest Közút + citation sources added; kozut.hu unreachable); foreign-buyer rules 0 / 5 / 1 (EU/EEA permit question open); listing platforms and forum sources: liveness only, no change
