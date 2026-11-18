# DuckDB spatial extension

`JAI-A1-19` · **85/100** · overall rank 89 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 34) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 8) |
| **Subcategory** | Analytical database |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | DuckDB Labs |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/duckdb/duckdb-spatial) · [Documentation](https://duckdb.org/docs/extensions/spatial) |
| **Also known as** | duckdb-spatial |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Runs in-process; RAM and disk proportional to data. Among the cheapest ways to handle large data. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/duckdb/duckdb-spatial/blob/main/LICENSE
- https://github.com/duckdb/duckdb-spatial
- https://duckdb.org/docs/extensions/spatial

---

## 1. Purpose

Spatial extension for DuckDB providing geometry types, spatial functions, spatial joins and reading of common geospatial formats directly in SQL, inside an embedded analytical database.

## Journalism / investigative use case

SQL over large datasets including geospatial ones, on a laptop: query a multi-gigabyte procurement extract, join it to administrative boundaries, and aggregate by region — the analysis that would otherwise need a PostGIS server or exceed pandas' memory.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Embedded means no server: a multi-gigabyte spatial join runs in a laptop process, which removes the infrastructure barrier that keeps newsrooms away from larger datasets
- Reads Parquet, CSV, GeoJSON and shapefiles directly in SQL, so the ETL step often disappears entirely
- MIT licensed with very active development (pushed 2026-11-12) backed by DuckDB Labs
- SQL is the lingua franca a mixed team can share, and the queries are a reproducible methodology artefact

## 5. Cons

- 133 open issues and a pre-1.0 extension line (tag v0.9.1): the spatial extension is less mature than DuckDB core, and function coverage against PostGIS is incomplete
- No release objects, so pinning means tracking DuckDB versions and extension compatibility, which is a real operational annoyance
- Spatial function semantics differ subtly from PostGIS in places, so a query ported from one to the other may produce different results without erroring
- Embedded model means no concurrent multi-user access, so it is an analysis tool rather than a shared database

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 723 stars with 133 open issues, no release objects, latest tag v0.9.1, pushed 2026-11-12, MIT licence. DuckDB's broader adoption in data journalism is well established; the spatial extension is newer and correspondingly less proven.

## 7. Assessment

Adopt DuckDB generally and use the spatial extension where it covers what you need, verifying results against QGIS or geopandas on a sample before trusting a large spatial join — the maturity gap against PostGIS is real. For your profile the combination that removes most infrastructure from data work is DuckDB plus Parquet plus Datasette for sharing: a few gigabytes of procurement or registry data becomes queryable and publishable without a server.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-12, no release objects, latest tag v0.9.1, 723 stars, 133 open issues. Current commits under DuckDB Labs; the pre-1.0 extension versioning and backlog indicate an area still maturing.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/duckdb/duckdb-spatial/blob/main/LICENSE

## 10. Costs

No fee. Runs in-process; RAM and disk proportional to data. Among the cheapest ways to handle large data. Estimate.

## 11. Privacy and data flows

Entirely local, in-process, no network. Excellent for sensitive datasets on an isolated machine.

## 12. Verdict

**Adopt**

## 13. Alternatives

- PostGIS where spatial function completeness and multi-user access matter
- [geopandas](OSINT-C2-21.md) for Python-native spatial analysis at smaller scale
- [QGIS](OSINT-C2-19.md) for interactive verification of spatial results

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/duckdb/duckdb-spatial
- https://duckdb.org/docs/extensions/spatial
- https://github.com/duckdb/duckdb-spatial/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 88. [Camelot](JAI-A2-06.md) · 90. [Haystack](JAI-A3-05.md) →
