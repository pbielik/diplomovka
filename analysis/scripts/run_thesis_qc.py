#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from qc_agents import resolve_agent_model, resolve_agent_reasoning_effort, run_agent_reviews
from qc_env import load_simple_dotenv
from qc_hard_checks import run_all_hard_checks
from qc_models import build_qc_report
from qc_report import write_report_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Deterministic QC runner for thesis data, output projections and citekeys."
    )
    parser.add_argument(
        "--run-mode",
        choices=("smoke", "pre_word", "final_results"),
        default="smoke",
        help="Controls how aggressively the runner gates findings.",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Override repo root. Defaults to the parent of analysis/.",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Override QC report output directory. Defaults to analysis/qc_reports/.",
    )
    parser.add_argument(
        "--agent-mode",
        choices=("off", "mock", "pydantic_ai"),
        default="mock",
        help="Controls whether the agent/orchestrator layer runs and which backend it uses.",
    )
    parser.add_argument(
        "--agent-model",
        default=None,
        help="Model identifier for `pydantic_ai` agent mode, e.g. `openai:gpt-5.4`.",
    )
    parser.add_argument(
        "--agent-reasoning-effort",
        choices=("low", "medium", "high", "xhigh", "minimal", "none"),
        default=None,
        help="Optional reasoning effort override for the agent backend.",
    )
    return parser.parse_args()


def resolve_repo_root(cli_value: str | None) -> Path:
    if cli_value:
        return Path(cli_value).expanduser().resolve()
    return Path(__file__).resolve().parents[2]


def resolve_output_dir(repo_root: Path, cli_value: str | None) -> Path:
    if cli_value:
        return Path(cli_value).expanduser().resolve()
    return repo_root / "analysis" / "qc_reports"


def decision_exit_code(decision: str) -> int:
    if decision == "BLOCK":
        return 2
    if decision == "REVISE":
        return 1
    return 0


def main() -> int:
    args = parse_args()
    run_mode = args.run_mode  # argparse choices guarantee validity
    repo_root = resolve_repo_root(args.repo_root)
    output_dir = resolve_output_dir(repo_root, args.output_dir)
    load_simple_dotenv(repo_root / ".env")
    resolved_agent_model = resolve_agent_model(args.agent_model) if args.agent_mode == "pydantic_ai" else None
    resolved_reasoning_effort = (
        resolve_agent_reasoning_effort(
            resolved_model=resolved_agent_model,
            agent_reasoning_effort=args.agent_reasoning_effort,
        )
        if args.agent_mode == "pydantic_ai"
        else None
    )

    checks = run_all_hard_checks(repo_root=repo_root, run_mode=run_mode)  # type: ignore[arg-type]
    agent_results = run_agent_reviews(
        repo_root=repo_root,
        run_mode=run_mode,  # type: ignore[arg-type]
        agent_mode=args.agent_mode,  # type: ignore[arg-type]
        hard_checks=checks,
        agent_model=args.agent_model,
        agent_reasoning_effort=args.agent_reasoning_effort,
    )
    report = build_qc_report(
        run_mode=run_mode,  # type: ignore[arg-type]
        agent_mode=args.agent_mode,  # type: ignore[arg-type]
        repo_root=repo_root,
        checks=checks,
        agent_results=agent_results,
        resolved_agent_model=resolved_agent_model,
        resolved_reasoning_effort=resolved_reasoning_effort,
    )
    written = write_report_files(report, output_dir)

    print(f"QC decision: {report.overall_decision}")
    print(f"Hard QC passed: {'yes' if report.hard_qc_passed else 'no'}")
    print(f"Agent mode: {args.agent_mode}")
    print(
        "Severity counts: "
        f"blocker={report.severity_counts['blocker']}, "
        f"major={report.severity_counts['major']}, "
        f"minor={report.severity_counts['minor']}, "
        f"info={report.severity_counts['info']}"
    )
    if report.agent_results:
        decisions = ", ".join(f"{result.agent_name}={result.decision}" for result in report.agent_results)
        print(f"Agent decisions: {decisions}")
    print(f"JSON report: {written['json']}")
    print(f"Markdown report: {written['markdown']}")

    return decision_exit_code(report.overall_decision)


if __name__ == "__main__":
    raise SystemExit(main())
