# Poland 🇵🇱 — Property Due-Diligence Playbook

ISO2: `pl`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits in `XX-XXX` format (`00-001` Warsaw centro, `30-001` Kraków, `80-001` Gdańsk, `50-001` Wrocław)
- **Admin levels**: 16 województwa (voivodeships) + 380 powiaty (314 powiaty + 66 miasta na prawach powiatu) + 2,479 gminy (2025 data, source GUS Podział administracyjny Polski, as of 1 Jan 2025 — rates/figures may have changed since)
- **Currency**: **PLN (Polish złoty)** — 1 EUR = 4.3685 PLN (NBP table A mid-rate, 22 Oct 2026); 12-month NBP range 4.2009 (28 Jan 2026) – 4.3900 (24 Sep 2026) (2026 data, source NBP API table A) (volatile)
- **Languages**: Polish (official); Kashubian, German, Belarusian (regional minorities)
- **Cadastre**:
  - **EKW (Elektroniczne Księgi Wieczyste, electronic land register)**: `https://ekw.ms.gov.pl/`
  - **Geoportal2** (national geoportal): `https://www.geoportal.gov.pl/`
  - **EGiB (Ewidencja Gruntów i Budynków)**: cadastre, accessed via gmina/powiat geoportals
  - **ZSIN (Zintegrowany System Informacji o Nieruchomościach)**: integrates EKW + EGiB
- **Identifier**: numer KW (e.g., `WA1M/12345678/9` — court code + sequence + check digit)
- **Ownership types**:
  - **Własność** (full ownership)
  - **Użytkowanie wieczyste** (perpetual usufruct — converted by law into ownership on 1 Jan 2019 for land built up for housing: single-family houses, or multi-family buildings where ≥50% of units are residential, plus ancillary structures (Ustawa z 20.07.2018, Dz.U. 2018 poz. 1716, art. 1); still exists for other land)
  - **Spółdzielcze prawo własnościowe / lokatorskie** (cooperative ownership)
  - **Najem** (rental)
- **EU member since 2004**; not in eurozone (PLN remains)

## Section: `--price`

### Primary sources

- **NBP BaRN database** (Baza cen nieruchomości mieszkaniowych, III kw. 2006 – II kw. 2026; source NBP, archived 2026-09-16): `https://nbp.pl/publikacje/cykliczne-materialy-analityczne-nbp/rynek-nieruchomosci/informacja-kwartalna/` — data file `https://static.nbp.pl/dane/rynek-nieruchomosci/ceny_mieszkan.xlsx` (offer and transaction prices per m² of flats, primary and secondary market, 16 voivodeship capitals + Gdynia, incl. VAT; secondary-market transaction series revised back in II kw. 2026 after BaRN was merged with AMRON, CRCM and RCN data)
  - Quarterly residential price reports — National Bank of Poland authoritative data
- **AMRON-SARFiN** (Polish Banking Association): `https://amron.pl/raporty/`
  - Bank valuation + transaction + mortgage finance data; quarterly
- **GUS (Główny Urząd Statystyczny)**: `https://stat.gov.pl/` — national statistics
- **Otodom Analytics**: `https://analytics.otodom.pl/en` — combines NBP/GUS/BIK/AMRON-SARFiN; gated for agents/developers
- **EKW** for individual title lookup (read-only by KW number, paid certified outprints)
- **Geoportal2** for parcel maps + zoning

### Listing platforms

- **Otodom** (Grupa OLX) — DOMINANT: OLX Group property sites (Otodom + Obido + OLX Nieruchomości) 6.70M real users, excl. mobile-app users (2023 data, Gemius Mediapanel April 2023 as cited by Otodom Analytics — rates/figures may have changed since): `https://www.otodom.pl/`
- **Morizon Group** (Morizon + Gratka + Noweinwestycje.pl; Morizon + Gratka run by Grupa Morizon-Gratka Sp. z o.o.) — 2.25M real users (2023 data, Gemius Mediapanel April 2023 via Otodom Analytics — rates/figures may have changed since): `https://www.morizon.pl/`
- **Nieruchomosci-online** — 1.94M real users (2023 data, Gemius Mediapanel April 2023 via Otodom Analytics — rates/figures may have changed since): `https://nieruchomosci-online.pl/`
- **Domiporta** — 1.19M real users (2023 data, Gemius Mediapanel April 2023 via Otodom Analytics — rates/figures may have changed since): `https://www.domiporta.pl/`
- **OLX Nieruchomości** within OLX Group — classifieds category for flats, houses and plots (listing platform ⚠️, source olx.pl, archived 2026-10-25): `https://www.olx.pl/nieruchomosci/`

### 2025 price benchmarks (big-city PLN/m² rows est., calibrated against the GUS 2025 and NBP II kw. 2026 city figures below; smaller-city and rural-east PLN/m² computed from GUS 2025 powiat medians; single-family totals est.)

| Region | Avg PLN/m² (apt) | Avg total (single-family, est.) |
|---|---:|---:|
| **Warszawa centrum** | 17,000–25,000+ | 1,800,000–4,500,000+ |
| **Warszawa periphery** | 12,000–17,000 | 1,200,000–2,200,000 |
| **Kraków centrum** | 14,000–20,000 | 1,400,000–2,800,000 |
| **Kraków periphery** | 10,000–14,000 | 1,000,000–1,800,000 |
| **Wrocław** | 11,000–15,000 | 1,000,000–1,800,000 |
| **Gdańsk / Gdynia / Sopot** | 12,000–18,000 | 1,100,000–2,200,000 |
| **Poznań** | 10,000–14,000 | 950,000–1,600,000 |
| **Łódź** | 7,500–11,000 | 700,000–1,200,000 |
| **Smaller cities** (other city powiats) | 5,771–7,499 (GUS 2025 quartiles, see below) | 550,000–1,000,000 |
| **Rural eastern PL** (land powiats incl. towns, 5 eastern voivodeships) | 4,905–6,787 (GUS 2025 quartiles, see below) | 250,000–550,000 |

GUS anchor — median price per m² of dwellings sold in market transactions, whole city (2025 data, source GUS BDL `https://bdl.stat.gov.pl/`, subject P3787; primary-market prices include VAT): primary + secondary — Warszawa 15,449 · Kraków 14,561 · Gdańsk 12,523 · Wrocław 12,426 · Gdynia 11,659 · Poznań 11,291 · Łódź 8,735 · Sopot 19,384 · Poland 8,774 PLN/m²; secondary market only — Warszawa 15,885 · Kraków 14,368 · Gdańsk 12,839 · Wrocław 12,219 · Poznań 10,782 · Łódź 7,709 · Poland 7,724 PLN/m². These are city-wide medians, not district- or parcel-level. GUS P3787 has no centrum/periphery split and covers flats only, so the table's district splits and single-family totals are est. Three city medians fall outside the table's est. ranges: Kraków (14,561) is above the Kraków periphery range (10,000–14,000); Gdynia (11,659) is below and Sopot (19,384) above the Gdańsk / Gdynia / Sopot range (12,000–18,000). For these cities, use the GUS median over the table.

Computed rows — GUS P3787 all-market medians per powiat (2025 data, source GUS Dziedzinowa Baza Wiedzy API `https://api-dbw.stat.gov.pl/`, variable 307, section 485; same series as BDL — the national 8,774 and secondary-market 7,724 match): **Smaller cities** = quartiles of the 46 city-powiat (miasto na prawach powiatu) medians, excluding Warszawa, Kraków, Łódź, Wrocław, Poznań, Gdańsk, Gdynia, Sopot, Szczecin, Bydgoszcz, Toruń, Lublin, Białystok, Katowice, Kielce, Olsztyn, Opole, Rzeszów, Zielona Góra and Gorzów Wielkopolski — 25th percentile 5,771 · median 6,688.5 · 75th percentile 7,499; full range 4,391 (Bytom) – 11,680 (Świnoujście). **Rural eastern PL** = quartiles of the 87 land-powiat (powiat ziemski) medians in lubelskie, podkarpackie, podlaskie, świętokrzyskie and warmińsko-mazurskie — 25th percentile 4,905 · median 5,882 · 75th percentile 6,787; full range 3,641 (powiat chełmski) – 8,034 (powiat augustowski). Quartiles use the exclusive method. Land powiats include the towns that are not city powiats. Voivodeship-wide all-market medians: lubelskie 8,488 · podlaskie 8,361 · podkarpackie 7,752 · świętokrzyskie 7,500 · warmińsko-mazurskie 6,625 PLN/m². These are powiat-level medians for flats, not prices for a village, a house or a parcel.

NBP cross-check — average transaction price per m² of flats, II kw. 2026 (notations March–May 2026; flats in multi-family buildings within city limits, incl. VAT; source NBP BaRN `https://static.nbp.pl/dane/rynek-nieruchomosci/ceny_mieszkan.xlsx`): secondary market — Warszawa 16,723 · Kraków 14,792 · Gdańsk 14,035 · Wrocław 12,590 · Gdynia 12,267 · Poznań 10,891 · Łódź 8,020 · 10 other cities (Białystok, Bydgoszcz, Katowice, Kielce, Lublin, Olsztyn, Opole, Rzeszów, Szczecin, Zielona Góra; stock-weighted) 9,125; primary market — Warszawa 16,783 · Kraków 15,923 · Gdańsk 14,491 · Wrocław 14,312 · Gdynia 12,887 (district-population-weighted) · Poznań 12,766 · Łódź 9,945 · 10 other cities 11,037 PLN/m². City-wide averages, not district- or parcel-level; BaRN does not cover Sopot. In both markets each of the seven city averages lies within the table's span for that city: Warszawa's in the periphery range, Kraków's in the centrum range and above the periphery range.

Single-family totals are est. carried over from the initial 2026-04 research (inputs not recorded); GUS and NBP BaRN publish no house prices by city or district (BaRN covers flats in multi-family buildings only). National cross-check only: mean value per sale of built-up land (nieruchomości gruntowe zabudowane: land with a house or another building; the GUS RCN table gives no split by building use, so this is not a house-only figure) ~PLN 809,000 (computed: 75,733 mln zł / 93,561 transactions; 2025 preliminary data from the Rejestr Cen Nieruchomości, source GUS Obrót nieruchomościami w 2025 r., 8 Jul 2026, `https://stat.gov.pl/obszary-tematyczne/infrastruktura-komunalna-nieruchomosci/nieruchomosci-budynki-infrastruktura-komunalna/obrot-nieruchomosciami-w-2025-r-,8,9.html`). Verify a specific house against recorded sale prices in the Rejestr Cen Nieruchomości, the public register of notarial-deed prices kept by the starosta (source GUS glossary `https://stat.gov.pl/metainformacje/slownik-pojec/pojecia-stosowane-w-statystyce-publicznej/4491,pojecie.html`).

### Compute

1. PLN/m² = price / **powierzchnia użytkowa** (usable area). Developer contracts and reservation agreements signed from 13 Feb 2026 must price the unit as usable m² × price per m², with the area measured under the Polish Standard on floor-area indices in force on the date of the building-permit application or building notification (art. 5a; 2026 data, source ustawa deweloperska, consolidated text Dz.U. 2026 poz. 880); usually PN-ISO 9836, 2022 version. Whether balconies, loggias, terraces and internal stairs then count is disputed: UOKiK, in a position agreed with MRiT, reads art. 5a with the 2020 building-design regulation, so balconies and stairs stay out, while lawyers warn the literal wording could bring them in, so check how the contract defines the area (prawo.pl Mar 2026 ⚠️ secondary). Art. 5a covers sales by a developer and first sales by another business, so on a private resale ask how the area was measured
2. **Sprawdź KW** — read all 4 sections of land register (I-O property, I-Sp rights, II ownership, III encumbrances, IV mortgage)
3. **Convert to EUR** at current FX (PLN volatile)
4. **Real Estate Reports** from NBP quarterly for area trend

### Key terms

- KW (Księga wieczysta) = land register
- Własność = ownership
- Użytkowanie wieczyste = perpetual usufruct (legacy)
- Spółdzielnia mieszkaniowa = housing cooperative
- Wspólnota mieszkaniowa = HOA for apartment building
- Świadectwo CEN = energy certificate

---

## Section: `--traffic`

### Sources

- **GDDKiA** (Generalna Dyrekcja Dróg Krajowych i Autostrad): `https://www.gov.pl/web/gddkia` — national roads
- **GPR (Generalny Pomiar Ruchu)** — five-year cycle since 1965; latest **GPR 2025** results (SDRR tables + maps for national and voivodeship roads): `https://www.gov.pl/web/gddkia/generalny-pomiar-ruchu-2025` (2025 data, source GDDKiA 'Ruch Drogowy 2025')
- **Per-województwo road authority** for regional roads
- **Per-gmina** for local

### Key term

**SDR (Średni Dobowy Ruch)** = AADT-equivalent; GPR publishes it as **SDRR** (średni dobowy ruch roczny, motor vehicles/day).

GPR 2025 calibration (2025 data, source GDDKiA 'Ruch Drogowy 2025'): national-road network average **14,870 v/d** (about +10% vs 13,567 in GPR 2020/21); international national roads 30,220; other national roads 8,645; motorways (A) **38,514**; expressways (S) **26,928**; GP-class 9,356; G-class 5,686.

### Verdict bands

- 🟢 < 1,500 v/d (rural roads, residential streets)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (urban arterial, voivodeship roads)
- 🔴 > 35,000 v/d (motorway, expressway, Warsaw arterials)

---

## Section: `--tax`

### Annual property tax — Podatek od nieruchomości (PoN)

#### 2025 reform (CONFIRMED)

**Effective 1 January 2025**: new statutory definitions of *budynek* (building) and *budowla* (structure) in art. 1a ust. 1 pkt 1–2 of the *Ustawa o podatkach i opłatach lokalnych*, with Annex 4 listing 28 categories of budowle; introduced by ustawa z 19.11.2024, Dz.U. 2024 poz. 1757, in force 1 Jan 2025 (2025 data, source api.sejm.gov.pl ELI + consolidated text Dz.U. 2025 poz. 707)
- Triggered by Constitutional Court judgment of 4 July 2023, SK 14/21: the *budowla* definition (art. 1a ust. 1 pkt 2) breached Constitution arts 84 and 217 and lost force 18 months after publication (source trybunal.gov.pl)
- Decoupled from Building Law — both require "construction works" basis
- Sources: Wolters Kluwer, EY, TPA, Grant Thornton confirm

#### Max rates 2026 and 2027 (art. 5 ust. 1, Ministry of Finance obwieszczenia)

| Category | 2026 max | 2027 max |
|---|---:|---:|
| **Residential building** (per m² usable area) | **1.25 PLN/m²/yr** | **1.29 PLN/m²/yr** |
| **Other land** (*grunty pozostałe*, incl. residential plots) | **0.77 PLN/m²/yr** | **0.80 PLN/m²/yr** |
| **Business-use building** | **35.53 PLN/m²/yr** | **36.49 PLN/m²/yr** |
| **Business-use land** | **1.45 PLN/m²/yr** | **1.49 PLN/m²/yr** |
| **Other building** | 12.00 PLN/m²/yr | 12.33 PLN/m²/yr |

- Sources: 2026 = Obwieszczenie MFiG of 1 Aug 2025 (M.P. 2025 poz. 726); 2027 = Obwieszczenie MFiG of 23 Jul 2026 (M.P. 2026 poz. 741, published 28 Jul 2026, applies from 1 Jan 2027) (2026 data, source monitorpolski.gov.pl)
- Indexation, computed from the gazettes: business building 34.00 (2025, M.P. 2024 poz. 716) → 35.53 (2026) = +4.5%; 35.53 → 36.49 (2027) = +2.7%
- Each gmina sets its actual rate by uchwała before year-end, within the ceiling. Average 2026 rates in gminas that do not differentiate rates: residential building 1.00 PLN/m² (1.16 in cities with powiat rights), other land 0.54 PLN/m² (2026 data, source MF "Wysokość stawek w opodatkowaniu nieruchomości w 2026 r.", podatki.gov.pl)
- Annual bill, computed: 50 m² flat = 50 × 1.25 = 62.50 PLN at the 2026 ceiling (64.50 PLN at the 2027 ceiling; 50.00 PLN at the 2026 average), plus its share of the plot at ≤0.77 PLN/m²; 150 m² house on a 1,000 m² plot = 150 × 1.25 + 1,000 × 0.77 = 957.50 PLN at the 2026 ceilings (993.50 PLN in 2027)

### Transaction taxes

- **PCC (Podatek od czynności cywilnoprawnych)**: **2%** on resale (paid by buyer; art. 7 ust. 1 pkt 1 lit. a + art. 4 pkt 1) (2026 data, source consolidated text Dz.U. 2026 poz. 191)
- **PCC 6% bulk-buyer rate (od 1.01.2024)**: 6% PCC on the **6th+ lokal mieszkalny on the same nieruchomość gruntowa** in a VAT-taxed (developer) sale, art. 7a (joint-ownership counts toward threshold; rate **stacks with VAT** — exception to the no-PCC-with-VAT rule in art. 2 pkt 4 lit. a). Source: Ustawa z 26.05.2023, **Dz.U. 2023 poz. 1463**, art. 4 pkt 1–3 in force 1 Jan 2024 (2026 data, source consolidated text Dz.U. 2026 poz. 191)
- **First-home exemption since 31 August 2023** (art. 9 pkt 17; PCC-taxed, i.e. secondary-market, sales only):
  - Ownership of a flat (*lokal mieszkalny*) or single-family house, or a *spółdzielcze własnościowe prawo* to either
  - Buyer(s) must be natural persons who have never held any such right or a share in one, except an inherited share of ≤50%
  - Joint purchase (e.g. spouses): the statute requires every buyer to meet the condition (2026 data, source consolidated text Dz.U. 2026 poz. 191)
- **VAT (new build)**: **8%** for flats ≤150 m² and single-family houses ≤300 m²; above the limit, 23% applies only to the share of the price for the floor area over the limit (art. 41 ust. 12b–12c + art. 146ef ustawy o VAT); 23% other RE (2026 data, source consolidated text Dz.U. 2026 poz. 1263)
- **Notariusz** fees: maximum taxa = graduated scale (§ 3), halved for the sale of a flat, a house or a building plot (§ 6 pkt 17–19), + 23% VAT; computed for a PLN 600,000 flat: (1,010 + 0.4% × 540,000) ÷ 2 = 1,585 PLN + 23% VAT = 1,949.55 PLN ≈ 0.33% of price, plus fees for wypisy (copies); the taxa is a maximum, negotiable downward (source Rozporządzenie MS z 28.06.2004, consolidated text Dz.U. 2024 poz. 1566)
- **Sąd (court) fees**: 200 PLN per KW entry of ownership and 200 PLN per mortgage entry (art. 42 ust. 1); 100 PLN to open a new KW, e.g. for a newly separated flat (art. 44 ust. 1 pkt 1) (2025 data, source ustawa o kosztach sądowych, consolidated text Dz.U. 2025 poz. 1228)

### Total transaction cost (buyer side)

Computed for a PLN 600,000 flat, excluding agent commission (inputs: PCC 2%, notary max taxa 1,949.55 PLN incl. VAT, notary max fee for filing the KW application 369 PLN incl. VAT from 5 Nov 2026, KW ownership entry 200 PLN; wypisy extra):
- **First home, resale (PCC-exempt)**: 1,949.55 + 369 + 200 = 2,518.55 PLN ≈ 0.4%
- **Resale, second home / BTL**: 12,000 + 1,949.55 + 369 + 200 = 14,518.55 PLN ≈ 2.4%
- **New build (developer)**: 8% VAT included in the price; no PCC (VAT-taxed sale; 6% PCC only on a 6th+ unit, see above); one or two half-scale notarial deeds (umowa deweloperska + transfer) + 369 PLN KW filing + 300 PLN court fees (new KW 100 + entry 200) ≈ 0.4–0.8%
- Add est. 2–3% agent commission when an agent is used (market practice, negotiable; no official source) and 200 PLN for the KW mortgage entry if financed

### Capital gains

- **PIT 19%** on the gain if sold within **5 years** from the end of the calendar year of acquisition (art. 10 ust. 1 pkt 8, art. 30e) (2026 data, source consolidated PIT act Dz.U. 2026 poz. 592)
- **Exempt after 5 years**
- **Exempt** pro rata to the proceeds spent on own housing within 3 years from the end of the tax year of sale (art. 21 ust. 1 pkt 131)
- Inheritance + gifts (*podatek od spadków i darowizn*): spouse, descendants, ascendants, stepchildren, siblings, stepfather and stepmother are fully exempt if the acquisition is reported to the urząd skarbowy within 6 months (art. 4a); otherwise Group I tax-free amount PLN 36,120 per donor (5-year aggregation), then 3% / 5% / 7% (art. 9 ust. 1, art. 15) (2026 data, source consolidated text Dz.U. 2026 poz. 478)

### Future risk

- **PoN reform definitions** still being litigated case-by-case
- **Użytkowanie wieczyste conversion** ongoing for residential
- **EU 2024/1028 short-let implementing act** (amendment of the ustawa o usługach hotelarskich, Sejm print 2865): passed by the Sejm on 8 Oct 2026 (407–24–9), amended by the Senate (resolution of 6 Nov 2026 with amendments, Sejm print 3341) and back before the Sejm, not in force. Sejm-passed text: Centralny Wykaz Turystycznych Obiektów Noclegowych with an ID number required in listings, fines up to PLN 50,000 (art. 45e–45g); most provisions apply 14 days after publication in Dz.U., wspólnota/spółdzielnia bans and gmina STR zones from 1 Jan 2028 (art. 8). No 15 Oct 2026 deadline in the text (2026 data, sources api.sejm.gov.pl process 2865 + text sent to the Senate; sejm.gov.pl process 2865, read 2026-11-11; MSiT 12.10.2026)
- **Opłata miejscowa reform from 1 Jan 2027** (ustawa z 18.09.2026, Dz.U. 2026 poz. 1354): per-night fee on accommodation services in hotel-type and other accommodation facilities (art. 35 ust. 1–3 ustawy o usługach hotelarskich), collected by the host as płatnik with a monthly return by the 15th and a 10% collection fee; caps 5.00 PLN/night (landscape localities) / 5.50 PLN/night (spa-protection areas), opłata uzdrowiskowa 6.86 PLN/night; stays over 29 consecutive nights exempt (2026 data, source Dz.U. 2026 poz. 1354)

---

## Section: `--rental`

### Long-term residential

- **Najem instytucjonalny** (institutional lease) — landlord-friendly fixed-term form for landlords letting as a business (since 11 Sep 2017, Ustawa o Krajowym Zasobie Nieruchomości, Dz.U. 2017 poz. 1529; art. 19f–19j ustawy o ochronie praw lokatorów)
- **Najem okazjonalny** (occasional lease) — owner is a natural person not letting as a business; fixed term ≤10 years; tenant's notarial submission to eviction attached (art. 19a ustawy o ochronie praw lokatorów)
- **Najem standardowy** (standard) — Civil Code; tenant-protected
- Rent increases (standard leases only): written notice, ≥3 months unless a longer term is agreed, served for the end of a calendar month (art. 8a ust. 1–3). An increase that takes annual rent above 3% of the dwelling's wartość odtworzeniowa, or starts from a level already above it, is allowed only in justified cases: cost recovery plus capital return and a fair profit (art. 8a ust. 4a–4b), or an increase no higher than the prior year's average CPI published by the Prezes GUS (art. 8a ust. 4e). On the tenant's written request the landlord must give the cause and calculation in writing within 14 days, or the increase is void (art. 8a ust. 4); within 2 months the tenant may refuse it in writing (ending the lease at the end of the notice period) or, for an increase above the 3% threshold, challenge it in court (art. 8a ust. 5). Art. 8a does not apply to najem okazjonalny (art. 19e) or najem instytucjonalny (art. 19j) (source: Ustawa o ochronie praw lokatorów, tekst jedn. Dz.U. 2023 poz. 725; latest amending act listed in ELI: Dz.U. 2022 poz. 2456)

### Short-let (Najem krótkoterminowy)

**EU 2024/1028 implementing act — status (as of 2026-10-23)**:
- NOT yet in force: the government bill amending the ustawa o usługach hotelarskich (adopted by the Rada Ministrów 14 Jul 2026; Sejm druk 2865, received 21 Jul 2026) passed the Sejm on 8 Oct 2026 (407 for / 24 against / 9 abstaining) and went to the Senate, which adopted amendments on 6 Nov 2026 (93 for, 0 against, 1 abstaining; PAP via Bankier.pl, not verified to a primary source — 2026-11-11), so the act returns to the Sejm; it is not in Dz.U. 2026 up to poz. 1480 (promulgated 9 Nov 2026) (2026 data, source api.sejm.gov.pl process 2865 + ELI Dz.U. 2026 list + MSiT 14.07.2026 and 12.10.2026)
- Separate MPs' bill o najmie krótkoterminowym (druk 2353, dated 3 Dec 2025): first reading 17 Apr 2026, referred to committee, not passed (2026 data, source api.sejm.gov.pl process 2353)
- Sejm-passed text (the Senate adopted amendments on 6 Nov 2026, Sejm print 3341; the Sejm has yet to vote on them): usługi hotelarskie = lets shorter than 30 days to one client; public **Centralny Wykaz Turystycznych Obiektów Noclegowych (CWTON)** on the tourism minister's website, fed by gminas (art. 42 ust. 4–5); the host must give the platform the CWTON ID before listing (art. 39 ust. 3a) and state it in the house rules (art. 44 ust. 3)
- **Fines up to PLN 50,000** (bill text, not yet law): operating without an ewidencja entry (art. 45e); offers without the CWTON ID (art. 45f ust. 2); platforms breaching Reg 2024/1028 arts 6, 7(2)–(3) or 9, per breach, after an unanswered 7-day notice (art. 45g)
- Struck off the ewidencja after 3 safety / public-order violations within 6 months; no re-registration for 1 year (art. 41b)
- Timing (art. 8): in force 14 days after Dz.U. publication; gminas move existing data to CWTON within 3 months, and existing ewidencja entries must be adapted within 4 months or lapse (arts 5–6); from **1 Jan 2028** wspólnoty / spółdzielnie may ban STR in their property (spółdzielnia: >50% of those entitled to vote; the host then has 6 months to stop; art. 39b) and rady gmin may set STR exclusion zones (art. 44b: ≥21-day consultation, in force ≥6 months after publication)
- The passed text contains no 15 Oct 2026 deadline; the CWTON ID for non-categorised accommodation exists only once the act is in force

#### Local rules

- **All gminas (incl. Kraków + Warsaw)**: before letting a flat as an *inny obiekt*, a przedsiębiorca (or farmer) must notify the gmina's ewidencja kept by the wójt / burmistrz / prezydent miasta (art. 38 ust. 3 + art. 39 ust. 3 ustawy o usługach hotelarskich, tekst jedn. Dz.U. 2023 poz. 1944) — a national rule, not city-specific
- **Kraków uchwała krajobrazowa** (advertising/landscape ordinance) — broader than STR-specific
- **Sopot, Gdańsk, Wrocław**: tightening rules

### Tax on rental

- **Najem prywatny (since 1 stycznia 2023)**: ryczałt is the **only allowed form** — **8.5%** up to PLN 100,000/yr (single) or PLN 200,000/yr (spouses with joint property who elect in writing that one of them taxes the whole revenue, art. 12 ust. 6 + 13); **12.5%** above; **no deduction of costs** and no tax-free amount; the threshold runs separately from any business revenue (art. 12 ust. 14) (2026 data, source: Ustawa o zryczałtowanym podatku dochodowym, tekst jedn. Dz.U. 2025 poz. 843, art. 2 ust. 1a + art. 12 ust. 1 pkt 4). PIT progressive scale **NO LONGER available** for najem prywatny — only if rental conducted as działalność gospodarcza (separate ZUS + accounting).
- **Kasa fiskalna** (cash register): exempt while sales to private individuals stay ≤ **PLN 20,000/yr** (prior-year test; pro rata for starters); the exemption regime runs to 31 Dec 2027 (2026 data, source: Rozporządzenie MF z 17.12.2024, Dz.U. 2024 poz. 1902, § 3 ust. 1)
- **VAT 8%** on short-term accommodation services (PKWiU 55: załącznik nr 3 + art. 146ef ustawy o VAT) once VAT-registered; the small-business exemption ends above **PLN 240,000/yr** sales (raised from PLN 200,000 on 1 Jan 2026, art. 113 ust. 1 as amended by Dz.U. 2025 poz. 896) (2026 data)

---

## Section: `--work=<profession>`

### Sources

- **Pracuj.pl** — self-described "lider na rynku cyfrowej rekrutacji" (operator claim, grupapracuj.pl, 2026): `https://www.pracuj.pl/`
- **OLX Praca**, **Indeed.pl**, **LinkedIn PL**
- **Urząd Pracy** (employment office) per powiat

### Self-employment

- **JDG (Jednoosobowa działalność gospodarcza)** — sole trader
  - **Składki ZUS** (social insurance, 2026): **PLN 1,926.76/mo** on the minimum full base of PLN 5,652, incl. voluntary sickness + FP/FS (PLN 1,788.29 without sickness); preferential base (30% of minimum wage): PLN 456.18/mo; income-based **Mały ZUS Plus** in between; składka zdrowotna on top (ryczałt filers with revenue ≤ PLN 60,000: PLN 498.35/mo) (2026 data, source ZUS "Wysokość składek" page of 2 Feb 2026)
  - **PIT 12%/32%** progressive (12% up to PLN 120,000 minus a PLN 3,600 tax-reducing amount, 32% above) OR **podatek liniowy 19%** OR **ryczałt** (flat-rate by category) (2026 data, source Ustawa o PIT, tekst jedn. Dz.U. 2026 poz. 592, art. 27 ust. 1 + art. 30c ust. 1)
- **Sp. z o.o.** (limited): min 5,000 PLN capital (2026 data, source KSH art. 154 § 1, tekst jedn. Dz.U. 2024 poz. 18)
- **VAT registration**: mandatory once sales exceed **PLN 240,000/yr** (subjective exemption limit raised from PLN 200,000 on 1 Jan 2026, art. 113 ust. 1 ustawy o VAT as amended by Dz.U. 2025 poz. 896; some sectors mandatory regardless of turnover)

### Salary benchmarks (2025)

- Average monthly gross wage (averages, not medians; 2025 data, source GUS BDL `https://bdl.stat.gov.pl/`, subject P2497, powiat level):
  - Warszawa: PLN 11,677.57
  - Kraków PLN 11,404.02 · Gdańsk PLN 10,955.78 · Poznań PLN 10,284.81 · Wrocław PLN 10,147.90
  - Łódź PLN 9,367.00 · Poland PLN 9,371.11 · lowest powiat (krotoszyński) PLN 6,463.65
- **Minimum wage (płaca minimalna)**: **PLN 4,806** gross monthly / PLN 31.40 hourly in 2026 (Dz.U. 2025 poz. 1242); **PLN 4,950** / PLN 32.30 from 1 Jan 2027 (Dz.U. 2026 poz. 1213)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Wody Polskie** (waters management) | `https://www.gov.pl/web/wody-polskie` | Flood + water management |
| **ISOK flood maps** | `https://wody.isok.gov.pl/` | Flood hazard maps |
| **IMGW** (meteorology + hydrology) | `https://www.imgw.pl/` | Weather, climate |
| **PIG-PIB** (Geological Institute) | `https://www.pgi.gov.pl/` | Geology, mining subsidence |
| **PAA (Państwowa Agencja Atomistyki)** | `https://monitoring.paa.gov.pl/maps-portal/` | Current radiation situation: gamma dose-rate map (per PAA, `https://www.gov.pl/web/paa`) — not a radon map; radon maps are on Poznaj Radon (below) |
| **Państwowa Inspekcja Sanitarna** (Sanepid / GIS) | `https://www.gov.pl/web/gis` | Radon: GIS leads identification of high-radon areas (Prawo atomowe art. 23e) |
| **GIOŚ** (env protection) | `https://www.gov.pl/web/gios` | Air, water, soil quality |
| **Polski Alarm Smogowy** | `https://polskialarmsmogowy.pl/` | Air-quality rankings built on GIOŚ data (NGO — secondary) |
| **GIOŚ air-quality portal** | `https://powietrze.gios.gov.pl/pjp/current` | Official station measurements |
| **Airly** | `https://airly.org/map/` | Live PM2.5 data (private sensor network — secondary) |
| **Czyste Powietrze** | `https://czystepowietrze.gov.pl/` | Anti-smog programme |
| **Baza Azbestowa** | `https://bazaazbestowa.gov.pl/` | Asbestos legacy register |

### Specific risks

- **Floods** — major risk:
  - **Wisła (Vistula), Odra (Oder), Warta** — the rivers where significant floods occurred most often in 1946–2017, with floods more frequent on the mountain left-bank tributaries of the Odra and the Carpathian tributaries of the Wisła (source PGW Wody Polskie, WORP 3rd-cycle report prepared by IMGW-PIB, 20 Mar 2025)
  - **Storm Boris September 2024** (flood 13 Sep–4 Oct 2024): flooding mainly in Dolnośląskie (incl. Kłodzko), Opolskie (incl. Nysa), Śląskie and Lubuskie, and in small parts of Małopolskie, Zachodniopomorskie and Wielkopolskie (source PGW Wody Polskie, WORP 3rd-cycle annex 7 'Powódź we wrześniu 2024', 24 Jan 2025); the flood-recovery special rules cover listed gminas in Dolnośląskie, Lubuskie, Opolskie and Śląskie only (consolidated text Dz.U. 2026 poz. 948, 15 Jul 2026)
    - 9 dead (Polish Police count as of 29 Sep 2024, via Demagog fact-check); ~57,000 directly affected and 6,544 evacuated as of 19 Sep 2024 (Prime Minister's Office figures, via IFRC DREF MDRPL003)
    - State of natural disaster declared 16 Sep 2024 (Rozporządzenie Rady Ministrów, Dz.U. 2024 poz. 1365) over parts of Dolnośląskie, Opolskie and Śląskie; later extended to part of Lubuskie (consolidated text of 22 Sep 2024, Dz.U. 2024 poz. 1395) — Małopolskie was not in the declared zone
  - Historic references: July–August 1997 ("Powódź tysiąclecia") and May–June 2010 are both listed among the catastrophic river floods of the Odra and Wisła basins in 1946–2017 (source PGW Wody Polskie, WORP 3rd-cycle report, 20 Mar 2025)
- **Smog / PM2.5** — major Polish issue:
  - National annual-mean PM10 concentration **+7% in 2024 vs 2023** (2024 data, source Polski Alarm Smogowy ranking on GIOŚ measurements, via Gramwzielone.pl 20 Oct 2025 — secondary) — rates/figures may have changed since; in 2025 more areas again exceeded PM10/PM2.5 limits (2025 data, source PAS comparison of GIOŚ annual assessments, via Gramwzielone.pl 18 Jun 2026 — secondary)
  - Emissions fell while concentrations rose: national PM10 emissions −7% and PM2.5 −9% in 2024 vs 2023 (2024 data, source KOBiZE 'Krajowy bilans emisji … 1990–2024', 2026) — rates/figures may have changed since
  - Worst towns (PAS rankings on GIOŚ data — secondary): Łódzkie (10 of the top-30 PM10 towns, 2024); Dolnośląskie (Nowa Ruda — #1 in all three categories for 2024; 91 PM10 exceedance days in 2025 vs 73 in 2024); Opolskie (Zdzieszowice — #1 for benzo(a)pyrene in 2025 at 900% of the limit); Małopolskie (Nowy Targ, Sucha Beskidzka); Śląskie (Żywiec, Myszków)
  - **~2.5M "kopciuchy"** (non-compliant solid-fuel boilers) still in use (2026 estimate, source Polski Alarm Smogowy via Gramwzielone.pl — NGO estimate); sector 1A4 "other sectors" (mainly household coal + biomass combustion) = **84%** of national PM2.5 emissions (2024 data, source KOBiZE 'Krajowy bilans emisji … 1990–2024', 2026) — rates/figures may have changed since
  - **Małopolska anti-smog uchwała** Nr XXXII/452/17 of 23 Jan 2017 (Dz. Urz. Woj. Małopolskiego poz. 787; amended by uchwała LIX/842/22 of 26 Sep 2022, poz. 6497) (source NIK post-audit statement P/24/069, 2024):
    - Kraków has its own uchwała Nr XVIII/243/16 of 15 Jan 2016 — solid fuels (coal, wood, other biomass) banned since 1 Sep 2019; only gas fuels + light heating oil allowed (source powietrze.malopolska.pl, 2026)
    - Rest of Małopolska — boilers below class 3 banned from end of April 2024 (moved from end-2022 by the 2022 amendment)
    - Class 3/4 coal/wood boilers must be replaced **by end of 2026**; class 5 installed before 1 Jul 2017 usable indefinitely (deadline as shown on powietrze.malopolska.pl, Oct 2026)
    - Stoves/fireplaces must meet ecodesign or ≥80% thermal efficiency since 1 May 2024
- **Mining subsidence (szkody górnicze)**:
  - **Górnośląskie Zagłębie Węglowe (GZW / USCB)** — ~1,500 tremors/yr of energy E ≥ 10⁵ J (1,765 in 2014; 2,000–3,000/yr in the 1960s–80s); ~70,000 such tremors catalogued 1974–2009 (2015 data, source GIG-PIB GRSS — rates/figures may have changed since; live map `https://grss.gig.eu/mapa-wstrzasow/`)
  - **Bełchatów lignite** — strongest mining-induced tremor recorded in Poland: M 4.6 (1980; 2010 data, source IGF PAN poster 'Wstrząsy indukowane', also GIG-PIB 'Sejsmiczność indukowana' — rates/figures may have changed since); example of a later event: M 3.7 on 22 Jan 2010 (same IGF PAN source); annual tremor count: no figure given — verify in the Bełchatów section of IGF PAN's yearly Seismological Bulletin (`https://pub.igf.edu.pl/`)
  - **KGHM copper** Polkowice/Rudna/Lubin in Dolnośląskie (LGOM) — strongest tremor M 4.5 (1977); about 20 mining events of M ≥ 3.0 in 2010, most of them here (2010 data, source IGF PAN 'Wstrząsy indukowane' — rates/figures may have changed since)
  - Regulated under Prawo geologiczne i górnicze
- **Radon**:
  - **PAA radiation map** (gamma dose rate, not radon): `https://monitoring.paa.gov.pl/maps-portal/`
  - **Radon-specific**: `https://www.gov.pl/web/poznajradon/mapy-radonowe2`
  - **Hotspots** (national radon action plan, M.P. 2021 poz. 169, citing PIG-PIB): Karkonosze + Strzegom granites, Izera Mountains gneisses, Kaczawa Mountains + Kłodzko Basin metamorphic/igneous rocks; NE glacial deposits, highest in Suwalszczyzna
  - **Reference level 300 Bq/m³** (Prawo atomowe); priority powiaty for radon measurement listed in Rozporządzenie Ministra Zdrowia z 18.06.2020 (Dz.U. 2020 poz. 1139, in force per Sejm ELI/ISAP, Oct 2026) — powiat-level screening, not a parcel verdict; only a measurement settles a building
- **Earthquake**: low natural seismicity — largest instrumentally recorded natural quake M 4.7, Podhale, 30 Nov 2004 (source IGF PAN); mining-induced tremors (above) are the main shaking risk
- **Heatwaves + drought**: 2025 mean temperature 9.5 °C, +0.8 °C vs the 1991–2020 normal; warming since 1951 put at 2.4 °C; 2025 was a dry year — 546 mm of precipitation (89.3% of normal) and a negative climatic water balance over most of the country in the growing season, below −300 mm locally on the Mazovian Lowland, Polesie, the Lublin Upland and part of the Sudetes (2025 data, source IMGW-PIB 'Klimat Polski 2025', 2026)
- **Storm damage**: severe convective storms can sweep most of the country in one day — e.g. 23 Jun 2025: gusts above 100 km/h, locally 115 km/h, and over 5,000 fire-service call-outs, most in Śląskie, Zachodniopomorskie and Wielkopolskie (2025 data, source IMGW-PIB 'Klimat Polski 2025', 2026); regional trend in storm-damage frequency: data not publicly available (Klimada 2.0 listed wind-speed projections as still in preparation, 2020) — verify at IMGW-PIB `https://imgw.pl/edukacja/raporty-klimatyczne-dla-polski/`

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1939 kamienica** | Lead paint, lead pipes, no DPC, damp, structural settlement |
| **PRL Wielka Płyta (1957–1990)** | ~60,000 large-panel buildings, ~50,000 (80%) of them three-layer panels; ITB examined 300 buildings in Mazowieckie, Łódzkie, Śląskie and Dolnośląskie; the ministry stated there is no threat to their structure or safety, and ITB issued guidance for checking panel-specific elements during the periodic building inspections; potential national investment in thermo-modernisation plus façade-layer anchoring PLN 25.8 bn (PLN 17.2 bn + PLN 8.6 bn) (2019 data, source Ministry of Investment and Development, 'Wielka płyta jest bezpieczna', 30 Jan 2019, gov.pl — rates/figures may have changed since); ~12M residents (2019 figure, source money.pl — secondary; verify with GUS census housing data — rates/figures may have changed since); durability originally estimated at **~50 years** (2019, RynekPierwotny.pl experts via money.pl — secondary); ITB report found systemic technological defects (2019, ITB report as quoted by money.pl — secondary); thermal bridges, slab-joint leaks, acoustic |
| **Eternit/asbestos roofing** | Program usuwania azbestu (adopted by the Rada Ministrów 14 May 2002) → Program Oczyszczania Kraju z Azbestu na lata 2009–2032, its continuation (uchwała RM nr 122/2009, text per uchwała nr 39/2010; source programme text, Ministerstwo Gospodarki 2010, on bazaazbestowa.gov.pl), target **31 Dec 2032**; 9.214 Mt inventoried, 7.005 Mt still to remove, removal pace ~200 kt/yr (2026 data, source MRiT answer to interpelacja nr 16053, 15 Apr 2026); draft asbestos act (UC60) sets no deadline and keeping or moving the 2032 date is open for the programme update |
| **1990s–2000s** | Improved insulation; some asbestos remains |
| **Post-2017 WT** | Tighter energy limits — EP(H+W) ≤ 95 kWh/(m²·yr) single-family / ≤ 85 multi-family from 1 Jan 2017 (WT, consolidated Dz.U. 2022 poz. 1225) |
| **Post-2021** | WT 2021 limits — EP(H+W) ≤ 70 kWh/(m²·yr) single-family / ≤ 65 multi-family from 31 Dec 2020 (WT, consolidated Dz.U. 2022 poz. 1225) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Świadectwo charakterystyki energetycznej (CEN)** | Handover at sale/rent required under art. 11 Ustawa o charakterystyce energetycznej budynków as amended from **28 April 2023** (Ustawa z 7.10.2022, Dz.U. 2022 poz. 2206); buyer/tenant cannot waive it (art. 11 ust. 4) | 10 years (art. 14 ust. 1); lapses earlier if works change the energy performance |
| **KW outprint (odpis z księgi wieczystej)** | Title verification | Current |
| **Zaświadczenie o wymeldowaniu** | Confirms no one registered at address; the gmina discloses the names of all persons registered at an address to an applicant who shows a legal interest (art. 47 ust. 1 and 4 with art. 46 ust. 2 pkt 1 ustawy o ewidencji ludności, consolidated Dz.U. 2026 poz. 384) | No statutory validity period (the act sets none for this disclosure); how recent it must be is practice, not statute — confirm with the notary (and the lender, if any) |
| **Wypis z rejestru gruntów + kartoteki lokali** | Cadastre extract | Current |
| **Podstawa nabycia** | Acquisition basis (prior deed) | Per case |
| **Zaświadczenie o braku zaległości czynszowych** | If apartment | Current |
| **Penalty for missing CEN** | grzywna (art. 41 ust. 1 pkt 3) — **20–5,000 PLN** general range (Kodeks wykroczeń art. 24 § 1); notary records the handover, or warns of the fine, in the akt notarialny (art. 11 ust. 6) | n/a |

### Climate change projections

- Mean annual temperature **+1.3 °C (RCP4.5) to >3 °C (RCP8.5)** by 2100 vs the 2011–2020 decade (2020 data, source IOŚ-PIB Klimada 2.0 short report — rates/figures may have changed since)
- Annual precipitation up ~30 mm (RCP4.5) to ~50 mm (RCP8.5) by 2060 and ~50 mm to ~100 mm by 2100 — most in the east, the mountains and on the coast, least in the centre-west; the largest seasonal changes fall in summer (June–August); the report gives no summer-drier / winter-wetter split (same source)
- More extreme rainfall (Boris 2024 type) — days with > 20 mm/day rise under both scenarios, about 1 day more under RCP8.5 than RCP4.5 (same source)
- More frequent heatwaves — hot days (Tmax > 30 °C) roughly ×2 (RCP4.5) to >×3 (RCP8.5) by 2100 (same source)
- Shorter winters, less snow — frost days (Tmin < 0 °C) ~95 → ~70/yr by the 2090s under RCP4.5, ~60 fewer under RCP8.5 (same source)

---

## Section: `--mains`

### Sources

- **WPK (Wodociągi i Kanalizacja)** per gmina (Miejskie/Gminne Przedsiębiorstwo Wodociągów i Kanalizacji)
- **Cesspit emptying** — the owner must hold a contract with a licensed haulier, and the gmina sets upper rates for emptying by uchwała (art. 6 ust. 1–2 ustawy o utrzymaniu czystości i porządku w gminach, consolidated Dz.U. 2025 poz. 733); the sewer price per m³ is in the water company's tariff, approved by the PGW Wody Polskie regional director (art. 24b ust. 1 and art. 27a ustawy o zbiorowym zaopatrzeniu w wodę, consolidated Dz.U. 2024 poz. 757); est. ~40 PLN/m³ emptied vs ~10 PLN/m³ sewer charge — an economic disincentive (unsourced, undated estimate; both prices vary by gmina and no national price series is publicly available — verify in the gmina's upper-rate uchwała and the approved tariff)
- **Eastern + central rural areas** worst-served: rural sewer use ≤50% of residents in the eastern and central voivodeships vs 68.2% in Pomorskie and 62.1% in Podkarpackie, >50% in Zachodniopomorskie, Opolskie, Wielkopolskie, Dolnośląskie and Śląskie (2024 data, source GUS 'Gospodarka mieszkaniowa i infrastruktura komunalna w 2024 r.', 17 Nov 2025) — rates/figures may have changed since; sewer-network density lowest in Podlaskie (20.7 km per 100 km²) and Lubelskie (32.6), highest in Śląskie (154.5) and Małopolskie (133.8) (2025 data, source GUS 'Infrastruktura komunalna – wodociągowa i kanalizacyjna w 2025 r.', 26 Jun 2026) — voivodeship averages, not a parcel verdict

### Verification

- **Towns and cities**: mains not universal — 78.1% of urban residential buildings connected to the sewer and 88.9% to mains water (2025 data, source GUS 'Infrastruktura komunalna – wodociągowa i kanalizacyjna w 2025 r.', 26 Jun 2026); urban averages — confirm the building's own connection
- **Sewerage coverage**: **46.9%** of the rural population uses the sewer network vs 91.3% urban, 73.3% national; rural mains water 86.8% (2025 data, source GUS BDL P2433 'Korzystający z instalacji w % ogółu ludności') — national averages; confirm the parcel's own connection with the gmina WPK
- **Suburbs**: mixed; check whether the gmina's aglomeracja and planned works appear in the national **Krajowy Program Oczyszczania Ścieków Komunalnych (KPOŚK)** — current 6th update (AKPOŚK 2022), 1,524 agglomerations, progress reported yearly by PGW Wody Polskie: `https://www.gov.pl/web/wody-polskie/krajowy-program-oczyszczania-sciekow-komunalnych`
- **Szambo** (cesspit) is the main on-site system: 2,088,736 cesspits = 80.1% of 2,608,428 on-site systems, the other 519,692 (19.9%) being home treatment plants (computed from GUS BDL P3197 'zbiorniki bezodpływowe' and 'oczyszczalnie przydomowe', state on 31 Dec 2025); GUS 'Infrastruktura komunalna – wodociągowa i kanalizacyjna w 2025 r.' (26 Jun 2026) gives the same 80.0% / 20.0% split but prints counts of 2,283.8k / 324.2k that do not match it — the BDL counts are used here; 76.3% of the 46.1 hm³ of cesspit sewage collected in 2025 came from rural areas (2025 data, same GUS release); home-treatment-plant share highest in Kujawsko-Pomorskie (34.5%), lowest in Podkarpackie (11.5%) (2024 data, source GUS 'Gospodarka mieszkaniowa i infrastruktura komunalna w 2024 r.', 17 Nov 2025) — rates/figures may have changed since; the owner must connect to an existing sewer, except that connection is not mandatory for a property with a compliant home treatment plant; where building a sewer is technically or economically unjustified, a cesspit or home treatment plant is required instead (art. 5 ust. 1 pkt 2 ustawy o utrzymaniu czystości i porządku w gminach, consolidated Dz.U. 2025 poz. 733)

### Costs

| Scenario | Cost (PLN, est.) |
|---|---:|
| Przyłącze do sieci wodociągowej | 5,000–15,000 |
| Przyłącze do kanalizacji | 8,000–25,000 |
| Szambo to mains | 12,000–35,000 |
| Przydomowa oczyszczalnia ścieków | 10,000–25,000 |
| Studnia głębinowa | 8,000–20,000 |

All rows are est. — undated ranges with no primary price source. The owner pays for building the przyłącze (art. 15 ust. 2 ustawy o zbiorowym zaopatrzeniu w wodę, consolidated Dz.U. 2024 poz. 757), and the water company must connect the property once the warunki przyłączenia in its regulamin are met and connection is technically possible (art. 15 ust. 4); get a quote against those conditions.

---

## Cost benchmarks (PL 2026)

| Work | Cost (PLN) |
|---|---:|
| Świadectwo CEN | 350–650 flat / 600–1,300 house (Jan 2026 average prices, comparison portal rankomat.pl ⚠️ secondary; cross-check 430–815 net, marketplace oferteo.pl, 2026 ⚠️); Czyste Powietrze grant cap for the post-works CEN: 400 at the 100% level (2026 data, source czystepowietrze.gov.pl "Na co i ile") |
| Notariusz (max taxa, flat sale) | 1,949.55 incl. VAT on a 600,000 sale (≈0.33%, computed) |
| KW + sąd fees | 200–500 (computed: 200 ownership entry, + 100 to open a new KW, + 200 mortgage entry; art. 42 ust. 1, art. 44 ust. 1 pkt 1, art. 45 ust. 1) (2026 data, source ustawa o kosztach sądowych w sprawach cywilnych, consolidated text Dz.U. 2025 poz. 1228; the 2026 amendments Dz.U. 2026 poz. 346, 473 and 1003 leave these articles unchanged) |
| PCC (resale, non-FTB) | 2% |
| Realtor | est. 1.5–3% buyer side, 2–5% seller side; 1.5–2% per side when both pay (2026 market guides ⚠️ secondary: cenauslug.pl Sep 2026, agency fee most often 2–4% of the value and 1.5–3% for a buyer's agent; pewnylokal.pl Feb 2026, 1.5–3% standard, 2–5% on a flat sale, 1.5–2% per side when split; commission not regulated by law per pewnylokal.pl, negotiable) |
| **Total transaction cost (FTB exempt, excl. agent)** | **≈0.4%** (computed, 600,000 flat) |
| **Total transaction cost (resale, second home, excl. agent)** | **≈2.4%** (computed, 600,000 flat) |
| **Total transaction cost (new build, 8% VAT included, excl. agent)** | **≈0.4–0.8%** (computed, 600,000 flat) |
| Asbestos eternit removal (dismantling + transport + disposal) | est. 4,000–14,000 for a 100 m² roof (computed: 100 m² × ~40–140 PLN/m²; low end cenauslug.pl Aug 2026: dismantling 35–55 PLN/m² + disposal incl. transport 500–850 PLN/t at 11–15 kg/m²; high end kb.pl Jan 2026: dismantling 60–80 + wrapping, transport and disposal 35–60 PLN/m²; 2026 price guides ⚠️ secondary that disagree, so the range spans both) |
| Wielka Płyta flat, general renovation (installations, bathroom, kitchen, finishes) | est. 75,000–275,000 for 50 m² (computed: 50 m² × 1,500–5,500 PLN/m², an all-flat range, not panel-block specific, totalmoney.pl Mar 2026 ⚠️ secondary); 110,000–160,000 for 50 m² at mid standard, ~2,400–3,200 PLN/m² (muratordom.pl Sep 2026 ⚠️ secondary, AI-assisted article); from 90,000 economy to over 230,000 premium for a 50 m² panel-block flat, mid standard 2,800–3,900 PLN/m² (marketplace oferteo.pl, May 2026 ⚠️ secondary; a related oferteo.pl guide on the same page gives 2,400–3,200 at mid standard, so the sources do not agree); a refresh that keeps the installations costs less — verify with 2–3 contractor quotes |
| Roof renovation (re-covering) | est. 16,000–45,000 metal tile / 21,000–60,000 ceramic tile for a 100–150 m² roof (computed: removal 30–50 + new covering with battens and membrane 80–150 + material 50–100 metal / 100–200+ ceramic PLN/m²; 2026 price guide, contractor marketplace oferteo.pl ⚠️ secondary; inputs cover the covering only, not rafter repairs); the same page puts whole orders at most often 1,000–33,000, typical ~7,000, with no roof size or scope stated |
| Deep energy retrofit, single-family house (insulation + windows + heat source) | est. 60,000–150,000 (LOW confidence: unsourced estimate from the 2026-04 initial population); calibration: Czyste Powietrze worked examples of the maximum grant at the 100% level, building above 140 kWh/(m²·yr), are 140,300 (air/water heat pump + thermo-modernisation) and 170,100 (ground-source pump + thermo-modernisation), thermo-modernisation capped at 83,000 (2026 data, source czystepowietrze.gov.pl "Na co i ile") |
| Boiler upgrade (pellet ekoprojekt or gas condensing) | 22,000–32,000 pellet / 20,000–28,000 gas condensing, incl. installation, 150 m² house (Mar 2026, trade press muratordom.pl ⚠️ secondary); Czyste Powietrze grant cap for a pellet boiler: 20,500 at the 100% level, incl. chimney and buffer tank (2026 data, source czystepowietrze.gov.pl) |
| Heat pump (incl. installation, ~150 m² house) | air/water 35,000–55,000; ground-source 55,000–90,000 (2026 price guides ⚠️ secondary: cenauslug.pl Aug 2026 35,000–45,000 / 70,000–90,000 incl. boreholes; muratordom.pl Mar 2026 38,000–55,000 / 55,000–85,000); Czyste Powietrze grant caps at the 100% level: 35,200 air/water (higher efficiency class), 45,000 + 20,000 lower source for ground-source (2026 data, source czystepowietrze.gov.pl) |
| Solar PV (rooftop, on-grid) | est. 20,000–28,000 for 5 kWp; est. 38,000–52,000 for 10 kWp; a 5–10 kWh battery adds est. 15,000–40,000 (May 2026 price guide, trade press muratordom.pl ⚠️ secondary, AI-assisted article); marketplace oferteo.pl gives the same 5 kW and 10 kW ranges, gross incl. installation (January 2026 estimates on a page updated May 2026 ⚠️ secondary; identical figures, so not an independent check), and est. 35,000–50,000 gross for a complete 10 kW system on its 10 kW page; no government price series was found, and oferteo's price-page ranges describe mid- and upper-class kit on a pitched roof, so calibrate with installer quotes |

- Renovation and equipment rows are market prices that no primary source publishes: ranges come from 2026 secondary price guides (⚠️) or are labelled est.; the Czyste Powietrze grant caps are the primary cross-check where one exists
- Polish energy certificates carry no A–G letter class yet: the recast EPBD's classes (transposition deadline 29 May 2026) are still in draft (trade press muratordom.pl, 5 Oct 2026 ⚠️ secondary; no 2026 regulation on energy-performance certificates in Dz.U. through poz. 1445 of 2 Nov 2026, api.sejm.gov.pl, checked 2026-11-03; EU-wide status in `shared/regulatory-watch.md`)

## Active fiscal incentives (2025-2026)

- **Czyste Powietrze** (NFOŚiGW, single-family houses): grant up to 40% / 70% / 100% of eligible costs (basic / higher / highest level); worked examples reach **PLN 170,100** at the highest level (ground-source heat pump + thermo-modernisation, building above 140 kWh/m²/yr) (2026 data, source czystepowietrze.gov.pl "Na co i ile")
  - **31 March 2025 reform**: gas/oil/fossil boilers no longer eligible (per EPBD); since 1 Jan 2026 no gas or oil boiler can be funded under any call (NFOŚiGW 05.06.2026)
  - Pellet boilers without emergency grate only
  - Pivot to heat pumps (PV is not among the funded items); from 2027 electric heating other than heat pumps (mats, electric boilers, electric radiators) is no longer funded
  - **20 Jul 2026 changes** (applications from that date): max unit rates for insulation, windows, doors and garage doors +10%; prefinanced works period 180 days, up from 120 (NFOŚiGW 20.07.2026)
  - Separate gas-boiler call (część 5) ran **15 Jul – 17 Nov 2025**; flood call (część 4) ran 12 Dec 2024 – 28 Feb 2026 (NFOŚiGW 05.06.2026)
- **Mój Prąd** (PV): 6th call (MP6) closed; applications filed by 12 Sep 2025 still under assessment (status 9 Apr 2026); NFOŚiGW states no "Mój Prąd 7.0" in the previous formula. Successor **Przydomowe Magazyny Energii** (home battery ≥10 kWh or heat store ≥100 dm³ for prosumers): PME2 call 20 Oct 2026 – 1 Oct 2027, budget up to PLN 1 bn (2026 data, sources mojprad.gov.pl, przydomowemagazyny.gov.pl)
- **Stop Smog**: low-income retrofit
- **Mieszkanie bez wkładu własnego** (*rodzinny kredyt mieszkaniowy*): BGK guarantee covers the gap between the buyer's deposit and 20% of the cost; deposit ≤PLN 200,000, term ≥15 years, household may own no flat or house; can be granted until 31 Dec 2030 (art. 3 ust. 3–4, art. 5 ust. 1) (2024 data, source consolidated text Dz.U. 2024 poz. 1724) — rates/figures may have changed since
- **Bezpieczny Kredyt 2%**: launched 1 July 2023; banks stopped taking applications on 2 Jan 2024 when projected subsidies hit 90% of the 2024 limit (BGK communiqué, per secondary source strefainwestorow.pl, 2 Jan 2024); since 22 Aug 2025 the statute allows the credit only on applications filed before that date (art. 3 ust. 5 as amended by Dz.U. 2025 poz. 1077) — **closed for good**. Existing borrowers keep subsidies on the first 120 instalments (art. 9b ust. 1) (2025 data, source Dz.U. 2025 poz. 1077 + consolidated text Dz.U. 2024 poz. 1724)
- **Kredyt #naStart / Mieszkanie na Start**: planned successor (project 8.04.2024); **withdrawn end of 2024**, funds redirected to powódź Boris relief; no bill on it reached the Sejm (10th-term print list, api.sejm.gov.pl, checked 2026-10-23)
- **Pierwsze Klucze**: latest mooted replacement (MRiT, 2025); **no bill in the Sejm as of 2026-10-23** (10th-term print list, api.sejm.gov.pl); legislative limbo
- **Rodzinny dom** scheme: families with 3+ kids

## Common listing platforms

- **Otodom** — biggest
- **Morizon Group** (incl. Gratka, Noweinwestycje.pl)
- **Nieruchomosci-online**, **Domiporta**, **OLX Nieruchomości**

## Caveats unique to PL

- **PoN 2025 reform**: new "budynek" vs "budowla" definitions effective 1 Jan 2025; case-by-case litigation expected
- **PCC first-home exemption since 31 Aug 2023** — secondary market only
- **8% VAT on small new residential** (≤150 m² flat / ≤300 m² house)
- **Currency risk** (PLN volatile vs EUR)
- **CHF mortgage scandal** — 2002-2008 vintage; ongoing court battles; SN full Civil Chamber resolution III CZP 25/22 of 25 Apr 2024 (moc zasady prawnej) set the main "frankowicze" precedent (secondary source Lege Artis, 28 Apr 2024; verify at sn.pl)
- **Użytkowanie wieczyste**: legacy form — converted to ownership for housing 2019; commercial still in use
- **Spółdzielcze własnościowe prawo do lokalu** — cooperative ownership (separate from KW); convert to full ownership recommended
- **Wspólnota mieszkaniowa** (HOA): arises automatically from sale of first lokal (art. 6 UWL); **"duża wspólnota" = ≥ 4 lokali (since 1.01.2020 UWL nowelizacja)** with mandatory zarząd; mała wspólnota (≤ 3 lokale) operates under Kodeks cywilny współwłasność rules (2026 data, source: UWL art. 6, 19–20, consolidated text Dz.U. 2026 poz. 232; threshold lowered from 7 to 3 by Dz.U. 2019 poz. 1309, art. 7, in force 1 Jan 2020)
- **Foreign-buyer regime — Ustawa z 24.03.1920 o nabywaniu nieruchomości przez cudzoziemców**: non-EEA/non-Swiss buyers need an **MSWiA permit** (zezwolenie ministra właściwego ds. wewnętrznych), issued only if the acquisition poses no threat to defence, state security or public order and the buyer shows ties to Poland, e.g. Polish origin, marriage to a Polish citizen, a residence permit or business activity in Poland (art. 1a ust. 1–2), and only if the Minister of National Defence (and, for farmland, the rural-development minister) does not object within 14 days, extendable to 2 months (art. 1 ust. 1–1a); EEA/Swiss citizens and companies exempt since 1 May 2004, after transition periods for farmland/forest (12 years, ended 1 May 2016) and second homes (5 years, ended 1 May 2009) (art. 8 ust. 2); Ustawa o kształtowaniu ustroju rolnego still applies to farmland. Non-EEA buying a standalone **lokal mieszkalny** (or a garage unit serving it): no permit (art. 8 ust. 1 pkt 1–1a), **except in the strefa nadgraniczna (border zone) and for farmland over 1 ha** (art. 8 ust. 3); buying **house+land or agricultural**: permit required, discretionary; processing est. 2–6 months (practice figure, not set in the act; verify with MSWiA). From 19 Nov 2026 notaries file foreign-acquisition deeds with MSWiA through the KRN electronic repository, for a fee charged to the parties (Dz.U. 2026 poz. 1099) (2026 data, sources: consolidated text Dz.U. 2017 poz. 2278; Dz.U. 2026 poz. 1099).
- **Okres ochronny (1 listopada – 31 marca)**: eviction judgments are not executed in this period if the evicted person has not been given a place to move to (art. 16 ustawy o ochronie praw lokatorów, Ustawa z 21.06.2001); does NOT apply to najem okazjonalny (art. 19e, provided the owner filed the art. 19b notice with the urząd skarbowy) or najem instytucjonalny (art. 19j) — which is precisely why these forms exist (source consolidated text Dz.U. 2023 poz. 725).
- **Świadectwo CEN mandatory since 28 Apr 2023**
- **Storm Boris 2024** = recent reform-driver event
- **Małopolska anti-smog**: most restrictive in Poland; Kraków zero-emission since 2019
- **Eternit removal deadline 31 Dec 2032** — major remaining stock
- **Wielka Płyta** refurbishment ongoing; designed for 50-year life, mostly past that now
- **EU 2024/1028 STR implementing act not yet in force**: passed by the Sejm on 8 Oct 2026 and amended by the Senate (resolution of 6 Nov 2026 with amendments, Sejm print 3341), back before the Sejm; listing ID number (Centralny Wykaz Turystycznych Obiektów Noclegowych) and fines up to PLN 50,000 apply 14 days after publication in Dz.U.; wspólnota/spółdzielnia bans and gmina STR zones from 1 Jan 2028; no 15 Oct 2026 deadline in the text (2026 data, sources api.sejm.gov.pl process 2865; sejm.gov.pl process 2865, read 2026-11-11; MSiT 12.10.2026)
- **Czyste Powietrze 31 March 2025**: gas boilers no longer eligible; since 1 Jan 2026 no gas or oil boiler can be funded under any call — pivot to heat pumps (NFOŚiGW 05.06.2026)
- **Mining subsidence** documented + compensable in USCB + Bełchatów + Polkowice areas
- **Radon hotspots**: Karkonosze, Sudety, Kłodzko, Suwalszczyzna
- **CHF "frankowicze"** mortgage holders — major civil case backlog; special court-procedure act for CHF consumer-loan cases (ustawa z 29.05.2026, Dz.U. 2026 poz. 985) in force since 7 Aug 2026
- **Income from private rental (najem prywatny)**: ryczałt 8.5% of revenue up to PLN 100,000/yr, 12.5% above (art. 12 ust. 1 pkt 4 ustawy o zryczałtowanym podatku dochodowym) (2025 data, source consolidated text Dz.U. 2025 poz. 843)

## Reddit / forum sources

- **r/poland** — biggest community
- **r/Polska** (Polish-language)
- **r/Warsaw**, **r/krakow**, **r/wroclaw**, **r/Gdansk**
- **r/PolskaPolityka** — political/regulatory discussions
- **Bankier.pl** forums — financial
- **Notes from Poland** (English news)
- **Murator** (`https://muratordom.pl/`; forum `https://forum.murator.pl/`) — building/renovation
- **DomPlus.pl** — ❌ DEPRECATED — dead on 2026-10-23 (domain redirects to a housing developer's site); verify with the Murator forum

## Verification authorities

| Authority | When to call |
|---|---|
| **Sąd Rejonowy (KW department)** | Title verification |
| **Geoportal2 / EGiB** | Cadastre extract |
| **Notariusz** (mandatory for sale) | Final transfer |
| **Urząd Skarbowy** | PCC, PIT, capital gains |
| **Gmina** | PoN, planning, permits |
| **Wody Polskie** | Flood risk |
| **PAA** | Radon |
| **Wspólnota mieszkaniowa** / **Spółdzielnia** | If apartment |
| **Sanepid** | Radon, water quality |
| **GIOŚ** | Air quality |
| **GDDKiA** (GPR) | Traffic counts on national + voivodeship roads |
| **GIG-PIB GRSS** | Mining-tremor history (Upper Silesia) |

## Source URL templates

| Source | URL pattern |
|---|---|
| EKW | `https://ekw.ms.gov.pl/` |
| Geoportal2 | `https://www.geoportal.gov.pl/` |
| NBP BaRN | `https://nbp.pl/publikacje/cykliczne-materialy-analityczne-nbp/rynek-nieruchomosci/` |
| AMRON | `https://amron.pl/raporty/` |
| Otodom | `https://www.otodom.pl/` |
| Wody Polskie | `https://www.gov.pl/web/wody-polskie` |
| ISOK floods | `https://wody.isok.gov.pl/` |
| PAA radon | `https://monitoring.paa.gov.pl/maps-portal/` |
| Czyste Powietrze | `https://czystepowietrze.gov.pl/` |
| Baza Azbestowa | `https://bazaazbestowa.gov.pl/` |
| Polski Alarm Smogowy | `https://polskialarmsmogowy.pl/` |
| GUS | `https://stat.gov.pl/` |
| GDDKiA traffic | `https://www.gov.pl/web/gddkia` |
| GIOŚ | `https://www.gov.pl/web/gios` |
| GIOŚ air-quality portal | `https://powietrze.gios.gov.pl/pjp/current` |
| GDDKiA GPR 2025 | `https://www.gov.pl/web/gddkia/generalny-pomiar-ruchu-2025` |
| GUS BDL (local data bank) | `https://bdl.stat.gov.pl/` |
| KPOŚK (Wody Polskie) | `https://www.gov.pl/web/wody-polskie/krajowy-program-oczyszczania-sciekow-komunalnych` |
| GIG-PIB GRSS tremor map | `https://grss.gig.eu/mapa-wstrzasow/` |
| Klimada 2.0 climate scenarios | `https://klimada2.ios.gov.pl/klimat-scenariusze/` |
| Radon (Poznaj Radon) | `https://www.gov.pl/web/poznajradon/mapy-radonowe2` |

## Status

✅ Fast-changing sections re-verified as of 2026-10-23; each section's date is in the Per-section verification table.

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing (GUS BDL 2025 city medians + GUS DBW 2025 powiat medians + NBP BaRN II kw. 2026 transaction means + AMRON-SARFiN + Otodom), traffic (GDDKiA GPR 2025 SDRR), tax (PoN 2025 reform + 2026 and 2027 max rates per MF obwieszczenia M.P. 2025 poz. 726 and M.P. 2026 poz. 741), rental (najem types + EU 2024/1028 implementing act, Sejm print 2865), work (ZUS, PIT, GUS 2025 wages), risks (smog + Boris 2024 and WORP 2025 flood history + radon + mining tremors + IMGW-PIB 2025 climate + Klimada 2.0 projections), mains (GUS BDL 2025 sewerage and on-site systems + GUS 2024 / 2025 regional and urban connection shares) cite primary government sources where stated; the `--price` centrum / periphery splits and single-family totals, the `--mains` connection-cost table and cesspit rates, and the CEN, realtor and renovation rows of Cost benchmarks are estimates or secondary price guides ⚠️ with no primary price source.
**Confidence**: HIGH for `--tax` (re-verified 2026-10-23 against statute and gazette text: PoN 2025 budynek/budowla definitions per Dz.U. 2024 poz. 1757, 2026 and 2027 max rates per M.P. 2025 poz. 726 and M.P. 2026 poz. 741, PCC 2% / 6% and first-home exemption, 8% VAT limits, notary taxa and court fees); HIGH for the `--rental` tax rules and `--work` figures (re-verified 2026-10-23: ryczałt 8.5% / 12.5%, VAT exemption limit PLN 240,000, ZUS 2026, GUS 2025 wages); MEDIUM for short-term-let rules (EU 2024/1028 implementing act, Sejm print 2865, passed the Sejm 8 Oct 2026; not in Dz.U. 2026 through poz. 1480 of 9 Nov 2026; the Senate amended it on 6 Nov 2026 (Sejm print 3341; amendment contents per press, not verified to a primary source — 2026-11-11), and the Sejm has yet to vote on them, so the fines, listing-ID duty and dates may still change); HIGH for świadectwo CEN mandate (28 Apr 2023), Storm Boris 2024 core figures and Małopolska anti-smog deadlines (re-checked 2026-10-23); MEDIUM for `--price` city-level ranges (est., calibrated against GUS 2025 city medians and NBP BaRN II kw. 2026 transaction means); HIGH for its smaller-city and rural-east PLN/m² rows as powiat-level figures (computed from GUS 2025 powiat medians, not parcel-level); LOW for its centrum / periphery splits and single-family totals (est., no primary source at that level; national GUS RCN 2025 cross-check only); HIGH for `--risks` items sourced to primary bodies (re-verified 2026-10-23 and closed by the 2026-11-03 gap-closing pass: WORP 2025 flood history, IGF PAN and GIG-PIB tremor records, IMGW-PIB 2025 climate data, ministry Wielka Płyta figures, Klimada 2.0 projections); MEDIUM for its NGO / secondary items (PAS smog rankings, ~2.5M kopciuchy, the secondary Wielka Płyta resident count, durability and ITB-defect items) and curated build-era rows; the regional storm-damage trend is marked data not publicly available, and the Bełchatów annual tremor count gives no figure, with a pointer to IGF PAN's yearly Seismological Bulletin; MEDIUM for `--mains` (rural sewerage from GUS BDL 2025; connection-cost table and cesspit cost are unsourced estimates); LOW for forum sources (subreddits unverifiable).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--tax` | 2026-10-23 | 2026-11-05 maintenance run | The ceilings behind the worked bills (1.25 and 1.29 PLN/m² residential, 0.77 and 0.80 PLN/m² other land) match the finance minister's notices M.P. 2025 poz. 726 and M.P. 2026 poz. 741. The 1.00 PLN/m² average matches the Ministry of Finance report on 2026 rates on podatki.gov.pl, and the arithmetic holds. |
| `--rental` | 2026-11-05 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--work=<profession>` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--traffic` | 2026-10-23 | 2026-10-23 refresh wave | 2 changed, 2 confirmed; GPR 2025 calibration added; verdict bands are curated wisdom, not data |
| Common listing platforms | 2026-10-23 | 2026-10-23 refresh wave + 2026-11-03 gap-closing pass | 5 confirmed, 1 unverifiable in the refresh (OLX Nieruchomości could not be read for verification); OLX category page confirmed from an archived capture (2026-10-25) in the `--price` gap-closing pass |
| Verification authorities | 2026-10-23 | 2026-10-23 refresh wave | 3 confirmed; GDDKiA (GPR) and GIG-PIB GRSS rows added |
| Source URL templates | 2026-10-23 | 2026-10-23 refresh wave | 14 existing URLs live with content checked; 7 URLs added |
| `--price` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| `--risks` | 2026-10-23 | 2026-11-05 maintenance run | The asbestos row matches the programme text (Ministerstwo Gospodarki, Warsaw 2010, annex to uchwała nr 39/2010 on bazaazbestowa.gov.pl) for the 14 May 2002 adoption and the continuation, the Baza Azbestowa downloads page for uchwały 122/2009 and 39/2010, and the MRiT answer to interpelacja nr 16053 of 15 April 2026 for the tonnages, removal pace, 31 Dec 2032 date and draft act UC60. The draft has not yet appeared in Sejm proceedings or Dziennik Ustaw. |
| `--mains` | 2026-10-23 | 2026-11-05 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (PL 2026) | 2026-10-23 | 2026-11-05 maintenance run | Rooftop solar PV ranges match the muratordom.pl May 2026 price guide and two oferteo.pl pages updated 4 May 2026, all secondary. No government price series was found, so the row is now marked est. with a calibration note. |

## Extension TODOs

- [ ] Per-gmina PoN rates (uchwały)
- [ ] PoN 2025 reform case law tracker (budynek vs budowla disputes)
- [ ] Małopolska anti-smog implementation deadline tracker
- [ ] Storm Boris 2024 affected zone overlay
- [ ] Wielka Płyta block inventory by city
- [ ] Eternit removal progress per gmina (2032 deadline)
- [ ] Mining subsidence zones overlay (USCB + Bełchatów + Polkowice)
- [ ] Radon zone overlay per powiat
- [ ] EU 2024/1028 implementing-act tracker (Sejm print 2865 passed the Sejm 8 Oct 2026; the Senate adopted amendments on 6 Nov 2026 (Sejm print 3341; amendment contents per press, not verified to a primary source — 2026-11-11), so the Sejm votes on them next (next planned sitting 17-19 Nov 2026); presidential signature and Dz.U. position not yet logged; not in Dz.U. 2026 through poz. 1480 of 9 Nov 2026; revisit 2026-11-20)
- [ ] CHF "frankowicze" case law summary
- [ ] Czyste Powietrze 31 Mar 2025 gas-boiler transition
- [ ] First-home PCC exemption decision tree

## Update history

- **2026-04-25** — Initial population
- **2026-05-27** — Tier-1 validation sweep: PCC 6% bulk-buyer rate added; najem prywatny ryczałt, Bezpieczny Kredyt 2% and successor schemes, wspólnota threshold, foreign-buyer regime and okres ochronny rewritten
- **2026-05-29** — Anti-hallucination consistency sweep: Group I inheritance exemption and kopciuchy PM2.5 share relabelled est.
- **2026-09-18** — Citation-repair wave: GIOŚ URLs re-pointed to `https://www.gov.pl/web/gios`
- **2026-10-23** — Refresh wave plus a gap-closing pass. Playbook-level date not re-stamped: Cost benchmarks remains open — its KW court fees are confirmed and its notary, PCC and total rows rest on the re-verified `--tax` section, but the CEN, realtor and renovation rows rest on secondary price guides ⚠️ or est. labels with no primary price source, and the deep energy retrofit row is an unsourced LOW-confidence est.; `--price`, `--risks` and `--mains` were closed by the gap-closing pass below. Counts per section (changed / confirmed / unverifiable):
  - Re-verified: `--tax` 17 / 14 / 2; `--rental` 10 / 6 / 2; `--work` 6 / 3 / 2; `--traffic` 2 / 2 / 0; Common listing platforms 0 / 5 / 1; Verification authorities 0 / 3 / 0 (2 rows added); Source URL templates 0 / 14 / 0 (7 URLs added)
  - Partly refreshed, not re-verified by the refresh (`--price`, `--risks` and `--mains` closed in the gap-closing pass below; Cost benchmarks still open): Country profile 2 / 3 / 4; `--price` 6 / 5 / 4; `--risks` 12 / 27 / 11; `--mains` 2 / 1 / 9; Cost benchmarks 5 / 2 / 8; Active fiscal incentives 10 / 2 / 5; Caveats unique to PL 6 / 6 / 1; foreign-buyer regime 4 / 1 / 1; Reddit / forum sources 2 / 2 / 7
  - Main changes: EU 2024/1028 implementing act (Sejm print 2865) passed the Sejm 8 Oct 2026 and is not in force, and the "15 Oct 2026" deadline is removed; 2027 PoN max rates added (M.P. 2026 poz. 741); notary fee and transaction-cost totals recomputed from statute (≈0.4% first home, ≈2.4% resale second home, ≈0.4–0.8% new build, excl. agent; previously ~3–4% / ~6–8% / ~3–4%); VAT exemption limit PLN 240,000 from 1 Jan 2026; ZUS 2026 and GUS 2025 average wages; NBP FX and GUS admin counts; price table relabelled est. with a GUS 2025 city-median anchor; Gemius 2023 listing-audience figures (stale-suffixed); Czyste Powietrze 2026 rules, Mój Prąd closed with Przydomowe Magazyny Energii as successor; foreign-buyer permit conditions restated from the 1920 act; Małopolska anti-smog resolution number corrected to XXXII/452/17; USCB tremor and climate-projection figures replaced (GIG-PIB GRSS, Klimada 2.0); WT energy limits replace "energy class C"; rural sewerage 46.9% (GUS BDL 2025); GPR 2025 traffic calibration; DomPlus.pl deprecated; CHF court-procedure act (Dz.U. 2026 poz. 985) and SN III CZP 25/22 date added
  - Status footer: Coverage check and Confidence recomputed; per-section verification table added
  - Gap-closing pass (checks dated 2026-11-03): `--price`, `--risks` and `--mains` closed, Cost benchmarks still open. Facts confirmed / changed / relabelled: `--price` 2 / 2 / 3, `--risks` 5 / 6 / 3, `--mains` 0 / 3 / 3, Cost benchmarks 1 / 0 / 9 (total 8 / 11 / 18). Main changes: NBP BaRN coverage (III kw. 2006 – II kw. 2026) confirmed from the data file and an archived capture, with II kw. 2026 city transaction means added as a cross-check; OLX Nieruchomości confirmed from an archived capture; smaller-city and rural-east PLN/m² rows computed from GUS 2025 powiat medians (6,000–9,500 → 5,771–7,499; 3,000–5,500 → 4,905–6,787); Storm Boris flood area corrected (Małopolskie flooded only in small parts), PAA map relabelled gamma dose rate, heatwave / drought / storm lines rebased on IMGW-PIB 2025 data, the unsourced seasonal-precipitation split removed, the Wielka Płyta row rebased on ministry figures and the Bełchatów exact day dropped; `--mains` worst-served regions corrected to eastern + central, GUS urban connection shares and cesspit counts added, cost rows labelled est. with the statutory price setters; KW court fees confirmed (Dz.U. 2025 poz. 1228), CEN, realtor and renovation rows re-based on dated secondary price guides ⚠️ or computed / LOW-confidence est., four of them cross-checked against Czyste Powietrze 2026 grant caps, and the "Class E → A" label dropped. Status footer Coverage check, Confidence and per-section rows updated to match.
- **2026-11-04** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--mains`, Cost benchmarks (PL 2026); still open `--risks`. Playbook-level date now 2026-10-23.
- **2026-11-05** — Maintenance run: closed `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`, `--mains`, Cost benchmarks (PL 2026).
