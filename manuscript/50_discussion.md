# 50 Discussion / Diskusia

> Táto kapitola je pripravená ako reálny diskusný draft. Je napísaná tak, aby sa po doplnení finálnych výsledkov dala relatívne ľahko preformulovať do Wordu so živými citáciami.

## 4 Diskusia

### 4.1 Stručné zhrnutie hlavných zistení

Cieľom diplomovej práce bolo pilotne metodologicky overiť kvalitu AI-generovaných simulovaných klinických interview s depresívnou symptomatikou a preskúmať, či sa ich kvalita mení v závislosti od experimentálne manipulovaných vlastností generovania. Výsledky ukázali, že **[doplniť 2–4 najdôležitejšie zistenia]**. V jadre teda práca naznačuje, že kvalita simulovaného AI rozhovoru nie je daná iba samotným modelom alebo seed scenárom, ale aj konkrétnym spôsobom riadenia generovania a mierou kontroly nad jeho variabilitou.

### 4.2 Interpretácia primárnych výsledkov

Prvým dôležitým okruhom výsledkov bola klinická plausibilita rozhovorov. Ak sa potvrdí priaznivý efekt guardrailu, možno to interpretovať tak, že explicitnejšie usmernenie generovania znižuje voľný drift a pomáha modelu držať sa symptomatického a komunikačného jadra seed scenára. Takýto efekt by bol metodologicky dôležitý, pretože naznačuje, že kvalita simulácie nie je len otázkou „silného modelu“, ale aj otázkou kontrolovaného návrhu generovania.

Ak sa zároveň ukáže, že guardrail znižuje aj defect index, je to prakticky ešte dôležitejší výsledok než samotné zvýšenie plausibility. Pre tréningové a výučbové použitie totiž nestačí, aby text pôsobil dobre na prvý dojem. Potrebné je aj to, aby neobsahoval kontradikcie, zjednodušenia alebo obsahové chyby, ktoré by mohli študenta alebo používateľa viesť k nesprávnym záverom.

Druhým kľúčovým okruhom je prirodzenosť jazyka. Ak sa preukáže, že rozvinutejší profil `R3` zvyšuje prirodzenosť rozhovoru, možno to chápať ako znak toho, že bohatšie a rozvinutejšie odpovede vytvárajú presvedčivejší dialóg. Zároveň však treba sledovať, či sa tým nezvyšuje aj miera defektov. Práve tento potenciálny trade-off medzi naturalness a kontrolou kvality je jedným z metodologicky najzaujímavejších momentov celej štúdie.

### 4.3 Interpretácia symptom fidelity výsledkov

Osobitne dôležitou časťou práce je symptom fidelity perspektíva. V nej sa kvalita rozhovoru neposudzuje len na základe dojmu, ale aj na základe zhody s vopred definovaným seed profilom. To je metodologicky silná stránka dizajnu, pretože umožňuje porovnávať rozhovory nielen ako celky, ale aj ako systematicky ukotvené varianty vo vzťahu k cieľovým symptomatickým anchorom.

Ak sa ukáže, že rozhovory s guardrailom majú nižšiu chybu voči seed anchorom, podporuje to predstavu, že guardrail nepôsobí iba ako štylistický regulátor, ale aj ako mechanizmus zvyšujúci obsahovú presnosť. Ak by sa však ukázalo, že rozdiely sú malé alebo nestabilné, znamenalo by to, že symptomatická presnosť ostáva aj pri kontrolovanom prompting-u krehkou a môže si vyžadovať ďalšie vrstvy riadenia, napríklad explicitnejšie pravidlá pre disclosure alebo kontrolné validačné kroky.

Zaujímavé je aj to, ktoré symptomatické domény vychádzajú stabilne a ktoré nie. Predpokladateľne sa môžu lepšie generovať tie oblasti, ktoré sa dajú vyjadriť jazykovo priamo a často sa objavujú vo verejnom diskurze, zatiaľ čo jemnejšie oblasti, ako napríklad psychomotorika, funkčný dopad alebo pasívne myšlienky na smrť bez explicitnej dramatizácie, môžu byť pre model náročnejšie na konzistentné uchopenie.

### 4.4 Tréningová použiteľnosť a vnímaný pôvod rozhovoru

Pre praktické využitie výsledkov je kľúčové, či sú rozhovory vnímané ako použiteľné na tréningové a výučbové účely. Ak sa ukáže, že vyššia plausibilita a nižší defect index sú spojené s vyššou tréningovou použiteľnosťou, potvrdzuje to logiku, že kvalita simulácie nie je samoúčelná, ale priamo súvisí s tým, či má materiál didaktickú hodnotu.

Podobne zaujímavá je aj otázka vnímaného pôvodu rozhovoru. Ak rozhovory s vyššou plausibilitou a nižším defect indexom menej často vyzerajú ako `ai_generated`, naznačuje to, že odborníci pri odhadovaní pôvodu zrejme nereagujú len na povrchové jazykové znaky, ale aj na hlbšiu konzistentnosť a klinickú logiku textu. Ak by sa však takéto prepojenie nepotvrdilo, bolo by to rovnako dôležité zistenie, pretože by naznačovalo, že vnímanie „AI-ovosti“ textu sa môže opierať aj o iné kvality než tie, ktoré sme merali ako primárne outcome-y.

### 4.5 Porovnanie s literatúrou

Výsledky práce je potrebné interpretovať v širšom kontexte troch oblastí literatúry. Prvou sú práce o štandardizovaných prípadoch, vinietach a modelových materiáloch vo výučbe a výskume. Tieto práce dlhodobo ukazujú, že štandardizácia je užitočná, ale vždy sa pohybuje v napätí s prirodzenosťou a ekologickou validitou [@placeholder_vignettes_training]. Zistenia predkladanej práce na tento problém nadväzujú, ale prenášajú ho do prostredia generatívnej AI.

Druhou oblasťou sú práce o generatívnej AI a kvalite textových výstupov. Tie spravidla zdôrazňujú, že jazyková plynulosť neznamená automaticky obsahovú správnosť a že aj veľmi presvedčivý text môže obsahovať nekonzistentnosti alebo halucinácie [@placeholder_hallucination_or_clinical_llm]. Ak sa v našich výsledkoch objavia red-flag chyby aj pri jazykovo plynulých rozhovoroch, bude to s týmito zisteniami v zhode.

Treťou oblasťou sú metodologické práce o hodnotení kvality meracích a simulačných materiálov odborníkmi. Predkladaná práca k nim prispieva tým, že nepoužíva iba celkový dojem, ale kombinuje primárne kvalitatívne ratingy, symptom fidelity logiku a defect dimenziu. Práve toto viacvrstvové hodnotenie považujem za jeden z hlavných metodologických prínosov práce.

### 4.6 Limity výskumu

Predkladaná štúdia má viacero limitov. Prvým je **pilotný charakter výskumu**. To znamená, že výsledky treba interpretovať opatrne, najmä pokiaľ ide o stabilitu efektových odhadov a možnosti širšieho zovšeobecnenia.

Druhým limitom je **počet hodnotiteľov**. Hoci expert rating prináša vysokú obsahovú hodnotu, malý alebo stredne veľký počet raterov prirodzene obmedzuje presnosť odhadov interrater reliability a zvyšuje citlivosť výsledkov na individuálne hodnotiace štýly.

Tretím limitom je **účelový výber hodnotiteľov**. Výskumný súbor nebol reprezentatívnou vzorkou všetkých odborníkov, ale skupinou expertov ochotných zapojiť sa do hodnotenia. To je pri pilotnej metodologickej štúdii pochopiteľné, ale zároveň to obmedzuje možnosti širšieho zovšeobecnenia.

Štvrtým limitom je samotná povaha stimulusového materiálu. Hodnotené boli **simulované textové interview**, nie reálne klinické rozhovory a nie multimodálne interakcie. V textovej simulácii chýbajú neverbálne prejavy, intonácia, tempo reči a ďalšie jemné signály, ktoré v reálnej klinickej situácii ovplyvňujú dojem z klienta aj interpretáciu symptomatiky.

Piatym limitom je **modelová a promptová závislosť výstupov**. Výsledky sa vzťahujú na konkrétnu konfiguráciu seedov, promptingu a experimentálnych presetov. Pri inom modeli alebo inom nastavení generovania by mohli vyzerať odlišne.

### 4.7 Praktické a metodologické dôsledky

Napriek uvedeným limitom má práca viacero praktických a metodologických dôsledkov. Po prvé, ukazuje, že AI-generované simulované interview možno hodnotiť systematicky a viacvrstvovo, nie iba intuitívne. Po druhé, naznačuje, že kvalita takýchto výstupov sa dá experimentálne zlepšovať cez kontrolu generovania. Po tretie, vytvára rámec, ktorý môže byť využitý aj pri ďalších témach, nielen pri depresívnej symptomatike.

Z praktického hľadiska môže byť výstup práce zaujímavý najmä pre:
- tréning a výučbu psychologického interview,
- pilotovanie ratingových nástrojov,
- prípravu štandardizovaných prípadov,
- metodologický výskum kvality AI-generovaných psychologických materiálov.

Z metodologického hľadiska považujem za dôležité, že práca kombinuje tri úrovne posudzovania: celkovú kvalitu, fidelity voči seed anchorom a defect perspektívu. Táto kombinácia znižuje riziko, že kvalitu rozhovoru budeme hodnotiť iba na základe jazykovej plynulosti alebo iba na základe formálne správneho symptom checklistu.

### 4.8 Odporúčania pre ďalší výskum

Budúci výskum by mal rozšíriť počet hodnotiteľov, spresniť anchorovanie niektorých domén a overiť, do akej miery sú zistenia replikovateľné pri inom modeli alebo inom prompting-u. Zaujímavým ďalším krokom by bolo aj porovnanie AI-generovaných simulovaných interview s ľudsky simulovanými rozhovormi alebo s iným typom štandardizovaných prípadov.

Za metodologicky sľubné považujem aj:
- rozšírenie seed priestoru,
- porovnanie viacerých modelov,
- využitie longitudinálneho alebo replikačného dizajnu,
- rozšírenie hodnotenia o multimodálnu rovinu,
- testovanie, či sa na základe expert feedbacku dá systém iteratívne zlepšovať.

### 4.9 Záver diskusie

Predkladaná práca ukazuje, že AI-generované simulované interview s depresívnou symptomatikou možno skúmať ako legitímny metodologický objekt psychologického výskumu. Ich kvalita nie je jednorozmerná a nemožno ju redukovať na plynulosť jazyka. Dôležitá je aj klinická logika, vnútorná konzistentnosť, symptom fidelity a neprítomnosť defektov. Pilotné zistenia naznačujú, že cielená kontrola generovania môže byť významným faktorom kvality a že odborné human-rated hodnotenie je vhodnou cestou, ako túto kvalitu transparentne a systematicky posudzovať.
