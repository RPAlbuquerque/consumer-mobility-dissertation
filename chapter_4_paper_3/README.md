# Chapter 4 / Paper 3

## Consumer Mobility and the Spatial Organization of Local Market Access

This directory contains the public analytical materials for Chapter 4 of the dissertation. The study examines what multiple indicators of aggregated consumer mobility can reveal about the spatial organization of local market access when sales and other direct market outcomes are unavailable. It combines seven mobility indicators in the Mobility-based Market Access Index (MMAI), examines global and local spatial structure, organizes local mobility configurations into four exploratory regimes, compares those regimes with nighttime-light intensity, and applies aggregate-preserving spatial downscaling in the São Paulo metropolitan window.

## Research question

> How can multiple indicators of aggregated consumer mobility be integrated and spatially represented to characterize local market access beyond visit volume when direct market outcomes are unavailable?

## Role in the dissertation

Chapter 2 reviews what existing research establishes about consumer mobility and local sales, while Chapter 3 examines the association between consumer mobility and localized sales performance in the 726 census tracts for which mobility, GEWI, and sales could be aligned. Chapter 4 addresses a different measurement problem by examining the broader national mobility layer without a direct sales outcome.

In this chapter, local market access is a bounded description of how observed visitation was organized within a geographic area during the study period. The concept covers the amount of visitation, the breadth of the observed visitor base, visitors classified as new or returning, visit duration, and week-to-week variability. `Local` specifies the geographic scope of the analysis, while `market` identifies the decision context in which firms may use the evidence. The term does not imply physical accessibility, demand, sales, profitability, or the existence of a localized market opportunity.

## Empirical setting

The national analytical file contains 387,779 verified Brazilian census tracts and seven mobility indicators for August 2024:

1. visit volume;
2. unique visitors;
3. new visitors;
4. repeat visitors;
5. average dwell time;
6. weekly stability in unique visitors; and
7. weekly stability in visit counts.

The count and dwell-time indicators were transformed using `log(1 + x)`. The coefficients of variation used to represent weekly variability were sign-reversed so that higher standardized values indicated greater stability, after which all seven indicators were standardized nationally. These indicators retain related aspects of visitation and include partially overlapping count measures; they are not treated as seven independent latent constructs.

## Analytical workflow

| Stage | Analytical role |
|---|---|
| MMAI construction | Combines the seven nationally standardized indicators through an explicit equal-weight average and rescales the retained index for presentation. |
| Global covariance alignment | Uses principal component analysis to compare the equal-weight MMAI with the dominant covariance pattern among the same seven indicators. |
| Spatial organization | Uses a row-standardized eight-nearest-neighbor matrix and Moran's I to examine whether similar MMAI values tend to occur near one another. |
| Local mobility structure | Estimates local covariance patterns at 7,398 spatially distributed focal tracts, using 200 nearest tracts in the primary specification. |
| Sensitivity analysis | Compares the dominant local structure with geographically weighted PCA at `k = 200` and with unweighted local PCA at `k = 100` and `k = 300`. |
| Exploratory access regimes | Applies k-means to the local PC1 and PC2 scores and variance shares, producing four exploratory configurations that are assigned to all tracts by nearest-focal location. |
| External differentiation | Compares the regimes with annual 2024 VIIRS nighttime-light intensity and evaluates held-out descriptive fit for visit volume, MMAI, and combined specifications. |
| Spatial downscaling | Uses VIIRS-derived within-tract weights to allocate each represented São Paulo tract's MMAI value among 100 m cells while algebraically preserving the original tract value. |

The notebook does not use PCA to construct the MMAI. The retained index is the equal-weight composite, while PCA provides an internal covariance-alignment check based on the same inputs.

## Main reported results

- PC1 explained 61.43% of total variance, and its loadings were higher for weekly stability and the numbers of new, repeat, and unique visitors than for visit volume.
- After sign orientation, the tract-level correlation between the MMAI and PC1 was 0.9447, indicating close internal alignment without constituting external validation or evidence of a single latent construct.
- The rescaled MMAI showed positive spatial autocorrelation under the selected neighborhood definition (`Moran's I = 0.4550`, `p <= .01`, the minimum attainable value with 99 permutations).
- The dominant local mobility pattern remained comparatively similar across the alternative geographic weights and neighborhood sizes, while the four regimes organized exploratory mobility configurations rather than ranking tracts by market quality.
- VIIRS data covered 220,195 tracts. In the 120,000-tract held-out comparison, visit volume alone produced stronger descriptive fit to nighttime-light intensity than the MMAI alone (`R2 = 0.3799` versus `0.2529`), while adding the MMAI increased the visit-volume specification to `R2 = 0.3904` and adding the regime indicators increased it to `0.3919`.
- The São Paulo analysis selected 52,621 tracts, of which 47,529 were represented by at least one 100 m cell. The downscaling procedure preserved each represented tract's original MMAI value exactly when the allocated cells were aggregated back to the tract.

## Directory contents

```text
chapter_4_paper_3/
├── README.md
├── notebooks/
│   ├── PUBLIC_COPY_NOTES.md
│   └── consumer_mobility_market_access.ipynb
├── data_dictionary/
│   ├── README.md
│   └── data_dictionary_mobility_market_access.xlsx
├── data/
│   └── README.md
├── environment/
│   ├── README.md
│   └── requirements.txt
└── outputs/
    └── README.md
```

### `notebooks/`

Contains the public analytical notebook for MMAI alignment, spatial dependence, local covariance analysis, exploratory access regimes, VIIRS comparisons, and aggregate-preserving spatial downscaling.

### `data_dictionary/`

Defines the seven mobility indicators, MMAI fields, tract identifier and geometry requirements, VIIRS variables, derived analytical fields, units, and interpretation boundaries.

### `data/`

Documents the expected project-relative input structure and distinguishes the restricted aggregated mobility data from the publicly obtainable census-tract boundaries and VIIRS raster. No restricted empirical observations are stored in the repository.

### `environment/`

Records the principal Python dependencies required by the public notebook and explains the limits of reconstructing the original restricted computing environment.

### `outputs/`

Documents the non-restricted figures selected to support inspection of the workflow and reported diagnostics without redistributing the underlying mobility records.

## Data access and reproduction status

The tract-level mobility input is proprietary and is not redistributed through this repository. Authorized execution requires an analysis-ready file containing the census-tract identifier, tract geometry, seven mobility indicators, retained MMAI, and rescaled MMAI. The annual 2024 VIIRS nighttime-light raster and Brazilian census-tract boundaries are publicly obtainable from their respective providers.

The public notebook uses project-relative paths and contains no private credentials, individual trajectories, device histories, or personally identifiable information. The code, parameters, and analytical sequence are public, while complete data-dependent reproduction requires authorized access to the restricted mobility input.

## Interpretation boundaries

- The MMAI describes the combined mobility profile represented by its seven inputs; it does not measure demand, sales, profitability, physical accessibility, or market quality.
- Local market access refers to the organization of observed presence and visitation within the selected geographic and temporal support.
- Visit volume remains an informative part of the analysis and is not treated as a complete representation of how observed local access is organized.
- The exploratory regimes are mobility configurations rather than rankings, consumer segments, administrative regions, natural markets, or performance classes.
- VIIRS nighttime-light intensity provides partial contextual evidence about local economic activity; it is not interpreted as daytime activity, demand, sales, conversion, or market performance.
- The national VIIRS comparison is descriptive and does not validate the MMAI or establish causal relationships.
- The 100 m São Paulo surface is a conditional allocation of tract-level MMAI values under the selected VIIRS weighting rule. It does not represent mobility observed at 100 m or an independently estimated cell-level index.
- Census tracts provide the analytical spatial support and are not treated as natural local-market boundaries.

## Recognition

The project from which this chapter originated, *From Mobility Intensity to Market Infrastructure: A Spatial AI Framework for Recovering Hidden Spatial Regimes and Multiscale Variation*, received third place in the [I-GUIDE Spatial AI Challenge 2025-26](https://i-guide.io/spatial-ai-challenge-2025-26/challenge-winners/) and was presented at the Spatial AI Challenge Winners Showcase during the I-GUIDE Forum 2026 & HDR Ecosystem Conference. The study was also accepted for presentation at the XXVIII ENGEMA 2026.

The project team comprised Rafael Albuquerque, Jéssica Miranda, Vinícius Andrade Brei, and Siqin (Sisi) Wang.

## Related dissertation materials

- The dissertation-level argument and repository map are available in the [root README](../README.md).
- The systematic-integrative review of consumer mobility and local sales is documented in [`chapter_2_paper_1/`](../chapter_2_paper_1/).
- The study of consumer mobility, place-based digital sentiment, and localized sales performance is documented in [`chapter_3_paper_2/`](../chapter_3_paper_2/).

## Citation

Please cite the dissertation and Chapter 4 when using the MMAI documentation, exploratory access-regime workflow, VIIRS comparison, or aggregate-preserving spatial downscaling procedure. Complete bibliographic information will be added after the dissertation is deposited in the UFRGS institutional repository.
