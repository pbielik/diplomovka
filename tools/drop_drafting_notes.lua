-- tools/drop_drafting_notes.lua
--
-- Pandoc Lua filter na odstránenie interných draftingových poznámok
-- z Word preview/exportov. Zachováva ich v markdowne, ale neprepúšťa ich
-- do .docx.

local function starts_with(text, prefix)
  return text:sub(1, #prefix) == prefix
end

function BlockQuote(elem)
  local text = pandoc.utils.stringify(elem):gsub("%s+", " ")

  local prefixes = {
    "Pracovný draft kapitoly.",
    "Táto kapitola je pripravená",
    "Doplniť:",
  }

  for _, prefix in ipairs(prefixes) do
    if starts_with(text, prefix) then
      return {}
    end
  end

  return elem
end
