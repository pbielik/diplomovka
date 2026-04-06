#!/usr/bin/env python3

import argparse
import json
import sqlite3
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / "references" / "zotero-thesis.bib"
BACKUP_ROOT = Path("/tmp") / "codex-zotero-cleanup-backups"
BBT_RPC_URL = "http://127.0.0.1:23119/better-bibtex/json-rpc"


def latest_backup_db() -> Path:
    candidates = sorted(BACKUP_ROOT.glob("*/zotero.sqlite"))
    if not candidates:
        raise FileNotFoundError(f"No cleanup backups found in {BACKUP_ROOT}")
    return candidates[-1]


def fetch_collection_citekeys(db_path: Path, collection_id: int) -> list[str]:
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute(
            """
            SELECT v.value
            FROM items i
            JOIN collectionItems c ON c.itemID = i.itemID
            JOIN itemData d ON d.itemID = i.itemID AND d.fieldID = 9
            JOIN itemDataValues v ON v.valueID = d.valueID
            LEFT JOIN deletedItems di ON di.itemID = i.itemID
            WHERE c.collectionID = ? AND di.itemID IS NULL
            ORDER BY v.value
            """,
            (collection_id,),
        ).fetchall()
    finally:
        conn.close()
    return [row[0] for row in rows]


def bbt_export(citekeys: list[str], translator: str = "Better BibTeX") -> str:
    payload = {
        "jsonrpc": "2.0",
        "method": "item.export",
        "params": [citekeys, translator],
        "id": "codex",
    }
    req = urllib.request.Request(
        BBT_RPC_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if "error" in body:
        raise RuntimeError(body["error"]["message"])
    return body["result"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export cleaned Zotero collection to Better BibTeX .bib")
    parser.add_argument("--db", type=Path, default=None, help="SQLite DB path to read citekeys from")
    parser.add_argument("--collection-id", type=int, default=1)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    db_path = args.db or latest_backup_db()
    citekeys = fetch_collection_citekeys(db_path, args.collection_id)
    if not citekeys:
        raise RuntimeError(f"No citekeys found for collection {args.collection_id}")
    bib = bbt_export(citekeys)
    args.output.write_text(bib, encoding="utf-8")
    print(f"Exported {len(citekeys)} citekeys to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
