from __future__ import annotations

import csv
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

from qc_models import CheckResult, Finding, RunMode, SEVERITY_RANK

RATING_1_TO_5_FIELDS = [
    *(f"G{idx}" for idx in range(1, 6)),
    "S1",
    "S2",
    *(f"R{idx}" for idx in range(1, 6)),
    "guess_confidence",
]
RATING_0_TO_3_FIELDS = [*(f"A{idx}" for idx in range(1, 10))]
TRANSCRIPT_LEVEL_RATING_FIELDS = tuple(f"A{idx}" for idx in range(1, 10))
GUESSED_ORIGIN_ALLOWED = {"ai_generated", "human_simulated", "real_participant", "unsure"}
PROFILE_ALLOWED = {"R1", "R2", "R3"}
GUARDRAIL_ALLOWED = {"0", "1"}
PLACEHOLDER_PATTERN = re.compile(r"\[doplniť[^\]]*\]", re.IGNORECASE)
LOCAL_ABSOLUTE_PATH_PATTERN = re.compile(r"/Users/[^\s)`]+")
PREVIEW_META_PATTERNS = {
    "preview_workflow_meta": re.compile(
        r"\bpreview\b|autoritatívn|clean run|\bpipeline\b|\bworkflow\b|working estimate|partial-anchor",
        re.IGNORECASE,
    )
}
MANUAL_CITATION_PATTERN = re.compile(
    r"\((?:[A-ZÁČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ][A-Za-zÁ-ž'’\-]+(?: et al\.)?(?: & [A-ZÁČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ][A-Za-zÁ-ž'’\-]+)?),\s*(?:19|20)\d{2}[a-z]?\)"
)
CITEKEY_PATTERN = re.compile(r"(?<!\w)@([A-Za-z0-9][A-Za-z0-9:_-]*)")
BIB_KEY_PATTERN = re.compile(r"@\w+\{([^,]+),")

REQUIRED_COLUMNS = {
    "ratings": {
        "record_id",
        "rater_id",
        "transcript_id",
        "seed_id",
        "guardrail",
        "profile",
        "variant_id",
        "backend_model",
        "target_turns",
        "actual_turns",
        "rating_duration_sec",
        "G1",
        "G2",
        "G3",
        "G4",
        "G5",
        "A1",
        "A2",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
        "A9",
        "S1",
        "S2",
        "R1",
        "R2",
        "R3",
        "R4",
        "R5",
        "guessed_origin",
        "guess_confidence",
        "comment",
    },
    "transcripts": {
        "transcript_id",
        "seed_id",
        "guardrail",
        "profile",
        "variant_id",
        "backend_model",
        "target_turns",
        "actual_turns",
        "chat_variability",
        "created_at",
        "transcript_path",
    },
    "seeds": {
        "seed_id",
        *(f"A{idx}_anchor" for idx in range(1, 10)),
        "S1_anchor",
        "S2_anchor",
        "target_severity_label",
        "functional_impact_label",
        "notes",
    },
    "raters": {
        "rater_id",
        "profession",
        "specialization",
        "years_practice",
        "experience_with_mdd",
        "notes",
    },
    "run_manifest": {
        "run_timestamp",
        "source_mode",
        "used_ratings",
        "used_transcripts",
        "used_seeds",
        "used_raters",
        "severity_error_mode",
        "n_rows_analysis_long",
        "n_raters",
        "n_transcripts",
        "n_seeds",
    },
}


def run_all_hard_checks(repo_root: Path, run_mode: RunMode) -> list[CheckResult]:
    return [
        run_data_integrity_qc(repo_root, run_mode),
        run_artifact_projection_qc(repo_root, run_mode),
        run_citation_registry_qc(repo_root, run_mode),
        run_manuscript_state_qc(repo_root, run_mode),
        run_preview_layer_qc(repo_root, run_mode),
    ]


def run_data_integrity_qc(repo_root: Path, run_mode: RunMode) -> CheckResult:
    findings: list[Finding] = []
    ratings_path = repo_root / "analysis" / "data_clean" / "ratings_clean.csv"
    transcripts_path = repo_root / "analysis" / "data_clean" / "transcripts_master.csv"
    seeds_path = repo_root / "analysis" / "data_clean" / "seed_anchors_final.csv"
    raters_path = repo_root / "analysis" / "data_clean" / "raters_clean.csv"
    run_manifest_path = repo_root / "analysis" / "outputs" / "run_manifest.csv"
    qc_dataset_summary_path = repo_root / "analysis" / "outputs" / "qc_dataset_summary.csv"
    analysis_long_path = repo_root / "analysis" / "outputs" / "analysis_long.csv"
    raw_validation_csv_path = repo_root / "analysis" / "validity data" / "data.csv"

    required_paths = {
        "ratings": ratings_path,
        "transcripts": transcripts_path,
        "seeds": seeds_path,
        "raters": raters_path,
        "run_manifest": run_manifest_path,
    }

    loaded_rows: dict[str, list[dict[str, str]]] = {}
    column_ok: dict[str, bool] = {}
    for name, path in required_paths.items():
        if not path.exists():
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=path,
                    check_id="missing_required_file",
                    message=f"Chýba povinný súbor `{name}` pre data integrity QC.",
                    suggested_fix=f"Doplň alebo znovu vygeneruj `{relative_path(repo_root, path)}`.",
                )
            )
            column_ok[name] = False
            continue

        rows = read_csv_rows(path)
        loaded_rows[name] = rows
        header = set(rows[0].keys()) if rows else set(read_csv_header(path))
        missing_columns = sorted(REQUIRED_COLUMNS[name] - header)
        if missing_columns:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=path,
                    check_id="missing_required_columns",
                    message=f"Súbor nemá povinné stĺpce: {', '.join(missing_columns)}.",
                    suggested_fix="Zosúlaď export s `analysis/rating_export_readiness_checklist.md`.",
                )
            )
            column_ok[name] = False
        else:
            column_ok[name] = True

    findings.extend(check_raw_validation_csv_shape(repo_root, raw_validation_csv_path, run_mode))

    if not all(column_ok.values()):
        return CheckResult(name="data_integrity_qc", findings=findings)

    ratings_rows = loaded_rows["ratings"]
    transcripts_rows = loaded_rows["transcripts"]
    seeds_rows = loaded_rows["seeds"]
    raters_rows = loaded_rows["raters"]
    run_manifest_rows = loaded_rows["run_manifest"]

    if len(run_manifest_rows) != 1:
        findings.append(
            make_finding(
                area="data",
                severity="blocker",
                repo_root=repo_root,
                path=run_manifest_path,
                check_id="run_manifest_row_count",
                message=f"`run_manifest.csv` má {len(run_manifest_rows)} riadkov namiesto presne jedného.",
                suggested_fix="Nechaj pipeline znovu prepísať `analysis/outputs/run_manifest.csv` jedným aktuálnym runom.",
            )
        )
        return CheckResult(name="data_integrity_qc", findings=findings)

    run_manifest = run_manifest_rows[0]

    if severity_for_source_mode(run_mode, run_manifest.get("source_mode", "")) is not None:
        severity = severity_for_source_mode(run_mode, run_manifest.get("source_mode", ""))
        findings.append(
            make_finding(
                area="data",
                severity=severity,
                repo_root=repo_root,
                path=run_manifest_path,
                check_id="source_mode_not_data_clean",
                message=(
                    f"Posledný pipeline run má `source_mode = {run_manifest.get('source_mode', '')}`, "
                    "nie `data_clean`."
                ),
                suggested_fix="Spusť `analysis/scripts/thesis_rating_pipeline.R` nad `analysis/data_clean/*.csv` a obnov outputy.",
            )
        )

    findings.extend(check_unique_field(repo_root, ratings_path, ratings_rows, "record_id"))
    findings.extend(check_unique_field(repo_root, transcripts_path, transcripts_rows, "transcript_id"))
    findings.extend(check_unique_field(repo_root, seeds_path, seeds_rows, "seed_id"))
    findings.extend(check_unique_field(repo_root, raters_path, raters_rows, "rater_id"))

    duplicate_pairs = duplicate_key_refs(ratings_rows, ("rater_id", "transcript_id"))
    if duplicate_pairs:
        findings.append(
            make_finding(
                area="data",
                severity="blocker",
                repo_root=repo_root,
                path=ratings_path,
                check_id="duplicate_rater_transcript_pair",
                message=(
                    "Na kombinácii `rater_id + transcript_id` existujú duplicity: "
                    + ", ".join(sorted(duplicate_pairs)[:5])
                ),
                suggested_fix="Odstráň duplicitné ratingy alebo oprav export, aby 1 riadok = 1 hodnotenie 1 ratera na 1 transkripte.",
            )
        )

    findings.extend(validate_rating_value_domains(repo_root, ratings_path, ratings_rows))
    findings.extend(check_transcript_level_anchor_invariance(repo_root, ratings_path, ratings_rows))
    findings.extend(validate_transcript_rows(repo_root, transcripts_path, transcripts_rows))
    findings.extend(validate_seed_rows(repo_root, seeds_path, seeds_rows))
    findings.extend(validate_rater_rows(repo_root, raters_path, raters_rows))

    transcript_index = index_by(transcripts_rows, "transcript_id")
    seed_index = index_by(seeds_rows, "seed_id")
    rater_index = index_by(raters_rows, "rater_id")

    for row_number, row in enumerate(ratings_rows, start=2):
        transcript = transcript_index.get(row["transcript_id"])
        if transcript is None:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=ratings_path,
                    check_id="missing_transcript_join",
                    message=f"Rating `{row['record_id']}` odkazuje na neexistujúci transcript `{row['transcript_id']}`.",
                    evidence_refs=[f"line {row_number}"],
                    suggested_fix="Zosúlaď `ratings_clean.csv` a `transcripts_master.csv` podľa `transcript_id`.",
                )
            )
            continue

        for field_name in ("seed_id", "guardrail", "profile", "variant_id", "backend_model", "target_turns", "actual_turns"):
            if normalize_scalar(row[field_name]) != normalize_scalar(transcript[field_name]):
                findings.append(
                    make_finding(
                        area="data",
                        severity="blocker",
                        repo_root=repo_root,
                        path=ratings_path,
                        check_id="rating_transcript_metadata_mismatch",
                        message=(
                            f"Rating `{row['record_id']}` má iné `{field_name}` než naviazaný transcript "
                            f"`{row['transcript_id']}`."
                        ),
                        evidence_refs=[f"line {row_number}"],
                        suggested_fix="Skontroluj joins a export design metadata medzi ratings a transcripts.",
                    )
                )
                break

        if row["seed_id"] not in seed_index:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=ratings_path,
                    check_id="missing_seed_join",
                    message=f"Rating `{row['record_id']}` odkazuje na neexistujúci seed `{row['seed_id']}`.",
                    evidence_refs=[f"line {row_number}"],
                    suggested_fix="Doplň alebo oprav `seed_anchors_final.csv`.",
                )
            )

        if row["rater_id"] not in rater_index:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=ratings_path,
                    check_id="missing_rater_join",
                    message=f"Rating `{row['record_id']}` odkazuje na neexistujúceho ratera `{row['rater_id']}`.",
                    evidence_refs=[f"line {row_number}"],
                    suggested_fix="Doplň alebo oprav `raters_clean.csv`.",
                )
            )

    for row_number, row in enumerate(transcripts_rows, start=2):
        expected_variant = expected_variant_id(row["guardrail"], row["profile"])
        if row["variant_id"] != expected_variant:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=transcripts_path,
                    check_id="transcript_variant_mismatch",
                    message=(
                        f"Transcript `{row['transcript_id']}` má `variant_id = {row['variant_id']}`, "
                        f"očakávané je `{expected_variant}`."
                    ),
                    evidence_refs=[f"line {row_number}"],
                    suggested_fix="Oprav `variant_id` tak, aby sedel s `guardrail + profile`.",
                )
            )

        if row["seed_id"] not in seed_index:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=transcripts_path,
                    check_id="transcript_missing_seed",
                    message=f"Transcript `{row['transcript_id']}` odkazuje na neexistujúci seed `{row['seed_id']}`.",
                    evidence_refs=[f"line {row_number}"],
                    suggested_fix="Doplň chýbajúci seed alebo oprav `seed_id` v `transcripts_master.csv`.",
                )
            )

    findings.extend(compare_run_manifest_to_data(repo_root, run_manifest_path, run_manifest, ratings_rows, transcripts_rows, seeds_rows, raters_rows))

    if qc_dataset_summary_path.exists():
        expected_summary = compute_dataset_summary_rows(ratings_rows, run_manifest)
        actual_summary = read_csv_rows(qc_dataset_summary_path)
        findings.extend(
            compare_row_sets(
                repo_root=repo_root,
                expected_rows=expected_summary,
                actual_rows=actual_summary,
                expected_label="recomputed dataset summary",
                actual_path=qc_dataset_summary_path,
                key_fields=("metric",),
                check_id="qc_dataset_summary_mismatch",
                area="data",
                suggested_fix="Spusť pipeline znovu alebo oprav summary export tak, aby sedel s clean dátami.",
            )
        )

    if analysis_long_path.exists():
        analysis_long_rows = read_csv_rows(analysis_long_path)
        expected_rows = len(ratings_rows)
        if len(analysis_long_rows) != expected_rows:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=analysis_long_path,
                    check_id="analysis_long_row_count",
                    message=(
                        f"`analysis_long.csv` má {len(analysis_long_rows)} riadkov, "
                        f"ale clean ratings majú {expected_rows} riadkov."
                    ),
                    suggested_fix="Skontroluj join logiku pipeline a znovu exportuj `analysis_long.csv`.",
                )
            )

    return CheckResult(name="data_integrity_qc", findings=findings)


def run_artifact_projection_qc(repo_root: Path, run_mode: RunMode) -> CheckResult:
    findings: list[Finding] = []

    output_paths = {
        "qc_dataset_summary": repo_root / "analysis" / "outputs" / "qc_dataset_summary.csv",
        "descriptives_items": repo_root / "analysis" / "outputs" / "descriptives_items.csv",
        "descriptives_composites": repo_root / "analysis" / "outputs" / "descriptives_composites.csv",
        "transcript_level_summary": repo_root / "analysis" / "outputs" / "transcript_level_summary.csv",
        "internal_consistency": repo_root / "analysis" / "outputs" / "internal_consistency.csv",
        "icc_summary": repo_root / "analysis" / "outputs" / "icc_summary.csv",
        "lmm_core_models": repo_root / "analysis" / "outputs" / "lmm_core_models.csv",
        "clmm_item_models": repo_root / "analysis" / "outputs" / "clmm_item_models.csv",
        "analysis_long": repo_root / "analysis" / "outputs" / "analysis_long.csv",
    }
    table_paths = {
        "table_1": repo_root / "tables" / "table_1_dataset_summary.csv",
        "table_2": repo_root / "tables" / "table_2_descriptives.csv",
        "table_3": repo_root / "tables" / "table_3_item_frequencies.csv",
        "table_4": repo_root / "tables" / "table_4_internal_consistency.csv",
        "table_5": repo_root / "tables" / "table_5_icc.csv",
        "table_6": repo_root / "tables" / "table_6_mixed_models_core.csv",
    }
    figure_paths = {
        "figure_1": repo_root / "figures" / "figure_1_primary_outcomes_by_condition.png",
        "figure_2": repo_root / "figures" / "figure_2_emmeans_core_models.png",
    }

    all_required = {**output_paths, **table_paths, **figure_paths}
    for name, path in all_required.items():
        if not path.exists():
            findings.append(
                make_finding(
                    area="stats",
                    severity="blocker",
                    repo_root=repo_root,
                    path=path,
                    check_id="missing_artifact",
                    message=f"Chýba povinný artifact `{name}` pre projection QC.",
                    suggested_fix="Spusť pipeline znovu a doplň chýbajúce exporty do `analysis/outputs/`, `tables/` alebo `figures/`.",
                )
            )

    if any(finding.check_id == "missing_artifact" for finding in findings):
        return CheckResult(name="artifact_projection_qc", findings=findings)

    qc_dataset_summary = read_csv_rows(output_paths["qc_dataset_summary"])
    descriptives_items = read_csv_rows(output_paths["descriptives_items"])
    descriptives_composites = read_csv_rows(output_paths["descriptives_composites"])
    transcript_level_summary = read_csv_rows(output_paths["transcript_level_summary"])
    internal_consistency = read_csv_rows(output_paths["internal_consistency"])
    icc_summary = read_csv_rows(output_paths["icc_summary"])
    lmm_core_models = read_csv_rows(output_paths["lmm_core_models"])
    clmm_item_models = read_csv_rows(output_paths["clmm_item_models"])
    analysis_long = read_csv_rows(output_paths["analysis_long"])

    findings.extend(
        check_transcript_level_reporting_units(
            repo_root=repo_root,
            descriptives_items_path=output_paths["descriptives_items"],
            descriptives_items=descriptives_items,
            descriptives_composites_path=output_paths["descriptives_composites"],
            descriptives_composites=descriptives_composites,
        )
    )
    findings.extend(
        check_transcript_level_summary_projection(
            repo_root=repo_root,
            transcript_level_summary_path=output_paths["transcript_level_summary"],
            transcript_level_summary=transcript_level_summary,
            analysis_long_path=output_paths["analysis_long"],
            analysis_long=analysis_long,
        )
    )

    findings.extend(
        compare_row_sets(
            repo_root=repo_root,
            expected_rows=qc_dataset_summary,
            actual_rows=read_csv_rows(table_paths["table_1"]),
            expected_label="analysis/outputs/qc_dataset_summary.csv",
            actual_path=table_paths["table_1"],
            key_fields=("metric",),
            check_id="table_1_projection_mismatch",
            area="stats",
            suggested_fix="Znovu exportuj `table_1_dataset_summary.csv` z autoritatívneho outputu.",
        )
    )

    expected_table_2 = [dict(row, section="items") for row in descriptives_items] + [
        dict(row, section="composites") for row in descriptives_composites
    ]
    findings.extend(
        compare_row_sets(
            repo_root=repo_root,
            expected_rows=expected_table_2,
            actual_rows=read_csv_rows(table_paths["table_2"]),
            expected_label="descriptives_items + descriptives_composites",
            actual_path=table_paths["table_2"],
            key_fields=("section", "variable"),
            check_id="table_2_projection_mismatch",
            area="stats",
            suggested_fix="Znovu exportuj `table_2_descriptives.csv` z autoritatívnych descriptives outputov.",
        )
    )

    expected_table_3 = compute_item_frequency_rows(analysis_long)
    findings.extend(
        compare_row_sets(
            repo_root=repo_root,
            expected_rows=expected_table_3,
            actual_rows=read_csv_rows(table_paths["table_3"]),
            expected_label="recomputed item frequencies from analysis_long.csv",
            actual_path=table_paths["table_3"],
            key_fields=("variable", "response"),
            check_id="table_3_projection_mismatch",
            area="stats",
            suggested_fix="Znovu exportuj `table_3_item_frequencies.csv` z `analysis_long.csv`.",
        )
    )

    findings.extend(
        compare_row_sets(
            repo_root=repo_root,
            expected_rows=internal_consistency,
            actual_rows=read_csv_rows(table_paths["table_4"]),
            expected_label="analysis/outputs/internal_consistency.csv",
            actual_path=table_paths["table_4"],
            key_fields=("block",),
            check_id="table_4_projection_mismatch",
            area="stats",
            suggested_fix="Znovu exportuj `table_4_internal_consistency.csv` z autoritatívneho outputu.",
        )
    )

    findings.extend(
        compare_row_sets(
            repo_root=repo_root,
            expected_rows=icc_summary,
            actual_rows=read_csv_rows(table_paths["table_5"]),
            expected_label="analysis/outputs/icc_summary.csv",
            actual_path=table_paths["table_5"],
            key_fields=("outcome",),
            check_id="table_5_projection_mismatch",
            area="stats",
            suggested_fix="Znovu exportuj `table_5_icc.csv` z autoritatívneho outputu.",
        )
    )

    expected_table_6 = [dict(row, model_family="lmm") for row in lmm_core_models] + [
        dict(row, model_family="clmm")
        for row in clmm_item_models
        if row.get("outcome") in {"g2", "g5", "s1", "s2"}
    ]
    findings.extend(
        compare_row_sets(
            repo_root=repo_root,
            expected_rows=expected_table_6,
            actual_rows=read_csv_rows(table_paths["table_6"]),
            expected_label="lmm_core_models + clmm_item_models",
            actual_path=table_paths["table_6"],
            key_fields=("outcome", "model_type", "term"),
            check_id="table_6_projection_mismatch",
            area="stats",
            suggested_fix="Znovu exportuj `table_6_mixed_models_core.csv` z modelových outputov.",
        )
    )

    return CheckResult(name="artifact_projection_qc", findings=findings)


def run_citation_registry_qc(repo_root: Path, run_mode: RunMode) -> CheckResult:
    findings: list[Finding] = []
    bib_path = repo_root / "references" / "zotero-thesis.bib"
    manuscript_dir = repo_root / "manuscript"

    if not bib_path.exists():
        findings.append(
            make_finding(
                area="citation",
                severity="blocker",
                repo_root=repo_root,
                path=bib_path,
                check_id="missing_bib_export",
                message="Chýba `references/zotero-thesis.bib`.",
                suggested_fix="Obnov Better BibTeX export a skontroluj Zotero workflow.",
            )
        )
        return CheckResult(name="citation_registry_qc", findings=findings)

    manuscript_paths = sorted(manuscript_dir.glob("*.md"))
    if not manuscript_paths:
        findings.append(
            make_finding(
                area="citation",
                severity="blocker",
                repo_root=repo_root,
                path=manuscript_dir,
                check_id="missing_manuscript_files",
                message="V priečinku `manuscript/` sa nenašli žiadne Markdown súbory na citekey audit.",
                suggested_fix="Skontroluj štruktúru rukopisu alebo spusti QC na správnom repo root.",
            )
        )
        return CheckResult(name="citation_registry_qc", findings=findings)

    bib_keys = parse_bib_keys(bib_path.read_text(encoding="utf-8"))

    for path in manuscript_paths:
        text = path.read_text(encoding="utf-8")
        citekey_hits: defaultdict[str, list[int]] = defaultdict(list)
        manual_hits: list[int] = []

        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in CITEKEY_PATTERN.finditer(line):
                citekey_hits[match.group(1)].append(line_number)
            if MANUAL_CITATION_PATTERN.search(line) and "@" not in line:
                manual_hits.append(line_number)

        for citekey, line_numbers in sorted(citekey_hits.items()):
            if citekey not in bib_keys:
                findings.append(
                    make_finding(
                        area="citation",
                        severity="blocker",
                        repo_root=repo_root,
                        path=path,
                        check_id="missing_citekey_in_bib",
                        message=f"Citekey `@{citekey}` sa používa v rukopise, ale nie je v `zotero-thesis.bib`.",
                        evidence_refs=[f"line {line_no}" for line_no in line_numbers[:5]],
                        suggested_fix="Doplň chýbajúci zdroj do Zotera alebo oprav citekey placeholder v rukopise.",
                    )
                )

        if manual_hits:
            severity = "major" if run_mode != "final_results" else "blocker"
            findings.append(
                make_finding(
                    area="citation",
                    severity=severity,
                    repo_root=repo_root,
                    path=path,
                    check_id="manual_author_year_citation",
                    message="Rukopis obsahuje manuálne author-year citácie namiesto citekey placeholderov.",
                    evidence_refs=[f"line {line_no}" for line_no in manual_hits[:5]],
                    suggested_fix="Nahraď manuálne citácie formou `[@citekey]` a nechaj finálne APA citácie až na Word + Zotero plugin.",
                )
            )

    return CheckResult(name="citation_registry_qc", findings=findings)


def run_manuscript_state_qc(repo_root: Path, run_mode: RunMode) -> CheckResult:
    findings: list[Finding] = []
    results_path = repo_root / "manuscript" / "40_results.md"

    if not results_path.exists():
        findings.append(
            make_finding(
                area="presentation",
                severity="blocker",
                repo_root=repo_root,
                path=results_path,
                check_id="missing_results_manuscript",
                message="Chýba `manuscript/40_results.md`.",
                suggested_fix="Obnov alebo vytvor Results draft pred QC runom.",
            )
        )
        return CheckResult(name="manuscript_state_qc", findings=findings)

    text = results_path.read_text(encoding="utf-8")
    placeholder_lines = [
        line_number
        for line_number, line in enumerate(text.splitlines(), start=1)
        if PLACEHOLDER_PATTERN.search(line)
    ]
    if placeholder_lines:
        severity: str
        if run_mode == "final_results":
            severity = "blocker"
        elif run_mode == "pre_word":
            severity = "major"
        else:
            severity = "info"
        findings.append(
            make_finding(
                area="presentation",
                severity=severity,
                repo_root=repo_root,
                path=results_path,
                check_id="results_placeholders_present",
                message="`40_results.md` stále obsahuje `[doplniť ...]` placeholdery.",
                evidence_refs=[f"line {line_no}" for line_no in placeholder_lines[:8]],
                suggested_fix="Pred `pre_word` alebo `final_results` runom doplň všetky placeholdery reálnymi hodnotami z outputov.",
            )
        )

    skipped_refs = collect_skipped_outcome_refs(repo_root)
    if skipped_refs:
        severity = "info"
        if run_mode == "pre_word":
            severity = "major"
        elif run_mode == "final_results":
            severity = "blocker"
        findings.append(
            make_finding(
                area="stats",
                severity=severity,
                repo_root=repo_root,
                path=results_path,
                check_id="core_outputs_skipped",
                message="Core outputy stále obsahujú `status = skipped`, takže inferenčný Results text ešte nie je finálny.",
                evidence_refs=skipped_refs[:10],
                suggested_fix="Doplň ďalších raterov / plný run pipeline a až potom uzatváraj finálny Results draft.",
            )
        )

    return CheckResult(name="manuscript_state_qc", findings=findings)


def run_preview_layer_qc(repo_root: Path, run_mode: RunMode) -> CheckResult:
    findings: list[Finding] = []
    severity = "minor" if run_mode == "smoke" else "major"
    preview_manuscripts = [
        repo_root / "manuscript" / "40_results_preview_current_export.md",
        repo_root / "manuscript" / "50_discussion_preview_current_export.md",
    ]
    preview_fragments = [
        repo_root / "tables" / "current_export_preview" / "fragment_validation.md",
        repo_root / "tables" / "current_export_preview" / "fragment_measurement.md",
        repo_root / "tables" / "current_export_preview" / "fragment_anchored.md",
    ]

    for path in preview_manuscripts:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        local_path_refs = [
            f"line {line_number}"
            for line_number, line in enumerate(lines, start=1)
            if LOCAL_ABSOLUTE_PATH_PATTERN.search(line)
        ]
        if local_path_refs:
            findings.append(
                make_finding(
                    area="presentation",
                    severity=severity,
                    repo_root=repo_root,
                    path=path,
                    check_id="preview_local_absolute_path",
                    message="Preview prose obsahuje lokálne absolútne cesty, ktoré do Word-ready textu nepatria.",
                    evidence_refs=local_path_refs[:8],
                    suggested_fix="Odstráň lokálne filesystem cesty z preview Results/Discussion a nechaj len vecný akademický text.",
                )
            )

        findings.extend(
            collect_preview_meta_findings(
                repo_root=repo_root,
                path=path,
                severity=severity,
                lines=lines,
            )
        )

    for path in preview_fragments:
        if not path.exists():
            continue
        findings.extend(
            collect_preview_meta_findings(
                repo_root=repo_root,
                path=path,
                severity=severity,
                lines=path.read_text(encoding="utf-8").splitlines(),
            )
        )

    return CheckResult(name="preview_layer_qc", findings=findings)


def compute_dataset_summary_rows(ratings_rows: list[dict[str, str]], run_manifest: dict[str, str]) -> list[dict[str, str]]:
    transcript_counts = Counter(row["transcript_id"] for row in ratings_rows)
    guardrail_counts = Counter(guardrail_label(row["guardrail"]) for row in ratings_rows)
    profile_counts = Counter(row["profile"] for row in ratings_rows)
    combo_counts = Counter(f"{guardrail_label(row['guardrail'])}_{row['profile']}" for row in ratings_rows)

    mean_ratings = sum(transcript_counts.values()) / len(transcript_counts) if transcript_counts else 0.0

    rows: list[dict[str, str]] = [
        {"metric": "source_mode", "value": run_manifest.get("source_mode", "")},
        {"metric": "n_raters", "value": str(len({row['rater_id'] for row in ratings_rows}))},
        {"metric": "n_transcripts", "value": str(len(transcript_counts))},
        {"metric": "n_seeds", "value": str(len({row['seed_id'] for row in ratings_rows}))},
        {"metric": "n_ratings", "value": str(len(ratings_rows))},
        {"metric": "mean_ratings_per_transcript", "value": compact_number(mean_ratings)},
        {"metric": "min_ratings_per_transcript", "value": str(min(transcript_counts.values())) if transcript_counts else "0"},
        {"metric": "max_ratings_per_transcript", "value": str(max(transcript_counts.values())) if transcript_counts else "0"},
        {"metric": "severity_error_mode", "value": run_manifest.get("severity_error_mode", "")},
    ]

    for label in ("off", "on"):
        if label in guardrail_counts:
            rows.append({"metric": f"guardrail_{label}", "value": str(guardrail_counts[label])})
    for profile in sorted(profile_counts):
        rows.append({"metric": f"profile_{profile}", "value": str(profile_counts[profile])})
    for combo in sorted(combo_counts):
        guardrail_part, profile_part = combo.split("_", maxsplit=1)
        rows.append(
            {
                "metric": f"guardrail_{guardrail_part}_profile_{profile_part}",
                "value": str(combo_counts[combo]),
            }
        )

    return rows


def compute_item_frequency_rows(analysis_long_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    frequency_columns = [*(f"g{idx}" for idx in range(1, 6)), *(f"r{idx}" for idx in range(1, 6)), "s1", "s2"]
    output_rows: list[dict[str, str]] = []

    for column in frequency_columns:
        non_missing = [row[column] for row in analysis_long_rows if normalize_scalar(row.get(column)) is not None]
        total = len(non_missing)
        counts = Counter(non_missing)
        for response in sorted(counts, key=lambda value: float(value)):
            output_rows.append(
                {
                    "variable": column,
                    "response": response,
                    "n": str(counts[response]),
                    "prop": compact_number(counts[response] / total if total else 0.0),
                }
            )

    return output_rows


def compare_run_manifest_to_data(
    repo_root: Path,
    run_manifest_path: Path,
    run_manifest: dict[str, str],
    ratings_rows: list[dict[str, str]],
    transcripts_rows: list[dict[str, str]],
    seeds_rows: list[dict[str, str]],
    raters_rows: list[dict[str, str]],
) -> list[Finding]:
    findings: list[Finding] = []
    expected_counts = {
        "n_raters": len({row["rater_id"] for row in ratings_rows}),
        "n_transcripts": len({row["transcript_id"] for row in transcripts_rows}),
        "n_seeds": len({row["seed_id"] for row in transcripts_rows}),
        "n_rows_analysis_long": len(ratings_rows),
    }
    for field_name, expected_value in expected_counts.items():
        actual_value = normalize_scalar(run_manifest.get(field_name))
        if actual_value != expected_value:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=run_manifest_path,
                    check_id="run_manifest_count_mismatch",
                    message=(
                        f"`run_manifest.csv` má `{field_name} = {run_manifest.get(field_name)}`, "
                        f"ale z clean dát vychádza `{expected_value}`."
                    ),
                    suggested_fix="Znovu spusti pipeline alebo oprav `run_manifest.csv`, aby sedel s aktuálnymi clean dátami.",
                )
            )

    used_fields = {
        "used_ratings": "ratings_clean.csv",
        "used_transcripts": "transcripts_master.csv",
        "used_seeds": "seed_anchors_final.csv",
        "used_raters": "raters_clean.csv",
    }
    for field_name, expected_suffix in used_fields.items():
        raw_value = run_manifest.get(field_name, "")
        if raw_value and not raw_value.endswith(expected_suffix):
            findings.append(
                make_finding(
                    area="data",
                    severity="major",
                    repo_root=repo_root,
                    path=run_manifest_path,
                    check_id="run_manifest_input_path_suffix",
                    message=(
                        f"`run_manifest.csv` uvádza `{field_name} = {raw_value}`, "
                        f"čo nekončí na `{expected_suffix}`."
                    ),
                    suggested_fix="Skontroluj, či run_manifest ukazuje na správne clean vstupy posledného behu.",
                )
            )

    if run_manifest.get("severity_error_mode") != "direct_1to5":
        findings.append(
            make_finding(
                area="data",
                severity="major",
                repo_root=repo_root,
                path=run_manifest_path,
                check_id="unexpected_severity_error_mode",
                message=(
                    f"Pipeline bežala s `severity_error_mode = {run_manifest.get('severity_error_mode')}`, "
                    "očakávané je `direct_1to5`."
                ),
                suggested_fix="Skontroluj pipeline konfiguráciu pre `severity_error` a `impact_error` vetvu.",
            )
        )

    return findings


def validate_rating_value_domains(repo_root: Path, ratings_path: Path, rows: list[dict[str, str]]) -> list[Finding]:
    findings: list[Finding] = []
    invalid_refs: defaultdict[str, list[str]] = defaultdict(list)

    for row_number, row in enumerate(rows, start=2):
        if row["guardrail"] not in GUARDRAIL_ALLOWED:
            invalid_refs["guardrail"].append(f"{row['record_id']} (line {row_number})")
        if row["profile"] not in PROFILE_ALLOWED:
            invalid_refs["profile"].append(f"{row['record_id']} (line {row_number})")
        if row["variant_id"] != expected_variant_id(row["guardrail"], row["profile"]):
            invalid_refs["variant_id"].append(f"{row['record_id']} (line {row_number})")
        if row["guessed_origin"] not in GUESSED_ORIGIN_ALLOWED:
            invalid_refs["guessed_origin"].append(f"{row['record_id']} (line {row_number})")

        for field_name in RATING_1_TO_5_FIELDS:
            if not integer_in_range(row.get(field_name), 1, 5):
                invalid_refs[field_name].append(f"{row['record_id']} (line {row_number})")
        for field_name in RATING_0_TO_3_FIELDS:
            if not integer_in_range(row.get(field_name), 0, 3):
                invalid_refs[field_name].append(f"{row['record_id']} (line {row_number})")

        for numeric_field in ("target_turns", "actual_turns", "rating_duration_sec"):
            if normalize_scalar(row.get(numeric_field)) is None:
                invalid_refs[numeric_field].append(f"{row['record_id']} (line {row_number})")

    for field_name, refs in sorted(invalid_refs.items()):
        findings.append(
            make_finding(
                area="data",
                severity="blocker",
                repo_root=repo_root,
                path=ratings_path,
                check_id="invalid_rating_value_domain",
                message=f"Pole `{field_name}` má nevalidné hodnoty v rating exporte.",
                evidence_refs=refs[:8],
                suggested_fix="Oprav coding alebo export pravidlá pre `ratings_clean.csv`.",
            )
        )

    return findings


def check_transcript_level_anchor_invariance(
    repo_root: Path,
    ratings_path: Path,
    rows: list[dict[str, str]],
) -> list[Finding]:
    findings: list[Finding] = []
    for field_name in TRANSCRIPT_LEVEL_RATING_FIELDS:
        refs: list[str] = []
        values_by_transcript: defaultdict[str, set[int | float | str]] = defaultdict(set)
        for row in rows:
            value = normalize_scalar(row.get(field_name))
            if value is not None:
                values_by_transcript[row["transcript_id"]].add(value)

        for transcript_id, values in values_by_transcript.items():
            if len(values) > 1:
                refs.append(f"{transcript_id}: {sorted(map(str, values))}")

        if refs:
            findings.append(
                make_finding(
                    area="data",
                    severity="blocker",
                    repo_root=repo_root,
                    path=ratings_path,
                    check_id="transcript_level_metadata_not_invariant",
                    message=(
                        f"Pole `{field_name}` sa mení medzi ratermi v rámci toho istého transkriptu, "
                        "hoci A1-A9 majú byť transcript-level metadata."
                    ),
                    evidence_refs=refs[:8],
                    suggested_fix="Zosúlaď A1-A9 tak, aby boli v `ratings_clean.csv` invariantné v rámci každého `transcript_id`.",
                )
            )

    return findings


def validate_transcript_rows(repo_root: Path, transcripts_path: Path, rows: list[dict[str, str]]) -> list[Finding]:
    findings: list[Finding] = []
    invalid_refs: defaultdict[str, list[str]] = defaultdict(list)

    for row_number, row in enumerate(rows, start=2):
        if row["guardrail"] not in GUARDRAIL_ALLOWED:
            invalid_refs["guardrail"].append(f"{row['transcript_id']} (line {row_number})")
        if row["profile"] not in PROFILE_ALLOWED:
            invalid_refs["profile"].append(f"{row['transcript_id']} (line {row_number})")
        if row["variant_id"] != expected_variant_id(row["guardrail"], row["profile"]):
            invalid_refs["variant_id"].append(f"{row['transcript_id']} (line {row_number})")
        for numeric_field in ("target_turns", "actual_turns"):
            if normalize_scalar(row.get(numeric_field)) is None:
                invalid_refs[numeric_field].append(f"{row['transcript_id']} (line {row_number})")
        if not row.get("transcript_path", "").endswith(".txt"):
            invalid_refs["transcript_path"].append(f"{row['transcript_id']} (line {row_number})")

    for field_name, refs in sorted(invalid_refs.items()):
        findings.append(
            make_finding(
                area="data",
                severity="blocker",
                repo_root=repo_root,
                path=transcripts_path,
                check_id="invalid_transcript_value_domain",
                message=f"Pole `{field_name}` má nevalidné hodnoty v `transcripts_master.csv`.",
                evidence_refs=refs[:8],
                suggested_fix="Oprav `transcripts_master.csv` tak, aby sedel s export contractom.",
            )
        )

    return findings


def validate_seed_rows(repo_root: Path, seeds_path: Path, rows: list[dict[str, str]]) -> list[Finding]:
    findings: list[Finding] = []
    invalid_refs: defaultdict[str, list[str]] = defaultdict(list)

    for row_number, row in enumerate(rows, start=2):
        for idx in range(1, 10):
            field_name = f"A{idx}_anchor"
            if not integer_in_range(row.get(field_name), 0, 3):
                invalid_refs[field_name].append(f"{row['seed_id']} (line {row_number})")
        for field_name in ("S1_anchor", "S2_anchor"):
            if not integer_in_range(row.get(field_name), 1, 5):
                invalid_refs[field_name].append(f"{row['seed_id']} (line {row_number})")

    for field_name, refs in sorted(invalid_refs.items()):
        findings.append(
            make_finding(
                area="data",
                severity="blocker",
                repo_root=repo_root,
                path=seeds_path,
                check_id="invalid_seed_anchor_domain",
                message=f"Anchor pole `{field_name}` má nevalidné hodnoty.",
                evidence_refs=refs[:8],
                suggested_fix="Oprav `seed_anchors_final.csv` tak, aby A* anchor polia boli `0-3` a `S1/S2_anchor` boli `1-5`.",
            )
        )

    return findings


def validate_rater_rows(repo_root: Path, raters_path: Path, rows: list[dict[str, str]]) -> list[Finding]:
    findings: list[Finding] = []
    invalid_refs: defaultdict[str, list[str]] = defaultdict(list)

    for row_number, row in enumerate(rows, start=2):
        years_practice = row.get("years_practice", "").strip()
        if not re.fullmatch(r"\d+(?:\.\d+)?|\d+_plus", years_practice):
            invalid_refs["years_practice"].append(f"{row['rater_id']} (line {row_number})")

        experience_with_mdd = row.get("experience_with_mdd", "").strip()
        if not experience_with_mdd:
            invalid_refs["experience_with_mdd"].append(f"{row['rater_id']} (line {row_number})")

    for field_name, refs in sorted(invalid_refs.items()):
        findings.append(
            make_finding(
                area="data",
                severity="major",
                repo_root=repo_root,
                path=raters_path,
                check_id="unexpected_rater_metadata_format",
                message=f"Pole `{field_name}` má neočakávaný formát v `raters_clean.csv`.",
                evidence_refs=refs[:8],
                suggested_fix="Drž stabilný coding pre rater metadata; `years_practice` má byť číslo alebo pásmo typu `16_plus` a `experience_with_mdd` nemá byť prázdne.",
            )
        )

    return findings


def check_raw_validation_csv_shape(repo_root: Path, path: Path, run_mode: RunMode) -> list[Finding]:
    if not path.exists():
        return []

    header, row_lengths = read_csv_field_lengths(path)
    if not header:
        return [
            make_finding(
                area="data",
                severity="major" if run_mode != "smoke" else "info",
                repo_root=repo_root,
                path=path,
                check_id="validation_csv_empty_or_missing_header",
                message="Raw validačný `data.csv` nemá čitateľnú hlavičku.",
                suggested_fix="Obnov export validačného CSV alebo ho znovu vygeneruj z workbooku s korektnou hlavičkou.",
            )
        ]

    expected_length = len(header)
    bad_rows = [f"line {line_number}: {length} fields" for line_number, length in row_lengths if length != expected_length]
    if not bad_rows:
        return []

    severity = "info" if run_mode == "smoke" else "major"
    return [
        make_finding(
            area="data",
            severity=severity,
            repo_root=repo_root,
            path=path,
            check_id="validation_csv_row_length_mismatch",
            message=(
                f"Raw validačný `data.csv` má riadky s iným počtom polí než hlavička ({expected_length})."
            ),
            evidence_refs=bad_rows[:8],
            suggested_fix="Spusť `python3 analysis/scripts/repair_validation_csv.py` alebo znovu vyexportuj `data.csv` z workbooku; source of truth ostáva `analysis/validity data/data.xlsx`.",
        )
    ]


def check_transcript_level_reporting_units(
    *,
    repo_root: Path,
    descriptives_items_path: Path,
    descriptives_items: list[dict[str, str]],
    descriptives_composites_path: Path,
    descriptives_composites: list[dict[str, str]],
) -> list[Finding]:
    findings: list[Finding] = []

    item_header = set(descriptives_items[0].keys()) if descriptives_items else set(read_csv_header(descriptives_items_path))
    composite_header = (
        set(descriptives_composites[0].keys())
        if descriptives_composites
        else set(read_csv_header(descriptives_composites_path))
    )

    if "analysis_unit" not in item_header:
        findings.append(
            make_finding(
                area="stats",
                severity="blocker",
                repo_root=repo_root,
                path=descriptives_items_path,
                check_id="missing_analysis_unit_column",
                message="`descriptives_items.csv` nemá stĺpec `analysis_unit`, takže nejde overiť jednotka analýzy pre A1-A9.",
                suggested_fix="Rozšír pipeline export tak, aby `descriptives_items.csv` explicitne niesol `analysis_unit`.",
            )
        )
        return findings

    if "analysis_unit" not in composite_header:
        findings.append(
            make_finding(
                area="stats",
                severity="blocker",
                repo_root=repo_root,
                path=descriptives_composites_path,
                check_id="missing_analysis_unit_column",
                message="`descriptives_composites.csv` nemá stĺpec `analysis_unit`, takže nejde overiť jednotka analýzy pre error vetvu.",
                suggested_fix="Rozšír pipeline export tak, aby `descriptives_composites.csv` explicitne niesol `analysis_unit`.",
            )
        )
        return findings

    items_by_variable = {row.get("variable", ""): row for row in descriptives_items}
    for variable in (f"a{idx}" for idx in range(1, 10)):
        row = items_by_variable.get(variable)
        if row is None:
            findings.append(
                make_finding(
                    area="stats",
                    severity="blocker",
                    repo_root=repo_root,
                    path=descriptives_items_path,
                    check_id="missing_transcript_level_item_row",
                    message=f"V `descriptives_items.csv` chýba riadok pre `{variable}`.",
                    suggested_fix="Znovu exportuj item descriptives tak, aby obsahovali aj transcript-level A1-A9 vetvu.",
                )
            )
            continue
        if row.get("analysis_unit") != "transcript":
            findings.append(
                make_finding(
                    area="stats",
                    severity="blocker",
                    repo_root=repo_root,
                    path=descriptives_items_path,
                    check_id="wrong_transcript_level_item_unit",
                    message=f"`{variable}` je v `descriptives_items.csv` reportované inou jednotkou než `transcript`.",
                    evidence_refs=[f"analysis_unit={row.get('analysis_unit', '')}"],
                    suggested_fix="A1-A9 reportuj po agregácii na 1 riadok = 1 transkript, nie rating-weighted cez long dáta.",
                )
            )

    composites_by_variable = {row.get("variable", ""): row for row in descriptives_composites}
    for variable in ("symptom_error_mean", "severity_error", "impact_error"):
        row = composites_by_variable.get(variable)
        if row is None:
            continue
        if row.get("analysis_unit") != "transcript":
            findings.append(
                make_finding(
                    area="stats",
                    severity="blocker",
                    repo_root=repo_root,
                    path=descriptives_composites_path,
                    check_id="wrong_transcript_level_composite_unit",
                    message=f"`{variable}` je v `descriptives_composites.csv` reportované inou jednotkou než `transcript`.",
                    evidence_refs=[f"analysis_unit={row.get('analysis_unit', '')}"],
                    suggested_fix="Anchor-fidelity error ukazovatele reportuj na transcript-level summary, nie rating-weighted cez opakované rater riadky.",
                )
            )

    return findings


def check_transcript_level_summary_projection(
    *,
    repo_root: Path,
    transcript_level_summary_path: Path,
    transcript_level_summary: list[dict[str, str]],
    analysis_long_path: Path,
    analysis_long: list[dict[str, str]],
) -> list[Finding]:
    findings: list[Finding] = []
    if not transcript_level_summary:
        findings.append(
            make_finding(
                area="stats",
                severity="blocker",
                repo_root=repo_root,
                path=transcript_level_summary_path,
                check_id="empty_transcript_level_summary",
                message="`transcript_level_summary.csv` je prázdny alebo sa nepodarilo načítať.",
                suggested_fix="Znovu spusti pipeline a over export transcript-level summary.",
            )
        )
        return findings

    duplicate_transcripts = duplicate_value_refs(transcript_level_summary, "transcript_id")
    if duplicate_transcripts:
        findings.append(
            make_finding(
                area="stats",
                severity="blocker",
                repo_root=repo_root,
                path=transcript_level_summary_path,
                check_id="duplicate_transcript_level_rows",
                message="`transcript_level_summary.csv` nemá unikátne `transcript_id`.",
                evidence_refs=sorted(duplicate_transcripts)[:8],
                suggested_fix="Zosúlaď transcript-level agregáciu tak, aby každému transkriptu zodpovedal presne jeden riadok.",
            )
        )

    expected_counts = Counter(row["transcript_id"] for row in analysis_long)
    summary_transcripts = {row["transcript_id"] for row in transcript_level_summary}
    missing_transcripts = sorted(set(expected_counts) - summary_transcripts)
    extra_transcripts = sorted(summary_transcripts - set(expected_counts))

    if missing_transcripts:
        findings.append(
            make_finding(
                area="stats",
                severity="blocker",
                repo_root=repo_root,
                path=transcript_level_summary_path,
                check_id="missing_transcripts_in_summary",
                message="`transcript_level_summary.csv` nepokrýva všetky transkripty z `analysis_long.csv`.",
                evidence_refs=missing_transcripts[:8],
                suggested_fix="Znovu exportuj transcript-level summary tak, aby obsahoval všetky unikátne transkripty z analytického long datasetu.",
            )
        )

    if extra_transcripts:
        findings.append(
            make_finding(
                area="stats",
                severity="blocker",
                repo_root=repo_root,
                path=transcript_level_summary_path,
                check_id="extra_transcripts_in_summary",
                message="`transcript_level_summary.csv` obsahuje transkripty, ktoré nie sú v `analysis_long.csv`.",
                evidence_refs=extra_transcripts[:8],
                suggested_fix="Skontroluj transcript-level join a odstráň riadky, ktoré nepatria do aktuálneho analytického datasetu.",
            )
        )

    for row in transcript_level_summary:
        transcript_id = row["transcript_id"]
        expected_n = expected_counts.get(transcript_id)
        actual_n = normalize_scalar(row.get("n_ratings"))
        if expected_n is not None and actual_n != expected_n:
            findings.append(
                make_finding(
                    area="stats",
                    severity="blocker",
                    repo_root=repo_root,
                    path=transcript_level_summary_path,
                    check_id="transcript_level_n_ratings_mismatch",
                    message=f"Transcript `{transcript_id}` má v `transcript_level_summary.csv` nesprávne `n_ratings`.",
                    evidence_refs=[f"expected={expected_n}", f"actual={row.get('n_ratings', '')}"],
                    suggested_fix="Odvádzaj `n_ratings` v transcript-level summary priamo z počtu rating riadkov v `analysis_long.csv`.",
                )
            )

    return findings


def check_unique_field(repo_root: Path, path: Path, rows: list[dict[str, str]], field_name: str) -> list[Finding]:
    duplicates = duplicate_value_refs(rows, field_name)
    if not duplicates:
        return []
    return [
        make_finding(
            area="data",
            severity="blocker",
            repo_root=repo_root,
            path=path,
            check_id="duplicate_unique_identifier",
            message=f"Pole `{field_name}` nie je unikátne: {', '.join(sorted(duplicates)[:5])}.",
            suggested_fix=f"Odstráň duplicity v `{relative_path(repo_root, path)}` tak, aby `{field_name}` bolo unikátne.",
        )
    ]


def compare_row_sets(
    repo_root: Path,
    expected_rows: list[dict[str, str]],
    actual_rows: list[dict[str, str]],
    expected_label: str,
    actual_path: Path,
    key_fields: tuple[str, ...],
    check_id: str,
    area: str,
    suggested_fix: str,
) -> list[Finding]:
    findings: list[Finding] = []
    expected_map = {make_row_key(row, key_fields): row for row in expected_rows}
    actual_map = {make_row_key(row, key_fields): row for row in actual_rows}

    missing_keys = sorted(set(expected_map) - set(actual_map))
    extra_keys = sorted(set(actual_map) - set(expected_map))

    if missing_keys:
        findings.append(
            make_finding(
                area=area,  # type: ignore[arg-type]
                severity="blocker",
                repo_root=repo_root,
                path=actual_path,
                check_id=check_id,
                message=f"V `{relative_path(repo_root, actual_path)}` chýbajú riadky oproti `{expected_label}`.",
                evidence_refs=[format_row_key(key_fields, key) for key in missing_keys[:8]],
                suggested_fix=suggested_fix,
            )
        )

    if extra_keys:
        findings.append(
            make_finding(
                area=area,  # type: ignore[arg-type]
                severity="blocker",
                repo_root=repo_root,
                path=actual_path,
                check_id=check_id,
                message=f"V `{relative_path(repo_root, actual_path)}` sú nadbytočné riadky oproti `{expected_label}`.",
                evidence_refs=[format_row_key(key_fields, key) for key in extra_keys[:8]],
                suggested_fix=suggested_fix,
            )
        )

    shared_keys = sorted(set(expected_map) & set(actual_map))
    for key in shared_keys:
        expected = expected_map[key]
        actual = actual_map[key]
        all_columns = sorted(set(expected) | set(actual))
        mismatches: list[str] = []
        for column in all_columns:
            if not values_equal(expected.get(column), actual.get(column)):
                mismatches.append(
                    f"{column}: expected `{expected.get(column)}`, actual `{actual.get(column)}`"
                )
        if mismatches:
            findings.append(
                make_finding(
                    area=area,  # type: ignore[arg-type]
                    severity="blocker",
                    repo_root=repo_root,
                    path=actual_path,
                    check_id=check_id,
                    message=(
                        f"Riadok `{format_row_key(key_fields, key)}` v `{relative_path(repo_root, actual_path)}` "
                        f"nesedí s `{expected_label}`."
                    ),
                    evidence_refs=mismatches[:8],
                    suggested_fix=suggested_fix,
                )
            )

    return findings


def collect_skipped_outcome_refs(repo_root: Path) -> list[str]:
    refs: list[str] = []
    status_files = [
        repo_root / "analysis" / "outputs" / "icc_summary.csv",
        repo_root / "analysis" / "outputs" / "lmm_core_models.csv",
        repo_root / "analysis" / "outputs" / "clmm_item_models.csv",
    ]

    for path in status_files:
        if not path.exists():
            continue
        for row in read_csv_rows(path):
            if row.get("status") == "skipped":
                refs.append(f"{relative_path(repo_root, path)}:{row.get('outcome', 'unknown')}")

    return refs


def read_csv_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        return next(reader, [])


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [dict(row) for row in reader]


def read_csv_field_lengths(path: Path) -> tuple[list[str], list[tuple[int, int]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, [])
        row_lengths = [(line_number, len(row)) for line_number, row in enumerate(reader, start=2)]
    return header, row_lengths


def parse_bib_keys(text: str) -> set[str]:
    return {match.group(1).strip() for match in BIB_KEY_PATTERN.finditer(text)}


def duplicate_value_refs(rows: list[dict[str, str]], field_name: str) -> set[str]:
    counts = Counter(row[field_name] for row in rows)
    return {value for value, count in counts.items() if count > 1}


def duplicate_key_refs(rows: list[dict[str, str]], fields: tuple[str, ...]) -> set[str]:
    counter = Counter(tuple(row[field] for field in fields) for row in rows)
    return {" / ".join(key) for key, count in counter.items() if count > 1}


def expected_variant_id(guardrail: str, profile: str) -> str:
    return f"G{guardrail}_{profile}"


def index_by(rows: list[dict[str, str]], field_name: str) -> dict[str, dict[str, str]]:
    return {row[field_name]: row for row in rows}


def integer_in_range(raw_value: str | None, minimum: int, maximum: int) -> bool:
    value = normalize_scalar(raw_value)
    return isinstance(value, int) and minimum <= value <= maximum


def normalize_scalar(raw_value: str | int | float | None) -> str | int | float | None:
    if raw_value is None:
        return None
    if isinstance(raw_value, (int, float)):
        return raw_value
    value = str(raw_value).strip()
    if value == "" or value.upper() == "NA":
        return None
    if value in {"Inf", "+Inf", "Infinity"}:
        return math.inf
    if value in {"-Inf", "-Infinity"}:
        return -math.inf
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?(?:\d+\.\d*|\d*\.\d+)(?:[eE][+-]?\d+)?", value):
        return float(value)
    return value


def values_equal(expected: str | None, actual: str | None, tolerance: float = 1e-9) -> bool:
    left = normalize_scalar(expected)
    right = normalize_scalar(actual)

    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        if math.isinf(left) or math.isinf(right):
            return left == right
        return abs(float(left) - float(right)) <= tolerance
    return left == right


def make_row_key(row: dict[str, str], key_fields: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(str(row.get(field, "")) for field in key_fields)


def format_row_key(key_fields: tuple[str, ...], key: tuple[str, ...]) -> str:
    return ", ".join(f"{field}={value}" for field, value in zip(key_fields, key, strict=True))


def compact_number(value: float) -> str:
    if math.isclose(value, int(value), rel_tol=0.0, abs_tol=1e-12):
        return str(int(value))
    return f"{value:.12g}"


def guardrail_label(raw_value: str) -> str:
    return {"0": "off", "1": "on"}.get(raw_value, raw_value)


def severity_for_source_mode(run_mode: RunMode, source_mode: str) -> str | None:
    if source_mode == "data_clean":
        return None
    if run_mode == "final_results":
        return "blocker"
    if run_mode == "pre_word":
        return "major"
    return "info"


def relative_path(repo_root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def make_finding(
    area: str,
    severity: str,
    repo_root: Path,
    path: Path,
    check_id: str,
    message: str,
    evidence_refs: list[str] | None = None,
    suggested_fix: str | None = None,
) -> Finding:
    return Finding(
        area=area,  # type: ignore[arg-type]
        severity=severity,  # type: ignore[arg-type]
        file=relative_path(repo_root, path),
        check_id=check_id,
        message=message,
        evidence_refs=evidence_refs or [],
        suggested_fix=suggested_fix,
    )


def collect_preview_meta_findings(
    *,
    repo_root: Path,
    path: Path,
    severity: str,
    lines: list[str],
) -> list[Finding]:
    findings: list[Finding] = []
    for check_id, pattern in PREVIEW_META_PATTERNS.items():
        refs = [
            f"line {line_number}"
            for line_number, line in enumerate(lines, start=1)
            if line.strip()
            and not line.lstrip().startswith("![")
            and pattern.search(line)
        ]
        if refs:
            findings.append(
                make_finding(
                    area="presentation",
                    severity=severity,
                    repo_root=repo_root,
                    path=path,
                    check_id=check_id,
                    message="Preview vrstva stále obsahuje interný workflow/meta jazyk namiesto neutrálneho akademického textu.",
                    evidence_refs=refs[:8],
                    suggested_fix="Odstráň z preview Results/Discussion a vložených fragmentov slová typu `preview`, `pipeline`, `clean run` a podobné workflow poznámky.",
                )
            )
    return findings
