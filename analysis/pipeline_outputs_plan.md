# Pipeline Outputs Plan

> Posledna aktualizacia: 2026-04-11
> Ucel: presne zafixovat, ake vystupy ma generovat analyticka pipeline pre manuscript, Word workflow a doplnkovy appendix.

## 1. Rozdelenie vystupov

Pipeline ma produkovat tri vrstvy vystupov:

1. `analysis/outputs/` — technicke a analyticke medzivystupy, ktore sa daju znovu pouzit pri dalsom spracovani.
2. `tables/` — manuscript-ready tabulky pre hlavny text a supplement.
3. `figures/` — manuscript-ready grafy pre hlavny text a supplement.

Exploracia otvorenych komentarov ostava manualna alebo polo-manualna; pipeline ma pre nu pripravit len pomocne summary, nie definitivne tematicke kodovanie.

## 2. Core vystupy pre hlavny text

### 2.1 `analysis/outputs/`

- `analysis_long.csv`
  - clean long dataset po joins a odvodenych premennych
- `qc_dataset_summary.csv`
  - pocet hodnotitelov, transkriptov, seedov, ratingov, priemerny pocet ratingov na transkript, minimum, maximum, counts podla `guardrail`, `profile`, `guardrail x profile`
- `descriptives_items.csv`
  - frekvencie, mediány a IQR pre `G1-G5`, `A1-A9`, `S1`, `S2`, `R1-R5`, `guess_confidence`
- `descriptives_composites.csv`
  - mean, SD, median, IQR, min, max pre `plausibility_index`, `defect_index`, `symptom_error_mean`
  - `severity_error` a `impact_error` ako priame `1-5` error skore medzi ľudskym `S1/S2` a seed anchors
- `expert_review_summary.csv`
  - pocet expertov, pocet posudenych poloziek, pocet posudenych seedov, pocet odporucanych uprav, najcastejsie typy pripomienok
- `internal_consistency.csv`
  - `alpha` a `omega` pre blok `G1-G5`, pre blok `G1-G3-G4` a pre blok `R1-R5`
- `icc_summary.csv`
  - zvoleny typ `ICC`, odhady, 95 % CI, interpretacna kategoria pre `plausibility_index`, `defect_index`, `S1`, `S2`
- `lmm_core_models.csv`
  - tidy summary pre `plausibility_index`, `defect_index`
  - transcript-level modelovy prehlad pre `symptom_error_mean`
  - transcript-level modelovy prehlad aj pre `severity_error` a `impact_error`
- `clmm_item_models.csv`
  - tidy summary pre `G2`, `G5`, `S1`, `S2` a `guess_confidence`
- `emmeans_core_models.csv`
  - estimated marginal means a planovane kontrasty pre hlavne outcome-y
- `guess_origin_summary.csv`
  - frekvencie a podiely kategorii `guessed_origin` celkovo aj podla `guardrail`, `profile`, `guardrail x profile`
- `guess_origin_logit.csv`
  - summary logistickeho modelu pre binarizovanu premennu `perceived_ai` s prediktormi `plausibility_index` a `defect_index`
- `comment_summary_stub.csv`
  - pomocny export komentarov s ID transkriptu, ID ratera a textom pre manualne tematicke kodovanie

### 2.2 `tables/`

- `table_1_dataset_summary.csv`
  - zdroj pre Tabulku 1 v Results
- `table_2_descriptives.csv`
  - zdroj pre Tabulku 2
- `table_3_item_frequencies.csv`
  - zdroj pre Tabulku 3
- `table_4_internal_consistency.csv`
  - zdroj pre Tabulku 4
- `table_5_icc.csv`
  - zdroj pre Tabulku 5
- `table_6_mixed_models_core.csv`
  - zdroj pre Tabulku 6; zahrna LMM aj klucove CLMM vystupy v kompaktnej forme

### 2.3 `figures/`

- `figure_1_primary_outcomes_by_condition.png`
  - boxploty alebo violin+box pre `plausibility_index` a `defect_index` podla `guardrail x profile`
- `figure_2_emmeans_core_models.png`
  - estimated marginal means s 95 % CI pre `plausibility_index` a `defect_index`; podla potreby facet aj pre `symptom_error_mean`

## 3. Doplnkove vystupy pre supplement / appendix

Tieto vystupy nie su jadrom testovania `H1-H9`. Sluzia ako opatrna doplnkova exploracia a maju byt v texte explicitne oznacene ako supplement alebo appendix.

### 3.1 Spearman korelacie na urovni transkriptov

Najprv sa pripravi transcript-level agregat, teda priemerne hodnoty napriec ratermi pre kazdy transkript. Korelacna matica sa potom pocita len na tychto agregatoch, nie na long datasete, aby sa neporusila logika nezavislych jednotiek.

#### `analysis/outputs/`

- `transcript_level_summary.csv`
  - 1 riadok = 1 transkript; obsahuje `guardrail`, `profile`, `seed_id` a transcript-level priemery hlavných kompozitov a vybraných poloziek
- `spearman_transcript_composites.csv`
  - Spearmanova korelacna matica pre `plausibility_index`, `defect_index`, `symptom_error_mean`, `G2`, `G5`

#### `tables/`

- `table_s1_spearman_transcript_composites.csv`
  - supplementarna korelacna tabulka

#### `figures/`

- `figure_s1_spearman_heatmap.png`
  - heatmap korelacnej matice

### 3.2 Exploratorna typologia transkriptov cez `PAM`

`PAM` sa ma robit len na transcript-level agregatoch. Vstupne premenné maju byt pred klastrovanim standardizovane; premenné, kde vyssia hodnota znamena horsi vysledok (`defect_index`, `symptom_error_mean`, `severity_error`, `impact_error`), sa maju reverzne orientovat tak, aby vyssie hodnoty konzistentne znamenali lepsiu kvalitu. Odporucany set premennych:

- `plausibility_index`
- reverzny `defect_index`
- reverzny `symptom_error_mean`
- `G2`
- `G5`

Ako sensitivity appendix je mozne doplnit aj:

- reverzny `severity_error`
- reverzny `impact_error`

Porovnavaju sa len riesenia s `k = 2` az `k = 4`. Do supplementu sa zaradi iba riesenie, ktore bude zaroven interpretovatelne a podporene aspon zakladnym indexom kvality riesenia, najma silhouette.

#### `analysis/outputs/`

- `pam_input_transcript_level.csv`
  - vstupna tabulka pre PAM po agregacii, orientacii smeru a standardizacii
- `pam_model_selection.csv`
  - prehlad rieseni `k = 2-4`, silhouette a velkosti klastrov
- `pam_cluster_assignments.csv`
  - priradenie transkriptov ku klastrom
- `pam_cluster_profiles.csv`
  - priemery alebo mediany vstupnych premennych podla klastrov
- `pam_cluster_condition_crosstab.csv`
  - cross-tab klaster x `guardrail`, klaster x `profile`, klaster x `guardrail x profile`
- `pam_cluster_medoids.csv`
  - identifikacia medoidov, teda reprezentativnych transkriptov pre kazdy klaster

#### `tables/`

- `table_s2_pam_cluster_profiles.csv`
  - supplementarna tabulka profilov klastrov
- `table_s3_pam_cluster_by_condition.csv`
  - supplementarna tabulka rozlozenia klastrov podla experimentálnych podmienok

#### `figures/`

- `figure_s2_pam_cluster_map.png`
  - 2D vizualizacia klastrov, napriklad cez PCA alebo MDS

## 4. Poznamky k modelom a poradiu reportovania

- Jadro inferencie tvoria komparacie medzi podmienkami cez `LMM` a `CLMM`, nie korelacie a nie klastrovanie.
- `S1` a `S2` su v jadre vedene ako samostatne human-rated ordinal outcome-y; popri nich sa teraz daju reportovat aj priame error ukazovatele voci `S1_anchor` a `S2_anchor`, kedze skaly su zarovnane na `1-5`.
- Planovane kontrasty pre `profile` maju byt primarne `R3 vs R1`; `R2 vs R1` a `R3 vs R2` maju byt sekundarne.
- Pri signifikantnej interakcii `guardrail x profile` sa maju reportovat simple effects, nie plosne vsetky parove porovnania.
- Korelacna matica a `PAM` maju byt interpretovane len ako doplnkovy opis struktury dat, nie ako dokaz pre `H1-H9`.
- Ak `PAM` nebude dostatocne stabilny alebo interpretovatelny, vystupy sa mozu ponechat len v `analysis/outputs/` a do manuscriptu ich nezaradovat.

## 5. Minimalny set pre prve run-ready spracovanie

Ak je cielom prvy plnohodnotny beh pipeline, minimalny set hotovych vystupov je:

1. `analysis_long.csv`
2. `qc_dataset_summary.csv`
3. `internal_consistency.csv`
4. `icc_summary.csv`
5. `lmm_core_models.csv`
6. `clmm_item_models.csv`
7. `table_1_dataset_summary.csv`
8. `table_2_descriptives.csv`
9. `table_4_internal_consistency.csv`
10. `table_5_icc.csv`
11. `table_6_mixed_models_core.csv`
12. `figure_1_primary_outcomes_by_condition.png`
13. `figure_2_emmeans_core_models.png`

Spearmanova matica a `PAM` mozu nasledovat az v druhom passe po stabilizacii jadra.
