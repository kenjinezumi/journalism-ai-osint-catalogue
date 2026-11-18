# QGIS

`OSINT-C2-19` · **91/100** · overall rank 29 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 11) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 4) |
| **Subcategory** | Geospatial analysis (desktop) |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | QGIS.org (OSGeo project) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-2.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/qgis/QGIS) · [Documentation](https://docs.qgis.org/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 91/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Data layers you load (satellite imagery, OSM extracts, commercial basemaps) carry their own licences, which is where the real restrictions sit. |
| **Restrictions** | GPL-2.0 on the application; plugins distributed for QGIS generally inherit copyleft expectations. The practical licence risk in GIS work is the DATA — commercial satellite imagery and some national mapping data forbid redistribution of derived products, so check before publishing a map. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Staff effort |
| **Cost conditions** | Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Runs on an analyst workstation; large raster work wants plenty of RAM and SSD. The costs that bite are data: commercial satellite imagery and tasking are priced per scene or per km² by the vendor (not priced here; see Sentinel Hub/Planet entry). Analyst training time is the other real cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/qgis/QGIS/blob/master/COPYING
- https://github.com/qgis/QGIS
- https://docs.qgis.org/

---

## 1. Purpose

Full desktop geographic information system for viewing, editing, analysing and publishing spatial data, with hundreds of processing algorithms and a large plugin ecosystem.

## Journalism / investigative use case

The workbench for any story with a spatial claim: overlay satellite imagery against a conflict incident's coordinates, measure distances and areas from imagery for damage assessment, join a leaked contracts dataset to administrative boundaries, or georeference a scanned historical map to compare land use over decades.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- The only tool here that lets a non-programmer do serious spatial analysis — georeferencing, measurement, raster algebra, buffer and overlay operations — which is the difference between a mapped story and a guessed one
- Georeferencing scanned maps and imagery is a distinctive investigative capability: it turns a photographed or leaked map into something you can measure against satellite data
- Enormous plugin ecosystem including satellite-imagery loaders, OSM downloaders and Sentinel Hub integration, so acquisition and analysis happen in one place
- Actively maintained under OSGeo governance with a long-term-release track (final-3_44_15, 2026-09-25) and daily commits

## 5. Cons

- Steep learning curve and a dense interface: a reporter will need training, and a bad projection choice silently produces wrong distances and areas — the most common and most consequential mistake
- 5,500 open issues (the largest in the catalogue), reflecting both scale and a long accumulated backlog; expect to encounter rough edges in less-used algorithms
- Heavy desktop application, awkward on low-powered machines and unsuitable for scripted pipelines (use GDAL/geopandas for that)
- GPL-2.0 means plugin and derivative distribution carries copyleft obligations — immaterial for internal analysis, relevant if you ship a tool

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 14,853 stars with 5,500 open issues, release final-3_44_15 (2026-09-25), pushed 2026-11-17, GPL-2.0. QGIS is the standard open GIS in both the geospatial and data-journalism communities, reflected in its adoption across OSGeo and in journalism training curricula.

## 7. Assessment

Adopt it as the newsroom's spatial workbench and invest in training one or two analysts properly — the capability-per-trained-analyst is very high, and spatial claims are where investigations get challenged. For your profile the single most valuable discipline to impose is projection hygiene: record the CRS used for every measurement, because an area calculated in Web Mercator at high latitude can be wrong by a factor that would embarrass a published story.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release final-3_44_15 (2026-09-25), 14,853 stars, 5,500 open issues. Daily commits, structured long-term-release and point-release cadence, OSGeo institutional governance with a funded development model. The vast issue count reflects two decades of accumulation at scale, not neglect.

## 9. Licensing

**Licence:** GPL-2.0 _(SPDX verified)_

**Model / data licence:** n/a. Data layers you load (satellite imagery, OSM extracts, commercial basemaps) carry their own licences, which is where the real restrictions sit.

**Restrictions:** GPL-2.0 on the application; plugins distributed for QGIS generally inherit copyleft expectations. The practical licence risk in GIS work is the DATA — commercial satellite imagery and some national mapping data forbid redistribution of derived products, so check before publishing a map.

**Licence evidence:** https://github.com/qgis/QGIS/blob/master/COPYING

## 10. Costs

No software fee. Runs on an analyst workstation; large raster work wants plenty of RAM and SSD. The costs that bite are data: commercial satellite imagery and tasking are priced per scene or per km² by the vendor (not priced here; see Sentinel Hub/Planet entry). Analyst training time is the other real cost.

## 11. Privacy and data flows

Fully local analysis — imagery and datasets stay on your machine. Two things to watch: plugins may call external services, and loading a basemap from a commercial tile provider sends your viewport (hence your area of interest) to that provider. For a sensitive location, use local imagery rather than a live basemap.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [geopandas](OSINT-C2-21.md) plus rasterio for scripted, reproducible analysis
- [GDAL](OSINT-C2-20.md) for command-line raster and vector conversion
- [kepler.gl](JAI-A1-25.md) or QGIS2Web for publishing rather than analysing

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/qgis/QGIS
- https://docs.qgis.org/
- https://github.com/qgis/QGIS/blob/master/COPYING

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 28. [Tails](SUR-B3-19.md) · 30. [ArchiveBox](OSINT-C1-28.md) →
