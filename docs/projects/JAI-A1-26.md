# Turf.js

`JAI-A1-26` · **75/100** · overall rank 219 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 88) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 23) |
| **Subcategory** | Geospatial computation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Turf.js contributors |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Turfjs/turf) · [Documentation](https://turfjs.org/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

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
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, negligible resources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Turfjs/turf/blob/master/LICENSE
- https://github.com/Turfjs/turf
- https://turfjs.org/

---

## 1. Purpose

Modular JavaScript and TypeScript library of geospatial operations — measurement, buffering, intersection, point-in-polygon, clustering, transformation — working on GeoJSON in the browser or Node.

## Journalism / investigative use case

Spatial computation in a published graphic or a JavaScript pipeline: compute which administrative district each incident falls in, buffer a pipeline route to show affected settlements, or calculate distances for an interactive the reader manipulates.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Modular packages mean you import only the operations you need, keeping published graphics light — important for interactive stories on constrained connections
- Working directly on GeoJSON matches the format newsroom spatial data actually arrives in, so there is no conversion step
- MIT licensed with active maintenance (v7.4.0, 2026-08-03; pushed 2026-11-11) and a large community (10,550 stars)
- Lets spatial logic live in the browser, so a reader-facing interactive can compute rather than only display

## 5. Cons

- Planar and spherical operation semantics differ across functions, and using the wrong one produces subtly wrong distances or areas — the same projection hazard as in any spatial work, surfaced differently
- Performance degrades on large feature collections, so it is for computation over modest datasets, not corpus-scale spatial analysis (use geopandas or DuckDB spatial for that)
- 302 open issues and a non-semantic release tag alongside the version, so pinning needs attention
- JavaScript-only, so it does not help a Python analysis pipeline

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 10,550 stars with 302 open issues, release v7.4.0 (2026-08-03), pushed 2026-11-11, MIT licence. Widely used in web mapping, which is well established in the ecosystem.

## 7. Assessment

Integrate it where spatial computation belongs in the browser or a Node pipeline — chiefly for interactives where the reader's input drives a calculation. For your profile the caution is the same as for all spatial work: be explicit about whether you are computing on a plane or a sphere, and verify a sample of results against geopandas or QGIS before a computed figure is published. For analysis rather than presentation, use the Python stack.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-11, latest release v7.4.0 (2026-08-03), 10,550 stars, 302 open issues. Current commits with a 7.x release line from a community team.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/Turfjs/turf/blob/master/LICENSE

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Client-side or local computation with no network calls — data need not leave the browser.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [geopandas](OSINT-C2-21.md) or DuckDB spatial for server-side and larger-scale computation
- PostGIS for spatial SQL at scale
- Shapely for Python-native geometry operations

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Turfjs/turf
- https://turfjs.org/
- https://github.com/Turfjs/turf/blob/master/LICENSE

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
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 218. [HTTrack](OSINT-C1-18.md) · 220. [warn-scraper](JAI-A1-30.md) →
