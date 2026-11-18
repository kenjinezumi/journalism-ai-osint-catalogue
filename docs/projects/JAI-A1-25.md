# kepler.gl

`JAI-A1-25` · **78/100** · overall rank 182 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 73) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 17) |
| **Subcategory** | Geospatial visualisation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | kepler.gl contributors (Uber origin, now Linux Foundation) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/keplergl/kepler.gl) · [Documentation](https://docs.kepler.gl/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Basemap tiles come from a configured provider with its own terms. |
| **Restrictions** | None material for the library. Default basemap configuration may point at a commercial provider requiring a token — check before publishing. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Client-side compute. If the default basemap provider requires a token, those terms and costs apply (not priced here). Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/keplergl/kepler.gl/blob/master/LICENSE
- https://github.com/keplergl/kepler.gl
- https://docs.kepler.gl/

---

## 1. Purpose

Web application and React component for exploratory geospatial visualisation of large datasets, with point, arc, hexbin, heatmap and trip layers, time playback and no-code layer configuration.

## Journalism / investigative use case

Exploring and presenting large location datasets without writing visualisation code: drop a CSV of hundreds of thousands of incidents in, configure a hexbin or time-animated trip layer, and see the pattern — then export the configuration for a published graphic.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- No-code layer configuration lets an analyst explore a large spatial dataset in minutes, which is where patterns are actually found — far faster than scripting candidate visualisations
- Handles hundreds of thousands of points smoothly via deck.gl, well beyond what a Leaflet map manages
- Time playback is directly useful for movement and sequence stories (flight paths, vessel tracks, incident progression)
- MIT licensed with active development (pushed 2026-11-17) and Linux Foundation governance after its Uber origin

## 5. Cons

- Release line is in a long alpha (v3.3.0-alpha.22, 2026-11-16), so there is no current stable release to pin — awkward for production use
- Heavy client-side application: large datasets need a capable machine, and embedding it in a story page adds substantial weight
- Exploratory output is rarely publication-quality as-is; turning a kepler.gl view into a designed graphic is a separate step
- 277 open issues and a governance transition history, so direction is less predictable than a single-maintainer project

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 12,094 stars with 277 open issues, release v3.3.0-alpha.22 (2026-11-16), pushed 2026-11-17, MIT licence. The prolonged alpha release line is visible in the API data and is the main operational caveat.

## 7. Assessment

Adopt it as an exploration tool rather than a publication tool — its value is letting an analyst see a large spatial dataset's structure quickly, which is hard to do any other way. For your profile the sensible workflow is kepler.gl to find the pattern, then a designed MapLibre or static graphic to publish it. Pin a specific alpha build if you embed it anywhere, since there is no stable release to rely on.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.3.0-alpha.22 (2026-11-16), 12,094 stars, 277 open issues. Same-day commits and frequent alpha releases under Linux Foundation governance; activity is clear, release stability is not.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Basemap tiles come from a configured provider with its own terms.

**Restrictions:** None material for the library. Default basemap configuration may point at a commercial provider requiring a token — check before publishing.

**Licence evidence:** https://github.com/keplergl/kepler.gl/blob/master/LICENSE

## 10. Costs

No fee. Client-side compute. If the default basemap provider requires a token, those terms and costs apply (not priced here). Estimate.

## 11. Privacy and data flows

Data can be loaded entirely client-side, so your dataset need not be uploaded anywhere — a genuine advantage over hosted visualisation services. Basemap tile requests go to the configured provider, disclosing viewport.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [QGIS](OSINT-C2-19.md) for analytical rather than visual exploration
- MapLibre with a custom build for publication-quality output
- [Datasette](JAI-A2-09.md) with a mapping plugin for lighter exploration of smaller datasets

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/keplergl/kepler.gl
- https://docs.kepler.gl/
- https://github.com/keplergl/kepler.gl/blob/master/LICENSE

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

← 181. [browsertrix-behaviors](OSINT-C1-34.md) · 183. [OpenDroneMap (ODM)](OSINT-C2-46.md) →
