# Chapter 3 / Paper 2: Consumer Mobility and Localized Sales Performance

## Consumer Mobility and Localized Sales Performance: Place-Based Digital Sentiment and Spatial Heterogeneity in the Mobility-Sales Association

This directory contains the public analytical documentation for Chapter 3 of *Consumer Mobility as Evidence About Local Markets*. The study examines the association between consumer mobility and localized sales performance across census tracts and whether the strength of that association varies with the level and polarity of place-based digital sentiment.

## Research question

> How is consumer mobility associated with localized sales performance across census tracts, and how does the strength of this association vary with the level and polarity of place-based digital sentiment?

## Role in the dissertation

Chapter 3 examines consumer mobility when a direct market outcome is available. It builds on Chapter 2’s conclusion that observed mobility shows where consumers moved and which places they reached, whereas local sales record an outcome attributed to a focal firm or offering within a specified place and period. These forms of evidence can be related empirically, but they are not interchangeable.

The chapter uses place-based digital sentiment to describe the positive or negative valence of geolocated digital discourse associated with a geographic area. The Geolocated Electronic Word-of-Mouth Index (GEWI) combines the valence and logged volume of retained geolocated discourse to measure this signal at the same spatial level as mobility and localized sales performance.

The study does not treat GEWI as a separate theoretical construct, general neighborhood sentiment, or representative consumer opinion. It is an empirical measure of historically accumulated place-based digital sentiment used to examine geographic variation in the mobility-sales association.

## Empirical setting

The integrated analytical sample contains 726 urban census tracts in Brazil for which aggregated consumer mobility, localized sales performance, and directly observed or spatially expanded GEWI values could be aligned.

- Consumer mobility and localized sales performance refer to August 2024.
- Consumer mobility is represented primarily by the number of unique visitors, with total visits, visit frequency, and average dwell time used as complementary measures.
- Localized sales performance is represented by transaction values from a Brazilian manufacturer of electrical materials attributed to census tracts.
- GEWI summarizes retained geolocated digital discourse accumulated between 2010 and July 12, 2023.
- GEWI was calculated directly in 96 census tracts containing at least five retained messages.
- Inverse-distance weighting expanded GEWI coverage to another 630 tracts for the integrated 726-tract analysis.
- The 96 directly observed tracts were retained as a benchmark for sensitivity assessment.
- Census tracts provide a common analytical spatial support but are not treated as natural local-market boundaries.

The digital-discourse records were selected using terms relevant to the electrical-materials context. GEWI consequently represents sector-relevant discourse attached to places rather than firm-specific eWOM or sentiment expressed by the entire population of each tract.

## Analytical workflow

The public workflow is organized into three notebooks that should be read and, when authorized data are available, executed in numerical order.

| Notebook | Analytical role |
|---|---|
| `01_mobility_preprocessing.ipynb` | Documents the preparation, geographic attribution, and aggregation of consumer mobility measures at the census-tract level. |
| `02_gewi_construction.ipynb` | Documents message filtering, sentiment scoring, GEWI construction, polarity decomposition, the minimum-message rule, and spatial coverage expansion. |
| `03_empirical_analysis.ipynb` | Documents sample integration, spatial diagnostics, spatial lag and spatial error specifications, GEWI interactions, polarity-specific estimates, sensitivity analyses, and flexible-model diagnostics. |

## Principal results

Across the spatial specifications reported in the dissertation, consumer mobility was positively associated with localized sales performance, with estimated elasticities ranging from 0.33 to 0.37. In practical terms, census tracts with a 10% higher number of visitors recorded approximately 3.3% to 3.7% higher localized sales performance.

The positive interaction between consumer mobility and GEWI indicated that the estimated mobility-sales association was stronger in tracts with more favorable place-based digital sentiment and weaker in tracts with less favorable sentiment. The polarity-specific estimates were statistically significant in opposite directions: favorable sentiment was associated with amplification of the mobility-sales relationship, while unfavorable sentiment was associated with attenuation.

In the reported coefficient units, the absolute magnitude of the negative interaction was approximately 2.5 times that of the positive interaction. This ratio describes the relative magnitude of the two estimates and is not the result of a separate test of coefficient equality. The polarity-specific evidence is consequently interpreted as a descriptive asymmetric pattern in the reported coefficients.

The direction of the central results remained visible across alternative spatial specifications and in the 96-tract subset where GEWI was calculated directly. Flexible-model analyses provided complementary evidence of heterogeneity and functional form but were not interpreted as causal treatment-effect estimates.

## Directory contents

```text
chapter_3_paper_2/
├── README.md
├── notebooks/
│   ├── 01_mobility_preprocessing.ipynb
│   ├── 02_gewi_construction.ipynb
│   ├── 03_empirical_analysis.ipynb
│   └── PUBLIC_COPY_NOTES.md
├── data_dictionary/
│   ├── README.md
│   ├── data_dictionary_aggregated_visitation_measures.xlsx
│   ├── data_dictionary_place_based_digital_sentiment_gewi.xlsx
│   └── data_dictionary_localized_sales_performance.xlsx
├── data/
│   └── README.md
└── environment/
    ├── README.md
    └── requirements.txt
```

## Data access and confidentiality

The empirical data are not redistributed through this repository. Reproduction of the data-dependent results requires independently authorized access to:

- aggregated mobile-location measures;
- restricted geolocated digital-discourse records or authorized derived GEWI files;
- confidential transaction data;
- census-tract geometries; and
- derived analytical files constructed from these inputs.

These restrictions arise from provider agreements, platform conditions, research-access requirements, and commercial confidentiality. The repository contains no personally identifiable information, individual trajectories, device histories, raw transaction records, or raw geolocated messages.

The data dictionaries and access documentation describe the expected variables, units, aggregation levels, spatial identifiers, and interpretive limits without disclosing restricted observations.

## Reproduction status

The notebooks are provided for analytical transparency and use project-relative paths. Readers can inspect the sequence of transformations, parameter choices, model specifications, sensitivity analyses, and diagnostics, but complete execution requires the restricted inputs documented in [`data/README.md`](data/README.md).

The public notebooks are distributed without embedded data-dependent outputs. They document how the reported evidence was produced from authorized aggregated inputs but do not claim unrestricted end-to-end reproduction.

The environment specification reconstructs the public Python requirements needed to inspect and conditionally execute the workflow. Because an exact lockfile from every stage of the original analysis is unavailable, the documented environment supports computational transparency without claiming bit-for-bit recreation of the original software environment.

## Interpretation boundaries

- Consumer mobility represents aggregated presence and visitation; it does not identify demand, purchasing, or individual visit-to-purchase transitions.
- Localized sales performance records transaction values attributed to a focal manufacturer and census tract; it does not represent total local demand, sales across all firms, or tract-level profitability.
- GEWI represents historically accumulated place-based digital sentiment and does not identify contemporaneous sentiment effects in August 2024.
- The spatially expanded GEWI values increase geographic coverage but do not become directly observed sentiment in the additional 630 tracts.
- The cross-sectional design identifies tract-level associations and does not establish causal effects of mobility or place-based digital sentiment.
- The principal spatial models account for spatial dependence but do not establish behavioral spillovers among individual consumers or firms.
- The polarity-specific coefficients can be compared descriptively, but the study does not report a separate statistical test of equality between their magnitudes.
- Census tracts provide the empirical unit of alignment and do not define natural local-market boundaries.
- The mobile-location records count observed devices visiting the tracts rather than identified purchasers of electrical materials.
- The flexible-model analyses examine heterogeneity, support, prediction, and functional form; they are not interpreted as causal treatment-effect estimators.

## Relationship with the other studies

- The dissertation-level argument and repository map are available in the [root README](../README.md).
- Chapter 2 establishes what existing research supports about consumer mobility and local sales and is documented in [`chapter_2_paper_1/`](../chapter_2_paper_1/).
- Chapter 4 examines how multiple mobility indicators characterize the spatial organization of local market access when direct market outcomes are unavailable and is documented in [`chapter_4_paper_3/`](../chapter_4_paper_3/).

Chapter 3 and Chapter 4 address complementary evidence conditions. Chapter 3 examines mobility in relation to localized sales performance and place-based digital sentiment, while Chapter 4 examines local access without a direct sales outcome. Neither chapter treats mobility as demand, purchasing, profitability, or localized market opportunity.

## Citation

Please cite the dissertation and Chapter 3 when using the GEWI measurement documentation, mobility-processing procedures, spatial-analysis workflow, or polarity-specific results. Complete bibliographic information will be added after the dissertation is deposited in the UFRGS institutional repository.
