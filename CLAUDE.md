# CLAUDE.md

Tento repozitár slúži na prípravu diplomovej práce z psychológie (téma: AI/LLM simulácie a kvalita rozhovorov, ratingová štúdia).

## Zdroj pravdy pre pravidlá

Všetky pravidlá pre prácu s týmto repozitárom (štruktúra IMRaD, Zotero workflow, citekeys, dáta, dashboard, STOP pravidlá, checklisty) sú v **`AGENTS.md`**. Ten je autoritatívny aj pre Claude Code — pred akoukoľvek väčšou úpravou si ho prečítaj a riaď sa ním.

Hierarchia priority pri konflikte (z `AGENTS.md`):
1. `docs/guides/sprievodca-zaverecnych-prac.md`
2. `AGENTS.md`
3. `docs/guides/master-outline-diplomovky-v2.md`
4. aktuálne drafty v `manuscript/`

## Rýchla orientácia

- Hlavný rukopis: `manuscript/20_introduction.md`, `30_method.md`, `40_results.md`, `50_discussion.md`
- Stav a backlog: `docs/aktualny-stav-diplomovky.md`, `docs/backlog-diplomovky.md`
- Literatúra: `docs/literature/literature_map_diplomovka.md`
- Dáta a skripty: `analysis/data_clean/`, `analysis/scripts/`
- Bibliografia: `references/zotero-thesis.bib` (Zotero = jediný zdroj pravdy)

## Jazyk

Pracovný jazyk repozitára aj rukopisu je **slovenčina**. Komunikuj s používateľom a píš do súborov po slovensky, ak nie je explicitne určené inak.

## Čo Claude NIKDY nesmie

- meniť výskumné otázky alebo hypotézy bez zodpovedajúcej úpravy v metóde a výsledkoch
- rušiť alebo prepisovať existujúce citekeys bez náhrady
- pridávať nové analytické vetvy (napr. K-Means) bez väzby na cieľ a hypotézy
- ručne upravovať bibliografické údaje, ktoré už existujú v Zotere
- písať finálne APA citácie do markdown draftov (používaj len `[@citekey]` placeholdery)
- pridávať analýzy, podtémy alebo odseky len na „nafúknutie" rozsahu

Pri väčšom drafting alebo rewrite vždy najprv prejdi STOP pravidlá a checklisty z `AGENTS.md` (sekcie 13, 15, 16, 17).
