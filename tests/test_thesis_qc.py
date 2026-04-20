from __future__ import annotations

import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "analysis" / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from qc_hard_checks import (  # noqa: E402
    run_artifact_projection_qc,
    run_citation_registry_qc,
    run_data_integrity_qc,
)
from qc_agents import build_agent_tasks, resolve_agent_reasoning_effort, run_agent_reviews  # noqa: E402
from qc_models import build_qc_report  # noqa: E402
from qc_report import write_report_files  # noqa: E402


class ThesisQCTestCase(unittest.TestCase):
    maxDiff = None

    def make_repo(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="thesis_qc_"))
        for relative in (
            "analysis/data_clean",
            "analysis/outputs",
            "tables",
            "figures",
            "references",
            "manuscript",
        ):
            (root / relative).mkdir(parents=True, exist_ok=True)
        return root

    def write(self, root: Path, relative: str, content: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def populate_minimal_valid_repo(self, root: Path) -> None:
        self.write(
            root,
            "analysis/data_clean/ratings_clean.csv",
            "\n".join(
                [
                    "record_id,rater_id,transcript_id,seed_id,guardrail,profile,variant_id,backend_model,target_turns,actual_turns,rating_duration_sec,G1,G2,G3,G4,G5,A1,A2,A3,A4,A5,A6,A7,A8,A9,S1,S2,R1,R2,R3,R4,R5,guessed_origin,guess_confidence,comment",
                    "1,r1,t1,S01,0,R1,G0_R1,pydantic_ai|gpt-5.4,24,40,120,4,3,4,4,3,2,2,2,1,1,2,2,2,0,3,3,2,2,2,2,2,human_simulated,4,ok",
                    "2,r2,t1,S01,0,R1,G0_R1,pydantic_ai|gpt-5.4,24,40,100,4,3,4,4,3,2,2,2,1,1,2,2,2,0,3,3,2,2,2,2,2,human_simulated,4,ok",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/data_clean/transcripts_master.csv",
            "\n".join(
                [
                    "transcript_id,seed_id,guardrail,profile,variant_id,backend_model,target_turns,actual_turns,chat_variability,created_at,transcript_path",
                    "t1,S01,0,R1,G0_R1,pydantic_ai|gpt-5.4,24,40,locked,2026-04-01,transcripts/t1.txt",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/data_clean/seed_anchors_final.csv",
            "\n".join(
                [
                    "seed_id,A1_anchor,A2_anchor,A3_anchor,A4_anchor,A5_anchor,A6_anchor,A7_anchor,A8_anchor,A9_anchor,S1_anchor,S2_anchor,target_severity_label,functional_impact_label,notes",
                    "S01,2,2,2,1,1,2,2,2,0,3,3,moderate,moderate,note",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/data_clean/raters_clean.csv",
            "\n".join(
                [
                    "rater_id,profession,specialization,years_practice,experience_with_mdd,notes",
                    "r1,psychologist,clinical,8,weekly,",
                    "r2,psychologist,clinical,16_plus,weekly,",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/run_manifest.csv",
            "\n".join(
                [
                    "run_timestamp,source_mode,used_ratings,used_transcripts,used_seeds,used_raters,severity_error_mode,n_rows_analysis_long,n_raters,n_transcripts,n_seeds",
                    "2026-04-17T10:00:00Z,data_clean,/tmp/ratings_clean.csv,/tmp/transcripts_master.csv,/tmp/seed_anchors_final.csv,/tmp/raters_clean.csv,direct_1to5,2,2,1,1",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/qc_dataset_summary.csv",
            "\n".join(
                [
                    "metric,value",
                    "source_mode,data_clean",
                    "n_raters,2",
                    "n_transcripts,1",
                    "n_seeds,1",
                    "n_ratings,2",
                    "mean_ratings_per_transcript,2",
                    "min_ratings_per_transcript,2",
                    "max_ratings_per_transcript,2",
                    "severity_error_mode,direct_1to5",
                    "guardrail_off,2",
                    "profile_R1,2",
                    "guardrail_off_profile_R1,2",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/descriptives_items.csv",
            "\n".join(
                [
                    "variable,n_non_missing,levels_used,median,iqr,mean,sd,min,max",
                    "g1,2,1,4,0,4,0,4,4",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/descriptives_composites.csv",
            "\n".join(
                [
                    "variable,n_non_missing,mean,sd,median,iqr,min,max",
                    "plausibility_index,2,4,0,4,0,4,4",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/internal_consistency.csv",
            "\n".join(
                [
                    "block,n_items,n_rows,alpha,omega,status,detail",
                    "g1_g5,5,2,0.8,0.8,ok,ok",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/icc_summary.csv",
            "\n".join(
                [
                    "outcome,icc_type,estimate,conf_low,conf_high,status,detail",
                    "plausibility_index,ICC2k,0.8,0.5,0.9,ok,ok",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/lmm_core_models.csv",
            "\n".join(
                [
                    "outcome,model_type,term,estimate,std_error,statistic,p_value,conf_low,conf_high,status,detail",
                    "plausibility_index,lmm,guardrailon,0.2,0.1,2,0.04,0.01,0.39,ok,ok",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/clmm_item_models.csv",
            "\n".join(
                [
                    "outcome,model_type,term,estimate,std_error,statistic,p_value,conf_low,conf_high,status,detail",
                    "g2,clmm,guardrailon,0.3,0.1,3,0.02,0.1,0.5,ok,ok",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "analysis/outputs/analysis_long.csv",
            "\n".join(
                [
                    "record_id,rater_id,transcript_id,seed_id,guardrail,profile,variant_id,backend_model,target_turns,actual_turns,rating_duration_sec,g1,g2,g3,g4,g5,a1,a2,a3,a4,a5,a6,a7,a8,a9,s1,s2,r1,r2,r3,r4,r5,guessed_origin,guess_confidence,comment,plausibility_index,defect_index,symptom_error_mean,severity_error,impact_error",
                    "1,r1,t1,S01,off,R1,G0_R1,pydantic_ai|gpt-5.4,24,40,120,4,3,4,4,3,2,2,2,1,1,2,2,2,0,3,3,2,2,2,2,2,human_simulated,4,ok,4,2.0,0.2,0,0",
                    "2,r2,t1,S01,off,R1,G0_R1,pydantic_ai|gpt-5.4,24,40,100,4,3,4,4,3,2,2,2,1,1,2,2,2,0,3,3,2,2,2,2,2,human_simulated,4,ok,4,2.0,0.2,0,0",
                ]
            )
            + "\n",
        )
        self.write(root, "tables/table_1_dataset_summary.csv", (root / "analysis/outputs/qc_dataset_summary.csv").read_text(encoding="utf-8"))
        self.write(
            root,
            "tables/table_2_descriptives.csv",
            "\n".join(
                [
                    "variable,n_non_missing,levels_used,median,iqr,mean,sd,min,max,section",
                    "g1,2,1,4,0,4,0,4,4,items",
                    "plausibility_index,2,NA,4,0,4,0,4,4,composites",
                ]
            )
            + "\n",
        )
        self.write(
            root,
            "tables/table_3_item_frequencies.csv",
            "\n".join(
                [
                    "variable,response,n,prop",
                    "g1,4,2,1",
                    "r1,2,2,1",
                    "r2,2,2,1",
                    "r3,2,2,1",
                    "r4,2,2,1",
                    "r5,2,2,1",
                    "s1,3,2,1",
                    "s2,3,2,1",
                    "g2,3,2,1",
                    "g3,4,2,1",
                    "g4,4,2,1",
                    "g5,3,2,1",
                ]
            )
            + "\n",
        )
        self.write(root, "tables/table_4_internal_consistency.csv", (root / "analysis/outputs/internal_consistency.csv").read_text(encoding="utf-8"))
        self.write(root, "tables/table_5_icc.csv", (root / "analysis/outputs/icc_summary.csv").read_text(encoding="utf-8"))
        self.write(
            root,
            "tables/table_6_mixed_models_core.csv",
            "\n".join(
                [
                    "outcome,model_type,term,estimate,std_error,statistic,p_value,conf_low,conf_high,status,detail,model_family",
                    "plausibility_index,lmm,guardrailon,0.2,0.1,2,0.04,0.01,0.39,ok,ok,lmm",
                    "g2,clmm,guardrailon,0.3,0.1,3,0.02,0.1,0.5,ok,ok,clmm",
                ]
            )
            + "\n",
        )
        (root / "figures/figure_1_primary_outcomes_by_condition.png").write_bytes(b"png")
        (root / "figures/figure_2_emmeans_core_models.png").write_bytes(b"png")
        self.write(
            root,
            "references/zotero-thesis.bib",
            "@article{valid2024key,\n  title = {Valid key}\n}\n",
        )
        self.write(root, "manuscript/20_introduction.md", "Text with [@valid2024key].\n")
        self.write(root, "manuscript/40_results.md", "Bez placeholderov.\n")

    def test_data_integrity_detects_duplicate_rater_transcript_pair(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        self.write(
            repo,
            "analysis/data_clean/ratings_clean.csv",
            (repo / "analysis/data_clean/ratings_clean.csv")
            .read_text(encoding="utf-8")
            .replace("2,r2,t1", "2,r1,t1"),
        )

        result = run_data_integrity_qc(repo, "smoke")

        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any(f.check_id == "duplicate_rater_transcript_pair" for f in result.findings))

    def test_citation_registry_detects_missing_citekey(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        self.write(root=repo, relative="manuscript/20_introduction.md", content="Broken [@missing2024key].\n")

        result = run_citation_registry_qc(repo, "smoke")

        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any(f.check_id == "missing_citekey_in_bib" for f in result.findings))

    def test_artifact_projection_detects_table_5_mismatch(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        self.write(
            repo,
            "tables/table_5_icc.csv",
            "\n".join(
                [
                    "outcome,icc_type,estimate,conf_low,conf_high,status,detail",
                    "plausibility_index,ICC2k,0.3,0.1,0.4,ok,wrong",
                ]
            )
            + "\n",
        )

        result = run_artifact_projection_qc(repo, "smoke")

        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any(f.check_id == "table_5_projection_mismatch" for f in result.findings))

    def test_report_writer_emits_json_and_markdown(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        checks = [
            run_data_integrity_qc(repo, "smoke"),
            run_artifact_projection_qc(repo, "smoke"),
            run_citation_registry_qc(repo, "smoke"),
        ]
        report = build_qc_report("smoke", "off", repo, checks)
        output_dir = repo / "analysis" / "qc_reports"

        written = write_report_files(report, output_dir)

        self.assertTrue(written["json"].exists())
        self.assertTrue(written["markdown"].exists())
        payload = json.loads(written["json"].read_text(encoding="utf-8"))
        self.assertEqual(payload["overall_decision"], "PASS_WITH_NOTES")
        self.assertIsNone(payload["orchestrator_summary"])

    def test_mock_agent_mode_returns_three_agent_results(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        checks = [
            run_data_integrity_qc(repo, "smoke"),
            run_artifact_projection_qc(repo, "smoke"),
            run_citation_registry_qc(repo, "smoke"),
        ]

        results = run_agent_reviews(repo, "smoke", "mock", checks)

        self.assertEqual(len(results), 3)
        self.assertTrue(all(result.backend == "mock" for result in results))
        self.assertTrue(all(result.prompt_file for result in results))

    def test_report_includes_orchestrator_summary_for_agent_runs(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        checks = [
            run_data_integrity_qc(repo, "smoke"),
            run_artifact_projection_qc(repo, "smoke"),
            run_citation_registry_qc(repo, "smoke"),
        ]
        results = run_agent_reviews(repo, "smoke", "mock", checks)

        report = build_qc_report(
            "smoke",
            "pydantic_ai",
            repo,
            checks,
            agent_results=results,
            resolved_agent_model="openai:gpt-5.4",
            resolved_reasoning_effort="high",
        )

        self.assertIsNotNone(report.orchestrator_summary)
        assert report.orchestrator_summary is not None
        self.assertEqual(report.orchestrator_summary.resolved_agent_model, "openai:gpt-5.4")
        self.assertEqual(report.orchestrator_summary.resolved_reasoning_effort, "high")
        self.assertTrue(any("citation_support_agent" in item for item in report.orchestrator_summary.agent_scopes))

    def test_resolve_agent_reasoning_effort_defaults_to_high_for_gpt_5_4(self) -> None:
        effort = resolve_agent_reasoning_effort(
            resolved_model="openai:gpt-5.4",
            agent_reasoning_effort=None,
        )
        self.assertEqual(effort, "high")

    def test_stats_claim_agent_task_includes_variable_alias_map(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        self.write(repo, "manuscript/30_method.md", "S1 je expertne hodnotená závažnosť. S2 je expertne hodnotený funkčný dopad.\n")

        tasks = build_agent_tasks(repo, "smoke")
        stats_task = next(task for task in tasks if task.agent_name == "stats_claim_agent")

        self.assertIn("VARIABLE ALIAS MAP FOR MANUSCRIPT WORDING", stats_task.user_input)
        self.assertIn("`S1` / `s1` = expertne hodnotená závažnosť", stats_task.user_input)
        self.assertIn("manuscript/30_method.md", [str(path.relative_to(repo)) for path in stats_task.input_refs])

    def test_pydantic_ai_mode_blocks_when_dependency_missing(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        checks = [
            run_data_integrity_qc(repo, "smoke"),
            run_artifact_projection_qc(repo, "smoke"),
            run_citation_registry_qc(repo, "smoke"),
        ]

        results = run_agent_reviews(repo, "smoke", "pydantic_ai", checks, agent_model="openai:gpt-5.4")

        self.assertEqual(len(results), 3)
        self.assertTrue(all(result.decision == "BLOCK" for result in results))
        self.assertTrue(any(f.check_id == "pydantic_ai_unavailable" for result in results for f in result.findings))

    def test_pydantic_ai_mode_blocks_when_agent_runtime_fails(self) -> None:
        repo = self.make_repo()
        self.populate_minimal_valid_repo(repo)
        checks = [
            run_data_integrity_qc(repo, "smoke"),
            run_artifact_projection_qc(repo, "smoke"),
            run_citation_registry_qc(repo, "smoke"),
        ]

        fake_module = types.ModuleType("pydantic_ai")

        class FakeAgent:
            def __init__(self, *args: object, **kwargs: object) -> None:
                pass

            def run_sync(self, user_input: str) -> object:
                raise RuntimeError(f"simulated provider failure for {user_input[:12]}")

        fake_module.Agent = FakeAgent  # type: ignore[attr-defined]

        with mock.patch.dict(sys.modules, {"pydantic_ai": fake_module}):
            results = run_agent_reviews(repo, "smoke", "pydantic_ai", checks, agent_model="openai:gpt-5.4")

        self.assertEqual(len(results), 3)
        self.assertTrue(all(result.decision == "BLOCK" for result in results))
        self.assertTrue(all(result.backend == "pydantic_ai" for result in results))
        self.assertTrue(any(f.check_id == "agent_runtime_error" for result in results for f in result.findings))


if __name__ == "__main__":
    unittest.main()
