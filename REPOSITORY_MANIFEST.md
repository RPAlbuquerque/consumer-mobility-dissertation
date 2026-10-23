# Repository Manifest

This manifest identifies the public research materials associated with each chapter of *Consumer Mobility as Evidence About Local Markets*. It distinguishes analytical transparency from complete data-dependent reproduction because the empirical chapters use proprietary, confidential, or otherwise restricted inputs that cannot be redistributed through this repository.

## Access categories

- **Public:** the material is stored directly in this repository.
- **Conditional reproduction:** the analytical code and documentation are public, but complete execution requires independently authorized access to the restricted empirical inputs.
- **Not redistributed:** the material is excluded because of licensing, copyright, confidentiality, privacy, or provider restrictions.

## Chapter-level inventory

| Dissertation component | Public materials | Materials not redistributed | Reproduction status |
|---|---|---|---|
| **Chapter 2 / Paper 1** | Database queries, search log, eligibility criteria, screening protocol, PRISMA 2020 counts, aggregate exclusion summary, coding protocol, included-study matrix, and validation script. | Commercial Scopus and Web of Science exports and copyrighted article files. | Public methodological documentation and an auditable inventory of the 86 retained studies. |
| **Chapter 3 / Paper 2** | Mobility-preprocessing notebook, GEWI-construction notebook, empirical-analysis notebook, data dictionaries, data-access documentation, public-copy notes, and environment specification. | Proprietary aggregated mobility data, restricted geolocated digital-discourse records, confidential transaction data, and restricted derived analytical files. | Conditional reproduction with independently authorized access to the required mobility, digital-discourse, and transaction data. |
| **Chapter 4 / Paper 3** | Analytical notebook, documentation for the seven mobility indicators and the Mobility-based Market Access Index (MMAI), VIIRS documentation, analytical parameters, public-copy notes, environment specification, data-access documentation, and selected non-restricted outputs. | Proprietary tract-level mobility inputs, restricted provider files, and derived empirical files whose redistribution is not authorized. | Conditional reproduction with independently authorized access to the mobility data; VIIRS nighttime-light data are publicly obtainable from their official provider. |

## Public file map

| Path | Purpose |
|---|---|
| `chapter_2_paper_1/README.md` | Explains the public materials associated with the systematic-integrative review and their relationship with Chapter 2. |
| `chapter_2_paper_1/search_strategy/` | Documents the Scopus and Web of Science queries, search fields, filters, dates, and exported record counts used to construct the review corpus. |
| `chapter_2_paper_1/screening_documentation/` | Documents the eligibility criteria, screening procedure, PRISMA 2020 counts, and aggregate exclusion records. |
| `chapter_2_paper_1/coding_framework/` | Documents how the retained studies were compared according to the consumers represented, movement observed, commercial outcome, market coverage, period, and research design. |
| `chapter_2_paper_1/included_studies/` | Identifies the 86 retained studies, the main evidence each study represents, and its role in the synthesis. |
| `chapter_2_paper_1/scripts/` | Contains the validation script used to check the included-study files, record counts, identifiers, and expected fields. |
| `chapter_3_paper_2/README.md` | Explains the public materials associated with the analysis of consumer mobility, place-based digital sentiment, and localized sales performance. |
| `chapter_3_paper_2/notebooks/` | Documents mobility preprocessing, GEWI construction, spatial specifications, polarity-specific analyses, flexible-model diagnostics, and robustness procedures. |
| `chapter_3_paper_2/data_dictionary/` | Defines the aggregated mobility, place-based digital sentiment, GEWI, and localized sales-performance fields used or expected by the analytical workflow. |
| `chapter_3_paper_2/data/` | Documents the restricted inputs, expected file structures, and conditions required for authorized execution. |
| `chapter_3_paper_2/environment/` | Provides the Python dependency specification and notes about the reconstructed public computational environment. |
| `chapter_4_paper_3/README.md` | Explains the public materials associated with the analysis of the spatial organization of local market access. |
| `chapter_4_paper_3/notebooks/` | Documents MMAI construction, global and local spatial analyses, exploratory access regimes, sensitivity specifications, nighttime-light comparisons, and aggregate-preserving spatial downscaling. |
| `chapter_4_paper_3/data_dictionary/` | Defines the seven mobility indicators, MMAI variables, spatial identifiers, regime fields, and VIIRS variables used or expected by the analytical workflow. |
| `chapter_4_paper_3/data/` | Documents the restricted mobility inputs, public nighttime-light inputs, expected file structures, and access conditions. |
| `chapter_4_paper_3/environment/` | Provides the Python dependency specification for the Chapter 4 analytical workflow. |
| `chapter_4_paper_3/outputs/` | Provides selected figures and supporting outputs that do not disclose restricted empirical records. |

## Interpretation of historical and legacy terms

The public documentation follows the concepts and terminology used in the final dissertation. Some materials retain historical or computational language when changing it would obscure how the research was conducted.

The original Chapter 2 database queries contain terms such as *exposure*, *opportunity*, and *conversion* because these terms were used to retrieve potentially relevant studies. Their presence in the search syntax documents the review procedure and does not identify them as constructs adopted by the final dissertation.

Some Chapter 4 computational fields retain legacy names such as `mii`, `mii_norm`, and `infrastructure_regime`. These names remain to preserve compatibility with the original code and data structures. In the dissertation and repository documentation, they correspond to the Mobility-based Market Access Index, its rescaled form, and the exploratory mobility-based access regimes; they do not represent a separate market-infrastructure construct.

The historical title of the I-GUIDE Spatial AI Challenge project is also preserved when documenting the origin and recognition of Chapter 4.

## Scope of reproducibility

The public notebooks expose the sequence of analytical procedures, transformations, parameter choices, model specifications, diagnostics, and expected outputs. They are distributed without restricted records or embedded data-dependent outputs and cannot independently reproduce the reported numerical results unless the researcher has authorized access to correctly structured versions of the required inputs.

The repository supports inspection of the analytical logic and conditional reproduction with authorized data access. It does not claim unrestricted end-to-end reproduction of analyses that depend on proprietary, confidential, or licensed data.

## Data-protection principles

No personally identifiable information, individual trajectories, device histories, raw transactions, raw geolocated messages, passwords, credentials, or provider-specific restricted download links are intentionally included. Project-relative placeholders, data dictionaries, and access documentation describe the required inputs without redistributing their contents.

The repository does not grant access to third-party data or override their original terms, licenses, or confidentiality requirements. Any researcher seeking to execute a restricted-data workflow must independently obtain authorization from the relevant provider or rights holder.

## Version control

The materials corresponding to the dissertation submitted for examination will be preserved through the Git tag and GitHub release `v1.0-thesis`. Subsequent corrections, documentation updates, or extensions will be recorded in later releases rather than silently replacing the archived thesis version.
