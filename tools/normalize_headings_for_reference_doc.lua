-- tools/normalize_headings_for_reference_doc.lua
--
-- Heading filter pre near-final Word build via reference DOCX.
--
-- Oproti clean paste workflow:
--   - NEZHADZUJE hlavný chapter heading o level nižšie,
--   - zachováva H1 pre Úvod / Metóda / Výsledky / Diskusia / Záver,
--   - len odstráni technické prefixy a pri file-level headingoch ponechá
--     slovenský názov za lomkou ("20 Introduction / Úvod" -> "Úvod"),
--   - file-level draft heading pre public appendix balík zahodí, aby sa
--     reálne prílohy riadili svojimi vlastnými headingmi.

local function clone_inlines(inlines)
  local copied = {}
  for _, inline in ipairs(inlines) do
    table.insert(copied, inline)
  end
  return copied
end

local function strip_numeric_prefix(inlines)
  local new_inlines = clone_inlines(inlines)

  if #new_inlines > 0
     and new_inlines[1].t == "Str"
     and new_inlines[1].text:match("^[%d%.]+$") then
    table.remove(new_inlines, 1)
    if #new_inlines > 0 and new_inlines[1].t == "Space" then
      table.remove(new_inlines, 1)
    end
  end

  return new_inlines
end

local function parse_inlines(text)
  local parsed = pandoc.read(text, "markdown")
  if #parsed.blocks == 0 then
    return { pandoc.Str(text) }
  end

  local first_block = parsed.blocks[1]
  if first_block.content then
    return first_block.content
  end

  return { pandoc.Str(text) }
end

function Header(elem)
  local text = pandoc.utils.stringify(elem)

  if elem.level == 1 then
    if text:match("^10%s+") or text:match("^71%s+") then
      return {}
    end

    if text:match("^%d+%s+") then
      local stripped = text:gsub("^%d+%s+", "")
      local slovak = stripped:match(".+/%s*(.+)$")
      local final_text = slovak or stripped
      return pandoc.Header(1, parse_inlines(final_text), elem.attr)
    end

    return elem
  end

  return pandoc.Header(elem.level, strip_numeric_prefix(elem.content), elem.attr)
end
