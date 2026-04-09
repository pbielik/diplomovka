# 30 Method / Metóda

> Pracovný draft kapitoly. Finálna verzia pôjde do Wordu so živými Zotero citáciami. Tento text je už koncipovaný ako thesis-ready verzia a má sa iba doplniť o finálne počty hodnotiteľov, finálnu informáciu o poradí prezentácie transkriptov a o konečnom inštrukčnom rámcovaní.

## 2 Metóda

### 2.1 Charakter výskumu a výskumný dizajn

Predkladaný výskum má charakter **pilotnej kvantitatívnej metodologickej štúdie** zameranej na odborné hodnotenie kvality AI-generovaných simulovaných klinických interview so zameraním na depresívnu symptomatiku. Cieľom výskumu nebolo overovať diagnostickú presnosť systému v klinickej praxi ani nahrádzať odborné klinické rozhodovanie, ale preskúmať, do akej miery sú generované rozhovory odbornými hodnotiteľmi vnímané ako klinicky vierohodné, jazykovo prirodzené, vnútorne konzistentné, symptomaticky primerané a použiteľné na tréningové alebo výučbové účely. Súčasne sa sledovalo, či experimentálne manipulované vlastnosti generovania rozhovoru ovplyvňujú kvalitu výsledného textu.

Výskum bol navrhnutý ako **faktorový experiment v rámci human-rated hodnotenia transkriptov**, v ktorom boli systematicky obmieňané dve nezávislé premenné. Prvou bola **prítomnosť štruktúrujúceho klinického usmernenia**, ktoré v technickej vrstve zodpovedalo premennej `guardrail` s úrovňami `off` a `on`. Druhou bol **štýl odpovedania simulovaného pacienta**, ktorý v technickej vrstve zodpovedal premennej `profile` s tromi úrovňami `R1`, `R2` a `R3`. Kombináciou týchto faktorov vzniklo šesť finálnych experimentálnych variantov. Každý variant bol aplikovaný na 12 vopred pripravených a klinicky ukotvených seed scenárov, čím vznikol súbor **72 transkriptov** určených na odborné hodnotenie. Klinická variabilita medzi rozhovormi bola teda nesená najmä seed scenármi, zatiaľ čo experimentálna variabilita bola cielene reprezentovaná dvoma manipulovanými faktormi generovania.

V praktickom zmysle tento dizajn tvorí jadro **simulačného rámca** skúmaného v práci. Jeho vstupnú vrstvu tvoria klinicky ukotvené seed scenáre, manipulačnú vrstvu faktory `guardrail` a `profile`, evaluačnú vrstvu expert-rated hodnotenie transkriptov a výstupnú vrstvu tri skupiny outcome ukazovateľov: primárna kvalitatívna vrstva, symptom fidelity vrstva a defect vrstva. Takto definovaný rámec umožňuje skúmať nielen to, či model vytvorí plynulý text, ale aj to, či vzniknutý rozhovor obstojí ako metodologicky kontrolovaný psychologický materiál.

Z pohľadu klasifikácie výskumného dizajnu ide o **komparačný faktorový dizajn s opakovaným odborným hodnotením textových stimulov**. Hlavnou úlohou nie je zisťovať vzťahy medzi prirodzene sa vyskytujúcimi psychologickými premennými u participantov, ale porovnávať kvalitu výstupov vytvorených v rôznych experimentálnych podmienkach. Jadrom výskumného problému je preto rozdiel medzi experimentálnymi variantmi a ich vplyv na viaceré outcome premenné. Takáto logika je v súlade s lokálnym sprievodcom záverečných prác, ktorý uvádza, že pri komparačnom výskume sú komparačné otázky a hypotézy hlavným vyjadrením výskumného problému.

Výskum bol koncipovaný ako pilotný aj z praktických dôvodov. Pilotné štúdie sú vhodné na overenie realizovateľnosti postupu, použiteľnosti nástroja, predbežného správania sa dát a identifikáciu problematických miest dizajnu ešte pred prípadným väčším konfirmačným výskumom. Vzhľadom na pilotný charakter je však potrebné interpretovať efektové odhady opatrne, keďže pri menších vzorkách bývajú menej stabilné. Táto opatrnosť sa potom premieta najmä do spôsobu interpretácie výsledkov, kde bude dôraz kladený nielen na štatistickú významnosť, ale aj na smer a veľkosť efektov [@sim2019ShouldTreatmentEffects; @soukup2013SubstantiveSignificanceIts].

Primárna konfirmačná analytická línia je viazaná na hypotézy `H1`–`H5` z Úvodu, teda na hlavné efekty `guardrail` na klinickú plausibilitu, prirodzenosť, defekty, symptom fidelity a tréningovú použiteľnosť. Hypotézy `H6`–`H9` tvoria rozšírenú pracovnú vrstvu zameranú na efekt `profile` a interakciu `guardrail × profile`. Otvorené komentáre hodnotiteľov a položka `guessed_origin` predstavujú doplnkovú exploračnú vrstvu, ktorá rozširuje interpretáciu hlavných výsledkov, ale netvorí jadro experimentálneho testu.

### 2.2 Základný súbor, výskumný súbor a jednotka analýzy

#### 2.2.1 Základný súbor

Základný súbor výskumu tvorí populácia odborníkov z oblasti psychológie, psychoterapie a psychiatrie, ktorí majú skúsenosť s prácou s klientmi s depresívnou symptomatikou alebo s diagnózou veľkej depresívnej poruchy. Keďže cieľom práce nebolo reprezentatívne zmapovať postoje celej populácie odborníkov, ale získať kvalifikované expertné posúdenie simulovaných klinických interview, výber participantov mal charakter **účelového výberu**. Takýto postup je v danej metodologickej situácii opodstatnený, pretože podmienkou zaradenia nebola bežná populačná príslušnosť, ale odborná kompetencia posúdiť kvalitu klinického rozhovoru.

#### 2.2.2 Výskumný súbor

Výskumný súbor tvorili **odborní hodnotitelia** z oblasti psychológie, psychoterapie a psychiatrie, ktorí mali skúsenosť s prácou s klientmi s depresívnou symptomatikou alebo s diagnózou MDD. Inklúznymi kritériami boli: (a) odborné vzdelanie alebo odborná prax v oblasti psychológie, psychoterapie alebo psychiatrie; (b) skúsenosť s prácou s depresívnou symptomatikou alebo s diagnózou MDD; (c) ochota zúčastniť sa na hodnotení textových transkriptov. Exklúznym kritériom bola absencia relevantnej odbornej skúsenosti alebo nedokončené hodnotenie v rozsahu znemožňujúcom jeho analytické použitie.

Počet zaradených hodnotiteľov bol **[doplniť finálny počet]**. Po doplnení finálnych údajov budú v tejto kapitole uvedené tie základné charakteristiky súboru, ktoré sú relevantné pre interpretáciu výsledkov: profesijné zloženie, dĺžka praxe, typ pracovného prostredia a skúsenosť s prácou s pacientmi s depresívnou symptomatikou. Tieto charakteristiky sú metodicky relevantné, pretože môžu ovplyvňovať prísnosť alebo spôsob expertného hodnotenia.

#### 2.2.3 Jednotka analýzy

Jednotkou analýzy nebol samotný hodnotiteľ ani samotný transkript, ale **jedno hodnotenie jedného transkriptu jedným hodnotiteľom**. Dataset preto vznikol v dlhom formáte, v ktorom jeden riadok reprezentuje jedno expertné hodnotenie. Tento prístup umožňuje súčasne zohľadniť variabilitu medzi transkriptmi, seedmi a hodnotiteľmi a je metodicky vhodný pre následné mixed-effects modelovanie. V praktickej rovine to znamená, že analýza nepracuje len s priemerom „na transkript", ale s každým jednotlivým ratingom ako s pozorovaním, ktoré je zároveň vnorené do hodnotiteľa aj do stimulového materiálu. Tento dizajn je silnejší než jednoduché agregovanie, pretože uchováva viac informácie o variabilite expertnej evaluácie.

### 2.3 Výskumný materiál

Stimulusový materiál pozostával zo **72 textových transkriptov** simulovaných interview. Tieto rozhovory boli generované na základe **12 fixných seed scenárov** (`S01`–`S12`), ktoré predstavovali klinicky ukotvené modelové profily depresívnej symptomatiky. Seedy obsahovali demografický a kontextový rámec, symptomatické kotvy pre oblasti `A1`–`A9`, pravidlá disclosure, štýlové nastavenia a bezpečnostné limity odpovedí. Takto definované seedy zabezpečovali, že jednotlivé transkripty neboli iba voľne generované texty, ale simulácie opreté o vopred pripravený klinický rámec, ktorý je v práci opísaný v Úvode (časť 1.1) a previazaný so symptomatickými doménami `A1`–`A9` [@kroenke2001phq9; @kennedy2008coresymptoms].

Finálny experimentálny preset pozostával zo šiestich variantov definovaných ako `G0/G1 × R1/R2/R3`, kde `G0/G1` označovalo neprítomnosť alebo prítomnosť guardrailu a `R1/R2/R3` predstavovalo zdržanlivý, vyvážený a rozvinutý štýl odpovedania simulovaného pacienta. V psychologickom jazyku tieto technické označenia v práci prekladáme ako:

- `G0` = bez štruktúrujúceho klinického usmernenia,
- `G1` = so štruktúrujúcim klinickým usmernením,
- `R1` = zdržanlivý štýl odpovedania simulovaného pacienta,
- `R2` = vyvážený štýl odpovedania simulovaného pacienta,
- `R3` = rozvinutý štýl odpovedania simulovaného pacienta.

Pri finálnom balíku transkriptov bola variabilita nastavená ako **locked**, aby sa minimalizoval nekontrolovaný drift a aby sa v hodnotení testovali primárne práve experimentálne manipulované vlastnosti generovania. Mimo zámerne menených faktorov sa výskum snažil zachovať čo najvyššiu štandardizáciu (rovnaký interview protokol, rovnaký počet turnov, rovnaký formát exportu, rovnaké nastavenie modelových parametrov mimo `guardrail` a `profile`).

Výhodou takto pripraveného materiálu bolo, že umožňoval súčasne sledovať dve úrovne variability. Prvou bola **klinická variabilita medzi seed scenármi**, teda odlišnosti medzi rôznymi modelovými prípadmi depresívnej symptomatiky. Druhou bola **experimentálna variabilita** spôsobená štruktúrujúcim klinickým usmernením a štýlom odpovedania simulovaného pacienta. Tento dvojvrstvový dizajn zvyšuje ekologickú validitu výskumu, pretože hodnotitelia neporovnávali len technicky mierne odlišné texty, ale rozhovory založené na odlišných klinických situáciách, pri ktorých sa zároveň testoval vplyv dvoch systematicky manipulovaných vlastností generovania.

### 2.4 Hodnotiaci nástroj

Na zber hodnotení bol použitý **autorsky zostavený ratingový dotazník** implementovaný v internom survey engine. Nástroj obsahoval tri hlavné bloky položiek, jednu nominálnu položku odhadovaného pôvodu rozhovoru a jednu otvorenú textovú položku.

#### 2.4.1 Štruktúra blokov

**Prvý blok – primárne kvalitatívne outcome-y `G1`–`G5`** zachytáva globálne expertné hodnotenie rozhovoru. Hodnotiteľ posudzuje interview ako celok, teda nie jednotlivý symptomatický detail, ale odborný dojem z textu:

- `G1` = klinická vierohodnosť rozhovoru,
- `G2` = prirodzenosť jazyka a plynulosť odpovedí,
- `G3` = vnútorná konzistentnosť rozhovoru,
- `G4` = súlad rozhovoru s obrazom depresívnej symptomatiky,
- `G5` = použiteľnosť rozhovoru na tréningové alebo výučbové účely.

**Druhý blok – symptom fidelity položky `A1`–`A9` a globálne odhady `S1` a `S2`** predstavujú špecifické symptomatické domény depresívnej symptomatiky a slúžia na porovnanie s anchor hodnotami uloženými v seed scenári. Položky `A1`–`A9` zodpovedajú deviatim obsahovým oblastiam depresívnej symptomatiky zavedeným v Úvode (1.1) a previazaným s logikou `PHQ-9` [@kroenke2001phq9]. Položka `S1` reprezentuje odhad celkovej závažnosti a položka `S2` odhad funkčného dopadu na bežné fungovanie.

**Tretí blok – QC a defect položky `R1`–`R5`** zachytávajú kvalitatívne defekty, ktoré síce nemusia byť „symptómami" v pravom slova zmysle, ale môžu zásadne znižovať použiteľnosť rozhovoru v metodologickom alebo pedagogickom kontexte:

- `R1` = prítomnosť kontradikcií alebo zjavnej nekonzistentnosti,
- `R2` = prítomnosť klišéovitých alebo stereotypných formulácií,
- `R3` = kontextový nesúlad alebo odpovede mimo zamýšľaného klinického rámca,
- `R4` = podozrenie na inú primárnu psychopatológiu, než je cieľový seed profil,
- `R5` = neprimeraná dramatizácia alebo neautentické zveličovanie.

Súčasťou nástroja bola aj nominálna položka `guessed_origin` (s možnosťami: AI-generovaný, ľudsky simulovaný, reálny participant, neviem odhadnúť), položka `guess_confidence` zachytávajúca istotu tohto odhadu a otvorená textová položka `comment` určená na slobodný kvalitatívny komentár hodnotiteľa.

#### 2.4.2 Odpoveďové formáty

Položky `G1`–`G5` a `guess_confidence` boli koncipované ako **5-bodové Likertove škály** a v analýze sú chápané ako ordinálne premenné. Položky `A1`–`A9`, `S1`, `S2` a `R1`–`R5` boli ukotvené na **škále 0–3**, aby boli lepšie naviazané na seed anchory a aby umožnili výpočet odchýlky medzi očakávaným a hodnoteným profilom. Takéto ukotvenie bolo zvolené zámerne, pretože umožňuje nielen subjektívne expertné posúdenie kvality, ale aj odvodenie error-based premenných, ktoré merajú mieru zhody medzi zamýšľaným scenárom a expertným odhadom.

Takéto členenie nástroja umožnilo oddeliť jadro kvality rozhovoru od fidelity voči seed anchorom a od QC vrstvy. Zároveň tým vznikol priamy most medzi teoretickými konštruktmi v Úvode (klinická vierohodnosť, prirodzenosť, konzistentnosť, symptomatická primeranosť, red flags, tréningová použiteľnosť — časť 1.5) a empirickými premennými použitými v analýze.

#### 2.4.3 Status psychometrických vlastností

Keďže ide o autorský nástroj, v literatúre nie sú k dispozícii jeho predchádzajúce psychometrické charakteristiky. Z tohto dôvodu sa analýza vnútornej konzistencie a interrater reliability stáva súčasťou overovania nástroja v konkrétnom výskumnom kontexte. Takýto postup je v súlade s lokálnym sprievodcom záverečných prác aj s odporúčaniami COSMIN metodológie pre obsahovú validitu a vnútornú konzistenciu pri novo zostavených ratingových nástrojoch [@terwee2018COSMINMethodologyEvaluating; @boateng2018scaledevelopment]. Pri reporte vnútornej konzistencie a interrater reliability sa preto v kapitole Výsledky vychádza priamo z aktuálneho výskumu.

### 2.5 Operacionalizácia teoretických pojmov a empirické premenné

V Úvode (časti 1.5 a 1.7) boli zavedené tri kľúčové teoretické konštrukty: **prítomnosť štruktúrujúceho klinického usmernenia**, **štýl odpovedania simulovaného pacienta** a **kvalita simulovaného interview**. V tejto časti opisujeme ich empirické zachytenie v ratingovom nástroji a v odvodených ukazovateľoch.

#### 2.5.1 Nezávislé premenné

**Prítomnosť štruktúrujúceho klinického usmernenia** bola operacionalizovaná ako binárna nezávislá premenná `guardrail` s dvoma úrovňami:

- `guardrail = off` (`G0`) = bez štruktúrujúceho klinického usmernenia,
- `guardrail = on` (`G1`) = so štruktúrujúcim klinickým usmernením.

V psychologickom jazyku reprezentuje táto premenná mieru explicitného riadenia generovania rozhovoru s cieľom zvýšiť jeho konzistentnosť, tematickú disciplínu a klinickú primeranosť. Príbuznú logiku v literatúre LLM simulovaných pacientov nájdeme v CureFun, PATIENT-ψ a Adaptive-VP, ktoré používajú explicitné štruktúrujúce mechanizmy na riadenie modelového správania [@li2024curefun; @wang2024patientpsi; @lee2025adaptivevp].

**Štýl odpovedania simulovaného pacienta** bol operacionalizovaný ako trojúrovňová kategoriálna nezávislá premenná `profile`:

- `profile = R1` = zdržanlivý štýl odpovedania,
- `profile = R2` = vyvážený štýl odpovedania,
- `profile = R3` = rozvinutý štýl odpovedania.

Táto premenná reprezentuje rozdiely v miere otvorenosti, stručnosti, spontánnej elaborácie a detailnosti odpovedí v rozhovore. Ide o zámerné zjednodušenie kontinua disclosure, ktoré v literatúre LLM klientov modelujú napríklad [@kim2025mindvoyager] cez metakogníciu a kontrolu otvorenosti sebazdieľania.

#### 2.5.2 Blokovacie a náhodné faktory

**Seed scenár** (`seed_id`) predstavoval blokovací faktor, ktorý zachytával klinický základ modelového prípadu. Seed scenár nebol predmetom hypotetického záujmu ako nezávislá premenná v psychologickom zmysle, ale metodicky slúžil na zachytenie systematickej variability medzi prípadmi.

**Identita hodnotiteľa** (`rater_id`) predstavovala ďalší zdroj variability, ktorý bolo potrebné zohľadniť na úrovni modelovania. Rozdiely medzi hodnotiteľmi mohli vyplývať z profesijného zázemia, prísnosti ratingu, skúsenosti či preferovaného klinického štýlu, a preto boli v inferenčných modeloch zohľadňované ako náhodný efekt.

#### 2.5.3 Primárne závislé premenné

Primárne závislé premenné tvorili položky `G1`–`G5` z prvého bloku ratingového nástroja. Okrem jednotlivých položiek bol vytvorený kompozitný ukazovateľ **klinickej plausibility** `plausibility_index`, vypočítaný ako priemer položiek `G1`, `G3` a `G4`, keďže tieto tri položky podľa projektovej logiky a obsahovej validity konceptuálne najtesnejšie reprezentujú jadro klinickej vierohodnosti simulovaného interview:

```
plausibility_index = (G1 + G3 + G4) / 3
```

Položka `G2` (prirodzenosť jazyka) je analyzovaná samostatne ako ukazovateľ jazykovej a interakčnej kvality. Položka `G5` (tréningová použiteľnosť) je analyzovaná samostatne ako ukazovateľ celkového odborného úsudku o pedagogickej využiteľnosti rozhovoru.

#### 2.5.4 Sekundárne premenné a error-based ukazovatele

Sekundárne premenné tvorili položky `A1`–`A9`, `S1` a `S2`. Položky `A1`–`A9` predstavovali expertný odhad prítomnosti alebo intenzity jednotlivých symptomatických oblastí podľa seed anchorov. Položka `S1` reprezentovala odhad celkovej závažnosti a položka `S2` odhad funkčného dopadu.

Keďže pre každý seed boli vopred definované anchor hodnoty, bolo možné okrem samotných ratingov odvodiť aj **error-based ukazovatele** vyjadrujúce mieru zhody rozhovoru s cieľovým profilom. V práci sú tieto ukazovatele definované ako absolútne odchýlky od seed anchorov:

```
symptom_error_mean = ( |A1 − anchor(A1)| + |A2 − anchor(A2)| + ... + |A9 − anchor(A9)| ) / 9
severity_error     = | S1 − anchor(S1) |
impact_error       = | S2 − anchor(S2) |
```

Nižšia hodnota týchto ukazovateľov znamená vyššiu presnosť zhody rozhovoru s cieľovým seed scenárom. Tieto premenné slúžia ako primárna kvantitatívna opora pre hypotézy `H4` a `H8` (symptom fidelity) a v kombinácii s `plausibility_index` umožňujú odlíšiť „vyzerá dobre na povrchu" od „zodpovedá zamýšľanému klinickému obrazu".

#### 2.5.5 QC premenné a kompozit defektov

QC premenné tvorili položky `R1`–`R5`, z ktorých bol odvodený kompozit `defect_index`. Ich účelom bolo zachytiť nedostatky rozhovorov, ktoré mohli znižovať ich metodologickú alebo výučbovú využiteľnosť. Kompozit `defect_index` je v práci operacionalizovaný ako priemer položiek `R1`–`R5`:

```
defect_index = (R1 + R2 + R3 + R4 + R5) / 5
```

Vyššia hodnota `defect_index` znamená vyšší výskyt defektov a teda nižšiu metodologickú a pedagogickú použiteľnosť rozhovoru. `defect_index` je primárnym ukazovateľom pre hypotézu `H3`.

#### 2.5.6 Doplnkové premenné

Položka `guessed_origin` predstavovala nominálnu premennú so štyrmi možnosťami odpovede: AI-generovaný, ľudsky simulovaný, reálny participant, neviem odhadnúť. Položka `guess_confidence` reprezentovala istotu tohto odhadu na 5-bodovej škále. Otvorená textová premenná `comment` slúžila na kvalitatívne doplnenie expertnej evaluácie a umožňovala hodnotiteľovi pomenovať vlastné dôvody pozitívneho alebo negatívneho hodnotenia.

#### 2.5.7 Konzistentnosť názvov premenných

V celej práci používam rovnaké názvy premenných ako v ratingovom codebooku a v analytickom datasete, aby nevznikol nesúlad medzi metódou, výsledkami a tabuľkami. Tieto názvy sú zhodné aj s implementáciou v R analytickom skripte v `analysis/scripts/thesis_rating_pipeline.R`.

### 2.6 Empirické výskumné otázky a hypotézy

Lokálny sprievodca uvádza, že po teoretickom vymedzení výskumného problému majú v Metóde nasledovať empirické výskumné otázky a hypotézy formulované v jazyku pozorovateľných alebo odvodených premenných. Súčasne však nie je účelné duplikovať tú istú analytickú líniu dvoma paralelnými formuláciami bez pridanej hodnoty. V tejto práci preto výskumné otázky `VO1`–`VO8` tvoria širšie bloky podľa skúmaných outcome-ov a hypotézy `H1`–`H9` predstavujú užšie smerové predpoklady najmä pre efekt `guardrail` a rozšírený efekt `profile`/interakcie. Všetky sú už v Úvode (časť 1.7) formulované v jazyku konkrétnych premenných ratingového nástroja, takže ich empirická úroveň je s konceptuálnou totožná. V tejto časti ich preto iba znovu uvádzame s explicitným prepojením na modelové schémy použité vo Výsledkoch.

#### 2.6.1 Empirické výskumné otázky (rekapitulácia z Úvodu, 1.7)

**Blok A — globálna kvalita interview a symptom fidelity**

**`VO1`.** Ako odborní hodnotitelia celkovo hodnotia klinickú vierohodnosť, prirodzenosť, vnútornú konzistentnosť a tréningovú použiteľnosť AI-generovaných simulovaných klinických interview o depresívnej symptomatike (`G1`–`G5`, `plausibility_index`)?

**`VO2`.** Do akej miery sú AI-generované simulované klinické interview symptomaticky primerané vzhľadom na cieľový seed scenár, z ktorého vychádzajú (`A1`–`A9`, `S1`, `S2`, `symptom_error_mean`, `severity_error`, `impact_error`)?

**Blok B — štýl odpovedania simulovaného pacienta (`profile`)**

**`VO3`.** Aký vzťah má štýl odpovedania simulovaného pacienta (`profile`) ku klinickej vierohodnosti, prirodzenosti, vnútornej konzistentnosti a tréningovej použiteľnosti interview (`plausibility_index`, `G2`, `G5`)?

**`VO4`.** Aký vzťah má štýl odpovedania simulovaného pacienta (`profile`) k symptomatickej primeranosti interview a k výskytu red flags (`symptom_error_mean`, `severity_error`, `impact_error`, `defect_index`)?

**Blok C — interakcia, zhoda a doplnkové výstupy**

**`VO5`.** Existuje interakčný efekt medzi prítomnosťou štruktúrujúceho klinického usmernenia (`guardrail`) a štýlom odpovedania simulovaného pacienta (`profile`) vo vzťahu ku kvalite interview (`plausibility_index`, `defect_index`, error-based premenné)?

**`VO6`.** Aká je miera zhody medzi odbornými hodnotiteľmi pri posudzovaní kvality interview (`ICC` pre `plausibility_index`, `defect_index`, `symptom_error_mean`)?

**`VO7`.** Ako často odborní hodnotitelia odhadujú, že rozhovor je AI-generovaný, ľudsky simulovaný, reálny alebo nejednoznačný, a s akou istotou tieto odhady robia (`guessed_origin`, `guess_confidence`)?

**`VO8`.** Aké typy pozitívnych a negatívnych komentárov sa v otvorených odpovediach odborných hodnotiteľov objavujú najčastejšie (`comment`)?

V poradí výsledkov budú tieto bloky reportované takto: `VO1`–`VO2` ako deskriptívny a symptom-fidelity blok, `VO3`–`VO4` ako blok efektu `profile`, `VO5` ako interakčný blok, `VO6` ako blok zhody a `VO7`–`VO8` ako doplnkový exploračný blok. Konfirmačný efekt `guardrail` je vzhľadom na silnejšiu literárnu oporu testovaný primárne cez `H1`–`H5`, aby sa zbytočne nezdvojovala výskumná otázka a hypotéza pre ten istý analytický test.

#### 2.6.2 Empirické hypotézy – jadro (`H1`–`H5`)

Jadrové hypotézy práce smerujú prednostne na premennú `guardrail`, pretože doterajšia literatúra poskytuje najpresvedčivejšiu oporu pre význam klinicky ukotveného a štruktúrovaného riadenia simulácie [@li2024curefun; @wang2024patientpsi; @lee2025adaptivevp]. Tieto hypotézy sú formulované jednostranne, pretože predpokladáme konkrétny smer účinku.

**Blok A — hypotézy ku globálnej kvalite interview a symptom fidelity (`VO1`, `VO2`)**

**`H1`.** Interview vytvorené so štruktúrujúcim klinickým usmernením (`guardrail = on`) budú odbornými hodnotiteľmi posudzované ako klinicky vierohodnejšie než interview vytvorené bez štruktúrujúceho klinického usmernenia (`guardrail = off`), a to na úrovni `plausibility_index` aj jednotlivých položiek `G1`, `G3` a `G4`.

**`H2`.** Interview vytvorené so štruktúrujúcim klinickým usmernením budú odbornými hodnotiteľmi posudzované ako prirodzenejšie a vnútorne konzistentnejšie než interview vytvorené bez tohto usmernenia, najmä na položke `G2`.

**`H3`.** Interview vytvorené so štruktúrujúcim klinickým usmernením budú obsahovať menej red flags a iných problematických prvkov než interview vytvorené bez tohto usmernenia, a to na úrovni `defect_index` aj jednotlivých položiek `R1`–`R5`.

**`H4`.** Interview vytvorené so štruktúrujúcim klinickým usmernením budú symptomaticky primeranejšie vzhľadom na cieľový seed scenár než interview bez tohto usmernenia, teda budú mať nižší `symptom_error_mean`, nižší `severity_error` a nižší `impact_error`.

**`H5`.** Interview vytvorené so štruktúrujúcim klinickým usmernením budú odbornými hodnotiteľmi posudzované ako použiteľnejšie na tréningové alebo výučbové účely než interview bez tohto usmernenia, a to na úrovni položky `G5`.

#### 2.6.3 Empirické hypotézy – rozšírená pracovná vrstva (`H6`–`H9`)

Popri jadrových hypotézach sú v práci formulované aj rozšírené hypotézy zamerané na efekt `profile` a interakciu `guardrail × profile`. Tieto hypotézy môžu byť pri finálnej redakcii buď ponechané, alebo redukované podľa sily ich literárnej opory.

**Blok B — hypotézy k efektu štýlu odpovedania simulovaného pacienta (`VO3`, `VO4`)**

**`H6`.** Interview s vyváženým alebo rozvinutým štýlom odpovedania simulovaného pacienta (`profile = R2` alebo `R3`) budú odbornými hodnotiteľmi posudzované ako klinicky vierohodnejšie než interview so zdržanlivým štýlom odpovedania (`profile = R1`), a to na úrovni `plausibility_index`.

**`H7`.** Interview s rozvinutejším štýlom odpovedania (`profile = R3`) budú odbornými hodnotiteľmi posudzované ako prirodzenejšie a tréningovo použiteľnejšie než interview so zdržanlivejším štýlom odpovedania (`profile = R1`, `R2`), najmä na položkách `G2` a `G5`.

**`H8`.** Interview s rozvinutejším štýlom odpovedania (`profile = R3`) budú poskytovať symptomaticky bohatší a presnejší obraz prípadu než interview so zdržanlivejším štýlom (`profile = R1`), teda budú mať nižší `symptom_error_mean`.

Pri širšie formulovanej `VO4` zatiaľ samostatne nehypotetizujeme efekt `profile` pre `severity_error`, `impact_error` a `defect_index`, pretože pre takto špecifický smer účinku nemáme rovnako silnú literárnu oporu ako pre `symptom_error_mean`. Tieto výstupy preto budú vo Výsledkoch spracované ako inferenčná odpoveď na `VO4`, nie ako samostatné smerové hypotézy.

**Blok C — hypotéza k interakcii a nehypotetické bloky (`VO5`–`VO8`)**

**`H9`.** Pozitívny účinok štruktúrujúceho klinického usmernenia na kvalitu interview bude výraznejší pri rozvinutejšom štýle odpovedania simulovaného pacienta (`profile = R3`) než pri zdržanlivejšom štýle (`profile = R1`, `R2`); inými slovami, očakávame interakciu `guardrail × profile` v prospech kombinácie `guardrail = on` a `profile = R3`, najmä pri `plausibility_index` a `defect_index`.

Pre `VO6` neformulujeme samostatnú hypotézu, pretože ide o merací blok zameraný na mieru zhody hodnotiteľov. `VO7` a `VO8` ostávajú zámerne exploračné a budú reportované bez samostatných smerových hypotéz.

### 2.7 Procedúra výskumu

#### 2.7.1 Príprava stimulusového materiálu

Najprv bol pripravený finálny balík seed scenárov a experimentálnych variantov generovania. Následne boli vygenerované textové transkripty podľa jednotného interview protokolu a uložené v štandardizovanom formáte. Pred zaradením do hodnotenia boli transkripty skontrolované z hľadiska technickej úplnosti a formálnej konzistencie. Táto predbežná kontrola mala zabezpečiť, aby hodnotitelia neposudzovali technicky poškodené, neúplné alebo zjavne chybne exportované materiály.

#### 2.7.2 Priebeh hodnotenia

Hodnotitelia dostávali na posúdenie jednotlivé transkripty prostredníctvom webového hodnotiaceho rozhrania. Pri každom transkripte vyplnili ratingový dotazník a podľa potreby doplnili otvorený komentár. V závislosti od finálneho rozdelenia hodnotiacej záťaže a od faktickej dostupnosti jednotlivých hodnotiteľov mohol byť počet ratingov na transkript **variabilný**, pričom cieľom bolo pri každom transkripte dosiahnuť aspoň dvojnásobné nezávislé hodnotenie. Hodnotenie prebiehalo individuálne a asynchrónne.

Poradie predkladania transkriptov bolo **blokovo randomizované**: v rámci každého hodnotiteľa boli transkripty zoskupené do blokov tak, aby bolo balansované zastúpenie experimentálnych buniek `guardrail × profile`, a v rámci každého bloku bolo poradie náhodné. Tento postup obmedzuje order effects a zároveň zabezpečuje, aby žiadny hodnotiteľ nebol vystavený nárazovo iba jednému typu variantu. Hodnotitelia boli pred začatím hodnotenia explicitne informovaní, že **ide výlučne o AI-generovaný materiál**, teda že všetky predkladané transkripty pochádzajú zo simulovaného interview vedeného veľkým jazykovým modelom v role pacienta. Toto rozhodnutie zvyšuje etickú transparentnosť hodnotenia a je dôležité aj pre interpretáciu položky `guessed_origin`, ktorá v tomto nastavení nezachytáva neslepý odhad pôvodu, ale skôr to, či hodnotiteľ napriek vedomiu o AI pôvode rozpozná rozhovor ako zjavne strojovo generovaný, alebo či ho z hľadiska vnútornej koherencie posúdi ako prijateľne podobný reálnej alebo ľudsky simulovanej výpovedi.

#### 2.7.3 Export a štruktúra dát

Pri exporte odpovedí sa odpovede ukladané v JSON štruktúre konvertovali do tabuľkového formátu vhodného na následné štatistické spracovanie. Finálny analytický dataset mal **dlhý formát** a obsahoval identifikátor hodnotiteľa, identifikátor transkriptu, identifikátor seedu, experimentálne premenné `guardrail` a `profile`, položkové ratingy `G1`–`G5`, `A1`–`A9`, `S1`, `S2`, `R1`–`R5`, doplnkové položky `guessed_origin`, `guess_confidence` a `comment` a všetky odvodené kompozity (`plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error`, `impact_error`).

### 2.8 Spracovanie dát a štatistická analýza

#### 2.8.1 Predspracovanie dát

Pred analýzou boli všetky exportované odpovede skontrolované, vyčistené a prekódované. Likertove odpovede boli konvertované zo stringového exportu na numerické alebo ordinálne premenné podľa typu plánovanej analýzy. Následne boli vytvorené odvodené premenné `plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error` a `impact_error` podľa vzorcov uvedených v časti 2.5. Pri predspracovaní bolo zároveň overené, či nevznikli technické missingy, duplikované záznamy alebo nekompletné exporty.

#### 2.8.2 Deskriptívna analýza

Najprv bola spracovaná **deskriptívna štatistika** položiek a kompozitov. Pri ordinálnych položkách boli sledované frekvencie, mediány a interkvartilové rozpätia, pri kompozitných ukazovateľoch aj priemery a smerodajné odchýlky. V súlade s lokálnym sprievodcom budú prezentované základné miery polohy a variability tak, aby mal čitateľ jasnú predstavu o správaní sa jednotlivých premenných ešte pred inferenčnou analýzou. Pri kompozitoch s približne intervalovým charakterom budú doplnené aj histogramy a boxploty, aby bolo možné orientačne posúdiť distribúciu a prítomnosť odľahlých hodnôt.

#### 2.8.3 Analýza vnútornej konzistencie

V súlade s odporúčaniami sprievodcu a s logikou COSMIN obsahovej validity bola zaradená aj **analýza vnútornej konzistencie** meracieho nástroja, najmä pre blok `G1`–`G5`, pre plausibility blok (`G1`, `G3`, `G4`) a pre blok `R1`–`R5` [@terwee2018COSMINMethodologyEvaluating; @marko2016VyuzitieZneuzitieCronbachovej]. Keďže ide o autorský ratingový nástroj, táto časť je dôležitá pre posúdenie, či sa položky reprezentujúce spoločný konštrukt správajú dostatočne konzistentne. Výsledky budú prezentované úsporne a zrozumiteľne, nie ako séria samostatných neprehľadných tabuliek.

#### 2.8.4 Interrater reliabilita

**Interrater reliabilita** bola vyhodnocovaná prostredníctvom **intraclass correlation coefficient (ICC)** pre agregované ukazovatele `plausibility_index`, `defect_index` a `symptom_error_mean`. V konečnom reporte bude explicitne uvedený zvolený typ ICC (model, single/average measures, konzistencia vs. absolútna zhoda) a interpretačná kategória zhody [@mchugh2012InterraterReliabilityKappa; @nelson2015manyratersordinal]. Vzhľadom na dizajn štúdie, kde ten istý transkript môžu hodnotiť viacerí odborníci, je interrater reliabilita zásadným ukazovateľom spoľahlivosti expertnej evaluácie.

#### 2.8.5 Inferenčná analýza

Hlavná inferenčná analýza je realizovaná pomocou **mixed-effects modelov**, keďže jednotkou analýzy je hodnotenie, ktoré je zároveň viazané na hodnotiteľa aj na seed/transkript. Mixed modely umožňujú súčasne modelovať fixné efekty experimentálnych faktorov a náhodnú variabilitu medzi hodnotiteľmi a seedmi, čo je pri opakovaných a zhlukovaných meraniach metodicky vhodný postup [@hedeker2016MixedeffectsLocationScaleModel].

Pre kompozitné a error-based ukazovatele sú plánované **lineárne zmiešané modely** s týmto základným tvarom:

```
outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)
```

Tento model je použitý pre premenné:

- `plausibility_index` (`H1`, `H6`, časť `H9`),
- `defect_index` (`H3`, časť `H9`),
- `symptom_error_mean` (`H4`, `H8`, časť `H9`),
- `severity_error` (`H4`, časť `H9`),
- `impact_error` (`H4`, časť `H9`).

Pre jednotlivé ordinálne položky, najmä `G2` (`H2`, `H7`), `G5` (`H5`, `H7`) a `guess_confidence`, sú plánované **ordinal mixed models** typu cumulative link mixed model [@christensenCumulativeLinkModels]. Tento prístup je vhodný pri viacúrovňových ordinálnych dátach, ktoré sú zhlukované alebo opakovane merané, a slúži ako citlivostná analýza popri lineárnej špecifikácii.

Z hľadiska väzby na výskumné otázky a hypotézy platí nasledovné: modely pre `plausibility_index`, `G2` a `G5` odpovedajú na jadro `VO1` a zároveň testujú `H1`, `H2` a `H5`; modely pre `symptom_error_mean`, `severity_error` a `impact_error` odpovedajú na `VO2` a testujú `H4`; hlavné efekty `profile` nad `plausibility_index`, `G2`, `G5`, `symptom_error_mean`, `severity_error`, `impact_error` a `defect_index` odpovedajú na `VO3` a `VO4` a pokrývajú `H6`–`H8`; interakčné členy `guardrail × profile` odpovedajú na `VO5` a testujú `H9`. `VO6` je riešená samostatným blokom ICC a `VO7`–`VO8` samostatným exploračným blokom.

#### 2.8.6 Explorácia doplnkových premenných

Exploratórne je plánovaná aj **analýza položky `guessed_origin`**, najmä pomocou frekvenčného rozdelenia odpovedí a prípadne logistického modelu nad binarizovanou premennou „vnímané ako AI vs. nie AI". Otvorené komentáre v premennej `comment` budú analyzované **kvalitatívne prostredníctvom stručného tematického kódovania** s cieľom doplniť kvantitatívne výsledky o typické dôvody pozitívneho alebo negatívneho hodnotenia. Cieľom tejto analýzy nie je vytvoriť samostatnú kvalitatívnu líniu práce, ale stručne pomenovať opakujúce sa dôvody pozitívneho a negatívneho hodnotenia, ktoré pomôžu interpretovať kvantitatívne výsledky.

#### 2.8.7 Interpretácia efektov

Keďže ide o pilotnú štúdiu s potenciálne limitovaným počtom hodnotiteľov, inferenčné výsledky budú interpretované **opatrne a s dôrazom na smer a veľkosť efektov, nie iba na dichotomické rozhodovanie podľa hladiny štatistickej významnosti**. Vo Výsledkoch a Diskusii sa preto popri `p`-hodnotách budú uvádzať aj odhady efektov, intervaly spoľahlivosti a vecná významnosť rozdielov tam, kde je to možné [@sim2019ShouldTreatmentEffects; @soukup2013SubstantiveSignificanceIts; @cohen1988StatisticalPowerAnalysis]. Lokálny sprievodca pritom priamo odporúča, aby kvalita výsledkovej časti nestála len na testovaní významnosti, ale aj na primeranej deskriptívnej a inferenčnej logike vrátane vecnej významnosti.

Analýzy, ktoré priamo neodpovedajú na `H1`–`H9`, budú v kapitole Výsledky explicitne označené ako doplnkové alebo exploratórne, aby sa neporušila logická väzba medzi cieľom, hypotézami a poradím prezentácie výsledkov.

### 2.9 Etické aspekty

Výskum nepracoval s reálnymi pacientskymi údajmi ani s reálnymi klinickými rozhovormi. Hodnotený materiál tvorili **simulované textové transkripty** vytvorené na základe vopred pripravených seed scenárov, takže riziko pre participantov bolo nízke a riziko zneužitia identifikovateľných pacientskych údajov bolo z podstaty dizajnu vylúčené. Napriek tomu boli rešpektované základné etické princípy psychologického výskumu, najmä **informovanosť hodnotiteľov** o charaktere úlohy, **dobrovoľnosť účasti**, **možnosť účasť kedykoľvek ukončiť** a **ochrana identifikačných údajov hodnotiteľov** pri spracovaní odpovedí.

Súčasne je dôležité zdôrazniť, že výskum nebol koncipovaný ako diagnostický nástroj a jeho zistenia nemajú slúžiť na bezprostredné klinické rozhodovanie. Tento rámec je v práci zachovávaný konzistentne od Úvodu cez Metódu až po Diskusiu a je v súlade so širším etickým rámcom WHO pre použitie LLM v zdravotníctve [@who2021ethicsaiforhealth; @who2024lmmguidance].
