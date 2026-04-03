# P1 Expansion Pass

Tento súbor dopĺňa literature bundle o konkrétne citekey-ready zdroje pre najkritickejšie gaps. Cieľ nie je mať finálnu úplnú bibliografiu, ale pripraviť prvý pevný balík zdrojov, ktorý sa dá hneď importovať do Zotera a použiť pri písaní.

## Ako tento pass používať

1. Importuj alebo manuálne založ tieto zdroje v Zotere.
2. Uzamkni citekeys presne v tvare uvedenom nižšie.
3. Kritické zdroje označ tagom `must-read`.
4. Po importe ich spáruj s klastrami v `source_clusters.md`.
5. Pri najdôležitejších položkách vytvor výpiskový súbor v `notes/literature/`.

---

## Gap A: klinické ukotvenie MDD a diferenciálna diagnostika

Tieto zdroje dopĺňajú už existujúce `kennedy2008coresymptoms`, `maj2020depressioncharacterization` a `guidi2011clinicalinterviewdepression`.

| Citekey | Zdroj | Identifikátor | Prečo presne sa hodí |
| --- | --- | --- | --- |
| `mcintyre2019mddvsbipolar` | McIntyre, R. S., Zimmerman, M., Goldberg, J. F., & First, M. B. (2019). *Differential Diagnosis of Major Depressive Disorder Versus Bipolar Disorder: Current Status and Best Clinical Practices.* Journal of Clinical Psychiatry, 80(3). | PMID `31091027`, DOI `10.4088/JCP.ot18043ah2` | Priamy zdroj k rozlišovaniu unipolárnej depresie a bipolárnej depresie. Hodí sa na obhájenie, prečo seedy a exclusion pravidlá nemajú nekriticky miešať bipolárne znaky s MDD. |
| `hirschfeld2014bipolardifferential` | Hirschfeld, R. M. (2014). *Differential diagnosis of bipolar disorder and major depressive disorder.* Journal of Affective Disorders, 169 Suppl 1, S12-S16. | PMID `25533909`, DOI `10.1016/S0165-0327(14)70004-7` | Krátky a praktický klinický zdroj k diagnostickým omylom medzi MDD a bipolárnou poruchou. Dobre sa hodí do úvodu aj do metodického odôvodnenia seed constraints. |
| `stein2021anxietycharacterization` | Stein, D. J., Craske, M. G., Rothbaum, B. O., et al. (2021). *The clinical characterization of the adult patient with an anxiety or related disorder aimed at personalization of management.* World Psychiatry, 20(3), 336-356. | PMID `34505377`, PMCID `PMC8429350`, DOI `10.1002/wps.20919` | Hodí sa na opatrné odlíšenie depresívnej symptomatiky od anxiety-related presentations. Je užitočný pre diskusiu komorbidity aj pre argument, že samotná distresová alebo úzkostná línia nestačí ako ekvivalent MDD. |
| `dubovsky2021psychoticdepression` | Dubovsky, S. L., Ghosh, B. M., Serotte, J. C., & Cranwell, V. (2021). *Psychotic Depression: Diagnosis, Differential Diagnosis, and Treatment.* Psychotherapy and Psychosomatics, 90(3), 160-177. | PMID `33166960`, DOI `10.1159/000511348` | Dôležitý zdroj pre psychotické črty, diferenciálnu diagnostiku a hranice medzi psychotic depression a inými klinickými obrazmi. Vhodný na obhájenie red-flag a exclusion prvkov v seed scenároch. |

---

## Gap B: content validity a expert validation rating nástroja

Tieto zdroje dopĺňajú už existujúce `COSMIN` položky v `source_clusters.md`.

| Citekey | Zdroj | Identifikátor | Prečo presne sa hodí |
| --- | --- | --- | --- |
| `lynn1986contentvalidity` | Lynn, M. R. (1986). *Determination and quantification of content validity.* Nursing Research, 35(6), 382-385. | PMID `3640358`, DOI `10.1097/00006199-198611000-00017` | Klasický základ pre expert judgement a content validity pri tvorbe nového nástroja. Hodí sa na stručné metodické ukotvenie toho, prečo expert panel vôbec používaš. |
| `polit2007cvi` | Polit, D. F., Beck, C. T., & Owen, S. V. (2007). *Is the CVI an acceptable indicator of content validity? Appraisal and recommendations.* Research in Nursing & Health, 30(4), 459-467. | PMID `17654487`, DOI `10.1002/nur.20199` | Najpraktickejší zdroj k I-CVI a S-CVI. Umožní ti pomenovať číselné alebo poločíselné jadro pilotnej obsahovej validity, ak sa rozhodneš reportovať expert ratings systematickejšie. |
| `hasson2000delphi` | Hasson, F., Keeney, S., & McKenna, H. (2000). *Research guidelines for the Delphi survey technique.* Journal of Advanced Nursing, 32(4), 1008-1015. | PMID `11095242`, DOI `10.1046/j.1365-2648.2000.t01-1-01567.x` | Užitočné pre framing, ak refine položiek alebo expertné pripomienky mali aspoň čiastočne konsenzuálny charakter. Pomáha presne povedať, čo je Delphi-like a čo ešte nie je plný Delphi dizajn. |
| `boateng2018scaledevelopment` | Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). *Best Practices for Developing and Validating Scales for Health, Social, and Behavioral Research: A Primer.* Frontiers in Public Health, 6, 149. | PMID `29942800`, PMCID `PMC6004510`, DOI `10.3389/fpubh.2018.00149` | Výborný most medzi psychometriou a praktickým výskumným workflow. Hodí sa na širší opis vývoja autorského rating nástroja a na obranu, že ide o pilotný vývoj, nie finálne validovaný scale. |
| `rutherfordhemming2015simulationcvi` | Rutherford-Hemming, T. (2015). *Determining Content Validity and Reporting a Content Validity Index for Simulation Scenarios.* Nursing Education Perspectives, 36(6), 389-393. | PMID `26753299`, DOI `10.5480/15-1640` | Mimoriadne vhodné pre tento projekt, lebo prepája CVI priamo so simulovanými scenármi. Pomôže ti obhájiť validáciu nástroja aj stimulusového materiálu v simulačnom kontexte. |

---

## Gap C: simulated patients a virtual patient framing

Tieto zdroje dopĺňajú už existujúce `yu2025simulatedpatientsystems`, `brugge2024patientsimulation`, `williams2017simulationmentalhealth` a `dawood2024standardizedpatient`.

| Citekey | Zdroj | Identifikátor | Prečo presne sa hodí |
| --- | --- | --- | --- |
| `cook2010computerizedvirtualpatients` | Cook, D. A., Erwin, P. J., & Triola, M. M. (2010). *Computerized virtual patients in health professions education: a systematic review and meta-analysis.* Academic Medicine, 85(10), 1589-1602. | PMID `20703150`, DOI `10.1097/ACM.0b013e3181edfe13` | Starší, ale konceptuálne veľmi silný zdroj k virtual patients ako edukačnému artefaktu. Pomáha ukotviť tvoju prácu v línii simulácie, nie len generovania textu. |
| `kononowicz2019virtualpatients` | Kononowicz, A. A., Woodham, L. A., Edelbring, S., et al. (2019). *Virtual Patient Simulations in Health Professions Education: Systematic Review and Meta-Analysis by the Digital Health Education Collaboration.* Journal of Medical Internet Research, 21(7), e14676. | PMID `31267981`, PMCID `PMC6632099`, DOI `10.2196/14676` | Novší systematický prehľad k virtual patient simulations. Hodí sa na argument o educational usefulness, skill outcomes a limite heterogénnych dizajnov. |

---

## Gap D: safety, non-diagnostic framing a human oversight

Tieto zdroje sa majú používať spolu s už existujúcimi `roustan2025cliniciansguide`, `asgari2025hallucinationframework`, `guo2024llmmentalhealth` a `omar2024llmpsychiatry`.

| Citekey | Zdroj | Identifikátor | Prečo presne sa hodí |
| --- | --- | --- | --- |
| `who2021ethicsaiforhealth` | World Health Organization. (2021). *Ethics and governance of artificial intelligence for health.* | URL `https://www.who.int/publications/i/item/9789240029200` | Autoritatívny rámec pre etiku, governance, zodpovednosť a ľudský dohľad. Hodí sa na všeobecnú oporu pre non-diagnostic framing a zdravotnícky kontext. |
| `who2024lmmguidance` | World Health Organization. (2024). *Ethics and governance of artificial intelligence for health: guidance on large multi-modal models.* | URL `https://iris.who.int/handle/10665/375579` | Priamo relevantný zdroj ku generatívnym modelom a ich využitiu v zdravotníctve vrátane vzdelávania, simulácie a rizík. Dáva silný rámec pre tvrdenie, že rozhodujúci musí zostať human oversight. |
| `goddard2012automationbias` | Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). *Automation bias: a systematic review of frequency, effect mediators, and mitigators.* Journal of the American Medical Informatics Association, 19(1), 121-127. | PMID `21685142`, PMCID `PMC3240751`, DOI `10.1136/amiajnl-2011-000089` | Výborný zdroj na vysvetlenie rizika prehnanej dôvery v automatizované výstupy. Vhodný do Limitation a Ethics sekcií ako obrana proti nekritickému prijímaniu AI výstupov. |
| `howell2024genaipatientsafety` | Howell, M. D. (2024). *Generative artificial intelligence, patient safety and healthcare quality: a review.* BMJ Quality & Safety, 33(11), 748-754. | PMID `39048292`, PMCID `PMC11503140`, DOI `10.1136/bmjqs-2023-016690` | Spája generatívnu AI s patient safety a quality-of-care perspektívou. Hodí sa na zdôvodnenie, prečo tvoja práca zostáva v tréningovo-výskumnom, nie diagnostickom režime. |
| `khera2023automationbiasassistiveai` | Khera, R., Simon, M. A., & Ross, J. S. (2023). *Automation Bias and Assistive AI: Risk of Harm From AI-Driven Clinical Decision Support.* JAMA, 330(23), 2255-2257. | PMID `38112824`, DOI `10.1001/jama.2023.22557` | Krátky, ale veľmi priamo použiteľný komentár k riziku škody pri AI asistencii v klinickom rozhodovaní. Hodí sa ako ostrý citačný oporný bod pre vetu o tom, prečo AI nemá v tejto práci autonómnu klinickú rolu. |

---

## Gap E: agreement metrics pri ordinálnych expert ratingoch

Tieto zdroje dopĺňajú už existujúci `koo2016icc`.

| Citekey | Zdroj | Identifikátor | Prečo presne sa hodí |
| --- | --- | --- | --- |
| `mchugh2012kappa` | McHugh, M. L. (2012). *Interrater reliability: the kappa statistic.* Biochemia Medica, 22(3), 276-282. | PMID `23092060`, PMCID `PMC3900052` | Najprístupnejší zdroj na vysvetlenie, čo kappa robí a čo nerieši. Hodí sa do textu, ak budeš chcieť čitateľne vysvetliť, prečo samotné percent agreement nestačí. |
| `jakobsson2005ordinalagreement` | Jakobsson, U., & Westergren, A. (2005). *Statistical methods for assessing agreement for ordinal data.* Scandinavian Journal of Caring Sciences, 19(4), 427-431. | PMID `16324069`, DOI `10.1111/j.1471-6712.2005.00368.x` | Stručný metodický zdroj priamo k ordinálnym dátam. Hodí sa, ak budeš potrebovať obhájiť výber medzi weighted kappa, ICC a inými prístupmi. |
| `marasini2016weightedindexes` | Marasini, D., Quatto, P., & Ripamonti, E. (2016). *Assessing the inter-rater agreement for ordinal data through weighted indexes.* Statistical Methods in Medical Research, 25(6), 2611-2633. | PMID `24740999`, DOI `10.1177/0962280214529560` | Dôležitý zdroj, ak chceš explicitne riešiť weighted agreement pri ordinálnych škálach. Silný oporný bod pre argument, že ordinálne ratingy si zaslúžia jemnejšie metriky než jednoduché ICC bez diskusie. |
| `nelson2015manyratersordinal` | Nelson, K. P., & Edwards, D. (2015). *Measures of agreement between many raters for ordinal classifications.* Statistics in Medicine, 34(23), 3116-3132. | PMID `26095449`, PMCID `PMC4560692`, DOI `10.1002/sim.6546` | Priamo relevantné pre dizajn s viacerými expert raters a ordinálnymi kategóriami. Hodí sa na obhajobu viacraterového agreement rámca. |
| `mitani2017ordinalsummarymeasures` | Mitani, A. A., Freer, P. E., & Nelson, K. P. (2017). *Summary measures of agreement and association between many raters' ordinal classifications.* Annals of Epidemiology, 27(10), 677-685.e4. | PMID `29029991`, PMCID `PMC5687310`, DOI `10.1016/j.annepidem.2017.09.001` | Užitočný zdroj pre situáciu, kde chceš rozlišovať agreement a association medzi viacerými ratermi. Metodicky sa hodí k interpretácii ordinal ratings v Results a pri obhajobe. |

---

## Odporúčaný prvý import batch

Ak chceš spraviť najprv minimum s najvyšším payoffom, importuj najprv tieto citekeys:

- `mcintyre2019mddvsbipolar`
- `dubovsky2021psychoticdepression`
- `polit2007cvi`
- `boateng2018scaledevelopment`
- `rutherfordhemming2015simulationcvi`
- `kononowicz2019virtualpatients`
- `who2021ethicsaiforhealth`
- `who2024lmmguidance`
- `goddard2012automationbias`
- `jakobsson2005ordinalagreement`
- `nelson2015manyratersordinal`

## Čo týmto passom získaš

- silnejšie klinické ukotvenie seedov a symptom domén,
- obhájiteľnejší popis pilotnej validity rating nástroja,
- pevnejší framing práce ako simulation/training artifact,
- explicitný safety a human-oversight rámec,
- presvedčivejšiu metodickú obranu pri ordinálnych ratingoch.
