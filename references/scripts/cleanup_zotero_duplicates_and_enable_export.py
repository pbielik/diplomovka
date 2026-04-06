#!/usr/bin/env python3

import argparse
import json
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
HOME = Path.home()
ZOTERO_DB = HOME / "Zotero" / "zotero.sqlite"
PREFS_JS = HOME / "Library/Application Support/Zotero/Profiles/0gav47l8.default/prefs.js"
BACKUP_DIR = Path("/tmp") / "codex-zotero-cleanup-backups"
FINAL_EXPORT = REPO_ROOT / "references" / "zotero-thesis.bib"
SEED_EXPORT = REPO_ROOT / "references" / "zotero-thesis-seed.bib"
BBT_TRANSLATOR_ID = "ca65189f-8815-4afe-8c8b-8c7c15f0edca"
COLLECTION_ID = 1


RENAME_KEYS = {
    "NR8JE3V3": "omar2024llmpsychiatry",
    "ICESGW9A": "guo2024llmmentalhealth",
}

TRASH_KEYS = [
    "X7GHXN4U",  # yu old uppercase citekey variant
    "TL4ZJLUJ",  # omar duplicate
    "SPJLL9I7",  # jin duplicate with bad citekey
    "32KLBQBZ",  # li duplicate suffix variant
    "P8MG7A4T",  # beck duplicate publisher import
]


def log(message: str) -> None:
    print(message, file=sys.stderr)


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


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


def backup_files() -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = BACKUP_DIR / stamp
    target.mkdir()
    shutil.copy2(ZOTERO_DB, target / "zotero.sqlite")
    wal = ZOTERO_DB.with_name("zotero.sqlite-wal")
    shm = ZOTERO_DB.with_name("zotero.sqlite-shm")
    if wal.exists():
        shutil.copy2(wal, target / "zotero.sqlite-wal")
    if shm.exists():
        shutil.copy2(shm, target / "zotero.sqlite-shm")
    shutil.copy2(PREFS_JS, target / "prefs.js")
    return target


def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(ZOTERO_DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def get_item_id(conn: sqlite3.Connection, key: str) -> int | None:
    row = conn.execute("SELECT itemID FROM items WHERE key = ?", (key,)).fetchone()
    return int(row["itemID"]) if row else None


def get_value_id(conn: sqlite3.Connection, value: str) -> int:
    row = conn.execute("SELECT valueID FROM itemDataValues WHERE value = ?", (value,)).fetchone()
    if row:
        return int(row["valueID"])
    conn.execute("INSERT INTO itemDataValues (value) VALUES (?)", (value,))
    row = conn.execute("SELECT valueID FROM itemDataValues WHERE value = ?", (value,)).fetchone()
    return int(row["valueID"])


def upsert_item_field(conn: sqlite3.Connection, item_id: int, field_id: int, value: str) -> None:
    value_id = get_value_id(conn, value)
    existing = conn.execute(
        "SELECT valueID FROM itemData WHERE itemID = ? AND fieldID = ?",
        (item_id, field_id),
    ).fetchone()
    if existing:
        conn.execute(
            "UPDATE itemData SET valueID = ? WHERE itemID = ? AND fieldID = ?",
            (value_id, item_id, field_id),
        )
    else:
        conn.execute(
            "INSERT INTO itemData (itemID, fieldID, valueID) VALUES (?, ?, ?)",
            (item_id, field_id, value_id),
        )


def mark_item_changed(conn: sqlite3.Connection, item_id: int) -> None:
    conn.execute(
        """
        UPDATE items
        SET dateModified = ?, clientDateModified = ?, version = version + 1, synced = 0
        WHERE itemID = ?
        """,
        (now_utc(), now_utc(), item_id),
    )


def trash_item(conn: sqlite3.Connection, item_key: str) -> None:
    item_id = get_item_id(conn, item_key)
    if item_id is None:
        log(f"Skip trash for missing item key {item_key}")
        return
    already = conn.execute("SELECT 1 FROM deletedItems WHERE itemID = ?", (item_id,)).fetchone()
    if not already:
        conn.execute("INSERT INTO deletedItems (itemID) VALUES (?)", (item_id,))
    mark_item_changed(conn, item_id)


def ensure_citation_key_available(conn: sqlite3.Connection, citekey: str, own_item_key: str) -> None:
    rows = conn.execute(
        """
        SELECT i.key
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID
        JOIN itemDataValues v ON v.valueID = d.valueID
        LEFT JOIN deletedItems di ON di.itemID = i.itemID
        WHERE d.fieldID = 9 AND v.value = ? AND di.itemID IS NULL
        """,
        (citekey,),
    ).fetchall()
    conflicts = [row["key"] for row in rows if row["key"] != own_item_key]
    if conflicts:
        raise RuntimeError(f"Cannot assign citekey {citekey}; already used by {', '.join(conflicts)}")


def rename_item_citekey(conn: sqlite3.Connection, item_key: str, new_citekey: str) -> None:
    item_id = get_item_id(conn, item_key)
    if item_id is None:
        raise RuntimeError(f"Missing item key {item_key} for citekey rename")
    ensure_citation_key_available(conn, new_citekey, item_key)
    upsert_item_field(conn, item_id, 9, new_citekey)
    upsert_item_field(conn, item_id, 19, f"Citation Key: {new_citekey}")
    mark_item_changed(conn, item_id)


def update_prefs_js() -> None:
    raw = PREFS_JS.read_text(encoding="utf-8")
    encoded = urllib.parse.quote(str(FINAL_EXPORT), safe="").replace(".", "%2e")
    pref_key = f'extensions.zotero.translators.better-bibtex.autoExport.{encoded}'
    payload = {
        "created": int(time.time() * 1000),
        "path": str(FINAL_EXPORT),
        "translatorID": BBT_TRANSLATOR_ID,
        "type": "collection",
        "id": COLLECTION_ID,
        "status": "done",
        "error": "",
        "recursive": False,
        "updated": int(time.time() * 1000),
        "enabled": True,
        "bibtexURL": "off",
        "DOIandURL": "both",
        "exportNotes": False,
        "useJournalAbbreviation": False,
    }
    pref_line = f'user_pref("{pref_key}", {json.dumps(json.dumps(payload))});'
    if pref_key in raw:
        raw = "\n".join(
            pref_line if line.startswith(f'user_pref("{pref_key}",') else line
            for line in raw.splitlines()
        ) + "\n"
    else:
        if not raw.endswith("\n"):
            raw += "\n"
        raw += pref_line + "\n"
    PREFS_JS.write_text(raw, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Cleanup Zotero duplicates and add final BBT export target.")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--restart-zotero", action="store_true")
    args = parser.parse_args()

    log("Planned citekey renames:")
    for item_key, citekey in RENAME_KEYS.items():
        log(f"- {item_key} -> {citekey}")
    log("Planned trash moves:")
    for item_key in TRASH_KEYS:
        log(f"- {item_key}")
    log(f"Planned final export target: {FINAL_EXPORT}")

    if not args.apply:
        log("Dry run only; no changes applied")
        return 0

    if args.restart_zotero:
        quit_zotero()
    backup_path = backup_files()
    log(f"Backup written to {backup_path}")

    conn = connect_db()
    try:
        with conn:
            for item_key, citekey in RENAME_KEYS.items():
                rename_item_citekey(conn, item_key, citekey)
            for item_key in TRASH_KEYS:
                trash_item(conn, item_key)
    finally:
        conn.close()

    update_prefs_js()

    if args.restart_zotero:
        launch_zotero()
        wait_for_connector()

    log("Cleanup applied successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
