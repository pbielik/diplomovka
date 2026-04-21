-- tools/normalize_emphasis_for_word.lua
--
-- Word-facing emphasis normalization:
--   - removes inline bold from running prose,
--   - keeps heading styles untouched,
--   - preserves selected technical labels and front-matter labels,
--   - leaves italics available for foreign or technical terms.

local function strip_strong_inlines(inlines)
  return inlines:walk({
    Strong = function(elem)
      return elem.content
    end,
  })
end

local function is_bold_label_paragraph(text)
  return text:match("^VO%d+%.")
    or text:match("^H%d+%.")
    or text:match("^Blok [A-Z]")
    or text:match("^Kľúčové slová:")
    or text:match("^Key words:")
    or text:match("^Tabuľka [A-Z]?%d")
    or text:match("^Obrázok [A-Z]?%d")
end

local function is_single_strong_paragraph(block)
  return #block.content == 1 and block.content[1].t == "Strong"
end

local function normalize_block(block)
  local text = pandoc.utils.stringify(block)
  if text == "" then
    return block
  end

  if is_single_strong_paragraph(block) or is_bold_label_paragraph(text) then
    return block
  end

  block.content = strip_strong_inlines(block.content)
  return block
end

function Para(elem)
  return normalize_block(elem)
end

function Plain(elem)
  return normalize_block(elem)
end
