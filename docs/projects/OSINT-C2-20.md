# GDAL

`OSINT-C2-20` · **86/100** · overall rank 72 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 21) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 8) |
| **Subcategory** | Geospatial data translation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | OSGeo / GDAL contributors |
| **Maintenance** | Actively maintained |
| **Licence** | Aggregate — LICENSE.TXT (read 2026-11-17) collects the licences applying across the tree: an MIT-licensed core plus many component licences. GitHub reports NOASSERTION |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/OSGeo/gdal) · [Documentation](https://gdal.org/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 86/100**

---

## 1. Purpose

Translator library and command-line suite for raster and vector geospatial formats, with reprojection, warping, mosaicking, clipping and format conversion across several hundred drivers.

## Journalism / investigative use case

The plumbing under every spatial pipeline: convert a government shapefile to GeoJSON for the web, reproject a leaked dataset into a measurable coordinate system, clip a 40GB satellite scene to the area of interest, or mosaic tiles into a single image for before-and-after comparison.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Format coverage no alternative matches, including the awkward national and legacy formats that government data arrives in — the practical reason it is unavoidable
- Command-line tools (gdalwarp, gdal_translate, ogr2ogr) make reprojection and clipping scriptable and reproducible, which is what a defensible methodology needs
- Underpins QGIS, geopandas, rasterio and most of the geospatial ecosystem, so learning it pays off across every other tool
- Very actively maintained (v3.13.3, 2026-08-18; pushed 2026-11-17) under OSGeo with a professional release process

## 5. Cons

- Licensing is an aggregate: the LICENSE.TXT read in this survey is a collection of licences covering the tree (MIT-licensed core plus many component licences), so a redistribution review means reading the file rather than trusting a single SPDX label — GitHub reports NOASSERTION for exactly this reason
- Command-line ergonomics are notoriously unfriendly: flag semantics are inconsistent across tools and error messages are cryptic
- 603 open issues and a very large driver surface, so obscure format bugs are a real possibility
- Easy to produce silently wrong output — a reprojection with a wrong source CRS assumption looks fine and is not

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 6,159 stars with 603 open issues, release v3.13.3 (2026-08-18), pushed 2026-11-17, SPDX NOASSERTION with an aggregate LICENSE.TXT (read and saved in this session's evidence). Its position as the foundation of the geospatial ecosystem is verifiable from the dependency declarations of QGIS, rasterio and geopandas.

## 7. Assessment

Adopt — you will use it whether you choose to or not, since it sits beneath everything else. For your profile the practical advice is to standardise a small set of scripted GDAL invocations (reproject, clip, convert) with explicit CRS arguments and keep them in version control, rather than running ad-hoc commands; that makes spatial preprocessing reproducible. Read LICENSE.TXT once if you ever intend to redistribute a GDAL-bundled product, because the aggregate licensing genuinely requires it.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.13.3 (2026-08-18), 6,159 stars, 603 open issues. Regular versioned releases under OSGeo governance with corporate contributors and a security process.

## 9. Licensing

**Licence:** Aggregate — LICENSE.TXT (read 2026-11-17) collects the licences applying across the tree: an MIT-licensed core plus many component licences. GitHub reports NOASSERTION _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Data you process carries its own licence.

**Restrictions:** Core is MIT-style, but the aggregate file exists because components differ — some drivers depend on libraries with stricter terms. For internal use this is immaterial; for redistributing a bundled binary, read LICENSE.TXT and check which drivers you ship.

**Licence evidence:** https://github.com/OSGeo/gdal/blob/master/LICENSE.TXT

## 10. Costs

No fee. CPU and disk proportional to imagery size — clipping a large scene is I/O-bound. Negligible licensing cost; infrastructure estimate only.

## 11. Privacy and data flows

Local processing with no network calls unless you point it at a remote dataset (GDAL can read over HTTP/S3, in which case the host sees your range requests and therefore your area of interest).

## 12. Verdict

**Adopt**

## 13. Alternatives

- [rasterio](OSINT-C2-22.md) and geopandas for Pythonic access to the same underlying capability
- [QGIS](OSINT-C2-19.md) for interactive rather than scripted work
- DuckDB spatial for SQL-based vector analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/OSGeo/gdal
- https://gdal.org/
- https://github.com/OSGeo/gdal/blob/master/LICENSE.TXT
- `../sources/evidence/leads.md`

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
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 71. [USAspending.gov (custom award data)](SUR-B2-14.md) · 73. [PyMuPDF](JAI-A2-42.md) →
