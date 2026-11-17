# tippecanoe

`JAI-A1-23` · **77/100** · overall rank 195 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 81) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 19) |
| **Subcategory** | Map publishing |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Felt (transferred from Mapbox) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/felt/tippecanoe) · [Documentation](https://github.com/felt/tippecanoe#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

---

## 1. Purpose

Command-line tool that builds vector tilesets from large GeoJSON collections, with zoom-dependent feature selection, simplification and attribute handling to keep tiles small.

## Journalism / investigative use case

Turning a large geospatial dataset into publishable map tiles: a million property parcels, every incident in a conflict dataset, all procurement locations in a country — tiled so a reader's browser loads only what is in view.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Handles very large feature collections and makes sensible zoom-dependent decisions automatically, which is the hard part of vector-tile production
- BSD-2-Clause with active maintenance (pushed 2026-11-16) under Felt's stewardship after the transfer from Mapbox
- Produces output consumable by MapLibre and PMTiles, completing a fully self-hosted map pipeline
- Deterministic CLI, so tile production is a reproducible build step rather than a manual process

## 5. Cons

- Release cadence has lapsed: release 2.79.0 dates from 2025-07-24 with a non-semantic tag since, so pinning is awkward
- The flag surface is large and the defaults are not always what you want for a given dataset — producing good tiles takes iteration and reading the documentation carefully
- C++ build or a package install, which is an extra toolchain in an otherwise JavaScript or Python workflow
- 173 open issues; feature-dropping decisions at low zoom can silently omit data in ways that misrepresent a dataset if you do not check the output

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,637 stars with 173 open issues, release 2.79.0 (2025-07-24), pushed 2026-11-16, BSD-2-Clause. The transfer from Mapbox to Felt is reflected in the repository ownership.

## 7. Assessment

Adopt it as the tile-production step in a self-hosted map pipeline. For your profile the quality check that matters is inspecting the tiles at low zoom: tippecanoe drops features to keep tiles small, and a map that silently omits a third of the incidents at country zoom is editorially wrong even though it looks fine. Set the feature-dropping behaviour deliberately and verify counts at each zoom level before publishing.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 2.79.0 (2025-07-24), 1,637 stars, 173 open issues. Current commits under Felt's maintenance with a lapsed release cadence; active but with poor release hygiene.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** n/a. Tiled data carries its source licence and attribution obligations.

**Restrictions:** None material.

**Licence evidence:** https://github.com/felt/tippecanoe/blob/main/LICENSE.md

## 10. Costs

No fee. CPU and disk for tile generation — a large dataset is minutes to hours and gigabytes of output. Estimate.

## 11. Privacy and data flows

Entirely local tile generation; no network calls.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [PMTiles](JAI-A1-24.md)' own tooling for simpler conversions
- Planetiler for OpenStreetMap-scale basemap generation
- A hosted tile service, accepting the third-party dependency and reader-privacy cost

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/felt/tippecanoe
- https://github.com/felt/tippecanoe/blob/main/LICENSE.md

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

← 194. [Subtitle Edit](JAI-A2-50.md) · 196. [Amnesty International investigations (indicators of compromise)](SUR-B3-11.md) →
