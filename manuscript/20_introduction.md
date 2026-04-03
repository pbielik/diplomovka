# 20 Introduction / Úvod

> Pracovný draft kapitoly. Finálna verzia pôjde do Wordu so živými Zotero citáciami. V markdown verzii používaj citekeys alebo placeholdery typu `[@citekey]`.

## 1 Úvod

### 1.1 Všeobecný úvod do problému

Generatívna umelá inteligencia sa v posledných rokoch postupne presúva z technologického prostredia aj do oblastí, ktoré boli tradične viazané na ľudskú expertízu, medzi ne patrí aj psychológia a psychologická prax [@obradovich2024llmpsychiatry; @meng2024llmmedicine]. Tento posun otvára viacero možností, ale aj metodologických a etických otázok. Popri témach automatizácie, podpory rozhodovania a spracovania textu sa čoraz častejšie objavuje aj otázka, či je možné pomocou generatívnych modelov vytvárať textové simulácie rozhovorov, ktoré by boli použiteľné na tréningové, výučbové alebo výskumné účely [@ajluni2025psychiatriceducation; @yu2025simulatedpatientsystems; @brugge2024patientsimulation].

V psychologickom a klinickom vzdelávaní má práca so štandardizovanými prípadmi dôležité miesto. Študentom, začínajúcim odborníkom aj výskumníkom umožňuje trénovať hodnotenie, formuláciu otázok, rozlišovanie symptomatiky a kritické uvažovanie nad kvalitou rozhovoru bez priameho zásahu do reálnej klinickej situácie [@evans2015vignettes; @williams2017simulationmentalhealth]. Štandardizované prípady, vinety alebo modelové rozhovory však majú aj svoje limity. Ich tvorba je časovo náročná, odborné ukotvenie nemusí byť vždy rovnomerné a opakovane vzniká problém, ako skombinovať štandardizáciu s dostatočnou prirodzenosťou textu či dialógu.

Práve v tomto bode sa javí generatívna AI ako potenciálne zaujímavý nástroj. Na jednej strane môže uľahčiť tvorbu väčšieho množstva simulovaných rozhovorov, variovanie scenárov a prípravu materiálov pre tréning alebo výskum. Na druhej strane vyvoláva pochybnosti, či takéto rozhovory dokážu zachytiť klinicky dôležité črty, či nepôsobia schematicky, neprirodzene alebo symptomaticky nepresne, a či ich odborníci vôbec považujú za metodologicky použiteľné [@roustan2025cliniciansguide; @asgari2025hallucinationframework].

V predkladanej práci sa preto nezameriavam na to, či AI dokáže „diagnostikovať“ depresiu, ani na to, či môže nahradiť odborné klinické rozhodovanie. Predmetom výskumu je omnoho užšie a metodologicky bezpečnejšie formulovaný problém: **akú kvalitu majú AI-generované simulované klinické interview s depresívnou symptomatikou, ak sú hodnotené odborníkmi z psychologickej a príbuznej klinickej praxe**. Objektom skúmania nie sú reálni pacienti ani reálne klinické rozhovory, ale simulované textové transkripty pripravené na základe vopred ukotvených seed scenárov.

Výskumný problém má zároveň vedecký aj praktický význam. Z vedeckého hľadiska reaguje na potrebu systematicky a transparentne skúmať, aké vlastnosti majú AI-generované simulácie v oblasti psychologického obsahu, a nie iba intuitívne alebo anekdoticky hodnotiť, či text „pôsobí dobre“. Z praktického hľadiska môže priniesť odpoveď na otázku, či a za akých podmienok možno takéto rozhovory využívať pri výučbe, tréningu, pilotovaní metodík alebo ďalšom výskume.

### 1.2 Prehľad literatúry

#### 1.2.1 Depresívna symptomatika ako rámec simulovaného interview

Depresívna symptomatika patrí medzi najčastejšie skúmané oblasti psychopatológie a zároveň predstavuje tematicky citlivý priestor, v ktorom je vierohodnosť rozhovoru obzvlášť dôležitá [@kennedy2008coresymptoms; @maj2020depressioncharacterization]. Ak má byť simulované interview použiteľné, nestačí, aby obsahovalo niekoľko izolovaných znakov smútku alebo únavy. Musí vytvárať ucelený, vnútorne konzistentný a klinicky zmysluplný obraz symptomatiky, ktorý bude zodpovedať tomu, ako sa depresívne prežívanie a fungovanie typicky prejavuje v rozhovore.

V tejto práci je klinický obraz depresívnej symptomatiky operacionalizovaný prostredníctvom deviatich obsahových oblastí: depresívna nálada, strata záujmu alebo anhedónia, poruchy spánku, zmeny apetítu alebo hmotnosti, psychomotorické zmeny, únava alebo nízka energia, pocity viny alebo bezcennosti, zhoršená koncentrácia alebo rozhodovanie a pasívne myšlienky na smrť. Tieto oblasti slúžia ako symptomatické kotvy seed scenárov a zároveň ako rámec odborného hodnotenia [@kroenke2001phq9; @kennedy2008coresymptoms].

Pri simulovanom rozhovore však nie je dôležitá len samotná prítomnosť symptómov. Rovnako dôležitý je ich kontext, spôsob disclosure, miera funkčného dopadu, vzájomná previaznutosť a súlad medzi tým, čo postava hovorí, ako to hovorí a aký celkový obraz vzniká [@guidi2011clinicalinterviewdepression; @maj2020depressioncharacterization]. Inými slovami, klinická vierohodnosť nie je jednoduchým súčtom symptómov, ale výsledkom ich obsahovej, naratívnej a komunikačnej integrácie.

#### 1.2.2 Štandardizované prípady, vinety a simulácie vo výskume a výučbe

Vo vzdelávaní a vo výskume sa už dlhšie využívajú rôzne formy štandardizovaných prípadov, viniet a modelových scenárov [@evans2015vignettes; @baguley2022vignettedata]. Ich výhodou je možnosť kontrolovať obsah, porovnávať reakcie hodnotiteľov na rovnaký materiál a pracovať s eticky menej rizikovým vstupom než pri reálnych klinických dátach. Zároveň však štandardizácia často vedie k zjednodušeniu, neprirodzenosti alebo k tomu, že materiál pôsobí skôr ako didaktický text než ako živý rozhovor.

Preto je dôležité rozlišovať medzi tým, či je prípad iba obsahovo správny, a tým, či pôsobí ako skutočný dialóg. Pre výučbové účely nemusí byť vždy postačujúce, ak text obsahuje „správne symptómy“. Ak má slúžiť na trénovanie citlivosti na jazyk, otázky, odpovede a celkový tok rozhovoru, musí byť zároveň dostatočne prirodzený a konzistentný [@williams2017simulationmentalhealth; @dawood2024standardizedpatient].

Generatívna AI môže v tomto kontexte priniesť výhodu v schopnosti rýchlo vytvárať viacero variantov toho istého klinického jadra. Na druhej strane však práve táto variabilita môže zvyšovať riziko driftu, klišé alebo narušenia symptomatickej presnosti. Preto je potrebné skúmať nielen výstup ako taký, ale aj to, **aké vlastnosti generovania vedú ku kvalitnejšiemu alebo menej kvalitnému výsledku**.

#### 1.2.3 Generatívna AI a simulácia dialógu

Veľké jazykové modely preukázali vysokú schopnosť generovať súvislý, plynulý a štylisticky presvedčivý text [@meng2024llmmedicine; @yu2025simulatedpatientsystems]. V aplikačnom kontexte to vytvorilo predstavu, že by mohli byť využiteľné aj na simuláciu klientskych odpovedí, modelových rozhovorov alebo tréningových situácií. Problémom však zostáva, že jazyková plynulosť sama osebe negarantuje klinickú správnosť, konzistentnosť ani adekvátny psychologický obsah [@roustan2025cliniciansguide; @asgari2025hallucinationframework].

Z metodologického hľadiska je preto dôležité odlíšiť dva typy kvality. Prvý typ možno označiť ako **povrchová jazyková kvalita**, teda to, či text znie prirodzene, plynulo a bez zjavne strojových formulácií. Druhý typ predstavuje **klinická obsahová kvalita**, teda to, či rozhovor zodpovedá symptomatickému obrazu, nevykazuje významné kontradikcie a nepôsobí tak, že smeruje k inej psychopatológii alebo k neprimeranej dramatizácii. V oblasti psychologickej simulácie je druhý typ kvality minimálne rovnako dôležitý ako prvý.

Doterajšia literatúra tak vytvára pomerne jasný rámec, ale zároveň necháva otvorenú konkrétnu metodologickú medzeru. Vieme, že štandardizované prípady a simulácie sú vo výučbe a vo výskume užitočné [@evans2015vignettes; @williams2017simulationmentalhealth], vieme aj to, že veľké jazykové modely dokážu generovať plynulý text [@meng2024llmmedicine; @yu2025simulatedpatientsystems], no podstatne menej vieme o tom, ako odborníci hodnotia **klinickú kvalitu kontrolovane generovaných, symptomaticky anchorovaných AI rozhovorov** a či sa táto kvalita mení v závislosti od konkrétneho nastavenia generovania. Práve na túto medzeru reaguje predkladaná práca.

#### 1.2.4 Potreba metodologicky ukotveného hodnotenia

Ak chceme AI-generované interview skúmať zmysluplne, nestačí vyhodnotiť, či odborníkovi text „pripadá dobrý“. Potrebujeme štruktúrované dimenzie hodnotenia. V tejto práci sú jadrom hodnotenia tri vrstvy:

1. **primárna kvalitatívna vrstva**, zahŕňajúca klinickú vierohodnosť, prirodzenosť jazyka, vnútornú konzistentnosť, súlad s obrazom depresívnej symptomatiky a tréningovú použiteľnosť,
2. **symptom fidelity vrstva**, ktorá porovnáva rating s vopred definovanými seed anchorami v oblastiach A1–A9, závažnosti a funkčného dopadu,
3. **QC a defect vrstva**, ktorá zachytáva kontradikcie, klišé, nesúlad symptomatiky a kontextu, podozrenie na inú psychopatológiu a neprimeranú expresivitu.

Takto koncipované hodnotenie umožňuje posudzovať AI-generované rozhovory nielen ako jazykový produkt, ale ako metodicky kontrolovaný psychologický materiál. Zároveň vytvára priestor pre analytické porovnanie rôznych variantov generovania.

### 1.3 Pojmový rámec výskumného problému

V tejto práci je kľúčovým pojmom **klinická vierohodnosť rozhovoru**. Týmto pojmom označujem mieru, do akej rozhovor vytvára presvedčivý obraz simulovanej osoby s depresívnou symptomatikou tak, aby bol odborne akceptovateľný ako modelový prípad. Klinická vierohodnosť preto zahŕňa nielen prítomnosť symptómov, ale aj ich vzájomnú logiku, spôsob komunikácie a konzistentnosť v rámci celého dialógu.

Druhým dôležitým pojmom je **prirodzenosť jazyka a štýlu odpovedí**. Ide o mieru, do akej odpovede nepôsobia strojovo, klišéovito alebo príliš didakticky, ale pripomínajú reálnu reč človeka v rozhovorovej situácii. Prirodzenosť sa však v tejto práci nechápe ako samoúčelný cieľ. Je dôležitá najmä preto, že ovplyvňuje tréningovú použiteľnosť a celkovú dôveryhodnosť transkriptu.

Tretím pojmom je **vnútorná konzistentnosť rozhovoru**, teda súlad medzi jednotlivými odpoveďami, symptomatickými tvrdeniami a kontextom. Rozhovor môže obsahovať klinicky správne prvky, no ak sa v ňom objavujú zjavné kontradikcie alebo nepomer medzi symptomatikou a naratívnym rámcom, jeho využiteľnosť klesá.

Štvrtým dôležitým pojmom je **symptom fidelity**, teda zhoda hodnoteného rozhovoru s vopred definovaným seed profilom. V tejto práci ide o kľúčové premostenie medzi generovaným textom a metodologickou kontrolou. Rozhovor teda nie je posudzovaný len podľa dojmu, ale aj podľa toho, či jeho symptomatický profil zodpovedá cieľovým anchorom v oblastiach A1–A9, závažnosti a funkčného dopadu.

Napokon zavádzam aj pojem **defect alebo red-flag dimenzia**, ktorým označujem súbor vlastností znižujúcich kvalitu rozhovoru. Patria sem vnútorné kontradikcie, klišé, nesúlad kontextu a symptomatiky, podozrenie na inú primárnu psychopatológiu a neprimeraná dramatizácia. Táto dimenzia je dôležitá preto, že umožňuje zachytiť kvalitu negatívne, teda cez typické zlyhania simulácie.

Osobitne dôležitým pojmom je aj **tréningová a výučbová použiteľnosť** rozhovoru. Týmto pojmom označujem mieru, do akej možno transkript rozumne použiť ako modelový materiál pri výučbe, tréningu interview alebo pri pilotovaní metodiky. Rozhovor môže byť jazykovo plynulý, ale ak nie je klinicky logický alebo symptomaticky ukotvený, jeho tréningová hodnota ostáva limitovaná.

Tieto pojmy spolu vytvárajú premostenie medzi teoretickým problémom a empirickými outcome-mi práce. V ďalších kapitolách sú preto systematicky preložené do položiek ratingového nástroja, kompozitných indexov a hypotéz `H1-H6`.

### 1.4 Cieľ práce

Hlavným cieľom diplomovej práce je **pilotne metodologicky overiť kvalitu AI-generovaných simulovaných klinických interview s depresívnou symptomatikou prostredníctvom odborného human-rated hodnotenia a preskúmať, či sa hodnotená kvalita mení v závislosti od experimentálne manipulovaných vlastností generovania rozhovoru**.

Sekundárnymi cieľmi práce sú:
- overiť, do akej miery rozhovory zodpovedajú cieľovým seed anchorom v symptomatických doménach A1–A9,
- preskúmať, či sa odhad závažnosti a funkčného dopadu približuje cieľovému seed profilu,
- zachytiť výskyt červených vlajok a defektov v rozhovoroch,
- preskúmať, či sú rozhovory vnímané ako použiteľné na tréningové alebo výučbové účely,
- preskúmať, či vyššia plausibilita a nižšia miera defektov súvisia s tým, ako hodnotitelia odhadujú pôvod rozhovoru.

### 1.5 Výskumné otázky a hypotézy

Na úrovni výskumného problému sa práca opiera o dve hlavné otázky:

- Do akej miery sú AI-generované simulované klinické interview s depresívnou symptomatikou odbornými hodnotiteľmi vnímané ako klinicky vierohodné, prirodzené, vnútorne konzistentné, symptomaticky ukotvené a tréningovo použiteľné?
- Menia sa tieto hodnotenia v závislosti od prítomnosti guardrailu a od realizačného profilu odpovedí?

Tieto všeobecné otázky sú ďalej rozpracované do konkrétnych hypotéz. Ich poradie zodpovedá logike, v akej budú následne riešené vo výsledkoch:

**H1.** Rozhovory generované s aktívnym guardrailom budú hodnotené vyššie v klinickej plausibilite než rozhovory bez guardrailu, a to na úrovni `plausibility_index` aj položiek `G1`, `G3` a `G4`.

**H2.** Rozhovory generované s aktívnym guardrailom budú vykazovať nižšiu mieru defektov než rozhovory bez guardrailu, a to na úrovni `defect_index` aj položiek `R1–R5`.

**H3.** Rozvinutejší realizačný profil `R3` bude spojený s vyššou prirodzenosťou jazyka a štýlu odpovedí než profily `R1` a `R2`, a to najmä na položke `G2`.

**H4.** Medzi guardrailom a realizačným profilom bude interakčný efekt tak, že priaznivý efekt guardrailu na klinickú plausibilitu a zníženie defektov bude výraznejší pri profile `R3` než pri profiloch `R1` a `R2`.

**H5.** Rozhovory generované s aktívnym guardrailom budú presnejšie zodpovedať seed anchorom, teda budú mať nižšiu priemernú absolútnu chybu v oblastiach `A1–A9`, `S1` a `S2` než rozhovory bez guardrailu.

**H6.** Vyššia klinická plausibilita a nižšia miera defektov budú spojené s vyššou tréningovou použiteľnosťou rozhovoru a s nižšou pravdepodobnosťou, že bude rozhovor označený ako `ai_generated`.

### 1.6 Prechod k metodickej časti

Úvodná časť práce ukázala, že problematika AI-generovaných simulovaných interview s depresívnou symptomatikou si vyžaduje metodologicky ukotvené hodnotenie, ktoré kombinuje jazykovú, klinickú a experimentálnu perspektívu. V nasledujúcej kapitole preto uvádzam výskumný dizajn, výber hodnotiteľov, opis stimulusového materiálu, ratingového nástroja a analytických postupov použitých na overenie formulovaných hypotéz.
