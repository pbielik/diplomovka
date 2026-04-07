#!/usr/bin/env python3

import argparse
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


HOME = Path.home()
DEFAULT_DB = Path("/tmp") / "zotero-live-current.sqlite"
ZOTERO_STORAGE = HOME / "Zotero" / "storage"

TARGET_CITEKEYS = [
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
]

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


def log(message: str) -> None:
    print(message, file=sys.stderr)


def priority_for(citekey: str) -> str:
    if citekey in MUST_READ:
        return "must-read"
    if citekey in OPTIONAL:
        return "optional"
    return "should-read"


def attachment_abs_path(attachment_key: str, db_path: str | None) -> str | None:
    if not attachment_key or not db_path:
        return None
    if db_path.startswith("storage:"):
        return str(ZOTERO_STORAGE / attachment_key / db_path.removeprefix("storage:"))
    return db_path


def classify(rows: list[sqlite3.Row]) -> tuple[str, list[dict[str, str]]]:
    if not rows:
        return "missing", []

    attachments: list[dict[str, str]] = []
    has_existing_pdf = False
    has_existing_snapshot = False
    has_broken = False

    for row in rows:
        attachment_key = row["attachment_key"]
        content_type = row["content_type"] or ""
        db_path = row["path"]
        abs_path = attachment_abs_path(attachment_key, db_path)
        exists = bool(abs_path and Path(abs_path).exists())
        attachments.append(
            {
                "attachment_key": attachment_key or "",
                "content_type": content_type,
                "db_path": db_path or "",
                "abs_path": abs_path or "",
                "exists": "yes" if exists else "no",
            }
        )
        if exists and content_type == "application/pdf":
            has_existing_pdf = True
        elif exists and (content_type.startswith("text/html") or abs_path.endswith("index.html")):
            has_existing_snapshot = True
        elif not exists:
            has_broken = True

    if has_existing_pdf:
        return "pdf", attachments
    if has_existing_snapshot:
        return "snapshot", attachments
    if has_broken:
        return "db-only-broken", attachments
    return "missing", attachments


def load_status(db: Path) -> list[dict[str, object]]:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    try:
        placeholders = ",".join("?" for _ in TARGET_CITEKEYS)
        rows = conn.execute(
            f"""
            SELECT parent.value AS citekey,
                   p.key AS parent_key,
                   a.key AS attachment_key,
                   ia.contentType AS content_type,
                   ia.path AS path
            FROM itemData d
            JOIN itemDataValues parent ON parent.valueID = d.valueID
            JOIN items p ON p.itemID = d.itemID
            LEFT JOIN itemAttachments ia ON ia.parentItemID = p.itemID
            LEFT JOIN items a ON a.itemID = ia.itemID
            WHERE d.fieldID = 9
              AND parent.value IN ({placeholders})
            ORDER BY parent.value, ia.itemID
            """,
            TARGET_CITEKEYS,
        ).fetchall()
    finally:
        conn.close()

    grouped: dict[str, list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        if row["attachment_key"] is not None:
            grouped[str(row["citekey"])].append(row)
        else:
            grouped.setdefault(str(row["citekey"]), [])

    result: list[dict[str, object]] = []
    for citekey in TARGET_CITEKEYS:
        grouped_rows = grouped.get(citekey, [])
        status, attachments = classify(grouped_rows)
        result.append(
            {
                "citekey": citekey,
                "priority": priority_for(citekey),
                "status": status,
                "attachments": attachments,
            }
        )
    return result


def render_markdown(status_rows: list[dict[str, object]], db: Path) -> str:
    pdf_count = sum(1 for row in status_rows if row["status"] == "pdf")
    snapshot_count = sum(1 for row in status_rows if row["status"] == "snapshot")
    missing_count = sum(1 for row in status_rows if row["status"] == "missing")
    broken_count = sum(1 for row in status_rows if row["status"] == "db-only-broken")

    snapshot_ts = datetime.fromtimestamp(db.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Fulltext checklist pre Zotero attachments",
        "",
        f"> Snapshot dátum: {snapshot_ts}",
        f"> Zdroj stavu: `{db}`",
        "",
        "## Rýchly súhrn",
        "",
        f"- core citekey-ready corpus: `{len(status_rows)}` zdrojov",
        f"- zdroje s lokálnym `PDF`: `{pdf_count}`",
        f"- zdroje s lokálnym `snapshotom`: `{snapshot_count}`",
        f"- zdroje bez attachmentu: `{missing_count}`",
        f"- zdroje s rozbitým DB attachmentom bez lokálneho súboru: `{broken_count}`",
        "",
    ]

    for priority in ["must-read", "should-read", "optional"]:
        subset = [row for row in status_rows if row["priority"] == priority and row["status"] != "pdf"]
        if not subset:
            continue
        lines.extend(
            [
                f"## {priority.upper()} bez lokálneho PDF",
                "",
                "| Citekey | Stav | Poznámka |",
                "| --- | --- | --- |",
            ]
        )
        for row in subset:
            note = "pridať snapshot alebo PDF" if row["status"] == "snapshot" else "doplniť attachment"
            if row["status"] == "db-only-broken":
                note = "DB attachment existuje, ale lokálny súbor chýba"
            lines.append(f"| `{row['citekey']}` | `{row['status']}` | {note} |")
        lines.append("")

    lines.extend(["## Už pokryté lokálnym PDF", ""])
    for row in status_rows:
        if row["status"] == "pdf":
            lines.append(f"- `{row['citekey']}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report local PDF/snapshot coverage for core Zotero citekeys.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--write-markdown", type=Path)
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"DB snapshot not found: {args.db}")

    status_rows = load_status(args.db)
    markdown = render_markdown(status_rows, args.db)

    if args.write_markdown:
        args.write_markdown.write_text(markdown + "\n", encoding="utf-8")
        log(f"Wrote markdown report to {args.write_markdown}")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
