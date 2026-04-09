# Literature Workflow

Tento adresár drží rozdelený literature bundle pre diplomovku. Bibliografický zdroj pravdy ostáva v Zotere. Súbory v `docs/literature/` sú plánovacia a workflow vrstva medzi Zoterom, výpiskami a rukopisom.

## Čo je kde

- `literature_map_diplomovka.md` – centrálny rozcestník
- `source_clusters.md` – tematické klastre a jadro zdrojov
- `gaps_and_missing_sources.md` – otvorené medzery a coverage risks
- `p1_expansion_pass.md` – konkrétny citekey-ready balík pre kritické gaps
- `agent_tasks.md` – hotové zadania pre agentov
- `action_plan.md` – stručný prioritizačný plán
- `missing_fulltext_for_notes.md` – živý blocker log pre citekeye bez lokálneho `PDF` alebo `snapshotu`

## Ako s bundle pracovať

1. Začni v `literature_map_diplomovka.md`.
2. Nový zdroj zaraď do klastru v `source_clusters.md`.
3. Urči jeho prioritu: `must-read`, `should-read` alebo `optional`.
4. Ulož ho do zodpovedajúcej Zotero kolekcie a označ relevantnými tagmi.
5. Ak je zdroj metodicky alebo argumentačne kľúčový, vytvor k nemu výpiskový súbor v `notes/literature/`.
6. Ak sa citekey objaví v rukopise, skontroluj príslušný source map v `references/` a zhodu s `references/zotero-thesis.bib`.
7. Ak sa pri výpisku zastavíš na tom, že v Zotere chýba lokálny fulltext, zapíš citekey do `missing_fulltext_for_notes.md`.

## Štandard pre validovateľné výpisky

Pri `must-read` a metodicky kritických zdrojoch používaj evidence-first štandard, aby sa dal každý bod rýchlo spätne overiť v PDF alebo snapshote:
- `opiera sa o:` sekciu, tabuľku, figúru alebo iný pomenovaný blok článku,
- `locator:` presná strana, tabuľka, sekcia alebo iný locator,
- `kontrolný excerpt:` väčší súvislý kontextový blok, nie len krátky anchor phrase,
- `parafráza:` stručná pracovná formulácia,
- `use:` kde sa to má použiť v rukopise alebo metodike.

Praktické pravidlo:
- bez locatora a excerptu sa bod nepovažuje za pripravený na bezpečnú parafrázu,
- ak locator nie je jasný, označ bod ako `needs manual check`.

## Kedy bundle aktualizovať

- keď pribudne nový tematický okruh, ktorý sa nezmestí do existujúceho klastru,
- keď sa zmení dizajn, hypotézy, premenné alebo analytický plán,
- keď sa objaví nový blocker v literatúre pre Method, Results alebo Discussion,
- keď sa zmení priorita zdroja z `optional` na `must-read` alebo naopak.
