# 71 Public Appendix Draft / Verejné prílohy

> Pracovný draft verejného appendix balíka pre Word. Zámerne obsahuje len public-safe verzie príloh a nepreberá interné runtime pravidlá, plný seed corpus ani plné transkripty.

## Príloha A
**Finálny ratingový dotazník použitý pri expertnom hodnotení transkriptov**

Táto príloha uvádza public-safe verziu autorského ratingového nástroja. V prílohe je ponechaná obsahová logika položiek a blokov, ale nie technická implementácia v internom survey engine.

### A.1 Inštrukčný rámec pre hodnotiteľa

Hodnotiteľ posudzuje každý transkript ako celok. Nehodnotí len prítomnosť jednotlivých symptómov, ale aj to, či rozhovor pôsobí klinicky vierohodne, vnútorne konzistentne, prirodzene a použiteľne pre tréningový alebo výučbový účel.

Hodnotenie je rozdelené do troch blokov:

- globálne hodnotenie kvality rozhovoru,
- odhad celkovej závažnosti a funkčného dopadu,
- hodnotenie prítomnosti problematických prvkov a varovných signálov.

Položky `G1` až `G5`, `S1`, `S2`, `R1` až `R5` a položka istoty odhadu pôvodu rozhovoru sú hodnotené na 5-bodovej škále. Položka odhadovaného pôvodu rozhovoru je nominálna a komentár je otvorená textová odpoveď.

### A.2 Blok G: Globálne hodnotenie kvality rozhovoru

**Tabuľka A1**  
*Blok G: Globálne hodnotenie kvality rozhovoru*

| Kód | Položka | Typ odpovede |
| --- | --- | --- |
| `G1` | Klinická vierohodnosť rozhovoru | 5-bodová škála |
| `G2` | Prirodzenosť jazyka a štýlu odpovedí | 5-bodová škála |
| `G3` | Vnútorná konzistentnosť rozhovoru | 5-bodová škála |
| `G4` | Súlad rozhovoru s obrazom depresívnej symptomatiky | 5-bodová škála |
| `G5` | Použiteľnosť rozhovoru na tréningové alebo výučbové účely | 5-bodová škála |

### A.3 Blok S: Globálny odhad závažnosti a funkčného dopadu

**Tabuľka A2**  
*Blok S: Globálny odhad závažnosti a funkčného dopadu*

| Kód | Položka | Typ odpovede |
| --- | --- | --- |
| `S1` | Ľudský odhad celkovej závažnosti depresívnej symptomatiky | 5-bodová škála |
| `S2` | Ľudský odhad funkčného dopadu na bežné fungovanie | 5-bodová škála |

### A.4 Blok R: Problematické prvky a varovné signály

**Tabuľka A3**  
*Blok R: Problematické prvky a varovné signály*

| Kód | Položka | Typ odpovede |
| --- | --- | --- |
| `R1` | Prítomnosť vnútorných kontradikcií v rozhovore | 5-bodová škála |
| `R2` | Klišé alebo šablónovité odpovede | 5-bodová škála |
| `R3` | Nesúlad medzi kontextom a symptomatikou | 5-bodová škála |
| `R4` | Podozrenie na inú primárnu psychopatológiu | 5-bodová škála |
| `R5` | Neprimeraná dramatizácia alebo neprirodzená expresivita | 5-bodová škála |

### A.5 Doplnkové položky

**Tabuľka A4**  
*Doplnkové položky ratingového dotazníka*

| Premenná | Obsah | Typ odpovede |
| --- | --- | --- |
| `guessed_origin` | Odhad pôvodu rozhovoru | nominálna položka |
|  | Kategórie: `AI-generovaný`, `ľudsky simulovaný`, `reálny participant`, `neviem odhadnúť` |  |
| `guess_confidence` | Istota odhadu pôvodu rozhovoru | 5-bodová škála |
| `comment` | Otvorený komentár hodnotiteľa | voľný text |

### A.6 Poznámka k public-safe verzii

Do verejnej verzie prílohy nepatria:

- screenshoty interného survey engine,
- technické exportné názvy polí nad rámec potrebných kódov,
- interné workflow poznámky pre randomizáciu alebo distribúciu transkriptov.

## Príloha B
**Operacionalizačná tabuľka premenných, kompozitov a stručný preklad zmiešaných modelov**

**Tabuľka B1**  
*Prehľad premenných, outcome-ov a analytického použitia*

| Blok | Premenné | Škála | Význam | Analytické použitie |
| --- | --- | --- | --- | --- |
| Nezávislé premenné | prítomnosť štruktúrujúceho klinického usmernenia; štýl odpovedania simulovaného pacienta | binárna; kategóriálna s 3 úrovňami | experimentálne manipulované vlastnosti generovania rozhovoru | hlavné fixné efekty v mixed modeloch |
| Blokovacie a náhodné faktory | `seed_id`, `rater_id` | identifikátory | zdroj variability medzi seedmi a medzi hodnotiteľmi | random intercepts |
| Primárne outcome-y | `G1` až `G5`, index klinickej vierohodnosti | ordinálne položky; kompozit približne intervalový | globálna kvalita rozhovoru, prirodzenosť a tréningová použiteľnosť | deskriptíva, ordinal mixed models, lineárne zmiešané modely |
| Sekundárne outcome-y | `A1` až `A9`, priemerná absolútna chyba voči seedu, `S1`, `S2` | transcript-level `0-3`; ľudské ratingy `1-5` | zhoda rozhovoru s cieľovým symptomatickým profilom a samostatný ľudský odhad závažnosti a funkčného dopadu | transcript-level deskriptíva a modely; doplnkovo ordinal mixed models |
| Voliteľné sensitivity outcome-y | chyba odhadu závažnosti, chyba odhadu funkčného dopadu | odvodené numerické error skóre | doplnkové porovnanie ľudského odhadu s seed kotvami | supplement alebo secondary analysis |
| QC a defektové outcome-y | `R1` až `R5`, index defektov | ordinálne položky; kompozit približne intervalový | kontradikcie, klišé, nesúlad, iná psychopatológia, dramatizácia | deskriptíva, ordinal mixed models, lineárne zmiešané modely |
| Exploratórne outcome-y | odhad pôvodu rozhovoru, istota odhadu, komentár | nominálna; ordinálna; text | percepcia pôvodu rozhovoru a kvalitatívna spätná väzba | frekvencie, doplnkové modely, tematické kódovanie |

### B.1 Hlavné odvodené ukazovatele a ich konštrukcia

**Tabuľka B2**  
*Hlavné odvodené ukazovatele a ich konštrukcia*

| Ukazovateľ | Zdrojové premenné | Výpočet | Reportovaná úroveň | Interpretácia |
| --- | --- | --- | --- | --- |
| Index klinickej vierohodnosti | `G1`, `G3`, `G4` | `mean(G1, G3, G4)` | rating-level kompozit | vyššia hodnota znamená vyššiu klinickú vierohodnosť rozhovoru |
| Index defektov | `R1`, `R2`, `R3`, `R4`, `R5` | `mean(R1, R2, R3, R4, R5)` | rating-level kompozit | vyššia hodnota znamená vyšší výskyt defektov |
| Priemerná absolútna chyba v symptomatických doménach | `A1` až `A9` a `A1_anchor` až `A9_anchor` | `mean(abs(Ai - Ai_anchor))` pre `i = 1...9` | transcript-level ukazovateľ | nižšia hodnota znamená vyššiu zhodu so seed profilom |
| Chyba odhadu závažnosti | `S1`, `S1_anchor` | najprv `abs(S1 - S1_anchor)` pri jednotlivom hodnotení, potom priemer za prepis rozhovoru | transcript-level report z rating-level error skóre | nižšia hodnota znamená vyššiu zhodu so seed kotvou závažnosti |
| Chyba odhadu funkčného dopadu | `S2`, `S2_anchor` | najprv `abs(S2 - S2_anchor)` pri jednotlivom hodnotení, potom priemer za prepis rozhovoru | transcript-level report z rating-level error skóre | nižšia hodnota znamená vyššiu zhodu so seed kotvou funkčného dopadu |

Poznámka. Položky `S1` a `S2` ako samostatné ľudské ratingy ostávajú v hlavnej analytickej vetve ordinálnymi rating-level premennými. Na transcript-level sa presúvajú iba ich odvodené chybové verzie, aby anchor-fidelity vetva nevážila prepisy rozhovorov podľa počtu dostupných hodnotení. Položky `A1` až `A9` sú už od začiatku transcript-level metadata, nie opakované ľudské ratingy.

### B.2 Fixné a náhodné efekty v hlavných modeloch

**Tabuľka B3**  
*Fixné a náhodné efekty v hlavných modeloch*

| Prvok modelu | Typ | Význam |
| --- | --- | --- |
| `guardrail` | fixný efekt | rozdiel medzi `G0` a `G1`, teda medzi podmienkou bez a so štruktúrujúcim klinickým usmernením |
| `profile` | fixný efekt | rozdiel medzi štýlmi odpovedania `P1`, `P2` a `P3` |
| `guardrail × profile` | fixná interakcia | ukazuje, či sa efekt usmernenia mení podľa profilu odpovedania |
| `seed_id` | náhodný intercept | zohľadňuje, že niektoré východiskové scenáre môžu byť celkovo ľahšie alebo ťažšie hodnotené |
| `rater_id` | náhodný intercept | zohľadňuje, že niektorí hodnotitelia môžu byť prísnejší alebo miernejší |

### B.3 Základné modelové rovnice

Pri výstupných ukazovateľoch na úrovni jednotlivých hodnotení, najmä pri indexe klinickej vierohodnosti a indexe defektov, sa používa tento základný tvar lineárneho zmiešaného modelu:

`outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)`

Čítanie modelu je nasledovné: výsledný ukazovateľ vysvetľujeme klinickým usmernením, profilom odpovedania a ich interakciou, pričom zároveň dovolíme, aby sa priemerná úroveň hodnotení líšila medzi východiskovými scenármi a medzi hodnotiteľmi.

Pri výstupných ukazovateľoch na úrovni prepisu rozhovoru `symptom_error_mean`, `severity_error` a `impact_error` sa po agregácii na úroveň jedného prepisu rozhovoru používa tento tvar:

`outcome ~ guardrail * profile + (1 | seed_id)`

V tomto bloku už v modeli nevystupuje `rater_id`, pretože sledovaný ukazovateľ je najprv sumarizovaný na úroveň prepisu rozhovoru. Tento krok bráni tomu, aby prepisy rozhovorov s vyšším počtom hodnotení dostali väčšiu váhu len preto, že boli častejšie posúdené.

### B.4 Ako čítať koeficienty v interakčnom modeli

V hlavnom kódovaní je referenčnou kombináciou bunka `G0 × P1`, teda rozhovor bez štruktúrujúceho klinického usmernenia a so zdržanlivým štýlom odpovedania simulovaného pacienta.

**Tabuľka B4**  
*Základný preklad koeficientov v interakčnom modeli*

| Termín v tabuľke | Ako ho čítať |
| --- | --- |
| Intercept | odhad pre referenčnú kombináciu `G0 × P1` |
| `guardrail` | rozdiel `G1` oproti `G0` pri profile `P1` |
| koeficient pre `P2` | rozdiel `P2` oproti `P1` pri `G0` |
| koeficient pre `P3` | rozdiel `P3` oproti `P1` pri `G0` |
| interakcia `G1 × P2` | o koľko sa efekt usmernenia v `P2` mení oproti `P1` |
| interakcia `G1 × P3` | o koľko sa efekt usmernenia v `P3` mení oproti `P1` |

Prakticky to znamená, že samotné koeficienty interakčného modelu sú vhodné na presnú inferenčnú interpretáciu, ale pre čitateľské porozumenie bývajú menej intuitívne. Preto je užitočné dopĺňať ich aj o odhadované marginálne priemery pre všetky bunky `G0/G1 × P1/P2/P3`, ktoré ukazujú priamo odhadovanú priemernú úroveň výsledného ukazovateľa v každej experimentálnej kombinácii.

### B.5 Poznámka k reportovaniu lineárnych zmiešaných modelov

V lineárnych zmiešaných modeloch sa v tejto práci reportujú odhady koeficientov, štandardné chyby, `t` štatistiky, Waldove 95 % intervaly spoľahlivosti a `p`-hodnoty. `p`-hodnoty v `LMM` vetve vychádzajú z balíka `lmerTest` so Satterthwaite aproximáciou stupňov voľnosti. Pri interpretácii však aj tak ostáva dôležité čítať popri `p`-hodnote najmä smer efektu, jeho veľkosť a interval spoľahlivosti.

## Príloha C
**Public-safe schéma seedov a anchorovania**

Táto príloha zámerne neobsahuje plný seed corpus. Jej funkciou je ukázať logiku klinického anchorovania bez odovzdania celého proprietárneho balíka prípadov.

### C.1 Symptomatické a globálne anchor domény

**Tabuľka C1**  
*Symptomatické a globálne anchor domény*

| Doména | Obsah |
| --- | --- |
| `A1` | depresívna nálada |
| `A2` | strata záujmu alebo anhedónia |
| `A3` | poruchy spánku |
| `A4` | zmeny apetítu alebo hmotnosti |
| `A5` | psychomotorické spomalenie alebo nepokoj |
| `A6` | únava alebo nízka energia |
| `A7` | pocity viny alebo bezcennosti |
| `A8` | zhoršená koncentrácia alebo rozhodovanie |
| `A9` | pasívne myšlienky na smrť |
| `S1` | cieľová úroveň celkovej závažnosti |
| `S2` | cieľová úroveň funkčného dopadu |

### C.2 Ilustračný seed prípad

Nasledujúci príklad ukazuje, ako vyzerá jeden public-safe ilustračný seed bez plnej naratívnej seed dokumentácie.

**Tabuľka C2**  
*Ilustračný public-safe seed prípad*

| Prvok | Ilustračný príklad |
| --- | --- |
| Označenie prípadu | ilustračný seed s moderátne závažným obrazom |
| Jadro obrazu | nízka nálada, anhedónia, únava, porucha spánku, vina a zhoršená koncentrácia |
| Funkčný dopad | zhoršenie školského alebo pracovného fungovania a sociálneho života |
| Diferenciálna opatrnosť | nejde len o bežný stres, izolovaný spánkový problém, intoxikáciu, mániu alebo psychózu |
| Cieľový severity anchor | stredná až vyššia stredná závažnosť podľa seed nastavenia |
| Cieľový impact anchor | stredný funkčný dopad podľa seed nastavenia |

### C.3 Prečo je seed corpus v práci len redigovaný

Plný seed corpus neuvádzam vo verejnej verzii appendixu, pretože by sprístupnil:

- presné klinické kotvy všetkých prípadov,
- plnú internú logiku rozdielov medzi seedmi,
- jadro know-how simulačného rámca, ktoré presahuje potrebu bežného čitateľa.

Pre potreby práce preto stačí:

- opísať logiku A1 až A9, `S1` a `S2`,
- uviesť jeden ilustračný prípad,
- v hlavnom texte transparentne vysvetliť, že plný seed corpus bol použitý pri generovaní a analytickom porovnaní.

## Príloha D
**Doplnkové analytické výstupy**

Táto príloha zhromažďuje doplnkové analytické výstupy, ktoré rozširujú hlavný text, ale nie sú nevyhnutné na sledovanie jeho hlavnej argumentačnej línie. Ich funkciou je poskytnúť plnší technický kontext bez toho, aby jadro výsledkovej časti nadmerne zaťažovali rozsiahle tabuľky, modelové výstupy a exploratívne vizualizácie.

### D.1 Plné deskriptívne a frekvenčné tabuľky

V tejto časti sú zaradené plné tabuľkové výstupy, ktoré v hlavnom texte vystupujú len v skrátenej alebo sumarizovanej podobe.

<!-- FULL_RUN_APPENDIX_D_SECTION_1 -->

### D.2 Plné modelové výstupy

Táto časť obsahuje plné koeficientové tabuľky a doplnkové modelové výstupy, ktoré v hlavnom texte slúžia najmä ako podklad pre stručnejšie interpretačné zhrnutie.

<!-- FULL_RUN_APPENDIX_D_SECTION_2 -->

### D.3 Doplnkové korelačné výstupy

Táto časť sumarizuje korelačné prepojenia medzi transcript-level kompozitmi a ďalšími agregovanými ukazovateľmi.

<!-- FULL_RUN_APPENDIX_D_SECTION_3 -->

### D.4 Doplnková exploratívna PAM typológia prepisov rozhovorov

Táto časť obsahuje doplnkovú exploratívnu typológiu prepisov rozhovorov pomocou metódy PAM. Analýza nebola použitá na testovanie hypotéz `H1` až `H9` a nenahrádza hlavné zmiešané modely. Jej účelom je iba orientačne ukázať, či sa v agregovaných dátach na úrovni prepisu rozhovoru črtajú opakujúce sa profily kvality.

Poznámka. PAM typológia je uvedená výlučne ako doplnkový exploratívny výstup. Neslúži na inferenčné rozhodovanie o hlavných hypotézach a nemá byť interpretovaná ako dôkaz samostatných typov AI-generovaných rozhovorov.

<!-- FULL_RUN_APPENDIX_D_SECTION_4 -->

## Príloha E
**Stručná public-safe verzia etických a rater inštrukčných dokumentov**

### E.1 Etický a procedurálny rámec

- hodnotený materiál pozostával zo simulovaných textových transkriptov;
- účasť hodnotiteľov bola dobrovoľná;
- odpovede boli analyzované v anonymizovanom alebo pseudonymizovanom analytickom datasete;
- hodnotenie prebiehalo individuálne a asynchrónne;
- hodnotitelia boli informovaní, že ide o AI-generovaný materiál.

### E.2 Stručná inštrukcia pre hodnotiteľa

- hodnotiť rozhovor ako celok, nie iba izolované symptómové položky;
- rozlišovať medzi celkovou kvalitou rozhovoru, symptomatickou primeranosťou a problémovými prvkami;
- pri odhade pôvodu rozhovoru odpovedať podľa vlastného odborného dojmu;
- otvorený komentár používať na stručné zachytenie dôvodov pozitívneho alebo negatívneho hodnotenia.

### E.3 Čo do verejnej verzie nepatrí

Do verejnej prílohy E nepatria:

- interné runtime pravidlá simulácie,
- technické branching pokyny,
- interné safety workflow pre AI-only beh,
- presné operačné inštrukcie používané mimo verejného znenia práce.

## Príloha F
**Kompaktná mapa empirických otázok, hypotéz, outcome-ov a modelov**

**Tabuľka F1**  
*Mapa empirických otázok, hypotéz, outcome-ov a modelov*

| Blok | Funkcia bloku | VO | H | Hlavné outcome-y | Model alebo postup |
| --- | --- | --- | --- | --- | --- |
| A | globálna kvalita interview | `VO1` | `H1`, `H2`, `H5` | index klinickej vierohodnosti; `G2`; `G5` | deskriptíva, `LMM`, ordinal mixed models |
| A | symptom fidelity voči seedu | `VO2` | `H4` | priemerná absolútna chyba v doménach `A1` až `A9`; doplnkovo `S1`, `S2`, error skóre | transcript-level modely, doplnkové `LMM` a ordinal mixed models |
| B | efekt štýlu odpovedania simulovaného pacienta | `VO3` | `H6`, `H7` | index klinickej vierohodnosti; `G2`; `G5` | `LMM`, ordinal mixed models |
| B | efekt štýlu odpovedania na fidelity a defekty | `VO4` | `H8` + nehypotetizované doplnkové výstupy | priemerná absolútna chyba, `severity_error`, `impact_error`, index defektov | `LMM`, transcript-level modely, doplnkové ordinal mixed models |
| C | interakcia oboch faktorov | `VO5` | `H9` | index klinickej vierohodnosti; index defektov; doplnkovo fidelity outcome-y | interakčné členy v mixed modeloch |
| C | zhoda hodnotiteľov | `VO6` | bez hypotézy | `ICC` pre hlavné kompozity a pre `S1`, `S2` | `ICC` |
| C | vnímaný pôvod rozhovoru | `VO7` | bez hypotézy | odhad pôvodu rozhovoru; istota odhadu | frekvencie, doplnkové modely |
| C | otvorené komentáre | `VO8` | bez hypotézy | komentár hodnotiteľa | stručné tematické kódovanie |

### F.1 Najkratšia verzia logiky appendixu

- Blok A ukazuje, či rozhovory pôsobia kvalitne a či zodpovedajú seed profilu.
- Blok B ukazuje, čo s kvalitou robí štýl odpovedania simulovaného pacienta.
- Blok C uzatvára interakciu, zhodu hodnotiteľov a doplnkové signály o pôvode rozhovoru a komentároch.

## Príloha H
**Vyhlásenie o použití generatívnej AI pri vypracovaní diplomovej práce**

Táto príloha sa vzťahuje výlučne na využitie generatívnej AI ako podporného nástroja pri príprave textu, redakčných úpravách a technických pomocných úlohách. Nevzťahuje sa na empirickú časť výskumu, v ktorej generatívna AI vystupuje ako súčasť skúmaného simulačného rámca a ako zdroj analyzovaného materiálu.

### H.1 Rozsah a povaha využitia

Pri vypracovaní tejto diplomovej práce boli v obmedzenej, kontrolovanej a podriadenej miere využité generatívne jazykové modely ako pomocné nástroje pri jazykových, štylistických, organizačných a technických úlohách. Ich použitie malo podporný charakter a neslúžilo ako náhrada odbornej práce autora.

### H.2 Oblasti využitia

Generatívna AI bola použitá najmä na jazykové a štylistické spresnenie textu, návrhy alternatívnych formulácií viet a odsekov, kontrolu zrozumiteľnosti a vnútornej nadväznosti rukopisu a technickú pomoc pri príprave pomocných skriptov, exportov a organizácie doplnkových materiálov.

### H.3 Oblasti, v ktorých AI použitá nebola

Generatívna AI nebola použitá na vytváranie, falšovanie alebo nahrádzanie výskumných dát, na autonómnu realizáciu alebo nekontrolované preberanie štatistických analýz, na samostatnú interpretáciu výsledkov ani na formulovanie finálnych vedeckých záverov. Nebola ani náhradou za odborné metodologické rozhodnutia autora alebo za Zotero ako zdroj pravdy pre bibliografické údaje a finálne citačné rozhodnutia.

### H.4 Autorská kontrola a zodpovednosť

Všetky metodologické rozhodnutia, výber a interpretácia odbornej literatúry, analytické postupy, interpretácia výsledkov, diskusia aj finálne znenie textu boli priebežne kriticky posúdené, upravené a schválené autorom práce, ktorý za ich obsah nesie plnú zodpovednosť.

Výstupy generatívnej AI neboli preberané automaticky ani nekriticky. Každý návrh bol individuálne posúdený autorom a podľa potreby upravený, doplnený alebo zamietnutý.
