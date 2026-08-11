from __future__ import annotations

import csv
from pathlib import Path


CHAPTER_DIR = Path(__file__).resolve().parents[1]
INCLUDED_STUDIES = CHAPTER_DIR / "included_studies" / "included_studies.tsv"
EXPECTED_STUDIES = 86
EXPECTED_COLUMNS = {
    "Study",
    "Article Title",
    "Journal",
    "Primary Synthesis Domain",
    "Contributions to the Exposure–Conversion Synthesis",
}


def main() -> None:
    with INCLUDED_STUDIES.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    if len(rows) != EXPECTED_STUDIES:
        raise ValueError(
            f"Expected {EXPECTED_STUDIES} included studies, found {len(rows)}."
        )

    columns = set(rows[0]) if rows else set()
    missing_columns = EXPECTED_COLUMNS - columns
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    titles = [row["Article Title"].strip().casefold() for row in rows]
    duplicate_titles = sorted({title for title in titles if titles.count(title) > 1})
    if duplicate_titles:
        raise ValueError(f"Duplicate article titles: {duplicate_titles}")

    empty_cells = [
        (index, column)
        for index, row in enumerate(rows, start=2)
        for column in EXPECTED_COLUMNS
        if not row[column].strip()
    ]
    if empty_cells:
        raise ValueError(f"Empty required cells: {empty_cells[:10]}")

    print(
        "Validation passed: 86 unique studies, all required columns present, "
        "and no empty required cells."
    )


if __name__ == "__main__":
    main()
