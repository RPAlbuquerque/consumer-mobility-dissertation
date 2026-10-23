# Data dictionary

`data_dictionary_mobility_market_access.xlsx` documents the supplied, preprocessed, and notebook-derived fields used in Chapter 4.

The workbook distinguishes each variable’s source or internal alias, data type, unit, spatial and temporal support, definition, analytical role, and interpretation boundary. It covers the census-tract identifier and geometry, the seven mobility indicators, the retained Mobility-based Market Access Index (MMAI), the rescaled MMAI, the global and local spatial-analysis fields, the exploratory access regimes, the VIIRS variables, and the São Paulo allocation fields.

The legacy implementation names `mii` and `mii_norm` refer to the final MMAI and its rescaled form. They are retained only to preserve compatibility with the public notebook and do not represent a separate Market Infrastructure Index or theoretical construct.

The dictionary also records that the `q1`–`q4` fields represent the four weekly partitions within August 2024, that the equal-weight MMAI was constructed before the notebook’s principal component analysis, and that PCA is used as an internal covariance-alignment check rather than to construct or validate the index.

VIIRS nighttime-light intensity has two distinct roles in the workflow: it provides bounded external context in the national analysis and supplies ancillary within-tract weights for the São Paulo downscaling procedure. The resulting 100 m values are conditional allocations of tract-level MMAI rather than mobility observations or independently estimated cell-level index values.

The workbook documents the expected structure of the restricted analytical input without reproducing empirical observations, provider-restricted information, individual trajectories, device histories, or personally identifiable information.
