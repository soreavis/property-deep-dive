# Greece 🇬🇷 — Property Due-Diligence Playbook

ISO2: `gr`. Status: ✅ Fully populated (researched 2026-04; **Tier-A quarterly refresh 2026-07-03** — fast-moving claims re-verified, structural sections unchanged).

## Country profile

- **Postcode**: 5 digits (`105 57` Athens centro, `546 24` Thessaloniki, `711 10` Heraklion)
- **Admin levels**: 13 περιφέρειες (regions) + 332 δήμοι (municipalities) + 122 περιφερειακές ενότητες (regional units)
- **Currency**: EUR (€) — adopted 2002
- **Languages**: Greek (official); English widely used in tourism/business
- **Cadastre**: **Ktimatologio (Hellenic Cadastre, Ελληνικό Κτηματολόγιο)**: `https://www.ktimatologio.gov.gr/` — parcel-based system with **KAEK unique parcel numbers**
- **Identifier**: KAEK (12-digit cadastral ID per parcel)
- **Ownership types**:
  - **Πλήρης κυριότητα** (full ownership)
  - **Ψιλή κυριότητα + επικαρπία** (bare ownership + usufruct)
  - **Συγκυριότητα** (co-ownership)
  - **Διαμέρισμα + κοινόχρηστα** (apartment + commons)

## Section: `--price`

### Primary sources

- **Ktimatologio (Hellenic Cadastre)**: `https://www.ktimatologio.gov.gr/`
  - **Status (2025-2026)**: 60% complete; full activation slipped from Nov 2025 to **2026**
  - 201 of 392 legacy mortgage offices closed in 2024
  - Free 24-hr search of registered parcels
  - Buyer requests **Apospasma Ktimatologikou Diagrammatos** (cadastral excerpt) + **Ktimatologiko Fyllo** (property sheet)
- **gov.gr digital property registry** (launched 2025): `https://www.gov.gr/en/ipiresies/periousia-kai-phorologia/ktematographese`
  - Integrates cadastre + tax + utility + forestry + energy data
- **Bank of Greece RPPI** (the authoritative price index): `https://www.bankofgreece.gr/en/statistics/real-estate-market`
  - Quarterly index built from ~951k bank valuations
  - **Q4 2025**: apartments +7.6% YoY (Athens +5.9%, Thessaloniki +8.0%, other cities +10.5%, other areas +8.6%; new apts +7.4%, old +7.8%); full-year 2025 avg +7.8% vs +9.1% in 2024 (Bank of Greece press release 19 Mar 2026; 2026-07-03 verified)
- **ELSTAT (Hellenic Statistical Authority)**: `https://www.statistics.gr` — building permits, construction cost
- **Hellenic Land Registry** for legacy mortgage records (where cadastre not yet operational)

### Listing platforms

- **Spitogatos.gr** — DOMINANT (consolidated Spitogatos + Spiti24 + Tospitimou + HomeGreekHome): `https://www.spitogatos.gr/en`
  - Has price index by area at /property-index
- **XE.gr** — second major aggregator: `https://www.xe.gr/property`
- **Indomio.gr**: `https://www.indomio.gr/`
- **Goldenhome.gr**: `https://www.goldenhome.gr/`
- **Plot.gr**, **Remax.gr**

### 2025 price benchmarks (Bank of Greece + Spitogatos)

| Region | Avg €/m² (apt) | Avg total (single-family) |
|---|---:|---:|
| **Athens centro (Plaka, Syntagma, Kolonaki)** | 3,500–6,000+ | 400,000–1,200,000+ |
| **Athens northern suburbs (Kifissia, Marousi)** | 2,800–4,500 | 380,000–800,000 |
| **Athens southern suburbs (Glyfada, Voula)** | 3,200–5,500 | 420,000–950,000 |
| **Athens western suburbs** | 1,500–2,500 | 180,000–350,000 |
| **Thessaloniki centro** | 1,800–2,800 | 200,000–400,000 |
| **Thessaloniki suburbs** | 1,500–2,200 | 180,000–320,000 |
| **Patras** | 1,200–1,800 | 130,000–250,000 |
| **Crete (Heraklion / Chania)** | 1,800–3,500 | 220,000–500,000 |
| **Mykonos / Santorini** | 5,000–15,000+ | 800,000–5,000,000+ |
| **Cyclades (other)** | 2,500–5,000 | 350,000–800,000 |
| **Rural Peloponnese / Epirus** | 800–1,500 | 100,000–250,000 |

### Compute

1. €/m² = price / **καθαρή ωφέλιμη επιφάνεια** (net usable area)
2. **Antikeimeniki Axia** (Objective Value) — official cadastral assessment, **frozen until 2027**
3. **Cross-check** Bank of Greece RPPI for area trend
4. **Settle objective value vs market**: market often 40-60% above objective

### Key terms

- KAEK = unique cadastral parcel number
- Antikeimeniki Axia = Objective (cadastral) Value
- Apospasma = cadastral excerpt
- Mihaniki Vevaiosi = engineer's statement
- PEA = energy certificate
- Authairesi = unauthorized construction

---

## Section: `--traffic`

### Sources

- **NEK** (Greek roads operator) for motorways
- **Hellenic Statistical Authority** for transport data
- **Ministry of Infrastructure** roads section
- **OpenStreetMap** + Google Maps Live for urban arterials

### Key term

**ΜΕΗΚ (Μέση Ετήσια Ημερήσια Κυκλοφορία)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (rural roads, small islands)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (Athens arterials, Egnatia)
- 🔴 > 35,000 v/d (Attiki Odos, Athens ring, Kifissou Avenue)

---

## Section: `--tax`

### Annual property tax — ENFIA

**Reformed annually since 2014; 2025-2026 reductions**:

#### ENFIA structure

- **Main ENFIA**: per m² × coefficients (location, age, floor, building type)
- **Supplementary ENFIA**: now charged only on companies and other legal entities — **5.5‰** of the value of their rights, **1‰** on property they use for their own business, and 3.5‰ on property not self-used by certain public-law and non-profit bodies (Property Tax Code ν.5219/2025 art. 12 par. 2). Individuals instead pay a **per-property value tax** of **0% up to €400k**, then **0.20%** (€400k–500k) rising by band to **1.00% above €2m**, only once their total property value exceeds **€300k**; out-of-plan land and certain listed buildings are outside it (art. 11 Section Γ). An individual's whole ENFIA is then **surcharged 5% / 10% / 15% / 20%** for a total value up to €650k / €800k / €1m / above €1m once the total exceeds **€500k** (art. 11 Section Ε), and **reduced by 30%** (total value ≤ €100k) **stepping down to 10%** (≤ €400k) (art. 13 par. 3) (2026 codified text, source [taxheaven Property Tax Code art. 11](https://www.taxheaven.gr/law/5219/2025/arthro/11) + [art. 12](https://www.taxheaven.gr/law/5219/2025/arthro/12) + [art. 13](https://www.taxheaven.gr/law/5219/2025/arthro/13); 2026-10-29 verified — the former '€200k individuals / €30k companies' thresholds are superseded)
- **Municipal levy (separate from ENFIA)**: ΤΑΠ, plus the ΦΗΧ on electricity bills, until 31 Dec 2026; from **1 Jan 2027** the **Τέλος Τοπικής Ανάπτυξης (ΤΤΑ)** replaces both — council-set 0.30‰–0.70‰ of the m² × zone price × age value, owed by the owner as of 1 January, collected on the electricity bill; a new owner declares to the municipality within one month (ENACTED, Ν.5314/2026 arts 392-396 + 448, ΦΕΚ Α΄ 103/29.06.2026; 2026-10-21 verified, source [ta.ypes.gov.gr codified Local Government Code](https://ta.ypes.gov.gr/vivlio-d/meros-b/kefalaio-d/arthro-393))

#### 2025-2026 reductions (CRITICAL)

- **Insured residences ≤ €500k taxable value**: **−20% ENFIA** (since 2025) — the home must be insured against **earthquake, fire and flood** for its full rebuild value (land excluded, at least €1,000/m²) with an insurer on the Bank of Greece register, for at least 3 months of the previous year, pro rata if under a year (Property Tax Code art. 10 par. 5; 2026-10-29 verified, source [taxheaven art. 10](https://www.taxheaven.gr/law/5219/2025/arthro/10))
- **Insured residences > €500k**: **−10%**
- **Villages ≤ 1,500 inhabitants**: **−50% ENFIA from 2026** (Law 5246/2025; main residence of GR tax residents, taxable value ≤ €400k; excludes Attica except the Islands regional unit; 1,700 threshold for West Macedonia, Evros and the border municipalities of Central Macedonia, East Macedonia-Thrace and Epirus) — **abolished entirely for these homes from 2027** (legislated in the same Law 5246/2025 art. 10, source minfin.gov.gr Property Tax Code codification); 90th TIF (Sept 2026) extension of the 2027 exemption to settlements up to 2,000 residents (2,200 West Macedonia) — PROPOSED, in a MinFin draft law in public consultation 18 Oct–1 Nov 2026 (draft Art. 15), not yet legislated; the draft drops Evros and the border municipalities from the higher tier, so they would fall under the general 2,000 and only West Macedonia keeps a higher limit (2,200); 1,500 / 1,700 stays in force until it is gazetted (2026-07-03 verified; 2027-exemption legal basis 2026-09-24 verified; 90th TIF limb 2026-10-28 verified, source [opengov.gr consultation text](https://opengov.gr/minfin/deliberations/enischysi-toy-diathesimoy-eisodimatos-tis-apotamieysis-kai-ton-ependyseon-forologikes-misthologikes/) + minfin.gov.gr press release 18 Oct 2026)
  - ~12,720 settlements affected (UNVERIFIED — no primary source re-read for this count in the 2026-10-29 pass)
- **Listed buildings**: the Property Tax Code's exemptions article (art. 10) lists no ENFIA exemption for them; listed monuments older than 100 years, and buildings listed as διατηρητέα by 31 Dec 2021 that predate 1 Jan 1940, are kept out of the per-property value tax and out of the total-value figure (art. 11 Section Γ par. 5(β)-(γ) and Section Ε par. 4) (2026 codified text, source [taxheaven art. 10](https://www.taxheaven.gr/law/5219/2025/arthro/10) + [art. 11](https://www.taxheaven.gr/law/5219/2025/arthro/11); 2026-10-29 verified — the former 'historic buildings ≤ €400k exempt' wording is not in the code)
- **Objective values frozen until 2027** — preserves base (UNVERIFIED — no primary source for a 2027 freeze date was found in the 2026-10-29 pass; check the zone price that applies on the date of the deed)

#### Illustrative ENFIA bills (est.)

> **est. — not a quote.** Ranges below are modelled from the Main ENFIA per-m² × coefficient structure (line 109) with the 2025-2026 reductions above applied; they are NOT sourced bills. Verify the exact figure on the [AADE myPROPERTY / ENFIA](https://www.aade.gr/) statement for the specific parcel.

| Property type | Illustrative annual ENFIA (est., 2025-2026 basis) |
|---|---:|
| Athens 80 m² apt (€150k objective) | ~€300–€600 |
| Athens villa (€500k objective) | ~€1,500–€3,500 |
| Cyclades vacation home (€350k) | ~€1,000–€2,500 |
| Rural village house (≤1,500 pop) | ~€100–€300 (reflects −50% village cut from 2026, line 116; abolished from 2027 — legislated, Law 5246/2025 art. 10) |

### Transaction taxes

- **Foros Metavivasis Akinitou (FMA)**: **3% + a 3% municipal surcharge on the tax = 3.09%** of taxable value on resale (Property Tax Code ν.5219/2025 art. 27 par. 1 «τρία τοις εκατό (3%) επί της φορολογητέας αξίας» + par. 5 «πρόσθετος φόρος τρία τοις εκατό (3%) υπέρ των Δήμων»; computed 3% × 1.03 = 3.09%; 2026-10-29 verified, source [taxheaven art. 27](https://www.taxheaven.gr/law/5219/2025/arthro/27))
  - **Watch — DRAFT BILL IN PUBLIC CONSULTATION, NOT LEGISLATED (90th-TIF bill, consultation 18 Oct–1 Nov 2026)**: FMA rises to **15% (15.45% with the municipal contribution)** from **1 Jul 2027** on the purchase of a **dwelling (κατοικία)** by a **natural person who is tax-resident outside the EU/EEA**; companies are outside the scope ([minfin.gov.gr press release 18 Oct 2026](https://minfin.gov.gr/anartithike-se-dimosia-diavoulefsi-to-nomoschedio-me-ta-metra-pou-anakoinothikan-stin-90i-diethni-ekthesi-thessalonikis-kai-efarmozontai-kata-ta-eti-2026-kai-2027/); rate per the MinFin 2027 draft State Budget, Oct 2026). The test is **tax residence, not citizenship**: the September announcement's citizenship / first-home-beneficiary wording is superseded. Draft Art. 16 ([opengov consultation text](https://opengov.gr/minfin/deliberations/enischysi-toy-diathesimoy-eisodimatos-tis-apotamieysis-kai-ton-ependyseon-forologikes-misthologikes/), read 2026-10-28) taxes a natural person who is tax-resident outside the EU/EEA when the tax liability arises, with no citizenship test and no carve-out for ομογενείς, long-term residents or Golden Visa buyers, so a Greek citizen or ομογενής tax-resident outside the EU/EEA would pay 15% and a non-EU national tax-resident in Greece or another EU/EEA state 3%. Draft Art. 48(8) applies it to final contracts drawn up from 1 Jul 2027 and says nothing about preliminary contracts signed earlier. It does not address [Property Tax Code art. 26 par. 1(a)](https://www.taxheaven.gr/law/5219/2025/arthro/26), under which a final contract signed within two years of a notarial preliminary contract is taxed at the rates in force when the preliminary was signed, so whether a notarial preliminary signed before 1 Jul 2027 keeps a non-EU/EEA-resident buyer at 3% is unresolved in the draft: flag it as an open question for the notary, not as settled either way. The wording can still change after the consultation. MinFin aims to legislate in November 2026; not tabled, voted or gazetted as of 2026-10-28. **The 3.09% above stays the current rate until an enacted change takes effect** — see shared/regulatory-watch.md 🇬🇷 GR.
- **VAT on new builds**: **24% statutory rate**, but **suspended through 31 Dec 2026** (Law 5246/2025 art. 12, gazetted 11 Nov 2025); **draft extension to 31 Dec 2027** in the 90th-TIF bill (public consultation 18 Oct–1 Nov 2026, not enacted — MinFin release 18 Oct 2026; DBP 2027)
  - During suspension, new builds attract 3.09% transfer tax instead
- **Notary fees**: ~1.0–1.5% sliding scale (est. — the statutory notary fee scale was not re-read in the 2026-10-29 pass; get the notary's written fee quote)
- **Lawyer fees**: ~1% (est.; recommended — no primary source found in the 2026-10-29 pass for a rule making a lawyer mandatory for non-residents, so treat that as unverified)
- **Realtor**: typically ~2% per side (buyer + seller) (est., market practice — no primary source re-read in the 2026-10-29 pass; confirm the fee in the brokerage agreement)
- **Ktimatologio registration fee** (on registering the deed): 0.5% + €20 in the legacy Μεταγραφών και Υποθηκών books, 0.6% + €20 where the deed goes into the operating-Cadastre book — KYA 2/12-1-2026, ΦΕΚ Β' 64/13-1-2026 art. 3 par. 4(α), (γ), (δ) («πέντε χιλιοστά (5 ‰)» of the value, «Πάγιο τέλος είκοσι (20) ευρώ», plus «ενός χιλιοστού (1‰)» in the art. 10 L.2664/1998 cadastral book); art. 3 par. 3 also lists a «πάγιο τέλος τριών (3) ευρώ» for registering a sale, and the decision does not say whether it stacks with the €20 — small, confirm with the notary (2026-10-29 verified against the [ΦΕΚ PDF](https://ia37rg02wpsa01.blob.core.windows.net/fek/02/2026/20260200064.pdf); see Cost benchmarks and shared/regulatory-watch.md 🇬🇷 GR)

### Total transaction cost (buyer side)

- Resale: ~6.6–8.2% of price (computed: 3.09% transfer + 1-1.5% notary + 1% lawyer + 2% realtor + 0.5-0.6% Ktimatologio registration fee = 7.59–8.19%, or 6.59–7.19% without a lawyer; plus €20 per registered deed) — watch, DRAFT BILL IN CONSULTATION, NOT LEGISLATED (90th-TIF bill, Oct 2026): for a natural person tax-resident outside the EU/EEA buying a home, from 1 Jul 2027 per the draft, computed 15.45% + 1–1.5% + 1% + 2% + 0.5–0.6% registration fee = 19.95–20.55% of price (see Transaction taxes)
- New build (during VAT suspension): same as resale ~6.6–8.2% (VAT-suspended new builds bear transfer tax instead of VAT, so the draft 15% FMA for buyers tax-resident outside the EU/EEA, from 1 Jul 2027, would reach them too — reading of the draft per secondary sources, verify in the enacted text)
- New build (post-VAT-suspension, from 1 Jan 2027 unless the drafted extension to 31 Dec 2027 is enacted): 24% VAT + others

### Capital gains

- **15% statutory rate** (Law 4172/2013)
- **Suspended through 31 Dec 2026** (ΚΦΕ art. 72 par. 33a as amended by L.5162/2024 art. 90, source [stegasi.gov.gr](https://stegasi.gov.gr/programs/anastoli-epivolis-forou-yperaxias-apo-metavivasi-akiniton)); extension through 31 Dec 2027 drafted in the 90th-TIF bill (public consultation 18 Oct–1 Nov 2026), not enacted
- Caveat: if reclassified as "business activity" (intent, frequency, 3+ properties), normal income tax + VAT apply

### IRS / income tax on rental

- Long-term letting, and short-term letting of up to 2 properties: "income from immovable property" (15% / 25% / 35% / 45% bands from tax year 2026, breaks at €12k / €24k / €36k — ΚΦΕ art. 40 par. 4; 15% / 35% / 45% through 2025 — see Tax on rental). The 2-property limit is a short-term-letting rule only (ΚΦΕ art. 39Α par. 1)
- **Short-term letting of 3+ properties → business activity**: the income is business income (ΚΦΕ art. 39Α par. 1) and the letting is a VAT-able service at the 13% reduced rate (VAT Code ν.5144/2024 art. 11 par. 2(α) + Annex III B.5); offering any service beyond bed linen makes even 1-2 short-let properties business income. The 3-property test does not apply to long-term letting (2026 codified text, source [taxheaven ΚΦΕ art. 39Α](https://www.taxheaven.gr/law/4172/2013/arthro/39%CE%91) + [VAT Code art. 11](https://www.taxheaven.gr/law/5144/2024/arthro/11) + [Annex III](https://www.taxheaven.gr/law/5144/2024/arthro/74); 2026-10-29 verified — the rule is in the codified ΚΦΕ and VAT Code, not Law 5170/2025)

### VAT (FPA)

- 24% standard
- 13% reduced (food, tourist services)
- New residential property: 24% (suspended through 31 Dec 2026; 2027 extension drafted, not enacted)

### Future risk

- **VAT suspension expires 31 Dec 2026** unless extended again — an extension to 31 Dec 2027 is in the 90th-TIF draft bill (consultation 18 Oct–1 Nov 2026, vote targeted November 2026), not enacted
- **Capital gains 15% suspension expires 31 Dec 2026** unless the drafted extension to 31 Dec 2027 (90th-TIF bill, not enacted) is voted and gazetted
- **Antikeimeniki Axia frozen until 2027** — likely revaluation (UNVERIFIED — no primary source for a 2027 freeze date was found in the 2026-10-29 pass)
- **Cadastre full activation 2026** — affects title clarity

---

## Section: `--rental`

### Long-term residential

- **Civil Code Article 574** governs lease
- Long-term rental (>3 years): notarized strongly recommended
- Tenant moderate protection
- Rent caps in some Athens neighborhoods (proposed 2025-2026) (UNVERIFIED — no primary source found for any rent-cap proposal in the 2026-10-29 pass; treat as unconfirmed until a bill is published)

### Short-let (Airbnb / Vrachychronia Misthosi)

**MAJOR REFORMS 2024-2025**:

#### Athens license freeze

- **From 1 Jan 2025**: NO new STR licenses in **1st, 2nd, 3rd municipal districts of Athens** (Plaka, Syntagma, Monastiraki, Koukaki, Exarchia, Pangrati area)
- Existing licenses keep operating — **two-tier market**: properties without an AMA by 31 Dec 2024 cannot operate STR at all in 2025-2026; pre-2024-12-31 hosts continue
- **Extended through 31 Dec 2026** by KYA 225563 ΕΞ 2025 (ΦΕΚ Β' 7200/31-12-2025); the statute's own first sentence (L.4446/2016 art.111 par.2A) sets 1 Jan–31 Dec 2025, and L.5313/2026 art.5 (ΦΕΚ 102/Α/25-6-2026) deleted the old '31 Dec 2026' cap from the 5th sentence, so the par.8 joint ministerial decision may now extend the freeze with no statutory end date (2026 data, codified text via taxheaven + e-nomothesia). A further extension to **31 Dec 2027** (Athens 1st/2nd/3rd + Thessaloniki A' Community) was announced by the PM at the 90th TIF (Sep 2026, news-tier: [ot.gr 7 Sep 2026](https://www.ot.gr/2026/09/07/tourismos/airbnb-freno-sti-vraxyxronia-misthosi-kai-to-2027-oi-koftes)) and is listed as a planned 2027 measure ('και για το έτος 2027') in the MinFin 2027 draft State Budget and DBP 2027 (Oct 2026), but is not yet in force: it needs only a new par.8 joint ministerial decision (none found as of 2026-10-29 in an et.gr full-text search of 2026 ΦΕΚ Β for «Βραχυχρόνιας Διαμονής», whose newest hit is Β 6467/26.10.2026, an AADE filing-deadline decision; the 2026 KYA was gazetted on 31 Dec 2025), and none of the 48 articles of the 90th-TIF bill (in public consultation to 1 Nov 2026) extends the freeze or adds a short-term-letting restriction — Art. 13 par. 2 and Art. 14 mention short-term letting only in passing, in the long-let exemption's conditions and in the business-levy definition of a branch (opengov text read 2026-10-29)
- **Thessaloniki A' Municipal Community**: first-time AMA registration barred 1 Jul–31 Dec 2026, extendable by the same par.8 joint ministerial decision (L.5313/2026 art.5, new par.2B of L.4446/2016 art.111; fine 50% of STR income, min €20,000; repeat breach in the same tax year = rents collected, min €40,000) (2026 data, source L.5313/2026 via e-nomothesia.gr)
- **Under legal challenge — not settled**: STAMA Greece + a 3rd-district property owner filed a Council of State annulment petition against the extension (Mar 2026); no ruling found as of Oct 2026 (2026-10-21 searches, news-tier), outcome expected to set nationwide precedent (2026-07-02, news-tier: [eKathimerini](https://www.ekathimerini.com/economy/real-estate/1298502/) + [BnBNews](https://bnbnews.gr/en/legislation/36901/stama-appeal-council-of-state-athens-short-term-rentals))
- **Resale risk — AMA deleted on transfer** (ENACTED — L.5313/2026 art.5, new par.2Γ of L.4446/2016 art.111, ΦΕΚ 102/Α/25-6-2026: any inter-vivos transfer, onerous or gratuitous, of a property in the par.2A Athens / par.2B Thessaloniki zones deletes its AMA and bars re-registration while the first-registration freeze lasts; 2026 data, codified text via e-nomothesia.gr — confirm in the ΦΕΚ): in the restricted central zones, **selling / donating / parental-transferring** an AMA-carrying flat deletes its AMA, so the **new owner cannot operate it as an STR** — a "ready-Airbnb" flat's STR right does NOT pass to a buyer. Inheritance: the enacted par.2Γ covers inter-vivos transfers only, so inheritance is outside the deletion rule (the 26 Jan 2026 ANA report that inheritance also deletes the AMA is superseded; 23 Jun 2026 Greek City Times matches the enacted text). Measure contested by POMIDA + STAMA (2026-07-02, news-tier: [Greek City Times 23 Jun 2026](https://greekcitytimes.com/2026/06/23/airbnb-new-rules-greece-july-1-2026-short-term-rentals) + [GTP 15 Jun 2026](https://news.gtp.gr/2026/06/15/greeces-plan-to-remove-short-term-rental-registrations-after-property-transfers-sparks-reactions) + [GTP/ANA 26 Jan 2026](https://news.gtp.gr/2026/01/26/short-term-rentals-in-greece-new-restrictions-take-effect-in-2026))

#### Cyclades / oversaturated regions

- STR freeze reported (Sep 2025, news-tier) as planned for **5 additional regions**; only the Thessaloniki A' Community freeze has been enacted (L.5313/2026 art.5 par.2B, from 1 Jul 2026), and no first-registration freeze elsewhere is in enacted text as of 2026-10-21 (1 Oct 2025 is the start date of the national STR standards, Law 5170/2025)
- **Cyclades bed caps — now GAZETTED**: the **Special Spatial Framework for Tourism (EChP-T)** was enacted by JMD **ΥΠΕΝ/ΔΝΕΠ/89997/3071/2026, ΦΕΚ Δ' 658/07.08.2026**, signed Friday 7 Aug 2026. Caps on NEW tourist accommodation are confirmed (100 beds/unit on island Groups II and III; on islands, 100 beds for the first 16 στρ. plus 6 beds per στρ. above in category-A areas, up to the category-B maximum of 350) together with the **25 m coastal no-build**, which the ministry describes as directly applicable. Press framing of "up to 30% fewer beds" (Apr 2026) is **still news-tier and appears in no gazetted text** — do not quote it as a figure. The short-term-letting limb is **not self-executing**: the gazetted text sets the framework by which STR *may* be regulated, so there is still no live Mykonos/Santorini STR freeze. Pending: the SSFT action programme (art. 12 A.1 item 6) lists a legislative suspension of new AMA registrations for **newly built homes on category-(Ν) islands** (every island except Crete and Evia) — not in force, no enacting law as of 2026-10-21 (see shared/regulatory-watch.md 🇬🇷 GR)

#### Law 5170/2025 (effective 1 Oct 2025)

- STR ONLY in **main-use spaces** (χώροι κύριας χρήσης, L.4067/2012 art. 2 par. 95: bedrooms, living areas, kitchens, clear height at least 2.50 m — 2.40 m was the minimum before the New Building Regulation, per the circular's footnote) with natural light, ventilation and air conditioning, legal under a building permit or a regularisation; auxiliary spaces (corridors, sanitary rooms, plant rooms, storerooms, parking) do not qualify (L.5170/2025 art. 3 par. 1(α) + Min. Tourism circular 19231/19.09.2025; 2026-10-29 verified, source [taxheaven L.5170/2025 art. 3](https://www.taxheaven.gr/law/5170/2025/arthro/3) — replaces the 'primary use, not commercial, not basement' gloss, which neither text uses)
- **Converted homes — 5-year STR ban** (L.5322/2026 art. 56(2), ΦΕΚ Α' 117/24.07.2026, in force on publication; a separate law from L.5170/2025): a dwelling created through the new exceptional change-of-use-to-housing routes of art. 199 par. 3 (buildings inside a town plan or settlement converted regardless of land uses, incl. those with a building-terms derogation granted up to 31 Dec 2025) or par. 3A (lawfully existing out-of-plan buildings) of the Spatial Planning Code ν. 5306/2026 cannot be short-let for at least 5 years from completion of the conversion, so ask the seller of a recently converted unit for the change-of-use file before counting on STR income (2026 data, source [ΦΕΚ Α' 117/2026](https://ia37rg02wpsa01.blob.core.windows.net/fek/01/2026/20260100117.pdf))
- Mandatory (Law 5170/2025 **Art. 3**, ΦΕΚ Α' 6/20.01.2025, via [Min. Tourism circular 19231/19.09.2025](https://mintour.gov.gr/wp-content/uploads/2025/09/%CE%A86%CE%9B%CE%98465%CE%A7%CE%98%CE%9F-%CE%93%CE%9F7.pdf); 2026-07-02 verified): natural lighting, civil-liability insurance (Greek-licensed insurer), electrician safety declaration, fire extinguisher, smoke detectors, RCD/anti-electrocution relay, escape signage, pest-control + first-aid
- Fines: **€5,000** first breach → **€10,000** (double) if a new inspection within a year of the fine finds a breach → **€20,000** (four times the original) for each further breach; €5,000 also if inspectors are refused entry; collected under KEDE (L.5170/2025 art. 3 par. 5-6; 2026-10-29 verified, source [taxheaven L.5170/2025 art. 3](https://www.taxheaven.gr/law/5170/2025/arthro/3); earlier [GTP Headlines](https://news.gtp.gr/2025/09/25/greece-introduces-new-rules-for-short-term-rentals-from-october-1/), secondary)
- **AMA (Property Registration Number)** must be shown on every listing (L.4446/2016 art. 111 par. 2(β)); AADE may demand listing data from platforms (par. 7), and a host who breaches par. 2 or 8 pays 50% of the year's gross STR revenue, minimum €5,000 (par. 5(α)). Reports of platforms auto-deleting non-compliant listings are news-tier: art. 111 itself sets no delisting duty (2026-10-29 verified, source [taxheaven art. 111](https://www.taxheaven.gr/law/4446/2016/arthro/111))

#### AMA (Arithmos Mitroou Akiniton)

- Mandatory registration number per property
- Issued by AADE (tax authority)
- Required to advertise on Airbnb/Booking/Vrbo
- **EFKA + AADE cross-checks** since 2023

### Tax on rental

- 1-2 properties: real estate income — **2026 reform** (effective 1 Jan 2026): **15% to €12k / 25% to €24k / 35% to €36k / 45% over €36k** (Law 5246/2025 art. 8 added the 25% band; through tax year 2025 the scale was 15% to €12k / 35% to €35k / 45% over €35k; first applied in the returns filed from March 2027 for 2026 income) (2026-05-27 verified; bands re-verified 2026-10-29 against the codified ΚΦΕ art. 40 par. 4 — «0-12.000 15% · 12.000,01-24.000 25% · 24.000,01-36.000 35% · >36.000 45%» — primary source [taxheaven ΚΦΕ art. 40](https://www.taxheaven.gr/law/4172/2013/arthro/40); secondary: [Athens Times — 2026 Tax Reform](https://athens-times.com/rental-income-tax-enfia-tax-assumptions-and-benefits-for-uniformed-personnel-tax-bill-passed-what-it-includes/) + [PwC Tax Summaries Greece](https://taxsummaries.pwc.com/greece/individual/taxes-on-personal-income))
- Short-term letting of 3+ properties: business activity (13% VAT) — ΚΦΕ art. 39Α par. 1 + VAT Code art. 11 par. 2(α); long-term letting is not caught by the 3-property test (see IRS / income tax on rental)
- **Income-tax reduction for renovation spend** (ΚΦΕ art. 39Β): spending on the energy, functional or aesthetic upgrade of a building not in another upgrade programme cuts the income tax of the individual who pays for it, spread equally over 5 years, capped at €16,000 of spend in total, goods at most one third of the services counted, paid electronically; applies to spend in tax years 1 Jan 2020–31 Dec 2026 (L.4646/2019 art. 66 par. 14), with an extension to 31 Dec 2027 drafted in the 90th-TIF bill (Art. 18, public consultation 18 Oct–1 Nov 2026, not enacted) (2026-10-29 verified, source [taxheaven ΚΦΕ art. 39Β](https://www.taxheaven.gr/law/4172/2013/arthro/39%CE%92) + [opengov consultation, draft Art. 18](https://opengov.gr/minfin/deliberations/enischysi-toy-diathesimoy-eisodimatos-tis-apotamieysis-kai-ton-ependyseon-forologikes-misthologikes/))
- **STR statute spine**: L.4446/2016 Art. 111 (AMA registry foundation) → L.4174/2013 Art. 54A (fines) → L.5073/2023 (refinements) → L.5162/2024 art.29 (par.2A Athens 1st/2nd/3rd district first-registration freeze) → L.5170/2025 Art. 3 (national STR property standards) → KYA 225563 ΕΞ 2025 (ΦΕΚ Β' 7200/31-12-2025, freeze extended to 31 Dec 2026) → L.5313/2026 art.5 (par.2B Thessaloniki freeze, par.2Γ AMA deletion on transfer, open-ended par.8 KYA extension power) (2026-05-27 verified, source [AADE Article 111 of Law 4446/2016 PDF](https://www.aade.gr/sites/default/files/2024-09/Article%20111%20of%20Law%204446_2016%20updated%20by%205073_2023%20-%20relevant%20provisions.pdf))

---

## Section: `--work=<profession>`

### Sources

- **OAED / DYPA** (Greek labour ministry job platform)
- **kariera.gr**, **Skywalker.gr**, **JobFind.gr**
- **LinkedIn GR**

### Self-employment

- **Atomiki epicheirisi** (sole trader): EFKA registration
- **Eteria periorismenis efthynis (EPE)**: limited liability
- **VAT (FPA)**: from €10,000 turnover (most sectors)
- **Personal tax** (2026 reform, effective 1 Jan 2026): **9% / 20% / 26% / 34% / 39% / 44%** (new 39% band at €40-60k; pre-2026 was 9/22/28/36/44; under-25s now 0% to €20k) (2026-05-27 verified, source [TaxRavens Greece Personal Income Tax 2026](https://taxravens.com/en/blog/greece-personal-taxation) + [Immigrant Invest 2026 Tax Guide](https://immigrantinvest.com/blog/taxes-in-greece/))
- **EFKA contributions** mandatory

### Salary benchmarks (2025)

- Median monthly gross:
  - Athens: ~€1,300–€2,000
  - Thessaloniki: ~€1,200–€1,800
  - Smaller cities: ~€1,000–€1,500
- **Minimum wage**: **€920/mo gross** (14 payments; €1,073.33 on a 12-month basis), effective 1 Apr 2026 (Ministerial Decision 8934/27.3.2026, ΦΕΚ Β΄ 1759 — up from €880, +4.55%; blue-collar daily wage €39.30 → €41.09; source ypergasias.gov.gr); government-stated target €950 by 2027 (news-tier) (2026-07-03 verified)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **EPPO / OASP** (Οργανισμός Αντισεισμικού Σχεδιασμού & Προστασίας, Earthquake Planning & Protection Organization) | `https://oasp.gr` | Seismic policy; seismic codes (EAK-2000, Eurocodes, older codes: `https://oasp.gr/kanonismoi`); volcanic-hazard assessment for the Hellenic Volcanic Arc |
| **HSGME / ΕΑΓΜΕ** (Ελληνική Αρχή Γεωλογικών & Μεταλλευτικών Ερευνών, formerly IGME) — Hellenic Survey of Geology & Mineral Exploration | `https://www.eagme.gr/` | Geology, faults, **Hellenic DataBase of Active Faults (HeDBAF)**: `https://activefaults.eagme.gr/en/` |
| **Civil Protection** (Υπουργείο Κλιματικής Κρίσης και Πολιτικής Προστασίας, Ministry of Climate Crisis and Civil Protection) | `https://civilprotection.gov.gr/en/xartis` | **Daily fire risk forecast map** (Ημερήσιος Χάρτης Πρόβλεψης Κινδύνου Πυρκαγιάς) May–Oct; past maps: `https://civilprotection.gov.gr/arxeio-imerision-xartwn`. The site returns HTTP 403 to scripted requests and opens in a browser |
| **NOA** (National Observatory of Athens, Institute of Geodynamics) | `http://hl-ntwc.gein.noa.gr/en/` (HTTP only; the HTTPS address fails with a certificate-name mismatch, checked 2026-10-29) | **Tsunami warnings** (HL-NTWC, 24/7 since 28 Aug 2012), seismicity |
| **ISMOSAV / ΙΜΠΗΣ** (Ινστιτούτο Μελέτης και Παρακολούθησης του Ηφαιστείου Σαντορίνης, Institute for the Study and Monitoring of the Santorini Volcano; non-profit, founded 1995) | `https://ismosav.gr/en/home/` | Santorini volcano observatory and monitoring networks (seismic, geodetic, satellite, thermal, chemical) |
| **EYDAP** (Athens water) | `https://www.eydap.gr` | Water and sewerage, Attica (see `--mains`) |
| **EYATH** (Thessaloniki water) | `https://www.eyath.gr` | Water and sewerage, Thessaloniki (see `--mains`) |

### Specific risks

#### Seismic (HIGH)

- **Seismic zone map** (Χάρτης Ζωνών Σεισμικής Επικινδυνότητας) of the national seismic code **ΕΑΚ-2000**, revised by ΦΕΚ Β' 1154/12.08.2003: **3 zones** (the previous map had 4), design ground acceleration **A = 0.16g / 0.24g / 0.36g** for zones I / II / III. Its Table 2.1 assigns prefectures, and in many prefectures individual (pre-2011) municipalities and communities, to zones, e.g. Δ. Αθηναίων and Δ. Θεσσαλονίκης zone I, Δ. Θήρας (Santorini) zone II. **Eurocode 8** with its Greek National Annex has been approved as an alternative since ΦΕΚ Β' 1457/05.06.2014: the owner picks either the national codes or the Eurocodes and may not mix them (2003 / 2014 texts, source [OASP](https://oasp.gr/kanonismoi/ellinikos-antiseismikos-kanonismos-2000); 2026-10-29 verified)
  - Revision under way as of Oct 2023: on 25 Oct 2023 OASP requested a budget commitment to commission a roadmap for drafting and updating Greece's seismic hazard maps (the specifications stage of its hazard-map committee); later progress not confirmed. The "5 zones, PGA 0.13–0.37g" proposal is unverified — no primary source found 2026-10-29
- **Recent significant events**:
  - **Athens 1999** (7 Sep, Mw 6.0 per USGS, Parnitha / Fyli)
  - **Lefkada 2003 + 2015** (14 Aug 2003 Mw 6.3; 17 Nov 2015 Mw 6.5, USGS)
  - **Samos-Izmir 2020** (Mw 7.0, generated tsunami alert)
  - **Crete 2021** (27 Sep, Arkalochori area, Heraklion; Mw 6.0, USGS)
  - **Santorini swarm Jan-Feb 2025** — civil-protection state of emergency for the Municipality of Thera, declared 6 Feb 2025 by the Civil Protection Secretary General and in force 1 Feb–3 Mar 2025 (news-tier, state news agency: [ANA-MPA 6 Feb 2025](https://www.amna.gr/en/article/882226/State-of-emergency-declared-on-Santorini-due-to-earthquakes)); many residents and workers left the island (news-tier). Volcano monitoring is by OASP (with INGV) and ISMOSAV (the earlier "UNESCO-IOC monitoring" is withdrawn — no source located in the 2026-10-29 pass)

#### Volcanic — Hellenic Volcanic Arc

- **Methana, Milos, Santorini, Nisyros, Kolumbo** (submarine, 6.5 km offshore of Thera; its 1650 eruption caused a strong tsunami — ISMOSAV)
- **Santorini caldera** + **Kolumbo** monitored continuously (ISMOSAV networks; OASP and INGV installed a permanent CO2-flux station on Nea Kameni in Jun 2025). Last eruption Nea Kameni 1950; unrest 2011 and 2024–2025 (ISMOSAV)
- **2025 Santorini swarm**: state of emergency 1 Feb–3 Mar 2025 (see Seismic above); many left the island (news-tier)

#### Wildfire (CATASTROPHIC RISK)

- **Civil Protection daily fire risk map** May–Oct: `https://civilprotection.gov.gr/en/xartis`
- **Mati 2018** (23 Jul, Eastern Attica): 104 dead (news-tier, [Capital.gr 29 Apr 2024](https://www.capital.gr/english/3804425/six-out-of-21-defendants-found-guilty-in-deadly-mati-fire)); burnt area of the Mati fire **1,260 ha** per NOA's BEYOND centre (WorldView-3 mapping, 30 Jul 2018; [BEYOND newsletter](https://beyond-eocenter.eu/images/docs/Newsletters/BEYOND_Newsletter_electronic_v10.html)). The earlier 5,000 ha is withdrawn — no source located in the 2026-10-29 pass
- **Recent**: Rhodes 2023, Evia 2021, Attica 2024
- **Anti-nero programme** (forest-fire prevention, YPEN, RRF-funded "Greece 2.0", since 2022): by 26 Nov 2024 about 190,000 στρέμματα (≈19,000 ha, computed at 0.1 ha per στρέμμα) of forest had been cleared, forest roads on 309,000 στρ. and firebreaks on more than 53,000 στρ. were being improved and maintained, and 67,600 στρ. of new mixed firebreaks were being opened; 42 / 47 / 74 contracts signed under the Anti-nero 2022 / 2023 / 2024 rounds (2024 data, source [YPEN press release 26 Nov 2024](https://ypen.gov.gr/perissotera-apo-750-ekat-evro-gia-draseis-prostasias-ton-dason/) — figures may have changed since). The earlier "12,000 km … 39 plans" is withdrawn — no source located in the 2026-10-29 pass

#### Tsunami

- **HL-NTWC** (Hellenic National Tsunami Warning Centre, NOA): `http://hl-ntwc.gein.noa.gr/en/`
- One of four accredited Tsunami Service Providers in UNESCO-IOC's NEAMTWS (accredited 27 Jun 2017); sends warnings to the General Secretariat for Civil Protection 24/7 since 28 Aug 2012 (HL-NTWC)
- **High-risk zones**: Hellenic Arc (E and W), Aegean fault zones, Gulf of Corinth
- **Coastal Crete, Rhodes, Karpathos, Cyclades** flagged

#### Other risks

- **Floods**: Attica + Thessaloniki + Peloponnese; **EU Directive 2007/60/EC** Flood Risk Management Plans (Σχέδια Διαχείρισης Κινδύνων Πλημμύρας, ΣΔΚΠ): the 1st revision (2nd cycle) is approved for all 14 river-basin districts by ministerial decisions in ΦΕΚ Β' Apr–Jun 2025 (e.g. EL06 Attica ΦΕΚ Β' 2752/04.06.2025, EL10 Central Macedonia ΦΕΚ Β' 2480/21.05.2025); plans are reviewed every 6 years. Flood hazard and flood risk maps from the revision are on the geoportal `https://floods.ypeka.gr/geoportal/` (portal `https://floods.ypeka.gr/`; 2025 data, 2026-10-29 verified)
- **Soil erosion** + landslide: Pindos mountains, Peloponnese
- **Coastal erosion** + sea-level rise — major Greek islands
- **Air pollution**: Thessaloniki winter PM10 (wood burning ~70% — unverified, no primary or peer-reviewed source for that share found 2026-10-29); Athens nephos summer
- **Crime**: Hellenic Police (Ελληνική Αστυνομία) statistics page with annual statistical yearbooks (Στατιστικές επετηρίδες): `https://www.astynomia.gr/statistika-stoicheia/` (HTTP 403 to scripts, opens in a browser). No street-level crime map was found 2026-10-29

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1940s** | No DPC, lead, asbestos cement starts |
| **1950s-1980s "polykatoikia" boom** | Asbestos very common, weak seismic compliance, illegal additions (authairesia) |
| **Post-1985** | Supplementary seismic articles (1984) applied exclusively from 1985; not the first code — Greece's first national seismic code dates from 1959 (Β.Δ. 19.2.1959, ΦΕΚ Α' 36/1959) (OASP) |
| **Post-1995 / post-2001** | NEAK applied exclusively from 1995; EAK-2000 in force from 2001; new 3-zone hazard map from 2003 (ΦΕΚ Β' 1154/2003) (OASP) |
| **Post-2010 KENAK** | Energy efficiency required |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **PEA (Pistopoiitiko Energeiakis Apodosis)** | Energy certificate; issued for a sale or a new lease and handed to the buyer or tenant, and the energy class must appear in every sale or letting advert (L.4122/2013 art. 12 par. 1(γ)-(δ), 2 and 4); in place since 2010 per the playbook (start date not re-verified) | 10 years at most; ends early on a major renovation (L.4122/2013 art. 11 par. 6) |
| **Mihaniki Vevaiosi** (βεβαίωση μηχανικού, engineer's certificate) + owner's solemn declaration (υπεύθυνη δήλωση) | Required since Law 4014/2011; now art. 368 of the Spatial and Urban Planning Code ν. 5306/2026 (ΦΕΚ Α' 88/08.06.2026), which carries over art. 83 of L.4495/2017: attached to every inter-vivos deed transferring or creating a real right, after electronic filing that gives the property a unique number | Valid 2 months from signature (art. 368 par. 6) |
| **Topographic diagram** with EGSA '87 coordinates | Accompanies the engineer's certificate, tied to the state coordinate system (ν. 5306/2026 art. 368 par. 4); not needed e.g. for in-plan units with a horizontal-property deed or building permit made before L.4178/2013 (par. 5) | Per case |
| **ENFIA paid certificate** | Tax clearance | Annual |
| **ΤΑΠ / ΤΤΑ (municipal property levy)** | No clearance certificate since 13 Dec 2023 (art. 33 par. 1 Ν.5076/2023); the Cadastre notifies the municipality after registration, and levy owed up to the transfer date is borne by the seller (Ν.5314/2026 art. 392); ΤΑΠ until 31 Dec 2026, ΤΤΑ from 1 Jan 2027 | Not a deed document |
| **Authairesia** review (illegal construction regularization) | If applicable | Per case |

### Climate change projections

- +2.0–3.5 °C by 2050 (est. — unverified, no primary source found 2026-10-29; verify against the Bank of Greece Climate Change Impacts Study Committee report)
- Sea-level rise: +15–20 cm by mid-century and +20–80 cm by 2100 per the latest update of the Bank of Greece report "The Environmental, Economic and Social Impacts of Climate Change in Greece" (news-tier, [To Vima 14 Aug 2024](https://www.tovima.com/society/climate-change-hits-greek-economy-hard-severe-risks-ahead/); primary report not read). The earlier +20–60 cm is withdrawn — no source located in the 2026-10-29 pass
- More extreme heat events
- Increased wildfire risk + intensity
- Reduced water availability

---

## Section: `--mains`

### Sources

- **EYDAP** (Athens, Attica): `https://www.eydap.gr` — exclusive right to provide water and sewerage services until **31 Dec 2040** (L.4812/2021 art. 114 par. 1; EYDAP's EGM of 24 Dec 2021 ratified the board's authorisation to sign the renewal contract, ATHEX filing). **2026 household tariff** (ΦΕΚ Β' 7188/30-12-2025, in force 1 Jan 2026), €/m³ by monthly consumption: 0–5 m³ €0.35, 5–20 €0.64, 20–27 €1.83, 27–35 €2.56, over 35 €3.20 (minimum charge 2 m³/month); sewer-use charge 75% of the water value; fixed €2.00/month water (½"–¾" meter) + €1.00/month sewer; VAT 13% on water and the environmental fee, 24% on the fixed charges and the sewer-use charge (2026 data, source [EYDAP tariff](https://www.eydap.gr/CustomerSupport/normalrates/))
- **EYATH** (Thessaloniki): `https://www.eyath.gr` — household tariff for the 2025–2029 regulatory period (ΦΕΚ Β' 3555/18.06.2026), €/m³ by 4-month consumption: 0–10 m³ €0.49, 11–40 €0.706, 41–60 €0.813, 61–120 €1.343, 121–160 €3.890, 161 and over €4.74; sewer-use charge 80% of the water value; fixed €2.00/month water (½"–¾") + €1.00/month sewer; billed every 4 months (2026 data, source [EYATH tariff](https://www.eyath.gr/plirofories-gia-to-timologio/))
- **Elsewhere**: municipal **DEYA** (Demotiki Epicheirisi Hydreusis Apochetefsis) companies — the DEYA union ΕΔΕΥΑ says it represents 122 of the 126 DEYA operating outside Athens and Thessaloniki, covering 5,222,077 residents (undated ΕΔΕΥΑ profile page, read 2026-10-29: `https://www.edeya.gr/index.php/el/edeya/parousiasi/profile`); the earlier "~230 DEYA serving ~4M people" is withdrawn
- No single national database — must contact local DEYA or municipality
- **Regulator**: ΡΑΑΕΥ (Ρυθμιστική Αρχή Αποβλήτων, Ενέργειας και Υδάτων, Regulatory Authority for Waste, Energy and Water; formerly RAE): `https://www.raaey.gr/`. Its supplier-tariff comparison for household electricity and gas: `https://energycost.gr/`
- **Electricity grid connection**: HEDNO / ΔΕΔΔΗΕ (distribution network operator), online low-voltage connection application at `https://www.deddie.gr/en/`
- **Connectivity**: telecoms regulator EETT (`https://www.eett.gr/`); no EETT per-address coverage checker was found 2026-10-29, so check each provider's own address tool
- Rural / out-of-plan properties: cesspool/septic still common

### Verification

- Athens + Thessaloniki: universal mains
- Most provincial cities: DEYA mains
- Rural islands + remote: often **vothros** (cesspool); **mikros viologikos** (small biological treatment)

### Costs

| Scenario | Cost (€) |
|---|---:|
| EYDAP / DEYA connection | 605.68 for a standard EYDAP water connection (κοινή παροχή; €63.12 paid on application; EYDAP procedures page, read 2026-10-29); DEYA fees vary; the earlier 2,500–8,000 range is est. (no official source) |
| Mains-line extension | est. 8,000–25,000 (no official price source) |
| Vothros to compliant biological treatment | est. 4,000–10,000 (no official source) |

---

## Cost benchmarks (GR 2026)

| Work | Cost (€) |
|---|---:|
| PEA (energy cert) | 200–500 |
| Mihaniki Vevaiosi | 300–800 |
| Topographic diagram | 400–1,200 |
| Notary | ~1.0–1.5% of price (est. — see Transaction taxes) |
| Lawyer | ~1% (recommended) |
| Realtor | ~2% per side |
| Foros Metavivasis | 3.09% (watch, DRAFT BILL IN CONSULTATION, NOT LEGISLATED (90th-TIF bill, Oct 2026): 15.45% on a home bought by a natural person tax-resident outside the EU/EEA from 1 Jul 2027 per the draft — see Transaction taxes) |
| Ktimatologio registration fee (sale) | 0.6% + €20 where the deed goes into the operating-Cadastre book (0.5% + €20 in the legacy Μεταγραφών και Υποθηκών books) — KYA 2/12-1-2026, ΦΕΚ Β' 64/13-1-2026 |
| **Total transaction cost (resale, buyer)** | **~6.6–8.2%** of price (computed, incl. the registration fee — see Total transaction cost) |
| **Total transaction cost (new build during VAT suspension)** | **~6.6–8.2%** |
| Vothros to biological treatment | est. 4,000–10,000 (no official source; see `--mains`) |
| Antiseismic retrofit | est. 30,000–80,000 (no official source; scope depends on the engineer's assessment) |
| Authairesia legalization | varies by amnesty |
| Roof renovation | 8,000–25,000 |
| Energy retrofit (Class C → A) | 25,000–60,000 |

## Active fiscal incentives (2025-2026)

- **Exoikonomo (Saving)** programme: energy retrofit grants
- **Spiti Mou II** programme: co-financed first-home mortgage (RRF via Hellenic Development Bank) — ages 25-50; income ≥€10k, caps €25k single / €35k +€5k per child (couples) / €39k +€5k per child beyond first (single-parent); loan ≤€190k at ≤90% of price, 50% of the loan interest-free; eligible homes built pre-2008, ≤150 m², price ≤€250k, no letting for 7 years. **ENDED**: applications closed 31 May 2026; loans not signed by the 2 Jun 2026 RRF milestone could be signed until 31 Aug 2026 with HDB funds, and signing closed on 31 Aug 2026 with 14,114 loan contracts (€1.54bn) out of 15,097 approvals (€1.82bn) — no new applications or signings (2026-10-21 verified, source [minfin.gov.gr joint release 3 Sep 2026](https://minfin.gov.gr/epitychis-i-oloklirosi-tou-spiti-mou-ii-pano-apo-14-100-sybolites-mas-vrikan-stegi)). Successor **Spiti Mou III** — ANNOUNCED at the 90th TIF, not yet in force: €2bn via the HDB (€500m RRF loans + €500m HDB cash + €1bn banks), borrowers up to 55, property value up to €300k, loan up to €230k at ≤90% of value, start planned January 2027 (government 90th TIF timetable; terms restated in the MinFin 2027 draft State Budget); no implementing KYA as of 2026-10-21
- **VAT suspension on new builds** through 31 Dec 2026 (Law 5246/2025 art. 12; extension to 31 Dec 2027 drafted in the 90th-TIF bill, not enacted)
- **Capital gains suspension** through 31 Dec 2026 (L.5162/2024 art. 90; extension to 31 Dec 2027 drafted in the 90th-TIF bill, not enacted)
- **3-year income-tax exemption for long lets of previously empty homes** (ΚΦΕ art. 72 par. 91): rent from a home of up to 120 m² (+20 m² per dependent child of the tenant beyond two) is untaxed for the first 36 months of a lease of at least 3 years signed between 8 Sep 2024 and 31 Dec 2026, if the home was declared empty (or not declared as let, lived in, own-used or lent) in the 3 prior tax years, or was used only for short-term letting in the prior year; it lapses if the home is vacated or switched to short-term letting within the 3 years. Extension of the signing window to 31 Dec 2027 drafted in the 90th-TIF bill (Art. 13 par. 2, public consultation 18 Oct–1 Nov 2026, not enacted) (2026-10-29 verified, source [taxheaven ΚΦΕ art. 72](https://www.taxheaven.gr/law/4172/2013/arthro/72) + [opengov consultation, draft Art. 13](https://opengov.gr/minfin/deliberations/enischysi-toy-diathesimoy-eisodimatos-tis-apotamieysis-kai-ton-ependyseon-forologikes-misthologikes/))
- **Reduced ENFIA** for insured + village properties (village primary homes ≤1,500 pop: −50% from 2026, abolished from 2027 — legislated, Law 5246/2025 art. 10; 90th TIF extension to 2,000 residents in a draft law in public consultation since 18 Oct 2026, not yet legislated)

## Common listing platforms

- **Spitogatos** — biggest
- **XE.gr** — second
- **Indomio**, **Goldenhome**, **Plot**, **Remax**

## Caveats unique to GR

- **Ktimatologio** (cadastre) still completing — full activation slipped to 2026
- **Ypothykofylakeio** (legacy mortgage register) for areas not yet operational cadastre
- **Authairesia (unauthorized construction)** widespread — Mihaniki Vevaiosi mandatory; amnesty regimes (L.4014/2011, L.4178/2013, L.4495/2017)
- **Antikeimeniki Axia** ≠ market value (often 40-60% below)
- **Mihaniki Vevaiosi** required for ALL sales since 2011
- **Athens STR license freeze** in central districts since 1 Jan 2025; **extended through 31 Dec 2026** by KYA 225563 ΕΞ 2025 (ΦΕΚ Β' 7200/31-12-2025; a 2027 extension for Athens and the Thessaloniki A' Community freeze is planned in the MinFin 2027 draft State Budget and needs only a new KYA, none issued as of 2026-10-29) — under Council of State annulment challenge (no ruling found as of Oct 2026), and L.5313/2026 art.5 (new par.2Γ, ΦΕΚ 102/Α/25-6-2026) **deletes a flat's AMA on any inter-vivos transfer (sale/donation/parental transfer)** in the frozen zones (inheritance outside the rule), so a "ready-Airbnb" resale premium may not pass to the buyer — see `--rental`
- **Special Spatial Framework for Tourism (EChP-T) — GAZETTED 7 Aug 2026**, JMD **ΥΠΕΝ/ΔΝΕΠ/89997/3071/2026**, **ΦΕΚ Δ' 658/07.08.2026**, signed by Environment Min. Papastavrou, Deputy Environment Min. Soukouli-Viliali and Tourism Min. Kefalogianni. It puts Mykonos, Santorini and Paros in island Group II (20-250 km²; Group I = islands over 250 km², e.g. Rhodes, Corfu, Naxos, Chios) and classifies the national territory into zones A-E. **Directly applicable on gazetting**, and these change what an out-of-plan plot is worth:
  - **Minimum out-of-plan plot size (αρτιότητα) for NEW HOTELS raised**, until first-level land-use plans set their own: **16 στρέμματα** in category A, **12** in B, **8** in C and D — against 8 στρ., reducible to 4 by derogation, previously applying throughout. A category-A hotel plot's threshold roughly doubled, and sub-threshold plots lose the derogation route for a hotel. The ΦΕΚ sets **no new plot minimum for a house** or other out-of-plan building. Existing tourist accommodation on a sub-threshold plot that has not used up its building coefficient may still expand under the old minimum (art. 14 par. 3), and tourist licensing procedures that already held a building permit, pre-approval, AEPO or a complete file at publication are exempt (art. 14 par. 1). (Scope corrected 2026-10-28 against the ΦΕΚ text.)
  - **Coastal 0-25 m: complete ban** on new constructions and formations, exceptions only for disabled access, ambulance access and specified aigialos/beach-legislation works.
  - **Star-category floor**: new accommodation only 3-5 star in zones A, B and C; 2-5 star in D.
  - **Bed caps**: 100 beds/unit on island Groups II (20-250 km²) and III (<20 km²); up to 350 on category-B islands; category-A island areas 100 beds for the first 16 στρ. plus 6 beds per στρ. above, up to the category-B maximum.
  - Organised tourist-development receptors (ΟΥΤΔ) on Group-I islands are permitted only as "ήπιας ανάπτυξης" (mild development), **except Rhodes and Corfu**.
  - **STR limb still not self-executing** — the gazetted text sets the framework by which short-term letting *may* be regulated (occupancy conditions, annual duration, geographic prohibition zones, new-supply limits); it imposes no freeze itself, so there is still **no live Mykonos/Santorini STR freeze** (see `--rental`). The "up to 30% fewer beds" press framing (Apr 2026) appears in no gazetted text. Pending: art. 12 A.1 item 6 lists a legislative suspension of new AMA registrations for **newly built homes on category-(Ν) islands** (every island except Crete and Evia), which needs its own law — none found as of 2026-10-21.
  - The bed caps and island groups above match the ΦΕΚ Δ' 658/2026 PDF (`https://ia37rg02wpsa01.blob.core.windows.net/fek/04/2026/20260400658.pdf`); the ministry's Q&A is on YPEN's own site (`https://ypen.gov.gr/erotiseis-kai-apantiseis-gia-to-eidiko-chorotaxiko-plaisio-gia-ton-tourismo`), while the YPEN SSFT landing page still showed the May 2026 consultation notice.
- **Santorini (Thira) out-of-plan permit suspension — new tourist accommodation only**: building permits outside the town plan are suspended for NEW buildings of special use 15 (tourist accommodation, special tourist infrastructure and other tourism businesses under L.4276/2014, per π.δ. 59/2018 art. 1), not for houses; decision ΥΠΕΝ/ΓΓΧΣΑΠ/107662/17 (ΦΕΚ Δ' 911/23.10.2026) extended it «για ένα (1) επιπλέον έτος από τη λήξη της, και σε κάθε περίπτωση όχι πέραν της έκδοσης του προεδρικού διατάγματος έγκρισης Ειδικού Πολεοδομικού Σχεδίου Δήμου Θήρας» (for one more year from its expiry, and never beyond the decree approving the Thira Special Urban Plan), after ΦΕΚ Δ' 172/10.03.2026; permit pre-approvals granted before the 2020 suspension and approved organised tourist receptors are exempt. **Mykonos**: a general suspension of out-of-plan permits inside the area of the Mykonos Special Urban Plan ran from 1 Jan 2025 for six months (ΦΕΚ Δ' 994/31.12.2024; computed end 30 Jun 2025); an et.gr full-text search of 2025-2026 ΦΕΚ Δ found no extension, so its status since then is UNVERIFIED — ask the municipal building office (ΥΔΟΜ) before buying an out-of-plan plot. The former 'Mykonos + Santorini freeze through 31 Dec 2026' wording is superseded (2026-10-29 verified, source [ΦΕΚ Δ' 911/2026](https://ia37rg02wpsa01.blob.core.windows.net/fek/04/2026/20260400911.pdf) + [ΦΕΚ Δ' 172/2026](https://ia37rg02wpsa01.blob.core.windows.net/fek/04/2026/20260400172.pdf) + [ΦΕΚ Δ' 994/2024](https://ia37rg02wpsa01.blob.core.windows.net/fek/04/2024/20240400994.pdf) + [π.δ. 59/2018, ΦΕΚ Α' 114/2018](https://ia37rg02wpsa01.blob.core.windows.net/fek/01/2018/20180100114.pdf))
- **Santorini caldera zone**: no new builds, additions, pools, water infrastructure on Thera/Thirassia
- **Out-of-plan construction** halted in many islands
- **Golden Visa** restructured 1 Sept 2024:
  - **€800k**: the Attica region (incl. Athens), the **Thessaloniki regional unit**, the **Mykonos and Thira regional units** (every island in them, whatever its population) and **every island with more than 3,100 residents at the latest census**; one property only, and a building (or a property with a building permit) needs **≥ 120 m² of main-use space** (codified L.5038/2023 art. 100 par. 2(α); 2026-10-29 verified, source [taxheaven L.5038/2023 art. 100](https://www.taxheaven.gr/law/5038/2023/arthro/100)). Islands above the threshold include Crete, Rhodes, Corfu, Kos and Paros per [Global Citizen Solutions](https://www.globalcitizensolutions.com/greece-golden-visa-new-rules/) (secondary)
  - **€400k**: all other regions (min 120 m², single unit)
  - **€250k**: only for (i) a property whose main spaces are converted to residential use — including a former industrial building with no industry operating in it for the last 5 years — with the change of use completed (by buyer or seller) before the permit application, or (ii) a listed building bought for full restoration or reconstruction, where a transfer before the works are complete is void; one property only (art. 100 par. 2(γ)-(δ), same source)
  - **Watch — DRAFT BILL IN CONSULTATION, NOT LEGISLATED (90th-TIF bill, consultation 18 Oct–1 Nov 2026)**: the MinFin summaries of the draft 15% FMA (15.45% with the municipal contribution) on homes bought by natural persons tax-resident outside the EU/EEA from 1 Jul 2027 name no Golden Visa carve-out, and draft Art. 16 has none either: it taxes «αγοράς κατοικίας από φυσικό πρόσωπο» (the purchase of a dwelling by a natural person) tax-resident outside the EU/EEA, and none of the bill's 48 articles concerns Golden Visa buyers (opengov consultation text read 2026-10-29). The draft taxes dwelling (κατοικία) purchases; whether a €250k commercial-to-residential conversion, bought as commercial premises, falls outside it is unresolved — confirm in the enacted text. See Transaction taxes and shared/regulatory-watch.md 🇬🇷 GR.
  - **STR ban on GV property (post-reform acquisitions)**: residences acquired under the post-Law-5100/2024 Golden Visa regime may NOT be short-let or sub-let — breach → residence-permit revocation + **€50,000** administrative fine on the owners/holders (Law 5100/2024 **Art. 64**, adding para 7A to Art. 100 of Immigration Code Law 5038/2023). Min. Migration **Circular 1/2026 (prot. 72019, 21 Apr 2026)** narrowed the scope: banned = lettings **<60 days** with no services beyond accommodation + bed linen; long-term leases and hotel-type leases-with-services remain permitted; **properties bought under the pre-Sept-2024 thresholds or in the transitional window are NOT subject to the ban** (statute's "or renewal" wording had suggested otherwise — one advisory source still claims renewals of older permits must comply `(superseded by the circular)`). Circular also refers cash-back GV deals (real price below the legal minimum) to the competent tax and/or law-enforcement authorities + the Hellenic AML Authority. (2026-07-03 verified)
- **VAT 24%** on new builds suspended through 31 Dec 2026 (2027 extension drafted, not enacted)
- **Capital gains 15%** suspended through 31 Dec 2026 (2027 extension drafted, not enacted)
- **Seismic design** mandatory for new builds under either EAK-2000 or Eurocode 8 with its Greek National Annex — the owner picks one framework and cannot mix them (ΦΕΚ Β' 1457/05.06.2014 par. 4 and 6); older buildings highly variable (first national seismic code 1959, supplementary articles applied from 1985 — see Build-era hazards)
- **Wildfire risk extreme** May–Oct — evacuation zones critical
- **Tsunami coastal risk** for Hellenic Arc + Aegean
- **Short-term letting of 3+ properties = business activity** (13% VAT + obligations; ΚΦΕ art. 39Α par. 1 + VAT Code art. 11 par. 2(α)) — long-term letting is not caught by this test
- **EFKA + AADE cross-checks** for short-let income
- **PEA** mandatory since 2010

## Reddit / forum sources

- **r/greece** — biggest community
- **r/Athens**, **r/Thessaloniki**
- **r/AskGreece**
- **r/expatsingreece** — expat-specific
- **Greek Reporter**, **Ekathimerini** (English)
- **Tornos News**, **GTP Headlines**

## Verification authorities

| Authority | When to call |
|---|---|
| **Ktimatologio Office** | Title verification |
| **Ypothykofylakeio** (where cadastre not operational) | Legacy title |
| **Notary** (mandatory for sale) | Final transfer |
| **DOY (tax office)** | ENFIA, transfer tax |
| **Engineer (mihanikos)** | Mihaniki Vevaiosi |
| **Civil Engineer for Authairesia regularization** | If applicable |
| **AADE** | Tax + AMA + STR registration |
| **EYDAP / EYATH / DEYA** | Mains drains |
| **EPPO/OASP** | Seismic risk |
| **Civil Protection** | Wildfire risk |
| **HL-NTWC** | Tsunami |

## Source URL templates

| Source | URL pattern |
|---|---|
| Ktimatologio | `https://ktimatologio.gr/` (`www.ktimatologio.gov.gr` returned 503 Server Unavailable on 2026-10-29, scripted and in a browser) |
| gov.gr property registry | `https://www.gov.gr/en/categories/periousia-kai-phorologia/ktematographese` (the old `/en/ipiresies/` path redirects here) |
| Bank of Greece RPPI | `https://www.bankofgreece.gr/en/statistics/real-estate-market` |
| Spitogatos | `https://www.spitogatos.gr/en` |
| EPPO seismic | `https://oasp.gr` |
| HSGME active faults | `https://activefaults.eagme.gr/en/` |
| Civil Protection fire | `https://civilprotection.gov.gr/en/xartis` |
| HL-NTWC tsunami | `http://hl-ntwc.gein.noa.gr/en/` |
| EYDAP | `https://www.eydap.gr` |
| ELSTAT | `https://www.statistics.gr` |
| AADE | `https://www.aade.gr/` |
| Floods (EU dir.) | `https://floods.ypeka.gr/` (flood hazard and risk maps: `https://floods.ypeka.gr/geoportal/`) |
| ISMOSAV (Santorini volcano) | `https://ismosav.gr/en/home/` |
| EYDAP tariff | `https://www.eydap.gr/CustomerSupport/normalrates/` |
| EYATH tariff | `https://www.eyath.gr/plirofories-gia-to-timologio/` |
| RAAEY energy tariff comparison | `https://energycost.gr/` |
| Hellenic Police statistics | `https://www.astynomia.gr/statistika-stoicheia/` |

## Status

✅ **Fully populated** as of 2026-04-25. **Last verified**: 2026-08-15 (**SSFT gazetted** — ΦΕΚ Δ' 658/07.08.2026, JMD ΥΠΕΝ/ΔΝΕΠ/89997/3071/2026, signed 7 Aug 2026, one day after the previous pass read it as unsigned; out-of-plan αρτιότητα, 25 m coastal ban, star-category floor and island bed caps now directly applicable, STR limb confirmed still enabling-only. Only the SSFT claims were re-verified in this pass. Earlier 2026-08-06: SSFT gazetting status checked against YPEN; prior Tier-A quarterly refresh 2026-07-03 — fast-moving claims re-verified; structural sections unchanged). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md). Announced non-EU 15% transfer-tax watch added 2026-09-24 from the government 90th TIF measures page; re-checked 2026-10-21 as a draft bill in public consultation (MinFin release 18 Oct 2026: 1 Jul 2027 start, natural persons tax-resident outside the EU/EEA; rate per the 2027 draft State Budget). 90th-TIF bill limbs (2,000-resident ENFIA exemption, VAT and CGT suspension extensions to 2027), the 2027 ΤΤΑ municipal levy, the Spiti Mou II close-out and the pending SSFT island new-build AMA freeze also re-checked 2026-10-21 (see shared/regulatory-watch.md). Rental / tax / visa tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md). Ktimatologio registration fee (KYA 2/12-1-2026) added to Cost benchmarks 2026-10-23. SSFT claims re-verified 2026-10-28 against the ΦΕΚ Δ' 658/2026 text: the 16/12/8 στρ. plot minimum applies to new hotels only (wording corrected), and an et.gr full-text search of 2026 ΦΕΚ Α, Β and Δ issues for the JMD number (ΥΠΕΝ/ΔΝΕΠ/89997/3071) found no amendment, corrigendum or implementing decision.
**Coverage check**: pricing, traffic, tax (incl. 2025-2026 ENFIA reforms + VAT/CGT suspensions), rental (incl. STR Law 5170/2025 + Athens freeze + Special Spatial Framework for Tourism, gazetted ΦΕΚ Δ' 658/07.08.2026), work, risks (seismic + volcanic + wildfire + tsunami), mains all have primary government sources + cost benchmarks.
**Confidence**: HIGH for STR reforms (Athens Times, GTP Headlines, ProtoThema, BNB News, Airbnb 2025 Greek tax guide all confirm); HIGH for ENFIA 2025-2026 cuts (multiple tax law firm sources confirm; village abolition from 2027 legislated in Law 5246/2025 art. 10; 90th TIF extension to 2,000 residents in a draft law in public consultation since 18 Oct 2026, not yet legislated); HIGH for the VAT/CGT suspensions through 31 Dec 2026 (VAT: Law 5246/2025 art. 12, gazetted 11 Nov 2025; CGT: L.5162/2024 art. 90, ΚΦΕ art. 72 par. 33a; vatcalc + Elxis + stegasi.gov.gr confirm; extensions to 31 Dec 2027 drafted in the 90th-TIF bill, not enacted); HIGH for Golden Visa restructuring (Global Citizen Solutions + multiple sources confirm 1 Sept 2024 effective) and the GV short-term-rental ban (Law 5100/2024 Art. 64; Varnavas + WFW + IMI Daily + Circular 1/2026 confirm). HIGH for Cyclades bed caps (Special Spatial Framework gazetted ΦΕΚ Δ' 658/07.08.2026; bed caps and island groups confirmed against the ΦΕΚ PDF and the YPEN Q&A). MEDIUM for cadastre completion timeline (target slipping repeatedly).

## Extension TODOs

- [ ] Per-municipality ENFIA coefficient table
- [ ] Authairesia regularization decision tree (which amnesty applies)
- [ ] Mykonos / Santorini permit freeze zone overlay
- [ ] Athens STR-frozen district perimeter
- [ ] Cyclades STR implementing acts under the Special Spatial Framework for Tourism (SSFT art. 12 A.1 items 5-6)
- [ ] EYDAP/DEYA per-municipality connection lookup
- [ ] Wildfire-vulnerable zone overlay (Civil Protection)
- [ ] Tsunami coastal hazard zoning per island
- [ ] Cadastre operational status per municipality
- [ ] Golden Visa eligibility decision tree
- [ ] PEA cost + energy class scoring for new + retrofit
