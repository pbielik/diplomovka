#!/usr/bin/env python3

import argparse
import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


HOME = Path.home()
ZOTERO_DB = HOME / "Zotero" / "zotero.sqlite"
BACKUP_DIR = Path("/tmp") / "codex-zotero-root-sync"
ROOT_COLLECTION_ID = 1


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


def plan_missing_root_memberships(conn: sqlite3.Connection) -> list[int]:
    rows = conn.execute(
        """
        WITH RECURSIVE descendants(collectionID) AS (
            SELECT collectionID
            FROM collections
            WHERE parentCollectionID = ?
            UNION ALL
            SELECT c.collectionID
            FROM collections c
            JOIN descendants d ON c.parentCollectionID = d.collectionID
        )
        SELECT DISTINCT ci.itemID
        FROM collectionItems ci
        JOIN descendants d ON d.collectionID = ci.collectionID
        LEFT JOIN collectionItems rootci
            ON rootci.itemID = ci.itemID
           AND rootci.collectionID = ?
        LEFT JOIN deletedItems di ON di.itemID = ci.itemID
        LEFT JOIN itemAttachments ia ON ia.itemID = ci.itemID
        LEFT JOIN itemNotes ino ON ino.itemID = ci.itemID
        WHERE rootci.itemID IS NULL
          AND di.itemID IS NULL
          AND ia.itemID IS NULL
          AND ino.itemID IS NULL
        ORDER BY ci.itemID
        """,
        (ROOT_COLLECTION_ID, ROOT_COLLECTION_ID),
    ).fetchall()
    return [int(row["itemID"]) for row in rows]


def insert_root_memberships(conn: sqlite3.Connection, item_ids: list[int]) -> int:
    inserted = 0
    for item_id in item_ids:
        conn.execute(
            "INSERT INTO collectionItems (collectionID, itemID, orderIndex) VALUES (?, ?, 0)",
            (ROOT_COLLECTION_ID, item_id),
        )
        inserted += 1
    return inserted


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ensure every bibliographic item in subcollections also belongs to the root Zotero collection."
    )
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--restart-zotero", action="store_true")
    args = parser.parse_args()

    if args.restart_zotero:
        quit_zotero()

    backup = backup_db()
    log(f"DB backup written to {backup}")

    conn = sqlite3.connect(ZOTERO_DB)
    conn.row_factory = sqlite3.Row
    try:
        missing_item_ids = plan_missing_root_memberships(conn)
        log(f"Missing root memberships found: {len(missing_item_ids)}")
        if not args.apply:
            log("Dry run only; no DB changes applied")
            return 0
        with conn:
            inserted = insert_root_memberships(conn, missing_item_ids)
    finally:
        conn.close()

    log(f"Inserted root memberships: {inserted}")

    if args.restart_zotero:
        launch_zotero()
        wait_for_connector()

    log("Root collection sync applied successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
