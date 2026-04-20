# Rating Export Readiness Checklist

> Posledna aktualizacia: 2026-04-20
> Ucel: mat na jednom mieste presne napisane, co musia obsahovat realne exporty pre analyzu a co dnes este nepokryva samotna pipeline.

## Verdikt

Analyticka vetva je uz `run-ready` na realnych datach a autoritativny ingest pre aktualny full export bol uspesne prevedeny do `analysis/data_clean/`.

Pre aktualny run uz plati:

1. clean vstupy existuju v `analysis/data_clean/`,
2. pipeline cita prioritne clean vstupy a fallbackuje na `analysis/templates/` len vtedy, ked clean subory chybaju,
3. `analysis/outputs/run_manifest.csv` pre aktualny autoritativny run reportuje `n_rows_analysis_long = 166`, `n_raters = 6`, `n_transcripts = 72`, `n_seeds = 12`.

Najblizsi blocker uz preto nie je ingest ani samotny beh pipeline, ale **prepísanie Results a Discussion na zaklade aktualnych outputov**.

## Povinne vstupne subory

V `analysis/data_clean/` maju byt pripravené tieto 4 subory:

1. `ratings_clean.csv`
2. `transcripts_master.csv`
3. `seed_anchors_final.csv`
4. `raters_clean.csv`

Pre aktualny full export uz tieto subory realne existuju a daju sa reprodukovatelne znovu vytvorit cez `analysis/scripts/import_current_export_to_data_clean.py`.

Aktualny skript `analysis/scripts/thesis_rating_pipeline.R` cita prioritne `analysis/data_clean/*.csv`; fallback na `analysis/templates/*.csv` ostava len ako bezpecna smoke-run vetva pri absencii clean vstupov.

## 1. ratings_clean.csv

### Jednotka analyzy

- 1 riadok = 1 hodnotenie 1 ratera na 1 transkripte.

### Povinne stlpce

- identifikatory a design metadata:
  - `record_id`
  - `rater_id`
  - `transcript_id`
  - `seed_id`
  - `guardrail`
  - `profile`
  - `variant_id`
- QC metadata:
  - `backend_model`
  - `target_turns`
  - `actual_turns`
  - `rating_duration_sec`
- hlavne ratingy:
  - `G1`, `G2`, `G3`, `G4`, `G5`
- symptom fidelity:
  - `A1`, `A2`, `A3`, `A4`, `A5`, `A6`, `A7`, `A8`, `A9`
  - `S1`, `S2`
- defect / QC blok:
  - `R1`, `R2`, `R3`, `R4`, `R5`
- exploracny blok:
  - `guessed_origin`
  - `guess_confidence`
  - `comment`

### Povinne domeny hodnot

- `guardrail`: iba `0` alebo `1`
- `profile`: iba `R1`, `R2`, `R3`
- `variant_id`: konzistentne s `guardrail × profile`, napr. `G0_R1`, `G1_R3`
- `G1` az `G5`, `guess_confidence`: iba `1` az `5`
- `S1`, `S2`: iba `1` az `5`
- `R1` az `R5`: iba `1` az `5`
- `A1` az `A9`: iba `0` az `3`
- `guessed_origin`: iba hodnoty zo schvaleneho setu
  - odporucane: `ai_generated`, `human_simulated`, `real_participant`, `unsure`

### Hard checks

- `record_id` musi byt unikatny.
- Nesmie existovat duplicate na kombinacii `rater_id + transcript_id`.
- `seed_id`, `guardrail`, `profile`, `variant_id` musia sediet s `transcripts_master.csv`.
- Vsetky povinne rating polia musia byt numericky parsovatelne.
- Ak ostanu missingy, musi byt jasne, ci ide o:
  - legitimne partial skipy,
  - vyradene hodnotenie,
  - technicky export bug.

## 2. transcripts_master.csv

### Jednotka

- 1 riadok = 1 transkript.

### Povinne stlpce

- `transcript_id`
- `seed_id`
- `guardrail`
- `profile`
- `variant_id`
- `backend_model`
- `target_turns`
- `actual_turns`
- `chat_variability`
- `created_at`
- `transcript_path`

### Hard checks

- `transcript_id` musi byt unikatny.
- Kazdy `transcript_id` pouzity v `ratings_clean.csv` musi existovat aj tu.
- Ak je experiment kompletny, malo by tu byt `72` riadkov:
  - `12 seedov × 6 variantov`
- `variant_id` musi byt deterministicky odvodeny z `guardrail + profile`.
- `transcript_path` ma ukazovat na realny subor alebo aspon na realne planovanu cestu.

### Poznamka

Aktualna pipeline tento subor nacitava, ale dalej ho nepouziva. Pre realny beh ma zmysel robit cez neho aspon QC join a kontrolu konzistencie exportu.

## 3. seed_anchors_final.csv

### Jednotka

- 1 riadok = 1 seed scenar.

### Povinne stlpce

- `seed_id`
- `A1_anchor` az `A9_anchor`
- `S1_anchor`
- `S2_anchor`
- `target_severity_label`
- `functional_impact_label`
- `notes`

### Hard checks

- `seed_id` musi byt unikatny.
- Kazdy `seed_id` z `ratings_clean.csv` musi mat anchor riadok.
- `A*_anchor` musia byt na skale `0` az `3`.
- `S1_anchor` a `S2_anchor` musia byt na skale `1` az `5`.
- Toto je zdroj pravdy pre:
  - `symptom_error_mean`
  - cielove transcript-level symptom kotvy
  - priame `severity_error` a `impact_error` pri `S1/S2` na skale `1-5`

## 4. raters_clean.csv

### Jednotka

- 1 riadok = 1 hodnotitel.

### Povinne stlpce

- `rater_id`
- `profession`
- `specialization`
- `years_practice`
- `experience_with_mdd`
- `notes`

### Hard checks

- `rater_id` musi byt unikatny.
- Kazdy `rater_id` z `ratings_clean.csv` musi existovat aj tu.
- `years_practice` ma byt konzistentne kodovane; povolene je ciste cislo alebo stabilne pasmo typu `16_plus`.
- `experience_with_mdd` ma byt konzistentne kodovane; idealne `0/1`, ale ak sa pouziva frekvencny wording typu `weekly`, ma byt stabilny napriec exportom.

## Minimalna QC tabulka pred prvym behom

Pred spustenim pipeline si over aspon tieto pocty:

- pocet hodnotitelov
- pocet transkriptov
- pocet seedov
- pocet ratingov celkovo
- priemerny pocet ratingov na transkript
- minimalny a maximalny pocet ratingov na transkript
- pocty riadkov podla:
  - `guardrail`
  - `profile`
  - `guardrail × profile`

Ak sa niekde rozbije balans, nie je to automaticky fatalne, ale musi to byt vedome pomenovane v Metode a neskor vo Vysledkoch.

## Co pipeline dnes este nepokryva uplne

Aktualny `analysis/scripts/thesis_rating_pipeline.R` uz vie:

- citat `analysis/data_clean/*.csv` a pri ich absencii spadnut do `analysis/templates/*.csv`,
- urobit join cez `ratings`, `transcripts`, `seeds` a `raters`,
- vypocitat:
  - `plausibility_index`
  - `defect_index`
  - `symptom_error_mean`
  - podla potreby aj `severity_error` a `impact_error` ako priame `1-5` error skore,
- vyprodukovat:
  - `alpha` aj `omega`,
  - `ICC` pre `plausibility_index`, `defect_index`, `S1`, `S2`,
  - mixed-model vystupy pre core outcome-y,
  - zakladne exploračné summary pre `guessed_origin`, `guess_confidence`,
  - tabulky a grafy do `tables/` a `figures/`.

Stale vsak plati, ze:

- otvorene komentare ostavaju manualna alebo polo-manualna kvalitatívna vrstva,
- `S1/S2` sa uz mozu porovnavat priamo s `S1_anchor/S2_anchor`, kedze seed anchors aj ludske ratingy pouzivaju rovnaku `1-5` skalu,
- transcript-level fidelity vetva (`A1-A9`, `symptom_error_mean`) potrebuje pri finalnom reporte opatrnu interpretaciu, lebo nejde o opakovany ludsky rating,
- smoke-run na templates nepredstavuje realny analyticky vysledok pre manuscript.

Pre aktualny stav to znamena, ze export aj pipeline uz bezia korektne, ale este stale nedostanes vsetko, co ocakava finalny manuscript bez dalsieho drafting passu:

- `manuscript/40_results.md`
- `docs/vo_h_model_results_map.md`
- Metoda v `manuscript/30_method.md`

## Najblizsi prakticky postup

1. Pri dalsom exporte najprv znovu spustit `python3 analysis/scripts/import_current_export_to_data_clean.py`.
2. Overit, ze `analysis/outputs/run_manifest.csv` stale sedi na ocakavane pocty a zdroj `data_clean`.
3. Spustit pipeline nad clean datami.
4. Rozhodnut, ci `severity_error` a `impact_error` pojdu do jadra reportu alebo len do supplementu.
5. Prepisat `manuscript/40_results.md` a `manuscript/50_discussion.md` podla aktualnych outputov.

## Kratka verzia

- Export je uz pripraveny aj v realnych clean suboroch.
- Potrebujes udrzat 4 clean CSV s presnymi ID a skalami a vediet ich reprodukovatelne obnovit.
- Najvacsie riziko uz nie je ingest, ale drift medzi outputmi a manuscript prose.
- Po dalsom exporte ma ist najprv ingest plus pipeline rerun, potom rewrite Results a Discussion.
