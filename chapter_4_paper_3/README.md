# Chapter 4 / Paper 3: Consumer Mobility and Local Market Access

## Consumer Mobility and the Spatial Organization of Local Market Access

This directory contains the public analytical documentation for Chapter 4 of the dissertation. The study examines whether aggregated consumer mobility can support pre-outcome local market diagnosis by revealing recurrent and spatially differentiated access conditions that visit volume alone does not represent.

## Research question

> Can aggregated consumer mobility support pre-outcome local market diagnosis by revealing recurrent and spatially differentiated access conditions beyond visit volume?

## Role in the dissertation

Paper 3 moves the dissertation to the stage before sales and other direct market outcomes are available. Chapter 3 documents that comparable consumer mobility does not correspond to the same localized sales performance everywhere, while Chapter 4 examines what mobility can reveal about the organization of local access when that performance is not yet observed.

The chapter focuses on mobility-based market infrastructure, defined as the recurrent-access dimension of the broader latent market infrastructure introduced in Chapter 2. This dimension is examined through visitation scale, visitor reach, inflow, recurrence, dwell time, and temporal stability, without treating recurrent access as demand, market opportunity, or performance.

## Empirical setting

The national analysis uses 387,779 verified Brazilian census tracts and seven standardized mobility indicators:

1. Visit volume.
2. Unique visitors.
3. New visitors.
4. Repeat visitors.
5. Average dwell time.
6. Temporal stability in unique visitors.
7. Temporal stability in visit counts.

The mobility measures cover August 2024. Census tracts provide analytical spatial support rather than natural local-market boundaries, so the results describe spatial differences during the observation month and do not establish whether the same access structure persisted over time.

## Analytical workflow

The public notebook documents the following sequence:

| Stage | Analytical role |
|---|---|
| MII alignment | Compares the retained equal-weight Market Infrastructure Index with the dominant covariance structure of the seven mobility indicators. |
| Spatial organization | Assesses whether normalized MII values are spatially organized under an explicit nearest-neighbor definition. |
| Localized mobility signatures | Estimates local covariance structures at spatially distributed focal locations and evaluates sensitivity to geographic weighting and neighborhood size. |
| Mobility-based access regimes | Organizes continuous local mobility signatures into four exploratory configurations for mapping and comparison. |
| VIIRS comparison | Places the mobility configurations beside nighttime-light intensity as bounded external context for local economic intensity. |
| Fine-scale allocation | Distributes tract-level MII values across a 100 m grid in the São Paulo metropolitan window while preserving the aggregate value of represented tracts. |

The notebook does not use PCA to create the retained MII. The index was constructed during preprocessing as an equal-weight combination of the seven standardized indicators, while PCA was subsequently used as an internal covariance-alignment check.

## Directory contents

```text
chapter_4_paper_3/
├── README.md
├── notebooks/
│   └── consumer_mobility_market_access.ipynb
├── data_dictionary/
│   └── data_dictionary_mobility_market_access.xlsx
├── data/
│   └── README.md
├── environment/
│   └── requirements.txt
└── outputs/
    └── README.md
```

### `notebooks/`

Contains the public analytical notebook for MII alignment, global and local spatial diagnostics, exploratory mobility-based access regimes, VIIRS comparisons, and conditional fine-scale allocation.

### `data_dictionary/`

Defines the mobility indicators, MII fields, tract identifier and geometry requirements, VIIRS variables, preprocessing status, units, and interpretation boundaries.

### `data/`

Documents the expected local input structure and distinguishes the restricted aggregated mobility input from the publicly obtainable VIIRS raster. No restricted empirical observations are stored in this directory.

### `environment/`

Contains the principal Python dependencies required by the notebook.

### `outputs/`

Contains only non-restricted supporting outputs selected to make the workflow and reported diagnostics easier to inspect without redistributing the underlying mobility records.

## Data access and reproduction status

The tract-level mobility input is proprietary and is not redistributed through this repository. Authorized execution requires a local analysis-ready file containing the census-tract identifier, tract geometry, seven standardized mobility indicators, retained MII, and normalized MII.

The annual 2024 VIIRS nighttime-light raster is publicly obtainable from its official provider. The public notebook uses project-relative input paths and does not include private credentials, provider-specific restricted links, individual trajectories, device histories, or personally identifiable information.

The code, parameters, and analytical sequence are public, while complete data-dependent reproduction requires authorized access to the restricted mobility input. This distinction makes the workflow auditable without presenting restricted data as openly available.

## Interpretation boundaries

- Mobility-based market infrastructure represents a pre-outcome access dimension rather than the complete physical, institutional, or competitive infrastructure of a market.
- The MII is an empirical index of mobility-based access conditions and is not the theoretical construct itself.
- Visit volume is one component of the access representation and is not interpreted as demand or performance.
- Mobility-based access regimes are exploratory configurations, not rankings, consumer segments, administrative regions, or market-performance classes.
- VIIRS nighttime-light intensity provides contextual proxy evidence and is not interpreted as sales, demand, conversion, or market performance.
- The 100 m surface is a conditional VIIRS-guided allocation of tract-level MII and does not represent mobility observed at 100 m.
- The analyses are descriptive and diagnostic; they do not identify causal effects.

## Recognition

The project that originated this chapter, *From Mobility Intensity to Market Infrastructure: A Spatial AI Framework for Recovering Hidden Spatial Regimes and Multiscale Variation*, received third place in the [I-GUIDE Spatial AI Challenge 2025-26](https://i-guide.io/spatial-ai-challenge-2025-26/challenge-winners/).

The project team comprised Rafael Albuquerque, Jéssica Miranda, Vinicius Andrade Brei, and Siqin (Sisi) Wang.

## Related dissertation materials

- The dissertation-level argument and repository map are available in the [root README](../README.md).
- The exposure-conversion framework and systematic review are documented in [`chapter_2_paper_1/`](../chapter_2_paper_1/).
- The empirical study of place-based digital sentiment and localized sales performance is documented in [`chapter_3_paper_2/`](../chapter_3_paper_2/).

## Citation

Please cite the dissertation and Chapter 4 when using the mobility-based market infrastructure framework, MII documentation, localized-regime workflow, or fine-scale allocation procedure. Complete bibliographic information will be added after the dissertation is deposited in the UFRGS institutional repository.
