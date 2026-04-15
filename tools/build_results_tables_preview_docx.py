#!/usr/bin/env python3
"""
Generate a native DOCX preview for thesis-style results tables.

Goals:
- captions above tables ("Tabuľka X")
- italicized caption titles
- centered tables with narrower width than the page text block
- horizontal rules only, no vertical borders

This uses direct OOXML packaging so Word preserves the intended layout.
"""

from __future__ import annotations

import csv
import math
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


REPO_ROOT = Path(__file__).resolve().parents[1]
TABLES_DIR = REPO_ROOT / "tables"
PREVIEW_DIR = TABLES_DIR / "styled_preview"
OUTPUT_DOCX = PREVIEW_DIR / "results_tables_preview.docx"
CODEBOOK_PATH = REPO_ROOT / "analysis" / "codebook_rating_study.csv"

PAGE_WIDTH_DXA = 11907
PAGE_HEIGHT_DXA = 16840
MARGIN_DXA = 1440
TEXT_WIDTH_DXA = PAGE_WIDTH_DXA - 2 * MARGIN_DXA

HEADER_LABELS = {
    "metric": "Ukazovateľ",
    "value": "Hodnota",
    "block": "Blok",
    "n_items": "Počet položiek",
    "n_rows": "Počet riadkov",
    "alpha": "Cronbachovo α",
    "omega": "McDonaldovo ω",
    "status": "Stav",
    "detail": "Poznámka",
    "outcome": "Ukazovateľ",
    "icc_type": "Typ ICC",
    "estimate": "Odhad",
    "conf_low": "95 % CI dolná",
    "conf_high": "95 % CI horná",
    "model_family": "Model",
}

TABLE_1_METRIC_LABELS = {
    "source_mode": "Zdroj dát",
    "n_raters": "Počet hodnotiteľov",
    "n_transcripts": "Počet transkriptov",
    "n_seeds": "Počet seedov",
    "n_ratings": "Počet hodnotení",
    "mean_ratings_per_transcript": "Priemerný počet hodnotení na transkript",
    "min_ratings_per_transcript": "Minimálny počet hodnotení na transkript",
    "max_ratings_per_transcript": "Maximálny počet hodnotení na transkript",
    "severity_error_mode": "Režim výpočtu chyby závažnosti",
    "guardrail_off": "Počet hodnotení bez guardrailu",
    "guardrail_on": "Počet hodnotení s guardrailom",
    "profile_R1": "Počet hodnotení pre profil P1",
    "profile_R2": "Počet hodnotení pre profil P2",
    "profile_R3": "Počet hodnotení pre profil P3",
    "guardrail_off_profile_R1": "Bez guardrailu × profil P1",
    "guardrail_off_profile_R2": "Bez guardrailu × profil P2",
    "guardrail_off_profile_R3": "Bez guardrailu × profil P3",
    "guardrail_on_profile_R1": "S guardrailom × profil P1",
    "guardrail_on_profile_R2": "S guardrailom × profil P2",
    "guardrail_on_profile_R3": "S guardrailom × profil P3",
}

BLOCK_LABELS = {
    "g1_g5": "Blok G1-G5",
    "plausibility_core": "Jadro klinickej vierohodnosti",
    "r1_r5": "Blok R1-R5",
}

STATUS_LABELS = {
    "ok": "OK",
    "skipped": "Preskočené",
    "failed": "Chyba",
}

DETAIL_LABELS = {
    "Alpha estimated; omega failed.": "Cronbachovo α bolo odhadnuté; McDonaldovo ω sa nepodarilo vypočítať.",
    "Need at least 2 transcripts and 2 raters for ICC.": "Pre ICC treba aspoň 2 transkripty a 2 hodnotiteľov.",
    "Insufficient rows or factor levels for LMM.": "Nedostatok riadkov alebo úrovní faktorov pre LMM.",
    "Insufficient transcript rows or factor levels for transcript-level LMM.": "Nedostatok transkriptových riadkov alebo úrovní faktorov pre transcript-level LMM.",
    "Insufficient rows, levels or response variation for CLMM.": "Nedostatok riadkov, úrovní alebo variability odpovedí pre CLMM.",
}

SOURCE_MODE_LABELS = {
    "data_clean": "Clean dáta",
    "templates_smoke_run": "Template smoke-run",
}

MODEL_FAMILY_LABELS = {
    "lmm": "LMM",
    "clmm": "CLMM",
}


def normalize_key(value: str) -> str:
    return value.strip().lower()


def load_codebook_labels() -> dict[str, str]:
    labels: dict[str, str] = {}
    with CODEBOOK_PATH.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            variable = normalize_key(row["variable"])
            labels[variable] = row["label"].strip()
    return labels


CODEBOOK_LABELS = load_codebook_labels()


def xml_text(value: str) -> str:
    return escape(value, {'"': "&quot;"})


def format_value(value: str) -> str:
    if value is None:
        return ""
    value = value.strip()
    if not value or value.lower() == "na":
        return ""
    try:
        numeric = float(value)
    except ValueError:
        return value

    if math.isinf(numeric):
        return "-Inf" if numeric < 0 else "Inf"
    rounded = round(numeric, 3)
    if rounded.is_integer():
        return str(int(rounded))
    return f"{rounded:.3f}".rstrip("0").rstrip(".")


def read_csv(path: Path, limit_rows: int | None = None) -> list[list[str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if limit_rows is None:
        return rows
    return rows[: limit_rows + 1]


def prettify_header(header: str) -> str:
    return HEADER_LABELS.get(header, header.replace("_", " "))


def prettify_cell(value: str, *, column: str, table_id: str) -> str:
    key = normalize_key(value)

    if table_id == "table_1" and column == "metric":
        return TABLE_1_METRIC_LABELS.get(value, value.replace("_", " "))
    if table_id == "table_1" and column == "value":
        return SOURCE_MODE_LABELS.get(key, value)
    if table_id == "table_4" and column == "block":
        return BLOCK_LABELS.get(key, value)
    if column == "outcome":
        return CODEBOOK_LABELS.get(key, value)
    if column == "status":
        return STATUS_LABELS.get(key, value)
    if column == "detail":
        return DETAIL_LABELS.get(value, value)
    if column == "model_family":
        return MODEL_FAMILY_LABELS.get(key, value.upper())
    if column == "icc_type":
        return value.upper()

    return value


def column_alignment(column: str) -> str:
    return "right" if column in {"value", "n_items", "n_rows", "alpha", "omega", "estimate", "conf_low", "conf_high"} else "left"


def preview_table_6(path: Path) -> list[list[str]]:
    rows = read_csv(path)
    if not rows:
        return [["Bez údajov"]]

    header = rows[0]
    wanted = ["outcome", "model_family", "estimate", "conf_low", "conf_high", "status"]
    indices = [header.index(name) for name in wanted if name in header]
    preview_rows = [[header[idx] for idx in indices]]
    for row in rows[1:9]:
      preview_rows.append([row[idx] if idx < len(row) else "" for idx in indices])
    return preview_rows


def make_paragraph(text: str, *, bold: bool = False, italic: bool = False, align: str = "left", after: int = 120, size: int = 24) -> str:
    jc = {"left": "left", "center": "center", "right": "right"}[align]
    rpr = []
    if bold:
        rpr.append("<w:b/>")
        rpr.append("<w:bCs/>")
    if italic:
        rpr.append("<w:i/>")
        rpr.append("<w:iCs/>")
    rpr.append(f'<w:sz w:val="{size}"/>')
    rpr.append(f'<w:szCs w:val="{size}"/>')

    return (
        '<w:p>'
        f'<w:pPr><w:jc w:val="{jc}"/><w:spacing w:after="{after}" w:line="276" w:lineRule="auto"/></w:pPr>'
        '<w:r>'
        f'<w:rPr>{"".join(rpr)}</w:rPr>'
        f'<w:t xml:space="preserve">{xml_text(text)}</w:t>'
        '</w:r>'
        '</w:p>'
    )


def make_note_paragraph(text: str) -> str:
    return (
        '<w:p>'
        '<w:pPr><w:jc w:val="left"/><w:spacing w:after="180" w:line="240" w:lineRule="auto"/></w:pPr>'
        '<w:r>'
        '<w:rPr><w:i/><w:iCs/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr>'
        '<w:t xml:space="preserve">Poznámka. </w:t>'
        '</w:r>'
        '<w:r>'
        '<w:rPr><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr>'
        f'<w:t xml:space="preserve">{xml_text(text)}</w:t>'
        '</w:r>'
        '</w:p>'
    )


def compute_widths(column_count: int, table_width: int) -> list[int]:
    if column_count == 1:
        return [table_width]
    if column_count == 2:
        return [int(table_width * 0.62), table_width - int(table_width * 0.62)]
    if column_count == 3:
        first = int(table_width * 0.42)
        rest = (table_width - first) // 2
        return [first, rest, table_width - first - rest]
    if column_count == 6:
        return [1900, 1300, 1000, 1000, 1000, table_width - 6200]

    first = int(table_width * 0.28)
    remaining = table_width - first
    each = remaining // (column_count - 1)
    widths = [first] + [each] * (column_count - 1)
    widths[-1] += table_width - sum(widths)
    return widths


def make_table(rows: list[list[str]], table_width: int, *, table_id: str, widths_override: list[int] | None = None) -> str:
    normalized = [[format_value(cell) for cell in row] for row in rows]
    column_count = max(len(row) for row in normalized)
    normalized = [row + [""] * (column_count - len(row)) for row in normalized]
    widths = widths_override if widths_override is not None else compute_widths(column_count, table_width)

    grid = "".join(f'<w:gridCol w:w="{width}"/>' for width in widths)

    rights = []
    current = 0
    for width in widths:
        current += width
        rights.append(current)

    table = [
        '<w:tbl>',
        '<w:tblPr>',
        f'<w:tblW w:w="{table_width}" w:type="dxa"/>',
        '<w:jc w:val="center"/>',
        '<w:tblLayout w:type="fixed"/>',
        '<w:tblCellMar><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar>',
        '<w:tblBorders>',
        '<w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/><w:right w:val="nil"/>',
        '<w:insideH w:val="nil"/><w:insideV w:val="nil"/>',
        '</w:tblBorders>',
        '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>',
        '</w:tblPr>',
        f'<w:tblGrid>{grid}</w:tblGrid>',
    ]

    for row_idx, row in enumerate(normalized):
        is_header = row_idx == 0
        is_last = row_idx == len(normalized) - 1
        table.append('<w:tr>')
        for col_idx, cell in enumerate(row):
            column_name = normalized[0][col_idx]
            align = column_alignment(column_name)
            display_value = prettify_header(cell) if is_header else prettify_cell(cell, column=column_name, table_id=table_id)
            cell_text = xml_text(display_value)
            top_border = '<w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>' if is_header else '<w:top w:val="nil"/>'
            bottom_border = (
                '<w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
                if is_header or is_last
                else '<w:bottom w:val="nil"/>'
            )
            para = (
                '<w:p>'
                f'<w:pPr><w:jc w:val="{align}"/><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
                '<w:r>'
                + (
                    '<w:rPr><w:b/><w:bCs/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>'
                    if row_idx == 0
                    else '<w:rPr><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr>'
                )
                + f'<w:t xml:space="preserve">{cell_text}</w:t>'
                '</w:r>'
                '</w:p>'
            )
            table.append(
                '<w:tc>'
                '<w:tcPr>'
                f'<w:tcW w:w="{widths[col_idx]}" w:type="dxa"/>'
                '<w:tcBorders>'
                f'{top_border}<w:left w:val="nil"/>{bottom_border}<w:right w:val="nil"/>'
                '</w:tcBorders>'
                '</w:tcPr>'
                + para +
                '</w:tc>'
            )
        table.append('</w:tr>')

    table.append('</w:tbl>')
    table.append(make_paragraph("", after=180))
    return "".join(table)


def build_document_xml() -> str:
    specs = [
        {
            "label": "Tabuľka 1",
            "title": "Základná charakteristika datasetu",
            "rows": read_csv(TABLES_DIR / "table_1_dataset_summary.csv", limit_rows=12),
            "width": 7000,
            "column_widths": [4400, 2600],
            "table_id": "table_1",
        },
        {
            "label": "Tabuľka 4",
            "title": "Vnútorná konzistencia ratingových blokov",
            "rows": read_csv(TABLES_DIR / "table_4_internal_consistency.csv"),
            "width": 8600,
            "column_widths": [2600, 900, 900, 1000, 1100, 900, 2200],
            "table_id": "table_4",
            "note": "α = Cronbachovo α; ω = McDonaldovo ω. V tejto pilotnej ukážke sú koeficienty počítané z veľmi malého počtu hodnotení, preto ich treba interpretovať len orientačne.",
        },
        {
            "label": "Tabuľka 5",
            "title": "Interrater reliabilita hlavných outcome-ov",
            "rows": read_csv(TABLES_DIR / "table_5_icc.csv"),
            "width": 8600,
            "column_widths": [2400, 1000, 900, 900, 900, 1000, 1500],
            "table_id": "table_5",
            "note": "ICC = intratriedna korelácia; CI = interval spoľahlivosti. V aktuálnom preview sú odhady preskočené, pretože pilotné dáta zatiaľ neobsahujú aspoň dvoch hodnotiteľov pre aspoň dva transkripty.",
        },
        {
            "label": "Tabuľka 6",
            "title": "Súhrn jadrových zmiešaných modelov",
            "rows": preview_table_6(TABLES_DIR / "table_6_mixed_models_core.csv"),
            "width": 8400,
            "column_widths": [2800, 1100, 1000, 1000, 1000, 1500],
            "table_id": "table_6",
            "note": "LMM = lineárny zmiešaný model; CLMM = kumulatívny link mixed model; CI = interval spoľahlivosti. V aktuálnom preview sú modely preskočené pre nedostatočný počet riadkov alebo úrovní faktorov.",
        },
    ]

    body = [
        make_paragraph("Testovací preview výsledkových tabuliek", bold=True, align="center", after=180, size=32),
        make_paragraph(
            "Toto je nový natívny DOCX preview build. Tabuľky sú zámerne užšie než textový blok, sú centrované a používajú len horizontálne čiary.",
            after=220,
        ),
    ]

    for spec in specs:
        body.append(make_paragraph(spec["label"], bold=True, after=60))
        body.append(make_paragraph(spec["title"], italic=True, after=90))
        body.append(
            make_table(
                spec["rows"],
                spec["width"],
                table_id=spec["table_id"],
                widths_override=spec["column_widths"],
            )
        )
        if spec.get("note"):
            body.append(make_note_paragraph(spec["note"]))

    body_xml = "".join(body)
    sect = (
        f'<w:sectPr><w:pgSz w:w="{PAGE_WIDTH_DXA}" w:h="{PAGE_HEIGHT_DXA}" w:code="9"/>'
        f'<w:pgMar w:top="{MARGIN_DXA}" w:right="{MARGIN_DXA}" w:bottom="{MARGIN_DXA}" w:left="{MARGIN_DXA}" w:header="720" w:footer="720" w:gutter="0"/>'
        '<w:cols w:space="720"/><w:docGrid w:linePitch="360"/></w:sectPr>'
    )

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f'<w:body>{body_xml}{sect}</w:body></w:document>'
    )


def build_styles_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="24"/>
        <w:szCs w:val="24"/>
        <w:lang w:val="sk-SK"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:after="120" w:line="276" w:lineRule="auto"/>
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
  </w:style>
</w:styles>
"""


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""


PACKAGE_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""


DOCUMENT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""


def main() -> None:
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(OUTPUT_DOCX, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", PACKAGE_RELS)
        docx.writestr("word/document.xml", build_document_xml())
        docx.writestr("word/styles.xml", build_styles_xml())
        docx.writestr("word/_rels/document.xml.rels", DOCUMENT_RELS)

    print(OUTPUT_DOCX)


if __name__ == "__main__":
    main()
