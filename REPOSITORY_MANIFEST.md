# Repository Manifest

This manifest identifies the public research materials associated with each empirical chapter of the dissertation and distinguishes analytical transparency from complete data-dependent reproduction.

## Access categories

- **Public:** the material is stored directly in this repository.
- **Conditional reproduction:** the code and documentation are public, but complete execution requires authorized access to restricted empirical inputs.
- **Not redistributed:** the material is excluded because of licensing, copyright, confidentiality, privacy, or provider restrictions.

## Chapter-level inventory

| Dissertation component | Public materials | Materials not redistributed | Reproduction status |
|---|---|---|---|
| **Chapter 2 / Paper 1** | Search strings, search log, eligibility criteria, screening protocol, PRISMA-informed counts, aggregate exclusion summary, coding framework, included-study matrix, and validation script. | Commercial Scopus and Web of Science exports, database-supplied abstracts, and copyrighted article files. | Public methodological documentation and auditable final corpus. |
| **Chapter 3 / Paper 2** | Mobility-preprocessing notebook, GEWI-construction notebook, empirical-analysis notebook, data dictionaries, data-access documentation, and environment specification. | Proprietary aggregated mobility data, restricted geolocated digital-discourse records, localized transaction data, and restricted derived analytical files. | Conditional reproduction with authorized data access. |
| **Chapter 4 / Paper 3** | Analytical notebook, MII and mobility-variable documentation, VIIRS documentation, parameters, environment specification, data-access documentation, and selected non-restricted outputs. | Proprietary tract-level mobility input, restricted provider files, and derived files whose redistribution is not authorized. | Conditional reproduction with authorized mobility-data access; VIIRS is publicly obtainable from its official provider. |

## Public file map

| Path | Purpose |
|---|---|
| `chapter_2_paper_1/search_strategy/` | Documents database queries, search fields, filters, dates, and exported record counts. |
| `chapter_2_paper_1/screening_documentation/` | Documents eligibility rules, screening procedures, PRISMA-informed counts, and aggregate exclusions. |
| `chapter_2_paper_1/coding_framework/` | Defines the categories used in the integrative synthesis. |
| `chapter_2_paper_1/included_studies/` | Identifies the 86 studies and their contributions to the exposure-conversion synthesis. |
| `chapter_3_paper_2/notebooks/` | Documents mobility preprocessing, GEWI construction, spatial specifications, and diagnostics. |
| `chapter_3_paper_2/data_dictionary/` | Defines the aggregated mobility, GEWI, and localized sales-performance fields. |
| `chapter_4_paper_3/notebooks/` | Documents the mobility-based market infrastructure workflow. |
| `chapter_4_paper_3/data_dictionary/` | Defines the mobility indicators, MII fields, spatial identifiers, and VIIRS variables. |
| `chapter_4_paper_3/outputs/` | Provides selected supporting outputs that do not disclose restricted empirical records. |

## Data-protection principles

No personally identifiable information, individual trajectories, device histories, raw transactions, raw geolocated messages, passwords, credentials, or provider-specific restricted download links are intentionally included. Project-relative placeholders and data dictionaries are used to document restricted inputs without redistributing them.

The repository should not be interpreted as granting access to third-party data or overriding their original terms. Any researcher seeking to execute a restricted-data workflow must obtain authorization independently from the relevant data provider or rights holder.

## Version control

The materials corresponding to the dissertation submitted for examination will be preserved as Git tag and GitHub release `v1.0-thesis`. Later corrections or extensions will be documented in subsequent releases rather than silently replacing the archived thesis version.
