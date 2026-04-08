#!/usr/bin/env bash
# build_word_clean.sh
#
# Clean Word export rukopisu pre paste do cieľového Word template-u.
#
# Oproti `build_word_preview.sh` aplikuje Lua filter
# `tools/strip_heading_numbers.lua`, ktorý:
#   - zhodí file-level h1 nadpisy ("# 10 Title abstract" ... "# 60 Conclusion"),
#   - odstráni numerické prefixy zo všetkých zostávajúcich nadpisov
#     ("## 1 Úvod" → "Úvod", "### 1.5.1 ..." → "..."),
#   - posunie h2..h6 o jeden level nižšie, takže chapter "## 1 Úvod" sa stane
#     h1 v .docx-e a cieľový Word template môže prebrať vlastné heading štýly
#     a auto-číslovanie.
#
# Použitie:
#   ./tools/build_word_clean.sh
#
# Vstup:
#   manuscript/10_title_abstract.md
#   manuscript/20_introduction.md
#   manuscript/30_method.md
#   manuscript/40_results.md
#   manuscript/50_discussion.md
#   manuscript/60_conclusion.md
#
# Výstup:
#   diplomovka_clean.docx (v koreni repa)
#
# Word strana: pri kopírovaní do cieľového dokumentu použi
#   Cmd+Ctrl+V → "Use Destination Styles"
# (alebo Home → Paste Special → Use Destination Styles), aby cieľový template
# prevzal heading štýly, tučné/kurzívu, zoznamy a tabuľky podľa svojich
# vlastných nastavení.
#
# Poznámka: Tento výstup je preview pre paste workflow, NIE final submission.
# Finálne živé Zotero citácie sa podľa `AGENTS.md` sekcia 11 robia vo Worde
# cez Zotero plugin (Add/Edit Citation, Insert Bibliography).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

INPUT_FILES=(
  "manuscript/10_title_abstract.md"
  "manuscript/20_introduction.md"
  "manuscript/30_method.md"
  "manuscript/40_results.md"
  "manuscript/50_discussion.md"
  "manuscript/60_conclusion.md"
)

BIB="references/zotero-thesis.bib"
CSL="$HOME/Zotero/styles/apa.csl"
LUA="tools/strip_heading_numbers.lua"
OUTPUT="diplomovka_clean.docx"

# Sanity checks.
for f in "${INPUT_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "CHYBA: vstupný súbor neexistuje: $f" >&2
    exit 1
  fi
done

if [[ ! -f "$BIB" ]]; then
  echo "CHYBA: bibliografia neexistuje: $BIB" >&2
  exit 1
fi

if [[ ! -f "$CSL" ]]; then
  echo "CHYBA: APA CSL štýl neexistuje: $CSL" >&2
  echo "Tip: Zotero ho zvyčajne nainštaluje do ~/Zotero/styles/apa.csl" >&2
  exit 1
fi

if [[ ! -f "$LUA" ]]; then
  echo "CHYBA: Lua filter neexistuje: $LUA" >&2
  exit 1
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "CHYBA: pandoc nie je nainštalovaný" >&2
  exit 1
fi

echo "Generujem $OUTPUT z ${#INPUT_FILES[@]} súborov (clean: bez čísel, shift -1)..."

pandoc \
  "${INPUT_FILES[@]}" \
  --from=markdown \
  --to=docx \
  --citeproc \
  --bibliography="$BIB" \
  --csl="$CSL" \
  --metadata=lang:sk-SK \
  --metadata=link-citations:true \
  --lua-filter="$LUA" \
  --output="$OUTPUT"

echo "Hotovo: $OUTPUT"
