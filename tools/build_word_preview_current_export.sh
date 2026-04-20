#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

CSV_PATH="${1:-$HOME/Downloads/mdd-ai-simulation_ratings_wide (4).csv}"
R_SCRIPT="$REPO_ROOT/analysis/scripts/build_current_export_preview_assets.R"
TABLE_STYLE_POSTPROCESSOR="$REPO_ROOT/tools/apply_table_style_to_docx.py"
BUILD_DIR="/tmp/diplomovka_current_export_preview_build"
RESULTS_BUILD="$BUILD_DIR/40_results_preview_current_export_built.md"
DISCUSSION_BUILD="$BUILD_DIR/50_discussion_preview_current_export_built.md"
OUTPUT_DOCX="$REPO_ROOT/diplomovka_preview_current_export.docx"

mkdir -p "$BUILD_DIR"

if [[ ! -f "$CSV_PATH" ]]; then
  echo "CHYBA: CSV export neexistuje: $CSV_PATH" >&2
  exit 1
fi

if [[ ! -f "$R_SCRIPT" ]]; then
  echo "CHYBA: chýba build script: $R_SCRIPT" >&2
  exit 1
fi

if [[ ! -f "$TABLE_STYLE_POSTPROCESSOR" ]]; then
  echo "CHYBA: chýba DOCX table postprocessor: $TABLE_STYLE_POSTPROCESSOR" >&2
  exit 1
fi

if [[ ! -f "$HOME/Zotero/styles/apa.csl" ]]; then
  echo "CHYBA: chýba APA CSL štýl v ~/Zotero/styles/apa.csl" >&2
  exit 1
fi

/opt/homebrew/bin/Rscript "$R_SCRIPT" "$CSV_PATH"

python3 - <<'PY'
from pathlib import Path

repo = Path("/Users/pavol.bielik/dev/src/github.com/pbielik/diplomovka")
build_dir = Path("/tmp/diplomovka_current_export_preview_build")
tables_dir = repo / "tables" / "current_export_preview"

results_src = repo / "manuscript" / "40_results_preview_current_export.md"
discussion_src = repo / "manuscript" / "50_discussion_preview_current_export.md"

replacements = {
    "<!-- CURRENT_EXPORT_FRAGMENT_VALIDATION -->": (tables_dir / "fragment_validation.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_DATASET -->": (tables_dir / "fragment_dataset.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_DESCRIPTIVES -->": (tables_dir / "fragment_descriptives.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_MEASUREMENT -->": (tables_dir / "fragment_measurement.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_CELLS -->": (tables_dir / "fragment_cells.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_MODELS -->": (tables_dir / "fragment_models.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_EXPLORATORY -->": (tables_dir / "fragment_exploratory.md").read_text(encoding="utf-8"),
    "<!-- CURRENT_EXPORT_FRAGMENT_ANCHORED -->": (tables_dir / "fragment_anchored.md").read_text(encoding="utf-8"),
}

results_text = results_src.read_text(encoding="utf-8")
for marker, content in replacements.items():
    results_text = results_text.replace(marker, content)

(build_dir / "40_results_preview_current_export_built.md").write_text(results_text, encoding="utf-8")
(build_dir / "50_discussion_preview_current_export_built.md").write_text(
    discussion_src.read_text(encoding="utf-8"),
    encoding="utf-8",
)
PY

/opt/homebrew/bin/pandoc \
  "$REPO_ROOT/manuscript/10_title_abstract.md" \
  "$REPO_ROOT/manuscript/20_introduction.md" \
  "$REPO_ROOT/manuscript/30_method.md" \
  "$RESULTS_BUILD" \
  "$DISCUSSION_BUILD" \
  "$REPO_ROOT/manuscript/60_conclusion.md" \
  --from=markdown \
  --to=docx \
  --citeproc \
  --bibliography="$REPO_ROOT/references/zotero-thesis.bib" \
  --csl="$HOME/Zotero/styles/apa.csl" \
  --metadata=lang:sk-SK \
  --metadata=link-citations:true \
  --lua-filter="$REPO_ROOT/tools/drop_drafting_notes.lua" \
  --output="$OUTPUT_DOCX"

python3 "$TABLE_STYLE_POSTPROCESSOR" "$OUTPUT_DOCX"

ls -lh "$OUTPUT_DOCX"
