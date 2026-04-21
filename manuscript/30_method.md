# 30 Method / Metóda

> Pracovný draft kapitoly. Finálna verzia pôjde do Wordu so živými Zotero citáciami. Tento text je už koncipovaný ako verzia pripravená pre rukopis a má sa iba doplniť o finálne počty hodnotiteľov, finálnu informáciu o poradí prezentácie prepisov rozhovorov a o konečnom inštrukčnom rámcovaní.

## 2 Metóda

### 2.1 Charakter výskumu a výskumný dizajn

Predkladaný výskum má charakter **pilotnej kvantitatívnej metodologickej štúdie** zameranej na odborné hodnotenie kvality AI-generovaných simulovaných klinických rozhovorov so zameraním na depresívnu symptomatiku. Cieľom výskumu nebolo overovať diagnostickú presnosť systému v klinickej praxi ani nahrádzať odborné klinické rozhodovanie, ale preskúmať, do akej miery sú generované rozhovory odbornými hodnotiteľmi vnímané ako klinicky vierohodné, jazykovo prirodzené, vnútorne konzistentné, symptomaticky primerané a použiteľné na tréningové alebo výučbové účely. Súčasne sa sledovalo, či experimentálne manipulované vlastnosti generovania rozhovoru ovplyvňujú kvalitu výsledného textu.

Výskum bol navrhnutý ako **faktorový experiment v rámci odborného hodnotenia prepisov rozhovorov**, v ktorom boli systematicky obmieňané dve nezávislé premenné. Prvou bola **prítomnosť štruktúrujúceho klinického usmernenia** s dvoma úrovňami: bez usmernenia a so štruktúrujúcim klinickým usmernením. Druhou bol **štýl odpovedania simulovaného pacienta** s tromi úrovňami: P1, P2 a P3. Kombináciou týchto faktorov vzniklo šesť finálnych experimentálnych variantov. Každý variant bol aplikovaný na 12 vopred pripravených a klinicky ukotvených východiskových scenárov, čím vznikol súbor **72 prepisov rozhovorov** určených na odborné hodnotenie. Klinická variabilita medzi rozhovormi bola teda nesená najmä východiskovými scenármi, zatiaľ čo experimentálna variabilita bola cielene reprezentovaná dvoma manipulovanými faktormi generovania.

V praktickom zmysle tento dizajn tvorí jadro **simulačného rámca** skúmaného v práci. Jeho vstupnú vrstvu tvoria klinicky ukotvené východiskové scenáre, manipulačnú vrstvu prítomnosť štruktúrujúceho klinického usmernenia a štýl odpovedania simulovaného pacienta, evaluačnú vrstvu odborné hodnotenie prepisov rozhovorov a výstupnú vrstvu tri skupiny výstupných ukazovateľov: primárna kvalitatívna vrstva, vrstva symptomatickej primeranosti a vrstva kontroly kvality a defektov. Takto definovaný rámec umožňuje skúmať nielen to, či model vytvorí plynulý text, ale aj to, či vzniknutý rozhovor obstojí ako metodologicky kontrolovaný psychologický materiál.

**Schéma 1**  
*Schéma simulačného a hodnotiaceho rámca*

::: {custom-style="SchemaLine"}
Východiskové scenáre S01-S12

↓

Experimentálne varianty G0/G1 × P1/P2/P3

↓

72 prepisov rozhovorov

↓

Expertné hodnotenie

↓

Položky G/S/R

↓

Kompozity a modely
:::

Schéma znázorňuje základnú logiku výskumného postupu: klinicky ukotvené východiskové scenáre boli kombinované s dvoma experimentálnymi faktormi generovania, čím vznikol súbor prepisov rozhovorov určených na odborné hodnotenie. Výstupy hodnotenia následne tvorili základ deskriptívnych, reliabilitných, inferenčných a doplnkových exploratórnych analýz.

Z pohľadu klasifikácie výskumného dizajnu ide o **komparačný faktorový dizajn s opakovaným odborným hodnotením textových stimulov**. Hlavnou úlohou nie je zisťovať vzťahy medzi prirodzene sa vyskytujúcimi psychologickými premennými u účastníkov výskumu, ale porovnávať kvalitu výstupov vytvorených v rôznych experimentálnych podmienkach. Jadrom výskumného problému je preto rozdiel medzi experimentálnymi variantmi a ich vplyv na viaceré výstupné premenné. Takáto logika je v súlade s lokálnym sprievodcom záverečných prác, ktorý uvádza, že pri komparačnom výskume sú komparačné otázky a hypotézy hlavným vyjadrením výskumného problému.

Výskum bol koncipovaný ako pilotný aj z praktických dôvodov. Pilotné štúdie sú vhodné na overenie realizovateľnosti postupu, použiteľnosti nástroja, predbežného správania sa dát a identifikáciu problematických miest dizajnu ešte pred prípadným väčším konfirmačným výskumom. Vzhľadom na pilotný charakter je však potrebné interpretovať efektové odhady opatrne, keďže pri menších vzorkách bývajú menej stabilné. Ako odporúčajú @sim2019ShouldTreatmentEffects a @soukup2013SubstantiveSignificanceIts, táto opatrnosť sa potom premieta najmä do spôsobu interpretácie výsledkov, kde bude dôraz kladený nielen na štatistickú významnosť, ale aj na smer a veľkosť efektov.

Primárna konfirmačná analytická línia je viazaná na hypotézy H1 až H5 z Úvodu, teda na hlavné efekty prítomnosti štruktúrujúceho klinického usmernenia na klinickú vierohodnosť, prirodzenosť, defekty, symptomatickú primeranosť a tréningovú použiteľnosť. Hypotézy H6 až H9 tvoria rozšírenú pracovnú vrstvu zameranú na efekt štýlu odpovedania simulovaného pacienta a na interakciu oboch faktorov. Otvorené komentáre hodnotiteľov a položka odhadovaného pôvodu rozhovoru predstavujú doplnkovú exploračnú vrstvu, ktorá rozširuje interpretáciu hlavných výsledkov, ale netvorí jadro experimentálneho testu.

### 2.2 Základný súbor, výskumný súbor a jednotka analýzy

#### 2.2.1 Základný súbor

Základný súbor výskumu tvorí populácia odborníkov z oblasti psychológie, psychoterapie a psychiatrie, ktorí majú skúsenosť s prácou s klientmi s depresívnou symptomatikou alebo s diagnózou veľkej depresívnej poruchy. Keďže cieľom práce nebolo reprezentatívne zmapovať postoje celej populácie odborníkov, ale získať kvalifikované expertné posúdenie simulovaných klinických rozhovorov, výber účastníkov mal charakter **účelového výberu**. Takýto postup je v danej metodologickej situácii opodstatnený, pretože podmienkou zaradenia nebola bežná populačná príslušnosť, ale odborná kompetencia posúdiť kvalitu klinického rozhovoru.

#### 2.2.2 Výskumný súbor

Výskumný súbor tvorili **odborní hodnotitelia** z oblasti psychológie, psychoterapie a psychiatrie, ktorí mali skúsenosť s prácou s klientmi s depresívnou symptomatikou alebo s diagnózou MDD. Inklúznymi kritériami boli: (a) odborné vzdelanie alebo odborná prax v oblasti psychológie, psychoterapie alebo psychiatrie; (b) skúsenosť s prácou s depresívnou symptomatikou alebo s diagnózou MDD; (c) ochota zúčastniť sa na hodnotení textových prepisov rozhovorov. Exklúznym kritériom bola absencia relevantnej odbornej skúsenosti alebo nedokončené hodnotenie v rozsahu znemožňujúcom jeho analytické použitie.

Počet zaradených hodnotiteľov bol **6**. Všetci zaradení hodnotitelia sa identifikovali ako psychológovia; podľa exportovaných metadát dvaja uviedli špecializáciu v klinickej psychológii a štyria v psychoterapii. Dĺžka praxe bola v exporte zachytená pásmami od `0-2` do `16+` rokov a kontakt s depresívnou symptomatikou bol uvádzaný ako týždenný alebo denný. Tieto charakteristiky sú metodicky relevantné, pretože môžu ovplyvňovať prísnosť alebo spôsob expertného hodnotenia.

#### 2.2.3 Jednotka analýzy

Jednotkou analýzy nebol samotný hodnotiteľ ani samotný prepis rozhovoru, ale **jedno hodnotenie jedného prepisu rozhovoru jedným hodnotiteľom**. Dátový súbor preto vznikol v dlhom formáte, v ktorom jeden riadok reprezentuje jedno expertné hodnotenie. Tento prístup umožňuje súčasne zohľadniť variabilitu medzi prepismi rozhovorov, východiskovými scenármi a hodnotiteľmi a je metodicky vhodný pre následné modelovanie pomocou zmiešaných modelov. V praktickej rovine to znamená, že analýza nepracuje len s priemerom „na prepis rozhovoru“, ale s každým jednotlivým hodnotením ako s pozorovaním, ktoré je zároveň vnorené do hodnotiteľa aj do podnetového materiálu. Tento dizajn je silnejší než jednoduché agregovanie, pretože uchováva viac informácie o variabilite expertnej evaluácie.

### 2.3 Podnetový materiál

Podnetový materiál pozostával zo **72 textových prepisov simulovaných rozhovorov**. Tieto rozhovory boli generované na základe **12 fixných východiskových scenárov** (S01 až S12), ktoré predstavovali klinicky ukotvené modelové profily depresívnej symptomatiky. Východiskové scenáre obsahovali demografický a kontextový rámec, symptomatické kotvy pre oblasti A1 až A9, pravidlá postupného odhaľovania ťažkostí, štýlové nastavenia a bezpečnostné limity odpovedí. Takto definované východiskové scenáre zabezpečovali, že jednotlivé prepisy rozhovorov neboli iba voľne generované texty, ale simulácie opreté o vopred pripravený klinický rámec, ktorý je v práci opísaný v Úvode (časť 1.1) a previazaný so symptomatickými doménami A1 až A9 podľa logiky PHQ-9 formulovanej @kroenke2001phq9 a jadrových symptómov opísaných @kennedy2008coresymptoms.

Logika anchorovania východiskových scenárov je v public-safe verzii zhrnutá aj v Prílohe C.

Finálne experimentálne nastavenie pozostávalo zo šiestich variantov definovaných v dátovom exporte ako G0/G1 × R1/R2/R3, kde G0/G1 označovalo neprítomnosť alebo prítomnosť štruktúrujúceho klinického usmernenia a R1/R2/R3 predstavovalo tri úrovne štýlu odpovedania simulovaného pacienta. Aby sa označenie štýlu odpovedania nebilo s defektovými položkami R1 až R5, v hlavnom texte práce tento faktor označujeme ako P1/P2/P3. V psychologickom jazyku teda pracujeme s týmto mapovaním:

- G0 = bez štruktúrujúceho klinického usmernenia,
- G1 = so štruktúrujúcim klinickým usmernením,
- P1 = zdržanlivý štýl odpovedania simulovaného pacienta,
- P2 = vyvážený štýl odpovedania simulovaného pacienta,
- P3 = rozvinutý štýl odpovedania simulovaného pacienta.

Pri finálnom balíku prepisov rozhovorov bola variabilita nastavená ako **uzamknutá**, aby sa minimalizoval nekontrolovaný posun generovania a aby sa v hodnotení testovali primárne práve experimentálne manipulované vlastnosti generovania. Mimo zámerne menených faktorov sa výskum snažil zachovať čo najvyššiu štandardizáciu (rovnaký protokol rozhovoru, rovnaký počet replík, rovnaký formát exportu, rovnaké nastavenie modelových parametrov mimo dvoch sledovaných faktorov).

Výhodou takto pripraveného materiálu bolo, že umožňoval súčasne sledovať dve úrovne variability. Prvou bola **klinická variabilita medzi východiskovými scenármi**, teda odlišnosti medzi rôznymi modelovými prípadmi depresívnej symptomatiky. Druhou bola **experimentálna variabilita** spôsobená štruktúrujúcim klinickým usmernením a štýlom odpovedania simulovaného pacienta. Tento dvojvrstvový dizajn zvyšuje ekologickú validitu výskumu, pretože hodnotitelia neporovnávali len technicky mierne odlišné texty, ale rozhovory založené na odlišných klinických situáciách, pri ktorých sa zároveň testoval vplyv dvoch systematicky manipulovaných vlastností generovania.

### 2.4 Hodnotiaci nástroj

Na zber hodnotení bol použitý **autorsky zostavený hodnotiaci dotazník** implementovaný v internom dotazníkovom rozhraní. Nástroj obsahoval tri hlavné bloky položiek, jednu nominálnu položku odhadovaného pôvodu rozhovoru a jednu otvorenú textovú položku. Jeho public-safe znenie je uvedené v Prílohe A.

#### 2.4.1 Štruktúra blokov

**Prvý blok – primárne kvalitatívne výstupné ukazovatele G1 až G5** zachytáva globálne expertné hodnotenie rozhovoru. Hodnotiteľ posudzuje rozhovor ako celok, teda nie jednotlivý symptomatický detail, ale odborný dojem z textu:

- G1 = klinická vierohodnosť rozhovoru,
- G2 = prirodzenosť jazyka a plynulosť odpovedí,
- G3 = vnútorná konzistentnosť rozhovoru,
- G4 = súlad rozhovoru s obrazom depresívnej symptomatiky,
- G5 = použiteľnosť rozhovoru na tréningové alebo výučbové účely.

**Druhý blok – globálne odhady závažnosti a funkčného dopadu S1 a S2** zachytáva expertný úsudok hodnotiteľa o tom, aký celkový stupeň depresívnej závažnosti a aký funkčný dopad rozhovor implikuje. Položka S1 reprezentuje odhad celkovej závažnosti a položka S2 odhad funkčného dopadu na bežné fungovanie.

**PHQ-9 symptomatické metadata na úrovni prepisu rozhovoru A1 až A9** nepredstavujú dodatočné ľudské hodnotenia od hodnotiteľa. Ide o štruktúrované PHQ-9 symptomatické polia importované z prostredia Sim Lab / Chat Lab, teda o sebapopisnú vrstvu pripojenú k danému simulovanému pacientovi a prepisu rozhovoru. Položky A1 až A9 zodpovedajú deviatim obsahovým oblastiam depresívnej symptomatiky zavedeným v Úvode (1.1) a previazaným s logikou PHQ-9, ktorú operacionalizovali @kroenke2001phq9. V analýze preto slúžia prednostne ako symptomatický profil na úrovni prepisu rozhovoru a ako podklad pre porovnanie s vopred definovanými kotvami východiskového scenára, nie ako psychometrická súčasť expertného hodnotiaceho nástroja.

**Tretí blok – položky kontroly kvality a defektov R1 až R5** zachytávajú kvalitatívne defekty, ktoré síce nemusia byť „symptómami" v pravom slova zmysle, ale môžu zásadne znižovať použiteľnosť rozhovoru v metodologickom alebo pedagogickom kontexte:

- R1 = prítomnosť kontradikcií alebo zjavnej nekonzistentnosti,
- R2 = prítomnosť klišéovitých alebo stereotypných formulácií,
- R3 = kontextový nesúlad alebo odpovede mimo zamýšľaného klinického rámca,
- R4 = podozrenie na inú primárnu psychopatológiu, než je cieľový profil východiskového scenára,
- R5 = neprimeraná dramatizácia alebo neautentické zveličovanie.

Súčasťou nástroja bola aj nominálna položka odhadovaného pôvodu rozhovoru (s možnosťami: AI-generovaný, ľudsky simulovaný, reálny účastník, neviem odhadnúť), položka zachytávajúca istotu tohto odhadu a otvorená textová položka určená na slobodný kvalitatívny komentár hodnotiteľa.

#### 2.4.2 Odpoveďové formáty

Položky G1 až G5, S1, S2, položky R1 až R5 a položka zachytávajúca istotu odhadu pôvodu boli koncipované ako **5-bodové škály** a v analýze sú chápané ako ordinálne premenné. Naproti tomu A1 až A9 nie sú súčasťou ľudského hodnotiaceho formulára, ale importované PHQ-9 symptomatické skóre na úrovni prepisu rozhovoru na **škále 0–3**. Toto rozlíšenie je metodicky dôležité: expertná evaluácia a symptomatické metadata na úrovni prepisu rozhovoru sa v práci používajú spoločne, ale nepredstavujú jednu a tú istú meraciu vrstvu.

Takéto členenie dátovej štruktúry umožnilo oddeliť jadro expertného hodnotenia rozhovoru od symptomatického profilu na úrovni prepisu rozhovoru a od vrstvy kontroly kvality. Zároveň tým vznikol priamy most medzi teoretickými konštruktmi v Úvode (klinická vierohodnosť, prirodzenosť, konzistentnosť, symptomatická primeranosť, varovné signály, tréningová použiteľnosť — časť 1.5) a empirickými premennými použitými v analýze.

#### 2.4.3 Status psychometrických vlastností

Keďže ide o autorský nástroj, v literatúre nie sú k dispozícii jeho predchádzajúce psychometrické charakteristiky. Z tohto dôvodu sa analýza vnútornej konzistencie a zhody medzi hodnotiteľmi stáva súčasťou overovania nástroja v konkrétnom výskumnom kontexte. Takýto postup je v súlade s lokálnym sprievodcom záverečných prác aj s odporúčaniami COSMIN metodológie pre obsahovú validitu a vnútornú konzistenciu pri novo zostavených hodnotiacich nástrojoch, ktoré rozpracovali @terwee2018COSMINMethodologyEvaluating a @boateng2018scaledevelopment. Pri reporte vnútornej konzistencie a zhody medzi hodnotiteľmi sa preto v kapitole Výsledky vychádza priamo z aktuálneho výskumu.

#### 2.4.4 Predbežná expertná obsahová kontrola položiek a východiskových scenárov

Popri neskoršej analýze vnútornej konzistencie a zhody medzi hodnotiteľmi bola do pracovného postupu zaradená aj **predbežná expertná obsahová kontrola** autorského hodnotiaceho dotazníka a východiskových scenárov. V tejto vrstve experti neposudzovali hotové prepisy rozhovorov, ale samotné položky nástroja a klinicky ukotvené východiskové scenáre ešte pred ich finálnym použitím v hlavnom hodnotení. Pri položkách sa sledovala ich relevancia, zrozumiteľnosť a potrebnosť pre finálny nástroj; pri východiskových scenároch klinická vierohodnosť, primeranosť symptomatických kotiev, jasnosť, dostatok informácií pre generovanie rozhovoru, nestereotypnosť a použiteľnosť pre výskumný alebo výučbový kontext.

V aktuálnom stave táto vrstva zahŕňala **šesť expertov**. Každý expert hodnotil 12 položiek hodnotiaceho nástroja na troch kritériách (relevancia, zrozumiteľnosť, potrebnosť) a 12 východiskových scenárov na siedmich hodnotiacich dimenziách, doplnených odhadom cieľovej závažnosti a otvoreným komentárom. Táto vrstva preto v práci nebude interpretovaná ako plnohodnotná psychometrická validácia ani ako formálny Delphi proces. Jej funkciou je zachytiť zjavne problematické formulácie, nejednoznačné položky alebo klinicky sporné nastavenia východiskových scenárov a zdokumentovať odporúčané redakčné úpravy pred hlavným hodnotením prepisov rozhovorov, čo zodpovedá logike obsahovej kalibrácie a expertného konsenzu opisovanej v prácach @polit2007cvi, @hasson2000delphi, @boateng2018scaledevelopment a @rutherfordhemming2015simulationcvi. Pri položkách dotazníka možno pomocne uviesť aj položkové podiely hodnotení `3-4`, tie však budú vzhľadom na veľkosť panelu interpretované opatrne a vždy spolu s kvalitatívnymi komentármi expertov, ako odporúčajú aj @terwee2018COSMINMethodologyEvaluating a @polit2007cvi.

### 2.5 Operacionalizácia teoretických pojmov a empirické premenné

V Úvode (časti 1.5 a 1.7) boli zavedené tri kľúčové teoretické konštrukty: **prítomnosť štruktúrujúceho klinického usmernenia**, **štýl odpovedania simulovaného pacienta** a **kvalita simulovaného rozhovoru**. V tejto časti opisujeme ich empirické zachytenie v hodnotiacom nástroji a v odvodených ukazovateľoch.

#### 2.5.1 Nezávislé premenné

**Prítomnosť štruktúrujúceho klinického usmernenia** bola operacionalizovaná ako binárna nezávislá premenná s dvoma úrovňami:

- G0 = bez štruktúrujúceho klinického usmernenia,
- G1 = so štruktúrujúcim klinickým usmernením.

V psychologickom jazyku reprezentuje táto premenná mieru explicitného riadenia generovania rozhovoru s cieľom zvýšiť jeho konzistentnosť, tematickú disciplínu a klinickú primeranosť. Príbuznú logiku v literatúre LLM simulovaných pacientov nájdeme v CureFun, PATIENT-ψ a Adaptive-VP; @li2024curefun, @wang2024patientpsi a @lee2025adaptivevp opisujú explicitné štruktúrujúce mechanizmy na riadenie modelového správania.

**Štýl odpovedania simulovaného pacienta** bol operacionalizovaný ako trojúrovňová kategoriálna nezávislá premenná. V exporte je uložený v poli `profile` s kódmi R1 až R3; v texte práce používame pracovné označenie P1 až P3:

- P1 = zdržanlivý štýl odpovedania,
- P2 = vyvážený štýl odpovedania,
- P3 = rozvinutý štýl odpovedania.

Táto premenná reprezentuje rozdiely v miere otvorenosti, stručnosti, spontánnej elaborácie a detailnosti odpovedí v rozhovore. Ide o zámerné zjednodušenie kontinua otvorenosti sebazdieľania, ktoré v literatúre LLM klientov modeluje napríklad @kim2025mindvoyager cez metakogníciu a kontrolu otvorenosti sebazdieľania.

#### 2.5.2 Blokovacie a náhodné faktory

**Východiskový scenár** predstavoval blokovací faktor, ktorý zachytával klinický základ modelového prípadu. Východiskový scenár nebol predmetom hypotetického záujmu ako nezávislá premenná v psychologickom zmysle, ale metodicky slúžil na zachytenie systematickej variability medzi prípadmi. Pojem blokovací faktor tu znamená, že pri modelovaní oddeľujeme rozdiely medzi východiskovými scenármi od hlavných experimentálnych faktorov, aby sa efekt usmernenia alebo štýlu odpovedania neplietol s tým, že niektoré prípady sú samy osebe klinicky odlišné alebo náročnejšie.

**Identita hodnotiteľa** predstavovala ďalší zdroj variability, ktorý bolo potrebné zohľadniť na úrovni modelovania. Rozdiely medzi hodnotiteľmi mohli vyplývať z profesijného zázemia, prísnosti hodnotenia, skúsenosti či preferovaného klinického štýlu, a preto boli v inferenčných modeloch zohľadňované ako náhodný efekt.

#### 2.5.3 Primárne závislé premenné

Primárne závislé premenné tvorili položky G1 až G5 z prvého bloku hodnotiaceho nástroja. Na **deskriptívnej úrovni** budú tieto položky reportované ako ordinálne ukazovatele prostredníctvom frekvencií, mediánov a interkvartilových rozpätí. Na **inferenčnej úrovni** budú položky G2 a G5 vystupovať ako samostatné ordinálne výstupné ukazovatele modelované pomocou ordinálnych zmiešaných modelov; položky G1, G3 a G4 budú slúžiť prednostne ako obsahová opora kompozitu klinickej vierohodnosti a len sekundárne ako položkové spresnenie hlavného výsledku.

Okrem jednotlivých položiek bol vytvorený kompozitný ukazovateľ **indexu klinickej vierohodnosti**, vypočítaný ako priemer položiek G1, G3 a G4, keďže tieto tri položky podľa projektovej logiky a obsahovej validity konceptuálne najtesnejšie reprezentujú jadro klinickej vierohodnosti simulovaného rozhovoru.

Index klinickej vierohodnosti bol vypočítaný ako: (G1 + G3 + G4) / 3.

Keďže ide o kompozit s približne intervalovým charakterom, index klinickej vierohodnosti bude v tabuľkách reportovaný primárne pomocou priemeru a smerodajnej odchýlky a doplnkovo možno uviesť aj medián a interkvartilové rozpätie. V inferenčnej analýze vystupuje ako hlavný výstupný ukazovateľ pre lineárne zmiešané modely. Položka G2 (prirodzenosť jazyka) je analyzovaná samostatne ako ordinálny ukazovateľ jazykovej a interakčnej kvality. Položka G5 (tréningová použiteľnosť) je analyzovaná samostatne ako ordinálny ukazovateľ celkového odborného úsudku o pedagogickej využiteľnosti rozhovoru.

#### 2.5.4 Sekundárne premenné a ukazovatele odchýlky

Sekundárnu vrstvu premenných tvorili dve navzájom odlišné, ale obsahovo prepojené časti. Prvou sú položky A1 až A9, ktoré predstavujú PHQ-9 symptomatické metadata importované zo sebapopisnej vrstvy simulovaného pacientského profilu na úrovni prepisu rozhovoru. Druhou sú položky S1 a S2, ktoré predstavujú expertný odhad celkovej závažnosti a funkčného dopadu.

Na **deskriptívnej úrovni** budú A1 až A9 reportované oddelene od ľudských hodnotení ako ukazovatele na úrovni prepisu rozhovoru; pri každej doméne je možné uviesť priemer, smerodajnú odchýlku, medián aj interkvartilové rozpätie podľa potreby. Položky S1 a S2 ostávajú ordinálnymi ľudskými hodnoteniami a budú deskriptívne sumarizované cez frekvencie, mediány a interkvartilové rozpätia. Na **inferenčnej úrovni** však jadro tejto vetvy netvoria jednotlivé doménové položky A1 až A9 ani samotné ordinálne hodnotenia S1 a S2, ale odvodené ukazovatele odchýlky, ktoré už majú jasný empirický význam vzhľadom na profil kotiev východiskového scenára.

Keďže pre každý východiskový scenár boli vopred definované kotvové hodnoty, bolo možné odvodiť aj **ukazovatele odchýlky** vyjadrujúce mieru zhody rozhovoru s cieľovým profilom. Pri A1 až A9 ide o zhodu na úrovni prepisu rozhovoru medzi importovaným PHQ-9 profilom a kotvou východiskového scenára. Pri S1 a S2 ide o expertne hodnotené položky závažnosti a funkčného dopadu; keďže kotvy východiskového scenára aj ľudské hodnotenia používajú rovnakú `1-5` škálu, ukazovatele odchýlky sa počítajú priamo bez dodatočnej harmonizácie.

- priemerná absolútna chyba v symptomatických doménach = (|A1 − anchor(A1)| + |A2 − anchor(A2)| + ... + |A9 − anchor(A9)|) / 9,
- chyba odhadu závažnosti = absolútna odchýlka expertného hodnotenia S1 od kotvovej hodnoty S1,
- chyba odhadu funkčného dopadu = absolútna odchýlka expertného hodnotenia S2 od kotvovej hodnoty S2.

Nižšia hodnota týchto ukazovateľov znamená vyššiu presnosť zhody rozhovoru s cieľovým východiskovým scenárom. Priemerná absolútna chyba v symptomatických doménach slúži prednostne ako ukazovateľ zhody na úrovni prepisu rozhovoru a bude reportovaná ako priemer a smerodajná odchýlka, prípadne doplnkovo medián a interkvartilové rozpätie. Rovnako budú reportované aj `severity_error` a `impact_error`, ktoré sa v inferenčnej časti používajú ako sekundárne približne intervalové výstupné ukazovatele. Expertne hodnotené položky závažnosti a funkčného dopadu zároveň ostávajú v texte viditeľné aj ako samostatná ordinálna ľudská vrstva. V kombinácii s indexom klinickej vierohodnosti tak možno odlíšiť „vyzerá dobre na povrchu“ od „zodpovedá zamýšľanému klinickému obrazu“.

Keďže kotvy východiskového scenára `S1_anchor` a `S2_anchor` boli finálne zarovnané na rovnakú `1-5` škálu ako expertné hodnotenia, je možné popri samostatnom vyhodnotení položiek S1 a S2 reportovať aj ich priamu chybovú verziu voči týmto kotvám.

#### 2.5.5 Premenné kontroly kvality a kompozit defektov

Premenné kontroly kvality tvorili položky R1 až R5, z ktorých bol odvodený kompozit **indexu defektov**. Ich účelom bolo zachytiť nedostatky rozhovorov, ktoré mohli znižovať ich metodologickú alebo výučbovú využiteľnosť. Na deskriptívnej úrovni budú položky R1 až R5 reportované ako ordinálne ukazovatele prostredníctvom frekvencií, mediánov a interkvartilových rozpätí. V inferenčnej rovine však jadrom tejto vetvy nie sú jednotlivé položky, ale ich kompozitný priemer, teda index defektov. Index defektov je v práci operacionalizovaný ako priemer položiek R1 až R5.

Index defektov bol vypočítaný ako: (R1 + R2 + R3 + R4 + R5) / 5.

Vyššia hodnota indexu defektov znamená vyšší výskyt defektov a teda nižšiu metodologickú a pedagogickú použiteľnosť rozhovoru. Index defektov je primárnym ukazovateľom pre hypotézu H3.

#### 2.5.6 Doplnkové premenné

Položka odhadovaného pôvodu rozhovoru predstavovala nominálnu premennú so štyrmi možnosťami odpovede: AI-generovaný, ľudsky simulovaný, reálny účastník, neviem odhadnúť. Položka istoty odhadu reprezentovala istotu tohto odhadu na 5-bodovej škále. Otvorená textová premenná komentára slúžila na kvalitatívne doplnenie expertnej evaluácie a umožňovala hodnotiteľovi pomenovať vlastné dôvody pozitívneho alebo negatívneho hodnotenia.

#### 2.5.7 Konzistentnosť názvov premenných

V celej práci používam rovnaké slovenské názvy premenných naprieč metódou, výsledkami a tabuľkami, aby nevznikol nesúlad medzi jednotlivými časťami rukopisu. Technické názvy z analytickej kódovej knihy a z R skriptu ostávajú súčasťou interného pracovného postupu, nie finálneho jazyka práce.

#### 2.5.8 Empirický jazyk ukazovateľov a väzba na testy

Vzhľadom na použitý faktorový komparačný dizajn je dôležité, aby boli empirické premenné v texte pomenované v jazyku, ktorý zodpovedá ich operacionalizácii aj typu plánovaného testu. V tejto práci preto nepoužívame jeden univerzálny jazyk pre všetky výstupné ukazovatele. To, či hovoríme o priemere, mediáne, distribúcii alebo pravdepodobnosti vyššieho skóre, závisí od typu premennej.

- **Ordinálne položky** (`G1` až `G5`, `S1`, `S2`, `R1` až `R5`) sú v deskriptívnej časti reportované cez frekvencie, mediány a interkvartilové rozpätia. Ak vstupujú do inferenčnej analýzy samostatne, formulujeme otázku ako rozdiel v distribúcii alebo ako vyššiu pravdepodobnosť dosiahnutia vyššieho skóre.
- **Kompozitné ukazovatele a ukazovatele odchýlky** (index klinickej vierohodnosti, index defektov, priemerná absolútna chyba v symptomatických doménach, chyba odhadu závažnosti, chyba odhadu funkčného dopadu) sú v deskriptívnej časti reportované primárne cez priemer a smerodajnú odchýlku a doplnkovo môžu mať uvedený aj medián a interkvartilové rozpätie. V inferenčnej časti sa pri nich pýtame na rozdiel v priemernej úrovni medzi experimentálnymi podmienkami.
- **Nominálne premenné** (odhadovaný pôvod rozhovoru) sú reportované cez frekvencie a percentá; v exploratívnej inferencii ich možno formulovať ako rozdiel v podieloch alebo v pravdepodobnosti konkrétnej kategórie odpovede.
- **Otvorené komentáre** nevystupujú ako číselné premenné, ale ako tematické kategórie. V ich prípade sa nepýtame na priemer ani medián, ale na frekvenciu a obsah opakujúcich sa tém.

Tento rozlišovací rámec je dôležitý aj pre formuláciu empirických výskumných otázok a hypotéz v nasledujúcej časti. Keďže hlavné prediktory práce sú kategoriálne experimentálne faktory, jadro empirického jazyka je v tejto práci **komparačné**, nie korelačné. Korelačný jazyk sa používa iba v doplnkových exploratórnych analýzach, nie pri jadrovom testovaní H1 až H9.

#### 2.5.9 Prehľad hlavných odvodených ukazovateľov

Keďže sa v tabuľkách a modelových výstupoch práce používajú aj odvodené ukazovatele, nasledujúca tabuľka zhŕňa ich konštrukciu na jednom mieste. Jej funkciou je explicitne ukázať, z ktorých vstupných premenných ukazovateľ vzniká, na akej úrovni sa reportuje a ako sa má interpretovať jeho smer.

**Tabuľka 1**  
*Prehľad hlavných odvodených ukazovateľov*

| Ukazovateľ | Vstupné premenné | Výpočet | Reportovaná úroveň | Interpretácia |
| --- | --- | --- | --- | --- |
| Index klinickej vierohodnosti | `G1`, `G3`, `G4` | `mean(G1, G3, G4)` | rating-level kompozit | vyššia hodnota znamená vyššiu klinickú vierohodnosť rozhovoru |
| Index defektov | `R1`, `R2`, `R3`, `R4`, `R5` | `mean(R1, R2, R3, R4, R5)` | rating-level kompozit | vyššia hodnota znamená vyšší výskyt defektov |
| Priemerná absolútna chyba v symptomatických doménach | `A1` až `A9` a ich kotvy `A1_anchor` až `A9_anchor` | `mean(abs(Ai - Ai_anchor))` pre `i = 1...9` | transcript-level ukazovateľ | nižšia hodnota znamená vyššiu zhodu so symptomatickým profilom východiskového scenára |
| Chyba odhadu závažnosti | `S1`, `S1_anchor` | najprv `abs(S1 - S1_anchor)` pri jednotlivom hodnotení, potom priemer za prepis rozhovoru v transcript-level vetve | odvodený error ukazovateľ reportovaný na transcript-level | nižšia hodnota znamená vyššiu zhodu s kotvou závažnosti |
| Chyba odhadu funkčného dopadu | `S2`, `S2_anchor` | najprv `abs(S2 - S2_anchor)` pri jednotlivom hodnotení, potom priemer za prepis rozhovoru v transcript-level vetve | odvodený error ukazovateľ reportovaný na transcript-level | nižšia hodnota znamená vyššiu zhodu s kotvou funkčného dopadu |

Dôležité je, že položky `S1` a `S2` ako samostatné ordinálne ľudské hodnotenia ostávajú rating-level premennými. Na úroveň prepisu rozhovoru sa presúvajú iba ich odvodené chybové verzie, aby anchor-fidelity vetva nevážila prepisy rozhovorov podľa počtu dostupných hodnotení. Rovnako položky `A1` až `A9` nepredstavujú opakované ľudské ratingy, ale transcript-level metadata, a preto z nich odvodená symptomatická chyba patrí metodicky do transcript-level vetvy.

### 2.6 Empirické výskumné otázky a hypotézy

Lokálny sprievodca uvádza, že po teoretickom vymedzení výskumného problému majú v Metóde nasledovať empirické výskumné otázky a hypotézy formulované v jazyku pozorovateľných alebo odvodených premenných. V tejto práci preto vedľa širších VO1 až VO8 z Úvodu používame aj ich **empirický preklad** viazaný na operacionalizáciu premenných a na typ testu. Keďže jadro dizajnu je komparačné a hlavné prediktory sú kategoriálne experimentálne faktory, nejde tu primárne o korelačný jazyk, ale o jazyk **rozdielu v priemere**, **rozdielu v mediáne alebo distribúcii** a pri ordinálnych modeloch o **pravdepodobnosť vyššieho skóre**.

#### 2.6.1 Empirické výskumné otázky (rekapitulácia z Úvodu, 1.7)

**Blok A — globálna kvalita rozhovoru a symptomatická primeranosť**

**VO1.** Aké sú frekvenčné rozdelenia, mediány a interkvartilové rozpätia položiek G1 až G5 a aká je priemerná úroveň indexu klinickej vierohodnosti pri AI-generovaných simulovaných klinických rozhovoroch o depresívnej symptomatike?

**VO2.** Aká je priemerná absolútna chyba symptomatických domén A1 až A9 na úrovni prepisu rozhovoru voči kotvám východiskových scenárov a aké sú rozdelenia expertných hodnotení S1 a S2, resp. ich priamych chybových skóre voči týmto kotvám?

**Blok B — štýl odpovedania simulovaného pacienta**

**VO3.** Líši sa priemerná úroveň indexu klinickej vierohodnosti a distribúcia skóre na položkách G2 a G5 medzi úrovňami štýlu odpovedania simulovaného pacienta P1, P2 a P3?

**VO4.** Líši sa priemerná absolútna chyba v symptomatických doménach, chyba odhadu závažnosti, chyba odhadu funkčného dopadu a priemerná úroveň indexu defektov medzi úrovňami štýlu odpovedania simulovaného pacienta P1, P2 a P3?

**Blok C — interakcia, zhoda a doplnkové výstupy**

**VO5.** Je pri indexe klinickej vierohodnosti, indexe defektov a hlavných ukazovateľoch odchýlky prítomná interakcia medzi prítomnosťou štruktúrujúceho klinického usmernenia a štýlom odpovedania simulovaného pacienta?

**VO6.** Aká je miera zhody medzi odbornými hodnotiteľmi pri posudzovaní kvality rozhovoru (ICC pre index klinickej vierohodnosti, index defektov a expertné odhady závažnosti a funkčného dopadu)?

**VO7.** Aké sú frekvencie a podiely jednotlivých kategórií odhadovaného pôvodu rozhovoru a aké je rozdelenie istoty tohto odhadu?

**VO8.** Aké typy pozitívnych a negatívnych komentárov sa v otvorených odpovediach odborných hodnotiteľov objavujú najčastejšie?

V poradí výsledkov budú tieto bloky reportované takto: VO1 až VO2 ako deskriptívny a symptomaticko-fidelitný blok, VO3 až VO4 ako blok efektu štýlu odpovedania, VO5 ako interakčný blok, VO6 ako blok zhody a VO7 až VO8 ako doplnkový exploračný blok. Konfirmačný efekt prítomnosti štruktúrujúceho klinického usmernenia je vzhľadom na silnejšiu literárnu oporu testovaný primárne cez H1 až H5, aby sa zbytočne nezdvojovala výskumná otázka a hypotéza pre ten istý analytický test. Prakticky to znamená, že VO bloky opisujú, **čo bude reportované**, zatiaľ čo hypotézy nižšie presnejšie hovoria, **aký rozdiel v priemere alebo distribúcii očakávame**.

#### 2.6.2 Empirické hypotézy – jadro (H1–H5)

Jadrové hypotézy práce smerujú prednostne na premennú prítomnosti štruktúrujúceho klinického usmernenia, pretože @li2024curefun, @wang2024patientpsi a @lee2025adaptivevp poskytujú najpresvedčivejšiu doterajšiu oporu pre význam klinicky ukotveného a štruktúrovaného riadenia simulácie. Tieto hypotézy sú formulované jednostranne, pretože predpokladáme konkrétny smer účinku.

**Blok A — hypotézy ku globálnej kvalite rozhovoru a symptomatickej primeranosti (VO1, VO2)**

**H1.** Priemerná hodnota indexu klinickej vierohodnosti bude vyššia pri rozhovoroch vytvorených so štruktúrujúcim klinickým usmernením než pri rozhovoroch vytvorených bez neho; sekundárne budú aj položky G1, G3 a G4 vykazovať posun distribúcie k vyšším kategóriám.

**H2.** Distribúcia odpovedí na položke G2 bude pri rozhovoroch vytvorených so štruktúrujúcim klinickým usmernením posunutá k vyšším kategóriám než pri rozhovoroch vytvorených bez tohto usmernenia.

**H3.** Priemerná hodnota indexu defektov bude nižšia pri rozhovoroch vytvorených so štruktúrujúcim klinickým usmernením než pri rozhovoroch vytvorených bez neho; sekundárne budú aj položky R1 až R5 vykazovať posun distribúcie k nižším kategóriám.

**H4.** Priemerná absolútna chyba v symptomatických doménach A1 až A9 na úrovni prepisu rozhovoru voči kotvám východiskových scenárov bude nižšia pri rozhovoroch vytvorených so štruktúrujúcim klinickým usmernením než pri rozhovoroch bez neho; rovnaký smer očakávame sekundárne aj pri priamych chybových skóre závažnosti a funkčného dopadu.

**H5.** Distribúcia odpovedí na položke G5 bude pri rozhovoroch vytvorených so štruktúrujúcim klinickým usmernením posunutá k vyšším kategóriám než pri rozhovoroch vytvorených bez tohto usmernenia.

#### 2.6.3 Empirické hypotézy – rozšírená pracovná vrstva (H6–H9)

Popri jadrových hypotézach sú v práci formulované aj rozšírené hypotézy zamerané na efekt štýlu odpovedania simulovaného pacienta a na interakciu oboch faktorov. Tieto hypotézy môžu byť pri finálnej redakcii buď ponechané, alebo redukované podľa sily ich literárnej opory.

**Blok B — hypotézy k efektu štýlu odpovedania simulovaného pacienta (VO3, VO4)**

**H6.** Priemerná hodnota indexu klinickej vierohodnosti bude vyššia pri rozhovoroch s vyváženým alebo rozvinutým štýlom odpovedania simulovaného pacienta (P2, P3) než pri rozhovoroch so zdržanlivým štýlom odpovedania (P1).

**H7.** Distribúcia odpovedí na položkách G2 a G5 bude pri rozvinutejšom štýle odpovedania simulovaného pacienta (P3) posunutá k vyšším kategóriám než pri zdržanlivejšom štýle odpovedania (P1, prípadne P2).

**H8.** Priemerná absolútna chyba v symptomatických doménach A1 až A9 na úrovni prepisu rozhovoru voči kotvám východiskových scenárov bude nižšia pri rozvinutejšom štýle odpovedania simulovaného pacienta (P3) než pri zdržanlivejšom štýle (P1).

Pri širšie formulovanej VO4 zatiaľ samostatne nehypotetizujeme efekt štýlu odpovedania pre expertne hodnotenú závažnosť, expertne hodnotený funkčný dopad a index defektov, pretože pre takto špecifický smer účinku nemáme rovnako silnú literárnu oporu ako pre priemernú absolútnu chybu v symptomatických doménach na úrovni prepisu rozhovoru. Tieto výstupy preto budú vo Výsledkoch spracované ako inferenčná odpoveď na VO4, nie ako samostatné smerové hypotézy.

**Blok C — hypotéza k interakcii a nehypotetické bloky (VO5–VO8)**

**H9.** Interakčný efekt medzi prítomnosťou štruktúrujúceho klinického usmernenia a štýlom odpovedania simulovaného pacienta bude štatisticky prítomný najmä pri indexe klinickej vierohodnosti a indexe defektov, pričom pozitívny účinok štruktúrujúceho klinického usmernenia bude najsilnejší pri rozvinutejšom štýle odpovedania (P3).

Pre VO6 neformulujeme samostatnú hypotézu, pretože ide o merací blok zameraný na mieru zhody hodnotiteľov. VO7 a VO8 ostávajú zámerne exploračné a budú reportované bez samostatných smerových hypotéz.

### 2.7 Procedúra výskumu

#### 2.7.1 Príprava podnetového materiálu

Najprv bol pripravený finálny balík východiskových scenárov a experimentálnych variantov generovania. Východiskové scenáre vznikali iteratívne a po každom revíznom kole sa spresňovali ich symptomatické kotvy, formulácie aj kontrolné pravidlá na základe predbežnej expertnej a technickej kontroly. Následne boli vygenerované textové prepisy rozhovorov podľa jednotného protokolu rozhovoru a uložené v štandardizovanom formáte. Pred zaradením do hodnotenia boli prepisy rozhovorov skontrolované z hľadiska technickej úplnosti a formálnej konzistencie. Táto predbežná kontrola mala zabezpečiť, aby hodnotitelia neposudzovali technicky poškodené, neúplné alebo zjavne chybne exportované materiály.

#### 2.7.2 Priebeh hodnotenia

Hodnotitelia dostávali na posúdenie jednotlivé prepisy rozhovorov prostredníctvom webového hodnotiaceho rozhrania. Pri každom prepise rozhovoru vyplnili hodnotiaci dotazník a podľa potreby doplnili otvorený komentár. V závislosti od finálneho rozdelenia hodnotiacej záťaže a od faktickej dostupnosti jednotlivých hodnotiteľov mohol byť počet hodnotení na prepis rozhovoru **variabilný**, pričom cieľom bolo pri každom prepise rozhovoru dosiahnuť aspoň dvojnásobné nezávislé hodnotenie. Hodnotenie prebiehalo individuálne a asynchrónne.

Poradie predkladania prepisov rozhovorov bolo **blokovo randomizované**: v rámci každého hodnotiteľa boli prepisy rozhovorov zoskupené do blokov tak, aby bolo vyvážené zastúpenie experimentálnych buniek vytvorených kombináciou prítomnosti štruktúrujúceho klinického usmernenia a štýlu odpovedania simulovaného pacienta, a v rámci každého bloku bolo poradie náhodné. Tento postup obmedzuje poradiové efekty a zároveň zabezpečuje, aby žiadny hodnotiteľ nebol vystavený nárazovo iba jednému typu variantu. Hodnotitelia boli pred začatím hodnotenia explicitne informovaní, že **ide výlučne o AI-generovaný materiál**, teda že všetky predkladané prepisy rozhovorov pochádzajú zo simulovaného rozhovoru vedeného veľkým jazykovým modelom v role pacienta. Toto rozhodnutie zvyšuje etickú transparentnosť hodnotenia a je dôležité aj pre interpretáciu položky odhadovaného pôvodu rozhovoru, ktorá v tomto nastavení nezachytáva neslepý odhad pôvodu, ale skôr to, či hodnotiteľ napriek vedomiu o AI pôvode rozpozná rozhovor ako zjavne strojovo generovaný, alebo či ho z hľadiska vnútornej koherencie posúdi ako prijateľne podobný reálnej alebo ľudsky simulovanej výpovedi.

#### 2.7.3 Export a štruktúra dát

Pri exporte odpovedí sa odpovede ukladané v JSON štruktúre konvertovali do tabuľkového formátu vhodného na následné štatistické spracovanie. Finálny analytický dátový súbor mal **dlhý formát** a obsahoval identifikátor hodnotiteľa, identifikátor prepisu rozhovoru, identifikátor východiskového scenára, experimentálne premenné prítomnosti štruktúrujúceho klinického usmernenia a štýlu odpovedania simulovaného pacienta, ľudské položkové hodnotenia G1 až G5, S1, S2 a R1 až R5, PHQ-9 symptomatické metadata na úrovni prepisu rozhovoru A1 až A9, doplnkové položky odhadovaného pôvodu rozhovoru, istoty odhadu a komentára a všetky odvodené kompozity. V technickom exporte je faktor štýlu odpovedania vedený pod poľom `profile`; v interných analytických súboroch sa môžu objavovať aj skrátené kódy G0/G1 a P1/P2/P3, kým v rukopise tieto úrovne označujeme slovenskými pomenovaniami.

### 2.8 Spracovanie dát a štatistická analýza

Štatistické spracovanie a modelovanie boli v tejto práci realizované primárne v **jazyku R**. Jazyk **Python** bol použitý pri niektorých pomocných technických krokoch pracovného postupu, najmä pri importe, čistení a kontrole dátových exportov, pri príprave pomocných súborov a pri automatizácii vybraných krokov kontroly kvality a exportu. R slúžil ako hlavné analytické prostredie pre deskriptívnu štatistiku, reliabilitné ukazovatele, `ICC`, zmiešané modely aj doplnkové analýzy na úrovni prepisu rozhovoru.

#### 2.8.1 Predspracovanie dát

Pred analýzou boli všetky exportované odpovede skontrolované, vyčistené a prekódované. Likertove odpovede boli konvertované zo stringového exportu na numerické alebo ordinálne premenné podľa typu plánovanej analýzy. Osobitne bolo overené, že PHQ-9 symptomatické metadata A1 až A9 na úrovni prepisu rozhovoru sú konzistentné s príslušným prepisom rozhovoru a východiskovým scenárom a že sa metodicky nemiešajú s ľudskými hodnoteniami. Následne boli vytvorené odvodené premenné indexu klinickej vierohodnosti, indexu defektov, priemernej absolútnej chyby v symptomatických doménach, ako aj priame chyby odhadu závažnosti a chyby odhadu funkčného dopadu voči kotvám východiskového scenára `S1_anchor` a `S2_anchor`, keďže tieto kotvy aj ľudské hodnotenia používajú rovnakú `1-5` škálu. Pri predspracovaní bolo zároveň overené, či nevznikli technické chýbajúce hodnoty, duplikované záznamy alebo nekompletné exporty.

#### 2.8.2 Deskriptívna analýza

Najprv bola spracovaná **deskriptívna štatistika** položiek a kompozitov. Pri ľudsky hodnotených ordinálnych položkách boli sledované frekvencie, mediány a interkvartilové rozpätia, pri kompozitných ukazovateľoch aj priemery a smerodajné odchýlky. PHQ-9 symptomatické metadata A1 až A9 na úrovni prepisu rozhovoru budú reportované oddelene ako vlastnosť samotných prepisov rozhovorov a ako súčasť ich kotvovej zhody, nie ako frekvenčné rozdelenie odpovedí hodnotiteľov. V súlade s lokálnym sprievodcom budú prezentované základné miery polohy a variability tak, aby mal čitateľ jasnú predstavu o správaní sa jednotlivých premenných ešte pred inferenčnou analýzou. Súčasťou tohto kroku bude aj stručná sumarizácia kontroly kvality dátového súboru, najmä počet hodnotiteľov, počet prepisov rozhovorov, počet východiskových scenárov, počet platných hodnotení a rozdelenie záznamov podľa prítomnosti štruktúrujúceho klinického usmernenia a štýlu odpovedania simulovaného pacienta. Pri kompozitoch s približne intervalovým charakterom budú doplnené aj histogramy a boxploty, aby bolo možné orientačne posúdiť distribúciu a prítomnosť odľahlých hodnôt.

Pred frekvenčnou a reliabilitnou analýzou hlavných hodnotení je v práci stručne zhrnutá aj **pilotná expertná obsahová kontrola** položiek a východiskových scenárov. Reportovaný je počet expertov, počet posúdených položiek a východiskových scenárov, položkové priemery a podiely hodnotení `3-4` pri položkách dotazníka, pri východiskových scenároch aj zhoda medzi zamýšľanou a expertne vnímanou závažnosťou a najčastejšie typy pripomienok. Ako upozorňuje @polit2007cvi, pri malom expertnom paneli však tieto ukazovatele slúžia len ako pomocná opora pre rozhodnutia o úpravách, nie ako samostatný dôkaz validity.

#### 2.8.3 Analýza vnútornej konzistencie

V súlade s odporúčaniami sprievodcu, s logikou COSMIN obsahovej validity podľa @terwee2018COSMINMethodologyEvaluating a s metodickým rámcom pre prácu s Cronbachovou alfou, ktorý sumarizuje @marko2016VyuzitieZneuzitieCronbachovej, bola zaradená aj **analýza vnútornej konzistencie** meracieho nástroja, najmä pre blok G1 až G5, pre blok indexu klinickej vierohodnosti (G1, G3, G4) a pre blok R1 až R5. Keďže ide o autorský hodnotiaci nástroj, táto časť je dôležitá pre posúdenie, či sa položky reprezentujúce spoločný konštrukt správajú dostatočne konzistentne. Výsledky budú prezentované úsporne a zrozumiteľne, nie ako séria samostatných neprehľadných tabuliek.

#### 2.8.4 Zhoda medzi hodnotiteľmi

**Zhoda medzi hodnotiteľmi** bola vyhodnocovaná prostredníctvom **koeficientu vnútrotriednej korelácie (ICC)** pre agregované ukazovatele indexu klinickej vierohodnosti, indexu defektov a pre expertne hodnotené položky závažnosti a funkčného dopadu. PHQ-9 symptomatické metadata A1 až A9 na úrovni prepisu rozhovoru do ICC bloku nevstupujú, keďže nejde o opakované ľudské hodnotenia toho istého objektu, ale o vlastnosť samotného prepisu rozhovoru. Primárne bude reportovaný **ICC2k**, teda dvojcestný model s náhodnými efektmi pre priemerné merania a absolútnu zhodu; pri malom alebo nevyváženom paneli však bude tento blok interpretovaný opatrne a vždy spolu s deskriptívnou zhodou jadrovej dvojice hodnotiteľov, čo odporúčajú aj @mchugh2012InterraterReliabilityKappa a @nelson2015manyratersordinal. Ak pre niektorý výstupný ukazovateľ nebude matica prepis rozhovoru × hodnotiteľ dostatočne plná na reportovateľný ICC odhad, ukazovateľ ostane v tejto vrstve len ako pilotná meracia informácia a nebude použitý ako jediný nosný argument kvality merania.

#### 2.8.5 Inferenčná analýza

Keďže jedno hodnotenie bolo viazané na konkrétneho hodnotiteľa aj na konkrétny východiskový scenár, pri hlavných analýzach boli použité **zmiešané modely**, ktoré umožňujú zohľadniť rozdiely medzi hodnotiteľmi a scenármi. Hlavná inferenčná analýza má v tejto práci **komparačný charakter** a v technickom vyjadrení modeluje fixné efekty experimentálnych faktorov spolu s náhodnou variabilitou medzi hodnotiteľmi a východiskovými scenármi, čo je pri opakovaných a zhlukovaných meraniach metodicky vhodný postup, ako ukazuje @hedeker2016MixedeffectsLocationScaleModel. Jadro analytickej línie preto netvoria jednoduché dvojskupinové testy ani plošné korelačné analýzy, ale porovnanie experimentálnych podmienok cez spoločný modelový rámec.

Na čitateľskej úrovni je dôležité odlíšiť, **čo sa v modeli priamo interpretuje** a **čo sa v modeli zohľadňuje ako zdroj variability**. V tejto práci sú ako **fixné efekty** zaradené obe experimentálne premenné, teda prítomnosť štruktúrujúceho klinického usmernenia a štýl odpovedania simulovaného pacienta, spolu s ich interakciou. Ako **náhodné efekty** vstupujú zdroje variability, ktoré nie sú samostatným predmetom hypotetického záujmu, ale môžu posúvať priemernú úroveň hodnotení medzi prípadmi alebo medzi hodnotiteľmi.

**Tabuľka 2**  
*Fixné a náhodné efekty v hlavných modeloch*

| Prvok modelu | Typ | Funkcia v interpretácii |
| --- | --- | --- |
| klinické usmernenie (`guardrail`) | fixný efekt | ukazuje rozdiel medzi podmienkou `G1` a `G0` |
| štýl odpovedania (`profile`) | fixný efekt | ukazuje rozdiel medzi `P1`, `P2` a `P3` |
| interakcia `guardrail × profile` | fixný efekt | ukazuje, či sa efekt usmernenia mení podľa profilu odpovedania |
| východiskový scenár (`seed_id`) | náhodný intercept | zohľadňuje, že niektoré prípady môžu byť celkovo ľahšie alebo ťažšie hodnotené |
| hodnotiteľ (`rater_id`) | náhodný intercept | zohľadňuje, že niektorí hodnotitelia môžu byť prísnejší alebo miernejší |

Pre kompozitné ukazovatele a ukazovatele odchýlky sú plánované **lineárne zmiešané modely**. Pri ukazovateľoch na úrovni jednotlivých hodnotení má základný model tvar `outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)`. To znamená, že výslednú hodnotu vysvetľujeme oboma experimentálnymi faktormi a ich interakciou, pričom zároveň dovoľujeme, aby sa priemerná úroveň sledovaného ukazovateľa líšila medzi východiskovými scenármi a medzi hodnotiteľmi.

Pri vetve ukazovateľov odchýlky na úrovni prepisu rozhovoru (`symptom_error_mean`, `severity_error`, `impact_error`) sa najprv vytvorí jeden sumarizačný riadok na prepis rozhovoru a následne sa používa model na úrovni prepisu rozhovoru `outcome ~ guardrail * profile + (1 | seed_id)`. Tento krok je metodicky dôležitý najmä pri anchor-fidelity vetve, pretože položky `A1` až `A9` predstavujú metadata na úrovni prepisu rozhovoru a odvodené chybové ukazovatele nemajú byť vážené podľa počtu dostupných hodnotení toho istého prepisu rozhovoru.

Referenčnou úrovňou bola kombinácia **bez štruktúrujúceho klinického usmernenia a štýl P1**. Intercept preto predstavuje odhad pre bunku `G0 × P1`. Koeficient pre klinické usmernenie ukazuje rozdiel `G1` oproti `G0` pri profile `P1`; koeficienty pre `P2` a `P3` ukazujú rozdiely oproti `P1` v podmienke `G0`; interakčné členy ukazujú, o koľko sa efekt usmernenia v profile `P2` alebo `P3` mení oproti referenčnému profilu `P1`. Keďže interakčný model sa číta menej intuitívne než jednoduchý dvojskupinový rozdiel, vo Výsledkoch preto popri koeficientoch interpretujem aj **odhadované marginálne priemery** pre jednotlivé bunky `G0/G1 × P1/P2/P3`. Podrobnejší technický preklad týchto modelov uvádza Príloha B.

Pri lineárnych zmiešaných modeloch budú popri odhadoch koeficientov a Waldových 95 % intervaloch spoľahlivosti reportované aj p-hodnoty odvodené pomocou balíka `lmerTest` so Satterthwaite aproximáciou stupňov voľnosti. Súčasťou interného exportu budú aj stručné diagnostické poznámky k singularite alebo konvergencii modelu tam, kde sa vyskytnú.

Ako doplnkové overenie robustnosti bude pri kompozitoch na úrovni jednotlivých hodnotení (najmä index klinickej vierohodnosti a index defektov) overený aj senzitívny model s dodatočným náhodným interceptom pre konkrétny prepis rozhovoru. Táto vetva nebude chápaná ako náhrada hlavného modelu, ale ako kontrola, či sa po explicitnom zohľadnení variability medzi prepismi rozhovorov nemení smer a hrubá interpretácia hlavných efektov.

Tento model je použitý pre premenné:

- index klinickej vierohodnosti (H1, H6, časť H9),
- index defektov (H3, časť H9),
- expertne hodnotená závažnosť ako ordinálny výstupný ukazovateľ a jej ukazovateľ chyby na úrovni prepisu rozhovoru (H4, časť H9),
- expertne hodnotený funkčný dopad ako ordinálny výstupný ukazovateľ a jeho ukazovateľ chyby na úrovni prepisu rozhovoru (H4, časť H9).

Pre jednotlivé ordinálne položky, najmä G2 (H2, H7), G5 (H5, H7) a položku zachytávajúcu istotu odhadu pôvodu rozhovoru, sú plánované **ordinálne zmiešané modely kumulatívneho typu**, ktorých rámec rozpracúva @christensenCumulativeLinkModels. Tento prístup je vhodný pri viacúrovňových ordinálnych dátach, ktoré sú zhlukované alebo opakovane merané. Na úrovni položiek bude použitý selektívne: pri G2 a G5 ako priamo hypotetizovaných výstupných ukazovateľoch a pri ďalších položkách len vtedy, ak bude potrebné spresniť interpretáciu kompozitného výsledku.

Pri faktore štýlu odpovedania simulovaného pacienta budú vopred uprednostnené **plánované kontrasty**, najmä kontrast rozvinutého štýlu odpovedania voči zdržanlivejšiemu štýlu (P3 vs. P1). Kontrasty P2 vs. P1 a P3 vs. P2 budú považované za sekundárne a budú reportované najmä vtedy, ak zmysluplne doplnia interpretáciu hlavného efektu. Ak sa pri niektorom výstupnom ukazovateli preukáže interakcia medzi prítomnosťou štruktúrujúceho klinického usmernenia a štýlom odpovedania simulovaného pacienta, budú nasledovať **analýzy jednoduchých efektov** v jednotlivých úrovniach profilu alebo usmernenia, nie plošné párové porovnania všetkých kombinácií.

Z hľadiska väzby na výskumné otázky a hypotézy platí nasledovné: modely pre index klinickej vierohodnosti, G2 a G5 odpovedajú na jadro VO1 a zároveň testujú H1, H2 a H5; symptomatická zhoda na úrovni prepisu rozhovoru odvodená z A1 až A9 poskytuje primárnu kvantitatívnu oporu pre H4 a H8 na úrovni samotných prepisov rozhovorov; expertne hodnotené položky závažnosti a funkčného dopadu dopĺňajú VO2 a VO4 ako samostatná ľudská vrstva; hlavné efekty štýlu odpovedania simulovaného pacienta nad indexom klinickej vierohodnosti, G2, G5, expertne hodnotenou závažnosťou, expertne hodnoteným funkčným dopadom a indexom defektov odpovedajú na VO3 a VO4 a pokrývajú H6 až H8; interakčné členy oboch faktorov odpovedajú na VO5 a testujú H9. VO6 je riešená samostatným blokom ICC a VO7 až VO8 samostatným exploračným blokom.

#### 2.8.6 Explorácia doplnkových premenných

Exploratórne je plánovaná aj **analýza položky odhadovaného pôvodu rozhovoru**, najmä pomocou frekvenčného rozdelenia odpovedí a prípadne logistického modelu nad binarizovanou premennou „vnímané ako AI vs. nie AI". Otvorené komentáre budú analyzované **kvalitatívne prostredníctvom stručného tematického kódovania** s cieľom doplniť kvantitatívne výsledky o typické dôvody pozitívneho alebo negatívneho hodnotenia. Cieľom tejto analýzy nie je vytvoriť samostatnú kvalitatívnu líniu práce, ale stručne pomenovať opakujúce sa dôvody pozitívneho a negatívneho hodnotenia, ktoré pomôžu interpretovať kvantitatívne výsledky.

Popri tom je plánovaná aj **doplnková korelačná analýza na úrovni prepisu rozhovoru** hlavných kompozitných ukazovateľov. Keďže korelačná matica nemá v tejto práci nahrádzať jadrové komparačné modely, bude počítaná až na úrovni agregovaných priemerov za jednotlivé prepisy rozhovorov, nie na úrovni každého jednotlivého riadku hodnotenia. Primárne pôjde o Spearmanove korelácie medzi indexom klinickej vierohodnosti, indexom defektov, symptomatickou zhodou na úrovni prepisu rozhovoru odvodenou z A1 až A9, prirodzenosťou jazyka a tréningovou použiteľnosťou. Funkciou tejto analýzy je stručne ukázať, či rozhovory, ktoré pôsobia vierohodnejšie a prirodzenejšie, bývajú zároveň hodnotené ako použiteľnejšie, menej defektné a symptomaticky bližšie k cieľovému profilu východiskového scenára.

Ako doplnková exploratórna analýza bola pripravená aj typológia prepisov rozhovorov pomocou metódy partitioning around medoids (PAM). Táto analýza bola realizovaná výlučne na agregovaných ukazovateľoch na úrovni prepisu rozhovoru, aby sa predišlo nadhodnoteniu informácie cez viacnásobné hodnotenia toho istého prepisu rozhovoru. PAM nebol použitý na testovanie hypotéz H1 až H9, ale iba ako orientačný spôsob, ako opísať, či sa v dátach črtajú opakujúce sa profily rozhovorov. Podrobnejšie korelačné a PAM výstupy sú preto uvedené len v Prílohe D.

#### 2.8.7 Interpretácia efektov

Keďže ide o pilotnú štúdiu s potenciálne limitovaným počtom hodnotiteľov, inferenčné výsledky budú interpretované **opatrne a s dôrazom na smer a veľkosť efektov, nie iba na dichotomické rozhodovanie podľa hladiny štatistickej významnosti**. Ako odporúčajú @sim2019ShouldTreatmentEffects, @soukup2013SubstantiveSignificanceIts a @cohen1988StatisticalPowerAnalysis, vo Výsledkoch a Diskusii sa preto popri p-hodnotách budú uvádzať aj odhady efektov, intervaly spoľahlivosti a vecná významnosť rozdielov tam, kde je to možné. Lokálny sprievodca pritom priamo odporúča, aby kvalita výsledkovej časti nestála len na testovaní významnosti, ale aj na primeranej deskriptívnej a inferenčnej logike vrátane vecnej významnosti.

Analýzy, ktoré priamo neodpovedajú na H1 až H9, budú v kapitole Výsledky explicitne označené ako doplnkové alebo exploratórne, aby sa neporušila logická väzba medzi cieľom, hypotézami a poradím prezentácie výsledkov. To sa týka najmä korelácií na úrovni prepisu rozhovoru a PAM typológie prepisov rozhovorov, ktoré môžu pomôcť lepšie opísať štruktúru dát, ale nemajú byť interpretované ako rovnocenná alternatíva ku konfirmačným zmiešaným modelom.

### 2.9 Etické aspekty

Výskum nepracoval s reálnymi pacientskymi údajmi ani s reálnymi klinickými rozhovormi. Hodnotený materiál tvorili **simulované textové prepisy rozhovorov** vytvorené na základe vopred pripravených východiskových scenárov, takže riziko pre účastníkov bolo nízke a riziko zneužitia identifikovateľných pacientskych údajov bolo z podstaty dizajnu vylúčené. Napriek tomu boli rešpektované základné etické princípy psychologického výskumu, najmä **informovanosť hodnotiteľov** o charaktere úlohy, **dobrovoľnosť účasti**, **možnosť kedykoľvek ukončiť účasť** a **ochrana identifikačných údajov hodnotiteľov** pri spracovaní odpovedí.

Súčasne je dôležité zdôrazniť, že výskum nebol koncipovaný ako diagnostický nástroj a jeho zistenia nemajú slúžiť na bezprostredné klinické rozhodovanie. Tento rámec je v práci zachovávaný konzistentne od Úvodu cez Metódu až po Diskusiu a je v súlade so širším etickým rámcom WHO pre použitie LLM v zdravotníctve, ktorý formulujú @who2021ethicsaiforhealth a @who2024lmmguidance.

Rozsah podporného použitia generatívnej AI pri authoringu a technických pomocných úlohách transparentne sumarizuje Príloha H.
