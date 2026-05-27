# Universal `--rental` Section — Yield-Delta + Neighborhood STR Zoning Extension

Marketed-gross-vs-realistic-net yield delta + neighborhood-level STR zoning registry for the property's country. Loaded when `--rental` is invoked alongside the per-country STR income/regime layer in each country playbook.

**Snapshot**: May 2026.

**Scope**: this doc supplies the *delta* layer — what gets *subtracted* from a marketed gross-yield headline (platform fees, management, lodging tax, regulatory day-cap haircut, insurance uplift, vacancy seasonality) — plus the *neighborhood-zone* layer (district / postcode / arrondissement / borough-level STR restrictions beyond what is captured at country level in `regulatory-watch.md`). The *base* layer (which STR regime applies country-wide, what STR licence the country requires, what STR income tax bracket applies) lives in each country's playbook `--rental` section.

## Universal contract

For the property's country + neighborhood, return:

1. **Cost-line stack**: 6 line items quantified (platform fee · management · lodging/tourist tax · regulatory rental-day cap · STR insurance uplift · vacancy band)
2. **Marketed gross yield**: cite the listing-platform or aggregator headline (Idealista / SeLoger / Spitogatos / AirDNA / Inside Airbnb / Global Property Guide / national portal)
3. **Realistic net yield**: transparent computation — `marketed_gross − Σ(cost lines) − regulatory_haircut → est. net (inputs above)`
4. **Yield-delta verdict band**: 🟢 ≤2 pp · 🟡 2-4 pp · 🟠 4-6 pp · 🔴 >6 pp or regulatory-kill (day-cap binding, licence freeze, zone moratorium, structural ban)
5. **Neighborhood-zone overlay**: district / arrondissement / borough rules (citing ordinance + effective date) where they materially diverge from the country baseline
6. **Compliance gate**: is a licence required? is it transferable on resale? is there a freeze on new entrants?
7. **Confidence**: HIGH / MEDIUM / LOW per the skill's contract

## Platform-fee baseline (2026 reset)

Airbnb finished migrating from the split-fee model (3% host + 14-16.5% guest) to **host-only 15.5%** for PMS-connected hosts on 27 Oct 2025; non-PMS hosts auto-migrated by 1 Dec 2025. PMS-flow hosts complete transition 13 Apr 2026. **Brazil hosts: 16%** (above global 15.5%). Treat **15.5% host-only** as the 2026 baseline; pre-Dec-2025 yield computations using "3% host fee" inputs are **stale** and must be re-stamped. [Airbnb host-fee resource](https://www.airbnb.com/resources/hosting-homes/a/simplifying-airbnb-service-fees-746) · [Hostaway 15.5% explainer](https://www.hostaway.com/blog/airbnb-host-only-fee-what-to-know-about-the-15-percent-host-fee/) · [PriceLabs rollout](https://hello.pricelabs.co/airbnb-host-fee-update/).

Booking.com: **15% baseline + 3 pp Preferred Partner + ~8 pp Superior Preferred** (total up to ~23%); Payments-by-Booking adds 1.1-3.1 pp. [Booking partner help](https://partner.booking.com/en-us/help/commission-invoices-tax/commission/understanding-our-commission).

Vrbo: **8% (5% commission + 3% payment) pay-per-booking**; subscription model alternative. [Lodgify Vrbo fees](https://www.lodgify.com/guides/vrbo/fees/).

Management commission bands (no trade-body central rate-card surfaced for FEVITUR ES / ALEP PT / FIAIP IT / SETE GR / APAVT PT / DLD AE — all figures aggregator-derived, verify with named operator):

| Segment | Short-let | Long-let |
|---|---|---|
| Western EU (FR / UK / IE / NL / BE / DE / AT / CH / LU) | 18-25% | 6-12% (ARLA / PSRA / NRLA) |
| Southern EU (ES / PT / IT / GR / CY / MT) | 20-30% | 8-12% |
| Eastern EU + Balkans + Baltics | 20-30% | 8-15% |
| Americas (Vacasa / AvantStay / Evolve / Sykes US-CA; named ops MX / BR / AR / CO / CL) | 25-35% (Vacasa effective 40%+ with add-ons) | 8-12% |
| Asia + Oceania (Squeeze / AirHost / Frank Porter / Bnbme / Bukit Vista) | 18-30% | 5-10% APAC |
| MENA + Africa (Frank Porter / Bnbme / Driven / Houst / yourhost.ma) | 15-30% | 5-7% AE, 8-12% others |

## Yield-delta verdict bands

| Band | Marketed-vs-net pp delta | Regulatory overlay | When to use |
|---|---|---|---|
| 🟢 | ≤ 2 pp | No zone freeze, no day-cap binding, registration-only compliance | "Pricing reflects costs; light regulatory risk; foreign-buyer thesis defensible." |
| 🟡 | 2-4 pp | Compliance burden present but achievable; day-cap exists but not yet binding | "Pricing partly optimistic; verify cost stack on parcel; manageable regulatory risk." |
| 🟠 | 4-6 pp | Day-cap binding OR zone restriction OR sale-trigger expiry OR pending moratorium | "Marketed yield substantially overstates net; underwrite as long-let-equivalent or apply 30-50% haircut." |
| 🔴 | > 6 pp or **regulatory-kill** | Outright STR ban, citywide unlicensed-illegal, zone freeze blocking new entrants, criminal penalties | "STR thesis structurally void in this zone — re-base as long-let or skip." |

**Regulatory-kill** triggers 🔴 regardless of cost-line delta:
- Citywide unlicensed STR illegal (HK <28d Cap 349, SG <3mo URA private / <6mo HDB, TH Hotel Act §4 <30d, CN domestic Airbnb suspended 30 Jul 2022, BD foreign-buyer STR unviable)
- Zone-level freeze on new licences (BCN PEUAT Zone 1, MAD Distrito Centro PEH, LIS Áreas de Contenção Absoluta, ATH 1st/2nd/3rd Municipal Districts AMA freeze, AMS 8 stress neighborhoods 15-night cap from 1 Apr 2026, HU Budapest VI Decree 26/2024 zero-day from 1 Jan 2026)
- Sale-triggered licence expiry (Lisbon containment zones — apartment-mode AL dies on resale, non-transferable)
- Day-cap binding (NYC LL18 <30d host-present-only, Paris 90-day primary residence + 0d non-principal, Loi Le Meur effective; Ireland 90-day PPR-only post-RPZ universalization 20 Jun 2025; Amsterdam 30/15d; Auckland APTR + Queenstown 90-day; Sydney Greater 180d non-hosted + Byron 60d)
- Criminal penalties (HK HK$200k + 2yr; TR Law 7464 TRY 100k-1M + unanimous co-owner consent; Bali nominee structures 5yr prison + IDR 1bn from Perda 4/2026)

## ⚠️ 7 cross-cutting traps

1. **Marketed gross yields are listing-platform-controlled** — Idealista / SeLoger / Spitogatos / Inmuebles24 / Property Finder publish gross numbers that exclude every cost line below. A 7% Idealista gross can become a 2.5% net once platform + management + tourist tax + regulatory haircut are applied. Treat platform yields as **seller-controlled** per the skill's source-ranking contract.
2. **Day-cap × ADR ≠ static computation** — a 90-day cap at $200 ADR with 78% occupancy is not "90 × $200 = $18k"; it is "90 × $200 × occupancy_within_cap". Paris 90-day, NYC LL18 <30d, AMS 30→15d, Sydney 180d, Queenstown 90d all bind utilisation, not just nights. Re-compute on the binding constraint, not the headline.
3. **Sale-triggered expiry destroys licence transferability** — Lisbon containment zones (Santa Maria Maior 68.8%, Misericórdia, Príncipe Real, Graça, Bica): selling an apartment-mode AL = automatic licence death; buyer cannot relist. Same logic in Porto Vitória 60.5% / São Nicolau 48.3% / Sé 44.1%. Underwrite the licence as **non-transferable on resale** unless explicitly confirmed otherwise.
4. **Condo / strata / co-owner consent is often binding before zoning is** — TR Law 7464 requires unanimous written consent of all co-owners (structural ban in most apartment buildings); HR 2024 amendment requires 66% (new registration) or 80% (5-year retention); MY 2025 Court of Appeal *Wawasan Raya v MARC* confirmed MC by-law STR bans enforceable; Bali kavling SHM nominee structures criminal from 2026; BR condominium convenção bans STJ-affirmed. The deed-holder may own the unit but **not own the right to STR-let it**.
5. **Tourist taxes are often pass-through but ADR-suppressive** — Paris taxe de séjour 2026 = 5% pre-tax/n/pp capped €15.93 + 200% Île-de-France surcharge (Paris); Lisbon TMT €4/pp/n cap 7n; AMS 12.5% per room; Berlin City Tax 5%; Rome €5-10/n by class; Athens Climate Resilience Levy STR €8 high / €2 low season; Bali IDR 150k/foreign-visitor; Cape Town VAT 15% + TOMSA 1%. Even when guest pays, the all-in price ceiling suppresses ADR by an equivalent amount.
6. **Aggregator occupancy figures disagree by 10-20 pp** — AirDNA / Airbtics / AirROI / Inside Airbnb publish different numbers for the same city using different sampling + listed-vs-unlisted definitions. Paris 2024-2025: AirDNA 66% vs Airbtics 78%. London: AirDNA 57% vs Airbtics 74% vs AirROI 43.7%. Use ranges; do not anchor on a point estimate. Cross-check 2 sources minimum.
7. **2024-2026 regulatory wave reshapes the curve fast** — Loi Le Meur (FR 19 Nov 2024); Italy CIN (1 Jan 2025); Athens AMA freeze (1 Jan 2025 → through 2026); BCN universal HUT expiry Oct 2028 (Collboni Jun 2024); Amsterdam 15-night cap 1 Apr 2026; VIC Short Stay Levy 7.5% 1 Jan 2025; Byron 60-day cap 23 Sep 2024; HCMC residential ban 1 Aug 2024 (Decision 26/2024); IN GST cut 22 Sep 2025; Kyoto hotel tax 9× hike 1 Mar 2026; Tokyo 3% from FY2027; KE 2% Airbnb levy Jun 2026; ZA Cape Town STR by-law Apr 2026 (proposed); IL VAT 17% → 18% Jan 2025; RW 3% Tourism Levy 1 Jul 2025; Seychelles small-property TESL exemption 1 Jan 2026; TR Law 7464 (1 Jan 2024) + unanimous consent rule; SC Hospitality Act 80% consent + 2024 amendment; HU Budapest VI Decree 26/2024 zero-day from 1 Jan 2026; SI 60-day apartment / 150-day single-dwelling cap from 2026-2027; EE Tallinn Vanalinn cap incoming. A 2023-vintage yield model is materially stale by 2026.

## Regional patterns

### Western Europe

**FR** — Loi Le Meur enacted 19 Nov 2024: 90-night primary-residence default (was 120); civil fine €15,000; **national registration mandatory by 20 May 2026**; co-ownership prohibition threshold lowered from unanimity to 2/3 (where bourgeois habitation clause exists); DPE F banned from rental 1 Jan 2028, E from 2034. Paris Q1 2026: ~€1M in fines, 150-person enforcement brigade, record €585,000 court fine (9e arrondissement SCI converting entire building). Paris taxe de séjour 2026: 5%/n/pp cap €15.93 + 200% Île-de-France surcharge. **All Paris intra-muros = zone tendue = de facto non-principal STR ban via compensation rule.** Band: 🔴 prosecution-active; 🟢 only if compliant primary-residence ≤90 nights. [Service Public](https://entreprendre.service-public.gouv.fr/actualites/A17929) · [56Paris Loi Le Meur](https://56paris.com/en/paris-short-term-rental-regulations-updates-on-the-le-meur-law).

**UK** — 90-night Greater London cap = s.25A Greater London Council (General Powers) Act 1973 as amended by s.44 Deregulation Act 2015; Airbnb auto-blocks since 2017. Business rates apply >140 nights available + 70 actually let (SBRR typically zeroes the bill if RV <£12k). STR insurance uplift 10-30% (NRLA confirmed — only Western EU country with primary trade-body figure). Westminster Article 4 directions exist for HMO but NOT STR-specific (gap Westminster wants to close). National STR registration proposed, not yet in force. [Deregulation Act 2015 s.46 notes](https://www.legislation.gov.uk/ukpga/2015/20/notes/division/5/46) · [GOV.UK business rates self-catering](https://www.gov.uk/introduction-to-business-rates/self-catering-and-holiday-let-accommodation).

**IE** — Major 2025-2026 reform: STR definition tightened to ≤21 nights (was 14); **all of Ireland is RPZ since 20 Jun 2025** → STR non-PPR requires planning permission citywide; PPR retains 90-day whole-home or unlimited room-rental. **Short Term Letting and Tourism Act 2025** + EU Reg 2024/1028: national STR register launches **20 May 2026** via Fáilte Ireland. Permanent National Rent Control Framework from 1 Mar 2026 — increases capped at min(CPI, 2%). Band: 🔴 non-PPR; 🟢 PPR within 90 nights. [Fáilte Ireland STLR](https://www.failteireland.ie/registration-and-grading/short-term-letting-register-(STLR).aspx) · [RDJ RPZ extension](https://www.rdj.ie/insights/rent-pressure-zones-to-be-extended-to-cover-the-entire-country-and-amendments-to-rent-regulation-set-to-be-introduced).

**NL** — Amsterdam toeristenbelasting **12.5% per room** (~€22/n on €176 avg); vakantieverhuur cap **30 nights/yr** + permit €73.30; **from 1 Apr 2026: 15-night cap in 8 stress neighborhoods** (7 Centrum stadsdelen + Oude Pijp). VvE consent often binding independent of municipal cap. Rotterdam 60d; Den Haag 30d. Band: 🔴 Amsterdam stress zones from Apr 2026. [Amsterdam toeristenbelasting](https://www.amsterdam.nl/en/municipal-taxes/tourist-tax/) · [NL Times 15-night cut](https://nltimes.nl/2025/12/19/amsterdam-cut-legal-vacation-rentals-15-nights-eight-neighborhoods).

**BE** — Brussels Ordonnance 8 May 2014: registration number required for any paid rental ≤90 consecutive days; fines €250-€25,000 + cessation order + premises sealing power. **0% of 5,593 listings have STR licence** (Airbtics audit) — enforcement gap, but high audit-asymmetry risk. Tourist tax ~€4.24/room/n (raised 2024). Band: 🟡 statute strict, enforcement loose. [Ordonnance 8 May 2014](https://etaamb.openjustice.be/fr/ordonnance-du-08-mai-2014_n2014031471.html).

**DE** — Berlin Zweckentfremdungsverbot: primary residence ≤90 days without permit (registration number required + visible in listing); fines up to **€500,000**, average ~€6,000; one district issued 717 penalty notices = €3.1M. **Milieuschutzgebiete STR ban** proposed — would affect ~1.2M residents; **status: not yet in force**. Berlin City Tax 5% (business travel exempt). Band: 🟠 baseline; 🔴 expected in Milieuschutz if enacted. [nuBerlin Zweckentfremdung](https://www.nuberlin.com/info/berlin-airbnb-law-zweckentfremdungsverbot/).

**AT** — Vienna Bauordnung § 119(2a) effective **1 Jul 2024**: outside Wohnzonen 90 nights/yr default; inside Wohnzonen Ausnahmebewilligung permit required + 80% residential floor-area rule. Fines up to €50,000 even for advertising >90 days online. **Ortstaxe 3.2% → 5% from 1 Jul 2026**. Band: 🔴 inside Wohnzonen without permit; 🟠 outside. [wien.gv.at Merkblatt PDF](https://www.wien.gv.at/pdf/ma37/merkblatt-verwendung-wohnungen-kurzzeitvermietung.pdf).

**CH** — Geneva max 90 nights/yr before commercial reclassification; Geneva taxe de séjour CHF 4.25/pp/n (CHF 2.50 camping). Zurich 90 days/yr in residential zones from 1 Jan 2024; Nov 2024 tightening referendum **rejected**. Lex Koller proposed amendment Apr 2026 to restrict foreign commercial RE acquisition. **0% of 2,002 Zurich listings hold STR licences** (Jul 2025 audit). Band: 🟠 cantonal cap. [ge.ch taxe de séjour](https://www.ge.ch/taxes-touristiques/taxe-sejour) · [propertyowner.ch Swiss STR](https://www.propertyowner.ch/en/airbnb-under-pressure-how-swiss-cities-and-regions-regulate-short-term-rentals/).

**LU** — Fiches d'hébergement digital mandatory under Law 28 Feb 2025 eff **1 Sep 2025** via Lux Héberge platform; commune prior declaration to mayor required; no hard day cap. Band: 🟡 admin burden, no cap. [guichet.public.lu](https://guichet.public.lu/en/citoyens/fiscalite/immobilier/location/bien-immobilier-meuble-location-temporaire.html).

### Southern Europe

**ES** — Airbnb host-only 15.5% + Spanish VAT 21% on the fee. BCN PEUAT Zone 1 (Ciutat Vella) full freeze; **all 10,101 HUT licences citywide expire Oct 2028** (Collboni decree Jun 2024). Catalonia IEET from 1 May 2025: €7.40/n 1-4★ apartments + Catalonia €4 surcharge rising €1/yr to €8 by 2029. Madrid: no municipal tourist tax currently; PEH 2018 Distrito Centro requires independent entrance + portal/lift separation from residents → de facto STR ban in shared-building residential. National Ventanilla Única / VUD ID required from 2025. Band: 🟠 BCN Zone 2 (time-decay 2028); 🔴 BCN Zone 1 + MAD Centro. [Ajuntament Barcelona PEUAT](https://ajuntament.barcelona.cat/pla-allotjaments-turistics/en) · [Generalitat IEET](https://atc.gencat.cat/web/.content/atc_tributs/ieet/documents/IEET-info-rates-en.pdf) · [Madrid PEH](https://www.madrid.es/portales/munimadrid/es/Inicio/Actualidad/Noticias/Aprobado-el-Plan-Especial-para-la-regulacion-de-los-alojamientos-turisticos).

**PT** — Decree-Law 76/2024 eff 1 Nov 2024 repealed Mais Habitação freeze + 5-yr renewal; max 27 guests/9 rooms/unit; municipalities retain "áreas de contenção" power. Lisbon TMT raised to €4/pp/n (Sept 2024), cap 7 nights. Porto TMT €3/pp/n. **Lisbon Santa Maria Maior 68.8% AL ratio = absolute containment**; Bairro Alto / Madragoa also absolute; Misericórdia / Príncipe Real / Graça / Bica relative containment (2.5-5% ratio). **Sale-triggered expiry**: in containment zones, selling an apartment-mode AL = automatic licence death. Porto Vitória 60.5% / São Nicolau 48.3% / Sé 44.1% / Santo Ildefonso 38.3% containment; **Cedofeita 9.8% → sustainable-growth (new AL permitted)**. Band: 🔴 Lisbon containment + sale-trigger; 🟢 Porto Cedofeita; 🟡-🟠 Algarve Albufeira/Lagos. [Renascença Lisbon AL](https://rr.pt/fotoreportagem/pais/2024/07/02/lisboa-fechou-o-centro-ao-alojamento-local-mas-deixou-a-porta-aberta-a-41-novos-hoteis/383878/) · [DN Porto Cedofeita freed](https://www.dn.pt/local-geral/porto-retoma-regulamento-do-alojamento-local-e-liberta-bonfim-e-cedofeita).

**IT** — National **CIN (Codice Identificativo Nazionale)** portal opened 1 Sep 2024, mandatory display from **1 Jan 2025**; fines €800-€8,000 no CIN + €500-€5,000 non-display. **Florence centro storico Oct 2023 ban OVERTURNED by TAR Toscana** (lapsed; appeals dismissed; new ordinance under preparation but not in force at 2026-05). Rome contributo di soggiorno €3-10/n by class first 10 nights. Venice Contributo di Accesso €5 day-tripper (€10 within 3 days), 2026 dates 3 Apr–26 Jul Fri-Sun + special weeks. **Milan 2026 Olympics**: tourist tax spike €9.50/n within 30km of venues, 2026 only. Band: 🟢 Rome CIN-compliant; 🟡 Florence (restoration risk); 🟠 Venice (moratorium pressure). [Ministero Turismo CIN](https://bdsr.ministeroturismo.gov.it/) · [Il Sole 24 Ore TAR](https://en.ilsole24ore.com/art/short-rents-tuscany-tar-ban-florence-no-longer-valid-AFwKFYiC) · [Venice CdA](https://cda.ve.it/en/).

**GR** — **Climate Resilience Levy** since 2024, raised 1 Jan 2025: STR €8/n high season (Apr-Oct) / €2 low; villas €8 (<80m²) or €15 (≥80m²) high / €2 / €4 low. AADE Property Number mandatory; STR national standards (safety + fire + civil liability) eff **1 Oct 2025**. **Athens 1st/2nd/3rd Municipal Districts AMA freeze 1 Jan 2025 — extended through 2026** (~8% AMA drop, 29,500 → 27,000 central). Cyclades **20-30% bed-cap proposal** under consultation; ministerial decision expected by 30 Jun 2026. Santorini/Mykonos new building restrictions from Nov 2025. Band: 🔴 Athens central; 🔴-pending Cyclades. [AADE STR](https://www.aade.gr/en/short-term-rental) · [ShortTermRentalz Athens freeze](https://shorttermrentalz.com/news/athens-new-str-licences-ban-2025/) · [ProtoThema 30% Cyclades](https://en.protothema.gr/2026/04/07/30-cut-to-tourist-beds-in-the-cyclades-clampdown-on-airbnb-as-well/).

**CY** — Law 9(I)/2020 amending 34(I)/2019: 3-year self-catering licence required from Deputy Ministry of Tourism; fines up to €5,000 + 1yr prison; registration number must display. VAT 9% reduced for short-term accommodation (vs 19% standard); €15,600 registration threshold. **No district-level moratoria**; **no national tourist tax currently in force** (€2.50/n proposal not enacted). 2025 enforcement crackdown intensified. Band: 🟢 clean regulatory map. [gov.cy registration](https://www.gov.cy/tourism/en/mi-katigoriopoiimeno/registration-of-self-service-accommodations-in-the-registry-of-the-deputy-ministry-of-tourism/).

**MT** — Holiday Furnished Premises Licence under Travel and Tourism Services Act Cap. 409; **Eco-contribution tripled to €1.50/pp/n in 2025** (was €0.50), age ≥18, cap on stay applies (re-verify post-2025 hike at mtca.gov.mt). VAT 7% reduced on hotel/HFP accommodation. **No zone-level moratoria.** Valletta UNESCO core: HFP issuance subject to MTA technical inspection (fire egress / room sizes / sanitary). Yield compression structural, not regulatory (Sliema 2.2-3% gross; Valletta 1.15-2.46%). Band: 🔴 yield (not regulation). [MTA HFP](https://mta.com.mt/application-for-a-holiday-furnished-premises-licence/) · [MTCA ECO](https://mtca.gov.mt/business-tax/eco/eco-on-accommodation).

### Eastern Europe + Balkans + Baltics

**PL** — No national STR day cap; no Warsaw tourist tax (opłata miejscowa only in Zakopane/Gdańsk-coast/Kraków-Swoszowice); enforcement near-zero (0/10,276 Warsaw + 0/7,280 Kraków listings licensed). EU Reg 2024/1028 listing-ID required May 2026. Band: 🟡 light enforcement, EU sweep incoming. [Lodge Compliance PL](https://www.lodgecompliance.com/countries/poland).

**CZ** — Prague poplatek za pobyt **CZK 50/n** (nights 1-10), CZK 25/n (11-60); proposal to double cap to CZK 100/n early 2025 not enacted. Prague 1 pushing Hotel Act amendment; not enacted. Band: 🟡 regulation in flight. [Prague.org tax guide](https://prague.org/prague-city-tax-guide/).

**SK** — Bratislava daň za ubytovanie €3.50/n Staré Mesto, €3.00/n other districts (VZN 4/2023 eff 1 Jul 2023); cap 60 nights/yr/guest. No STR cap. Band: 🟢 light-touch. [bratislava.sk](https://bratislava.sk/en/city-of-bratislava/taxes-and-levies/tourist-tax).

**HU** — Budapest **District VI (Terézváros)**: referendum 2-15 Sep 2024 (20.52% turnout, 54% in favor); **Decree 26/2024 (X.31) → STR allowable days/yr = ZERO from 1 Jan 2026**, upheld by Hungarian Supreme Court. District VII (Erzsébetváros): Sep 2025 regulation caps new commercial accommodations at **10% of any residential building's floor area** (different mechanism). Two-year national moratorium on new STR registrations announced 2025. Airbnb flat tax per room **quadrupled 2024**. IFA 4% Budapest tourist tax. Band: 🔴 District VI (zero-day live 1 Jan 2026); 🟠 District VII. [terezvaros.hu](https://szavazz.terezvaros.hu/en) · [hungarytoday.hu Supreme Court](https://hungarytoday.hu/supreme-court-upholds-budapest-districts-ban-on-short-term-rentals/).

**RO** — No federal STR cap; mandatory ANT structură de cazare turistică classification; ANAF crackdown identified 22,000+ unreported hosts 2023-2024. Bucharest sector-level tax variance. 10% flat PIT. Band: 🟢 yield; 🟡 tax-enforcement risk. [Airbnb RO Tax Guide 2025](https://assets.airbnb.com/help/Airbnb_TaxGuide2025_Romania_ENGLISH.pdf).

**BG** — Sofia turisticheski danak BGN 0.20-3.00/n band; 2024-2025 proposal to ~triple rates not enacted. No zone cap. Band: 🟢-🟡. [MOF BG](https://www.minfin.bg/en/781).

**HR** — 2024 amendment to Zakon o ugostiteljskoj djelatnosti (eff 1 Jan 2025): **66% co-owner consent for new STR registration** + **80% retention threshold within 5 years** (two distinct provisions — sources reconcile both apply at different stages; verify at Narodne novine). **180-day cap** for non-professional landlords. Tourist tax €1.00-€2.20/n by zone+season. **Dubrovnik Stari Grad moratorium on new registrations 2023, extended through 2025** = 🔴 new entries blocked. Hvar/Split UNESCO cores no documented moratorium but premium pricing without zone-protection. Band: 🔴 Dubrovnik; 🟠 Split; 🟢 Zagreb. [gov.hr](https://gov.hr/en/tourist-tax/1520) · [bne IntelliNews HR](https://www.intellinews.com/croatia-moves-to-restrict-airbnbs-to-address-housing-crisis-340368/).

**SI** — Tourist tax + promo fee Ljubljana €2.50 + 25% = €3.13/n. **2024 STR law (phased 2026-2027)**: **150-day/yr cap single/two-unit dwellings + 60-day/yr cap apartments in multi-unit buildings** (municipalities flex 30-90 multi or 30-180 single). Ljubljana confirmed 60-day scope from 2027. Band: 🔴 Ljubljana from 2027 STR-centric. [sloveniatimes.com](https://sloveniatimes.com/44213/law-targets-overtourism-and-housing-crunch-with-rental-caps).

**BA / ME / RS / MK** — Sarajevo BAM 2/n; Kotor/Budva/Tivat €1/n; Belgrade RSD 130-160/n; Skopje not publicly available — all light-touch regimes, no zone-cap. Band: 🟢-🟡 across the bloc.

**AL** — **DIVA digital tax platform mandatory 1 Jan 2026**; 15% flat STR tax, annual deadline 31 Mar; no NIPT required. Band: 🟡 formalization 2026 (tightens net yield). [HLB Albania](https://www.hlb.al/short-term-rentals-in-albania-new-tax-reporting-obligations-from-2026/).

**EE** — Mandatory STR registration since **Jul 2025** (EU Reg 2024/1028 alignment); 22% income tax; Tallinn accommodation licence + Vanalinn (Old Town) cap **incoming** (announced, mechanism not finalized). Band: 🟠 Vanalinn pending; 🟡 elsewhere. [Cobalt Legal 2025](https://www.cobalt.legal/news-cases/key-amendments-in-estonian-tax-legislation-in-2025/).

**LV** — Riga tourist tax €1/n cap €10 (10 nights) eff Jan 2023; no zone cap; STR national framework in progress. **Riga Vecrīga 7.95-9.81% gross yield** (highest in Baltics). Band: 🟢 light regime. [riga.lv](https://www.riga.lv/en/article/riga-introducing-tourist-charge-next-year).

**LT** — Vilnius tourist tax **€2/n eff 1 Jan 2024** (raised from €1); no zone cap; uniform citywide. Band: 🟢. [govilnius.lt](https://www.govilnius.lt/plan-your-trip/city-tax).

### Americas

**US** — Airbnb host-only 15.5% national; Vacasa 25-35% (effective 40%+ with add-ons). **NYC LL18 (Local Law 18 of 2022)**: Final Rules eff **6 Mar 2023**; platform enforcement began **5 Sep 2023**. Host-present + registration required for <30-day stays → listings ↓83% citywide, outer boroughs ↓~92%. SF 90-day unhosted cap. LA HSO 120-day cap primary residence only. Santa Monica <30d hosted-only. **Miami Beach STR ban**: Aug 2025 Miami-Dade court (Hanzman J.) **struck the ordinance** as conflicting with state law — enforcement status uncertain pending appeal. **Honolulu Bill 41 (CO 22-7)**: signed 26 Apr 2022, eff 23 Oct 2022 (90+ days outside resort zones); **2023 court partially reversed to 30 days** in non-resort. Band: 🔴 NYC + LA + SF for non-resident foreign buyer. [NYC OSE Registration](https://www.nyc.gov/site/specialenforcement/registration-law/registration.page) · [Haber Law Miami Beach](https://www.haber.law/short-term-rentals-ruled-illegal-in-miami-beach-now-what/).

**CA** — Toronto principal-residence rule citywide + $375 annual registration (from 1 Jan 2025) + entire-home 180-night cap. **BC Short-Term Rental Accommodations Act eff 1 May 2024**: principal residence + secondary suite/laneway only; provincial registry mandatory 2 Jun 2025; municipal licence 1 Oct 2024. Montréal CITQ mandatory + $2M liability insurance proof; compliance jumped 58% → 90% Jan-Feb 2024. Band: 🔴 non-resident foreign buyer (principal-residence rule blocks). [Toronto STR](https://www.toronto.ca/community-people/housing-shelter/rental-housing-rights-information/short-term-rentals/short-term-rental-operators-hosts/) · [BC May 2024 rules](https://news.gov.bc.ca/releases/2024HOUS0020-000590) · [CITQ legal provisions](https://citq.qc.ca/en/enregistrement_dispositionslegislatives.php).

**MX** — **CDMX Tourism Law Reform** published Gaceta Oficial **4 Apr 2024** (NOT "2022"); implementing reglamento 25 Sep 2024 + further reforms 3 Oct 2024. **50% annual occupancy cap on STR units registered via digital platforms** — loss of registration if exceeded. Host + platform registries mandatory. Social-housing + post-2017 quake reconstruction prohibited from STR. Q-Roo ISH 5% traditional + **6% via digital platforms** (eff 2025) + VISITAX $5 USD/visitor. Band: 🟠 CDMX (50% cap nullifies most STR upside); 🟡 Q-Roo. [CCN-Law CDMX summary](https://ccn-law.com/en/mexico-enacts-amendments-to-mexico-citys-tourism-law-and-rules-for-private-lodging-accommodations/) · [Q-Roo ISH Law](https://satq.qroo.gob.mx/contenidos/dmarcolegal/53f80d58-d367-11ef-b142-005056a29996).

**BR** — Airbnb host fee **16% (above 15.5% global)**. ISS 2-5% by municipality; Salvador / Petrópolis / Olímpia / Ponta Grossa approved on STR; São Paulo / Rio / Florianópolis pending. **Tax reform 2026+**: IBS/CBS phase-in; from 2027, IBS applies to individuals with **>3 properties + >R$240k/yr rental** — combined effective tax up to **44.3%**. Condominium convenção is de-facto regulator; STJ rulings favor condo prohibitions. Band: 🟡 single-property; 🟠 multi-property professional post-2027. [Domingues e Pinho tax reform](https://www.dpc.com.br/tax-reform-what-changes-for-individuals-in-the-rent-and-sale-of-real-estate/?lang=en).

**AR** — CABA Ley 6255 + **Resolución 8/ENTUR/2025 (Feb 2025)**: new 180-day owner-registration deadline from 3 Feb 2025; mandatory registration number on all listings; DUU (Derecho de Uso Urbano) per Ley 6278 — foreign tourists >12y pay ~US$1.50/n. Band: 🟢 yield mechanics; 🟡 FX/capital-controls overlay. [CEDOM Ley 6255](https://www.cedom.gob.ar/legislacion/normas/leyes/RepoLeyes/ley6255.html) · [Boletín Oficial CABA Res. 8/2025](https://boletinoficial.buenosaires.gob.ar/normativaba/norma/501695).

**UY** — Punta del Este high seasonality (Jan-Feb); IVA 22% on STR services; MINTUR Receptive Operator status applies to Maldonado. Band: 🟡 concentration risk.

**CL** — IVA 19% on furnished STR but **foreign-tourist exemption** (Art. 12 letra E n°17 LIVS) when guest is non-resident + foreign-currency-denominated + SII-registered. Las Condes / Providencia / Vitacura commune-level rules tightening 2024-2026 (not centrally indexed). Band: 🟢 foreign-tourist-mix portfolio. [SII Chile FAQ](https://www.sii.cl/preguntas_frecuentes/iva/001_030_0776.htm).

**CO** — RNT mandatory; ANAF-equivalent crackdown on unlicensed (>1,700 Medellín units identified 2024). **Bogotá "Decreto 538/2024" 10% STR tax + Medellín "Acuerdo 056/2024" El Poblado restrictions: SPECIFIC ORDINANCE NUMBERS UNVERIFIED in primary search** — verify at alcaldiabogota.gov.co/sisjur and concejodemedellin.gov.co before relying. Band: 🟡 yield real, compliance + condo-veto risk high.

**PE** — Lima IGV 18%; Miraflores/Barranco condo bans common; <1% listings hold licences (low enforcement). Band: 🟡.

**EC** — Reglamento de Alojamiento Turístico en Inmuebles Habitacionales published **21 Sep 2023**; MINTUR registration via SITURIN mandatory; IVA raised to 15% (from 12% in 2024). Band: 🟡. [MINTUR Reglamento](https://www.turismo.gob.ec/ecuador-ya-cuenta-con-un-nuevo-reglamento-para-los-alojamientos-turisticos-en-inmuebles-habitacionales/).

**PA** — **National 45-day minimum rental rule** Panama City **except in designated tourism zones (Casco Viejo + parts of Santa Ana)**. ATP RNT + MIVIOT zoning certificate required. Band: 🟢 Casco Viejo; 🔴 elsewhere Panama City.

**CR** — **13% IVA on STR <30 days**; mandatory ICT registration + Hacienda electronic invoicing (NITE); annual income >₡1M (~$1,800) triggers compliance. **Platforms data-share with Hacienda from 2026**. Band: 🟢 with full compliance. [Airbnb CR Tax Guide 2024](https://assets.airbnb.com/help/AirbnbTaxGuide2024_Costa_Rica_ENGLISH.pdf).

**DO** — **NO national STR statute as of May 2026**; MITUR + Asonahores draft framework under finalization (Apr 2025 reporting); condo bylaws under Ley 5038 are de-facto regulator. ITBIS 18% on STR. (NOTE: DO = Dominican Republic; distinct from DM = Dominica, out of scope.) Band: 🟡 condo-dependent. [Dominican Today MITUR/Asonahores](https://dominicantoday.com/dr/local/2025/04/25/mitur-and-asonahores-finalize-airbnb-regulation-framework/).

**JM** — TPDCo licensing voluntary but de-facto required for villa-scale (3-4 weeks processing); GCT 15% + GART $10/n villas 1-4 rooms / $20 5-20 / $30 >20. Band: 🟡.

**BS** — VAT **10% since 2022** (not 12% as some references cite); DIR Vacation Rental Registration mandatory since Apr 2023. Band: 🟡.

**BB** — **2.5% Room Rate Levy + 10% Shared Economy Levy** (NOT 8.75% as some references cite); BRA registration mandatory. Band: 🟡. [BRA tourism levies](https://bra.gov.bb/News/Press-Releases/Tourism-Sector-Reminded-to-File-an).

### Asia + Oceania

**JP** — **Minpaku Law (Act on Private Lodging Business, Act 65 of 2017)** eff 15 Jun 2018: **180-night/yr cap** nationwide (FY = noon 1 Apr to noon 1 Apr). Hotel tax overhaul 2025-2027: Osaka tiered shift 1 Sep 2025 (¥200/¥400/¥500 by ADR); Kyoto **9× hike from 1 Mar 2026** (top tier ¥10,000); Tokyo **3% from FY2027** (announced 2025-11-27, replacing tiered ¥100-200). Shibuya/Shinjuku/Minato/Kyoto: weekend/holiday-only in Category 1 & 2 low-rise residential. **Osaka Tokku Minpaku Zone** (Minato/Nishi/Chuo wards): 2-night minimum, **no 180-day cap** (separate regime). Band: 🟡 outside Tokku; 🟠 inside residential ward weekend-only zones. [mlit.go.jp Minpaku law](https://www.mlit.go.jp/kankocho/minpaku/overview/minpaku/law1_en.html) · [japantimes.co.jp Tokyo 3%](https://www.japantimes.co.jp/news/2025/11/27/japan/accommodation-tax-fixed-rate-tokyo/) · [nippon.com Kyoto hike](https://www.nippon.com/en/japan-data/h02298/kyoto-targets-big-spenders-with-lodging-tax-hike).

**KR** — Urban Homestay Business for Foreign Tourists (외국인관광도시민박업): owner-occupied + **foreign-guests-only** + max 230 m²; Hanokstay both nationalities. **All KR listings must submit gov-verified business licence by 16 Oct 2025**; un-verified blocked. Band: 🟠 foreigners-only structurally restrictive. [airbnb.com/help/article/1387](https://www.airbnb.com/help/article/1387).

**CN** — **Airbnb domestic suspended 30 Jul 2022**; foreign buyer 1-yr residency required; PSB 24h guest registration. STR-as-investment thesis structurally weak. Band: 🔴 skip.

**HK** — **<28 consecutive days = illegal** without Hotel & Guesthouse licence under **Cap. 349 Hotel and Guesthouse Accommodation Ordinance**; fine up to **HK$200,000 + 2 years imprisonment**. Hotel Accommodation Tax suspended 1 Jul 2008. ≥28-day "serviced apartment" path legal. Band: 🔴 <28d; 🟡 ≥28d serviced. [elegislation.gov.hk Cap 349](https://www.elegislation.gov.hk/hk/cap349).

**TW** — 民宿管理辦法 Homestay Management Regulation: operator-occupied + designated rural/cultural-tourism zones only + max 15 rooms (8 urban-fringe). Taipei Da'an/Xinyi/Zhongshan residential STR effectively illegal. ~90% Taipei listings illegal. Band: 🔴 urban residential.

**SG** — **Minimum 3 consecutive months private / 6 months HDB** (URA rule, revised down from 6mo Jun 2017) citywide — STR home-sharing structurally banned. GST 9%. Band: 🟠 (3mo serviced-let only). [ura.gov.sg](https://www.ura.gov.sg/Corporate/Property/Residential/Short-Term-Accommodation).

**MY** — Tourism Tax **RM 10/room/n** foreign-tourist-only; SST 8% on accommodation (from 1 Mar 2024). Penang Island STR ban 2020 strata-residential (commercial-titled only). **2025 Court of Appeal *Wawasan Raya Sdn Bhd v MARC Service Residence MC*** clarified MC powers — STR-prohibitive private covenants enforceable under specific tests. Band: 🟡 KL strata where MC permits; 🔴 Penang Island residential strata. [rdslawpartners.com 2025 ruling](https://www.rdslawpartners.com/post/court-of-appeal-s-ruling-brings-long-awaited-clarity-to-malaysia-s-short-term-rental-debate).

**ID** — **Bali Provincial Levy IDR 150,000/foreign visitor** eff 14 Feb 2024 (Perda 6/2023). Foreigners cannot hold Pondok Wisata licence — restricted to Indonesian citizens (Permenpar 18/2016); compliant path = PT PMA + Villa licence (KBLI 55193). **Bali Perda 4/2026 criminalises nominee structures** (up to 5yr prison + IDR 1bn fine); OTA platforms must verify NIB by **Mar 2026 deadline**. Band: 🟡 PT PMA-compliant; 🔴 nominee path post-2026. [balipropertyrules.com](https://balipropertyrules.com/guides/bali-villa-licensing-foreigners/).

**TH** — Hotel Act B.E. 2547 (2004) **§4**: accommodation <30 days requires Hotel Licence; penalty **THB 20,000 fine + 1yr imprisonment**. Bangkok/Phuket enforcement intensifying 2023-2026. Condo juristic-management increasingly banning <30d. Band: 🟡 where juristic permits + hotel-licence-aware; 🔴 unlicensed <30d. [samuiforsale.com Hotel Act](https://www.samuiforsale.com/law-texts/thailand-hotel-act-2004-translation.html).

**VN** — **HCMC residential STR ban via Decision 26/2024/QD-UBND eff 1 Aug 2024** (interpreting 2023 Housing Law) — only mixed-use condotels permitted. Hanoi: no specific STR regulation as of 2026; business registration with DoF still required. Band: 🔴 HCMC residential; 🟡 condotel.

**PH** — DOT accreditation mandatory; Boracay carrying capacity capped 19,215 persons; DOT-Accredited Establishments with CAO. Condo-corp by-laws variably restrict Manila/Makati/BGC. Band: 🟡 where corp permits.

**IN** — GST cut **22 Sep 2025**: **5% (no ITC) for rooms ≤₹7,500/n; 18% (with ITC) for >₹7,500/n** (was 12%/18%). Society/AOA by-laws can restrict in cooperative housing (esp. Maharashtra/Karnataka/Goa). Goa Tourism Dept registration + CRZ restrictions. Band: 🟡. [cleartax.in GST hospitality](https://cleartax.in/s/impact-of-gst-hospitality-industry).

**LK** — Tourism Development Levy 1% (or 0.5% if turnover ≤LKR 12M/yr) under Finance Act 25 of 2003; SLTDA registration mandatory. Galle Fort UNESCO heritage stack adds friction. Band: 🟡. [sltda.gov.lk TDL](https://sltda.gov.lk/en/tourism-development-levy--notices).

**AU** — **VIC Short Stay Levy 7.5%** of total booking fee eff **1 Jan 2025** (stays <28 days; principal residence + hotels exempt); 25% to regional. **NSW STRA Code**: register $65; Greater Sydney 180-day non-hosted cap (Eastern Harbour/Central River/Western Parkland); fines up to **$1.1M (corp) / $220k (individual)**. **Byron Shire 60-day non-hosted cap eff 23 Sep 2024**. Band: 🟠 Sydney non-hosted; 🟢 hosted; 🔴 Byron non-hosted. [sro.vic.gov.au short-stay-levy](https://www.sro.vic.gov.au/owning-property/short-stay-levy) · [planning.nsw.gov.au STRA](https://www.planning.nsw.gov.au/policy-and-legislation/housing/short-term-rental-accommodation).

**NZ** — **Marketplace GST 15% collected by Airbnb/Bachcare from 1 Apr 2024** (8.5% flat-rate credit for non-registered hosts); Auckland APTR commercial-rated uplift for STR >28 nights/yr (validated by Supreme Court 2022). **Queenstown Lakes 90 nights/yr whole-house cap** without resource consent + 25% rates uplift on registered. Band: 🟡 Auckland; 🟠 Queenstown. [findex.co.nz NZ app-tax](https://www.findex.co.nz/insights/article/app-tax-and-gst-changes-for-short-term-rentals) · [qldc.govt.nz STR factsheet](https://www.qldc.govt.nz/media/zithkrtz/qldc_short-term-visitor-accommodation_factsheet_mar24-v2.pdf).

**FJ** — VAT 15% (raised from 9% 2023); ECAL 5% turnover (reduced from 10%, threshold FJD 3M); STT 6% suspended/varied; foreign-buyer freehold ban <1 acre town residential — leasehold or commercial-zoned only. Band: 🟡 Denarau leasehold.

### MENA + Africa

**AE** — Dubai DTCM **officially renamed DET (Dubai Economy and Tourism)**. Holiday Home Operator Permit mandatory since 2017: AED 1,520 reg + 320 inspection + AED 370-1,270 annual unit permit. **Tourism Dirham AED 10/n standard / AED 15/n deluxe per bedroom, first 30 nights**. **Abu Dhabi tourism fee 6%** (per 2025 DCT circulars; supersedes older 3.5% + AED 15/n line; verify); DCT short-let licence renewal AED 900/yr; **Circular 8/2025 (Oct 2025)** strengthened compliance. VAT 5% if registered. Band: 🟢 Dubai compliant; r/dubairealestate "long-let yields similar to short-let now" — Bayut H1 2025 confirms long-let tightened (8% YoY rent growth). [DET holiday home](https://www.dubaidet.gov.ae/en/our-services/for-consumers-and-students/issue-a-new-holiday-homes-permit) · [DCT circulars](https://dct.gov.ae/en/media.centre/circulars.aspx).

**SA** — MT tourism-accommodation licence via my.gov.sa; **Mabaat** is the MT-licensed STR platform (NOT "Tarseen" — Tarseen reference not verified; likely conflation with Mabaat or Ejar); VAT 15%; ~50% of SA Airbnb listings licensed (Lodge Compliance audit). Riyadh 5-year rent freeze 2025. Band: 🟡 maturing.

**OM** — MHT permit mandatory; new tourism law 2025 stricter standards; Savills/Visit Oman/Hospiria partnership Dec 2025 (formalization signal). VAT 5%. Band: 🟡. [mht.gov.om](https://mht.gov.om/).

**BH** — **Tourist Levy BHD 3 per room per day eff 1 May 2024** (supersedes prior BD 0.5/n). VAT 10% since 2022. No comprehensive STR framework. Band: 🟠 regulation gap. [KPMG BH GCC Tax News May 2024](https://assets.kpmg.com/content/dam/kpmg/bh/pdf/2024/05/kpmg-bahrain-gcc-tax-news-05052024.pdf).

**QA** — QT Holiday Homes Licence (5-yr) mandatory; Circular 12/2022 framework; hotel-sector 10% tourism tax per PWC (STR applicability — verify with QT directly). VAT not yet implemented. Band: 🟡. [QT Holiday Homes](https://www.qatartourism.com/en/licensing-e-services/e-services/holiday-homes).

**KW / JO** — Regulation gaps; no documented STR licensing regime comparable to GCC peers. Band: 🟠 — classify as "no significant foreign-buyer STR market" unless specific buyer thesis.

**IL** — **VAT 18% from Jan 2025** (raised from 17%); ITA treats Airbnb income as **business income** (no 10% linear or passive-rental exemption); ITA running snap audits in TLV/Jerusalem/Haifa/Eilat. 0% of TLV listings have STR licence; 90-night/yr cap *considered* not enacted. Eilat zero-VAT zone (verify current status). Post-7-Oct-2023 ADR depressed 2024 H1, recovered 2025. Band: 🟡 enforcement-risk rising. [CPA-Dray ITA STR](https://www.cpa-dray.com/en/blog/short-term-rentals-airbnb-israeli-taxation/).

**EG** — VAT 14% + **Tourism Support Fund 1% (or EGP 5-50/n)** since Mar 2023 + Service 12% ~ 26% guest-side stack. Minimum 5★ USD 40 / 4★ USD 28 nightly (Nov 2021). Sharm El-Sheikh ~1% city tax. Band: 🟡.

**TR** — **Law 7464 ("Konut Hizmetleri Kanunu")** enacted 25 Oct 2023, gazette 2 Nov 2023, **in force 1 Jan 2024**: 100-day max stay per booking = STR threshold; national permit via Ministry of Culture & Tourism e-Devlet; **unanimous written consent from all condominium co-owners required**; fines **TRY 100,000-1M**; post-31-Dec-2024 transition closed. Konaklama Vergisi 2% since Jan 2023. VAT (KDV) 10% reduced accommodation / 20% standard. Band: 🔴 unanimous-consent structural barrier in apartment blocks. [Mondaq Law 7464](https://www.mondaq.com/turkey/data-protection/1422698/understanding-t%C3%BCrkiyes-new-law-on-short-term-residential-rentals-for-tourism-law-no-7464).

**MA** — **Standards 2.0** classification rollout 2025; riad inspection MAD 1,200. TPT per-night per-star (MAD 7-30/n by classification — verify ONMT brackets). VAT 10% accommodation. 0% of Marrakech 9,648 listings have STR licence — enforcement still low. Management 10-15% short-let (yourhost.ma; Atrravel reference not verified). Band: 🟡 (tightening but enforcement low; price for 2027 step-up risk). [Styqr Standards 2.0](https://styqr.fr/en/2025/10/01/new-standards-for-tourist-accommodation-in-morocco-2025-welcome-to-standards-2-0/).

**TN** — **Taxe de séjour quadrupled 2024**: TND 4 (2★), 8 (3★), 12 (4-5★) per night, **eff 1 Nov 2024**; **explicitly extended to private residences rented for tourism**. Hotel turnover tax 1% → 3% (Finance Law 2024). VAT 7% reduced accommodation. Band: 🟡.

**ZA** — TOMSA Tourism Levy 1% voluntary; VAT 15%; **Tourism Amendment Bill 2019 SHELVED** (not pending as some references cite). Cape Town STR By-Law **proposed April 2026** (not enacted); body-corporate de-facto bans dominate Sea Point/Green Point/De Waterkant/CBD/Camps Bay/Clifton. 26,304 Cape Town active listings (Inside Airbnb 25 Jun 2025). Band: 🟠 Cape Town (April 2026 by-law inflight + body-corp binary). [Capetowner Apr 2026](https://capetowner.co.za/news/2026-04-20-new-regulations-for-short-term-rentals-in-cape-town-what-you-need-to-know/).

**KE** — **2% Tourism Levy extension to Airbnb/Booking.com from June 2026**; mandatory registration with **TRA (Tourism Regulatory Authority)** — NOT "NCITS"; Nairobi county permits + KEBS hospitality standards; VAT 16%. Band: 🟡 June 2026 inflection. [Business Daily Africa](https://www.businessdailyafrica.com/bd/economy/kenya-expands-2pc-tourism-levy-to-airbnb-booking-com-rentals-5339302).

**NG** — Lagos HORC Law 2009 5% consumption tax + Tourism Promotion Agency Law 2019; VAT 7.5% on hotel/short-stay; LASBCA STR business permit. ₦264.3bn 2024 Lagos market revenue, +200% YoY nightly rates. Band: 🟡 FX volatility + state-by-state patchwork.

**GH** — Tourism Levy 1% (L.I. 2185 / Tourism Regulations 2012); VAT + NHIL + GETfund + COVID-19 levy + GTA + EPA + 14 more line items. GTA shut-downs documented 2022. Band: 🟠 tax-stack complexity.

**RW** — **3% Tourism Levy in force 1 Jul 2025** — applies to hotels, motels, lodges, apartments, **Airbnb, camping sites**; registration deadline end-Jul 2025; first declaration 15 Aug 2025; monthly thereafter. VAT 18%. Band: 🟢 clean recent regime. [RRA notice](https://www.rra.gov.rw/en/details?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=2811&cHash=238f70126ddc5583e158c57fcd95edce).

**SN** — VAT 10% reduced tourism; LMNP-equivalent furnished rental possible; STR-specific licensing not documented. Band: 🟠 regulation gap.

**CV** — Tourist Tax €2/day visitors >16y cap 10 days; **20% flat non-resident rental withholding**; IUP 5-year waiver for tourism on Sal/Boa Vista/Maio; VAT 15%; SRSMC 4% for small companies. Band: 🟡 tax incentives strong + 20% WHT drag.

**SC** — **Tourism Environmental Sustainability Levy (TESL)** eff 1 Aug 2023: small (1-24 rooms) SCR 25/pp/n, medium SCR 75, large SCR 100 + yachts; **charged on invoice NOT advertised price**. **From 1 Jan 2026: small establishments (1-24 rooms) NO LONGER subject to levy** — yield-positive for foreign-owned villas. Band: 🟢. [Inside Seychelles changes](https://www.insideseychelles.com/changes-to-sustainability-levy/).

**MU** — Tourism Levy 2% of total accommodation bill (excl VAT) since 2013; VAT 15% (registration threshold MUR 6M); rental income tax 15% flat; holiday-rental <MUR 700k/yr fully exempt. IRS/RES/PDS schemes minimums USD 375k+. Band: 🟡 (lifestyle + residency play, modest yield).

## Universal mitigations

For foreign buyers, applicable across all 109 countries:

1. **Re-base the gross-yield headline** — pull marketed yield from a single named source (Idealista / SeLoger / Spitogatos / AirDNA / GPG / local portal) with date stamp; subtract each cost line transparently; produce a *single net yield range* not a point estimate. Cite the source publicly so buyer can verify.
2. **Test the day-cap binding constraint** — multiply cap × ADR × cap-window occupancy, not cap × ADR. Paris 90 nights at €162 ADR with 78% occupancy = 90 × 162 × 0.78 = €11,372, not €14,580. AMS 15-night cap from 1 Apr 2026 collapses to ~€2,640 in 8 stress zones.
3. **Verify licence transferability on resale** — Lisbon containment-zone apartment-mode AL dies on resale (non-transferable). BCN HUT licence expires Oct 2028 universal. Athens AMA freeze blocks new entrants. Get explicit confirmation from selling agent + cross-check with municipal portal before pricing licence into offer.
4. **Pull condo / strata / co-owner consent rules pre-offer** — TR Law 7464 unanimous consent, HR 66%/80%, MY 2025 *Wawasan* binding precedent, BR condominium convenção, BCN PEUAT, Lisbon area-de-contenção, Athens AMA, Bali Perda 4/2026 nominee criminalization. Deed-holding ≠ STR-letting rights.
5. **Cross-check 2 aggregator sources on occupancy** — AirDNA / Airbtics / AirROI / Inside Airbnb disagree 10-20 pp on the same city; use ranges. Verify if listed-only or scraped-inclusive sampling.
6. **Stress-test for pending moratoria** — Cyclades 30% bed-cap (ministerial decision due 30 Jun 2026), Cape Town STR By-Law (April 2026 proposal), Berlin Milieuschutz STR ban, Athens AMA freeze 2026+, Sydney STRA escalations, Westminster Article 4 STR-specific gap closure. Treat "proposed" as upside risk, not as ignored noise.
7. **Insurance uplift gap** — only UK has primary trade-body figure (10-30% NRLA). All other 102 countries: bind a quote from a named carrier pre-purchase. Standard landlord policy typically void for unhosted STR; STR-rider can be +30-100% over base.

## Confidence labels

- **HIGH**: Primary government / regulated entity source within 12 months; ordinance number cited; effective date verified; cost-line stack fully sourced. Applies to: FR, UK, IE, NL, DE, AT, CH, ES, PT, IT, GR, MT (mostly), JP, KR, HK, SG, AU, NZ, US, CA, MX (CDMX), TR, AE Dubai, MA (regs), ZA (regs), KE, RW, SC.
- **MEDIUM**: Cost-lines mostly sourced; ordinance present but specific number / sub-clause requires Narodne novine / Official Gazette / Boletín Oficial direct verification; aggregator data acceptable for occupancy bands. Applies to: HR, SI, BA, ME, RS, PL, CZ, SK, HU, RO, BG, EE, LV, LT, AL, BR, AR, UY, CL, EC, PA, CR, JM, BS, BB, MY, ID, TH, VN, PH, IN, LK, FJ, SA, OM, QA, EG, TN, NG, GH, CV, MU.
- **LOW**: STR licensing regime not documented in primary public source OR no significant foreign-buyer STR market — flagged with `data not publicly available — verify at <authority>`. Applies to: KW, JO, SN, MK, NP, BD, CN (skipped — Airbnb domestic suspended).
- **Verified-unverified**: 5 specific items flagged as `unverified` / `superseded` and require primary-source confirmation before relying:
  - CO **Bogotá Decreto 538/2024** (10% STR tax) — not retrievable; closest match Decreto 236/2024
  - CO **Medellín Acuerdo 056/2024** El Poblado — RNT enforcement real but specific acuerdo unverified
  - BS hotel guest tax — verified 10% VAT since 2022 (not 12%)
  - BB tourist levy — verified 2.5% Room Rate + 10% Shared Economy (not 8.75%)
  - SA "Tarseen" — replace with **Mabaat** (MT-licensed) or Ejar; KE "NCITS" → **TRA**; MA "Atrravel" → yourhost.ma/KNA

## Status

**Last refreshed**: 2026-05-11. **Next refresh**: per-event for highest-volatility (FR Loi Le Meur registration 20 May 2026 launch; AMS 15-night cap 1 Apr 2026 launch; HU Budapest VI zero-day 1 Jan 2026 launch; Cyclades bed-cap ministerial decision by 30 Jun 2026; Cape Town STR By-Law enactment; SC TESL 1 Jan 2026 small-property exemption; KE 2% levy June 2026; Bali OTA NIB verification Mar 2026; Tokyo 3% FY2027 announcement; Kyoto hotel tax 1 Mar 2026 9× hike), monthly for active reform calendars (BCN 2028 expiry countdown; Athens AMA extension review; SI 2027 60-day cap; FL/CA US municipal enforcement), quarterly for stable jurisdictions (Cyprus, Malta, Western EU baseline).

**Confidence**: HIGH for cross-cutting platform-fee baseline + 2024-2026 reform calendar (well-sourced); MEDIUM-HIGH for per-country one-liners (mix of primary regulator + named-secondary); MEDIUM for neighborhood-zone overlays (municipal portals are not consistently English-language indexed; verify in local language). LOW for the 5 verified-unverified items pending primary-source confirmation.
