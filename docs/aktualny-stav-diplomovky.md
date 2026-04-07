# Aktuálny stav diplomovky

> Posledná aktualizácia: 2026-04-07
> Tento súbor je operatívny dashboard. Má ukazovať reálny stav repa, nie želaný stav.

## Verdikt k dnešnému stavu

Práca nie je v počiatočnej fáze. Máš hotový výskumný rámec, revidovaný draft úvodu a metódy, vyčistenú kostru výsledkov, nový rozdelený literature bundle v `docs/literature/` a markdown knižnicu pomocných materiálov pre thesis writing v `docs/resources/thesis-writing-md/`. Kritická cesta je teraz jasnejšia: Zotero seed workflow je po importe a cleanup-e funkčný, `references/zotero-thesis.bib` obsahuje 114 entries vrátane 6 nových zdrojov z rozšíreného Úvodu (`who2025depression`, `chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager`), `references/bibliography-notes.md` má exact coverage a všetky citekeys v `manuscript/20_introduction.md` sa zosúladili s bibom (0 missing), core zdroje sú priradené do tematických subkolekcií, hlavná kolekcia je zosynchronizovaná so subkolekciami, thesis jadro má manuálnu vrstvu priorít a tematických tagov (mapovania pre 6 nových zdrojov sú pridané v `assign_zotero_subcollections.py` a `assign_zotero_tags.py` a čakajú na manuálne spustenie s `--apply --restart-zotero`), a dnešný fulltext audit ukazuje, že z citekey-ready zdrojov má väčšina lokálne PDF a v `must-read` bloku zostávajú už iba ojedinelé missing attachmenty. Evidence-anchored poznámkový korpus je rozšírený na `36` notes (30 existujúcich + 6 nových pre rozšírený Úvod), pričom 5 z 6 nových notes (`chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager`) má teraz hlboké evidence blocky postavené na plných PDF s konkrétnymi page locatormi a verbatim excerptmi (8-11 blokov per note), a `who2025depression` zostáva pri HTML fact sheet excerptoch, ktoré sú dostatočné. Z aktuálne PDF-ready core vetvy ostáva bez validovateľného note už len `cook2010computerizedvirtualpatients`, kde current attachment stále vyzerá byť supplement-only. Ďalší reálny posun je dorobiť posledné missing full texty z `must-read` bloku, dostať reálne rating dáta do `analysis/data_clean/`, spustiť pipeline na reálnych vstupoch a z toho doplniť výsledky, diskusiu, záver a finálny abstrakt.

## Stav repa po oblastiach

| Oblasť | Stav | Čo už je v repo | Čo chýba na ďalší posun |
| --- | --- | --- | --- |
| Rukopis | `rozpracované` | outline, názov/abstrakt, revidovaný úvod, revidovaná metóda, vyčistená kostra výsledkov, diskusný draft | finálne počty, výsledky z analýzy, doplnenie placeholderov, finálne prepojenie na Word |
| Literatúra | `in_progress` | source map, import checklist, citekey seed workflow, rozdelený literature bundle s klastrami, gapmi, agent taskmi, plánom, `P1 expansion pass`, audit seed workflow v `docs/literature/bbt_seed_audit_2026-04-06.md`, importér `references/scripts/import_bibliography_notes_to_zotero.py`, cleanup script `references/scripts/cleanup_zotero_duplicates_and_enable_export.py`, export script `references/scripts/export_cleaned_collection_to_bib.py`, script na prvé roztriedenie do subkolekcií `references/scripts/assign_zotero_subcollections.py`, script na sync hlavnej kolekcie `references/scripts/sync_zotero_root_collection.py`, script na manuálne thesis tagy `references/scripts/assign_zotero_tags.py`, script na current audit attachmentov `references/scripts/report_zotero_fulltext_status.py`, finálny export `references/zotero-thesis.bib`, zosúladený `references/zotero-thesis-seed.bib`, prvý batch roztriedenia nových zdrojov do relevantných subkolekcií, sync hlavnej kolekcie so subkolekciami, manuálne priority + tematické tagy pre jadro citekey-ready zdrojov, dnešný fulltext checklist v `docs/literature/fulltext_checklist_2026-04-07.md`, 30 evidence-anchored výpiskov v `notes/literature/` a workflow pravidlá pre validovateľné notes zapísané v `AGENTS.md`, `docs/literature/README.md` a `references/zotero_import_checklist.md` | dorobiť posledné missing full texty pre `must-read` jadro, manuálne overiť `cook2010computerizedvirtualpatients` kvôli supplement-only attachmentu a potom ďalej rozširovať evidenčné výpisky |
| Dáta a analýza | `skelet pripravený` | codebook, premenné, hypotézy, R pipeline, CSV šablóny | clean data v `analysis/data_clean/`, beh pipeline na reálnych dátach, exporty do `analysis/outputs/`, `tables/`, `figures/` |
| Písacie podklady | `done` | konvertované materiály v `docs/resources/thesis-writing-md/`, syntetický README a nový brief `docs/guides/master-outline-diplomovky-v2.md` | používať ich pri draftingu, outline a auditovaní sekcií |
| Operatívny tracking | `zavedené` | tento dashboard, backlog, aktualizačné pravidlá pre agentov, workflow README pre literatúru | priebežná údržba po každej väčšej zmene |

## Stav kapitol IMRaD

| Súbor | Stav | Hodnotenie stavu | Najväčší blocker |
| --- | --- | --- | --- |
| `manuscript/10_title_abstract.md` | `rozpracované` | pracovný názov a použiteľný draft abstraktu už existujú | finálne výsledky pre abstrakt |
| `manuscript/20_introduction.md` | `silný draft` | prepracovaný podľa rozšíreného draftu: 1.1 depresívna symptomatika, 1.2 klasické simulované patienty, 1.3 LLM simulovaní pacienti (CureFun, PATIENT-ψ, Adaptive-VP, MindVoyager), 1.4 expertná evaluácia + COSMIN, 1.5 pojmový rámec s operacionalizáciou `guardrail` a `profile`, 1.6 výskumná medzera, 1.7 cieľ/VO1-VO8/H1-H9 (jadro H1-H5, rozšírené H6-H9); všetkých 23 unikátnych citekeys overených proti `references/zotero-thesis.bib` (0 missing) vrátane 6 nových zdrojov `who2025depression`, `chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager`, ktoré majú evidence-anchored výpisky v `notes/literature/` s hlbokými blokami z plných PDF (5 z 6 notes) | štylistické doladenie a postupné integrovanie nových evidence blokov (page locatorov, kvantitatívnych benchmarkov ako PATIENT-ψ µ=1.3, Adaptive-VP F=8.421, CureFun B-ELO +250.18) priamo do textu kapitol 1.2-1.5 |
| `manuscript/30_method.md` | `silný draft` | dizajn, premenné a analytický plán sú dobre pomenované a lepšie previazané s H1-H6 | finálne počty raterov, finálny opis procedúry podľa reálneho zberu |
| `manuscript/40_results.md` | `kostra` | logika prezentácie je čistejšia a lepšie drží poradie hypotéz a reportovacích pravidiel | chýbajú reálne dáta, reliabilita, ICC, modely, tabuľky a grafy |
| `manuscript/50_discussion.md` | `polodraft` | interpretívna kostra a limity sú pripravené | treba ju prepísať podľa skutočných výsledkov, nie podľa hypotetických formulácií |
| `manuscript/60_conclusion.md` | `kostra` | záver má jasný rámec | potrebuje 3-5 finálnych viet po analýze |

## Kritická cesta

```mermaid
flowchart LR
    A["Literature review map + priority gaps"] --> B["Zotero kolekcie, tagy a export `references/zotero-thesis.bib`"]
    B --> C["Stabilné citekeys a literárne výpisky"]
    D["Reálny rating export + finálne seedy"] --> E["Clean dáta v `analysis/data_clean/`"]
    E --> F["Beh `analysis/scripts/thesis_rating_pipeline.R` na reálnych dátach"]
    F --> G["Exporty do `analysis/outputs/`, `tables/`, `figures/`"]
    G --> H["Doplnenie `manuscript/40_results.md`"]
    H --> I["Prepis `manuscript/50_discussion.md` podľa výsledkov"]
    C --> I
    I --> J["Finálny abstrakt, záver a Word milestone"]
```

## Najdôležitejšie dependency a blokery

| Dependency | Stav | Blokuje | Poznámka |
| --- | --- | --- | --- |
| `references/zotero-thesis.bib` | `done` | nič blokujúce | finálny cleaned export už reálne existuje v repo a sedí s current bibliography-notes workflow; hlavná Zotero kolekcia je zosynchronizovaná so subkolekciami a core zdroje majú manuálne thesis tagy |
| `references/zotero-thesis-seed.bib` | `done` | nič blokujúce | helper seed je zosúladený s finálnym exportom; `bibliography-notes` coverage je `36 / 36 exact` |
| Výpisky v `notes/literature/` | `in_progress` | rýchle prepisovanie intro/discussion | existuje už 36 evidence-anchored note súborov (30 pôvodných + 6 nových pre rozšírený Úvod); workflow štandard je `opiera sa o + locator + väčší kontextový excerpt + parafráza + use`; 5 z 6 nových notes (`chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager`) má teraz hlboké evidence blocky z plných PDF s page locatormi, šiesty (`who2025depression`) zostáva pri HTML fact sheet excerptoch ako dostatočný; z aktuálne PDF-ready core vetvy ostáva bez validovateľného note už len `cook2010computerizedvirtualpatients`, kde current Zotero attachment vyzerá byť len supplement; popri tom treba dorobiť posledné missing full texty z `docs/literature/fulltext_checklist_2026-04-07.md` |
| Mapové literárne medzery A-D | `in_progress` | silnejšiu Method a Discussion | P1 expansion pass je už importnutý do Zotera, pretavený do čistého exportu a prvotne roztriedený do subkolekcií, ale ešte treba spraviť výpisky |
| Nové literárne medzery F-I (6 zdrojov z rozšíreného Úvodu) | `resolved` | nič blokujúce | `who2025depression`, `chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager` sú importnuté do Zotera, zahrnuté v `references/zotero-thesis.bib` (114 entries), placeholdery v `manuscript/20_introduction.md` sa zosúladili s bibom (0 missing, overené regexom) a pre každý z nich existuje evidence-anchored výpisk v `notes/literature/`; backlog `B22` a `B23` sú `done` |
| Clean ratings dataset | `chýba` | výsledky, tabuľky, grafy, záver | bez neho je `40_results.md` iba šablóna |
| Exporty v `tables/` a `figures/` | `chýbajú` | Word milestone a finálny Results | priečinky existujú, ale sú prázdne |
| Finálne počty raterov/ratingov | `chýbajú` | Method, Results, Abstract | placeholdery ostali v texte |

## Čo môžeš robiť hneď

- spustiť `references/scripts/assign_zotero_subcollections.py --apply --restart-zotero` a `references/scripts/assign_zotero_tags.py --apply --restart-zotero` pre priradenie 6 nových zdrojov do tematických subkolekcií a manuálnych thesis tagov (mapovania sú už pridané do skriptov)
- integrovať hlboké evidence blocky z 5 prehĺbených notes (`chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager`) priamo do textu kapitol 1.2-1.5 v `manuscript/20_introduction.md` — najmä konkrétne kvantitatívne benchmarky (PATIENT-ψ µ=1.3 p<10⁻⁴, Adaptive-VP F=8.421 p=.008, CureFun B-ELO +250.18, Spearman ρ ≈ 0.81) a pred-LLM precedensy (Dupuy 2020 s 35 študentmi a MDD VP)
- dorobiť posledné missing full texty pre `must-read` blok podľa `docs/literature/fulltext_checklist_2026-04-07.md`
- manuálne overiť `cook2010computerizedvirtualpatients` a doplniť hlavný fulltext, ak current attachment ostáva supplement-only
- rozšíriť výpisky zo súčasných 30 evidence-anchored notes na celé must-read jadro a na nové literárne gaps F-I v `notes/literature/`
- jemne doladiť priority/tagy a prípadné sekundárne subkolekcie pre širší thesis corpus
- pripraviť clean export ratingov do `analysis/data_clean/`
- doplniť finálne počty raterov a ratingov do `manuscript/30_method.md` a `manuscript/40_results.md`
- pri ďalšom draftingu používať aj `docs/guides/master-outline-diplomovky-v2.md`, nie len starší sprievodca a outline
- upravovať úvod a metódu štylisticky, lebo ich logika už stojí

## Čo zatiaľ neriešiť ako finálne

- finálny abstrakt
- finálny záver
- finálne znenie diskusie
- definitívne tabuľky a grafy do Wordu

Tieto časti sú závislé od reálnych analytických výstupov.
