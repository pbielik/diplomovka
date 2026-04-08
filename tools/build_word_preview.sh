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

# Vstupné súbory v poradí IMRaD.
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
OUTPUT="diplomovka_preview.docx"

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

if ! command -v pandoc >/dev/null 2>&1; then
  echo "CHYBA: pandoc nie je nainštalovaný" >&2
  exit 1
fi

echo "Generujem $OUTPUT z ${#INPUT_FILES[@]} súborov..."

pandoc \
  "${INPUT_FILES[@]}" \
  --from=markdown \
  --to=docx \
  --citeproc \
  --bibliography="$BIB" \
  --csl="$CSL" \
  --metadata=lang:sk-SK \
  --metadata=link-citations:true \
  --output="$OUTPUT"

echo "Hotovo: $OUTPUT"
