#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
import tempfile
import textwrap
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


REPLACEMENTS = {
    "<!-- FULL_RUN_FRAGMENT_VALIDATION -->": "fragment_validation.md",
    "<!-- FULL_RUN_FRAGMENT_DATASET -->": "fragment_dataset.md",
    "<!-- FULL_RUN_FRAGMENT_DESCRIPTIVES -->": "fragment_descriptives.md",
    "<!-- FULL_RUN_FRAGMENT_MEASUREMENT -->": "fragment_measurement.md",
    "<!-- FULL_RUN_FRAGMENT_MODELS -->": "fragment_models.md",
}

APPENDIX_REPLACEMENTS = {
    "<!-- FULL_RUN_APPENDIX_D_SECTION_1 -->": "appendix_d_section_1.md",
    "<!-- FULL_RUN_APPENDIX_D_SECTION_2 -->": "appendix_d_section_2.md",
    "<!-- FULL_RUN_APPENDIX_D_SECTION_3 -->": "appendix_d_section_3.md",
    "<!-- FULL_RUN_APPENDIX_D_SECTION_4 -->": "appendix_d_section_4.md",
}

SCENARIO_LABELS = {
    "Žena v strednom veku s caregiving záťažou": "Žena v strednom veku so záťažou pri starostlivosti o blízkeho",
}

DATASET_METRIC_LABELS = {
    "Počet seedov": "Počet východiskových scenárov",
    "Počet hodnotení v G0": "Počet hodnotení bez usmernenia (G0)",
    "Počet hodnotení v G1": "Počet hodnotení s usmernením (G1)",
    "Počet hodnotení pre P1": "Počet hodnotení pre profil P1",
    "Počet hodnotení pre P2": "Počet hodnotení pre profil P2",
    "Počet hodnotení pre P3": "Počet hodnotení pre profil P3",
    "G0 × P1": "Bez usmernenia × P1",
    "G0 × P2": "Bez usmernenia × P2",
    "G0 × P3": "Bez usmernenia × P3",
    "G1 × P1": "S usmernením × P1",
    "G1 × P2": "S usmernením × P2",
    "G1 × P3": "S usmernením × P3",
}

VARIABLE_LABELS = {
    "Klinická vierohodnosť rozhovoru": "Klinická vierohodnosť rozhovoru",
    "Prirodzenosť jazyka a štýlu odpovedí": "Prirodzenosť jazyka a štýlu odpovedí",
    "Vnútorná konzistentnosť rozhovoru": "Vnútorná konzistentnosť rozhovoru",
    "Súlad rozhovoru s obrazom depresívnej symptomatiky": "Súlad rozhovoru s obrazom depresívnej symptomatiky",
    "Použiteľnosť rozhovoru na tréningové / výučbové účely": "Použiteľnosť rozhovoru na tréningové a výučbové účely",
    "Istota odhadu pôvodu": "Istota odhadu pôvodu rozhovoru",
    "Prítomnosť vnútorných kontradikcií v rozhovore": "Prítomnosť vnútorných kontradikcií v rozhovore",
    "Klišé alebo šablónovité odpovede": "Klišé alebo šablónovité odpovede",
    "Nesúlad medzi kontextom a symptomatikou": "Nesúlad medzi kontextom a symptomatikou",
    "Podozrenie na inú primárnu psychopatológiu": "Podozrenie na inú primárnu psychopatológiu",
    "Neprimeraná dramatizácia alebo neprirodzená expresivita": "Neprimeraná dramatizácia alebo neprirodzená expresivita",
    "Ľudský odhad celkovej závažnosti depresívnej symptomatiky": "Odhad závažnosti depresívnej symptomatiky",
    "Ľudský odhad funkčného dopadu na bežné fungovanie": "Odhad funkčného dopadu na bežné fungovanie",
    "PHQ-9 symptomatické metadata: depresívna nálada": "A1 Depresívna nálada",
    "PHQ-9 symptomatické metadata: strata záujmu / anhedónia": "A2 Strata záujmu a anhedónia",
    "PHQ-9 symptomatické metadata: poruchy spánku": "A3 Poruchy spánku",
    "PHQ-9 symptomatické metadata: zmeny apetítu / hmotnosti": "A4 Zmeny apetítu a hmotnosti",
    "PHQ-9 symptomatické metadata: psychomotorické spomalenie alebo nepokoj": "A5 Psychomotorické spomalenie alebo nepokoj",
    "PHQ-9 symptomatické metadata: únava / nízka energia": "A6 Únava a nízka energia",
    "PHQ-9 symptomatické metadata: pocity viny / bezcennosti": "A7 Pocity viny a bezcennosti",
    "PHQ-9 symptomatické metadata: zhoršená koncentrácia / rozhodovanie": "A8 Zhoršená koncentrácia a rozhodovanie",
    "PHQ-9 symptomatické metadata: pasívne myšlienky na smrť": "A9 Pasívne myšlienky na smrť",
    "Kompozit defektov": "Index defektov",
    "Kompozit klinickej vierohodnosti": "Index klinickej vierohodnosti",
    "Absolútna chyba S2 voči seedu": "Absolútna chyba odhadu funkčného dopadu (S2)",
    "Absolútna chyba S1 voči seedu": "Absolútna chyba odhadu závažnosti (S1)",
    "Priemerná absolútna chyba v symptomatických doménach A1-A9 voči seedu": "Priemerná absolútna chyba v doménach A1-A9",
}

SECTION_LABELS = {
    "Položky": "Položky",
    "Kompozity": "Kompozity",
}

ANALYSIS_UNIT_LABELS = {
    "hodnotenie": "hodnotenie",
    "prepis rozhovoru": "prepis rozhovoru",
    "transkript": "prepis rozhovoru",
}

MODEL_LABELS = {
    "LMM": "LMM",
    "LMM (úroveň prepisu rozhovoru)": "LMM (úroveň prepisu rozhovoru)",
    "CLMM": "CLMM",
    "LMM sensitivity s random interceptom pre prepis rozhovoru": "LMM (kontrolný model pre prepis rozhovoru)",
}

EFFECT_LABELS = {
    "Intercept (referenčná kombinácia G0 × P1)": "Intercept (ref. bez usmernenia × P1)",
    "Hlavný efekt klinického usmernenia G1 (vs. G0)": "Usmernenie (áno vs. nie)",
    "Hlavný efekt P2 (vs. P1)": "Profil P2 (vs. P1)",
    "Hlavný efekt P3 (vs. P1)": "Profil P3 (vs. P1)",
    "Interakcia klinického usmernenia G1 × P2": "Interakcia: usmernenie × P2",
    "Interakcia klinického usmernenia G1 × P3": "Interakcia: usmernenie × P3",
}

ITEM_CODE_LABELS = {
    "Klinická vierohodnosť rozhovoru": "G1",
    "Prirodzenosť jazyka a štýlu odpovedí": "G2",
    "Vnútorná konzistentnosť rozhovoru": "G3",
    "Súlad rozhovoru s obrazom depresívnej symptomatiky": "G4",
    "Použiteľnosť rozhovoru na tréningové / výučbové účely": "G5",
    "Ľudský odhad celkovej závažnosti depresívnej symptomatiky": "S1",
    "Ľudský odhad funkčného dopadu na bežné fungovanie": "S2",
    "Prítomnosť vnútorných kontradikcií v rozhovore": "R1",
    "Klišé alebo šablónovité odpovede": "R2",
    "Nesúlad medzi kontextom a symptomatikou": "R3",
    "Podozrenie na inú primárnu psychopatológiu": "R4",
    "Neprimeraná dramatizácia alebo neprirodzená expresivita": "R5",
}

CORE_DESCRIPTIVE_VARIABLES = [
    "Kompozit klinickej vierohodnosti",
    "Prirodzenosť jazyka a štýlu odpovedí",
    "Použiteľnosť rozhovoru na tréningové / výučbové účely",
    "Kompozit defektov",
    "Priemerná absolútna chyba v symptomatických doménach A1-A9 voči seedu",
    "Absolútna chyba S1 voči seedu",
    "Absolútna chyba S2 voči seedu",
]

CORE_DESCRIPTIVE_ROW_LABELS = {
    "Kompozit klinickej vierohodnosti": "Index klinickej vierohodnosti",
    "Prirodzenosť jazyka a štýlu odpovedí": "G2 Prirodzenosť jazyka",
    "Použiteľnosť rozhovoru na tréningové / výučbové účely": "G5 Tréningová použiteľnosť",
    "Kompozit defektov": "Index defektov",
    "Priemerná absolútna chyba v symptomatických doménach A1-A9 voči seedu": "Priemerná absolútna chyba A1-A9",
    "Absolútna chyba S1 voči seedu": "Chyba odhadu závažnosti S1",
    "Absolútna chyba S2 voči seedu": "Chyba odhadu funkčného dopadu S2",
}

VALIDATION_ITEM_SHORT_LABELS = {
    "G1": "Klinická vierohodnosť",
    "G2": "Prirodzenosť jazyka",
    "G3": "Vnútorná konzistentnosť",
    "G4": "Zhoda s depresiou",
    "G5": "Tréningová použiteľnosť",
    "S1": "Odhad závažnosti",
    "S2": "Odhad funkčného dopadu",
    "R1": "Vnútorné kontradikcie",
    "R2": "Klišé a šablónovitosť",
    "R3": "Kontextový nesúlad",
    "R4": "Iná psychopatológia",
    "R5": "Neprimeraná dramatizácia",
}

VALIDATION_ITEM_ORDER = {
    "G1": 1,
    "G2": 2,
    "G3": 3,
    "G4": 4,
    "G5": 5,
    "S1": 6,
    "S2": 7,
    "R1": 8,
    "R2": 9,
    "R3": 10,
    "R4": 11,
    "R5": 12,
}

VALIDATION_SEED_SHORT_LABELS = {
    "1": "Pracovno-študijné preťaženie",
    "2": "Smenná práca a záťaž",
    "3": "Záťaž pri starostlivosti",
    "4": "Vysoká pracovná záťaž",
    "5": "Rozvod a finančný tlak",
    "6": "Dlhodobá pracovná záťaž",
    "7": "Vdovstvo a strata rytmu",
    "8": "Strata dennej rutiny",
    "9": "Výkonový tlak a ruminácie",
    "10": "Stagnácia s pasívnym A9",
    "11": "Nízky príjem a stiahnutie",
    "12": "Vysoká zodpovednosť a utlmenie",
}


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def decimal_or_none(value: str | None) -> Decimal | None:
    if value is None:
        return None
    normalized = value.strip()
    if not normalized or normalized.upper() == "NA":
        return None
    normalized = normalized.replace(",", ".")
    try:
        return Decimal(normalized)
    except InvalidOperation:
        return None


def format_decimal(
    value: str | Decimal | None,
    *,
    digits: int = 2,
    drop_leading_zero: bool = False,
    missing: str = "—",
) -> str:
    decimal_value = decimal_or_none(str(value) if isinstance(value, Decimal) else value)
    if decimal_value is None:
        return missing

    quantum = Decimal("1") if digits == 0 else Decimal("1").scaleb(-digits)
    rounded = decimal_value.quantize(quantum, rounding=ROUND_HALF_UP)
    text = f"{rounded:.0f}" if digits == 0 else f"{rounded:.{digits}f}"
    text = text.replace(".", ",")

    if drop_leading_zero and text.startswith("0,"):
        text = text[1:]
    elif drop_leading_zero and text.startswith("-0,"):
        text = "-" + text[2:]

    return text


def format_integer_or_decimal(value: str | None, *, digits: int = 2) -> str:
    decimal_value = decimal_or_none(value)
    if decimal_value is None:
        return value.strip() if isinstance(value, str) and value.strip() else "—"
    if decimal_value == decimal_value.to_integral_value():
        return format_decimal(value, digits=0)
    return format_decimal(value, digits=digits)


def format_percent(value: str | None, *, digits: int = 1, from_proportion: bool = False) -> str:
    decimal_value = decimal_or_none(value)
    if decimal_value is None:
        return "—"
    if from_proportion:
        decimal_value *= Decimal("100")
    return format_decimal(decimal_value, digits=digits)


def format_p_value(value: str | None) -> str:
    decimal_value = decimal_or_none(value)
    if decimal_value is None:
        return "—"
    if decimal_value < Decimal("0.001"):
        return "< ,001"
    return format_decimal(value, digits=3, drop_leading_zero=True)


def format_interval(low: str | None, high: str | None, *, digits: int = 2) -> str:
    low_text = format_decimal(low, digits=digits)
    high_text = format_decimal(high, digits=digits)
    if low_text == "—" or high_text == "—":
        return "—"
    return f"[{low_text}; {high_text}]"


def localize_scenario_label(label: str) -> str:
    return SCENARIO_LABELS.get(label, label)


def localize_variable_label(label: str) -> str:
    return VARIABLE_LABELS.get(label, label)


def localize_dataset_metric(label: str) -> str:
    return DATASET_METRIC_LABELS.get(label, label)


def localize_section_label(label: str) -> str:
    return SECTION_LABELS.get(label, label)


def localize_analysis_unit_label(label: str) -> str:
    return ANALYSIS_UNIT_LABELS.get(label, label)


def localize_model_label(label: str) -> str:
    return MODEL_LABELS.get(label, label)


def localize_effect_label(label: str) -> str:
    return EFFECT_LABELS.get(label, label)


def escape_cell(value: str) -> str:
    return value.replace("|", "/").replace("\n", " ").strip()


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""

    header = rows[0]
    lines = [
        "| " + " | ".join(escape_cell(cell) for cell in header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]

    for row in rows[1:]:
        padded = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(escape_cell(cell) for cell in padded[: len(header)]) + " |")

    return "\n".join(lines)


def table_from_columns(columns: list[str], rows: list[dict[str, str]]) -> list[list[str]]:
    table_rows = [columns]
    for row in rows:
        table_rows.append([row.get(column, "") for column in columns])
    return table_rows


def collapse_repeated_values(table_rows: list[list[str]], repeat_columns: list[int]) -> list[list[str]]:
    if len(table_rows) <= 2:
        return table_rows

    collapsed = [table_rows[0]]
    previous: list[str] | None = None
    for row in table_rows[1:]:
        current = row.copy()
        if previous is not None:
            for column_index in repeat_columns:
                if current[column_index] == previous[column_index]:
                    current[column_index] = ""
        collapsed.append(current)
        previous = row
    return collapsed


def collapse_model_table_rows(table_rows: list[list[str]]) -> list[list[str]]:
    if len(table_rows) <= 2:
        return table_rows

    collapsed = [table_rows[0]]
    previous_outcome = ""
    previous_model = ""

    for row in table_rows[1:]:
        current = row.copy()
        current_outcome = current[0]
        current_model = current[1]

        if current_outcome == previous_outcome:
            current[0] = ""
            if current_model == previous_model:
                current[1] = ""

        collapsed.append(current)
        previous_outcome = row[0]
        previous_model = row[1]

    return collapsed


def caption(label: str, title: str) -> str:
    return f"**{label}**  \n*{title}*\n"


def table_block_from_rows(rows: list[list[str]], label: str, title: str, note: str | None = None) -> str:
    block = [caption(label, title), markdown_table(rows)]
    if note:
        block.extend(["", f"Poznámka. {note}"])
    return "\n".join(block).strip() + "\n"


def table_block(path: Path, label: str, title: str, note: str | None = None) -> str:
    return table_block_from_rows(transform_rows(path), label, title, note)


def figure_block(path: Path, label: str, title: str, note: str | None = None) -> str:
    block = [
        caption(label, title).rstrip(),
        "",
        f"![{label}]({path.resolve()})",
    ]
    if note:
        block.extend(["", f"Poznámka. {note}"])
    block.append("")
    return "\n".join(block)


def paragraph_block(text: str) -> str:
    return text.strip() + "\n"


def transform_table_s4(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        follow_up = row.get("Potrebný follow-up", "").strip().lower()
        transformed.append(
            {
                "Kód": row.get("Kód", ""),
                "Položka": row.get("Položka", ""),
                "Relevantnosť M": format_decimal(row.get("Relevantnosť M"), digits=2),
                "Zrozumiteľnosť M": format_decimal(row.get("Zrozumiteľnosť M"), digits=2),
                "Potrebnosť M": format_decimal(row.get("Potrebnosť M"), digits=2),
                "Celkový priemer M": format_decimal(row.get("Celkový priemer M"), digits=2),
                "Podpora 3-4 (%)": format_percent(row.get("Podpora 3-4 (%)"), digits=1),
                "Potrebná doplňujúca úprava": {"true": "áno", "false": "nie"}.get(follow_up, row.get("Potrebný follow-up", "")),
            }
        )

    columns = [
        "Kód",
        "Položka",
        "Relevantnosť M",
        "Zrozumiteľnosť M",
        "Potrebnosť M",
        "Celkový priemer M",
        "Podpora 3-4 (%)",
        "Potrebná doplňujúca úprava",
    ]
    return table_from_columns(columns, transformed)


def transform_table_s5(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        seed_id = row.get("Seed", "")
        transformed.append(
            {
                "Kód scenára": seed_id.zfill(2) if seed_id.isdigit() else seed_id,
                "Scenár": localize_scenario_label(row.get("Scenár", "")),
                "Celkový priemer M": format_decimal(row.get("Celkový priemer M"), digits=2),
                "Dostatok informácií M": format_decimal(row.get("Dostatok informácií M"), digits=2),
                "Nestereotypnosť M": format_decimal(row.get("Nestereotypnosť M"), digits=2),
                "Vhodnosť pre výskum M": format_decimal(row.get("Vhodnosť pre výskum M"), digits=2),
                "Cieľová závažnosť": row.get("Cieľová závažnosť", ""),
                "Modálna expertná závažnosť": row.get("Modálna expert. závažnosť", ""),
                "Zhoda so závažnosťou (%)": format_percent(row.get("Zhoda so závažnosťou (%)"), digits=1),
            }
        )

    columns = [
        "Kód scenára",
        "Scenár",
        "Celkový priemer M",
        "Dostatok informácií M",
        "Nestereotypnosť M",
        "Vhodnosť pre výskum M",
        "Cieľová závažnosť",
        "Modálna expertná závažnosť",
        "Zhoda so závažnosťou (%)",
    ]
    return table_from_columns(columns, transformed)


def transform_table_1(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        metric = row.get("metric", "")
        value = row.get("value", "")
        if metric == "Priemerný počet hodnotení na prepis rozhovoru":
            value = format_decimal(value, digits=2)
        else:
            value = format_integer_or_decimal(value, digits=2)
        transformed.append({"Ukazovateľ": localize_dataset_metric(metric), "Hodnota": value})
    return table_from_columns(["Ukazovateľ", "Hodnota"], transformed)


def transform_table_2(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        transformed.append(
            {
                "Premenná": localize_variable_label(row.get("variable", "")),
                "Blok": localize_section_label(row.get("section", "")),
                "Úroveň analýzy": localize_analysis_unit_label(row.get("analysis_unit", "")),
                "n": format_decimal(row.get("n_non_missing"), digits=0),
                "Počet kategórií": format_decimal(row.get("levels_used"), digits=0),
                "M": format_decimal(row.get("mean"), digits=2),
                "SD": format_decimal(row.get("sd"), digits=2),
                "Me": format_decimal(row.get("median"), digits=2),
                "IQR": format_decimal(row.get("iqr"), digits=2),
                "Min": format_decimal(row.get("min"), digits=2),
                "Max": format_decimal(row.get("max"), digits=2),
            }
        )

    columns = [
        "Premenná",
        "Blok",
        "Úroveň analýzy",
        "n",
        "Počet kategórií",
        "M",
        "SD",
        "Me",
        "IQR",
        "Min",
        "Max",
    ]
    return table_from_columns(columns, transformed)


def transform_table_3(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        transformed.append(
            {
                "Premenná": localize_variable_label(row.get("variable", "")),
                "Odpoveď": row.get("response", ""),
                "n": format_decimal(row.get("n"), digits=0),
                "Podiel (%)": format_percent(row.get("prop"), digits=1, from_proportion=True),
            }
        )
    return collapse_repeated_values(
        table_from_columns(["Premenná", "Odpoveď", "n", "Podiel (%)"], transformed),
        [0],
    )


def transform_table_4(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        transformed.append(
            {
                "Blok": row.get("block", ""),
                "Počet položiek": format_decimal(row.get("n_items"), digits=0),
                "n": format_decimal(row.get("n_rows"), digits=0),
                "α": format_decimal(row.get("alpha"), digits=2),
                "ω": format_decimal(row.get("omega"), digits=2),
            }
        )
    return table_from_columns(["Blok", "Počet položiek", "n", "α", "ω"], transformed)


def transform_model_table(rows: list[dict[str, str]], *, statistic_header: str = "t / z") -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        transformed.append(
            {
                "Ukazovateľ": localize_variable_label(row.get("outcome", "")),
                "Model": localize_model_label(row.get("model_type", row.get("model_family", ""))),
                "Efekt": localize_effect_label(row.get("term", "")),
                "b": format_decimal(row.get("estimate"), digits=2),
                "SE": format_decimal(row.get("std_error"), digits=2),
                statistic_header: format_decimal(row.get("statistic"), digits=2),
                "p": format_p_value(row.get("p_value")),
                "95 % IS": format_interval(row.get("conf_low"), row.get("conf_high"), digits=2),
            }
        )
    columns = ["Ukazovateľ", "Model", "Efekt", "b", "SE", statistic_header, "p", "95 % IS"]
    return collapse_model_table_rows(table_from_columns(columns, transformed))


def transform_rows(path: Path) -> list[list[str]]:
    rows = read_csv_rows(path)
    if not rows:
        return []

    transforms = {
        "table_s4_expert_review_items.csv": transform_table_s4,
        "table_s5_expert_review_seeds.csv": transform_table_s5,
        "table_1_dataset_summary.csv": transform_table_1,
        "table_2_descriptives.csv": transform_table_2,
        "table_3_item_frequencies.csv": transform_table_3,
        "table_4_internal_consistency.csv": transform_table_4,
        "table_6_mixed_models_core.csv": transform_model_table,
        "table_s6_lmm_sensitivity_transcript_id.csv": lambda rows: transform_model_table(rows, statistic_header="t"),
    }

    transform = transforms.get(path.name)
    if transform is None:
        header = list(rows[0].keys())
        plain_rows = [header]
        plain_rows.extend([[row.get(column, "") for column in header] for row in rows])
        return plain_rows
    return transform(rows)


def dataset_metrics(rows: list[dict[str, str]]) -> dict[str, str]:
    return {row.get("metric", ""): row.get("value", "") for row in rows}


def build_dataset_overview_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    metrics = dataset_metrics(rows)
    ordered_metrics = [
        "Počet hodnotiteľov",
        "Počet prepisov rozhovorov",
        "Počet seedov",
        "Počet hodnotení",
        "Priemerný počet hodnotení na prepis rozhovoru",
        "Minimálny počet hodnotení na prepis rozhovoru",
        "Maximálny počet hodnotení na prepis rozhovoru",
    ]

    transformed: list[dict[str, str]] = []
    for metric in ordered_metrics:
        value = metrics.get(metric, "")
        if metric == "Priemerný počet hodnotení na prepis rozhovoru":
            value = format_decimal(value, digits=2)
        else:
            value = format_integer_or_decimal(value, digits=2)
        transformed.append(
            {
                "Ukazovateľ": localize_dataset_metric(metric),
                "Hodnota": value,
            }
        )
    return table_from_columns(["Ukazovateľ", "Hodnota"], transformed)


def build_dataset_cell_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    metrics = dataset_metrics(rows)
    g0_p1 = format_decimal(metrics.get("G0 × P1"), digits=0)
    g0_p2 = format_decimal(metrics.get("G0 × P2"), digits=0)
    g0_p3 = format_decimal(metrics.get("G0 × P3"), digits=0)
    g1_p1 = format_decimal(metrics.get("G1 × P1"), digits=0)
    g1_p2 = format_decimal(metrics.get("G1 × P2"), digits=0)
    g1_p3 = format_decimal(metrics.get("G1 × P3"), digits=0)

    transformed = [
        {
            "Podmienka": "Bez usmernenia (G0)",
            "P1": g0_p1,
            "P2": g0_p2,
            "P3": g0_p3,
            "Spolu": format_decimal(metrics.get("Počet hodnotení v G0"), digits=0),
        },
        {
            "Podmienka": "S usmernením (G1)",
            "P1": g1_p1,
            "P2": g1_p2,
            "P3": g1_p3,
            "Spolu": format_decimal(metrics.get("Počet hodnotení v G1"), digits=0),
        },
        {
            "Podmienka": "Spolu",
            "P1": format_decimal(metrics.get("Počet hodnotení pre P1"), digits=0),
            "P2": format_decimal(metrics.get("Počet hodnotení pre P2"), digits=0),
            "P3": format_decimal(metrics.get("Počet hodnotení pre P3"), digits=0),
            "Spolu": format_decimal(metrics.get("Počet hodnotení"), digits=0),
        },
    ]
    return table_from_columns(["Podmienka", "P1", "P2", "P3", "Spolu"], transformed)


def build_compact_descriptives_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    rows_by_variable = {row.get("variable", ""): row for row in rows}
    transformed: list[dict[str, str]] = []
    for variable in CORE_DESCRIPTIVE_VARIABLES:
        row = rows_by_variable.get(variable)
        if row is None:
            raise KeyError(f"Missing descriptive row for '{variable}'.")
        transformed.append(
            {
                "Premenná": CORE_DESCRIPTIVE_ROW_LABELS[variable],
                "Úroveň analýzy": localize_analysis_unit_label(row.get("analysis_unit", "")),
                "n": format_decimal(row.get("n_non_missing"), digits=0),
                "M": format_decimal(row.get("mean"), digits=2),
                "SD": format_decimal(row.get("sd"), digits=2),
                "Me": format_decimal(row.get("median"), digits=2),
                "IQR": format_decimal(row.get("iqr"), digits=2),
                "Min": format_decimal(row.get("min"), digits=2),
                "Max": format_decimal(row.get("max"), digits=2),
            }
        )
    return table_from_columns(
        ["Premenná", "Úroveň analýzy", "n", "M", "SD", "Me", "IQR", "Min", "Max"],
        transformed,
    )


def find_model_row(rows: list[dict[str, str]], outcome: str, term: str) -> dict[str, str]:
    for row in rows:
        if row.get("outcome") == outcome and row.get("term") == term:
            return row
    raise KeyError(f"Missing model row for outcome='{outcome}', term='{term}'.")


def build_hypothesis_summary_rows(
    lmm_rows: list[dict[str, str]],
    clmm_rows: list[dict[str, str]],
) -> list[list[str]]:
    h1 = find_model_row(lmm_rows, "Kompozit klinickej vierohodnosti", "Hlavný efekt klinického usmernenia G1 (vs. G0)")
    h3 = find_model_row(lmm_rows, "Kompozit defektov", "Hlavný efekt klinického usmernenia G1 (vs. G0)")
    h4 = find_model_row(
        lmm_rows,
        "Priemerná absolútna chyba v symptomatických doménach A1-A9 voči seedu",
        "Hlavný efekt klinického usmernenia G1 (vs. G0)",
    )
    h2 = find_model_row(clmm_rows, "Prirodzenosť jazyka a štýlu odpovedí", "Hlavný efekt klinického usmernenia G1 (vs. G0)")
    h5 = find_model_row(clmm_rows, "Použiteľnosť rozhovoru na tréningové / výučbové účely", "Hlavný efekt klinického usmernenia G1 (vs. G0)")
    s2_p2 = find_model_row(clmm_rows, "Ľudský odhad funkčného dopadu na bežné fungovanie", "Hlavný efekt P2 (vs. P1)")
    s2_p3 = find_model_row(clmm_rows, "Ľudský odhad funkčného dopadu na bežné fungovanie", "Hlavný efekt P3 (vs. P1)")
    s1_int = find_model_row(clmm_rows, "Ľudský odhad celkovej závažnosti depresívnej symptomatiky", "Interakcia klinického usmernenia G1 × P3")
    s2_int = find_model_row(clmm_rows, "Ľudský odhad funkčného dopadu na bežné fungovanie", "Interakcia klinického usmernenia G1 × P3")

    rows = [
        {
            "Blok": "Globálna kvalita",
            "Hypotéza / VO": "H1",
            "Hlavný ukazovateľ": "Index klinickej vierohodnosti",
            "Výsledok": f"efekt usmernenia veľmi malý, p = {format_p_value(h1.get('p_value'))}",
            "Záver": "nepodporené",
        },
        {
            "Blok": "Prirodzenosť",
            "Hypotéza / VO": "H2",
            "Hlavný ukazovateľ": "G2",
            "Výsledok": f"koeficient usmernenia prakticky nulový, p = {format_p_value(h2.get('p_value'))}",
            "Záver": "nepodporené",
        },
        {
            "Blok": "Defekty",
            "Hypotéza / VO": "H3",
            "Hlavný ukazovateľ": "Index defektov",
            "Výsledok": f"priaznivý smer, ale neistý, p = {format_p_value(h3.get('p_value'))}",
            "Záver": "nepodporené / iba náznak",
        },
        {
            "Blok": "Symptómová zhoda",
            "Hypotéza / VO": "H4",
            "Hlavný ukazovateľ": "Priemerná absolútna chyba A1-A9",
            "Výsledok": f"bez jasného efektu, p = {format_p_value(h4.get('p_value'))}",
            "Záver": "nepodporené",
        },
        {
            "Blok": "Použiteľnosť",
            "Hypotéza / VO": "H5",
            "Hlavný ukazovateľ": "G5",
            "Výsledok": f"pozitívny smer, ale bez robustného efektu, p = {format_p_value(h5.get('p_value'))}",
            "Záver": "nepodporené",
        },
        {
            "Blok": "Profil odpovedania",
            "Hypotéza / VO": "H6–H8",
            "Hlavný ukazovateľ": "P1/P2/P3",
            "Výsledok": (
                "jadrové profile efekty bez stabilnej podpory; "
                f"v S2 len doplnkový signál (P2: p = {format_p_value(s2_p2.get('p_value'))}; "
                f"P3: p = {format_p_value(s2_p3.get('p_value'))})"
            ),
            "Záver": "nepodporené",
        },
        {
            "Blok": "Interakcia",
            "Hypotéza / VO": "H9",
            "Hlavný ukazovateľ": "G × P",
            "Výsledok": (
                "jadrové ukazovatele bez robustnej podpory; "
                f"sekundárne S1/S2 iba opatrný signál (S1: p = {format_p_value(s1_int.get('p_value'))}; "
                f"S2: p = {format_p_value(s2_int.get('p_value'))})"
            ),
            "Záver": "nepodporené ako hlavný záver",
        },
    ]
    return table_from_columns(
        ["Blok", "Hypotéza / VO", "Hlavný ukazovateľ", "Výsledok", "Záver"],
        rows,
    )


def build_validation_item_rows(
    rows: list[dict[str, str]],
    *,
    include_prefixes: tuple[str, ...],
) -> list[list[str]]:
    filtered: list[dict[str, str]] = []
    for row in rows:
        code = row.get("Kód", "")
        if not code.startswith(include_prefixes):
            continue
        filtered.append(
            {
                "Kód": code,
                "Položka": row.get("Položka", ""),
                "Relevantnosť M": format_decimal(row.get("Relevantnosť M"), digits=2),
                "Zrozumiteľnosť M": format_decimal(row.get("Zrozumiteľnosť M"), digits=2),
                "Potrebnosť M": format_decimal(row.get("Potrebnosť M"), digits=2),
                "Celkový priemer M": format_decimal(row.get("Celkový priemer M"), digits=2),
                "Podpora 3-4 (%)": format_decimal(row.get("Podpora 3-4 (%)"), digits=1),
                "Potrebná doplňujúca úprava": "áno" if row.get("Potrebný follow-up", "").lower() == "true" else "nie",
            }
        )

    return table_from_columns(
        [
            "Kód",
            "Položka",
            "Relevantnosť M",
            "Zrozumiteľnosť M",
            "Potrebnosť M",
            "Celkový priemer M",
            "Podpora 3-4 (%)",
            "Potrebná doplňujúca úprava",
        ],
        filtered,
    )


def build_validation_heatmap_item_rows(
    rows: list[dict[str, str]],
    *,
    include_prefixes: tuple[str, ...],
) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in sorted(rows, key=lambda item: VALIDATION_ITEM_ORDER.get(item.get("Kód", ""), 99)):
        code = row.get("Kód", "")
        if not code.startswith(include_prefixes):
            continue
        transformed.append(
            {
                "Položka": f"{code} — {VALIDATION_ITEM_SHORT_LABELS.get(code, row.get('Položka', ''))}",
                "Relevantnosť": format_decimal(row.get("Relevantnosť M"), digits=2),
                "Zrozumiteľnosť": format_decimal(row.get("Zrozumiteľnosť M"), digits=2),
                "Potrebnosť": format_decimal(row.get("Potrebnosť M"), digits=2),
                "Celkovo": format_decimal(row.get("Celkový priemer M"), digits=2),
            }
        )

    return table_from_columns(
        ["Položka", "Relevantnosť", "Zrozumiteľnosť", "Potrebnosť", "Celkovo"],
        transformed,
    )


def build_seed_quality_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        seed = row.get("Seed", "")
        code = seed.zfill(2) if seed.isdigit() else seed
        transformed.append(
            {
                "Kód scenára": code,
                "Scenár": localize_scenario_label(row.get("Scenár", "")),
                "Celkový priemer M": format_decimal(row.get("Celkový priemer M"), digits=2),
                "Dostatok informácií M": format_decimal(row.get("Dostatok informácií M"), digits=2),
                "Nestereotypnosť M": format_decimal(row.get("Nestereotypnosť M"), digits=2),
                "Vhodnosť pre výskum M": format_decimal(row.get("Vhodnosť pre výskum M"), digits=2),
            }
        )

    return table_from_columns(
        [
            "Kód scenára",
            "Scenár",
            "Celkový priemer M",
            "Dostatok informácií M",
            "Nestereotypnosť M",
            "Vhodnosť pre výskum M",
        ],
        transformed,
    )


def build_seed_heatmap_rows(
    rows: list[dict[str, str]],
    *,
    columns: list[tuple[str, str]],
    id_column: str = "Seed",
    label_column: str = "Scenár",
) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    ordered_rows = sorted(
        rows,
        key=lambda item: (
            decimal_or_none(item.get(id_column)) if item.get(id_column) else Decimal("999"),
        ),
    )
    for row in ordered_rows:
        seed = row.get(id_column, "")
        transformed_row = {
            "Scenár": f"S{seed.zfill(2) if seed.isdigit() else seed} — {VALIDATION_SEED_SHORT_LABELS.get(seed, row.get(label_column, ''))}"
        }
        for header, source_column in columns:
            transformed_row[header] = format_decimal(row.get(source_column), digits=2)
        transformed.append(transformed_row)

    return table_from_columns(["Scenár"] + [header for header, _ in columns], transformed)


def build_seed_severity_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in rows:
        seed = row.get("Seed", "")
        code = seed.zfill(2) if seed.isdigit() else seed
        transformed.append(
            {
                "Kód scenára": code,
                "Scenár": localize_scenario_label(row.get("Scenár", "")),
                "Cieľová závažnosť": row.get("Cieľová závažnosť", ""),
                "Modálna expertná závažnosť": row.get("Modálna expert. závažnosť", ""),
                "Zhoda so závažnosťou (%)": format_decimal(row.get("Zhoda so závažnosťou (%)"), digits=1),
            }
        )

    return table_from_columns(
        [
            "Kód scenára",
            "Scenár",
            "Cieľová závažnosť",
            "Modálna expertná závažnosť",
            "Zhoda so závažnosťou (%)",
        ],
        transformed,
    )


def build_spearman_matrix_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    variable_order = [
        "Kompozit klinickej vierohodnosti",
        "Kompozit defektov",
        "Priemerná absolútna chyba v symptomatických doménach A1-A9 voči seedu",
        "Prirodzenosť jazyka a štýlu odpovedí",
        "Použiteľnosť rozhovoru na tréningové / výučbové účely",
    ]
    variable_labels = {
        "Kompozit klinickej vierohodnosti": "Index klinickej vierohodnosti",
        "Kompozit defektov": "Index defektov",
        "Priemerná absolútna chyba v symptomatických doménach A1-A9 voči seedu": "Priemerná absolútna chyba A1-A9",
        "Prirodzenosť jazyka a štýlu odpovedí": "Prirodzenosť jazyka",
        "Použiteľnosť rozhovoru na tréningové / výučbové účely": "Tréningová použiteľnosť",
    }

    rho_lookup: dict[tuple[str, str], str] = {}
    for row in rows:
        if row.get("status") != "ok":
            continue
        variable_1 = row.get("variable_1", "")
        variable_2 = row.get("variable_2", "")
        rho_lookup[(variable_1, variable_2)] = format_decimal(row.get("rho"), digits=2)

    table_rows = [["Ukazovateľ"] + [variable_labels[variable] for variable in variable_order]]
    for variable_row in variable_order:
        matrix_row = [variable_labels[variable_row]]
        for variable_column in variable_order:
            value = rho_lookup.get((variable_row, variable_column))
            if value is None:
                value = rho_lookup.get((variable_column, variable_row), "—")
            matrix_row.append(value)
        table_rows.append(matrix_row)

    return table_rows


def build_pam_profile_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    transformed: list[dict[str, str]] = []
    for row in sorted(rows, key=lambda item: item.get("cluster", "")):
        transformed.append(
            {
                "Klaster": row.get("cluster", ""),
                "n prepisov rozhovorov": format_decimal(row.get("n_transcripts"), digits=0),
                "Index klinickej vierohodnosti (št.)": format_decimal(row.get("plausibility_index"), digits=2),
                "Index defektov (št.)": format_decimal(row.get("defect_index"), digits=2),
                "Priemerná absolútna chyba A1-A9 (št.)": format_decimal(row.get("symptom_error_mean"), digits=2),
                "G2 (št.)": format_decimal(row.get("g2"), digits=2),
                "G5 (št.)": format_decimal(row.get("g5"), digits=2),
                "S1 chyba (št.)": format_decimal(row.get("severity_error"), digits=2),
                "S2 chyba (št.)": format_decimal(row.get("impact_error"), digits=2),
            }
        )

    columns = [
        "Klaster",
        "n prepisov rozhovorov",
        "Index klinickej vierohodnosti (št.)",
        "Index defektov (št.)",
        "Priemerná absolútna chyba A1-A9 (št.)",
        "G2 (št.)",
        "G5 (št.)",
        "S1 chyba (št.)",
        "S2 chyba (št.)",
    ]
    return table_from_columns(columns, transformed)


def build_pam_condition_rows(rows: list[dict[str, str]]) -> list[list[str]]:
    grouping_order = {
        "Klinické usmernenie": 0,
        "Profil": 1,
        "Klinické usmernenie × profil": 2,
    }

    transformed: list[dict[str, str]] = []
    for row in sorted(
        rows,
        key=lambda item: (
            item.get("cluster", ""),
            grouping_order.get(item.get("grouping", ""), 99),
            item.get("guardrail", ""),
            item.get("profile", ""),
        ),
    ):
        grouping = row.get("grouping", "")
        if grouping == "Klinické usmernenie":
            condition = row.get("guardrail", "")
        elif grouping == "Profil":
            condition = row.get("profile", "")
        else:
            guardrail = row.get("guardrail", "")
            profile = row.get("profile", "")
            condition = f"{guardrail} × {profile}".strip()

        transformed.append(
            {
                "Klaster": row.get("cluster", ""),
                "Zoskupenie": grouping,
                "Podmienka": condition,
                "n prepisov rozhovorov": format_decimal(row.get("n"), digits=0),
            }
        )

    columns = ["Klaster", "Zoskupenie", "Podmienka", "n prepisov rozhovorov"]
    return collapse_repeated_values(table_from_columns(columns, transformed), [0, 1])


def run_r_script(code: str, *, workdir: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".R", encoding="utf-8", delete=False) as handle:
        handle.write(code)
        script_path = Path(handle.name)

    try:
        completed = subprocess.run(
            ["Rscript", str(script_path)],
            cwd=workdir,
            capture_output=True,
            text=True,
            check=False,
        )
    finally:
        script_path.unlink(missing_ok=True)

    if completed.returncode != 0:
        raise RuntimeError(
            "Rscript failed while generating results assets.\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        )


def refresh_expert_review_outputs(repo_root: Path) -> None:
    script_path = repo_root / "analysis" / "scripts" / "build_expert_review_outputs.py"
    bundled_python = Path.home() / ".cache" / "codex-runtimes" / "codex-primary-runtime" / "dependencies" / "python" / "bin" / "python3"
    candidate_commands: list[list[str]] = []

    if os.environ.get("CODEX_WORKSPACE_PYTHON"):
        candidate_commands.append([os.environ["CODEX_WORKSPACE_PYTHON"]])
    if bundled_python.exists():
        candidate_commands.append([str(bundled_python)])
    if (repo_root / ".venv" / "bin" / "python").exists():
        candidate_commands.append([str(repo_root / ".venv" / "bin" / "python")])
    candidate_commands.append([sys.executable])
    candidate_commands.append(["python3"])

    selected_python: list[str] | None = None
    for candidate in candidate_commands:
        probe = subprocess.run(
            candidate + ["-c", "import pandas, openpyxl, PIL"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if probe.returncode == 0:
            selected_python = candidate
            break

    if selected_python is None:
        raise RuntimeError(
            "Expert review output refresh could not find a Python interpreter with pandas, openpyxl and Pillow."
        )

    completed = subprocess.run(
        selected_python + [str(script_path)],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "Expert review output refresh failed.\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        )


def generate_results_figures(
    repo_root: Path,
    *,
    frequency_global_path: Path,
    frequency_warning_path: Path,
    symptom_error_path: Path,
) -> None:
    tables_dir = repo_root / "tables"
    outputs_dir = repo_root / "analysis" / "outputs"

    r_code = textwrap.dedent(
        f"""
        suppressPackageStartupMessages({{
          library(ggplot2)
          library(readr)
          library(dplyr)
        }})

        freq_path <- {str(tables_dir / "table_3_item_frequencies.csv")!r}
        transcript_path <- {str(outputs_dir / "transcript_level_summary_report.csv")!r}
        global_out <- {str(frequency_global_path)!r}
        warning_out <- {str(frequency_warning_path)!r}
        symptom_out <- {str(symptom_error_path)!r}

        freq <- readr::read_csv(freq_path, show_col_types = FALSE) |>
          mutate(
            item = recode(
              variable,
              "Klinická vierohodnosť rozhovoru" = "G1",
              "Prirodzenosť jazyka a štýlu odpovedí" = "G2",
              "Vnútorná konzistentnosť rozhovoru" = "G3",
              "Súlad rozhovoru s obrazom depresívnej symptomatiky" = "G4",
              "Použiteľnosť rozhovoru na tréningové / výučbové účely" = "G5",
              "Ľudský odhad celkovej závažnosti depresívnej symptomatiky" = "S1",
              "Ľudský odhad funkčného dopadu na bežné fungovanie" = "S2",
              "Prítomnosť vnútorných kontradikcií v rozhovore" = "R1",
              "Klišé alebo šablónovité odpovede" = "R2",
              "Nesúlad medzi kontextom a symptomatikou" = "R3",
              "Podozrenie na inú primárnu psychopatológiu" = "R4",
              "Neprimeraná dramatizácia alebo neprirodzená expresivita" = "R5"
            ),
            prop = as.numeric(prop),
            response = factor(response, levels = c("1", "2", "3", "4", "5"))
          )

        likert_colors <- c(
          "1" = "#DCE7F2",
          "2" = "#B4CBDD",
          "3" = "#86ABC3",
          "4" = "#4B8F8C",
          "5" = "#1D5C63"
        )

        make_likert_plot <- function(data, item_order, title_text) {{
          ggplot(
            data |> mutate(item = factor(item, levels = rev(item_order))),
            aes(x = prop, y = item, fill = response)
          ) +
            geom_col(
              width = 0.72,
              color = "white",
              linewidth = 0.35,
              position = position_stack(reverse = TRUE)
            ) +
            scale_fill_manual(values = likert_colors, name = "Odpoveď") +
            scale_x_continuous(
              labels = function(x) paste0(round(x * 100), " %"),
              expand = expansion(mult = c(0, 0.02))
            ) +
            labs(
              title = title_text,
              x = "Podiel hodnotení",
              y = NULL
            ) +
            theme_minimal(base_size = 12) +
            theme(
              panel.grid.minor = element_blank(),
              panel.grid.major.y = element_blank(),
              legend.position = "right",
              plot.title = element_text(face = "bold")
            )
        }}

        global_items <- c("G1", "G2", "G3", "G4", "G5", "S1", "S2")
        warning_items <- c("R1", "R2", "R3", "R4", "R5")

        ggsave(
          filename = global_out,
          plot = make_likert_plot(
            freq |> filter(item %in% global_items),
            global_items,
            "Rozdelenie globálnych hodnotení G1–G5 a S1–S2"
          ),
          width = 9.2,
          height = 5.8,
          dpi = 300,
          bg = "white"
        )

        ggsave(
          filename = warning_out,
          plot = make_likert_plot(
            freq |> filter(item %in% warning_items),
            warning_items,
            "Rozdelenie varovných signálov R1–R5"
          ),
          width = 8.6,
          height = 5.0,
          dpi = 300,
          bg = "white"
        )

        transcript <- readr::read_csv(transcript_path, show_col_types = FALSE) |>
          mutate(
            guardrail = factor(guardrail, levels = c("G0", "G1")),
            profile = factor(profile, levels = c("P1", "P2", "P3")),
            symptom_error_mean = as.numeric(symptom_error_mean)
          )

        symptom_plot <- ggplot(
          transcript,
          aes(x = profile, y = symptom_error_mean, fill = guardrail)
        ) +
          geom_boxplot(
            position = position_dodge(width = 0.78),
            width = 0.58,
            outlier.shape = NA,
            alpha = 0.95,
            linewidth = 0.45
          ) +
          geom_point(
            position = position_jitterdodge(jitter.width = 0.08, dodge.width = 0.78),
            color = "black",
            alpha = 0.55,
            size = 1.8
          ) +
          scale_fill_manual(
            values = c("G0" = "#F29A94", "G1" = "#69C3C7"),
            labels = c("G0", "G1"),
            name = "Klinické usmernenie"
          ) +
          labs(
            title = "Priemerná absolútna chyba A1–A9 podľa experimentálnych podmienok",
            x = "Profil odpovedania",
            y = "Priemerná absolútna chyba A1–A9"
          ) +
          theme_minimal(base_size = 12) +
          theme(
            panel.grid.minor = element_blank(),
            plot.title = element_text(face = "bold"),
            legend.position = "right"
          )

        ggsave(
          filename = symptom_out,
          plot = symptom_plot,
          width = 8.8,
          height = 5.6,
          dpi = 300,
          bg = "white"
        )
        """
    ).strip()

    run_r_script(r_code, workdir=repo_root)


def build_appendix_helper(repo_root: Path, fragments_dir: Path) -> None:
    tables_dir = repo_root / "tables"
    figures_dir = repo_root / "figures"
    validation_item_rows = read_csv_rows(tables_dir / "table_s4_expert_review_items.csv")
    validation_seed_rows = read_csv_rows(tables_dir / "table_s5_expert_review_seeds.csv")
    section_1 = "\n\n".join(
        [
            table_block_from_rows(
                build_validation_item_rows(validation_item_rows, include_prefixes=("G", "S")),
                "Prílohová tabuľka D1",
                "Predbežná expertná kontrola jadrových a globálnych položiek",
            ),
            table_block_from_rows(
                build_validation_item_rows(validation_item_rows, include_prefixes=("R",)),
                "Prílohová tabuľka D2",
                "Predbežná expertná kontrola defektových položiek",
            ),
            table_block_from_rows(
                build_seed_quality_rows(validation_seed_rows),
                "Prílohová tabuľka D3",
                "Predbežná expertná kontrola scenárov: kvalita a použiteľnosť",
            ),
            table_block_from_rows(
                build_seed_severity_rows(validation_seed_rows),
                "Prílohová tabuľka D4",
                "Predbežná expertná kontrola scenárov: závažnosť a zhoda s cieľom",
            ),
            table_block(
                tables_dir / "table_2_descriptives.csv",
                "Prílohová tabuľka D5",
                "Úplná deskriptívna tabuľka položiek, symptómových domén a kompozitov",
            ),
            table_block(
                tables_dir / "table_3_item_frequencies.csv",
                "Prílohová tabuľka D6",
                "Úplná frekvenčná tabuľka položiek G1 až G5, S1, S2 a R1 až R5",
            ),
        ]
    )

    section_2 = "\n\n".join(
        [
            table_block(
                tables_dir / "table_6_mixed_models_core.csv",
                "Prílohová tabuľka D7",
                "Plné koeficientové tabuľky jadrových zmiešaných modelov",
                note="b = regresný koeficient; SE = štandardná chyba; IS = interval spoľahlivosti; LMM = lineárny zmiešaný model; CLMM = kumulatívny logistický zmiešaný model.",
            ),
            table_block(
                tables_dir / "table_s6_lmm_sensitivity_transcript_id.csv",
                "Prílohová tabuľka D8",
                "Kontrolné lineárne zmiešané modely s interceptom pre prepis rozhovoru",
                note="Kontrolný model vykázal singularitu a slúži iba ako doplnková kontrola stability smeru efektov.",
            ),
            figure_block(
                figures_dir / "figure_2_emmeans_core_models.png",
                "Prílohový obrázok D1",
                "Odhadované marginálne priemery jadrových modelov",
            ),
        ]
    )

    spearman_rows = read_csv_rows(tables_dir / "table_s1_spearman_transcript_composites.csv")
    section_3 = "\n\n".join(
        [
            table_block_from_rows(
                build_spearman_matrix_rows(spearman_rows),
                "Prílohová tabuľka D9",
                "Spearmanova korelačná matica transcript-level kompozitov",
                note="Uvedené sú Spearmanove korelačné koeficienty rho medzi agregovanými ukazovateľmi na úrovni prepisu rozhovoru.",
            ),
            figure_block(
                figures_dir / "figure_s1_spearman_heatmap.png",
                "Prílohový obrázok D2",
                "Korelačná heatmapa transcript-level kompozitov",
            ),
        ]
    )

    pam_profile_rows = read_csv_rows(tables_dir / "table_s2_pam_cluster_profiles.csv")
    pam_condition_rows = read_csv_rows(tables_dir / "table_s3_pam_cluster_by_condition.csv")
    section_4 = "\n\n".join(
        [
            table_block_from_rows(
                build_pam_profile_rows(pam_profile_rows),
                "Prílohová tabuľka D10",
                "Profily PAM klastrov na agregovaných ukazovateľoch kvality rozhovoru",
                note="Hodnoty sú štandardizované na úrovni vstupov použitého PAM riešenia a slúžia na relatívne porovnanie klastrov, nie na inferenčné testovanie.",
            ),
            table_block_from_rows(
                build_pam_condition_rows(pam_condition_rows),
                "Prílohová tabuľka D11",
                "Rozloženie PAM klastrov podľa experimentálnych podmienok",
            ),
            figure_block(
                figures_dir / "figure_s2_pam_cluster_map.png",
                "Prílohový obrázok D3",
                "Vizualizačná mapa PAM klastrov",
            ),
        ]
    )

    appendix_sections = {
        "appendix_d_section_1.md": section_1,
        "appendix_d_section_2.md": section_2,
        "appendix_d_section_3.md": section_3,
        "appendix_d_section_4.md": section_4,
    }
    for filename, content in appendix_sections.items():
        (fragments_dir / filename).write_text(content + "\n", encoding="utf-8")

    appendix_blocks = "\n\n".join(appendix_sections.values())
    (fragments_dir / "appendix_d_results_support.md").write_text(appendix_blocks + "\n", encoding="utf-8")


def build_fragments(repo_root: Path, fragments_dir: Path) -> None:
    tables_dir = repo_root / "tables"
    outputs_dir = repo_root / "analysis" / "outputs"
    figures_dir = repo_root / "figures"
    fragments_dir.mkdir(parents=True, exist_ok=True)
    refresh_expert_review_outputs(repo_root)

    frequency_global_figure = figures_dir / "figure_2a_global_item_frequencies.png"
    frequency_warning_figure = figures_dir / "figure_2b_warning_item_frequencies.png"
    symptom_error_figure = figures_dir / "figure_5_symptom_error_mean_by_condition.png"

    generate_results_figures(
        repo_root,
        frequency_global_path=frequency_global_figure,
        frequency_warning_path=frequency_warning_figure,
        symptom_error_path=symptom_error_figure,
    )

    dataset_rows = read_csv_rows(tables_dir / "table_1_dataset_summary.csv")
    descriptives_rows = read_csv_rows(tables_dir / "table_2_descriptives.csv")
    lmm_rows = read_csv_rows(outputs_dir / "lmm_core_models_report.csv")
    clmm_rows = read_csv_rows(outputs_dir / "clmm_item_models_report.csv")
    validation_item_rows = read_csv_rows(tables_dir / "table_s4_expert_review_items.csv")
    validation_seed_summary_rows = read_csv_rows(outputs_dir / "expert_review_seed_summary.csv")

    validation = "\n\n".join(
        [
            table_block_from_rows(
                build_validation_heatmap_item_rows(validation_item_rows, include_prefixes=("G", "S")),
                "Tabuľka 3a",
                "Predbežná expertná kontrola globálnych položiek a odhadov",
                note="V near-final Word buildoch je táto tabuľka farebne škálovaná podľa priemerného skóre na škále 1 až 4; tmavšia výplň znamená silnejšiu expertnú podporu.",
            ),
            table_block_from_rows(
                build_validation_heatmap_item_rows(validation_item_rows, include_prefixes=("R",)),
                "Tabuľka 3b",
                "Predbežná expertná kontrola defektových položiek",
                note="V near-final Word buildoch je táto tabuľka farebne škálovaná podľa priemerného skóre na škále 1 až 4; tmavšia výplň znamená silnejšiu expertnú podporu.",
            ),
            table_block_from_rows(
                build_seed_heatmap_rows(
                    validation_seed_summary_rows,
                    columns=[
                        ("Amb. profil", "ambulatory_profile_mean_1_4"),
                        ("Kontext", "context_realism_mean_1_4"),
                        ("Symptómy", "symptom_plausibility_mean_1_4"),
                        ("Jasnosť", "clarity_mean_1_4"),
                    ],
                    id_column="seed_id",
                    label_column="seed_title",
                ),
                "Tabuľka 4a",
                "Predbežná expertná kontrola scenárov: klinická vierohodnosť",
                note="Farebné škálovanie v Word buildoch slúži ako čitateľská pomôcka; pre plné scenárové výstupy vrátane závažnosti a zhody pozri Prílohu D.",
            ),
            table_block_from_rows(
                build_seed_heatmap_rows(
                    validation_seed_summary_rows,
                    columns=[
                        ("Info. dostatok", "information_sufficiency_mean_1_4"),
                        ("Nestereotyp.", "anti_stereotypy_mean_1_4"),
                        ("Pre výskum", "research_usefulness_mean_1_4"),
                        ("Celkovo", "overall_mean_1_4"),
                    ],
                    id_column="seed_id",
                    label_column="seed_title",
                ),
                "Tabuľka 4b",
                "Predbežná expertná kontrola scenárov: výskumná použiteľnosť",
                note="Farebné škálovanie v Word buildoch slúži ako čitateľská pomôcka; pre plné scenárové výstupy vrátane závažnosti a zhody pozri Prílohu D.",
            ),
        ]
    )

    dataset = "\n\n".join(
        [
            table_block_from_rows(
                build_dataset_overview_rows(dataset_rows),
                "Tabuľka 5a",
                "Základná charakteristika analyzovaného súboru hodnotení",
                note="Zdrojom je autoritatívny clean run nad aktuálnym datasetom.",
            ),
            table_block_from_rows(
                build_dataset_cell_rows(dataset_rows),
                "Tabuľka 5b",
                "Počty hodnotení podľa experimentálnych podmienok",
            ),
        ]
    )

    descriptives = "\n\n".join(
        [
            table_block_from_rows(
                build_compact_descriptives_rows(descriptives_rows),
                "Tabuľka 6",
                "Kompaktný prehľad jadrových deskriptívnych ukazovateľov",
                note="V hlavnom texte sú ponechané iba premenné priamo viazané na výskumné otázky a hypotézy. Úplná deskriptívna tabuľka všetkých položiek a kompozitov je určená pre Prílohu D.",
            ),
            figure_block(
                frequency_global_figure,
                "Obrázok 1a",
                "Rozdelenie globálnych hodnotení G1–G5 a S1–S2",
                note="Graf zobrazuje percentuálne rozdelenie odpovedí pre globálne položky a ľudské odhady závažnosti a funkčného dopadu.",
            ),
            figure_block(
                frequency_warning_figure,
                "Obrázok 1b",
                "Rozdelenie varovných signálov R1–R5",
                note="Graf zobrazuje percentuálne rozdelenie odpovedí pre položky zachytávajúce defektové alebo varovné signály rozhovoru.",
            ),
        ]
    )

    measurement = "\n\n".join(
        [
            table_block(
                tables_dir / "table_4_internal_consistency.csv",
                "Tabuľka 7",
                "Vnútorná konzistencia hodnotiacich blokov",
            ),
        ]
    )

    models = "\n\n".join(
        [
            table_block_from_rows(
                build_hypothesis_summary_rows(lmm_rows, clmm_rows),
                "Tabuľka 8",
                "Súhrn odpovedí na hypotézy a výskumné otázky",
                note="Plné koeficientové tabuľky jadrových zmiešaných modelov sú určené pre Prílohu D.",
            ),
            figure_block(
                figures_dir / "figure_1a_plausibility_index_by_condition.png",
                "Obrázok 2",
                "Index klinickej vierohodnosti podľa experimentálnych podmienok",
                note="Čierne body predstavujú jednotlivé hodnotenia; boxy zobrazujú medián a interkvartilové rozpätie. Vyššie skóre znamená vyššiu klinickú vierohodnosť.",
            ),
            figure_block(
                figures_dir / "figure_1b_defect_index_by_condition.png",
                "Obrázok 3",
                "Index defektov podľa experimentálnych podmienok",
                note="Čierne body predstavujú jednotlivé hodnotenia; boxy zobrazujú medián a interkvartilové rozpätie. Vyššie skóre znamená viac defektov, teda menej priaznivý výsledok.",
            ),
            figure_block(
                symptom_error_figure,
                "Obrázok 4",
                "Priemerná absolútna chyba v symptomatických doménach podľa experimentálnych podmienok",
                note="Graf zobrazuje transcript-level rozdelenie ukazovateľa `symptom_error_mean`; nižšie hodnoty znamenajú presnejšiu zhodu s anchor profilom východiskového scenára.",
            ),
        ]
    )

    (fragments_dir / "fragment_validation.md").write_text(validation + "\n", encoding="utf-8")
    (fragments_dir / "fragment_dataset.md").write_text(dataset + "\n", encoding="utf-8")
    (fragments_dir / "fragment_descriptives.md").write_text(descriptives + "\n", encoding="utf-8")
    (fragments_dir / "fragment_measurement.md").write_text(measurement + "\n", encoding="utf-8")
    (fragments_dir / "fragment_models.md").write_text(models + "\n", encoding="utf-8")
    build_appendix_helper(repo_root, fragments_dir)


def build_results_manuscript(source_path: Path, output_path: Path, fragments_dir: Path) -> None:
    text = source_path.read_text(encoding="utf-8")
    for marker, filename in REPLACEMENTS.items():
        fragment_text = (fragments_dir / filename).read_text(encoding="utf-8")
        text = text.replace(marker, fragment_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


def build_appendix_manuscript(source_path: Path, output_path: Path, fragments_dir: Path) -> None:
    text = source_path.read_text(encoding="utf-8")
    for marker, filename in APPENDIX_REPLACEMENTS.items():
        fragment_text = (fragments_dir / filename).read_text(encoding="utf-8")
        text = text.replace(marker, fragment_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build manuscript-ready full-run results fragments.")
    parser.add_argument(
        "--output",
        required=True,
        help="Path for the built 40_results.md with injected fragments.",
    )
    parser.add_argument(
        "--appendix-output",
        help="Optional path for built appendix markdown with injected Appendix D support.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    fragments_dir = repo_root / "tables" / "full_run_results"
    source_path = repo_root / "manuscript" / "40_results.md"
    output_path = Path(args.output).resolve()

    build_fragments(repo_root, fragments_dir)
    build_results_manuscript(source_path, output_path, fragments_dir)
    if args.appendix_output:
        appendix_source_path = repo_root / "manuscript" / "71_public_appendix_draft.md"
        appendix_output_path = Path(args.appendix_output).resolve()
        build_appendix_manuscript(appendix_source_path, appendix_output_path, fragments_dir)
    print(output_path)


if __name__ == "__main__":
    main()
