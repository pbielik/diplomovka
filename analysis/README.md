# Analysis

## Čo je tu pripravené
- `codebook_rating_study.csv`
- `methods_variables_table.csv`
- `hypotheses_H1_H6.md`
- `data_clean/` — clean analytické vstupy pre pipeline
- `templates/` — CSV šablóny
- `scripts/thesis_rating_pipeline.R` — R kostra

## Jednotka analýzy
1 riadok = 1 hodnotenie 1 ratera na 1 transkripte.

## Hlavný model
`outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)`

## Pred analýzou
- dostaň reálne exporty do `analysis/data_clean/`,
- over finálne anchor hodnoty vrátane `S2_anchor`,
- skontroluj recode škál,
- nechaj názvy premenných konzistentné medzi metódou, CSV a R skriptom,
- skontroluj, že kľúčové metodické rozhodnutia majú oporu v literature bundle v `docs/literature/`, najmä v `source_clusters.md` a `gaps_and_missing_sources.md` pre seed anchoring, content validity rating nástroja a agreement metrics pri ordinálnych ratingoch.
