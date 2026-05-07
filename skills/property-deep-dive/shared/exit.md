# Universal `--exit` Section

Sell-side conditions: time-on-market (DOM), agent commission structure, contract norms, off-market vs MLS, sell-side closing costs, liquidity rating. Buyers should understand how easy it will be to **exit** a property before committing to buy.

**Snapshot**: May 2026 (Tier-5 additions — 87 countries total).

## Universal contract

For the property's country, return:
1. **Typical days-on-market (DOM)** — capital + secondary
2. **Agent commission structure** — buyer-pays / seller-pays / split, % of sale price
3. **Standard agency contract** — exclusive (mandate) vs open; duration; cooling-off
4. **Off-market vs MLS** — does country have true MLS or is off-market dominant?
5. **Average price discount** vs initial asking
6. **Sell-side closing costs as % of sale price**
7. **Liquidity rating**: HIGH / MEDIUM / LOW / VERY LOW
8. **Resale-market quirks**

## Output template

```markdown
## Exit Profile

**Country**: <ISO2>
**DOM (capital / secondary)**: <range>
**Agent commission**: <structure + %>
**Contract**: <type, duration, cooling-off>
**MLS**: <true MLS | portal-driven | off-market dominant>
**Asking → sale gap**: <%>
**Sell-side closing %**: <range>
**Liquidity**: <HIGH | MEDIUM | LOW | VERY LOW>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Region files

Country-level exit data lives in per-region files under [`exit/`](./exit/). Each file is a self-contained block; cross-region patterns and the liquidity heatmap remain in this index.

| Region | File | Countries |
|---|---|---|
| Western Europe | [`exit/western-europe.md`](./exit/western-europe.md) | FR, IT, DE, AT, CH, LI, MC, AD, NL, BE, LU, IE, UK |
| Iberia / Mediterranean | [`exit/iberia-mediterranean.md`](./exit/iberia-mediterranean.md) | ES, PT, GR, CY, MT |
| Nordics | [`exit/nordics.md`](./exit/nordics.md) | SE, FI, NO, DK, IS |
| CEE / Baltics | [`exit/cee-baltics.md`](./exit/cee-baltics.md) | CZ, SK, PL, HU, SI, HR, EE, LV, LT, RO, BG, MD |
| Western Balkans | [`exit/western-balkans.md`](./exit/western-balkans.md) | RS, ME, BA, MK, AL |
| Anglo non-EU | [`exit/anglo-non-eu.md`](./exit/anglo-non-eu.md) | US, CA, AU, NZ |
| Latin America | [`exit/latin-america.md`](./exit/latin-america.md) | MX, BR, AR, CR, PA, DO, CO, UY, CL, PE, EC, PY |
| MENA / Levant / North Africa | [`exit/mena-levant-north-africa.md`](./exit/mena-levant-north-africa.md) | TR, AE, QA, SA, IL, MA, TN, EG, JO, OM, BH, KW, LB |
| Sub-Saharan Africa | [`exit/sub-saharan-africa.md`](./exit/sub-saharan-africa.md) | ZA, NG, KE |
| Asia-Pacific | [`exit/asia-pacific.md`](./exit/asia-pacific.md) | JP, TH, ID, MY, VN, PH, SG, HK, KR, TW, MO |
| South Asia | [`exit/south-asia.md`](./exit/south-asia.md) | IN |
| Caucasus | [`exit/caucasus.md`](./exit/caucasus.md) | GE, AM, AZ |

## Liquidity heatmap (4-tier composite)

| Tier | Countries |
|---|---|
| **HIGH** (DOM <60d, MLS/portal transparency, deep buyer pool) | NL, SE, NO, IE, UK (excl. chain), CA, AU, NZ, US (metros + Sun Belt), parts of ES (Madrid/BCN/Costa del Sol), PT (Lisbon/Porto/Algarve), DE top-7, CH (Zurich/Geneva), AE (Dubai prime), ZA (Cape Town Atlantic), **SG (CCR Districts 9/10/11)** |
| **MEDIUM** (DOM 60-150d) | FR (urban), IT (Milan/Rome), AT, BE (urban), DK, CZ, PL, HU (Budapest), HR coast, EE, LT, RO (Cluj/BUC), GR (Athens), CY (Limassol), MT, MX (CDMX/Riviera), TR (Istanbul prime), JP (Tokyo 23-ku), TH (Bangkok CBD), GE (Tbilisi), IL (Tel Aviv), CO (Medellín/Bogotá), CL (Santiago prime), UY (Montevideo), **HK (HK Island prime + Kowloon prime)**, **KR (Seoul Gangnam-gu / Seocho-gu / Yongsan-gu)**, **TW (Taipei Da'an / Xinyi / Zhongshan)**, **MC (Monte-Carlo / La Condamine / Larvotto)**, **AD (Andorra la Vella ski-zone seasonal)**, **EC (Cuenca Centro Histórico / Gringolandia US/CA expat hub)**, **AM (Yerevan Kentron / Arabkir Russian-relocant compressed)**, **IN (Mumbai BKC / Bandra / Worli + Delhi NCR Lutyens / Cyber City Gurgaon + Bengaluru Indiranagar / Koramangala / HSR + Hyderabad HITEC City + Pune Koregaon Park)**, **KE (Nairobi Karen / Lavington / Westlands / Runda / Muthaiga / Kitisuru)** |
| **LOW** (DOM 150-300d, thin pool) | LU, FI, IS, SK, SI, LV, BG, RS, ME interior, MK, AL, BA Sarajevo, BR (secondary), CR, PA, AR (BA prime — cash-only LOW), DO (interior/off-peak), MA (Casablanca/Marrakech), MY (KL/Penang), VN (HCMC/Hanoi prime), PH (Manila prime), ID (Jakarta/Bali secondary), JP (regional), TH (Pattaya), IL (periphery), **MO (Macao Peninsula prime)**, **MD (Chișinău Centru / Botanica)**, **AD (parish villages off-season)**, **QA (Pearl-Qatar / West Bay Lagoon / Lusail prime)**, **SA (Riyadh DQ / Olaya / Al Malaz prime + Jeddah Corniche)**, **PE (Lima Miraflores / Barranco / San Isidro / Surco)**, **PY (Asunción Carmelitas / Villa Morra / Las Lomas)**, **AZ (Baku Yasamal / Nasimi / Sabail prime)**, **TN (Tunis La Marsa / Sidi Bou Said / Les Berges du Lac prime)**, **JO (Amman Abdoun / Sweifieh / Khalda / Dabouq / Deir Ghbar)**, **OM (Muscat Al Mouj / The Wave / Madinat Al Sultan Qaboos / Qurum prime ITC zones)**, **BH (Manama Seef / Diplomatic Area / Amwaj Islands / Reef Island prime designated freehold zones)**, **NG (Lagos VI / Ikoyi / Lekki Phase 1 / Banana Island / Oniru + Abuja Maitama / Asokoro / Wuse 2 prime)** |
| **VERY LOW** (DOM 300+d, illiquid) | Rural FR / IT South / ES inland / BG Black Sea overhang / HU rural east / BA rural / AL rural / Northern FI / Latgale LV / AR (everywhere ex-BA), BR rural, CR rural, PA Bocas/interior, JP akiya / regional, MY Sabah/Sarawak, VN secondary, PH Cebu/Davao, EG (everywhere ex-Cairo prime), MA medina/riad illiquid, ZA rural, ID Surabaya/Yogya, **LI (tiny ~40k market with quota residency)**, **MO (Cotai oversupply)**, **MD (rural / Bălți)**, **TW (regional / aging-society secondary)**, **KR (regional / aging-society secondary)**, **QA (outside designated freehold zones — foreigners can't buy elsewhere)**, **SA (Mecca/Medina Muslim-only constitutional bar; secondary cities)**, **PE (Cusco / Arequipa / sierra rural)**, **EC (Guayaquil post-2024 Internal Armed Conflict / regional)**, **PY (Encarnación / Ciudad del Este / Chaco)**, **AM (regional Gyumri / Vanadzor)**, **AZ (Karabakh / East Zangezur reintegrated zones AZ-citizen-priority)**, **TN (Sfax / interior / Djerba off-season)**, **IN (rural agricultural — foreign-buyer barred for non-NRI/non-OCI per FEMA 2018 Sch.I; agricultural / plantation / farmhouse barred even for NRIs/OCIs)**, **NG (Port Harcourt / Calabar / Kano + rural)**, **KE (rural agricultural — citizen-only constitutional restriction; Mombasa city / Nakuru / Kisumu / Naivasha SGR-corridor)**, **JO (Irbid / Zarqa / regional)**, **OM (outside ITC designated zones — foreigners cannot buy)**, **BH (outside designated freehold zones — foreigners cannot buy elsewhere)**, **KW (foreigners CANNOT own real estate freehold — only Iqama-employer leasehold; market structurally bifurcated)**, **LB (Beirut Achrafieh / Verdun / Hamra prime + everywhere else — post-2019 banking collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024 cascading liquidity collapse; foreign-buyer aggregate-area limits + Council-of-Ministers approval)** |

## Key cross-country patterns

1. **True MLS exists in NL (Funda), CA (CREA Realtor.ca), US (~580 regional MLSs), JP (REINS, broker-only)** — everywhere else is portal-driven (Hemnet/Finn/Domain are MLS-equivalent in transparency but not formally MLS); **TW 實價登錄 (actual price registration system, since 2012)** + **KR MOLIT 실거래가** + **HK Land Registry EPRC** + **SG URA caveats** offer high price-history transparency without formal MLS
2. **"Both-sides-pay" commission** structure: IT, DE (post-2020), PL, RO, BG, HR, GR, RS, BA, AL, AR, CA, TR, IL, MA, UY, CL, **MC, MO, SG (1+2 split), HK (1+1), TW (2+1-2)** — material to net-proceeds modelling. **US shifting** post-NAR settlement Aug 2024 (buyer-agent commissions unbundled)
3. **Energy/EPC labels are now liquidity gates** in FR (DPE), DE (GEG), BE-Flanders, NL, UK (EPC), IT (APE) — F/G class properties face collapsing buyer pools
4. **Foreign-seller withholding** is a material exit cost in: **US (FIRPTA 15% gross)**, **ZA (Section 35A 7.5% on sale > R2M)**, **DO (27% gross)**, **ES (3% retention)**, **PT (28% non-res rate)**, **IL (25% Mas Shevach)**, **MY (RPGT 10% permanent)** — model into net-proceeds
5. **Foreign-buyer bans/restrictions** narrowing exit pool: CA (to 2027), AU (established to 2027), NZ (perm), MX (fideicomiso), AT (Tyrol/Salzburg/Vorarlberg quotas), CH (Lex Koller), MT (AIP outside SDA), HR (10-yr lock on agri non-EU), **TH (49% condo cap)**, **PH (no land for foreigners, 40% condo cap)**, **VN (30% per building, 50-yr leasehold)**, **ID (Hak Pakai only — no freehold for foreigners)**, **MY (state-by-state minimum thresholds)**, **AE (freehold only in Designated Areas)**, **SG (Restricted Residential Property Act — no landed homes for foreigners + ABSD 60% non-resident)**, **LI (Lex-Koller-equivalent + EEA-only + quota residency ~28+17/year)**, **MD (agricultural land foreign-restricted; Transnistria-scope excluded)**, **TW (reciprocity-list-based — verify BOCA list)**, **QA (designated freehold zones only — Pearl-Qatar / West Bay Lagoon / Lusail; rest leasehold)**, **SA (Mecca/Medina constitutional Muslim-only ownership; Real-Estate-Owner Premium Residency SAR 4M)**, **PE (border 50km Andean Constitution Art. 71 restriction)**, **PY (border 50km Ley 2532/2005)**, **AZ (Karabakh / East Zangezur AZ-citizen-priority subsidized exclusionary; ANAMA de-mining cert required)**, **AM (agricultural land barred for foreigners)**, **IN (foreign-buyer residential ban for non-NRI/non-OCI per FEMA 2018 Sch.I; agricultural / plantation / farmhouse barred even for NRIs/OCIs)**, **NG (Land Use Act 1978 — all land vested in state Governor; only Statutory Right of Occupancy 99-yr leasehold for foreigners; Governor's consent required)**, **KE (agricultural land citizen-only per Constitution Art. 65; 99-yr leasehold cap on non-citizen freehold-equivalents)**, **JO (Council-of-Ministers approval required for properties >threshold; ≤4,000 m² agricultural barred; reciprocity required for some nationalities)**, **OM (foreigners limited to ITC designated zones per RD 12/2006 / 89/2021)**, **BH (designated freehold zones only — Diyar Al Muharraq / Amwaj / Durrat / Reef / Bahrain Bay / Seef / Manama Diplomatic Area)**, **KW (foreigners CANNOT own real estate freehold — only Iqama-employer leasehold per Decree-Law 74/1979 — among the most restrictive globally)**, **LB (foreign-buyer aggregate-area limits — ≤3,000 m² Beirut / ≤10,000 m² Mount Lebanon / coastal limits; Council-of-Ministers approval for >limits; Lebanese-descent buyers exempt)**
6. **Cadastral/title issues** are the binding sellability constraint in AL (#1), BA, RS rural, MK rural, IT South borgo, ES rural inland, RO restitution residue, BG rural, MX ejido, **EG (~90% unregistered)**, **MA medina/riad multi-heir**, **VN Pink Book chain verification** — clean title is worth more than price-cutting
7. **Seasonal-only liquidity**: ME coast, HR Adriatic, GR islands, BG Black Sea, CR Guanacaste, MX Riviera, PT Algarve, IS countryside, AT/CH alpine, **UY Punta del Este (Dec-Feb)**, **EG North Coast (Sahel)**, **TH Phuket/Pattaya**, **JP Niseko**, **TN Djerba/Hammamet/Sousse coast**, **EC Salinas/Olón Pacific coast**
8. **Bidding-up cultures** (sale > asking): NL, SE, NO, IE, UK pre-2024, AU auction states, CA (2021-2022 peak), **US Sun Belt 2021-2022 peak**
9. **Chain risk** unique to UK; **co-op approval** unique to SE bostadsrätt, FI asunto-osakeyhtiö, DK andelsbolig
10. **CGT primary-residence exemption is universal** in EU/UK/Anglo (with conditions); the differentiator is **non-resident treatment** — ES/PT/FR/IT/UK/AU/CA/US all have non-resident withholding or higher rates
11. **GROSS-revenue CGT regimes** (tax on sale price, not gain) — punitive on low-margin / loss sales: **EG (2.5% Law 175/2023)**, **PH (6% CGT)**, **ID (PPh Final 2.5%)**, **VN (2% transfer)**, **TH (3.3% SBT if <5 yrs)** — material vs net-gain regimes elsewhere
12. **FX repatriation friction** (foreign sellers): **EG Form 4** (without it: EGP-only exit during devaluation = catastrophic), **MA Office des Changes**, **VN SBV approval**, **ID Bank Indonesia documentation**, **TH FET form**, **PH BSP registration**, **ID restricted to original investment + accrued**, **TN Office des Changes (similar MA-style friction)**, **PE SBS banking-channel documentation**, **AM CBA (Central Bank of Armenia) banking documentation**, **NG Form A (similar EG Form 4 friction; without it: NGN-only exit during devaluation = catastrophic)**, **IN RBI repatriation rules** (NRI/OCI sellers; LRS USD 250k/yr cap; NRO/NRE bank-account split; TDS s.195 20%/30% LTCG/STCG), **KE KRA s.45 ITA non-resident withholding** (bank-channel documentation), **LB banking-frozen USD vs fresh-USD distinction post-2019 collapse + Sayrafa vs parallel rate triple-tier** — must verify at PURCHASE for clean exit
13. **No-CGT zones**: **AE (no personal income tax)**, **GE (after 2 yrs)**, **DK primary residence**, **GR (suspended through 2026)**, **SG (no CGT — but SSD 4-12% if <3 yrs)**, **HK (no CGT for individuals — but SSD 10-20% if <36 months)**, **MO (no CGT — but SSD 5-20% if <24 months)**, **MC (no PIT/CGT)**, **QA (no PIT/CGT for individuals)**, **SA (no PIT/CGT for individuals — but RETT 5% on disposal)**, **PY (territorial — foreign-source not taxed; PY-source IRP 8/9/10%)**, **OM (no PIT for individuals — Oman individual income-tax law drafted 2022 NOT enacted as of May 2026)**, **BH (no PIT for individuals)**, **KW (no PIT for individuals — but foreigners CANNOT own freehold)** — material to exit timing
14. **Earthquake / seismic disclosure** material to exit: **JP (Shin-Taishin 1981+ standard)**, **TR (post-Feb 2023 Kahramanmaraş)**, **NZ Wellington apartments**, **CL (post-2010 Maule)**, **TW (post-2024 Hualien M7.4 + post-1999 921 Chi-Chi standards)**, **AM (post-1988 Spitak M6.8 baseline + Yerevan/Gyumri/Vanadzor microzoning)**, **AZ (post-2000 Baku M6.8 + AzDTN 2.4-1 2010 code)**, **PE (Pacific Ring of Fire HIGH seismic)**, **EC (post-2016 Pedernales M7.8 + Cotopaxi volcano active 2024)**

15. **Anti-speculation Special Stamp Duty regimes** (seller-side withholding triggered by short-hold flips): **SG SSD 4-12% if <3 yrs**, **HK SSD 10-20% if <36 months**, **MO SSD 5-20% if <24 months**, **TW HLTIT 2.0 45%/35%/20%/15% sliding by hold ≤2/2-5/5-10/>10 yrs (Jul 2021 reform)**, **KR multi-home top CGT up to 75% + 종부세 0.5-5% annually** — model into hold-period strategy
16. **High-transparency price-history regimes without formal MLS**: **TW 實價登錄 (since 2012)**, **KR MOLIT 실거래가**, **SG URA caveats**, **HK Land Registry EPRC** — useful for buyer-side due-diligence even where MLS absent
17. **Microstate / quota-restricted markets**: **LI (~40k pop, ~28 EEA + ~17 third-country/year by lottery)**, **MC (~38k pop, Sûreté Publique due-diligence + ~€500k bank deposit)**, **AD (~85k pop, ~75% non-Andorran, Llei 26/2024 STR + parish quotas)** — small-market price-discovery slow

## Anti-hallucination

- **DOM is broker-aggregated** — verify per-transaction in 2-3 local agents per micro-market
- **Sparse-data flag**: Balkans + LatAm + MENA + parts of SE Asia have no central HPI registry comparable to EU stat offices; commission norms regionally fluid (TR/EG/ID/VN especially)
- **Don't conflate auction "passed-in"** (no sale) with sale at reserve
- **Currency mismatch** for foreign-priced markets (CR/PA/AR/UY/DO USD; LU EUR with FR/DE/BE buyer cycles; CL UF inflation-indexed; TR USD-pricing in foreign-buyer zones; EG severe EGP devaluation cycle)
- **Tax law churn 2023-2026 is unusually high** in CO (Ley 2277/2022), CL (Ley 21.210/21.442), EG (Law 175/2023), MY (RPGT reforms), US (NAR settlement Aug 2024), ZA (expropriation 2025) — re-verify rates against primary source before quoting
- **Regional cycle sensitivity**: GE/TR foreign demand sensitive to Russian capital cycle 2022-2026; DO/CO foreign demand to USD/USA cycle; UY/AR linked but inversely; MY/TH/VN/PH to China outbound cycle; ID/MY/JP to JPY/CNY
- **GROSS-revenue tax regimes** (PH 6%, EG 2.5%, ID 2.5%, VN 2%, partial TH 3.3%) require explicit "gross of sale price not gain" framing — easy hallucination trap

## Status

Last refreshed: 2026-05-01. 8 Tier-5 countries added (IN, NG, KE, JO, OM, BH, KW, LB) — total 87 countries (Tier-1: US, TR, AE, JP, TH, DO, CO, UY, CL, ZA; Tier-2: GE, ID, MY, VN, PH, IL, MA, EG; Tier-3: SG, HK, KR, TW, MO, LI, MC, AD, MD; Tier-4: QA, SA, PE, EC, PY, AM, AZ, TN; Tier-5: IN, NG, KE, JO, OM, BH, KW, LB).
