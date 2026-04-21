from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

from qc_hard_checks import (
    CITEKEY_PATTERN,
    PLACEHOLDER_PATTERN,
    collect_skipped_outcome_refs,
    read_csv_rows,
    relative_path,
)
from qc_models import AgentMode, AgentResult, CheckResult, Finding, RunMode


@dataclass(slots=True)
class AgentTask:
    agent_name: str
    prompt_path: Path
    input_refs: list[Path]
    user_input: str


def run_agent_reviews(
    repo_root: Path,
    run_mode: RunMode,
    agent_mode: AgentMode,
    hard_checks: list[CheckResult],
    agent_model: str | None = None,
    agent_reasoning_effort: str | None = None,
) -> list[AgentResult]:
    if agent_mode == "off":
        return []

    if any(check.status == "BLOCK" for check in hard_checks):
        return [
            AgentResult(
                agent_name=name,
                backend=agent_mode,
                decision="SKIP",
                confidence=1.0,
                summary="Skipped because deterministic hard QC already returned a blocker.",
                prompt_file=None,
                input_refs=[],
            )
            for name in (
                "citation_support_agent",
                "stats_claim_agent",
                "results_presentation_agent",
            )
        ]

    tasks = build_agent_tasks(repo_root, run_mode)

    if agent_mode == "mock":
        return [run_mock_agent(task, repo_root=repo_root, run_mode=run_mode, hard_checks=hard_checks) for task in tasks]

    return [
        run_pydantic_ai_agent(
            task,
            repo_root=repo_root,
            run_mode=run_mode,
            agent_model=agent_model,
            agent_reasoning_effort=agent_reasoning_effort,
        )
        for task in tasks
    ]


def build_agent_tasks(repo_root: Path, run_mode: RunMode) -> list[AgentTask]:
    results_path = repo_root / "manuscript" / "40_results.md"
    method_path = repo_root / "manuscript" / "30_method.md"
    preview_results_path = repo_root / "manuscript" / "40_results_preview_current_export.md"
    preview_discussion_path = repo_root / "manuscript" / "50_discussion_preview_current_export.md"
    preview_tables_dir = repo_root / "tables" / "current_export_preview"
    preview_table_4_path = preview_tables_dir / "table_4_internal_consistency.md"
    preview_table_5_path = preview_tables_dir / "table_5_pair_agreement.md"
    preview_table_6_path = preview_tables_dir / "table_6_cell_descriptives.md"
    preview_table_7a_path = preview_tables_dir / "table_7a_model_summary_rating.md"
    preview_table_7b_path = preview_tables_dir / "table_7b_model_summary_transcript.md"
    preview_table_10_path = preview_tables_dir / "table_10_anchored_subset.md"
    icc_path = repo_root / "analysis" / "outputs" / "icc_summary.csv"
    lmm_path = repo_root / "analysis" / "outputs" / "lmm_core_models.csv"
    clmm_path = repo_root / "analysis" / "outputs" / "clmm_item_models.csv"
    table_4_path = repo_root / "tables" / "table_4_internal_consistency.csv"
    table_5_path = repo_root / "tables" / "table_5_icc.csv"
    table_6_path = repo_root / "tables" / "table_6_mixed_models_core.csv"
    bib_path = repo_root / "references" / "zotero-thesis.bib"

    results_text = safe_read_text(results_path)
    method_text = safe_read_text(method_path)
    preview_results_text = safe_read_text(preview_results_path)
    preview_discussion_text = safe_read_text(preview_discussion_path)
    preview_rendered_results_text = render_current_export_preview_results(repo_root)
    preview_table_4 = safe_read_text(preview_table_4_path)
    preview_table_5 = safe_read_text(preview_table_5_path)
    preview_table_6 = safe_read_text(preview_table_6_path)
    preview_table_7a = safe_read_text(preview_table_7a_path)
    preview_table_7b = safe_read_text(preview_table_7b_path)
    preview_table_10 = safe_read_text(preview_table_10_path)
    icc_rows = read_csv_preview(icc_path)
    lmm_rows = read_csv_preview(lmm_path)
    clmm_rows = read_csv_preview(clmm_path)
    table_4_rows = read_csv_preview(table_4_path)
    table_5_rows = read_csv_preview(table_5_path)
    table_6_rows = read_csv_preview(table_6_path)
    citekeys = sorted({match.group(1) for match in CITEKEY_PATTERN.finditer(results_text)})
    results_excerpt = trim_text(results_text, 20000)
    preview_results_excerpt = trim_text(preview_results_text, 16000)
    preview_discussion_excerpt = trim_text(preview_discussion_text, 10000)
    preview_rendered_results_excerpt = trim_text(preview_rendered_results_text, 20000)

    tasks: list[AgentTask] = [
        AgentTask(
            agent_name="citation_support_agent",
            prompt_path=repo_root / "prompts" / "qc" / "citation_support.md",
            input_refs=[results_path, method_path, bib_path],
            user_input=(
                f"RUN MODE: {run_mode}\n\n"
                "RESULTS EXCERPT:\n"
                f"{results_excerpt}\n\n"
                "METHOD EXCERPT:\n"
                f"{trim_text(method_text, 5000)}\n\n"
                f"CITEKEYS IN RESULTS: {', '.join(f'@{key}' for key in citekeys) if citekeys else '(none found)'}\n"
                "Review whether the Results section keeps claims aligned with its local citation support. "
                "Do not invent external sources.\n"
            ),
        ),
        AgentTask(
            agent_name="stats_claim_agent",
            prompt_path=repo_root / "prompts" / "qc" / "stats_claim.md",
            input_refs=[results_path, method_path, icc_path, lmm_path, clmm_path, table_5_path, table_6_path],
            user_input=(
                f"RUN MODE: {run_mode}\n\n"
                "RESULTS EXCERPT:\n"
                f"{results_excerpt}\n\n"
                "VARIABLE ALIAS MAP FOR MANUSCRIPT WORDING:\n"
                "- `plausibility_index` = index klinickej vierohodnosti\n"
                "- `defect_index` = index defektov\n"
                "- `S1` / `s1` = expertne hodnotená závažnosť\n"
                "- `S2` / `s2` = expertne hodnotený funkčný dopad\n"
                "- `severity_error` = chyba odhadu závažnosti voči `S1_anchor`\n"
                "- `impact_error` = chyba odhadu funkčného dopadu voči `S2_anchor`\n\n"
                "METHOD EXCERPT:\n"
                f"{trim_text(method_text, 6000)}\n\n"
                "ICC SUMMARY CSV:\n"
                f"{icc_rows}\n\n"
                "LMM CORE MODELS CSV:\n"
                f"{lmm_rows}\n\n"
                "CLMM ITEM MODELS CSV:\n"
                f"{clmm_rows}\n\n"
                "TABLE 5 CSV:\n"
                f"{table_5_rows}\n\n"
                "TABLE 6 CSV:\n"
                f"{table_6_rows}\n\n"
                "Review whether textual claims about Results match the provided output artifacts. "
                "Treat `status=skipped` as not reportable in final inferential prose.\n"
            ),
        ),
        AgentTask(
            agent_name="results_presentation_agent",
            prompt_path=repo_root / "prompts" / "qc" / "results_presentation.md",
            input_refs=[
                preview_results_path,
                preview_discussion_path,
                preview_tables_dir / "fragment_validation.md",
                preview_tables_dir / "fragment_dataset.md",
                preview_tables_dir / "fragment_descriptives.md",
                preview_tables_dir / "fragment_measurement.md",
                preview_tables_dir / "fragment_cells.md",
                preview_tables_dir / "fragment_models.md",
                preview_tables_dir / "fragment_exploratory.md",
                preview_tables_dir / "fragment_anchored.md",
                preview_table_4_path,
                preview_table_5_path,
                preview_table_6_path,
                preview_table_7a_path,
                preview_table_7b_path,
                preview_table_10_path,
                results_path,
            ],
            user_input=(
                f"RUN MODE: {run_mode}\n\n"
                "PRIMARY RESULTS EXCERPT FOR PRESENTATION REVIEW:\n"
                f"{preview_rendered_results_excerpt or results_excerpt}\n\n"
                "DISCUSSION EXCERPT FOR BOUNDARY CHECK:\n"
                f"{preview_discussion_excerpt or '(preview discussion file missing)'}\n\n"
                "SUPPORTING TABLE: INTERNAL CONSISTENCY\n"
                f"{trim_text(preview_table_4, 5000) or '(internal consistency table missing)'}\n\n"
                "SUPPORTING TABLE: PAIR AGREEMENT\n"
                f"{trim_text(preview_table_5, 5000) or '(pair agreement table missing)'}\n\n"
                "SUPPORTING TABLE: CELL DESCRIPTIVES\n"
                f"{trim_text(preview_table_6, 7000) or '(cell descriptives table missing)'}\n\n"
                "SUPPORTING TABLE: MODEL SUMMARY (RATING LEVEL)\n"
                f"{trim_text(preview_table_7a, 5000) or '(rating-level model summary missing)'}\n\n"
                "SUPPORTING TABLE: MODEL SUMMARY (TRANSCRIPT LEVEL)\n"
                f"{trim_text(preview_table_7b, 4000) or '(transcript-level model summary missing)'}\n\n"
                "SUPPORTING TABLE: ANCHOR DEVIATIONS\n"
                f"{trim_text(preview_table_10, 5000) or '(anchor-deviation table missing)'}\n\n"
                "Review whether the Results draft is readable, non-redundant and aligned with IMRaD/result-reporting expectations. "
                "Focus on presentation issues, not recomputing statistics. "
                "If current-export preview files exist, explicitly flag local filesystem paths, workflow/meta language "
                "(`preview`, `pipeline`, `clean run`, `autoritatívny output`) and any unit-of-analysis confusion "
                "between 166 rating rows and 72 transcript-level anchor summaries.\n"
            ),
        ),
    ]
    return tasks


def run_mock_agent(
    task: AgentTask,
    *,
    repo_root: Path,
    run_mode: RunMode,
    hard_checks: list[CheckResult],
) -> AgentResult:
    findings: list[Finding] = []
    decision = "PASS"
    summary = "Mock backend inspected the prepared context and found no additional findings beyond deterministic hard QC."

    if task.agent_name == "stats_claim_agent":
        skipped_refs = collect_skipped_outcome_refs(repo_root)
        if run_mode in {"pre_word", "final_results"} and skipped_refs:
            decision = "REVISE"
            summary = (
                "Mock backend mirrors the deterministic gate: core outputs still contain skipped inferential rows, "
                "so claim-level review should stay in revise mode."
            )
    elif task.agent_name == "results_presentation_agent":
        results_text = safe_read_text(repo_root / "manuscript" / "40_results.md")
        has_placeholders = bool(PLACEHOLDER_PATTERN.search(results_text))
        if run_mode in {"pre_word", "final_results"} and has_placeholders:
            decision = "REVISE"
            summary = (
                "Mock backend mirrors the deterministic gate: Results still contains placeholders, "
                "so presentation review remains in revise mode."
            )
    elif task.agent_name == "citation_support_agent":
        citation_findings = [
            finding
            for check in hard_checks
            if check.name == "citation_registry_qc"
            for finding in check.findings
        ]
        if citation_findings:
            decision = "REVISE"
            summary = "Mock backend observed unresolved citation-registry findings."

    return AgentResult(
        agent_name=task.agent_name,
        backend="mock",
        decision=decision,  # type: ignore[arg-type]
        confidence=0.35,
        summary=summary,
        findings=findings,
        prompt_file=relative_path(repo_root, task.prompt_path),
        input_refs=[relative_path(repo_root, path) for path in task.input_refs],
    )


def run_pydantic_ai_agent(
    task: AgentTask,
    *,
    repo_root: Path,
    run_mode: RunMode,
    agent_model: str | None,
    agent_reasoning_effort: str | None,
) -> AgentResult:
    try:
        from pydantic_ai import Agent
    except ImportError:
        return build_agent_block_result(
            task=task,
            repo_root=repo_root,
            summary="`pydantic_ai` nie je nainštalovaný, takže agentová vrstva sa nedá spustiť v tomto režime.",
            check_id="pydantic_ai_unavailable",
            message="Explicitne zvolený `pydantic_ai` backend nie je dostupný v lokálnom Python env.",
            suggested_fix="Nainštaluj `pydantic_ai` a jeho provider závislosti alebo použi `--agent-mode mock`.",
        )

    resolved_model = resolve_agent_model(agent_model)
    if not resolved_model:
        return build_agent_block_result(
            task=task,
            repo_root=repo_root,
            summary="Chýba model pre `pydantic_ai` backend.",
            check_id="missing_agent_model",
            message="Pre `pydantic_ai` backend nebol zadaný model cez `--agent-model` ani `THESIS_QC_AGENT_MODEL`.",
            suggested_fix="Spusti runner s `--agent-model openai:gpt-5.4-mini`, nastav `THESIS_QC_AGENT_MODEL` alebo doplň provider API key.",
        )

    prompt = safe_read_text(task.prompt_path)
    resolved_reasoning_effort = resolve_agent_reasoning_effort(
        resolved_model=resolved_model,
        agent_reasoning_effort=agent_reasoning_effort,
    )
    agent = Agent(
        resolved_model,
        system_prompt=prompt,
        model_settings=build_agent_model_settings(
            resolved_model=resolved_model,
            resolved_reasoning_effort=resolved_reasoning_effort,
        ),
    )
    try:
        result = agent.run_sync(task.user_input)
    except Exception as exc:
        return build_agent_block_result(
            task=task,
            repo_root=repo_root,
            summary=f"`{task.agent_name}` zlyhal pri provider requeste.",
            check_id="agent_runtime_error",
            message=f"Agent backend zlyhal: {exc.__class__.__name__}: {exc}",
            suggested_fix="Over API key, sieťovú dostupnosť a provider/model konfiguráciu, potom spusti QC znovu.",
        )

    try:
        payload = coerce_agent_payload(result.output)
    except ValueError as exc:
        return build_agent_block_result(
            task=task,
            repo_root=repo_root,
            summary=f"`{task.agent_name}` vrátil nevalidný payload.",
            check_id="agent_output_parse_error",
            message=str(exc),
            suggested_fix="Uprav prompt alebo output contract tak, aby agent vracal validný JSON objekt.",
        )

    try:
        return parse_agent_payload(
            payload=payload,
            expected_agent_name=task.agent_name,
            backend="pydantic_ai",
            repo_root=repo_root,
            prompt_path=task.prompt_path,
            input_refs=task.input_refs,
        )
    except Exception as exc:
        return build_agent_block_result(
            task=task,
            repo_root=repo_root,
            summary=f"`{task.agent_name}` vrátil payload, ktorý sa nedal zmapovať na `AgentResult`.",
            check_id="agent_output_shape_error",
            message=f"Payload validation zlyhala: {exc.__class__.__name__}: {exc}",
            suggested_fix="Skontroluj shape JSON odpovede a zosúlaď ho s `parse_agent_payload` kontraktom.",
        )


def build_agent_block_result(
    *,
    task: AgentTask,
    repo_root: Path,
    summary: str,
    check_id: str,
    message: str,
    suggested_fix: str,
) -> AgentResult:
    return AgentResult(
        agent_name=task.agent_name,
        backend="pydantic_ai",
        decision="BLOCK",
        confidence=1.0,
        summary=summary,
        findings=[
            Finding(
                area="presentation",
                severity="blocker",
                file=relative_path(repo_root, task.prompt_path),
                check_id=check_id,
                message=message,
                evidence_refs=[],
                suggested_fix=suggested_fix,
            )
        ],
        prompt_file=relative_path(repo_root, task.prompt_path),
        input_refs=[relative_path(repo_root, path) for path in task.input_refs],
    )


def coerce_agent_payload(output: object) -> dict[str, object]:
    if isinstance(output, dict):
        return output
    if isinstance(output, str):
        cleaned = output.strip()
        if not cleaned:
            raise ValueError("Agent output je prázdny string.")
        if cleaned.startswith("```"):
            cleaned = "\n".join(
                line for line in cleaned.splitlines() if not line.strip().startswith("```")
            ).strip()
        try:
            payload = json.loads(cleaned)
        except json.JSONDecodeError:
            start = cleaned.find("{")
            end = cleaned.rfind("}")
            if start == -1 or end == -1 or end <= start:
                raise
            payload = json.loads(cleaned[start : end + 1])
        if isinstance(payload, dict):
            return payload
        raise ValueError(f"Agent output musí byť JSON objekt, nie {type(payload).__name__}.")
    raise ValueError(f"Agent output musí byť `str` alebo `dict`, nie {type(output).__name__}.")


def parse_agent_payload(
    *,
    payload: dict[str, object],
    expected_agent_name: str,
    backend: AgentMode,
    repo_root: Path,
    prompt_path: Path,
    input_refs: list[Path],
) -> AgentResult:
    raw_findings = payload.get("findings", [])
    findings: list[Finding] = []
    if isinstance(raw_findings, list):
        for item in raw_findings:
            if not isinstance(item, dict):
                continue
            findings.append(
                Finding(
                    area=str(item.get("area", "presentation")),  # type: ignore[arg-type]
                    severity=str(item.get("severity", "minor")),  # type: ignore[arg-type]
                    file=str(item.get("file") or relative_path(repo_root, prompt_path)),
                    check_id=str(item.get("check_id", "agent_finding")),
                    message=str(item.get("message", "")),
                    evidence_refs=[str(value) for value in item.get("evidence_refs", []) if isinstance(value, str)],
                    suggested_fix=str(item["suggested_fix"]) if item.get("suggested_fix") else None,
                )
            )

    return AgentResult(
        agent_name=str(payload.get("agent_name", expected_agent_name)),
        backend=backend,
        decision=str(payload.get("decision", "PASS")),  # type: ignore[arg-type]
        confidence=float(payload.get("confidence", 0.5)),
        summary=str(payload.get("summary", "")),
        findings=findings,
        prompt_file=relative_path(repo_root, prompt_path),
        input_refs=[relative_path(repo_root, path) for path in input_refs],
    )


def safe_read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def render_current_export_preview_results(repo_root: Path) -> str:
    results_path = repo_root / "manuscript" / "40_results_preview_current_export.md"
    tables_dir = repo_root / "tables" / "current_export_preview"
    if not results_path.exists():
        return ""

    replacements = {
        "<!-- CURRENT_EXPORT_FRAGMENT_VALIDATION -->": tables_dir / "fragment_validation.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_DATASET -->": tables_dir / "fragment_dataset.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_DESCRIPTIVES -->": tables_dir / "fragment_descriptives.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_MEASUREMENT -->": tables_dir / "fragment_measurement.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_CELLS -->": tables_dir / "fragment_cells.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_MODELS -->": tables_dir / "fragment_models.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_EXPLORATORY -->": tables_dir / "fragment_exploratory.md",
        "<!-- CURRENT_EXPORT_FRAGMENT_ANCHORED -->": tables_dir / "fragment_anchored.md",
    }

    rendered = results_path.read_text(encoding="utf-8")
    for marker, path in replacements.items():
        rendered = rendered.replace(marker, safe_read_text(path))
    return rendered


def trim_text(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n\n[TRUNCATED]"


def read_csv_preview(path: Path, max_lines: int = 20) -> str:
    if not path.exists():
        return ""
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) <= max_lines:
        return "\n".join(lines)
    return "\n".join(lines[:max_lines]) + "\n[TRUNCATED]"


def infer_default_agent_model() -> str | None:
    if os.environ.get("OPENAI_API_KEY"):
        return "openai:gpt-5.4"
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic:claude-3-5-sonnet-latest"
    if os.environ.get("GOOGLE_API_KEY"):
        return "google-gla:gemini-2.5-pro"
    return None


def resolve_agent_model(agent_model: str | None) -> str | None:
    return agent_model or os.environ.get("THESIS_QC_AGENT_MODEL") or infer_default_agent_model()


def resolve_agent_reasoning_effort(
    *,
    resolved_model: str | None,
    agent_reasoning_effort: str | None,
) -> str | None:
    if agent_reasoning_effort:
        return agent_reasoning_effort
    if env_value := os.environ.get("THESIS_QC_AGENT_REASONING_EFFORT"):
        return env_value
    if resolved_model and resolved_model.startswith("openai:gpt-5.4"):
        return "high"
    return None


def build_agent_model_settings(
    *,
    resolved_model: str,
    resolved_reasoning_effort: str | None,
) -> dict[str, object] | None:
    if not resolved_reasoning_effort:
        return None
    if resolved_model.startswith("openai:"):
        return {"openai_reasoning_effort": resolved_reasoning_effort}
    return {"reasoning_effort": resolved_reasoning_effort}
