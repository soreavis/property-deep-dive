# Universal `--esg` Section

ESG (Environmental, Social, Governance) overlay for property: energy class distribution, climate exposure, community impact. Bridges `--climate` (forward physical risk) with `--mains` (current energy/utility) and `--insurance` (cat-risk schemes).

**Snapshot**: April 2026.

## Why ESG matters for property

1. **EU EPBD recast (2024/1275)** — Member State transposition by **29 May 2026**. Affects sale/rent disclosure and minimum energy performance for worst-performing buildings. **Class G/F buildings face rental bans** in many countries (FR already; others phasing in).
2. **Stranded asset risk** — buildings that can't be brought to minimum-class face value erosion ("brown discount")
3. **Climate-risk premium** — insurers and lenders increasingly price physical-risk overlay (flood/EQ/wildfire)
4. **Tenant preferences shifting** — younger tenants prefer A/B-class buildings; rental yield differentiates

## Universal contract

For the property's country, return:
1. **EPC distribution** (% of stock by class A-G)
2. **Worst-performing class rental ban schedule** (e.g., FR G banned 2025, F 2028, E 2034)
3. **Climate exposure** (Climate Central / Copernicus risk index)
4. **Community impact** (local renewable share, public transport access, walkability)
5. **Carbon-tax / property energy levy** if any
6. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## ESG Profile

**Country**: <ISO2>
**EPC distribution (latest)**: A: <%> · B: <%> · C: <%> · D: <%> · E: <%> · F: <%> · G: <%>
**Worst-class rental ban**: <schedule>
**Climate exposure (sea-level/heat/drought/wildfire)**: <index>
**Community-impact (renewables/walk-score)**: <evaluation>
**Carbon levy**: <yes/no — rate>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## EPC distribution per country (Apr 2026 best-available)

Distribution of building stock by EPC class (residential). Source mix: **EU Buildings Database (Buildings.eu)** + national EPBD reports + national stat offices.

| Country | A+/A | B | C | D | E | F | G |
|---|---:|---:|---:|---:|---:|---:|---:|
| FR | 5% | 12% | 25% | 28% | 18% | 9% | 3% |
| IT | 4% | 9% | 22% | 30% | 22% | 9% | 4% |
| DE | 8% | 15% | 28% | 28% | 15% | 5% | 1% |
| ES | 6% | 14% | 25% | 30% | 18% | 5% | 2% |
| PT | 10% | 18% | 25% | 22% | 15% | 7% | 3% |
| NL | 14% | 22% | 28% | 22% | 9% | 4% | 1% |
| BE | 6% | 14% | 25% | 30% | 18% | 5% | 2% |
| LU | 12% | 22% | 28% | 22% | 12% | 3% | 1% |
| AT | 14% | 25% | 28% | 22% | 8% | 2% | 1% |
| CH | 10% | 22% | 30% | 25% | 10% | 2% | 1% |
| UK | 4% | 14% | 35% | 30% | 12% | 4% | 1% |
| IE | 4% | 12% | 32% | 32% | 15% | 4% | 1% |
| Nordic (SE/FI/NO/DK/IS) | 25-35% | 30-35% | 22-25% | 10-15% | 3-5% | 1-2% | 0-1% |

**Disclaimer**: EPC class methodologies are NOT harmonised across countries (the same physical building can be class B in DE and class C in FR). EU EPBD recast 2024/1275 aims to converge — transposition deadline 29 May 2026.

### Non-EU energy-rating regimes (Tier-1 + Tier-2 expansion, Apr 2026)

EPC-style class distributions are not published by stat office for most non-EU regimes — output the **regime name, scope, and verification path** rather than fabricating an A-G split.

| Country | Regime | Mandatory? | Stock penetration | Source |
|---|---|---|---|---|
| 🇺🇸 US | HERS Index (RESNET) — voluntary national. State overlays: CA Title 24 (mandatory new build), NY LL97 (commercial >25k sqft) | Federal: voluntary; CA/NY: mandatory in scope | est. <20% of single-family stock rated (HERS) — verify at resnet.us | resnet.us; energy.ca.gov |
| 🇹🇷 TR | BEP Yönetmeliği EPC — mandatory for buildings permitted post-2011 | Mandatory at sale/rent if permit ≥2011 | Pre-2011 stock largely unrated — verify at csb.gov.tr | csb.gov.tr |
| 🇦🇪 AE | Estidama Pearl Rating (Abu Dhabi) + Al Sa'fat (Dubai) | Mandatory new build (both emirates) | Older Dubai/AUH stock unrated — verify at dm.gov.ae / upc.gov.ae | dm.gov.ae; upc.gov.ae |
| 🇯🇵 JP | BELS (Building Energy-saving Labeling System) | 2025 Building Energy Conservation Act mandates higher efficiency for all new builds | Voluntary on existing stock; new builds rated from 2025 — verify at mlit.go.jp | mlit.go.jp |
| 🇹🇭 TH | TREES (TGBI) | Voluntary | Single-digit % of commercial; residential rare — verify at tgbi.or.th | tgbi.or.th |
| 🇩🇴 DO | No national EPC regime (per public sources Apr 2026) | — | data not publicly available — verify at mem.gob.do | mem.gob.do |
| 🇨🇴 CO | NSR-10 seismic + emerging sostenibilidad codes | Seismic mandatory; energy-efficiency voluntary | Energy class data not publicly available — verify at minvivienda.gov.co | minvivienda.gov.co |
| 🇺🇾 UY | CO2 / energy-efficiency cert pilot (MIEM) | Voluntary | Pilot scope only — verify at miem.gub.uy | miem.gub.uy |
| 🇨🇱 CL | CES (Certificación de Edificio Sustentable) | Voluntary; mandatory for some public buildings | est. <5% of stock — verify at certificacionsustentable.cl | certificacionsustentable.cl |
| 🇿🇦 ZA | SANS 10400-XA energy efficiency (post-2008 builds) | Mandatory at building plan approval | Pre-2008 stock unrated; post-2011 stock subject to XA — verify at sabs.co.za | sabs.co.za |
| 🇬🇪 GE | Nascent regime — EU candidate alignment in progress | Not yet mandatory | Distribution data not publicly available — verify at economy.ge | economy.ge |
| 🇮🇩 ID | GREENSHIP (GBCI) | Voluntary | Sub-1% of stock — verify at gbcindonesia.org | gbcindonesia.org |
| 🇲🇾 MY | GBI (GreenBuildingIndex) + GreenRE | Voluntary | est. <5% of commercial; residential rare — verify at greenbuildingindex.org | greenbuildingindex.org |
| 🇻🇳 VN | LOTUS (VGBC) + EE Law 2010 framework | Voluntary | Sub-1% — verify at vgbc.vn | vgbc.vn |
| 🇵🇭 PH | BERDE (PhilGBC) + DOE Philippine Green Building Code (2024 update) | DOE code mandatory in scope (large buildings); BERDE voluntary | Residential coverage low — verify at philgbc.org / doe.gov.ph | philgbc.org; doe.gov.ph |
| 🇮🇱 IL | Israeli Standard 5281 (בנייה ירוקה / green building) | Mandatory rating for new builds from 2022 | Older stock unrated — verify at sii.org.il | sii.org.il |
| 🇲🇦 MA | HEQ certification + Loi 47-09 energy efficiency (2014) | 47-09 mandatory at permit; HEQ voluntary | Pre-2014 stock largely unrated — verify at amee.ma | amee.ma |
| 🇪🇬 EG | GPRS (Green Pyramid Rating System) | Voluntary; mandatory for some New Capital projects | Sub-1% of national stock — verify at hbrc.edu.eg | hbrc.edu.eg |
| 🇸🇬 SG | BCA Green Mark | Mandatory for new builds + major retrofits since 2008 (Building Control Regulations) | Coverage broad on new build; older HDB/private stock unrated unless Green Mark Existing — verify at bca.gov.sg | bca.gov.sg |
| 🇭🇰 HK | BEAM Plus + EMSD MEEO (Mandatory Energy Efficiency Labelling) | BEAM voluntary; MEEO mandatory for buildings >5,000 m² gross floor area (commercial subset) | Residential coverage low — verify at beamsociety.org.hk + emsd.gov.hk | beamsociety.org.hk; emsd.gov.hk |
| 🇰🇷 KR | G-SEED (Green Standard for Energy and Environmental Design) + Building Energy Efficiency Rating System | G-SEED mandatory for public buildings + voluntary private; energy-rating mandatory at sale/rent for selected building types since 2016 | Coverage growing; older stock often unrated — verify at greentogether.go.kr | greentogether.go.kr |
| 🇹🇼 TW | EEWH (Ecology, Energy saving, Waste reduction, Health) | Mandatory for public buildings ≥NTD 50M; voluntary private | Sub-5% of stock rated — verify at abri.gov.tw | abri.gov.tw |
| 🇱🇮 LI | n/a (small jurisdiction; cross-references CH MINERGIE / GEAK) | Voluntary; CH MINERGIE acceptable | Coverage low — verify at llv.li / minergie.ch | llv.li; minergie.ch |
| 🇲🇴 MO | n/a (no comprehensive public regime as of Apr 2026) | — | data not publicly available — verify at dscc.gov.mo | dscc.gov.mo |
| 🇦🇩 AD | n/a (small jurisdiction; cross-references EU EPBD via Spain/France markets) | Not yet mandatory | data not publicly available — verify at govern.ad | govern.ad |
| 🇲🇨 MC | French DPE acceptable for properties marketed to FR-jurisdiction buyers | French DPE not formally mandatory in MC but commonly used | data not publicly available — verify at gouv.mc | gouv.mc |
| 🇲🇩 MD | EU candidate alignment in progress — EPBD transposition draft (no in-force regime as of Apr 2026) | Not yet mandatory | Distribution data not publicly available — verify at minfin.gov.md / mediu.gov.md | minfin.gov.md; mediu.gov.md |

**Caveat**: These regimes use **different scales** (HERS is 0-150 with lower=better; BERDE is 1-5 stars; Estidama is 1-5 Pearls; SANS 10400-XA is pass/fail; BCA Green Mark is Certified/Gold/GoldPLUS/Platinum; BEAM Plus is Bronze/Silver/Gold/Platinum; G-SEED is 1-7 grade; EEWH is Certified/Bronze/Silver/Gold/Diamond). They are **not** equivalent to EU A-G classes and must not be presented on the same axis.

## Worst-class rental ban schedule

### Active bans (Apr 2026)
- **🇫🇷 FR**: Class G new tenancies banned **1 Jan 2025**; F banned **1 Jan 2028**; E banned **1 Jan 2034** (per Loi Climat-Résilience). **Audit énergétique** mandatory at sale for G (Apr 2023) + F (Apr 2025)
- **🇳🇱 NL**: Office buildings min C since 2023; residential bans phasing through Wet betaalbare huur 2024
- **🇩🇪 DE**: GEG mandatory upgrade triggers on inheritance/sale (replace oil/gas heater within 2 years if H is in fossil-fuel mode)

### Coming bans (announced for 2026-2030)
- **🇪🇸 ES**: Plan Nacional Vivienda includes worst-class restrictions from 2027 [verify]
- **🇧🇪 BE**: Flemish region phasing minimum class for rental from 2028 [verify]
- **🇮🇪 IE**: Climate Action Plan 2024 — minimum BER for rentals proposed 2025 [verify final form]
- **🇮🇹 IT**: Decreto Salva Casa 2024 + EPBD recast deadlines

### EU EPBD recast (2024/1275) — affects ALL EU/EEA
- **Public + non-residential buildings**: minimum class to F by 2027; E by 2030
- **Residential**: minimum class to E by 2030; D by 2033
- Member State transposition deadline: **29 May 2026**

## Climate exposure index per country

(Composite of Climate Central sea-level rise risk + Copernicus heat-stress + Copernicus drought index + GFW wildfire activity)

### Highest exposure
- 🇮🇸 IS — Reykjanes volcanic series since Dec 2023 (9 eruptions); Grindavík evacuated
- 🇲🇹 MT — water scarcity acute; sea-level rise on low-lying coastal SDAs
- 🇨🇾 CY — drought-stressed (2025 worst since 1901); wildfire risk Limassol foothills
- 🇮🇹 IT — south heatwaves + drought; coastal Veneto/Liguria flood
- 🇪🇸 ES — drought-stressed Andalucía/Murcia; coastal flood; DANA 2024 reference
- 🇵🇹 PT — Algarve drought; wildfire interior
- 🇬🇷 GR — wildfire (2023 worst on record); coastal islands tourism+water
- 🇧🇬 BG — 2024 worst-recorded wildfire year (~600 fires)
- 🇭🇷 HR — Adriatic coastal flood + wildfire interior
- 🇦🇱 AL — coastal flood + 2019 Durrës earthquake legacy
- 🇲🇪 ME — coastal flood + earthquake risk

### Mid exposure
- 🇫🇷 FR — Catnat covers; PPRN expansion 2025; Mediterranean coastal stress
- 🇨🇭 CH — Alpine landslide; cantonal mandatory insurance
- 🇸🇰 SK, 🇭🇺 HU, 🇨🇿 CZ — Central European flood (2024 Boris)
- 🇸🇮 SI — 2023 floods exposed underinsurance
- 🇷🇴 RO — Vrancea seismic Bucharest; Apele Române flood
- 🇨🇦 CA — wildfire Western provinces; flood national pool 2025
- 🇦🇺 AU — Cyclone Pool ARPC; Northern QLD flood/cyclone
- 🇳🇿 NZ — earthquake (Toka Tū Ake mandatory) + 2023 Auckland floods

### Lower exposure
- Northern Europe: 🇸🇪 SE, 🇫🇮 FI, 🇩🇰 DK, 🇳🇱 NL (dyke-protected), 🇧🇪 BE, 🇩🇪 DE
- Baltics: 🇪🇪 EE, 🇱🇻 LV, 🇱🇹 LT (some coastal storm surge)
- Central: 🇱🇺 LU, 🇦🇹 AT (Alpine but low-density); UK (mostly)

### Tier-1 + Tier-2 expansion (Apr 2026, public-source composite)

Hazard tags below are derived from primary national/UN sources (USGS, JMA, JRC INFORM, ThinkHazard!, Climate Central). Parcel-level claim requires a parcel risk pull (state/national flood map, seismic microzonation) — see `shared/climate.md` for the per-country verification path.

**Highest exposure (Tier-1 + Tier-2)**:
- 🇯🇵 JP — Megaquake risk (Nankai Trough, JMA active monitoring); typhoon + tsunami; Mt Fuji volcanic monitoring [verify at jma.go.jp]
- 🇵🇭 PH — typhoon belt (avg ~20/yr); seismic (PHIVOLCS); Taal/Mayon volcanic — verify at phivolcs.dost.gov.ph
- 🇮🇩 ID — Pacific Ring of Fire seismic + tsunami; volcanic (>120 active); Jakarta land subsidence — verify at bmkg.go.id
- 🇩🇴 DO — North-Atlantic hurricane belt (peak Aug-Oct); Hispaniola seismic — verify at onamet.gov.do
- 🇨🇱 CL — subduction-zone seismic (Mw 8.8 2010 reference); Atacama mega-drought ongoing since 2010; tsunami — verify at sernageomin.cl
- 🇨🇴 CO — Andean seismic; Pacific tsunami; Magdalena/Cauca flood — verify at sgc.gov.co
- 🇪🇬 EG — Nile Delta sea-level rise (Climate Central: ~30% Alexandria below SLR-2050 line); water scarcity — verify at climatecentral.org
- 🇲🇦 MA — 2023 Marrakech-Al Haouz Mw 6.8 quake; coastal Atlantic storm — verify at cnrst.ma
- 🇹🇷 TR — North Anatolian Fault (2023 Kahramanmaraş Mw 7.8 — 50k+ deaths); coastal Aegean — verify at afad.gov.tr
- 🇮🇱 IL — Dead Sea Transform fault; coastal SLR Tel Aviv — verify at gsi.gov.il

**Mid exposure**:
- 🇺🇸 US — multi-hazard by region: CA wildfire/quake; FL/TX hurricane; Tornado Alley; AK seismic — verify at fema.gov / usgs.gov
- 🇦🇪 AE — extreme heat (50°C+ summer); Apr 2024 Dubai flooding (cloud-seeding controversy); coastal SLR Palm/Marina — verify at ncm.ae
- 🇹🇭 TH — Bangkok subsidence + monsoon flood; tsunami Andaman coast (2004 reference) — verify at tmd.go.th
- 🇲🇾 MY — monsoon flood (2021 Selangor reference); peat-fire haze — verify at met.gov.my
- 🇻🇳 VN — typhoon coast; Mekong Delta SLR + saline intrusion — verify at nchmf.gov.vn
- 🇿🇦 ZA — Western Cape "Day Zero" drought (2018 reference); KZN floods (2022); coastal storm — verify at weathersa.co.za
- 🇺🇾 UY — coastal flood Río de la Plata; drought 2022-23 — verify at inumet.gub.uy

**Lower-but-not-zero exposure**:
- 🇬🇪 GE — Caucasus seismic; Black Sea coastal storm — verify at nea.gov.ge

### Tier-3 expansion (Apr 2026)

**Highest exposure (Tier-3)**:
- 🇹🇼 TW — Pacific Ring of Fire seismic (Apr 2024 Hualien Mw 7.4 reference, also 921 Sep 1999 Mw 7.7 baseline); typhoon belt; coastal storm Taipei basin flood — verify at cwa.gov.tw (Central Weather Administration / 中央氣象署)
- 🇭🇰 HK — typhoon belt (avg ~5-6 affecting/yr); coastal SLR; landslide hill-side districts (HKO + GEO Geotechnical Engineering Office monitoring); urban heat — verify at hko.gov.hk / cedd.gov.hk
- 🇲🇴 MO — typhoon belt + coastal SLR (Mangkhut Sep 2018 reference); reclaimed-land subsidence — verify at smg.gov.mo (Direcção dos Serviços Meteorológicos e Geofísicos)
- 🇰🇷 KR — coastal storm + monsoon flood (Aug 2022 Seoul Gangnam flood reference); Pohang Mw 5.4 Nov 2017 induced-seismicity reference; typhoon SE coast — verify at kma.go.kr
- 🇲🇩 MD — Vrancea Mw 7+ seismic legacy (Mar 1977 Bucharest reference also affected Chișinău); flood Prut/Nistru basins; drought 2007/2012/2020 reference — verify at meteo.md (Serviciul Hidrometeorologic de Stat)

**Mid exposure (Tier-3)**:
- 🇸🇬 SG — coastal SLR (~30% land below 5m elevation per CCRS Centre for Climate Research Singapore); urban heat island; transboundary haze (Indonesian peat-fire) Jul-Oct — verify at nea.gov.sg / ccrs.weather.gov.sg

**Lower-but-not-zero exposure (Tier-3)**:
- 🇱🇮 LI — Alpine landslide / avalanche; flood Rhine; cross-references MeteoSwiss + Hydroamt — verify at llv.li
- 🇦🇩 AD — Alpine avalanche (FORTA Servei de Forces de Comunicacions monitoring); flood Valira; wildfire drought summers — verify at meteo.ad (SAGEMM)
- 🇲🇨 MC — coastal SLR (Plan Bleu / Plan Climat Monaco — verify at gouv.mc); Mediterranean storm; very small footprint limits parcel-level variation

## Community impact / walkability / renewable share

### Highest renewable-share electricity grids (host country)
- 🇮🇸 IS: ~100% (geothermal + hydro)
- 🇳🇴 NO: ~98% (hydro)
- 🇸🇪 SE: ~75% (hydro + nuclear)
- 🇩🇰 DK: ~80% (wind)
- 🇨🇭 CH: ~62% (hydro)
- 🇦🇹 AT: ~80% (hydro)
- 🇵🇹 PT: ~67% (wind+solar)
- 🇫🇮 FI: ~50% (hydro+nuclear+wind)

### Lowest renewable-share (most fossil-dependent)
- 🇲🇹 MT: ~10% (single submarine cable to Sicily)
- 🇨🇾 CY: ~14% (island isolation)
- 🇵🇱 PL: ~21% (coal-heavy still)
- 🇨🇿 CZ: ~16%
- 🇷🇸 RS: ~30%
- 🇧🇦 BA: ~40%

### Tier-1 + Tier-2 grid mix (% renewable, electricity, latest national figures)

Sources: IEA national reports + national grid operator data, latest available; figures rounded.

| Country | % renewable (electricity) | Notable | As-of |
|---|---:|---|---|
| 🇺🇾 UY | ~98% | Wind + hydro + solar — 2017 milestone; among highest in world | 2024 (UTE) |
| 🇨🇴 CO | ~70% | Hydro-dominant; El Niño exposure | 2024 (XM) |
| 🇨🇱 CL | ~55% | Solar (Atacama) + wind growth | 2024 (CNE) |
| 🇿🇦 ZA | ~15% | Coal-heavy (Eskom); load-shedding still endemic | 2024 (Eskom) |
| 🇲🇦 MA | ~40% | Noor Ouarzazate solar; wind Tarfaya — target 52% by 2030 | 2024 (ONEE) |
| 🇺🇸 US | ~22% | Wide state variation: WA/OR ~70%+; WV/KY <5% | 2024 (EIA) |
| 🇯🇵 JP | ~24% | Solar + hydro; nuclear restart trajectory | 2024 (METI) |
| 🇮🇱 IL | ~13% | Solar growth target 30% by 2030 | 2024 (energy.gov.il) |
| 🇹🇷 TR | ~44% | Hydro + wind + geothermal + solar | 2024 (TEİAŞ) |
| 🇦🇪 AE | ~7% | Mostly natural gas; Barakah nuclear adds capacity (not classed renewable) | 2024 (DEWA / FEWA) |
| 🇹🇭 TH | ~12% | Natural-gas dominant | 2024 (EPPO) |
| 🇲🇾 MY | ~18% | Hydro Sarawak; solar growth peninsular | 2024 (energycommission.gov.my) |
| 🇻🇳 VN | ~40% | Hydro + recent solar boom (2020-22) | 2024 (EVN) |
| 🇵🇭 PH | ~22% | Geothermal + hydro | 2024 (DOE) |
| 🇮🇩 ID | ~14% | Coal-dominant | 2024 (PLN) |
| 🇩🇴 DO | ~18% | Solar + wind growth; oil/gas dominant | 2024 (CNE) |
| 🇪🇬 EG | ~12% | Hydro Aswan + solar Benban | 2024 (EgyptERA) |
| 🇬🇪 GE | ~80% | Hydro-dominant (Caucasus) | 2024 (gnerc.org) |
| 🇸🇬 SG | ~5% | Natural-gas dominant (~95%); SolarNova rooftop programme expanding | 2024 (EMA Energy Market Authority) |
| 🇭🇰 HK | ~1% | Coal + LNG dominant; Climate Action Plan 2050 targets phase-out coal by 2035 | 2024 (CLP/HK Electric / EMSD) |
| 🇰🇷 KR | ~10% | Coal + LNG + nuclear dominant; renewables (solar/wind) growing — verify at kpx.or.kr | 2024 (KEPCO/KPX) |
| 🇹🇼 TW | ~12% | Coal + LNG dominant; nuclear phase-out delayed; solar + offshore-wind growing | 2024 (taipower.com.tw) |
| 🇲🇴 MO | ~15% (incl. Guangdong-grid imports) | Mostly Guangdong-grid imports (~80%); local solar minimal — verify at dscc.gov.mo | 2024 (CEM) |
| 🇲🇩 MD | ~25% est. | Hydro Costești-Stînca (shared with RO); imports from RO post-2022 grid-sync (Mar 2022) reduced gas-import dependency — verify at moldelectrica.md | 2024 (ANRE) |
| 🇱🇮 LI | ~70% est. | CHF-grid integrated; hydro + cross-border CH grid dominant — verify at llv.li | 2024 (LKW Liechtensteinische Kraftwerke) |
| 🇦🇩 AD | ~25% (incl. domestic hydro + ES-grid imports) | Mostly ES-grid imports; FEDA hydro Engolasters — verify at feda.ad | 2024 (FEDA) |
| 🇲🇨 MC | n/a (FR-grid integrated) | EDF-grid (FR mix ~75% nuclear + renewables) — verify at gouv.mc | 2024 (SMEG) |

## Recent climate-adaptation policy (Tier-1 + Tier-2)

Date-stamped reform tracking — for revisit cadence see `shared/regulatory-watch.md`.

- 🇺🇸 US — **IRA §25C / §25D residential energy credits TERMINATED 31 Dec 2025** per OBBBA (Jul 2025). Pre-31-Dec-2025 expenditures grandfathered. State programs (CA Title 24, NY LL97) unchanged.
- 🇹🇷 TR — Climate Law (İklim Kanunu) parliamentary draft 2024-2025; ETS-style scheme proposed. Verify enacted form at csb.gov.tr.
- 🇦🇪 AE — UAE Net Zero 2050 framework (announced 2021); COP28 hosted Nov 2023; National Climate Change Plan 2017-2050.
- 🇯🇵 JP — **2025 Building Energy Conservation Act** mandates higher efficiency for all new builds Apr 2025. GX-ETS (carbon-pricing voluntary phase) launched 2023, mandatory 2026.
- 🇹🇭 TH — Climate Change Act enacted 2024 (framework only — implementing levy not active).
- 🇩🇴 DO — ENERSOL solar program for residential (subsidies; verify scope at mem.gob.do); hurricane code post-Maria.
- 🇨🇴 CO — **Ley 2169/2021** carbon-neutrality 2050 + climate transition framework.
- 🇺🇾 UY — National Climate Change Policy (2017); 100%-renewable electricity milestone (2017); CO2/EE cert pilot ongoing.
- 🇨🇱 CL — **Código de Aguas reform 2022/2024** (water priority for human consumption); Ley Marco de Cambio Climático 21.455 (2022).
- 🇿🇦 ZA — Climate Change Act signed Jul 2024; Carbon Tax Act 2019 in force (large emitters).
- 🇬🇪 GE — EU candidate alignment in progress; National Energy & Climate Plan draft; targets harmonisation 2030.
- 🇮🇩 ID — RUEN (Rencana Umum Energi Nasional) energy plan; FOLU Net Sink 2030 forestry-focused commitment.
- 🇲🇾 MY — Net Zero 2050 commitment (announced 2021); National Energy Transition Roadmap (Aug 2023).
- 🇻🇳 VN — **EE Law 2010** (energy efficiency framework); JETP (Just Energy Transition Partnership) USD 15.5B announced Dec 2022.
- 🇵🇭 PH — **DOE Philippine Green Building Code 2024 update**; Climate Change Act 2009 (framework).
- 🇮🇱 IL — Israeli Standard 5281 mandatory for new builds from 2022; Climate Law draft pending Knesset.
- 🇲🇦 MA — **Loi 47-09** energy efficiency (2014); Noor Ouarzazate solar complex (~580 MW); 52% renewable target 2030.
- 🇪🇬 EG — Egypt Vision 2030 sustainability axis; New Administrative Capital green-build mandates; COP27 hosted Nov 2022.
- 🇸🇬 SG — **Singapore Green Plan 2030**; Carbon Pricing Act SGD 25/tCO2 (2024-25), SGD 45 (2026-27), SGD 50-80 (by 2030); BCA Green Mark mandatory new build since 2008 — verify at greenplan.gov.sg.
- 🇭🇰 HK — **Climate Action Plan 2050** (Oct 2021); coal phase-out by 2035 target; MEEO Mandatory Energy Efficiency Labelling (commercial subset); BEAM Plus voluntary — verify at climateready.gov.hk.
- 🇰🇷 KR — **Carbon Neutrality and Green Growth Framework Act** (Aug 2022); KETS Korea Emissions Trading Scheme since 2015 (Phase 4 2026-30 in design); G-SEED + Building Energy Efficiency Rating mandatory for some types — verify at me.go.kr.
- 🇹🇼 TW — **Climate Change Response Act** (passed Jan 2023, implementing carbon-fee draft 2024 — verify enacted form at moenv.gov.tw); EEWH mandatory for public buildings.
- 🇲🇴 MO — **Macao Climate Action Plan 2030** (verify at dspa.gov.mo); no comprehensive carbon levy as of Apr 2026.
- 🇲🇩 MD — EU candidate alignment in progress (accession negotiations opened Jun 2024); EPBD transposition draft pending — verify at minfin.gov.md / mediu.gov.md.
- 🇱🇮 LI — Energy Strategy 2030 (CHF-aligned; cross-references Swiss CO2 Act); CHF 120/tCO2 effective via CH integration — verify at llv.li.
- 🇦🇩 AD — Energy & Climate Strategy 2030 (energia.ad); no comprehensive carbon levy as of Apr 2026 — verify at govern.ad.
- 🇲🇨 MC — **National Energy Transition Plan 2017-2030**; carbon-neutrality by 2050 commitment; FR-grid integrated — verify at gouv.mc.

**Rule**: Reforms in this list with `2024+` effective dates require cross-check at the country's primary ministry URL before quoting in a final report — frameworks often pass before implementing regulations.

### Best walkability / public transport (urban):
- Vienna 🇦🇹, Zurich 🇨🇭, Copenhagen 🇩🇰, Amsterdam 🇳🇱, Paris 🇫🇷 (intra-mura), Berlin 🇩🇪, Munich 🇩🇪, Stockholm 🇸🇪, Helsinki 🇫🇮, Oslo 🇳🇴
- Singapore 🇸🇬 (LTA MRT + bus + walkability top-tier; ~80% household-to-MRT 10-min walk per LTA), Hong Kong 🇭🇰 (MTR + minibuses + escalator-network Central-Mid-Levels), Macao 🇲🇴 (small footprint + LRT Taipa/Cotai), Seoul 🇰🇷 (Seoul Metro + KTX intercity), Taipei 🇹🇼 (MRT + YouBike), Monaco 🇲🇨 (small footprint, CAM bus + free vertical lifts/elevators)

### Worst walkability (car-dependent):
- US sprawl (not in skill), CA suburbs, AU suburbs, NZ outside Auckland/Wellington
- LatAm interior cities

## Carbon-tax / property energy levy

| Country | Carbon tax / energy levy | Rate / status |
|---|---|---|
| 🇫🇷 FR | TICPE on heating fuel | Variable; gas/oil cap-and-trade EU ETS2 from 2027 |
| 🇩🇪 DE | National CO2 price | €65/tonne 2026 (EU ETS2 from 2027) |
| 🇸🇪 SE | Highest carbon tax in EU | €130/tonne |
| 🇫🇮 FI | Carbon tax | €77/tonne |
| 🇳🇴 NO | Carbon tax | €83/tonne (NOK ~900) |
| 🇨🇭 CH | CO2 tax | CHF 120/tonne |
| 🇪🇺 ALL | EU ETS2 | €45/tonne starting 2027 (transport + buildings) |
| 🇨🇦 CA | Federal carbon levy | CAD 95/tonne 2026 |
| 🇺🇸 US | No federal carbon tax. State RGGI cap-and-trade (NE states) + CA cap-and-trade. **IRA tax credits §25C/§25D TERMINATED 31 Dec 2025** per OBBBA Jul 2025 — verify at irs.gov/pub/irs-pdf/p5886.pdf | RGGI auction price ~$15-25/tonne 2025; CA ~$30/tonne 2025 |
| 🇿🇦 ZA | Carbon Tax Act 2019 (incl. Apr 2025 rate hike to ZAR 236/tonne) — applies to large emitters, **not residential heating** | ZAR 236/tonne 2025 — verify at sars.gov.za |
| 🇯🇵 JP | "Tax for Climate Change Mitigation" (carbon surcharge on petroleum/coal/gas) | JPY 289/tonne CO2 (2012-set, low) — verify at env.go.jp; GX-ETS phasing in from 2026 |
| 🇨🇱 CL | Green tax (Ley 20.780 / 2014) on stationary emitters >50MWth — not residential | USD 5/tonne 2025 — verify at sii.cl |
| 🇨🇴 CO | National carbon tax on fossil fuels (Ley 1819/2016) | ~COP 27,800/tonne (~USD 6-7) 2025 — verify at dian.gov.co |
| 🇺🇾 UY | CO2 tax on petroleum (IMESI overlay, 2022) | est. USD 137/tonne (highest in LatAm) — verify at impo.com.uy |
| 🇮🇱 IL | No comprehensive carbon tax as of Apr 2026; phased fuel-tax adjustments announced — verify at finance.gov.il | — |
| 🇹🇷 TR | No carbon tax as of Apr 2026; Climate Law (2024 prep) under parliamentary review — verify at csb.gov.tr | — |
| 🇦🇪 AE | No carbon tax. UAE Net Zero 2050 framework relies on subsidies + energy-efficiency mandates — verify at moccae.gov.ae | — |
| 🇹🇭 TH | No carbon tax in force; Climate Change Act 2024 enacted but levy not active — verify at onep.go.th | — |
| 🇩🇴 DO 🇲🇾 MY 🇻🇳 VN 🇵🇭 PH 🇲🇦 MA 🇪🇬 EG 🇮🇩 ID 🇬🇪 GE | No comprehensive carbon tax on residential property as of Apr 2026 | data not publicly available — verify at each country's environment ministry |
| 🇸🇬 SG | Carbon Pricing Act (since 2019); applies to facilities emitting ≥25kt CO2e/yr (large emitters, NOT residential) | SGD 25/tCO2 (2024-25), SGD 45 (2026-27), SGD 50-80 by 2030 — verify at nccs.gov.sg |
| 🇭🇰 HK | No carbon tax as of Apr 2026; Climate Action Plan 2050 relies on regulatory mandates + electricity-sector retirement schedule — verify at climateready.gov.hk | — |
| 🇰🇷 KR | KETS (ETS for ~700 large emitters covering ~74% national emissions) + Petroleum & Energy Tax | KETS allowance KRW ~10,000/tCO2 (2024 average — verify at gir.go.kr); does NOT directly hit residential heating |
| 🇹🇼 TW | Carbon-fee scheme enacted via Climate Change Response Act 2023; applies to ≥25kt CO2e/yr facilities — NOT residential | Rate NTD 300/tCO2 from 2025 (transitional) — verify at moenv.gov.tw |
| 🇱🇮 LI | CHF 120/tCO2 effective via CH CO2 Act integration (Currency Treaty + customs union with CH) — verify at llv.li | CHF 120/tCO2 (CH-aligned) |
| 🇲🇨 MC | No comprehensive carbon levy as of Apr 2026 — National Energy Transition Plan relies on subsidies + mandates — verify at gouv.mc | — |
| 🇦🇩 AD 🇲🇴 MO 🇲🇩 MD | No comprehensive carbon tax on residential property as of Apr 2026 | data not publicly available — verify at each country's environment / energy ministry |

For property buyers: **carbon levy on heating fuel directly affects annual operating cost**. Class F/G buildings on oil/gas heating face increasing operating cost over the next 5-10 years.

In tropical / subtropical markets (TH, ID, MY, VN, PH, AE, EG, DO), carbon-cost overlay on **cooling** (electricity for AC) is the dominant operational-cost lever — not heating fuel. The grid-mix renewable share + electricity tariff drives this; see `shared/mains.md`.

## Brown-discount evidence (research-backed)

- Studies in DE/UK/IE find **0.7-1.5% per EPC class** discount/premium (e.g., a class G property sells at ~3-4% discount to class C; class A at ~3-4% premium)
- Discount widening post-2024 as EPBD recast and climate awareness grow
- Worst-case for stranded assets: pre-1970s rural properties in countries with rental-ban schedules

## Anti-hallucination

- **EPC distributions** are estimates from EU Buildings DB + national reports — vary by year and recategorization
- **Worst-class rental bans** are policy commitments — verify enacted vs proposed
- **Climate exposure** is composite — single-event certainty (Iran-conflict 2026 energy shock) doesn't translate to property-stranded-risk certainty
- **Carbon-tax rates** change annually — verify current rate before committing to 30-yr operating cost projection

## Status

Last refreshed: 2026-05-01 (Tier-3 expansion — 9 countries: SG/HK/KR/TW/LI/MO/AD/MC/MD; cumulative 71 countries).

**Confidence**: MEDIUM — non-EU energy-rating regimes use different scales (HERS, BELS, BERDE, GREENSHIP, GBI, LOTUS, GPRS, Estidama, CES, Pearl, IS 5281, BCA Green Mark, BEAM Plus, G-SEED, EEWH) which are not directly comparable to EU A-G EPC; stock-penetration figures are estimates per published regime sources. Carbon-tax rates valid as of latest national publication; revisit cadence per `shared/regulatory-watch.md`.
