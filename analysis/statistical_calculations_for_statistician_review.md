# Statistical Calculations For Statistician Review

> Posledná aktualizácia: 2026-04-21
> Účel: mať na jednom mieste prehľad toho, aké štatistické výpočty sa v projekte aktuálne robia, v ktorých skriptoch sú implementované a ktoré z nich patria k pilotnej validácii seedov a rater dotazníka vs. k hlavným hypotézam diplomovky.

## 1. Source Of Truth

Tento projekt má momentálne dve analytické vrstvy:

1. `analysis/scripts/build_expert_review_outputs.py`
   - helper skript pre predbežnú expertnú obsahovú kontrolu seed scenárov a rater dotazníka,
   - nevykonáva inferenčné modely pre hypotézy `H1-H9`,
   - produkuje clean CSV a summary tabuľky pre pilotnú validáciu.

2. `analysis/scripts/thesis_rating_pipeline.R`
   - hlavný autoritatívny skript pre QC, deskriptívu, reliabilitu, `ICC`, mixed models, supplement a exporty,
   - je to hlavná štatistická vrstva pre diplomovku.

Prakticky:

- `validation / content review` = aktuálne helper Python vrstva
- `main thesis statistics` = R pipeline

Ak štatistik bude trvať na tom, že aj pilotná validačná vrstva má byť spracovaná v `R`, dá sa to neskôr portovať. Aktuálny stav však nie je jednotný `R-only` stack.

## 1.1 Čo Má Dostať Štatistik

Na reálne posúdenie nestačí len textový opis. Štatistik by mal dostať:

1. tento briefing:
   - `analysis/statistical_calculations_for_statistician_review.md`
2. helper validačný skript:
   - `analysis/scripts/build_expert_review_outputs.py`
3. hlavný inferenčný skript:
   - `analysis/scripts/thesis_rating_pipeline.R`
4. vstupné dáta pre pilotnú validáciu:
   - `analysis/validity data/data.xlsx`
   - alebo už vyčistené CSV v `analysis/data_clean/validation_experts_clean.csv`, `analysis/data_clean/rater_items_expert_review_clean.csv`, `analysis/data_clean/seeds_expert_review_clean.csv`
5. vstupné dáta pre hlavnú analýzu:
   - `analysis/data_clean/ratings_clean.csv`
   - `analysis/data_clean/transcripts_master.csv`
   - `analysis/data_clean/seed_anchors_final.csv`
   - `analysis/data_clean/raters_clean.csv`
6. ukážku aktuálnych výstupov:
   - `analysis/outputs/`
   - `tables/`
   - `figures/`

Minimum je teda:

- `markdown briefing`
- `oba skripty`
- `vstupné dáta`
- `jedna sada aktuálnych exportov`

Ak má štatistik robiť len metodický audit, toto stačí. Ak má robiť re-run alebo patch návrhu, potrebuje aj lokálne prostredie s `R` balíkmi a Python knižnicami.

## 1.2 Ako Sa To Spúšťa

Aktuálne sú oba skripty spustiteľné priamo bez CLI argumentov z koreňa repa.

Pilotná validačná vetva:

```bash
python3 analysis/scripts/build_expert_review_outputs.py
```

Hlavná diplomová analytika:

```bash
Rscript analysis/scripts/thesis_rating_pipeline.R
```

Čo je dôležité:

- Python helper skript číta raw workbook `analysis/validity data/data.xlsx` a produkuje clean CSV, summary tabuľky a preview výstupy.
- R pipeline číta `analysis/data_clean/*.csv`, vykoná QC, deskriptívu, reliabilitu, `ICC`, modely a exporty do `analysis/outputs/`, `tables/` a `figures/`.
- Pilotná validácia a hlavná inferenčná analytika sú teda oddelené aj dátovo, aj skriptovo.

## 1.3 Je Problém, Že Validácia Je V Pythone?

Sama o sebe nie.

Pre štatistika nie je rozhodujúce, či je skript v `R` alebo v `Python`, ale:

- či sú výpočty explicitne opísané,
- či vie dohľadať source of truth skript,
- či sú jasné vstupy a výstupy,
- či sú výsledky reprodukovateľné.

V tomto projekte je Python validačná vrstva obhájiteľná preto, že:

- nejde o hlavnú inferenčnú vetvu hypotéz,
- ide hlavne o prepis workbooku, deskriptívne summary, proporcie podpory a follow-up flagy,
- hlavná štatistika diplomovky aj tak beží v `R`.

Čo by už bolo slabšie:

- keby boli v Pythone skryté hlavné inferenčné modely,
- keby validačný skript nebol zdokumentovaný,
- keby briefing tvrdil `R-only` workflow, hoci repo je zmiešané.

Praktický záver pre audit:

- `Python helper for pilot validation` = prijateľné
- `R as main inferential stack` = stále čisté a obhájiteľné

Ak štatistik bude chcieť jednotný stack, najlogickejší kandidát na neskorší port do `R` je práve `build_expert_review_outputs.py`, nie hlavný pipeline.

## 2. Analytický Stack

### 2.1 Hlavná štatistika

Hlavná štatistická analýza beží v `R`.

Použité balíky v `analysis/scripts/thesis_rating_pipeline.R`:

- `readr`, `dplyr`, `tidyr`, `janitor`
- `ggplot2`
- `psych`
- `lme4`
- `lmerTest`
- `ordinal`
- `emmeans`
- `cluster`

### 2.2 Pomocná validačná vrstva

Pilotný expert review pass seedov a rater dotazníka je spracovaný helper skriptom:

- `analysis/scripts/build_expert_review_outputs.py`

Používa:

- `pandas`
- `openpyxl`
- `PIL`

Táto vrstva je určená hlavne na:

- prepis raw workbooku do clean CSV,
- výpočet jednoduchých priemerov a proporcií podpory,
- zoradenie položiek a seedov podľa slabších miest,
- prípravu preview tabuliek a heatmap.

Nejde o plnohodnotnú psychometrickú validáciu.

## 3. Časť A: Predbežná Validácia Seedov A Rater Dotazníka

## 3.1 Účel

Táto vetva má slúžiť ako:

- pilotný expert review pass,
- predbežná obsahová kontrola,
- dokumentácia toho, čo sa na základe expertnej spätnej väzby upravilo.

Nemá sa prezentovať ako:

- finálna validácia nástroja,
- plnohodnotný Delphi proces,
- samostatná psychometrická štúdia.

Rámec je opísaný v:

- `analysis/expert_content_review_framework.md`

## 3.2 Vstupy

Raw zdroj:

- `analysis/validity data/data.xlsx`

Helper clean výstupy:

- `analysis/data_clean/validation_experts_clean.csv`
- `analysis/data_clean/rater_items_expert_review_clean.csv`
- `analysis/data_clean/seeds_expert_review_clean.csv`

Hlavné summary výstupy:

- `analysis/outputs/expert_review_panel_summary.csv`
- `analysis/outputs/expert_review_panel_breakdown.csv`
- `analysis/outputs/expert_review_item_summary.csv`
- `analysis/outputs/expert_review_seed_summary.csv`
- `analysis/outputs/expert_review_comment_log.csv`

## 3.3 Jednotka Analýzy

Pre pilotnú validáciu sú tri rôzne jednotky:

1. `1 riadok = 1 expert`
   - panel summary a breakdown

2. `1 riadok = 1 expert x 1 položka dotazníka`
   - item review

3. `1 riadok = 1 expert x 1 seed`
   - seed review

## 3.4 Výpočty Pre Rater Dotazník

Skript: `analysis/scripts/build_expert_review_outputs.py`

Pre každú položku dotazníka a každého experta sa rátajú tri ratingy na škále `1-4`:

- `relevance_1_4`
- `clarity_1_4`
- `need_1_4`

Pre každý riadok `expert x item`:

```text
item_mean_1_4 = (relevance_1_4 + clarity_1_4 + need_1_4) / 3
```

Pre každú položku naprieč expertmi sa rátajú:

```text
relevance_mean_1_4 = mean(relevance_1_4)
clarity_mean_1_4 = mean(clarity_1_4)
need_mean_1_4 = mean(need_1_4)
```

Podiel podpory vyšších kategórií:

```text
relevance_support_3_4 = proportion(relevance_1_4 >= 3)
clarity_support_3_4 = proportion(clarity_1_4 >= 3)
need_support_3_4 = proportion(need_1_4 >= 3)
```

Agregované pomocné ukazovatele pre položku:

```text
overall_mean_1_4 =
  mean(relevance_mean_1_4, clarity_mean_1_4, need_mean_1_4)

overall_support_3_4 =
  mean(relevance_support_3_4, clarity_support_3_4, need_support_3_4)
```

Flag pre follow-up:

```text
follow_up_flag = min(
  relevance_support_3_4,
  clarity_support_3_4,
  need_support_3_4
) < 0.833
```

Poznámka:

- toto je proporčný threshold,
- pri aktuálnom paneli `n = 6` znamená `0.833` prakticky menej než `5/6` expertov s hodnotením `3-4`,
- nie je to formálne `I-CVI / S-CVI`, ale pragmatický pilotný support metric.

## 3.5 Výpočty Pre Seed Scenáre

Skript: `analysis/scripts/build_expert_review_outputs.py`

Každý expert hodnotí každý seed na škále `1-4` v 7 kritériách:

- `ambulatory_profile`
- `context_realism`
- `symptom_plausibility`
- `clarity`
- `information_sufficiency`
- `anti_stereotypy`
- `research_usefulness`

Pre každý riadok `expert x seed`:

```text
overall_mean_1_4 =
  mean(
    ambulatory_profile_1_4,
    context_realism_1_4,
    symptom_plausibility_1_4,
    clarity_1_4,
    information_sufficiency_1_4,
    anti_stereotypy_1_4,
    research_usefulness_1_4
  )
```

Pre severity je v skripte natvrdo definovaný target mapping `TARGET_SEVERITY`.

Pre každý riadok `expert x seed`:

```text
severity_matches_target =
  1 if severity_rating_code == target_severity_code
  0 otherwise
```

Pre každý seed naprieč expertmi sa rátajú:

- priemer pre každé kritérium,
- podiel podpory `3-4` pre každé kritérium,
- `overall_mean_1_4`,
- `overall_support_3_4 = proportion(overall_mean_1_4 >= 3)`,
- `target_match_share = mean(severity_matches_target)`,
- `n_comments`,
- `modal_severity_label`.

Flag pre severity follow-up:

```text
severity_follow_up_flag = target_match_share < 0.5
```

To znamená:

- seed ide na follow-up, ak menej než polovica expertov trafí cieľovú závažnosť.

## 3.6 Panel Summary

Skript: `analysis/scripts/build_expert_review_outputs.py`

Panel summary ráta:

- `n_experts`
- `n_item_review_rows`
- `n_seed_review_rows`
- `n_item_dimension_ratings`
- `n_seed_dimension_ratings`
- `n_seed_severity_ratings`
- `years_practice_median`
- `years_practice_min`
- `years_practice_max`
- počet expertov s komentárom k nástroju,
- počet expertov s celkovým seed komentárom,
- celkový počet zalogovaných komentárov.

Panel breakdown ráta počet a podiel pre:

- `profession`
- `specialization`
- `depression_experience`
- `interview_experience`
- `teaching_or_supervision_experience`
- `ai_experience`

## 3.7 Dôležité Metodické Poznámky K Validácii

- Toto nie je formálny `CVI` pipeline, hoci proporcie podpory `3-4` sa mu podobajú.
- Toto nie je formalizovaný `Delphi`.
- Hlavná hodnota tejto vetvy je:
  - zdokumentovať slabé položky,
  - zdokumentovať slabé seedy,
  - transparentne ukázať, čo sa po review upravilo.

Pre štatistika sú tu hlavné body na posúdenie:

1. či tento pilotný content-review framing stačí reportovať deskriptívne,
2. či má zmysel doplniť formálnejší `I-CVI` / `S-CVI`,
3. či thresholdy `0.833` a `0.5` dávajú zmysel alebo ich treba explicitnejšie obhájiť.

## 3.8 Väzba Na R Pipeline

Hlavný R pipeline expert review detailne nepočíta. V `analysis/scripts/thesis_rating_pipeline.R` iba:

- zistí, či clean expert review CSV existujú,
- spočíta počet riadkov,
- uloží jednoduché `expert_review_summary.csv`.

Teda:

- detailná validačná logika = `build_expert_review_outputs.py`
- hlavná inferenčná logika = `thesis_rating_pipeline.R`

## 4. Časť B: Hlavná Štatistická Analýza Pre Hypotézy

## 4.1 Vstupy

Hlavný analytický dataset vzniká joinom týchto 4 CSV:

- `analysis/data_clean/ratings_clean.csv`
- `analysis/data_clean/transcripts_master.csv`
- `analysis/data_clean/seed_anchors_final.csv`
- `analysis/data_clean/raters_clean.csv`

Join kľúče:

```text
ratings_clean.transcript_id = transcripts_master.transcript_id
ratings_clean.seed_id = seed_anchors_final.seed_id
ratings_clean.rater_id = raters_clean.rater_id
```

Jednotka analýzy:

```text
1 riadok = 1 hodnotenie 1 ratera na 1 transkripte
```

## 4.2 Premenné

Hlavné prediktory:

- `guardrail`
- `profile`

Náhodné efekty:

- `seed_id`
- `rater_id`

Primárne outcome-y:

- `G1-G5`
- `plausibility_index`

Sekundárne outcome-y:

- `A1-A9`
- `symptom_error_mean`
- `S1`
- `S2`
- doplnkovo `severity_error`
- doplnkovo `impact_error`

QC / defect outcome-y:

- `R1-R5`
- `defect_index`

Exploratórne outcome-y:

- `guessed_origin`
- `guess_confidence`
- `comment`

## 4.3 Odvodené Premenné

Skript: `analysis/scripts/thesis_rating_pipeline.R`

### 4.3.1 Index klinickej vierohodnosti

```text
plausibility_index = mean(G1, G3, G4)
```

### 4.3.2 Index defektov

```text
defect_index = mean(R1, R2, R3, R4, R5)
```

### 4.3.3 Položkové anchor chyby A1-A9

Pre každú symptomatickú doménu:

```text
A_i_error = abs(A_i - A_i_anchor)
```

### 4.3.4 Priemerná absolútna chyba symptom fidelity

```text
symptom_error_mean =
  mean(
    A1_error, A2_error, A3_error, A4_error, A5_error,
    A6_error, A7_error, A8_error, A9_error
  )
```

### 4.3.5 Priame severity / impact error skóre

```text
severity_error = abs(S1 - S1_anchor)
impact_error = abs(S2 - S2_anchor)
```

Aktuálna logika repa je:

- seed anchors `S1_anchor` a `S2_anchor` sú zarovnané na `1-5`,
- žiadna dodatočná harmonizácia sa už nerobí,
- ide o priame error skóre.

## 4.4 QC A Deskriptíva

### 4.4.1 QC summary

Pipeline vytvára:

- počty raterov, transkriptov, seedov, ratingov,
- priemerný počet ratingov na transkript,
- minimum a maximum ratingov na transkript,
- counts podľa `guardrail`,
- counts podľa `profile`,
- counts podľa `guardrail x profile`.

### 4.4.2 Deskriptíva položiek

Pre:

- `G1-G5`
- `A1-A9`
- `S1`
- `S2`
- `R1-R5`
- `guess_confidence`

sa rátajú:

```text
n_non_missing
levels_used
median
IQR
mean
SD
min
max
```

Poznámka:

- `A1-A9` sa sumarizujú po agregácii na `1 riadok = 1 transkript`, nie rating-weighted cez long dáta.

### 4.4.3 Deskriptíva kompozitov

Pre:

- `plausibility_index`
- `defect_index`
- `symptom_error_mean`
- podľa dostupnosti aj `severity_error`
- podľa dostupnosti aj `impact_error`

sa rátajú:

```text
n_non_missing
mean
SD
median
IQR
min
max
```

Poznámka:

- `plausibility_index` a `defect_index` ostávajú rating-level kompozity.
- `symptom_error_mean`, `severity_error` a `impact_error` sa reportujú na transcript-level summary, aby sa anchor fidelity vetva nevážila počtom raterov.

## 4.5 Vnútorná Konzistencia

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `compute_alpha_omega()`

Bloky:

- `G1-G5`
- `G1, G3, G4`
- `R1-R5`

Výpočty:

```text
alpha = psych::alpha(...)
omega = psych::omega(..., nfactors = 1)
```

Interpretácia:

- reportovať len jednu explicitne pomenovanú verziu omegy, teda `omega total` z `psych::omega(..., nfactors = 1)`;
- ak by prose používalo inú verziu alebo nejasný estimator, treba to zosúladiť alebo omegu z textu vypustiť.

Skip pravidlo:

```text
if n_items < 2 or n_rows < 3 -> skipped
```

## 4.6 Interrater Agreement

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `compute_icc()`

Outcome-y:

- `plausibility_index`
- `defect_index`
- `S1`
- `S2`

Implementácia:

- long data sa preklopia do `transcript x rater` wide matice,
- potom sa používa `psych::ICC(...)`,
- reportovaný je riadok:

```text
ICC2k
```

Skip pravidlá:

```text
if < 2 transcripts or < 2 raters -> skipped
if < 2 non-empty rater columns -> skipped
```

## 4.7 Hlavné Inferenčné Modely

## 4.7.1 LMM pre rater-level numerické outcome-y

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `fit_lmm()`

Formula:

```text
outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)
```

Outcome-y:

- `plausibility_index`
- `defect_index`

Odhady:

- fixed effects coefficients,
- p-hodnoty z `lmerTest` so Satterthwaite aproximáciou,
- Wald CI cez `confint(..., method = "Wald")`,
- `emmeans` pre `guardrail x profile`,
- diagnostické poznámky v stĺpci `detail`, najmä pri singularite alebo konvergenčných upozorneniach.

Skip pravidlo:

```text
nrow >= 8
and >= 2 levels of guardrail
and >= 2 levels of profile
and >= 2 seeds
and >= 2 raters
```

Doplnkový sensitivity model:

```text
outcome ~ guardrail * profile + (1 | seed_id) + (1 | transcript_id) + (1 | rater_id)
```

Táto sensitivity vetva sa aktuálne exportuje samostatne pre `plausibility_index` a `defect_index`. Jej funkciou je robustness check, nie náhrada hlavného modelu.

## 4.7.2 Transcript-level LMM

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `fit_transcript_lmm()`

Najprv sa vytvorí:

```text
transcript_level_summary =
  mean outcome naprieč raters pre každý transcript
```

Formula:

```text
outcome ~ guardrail * profile + (1 | seed_id)
```

Outcome-y:

- `symptom_error_mean`
- podľa dostupnosti `severity_error`
- podľa dostupnosti `impact_error`

Odhady:

- p-hodnoty z `lmerTest` so Satterthwaite aproximáciou,
- Wald CI cez `confint(..., method = "Wald")`,
- diagnostické poznámky v stĺpci `detail`, najmä pri singularite alebo konvergenčných upozorneniach.

Skip pravidlo:

```text
nrow >= 8
and >= 2 levels of guardrail
and >= 2 levels of profile
and >= 2 seeds
```

## 4.7.3 CLMM pre ordinálne outcome-y

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `fit_clmm()`

Formula:

```text
ordered(response) ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)
```

Outcome-y:

- `G2`
- `G5`
- `S1`
- `S2`
- `guess_confidence`

Odhady:

- koeficienty,
- `z`,
- `p`,
- približné Wald `95 % CI`:

```text
conf_low = Estimate - 1.96 * SE
conf_high = Estimate + 1.96 * SE
```

Poznámka:

- raw export `clmm_item_models.csv` obsahuje aj threshold/cut-point termy,
- hlavná core tabuľka pre hypotézy ich filtruje a ponecháva len efektové termy s `guardrail`, `profile` a ich interakciou,
- stĺpec `detail` nesie minimálne počet použitých response kategórií a prípadnú poznámku ku konvergencii.

Skip pravidlo:

```text
nrow >= 8
and >= 2 response levels
and >= 2 levels of guardrail
and >= 2 levels of profile
and >= 2 seeds
and >= 2 raters
```

## 4.8 Mapovanie Na Hypotézy

Aktuálne mapovanie na `H1-H9`:

- `H1`: `plausibility_index`
- `H2`: `G2`
- `H3`: `defect_index`
- `H4`: primárne `symptom_error_mean`, sekundárne `severity_error`, `impact_error`, deskriptívne `S1`, `S2`
- `H5`: `G5`
- `H6`: efekt `profile` na `plausibility_index`
- `H7`: efekt `profile` na `G2`, `G5`
- `H8`: efekt `profile` na `symptom_error_mean`, sekundárne `severity_error`, `impact_error`, `defect_index`
- `H9`: interakcia `guardrail x profile` nad hlavnými kompozitmi a error-based outcome-mi

Praktická mapa je aj v:

- `docs/vo_h_model_results_map.md`

## 4.9 Explorácie Mimo Jadra H1-H9

### 4.9.1 Spearman transcript-level korelácie

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `compute_spearman_matrix()`

Premenné:

- `plausibility_index`
- `defect_index`
- `symptom_error_mean`
- `g2`
- `g5`

Výpočet:

```text
cor(..., method = "spearman", use = "pairwise.complete.obs")
```

Skip pravidlo:

```text
at least 3 transcripts
and at least 2 variables
```

### 4.9.2 PAM typológia transkriptov

Skript: `analysis/scripts/thesis_rating_pipeline.R`

Funkcia:

- `run_pam_analysis()`

Premenné:

- `plausibility_index`
- reverzný `defect_index`
- reverzný `symptom_error_mean`
- `g2`
- `g5`
- podľa dostupnosti reverzný `severity_error`
- podľa dostupnosti reverzný `impact_error`

Postup:

1. transcript-level agregácia
2. reverzia premenných, kde vyššie = horšie
3. `scale(...)`
4. `pam(k = 2..4)`
5. výber podľa najvyššieho `silhouette`
6. cluster assignments, profiles, crosstab, medoids, MDS coordinates

Skip pravidlá:

```text
at least 4 transcripts
at least 3 variables
at least 4 complete transcript rows after NA drop
```

Poznámka:

- toto je doplnkový appendix,
- nie jadro testovania hypotéz.

## 5. Krátke Otázky Pre Štatistika

Toto sú body, ktoré by mal štatistik explicitne posúdiť:

1. Je rozumné používať `ICC2k` ako hlavný agreement index pre kompozity a `S1/S2`, alebo by bolo vhodnejšie doplniť weighted agreement metric pre ordinálne ratingy?
2. Je obhájiteľné brať `plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error`, `impact_error` ako približne intervalové outcome-y pre `LMM`?
3. Je pre túto diplomovku prijateľné používať pri `LMM` p-hodnoty z `lmerTest` so Satterthwaite aproximáciou a zároveň reportovať aj Wald `95 % CI` a modelové diagnostické poznámky?
4. Má `severity_error` a `impact_error` ostať len ako secondary / supplement vetva, alebo sa dajú obhájiť aj v jadre?
5. Má pilotný expert review ostať pri priemeroch a support proporciách, alebo doplniť formálnejší `I-CVI` / `S-CVI`?
6. Je transcript-level model pre `symptom_error_mean` s random interceptom len pre `seed_id` dostatočný, alebo by bolo vhodné iné riešenie pri plnom datasete?
7. Je `PAM` vhodné ponechať ako appendix, alebo ho pri finálnom reporte radšej vypustiť, ak nebude veľmi stabilné?

## 6. Najkratšia Verzia

- `validation seedov a dotazníka` = aktuálne helper Python skript s priemermi, support proporciami a follow-up flagmi
- `hlavná diplomová analytika` = R pipeline
- `jadro hypotéz` = deskriptíva + `alpha/omega` + `ICC` + `LMM` + `CLMM`
- `doplnok` = Spearman transcript-level korelácie + `PAM`
