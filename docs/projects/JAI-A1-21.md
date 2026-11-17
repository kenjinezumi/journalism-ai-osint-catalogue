# Leaflet

`JAI-A1-21` · **74/100** · overall rank 226 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 91) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 25) |
| **Subcategory** | Map publishing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Volodymyr Agafonkin and contributors |
| **Maintenance** | Stable with low activity |
| **Licence** | BSD-2-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Leaflet/Leaflet) · [Documentation](https://leafletjs.com/reference.html) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 5/5 · licence+cost 5/5 → **weighted 74/100**

---

## 1. Purpose

Lightweight JavaScript library for interactive maps, with tile-layer support, vector overlays, markers, popups and a large plugin ecosystem, designed to work on mobile and in constrained environments.

## Journalism / investigative use case

Publishing an interactive map with a story: incident locations, a procurement geography, a flight path — rendered in the reader's browser with a small library that works on low-end devices and slow connections, which matters for audiences in the regions exile media serve.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Very small and dependency-free, so it loads on poor connections and old devices — a real editorial consideration for audiences outside wealthy markets
- BSD-2-Clause with an enormous ecosystem (45,950 stars) and plugins for clustering, heatmaps and most newsroom needs
- Simple API that a front-end developer learns in an afternoon, so a map is hours of work rather than a project
- Still actively developed (pushed 2026-11-17) with a 2.0 beta line after a long stable period

## 5. Cons

- Release cadence is slow: the stable release v1.9.4 dates from 2023-05-18 with v2.0.0-beta.4 tagged since, so you choose between a three-year-old stable release and a beta
- Raster-tile oriented by design; large vector datasets and smooth zooming are MapLibre's territory, not Leaflet's
- Default tile layers point at third-party providers (OpenStreetMap or commercial), so every reader's map viewport is reported to that provider — a reader-privacy issue most newsrooms never consider
- 219 open issues; plugin quality varies enormously and many popular plugins are unmaintained

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 45,950 stars with 219 open issues, stable release v1.9.4 (2023-05-18), tag v2.0.0-beta.4, pushed 2026-11-17, BSD-2-Clause. The long gap between the stable release and current development is visible in the API data.

## 7. Assessment

Adopt it for most newsroom maps — the loading-weight advantage is decisive when your audience is on constrained connections, and the API is quick enough that maps actually get made. For your profile the under-considered issue is reader privacy: self-host your tiles (PMTiles plus a static host) rather than loading from a third-party provider, because otherwise every reader of a sensitive story reports their map interactions to someone else. Decide deliberately between the stable release and the 2.0 beta.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, stable release v1.9.4 (2023-05-18), tag v2.0.0-beta.4, 45,950 stars, 219 open issues. Current commits on a 2.0 line but no stable release in three years — a mature library in a slow major-version transition.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** n/a. Map tiles carry the tile provider's licence and attribution requirements (OpenStreetMap tiles require ODbL attribution).

**Restrictions:** Library permissive. Attribution obligations attach to the tiles and data you display, which is a real publication requirement rather than a formality.

**Licence evidence:** https://github.com/Leaflet/Leaflet/blob/main/LICENSE

## 10. Costs

No fee. Tile serving is the cost: third-party providers have usage limits and paid tiers (not priced here), while self-hosted PMTiles on static storage is nearly free. Estimate.

## 11. Privacy and data flows

Client-side rendering, but tile requests go to whichever provider you configure, disclosing each reader's map viewport and interaction pattern to that provider. Self-hosting tiles removes this and is the recommended configuration for sensitive stories.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [MapLibre GL JS](JAI-A1-22.md) for vector tiles and smooth zooming at greater weight
- [PMTiles](JAI-A1-24.md) plus tippecanoe to self-host tiles and remove the third-party dependency
- A static image map where interactivity adds nothing

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Leaflet/Leaflet
- https://leafletjs.com/reference.html
- https://github.com/Leaflet/Leaflet/blob/main/LICENSE

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

← 225. [Internet Health Report (IHR)](SUR-B1-13.md) · 227. [OpenTimestamps](OSINT-C3-41.md) →
