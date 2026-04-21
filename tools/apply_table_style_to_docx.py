#!/usr/bin/env python3
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

from docx_table_style import FINAL_TABLE_STYLE, TEXT_WIDTH_DXA


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS = {"w": W_NS, "wp": WP_NS}
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


def object_inset_dxa(width_dxa: int) -> int:
    bounded_width = min(width_dxa, TEXT_WIDTH_DXA)
    return max(0, int((TEXT_WIDTH_DXA - bounded_width) / 2))


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


def apply_grid_widths(table: ET.Element, widths: list[int]) -> None:
    grid = table.find("w:tblGrid", NS)
    if grid is None:
        return
    grid_columns = grid.findall("w:gridCol", NS)
    for column, width in zip(grid_columns, widths):
        column.set(qn("w"), str(width))


def cell_text(cell: ET.Element) -> str:
    return "".join(node.text or "" for node in cell.findall(".//w:t", NS)).strip()


def parse_score(text: str) -> float | None:
    normalized = text.strip().replace(",", ".")
    if not normalized:
        return None
    try:
        value = float(normalized)
    except ValueError:
        return None
    if 1.0 <= value <= 4.0:
        return value
    return None


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "".join(f"{part:02X}" for part in rgb)


def lerp_color(start: tuple[int, int, int], end: tuple[int, int, int], ratio: float) -> tuple[int, int, int]:
    return tuple(int(start[idx] + (end[idx] - start[idx]) * ratio) for idx in range(3))


def color_for_score(score: float) -> str:
    start = (248, 252, 249)
    end = (210, 232, 217)
    ratio = max(0.0, min(1.0, (score - 1.0) / 3.0))
    return rgb_to_hex(lerp_color(start, end, ratio))


def set_cell_shading(cell_pr: ET.Element, fill: str) -> None:
    upsert(cell_pr, make_element("shd", {"val": "clear", "color": "auto", "fill": fill}))


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


def set_paragraph_spacing(
    paragraph: ET.Element,
    *,
    before: int | None = None,
    after: int | None = None,
    line: int = 240,
    line_rule: str = "auto",
) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    spacing = paragraph_pr.find("w:spacing", NS)
    if spacing is None:
        spacing = make_element("spacing")
        paragraph_pr.append(spacing)

    if before is not None:
        spacing.set(qn("before"), str(before))
    if after is not None:
        spacing.set(qn("after"), str(after))
    spacing.set(qn("line"), str(line))
    spacing.set(qn("lineRule"), line_rule)


def set_paragraph_indents(paragraph: ET.Element, *, left: int, right: int) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    upsert(paragraph_pr, make_element("jc", {"val": "left"}))
    upsert(paragraph_pr, make_element("ind", {"left": str(left), "right": str(right)}))


def set_keep_next(paragraph: ET.Element, enabled: bool = True) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    existing = paragraph_pr.find("w:keepNext", NS)
    if enabled:
        if existing is None:
            paragraph_pr.append(make_element("keepNext"))
    elif existing is not None:
        paragraph_pr.remove(existing)


def set_keep_lines(paragraph: ET.Element, enabled: bool = True) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    existing = paragraph_pr.find("w:keepLines", NS)
    if enabled:
        if existing is None:
            paragraph_pr.append(make_element("keepLines"))
    elif existing is not None:
        paragraph_pr.remove(existing)


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()


def paragraph_style_id(paragraph: ET.Element) -> str | None:
    paragraph_pr = paragraph.find("w:pPr", NS)
    if paragraph_pr is None:
        return None

    paragraph_style = paragraph_pr.find("w:pStyle", NS)
    if paragraph_style is None:
        return None

    return paragraph_style.get(qn("val"))


def is_caption_label_paragraph(paragraph: ET.Element) -> bool:
    text = paragraph_text(paragraph)
    return text.startswith("Tabuľka ") or text.startswith("Obrázok ")


def is_note_paragraph(paragraph: ET.Element) -> bool:
    return paragraph_text(paragraph).startswith("Poznámka.")


def is_image_caption_paragraph(paragraph: ET.Element) -> bool:
    return paragraph_style_id(paragraph) == "ImageCaption"


def paragraph_has_drawing(paragraph: ET.Element) -> bool:
    return paragraph.find(".//w:drawing", NS) is not None


def drawing_width_dxa(paragraph: ET.Element) -> int | None:
    extent = paragraph.find(".//wp:extent", NS)
    if extent is None:
        return None

    cx = extent.get("cx")
    if cx is None:
        return None

    return max(0, round(int(cx) / 635))


def set_run_font_size(run: ET.Element, font_hp: int) -> None:
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
    upsert(run_pr, make_element("sz", {"val": str(font_hp)}))
    upsert(run_pr, make_element("szCs", {"val": str(font_hp)}))


def set_run_color(run: ET.Element, color: str) -> None:
    run_pr = ensure_first_child(run, "rPr")
    upsert(run_pr, make_element("color", {"val": color}))


def set_run_style(run: ET.Element, *, is_header: bool) -> None:
    font_size = STYLE.table_header_font_hp if is_header else STYLE.table_body_font_hp
    set_run_font_size(run, font_size)

    run_pr = ensure_first_child(run, "rPr")

    if is_header:
        upsert(run_pr, make_element("b"))
        upsert(run_pr, make_element("bCs"))


def is_validation_heatmap_table(table: ET.Element) -> bool:
    rows = table.findall("w:tr", NS)
    if not rows:
        return False
    header_cells = rows[0].findall("w:tc", NS)
    header = [cell_text(cell) for cell in header_cells]
    valid_headers = {
        ("Položka", "Relevantnosť", "Zrozumiteľnosť", "Potrebnosť", "Celkovo"),
        ("Scenár", "Amb. profil", "Kontext", "Symptómy", "Jasnosť"),
        ("Scenár", "Info. dostatok", "Nestereotyp.", "Pre výskum", "Celkovo"),
    }
    return tuple(header) in valid_headers


def style_table_rows(table: ET.Element, scaled_widths: list[int], *, heatmap_table: bool = False) -> None:
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

            if heatmap_table:
                if is_header:
                    set_cell_shading(cell_pr, "FFFFFF")
                elif cell_index == 0:
                    set_cell_shading(cell_pr, "FFFFFF")
                else:
                    score = parse_score(cell_text(cell))
                    if score is not None:
                        set_cell_shading(cell_pr, color_for_score(score))
                    else:
                        set_cell_shading(cell_pr, "FFFFFF")

            for paragraph in cell.findall(".//w:p", NS):
                set_paragraph_spacing(paragraph, after=0)
            for run in cell.findall(".//w:r", NS):
                set_run_style(run, is_header=is_header)
                if heatmap_table:
                    set_run_color(run, "1F2529")


def style_note_paragraph(paragraph: ET.Element, inset: int) -> None:
    set_paragraph_indents(paragraph, left=inset, right=inset)
    set_paragraph_spacing(paragraph, after=STYLE.note_after)
    for run in paragraph.findall(".//w:r", NS):
        set_run_font_size(run, STYLE.note_font_hp)


def apply_spacing_after_objects(root: ET.Element) -> None:
    body = root.find("w:body", NS)
    if body is None:
        return

    children = list(body)
    object_tags = {qn("tbl")}

    for index, child in enumerate(children):
        is_object = child.tag in object_tags or (child.tag == qn("p") and paragraph_has_drawing(child))
        if not is_object:
            continue

        next_paragraph: ET.Element | None = None
        for following in children[index + 1 :]:
            if following.tag == qn("p"):
                if is_note_paragraph(following) or is_image_caption_paragraph(following):
                    continue
                next_paragraph = following
                break
            if following.tag == qn("tbl"):
                break

        if next_paragraph is None:
            continue

        if paragraph_style_id(next_paragraph) in {"TableCaption", "FigureCaption"}:
            set_paragraph_spacing(next_paragraph, before=STYLE.table_after)
            continue

        set_paragraph_spacing(next_paragraph, before=STYLE.table_after)


def align_caption_blocks(root: ET.Element, table_widths: dict[int, int]) -> None:
    body = root.find("w:body", NS)
    if body is None:
        return

    children = [child for child in list(body) if child.tag in {qn("p"), qn("tbl")}]
    image_captions_to_remove: list[ET.Element] = []
    for index, child in enumerate(children):
        if child.tag != qn("p") or not is_caption_label_paragraph(child):
            continue

        caption_block = [child]
        object_index = index + 1

        if object_index < len(children):
            next_child = children[object_index]
            if (
                next_child.tag == qn("p")
                and not paragraph_has_drawing(next_child)
                and not is_caption_label_paragraph(next_child)
                and object_index + 1 < len(children)
            ):
                next_target = children[object_index + 1]
                if next_target.tag == qn("tbl") or (
                    next_target.tag == qn("p") and paragraph_has_drawing(next_target)
                ):
                    caption_block.append(next_child)
                    object_index += 1

        if object_index >= len(children):
            continue

        target = children[object_index]
        object_width = None
        if target.tag == qn("tbl"):
            object_width = table_widths.get(id(target), table_width_dxa())
        elif target.tag == qn("p") and paragraph_has_drawing(target):
            object_width = drawing_width_dxa(target)

        if not object_width:
            continue

        inset = object_inset_dxa(object_width)
        for paragraph in caption_block:
            set_paragraph_indents(paragraph, left=inset, right=inset)
            set_paragraph_spacing(paragraph, after=STYLE.title_after)
            set_keep_next(paragraph)
            set_keep_lines(paragraph)

        trailing_index = object_index + 1
        while trailing_index < len(children):
            trailing_child = children[trailing_index]
            if trailing_child.tag != qn("p"):
                break
            if is_image_caption_paragraph(trailing_child):
                image_captions_to_remove.append(trailing_child)
                trailing_index += 1
                continue
            if is_note_paragraph(trailing_child):
                style_note_paragraph(trailing_child, inset)
                trailing_index += 1
                continue
            break

    for paragraph in image_captions_to_remove:
        if paragraph in list(body):
            body.remove(paragraph)


def restyle_document(document_xml: bytes) -> bytes:
    root = ET.fromstring(document_xml)
    table_widths: dict[int, int] = {}
    body = root.find("w:body", NS)
    tables = list(body) if body is not None else root.findall(".//w:tbl", NS)

    for child in tables:
        if child.tag != qn("tbl"):
            continue
        table = child
        scaled_widths = apply_table_properties(table)
        heatmap_table = is_validation_heatmap_table(table)
        if heatmap_table:
            scaled_widths = scale_widths([44, 14, 14, 14, 14], table_width_dxa())
            apply_grid_widths(table, scaled_widths)
        style_table_rows(table, scaled_widths, heatmap_table=heatmap_table)
        table_widths[id(table)] = sum(scaled_widths) if scaled_widths else table_width_dxa()

    align_caption_blocks(root, table_widths)
    apply_spacing_after_objects(root)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def process_docx(path: Path) -> None:
    original_entries: dict[str, bytes] = {}
    with zipfile.ZipFile(path, "r") as source:
        for info in source.infolist():
            original_entries[info.filename] = source.read(info.filename)

    document_xml = original_entries.get("word/document.xml")
    if document_xml is None:
        raise FileNotFoundError(f"{path} neobsahuje word/document.xml")

    original_entries["word/document.xml"] = restyle_document(document_xml)

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
