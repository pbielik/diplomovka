# Thesis Writing Materials v Markdowne

> Posledná aktualizácia: 2026-03-30
> Tieto podklady sú pracovné a pomocné. Pri používaní má prednosť `docs/guides/sprievodca-zaverecnych-prac.md` a pravidlá v `AGENTS.md`.

## Čo je v balíku

| Súbor | Pôvodný zdroj | O čom je | Ako to čítať |
| --- | --- | --- | --- |
| `skdp-uvod-dojmy-1.md` | PDF | najčastejšie chyby v úvode, prehľade literatúry, pojmovom rámci a pri práci so štúdiami | skôr checklist než súvislý text |
| `skdp-uvod-dojmy-2.md` | PDF | formulácia výskumných otázok a hypotéz, pravidlá vedeckého štýlu | vhodné na redakčný pass pred odovzdaním draftu |
| `skdp-metoda.md` | PDF | checklist k metóde: výberový súbor, operacionalizácia, meranie, procedúra, analýzy, etika, preklad nástroja | veľmi silný auditný podklad pre `30_method.md` |
| `sekcia-iii-postupy-analyz.md` | PDF | rýchla mapa analytických postupov a ich účelu | dobré ako orientačná pomôcka pre Results |
| `reportovanie-vysledkov.md` | PPTX | formálne pravidlá reportovania čísel, tabuliek, grafov a jazyka | užitočné pri finalizácii výsledkov a tabuliek |
| `multivariacna-statistika.md` | PPTX | lineárna a viacnásobná regresia, predpoklady, multikolinearita, stručný úvod ku K-Means | relevantné len tam, kde to sedí s analytickým plánom |
| `k-means-navod-spss.md` | DOCX | praktický návod na K-Means v SPSS vrátane screenshotov a interpretácie výstupov | špecializovaný materiál, nie jadro tvojej aktuálnej práce |

## Hlavná syntéza

Tieto materiály nie sú jeden kurz, ale tri odlišné typy podkladov:

1. `skdp-uvod-dojmy-1.md`, `skdp-uvod-dojmy-2.md`, `skdp-metoda.md`
   Sú to kontrolné zoznamy častých chýb v diplomovkách. Najväčšia hodnota je v tom, že ukazujú, kde sa práce zvyknú rozpojiť medzi úvodom, hypotézami, metódou a výsledkami.

2. `reportovanie-vysledkov.md`, `sekcia-iii-postupy-analyz.md`
   Sú to podklady k logike výsledkov a k formálnemu reportovaniu. Pomáhajú rozhodnúť, čo má ísť do textu, čo do tabuľky, čo do grafu a ako číselné výsledky zapisovať.

3. `multivariacna-statistika.md`, `k-means-navod-spss.md`
   Sú to technickejšie materiály k štatistickým postupom. V tvojom repozitári sú užitočné skôr ako referenčné pozadie než ako priamy plán analýzy.

## Kde to využiť v tvojej diplomovke

### `manuscript/20_introduction.md`

Najviac použi:
- `skdp-uvod-dojmy-1.md`
- `skdp-uvod-dojmy-2.md`

Konkrétne na kontrolu:
- či všeobecný úvod jasne zdôvodňuje význam problému a medzeru v poznaní,
- či prehľad literatúry vedie k tvojej téme a nie je len sledom parafráz,
- či pojmový rámec definuje všetky kľúčové konštrukty, ktoré sa potom objavia v hypotézach,
- či H1-H6 idú v rovnakom poradí, v akom budú riešené vo výsledkoch,
- či štýl ostáva odborný, stručný a bez zbytočne dlhých viet.

Pre tvoju tému je to dôležité hlavne preto, že úvod už máš silný, ale stále sa môže rozpojiť medzi:
- teoretickým rámcom AI simulácií,
- definíciou kvality rozhovoru,
- a konkrétnymi outcome-mi `G1-G5`, `A1-A9`, `R1-R5`.

### `manuscript/30_method.md`

Najviac použi:
- `skdp-metoda.md`
- `sekcia-iii-postupy-analyz.md`

Konkrétne na kontrolu:
- či je presne a replikovateľne opísaný výber raterov,
- či je jednotka analýzy pomenovaná konzistentne,
- či operacionalizácia kompozitov a položiek sedí s codebookom a hypotézami,
- či opis analýz vysvetľuje aj rozhodnutia o reliabilite, ICC a mixed-effects modeloch,
- či etická sekcia hovorí len to, čo bolo reálne urobené.

Pre tvoju tému je toto momentálne najpraktickejší materiál z celého balíka.

### `manuscript/40_results.md`

Najviac použi:
- `sekcia-iii-postupy-analyz.md`
- `reportovanie-vysledkov.md`
- čiastočne `multivariacna-statistika.md`

Konkrétne na kontrolu:
- poradie prezentácie: opis dát, reliabilita, hlavné hypotézy, sekundárne analýzy, explorácie,
- ktoré výsledky majú ísť do textu a ktoré do tabuliek alebo grafov,
- ako zapisovať priemery, SD, mediány, IQR, p-hodnoty a názvy štatistík,
- ako nezahltiť kapitolu číslami a pritom nestratiť interpretačnú logiku.

Pre tvoju prácu je dôležité neprevziať z týchto materiálov nové analýzy len preto, že existujú. Ak analýza nie je naviazaná na cieľ, H1-H6 alebo explicitný exploratory blok, nepatrí do Results.

### `manuscript/50_discussion.md`

Tieto materiály pomáhajú nepriamo:
- `skdp-uvod-dojmy-1.md` pri návrate k literatúre a k vedúcej myšlienke,
- `skdp-uvod-dojmy-2.md` pri vedeckom štýle a pri vyhnutí sa prehnaným formuláciám.

Na diskusiu však tento balík nie je hlavný zdroj. Tam bude dôležitejšia tvoja vlastná literatúra a výpisky v `notes/literature/`.

### `analysis/` a analytický plán

Najviac použi:
- `sekcia-iii-postupy-analyz.md`
- `multivariacna-statistika.md`
- `k-means-navod-spss.md` len ak by si niekedy robil samostatnú exploráciu typológií

V aktuálnom stave repa z toho plynie:
- regresné a K-Means materiály sú skôr referenčné pozadie,
- jadrom tvojej aktuálnej analytickej línie ostávajú reliabilita, ICC, LMM a ordinal mixed models,
- K-Means teraz nepridávaj ako novú vetvu len preto, že existuje návod.

## Odporúčaný pracovný postup

1. Pri každom väčšom prepise najprv otvor `docs/guides/sprievodca-zaverecnych-prac.md`.
2. Potom použi `skdp-uvod-dojmy-1.md` a `skdp-uvod-dojmy-2.md` na redakčný pass úvodu.
3. Pred finalizáciou metódy prejdi `skdp-metoda.md` ako checklist bod po bode.
4. Po prvých reálnych výstupoch z pipeline použi `reportovanie-vysledkov.md` a `sekcia-iii-postupy-analyz.md` pri skladaní Results.
5. Technickejšie štatistické materiály používaj len vtedy, keď podporujú už existujúci analytický plán.

## Poznámky ku konverzii

- Konverzia zachováva text použiteľný na čítanie a vyhľadávanie, nie perfektné formátovanie.
- `k-means-navod-spss.md` má prenesené aj obrázky do priečinka `k-means-navod-spss-assets/`.
- Pri niektorých slide deckoch ostali slidy bez textovej vrstvy ako `_No visible text found._`.
