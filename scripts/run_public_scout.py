#!/usr/bin/env python3
"""Build the public-safe photodimerization scout outputs.

This script intentionally reads only data/public_demo_cases.csv. It is a small
external-facing version of the scout loop: preserve public source
anchors, order the rows for review, and write explanation artifacts with caveats
kept visible.
"""

from __future__ import annotations

import csv
import html
from pathlib import Path
from typing import Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "public_demo_cases.csv"
OUT = ROOT / "outputs"

FIELDNAMES = [
    "illustrative_triage_order",
    "case_id",
    "row_class",
    "substrate",
    "environment",
    "source_anchor",
    "public_outcome_class",
    "organization_signal",
    "geometry_signal",
    "public_use_status",
    "caveat",
    "next_experiment_or_source_check",
]

STATUS_WEIGHT = {
    "public_now": 4,
    "promote_public_demo": 3,
    "public_schema_demo": 1,
}

CLASS_WEIGHT = {
    "public_crystal_water_comparison": 4,
    "public_evidence": 3,
    "public_water_outcome_only": 2,
    "schema_demo_only": 0,
}

COLORS = {
    "public_crystal_water_comparison": "#6b4ca0",
    "public_evidence": "#0b7378",
    "public_water_outcome_only": "#516aa3",
    "schema_demo_only": "#9a7a2f",
}


def load_rows() -> List[Dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def order_rows(rows: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    ordered = sorted(
        rows,
        key=lambda row: (
            STATUS_WEIGHT.get(row.get("public_use_status", ""), 0),
            CLASS_WEIGHT.get(row.get("row_class", ""), 0),
            row.get("case_id", ""),
        ),
        reverse=True,
    )
    for index, row in enumerate(ordered, start=1):
        row["illustrative_triage_order"] = str(index)
    return ordered


def write_ranked(rows: List[Dict[str, str]]) -> Path:
    OUT.mkdir(exist_ok=True)
    path = OUT / "public_demo_ranked_candidates.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows({key: row.get(key, "") for key in FIELDNAMES} for row in rows)
    return path


def write_cards(rows: List[Dict[str, str]]) -> Path:
    path = OUT / "public_demo_explanation_cards.md"
    lines = [
        "# Public Demo Explanation Cards",
        "",
        "Generated only from `data/public_demo_cases.csv`. These cards are public-safe literature/demo scaffolds for the HHMI proof packet; they are not a trained-model validation set and the order below is illustrative triage, not a predictive accuracy claim.",
        "",
        f"Public demo rows: {len(rows)} total.",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"## {row['illustrative_triage_order']}. {row['substrate']} - {row['environment']}",
                "",
                f"- **Case ID:** {row['case_id']}",
                f"- **Row class / status:** {row['row_class']} / {row['public_use_status']}",
                f"- **What it shows:** {row['public_outcome_class']}",
                f"- **Why it matters:** {row['organization_signal']}",
                f"- **Geometry signal:** {row['geometry_signal']}",
                f"- **Source anchor:** {row['source_anchor']}",
                f"- **Caveat:** {row['caveat']}",
                f"- **Next check:** {row['next_experiment_or_source_check']}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def trim(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def write_svg(rows: List[Dict[str, str]]) -> Path:
    row_height = 82
    width = 1120
    height = 104 + row_height * len(rows)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fffdf8"/>',
        '<text x="28" y="34" font-family="-apple-system,Inter,sans-serif" font-size="22" font-weight="700" fill="#27231f">HHMI public photodimerization scout rows</text>',
        '<text x="28" y="60" font-family="-apple-system,Inter,sans-serif" font-size="13" fill="#51483e">Built only from data/public_demo_cases.csv; illustrative triage, not model validation.</text>',
    ]
    for index, row in enumerate(rows):
        y = 84 + index * row_height
        color = COLORS.get(row.get("row_class", ""), "#516aa3")
        title = html.escape(f"{row['substrate']} - {row['environment']}")
        source = html.escape(f"{row['row_class']} - {trim(row['source_anchor'], 132)}")
        caveat = html.escape(f"Caveat: {trim(row['caveat'], 142)}")
        parts.extend(
            [
                f'<rect x="24" y="{y}" width="1072" height="68" rx="14" fill="#f4ecdf"/>',
                f'<rect x="24" y="{y}" width="10" height="68" rx="5" fill="{color}"/>',
                f'<text x="48" y="{y + 22}" font-family="-apple-system,Inter,sans-serif" font-size="15" font-weight="700" fill="#27231f">{title}</text>',
                f'<text x="48" y="{y + 43}" font-family="-apple-system,Inter,sans-serif" font-size="12" fill="#51483e">{source}</text>',
                f'<text x="48" y="{y + 61}" font-family="-apple-system,Inter,sans-serif" font-size="12" fill="#6a372f">{caveat}</text>',
            ]
        )
    parts.append("</svg>")
    path = OUT / "public_demo_rows.svg"
    path.write_text("\n".join(parts), encoding="utf-8")
    return path


def main() -> None:
    rows = order_rows(load_rows())
    ranked = write_ranked(rows)
    cards = write_cards(rows)
    svg = write_svg(rows)
    print(f"Loaded {len(rows)} public demo rows")
    print(f"Wrote {ranked}")
    print(f"Wrote {cards}")
    print(f"Wrote {svg}")


if __name__ == "__main__":
    main()
