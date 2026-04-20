# Final Run Playbook

> Posledna aktualizacia: 2026-04-20
> Ucel: mat jeden kratky, bezpecny postup pre posledny ingest, autoritativny pipeline run, QC a prepis manuscriptu.

## Kedy tento playbook pouzit

- ked je zber ratingov pre dany milestone uz uzavrety,
- ked chces posledny export preliat do `analysis/data_clean/`,
- ked chces z toho isteho runu napisat finalne `40_results.md`, `50_discussion.md`, abstrakt a Word milestone.

Ak este mozu prist dalsie ratingy, povazuj aktualne outputy len za rehearsal run, nie za finalny manuscript truth.

## Source of truth

- finalny wide export ratingov = vstup pre ingest
- `analysis/data_clean/` = autoritativne clean vstupy pre pipeline
- `analysis/outputs/`, `tables/`, `figures/` = autoritativne analyticke vystupy
- `manuscript/40_results_full_run_staging.md` = staging scaffold pre posledny prepis Results
- `analysis/validity data/data.xlsx` = source of truth pre validity workbook

Raw `analysis/validity data/data.csv` je znamy problemovy snapshot. Pokial sa nezmeni workflow validity dat, neblokuj na nom finalny run; eviduj ho len ako technicku poznamku.

## Pred runom

1. Skontroluj, ze finalny export uz obsahuje vsetky nove ratingy, ktore maju ist do milestone.
2. Nemanualne neupravuj `analysis/data_clean/*.csv`.
3. Ak chces odmazat stare preview/QC artefakty, pouzi:

```bash
bash tools/pre_final_run_housekeeping.sh --apply
```

4. Over, ze finalny export je mimo repo alebo mas jeho presnu absolutnu cestu.

## Krok 1: ingest finalneho exportu

Spusti ingest do `analysis/data_clean/`:

```bash
python3 analysis/scripts/import_current_export_to_data_clean.py --source "/ABS/PATH/TO/final_export.csv"
```

Ak je finalny export na defaultnej ceste v `~/Downloads/mdd-ai-simulation_ratings_wide (4).csv`, parameter `--source` mozes vynechat.

Po ingeste rychlo skontroluj:

- `analysis/data_clean/ratings_clean.csv`
- `analysis/data_clean/transcripts_master.csv`
- `analysis/data_clean/raters_clean.csv`
- `analysis/data_clean/seed_anchors_final.csv`

Minimalne ocakavania:

- `ratings_clean.csv`: 1 riadok = 1 rating
- `transcripts_master.csv`: 1 riadok = 1 transkript
- `raters_clean.csv`: 1 riadok = 1 hodnotitel
- anchor vetva ostava transcript-level, nie rating-weighted

## Krok 2: autoritativny pipeline run

```bash
Rscript analysis/scripts/thesis_rating_pipeline.R
```

Po rune si ako prve otvor:

- `analysis/outputs/run_manifest.csv`
- `analysis/outputs/qc_dataset_summary.csv`

Run manifest musi byt v zhode s finalnym exportom:

- `source_mode = data_clean`
- spravny pocet `n_ratings`
- spravny pocet `n_raters`
- spravny pocet `n_transcripts`
- spravny pocet `n_seeds`

Ak sa tieto pocty nezhoduju s realnym finalnym exportom, nezacni prepisovat manuscript. Najprv oprav ingest alebo export.

## Krok 3: QC gate

Najprv smoke gate:

```bash
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode smoke --agent-mode mock
```

Potom pre-Word gate:

```bash
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode pre_word --agent-mode mock
```

Optionalne vies pustit aj agentovy pass:

```bash
.venv-ai-tools/bin/python analysis/scripts/run_thesis_qc.py --run-mode pre_word --agent-mode pydantic_ai
```

Ocakavany ciel:

- `smoke = PASS` alebo `PASS_WITH_NOTES`
- `pre_word = PASS` alebo `PASS_WITH_NOTES`

Ak ostane len `info` finding pre raw `analysis/validity data/data.csv`, je to akceptovatelne. Ak sa objavi `blocker` alebo `major`, najprv ho zavri a az potom prepisuj manuscript.

## Krok 4: last-mile manuscript rewrite

Poradie prepisu:

1. `manuscript/40_results_full_run_staging.md`
2. `manuscript/40_results.md`
3. `manuscript/50_discussion.md`
4. `manuscript/10_title_abstract.md`
5. `manuscript/60_conclusion.md`

Pravidla:

- `40_results_full_run_staging.md` pouzi ako source map a prose scaffold, nie ako finalny subor.
- Finalne `40_results.md` musi sediet s CSV outputmi z posledneho runu.
- Ak `ICC` ostane neodhadnutelny alebo `NA`, reportuj to ako neodhadnutelne, nie ako numericky vysledok.
- Ak `emmeans_core_models.csv` nie je `ok`, neopieraj o ne hlavny text.
- Transcript-level ukazovatele (`A1-A9`, `symptom_error_mean`, `severity_error`, `impact_error`) vzdy reportuj ako transcript-level vetvu.
- Rating-level ukazovatele (`G*`, `S*`, `R*`, kompozity) vzdy reportuj ako rating-level vetvu.

## Krok 5: aktualizacia workflow dokumentov

Po prepisani hlavnych manuscript suborov aktualizuj:

- `docs/aktualny-stav-diplomovky.md`
- `docs/backlog-diplomovky.md`

Minimalne:

- datum poslednej aktualizacie,
- co je `done`,
- co ostava `in_progress`,
- najblizsi konkretny krok.

## Krok 6: Word build

Po uspesnom `pre_word` QC a po prepise manuscriptu:

```bash
./tools/build_word_preview.sh
./tools/build_word_clean.sh
./tools/build_word_plan_b_citekeys.sh
```

Pouzi ten build, ktory zodpoveda faze Word workflowu.

## Exit criteria

Finalny milestone je pripraveny az vtedy, ked plati vsetko z tohto:

- ingest prebehol bez manualnych oprav clean CSV,
- `run_manifest.csv` sedi s finalnym exportom,
- `pre_word` QC neobsahuje `blocker` ani `major`,
- `40_results.md` reportuje tie iste pocty a tie iste efekty ako autoritativne CSV outputy,
- `50_discussion.md` interpretuje uz realne vysledky, nie hypoteticky pilot,
- abstrakt a zaver pouzivaju rovnake pocty a rovnaky framing ako Results,
- dashboard a backlog uz nehovoria o pre-final stave, ak milestone uz bol uzavrety.

## Co nerobit

- neprepisuj rucne `analysis/data_clean/*.csv`
- neber `current-export preview` ako source of truth, ked uz existuje finalny clean run
- nepretlacaj do Results `emmeans`, `ICC` alebo ine bloky, ak v autoritativnych outputoch ostali neodhadnutelne
- nepis finalnu Discussion skor, nez je stabilny finalny Results text
