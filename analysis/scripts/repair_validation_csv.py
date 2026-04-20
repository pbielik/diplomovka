#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    default_input = repo_root / "analysis" / "validity data" / "data.csv"
    default_output = repo_root / "analysis" / "validity data" / "data_repaired_trimmed.csv"

    parser = argparse.ArgumentParser(
        description=(
            "Repair malformed validation CSV rows by trimming them to the header width. "
            "Use this only as a structural repair for the raw export; `data.xlsx` remains the source of truth."
        )
    )
    parser.add_argument("--input", default=str(default_input), help="Path to the malformed raw CSV export.")
    parser.add_argument(
        "--output",
        default=str(default_output),
        help="Path for the repaired CSV with rows trimmed/padded to header width.",
    )
    return parser.parse_args()


def repair_csv(input_path: Path, output_path: Path) -> dict[str, object]:
    with input_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        if not header:
            raise ValueError(f"Input CSV `{input_path}` is empty or missing a header row.")

        header_len = len(header)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        repaired_rows = 0
        padded_rows = 0
        untouched_rows = 0
        repaired_line_refs: list[str] = []

        with output_path.open("w", encoding="utf-8", newline="") as out_handle:
            writer = csv.writer(out_handle)
            writer.writerow(header)

            for line_number, row in enumerate(reader, start=2):
                if len(row) > header_len:
                    writer.writerow(row[:header_len])
                    repaired_rows += 1
                    repaired_line_refs.append(f"line {line_number}: {len(row)} -> {header_len}")
                elif len(row) < header_len:
                    writer.writerow(row + [""] * (header_len - len(row)))
                    padded_rows += 1
                    repaired_line_refs.append(f"line {line_number}: {len(row)} -> {header_len}")
                else:
                    writer.writerow(row)
                    untouched_rows += 1

    return {
        "header_len": header_len,
        "repaired_rows": repaired_rows,
        "padded_rows": padded_rows,
        "untouched_rows": untouched_rows,
        "repaired_line_refs": repaired_line_refs,
        "output_path": str(output_path),
    }


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV does not exist: {input_path}")

    summary = repair_csv(input_path=input_path, output_path=output_path)
    print(f"Validation CSV repaired: {summary['output_path']}")
    print(f"Header columns: {summary['header_len']}")
    print(f"Trimmed rows: {summary['repaired_rows']}")
    print(f"Padded rows: {summary['padded_rows']}")
    print(f"Untouched rows: {summary['untouched_rows']}")
    if summary["repaired_line_refs"]:
        print("Changed rows:")
        for ref in summary["repaired_line_refs"]:
            print(f"- {ref}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
