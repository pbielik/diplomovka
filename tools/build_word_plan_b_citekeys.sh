#!/usr/bin/env bash
# build_word_plan_b_citekeys.sh
#
# Plan B Word export rukopisu pre workflow:
#   markdown -> clean .docx s ponechanými citekeys -> manuálne nahradenie
#   citácií vo Worde cez Zotero plugin.
#
# Oproti `build_word_clean.sh`:
#   - NEPOUŽÍVA `--citeproc`
#   - NEVKLADÁ plain-text APA citácie
#   - ponecháva `[@citekey]` priamo v texte .docx
#   - stále aplikuje `tools/strip_heading_numbers.lua`, aby bol export vhodný
#     na paste do cieľového Word template-u
#
# Použitie:
#   ./tools/build_word_plan_b_citekeys.sh
#
# Výstup:
#   diplomovka_plan_b_citekeys.docx
#
# Word workflow:
#   1. otvor .docx
#   2. cez Zotero plugin nahradzuj jednotlivé `[@citekey]` citáciami
#      pomocou Add/Edit Citation
#   3. nakoniec použi Insert Bibliography

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

LUA="tools/strip_heading_numbers.lua"
TABLE_STYLE_POSTPROCESSOR="tools/apply_table_style_to_docx.py"
OUTPUT="diplomovka_plan_b_citekeys.docx"
PANDOC_BIN="${PANDOC_BIN:-}"

for f in "${INPUT_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "CHYBA: vstupný súbor neexistuje: $f" >&2
    exit 1
  fi
done

if [[ ! -f "$LUA" ]]; then
  echo "CHYBA: Lua filter neexistuje: $LUA" >&2
  exit 1
fi

if [[ ! -f "$TABLE_STYLE_POSTPROCESSOR" ]]; then
  echo "CHYBA: DOCX table postprocessor neexistuje: $TABLE_STYLE_POSTPROCESSOR" >&2
  exit 1
fi

if [[ -z "$PANDOC_BIN" ]]; then
  if command -v pandoc >/dev/null 2>&1; then
    PANDOC_BIN="$(command -v pandoc)"
  elif [[ -x "/opt/homebrew/bin/pandoc" ]]; then
    PANDOC_BIN="/opt/homebrew/bin/pandoc"
  else
    echo "CHYBA: pandoc nie je nainštalovaný" >&2
    exit 1
  fi
fi

echo "Generujem $OUTPUT z ${#INPUT_FILES[@]} súborov (Plan B: citekeys ostávajú v texte)..."

"$PANDOC_BIN" \
  "${INPUT_FILES[@]}" \
  --from=markdown \
  --to=docx \
  --metadata=lang:sk-SK \
  --lua-filter="$LUA" \
  --output="$OUTPUT"

python3 "$TABLE_STYLE_POSTPROCESSOR" "$OUTPUT"

echo "Hotovo: $OUTPUT"
