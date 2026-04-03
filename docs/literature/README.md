# Literature Workflow

Tento adresár drží rozdelený literature bundle pre diplomovku. Bibliografický zdroj pravdy ostáva v Zotere. Súbory v `docs/literature/` sú plánovacia a workflow vrstva medzi Zoterom, výpiskami a rukopisom.

## Čo je kde

- `literature_map_diplomovka.md` – centrálny rozcestník
- `source_clusters.md` – tematické klastre a jadro zdrojov
- `gaps_and_missing_sources.md` – otvorené medzery a coverage risks
- `p1_expansion_pass.md` – konkrétny citekey-ready balík pre kritické gaps
- `agent_tasks.md` – hotové zadania pre agentov
- `action_plan.md` – stručný prioritizačný plán

## Ako s bundle pracovať

1. Začni v `literature_map_diplomovka.md`.
2. Nový zdroj zaraď do klastru v `source_clusters.md`.
3. Urči jeho prioritu: `must-read`, `should-read` alebo `optional`.
4. Ulož ho do zodpovedajúcej Zotero kolekcie a označ relevantnými tagmi.
5. Ak je zdroj metodicky alebo argumentačne kľúčový, vytvor k nemu výpiskový súbor v `notes/literature/`.
6. Ak sa citekey objaví v rukopise, skontroluj príslušný source map v `references/` a zhodu s `references/zotero-thesis.bib`.

## Kedy bundle aktualizovať

- keď pribudne nový tematický okruh, ktorý sa nezmestí do existujúceho klastru,
- keď sa zmení dizajn, hypotézy, premenné alebo analytický plán,
- keď sa objaví nový blocker v literatúre pre Method, Results alebo Discussion,
- keď sa zmení priorita zdroja z `optional` na `must-read` alebo naopak.
