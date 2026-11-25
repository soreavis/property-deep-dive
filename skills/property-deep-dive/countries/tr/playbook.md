# Türkiye 🇹🇷 — Property Due-Diligence Playbook

ISO2: `tr`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Posta kodu (postcode)**: 5 digits, no internal space (e.g., `34000` İstanbul, `06000` Ankara, `35000` İzmir, `07000` Antalya)
  - First 2 digits: il (province) plaka kodu (matches license-plate code 01–81)
  - Last 3 digits: ilçe + mahalle cluster
- **Admin levels**: 81 il (province) → 973 ilçe (district) → ~32,000 mahalle/köy (neighbourhood/village). 30 of the 81 are **Büyükşehir Belediyesi** (metropolitan municipality).
- **Currency**: TRY (Türk lirası). **Foreign-buyer transactions widely quoted in USD or EUR** because of TRY hyperinflation (CPI hit 85.51 % YoY Oct 2022, re-peaked ~75 % YoY May 2024, ~44 % by end-2024, low-30s by late 2025, ~32.6 % YoY May 2026, **31.51 % YoY Aug 2026** per TÜİK (2026 data, quoted in TCMB PPK summary 2026-42) — TÜİK's Aug-2026 bulletin puts the 12-month-average TÜFE (the rent-cap basis) at 31.79 %; CBRT one-week repo rate peaked 50 % Mar 2024, eased through 2025–26 to **36.0 %** — cut from 37 % at the 22 Oct 2026 PPK per TCMB Basın Duyurusu 2026-45 (37 % had been held at the 10 Sep 2026 PPK, 2026-38; checked 2026-11-25); rates may have changed since — re-check TÜİK monthly). **Verify TRY vs FX pricing on every listing.** (2026-09-24 verified)
- **Languages**: Turkish (official); English usable in tourist zones (İstanbul, Antalya, Bodrum, Alanya, Fethiye); Kurdish substantial in southeast (admin Turkish only).
- **Cadastre**: **TKGM** (Tapu ve Kadastro Genel Müdürlüğü) — title is **`Tapu Senedi`**. Online: `https://www.tkgm.gov.tr/` + **Web Tapu** (e-Devlet integration at `https://webtapu.tkgm.gov.tr/`).
- **Identifier**: `Tapu Senedi` carries `il / ilçe / mahalle/köy / ada no / parsel no / bağımsız bölüm no` (last for apartments).
- **Major reforms**:
  - **2012**: Tapu Kanunu Article 35 reciprocity expanded — foreigners from ~183 countries permitted (previously narrow reciprocity; "mütekabiliyet" requirement softened to government discretion).
  - **2017**: Citizenship by Investment program created (Cumhurbaşkanlığı Kararı 2017/9601), property route at $1,000,000.
  - **2018**: **TBDY 2018** (Türkiye Bina Deprem Yönetmeliği) — new earthquake-resistant building code, in force **1 Jan 2019**. New AFAD seismic hazard map at `https://tdth.afad.gov.tr/`.
  - **Sept 2018 → Jun 2022**: CBI threshold dropped to $250 k → raised to **$400,000** (current).
  - **Nov 2023 → 1 Jan 2024**: **Law 7464** (Konutların Turizm Amaçlı Kiralanmasına ve Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun) — mandatory İzin Belgesi for short-term rentals.
  - **Feb 2023**: Kahramanmaraş twin earthquakes, 6 Feb 2023 — **AFAD official magnitudes Mw 7.7** (Pazarcık, 04:17 TSİ) + **Mw 7.6** (Elbistan, 13:24 TSİ); USGS catalogues the same pair as Mw 7.8 + Mw 7.5, but AFAD is the only body legally authorised to publish Türkiye earthquake magnitudes — quote the AFAD pair (2026-08-07 verified). ~50,000 deaths. Triggered regulatory tightening on building inspection, DASK, and "kentsel dönüşüm" (urban transformation) acceleration.

## Section: `--price`

### Primary sources (official)

- **TÜİK Konut Fiyat Endeksi** (House Price Index, monthly — based on appraisal reports, hedonic): `https://data.tuik.gov.tr/Bulten/Index?p=Konut-Fiyat-Endeksi` (verify URL/liveness — this refresh sourced prices from TCMB KFE)
- **TCMB Konut Fiyat Endeksi** (Central Bank, monthly, hedonic; bulletin also carries the **Yeni Kiracı Kira Endeksi** — new-tenant rent index): `https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+menu/istatistikler/reel+sektor+istatistikleri/konut+fiyat+endeksi/` (verified live 2026-07-03)
- **TÜİK Konut Satış İstatistikleri** (sales count, monthly): `https://data.tuik.gov.tr/Kategori/GetKategori?p=insaat-ve-konut-116`

### Secondary / private benchmarks

- **REIDIN-GYODER Yeni Konut Fiyat Endeksi** (new-build price index, İstanbul focus): `https://gyoder.org.tr/` (paid pro tier; press releases free)
- **Endeksa** (machine-valuation, neighbourhood granularity): `https://www.endeksa.com/`
- **Hepsiemlak Konut Fiyat Endeksi** + **Sahibinden + Bahçeşehir Üniversitesi Endeksi**

### Listing platforms

- **sahibinden.com** — largest by far (≈ 65 % share of TR online property listings): `https://www.sahibinden.com/satilik/<il>-<ilce>` or `/kiralik/`
- **hepsiemlak.com** — full-broker: `https://www.hepsiemlak.com/<il>-<ilce>-satilik`
- **emlakjet.com**, **zingat.com**, **hurriyetemlak.com**

### Price benchmarks (Q4 2025 reference, TCMB average m² prices)

| Region / city | TRY/m² (Q4 2025 avg) | USD/m² (≈) | YoY change |
|---|---:|---:|---:|
| **Türkiye geneli** | ~45,457 | $973 | +26.1 % |
| **İstanbul** | ~74,153 | $1,588 | +33.6 % |
| **Ankara** | ~41,274 | $884 | +38.7 % |
| **İzmir** | ~49,584 | $1,062 | +30.8 % (TCMB KFE index, Dec 2025 — not a Q4 m² price change like the rows above) |
| **Antalya / Muğla coast** | est. mid-tier with foreign-buyer premium | est. $1,200–$2,000 | mid-20s % |

(Q4 2025 reference levels: TCMB average m² prices (TRY/m²) as reported by Bigpara/Hürriyet on 19 Jan 2026, a secondary report of the TCMB figures; YoY = Q4 2025 vs Q4 2024 m² price, computed: Türkiye 45,457 ÷ 36,061 = 1.261, İstanbul 74,153 ÷ 55,503 = 1.336, Ankara 41,274 ÷ 29,764 = 1.387; the İzmir and coast rows show the TCMB KFE index change to Dec 2025 instead (İzmir 30.8 %; Antalya–Burdur–Isparta 24.2 %, Aydın–Denizli–Muğla 25.4 %); USD figures computed at ~46.7 TRY/USD (TCMB indicative rate of 2 Jul 2026: 46.6080 buying / 46.6920 selling), e.g. 45,457 ÷ 46.7 ≈ 973 — TRY/m² levels are inflation-eroded; est ranges are judgment bands; rates may have changed since — re-pull TCMB's quarterly m² prices)

**By October 2026** (TCMB KFE Oct-2026 bulletin, primary) nominal YoY had eased to **+21.1 % nationally** (İstanbul +24.8 %, Ankara +22.7 %, İzmir +17.9 %), but **real YoY was −6.6 %** — Turkish housing is rising in TRY yet losing value against inflation. Re-pull TCMB KFE monthly; cross-check TÜİK KFE. (2026-11-25 verified, TCMB KFE Oct 2026)

### İstanbul district hierarchy (foreign-buyer relevant; verify per-district at sahibinden cenova haritası)

- **Premium**: Beşiktaş, Beyoğlu (Cihangir, Galata), Kadıköy, Üsküdar, Sarıyer, Bebek, Etiler — **est. $2,500–$5,000+/m²** for renovated or new
- **Mid (popular foreign buyer)**: Şişli, Kağıthane, Maltepe, Ataşehir — **est. $1,200–$2,500/m²**
- **Mid-affordable**: Esenyurt, Beylikdüzü, Başakşehir (heavy CBI inventory) — **est. $700–$1,500/m²**
- **Outer**: Pendik, Tuzla, Sultangazi, Esenler — **est. $500–$1,000/m²**

### Compute

1. Listing price/m² = listing price ÷ `brüt m²` (gross — includes wall thickness, common areas) OR `net m²` (interior only). **Clarify which on every listing — gap est. 15–25 %** (judgment band: brüt adds wall thickness and a share of common areas, so the gap widens with shared space; take both figures from the project's area table, not the listing).
2. Compare to TÜİK KFE for the il (province-level only — not parcel-specific).
3. Compare to Endeksa neighbourhood machine-valuation (mahalle-level granularity).
4. **Trap**: `0+1` = studio (no separate bedroom), `1+1` = one bed, `2+1` = two bed + lounge, `3+1` etc. — Turkish convention.
5. **Trap**: TRY vs USD/EUR — many İstanbul/Antalya listings quote in **USD** even when only TRY is legally tender. Verify the deed (`Tapu Senedi`) declared value vs informal price.
6. **Trap**: KDV inclusive vs exclusive on yeni proje (newbuilds) — `KDV dahil` (VAT incl.) vs `KDV hariç` (VAT excl.); see § Tax for rate tiers.
7. **Trap**: "Kat irtifakı" (pre-occupancy title) vs "kat mülkiyeti" (post-occupancy/iskan complete) — pre-occupancy title means the building lacks the final occupancy permit and bank financing may be restricted.

---

## Section: `--traffic`

### Primary sources

- **KGM (Karayolları Genel Müdürlüğü) Trafik ve Ulaşım Bilgileri**: `https://www.kgm.gov.tr/Sayfalar/KGM/SiteTr/Trafik/TrafikHacimHaritasi.aspx`
  - Annual `Trafik Hacim Haritası` (traffic volume map) — coverage: D + O (otoyol/motorway) network primarily; some state roads
  - Latest published map: 2023 data (rates may have changed since)
- **İBB (İstanbul Büyükşehir Belediyesi) Açık Veri Portalı**: `https://data.ibb.gov.tr/` — İstanbul-only; real-time traffic feeds, bus loads, metro
- **Yandex Traffic / Google Traffic** — only commercial-grade real-time fallback

### Key term

**YOGT (Yıllık Ortalama Günlük Trafik)** — Annual Average Daily Traffic, equivalent to AADT.

### Verdict bands

- 🟢 < 1,500 v/d (rural devlet yolu, köy yolu)
- 🟡 1,500–8,000 v/d (small il/devlet yolu, urban side street)
- 🟠 8,000–30,000 v/d (busy devlet yolu, urban arterial, smaller D-road)
- 🔴 > 30,000 v/d (otoyol, major D-road, urban core, İstanbul boğaz köprüleri)

### Coarse fallback (OSM `highway` class)

- `motorway` = otoyol (O-prefix)
- `trunk`/`primary` = devlet yolu (D-prefix)
- `secondary` = il yolu
- `tertiary` = köy yolu / minor connector
- `residential` = mahalle içi yol

---

## Section: `--tax`

### Annual property tax — Emlak Vergisi (Law 1319)

**Administered by**: belediye (municipality) — not central tax authority.

| Property type | Rate (small belediye) | Rate (Büyükşehir, ×2) |
|---|---:|---:|
| **Residential (mesken/konut)** | **0.1 %** | **0.2 %** |
| **Commercial (işyeri)** | 0.2 % | 0.4 % |
| **Building plot (arsa — land parcelled by the belediye)** | 0.3 % | 0.6 % |
| **Agricultural land (arazi)** | 0.1 % | 0.2 % |

(source GİB Emlak Vergisi Kanunu mad. 8; rates confirmed **unchanged for 2026** — Büyükşehir ×2 also unchanged; only the base values were re-set, see below. 2026-07-03 verified)

**Büyükşehir multiplier**: rates are **doubled** within boundaries of the 30 metropolitan municipalities (İstanbul, Ankara, İzmir, Antalya, Bursa, Konya, Adana, Gaziantep, Kayseri, Şanlıurfa, Diyarbakır, Mersin, Eskişehir, Hatay, Manisa, Kahramanmaraş, Samsun, Aydın, Balıkesir, Denizli, Erzurum, Kocaeli, Malatya, Mardin, Muğla, Ordu, Sakarya, Tekirdağ, Trabzon, Van).

### Base value: Emlak Vergisi Değeri

Property tax base = **rayiç bedel** (declared/appraised value) updated every 4 years by belediye + annual yeniden değerleme oranı (revaluation coefficient, set by Hazine ve Maliye Bakanlığı per Resmi Gazete).

- Latest 4-year valuation cycle: **2026–2029**. 2026 increases are now **capped by statute** — Law 7566 (RG 2025-12-19 No. 33112) added **geçici mad. 23** to the Emlak Vergisi Kanunu: 2026 bina/arazi vergi değerleri computed from the new takdir-komisyonu arsa/arazi birim değerleri **may not exceed the 2025 vergi değeri plus twice that amount (3×)** — statutory wording 'iki kat fazlasını geçemez'; Tebliğ 89 example: 2025 value 900,000 TL → 2026 cap 2,700,000 TL; values under the cap apply as computed, with no fixed multiplier (implemented by Emlak Vergisi Genel Tebliğ Seri No 89, RG 2025-12-31 No. 33124 5. mükerrer). 2027–2029 matrahs chain off these capped 2026 values. Note: Law 7566 md 11 also raises the annual uplift in non-takdir years from half to the **full** yeniden değerleme oranı (in force 19 Dec 2025 per the mevzuat.gov.tr consolidated text; it drives the 2027–2029 chain; the President may cut the uplift to zero, EVK Art. 29). Payment: 1st taksit by 31 May, 2nd by 30 Nov. Rates unchanged (see table above). (2026-07-03 verified)
- Yeniden değerleme oranı used for 2025 amounts (set for 2024): **43.93 %** (VUK Genel Tebliği Sıra No 574, RG 2024-11-27 No. 32735)
- Yeniden değerleme oranı used for 2026 amounts (set for 2025): **25.49 %** (VUK Genel Tebliği Sıra No 585, RG 2025-11-27 No. 33090; the Değerli Konut Vergisi amounts rise by half of it, 12.745 %, per Emlak Vergisi Genel Tebliği Seri No 88)

### Example calculation

100 m² konut, illustrative emlak vergisi değeri (rayiç bedel) 4,000,000 TRY, in **İstanbul (Büyükşehir)** — computed:
- Annual Emlak Vergisi = 4,000,000 × 0.002 = **8,000 TRY/yr** (~$171 at 1 USD ≈ 46.7 TRY, 2026-07 rate)

100 m² konut in **Bartın (not a Büyükşehir)**, illustrative emlak vergisi değeri (rayiç) 1,500,000 TRY — computed:
- Annual Emlak Vergisi = 1,500,000 × 0.001 = **1,500 TRY/yr** (computed; ~$32 at 46.67 TRY/USD, TCMB USD selling rate of 1 Jul 2026)

### Çevre Temizlik Vergisi (Environmental Cleaning / sanitation fee)

- Residential: charged **per m³ of water used** and collected on the su faturası (water bill): **4 TRY/m³ in Büyükşehir belediyeleri, 3 TRY/m³ in other belediyeler, 1.50 TRY/m³ in belediyeler under 5,000 people or in kalkınmada öncelikli yöreler (2026)** (Belediye Gelirleri Kanunu mük. md 44; Genel Tebliğ Seri No 59, RG 2025-12-31)
- Computed example (illustrative 120 m³ of water a year in a Büyükşehir): 120 × 4 = 480 TRY/yr
- Commercial: progressive by m² + activity tier

### High-Value Residential Tax — Değerli Konut Vergisi (since 2020)

For residences whose **bina vergi değeri** (the emlak vergisi value, not the market price) exceeds **15,709,000 TRY (2025)** / **17,711,000 TRY (2026; Emlak Vergisi Kanunu Genel Tebliği Seri No 88)** (2026-11-25 verified, source [GİB 2026 Değerli Konut Vergisi Rehberi PDF](https://cdn.gib.gov.tr/api/gibportal-file/file/getFile?objectKey=DUYURU/UNIVERSAL/2026/2026_Degerli_Konut_Vergisi_Rehberi.pdf)):

| Bracket 2026 (TRY rayiç bedel) | Rate |
|---|---:|
| 17,711,000 – 26,567,000 | 3 ‰ (binde 3) on the part above 17,711,000 |
| 26,567,000 – 35,425,000 | 6 ‰ (binde 6) on the part above 26,567,000, plus 26,568 TL for the first tier |
| > 35,425,000 | 10 ‰ (1.0 %) on the part above 35,425,000, plus 79,716 TL for the tiers below |

(2026 threshold per Emlak Vergisi Kanunu Genel Tebliği Seri No 88 / Emlak Vergisi Kanunu mad. 42; rates and tier amounts per mad. 44, in per-mille (binde) in the law; thresholds and tier limits rise each year by half the yeniden değerleme oranı)

### Transaction tax — Tapu Harcı (Title Deed Transfer Fee)

- **Total: 4 % of the declared sale value**, which may not be below the emlak vergisi değeri (492 sayılı Harçlar Kanunu, (4) sayılı tarife, 20(a): binde 20 from each party)
- Statutory split: **2 % buyer + 2 % seller**; in practice the parties often agree that the **buyer pays the full 4 %** (negotiable; curated wisdom from market practice, not statute)
- Calculated on declared sale value (must be ≥ rayiç bedel — under-declaration triggers GİB audit + ceza)
- Paid at TKGM Tapu Müdürlüğü on transfer day

### KDV (VAT) on residential sales

For NEW property sold by developer (yapı müteahhidi):

| Property net m² + class | KDV rate |
|---|---:|
| Law 6306 urban-transformation project (risky building or risk/reserve area), building permit from 1 Apr 2022 — part of net area up to 150 m² | **1 %** |
| Standard new build, building permit from 1 Apr 2022 — part of net area up to 150 m² (any location) | **10 %** |
| Part of net area above 150 m² (permit from 1 Apr 2022); the whole unit if net > 150 m² and the permit predates 1 Apr 2022 | **20 %** |

(rates per BKK 2007/13033 as amended by CB Kararı 5359 for permits from 1 Apr 2022 and CB Kararı 7346, which raised 8 %/18 % to 10 %/20 % from 10 Jul 2023 — GİB consolidated KDV rate list; units with a building permit from before 1 Apr 2022 keep the old rules: net ≤ 150 m² at 1 % outside büyükşehir and 1 %, 10 % or 20 % inside büyükşehir for luxury or first-class builds by arsa birim m² vergi değeri — verify with the developer's invoice)

**Resale (ikinci el)**: generally KDV exempt unless seller is a registered KDV mükellefi.

### KDV exemption for foreign first-time buyers (KDV Kanunu mad. 13/i)

Conditions (cumulative):
1. Buyer is **non-Turkish citizen + non-resident in Türkiye** (≥6 months physical absence) — or Turkish citizen with valid yabancı oturma izni in another country and >6 months abroad
2. Property is **first sale** (ilk teslim) — direct from developer or from Turkish citizen who acquired ≥3 years earlier
3. Property purchase **paid in foreign currency, transferred from abroad** to Turkish bank account (proof: dekont)
4. Property is **konut (residential) or işyeri (commercial)** — not arsa (land)
5. **Holding period: minimum 3 years** from acquisition (was 1 year; raised to 3 years by Law 7394 of 8 Apr 2022). Selling within 3 years requires paying the exempted KDV plus tecil faizi (6183 sayılı Kanun md 48) before the tapu transfer; if the conditions were not met, buyer and seller are jointly liable for the KDV, vergi ziyaı cezası and gecikme faizi.

Result: KDV **0 %** on qualifying purchase (saves the KDV the unit would otherwise carry, up to 20 %: for a konut with a building permit from 1 Apr 2022, 10 % on the part of the net area up to 150 m² and 20 % on the part above; 1 % in Law 6306 urban-transformation projects).

### Capital gains tax (Değer Artış Kazancı)

- Residential property held **> 5 years**: **EXEMPT** (Gelir Vergisi Kanunu mük. mad. 80)
- Held ≤ 5 years: gain (sale − indexed acquisition cost − allowable expenses) added to other income; progressive **15–40 %** brackets (2026 non-wage: 15 % to 190k, 20 % to 400k, 27 % to 1M, 35 % to 5.3M, 40 % above — wage-income bands differ, 27 % band runs to 1.5M; GİB Gelir Vergisi Genel Tebliği Seri No 332)
- Annual istisna for değer artışı kazancı: **150,000 TRY (2026)** (120,000 in 2025) — it applies to gains on real estate sold within 5 years, per GİB's 2026 guide to declaring real-estate gains. (2026-11-25 verified)

### Inheritance + gift tax — Veraset ve İntikal Vergisi

- Inheritance progressive **1–10 %**; gift progressive **10–30 %** (Veraset ve İntikal Vergisi Kanunu)
- Spouse + children istisna: **2,907,136 TL per heir (2026)**; spouse alone, no descendants: **5,817,845 TL (2026)** (Veraset ve İntikal VK Genel Tebliği Seri No 57, RG 2025-12-31 No. 33124 5. mükerrer); 2025 was 2,316,628 TL per heir. (2026-11-25 verified)

### Future risk

- **2026–2029 rayiç bedel cycle**: Law 7566 (geçici mad. 23) now caps 2026 increases **statutorily** — the 2026 matrah may not exceed 3× the 2025 vergi değeri (2025 value plus twice that amount; see § base value). Watch for challenges to the FULL-rate annual uplift that Law 7566 md 11 introduces for 2027–2029 (EVK md 29 now applies the whole yeniden değerleme oranı, no longer half). Source: Resmi Gazete + belediye ilan/notification. (2026-11-25 verified)
- **KDV on housing** is set by presidential decree and changes often: the 1 % rate for net ≤ 150 m² units ended for building permits from 1 Apr 2022 (except Law 6306 urban-transformation projects), and the 8 %/18 % rates became 10 %/20 % on 10 Jul 2023 — verify at https://www.gib.gov.tr/ (KDV oranları list) before signing.
- **Değerli Konut Vergisi** brackets revalued annually — luxury İstanbul buyers should track.

---

## Section: `--rental`

### Long-term residential — Gayrimenkul Sermaye İradı (GMSİ)

Gelir Vergisi Kanunu §70–74. Tax declared via annual Gelir Vergisi Beyannamesi (March).

#### Residential rental istisna (exemption) — 2026

- **58,000 TRY/yr** (mesken kira geliri istisnası, 2026; was 47,000 in 2025, 33,000 in 2024 — revalued annually by yeniden değerleme oranı)
- Applies once across all residential properties combined
- **Lost** if: (a) total income from all sources exceeds the high-bracket threshold, or (b) rental income not declared by deadline

(2026 threshold per GİB Gelir Vergisi Genel Tebliği Seri No 332, RG 2025-12-31 No. 33124 5. mükerrer; verify GİB annual update. 2026-11-25 verified)

#### Rent-increase cap (Türk Borçlar Kanunu mad. 344)

- Annual rent increases on existing residential leases are capped at the **12-month-average TÜFE** (CPI). The temporary 25 % ceiling (TBK geçici md. 1–2, added by Laws 7409 and 7456) covered renewal periods from June 2022 up to and including **1 Jul 2024**; from 2 Jul 2024 the cap reverted to the TBK mad. 344 12-month-average TÜFE ceiling.
- **October 2026 legal ceiling: 31.23 %** (12-month-average TÜFE from TÜİK's Oct-2026 CPI bulletin, as reported by Alomaliye — secondary; TÜİK's own Aug-2026 bulletin gave 31.79 %) — the applicable ceiling resets monthly; verify the renewal month's TÜFE 12-month average at `https://veriportali.tuik.gov.tr/`. (2026-11-25 checked)

#### Cost methods (must be uniform across all GMSİ)

- **Götürü Gider** (lump-sum): **15 % flat deduction** of gross — no documentation needed; simplest for non-resident foreigners. **Cannot revert to gerçek for 2 years once selected.**
- **Gerçek Usul** (actual): document all expenses (loan interest, insurance, repair amortization, depreciation, management fees) — better for high-cost properties

#### Rates — 2026 income brackets (non-wage / GMSİ)

| ZD bracket (TRY) | Rate |
|---|---:|
| 0 – 190,000 | 15 % |
| 190,001 – 400,000 | 20 % |
| 400,001 – 1,000,000 | 27 % |
| 1,000,001 – 5,300,000 | 35 % |
| > 5,300,000 | 40 % |

(2026 non-wage/GMSİ brackets per GİB Gelir Vergisi Genel Tebliği Seri No 332; revalued annually by yeniden değerleme oranı. **Wage-income upper bands differ** — the 27 % band runs to 1,500,000 and the 35 % band 1,500,000–5,300,000. 2026-11-25 verified)

#### Non-resident foreign owner

- Same GMSİ regime
- Beyanname filed via **Hazır Beyan Sistemi** at `https://hazirbeyan.gib.gov.tr/`
- No social security contribution on GMSİ (unlike Bağ-Kur for OSVÇ-equivalent)

### Short-term rentals (gunluk konut kiralama / Airbnb / Booking)

**Status as of 2026: permit-only regime.** Law 7464's permit rules have applied since 1 Jan 2024, and KTB provincial directorates publish the 2026 fine amounts (180,617–1,806,177 TRY).

#### Law 7464 (Konutların Turizm Amaçlı Kiralanmasına ve Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun)

- Published Resmi Gazete **2 Nov 2023** (No. 32357); its short-term-rental articles (mad. 1–6) in force **1 Jan 2024**: `https://www.resmigazete.gov.tr/eskiler/2023/11/20231102-16.htm`
- Implementing regulation (Yönetmelik): RG 28 Dec 2023
- **Definition**: konut kiralama for ≤ 100 nights consecutively to same tenant for tourism purposes
- **Mandatory İzin Belgesi** (Turizm Amaçlı Kiralanan Konut İzin Belgesi) issued by **Kültür ve Turizm Bakanlığı** via e-Devlet
- Application portal: `https://www.ktb.gov.tr/` + e-Devlet integration

#### Conditions for İzin Belgesi

1. Building "kat malikleri kurulu" (apartment owners' assembly) **unanimous consent** in writing — single objection blocks the permit
2. In buildings with more than three units, at most **25 % of the units** can be permitted to the **same owner** (kiraya veren); more than five units for one owner in one building also needs an işyeri açma ve çalışma ruhsatı (Law 7464 mad. 3(4)). Serviced high-end residences (yüksek nitelikli konutlar: reception, security and daily cleaning, with short lets allowed in the building's yönetim planı) are exempt from this cap and from the unanimous-consent rule above (mad. 3)
3. Turkish citizen or registered legal entity as license holder (foreign owners use TR-resident company or attorney)
4. Building must have **iskan (Yapı Kullanma İzin Belgesi)** — no permit on kat irtifakı stage

#### Penalties (Law 7464 mad. 4)

| Violation | Fine (TRY) |
|---|---:|
| Operating without İzin Belgesi — **3-stage progressive ladder** (NOT discretionary range) | Statutory base **Stage 1: 100,000 TRY/property + 15-gün süre to obtain permit; Stage 2 (still no permit): 500,000 TRY/property + 15-gün süre; Stage 3 (continued violation): 1,000,000 TRY** (Law 7464 mad. 4(1)(a), (b) and (f); [consolidated text](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.7464.pdf), 2026-11-25 verified). **Base fines are revalued annually by yeniden değerleme oranı — 2026 applied amounts are 180,617 / 903,088 / 1,806,177 TRY** (about ×1.806, rounded down; new figures land each January) (2026-11-25 verified, source [KTB Sakarya İl Kültür ve Turizm Müdürlüğü](https://sakarya.ktb.gov.tr/TR-362923/turizm-amacli-konut-ve-basvurulari.html)) |
| Misleading property description (konum/nitelik/fiziksel özellikler) | **100,000 TRY** statutory base, permit holders (mad. 4(2)(ç)); the 2026 revalued amount is not on the KTB pages checked — the other bases rose by about ×1.806 |
| Listing on platform without permit | **100,000 per property + access blocking after 24h notice** |
| Existing operators who missed the transition (geçici md. 1: apply within one month of 1 Jan 2024; applications decided within three months) | mad. 4 fines apply; rejected applicants must stop, though current guests' contracts run to term |
| Failure to remove unlicensed listing within 24h after Bakanlık notice | platform fine + listing removal |

#### Hosts on platforms (Airbnb, Booking)

- Platforms required to **verify İzin Belgesi number** before listing publishes
- Airbnb + Booking now request permit upload from TR hosts (post-2024); **Airbnb blocks listings lacking the Ministry İzin Belgesi number** (unverified listings cannot accept new bookings)
- Stays > 100 consecutive nights = pansiyon işletmeciliği regime (different licensing — Belediye İşyeri Açma Ruhsatı + Bağ-Kur)

#### Tax regime for short-term rental income

- **If Turkish-tax-resident**: GİB's Genel Yazı No. 7877 of 24 Jan 2025 treated short-term letting as ticari kazanç (commercial earnings, with KDV), but the Danıştay suspended it (3rd Chamber, 27 Oct 2025; 3rd and 7th Chambers jointly, 8 Apr 2026; GİB's objection rejected 29 Jun 2026): without a hotel-style commercial organisation the income stays GMSİ and no konaklama vergisi is due. No ruling on the merits was found as of 18 Nov 2026 (Alomaliye, secondary) — confirm the current position with a mali müşavir.
- **Non-resident foreign owner**: still GMSİ-eligible per practice; verify with mali müşavir.
- **Konaklama Vergisi** (accommodation tax, since 1 Jan 2023): **2 %** of accommodation revenue in the law, cut to **1 % from 1 May to 31 Dec 2026** (CBK 11263, RG 1 May 2026), back to 2 % from 2027 unless a new decision extends it; declared monthly. Under the Danıştay stay above, letting a dwelling without a commercial organisation is not subject.

### Strategic notes

- **İstanbul, Antalya, Bodrum, Kapadokya, Alanya, Fethiye, Çeşme**: highest yields; biggest regulatory + kat malikleri consent challenge
- **Building-level consent is the single hardest gate** — buy in blocks designed/zoned for STR or accept LTR-only
- **Konut Tipi Site / Komplekss with on-site management**: typically pre-arranged consent; ask for "site yönetimi izni" before purchase
- **EU Reg 2024/1028 (STR transparency)**: does NOT apply to TR (non-EU) but may indirectly affect platform behaviour for cross-border bookings

---

## Section: `--work=<profession>`

### Job platforms

- **kariyer.net** — largest, white-collar focus: `https://www.kariyer.net/`
- **secretcv.com**, **eleman.net**, **yenibiriş.com**
- **indeed.com.tr**, **LinkedIn TR** (very active in IT, finance, holdings, big corporates)
- **İŞKUR** (Türkiye İş Kurumu, public employment service): `https://www.iskur.gov.tr/`

### Self-employment regimes

- **Şahıs Şirketi** (sole proprietorship) — simplest, registered at vergi dairesi; basit usul or gerçek usul gelir vergisi
  - Basit usul (small traders): 2026 limits — annual purchases ≤ 1,200,000 TRY or sales ≤ 1,900,000 TRY (trading), gross receipts ≤ 600,000 TRY (services), workplace rent ≤ 99,000 TRY/yr inside büyükşehir limits (60,000 elsewhere); the business profit (ticari kazanç) is exempt from income tax (GVK mükerrer 20/A, Law 7338); records kept through the Defter-Beyan Sistemi
  - Gerçek usul: full ledger; brackets 15–40 %
- **Limited Şirket (Ltd. Şti.)** — corporate, 50,000 TRY minimum capital (since 1 Jan 2024, CBK 7887); kurumlar vergisi **25 %** (30 % for banks, finance, insurance and similar firms, KVK mad. 32); kâr payı stopajı **15 %** (raised from 10 % on 22 Dec 2024, CBK 9286)
- **Anonim Şirket (A.Ş.)** — joint stock, 250,000 TRY minimum; same kurumlar vergisi
- **Bağ-Kur (4/1-b SGK)** social security: mandatory for self-employed; 2026 monthly minimum **11,808.23 TRY** (10,156.73 TRY with the 5-point discount for those who pay on time), on the 33,030 TRY minimum earnings base

### Salaried benchmarks (2025 brüt avg)

- **Asgari ücret 2026 (minimum wage)**: **33,030.00 TRY/ay brüt** (net 28,075.50 TRY, günlük brüt 1,101.00 TRY) — **+27 %** vs 2025 (26,005.50 brüt / 22,104.67 net); Asgari Ücret Tespit Komisyonu Kararı, effective 1 Jan 2026 (RG 26 Dec 2025 No. 33119). 2026-11-25 verified.
- **Median brüt 2025**: data not publicly available — verify TÜİK Hanehalkı İşgücü Anketi
- **İstanbul beyaz yaka median**: est. 50,000–80,000 TRY/ay (mid-career, white-collar sectors)
- **IT/finance senior İstanbul**: est. 100,000–250,000 TRY/ay; FX-indexed comp common

### Foreign worker permit

- **Çalışma İzni** required from **Çalışma ve Sosyal Güvenlik Bakanlığı**
- Online application: `https://ecalismaizni.csgb.gov.tr/`
- Quota: typically 1 foreign worker per 5 TR-citizen workers in same employer
- Independent professional (e.g., remote work for foreign employer): use **kısa dönem ikamet izni** + register as serbest meslek with vergi dairesi

### Catchment heuristics

- Within 60 min of one of 30 Büyükşehir centres: meaningful labour market
- Outside Büyükşehir + > 60 min from major city: thin (tourism, agriculture, public sector dominant)
- **Tier-1 (best foreign-friendly job markets)**: İstanbul, Ankara, İzmir
- **Tier-2 (sectoral)**: Antalya (tourism + tech hub emerging), Bursa (auto), Gaziantep (industry), Mersin (logistics)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **AFAD Türkiye Deprem Tehlike Haritası** | `https://tdth.afad.gov.tr/` | Site-specific PGA, SS, S1, SDS, SD1, PGV per coordinates + soil class (ZA–ZE) |
| **AFAD ana portalı** | `https://www.afad.gov.tr/` + `https://deprem.afad.gov.tr/` | Real-time seismicity, historic catalog, fault maps |
| **MTA Diri Fay Haritası** (active fault map) | `https://www.mta.gov.tr/v3.0/hizmetler/yenilenmis-diri-fay-haritalari` | 1:25k active fault traces |
| **MTA Heyelan Envanteri** (landslide) | `https://www.mta.gov.tr/v3.0/hizmetler/heyelan-envanteri` | Historic landslide registry |
| **DSİ Taşkın Haritaları** (flood) | `https://www.dsi.gov.tr/` | River + flood plain mapping (district/basin level — parcel-level limited) |
| **Çevre Bakanlığı / Atlas** | `https://atlas.gov.tr/` | National geo-portal incl. zoning + protected areas |
| **MGM** (Meteoroloji Genel Müdürlüğü) | `https://www.mgm.gov.tr/` | Climate normals, extreme weather |
| **Tarım ve Orman Bakanlığı orman yangını** | `https://www.ogm.gov.tr/` | Wildfire risk + history |

### Earthquake — the single dominant risk

- **TR is one of the world's most seismically active countries** (North Anatolian + East Anatolian + Aegean fault systems)
- **2023 Kahramanmaraş twin earthquakes, 6 Feb 2023 — AFAD Mw 7.7 (Pazarcık, 04:17 TSİ) + Mw 7.6 (Elbistan, 13:24 TSİ)**: ~50,000 deaths, ~300,000 buildings collapsed/severely damaged — exposed widespread non-compliance with prior building codes. USGS catalogues the same pair as Mw 7.8 + Mw 7.5; AFAD is the only body legally authorised to publish Türkiye earthquake magnitudes, so quote the AFAD pair ([AFAD Kahramanmaraş Depremleri Ön Değerlendirme Raporu](https://deprem.afad.gov.tr/assets/pdf/Kahramanmaras%20%20Depremleri_%20On%20Degerlendirme%20Raporu.pdf), 2026-08-07 verified)
- **AFAD seismic hazard map (2018)** publishes site-specific PGA at `https://tdth.afad.gov.tr/` — input coords + soil class

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1975** | No earthquake-aware code; weak masonry; lead pipes; no insulation; asbestos in roofing common |
| **1975 (DBYBHY-75)** | First nationwide earthquake code — minimal by modern standards |
| **1998 (DBYBHY-98) post-Marmara prep** | Updated post-Erzincan; still inadequate vs Marmara 1999 reality |
| **1999 Marmara M7.6** | ~17,000 deaths — code revised 2007 (DBYBHY-2007) |
| **2007 (DBYBHY-2007)** | Improved but still using 1996 hazard map; widespread non-compliance |
| **2018 (TBDY-2018 — RG 18 Mar 2018 No. 30364 mükerrer, in force 1 Jan 2019)** | Site-specific spectra, modern hazard map, tall-building + base-isolation provisions; **the watershed code** and the current baseline (AFAD's TBDY page, 2026-11-25 checked: published 18 Mar 2018, in force 1 Jan 2019) |
| **Post-2023 Kahramanmaraş** | "kentsel dönüşüm" (urban transformation) accelerated by Law 7471 (RG 9 Nov 2023 No. 32364), which amended Law 6306: decisions now need a simple majority of shares (was two-thirds), and the Ministry's powers under the law passed to the Kentsel Dönüşüm Başkanlığı |

**Practical rule**: pre-1999 buildings in seismic zones = high risk unless visibly güçlendirme (retrofit/strengthening) certified; post-2018 buildings designed to TBDY-2018 are substantially safer (subject to actual construction quality — verify yapı denetim raporu).

### Mandatory documents at sale

| Document | Required because | Notes |
|---|---|---|
| **Tapu Senedi (deed)** | Always — TKGM verifies ownership + encumbrances | Web Tapu allows e-verification |
| **DASK Poliçesi (earthquake insurance)** | Mandatory for residential (Zorunlu Deprem Sigortası) — still compulsory, enforced at electricity/water subscription and tapu/konut-kredisi checkpoints (2026-08-07 verified) | See cost block below; 2026 tariff live and ÜFE-indexed monthly |
| **Yapı Kullanma İzin Belgesi (iskan)** | Confirms building completed + permit-compliant | Older buildings may lack — flag |
| **Enerji Kimlik Belgesi (EKB)** | Required in sale and rental transactions since **1 Jan 2020** — BEP Yönetmeliği mad. 25(15), deferred to that date by geçici md. 5 (RG 28 Apr 2017); existing buildings originally had ten years from the Enerji Verimliliği Kanunu (RG 2 May 2007), i.e. to 2 May 2017, to get one | 10-year validity; classes A–G |
| **İmar Durumu Belgesi** | Issued by belediye — confirms zoning + permitted use | Needed if buyer plans extension |
| **Kat Mülkiyeti vs Kat İrtifakı** | Tapu type — see Quirks | Pre-iskan → kat irtifakı |
| **Site/Apartman Aidat Borcu Yoktur Yazısı** | If kat mülkiyetli site/apartman | At signing |

**EKB at sale**: the owner must give the buyer or tenant a copy (BEP Yönetmeliği mad. 25(15)); do not count on the tapu office to check it — buyer should insist.

### Climate change projections

- **MGM** + **EU Copernicus C3S**: TR Mediterranean climate warming faster than global average
- **Aegean / Mediterranean coast**: drought intensifying; heat days TX≥35°C rising sharply (Antalya, Adana, Mersin ~60+ such days/yr by mid-2020s, est. may rise toward ~90/yr by 2050 — figures not bound to a specific scenario/dataset year here; verify at MGM + Copernicus C3S)
- **İstanbul + Marmara**: heat island + irregular precipitation; flash floods rising
- **Eastern Anatolia**: temp rise + glacier loss in Doğu Karadeniz; heavy snow → rain transition
- **Wildfire**: 2021 Antalya/Muğla mega-fires (160k ha) presaging trend; Aegean coast highest risk

---

## Section: `--mains`

### Major water + sewer utilities (regional)

| Utility | Coverage | URL |
|---|---|---|
| **İSKİ** (İstanbul Su ve Kanalizasyon İdaresi) | İstanbul metro | `https://www.iski.istanbul/` |
| **ASKİ** (Ankara) | Ankara metro | `https://www.aski.gov.tr/` |
| **İZSU** (İzmir) | İzmir metro | `https://www.izsu.gov.tr/` |
| **ASAT** (Antalya) | Antalya metro | `https://www.asat.gov.tr/` |
| **BUSKİ** (Bursa) | Bursa metro | `https://www.buski.gov.tr/` |
| **KOSKİ** (Konya), **MUSKİ** (Muğla), **AYDEM** (Aydın), **MASKİ** (Mersin) | respective Büyükşehirs | per official portal |
| **DSİ** (Devlet Su İşleri) | National water resources, irrigation | `https://www.dsi.gov.tr/` |
| Local belediye | Smaller cities + rural | per belediye portal |

### Verification

1. Check **belediye portal** > "Su ve Kanalizasyon" or call belediye santral
2. Listing language:
   - "şehir suyu" / "belediye suyu" + "kanalizasyon" = mains water + mains sewer
   - "şehir suyu var, kanalizasyon yok" = mains water but no mains sewer (septik tank)
   - "kuyu suyu" = well water (rural, common)
   - "fosseptik" / "septik" = cesspit; "BÖSAS" / "bireysel arıtma" = individual treatment plant
3. **Most Büyükşehir districts have mains water + sewer**; **rural villages (köy) often lack mains sewer**, especially in Doğu Anadolu, Karadeniz, Güneydoğu Anadolu

### Costs (2026 typical, TRY)

| Scenario | Cost |
|---|---:|
| Connection fee (where mains exists at street) | 5,000–25,000 |
| Mains drain construction (rural property, trunk in village) | 30,000–150,000 |
| Septik tank install / replacement | 25,000–80,000 |
| Bireysel arıtma (modern compliant package plant) | 80,000–250,000 |
| Kuyu açtırma (bore well, depth-dependent) | 15,000–80,000 |

(2026 estimates from market reports + insaat platforms; verify current quotes — TRY inflation moves prices monthly)

---

## Cost benchmarks (TR 2026)

| Work | Cost (TRY) |
|---|---:|
| **DASK** (100 m² betonarme) | **~830–3,200/yr** by risk zone — computed: insured sum 1,135,700 (100 m² × 11,357 TL/m², 01.07.2026 birim) × zone rate 0.73–2.82‰; high-hazard Marmara/İstanbul at upper end (verify per address via dask.gov.tr adres kodu lookup; before renewal discounts). 2026-07-03 verified |
| **DASK** (200 m² betonarme) | **~1,660–6,400/yr** (same method; insured sum 2,271,400 TL) |
| **DASK azami teminat (Nov 2026)** | up to **2,605,100 TRY** total cover per policy (from 01.11.2026; 2,648,084 from 01.12.2026) — revalued **monthly** by TÜİK Yİ-ÜFE since 1 Jan 2024 (DASK tarife; 01.01.2026 was 2,095,462, 01.07.2026 was 2,407,723); betonarme birim 12,288 TRY/m² (01.11.2026; 11,357 on 01.07.2026). 2026-11-25 verified |
| **Avukat / hukuki danışman** (transaction lawyer) | ~1–3 % of price est. (negotiable; market practice, not a legal tariff — calibration: the range foreign-buyer guides quote, no official survey of conveyancing fees was found; minimum fees: yearly Avukatlık Asgari Ücret Tarifesi, verify at https://www.barobirlik.org.tr/) |
| **Tapu Harcı total** | 4 % of declared sale value |
| **Tercüman (sworn translator)** for foreign buyer at TKGM | 2,000–5,000/transaction |
| **EKB (Enerji Kimlik Belgesi)** for rodun tip residential | 500–2,500 |
| **Yapı denetim hizmet bedeli** (newbuilds; agreed in the owner's yapı denetimi contract) | 1.75 % of approximate construction cost up to 1,000 m² built area, 1.5 % up to 50,000 m², 1.25 % above; up to 3.5 % for jobs not assigned electronically (Law 4708 md 5) |
| **Bağımsız değerleme raporu** (SPK-licensed valuation, mandatory for CBI) | 5,000–25,000 depending on property |
| **Notary (noter)** for satış vaadi sözleşmesi (preliminary contract) | 1,500–8,000 |
| **Konut sigortası** (full home insurance, optional) | 2,000–10,000/yr per 100 m² |
| **Total transaction cost (foreign buyer side)** | **~5–8 % of price est.** when the buyer pays the full 4 % Tapu Harcı (4 % + lawyer 1–3 % + valuation 5,000–25,000 + translator 2,000–5,000 TRY, about 0.2–0.8 % of a 4,000,000 TRY home); **~3–6 % est.** if the 2 % / 2 % statutory split holds. Calibration: built from the rows above, not from a survey |

(2025–2026 estimates; verify current quotes — TRY inflation rapidly outdates these)

## Active fiscal incentives (2025–2026)

- **KDV exemption for foreign first-time buyer** — see § Tax (KDV Kanunu mad. 13/i)
- **Citizenship by Investment** — $400,000 property route (3-year resale lock); see § Quirks
- **TOKİ (Toplu Konut İdaresi)** social housing programs — first-time buyer Turkish-citizen schemes (foreigners not eligible for most TOKİ): `https://www.toki.gov.tr/`
- **Konut Hesabı (Devlet Katkılı)** — government top-up savings for Turkish first-time buyers
- **Yeşil Bina Sertifikası / Yeşil Konut kredisi** — green-build mortgages from state banks (Ziraat, Halk, Vakıf) at preferential rates
- **Lisanssız Üretim (rooftop solar self-consumption)**: under EPDK Lisanssız Elektrik Üretim Yönetmeliği — net-metering via dağıtım şirketi; up to 25 kW per uninterrupted point
- **Kentsel Dönüşüm (Law 6306 urban transformation)**: subsidized loans + tax breaks for tearing down + rebuilding pre-2000 risky buildings; particularly active post-2023

## Common listing platforms

- **sahibinden.com** — largest by far, full extraction; subscription gating on contact info
- **hepsiemlak.com** — broker-listed, well-photographed
- **emlakjet.com**, **zingat.com**, **hurriyetemlak.com**
- **endeksa.com** — automated valuation + neighbourhood analytics
- **emlak8.com** (newbuilds)
- Foreign-buyer focus: **propertyturkey.com**, **antalyahomes.com**, **istanbulhomes.com** (typically markup-included)

## Caveats unique to TR

- **TRY hyperinflation makes long-term comparisons tricky** — always check date + USD-equivalent. CPI hit 85.51 % YoY Oct 2022, re-peaked ~75 % YoY May 2024, ~44 % end-2024, low-30s late 2025, ~32.6 % YoY May 2026, **31.51 % YoY Aug 2026** (TÜİK, quoted in TCMB PPK summary 2026-42); rates may have changed.
- **Foreign-buyer pricing premium est. ~15–35 %** in Antalya, Alanya, Bodrum, Fethiye — qualitative, based on the EN-language vs TR-language sahibinden listing spread, not a sourced benchmark; verify per listing.
- **CBI threshold + rules change frequently** — $1M (2017) → $250k (Sept 2018) → **$400k (June 2022, current)**. 3-year resale lock + once-only-per-property restriction; some districts excluded (İstanbul + Antalya have ilçe-level exclusions for tightening). Verify Cumhurbaşkanlığı + Resmi Gazete.
- **Earthquake risk dominates in Marmara, Aegean, Eastern Anatolia, southeast** — never skip AFAD lookup at `https://tdth.afad.gov.tr/`.
- **TBDY 2018 is the building-quality watershed**: post-2019 in-force = substantially safer in design; pre-1999 = high risk unless retrofit-certified.
- **Post-Kahramanmaraş 2023 regulatory tightening**: yapı denetim audits, DASK enforcement, kentsel dönüşüm acceleration via Law 6306 — buyers should expect more scrutiny on older buildings.
- **Web Tapu enables online deed transfer** (since 2018) but in-person at TKGM Tapu Müdürlüğü still standard for foreigners + transactions involving foreign currency.
- **KDV exemption for foreign first-time buyers** has strict conditions: (a) FX bring-in proof via dekont, (b) 3-year holding period (raised from 1 year by Law 7394 of 8 Apr 2022), (c) first-sale (ilk teslim) only, (d) buyer non-resident.
- **Foreign-buyer 30-hectare cap nationwide per individual** (Tapu Kanunu mad. 35); plus military restricted zones (verify with Genelkurmay confirmation via TKGM).
- **Reciprocity list** (~183 countries permitted): some nationalities (e.g., Syria, Armenia, North Korea, Cuba) restricted; verify current list with TKGM + İçişleri Bakanlığı.
- **Kat irtifakı vs kat mülkiyeti** — buying a unit on kat irtifakı (pre-iskan) means the building lacks final occupancy permit; bank financing limited; resale risk; insist on iskan before close.
- **Money laundering (MASAK) regulations** since 2021 require all property purchases > 75,000 TRY to flow through bank with full documentation.

## Reddit / forum sources

- **r/Turkey**, **r/istanbul**, **r/turkishlearning** — bilingual mix
- **r/expats**, **r/expat_in_Turkey**, **r/IWantOut** (relocation discussions)
- **turkishliving.com** forum — long-time expat discussion (Aegean coast skew)
- **bodrumlife** + **antalya-expats** Facebook groups
- **eksisozluk.com** — Turkish public-discussion site; useful for sentiment on specific developers, sites, neighbourhoods (search "<developer> şikayet" or "<site adı> deneyim")
- **sikayetvar.com** — consumer complaint registry for developers/agents

## Verification authorities

| Authority | When to call |
|---|---|
| **TKGM Tapu Müdürlüğü** (district registry) | Tapu verification, encumbrance check, transfer |
| **TKGM Web Tapu** | Online verification + select online transactions |
| **Belediye İmar ve Şehircilik Müdürlüğü** | İmar Durumu (zoning), kentsel dönüşüm status, building permit history |
| **AFAD İl Müdürlüğü** | Seismic risk + DASK confirmation |
| **GİB (Gelir İdaresi Başkanlığı)** | Tax liability, rayiç bedel, KDV exemption application |
| **Çevre Şehircilik ve İklim Değişikliği Bakanlığı il müdürlüğü** | EKB issuing authority, environmental compliance |
| **Bakanlık Göç İdaresi (PMM)** | Foreign residency permit (ikamet) |
| **Kültür ve Turizm Bakanlığı il müdürlüğü** | Law 7464 İzin Belgesi for short-term rental |
| **DASK** (Doğal Afet Sigortaları Kurumu) | Earthquake insurance — `https://www.dask.gov.tr/` |
| **Bağımsız SPK-lisanslı değerleme uzmanı** | CBI valuation report |
| **Avukat (lawyer)** + **mali müşavir (CPA)** | Transaction + tax compliance |

## Quirks to know

- **Kat irtifakı vs kat mülkiyeti** (the most important quirk):
  - **Kat irtifakı** (construction servitude title) = pre-occupancy, building under construction or iskan not yet issued; you own the air-rights share but not the finished unit yet. Banks restrict lending; resale harder.
  - **Kat mülkiyeti** (condominium ownership) = post-iskan, full ownership of the bağımsız bölüm (independent section). This is what you want.
  - Conversion: must apply to TKGM after iskan issuance — sometimes delayed by years if developer disputes.
- **İmar Durumu** (zoning status): always pull from belediye before purchase — specifies allowed yapı yüksekliği, taban alanı katsayısı (TAKS), kat alanı katsayısı (KAKS); non-permitted extensions on existing buildings are common and unauthorised.
- **Iskan (Yapı Kullanma İzin Belgesi)** often missing on older buildings or kaçak ilave (illegal extensions); makes utility connection + sale harder.
- **Bağımsız değerleme uzmanı** (SPK-licensed valuer) — required for CBI; must be on SPK list; report binds the deed declared value upward. Since TKGM's Sep-2026 change (announcement 29 Sep 2026) any SPK-authorised valuation firm may prepare the report behind the Tutar Tespit Belgesi (TTB), requested via WebTapu/TADEBİS; the gap between TTB and the tapu application may not exceed 12 months (2026 data, source TKGM yourkeyturkiye.gov.tr/vatandaslik-kazanimi, read 2026-10-21).
- **Bilirkişi (court-appointed expert)** for property tax disputes (rayiç bedel itiraz).
- **Foreign-buyer 30-hectare cap nationwide per individual** under Tapu Kanunu mad. 35 — including all properties combined.
- **Military-restricted zones**: TKGM checks against Genelkurmay before transferring to foreigners; ~5 % of country area; verifiable only at transaction time.
- **MASAK (Mali Suçları Araştırma Kurulu)**: anti-money-laundering — purchases > 75 k TRY must flow through Turkish bank with FX dekont if foreign-funded.
- **Tapu cinsi**: residential ("mesken"), commercial ("dükkan", "büro"), agricultural ("tarla"), olive grove ("zeytinlik" — special legal protection), forest ("orman" — generally cannot be private title); always verify cinsi on the deed.
- **Site yönetimi** (gated community management): aidat (monthly fee) varies hugely 1,000–10,000+ TRY/ay; check site karar defteri for past disputes.
- **Vergi numarası**: foreign buyers must obtain a TR vergi numarası (tax ID) before TKGM transfer — issued same-day at any vergi dairesi with passport.

## Source URL templates

| Source | URL pattern |
|---|---|
| TKGM main | `https://www.tkgm.gov.tr/` |
| Web Tapu | `https://webtapu.tkgm.gov.tr/` |
| AFAD seismic hazard map | `https://tdth.afad.gov.tr/` |
| AFAD main | `https://www.afad.gov.tr/` |
| MTA active fault map | `https://www.mta.gov.tr/v3.0/hizmetler/yenilenmis-diri-fay-haritalari` |
| MGM (meteorology) | `https://www.mgm.gov.tr/` |
| TÜİK Konut Fiyat Endeksi | `https://data.tuik.gov.tr/Bulten/Index?p=Konut-Fiyat-Endeksi` |
| TCMB (CBRT) | `https://www.tcmb.gov.tr/` |
| GİB (tax authority) | `https://www.gib.gov.tr/` |
| GİB Hazır Beyan (rental income) | `https://hazirbeyan.gib.gov.tr/` |
| DASK | `https://www.dask.gov.tr/` |
| DSİ flood + water | `https://www.dsi.gov.tr/` |
| sahibinden | `https://www.sahibinden.com/satilik/<il>-<ilce>` |
| hepsiemlak | `https://www.hepsiemlak.com/<il>-<ilce>-satilik` |
| emlakjet | `https://www.emlakjet.com/satilik-konut/<il>-<ilce>/` |
| Endeksa | `https://www.endeksa.com/tr/analiz/<il>/<ilce>/satilik/konut` |
| Resmi Gazete | `https://www.resmigazete.gov.tr/` |
| Çalışma İzni başvurusu | `https://ecalismaizni.csgb.gov.tr/` |
| Kültür ve Turizm Bakanlığı (Law 7464 İzin Belgesi) | `https://www.ktb.gov.tr/` |
| TOKİ | `https://www.toki.gov.tr/` |
| e-Devlet (citizen portal) | `https://www.turkiye.gov.tr/` |

## Status

✅ **Fully populated** (initially populated 2026-05-01).

**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources (TKGM, TÜİK, AFAD, GİB, MTA, MGM, DSİ, Resmi Gazete) + cost benchmarks + caveats + 2025 rates date-stamped.

**Confidence**:
- **HIGH** for cadastre/foreign-buyer rules/CBI mechanics/Law 7464 STR rules (all sourced to primary law + RG + TKGM/Bakanlık portals).
- **MEDIUM** for current-year tax thresholds — TRY hyperinflation means yeniden değerleme oranı + GMSİ istisna + Değerli Konut Vergisi brackets revalue annually; 2026 figures verified against the December 2025 RG circulars (2026-07-03) but must be re-checked each January.
- **MEDIUM** for parcel-level price benchmarks — TÜİK KFE is province-level only; mahalle-level requires Endeksa or sahibinden cenova haritası lookup per address.
- **MEDIUM** for STR enforcement — Law 7464 mature but municipal enforcement variance; provisional permit transition (31 Dec 2024) closed but ongoing audit risk.

**Last verified**: 2026-08-07 (§ --risks re-verified — Kahramanmaraş magnitudes corrected to the AFAD official pair Mw 7.7 + Mw 7.6, TBDY 2018 confirmed as the current code with no successor enacted, DASK compulsory-cover checkpoints confirmed; balance of the 2026-07-03 Tier-A quarterly refresh unchanged). Macro tracker entries re-checked 2026-09-24 in the October regwatch wave (see shared/regulatory-watch.md). Starlink (connectivity), Kahramanmaraş (risks), Emlak Vergisi 2026 status (tax) and CBI threshold (visa) tracker entries re-checked 2026-10-21 (December regwatch wave, run early; see shared/regulatory-watch.md).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--mains` | 2026-11-25 | 2026-11-25 maintenance run | Every figure re-read on its recorded source, or the source unchanged. |
| Cost benchmarks (TR 2026) | 2026-11-25 | 2026-11-25 maintenance run | DASK cover now 2,605,100 TL (November 2026, DASK tariff page); yapı denetim fees follow Law 4708 md 5; lawyer and total transaction costs are estimates built from the table's rows. |

## Extension TODOs (deepen on first real run)

- [ ] Per-Büyükşehir Emlak Vergisi rayiç bedel revaluation (2026–2029 cycle) — capture per-belediye new declared values
- [ ] Per-il KGM YOGT data extraction (latest published year)
- [ ] Mahalle-level Endeksa machine-valuation parsing for top 200 mahalleler
- [ ] CBI exclusion district list (İstanbul + Antalya have ilçe-level exclusions tightening; track Cumhurbaşkanlığı kararı + İçişleri Bakanlığı circulars)
- [ ] Post-Kahramanmaraş kentsel dönüşüm (Law 6306) per-il subsidy + risk-building list
- [ ] Yabancı uyruklu (foreign-buyer) transaction stats per il (TÜİK quarterly)
- [ ] DASK premium calculator integration for parcel-level estimate (gross m² × construction class × city-zone)

## Update history

- **2026-11-25** — Maintenance run: closed `--mains`, Cost benchmarks (TR 2026); still open `--price`, `--tax`, `--rental`, `--work=<profession>`, `--risks`.
