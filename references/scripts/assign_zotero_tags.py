#!/usr/bin/env python3

import argparse
import shutil
import sqlite3
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path


HOME = Path.home()
ZOTERO_DB = HOME / "Zotero" / "zotero.sqlite"
BACKUP_DIR = Path("/tmp") / "codex-zotero-tagging"


MUST_READ = {
    "obradovich2024llmpsychiatry",
    "ajluni2025psychiatriceducation",
    "yu2025simulatedpatientsystems",
    "evans2015vignettes",
    "kennedy2008coresymptoms",
    "maj2020depressioncharacterization",
    "kroenke2001phq9",
    "guidi2011clinicalinterviewdepression",
    "roustan2025cliniciansguide",
    "asgari2025hallucinationframework",
    "mcintyre2019mddvsbipolar",
    "polit2007cvi",
    "boateng2018scaledevelopment",
    "terwee2018COSMINMethodologyEvaluating",
    "kononowicz2019virtualpatients",
    "who2021ethicsaiforhealth",
    "jakobsson2005ordinalagreement",
    "nelson2015manyratersordinal",
}

OPTIONAL = {
    "baguley2022vignettedata",
    "dawood2024standardizedpatient",
    "hirschfeld2014bipolardifferential",
    "stein2021anxietycharacterization",
    "marasini2016weightedindexes",
    "mitani2017ordinalsummarymeasures",
}

TOPICAL_TAGS = {
    "llm": {
        "obradovich2024llmpsychiatry",
        "meng2024llmmedicine",
        "ajluni2025psychiatriceducation",
        "yu2025simulatedpatientsystems",
        "brugge2024patientsimulation",
        "williams2017simulationmentalhealth",
        "dawood2024standardizedpatient",
        "roustan2025cliniciansguide",
        "asgari2025hallucinationframework",
        "cook2010computerizedvirtualpatients",
        "kononowicz2019virtualpatients",
        "who2024lmmguidance",
        "howell2024genaipatientsafety",
        "khera2023automationbiasassistiveai",
        "omar2024llmpsychiatry",
        "guo2024llmmentalhealth",
    },
    "depression": {
        "kennedy2008coresymptoms",
        "maj2020depressioncharacterization",
        "kroenke2001phq9",
        "guidi2011clinicalinterviewdepression",
        "mcintyre2019mddvsbipolar",
        "hirschfeld2014bipolardifferential",
        "stein2021anxietycharacterization",
        "dubovsky2021psychoticdepression",
    },
    "validation": {
        "lynn1986contentvalidity",
        "polit2007cvi",
        "hasson2000delphi",
        "boateng2018scaledevelopment",
        "rutherfordhemming2015simulationcvi",
        "terwee2018COSMINMethodologyEvaluating",
    },
    "methods": {
        "evans2015vignettes",
        "baguley2022vignettedata",
        "brugge2024patientsimulation",
        "williams2017simulationmentalhealth",
        "dawood2024standardizedpatient",
        "lynn1986contentvalidity",
        "polit2007cvi",
        "hasson2000delphi",
        "boateng2018scaledevelopment",
        "rutherfordhemming2015simulationcvi",
        "cook2010computerizedvirtualpatients",
        "kononowicz2019virtualpatients",
        "mchugh2012kappa",
        "jakobsson2005ordinalagreement",
        "marasini2016weightedindexes",
        "nelson2015manyratersordinal",
        "mitani2017ordinalsummarymeasures",
        "terwee2018COSMINMethodologyEvaluating",
    },
    "ethics": {
        "roustan2025cliniciansguide",
        "asgari2025hallucinationframework",
        "who2021ethicsaiforhealth",
        "who2024lmmguidance",
        "goddard2012automationbias",
        "howell2024genaipatientsafety",
        "khera2023automationbiasassistiveai",
    },
    "analysis": {
        "mchugh2012kappa",
        "jakobsson2005ordinalagreement",
        "marasini2016weightedindexes",
        "nelson2015manyratersordinal",
        "mitani2017ordinalsummarymeasures",
    },
}

SEEDING = {
    "obradovich2024llmpsychiatry",
    "meng2024llmmedicine",
    "ajluni2025psychiatriceducation",
    "yu2025simulatedpatientsystems",
    "brugge2024patientsimulation",
    "evans2015vignettes",
    "baguley2022vignettedata",
    "williams2017simulationmentalhealth",
    "dawood2024standardizedpatient",
    "kennedy2008coresymptoms",
    "maj2020depressioncharacterization",
    "kroenke2001phq9",
    "guidi2011clinicalinterviewdepression",
    "roustan2025cliniciansguide",
    "asgari2025hallucinationframework",
    "mcintyre2019mddvsbipolar",
    "hirschfeld2014bipolardifferential",
    "stein2021anxietycharacterization",
    "dubovsky2021psychoticdepression",
    "lynn1986contentvalidity",
    "polit2007cvi",
    "hasson2000delphi",
    "boateng2018scaledevelopment",
    "rutherfordhemming2015simulationcvi",
    "cook2010computerizedvirtualpatients",
    "kononowicz2019virtualpatients",
    "who2021ethicsaiforhealth",
    "who2024lmmguidance",
    "goddard2012automationbias",
    "howell2024genaipatientsafety",
    "khera2023automationbiasassistiveai",
    "mchugh2012kappa",
    "jakobsson2005ordinalagreement",
    "marasini2016weightedindexes",
    "nelson2015manyratersordinal",
    "mitani2017ordinalsummarymeasures",
    "omar2024llmpsychiatry",
    "guo2024llmmentalhealth",
    "terwee2018COSMINMethodologyEvaluating",
}


TARGET_CITEKEYS = set().union(MUST_READ, OPTIONAL, SEEDING, *TOPICAL_TAGS.values())
SHOULD_READ = TARGET_CITEKEYS - MUST_READ - OPTIONAL


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
    last_error: subprocess.CalledProcessError | None = None
    for _ in range(10):
        try:
            subprocess.run(["open", "-a", "Zotero"], check=True, capture_output=True, text=True)
            return
        except subprocess.CalledProcessError as error:
            last_error = error
            time.sleep(1)
    assert last_error is not None
    raise last_error


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
    return {str(row["citekey"]): int(row["itemID"]) for row in rows}


def build_tag_map() -> dict[str, set[str]]:
    tag_map = {citekey: {"seeding"} for citekey in TARGET_CITEKEYS}
    for citekey in MUST_READ:
        tag_map[citekey].add("must-read")
    for citekey in OPTIONAL:
        tag_map[citekey].add("optional")
    for citekey in SHOULD_READ:
        tag_map[citekey].add("should-read")
    for tag_name, citekeys in TOPICAL_TAGS.items():
        for citekey in citekeys:
            tag_map[citekey].add(tag_name)
    return tag_map


def ensure_tag_id(conn: sqlite3.Connection, tag_name: str) -> tuple[int, bool]:
    existing = conn.execute("SELECT tagID FROM tags WHERE name = ?", (tag_name,)).fetchone()
    if existing:
        return int(existing["tagID"]), False
    cursor = conn.execute("INSERT INTO tags (name) VALUES (?)", (tag_name,))
    return int(cursor.lastrowid), True


def assign_tags(conn: sqlite3.Connection) -> tuple[int, list[str], Counter[str], int]:
    citekey_to_item = get_item_ids_by_citekey(conn)
    tag_map = build_tag_map()
    tag_ids: dict[str, int] = {}
    created_tags = 0
    for tag_name in sorted({tag for tags in tag_map.values() for tag in tags}):
        tag_id, created = ensure_tag_id(conn, tag_name)
        tag_ids[tag_name] = tag_id
        if created:
            created_tags += 1

    inserted = 0
    missing: list[str] = []
    applied_counter: Counter[str] = Counter()
    for citekey, tags in sorted(tag_map.items()):
        item_id = citekey_to_item.get(citekey)
        if item_id is None:
            missing.append(citekey)
            continue
        for tag_name in sorted(tags):
            tag_id = tag_ids[tag_name]
            exists = conn.execute(
                "SELECT 1 FROM itemTags WHERE itemID = ? AND tagID = ?",
                (item_id, tag_id),
            ).fetchone()
            if exists:
                continue
            conn.execute(
                "INSERT INTO itemTags (itemID, tagID, type) VALUES (?, ?, 0)",
                (item_id, tag_id),
            )
            inserted += 1
            applied_counter[tag_name] += 1
    return inserted, missing, applied_counter, created_tags


def main() -> int:
    parser = argparse.ArgumentParser(description="Assign manual thesis tags to core Zotero citekeys.")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--restart-zotero", action="store_true")
    args = parser.parse_args()

    log(f"Target citekeys for manual tagging: {len(TARGET_CITEKEYS)}")
    log("Manual thesis tags: must-read, should-read, optional, methods, validation, ethics, llm, depression, seeding, analysis")

    if args.restart_zotero:
        quit_zotero()

    if args.apply:
        backup = backup_db()
        log(f"DB backup written to {backup}")

    conn = sqlite3.connect(ZOTERO_DB)
    conn.row_factory = sqlite3.Row
    try:
        if not args.apply:
            missing = sorted(TARGET_CITEKEYS - set(get_item_ids_by_citekey(conn)))
            log(f"Missing citekeys for dry run: {len(missing)}")
            if missing:
                log(", ".join(missing))
            log("Dry run only; no DB changes applied")
            return 0
        with conn:
            inserted, missing, applied_counter, created_tags = assign_tags(conn)
    finally:
        conn.close()

    log(f"Created manual tag records: {created_tags}")
    log(f"Inserted item-tag memberships: {inserted}")
    if missing:
        log("Missing citekeys: " + ", ".join(missing))
    for tag_name in sorted(applied_counter):
        log(f"{tag_name}: +{applied_counter[tag_name]}")

    if args.restart_zotero:
        launch_zotero()
        wait_for_connector()

    log("Tag assignment applied successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
