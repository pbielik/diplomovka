#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

BUILD_DIR="/tmp/diplomovka_near_final_build"
RESULTS_BUILD="$BUILD_DIR/40_results_built.md"
APPENDIX_BUILD="$BUILD_DIR/71_public_appendix_built.md"
FRONTMATTER_BUILD="$BUILD_DIR/10_front_matter_near_final.md"
RESULTS_ASSET_BUILDER="$REPO_ROOT/analysis/scripts/build_full_run_results_assets.py"
FRONTMATTER_BUILDER="$REPO_ROOT/tools/build_front_matter.py"
TABLE_STYLE_POSTPROCESSOR="$REPO_ROOT/tools/apply_table_style_to_docx.py"
NEAR_FINAL_POSTPROCESSOR="$REPO_ROOT/tools/apply_near_final_word_template.py"
REFERENCE_DOC="${REFERENCE_DOC:-$REPO_ROOT/final thesis/Diplomová práca v0.2.docx}"
OUTPUT_DOCX="${OUTPUT_DOCX:-$REPO_ROOT/diplomovka_near_final.docx}"
APPENDIX_SOURCE="${APPENDIX_SOURCE:-$REPO_ROOT/manuscript/71_public_appendix_draft.md}"
PANDOC_BIN="${PANDOC_BIN:-}"
EMPHASIS_FILTER="$REPO_ROOT/tools/normalize_emphasis_for_word.lua"

if [[ ! -f "$RESULTS_ASSET_BUILDER" ]]; then
  echo "CHYBA: chýba build script pre Results: $RESULTS_ASSET_BUILDER" >&2
  exit 1
fi

if [[ ! -f "$FRONTMATTER_BUILDER" ]]; then
  echo "CHYBA: chýba builder front matter: $FRONTMATTER_BUILDER" >&2
  exit 1
fi

if [[ ! -f "$TABLE_STYLE_POSTPROCESSOR" ]]; then
  echo "CHYBA: chýba DOCX table postprocessor: $TABLE_STYLE_POSTPROCESSOR" >&2
  exit 1
fi

if [[ ! -f "$NEAR_FINAL_POSTPROCESSOR" ]]; then
  echo "CHYBA: chýba near-final DOCX postprocessor: $NEAR_FINAL_POSTPROCESSOR" >&2
  exit 1
fi

if [[ ! -f "$EMPHASIS_FILTER" ]]; then
  echo "CHYBA: chýba emphasis filter: $EMPHASIS_FILTER" >&2
  exit 1
fi

if [[ ! -f "$REFERENCE_DOC" ]]; then
  echo "CHYBA: chýba reference DOCX: $REFERENCE_DOC" >&2
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
python3 "$RESULTS_ASSET_BUILDER" --output "$RESULTS_BUILD" --appendix-output "$APPENDIX_BUILD"
python3 "$FRONTMATTER_BUILDER" "$REPO_ROOT/manuscript/10_title_abstract.md" --output "$FRONTMATTER_BUILD"

INPUT_FILES=(
  "$FRONTMATTER_BUILD"
  "$REPO_ROOT/manuscript/20_introduction.md"
  "$REPO_ROOT/manuscript/30_method.md"
  "$RESULTS_BUILD"
  "$REPO_ROOT/manuscript/50_discussion.md"
  "$REPO_ROOT/manuscript/60_conclusion.md"
)

if [[ -f "$APPENDIX_BUILD" ]]; then
  INPUT_FILES+=("$APPENDIX_BUILD")
elif [[ -f "$APPENDIX_SOURCE" ]]; then
  INPUT_FILES+=("$APPENDIX_SOURCE")
fi

echo "Generujem near-final Word build do $OUTPUT_DOCX ..."

"$PANDOC_BIN" \
  "${INPUT_FILES[@]}" \
  --from=markdown \
  --to=docx \
  --reference-doc="$REFERENCE_DOC" \
  --metadata=lang:sk-SK \
  --lua-filter="$REPO_ROOT/tools/drop_drafting_notes.lua" \
  --lua-filter="$EMPHASIS_FILTER" \
  --lua-filter="$REPO_ROOT/tools/normalize_headings_for_reference_doc.lua" \
  --output="$OUTPUT_DOCX"

python3 "$TABLE_STYLE_POSTPROCESSOR" "$OUTPUT_DOCX"
python3 "$NEAR_FINAL_POSTPROCESSOR" "$OUTPUT_DOCX"

ls -lh "$OUTPUT_DOCX"
