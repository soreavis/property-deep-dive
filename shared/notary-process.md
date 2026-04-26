# Universal `--notary` Section

Per-country property-transaction process across all 44 supported countries: notary or equivalent requirement, typical timeline from accepted offer to registered deed, total closing-cost percentage, title-insurance practice, and 2025-2026 process reforms.

**Snapshot**: April 2026.

**Anti-hallucination**: civil-law jurisdictions require notarial deed; common-law use solicitors / conveyancers / title companies. Closing-cost percentages are ranges; verify with notary/lawyer for any specific transaction. `[verify]` marks figures the agent could not confirm.

## Universal contract

For the property's country, return:
1. **Notary required?** (civil-law) vs solicitor/title company (common-law)
2. **Days from accepted offer to deed/registration**
3. **Closing costs as % of price** (transfer tax + notary + registration + cadastral)
4. **Title insurance availability/standard practice**
5. **2025-26 process reforms**
6. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Notary / Process Profile

**Country**: <ISO2>
**Notary required**: <yes (civil-law notary) | no (solicitor/title-company)>
**Offer → deed (days)**: <range>
**Closing costs %**: <range>
**Title insurance**: <standard | rare | not used>
**2025–26 reforms**: <list>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Standing caveats**:
- Timelines assume no chain, no unusual title issues, ready financing
- Fee % regressive in many civil-law countries — figures shown apply to typical mid-range transactions
- Agent commission and lender fees are SEPARATE from these closing-cost ranges

---

## Europe

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **FR** | Yes — notaire (acte authentique) | ~3 months (compromis ~10 days, then 2.5 mo to acte) | **~7-8% all-in** existing; ~2-3% new-build (TVA + frais réduits); droits de mutation ~5.81%, émoluments notaire ~0.8-1%, contribution sécurité immobilière 0.10%, débours (notaires.fr, service-public.fr) | Not used; notaire's research (état hypothécaire, urbanisme) substitutes | **Décret 28 fev 2024** allowing acte authentique électronique à distance fully operational 2025; **DPE** compulsory for sales since 2021, audit énergétique for F/G since Apr 2023 (G) / Apr 2025 (F) — passoires thermiques rental ban schedule continues |
| **IT** | Yes — notaio (rogito) | ~1-2 months (preliminare → rogito) | **~3-10%** depending on residency: prima casa (resident, primary): imposta registro 2% on cadastral, fixed €50+€50; non-resident or seconda casa: 9% on cadastral; new build from builder: VAT 4-22% + fixed; notaio 1-2.5% (agenziaentrate.gov.it) | Not used; notaio verifies title 20-yr trentennial search | **Preliminare registration online via Adempimento Unico** mature; **Visura catastale and ipotecaria** fully digitised 2024; CNN 2025 e-notarisation framework [verify] |
| **CZ** | Notary not required for most residential — **written contract with verified signatures** sufficient; notary common for security/escrow | ~6-10 weeks | ~2-4%: **transfer tax ABOLISHED 26 Sep 2020** (Law 386/2020); cadastre fee CZK 2,000; legal/escrow ~0.5-1% (cuzk.cz, mfcr.cz) | Not used; cadastre (katastr nemovitostí) public-faith | Cadastre digitisation continues; **electronic conversion service** updates 2024-25 [verify] |
| **SK** | Notary or attorney signature verification required; full notarial deed not mandatory | ~6-10 weeks | ~2-4%: no real-estate transfer tax since 2005; cadastre fee €100 (or €33 expedited fee abolished 2024 [verify]); legal ~0.5-1% | Not used | Cadastre digitisation ongoing |
| **DE** | Yes — Notar (notarielle Beurkundung) mandatory by §311b BGB | ~4-8 weeks (Auflassung → Eintragung in Grundbuch can take additional weeks) | **~7-12%**: Grunderwerbsteuer **3.5-6.5%** (varies by Land: BY/SN 3.5%; NRW/BB/SL/SH/TH 6.5%); Notar+Grundbuch ~1.5-2%; Maklerprovision 3.57% buyer share since Dec 2020 | Not standard; Notar verifies | **GwG (Money Laundering Act) tightening 2024** — notaries required enhanced UBO checks; **Grundbuch fully digital** in most Länder by 2025; some Länder (BY) reducing GrESt for first-time buyers [verify proposals 2025] |
| **AT** | Notar OR Rechtsanwalt certifies signatures; full notarial deed common but not mandatory | ~6-10 weeks | **~10-12%**: Grunderwerbsteuer 3.5%, Eintragungsgebühr 1.1%, legal/notar ~1-3%, Maklerprovision 3.6% buyer (bmf.gv.at) | Not used | **Maklerprovision reform 1 Jul 2023** — Bestellerprinzip; ongoing digitalisation of Grundbuch |
| **CH** | Yes — notaire/Notar (cantonal regimes vary; some cantons use Bezirksnotariat, others private) | ~6 weeks | **~4-5%**: transfer tax 0.2-3.3% varies by canton (some abolished e.g. ZH); notary 0.1-1%; Grundbuch 0.15-0.5% | Not used | **Lex Koller** tightening proposals 2024-25 [verify]; cantonal e-Grundbuch rollouts |
| **ES** | Yes — notario (escritura pública) | ~2 months | **~10-13% existing, ~12-15% new**: ITP (existing) 6-11% varies by autonomous community (Andalucía 7%, Madrid 6%, Cataluña 10-11%); IVA 10% + AJD 0.5-1.5% (new); notario 0.1-0.5%; Registro 0.1-0.4% | Not used; **Registro de la Propiedad** public-faith | **Ley 12/2023 vivienda** rent controls in tense areas; **regional ITP cuts** (Madrid, Andalucía, Galicia) continued 2024-25; e-notary signing post-COVID retained |
| **PT** | Notary OR Casa Pronta one-stop service; advogado/solicitador alternative | ~6 weeks | **~7-10%**: IMT 1-7.5% (progressive, primary residence relief); IS 0.8%; notary/registry ~€500-1,500 (portaldasfinancas.gov.pt) | Not used | **Mais Habitação law 2023**: NHR closed end 2023 (replaced by IFICI); **Golden Visa real-estate route eliminated Oct 2023**; Casa Pronta digital expansion |
| **SE** | No notary; **Lantmäteriet** registers; broker (mäklare) typically coordinates | ~30-60 days | **~1.5-4.25%**: stämpelskatt 1.5% (private) or 4.25% (legal entity); pantbrev 2% (mortgage); lagfart fee SEK 825 (lantmateriet.se) | Not used | None major announced |
| **FI** | No notary in common-law sense; **kaupanvahvistaja** (public purchase witness) certifies; alternative DIAS digital service since 2019 | ~4-8 weeks | **~4-5%**: varainsiirtovero **3% (residential, reduced from 4% on 12 Oct 2023)**, 1.5% on housing-company shares (reduced from 2%); Maanmittauslaitos fees ~€134 (vero.fi) | Not used | **Transfer tax cut 12 Oct 2023**; first-home buyer exemption REPEALED same date for buyers under 40 |
| **NO** | No notary; **Statens kartverk** registers | ~4-8 weeks | **~3-4%**: dokumentavgift 2.5% on title transfer (fast-eiendom, not borettslag shares); tinglysing fee NOK 585 (kartverket.no) | Not used | E-tinglysning fully operational; no major reform 2025-26 [verify] |
| **UK** | No notary; solicitor or licensed conveyancer | **~12 weeks average** (Land Registry + HomeOwners Alliance 2024) | **~2-15%**: SDLT (England/NI) **0% to £125k, 2% £125-250k, 5% £250-925k, 10% £925k-1.5m, 12% above; +5% surcharge for second/BTL; +2% non-resident**; effective from **1 Apr 2025** (thresholds reverted from temporary £250k nil-rate); Land Registry £20-1,105; legal £1-2k (gov.uk SDLT) | **Title insurance occasional** for indemnity (defective title, missing planning); not standard | **SDLT thresholds reverted 1 Apr 2025**; **Renters' Rights Act 2024** affects landlord market; Land Registry "Digital Street" continued; Leasehold and Freehold Reform Act 2024 in force from 2025 onwards |
| **NL** | Yes — notaris (akte van levering) | ~6 weeks | **~4-6%**: overdrachtsbelasting **2% owner-occupier, 10.4% investor (since 2023)**; first-home exemption (under 35, <€510k 2024); notaris ~€1,500-2,500; Kadaster €145 (belastingdienst.nl) | Not used; Kadaster public-faith | **Overdrachtsbelasting investor rate 10.4% since 1 Jan 2023**; first-home cap raised annually; **Wet betaalbare huur 2024** rent regulation; **Box-3 vermogen reforms** ongoing |
| **BE** | Yes — notaire/notaris | ~3-4 months | **~12-17%**: droits d'enregistrement Wallonia 12.5%, Flanders **3% primary residence (since 2022, reduced from 6%)** / 12% other, Brussels 12.5%; honoraires notaire ~1-1.5% (notaire.be) | Not used | **Flanders primary residence rate 3% since 1 Jan 2022**; **federal e-notary platform** (Izimi/StarApp) mature; AML tightening 2024 |
| **DK** | No notary; advokat or estate agent handles; **Tinglysning** electronic registration | ~30 days | **~2-3%**: tinglysningsafgift 0.6% + DKK 1,850 (deed); **stamp duty REFORM 2024** [verify exact rate change]; ~1% legal | Not used | **Boligskattereform 1 Jan 2024** — property tax (ejendomsværdiskat + grundskyld) overhauled, valuation system relaunched after years of delay |
| **IS** | No notary; District Magistrate (sýslumaður) registers | ~30-60 days | ~3-4%: stimpilgjald 0.8% (individual primary, halved) / 1.6% (other); þinglýsingargjald ISK 2,500 (syslumenn.is) | Not used | None major announced |
| **SI** | Notary signature certification (overitev) — full notarial deed not mandatory but common | ~4-8 weeks | ~4-6%: davek na promet nepremičnin 2% (existing); DDV 9.5%/22% (new); legal/notar ~1% (gov.si) | Not used | E-Sodišče mature; no major reform |
| **IE** | No notary; solicitor | ~12 weeks | **~3-4%**: Stamp Duty 1% to €1m, 2% above (residential); **10% rate from 2 Oct 2024** for buyers acquiring 10+ houses (anti-fund); Land Registry €175-700; legal ~1% (revenue.ie) | Title insurance rare but emerging | **Budget 2025 (1 Oct 2024)**: bulk-purchase rate raised; **3% rate on residential >€1.5m introduced** [verify]; Help-to-Buy extended to 2029 |
| **GR** | Yes — symvolaiografos | ~2-3 months | **~10-12%**: foros metavivasis 3.09% (existing) / VAT 24% suspended on new builds through 2026; symvolaiografos ~1-1.5%; ypothikofylakeio ~0.5% (aade.gr) | Not used | **VAT suspension on new builds extended through 2026**; Golden Visa property-investment threshold raised to €800k Athens/Thessaloniki/Mykonos/Santorini from 31 Aug 2024 |
| **PL** | Yes — notariusz (akt notarialny) | ~4-8 weeks | **~3-5%**: PCC 2% (existing) — **first-time-buyer exemption since 31 Aug 2023**; VAT 8/23% (new) replaces PCC; notariusz taksa max 0.25-3% regressive (podatki.gov.pl) | Not used | **First-home PCC exemption** continues; mortgage holiday programmes 2024 |
| **EE** | Yes — notar | ~4-8 weeks | ~1-2%: state fee 0.04-0.4% regressive; notar 0.1-0.5%; **no transfer tax** (notar.ee) | Not used | E-notary mature; cross-border e-notarisation pilots |
| **HR** | Notar (javni bilježnik) signature certification; lawyer drafts | ~6-10 weeks | ~5-7%: porez na promet nekretnina 3% (existing); VAT 25% (new); legal ~1-2%; cadastre ~€100 (porezna-uprava.hr) | Not used | **Land registry digitisation** (e-Građani) mature; foreign-buyer market active post-2023 euro adoption |
| **HU** | Notar (közjegyző) involvement limited; ügyvéd (lawyer) drafts | ~4-8 weeks | **~6-9%**: illeték 4% to HUF 1bn, 2% above; ügyvéd ~0.5-1%; földhivatal HUF 6,600 (nav.gov.hu) | Not used | **CSOK Plusz family-housing subsidy from 1 Jan 2024**; **first-home illeték exemption** under 35 (since 2024) [verify]; foreign-buyer permitting unchanged |
| **LT** | Yes — notaras | ~4-6 weeks | ~1-3%: no transfer tax; notaras 0.45% regressive (max ~€7,000); Registrų centras fees (registrucentras.lt) | Not used | None major announced |
| **LV** | Notar (zvērināts notārs) certifies | ~6-10 weeks | ~3-4%: state duty 1.5%/2% (cap €50,000); notar fees; cadastre (zemesgramata.lv) | Not used | None major |
| **RO** | Yes — notar public | ~4-8 weeks | ~3-5%: notar 0.4-2.2% regressive; impozit pe venit din transfer 1-3% (seller); ANCPI cadastre fees; **VAT 9% reduced for homes <€140k abolished 1 Jan 2025** [verify]; (anaf.ro) | Not used | **Tax reform 1 Aug 2025**: VAT 19→21%; reduced 9% housing window 1 Aug 2025–31 Jul 2026; PAID enforcement campaigns continue |
| **BG** | Yes — notarius (нотариус) | ~4-8 weeks | ~3-5%: data za prehvurlyane 0.1-3% (varies by municipality); notar fees regressive; вписване 0.1% (nra.bg) | Not used | **Eurozone entry 1 Jan 2026**; mandatory dual EUR/BGN display through ~Aug 2026 |
| **LU** | Yes — notaire | ~6-10 weeks | **~7-10%**: droit d'enregistrement 6% + droit de transcription 1% (effective 7%); Bëllegen Akt up to €40k credit per person primary residence; notaire ~1-1.5% (guichet.lu) | Not used | **Bëllegen Akt €40k permanent from 1 July 2025**; STR registration Law 28 Feb 2025 in force 1 Sep 2025 |
| **CY** | No notary in continental sense; **lawyer + Land Registry**; contract stamped; specific performance protected | ~6-12 weeks | **~5-10%**: transfer fees 3-8% (50% reduction since 2011 if VAT applies); VAT 19% (new) reduced to 5% for primary up to 130 sqm/€350k; Stamp Duty 0.15-0.2% (mof.gov.cy) | Title insurance rare; **title-deed delays** historic issue, improving | **Reduced VAT 5% scope tightened from Jun 2023** — €350k cap, 130sqm cap, 190sqm overall; **2026 Tax Reform** stamp duty largely abolished, CGT exemptions raised |
| **MT** | Yes — Notary (kuntratt) | ~3 months (konvenju → finali) | **~5-12%**: stamp duty 5% (resident) — first-time buyer exemption on first €200k; UCA/vacant 0% on first €750k (Jan 2025–Dec 2026); VAT 0% (residential exempt); notary ~1-2% (cfr.gov.mt) | Not used | **MEIN ECJ illegality 29 Apr 2025**; LRA reform 2025-2035 toward full compulsory registration; Tourism Accommodation Regs 2025 STR consolidation |

## Western Balkans

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **RS** | Yes — javni beležnik | ~4-8 weeks | ~3-5%: porez na prenos apsolutnih prava 2.5% (existing) or VAT 10% (new); notar fees regressive (poreska.gov.rs) | Not used | **eKatastar** digital registry mature; e-notarisation pilots [verify] |
| **ME** | Yes — notar | ~4-8 weeks | ~3-5%: porez na promet nepokretnosti **progressive 3/5/6% since 1 Jan 2024**; notar; cadastre (poreskauprava.gov.me) | Not used | RETT progressive structure 2024 |
| **BA** | Notar (Federation) or court (Republika Srpska) | ~6-12 weeks | ~3-7%: varies by entity (FBiH 5%, RS-entity 0%); legal/cadastre | Not used | None major announced |
| **MK** | Yes — notar | ~4-8 weeks | ~3-5%: data na promet 2-4% (varies by municipality); VAT 18% (new); notar; cadastre (ujp.gov.mk) | Not used | None major announced |
| **AL** | Yes — noter | ~4-8 weeks | ~3-5%: tatim mbi kalimin e të drejtës 2% (seller); noter; ZRPP cadastre (tatime.gov.al) | Not used | **ASHK** reform ongoing — historic title-clarity issues; iKadaster World Bank-supported end-2026 fully digital target |

## Anglo non-EU

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **CA** | No federal notary (except Quebec where notaire civil-law required); elsewhere lawyer / notary public (signature) | ~30-60 days (varies; QC longer) | **~2-4% + Land Transfer Tax**: LTT varies by province (Ontario 0.5-2.5% + Toronto municipal LTT same; BC 1-3% + 2% above $3m + 20% Foreign Buyers Tax); legal $1-2k; QC: notaire ~1-2% | **Title insurance standard** in ON, BC, AB; ~$200-500 one-time | **Federal foreign-buyer ban extended to 1 Jan 2027**; BC anti-flipping tax from 1 Jan 2025; FFIP flood-pool rollout; UHT filing rules updated 2024 |
| **AU** | No notary; solicitor or licensed conveyancer; state-by-state | ~30-90 days (cooling-off varies) | **~5-9% + Stamp Duty**: 1.25-7% (state-by-state, progressive); Foreign Investment Review Board fee + foreign-purchaser additional duty 7-8% (NSW/VIC); legal $1-2k | Title insurance available; ~$300-700; not standard but increasingly used | **NSW Property Tax option (replaces stamp duty for FHB)** continues; **Foreign-buyer ban on existing homes 1 Apr 2025 - 31 Mar 2027**; FIRB fees raised 2024 |
| **NZ** | No notary; solicitor | ~30-60 days | **~1-2%**: NO stamp duty; LINZ registration NZD 100-200; legal NZD 1,500-3,000 (linz.govt.nz) | Not standard | **Foreign-buyer ban remains** (Overseas Investment Amendment Act 2018); brightline test reverted to 2 years from 1 Jul 2024 (from 10 years); Natural Hazards Insurance Act 2023 in force 1 Jul 2024 |

## Latin America

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **MX** | Yes — Notario Público (federally licensed, restricted number per state) | ~30-60 days | **~5-10%**: ISAI (impuesto sobre adquisición) 2-5% varies by state; notario 1-2%; Registro Público 0.5-1%; **Fideicomiso (bank trust) for foreigners in restricted zone** ~$500-2,000 setup + annual | **Title insurance standard for foreign buyers** (Stewart, First American Mexico); domestic less common | Article 27 constitutional restriction (50km coast / 100km border) unchanged; fideicomiso 50-yr renewable; CFE/INFONAVIT digital integration |
| **BR** | Yes — Tabelião / Cartório (escritura pública) | ~30-90 days | **~5-7%**: ITBI 2-3% (municipal); cartório 1-2% (escritura + registro) | Not standard; cartório public-faith | **Cartório digitisation (CRA, ONR)** mature; e-CRBio property registry rollouts; CIB national identifier 2026 rollout |
| **AR** | Yes — Escribano público | ~30-60 days | **~6-8%**: ITI 1.5% (seller, except primary residence reinvested); sellos 1.5-4% varies by province; escribano 1-2% | Not standard | **Milei deregulation 2024-25**: rent law repeal (DNU 70/2023), USD-denominated mortgages reintroduced; **RIGI** for large investors; Blanqueo de capitales 2024 |
| **CR** | Yes — Notario Público (must be lawyer) | ~30-60 days | **~4-5%**: transfer tax 1.5%; stamp duties ~0.85%; notario ~1.25-2%; Registro Nacional 0.5% (hacienda.go.cr) | Title insurance available (Stewart, First American); used by foreign buyers | Concessions law (Maritime Zone) restrictions for foreigners unchanged; digital Registro Nacional services expanded |
| **PA** | Yes — Notario Público | ~30-60 days | **~4-7%**: transfer tax 2% (seller); ITBMS not on residential resale; notario ~1%; Registro Público 0.5% (dgi.mef.gob.pa) | Title insurance common for foreign buyers | None major announced [verify]; FATF grey-list exit 2023 improved bank processing; digital Registro Público |

---

## Notary-process gaps surfaced (cannot verify with primary source as of Apr 2026)

- UK SDLT exact threshold mechanics post-1 Apr 2025 (temporary £250k nil-rate band reverted to £125k; first-time-buyer relief threshold reverted from £625k to £500k)
- Irish Stamp Duty 2024 Budget specifics — bulk-buyer rate, mansion rate on portion above €1.5m
- Lithuanian / Latvian notary tariff updates 2024-25
- Romanian VAT 9% scope on housing — eliminated 1 Jan 2025 per Ordonanță 115/2023 [verify exact rules]
- Various Western Balkans rates — local tax authorities update annually
- Australian Foreign Investment Review Board fee schedule 2024-25
- Mexican ISAI rates by state — vary annually by municipal budgets

## Cross-cutting reforms calendar (Apr 2026 horizon)

- **EU AML 6th Directive (AMLA Regulation)** — direct supervision of high-risk gatekeepers including notaries from 2025-26; enhanced UBO checks for all property transactions
- **EU Energy Performance of Buildings Directive (EPBD recast 2024/1275)** — Member State transposition by 29 May 2026; affects sale/rent disclosure and minimum energy performance for worst-performing buildings
- **EU Mortgage Credit Directive review 2025** — climate-stress disclosure to borrowers
- **OECD Pillar Two and global minimum tax** — affects investor structures (REITs, SCI, etc.) but not retail buyers
- **DAC8 (crypto-asset reporting)** — implementation 2026; relevant where buyers fund via crypto
- **EU Digital Decade Targets 2030** — driving e-notary, e-cadastre, e-conveyancing across the bloc

## Confidence labels

- **HIGH**: notary requirement + closing-cost structure verified via official authority URL within last 12 months
- **MEDIUM**: secondary aggregator (PwC/KPMG/Global Property Guide); 12-24 months
- **LOW**: ranges only or proposed-but-not-enacted

## Status

Last refreshed: 2026-04-26. Next refresh: per-event (each tax-rate change), annually otherwise.
