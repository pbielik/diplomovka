#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

MODE="dry-run"
if [[ "${1:-}" == "--apply" ]]; then
  MODE="apply"
fi

SAFE_PATHS=(
  "Rplots.pdf"
  "analysis/qc_reports"
  "tables/current_export_preview"
  "figures/current_export_preview"
  "tables/styled_preview/expert_review_preview.html"
  "tables/styled_preview/table_s4_expert_review_items.html"
  "tables/styled_preview/table_s5_expert_review_seeds.html"
  "diplomovka_preview_current_export.docx"
)

print_header() {
  echo "== pre_final_run_housekeeping ($MODE) =="
}

has_tracked_files_under() {
  local path="$1"
  [[ -n "$(git ls-files -- "$path")" ]]
}

handle_path() {
  local path="$1"
  if [[ ! -e "$path" ]]; then
    return
  fi

  if has_tracked_files_under "$path"; then
    echo "SKIP tracked: $path"
    return
  fi

  if [[ "$MODE" == "apply" ]]; then
    rm -rf "$path"
    echo "REMOVED: $path"
  else
    echo "WOULD REMOVE: $path"
  fi
}

print_header
for path in "${SAFE_PATHS[@]}"; do
  handle_path "$path"
done

echo
echo "Remaining git status:"
git status --short

cat <<'EOF'

Poznámka:
- skript maže iba známe generované artefakty mimo trackovaných súborov,
- nemení trackované zmeny ani nevolá `git reset` / `git clean`,
- ak po ňom ostáva repo dirty, ide už o reálne úpravy alebo nové súbory, ktoré treba vedome rozhodnúť.
EOF
