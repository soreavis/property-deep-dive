# Crime Data Sources — Universal Section `--crime`

The `--crime` section pulls **commune-level crime statistics** for the property's locality.

Unlike amenities (universal via OSM), crime data is country-specific because each national police force or statistics office publishes differently. This file is the registry of **per-country crime data sources**.

## Universal contract for `--crime`

For the property's locality, return:
1. **Population-normalised crime rate** per 1,000 inhabitants (or 100k where conventional)
2. **Trend** (increasing / stable / decreasing) — last 5 years if available
3. **Breakdown** by category (property crime, violent crime, burglary, vehicle theft, etc.)
4. **Comparison vs national + regional average**
5. **Walking-around safety** caveat (data ≠ feeling; subjective wisdom matters)
6. **Confidence** label

## Output template

```markdown
## Crime & Safety

**Locality**: <commune/city/Stadt>, <region>
**Population**: <pop>
**Data year**: <YYYY> (latest published)
**Source**: <national/regional police statistics or stat office>

### Headline metrics

| Metric | This locality | National avg | Regional avg | Trend (5yr) |
|---|---:|---:|---:|---|
| Total crimes / 1,000 hab | <X> | <Y> | <Z> | ↑↓→ |
| Property crime / 1,000 | <X> | <Y> | <Z> | ↑↓→ |
| Burglary / 1,000 | <X> | <Y> | <Z> | ↑↓→ |
| Violent crime / 1,000 | <X> | <Y> | <Z> | ↑↓→ |
| Vehicle theft / 1,000 | <X> | <Y> | <Z> | ↑↓→ |

### Verdict
- 🟢 below national average across all categories
- 🟡 mixed: some categories elevated
- 🟠 noticeably above average for category X
- 🔴 significantly above national average; flagged for due diligence

### Walking-around safety
<one-line qualitative note from local sources/forums>

### Confidence
<HIGH | MEDIUM | LOW> — <one-sentence justification>

### Sources
- <Primary national police statistics URL>
- <Regional / commune-level data if applicable>

⚠️ **Caveats**: 
- Crime statistics reflect *recorded* offences; under-reporting varies by category
- Tourist destinations often have inflated rates (transient population)
- Rural communes have small absolute numbers (statistical noise)
```

## Per-country crime data sources

### 🇫🇷 France

- **Ministère de l'Intérieur — Service Statistique Ministériel de la Sécurité Intérieure (SSMSI)**:
  - Portal: `https://www.interieur.gouv.fr/Interstats/`
  - Open data: `https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales/`
  - **Commune-level CSV available** (with caveats for small communes — censored < 5 cases)
- **ONDRP** (Observatoire National de la Délinquance et des Réponses Pénales) — historical
- **CSI 2022/2023 (Cadre Statistique Interministériel)** new methodology

### 🇮🇹 Italy

- **ISTAT delitti denunciati**: `https://www.istat.it/it/violenza-sulle-donne` + general crime
- **Ministero dell'Interno**: `https://www.interno.gov.it/` for sicurezza
- **Polizia di Stato + Carabinieri** statistics by provincia
- **Sole24Ore Indice Qualità della Vita** annually publishes provincia rankings incl. sicurezza

### 🇨🇿 Czech Republic

- **Policie ČR Mapy zločinu**: `https://mapakriminality.cz/` — interactive map per ORP/obec
- **ČSÚ Kriminalita**: `https://csu.gov.cz/`
- Per-okres + obec data; updated quarterly

### 🇸🇰 Slovakia

- **Štatistický úrad SR — Demography/Justice indicators (most reliable)**: `https://slovak.statistics.sk/wps/portal/ext/themes/demography/justice/indicators/`
- **Ministerstvo vnútra SR — Polícia (homepage; statistics tab JS-rendered)**: `https://www.minv.sk/`
- **Štatistický úrad SR Kriminalita**: `https://www.statistics.sk/`
- Per-okres + per-obec data

### 🇩🇪 Germany

- **BKA Polizeiliche Kriminalstatistik (PKS)** — annual national report: `https://www.bka.de/DE/AktuelleInformationen/StatistikenLagebilder/PolizeilicheKriminalstatistik/pks_node.html`
- Per-Bundesland LKA reports
- **Berlin Sicherheitsatlas, München Sicherheitsbericht** city-level
- **Stadtstatistik / Open Data per major city**

### 🇦🇹 Austria

- **BMI Sicherheitsbericht**: `https://www.bmi.gv.at/304/files/Sicherheitsbericht.aspx`
- **Statistik Austria Kriminalstatistik**: `https://www.statistik.at/`
- Per-Bezirk + Bundesländer; annual

### 🇨🇭 Switzerland

- **BFS Polizeiliche Kriminalstatistik (PKS-CH)**: `https://www.bfs.admin.ch/bfs/de/home/statistiken/kriminalitaet-strafrecht.html`
- Annual federal report; per-canton + per-Gemeinde data
- Federal + 26 cantonal police forces — combined PKS

### 🇪🇸 Spain

- **INE Estadísticas de Criminalidad**: `https://www.ine.es/`
- **Ministerio del Interior — Anuario Estadístico**: `https://www.interior.gob.es/opencms/es/archivos-y-documentacion/documentacion-y-publicaciones/anuarios-y-estadisticas/anuarios-estadisticos-anteriores/`
- Per-CCAA + provincia + municipio
- **Mossos d'Esquadra** (Cataluña), **Ertzaintza** (País Vasco) separate

### 🇵🇹 Portugal

- **INE Estatísticas da Justiça e Segurança**: `https://www.ine.pt/`
- **PSP / GNR + Sistema de Segurança Interna (SSI)** annual report — RASI: `https://www.portugal.gov.pt/`
- **Pordata Segurança e Justiça**: `https://www.pordata.pt/portugal/seguranca+e+justica`

### 🇸🇪 Sweden

- **Brå (Brottsförebyggande rådet) — Kriminalstatistik**: `https://www.bra.se/statistik.html`
- **Polisen.se** monthly local reports
- Per-kommun data + neighbourhood-level for major cities

### 🇫🇮 Finland

- **Tilastokeskus Rikostilastot**: `https://stat.fi/til/rpk/index.html`
- **Poliisi statistics**: `https://poliisi.fi/`
- Per-kunta data; quarterly updates

### 🇳🇴 Norway

- **SSB Kriminalstatistikk**: `https://www.ssb.no/sosiale-forhold-og-kriminalitet/kriminalitet-og-rettsvesen/`
- **Politiet.no** local reports per district
- Per-kommune data

### 🇩🇰 Denmark

- **Danmarks Statistik (DST) Kriminalitet**: `https://www.dst.dk/da/Statistik/emner/sociale-forhold/kriminalitet`
- **Politi.dk** statistics
- Per-kommune + sogn

### 🇮🇸 Iceland

- **Hagstofa Íslands Sakamál**: `https://hagstofa.is/`
- **Lögreglan** national police statistics
- Small population means absolute numbers volatile; trends per region

### 🇳🇱 Netherlands

- **CBS Statline Misdaadstatistiek**: `https://www.cbs.nl/`
- **Politie.nl** maandcijfers per gemeente
- Per-gemeente + buurt-level for major cities

### 🇧🇪 Belgium

- **StatBel Délinquance / Criminaliteit**: `https://statbel.fgov.be/`
- **Police fédérale Statistiques**: `https://www.stat.policefederale.be/`
- Per-arrondissement + commune

### 🇬🇧 United Kingdom

- **police.uk Crime maps**: `https://www.police.uk/` — **best-in-class** address-level crime data
- **ONS Crime in England and Wales**: `https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice`
- Per-LSOA + neighbourhood; postcode lookup

### 🇮🇪 Ireland

- **CSO Recorded Crime**: `https://www.cso.ie/`
- **Garda Síochána statistics**: `https://www.garda.ie/`
- Per-Garda Division (regional)

### 🇸🇮 Slovenia

- **SURS Kriminaliteta**: `https://www.surs.si/`
- **Policija statistics**: `https://www.policija.si/`
- Per-policijska postaja

### 🇬🇷 Greece

- **Hellenic Police (ELAS, ΕΛ.ΑΣ.)**: `https://www.astynomia.gr/?lang=en` — annual crime reports
- **Hellenic Statistical Authority (ELSTAT) — Justice & Crime statistics**: `https://www.statistics.gr/en/statistics/-/publication/SJU03/-` — published per perifereia + nomos (region + prefecture)
- **Ministry of Citizen Protection (Υπουργείο Προστασίας του Πολίτη)**: annual security reports
- Press contact: `press@hellenicpolice.gr`
- **Granularity**: per-perifereia routine; per-dimos (municipality) only for major cities (Athens, Thessaloniki, Piraeus); rural communes typically aggregated
- **Caveat**: tourist islands inflated due to transient population (denominator mismatch); flag for Mykonos, Santorini, Rhodes, Crete coast

### 🇲🇽 Mexico

- **SESNSP (Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública)**: `https://www.gob.mx/sesnsp` — monthly municipal-level crime statistics
- **INEGI ENVIPE** (Encuesta Nacional de Victimización y Percepción): victim survey
- **Granularity**: per-estado + per-municipio
- **Caveat**: dark figure (cifra negra) very high in MX (~93% unreported); rely on victim survey + homicide data (most reliable)
- **2025 reference**: ~24 homicides per 100k national; Colima/Zacatecas/Guanajuato highest; Yucatán/Campeche lowest

### 🇧🇷 Brazil

- **Atlas da Violência (IPEA + FBSP)**: `https://www.ipea.gov.br/atlasviolencia/` — annual data
- **Anuário Brasileiro de Segurança Pública (FBSP)**: `https://forumseguranca.org.br/anuario-brasileiro-de-seguranca-publica/`
- **SINESP** (Sistema Nacional de Informações de Segurança Pública)
- **State SSP** (Secretaria de Segurança Pública) per state — São Paulo SSP best data
- **Granularity**: per-estado + per-município + bairro for major cities
- **Caveat**: state methodology varies; SP, RJ, MG most rigorous

### 🇦🇷 Argentina

- **Sistema Nacional de Información Criminal (SNIC)**: `https://www.argentina.gob.ar/seguridad/estadisticascriminales`
- **Provincial police** (Policía de la Ciudad CABA, Bonaerense PBA, Mendoza, etc.)
- **CABA Estadísticas**: city-level data
- **Granularity**: per-province + CABA (district-level)
- **Caveat**: under-reporting common; provincial divergence in methodology

### 🇨🇷 Costa Rica

- **OIJ (Organismo de Investigación Judicial)**: `https://oij.poder-judicial.go.cr/` — annual statistics
- **Ministerio de Seguridad Pública**: `https://www.seguridadpublica.go.cr/`
- **INEC Encuesta de Victimización** — victim survey
- **Granularity**: per-province + per-cantón
- **Caveat**: Limón Caribbean coast typically highest; Pacific tourist zones inflated by transient pop

### 🇵🇦 Panama

- **MINGOB (Ministerio de Gobierno)** crime stats: `https://www.mingob.gob.pa/`
- **Policía Nacional**: `https://www.policia.gob.pa/`
- **INEC Estadísticas Sociodemográficas**
- **Granularity**: per-province + per-distrito
- **Caveat**: Panama City + Colón higher than rural; expat zones (Boquete, Coronado) generally low

### 🇷🇸 Serbia

- **Republički Zavod za Statistiku (RZS) — Statistika kriminaliteta**: `https://www.stat.gov.rs/`
- **MUP (Ministarstvo unutrašnjih poslova)**: `https://www.mup.gov.rs/`
- **Granularity**: per-okrug (district) + per-municipality
- **Caveat**: under-reporting common; methodology aligned with EU since candidacy

### 🇲🇪 Montenegro

- **MONSTAT — Statistika kriminaliteta**: `https://www.monstat.org/`
- **Uprava policije**: `https://www.uprava.gov.me/`
- **Granularity**: per-opština (25 municipalities)
- **Caveat**: tourist transient population inflates rates Adriatic Jul-Aug

### 🇧🇦 Bosnia & Herzegovina

- **BHAS (Agencija za statistiku BiH)**: `https://www.bhas.ba/`
- **Entity-level police**: MUP FBiH + MUP RS entity + Brčko District police
- **Granularity**: per-entity + per-canton (FBiH) + per-opština
- **Caveat**: dual-entity methodology divergence; war-legacy reporting variable

### 🇲🇰 North Macedonia

- **MAKSTAT (Drzaven zavod za statistika) — Pravosudna i kriminalna statistika**: `https://www.stat.gov.mk/`
- **MVR (Ministerstvo za vnatresni raboti)**: `https://www.mvr.gov.mk/`
- **Granularity**: per-region + per-municipality + Skopje sub-municipalities
- **Caveat**: small population = small absolute numbers

### 🇦🇱 Albania

- **INSTAT — Statistikat e Krimit**: `https://www.instat.gov.al/`
- **Policia e Shtetit**: `https://www.policiaeshtetit.gov.al/`
- **Granularity**: per-qark (12 counties) + per-bashki
- **Caveat**: tourist transient inflates Vlorë + Sarandë; under-reporting common

### 🇨🇦 Canada

- **Statistics Canada — Police-reported crime statistics**: `https://www150.statcan.gc.ca/n1/pub/85-002-x/2024001/article/00010-eng.htm` — annual Juristat publication, Uniform Crime Reporting Survey (UCR)
- **Statistics Canada Crime Severity Index (CSI)**: per CMA + per province
- **Police-reported crime data tables**: open-data downloads
- **Provincial / municipal portals** (e.g., Toronto Police Open Data, VPD Crime Map)
- **Granularity**: per-CMA + per-province + city; Toronto and Vancouver have neighbourhood-level
- **Caveat**: methodology stable; CSI weights different offence types

### 🇦🇺 Australia

- **Australian Bureau of Statistics (ABS) — Recorded Crime, Victims**: `https://www.abs.gov.au/statistics/people/crime-and-justice/recorded-crime-victims-australia` — annual victim-survey + administrative data
- **State police statistics**: NSW BOCSAR `https://www.bocsar.nsw.gov.au/`, Crime Statistics Agency Victoria `https://www.crimestatistics.vic.gov.au/`, QPS QLD
- **Granularity**: per-state + LGA + suburb; NSW BOCSAR has best LGA-level data
- **Caveat**: state methodology divergence; NSW BOCSAR most rigorous

### 🇳🇿 New Zealand

- **NZ Police "Crime Snapshot"**: `https://www.police.govt.nz/about-us/publication/crime-snapshot`
- **Stats NZ Justice + Crime publications**: `https://www.stats.govt.nz/topics/justice-and-crime`
- **Granularity**: per-region + meshblock; Police "By the numbers" provides territory-level
- **Caveat**: small national pop = small absolute numbers; per-capita most useful

### 🇪🇪 Estonia

- **Statistikaamet (Statistics Estonia) crime publications**: `https://stat.ee/en/find-statistics/statistics-theme/social-life`
- **Politsei- ja Piirivalveamet (PPA)**: `https://www.politsei.ee/en` — annual reports
- **Justiitsministeerium (Ministry of Justice)** — crime overview reports
- **Granularity**: per-maakond (county) + Tallinn district-level for capital
- **Caveat**: methodology aligned with EU; small population = high variance

### 🇭🇷 Croatia

- **Ministarstvo unutarnjih poslova (MUP)**: `https://mup.gov.hr/statistika/283222` — annual police crime statistics
- **Državni zavod za statistiku (DZS)**: `https://podaci.dzs.hr/` — Pravosuđe (justice) statistics
- **Granularity**: per-županija (county) + per-policijska uprava (police district)
- **Caveat**: tourism transient population inflates rates Adriatic Jul-Aug

### 🇭🇺 Hungary

- **KSH (Hungarian Central Statistical Office)**: `https://www.ksh.hu/stadat?lang=en&theme=igs` — Ig (Justice + Crime)
- **ENYÜBS (Egységes Nyomozó Hatósági és Ügyészségi Bűnügyi Statisztika)**: unified investigation/prosecution statistics
- **Belügyminisztérium (Ministry of Interior)** annual crime overview
- **Granularity**: per-megye (county) + Budapest district + main cities
- **Caveat**: ENYÜBS counts cases; multiple-victim offenses may inflate

### 🇵🇱 Poland

- **KGP Statystyka (Komenda Główna Policji portal)**: `https://statystyka.policja.pl/` — primary crime statistics portal
  - Per-województwo (16) + per-powiat (380) + per-gmina granular data
  - Annual + quarterly updates
  - Categories: kradzież, kradzież z włamaniem, rozbój, uszkodzenie rzeczy, bójka i pobicie, zabójstwo, pedofilia
- **Komenda Stołeczna Policji** (Warsaw): `https://ksp.bip.policja.gov.pl/ksp/statystyki` — full monthly catalogue
- **Per-city KMP** (Komenda Miejska Policji), e.g., Gdańsk: `https://gdansk.policja.gov.pl/pm1/informacje/statystyki/`
- **GUS (Główny Urząd Statystyczny)**: `https://stat.gov.pl/` — Bezpieczeństwo publiczne i sądownictwo
- **2024 reference**: ~440,000 total crimes; -30k common crimes vs 2023; homicides 503 (was 565); shoplifting -24.7%
- **Granularity**: per-województwo + per-powiat well-published; per-gmina via local KMP
- **Caveat**: methodology stable; 2017 + 2020 reforms minor

### 🇱🇹 Lithuania

- **Informatikos ir ryšių departamentas (ITKD) — Police**: `https://www.ird.lt/` — primary crime statistics portal
- **Statistics Lithuania (OSP)**: `https://osp.stat.gov.lt/` — Crime tables; bot-blocked on HEAD, browser-OK
- **Granularity**: per-apskritis (county) + per-savivaldybė (municipality) + Vilnius/Kaunas/Klaipėda district-level
- **Caveat**: post-2022 RU/BY-buyer dynamics affect Klaipėda + border-zone reporting

### 🇱🇻 Latvia

- **Iekšlietu ministrija (MoI) — Valsts policija (State Police)**: `https://www.vp.gov.lv/` — primary crime portal
- **CSP (Central Statistical Bureau)**: `https://stat.gov.lv/en` — crime / justice tables
- **Granularity**: per-statistical-region (Riga / Pierīga / Vidzeme / Kurzeme / Zemgale / Latgale) + per-novads (municipality)
- **Caveat**: Latgale (E border) Russian-speaking-majority districts have different demographics; do not over-interpret regional-only data

### 🇷🇴 Romania

- **Inspectoratul General al Poliției Române (IGPR)**: `https://www.politiaromana.ro/` — annual crime statistics, by județ (county) + main cities
- **INS (Institutul Național de Statistică)**: `https://www.insse.ro/` — Justiție și criminalitate tables
- **AMCCRS Bucharest seismic + crime overlay** (informal): https://www.hartablocuri.ro/ — community-augmented map (year of construction + crime hot-spots)
- **Granularity**: per-județ (42) + Bucharest sectors (1-6) + main cities
- **Caveat**: Bucharest sector-level data is the de-facto granularity for capital; rural commune data often suppressed

### 🇧🇬 Bulgaria

- **MVR (Ministry of Interior)**: `https://www.mvr.bg/` — primary crime data
- **NSI (Statistical Institute)**: `https://www.nsi.bg/en/` — Public order and security
- **Granularity**: per-oblast (28 provinces) + main cities + Sofia districts
- **Caveat**: Black Sea coast resort municipalities (Nesebar, Sozopol, Pomorie, Varna, Burgas) inflate rates seasonally; Sofia districts vary substantially (Ovcha kupel/Lyulin vs central)

### 🇱🇺 Luxembourg

- **Police Grand-Ducale**: `https://police.public.lu/` — annual statistics + transparency portal
- **STATEC**: `https://statistiques.public.lu/` — Délinquance et sécurité tables
- **Granularity**: per-circonscription de police + per-commune (102) + Luxembourg City quarters
- **Caveat**: Luxembourg City Gare district has elevated rates; cross-border commuter dynamic affects daytime vs resident-population denominator

### 🇨🇾 Cyprus

- **Cyprus Police**: `https://www.police.gov.cy/police/police.nsf/cyens.aspx` — annual crime report
- **CyStat**: `https://www.cystat.gov.cy/` — Justice and security
- **Granularity**: per-district (Lefkosia / Lemesos / Larnaka / Pafos / Famagusta-RoC) + main cities
- **Caveat**: Limassol Russian/CIS HNW concentration affects financial-crime + IT/cyber categories; tourist-zone Ayia Napa/Paralimni inflates summer rates; **TRNC/north not covered by RoC police statistics**

### 🇲🇹 Malta

- **Malta Police Force**: https://pulizija.gov.mt/en/ — crime statistics
- **NSO (National Statistics Office)**: https://nso.gov.mt/ — Crime and Justice tables
- **Granularity**: per-district (NSO Districts 1-6: Southern Harbour / Northern Harbour / South Eastern / Western / Northern / Gozo and Comino) + per-locality (68)
- **Caveat**: Sliema/St Julians/Paceville cluster has elevated theft-from-person + drug-related events; Marsa/Hamrun migrant-services hub elevated petty theft; Gozo materially lower across all categories

## Universal extraction approach

For each country, the workflow:

1. **Get latest year** from the national portal
2. **Look up commune/locality**:
   - National stat portal → search by commune name + administrative code (INSEE / comune ID / kommune ID / etc.)
   - If small commune (< 1,000 inhabitants), often suppressed — use the **next-larger admin unit** (canton / district / okres)
3. **Compute rate**: divide raw count by population × 1,000 (or 100,000 for serious crime)
4. **Compare**:
   - National average from same source
   - Regional average from same source
5. **Trend**: pull last 5 years if available; report direction
6. **Output** per universal template

## Caveats to surface in every report

- **Recorded vs actual**: under-reporting varies by category (sexual offences, minor theft) and country
- **Tourist destinations** often look "high crime" due to denominator (resident pop) vs numerator (transient pop) mismatch
- **Small communes**: absolute numbers are volatile; one bad year skews stats
- **Methodology changes**: 2022-2023 many countries reformed crime classification (esp. FR CSI), making time-series comparisons tricky
- **Reporting culture**: northern Europe high-trust = high reporting; southern Europe lower reporting → apparent stats may be biased downward
- **Crime maps interpretation**: a hex with "5 incidents" in 12 months for a 5,000-pop neighbourhood = essentially low

## Confidence labels

- **HIGH**: National police data + commune-specific + recent (< 12 months)
- **MEDIUM**: Regional/commune data older (12-36 months) or methodology changed in last 2 years
- **LOW**: Only regional data (commune too small to publish); statistical noise; or no data available

## Forbidden hallucinations

- **Never invent absolute numbers** when commune-level is suppressed
- **Never claim "X is dangerous"** without citing data
- **Surface conflicts** (e.g., police statistics show low crime but local forum reports differ) — present both
- **Always include the methodology change footnote** for FR / IT / DE post-2022

## Output bands

🟢 **GREEN** — Total crime rate < 50 % national average
🟡 **YELLOW** — Within 50-110 % national average
🟠 **ORANGE** — 110-200 % national average for one or more categories
🔴 **RED** — > 200 % national average; multiple categories elevated; or known crime hotspot in local press
