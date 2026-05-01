# Universal `--notary` Section

Per-country property-transaction process across all supported countries: notary or equivalent requirement, typical timeline from accepted offer to registered deed, total closing-cost percentage, title-insurance practice, and 2025-2026 process reforms.

**Snapshot**: April 2026; Tier-1 + Tier-2 expansion 2026-05-01.

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
| **DO** | Yes — Notario Público (must be lawyer-notary, exequatur de notario); independent buyer-side abogado strongly advised | ~30-90 days | **~4-5%**: impuesto de transferencia 3% (Ley 288-04) on Avalúo Catastral; Registro de Títulos ~1%; notario 1-1.5%; legal 1% (dgii.gov.do) | Title insurance available (Stewart, First American DR); used by foreign buyers, particularly for **Constancia Anotada** parcels lacking saneamiento | **CONFOTUR Ley 158-01 / 195-13** continues — 15-yr IPI + transfer-tax exemption for tourist-zone projects; saneamiento → Matrícula migration ongoing |
| **CO** | Yes — Notario público + ORIP (Oficina de Registro de Instrumentos Públicos), supervised by SNR | ~30-60 days | **~2-4%**: gastos notariales 0.27% (Decreto 0188/2017, split 50/50); impuesto de registro **0.5-1.0%** (Bogotá 1%); retención en la fuente 1% (when seller is sociedad); legal 1-2% (supernotariado.gov.co) | Title insurance rare; CTL (Certificado de Tradición y Libertad) from ORIP serves as title-chain proof | Annual SNR Resolución updates tarifas; **estudio de títulos** (30-yr title chain) standard step |
| **UY** | Yes — Escribano público mandatory (buyer chooses per custom); profession regulated by AEU | ~60-90 days | **~6-8%**: ITP 4% (2% buyer + 2% seller, Ley 16.107); escribano ~3% of price (AEU barème); Registro de Propiedad ~0.5%; legal 1% (aeu.org.uy) | Not standard; escribano runs título chain via Registro de la Propiedad | **Ley 19.567 (2017)** Vivienda Promovida tax incentives continue; **Ley 18.795** social-interest housing exemptions; no major 2025 reform |
| **CL** | Yes — Notario + Conservador de Bienes Raíces (CBR, territorial — ~70 nationally; e.g., CBR Santiago) | ~30-60 days | **~3-5%**: notario ~1.2%; CBR 0.2-0.7% regressive; **impuesto del timbre 0.8%** on mortgage (Decreto Ley 3.475); legal 1% (conservadores.cl) | Not standard; CBR registry public-faith — title via Foja/Número/Año | **Ley 21.420 (2022)** eliminated DFL2 benefit (transfer-tax exemption) for >2 properties; **sobretasa** on aggregate residential >UF 670 raised to 0.275-0.425% per Ley 21.210 — annual SII payable |

## North America (federal — state-level overrides)

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **US** | No federal notary; **state-by-state** — three regimes: (i) **escrow states** (CA, AZ, OR, WA — neutral escrow holds funds + docs); (ii) **attorney states** (NY, MA, GA, SC, NC + others — closing attorney mandatory); (iii) **title-company states** (most others — title company runs settlement) | **30-45 days typical** (financed); 14-30 days cash | **~2-5% buyer-side + Land/Real-Estate Transfer Tax**: settlement/closing fee $300-1,500; recording fee $20-300/document (county-set); state/county transfer tax 0-2.5% (none in 12 states; highest DC, DE, NY, CT); ALTA owner's title-insurance one-time ~0.3-0.7% of price; lender's title insurance lender-required where mortgage financed (irs.gov, alta.org) | **Title insurance MANDATORY** when lender financing (lender's policy); owner's policy strongly recommended and standard in most resale deals — ALTA forms; one-time premium at closing | **NAR settlement Aug 2024** — buyer-agent commission must be negotiated separately, no longer auto-published in MLS; many states updated standard contracts. **CTA Beneficial Ownership Information (BOI) reporting** under FinCEN — most domestic-entity reporting nullified by Mar 2025 interim final rule (foreign-entity-only); verify at `fincen.gov`. **NYC FARE Act 1 Nov 2024** — broker fees shift from tenants to landlord-payers. Per-state property-tax + transfer-tax overhauls vary annually |

## Middle East / North Africa

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **TR** | No civil-law notary for the deed itself; **Tapu Müdürlüğü (TKGM)** registration is constitutive — same-day deed transfer once docs ready (sworn translator required for foreign buyers) | **Same day** at Tapu office once Web Tapu file complete; total prep ~2-6 weeks | **~5-8%**: Tapu Harcı **4% of declared sale value** (statutory split 2% buyer + 2% seller — buyer often pays full 4%); döner sermaye fee ~TRY 4,000 (2025); sworn translator 2,000-5,000 TRY; legal 0.5-1.5%; KDV 1/10/20% on new builds (tkgm.gov.tr) | Not used; Tapu register is public-faith (Articles 1023-1024 TMK) | **2017 CBI** continues at $400k threshold (raised from $250k in 2022); **Web Tapu e-Devlet integration** enables remote pre-checks; **Yeni Tapu Senedi format 2024** [verify] — QR-coded |
| **AE** | No civil-law notary; **DLD (Dubai)** / **ADREC (Abu Dhabi)** — Trustee Office handles same-day transfer; **Sharjah Real Estate Reg.** + **RAK Municipality** for those emirates | **Same day** at Trustee Office (Dubai) once NOC + funds + docs ready; off-plan via **Oqood** interim registration | **~7-10% (Dubai)**: DLD transfer fee **4% of price** (split 50/50 by statute, buyer pays in practice); Trustee Office fee AED 4,000 (>500k) / AED 2,000 (<500k); title-deed issuance AED 580; mortgage registration 0.25% (if financed); broker 2%; conveyancer AED 6,000-15,000 (dubailand.gov.ae) | Not used; DLD/ADREC registers public-faith | **Dubai Law No. 7 of 2023** — extended foreign freehold areas; **Dubai Law No. 2 of 2025** — DIFC Wills directly enforceable against DLD; **5% housing fee** levied on annual rent (Dubai), 3% Abu Dhabi — applies to occupiers; **2% Dubai Land Department admin charge** deprecated |
| **IL** | Lawyer (עורך דין מקרקעין) drafts and represents both sides; **Tabu / Land Registry** + **RMI (Israel Land Authority)** for state-leased land — **dual title system** | **60-120 days** (longer for state-leased land needing RMI consent) | **~6-12%**: **Mas Rechisha (purchase tax)** progressive — non-resident scale higher than resident; Olim 7-yr discount (Sec. 12 Land Tax Regulations); attorney **0.5-2%** + 18% VAT; Tabu registration ILS 11/nesach (taboo.gov.il); RMI capitalization fee where applicable; broker 2% + VAT (gov.il/he/departments/topics/real_estate_taxation) | Not used; Tabu register public-faith for chofshi; RMI register for hachira | **Decision 1185 Heskem Hadash** continues (state-leased → freehold conversion); annual Mas Rechisha bracket update mid-January (CBS-indexed); **war-driven insurance disruption since Oct 2023** — Karnit / Property Tax Compensation Fund covers missile damage but private insurers limit non-mandatory cover |
| **MA** | Yes — **Notaire** (modern, for titré) OR **Adoul** (Islamic notary, for melkia — avoid for foreign buyers); **ANCFCC** registers titre foncier | **60-120 days** (longer if non-titré → réquisition d'immatriculation 6-24 months) | **~6-10%**: **enregistrement (droits)** **4%** (residential, Code de l'enregistrement); **conservation foncière 1.5% + 150 MAD** certificate (ancfcc.gov.ma); **notaire 0.5-1% + 20% TVA** on fee (Ordre National des Notaires barème); timbre ~20 MAD/page; agent 2.5% + 20% TVA (tax.gov.ma) | Not used; ANCFCC titre foncier is Torrens-style indefeasible | **2002 ANCFCC creation** consolidated colonial Conservation Foncière; ongoing **immatriculation campaigns** to convert melkia → titré; **Loi 39-08 Code des droits réels** mature; CGT exemption for primary-residence holding ≥6 years |
| **EG** | Notarization at **REPA (Real Estate Publicity Authority — مصلحة الشهر العقاري والتوثيق)** office; lawyer-drafted contract (`عقد ابتدائي`) typical; **dual-system gap** between sijil al-shakhsi (deed-recording, ~95%) and sijil al-‘ayni (Torrens-like, ~5-10%) | **90-180 days** (slow; longer for non-‘ayni properties or foreign-currency Form 4 verification) | **~6-9%**: **stamp duty / rasm tasgil 2.5%** of declared price (3% in some categories); notary fees included in registration; **lawyer 1-3%** (foreign buyer must retain independent counsel); brokerage 2.5-5%; declared price typically understated 30-50% (sherpa.gov.eg) | Not available in Egyptian market; sijil al-shakhsi gives weaker title than al-‘ayni — verification by lawyer at REPA is the substitute | **Form 4 USD-tracking** mandatory for foreign-currency property purchases (CBE FX regime); **citizenship-by-real-estate** $300k threshold (Decree 1191/2023); REPA digitisation continues but coverage of sijil al-‘ayni still <10% nationally |

## Caucasus / Central Asia

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **GE** | **Optional** — NAPR (National Agency of Public Registry) registration is constitutive; notarised contract not mandatory; **PSDA (Public Service Hall)** processes filings | **Same hour** possible — **1-hour express transfer** at PSDA (500 GEL fee); standard 200 GEL same-day; 50 GEL ~4 working days (uniquely fast globally) | **~0.1-0.5%** (among the lowest worldwide): **NO transfer tax** (Tax Code); NAPR registration 50/200/500 GEL; notary optional 0.05-0.5% (Notarial Chamber); agent 3-5% (seller side typical); 18% VAT only on new-build by VAT-registered developer (napr.gov.ge) | Not used; NAPR register public-faith; English-language extracts available | **EU candidate status (Dec 2023)** — harmonisation pressure may introduce transfer tax over medium term, no concrete bill 2025; **investment residence permit** thresholds USD 100k / USD 300k continue |

## East Asia

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **JP** | **司法書士 (shihoshoshi — judicial scrivener)** mandatory in practice for 登記 (registration) at 法務局 (Legal Affairs Bureau); no civil-law notary on the deed (kōshōnin only for wills); 重要事項説明 by 宅地建物取引士 (Takken) | **30-45 days** typical (contract → registration); shorter for cash, longer for mortgage | **~6-10%**: **不動産取得税 3%** (residential land + house, until 2027-03-31; standard 4%); **登録免許税** land 1.5% (until 2026-03-31, std 2%) + building 0.3% (existing residential, until 2027-03-31); **印紙税** ¥10k-60k flat; 司法書士 ¥50k-150k; 仲介手数料 max 3% + ¥60k + 10% 消費税 (mof.go.jp, moj.go.jp) | Not used; 登記簿 (registry) at 法務局 is public-faith | **2024 民法・不動産登記法改正** (effective 2024-04-01) — mandatory inheritance registration within 3 years (¥50k fine); address-change registration within 2 years; aimed at solving 所有者不明土地 (~23% of all JP land); **管理不全空家** designation revokes residential-land tax exemption |

## Southeast Asia

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **TH** | No civil-law notary (Thailand has no notary profession in the European sense); **Land Office (Department of Lands, กรมที่ดิน)** processes same-day transfer; lawyer drafts contract; sworn translator for foreign buyers | **Same day** at Land Office once docs + FET form + Foreign Quota Cert ready; total prep 30-60 days | **~6-8% (split buyer/seller per contract)**: **transfer fee 2%** of appraised value (kept reduced 0.01% for some categories through 2024 — now reverted); **SBT (Specific Business Tax) 3.3%** if seller held <5 yrs; **stamp duty 0.5%** if SBT not applicable; **WHT 1%** (juristic) or progressive PIT (individual seller); FET form mandatory for foreign buyers ≥USD 50k inbound (treasury.go.th, bot.or.th) | Not used; Chanote title (Nor Sor 4 Jor) at Land Office is the title proof; foreigners restricted to condo within 49% project quota | **Land and Building Tax Act BE 2562 (2019)** — first national property tax, effective 2020; **proposed 99-year lease** (2024-2025) for foreigners under cabinet review, **not enacted as of May 2026**; **anti-nominee enforcement** intensified 2023-2024 (Phuket, Koh Samui) |
| **ID** | Yes — **PPAT (Pejabat Pembuat Akta Tanah)** notary mandatory for **AJB (Akta Jual Beli)**; BPN (Badan Pertanahan Nasional / Kementerian ATR/BPN) registers; sworn translator for foreign buyers | **2-6 months** (longer for HGB-conversion or PPJB → AJB sequences in pre-construction) | **~10-14%**: **BPHTB 5%** of NJOP-NPOPTKP (Bea Perolehan Hak atas Tanah dan Bangunan, **UU HKPD 1/2022**); **PPh Final 2.5%** seller; PPN 11% on new-build by PKP developer (since Apr 2022); PPnBM on luxury; PPAT notary 0.5-1%; BPN registration ~0.2% (atrbpn.go.id) | Not used; sertifikat from BPN (Hak Pakai for foreigners; Hak Milik citizens-only) | **PP 18/2021** overhauled foreign Hak Pakai → 30+20+30 = 80 yr max; **UU HKPD 1/2022** restructured local taxes — full implementation 1 Jan 2024; **Bali PN nominee-voidance precedents 2023-2025** — Hak Milik nominee structures voided, foreigner loses principal |
| **MY** | No civil-law notary; **lawyer's MOT (Memorandum of Transfer)** registered at state Land Office; SPA → MOT → registration sequence | **6-12 weeks** typical (longer if §433B state-consent required for foreign buyer) | **~5-8% (foreigners)**: **MOT stamp duty 4% flat** for foreigners (Stamp Act 1949 + Finance Act amendments — verify at LHDN, hasil.gov.my); legal 0.5-1% on SPA + 0.5-1% on loan agreement; state-consent fee MYR 1,000-10,000; valuation; SST 8% on services since 1 Mar 2024 (mysst.customs.gov.my) | Not used; geran (title) at state Land Office is public-faith | **MM2H relaunched June 2024** (3-tier Silver/Gold/Platinum under MOTAC); **state-set foreigner minimum-purchase-price** varies MYR 500k-3M (state EXCO circulars); **§433B consent** processing 4-12 weeks |
| **VN** | Yes — **notary office (công chứng)** mandates notarised sale contract (Civil Code Art. 459, Notary Law 2014/2024 amendments); provincial Land Registry (VPĐKĐĐ) issues **Sổ Hồng (Pink Book)** | **30-60 days** (notarisation) + **3-12 months** for Pink Book issuance to foreign buyers (provincial backlog) | **~4-6%**: **registration fee 0.5%** (lệ phí trước bạ, Decree 10/2022/ND-CP); **transfer tax / personal income tax 2%** of contract value (seller); notary 0.1-0.3% (regressive cap); legal 1-2% (monre.gov.vn) | Not used; Sổ Hồng is the State-issued certificate of Land Use Right | **2024 Land Law (Law 31/2024/QH15)** + **2023 Housing Law (Law 27/2023/QH15)** both effective **1 Aug 2025** (advanced from 1 Jan 2025); Decree 101/2024/ND-CP — foreign mortgage rights expanded to 100% foreign-owned credit institutions; **30% per block / 250 landed houses per ward** foreigner quotas continue |
| **PH** | Notarial acknowledgment of **Deed of Absolute Sale** (lawyer-notary); registered at **LRA Registry of Deeds** (Torrens system, PD 1529); titles drafted in English | **60-90 days** (BIR clearance + RD registration) | **~9-10%**: **CGT 6%** on higher of GSP/zonal/FMV (seller); **DST 1.5%** (NIRC §196); **local transfer tax 0.5%** (provinces) / **0.75%** (cities + Metro Manila); **registration fee ~0.25%** (LRA graduated schedule); legal 1-2% (lra.gov.ph, bir.gov.ph) | Not standard; Torrens TCT/CCT from LRA RD is the indefeasible title | **RA 12001 Real Property Valuation Reform Act (Jun 2024)** — uniform valuation across LGUs, phased through 2027; **40% foreign quota** on condominium projects (RA 4726) continues; **anti-dummy law (CA 108)** strict on Filipino-quota land structures |

## Africa

| Country | Notary required | Days offer→deed | Closing-cost % | Title insurance | 2025-26 reforms |
|---|---|---|---|---|---|
| **ZA** | No civil-law notary; **Conveyancer (admitted attorney + Conveyancing exam)** mandatory at one of the **Deeds Offices** (Cape Town, Pretoria, Johannesburg + 8 others); FICA AML on source of funds | **60-90 days** typical (Rates Clearance + bond reg + Deeds Office lodgment) | **~4-7% buyer-side**: **Transfer Duty SARS Schedule 8** (progressive — 0% to R1.21M, then 3-13% bands; sars.gov.za); conveyancer R20-50k + VAT (Law Society guideline); Deeds Office reg ~R1-2k; bond reg attorney R20-50k + VAT (if financed); bank initiation ~R6k. **Mandatory CoCs** at sale: Beetle (coastal — W. Cape, KZN, E. Cape, Garden Route), Electrical (national, OHS Act + EI Regs 2009, 2-yr validity), Plumbing (CoCT + others), Gas (where applicable); Rates Clearance Certificate (transfer cannot register without it, 60-day validity); Body Corporate Levy Clearance for sectional title | Not standard; Deeds Office register public-faith | **Non-resident seller withholding** 7.5% (natural) / 10% (company) / 15% (trust) on >R2M sales (s35A ITA); 2025/26 Transfer Duty brackets per SARS Budget; ongoing **eDeeds** rollout (Deeds Office digitisation) |

---

## Notary-process gaps surfaced (cannot verify with primary source as of Apr 2026)

- UK SDLT exact threshold mechanics post-1 Apr 2025 (temporary £250k nil-rate band reverted to £125k; first-time-buyer relief threshold reverted from £625k to £500k)
- Irish Stamp Duty 2024 Budget specifics — bulk-buyer rate, mansion rate on portion above €1.5m
- Lithuanian / Latvian notary tariff updates 2024-25
- Romanian VAT 9% scope on housing — eliminated 1 Jan 2025 per Ordonanță 115/2023 [verify exact rules]
- Various Western Balkans rates — local tax authorities update annually
- Australian Foreign Investment Review Board fee schedule 2024-25
- Mexican ISAI rates by state — vary annually by municipal budgets
- US state/county transfer-tax + recording-fee schedules — vary by 50 states + thousands of counties; per-state playbooks needed for parcel-level estimate
- TR Tapu Harcı declared-value vs market-value gap — under-declaration triggers GİB ceza, but rayiç bedel floors vary by belediye and update annually
- AE off-plan Oqood → Title Deed handover timeline — developer-specific; verify Escrow Account closure under RERA
- IL annual Mas Rechisha bracket update (mid-January CBS-indexed) — exact non-resident scale for current year requires Tax Authority dynamic-collector page
- MA droit d'enregistrement category-specific rates (4% standard, 3% social housing, 1% certain reductions) — verify per transaction at DGI
- EG stamp-duty / rasm tasgil exact rate (2.5% vs 3% category boundary) — adjusted multiple times in recent years; verify per transaction at REPA
- ID BPHTB local-government variation (UU HKPD 1/2022 sets ceiling at 5%; some LGUs lower) and PPN exemption windows for first-time + low-cost housing
- MY state-foreigner thresholds — circulars updated each state-budget cycle; SPA-binding figure must come from state EXCO
- VN Decree 102/2024/ND-CP + 95/2024/ND-CP implementing details for foreign buyers (Pink Book issuance timeline, mortgage rules) — provincial backlog variation
- PH BIR zonal value updates — per RDO; LGU FMV on different cycle; "highest-of" tax base requires fresh lookup
- TH DOL transfer-fee waivers / SBT discounts — periodic stimulus measures (recently expired); verify current Royal Decree at filing
- ZA SARS Transfer Duty brackets — annual Budget update each Feb-Mar; 2026/27 schedule pending

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

Last refreshed: 2026-05-01 (Tier-1 + Tier-2 expansion: US, TR, AE, JP, TH, DO, CO, UY, CL, ZA, GE, ID, MY, VN, PH, IL, MA, EG added). Prior refresh: 2026-04-26. Next refresh: per-event (each tax-rate change), annually otherwise.

**Confidence**: HIGH for civil-law notary requirement + headline rate brackets (Tapu Harcı 4%, BPHTB 5%, ITP 4% UY, Tabu/RMI dual system, etc. — all verified to primary statute or authority URL). MEDIUM for closing-cost ranges (regressive notary tariffs, regional/state variation). LOW for proposed-but-not-enacted reforms (TH 99-yr lease, IL non-resident bracket adjustments). Always re-verify per transaction.
