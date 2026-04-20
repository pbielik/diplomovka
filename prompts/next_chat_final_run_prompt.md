# Next Chat Final Run Prompt

Prečítaj si:

1. `AGENTS.md`
2. `docs/guides/sprievodca_summary.md`
3. `docs/aktualny-stav-diplomovky.md`
4. `docs/backlog-diplomovky.md`
5. `docs/next-chat-final-run-handoff.md`
6. `analysis/final_run_playbook.md`
7. `manuscript/40_results_full_run_staging.md`

Kontext:

- Repo už má funkčný autoritatívny rehearsal run.
- Ingest do `analysis/data_clean/` je reprodukovateľný cez `analysis/scripts/import_current_export_to_data_clean.py`.
- Pipeline `analysis/scripts/thesis_rating_pipeline.R` prechádza.
- `pre_word` QC aktuálne končí `PASS_WITH_NOTES`.
- Hlavné `manuscript/40_results.md` ešte nie je prepísané na final full-run prose.
- Známy raw problém v `analysis/validity data/data.csv` neblokuje run, pokiaľ ostáva len ako `info`.

Tvoj cieľ:

- ak finálny export ešte nie je dodaný, nič nefinalizuj a priprav len workflow na posledný run,
- ak finálny export je dodaný, urob posledný ingest, pipeline run, QC a prepíš `40_results.md` a `50_discussion.md` podľa autoritatívnych outputov.

Ak je finálny export dodaný, postupuj presne takto:

1. Spusť:

```bash
python3 analysis/scripts/import_current_export_to_data_clean.py --source "/ABS/PATH/TO/final_export.csv"
```

2. Spusť:

```bash
Rscript analysis/scripts/thesis_rating_pipeline.R
```

3. Spusť:

```bash
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode smoke --agent-mode mock
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode pre_word --agent-mode mock
```

4. Ak QC nemá `blocker` ani `major`, vyplň `manuscript/40_results_full_run_staging.md` podľa aktuálnych outputov.
5. Z neho prepíš:
   - `manuscript/40_results.md`
   - `manuscript/50_discussion.md`
   - podľa potreby aj `manuscript/10_title_abstract.md` a `manuscript/60_conclusion.md`
6. Aktualizuj dashboard a backlog.
7. Na konci stručne zhrň:
   - aký export si použil,
   - aké sú finálne počty,
   - či QC prešlo,
   - ktoré manuscript súbory si prepísal.

Pravidlá:

- Nemanualne neupravuj `analysis/data_clean/*.csv`.
- Nemiešaj transcript-level a rating-level vetvy.
- Neber preview drafty ako source of truth, ak už existuje finalný clean run.
- Ak `ICC` alebo iný blok ostane neodhadnuteľný, reportuj to transparentne, nevymýšľaj numerický výsledok.
- Ak sa objaví blokujúci QC nález, najprv ho oprav a až potom prepisuj manuscript.
