# Price-Index Data Feeds Catalog

Per-country house price index sources, including API/CSV/RSS availability, frequency, latest verifiable value. **This catalog supports `--update --refresh-only`** — when the validator is pulling fresh comp values for `--price`, this is the source-of-truth registry.

**Snapshot**: April 2026.

## Universal contract

For each country, return:
1. **Authoritative source** (national statistics office or central bank)
2. **Index URL** (HTML, hopefully also CSV/JSON)
3. **API/CSV/RSS availability** (machine-readable feed?)
4. **Frequency** (monthly / quarterly / annual)
5. **Latest verifiable value** as of refresh-date
6. **Eurostat HPI cross-reference** (most EU sources align with Eurostat HPI series)

## Output template

```markdown
## Price-Index Feed

**Country**: <ISO2>
**Source**: <authority>
**Index name**: <official series name>
**HTML**: <URL>
**Machine-readable**: <CSV / JSON / RSS / FRED / none>
**Frequency**: <quarterly | monthly | annual>
**Latest value (date)**: <number with date>
**Eurostat HPI ref**: <https://ec.europa.eu/eurostat/databrowser/view/prc_hpi_q__custom_xxx/default/table>
```

---

## Europe — verified sources

| ISO | Source | Index | HTML / data | Frequency | Latest value (Apr 2026) |
|---|---|---|---|---|---|
| **FR** | INSEE | Indice des prix des logements | https://www.insee.fr/fr/statistiques/serie/000857179 | quarterly | Q4 2025 |
| **IT** | ISTAT | Indice dei prezzi delle abitazioni | https://www.istat.it/it/files/abitazioni/ | quarterly | Q4 2025 |
| **CZ** | ČSÚ | Cenové indexy bytů | https://csu.gov.cz/ | quarterly | Q4 2025 |
| **SK** | NBS / ŠÚ SR | RBNV | https://nbs.sk/statisticke-udaje/ + https://slovak.statistics.sk/ | quarterly | Q4 2025 |
| **DE** | Destatis | Häuserpreisindex | https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Baupreise-Immobilienpreisindex/ | quarterly | Q4 2025 |
| **AT** | Statistik Austria + OeNB | Wohnimmobilien | https://www.statistik.at/ + https://www.oenb.at/ | quarterly | Q4 2025 |
| **CH** | Wüest Partner / Swiss FSO | swiss real-estate index | https://www.wuestpartner.com/ + https://www.bfs.admin.ch/ | quarterly | Q4 2025 |
| **ES** | INE | IPV (Índice de Precios de Vivienda) | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838 | quarterly | Q4 2025 |
| **PT** | INE | IPHab (Índice de Preços da Habitação) | https://www.ine.pt/ | quarterly | Q4 2025 |
| **SE** | SCB + Lantmäteriet | Fastighetsprisindex | https://www.scb.se/ | quarterly | Q4 2025 |
| **FI** | Tilastokeskus | Asuntojen hintaindeksi | https://stat.fi/en/statistics/ashi | quarterly | Q4 2025 |
| **NO** | SSB + Eiendom Norge | Boligprisindeks | https://www.ssb.no/en/statbank/list/bpi | monthly | Q4 2025 |
| **UK** | UK HPI (HMLR + ONS + Land Registry) | UK HPI | https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads | monthly | Latest published |
| **NL** | CBS + Kadaster | Prijsindex bestaande koopwoningen | https://www.cbs.nl/ | monthly | Q4 2025 |
| **BE** | STATBEL | Prijzen onroerende goederen | https://statbel.fgov.be/ | quarterly | Q4 2025 |
| **DK** | Danmarks Statistik | Ejendomspriser | https://www.dst.dk/en | quarterly | Q4 2025 |
| **IS** | HMS / Þjóðskrá | Vísitala íbúðaverðs | https://hms.is/en/ | monthly | Latest |
| **SI** | SURS / GURS | Cene stanovanjskih nepremičnin | https://www.stat.si/StatWeb/en | quarterly | Q4 2025 |
| **IE** | CSO | Residential Property Price Index | https://www.cso.ie/en/statistics/prices/residentialpropertypriceindex/ | monthly | Latest |
| **GR** | Bank of Greece + Hellenic Stat | RPPI | https://www.bankofgreece.gr/ + https://www.statistics.gr/en/home | quarterly | Q4 2025 |
| **PL** | NBP BaRN | RBNV | https://nbp.pl/en/statistic/property-prices/ | quarterly | Q4 2025 |
| **EE** | Statistics Estonia | RBNV | https://andmed.stat.ee/ | quarterly | Q4 2025 |
| **HR** | DZS + HNB | RBNV | https://podaci.dzs.hr/en/ + https://www.hnb.hr/ | quarterly | Q4 2025 |
| **HU** | KSH + MNB | Lakásárindex | https://www.ksh.hu/ + https://www.mnb.hu/en | quarterly | Q4 2025 |
| **LT** | Ober-Haus + OSP | OHBI + HPI | https://www.ober-haus.lt/en/rinkos_apzvalgos/lithuanian-price-index/ + https://osp.stat.gov.lt/ | monthly + quarterly | Dec 2025 (Vilnius +10.7% YoY) |
| **LV** | CSP + Latvijas Banka | HPI | https://stat.gov.lv/en + https://www.bank.lv/ | quarterly | Q4 2025: 224.02 (+8.4% YoY through Q3) |
| **RO** | INS | IPL (Indicele prețurilor locuințelor) | https://www.insse.ro/ | quarterly | Q4 2025: 168.99 |
| **BG** | NSI | HPI | https://www.nsi.bg/en/metadata/house-price-index-hpi-227 | quarterly | Q4 2025: 256.71 |
| **LU** | STATEC + Observatoire de l'Habitat | HPI | https://statistiques.public.lu/en/publications/series/logement-chiffres.html | quarterly | Q1 2025: apartments €8,094/m² (+3.7% YoY) |
| **CY** | Central Bank of Cyprus | RPPI | https://www.centralbank.cy/en/publications/residential-property-price-indices | quarterly | Q4 2025: +2.3% QoQ; house +7.1% YoY; Limassol apt 150.1 |
| **MT** | NSO + Central Bank of Malta | RPPI | https://nso.gov.mt/property/ + https://www.centralbankmalta.org/ | quarterly | Q4 2025: 177.36 (+6.1% YoY) |

## Western Balkans

| ISO | Source | Index | URL | Frequency |
|---|---|---|---|---|
| RS | NBS price index | RPPI | https://www.nbs.rs/ | quarterly |
| ME | MONSTAT + CBCG | HPI | https://www.monstat.org/eng/ + https://www.cbcg.me/en | quarterly |
| BA | BHAS + entity statistics offices | HPI | https://bhas.gov.ba/ | annual / quarterly |
| MK | MAKSTAT + NBRSM | HPI | https://www.stat.gov.mk/ | quarterly |
| AL | INSTAT + Bank of Albania (Fischer HPI) | HPI | https://www.instat.gov.al/en/ + https://www.bankofalbania.org/ | quarterly |

## Anglo non-EU

| ISO | Source | Index | URL | Frequency |
|---|---|---|---|---|
| CA | CREA | MLS HPI | https://www.crea.ca/ | monthly |
| AU | ABS RPPI + CoreLogic | RPPI | https://www.abs.gov.au/ + https://www.corelogic.com.au/ | quarterly + monthly |
| NZ | REINZ HPI + QV | HPI | https://www.reinz.co.nz/ + https://www.qv.co.nz/ | monthly |

## Latin America

| ISO | Source | Index | URL | Frequency |
|---|---|---|---|---|
| MX | SHF | HPI | https://www.gob.mx/shf | quarterly |
| BR | FIPE-ZAP + IGMI-R (BCB) | HPI | https://www.fipe.org.br/ + https://www.bcb.gov.br/ | monthly |
| AR | Reporte Inmobiliario + INDEC | HPI | https://www.reporteinmobiliario.com/ | monthly |
| CR | BCCR + INEC | HPI | https://www.bccr.fi.cr/ | quarterly |
| PA | INEC + Acobir | HPI | https://www.inec.gob.pa/ + https://www.acobir.com/ | annual |

---

## BIS / FRED cross-references (international comparable)

The Bank for International Settlements (BIS) maintains a uniform Residential Property Price database; FRED republishes it. Use these for cross-country comparable real-terms growth — NOT for level €/m² values.

- **BIS portal**: https://www.bis.org/statistics/pp.htm
- **BIS by-country**: https://www.bis.org/statistics/pp_selected.htm
- **FRED collection**: https://fred.stlouisfed.org/categories/32218

Examples:
- LT: https://fred.stlouisfed.org/series/QLTN628BIS
- LV: https://fred.stlouisfed.org/series/QLVN628BIS
- BG: https://fred.stlouisfed.org/series/QBGN628BIS

## Eurostat HPI

Pan-EU comparable index (quality-adjusted, base=100). For all EU+EEA countries.

- **Database**: https://ec.europa.eu/eurostat/web/housing/database
- **Methodology**: https://ec.europa.eu/eurostat/cache/metadata/en/prc_hpi_oo_esms.htm

---

## Refresh logic for `--update --refresh-only`

Per country playbook:

1. **Fetch latest index value** from authoritative source (HTML scrape OR machine-readable endpoint where available)
2. **Cross-check against Eurostat HPI** for EU/EEA (any divergence >5% YoY = flag)
3. **Compute YoY + QoQ delta** vs prior playbook value
4. **Update country playbook §price** with: latest value, source URL, retrieval timestamp
5. **Trigger anti-hallucination check 4** ("source ranking — never silently upgrade")
6. **Log to `playbook.md.bak-<date>`** as part of standard updater flow

## Frequency-of-refresh recommendation

- **Monthly**: countries with monthly index (UK, NL, IE, NO, IS, CR, BR, CA, NZ, LT/Ober-Haus)
- **Quarterly**: most EU + LV/RO/BG/LU/CY/MT
- **Per-event**: any reform (BG eurozone, RO VAT, ES regional ITP) triggers an immediate re-fetch

## Status

Last refreshed: 2026-04-26.
