#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import shutil
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_CLEAN_DIR = REPO_ROOT / "analysis" / "data_clean"
CANONICAL_SEEDS_PATH = REPO_ROOT / "analysis" / "seed_anchors_final.csv"


PHQ9_TO_A = {
    "A1": "phq9_depressed_mood_score",
    "A2": "phq9_anhedonia_score",
    "A3": "phq9_sleep_disturbance_score",
    "A4": "phq9_appetite_change_score",
    "A5": "phq9_psychomotor_change_score",
    "A6": "phq9_fatigue_score",
    "A7": "phq9_worthlessness_or_guilt_score",
    "A8": "phq9_concentration_difficulty_score",
    "A9": "phq9_self_harm_thoughts_score",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert the current wide rating export into analysis/data_clean/*.csv."
    )
    parser.add_argument(
        "--source",
        default=str(Path.home() / "Downloads" / "mdd-ai-simulation_ratings_wide (4).csv"),
        help="Path to the wide rating CSV export.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def normalize_guardrail(value: str) -> str:
    mapping = {"off": "0", "on": "1", "0": "0", "1": "1"}
    normalized = mapping.get((value or "").strip().lower())
    if normalized is None:
        raise ValueError(f"Unexpected guardrail value: {value!r}")
    return normalized


def normalize_profile(value: str) -> str:
    profile = (value or "").strip().upper()
    if profile not in {"R1", "R2", "R3"}:
        raise ValueError(f"Unexpected profile value: {value!r}")
    return profile


def build_variant_id(guardrail: str, profile: str) -> str:
    return f"G{guardrail}_{profile}"


def numeric_text(value: str) -> str:
    value = (value or "").strip()
    if value == "":
        return ""
    return str(int(float(value)))


def combine_comment(row: dict[str, str]) -> str:
    least_convincing = (row.get("interview-rating_v1__O1_least_convincing") or "").strip()
    missing_or_exaggerated = (row.get("interview-rating_v1__O2_missing_or_exaggerated") or "").strip()
    parts: list[str] = []
    if least_convincing:
        parts.append(f"least_convincing: {least_convincing}")
    if missing_or_exaggerated:
        parts.append(f"missing_or_exaggerated: {missing_or_exaggerated}")
    return " | ".join(parts)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_ratings_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    ratings_rows: list[dict[str, str]] = []

    for row in rows:
        guardrail = normalize_guardrail(row["iv_prompt_guardrail_mode"])
        profile = normalize_profile(row["iv_realization_profile"])
        variant_id = (row.get("iv_variant_id") or "").strip() or build_variant_id(guardrail, profile)
        expected_variant_id = build_variant_id(guardrail, profile)
        if variant_id != expected_variant_id:
            raise ValueError(
                f"Variant mismatch for transcript {row['transcript_stable_id']}: "
                f"{variant_id!r} != {expected_variant_id!r}"
            )

        rating_row = {
            "record_id": numeric_text(row["assignment_id"]),
            "rater_id": (row["assignee_code"] or "").strip(),
            "transcript_id": (row["transcript_stable_id"] or "").strip(),
            "seed_id": (row["seed"] or row["scenario_code"] or "").strip(),
            "guardrail": guardrail,
            "profile": profile,
            "variant_id": variant_id,
            "backend_model": f"{(row.get('chat_lab_backend') or '').strip()}|{(row.get('chat_lab_model') or '').strip()}".strip("|"),
            "target_turns": numeric_text(row.get("iv_target_turns", "")),
            "actual_turns": numeric_text(row.get("turn_count", "")),
            "rating_duration_sec": numeric_text(row.get("assignment_duration_seconds", "")),
            "G1": numeric_text(row.get("interview-rating_v1__G1_clinical_credibility", "")),
            "G2": numeric_text(row.get("interview-rating_v1__G2_natural_language", "")),
            "G3": numeric_text(row.get("interview-rating_v1__G3_internal_consistency", "")),
            "G4": numeric_text(row.get("interview-rating_v1__G4_depression_fit", "")),
            "G5": numeric_text(row.get("interview-rating_v1__G5_methodological_utility", "")),
            "S1": numeric_text(row.get("interview-rating_v1__S1_symptom_severity", "")),
            "S2": numeric_text(row.get("interview-rating_v1__S2_functional_impact", "")),
            "R1": numeric_text(row.get("interview-rating_v1__R1_contradictions", "")),
            "R2": numeric_text(row.get("interview-rating_v1__R2_cliche_template", "")),
            "R3": numeric_text(row.get("interview-rating_v1__R3_context_symptom_mismatch", "")),
            "R4": numeric_text(row.get("interview-rating_v1__R4_other_primary_psychopathology", "")),
            "R5": numeric_text(row.get("interview-rating_v1__R5_excessive_dramatization", "")),
            "guessed_origin": (row.get("interview-rating_v1__P1_perceived_origin") or "").strip(),
            "guess_confidence": numeric_text(row.get("interview-rating_v1__P2_origin_confidence", "")),
            "comment": combine_comment(row),
        }

        for a_label, source_field in PHQ9_TO_A.items():
            rating_row[a_label] = numeric_text(row.get(source_field, ""))

        ratings_rows.append(rating_row)

    ratings_rows.sort(key=lambda item: int(item["record_id"]))
    return ratings_rows


def build_transcript_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["transcript_stable_id"] or "").strip()].append(row)

    transcript_rows: list[dict[str, str]] = []
    for transcript_id, group_rows in sorted(grouped.items()):
        base = group_rows[0]
        guardrail = normalize_guardrail(base["iv_prompt_guardrail_mode"])
        profile = normalize_profile(base["iv_realization_profile"])
        variant_id = (base.get("iv_variant_id") or "").strip() or build_variant_id(guardrail, profile)
        actual_turns = {numeric_text(item.get("turn_count", "")) for item in group_rows}
        generation_dates = {(item.get("generation_date") or "").strip() for item in group_rows}

        if len(actual_turns) != 1:
            raise ValueError(f"Transcript {transcript_id} has inconsistent turn counts: {sorted(actual_turns)}")
        if len(generation_dates) != 1:
            raise ValueError(f"Transcript {transcript_id} has inconsistent generation dates: {sorted(generation_dates)}")

        transcript_rows.append(
            {
                "transcript_id": transcript_id,
                "seed_id": (base.get("seed") or base.get("scenario_code") or "").strip(),
                "guardrail": guardrail,
                "profile": profile,
                "variant_id": variant_id,
                "backend_model": f"{(base.get('chat_lab_backend') or '').strip()}|{(base.get('chat_lab_model') or '').strip()}".strip("|"),
                "target_turns": numeric_text(base.get("iv_target_turns", "")),
                "actual_turns": actual_turns.pop(),
                "chat_variability": (base.get("chat_lab_variability_level") or "").strip(),
                "created_at": generation_dates.pop(),
                "transcript_path": f"transcripts/current_export/{transcript_id}.txt",
            }
        )

    return transcript_rows


def build_rater_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, set[tuple[str, ...]]] = defaultdict(set)
    coverage = Counter()

    for row in rows:
        rater_id = (row["assignee_code"] or "").strip()
        grouped[rater_id].add(
            (
                (row.get("rater_profession") or "").strip(),
                (row.get("rater_specialization") or "").strip(),
                (row.get("rater_years_practice") or "").strip(),
                (row.get("rater_depression_contact") or "").strip(),
                (row.get("rater_interview_experience") or "").strip(),
                (row.get("rater_ai_experience") or "").strip(),
                (row.get("rater_confidence_mdd") or "").strip(),
            )
        )
        coverage[rater_id] += 1

    rater_rows: list[dict[str, str]] = []
    for rater_id in sorted(grouped, key=lambda value: int(value)):
        meta_values = grouped[rater_id]
        if len(meta_values) != 1:
            raise ValueError(f"Rater {rater_id} has inconsistent metadata: {meta_values}")
        profession, specialization, years_practice, experience_with_mdd, interview_experience, ai_experience, confidence_mdd = next(iter(meta_values))
        rater_rows.append(
            {
                "rater_id": rater_id,
                "profession": profession,
                "specialization": specialization,
                "years_practice": years_practice,
                "experience_with_mdd": experience_with_mdd,
                "notes": (
                    f"interview_experience={interview_experience}; "
                    f"ai_experience={ai_experience}; "
                    f"confidence_mdd={confidence_mdd}; "
                    f"n_ratings={coverage[rater_id]}"
                ),
            }
        )

    return rater_rows


def validate_invariance(ratings_rows: list[dict[str, str]]) -> None:
    by_transcript: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for row in ratings_rows:
        for field in PHQ9_TO_A:
            by_transcript[row["transcript_id"]][field].add(row[field])

    inconsistent: list[str] = []
    for transcript_id, field_map in by_transcript.items():
        drift = {field: values for field, values in field_map.items() if len(values) > 1}
        if drift:
            inconsistent.append(f"{transcript_id}: {drift}")

    if inconsistent:
        raise ValueError("A1-A9 are not transcript-invariant:\n" + "\n".join(inconsistent))


def main() -> None:
    args = parse_args()
    source_path = Path(args.source).expanduser().resolve()
    if not source_path.exists():
        raise FileNotFoundError(f"Wide export not found: {source_path}")
    if not CANONICAL_SEEDS_PATH.exists():
        raise FileNotFoundError(f"Canonical seed anchors not found: {CANONICAL_SEEDS_PATH}")

    rows = read_rows(source_path)
    ensure_directory(DATA_CLEAN_DIR)

    ratings_rows = build_ratings_rows(rows)
    validate_invariance(ratings_rows)
    transcript_rows = build_transcript_rows(rows)
    rater_rows = build_rater_rows(rows)

    ratings_fieldnames = [
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
    ]
    transcript_fieldnames = [
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
    ]
    rater_fieldnames = [
        "rater_id",
        "profession",
        "specialization",
        "years_practice",
        "experience_with_mdd",
        "notes",
    ]

    write_csv(DATA_CLEAN_DIR / "ratings_clean.csv", ratings_fieldnames, ratings_rows)
    write_csv(DATA_CLEAN_DIR / "transcripts_master.csv", transcript_fieldnames, transcript_rows)
    write_csv(DATA_CLEAN_DIR / "raters_clean.csv", rater_fieldnames, rater_rows)
    shutil.copyfile(CANONICAL_SEEDS_PATH, DATA_CLEAN_DIR / "seed_anchors_final.csv")

    cell_counts = Counter((row["guardrail"], row["profile"]) for row in ratings_rows)
    print(f"Source: {source_path}")
    print(f"ratings_clean.csv: {len(ratings_rows)} rows")
    print(f"transcripts_master.csv: {len(transcript_rows)} rows")
    print(f"raters_clean.csv: {len(rater_rows)} rows")
    print("guardrail_profile_counts:")
    for (guardrail, profile), count in sorted(cell_counts.items()):
        print(f"  G{guardrail}-{profile}: {count}")


if __name__ == "__main__":
    main()
