# 2026-04-08 - Zapracovanie vzdelávacieho framingu práce

## Jadro usmernenia od školiteľky

Praktický framing práce má byť posunutý tak, aby sa hlavný prínos diplomovky nečítal iba ako metodologické hodnotenie AI simulácií, ale aj ako **príspevok k vzdelávaniu študentov psychologických smerov**. Jadrová myšlienka:

- študenti nemajú vždy dostatočne široký a opakovateľný prístup k reálnym klinickým pacientom,
- simulácie môžu vytvoriť bezpečné, kontrolované a škálovateľné prostredie na nácvik interview,
- textové simulácie sú prvý krok; dlhodobejšie rozšírenie môže smerovať k `voice`, `video` a k ďalším poruchám,
- simulácie sa majú rámcovať ako **doplnok a most k výcviku**, nie ako náhrada reálneho kontaktu s pacientom.

## Ako to zapracovať do IMRaD logiky

### Úvod

`manuscript/20_introduction.md`

1. `1.2 Klinický rozhovor a simulovaní pacienti v psychologickom a psychiatrickom vzdelávaní`
   - Posilniť vetu, že didaktická hodnota simulácií nespočíva len v bezpečnosti a štandardizácii, ale aj v tom, že umožňujú opakovaný tréning tam, kde je prístup k reálnym klinickým situáciám limitovaný.
   - Doplniť jasný most:
     - reálne placementy a klinická prax sú v zahraničí štandardom najmä v profesionálne orientovaných programoch,
     - takáto skúsenosť však nie je kapacitne dostupná pre všetkých študentov ani vo všetkých kontextoch,
     - preto majú simulovaní pacienti legitímnu didaktickú funkciu.

2. `1.3 Veľké jazykové modely a nová generácia simulovaných pacientov`
   - Doplniť, že LLM posúvajú simulácie od statických scenárov k opakovateľnému interaktívnemu tréningu.
   - Explicitne pomenovať, že to je dôležité pre výučbu klinického rozhovoru, nie iba pre technologický vývoj.

3. `1.6 Výskumná medzera a prínos práce`
   - Rozšíriť praktický prínos takto:
     - práca nepovie, či AI „vie robiť psychológa“,
     - ale pomáha určiť, aké vlastnosti musí mať simulovaný rozhovor, aby bol odborníkmi považovaný za použiteľný vo výučbe a tréningu.
   - Tu je vhodné explicitne uviesť, že ide o **metodologický predstupeň budúceho vzdelávacieho nasadenia**.

4. `1.7 Cieľ práce`
   - Hlavný cieľ netreba prepisovať radikálne.
   - Stačí jemne zvýrazniť, že premenná tréningovej a výučbovej použiteľnosti (`G5`) nie je okrajová, ale tvorí most medzi metodologickým výsledkom a praktickým využitím v psychologickom vzdelávaní.

### Diskusia

`manuscript/50_discussion.md`

1. `4.4 Tréningová použiteľnosť a vnímaný pôvod rozhovoru`
   - Toto je prirodzené miesto pre hlavnú praktickú interpretáciu.
   - Doplniť, čo znamená vysoká alebo nízka tréningová použiteľnosť pre výučbu študentov:
     - nácvik vedenia interview,
     - nácvik rozpoznávania symptomatiky,
     - nácvik citlivého dopytovania,
     - nácvik práce s menej ochotným alebo menej koherentným klientom.

2. `4.7 Praktické a metodologické dôsledky`
   - Rozšíriť o samostatný odsek k psychologickému vzdelávaniu.
   - Navrhovaná logika:
     - simulácie nevylučujú živú prax,
     - ale môžu znižovať vstupnú bariéru pred prvým kontaktom s klientom,
     - môžu štandardizovať výučbu naprieč rôznou kvalitou lokálnych podmienok,
     - môžu slúžiť na opakovanie zriedkavejších alebo citlivých situácií.

3. `4.8 Odporúčania pre ďalší výskum`
   - Sem patrí roadmap:
     - multimodalita (`voice`, `video`, nonverbálne signály),
     - ďalšie diagnostické okruhy,
     - porovnanie text-only a multimodálnych simulácií,
     - testovanie efektu na reálne študentské učenie, nie iba na expert rating výstupov.

### Záver a obhajoba

`manuscript/60_conclusion.md` a prezentácia

- V závere mať jednu veľmi čistú vetu:
  - práca vytvára podklad pre využitie AI simulovaných pacientov vo výučbe psychologického interview.
- V prezentácii a na obhajobe to má byť jeden z hlavných bodov praktického prínosu.
- Formulácia má byť opatrná:
  - nejde o náhradu klinickej praxe,
  - ide o dostupný, opakovateľný a kontrolovateľný doplnok výcviku.

## Hlavná línia argumentu pre obhajobu

1. Reálna klinická skúsenosť je pre výcvik dôležitá, ale nie je neobmedzene dostupná.
2. Zahraničné programy to riešia kombináciou placementov, univerzitných kliník a simulácií.
3. Simulácie majú najväčší zmysel vtedy, keď sú dostatočne klinicky vierohodné a pedagogicky použiteľné.
4. Predkladaná práca presne toto testuje: či odborníci považujú AI-generované rozhovory za vierohodné, konzistentné a použiteľné na tréning.
5. Praktický prínos práce pre psychológiu teda spočíva v tom, že pomáha určiť podmienky, za ktorých môžu byť takéto simulácie rozumne nasadené vo vzdelávaní.

## Ak sa komisia spýta na `CVI`, Delphi alebo autorský nástroj

Toto je pravdepodobne jedna z prirodzených metodických otázok. Bezpečná línia odpovede je:

- nepoužívam autorský nástroj preto, že by som chcel obísť štandardné metodické postupy,
- používam ho preto, že hodnotím veľmi špecifický objekt: kvalitu `AI`-generovaného simulovaného klinického rozhovoru,
- na tento presný účel som nemal k dispozícii hotový validovaný nástroj, ktorý by súčasne pokrýval klinickú vierohodnosť, prirodzenosť, konzistentnosť, symptomatickú primeranosť, tréningovú použiteľnosť a defekty,
- `CVI` logiku som neodmietol; použil som ju v podobe predbežnej expertnej obsahovej kontroly položiek a seed scenárov,
- `CVI` však samo osebe nestačí na hlavný cieľ práce, pretože rieši najmä obsahovú primeranosť položiek, nie neskoršie psychometrické správanie nástroja v dátach ani efekt experimentálnych faktorov.

### Krátka verzia odpovede

> Autorský nástroj som nepoužil preto, že by som nechcel štandardnú validáciu, ale preto, že skúmaný objekt je špecifický a hotový nástroj pre hodnotenie kvality AI simulovaného klinického rozhovoru som nemal k dispozícii. `CVI` alebo podobné expert-panelové prístupy sú vhodné pre obsahovú kontrolu položiek a scenárov, a práve v tejto vrstve som ich logiku aj využil. Hlavné výskumné otázky však vyžadovali aj analýzu vnútornej konzistencie, zhody medzi hodnotiteľmi a modelovanie efektu `guardrail` a štýlu odpovedania, takže `CVI` nemohlo byť jediným nosným metodickým rámcom.

### Vecné jadro odpovede

1. `Prečo nie hotový nástroj`
   - V práci sa nehodnotí depresia ako taká ani bežný screening.
   - Hodnotí sa kvalita simulovaného rozhovoru ako špecifický výskumný artefakt.
   - Potreboval som preto rámec, ktorý pokrýva viac vrstiev naraz: `G1-G5`, `S1-S2` a `R1-R5`.

2. `Prečo nestačí CVI`
   - `CVI` je dobré na otázku, či sú položky relevantné a zrozumiteľné.
   - Nie je to však odpoveď na otázku, ako sa nástroj správa po nasadení do ratingovej štúdie.
   - Samotné `CVI` nepovie, či sa položky správajú konzistentne, či sa experti zhodujú a či experimentálne manipulácie menia výsledok.

3. `Čo som teda urobil namiesto toho`
   - Najprv prebehla predbežná expertná obsahová kontrola položiek a seed scenárov.
   - Potom som v ostrých dátach sledoval vnútornú konzistenciu, `ICC` a mixed-model analytickú vetvu.
   - Teda: obsahová kalibrácia najprv, psychometrické a inferenčné overovanie potom.

4. `Prečo nehovorím o plnej validácii`
   - Expert panel mal `n = 6`, takže číselné ukazovatele obsahovej validity treba čítať opatrne.
   - Preto túto vrstvu neprezentujem ako definitívnu psychometrickú validáciu ani ako formálny Delphi proces.
   - Bezpečnejšie a presnejšie pomenovanie je predbežná expertná obsahová kontrola alebo pilotný expert review pass.

### Jedna veta, ak bude treba úplne stručnú reakciu

> `CVI` by bolo vhodné pre obsahovú validitu položiek, ale nie ako jediný rámec pre celú túto štúdiu; preto som pri autorskom nástroji spojil predbežnú expert review vrstvu s neskorším overovaním cez vnútornú konzistenciu, `ICC` a mixed models.

### Čomu sa pri odpovedi radšej vyhnúť

- nehovoriť, že nástroj je „plne validovaný“,
- netvrdiť, že `CVI` je zlé alebo zastarané,
- netvrdiť, že `Delphi` by bolo nesprávne; presnejšie je povedať, že dizajn tejto práce nebol formálny viac-kolový Delphi proces,
- neprezentovať expert review vrstvu ako hlavný dôkaz kvality celého merania.

### Interná opora v rukopise

- logika expertnej evaluácie a vrstiev kvality je v [20_introduction.md](/Users/pavol.bielik/dev/src/github.com/pbielik/diplomovka/manuscript/20_introduction.md:63),
- status autorského nástroja a dôvod, prečo sa sleduje vnútorná konzistencia a zhoda medzi hodnotiteľmi, je v [30_method.md](/Users/pavol.bielik/dev/src/github.com/pbielik/diplomovka/manuscript/30_method.md:87),
- predbežná expertná obsahová kontrola položiek a seed scenárov je opísaná v [30_method.md](/Users/pavol.bielik/dev/src/github.com/pbielik/diplomovka/manuscript/30_method.md:91),
- opatrný framing pilotného expert review passu je rozpracovaný aj v [expert_content_review_framework.md](/Users/pavol.bielik/dev/src/github.com/pbielik/diplomovka/analysis/expert_content_review_framework.md:9).

## Prečo je to dobré pre psychológiu

### 1. Znižuje to rozdiel medzi teóriou a prvým kontaktom s klientom

Študent sa môže učiť:

- ako viesť rozhovor,
- ako sa pýtať citlivo a neutrálne,
- ako rozpoznať jadro symptomatiky,
- ako zniesť neistotu a nechať klienta hovoriť vlastným tempom.

To je dôležité preto, že veľká časť študentov sa klinicky relevantné interview učí najprv z textov, kazuistík a role-playov, ale nie vždy má široký a opakovateľný kontakt s reálnym pacientom. Simulácia tu vytvára medzikrok medzi teoretickým poznaním a prvou supervidovanou praxou.

### 2. Umožňuje to opakovanie bez etického a organizačného preťaženia

Pri reálnom pacientovi sa nedá:

- ľubovoľne opakovať ten istý prípad,
- štandardizovať mieru disclosure,
- kontrolovať, ktoré symptomatické oblasti sa objavia a v akom poradí,
- lacno vytvoriť desiatky variantov toho istého prípadu.

Simulácia preto nie je cenná len ako náhrada nedostatku praxe, ale aj ako nástroj kontrolovaného tréningu. Psychológia z toho profituje, lebo sa dá cielene trénovať konkrétna interview kompetencia, nie iba všeobecný dojem z rozhovoru.

### 3. Dáva priestor na širšie spektrum prípadov, než bežne stihne výučba

Pri dobre pripravenej platforme možno rýchlo vytvárať:

- rôzne úrovne závažnosti,
- rôzne štýly odpovedania,
- rôzne miery otvorenosti klienta,
- ďalšie diagnostické okruhy.

To je dôležité pre psychológiu, lebo študenti potrebujú vidieť, že rovnaká porucha sa nemusí prejavovať jedným stereotypným spôsobom. Tvoja práca podporuje presne toto: nie statickú kazuistiku, ale variabilnú, no stále klinicky ukotvenú simuláciu.

### 4. Umožňuje bezpečný tréning citlivých situácií

Niektoré témy sú výcvikovo dôležité, ale pedagogicky citlivé:

- pasívne myšlienky na smrť,
- zahanbenie a vina,
- slabšia spolupráca klienta,
- nejasné alebo stručné odpovede.

Simulácia umožňuje tieto situácie trénovať bez toho, aby sa študent hneď učil na reálnom pacientovi v ostrej situácii. Pre psychológiu to znamená bezpečnejší tréningový vstup, nie dehumanizáciu kontaktu.

### 5. Podporuje štandardizáciu výučby

Ak každý študent dostane úplne inú náhodnú skúsenosť, výučba sa hodnotí ťažko. Simulačná platforma umožňuje:

- dať viacerým študentom rovnaké jadro prípadu,
- systematicky meniť iba vybrané premenné,
- porovnávať výkon alebo reflexiu nad porovnateľným materiálom,
- transparentne dokumentovať, aké podmienky boli použité.

To je silný prínos pre psychológiu ako odbor, pretože z výučby robí nielen remeslo, ale aj oblasť, kde sa dá pedagogický materiál metodicky testovať a zlepšovať.

## Prečo je dôležité, že máš platformu a nie len jeden prompt

Tu je tvoja silná stránka. Nevyvíjaš len „AI pacienta“, ale **kontrolovanú simulačnú infraštruktúru**.

### Čo to znamená vecne

Sesterský repozitár `ai-patient-sim` je postavený ako controlled interview-generation pipeline, nie ako voľný chatbot. V README sa explicitne uvádza fixný `Interview Pack`, validované scenario cards, hard `QC`, `judge`, `optimizer`, `comparator`, virtual rater, experiment grid, dashboard a web UI [../ai-patient-sim/README.md](/Users/pavol.bielik/dev/src/github.com/pbielik/ai-patient-sim/README.md#L21). Dokumentácia zároveň zdôrazňuje, že nejde o therapist chatbot ani free-form autonomous agent system, ale o auditovateľný research-oriented workflow [../ai-patient-sim/docs/FRAMEWORK_OVERVIEW.md](/Users/pavol.bielik/dev/src/github.com/pbielik/ai-patient-sim/docs/FRAMEWORK_OVERVIEW.md#L3).

Pre obhajobu je to dôležité, lebo môžeš povedať:

- nejde o ad hoc promptovanie,
- ide o kontrolované generovanie s fixným interview rámcom,
- ide o systém, kde vieme simuláciu iteratívne zlepšovať,
- ide o systém, kde vieme spätne auditovať, čo sa generovalo a prečo.

### Prečo je to prínos pre psychologický výskum a prax

1. `Replikovateľnosť`
   - Keď držíš seedy, interview pack a nezávislé premenné fixne, vieš porovnávať varianty bez toho, aby sa menil celý prípad.

2. `Kontrola kvality`
   - Hard QC, soft QC, judge, optimizer, comparator a virtual rater znamenajú, že simuláciu nenechávaš len „nejako vyjsť“, ale aktívne filtruješ nekonzistentnosť, generic filler a safety problémy.

3. `Rýchly vývoj ďalších porúch`
   - Ak máš seed-first architektúru, vieš rýchlejšie pripraviť nové klinicky ukotvené scenáre pre ďalšie poruchy bez toho, aby si zakaždým začínal od nuly.

4. `Výskumná použiteľnosť`
   - Platforma vie exportovať metadata, študijné varianty a bundle pre human-rating workflow, takže sa dá prepojiť s hodnotením odborníkmi a neskoršou štatistickou analýzou.

5. `Pedagogická škálovateľnosť`
   - Keď platforma dokáže generovať a batchovo spracovávať viac variantov, vieš pripravovať tréningové balíky pre viac študentov a viac tém bez lineárneho rastu personálnych nákladov.

### Konkrétne body z platformy, ktoré sa oplatí spomenúť

1. `Validated seed source of truth`
   - Finálny study pack drží `12` immutable validated seedov a `6` fixných variantov, teda `72` finálnych rozhovorov [../ai-patient-sim/app/experiments/final_study_pack.py](/Users/pavol.bielik/dev/src/github.com/pbielik/ai-patient-sim/app/experiments/final_study_pack.py#L5).

2. `Kontrolované nezávislé premenné`
   - Varianty sú definované ako `guardrail on/off × R1/R2/R3`, čiže platforma vie systematicky testovať, čo zlepšuje vierohodnosť a tréningovú použiteľnosť [../ai-patient-sim/app/experiments/final_study_pack.py](/Users/pavol.bielik/dev/src/github.com/pbielik/ai-patient-sim/app/experiments/final_study_pack.py#L43).

3. `Automated Chat Lab`
   - Batch režim vie generovať sessions naprieč seedmi alebo variantmi, držať schválený `IP3` flow, ukladať hidden `PHQ-9` metadata a ukladať sessions do report-ready storage [../ai-patient-sim/app/web/templates/chat_lab_automated.html](/Users/pavol.bielik/dev/src/github.com/pbielik/ai-patient-sim/app/web/templates/chat_lab_automated.html#L7).

4. `Human-rating napojenie`
   - Chat Lab exportuje flat metadata pre survey tool, aby sa dalo spájať generovanie, ľudské ratingy a štatistické spracovanie bez ručných joinov [../ai-patient-sim/docs/research/CHAT_LAB_SURVEY_TOOL_HANDOFF.md](/Users/pavol.bielik/dev/src/github.com/pbielik/ai-patient-sim/docs/research/CHAT_LAB_SURVEY_TOOL_HANDOFF.md#L1).

## Ako to hovoriť jednoducho na obhajobe

Krátka verzia:

> Prínos mojej práce nespočíva len v tom, že AI vie vygenerovať rozhovor. Dôležitejšie je, že som pripravil metodicky kontrolovanú platformu, v ktorej vieme simulované klinické prípady systematicky vytvárať, porovnávať, hodnotiť a zlepšovať pre potreby psychologického vzdelávania.

Rozšírená verzia:

> Pre psychológiu je dôležité, aby študenti mali možnosť trénovať interview aj vtedy, keď nemajú rovnaký prístup k reálnej klinickej praxi. Táto práca ukazuje, že AI simulácie možno nielen generovať, ale aj kontrolovať a hodnotiť tak, aby boli použiteľné ako doplnkový výcvikový nástroj. Zároveň som vytvoril platformový základ, ktorý umožňuje pripravovať ďalšie klinické scenáre, testovať ich kvalitu a neskôr ich rozširovať aj do multimodálnej podoby.

## Praktický prínos pre psychológov

Toto môžeš pokojne pomenovať aj explicitne:

- pre pedagógov psychológie: štandardizovateľný tréningový materiál,
- pre študentov: bezpečný nácvik pred prvou supervidovanou praxou,
- pre výskumníkov: platforma na testovanie, ktoré vlastnosti simulácie zvyšujú jej pedagogickú hodnotu,
- pre klinicky orientované pracoviská: možnosť pripraviť lokálne relevantné prípady bez potreby stavať celé SP programy od nuly,
- pre odbor ako celok: most medzi psychologickou expertízou, metodológiou a AI nástrojmi.

## Ako to zapracovať ešte explicitnejšie do textu

Ak tento framing prijmeš ako hlavnú praktickú líniu, v Úvode môžeš priamo pomenovať tri vrstvy prínosu:

1. `metodologický`
   - práca testuje, aké vlastnosti zvyšujú kvalitu simulovaného interview,
2. `edukačný`
   - práca pripravuje podklad pre použitie simulácií vo výučbe psychologického interview,
3. `platformový`
   - práca nestavia len jednorazový dataset, ale základ pre budúcu simulačnú platformu rozšíriteľnú na ďalšie poruchy a modality.

## Zahraničné opory a príklady

Poznámka: pre samotný rukopis majú byť jadrom najmä peer-reviewed zdroje. Weby univerzít sú vhodné najmä pre obhajobu, prezentáciu a opatrný kontextový odsek.

### Priama klinická prax / placementy

1. `UCL` (UK)
   - UCL uvádza, že trainees sú počas výcviku na klinických placementoch v `NHS settings` počas celého tréningu.
   - Zdroj: <https://www.ucl.ac.uk/clinical-psychology-doctorate/clinicalplacement>

2. `Oxford Institute of Clinical Psychology Training and Research` (UK)
   - Oxfordský `DClinPsych` je `NHS-funded course` a je priamo ukotvený na `Warneford Hospital`.
   - Zdroj: <https://oxicptr.web.ox.ac.uk/admissions>

3. `University of Queensland` (Australia)
   - Program uvádza minimum `1395 hours of supervised clinical practice` v oblastiach ako child and family, clinical neuropsychology a older adults.
   - Zdroj: <https://study.uq.edu.au/study-options/programs/master-clinical-neuropsychology-and-clinical-psychology-5766>

### Univerzitné psychologické kliniky

1. `Curtin University Adult Psychology Clinic` (Australia)
   - Služby poskytujú `clinical and professional psychology trainees` v rámci `supervised advanced post-graduate training`.
   - Zdroj: <https://www.curtin.edu.au/about/learning-teaching/health-sciences/about/clinics/adult-psychology-clinic/>

2. `University of Washington Psychological Services and Training Center` (USA)
   - Ide o hlavné tréningové centrum pre doktorandov klinickej psychológie; služby poskytujú `advanced graduate students` pod supervíziou licencovaných odborníkov.
   - Zdroj: <https://psych.uw.edu/community/the-clinic>
   - Doplňujúci tréningový opis: <https://psych.uw.edu/community/the-clinic/training-program>

### Simulácie ako doplnok výcviku

1. `Chaby et al., 2022`
   - Prehľad ukazuje, že komunikácia s psychiatrickými pacientmi je tréningovo náročná a že virtual patients vytvárajú relevantný rámec pre tréning komunikácie v psychiatrii a geriatrii.
   - Zároveň mapuje viacero depresívnych a suicidálnych scenárov v pred-LLM virtual patient nástrojoch.
   - Zdroj: <https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2022.827312/full>

2. `APS research summary k Sheen et al., 2021`
   - Austrálska psychologická spoločnosť sumarizuje, že simulation-based education u študentov klinickej psychológie zvýšila vnímanú pripravenosť a bola študentmi vnímaná ako bližšia klinickej praxi než case-based materiály.
   - Zdroj: <https://psychology.org.au/for-members/publications/inpsych/2020/april-may-issue-2/analyse-this/simulating-competence>

## Odporúčaná formulácia do rukopisu

Pracovná veta do Úvodu:

> V zahranične etablovaných klinicky orientovaných psychologických programoch je odborný výcvik často opretý o kombináciu supervidovaných placementov, univerzitných kliník a simulačných foriem výučby. Simulovaní pacienti preto nemožno chápať ako náhradu reálnej klinickej skúsenosti, ale skôr ako škálovateľný a pedagogicky kontrolovateľný doplnok, ktorý môže rozšíriť tréningové príležitosti tam, kde priama prax nie je dostupná v dostatočnom rozsahu.

Pracovná veta do Diskusie:

> Ak sa AI-generované interview ukazujú ako klinicky vierohodné a tréningovo použiteľné, ich hlavný praktický význam nespočíva v nahrádzaní klinickej praxe, ale v tom, že môžu slúžiť ako premostenie medzi teoretickou prípravou a prvými supervidovanými kontaktmi s klientom.

## Čomu sa vyhnúť

- Netvrdiť, že simulácie môžu nahradiť reálnych pacientov.
- Netvrdiť, že všetci zahraniční študenti psychológie majú rozsiahlu prax; presnejšie je hovoriť, že to je typické najmä pre profesijne orientované klinické a doktorandské programy.
- Nerobiť z práce evaluáciu študentského learning outcome, keďže aktuálny dizajn hodnotí kvalitu simulovaných interview, nie zmenu vedomostí študentov.
- Netvrdiť bez zdroja, že „na Slovensku takáto prax neexistuje“. Bezpečnejšia formulácia je, že jej dostupnosť môže byť lokálne obmedzená alebo nerovnomerná.

## Odporúčané ďalšie kroky

1. Doplniť tento framing do `1.2`, `1.6`, `4.4`, `4.7` a `4.8`.
2. Pripraviť 1 slide do prezentácie s názvom napr. `Prečo je to prínos pre vzdelávanie v psychológii`.
3. Doplniť 1 slide `Ako to riešia v zahraničí` s 3 až 5 konkrétnymi príkladmi.
4. Ak budú nové zdroje pridávané do textu, zaradiť ich najmä do klastrov `02 LLM, mental health a psychiatria` a `05 Všeobecná metodológia psychologického výskumu`, prípadne ako podklad pre gap `C`.
5. Ak bude tento framing prijatý ako hlavná línia obhajoby, následne upraviť aj `docs/aktualny-stav-diplomovky.md` a `docs/backlog-diplomovky.md`.
