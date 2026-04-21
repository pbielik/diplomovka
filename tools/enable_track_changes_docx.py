#!/usr/bin/env python3
from __future__ import annotations

import argparse
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}

ET.register_namespace("w", W_NS)


def qn(tag: str) -> str:
    return f"{{{W_NS}}}{tag}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Enable Track Changes in a .docx by adding w:trackRevisions to word/settings.xml."
    )
    parser.add_argument("input_docx", help="Path to the source .docx file.")
    parser.add_argument(
        "output_docx",
        nargs="?",
        help="Optional output .docx path. Defaults to overwriting the input file.",
    )
    return parser.parse_args()


def clone_zip_info(info: zipfile.ZipInfo) -> zipfile.ZipInfo:
    cloned = zipfile.ZipInfo(info.filename, date_time=info.date_time)
    cloned.compress_type = info.compress_type
    cloned.comment = info.comment
    cloned.extra = info.extra
    cloned.create_system = info.create_system
    cloned.create_version = info.create_version
    cloned.extract_version = info.extract_version
    cloned.flag_bits = info.flag_bits
    cloned.volume = info.volume
    cloned.internal_attr = info.internal_attr
    cloned.external_attr = info.external_attr
    return cloned


def inject_track_revisions(settings_xml: bytes) -> bytes:
    root = ET.fromstring(settings_xml)
    if root.find("w:trackRevisions", NS) is not None:
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)

    track_revisions = ET.Element(qn("trackRevisions"))

    insert_after = -1
    preferred_predecessors = {
        qn("zoom"),
        qn("embedSystemFonts"),
        qn("proofState"),
        qn("stylePaneFormatFilter"),
    }
    for index, child in enumerate(list(root)):
        if child.tag in preferred_predecessors:
            insert_after = index

    root.insert(insert_after + 1, track_revisions)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def enable_track_changes(input_docx: Path, output_docx: Path) -> None:
    if not input_docx.is_file():
        raise FileNotFoundError(f"Input .docx does not exist: {input_docx}")

    input_mode = input_docx.stat().st_mode

    with zipfile.ZipFile(input_docx, "r") as source_zip:
        try:
            settings_xml = source_zip.read("word/settings.xml")
        except KeyError as exc:
            raise FileNotFoundError(f"Missing word/settings.xml in {input_docx}") from exc

        patched_settings = inject_track_revisions(settings_xml)

        with tempfile.NamedTemporaryFile(
            prefix=output_docx.stem + ".",
            suffix=".docx",
            dir=output_docx.parent,
            delete=False,
        ) as temp_file:
            temp_path = Path(temp_file.name)

        try:
            with zipfile.ZipFile(temp_path, "w") as target_zip:
                for info in source_zip.infolist():
                    payload = patched_settings if info.filename == "word/settings.xml" else source_zip.read(info.filename)
                    target_zip.writestr(clone_zip_info(info), payload)
            temp_path.replace(output_docx)
            output_docx.chmod(input_mode)
        except Exception:
            temp_path.unlink(missing_ok=True)
            raise


def main() -> int:
    args = parse_args()
    input_docx = Path(args.input_docx).expanduser().resolve()
    output_docx = Path(args.output_docx).expanduser().resolve() if args.output_docx else input_docx
    output_docx.parent.mkdir(parents=True, exist_ok=True)
    enable_track_changes(input_docx=input_docx, output_docx=output_docx)
    print(f"Track Changes enabled: {output_docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
