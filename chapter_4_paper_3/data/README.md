# Data Requirements for Chapter 4

The Chapter 4 workflow combines restricted aggregated mobility data with a publicly available annual VIIRS nighttime-light raster.

## Restricted mobility input

The tract-level mobility input is not redistributed. An authorized local copy must contain:

- a unique census-tract identifier;
- census-tract geometry;
- the seven standardized mobility indicators described in the chapter;
- the retained MII field; and
- the normalized MII field.

## VIIRS input

The workflow uses annual 2024 VIIRS nighttime-light intensity as external contextual evidence and as the ancillary allocation surface in the São Paulo analysis. Users should obtain the corresponding raster from its official provider and document the version used.

## Expected local structure

```text
chapter_4_paper_3/
  data/
    private/
      mii_brazil_analysis_ready.gpkg.zip
    external/
      VIIRS_annual_2024.zip
```

The public notebook refers only to these project-relative locations. Restricted input data, provider URLs, and credentials are intentionally absent.
