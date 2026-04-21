# 70 Appendices / Prílohy

> Pracovný framing príloh pre diplomovú prácu. Cieľom je oddeliť to, čo má byť súčasťou verejného thesis balíka, od toho, čo je proprietárne, citlivé alebo len interné workflow.

## Funkcia príloh v tejto práci

Prílohy majú doplniť hlavný text tam, kde by plné znenie nástroja, doplnková tabuľka alebo servisný dokument znižovali čitateľnosť jadra IMRaD. Nemajú fungovať ako odkladisko všetkého, čo vzniklo počas práce.

Lokálny sprievodca zároveň výslovne uvádza dve dôležité pravidlá:

- empirické výskumné otázky a hypotézy možno dať do príloh, ak by v hlavnom texte znižovali prehľadnosť;
- samotné prílohy nie sú priestorom pre všetky tabuľky, grafy alebo technické výstupy, ktoré sa „nezmestili“ do textu.

Pre túto diplomovku to znamená, že do príloh patria len také artefakty, ktoré:

- priamo pomáhajú pochopiť dizajn, nástroj alebo doplnkové výsledky,
- sú obhájiteľné pri obhajobe,
- nevyzrádzajú zbytočne interné know-how simulačného rámca,
- neobsahujú zbytočné identifikátory alebo citlivé metadata.

## Dôležité pravidlo pre CRZP a proprietárne materiály

Presun niečoho do príloh **sám osebe nerieši neverejnosť**. Ak niečo nechceš mať verejne dostupné v registri, nesmie to byť súčasťou verejného PDF balíka práce. Také materiály treba buď:

- odovzdať ako osobitné neverejné alebo obmedzene šírené prílohy podľa pravidiel školy,
- alebo ich vôbec nedávať do verejnej verzie práce a v texte ich iba zhrnúť.

Pri tejto práci sa to týka najmä presných runtime pravidiel simulácie, plného seed corpusu, plných transkriptov a surových exportov.

## Vrstva A: Verejné prílohy vhodné do práce

Toto je odporúčaný **public-safe balík**, ktorý môže ísť priamo do Word verzie práce alebo do verejného appendix balíka.

| Príloha | Názov | Zdroj v repo | Prečo tam patrí | Poznámka k redakcii |
| --- | --- | --- | --- | --- |
| A | Finálny ratingový nástroj | `manuscript/30_method.md`, `analysis/codebook_rating_study.csv` | čitateľ uvidí plné znenie položiek a škál | bez screenshotov survey engine; len čisté znenie položiek, škály a inštrukcia pre ratera |
| B | Operacionalizačná tabuľka premenných a kompozitov + stručný preklad mixed modelov | `analysis/methods_variables_table.csv`, `analysis/codebook_rating_study.csv`, `analysis/derived_variables_table.csv`, `manuscript/30_method.md` | kompaktná opora medzi teóriou, premennými, analytickými úrovňami a čítaním hlavných modelov | upraviť do jazyka práce; technické názvy ponechať len tam, kde sú potrebné |
| C | Public-safe schéma seedov a anchorovania | `manuscript/30_method.md`, `analysis/data_clean/seed_anchors_final.csv` | ukáže logiku seed anchoringu bez odovzdania celého know-how balíka | zaradiť len schému domén A1-A9, logiku anchorov a 1 ilustračný seed; nie celý 12-seed corpus |
| D | Doplnkové tabuľky a grafy | `tables/table_s1_spearman_transcript_composites.csv`, `tables/table_s2_pam_cluster_profiles.csv`, `tables/table_s3_pam_cluster_by_condition.csv`, `figures/figure_s1_spearman_heatmap.png`, `figures/figure_s2_pam_cluster_map.png` | patrí sem iba doplnkový analytický materiál, ktorý podporuje text, ale netvorí jadro testovania | zaradiť len tie supplementy, ktoré ostanú interpretačne zmysluplné po finálnom run-e |
| E | Etické a rater inštrukčné dokumenty v odľahčenej verzii | `manuscript/30_method.md`, prípadné finálne dokumenty k zberu | zvyšujú transparentnosť procedúry | bez interných runtime pravidiel a bez technických branching pokynov |
| F | Kompaktná mapa empirických otázok, hypotéz, outcome-ov a modelov | `docs/vo_h_model_results_map.md`, `manuscript/20_introduction.md`, `manuscript/30_method.md` | lokálny sprievodca priamo odporúča empirické VO/H presunúť do príloh, ak by zahlcovali text | urobiť z toho jednu prehľadnú tabuľku, nie viacstranový interný planning doc |
| H | Transparentné vyhlásenie o využití generatívnej AI pri vypracovaní práce | reálny authoring a technický workflow práce | zvyšuje metodickú a etickú transparentnosť a odlišuje AI ako predmet výskumu od AI ako podporného nástroja pri písaní | držať text stručný, vecný a viazaný na reálne použitie; nepreháňať technické detaily, ale jasne pomenovať hranice použitia |

## Vrstva B: Neverejné alebo obmedzene šírené prílohy

Toto sú artefakty, ktoré **majú vysokú metodickú hodnotu**, ale zároveň nesú simulačné know-how, interné runtime pravidlá alebo zbytočne detailné surové podklady. Ak ich budeš vôbec odovzdávať, odporúčané je riešiť ich mimo verejného PDF balíka.

| Balík | Názov | Zdroj v repo | Prečo ho nedávať do verejnej verzie |
| --- | --- | --- | --- |
| R1 | AI-only runtime interview pack | `docs/resources/interview-protocol/interview_protocol_ai_only_runtime.md`, `.txt`, `.docx`, changelog | obsahuje presné runtime pravidlá, turn limits, interné safety branching a simulačné know-how |
| R2 | Plný seed corpus s exact anchors a notes | `analysis/data_clean/seed_anchors_final.csv` | ide o jadro proprietárneho návrhu prípadov a presných cieľových profilov |
| R3 | Plný corpus transkriptov alebo väčší výber transkriptov | `analysis/data_clean/transcripts_master.csv` + externé transcript files | ide o hlavný generovaný asset práce; verejným sprístupnením by si odovzdal hotový tréningový materiál |
| R4 | Surový rating export vrátane komentárov a rater metadata | `analysis/data_clean/ratings_clean.csv`, `analysis/data_clean/raters_clean.csv` | pri malom počte expertov zvyšuje riziko nepriamej identifikácie; komentáre sú surové pracovné dáta |
| R5 | Technické exportné schémy a interné survey-engine vrstvy | `manuscript/30_method.md`, prípadné budúce exporty zo survey engine | nie sú nutné pre čitateľské porozumenie a odhaľujú zbytočne internú implementáciu |

Pre túto vrstvu platí prísnejšie pravidlo: ak materiál nie je nevyhnutný pre obhajobu alebo formálne odovzdanie, je lepšie ho **nechať iba v internom repo workflowe** a v práci ho zhrnúť.

## Vrstva C: Čisto interné repo artefakty, ktoré do príloh nepatria

Tieto súbory a priečinky majú workflow funkciu, ale nemajú byť appendixom:

- operatívny tracking: `docs/aktualny-stav-diplomovky.md`, `docs/backlog-diplomovky.md`
- interné plánovanie a konzultácie: `notes/meetings/`, `prompts/`
- literárny workflow: `docs/literature/`, `notes/literature/`, `references/scripts/`, `references/zotero-thesis-seed.bib`
- build a tooling vrstva: `tools/`, `tables/styled_preview/`, `tools/ai-tools/`
- technické pipeline medzivýstupy: väčšina `analysis/outputs/`
- draftové a technické verzie protokolov: changelogy, working exports, preview `.docx`
- všeobecné interné guides a agent workflow docs: `AGENTS.md`, `CLAUDE.md`, `PRIRUCKA_DIPLOMOVKA_AI_ZOTERO_WORD.md`, `docs/guides/`

Tieto materiály treba používať pri písaní a pri odovzdávacom workflowe, ale nie ich kopírovať do appendixu.

## Odporúčaný finálny appendix balík pre túto diplomovku

Ak by som to mal teraz zafixovať ako najrozumnejší cieľový stav, odporúčam:

### Verejný appendix balík

1. Príloha A — finálny ratingový dotazník.
2. Príloha B — operacionalizačná tabuľka premenných, kompozitov, analytických úrovní a stručného prekladu mixed modelov.
3. Príloha C — skrátená schéma seedov a anchor domén s jedným ilustračným prípadom.
4. Príloha D — doplnkové tabuľky a grafy, ktoré ostanú po finálnom run-e interpretačne zmysluplné.
5. Príloha E — etické a rater inštrukčné dokumenty v redigovanej verzii.
6. Príloha F — kompaktná mapa empirických otázok, hypotéz, outcome-ov a modelov.
7. Príloha H — transparentné vyhlásenie o využití generatívnej AI pri authoringu a technickom workflowe práce.

### Neverejný alebo obmedzene šírený appendix balík

1. AI-only runtime interview pack.
2. Plný 12-seed corpus s exact anchors a notes.
3. Plný alebo väčší výber transkriptov.
4. Surové ratingové exporty vrátane komentárov a detailnejších rater metadata.
5. Technická dokumentácia k internému survey-engine alebo runtime vrstve, ak ju bude škola vôbec vyžadovať.

## Čo konkrétne neťahať do verejného registra

Ak je cieľ nechrániť „vatou“ všetko, ale skutočne vyrezať proprietárne jadro, do verejného balíka by som **nedával**:

- presné runtime wordingy z AI-only interview packu,
- interné branching pravidlá simulácie a safety eskalácie,
- plné seed narrative notes z `seed_anchors_final.csv`,
- plné transkripty alebo väčší transcript corpus,
- surové otvorené komentáre hodnotiteľov,
- detailné rater metadata pri malom expertnom paneli,
- technické polia typu `backend_model`, `transcript_path`, `created_at`, `chat_variability`,
- interné workflow dokumenty, backlog, meeting notes, prompty a skripty.

## Najbližší praktický krok

Keď sa bude robiť finálna Word skladba, táto kapitola sa má preklopiť do dvoch vrstiev:

1. z nej urobiť krátku pracovnú osnovu pre skutočné verejné prílohy A-F;
2. samostatne rozhodnúť, či balík R1-R5 vôbec potrebuješ odovzdávať škole, alebo stačí mať ho pripravený len pre školiteľa, oponenta alebo pre interný archív.

Prvý konkrétny preklop tohto rámca už existuje v súbore `manuscript/71_public_appendix_draft.md`.
