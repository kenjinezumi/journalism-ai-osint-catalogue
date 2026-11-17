# titiler

`JAI-A1-27` · **75/100** · overall rank 217 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 87) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 22) |
| **Subcategory** | Raster tile serving |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Development Seed |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/developmentseed/titiler) · [Documentation](https://developmentseed.org/titiler/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Modular FastAPI application for dynamically serving map tiles from cloud-optimised GeoTIFFs and STAC items, with on-the-fly band math, rescaling and colour mapping.

## Journalism / investigative use case

Publishing satellite imagery interactively without pre-rendering tiles: serve a before-and-after pair of Sentinel scenes with a band-math index computed on request, so readers can pan and compare a damaged area themselves rather than looking at two static crops.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Dynamic band math means you can publish an interactive vegetation or burn index without producing a tileset in advance — a materially shorter path from analysis to published graphic
- Works directly against cloud-optimised GeoTIFFs and STAC catalogues, so it plugs into the pystac-based imagery workflow
- MIT licensed with very active maintenance (release 2.4.1 on 2026-11-16, pushed 2026-11-17) and a clean tracker (25 open issues)
- FastAPI-based and modular, so it is straightforward for a Python team to deploy and extend

## 5. Cons

- Dynamic tiling means a running server with compute per request, so a story that goes viral becomes a cost and capacity question — unlike PMTiles' static approach
- Release-object and tag divergence (2.4.1 release against a v0.25.0 tag) makes version tracking confusing
- Requires understanding of raster band semantics and rescaling to produce a correct image, so a misconfigured deployment publishes a misleading picture
- Narrow use case: it serves raster imagery, and most newsroom maps are vector

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,208 stars with 25 open issues, release 2.4.1 (2026-11-16), pushed 2026-11-17, MIT licence. Development Seed is an established geospatial engineering organisation, which is the relevant institutional context.

## 7. Assessment

Integrate it where satellite imagery is the published artefact and interactivity matters — otherwise pre-render static images, which is cheaper and more robust. For your profile the planning point is capacity: a dynamic tile server behind a successful story is a scaling problem you will meet at the worst moment, so put a CDN in front and consider pre-rendering the specific views the story emphasises while leaving the dynamic path for exploration.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 2.4.1 (2026-11-16), 1,208 stars, 25 open issues. Same-day commits and a release within a day of the survey, under an established organisation.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Served imagery carries the provider's licence — commercial scenes often restrict redistribution, which publishing tiles would constitute.

**Restrictions:** Software permissive. The real constraint is imagery rights: publishing tiles of commercial satellite imagery is redistribution and usually requires specific permission.

**Licence evidence:** https://github.com/developmentseed/titiler/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure: a running server with compute per tile request plus egress — the cost scales with readership, unlike static tiles. Put a CDN in front. Estimate.

## 11. Privacy and data flows

Your server serves the tiles, so no third-party provider sees reader requests — but your server does, so reader-request logging is a policy decision.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Publishing commercial satellite imagery as tiles is redistribution and usually needs explicit permission

## 13. Alternatives

- Pre-rendered static images or PMTiles for most published imagery
- [QGIS](OSINT-C2-19.md) exports for a one-off graphic
- A commercial imagery platform's embed, accepting third-party dependency and reader exposure

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/developmentseed/titiler
- https://developmentseed.org/titiler/
- https://github.com/developmentseed/titiler/blob/main/LICENSE

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

← 216. [OutbackCDX](OSINT-C1-44.md) · 218. [HTTrack](OSINT-C1-18.md) →
