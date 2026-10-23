# Data requirements for Chapter 4

The Chapter 4 workflow combines a restricted tract-level mobility file with a publicly obtainable annual VIIRS nighttime-light raster. The repository does not contain empirical mobility observations, individual trajectories, device histories, or personally identifiable information.

## Restricted mobility input

Authorized execution requires one analysis-ready GeoPackage containing a single record for each of the 387,779 verified Brazilian census tracts and the following fields:

- a stable census-tract identifier;
- census-tract geometry;
- visit volume;
- unique visitors;
- new visitors;
- repeat visitors;
- average dwell time;
- weekly stability in unique visitors;
- weekly stability in visit counts;
- the retained Mobility-based Market Access Index (MMAI); and
- the rescaled MMAI used for presentation and spatial analysis.

The analytical file already contains the transformations and national standardization described in Chapter 4. Count and dwell-time measures were transformed using `log(1 + x)`, weekly coefficients of variation were sign-reversed so that higher values represented greater stability, and the seven indicators were standardized nationally before the equal-weight MMAI was calculated.

The public notebook retains the legacy local filename `mii_brazil_analysis_ready.gpkg.zip` and may encounter the internal field aliases `mii` and `mii_norm`. These implementation names refer to the final MMAI and its rescaled form; they do not indicate a separate Market Infrastructure Index or a different construct.

## VIIRS input

The workflow uses annual 2024 VIIRS nighttime-light radiance in two analytically distinct ways:

1. **National external context.** Mean nighttime-light intensity is calculated for the 220,195 census tracts with valid VIIRS coverage and is used to compare the four exploratory mobility-based access regimes and the descriptive fit of visit-volume and MMAI specifications.
2. **São Paulo ancillary allocation surface.** Reprojected VIIRS values provide normalized within-tract weights for allocating each represented tract's MMAI value among 100 m cells while preserving the original tract value.

Nighttime-light intensity provides partial contextual evidence about local economic activity. It does not measure daytime activity, demand, sales, conversion, profitability, or market performance. Because VIIRS supplies the weights used in the São Paulo allocation, it cannot independently validate the resulting cell values.

Users should obtain the annual 2024 raster from the official VIIRS provider and document the product version and retrieval date used in any independent execution.

## Expected local structure

```text
chapter_4_paper_3/
└── data/
    ├── private/
    │   └── mii_brazil_analysis_ready.gpkg.zip
    └── external/
        └── VIIRS_annual_2024.zip
