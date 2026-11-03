# Bosnia and Herzegovina 🇧🇦 — Property Due-Diligence Playbook

ISO2: `ba`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`71000` Sarajevo, `78000` Banja Luka, `88000` Mostar, `75000` Tuzla)
- **DUAL-ENTITY STATE** (post-Dayton 1995):
  - **Federacija BiH (FBiH)** — Bosniak + Croat majority; 10 cantons
  - **Republika Srpska (RS entity)** — Serb majority
  - **Brčko District** — separate self-governing
- **Currency**: **BAM (Konvertibilna marka)** — pegged to EUR at **1 EUR = 1.95583 BAM** via currency board (KM issued 1:1 against the Deutsche Mark from 1998; euro peg since 1 Jan 2002, CBBH Annual Report 2024); EXTREMELY stable
- **Languages**: Bosnian, Croatian, Serbian (all three official)
- **Cadastre — DUAL ENTITY**:
  - **FBiH**: Federalna uprava za geodetske i imovinsko-pravne poslove `https://fgu.com.ba/en/`
    - Public portal: `https://katastar.ba/`
    - Geoportal: `https://www.katastar.ba/geoportal` (registration + login required for cadastral data, checked 2026-10-23)
    - 79 FBiH municipalities, centralized DB Sarajevo
  - **RS entity**: **RGURS** (RUGIPP — Republička uprava za geodetske i imovinsko-pravne poslove) `https://www.rgurs.org/sr-lat`
    - eKatastar: `http://ekatastar.rgurs.org/` — public view (Javni uvid), search by parcel or address; HTTPS handshake failed 2026-10-23, plain http works
    - Geoportal: `https://geoportal.rgurs.org/`
    - HQ Banja Luka, 48 regional units, 16 regional offices
  - **Brčko District**: separate (less digitized)
- **Identifier**: parcela + KO + entity selector (CRITICAL — must specify FBiH/RS-entity/Brčko)
- **EU candidate** since Dec 2022 (post-Dayton legacy slows reforms); the European Council decided on 21 Mar 2024 to open accession negotiations, but the Council adopts the negotiating framework only once the steps in the Commission's 12 Oct 2022 recommendation are taken (European Commission enlargement page, checked 2026-10-23); in a 21 Mar 2026 op-ed on the EEAS site the EU Head of Delegation called the two years since "yet another missed opportunity"

## Section: `--price`

### Primary sources

- **CBBH (Centralna banka BiH)**: `https://www.cbbh.ba/` — Financial Stability Reports
- **Agencija za statistiku BiH (BHAS)**: `https://bhas.gov.ba/` — quarterly prices of new dwellings sold
- **Entity statistics**: Federalni zavod za statistiku FBiH (`https://fzs.ba/`) + Republički zavod za statistiku RS (`https://www.rzs.rs.ba/`) — quarterly new-dwelling prices with Sarajevo / Banja Luka rows
- **Registered-sale price registers**: FGU Registar cijena nekretnina, FBiH (`https://katastar.ba/rcn`, half-yearly and annual reports by municipality; resale contracts only, first sales excluded) + RGURS Registar cijena nepokretnosti, RS (`https://www.rgurs.org/sr-lat/stranica/reg-cijena-nepokretn`)
- **Global Property Guide**, **Investropa** — secondary aggregators

### Listing platforms

- **PIK.ba** (the former OLX.ba, still served at `olx.ba`; pik.ba redirects there), **Nekretnine.ba**, **Nađi stan** (`nadjistan.ba`), **Realitica** (BiH section) — live 2026-10-23
- **Sasomange.ba**, **Pojdimo.ba**: ❌ DEPRECATED — dead on 2026-10-23 (no DNS record); verify current portals at PIK.ba
- Sarajevo + Banja Luka primary markets

### 2026 price benchmarks (official statistics)

New build = completed new dwellings sold by developers (BHAS / FZS / RZS RS quarterly surveys). Resale = second and later sales only, first sales excluded: contracts valued by municipal commissions for transfer tax and entered in the FGU Registar cijena nekretnina (FBiH only). EUR at the 1.95583 peg. City / municipality averages, not parcel values; quarterly city samples are small (n shown) and swing from quarter to quarter.

| Region | EUR/m² (BAM/m²) | YoY |
|---|---:|---:|
| **BiH, new build** | 1,693 (3,311) *(Q2 2026 data, source BHAS)* | +5.2% vs Q2 2025 (BHAS) |
| **FBiH, new build** | 1,772 (3,466; n = 236) *(Q2 2026 first results, source FZS)* | +11.5% vs Q2 2025 (FZS) |
| **FBiH, resale apartments** | 1,585 (3,100; n = 678) *(H1 2026 data, source FGU RCN)* | unchanged vs H1 2025 (FGU RCN) |
| **Sarajevo (FBiH), new build** | 2,201 (4,305; n = 63) *(Q2 2026 first results, source FZS)* | computed +21.3% vs BAM 3,548.9 in Q2 2025 first results (FZS) |
| **Sarajevo municipalities, resale apartments** | Centar 2,556 (5,000) · Stari Grad 2,500 (4,890) · Novo Sarajevo 2,480 (4,850) · Novi Grad 2,127 (4,160) *(H1 2026 data, source FGU RCN)* | Centar +23% · Novi Grad +22% · Stari Grad +18% · Novo Sarajevo +15% vs H1 2025 (FGU RCN) |
| **RS entity, new build** | 1,633 (3,193; n = 670) *(Q2 2026 data, source RZS RS)* | +0.8% vs Q2 2025 (RZS RS) |
| **Banja Luka (RS entity), new build** | 2,124 (4,154; n = 161) *(Q2 2026 data, source RZS RS)* | computed +13.8% vs BAM 3,649 in Q2 2025 (RZS RS) |
| **Mostar (FBiH), resale apartments** | 1,483 (2,900; n = 59) *(H1 2026 data, source FGU RCN)* | numeric YoY not published by FGU |
| **Tuzla (FBiH), resale apartments** | 1,580 (3,090; n = 87) *(H1 2026 data, source FGU RCN)* | numeric YoY not published by FGU |
| **Zenica (FBiH), resale apartments** | 1,534 (3,000; n = 80) *(H1 2026 data, source FGU RCN)* | numeric YoY not published by FGU |
| **Bijeljina (RS entity), new build** | 1,370 (2,679; n = 60) *(H1 2026 data, Klix.ba citing RZS RS — secondary)* | data not publicly available — verify at rzs.rs.ba |

*(superseded)* The previous GPG-attributed figures (Sarajevo €1,980 for 2024, Banja Luka €1,991, Mostar €1,179 / +27.2%) and the unsourced 2025 €/m² bands for Sarajevo, Mostar, Tuzla, Bijeljina and Zenica are replaced by the official series above. *(2026-10-23 verified against BHAS Q2 2026, FZS 2.3.2 Q2 2026, RZS RS 256/26 and FGU RCN H1 2026 releases; Bijeljina from Klix.ba, 10 Aug 2026)*

### Compute

1. EUR/m² = price / **korisna površina** (usable area)
2. **Currency**: BAM-EUR peg 1.95583 = predictable conversion (no FX risk)
3. **Cross-check entity**: FBiH vs RS entity has DIFFERENT taxes/laws
4. Cross-check **PIK.ba** (ex-OLX) asking prices against transaction data: BHAS / FZS / RZS RS new-dwelling prices + FGU RCN registered sales (FBiH)

### Key terms

- BAM = Konvertibilna marka (pegged to EUR)
- FBiH = Federacija Bosne i Hercegovine
- RS entity = Republika Srpska entitet
- KO = katastarska opština
- Energetski certifikat = energy certificate
- ZK izvadak = land register extract

---

## Section: `--traffic`

### Sources

- **JP Ceste Federacije BiH d.o.o. Sarajevo** (`https://jpcfbih.ba/bs/poslovanje/publikacije`) — FBiH magistral roads; annual automatic-count publication *Intenzitet prometa na mreži magistralnih cesta Federacije BiH* (2025 edition: 143 counting points) *(2026-10-23 verified)*
- **JP Autoceste FBiH** (`https://www.jpautoceste.ba/`) — A1 motorway (Corridor Vc) in FBiH
- **JP Putevi Republike Srpske** (`https://www.putevirs.com/`) — RS magistral + regional roads; **JP Autoputevi Republike Srpske** (`https://www.autoputevirs.com/`) — RS motorways + expressways (Zakon o javnim putevima RS)
- Sarajevo + Banja Luka city traffic data

### Key term

**PGDS (prosječni godišnji dnevni saobraćaj)** = AADT-equivalent; JP Ceste FBiH also reports **PLDS** (prosječni ljetni dnevni saobraćaj, summer average). Also written **PGDP** (… dnevni promet).

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional, urban side streets)
- 🟠 10,000–35,000 v/d (Sarajevo arterials, M-roads)
- 🔴 > 35,000 v/d (autoput A1, Sarajevo ring)

*Calibration (2025 data, source JP Ceste FBiH, Intenzitet prometa na mreži magistralnih cesta FBiH u 2025.): of 143 magistral-road counters, 58.7 % < 6,000 v/d, 33.6 % 6,000–15,000 v/d, 7.7 % > 15,000 v/d. Busiest: M4 Šićki Brod 1 – Simin Han 1 (Tuzla zapad) 24,828 v/d, M18 Stup – Trnovo (Stup, Sarajevo) 24,165 v/d, M17 Blažuj – Tarčin 19,967 v/d. No magistral road reaches 🔴; no published A1 motorway PGDS was located, so the 🔴 examples are unconfirmed. A counter value describes its road section, not a specific parcel.*

---

## Section: `--tax`

### Annual property tax — DUAL ENTITY DIFFERENT SYSTEMS

#### FBiH (Federacija)

- **No FBiH-wide property tax** — each canton's own law sets what is taxed and how much. PwC gives **BAM 0.5–3 per m²** across cantons (FLAT per-sqm, NOT percentage) *(2026 data, source PwC BA Corporate — other taxes, last reviewed 23 Sep 2026; per-canton figures unconfirmed — see Extension TODO)*
- **Sarajevo Canton** (Zakon o porezu na imovinu KS, Sl. novine KS 7/09, art. 3 + 6): taxes holiday homes/flats (min **3 KM/m²** up to 150 m², **5 KM/m²** above) and flats, houses or business premises **let out** (min **4 KM/m²**); each municipality sets the exact amount (art. 6(2)). An owner-occupied main home is **not on the taxable list** *(2009 law text on pufbih.ba — check later amendments with Porezna uprava FBiH)*
- Computed from the KS minimums: 60 m² flat let out ≥ 240 KM/yr (60 × 4); 60 m² holiday flat ≥ 180 KM/yr (60 × 3); owner-occupied main home 0

#### RS entity

- **Up to 0.20 % of assessed market value** (percentage-based, unlike FBiH); **up to 0.10 %** for premises used directly for production. Each municipality/city adopts its rate by 31 January for the current year, plus the zone values that form the tax base (value at 31 Dec of the prior year) (art. 4 + 8 Zakon o porezu na nepokretnosti RS, Sl. glasnik RS 91/15). Example: Novi Grad set 0.20 % for 2026 (decision of 25 Dec 2025). Paid by the owner in two instalments, by 30 June and 30 September (PwC) *(2026 data, sources: law text on paragraf.ba + Novi Grad 2026 decision + PwC BA Individual — other taxes, last reviewed 23 Sep 2026)*
- Computed: at the 0.20 % cap, an assessed value of 195,583 KM (€100k) gives ≈391 KM (≈€200)/yr — the base is the municipality's zone value, not the purchase price

### Transaction taxes — MAJOR DIVERGENCE

| Tax | FBiH | RS entity |
|---|---|---|
| **Transfer tax (porez na promet nepokretnosti)** | **up to 5 %**, set by cantonal law — 5 % in Sarajevo, Zenica-Doboj and Tuzla cantons; Herzegovina-Neretva lets each municipality set the rate (max 5 %). **Payer varies**: the buyer in Sarajevo Canton and (unless the contract says otherwise) Zenica-Doboj, the seller in Tuzla Canton *(2026 data, sources: KS law Sl. novine KS 28/18 art. 7 + 11; ZDK law art. 5 + 9; HNK law art. 12 on pufbih.ba; Tuzla per tuzlainfo.ba 8 Jul 2025 — secondary)* | **0% — NO transfer tax** *(2026 data, PwC BA Corporate — other taxes)* |
| **VAT (PDV)** | 17% on first-sale new builds | 17% |
| **Notary fees** | Fixed tariff: **320 KM** for 75,001–100,000 KM, **+30 KM** per started 100,000 KM above, capped at 1,800 KM, + VAT (Tarifa o nagradama i naknadama notara, Sl. novine FBiH 40/21, tarifni broj 1) | Points tariff, 1 point ≤ 0.50 KM excl. VAT: **750 points** (≤375 KM) for 80,001–100,000 KM, **900 points** (≤450 KM) for 150,001–200,000 KM, max 4,000 points (Uredba, Sl. glasnik RS 85/21, tarifni broj 1) |

**VAT 17%** = one of the lower headline VAT rates in Europe, no reduced rate; applies to first-sale new builds only *(2026 data, source PwC BA Corporate — other taxes)*. In Sarajevo Canton a new build sold to its first buyer with VAT paid is exempt from transfer tax (art. 16(b) KS law 28/18). Computed notary fee on a 195,583 KM (€100k) flat: FBiH 350 KM ≈ 0.18 %, RS ≤ 450 KM ≈ 0.23 %, both before VAT on the fee

### First-home VAT refund (art. 54a ZPDV) — IN FORCE, but CLOSED TO FOREIGN BUYERS

- **Status**: **IN FORCE and claimable since 8 July 2026**. Art. 54a ZPDV was adopted by the **Predstavnički dom 3 Dec 2024** and the **Dom naroda 2 Apr 2025** (Sl. glasnik BiH 20/25) but self-suspended until its rulebook landed; the **UINO rulebook art. 105a was published 30 June 2026** (Sl. glasnik BiH 45/26) and entered force **8 July 2026** — claims are now open. Verify status: [UINO VAT refund](https://www.uino.gov.ba/portal/en/vat/vat-refund/) + [UINO — povrat PDV-a za kupnju prvog stambenog objekta](https://www.uino.gov.ba/portal/hr/novosti-hr/povrat-pdv-a-za-kupnju-prvog-stambenog-objekta) *(2026-10-21 verified against the Sl. glasnik BiH 20/25 and 45/26 texts on uino.gov.ba + UINO notice; the notice cites the law as 25/25, but the gazette and UINO's legislation list say 20/25)*
- **ELIGIBILITY IS ADULT BiH CITIZENS WITH PERMANENT BiH RESIDENCE ONLY — a foreign buyer CANNOT claim this refund** *(2026-08-07 verified)*. As a foreign buyer, budget the full 17 % VAT into the new-build purchase price
- **Scope**: state-level — covers **FBiH + RS + Brčko**, **not FBiH-only**. New-build only, and only where the sale is itself subject to VAT
- **Amount**: **40 m² for the buyer + 15 m² per family-household member** at **VAT 17 %**; refund **capped at 14.5299 % × (BiH average flat price incl. VAT, from the latest Agency for Statistics quarterly bulletin at contract date) × 55 m²** — computed for contracts signed after the BHAS Q2 2026 release (20 Aug 2026; average 3,311 KM/m² incl. VAT) and until the next release: 0.145299 × 3,311 × 55 ≈ **26,460 KM**; with the Q1 2026 figure (3,701 KM/m², release 20 May 2026) the cap was ≈29,576 KM *(2026 data, source BHAS new-dwelling price releases of 20 May + 20 Aug 2026)*
- **Conditions**: buyer must not have owned a flat, house, apartment or other dwelling for living or letting in BiH in the **7 years before the claim date** (rulebook art. 105a(6)(a)); **5-year no-resale lock-in** running from service of the decision (art. 105a(14)). A resale inside 5 years means repaying the refund plus interest (art. 105a(15)), and art. 67 ZPDV sets a 5,000-10,000 KM fine
- **Deadline**: claims due by **30 June of the year after the sale is registered**; a **6-month transitional window (to ~8 Jan 2027)** covers sales registered between 20/25 and 45/26 taking effect. Sales registered before 20/25 took effect are excluded unless the buyer was not at fault (rulebook art. 2). Claims go to the UINO regional centre for the seller's seat and are decided within 6 months

### Personal income tax (PIT) — flat, by entity

| Entity | PIT rate |
|---|---:|
| **FBiH** | **10%** flat (Zakon o porezu na dohodak FBiH, Sl. novine FBiH 10/08 +) |
| **RS entity** | **8%** on employment income (lična primanja) only; **10%** self-employment; **13%** on capital income incl. rental, capital gains, author rights and other income (art. 4 Zakon o porezu na dohodak RS, Sl. glasnik RS 60/15 ... 114/25) |
| **Brčko District** | **10%** flat |

Basic personal allowances differ significantly across entities — FBiH **3,600 KM/yr** (300 KM/month, Porezna uprava FBiH); RS **12,000 KM/yr** + 1,800 KM/yr per dependent (art. 10(3) RS law, since Sl. glasnik RS 119/21); Brčko **14,400 KM/yr** (1,200 KM/month, art. 25 BD law, unofficial consolidated text through Sl. glasnik BD 5/25 — verify at Direkcija za finansije Brčko distrikta). PwC (last reviewed 23 Sep 2026) still shows RS and Brčko at 6,000 KM/yr (superseded by the law texts). RS small entrepreneurs: 2% of annual revenue. *(2026-10-21 verified against the RS and BD consolidated law texts + Porezna uprava FBiH + PwC BA Individual taxes)*

### Capital gains — individuals, by entity

| Entity | CGT (individuals) |
|---|---|
| **FBiH** | **10 %** final tax on the gain (market value less acquisition value indexed by industrial producer prices); **NOT taxed** if the property was the home of the owner or dependants until sale, or if sold **more than 3 years after acquisition** (art. 20(4), 20(9), 32(4) Zakon o porezu na dohodak FBiH, Sl. novine FBiH 10/08, 9/10, 44/11, 7/13, 65/13). The earlier PwC/Eurofast "not taxable" reading is **(superseded)** by the statute; PwC (last reviewed 23 Sep 2026) states no FBiH capital-gains rule *(2026 data, law text on paragraf.ba + oilgas.fmeri.gov.ba)* |
| **RS entity** | **13 %** (art. 4(3) Zakon o porezu na dohodak RS); **NOT taxed** on real estate owned continuously for **at least 7 years**, on inherited property, or on transfers between spouses or first-degree relatives (art. 36a); no main-home exemption *(2026 data, consolidated text Sl. glasnik RS 60/15 … 114/25 on paragraf.ba)* |
| **Brčko District** | **10 %** on each gain (art. 33(8) Zakon o porezu na dohodak BD, as amended June 2020); **NOT taxed** if the property was the home of the owner or dependants, or if sold more than 3 years after acquisition (art. 21(11), unofficial consolidated text) — verify with Direkcija za finansije BD *(2026 data, Skupština BD amendment text + consolidated text)* |

### Total transaction cost (buyer side)

*Computed from the tariffs and statutes above for €50k–€250k; land-register / cadastre fees and any agency commission come on top — data not verified, ask the notary for a quote.*
- FBiH resale: **~5.1–5.4 %** where the buyer is the transfer-tax payer (5 % + notary ≈0.1–0.4 %), **~0.1–0.4 %** where the seller pays (e.g. Tuzla Canton)
- RS entity resale: **~0.1–0.4 %** (notary only; no transfer tax)
- New build: 17 % VAT in the price + notary ≈0.1–0.4 %; no transfer tax on a VAT-paid first sale in Sarajevo Canton (other cantons: verify)

### Future risk

- EU accession reforms may align entities (slowly)
- First-home VAT refund is state-level and already IN FORCE (8 Jul 2026) — the part still moving is the transitional claim window, which closes ~8 Jan 2027

---

## Section: `--rental`

### Long-term residential

- Tenancy laws differ by entity
- FBiH cantonal variation
- Tenant protections moderate

### Short-let

- **Sarajevo + Mostar**: registration required, low enforcement
- **Mostar UNESCO** stricter
- 2026 Slovenia/Croatia-style consent rules **not confirmed** for BA

### Tax on rental

- Resident: flat rates, NOT progressive — **FBiH 10% / RS 13%** (rental is capital income under art. 31 RS law, taxed at 13% under art. 4(3) on income less 20% normed costs under art. 34 — NOT the 8% employment rate) **/ Brčko 10%** (tourist letting 10% without allowance) *(2026-10-21 verified, RS + BD consolidated law texts)*
- Non-resident: verify treaty + withholding-schedule per entity at fmf.gov.ba / mf.vladars.net

---

## Section: `--work=<profession>`

### Sources

- **Federalni zavod za zapošljavanje** (`https://www.fzzz.ba/`) + **JU Zavod za zapošljavanje Republike Srpske** (`https://zzzrs.net/`)
- **MojPosao.ba** (kolektiv.ba redirects here), **PIK.ba** jobs (formerly OLX Posao), **LinkedIn BA**
- **Posao.ba**: ❌ DEPRECATED — dead on 2026-10-23 as a job board (posao.ba now redirects to serda.ba, the Sarajevo regional development agency); verify with Federalni zavod za zapošljavanje / Zavod za zapošljavanje RS

### Self-employment

- **Obrt** (sole trader)
- **D.o.o.** (limited): minimum capital is set per entity, not per canton — FBiH **BAM 1,000** (art. 307(1) Zakon o privrednim društvima FBiH, Sl. novine FBiH 81/15, 75/21); RS entity **BAM 1** cash capital (art. 107(1) Zakon o privrednim društvima RS, Sl. glasnik RS 127/08 … 45/25) *(2026 data, consolidated texts via Paragraf Lex BA)*
- **PDV** registration: mandatory above **BAM 100,000** taxable turnover (art. 57(1) ZPDV; raised from BAM 50,000 by Sl. glasnik BiH 80/23, in force 2 Dec 2023) *(2026 data, sources UINO notice of 29 Nov 2023 + ZPDV consolidated text via Paragraf Lex BA)*

### Salary benchmarks (2026)

- Average monthly wages (the statistics offices publish averages, not medians):
  - Sarajevo (Kanton Sarajevo): net BAM 2,056 (≈ €1,051) / gross BAM 3,259 (≈ €1,666) *(June 2026 data, source Zavod za informatiku i statistiku Kantona Sarajevo)*
  - FBiH: net BAM 1,714 / gross BAM 2,681 *(June 2026 data, source Federalni zavod za statistiku, release 8.1.6)*
  - RS entity: net BAM 1,727 / gross BAM 2,668 *(Sept 2026 data, source Republički zavod za statistiku RS, release of 22 Oct 2026)*
  - Banja Luka: net BAM 1,573 / gross BAM 2,439; Bijeljina: net BAM 1,312 / gross BAM 2,012 *(2024 data, source RZS RS "Gradovi i opštine Republike Srpske 2025") — rates/figures may have changed since*
  - BiH: net BAM 1,693 *(Q2 2026 data, source BHAS)*
- **Minimum wages (net)**: FBiH **BAM 1,027** for every full-time worker (Odluka Vlade FBiH, Sl. novine FBiH 100/25); RS entity tiered by the education a job requires, from **BAM 1,000** (gross 1,476.23) to **BAM 1,450** for university-level jobs (gross 2,245.90) (Odluka o najnižoj plati, Sl. glasnik RS 115/25) *(2026 data, sources Sl. novine FBiH 100/25 + Vlada RS, 26 Dec 2025)*

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **RHMZ RS** (Republički hidrometeorološki zavod RS — seismology service) | `https://rhmzrs.com/` | Seismic monitoring (RS network), meteorology, hydrology |
| **FHMZ BiH** (Federalni hidrometeorološki zavod) | `https://www.fhmzbih.gov.ba/` | Weather, climate, seismicity of BiH |
| **BHMAC (Mine Action Centre)** | `https://www.bhmac.org/` | **Mine contamination from 1992-95 war** |
| **Institut za standardizaciju BiH — Eurocode maps** | `https://eurokodovi.ba/` | BAS EN 1998-1/NA:2018 seismic zones + reference ground acceleration, looked up by coordinates |
| **Agencija za vodno područje rijeke Save** (FBiH) | `https://www.voda.ba/mape-rizika` | Flood hazard + flood risk maps (20 / 100 / 500-yr return periods) for significant-flood-risk areas in the FBiH Sava basin |

### Specific risks

#### Earthquake

- **27 Oct 1969 Banja Luka M6.6** (after an M5.6 foreshock on 26 Oct): **15 dead, 1,117 injured, 86,000 flats destroyed or heavily damaged** — the strongest quake recorded in BiH *(source RHMZ RS, "57 godina od katastrofalnog zemljotresa u Banjoj Luci", 2026)*
- **Background activity**: about 3 instrument-only quakes a day (below Mercalli III), roughly ten a year felt or damaging; 1,084 quakes above M3.0 recorded since 1900 *(source FHMZ BiH — Seizmičnost teritorije BiH, page undated — rates/figures may have changed since)*
- **Highest-hazard zones** over a 100-yr+ horizon: south-east Herzegovina (**Trebinje, Neum**), **Banja Luka**, **Treskavica** mountain (south of Sarajevo); regional faults include Bugojno, Višegrad, **Neretva** and Banja Luka, and quakes near Dubrovnik, Makarska, Knin and Montenegro also reach BiH *(source FHMZ BiH)* — south-east Herzegovina is among the highest-hazard zones, not a low one
- **Site value**: BAS EN 1998-1/NA:2018 reference ground acceleration at `https://eurokodovi.ba/` (enter coordinates) — a zone value for the location, not an assessment of the building

#### Floods

- **May 2014 catastrophic floods** (rain 14–19 May): Sava + Bosna rivers (same Tamara/Yvette cyclone as Serbia), the heaviest rainfall in 120 years; ~90,000 people displaced, about a third of the country affected across FBiH, RS and Brčko; total economic impact **BAM 3.98 bn** *(2014 data, source BiH/EU/UN/World Bank Recovery Needs Assessment, via ILO + PreventionWeb)*
- **3–4 Oct 2024 flash floods + landslides** (Herzegovina-Neretva + Central Bosnia cantons): **27 dead**; ~1,660 households damaged — Konjic 594, Kiseljak 284, Jablanica 252, Kreševo 244, Fojnica 218, Mostar 68; worst damage in Donja Jablanica, Zlate and Buturović Polje *(2024 data, source IFRC DREF final report MDRBA017)*
- **Flood maps**: FBiH Sava-basin hazard + risk maps at `https://www.voda.ba/mape-rizika` — check the parcel against the mapped extent; an unmapped stream is not evidence of no risk

#### Mine contamination — UNIQUE

- **Legacy from Yugoslav Wars 1992-1995**
- **Republika Srpska + Federation** rural areas affected — suspected hazardous area **774.69 km²** (FBiH 624.51 km², RS 150.18 km²) *(January 2026 data, source BHMAC — Plan deminiranja u BiH za 2026. godinu, prijedlog)*, down from 822.87 km² in January 2025; an estimated **170,062 mines** remaining and 1,398 affected communities in 118 municipalities *(January 2025 data, source BHMAC — Minska situacija — rates/figures may have changed since)*
- BiH will not meet its March 2027 Ottawa-Convention clearance deadline; BHMAC's 2026 plan states a new extension request will be filed in 2026 — treat contamination as long-term
- **BHMAC check mandatory (due-diligence step)** for rural/peri-urban properties: BHMAC sends mine-situation records to municipalities, so ask the općina/opština **Služba za civilnu zaštitu** (demining coordinator); BHMAC's mobile app shows the distance to the nearest suspected area *(2026-10-23 verified, BHMAC Pitanja i odgovori)*
- Insurance + mortgage may require demining certificate *(unconfirmed — no lender or insurer rule located)*

#### Other

- **Landslides**: Bosnian highlands — set off across the country in May 2014 and in the Oct 2024 Jablanica/Konjic event (above)
- **Wildfires**: Herzegovina karst
- **Air quality**: Sarajevo (basin temperature inversions) + Tuzla winter smog from household coal/wood heating; >90 % of Sarajevo Canton residents (391,406) live where the PM10 daily limit was exceeded at least 35 times *(source UNDP / Sarajevo Canton solid-fuel strategy executive summary, Jan 2025)*; ~3,300 premature deaths a year in BiH from PM2.5 *(source EEA, Europe's environment 2025)*

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **Yugoslav 1945-1990** | Asbestos common, panel buildings; seismic building rules tightened after the 1963 Skopje quake and again after Banja Luka 1969 (RHMZ RS) — check the design year |
| **War-damaged 1992-1995** | **Reconstruction quality variable**; some "fast rebuild" structures problematic |
| **Post-2000** | Improved codes (Eurocode 8 national annex BAS EN 1998-1/NA:2018); EU funding driving modernization |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski / energijski certifikat** | **FBiH**: seller must show the buyer the certificate before ownership transfers, and sale ads must state the energy indicator (art. 22 Zakon o energijskoj efikasnosti u FBiH, Sl. novine FBiH 22/17); **Brčko**: required for buildings and parts sold or let, valid 10 years (art. 61 Zakon o energetskoj efikasnosti BD, adopted 14 Jul 2022); **RS**: required before sale or rental only for new buildings built after the law took effect (art. 90(4) Zakon o uređenju prostora i građenju RS) *(2026-10-23 verified, FBiH + BD law texts on parlamentfbih.gov.ba + skupstinabd.ba; RS consolidated text via paragraf.ba)* |
| **Notar + ugovor (entity-specific notary law)** | **RS**: notarial form mandatory for real-estate transfers, void otherwise (art. 57 Zakon o notarskoj službi u RS, consolidated text via paragraf.ba); **Brčko**: notarial form mandatory (law-firm summary — verify); **FBiH**: no longer mandatory — FBiH Constitutional Court U-15/10 (2 Dec 2015) struck down art. 73 Zakon o notarima (FBiH Government draft-amendment memorandum, parlamentfbih.gov.ba); signatures certified at a notary or the municipal court are accepted for land-register entry (FBiH Supreme Court legal position of 8 Dec 2022, per law-firm summary — verify with the gruntovnica) |
| **ZK izvadak / vlasnički list** (land register extract) | Title verification — FBiH: from the zemljišnoknjižni ured of the općinski sud; the cadastre's posjedovni list is NOT proof of ownership (pravosudje.ba, Općinski sud Kakanj). RS: list nepokretnosti from the RGURS područna jedinica; the eKatastar online view is informational, not an official document (ekatastar.rgurs.org) |
| **Mine-situation check (rural)** | Where applicable; ask the općina/opština civil-protection service, which holds BHMAC records — a statutory "demining certificate" at sale is unconfirmed |

---

## Section: `--mains`

### Sources

- **Vodovod per municipality**, all separate: Sarajevo — KJKP Vodovod i kanalizacija (`https://www.viksa.ba/`; posts daily lists of streets with repair-related supply interruptions — check the target street); Banja Luka — Vodovod a.d. Banja Luka (`https://vodovod-bl.com/`); Mostar — Vodovod Mostar (`https://vodovod-mostar.ba/`) *(2026-10-23 verified, operator sites)*
- **Many post-war repairs ongoing** — infrastructure variable
- Rural: septic + cesspits common

### Costs

*est. model ranges from regional contractor figures — verify with local vodovod / utility quote.*

| Scenario | Cost (EUR, est.) |
|---|---:|
| Mains connection | 1,500–5,000 |
| Septic upgrade | 2,500–6,000 |
| Bored well | 3,000–8,000 |

---

## Cost benchmarks (BA 2026)

*Tax and notary rows computed from statutes and tariffs (2026 data, see `--tax`); work rows are est. model ranges (BA 2026) — verify with quotes; demining cost in particular is highly variable.*

| Work | Cost (EUR, est.) |
|---|---:|
| Energetski certifikat | 100–250 |
| Notar fees | ≈0.1–0.4 % of price for €50k–€250k (computed from FBiH 40/21 + RS 85/21 tariffs, before VAT) |
| Transfer tax (FBiH) | up to 5 % (5 % in Sarajevo, Zenica-Doboj, Tuzla cantons; payer varies by canton) |
| Transfer tax (RS entity) | **0%** |
| **Total transaction cost (FBiH)** | **~0.1–0.4 %** (seller pays transfer tax) to **~5.1–5.4 %** (buyer pays), before registration fees + agency commission |
| **Total transaction cost (RS entity)** | **~0.1–0.4 %** before registration fees + agency commission |
| Roof renovation | 3,500–10,000 |
| Demining (rural property) | 5,000–25,000+ |
| War-damage retrofit | varies massively |
| Energy retrofit | 8,000–25,000 |

## Active fiscal incentives (2025-2026)

- **First-home VAT refund (art. 54a ZPDV)** — IN FORCE since 8 Jul 2026, state-level (FBiH + RS + Brčko); 17 % VAT on 40 m² + 15 m² per family-household member, capped; **adult BiH citizens with permanent BiH residence only — foreign buyers ineligible** *(2026-08-07 verified)*
- **EU pre-accession funding** — candidate status granted by the European Council Dec 2022; IPA III 2025-2027 multiannual action of €140.5m adopted July 2025 *(2025 data, source EEAS BiH country fiche, Nov 2025)* — not a buyer-level incentive
- **EU Reform Agenda (Reform and Growth Facility)** — adopted by the BiH Council of Ministers 30 Sep 2025 (per European Western Balkans), approval announced by the European Commission 4 Dec 2025; up to **€976.6m**, released only after the Facility and Loan Agreements enter into force and conditions are met *(2025 data, source European Commission, 4 Dec 2025; ratification status not verified)* — not a buyer-level incentive
- **New-build market**: 1,160 new flats sold in BiH in Q2 2026 at an average 3,311 KM/m², +7.3 % on the 2025 average (Q1 2026: 1,202 flats at 3,701 KM/m², +20.0 %) *(2026 data, source BHAS releases of 20 May + 20 Aug 2026)*; a VAT-refund effect on Sarajevo construction: data not publicly available — verify at bhas.gov.ba

## Common listing platforms

- **PIK.ba** (formerly OLX.ba, served at `olx.ba`) — DOMINANT; self-reported >3 million registered users and >4 million active listings (platform's own "O nama" page, 2026 — listing platform, unaudited)
- **Nekretnine.ba**, **Nađi stan** (`nadjistan.ba`), **Realitica** (BiH section)
- **Sasomange.ba**, **Pojdimo.ba**: ❌ DEPRECATED — dead on 2026-10-23 (no DNS record); verify current portals at PIK.ba

## Caveats unique to BA

- **DUAL-ENTITY STATE**: FBiH vs RS entity have **different cadastres, different taxes, different laws** — must specify entity throughout DD
- **Brčko District** separate (own cadastre at [Vlada Brčko Distrikta](https://www.bdcentral.net/)); **annual property tax 0.05 % – 1 %** of market value, rate adopted by the District Assembly by 31 Dec for the next year (art. 7 Zakon o porezu na nekretnine BD, 27/07, 52/18); **0.05 %** applied in 2024 and proposed for 2026; **no real estate transfer tax**; separate Direkcija za finansije BD + Poreska uprava BD authority *(2026 data, sources: PwC BA Individual + Corporate — other taxes, last reviewed 23 Sep 2026; Skupština BD 15 Dec 2025; Radio Brčko 31 Dec 2024; law text via advokat-prnjavorac.com — secondary)*
- **Currency BAM** pegged to EUR 1.95583 via currency board (1998+) — extremely stable
- **17% VAT** = one of the lower headline VAT rates in Europe
- **FBiH transfer tax up to 5 %** (cantonal; the buyer pays in some cantons, the seller in others) vs **RS entity and Brčko: NO transfer tax** — major divergence *(2026 data, PwC BA Corporate — other taxes + cantonal law texts)*
- **CGT on a property sale**: FBiH and Brčko **10 %**, but not on the seller's own home or after a 3-year hold; RS entity **13 %**, not after a 7-year hold (see `--tax`)
- **Mine contamination from Yugoslav Wars 1992-1995** — verify BHMAC for rural properties
- **2014 floods** Sava + Bosna rivers (massive event)
- **EU candidate Dec 2022** — slow reform pace
- **First-home VAT refund**: BiH state-level (covers FBiH + RS + Brčko) — **IN FORCE and claimable since 8 Jul 2026** (art. 54a ZPDV, Sl. glasnik BiH 20/25; UINO rulebook art. 105a, Sl. glasnik BiH 45/26); 40 m² + 15 m² per family-household member at 17 % VAT, capped; **restricted to adult BiH citizens with permanent BiH residence — a foreign buyer cannot claim it** *(not "FBiH House" — state-level under uino.gov.ba; 2026-08-07 verified)*
- **EU Reform Agenda** adopted by the BiH Council of Ministers 30 Sep 2025, approved by the European Commission 4 Dec 2025 (see Active fiscal incentives)
- **Banja Luka 1969** earthquake reference (M6.6)
- **Mostar UNESCO** Old Bridge area = strict construction
- **Foreign-buyer regime is RECIPROCITY-BASED** under **Zakon o stvarnim pravima FBiH (Sl. novine FBiH 66/13, 100/13, 32/19 — Constitutional Court decision)** art. 15 + RS counterpart. Reciprocity is **presumed**; the Federal Ministry of Justice publishes the list of countries **without** reciprocity by **31 January** each year (art. 15(2)). Its list of 27 Jul 2023 and supplement of 10 Nov 2023 mark e.g. **Switzerland, Lithuania**, Kuwait, Qatar, China, Sri Lanka and the UAE as no-reciprocity (no 2026 list found — rates/figures may have changed since). A person **born in BiH, or a descendant** of one, is not treated as a foreign person (art. 15(3)). **Agricultural land is barred** to foreign natural and legal persons unless a treaty says otherwise (art. 7 Zakon o poljoprivrednom zemljištu FBiH, Sl. novine FBiH 52/09) but can be inherited (art. 99); areas designated by law under art. 16 are barred too. **Inheritance** of other real estate is outside the reciprocity test (art. 15(2)). In Brčko the reciprocity list is published by the Pravosudna komisija BD. **Workaround**: incorporate a BA **d.o.o.** (domestic legal entity, not subject to reciprocity test) *(2026 data, sources: law texts on paragraf.ba + mpsv-hnz-k.ba, FMP reciprocity list of 27 Jul 2023 + 10 Nov 2023 supplement on fmp.gov.ba, BD property law on skupstinabd.ba; d.o.o. route per DLA Piper REALWORLD + Multilaw)*
- **Sarajevo Stari Grad** UNESCO buffer
- **War-damaged properties** require careful inspection

## Reddit / forum sources

- **r/bosnia**, **r/Sarajevo**, **r/BanjaLuka**
- **Balkan Insight**, **Sarajevo Times**
- **Banja Luka News**: ❌ DEPRECATED — no outlet found under that name (banjaluka.news has no DNS record, 2026-10-23); verify with Banja Luka city portals such as Banjaluka.net

## Verification authorities

| Authority | When to call |
|---|---|
| **FBiH**: zemljišnoknjižni ured (gruntovnica) of the općinski sud for title + FGU / općina cadastre (`katastar.ba`) for the parcel; **RS**: RGURS područna jedinica (katastar nepokretnosti) | Title verification (entity-specific) |
| **Notar** | RS: mandatory closing (notarial form, art. 57 Zakon o notarskoj službi u RS); FBiH: optional since Constitutional Court U-15/10 (2015) — a notary or the municipal court certifies the signatures |
| **Općina/opština** | Local tax + permits |
| **BHMAC** + općina/opština **Služba za civilnu zaštitu** | If rural — mine-situation check (BHMAC routes its records to the municipality) |
| **Poreska uprava** entity | Tax compliance |
| **Predstavnik etažnih vlasnika** + **upravnik** (FBiH cantonal laws, e.g. Sarajevo Canton) / **Zajednica etažnih vlasnika (ZEV)** (RS, Zakon o održavanju zgrada) | If apartment building — common reserve (zajednička rezerva), arrears, planned works |

## Source URL templates

| Source | URL pattern |
|---|---|
| FBiH cadastre (FGU) | `https://fgu.com.ba/en/` — refused connections on 2026-10-23 (still indexed; retry); FGU's public data portal is `https://katastar.ba/` |
| FBiH public portal | `https://katastar.ba/` |
| FBiH geoportal | `https://www.katastar.ba/geoportal` — login required (free katastar.ba account; redirected to a log-in notice on 2026-10-23) |
| RS entity cadastre | `https://www.rgurs.org/sr-lat` |
| RS entity eKatastar | `https://ekatastar.rgurs.org/` — public view is informational, not an official document |
| RS entity geoportal | `https://geoportal.rgurs.org/` |
| CBBH | `https://www.cbbh.ba/` |
| BHAS (statistics) | `https://bhas.gov.ba/` |
| BHMAC (mine action) | `https://www.bhmac.org/` |
| BHMAC mine situation | `https://www.bhmac.org/trenutna-minska-situacija-plan-izvjestaj/` |
| JP Ceste FBiH traffic counts | `https://jpcfbih.ba/bs/poslovanje/publikacije` |
| RHMZ RS (seismology, RS) | `https://rhmzrs.com/` |
| FHMZ BiH seismicity | `https://www.fhmzbih.gov.ba/latinica/SEIZMO/Skarakteristike.php` |
| Eurocode 8 seismic map (BAS EN 1998-1/NA:2018) | `https://eurokodovi.ba/` |
| FBiH Sava-basin flood maps | `https://www.voda.ba/mape-rizika` |
| Pik.ba (ex-OLX.ba, renamed June 2026) | `https://olx.ba/nekretnine` (`pik.ba/nekretnine` 301-redirects here) |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (BHAS / FZS / RZS RS new-dwelling prices + FGU registered sales, Q2 / H1 2026), traffic (JP Ceste FBiH 2025 counts; entity road operators), tax (DUAL ENTITY: FBiH cantonal property tax, BAM 0.5–3/m² range per PwC + cantonal transfer tax up to 5 % + 17 % VAT first-sale + 10 % CGT, not on the owner's home or after a 3-year hold; RS entity property tax up to 0.20 % of assessed market value + no transfer tax + 17 % VAT + 13 % CGT), rental (entity-specific), work (entity-specific), risks (Banja Luka 1969 + 2014 Sava+Bosna floods + BHMAC mine contamination + war-damage), mains.
**Last verified**: 2026-08-07 (`--tax` first-home VAT refund re-verified — in force 8 Jul 2026, foreign buyers ineligible; balance of the 2026-05-27 sweep unchanged). Tax tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).
**Confidence**: HIGH for BAM-EUR peg 1.95583 currency board (CBBH); HIGH for `--price` (official BHAS / FZS / RZS RS Q2 2026 new-dwelling prices + FGU RCN H1 2026 registered sales — city and municipality averages with small quarterly samples; the Bijeljina row is secondary), `--work` (2026 minimum-wage decisions, PDV threshold, d.o.o. capital and average wages from primary or legal-database texts) and the listing-platform list (PIK.ba dominance is self-reported), all three re-verified 2026-10-23; HIGH for entity divergence (FBiH 10 % / RS 8 % employment, 13 % capital incl. rental / Brčko 10 % PIT; FBiH cantonal transfer tax up to 5 % / RS and Brčko no transfer tax); HIGH for FBiH CGT 10 % except on the owner's home or a sale more than 3 years after acquisition (art. 20(9) + 32(4) Zakon o porezu na dohodak FBiH; the PwC/Eurofast 'not taxable' reading is superseded); HIGH for RS property tax up to 0.20 % of assessed market value (art. 8 Zakon o porezu na nepokretnosti RS); HIGH for mine contamination as ongoing diligence concern (BHMAC); HIGH for reciprocity regime under Zakon o stvarnim pravima FBiH + agricultural-land bar (law texts + FMP list); HIGH for the first-home VAT refund being in force since 8 Jul 2026 and closed to foreign buyers (art. 54a ZPDV + UINO rulebook art. 105a, Sl. glasnik BiH 20/25 + 45/26); MEDIUM for the d.o.o. workaround (law-firm guides only); MEDIUM for FBiH property tax (no FBiH-wide tax; only the Sarajevo Canton law read, the BAM 0.5–3/m² range is PwC's) and for the FBiH transfer-tax rate and payer by canton (four of ten cantons sourced, Tuzla from a secondary source); MEDIUM for Brčko property tax 0.05–1 % (PwC + law text via a secondary site — verify primary at bdcentral.net); MEDIUM for `--rental` (entity rates re-read in the law texts, Brčko rate and short-let lines not re-checked), `--risks` (wildfire, build-era, demining-certificate and Brčko notarial-form rows curated or unconfirmed) and `--traffic` (🔴 examples unconfirmed — no A1 motorway PGDS published); LOW for the est. ranges in `--mains` and Cost benchmarks (no primary price source) and for land-register / cadastre registration fees (not verified). Not re-checked: postcodes, RGURS unit counts, the official-language line and the Reddit communities.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-23 | 2026-10-23 refresh wave | Benchmark table rebuilt from BHAS Q2 2026, FZS Q2 2026, RZS RS Q2 2026 and FGU RCN H1 2026 releases (GPG figures superseded; Bijeljina row secondary); entity statistics offices and the FBiH / RS price registers added; Sasomange.ba and Pojdimo.ba ❌ DEPRECATED; Investropa not checked |
| `--work` | 2026-10-23 | 2026-10-23 refresh wave | 2026 minimum wages (FBiH flat, RS tiered by required education), PDV threshold BAM 50,000 → 100,000 (since 2 Dec 2023), d.o.o. capital set per entity, 2026 average wages from the statistics offices replace the unsourced medians; employment-service names corrected; Posao.ba ❌ DEPRECATED; LinkedIn BA not checked |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave | OLX.ba renamed PIK.ba (still served at olx.ba); Nađi stan and Realitica added; Sasomange.ba and Pojdimo.ba ❌ DEPRECATED; dominance rests on PIK.ba's own unaudited figures |

## Extension TODOs

- [ ] Cantonal transfer tax table (FBiH 10 cantons) — Sarajevo, Zenica-Doboj, Herzegovina-Neretva and Tuzla (secondary) cantons now in `--tax`; the other six open
- [ ] BHMAC demining verification flow per parcel
- [ ] War-damage assessment rubric
- [ ] FBiH cantonal property tax per canton (PwC range BAM 0.5–3/m²; only the Sarajevo Canton law read so far, see `--tax`)
- [x] RS entity property tax verification — CLOSED: up to 0.20 % of assessed market value, up to 0.10 % for premises used directly for production, rate adopted by each municipality / city by 31 January (art. 8 Zakon o porezu na nepokretnosti RS, Sl. glasnik RS 91/15, read 2026-11-03; see `--tax`)
- [ ] Brčko District separate process documentation
- [ ] CGT optimization: FBiH 10 % unless the owner's home or held more than 3 years (art. 20(9) + 32(4) Zakon o porezu na dohodak FBiH) vs RS entity 13 % (holding-period exemption in `--tax`)
- [x] 2024 VAT refund eligibility — CLOSED 2026-08-07: state-level (FBiH + RS + Brčko), in force 8 Jul 2026, adult BiH citizens with permanent BiH residence only — foreign buyers ineligible (see `--tax`)
- [ ] Sarajevo + Mostar UNESCO construction limits
- [ ] EU candidate accession reforms tracker

## Update history

- **2026-04-26** — Initial population (researched 2026-04)
- **2026-05-27** — Tier-1 corrections: first-home VAT refund recast as BiH state-level (not FBiH-only), PIT-by-entity table added, FBiH CGT source conflict surfaced
- **2026-05-29** — Anti-hallucination sweep: VAT wording corrected, est. labels on the mains and cost-benchmark ranges
- **2026-06-13** — BHAS URL re-pointed to bhas.gov.ba
- **2026-08-07** — First-home VAT refund re-verified: in force 8 Jul 2026, foreign buyers ineligible
- **2026-10-21** — December regwatch wave (run early): first-home VAT refund status, conditions and deadline, RS PIT split (8 % employment / 10 % self-employment / 13 % capital), personal allowances and rental tax rates re-verified against the law texts
- **2026-10-23** — Refresh wave (market, tax-legal, risk-infra); playbook-level date not re-stamped because `--tax`, `--rental`, `--risks` and `--mains` are not fully re-verified. Counts are changed / confirmed / unverifiable:
  - **Re-verified** (see Per-section verification): `--price` 20 / 4 / 1; `--work` 11 / 1 / 1; Common listing platforms 3 / 1 / 1
  - **Refreshed, not fully re-verified**: Country profile 5 / 7 / 6; `--rental` 0 / 4 / 4; Reddit / forum sources 1 / 2 / 3; `--tax` 12 / 22 / 6; Cost benchmarks 4 / 1 / 5; Active fiscal incentives 3 / 2 / 0; Caveats 5 / 6 / 1; `--traffic` 3 / 3 / 3; `--risks` 9 / 7 / 5; `--mains` 1 / 3 / 5; Verification authorities 4 / 0 / 2; Source URL templates 4 / 6 / 1 (all 10 URLs checked, verified primary URLs added)
  - Main changes: official BHAS / FZS / RZS RS Q2 2026 and FGU RCN H1 2026 price table replaces the GPG figures; OLX.ba → PIK.ba, with Sasomange.ba, Pojdimo.ba, Posao.ba and Banja Luka News ❌ DEPRECATED; 2026 minimum wages, PDV threshold BAM 100,000, d.o.o. capital per entity and 2026 average wages; euro-peg history, katastar.ba geoportal login and EU accession-negotiation status; FBiH CGT 10 % from the statute (the "not taxable" reading superseded), Brčko CGT 10 % and the RS holding-period exemption; no FBiH-wide property tax (Sarajevo Canton law minimums), RS property tax up to 0.20 %; FBiH transfer tax up to 5 % with the payer by canton; notary fees and buyer-side totals computed from the FBiH and RS tariffs; VAT-refund cap computed with the BHAS Q2 2026 average; IPA III and Reform Agenda status; reciprocity line rebuilt from the law texts and the FMP list; road operators renamed and the traffic bands calibrated on JP Ceste FBiH 2025 counts; 1969 Banja Luka quake toll 15 (not ~20) and south-east Herzegovina corrected to one of the highest seismic-hazard zones; 2014 recovery-needs figures and the Oct 2024 floods; BHMAC suspected hazardous area 774.69 km² (Jan 2026); notarial form optional in FBiH since U-15/10; energy-certificate duty per entity; FBiH title at the municipal-court gruntovnica
  - Follow-up consistency fixes: Status coverage and Confidence lines and four Extension TODOs (cantonal transfer tax, FBiH property tax, RS property tax, CGT) aligned with `--tax`
  - Not re-verified: postcodes, RGURS unit counts, the official-language line, fgu.com.ba reachability, Investropa, the Brčko rental rate and short-let lines, LinkedIn BA, the Reddit communities, land-register / cadastre fees, the transfer-tax rate and payer in six cantons, the art. 67 ZPDV fine, the 🔴 traffic examples, the est. work and mains cost rows, the demining-certificate and Brčko notarial-form rows, the Općina and Poreska uprava authority rows
