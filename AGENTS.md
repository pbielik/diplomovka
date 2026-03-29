# AGENTS.md

Tento repozitár slúži na prípravu diplomovej práce z psychológie.

## Autoritatívne pravidlá pre štruktúru práce

1. Hlavná štruktúra rukopisu **musí byť podľa IMRaD**:
   - Introduction / Úvod
   - Method / Metóda
   - Results / Výsledky
   - Discussion / Diskusia

2. Pri návrhu alebo úpravách textu sa riaď lokálnym sprievodcom:
   - `docs/guides/sprievodca-zaverecnych-prac.md`

3. Ak niečo v návrhu odporuje lokálnemu sprievodcovi, **prednosť má lokálny sprievodca**.

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

## Pravidlá pre písanie

- používaj odborný, ale čitateľný štýl
- vyhýbaj sa zbytočne dlhým vetám
- drž konzistentnú terminológiu
- netvor nové analytické vetvy bez väzby na cieľ, otázky a hypotézy
- nové analýzy nepridávaj len na „nafúknutie“ výsledkov

## Pravidlá pre dáta a analýzu

- 1 riadok v hlavnom rating datasete = 1 hodnotenie jedného ratera na jednom transkripte
- surové dáta neprepisuj ručne; čisté dáta ukladaj do `analysis/data_clean/`
- analytické skripty ukladaj do `analysis/scripts/`
- tabuľky a grafy exportuj do `tables/` a `figures/`

## Keď vytváraš nové súbory

- outline kapitol udržuj v `manuscript/`
- literárne výpisky dávaj do `notes/literature/`
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
3. tento dodatok
4. aktuálne drafty v `manuscript/`

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
- pri zdrojoch používaj collections a jednoduché tagy,
- pri každom kľúčovom zdroji maj krátku poznámku alebo výpiskový súbor,
- bibliografické údaje neupravuj ručne v markdown draftoch, ak už existujú v Zotere.

Odporúčané kolekcie:
- `Diplomovka/00 Core`
- `Diplomovka/01 Teória`
- `Diplomovka/02 Metóda`
- `Diplomovka/03 Štatistika`
- `Diplomovka/04 Diskusia`
- `Diplomovka/05 AI a simulácia`
- `Diplomovka/06 Depresia a interview`

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
- hlavná myšlienka,
- na čo sa zdroj použije,
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

Ak agent presúva odseky:
- zachová citekeys,
- zachová logiku IMRaD,
- skontroluje, či sa nezlomila nadväznosť medzi úvodom, metódou a výsledkami.

## 13. Kontrolný checklist pred väčšou úpravou

Pred každou väčšou úpravou si over:
- Je zásah v súlade s IMRaD?
- Je zásah v súlade so sprievodcom?
- Má každý nový odsek funkciu?
- Sú citekeys zachované?
- Zodpovedá výsledková vetva cieľu a hypotézam?
- Nepridávajú sa zbytočné analýzy?
- Zostáva metóda replikovateľná?

## 14. Kontrolný checklist pred exportom do Wordu

Pred presunom textu do Wordu skontroluj:
- placeholder citekeys sú platné,
- názvy kapitol zodpovedajú IMRaD,
- text neobsahuje interné poznámky typu TODO bez označenia,
- tabuľky a grafy majú jasný názov,
- metóda a výsledky používajú rovnaké názvy premenných,
- hypotézy a výsledky sa navzájom nevylučujú.

## 15. Kontrolný checklist po každom väčšom zásahu

Po každom väčšom zásahu skontroluj:
- bol aktualizovaný `docs/aktualny-stav-diplomovky.md`, ak sa zmenil stav práce,
- bol aktualizovaný `docs/backlog-diplomovky.md`, ak sa zmenili priority alebo dependency,
- nezostal v texte nový placeholder bez jasného dôvodu,
- sedí stále väzba medzi úvodom, metódou, výsledkami a diskusiou.
