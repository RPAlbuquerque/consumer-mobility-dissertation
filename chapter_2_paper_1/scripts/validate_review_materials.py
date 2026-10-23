from __future__ import annotations

import csv
from pathlib import Path


CHAPTER_DIR = Path(__file__).resolve().parents[1]
INCLUDED_STUDIES_DIR = CHAPTER_DIR / "included_studies"
CSV_FILE = INCLUDED_STUDIES_DIR / "included_studies.csv"
TSV_FILE = INCLUDED_STUDIES_DIR / "included_studies.tsv"

EXPECTED_STUDIES = 86
EXPECTED_COLUMNS = [
    "Study",
    "Article Title",
    "Journal",
    "Main Evidence Represented",
    "Role in the Synthesis",
]

EXPECTED_EVIDENCE_DOMAINS = {
    "Retail traffic, visits, and store conversion",
    "Local consumption and spending flows",
    "Commercial districts, market areas, and spatial infrastructure",
    "Location-based marketing and digital conversion",
    "Services, hospitality, and non-retail local markets",
    "General mobility-market theory and methods",
}

EXPECTED_SYNTHESIS_ROLES = {
    "Mobility measurement and visitation evidence",
    "Mobility traces linked to market outcomes",
    "Location-based marketing linked to offline behavior",
    "Spatial access and observed mobility",
    "Commercial districts and place-based markets",
    "Local consumption and spending flows",
    "Local conditions shaping mobility and commercial outcomes",
    "Transferable mobility-market theory or methods",
}

OBSOLETE_TERMS = {
    "Exposure–Conversion Synthesis",
    "Conditional Mobility–Sales Synthesis",
}


def read_studies(path: Path, delimiter: str) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    return fieldnames, rows


def validate_file(
    path: Path,
    fieldnames: list[str],
    rows: list[dict[str, str]],
) -> None:
    if fieldnames != EXPECTED_COLUMNS:
        raise ValueError(
            f"{path.name}: expected columns {EXPECTED_COLUMNS}, found {fieldnames}."
        )

    if len(rows) != EXPECTED_STUDIES:
        raise ValueError(
            f"{path.name}: expected {EXPECTED_STUDIES} included studies, "
            f"found {len(rows)}."
        )

    empty_cells = [
        (index, column)
        for index, row in enumerate(rows, start=2)
        for column in EXPECTED_COLUMNS
        if not (row.get(column) or "").strip()
    ]
    if empty_cells:
        raise ValueError(f"{path.name}: empty required cells: {empty_cells[:10]}")

    studies = [(row.get("Study") or "").strip().casefold() for row in rows]
    duplicate_studies = sorted(
        {study for study in studies if studies.count(study) > 1}
    )
    if duplicate_studies:
        raise ValueError(
            f"{path.name}: duplicate study identifiers: {duplicate_studies}"
        )

    titles = [(row.get("Article Title") or "").strip().casefold() for row in rows]
    duplicate_titles = sorted({title for title in titles if titles.count(title) > 1})
    if duplicate_titles:
        raise ValueError(f"{path.name}: duplicate article titles: {duplicate_titles}")

    invalid_domains = sorted(
        {
            row["Main Evidence Represented"].strip()
            for row in rows
            if row["Main Evidence Represented"].strip()
            not in EXPECTED_EVIDENCE_DOMAINS
        }
    )
    if invalid_domains:
        raise ValueError(
            f"{path.name}: unexpected evidence domains: {invalid_domains}"
        )

    invalid_roles = sorted(
        {
            role.strip()
            for row in rows
            for role in row["Role in the Synthesis"].split(";")
            if role.strip() not in EXPECTED_SYNTHESIS_ROLES
        }
    )
    if invalid_roles:
        raise ValueError(f"{path.name}: unexpected synthesis roles: {invalid_roles}")

    obsolete_hits = sorted(
        {
            term
            for row in rows
            for value in row.values()
            for term in OBSOLETE_TERMS
            if term.casefold() in (value or "").casefold()
        }
    )
    if obsolete_hits:
        raise ValueError(f"{path.name}: obsolete terminology found: {obsolete_hits}")


def main() -> None:
    csv_columns, csv_rows = read_studies(CSV_FILE, ",")
    tsv_columns, tsv_rows = read_studies(TSV_FILE, "\t")

    validate_file(CSV_FILE, csv_columns, csv_rows)
    validate_file(TSV_FILE, tsv_columns, tsv_rows)

    if csv_rows != tsv_rows:
        raise ValueError(
            "The CSV and TSV files do not contain the same studies in the same order."
        )

    print(
        "Validation passed: CSV and TSV contain the same 86 unique studies, "
        "use the final Table A1 columns and categories, and contain no empty "
        "required cells or obsolete synthesis terminology."
    )


if __name__ == "__main__":
    main()
