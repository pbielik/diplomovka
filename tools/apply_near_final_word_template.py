#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import re
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W_NS, "r": R_NS}

ET.register_namespace("w", W_NS)
ET.register_namespace("r", R_NS)

CAPTION_ID_PATTERN = r"(?:[A-Z]?\d+[a-z]?(?:\.\d+)*)"
FIRST_LINE_INDENT_TWIPS = 709
INDENTED_BODY_STYLES = {"BodyText", "FirstParagraph", "Compact", "BlockText"}
FIGURE_LIKE_CAPTION_PREFIXES = ("Obrázok", "Schéma")


def qn(ns: str, tag: str) -> str:
    namespace = {"w": W_NS, "r": R_NS}[ns]
    return f"{{{namespace}}}{tag}"


def make_w(tag: str, attrs: dict[str, str] | None = None) -> ET.Element:
    element = ET.Element(qn("w", tag))
    for key, value in (attrs or {}).items():
        element.set(qn("w", key), value)
    return element


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()


def paragraph_style_id(paragraph: ET.Element) -> str | None:
    paragraph_pr = paragraph.find("w:pPr", NS)
    if paragraph_pr is None:
        return None
    paragraph_style = paragraph_pr.find("w:pStyle", NS)
    if paragraph_style is None:
        return None
    return paragraph_style.get(qn("w", "val"))


def ensure_first_child(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(f"w:{tag}", NS)
    if child is None:
        child = make_w(tag)
        parent.insert(0, child)
    return child


def upsert(parent: ET.Element, child: ET.Element) -> None:
    for existing in parent.findall(child.tag):
        parent.remove(existing)
    parent.append(child)


def set_paragraph_style(paragraph: ET.Element, style_id: str) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    upsert(paragraph_pr, make_w("pStyle", {"val": style_id}))


def set_page_break_before(paragraph: ET.Element, enabled: bool) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    existing = paragraph_pr.find("w:pageBreakBefore", NS)
    if enabled:
        if existing is None:
            paragraph_pr.append(make_w("pageBreakBefore"))
    elif existing is not None:
        paragraph_pr.remove(existing)


def set_keep_next(paragraph: ET.Element, enabled: bool = True) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    existing = paragraph_pr.find("w:keepNext", NS)
    if enabled:
        if existing is None:
            paragraph_pr.append(make_w("keepNext"))
    elif existing is not None:
        paragraph_pr.remove(existing)


def set_keep_lines(paragraph: ET.Element, enabled: bool = True) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    existing = paragraph_pr.find("w:keepLines", NS)
    if enabled:
        if existing is None:
            paragraph_pr.append(make_w("keepLines"))
    elif existing is not None:
        paragraph_pr.remove(existing)


def set_first_line_indent(paragraph: ET.Element, first_line_twips: int) -> None:
    paragraph_pr = ensure_first_child(paragraph, "pPr")
    indent = paragraph_pr.find("w:ind", NS)
    if indent is None:
        indent = make_w("ind")
        paragraph_pr.append(indent)
    indent.set(qn("w", "firstLine"), str(first_line_twips))


def clear_first_line_indent(paragraph: ET.Element) -> None:
    paragraph_pr = paragraph.find("w:pPr", NS)
    if paragraph_pr is None:
        return

    indent = paragraph_pr.find("w:ind", NS)
    if indent is None:
        return

    first_line_key = qn("w", "firstLine")
    if first_line_key in indent.attrib:
        del indent.attrib[first_line_key]

    if not indent.attrib:
        paragraph_pr.remove(indent)


def make_text_run(text: str, *, bold: bool = False, italic: bool = False, line_break_before: bool = False) -> ET.Element:
    run = make_w("r")
    if bold or italic:
        run_pr = make_w("rPr")
        if bold:
            run_pr.append(make_w("b"))
            run_pr.append(make_w("bCs"))
        if italic:
            run_pr.append(make_w("i"))
            run_pr.append(make_w("iCs"))
        run.append(run_pr)
    if line_break_before:
        run.append(make_w("br"))
    text_node = make_w("t")
    if text.startswith(" ") or text.endswith(" "):
        text_node.set(f"{{{XML_NS}}}space", "preserve")
    text_node.text = text
    run.append(text_node)
    return run


def make_heading_paragraph(text: str, *, style_id: str = "NavigationHeading", page_break_before: bool = False) -> ET.Element:
    paragraph = make_w("p")
    paragraph_pr = make_w("pPr")
    paragraph_pr.append(make_w("pStyle", {"val": style_id}))
    if page_break_before:
        paragraph_pr.append(make_w("pageBreakBefore"))
    paragraph.append(paragraph_pr)
    paragraph.append(make_text_run(text))
    return paragraph


def make_field_paragraph(field_instr: str) -> ET.Element:
    paragraph = make_w("p")

    begin_run = make_w("r")
    begin_run.append(make_w("fldChar", {"fldCharType": "begin", "dirty": "true"}))
    paragraph.append(begin_run)

    instr_run = make_w("r")
    instr_text = make_w("instrText")
    instr_text.set(f"{{{XML_NS}}}space", "preserve")
    instr_text.text = f" {field_instr} "
    instr_run.append(instr_text)
    paragraph.append(instr_run)

    separate_run = make_w("r")
    separate_run.append(make_w("fldChar", {"fldCharType": "separate"}))
    paragraph.append(separate_run)

    placeholder_run = make_w("r")
    placeholder_text = make_w("t")
    placeholder_text.text = " "
    placeholder_run.append(placeholder_text)
    paragraph.append(placeholder_run)

    end_run = make_w("r")
    end_run.append(make_w("fldChar", {"fldCharType": "end"}))
    paragraph.append(end_run)

    return paragraph


def find_footer_rel_ids(entries: dict[str, bytes], rels_root: ET.Element) -> tuple[str, str]:
    empty_rel_id: str | None = None
    numbered_rel_id: str | None = None

    for rel in rels_root:
        if not rel.attrib.get("Type", "").endswith("/footer"):
            continue
        rel_id = rel.attrib["Id"]
        target = rel.attrib["Target"]
        footer_xml = entries.get(f"word/{target}")
        if footer_xml is None:
            continue

        footer_root = ET.fromstring(footer_xml)
        has_page_field = (
            footer_root.find(".//w:instrText[.='PAGE   \\* MERGEFORMAT']", NS) is not None
            or footer_root.find(".//w:fldSimple", NS) is not None
            or "PAGE" in "".join(node.text or "" for node in footer_root.findall(".//w:instrText", NS))
        )
        paragraph_texts = "".join(node.text or "" for node in footer_root.findall(".//w:t", NS)).strip()

        if has_page_field:
            numbered_rel_id = rel_id
        elif not paragraph_texts:
            empty_rel_id = rel_id

    if empty_rel_id is None or numbered_rel_id is None:
        raise RuntimeError("Nepodarilo sa identifikovať prázdny a číslovaný footer vo reference DOCX.")

    return empty_rel_id, numbered_rel_id


def set_footer_reference(sect_pr: ET.Element, rel_id: str) -> None:
    for ref in sect_pr.findall("w:footerReference", NS):
        sect_pr.remove(ref)
    footer_ref = ET.Element(qn("w", "footerReference"))
    footer_ref.set(qn("w", "type"), "default")
    footer_ref.set(qn("r", "id"), rel_id)
    sect_pr.insert(0, footer_ref)


def set_pg_num_type(sect_pr: ET.Element, *, fmt: str | None = None, start: int | None = None) -> None:
    existing = sect_pr.find("w:pgNumType", NS)
    if fmt is None and start is None:
        if existing is not None:
            sect_pr.remove(existing)
        return

    if existing is None:
        existing = make_w("pgNumType")
        sect_pr.append(existing)

    if fmt is not None:
        existing.set(qn("w", "fmt"), fmt)
    elif qn("w", "fmt") in existing.attrib:
        del existing.attrib[qn("w", "fmt")]

    if start is not None:
        existing.set(qn("w", "start"), str(start))
    elif qn("w", "start") in existing.attrib:
        del existing.attrib[qn("w", "start")]


def set_section_break_type(sect_pr: ET.Element, break_type: str) -> None:
    type_node = sect_pr.find("w:type", NS)
    if type_node is None:
        type_node = make_w("type", {"val": break_type})
        sect_pr.insert(0, type_node)
    else:
        type_node.set(qn("w", "val"), break_type)


def set_footer_distance(sect_pr: ET.Element, distance_twips: int) -> None:
    page_margins = sect_pr.find("w:pgMar", NS)
    if page_margins is None:
        page_margins = make_w("pgMar")
        sect_pr.append(page_margins)
    page_margins.set(qn("w", "footer"), str(distance_twips))


def make_section_break_paragraph(sect_pr: ET.Element) -> ET.Element:
    paragraph = make_w("p")
    paragraph_pr = make_w("pPr")
    paragraph_pr.append(copy.deepcopy(sect_pr))
    paragraph.append(paragraph_pr)
    return paragraph


def ensure_caption_styles(styles_root: ET.Element) -> None:
    for style_id, style_name in (
        ("TableCaption", "Table Caption"),
        ("FigureCaption", "Figure Caption"),
    ):
        style = styles_root.find(f"w:style[@w:styleId='{style_id}']", NS)
        if style is not None:
            continue

        new_style = ET.Element(qn("w", "style"), {qn("w", "type"): "paragraph", qn("w", "customStyle"): "1", qn("w", "styleId"): style_id})
        new_style.append(make_w("name", {"val": style_name}))
        new_style.append(make_w("basedOn", {"val": "Popis"}))
        new_style.append(make_w("next", {"val": "Normlny"}))
        new_style.append(make_w("qFormat"))
        paragraph_pr = make_w("pPr")
        paragraph_pr.append(make_w("keepNext"))
        paragraph_pr.append(make_w("keepLines"))
        new_style.append(paragraph_pr)
        styles_root.append(new_style)


def ensure_schema_line_style(styles_root: ET.Element) -> None:
    style = styles_root.find("w:style[@w:styleId='SchemaLine']", NS)
    if style is None:
        style = ET.Element(
            qn("w", "style"),
            {
                qn("w", "type"): "paragraph",
                qn("w", "customStyle"): "1",
                qn("w", "styleId"): "SchemaLine",
            },
        )
        styles_root.append(style)

    if style.find("w:name", NS) is None:
        style.append(make_w("name", {"val": "Schema Line"}))
    if style.find("w:basedOn", NS) is None:
        style.append(make_w("basedOn", {"val": "BodyText"}))
    if style.find("w:next", NS) is None:
        style.append(make_w("next", {"val": "Normlny"}))
    if style.find("w:qFormat", NS) is None:
        style.append(make_w("qFormat"))

    paragraph_pr = style.find("w:pPr", NS)
    if paragraph_pr is None:
        paragraph_pr = make_w("pPr")
        style.append(paragraph_pr)

    upsert(paragraph_pr, make_w("jc", {"val": "center"}))
    upsert(paragraph_pr, make_w("spacing", {"before": "0", "after": "60", "line": "240", "lineRule": "auto"}))
    upsert(paragraph_pr, make_w("ind", {"firstLine": "0", "left": "0", "right": "0"}))


def ensure_navigation_heading_style(styles_root: ET.Element) -> None:
    style = styles_root.find("w:style[@w:styleId='NavigationHeading']", NS)
    if style is not None:
        return

    new_style = ET.Element(
        qn("w", "style"),
        {
            qn("w", "type"): "paragraph",
            qn("w", "customStyle"): "1",
            qn("w", "styleId"): "NavigationHeading",
        },
    )
    new_style.append(make_w("name", {"val": "Navigation Heading"}))
    new_style.append(make_w("basedOn", {"val": "Nadpis1"}))
    new_style.append(make_w("next", {"val": "Normlny"}))
    new_style.append(make_w("qFormat"))

    paragraph_pr = make_w("pPr")
    paragraph_pr.append(make_w("outlineLvl", {"val": "9"}))
    new_style.append(paragraph_pr)

    styles_root.append(new_style)


def paragraph_has_drawing(paragraph: ET.Element) -> bool:
    return paragraph.find(".//w:drawing", NS) is not None


def is_caption_label_only(text: str, prefix: str) -> bool:
    return re.fullmatch(rf"{prefix} {CAPTION_ID_PATTERN}", text) is not None


def is_inline_caption(text: str, prefix: str) -> bool:
    match = re.fullmatch(rf"{prefix} (?P<identifier>{CAPTION_ID_PATTERN})(?P<title>.*)", text)
    if match is None:
        return False

    title = (match.group("title") or "").lstrip()
    if not title:
        return False

    first = title[0]
    return first.isupper() or first.isdigit() or first in {'"', "'", "(", "[", "„", "“"}


def apply_body_first_line_indent(body: ET.Element) -> None:
    first_nonempty_paragraph_seen = False

    for child in list(body):
        if child.tag != qn("w", "p"):
            continue

        text = paragraph_text(child)
        if not text:
            continue

        if not first_nonempty_paragraph_seen:
            first_nonempty_paragraph_seen = True
            continue

        paragraph_pr = child.find("w:pPr", NS)
        if paragraph_pr is not None and paragraph_pr.find("w:numPr", NS) is not None:
            clear_first_line_indent(child)
            continue

        if text.startswith("Poznámka."):
            clear_first_line_indent(child)
            continue

        style_id = paragraph_style_id(child)
        if style_id not in INDENTED_BODY_STYLES:
            continue

        if text in {"Abstrakt", "Abstract"}:
            continue
        if text.startswith(("Kľúčové slová:", "Key words:")):
            continue
        if paragraph_has_drawing(child):
            continue

        set_first_line_indent(child, FIRST_LINE_INDENT_TWIPS)


def style_caption_paragraphs(body: ET.Element) -> None:
    children = list(body)
    index = 0

    while index < len(children) - 1:
        current = children[index]
        next_child = children[index + 1]

        if current.tag != qn("w", "p"):
            index += 1
            continue

        label_text = paragraph_text(current)
        if is_inline_caption(label_text, "Tabuľka") and next_child.tag == qn("w", "tbl"):
            set_paragraph_style(current, "TableCaption")
            set_keep_next(current)
            set_keep_lines(current)
            index += 1
            continue

        matched_inline_figure_caption = False
        for prefix in FIGURE_LIKE_CAPTION_PREFIXES:
            if (
                is_inline_caption(label_text, prefix)
                and next_child.tag == qn("w", "p")
                and (
                    paragraph_style_id(next_child) in {"CaptionedFigure", "SchemaLine"}
                    or paragraph_has_drawing(next_child)
                )
            ):
                set_paragraph_style(current, "FigureCaption")
                set_keep_next(current)
                set_keep_lines(current)
                matched_inline_figure_caption = True
                index += 1
                break
        if matched_inline_figure_caption:
            continue

        if current.tag != qn("w", "p") or next_child.tag != qn("w", "p"):
            index += 1
            continue

        title_text = paragraph_text(next_child)
        if is_caption_label_only(label_text, "Tabuľka"):
            style_id = "TableCaption"
        elif any(is_caption_label_only(label_text, prefix) for prefix in FIGURE_LIKE_CAPTION_PREFIXES):
            style_id = "FigureCaption"
        else:
            index += 1
            continue

        if not title_text or title_text.startswith("Poznámka."):
            index += 1
            continue

        merged = copy.deepcopy(current)
        for child in list(merged):
            if child.tag != qn("w", "pPr"):
                merged.remove(child)

        set_paragraph_style(merged, style_id)
        set_keep_next(merged)
        set_keep_lines(merged)
        merged.append(make_text_run(label_text, bold=True))
        merged.append(make_text_run(title_text, italic=True, line_break_before=True))

        current_pos = list(body).index(current)
        body.remove(current)
        body.remove(next_child)
        body.insert(current_pos, merged)

        children = list(body)
        index = max(current_pos - 1, 0)


def style_schema_blocks(body: ET.Element) -> None:
    children = [child for child in list(body) if child.tag == qn("w", "p")]
    index = 0

    while index < len(children):
        paragraph = children[index]
        if paragraph_style_id(paragraph) != "SchemaLine":
            index += 1
            continue

        block: list[ET.Element] = []
        while index < len(children) and paragraph_style_id(children[index]) == "SchemaLine":
            block.append(children[index])
            index += 1

        for block_index, schema_paragraph in enumerate(block):
            clear_first_line_indent(schema_paragraph)
            set_keep_lines(schema_paragraph)
            set_keep_next(schema_paragraph, enabled=block_index < len(block) - 1)


def restyle_appendix_headings(body: ET.Element) -> tuple[ET.Element | None, ET.Element | None]:
    first_heading: ET.Element | None = None
    first_appendix_heading: ET.Element | None = None
    in_appendix = False

    for child in list(body):
        if child.tag != qn("w", "p"):
            continue

        style_id = paragraph_style_id(child)
        text = paragraph_text(child)
        if style_id is None:
            continue

        if style_id == "Nadpis1" and first_heading is None:
            first_heading = child

        if style_id == "Nadpis2" and re.match(r"^Príloha [A-Z]", text):
            set_paragraph_style(child, "Nadpis1-Prloha")
            in_appendix = True
            if first_appendix_heading is None:
                first_appendix_heading = child
            continue

        if style_id == "Nadpis1" and in_appendix:
            in_appendix = False

        if in_appendix and style_id == "Nadpis3":
            set_paragraph_style(child, "Nadpis2-Orloha")

    return first_heading, first_appendix_heading


def is_navigation_field_paragraph(paragraph: ET.Element) -> bool:
    instructions = [
        (node.text or "").strip()
        for node in paragraph.findall(".//w:instrText", NS)
    ]
    return any(instr.startswith("TOC ") or instr == "TOC" for instr in instructions)


def remove_existing_navigation_and_section_breaks(body: ET.Element, first_heading: ET.Element | None) -> None:
    if first_heading is None:
        return

    first_index = list(body).index(first_heading)
    removable: list[ET.Element] = []

    for child in list(body)[:first_index]:
        if child.tag != qn("w", "p"):
            continue

        style_id = paragraph_style_id(child)
        paragraph_pr = child.find("w:pPr", NS)
        has_section_break = paragraph_pr is not None and paragraph_pr.find("w:sectPr", NS) is not None

        if style_id == "NavigationHeading" or is_navigation_field_paragraph(child) or has_section_break:
            removable.append(child)

    for child in removable:
        body.remove(child)


def insert_navigation_blocks(body: ET.Element, first_heading: ET.Element) -> None:
    first_index = list(body).index(first_heading)
    blocks = [
        make_heading_paragraph("Obsah", page_break_before=True),
        make_field_paragraph('TOC \\h \\z \\t "heading 1,1,heading 2,2,heading 3,3,Nadpis 1 - Príloha,1,Nadpis 2 - Oríloha,2"'),
        make_heading_paragraph("Zoznam tabuliek", page_break_before=True),
        make_field_paragraph('TOC \\h \\z \\t "Table Caption,1"'),
        make_heading_paragraph("Zoznam obrázkov", page_break_before=True),
        make_field_paragraph('TOC \\h \\z \\t "Figure Caption,1"'),
    ]
    for offset, block in enumerate(blocks):
        body.insert(first_index + offset, block)


def apply_chapter_page_breaks(body: ET.Element, first_heading: ET.Element | None, first_appendix_heading: ET.Element | None) -> None:
    if first_heading is None:
        return

    for child in list(body):
        if child.tag != qn("w", "p"):
            continue
        style_id = paragraph_style_id(child)
        if style_id not in {"Nadpis1", "Nadpis1-Prloha"}:
            continue

        should_break = child is not first_heading and child is not first_appendix_heading
        set_page_break_before(child, should_break)


def insert_section_breaks(
    body: ET.Element,
    *,
    first_heading: ET.Element | None,
    first_appendix_heading: ET.Element | None,
    empty_footer_rel_id: str,
    numbered_footer_rel_id: str,
) -> None:
    tail_sect_pr = body.find("w:sectPr", NS)
    if tail_sect_pr is None or first_heading is None:
        return

    frontmatter_sect_pr = copy.deepcopy(tail_sect_pr)
    set_footer_reference(frontmatter_sect_pr, empty_footer_rel_id)
    set_pg_num_type(frontmatter_sect_pr)
    set_section_break_type(frontmatter_sect_pr, "nextPage")
    set_footer_distance(frontmatter_sect_pr, 480)
    main_sect_pr = copy.deepcopy(tail_sect_pr)
    set_footer_reference(main_sect_pr, numbered_footer_rel_id)
    set_pg_num_type(main_sect_pr)
    set_footer_distance(main_sect_pr, 480)

    insert_index = list(body).index(first_heading)
    body.insert(insert_index, make_section_break_paragraph(frontmatter_sect_pr))

    if first_appendix_heading is not None:
        appendix_sect_pr = copy.deepcopy(main_sect_pr)
        set_footer_reference(appendix_sect_pr, numbered_footer_rel_id)
        set_pg_num_type(appendix_sect_pr, fmt="upperRoman", start=1)
        set_footer_distance(appendix_sect_pr, 480)

        appendix_break_sect_pr = copy.deepcopy(main_sect_pr)
        set_section_break_type(appendix_break_sect_pr, "nextPage")
        set_footer_distance(appendix_break_sect_pr, 480)
        appendix_index = list(body).index(first_appendix_heading)
        body.insert(appendix_index, make_section_break_paragraph(appendix_break_sect_pr))

        body.remove(tail_sect_pr)
        body.append(appendix_sect_pr)
    else:
        body.remove(tail_sect_pr)
        body.append(main_sect_pr)


def process_docx(path: Path) -> None:
    original_entries: dict[str, bytes] = {}
    with zipfile.ZipFile(path, "r") as source:
        for info in source.infolist():
            original_entries[info.filename] = source.read(info.filename)

    document_xml = original_entries.get("word/document.xml")
    styles_xml = original_entries.get("word/styles.xml")
    rels_xml = original_entries.get("word/_rels/document.xml.rels")
    if document_xml is None or styles_xml is None or rels_xml is None:
        raise FileNotFoundError(f"{path} neobsahuje kompletné Word XML časti.")

    rels_root = ET.fromstring(rels_xml)
    empty_footer_rel_id, numbered_footer_rel_id = find_footer_rel_ids(original_entries, rels_root)

    styles_root = ET.fromstring(styles_xml)
    ensure_caption_styles(styles_root)
    ensure_schema_line_style(styles_root)
    ensure_navigation_heading_style(styles_root)
    original_entries["word/styles.xml"] = ET.tostring(styles_root, encoding="utf-8", xml_declaration=True)

    document_root = ET.fromstring(document_xml)
    body = document_root.find("w:body", NS)
    if body is None:
        raise RuntimeError("word/document.xml neobsahuje body element.")

    style_caption_paragraphs(body)
    style_schema_blocks(body)
    first_heading, first_appendix_heading = restyle_appendix_headings(body)
    remove_existing_navigation_and_section_breaks(body, first_heading)
    first_heading, first_appendix_heading = restyle_appendix_headings(body)
    apply_body_first_line_indent(body)
    if first_heading is not None:
        insert_navigation_blocks(body, first_heading)
    insert_section_breaks(
        body,
        first_heading=first_heading,
        first_appendix_heading=first_appendix_heading,
        empty_footer_rel_id=empty_footer_rel_id,
        numbered_footer_rel_id=numbered_footer_rel_id,
    )
    apply_chapter_page_breaks(body, first_heading, first_appendix_heading)

    original_entries["word/document.xml"] = ET.tostring(document_root, encoding="utf-8", xml_declaration=True)

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as target:
        for filename, payload in original_entries.items():
            target.writestr(filename, payload)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply near-final thesis Word formatting to an existing DOCX export.")
    parser.add_argument("docx", nargs="+", type=Path, help="DOCX file(s) to postprocess in place")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for docx_path in args.docx:
        process_docx(docx_path.resolve())
        print(docx_path.resolve())


if __name__ == "__main__":
    main()
