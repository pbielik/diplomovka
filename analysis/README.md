# Analysis

## Čo je tu pripravené
- `codebook_rating_study.csv`
- `methods_variables_table.csv`
- `hypotheses_H1_H6.md`
- `rating_export_readiness_checklist.md`
- `expert_content_review_framework.md`
- `statistical_calculations_for_statistician_review.md` — briefing pre štatistika: validačné výpočty, hlavné modely, vzorce a mapovanie na hypotézy
- `pipeline_outputs_plan.md` — presný plán tabuliek, grafov a modelových výstupov pre pipeline
- `data_clean/` — clean analytické vstupy pre pipeline
- `qc_reports/` — výstupy z deterministic QC runnera nad dátami, outputmi, tabuľkami a citekeymi
- `templates/` — CSV šablóny vrátane pilotného expert review passu
- `scripts/thesis_rating_pipeline.R` — R kostra
- `scripts/run_thesis_qc.py` — deterministic QC gate pre clean dáta, output projections a citekeys

## Jednotka analýzy
1 riadok = 1 hodnotenie 1 ratera na 1 transkripte.

Pre anchor fidelity vetvu platí doplnkové pravidlo:

- `A1-A9`, `symptom_error_mean`, `severity_error` a `impact_error` sa pri deskriptíve a transcript-level error modeloch agregujú na `1 riadok = 1 transkript`, aby sa nevážili počtom raterov.

## Hlavný model
`outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)`

## Štatistický Stack
Hlavná štatistická analýza tejto diplomovky beží v `R`, nie v `Python`.

Autoritatívny skript je `analysis/scripts/thesis_rating_pipeline.R`.

### R vrstva: core analytika
- `readr`, `dplyr`, `tidyr`, `janitor`:
  import CSV, joins, recode škál, odvodené premenné a reshape dát.
- `ggplot2`:
  manuscript-ready grafy a placeholder ploty.
- `psych`:
  `alpha`, `omega` a `ICC`.
- `lme4`:
  lineárne mixed models pre numerické outcome-y.
- `ordinal`:
  cumulative link mixed models pre ordinálne outcome-y.
- `emmeans`:
  estimated marginal means a post hoc modelové summary.
- `cluster`:
  exploratívna `PAM` typológia transkriptov.

### Python vrstva: helper workflow, nie core štatistika
- Python sa v tomto repo používa najmä na pomocné workflow skripty, exporty a preview buildy.
- Nejde o autoritatívnu vrstvu pre `ICC`, `LMM`, `CLMM`, `PAM` ani pre manuscript-ready štatistické tabuľky.
- Ak nejaký Python skript pracuje s analytickými výstupmi, robí to ako nadstavba nad CSV exportmi z R pipeline, nie ako náhrada samotnej štatistickej analýzy.

Najkratšia odpoveď:
- `R` = štatistika a modely.
- `Python` = pomocné utility okolo workflowu a prezentácie výstupov.

## QC vrstva

Pred `pre_word` alebo `final_results` workflowom má zmysel spustiť deterministic QC runner:

```bash
python3 analysis/scripts/run_thesis_qc.py --run-mode smoke
python3 analysis/scripts/run_thesis_qc.py --run-mode pre_word
```

Agentová vrstva je po novom integrovaná priamo do toho istého runnera. Predvolený lokálne overiteľný režim je `mock`:

```bash
python3 analysis/scripts/run_thesis_qc.py --run-mode smoke --agent-mode mock
```

Ak chceš explicitne zapnúť `pydantic_ai` backend, potrebuješ mať lokálne dostupné balíky a model:

```bash
python3 analysis/scripts/run_thesis_qc.py \
  --run-mode smoke \
  --agent-mode pydantic_ai \
  --agent-model openai:gpt-5.4 \
  --agent-reasoning-effort high
```

Runner po novom automaticky načíta repo `.env`, takže ak v ňom máš `OPENAI_API_KEY`, vie si pre `pydantic_ai` režim sám odvodiť default model `openai:gpt-5.4` aj bez `--agent-model`. Pre túto OpenAI vetvu zároveň defaultne nastavuje `high` reasoning effort; override je možný cez `--agent-reasoning-effort` alebo `THESIS_QC_AGENT_REASONING_EFFORT`.
Ak `pydantic_ai` backend zlyhá na provideri, sieti alebo nevalidnom outpute, runner už nespadne tracebackom; vráti kontrolovaný `BLOCK` s typed findings v reporte.

Runner kontroluje:

- clean dáta a joins medzi `ratings`, `transcripts`, `seeds`, `raters`,
- konzistenciu medzi `analysis/outputs/*.csv` a `tables/*.csv`,
- validitu citekey placeholderov voči `references/zotero-thesis.bib`,
- placeholdery a `skipped` stavy v `manuscript/40_results.md`.

Pred finálnym runom sa oplatí spraviť aj safe housekeeping generovaných artefaktov:

```bash
bash tools/pre_final_run_housekeeping.sh
bash tools/pre_final_run_housekeeping.sh --apply
```

Ak potrebuješ technicky opraviť raw validačný CSV snapshot bez zásahu do source workbooku:

```bash
python3 analysis/scripts/repair_validation_csv.py
```

To vytvorí `analysis/validity data/data_repaired_trimmed.csv`; source of truth pre expert-review raw export však ostáva `analysis/validity data/data.xlsx`.

Pri `--agent-mode mock` doplní aj orchestrator a tri typed review roly:

- `citation_support_agent`
- `stats_claim_agent`
- `results_presentation_agent`

Pri `--agent-mode pydantic_ai` sa použijú prompty v `prompts/qc/`, ale ak lokálne chýba `pydantic_ai` alebo zlyhá provider/runtime, runner to explicitne nahlási ako blocker v reporte.
JSON aj Markdown report po novom obsahujú aj `orchestrator_summary`, teda stručný súhrn toho, čo kontroloval každý agent, kde je zhoda alebo scope split a aký model sa reálne resolveroval pre agentový beh.

## Pred analýzou
- dostaň reálne exporty do `analysis/data_clean/`,
- skontroluj ich podľa `analysis/rating_export_readiness_checklist.md`,
- ak chceš reportovať predbežnú expert content review vrstvu, prepíš aktuálny 6-členný expert panel do šablón z `analysis/templates/`,
- over finálne anchor hodnoty vrátane `S2_anchor`,
- skontroluj recode škál,
- `S1` a `S2` ber v jadre ako samostatné human-rated outcome-y; seed `S1_anchor` a `S2_anchor` su uz na rovnakej `1-5` skale, takze error vetva moze bezat priamo,
- nechaj názvy premenných konzistentné medzi metódou, CSV a R skriptom,
- pri implementácii pipeline sa riaď presným output planom v `analysis/pipeline_outputs_plan.md`,
- skontroluj, že kľúčové metodické rozhodnutia majú oporu v literature bundle v `docs/literature/`, najmä v `source_clusters.md` a `gaps_and_missing_sources.md` pre seed anchoring, content validity rating nástroja a agreement metrics pri ordinálnych ratingoch.
