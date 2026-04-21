#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


OPENXML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def extract_section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\n+(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError(f"Nepodarilo sa nájsť sekciu: {heading}")
    return match.group(1).strip()


def extract_bold_line(block: str) -> str:
    match = re.search(r"\*\*(.+?)\*\*", block, flags=re.DOTALL)
    if not match:
        raise ValueError("V sekcii chýba očakávaný tučný riadok.")
    return " ".join(match.group(1).split())


def extract_paragraph_before_label(block: str, label: str) -> str:
    marker = f"**{label}:**"
    if marker not in block:
        raise ValueError(f"V sekcii chýba label {label}.")
    paragraph, _ = block.split(marker, 1)
    return "\n".join(line.rstrip() for line in paragraph.strip().splitlines()).strip()


def extract_label_value(block: str, label: str) -> str:
    match = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", block)
    if not match:
        raise ValueError(f"V sekcii chýba hodnota pre {label}.")
    return " ".join(match.group(1).split())


def xml_page_break() -> str:
    return (
        "```{=openxml}\n"
        f"<w:p xmlns:w=\"{OPENXML_NS}\"><w:r><w:br w:type=\"page\"/></w:r></w:p>\n"
        "```\n"
    )


def build_front_matter(source: Path) -> str:
    text = source.read_text(encoding="utf-8")

    title_block = extract_section(text, "Preferovaný názov")
    sk_block = extract_section(text, "Návrh abstraktu SK")
    en_block = extract_section(text, "Draft abstract EN")

    title = extract_bold_line(title_block)
    sk_abstract = extract_paragraph_before_label(sk_block, "Kľúčové slová")
    sk_keywords = extract_label_value(sk_block, "Kľúčové slová")
    en_abstract = extract_paragraph_before_label(en_block, "Key words")
    en_keywords = extract_label_value(en_block, "Key words")

    parts = [
        f"**{title}**",
        "",
        xml_page_break().rstrip(),
        "",
        "**Abstrakt**",
        "",
        sk_abstract,
        "",
        f"**Kľúčové slová:** {sk_keywords}",
        "",
        xml_page_break().rstrip(),
        "",
        "**Abstract**",
        "",
        en_abstract,
        "",
        f"**Key words:** {en_keywords}",
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build clean near-final front matter from manuscript/10_title_abstract.md.")
    parser.add_argument("source", type=Path, help="Path to manuscript/10_title_abstract.md")
    parser.add_argument("--output", required=True, type=Path, help="Output markdown path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.write_text(build_front_matter(args.source.resolve()), encoding="utf-8")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
