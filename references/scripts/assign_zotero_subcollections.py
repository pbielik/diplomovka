#!/usr/bin/env python3

import argparse
import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
HOME = Path.home()
ZOTERO_DB = HOME / "Zotero" / "zotero.sqlite"
BACKUP_DIR = Path("/tmp") / "codex-zotero-subcollections"


COLLECTIONS = {
    "mdd_symptomatology": 14,          # 01.1 MDD symptomatology
    "differential_diagnosis": 15,     # 01.2 Differential diagnosis
    "phq_anchor": 16,                 # 01.3 PHQ-8 / PHQ-9
    "systematic_reviews": 17,         # 02.1 Systematic reviews
    "simulated_patients": 18,         # 02.2 Simulated patients / virtual patients
    "education_training": 19,         # 02.3 Education / training use-cases
    "risks_limitations": 20,          # 02.4 Risks / limitations
    "llm_general": 37,                # 02.5 Use of LLM
    "cosmin": 21,                     # 03.1 COSMIN
    "content_validity": 22,           # 03.2 Content validity / CVI
    "expert_panel": 23,               # 03.3 Expert panel / Delphi
    "interrater_reliability": 24,     # 03.4 Interrater reliability
    "validity_reliability": 38,       # 03.5 Validity and Realiability
    "pilot_design": 25,               # 04.1 Pilot study design
    "icc_agreement": 26,              # 04.2 ICC / agreement
    "ordinal_models": 28,             # 04.4 Ordinal models
    "ethics_governance": 9,           # 07 Ethics – AI governance
    "phq_seed_anchors": 31,           # 08.2 PHQ anchor papers
}


CITEKEY_COLLECTIONS = {
    "obradovich2024llmpsychiatry": ["llm_general", "risks_limitations"],
    "meng2024llmmedicine": ["llm_general"],
    "ajluni2025psychiatriceducation": ["education_training"],
    "yu2025simulatedpatientsystems": ["simulated_patients"],
    "brugge2024patientsimulation": ["simulated_patients", "education_training"],
    "evans2015vignettes": ["pilot_design"],
    "baguley2022vignettedata": ["pilot_design"],
    "williams2017simulationmentalhealth": ["education_training"],
    "dawood2024standardizedpatient": ["education_training"],
    "kennedy2008coresymptoms": ["mdd_symptomatology"],
    "maj2020depressioncharacterization": ["mdd_symptomatology"],
    "kroenke2001phq9": ["phq_anchor", "phq_seed_anchors"],
    "guidi2011clinicalinterviewdepression": ["mdd_symptomatology"],
    "roustan2025cliniciansguide": ["risks_limitations"],
    "asgari2025hallucinationframework": ["risks_limitations", "ethics_governance"],
    "mcintyre2019mddvsbipolar": ["differential_diagnosis"],
    "hirschfeld2014bipolardifferential": ["differential_diagnosis"],
    "stein2021anxietycharacterization": ["differential_diagnosis"],
    "dubovsky2021psychoticdepression": ["differential_diagnosis"],
    "lynn1986contentvalidity": ["content_validity"],
    "polit2007cvi": ["content_validity"],
    "hasson2000delphi": ["expert_panel"],
    "boateng2018scaledevelopment": ["validity_reliability"],
    "rutherfordhemming2015simulationcvi": ["content_validity"],
    "cook2010computerizedvirtualpatients": ["simulated_patients"],
    "kononowicz2019virtualpatients": ["simulated_patients"],
    "who2021ethicsaiforhealth": ["ethics_governance"],
    "who2024lmmguidance": ["ethics_governance"],
    "goddard2012automationbias": ["ethics_governance", "risks_limitations"],
    "howell2024genaipatientsafety": ["ethics_governance", "risks_limitations"],
    "khera2023automationbiasassistiveai": ["ethics_governance", "risks_limitations"],
    "mchugh2012kappa": ["interrater_reliability", "icc_agreement"],
    "jakobsson2005ordinalagreement": ["interrater_reliability", "icc_agreement", "ordinal_models"],
    "marasini2016weightedindexes": ["icc_agreement", "ordinal_models"],
    "nelson2015manyratersordinal": ["icc_agreement", "ordinal_models"],
    "mitani2017ordinalsummarymeasures": ["icc_agreement", "ordinal_models"],
    "omar2024llmpsychiatry": ["systematic_reviews"],
    "guo2024llmmentalhealth": ["systematic_reviews"],
    "terwee2018COSMINMethodologyEvaluating": ["cosmin", "content_validity"],
    "who2025depression": ["mdd_symptomatology"],
    "chaby2022embodiedvirtualpatients": ["simulated_patients"],
    "li2024curefun": ["simulated_patients", "llm_general"],
    "wang2024patientpsi": ["simulated_patients", "llm_general"],
    "lee2025adaptivevp": ["simulated_patients", "llm_general"],
    "kim2025mindvoyager": ["simulated_patients", "llm_general"],
    "appeswg2021newreality": ["education_training"],
    "rice2022simulatedplacements": ["education_training"],
    "sheen2021simulationeducation": ["education_training"],
    "glatz2022simulationelements": ["education_training"],
    "schmidt2025client101": ["simulated_patients", "education_training"],
    "morrison2025virtuallypsychologist": ["simulated_patients", "education_training"],
}


def log(message: str) -> None:
    print(message, file=sys.stderr)


def quit_zotero() -> None:
    subprocess.run(
        ["osascript", "-e", 'tell application "Zotero" to quit'],
        check=True,
        capture_output=True,
        text=True,
    )
    for _ in range(30):
        status = subprocess.run(["pgrep", "-x", "Zotero"], capture_output=True, text=True)
        if status.returncode != 0:
            return
        time.sleep(1)
    raise RuntimeError("Zotero did not quit within 30 seconds")


def launch_zotero() -> None:
    subprocess.run(["open", "-a", "Zotero"], check=True, capture_output=True, text=True)


def wait_for_connector() -> None:
    for _ in range(60):
        status = subprocess.run(
            ["curl", "-sS", "http://127.0.0.1:23119/connector/ping"],
            capture_output=True,
            text=True,
        )
        if status.returncode == 0 and "Zotero is running" in status.stdout:
            return
        time.sleep(1)
    raise RuntimeError("Zotero connector did not come back within 60 seconds")


def backup_db() -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = BACKUP_DIR / f"zotero.sqlite.{stamp}"
    shutil.copy2(ZOTERO_DB, target)
    return target


def get_item_ids_by_citekey(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute(
        """
        SELECT v.value AS citekey, i.itemID
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID AND d.fieldID = 9
        JOIN itemDataValues v ON v.valueID = d.valueID
        LEFT JOIN deletedItems di ON di.itemID = i.itemID
        WHERE di.itemID IS NULL
        """
    ).fetchall()
    return {row["citekey"]: int(row["itemID"]) for row in rows}


def assign_collections(conn: sqlite3.Connection) -> tuple[int, list[str]]:
    conn.row_factory = sqlite3.Row
    citekey_to_item = get_item_ids_by_citekey(conn)
    inserted = 0
    missing = []
    for citekey, targets in CITEKEY_COLLECTIONS.items():
        item_id = citekey_to_item.get(citekey)
        if item_id is None:
            missing.append(citekey)
            continue
        for target in targets:
            collection_id = COLLECTIONS[target]
            exists = conn.execute(
                "SELECT 1 FROM collectionItems WHERE collectionID = ? AND itemID = ?",
                (collection_id, item_id),
            ).fetchone()
            if exists:
                continue
            conn.execute(
                "INSERT INTO collectionItems (collectionID, itemID, orderIndex) VALUES (?, ?, 0)",
                (collection_id, item_id),
            )
            inserted += 1
    return inserted, missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Assign cleaned Zotero citekeys to thematic subcollections.")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--restart-zotero", action="store_true")
    args = parser.parse_args()

    log(f"Planned citekeys to sort: {len(CITEKEY_COLLECTIONS)}")
    if not args.apply:
        log("Dry run only; no DB changes applied")
        return 0

    if args.restart_zotero:
        quit_zotero()
    backup = backup_db()
    log(f"DB backup written to {backup}")

    conn = sqlite3.connect(ZOTERO_DB)
    conn.row_factory = sqlite3.Row
    try:
        with conn:
            inserted, missing = assign_collections(conn)
    finally:
        conn.close()

    log(f"Inserted collection memberships: {inserted}")
    if missing:
        log("Missing citekeys: " + ", ".join(sorted(missing)))

    if args.restart_zotero:
        launch_zotero()
        wait_for_connector()

    log("Subcollection assignment applied successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
