# Data Requirements for Chapter 3

The underlying data used in Chapter 3 are not included in this repository.

## Restricted inputs

The workflow requires authorized access to:

1. Aggregated mobile-location measures at the census-tract level.
2. Geolocated digital-discourse records and the derived tract-level GEWI fields.
3. Localized transaction values aggregated to the census-tract level.
4. Census-tract geometries used for spatial integration and neighborhood construction.

These materials are restricted by provider agreements, platform conditions, confidentiality requirements, or combinations of these constraints.

## Expected local structure

```text
chapter_3_paper_2/
  data/
    private/
      mobility/
      geolocated_discourse/
      gewi/
      sales/
      census_tracts/
      analysis/
```

The notebooks use paths relative to the Chapter 3 directory. File names and required fields are described in the notebooks and the accompanying data dictionaries.

## Public substitutes

The `data_dictionary/` directory provides variable definitions, units, aggregation levels, and interpretive limits. No synthetic data are presented as substitutes for the restricted empirical records.
