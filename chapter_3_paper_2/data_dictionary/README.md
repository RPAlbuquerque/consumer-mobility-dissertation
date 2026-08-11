# Data Dictionaries

This directory documents the three empirical layers used in Chapter 3: aggregated consumer mobility, place-based digital sentiment (GEWI), and localized sales performance. The workbooks contain field definitions and measurement metadata only; they do not contain empirical observations.

| File | Coverage |
|---|---|
| `data_dictionary_aggregated_visitation_measures.xlsx` | Census-tract mobility measures and their temporal aggregation. |
| `data_dictionary_place_based_digital_sentiment_gewi.xlsx` | Source fields used in the restricted discourse workflow and the derived GEWI measurement layer. |
| `data_dictionary_localized_sales_performance.xlsx` | Transaction fields used to construct census-tract localized sales performance. |

Some source fields documented in these workbooks are restricted or potentially identifying at the record level. Their names are retained to make the preprocessing logic auditable, but no record-level values are included in this repository.
