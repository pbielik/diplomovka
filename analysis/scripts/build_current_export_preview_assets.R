#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(readr)
  library(ggplot2)
  library(psych)
  library(lme4)
  library(ordinal)
  library(stringr)
  library(forcats)
})

args <- commandArgs(trailingOnly = TRUE)

repo_root <- normalizePath(getwd(), mustWork = TRUE)
default_csv <- file.path(Sys.getenv("HOME"), "Downloads", "mdd-ai-simulation_ratings_wide (4).csv")
csv_path <- if (length(args) >= 1) args[[1]] else default_csv
anchors_candidates <- c(
  file.path(repo_root, "analysis", "seed_anchors_final.csv"),
  file.path(repo_root, "analysis", "data_clean", "seed_anchors_final.csv")
)
anchors_path <- anchors_candidates[file.exists(anchors_candidates)][1]
expert_items_csv_path <- file.path(repo_root, "tables", "table_s4_expert_review_items.csv")
expert_seeds_csv_path <- file.path(repo_root, "tables", "table_s5_expert_review_seeds.csv")
expert_items_heatmap_path <- normalizePath(file.path(repo_root, "figures", "figure_s3_expert_review_items_heatmap.png"), mustWork = FALSE)
expert_seeds_heatmap_path <- normalizePath(file.path(repo_root, "figures", "figure_s4_expert_review_seeds_heatmap.png"), mustWork = FALSE)
tables_dir <- file.path(repo_root, "tables", "current_export_preview")
figures_dir <- file.path(repo_root, "figures", "current_export_preview")

dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

profile_label <- function(x) {
  dplyr::recode(x, R1 = "P1", R2 = "P2", R3 = "P3", .default = x)
}

guardrail_code <- function(x) {
  dplyr::recode(x, off = "G0", on = "G1", .default = x)
}

cell_label <- function(guardrail, profile) {
  paste0(guardrail_code(guardrail), " × ", profile_label(profile))
}

localized_scenario_label <- function(x) {
  dplyr::recode(
    x,
    `Žena v strednom veku s caregiving záťažou` = "Žena v strednom veku so záťažou pri starostlivosti o blízkeho",
    .default = x
  )
}

fmt_num <- function(x, digits = 2) {
  ifelse(
    is.na(x),
    "",
    formatC(x, format = "f", digits = digits, decimal.mark = ",")
  )
}

safe_single_mean <- function(x) {
  if (all(is.na(x))) {
    return(NA_real_)
  }
  mean(x, na.rm = TRUE)
}

write_md_table <- function(df, path, digits = 2) {
  cols <- names(df)
  align <- paste(rep("---", length(cols)), collapse = " | ")
  col_digits <- vapply(df, function(column) {
    if (!is.numeric(column)) {
      return(NA_integer_)
    }
    non_missing <- column[!is.na(column)]
    if (!length(non_missing)) {
      return(as.integer(digits))
    }
    if (all(abs(non_missing - round(non_missing)) < 1e-9)) {
      return(0L)
    }
    as.integer(digits)
  }, integer(1))
  lines <- c(
    paste0("| ", paste(cols, collapse = " | "), " |"),
    paste0("| ", align, " |")
  )

  for (idx in seq_len(nrow(df))) {
    row <- df[idx, , drop = FALSE]
    vals <- vapply(seq_along(row), function(col_idx) {
      value <- row[[col_idx]]
      if (is.numeric(value)) {
        return(fmt_num(value, digits = col_digits[[col_idx]]))
      }
      value <- as.character(value)
      ifelse(is.na(value), "", value)
    }, character(1))
    lines <- c(lines, paste0("| ", paste(vals, collapse = " | "), " |"))
  }

  writeLines(lines, path, useBytes = TRUE)
}

caption_lines <- function(label, title) {
  c(
    sprintf("**%s**  ", label),
    sprintf("*%s*", title),
    ""
  )
}

table_caption <- function(number, title) {
  caption_lines(sprintf("Tabuľka %d", number), title)
}

figure_caption <- function(number, title) {
  caption_lines(sprintf("Obrázok %d", number), title)
}

supplement_table_caption <- function(label, title) {
  caption_lines(sprintf("Tabuľka %s", label), title)
}

supplement_figure_caption <- function(label, title) {
  caption_lines(sprintf("Obrázok %s", label), title)
}

safe_alpha <- function(data, vars, block_label) {
  block <- data %>% select(all_of(vars))

  alpha_value <- tryCatch(
    psych::alpha(block, warnings = FALSE, check.keys = FALSE)$total$raw_alpha,
    error = function(e) NA_real_
  )

  omega_value <- tryCatch(
    suppressWarnings(psych::omega(block, plot = FALSE, warnings = FALSE, nfactors = 1)$omega.tot),
    error = function(e) NA_real_
  )

  tibble(
    Blok = block_label,
    `Počet položiek` = length(vars),
    `Cronbachovo alpha` = alpha_value,
    `McDonaldovo omega total (1f)` = omega_value
  )
}

extract_lmm_row <- function(data, outcome, label) {
  fit <- tryCatch(
    lme4::lmer(
      formula = stats::as.formula(
        paste0(outcome, " ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)")
      ),
      data = data,
      REML = FALSE
    ),
    error = function(e) NULL
  )

  if (is.null(fit)) {
    return(tibble(
      Ukazovateľ = label,
      Model = "LMM",
      `Usmernenie b` = NA_real_,
      `Usmernenie SE` = NA_real_,
      `Profil P2 b` = NA_real_,
      `Profil P3 b` = NA_real_,
      `Najväčší absolútny interakčný koeficient (b)` = NA_real_,
      `Najnižšia interakčná p-hodnota` = NA_real_
    ))
  }

  coef_tab <- summary(fit)$coefficients
  term_value <- function(term, col) {
    if (!term %in% rownames(coef_tab)) {
      return(NA_real_)
    }
    coef_tab[term, col]
  }

  interactions <- abs(c(
    term_value("guardrailon:profileP2", "Estimate"),
    term_value("guardrailon:profileP3", "Estimate")
  ))

  tibble(
    Ukazovateľ = label,
    Model = "LMM",
    `Usmernenie b` = term_value("guardrailon", "Estimate"),
    `Usmernenie SE` = term_value("guardrailon", "Std. Error"),
    `Profil P2 b` = term_value("profileP2", "Estimate"),
    `Profil P3 b` = term_value("profileP3", "Estimate"),
    `Najväčší absolútny interakčný koeficient (b)` = suppressWarnings(max(interactions, na.rm = TRUE)),
    `Najnižšia interakčná p-hodnota` = NA_real_
  ) %>%
    mutate(
      `Najväčší absolútny interakčný koeficient (b)` = ifelse(
        is.infinite(`Najväčší absolútny interakčný koeficient (b)`),
        NA_real_,
        `Najväčší absolútny interakčný koeficient (b)`
      )
    )
}

extract_transcript_lmm_row <- function(data, outcome, label) {
  fit_data <- data %>%
    distinct(transcript_id, seed_id, guardrail, profile, .data[[outcome]])

  fit <- tryCatch(
    lme4::lmer(
      formula = stats::as.formula(
        paste0(outcome, " ~ guardrail * profile + (1 | seed_id)")
      ),
      data = fit_data,
      REML = FALSE
    ),
    error = function(e) NULL
  )

  if (is.null(fit)) {
    return(tibble(
      Ukazovateľ = label,
      Model = "LMM (prepis rozhovoru)",
      `Usmernenie b` = NA_real_,
      `Usmernenie SE` = NA_real_,
      `Profil P2 b` = NA_real_,
      `Profil P3 b` = NA_real_,
      `Najväčší absolútny interakčný koeficient (b)` = NA_real_,
      `Najnižšia interakčná p-hodnota` = NA_real_
    ))
  }

  coef_tab <- summary(fit)$coefficients
  term_value <- function(term, col) {
    if (!term %in% rownames(coef_tab)) {
      return(NA_real_)
    }
    coef_tab[term, col]
  }

  interactions <- abs(c(
    term_value("guardrailon:profileP2", "Estimate"),
    term_value("guardrailon:profileP3", "Estimate")
  ))

  tibble(
    Ukazovateľ = label,
    Model = "LMM (prepis rozhovoru)",
    `Usmernenie b` = term_value("guardrailon", "Estimate"),
    `Usmernenie SE` = term_value("guardrailon", "Std. Error"),
    `Profil P2 b` = term_value("profileP2", "Estimate"),
    `Profil P3 b` = term_value("profileP3", "Estimate"),
    `Najväčší absolútny interakčný koeficient (b)` = suppressWarnings(max(interactions, na.rm = TRUE)),
    `Najnižšia interakčná p-hodnota` = NA_real_
  ) %>%
    mutate(
      `Najväčší absolútny interakčný koeficient (b)` = ifelse(
        is.infinite(`Najväčší absolútny interakčný koeficient (b)`),
        NA_real_,
        `Najväčší absolútny interakčný koeficient (b)`
      )
    )
}

extract_clmm_row <- function(data, outcome, label) {
  clmm_data <- data %>%
    select(all_of(c(outcome, "guardrail", "profile", "seed_id", "rater_id"))) %>%
    filter(!is.na(.data[[outcome]])) %>%
    mutate(response = ordered(.data[[outcome]]))

  fit <- tryCatch(
    ordinal::clmm(
      response ~ guardrail * profile + (1 | seed_id) + (1 | rater_id),
      data = clmm_data,
      Hess = TRUE,
      link = "logit"
    ),
    error = function(e) NULL
  )

  if (is.null(fit)) {
    return(tibble(
      Ukazovateľ = label,
      Model = "CLMM",
      `Usmernenie b` = NA_real_,
      `Usmernenie SE` = NA_real_,
      `Profil P2 b` = NA_real_,
      `Profil P3 b` = NA_real_,
      `Najväčší absolútny interakčný koeficient (b)` = NA_real_,
      `Najnižšia interakčná p-hodnota` = NA_real_
    ))
  }

  coef_tab <- summary(fit)$coefficients
  term_value <- function(term, col) {
    if (!term %in% rownames(coef_tab)) {
      return(NA_real_)
    }
    coef_tab[term, col]
  }

  interaction_estimates <- abs(c(
    term_value("guardrailon:profileP2", "Estimate"),
    term_value("guardrailon:profileP3", "Estimate")
  ))
  interaction_ps <- c(
    term_value("guardrailon:profileP2", "Pr(>|z|)"),
    term_value("guardrailon:profileP3", "Pr(>|z|)")
  )

  tibble(
    Ukazovateľ = label,
    Model = "CLMM",
    `Usmernenie b` = term_value("guardrailon", "Estimate"),
    `Usmernenie SE` = term_value("guardrailon", "Std. Error"),
    `Profil P2 b` = term_value("profileP2", "Estimate"),
    `Profil P3 b` = term_value("profileP3", "Estimate"),
    `Najväčší absolútny interakčný koeficient (b)` = suppressWarnings(max(interaction_estimates, na.rm = TRUE)),
    `Najnižšia interakčná p-hodnota` = suppressWarnings(min(interaction_ps, na.rm = TRUE))
  ) %>%
    mutate(
      `Najväčší absolútny interakčný koeficient (b)` = ifelse(
        is.infinite(`Najväčší absolútny interakčný koeficient (b)`),
        NA_real_,
        `Najväčší absolútny interakčný koeficient (b)`
      ),
      `Najnižšia interakčná p-hodnota` = ifelse(
        is.infinite(`Najnižšia interakčná p-hodnota`),
        NA_real_,
        `Najnižšia interakčná p-hodnota`
      )
    )
}

raw <- readr::read_csv(csv_path, show_col_types = FALSE)
partial_anchors <- readr::read_csv(anchors_path, show_col_types = FALSE)

analysis_long <- raw %>%
  transmute(
    transcript_id = transcript_stable_id,
    rater_id = factor(assignee_code),
    seed_id = factor(seed),
    guardrail = factor(iv_prompt_guardrail_mode, levels = c("off", "on")),
    profile = factor(profile_label(iv_realization_profile), levels = c("P1", "P2", "P3")),
    cell = factor(
      cell_label(iv_prompt_guardrail_mode, iv_realization_profile),
      levels = c("G0 × P1", "G0 × P2", "G0 × P3", "G1 × P1", "G1 × P2", "G1 × P3")
    ),
    g1 = suppressWarnings(as.numeric(`interview-rating_v1__G1_clinical_credibility`)),
    g2 = suppressWarnings(as.numeric(`interview-rating_v1__G2_natural_language`)),
    g3 = suppressWarnings(as.numeric(`interview-rating_v1__G3_internal_consistency`)),
    g4 = suppressWarnings(as.numeric(`interview-rating_v1__G4_depression_fit`)),
    g5 = suppressWarnings(as.numeric(`interview-rating_v1__G5_methodological_utility`)),
    s1 = suppressWarnings(as.numeric(`interview-rating_v1__S1_symptom_severity`)),
    s2 = suppressWarnings(as.numeric(`interview-rating_v1__S2_functional_impact`)),
    r1 = suppressWarnings(as.numeric(`interview-rating_v1__R1_contradictions`)),
    r2 = suppressWarnings(as.numeric(`interview-rating_v1__R2_cliche_template`)),
    r3 = suppressWarnings(as.numeric(`interview-rating_v1__R3_context_symptom_mismatch`)),
    r4 = suppressWarnings(as.numeric(`interview-rating_v1__R4_other_primary_psychopathology`)),
    r5 = suppressWarnings(as.numeric(`interview-rating_v1__R5_excessive_dramatization`)),
    o1 = `interview-rating_v1__O1_least_convincing`,
    o2 = `interview-rating_v1__O2_missing_or_exaggerated`,
    guessed_origin = `interview-rating_v1__P1_perceived_origin`,
    guess_confidence = suppressWarnings(as.numeric(`interview-rating_v1__P2_origin_confidence`))
  ) %>%
  mutate(
    plausibility_index = rowMeans(across(c(g1, g3, g4)), na.rm = TRUE),
    defect_index = rowMeans(across(c(r1, r2, r3, r4, r5)), na.rm = TRUE)
  )

analysis_anchored <- raw %>%
  transmute(
    transcript_id = transcript_stable_id,
    rater_id = factor(assignee_code),
    seed_id = factor(seed),
    guardrail = factor(iv_prompt_guardrail_mode, levels = c("off", "on")),
    profile = factor(profile_label(iv_realization_profile), levels = c("P1", "P2", "P3")),
    cell = factor(
      cell_label(iv_prompt_guardrail_mode, iv_realization_profile),
      levels = c("G0 × P1", "G0 × P2", "G0 × P3", "G1 × P1", "G1 × P2", "G1 × P3")
    ),
    s1 = suppressWarnings(as.numeric(`interview-rating_v1__S1_symptom_severity`)),
    s2 = suppressWarnings(as.numeric(`interview-rating_v1__S2_functional_impact`)),
    a1 = suppressWarnings(as.numeric(phq9_depressed_mood_score)),
    a2 = suppressWarnings(as.numeric(phq9_anhedonia_score)),
    a3 = suppressWarnings(as.numeric(phq9_sleep_disturbance_score)),
    a4 = suppressWarnings(as.numeric(phq9_appetite_change_score)),
    a5 = suppressWarnings(as.numeric(phq9_psychomotor_change_score)),
    a6 = suppressWarnings(as.numeric(phq9_fatigue_score)),
    a7 = suppressWarnings(as.numeric(phq9_worthlessness_or_guilt_score)),
    a8 = suppressWarnings(as.numeric(phq9_concentration_difficulty_score)),
    a9 = suppressWarnings(as.numeric(phq9_self_harm_thoughts_score))
  ) %>%
  inner_join(partial_anchors, by = "seed_id") %>%
  mutate(
    a1_error = abs(a1 - A1_anchor),
    a2_error = abs(a2 - A2_anchor),
    a3_error = abs(a3 - A3_anchor),
    a4_error = abs(a4 - A4_anchor),
    a5_error = abs(a5 - A5_anchor),
    a6_error = abs(a6 - A6_anchor),
    a7_error = abs(a7 - A7_anchor),
    a8_error = abs(a8 - A8_anchor),
    a9_error = abs(a9 - A9_anchor),
    symptom_error_mean = rowMeans(
      across(c(a1_error, a2_error, a3_error, a4_error, a5_error, a6_error, a7_error, a8_error, a9_error)),
      na.rm = TRUE
    ),
    severity_error = abs(s1 - S1_anchor),
    impact_error = abs(s2 - S2_anchor)
  )

analysis_transcript_anchored <- analysis_anchored %>%
  group_by(transcript_id, seed_id, guardrail, profile, cell) %>%
  summarise(
    symptom_error_mean = safe_single_mean(.data$symptom_error_mean),
    severity_error = safe_single_mean(.data$severity_error),
    impact_error = safe_single_mean(.data$impact_error),
    n_ratings = n(),
    .groups = "drop"
  )

ratings_per_transcript <- table(analysis_long$transcript_id)
ratings_distribution <- as.data.frame(table(ratings_per_transcript)) %>%
  transmute(
    `Počet hodnotení na prepis rozhovoru` = as.integer(as.character(ratings_per_transcript)),
    `Počet prepisov rozhovorov` = Freq
  ) %>%
  arrange(`Počet hodnotení na prepis rozhovoru`)

dataset_overview <- bind_rows(
  tibble(
    Ukazovateľ = c(
      "Počet hodnotení",
      "Počet prepisov rozhovorov",
      "Počet východiskových scenárov",
      "Počet hodnotiteľov v exporte",
      "Priemerný počet hodnotení na prepis rozhovoru",
      "Minimum hodnotení na prepis rozhovoru",
      "Maximum hodnotení na prepis rozhovoru"
    ),
    Hodnota = c(
      nrow(analysis_long),
      n_distinct(analysis_long$transcript_id),
      n_distinct(analysis_long$seed_id),
      n_distinct(analysis_long$rater_id),
      round(mean(ratings_per_transcript), 2),
      min(ratings_per_transcript),
      max(ratings_per_transcript)
    )
  ),
  analysis_long %>%
    count(cell, name = "Hodnota") %>%
    transmute(Ukazovateľ = paste0("Bunka ", .data$cell), Hodnota = .data$Hodnota)
)

rater_coverage <- analysis_long %>%
  group_by(rater_id) %>%
  summarise(
    `Počet hodnotení` = n(),
    `Počet prepisov rozhovorov` = n_distinct(transcript_id),
    `Počet profilov` = n_distinct(profile),
    `Počet buniek` = n_distinct(cell),
    .groups = "drop"
  ) %>%
  rename(`Hodnotiteľ` = rater_id) %>%
  arrange(desc(`Počet hodnotení`), `Hodnotiteľ`)

overall_descriptives <- bind_rows(
  tibble(
    `Ukazovateľ` = c("Index klinickej vierohodnosti", "Index defektov", "Prirodzenosť jazyka (G2)", "Tréningová použiteľnosť (G5)", "Odhad závažnosti (S1)", "Odhad funkčného dopadu (S2)"),
    `N` = c(
      sum(!is.na(analysis_long$plausibility_index)),
      sum(!is.na(analysis_long$defect_index)),
      sum(!is.na(analysis_long$g2)),
      sum(!is.na(analysis_long$g5)),
      sum(!is.na(analysis_long$s1)),
      sum(!is.na(analysis_long$s2))
    ),
    `Priemer` = c(
      mean(analysis_long$plausibility_index, na.rm = TRUE),
      mean(analysis_long$defect_index, na.rm = TRUE),
      mean(analysis_long$g2, na.rm = TRUE),
      mean(analysis_long$g5, na.rm = TRUE),
      mean(analysis_long$s1, na.rm = TRUE),
      mean(analysis_long$s2, na.rm = TRUE)
    ),
    `SD` = c(
      sd(analysis_long$plausibility_index, na.rm = TRUE),
      sd(analysis_long$defect_index, na.rm = TRUE),
      sd(analysis_long$g2, na.rm = TRUE),
      sd(analysis_long$g5, na.rm = TRUE),
      sd(analysis_long$s1, na.rm = TRUE),
      sd(analysis_long$s2, na.rm = TRUE)
    ),
    `Medián` = c(
      median(analysis_long$plausibility_index, na.rm = TRUE),
      median(analysis_long$defect_index, na.rm = TRUE),
      median(analysis_long$g2, na.rm = TRUE),
      median(analysis_long$g5, na.rm = TRUE),
      median(analysis_long$s1, na.rm = TRUE),
      median(analysis_long$s2, na.rm = TRUE)
    ),
    `IQR` = c(
      IQR(analysis_long$plausibility_index, na.rm = TRUE),
      IQR(analysis_long$defect_index, na.rm = TRUE),
      IQR(analysis_long$g2, na.rm = TRUE),
      IQR(analysis_long$g5, na.rm = TRUE),
      IQR(analysis_long$s1, na.rm = TRUE),
      IQR(analysis_long$s2, na.rm = TRUE)
    ),
    `Minimum` = c(
      min(analysis_long$plausibility_index, na.rm = TRUE),
      min(analysis_long$defect_index, na.rm = TRUE),
      min(analysis_long$g2, na.rm = TRUE),
      min(analysis_long$g5, na.rm = TRUE),
      min(analysis_long$s1, na.rm = TRUE),
      min(analysis_long$s2, na.rm = TRUE)
    ),
    `Maximum` = c(
      max(analysis_long$plausibility_index, na.rm = TRUE),
      max(analysis_long$defect_index, na.rm = TRUE),
      max(analysis_long$g2, na.rm = TRUE),
      max(analysis_long$g5, na.rm = TRUE),
      max(analysis_long$s1, na.rm = TRUE),
      max(analysis_long$s2, na.rm = TRUE)
    )
  )
)

cell_descriptives_rating <- analysis_long %>%
  group_by(cell) %>%
  summarise(
    `N hodnotení` = n(),
    `Klinická vierohodnosť (hodnotenia)` = mean(plausibility_index, na.rm = TRUE),
    `Defekty (hodnotenia)` = mean(defect_index, na.rm = TRUE),
    `G2 prirodzenosť (hodnotenia)` = mean(g2, na.rm = TRUE),
    `G5 použiteľnosť (hodnotenia)` = mean(g5, na.rm = TRUE),
    `S1 závažnosť (hodnotenia)` = mean(s1, na.rm = TRUE),
    `S2 funkčný dopad (hodnotenia)` = mean(s2, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  rename(`Bunka dizajnu` = cell)

cell_descriptives_transcript <- analysis_transcript_anchored %>%
  group_by(cell) %>%
  summarise(
    `N prepisov rozhovorov` = n(),
    `Priemerná absolútna chyba v symptomatických doménach (prepisy rozhovorov)` = mean(symptom_error_mean, na.rm = TRUE),
    `Chyba odhadu závažnosti (prepisy rozhovorov)` = mean(severity_error, na.rm = TRUE),
    `Chyba odhadu funkčného dopadu (prepisy rozhovorov)` = mean(impact_error, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  rename(`Bunka dizajnu` = cell)

cell_descriptives <- cell_descriptives_rating %>%
  left_join(
    cell_descriptives_transcript,
    by = "Bunka dizajnu"
  )

internal_consistency <- bind_rows(
  safe_alpha(analysis_long, c("g1", "g2", "g3", "g4", "g5"), "Globálny blok G1-G5"),
  safe_alpha(analysis_long, c("g1", "g3", "g4"), "Jadro klinickej vierohodnosti"),
  safe_alpha(analysis_long, c("r1", "r2", "r3", "r4", "r5"), "Defektový blok R1-R5")
)

core_pair <- analysis_long %>%
  filter(rater_id %in% c("13", "14")) %>%
  select(transcript_id, rater_id, plausibility_index, defect_index, s1, s2) %>%
  pivot_wider(names_from = rater_id, values_from = c(plausibility_index, defect_index, s1, s2), names_sep = "_")

pair_agreement <- tibble(
  `Ukazovateľ` = c("Index klinickej vierohodnosti", "Index defektov", "Odhad závažnosti (S1)", "Odhad funkčného dopadu (S2)"),
  `Presná zhoda` = c(
    mean(core_pair$plausibility_index_13 == core_pair$plausibility_index_14, na.rm = TRUE),
    mean(core_pair$defect_index_13 == core_pair$defect_index_14, na.rm = TRUE),
    mean(core_pair$s1_13 == core_pair$s1_14, na.rm = TRUE),
    mean(core_pair$s2_13 == core_pair$s2_14, na.rm = TRUE)
  ),
  `Priemerná absolútna odchýlka` = c(
    mean(abs(core_pair$plausibility_index_13 - core_pair$plausibility_index_14), na.rm = TRUE),
    mean(abs(core_pair$defect_index_13 - core_pair$defect_index_14), na.rm = TRUE),
    mean(abs(core_pair$s1_13 - core_pair$s1_14), na.rm = TRUE),
    mean(abs(core_pair$s2_13 - core_pair$s2_14), na.rm = TRUE)
  ),
  `Počet spoločných prepisov rozhovorov` = rep(nrow(core_pair), 4)
)

format_model_summary <- function(df) {
  df %>%
    mutate(
      `Najnižšia interakčná p-hodnota` = ifelse(
        is.na(`Najnižšia interakčná p-hodnota`),
        "neuvádza sa",
        formatC(`Najnižšia interakčná p-hodnota`, format = "f", digits = 2, decimal.mark = ",")
      )
    )
}

model_summary_rating <- bind_rows(
  extract_lmm_row(analysis_long, "plausibility_index", "Index klinickej vierohodnosti"),
  extract_lmm_row(analysis_long, "defect_index", "Index defektov"),
  extract_clmm_row(analysis_long, "g2", "Prirodzenosť jazyka (G2)"),
  extract_clmm_row(analysis_long, "g5", "Tréningová použiteľnosť (G5)"),
  extract_clmm_row(analysis_long, "s1", "Odhad závažnosti (S1)"),
  extract_clmm_row(analysis_long, "s2", "Odhad funkčného dopadu (S2)")
) %>%
  format_model_summary()

model_summary_transcript <- bind_rows(
  extract_transcript_lmm_row(analysis_transcript_anchored, "symptom_error_mean", "Priemerná absolútna chyba v symptomatických doménach"),
  extract_transcript_lmm_row(analysis_transcript_anchored, "severity_error", "Chyba odhadu závažnosti"),
  extract_transcript_lmm_row(analysis_transcript_anchored, "impact_error", "Chyba odhadu funkčného dopadu")
) %>%
  format_model_summary()

model_summary <- bind_rows(model_summary_rating, model_summary_transcript)

guess_summary <- analysis_long %>%
  filter(!is.na(guessed_origin), guessed_origin != "") %>%
  mutate(
    guessed_origin = recode(
      guessed_origin,
      ai_generated = "AI-generované",
      human_simulated = "ľudsky simulované",
      real_participant = "reálny účastník",
      .default = guessed_origin
    )
  ) %>%
  count(guessed_origin, name = "Počet") %>%
  mutate(`Podiel z vyplnených` = Počet / sum(Počet)) %>%
  rename(`Odhadovaný pôvod` = guessed_origin)

comment_text <- analysis_long %>%
  transmute(
    text = str_trim(str_squish(paste(coalesce(o1, ""), coalesce(o2, ""), sep = " ")))
  ) %>%
  filter(text != "")

comment_themes <- tibble(
  `Téma komentára` = c(
    "Nacvičené alebo natrénované odpovede",
    "Slabšie doplňujúce otázky alebo chýbajúca hĺbka",
    "Rodová nekonzistentnosť",
    "Doslovný preklad alebo neprirodzená slovenčina",
    "Príliš explicitná bezpečnostná formulácia"
  ),
  `Počet komentárov` = c(
    sum(str_detect(str_to_lower(comment_text$text), "nacvi|natren|pripraven|mechanic|robot")),
    sum(str_detect(str_to_lower(comment_text$text), "follow|dop.yt|hlb|plytk|nedop")),
    sum(str_detect(str_to_lower(comment_text$text), "rodov|mu.z|zena|pohlav|gender")),
    sum(str_detect(str_to_lower(comment_text$text), "preklad|anglic|sloven")),
    sum(str_detect(str_to_lower(comment_text$text), "safety|bezpe|linka|kriz"))
  )
)

anchored_summary <- tibble(
  Ukazovateľ = c(
    "Počet východiskových scenárov s referenčnými hodnotami",
    "Počet prepisov rozhovorov s referenčnými hodnotami",
    "Počet hodnotení naviazaných na referenčné hodnoty východiskových scenárov",
    "Priemerná absolútna chyba v symptomatických doménach",
    "SD priemernej absolútnej chyby v symptomatických doménach",
    "Medián priemernej absolútnej chyby v symptomatických doménach",
    "Priemerná chyba odhadu závažnosti",
    "SD chyby odhadu závažnosti",
    "Medián chyby odhadu závažnosti",
    "Priemerná chyba odhadu funkčného dopadu",
    "SD chyby odhadu funkčného dopadu",
    "Medián chyby odhadu funkčného dopadu"
  ),
  Hodnota = c(
    n_distinct(analysis_transcript_anchored$seed_id),
    n_distinct(analysis_transcript_anchored$transcript_id),
    nrow(analysis_anchored),
    mean(analysis_transcript_anchored$symptom_error_mean, na.rm = TRUE),
    sd(analysis_transcript_anchored$symptom_error_mean, na.rm = TRUE),
    median(analysis_transcript_anchored$symptom_error_mean, na.rm = TRUE),
    mean(analysis_transcript_anchored$severity_error, na.rm = TRUE),
    sd(analysis_transcript_anchored$severity_error, na.rm = TRUE),
    median(analysis_transcript_anchored$severity_error, na.rm = TRUE),
    mean(analysis_transcript_anchored$impact_error, na.rm = TRUE),
    sd(analysis_transcript_anchored$impact_error, na.rm = TRUE),
    median(analysis_transcript_anchored$impact_error, na.rm = TRUE)
  ),
  `Základ N` = c(
    "12 východiskových scenárov",
    "72 prepisov rozhovorov",
    sprintf("%d hodnotení", nrow(analysis_anchored)),
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov",
    "72 prepisov rozhovorov"
  )
)

plot_coverage <- ratings_distribution %>%
  mutate(`Počet hodnotení na prepis rozhovoru` = factor(`Počet hodnotení na prepis rozhovoru`))

figure_1_path <- normalizePath(file.path(figures_dir, "figure_1_ratings_per_transcript.png"), mustWork = FALSE)
ggplot(plot_coverage, aes(x = `Počet hodnotení na prepis rozhovoru`, y = `Počet prepisov rozhovorov`)) +
  geom_col(fill = "#587C69", width = 0.65) +
  labs(x = "Počet hodnotení na prepis rozhovoru", y = "Počet prepisov rozhovorov") +
  theme_minimal(base_size = 11)
ggsave(figure_1_path, width = 6.8, height = 4.2, dpi = 220)

dist_long <- analysis_long %>%
  select(plausibility_index, defect_index, g2, g5) %>%
  rename(
    `Index klinickej vierohodnosti` = plausibility_index,
    `Index defektov` = defect_index,
    `G2 prirodzenosť` = g2,
    `G5 použiteľnosť` = g5
  ) %>%
  pivot_longer(everything(), names_to = "Outcome", values_to = "Hodnota") %>%
  bind_rows(
    analysis_transcript_anchored %>%
      transmute(Outcome = "Priemerná absolútna chyba v symptomatických doménach", Hodnota = symptom_error_mean)
  )

figure_2_path <- normalizePath(file.path(figures_dir, "figure_2_distributions.png"), mustWork = FALSE)
ggplot(dist_long, aes(x = Hodnota)) +
  geom_histogram(fill = "#2E6F95", color = "white", bins = 12) +
  facet_wrap(~ Outcome, scales = "free_x") +
  labs(x = "Hodnota skóre", y = "Počet pozorovaní") +
  theme_minimal(base_size = 11)
ggsave(figure_2_path, width = 8.9, height = 5.6, dpi = 220)

item_freq <- analysis_long %>%
  select(g1, g2, g3, g4, g5, s1, s2, r1, r2, r3, r4, r5) %>%
  rename(
    G1 = g1, G2 = g2, G3 = g3, G4 = g4, G5 = g5,
    S1 = s1, S2 = s2,
    R1 = r1, R2 = r2, R3 = r3, R4 = r4, R5 = r5
  ) %>%
  pivot_longer(everything(), names_to = "Položka", values_to = "Odpoveď") %>%
  filter(!is.na(Odpoveď)) %>%
  mutate(
    Blok = case_when(
      str_starts(Položka, "G") ~ "Globálne položky",
      str_starts(Položka, "S") ~ "Severity a dopad",
      TRUE ~ "Defekty"
    ),
    Odpoveď = factor(Odpoveď, levels = c(1, 2, 3, 4, 5))
  ) %>%
  count(Blok, Položka, Odpoveď, name = "Počet") %>%
  group_by(Blok, Položka) %>%
  mutate(Podiel = Počet / sum(Počet)) %>%
  ungroup()

figure_3_path <- normalizePath(file.path(figures_dir, "figure_3_item_response_profiles.png"), mustWork = FALSE)
ggplot(item_freq, aes(x = fct_rev(Položka), y = Podiel, fill = Odpoveď)) +
  geom_col(width = 0.75, position = "fill") +
  facet_wrap(~ Blok, scales = "free_y") +
  coord_flip() +
  scale_fill_brewer(palette = "Blues", direction = 1) +
  labs(x = NULL, y = "Podiel odpovedí", fill = "Skóre") +
  theme_minimal(base_size = 11)
ggsave(figure_3_path, width = 9.1, height = 6.1, dpi = 220)

primary_by_cell <- analysis_long %>%
  select(cell, plausibility_index, defect_index) %>%
  pivot_longer(cols = c(plausibility_index, defect_index), names_to = "Outcome", values_to = "Hodnota") %>%
  mutate(
    Outcome = recode(
      Outcome,
      plausibility_index = "Index klinickej vierohodnosti",
      defect_index = "Index defektov"
    )
  )

figure_4_path <- normalizePath(file.path(figures_dir, "figure_4_primary_boxplots_by_cell.png"), mustWork = FALSE)
ggplot(primary_by_cell, aes(x = cell, y = Hodnota, fill = cell)) +
  geom_boxplot(width = 0.72, outlier.alpha = 0.35) +
  facet_wrap(~ Outcome, scales = "free_y") +
  labs(x = "Experimentálna bunka", y = "Skóre") +
  theme_minimal(base_size = 11) +
  theme(legend.position = "none")
ggsave(figure_4_path, width = 9.2, height = 5.4, dpi = 220)

secondary_by_cell <- analysis_long %>%
  select(cell, g2, g5, s1, s2) %>%
  pivot_longer(cols = c(g2, g5, s1, s2), names_to = "Outcome", values_to = "Hodnota") %>%
  mutate(
    Outcome = recode(
      Outcome,
      g2 = "G2 prirodzenosť",
      g5 = "G5 použiteľnosť",
      s1 = "S1 závažnosť",
      s2 = "S2 funkčný dopad"
    ),
    Outcome = factor(
      Outcome,
      levels = c(
        "G2 prirodzenosť",
        "G5 použiteľnosť",
        "S1 závažnosť",
        "S2 funkčný dopad"
      )
    )
  )

figure_5_path <- normalizePath(file.path(figures_dir, "figure_5_secondary_boxplots_by_cell.png"), mustWork = FALSE)
ggplot(secondary_by_cell, aes(x = cell, y = Hodnota, fill = cell)) +
  geom_boxplot(width = 0.72, outlier.alpha = 0.35) +
  facet_wrap(~ Outcome, scales = "free_y") +
  labs(x = "Experimentálna bunka", y = "Skóre") +
  theme_minimal(base_size = 11) +
  theme(legend.position = "none")
ggsave(figure_5_path, width = 9.5, height = 6.3, dpi = 220)

secondary_cell_freq <- secondary_by_cell %>%
  filter(!is.na(Hodnota)) %>%
  mutate(Skóre = factor(Hodnota, levels = c(1, 2, 3, 4, 5))) %>%
  count(Outcome, cell, Skóre, name = "Počet") %>%
  complete(
    Outcome,
    cell,
    Skóre = factor(c(1, 2, 3, 4, 5), levels = c(1, 2, 3, 4, 5)),
    fill = list(Počet = 0)
  ) %>%
  group_by(Outcome, cell) %>%
  mutate(Podiel = ifelse(sum(Počet) > 0, Počet / sum(Počet), 0)) %>%
  ungroup()

figure_5a_path <- normalizePath(file.path(figures_dir, "figure_5a_secondary_boxplots_jitter_by_cell.png"), mustWork = FALSE)
ggplot(secondary_by_cell, aes(x = cell, y = Hodnota, fill = cell)) +
  geom_boxplot(width = 0.54, alpha = 0.65, outlier.shape = NA) +
  geom_jitter(
    aes(color = cell),
    width = 0.14,
    height = 0.06,
    alpha = 0.4,
    size = 1.4,
    show.legend = FALSE
  ) +
  facet_wrap(~ Outcome, ncol = 2) +
  scale_y_continuous(breaks = 1:5, limits = c(1, 5)) +
  labs(x = "Experimentálna bunka", y = "Skóre") +
  theme_minimal(base_size = 11) +
  theme(legend.position = "none")
ggsave(figure_5a_path, width = 9.5, height = 6.6, dpi = 220)

figure_5b_path <- normalizePath(file.path(figures_dir, "figure_5b_secondary_stacked_frequencies_by_cell.png"), mustWork = FALSE)
ggplot(secondary_cell_freq, aes(x = cell, y = Podiel, fill = Skóre)) +
  geom_col(width = 0.74) +
  facet_wrap(~ Outcome, ncol = 2) +
  scale_fill_brewer(palette = "YlGnBu", direction = 1) +
  scale_y_continuous(labels = function(x) paste0(round(x * 100), "%")) +
  labs(x = "Experimentálna bunka", y = "Podiel odpovedí", fill = "Skóre") +
  theme_minimal(base_size = 11) +
  theme(axis.text.x = element_text(angle = 25, hjust = 1))
ggsave(figure_5b_path, width = 9.6, height = 6.6, dpi = 220)

figure_5c_path <- normalizePath(file.path(figures_dir, "figure_5c_secondary_heatmap_by_cell.png"), mustWork = FALSE)
ggplot(secondary_cell_freq, aes(x = cell, y = Skóre, fill = Podiel)) +
  geom_tile(color = "white", linewidth = 0.35) +
  geom_text(
    aes(label = ifelse(Podiel >= 0.08, paste0(round(Podiel * 100), "%"), "")),
    size = 3.0,
    color = "#1B1B1B"
  ) +
  facet_wrap(~ Outcome, ncol = 2) +
  scale_fill_gradient(low = "#F7FBFF", high = "#08519C") +
  labs(x = "Experimentálna bunka", y = "Skóre", fill = "Podiel") +
  theme_minimal(base_size = 11) +
  theme(axis.text.x = element_text(angle = 25, hjust = 1))
ggsave(figure_5c_path, width = 9.6, height = 6.6, dpi = 220)

rater_profiles <- analysis_long %>%
  group_by(rater_id) %>%
  summarise(
    `Index klinickej vierohodnosti_mean` = mean(plausibility_index, na.rm = TRUE),
    `Index klinickej vierohodnosti_sd` = sd(plausibility_index, na.rm = TRUE),
    `Index defektov_mean` = mean(defect_index, na.rm = TRUE),
    `Index defektov_sd` = sd(defect_index, na.rm = TRUE),
    `S1 závažnosť_mean` = mean(s1, na.rm = TRUE),
    `S1 závažnosť_sd` = sd(s1, na.rm = TRUE),
    `S2 funkčný dopad_mean` = mean(s2, na.rm = TRUE),
    `S2 funkčný dopad_sd` = sd(s2, na.rm = TRUE),
    `Počet hodnotení` = n(),
    .groups = "drop"
  ) %>%
  pivot_longer(
    cols = -c(rater_id, `Počet hodnotení`),
    names_to = c("Outcome", ".value"),
    names_pattern = "(.+)_(mean|sd)"
  )

figure_6_path <- normalizePath(file.path(figures_dir, "figure_6_rater_profiles.png"), mustWork = FALSE)
ggplot(rater_profiles, aes(x = factor(rater_id), y = mean)) +
  geom_pointrange(
    aes(ymin = pmax(mean - sd, 0), ymax = mean + sd),
    color = "#8C4C2E"
  ) +
  facet_wrap(~ Outcome, scales = "free_y") +
  labs(x = "Hodnotiteľ", y = "Priemer ± SD") +
  theme_minimal(base_size = 11)
ggsave(figure_6_path, width = 9.0, height = 6.0, dpi = 220)

figure_7_path <- normalizePath(file.path(figures_dir, "figure_7_comment_themes.png"), mustWork = FALSE)
ggplot(comment_themes, aes(x = reorder(`Téma komentára`, `Počet komentárov`), y = `Počet komentárov`)) +
  geom_col(fill = "#3E7C59", width = 0.7) +
  coord_flip() +
  labs(x = NULL, y = "Počet komentárov") +
  theme_minimal(base_size = 11)
ggsave(figure_7_path, width = 8.6, height = 4.8, dpi = 220)

table_1_path <- file.path(tables_dir, "table_1_dataset_overview.md")
table_2_path <- file.path(tables_dir, "table_2_rater_coverage.md")
table_3_path <- file.path(tables_dir, "table_3_overall_descriptives.md")
table_4_path <- file.path(tables_dir, "table_4_internal_consistency.md")
table_5_path <- file.path(tables_dir, "table_5_pair_agreement.md")
table_6_path <- file.path(tables_dir, "table_6_cell_descriptives.md")
table_6a_path <- file.path(tables_dir, "table_6a_cell_descriptives_rating.md")
table_6b_path <- file.path(tables_dir, "table_6b_cell_descriptives_transcript.md")
table_7_path <- file.path(tables_dir, "table_7_model_summary.md")
table_7a_path <- file.path(tables_dir, "table_7a_model_summary_rating.md")
table_7b_path <- file.path(tables_dir, "table_7b_model_summary_transcript.md")
table_8_path <- file.path(tables_dir, "table_8_guess_origin.md")
table_9_path <- file.path(tables_dir, "table_9_comment_themes.md")
table_10_path <- file.path(tables_dir, "table_10_anchored_subset.md")
table_s4_preview_path <- file.path(tables_dir, "table_s4_expert_review_items.md")
table_s5_preview_path <- file.path(tables_dir, "table_s5_expert_review_seeds.md")

write_md_table(dataset_overview, table_1_path, digits = 2)
write_md_table(rater_coverage, table_2_path, digits = 0)
write_md_table(overall_descriptives, table_3_path, digits = 2)
write_md_table(internal_consistency, table_4_path, digits = 2)
write_md_table(pair_agreement, table_5_path, digits = 2)
write_md_table(cell_descriptives, table_6_path, digits = 2)
write_md_table(cell_descriptives_rating, table_6a_path, digits = 2)
write_md_table(cell_descriptives_transcript, table_6b_path, digits = 2)
write_md_table(model_summary, table_7_path, digits = 2)
write_md_table(model_summary_rating, table_7a_path, digits = 2)
write_md_table(model_summary_transcript, table_7b_path, digits = 2)
write_md_table(guess_summary, table_8_path, digits = 2)
write_md_table(comment_themes, table_9_path, digits = 0)
write_md_table(anchored_summary, table_10_path, digits = 2)

if (file.exists(expert_items_csv_path) && file.exists(expert_seeds_csv_path)) {
  expert_items_preview <- readr::read_csv(expert_items_csv_path, show_col_types = FALSE) %>%
    mutate(`Potrebná doplňujúca úprava` = ifelse(`Potrebný follow-up`, "áno", "nie")) %>%
    select(-`Potrebný follow-up`)

  expert_seeds_preview <- readr::read_csv(expert_seeds_csv_path, show_col_types = FALSE) %>%
    transmute(
      `Kód scenára` = sprintf("%02d", as.integer(Seed)),
      `Scenár` = localized_scenario_label(Scenár),
      `Celkový priemer M`,
      `Dostatok informácií M`,
      `Nestereotypnosť M`,
      `Vhodnosť pre výskum M`,
      `Cieľová závažnosť`,
      `Modálna expert. závažnosť`,
      `Zhoda so závažnosťou (%)`
    )

  write_md_table(expert_items_preview, table_s4_preview_path, digits = 1)
  write_md_table(expert_seeds_preview, table_s5_preview_path, digits = 1)
}

writeLines(
  c(
    if (file.exists(table_s4_preview_path)) c(
      caption_lines("Tabuľka 1", "Predbežná expertná kontrola položiek hodnotiaceho nástroja"),
      readLines(table_s4_preview_path, warn = FALSE),
      "",
      caption_lines("Obrázok 1", "Tepelná mapa predbežnej expertnej kontroly položiek hodnotiaceho nástroja"),
      sprintf("![Obrázok 1](%s)", expert_items_heatmap_path),
      ""
    ) else character(0),
    if (file.exists(table_s5_preview_path)) c(
      caption_lines("Tabuľka 2", "Predbežná expertná kontrola východiskových scenárov"),
      readLines(table_s5_preview_path, warn = FALSE),
      "",
      caption_lines("Obrázok 2", "Tepelná mapa predbežnej expertnej kontroly východiskových scenárov"),
      sprintf("![Obrázok 2](%s)", expert_seeds_heatmap_path),
      "",
      "Poznámka. Táto validačná vrstva sa interpretuje ako predbežná obsahová kalibrácia nástroja a východiskových scenárov, nie ako finálny psychometrický dôkaz validity."
    ) else character(0)
  ),
  file.path(tables_dir, "fragment_validation.md"),
  useBytes = TRUE
)

writeLines(
  c(
    table_caption(3, "Základná charakteristika analyzovaného súboru hodnotení"),
    readLines(table_1_path, warn = FALSE),
    "",
    table_caption(4, "Pokrytie hodnotiteľov v analyzovanom súbore"),
    readLines(table_2_path, warn = FALSE),
    "",
    figure_caption(3, "Rozdelenie počtu hodnotení na prepis rozhovoru"),
    sprintf("![Obrázok 3](%s)", figure_1_path)
  ),
  file.path(tables_dir, "fragment_dataset.md"),
  useBytes = TRUE
)

writeLines(
  c(
    table_caption(5, "Deskriptívne ukazovatele hlavných ľudsky hodnotených premenných"),
    readLines(table_3_path, warn = FALSE),
    "",
    "Poznámka. Všetky `N` v tejto tabuľke predstavujú počty hodnotení. Pri viacerých položkách ostal medián aj IQR stlačený do úzkeho pásma; hodnotenia sa sústreďovali najmä v stredne vyšších kategóriách.",
    "",
    figure_caption(4, "Distribúcie hlavných kompozitov a vybraných položiek"),
    sprintf("![Obrázok 4](%s)", figure_2_path),
    "",
    figure_caption(5, "Frekvenčné profily odpovedí pre bloky G, S a R"),
    sprintf("![Obrázok 5](%s)", figure_3_path)
  ),
  file.path(tables_dir, "fragment_descriptives.md"),
  useBytes = TRUE
)

writeLines(
  c(
    table_caption(6, "Predbežná vnútorná konzistencia hodnotiacich blokov"),
    readLines(table_4_path, warn = FALSE),
    "",
    table_caption(7, "Zhoda jadrovej dvojice hodnotiteľov 13 a 14"),
    readLines(table_5_path, warn = FALSE),
    "",
    "Poznámka. ICC sa v tejto vrstve neuvádza ako hlavný ukazovateľ, keďže plné pokrytie zabezpečovala najmä dvojica hodnotiteľov 13 a 14 a jeden z nich používal škálu užšie.",
    "",
    figure_caption(6, "Profily hodnotiteľov podľa priemeru a variability"),
    sprintf("![Obrázok 6](%s)", figure_6_path)
  ),
  file.path(tables_dir, "fragment_measurement.md"),
  useBytes = TRUE
)

writeLines(
  c(
    caption_lines("Tabuľka 8", "Ukazovatele na úrovni jednotlivých hodnotení podľa experimentálnych buniek"),
    readLines(table_6a_path, warn = FALSE),
    "",
    sprintf("Poznámka. Všetky ukazovatele v tejto tabuľke vychádzajú zo %d ľudských hodnotení.", nrow(analysis_long)),
    "",
    caption_lines("Tabuľka 9", "Ukazovatele odchýlky na úrovni prepisov rozhovorov podľa experimentálnych buniek"),
    readLines(table_6b_path, warn = FALSE),
    "",
    sprintf(
      "Poznámka. Všetky ukazovatele v tejto tabuľke sú počítané na úrovni %d unikátnych prepisov rozhovorov.",
      n_distinct(analysis_transcript_anchored$transcript_id)
    ),
    "",
    figure_caption(7, "Krabicové grafy primárnych kompozitov podľa experimentálnych buniek"),
    sprintf("![Obrázok 7](%s)", figure_4_path),
    "",
    figure_caption(8, "Krabicové grafy vybraných položiek G2, G5, S1 a S2 podľa experimentálnych buniek"),
    sprintf("![Obrázok 8](%s)", figure_5_path)
  ),
  file.path(tables_dir, "fragment_cells.md"),
  useBytes = TRUE
)

writeLines(
  c(
    caption_lines("Tabuľka 10", "Kompaktný prehľad modelových odhadov na úrovni jednotlivých hodnotení"),
    readLines(table_7a_path, warn = FALSE),
    "",
    caption_lines("Tabuľka 11", "Kompaktný prehľad modelových odhadov na úrovni prepisov rozhovorov"),
    readLines(table_7b_path, warn = FALSE),
    "",
    "Poznámka. Referenčná bunka bola `G0 × P1`. Pri LMM pre index klinickej vierohodnosti a index defektov sú použité náhodné efekty pre východiskový scenár aj hodnotiteľa; pri troch ukazovateľoch odchýlky na úrovni prepisu rozhovoru len náhodný efekt pre východiskový scenár. Pri CLMM sú do kompaktnej tabuľky prenesené aj orientačné interakčné p-hodnoty pre najsilnejší interakčný člen. Formulácia `neuvádza sa` znamená, že daný riadok nemá v tejto kompaktnej projekcii priamo reportovanú interakčnú p-hodnotu."
  ),
  file.path(tables_dir, "fragment_models.md"),
  useBytes = TRUE
)

writeLines(
  c(
    table_caption(13, "Frekvenčný prehľad odhadovaného pôvodu rozhovoru"),
    readLines(table_8_path, warn = FALSE),
    "",
    table_caption(14, "Hrubé tematické kódy otvorených komentárov"),
    readLines(table_9_path, warn = FALSE),
    "",
    figure_caption(9, "Najčastejšie témy otvorených komentárov"),
    sprintf("![Obrázok 9](%s)", figure_7_path)
  ),
  file.path(tables_dir, "fragment_exploratory.md"),
  useBytes = TRUE
)

writeLines(
  c(
    table_caption(12, "Ukazovatele odchýlky voči referenčným hodnotám východiskových scenárov na úrovni prepisov rozhovorov"),
    readLines(table_10_path, warn = FALSE),
    "",
    "Poznámka. Všetky tri ukazovatele odchýlky sú sumarizované na úrovni prepisov rozhovorov. Pri chybe odhadu závažnosti a chybe odhadu funkčného dopadu ide o priemer expertných odhadov S1 a S2 na úrovni prepisu rozhovoru voči referenčným hodnotám východiskových scenárov."
  ),
  file.path(tables_dir, "fragment_anchored.md"),
  useBytes = TRUE
)

message("Current export preview assets written to ", tables_dir, " and ", figures_dir)
