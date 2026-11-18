# OpenDroneMap (ODM)

`OSINT-C2-46` · **78/100** · overall rank 183 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 60) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 29) |
| **Subcategory** | Photogrammetry |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenDroneMap community |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/OpenDroneMap/ODM) · [Documentation](https://docs.opendronemap.org/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Your imagery is yours; derived models inherit whatever rights attach to the source imagery. |
| **Restrictions** | AGPL-3.0: a modified network service built on ODM must publish source. Internal processing is unaffected. Note that WebODM (the web interface) is separately licensed — check it if you deploy that too. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: a workstation or server with substantial RAM (16-64GB depending on image count) and hours of CPU per dataset; GPU helps some stages. Assumptions: self-hosted, hundreds of images per dataset.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/OpenDroneMap/ODM/blob/master/LICENSE
- https://github.com/OpenDroneMap/ODM
- https://docs.opendronemap.org/

---

## 1. Purpose

Photogrammetry toolkit that turns overlapping aerial or drone images into orthophotos, digital elevation models, point clouds and textured 3D models.

## Journalism / investigative use case

Turn drone footage of a site into a measurable orthophoto or 3D model — for example quantifying the volume of an illegal spoil heap, measuring the footprint of unpermitted construction, or producing a to-scale model of a destroyed building for a reconstruction graphic.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Converts footage into measurements, which transforms drone imagery from illustration into evidence — volumes, areas and heights you can state with a stated accuracy
- Produces standard outputs (GeoTIFF orthophotos, point clouds) that flow into QGIS for further analysis and into graphics for publication
- Actively maintained (v3.6.2, 2026-08-12; pushed 2026-11-13) with a substantial community (6,603 stars) and a well-documented Docker path
- Self-hosted, so sensitive site imagery never leaves your infrastructure — unlike commercial photogrammetry services

## 5. Cons

- AGPL-3.0: offering a modified ODM as a network service triggers source obligations, which matters if you build a processing service for partners
- Requires properly overlapping imagery with good coverage; footage shot as video or without systematic overlap produces poor or failed reconstructions, and this is the usual reason attempts fail
- Computationally heavy — a few hundred images can take hours on a workstation and benefits from substantial RAM; large sets realistically need a server
- Measurement accuracy depends on ground control or good GPS metadata, and reporting a measurement without stating its accuracy basis would be indefensible

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 6,603 stars with 126 open issues, release v3.6.2 (2026-08-12), pushed 2026-11-13, AGPL-3.0. ODM is the standard open photogrammetry pipeline, reflected in its adoption in humanitarian mapping (an adjacent field with similar needs).

## 7. Assessment

Adopt if your work involves drone flights over sites — the measurement capability is a real evidentiary step up from aerial photographs. For your profile two preconditions matter: plan the flight for photogrammetry (systematic overlap, consistent altitude) rather than for pictures, because reconstruction quality is decided at capture; and establish ground control or document the GPS accuracy, since every published measurement needs a stated error basis. Note also the legal dimension — drone flights over sensitive sites carry their own risks independent of this software.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release v3.6.2 (2026-08-12), 6,603 stars, 126 open issues. Regular releases from an established community with a commercial sponsor behind parts of the ecosystem.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Your imagery is yours; derived models inherit whatever rights attach to the source imagery.

**Restrictions:** AGPL-3.0: a modified network service built on ODM must publish source. Internal processing is unaffected. Note that WebODM (the web interface) is separately licensed — check it if you deploy that too.

**Licence evidence:** https://github.com/OpenDroneMap/ODM/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a workstation or server with substantial RAM (16-64GB depending on image count) and hours of CPU per dataset; GPU helps some stages. Assumptions: self-hosted, hundreds of images per dataset.

## 11. Privacy and data flows

Fully local processing, so site imagery stays on your infrastructure — the key advantage over commercial photogrammetry services, which would receive imagery of a site you may be investigating.

## 12. Verdict

**Pilot**

## 13. Alternatives

- Commercial photogrammetry services for speed, accepting imagery disclosure
- [QGIS](OSINT-C2-19.md) georeferencing for simpler 2D measurement from a single aerial image
- Satellite imagery via pystac where resolution suffices and no flight is possible

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/OpenDroneMap/ODM
- https://docs.opendronemap.org/
- https://github.com/OpenDroneMap/ODM/blob/master/LICENSE

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

← 182. [kepler.gl](JAI-A1-25.md) · 184. [Aleph (alephdata, original)](OSINT-C3-02.md) →
