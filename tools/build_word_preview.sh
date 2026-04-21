#!/usr/bin/env bash
# build_word_preview.sh
#
# Vyrenderuje rukopis diplomovky z markdownu do .docx pomocou pandocu + citeproc.
# Citácie sa z `[@citekey]` placeholderov premenia na APA 7 plain-text citácie
# pomocou `references/zotero-thesis.bib` a CSL štýlu APA 7.
#
# Použitie:
#   ./tools/build_word_preview.sh
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
#   diplomovka_preview.docx (v koreni repa)
#
# Poznámka: Tento výstup je preview, NIE final submission. Finálne citácie sa
# podľa `AGENTS.md` sekcia 11 a `PRIRUCKA_DIPLOMOVKA_AI_ZOTERO_WORD.md` bod 5.3
# robia vo Worde cez Zotero plugin (Add/Edit Citation, Insert Bibliography).

set -euo pipefail

# Prejdi do koreňa repa, nech je skript volateľný odkiaľkoľvek.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

BUILD_DIR="/tmp/diplomovka_full_run_results_build"
RESULTS_BUILD="$BUILD_DIR/40_results_built.md"
RESULTS_ASSET_BUILDER="analysis/scripts/build_full_run_results_assets.py"

# Vstupné súbory v poradí IMRaD.
SOURCE_FILES=(
  "manuscript/10_title_abstract.md"
  "manuscript/20_introduction.md"
  "manuscript/30_method.md"
  "manuscript/50_discussion.md"
  "manuscript/60_conclusion.md"
)

BIB="references/zotero-thesis.bib"
CSL="$HOME/Zotero/styles/apa.csl"
LUA_NOTES="tools/drop_drafting_notes.lua"
LUA_EMPHASIS="tools/normalize_emphasis_for_word.lua"
TABLE_STYLE_POSTPROCESSOR="tools/apply_table_style_to_docx.py"
OUTPUT="diplomovka_preview.docx"
PANDOC_BIN="${PANDOC_BIN:-}"

# Sanity checks.
for f in "${SOURCE_FILES[@]}"; do
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

if [[ ! -f "$LUA_NOTES" ]]; then
  echo "CHYBA: Lua filter neexistuje: $LUA_NOTES" >&2
  exit 1
fi

if [[ ! -f "$LUA_EMPHASIS" ]]; then
  echo "CHYBA: Lua filter neexistuje: $LUA_EMPHASIS" >&2
  exit 1
fi

if [[ ! -f "$TABLE_STYLE_POSTPROCESSOR" ]]; then
  echo "CHYBA: DOCX table postprocessor neexistuje: $TABLE_STYLE_POSTPROCESSOR" >&2
  exit 1
fi

if [[ ! -f "$RESULTS_ASSET_BUILDER" ]]; then
  echo "CHYBA: build script pre Results fragmenty neexistuje: $RESULTS_ASSET_BUILDER" >&2
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

mkdir -p "$BUILD_DIR"
python3 "$RESULTS_ASSET_BUILDER" --output "$RESULTS_BUILD"

INPUT_FILES=(
  "manuscript/10_title_abstract.md"
  "manuscript/20_introduction.md"
  "manuscript/30_method.md"
  "$RESULTS_BUILD"
  "manuscript/50_discussion.md"
  "manuscript/60_conclusion.md"
)

if [[ ! -f "$RESULTS_BUILD" ]]; then
  echo "CHYBA: nevznikol built Results súbor: $RESULTS_BUILD" >&2
  exit 1
fi

echo "Generujem $OUTPUT z ${#INPUT_FILES[@]} súborov..."

"$PANDOC_BIN" \
  "${INPUT_FILES[@]}" \
  --from=markdown \
  --to=docx \
  --citeproc \
  --bibliography="$BIB" \
  --csl="$CSL" \
  --metadata=lang:sk-SK \
  --metadata=link-citations:true \
  --lua-filter="$LUA_NOTES" \
  --lua-filter="$LUA_EMPHASIS" \
  --output="$OUTPUT"

python3 "$TABLE_STYLE_POSTPROCESSOR" "$OUTPUT"

echo "Hotovo: $OUTPUT"
