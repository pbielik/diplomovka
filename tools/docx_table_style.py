#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass


PAGE_WIDTH_DXA = 11907
PAGE_HEIGHT_DXA = 16840
MARGIN_DXA = 1440
TEXT_WIDTH_DXA = PAGE_WIDTH_DXA - 2 * MARGIN_DXA


@dataclass(frozen=True)
class TableStylePreset:
    name: str
    font_family: str
    body_font_hp: int
    caption_font_hp: int
    table_header_font_hp: int
    table_body_font_hp: int
    note_font_hp: int
    caption_after: int
    title_after: int
    note_after: int
    table_after: int
    cell_pad_left: int
    cell_pad_right: int
    cell_pad_top: int
    cell_pad_bottom: int
    border_color: str
    border_thick_sz: int
    border_mid_sz: int
    border_thin_sz: int
    default_table_width_pct: float


FINAL_TABLE_STYLE = TableStylePreset(
    name="pevš-final-preview",
    font_family="Times New Roman",
    body_font_hp=24,          # 12 pt
    caption_font_hp=20,       # 10 pt
    table_header_font_hp=20,  # 10 pt bold
    table_body_font_hp=20,    # 10 pt
    note_font_hp=18,          # 9 pt
    caption_after=70,
    title_after=80,
    note_after=180,
    table_after=210,
    cell_pad_left=90,
    cell_pad_right=90,
    cell_pad_top=35,
    cell_pad_bottom=35,
    border_color="000000",
    border_thick_sz=10,
    border_mid_sz=8,
    border_thin_sz=4,
    default_table_width_pct=0.88,
)

