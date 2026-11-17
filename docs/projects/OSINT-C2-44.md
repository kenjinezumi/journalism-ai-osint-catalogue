# PySTAC

`OSINT-C2-44` · **83/100** · overall rank 119 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 37) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 18) |
| **Subcategory** | Satellite imagery catalogues |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | stac-utils |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (licence blob read 2026-11-17; GitHub reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/stac-utils/pystac) · [Documentation](https://pystac.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 83/100**

---

## 1. Purpose

Python library for reading, writing and querying SpatioTemporal Asset Catalogs (STAC), the standard for describing and searching geospatial imagery collections.

## Journalism / investigative use case

The free route to satellite imagery: search public STAC catalogues (Copernicus, Landsat, Planetary Computer) for every scene covering a location in a date window, then fetch only the bands and area you need — all with no vendor account and no cost.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Opens access to large volumes of openly licensed imagery (Sentinel-1/2, Landsat) at zero cost, which covers a majority of practical before-and-after investigative needs
- STAC is now the de facto standard, so one library works across Copernicus, Planetary Computer, USGS and others rather than learning several APIs
- Apache-2.0 (licence resolved in this session; GitHub reports NOASSERTION) with very active maintenance (pushed 2026-11-16) under community governance
- Cloud-optimised GeoTIFF support means windowed reads of the area of interest only — fast and cheap even over the network

## 5. Cons

- A catalogue client, not an analysis tool: you still need rasterio or GDAL to do anything with the imagery, so it is one component of a pipeline
- Resolution is limited to what open programmes provide (Sentinel-2 at 10m, Landsat at 30m), which is insufficient for identifying vehicles, individuals or small structures — commercial imagery remains necessary for those
- Release and tag naming is confusing (per-extension release objects alongside a v1.16.0 tag), so pinning takes attention
- 68 open issues and a spread of related repositories (pystac-client, stac-utils tooling) that you need to navigate to assemble a workflow

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 470 stars with 68 open issues, pushed 2026-11-16, licence resolved to Apache-2.0 by reading the blob (GitHub reports NOASSERTION). STAC's adoption by Copernicus, USGS and Microsoft Planetary Computer is the relevant evidence of its standard status.

## 7. Assessment

Adopt as your default satellite-imagery access path, with commercial imagery reserved for cases where 10m resolution genuinely will not answer the question. For your profile this is the cost-control decision that matters most in satellite work: most deforestation, flooding, construction-footprint and large-scale destruction stories are answerable at Sentinel-2 resolution for free, and only vehicle- or building-level identification needs a paid scene. Pair with pystac-client for search and rasterio for analysis.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, release objects published per-extension (latest pystac-ext-xarray-assets-v1.0.2, 2026-11-04) with a v1.16.0 tag, 470 stars, 68 open issues. Current commits under stac-utils community governance alongside a widely adopted specification.

## 9. Licensing

**Licence:** Apache-2.0 (licence blob read 2026-11-17; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Imagery licences depend entirely on the catalogue: Copernicus Sentinel data is openly licensed with attribution; Landsat is US public domain; commercial catalogues accessed via STAC carry their own restrictive terms.

**Restrictions:** Library permissive. For open programmes the data restrictions are light (attribution), which is the main reason to prefer this path over commercial imagery.

**Licence evidence:** https://github.com/stac-utils/pystac/blob/main/LICENSE

## 10. Costs

No fee for the library and no fee for open imagery. Cost is bandwidth and storage for the scenes or windows you fetch, plus compute for analysis. Estimate: a before-and-after study of one site is gigabytes, not terabytes.

## 11. Privacy and data flows

Searches and range requests go to the catalogue host (Copernicus, Microsoft, USGS), disclosing your area of interest to that host. Less targeted than a commercial tasking request but not private.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [sentinelhub-py](OSINT-C2-43.md) where higher resolution or server-side processing justifies a paid service
- [Microsoft Planetary Computer](OSINT-C2-45.md) for hosted compute next to the data
- Copernicus Dataspace directly for bulk Sentinel downloads

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/stac-utils/pystac
- https://pystac.readthedocs.io/
- https://github.com/stac-utils/pystac/blob/main/LICENSE
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

← 118. [Huginn](JAI-A1-16.md) · 120. [Querido Diário](OSINT-C3-14.md) →
