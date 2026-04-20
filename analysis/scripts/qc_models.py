from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

Severity = Literal["info", "minor", "major", "blocker"]
CheckStatus = Literal["PASS", "REVISE", "BLOCK"]
RunMode = Literal["smoke", "pre_word", "final_results"]
OverallDecision = Literal["PASS_WITH_NOTES", "REVISE", "BLOCK"]
AgentMode = Literal["off", "mock", "pydantic_ai"]
AgentDecision = Literal["PASS", "REVISE", "BLOCK", "SKIP"]

SEVERITY_RANK: dict[Severity, int] = {
    "info": 0,
    "minor": 1,
    "major": 2,
    "blocker": 3,
}


@dataclass(slots=True)
class Finding:
    area: Literal["data", "citation", "stats", "presentation"]
    severity: Severity
    file: str
    check_id: str
    message: str
    evidence_refs: list[str] = field(default_factory=list)
    suggested_fix: str | None = None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class CheckResult:
    name: str
    findings: list[Finding] = field(default_factory=list)

    @property
    def status(self) -> CheckStatus:
        if any(finding.severity == "blocker" for finding in self.findings):
            return "BLOCK"
        if any(SEVERITY_RANK[finding.severity] >= SEVERITY_RANK["major"] for finding in self.findings):
            return "REVISE"
        return "PASS"

    @property
    def summary(self) -> str:
        if not self.findings:
            return "No findings."

        counts: dict[Severity, int] = {severity: 0 for severity in SEVERITY_RANK}
        for finding in self.findings:
            counts[finding.severity] += 1

        parts = [
            f"{counts['blocker']} blocker",
            f"{counts['major']} major",
            f"{counts['minor']} minor",
            f"{counts['info']} info",
        ]
        return ", ".join(parts) + "."

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "status": self.status,
            "summary": self.summary,
            "findings": [finding.to_dict() for finding in self.findings],
        }


@dataclass(slots=True)
class AgentResult:
    agent_name: str
    backend: AgentMode
    decision: AgentDecision
    confidence: float
    summary: str
    findings: list[Finding] = field(default_factory=list)
    prompt_file: str | None = None
    input_refs: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "agent_name": self.agent_name,
            "backend": self.backend,
            "decision": self.decision,
            "confidence": self.confidence,
            "summary": self.summary,
            "prompt_file": self.prompt_file,
            "input_refs": self.input_refs,
            "findings": [finding.to_dict() for finding in self.findings],
        }


@dataclass(slots=True)
class OrchestratorSummary:
    resolved_agent_model: str | None
    resolved_reasoning_effort: str | None
    agent_scopes: list[str] = field(default_factory=list)
    agreements: list[str] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    final_verdict: str = ""
    final_summary: str = ""

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class QCReport:
    run_mode: RunMode
    agent_mode: AgentMode
    repo_root: str
    generated_at: str
    checks: list[CheckResult]
    agent_results: list[AgentResult] = field(default_factory=list)
    resolved_agent_model: str | None = None
    resolved_reasoning_effort: str | None = None

    @property
    def findings(self) -> list[Finding]:
        collected: list[Finding] = []
        for check in self.checks:
            collected.extend(check.findings)
        for result in self.agent_results:
            collected.extend(result.findings)
        return collected

    @property
    def hard_qc_passed(self) -> bool:
        return not any(finding.severity == "blocker" for check in self.checks for finding in check.findings)

    @property
    def overall_decision(self) -> OverallDecision:
        if any(finding.severity == "blocker" for finding in self.findings):
            return "BLOCK"
        if any(result.decision == "BLOCK" for result in self.agent_results):
            return "BLOCK"
        if self.run_mode in {"pre_word", "final_results"} and any(
            finding.severity == "major" for finding in self.findings
        ):
            return "REVISE"
        if self.run_mode in {"pre_word", "final_results"} and any(
            result.decision == "REVISE" for result in self.agent_results
        ):
            return "REVISE"
        return "PASS_WITH_NOTES"

    @property
    def severity_counts(self) -> dict[str, int]:
        counts = {severity: 0 for severity in SEVERITY_RANK}
        for finding in self.findings:
            counts[finding.severity] += 1
        return counts

    @property
    def next_actions(self) -> list[str]:
        actions: list[str] = []
        seen: set[str] = set()

        for finding in self.findings:
            if finding.suggested_fix and finding.suggested_fix not in seen:
                seen.add(finding.suggested_fix)
                actions.append(finding.suggested_fix)

        if actions:
            return actions

        if self.overall_decision == "BLOCK":
            return ["Odstrániť blocker findings a spustiť QC znovu."]
        if self.overall_decision == "REVISE":
            return ["Zapracovať major findings a potom spustiť QC znovu."]
        return ["QC prešiel bez blockerov; môžeš pokračovať ďalším workflow krokom."]

    @property
    def orchestrator_summary(self) -> OrchestratorSummary | None:
        if not self.agent_results:
            return None

        scope_map = {
            "citation_support_agent": "Kontrola citačnej opory tvrdení a lokálneho source-support driftu vo Results.",
            "stats_claim_agent": "Kontrola zhody medzi Results prose a CSV outputmi (`ICC`, `LMM`, `CLMM`, tabuľky).",
            "results_presentation_agent": "Kontrola čitateľnosti, redundancie a IMRaD-aligned prezentácie výsledkov.",
        }

        agent_scopes = [
            f"{result.agent_name}: {scope_map.get(result.agent_name, 'Špecializovaná QC rola.')}"
            for result in self.agent_results
        ]

        agreements: list[str] = []
        conflicts: list[str] = []
        by_name = {result.agent_name: result for result in self.agent_results}

        citation_result = by_name.get("citation_support_agent")
        if citation_result and citation_result.decision == "PASS":
            agreements.append("Citačná kontrola nenašla lokálny source-support drift.")

        stats_result = by_name.get("stats_claim_agent")
        if stats_result and stats_result.decision == "PASS":
            agreements.append("Štatistické tvrdenia sedia s aktuálnymi CSV outputmi.")

        presentation_result = by_name.get("results_presentation_agent")
        if presentation_result and presentation_result.decision == "PASS":
            agreements.append("Prezentácia výsledkov je v aktuálnom rune čitateľná bez ďalších redakčných zásahov.")

        non_pass = [result for result in self.agent_results if result.decision in {"REVISE", "BLOCK"}]
        if non_pass:
            conflicts.append(
                "Scope split medzi agentmi: "
                + ", ".join(f"{result.agent_name}={result.decision}" for result in non_pass)
            )

        if self.overall_decision == "BLOCK":
            final_summary = "Orchestrator uzatvára run ako blocker, pretože aspoň jeden agent alebo finding ostal na blocker úrovni."
        elif any(result.decision == "REVISE" for result in self.agent_results):
            final_summary = "Orchestrator uzatvára run bez blockeru, ale s odporúčaním na redakčnú alebo workflow revíziu pred finálnym exportom."
        else:
            final_summary = "Orchestrator uzatvára run bez blockeru a bez otvorených agentových revízií."

        return OrchestratorSummary(
            resolved_agent_model=self.resolved_agent_model,
            resolved_reasoning_effort=self.resolved_reasoning_effort,
            agent_scopes=agent_scopes,
            agreements=agreements,
            conflicts=conflicts,
            final_verdict=self.overall_decision,
            final_summary=final_summary,
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "run_mode": self.run_mode,
            "agent_mode": self.agent_mode,
            "repo_root": self.repo_root,
            "generated_at": self.generated_at,
            "resolved_agent_model": self.resolved_agent_model,
            "resolved_reasoning_effort": self.resolved_reasoning_effort,
            "hard_qc_passed": self.hard_qc_passed,
            "overall_decision": self.overall_decision,
            "severity_counts": self.severity_counts,
            "checks": [check.to_dict() for check in self.checks],
            "agent_results": [result.to_dict() for result in self.agent_results],
            "orchestrator_summary": self.orchestrator_summary.to_dict() if self.orchestrator_summary else None,
            "findings": [finding.to_dict() for finding in self.findings],
            "next_actions": self.next_actions,
        }


def build_qc_report(
    run_mode: RunMode,
    agent_mode: AgentMode,
    repo_root: Path,
    checks: list[CheckResult],
    agent_results: list[AgentResult] | None = None,
    resolved_agent_model: str | None = None,
    resolved_reasoning_effort: str | None = None,
) -> QCReport:
    return QCReport(
        run_mode=run_mode,
        agent_mode=agent_mode,
        repo_root=str(repo_root),
        generated_at=datetime.now(UTC).isoformat(timespec="seconds"),
        checks=checks,
        agent_results=agent_results or [],
        resolved_agent_model=resolved_agent_model,
        resolved_reasoning_effort=resolved_reasoning_effort,
    )
