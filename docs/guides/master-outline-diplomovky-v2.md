# Master Outline diplomovej práce (v2)

> Tento brief je lokálny pracovný rámec pre drafting diplomovej práce v štýle PEVŠ.
> Ak vznikne konflikt, prednosť má `docs/guides/sprievodca-zaverecnych-prac.md`, potom `AGENTS.md`.

## Účel dokumentu

Tento brief slúži ako záväzný pracovný rámec pre AI agenta pri písaní diplomovej práce. Cieľom je zabezpečiť, aby práca mala jednotnú logiku, primeraný rozsah, konzistentnú terminológiu a aby sa neoddelili teoretická a empirická línia.

Práca má byť písaná ako jeden prepojený celok podľa logiky:

**Úvod → Metóda → Výsledky → Diskusia**

## 1. Základná logika práce

### 1.1 Hlavné pravidlo

Každá sekcia musí mať jasnú funkciu. Do práce nepatrí text len preto, že sa to patrí.

Každá podkapitola má neskôr podporiť aspoň jednu z týchto vecí:
- výskumný problém,
- výskumnú otázku alebo hypotézu,
- operacionalizáciu premennej,
- interpretáciu výsledkov.

### 1.2 Čomu sa vyhnúť

- oddeleniu „teoretickej“ a „empirickej“ časti bez väzieb,
- prehľadu literatúry ako sledu parafráz bez vedúcej línie,
- pojmovému rámcu, ktorý je len zoznamom metód merania,
- výsledkom, ktoré sú zoradené podľa toho, čo sa dalo najľahšie vypočítať,
- dopĺňaniu nových analýz len preto, že existujú v metodických materiáloch.

## 2. Cieľový rozsah práce

Odporúčaný rozsah hlavného textu:

- **Úvod:** 24–30 strán
- **Metóda:** 10–14 strán
- **Výsledky:** 22–28 strán
- **Diskusia:** 10–14 strán

### Cieľ spolu

**66–86 strán čistého jadra** od Úvodu po koniec Diskusie.

Optimálny cieľ:
**70–85 strán hlavného textu** bez príloh.

## 3. Odporúčaná kostra práce

### 1 Úvod

#### Cieľ sekcie

Vybudovať argumentačný funnel od širšieho kontextu k presne formulovanému výskumnému problému, pojmovému rámcu a otázkam alebo hypotézam.

#### Odporúčané podkapitoly

##### 1.1 AI v psychológii a pomáhajúcich profesiách
- širší odborný kontext,
- význam témy,
- prečo je AI v psychologickom prostredí relevantná.

##### 1.2 Generatívna AI a simulácia komunikácie
- čo je AI-generovaný rozhovor,
- ako sa líši od bežného chatbot outputu,
- prečo je metodicky zaujímavý.

##### 1.3 Depresívna symptomatológia ako rámec simulovaného interview
- stručné klinicky relevantné ukotvenie,
- len tie aspekty, ktoré sú potrebné pre seed scenáre a interview domény,
- jasné prepojenie na `A1-A9`.

##### 1.4 Štandardizované prípadové scenáre / seedy ako metodický nástroj
- prečo nejde o náhodné prompty,
- prečo majú byť vstupy štandardizované,
- prečo je to dôležité pre porovnateľnosť rozhovorov.

##### 1.5 Kvalita AI-generovaných rozhovorov
- definovať hlavné hodnotené dimenzie,
- napr. klinická vierohodnosť, konzistentnosť, prirodzenosť, zhoda so seed profilom, bezpečnosť,
- jasne ukázať, ktoré dimenzie budú neskôr outcome-mi.

##### 1.6 Expert rating ako spôsob validácie
- zdôvodniť výber expertov,
- vysvetliť, prečo expert judgment dáva zmysel v pilotnej metodologickej štúdii.

##### 1.7 Pojmový rámec výskumného problému
- stručná syntéza,
- definovať všetky kľúčové teoretické premenné,
- nesmie ísť iba o zoznam nástrojov alebo škál.

##### 1.8 Cieľ výskumu, výskumné otázky a hypotézy
- formulovať menej, ale silnejších analytických blokov,
- poradie otázok a hypotéz musí zodpovedať poradiu ich riešenia vo Výsledkoch,
- nemiešať teoretický a empirický jazyk.

#### Pravidlá pre Úvod

- explicitne zdôvodniť dôležitosť problému,
- identifikovať gap v poznaní,
- zachovať vedúcu teoretickú myšlienku,
- nepoužívať príliš veľa mikro-VO a mikro-VH,
- neuvádzať nové premenné až vo výskumných otázkach, ak predtým neboli vysvetlené v texte,
- nepoužívať dlhé odseky postavené na jednej citácii.

### 2 Metóda

#### Cieľ sekcie

Presne, replikovateľne a logicky opísať dizajn, výber, materiál, operacionalizáciu, procedúru a analýzy.

#### Odporúčané podkapitoly

##### 2.1 Výskumný dizajn
- pomenovať typ štúdie,
- napr. pilotná metodologická kvantitatívna štúdia s expert-rated hodnotením AI-generovaných interview transkriptov.

##### 2.2 Materiál a tvorba interview korpusu
- seedy,
- pravidlá generovania,
- modelové podmienky,
- guardraily,
- počet rozhovorov,
- pravidlá quality control.

##### 2.3 Populácia, výber a výskumný súbor

Poradie má byť logické:
1. populácia,
2. spôsob výberu,
3. reálny súbor.

Treba presne uviesť:
- koho sa výskum týka,
- inklúzne a exklúzne kritériá,
- spôsob výberu,
- veľkosť súboru,
- návratnosť, ak je relevantná,
- odhad potrebnej veľkosti súboru, ak bol realizovaný.

Pri tejto práci je odporúčané rozlíšenie:
- **súbor rozhovorov**,
- **súbor expert hodnotiteľov**.

##### 2.4 Hodnotiaci nástroj a operacionalizácia

Pri každej premennej uviesť:
- teoretický význam,
- presnú podobu položky alebo kompozitu,
- odpoveďový formát,
- spôsob skórovania,
- analytické použitie.

Operacionalizácia má byť ideálne v prehľadnej tabuľke.

Odporúčaný rozsah popisu premennej:
- názov,
- typ premennej,
- hodnoty,
- reverzné položky,
- spôsob tvorby indexu,
- väzba na hypotézu alebo analytický blok.

##### 2.5 Procedúra
- ako boli rozhovory generované,
- ako boli vybrané,
- ako boli randomizované,
- ako boli priradené raterom,
- v akom poradí boli hodnotené,
- čo presne participant alebo rater videl a robil.

##### 2.6 Metódy analýzy dát

Nepísať formou holých odrážok bez zdôvodnenia.

Treba uviesť:
- ktoré analýzy boli použité,
- prečo boli použité,
- ako sa rozhodovalo pri chýbajúcich hodnotách,
- ako sa posudzovali distribúcie, odľahlé hodnoty a predpoklady modelov,
- ako sa hodnotila reliabilita,
- ako sa riešila zhoda hodnotiteľov,
- aký bol plán pre hlavné a sekundárne analýzy.

##### 2.7 Etické aspekty výskumu
- písať len to, čo bolo reálne urobené,
- stručne a vecne,
- uviesť informovaný súhlas, anonymizáciu, ochranu dát a schválenie, ak existuje.

#### Pravidlá pre Metódu

- jednotka analýzy musí byť pomenovaná konzistentne,
- spôsob výberu nesmie byť terminologicky nesprávne označený,
- sociodemografické premenné uvádzať len tie, ktoré majú vzťah k problému,
- rozdelenie participantov podľa sociodemografických znakov patrí do Metódy, nie až do Výsledkov,
- etická sekcia nesmie obsahovať fiktívne alebo neoverené tvrdenia.

### 3 Výsledky

#### Cieľ sekcie

Prezentovať výsledky v poradí, ktoré priamo sleduje logiku cieľov, otázok a hypotéz.

#### Odporúčané poradie

##### 3.1 Popis interview korpusu
- počet rozhovorov,
- počet seedov,
- počet podmienok,
- základné charakteristiky.

##### 3.2 Základné deskriptíva ratingového nástroja
- opis dát,
- rozdelenie odpovedí,
- priemery, `SD`, mediány, `IQR` podľa typu premennej.

##### 3.3 Kvalita merania
- vnútorná konzistencia,
- reliabilita škál,
- zhoda hodnotiteľov.

##### 3.4 Hlavné výsledky podľa hypotéz a otázok
- riešiť v tom istom poradí, v akom sú uvedené v Úvode,
- najprv hlavné hypotézy,
- potom sekundárne analýzy,
- explorácie až na konci.

##### 3.5 Doplnkové analytické bloky

Len ak sú vopred zdôvodnené:
- rozdiely medzi seedmi,
- rozdiely medzi generatívnymi podmienkami,
- vzťahy medzi ratingovými dimenziami,
- prediktory celkovej kvality,
- exploratory bloky.

#### Čo patrí do textu, tabuľky a grafu

- menej ako 3 údaje → text,
- 4 až 20 údajov → tabuľka,
- veľa údajov alebo profilové porovnania → graf.

#### Pravidlá reportovania

- používať konzistentný zápis čísel,
- používať konkrétne `p`-hodnoty,
- nepoužívať anglické názvy premenných, počítačové názvy ani SPSS labely v texte alebo v grafoch,
- nezahltiť text číslami, ale zachovať interpretačnú logiku,
- zachovať poradie: opis dát → kvalita merania → hlavné hypotézy → sekundárne analýzy → explorácie.

#### Formálna úprava tabuliek a grafov podľa sprievodcu

- číslo a názov patria nad objekt a majú byť zarovnané na ľavú stranu,
- číslo tabuľky alebo grafu má byť tučné,
- názov má byť kurzívou na samostatnom riadku pod číslom,
- každá tabuľka a každý graf musia byť explicitne spomenuté v texte,
- tabuľka alebo graf majú byť čitateľné aj bez dlhého dovysvetľovania v hlavnom texte,
- všetky názvy stĺpcov, osí, legiend a položiek majú byť v jazyku práce, nie ako surový export zo štatistického programu,
- neštandardné skratky a označenia treba vysvetliť v poznámke pod objektom; bežné štatistické skratky ako `M`, `SD`, `F`, `t`, `df`, `p`, `N` alebo `r` znovu nevysvetľovať,
- pri tabuľkách preferovať horizontálne oddeľovače a bezdôvodne nepoužívať zvislé čiary,
- pri grafoch držať čitateľné písmo a nepoužiť graf len preto, že ho vie exportovať software.

#### Čomu sa vyhnúť

- novým analýzam, ktoré nie sú naviazané na cieľ alebo hypotézy,
- technickým štatistickým vetvám len preto, že existujú v metodických materiáloch,
- automatickému pridaniu `K-Means` alebo inej typológie bez silného dôvodu.

##### Poznámka k aktuálnej práci

Jadrom analytického plánu majú zostať:
- reliabilita,
- `ICC`,
- `LMM`,
- ordinal mixed models.

**`K-Means` nepridávať ako novú vetvu len preto, že existuje návod.**

### 4 Diskusia

#### Cieľ sekcie

Interpretovať výsledky a uzavrieť argumentačnú slučku medzi teóriou, metódou a výsledkami.

#### Odporúčané podkapitoly

##### 4.1 Interpretácia hlavných zistení
- čo sa zistilo,
- čo to znamená vzhľadom na literatúru a cieľ práce.

##### 4.2 Metodologický prínos práce
- veľmi dôležité pre túto tému,
- vysvetliť, čo práca prináša pre generovanie a hodnotenie AI rozhovorov.

##### 4.3 Limity práce
- model dependence,
- počet raterov,
- seed dependence,
- jazyková a ekologická validita,
- obmedzenia dizajnu.

##### 4.4 Praktické implikácie
- výskum,
- metodika,
- budúce využitie rating pipeline,
- prípadne výučba alebo ďalšie validačné kroky.

##### 4.5 Budúce výskumné zámery
- replikácia,
- viac modelov,
- viac jazykov,
- porovnanie s ľudskými rozhovormi,
- rozšírenie ratingových nástrojov.

#### Pravidlá pre Diskusiu

- nesmie len opakovať výsledky,
- interpretácia musí nadväzovať na Úvod,
- tvrdenia nesmú byť silnejšie, než umožňujú dáta,
- vyhnúť sa emocionálne podfarbeným formuláciám a nadmernej sebaidentifikácii autora.

## 4. Formulácia výskumných otázok a hypotéz

### Povinné pravidlá

- neformulovať veľké množstvo drobných VO a VH,
- neformulovať VO a VH duplicitne,
- poradie VO a VH musí zodpovedať poradiu ich riešenia vo Výsledkoch,
- nespájať do jednej otázky viacero logických krokov,
- k hypotézam pripojiť relevantné zdroje ešte pred alebo pri ich zdôvodnení,
- ak sa vo výsledkoch objaví multivariačný model, musí byť naň vopred pripravený analytický blok v Úvode alebo Metóde.

### Jazykové pravidlo

Teoretický jazyk patrí do Úvodu.
Empirický jazyk patrí do Metódy a Výsledkov.

Nemiešať napríklad:
- teoretický konštrukt,
- dimenziu nástroja,
- sumačný index,
- modelový outcome,
ako keby to bola tá istá vec.

## 5. Jazyk a štýl

### Píš takto

- odborne,
- presne,
- stručne,
- s jasnou vedúcou líniou,
- s konzistentnou terminológiou.

### Nepíš takto

- dlhé vety,
- vatové odseky,
- opakovanie tej istej myšlienky inými slovami,
- nadbytočné detaily z citovaných štúdií,
- antropomorfizmus,
- časté striedanie času,
- viacero názvov pre ten istý konštrukt.

### Konzistencia terminológie

Každý hlavný konštrukt má mať:
- jeden preferovaný názov,
- prípadne raz zavedenú skratku,
- potom už konzistentné používanie naprieč celou prácou.

## 6. Čo má Codex robiť pri draftingu

Pri každej sekcii má agent vykonať tieto kroky:

1. **Najprv identifikovať funkciu sekcie.**
2. **Potom napísať stručnú osnovu.**
3. **Až potom draftovať text.**
4. **Po dopísaní vykonať audit:**
   - nadväzuje sekcia na cieľ práce?
   - zavádza len premenné, ktoré budú ďalej použité?
   - je terminológia konzistentná?
   - zodpovedá poradie sekcií analytickej logike?
   - neobjavila sa nová analýza bez dôvodu?

## 7. STOP pravidlá pre agenta

Agent má zastaviť drafting a explicitne označiť problém, ak nastane niektorá z týchto situácií:

- v texte sa objaví nová premenná, ktorá nebola predtým zavedená,
- hypotézy a výsledky sa prestanú zhodovať v poradí,
- Metóda neumožňuje replikáciu,
- analýza je navrhnutá bez väzby na cieľ práce,
- etická sekcia by mala obsahovať tvrdenie, ktoré nie je overené,
- do výsledkov by sa mala zaradiť analýza len preto, že by mohla byť zaujímavá.

## 8. Špecifické pravidlo pre túto diplomovku

Pre aktuálnu tému treba priebežne kontrolovať, či sa nerozpojili tieto tri vrstvy:

- **teoretický rámec AI simulácií**,
- **definícia kvality rozhovoru**,
- **konkrétne outcome premenné a ratingové bloky**.

Ak sa tieto tri vrstvy prestanú prekrývať, agent musí text prepracovať.

## 9. Krátka verzia pokynu pre Codex

Použi túto logiku:

- Úvod = funnel + vedúca myšlienka + pojmový rámec + ciele + otázky/hypotézy
- Metóda = dizajn + materiál + výber + operacionalizácia + procedúra + analýzy + etika
- Výsledky = opis dát + kvalita merania + hlavné hypotézy + sekundárne analýzy + explorácie
- Diskusia = interpretácia + metodologický prínos + limity + implikácie + budúce smery

A dodrž tieto zásady:

- nič nepíš bez funkcie,
- nič nemeraj bez definície,
- nič neanalyzuj bez väzby na cieľ,
- nič netvrď silnejšie, než dovoľujú dáta.
