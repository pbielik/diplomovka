#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tidyr)
  library(ggplot2)
  library(janitor)
  library(psych)
  library(lme4)
  library(lmerTest)
  library(ordinal)
  library(emmeans)
  library(cluster)
})

options(stringsAsFactors = FALSE, dplyr.summarise.inform = FALSE)

repo_root <- normalizePath(".", winslash = "/", mustWork = TRUE)
output_dir <- file.path(repo_root, "analysis", "outputs")
tables_dir <- file.path(repo_root, "tables")
figures_dir <- file.path(repo_root, "figures")
styled_preview_dir <- file.path(tables_dir, "styled_preview")
codebook_path <- file.path(repo_root, "analysis", "codebook_rating_study.csv")

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(styled_preview_dir, recursive = TRUE, showWarnings = FALSE)

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

html_escape <- function(x) {
  x <- as.character(x)
  x <- gsub("&", "&amp;", x, fixed = TRUE)
  x <- gsub("<", "&lt;", x, fixed = TRUE)
  x <- gsub(">", "&gt;", x, fixed = TRUE)
  x <- gsub("\"", "&quot;", x, fixed = TRUE)
  x
}

display_header <- function(name) {
  mapped <- unname(header_label_map[name])
  if (!is.na(mapped) && nzchar(mapped)) {
    return(mapped)
  }

  gsub("_", " ", name, fixed = TRUE)
}

load_codebook_label_map <- function(path) {
  if (!file.exists(path)) {
    return(stats::setNames(character(0), character(0)))
  }

  codebook <- tryCatch(
    readr::read_csv(path, show_col_types = FALSE) |>
      janitor::clean_names(),
    error = function(e) NULL
  )

  if (is.null(codebook) || !all(c("variable", "label") %in% names(codebook))) {
    return(stats::setNames(character(0), character(0)))
  }

  labels <- trimws(codebook$label)
  names(labels) <- tolower(trimws(codebook$variable))
  labels
}

map_named_values <- function(x, mapping, normalize = FALSE) {
  values <- as.character(x)
  lookup <- if (normalize) tolower(values) else values
  mapped <- unname(mapping[lookup])
  fallback <- values
  replace_idx <- !is.na(mapped) & nzchar(mapped)
  fallback[replace_idx] <- mapped[replace_idx]
  fallback[is.na(x)] <- NA_character_
  fallback
}

guardrail_label_map <- c(
  "0" = "G0",
  "1" = "G1",
  "off" = "G0",
  "on" = "G1",
  "G0" = "G0",
  "G1" = "G1"
)

profile_label_map <- c(
  "R1" = "P1",
  "R2" = "P2",
  "R3" = "P3",
  "P1" = "P1",
  "P2" = "P2",
  "P3" = "P3"
)

section_label_map <- c(
  "items" = "Položky",
  "composites" = "Kompozity"
)

analysis_unit_label_map <- c(
  "rating" = "hodnotenie",
  "transcript" = "prepis rozhovoru"
)

block_label_map <- c(
  "g1_g5" = "Blok G1-G5",
  "plausibility_core" = "Jadro indexu klinickej vierohodnosti",
  "r1_r5" = "Blok R1-R5"
)

model_family_label_map <- c(
  "lmm" = "LMM",
  "clmm" = "CLMM"
)

model_type_label_map <- c(
  "lmm" = "LMM",
  "transcript_lmm" = "LMM (úroveň prepisu rozhovoru)",
  "lmm_sensitivity_transcript" = "LMM sensitivity s random interceptom pre prepis rozhovoru",
  "clmm" = "CLMM"
)

status_label_map <- c(
  "ok" = "ok",
  "skipped" = "preskočené",
  "failed" = "chyba"
)

grouping_label_map <- c(
  "overall" = "Celkovo",
  "guardrail" = "Klinické usmernenie",
  "profile" = "Profil",
  "guardrail_profile" = "Klinické usmernenie × profil"
)

guessed_origin_label_map <- c(
  "ai_generated" = "AI-generovaný rozhovor",
  "human_simulated" = "Ľudsky simulovaný rozhovor",
  "real_participant" = "Reálny participant",
  "unsure" = "Neisté"
)

source_mode_label_map <- c(
  "data_clean" = "Vyčistené dáta",
  "templates_smoke_run" = "Template smoke-run"
)

severity_error_mode_label_map <- c(
  "direct_1to5" = "Priama absolútna chyba na škále 1-5"
)

metric_label_map <- c(
  "source_mode" = "Zdroj dát",
  "n_raters" = "Počet hodnotiteľov",
  "n_transcripts" = "Počet prepisov rozhovorov",
  "n_seeds" = "Počet seedov",
  "n_ratings" = "Počet hodnotení",
  "mean_ratings_per_transcript" = "Priemerný počet hodnotení na prepis rozhovoru",
  "min_ratings_per_transcript" = "Minimálny počet hodnotení na prepis rozhovoru",
  "max_ratings_per_transcript" = "Maximálny počet hodnotení na prepis rozhovoru",
  "severity_error_mode" = "Spôsob výpočtu chyby závažnosti",
  "guardrail_off" = "Počet hodnotení v G0",
  "guardrail_on" = "Počet hodnotení v G1",
  "profile_R1" = "Počet hodnotení pre P1",
  "profile_R2" = "Počet hodnotení pre P2",
  "profile_R3" = "Počet hodnotení pre P3",
  "guardrail_off_profile_R1" = "G0 × P1",
  "guardrail_off_profile_R2" = "G0 × P2",
  "guardrail_off_profile_R3" = "G0 × P3",
  "guardrail_on_profile_R1" = "G1 × P1",
  "guardrail_on_profile_R2" = "G1 × P2",
  "guardrail_on_profile_R3" = "G1 × P3"
)

header_label_map <- c(
  "metric" = "Ukazovateľ",
  "value" = "Hodnota",
  "variable" = "Premenná",
  "section" = "Sekcia",
  "analysis_unit" = "Analytická úroveň",
  "n_non_missing" = "n",
  "levels_used" = "Počet použitých kategórií",
  "mean" = "Priemer",
  "sd" = "SD",
  "median" = "Medián",
  "iqr" = "IQR",
  "min" = "Min",
  "max" = "Max",
  "response" = "Odpoveď",
  "prop" = "Podiel",
  "block" = "Blok",
  "n_items" = "Počet položiek",
  "n_rows" = "Počet riadkov",
  "outcome" = "Ukazovateľ",
  "icc_type" = "Typ ICC",
  "model_family" = "Model",
  "model_type" = "Typ modelu",
  "term" = "Term",
  "estimate" = "Odhad",
  "std_error" = "SE",
  "statistic" = "Testová štatistika",
  "p_value" = "p",
  "conf_low" = "95 % CI dolná",
  "conf_high" = "95 % CI horná",
  "status" = "Stav",
  "detail" = "Poznámka",
  "variable_1" = "Premenná 1",
  "variable_2" = "Premenná 2",
  "rho" = "Spearmanovo rho",
  "grouping" = "Skupina",
  "guardrail" = "Klinické usmernenie",
  "profile" = "Profil",
  "cluster" = "Klastr",
  "n" = "Počet",
  "n_transcripts" = "Počet prepisov rozhovorov"
)

variable_label_map <- load_codebook_label_map(codebook_path)

label_variable <- function(x) {
  map_named_values(x, variable_label_map, normalize = TRUE)
}

label_guardrail <- function(x) {
  map_named_values(x, guardrail_label_map)
}

label_profile <- function(x) {
  map_named_values(x, profile_label_map)
}

label_model_term <- function(x) {
  values <- as.character(x)

  vapply(values, function(value) {
    if (is.na(value)) {
      return(NA_character_)
    }

    if (!nzchar(value)) {
      return(value)
    }

    if (value == "(Intercept)") {
      return("Intercept (referenčná kombinácia G0 × P1)")
    }

    normalized <- value
    normalized <- gsub("guardrailon", "guardrailG1", normalized, fixed = TRUE)
    normalized <- gsub("profileR", "profileP", normalized, fixed = TRUE)

    if (normalized == "guardrailG1") {
      return("Hlavný efekt klinického usmernenia G1 (vs. G0)")
    }

    if (normalized == "profileP2") {
      return("Hlavný efekt P2 (vs. P1)")
    }

    if (normalized == "profileP3") {
      return("Hlavný efekt P3 (vs. P1)")
    }

    if (normalized == "guardrailG1:profileP2" || normalized == "profileP2:guardrailG1") {
      return("Interakcia klinického usmernenia G1 × P2")
    }

    if (normalized == "guardrailG1:profileP3" || normalized == "profileP3:guardrailG1") {
      return("Interakcia klinického usmernenia G1 × P3")
    }

    value
  }, character(1), USE.NAMES = FALSE)
}

humanize_qc_dataset_summary <- function(data) {
  data |>
    mutate(
      value = case_when(
        .data$metric == "source_mode" ~ map_named_values(.data$value, source_mode_label_map),
        .data$metric == "severity_error_mode" ~ map_named_values(.data$value, severity_error_mode_label_map),
        TRUE ~ as.character(.data$value)
      ),
      metric = map_named_values(.data$metric, metric_label_map)
    )
}

humanize_descriptives_table <- function(data) {
  humanized <- data |>
    mutate(
      variable = label_variable(.data$variable),
      analysis_unit = map_named_values(.data$analysis_unit, analysis_unit_label_map)
    )

  if ("section" %in% names(humanized)) {
    humanized <- humanized |>
      mutate(section = map_named_values(.data$section, section_label_map))
  }

  humanized
}

humanize_item_frequencies <- function(data) {
  data |>
    mutate(variable = label_variable(.data$variable))
}

humanize_internal_consistency <- function(data) {
  data |>
    mutate(
      block = map_named_values(.data$block, block_label_map),
      status = map_named_values(.data$status, status_label_map)
    )
}

humanize_icc_table <- function(data) {
  data |>
    mutate(
      outcome = label_variable(.data$outcome),
      status = map_named_values(.data$status, status_label_map)
    )
}

humanize_model_table <- function(data) {
  humanized <- data |>
    mutate(
      outcome = label_variable(.data$outcome),
      term = label_model_term(.data$term),
      status = map_named_values(.data$status, status_label_map)
    )

  if ("model_family" %in% names(humanized)) {
    humanized <- humanized |>
      mutate(model_family = map_named_values(.data$model_family, model_family_label_map))
  }

  if ("model_type" %in% names(humanized)) {
    humanized <- humanized |>
      mutate(model_type = map_named_values(.data$model_type, model_type_label_map))
  }

  humanized
}

humanize_spearman_table <- function(data) {
  data |>
    mutate(
      variable_1 = label_variable(.data$variable_1),
      variable_2 = label_variable(.data$variable_2),
      status = map_named_values(.data$status, status_label_map)
    )
}

humanize_pam_profiles <- function(data) {
  if (all(c("component", "status", "detail") %in% names(data))) {
    return(data |> mutate(status = map_named_values(.data$status, status_label_map)))
  }

  data
}

humanize_pam_crosstab <- function(data) {
  if (all(c("component", "status", "detail") %in% names(data))) {
    return(data |> mutate(status = map_named_values(.data$status, status_label_map)))
  }

  data |>
    mutate(
      guardrail = label_guardrail(.data$guardrail),
      profile = label_profile(.data$profile),
      grouping = map_named_values(.data$grouping, grouping_label_map)
    )
}

humanize_emmeans_table <- function(data) {
  data |>
    mutate(
      outcome = label_variable(.data$outcome),
      guardrail = label_guardrail(.data$guardrail),
      profile = label_profile(.data$profile),
      status = map_named_values(.data$status, status_label_map)
    )
}

humanize_transcript_level_summary <- function(data) {
  data |>
    mutate(
      guardrail = label_guardrail(.data$guardrail),
      profile = label_profile(.data$profile)
    )
}

humanize_guess_origin_summary <- function(data) {
  humanized <- data |>
    mutate(
      grouping = map_named_values(.data$grouping, grouping_label_map),
      guardrail = label_guardrail(.data$guardrail),
      profile = label_profile(.data$profile),
      guessed_origin = ifelse(
        is.na(.data$guessed_origin) | .data$guessed_origin == "",
        "Nevyplnené",
        map_named_values(.data$guessed_origin, guessed_origin_label_map)
      )
    )

  if ("status" %in% names(humanized)) {
    humanized <- humanized |>
      mutate(status = map_named_values(.data$status, status_label_map))
  }

  humanized
}

humanize_guess_origin_logit <- function(data) {
  data |>
    mutate(
      term = dplyr::case_when(
        .data$term == "(Intercept)" ~ "Intercept",
        .data$term == "plausibility_index" ~ label_variable("plausibility_index"),
        .data$term == "defect_index" ~ label_variable("defect_index"),
        TRUE ~ .data$term
      ),
      status = map_named_values(.data$status, status_label_map)
    )
}

humanize_comment_summary <- function(data) {
  data |>
    mutate(
      guardrail = label_guardrail(.data$guardrail),
      profile = label_profile(.data$profile)
    )
}

format_cell_value <- function(x) {
  if (length(x) == 0 || is.na(x)) {
    return("")
  }

  if (inherits(x, c("Date", "POSIXct", "POSIXt"))) {
    return(as.character(x))
  }

  if (is.numeric(x)) {
    return(format(round(x, 3), nsmall = 0, trim = TRUE, scientific = FALSE))
  }

  as.character(x)
}

build_table_html_fragment <- function(data, caption_label, caption_title, note = NULL) {
  data <- as.data.frame(data, stringsAsFactors = FALSE)

  numeric_cols <- vapply(data, is.numeric, logical(1))
  header_html <- paste0(
    "<tr>",
    paste0(
      "<th>",
      html_escape(vapply(names(data), display_header, character(1))),
      "</th>",
      collapse = ""
    ),
    "</tr>"
  )

  if (nrow(data) == 0) {
    body_html <- paste0(
      "<tr><td colspan=\"",
      ncol(data),
      "\" class=\"empty-row\">Bez dostupných údajov.</td></tr>"
    )
  } else {
    body_html <- paste0(
      vapply(seq_len(nrow(data)), function(row_idx) {
        row_values <- data[row_idx, , drop = FALSE]
        cells <- vapply(seq_along(row_values), function(col_idx) {
          column_name <- names(row_values)[col_idx]
          css_class <- if (isTRUE(numeric_cols[[column_name]])) "num" else "text"
          paste0(
            "<td class=\"", css_class, "\">",
            html_escape(format_cell_value(row_values[[column_name]][[1]])),
            "</td>"
          )
        }, character(1))
        paste0("<tr>", paste0(cells, collapse = ""), "</tr>")
      }, character(1)),
      collapse = ""
    )
  }

  note_html <- if (!is.null(note) && nzchar(note)) {
    paste0("<p class=\"table-note\">Poznámka. ", html_escape(note), "</p>")
  } else {
    ""
  }

  paste0(
    "<section class=\"table-block\">",
    "<p class=\"caption-label\">", html_escape(caption_label), "</p>",
    "<p class=\"caption-title\">", html_escape(caption_title), "</p>",
    "<table class=\"thesis-table\"><thead>", header_html, "</thead><tbody>", body_html, "</tbody></table>",
    note_html,
    "</section>"
  )
}

write_table_html_page <- function(data, caption_label, caption_title, output_path, note = NULL) {
  page_html <- paste0(
    "<!DOCTYPE html><html lang=\"sk\"><head><meta charset=\"utf-8\">",
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
    "<title>", html_escape(caption_label), "</title>",
    "<style>",
    "body{font-family:'Times New Roman',serif;font-size:12pt;line-height:1.35;color:#000;margin:32px auto;max-width:1000px;padding:0 24px;}",
    ".caption-label{font-weight:700;margin:0 0 4px 0;}",
    ".caption-title{font-style:italic;margin:0 0 10px 0;}",
    ".thesis-table{width:100%;border-collapse:collapse;margin:0 0 10px 0;}",
    ".thesis-table th,.thesis-table td{padding:6px 8px;vertical-align:top;border-left:none;border-right:none;}",
    ".thesis-table thead th{border-top:1px solid #000;border-bottom:2px solid #000;text-align:left;}",
    ".thesis-table tbody td{border-bottom:1px solid #000;}",
    ".thesis-table td.num{text-align:right;white-space:nowrap;}",
    ".thesis-table td.text{text-align:left;}",
    ".empty-row{text-align:left;}",
    ".table-note{font-size:10.5pt;margin-top:6px;}",
    ".export-meta{font-size:10.5pt;color:#444;margin-top:18px;}",
    "</style></head><body>",
    build_table_html_fragment(data, caption_label, caption_title, note),
    "<p class=\"export-meta\">Automaticky exportované z analysis/scripts/thesis_rating_pipeline.R.</p>",
    "</body></html>"
  )

  writeLines(page_html, output_path, useBytes = TRUE)
}

build_figure_html_fragment <- function(image_rel_path, caption_label, caption_title, note = NULL) {
  note_html <- ""
  if (!is.null(note) && nzchar(note)) {
    note_html <- paste0("<p class=\"figure-note\">", html_escape(note), "</p>")
  }

  paste0(
    "<section class=\"figure-block\">",
    "<p class=\"caption-label\">", html_escape(caption_label), "</p>",
    "<p class=\"caption-title\">", html_escape(caption_title), "</p>",
    "<img src=\"", html_escape(image_rel_path), "\" alt=\"", html_escape(caption_title), "\" class=\"thesis-figure\">",
    note_html,
    "</section>"
  )
}

write_results_preview_page <- function(table_specs, figure_specs, output_path) {
  table_html <- paste0(
    vapply(table_specs, function(spec) {
      build_table_html_fragment(
        data = spec$data,
        caption_label = spec$caption_label,
        caption_title = spec$caption_title,
        note = spec$note
      )
    }, character(1)),
    collapse = ""
  )

  figure_html <- paste0(
    vapply(figure_specs, function(spec) {
      build_figure_html_fragment(
        image_rel_path = spec$image_rel_path,
        caption_label = spec$caption_label,
        caption_title = spec$caption_title,
        note = if ("note" %in% names(spec)) spec$note else NULL
      )
    }, character(1)),
    collapse = ""
  )

  page_html <- paste0(
    "<!DOCTYPE html><html lang=\"sk\"><head><meta charset=\"utf-8\">",
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
    "<title>Náhľad tabuliek a obrázkov</title>",
    "<style>",
    "body{font-family:'Times New Roman',serif;font-size:12pt;line-height:1.35;color:#000;margin:32px auto;max-width:1100px;padding:0 24px;}",
    "h1,h2{font-weight:700;}",
    "h1{font-size:18pt;margin:0 0 8px 0;} h2{font-size:14pt;margin:28px 0 10px 0;}",
    ".lead,.export-meta{font-size:10.5pt;color:#444;}",
    ".caption-label{font-weight:700;margin:0 0 4px 0;}",
    ".caption-title{font-style:italic;margin:0 0 10px 0;}",
    ".table-block,.figure-block{margin:0 0 26px 0;page-break-inside:avoid;}",
    ".thesis-table{width:100%;border-collapse:collapse;margin:0 0 10px 0;}",
    ".thesis-table th,.thesis-table td{padding:6px 8px;vertical-align:top;border-left:none;border-right:none;}",
    ".thesis-table thead th{border-top:1px solid #000;border-bottom:2px solid #000;text-align:left;}",
    ".thesis-table tbody td{border-bottom:1px solid #000;}",
    ".thesis-table td.num{text-align:right;white-space:nowrap;}",
    ".thesis-table td.text{text-align:left;}",
    ".empty-row{text-align:left;}",
    ".table-note{font-size:10.5pt;margin-top:6px;}",
    ".figure-note{font-size:10.5pt;margin-top:6px;}",
    ".thesis-figure{display:block;max-width:100%;height:auto;margin:0 auto;border:none;}",
    "</style></head><body>",
    "<h1>Náhľad tabuliek a obrázkov pre Results</h1>",
    "<p class=\"lead\">Štýl je nastavený podľa lokálneho sprievodcu: číslo nad objektom tučne, názov na ďalšom riadku kurzívou, bez zvislých čiar a s horizontálnymi oddeľovačmi.</p>",
    "<h2>Tabuľky</h2>",
    table_html,
    "<h2>Obrázky</h2>",
    figure_html,
    "<p class=\"export-meta\">Automaticky exportované z analysis/scripts/thesis_rating_pipeline.R.</p>",
    "</body></html>"
  )

  writeLines(page_html, output_path, useBytes = TRUE)
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

extract_emmeans_table <- function(model, outcome) {
  emm_summary <- as.data.frame(
    summary(
      emmeans::emmeans(model, ~ guardrail * profile, lmer.df = "satterthwaite"),
      infer = c(TRUE, TRUE)
    )
  )

  lower_name <- dplyr::case_when(
    "lower.CL" %in% names(emm_summary) ~ "lower.CL",
    "asymp.LCL" %in% names(emm_summary) ~ "asymp.LCL",
    TRUE ~ NA_character_
  )
  upper_name <- dplyr::case_when(
    "upper.CL" %in% names(emm_summary) ~ "upper.CL",
    "asymp.UCL" %in% names(emm_summary) ~ "asymp.UCL",
    TRUE ~ NA_character_
  )

  if (is.na(lower_name) || is.na(upper_name)) {
    stop("emmeans summary is missing confidence interval columns.")
  }

  emm_summary |>
    transmute(
      outcome = outcome,
      guardrail = as.character(.data$guardrail),
      profile = as.character(.data$profile),
      emmean = .data$emmean,
      std_error = .data$SE,
      conf_low = .data[[lower_name]],
      conf_high = .data[[upper_name]],
      status = "ok",
      detail = NA_character_
    )
}

extract_lmm_detail <- function(model) {
  detail_parts <- c("p_value from lmerTest Satterthwaite approximation.")

  singular_flag <- tryCatch(
    lme4::isSingular(model, tol = 1e-4),
    error = function(e) NA
  )

  if (isTRUE(singular_flag)) {
    detail_parts <- c(detail_parts, "Singular fit detected (tol = 1e-4).")
  }

  convergence_messages <- tryCatch(
    model@optinfo$conv$lme4$messages,
    error = function(e) NULL
  )

  if (!is.null(convergence_messages) && length(convergence_messages) > 0) {
    detail_parts <- c(
      detail_parts,
      paste("Convergence note:", paste(as.character(convergence_messages), collapse = " | "))
    )
  }

  paste(detail_parts, collapse = " ")
}

extract_clmm_detail <- function(model, response_levels) {
  detail_parts <- c(paste0("Response levels used: ", response_levels, "."))

  convergence_code <- tryCatch(
    {
      code <- model$convergence
      if (is.null(code) || length(code) == 0) {
        NA_real_
      } else {
        suppressWarnings(as.numeric(code[[1]]))
      }
    },
    error = function(e) NA
  )

  if (!is.na(convergence_code) && convergence_code != 0) {
    detail_parts <- c(detail_parts, paste0("Non-zero convergence code: ", convergence_code, "."))
  }

  paste(detail_parts, collapse = " ")
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
      detail = "Nedostatočný počet riadkov alebo úrovní faktorov pre LMM."
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
    suppressWarnings(lmerTest::lmer(model_formula, data = analysis_data, REML = FALSE)),
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
  has_t_value <- "t value" %in% names(coefficient_table)
  has_p_value <- "Pr(>|t|)" %in% names(coefficient_table)
  model_detail <- extract_lmm_detail(model)

  confint_table <- extract_confint(model, coefficient_table$term)

  tidy_table <- coefficient_table |>
    rename(
      estimate = Estimate,
      std_error = `Std. Error`
    ) |>
    mutate(
      statistic = if (has_t_value) .data[["t value"]] else NA_real_,
      p_value = if (has_p_value) .data[["Pr(>|t|)"]] else NA_real_,
      outcome = outcome,
      model_type = "lmm",
      status = "ok",
      detail = model_detail
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
    extract_emmeans_table(model, outcome),
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

fit_lmm_sensitivity_transcript <- function(data, outcome) {
  analysis_data <- data |>
    filter(!is.na(.data[[outcome]])) |>
    droplevels()

  enough_data <- nrow(analysis_data) >= 8 &&
    n_distinct(analysis_data$guardrail) >= 2 &&
    n_distinct(analysis_data$profile) >= 2 &&
    n_distinct(analysis_data$seed_id) >= 2 &&
    n_distinct(analysis_data$transcript_id) >= 2 &&
    n_distinct(analysis_data$rater_id) >= 2

  if (!enough_data) {
    skipped <- tibble(
      outcome = outcome,
      model_type = "lmm_sensitivity_transcript",
      term = NA_character_,
      estimate = NA_real_,
      std_error = NA_real_,
      statistic = NA_real_,
      p_value = NA_real_,
      conf_low = NA_real_,
      conf_high = NA_real_,
      status = "skipped",
      detail = "Nedostatočný počet riadkov alebo úrovní faktorov pre sensitivity LMM na úrovni prepisu rozhovoru."
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
      detail = "Sensitivity LMM na úrovni prepisu rozhovoru nebol odhadnutý."
    )

    return(list(model = NULL, tidy = skipped, emmeans = emmeans_skipped))
  }

  model_formula <- as.formula(
    paste(outcome, "~ guardrail * profile + (1 | seed_id) + (1 | transcript_id) + (1 | rater_id)")
  )

  model <- tryCatch(
    suppressWarnings(lmerTest::lmer(model_formula, data = analysis_data, REML = FALSE)),
    error = function(e) e
  )

  if (inherits(model, "error")) {
    failed <- tibble(
      outcome = outcome,
      model_type = "lmm_sensitivity_transcript",
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
      detail = "Odhad sensitivity LMM na úrovni prepisu rozhovoru zlyhal."
    )

    return(list(model = NULL, tidy = failed, emmeans = emmeans_failed))
  }

  coefficient_table <- as.data.frame(summary(model)$coefficients)
  coefficient_table$term <- rownames(coefficient_table)
  rownames(coefficient_table) <- NULL
  has_t_value <- "t value" %in% names(coefficient_table)
  has_p_value <- "Pr(>|t|)" %in% names(coefficient_table)
  model_detail <- paste(
    "Sensitivity model s random interceptom pre `transcript_id`.",
    extract_lmm_detail(model)
  )

  confint_table <- extract_confint(model, coefficient_table$term)

  tidy_table <- coefficient_table |>
    rename(
      estimate = Estimate,
      std_error = `Std. Error`
    ) |>
    mutate(
      statistic = if (has_t_value) .data[["t value"]] else NA_real_,
      p_value = if (has_p_value) .data[["Pr(>|t|)"]] else NA_real_,
      outcome = outcome,
      model_type = "lmm_sensitivity_transcript",
      status = "ok",
      detail = model_detail
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
    extract_emmeans_table(model, outcome),
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
      detail = "Nedostatočný počet riadkov alebo úrovní faktorov pre LMM na úrovni prepisu rozhovoru."
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
      detail = "LMM na úrovni prepisu rozhovoru nebol odhadnutý."
    )

    return(list(model = NULL, tidy = skipped, emmeans = emmeans_skipped))
  }

  model_formula <- as.formula(
    paste(outcome, "~ guardrail * profile + (1 | seed_id)")
  )

  model <- tryCatch(
    suppressWarnings(lmerTest::lmer(model_formula, data = analysis_data, REML = FALSE)),
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
      detail = "Odhad LMM na úrovni prepisu rozhovoru zlyhal."
    )

    return(list(model = NULL, tidy = failed, emmeans = emmeans_failed))
  }

  coefficient_table <- as.data.frame(summary(model)$coefficients)
  coefficient_table$term <- rownames(coefficient_table)
  rownames(coefficient_table) <- NULL
  has_t_value <- "t value" %in% names(coefficient_table)
  has_p_value <- "Pr(>|t|)" %in% names(coefficient_table)
  model_detail <- extract_lmm_detail(model)

  confint_table <- extract_confint(model, coefficient_table$term)

  tidy_table <- coefficient_table |>
    rename(
      estimate = Estimate,
      std_error = `Std. Error`
    ) |>
    mutate(
      statistic = if (has_t_value) .data[["t value"]] else NA_real_,
      p_value = if (has_p_value) .data[["Pr(>|t|)"]] else NA_real_,
      outcome = outcome,
      model_type = "transcript_lmm",
      status = "ok",
      detail = model_detail
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
    extract_emmeans_table(model, outcome),
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
  response_levels <- n_distinct(analysis_data$response)

  enough_data <- nrow(analysis_data) >= 8 &&
    response_levels >= 2 &&
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
        detail = "Nedostatočný počet riadkov, úrovní alebo variability odpovedí pre CLMM."
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
  model_detail <- extract_clmm_detail(model, response_levels)

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
      detail = model_detail
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
        detail = "Nedostatočný počet riadkov alebo stĺpcov pre alpha/omega."
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
      detail = "Na výpočet ICC sú potrebné aspoň 2 prepisy rozhovorov a 2 hodnotitelia."
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
        detail = "Na výpočet ICC sú potrebné aspoň 2 neprazdne stĺpce hodnotiteľov."
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
          detail = "Na Spearmanovu maticu sú potrebné aspoň 3 prepisy rozhovorov a 2 premenné."
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
      detail = "Na PAM analýzu sú potrebné aspoň 4 prepisy rozhovorov a 3 premenné."
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
      as.character(mean(table(analysis_long$transcript_id))),
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

transcript_level_items <- analysis_long |>
  group_by(transcript_id, seed_id, guardrail, profile) |>
  summarise(
    across(any_of(paste0("a", 1:9)), safe_single_mean),
    .groups = "drop"
  )

item_vars_rating <- c(paste0("g", 1:5), "s1", "s2", paste0("r", 1:5), "guess_confidence")
item_vars_transcript <- paste0("a", 1:9)

descriptives_items <- bind_rows(
  analysis_long |>
    select(any_of(item_vars_rating)) |>
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
      max = ifelse(n_non_missing == 0, NA_real_, max(value, na.rm = TRUE)),
      analysis_unit = "rating"
    ),
  transcript_level_items |>
    select(any_of(item_vars_transcript)) |>
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
      max = ifelse(n_non_missing == 0, NA_real_, max(value, na.rm = TRUE)),
      analysis_unit = "transcript"
    )
)

composite_vars_rating <- c("plausibility_index", "defect_index")
composite_vars_transcript <- c("symptom_error_mean")
if (has_non_missing(transcript_level_summary$severity_error)) {
  composite_vars_transcript <- c(composite_vars_transcript, "severity_error")
}
if (has_non_missing(transcript_level_summary$impact_error)) {
  composite_vars_transcript <- c(composite_vars_transcript, "impact_error")
}

descriptives_composites <- bind_rows(
  analysis_long |>
    select(any_of(composite_vars_rating)) |>
    pivot_longer(everything(), names_to = "variable", values_to = "value") |>
    group_by(variable) |>
    summarise(
      n_non_missing = sum(!is.na(value)),
      mean = ifelse(n_non_missing == 0, NA_real_, mean(value, na.rm = TRUE)),
      sd = ifelse(n_non_missing <= 1, NA_real_, sd(value, na.rm = TRUE)),
      median = ifelse(n_non_missing == 0, NA_real_, median(value, na.rm = TRUE)),
      iqr = ifelse(n_non_missing == 0, NA_real_, IQR(value, na.rm = TRUE)),
      min = ifelse(n_non_missing == 0, NA_real_, min(value, na.rm = TRUE)),
      max = ifelse(n_non_missing == 0, NA_real_, max(value, na.rm = TRUE)),
      analysis_unit = "rating"
    ),
  transcript_level_summary |>
    select(any_of(composite_vars_transcript)) |>
    pivot_longer(everything(), names_to = "variable", values_to = "value") |>
    group_by(variable) |>
    summarise(
      n_non_missing = sum(!is.na(value)),
      mean = ifelse(n_non_missing == 0, NA_real_, mean(value, na.rm = TRUE)),
      sd = ifelse(n_non_missing <= 1, NA_real_, sd(value, na.rm = TRUE)),
      median = ifelse(n_non_missing == 0, NA_real_, median(value, na.rm = TRUE)),
      iqr = ifelse(n_non_missing == 0, NA_real_, IQR(value, na.rm = TRUE)),
      min = ifelse(n_non_missing == 0, NA_real_, min(value, na.rm = TRUE)),
      max = ifelse(n_non_missing == 0, NA_real_, max(value, na.rm = TRUE)),
      analysis_unit = "transcript"
    )
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
rater_lmm_sensitivity_results <- lapply(rater_lmm_outcomes, function(outcome) {
  fit_lmm_sensitivity_transcript(analysis_long, outcome)
})
names(rater_lmm_sensitivity_results) <- rater_lmm_outcomes

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
lmm_sensitivity_transcript_models <- bind_rows(
  lapply(rater_lmm_sensitivity_results, `[[`, "tidy")
)
emmeans_sensitivity_transcript_models <- bind_rows(
  lapply(rater_lmm_sensitivity_results, `[[`, "emmeans")
)

clmm_outcomes <- c("g2", "g5", "s1", "s2", "guess_confidence")
clmm_item_models <- bind_rows(lapply(clmm_outcomes, function(outcome) fit_clmm(analysis_long, outcome)))
clmm_core_models <- clmm_item_models |>
  filter(
    outcome %in% c("g2", "g5", "s1", "s2"),
    grepl("guardrail|profile", term)
  )

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
      detail = "Nedostatočný počet riadkov alebo binárnej variability pre logistický model."
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

qc_dataset_summary_report <- humanize_qc_dataset_summary(qc_dataset_summary)
descriptives_items_report <- humanize_descriptives_table(descriptives_items)
descriptives_composites_report <- humanize_descriptives_table(descriptives_composites)
internal_consistency_report <- humanize_internal_consistency(internal_consistency)
icc_summary_report <- humanize_icc_table(icc_summary)
lmm_core_models_report <- humanize_model_table(lmm_core_models)
lmm_sensitivity_transcript_models_report <- humanize_model_table(lmm_sensitivity_transcript_models)
clmm_item_models_report <- humanize_model_table(clmm_item_models)
emmeans_core_models_report <- humanize_emmeans_table(emmeans_core_models)
emmeans_sensitivity_transcript_models_report <- humanize_emmeans_table(emmeans_sensitivity_transcript_models)
guess_origin_summary_report <- humanize_guess_origin_summary(guess_origin_summary)
guess_origin_logit_report <- humanize_guess_origin_logit(guess_origin_logit)
comment_summary_report <- humanize_comment_summary(comment_summary_stub)
transcript_level_summary_report <- humanize_transcript_level_summary(transcript_level_summary)
spearman_result_report <- humanize_spearman_table(spearman_result$table)
pam_profiles_report <- humanize_pam_profiles(pam_result$profiles)
pam_crosstab_report <- humanize_pam_crosstab(pam_result$crosstab)

readr::write_csv(run_manifest, file.path(output_dir, "run_manifest.csv"))
readr::write_csv(analysis_long, file.path(output_dir, "analysis_long.csv"))
readr::write_csv(qc_dataset_summary, file.path(output_dir, "qc_dataset_summary.csv"))
readr::write_csv(qc_dataset_summary_report, file.path(output_dir, "qc_dataset_summary_report.csv"))
readr::write_csv(descriptives_items, file.path(output_dir, "descriptives_items.csv"))
readr::write_csv(descriptives_items_report, file.path(output_dir, "descriptives_items_report.csv"))
readr::write_csv(descriptives_composites, file.path(output_dir, "descriptives_composites.csv"))
readr::write_csv(descriptives_composites_report, file.path(output_dir, "descriptives_composites_report.csv"))
readr::write_csv(expert_review_summary, file.path(output_dir, "expert_review_summary.csv"))
readr::write_csv(internal_consistency, file.path(output_dir, "internal_consistency.csv"))
readr::write_csv(internal_consistency_report, file.path(output_dir, "internal_consistency_report.csv"))
readr::write_csv(icc_summary, file.path(output_dir, "icc_summary.csv"))
readr::write_csv(icc_summary_report, file.path(output_dir, "icc_summary_report.csv"))
readr::write_csv(lmm_core_models, file.path(output_dir, "lmm_core_models.csv"))
readr::write_csv(lmm_core_models_report, file.path(output_dir, "lmm_core_models_report.csv"))
readr::write_csv(
  lmm_sensitivity_transcript_models,
  file.path(output_dir, "lmm_sensitivity_transcript_id_models.csv")
)
readr::write_csv(
  lmm_sensitivity_transcript_models_report,
  file.path(output_dir, "lmm_sensitivity_transcript_id_models_report.csv")
)
readr::write_csv(clmm_item_models, file.path(output_dir, "clmm_item_models.csv"))
readr::write_csv(clmm_item_models_report, file.path(output_dir, "clmm_item_models_report.csv"))
readr::write_csv(emmeans_core_models, file.path(output_dir, "emmeans_core_models.csv"))
readr::write_csv(emmeans_core_models_report, file.path(output_dir, "emmeans_core_models_report.csv"))
readr::write_csv(
  emmeans_sensitivity_transcript_models,
  file.path(output_dir, "emmeans_sensitivity_transcript_id_models.csv")
)
readr::write_csv(
  emmeans_sensitivity_transcript_models_report,
  file.path(output_dir, "emmeans_sensitivity_transcript_id_models_report.csv")
)
readr::write_csv(guess_origin_summary, file.path(output_dir, "guess_origin_summary.csv"))
readr::write_csv(guess_origin_summary_report, file.path(output_dir, "guess_origin_summary_report.csv"))
readr::write_csv(guess_origin_logit, file.path(output_dir, "guess_origin_logit.csv"))
readr::write_csv(guess_origin_logit_report, file.path(output_dir, "guess_origin_logit_report.csv"))
readr::write_csv(comment_summary_stub, file.path(output_dir, "comment_summary_stub.csv"))
readr::write_csv(comment_summary_report, file.path(output_dir, "comment_summary_stub_report.csv"))
readr::write_csv(transcript_level_summary, file.path(output_dir, "transcript_level_summary.csv"))
readr::write_csv(transcript_level_summary_report, file.path(output_dir, "transcript_level_summary_report.csv"))
readr::write_csv(spearman_result$table, file.path(output_dir, "spearman_transcript_composites.csv"))
readr::write_csv(spearman_result_report, file.path(output_dir, "spearman_transcript_composites_report.csv"))
readr::write_csv(pam_result$selection, file.path(output_dir, "pam_model_selection.csv"))
readr::write_csv(pam_result$assignments, file.path(output_dir, "pam_cluster_assignments.csv"))
readr::write_csv(pam_result$profiles, file.path(output_dir, "pam_cluster_profiles.csv"))
readr::write_csv(pam_profiles_report, file.path(output_dir, "pam_cluster_profiles_report.csv"))
readr::write_csv(pam_result$crosstab, file.path(output_dir, "pam_cluster_condition_crosstab.csv"))
readr::write_csv(pam_crosstab_report, file.path(output_dir, "pam_cluster_condition_crosstab_report.csv"))
readr::write_csv(pam_result$medoids, file.path(output_dir, "pam_cluster_medoids.csv"))

table_2_data <- bind_rows(
  descriptives_items |> mutate(section = "items"),
  descriptives_composites |> mutate(section = "composites")
)
table_6_data <- bind_rows(
  lmm_core_models |> mutate(model_family = "lmm"),
  clmm_core_models |> mutate(model_family = "clmm")
)
table_1_export <- qc_dataset_summary_report
table_2_export <- humanize_descriptives_table(table_2_data)
table_3_export <- humanize_item_frequencies(item_frequencies)
table_4_export <- internal_consistency_report
table_5_export <- icc_summary_report
table_6_export <- humanize_model_table(table_6_data)
table_s1_export <- spearman_result_report
table_s2_export <- pam_profiles_report
table_s3_export <- pam_crosstab_report
table_s6_export <- lmm_sensitivity_transcript_models_report

readr::write_csv(table_1_export, file.path(tables_dir, "table_1_dataset_summary.csv"))
readr::write_csv(
  table_2_export,
  file.path(tables_dir, "table_2_descriptives.csv")
)
readr::write_csv(table_3_export, file.path(tables_dir, "table_3_item_frequencies.csv"))
readr::write_csv(table_4_export, file.path(tables_dir, "table_4_internal_consistency.csv"))
readr::write_csv(table_5_export, file.path(tables_dir, "table_5_icc.csv"))
readr::write_csv(
  table_6_export,
  file.path(tables_dir, "table_6_mixed_models_core.csv")
)
readr::write_csv(
  table_s6_export,
  file.path(tables_dir, "table_s6_lmm_sensitivity_transcript_id.csv")
)
readr::write_csv(table_s1_export, file.path(tables_dir, "table_s1_spearman_transcript_composites.csv"))
readr::write_csv(table_s2_export, file.path(tables_dir, "table_s2_pam_cluster_profiles.csv"))
readr::write_csv(table_s3_export, file.path(tables_dir, "table_s3_pam_cluster_by_condition.csv"))

figure_1_path <- file.path(figures_dir, "figure_1_primary_outcomes_by_condition.png")
figure_1a_path <- file.path(figures_dir, "figure_1a_plausibility_index_by_condition.png")
figure_1b_path <- file.path(figures_dir, "figure_1b_defect_index_by_condition.png")
if (nrow(analysis_long) > 0) {
  figure_1_data <- analysis_long |>
    select(any_of(c("guardrail", "profile", "plausibility_index", "defect_index"))) |>
    pivot_longer(
      cols = c("plausibility_index", "defect_index"),
      names_to = "outcome",
      values_to = "value"
    ) |>
    mutate(
      guardrail = factor(label_guardrail(.data$guardrail), levels = c("G0", "G1")),
      profile = factor(label_profile(.data$profile), levels = c("P1", "P2", "P3")),
      outcome = factor(
        label_variable(.data$outcome),
        levels = label_variable(c("plausibility_index", "defect_index"))
      )
    ) |>
    filter(!is.na(.data$value))

  if (nrow(figure_1_data) > 0) {
    build_primary_outcome_boxplot <- function(data, outcome_label, title) {
      ggplot(filter(data, .data$outcome == outcome_label), aes(x = profile, y = value, fill = guardrail)) +
        geom_boxplot(alpha = 0.7, outlier.shape = NA) +
        geom_jitter(width = 0.1, height = 0, alpha = 0.7, size = 2) +
        labs(
          title = title,
          subtitle = paste("Zdroj dát:", map_named_values(source_mode, source_mode_label_map)),
          x = "Profil odpovedania",
          y = "Skóre",
          fill = "Klinické usmernenie"
        ) +
        theme_minimal() +
        theme(legend.position = "top")
    }

    figure_1 <- ggplot(figure_1_data, aes(x = profile, y = value, fill = guardrail)) +
      geom_boxplot(alpha = 0.7, outlier.shape = NA) +
      geom_jitter(width = 0.1, height = 0, alpha = 0.7, size = 2) +
      facet_wrap(~ outcome, scales = "free_y") +
      labs(
        title = "Primárne výstupné ukazovatele podľa experimentálnych podmienok",
        subtitle = paste("Zdroj dát:", map_named_values(source_mode, source_mode_label_map)),
        x = "Profil odpovedania",
        y = "Skóre",
        fill = "Klinické usmernenie"
      ) +
      theme_minimal()

    figure_1a <- build_primary_outcome_boxplot(
      figure_1_data,
      label_variable("plausibility_index"),
      "Index klinickej vierohodnosti podľa experimentálnych podmienok"
    )
    figure_1b <- build_primary_outcome_boxplot(
      figure_1_data,
      label_variable("defect_index"),
      "Index defektov podľa experimentálnych podmienok"
    )

    ggsave(figure_1_path, figure_1, width = 10, height = 6, dpi = 150)
    ggsave(figure_1a_path, figure_1a, width = 8, height = 6, dpi = 150)
    ggsave(figure_1b_path, figure_1b, width = 8, height = 6, dpi = 150)
  } else {
    placeholder_plot(
      figure_1_path,
      "Obrázok 1 nebol vytvorený",
      "Nie sú dostupné nenulové hodnoty primárnych výstupných ukazovateľov."
    )
    placeholder_plot(
      figure_1a_path,
      "Obrázok 1A nebol vytvorený",
      "Nie sú dostupné nenulové hodnoty indexu klinickej vierohodnosti."
    )
    placeholder_plot(
      figure_1b_path,
      "Obrázok 1B nebol vytvorený",
      "Nie sú dostupné nenulové hodnoty indexu defektov."
    )
  }
} else {
  placeholder_plot(
    figure_1_path,
    "Obrázok 1 nebol vytvorený",
    "Analytický súbor je prázdny."
  )
  placeholder_plot(
    figure_1a_path,
    "Obrázok 1A nebol vytvorený",
    "Analytický súbor je prázdny."
  )
  placeholder_plot(
    figure_1b_path,
    "Obrázok 1B nebol vytvorený",
    "Analytický súbor je prázdny."
  )
}

figure_2_path <- file.path(figures_dir, "figure_2_emmeans_core_models.png")
figure_2_data <- emmeans_core_models |>
  filter(status == "ok", outcome %in% c("plausibility_index", "defect_index")) |>
  mutate(
    guardrail = factor(label_guardrail(.data$guardrail), levels = c("G0", "G1")),
    profile = factor(label_profile(.data$profile), levels = c("P1", "P2", "P3")),
    outcome = factor(
      label_variable(.data$outcome),
      levels = label_variable(c("plausibility_index", "defect_index"))
    )
  )

if (nrow(figure_2_data) > 0) {
  figure_2 <- ggplot(figure_2_data, aes(x = profile, y = emmean, color = guardrail, group = guardrail)) +
    geom_point(size = 3) +
    geom_line() +
    geom_errorbar(aes(ymin = conf_low, ymax = conf_high), width = 0.1) +
    facet_wrap(~ outcome, scales = "free_y") +
    labs(
      title = "Odhadované marginálne priemery jadrových modelov",
      subtitle = paste("Zdroj dát:", map_named_values(source_mode, source_mode_label_map)),
      x = "Profil odpovedania",
      y = "Odhadovaný marginálny priemer",
      color = "Klinické usmernenie"
    ) +
    theme_minimal()

  ggsave(figure_2_path, figure_2, width = 10, height = 6, dpi = 150)
} else {
  placeholder_plot(
    figure_2_path,
    "Obrázok 2 nebol vytvorený",
    "Odhadované marginálne priemery nie sú pre aktuálne dáta dostupné."
  )
}

figure_s1_path <- file.path(figures_dir, "figure_s1_spearman_heatmap.png")
if (!is.null(spearman_result$matrix)) {
  heatmap_data <- as.data.frame(as.table(spearman_result$matrix)) |>
    rename(variable_1 = Var1, variable_2 = Var2, rho = Freq) |>
    mutate(
      variable_1 = factor(
        label_variable(.data$variable_1),
        levels = label_variable(c("plausibility_index", "defect_index", "symptom_error_mean", "g2", "g5"))
      ),
      variable_2 = factor(
        label_variable(.data$variable_2),
        levels = label_variable(c("plausibility_index", "defect_index", "symptom_error_mean", "g2", "g5"))
      )
    )

  figure_s1 <- ggplot(heatmap_data, aes(x = variable_1, y = variable_2, fill = rho)) +
    geom_tile(color = "white") +
    scale_fill_gradient2(low = "#b2182b", mid = "white", high = "#2166ac", midpoint = 0, limits = c(-1, 1)) +
    labs(
      title = "Spearmanove korelácie na úrovni prepisov rozhovorov",
      subtitle = paste("Zdroj dát:", map_named_values(source_mode, source_mode_label_map)),
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
    "Spearmanova heatmapa nebola vytvorená",
    "Na Spearmanovu maticu je príliš málo riadkov na úrovni prepisov rozhovorov."
  )
}

figure_s2_path <- file.path(figures_dir, "figure_s2_pam_cluster_map.png")
if (!is.null(pam_result$coordinates)) {
  figure_s2 <- ggplot(pam_result$coordinates, aes(x = dim1, y = dim2, color = cluster, label = transcript_id)) +
    geom_point(size = 3) +
    labs(
      title = "Mapa klastrov PAM",
      subtitle = paste("Zdroj dát:", map_named_values(source_mode, source_mode_label_map)),
      x = "Dimenzia 1",
      y = "Dimenzia 2",
      color = "Klastr"
    ) +
    theme_minimal()

  ggsave(figure_s2_path, figure_s2, width = 8, height = 6, dpi = 150)
} else {
  placeholder_plot(
    figure_s2_path,
    "Mapa PAM klastrov nebola vytvorená",
    "Na PAM analýzu je príliš málo riadkov na úrovni prepisov rozhovorov."
  )
}

main_table_specs <- list(
  list(
    data = table_1_export,
    caption_label = "Tabuľka 1",
    caption_title = "Základná charakteristika súboru hodnotení",
    note = paste("Zdroj dát:", map_named_values(source_mode, source_mode_label_map))
  ),
  list(
    data = table_2_export,
    caption_label = "Tabuľka 2",
    caption_title = "Deskriptívne ukazovatele položiek a kompozitov",
    note = "Export spája deskriptíva na úrovni položiek a kompozitov do jedného prehľadu pripraveného pre rukopis."
  ),
  list(
    data = table_3_export,
    caption_label = "Tabuľka 3",
    caption_title = "Frekvenčné rozdelenie kľúčových položiek",
    note = "Určené najmä pre G1 až G5, S1, S2 a R1 až R5; pri finálnom reporte sa dá podľa potreby zúžiť."
  ),
  list(
    data = table_4_export,
    caption_label = "Tabuľka 4",
    caption_title = "Vnútorná konzistencia hodnotiacich blokov",
    note = NULL
  ),
  list(
    data = table_5_export,
    caption_label = "Tabuľka 5",
    caption_title = "Zhoda medzi hodnotiteľmi pri hlavných výstupných ukazovateľoch",
    note = NULL
  ),
  list(
    data = table_6_export,
    caption_label = "Tabuľka 6",
    caption_title = "Súhrn jadrových zmiešaných modelov",
    note = "V kompaktnej podobe spája LMM a kľúčové CLMM výstupy."
  )
)

for (table_idx in seq_along(main_table_specs)) {
  spec <- main_table_specs[[table_idx]]
  write_table_html_page(
    data = spec$data,
    caption_label = spec$caption_label,
    caption_title = spec$caption_title,
    output_path = file.path(styled_preview_dir, paste0("table_", table_idx, ".html")),
    note = spec$note
  )
}

main_figure_specs <- list(
  list(
    image_rel_path = file.path("..", "..", "figures", basename(figure_1a_path)),
    caption_label = "Obrázok 1",
    caption_title = "Index klinickej vierohodnosti podľa experimentálnych podmienok",
    note = "Poznámka. Čierne body predstavujú jednotlivé hodnotenia; boxy zobrazujú medián a interkvartilové rozpätie. Vyššie skóre znamená vyššiu klinickú vierohodnosť."
  ),
  list(
    image_rel_path = file.path("..", "..", "figures", basename(figure_1b_path)),
    caption_label = "Obrázok 2",
    caption_title = "Index defektov podľa experimentálnych podmienok",
    note = "Poznámka. Čierne body predstavujú jednotlivé hodnotenia; boxy zobrazujú medián a interkvartilové rozpätie. Vyššie skóre znamená viac defektov, teda menej priaznivý výsledok."
  ),
  list(
    image_rel_path = file.path("..", "..", "figures", basename(figure_2_path)),
    caption_label = "Obrázok 3",
    caption_title = "Odhadované marginálne priemery jadrových modelov"
  )
)

write_results_preview_page(
  table_specs = main_table_specs,
  figure_specs = main_figure_specs,
  output_path = file.path(styled_preview_dir, "results_preview.html")
)

message("thesis_rating_pipeline.R completed.")
message("Source mode: ", source_mode)
message("Outputs written to analysis/outputs/, tables/, tables/styled_preview/ and figures/.")
