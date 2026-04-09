# Backlog diplomovky

> Posledná aktualizácia: 2026-04-08
> Používaj tento súbor ako operatívny backlog. Stav `done` patrí len položkám, ktoré majú jasný artefakt v repo alebo vo Word milestone.

## Prioritný backlog

| ID | Priorita | Stav | Úloha | Závisí od | Výstup |
| --- | --- | --- | --- | --- | --- |
| B00 | `P2` | `done` | Zapracovať literature review map do workflow dokumentov a šablón | nový literature bundle v `docs/literature/` | aktualizované workflow docs, agent rules a template pre výpisky |
| B01 | `P1` | `done` | Dokončiť Zotero cleanup po bibliography-notes importe: case-duplicate `yu`, legacy duplicity a finálny Better BibTeX export | Zotero kolekcia `Diplomovka`, audit `docs/literature/bbt_seed_audit_2026-04-06.md`, seed import script | `references/zotero-thesis.bib`, zosúladený `references/zotero-thesis-seed.bib`, exact coverage `36 / 36` a odstránený `yu` case-conflict |
| B02 | `P1` | `in_progress` | Vytvoriť jadro literárnych výpiskov podľa must-read klastrov z literature bundle | B01 nie je striktne nutné, ale pomáha; B21 je praktický predstupeň | evidence-anchored notes už existujú pre `obradovich2024llmpsychiatry`, `kroenke2001phq9`, `terwee2018COSMINMethodologyEvaluating`, `maj2020depressioncharacterization`, `guidi2011clinicalinterviewdepression`, `yu2025simulatedpatientsystems`, `boateng2018scaledevelopment`, `meng2024llmmedicine`, `mcintyre2019mddvsbipolar`, `who2021ethicsaiforhealth`, `ajluni2025psychiatriceducation`, `evans2015vignettes`, `kononowicz2019virtualpatients`, `nelson2015manyratersordinal`, `howell2024genaipatientsafety`, `asgari2025hallucinationframework`, `brugge2024patientsimulation`, `goddard2012automationbias`, `jakobsson2005ordinalagreement`, `kennedy2008coresymptoms`, `hirschfeld2014bipolardifferential`, `who2024lmmguidance`, `williams2017simulationmentalhealth`, `dawood2024standardizedpatient`, `stein2021anxietycharacterization`, `baguley2022vignettedata`, `roustan2025cliniciansguide`, `polit2007cvi`, `cook2010computerizedvirtualpatients`, `mchugh2012InterraterReliabilityKappa`, `omar2024llmpsychiatry`, `guo2024llmmentalhealth`, `mitani2017ordinalsummarymeasures`, `haltaufderheide2024EthicsChatGPTMedicine`, `who2025depression`, `chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager`, `bucher2025ItsNotOnlya`, `hua2025ScopingReviewLarge`, `park2019DepressionPrimaryCarea`, `maurer2018DepressionScreeningDiagnosis`, `ariasdelatorre2022PrevalenceDepressionEurope`, `louie2024RoleplaydohEnablingDomainExperts`, `zengEmbracingFutureMedical`, `na2025SurveyLargeLanguage`, `chen2023SoulChatImprovingLLMs`, `kim2024MindfulDiaryHarnessingLarge`, `appeswg2021newreality`, `rice2022simulatedplacements`, `sheen2021simulationeducation`, `glatz2022simulationelements`, `schmidt2025client101` a `morrison2025virtuallypsychologist`; korpus má spolu 56 evidence-anchored notes; template aj workflow docs už používajú `opiera sa o + locator + väčší kontextový excerpt + parafráza + use`; `sheen2021simulationeducation` je po lokalnom PDF checku uzavretý ako plnohodnotný note, `guidi2011clinicalinterviewdepression` je doplnený ako novy klinicky anchor pre intro, `polit2007cvi` je doplnený ako metodicky CVI anchor pre validaciu, `cook2010computerizedvirtualpatients` ako historicky systematicky anchor pre virtual patients a `mchugh2012InterraterReliabilityKappa` ako explanatory anchor pre agreement metriky; fulltext-ready core vetva uz nema otvoreny note gap; B02 ostáva otvorené kvôli zvyšným literárnym gapom |
| B03 | `P1` | `todo` | Dostať reálny rating export do `analysis/data_clean/` | hotový zber alebo export zo survey engine | clean CSV pre ratingy a prípadné master tabuľky |
| B04 | `P1` | `todo` | Overiť finálne anchor hodnoty seedov a názvy premenných | B03 | konzistentné seedy a naming medzi CSV, metódou a R pipeline |
| B05 | `P1` | `todo` | Spustiť `analysis/scripts/thesis_rating_pipeline.R` na reálnych dátach | B03, B04 | `analysis/outputs/*.csv` s reálnymi výsledkami |
| B06 | `P1` | `todo` | Exportovať základné tabuľky a grafy do `tables/` a `figures/` | B05 | Tabuľka 1, reliabilita, modelové tabuľky, 2-3 hlavné grafy |
| B07 | `P1` | `todo` | Doplniť `manuscript/40_results.md` podľa reálnych výstupov | B05, B06 | plný draft Results bez analytických placeholderov |
| B08 | `P1` | `todo` | Prepísať `manuscript/50_discussion.md` podľa skutočných zistení | B07 | diskusia viazaná na reálne výsledky a literatúru |
| B09 | `P2` | `todo` | Doplniť finálne počty a procedural detail do `manuscript/30_method.md` | B03 | metóda bez procesných placeholderov |
| B10 | `P2` | `todo` | Finalizovať abstrakt a záver | B07, B08, B09 | finálny `10_title_abstract.md` a `60_conclusion.md` |
| B11 | `P2` | `todo` | Vytvoriť Word milestone draft so živými citáciami | B01, B07, B08, B10 | exportovateľný rukopis pre školiteľa |
| B12 | `P2` | `done` | Spraviť checklist revision pass cez Introduction, Method a Results s pomocou `docs/resources/thesis-writing-md/README.md` | nový markdown balík thesis writing materiálov | revidované drafty v `manuscript/20_introduction.md`, `manuscript/30_method.md`, `manuscript/40_results.md` |
| B13 | `P2` | `done` | Zapracovať master outline v2 do workflowu, guides a agent promptov | nové metodické usmernenia | `docs/guides/master-outline-diplomovky-v2.md`, aktualizované `AGENTS.md` a prompt súbory |
| B14 | `P2` | `done` | Pripraviť P1 expansion pass s konkrétnymi citekey-ready zdrojmi pre gaps A-E | literature bundle a PubMed/WHO metadata | `docs/literature/p1_expansion_pass.md`, aktualizované `references/bibliography-notes.md` a pracovný seed candidate v `references/zotero-thesis-seed.bib` |
| B15 | `P1` | `done` | Spraviť audit Better BibTeX seed workflow proti manuscriptu a literature bundle | lokálne workflow docs, source mapy a seed `.bib` | `docs/literature/bbt_seed_audit_2026-04-06.md` s gap listom, duplicitami a cleanup poradím |
| B16 | `P1` | `done` | Automatizovať import `references/bibliography-notes.md` do Zotera a dostať exact citekeys do aktuálneho seed exportu | lokálny Zotero connector, BBT JSON-RPC a notes bridge | `references/scripts/import_bibliography_notes_to_zotero.py`, hromadný import do Zotera a exact coverage `36 / 36` |
| B17 | `P1` | `done` | Vyčistiť Zotero duplicity a doplniť finálny export workflow | B16, lokálny Zotero DB cleanup a BBT export | `references/scripts/cleanup_zotero_duplicates_and_enable_export.py`, `references/scripts/export_cleaned_collection_to_bib.py`, finálny `references/zotero-thesis.bib` |
| B18 | `P2` | `done` | Roztriediť novú imported literatúru z top-level Zotero kolekcie do tematických subkolekcií podľa literature bundle | B16, B17 | `references/scripts/assign_zotero_subcollections.py` a prvý batch priradení do `01.*`, `02.*`, `03.*`, `04.*`, `07` a `08.2` subkolekcií bez odstránenia položiek z hlavnej kolekcie |
| B19 | `P2` | `done` | Zosynchronizovať hlavnú Zotero kolekciu s jej subkolekciami, aby bibliografické položky zo subkolekcií boli aj na top-level | B18 | `references/scripts/sync_zotero_root_collection.py` a doplnené priame členstvo chýbajúcich položiek v hlavnej kolekcii |
| B20 | `P2` | `done` | Pridať manuálnu vrstvu thesis tagov pre core citekey-ready literatúru | B18, B19 | `references/scripts/assign_zotero_tags.py` a priradené tagy `must-read`, `should-read`, `optional`, `methods`, `validation`, `ethics`, `llm`, `depression`, `seeding`, `analysis` |
| B21 | `P2` | `in_progress` | Doplniť missing full texty alebo snapshoty pre citekey-ready jadro pred systematickými výpiskami | B20 | fulltext attachments podľa `docs/literature/fulltext_checklist_2026-04-08.md`; aktuálny lokálny stav už má overené PDF pre `guidi2011clinicalinterviewdepression`, `sheen2021simulationeducation`, `polit2007cvi` aj `cook2010computerizedvirtualpatients`, takže MUST-READ fulltext blok je uzavretý; zostávajú len SHOULD-READ / OPTIONAL missing attachmenty |
| B22 | `P1` | `done` | Doplniť 6 nových zdrojov z rozšíreného draftu Úvodu do Zotera a potvrdiť citekeys | rozšírený draft `manuscript/20_introduction.md`, gap F-I v `docs/literature/gaps_and_missing_sources.md` | import do Zotero kolekcie `01 Depresia a MDD` (WHO 2025) a `02 LLM, mental health a psychiatria` (Chaby 2022, Li 2024 CureFun, Wang 2024 PATIENT-ψ, Lee 2025 Adaptive-VP, Kim 2025 MindVoyager) je hotový, `references/zotero-thesis.bib` aktuálne obsahuje 120 entries vrátane všetkých 6 nových citekeys, verifikované že `who2025depression`, `chaby2022embodiedvirtualpatients`, `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`, `kim2025mindvoyager` presne sedia s placeholderami v `20_introduction.md` (0 missing), mapovania pre subkolekcie a thesis tagy boli doplnené aj aplikované do Zotero DB |
| B23 | `P2` | `done` | Vytvoriť evidence-anchored výpisky pre 6 nových zdrojov z Úvodu | B22 | výpisky v `notes/literature/who2025depression.md`, `notes/literature/chaby2022embodiedvirtualpatients.md`, `notes/literature/li2024curefun.md`, `notes/literature/wang2024patientpsi.md`, `notes/literature/lee2025adaptivevp.md`, `notes/literature/kim2025mindvoyager.md` s formátom `opiera sa o + locator + kontrolný excerpt + parafráza + use`, pričom excerpty pochádzajú z verejne dostupných HTML verzií (WHO fact sheet, Frontiers, arXiv, ACL Anthology); hlbšie sekcie mimo abstraktov sú označené ako `needs manual check` a dajú sa doplniť po stiahnutí plných PDF |
| B24 | `P2` | `done` | Zapracovať vzdelávací framing a aplikačný presah práce do Úvodu, Diskusie a obhajoby | konzultačné usmernenie školiteľky, note `notes/meetings/2026-04-08-skolitelka-vzdelavaci-framing-plan.md`, sesterský repozitár `../ai-patient-sim` | vzdelávací framing je zapracovaný do `manuscript/20_introduction.md` (1.2, 1.6), `manuscript/50_discussion.md` (4.4, 4.5, 4.7, 4.8) a posilnený v `manuscript/60_conclusion.md`; aplikačný presah je teraz formulovaný prednostne ako budúci simulačný rámec, nie ako platformový claim; supporting literature je doplnená v `references/zotero-thesis.bib` a `notes/literature/` |
| B25 | `P2` | `done` | Explicitne zafixovať os simulačného rámca v Úvode a Metóde a vytvoriť source-to-section map pre Úvod | B02, B24 | `manuscript/20_introduction.md` a `manuscript/30_method.md` už explicitne pomenúvajú rámec `seedy -> guardrail/profile -> expert-rated hodnotenie -> plausibility/symptom fidelity/defect`; zároveň existuje `docs/literature/source_to_section_map_introduction.md`, ktorý mapuje bloky 1.1–1.6 na konkrétne evidence-anchored notes a označuje slabšie opory typu `manual check` |

## Závislosti a poradie práce

| Ak chceš spraviť toto | Najprv potrebuješ | Dá sa robiť paralelne? |
| --- | --- | --- |
| Finálny Results | clean dáta, pipeline, exporty | `nie` |
| Finálnu Discussion | výsledky, core literatúru a safety/limity zdroje | `čiastočne` |
| Finálny abstrakt | výsledky + záver práce | `nie` |
| Lepší Introduction | Zotero export, výpisky a literature bundle must-read jadro | `áno` |
| Čistejšiu Method | finálne počty, procedúru a metodické zdroje z literature bundle | `áno` |
| Word milestone | stabilné citekeys + dopísané IMRaD časti | `nie` |

## Najbližší odporúčaný sled

1. rozširovať `B02` na ďalšie mapové gapy a secondary papers mimo fulltext-ready core vetvy.
2. `B21` priebežne dočisťovať už len SHOULD-READ / OPTIONAL missing attachmenty.
3. zredukovať a štylisticky doladiť už integrovaný vzdelávací framing a líniu simulačného rámca v `20_introduction.md`, `50_discussion.md` a podkladoch na obhajobu podľa potreby školiteľky.
4. `B03` a `B04` pripraviť clean dáta a overiť naming.
5. `B05` a `B06` dostať z pipeline prvé reálne výstupy.

## Definition of done pre kritické položky

- `B01` je hotové až vtedy, keď súbor `references/zotero-thesis.bib` reálne existuje, citekeys sedia s markdown draftmi a seed audit nemá blocking gaps pre current bibliography-notes workflow.
- `B03` je hotové až vtedy, keď máš clean CSV v `analysis/data_clean/` a vieš ho bez ručných zásahov znovu vytvoriť.
- `B05` je hotové až vtedy, keď `analysis/outputs/` obsahuje reálne exporty z pipeline, nie iba placeholdery.
- `B07` je hotové až vtedy, keď v `40_results.md` nezostanú analytické placeholdery typu `[doplniť]`.
- `B08` je hotové až vtedy, keď diskusia interpretuje skutočné výsledky a neopiera sa o hypotetické formulácie.
