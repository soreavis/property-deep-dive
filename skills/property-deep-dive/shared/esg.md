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

### Best walkability / public transport (urban):
- Vienna 🇦🇹, Zurich 🇨🇭, Copenhagen 🇩🇰, Amsterdam 🇳🇱, Paris 🇫🇷 (intra-mura), Berlin 🇩🇪, Munich 🇩🇪, Stockholm 🇸🇪, Helsinki 🇫🇮, Oslo 🇳🇴

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

For property buyers: **carbon levy on heating fuel directly affects annual operating cost**. Class F/G buildings on oil/gas heating face increasing operating cost over the next 5-10 years.

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

Last refreshed: 2026-04-26.
