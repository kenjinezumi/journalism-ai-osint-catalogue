# rasterio

`OSINT-C2-22` · **86/100** · overall rank 75 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 22) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 9) |
| **Subcategory** | Raster and satellite imagery analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Rasterio contributors (originally Mapbox) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause (LICENSE.txt read 2026-11-17, Mapbox copyright; GitHub reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/rasterio/rasterio) · [Documentation](https://rasterio.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 86/100**

---

## 1. Purpose

Pythonic interface to GDAL's raster capabilities, reading and writing geospatial raster datasets as NumPy arrays with windowed reads, reprojection and masking.

## Journalism / investigative use case

The analysis layer for satellite work: compute a vegetation or burn index to show deforestation or fire damage over time, difference two scenes to detect new construction at a military or industrial site, or extract pixel values at incident coordinates to corroborate a claim about ground conditions.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Windowed reads let you work with a small area of a very large scene without loading it all, which is what makes satellite analysis practical on an ordinary machine
- NumPy array interface means band arithmetic (NDVI, NBR, change detection) is a few lines, so the analytical techniques used in environmental and conflict reporting are directly accessible
- BSD-3-Clause (licence read in this session — GitHub reports NOASSERTION) with active maintenance (1.5.2, 2026-09-30)
- Clean, well-documented Pythonic API that avoids GDAL's command-line awkwardness while using the same engine

## 5. Cons

- Depends on GDAL, so installation inherits that complexity — wheels have improved this but environment conflicts remain the common complaint
- Raster analysis is easy to do wrong: cloud masking, scaling factors and band-specific preprocessing all materially affect an index, and an uncorrected result can show change that is not there
- 158 open issues and release-tag hygiene is mixed (latest tag 'rtd-deps-tag' alongside the 1.5.2 release), so pinning needs care
- No visualisation or georeferencing UI — analysis only

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 2,595 stars with 158 open issues, release 1.5.2 (2026-09-30), pushed 2026-11-03, licence resolved to BSD-3-Clause by reading LICENSE.txt (Mapbox copyright) since GitHub reports NOASSERTION.

## 7. Assessment

Adopt for satellite analysis, with a methodological caution that matters more than the tooling: before publishing a change-detection finding, verify that the apparent change is not an artefact of cloud cover, seasonal variation, sensor differences or scaling. For your profile the strongest pattern is to pair rasterio analysis with manual visual confirmation in QGIS on the same scenes — the index tells you where to look, the human confirms what is there.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-03, latest release 1.5.2 (2026-09-30), 2,595 stars, 158 open issues. Regular releases with a broad contributor base; two weeks since last push is normal cadence for a mature library.

## 9. Licensing

**Licence:** BSD-3-Clause (LICENSE.txt read 2026-11-17, Mapbox copyright; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Satellite imagery carries the provider's licence — this is where restrictions actually apply.

**Restrictions:** Code permissive. The material restrictions are on imagery: Sentinel and Landsat are openly licensed, but commercial providers (Planet, Maxar) restrict redistribution of imagery and sometimes of derived products — check before publishing a processed image.

**Licence evidence:** https://github.com/rasterio/rasterio/blob/main/LICENSE.txt

## 10. Costs

No fee. CPU and disk proportional to scene size; satellite scenes are large (hundreds of MB to GB each). The real cost is imagery acquisition where commercial data is needed. Estimate.

## 11. Privacy and data flows

Local processing. If reading remotely (S3, HTTP), the host sees your range requests and therefore your area of interest — relevant when the area itself is sensitive.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [GDAL](OSINT-C2-20.md) command-line tools for one-off conversion and clipping
- [QGIS](OSINT-C2-19.md) for visual analysis and georeferencing
- [sentinelhub-py](OSINT-C2-43.md) or pystac for acquiring the imagery in the first place

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/rasterio/rasterio
- https://rasterio.readthedocs.io/
- https://github.com/rasterio/rasterio/blob/main/LICENSE.txt
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
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |

---

← 74. [Apktool](SUR-B2-05.md) · 76. [sentence-transformers](JAI-A2-45.md) →
