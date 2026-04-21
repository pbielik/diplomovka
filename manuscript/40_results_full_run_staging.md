# 3 Vysledky

> Status: pre-final staging scaffold pre posledny full run.
> Funkcia sekcie: urychlit posledny prepis `40_results.md` po finalnom exporte tak, aby kazda veta mala jasny zdroj v `analysis/outputs/`, `tables/` alebo `figures/`.
> Nepouzivaj tento subor ako finalny manuscript text bez manualneho prepisu a bez nahradenia tokenov `[[...]]`.

## Ako tento scaffold pouzit

1. Dokonci `analysis/final_run_playbook.md`.
2. Nahrad tokeny `[[...]]` podla uvedenych source files.
3. Ak niektory blok ostane `NA`, `failed` alebo `skipped`, pouzi fallback vetu uvedenu v danej sekcii.
4. Az potom prenes vysledny prose do `manuscript/40_results.md`.

## Outline finalneho Results

1. Predbezna expertna obsahova kontrola ratingoveho nastroja a seed scenarov
2. Charakteristika finalneho ratingoveho datasetu
3. Distribucne a frekvencne charakteristiky ratingov
4. Kvalita merania a zhoda hodnotitelov
5. Deskriptivne profily podla experimentalych buniek
6. Hlavne inferencne bloky podla `VO` a hypotet
7. Transcript-level ukazovatele odchylky voci referencnym seed hodnotam
8. Exploratorne vystupy
9. Strucne zhrnutie vysledkov

## 3.1 Predbezna expertna obsahova kontrola ratingoveho nastroja a seed scenarov

Function:
- stabilny uvodny blok, ktory sa meni len vtedy, ak sa meni expert review vrstva

Source files:
- `analysis/outputs/expert_review_summary.csv`
- `tables/table_s4_expert_review_items.csv`
- `tables/table_s5_expert_review_seeds.csv`
- `figures/figure_s3_expert_review_items_heatmap.png`
- `figures/figure_s4_expert_review_seeds_heatmap.png`

Draft skeleton:

Este pred hlavnym hodnotenim transkriptov prebehla samostatna expertna obsahova kontrola autorskeho ratingoveho nastroja a seed scenarov. Do tejto vrstvy bolo zapojenych `[[EXPERT_N]]` expertov s medianom odbornej praxe `[[EXPERT_PRACTICE_MEDIAN]]` rokov (rozsah `[[EXPERT_PRACTICE_RANGE]]`). Vzniklo pritom `[[EXPERT_ITEM_REVIEW_ROWS]]` hodnoteni poloziek ratingoveho nastroja, `[[EXPERT_SEED_REVIEW_ROWS]]` hodnoteni seed scenarov a `[[EXPERT_COMMENT_N]]` kvalitativnych komentarov.

Pri polozkach ratingoveho nastroja sa celkove priemery pohybovali priblizne od `[[ITEM_MEAN_MIN]]` do `[[ITEM_MEAN_MAX]]` na stvorbodovej skale. Najsilnejsie boli podporene `[[ITEMS_STRONGEST]]`, zatial co slabsie dopadli najma `[[ITEMS_WEAKEST]]`. Pri seed scenaroch sa celkove priemery pohybovali priblizne od `[[SEED_MEAN_MIN]]` do `[[SEED_MEAN_MAX]]`, pricom eksperti najcastejsie upozornovali na `[[SEED_MAIN_COMMENT_THEMES]]`.

Tento blok nepredstavuje finalnu psychometricku validaciu ani formalny Delphi proces. Jeho funkciou je ukazat, ze ratingovy nastroj a seed scenare presli pred hlavnym zberom dat obsahovou kontrolou a ze slabiny sa sustredovali najma v `[[EXPERT_REVIEW_MAIN_RISK_AREA]]`.

## 3.2 Charakteristika finalneho ratingoveho datasetu

Function:
- ukazat jednotku analyzy, finalne pocty a pripadne nevyvazenie buniek

Source files:
- `analysis/outputs/run_manifest.csv`
- `analysis/outputs/qc_dataset_summary.csv`
- `tables/table_1_dataset_summary.csv`

Draft skeleton:

Analyzovany dataset obsahoval spolu `[[N_RATINGS]]` expertnych hodnoteni, ktore sa vztahovali na `[[N_TRANSCRIPTS]]` transkriptov odvodenych z `[[N_SEEDS]]` seed scenarov. V datasete vystupovalo `[[N_RATERS]]` hodnotitelov a na jeden transkript pripadalo v priemere `[[MEAN_RATINGS_PER_TRANSCRIPT]]` hodnotenia (rozsah `[[MIN_RATINGS_PER_TRANSCRIPT]]` az `[[MAX_RATINGS_PER_TRANSCRIPT]]`). Zakladne charakteristiky datasetu sumarizuje Tabulka 1.

Na urovni experimentaleho dizajnu bol zastupeny kompletny faktorovy plan `2 x 3`, teda vsetky kombinacie pritomnosti strukturujuceho klinickeho usmernenia a stylu odpovedania simulovaneho pacienta. Pokrytie buniek vsak bolo `[[CELL_BALANCE_SUMMARY]]`: `off x P1 = [[CELL_OFF_P1]]`, `off x P2 = [[CELL_OFF_P2]]`, `off x P3 = [[CELL_OFF_P3]]`, `on x P1 = [[CELL_ON_P1]]`, `on x P2 = [[CELL_ON_P2]]`, `on x P3 = [[CELL_ON_P3]]`.

Tato struktura datasetu uz umoznuje inferencne modelovanie, no pri interpretacii treba zohladnit `[[RATER_PANEL_NOTE]]`.

## 3.3 Distribucne a frekvencne charakteristiky ratingov

Function:
- najprv ukazat overall level outcome-ov, potom frekvencne rozdelenie poloziek

Source files:
- `tables/table_2_descriptives.csv`
- `tables/table_3_item_frequencies.csv`
- `figures/figure_1a_plausibility_index_by_condition.png`
- `figures/figure_1b_defect_index_by_condition.png`

Draft skeleton:

Na urovni hlavnych kompozitov dosiahol index klinickej vierohodnosti priemernu hodnotu `[[PLAUSIBILITY_MEAN]]` (`SD = [[PLAUSIBILITY_SD]]`, median = `[[PLAUSIBILITY_MEDIAN]]`, `IQR = [[PLAUSIBILITY_IQR]]`, rozsah `[[PLAUSIBILITY_MIN]]` az `[[PLAUSIBILITY_MAX]]`). Index defektov dosiahol priemer `[[DEFECT_MEAN]]` (`SD = [[DEFECT_SD]]`, median = `[[DEFECT_MEDIAN]]`, `IQR = [[DEFECT_IQR]]`, rozsah `[[DEFECT_MIN]]` az `[[DEFECT_MAX]]`).

Podobne vyzneli aj klucove jednotlive polozky. Prirodzenost jazyka (`G2`) dosiahla priemer `[[G2_MEAN]]` (`SD = [[G2_SD]]`) a treningova pouzitelnost (`G5`) priemer `[[G5_MEAN]]` (`SD = [[G5_SD]]`). Odhad celkovej zavaznosti (`S1`) mal priemer `[[S1_MEAN]]` a odhad funkcneho dopadu (`S2`) priemer `[[S2_MEAN]]`. Vo viacerych blokoch pritom median aj `IQR` ostavali stlacene v uzkom pasme, co naznacuje `[[DISTRIBUTION_COMPRESSION_NOTE]]`.

Frekvencne rozdelenia poloziek ukazuju, ze pri polozkach `G1-G5` dominovala najma odpoved `[[G_BLOCK_MODAL_RESPONSE]]`, zatial co pri polozkach `R1-R5` prevladali kategorie `[[R_BLOCK_MODAL_RESPONSE]]`. Defekty preto boli vo vacsine pripadov hodnotene ako `[[DEFECT_LEVEL_SUMMARY]]`.

## 3.4 Kvalita merania a zhoda hodnotitelov

Function:
- oddelit vnutornu konzistenciu od interrater vrstvy

Source files:
- `tables/table_4_internal_consistency.csv`
- `tables/table_5_icc.csv`
- `analysis/outputs/internal_consistency.csv`
- `analysis/outputs/icc_summary.csv`

Draft skeleton:

Predbezna vnutorna konzistencia ratingoveho nastroja bola na tomto datasete interpretacne pouzitelna. Pre blok globalnych poloziek `G1-G5` dosiahlo Cronbachovo `alpha = [[ALPHA_G1_G5]]` a McDonaldovo `omega total (1f) = [[OMEGA_G1_G5]]`. Pri jadrovom kompozite klinickej vierohodnosti (`G1`, `G3`, `G4`) boli odhady `alpha = [[ALPHA_PLAUSIBILITY_CORE]]` a `omega = [[OMEGA_PLAUSIBILITY_CORE]]`; pri defektovom bloku `R1-R5` dosiahli `alpha = [[ALPHA_R1_R5]]` a `omega = [[OMEGA_R1_R5]]`.

Fallback veta pre interrater blok, ak `ICC` ostane neodhadnutelny:

Interrater zhoda ostala na tomto datasete metodicky limitovana. Hoci panel uz obsahoval viac hodnotitelov, `ICC` odhady pre jadrove outcome-y neboli v aktualnom spracovani reportovatelne, a preto tento blok ostava interpretovany opatrne len ako meracia poznamka, nie ako nosny dokaz kvality merania.

Variant A, ak `ICC` bude odhadnutelny:

Zhoda medzi hodnotitelmi bola pri jadrovych outcome-och `[[ICC_INTERPRETATION_SUMMARY]]`. Pre index klinickej vierohodnosti vyslo `ICC2k = [[ICC_PLAUSIBILITY]]` (`95 % CI [[ICC_PLAUSIBILITY_CI]]`), pre index defektov `[[ICC_DEFECT]]`, pre `S1` `[[ICC_S1]]` a pre `S2` `[[ICC_S2]]`.

Variant B, ak `ICC` ostane `NA`:

Aj pri finalnom rune ostala interrater vrstva limitovana a `ICC` odhady pre jadrove outcome-y neboli v aktualnom spracovani numericky reportovatelne. Vo vysledkoch preto tato cast funguje len ako transparentne priznanie limitu panelu, nie ako samostatny nosny argument.

## 3.5 Deskriptivne profily podla experimentalnych buniek

Function:
- ukazat cell-level patterny bez preinterpretovania

Source files:
- `analysis/outputs/analysis_long.csv`
- `analysis/outputs/transcript_level_summary.csv`
- `figures/figure_1a_plausibility_index_by_condition.png`
- `figures/figure_1b_defect_index_by_condition.png`
- `tables/styled_preview/results_preview.html`

Draft skeleton:

Na urovni indexu klinickej vierohodnosti sa priemery medzi bunkami pohybovali v uzkom pasme `[[PLAUSIBILITY_CELL_RANGE]]`. Najvyssia deskriptivna hodnota sa objavila v bunke `[[PLAUSIBILITY_CELL_MAX_LABEL]]`, najnizsia v `[[PLAUSIBILITY_CELL_MIN_LABEL]]`, no rozdiely medzi bunkami boli male. Pri indexe defektov bolo rozpatie `[[DEFECT_CELL_RANGE]]`; najslabsie vysla bunka `[[DEFECT_CELL_MAX_LABEL]]`, najpriaznivejsie `[[DEFECT_CELL_MIN_LABEL]]`.

Pri jednotlivych polozkach sa objavilo o nieco viac variability. Prirodzenost jazyka (`G2`) bola deskriptivne najvyssia v `[[G2_CELL_MAX_LABEL]]`, treningova pouzitelnost (`G5`) v `[[G5_CELL_MAX_LABEL]]`, zatial co najnizsie priemery sa objavili v `[[LOWER_CELL_PATTERN_SUMMARY]]`. Tento blok ma len orientacnu funkciu a pripravuje podu pre inferencne modely v nasledujucej sekcii.

## 3.6 Hlavne inferencne bloky podla VO a hypotet

Function:
- odpovedat na konfirmacne bloky A-C bez rozsiahlej interpretacie

Source files:
- `tables/table_6_mixed_models_core.csv`
- `tables/table_s6_lmm_sensitivity_transcript_id.csv`
- `analysis/outputs/lmm_core_models.csv`
- `analysis/outputs/lmm_sensitivity_transcript_id_models.csv`
- `analysis/outputs/clmm_item_models.csv`
- `analysis/outputs/emmeans_core_models.csv`
- `docs/vo_h_model_results_map.md`

### 3.6.1 Efekt strukturujuceho klinickeho usmernenia na globalnu kvalitu interview

Draft skeleton:

Pre index klinickej vierohodnosti sa v linearnom mixed modeli neobjavil vyrazny hlavny efekt pritomnosti strukturujuceho klinickeho usmernenia (`b = [[LMM_PLAUSIBILITY_GUARDRAIL_B]]`, `SE = [[LMM_PLAUSIBILITY_GUARDRAIL_SE]]`, `95 % CI [[LMM_PLAUSIBILITY_GUARDRAIL_CI]]`). Deskriptivne priemery podla guardrailu boli `[[PLAUSIBILITY_OFF_MEAN]]` bez usmernenia a `[[PLAUSIBILITY_ON_MEAN]]` so zapnutym usmernenim.

Rovnako slaby alebo nanajvys mierny obraz sa ukazal aj pri prirodzenosti jazyka (`G2`) a treningovej pouzitelnosti (`G5`). Pri `G2` bol koeficient guardrailu `[[CLMM_G2_GUARDRAIL_B]]` (`p = [[CLMM_G2_GUARDRAIL_P]]`), pri `G5` `[[CLMM_G5_GUARDRAIL_B]]` (`p = [[CLMM_G5_GUARDRAIL_P]]`). Pri indexe defektov bol guardrail efekt smerovo `[[LMM_DEFECT_GUARDRAIL_DIRECTION]]` (`b = [[LMM_DEFECT_GUARDRAIL_B]]`, `SE = [[LMM_DEFECT_GUARDRAIL_SE]]`), ale jeho velkost ostala mala.

Zaver tejto podsekcie:

Tento blok poskytol `[[H1_H2_H3_H5_SUMMARY]]`.

### 3.6.2 Efekt stylu odpovedania simulovaneho pacienta

Draft skeleton:

Ani pri faktore stylu odpovedania sa neobjavil silny a konzistentny rozdiel. Priemerny index klinickej vierohodnosti bol pri `P1` `[[PLAUSIBILITY_P1_MEAN]]`, pri `P2` `[[PLAUSIBILITY_P2_MEAN]]` a pri `P3` `[[PLAUSIBILITY_P3_MEAN]]`; modelove koeficienty pre `P2` a `P3` ostali `[[PROFILE_EFFECT_SUMMARY]]`.

Podobny obraz sa ukazal aj pri prirodzenosti (`G2`) a treningovej pouzitelnosti (`G5`). Pri `G2` boli profilove efekty `[[CLMM_G2_PROFILE_SUMMARY]]`; pri `G5` `[[CLMM_G5_PROFILE_SUMMARY]]`. Tento blok preto `[[H6_H7_SUMMARY]]`.

### 3.6.3 Interakcia medzi guardrailom a profilom

Draft skeleton:

Na urovni jadrovych outcome-ov sa neobjavil silny interakcny efekt podporujuci hypotetizovanu zavislost guardrailu od profilu. Pri indexe klinickej vierohodnosti boli interakcne koeficienty `[[LMM_PLAUSIBILITY_INTERACTION_SUMMARY]]`, pri indexe defektov `[[LMM_DEFECT_INTERACTION_SUMMARY]]`.

Ak sa objavi jediny vyraznejsi signal v ordinalnych alebo secondary modeloch, pouzi vetu:

Najvyraznejsi interakcny signal sa objavil pri `[[INTERACTION_OUTCOME]]`, kde `[[INTERACTION_PATTERN_SUMMARY]]`. Tento vysledok preto zostava doplnkovym alebo exploratornym zistenim, nie nosnym nalezom prace.

Pre rating-level kompozity bol zaroven odhadnuty aj doplnkovy sensitivity model s random interceptom pre konkretny transkript. Tento robustness check priniesol pri indexe klinickej vierohodnosti aj pri indexe defektov prakticky rovnaky obraz ako hlavny model: smer efektov sa nemenil a vecna interpretacia ostala zhodna. Kedze ide len o doplnkovu kontrolnu vetvu a v aktualnom rune sa pri nej objavila aj singularita, je reportovana iba v Tabulke 9, nie ako jadro hlavnej inferencnej tabulky.

## 3.7 Transcript-level ukazovatele odchylky voci referencnym hodnotam seed scenarov

Function:
- striktne oddelit transcript-level anchor vetvu od rating-level outcome-ov

Source files:
- `tables/table_2_descriptives.csv`
- `analysis/outputs/lmm_core_models.csv`
- `analysis/outputs/transcript_level_summary.csv`
- `analysis/outputs/qc_dataset_summary.csv`

Draft skeleton:

V tejto casti oznacuju referencne hodnoty seed scenarov vopred urcene cielove hodnoty symptomov, zavaznosti a funkcneho dopadu pre kazdy seed. Tato vrstva vychadza z `[[TRANSCRIPT_LEVEL_N]]` unikatnych transkriptov, nie z rating-level poctu hodnoteni. Priemerna `symptom_error_mean` dosiahla hodnotu `[[SYMPTOM_ERROR_MEAN]]` (`SD = [[SYMPTOM_ERROR_SD]]`, median = `[[SYMPTOM_ERROR_MEDIAN]]`, `IQR = [[SYMPTOM_ERROR_IQR]]`, rozsah `[[SYMPTOM_ERROR_MIN]]` az `[[SYMPTOM_ERROR_MAX]]`). Pri transcript-level priemere expertnych odhadov bola `severity_error = [[SEVERITY_ERROR_MEAN]]` a `impact_error = [[IMPACT_ERROR_MEAN]]`.

Z pohladu hypotety `H4` bol guardrail efekt `[[SYMPTOM_GUARDRAIL_EFFECT_SUMMARY]]`. V transcript-level modeli pre `symptom_error_mean` vysiel koeficient `b = [[LMM_SYMPTOM_GUARDRAIL_B]]` (`SE = [[LMM_SYMPTOM_GUARDRAIL_SE]]`, `95 % CI [[LMM_SYMPTOM_GUARDRAIL_CI]]`). Pri profile odpovedania nevznikol `[[H8_SUMMARY]]`; priemerna symptom error bola `P1 = [[SYMPTOM_P1_MEAN]]`, `P2 = [[SYMPTOM_P2_MEAN]]`, `P3 = [[SYMPTOM_P3_MEAN]]`.

Ak bude treba explicitne dodat jednotku analyzy, pouzi vetu:

Vsetky hodnoty v tejto sekcii su transcript-level. Ukazovatele `severity_error` a `impact_error` vznikli agregaciou ratingov `S1` a `S2` na uroven transkriptu a nemaju sa miesat s ordinalnymi rating-level polozkami `S1` a `S2`.

## 3.8 Exploratorne vystupy

Function:
- doplnit kvantitativny obraz o povod rozhovoru a otvorene komentare

Source files:
- `analysis/outputs/guess_origin_summary.csv`
- `analysis/outputs/guess_origin_logit.csv`
- `analysis/outputs/comment_summary_stub.csv`

Draft skeleton:

Polozka odhadovaneho povodu rozhovoru bola vyplnena pri `[[GUESS_ORIGIN_N_NON_MISSING]]` ratingoch. V tejto casti sa `[[GUESS_ORIGIN_PATTERN_SUMMARY]]`. Tento blok ma len exploratorny charakter a nesluzi ako jadro testovania kvality rozhovorov.

Otvorene komentare boli kvalitativne informativnejsie. Dominantnym motivom bol `[[COMMENT_THEME_1]]`; menej casto sa objavovalo `[[COMMENT_THEME_2]]` a `[[COMMENT_THEME_3]]`. Kvalitativna vrstva tak doplna kvantitativny obraz najma tym, ze `[[COMMENT_INTERPRETIVE_SUMMARY]]`.

## 3.9 Strucne zhrnutie vysledkov

Function:
- uzavriet chapter-level obraz bez prechodu do diskusie

Source files:
- `analysis/outputs/run_manifest.csv`
- `tables/table_4_internal_consistency.csv`
- `tables/table_5_icc.csv`
- `tables/table_6_mixed_models_core.csv`
- `tables/table_2_descriptives.csv`

Draft skeleton:

Predbezna expertna obsahova kontrola ukazala, ze jadro ratingoveho nastroja a seed scenarov je obsahovo pouzitelne, no zaroven upozornila na slabiny v `[[SUMMARY_EXPERT_REVIEW_RISK]]`. Analyzovany subor `[[N_RATINGS]]` hodnoteni zaroven ukazal, ze simulovane rozhovory boli expertmi v priemere hodnotene ako `[[SUMMARY_GLOBAL_QUALITY]]`, zatial co defekty ostavali `[[SUMMARY_DEFECT_LEVEL]]`.

Na urovni hlavnych konfirmacnych hypotet sa v tomto subore `[[SUMMARY_HYPOTHESES_MAIN]]`. Transcript-level blok voci referencnym hodnotam seed scenarov ukazal `[[SUMMARY_ANCHOR_BLOCK]]`. Exploratorna vrstva napokon doplnila, ze `[[SUMMARY_EXPLORATORY_BLOCK]]`.

## Minimalny token checklist pred prenosom do `40_results.md`

- `[[N_RATINGS]]`, `[[N_TRANSCRIPTS]]`, `[[N_SEEDS]]`, `[[N_RATERS]]`
- `[[PLAUSIBILITY_MEAN]]`, `[[DEFECT_MEAN]]`, `[[G2_MEAN]]`, `[[G5_MEAN]]`, `[[S1_MEAN]]`, `[[S2_MEAN]]`
- `[[ALPHA_G1_G5]]`, `[[OMEGA_G1_G5]]`, fallback volba pre `ICC`
- `[[LMM_PLAUSIBILITY_GUARDRAIL_B]]`, `[[LMM_DEFECT_GUARDRAIL_B]]`
- `[[CLMM_G2_GUARDRAIL_B]]`, `[[CLMM_G5_GUARDRAIL_B]]`
- `[[SYMPTOM_ERROR_MEAN]]`, `[[LMM_SYMPTOM_GUARDRAIL_B]]`
- `[[SUMMARY_HYPOTHESES_MAIN]]`

Ak po poslednom rune ostane ktorykolvek z tychto tokenov nevyplneny, neprenasaj text do finalneho `40_results.md`.
