# 50 Discussion / Diskusia

## 4 Diskusia

### 4.1 Stručné zhrnutie hlavných zistení

Cieľom práce bolo pilotne metodologicky overiť kvalitu AI-generovaných simulovaných klinických interview s depresívnou symptomatikou a preskúmať, či sa kvalita mení podľa prítomnosti štruktúrujúceho klinického usmernenia a podľa štýlu odpovedania simulovaného pacienta. Aktuálny korpus ukázal šesť hlavných zistení.

Po prvé, predbežná expertná obsahová kontrola ukázala, že jadro ratingového nástroja a seed scenárov je obsahovo obhájiteľné, ale zároveň upozornila na slabšie miesto v defektových položkách `R2`, `R3` a `R5` a na potrebu doladiť časť seed scenárov, najmä `08` a `10`. Po druhé, samotné rozhovory boli v priemere hodnotené ako **skôr klinicky vierohodné, jazykovo relatívne prirodzené a stredne použiteľné na tréningové účely**, pričom defekty ostávali skôr v nízkom pásme. Po tretie, distribúcie viacerých outcome-ov boli výrazne stlačené do úzkeho stredne vyššieho pásma, čo znamená, že veľká časť dát neleží na osi „dobré verzus zlé“, ale skôr na osi „celkom dobré verzus o niečo lepšie alebo slabšie“. Po štvrté, v aktuálnych dátach sa **neobjavil jasný a robustný dôkaz**, že by samotné zapnutie guardrailu alebo rozvinutejší profil odpovedania systematicky zlepšovali hlavné ľudské outcome-y. Po piate, dominantnou slabinou simulácií nebol hrubý klinický rozpad, ale skôr pocit nacvičenosti, mechanickosti a slabšieho follow-upu. Po šieste, kľúčovým limitom datasetu zostáva štruktúra rating vrstvy: plné pokrytie nesie najmä jadrová dvojica hodnotiteľov a jeden z nich používal škálu výrazne užšie.

Z hľadiska celkového obrazu teda práca skôr podporuje tvrdenie, že generovaný materiál je už na úrovni **použiteľného pilotného simulačného materiálu**, ale ešte nie je dostatočne stabilný na to, aby bolo možné jednoducho „zapnúť“ vyššiu kvalitu jediným guardrailom alebo aby bolo možné s vysokou istotou tvrdiť, že rozvinutejší profil automaticky vedie k lepšiemu rozhovoru.

### 4.2 Čo znamená priaznivý priemer, ale stlačené rozdelenie

Jedným z najdôležitejších zistení aktuálneho exportu je napätie medzi dvoma vrstvami výsledkov. Na jednej strane sú priemery globálnych outcome-ov priaznivé: rozhovory nepôsobia ako séria zjavne zlých alebo didakticky nepoužiteľných simulácií. Na druhej strane sú distribúcie viacerých outcome-ov silno koncentrované okolo stredne vyšších kategórií. To znamená, že ratingový priestor nie je v tomto datasete široko rozprestretý, ale skôr stlačený.

Tento obraz je dôležitý z interpretačného aj metodologického hľadiska. Interpretačne naznačuje, že systém už dokáže produkovať rozhovory, ktoré u expertov nespúšťajú dojem zjavného zlyhania. Metodologicky však takáto kompresia znižuje citlivosť na malé experimentálne rozdiely. Ak väčšina rozhovorov končí v pásme „skôr dobré“, potom aj reálny efekt guardrailu alebo profilu môže zostať v dátach utlmený len preto, že škála a rateri nevyužili dostatočne široký rozsah odpovedí.

Preto je dôležité, že nulový alebo slabý efekt v tomto datasete nemožno automaticky čítať ako dôkaz neexistencie rozdielu. Časť slabosti efektov môže byť reálna, ale časť môže byť aj dôsledkom distribučno-meracieho stlačenia. V pilotnej metodologickej práci je tento poznatok sám o sebe cenný: ukazuje, že ďalší posun už nezávisí len od generovania nových transkriptov, ale aj od toho, ako jemne vieme zachytiť rozdiely medzi nimi.

### 4.3 Čo do interpretácie vnáša predbežná expertná validácia

Predbežná expertná obsahová kontrola je dôležitá preto, že mení spôsob, akým treba čítať neskoršie current-export výsledky. Na jednej strane ukazuje, že ratingový nástroj ani seedy nevstupovali do hlavného zberu ako úplne nespracovaný alebo klinicky nepreverený materiál. Globálne položky a odhady závažnosti či funkčného dopadu boli expertmi podporené pomerne priaznivo, čo posilňuje argument, že jadro konštruktu bolo uchopené zmysluplne.

Na druhej strane tá istá validačná vrstva vopred ukázala, kde možno čakať väčšiu neistotu. Slabšia podpora položiek `R2`, `R3` a `R5` znamená, že práve defektový blok mohol byť od začiatku citlivejší na interpretačný štýl jednotlivých raterov. Podobne pri seedoch `08` a `10` sa ukázal nesúlad medzi zamýšľanou a expertne vnímanou závažnosťou, čo naznačuje, že časť variability v neskorších severity a fidelity vetvách nemusí byť iba vlastnosťou modelu alebo raterov, ale aj dôsledkom menej jednoznačne ukotveného stimulusového materiálu.

Pre diskusiu to znamená dve veci. Po prvé, current-export výsledky nemožno redukovať na otázku „funguje alebo nefunguje guardrail“. Po druhé, metodická sila práce neleží len v samotnom porovnaní experimentálnych buniek, ale aj v tom, že pred hlavným zberom prebehla obsahová kalibrácia nástroja a seedov. Tá síce nezabezpečuje definitívnu validitu, ale podstatne zvyšuje dôveryhodnosť toho, že neskoršie rozdiely a limity už zachytávajú reálnejšie vlastnosti simulácií, nie len úplne surový draft materiálu.

### 4.4 Prečo guardrail a profil nevyšli silnejšie

Najprv treba povedať, že výsledky neukazujú úplnú absenciu patternov. Pri indexe defektov bol guardrail efekt smerovo mierne priaznivý, pri niektorých bunkách s profilom `P3` sa deskriptívne ukázal priaznivejší obraz pri `G5`, `S1` a `S2`, a v doplnkových ordinálnych modeloch sa objavil aj slabší interakčný náznak. Problém je skôr v tom, že tieto posuny neboli dosť veľké ani dosť stabilné na to, aby vytvorili presvedčivý konfirmačný obraz.

Jedno možné vysvetlenie je, že manipulácia bola príliš hrubá vzhľadom na to, čo sa práca snaží zlepšiť. Samotné dichotomické rozlíšenie `off` verzus `on` zrejme nestačí na to, aby systematicky zmenilo kvalitu výsledného rozhovoru vo všetkých dimenziách. V praxi môže kvalitu rozhovoru ovplyvňovať celý rad jemnejších prvkov: presná formulácia guardrail textu, spôsob otázok, dôraz na follow-up, disclosure pravidlá, lokálna jazyková prirodzenosť alebo miera odpovednej variability.

Druhé vysvetlenie sa týka profilu odpovedania. Intuitívne sa môže zdať, že elaborovanejší profil bude automaticky lepší, ale aktuálne dáta ukazujú, že to tak byť nemusí. Viac textu a viac detailov môže zvyšovať pocit prirodzenosti len dovtedy, kým nezačne rásť dojem pripravenosti, mechanickosti alebo tematickej disciplíny bez organickej spontaneity. V tomto zmysle je veľmi možné, že `P3` nie je jednoducho „lepší“ než `P1`, ale len posúva chyby do iného typu.

Tretie vysvetlenie je meracie. Ak ratingy ostávajú v úzkom pásme a jadrová dvojica hodnotiteľov nepoužíva škálu rovnako široko, malé efekty majú nízku šancu ukázať sa ako robustné. To neznamená, že tam sú skryté veľké efekty; skôr to znamená, že pre malé a stredné rozdiely bol tento pilot málo citlivý.

### 4.5 Kde sa simulácie lámu: autenticita skôr než klinické jadro

Najzaujímavejším výsledkom kvalitatívnej vrstvy je, že dominantnou témou komentárov nebol hrubý klinický rozpad, ale **nacvičenosť alebo natrénovanosť odpovedí**. Tento motív je dôležitý, pretože mení interpretáciu toho, čo je dnes na simuláciách najslabšie. Nejde primárne o to, že by systém nevedel udržať základný depresívny rámec, ale skôr o to, že časť rozhovorov neznie dosť organicky.

Tento obraz dobre korešponduje s novšou literatúrou o virtuálnych klientoch a LLM simuláciách. Výskum opakovane ukazuje, že digitálne simulácie môžu byť didakticky cenné už vtedy, keď ešte nedosahujú plný realizmus, ale ich slabinou býva práve prílišná kooperatívnosť, nižšia spontánnosť alebo mechanickejší štýl odpovedí [@chaby2022embodiedvirtualpatients; @schmidt2025client101; @morrison2025virtuallypsychologist]. Aj v tomto datasete sa teda slabina neukazuje ako „nevie to depresiu“, ale skôr ako „vie to depresiu len trochu príliš učebnicovo“.

To je pre ďalší vývoj rámca veľmi dôležité. Ak sa má kvalita posúvať vyššie, nestačí len znižovať chyby. Potrebné je zlepšiť aj **mikrodynamiku rozhovoru**: prirodzenosť váhania, odpoveď na doplňujúcu otázku, lokálnu koherenciu detailov, citlivé prechody medzi témami a schopnosť niesť klinicky významný obsah bez dojmu, že je odpoveď „pripravená pre hodnotiteľa“.

### 4.6 Čo hovoria výsledky o tréningovej použiteľnosti

To, že tréningová použiteľnosť (`G5`) mala medián 4 a priemer ostal blízko hranice „skôr použiteľné“, je z aplikačného hľadiska povzbudivé. Znamená to, že expert panel v priemere nevnímal tieto rozhovory ako principiálne nepoužiteľné. Pre psychologické vzdelávanie je to dôležité, pretože simulácie nemusia byť dokonalé, aby mali didaktickú hodnotu. Dôležité je skôr to, či poskytujú bezpečný, opakovateľný a dostatočne vierohodný materiál, na ktorom sa dá trénovať vedenie interview a klinické uvažovanie [@appeswg2021newreality; @rice2022simulatedplacements].

Zároveň však komentáre o mechanickosti a slabšom follow-upe naznačujú, že tento materiál ešte nie je ideálny ako úplne samonosný tréningový nástroj. Skôr vyzerá ako **materiál vhodný do kontrolovaného výučbového rámca**, kde je prítomný debriefing, supervízia alebo aspoň explicitná reflexia limitov rozhovoru. V tom je aktuálny export veľmi realistický: neponúka obraz hotového virtuálneho pacienta, ale obraz sľubného simulačného medzikroku.

Tento záver je v súlade s literatúrou o simuláciách vo výučbe psychológie a psychiatrie, ktorá ich neberie ako náhradu reálneho klienta, ale ako most medzi teoretickou prípravou, štruktúrovaným nácvikom a neskoršou praxou [@rice2022simulatedplacements; @sheen2021simulationeducation; @glatz2022simulationelements].

### 4.7 Merací blok: najväčší limit nie je počet transkriptov, ale rater layer

Najdôležitejším metodologickým limitom aktuálneho exportu nie je počet transkriptov ani pokrytie experimentálnych buniek, ale **architektúra hodnotiteľskej vrstvy**. Formálne je raterov viac, ale plný dizajn nesú v praxi najmä dvaja hodnotitelia. To oslabuje najmä outcome-y, ktoré sú priamo závislé od ľudského úsudku, teda globálnu vierohodnosť, defekty, tréningovú použiteľnosť aj odhady závažnosti a funkčného dopadu.

Obzvlášť dôležitá je kompresia škály u jedného z jadrových hodnotiteľov. Táto vlastnosť má dvojitý dopad. Po prvé, znižuje variabilitu a tým aj šancu zachytiť jemnejšie rozdiely medzi transkriptmi. Po druhé, oslabuje presvedčivosť klasických agreement ukazovateľov. To neznamená, že výsledky sú nepoužiteľné. Znamená to však, že ich treba čítať ako **pilotné odhady smeru a veľkosti efektov**, nie ako robustný konsenzus širšieho expert panelu [@mchugh2012InterraterReliabilityKappa].

Je dôležité všimnúť si aj to, že vnútorná konzistencia blokov bola celkom slušná a že ešte pred hlavným zberom prešiel nástroj aj predbežnou obsahovou kontrolou expertov. To naznačuje, že problém nie je primárne v tom, že by položky vôbec nedržali spolu alebo že by nástroj bol od začiatku obsahovo chybný. Skôr ide o to, že **merací nástroj, stimulusový materiál a rater panel zatiaľ nedávajú rovnako silný signál**. Z pohľadu vývoja autorského ratingového nástroja je to úplne legitímna pilotná situácia: najprv sa ukáže, že bloky dávajú zmysel obsahovo a vnútorne, a až potom sa spevňuje širšia reliabilita a stabilita naprieč hodnotiteľmi [@boateng2018scaledevelopment; @terwee2018COSMINMethodologyEvaluating].

### 4.8 Čo zatiaľ vieme a nevieme povedať o symptom fidelity

Po doplnení plného anchor súboru bolo možné čítať transcript-level symptom-fidelity vetvu nad celým 12-seed korpusom. To je dôležitý krok, pretože umožňuje interpretovať `symptom_error_mean`, `severity_error` a `impact_error` nad celým aktuálnym súborom, nie len nad malou podmnožinou seedov.

Výsledok tejto vetvy je zaujímavý práve tým, že je umiernenejší než niektoré intuície. Symptom-fidelity chyba je skôr mierna než vysoká a guardrail efekt má priaznivý, ale malý smer. To znamená, že systém pravdepodobne drží základnú symptomatickú logiku o niečo lepšie, než naznačovali otvorené komentáre o mechanickosti. Zároveň sa však nepotvrdzuje predstava, že guardrail alebo rozvinutejší profil automaticky vyriešia fidelity problém výrazným spôsobom.

Aj po tomto posune však treba zostať opatrný. Dôvodom už nie je chýbajúce seed pokrytie, ale to, že error-based ukazovatele ostávajú citlivé na malý a nevyvážený rater panel a na spôsob transcript-level agregácie expertných odhadov pri `S1` a `S2`.

### 4.9 Porovnanie s literatúrou

Výsledky tejto práce sa najlepšie čítajú v troch literárnych rámcoch. Prvým je literatúra o štandardizovaných prípadoch a simuláciách vo vzdelávaní, ktorá dlhodobo ukazuje napätie medzi štandardizáciou a ekologickou validitou [@evans2015vignettes; @williams2017simulationmentalhealth]. Aj aktuálny export ukazuje presne toto napätie: rozhovory sú dostatočne disciplinované na to, aby držali základný klinický rámec, no práve táto disciplína môže znižovať pocit autenticity.

Druhým rámcom sú novšie práce o virtuálnych klientoch a LLM simuláciách. Tie spravidla ukazujú, že digitálne simulácie sú užitočné najmä ako bezpečný, opakovateľný a kontrolovateľný medzikrok, ale ich limitom býva nižšia spontánnosť a občasná „prehnaná ochota“ systému spolupracovať [@chaby2022embodiedvirtualpatients; @schmidt2025client101; @morrison2025virtuallypsychologist]. Dominantný motív nacvičenosti v našich komentároch s týmto obrazom veľmi dobre korešponduje.

Tretím rámcom je literatúra o kvalite generatívnych AI výstupov. Tá zdôrazňuje rozdiel medzi plynulosťou textu a jeho obsahovou spoľahlivosťou [@roustan2025cliniciansguide; @asgari2025hallucinationframework]. V našich dátach sa tento problém neukázal ako masívna halucinačná katastrofa. Ukázal sa skôr ako jemný rozdiel medzi tým, že rozhovor „znie celkom dobre“, a tým, že je dostatočne organický, hlboký a presvedčivý aj pri bližšom odbornom čítaní.

Za zmienku stojí aj to, že klinické uchopenie závažnosti depresie nie je ani v bežnej praxi triviálne. Literatúra upozorňuje, že kategórie severity bývajú v klinickom prostredí generické a nie vždy majú silné anchor body [@maj2020depressioncharacterization]. Časť variability pri `S1` a `S2` preto nemusí odrážať len slabinu simulácie, ale aj to, že samotný konštrukt globálneho odhadu severity a funkčného dopadu je pre ľudských hodnotiteľov náročný.

### 4.10 Limity výskumu

Prvým limitom je, že ide stále o pilotný dataset s relatívne malým a nevyváženým rater panelom. Čísla preto treba čítať ako odhad smeru a veľkosti efektov, nie ako definitívne uzavretý obraz kvality simulácií.

Druhým limitom je, že predbežná expertná obsahová kontrola mala charakter **pilotnej kalibrácie**, nie plnohodnotnej psychometrickej validity štúdie. Zvyšuje dôveryhodnosť nástroja a seedov, ale sama osebe neuzatvára otázku content validity ani nezaručuje, že po redakčných úpravách už v materiáli nezostali slabšie miesta.

Tretím limitom je **jadrová dvojica full raterov**. Hoci každý transkript mal aspoň dve nezávislé hodnotenia a celý dizajn bol pokrytý, väčšinu ľudskej inferenčnej vrstvy nesú v praxi dvaja hodnotitelia.

Štvrtým limitom je **nebalans ratingov medzi bunkami**, najmä vyššie pokrytie bunky `off × P1`. Mixed modely tento problém čiastočne tlmia, ale úplne ho neodstraňujú.

Piatym limitom je **stlačené rozdelenie viacerých outcome-ov**, ktoré znižuje citlivosť na malé rozdiely medzi podmienkami.

Šiestym limitom je, že **anchorová error vetva** ostáva metodicky citlivá na malý a nevyvážený rater panel a na transcript-level agregáciu expertných odhadov pri `S1` a `S2`. Aj pri plnej anchor coverage ju preto treba interpretovať opatrnejšie než robustnejšie ľudsky hodnotené outcome-y.

Siedmym limitom je samotná povaha stimulusového materiálu. Hodnotené boli textové simulácie, nie živé multimodálne rozhovory. Chýbajú teda neverbálne a paralingvistické znaky, ktoré v reálnej klinickej situácii výrazne spoluutvárajú dojem z klienta aj interpretáciu symptomatiky.

### 4.11 Praktické a metodologické dôsledky

Napriek týmto limitom má aktuálny export dôležitý praktický aj metodologický význam. Po prvé, ukazuje, že kvalitu simulovaných AI rozhovorov možno hodnotiť viacvrstvovo: nie iba cez globálny dojem, ale aj cez blok prirodzenosti, použiteľnosti, defektov a neskôr aj transcript-level fidelity. Dôležité pritom je, že táto viacvrstvová logika nebola postavená až dodatočne po zbere, ale prešla aj predbežnou expertnou obsahovou kontrolou položiek a seedov. To je metodicky silnejší rámec než jednoduché hodnotenie „znie to dobre / neznie to dobre“.

Po druhé, výsledky naznačujú, že ďalší posun kvality pravdepodobne nepríde len cez pridanie ďalších transkriptov, ale cez **lepšie kalibrovaný expert panel** a cez úpravy, ktoré znížia pocit nacvičenosti a zvýšia klinickú hĺbku rozhovoru. Prakticky to znamená väčší dôraz na follow-up logiku, prirodzenosť slovenskej formulácie, lokálnu koherenciu detailov a citlivejšie vedenie rozhovoru v oblastiach záťaže a rizika.

Po tretie, dáta podporujú chápanie tejto práce ako vývoja **simulačného rámca**, nie len jedného promptu alebo jedného balíka transkriptov. Hodnota práce je práve v tom, že spája seedy, kontrolované generovanie, expert rating a viacvrstvové hodnotenie kvality. Takýto rámec je metodologicky prenositeľný aj na ďalšie klinické témy.

### 4.12 Odporúčania pre ďalší výskum

Najrozumnejším ďalším krokom nie je okamžite generovať ďalší veľký balík nových transkriptov, ale **posilniť expert rating vrstvu**. Z pohľadu aktuálnych dát by mal najväčší prínos ešte aspoň jeden ďalší full rater nad existujúcimi 72 transkriptmi. Takýto krok by zlepšil interpretovateľnosť zhody aj stabilitu inferenčných modelov viac než ďalšie rozširovanie stimulusového priestoru.

Ďalším krokom by mala byť revízia promptového a interview dizajnu so zameraním na zníženie nacvičenosti odpovedí, na väčšiu prirodzenosť follow-up otázok a na lepšie odlíšenie depresívneho obrazu od všeobecného stresu alebo vyhorenia. Až potom bude dávať väčší zmysel rozširovať seed priestor, porovnávať viac modelov alebo testovať učebné výsledky u študentov psychológie [@sheen2021simulationeducation; @glatz2022simulationelements; @schmidt2025client101].

Popri tom treba dotiahnuť aj štatistické a metodické ukotvenie anchorovej error vetvy tak, aby mala rovnaký evidenčný status ako ostatné outcome bloky a aby sa dala interpretovať s rovnakou mierou istoty.

### 4.13 Záver diskusie

Aktuálny korpus ukazuje, že AI-generované simulované interview s depresívnou symptomatikou už možno považovať za **metodicky použiteľný pilotný materiál**, nie však ešte za plne stabilný a jednoducho optimalizovateľný produkt. Dôležité pritom je, že tento záver nestojí len na samotných ratingoch transkriptov, ale aj na predbežnej expertnej obsahovej kontrole nástroja a seed scenárov. Rozhovory držia základný klinický rámec a v priemere nepôsobia ako zjavne nekvalitné, ale ich slabinou ostáva autenticita, stlačené rozdelenie ratingov, limitovaná zhoda expertov a opatrná interpretovateľnosť anchorovej error vetvy.

Hlavným prínosom práce preto v tejto fáze nie je dôkaz silného experimentálneho efektu guardrailu alebo profilu, ale ukázanie, že kvalitu takýchto simulácií možno systematicky mapovať, porovnávať a postupne zlepšovať v rámci kontrolovaného simulačného rámca. Práve táto metodická mapa je dnes silnejšia než akýkoľvek predčasne tvrdý záver o tom, že jedna konkrétna generatívna manipulácia už problém vyriešila.
