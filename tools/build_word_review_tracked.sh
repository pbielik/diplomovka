#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

CSV_PATH="${1:-$HOME/Downloads/mdd-ai-simulation_ratings_wide (4).csv}"
SOURCE_DOCX="$REPO_ROOT/diplomovka_preview_current_export.docx"
OUTPUT_DOCX="$REPO_ROOT/diplomovka_review_tracked.docx"
TRACK_CHANGES_POSTPROCESSOR="$REPO_ROOT/tools/enable_track_changes_docx.py"

if [[ ! -f "$TRACK_CHANGES_POSTPROCESSOR" ]]; then
  echo "CHYBA: chýba postprocessor: $TRACK_CHANGES_POSTPROCESSOR" >&2
  exit 1
fi

bash "$REPO_ROOT/tools/build_word_preview_current_export.sh" "$CSV_PATH"
python3 "$TRACK_CHANGES_POSTPROCESSOR" "$SOURCE_DOCX" "$OUTPUT_DOCX"

ls -lh "$OUTPUT_DOCX"
