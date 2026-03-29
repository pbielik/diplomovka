# AI Tools

Nastroje v tomto priecinku sluzia na lokalnu pripravu podkladov pre diplomovku.

## `doc_to_markdown.py`

CLI konverter dokumentov do Markdownu.

Podporovane vstupy:

- `pdf`
- `docx`
- `doc`
- `xlsx`
- `pptx`

Pouzitie:

```bash
python3 tools/ai-tools/doc_to_markdown.py "docs/guides/1_Sprievodca tvorbou ZP.pdf" "docs/guides/sprievodca-zaverecnych-prac.md" --title "Sprievodca tvorbou zaverecnych prac"
```

Pri PDF s rozbitym font encodingom sa oplati zapnut OCR fallback:

```bash
python3 tools/ai-tools/doc_to_markdown.py --pdf-ocr "docs/guides/1_Sprievodca tvorbou ZP.pdf" "docs/guides/sprievodca-zaverecnych-prac.md" --title "Sprievodca tvorbou zaverecnych prac"
```

Poznamky k backendom:

- `pdf`: macOS `PDFKit` cez `swift`, volitelne s OCR fallbackom cez Apple Vision
- `docx`: `pandoc`
- `doc`: `textutil`, pripadne `pandoc` na prevod HTML do Markdownu
- `xlsx`: vlastny parser OOXML v standardnej kniznici Pythonu
- `pptx`: vlastny parser OOXML v standardnej kniznici Pythonu

Limity:

- PDF prevod je best-effort. Pri niektorych PDF s problematickym font encodingom moze byt potrebna rucna oprava diakritiky alebo formatovania.
- `--pdf-ocr` je pomalsi, ale casto da lepsi vysledok pri skenoch alebo PDF s pokazenou textovou vrstvou.
- `xls` a `ppt` (stare binarne Office formaty) tento skript zatial nepodporuje.
