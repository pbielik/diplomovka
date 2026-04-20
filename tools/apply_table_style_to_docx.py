#!/usr/bin/env python3
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

from docx_table_style import FINAL_TABLE_STYLE, TEXT_WIDTH_DXA


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}
STYLE = FINAL_TABLE_STYLE

ET.register_namespace("w", W_NS)


def qn(tag: str) -> str:
    return f"{{{W_NS}}}{tag}"


def make_element(tag: str, attrs: dict[str, str] | None = None) -> ET.Element:
    element = ET.Element(qn(tag))
    for key, value in (attrs or {}).items():
        element.set(qn(key), value)
    return element


def upsert(parent: ET.Element, child: ET.Element) -> None:
    for existing in parent.findall(child.tag):
        parent.remove(existing)
    parent.append(child)


def ensure_first_child(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(f"w:{tag}", NS)
    if child is None:
        child = ET.Element(qn(tag))
        parent.insert(0, child)
    return child


def table_width_dxa() -> int:
    return int(TEXT_WIDTH_DXA * STYLE.default_table_width_pct)


def scale_widths(widths: list[int], target_total: int) -> list[int]:
    if not widths:
        return []
    total = sum(widths)
    if total <= 0:
        even = target_total // len(widths)
        scaled = [even] * len(widths)
        scaled[-1] += target_total - sum(scaled)
        return scaled

    scaled = [max(1, round(width * target_total / total)) for width in widths]
    scaled[-1] += target_total - sum(scaled)
    return [int(width) for width in scaled]


def apply_table_properties(table: ET.Element) -> list[int]:
    table_pr = table.find("w:tblPr", NS)
    if table_pr is None:
        table_pr = ET.Element(qn("tblPr"))
        table.insert(0, table_pr)

    managed_tags = {
        qn("tblW"),
        qn("jc"),
        qn("tblLayout"),
        qn("tblCellMar"),
        qn("tblBorders"),
        qn("tblLook"),
    }
    kept_children = [child for child in list(table_pr) if child.tag not in managed_tags]
    table_pr[:] = kept_children

    widths = [
        int(col.get(qn("w"), "0"))
        for col in table.findall("./w:tblGrid/w:gridCol", NS)
    ]
    target_width = table_width_dxa()
    scaled_widths = scale_widths(widths, target_width) if widths else []

    new_children = [
        make_element("tblW", {"w": str(target_width), "type": "dxa"}),
        make_element("jc", {"val": "center"}),
        make_element("tblLayout", {"type": "fixed"}),
        make_element(
            "tblCellMar",
            {},
        ),
        make_element("tblBorders", {}),
        make_element(
            "tblLook",
            {
                "val": "04A0",
                "firstRow": "1",
                "lastRow": "0",
                "firstColumn": "1",
                "lastColumn": "0",
                "noHBand": "0",
                "noVBand": "1",
            },
        ),
    ]

    cell_margins = new_children[3]
    cell_margins.extend(
        [
            make_element("top", {"w": str(STYLE.cell_pad_top), "type": "dxa"}),
            make_element("left", {"w": str(STYLE.cell_pad_left), "type": "dxa"}),
            make_element("bottom", {"w": str(STYLE.cell_pad_bottom), "type": "dxa"}),
            make_element("right", {"w": str(STYLE.cell_pad_right), "type": "dxa"}),
        ]
    )

    table_borders = new_children[4]
    table_borders.extend(
        [
            make_element("top", {"val": "nil"}),
            make_element("left", {"val": "nil"}),
            make_element("bottom", {"val": "nil"}),
            make_element("right", {"val": "nil"}),
            make_element("insideH", {"val": "nil"}),
            make_element("insideV", {"val": "nil"}),
        ]
    )

    insert_at = 1 if kept_children and kept_children[0].tag == qn("tblStyle") else 0
    for offset, child in enumerate(new_children):
        table_pr.insert(insert_at + offset, child)

    grid = table.find("w:tblGrid", NS)
    if grid is not None and scaled_widths:
        grid_columns = grid.findall("w:gridCol", NS)
        for column, width in zip(grid_columns, scaled_widths):
            column.set(qn("w"), str(width))

    return scaled_widths


def set_cell_borders(cell_pr: ET.Element, *, is_header: bool, is_last_row: bool) -> None:
    borders = cell_pr.find("w:tcBorders", NS)
    if borders is None:
        borders = ET.SubElement(cell_pr, qn("tcBorders"))
    else:
        borders.clear()

    top_border = (
        make_element(
            "top",
            {
                "val": "single",
                "sz": str(STYLE.border_thick_sz),
                "space": "0",
                "color": STYLE.border_color,
            },
        )
        if is_header
        else make_element("top", {"val": "nil"})
    )
    bottom_border = (
        make_element(
            "bottom",
            {
                "val": "single",
                "sz": str(STYLE.border_mid_sz if is_header else STYLE.border_thick_sz),
                "space": "0",
                "color": STYLE.border_color,
            },
        )
        if is_header or is_last_row
        else make_element("bottom", {"val": "nil"})
    )

    borders.extend(
        [
            top_border,
            make_element("left", {"val": "nil"}),
            bottom_border,
            make_element("right", {"val": "nil"}),
        ]
    )


def set_paragraph_spacing(paragraph: ET.Element) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    spacing = make_element("spacing", {"after": "0", "line": "240", "lineRule": "auto"})
    upsert(paragraph_pr, spacing)


def set_run_style(run: ET.Element, *, is_header: bool) -> None:
    run_pr = ensure_first_child(run, "rPr")
    upsert(
        run_pr,
        make_element(
            "rFonts",
            {
                "ascii": STYLE.font_family,
                "hAnsi": STYLE.font_family,
                "cs": STYLE.font_family,
            },
        ),
    )
    font_size = STYLE.table_header_font_hp if is_header else STYLE.table_body_font_hp
    upsert(run_pr, make_element("sz", {"val": str(font_size)}))
    upsert(run_pr, make_element("szCs", {"val": str(font_size)}))

    if is_header:
        upsert(run_pr, make_element("b"))
        upsert(run_pr, make_element("bCs"))


def style_table_rows(table: ET.Element, scaled_widths: list[int]) -> None:
    rows = table.findall("w:tr", NS)
    if not rows:
        return

    for row_index, row in enumerate(rows):
        is_header = row_index == 0
        is_last_row = row_index == len(rows) - 1
        cells = row.findall("w:tc", NS)
        for cell_index, cell in enumerate(cells):
            cell_pr = cell.find("w:tcPr", NS)
            if cell_pr is None:
                cell_pr = ET.Element(qn("tcPr"))
                cell.insert(0, cell_pr)

            if scaled_widths and cell_index < len(scaled_widths):
                upsert(
                    cell_pr,
                    make_element("tcW", {"w": str(scaled_widths[cell_index]), "type": "dxa"}),
                )

            set_cell_borders(cell_pr, is_header=is_header, is_last_row=is_last_row)

            for paragraph in cell.findall(".//w:p", NS):
                set_paragraph_spacing(paragraph)
            for run in cell.findall(".//w:r", NS):
                set_run_style(run, is_header=is_header)


def restyle_tables(document_xml: bytes) -> bytes:
    root = ET.fromstring(document_xml)
    for table in root.findall(".//w:tbl", NS):
        scaled_widths = apply_table_properties(table)
        style_table_rows(table, scaled_widths)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def process_docx(path: Path) -> None:
    original_entries: dict[str, bytes] = {}
    with zipfile.ZipFile(path, "r") as source:
        for info in source.infolist():
            original_entries[info.filename] = source.read(info.filename)

    document_xml = original_entries.get("word/document.xml")
    if document_xml is None:
        raise FileNotFoundError(f"{path} neobsahuje word/document.xml")

    original_entries["word/document.xml"] = restyle_tables(document_xml)

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as target:
        for filename, payload in original_entries.items():
            target.writestr(filename, payload)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply thesis table styling to an existing DOCX export.")
    parser.add_argument("docx", nargs="+", type=Path, help="DOCX file(s) to restyle in place")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for docx_path in args.docx:
        process_docx(docx_path.resolve())
        print(docx_path.resolve())


if __name__ == "__main__":
    main()
