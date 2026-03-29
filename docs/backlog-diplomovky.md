# Backlog diplomovky

> Posledná aktualizácia: 2026-03-29
> Používaj tento súbor ako operatívny backlog. Stav `done` patrí len položkám, ktoré majú jasný artefakt v repo alebo vo Word milestone.

## Prioritný backlog

| ID | Priorita | Stav | Úloha | Závisí od | Výstup |
| --- | --- | --- | --- | --- | --- |
| B01 | `P1` | `todo` | Nastaviť Better BibTeX auto-export do `references/zotero-thesis.bib` | Zotero kolekcia `Diplomovka` | aktuálny `.bib` export s platnými citekeys |
| B02 | `P1` | `todo` | Vytvoriť jadro literárnych výpiskov pre úvod a diskusiu | B01 nie je striktne nutné, ale pomáha | 8-12 súborov alebo Zotero notes pre kľúčové zdroje |
| B03 | `P1` | `todo` | Dostať reálny rating export do `analysis/data_clean/` | hotový zber alebo export zo survey engine | clean CSV pre ratingy a prípadné master tabuľky |
| B04 | `P1` | `todo` | Overiť finálne anchor hodnoty seedov a názvy premenných | B03 | konzistentné seedy a naming medzi CSV, metódou a R pipeline |
| B05 | `P1` | `todo` | Spustiť `analysis/scripts/thesis_rating_pipeline.R` na reálnych dátach | B03, B04 | `analysis/outputs/*.csv` s reálnymi výsledkami |
| B06 | `P1` | `todo` | Exportovať základné tabuľky a grafy do `tables/` a `figures/` | B05 | Tabuľka 1, reliabilita, modelové tabuľky, 2-3 hlavné grafy |
| B07 | `P1` | `todo` | Doplniť `manuscript/40_results.md` podľa reálnych výstupov | B05, B06 | plný draft Results bez analytických placeholderov |
| B08 | `P1` | `todo` | Prepísať `manuscript/50_discussion.md` podľa skutočných zistení | B07 | diskusia viazaná na reálne výsledky a literatúru |
| B09 | `P2` | `todo` | Doplniť finálne počty a procedural detail do `manuscript/30_method.md` | B03 | metóda bez procesných placeholderov |
| B10 | `P2` | `todo` | Finalizovať abstrakt a záver | B07, B08, B09 | finálny `10_title_abstract.md` a `60_conclusion.md` |
| B11 | `P2` | `todo` | Vytvoriť Word milestone draft so živými citáciami | B01, B07, B08, B10 | exportovateľný rukopis pre školiteľa |

## Závislosti a poradie práce

| Ak chceš spraviť toto | Najprv potrebuješ | Dá sa robiť paralelne? |
| --- | --- | --- |
| Finálny Results | clean dáta, pipeline, exporty | `nie` |
| Finálnu Discussion | výsledky a core literatúru | `čiastočne` |
| Finálny abstrakt | výsledky + záver práce | `nie` |
| Lepší Introduction | Zotero export a výpisky | `áno` |
| Čistejšiu Method | finálne počty a procedúru | `áno` |
| Word milestone | stabilné citekeys + dopísané IMRaD časti | `nie` |

## Najbližší odporúčaný sled

1. `B01` nastaviť Zotero export.
2. `B02` spraviť minimálne jadro výpiskov.
3. `B03` a `B04` pripraviť clean dáta a overiť naming.
4. `B05` a `B06` dostať z pipeline prvé reálne výstupy.
5. `B07` až `B10` dopísať manuscript.

## Definition of done pre kritické položky

- `B01` je hotové až vtedy, keď súbor `references/zotero-thesis.bib` reálne existuje a citekeys sedia s markdown draftmi.
- `B03` je hotové až vtedy, keď máš clean CSV v `analysis/data_clean/` a vieš ho bez ručných zásahov znovu vytvoriť.
- `B05` je hotové až vtedy, keď `analysis/outputs/` obsahuje reálne exporty z pipeline, nie iba placeholdery.
- `B07` je hotové až vtedy, keď v `40_results.md` nezostanú analytické placeholdery typu `[doplniť]`.
- `B08` je hotové až vtedy, keď diskusia interpretuje skutočné výsledky a neopiera sa o hypotetické formulácie.
