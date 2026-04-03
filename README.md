# Diplomovka – repo starter

Tento repozitár je pripravený pre písanie diplomovej práce s workflow:

- **Zotero** = master databáza literatúry
- **Word** = finálny rukopis s živými citáciami
- **Repo** = drafty, výpisky, analýzy, tabuľky, grafy, prompty a pomocný `.bib` export

## Riadiace dokumenty
- [Aktuálny stav diplomovky](docs/aktualny-stav-diplomovky.md)
- [Backlog diplomovky](docs/backlog-diplomovky.md)
- [Literature review hub](docs/literature/literature_map_diplomovka.md)

## Základné pravidlo štruktúry práce
Štruktúra rukopisu sa riadi modelom **IMRaD** a lokálnym sprievodcom.

## Hlavné priečinky
- `references/` – bibliografia, `.bib` export, citačné poznámky
- `notes/` – výpisky zo zdrojov, meeting notes, nápady
- `manuscript/` – drafty kapitol a outline
- `analysis/` – dáta, skripty, logy, výstupy
- `tables/`, `figures/` – exporty do Wordu
- `prompts/` – stabilné prompty pre AI/agentov
- `docs/literature/` – mapy literatúry, gap tracking a workflow pre rešerš
- `docs/guides/` – interné sprievodce a metodické materiály

## Odporúčaný workflow
1. Začni v `docs/literature/literature_map_diplomovka.md` a podľa potreby otvor detailný súbor pre klastre, gaps alebo agent tasky.
2. Zdroje ukladaj do Zotera v tematických kolekciách a tagoch podľa literature map.
3. Do repa exportuj pomocný súbor `references/zotero-thesis.bib`.
4. Ku kľúčovým zdrojom rob stručné výpisky do `notes/literature/`.
5. Ak zdroj vstupuje do textu, skontroluj príslušný source map v `references/`.
6. Drafty kapitol píš do `manuscript/*.md`.
7. Vo draftoch používaj citekey placeholdery, napr. `[@koo2016icc]`.
8. Finálnu verziu skladaj vo Worde cez Zotero plugin.
9. Do Git-u ukladaj textové drafty, R skripty, tabuľky a grafy; `.docx` commituj len ako vedomé snapshoty.

## Prvé kroky
- skontroluj `AGENTS.md`
- otvor `docs/aktualny-stav-diplomovky.md`
- otvor `docs/backlog-diplomovky.md`
- otvor `docs/literature/literature_map_diplomovka.md`
- otvor `docs/literature/source_clusters.md`
- otvor `manuscript/00_outline.md`
- otvor `references/zotero_import_checklist.md`
- nastav auto-export Better BibTeX do `references/zotero-thesis.bib`
- začni vypĺňať `notes/literature/_template.md`
