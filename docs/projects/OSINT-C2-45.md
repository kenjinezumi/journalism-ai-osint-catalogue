# Microsoft Planetary Computer

`OSINT-C2-45` · **60/100** · overall rank 319 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 125) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 46) |
| **Subcategory** | Satellite imagery platform |
| **Type** | platform |
| **Bucket** | `proprietary-service` |
| **Maintainer** | Microsoft |
| **Maintenance** | Uncertain |
| **Licence** | MIT on the public repository (documentation and tracker); the platform itself operates under Microsoft service terms, not verified in this survey |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/microsoft/PlanetaryComputer) · [Documentation](https://planetarycomputer.microsoft.com/docs/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 2/5 · privacy 2/5 · usability 3/5 · licence+cost 4/5 → **weighted 60/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | MIT on the public repository (documentation and tracker); the platform itself operates under Microsoft service terms, not verified in this survey |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Catalogue datasets carry their own licences — predominantly open (Copernicus, USGS, CC-BY) but per-dataset verification is needed before republication. |
| **Restrictions** | The repository licence is immaterial. The operative terms are Microsoft's service terms plus each dataset's licence; neither was verified here. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** Historically free for catalogue access and Hub compute, but current terms and limits were NOT verified in this survey — treat as unknown and confirm before planning work around it. No software fee.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/microsoft/PlanetaryComputer/blob/main/LICENSE
- https://github.com/microsoft/PlanetaryComputer
- https://planetarycomputer.microsoft.com/docs/

> **Unresolved:** the price is not established by these records — this is not a statement that it is free.

---

## 1. Purpose

Hosted platform providing a large STAC-indexed catalogue of open environmental and satellite datasets with co-located compute (Hub notebooks) for analysis next to the data.

## Journalism / investigative use case

Analysing satellite imagery at scale without downloading it: run a multi-year change-detection analysis over a region in a hosted notebook where the data already sits, which is otherwise infeasible on a newsroom connection.

## 2. Audience

engineer

## 3. Project type

platform · bucket `proprietary-service`

## 4. Pros

- Co-located compute removes the bandwidth barrier that makes multi-year, multi-scene analysis impractical locally — a genuine capability difference, not just convenience
- Very large catalogue of open datasets (Sentinel, Landsat, climate, land cover) indexed with STAC, so acquisition and analysis are in one place
- Historically free access to the catalogue and Hub, which makes serious satellite analysis available to newsrooms with no imagery budget
- The STAC API is standards-based, so analysis code is portable to other catalogues if the platform changes

## 5. Cons

- Hosted Microsoft platform: your analysis, areas of interest and notebooks sit on Microsoft infrastructure, which is a custody decision — and for investigations into locations in jurisdictions where Microsoft operates commercially, worth thinking about
- The GitHub repository is an issues-and-documentation tracker, not the platform code: last push 2024-11-19 with a 2023 release and 80 open issues, so the repository tells you little about the platform's health
- Platform continuity and access terms are outside your control, and current access terms and any usage limits were NOT verified in this survey
- Requires comfort with notebook-based geospatial Python; not a tool for an analyst without that background

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the GitHub repository is a tracker (210 stars, 80 open issues, release 2023.1.26 from 2023-01-26, last push 2024-11-19) and not the platform itself, so repository-based maintenance assessment is not meaningful for the service. Current access terms were not verified.

## 7. Assessment

Worth using for the specific case of large-scale, multi-temporal analysis you cannot run locally, treated as a convenience rather than a dependency: keep your analysis code STAC-portable so it can run against Copernicus or elsewhere if access terms change. For your profile the privacy question is the one to settle deliberately — running an investigation's satellite analysis on Microsoft infrastructure discloses the areas and periods of interest, and for a hostile-state subject that may be unacceptable even though the imagery is public.

## 8. Maintenance

**Uncertain** — The public repository is an issue tracker rather than the platform code: GitHub API 2026-11-17 shows pushed_at 2024-11-19, release 2023.1.26 (2023-01-26), 210 stars, 80 open issues. Platform health cannot be assessed from this, and current service terms were not verified in this survey. Classified Uncertain rather than inferring continuity from the vendor's size.

## 9. Licensing

**Licence:** MIT on the public repository (documentation and tracker); the platform itself operates under Microsoft service terms, not verified in this survey _(SPDX verified)_

**Model / data licence:** Catalogue datasets carry their own licences — predominantly open (Copernicus, USGS, CC-BY) but per-dataset verification is needed before republication.

**Restrictions:** The repository licence is immaterial. The operative terms are Microsoft's service terms plus each dataset's licence; neither was verified here.

**Licence evidence:** https://github.com/microsoft/PlanetaryComputer/blob/main/LICENSE

## 10. Costs

Historically free for catalogue access and Hub compute, but current terms and limits were NOT verified in this survey — treat as unknown and confirm before planning work around it. No software fee.

## 11. Privacy and data flows

Hosted: your queries, areas of interest, notebooks and intermediate results sit on Microsoft infrastructure. Appropriate for public-interest environmental analysis, a considered decision for anything adversarial.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Hosted third-party custody of analysis and areas of interest; current access terms unverified

## 13. Alternatives

- pystac plus Copernicus Dataspace for a self-controlled open-imagery path
- [sentinelhub-py](OSINT-C2-43.md) where higher resolution is needed and a quote is obtained
- Local analysis with rasterio where the data volume is manageable

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/microsoft/PlanetaryComputer
- https://planetarycomputer.microsoft.com/docs/

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

← 318. [Kùzu](JAI-A3-18.md) · 320. [gdelt-doc-api](JAI-A1-15.md) →
