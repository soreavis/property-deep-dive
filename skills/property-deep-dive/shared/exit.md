# Universal `--exit` Section

Sell-side conditions: time-on-market (DOM), agent commission structure, contract norms, off-market vs MLS, sell-side closing costs, liquidity rating. Buyers should understand how easy it will be to **exit** a property before committing to buy.

**Snapshot**: April 2026.

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

---

## Liquidity heatmap (4-tier composite)

| Tier | Countries |
|---|---|
| **HIGH** (DOM <60d, MLS/portal transparency, deep buyer pool) | NL, SE, NO, IE, UK (excl. chain), CA, AU, NZ, parts of ES (Madrid/BCN/Costa del Sol), PT (Lisbon/Porto/Algarve), DE top-7, CH (Zurich/Geneva) |
| **MEDIUM** (DOM 60-150d) | FR (urban), IT (Milan/Rome), AT, BE (urban), DK, CZ, PL, HU (Budapest), HR coast, EE, LT, RO (Cluj/BUC), GR (Athens), CY (Limassol), MT, MX (CDMX/Riviera) |
| **LOW** (DOM 150-300d, thin pool) | LU, FI, IS, SK, SI, LV, BG, RS, ME interior, MK, AL, BA Sarajevo, BR (secondary), CR, PA, AR (BA prime — cash-only LOW) |
| **VERY LOW** (DOM 300+d, illiquid) | Rural FR / IT South / ES inland / BG Black Sea overhang / HU rural east / BA rural / AL rural / Northern FI / Latgale LV / AR (everywhere ex-BA), BR rural, CR rural, PA Bocas/interior |

## Key cross-country patterns

1. **Only NL (Funda) and CA (CREA Realtor.ca) have true MLS** — every other market is portal-driven (Hemnet/Finn/Domain are MLS-equivalent in transparency but not formally MLS)
2. **"Both-sides-pay" commission** structure: IT, DE (post-2020), PL, RO, BG, HR, GR, RS, BA, AL, AR, CA — material to net-proceeds modelling
3. **Energy/EPC labels are now liquidity gates** in FR (DPE), DE (GEG), BE-Flanders, NL, UK (EPC), IT (APE) — F/G class properties face collapsing buyer pools
4. **Foreign-buyer bans/restrictions** narrowing exit pool: CA (to 2027), AU (established to 2027), NZ (perm), MX (fideicomiso), AT (Tyrol/Salzburg/Vorarlberg quotas), CH (Lex Koller), MT (AIP outside SDA), HR (10-yr lock on agri non-EU)
5. **Cadastral/title issues** are the binding sellability constraint in AL (#1), BA, RS rural, MK rural, IT South borgo, ES rural inland, RO restitution residue, BG rural, MX ejido — clean title is worth more than price-cutting
6. **Seasonal-only liquidity**: ME coast, HR Adriatic, GR islands, BG Black Sea, CR Guanacaste, MX Riviera, PT Algarve, IS countryside, AT/CH alpine
7. **Bidding-up cultures** (sale > asking): NL, SE, NO, IE, UK pre-2024, AU auction states, CA (2021-2022 peak)
8. **Chain risk** unique to UK; **co-op approval** unique to SE bostadsrätt, FI asunto-osakeyhtiö, DK andelsbolig
9. **CGT primary-residence exemption is universal** in EU/UK/Anglo (with conditions); the differentiator is **non-resident treatment** — ES/PT/FR/IT/UK/AU/CA all have non-resident withholding or higher rates

## Anti-hallucination

- **DOM is broker-aggregated** — verify per-transaction in 2-3 local agents per micro-market
- **Sparse-data flag**: Balkans + LatAm have no central HPI registry comparable to EU stat offices
- **Don't conflate auction "passed-in"** (no sale) with sale at reserve
- **Currency mismatch** for foreign-priced markets (CR/PA/AR USD; LU EUR with FR/DE/BE buyer cycles)

## Status

Last refreshed: 2026-04-26.
