# Public notebook notes

`consumer_mobility_market_access.ipynb` is the repository-facing copy of the analytical notebook used for Chapter 4.

The public copy preserves the analytical sequence, parameters, diagnostics, and figure-generating procedures while making the following repository-specific changes:

- notebook outputs, execution counts, and environment-specific metadata were cleared;
- restricted provider links and hosted-data shortcuts were removed;
- private input locations were replaced with the project-relative paths documented in `../data/README.md`;
- the terminology was aligned with the final chapter, including local market access, the Mobility-based Market Access Index (MMAI), and exploratory mobility-based access regimes;
- legacy computational fields such as `mii`, `mii_norm`, and `infrastructure_regime` were retained only where required for compatibility with the analysis-ready input and existing code;
- challenge-submission framing was removed apart from the bounded recognition statement retained in the chapter documentation;
- the VIIRS comparison was aligned with the final 120,000-tract held-out specification reported in the dissertation; and
- the São Paulo procedure was described as aggregate-preserving spatial downscaling through a dasymetric-inspired conditional allocation because the MMAI is a dimensionless composite rather than an extensive quantity such as population, expenditure, or sales.

No restricted mobility observations, individual trajectories, device histories, credentials, or personally identifiable information are embedded in the notebook. The annual 2024 VIIRS raster must be obtained independently from its official provider.

No empirical result was recomputed during repository packaging. Full execution remains conditional on authorized access to the restricted tract-level mobility input and local acquisition of the VIIRS raster. These adaptations make the analytical workflow inspectable without implying that the restricted data are openly reproducible or that the 100 m surface contains mobility observed at that resolution.
