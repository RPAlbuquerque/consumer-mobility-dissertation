# Data Requirements for Chapter 3

The empirical inputs used in Chapter 3 are not included in this repository. The public notebooks document the analytical workflow, but complete execution requires independently authorized access to the restricted data described below.

## Required inputs

The Chapter 3 workflow combines four empirical layers at the census-tract level.

| Input | Analytical role | Temporal coverage | Access status |
|---|---|---|---|
| Aggregated mobile-location measures | Measures consumer presence and visitation across census tracts. | August 2024 | Proprietary and not redistributed. |
| Geolocated digital-discourse records or authorized derived GEWI files | Supports construction of place-based digital sentiment and its positive and negative components. | 2010 through July 12, 2023 | Restricted and not redistributed. |
| Localized transaction values | Measures localized sales performance for the focal manufacturer and offering. | August 2024 | Commercially confidential and not redistributed. |
| Census-tract geometries | Provides the common spatial support, projected coordinates, neighborhood structures, and map geometries. | Geographic boundary file used in the analysis | Must be obtained from an authorized or official source. |

Consumer mobility and localized sales performance share the August 2024 analytical window. GEWI summarizes historically accumulated geolocated discourse and is not interpreted as contemporaneous monthly sentiment.

## Canonical input structure

The empirical-analysis notebook expects the following project-relative structure:

```text
chapter_3_paper_2/
└── data/
    └── private/
        ├── mobility/
        │   └── mobility_by_tract_aug2024.csv.gz
        ├── geolocated_discourse/
        │   └── [authorized source files organized as documented in the GEWI notebook]
        ├── gewi/
        │   └── gewi_observed_by_tract.csv.gz
        ├── sales/
        │   └── sales_by_tract_aug2024.csv.gz
        ├── census_tracts/
        │   └── census_tracts.gpkg
        └── analysis/
            ├── figures/
            └── tables/
```

The mobility- and GEWI-construction notebooks document the intermediate files created from authorized source records. The empirical-analysis notebook begins from the tract-level mobility, sales, and directly observed GEWI files shown above.

File names may be adapted locally when required by an authorized provider, but the corresponding notebook paths and field mappings must be updated consistently.

## Expected spatial identifiers

The analytical inputs must contain a compatible census-tract identifier that can be normalized to the 15-digit tract code used in the integrated analysis.

Each tract-level input should contain no more than one analytical row per census tract after aggregation. The census geometry must:

- contain the corresponding tract identifier;
- include valid polygon geometries;
- declare its source coordinate reference system; and
- support projection to the coordinate system used for distance and neighborhood calculations.

Census tracts provide a common spatial support for aligning mobility, GEWI, and localized sales performance. They are administrative units and are not interpreted as natural local-market boundaries.

## Coverage requirements

The integrated analysis reported in the dissertation contains 726 urban census tracts.

- GEWI was calculated directly in 96 tracts containing at least five retained messages.
- Inverse-distance weighting expanded GEWI coverage to another 630 tracts.
- The expanded values support the integrated analysis but do not become directly observed place-based digital sentiment.
- The 96 directly observed tracts were retained for sensitivity assessment.
- Mobility records represent observed visiting devices rather than identified purchasers of electrical materials.
- Localized sales performance represents transaction values attributed to the focal manufacturer and census tract rather than total sales across all firms.

## Data dictionaries

The [`../data_dictionary/`](../data_dictionary/) directory documents the variables, units, aggregation levels, spatial identifiers, analytical roles, and interpretive boundaries associated with the required inputs.

The dictionaries describe the expected schemas without disclosing restricted observations. No synthetic data are presented as substitutes for the empirical records.

## Confidentiality and redistribution

The following materials must not be committed to the public repository:

- proprietary mobile-location records;
- device-level observations or trajectories;
- raw geolocated messages;
- message-level user or account identifiers;
- confidential transaction records;
- provider-specific derived files whose redistribution is restricted;
- credentials, access tokens, or private download links; and
- intermediate files containing restricted row-level observations.

The `.gitignore` rules and the `data/private/` structure are intended to keep these materials outside version control. Researchers using authorized copies remain responsible for complying with the corresponding provider agreements, platform conditions, confidentiality requirements, and data-protection obligations.

## Reproduction status

The public repository supports inspection of the data contracts, transformations, spatial procedures, model specifications, and diagnostics. It does not provide unrestricted end-to-end reproduction because the empirical inputs cannot be redistributed.

A complete data-dependent execution requires authorized files that conform to the documented schemas and spatial identifiers. The reported results should not be expected from substitute or synthetic data.
