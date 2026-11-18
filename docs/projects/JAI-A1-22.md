# MapLibre GL JS

`JAI-A1-22` · **85/100** · overall rank 92 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 37) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 9) |
| **Subcategory** | Map publishing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | MapLibre organisation |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause (licence blob read 2026-11-17, MapLibre contributors; GitHub reports NOASSERTION) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/maplibre/maplibre-gl-js) · [Documentation](https://maplibre.org/maplibre-gl-js/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause (licence blob read 2026-11-17, MapLibre contributors; GitHub reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Tiles and underlying data carry their own licences and attribution requirements. |
| **Restrictions** | Library permissive — and deliberately so, as the fork exists to escape Mapbox's licence change. Attribution obligations attach to the map data you display. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Tile production and hosting are the costs; PMTiles on static storage is close to free. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/maplibre/maplibre-gl-js/blob/main/LICENSE.txt
- https://github.com/maplibre/maplibre-gl-js
- https://maplibre.org/maplibre-gl-js/docs/
- `../sources/evidence/leads.md`

---

## 1. Purpose

WebGL-based vector-tile map rendering library, the community fork of Mapbox GL JS from before its licence change, supporting styled vector tiles, 3D terrain and smooth continuous zoom.

## Journalism / investigative use case

Publishing maps where the data is large or the styling matters: thousands of incident points with smooth zoom, a custom cartographic style matching your publication's design, or terrain rendering for a conflict-geography explainer.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Vector tiles handle large datasets and arbitrary zoom far better than raster approaches, so a map with tens of thousands of features stays usable
- BSD-3-Clause (licence resolved in this survey; GitHub reports NOASSERTION) — the fork exists precisely because Mapbox moved to a restrictive licence, so this is the licence-safe lineage and that history is worth knowing
- Very actively maintained (v6.19.0 released 2026-11-17, same-day push) with a substantial community (12,111 stars) and genuine multi-organisation governance
- Pairs directly with PMTiles for fully self-hosted vector maps with no tile-server infrastructure

## 5. Cons

- Heavier than Leaflet in both bundle size and GPU requirements, which matters for readers on low-end devices — the opposite trade-off to Leaflet and a real editorial choice
- Styling is powerful and complex: producing a good custom style is a design project, not a configuration tweak
- 296 open issues and a fast major-version cadence, so pinning matters
- Requires vector tiles, so you need a tile-production step (tippecanoe) that raster workflows avoid

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 12,111 stars with 296 open issues, release v6.19.0 published 2026-11-17 with same-day push, SPDX NOASSERTION with the licence resolved to BSD-3-Clause by reading the blob (MapLibre contributors copyright). The project's origin as a community fork after Mapbox's licence change is documented by the organisation.

## 7. Assessment

Adopt it where the map is the story and data volume or styling justifies the weight; choose Leaflet where reach on constrained devices matters more. For your profile the combination worth building once is MapLibre plus tippecanoe plus PMTiles on static storage: it gives you fully self-hosted vector maps with no tile-server to run, no third-party provider seeing your readers, and no licence exposure — which is a durable capability rather than a per-story effort.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v6.19.0 published the same day, 12,111 stars, 296 open issues. Same-day release and commits under multi-organisation community governance.

## 9. Licensing

**Licence:** BSD-3-Clause (licence blob read 2026-11-17, MapLibre contributors; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Tiles and underlying data carry their own licences and attribution requirements.

**Restrictions:** Library permissive — and deliberately so, as the fork exists to escape Mapbox's licence change. Attribution obligations attach to the map data you display.

**Licence evidence:** https://github.com/maplibre/maplibre-gl-js/blob/main/LICENSE.txt

## 10. Costs

No fee. Tile production and hosting are the costs; PMTiles on static storage is close to free. Estimate.

## 11. Privacy and data flows

Client-side rendering; tile requests go to your configured source. Self-hosted PMTiles keeps reader interactions entirely within your infrastructure, which is the privacy-preserving configuration.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Leaflet](JAI-A1-21.md) for lighter maps and better reach on constrained devices
- deck.gl or kepler.gl for heavy data-visualisation layers
- Static map images where interactivity is not needed

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/maplibre/maplibre-gl-js
- https://maplibre.org/maplibre-gl-js/docs/
- https://github.com/maplibre/maplibre-gl-js/blob/main/LICENSE.txt
- `../sources/evidence/leads.md`

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

← 91. [llm (Simon Willison's CLI)](JAI-A3-12.md) · 93. [OSMnx](OSINT-C2-26.md) →
