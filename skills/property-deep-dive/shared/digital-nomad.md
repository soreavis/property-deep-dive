# Universal `--digital-nomad` Section

Digital-nomad-specific filter: digital nomad visa (DNV) availability, internet quality, coworking density, time-zone overlap with major work hubs.

**Snapshot**: April 2026.

## Universal contract

For the property's country, return:
1. **DNV available?** + thresholds + duration
2. **Internet quality** (Speedtest median, fibre coverage, 4G/5G mobile)
3. **Coworking density** (in city of interest)
4. **Time-zone overlap** with major work hubs (US-East/PT/UK/CET/IST)
5. **Tax residency trigger** (typical 183-day rule + special cases)
6. **Cost of living for nomad lifestyle** (city + restaurants + transit)
7. **Tax-treaty status** (with major source countries)

## Output template

```markdown
## Digital Nomad Profile

**Country**: <ISO2>
**DNV available**: <yes / no>
**Threshold**: <income/month or savings>
**Duration**: <max years>
**Internet (Speedtest median)**: <Mbps fixed / mobile>
**Coworking density**: <high | medium | low + count>
**Time-zone overlap (US-East / EU)**: <hours/day>
**Tax residency trigger**: <183 days standard / special>
**Cost of living tier**: <see compare table>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## DNV (Digital Nomad Visa) availability — Apr 2026 snapshot

### Active DNVs in skill-supported countries

| Country | Program | Threshold | Duration | Notes |
|---|---|---|---|---|
| **EE** | Digital Nomad Visa | €4,500 net monthly | 1-yr; no PR | Estonia first to launch (2020) |
| **HR** | Digital Nomad Visa | €3,622.50/mo (Jan 2026; 2.5× avg net) OR €43,470 lump | 18 months max, **NOT consecutively renewable** (6-mo cooldown) | Tax-exempt foreign income |
| **PT** | Digital Nomad Visa (D8) | €3,480/mo (4× SMN) | 1-yr renewable; PR after 5 yrs | Replaces tourist-visa workaround |
| **ES** | Digital Nomad Visa (Beckham-style) | €2,762/mo (200% min wage) | 1-yr→3-yr; flat 24% on Spanish income for 5 yrs | Active program, but property purchases NOT a route to citizenship after Apr 2025 GV repeal |
| **IS** | Long-Term Visa for Remote Work | ISK 1,000,000/mo (~€7,300) | 6 months (not extendable) | Short-stay only; NOT residency |
| **IT** | Digital Nomad Visa | €28,000/yr (~€2,333/mo) | 1-yr renewable | Tax residency trigger 183 days |
| **GR** | Digital Nomad Visa | €3,500/mo | 1-yr renewable; PR pathway 5 yrs | 50% tax discount first 7 yrs |
| **HU** | White Card | €2,000/mo | 1-yr renewable; max 2 years | Strict — no PR pathway |
| **CZ** | Zivnostenský (entrepreneur visa) | ~110,000 CZK savings + plan | annual renewal; PR 5 yrs | Not formally a DNV but used as one |
| **MT** | Nomad Residence Permit | €2,700/mo (€32,400/yr) | 1-yr renewable up to 4 yrs | Apply via Residency Malta Agency |
| **CY** | Digital Nomad Visa | €3,500/mo | 1-yr renewable up to 3 yrs | Tax residency trigger 183 days |
| **RO** | Digital Nomad Visa | ~3× avg gross salary (~€3,000/mo) | 1-yr renewable | |
| **MX** | Temporary residency (income-solvency proxy) | ~US$4,400/mo income OR ~US$74k savings | Renewable 4 yrs → PR | Not formally a DNV but used as one |
| **CR** | Rentista | US$2,500/mo (24 months) OR US$60k bank deposit | 2-yr renewable; PR 3 yrs | |
| **BR** | VITEM XIV — Digital Nomad | US$1,500/mo OR US$18,000 savings | 1-yr renewable once (max 2 yrs) | |
| **AL** | Unique Permit (Digital Nomad / Self-Employed) | 32,000 ALL/mo (~€385) OR 300,000 ALL (~€3,614) deposit | 1-yr renewable up to 5× (max 6 yrs) | Law 79/2021 |
| **JP** | Digital Nomad Visa | JPY 10M/yr income proof (~US$65k) | 6 months (NOT renewable in-country; not residency) | Launched Apr 2024; treaty-country nationals only |
| **TH** | DTV (Destination Thailand Visa) | THB 500k savings (~US$14k) + remote-employer / freelance proof | 5-yr multi-entry; 180 days/stay (extendable +180) | Launched mid-2024; replaces tourist-visa workarounds |
| **CO** | Migrante V — Visitante remote-worker | ~US$684/mo (3× SMMLV, 2026 figure) | 2 yrs (renewable) | Decreto 1209/2022 |
| **UY** | Digital Nomad Visa (Decreto 162/023) | ~US$1,500/mo income claim (declarative) | Initial 6 months → 1-yr extension | Live since 2023 |
| **CL** | Visa de Residencia Temporaria (DN sub-category) | No fixed threshold; remote-work contract required | 1-yr renewable | Used as DNV in practice |
| **ZA** | Remote Work Visitor Visa | ZAR 1M/yr (~US$54k) from foreign employer | 3-yr | Launched May 2024; Govt Gazette 50714 |
| **GE** | Remotely from Georgia | US$24k/yr OR US$2k/mo income | 360-day visa-free stay (most nationalities anyway) | Aug 2020; updated 2024 — informal in practice |
| **MY** | DE Rantau Nomad Pass | MYR 24k/mo (~US$5k) | 3-mo to 12-mo (renewable 12-mo) | Launched Oct 2022 |

### No specific DNV (use entrepreneur / business visa)

**FR, DE, BE, NL, LU, AT, CH, IE, UK** — alternative paths (Talent Passport, Freiberufler, DAFT for US, etc.). See `--visa` for details.

**SE, FI, NO, DK** — entrepreneur permits + remote work generally not DNV-classified.

**SK, SI, PL, BG, LT, LV, EE** — most have entrepreneur tracks; only EE has formal DNV.

**RS, ME, BA, MK, AL** — visa-free 90 days for many nationalities; longer needs business permit.

**CA, AU, NZ** — no DNV; ETA/work visa system; CA explicitly considering 2026.

**PA** — visa-free 180 days for 50+ nationalities is a de-facto nomad-friendly policy.

**US** — NO formal DNV; B-1/B-2 visitor (90-180 days) used as workaround for foreign-employer remote work; ESTA visa-waiver covers 90 days for VWP nationals. Remote-work-on-tourist-status is a grey area (USCIS has not formally blessed it).

**TR** — NO formal DNV (proposal floated 2024, not enacted as of Apr 2026); short-term residency permit (kısa dönem ikamet) for property owners is the practical route. Digital nomads informally use 90-day visa-free → residency renewal.

**AE** — Dubai **Virtual Working Programme** (1-yr, US$5k/mo income proof) and federal **Green Visa** for freelancers (5-yr, AED 360k income for 2 prior years) are the de-facto DNV equivalents. Not labelled "digital nomad" but functionally equivalent.

**DO, ID, VN, PH, IL, MA, EG** — NO formal DNV as of Apr 2026:
- **DO**: tourist 30-90 days; nomads use stay-extension workarounds
- **ID**: B211A visa (60-day, multi-extend up to 6 mo); a 5-yr DNV was proposed 2022 but not enacted
- **VN**: proposals tabled 2024-2025, none enacted; e-visa 90-day is the workaround
- **PH**: SRRV (Special Resident Retiree Visa, US$10k-50k deposit) used as nomad alternative; DNV proposed 2024
- **IL**: B/2 tourist (3-mo, extendable); NO DNV
- **MA**: Carte de Séjour (long-stay, 1-yr renewable) for nomads with 3-mo+ stay; DNV proposed 2024
- **EG**: tourist 30-90 days only; no formal DNV proposed yet

## Internet quality (Apr 2026 best-available)

Speedtest Global Index country medians (Apr 2026 snapshot — verify https://www.speedtest.net/global-index for current).

### Tier 1 — fixed median ≥150 Mbps + 5G ubiquitous
🇸🇬 SG (not in skill yet) · 🇰🇷 KR (not in skill yet) · 🇺🇸 US · 🇨🇭 CH · 🇫🇷 FR · 🇪🇸 ES · 🇸🇪 SE · 🇩🇰 DK · 🇳🇱 NL · 🇳🇴 NO · 🇳🇿 NZ · 🇨🇦 CA · 🇦🇺 AU · 🇯🇵 JP (1Gbps fibre standard urban) · 🇦🇪 AE (Dubai/Abu Dhabi etisalat/du fibre)

### Tier 2 — fixed median 80-150 Mbps + 5G in cities
🇩🇪 DE · 🇬🇧 UK · 🇮🇪 IE · 🇧🇪 BE · 🇮🇹 IT · 🇵🇹 PT · 🇪🇪 EE · 🇱🇹 LT · 🇱🇻 LV · 🇨🇿 CZ · 🇸🇰 SK · 🇫🇮 FI · 🇮🇸 IS · 🇱🇺 LU · 🇲🇹 MT · 🇹🇭 TH (Bangkok/Chiang Mai AIS/3BB) · 🇮🇱 IL (Bezeq/Hot fibre)

### Tier 3 — fixed median 40-80 Mbps + 5G in capital
🇨🇾 CY · 🇬🇷 GR · 🇵🇱 PL · 🇭🇺 HU · 🇸🇮 SI · 🇭🇷 HR · 🇧🇬 BG · 🇷🇴 RO · 🇦🇹 AT · 🇲🇽 MX (CDMX/Monterrey) · 🇧🇷 BR (SP/Rio) · 🇨🇷 CR (San José) · 🇵🇦 PA (Panama City) · 🇹🇷 TR (Istanbul/Ankara Türknet/Turkcell) · 🇲🇾 MY (KL TM Unifi) · 🇨🇱 CL (Santiago Movistar/VTR) · 🇨🇴 CO (Bogotá/Medellín Movistar) · 🇿🇦 ZA (Cape Town/JHB Vodacom/MTN fibre)

### Tier 4 — variable, urban-centric
🇷🇸 RS · 🇲🇪 ME · 🇧🇦 BA · 🇲🇰 MK · 🇦🇱 AL · 🇦🇷 AR · 🇬🇪 GE (Tbilisi Magticom/Silknet) · 🇺🇾 UY (Montevideo Antel) · 🇩🇴 DO (Santo Domingo Claro/Altice) · 🇮🇩 ID (Jakarta/Bali Telkomsel/Indihome) · 🇻🇳 VN (HCMC/Hanoi Viettel/VNPT) · 🇵🇭 PH (Manila PLDT/Globe — speeds rising 2024-25) · 🇲🇦 MA (Casablanca/Rabat Maroc Telecom fibre) · 🇪🇬 EG (New Capital + Cairo/Alex Telecom Egypt fibre)

**Reality check for nomads**: median speed often quoted is fibre-to-the-home in urban centers. Rural / coastal-village can drop to 4G / 30 Mbps. Always check the **specific address** before committing — many country playbooks include this in `--mains` (utilities) or `--amenities`.

## Coworking density (top nomad cities Apr 2026)

| City | Country | Coworking spaces (approx, NomadList) |
|---|---|---|
| Lisbon | PT | 80+ |
| Berlin | DE | 100+ |
| Madrid | ES | 70+ |
| Barcelona | ES | 90+ |
| Mexico City | MX | 60+ |
| Buenos Aires | AR | 50+ |
| Belgrade | RS | 30+ |
| Tbilisi | GE | 40+ |
| Tallinn | EE | 25+ |
| Tirana | AL | 15+ |
| Split | HR | 20+ |
| Athens | GR | 35+ |
| Valletta/Sliema | MT | 15+ |
| Bucharest | RO | 30+ |
| Bangkok | TH | 80+ |
| Chiang Mai | TH | 60+ (DN hotspot since pre-2020) |
| Bali (Canggu/Ubud) | ID | 60+ |
| Tokyo | JP | 80+ (WeWork strong; many cafés double as workspaces) |
| Dubai | AE | 70+ |
| Istanbul | TR | 50+ |
| Mexico City | MX | 60+ (also a TZ/LatAm hub for nomads) |
| Medellín | CO | 50+ (Laureles/Poblado) |
| Cape Town | ZA | 35+ (DN hub Q4-Q1 ZAF summer) |
| Buenos Aires | AR | 50+ |
| Montevideo | UY | 15+ |
| Santiago | CL | 30+ |
| Tel Aviv | IL | 45+ |
| Marrakech / Casablanca | MA | 20+ combined |
| Cairo | EG | 15+ |
| Kuala Lumpur | MY | 50+ |
| HCMC / Hanoi | VN | 40+ combined |
| Manila / Cebu | PH | 30+ combined |

For property-DD purposes: a coworking space within 15-min walk is a strong Tier-1 nomad signal.

## Time-zone overlap with major work hubs

For remote work, time-zone overlap with the team is critical. Hours per day in overlap (assuming 9am-6pm working hours).

| Country | TZ | US-East (ET) overlap | UK (GMT) overlap | CET overlap |
|---|---|---|---|---|
| US East/CA-East | ET | 9 hrs | 4-5 hrs | 3-4 hrs |
| US West/CA-West | PT | 5 hrs | 1-2 hrs | 0-1 hrs |
| MX, CR, PA | CT | 8 hrs | 3 hrs | 2 hrs |
| BR (SP) | BRT (-3) | 7 hrs | 3-4 hrs | 2-3 hrs |
| AR, UY, CL (winter), DO | -3 / -4 | 6-7 hrs | 3-4 hrs | 2-3 hrs |
| CO | COT (-5) | 9 hrs | 4 hrs | 3 hrs |
| UK, IE, IS, PT | GMT/UTC | 5 hrs | 9 hrs | 8 hrs |
| MA | WET (UTC+1 perm. since 2018) | 4 hrs | 8 hrs | 9 hrs |
| EU (most) | CET | 4 hrs | 8 hrs | 9 hrs |
| FI, EE, LV, LT, GR, BG, RO, CY, MT (Eastern Europe) | EET | 3 hrs | 7 hrs | 8 hrs |
| ZA, EG, IL | UTC+2 / UTC+3 (no DST in ZA/EG; IL has DST) | 2-3 hrs | 7 hrs | 8 hrs |
| TR | UTC+3 (perm., no DST since 2016) | 2 hrs | 6 hrs | 7 hrs |
| GE, AE | UTC+4 | 1-2 hrs | 5 hrs | 6 hrs |
| TH, VN, ID (Jakarta WIB) | UTC+7 | 0 hrs | 2 hrs | 3 hrs |
| MY, PH, ID (Bali WITA UTC+8) | UTC+8 | -1 hrs | 1 hrs | 2 hrs |
| JP | JST (UTC+9, no DST) | -2 hrs | 0 hrs | 1 hrs |
| AU East | AEDT (+10/+11) | -2 hrs | -10 hrs | -8 hrs |
| NZ | NZDT (+12/+13) | -4 hrs | -11 hrs | -10 hrs |

**Best for US-team nomads**: LatAm (especially MX/CR/PA same TZ as US-Central; CO/DO same as US-East) > EU coastal-west (PT/ES) > rest of EU > MA (1-hr CET shift, 4-hr ET overlap) > ZA/IL/EG > GE/AE > AU/NZ/JP/SE-Asia (effectively next-day).

**Best for EU-team nomads**: Anywhere in EU (CET/EET) > UK > Iberian coast (PT/ES) > MA/ZA/EG/IL/TR (1-2 hrs offset, full overlap) > GE/AE (1-2 hrs ahead) > TH/VN/ID-W (3-hr ahead, half-day overlap) > MY/PH/JP (limited overlap) > LatAm (afternoon-evening overlap only).

## Tax residency trigger

Standard rule across most skill-supported countries:
- **183 days in 12 months → tax resident**
- Some countries also use "centre of vital interests" or "habitual abode" tests

**Special / shorter triggers (be careful)**:
- 🇨🇦 CA: ties to Canada (home, family, dependents) can trigger residency at <183 days
- 🇺🇸 US: substantial presence test (weighted 3-year) + citizenship-based
- 🇦🇺 AU: domicile + ordinarily-resident + 183 days + Commonwealth Superannuation tests
- 🇨🇭 CH: 30/90-day rule (lower than 183) — be careful for short stays

**Special / favorable**:
- 🇪🇪 EE: digital nomad / e-Residency does NOT confer tax residency by itself
- 🇲🇪 ME: 183-day rule but generally lenient enforcement
- 🇲🇽 MX: territorial-ish for residents abroad; 183 days triggers full tax-residency
- 🇦🇪 AE: 0% personal income tax; tax-residency cert available after 90/183 days (depending on type) — verify with FTA
- 🇬🇪 GE: 183 days OR "high-net-worth status" — territorial-ish; foreign-source income often exempt for non-resident-of-source treaty cases
- 🇹🇭 TH: 180 days = resident; **2024 reform** taxes foreign-source income brought into TH in same/later year (was previously exempt if remitted in next year) — verify with Revenue Department
- 🇲🇾 MY: 182 days = resident; foreign-source income exemption extended to 2036 for individuals (per Budget 2024)
- 🇺🇾 UY: **tax holiday** — new tax-residents can elect 11-yr exemption on foreign-source income (or 7% rate option)
- 🇿🇦 ZA: 183 days + continuous-91 test; worldwide-income basis once resident
- 🇺🇸 US: substantial presence test + citizenship-based — see top of section
- 🇯🇵 JP: 1 yr + "domicile" test → resident; foreign-source income exempted for first 5 yrs as "non-permanent resident" if not remitted to JP

## Cost of living for nomad lifestyle (1-bedroom + restaurants + transit)

### Cheap (<€1,500/mo)
🇦🇱 Tirana · 🇧🇦 Sarajevo · 🇲🇰 Skopje · 🇲🇪 Podgorica · 🇷🇸 Belgrade · 🇧🇬 Sofia · 🇷🇴 Bucharest · 🇲🇽 Mexico City (off-Polanco) · 🇦🇷 Buenos Aires (post-Milei) · 🇬🇪 Tbilisi · 🇪🇬 Cairo · 🇻🇳 HCMC / Hanoi · 🇵🇭 Manila / Cebu · 🇮🇩 Jakarta (off-Menteng) / Yogyakarta · 🇲🇦 Casablanca / Marrakech (off-Medina rentals) · 🇹🇭 Chiang Mai · 🇹🇷 Istanbul (post-2023 lira slide; verify in TRY at point of search) · 🇨🇴 Medellín / Bogotá · 🇩🇴 Santo Domingo (off-zona-colonial)

### Mid (€1,500-2,500)
🇵🇹 Porto / Setúbal · 🇪🇸 Valencia / Malaga · 🇮🇹 Bari / Catania · 🇬🇷 Athens · 🇨🇿 Brno · 🇭🇺 Budapest · 🇵🇱 Warsaw · 🇨🇷 San José · 🇵🇦 Panama City · 🇲🇽 Guadalajara · 🇲🇾 Kuala Lumpur · 🇹🇭 Bangkok · 🇮🇩 Bali (Canggu/Ubud) · 🇿🇦 Cape Town (off-Atlantic-seaboard) / JHB · 🇨🇱 Santiago · 🇺🇾 Montevideo

### Mid-high (€2,500-3,500)
🇵🇹 Lisbon · 🇪🇸 Madrid / Barcelona · 🇮🇹 Milan / Rome · 🇩🇪 Berlin / Hamburg · 🇫🇷 Lyon · 🇳🇱 Rotterdam · 🇮🇪 Galway · 🇲🇹 Sliema · 🇨🇾 Limassol · 🇪🇪 Tallinn · 🇧🇷 São Paulo · 🇮🇱 Tel Aviv (off-center) · 🇯🇵 Tokyo (off-23-ku) / Osaka

### Expensive (€3,500+)
🇨🇭 Zurich · 🇳🇴 Oslo · 🇮🇸 Reykjavik · 🇱🇺 Luxembourg · 🇬🇧 London · 🇮🇪 Dublin · 🇸🇪 Stockholm · 🇩🇰 Copenhagen · 🇨🇭 Geneva · 🇫🇷 Paris · 🇳🇱 Amsterdam · 🇩🇪 Munich · 🇨🇦 Toronto/Vancouver · 🇦🇺 Sydney/Melbourne · 🇳🇿 Auckland · 🇺🇸 NYC / SF / LA / Boston · 🇦🇪 Dubai (Marina/DIFC) · 🇮🇱 Tel Aviv (center) · 🇯🇵 Tokyo (central 23-ku premium)

## Tax-treaty cross-references

**Most tax treaties between OECD countries** prevent double taxation but require careful navigation:
- **183-day test in treaty article** — usually shifts tax residency
- **Tie-breaker rules** — residence > permanent home > centre of vital interests > habitual abode > nationality
- **Pension articles** vary — see `--retirement` for details

For US citizens specifically: **citizenship-based taxation** means worldwide income is taxed regardless of residency. **FBAR + FATCA** disclosure required for foreign accounts >US$10k. Tax treaty doesn't fully solve this; foreign-tax credit + foreign-earned-income exclusion (~US$130k 2026) help.

## Anti-hallucination

- **DNV thresholds change** — verify with the destination country's immigration portal
- **Speedtest median is national** — your specific address may be much slower (rural fibre lag)
- **Time zone overlap** changes around DST shifts — refine for your specific work-hour schedule
- **Tax residency rules** are stricter than 183 days in many countries (CH 30-day, CA ties test)
- **Coworking counts** are NomadList-style approximations — not exhaustive

## Status

Last refreshed: 2026-05-01 (added Tier-1 + Tier-2 country coverage: US, TR, AE, JP, TH, DO, CO, UY, CL, ZA, GE, ID, MY, VN, PH, IL, MA, EG).

**Confidence**: MEDIUM — DNV thresholds and tax-residency cutoffs verified against destination immigration / tax authorities as of Apr 2026, but several reforms are in flight (TH 2024 foreign-source remittance change, JP DNV launched Apr 2024, ZA Remote-Work Visa launched May 2024, UY tax-holiday election, MY foreign-source exemption to 2036). Speedtest tier placements are urban-centric — rural fibre lags significantly in TH, ID, VN, PH, MA, EG, ZA, MX, BR. Always verify the **specific address** via `--mains` / `--amenities`. Cost-of-living tiers compress under FX volatility (TR especially) — bands are EUR-equivalent at ~Apr 2026 rates.
