# Universal `--exit` Section

Sell-side conditions: time-on-market (DOM), agent commission structure, contract norms, off-market vs MLS, sell-side closing costs, liquidity rating. Buyers should understand how easy it will be to **exit** a property before committing to buy.

**Snapshot**: May 2026 (Tier-3 additions — 71 countries total).

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

## Western Europe

### 🇫🇷 France
- **DOM**: Paris ~75-90 d / Lyon ~85-100 / secondary 100-140 d / rural >180 d
- **Commission**: seller-pays 4-7% incl. VAT (sliding by price)
- **Contract**: mandat simple/exclusif; 3 mo exclusive standard, auto-renewing to 24 mo cap; 14-day cooling-off
- **MLS**: NO true MLS. AMEPI inter-agency (~30%); SeLoger / LeBonCoin / Bien'ici dominate
- **Discount**: 4-7% off asking; rural Vienne / Creuse 10-15%
- **Sell-side**: agent 4-7% + plus-value 36.2% on gain (abated 6yr+; full exempt 22yr IR / 30yr CSG) + diagnostics ~€500-800
- **Liquidity**: 🟢 MEDIUM Paris/Lyon/Bordeaux/Nice; 🟠 LOW rural
- **Quirks**: Mandatory DPE — F/G class properties (passoires thermiques) face collapsing liquidity (rental ban G since Jan 2025, F from 2028). Compromis → ~3 mo to acte authentique

### 🇮🇹 Italy
- **DOM**: Milan ~95 d / Rome ~120 d / Florence ~110 / South 180-300 d
- **Commission**: **BOTH SIDES PAY** (unique in Europe): 2-4% each + VAT 22% = ~5-8% combined
- **Contract**: incarico exclusive 6 mo; cooling-off 10 days off-premises
- **MLS**: no formal MLS; FIAIP/FIMAA networks share informally; Immobiliare.it dominant
- **Discount**: 8-12% off asking national; deeper South + rural
- **Sell-side**: plusvalenza 26% flat on gain if <5 yrs (exempt primary); commission 2-4% + VAT
- **Liquidity**: 🟢 MEDIUM Milan/Rome/Bologna; 🟠 LOW South/inland/borgo
- **Quirks**: "Superbonus 110%" credit-encumbered properties (2020-2023) carry transferred tax obligations; €1 borgo houses often unsellable on resale

### 🇩🇪 Germany
- **DOM**: Berlin ~90 d / Munich ~110 / Hamburg ~95 / Leipzig ~80 / rural east 200+
- **Commission**: **SPLIT since Dec 2020** (Bestellerprinzip-adjacent): 3.57% each + VAT (7.14% total) — 50/50 mandatory in single-family resale
- **Contract**: Maklervertrag exclusive 3-6 mo; 14-day cooling-off
- **MLS**: no MLS; ImmoScout24, Immowelt, Kleinanzeigen
- **Discount**: 5-10% off asking; 2024-2025 correction added 3-5 ppts
- **Sell-side**: Spekulationssteuer at marginal income rate if <10 yrs (exempt if owner-occupied 2+ yrs); commission 3.57%
- **Liquidity**: 🟢 MEDIUM-HIGH top-7 cities; 🟠 MEDIUM secondary; 🔴 LOW rural east
- **Quirks**: Energy class E-H increasingly hard to sell post-GEG 2024; Erbpacht (leasehold) stigmatised; Vorkaufsrecht (municipal pre-emption) in select Berlin districts

### 🇦🇹 Austria
- **DOM**: Vienna ~110 d / Salzburg ~130 / Graz ~100 / Tyrol resort 60-90
- **Commission**: split 3% + 20% VAT each = 3.6% (capped Maklergesetz)
- **Contract**: alleinvermittlungsauftrag exclusive 3-6 mo
- **MLS**: no MLS; willhaben.at + ImmoScout24
- **Discount**: 5-8% off asking
- **Sell-side**: ImmoESt 30% on gain (with indexation); commission 3.6%
- **Liquidity**: 🟢 MEDIUM Vienna; 🟢 MEDIUM-HIGH ski resorts; 🟠 LOW Burgenland rural
- **Quirks**: **Strict Ausländergrundverkehr in Tyrol/Vorarlberg/Salzburg** — non-EU/EEA buyers blocked or quota-limited, narrows future buyer pool

### 🇨🇭 Switzerland
- **DOM**: Zurich ~70 d / Geneva ~90 / Lausanne ~85 / Lugano ~140 / rural alpine 180-365+
- **Commission**: seller-pays 2-3% + 8.1% VAT; luxury chalet 1.5-2%
- **Contract**: Mäklervertrag exclusive 3-6 mo
- **MLS**: NO MLS, very fragmented; Homegate, ImmoScout24.ch, Comparis
- **Discount**: 2-5% off asking — narrowest in Europe
- **Sell-side**: cantonal Grundstückgewinnsteuer (sliding 0-50%, drops sharply with holding — e.g. ZH 0% after 25 yrs); notary 0.1-0.5%; commission 2-3%
- **Liquidity**: 🟢 HIGH Zurich/Geneva metros; 🟠 MEDIUM Basel/Bern/Lausanne; 🔴 LOW alpine secondary residences
- **Quirks**: **Lex Koller** restricts non-resident buyers — future buyer pool excludes most foreigners outside resort zones; chalet quota in Valais/Graubünden

### 🇱🇮 Liechtenstein
- **DOM**: Vaduz ~120-200 / Schaan ~150-250 / regional 200-365+ [verify per-transaction]
- **Commission**: seller-pays 2-3% + 8.1% VAT (CH-aligned practice; no LI-specific broker law)
- **Contract**: Maklervertrag exclusive 3-6 mo (CH-aligned)
- **MLS**: NO MLS; thin market; **eRanger.li / Homegate.ch / ImmoScout24.ch** cross-listing common — most LI buyers cross to CH portals
- **Discount**: 3-5% off asking — narrow (CH-aligned)
- **Sell-side**: **Grundstückgewinnsteuer cantonal-equivalent** at LI-level (verify Steuerverwaltung FL); notary + Grundbuchamt registration ~0.5-1%; commission 2-3%+VAT
- **Liquidity**: 🔴 LOW Vaduz/Schaan — tiny market (~40k pop nationwide); buyer pool quota-restricted (~28 EEA + ~17 third-country/year by lottery)
- **Quirks**: **Lex Koller-equivalent** restricts non-EEA buyers — CH-integrated practice but no automatic CH-resident purchase rights; quota residency narrows future buyer pool dramatically; cross-border buyer demand mostly CH-resident; FL1 + Telecom Liechtenstein gigabit; tiny market = price discovery slow

### 🇲🇨 Monaco
- **DOM**: Monte-Carlo / La Condamine / Fontvieille ~90-180 / Larvotto / Saint-Roman ~120-200 / regional 200-365+ [verify with Chambre Immobilière de Monaco]
- **Commission**: **agent agency 3% + buyer agency 3% (BOTH SIDES PAY)** typical + 20% TVA on agent fees; luxury negotiable to 2-3% combined
- **Contract**: mandat de vente exclusive 3-6 mo
- **MLS**: NO MLS; thin market; **Chambre Immobilière de Monaco + Riviera-aligned portals** (FNAIM-style cross-listings to FR Côte d'Azur) — agent-driven
- **Discount**: 5-10% off asking; ultra-prime narrower
- **Sell-side**: **NO CGT** on real-estate gain in MC (NO PIT regime — except FR nationals via 1963 Convention); droits d'enregistrement ~4.5% + notaire ~1.5% (typically buyer-side); commission 3% each + 20% TVA
- **Liquidity**: 🟢 MEDIUM-HIGH Monte-Carlo / La Condamine / Larvotto core (UHNW global demand sustained 2020-2026); 🟠 MEDIUM Fontvieille; thin secondary
- **Quirks**: **Sûreté Publique due-diligence** required for non-resident buyers/sellers (KYC + source-of-funds); **carte de séjour pathway requires ~€500k bank deposit** + property purchase or rental practitioner; **NO PIT/CGT is the principal draw** sustaining global UHNW demand; sea-level rise concern (Plan Bleu / Plan Climat); cross-border seasonal demand from FR (Nice/Menton) and IT (Imperia)

### 🇦🇩 Andorra
- **DOM**: Andorra la Vella / Escaldes-Engordany ~100-180 / parish villages (Encamp / La Massana / Ordino / Canillo / Sant Julià) 120-300 / La Massana ski-zone 90-200 [verify with AGIA]
- **Commission**: seller-pays 3-5% + AD GST 4.5% (IGI; among lowest VAT in Europe); split occasionally
- **Contract**: contracte de mediació exclusive 3-6 mo
- **MLS**: NO MLS; **Habitaclia + Idealista (ES portal cross-listings)** dominate; AGIA member-network
- **Discount**: 5-12% off asking; village stock deeper
- **Sell-side**: **plusvàlua municipal sliding** (parish-by-parish; commune-level; 0% after long hold); IRPF 0/5/10% on gain at AD-resident progressive rates — verify Departament de Tributs i Fronteres; commission 3-5%
- **Liquidity**: 🟠 MEDIUM Andorra la Vella / Escaldes-Engordany core; 🟠 MEDIUM-HIGH ski-zone (La Massana / Encamp / Canillo) seasonal Dec-Apr; 🔴 LOW village stock off-season
- **Quirks**: **Llei 26/2024 STR regulation + parish quotas** narrow short-let economics (verify per parròquia at Govern d'Andorra); foreign-buyer registration at Govern d'Andorra mandatory since 2012 reform; **20yr to naturalisation** (longest in Western Europe); CASS social-security mandatory for residents; high mountain isolation; ~75% non-Andorran of ~85k pop sustains buyer-pool diversity (ES/FR/PT/UK)

### 🇳🇱 Netherlands
- **DOM**: Amsterdam ~28 d / Rotterdam ~25 / Utrecht ~30 / national ~30-40 d
- **Commission**: seller-pays 1-2% (no VAT for NVM members on resi)
- **Contract**: bemiddelingsovereenkomst exclusive 3 mo standard; no statutory cooling-off seller (buyer 3-day)
- **MLS**: **YES — Funda is a true MLS** (NVM-owned) — exceptional transparency
- **Discount**: 2025-2026 averaging **+3 to +8% OVER asking** in Randstad; -2-3% regional
- **Sell-side**: no CGT on primary residence; commission 1-2%; energy label mandatory
- **Liquidity**: 🟢 VERY HIGH Randstad; 🟢 HIGH rest
- **Quirks**: **Most transparent + fastest market in EU**; bidding wars normal; erfpacht (leasehold) common Amsterdam/Rotterdam

### 🇧🇪 Belgium
- **DOM**: Brussels ~70-90 d / Antwerp ~75 / Ghent ~65 / Wallonia rural 150-250
- **Commission**: seller-pays 3% + 21% VAT = 3.63%
- **Contract**: bemiddelingsovereenkomst exclusive 3-6 mo; 7-day cooling-off (statutory)
- **MLS**: no MLS; Immoweb, Zimmo
- **Discount**: 5-10% off asking
- **Sell-side**: no CGT on primary residence held >5 yrs; meerwaardebelasting 16.5% if <5 yrs; commission 3.63%
- **Liquidity**: 🟢 MEDIUM Brussels/Antwerp/Ghent; 🟠 LOW Wallonia rural
- **Quirks**: **3 regions = 3 regimes** (FL/BR/WA) on transfer tax, energy rules, registration; Flanders renovation obligations since 2023

### 🇱🇺 Luxembourg
- **DOM**: Lux City ~120-180 d / national 150-220 d (post-2022-2024 correction)
- **Commission**: seller-pays 3% + 17% VAT = 3.51%
- **Contract**: mandat exclusive 3 mo
- **MLS**: no MLS; **very thin market** — atHome.lu + immotop.lu
- **Discount**: 8-15% off asking 2025-2026 (post-correction)
- **Sell-side**: plus-value half-marginal rate if held >2 yrs; primary residence exempt; commission 3.51%
- **Liquidity**: 🟠 LOW-MEDIUM — small market, ~3,000-4,000 transactions/yr nationwide
- **Quirks**: Tiny market = price discovery slow; cross-border buyers (FR/BE/DE) dominate — sensitive to FX and rate cycles

### 🇮🇪 Ireland
- **DOM**: Dublin ~50-70 d / Cork ~60 / national ~80 d
- **Commission**: seller-pays 1-2.5% + 23% VAT
- **Contract**: sole agency 8-12 weeks
- **MLS**: no MLS; Daft.ie + MyHome.ie de-facto duopoly, good transparency
- **Discount**: -2 to +5% vs asking; bidding common Dublin
- **Sell-side**: CGT 33% on gain (PPR exemption primary); BER cert mandatory; commission 1-2.5%
- **Liquidity**: 🟢 HIGH Dublin commuter belt; 🟠 MEDIUM rest
- **Quirks**: Severe stock shortage = strong seller's market; **gazumping legal** until contracts exchanged; sealed-bid common above €750k

### 🇬🇧 United Kingdom
- **DOM**: London ~55-75 d / Manchester ~40 / Birmingham ~45 / national ~50-65 d sale-agreed; **then 4-6 mo to completion**
- **Commission**: seller-pays 1-2.5% + VAT (multi-agency 2.5-3.5%); online flat-fee £999-£3000
- **Contract**: sole agency 8-12 weeks; sole-selling-rights distinct (broader)
- **MLS**: no MLS; Rightmove, Zoopla, OnTheMarket dominate
- **Discount**: 3-7% off asking; 2024-2025 more discount-friendly
- **Sell-side**: CGT 18-24% on gain (PPR exempt); EPC mandatory; commission 1-2.5%+VAT; conveyancing £800-2000
- **Liquidity**: 🟢 HIGH London/SE/major cities; 🟠 MEDIUM north/Wales; 🔴 LOW leasehold flats with short leases or cladding issues
- **Quirks**: **Chain-driven delays unique to UK** — your sale tied to buyer's sale tied to *their* buyer; ~30% of transactions fall through; leasehold reform (2024) reshaping flat resales; cladding (post-Grenfell EWS1) drags

## Iberia / Mediterranean

### 🇪🇸 Spain
- **DOM**: Madrid ~50-70 d / Barcelona ~60-80 / Málaga/Costa del Sol ~70 / Valencia ~75 / Seville ~90 / inland 150-300+
- **Commission**: seller-pays 3-6% + 21% VAT (5% typical; 3-4% luxury)
- **Contract**: exclusiva 3-6 mo; 14-day cooling-off off-premises
- **MLS**: regional MLSs exist (Costa del Sol, Madrid); fragmented; Idealista + Fotocasa
- **Discount**: 8-12% off asking national; coastal narrower
- **Sell-side**: CGT 19-28% sliding (residents); 19% flat non-residents (EU/EEA); plusvalía municipal
- **Liquidity**: 🟢 HIGH Madrid/BCN/Costa del Sol/Balearics; 🟠 MEDIUM Valencia/Seville; 🔴 LOW inland (Soria, Teruel, Cuenca)
- **Quirks**: Golden Visa terminated April 2025 — high-end Madrid/BCN/Marbella absorbing impact; **non-resident sellers face 3% retention** by buyer remitted to AEAT

### 🇵🇹 Portugal
- **DOM**: Lisbon ~60-90 d / Porto ~70 / Algarve ~90 / Silver Coast 100-150 / interior 200-365
- **Commission**: seller-pays 4-6% + 23% VAT (5% typical)
- **Contract**: em regime de exclusividade 6 mo standard, max 24
- **MLS**: no MLS; Idealista, Imovirtual, Casa Sapo
- **Discount**: 5-10% off asking; rural deeper
- **Sell-side**: residents taxed on 50% of gain at marginal (exempt if reinvested in PR within EU); non-residents 28% flat; commission 4-6%+VAT
- **Liquidity**: 🟢 HIGH Lisbon/Porto/Algarve coastal; 🟠 MEDIUM Silver Coast; 🔴 LOW interior (Alentejo inland, Beira)
- **Quirks**: NHR ended Dec 2023 — softening top-end Lisbon/Porto 2024-2026; Golden Visa real-estate route closed Oct 2023; AL (STR licence) freezes/non-renewal in Lisbon/Porto reshape investor exits

### 🇬🇷 Greece
- **DOM**: Athens ~90-150 d / Thessaloniki ~120 / islands seasonal 90-300 / mainland rural 200-365+
- **Commission**: BOTH SIDES PAY 2% each + 24% VAT
- **Contract**: σύμβαση μεσιτείας exclusive 6 mo
- **MLS**: no MLS; Spitogatos.gr + XE.gr
- **Discount**: 8-15% off asking; islands narrower
- **Sell-side**: **CGT on real estate suspended through 2026 (extended)**; commission 2%+VAT; ENFIA arrears must be cleared at sale
- **Liquidity**: 🟢 MEDIUM-HIGH Athens centre/southern suburbs; 🟢 MEDIUM Thessaloniki + Cyclades/Ionian top islands; 🔴 LOW mainland rural; 🔴 VERY LOW less-touristed islands
- **Quirks**: Golden Visa thresholds raised Sep 2024 cooling top-end; forest/coastal/archaeological zone overlays critical to verify; Ktimatologio rollout still incomplete in pockets

### 🇨🇾 Cyprus
- **DOM**: Limassol ~80-120 d / Nicosia ~110 / Paphos ~120 / Larnaca ~100
- **Commission**: seller-pays 3-5% + 19% VAT
- **Contract**: RoEA-licensed, exclusive 3-6 mo
- **MLS**: no MLS; Bazaraki + Property.com.cy
- **Discount**: 5-12% off asking
- **Sell-side**: CGT 20% on gain (lifetime exemptions: €30,000 general post-2026, €150,000 primary post-2026); commission 3-5%
- **Liquidity**: 🟢 MEDIUM-HIGH Limassol (Russian/Israeli/Lebanese demand 2022-2026); 🟠 MEDIUM Paphos/Larnaca; 🔴 LOW villages
- **Quirks**: Title-deed delays a long-running issue (developer mortgages "trapped" titles — Amendment Law 110(I)/2025 addressing); CBI scheme withdrawn 2020 left lingering luxury overhang in Limassol/Paphos

### 🇲🇹 Malta
- **DOM**: Sliema/St Julian's ~90-120 d / Valletta/Gozo 120-200
- **Commission**: seller-pays 3.5-5% + 18% VAT
- **Contract**: sole agency 3-6 mo
- **MLS**: no MLS; agent-driven, MaltaPark + agency portals
- **Discount**: 5-10% off asking
- **Sell-side**: final withholding 8% of sale price (5% if <5 yrs and conditions; 12% gain-tax option in some cases); commission 3.5-5%
- **Liquidity**: 🟢 MEDIUM Sliema/St Julian's/Valletta core; 🟠 LOW-MEDIUM Gozo
- **Quirks**: **AIP restrictions for non-residents outside SDA** narrows future foreign-buyer pool to SDAs; UCA (Urban Conservation Area) heritage rules affect refurbs

## Nordics

### 🇸🇪 Sweden
- **DOM**: Stockholm ~25-40 d / Gothenburg ~30 / Malmö ~35 / national ~40-50 d
- **Commission**: seller-pays 2-4% + 25% VAT (Stockholm 1.5-2.5%; rural up to 5%)
- **Contract**: förmedlingsuppdrag exclusive 3 mo standard
- **MLS**: **Hemnet ~ MLS** — extreme transparency, all listings + price history + sold prices
- **Discount**: bidding-up culture; sales often 5-15% over starting (utgångspris intentionally low); cooler 2024-2025 brought it closer to flat
- **Sell-side**: CGT 22% on gain (deferred if reinvesting — uppskov); commission 2-4%
- **Liquidity**: 🟢 HIGH Stockholm/Gothenburg/Malmö; 🟠 MEDIUM rest
- **Quirks**: Bostadsrätt (co-op apartment) ≠ ownership — board approval needed; **budgivning (open bidding)** post-viewing is cultural norm

### 🇫🇮 Finland
- **DOM**: Helsinki ~80-100 d / Tampere ~90 / Turku ~100 / national ~110-130 d
- **Commission**: seller-pays 3-5% incl. VAT 25.5%; min ~€3,000-5,000
- **Contract**: toimeksiantosopimus exclusive 4 mo standard
- **MLS**: no MLS; Etuovi.com + Oikotie
- **Discount**: 5-10% off asking; 2024-2025 deeper
- **Sell-side**: CGT 30-34% on gain (primary exempt if owned + lived in 2 yrs); commission 3-5%; energy cert mandatory
- **Liquidity**: 🟠 MEDIUM Helsinki metro; 🔴 LOW elsewhere — Finland in deep housing slump 2024-2026
- **Quirks**: Asunto-osakeyhtiö (housing co-op) = own shares in building; northern/eastern rural near-zero liquidity

### 🇳🇴 Norway
- **DOM**: Oslo ~25-45 d / Bergen ~35 / Trondheim ~30 / national ~45-60 d
- **Commission**: seller-pays 1-3% + 25% VAT; min NOK 30-60k
- **Contract**: oppdragsavtale exclusive 6 mo (statutory max)
- **MLS**: no MLS; Finn.no near-monopoly
- **Discount**: bidding-up common; sale often equals/exceeds asking
- **Sell-side**: CGT 22% on gain (exempt if owned 1 yr + lived 1 of last 2); **tilstandsrapport mandatory since 2022**
- **Liquidity**: 🟢 HIGH Oslo/Bergen/Trondheim/Stavanger; 🟠 MEDIUM rest
- **Quirks**: Mandatory pre-sale condition report shifted defect liability to seller; concessions law (konsesjonsloven) on rural/agri >100 dekar

### 🇩🇰 Denmark
- **DOM**: Copenhagen ~60-90 d / Aarhus ~70 / national ~120-180 d
- **Commission**: seller-pays 1-3% + 25% VAT; flat-fee variants common
- **Contract**: formidlingsaftale exclusive 6 mo statutory max; **6-day buyer cooling-off (fortrydelsesret)**
- **MLS**: no MLS; Boligsiden aggregates almost all
- **Discount**: 3-7% off asking
- **Sell-side**: CGT exempt if primary residence (parcelhus rule); 0% typical; commission 1-3%+VAT
- **Liquidity**: 🟢 HIGH Copenhagen; 🟠 MEDIUM Aarhus/Odense/Aalborg; 🔴 LOW rural Jutland
- **Quirks**: Andelsbolig (cooperative) ≠ ejerbolig (full ownership) — different price ceilings, association approval; new property valuation system (2024) reshaping tax base

### 🇮🇸 Iceland
- **DOM**: Reykjavík ~60-90 d / national ~80-120 d
- **Commission**: seller-pays 1.5-2.5% + 24% VAT
- **Contract**: söluumboð exclusive 6 mo
- **MLS**: no MLS; Mbl.is/fasteignir.is
- **Discount**: 2-5% off asking
- **Sell-side**: CGT 22% on gain (primary exempt if held 2+ yrs); commission 1.5-2.5%
- **Liquidity**: 🟢 MEDIUM Reykjavík capital region (~2/3 of all population); 🔴 LOW-VERY LOW outside
- **Quirks**: Tiny market (~370k pop), volatile; volcanic/seismic disclosures matter (Grindavík 2023-2024); STR regulation reshaped 2025

## CEE / Baltics

### 🇨🇿 Czech Republic
- **DOM**: Prague ~75-100 / Brno ~90 / Ostrava ~120 / rural 150-250
- **Commission**: seller-pays 3-5% + 21% VAT
- **MLS**: no; Sreality.cz dominant
- **Sell-side**: income-tax exempt if held 10 yrs (since 2021; was 5) or primary residence reinvested; commission 3-5%; transfer tax abolished 2020
- **Liquidity**: 🟠 MEDIUM Prague/Brno; 🔴 LOW rural

### 🇸🇰 Slovakia
- **DOM**: Bratislava ~90-120 / Košice ~100 / rural 150-300
- **Commission**: seller-pays 3-5% + 23% VAT
- **MLS**: no; Nehnutelnosti.sk + Reality.sk
- **Sell-side**: income-tax exempt if held 5+ yrs; commission 3-5%; no transfer tax
- **Liquidity**: 🟠 MEDIUM Bratislava; 🔴 LOW-VERY LOW east/rural
- **Quirks**: Co-ownership (podielové vlastníctvo) very common in inherited rural plots — clean title is gating issue

### 🇵🇱 Poland
- **DOM**: Warsaw ~70-100 / Kraków ~80 / Gdańsk/Wrocław ~85 / national ~120 d
- **Commission**: BOTH SIDES PAY 2-3% each + VAT; some seller-only at 3-5%
- **Contract**: exclusive (na wyłączność) 3-6 mo
- **MLS**: no; Otodom + OLX + Morizon
- **Sell-side**: PIT 19% on gain if held <5 yrs (cal. yrs incl. acquisition year); exempt if reinvested in housing within 3 yrs
- **Liquidity**: 🟢 HIGH Warsaw/Kraków/Gdańsk/Wrocław; 🟠 MEDIUM Łódź/Poznań; 🔴 LOW east rural
- **Quirks**: Perpetual usufruct (użytkowanie wieczyste) being phased out — check status

### 🇭🇺 Hungary
- **DOM**: Budapest ~75-100 / Debrecen ~90 / Lake Balaton seasonal 60-180 / rural 150-300
- **Commission**: seller-pays 3-5% + 27% VAT (highest VAT in EU)
- **MLS**: no; Ingatlan.com dominant
- **Sell-side**: PIT 15% on gain, sliding to 0% after 5 yrs; commission 3-5%+27%VAT
- **Liquidity**: 🟠 MEDIUM Budapest; MEDIUM Balaton seasonal; 🔴 LOW rural east

### 🇸🇮 Slovenia
- **DOM**: Ljubljana ~90-120 / coast 100-180 / rural 200-365
- **Commission**: seller-pays 4% + 22% VAT (statutory cap 4%)
- **Contract**: exclusive 9 mo max statutory; 15-day cooling-off
- **Sell-side**: CGT 25%, decreasing 5pp every 5 yrs (0% after 15)
- **Liquidity**: 🟠 MEDIUM Ljubljana; MEDIUM coast seasonal; 🔴 LOW rural

### 🇭🇷 Croatia
- **DOM**: Zagreb ~90-120 / Split ~100 / Dubrovnik 150+ / Istria 100-200 / rural 200-365
- **Commission**: BOTH SIDES PAY 2-3% each + 25% VAT
- **MLS**: no; Njuškalo + Crozilla
- **Sell-side**: CGT 24% if sold <2 yrs (exempt after); commission 2-3%+VAT
- **Liquidity**: 🟢 MEDIUM-HIGH coast (Adriatic, Dalmatia); MEDIUM Zagreb; 🔴 LOW inland Slavonia
- **Quirks**: Cadastre vs land registry mismatches still drag (legacy, gradually resolved); foreign-buyer reciprocity rules; agricultural land 10-yr lock for non-EU

### 🇪🇪 Estonia
- **DOM**: Tallinn ~50-80 / Tartu ~70 / national ~100
- **Commission**: seller-pays 2-4% + 22% VAT
- **MLS**: no; KV.ee + City24
- **Sell-side**: income tax 22% on gain (primary residence exempt)
- **Liquidity**: 🟢 HIGH Tallinn (relative to size); 🟠 MEDIUM Tartu/Pärnu; 🔴 LOW rural east
- **Quirks**: **Most digitised land registry in EU** (e-Kinnistu); fast transactions

### 🇱🇻 Latvia
- **DOM**: Riga ~80-120 / Jūrmala (resort) seasonal 100-200 / national ~150
- **Commission**: seller-pays 3-5% + 21% VAT
- **MLS**: no; SS.com (classifieds-style) dominates
- **Sell-side**: PIT 25.5% on gain (exempt if primary, 5 yrs + 12 mo declared); commission 3-5%
- **Liquidity**: 🟠 MEDIUM Riga centre; 🔴 LOW Soviet-era stock; VERY LOW Latgale rural east
- **Quirks**: "Denationalised house" (denacionalizēts) tenancy issues persist on pre-WWII stock; Russian-speaking buyer pool diminished post-2022

### 🇱🇹 Lithuania
- **DOM**: Vilnius ~60-90 / Kaunas ~70 / Klaipėda ~80 / national ~100
- **Commission**: seller-pays 2-4% + 21% VAT
- **MLS**: no; Aruodas dominant + Domoplius + Skelbiu
- **Sell-side**: PIT 15% on gain if held <10 yrs and not primary; commission 2-4%
- **Liquidity**: 🟢 MEDIUM-HIGH Vilnius (strongest of Baltics 2024-2026); 🟠 MEDIUM Kaunas/Klaipėda; 🔴 LOW rural

### 🇷🇴 Romania
- **DOM**: Bucharest ~80-120 / Cluj ~70-100 / Timișoara ~90 / rural 150-365+
- **Commission**: BOTH SIDES PAY 2-3% each + 19% VAT
- **MLS**: no; Imobiliare.ro + Storia + OLX
- **Sell-side**: tax 1-3% of gain (sliding by holding period and amount)
- **Liquidity**: 🟠 MEDIUM Bucharest/Cluj/Timișoara; 🔴 LOW small towns; VERY LOW rural
- **Quirks**: Restitution claims on pre-1989 properties historically muddied titles (mostly resolved but always check); Cluj is hottest urban market in CEE

### 🇧🇬 Bulgaria
- **DOM**: Sofia ~90-120 / Plovdiv ~110 / Varna/Burgas 120-180 / Bansko 150-300 / rural 200-365+
- **Commission**: BOTH SIDES PAY 2-3% each + 20% VAT
- **MLS**: no; Imot.bg + Imoti.net
- **Sell-side**: PIT 10% on gain (exempt: 1 residence held 3+ yrs, 2 residences 5+ yrs)
- **Liquidity**: 🟠 MEDIUM Sofia; 🔴 LOW Plovdiv/Varna/Burgas; VERY LOW Black Sea overdeveloped resort + Bansko ski (oversupply)
- **Quirks**: Apartment complexes on Black Sea / Bansko built 2005-2010 face structural oversupply; agricultural land foreign-restricted

### 🇲🇩 Moldova
- **DOM**: Chișinău (Centru / Botanica / Buiucani) ~120-200 / Bălți / Tiraspol-area excluded / regional 200-365+ [verify per-transaction]
- **Commission**: 2-4% **typically split or seller-only** (informal; weakly regulated) + 20% VAT only on services where applicable
- **Contract**: agency contracts 3-6 mo informal; Camera de Înregistrare a Proprietății (State Registration Chamber) registration ~5-15 days
- **MLS**: no MLS; **999.md (national classifieds) + Lara.md + Make.md** dominate; agency portals fragmented
- **Discount**: 10-20% off asking; rural deeper
- **Sell-side**: **PIT flat 12%** on gain (one of lowest in Europe); primary-residence exempt if held 3+ yrs (verify SFS); **agricultural land foreign-restricted** (only buildings + non-agricultural for foreigners); commission 2-4%
- **Liquidity**: 🟠 LOW-MEDIUM Chișinău Centru / Botanica / Buiucani; 🔴 LOW Bălți; VERY LOW rural; **Transnistria-scope EXCLUDED** (no due-diligence on titles east of Dniester)
- **Quirks**: **CBI ENDED via Law 100/2020** — Investor Residency Law 200/2010 (€250k, 5yr) is the practical track; **Romanian-citizenship-by-descent** widely used by MD residents → EU passport path runs in parallel to the property economics; gigabit fiber Moldtelecom + Orange MD + StarNet (one of the fastest fiber penetrations in Eastern Europe per Ookla 2024-2026); EU candidate Jun 2022 — accession-track sentiment may compress yields over time; medical-staff emigration to RO/EU is structural concern for buyer-pool demographic profile

## Western Balkans

### 🇷🇸 Serbia
- **DOM**: Belgrade ~90-150 / Novi Sad ~100 / national 150-300+ [verify per-transaction]
- **Commission**: BOTH SIDES PAY 2-3% each + 20% VAT
- **MLS**: no; 4zida.rs + Halo Oglasi
- **Sell-side**: CGT 15% on gain (exempt if reinvested in housing within 90 d, or held 10+ yrs)
- **Liquidity**: 🟠 MEDIUM Belgrade Vračar/Stari Grad/Novi Beograd; 🔴 LOW rest

### 🇲🇪 Montenegro
- **DOM**: coastal 60-180 / Podgorica 120-250 / interior 200-365+ [verify]
- **Commission**: seller-pays 3-5% + 21% VAT or split
- **MLS**: no; Nekretnine.me
- **Sell-side**: CGT 15% on gain
- **Liquidity**: 🟠 MEDIUM coast peak season (May-Sep) only; 🔴 LOW off-season; VERY LOW interior
- **Quirks**: Coastal seasonal-only — viewings/transactions concentrate May-Sep; Russian/Ukrainian buyer pool reshaped post-2022

### 🇧🇦 Bosnia & Herzegovina
- **DOM**: Sarajevo 120-200 / Banja Luka 150-200 / Mostar 150-250 / rural 300-700+ [verify]
- **Commission**: BOTH SIDES PAY 2-3% each (informal; lighter regulation)
- **MLS**: no; Olx.ba
- **Sell-side**: FBiH ~10% on gain (>5 yrs exempt); RS-entity differs
- **Liquidity**: 🔴 LOW Sarajevo central; VERY LOW rest
- **Quirks**: **Cadastral fragmentation drags transactions** — two entities + Brčko + dual land-book/cadastre legacy; minefield zones near former front lines (check IMSMA database)

### 🇲🇰 North Macedonia
- **DOM**: Skopje 100-180 / Ohrid lakeside 90-200 / rest 200-400+ [verify]
- **Commission**: seller-pays 2-4% or split
- **MLS**: no; Reklama5.mk
- **Sell-side**: CGT 10% on gain (sliding, exempt after 5 yrs primary)
- **Liquidity**: 🔴 LOW Skopje (Centar/Karpoš); VERY LOW rest
- **Quirks**: Cash-driven; rural inheritance fractionalisation severe; diaspora demand episodic

### 🇦🇱 Albania
- **DOM**: Tirana 90-180 / Sarande/Vlorë coast 100-250 / rural 200-500+ [verify]
- **Commission**: BOTH SIDES PAY 2-3% each (informal, often higher; weakly regulated)
- **MLS**: no; MerrJep.com
- **Sell-side**: CGT 15% on gain (since 2024 reform); cadastral fee ~1%
- **Liquidity**: 🔴 LOW Tirana Blloku/Komuna e Parisit; VERY LOW rest
- **Quirks**: **Cadastral issues are the binding constraint** — pre-1991 communist-era ownership chaos + 1990s informal construction (~30-40% of stock in Tirana); ALUIZNI legalisation programme ongoing but slow

## Anglo non-EU

### 🇺🇸 United States
- **DOM**: NYC ~70-90 d / SF ~30-45 / LA ~50-70 / Miami ~75-100 / Austin ~50-70 / Chicago ~60-80 / national median ~55-70 d (NAR 2025 data)
- **Commission**: **NAR settlement effective Aug 17, 2024 unbundled buyer-agent commissions** — historic 5-6% seller-pays-both-sides model fragmenting; many states now buyer-pays own agent (negotiated upfront); listing-side typically 2.5-3%
- **Contract**: exclusive listing 60-180 d (state-by-state); buyer-rep agreement now mandatory before showings (NAR settlement)
- **MLS**: **YES — true MLS** (~580 regional MLSs feeding Zillow/Realtor.com/Redfin); deepest transparency globally
- **Discount**: 2024-2026 reset = 2-5% off asking national; hot Sun Belt (Austin/Phoenix) closer to flat
- **Sell-side**: federal CGT 0/15/20% long-term + state (CA up to 13.3%, NY ~10.9%); **§ 121 primary-residence exemption $250k single / $500k MFJ** (must own + occupy 2 of last 5 yrs); **FIRPTA 15% withholding on non-resident sellers** of US real property (gross sale price, > $300k); commission 4-6% combined (legacy) trending lower post-NAR
- **Liquidity**: 🟢 HIGH metros + Sun Belt; 🟠 MEDIUM Rust Belt secondary; 🔴 LOW remote rural / declining metros (parts of Detroit, rural West Virginia)
- **Quirks**: **NAR settlement reshaping commission norms 2024-2026** — buyer-agent commissions now negotiated separately, increased buyer cash-to-close; HOA/condo rules vary wildly; insurance availability collapsing in CA wildfire / FL hurricane zones is a growing exit drag; foreign buyers face FIRPTA holdback, 1099-S reporting

### 🇨🇦 Canada
- **DOM**: Toronto ~25-40 / Vancouver ~30 / Montreal ~30 / Calgary ~25 / national ~35-50
- **Commission**: **SELLER-PAYS BOTH SIDES**: 4-6% total (split 2-3% to listing / 2-3% to buyer agent); ON 5% typical on first $X then 2.5%; flat-fee/discount brokerages exist
- **Contract**: listing agreement exclusive 60-180 d
- **MLS**: **YES — true MLS** (CREA Realtor.ca + provincial boards), highly transparent
- **Discount**: hot markets 2021-2022 sold over-asking; 2024-2026 reset = 2-7% off
- **Sell-side**: capital gains 50% inclusion at marginal rate (66.7% above $250k as of 2024 reform); primary residence exempt (PRE); commission 4-6%
- **Liquidity**: 🟢 HIGH GTA/GVA/Montreal/Calgary/Ottawa; 🟠 MEDIUM smaller cities; 🔴 LOW remote
- **Quirks**: **Foreign Buyer Ban extended to Jan 2027** — narrows exit pool if non-Canadian; assignment-sale taxation (since 2022); BC speculation tax + ON NRST + Vancouver empty-homes tax compress non-resident options

### 🇦🇺 Australia
- **DOM**: Sydney ~30-40 / Melbourne ~35 / Brisbane ~30 / Perth ~25 (hot 2024-2026) / Adelaide ~30
- **Commission**: seller-pays 1.5-3.5% + 10% GST (Sydney/Melb 1.8-2.5%; regional 2.5-3.5%)
- **Contract**: exclusive listing 60-90 d; auction-led culture in NSW/VIC
- **MLS**: no MLS; Domain + Realestate.com.au de-facto duopoly with high transparency
- **Discount**: auction-driven so often clears at or above reserve in hot markets; private treaty 3-7% off
- **Sell-side**: CGT at marginal, 50% discount if held 12+ mo; primary residence exempt; commission 1.5-3.5%+GST; marketing fees often separate AUD 3-10k
- **Liquidity**: 🟢 HIGH Sydney/Melbourne/Brisbane/Perth (Perth especially hot 2024-2026); 🟠 MEDIUM regional; 🔴 LOW remote
- **Quirks**: **FIRB restrictions + temporary ban on foreign purchase of established dwellings 2025-2027** narrows future buyer pool; vendor disclosure regimes vary by state

### 🇳🇿 New Zealand
- **DOM**: Auckland ~45-65 / Wellington ~50 / Christchurch ~40 / national ~50
- **Commission**: seller-pays 2.5-4% + 15% GST; tiered (e.g. 4% first $400k + 2% balance)
- **Contract**: sole agency 60-90 d; auction-led in Auckland
- **MLS**: no MLS; Trade Me Property + Realestate.co.nz
- **Discount**: 5-10% off asking 2024-2026 (post-correction)
- **Sell-side**: bright-line test: gain taxed if sold <2 yrs (rolled back from 10 yrs in 2024 for non-new-builds); commission 2.5-4%+GST
- **Liquidity**: 🟢 HIGH Auckland/Wellington/Christchurch; 🟠 MEDIUM regional; 🔴 LOW remote
- **Quirks**: **Foreign-buyer ban (OIA 2018) still in force** for established residential — narrows exit pool to citizens/residents; weathertight (leaky building) and seismic (esp. Wellington apartments) issues drag stock

## Latin America

### 🇲🇽 Mexico
- **DOM**: CDMX (Polanco/Roma/Condesa) ~90-150 / Guadalajara ~100 / Monterrey ~90 / Mérida 120-180 / Riviera Maya 90-200 / San Miguel de Allende 150-250
- **Commission**: seller-pays 4-7% + 16% IVA (5-6% typical); luxury can negotiate to 4%
- **Contract**: exclusividad 3-6 mo
- **MLS**: **partial MLS** in select metros (AMPI MLS Vallarta, Cabo, Mérida, Monterrey); CDMX fragmented
- **Discount**: 8-15% off asking
- **Sell-side**: ISR 25-35% on gain for residents (with allowances + indexation; primary residence exemption up to 700k UDIs); 25%/35% non-residents; commission 4-7%+IVA; notary buyer-side
- **Liquidity**: 🟠 MEDIUM CDMX prime / Guadalajara / Monterrey; 🟢 MEDIUM-HIGH Riviera Maya tourist core; 🔴 LOW secondary towns
- **Quirks**: **Fideicomiso (bank trust) required for foreigners in restricted zone** (50 km coast / 100 km border) — future foreign buyer needs trust setup, adds cost/time; ejido land cannot be freely sold (verify dominio pleno)

### 🇧🇷 Brazil
- **DOM**: São Paulo ~120-200 / Rio (Zona Sul) 100-180 / Florianópolis 100-150 / NE coast seasonal 120-300
- **Commission**: seller-pays 5-6% (CRECI 6% residential)
- **Contract**: exclusividade 3-6 mo
- **MLS**: no formal MLS; ZAP+VivaReal+OLX dominant
- **Discount**: 10-20% off asking
- **Sell-side**: ganho de capital 15-22.5% sliding; primary exempt if reinvested within 180 d; commission 5-6%; ITBI buyer-side
- **Liquidity**: 🟠 MEDIUM São Paulo/Rio/Curitiba/Floripa prime; 🔴 LOW secondary cities; VERY LOW rural / NE inland
- **Quirks**: Inflation indexation matters (CGT base adjusted); condomínio fees disclosure critical (high in Rio); coastal NE foreign-buyer demand sensitive to BRL/EUR cycle

### 🇦🇷 Argentina
- **DOM**: BA (Recoleta/Palermo) 180-365+ / Córdoba/Rosario 200-400 / national 300-500+ [verify]
- **Commission**: BOTH SIDES PAY 3-4% each (BA city law caps buyer 3%; seller 4%); some 2024-2026 deregulation under Milei
- **MLS**: no; ZonaProp + Argenprop
- **Discount**: 15-25% off asking — chronic
- **Sell-side**: ITI 1.5% of sale price OR Cedular 15% on gain (post-2018 acquisitions)
- **Liquidity**: 🔴 LOW even in BA prime — multi-year stock turnover, almost entirely cash USD market
- **Quirks**: **Transactions in physical USD historically** — Milei's 2024-2026 reforms loosening capital controls, peso strengthening; "blue dollar" / MEP cycle volatility; mortgage market re-emerging late 2024 after 6-yr drought

### 🇨🇷 Costa Rica
- **DOM**: Central Valley (Escazú/Santa Ana) 120-250 / Guanacaste coast 150-365+ / Caribbean 200-500
- **Commission**: seller-pays 5-7% (CCCBR 6%) + 13% VAT
- **MLS**: **MLS-CRGAR exists** for member realtors but coverage partial (~30-40%); much off-market
- **Discount**: 10-20% off asking
- **Sell-side**: capital gains 15% flat (since 2019 reform); option for 2.25% of sale price for first sale of habitual residence
- **Liquidity**: 🟠 MEDIUM-LOW Escazú/Santa Ana expat core; 🔴 LOW beach towns (seasonal/dollar-priced); VERY LOW rural
- **Quirks**: **Maritime Zone Law: first 50m public, next 150m concession (NOT freehold)** — concession property has narrower buyer pool; squatter rights (uso capión); everything dollar-priced

### 🇵🇦 Panama
- **DOM**: PTY (Costa del Este/Punta Pacífica) 120-200 / Boquete/Coronado expat 150-300 / Bocas del Toro 200-400+
- **Commission**: seller-pays 5% (ACOBIR standard) + 7% ITBMS
- **MLS**: no; ACOBIR has internal sharing; Encuentra24 dominant
- **Discount**: 10-20% off asking; PTY oversupply 2020-2024 pushed deeper
- **Sell-side**: CGT 10% on gain OR 3% advance on sale price (taxpayer chooses lower); transfer tax 2% buyer-side
- **Liquidity**: 🟠 MEDIUM Costa del Este / Punta Pacífica / Casco Viejo; 🔴 LOW-MEDIUM Coronado/Boquete expat; LOW Bocas/interior
- **Quirks**: **Rights-of-possession (ROP) land vs titled land** — ROP cheaper but harder to resell, esp. to financed buyers; PTY apartment oversupply 2010-2020 still digesting; USD-pegged so no FX layer

### 🇩🇴 Dominican Republic
- **DOM**: Punta Cana/Bávaro 120-250 / Cap Cana 150-300 / Santo Domingo (Piantini/Naco) 100-180 / Las Terrenas/Samaná 150-300+
- **Commission**: seller-pays 3-6% (5% common; luxury negotiable to 3-4%) + 18% ITBIS on commission only
- **Contract**: contrato de exclusividad 3-6 mo
- **MLS**: no formal MLS; AEI (Asociación de Empresas Inmobiliarias) members share informally; Encuentra24 + Punta Cana-specific portals
- **Discount**: 10-20% off asking; CONFOTUR developments may transact closer to ask
- **Sell-side**: residents capital gains 27% on net gain; **non-residents 27% withholding on gain** (or 1% of sale price advance, lower of two); **CONFOTUR exempt zones for first sale within program**; commission 3-6%
- **Liquidity**: 🟠 MEDIUM Punta Cana/Cap Cana tourist core (USD-priced); 🟠 LOW-MEDIUM Santo Domingo prime; 🔴 LOW interior / Samaná off-peak
- **Quirks**: **CONFOTUR (Law 158-01) tax incentives** for tourism-zone properties — verify eligibility transfers; USD-priced coastal markets, DOP-priced inland (FX exposure on inland exit); title irregularities common — Jurisdicción Inmobiliaria certificates required

### 🇨🇴 Colombia
- **DOM**: Bogotá (Chicó/Chapinero) ~120-200 / Medellín (Poblado/Laureles) ~100-180 / Cartagena (centro histórico) 150-300 / Cali ~150
- **Commission**: seller-pays 3-5% + 19% IVA (Lonja de Propiedad Raíz standard 3% — varies regionally)
- **Contract**: contrato de corretaje exclusivo 3-6 mo
- **MLS**: no formal MLS; Lonjas (regional realtor associations) share among members; Finca Raíz + Metrocuadrado dominate portals
- **Discount**: 10-15% off asking; coastal/Cartagena narrower
- **Sell-side**: **ganancia ocasional 15% flat on gain** (Ley 2277/2022 lifted from 10% effective 2023); residents may exempt up to ~7,300 UVT if sale proceeds reinvested in housing within 12 mo; commission 3-5%+IVA; retención en la fuente 1% buyer-side
- **Liquidity**: 🟢 MEDIUM Medellín Poblado / Bogotá Chicó-Chapinero; 🟠 MEDIUM Cartagena historic core; 🔴 LOW secondary cities
- **Quirks**: **Medellín "digital nomad" demand 2021-2024 cooling 2025-2026** as STR licensing tightens (Ley 2068 + local restrictions); USD-pricing creep in Poblado/Cartagena; estrato (1-6 socioeconomic strata) affects utilities + resale pool

### 🇺🇾 Uruguay
- **DOM**: Montevideo (Pocitos/Punta Carretas) ~120-180 / Punta del Este (Beverly Hills/La Barra) seasonal 90-300 (peak Dec-Feb) / Colonia 150-250
- **Commission**: 3-5% **typically split buyer/seller** (3% each common Punta del Este; Montevideo sometimes seller-only) + 22% IVA
- **Contract**: orden de venta exclusiva 3-6 mo
- **MLS**: no MLS; CIU (Cámara Inmobiliaria) members share; Mercado Libre + Gallito + InfoCasas
- **Discount**: 5-15% off asking; Punta del Este off-season deeper
- **Sell-side**: **IRPF cedular 12% on real (CPI-indexed) gain** OR 1.8% of sale price for pre-2007 acquisitions (taxpayer chooses lower); commission 3-5%+IVA each side
- **Liquidity**: 🟢 MEDIUM Pocitos/Punta Carretas/Carrasco; 🟠 MEDIUM Punta del Este peak; 🔴 LOW off-season Punta del Este; 🔴 LOW interior
- **Quirks**: **USD-priced market** (Argentine + Brazilian buyers dominate Punta del Este); seasonal liquidity (Dec-Feb); strict bank secrecy + low-friction foreign ownership = stable buyer pool; tax residency program (60-day rule) drives demand

### 🇨🇱 Chile
- **DOM**: Santiago (Las Condes/Vitacura/Providencia) ~90-150 / Viña del Mar/Valparaíso 120-200 / Concepción 120-180 / regions 150-300
- **Commission**: 2% **each side typical** (seller + buyer pay 2% each) + 19% IVA; some seller-only at 3%
- **Contract**: corretaje exclusivo 3-6 mo
- **MLS**: no MLS; Portal Inmobiliario + Yapo + TocToc
- **Discount**: 8-15% off asking 2024-2026 (post-correction)
- **Sell-side**: residents **CGT 10% on gain on residential** (first **UF 8,000 lifetime exempt** for individuals — Ley 21.210); non-residents 35% (additional tax); **Ley 21.442 (2022) condominium law** restructured edificios; commission 2%+IVA each side
- **Liquidity**: 🟢 MEDIUM Las Condes/Vitacura/Providencia; 🟠 MEDIUM Viña/Concepción; 🔴 LOW regions
- **Quirks**: **UF (Unidad de Fomento) inflation-indexed pricing** — contracts and prices in UF, paid in CLP at fixing date (FX/inflation hedge); 2019-2020 social unrest + 2021-2022 constitutional uncertainty + 2023 mortgage rate spike still digesting in 2026; co-propiedad inmobiliaria (condominio) regime governs apartments

## MENA / Levant / North Africa

### 🇹🇷 Türkiye
- **DOM**: Istanbul (European/Asian sides) ~60-120 / Antalya/Bodrum coast 90-180 / Ankara 100-150 / İzmir 80-120 / interior 150-300+
- **Commission**: **2-4% each side typical (negotiable)** + 20% KDV (VAT); commercial properties higher
- **Contract**: yetki belgesi 3-12 mo (since 2014 broker law)
- **MLS**: no formal MLS; sahibinden.com dominant + Hürriyet Emlak + Endeksa
- **Discount**: 5-15% off asking; deeper in TRY; foreign-USD-priced narrower
- **Sell-side**: **foreign-seller treated like resident for tax** (no FIRPTA-equivalent withholding); CGT exempt if held 5+ yrs; <5 yrs taxed at marginal rates with inflation indexation; **KFE (per-il published unit value)** governs minimum deed value for transfer fees
- **Liquidity**: 🟢 MEDIUM-HIGH Istanbul prime (Beşiktaş/Şişli/Kadıköy); 🟢 MEDIUM Antalya/Bodrum coast; 🟠 MEDIUM Ankara/İzmir; 🔴 LOW interior
- **Quirks**: **TRY devaluation 2021-2024 made USD-pricing dominant** in foreign-buyer zones (Antalya/Bodrum/Istanbul prime); **citizenship-by-investment threshold raised to USD 400k** (Jun 2022) reshaped low-end foreign demand; earthquake disclosure (post-Feb 2023 Kahramanmaraş) increasingly priced in; Tapu (deed) registration straightforward but sworn translator + verifying encumbrances critical

### 🇦🇪 United Arab Emirates
- **DOM**: Dubai (Marina/Downtown/Palm) ~45-90 / Abu Dhabi (Saadiyat/Reem) 60-120 / secondary emirates 90-180
- **Commission**: **2% seller-side typical (DLD-regulated)** + 5% VAT on commission; buyer-side 2% if buyer-rep
- **Contract**: **RERA Form A (seller-broker), Form B (buyer-broker), Form F (MOU/sale agreement)** mandatory in Dubai; 60-90 d transfer
- **MLS**: no MLS; Property Finder + Bayut + Dubizzle
- **Discount**: 5-10% off asking; off-plan oversupply pockets deeper
- **Sell-side**: **NO CGT in UAE** (zero personal income tax); **DLD transfer fee 4% (typically split 50/50 buyer/seller in practice though contract-defined)**; commission 2%+VAT; NOC fee from developer ~AED 5,000-10,000
- **Liquidity**: 🟢 HIGH Dubai prime (Marina/Downtown/Palm Jumeirah/Emirates Hills); 🟢 MEDIUM-HIGH Abu Dhabi investment zones; 🟠 MEDIUM Sharjah/RAK; 🔴 LOW interior emirates
- **Quirks**: **Off-plan pipeline ~70-100k units delivering 2025-2027** = oversupply risk in mid-tier Dubai; foreigners restricted to **freehold zones** (Dubai Designated Areas); leasehold elsewhere narrows resale pool; **Golden Visa (10-yr) for AED 2M+ property** sustains foreign demand; service charges (DLD-regulated) critical disclosure

### 🇮🇱 Israel
- **DOM**: Tel Aviv (Center/North TA/Ramat Gan) ~90-150 / Jerusalem 100-200 / Haifa 120-200 / Beersheba 150-300 / periphery longer
- **Commission**: **2% each side + 17% VAT (Ma'am)** typical (some 1.5-2% buyer; 2% seller)
- **Contract**: contract via עורך דין (orech din / lawyer-led) — both sides retain own attorney; Mas Rehisha (purchase tax) buyer-side
- **MLS**: no formal MLS; Yad2 + Madlan + WinWin
- **Discount**: 5-12% off asking; 2024-2026 conflict-cycle deeper in periphery
- **Sell-side**: **Mas Shevach (capital gains / appreciation tax)** — residents marginal sliding (typically 25%); **non-residents 25% on real gain (CPI-adjusted)** with potential 50% effective on certain pre-2003 acquisitions (linear method); single-residence exemption every 18 mo (residents); Bait Meshutaf (condominium) governance
- **Liquidity**: 🟢 MEDIUM-HIGH Tel Aviv center; 🟠 MEDIUM Jerusalem/Haifa; 🔴 LOW periphery / Negev / Galilee rural
- **Quirks**: **2023-2026 conflict cycle reshaped buyer pool** — diaspora demand strong but transaction friction higher; **Tabu (Israel Land Authority) leasehold (49+49 yrs)** vs freehold matters for resale; new property **Mas Rehisha tiers favour single-residence buyers** (foreign + multi-property heavily taxed); shekel volatility material to USD-buyer exit math

### 🇲🇦 Morocco
- **DOM**: Casablanca (Anfa/Maarif/Bourgogne) ~120-200 / Marrakech (Hivernage/Palmeraie) 150-300 / Rabat (Souissi/Agdal) 150-250 / Tangier 120-200
- **Commission**: 2.5% each side typical + 20% TVA; some seller-only at 3-5%
- **Contract**: contrat de courtage exclusive 3-6 mo; adoul (notarial witness) or notaire moderne for deed
- **MLS**: no MLS; Mubawab + Avito + Sarouty
- **Discount**: 10-20% off asking; Marrakech riad/medina deeper
- **Sell-side**: **TPI (Taxe sur les Profits Immobiliers) 20% on net gain**; minimum 3% of sale price (whichever higher); exempt if **primary residence held 6+ yrs**; commission 2.5%+TVA; conservation foncière 1% buyer-side
- **Liquidity**: 🟠 MEDIUM Casablanca prime / Marrakech expat zones; 🔴 LOW Rabat/Tangier/Agadir; VERY LOW medina/riad inventory
- **Quirks**: **Office des Changes mandatory for repatriation** of sale proceeds — without proper documentation of original FX import, foreign-seller proceeds locked in MAD; medina/riad properties often have **fragmented inheritance ownership** (multi-heir consent required); melk (private freehold) vs habous/collective land critical distinction — foreigners restricted from agricultural land

### 🇪🇬 Egypt
- **DOM**: Cairo (New Cairo/Sheikh Zayed/Maadi/Zamalek) ~120-300 / North Coast (Sahel) seasonal 90-300 / Hurghada/El Gouna 150-365+ / Alexandria 150-300
- **Commission**: 1-3% (informal market — often lower or absent); broker law nascent; +14% VAT where formal
- **Contract**: agency contracts informal; deed registration (shahr aqari) historically incomplete (<10% of properties registered as of 2020s reforms)
- **MLS**: no MLS; OLX Egypt + Aqarmap + Property Finder Egypt
- **Discount**: 15-30% off asking common (pricing fluid; EGP devaluation cycles)
- **Sell-side**: **Law 175/2023 imposes CGT 2.5% of GROSS sale price** (replacing prior 10% on gain regime — material change); commission 1-3%; deed registration fee 3% (capped EGP 2,000 historically); **Form 4 mandatory for USD repatriation** via banking channels — without Form 4 documentation of original USD import, exit proceeds in EGP only
- **Liquidity**: 🔴 LOW Cairo prime (compounds: Mivida, Palm Hills, Zamalek); VERY LOW everywhere else; coastal seasonal-only
- **Quirks**: **EGP devaluation (Mar 2024: ~50% vs USD; ongoing)** = catastrophic exit if Form 4 not filed at purchase — proceeds trapped in depreciating EGP; New Capital + North Coast oversupply 2020-2026; **most properties UNREGISTERED** (informal sales via contracts) narrowing financed-buyer pool; foreign ownership requires Prime Minister approval in some zones; remittance restrictions episodic during FX crises

## Sub-Saharan Africa

### 🇿🇦 South Africa
- **DOM**: Cape Town (Atlantic Seaboard/CBD/Southern Suburbs) ~60-120 / Johannesburg (Sandton/Rosebank/Houghton) 90-180 / Durban 120-200 / Pretoria 100-150
- **Commission**: **5-7.5% + 15% VAT (PPRA-regulated)** seller-side typical; net 5.75-8.625%
- **Contract**: sole mandate 90 d standard (PPRA-regulated since 2022)
- **MLS**: no MLS; Property24 + Private Property dominate
- **Discount**: 5-10% off asking; 2024-2026 closer to flat in Cape Town
- **Sell-side**: **CGT 40% inclusion rate on gain at marginal income tax** (effective max ~18% for individuals at 45% bracket); R2M primary-residence exemption per individual; **Section 35A 7.5% withholding on non-resident sellers (sale > R2M)** — withheld by buyer's conveyancer, remitted to SARS; commission 5-7.5%+VAT
- **Liquidity**: 🟢 HIGH Cape Town Atlantic Seaboard / City Bowl / Southern Suburbs (semigration magnet 2020-2026); 🟠 MEDIUM Sandton/Rosebank prime; 🔴 LOW Durban/Pretoria suburbs; VERY LOW rural
- **Quirks**: **"Semigration" northward-to-Cape-Town flow 2020-2026** = Cape Town outperforming JHB (top-end Atlantic Seaboard ZAR pricing diverging); **load-shedding** (electricity outages) drives backup-power premiums + accelerates emigration sales; **expropriation-without-compensation legislation (signed 2025)** politically narrow but material to international buyer perception; sectional title vs freehold distinction; rand volatility material to foreign-seller exit math

## Asia-Pacific

### 🇯🇵 Japan
- **DOM**: Tokyo 23-ku ~60-100 / Osaka ~80-120 / Kyoto ~100-150 / Sapporo/Fukuoka 90-150 / regional 150-365+ / akiya rural often unsellable
- **Commission**: **chukai tesuryo 仲介手数料 capped at 3% + JPY 60,000 + 10% consumption tax** (Takken-gyo Law) — typical structure: each side pays own agent (often same agency = both fees collected)
- **Contract**: 専任媒介契約 (senin baikai keiyaku) exclusive 3 mo standard; 14-day cooling-off
- **MLS**: **REINS (Real Estate Information Network System)** — broker-only MLS, mandatory listing for exclusive contracts; consumer-facing fragmented (SUUMO + HOMES + AtHome)
- **Discount**: 3-8% off asking Tokyo prime; rural deeper; akiya near-zero
- **Sell-side**: **CGT split: short-term <5 yrs = 39.63% (incl. local + recovery); long-term ≥5 yrs = 20.315%** (national 15% + local 5% + recovery surcharge); primary residence JPY 30M deduction; commission 3%+JPY 60k+CT each side
- **Liquidity**: 🟢 MEDIUM-HIGH Tokyo 23-ku prime (Minato/Shibuya/Chuo); 🟢 MEDIUM Osaka/Kyoto core; 🟠 MEDIUM Sapporo/Fukuoka; 🔴 LOW regional cities; VERY LOW akiya / rural
- **Quirks**: **Akiya (空き家 abandoned house) crisis** — ~9M vacant homes (2023 census), structural depopulation makes most rural inventory functionally unsellable; **JPY weakness 2022-2026 fuelled foreign-buyer demand** (Tokyo prime + Niseko ski) — material to USD-priced exit timing; building depreciation aggressive (wood ~22 yr, RC ~47 yr useful life for tax) compresses resale value vs land; earthquake compliance (Shin-Taishin 1981+ standard) gates buyer pool

### 🇹🇭 Thailand
- **DOM**: Bangkok (Sukhumvit/Sathorn/Silom) 60-120 / Phuket 90-180 / Chiang Mai 90-150 / Pattaya 120-250 / Hua Hin 120-200
- **Commission**: 3-5% seller-side typical + 7% VAT; up to 5-6% on luxury / longer hold
- **Contract**: agency agreement 3-6 mo; foreign condo quota 49% binding
- **MLS**: no MLS; DDproperty + Hipflat + FazWaz
- **Discount**: 10-20% off asking; Pattaya/Phuket secondary deeper
- **Sell-side**: **specific business tax 3.3% of sale price if held <5 yrs** (else stamp duty 0.5%); withholding tax sliding 0-35% on gain (corporate sellers different); transfer fee 2% (often split); **foreign sellers can repatriate via FET (Foreign Exchange Transaction) form** — required to bring USD in originally to repatriate cleanly
- **Liquidity**: 🟢 MEDIUM-HIGH Bangkok Sukhumvit/Sathorn/Silom (CBD); 🟠 MEDIUM Phuket/Chiang Mai/Hua Hin; 🔴 LOW Pattaya secondary; VERY LOW upcountry
- **Quirks**: **49% foreign-quota cap on condos** — buildings near cap mean future foreign buyer pool blocked; foreigners cannot own land freehold (leasehold 30yr+30yr or Thai-company structures); **FET form is THE document for clean USD repatriation** — without it, baht-only exit; oversupply Pattaya/Hua Hin from 2014-2019 buildout still digesting

### 🇮🇩 Indonesia
- **DOM**: Jakarta (Menteng/Kemang/SCBD) 120-300 / Bali (Seminyak/Canggu/Ubud) 150-365+ / Surabaya 200-365 / Yogyakarta/Bandung 200-365+
- **Commission**: 2-5% (Bali expat market 5%; Jakarta domestic 2-3%) + 11% PPN (VAT)
- **Contract**: hak pakai (right-to-use) for foreigners 30+20+30 yr; HGB for entities; agency contracts 3-6 mo
- **MLS**: no MLS; Rumah123 + Lamudi + 99.co
- **Discount**: 15-25% off asking; Bali seller's market closer to flat 2024-2026
- **Sell-side**: **PPh Final 2.5% of GROSS sale price** (seller-side, withheld at notary) — Indonesia uses gross-revenue tax for resi; BPHTB 5% buyer-side; commission 2-5%+PPN; **foreign-seller repatriation restricted to original investment + accrued returns** (Bank Indonesia documentation required)
- **Liquidity**: 🟠 MEDIUM Jakarta prime expat zones / Bali Canggu-Seminyak-Ubud foreign hotspots; 🔴 LOW Bali secondary villages; VERY LOW Surabaya/Yogya/Bandung secondary
- **Quirks**: **Foreigners CANNOT own freehold (Hak Milik)** — only Hak Pakai (use, 30+20+30 yr) or via HGB nominee structures (legally fraught); Bali villa boom 2020-2024 + zoning tightening 2024-2026 (governor moratorium discussions) reshape exit pool; **PPh 2.5% gross tax = punitive for low-margin sales** (loss-making sale still owes 2.5%); BI repatriation rules + LCS (local currency settlement) reforms ongoing

### 🇲🇾 Malaysia
- **DOM**: KL (KLCC/Bangsar/Mont Kiara) 90-180 / Penang (Georgetown/Tanjung Bungah) 120-200 / Johor Bahru 150-300 / Kota Kinabalu 120-250
- **Commission**: **2-3% seller-pays (Board of Valuers/MIEA capped at 3% for resi)** + 8% SST on services
- **Contract**: SPA (Sale & Purchase Agreement) standard; agency 3-6 mo
- **MLS**: no MLS; PropertyGuru + iProperty + EdgeProp
- **Discount**: 10-20% off asking; KL/JB oversupply deeper
- **Sell-side**: **RPGT (Real Property Gains Tax) — foreigners 10% PERMANENT regardless of holding period** (citizens: 30%/20%/15% sliding by year, 0% after 5+ yrs); commission 2-3%+SST; legal fees ~1%; stamp duty buyer-side
- **Liquidity**: 🟠 MEDIUM-LOW KL prime (KLCC/Bangsar/Mont Kiara) — chronic oversupply; 🔴 LOW Penang secondary; VERY LOW Johor Bahru (Forest City + JB oversupply); 🔴 LOW Sabah/Sarawak
- **Quirks**: **RPGT 10% permanent on foreign sellers = major exit drag** vs citizen 0% after 5 yrs (asymmetric tax structure narrows foreign buyer-then-seller economics); **MM2H program reformed Sep 2024** (lower thresholds vs 2021 reform) — foreign demand returning slowly; **MYR 1M minimum foreign purchase price** (state-by-state varies KL 1M, Penang 1M-2M, JB 2M); KL CBD oversupply persistent since 2017

### 🇻🇳 Vietnam
- **DOM**: HCMC (D1/D2/D7/Thu Duc) 120-300 / Hanoi (Hoan Kiem/Tay Ho/Cau Giay) 120-300 / Da Nang/Nha Trang coast seasonal 150-365 / secondary 200-365+
- **Commission**: **1-2% seller-side typical** (informal market); +10% VAT where formal; agents weakly regulated
- **Contract**: SPA via công chứng (notary); foreigners limited to 30% of units in apartment buildings, 50-yr leasehold (renewable)
- **MLS**: no MLS; Batdongsan + Cho Tot Nha + Alonhadat
- **Discount**: 10-25% off asking; 2024-2026 deeper post-corporate-bond crisis
- **Sell-side**: **transfer tax 2% of GROSS sale price** (seller-side); foreign sellers withheld at source; commission 1-2%+VAT; **foreign-seller repatriation requires SBV (State Bank of Vietnam) approval** — material friction
- **Liquidity**: 🔴 LOW HCMC D1/D2/Thu Duc prime; 🔴 LOW Hanoi prime; VERY LOW everywhere else; 2023-2026 corporate-bond + Evergrande-style developer crisis hit liquidity hard
- **Quirks**: **Foreigners limited to 30% of units per apartment building (50% for villas in restricted zones)** + 50-yr leasehold (renewable, but renewal not guaranteed) — fundamental exit constraint; **SBV repatriation approval = process risk** for foreign sellers; off-plan/pre-sale fraud cases frequent; Pink Book (Sổ Hồng) is the title document — verify chain; corporate-bond crisis 2022-2024 froze developer pipelines, oversupply digesting through 2026+

### 🇵🇭 Philippines
- **DOM**: Metro Manila (Makati/BGC/Ortigas) 120-250 / Cebu City 150-300 / Davao 200-365 / resort areas (Boracay/Palawan) 200-365+
- **Commission**: **3-5% seller-pays** typical (PRC-licensed brokers; PAREB) + 12% VAT
- **Contract**: Deed of Absolute Sale via notary; foreigners cannot own land (condo only, 40% foreign-quota cap)
- **MLS**: no MLS; Lamudi + Property24.com.ph + DotProperty
- **Discount**: 10-20% off asking; Manila condo oversupply deeper
- **Sell-side**: **CGT 6% of GROSS sale price OR zonal value (whichever higher)** — flat for residential; **DST (documentary stamp tax) 1.5%**; **LTT (local transfer tax) 0.5-0.75%** (Metro Manila 0.75%); commission 3-5%+VAT; total seller-side ~10-12% common
- **Liquidity**: 🔴 LOW Makati/BGC/Ortigas prime (oversupply 2020-2026); VERY LOW Cebu/Davao secondary; VERY LOW resort areas off-season
- **Quirks**: **Foreigners CANNOT own land** (1987 Constitution) — condo-only with 40% per-building cap; **Manila CBD condo oversupply 2020-2026** (POGO exodus + remote-work cooling); CGT 6% on GROSS sale price = punitive on low-margin / loss sales; **BSP repatriation documentation (registration of original FX inflow)** required for clean USD exit

### 🇸🇬 Singapore
- **DOM**: Districts 9/10/11 (Orchard / River Valley / Bukit Timah) ~30-60 / Districts 1/2/4 (Marina / Sentosa) ~45-90 / OCR (Outside Central Region) 60-120 / non-prime mass-market 90-150
- **Commission**: **2% seller-pays + 1% buyer-pays typical** (CEA-regulated); GST 9% on commission (Jan 2024 rate)
- **Contract**: exclusive estate-agency agreement 3-6 mo (CEA-regulated under EAA 2010)
- **MLS**: **partial MLS via CEA agent platforms (PropertyGuru + 99.co + EdgeProp)** — high portal transparency but no formal national MLS; URA private-residential transaction caveats publicly searchable
- **Discount**: 2-7% off asking; new launches narrower; prime resale closer to flat
- **Sell-side**: **NO CGT in SG**; **SSD (Seller's Stamp Duty) 4-12% sliding if sold within 3 yrs** of acquisition (residential); **ABSD applies on BUYER side** (60% non-resident, 30% PR, 20%/30% Singaporeans on 2nd/3rd home — Apr 2023 cooling-measure rates); commission 2%+GST seller-side
- **Liquidity**: 🟢 HIGH CCR (Districts 9/10/11) — global UHNW demand; 🟢 MEDIUM-HIGH RCR; 🟠 MEDIUM OCR mass-market; chronic structural undersupply on private resale; HDB resale has separate rules (eligibility-gated)
- **Quirks**: **ABSD 60% non-resident** (Apr 2023 cooling-measure) restructures any non-PR purchase economics; **Restricted Residential Property Act** bars foreigners from landed homes (strata/condo only without SLA approval); **HDB (public-housing 80% of stock)** has eligibility rules excluding non-residents; **English universal in admin/contracts**; SGD MAS-managed-float; **GST 9% Jan 2024** affects new-build pricing

### 🇭🇰 Hong Kong
- **DOM**: Mid-Levels / Pokfulam / Stanley / Repulse Bay (Hong Kong Island prime) ~60-120 / Tsim Sha Tsui / Mong Kok (Kowloon prime) 90-150 / NT (New Territories) 120-250 / outlying islands 200-365+
- **Commission**: **1% seller-pays + 1% buyer-pays typical** (EAA-regulated under Ord. Cap 511) — agency fees relatively low globally
- **Contract**: agency agreement 3-6 mo (EAA-licensed); preliminary agreement → formal sale-and-purchase via lawyer-led conveyance
- **MLS**: NO MLS; **Centaline / Midland / Ricacorp / Hong Kong Property** dominate listings + **EPRC transaction caveats** searchable via Land Registry
- **Discount**: 5-12% off asking 2024-2026 (post-correction); 2024 high-tide partial recovery
- **Sell-side**: **NO CGT for individuals** (Profits Tax doesn't apply to personal capital gains); **Special Stamp Duty (SSD) 10-20% sliding if sold within 36 months** of acquisition; commission 1%+VAT seller-side; legal fees ~0.1-0.2%
- **Liquidity**: 🟢 MEDIUM-HIGH HK Island prime + Kowloon prime; 🟠 MEDIUM Mid-Levels mass-market; 🔴 LOW NT/outlying; partial post-2020 expat-outflow recovery 2023-2026
- **Quirks**: **BSD 15% non-PR + AVD up to 4.25%** (partial cooling-measure rollback Oct 2023-2024 — verify per IRD); **CIES reactivated Mar 2024** (HK$30M + ≤HK$10M residential) opens investment-track residency; **Article 23 (NSL) Mar 2024 sentiment factor** for some buyers; HKD-USD peg LERS 7.75-7.85 (HKMA Convertibility Undertaking); English co-official; condo-style strata is the dominant tenure

### 🇰🇷 South Korea
- **DOM**: Seoul (Gangnam-gu / Seocho-gu / Yongsan-gu / Mapo-gu) ~60-120 / Bundang / Pangyo (GG) 90-180 / Busan (Haeundae / Suyeong) 120-250 / Daegu / Gwangju 150-300 / regional 200-365+
- **Commission**: **0.4-0.9% each side regulated sliding by price** (under Licensed Real Estate Agents Act — 공인중개사법; max 0.9% above ₩1.5B for residential as of 2024 schedule) + 10% VAT; one of the lowest globally
- **Contract**: 매매계약 (mae-mae gye-yak — purchase agreement) via licensed agent (공인중개사) + notary; 전세 (jeonse rental-deposit) separate
- **MLS**: no MLS; **Naver Real Estate (네이버 부동산) + Zigbang + Dabang + Hogangnono** dominate portals; **MOLIT 실거래가 (actual transaction prices)** publicly searchable — high price-history transparency
- **Discount**: 5-10% off asking 2024-2026 (post 2022-2023 correction); Gangnam prime narrower
- **Sell-side**: **CGT separate 6-45% sliding by gain + holding period**; **multi-home owners face 종부세 (comprehensive real estate tax) 0.5-5% annually** + **multi-home top CGT rate up to 75%** (post-2020 Moon-era reforms; partial Yoon-era rollback under negotiation 2024-2026 — verify NTS); commission 0.4-0.9%+VAT
- **Liquidity**: 🟢 MEDIUM-HIGH Seoul Gangnam-gu / Seocho-gu / Yongsan-gu (chronic undersupply prime); 🟢 MEDIUM Mapo-gu / Songpa-gu; 🟠 MEDIUM Bundang/Pangyo (tech-cluster); 🔴 LOW regional metros; VERY LOW rural; aging-society secondary-region demographic headwind
- **Quirks**: **Jeonse (전세) rental-deposit system** unique structural risk for renters (post-2022 HUG fraud-crisis reforms — Bali jaja jeonse fraud); **comprehensive real estate tax 종부세** is among the most progressive multi-home regimes globally; foreigners can buy via Foreigner's Land Acquisition Act notification (open to most nationalities); **gigabit fiber norm** (KT/SK/LG); cold winters; aging society

### 🇹🇼 Taiwan
- **DOM**: Taipei (Da'an / Xinyi / Zhongshan / Songshan) ~90-150 / Taipei (Neihu / Tianmu / Beitou) 100-180 / New Taipei (Banqiao / Xindian / Tamsui) 120-200 / Taoyuan / Hsinchu (Science Park) 100-180 / Taichung / Kaohsiung 150-250 / regional 200-365+
- **Commission**: **2% seller-pays + 1-2% buyer-pays typical (NOT capped)** + 5% VAT; market practice varies (some buyer-only)
- **Contract**: 不動產買賣契約書 (real-estate sale agreement) via licensed broker (不動產經紀人) + notary; **STR-style "actual price registration system" (實價登錄)** since 2012 reform makes prices public
- **MLS**: no MLS; **591房屋交易 + Yungching + Sinyi** dominate portals; **MOI Land 實價登錄 (actual price registration)** publicly searchable — high transparency
- **Discount**: 5-12% off asking 2024-2026
- **Sell-side**: **House and Land Transactions Income Tax (HLTIT, 房地合一稅 2.0)** post-Jul 2021 reform: 45% if held <2 yrs / 35% if 2-5 yrs / 20% if 5-10 yrs / 15% if >10 yrs (resident individuals; non-residents 45%/35%) — among the most progressive holding-period regimes globally; **Land Value Increment Tax (LVIT, 土地增值稅) seller-side** sliding 20-40% on land-value gain (separate from HLTIT); commission 2%+VAT
- **Liquidity**: 🟢 MEDIUM-HIGH Taipei Da'an / Xinyi / Zhongshan core (chronic undersupply prime); 🟢 MEDIUM Songshan / Neihu / Beitou; 🟠 MEDIUM New Taipei prime + Hsinchu Science Park; 🔴 LOW regional cities; aging-society secondary headwind
- **Quirks**: **Reciprocity-list-based foreign-buyer eligibility** — nationality determines eligibility (verify BOCA list per nationality); **2024 Hualien M7.4 earthquake** material to seismic disclosure (post-1999 921 Chi-Chi standards); **"actual price registration system" (實價登錄)** since 2012 reform = public price-history transparency unusual for the region; gigabit FTTH norm (Chunghwa, Taiwan Mobile); HSR + Taipei MRT

### 🇲🇴 Macao SAR
- **DOM**: Macao Peninsula (NAPE / ZAPE / São Lourenço) ~120-250 / Taipa (Taipa Grande / Taipa Pequena) 150-300 / Cotai 200-365+
- **Commission**: **1-2% each side typical** (informal practice; broker law nascent) + 5% VAT
- **Contract**: agency agreement 3-6 mo; deed registration via Conservatória do Registo Predial
- **MLS**: NO MLS; **Macao Property Holdings + agency-network listings** dominate; thin portal coverage
- **Discount**: 10-20% off asking 2024-2026 (post-correction; Cotai oversupply)
- **Sell-side**: **NO CGT on personal property gain**; **Special Stamp Duty (SSD) 5-20% if sold within 24 months** of acquisition (anti-speculation regime); deed registration ~3-6%; commission 1-2%
- **Liquidity**: 🟠 MEDIUM Macao Peninsula NAPE / ZAPE / São Lourenço prime; 🟠 LOW-MEDIUM Taipa; 🔴 LOW Cotai (oversupply); thin secondary market
- **Quirks**: **Investment Residence SUSPENDED since 2007** — no residency pathway via property; **Talent Programme 2024 NOT property-linked**; gaming ~50% GDP (concessões 2022 renewed 10yr) creates high cyclicality; MOP-HKD-USD double peg (HKMA-linked stability); ~673k pop; Cantonese + Portuguese co-official + English in tourism; **post-Hato 2017 storm-surge resilience reforms** (verify with DSAMA); UNESCO heritage zones overlay critical for refurbs

## Caucasus

### 🇬🇪 Georgia
- **DOM**: Tbilisi (Vake/Saburtalo/Vera) 60-120 / Batumi 90-180 (Russian + Iranian + Israeli demand) / regions 150-300+
- **Commission**: 3-5% seller-side typical (often split or buyer-pays in Batumi off-plan); 18% VAT only on services where applicable
- **Contract**: agency contracts informal; Public Service Hall (House of Justice) registration takes ~1-3 days
- **MLS**: no MLS; MyHome.ge + SS.ge dominate
- **Discount**: 5-15% off asking; off-plan Batumi narrower
- **Sell-side**: **NO CGT after 2-yr ownership** (residents and non-residents alike); <2 yrs taxed at 5% of gain (with documented basis) or 1.5-2% of sale price (without); **transaction costs ~0.1-0.5% (lowest in region)**; commission 3-5%
- **Liquidity**: 🟢 MEDIUM-HIGH Tbilisi Vake/Saburtalo/Vera (Russian + Israeli + diaspora demand 2022-2026); 🟠 MEDIUM Batumi (seasonal coastal + STR); 🔴 LOW regions
- **Quirks**: **Lowest friction in Eurasian region** — fast registration, no CGT after 2 yrs, foreigners can buy freehold (except agricultural land); **2022-2024 Russian relocation surge** drove Tbilisi prices up 40-60% (digesting 2025-2026); Batumi off-plan rental-pool deals often disappoint vs. marketed yields; foreign-buyer pool sensitive to regional geopolitics + Russian capital cycle

---

## Liquidity heatmap (4-tier composite)

| Tier | Countries |
|---|---|
| **HIGH** (DOM <60d, MLS/portal transparency, deep buyer pool) | NL, SE, NO, IE, UK (excl. chain), CA, AU, NZ, US (metros + Sun Belt), parts of ES (Madrid/BCN/Costa del Sol), PT (Lisbon/Porto/Algarve), DE top-7, CH (Zurich/Geneva), AE (Dubai prime), ZA (Cape Town Atlantic), **SG (CCR Districts 9/10/11)** |
| **MEDIUM** (DOM 60-150d) | FR (urban), IT (Milan/Rome), AT, BE (urban), DK, CZ, PL, HU (Budapest), HR coast, EE, LT, RO (Cluj/BUC), GR (Athens), CY (Limassol), MT, MX (CDMX/Riviera), TR (Istanbul prime), JP (Tokyo 23-ku), TH (Bangkok CBD), GE (Tbilisi), IL (Tel Aviv), CO (Medellín/Bogotá), CL (Santiago prime), UY (Montevideo), **HK (HK Island prime + Kowloon prime)**, **KR (Seoul Gangnam-gu / Seocho-gu / Yongsan-gu)**, **TW (Taipei Da'an / Xinyi / Zhongshan)**, **MC (Monte-Carlo / La Condamine / Larvotto)**, **AD (Andorra la Vella ski-zone seasonal)** |
| **LOW** (DOM 150-300d, thin pool) | LU, FI, IS, SK, SI, LV, BG, RS, ME interior, MK, AL, BA Sarajevo, BR (secondary), CR, PA, AR (BA prime — cash-only LOW), DO (interior/off-peak), MA (Casablanca/Marrakech), MY (KL/Penang), VN (HCMC/Hanoi prime), PH (Manila prime), ID (Jakarta/Bali secondary), JP (regional), TH (Pattaya), IL (periphery), **MO (Macao Peninsula prime)**, **MD (Chișinău Centru / Botanica)**, **AD (parish villages off-season)** |
| **VERY LOW** (DOM 300+d, illiquid) | Rural FR / IT South / ES inland / BG Black Sea overhang / HU rural east / BA rural / AL rural / Northern FI / Latgale LV / AR (everywhere ex-BA), BR rural, CR rural, PA Bocas/interior, JP akiya / regional, MY Sabah/Sarawak, VN secondary, PH Cebu/Davao, EG (everywhere ex-Cairo prime), MA medina/riad illiquid, ZA rural, ID Surabaya/Yogya, **LI (tiny ~40k market with quota residency)**, **MO (Cotai oversupply)**, **MD (rural / Bălți)**, **TW (regional / aging-society secondary)**, **KR (regional / aging-society secondary)** |

## Key cross-country patterns

1. **True MLS exists in NL (Funda), CA (CREA Realtor.ca), US (~580 regional MLSs), JP (REINS, broker-only)** — everywhere else is portal-driven (Hemnet/Finn/Domain are MLS-equivalent in transparency but not formally MLS); **TW 實價登錄 (actual price registration system, since 2012)** + **KR MOLIT 실거래가** + **HK Land Registry EPRC** + **SG URA caveats** offer high price-history transparency without formal MLS
2. **"Both-sides-pay" commission** structure: IT, DE (post-2020), PL, RO, BG, HR, GR, RS, BA, AL, AR, CA, TR, IL, MA, UY, CL, **MC, MO, SG (1+2 split), HK (1+1), TW (2+1-2)** — material to net-proceeds modelling. **US shifting** post-NAR settlement Aug 2024 (buyer-agent commissions unbundled)
3. **Energy/EPC labels are now liquidity gates** in FR (DPE), DE (GEG), BE-Flanders, NL, UK (EPC), IT (APE) — F/G class properties face collapsing buyer pools
4. **Foreign-seller withholding** is a material exit cost in: **US (FIRPTA 15% gross)**, **ZA (Section 35A 7.5% on sale > R2M)**, **DO (27% gross)**, **ES (3% retention)**, **PT (28% non-res rate)**, **IL (25% Mas Shevach)**, **MY (RPGT 10% permanent)** — model into net-proceeds
5. **Foreign-buyer bans/restrictions** narrowing exit pool: CA (to 2027), AU (established to 2027), NZ (perm), MX (fideicomiso), AT (Tyrol/Salzburg/Vorarlberg quotas), CH (Lex Koller), MT (AIP outside SDA), HR (10-yr lock on agri non-EU), **TH (49% condo cap)**, **PH (no land for foreigners, 40% condo cap)**, **VN (30% per building, 50-yr leasehold)**, **ID (Hak Pakai only — no freehold for foreigners)**, **MY (state-by-state minimum thresholds)**, **AE (freehold only in Designated Areas)**, **SG (Restricted Residential Property Act — no landed homes for foreigners + ABSD 60% non-resident)**, **LI (Lex-Koller-equivalent + EEA-only + quota residency ~28+17/year)**, **MD (agricultural land foreign-restricted; Transnistria-scope excluded)**, **TW (reciprocity-list-based — verify BOCA list)**
6. **Cadastral/title issues** are the binding sellability constraint in AL (#1), BA, RS rural, MK rural, IT South borgo, ES rural inland, RO restitution residue, BG rural, MX ejido, **EG (~90% unregistered)**, **MA medina/riad multi-heir**, **VN Pink Book chain verification** — clean title is worth more than price-cutting
7. **Seasonal-only liquidity**: ME coast, HR Adriatic, GR islands, BG Black Sea, CR Guanacaste, MX Riviera, PT Algarve, IS countryside, AT/CH alpine, **UY Punta del Este (Dec-Feb)**, **EG North Coast (Sahel)**, **TH Phuket/Pattaya**, **JP Niseko**
8. **Bidding-up cultures** (sale > asking): NL, SE, NO, IE, UK pre-2024, AU auction states, CA (2021-2022 peak), **US Sun Belt 2021-2022 peak**
9. **Chain risk** unique to UK; **co-op approval** unique to SE bostadsrätt, FI asunto-osakeyhtiö, DK andelsbolig
10. **CGT primary-residence exemption is universal** in EU/UK/Anglo (with conditions); the differentiator is **non-resident treatment** — ES/PT/FR/IT/UK/AU/CA/US all have non-resident withholding or higher rates
11. **GROSS-revenue CGT regimes** (tax on sale price, not gain) — punitive on low-margin / loss sales: **EG (2.5% Law 175/2023)**, **PH (6% CGT)**, **ID (PPh Final 2.5%)**, **VN (2% transfer)**, **TH (3.3% SBT if <5 yrs)** — material vs net-gain regimes elsewhere
12. **FX repatriation friction** (foreign sellers): **EG Form 4** (without it: EGP-only exit during devaluation = catastrophic), **MA Office des Changes**, **VN SBV approval**, **ID Bank Indonesia documentation**, **TH FET form**, **PH BSP registration**, **ID restricted to original investment + accrued** — must verify at PURCHASE for clean exit
13. **No-CGT zones**: **AE (no personal income tax)**, **GE (after 2 yrs)**, **DK primary residence**, **GR (suspended through 2026)**, **SG (no CGT — but SSD 4-12% if <3 yrs)**, **HK (no CGT for individuals — but SSD 10-20% if <36 months)**, **MO (no CGT — but SSD 5-20% if <24 months)**, **MC (no PIT/CGT)** — material to exit timing
14. **Earthquake / seismic disclosure** material to exit: **JP (Shin-Taishin 1981+ standard)**, **TR (post-Feb 2023 Kahramanmaraş)**, **NZ Wellington apartments**, **CL (post-2010 Maule)**, **TW (post-2024 Hualien M7.4 + post-1999 921 Chi-Chi standards)**

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

Last refreshed: 2026-05-01. 9 Tier-3 countries added (SG, HK, KR, TW, MO, LI, MC, AD, MD) — total 71 countries (Tier-1: US, TR, AE, JP, TH, DO, CO, UY, CL, ZA; Tier-2: GE, ID, MY, VN, PH, IL, MA, EG; Tier-3: SG, HK, KR, TW, MO, LI, MC, AD, MD).
