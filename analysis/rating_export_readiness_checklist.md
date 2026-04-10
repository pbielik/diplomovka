# Rating Export Readiness Checklist

> Posledna aktualizacia: 2026-04-10
> Ucel: mat na jednom mieste presne napisane, co musia obsahovat realne exporty pre analyzu a co dnes este nepokryva samotna pipeline.

## Verdikt

Analyticka vetva je konceptualne pripravena, ale este nie je `run-ready` na realnych datach bez dvoch krokov:

1. dostat realne clean vstupy do `analysis/data_clean/`,
2. upravit pipeline tak, aby citala clean vstupy namiesto template CSV a produkovala vystupy, ktore rukopis skutocne ocakava.

Najblizsi blocker teda uz nie je literatura, ale **kvalita a konzistencia exportu**.

## Povinne vstupne subory

V `analysis/data_clean/` maju byt pripravené tieto 4 subory:

1. `ratings_clean.csv`
2. `transcripts_master.csv`
3. `seed_anchors_final.csv`
4. `raters_clean.csv`

Aktualny skript `analysis/scripts/thesis_rating_pipeline.R` este stale cita `analysis/templates/*.csv`, nie tieto clean subory. To je znamy technicky gap, nie problem exportu samotneho.

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
- `A1` az `A9`, `S1`, `S2`, `R1` az `R5`: iba `0` az `3`
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
- `A*_anchor`, `S1_anchor`, `S2_anchor` musia byt na skale `0` az `3`.
- Toto je zdroj pravdy pre:
  - `symptom_error_mean`
  - `severity_error`
  - `impact_error`

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
- `years_practice` musi byt numericky parsovatelne.
- `experience_with_mdd` ma byt konzistentne kodovane, idealne `0/1`.

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

## Co pipeline dnes este nepokryva

Aktualny `analysis/scripts/thesis_rating_pipeline.R` je stale len kostra. Dnes:

- cita `analysis/templates/*.csv`, nie `analysis/data_clean/*.csv`
- nepouziva `transcripts_master.csv` na QC ani join logiku
- pocita len:
  - `plausibility_index`
  - `defect_index`
  - `symptom_error_mean`
  - `severity_error`
  - `impact_error`
- realne modeluje len:
  - `plausibility_index`
  - `defect_index`
  - `symptom_error_mean`
- robi len 2 alpha vypocty a neprodukuje:
  - `omega`
  - blok `R1-R5`
  - `ICC`
  - item-level ordinal models pre `G2`, `G5`, `G1`, `G3`, `G4`, `R1-R5`
  - exploracne modely pre `guessed_origin`, `guess_confidence`
- negeneruje tabulky a grafy do `tables/` a `figures/`

To znamena, ze realny export moze byt pripraveny spravne, ale bez dalsieho pipeline passu este nedostanes vsetko, co ocakava:

- `manuscript/40_results.md`
- `docs/vo_h_model_results_map.md`
- Metoda v `manuscript/30_method.md`

## Najblizsi prakticky postup

1. Vyexportovat realne clean subory do `analysis/data_clean/`.
2. Skontrolovat ich proti tomuto checklistu.
3. Dorobit pipeline tak, aby:
   - citala clean vstupy,
   - spravila QC summary,
   - pocitala alpha aj omega,
   - vyratala `ICC`,
   - pridala hlavne ordinal / mixed model vystupy pre H1 az H9,
   - zapisala vystupy do `analysis/outputs/`, `tables/` a `figures/`.
4. Az potom doplnat `manuscript/40_results.md`.

## Kratka verzia

- Export je pripraveny v logike, nie v realnych suboroch.
- Potrebujes 4 clean CSV s presnymi ID a skalami.
- Najvacsie riziko nie je statistika, ale rozbite joins a nekonzistentne codingy.
- Ked budu clean CSV hotove, dalsi krok ma byt pipeline patch, nie dalsia literatura.
