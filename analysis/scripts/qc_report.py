from __future__ import annotations

import json
from pathlib import Path

from qc_models import QCReport


def build_markdown_report(report: QCReport) -> str:
    lines: list[str] = [
        "# Thesis QC Report",
        "",
        f"- Generated at: `{report.generated_at}`",
        f"- Run mode: `{report.run_mode}`",
        f"- Agent mode: `{report.agent_mode}`",
        f"- Resolved agent model: `{report.resolved_agent_model or 'n/a'}`",
        f"- Resolved reasoning effort: `{report.resolved_reasoning_effort or 'n/a'}`",
        f"- Repo root: `{report.repo_root}`",
        f"- Hard QC passed: `{'yes' if report.hard_qc_passed else 'no'}`",
        f"- Overall decision: `{report.overall_decision}`",
        "",
        "## Severity Counts",
        "",
        f"- blocker: `{report.severity_counts['blocker']}`",
        f"- major: `{report.severity_counts['major']}`",
        f"- minor: `{report.severity_counts['minor']}`",
        f"- info: `{report.severity_counts['info']}`",
        "",
        "## Checks",
        "",
    ]

    for check in report.checks:
        lines.append(f"- `{check.name}`: `{check.status}` — {check.summary}")

    lines.extend(["", "## Agents", ""])
    if not report.agent_results:
        lines.append("- Žiadna agentová vrstva nebola spustená.")
    else:
        for result in report.agent_results:
            prompt_suffix = f" (`{result.prompt_file}`)" if result.prompt_file else ""
            lines.append(
                f"- `{result.agent_name}` cez `{result.backend}`: `{result.decision}`{prompt_suffix} — {result.summary}"
            )

    lines.extend(["", "## Orchestrator Summary", ""])
    if not report.orchestrator_summary:
        lines.append("- Orchestrator summary nie je dostupný bez agentových výsledkov.")
    else:
        summary = report.orchestrator_summary
        lines.append(f"- Resolved agent model: `{summary.resolved_agent_model or 'n/a'}`")
        lines.append(f"- Resolved reasoning effort: `{summary.resolved_reasoning_effort or 'n/a'}`")
        lines.append(f"- Final verdict: `{summary.final_verdict}`")
        lines.append(f"- Summary: {summary.final_summary}")
        lines.append("- Agent scopes:")
        for item in summary.agent_scopes:
            lines.append(f"  - {item}")
        if summary.agreements:
            lines.append("- Agreements:")
            for item in summary.agreements:
                lines.append(f"  - {item}")
        if summary.conflicts:
            lines.append("- Conflicts / splits:")
            for item in summary.conflicts:
                lines.append(f"  - {item}")

    lines.extend(["", "## Findings", ""])

    if not report.findings:
        lines.append("Žiadne findings.")
    else:
        for index, finding in enumerate(report.findings, start=1):
            lines.append(
                f"{index}. `{finding.severity}` `{finding.check_id}` v `{finding.file}` — {finding.message}"
            )
            if finding.evidence_refs:
                lines.append(f"   Evidence: {', '.join(finding.evidence_refs)}")
            if finding.suggested_fix:
                lines.append(f"   Suggested fix: {finding.suggested_fix}")

    lines.extend(["", "## Next Actions", ""])
    for action in report.next_actions:
        lines.append(f"- {action}")

    lines.append("")
    return "\n".join(lines)


def write_report_files(report: QCReport, output_dir: Path) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = report.generated_at.replace(":", "").replace("-", "")
    base_name = f"{stamp}_{report.run_mode}_{report.agent_mode}"
    json_path = output_dir / f"{base_name}.json"
    md_path = output_dir / f"{base_name}.md"
    latest_json = output_dir / f"latest_{report.run_mode}_{report.agent_mode}.json"
    latest_md = output_dir / f"latest_{report.run_mode}_{report.agent_mode}.md"

    json_payload = json.dumps(report.to_dict(), ensure_ascii=False, indent=2)
    markdown_payload = build_markdown_report(report)

    json_path.write_text(json_payload + "\n", encoding="utf-8")
    md_path.write_text(markdown_payload, encoding="utf-8")
    latest_json.write_text(json_payload + "\n", encoding="utf-8")
    latest_md.write_text(markdown_payload, encoding="utf-8")

    return {
        "json": json_path,
        "markdown": md_path,
        "latest_json": latest_json,
        "latest_markdown": latest_md,
    }
