# Diplomovka – repo starter

Tento repozitár je pripravený pre písanie diplomovej práce s workflow:

- **Zotero** = master databáza literatúry
- **Word** = finálny rukopis s živými citáciami
- **Repo** = drafty, výpisky, analýzy, tabuľky, grafy, prompty a pomocný `.bib` export

## Základné pravidlo štruktúry práce
Štruktúra rukopisu sa riadi modelom **IMRaD** a lokálnym sprievodcom.

## Hlavné priečinky
- `references/` – bibliografia, `.bib` export, citačné poznámky
- `notes/` – výpisky zo zdrojov, meeting notes, nápady
- `manuscript/` – drafty kapitol a outline
- `analysis/` – dáta, skripty, logy, výstupy
- `tables/`, `figures/` – exporty do Wordu
- `prompts/` – stabilné prompty pre AI/agentov
- `docs/guides/` – interné sprievodce a metodické materiály

## Odporúčaný workflow
1. Zdroje ukladaj do Zotera.
2. Do repa exportuj pomocný súbor `references/zotero-thesis.bib`.
3. Ku kľúčovým zdrojom rob stručné výpisky do `notes/literature/`.
4. Drafty kapitol píš do `manuscript/*.md`.
5. Vo draftoch používaj citekey placeholdery, napr. `[@koo2016icc]`.
6. Finálnu verziu skladaj vo Worde cez Zotero plugin.
7. Do Git-u ukladaj textové drafty, R skripty, tabuľky a grafy; `.docx` commituj len ako vedomé snapshoty.

## Prvé kroky
- skontroluj `AGENTS.md`
- otvor `manuscript/00_outline.md`
- nastav auto-export Better BibTeX do `references/zotero-thesis.bib`
- začni vypĺňať `notes/literature/_template.md`
