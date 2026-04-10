# analysis/data_clean

Tento priečinok je určený pre čisté analytické vstupy.

Ukladaj sem iba dáta, ktoré:
- vznikli reprodukovateľným čistením alebo exportom,
- majú stabilné názvy premenných,
- sú pripravené na načítanie v `analysis/scripts/thesis_rating_pipeline.R`.

Odporúčané súbory:
- `ratings_clean.csv`
- `seed_anchors_final.csv`
- `raters_clean.csv`
- `transcripts_master.csv`

Voliteľné clean súbory pre predbežný expert review pass:
- `validation_experts_clean.csv`
- `rater_items_expert_review_clean.csv`
- `seeds_expert_review_clean.csv`

Surové exporty sem nepatria.

Pred prvym realnym behom pipeline ich skontroluj podla:
- `analysis/rating_export_readiness_checklist.md`
