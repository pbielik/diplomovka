# AGENTS.md

Tento repozitár slúži na prípravu diplomovej práce z psychológie.

## Autoritatívne pravidlá pre štruktúru práce

1. Hlavná štruktúra rukopisu **musí byť podľa IMRaD**:
   - Introduction / Úvod
   - Method / Metóda
   - Results / Výsledky
   - Discussion / Diskusia

2. Pri návrhu alebo úpravách textu sa riaď lokálnymi sprievodcami:
   - `docs/guides/sprievodca-zaverecnych-prac.md`
   - `docs/guides/master-outline-diplomovky-v2.md`

3. Ak niečo v návrhu odporuje lokálnemu sprievodcovi, **prednosť má `docs/guides/sprievodca-zaverecnych-prac.md`**, potom `AGENTS.md`, potom `docs/guides/master-outline-diplomovky-v2.md`.

## Dodatočný drafting brief

- `docs/guides/master-outline-diplomovky-v2.md` je pracovný brief pre drafting, audit sekcií, odporúčaný rozsah a STOP pravidlá.
- Používaj ho najmä pri outline, väčšom rewrite alebo pri kontrole logiky medzi Úvodom, Metódou, Výsledkami a Diskusiou.
- Každá sekcia a podkapitola musí mať funkciu. Ak nevieš povedať, čomu konkrétne slúži, text tam pravdepodobne nepatrí.
- Nepoužívaj logiku „teoretická časť vs. empirická časť“. Práca má byť jeden prepojený celok.

## Cieľový rozsah hlavného textu

- Úvod: 24–30 strán
- Metóda: 10–14 strán
- Výsledky: 22–28 strán
- Diskusia: 10–14 strán
- cieľ spolu: 66–86 strán jadra, ideálne 70–85 strán bez príloh

## Obsah kapitol podľa sprievodcu

### Introduction
Má obsahovať:
- všeobecný úvod do problému
- prehľad literatúry
- pojmový rámec výskumného problému
- explicitne formulované ciele, výskumné otázky a hypotézy

### Method
Má obsahovať:
- populáciu a výberový súbor
- empirické premenné, empirické výskumné otázky a hypotézy
- metódy zberu dát
- výskumný dizajn (plán)
- spracovanie dát / procedúru

### Results
Má obsahovať:
- logiku prezentácie výsledkov
- frekvenčnú analýzu odpovedí na položky, ak je relevantná
- analýzu vnútornej konzistencie meracieho nástroja, ak je relevantná
- grafické znázornenie sumačných indexov, ak je relevantné
- deskriptívnu štatistiku
- riešenie výskumných otázok a hypotéz
- tabuľky a grafy len v rozsahu, ktorý je zmysluplný a nezdvojuje text

### Discussion
Má obsahovať:
- interpretáciu výsledkov
- diskusiu o limitoch výskumných metód
- diskusiu o dôsledkoch vyplývajúcich z výsledkov
- diskusiu o budúcich zámeroch

## Pravidlá pre citácie a literatúru

1. Zotero je hlavný zdroj pravdy pre literatúru.
2. V draftoch používaj citekey placeholdery, napr. `[@koo2016icc]`.
3. Finálne citácie sa vkladajú vo Worde cez Zotero plugin.
4. Všetky výpisky musia obsahovať odkaz na zdroj a krátku anotáciu.
5. Nepíš v draftoch ručne finálne APA citácie, ak sa text ešte bude prepisovať.
6. `docs/literature/literature_map_diplomovka.md` je centrálny rozcestník literature bundle; pri každej novej rešerši ho najprv skontroluj a potom otvor príslušný detailný súbor v `docs/literature/`.
7. Každý kľúčový zdroj priraď k tematickému klastru, priorite a funkcii v rukopise alebo metodike.

## Pravidlá pre písanie

- používaj odborný, ale čitateľný štýl
- vyhýbaj sa zbytočne dlhým vetám
- drž konzistentnú terminológiu
- každá sekcia musí mať vedúcu líniu a jasnú funkciu
- neoddeľuj teoretickú a empirickú líniu tak, aby sa prestali podopierať
- netvor nové analytické vetvy bez väzby na cieľ, otázky a hypotézy
- nové analýzy nepridávaj len na „nafúknutie“ výsledkov
- neuvádzaj nové premenné až vo VO/VH alebo vo Výsledkoch, ak neboli predtým vysvetlené
- nepreťažuj text dlhými odsekmi postavenými na jednej citácii

## Pravidlá pre dáta a analýzu

- 1 riadok v hlavnom rating datasete = 1 hodnotenie jedného ratera na jednom transkripte
- surové dáta neprepisuj ručne; čisté dáta ukladaj do `analysis/data_clean/`
- analytické skripty ukladaj do `analysis/scripts/`
- tabuľky a grafy exportuj do `tables/` a `figures/`
- pri aktuálnej práci majú jadro analytického plánu tvoriť reliabilita, `ICC`, `LMM` a ordinal mixed models
- `K-Means` nepridávaj ako novú analytickú vetvu len preto, že existuje návod alebo metodický materiál

## Keď vytváraš nové súbory

- outline kapitol udržuj v `manuscript/`
- literárne výpisky dávaj do `notes/literature/`
- mapy literatúry a literárne workflow drž v `docs/literature/`
- meeting notes dávaj do `notes/meetings/`
- prompts ukladaj do `prompts/`

## Pravidlá pre dashboard a backlog

- aktuálny stav práce udržuj v `docs/aktualny-stav-diplomovky.md`
- operatívny backlog a dependency tracking udržuj v `docs/backlog-diplomovky.md`
- pri každej podstatnej zmene v `manuscript/`, `analysis/`, `references/`, `notes/` alebo workflow aktualizuj:
  - dátum poslednej aktualizácie,
  - stav dotknutej oblasti,
  - nové blokery alebo odblokovania,
  - najbližší konkrétny krok
- používaj iba statusy `todo`, `in_progress`, `blocked`, `done` alebo ich stručné slovenské ekvivalenty
- status `done` používaj len vtedy, keď existuje reálny artefakt v repo alebo finálny milestone vo Worde
- ak sa zmení dizajn, hypotézy, premenné alebo analytický plán, aktualizuj okrem rukopisu aj dashboard a backlog
- dashboard a backlog majú zostať krátke, vecné a dobre čitateľné na GitHube; preferuj tabuľky, checklisty a Mermaid len tam, kde zvyšujú prehľad

---

# AGENTS_APPENDIX_IMRAD_ZOTERO.md

Tento dodatok rozširuje `AGENTS.md` o presné pravidlá pre:
- používanie lokálneho sprievodcu,
- prácu s draftmi podľa IMRaD,
- používanie Zotera a Better BibTeX,
- spracovanie literatúry a citekeys,
- bezpečné prepisovanie textu bez rozbitia citácií.

## 1. Hierarchia pravidiel

Pri návrhu, úprave alebo reorganizácii textu sa riaď touto prioritou:

1. `docs/guides/sprievodca-zaverecnych-prac.md`
2. `AGENTS.md`
3. `docs/guides/master-outline-diplomovky-v2.md`
4. tento dodatok
5. aktuálne drafty v `manuscript/`

Ak vznikne konflikt, **prednosť má lokálny sprievodca**.

## 2. Povinný IMRaD režim

Diplomová práca sa musí držať modelu **IMRaD**.

Povolené hlavné sekcie rukopisu:
- `20_introduction.md`
- `30_method.md`
- `40_results.md`
- `50_discussion.md`

Doplňujúce sekcie sú prípustné len ako servisné alebo formálne časti:
- názov a abstrakt,
- záver,
- zoznam literatúry,
- prílohy.

Nepoužívaj logiku „teoretická časť“ vs. „praktická časť“, ak by tým vzniklo oddelenie teórie od empirickej línie výskumu.
Úvod musí viesť k cieľu, otázkam a hypotézam.
Metóda musí byť replikovateľná.
Výsledky musia riešiť len to, čo bolo pripravené v úvode a metóde.
Diskusia musí interpretovať výsledky vo väzbe na literatúru, limity a implikácie.

## 3. Pravidlá pre úvod

V `20_introduction.md` musí byť zachovaná táto logika:

1. všeobecné uvedenie do problému,
2. prehľad literatúry,
3. pojmový rámec,
4. priblíženie metodologických a empirických východísk,
5. cieľ práce,
6. výskumné otázky a/alebo hypotézy.

Nepridávaj nové podtémy, ktoré nie sú potrebné pre:
- pochopenie výskumného problému,
- voľbu metódy,
- interpretáciu budúcich výsledkov.

Každý odsek v úvode by mal mať aspoň jednu z týchto funkcií:
- definovať pojem,
- ukotviť teóriu,
- ukázať medzeru v poznaní,
- zdôvodniť premennú alebo dizajn,
- pripraviť cieľ, otázku alebo hypotézu.

## 4. Pravidlá pre metódu

V `30_method.md` musí byť text písaný tak, aby:
- bol replikovateľný,
- obsahoval len skutočne použité postupy,
- neobsahoval analytické ambície, ktoré nebudú vo výsledkoch splnené.

Povinné bloky:
- charakter výskumu a dizajn,
- výskumný súbor,
- výskumný materiál,
- hodnotiaci nástroj,
- premenné,
- procedúra,
- spracovanie dát a štatistická analýza,
- etické aspekty.

Ak sa zmení dizajn, premenné alebo analytický plán, aktualizuj:
1. metódu,
2. hypotézy,
3. výsledkové šablóny,
4. prípadne aj úvod, ak sa mení výskumný problém.

## 5. Pravidlá pre výsledky

`40_results.md` nesmie obsahovať:
- literárny prehľad,
- rozsiahle teoretické interpretácie,
- nové hypotézy vytvorené až po analýze.

Vo výsledkoch:
- najprv opíš dáta,
- potom reliabilitu a základné vlastnosti merania, ak sú relevantné,
- potom hlavné analýzy podľa hypotéz,
- potom sekundárne a exploratórne analýzy.

Každá hlavná analytická vetva musí byť spätá s:
- cieľom,
- otázkou alebo hypotézou,
- definovanou premennou v metóde.

Nepoužívaj „výplňové“ analýzy len na rozšírenie rozsahu práce.

## 6. Pravidlá pre diskusiu

`50_discussion.md` musí mať túto logiku:
1. stručné zhrnutie hlavných zistení,
2. interpretácia vo vzťahu k literatúre,
3. metodologické limity,
4. praktické a teoretické implikácie,
5. odporúčania pre budúci výskum.

Diskusia nesmie byť len opakovaním výsledkov inými slovami.

Ak výsledok hypotézu nepodporí, nie je to chyba práce.
Treba ho:
- pomenovať,
- interpretovať opatrne,
- zasadiť do literatúry alebo limitov,
- neprezentovať ako zlyhanie výskumu.

## 7. Pravidlá pre Zotero

Zotero je **jediný zdroj pravdy** pre bibliografické údaje.

Povinné zásady:
- nové zdroje ukladaj najprv do Zotera,
- pred importom nového zdroja over, do ktorého klastru patrí v literature bundle v `docs/literature/`,
- pri zdrojoch používaj collections a jednoduché tagy podľa literature map,
- pri každom kľúčovom zdroji maj krátku poznámku alebo výpiskový súbor,
- bibliografické údaje neupravuj ručne v markdown draftoch, ak už existujú v Zotere.

Odporúčané kolekcie podľa literature map:
- `Diplomovka/01 Depresia a MDD`
- `Diplomovka/02 LLM, mental health a psychiatria`
- `Diplomovka/03 Validácia rating nástroja`
- `Diplomovka/04 Metóda, štatistika a analytický dizajn`
- `Diplomovka/05 Všeobecná metodológia psychologického výskumu`
- `Diplomovka/06 Kvalitatívne metódy (optional)`
- `Diplomovka/07 Etika a AI governance`
- `Diplomovka/99 Tools a guides (not core)`

Odporúčané tagy:
- `must-read`
- `should-read`
- `optional`
- `methods`
- `validation`
- `ethics`
- `llm`
- `depression`
- `seeding`
- `analysis`

## 8. Pravidlá pre citekeys

V pracovných draftoch používaj citekeys vo formáte:
- `[@obradovich2024llmpsychiatry]`
- `[@kroenke2001phq9]`

Nikdy nepíš ručne finálne citácie typu:
- `(Author, Year)`
ak sa text ešte bude meniť.

Povolené formy v draftoch:
- `[@citekey]`
- viac zdrojov: `[@citekey1; @citekey2]`

Citekeys majú byť:
- stabilné,
- bez diakritiky,
- bez medzier,
- malé písmená,
- ideálne `autorRokKlucoveSlovo`.

Ak sa citekey zmení v Zotere, oprav:
1. markdown drafty,
2. source mapy,
3. pomocné `.bib` seed súbory.

## 9. Better BibTeX workflow

Ak je aktívny Better BibTeX:
- udržiavaj export `references/zotero-thesis.bib`,
- citekeys v markdown musia sedieť s týmto exportom,
- seed `.bib` súbor slúži len ako pomocný most, nie ako finálny zdroj pravdy.

Ak existuje konflikt medzi seed `.bib` a reálnym Zotero exportom:
- prednosť má Zotero export,
- markdown drafty sa majú zosúladiť s finálnymi citekeys.

## 10. Literárne výpisky

Každý dôležitý zdroj by mal mať buď:
- Zotero note,
- alebo súbor v `notes/literature/`.

Odporúčaný formát výpisku:
- citekey,
- plná citácia,
- identifikátor alebo URL,
- klaster z literature map,
- priorita (`must-read`, `should-read`, `optional`),
- hlavná myšlienka,
- na čo sa zdroj použije v rukopise alebo metodike,
- kľúčový výsledok / definícia,
- limit alebo poznámka,
- status (`must-cite`, `maybe`, `discussion`, `method`).

Výpisky nemajú byť prepisom celého článku.
Majú byť krátke a použiteľné pri písaní.

## 11. Word workflow

Word je finálny priestor pre:
- živé Zotero citácie,
- finálnu bibliografiu,
- finálne formátovanie.

Repo nie je hlavný priestor pre verzovanie `.docx`.
Ak potrebuješ uložiť snapshot Word verzie, ukladaj ju ako:
- milestone,
- final submission,
- archive snapshot.

Drafty sa majú rozpracúvať primárne v markdown alebo textových súboroch v repozitári.

## 12. Keď agent upravuje text

Ak agent upravuje text:
- nesmie meniť výskumné otázky alebo hypotézy bez zodpovedajúcej úpravy v metóde a výsledkoch,
- nesmie pridávať nové zdroje bez označenia, kam ich treba zaradiť,
- nesmie rušiť citekeys bez náhrady,
- nesmie odstraňovať väzbu medzi odsekom a jeho citačnou oporou.

Pred draftingom alebo väčším rewrite musí agent:
1. identifikovať funkciu sekcie,
2. pripraviť stručnú osnovu,
3. až potom draftovať text,
4. po úprave vykonať audit väzieb na cieľ, premenné, hypotézy a poradie výsledkov.

Ak agent presúva odseky:
- zachová citekeys,
- zachová logiku IMRaD,
- skontroluje, či sa nezlomila nadväznosť medzi úvodom, metódou a výsledkami.

## 13. STOP pravidlá pre agenta

Agent musí zastaviť drafting a explicitne označiť problém, ak nastane niektorá z týchto situácií:
- v texte sa objaví nová premenná, ktorá nebola predtým zavedená,
- hypotézy a výsledky sa prestanú zhodovať v poradí,
- metóda neumožňuje replikáciu,
- analýza je navrhnutá bez väzby na cieľ práce,
- etická sekcia by mala obsahovať tvrdenie, ktoré nie je overené,
- do výsledkov by sa mala zaradiť analýza len preto, že by mohla byť zaujímavá.

## 14. Špecifická kontrola pre túto diplomovku

Pri každom väčšom zásahu treba skontrolovať, či sa nerozpojili tieto tri vrstvy:
- teoretický rámec AI simulácií,
- definícia kvality rozhovoru,
- konkrétne outcome premenné a ratingové bloky.

Ak sa tieto tri vrstvy prestanú prekrývať, text treba prepracovať.

## 15. Kontrolný checklist pred väčšou úpravou

Pred každou väčšou úpravou si over:
- Je zásah v súlade s IMRaD?
- Je zásah v súlade so sprievodcom?
- Má sekcia jasnú funkciu?
- Má každý nový odsek funkciu?
- Sú citekeys zachované?
- Neobjavila sa nová premenná bez zavedenia?
- Zodpovedá výsledková vetva cieľu a hypotézam?
- Zodpovedá poradie sekcií a hypotéz analytickej logike?
- Nepridávajú sa zbytočné analýzy?
- Zostáva metóda replikovateľná?
- Ostáva prepojenie medzi teoretickým rámcom AI simulácií, definíciou kvality a outcome premennými?

## 16. Kontrolný checklist pred exportom do Wordu

Pred presunom textu do Wordu skontroluj:
- placeholder citekeys sú platné,
- názvy kapitol zodpovedajú IMRaD,
- text neobsahuje interné poznámky typu TODO bez označenia,
- tabuľky a grafy majú jasný názov,
- metóda a výsledky používajú rovnaké názvy premenných,
- hypotézy a výsledky sa navzájom nevylučujú,
- vo výsledkoch sa nepoužívajú nepreložené SPSS labely alebo počítačové názvy premenných ako finálny jazyk práce.

## 17. Kontrolný checklist po každom väčšom zásahu

Po každom väčšom zásahu skontroluj:
- bol aktualizovaný `docs/aktualny-stav-diplomovky.md`, ak sa zmenil stav práce,
- bol aktualizovaný `docs/backlog-diplomovky.md`, ak sa zmenili priority alebo dependency,
- nezostal v texte nový placeholder bez jasného dôvodu,
- sedí stále väzba medzi úvodom, metódou, výsledkami a diskusiou,
- zostáva zachovaná jedna vedúca línia od problému po interpretáciu.
