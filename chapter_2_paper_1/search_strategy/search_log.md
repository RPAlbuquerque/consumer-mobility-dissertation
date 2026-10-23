# Search Log

## Search execution

Scopus and Web of Science were searched on May 15, 2026, without a start-date restriction.

In Scopus, the search covered article titles, abstracts, and keywords through the `TITLE-ABS-KEY` field. In Web of Science, the search used the `TS` topic field, with the syntax adapted to the database.

The searches combined three Boolean blocks:

1. consumer mobility and location traces;
2. consumer, market, commercial, or service contexts; and
3. exposure, opportunity, conversion, performance, and related behavioral or commercial outcomes.

Terms within each block were combined with `OR`, while the three blocks were combined with `AND`. The complete database-specific expressions are preserved in [`scopus_query.md`](scopus_query.md) and [`wos_query.md`](wos_query.md).

The search vocabulary was intentionally broader than the final wording of the research question because relevant evidence appears across studies of physical presence, visitation, access, purchasing, spending, competition, sales, and other commercial outcomes. The presence of terms such as *exposure*, *opportunity*, and *conversion* in the original queries documents the search procedure and does not make these terms constructs in the final synthesis.

## Publication and database filters

The exported records were limited to:

- English-language journal articles;
- records indexed by May 15, 2026;
- the Scopus subject areas documented in the Scopus query file; and
- the Web of Science categories documented in the Web of Science query file.

## Identification and export counts

| Stage | Scopus | Web of Science | Total |
|---|---:|---:|---:|
| Records identified before additional database filters | 1,261 | 574 | 1,835 |
| Records exported after database filters | 521 | 290 | 811 |

## Deduplication

The Scopus and Web of Science exports were merged into one bibliographic database. Duplicate records were identified using normalized DOI as the primary key and normalized article title plus publication year as the fallback.

| Deduplication result | Records |
|---|---:|
| Total exported records | 811 |
| DOI-based duplicate matches | 210 |
| Title-year duplicate matches | 2 |
| Total duplicate records removed | 212 |
| Unique records retained for screening | 599 |

## Screening outcome

The 599 unique records were screened according to the criteria and procedure documented in [`../screening_documentation/`](../screening_documentation/).

| Final decision | Records |
|---|---:|
| Articles retained for the integrative synthesis | 86 |
| Records excluded after screening | 513 |
| Total unique records screened | 599 |

The 86 retained articles were read in full and formed the final evidence corpus for coding and integrative synthesis.

## Access restriction

The complete Boolean expressions, search fields, filters, dates, and aggregate record counts are publicly documented in this repository. The raw Scopus and Web of Science exports are commercial database files and are not redistributed.
