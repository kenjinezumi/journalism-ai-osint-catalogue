# geopandas

`OSINT-C2-21` · **94/100** · overall rank 11 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 7) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 2) |
| **Subcategory** | Geospatial analysis (Python) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | GeoPandas developers |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/geopandas/geopandas) · [Documentation](https://geopandas.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 94/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Datasets carry their own licences. |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU and RAM proportional to dataset size; memory is the binding constraint on large joins. Negligible infrastructure for typical newsroom datasets.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/geopandas/geopandas/blob/main/LICENSE.txt
- https://github.com/geopandas/geopandas
- https://geopandas.org/

---

## 1. Purpose

Python library extending pandas with geometry columns, providing spatial joins, overlays, buffering, dissolving, reprojection and plotting over vector data.

## Journalism / investigative use case

The scripted counterpart to QGIS for reproducible spatial analysis: join a leaked list of addresses to electoral boundaries to show which districts a scheme benefited, count incidents within a radius of military installations, or dissolve parcel data by owner to reveal concentrated land holdings.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Reproducibility is the decisive advantage over desktop GIS: a notebook documenting every spatial operation can be rerun, reviewed and published as methodology, which a sequence of QGIS clicks cannot
- Familiar pandas idioms mean a data journalist already comfortable with dataframes can do spatial joins without learning GIS software
- BSD-3-Clause with active maintenance (v1.2.0, 2026-09-28) and a 1.x stable API after a long pre-1.0 period
- Integrates with the whole Python data stack, so spatial results flow directly into charts, tables and further analysis

## 5. Cons

- Spatial joins on large datasets are memory-hungry and slow compared with a spatial database — above a few million geometries you want PostGIS or DuckDB spatial
- 437 open issues and a dependency chain (shapely, pyproj, GDAL bindings) that is a frequent source of installation pain, especially on Windows
- Reprojection correctness is the user's responsibility: geopandas will happily compute a wrong area if you forget to project out of degrees, and it is the single most common error in published spatial journalism
- No visualisation beyond basic matplotlib plots, so publication-quality maps need another tool

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 5,301 stars with 437 open issues, release v1.2.0 (2026-09-28), pushed 2026-11-14, BSD-3-Clause. Widely used in data journalism, reflected in its prominence in the field's teaching materials.

## 7. Assessment

Adopt as the default for any spatial analysis that will inform a published claim, precisely because the notebook is the methodology. For your profile I would pair it with one habit: assert the CRS explicitly at the top of every analysis and compute areas and distances only in a projected CRS appropriate to the region. That single discipline prevents the most common category of spatial error in journalism.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v1.2.0 (2026-09-28), 5,301 stars, 437 open issues. Regular releases on a stable 1.x line with a broad contributor base and NumFOCUS-adjacent governance.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** n/a. Datasets carry their own licences.

**Restrictions:** None material.

**Licence evidence:** https://github.com/geopandas/geopandas/blob/main/LICENSE.txt

## 10. Costs

No fee. CPU and RAM proportional to dataset size; memory is the binding constraint on large joins. Negligible infrastructure for typical newsroom datasets.

## 11. Privacy and data flows

Local processing. Note that some convenience functions can download basemaps or example datasets from external hosts — review before use on an isolated machine.

## 12. Verdict

**Adopt**

## 13. Alternatives

- DuckDB spatial or PostGIS for datasets too large for memory
- [QGIS](OSINT-C2-19.md) for interactive exploration and georeferencing
- [rasterio](OSINT-C2-22.md) for raster rather than vector analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/geopandas/geopandas
- https://geopandas.org/
- https://github.com/geopandas/geopandas/blob/main/LICENSE.txt

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 10. [FreshRSS](JAI-A1-03.md) · 12. [mat2](SUR-B3-07.md) →
