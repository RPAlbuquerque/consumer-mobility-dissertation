# Search Log

## Review databases and date

Scopus and Web of Science were searched on May 15, 2026. The searches combined three concept blocks: mobility and location traces; consumer, marketing, or commercial contexts; and terms broad enough to retrieve evidence on exposure, opportunity, conversion, sales, performance, spending, and place-based heterogeneity.

The Boolean expressions documented in `scopus_query.md` and `wos_query.md` reproduce the search syntax used in each database. Terms within each block were combined with `OR`, and the three blocks were combined with `AND`.

## Identification and export counts

| Stage | Scopus | Web of Science | Total |
|---|---:|---:|---:|
| Records identified before additional database filters | 1,261 | 574 | 1,835 |
| Records exported after database filters | 521 | 290 | 811 |

## Deduplication

The two exports were merged into one bibliographic database. Duplicate records were identified using normalized DOI as the primary key and exact normalized title combined with publication year as the fallback key.

| Deduplication result | Records |
|---|---:|
| Total exported records | 811 |
| DOI-based duplicate matches | 210 |
| Title-year duplicate matches | 2 |
| Total duplicates removed | 212 |
| Unique records retained for screening | 599 |

## Screening outcome

The 599 unique records were screened against the eligibility criteria documented in `../screening_documentation/`.

| Decision | Records |
|---|---:|
| Included in the final integrative synthesis | 86 |
| Excluded after screening | 513 |
| Total screened | 599 |

The 86 retained articles formed the final corpus for coding and integrative synthesis.

Raw commercial database exports are not redistributed through this repository.
