# 50 Discussion / Diskusia

> Táto kapitola je pripravená ako reálny diskusný draft. Je napísaná tak, aby sa po doplnení finálnych výsledkov dala relatívne ľahko preformulovať do Wordu so živými citáciami.

## 4 Diskusia

### 4.1 Stručné zhrnutie hlavných zistení

Cieľom diplomovej práce bolo pilotne metodologicky overiť kvalitu AI-generovaných simulovaných klinických interview s depresívnou symptomatikou a preskúmať, či sa ich kvalita mení v závislosti od experimentálne manipulovaných vlastností generovania. Výsledky ukázali, že **[doplniť 2–4 najdôležitejšie zistenia]**. V jadre teda práca naznačuje, že kvalita simulovaného AI rozhovoru nie je daná iba samotným modelom alebo seed scenárom, ale aj konkrétnym spôsobom riadenia generovania a mierou kontroly nad jeho variabilitou.

### 4.2 Interpretácia primárnych výsledkov

Prvým dôležitým okruhom výsledkov bola klinická vierohodnosť rozhovorov. Ak sa potvrdí priaznivý efekt prítomnosti štruktúrujúceho klinického usmernenia, možno to interpretovať tak, že explicitnejšie usmernenie generovania znižuje voľný drift a pomáha modelu držať sa symptomatického a komunikačného jadra seed scenára. Takýto efekt by bol metodologicky dôležitý, pretože naznačuje, že kvalita simulácie nie je len otázkou „silného modelu“, ale aj otázkou kontrolovaného návrhu generovania.

Ak sa zároveň ukáže, že prítomnosť štruktúrujúceho klinického usmernenia znižuje aj index defektov, je to prakticky ešte dôležitejší výsledok než samotné zvýšenie klinickej vierohodnosti. Pre tréningové a výučbové použitie totiž nestačí, aby text pôsobil dobre na prvý dojem. Potrebné je aj to, aby neobsahoval kontradikcie, zjednodušenia alebo obsahové chyby, ktoré by mohli študenta alebo používateľa viesť k nesprávnym záverom.

Druhým kľúčovým okruhom je prirodzenosť jazyka. Ak sa preukáže, že rozvinutejší štýl odpovedania na úrovni R3 zvyšuje prirodzenosť rozhovoru, možno to chápať ako znak toho, že bohatšie a rozvinutejšie odpovede vytvárajú presvedčivejší dialóg. Zároveň však treba sledovať, či sa tým nezvyšuje aj miera defektov. Práve toto možné napätie medzi prirodzenosťou a kontrolou kvality je jedným z metodologicky najzaujímavejších momentov celej štúdie.

### 4.3 Interpretácia výsledkov symptomatickej primeranosti

Osobitne dôležitou časťou práce je perspektíva symptomatickej primeranosti. V nej sa kvalita rozhovoru neposudzuje len na základe dojmu, ale aj na základe zhody s vopred definovaným seed profilom. To je metodologicky silná stránka dizajnu, pretože umožňuje porovnávať rozhovory nielen ako celky, ale aj ako systematicky ukotvené varianty vo vzťahu k cieľovým symptomatickým kotvám.

Ak sa ukáže, že rozhovory so štruktúrujúcim klinickým usmernením majú nižšiu chybu voči seed kotvám, podporuje to predstavu, že toto usmernenie nepôsobí iba ako štylistický regulátor, ale aj ako mechanizmus zvyšujúci obsahovú presnosť. Ak by sa však ukázalo, že rozdiely sú malé alebo nestabilné, znamenalo by to, že symptomatická presnosť ostáva aj pri kontrolovanom promptovaní krehkou a môže si vyžadovať ďalšie vrstvy riadenia, napríklad explicitnejšie pravidlá pre disclosure alebo kontrolné validačné kroky.

Zaujímavé je aj to, ktoré symptomatické domény vychádzajú stabilne a ktoré nie. Predpokladateľne sa môžu lepšie generovať tie oblasti, ktoré sa dajú vyjadriť jazykovo priamo a často sa objavujú vo verejnom diskurze, zatiaľ čo jemnejšie oblasti, ako napríklad psychomotorika, funkčný dopad alebo pasívne myšlienky na smrť bez explicitnej dramatizácie, môžu byť pre model náročnejšie na konzistentné uchopenie.

### 4.4 Tréningová použiteľnosť a vnímaný pôvod rozhovoru

Pre praktické využitie výsledkov je kľúčové, či sú rozhovory vnímané ako použiteľné na tréningové a výučbové účely. Ak sa ukáže, že vyšší index klinickej vierohodnosti a nižší index defektov sú spojené s vyššou tréningovou použiteľnosťou, potvrdzuje to logiku, že kvalita simulácie nie je samoúčelná, ale priamo súvisí s tým, či má materiál didaktickú hodnotu. Pre psychologické vzdelávanie by takýto výsledok znamenal, že simulovaný rozhovor môže slúžiť nielen ako ilustrácia symptómov, ale aj ako nástroj na nácvik vedenia interview, rozpoznávania jadra symptomatiky, citlivého dopytovania na funkčný dopad či suicidálne témy a na učenie sa tolerovať neistotu pri rozhovore s menej otvoreným alebo menej koherentným klientom [@rice2022simulatedplacements; @schmidt2025client101; @morrison2025virtuallypsychologist].

Toto je dôležité aj preto, že literatúra o simuláciách vo vzdelávaní psychológov opakovane rámcuje simulácie ako most medzi teoretickým učením a prvou supervidovanou praxou, nie ako náhradu reálneho klienta [@appeswg2021newreality; @ajluni2025psychiatriceducation]. Ak by odborníci hodnotili časť našich rozhovorov ako dostatočne použiteľnú na tréning, bolo by možné uvažovať o ich nasadení ako o bezpečnom a opakovateľnom medzikroku pred prvým kontaktom s klientom, prípadne ako o doplnku tam, kde sú klinické praxe alebo pestrosť dostupných prípadov limitované [@rice2022simulatedplacements; @williams2017simulationmentalhealth].

Podobne zaujímavá je aj otázka vnímaného pôvodu rozhovoru. Ak rozhovory s vyšším indexom klinickej vierohodnosti a nižším indexom defektov menej často pôsobia ako zjavne AI-generované, naznačuje to, že odborníci pri odhadovaní pôvodu zrejme nereagujú len na povrchové jazykové znaky, ale aj na hlbšiu konzistentnosť a klinickú logiku textu. Ak by sa však takéto prepojenie nepotvrdilo, bolo by to rovnako dôležité zistenie, pretože by naznačovalo, že vnímanie „AI-ovosti“ textu sa môže opierať aj o iné kvality než tie, ktoré sme merali ako primárne výstupy. Z pedagogického hľadiska navyše ani prípadné rozpoznanie AI pôvodu nemusí automaticky rušiť využiteľnosť materiálu; rozhodujúcejšie je, či rozhovor podporuje správne učenie a nevedie študenta k chybným klinickým inferenciám. Štúdia Client101 napríklad ukazuje, že aj relatívne ľudsky pôsobiaci virtuálny klient môže byť didakticky užitočný a zároveň stále narážať na limity realizmu, najmä ak je príliš ochotný alebo málo komplexný [@schmidt2025client101].

### 4.5 Porovnanie s literatúrou

Výsledky práce je potrebné interpretovať v širšom kontexte štyroch oblastí literatúry. Prvou sú práce o štandardizovaných prípadoch, vinietach a modelových materiáloch vo výučbe a výskume. Tieto práce dlhodobo ukazujú, že štandardizácia je užitočná, ale vždy sa pohybuje v napätí s prirodzenosťou a ekologickou validitou [@evans2015vignettes; @williams2017simulationmentalhealth]. Zistenia predkladanej práce na tento problém nadväzujú, ale prenášajú ho do prostredia generatívnej AI.

Druhou oblasťou je priamo vzdelávanie psychológov založené na simuláciách. Odporúčania a metodické texty skupiny APPESWG ukazujú, že simulácie a dokonca aj simulované praxe už majú v profesionálnom psychologickom tréningu legitímne miesto, najmä ak pomáhajú štandardizovať tréning, chrániť klientov a vytvárať opakovanú prax so spätnou väzbou [@appeswg2021newreality; @rice2022simulatedplacements]. Empirické práce z klinickopsychologického prostredia zároveň naznačujú, že prvky výučby založenej na simuláciách sa môžu spájať s rastom sebadôvery, vnímanej pripravenosti a niekedy aj s vyššou pripravenosťou na klinickú prax podľa supervízorov, hoci väčšina týchto zistení má exploratórny alebo kurikulárno-implementačný charakter [@sheen2021simulationeducation; @glatz2022simulationelements]. To je dôležité pre interpretáciu našich výsledkov: naša štúdia ešte netestuje, či sa študenti na AI simuláciách skutočne učia lepšie, ale poskytuje predchádzajúci krok tým, že overuje kvalitu samotného materiálu, na ktorom by sa takéto učenie mohlo zakladať.

Treťou oblasťou sú práce o virtuálnych klientoch a chatbotových simuláciách v psychologickom a psychiatrickom vzdelávaní. Prehľad [@chaby2022embodiedvirtualpatients] ukazuje, že tréning komunikácie s pacientom prostredníctvom virtuálnych pacientov má v psychiatrii dlhšiu tradíciu, no pred-LLM nástroje často narážali na obmedzenú konverzačnú flexibilitu. Novšie práce ako Client101 a „You're virtually a psychologist“ ukazujú, že nástroje typu virtuálneho klienta sú študentmi a praktikmi vnímané ako bezpečný a dostupný doplnok tréningu, no ich didaktická hodnota závisí od realizmu, primeranej komplexity a od zasadenia do ľudskej supervízie [@schmidt2025client101; @morrison2025virtuallypsychologist]. Ak sa v našich výsledkoch ukáže, že niektoré varianty rozhovorov pôsobia príliš ochotne, genericky alebo málo konzistentne, bude to presne v súlade s týmito novšími zisteniami.

Štvrtou oblasťou sú práce o generatívnej AI a kvalite textových výstupov. Tie spravidla zdôrazňujú, že jazyková plynulosť neznamená automaticky obsahovú správnosť a že aj veľmi presvedčivý text môže obsahovať nekonzistentnosti alebo halucinácie [@roustan2025cliniciansguide; @asgari2025hallucinationframework]. Ak sa v našich výsledkoch objavia závažné problematické chyby aj pri jazykovo plynulých rozhovoroch, bude to s týmito zisteniami v zhode. Predkladaná práca k tejto oblasti prispieva tým, že nepoužíva iba celkový dojem, ale kombinuje primárne kvalitatívne ratingy, logiku symptomatickej primeranosti a dimenziu defektov. Práve toto viacvrstvové hodnotenie považujem za jeden z hlavných metodologických prínosov práce.

### 4.6 Limity výskumu

Predkladaná štúdia má viacero limitov. Prvým je **pilotný charakter výskumu**. To znamená, že výsledky treba interpretovať opatrne, najmä pokiaľ ide o stabilitu efektových odhadov a možnosti širšieho zovšeobecnenia.

Druhým limitom je **počet hodnotiteľov**. Hoci expert rating prináša vysokú obsahovú hodnotu, malý alebo stredne veľký počet raterov prirodzene obmedzuje presnosť odhadov interrater reliability a zvyšuje citlivosť výsledkov na individuálne hodnotiace štýly.

Tretím limitom je **účelový výber hodnotiteľov**. Výskumný súbor nebol reprezentatívnou vzorkou všetkých odborníkov, ale skupinou expertov ochotných zapojiť sa do hodnotenia. To je pri pilotnej metodologickej štúdii pochopiteľné, ale zároveň to obmedzuje možnosti širšieho zovšeobecnenia.

Štvrtým limitom je samotná povaha stimulusového materiálu. Hodnotené boli **simulované textové interview**, nie reálne klinické rozhovory a nie multimodálne interakcie. V textovej simulácii chýbajú neverbálne prejavy, intonácia, tempo reči a ďalšie jemné signály, ktoré v reálnej klinickej situácii ovplyvňujú dojem z klienta aj interpretáciu symptomatiky.

Piatym limitom je **modelová a promptová závislosť výstupov**. Výsledky sa vzťahujú na konkrétnu konfiguráciu seedov, promptového nastavenia a experimentálnych presetov. Pri inom modeli alebo inom nastavení generovania by mohli vyzerať odlišne.

### 4.7 Praktické a metodologické dôsledky

Napriek uvedeným limitom má práca viacero praktických a metodologických dôsledkov. Po prvé, ukazuje, že AI-generované simulované interview možno hodnotiť systematicky a viacvrstvovo, nie iba intuitívne. Po druhé, naznačuje, že kvalita takýchto výstupov sa dá experimentálne zlepšovať cez kontrolu generovania. Po tretie, vytvára rámec, ktorý môže byť využitý aj pri ďalších témach, nielen pri depresívnej symptomatike.

Z hľadiska psychologického vzdelávania je dôležité najmä to, že práca ponúka argument pre simulácie ako **doplnok**, nie náhradu živej praxe. Ak je kvalita simulovaného rozhovoru dostatočná, môže takýto materiál znižovať vstupnú bariéru pred prvým kontaktom s klientom, vytvárať bezpečný priestor na prvé pokusy, štandardizovať časť výučby naprieč nerovnakými lokálnymi podmienkami a cielene sprístupňovať aj menej časté alebo citlivé situácie, ktoré sa v bežnej výučbe nemusia objaviť včas alebo v dostatočnom rozsahu [@appeswg2021newreality; @rice2022simulatedplacements; @schmidt2025client101; @morrison2025virtuallypsychologist]. Pre študentov psychológie je takýto prínos relevantný najmä pri nácviku vedenia interview, práce s mlčaním či neistotou, rozpoznávania jadra symptomatiky, citlivého dopytovania na suicidálne alebo inak zaťažujúce témy a pri učení sa odlíšiť vierohodný klinický obraz od jazykovo plynulej, ale obsahovo problematickej simulácie.

Z prakticko-technologického hľadiska považujem za dôležité aj to, že predmetom práce nie je iba jednorazový prompt alebo jednorazový set transkriptov. V rámci práce vzniká kontrolovaný simulačný rámec, v ktorom sa dajú prípady systematicky pripravovať, porovnávať, hodnotiť a iteratívne zlepšovať. To je relevantné nielen pre túto jednu štúdiu, ale aj ako metodický základ pre budúce tréningové a výskumné využitie pri ďalších klinických scenároch.

Z praktického hľadiska môže byť výstup práce zaujímavý najmä pre:
- tréning a výučbu psychologického interview,
- pilotovanie ratingových nástrojov,
- prípravu štandardizovaných prípadov,
- metodologický výskum kvality AI-generovaných psychologických materiálov,
- budovanie rozšíriteľného simulačného rámca pre ďalšie klinické scenáre.

Z metodologického hľadiska považujem za dôležité, že práca kombinuje tri úrovne posudzovania: celkovú kvalitu, zhodu so seed kotvou a perspektívu defektov. Táto kombinácia znižuje riziko, že kvalitu rozhovoru budeme hodnotiť iba na základe jazykovej plynulosti alebo iba na základe formálne správneho symptom checklistu.

### 4.8 Odporúčania pre ďalší výskum

Budúci výskum by mal rozšíriť počet hodnotiteľov, spresniť anchorovanie niektorých domén a overiť, do akej miery sú zistenia replikovateľné pri inom modeli alebo inom promptovaní. Zaujímavým ďalším krokom by bolo aj porovnanie AI-generovaných simulovaných interview s ľudsky simulovanými rozhovormi, s rovesníckym hraním rolí, so štandardizovanými pacientmi alebo s iným typom štandardizovaných prípadov. Ešte dôležitejšie však bude posunúť sa od expertne hodnotenej kvality materiálu k učebným výsledkom, teda testovať, či práca s takýmito simuláciami skutočne zlepšuje schopnosť viesť interview, rozpoznávanie symptomatiky, sebaúčinnosť, pripravenosť na klinickú prax alebo citlivé zvládanie rizikových tém u študentov psychológie [@sheen2021simulationeducation; @glatz2022simulationelements; @schmidt2025client101].

Za metodologicky a aplikačne sľubné považujem aj:
- rozšírenie seed priestoru a ďalších diagnostických okruhov,
- porovnanie viacerých modelov a viacerých architektúr riadenia simulácie,
- využitie longitudinálneho alebo replikačného dizajnu,
- rozšírenie hodnotenia o hlasovú a obrazovú rovinu a o nonverbálne signály,
- testovanie, či sa na základe expert feedbacku dá systém iteratívne zlepšovať,
- overenie, ako simulácie najlepšie integrovať do supervízie, debriefingu a existujúceho kurikula tak, aby zostali doplnkom, nie náhradou reálnej praxe.

### 4.9 Záver diskusie

Predkladaná práca ukazuje, že AI-generované simulované interview s depresívnou symptomatikou možno skúmať ako legitímny metodologický objekt psychologického výskumu. Ich kvalita nie je jednorozmerná a nemožno ju redukovať na plynulosť jazyka. Dôležitá je aj klinická logika, vnútorná konzistentnosť, symptomatická primeranosť a neprítomnosť defektov. Pilotné zistenia naznačujú, že cielená kontrola generovania môže byť významným faktorom kvality a že odborné hodnotenie hodnotiteľmi je vhodnou cestou, ako túto kvalitu transparentne a systematicky posudzovať.
