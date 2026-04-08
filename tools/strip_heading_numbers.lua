-- tools/strip_heading_numbers.lua
--
-- Pandoc Lua filter pre clean Word export diplomovky.
--
-- Robí tri veci v jednom prechode:
--
--   1. Zhodí file-level h1 nadpisy, ktoré začínajú dvojciferným číslom
--      ("# 10 Title abstract", "# 20 Introduction", ..., "# 60 Conclusion").
--      Tieto sú technické názvy súborov, nie reálne kapitolové nadpisy.
--
--   2. Odstráni numerické prefixy z všetkých zostávajúcich nadpisov.
--      Príklady:
--        "## 1 Úvod"                              → "Úvod"
--        "### 1.5.1 Konzistentnosť názvov..."     → "Konzistentnosť názvov..."
--        "#### 2.6.2 Empirické hypotézy – jadro"  → "Empirické hypotézy – jadro"
--
--   3. Posunie heading levels h2..h6 o -1, čiže chapter "## 1 Úvod" sa
--      stane h1 v .docx-e a cieľový Word template môže naň priamo
--      naviazať vlastný štýl Heading 1 (vrátane auto-číslovania).
--
-- Špeciálny prípad: nadpis "# Literatúra" (h1 bez čísla) ostáva ako h1,
-- aby bibliografia vygenerovaná pandoc citeproc-om dostala svoj nadpis.
--
-- Inline obsah nadpisov (Code spans typu `H1`, `–`, kurzíva) sa zachováva.

function Header(elem)
  local text = pandoc.utils.stringify(elem)

  -- 1. Zhodenie file-level h1 nadpisov ("10 ...", "20 ...", ..., "60 ...").
  if elem.level == 1 then
    if text:match("^%d+%s+") then
      return {}
    end
    -- "Literatúra" a iné h1 bez číselného prefixu ostávajú nedotknuté.
    return elem
  end

  -- 2. Strip numerického prefixu pre h2..h6.
  --    Markdown "## 1.5.1 Konzistentnosť" pandoc parsuje ako
  --    [Str "1.5.1", Space, Str "Konzistentnosť"], takže prvý Str element
  --    je samostatný numerický token, ktorý vieme bezpečne odstrániť aj so
  --    samostatným nasledujúcim Space tokenom.
  local new_inlines = {}
  for i, inline in ipairs(elem.content) do
    table.insert(new_inlines, inline)
  end

  if #new_inlines > 0
     and new_inlines[1].t == "Str"
     and new_inlines[1].text:match("^[%d%.]+$") then
    table.remove(new_inlines, 1)
    if #new_inlines > 0 and new_inlines[1].t == "Space" then
      table.remove(new_inlines, 1)
    end
  end

  -- 3. Shift levelu o -1 (h2 → h1, h3 → h2, h4 → h3, ...).
  return pandoc.Header(elem.level - 1, new_inlines, elem.attr)
end
