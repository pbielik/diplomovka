# thesis_rating_pipeline.R
required_packages <- c("tidyverse", "janitor", "psych", "lme4", "lmerTest", "ordinal", "broom.mixed")
# install.packages(setdiff(required_packages, rownames(installed.packages())))

library(tidyverse)
library(janitor)
library(psych)
library(lme4)
library(lmerTest)
library(ordinal)
library(broom.mixed)

ratings <- read_csv("analysis/templates/ratings_template.csv", show_col_types = FALSE) |> clean_names()
transcripts <- read_csv("analysis/templates/transcripts_template.csv", show_col_types = FALSE) |> clean_names()
seeds <- read_csv("analysis/templates/seed_anchors_template.csv", show_col_types = FALSE) |> clean_names()
raters <- read_csv("analysis/templates/raters_template.csv", show_col_types = FALSE) |> clean_names()

likert_1_5 <- c("g1","g2","g3","g4","g5","guess_confidence")
anchored_0_3 <- c(paste0("a", 1:9), "s1", "s2", paste0("r", 1:5))

ratings <- ratings |>
  mutate(
    guardrail = factor(guardrail, levels = c(0, 1), labels = c("off", "on")),
    profile = factor(profile, levels = c("R1", "R2", "R3")),
    seed_id = factor(seed_id),
    rater_id = factor(rater_id),
    transcript_id = factor(transcript_id),
    across(all_of(likert_1_5), ~ as.numeric(.x)),
    across(all_of(anchored_0_3), ~ as.numeric(.x)),
    guessed_origin = factor(guessed_origin)
  ) |>
  left_join(seeds, by = "seed_id") |>
  left_join(raters, by = "rater_id")

analysis_long <- ratings |>
  mutate(
    plausibility_index = rowMeans(select(., g1, g3, g4), na.rm = TRUE),
    defect_index = rowMeans(select(., r1, r2, r3, r4, r5), na.rm = TRUE),
    a1_error = abs(a1 - a1_anchor),
    a2_error = abs(a2 - a2_anchor),
    a3_error = abs(a3 - a3_anchor),
    a4_error = abs(a4 - a4_anchor),
    a5_error = abs(a5 - a5_anchor),
    a6_error = abs(a6 - a6_anchor),
    a7_error = abs(a7 - a7_anchor),
    a8_error = abs(a8 - a8_anchor),
    a9_error = abs(a9 - a9_anchor),
    symptom_error_mean = rowMeans(select(., starts_with("a") & ends_with("_error")), na.rm = TRUE),
    severity_error = abs(s1 - s1_anchor),
    impact_error = abs(s2 - s2_anchor)
  )

print(psych::alpha(select(analysis_long, g1, g2, g3, g4, g5)))
print(psych::alpha(select(analysis_long, g1, g3, g4)))

m_plausibility <- lmer(plausibility_index ~ guardrail * profile + (1 | seed_id) + (1 | rater_id), data = analysis_long, REML = FALSE)
m_defect <- lmer(defect_index ~ guardrail * profile + (1 | seed_id) + (1 | rater_id), data = analysis_long, REML = FALSE)
m_symptom_error <- lmer(symptom_error_mean ~ guardrail * profile + (1 | seed_id) + (1 | rater_id), data = analysis_long, REML = FALSE)

summary(m_plausibility)
summary(m_defect)
summary(m_symptom_error)

dir.create("analysis/outputs", recursive = TRUE, showWarnings = FALSE)
write_csv(analysis_long, "analysis/outputs/analysis_long.csv")
write_csv(broom.mixed::tidy(m_plausibility, effects = c("fixed", "ran_pars")), "analysis/outputs/model_plausibility.csv")
write_csv(broom.mixed::tidy(m_defect, effects = c("fixed", "ran_pars")), "analysis/outputs/model_defect.csv")
write_csv(broom.mixed::tidy(m_symptom_error, effects = c("fixed", "ran_pars")), "analysis/outputs/model_symptom_error.csv")
