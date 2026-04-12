#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tidyr)
  library(ggplot2)
  library(janitor)
  library(psych)
  library(lme4)
  library(ordinal)
  library(emmeans)
  library(cluster)
})

options(stringsAsFactors = FALSE, dplyr.summarise.inform = FALSE)

repo_root <- normalizePath(".", winslash = "/", mustWork = TRUE)
output_dir <- file.path(repo_root, "analysis", "outputs")
tables_dir <- file.path(repo_root, "tables")
figures_dir <- file.path(repo_root, "figures")

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

clean_paths <- list(
  ratings = file.path(repo_root, "analysis", "data_clean", "ratings_clean.csv"),
  transcripts = file.path(repo_root, "analysis", "data_clean", "transcripts_master.csv"),
  seeds = file.path(repo_root, "analysis", "data_clean", "seed_anchors_final.csv"),
  raters = file.path(repo_root, "analysis", "data_clean", "raters_clean.csv")
)

template_paths <- list(
  ratings = file.path(repo_root, "analysis", "templates", "ratings_template.csv"),
  transcripts = file.path(repo_root, "analysis", "templates", "transcripts_template.csv"),
  seeds = file.path(repo_root, "analysis", "templates", "seed_anchors_template.csv"),
  raters = file.path(repo_root, "analysis", "templates", "raters_template.csv")
)

severity_error_mode <- "direct_1to5"

expert_review_paths <- list(
  validation = file.path(repo_root, "analysis", "data_clean", "validation_experts_clean.csv"),
  items = file.path(repo_root, "analysis", "data_clean", "rater_items_expert_review_clean.csv"),
  seeds = file.path(repo_root, "analysis", "data_clean", "seeds_expert_review_clean.csv")
)

all_clean_available <- all(vapply(clean_paths, file.exists, logical(1)))
source_mode <- if (all_clean_available) "data_clean" else "templates_smoke_run"
input_paths <- if (all_clean_available) clean_paths else template_paths

read_clean_csv <- function(path) {
  readr::read_csv(path, show_col_types = FALSE) |>
    janitor::clean_names()
}

safe_numeric <- function(data, columns) {
  data |>
    mutate(across(any_of(columns), ~ suppressWarnings(as.numeric(.x))))
}

safe_row_mean <- function(data, columns) {
  cols <- intersect(columns, names(data))
  if (length(cols) == 0) {
    return(rep(NA_real_, nrow(data)))
  }

  matrix_data <- as.data.frame(data[, cols, drop = FALSE])
  non_missing <- rowSums(!is.na(matrix_data))
  values <- rowMeans(matrix_data, na.rm = TRUE)
  values[non_missing == 0] <- NA_real_
  values
}

safe_single_mean <- function(x) {
  if (all(is.na(x))) {
    return(NA_real_)
  }
  mean(x, na.rm = TRUE)
}

has_non_missing <- function(x) {
  any(!is.na(x))
}

status_row <- function(component, status, detail, outcome = NA_character_) {
  tibble(
    component = component,
    outcome = outcome,
    status = status,
    detail = detail
  )
}

write_status_csv <- function(path, component, detail, outcome = NA_character_) {
  readr::write_csv(
    status_row(component = component, status = "skipped", detail = detail, outcome = outcome),
    path
  )
}

placeholder_plot <- function(path, title, subtitle) {
  plot_obj <- ggplot() +
    annotate("text", x = 0, y = 0.1, label = title, size = 6, fontface = "bold") +
    annotate("text", x = 0, y = -0.1, label = subtitle, size = 4) +
    xlim(-1, 1) +
    ylim(-1, 1) +
    theme_void()

  ggsave(path, plot_obj, width = 9, height = 5, dpi = 150)
}

extract_confint <- function(model, terms) {
  ci <- tryCatch(
    suppressMessages(confint(model, method = "Wald")),
    error = function(e) NULL
  )

  if (is.null(ci)) {
    return(tibble(term = terms, conf_low = NA_real_, conf_high = NA_real_))
  }

  ci_df <- as.data.frame(ci)
  ci_df$term <- rownames(ci)
  rownames(ci_df) <- NULL

  ci_df |>
    transmute(
      term = .data$term,
      conf_low = .data[["2.5 %"]],
      conf_high = .data[["97.5 %"]]
    ) |>
    filter(term %in% terms)
}

fit_lmm <- function(data, outcome) {
  analysis_data <- data |>
    filter(!is.na(.data[[outcome]])) |>
    droplevels()

  enough_data <- nrow(analysis_data) >= 8 &&
    n_distinct(analysis_data$guardrail) >= 2 &&
    n_distinct(analysis_data$profile) >= 2 &&
    n_distinct(analysis_data$seed_id) >= 2 &&
    n_distinct(analysis_data$rater_id) >= 2

  if (!enough_data) {
    skipped <- tibble(
      outcome = outcome,
      model_type = "lmm",
      term = NA_character_,
      estimate = NA_real_,
      std_error = NA_real_,
      statistic = NA_real_,
      p_value = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "skipped",
      detail = "Insufficient rows or factor levels for LMM."
    )

    emmeans_skipped <- tibble(
      outcome = outcome,
      guardrail = NA_character_,
      profile = NA_character_,
      emmean = NA_real_,
      std_error = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "skipped",
      detail = "LMM not fitted."
    )

    return(list(model = NULL, tidy = skipped, emmeans = emmeans_skipped))
  }

  model_formula <- as.formula(
    paste(outcome, "~ guardrail * profile + (1 | seed_id) + (1 | rater_id)")
  )

  model <- tryCatch(
    suppressWarnings(lme4::lmer(model_formula, data = analysis_data, REML = FALSE)),
    error = function(e) e
  )

  if (inherits(model, "error")) {
    failed <- tibble(
      outcome = outcome,
      model_type = "lmm",
      term = NA_character_,
      estimate = NA_real_,
      std_error = NA_real_,
      statistic = NA_real_,
      p_value = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "failed",
      detail = conditionMessage(model)
    )

    emmeans_failed <- tibble(
      outcome = outcome,
      guardrail = NA_character_,
      profile = NA_character_,
      emmean = NA_real_,
      std_error = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "failed",
      detail = "LMM fit failed."
    )

    return(list(model = NULL, tidy = failed, emmeans = emmeans_failed))
  }

  coefficient_table <- as.data.frame(summary(model)$coefficients)
  coefficient_table$term <- rownames(coefficient_table)
  rownames(coefficient_table) <- NULL

  confint_table <- extract_confint(model, coefficient_table$term)

  tidy_table <- coefficient_table |>
    rename(
      estimate = Estimate,
      std_error = `Std. Error`
    ) |>
    mutate(
      statistic = if ("t value" %in% names(.)) .data[["t value"]] else NA_real_,
      p_value = NA_real_,
      outcome = outcome,
      model_type = "lmm",
      status = "ok",
      detail = NA_character_
    ) |>
    select(
      outcome, model_type, term, estimate, std_error,
      statistic, p_value, status, detail
    ) |>
    left_join(confint_table, by = "term") |>
    select(
      outcome, model_type, term, estimate, std_error, statistic,
      p_value, conf_low, conf_high, status, detail
    )

  emm_table <- tryCatch(
    {
      emm <- emmeans::emmeans(model, ~ guardrail * profile)
      as.data.frame(summary(emm, infer = c(TRUE, TRUE))) |>
        transmute(
          outcome = outcome,
          guardrail = as.character(.data$guardrail),
          profile = as.character(.data$profile),
          emmean = .data$emmean,
          std_error = .data$SE,
          conf_low = .data$lower.CL,
          conf_high = .data$upper.CL,
          status = "ok",
          detail = NA_character_
        )
    },
    error = function(e) {
      tibble(
        outcome = outcome,
        guardrail = NA_character_,
        profile = NA_character_,
        emmean = NA_real_,
        std_error = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "failed",
        detail = conditionMessage(e)
      )
    }
  )

  list(model = model, tidy = tidy_table, emmeans = emm_table)
}

fit_transcript_lmm <- function(data, outcome) {
  analysis_data <- data |>
    filter(!is.na(.data[[outcome]])) |>
    droplevels()

  enough_data <- nrow(analysis_data) >= 8 &&
    n_distinct(analysis_data$guardrail) >= 2 &&
    n_distinct(analysis_data$profile) >= 2 &&
    n_distinct(analysis_data$seed_id) >= 2

  if (!enough_data) {
    skipped <- tibble(
      outcome = outcome,
      model_type = "transcript_lmm",
      term = NA_character_,
      estimate = NA_real_,
      std_error = NA_real_,
      statistic = NA_real_,
      p_value = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "skipped",
      detail = "Insufficient transcript rows or factor levels for transcript-level LMM."
    )

    emmeans_skipped <- tibble(
      outcome = outcome,
      guardrail = NA_character_,
      profile = NA_character_,
      emmean = NA_real_,
      std_error = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "skipped",
      detail = "Transcript-level LMM not fitted."
    )

    return(list(model = NULL, tidy = skipped, emmeans = emmeans_skipped))
  }

  model_formula <- as.formula(
    paste(outcome, "~ guardrail * profile + (1 | seed_id)")
  )

  model <- tryCatch(
    suppressWarnings(lme4::lmer(model_formula, data = analysis_data, REML = FALSE)),
    error = function(e) e
  )

  if (inherits(model, "error")) {
    failed <- tibble(
      outcome = outcome,
      model_type = "transcript_lmm",
      term = NA_character_,
      estimate = NA_real_,
      std_error = NA_real_,
      statistic = NA_real_,
      p_value = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "failed",
      detail = conditionMessage(model)
    )

    emmeans_failed <- tibble(
      outcome = outcome,
      guardrail = NA_character_,
      profile = NA_character_,
      emmean = NA_real_,
      std_error = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "failed",
      detail = "Transcript-level LMM fit failed."
    )

    return(list(model = NULL, tidy = failed, emmeans = emmeans_failed))
  }

  coefficient_table <- as.data.frame(summary(model)$coefficients)
  coefficient_table$term <- rownames(coefficient_table)
  rownames(coefficient_table) <- NULL

  confint_table <- extract_confint(model, coefficient_table$term)

  tidy_table <- coefficient_table |>
    rename(
      estimate = Estimate,
      std_error = `Std. Error`
    ) |>
    mutate(
      statistic = if ("t value" %in% names(.)) .data[["t value"]] else NA_real_,
      p_value = NA_real_,
      outcome = outcome,
      model_type = "transcript_lmm",
      status = "ok",
      detail = NA_character_
    ) |>
    select(
      outcome, model_type, term, estimate, std_error,
      statistic, p_value, status, detail
    ) |>
    left_join(confint_table, by = "term") |>
    select(
      outcome, model_type, term, estimate, std_error, statistic,
      p_value, conf_low, conf_high, status, detail
    )

  emm_table <- tryCatch(
    {
      emm <- emmeans::emmeans(model, ~ guardrail * profile)
      as.data.frame(summary(emm, infer = c(TRUE, TRUE))) |>
        transmute(
          outcome = outcome,
          guardrail = as.character(.data$guardrail),
          profile = as.character(.data$profile),
          emmean = .data$emmean,
          std_error = .data$SE,
          conf_low = .data$lower.CL,
          conf_high = .data$upper.CL,
          status = "ok",
          detail = NA_character_
        )
    },
    error = function(e) {
      tibble(
        outcome = outcome,
        guardrail = NA_character_,
        profile = NA_character_,
        emmean = NA_real_,
        std_error = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "failed",
        detail = conditionMessage(e)
      )
    }
  )

  list(model = model, tidy = tidy_table, emmeans = emm_table)
}

fit_clmm <- function(data, outcome) {
  analysis_data <- data |>
    filter(!is.na(.data[[outcome]])) |>
    mutate(response = ordered(.data[[outcome]])) |>
    droplevels()

  enough_data <- nrow(analysis_data) >= 8 &&
    n_distinct(analysis_data$response) >= 2 &&
    n_distinct(analysis_data$guardrail) >= 2 &&
    n_distinct(analysis_data$profile) >= 2 &&
    n_distinct(analysis_data$seed_id) >= 2 &&
    n_distinct(analysis_data$rater_id) >= 2

  if (!enough_data) {
    return(
      tibble(
        outcome = outcome,
        model_type = "clmm",
        term = NA_character_,
        estimate = NA_real_,
        std_error = NA_real_,
        statistic = NA_real_,
        p_value = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "skipped",
        detail = "Insufficient rows, levels or response variation for CLMM."
      )
    )
  }

  model <- tryCatch(
    suppressWarnings(
      ordinal::clmm(
        response ~ guardrail * profile + (1 | seed_id) + (1 | rater_id),
        data = analysis_data
      )
    ),
    error = function(e) e
  )

  if (inherits(model, "error")) {
    return(
      tibble(
        outcome = outcome,
        model_type = "clmm",
        term = NA_character_,
        estimate = NA_real_,
        std_error = NA_real_,
        statistic = NA_real_,
        p_value = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "failed",
        detail = conditionMessage(model)
      )
    )
  }

  coefficient_table <- as.data.frame(summary(model)$coefficients)
  coefficient_table$term <- rownames(coefficient_table)
  rownames(coefficient_table) <- NULL

  coefficient_table |>
    transmute(
      outcome = outcome,
      model_type = "clmm",
      term = .data$term,
      estimate = .data$Estimate,
      std_error = .data$`Std. Error`,
      statistic = .data$`z value`,
      p_value = .data$`Pr(>|z|)`,
      conf_low = .data$Estimate - 1.96 * .data$`Std. Error`,
      conf_high = .data$Estimate + 1.96 * .data$`Std. Error`,
      status = "ok",
      detail = NA_character_
    )
}

compute_alpha_omega <- function(data, variables, block_label) {
  score_data <- data |>
    select(any_of(variables)) |>
    filter(if_any(everything(), ~ !is.na(.x)))

  if (ncol(score_data) < 2 || nrow(score_data) < 3) {
    return(
      tibble(
        block = block_label,
        n_items = ncol(score_data),
        n_rows = nrow(score_data),
        alpha = NA_real_,
        omega = NA_real_,
        status = "skipped",
        detail = "Insufficient rows or columns for alpha/omega."
      )
    )
  }

  alpha_obj <- tryCatch(
    psych::alpha(score_data, warnings = FALSE, check.keys = FALSE),
    error = function(e) e
  )

  omega_obj <- tryCatch(
    suppressWarnings(psych::omega(score_data, plot = FALSE, warnings = FALSE, nfactors = 1)),
    error = function(e) e
  )

  alpha_value <- if (inherits(alpha_obj, "error")) NA_real_ else unname(alpha_obj$total$raw_alpha)
  omega_value <- if (inherits(omega_obj, "error")) NA_real_ else unname(omega_obj$omega.tot)

  tibble(
    block = block_label,
    n_items = ncol(score_data),
    n_rows = nrow(score_data),
    alpha = alpha_value,
    omega = omega_value,
    status = if (is.na(alpha_value) && is.na(omega_value)) "failed" else "ok",
    detail = if (is.na(alpha_value) && is.na(omega_value)) {
      "Alpha and omega estimation failed."
    } else if (is.na(omega_value)) {
      "Alpha estimated; omega failed."
    } else {
      NA_character_
    }
  )
}

compute_icc <- function(data, value_var, outcome_label) {
  wide_data <- data |>
    select(transcript_id, rater_id, any_of(value_var)) |>
    filter(!is.na(.data[[value_var]])) |>
    distinct() |>
    mutate(
      transcript_id = as.character(.data$transcript_id),
      rater_id = as.character(.data$rater_id)
    ) |>
    pivot_wider(names_from = "rater_id", values_from = all_of(value_var))

  if (nrow(wide_data) < 2 || ncol(wide_data) < 3) {
    return(
      tibble(
        outcome = outcome_label,
        icc_type = "ICC2k",
        estimate = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "skipped",
        detail = "Need at least 2 transcripts and 2 raters for ICC."
      )
    )
  }

  score_matrix <- as.data.frame(wide_data[, -1, drop = FALSE])
  keep_cols <- colSums(!is.na(score_matrix)) > 0
  score_matrix <- score_matrix[, keep_cols, drop = FALSE]

  if (ncol(score_matrix) < 2) {
    return(
      tibble(
        outcome = outcome_label,
        icc_type = "ICC2k",
        estimate = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "skipped",
        detail = "Need at least 2 non-empty rater columns for ICC."
      )
    )
  }

  icc_obj <- tryCatch(
    psych::ICC(score_matrix),
    error = function(e) e
  )

  if (inherits(icc_obj, "error")) {
    return(
      tibble(
        outcome = outcome_label,
        icc_type = "ICC2k",
        estimate = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "failed",
        detail = conditionMessage(icc_obj)
      )
    )
  }

  icc_row <- icc_obj$results["ICC2k", , drop = FALSE]

  tibble(
    outcome = outcome_label,
    icc_type = "ICC2k",
    estimate = icc_row$ICC,
    conf_low = icc_row$`lower bound`,
    conf_high = icc_row$`upper bound`,
    status = "ok",
    detail = NA_character_
  )
}

compute_spearman_matrix <- function(transcript_summary) {
  variables <- c("plausibility_index", "defect_index", "symptom_error_mean", "g2", "g5")
  available <- intersect(variables, names(transcript_summary))

  if (length(available) < 2 || nrow(transcript_summary) < 3) {
    return(
      list(
        table = tibble(
          variable_1 = NA_character_,
          variable_2 = NA_character_,
          rho = NA_real_,
          status = "skipped",
          detail = "Need at least 3 transcripts and 2 variables for Spearman matrix."
        ),
        matrix = NULL
      )
    )
  }

  corr_matrix <- suppressWarnings(
    cor(
      transcript_summary[, available, drop = FALSE],
      method = "spearman",
      use = "pairwise.complete.obs"
    )
  )

  corr_table <- as.data.frame(as.table(corr_matrix)) |>
    rename(variable_1 = Var1, variable_2 = Var2, rho = Freq) |>
    mutate(
      status = "ok",
      detail = NA_character_
    )

  list(table = corr_table, matrix = corr_matrix)
}

run_pam_analysis <- function(transcript_summary) {
  pam_vars <- c("plausibility_index", "defect_index", "symptom_error_mean", "g2", "g5")
  optional_error_vars <- c("severity_error", "impact_error")
  available <- intersect(pam_vars, names(transcript_summary))
  available <- c(
    available,
    optional_error_vars[vapply(optional_error_vars, function(var) {
      var %in% names(transcript_summary) && has_non_missing(transcript_summary[[var]])
    }, logical(1))]
  )

  if (length(available) < 3 || nrow(transcript_summary) < 4) {
    skipped <- tibble(
      component = "pam",
      outcome = NA_character_,
      status = "skipped",
      detail = "Need at least 4 transcripts and 3 variables for PAM."
    )

    return(list(
      selection = skipped,
      assignments = skipped,
      profiles = skipped,
      crosstab = skipped,
      medoids = skipped,
      coordinates = NULL
    ))
  }

  pam_input <- transcript_summary |>
    select(any_of(c("transcript_id", "seed_id", "guardrail", "profile", available)))

  for (reverse_var in c("defect_index", "symptom_error_mean", "severity_error", "impact_error")) {
    if (reverse_var %in% names(pam_input)) {
      pam_input[[reverse_var]] <- -pam_input[[reverse_var]]
    }
  }

  model_vars <- setdiff(names(pam_input), c("transcript_id", "seed_id", "guardrail", "profile"))
  pam_input <- tidyr::drop_na(pam_input, any_of(model_vars))

  if (nrow(pam_input) < 4) {
    skipped <- tibble(
      component = "pam",
      outcome = NA_character_,
      status = "skipped",
      detail = "Too few complete transcript rows after removing missing values."
    )

    return(list(
      selection = skipped,
      assignments = skipped,
      profiles = skipped,
      crosstab = skipped,
      medoids = skipped,
      coordinates = NULL
    ))
  }

  scaled_matrix <- scale(pam_input[, model_vars, drop = FALSE])
  rownames(scaled_matrix) <- pam_input$transcript_id

  max_k <- min(4, nrow(pam_input) - 1)
  if (max_k < 2) {
    skipped <- tibble(
      component = "pam",
      outcome = NA_character_,
      status = "skipped",
      detail = "Too few transcripts for PAM model selection."
    )

    return(list(
      selection = skipped,
      assignments = skipped,
      profiles = skipped,
      crosstab = skipped,
      medoids = skipped,
      coordinates = NULL
    ))
  }

  k_values <- 2:max_k
  pam_models <- lapply(k_values, function(k) {
    tryCatch(cluster::pam(scaled_matrix, k = k), error = function(e) e)
  })

  model_selection <- bind_rows(lapply(seq_along(k_values), function(i) {
    model <- pam_models[[i]]
    if (inherits(model, "error")) {
      return(
        tibble(
          k = k_values[[i]],
          silhouette = NA_real_,
          n_clusters = k_values[[i]],
          status = "failed",
          detail = conditionMessage(model)
        )
      )
    }

    tibble(
      k = k_values[[i]],
      silhouette = model$silinfo$avg.width,
      n_clusters = length(unique(model$clustering)),
      status = "ok",
      detail = NA_character_
    )
  }))

  valid_rows <- model_selection |>
    filter(status == "ok", !is.na(silhouette))

  if (nrow(valid_rows) == 0) {
    skipped <- tibble(
      component = "pam",
      outcome = NA_character_,
      status = "failed",
      detail = "PAM model selection failed for all tested k."
    )

    return(list(
      selection = model_selection,
      assignments = skipped,
      profiles = skipped,
      crosstab = skipped,
      medoids = skipped,
      coordinates = NULL
    ))
  }

  best_k <- valid_rows |>
    arrange(desc(silhouette), k) |>
    dplyr::slice_head(n = 1) |>
    pull(k)

  best_model <- pam_models[[which(k_values == best_k)]]

  assignments <- pam_input |>
    mutate(cluster = paste0("C", best_model$clustering))

  profiles <- assignments |>
    group_by(cluster) |>
    summarise(
      across(all_of(model_vars), safe_single_mean),
      n_transcripts = n(),
      .groups = "drop"
    )

  crosstab <- bind_rows(
    assignments |>
      count(cluster, guardrail, name = "n") |>
      mutate(grouping = "guardrail"),
    assignments |>
      count(cluster, profile, name = "n") |>
      mutate(grouping = "profile"),
    assignments |>
      count(cluster, guardrail, profile, name = "n") |>
      mutate(grouping = "guardrail_profile")
  )

  medoid_names <- rownames(best_model$medoids)
  medoids <- assignments |>
    filter(transcript_id %in% medoid_names) |>
    mutate(is_medoid = TRUE)

  coordinates <- cmdscale(dist(scaled_matrix), k = 2) |>
    as.data.frame()
  coordinates$transcript_id <- rownames(coordinates)
  coordinates <- coordinates |>
    rename(dim1 = V1, dim2 = V2) |>
    left_join(assignments |> select(transcript_id, cluster), by = "transcript_id")

  list(
    selection = model_selection |>
      mutate(selected = ifelse(.data$k == best_k & .data$status == "ok", TRUE, FALSE)),
    assignments = assignments,
    profiles = profiles,
    crosstab = crosstab,
    medoids = medoids,
    coordinates = coordinates
  )
}

ratings <- read_clean_csv(input_paths$ratings)
transcripts <- read_clean_csv(input_paths$transcripts)
seeds <- read_clean_csv(input_paths$seeds)
raters <- read_clean_csv(input_paths$raters)

likert_1_5 <- c("g1", "g2", "g3", "g4", "g5", "s1", "s2", paste0("r", 1:5), "guess_confidence")
anchored_0_3 <- paste0("a", 1:9)

analysis_long <- ratings |>
  left_join(
    transcripts |>
      select(any_of(c("transcript_id", "chat_variability", "created_at", "transcript_path"))),
    by = "transcript_id"
  ) |>
  left_join(seeds, by = "seed_id") |>
  left_join(raters, by = "rater_id") |>
  safe_numeric(c(likert_1_5, anchored_0_3)) |>
  mutate(
    guardrail = factor(as.character(.data$guardrail), levels = c("0", "1"), labels = c("off", "on")),
    profile = factor(.data$profile, levels = c("R1", "R2", "R3")),
    seed_id = factor(.data$seed_id),
    rater_id = factor(.data$rater_id),
    transcript_id = factor(.data$transcript_id),
    guessed_origin = factor(.data$guessed_origin)
  )

analysis_long$plausibility_index <- safe_row_mean(analysis_long, c("g1", "g3", "g4"))
analysis_long$defect_index <- safe_row_mean(analysis_long, c("r1", "r2", "r3", "r4", "r5"))

for (item in paste0("a", 1:9)) {
  anchor_name <- paste0(item, "_anchor")
  error_name <- paste0(item, "_error")

  if (all(c(item, anchor_name) %in% names(analysis_long))) {
    analysis_long[[error_name]] <- abs(analysis_long[[item]] - analysis_long[[anchor_name]])
  } else {
    analysis_long[[error_name]] <- NA_real_
  }
}

analysis_long$symptom_error_mean <- safe_row_mean(analysis_long, paste0("a", 1:9, "_error"))
analysis_long$severity_error <- if (
  all(c("s1", "s1_anchor") %in% names(analysis_long))
) {
  abs(analysis_long$s1 - analysis_long$s1_anchor)
} else {
  rep(NA_real_, nrow(analysis_long))
}
analysis_long$impact_error <- if (
  all(c("s2", "s2_anchor") %in% names(analysis_long))
) {
  abs(analysis_long$s2 - analysis_long$s2_anchor)
} else {
  rep(NA_real_, nrow(analysis_long))
}

run_manifest <- tibble(
  run_timestamp = format(Sys.time(), "%Y-%m-%d %H:%M:%S %z"),
  source_mode = source_mode,
  used_ratings = input_paths$ratings,
  used_transcripts = input_paths$transcripts,
  used_seeds = input_paths$seeds,
  used_raters = input_paths$raters,
  severity_error_mode = severity_error_mode,
  n_rows_analysis_long = nrow(analysis_long),
  n_raters = n_distinct(analysis_long$rater_id),
  n_transcripts = n_distinct(analysis_long$transcript_id),
  n_seeds = n_distinct(analysis_long$seed_id)
)

qc_dataset_summary <- bind_rows(
  tibble(
    metric = c(
      "source_mode", "n_raters", "n_transcripts", "n_seeds", "n_ratings",
      "mean_ratings_per_transcript", "min_ratings_per_transcript", "max_ratings_per_transcript",
      "severity_error_mode"
    ),
    value = c(
      source_mode,
      as.character(n_distinct(analysis_long$rater_id)),
      as.character(n_distinct(analysis_long$transcript_id)),
      as.character(n_distinct(analysis_long$seed_id)),
      as.character(nrow(analysis_long)),
      as.character(round(mean(table(analysis_long$transcript_id)), 2)),
      as.character(min(table(analysis_long$transcript_id))),
      as.character(max(table(analysis_long$transcript_id))),
      severity_error_mode
    )
  ),
  analysis_long |>
    count(guardrail, name = "n") |>
    transmute(metric = paste0("guardrail_", .data$guardrail), value = as.character(.data$n)),
  analysis_long |>
    count(profile, name = "n") |>
    transmute(metric = paste0("profile_", .data$profile), value = as.character(.data$n)),
  analysis_long |>
    count(guardrail, profile, name = "n") |>
    transmute(metric = paste0("guardrail_", .data$guardrail, "_profile_", .data$profile), value = as.character(.data$n))
)

transcript_level_summary <- analysis_long |>
  group_by(transcript_id, seed_id, guardrail, profile) |>
  summarise(
    plausibility_index = safe_single_mean(.data$plausibility_index),
    defect_index = safe_single_mean(.data$defect_index),
    symptom_error_mean = safe_single_mean(.data$symptom_error_mean),
    s1 = safe_single_mean(.data$s1),
    s2 = safe_single_mean(.data$s2),
    severity_error = safe_single_mean(.data$severity_error),
    impact_error = safe_single_mean(.data$impact_error),
    g2 = safe_single_mean(.data$g2),
    g5 = safe_single_mean(.data$g5),
    n_ratings = n(),
    .groups = "drop"
  )

item_vars <- c(paste0("g", 1:5), paste0("a", 1:9), "s1", "s2", paste0("r", 1:5), "guess_confidence")
descriptives_items <- analysis_long |>
  select(any_of(item_vars)) |>
  pivot_longer(everything(), names_to = "variable", values_to = "value") |>
  group_by(variable) |>
  summarise(
    n_non_missing = sum(!is.na(value)),
    levels_used = n_distinct(value[!is.na(value)]),
    median = ifelse(n_non_missing == 0, NA_real_, median(value, na.rm = TRUE)),
    iqr = ifelse(n_non_missing == 0, NA_real_, IQR(value, na.rm = TRUE)),
    mean = ifelse(n_non_missing == 0, NA_real_, mean(value, na.rm = TRUE)),
    sd = ifelse(n_non_missing <= 1, NA_real_, sd(value, na.rm = TRUE)),
    min = ifelse(n_non_missing == 0, NA_real_, min(value, na.rm = TRUE)),
    max = ifelse(n_non_missing == 0, NA_real_, max(value, na.rm = TRUE))
  )

composite_vars <- c("plausibility_index", "defect_index", "symptom_error_mean")
if (has_non_missing(analysis_long$severity_error)) {
  composite_vars <- c(composite_vars, "severity_error")
}
if (has_non_missing(analysis_long$impact_error)) {
  composite_vars <- c(composite_vars, "impact_error")
}

descriptives_composites <- analysis_long |>
  select(any_of(composite_vars)) |>
  pivot_longer(everything(), names_to = "variable", values_to = "value") |>
  group_by(variable) |>
  summarise(
    n_non_missing = sum(!is.na(value)),
    mean = ifelse(n_non_missing == 0, NA_real_, mean(value, na.rm = TRUE)),
    sd = ifelse(n_non_missing <= 1, NA_real_, sd(value, na.rm = TRUE)),
    median = ifelse(n_non_missing == 0, NA_real_, median(value, na.rm = TRUE)),
    iqr = ifelse(n_non_missing == 0, NA_real_, IQR(value, na.rm = TRUE)),
    min = ifelse(n_non_missing == 0, NA_real_, min(value, na.rm = TRUE)),
    max = ifelse(n_non_missing == 0, NA_real_, max(value, na.rm = TRUE))
  )

item_frequencies <- analysis_long |>
  select(any_of(c(paste0("g", 1:5), "s1", "s2", paste0("r", 1:5)))) |>
  pivot_longer(everything(), names_to = "variable", values_to = "response") |>
  filter(!is.na(response)) |>
  count(variable, response, name = "n") |>
  group_by(variable) |>
  mutate(prop = n / sum(n)) |>
  ungroup()

internal_consistency <- bind_rows(
  compute_alpha_omega(analysis_long, paste0("g", 1:5), "g1_g5"),
  compute_alpha_omega(analysis_long, c("g1", "g3", "g4"), "plausibility_core"),
  compute_alpha_omega(analysis_long, paste0("r", 1:5), "r1_r5")
)

icc_summary <- bind_rows(
  compute_icc(analysis_long, "plausibility_index", "plausibility_index"),
  compute_icc(analysis_long, "defect_index", "defect_index"),
  compute_icc(analysis_long, "s1", "s1"),
  compute_icc(analysis_long, "s2", "s2")
)

rater_lmm_outcomes <- c("plausibility_index", "defect_index")
rater_lmm_results <- lapply(rater_lmm_outcomes, function(outcome) fit_lmm(analysis_long, outcome))
names(rater_lmm_results) <- rater_lmm_outcomes

transcript_lmm_outcomes <- c("symptom_error_mean")
if (has_non_missing(transcript_level_summary$severity_error)) {
  transcript_lmm_outcomes <- c(transcript_lmm_outcomes, "severity_error")
}
if (has_non_missing(transcript_level_summary$impact_error)) {
  transcript_lmm_outcomes <- c(transcript_lmm_outcomes, "impact_error")
}

transcript_lmm_results <- lapply(transcript_lmm_outcomes, function(outcome) {
  fit_transcript_lmm(transcript_level_summary, outcome)
})
names(transcript_lmm_results) <- transcript_lmm_outcomes

lmm_core_models <- bind_rows(c(
  lapply(rater_lmm_results, `[[`, "tidy"),
  lapply(transcript_lmm_results, `[[`, "tidy")
))
emmeans_core_models <- bind_rows(c(
  lapply(rater_lmm_results, `[[`, "emmeans"),
  lapply(transcript_lmm_results, `[[`, "emmeans")
))

clmm_outcomes <- c("g2", "g5", "s1", "s2", "guess_confidence")
clmm_item_models <- bind_rows(lapply(clmm_outcomes, function(outcome) fit_clmm(analysis_long, outcome)))
clmm_core_models <- clmm_item_models |>
  filter(outcome %in% c("g2", "g5", "s1", "s2"))

guess_origin_summary <- bind_rows(
  analysis_long |>
    count(guessed_origin, name = "n") |>
    mutate(grouping = "overall", guardrail = NA_character_, profile = NA_character_) |>
    group_by(grouping) |>
    mutate(prop = n / sum(n)) |>
    ungroup(),
  analysis_long |>
    count(guardrail, guessed_origin, name = "n") |>
    mutate(grouping = "guardrail", profile = NA_character_) |>
    group_by(grouping, guardrail) |>
    mutate(prop = n / sum(n)) |>
    ungroup(),
  analysis_long |>
    count(profile, guessed_origin, name = "n") |>
    mutate(grouping = "profile", guardrail = NA_character_) |>
    group_by(grouping, profile) |>
    mutate(prop = n / sum(n)) |>
    ungroup(),
  analysis_long |>
    count(guardrail, profile, guessed_origin, name = "n") |>
    mutate(grouping = "guardrail_profile") |>
    group_by(grouping, guardrail, profile) |>
    mutate(prop = n / sum(n)) |>
    ungroup()
)

guess_origin_logit <- {
  logit_data <- analysis_long |>
    mutate(perceived_ai = ifelse(.data$guessed_origin == "ai_generated", 1, 0)) |>
    filter(!is.na(.data$perceived_ai), !is.na(.data$plausibility_index), !is.na(.data$defect_index))

  if (nrow(logit_data) < 8 || n_distinct(logit_data$perceived_ai) < 2) {
    tibble(
      term = NA_character_,
      estimate = NA_real_,
      std_error = NA_real_,
      statistic = NA_real_,
      p_value = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "skipped",
      detail = "Insufficient rows or binary variation for logistic model."
    )
  } else {
    model <- tryCatch(
      glm(perceived_ai ~ plausibility_index + defect_index, data = logit_data, family = binomial()),
      error = function(e) e
    )

    if (inherits(model, "error")) {
      tibble(
        term = NA_character_,
        estimate = NA_real_,
        std_error = NA_real_,
        statistic = NA_real_,
        p_value = NA_real_,
        conf_low = NA_real_,
        conf_high = NA_real_,
        status = "failed",
        detail = conditionMessage(model)
      )
    } else {
      coef_table <- as.data.frame(summary(model)$coefficients)
      coef_table$term <- rownames(coef_table)
      rownames(coef_table) <- NULL

      conf_table <- suppressMessages(confint.default(model))
      conf_df <- as.data.frame(conf_table)
      conf_df$term <- rownames(conf_df)
      rownames(conf_df) <- NULL

      coef_table |>
        transmute(
          term = .data$term,
          estimate = .data$Estimate,
          std_error = .data$`Std. Error`,
          statistic = .data$`z value`,
          p_value = .data$`Pr(>|z|)`,
          status = "ok",
          detail = NA_character_
        ) |>
        left_join(
          conf_df |>
            transmute(term = .data$term, conf_low = .data$`2.5 %`, conf_high = .data$`97.5 %`),
          by = "term"
        )
    }
  }
}

comment_summary_stub <- analysis_long |>
  select(any_of(c("record_id", "rater_id", "transcript_id", "seed_id", "guardrail", "profile", "comment"))) |>
  mutate(comment = ifelse(is.na(.data$comment), "", .data$comment))

expert_review_summary <- {
  existing_files <- names(expert_review_paths)[vapply(expert_review_paths, file.exists, logical(1))]
  if (length(existing_files) == 0) {
    tibble(
      source = "missing",
      n_validation_experts = NA_integer_,
      n_item_review_rows = NA_integer_,
      n_seed_review_rows = NA_integer_,
      status = "skipped",
      detail = "No clean expert review CSV found in analysis/data_clean/."
    )
  } else {
    validation_n <- if (file.exists(expert_review_paths$validation)) nrow(read_clean_csv(expert_review_paths$validation)) else NA_integer_
    items_n <- if (file.exists(expert_review_paths$items)) nrow(read_clean_csv(expert_review_paths$items)) else NA_integer_
    seeds_n <- if (file.exists(expert_review_paths$seeds)) nrow(read_clean_csv(expert_review_paths$seeds)) else NA_integer_

    tibble(
      source = "data_clean",
      n_validation_experts = validation_n,
      n_item_review_rows = items_n,
      n_seed_review_rows = seeds_n,
      status = "ok",
      detail = NA_character_
    )
  }
}

spearman_result <- compute_spearman_matrix(transcript_level_summary)
pam_result <- run_pam_analysis(transcript_level_summary)

readr::write_csv(run_manifest, file.path(output_dir, "run_manifest.csv"))
readr::write_csv(analysis_long, file.path(output_dir, "analysis_long.csv"))
readr::write_csv(qc_dataset_summary, file.path(output_dir, "qc_dataset_summary.csv"))
readr::write_csv(descriptives_items, file.path(output_dir, "descriptives_items.csv"))
readr::write_csv(descriptives_composites, file.path(output_dir, "descriptives_composites.csv"))
readr::write_csv(expert_review_summary, file.path(output_dir, "expert_review_summary.csv"))
readr::write_csv(internal_consistency, file.path(output_dir, "internal_consistency.csv"))
readr::write_csv(icc_summary, file.path(output_dir, "icc_summary.csv"))
readr::write_csv(lmm_core_models, file.path(output_dir, "lmm_core_models.csv"))
readr::write_csv(clmm_item_models, file.path(output_dir, "clmm_item_models.csv"))
readr::write_csv(emmeans_core_models, file.path(output_dir, "emmeans_core_models.csv"))
readr::write_csv(guess_origin_summary, file.path(output_dir, "guess_origin_summary.csv"))
readr::write_csv(guess_origin_logit, file.path(output_dir, "guess_origin_logit.csv"))
readr::write_csv(comment_summary_stub, file.path(output_dir, "comment_summary_stub.csv"))
readr::write_csv(transcript_level_summary, file.path(output_dir, "transcript_level_summary.csv"))
readr::write_csv(spearman_result$table, file.path(output_dir, "spearman_transcript_composites.csv"))
readr::write_csv(pam_result$selection, file.path(output_dir, "pam_model_selection.csv"))
readr::write_csv(pam_result$assignments, file.path(output_dir, "pam_cluster_assignments.csv"))
readr::write_csv(pam_result$profiles, file.path(output_dir, "pam_cluster_profiles.csv"))
readr::write_csv(pam_result$crosstab, file.path(output_dir, "pam_cluster_condition_crosstab.csv"))
readr::write_csv(pam_result$medoids, file.path(output_dir, "pam_cluster_medoids.csv"))

readr::write_csv(qc_dataset_summary, file.path(tables_dir, "table_1_dataset_summary.csv"))
readr::write_csv(
  bind_rows(
    descriptives_items |> mutate(section = "items"),
    descriptives_composites |> mutate(section = "composites")
  ),
  file.path(tables_dir, "table_2_descriptives.csv")
)
readr::write_csv(item_frequencies, file.path(tables_dir, "table_3_item_frequencies.csv"))
readr::write_csv(internal_consistency, file.path(tables_dir, "table_4_internal_consistency.csv"))
readr::write_csv(icc_summary, file.path(tables_dir, "table_5_icc.csv"))
readr::write_csv(
  bind_rows(
    lmm_core_models |> mutate(model_family = "lmm"),
    clmm_core_models |> mutate(model_family = "clmm")
  ),
  file.path(tables_dir, "table_6_mixed_models_core.csv")
)
readr::write_csv(spearman_result$table, file.path(tables_dir, "table_s1_spearman_transcript_composites.csv"))
readr::write_csv(pam_result$profiles, file.path(tables_dir, "table_s2_pam_cluster_profiles.csv"))
readr::write_csv(pam_result$crosstab, file.path(tables_dir, "table_s3_pam_cluster_by_condition.csv"))

figure_1_path <- file.path(figures_dir, "figure_1_primary_outcomes_by_condition.png")
if (nrow(analysis_long) > 0) {
  figure_1_data <- analysis_long |>
    select(any_of(c("guardrail", "profile", "plausibility_index", "defect_index"))) |>
    pivot_longer(
      cols = c("plausibility_index", "defect_index"),
      names_to = "outcome",
      values_to = "value"
    ) |>
    filter(!is.na(.data$value))

  if (nrow(figure_1_data) > 0) {
    figure_1 <- ggplot(figure_1_data, aes(x = profile, y = value, fill = guardrail)) +
      geom_boxplot(alpha = 0.7, outlier.shape = NA) +
      geom_jitter(width = 0.1, height = 0, alpha = 0.7, size = 2) +
      facet_wrap(~ outcome, scales = "free_y") +
      labs(
        title = "Primary outcomes by experimental condition",
        subtitle = paste("Source mode:", source_mode),
        x = "Profile",
        y = "Score",
        fill = "Guardrail"
      ) +
      theme_minimal()

    ggsave(figure_1_path, figure_1, width = 10, height = 6, dpi = 150)
  } else {
    placeholder_plot(
      figure_1_path,
      "Figure 1 skipped",
      "No non-missing primary outcome values available."
    )
  }
} else {
  placeholder_plot(
    figure_1_path,
    "Figure 1 skipped",
    "Analysis dataset is empty."
  )
}

figure_2_path <- file.path(figures_dir, "figure_2_emmeans_core_models.png")
figure_2_data <- emmeans_core_models |>
  filter(status == "ok", outcome %in% c("plausibility_index", "defect_index"))

if (nrow(figure_2_data) > 0) {
  figure_2 <- ggplot(figure_2_data, aes(x = profile, y = emmean, color = guardrail, group = guardrail)) +
    geom_point(size = 3) +
    geom_line() +
    geom_errorbar(aes(ymin = conf_low, ymax = conf_high), width = 0.1) +
    facet_wrap(~ outcome, scales = "free_y") +
    labs(
      title = "Estimated marginal means for core mixed models",
      subtitle = paste("Source mode:", source_mode),
      x = "Profile",
      y = "Estimated marginal mean",
      color = "Guardrail"
    ) +
    theme_minimal()

  ggsave(figure_2_path, figure_2, width = 10, height = 6, dpi = 150)
} else {
  placeholder_plot(
    figure_2_path,
    "Figure 2 skipped",
    "Estimated marginal means are unavailable for current data."
  )
}

figure_s1_path <- file.path(figures_dir, "figure_s1_spearman_heatmap.png")
if (!is.null(spearman_result$matrix)) {
  heatmap_data <- as.data.frame(as.table(spearman_result$matrix)) |>
    rename(variable_1 = Var1, variable_2 = Var2, rho = Freq)

  figure_s1 <- ggplot(heatmap_data, aes(x = variable_1, y = variable_2, fill = rho)) +
    geom_tile(color = "white") +
    scale_fill_gradient2(low = "#b2182b", mid = "white", high = "#2166ac", midpoint = 0, limits = c(-1, 1)) +
    labs(
      title = "Transcript-level Spearman correlations",
      subtitle = paste("Source mode:", source_mode),
      x = NULL,
      y = NULL,
      fill = "rho"
    ) +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))

  ggsave(figure_s1_path, figure_s1, width = 8, height = 6, dpi = 150)
} else {
  placeholder_plot(
    figure_s1_path,
    "Figure S1 skipped",
    "Too few transcript-level rows for Spearman matrix."
  )
}

figure_s2_path <- file.path(figures_dir, "figure_s2_pam_cluster_map.png")
if (!is.null(pam_result$coordinates)) {
  figure_s2 <- ggplot(pam_result$coordinates, aes(x = dim1, y = dim2, color = cluster, label = transcript_id)) +
    geom_point(size = 3) +
    labs(
      title = "PAM cluster map",
      subtitle = paste("Source mode:", source_mode),
      x = "Dimension 1",
      y = "Dimension 2",
      color = "Cluster"
    ) +
    theme_minimal()

  ggsave(figure_s2_path, figure_s2, width = 8, height = 6, dpi = 150)
} else {
  placeholder_plot(
    figure_s2_path,
    "Figure S2 skipped",
    "Too few transcript-level rows for PAM."
  )
}

message("thesis_rating_pipeline.R completed.")
message("Source mode: ", source_mode)
message("Outputs written to analysis/outputs/, tables/ and figures/.")
