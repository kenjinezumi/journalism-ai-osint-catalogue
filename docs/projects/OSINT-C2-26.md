# OSMnx

`OSINT-C2-26` · **85/100** · overall rank 93 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 28) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 13) |
| **Subcategory** | Street network analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Geoff Boeing (gboeing) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/gboeing/osmnx) · [Documentation](https://osmnx.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | OpenStreetMap data is ODbL 1.0. |
| **Restrictions** | None on the code. ODbL attribution and share-alike apply if you publish a derived database of OSM features. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU and RAM for graph analysis; city-scale networks are comfortable on a laptop. Downloading from public Overpass is free but rate-limited. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/gboeing/osmnx/blob/main/LICENSE.txt
- https://github.com/gboeing/osmnx
- https://osmnx.readthedocs.io/

---

## 1. Purpose

Python library that downloads OpenStreetMap street networks and other geospatial features, builds them as NetworkX graphs, and provides routing, centrality, orientation and morphology analysis.

## Journalism / investigative use case

Analyse movement and access questions with a spatial basis: compute how long an ambulance journey actually takes from a neighbourhood to the nearest hospital, test whether a claimed route in a video is physically plausible in the available time, or measure how a new road or checkpoint changes accessibility for a community.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Turns street data into an analysable graph, which lets you make quantitative accessibility claims — a strong, defensible basis for public-interest reporting on health, transport and segregation
- Routing and travel-time analysis provides a physical-plausibility test for claims about movement in videos or testimony, which is a distinctive verification capability
- MIT licensed, exceptionally maintained (pushed 2026-11-17, latest tag v2.1.2) with essentially no open issues (1) against 5,902 stars — the cleanest tracker in this segment
- Excellent documentation with published academic methodology, so the analysis is citable

## 5. Cons

- Analysis quality depends entirely on OSM completeness, which varies enormously by region — in under-mapped areas the network is incomplete and travel-time results will be optimistic
- No release objects on GitHub (tag v2.1.2 only), so pinning relies on tags or PyPI
- Downloading large networks from Overpass is slow and rate-limited; city-scale is fine, country-scale needs a local extract
- Routing uses simple impedance models, so results are a plausibility estimate rather than a traffic simulation — presenting them as actual travel times would overstate them

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 5,902 stars with 1 open issue and same-day commits (2026-11-17), MIT licence. The near-empty issue tracker at this scale is exceptional and the strongest maintenance evidence in this segment. The project has a published academic methodology, which is relevant credibility for citation.

## 7. Assessment

Adopt for any story with an access, distance or movement claim — it gives you numbers you can defend, which is rare in spatial reporting. For your profile the two cautions are: check OSM completeness for your region before trusting travel-time results, and describe outputs as modelled rather than measured times. The plausibility-testing use (could someone have travelled that route in that time?) is an underused verification technique worth building into your workflow.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, no release objects, latest tag v2.1.2, 5,902 stars, 1 open issue. Same-day commits with an essentially empty backlog at substantial scale — outstanding maintenance discipline from a single academic maintainer.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0.

**Restrictions:** None on the code. ODbL attribution and share-alike apply if you publish a derived database of OSM features.

**Licence evidence:** https://github.com/gboeing/osmnx/blob/main/LICENSE.txt

## 10. Costs

No fee. CPU and RAM for graph analysis; city-scale networks are comfortable on a laptop. Downloading from public Overpass is free but rate-limited. Estimate.

## 11. Privacy and data flows

Network downloads go to Overpass (public instance unless configured otherwise), disclosing the areas you are analysing. Analysis itself is local.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Direct Overpass queries plus NetworkX if you want more control
- [QGIS](OSINT-C2-19.md) network analysis tools for interactive work
- Valhalla or OSRM for serious routing with realistic impedances

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/gboeing/osmnx
- https://osmnx.readthedocs.io/
- https://github.com/gboeing/osmnx/blob/main/LICENSE.txt

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |

---

← 92. [MapLibre GL JS](JAI-A1-22.md) · 94. [Photon (komoot geocoder)](OSINT-C2-29.md) →
