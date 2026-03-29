# 30 Method / Metóda

> Pracovný draft kapitoly. Finálna verzia pôjde do Wordu so živými Zotero citáciami. Tento text je už koncipovaný ako thesis-ready verzia a má sa iba doplniť o finálne počty, citekeys a drobné formálne úpravy.

## 2 Metóda

### 2.1 Charakter výskumu a výskumný dizajn

Predkladaný výskum má charakter **pilotnej kvantitatívnej metodologickej štúdie** zameranej na odborné hodnotenie kvality AI-generovaných simulovaných klinických interview so zameraním na depresívnu symptomatiku. Cieľom výskumu nebolo overovať diagnostickú presnosť systému v klinickej praxi ani nahrádzať odborné rozhodovanie, ale preskúmať, do akej miery sú generované rozhovory odbornými hodnotiteľmi vnímané ako klinicky vierohodné, jazykovo prirodzené, vnútorne konzistentné a zodpovedajúce cieľovému symptomatickému profilu.

Výskum bol navrhnutý ako **faktorový experiment v rámci human-rated hodnotenia transkriptov**. Experimentálne boli manipulované dve nezávislé premenné: prítomnosť alebo neprítomnosť promptového guardrailu (`guardrail: off/on`) a realizačný profil odpovedí (`profile: R1/R2/R3`). Kombináciou týchto faktorov vzniklo šesť finálnych experimentálnych variantov. Každý variant bol aplikovaný na 12 vopred pripravených a klinicky ukotvených seed scenárov, čím vznikol súbor 72 textových transkriptov určených na odborné hodnotenie.

Zvolený dizajn bol koncipovaný ako kontrolovaná modelová situácia, v ktorej bolo možné systematicky sledovať vplyv experimentálnych faktorov na kvalitu generovaného rozhovoru pri zachovaní klinickej variability medzi seedmi. Keďže jednotlivé hodnotenia boli zároveň viazané na konkrétny seed aj na konkrétneho hodnotiteľa, už pri projektovaní výskumu sa počítalo s viacúrovňovou štruktúrou dát.

### 2.2 Výskumný súbor

Výskumný súbor tvorili **odborní hodnotitelia** z oblasti psychológie, psychoterapie a psychiatrie, ktorí mali skúsenosť s klientmi s depresívnou symptomatikou alebo s diagnózou MDD. Výber mal charakter **účelového výberu**, pretože cieľom nebolo reprezentatívne zachytiť celú populáciu odborníkov, ale získať kvalifikované expertné posúdenie transkriptov. Do výskumu boli zaradení iba tí hodnotitelia, ktorí spĺňali odborné kritériá a súhlasili s účasťou na hodnotení.

Inklúznymi kritériami boli: (a) odborné vzdelanie alebo odborná prax v oblasti psychológie, psychoterapie alebo psychiatrie, (b) skúsenosť s prácou s depresívnou symptomatikou alebo s diagnózou MDD, (c) ochota zúčastniť sa na hodnotení textových transkriptov. Exklúznym kritériom bola absencia relevantnej odbornej skúsenosti alebo nedokončené hodnotenie v rozsahu znemožňujúcom jeho analytické použitie.

Počet zaradených hodnotiteľov bol **[doplniť finálny počet]**. Každý hodnotiteľ posudzoval podmnožinu transkriptov podľa finálneho rozvrhu ratingu. Jednotkou analýzy nebol samotný hodnotiteľ ani samotný transkript, ale **jedno hodnotenie jedného transkriptu jedným hodnotiteľom**. Dataset preto nadobudol dlhý formát, v ktorom jeden riadok reprezentoval jedno expertné hodnotenie.

### 2.3 Výskumný materiál

Stimulusový materiál pozostával zo 72 textových transkriptov simulovaných interview. Tieto rozhovory boli generované na základe 12 fixných seed scenárov (`S01–S12`), ktoré predstavovali klinicky ukotvené modelové profily depresívnej symptomatiky. Seedy obsahovali demografický a kontextový rámec, symptomatické kotvy pre oblasti `A1–A9`, pravidlá disclosure, štýlové nastavenia a bezpečnostné limity odpovedí.

Klinická variabilita medzi transkriptmi bola primárne nesená seedmi. Experimentálne manipulovaná variabilita bola reprezentovaná faktormi `guardrail` a `profile`. Finálny experimentálny preset pozostával zo šiestich variantov definovaných ako `G0/G1 × R1/R2/R3`, kde `G0/G1` označovalo neprítomnosť alebo prítomnosť guardrailu a `R1/R2/R3` predstavovalo rezervovanejší, baseline a rozvinutejší realizačný profil. Pri finálnom balíku transkriptov bola variabilita nastavená ako `locked`, aby sa minimalizoval nekontrolovaný drift a aby sa v hodnotení testovali primárne práve experimentálne manipulované vlastnosti generovania.

### 2.4 Hodnotiaci nástroj

Na zber hodnotení bol použitý autorsky zostavený ratingový dotazník implementovaný v internom survey engine. Nástroj obsahoval tri hlavné bloky položiek.

Prvý blok tvorili **primárne kvalitatívne outcome-y** `G1–G5`, zamerané na klinickú vierohodnosť rozhovoru, prirodzenosť jazyka a štýlu odpovedí, vnútornú konzistentnosť rozhovoru, súlad rozhovoru s obrazom depresívnej symptomatiky a použiteľnosť rozhovoru na tréningové alebo výučbové účely.

Druhý blok tvorili **symptom fidelity položky** `A1–A9` a odhady `S1` a `S2`, ktoré zachytávali zhodu rozhovoru s cieľovým symptomatickým profilom seedu, odhad celkovej závažnosti depresívnej symptomatiky a odhad funkčného dopadu na bežné fungovanie.

Tretí blok tvorili **QC a defect položky** `R1–R5`, zamerané na kontradikcie, klišé alebo šablónovité odpovede, nesúlad medzi kontextom a symptomatikou, podozrenie na inú primárnu psychopatológiu a neprimeranú dramatizáciu alebo neprirodzenú expresivitu.

Položky `G1–G5` a `guess_confidence` boli koncipované ako 5-bodové Likertove škály. Položky `A1–A9`, `S1`, `S2` a `R1–R5` boli ukotvené na škále `0–3`, aby boli lepšie naviazané na seed anchory a aby umožnili výpočet odchýlky medzi očakávaným a hodnoteným profilom. Súčasťou nástroja bola aj nominálna položka `guessed_origin` a otvorená textová položka `comment`.

### 2.5 Premenné a operacionalizácia

Hlavnými **nezávislými premennými** boli `guardrail` a `profile`. Premenná `guardrail` mala dve úrovne: vypnutý a zapnutý guardrail. Premenná `profile` mala tri úrovne: `R1` (rezervovanejší profil), `R2` (baseline profil) a `R3` (rozvinutejší profil). Ako blokovací faktor bol použitý `seed_id`, ktorý reprezentoval klinický základ scenára. Na úrovni modelovania bol zároveň zohľadnený `rater_id`, teda identita hodnotiteľa.

**Primárne závislé premenné** tvorili položky `G1–G5`. Okrem jednotlivých položiek bol vytvorený kompozitný ukazovateľ **klinickej plausibility** `plausibility_index`, vypočítaný ako priemer položiek `G1`, `G3` a `G4`, pretože tieto tri položky konceptuálne najtesnejšie reprezentovali jadro klinickej vierohodnosti simulovaného interview. Položka `G2` bola analyzovaná samostatne ako ukazovateľ prirodzenosti jazyka a `G5` ako ukazovateľ tréningovej použiteľnosti.

**Sekundárne premenné** tvorili položky `A1–A9`, `S1` a `S2`. Keďže pre každý seed boli vopred definované anchor hodnoty, bolo možné okrem samotných ratingov odvodiť aj **error-based ukazovatele**, konkrétne absolútnu odchýlku hodnotenia od seed anchoru. Takto vznikli premenné `symptom_error_mean`, `severity_error` a `impact_error`.

**QC premenné** tvorili položky `R1–R5`, z ktorých bol odvodený aj kompozit `defect_index`. Ich účelom bolo zachytiť tie nedostatky rozhovorov, ktoré mohli znižovať ich klinickú alebo výučbovú použiteľnosť.

### 2.6 Procedúra

Najprv bol pripravený finálny balík seed scenárov a experimentálnych variantov generovania. Následne boli vygenerované textové transkripty podľa jednotného interview protokolu a uložené v štandardizovanom formáte. Pred zaradením do hodnotenia boli transkripty skontrolované z hľadiska technickej úplnosti a formálnej konzistencie.

Hodnotitelia dostávali na posúdenie jednotlivé transkripty prostredníctvom webového hodnotiaceho rozhrania. Pri každom transkripte vyplnili ratingový dotazník a prípadne doplnili otvorený komentár. V závislosti od finálneho rozdelenia hodnotiacej záťaže každý transkript hodnotili **[doplniť: dvaja / viacerí]** hodnotitelia. Hodnotenie prebiehalo individuálne a asynchrónne.

Pri exporte odpovedí sa odpovede ukladané v JSON štruktúre konvertovali do tabuľkového formátu vhodného na následné štatistické spracovanie. Finálny analytický dataset mal dlhý formát a obsahoval identifikátor hodnotiteľa, identifikátor transkriptu, experimentálne premenné, položkové ratingy a odvodené kompozity.

### 2.7 Spracovanie dát a štatistická analýza

Pred analýzou boli všetky exportované odpovede skontrolované, vyčistené a prekódované. Likertove odpovede boli konvertované zo stringového exportu na numerické alebo ordinálne premenné podľa typu analýzy. Následne boli vytvorené odvodené premenné `plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error` a `impact_error`.

Najprv bola spracovaná **deskriptívna štatistika** položiek a kompozitov. Pri ordinálnych položkách boli sledované frekvencie, mediány a interkvartilové rozpätia, pri kompozitných ukazovateľoch aj priemery a smerodajné odchýlky. V ďalšom kroku bola analyzovaná **vnútorná konzistencia** vybraných blokov položiek, najmä bloku `G1–G5`, plausibility bloku a bloku `R1–R5`.

Interrater reliabilita bola vyhodnocovaná prostredníctvom **intraclass correlation coefficient (ICC)** pre agregované ukazovatele. Pri reporte ICC sa počítalo s explicitným uvedením zvoleného typu koeficientu a spôsobu jeho interpretácie.

Hlavná inferenčná analýza bola realizovaná pomocou **mixed-effects modelov**, keďže jednotkou analýzy bolo hodnotenie, ktoré bolo zároveň viazané na hodnotiteľa aj na seed. Pre kompozitné a error-based ukazovatele boli použité lineárne zmiešané modely s fixnými efektmi `guardrail`, `profile` a ich interakcie a s náhodnými interceptmi pre `seed_id` a `rater_id`. Základný model mal tvar:

`outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)`

Pre jednotlivé ordinálne položky, najmä `G2`, `G5` a `guess_confidence`, boli plánované **ordinal mixed models** typu cumulative link mixed model ako citlivostná alebo doplnková analýza. Exploratórne bola plánovaná aj analýza položky `guessed_origin`, a to najmä pomocou frekvenčného rozdelenia a prípadne logistického modelu nad binarizovanou premennou „vnímané ako AI vs. nie AI“.

Otvorené komentáre hodnotiteľov boli analyzované kvalitatívne prostredníctvom stručného tematického kódovania. Cieľom tejto analýzy nebolo budovať samostatnú kvalitatívnu časť práce, ale doplniť kvantitatívne výsledky o opakujúce sa dôvody pozitívneho a negatívneho hodnotenia.

### 2.8 Etické aspekty

Výskum nepracoval s reálnymi pacientskymi údajmi ani s reálnymi klinickými rozhovormi. Hodnotený materiál tvorili simulované textové transkripty vytvorené na základe vopred pripravených seed scenárov. Riziko pre participantov bolo preto nízke. Napriek tomu boli rešpektované základné etické princípy psychologického výskumu, najmä informovanosť hodnotiteľov o charaktere úlohy, dobrovoľnosť účasti, možnosť účasť ukončiť a ochrana ich identifikačných údajov pri spracovaní odpovedí.
