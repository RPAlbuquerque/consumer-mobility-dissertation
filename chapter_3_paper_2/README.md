# Chapter 3 / Paper 2: Place-Based Digital Sentiment and the Local Market Conversion Gap

## From Consumer Mobility to Localized Sales Performance: Place-Based Digital Sentiment and the Local Market Conversion Gap

This directory contains the public analytical documentation for Chapter 3 of the dissertation. The study examines why local markets receiving comparable consumer mobility may display different localized sales performance and whether place-based digital sentiment helps characterize this variation.

## Research question

> When local markets receive comparable consumer mobility, does place-based digital sentiment help characterize differences in localized sales performance?

## Role in the dissertation

Paper 2 gives empirical form to the exposure-conversion framework developed in Chapter 2. Consumer mobility indicates where market exposure may occur, place-based digital sentiment represents one informational condition surrounding that exposure, and localized sales performance captures the outcome observed at the local-market level. Variation in the mobility-sales relationship across places constitutes the local market conversion gap.

The design is observational and does not identify an individual transition from a visit to a purchase or a causal effect of digital sentiment on sales. Its contribution is to show whether mobility, place-based digital information, and localized sales are systematically related across spatially differentiated local markets.

## Empirical setting

The main analytical sample contains 726 urban census tracts in Brazil for which aggregated consumer mobility, place-based digital sentiment coverage, and localized sales performance could be evaluated at a common spatial level.

- Consumer mobility and localized sales performance refer to the common August 2024 analytical window.
- GEWI represents historically accumulated geolocated digital discourse rather than contemporaneous monthly sentiment.
- GEWI was directly observed in 96 census tracts meeting the minimum message threshold.
- Spatial interpolation expanded GEWI coverage for the main 726-tract analysis, while the directly observed subset was retained for comparison and sensitivity assessment.
- Census tracts provide analytical spatial support and are not treated as natural local-market boundaries.

## Analytical workflow

The public workflow is organized into three notebooks that should be read and, where authorized data are available, executed in numerical order.

| Notebook | Analytical role |
|---|---|
| `01_mobility_preprocessing.ipynb` | Documents the preparation and aggregation of consumer mobility measures at the census-tract level. |
| `02_gewi_construction.ipynb` | Documents sentiment scoring, message-volume adjustment, GEWI construction, polarity decomposition, and spatial coverage expansion. |
| `03_empirical_analysis.ipynb` | Documents sample integration, spatial diagnostics, spatial lag and spatial error specifications, sensitivity analyses, and flexible-model diagnostics. |

## Directory contents

```text
chapter_3_paper_2/
├── README.md
├── notebooks/
│   ├── 01_mobility_preprocessing.ipynb
│   ├── 02_gewi_construction.ipynb
│   └── 03_empirical_analysis.ipynb
├── data_dictionary/
│   ├── data_dictionary_aggregated_visitation_measures.xlsx
│   ├── data_dictionary_place_based_digital_sentiment_gewi.xlsx
│   └── data_dictionary_localized_sales_performance.xlsx
├── data/
│   └── README.md
└── environment/
    └── requirements.txt
```

## Data access and confidentiality

The empirical data are not redistributed through this repository. Reproduction of the data-dependent results requires authorized access to aggregated mobile-location measures, geolocated digital-discourse records or authorized derived GEWI files, localized transaction data, and census-tract geometries.

These restrictions arise from provider agreements, platform conditions, and commercial confidentiality. The repository contains no personally identifiable information, individual trajectories, device histories, raw transaction records, or raw geolocated messages.

The data dictionaries describe the constructs, variables, units, aggregation levels, and interpretive limits needed to understand the analytical inputs without disclosing restricted observations.

## Reproduction status

The notebooks are provided for analytical transparency and use project-relative paths. A reader can inspect the complete sequence of transformations, specifications, parameters, and diagnostics, while full execution requires the restricted inputs described in `data/README.md`.

The public notebooks should not be interpreted as a claim that the underlying proprietary data are openly reproducible. They document how the reported evidence was produced from the authorized aggregated inputs.

## Interpretation boundaries

- Consumer mobility is treated as an indicator of potential market exposure, not as demand or performance.
- Place-based digital sentiment is treated as a local informational condition, not as conversion itself.
- Localized sales performance is observed at the census-tract level rather than for individual consumers or stores.
- Spatial models account for dependence among neighboring local markets but do not establish behavioral spillovers.
- Flexible machine-learning models serve as diagnostics and are not interpreted as causal treatment-effect estimators.

## Related dissertation materials

- The dissertation-level argument and repository map are available in the [root README](../README.md).
- The exposure-conversion framework and systematic review are documented in [`chapter_2_paper_1/`](../chapter_2_paper_1/).
- The pre-outcome mobility-based market infrastructure study is documented in [`chapter_4_paper_3/`](../chapter_4_paper_3/).

## Citation

Please cite the dissertation and Chapter 3 when using the GEWI measurement documentation, spatial-analysis workflow, or local market conversion-gap framework. Complete bibliographic information will be added after the dissertation is deposited in the UFRGS institutional repository.
