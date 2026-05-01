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

- **Statistics Canada — Police-reported crime statistics**: `https://www150.statcan.gc.ca/n1/en/catalogue/85-002-X` — annual Juristat publication, Uniform Crime Reporting Survey (UCR)
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

- **NZ Police "Crime Snapshot"**: `https://www.police.govt.nz/crime-snapshot`
- **Stats NZ Justice + Crime publications**: `https://www.stats.govt.nz/topics/crime-and-justice/`
- **Granularity**: per-region + meshblock; Police "By the numbers" provides territory-level
- **Caveat**: small national pop = small absolute numbers; per-capita most useful

### 🇪🇪 Estonia

- **Statistikaamet (Statistics Estonia) crime publications**: `https://stat.ee/en/find-statistics/statistics-theme/well-being/security`
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

### 🇺🇸 United States

- **FBI UCR / NIBRS (Crime Data Explorer)**: `https://www.fbi.gov/services/cjis/ucr` + `https://cde.ucr.cjis.gov/` — primary national portal; NIBRS now mandatory (replacing summary UCR) with offense-level detail
- **BJS NCVS (National Crime Victimization Survey)**: `https://bjs.ojp.gov/` — annual victimization survey to triangulate dark figure
- **City-level**: most large PDs publish open-data portals (NYC NYPD CompStat, LAPD, Chicago Data Portal, SFPD, Seattle, Boston) — neighborhood / beat / precinct granularity
- **Granularity**: per-state + per-county + per-agency (≈18,000); city-level frequently parcel-adjacent via PD APIs; rural sheriff's offices often lag NIBRS reporting
- **Caveat**: NIBRS transition (2021+) created series-break; some large agencies (e.g., NYPD historically lagged) report incompletely → national totals are estimates; federal "violent crime" definition excludes simple assault — compare like-for-like

### 🇹🇷 Turkey

- **TÜİK Adalet İstatistikleri (TurkStat Justice Statistics)**: `https://data.tuik.gov.tr/Kategori/GetKategori?p=Adalet-ve-Secim-110` — annual criminal justice tables
- **Emniyet Genel Müdürlüğü (General Directorate of Security)**: `https://www.egm.gov.tr/` — police statistics (limited public granularity)
- **Jandarma Genel Komutanlığı**: rural districts outside police jurisdiction
- **Granularity**: per-il (province, 81) routinely published; per-ilçe (district) data not publicly available at parcel level — verify with local police district (karakol)
- **Caveat**: under-reporting in domestic violence + tourist-zone petty theft; methodology revisions 2017 + 2020; political-context offences may be undercounted

### 🇦🇪 United Arab Emirates

- **Dubai Police**: `https://www.dubaipolice.gov.ae/` — published headline statistics + smart-app reporting
- **Ministry of Interior (MoI)**: `https://www.moi.gov.ae/` — federal annual report (low transparency)
- **Abu Dhabi Police**: `https://www.adpolice.gov.ae/` — emirate-level
- **Granularity**: emirate-level headline rates only; **data not publicly available at parcel/district/community level — verify with local police station (markaz)**
- **Caveat**: very low transparency vs Western peers; published rates emphasize year-on-year decline narrative; expat vs national breakdown rarely disclosed; "safest country" claims rest on government press releases not open data

### 🇯🇵 Japan

- **警察庁 (National Police Agency, NPA / Keisatsucho)**: `https://www.npa.go.jp/` — annual White Paper (犯罪統計) per prefecture
- **法務省 (Ministry of Justice / Houmusho)**: `https://www.moj.go.jp/` — annual White Paper on Crime (犯罪白書)
- **e-Stat**: `https://www.e-stat.go.jp/` — open-data portal; per-todofuken (47 prefectures) + per-city for major metros
- **Granularity**: per-prefecture + per-city; ward-level (区) for 23 Tokyo special wards + ordinance-designated cities; rural town-level often aggregated
- **Caveat**: very low absolute crime; reporting rates high (high-trust); under-reporting concentrated in sexual offences + domestic violence; methodology stable

### 🇹🇭 Thailand

- **Royal Thai Police (สำนักงานตำรวจแห่งชาติ)**: `https://www.royalthaipolice.go.th/` — published headline statistics
- **Office of the Judiciary / Office of the Attorney General**: court statistics for triangulation
- **Granularity**: national + regional headlines; **per-province (จังหวัด, 77) inconsistently published; tourist-zone (Phuket, Pattaya, Koh Samui, Krabi) data not publicly available at parcel/district level — verify with local tourist police (1155)**
- **Caveat**: significant under-reporting (cultural reluctance + insurance non-incentive); tourist-zone gaps (transient victim population, language barriers, settlement-out-of-court norm); foreign-victim incidents often handled by Tourist Police separately and not aggregated

### 🇩🇴 Dominican Republic

- **Policía Nacional (PN)**: `https://www.policianacional.gob.do/` — published statistics
- **Procuraduría General de la República**: `https://pgr.gob.do/` — homicide + serious-offence series (most reliable)
- **ONE (Oficina Nacional de Estadística)**: `https://www.one.gob.do/` — Estadísticas de seguridad
- **Granularity**: per-provincia (32) + Distrito Nacional + Santo Domingo provincia; tourist-zone (Punta Cana / Bávaro / Sosúa / Las Terrenas) often aggregated under Higüey or Puerto Plata
- **Caveat**: under-reporting common in petty theft + domestic; homicide series most trustworthy; tourist-zone incident data often suppressed for tourism-marketing reasons

### 🇨🇴 Colombia

- **Policía Nacional de Colombia**: `https://www.policia.gov.co/` — annual + monthly statistics
- **Medicina Legal (Instituto Nacional de Medicina Legal y Ciencias Forenses)**: `https://www.medicinalegal.gov.co/` — homicide + violent-death series (gold standard, autopsy-anchored)
- **DANE (Departamento Administrativo Nacional de Estadística)**: `https://www.dane.gov.co/` — Encuesta de Convivencia y Seguridad Ciudadana (ECSC) victimization survey
- **Granularity**: per-departamento (32) + per-municipio + Bogotá localidades (20)
- **Caveat**: post-conflict regional divergence (Cauca, Norte de Santander, Catatumbo materially higher than Antioquia/Bogotá); Medellín comuna-level data well-published; armed-actor "social cleansing" + extortion under-reported

### 🇺🇾 Uruguay

- **Ministerio del Interior — Observatorio Nacional sobre Violencia y Criminalidad**: `https://www.minterior.gub.uy/observatorio` — primary portal with monthly + annual series
- **INE (Instituto Nacional de Estadística)**: `https://www.ine.gub.uy/` — Estadísticas vitales + crime tables
- **Granularity**: per-departamento (19) + Montevideo (per-municipio A-G + per-barrio for some series)
- **Caveat**: methodology stable; small population means absolute numbers volatile in interior departments; Montevideo barrio-level rates differ materially (Casavalle/Cerro vs Pocitos/Carrasco)

### 🇨🇱 Chile

- **Carabineros de Chile**: `https://www.carabineros.cl/` — police statistics
- **Subsecretaría de Prevención del Delito (SPD)**: `http://www.seguridadpublica.gov.cl/` — ENUSC (Encuesta Nacional Urbana de Seguridad Ciudadana) victimization survey + DEIS administrative data
- **PDI (Policía de Investigaciones)**: `https://www.pdichile.cl/` — investigative crime
- **Granularity**: per-región (16) + per-comuna (346) + Santiago Metropolitan Region comuna-level routine
- **Caveat**: ENUSC vs Carabineros gap (victim survey shows ~3-5x higher than recorded); 2019 social unrest + 2022-2024 organized-crime expansion (esp. Tren de Aragua) created series-break in Antofagasta/Iquique/Arica; Las Condes/Vitacura/Lo Barnechea materially lower than national avg

### 🇿🇦 South Africa

- **SAPS (South African Police Service) Crime Stats**: `https://www.saps.gov.za/services/crimestats.php` — quarterly per-station data (≈1,150 police stations)
- **Stats SA Victims of Crime Survey (VOCS)**: `https://www.statssa.gov.za/` — annual victimization survey (essential complement)
- **Institute for Security Studies (ISS)**: `https://issafrica.org/` — secondary analysis + per-station mapping
- **Granularity**: per-province (9) + per-station (1,150) — among the most granular in Africa; per-suburb only for major metros via private aggregators
- **Caveat**: under-reporting significant for sexual offences + assault (VOCS gap); precinct boundaries don't match suburb boundaries (Sandton vs Alexandra share Linden / Sandton stations); "contact crime" categorization changed 2015+; gated-estate vs township within same precinct can differ by orders of magnitude

### 🇬🇪 Georgia

- **Ministry of Internal Affairs (MIA / შინაგან საქმეთა სამინისტრო)**: `https://police.ge/` — annual + monthly crime statistics
- **Geostat (National Statistics Office of Georgia)**: `https://www.geostat.ge/en` — criminal justice tables
- **Supreme Court of Georgia**: court statistics
- **Granularity**: per-region (mkhare, 9 + 2 autonomous + Tbilisi) + Tbilisi raioni (districts); rural municipality data published but small absolute numbers
- **Caveat**: post-2003 reform reduced petty corruption + recorded-crime methodology stabilized; under-reporting in domestic violence (cultural); breakaway regions (Abkhazia, South Ossetia) not in MIA series

### 🇮🇩 Indonesia

- **Polri (Kepolisian Negara Republik Indonesia)**: `https://www.polri.go.id/` — national headline statistics; Polda (provincial) sites for per-province
- **BPS (Badan Pusat Statistik) Statistik Kriminal**: `https://www.bps.go.id/` — annual Statistik Kriminal publication
- **Granularity**: per-provinsi (38) + per-Polda; per-kabupaten/kota (≈514) data inconsistently public — verify with local Polres
- **Caveat**: significant under-reporting (low trust in low-rank police, settlement-out-of-court norm "musyawarah"); tourist-zone (Bali Kuta/Seminyak/Canggu, Lombok Senggigi/Kuta) data not publicly available at parcel/banjar level — verify with local Polsek; Aceh Sharia-court offences separate

### 🇲🇾 Malaysia

- **PDRM (Polis Diraja Malaysia)**: `https://www.rmp.gov.my/` — annual statistics + IGP press releases
- **DOSM (Department of Statistics Malaysia) crime stats**: `https://www.dosm.gov.my/` — Compendium of Social Statistics
- **Royal Malaysia Police Crime Index (Indeks Jenayah)**: 7-category index (murder, rape, robbery, assault, burglary, vehicle theft, snatch theft)
- **Granularity**: per-state (13 + 3 federal territories) + per-district (daerah polis); KL/Selangor district-level routine; East Malaysia (Sabah/Sarawak) lower granularity
- **Caveat**: "Crime Index" methodology change 2014 + 2020 created series-break; under-reporting in commercial-fraud + domestic; expat-targeted scams (Macau scam, parcel scam) often handled by separate CCID

### 🇻🇳 Vietnam

- **Bộ Công An (Ministry of Public Security)**: `https://bocongan.gov.vn/` — limited public statistics
- **Tổng cục Thống kê (General Statistics Office)**: `https://www.gso.gov.vn/` — annual statistical yearbook (criminal justice chapter)
- **Supreme People's Procuracy (Viện Kiểm sát Nhân dân Tối cao)**: court-side series
- **Granularity**: national headlines + occasional per-province (63); **city/district/ward (phường) level data not publicly available — verify with local public security ward office (Công an phường)**
- **Caveat**: very low transparency; published narratives emphasize stability + low crime; political-context offences excluded from public series; expat-targeted petty theft (HCMC District 1, Hanoi Old Quarter) anecdotally elevated but not publicly quantified

### 🇵🇭 Philippines

- **PNP (Philippine National Police) Crime Statistics**: `https://www.pnp.gov.ph/` — monthly + annual reports; Crime Information Reporting and Analysis System (CIRAS)
- **PSA (Philippine Statistics Authority)**: `https://psa.gov.ph/` — Crime statistics integrated in Statistical Yearbook
- **Granularity**: per-region (17) + per-province (82) + per-city/municipality + Metro Manila per-city + per-barangay (for major cities only)
- **Caveat**: 2016-2022 "war on drugs" period created reporting distortions (extra-judicial killings + drug-related deaths separately tracked, definitions contested); under-reporting in domestic + sexual; Mindanao conflict-zone data partially aggregated; tourist-zone (Boracay, Cebu, Palawan) incidents sometimes routed through DOT separately

### 🇮🇱 Israel

- **Israel Police (משטרת ישראל)**: `https://www.gov.il/he/departments/israel_police` — published statistics + open-data
- **Central Bureau of Statistics (CBS / הלמ"ס)**: `https://www.cbs.gov.il/` — Social Statistics including criminal justice
- **State Attorney + Ministry of Justice**: indictment + conviction series
- **Granularity**: per-district (6) + per-city + Jerusalem/Tel Aviv neighborhood-level via municipal open data
- **Caveat**: West Bank settlements partially in Israeli police series (depending on jurisdiction split with IDF/Civil Administration); East Jerusalem under-reporting (Palestinian residents use parallel mechanisms); 2023+ security situation created series-break + "security incidents" categorized separately from "crime"

### 🇲🇦 Morocco

- **DGSN (Direction Générale de la Sûreté Nationale)**: `https://www.dgsn.gov.ma/` — annual press conference + bulletins (urban areas)
- **Gendarmerie Royale**: rural areas outside DGSN jurisdiction
- **HCP (Haut-Commissariat au Plan) victimization surveys**: `https://www.hcp.ma/` — periodic enquêtes (most recent 2018-2019)
- **Granularity**: national + per-region (12) headlines; per-prefecture/province inconsistently published; per-arrondissement (Casablanca/Rabat) only via DGSN press
- **Caveat**: under-reporting common (HCP victim survey shows ~3-4x higher than DGSN recorded); tourist-zone (Marrakech medina, Tangier, Essaouira, Agadir) petty-theft + harassment under-reported; methodology not aligned with EU; data not publicly available at parcel/quarter level — verify with local arrondissement DGSN

### 🇪🇬 Egypt

- **CAPMAS (Central Agency for Public Mobilization and Statistics) Annual Statistical Yearbook + Criminal Statistics**: `https://www.capmas.gov.eg/` — annual report (criminal justice chapter)
- **Ministry of Interior (وزارة الداخلية)**: `https://moi.gov.eg/` — security communiqués (low public-data granularity)
- **Granularity**: national + governorate-level (27) headlines; **city/district/sheyakha level data not publicly available — verify with local police station (qism al-shorta)**
- **Caveat**: very low transparency; political-context + terrorism-related offences excluded or separately classified; under-reporting significant in sexual harassment (despite 2014 law) + domestic; tourist-zone (Sharm el-Sheikh, Hurghada, Luxor, Aswan) incidents handled by Tourist & Antiquities Police (سياحة وآثار) separately

### 🇸🇬 Singapore

- **Singapore Police Force (SPF) Annual Crime Brief**: `https://www.police.gov.sg/Media-Room/News` — annual + half-yearly crime briefs
- **Singstat (Department of Statistics) Public Order tables**: `https://www.singstat.gov.sg/find-data/search-by-theme/society/public-order-and-safety` — national crime time-series
- **Granularity**: national + 7 police land divisions (Central / Ang Mo Kio / Bedok / Clementi / Jurong / Woodlands / Tanglin) + Neighbourhood Police Centre (NPC) catchments; SPF "Hot-spot Information" published per NPC for select offences
- **Caveat**: very low absolute crime (one of densest crime data globally per CSAR + low under-reporting); methodology stable; cyber-crime/scam categories rapidly evolving (Anti-Scam Centre 2019+); flag transient-population denominator for tourist zones (Orchard / Marina Bay / Sentosa)

### 🇭🇰 Hong Kong

- **Hong Kong Police Force (HKPF / 香港警務處) Crime Statistics**: `https://www.police.gov.hk/ppp_en/09_statistics/csc.html` — quarterly + annual statistics
- **Census & Statistics Department (C&SD / 政府統計處)**: `https://www.censtatd.gov.hk/` — Hong Kong Annual Digest of Statistics (Justice & Crime chapter)
- **Granularity**: per-region (HK Island / Kowloon East / Kowloon West / New Territories North / New Territories South / Marine) + per-District Council district (18) + per-police-district
- **Caveat**: very high reporting rate (high-trust); methodology stable pre-2020; **Article 23 National Security Law (Mar 2024) categorisation of "national-security offences" separately classified — ordinary crime data unaffected but flag for relocation-decision context**

### 🇰🇷 South Korea

- **Korean National Police Agency (KNPA / 경찰청) Crime Statistics**: `https://www.police.go.kr/` — annual White Paper + monthly statistics
- **KOSIS (Korean Statistical Information Service)**: `https://kosis.kr/eng/` — Crime Statistics tables (national stats office portal)
- **Korean Institute of Criminology (KIC / 한국형사·법무정책연구원)**: `https://www.kicj.re.kr/` — secondary analysis + victimization survey
- **Granularity**: per-province / metropolitan-city (17) + per-police-district (시도경찰청 → 경찰서) + Seoul gu (district, 25) + sub-station (지구대/파출소)
- **Caveat**: very low absolute crime; reporting rates high; under-reporting concentrated in sexual offences + domestic violence (despite 2010s reforms); tourist-zone (Myeongdong / Hongdae / Itaewon / Gangnam) flag for transient-victim denominator; methodology stable

### 🇹🇼 Taiwan

- **National Police Agency (NPA / 內政部警政署) Crime Statistics**: `https://www.npa.gov.tw/` — annual statistics + Police Statistical Yearbook
- **Directorate-General of Budget, Accounting & Statistics (DGBAS / 主計總處)**: `https://eng.dgbas.gov.tw/` — Statistical Yearbook (Public Order chapter)
- **Ministry of Justice (MOJ / 法務部)** prosecutorial statistics — court-side triangulation
- **Granularity**: per-municipality (6 special + 16 county/city) + per-police-precinct (分局) + Taipei + New Taipei district-level for capitals
- **Caveat**: very low absolute crime; methodology stable; under-reporting in domestic + sexual; cross-Strait political-context offences separately classified; published narratives emphasize "safe city" framing

### 🇱🇮 Liechtenstein

- **Landespolizei (National Police) Memoria di Attività / Tätigkeitsbericht**: `https://www.landespolizei.li/` — annual activity report + crime statistics
- **Statistik Liechtenstein**: `https://www.llv.li/en/national-administration/office-of-statistics` — Crime & Justice statistics
- **Granularity**: national + per-Gemeinde (11 municipalities); small absolute numbers
- **Caveat**: very low absolute crime; small population (~40k) means single incidents move per-capita rates; methodology aligned with CH; cross-border CH/AT police cooperation

### 🇲🇴 Macao

- **Corpo de Polícia de Segurança Pública (CSP / 治安警察局)**: `https://www.fsm.gov.mo/psp/` — published statistics + annual report
- **DSEC (Direcção dos Serviços de Estatística e Censos / 統計暨普查局)**: `https://www.dsec.gov.mo/` — Crime & Justice tables
- **Polícia Judiciária (PJ / 司法警察局)**: investigative crime statistics
- **Granularity**: national + parish-level (7 freguesias) + casino-zone (Cotai) often aggregated; DSEC publishes per-category time series
- **Caveat**: very low absolute crime; gaming-zone (Cotai/Macao Peninsula) inflates fraud + loan-shark categories; transient-population denominator (~30M+ visitors/yr pre-COVID, recovering) skews tourist-zone rates; under-reporting in domestic; political-context offences post-2020 NSL framework separately classified

### 🇦🇩 Andorra

- **Cos de Policia d'Andorra — Memòria d'Activitat**: `https://www.policia.ad/` — annual activity report + crime statistics
- **Estadística d'Andorra (Departament d'Estadística)**: `https://www.estadistica.ad/` — Justícia i Criminalitat tables
- **Granularity**: national + per-parròquia (7 parishes); small absolute numbers
- **Caveat**: very low absolute crime; ski-tourist transient population (winter Dec-Apr + summer Jul-Aug) inflates seasonal rates; small national pop (~85k) means single incidents move per-capita rates; methodology stable

### 🇲🇨 Monaco

- **Direction de la Sûreté Publique (DSP)**: `https://www.gouv.mc/Action-Gouvernementale/Securite-Justice` — Sûreté Publique pages + published statistics
- **IMSEE (Institut Monégasque de la Statistique et des Études Économiques)**: `https://www.monacostatistics.mc/` — Sécurité & Justice tables
- **Granularity**: national (single police jurisdiction); ward-level (Monaco-Ville / La Condamine / Monte-Carlo / Fontvieille) for select offences
- **Caveat**: very low absolute crime; very high police-to-resident ratio (~1 cop per 60 residents — densest globally per DSP); transient-population denominator (~9M visitors/yr) skews tourist-zone rates; under-reporting low (high trust + dense surveillance)

### 🇲🇩 Moldova

- **Inspectoratul General al Poliției (IGP)**: `https://politia.md/` — annual crime statistics + monthly bulletins
- **BNS (Biroul Național de Statistică)**: `https://statistica.gov.md/` — Justiție și Criminalitate tables (national stats office)
- **Procuratura Generală**: `https://procuratura.md/` — prosecutorial statistics for triangulation
- **Granularity**: per-raion (32 districts + Chișinău + Bălți + Comrat ATU Găgăuzia) + Chișinău sectors (5); rural raion data published but small absolute numbers
- **Caveat**: under-reporting common in domestic + sexual; **Transnistria (separatist-administered) NOT in IGP series — separate parallel statistics published by Tiraspol "ministry" but not citable as primary**; emigration sustained since 1990s affects denominator; methodology aligned with EU since candidate status (Jun 2022 → accession negotiations Jun 2024)

### 🇶🇦 Qatar

- **Ministry of Interior — Public Security (وزارة الداخلية — الأمن العام)**: `https://www.moi.gov.qa/` — published annual reports + traffic + crime communiqués
- **PSA (Planning & Statistics Authority)**: `https://www.psa.gov.qa/` — Annual Crime & Justice Statistics (Crime in Qatar bulletin)
- **Public Prosecution (النيابة العامة)**: `https://www.pp.gov.qa/` — prosecutorial statistics
- **Granularity**: national + per-municipality (8 baladiyat: Doha / Al Rayyan / Al Wakrah / Al Khor / Umm Salal / Al Daayen / Al Shamal / Al Shahaniya); **Doha + Al Rayyan district-level data not publicly available — verify with local police station (markaz al-shorta)**
- **Caveat**: very low absolute crime per public communiqués; transparency limited vs Western peers; published rates emphasize year-on-year decline narrative; expat (88% of population) vs Qatari breakdown rarely disclosed; political-context offences excluded; 2022 World Cup security baseline still used as reference

### 🇸🇦 Saudi Arabia

- **Ministry of Interior — Public Security (الأمن العام)**: `https://www.moi.gov.sa/` — annual reports + Tawakkalna app reporting
- **GASTAT (General Authority for Statistics)**: `https://www.stats.gov.sa/` — Statistical Yearbook (Justice & Crime chapter)
- **Public Prosecution (النيابة العامة)**: `https://www.pp.gov.sa/` — prosecutorial statistics
- **Granularity**: national + per-region (13 mintaqat: Riyadh / Makkah / Eastern Province / Madinah / Al Qassim / Asir / Tabuk / Hail / Northern Borders / Jazan / Najran / Al Bahah / Al Jouf); **city/district-level (e.g., Riyadh districts, Jeddah Corniche/Al Hamra) data not publicly available — verify with local police station (markaz)**
- **Caveat**: very low absolute violent crime; Sharia-court offences separately classified; under-reporting in domestic + sexual significant (despite 2018-2021 reforms); expat-targeted incidents in compounds (Aramco/SABIC) often handled internally; political-context + counter-terrorism offences excluded from public series; tourist-zone (Diriyah / Red Sea / NEOM) baseline establishing under Vision 2030

### 🇵🇪 Peru

- **PNP (Policía Nacional del Perú)**: `https://www.policia.gob.pe/` — annual statistics + monthly bulletins; Sistema de Denuncias Policiales (SIDPOL)
- **INEI (Instituto Nacional de Estadística e Informática)**: `https://www.inei.gob.pe/` — Estadísticas de Seguridad Ciudadana + Encuesta Nacional de Programas Presupuestales (ENAPRES) victimization survey
- **Ministerio Público — Fiscalía de la Nación**: `https://www.gob.pe/mpfn` — prosecutorial statistics
- **Granularity**: per-departamento (24 + Constitutional Province of Callao) + per-provincia + per-distrito + Lima Metropolitana per-distrito (43); rural province data published but small absolute numbers
- **Caveat**: under-reporting common (~73% per ENAPRES victim survey 2023); homicide series most reliable; tourist-zone (Cusco / Machu Picchu / Arequipa) inflated by transient denominator; Lima district-level rates differ materially (San Isidro / Miraflores / Barranco vs San Juan de Lurigancho / Comas / Villa El Salvador); state-of-emergency areas (esp. VRAEM coca region) separately tracked

### 🇪🇨 Ecuador

- **PNE (Policía Nacional del Ecuador)**: `https://www.policianacional.gob.ec/` — annual + monthly statistics + ECU-911 incident dispatch
- **INEC (Instituto Nacional de Estadística y Censos)**: `https://www.ecuadorencifras.gob.ec/` — Estadísticas de Seguridad Ciudadana + Encuesta de Victimización
- **Fiscalía General del Estado**: `https://www.fiscalia.gob.ec/` — prosecutorial statistics
- **Granularity**: per-provincia (24) + per-cantón (221) + Quito + Guayaquil + Cuenca district-level
- **Caveat**: **2024 violent-crime peak Guayaquil/Esmeraldas/Manta (homicide rate ~45/100k national, ~80/100k Guayas/Esmeraldas — verify per latest INEC release)**; series-break Jan 2024 (Internal Armed Conflict declaration vs 22 narco-groups); under-reporting common; series before 2017 shows materially lower baseline pre-narco-trafficking expansion; tourist-zone (Galápagos / Mindo / Otavalo) materially safer than coastal Pacific cities

### 🇵🇾 Paraguay

- **Policía Nacional del Paraguay**: `https://www.policianacional.gov.py/` — annual statistics + departmental headquarters bulletins
- **INE (Instituto Nacional de Estadística)**: `https://www.ine.gov.py/` — Estadísticas Sociales y Demográficas (Justice & Crime chapter)
- **Ministerio Público — Fiscalía General**: `https://www.ministeriopublico.gov.py/` — prosecutorial statistics
- **Granularity**: per-departamento (17 + Asunción) + per-distrito + Asunción barrio-level for some series
- **Caveat**: under-reporting moderate (settlement-out-of-court norm + Guaraní-language barriers in rural areas); border-zone Ciudad del Este (Triple Frontier with BR + AR) inflated by transit/contraband-economy; Pedro Juan Caballero (BR border) elevated; Asunción + Encarnación rates moderate; small population means absolute numbers volatile in interior departments

### 🇦🇲 Armenia

- **Police of Armenia (ՀՀ Ոստիկանություն)**: `https://www.police.am/` — annual statistics + monthly bulletins
- **ARMSTAT (Statistical Committee of Armenia / Armstatbank)**: `https://www.armstat.am/` — Crime & Justice tables in Statistical Yearbook
- **Prosecutor General's Office (ՀՀ Գլխավոր Դատախազություն)**: `https://www.prosecutor.am/` — prosecutorial statistics
- **Granularity**: per-marz (10 provinces + Yerevan as separate administrative unit) + Yerevan district-level (12 administrative districts)
- **Caveat**: very low absolute crime (one of lowest in Caucasus); 2018 Velvet Revolution + 2020 Nagorno-Karabakh war + 2023 Azerbaijani offensive on NK created series-breaks; under-reporting in domestic violence (despite 2017 law); IT-sector + diaspora-driven Yerevan demographics differ from rural marzes; ~7M global diaspora overlay structurally affects denominator pattern

### 🇦🇿 Azerbaijan

- **Ministry of Internal Affairs (Azərbaycan Respublikası Daxili İşlər Nazirliyi)**: `https://www.mia.gov.az/` — annual reports + ASAN-integrated reporting
- **SSC (State Statistical Committee / Dövlət Statistika Komitəsi)**: `https://www.stat.gov.az/` — Crime & Justice tables
- **Prosecutor General's Office (Baş Prokurorluq)**: `https://www.genprosecutor.gov.az/` — prosecutorial statistics
- **Granularity**: national + per-rayon (66 districts + 11 cities of republican subordination) + Baku district-level (12 rayons)
- **Caveat**: very low absolute crime per public statistics; transparency limited; political-context + post-2020/2023 NK-related offences separately classified; under-reporting in domestic + sexual significant; ASAN Service efficient governance reduces friction for citizen reporting but published rates skew toward administrative completeness vs ground-truth

### 🇹🇳 Tunisia

- **DGSN (Direction Générale de la Sûreté Nationale)**: `https://www.interieur.gov.tn/` — Ministry of Interior portal; annual security communiqués
- **Garde Nationale (Garde Nationale Tunisienne)**: rural areas outside DGSN jurisdiction
- **INS (Institut National de la Statistique)**: `https://www.ins.tn/` — Statistiques Sociales et Démographiques (Justice & Sécurité)
- **Ministère de la Justice**: `https://www.e-justice.tn/` — prosecutorial + court statistics
- **Granularity**: national + per-gouvernorat (24) headlines; per-délégation (264) inconsistently published; per-arrondissement (Tunis city) only via DGSN press releases
- **Caveat**: under-reporting common (HCP-style victim survey not published routinely); tourist-zone (Hammamet / Sousse / Monastir / Djerba) petty-theft + harassment under-reported (post-2015 Sousse + Bardo attacks reshaped published-narrative); 2023+ irregular-migration-route incidents around Sfax materially affect regional rates; methodology not aligned with EU; political-context + counter-terrorism offences separately classified; data not publicly available at parcel/quarter level — verify with local DGSN brigade

### 🇮🇳 India

- **NCRB (National Crime Records Bureau)**: `https://ncrb.gov.in/` — annual Crime in India report (most authoritative); per-state + per-city (53 metropolitan cities ≥1M pop) coverage
- **MHA (Ministry of Home Affairs)**: `https://www.mha.gov.in/` — policy + Inter-State CCTNS (Crime and Criminal Tracking Network & Systems)
- **State Police**: each state has dedicated police force — Mumbai Police `https://mumbaipolice.gov.in/`, Delhi Police `https://www.delhipolice.gov.in/`, Bengaluru City Police `https://bcp.karnataka.gov.in/`, Chennai City Police `https://www.chennaipolice.gov.in/`, Kolkata Police `https://kolkatapolice.gov.in/`, Hyderabad City Police `https://www.hyderabadpolice.gov.in/`, Pune City Police `https://punepolice.gov.in/`, Gurgaon Police `https://police.gov.in/` (Haryana)
- **Granularity**: per-state (28 + 8 UTs) + per-district + 53 metropolitan cities (NCRB Crime in India "Crime in Cities" chapter); per-PS (police-station, ~17,000) data via state portals inconsistent
- **Caveat**: significant under-reporting (NCRB acknowledges; victim-survey data limited — no routine NSO crime survey); methodology stable post-2014; political-context + insurgency offences (J&K, Nagaland, Manipur) separately classified; 2023 Bharatiya Nyaya Sanhita + Bharatiya Nagarik Suraksha Sanhita replaced IPC + CrPC effective 1 Jul 2024 — categorisation may shift in 2024+ NCRB publications; metro-level rates differ materially (Bengaluru/Pune/Chennai materially lower than Delhi/Lucknow/Patna)

### 🇳🇬 Nigeria

- **NPF (Nigeria Police Force)**: `https://npf.gov.ng/` — annual statistics + state command data; limited public granularity
- **NBS (National Bureau of Statistics)**: `https://nigerianstat.gov.ng/` — Crime Statistics Quarterly Report + Crime Experience and Safety Survey (CESS)
- **MHA (Ministry of Interior)**: `https://interior.gov.ng/`
- **State Commands** (NPF state offices): Lagos State Police `https://lspc.gov.ng/`, FCT Abuja `https://npf.gov.ng/abuja/`, Rivers State (Port Harcourt), Kano State; **per-LGA (774) + per-ward data not publicly available — verify with local Divisional Police Office (DPO)**
- **Granularity**: national + per-state (36 + FCT) headlines via NBS; per-LGA inconsistently published; per-ward (8,809) not routine
- **Caveat**: very high dark-figure (CESS 2024 victim survey shows ~3-5x recorded crime); Boko Haram NE (Borno/Yobe/Adamawa) + ISWAP Lake Chad / IPOB-ESN SE / banditry NW (Zamfara/Kaduna/Katsina) / Gulf of Guinea piracy + maritime kidnapping separately tracked under counter-terrorism; Lagos VI/Ikoyi/Lekki materially lower than mainland; published rates emphasize stability narrative; English official + 500+ languages + Pidgin universal affects victim reporting in non-Hausa/Yoruba/Igbo zones

### 🇰🇪 Kenya

- **NPS (National Police Service)**: `https://www.nationalpolice.go.ke/` — annual statistics + DCIO incident reports
- **DCI (Directorate of Criminal Investigations)**: `https://www.dci.go.ke/` — investigative crime statistics + Crime Trend Analysis
- **KNBS (Kenya National Bureau of Statistics)**: `https://www.knbs.or.ke/` — Statistical Abstract Crime chapter + Kenya Population & Housing Census 2019 base
- **Nairobi**: `https://www.nairobi.go.ke/` (county) + Nairobi Metropolitan Services + DCI Nairobi region
- **Mombasa**: Mombasa County `https://mombasa.go.ke/` + Coast Regional Police
- **Granularity**: per-county (47) + per-sub-county (290) + per-ward (1,450) headlines via KNBS; per-station (~1,000+) inconsistently published; Nairobi sub-county (Westlands/Karen/Kilimani/Embakasi/Kibra) varies materially
- **Caveat**: under-reporting common (NPS acknowledges; 2018 victim-survey gap ~2-3x); al-Shabaab cross-border NE Kenya (Garissa/Mandera/Wajir/Lamu) separately tracked under counter-terrorism — affects regional rates materially; 2024 East Africa floods + 2024 Gen-Z protests created reporting series-break; M-PESA mobile money 95%+ adoption reduces cash-crime incentive but enables fintech-fraud; Westlands/Karen/Kilimani/Lavington materially lower than Eastlands (Kibra/Mathare/Mukuru); SGR Mombasa-Nairobi corridor security visible

### 🇯🇴 Jordan

- **PSD (Public Security Directorate / مديرية الأمن العام)**: `https://www.psd.gov.jo/` — annual statistics + Criminal Information Department
- **DOS (Department of Statistics / دائرة الإحصاءات العامة)**: `http://dosweb.dos.gov.jo/` — Statistical Yearbook (Justice & Crime chapter)
- **Ministry of Interior**: `https://moi.gov.jo/`
- **Amman**: Greater Amman Municipality `https://www.amman.jo/` + PSD Amman Governorate
- **Granularity**: national + per-governorate (12) + Amman district-level (Western Amman / Eastern Amman / Madaba peripheral); per-locality inconsistently published
- **Caveat**: among LOWEST crime rates in MENA per PSD — Amman safer than most regional capitals; under-reporting in domestic + sexual significant (despite 2017 reforms); Syrian + Palestinian refugee dynamics (~30%+ of population) affect denominator + crime-vector mix in Zarqa/Mafraq/Irbid; political-context + counter-terrorism offences (Salafi-jihadi networks) separately classified; tourist-zone (Petra/Wadi Rum/Dead Sea) very low

### 🇴🇲 Oman

- **ROP (Royal Oman Police / شرطة عمان السلطانية)**: `https://www.rop.gov.om/` — annual statistics + ROP Crime Wing
- **NCSI (National Centre for Statistics and Information)**: `https://www.ncsi.gov.om/` — Statistical Yearbook (Public Order chapter); NCSI Real Estate Activity Bulletin separately for property-context
- **Ministry of Interior**: `https://moi.gov.om/`
- **Muscat**: Muscat Municipality `https://www.mm.gov.om/` + ROP Muscat Governorate
- **Granularity**: national + per-governorate (11 muhafazat) headlines; per-wilaya (61) + per-district (community level) data not publicly available — verify with local ROP station (markaz al-shorta)
- **Caveat**: among LOWEST crime rates in GCC per ROP; very low transparency vs Western peers; published rates emphasize year-on-year decline narrative; Omani + expat (~46%) breakdown rarely disclosed; tribal-customary dispute resolution (Sharia + walaa) handles many incidents informally — official statistics under-count; political-context + 2011 Sohar protest legacy separately classified; Vision 2040 baseline establishing tourism-zone (Muscat / Salalah / Musandam) data

### 🇧🇭 Bahrain

- **Public Security (وزارة الداخلية — الأمن العام)**: `https://www.policemc.gov.bh/` — annual statistics + Ministry of Interior reports
- **iGA (Information & eGovernment Authority)**: `https://www.iga.gov.bh/` — Statistical Abstract (Public Order chapter)
- **MoH Real Estate Registry**: `https://www.moh.gov.bh/` (separate from policing — referenced for property context)
- **Manama**: Capital Governorate Municipal Council + Public Security Manama
- **Granularity**: national + per-governorate (4: Capital / Muharraq / Northern / Southern) + per-municipal-area (12) headlines; per-block / per-village data not publicly available — verify with local police station
- **Caveat**: very low crime per public communiqués (post-2011 Pearl Roundabout protests stabilized); methodology not aligned with EU; under-reporting in domestic + sexual significant; Bahraini + expat (~55%) breakdown rarely disclosed; political-context + 2011-14 unrest legacy + Shi'a-village vs Sunni-government dynamic affects published-narrative selectivity; sectarian incidents in villages (Sitra / Diraz / Bani Jamra) may not appear in city-aggregated stats

### 🇰🇼 Kuwait

- **MOI (Ministry of Interior / وزارة الداخلية الكويتية)**: `https://www.moi.gov.kw/` — annual statistics + General Department of Criminal Investigation
- **CSB (Central Statistical Bureau / الإدارة المركزية للإحصاء)**: `https://www.csb.gov.kw/` — Statistical Abstract; limited Public Order coverage
- **PACI (Public Authority for Civil Information)**: `https://www.paci.gov.kw/` — population denominator data (mandatory civil-ID registry includes nationality + residence)
- **Kuwait City**: Kuwait Municipality `https://www.baladia.gov.kw/` + MOI Capital Governorate
- **Granularity**: national + per-governorate (6: Capital / Hawalli / Farwaniya / Mubarak Al-Kabeer / Ahmadi / Jahra) + Kuwait City district-level inconsistent; per-block / per-area (qit'a) data not publicly available — verify with local police station (markaz)
- **Caveat**: very low absolute crime per public statistics; transparency limited vs Western peers; published rates emphasize stability narrative; Kuwaiti + expat (~70%) breakdown rarely disclosed; bidoon (stateless) population (~100k) under-counted in denominator; political-context + 1990-91 Iraq invasion legacy separately classified; tribal-customary mediation handles many incidents informally; tourist-zone limited (no GCC-style mass tourism)

### 🇱🇧 Lebanon

- **ISF (Internal Security Forces / قوى الأمن الداخلي)**: `https://www.isf.gov.lb/` — annual statistics + ISF Information Branch
- **General Directorate of General Security**: `https://www.general-security.gov.lb/` — immigration + state-security overlap
- **CAS (Central Administration of Statistics / إدارة الإحصاء المركزي)**: `http://www.cas.gov.lb/` — limited Public Order coverage; no routine victim survey
- **Beirut**: Beirut Governorate + ISF Beirut + Beirut Municipality `https://www.beirut.gov.lb/`
- **Granularity**: national + per-governorate (8 muhafazat: Beirut / Mount Lebanon / North Lebanon / Akkar / Beqaa / Baalbek-Hermel / South Lebanon / Nabatieh) + per-district (qada) headlines; per-town/quarter data not publicly available — verify with local ISF station (markaz al-mukhtar)
- **Caveat**: ISF security forces stretched + private security common (compounded by 2019 collapse + 2024 Israel-Hezbollah war); under-reporting significant in all categories; Hezbollah-controlled areas (Dahieh SE Beirut / Bekaa / S Lebanon south of Litani) — statistics partially routed through Hezbollah parallel security apparatus, not in ISF series; **2024 Israel-Hezbollah war Sep-Nov 2024** physical damage + displacement created series-break; sectarian + Syrian-refugee + Palestinian-refugee (Ain al-Hilweh, Burj el-Barajneh, Shatila) camps have parallel security — not in ISF series; Aug 2020 Beirut Port explosion (~218 deaths) reshaped baseline; cybercrime growing (post-USD-collapse fraud)

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
