# Next Chat Handoff: Final Run

> Posledná aktualizácia: 2026-04-21
> Účel: odovzdať ďalšiemu chatu presne to, čo má urobiť pri poslednom exporte ratingov, bez nutnosti znovu rekonštruovať workflow.

## Aktuálny stav

- Autoritatívny rehearsal run už prebehol nad plným exportom a funguje end-to-end.
- `analysis/data_clean/` je už zapojené do hlavného workflowu a ingest je reprodukovateľný cez `analysis/scripts/import_current_export_to_data_clean.py`.
- `Rscript analysis/scripts/thesis_rating_pipeline.R` prechádza.
- `python analysis/scripts/run_thesis_qc.py --run-mode pre_word --agent-mode mock` aktuálne končí `PASS_WITH_NOTES`.
- Jediná známa neblokujúca poznámka je raw `analysis/validity data/data.csv`; source of truth ostáva `analysis/validity data/data.xlsx`.
- `manuscript/30_method.md` už obsahuje finálny počet `6` hodnotiteľov pre aktuálny rehearsal run.
- Hlavné `manuscript/40_results.md` ešte stále nie je prepísané na full-run prose; na to slúži staging scaffold.

## Čo je pripravené

- Playbook pre posledný run: `analysis/final_run_playbook.md`
- Staging scaffold pre Results: `manuscript/40_results_full_run_staging.md`
  - staging uz obsahuje aj pripraveny wording pre doplnkovy sensitivity `LMM` s `(1 | transcript_id)` a odkaz na kontinuálne číslovanú sensitivity tabuľku
- Dashboard: `docs/aktualny-stav-diplomovky.md`
- Backlog: `docs/backlog-diplomovky.md`

## Čo ďalší chat nemá robiť

- Nemá ručne prepisovať `analysis/data_clean/*.csv`.
- Nemá brať `current-export preview` ako source of truth, ak už je k dispozícii finálny clean run.
- Nemá finalizovať `40_results.md`, kým nie je dodaný posledný export ratingov.
- Nemá blokovať finálny run len kvôli raw `analysis/validity data/data.csv`, pokiaľ QC hlási len `info`.

## Keď finálny export ešte nie je dodaný

Ďalší chat má:

1. Prečítať `AGENTS.md`, `docs/guides/sprievodca_summary.md`, `docs/aktualny-stav-diplomovky.md`, `docs/backlog-diplomovky.md`, `analysis/final_run_playbook.md` a `manuscript/40_results_full_run_staging.md`.
2. Neprepísať ešte hlavné `40_results.md`.
3. Pripraviť sa len na posledný ingest/run a čakať na cestu k finálnemu exportu.

## Keď finálny export už je dodaný

Ďalší chat má urobiť presne toto:

1. Spustiť:

```bash
python3 analysis/scripts/import_current_export_to_data_clean.py --source "/ABS/PATH/TO/final_export.csv"
```

2. Spustiť:

```bash
Rscript analysis/scripts/thesis_rating_pipeline.R
```

3. Spustiť QC:

```bash
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode smoke --agent-mode mock
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode pre_word --agent-mode mock
```

4. Ak nie sú `blocker` ani `major`, vyplniť `manuscript/40_results_full_run_staging.md` podľa aktuálnych outputov.
5. Z prefinalizovaného scaffoldu prepísať:
   - `manuscript/40_results.md`
   - `manuscript/50_discussion.md`
   - podľa potreby `manuscript/10_title_abstract.md`
   - podľa potreby `manuscript/60_conclusion.md`
6. Aktualizovať:
   - `docs/aktualny-stav-diplomovky.md`
   - `docs/backlog-diplomovky.md`
7. Až potom robiť Word build.

## Minimálny verification checklist

- `analysis/outputs/run_manifest.csv` sedí s finálnym exportom
- `analysis/outputs/qc_dataset_summary.csv` sedí s finálnym exportom
- `analysis/outputs/emmeans_core_models.csv` už nie je `failed`
- `40_results.md` reportuje rovnaké počty ako `run_manifest.csv`
- transcript-level vetva ostáva transcript-level
- Discussion už nehovorí jazykom rehearsal runu

## Krátka veta pre ďalší chat

Ak je finálny export k dispozícii, neanalyzuj workflow odznova: použi `analysis/final_run_playbook.md`, doplň `manuscript/40_results_full_run_staging.md` z aktuálnych CSV outputov a až potom prepíš hlavné manuscript súbory.
