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

| Kód | Položka | Typ odpovede |
| --- | --- | --- |
| `G1` | Klinická vierohodnosť rozhovoru | 5-bodová škála |
| `G2` | Prirodzenosť jazyka a štýlu odpovedí | 5-bodová škála |
| `G3` | Vnútorná konzistentnosť rozhovoru | 5-bodová škála |
| `G4` | Súlad rozhovoru s obrazom depresívnej symptomatiky | 5-bodová škála |
| `G5` | Použiteľnosť rozhovoru na tréningové alebo výučbové účely | 5-bodová škála |

### A.3 Blok S: Globálny odhad závažnosti a funkčného dopadu

| Kód | Položka | Typ odpovede |
| --- | --- | --- |
| `S1` | Ľudský odhad celkovej závažnosti depresívnej symptomatiky | 5-bodová škála |
| `S2` | Ľudský odhad funkčného dopadu na bežné fungovanie | 5-bodová škála |

### A.4 Blok R: Problematické prvky a varovné signály

| Kód | Položka | Typ odpovede |
| --- | --- | --- |
| `R1` | Prítomnosť vnútorných kontradikcií v rozhovore | 5-bodová škála |
| `R2` | Klišé alebo šablónovité odpovede | 5-bodová škála |
| `R3` | Nesúlad medzi kontextom a symptomatikou | 5-bodová škála |
| `R4` | Podozrenie na inú primárnu psychopatológiu | 5-bodová škála |
| `R5` | Neprimeraná dramatizácia alebo neprirodzená expresivita | 5-bodová škála |

### A.5 Doplnkové položky

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
**Operacionalizačná tabuľka premenných, kompozitov a ich analytického použitia**

| Blok | Premenné | Škála | Význam | Analytické použitie |
| --- | --- | --- | --- | --- |
| Nezávislé premenné | prítomnosť štruktúrujúceho klinického usmernenia; štýl odpovedania simulovaného pacienta | binárna; kategóriálna s 3 úrovňami | experimentálne manipulované vlastnosti generovania rozhovoru | hlavné fixné efekty v mixed modeloch |
| Blokovacie a náhodné faktory | `seed_id`, `rater_id` | identifikátory | zdroj variability medzi seedmi a medzi hodnotiteľmi | random intercepts |
| Primárne outcome-y | `G1` až `G5`, index klinickej vierohodnosti | ordinálne položky; kompozit približne intervalový | globálna kvalita rozhovoru, prirodzenosť a tréningová použiteľnosť | deskriptíva, ordinal mixed models, lineárne zmiešané modely |
| Sekundárne outcome-y | `A1` až `A9`, priemerná absolútna chyba voči seedu, `S1`, `S2` | transcript-level `0-3`; ľudské ratingy `1-5` | zhoda rozhovoru s cieľovým symptomatickým profilom a samostatný ľudský odhad závažnosti a funkčného dopadu | transcript-level deskriptíva a modely; doplnkovo ordinal mixed models |
| Voliteľné sensitivity outcome-y | chyba odhadu závažnosti, chyba odhadu funkčného dopadu | odvodené numerické error skóre | doplnkové porovnanie ľudského odhadu s seed kotvami | supplement alebo secondary analysis |
| QC a defektové outcome-y | `R1` až `R5`, index defektov | ordinálne položky; kompozit približne intervalový | kontradikcie, klišé, nesúlad, iná psychopatológia, dramatizácia | deskriptíva, ordinal mixed models, lineárne zmiešané modely |
| Exploratórne outcome-y | odhad pôvodu rozhovoru, istota odhadu, komentár | nominálna; ordinálna; text | percepcia pôvodu rozhovoru a kvalitatívna spätná väzba | frekvencie, doplnkové modely, tematické kódovanie |

### B.1 Hlavné odvodené ukazovatele

| Ukazovateľ | Výpočet | Interpretácia |
| --- | --- | --- |
| Index klinickej vierohodnosti | `(G1 + G3 + G4) / 3` | vyššia hodnota znamená vyššiu klinickú vierohodnosť rozhovoru |
| Index defektov | `(R1 + R2 + R3 + R4 + R5) / 5` | vyššia hodnota znamená vyšší výskyt defektov |
| Priemerná absolútna chyba v symptomatických doménach | `mean(abs(Ai - Ai_anchor))` pre `A1` až `A9` | nižšia hodnota znamená vyššiu zhodu so seed profilom |
| Chyba odhadu závažnosti | `abs(S1 - S1_anchor)` | nižšia hodnota znamená vyššiu zhodu so seed kotvou |
| Chyba odhadu funkčného dopadu | `abs(S2 - S2_anchor)` | nižšia hodnota znamená vyššiu zhodu so seed kotvou |

## Príloha C
**Public-safe schéma seedov a anchorovania**

Táto príloha zámerne neobsahuje plný seed corpus. Jej funkciou je ukázať logiku klinického anchorovania bez odovzdania celého proprietárneho balíka prípadov.

### C.1 Symptomatické a globálne anchor domény

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
**Doplnkové tabuľky a grafy**

Táto príloha má niesť len tie doplnkové analytické výstupy, ktoré po finálnom run-e zostanú interpretačne zmysluplné a zároveň nebudú zbytočne duplikovať hlavný text.

### D.1 Odporúčaný supplement balík

| Označenie | Obsah | Zdrojový artefakt |
| --- | --- | --- |
| Tabuľka S1 | Spearmanova korelačná matica transcript-level kompozitov | `tables/table_s1_spearman_transcript_composites.csv` |
| Obrázok S1 | Heatmap korelačnej matice | `figures/figure_s1_spearman_heatmap.png` |
| Tabuľka S2 | Profily PAM klastrov | `tables/table_s2_pam_cluster_profiles.csv` |
| Tabuľka S3 | Rozloženie PAM klastrov podľa podmienok | `tables/table_s3_pam_cluster_by_condition.csv` |
| Obrázok S2 | Mapovanie PAM klastrov | `figures/figure_s2_pam_cluster_map.png` |
| Tabuľka S4 | Predbežná expertná kontrola položiek ratingového nástroja | `tables/table_s4_expert_review_items.csv` |
| Tabuľka S5 | Predbežná expertná kontrola seed scenárov | `tables/table_s5_expert_review_seeds.csv` |
| Obrázok S3 | Heatmap predbežnej expertnej kontroly položiek ratingového nástroja | `figures/figure_s3_expert_review_items_heatmap.png` |
| Obrázok S4 | Heatmap predbežnej expertnej kontroly seed scenárov | `figures/figure_s4_expert_review_seeds_heatmap.png` |

### D.2 Redakčné pravidlo pre finálny výber

Do finálnej verzie prílohy D zaradiť iba tie tabuľky a grafy, ktoré:

- budú po finálnom analytickom behu stabilné a interpretačne obhájiteľné,
- budú mať jasnú väzbu na hlavný text,
- nebudú len technickým výstupom pipeline bez výpovednej hodnoty.

Ak niektorý doplnkový výstup po finálnom run-e neostane stabilný alebo interpretačne čistý, má ostať v internom workflowe a nie v appendixe.

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

## Poznámka k ďalšiemu kroku

Tento súbor je zámerne písaný ako medzivrstva medzi interným framingom v `manuscript/70_appendices.md` a finálnym Word appendixom. Pri poslednom prechode do Wordu bude treba:

1. skrátiť technické formulácie na fakultne prirodzenejší prose,
2. doplniť finálne názvy tabuliek a obrázkov podľa posledného analytického run-u,
3. rozhodnúť, či príloha D ostane celá, alebo sa zúži len na jeden doplnkový analytický blok.
