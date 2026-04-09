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
OUTPUT="diplomovka_plan_b_citekeys.docx"

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

if ! command -v pandoc >/dev/null 2>&1; then
  echo "CHYBA: pandoc nie je nainštalovaný" >&2
  exit 1
fi

echo "Generujem $OUTPUT z ${#INPUT_FILES[@]} súborov (Plan B: citekeys ostávajú v texte)..."

pandoc \
  "${INPUT_FILES[@]}" \
  --from=markdown \
  --to=docx \
  --metadata=lang:sk-SK \
  --lua-filter="$LUA" \
  --output="$OUTPUT"

echo "Hotovo: $OUTPUT"
