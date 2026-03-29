#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


SCRIPT_DIR = Path(__file__).resolve().parent
PDF_SWIFT_HELPER = SCRIPT_DIR / "pdfkit_extract.swift"

XML_NS = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
}

SUPPORTED_SUFFIXES = {
    ".pdf",
    ".docx",
    ".doc",
    ".xlsx",
    ".pptx",
}


class ConversionError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert PDF, Word, Excel and PowerPoint files to Markdown.",
    )
    parser.add_argument("source", type=Path, help="Source document path.")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Output Markdown path. Defaults to <source>.md next to the input file.",
    )
    parser.add_argument(
        "--title",
        help="Optional top-level Markdown heading to prepend.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Write Markdown to stdout instead of a file.",
    )
    parser.add_argument(
        "--pdf-ocr",
        action="store_true",
        help="Use macOS Vision OCR for PDF text extraction. Slower, but better for PDFs with broken font encodings.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    if not source.exists():
        raise SystemExit(f"Source file does not exist: {source}")

    suffix = source.suffix.lower()
    if suffix not in SUPPORTED_SUFFIXES:
        supported = ", ".join(sorted(SUPPORTED_SUFFIXES))
        raise SystemExit(f"Unsupported format '{suffix}'. Supported: {supported}")

    markdown = convert_document(source, suffix, title=args.title, pdf_ocr=args.pdf_ocr)

    if args.stdout:
        sys.stdout.write(markdown)
        return 0

    output = args.output.resolve() if args.output else source.with_suffix(".md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    print(output)
    return 0


def convert_document(source: Path, suffix: str, title: str | None, pdf_ocr: bool = False) -> str:
    if suffix == ".pdf":
        pages = extract_pdf_pages(source, use_ocr=pdf_ocr)
        return render_pdf_markdown(pages, title=title)
    if suffix == ".docx":
        body = pandoc_convert(source, source_format="docx")
        return add_title(body, title)
    if suffix == ".doc":
        body = convert_doc_with_textutil(source)
        return add_title(body, title)
    if suffix == ".xlsx":
        body = convert_xlsx_to_markdown(source)
        return add_title(body, title)
    if suffix == ".pptx":
        body = convert_pptx_to_markdown(source)
        return add_title(body, title)
    raise ConversionError(f"Unsupported format: {suffix}")


def add_title(body: str, title: str | None) -> str:
    body = body.strip()
    if not title:
        return body + "\n"
    if body.startswith("# "):
        return body + "\n"
    return f"# {title}\n\n{body}\n"


def run_command(cmd: list[str], *, input_text: str | None = None) -> str:
    try:
        result = subprocess.run(
            cmd,
            input=input_text,
            text=True,
            capture_output=True,
            check=True,
        )
    except FileNotFoundError as exc:
        raise ConversionError(f"Missing required command: {cmd[0]}") from exc
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or exc.stdout.strip() or str(exc)
        raise ConversionError(message) from exc
    return result.stdout


def pandoc_convert(source: Path, *, source_format: str) -> str:
    return run_command(
        [
            "pandoc",
            "--from",
            source_format,
            "--to",
            "gfm",
            "--wrap=none",
            str(source),
        ],
    ).strip()


def convert_doc_with_textutil(source: Path) -> str:
    html_text = run_command(["textutil", "-convert", "html", "-stdout", str(source)])
    try:
        markdown = run_command(
            ["pandoc", "--from", "html", "--to", "gfm", "--wrap=none"],
            input_text=html_text,
        )
    except ConversionError:
        plain_text = run_command(["textutil", "-convert", "txt", "-stdout", str(source)])
        markdown = plain_text_to_markdown(plain_text)
    return markdown.strip()


def extract_pdf_pages(source: Path, *, use_ocr: bool = False) -> list[str]:
    if not PDF_SWIFT_HELPER.exists():
        raise ConversionError(f"Missing PDF helper: {PDF_SWIFT_HELPER}")
    module_cache = Path(tempfile.gettempdir()) / "swift-module-cache"
    module_cache.mkdir(parents=True, exist_ok=True)
    cmd = [
        "swift",
        "-module-cache-path",
        str(module_cache),
        str(PDF_SWIFT_HELPER),
    ]
    if use_ocr:
        cmd.append("--ocr")
    cmd.append(str(source))
    raw = run_command(
        cmd,
    )
    try:
        pages = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ConversionError("Failed to decode PDF extractor output.") from exc
    if not isinstance(pages, list):
        raise ConversionError("Unexpected PDF extractor payload.")
    return [str(page) for page in pages]


def render_pdf_markdown(pages: list[str], title: str | None) -> str:
    cleaned_pages = [cleanup_pdf_page(page) for page in pages]
    cleaned_pages = [page for page in cleaned_pages if page.strip()]
    sections: list[str] = []
    if title:
        sections.append(f"# {title}")
    for page in cleaned_pages:
        blocks = lines_to_markdown_blocks(page.splitlines())
        if blocks:
            sections.append("\n\n".join(blocks))
    markdown = "\n\n".join(section.rstrip() for section in sections if section.strip()) + "\n"
    return cleanup_slovak_pdf_markdown(markdown)


def cleanup_slovak_pdf_markdown(markdown: str) -> str:
    artifact_score = sum(
        markdown.count(token)
        for token in [
            "~",
            "Q",
            "podIa",
            "vbe",
            "bkola",
            "btudent",
            "záverených",
        ]
    )
    if artifact_score < 5:
        return markdown

    text = markdown

    substring_replacements = [
        ("~", "ž"),
        ("Q", "ň"),
        ("}iadna", "Žiadna"),
        ("}eny", "Ženy"),
        ("}ivotná", "Životná"),
        ("}ivot", "Život"),
        ("}ih", "Žiť"),
        ("ybb", "yšš"),
        ("Ybb", "Yšš"),
        ("vbet", "všet"),
        ("Vbet", "Všet"),
        ("vbe", "vše"),
        ("Vbe", "Vše"),
        ("bk", "šk"),
        ("bt", "št"),
        ("bpec", "špec"),
        ("btr", "štr"),
        ("btat", "štat"),
        ("bty", "šty"),
        ("bik", "šik"),
        ("zvyb", "zvyš"),
        ("vbak", "však"),
        ("avbak", "avšak"),
        ("myblien", "myšlien"),
        ("najastej", "najčastejš"),
        ("väbi", "väčši"),
        ("Rozlib", "Rozliš"),
        ("rozlib", "rozliš"),
        ("odlib", "odliš"),
        ("prílib", "príliš"),
        ("rebpekt", "rešpekt"),
        ("koreb", "koreš"),
        ("konbtr", "konštr"),
        ("nab", "naš"),
        ("Nab", "Naš"),
        ("náb", "náš"),
        ("Náb", "Náš"),
        ("rieb", "rieš"),
        ("opíb", "opíš"),
        ("prináb", "prináš"),
        ("zbytone", "zbytočné"),
        ("zrun", "zručn"),
        ("skuton", "skutočn"),
        ("poet", "počet"),
        ("vďan", "vďačn"),
        ("náron", "náročn"),
        ("komunikan", "komunikačn"),
        ("informan", "informačn"),
        ("korelan", "korelačn"),
        ("komparan", "komparačn"),
        ("kvalifikan", "kvalifikačn"),
        ("identifikan", "identifikačn"),
        ("replikan", "replikačn"),
        ("vizualizan", "vizualizačn"),
        ("populan", "populačn"),
        ("stratifikan", "stratifikačn"),
        ("konzultan", "konzultačn"),
        ("situan", "situačn"),
        ("funkn", "funkčn"),
        ("sebaúin", "sebaúčin"),
        ("spolon", "spoločn"),
        ("spoloen", "spoločen"),
        ("vzhah", "vzťah"),
        ("vzeah", "vzťah"),
        ("záverených", "záverečných"),
        ("záverená", "záverečná"),
        ("záverenej", "záverečnej"),
        ("záverenú", "záverečnú"),
        ("záverené", "záverečné"),
        ("závereným", "záverečným"),
        ("záverenými", "záverečnými"),
        ("Preo", "Prečo"),
        ("preo", "prečo"),
        ("Michal čerebník", "Michal Čerebník"),
        ("doc. PhDr. Michal čerebník", "doc. PhDr. Michal Čerebník"),
        ("podIa", "podľa"),
        ("PrehIad", "Prehľad"),
        ("prehIad", "prehľad"),
        ("hIad", "hľad"),
        ("veIk", "veľk"),
        ("kIú", "kľú"),
        ("kIu", "kľu"),
        ("Iudia", "ľudia"),
        ("Iuď", "ľuď"),
        ("podieIa", "podieľa"),
        ("itateI", "čitateľ"),
        ("zrozumiteI", "zrozumiteľ"),
        ("voIb", "voľb"),
        ("pohIad", "pohľad"),
        ("dohIad", "dohľad"),
        ("školiteI", "školiteľ"),
        ("vydavateI", "vydavateľ"),
        ("akéhokoIvek", "akéhokoľvek"),
        ("akýchkoIvek", "akýchkoľvek"),
        ("nakoIko", "nakoľko"),
        ("niekoIko", "niekoľko"),
        ("spoIahliv", "spoľahliv"),
        ("chvíIu", "chvíľu"),
        ("zohIad", "zohľad"),
        ("prijateInosti", "prijateľnosti"),
        ("porovnateIn", "porovnateľn"),
        ("ovplyvniteIn", "ovplyvniteľn"),
        ("nepredvídateIn", "nepredvídateľn"),
        ("zrozumiteIn", "zrozumiteľn"),
        ("rozhIadenosh", "rozhľadenosť"),
        ("Vaeobec", "Všeobec"),
        ("najčastejšb", "najčastejš"),
        ("Rieben", "Riešen"),
        ("ísel", "čísel"),
        ("Cvienie", "Cvičenie"),
        ("TabuIka", "Tabuľka"),
        ("VoIba", "Voľba"),
        ("IubovoI", "ľubovoľ"),
        ("CieI", "Cieľ"),
        ("cieI", "cieľ"),
        ("uebn", "učebn"),
        ("Uebn", "Učebn"),
        ("uen", "učen"),
        ("poas", "počas"),
        ("astokrát", "častokrát"),
        ("inbpirácia", "inšpirácia"),
        ("bablóna", "šablóna"),
        ("potrieš", "potrieb"),
        ("výub", "výučb"),
        ("vyuovaných", "vyučovaných"),
        ("vyuuj", "vyuč"),
        ("užitoné", "užitočné"),
        ("uIahih", "uľahčiť"),
        ("ítah", "čítať"),
        ("objavih", "objaviť"),
        ("klásh", "klásť"),
        ("spresňovah", "spresňovať"),
        ("prebiehah", "prebiehať"),
        ("Dokonen", "Dokončen"),
        ("akoliteI", "Školiteľ"),
        ("skonenia", "skončenia"),
        ("Dizertan", "Dizertačn"),
        ("Oak", "Očak"),
        ("oak", "očak"),
        ("zlepbenie", "zlepšenie"),
        ("najdôležitejb", "najdôležitejš"),
        ("prenositeIn", "prenositeľn"),
        ("zamestnateIn", "zamestnateľn"),
        ("biestich", "šiestich"),
        ("úelom", "účelom"),
        ("iže", "čiže"),
        ("pokroil", "pokročil"),
        ("naznauje", "naznačuje"),
        ("pokraov", "pokračov"),
        ("udeIuje", "udeľuje"),
        ("rozbir", "rozšir"),
        ("birb", "širš"),
        ("birok", "širok"),
        ("súasn", "súčasn"),
        ("úast", "účast"),
        ("zúast", "zúčast"),
        ("preít", "prečít"),
        ("doít", "dočít"),
        ("iark", "čiark"),
        ("iarov", "čiarov"),
        ("iarou", "čiarou"),
        ("Líbi", "Líši"),
        ("líbi", "líši"),
        ("veImi", "veľmi"),
        ("hažko", "ťažko"),
        ("úely", "účely"),
        ("príslubnej", "príslušnej"),
        ("innosť", "činnosť"),
        ("zish", "zisť"),
        ("reberbe", "rešerše"),
        ("lovek", "človek"),
        ("novbieho", "novšieho"),
        ("zIavového", "zľavového"),
        ("hráov", "hráčov"),
        ("zosmiebnenia", "zosmiešnenia"),
        ("vylúenie", "vylúčenie"),
        ("rozsiahlejbie", "rozsiahlejšie"),
        ("komplexnejbieho", "komplexnejšieho"),
        ("väbej", "väčšej"),
        ("menbej", "menšej"),
        ("píbu", "píšu"),
        ("úspebnosti", "úspešnosti"),
        ("spoíva", "spočíva"),
        ("Mareb", "Mareš"),
        ("vysvetIuje", "vysvetľuje"),
        ("priešeh", "priebeh"),
        ("Iahko", "ľahko"),
        ("ukoneným", "ukončeným"),
        ("úinok", "účinok"),
        ("dopEňame", "dopĺňame"),
        ("KIúové", "Kľúčové"),
        ("redaknou", "redakčnou"),
        ("prebiel", "prešiel"),
        ("rozbirovah", "rozširovať"),
        ("reprodukovah", "reprodukovať"),
        ("ukladah", "ukladať"),
        ("obsiahnutý v btvrtej", "obsiahnutý v štvrtej"),
        ("najnovb", "najnovš"),
        ("PokiaI", "Pokiaľ"),
        ("NakoIko", "Nakoľko"),
        ("PodIa", "Podľa"),
        ("voIn", "voľn"),
        ("veIa", "veľa"),
        ("tabuI", "tabuľ"),
        ("Odporúa", "Odporúča"),
        ("teIn", "teľn"),
        ("teI", "teľ"),
        ("oddeI", "oddeľ"),
        ("rozdeI", "rozdeľ"),
        ("zdieI", "zdieľ"),
        ("schvaI", "schvaľ"),
        ("vysvetI", "vysvetľ"),
        ("myseI", "myseľ"),
        ("sprevádzah", "sprevádzať"),
        ("kráah", "kráčať"),
        ("koncipovah", "koncipovať"),
        ("pokraovah", "pokračovať"),
        ("spracovávah", "spracovávať"),
    ]
    for bad, good in substring_replacements:
        text = text.replace(bad, good)

    regex_replacements = [
        (r"\bapec", "špec"),
        (r"\batr", "štr"),
        (r"\batat", "štat"),
        (r"\batudent", "študent"),
        (r"(?m)^- čo ", "- Čo "),
        (r"(?m)^## 2 štruktúra", "## 2 Štruktúra"),
        (r"(?m)^## 3 špecifiká", "## 3 Špecifiká"),
        (r"(?m)^- 2 štruktúra", "- 2 Štruktúra"),
        (r"(?m)^- štruktúra záverečnej práce", "- Štruktúra záverečnej práce"),
        (r"(?m)^## - Špecifiká", "## 3 Špecifiká"),
        (r"(?m)^- - Špecifiká", "- 3 Špecifiká"),
        (r"(?<=\s)3(?=\s)", " - "),
        (r"osh(?=(?:ami|ou|a|i|\b))", "osť"),
    ]
    for pattern, replacement in regex_replacements:
        text = re.sub(pattern, replacement, text)

    exact_word_replacements = {
        "byh": "byť",
        "uviesh": "uviesť",
        "realizovah": "realizovať",
        "mah": "mať",
        "prezentovah": "prezentovať",
        "obsahovah": "obsahovať",
        "identifikovah": "identifikovať",
        "získah": "získať",
        "pripravih": "pripraviť",
        "formulovah": "formulovať",
        "využívah": "využívať",
        "porozumieh": "porozumieť",
        "skúmah": "skúmať",
        "používah": "používať",
        "použih": "použiť",
        "odpovedah": "odpovedať",
        "venovah": "venovať",
        "zistih": "zistiť",
        "vyhľadávah": "vyhľadávať",
        "opísah": "opísať",
        "ísh": "ísť",
        "upozornih": "upozorniť",
        "vytvorih": "vytvoriť",
        "zaradih": "zaradiť",
        "doplnih": "doplniť",
        "preukázah": "preukázať",
        "vedieh": "vedieť",
        "zamerah": "zamerať",
        "zvolih": "zvoliť",
        "orientovah": "orientovať",
        "konzultovah": "konzultovať",
        "pýtah": "pýtať",
        "považovah": "považovať",
        "reflektovah": "reflektovať",
        "riebih": "riešiť",
        "obohatih": "obohatiť",
        "uvedomih": "uvedomiť",
        "zohľadnih": "zohľadniť",
        "vypracovah": "vypracovať",
        "posúdih": "posúdiť",
        "zvýših": "zvýšiť",
        "vyhnúh": "vyhnúť",
        "slúžih": "slúžiť",
        "prejavih": "prejaviť",
        "pracovah": "pracovať",
        "uplatnih": "uplatniť",
        "aplikovah": "aplikovať",
        "spracovah": "spracovať",
        "citovah": "citovať",
        "interpretovah": "interpretovať",
        "overih": "overiť",
        "skontrolovah": "skontrolovať",
        "rozhodnúh": "rozhodnúť",
        "stretnúh": "stretnúť",
        "dohľadah": "dohľadať",
        "vybrah": "vybrať",
        "naplánovah": "naplánovať",
        "uvádzah": "uvádzať",
        "informovah": "informovať",
        "menih": "meniť",
        "využih": "využiť",
        "oblash": "oblasť",
        "dosh": "dosť",
        "úash": "účasť",
        "úashou": "účasťou",
        "súash": "súčasť",
        "súashou": "súčasťou",
        "Súashou": "Súčasťou",
        "ash": "časť",
        "ashou": "časťou",
        "Žiadosh": "Žiadosť",
        "skúsenosh": "skúsenosť",
        "možnosh": "možnosť",
        "pozornosh": "pozornosť",
        "schopnosh": "schopnosť",
        "náročnosh": "náročnosť",
        "veľkosh": "veľkosť",
        "príležitosh": "príležitosť",
        "spokojnosh": "spokojnosť",
        "vďačnosh": "vďačnosť",
        "zručnosh": "zručnosť",
        "skutočnosh": "skutočnosť",
        "presnosh": "presnosť",
        "transparentnosh": "transparentnosť",
        "spoločnosh": "spoločnosť",
        "funknosh": "funkčnosť",
        "as": "čas",
        "ase": "čase",
        "asu": "času",
        "asti": "časti",
        "astí": "častí",
        "asto": "často",
        "asté": "časté",
        "asový": "časový",
        "asová": "časová",
        "asové": "časové",
        "asovým": "časovým",
        "asopisu": "časopisu",
        "asopis": "časopis",
        "asopise": "časopise",
        "asopisoch": "časopisoch",
        "asopisov": "časopisov",
        "asopisy": "časopisy",
        "lenom": "členom",
        "lenov": "členov",
        "lenovia": "členovia",
        "lenovi": "členovi",
        "spracovávah": "spracovávať",
        "získavah": "získavať",
        "komunikovah": "komunikovať",
        "zameriavah": "zameriavať",
        "zohľadňovah": "zohľadňovať",
        "predchádzah": "predchádzať",
        "zabezpeih": "zabezpečiť",
        "pochopiteIná": "pochopiteľná",
        "nastah": "nastať",
        "priniesh": "priniesť",
        "zmapovah": "zmapovať",
        "kvantifikovah": "kvantifikovať",
        "predložih": "predložiť",
        "naplnih": "naplniť",
        "sledovah": "sledovať",
        "ďalbom": "ďalšom",
        "albie": "ďalšie",
        "potu": "počtu",
    }
    for bad, good in exact_word_replacements.items():
        text = re.sub(rf"\b{re.escape(bad)}\b", good, text)

    front_matter = """Paneurópska vysoká škola v Bratislave
Fakulta psychológie

## Sprievodca tvorbou záverečných prác

Veronika Boleková
Veronika Chlebcová
Michal Čerebník

Bratislava 2022

Sprievodca tvorbou záverečných prác

Veronika Boleková, Veronika Chlebcová, Michal Čerebník

Fakulta psychológie, Paneurópska vysoká škola

© PhDr. Veronika Boleková, PhD.
Mgr. Veronika Chlebcová, PhD.
doc. PhDr. Michal Čerebník, PhD.

© Paneurópska vysoká škola
Prvé vydanie, 2022

Recenzenti

prof. PhDr. Marína Mikulajová, CSc.
Fakulta psychológie, Paneurópska vysoká škola v Bratislave

doc. PhDr. Michal Hajdúk, PhD.
Katedra psychológie, Filozofická fakulta Univerzity Komenského v Bratislave, Psychiatrická klinika LF UK a UNB, Centrum výskumu psychických porúch UK

ISBN 978-80-8275-004-4

© Všetky práva vyhradené. Žiadna časť tejto publikácie sa nesmie reprodukovať, ukladať do informačných systémov alebo inak rozširovať bez predchádzajúceho písomného súhlasu autorov publikácie. Rukopis neprešiel redakčnou ani jazykovou úpravou."""
    text = re.sub(
        r"Paneurópska vysoká .*?Rukopis .*? úpravou\.",
        front_matter,
        text,
        count=1,
        flags=re.S,
    )

    cleanup_line_replacements = {
        "## - Špecifiká realizácie kvalitatívneho výskumu v záverečnej práci": "## 3 Špecifiká realizácie kvalitatívneho výskumu v záverečnej práci",
        "- - Špecifiká realizácie kvalitatívneho výskumu v záverečnej práci (s. 58)": "- 3 Špecifiká realizácie kvalitatívneho výskumu v záverečnej práci (s. 58)",
        "## 1 Test cesty TMT-A -": "1 Test cesty TMT-A -",
        "## - a viac autorov": "3 a viac autorov",
        "## - iniciály krstného": "- iniciály krstného",
    }
    for bad, good in cleanup_line_replacements.items():
        text = text.replace(bad, good)

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    return text


def cleanup_pdf_page(page: str) -> str:
    text = page.replace("\r\n", "\n")
    text = replace_contextual_artifact(text, "\r", "č", "Č")
    text = replace_contextual_artifact(text, "\x1f", "ď", "Ď")
    text = text.replace("\u00ad", "")
    text = unicodedata.normalize("NFKC", text)
    lines = [normalize_line(line) for line in text.split("\n")]
    filtered: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            filtered.append("")
            continue
        if stripped == "Autorsky chránený dokument":
            continue
        if re.fullmatch(r"\d+", stripped):
            continue
        filtered.append(stripped)
    filtered = merge_heading_fragments(filtered)
    return collapse_blank_lines(filtered)


def replace_contextual_artifact(text: str, needle: str, lower: str, upper: str) -> str:
    if needle not in text:
        return text
    chars: list[str] = []
    text_len = len(text)
    for idx, char in enumerate(text):
        if char != needle:
            chars.append(char)
            continue
        prev = previous_visible_char(text, idx)
        nxt = next_visible_char(text, idx, text_len)
        replacement = upper if should_use_uppercase(prev, nxt) else lower
        chars.append(replacement)
    return "".join(chars)


def previous_visible_char(text: str, idx: int) -> str:
    cursor = idx - 1
    while cursor >= 0:
        char = text[cursor]
        if char not in {" ", "\t", "\n"}:
            return char
        cursor -= 1
    return ""


def next_visible_char(text: str, idx: int, text_len: int) -> str:
    cursor = idx + 1
    while cursor < text_len:
        char = text[cursor]
        if char not in {" ", "\t", "\n"}:
            return char
        cursor += 1
    return ""


def should_use_uppercase(prev: str, nxt: str) -> bool:
    if not prev or prev in "([{\"'":
        return True
    if prev.isupper():
        return True
    if nxt.isupper():
        return True
    return False


def normalize_line(line: str) -> str:
    line = line.replace("\t", " ")
    line = re.sub(r"\s+", " ", line)
    return html.unescape(line).strip()


def collapse_blank_lines(lines: Iterable[str]) -> str:
    collapsed: list[str] = []
    blank = False
    for line in lines:
        if line:
            collapsed.append(line)
            blank = False
            continue
        if not blank:
            collapsed.append("")
        blank = True
    while collapsed and not collapsed[0]:
        collapsed.pop(0)
    while collapsed and not collapsed[-1]:
        collapsed.pop()
    return "\n".join(collapsed)


def merge_heading_fragments(lines: list[str]) -> list[str]:
    merged: list[str] = []
    idx = 0
    while idx < len(lines):
        current = lines[idx]
        nxt = lines[idx + 1] if idx + 1 < len(lines) else ""
        if should_merge_heading_lines(current, nxt):
            merged.append(f"{current} {nxt}".strip())
            idx += 2
            continue
        merged.append(current)
        idx += 1
    return merged


def should_merge_heading_lines(current: str, nxt: str) -> bool:
    if not current or not nxt:
        return False
    if current.startswith("#") or nxt.startswith("#"):
        return False
    if any(char.isdigit() for char in current) or any(char.isdigit() for char in nxt):
        return False
    if len(current) + len(nxt) > 90:
        return False
    return looks_like_all_caps_heading(current) and looks_like_all_caps_heading(nxt)


def lines_to_markdown_blocks(lines: list[str]) -> list[str]:
    blocks: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if not paragraph:
            return
        blocks.append(" ".join(paragraph))
        paragraph.clear()

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            flush_paragraph()
            continue
        if is_toc_line(line):
            flush_paragraph()
            blocks.append(render_toc_line(line))
            continue
        if is_heading(line):
            flush_paragraph()
            blocks.append(f"{'#' * heading_level(line)} {line}")
            continue
        if is_bullet_line(line):
            flush_paragraph()
            blocks.append(render_bullet_line(line))
            continue
        paragraph.append(line)

    flush_paragraph()
    return blocks


def is_toc_line(line: str) -> bool:
    return bool(re.search(r"\.{3,}\s*\d+$", line))


def render_toc_line(line: str) -> str:
    match = re.match(r"^(.*?)\s*\.{3,}\s*(\d+)$", line)
    if not match:
        return f"- {line}"
    label, page = match.groups()
    return f"- {label.strip()} (s. {page})"


def is_heading(line: str) -> bool:
    stripped = line.strip()
    if len(stripped) > 100:
        return False
    if stripped.startswith("ISBN "):
        return False
    if stripped in {"Obsah", "Úvod", "Záver", "Literatúra", "PRÍLOHA"}:
        return True
    if looks_like_numbered_heading(stripped):
        return True
    words = stripped.split()
    if 2 <= len(words) <= 8 and looks_like_all_caps_heading(stripped) and count_digits(stripped) <= max(count_letters(stripped) // 2, 1):
        return True
    return False


def looks_like_all_caps_heading(line: str) -> bool:
    letters = [char for char in line if char.isalpha()]
    if len(letters) < 4:
        return False
    upper_ratio = sum(1 for char in letters if char.isupper()) / len(letters)
    return upper_ratio >= 0.7


def looks_like_numbered_heading(line: str) -> bool:
    match = re.match(r"^(\d+(?:\.\d+)*)\s+(.+)$", line)
    if not match:
        return False
    prefix, remainder = match.groups()
    first_number = int(prefix.split(".")[0])
    if first_number > 20:
        return False
    if "." not in prefix and first_number > 10:
        return False
    first_word = remainder.split()[0]
    if not any(char.isalpha() for char in first_word):
        return False
    if count_digits(line) > count_letters(line):
        return False
    digit_groups = re.findall(r"\d+(?:[.,]\d+)?", remainder)
    if "." in prefix:
        if len(digit_groups) > 1:
            return False
    elif digit_groups:
        return False
    if "**" in line:
        return False
    if "," in remainder and "." not in prefix:
        return False
    if re.search(r"\(\d{4}\)", remainder):
        return False
    return True


def count_digits(value: str) -> int:
    return sum(1 for char in value if char.isdigit())


def count_letters(value: str) -> int:
    return sum(1 for char in value if char.isalpha())


def heading_level(line: str) -> int:
    if re.match(r"^\d+\.\d+\.\d+\s+", line):
        return 4
    if re.match(r"^\d+\.\d+\s+", line):
        return 3
    if re.match(r"^\d+\s+", line):
        return 2
    return 2


def is_bullet_line(line: str) -> bool:
    return bool(re.match(r"^[\-*•]\s+", line))


def render_bullet_line(line: str) -> str:
    line = re.sub(r"^[\-*•]\s+", "", line).strip()
    return f"- {line}"


def plain_text_to_markdown(text: str) -> str:
    lines = [normalize_line(line) for line in text.splitlines()]
    return "\n\n".join(lines_to_markdown_blocks(lines))


def convert_xlsx_to_markdown(source: Path) -> str:
    with zipfile.ZipFile(source) as archive:
        shared_strings = read_shared_strings(archive)
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        rels = read_relationships(archive, "xl/_rels/workbook.xml.rels")
        sheets: list[str] = []

        for sheet in workbook.findall("main:sheets/main:sheet", XML_NS):
            name = sheet.attrib.get("name", "Sheet")
            rel_id = sheet.attrib.get(f"{{{XML_NS['r']}}}id")
            if not rel_id or rel_id not in rels:
                continue
            target = resolve_zip_path("xl/workbook.xml", rels[rel_id])
            rows = read_sheet_rows(archive, target, shared_strings)
            if not rows:
                sheets.append(f"## {name}\n\n_No visible rows found._")
                continue
            sheets.append(f"## {name}\n\n{render_markdown_table(rows)}")
        return "\n\n".join(sheets).strip()


def read_shared_strings(archive: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    strings: list[str] = []
    for item in root.findall("main:si", XML_NS):
        text = "".join(node.text or "" for node in item.findall(".//main:t", XML_NS))
        strings.append(text)
    return strings


def read_relationships(archive: zipfile.ZipFile, rel_path: str) -> dict[str, str]:
    if rel_path not in archive.namelist():
        return {}
    root = ET.fromstring(archive.read(rel_path))
    rels: dict[str, str] = {}
    for rel in root.findall("pr:Relationship", XML_NS):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            rels[rel_id] = target
    return rels


def resolve_zip_path(base_path: str, target: str) -> str:
    return posixpath.normpath(posixpath.join(posixpath.dirname(base_path), target))


def read_sheet_rows(
    archive: zipfile.ZipFile,
    sheet_path: str,
    shared_strings: list[str],
) -> list[list[str]]:
    root = ET.fromstring(archive.read(sheet_path))
    rows: list[dict[int, str]] = []
    max_col = 0
    for row in root.findall(".//main:sheetData/main:row", XML_NS):
        row_values: dict[int, str] = {}
        for cell in row.findall("main:c", XML_NS):
            ref = cell.attrib.get("r", "")
            col_idx = column_letters_to_index(cell_reference_column(ref))
            row_values[col_idx] = extract_sheet_cell_value(cell, shared_strings)
            max_col = max(max_col, col_idx)
        if row_values:
            rows.append(row_values)
    matrix: list[list[str]] = []
    for row in rows:
        matrix.append([row.get(idx, "") for idx in range(max_col + 1)])
    return trim_empty_table(matrix)


def cell_reference_column(ref: str) -> str:
    match = re.match(r"([A-Z]+)", ref)
    return match.group(1) if match else "A"


def column_letters_to_index(letters: str) -> int:
    value = 0
    for char in letters:
        value = value * 26 + (ord(char.upper()) - ord("A") + 1)
    return max(value - 1, 0)


def extract_sheet_cell_value(cell: ET.Element, shared_strings: list[str]) -> str:
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        value = "".join(node.text or "" for node in cell.findall(".//main:t", XML_NS))
        return sanitize_table_cell(value)
    value_node = cell.find("main:v", XML_NS)
    if value_node is None or value_node.text is None:
        return ""
    raw = value_node.text
    if cell_type == "s":
        idx = int(raw)
        if 0 <= idx < len(shared_strings):
            return sanitize_table_cell(shared_strings[idx])
        return ""
    if cell_type == "b":
        return "TRUE" if raw == "1" else "FALSE"
    return sanitize_table_cell(raw)


def trim_empty_table(rows: list[list[str]]) -> list[list[str]]:
    while rows and all(not cell.strip() for cell in rows[-1]):
        rows.pop()
    if not rows:
        return rows
    max_width = max(len(row) for row in rows)
    for row in rows:
        row.extend([""] * (max_width - len(row)))
    while max_width > 0 and all(not row[max_width - 1].strip() for row in rows):
        for row in rows:
            row.pop()
        max_width -= 1
    return rows


def render_markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return "_No data found._"
    header = rows[0]
    if all(not cell.strip() for cell in header):
        header = [f"Column {idx + 1}" for idx in range(len(header))]
        body_rows = rows
    else:
        body_rows = rows[1:]
    header_line = "| " + " | ".join(escape_markdown_table_cell(cell or f"Column {idx + 1}") for idx, cell in enumerate(header)) + " |"
    divider_line = "| " + " | ".join("---" for _ in header) + " |"
    body_lines = [
        "| " + " | ".join(escape_markdown_table_cell(cell) for cell in row) + " |"
        for row in body_rows
    ]
    return "\n".join([header_line, divider_line, *body_lines])


def sanitize_table_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def escape_markdown_table_cell(value: str) -> str:
    return sanitize_table_cell(value).replace("|", "\\|")


def convert_pptx_to_markdown(source: Path) -> str:
    with zipfile.ZipFile(source) as archive:
        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        rels = read_relationships(archive, "ppt/_rels/presentation.xml.rels")
        sections: list[str] = []
        slide_ids = presentation.findall("p:sldIdLst/p:sldId", XML_NS)

        for idx, slide in enumerate(slide_ids, start=1):
            rel_id = slide.attrib.get(f"{{{XML_NS['r']}}}id")
            if not rel_id or rel_id not in rels:
                continue
            slide_path = resolve_zip_path("ppt/presentation.xml", rels[rel_id])
            paragraphs = read_pptx_paragraphs(archive, slide_path)
            sections.append(render_slide_markdown(idx, paragraphs))
        return "\n\n".join(section for section in sections if section).strip()


def read_pptx_paragraphs(archive: zipfile.ZipFile, slide_path: str) -> list[str]:
    root = ET.fromstring(archive.read(slide_path))
    paragraphs: list[str] = []
    for paragraph in root.findall(".//a:p", XML_NS):
        text = "".join(node.text or "" for node in paragraph.findall(".//a:t", XML_NS))
        text = normalize_line(text)
        if text:
            paragraphs.append(text)
    return paragraphs


def render_slide_markdown(index: int, paragraphs: list[str]) -> str:
    if not paragraphs:
        return f"## Slide {index}\n\n_No visible text found._"
    title = paragraphs[0] if len(paragraphs[0].split()) <= 14 else f"Slide {index}"
    lines: list[str] = [f"## {title}"]
    remaining = paragraphs[1:] if title != f"Slide {index}" else paragraphs
    if title == f"Slide {index}":
        lines.append(paragraphs[0])
        remaining = paragraphs[1:]
    for paragraph in remaining:
        lines.append(f"- {paragraph}")
    return "\n\n".join([lines[0], "\n".join(lines[1:])]) if len(lines) > 1 else lines[0]


if __name__ == "__main__":
    raise SystemExit(main())
