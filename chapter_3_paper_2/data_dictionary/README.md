# Data Dictionaries for Chapter 3

This directory documents the three empirical layers aligned in Chapter 3: aggregated consumer mobility, place-based digital sentiment, and localized sales performance. The workbooks contain variable names, definitions, units, aggregation levels, analytical roles, and interpretive boundaries; they do not contain empirical observations.

## Dictionary files

| File | Empirical layer | Documentation scope |
|---|---|---|
| `data_dictionary_aggregated_visitation_measures.xlsx` | Consumer mobility | Documents the census-tract mobility measures observed in August 2024, including the number of unique visitors used as the focal measure and the complementary measures of total visits, visit frequency, and average dwell time. |
| `data_dictionary_place_based_digital_sentiment_gewi.xlsx` | Place-based digital sentiment | Documents the restricted source fields used in the geolocated-discourse workflow and the derived tract-level variables used to construct the baseline, positive, and negative GEWI measures, identify directly observed tracts, and distinguish direct from spatially expanded coverage. |
| `data_dictionary_localized_sales_performance.xlsx` | Localized sales performance | Documents the transaction fields and derived tract-level measure used to represent the focal manufacturer’s transaction value attributed to each census tract in August 2024. |

## Relationship among the empirical layers

The three dictionaries document different forms of evidence that are aligned geographically but are not interpreted as equivalent.

- Consumer mobility records aggregated presence and visitation in census tracts.
- GEWI combines the valence and logged volume of retained geolocated digital discourse to measure historically accumulated place-based digital sentiment.
- Localized sales performance records the focal manufacturer’s transaction value attributed to census tracts.

The shared census-tract identifier allows these layers to be integrated in the empirical analysis. This geographic alignment does not show that the observed visitors produced the recorded transactions or that the authors of the retained messages were the consumers represented in the mobility or sales data.

## Temporal coverage

| Empirical layer | Temporal coverage |
|---|---|
| Consumer mobility | August 2024 |
| Place-based digital sentiment | Geolocated discourse accumulated from 2010 through July 12, 2023 |
| Localized sales performance | August 2024 |

GEWI is interpreted as a historical summary of place-based digital sentiment rather than a contemporaneous sentiment measure for August 2024.

## Coverage and observation status

GEWI was calculated directly in 96 census tracts containing at least five retained geolocated messages. Inverse-distance weighting expanded its coverage to 630 additional tracts, producing the integrated sample of 726 tracts.

The dictionaries distinguish:

- values calculated from messages observed within the tract;
- values produced through the spatial coverage-expansion procedure; and
- variables derived after the three empirical layers were aligned.

A spatially expanded GEWI value does not become directly observed place-based digital sentiment.

## Interpretation boundaries

The dictionaries preserve the distinction among construct, empirical measure, source field, derived variable, spatial unit, and outcome.

- Device-based visitation measures do not identify demand, purchasing, or individual consumers.
- GEWI does not represent the opinions of all residents or visitors in a tract.
- The retained discourse is relevant to the electrical-materials setting but does not represent firm-specific evaluations of the focal manufacturer.
- Localized sales performance does not represent market-wide demand, sales across all firms, or tract-level profitability.
- Census tracts provide analytical spatial support and are not treated as natural local-market boundaries.

## Confidentiality

Some source fields documented in the workbooks are restricted or potentially identifying at the record level. Their names are retained only to make the preprocessing and aggregation logic inspectable.

The repository contains no source observations, message texts, usernames, account identifiers, device identifiers, transaction records, customer information, or individual trajectories.
