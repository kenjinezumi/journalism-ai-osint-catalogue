# sentinelhub-py

`OSINT-C2-43` · **70/100** · overall rank 265 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 94) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 38) |
| **Subcategory** | Satellite imagery access |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Sentinel Hub (Planet) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (library) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** — library free (MIT); Sentinel Hub / Planet service pricing NOT publicly listed — quote required (re-verified 2026-11-17) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/sentinel-hub/sentinelhub-py) · [Documentation](https://sentinelhub-py.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 2/5 · usability 4/5 · licence+cost 2/5 → **weighted 70/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (library) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Imagery licences vary by source: Sentinel data is openly licensed under the Copernicus terms; commercial constellations accessed through the service carry restrictive per-scene terms including limits on redistribution of imagery and sometimes of derived products. |
| **Restrictions** | Library is unrestricted. The imagery is where the restrictions are, and they matter for publication: confirm redistribution rights for any commercial scene you intend to publish, including whether you may publish a derived index image. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** — library free (MIT); Sentinel Hub / Planet service pricing NOT publicly listed — quote required (re-verified 2026-11-17) |
| **Additional costs** | **Mandatory paid dependency** — mandatory paid satellite-imagery service for commercial constellations (quote required); self-hosted compute |
| **Cost conditions** | **Mandatory paid dependency**; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Library free. Service: **not publicly listed — quote required** (verified 2026-11-17: sentinel-hub.com/pricing redirects to planet.com/pricing, which rendered no prices). Historical free and research tiers cannot be confirmed. Budget as an unknown pending a vendor quote; do not plan against any figure from secondary sources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/sentinel-hub/sentinelhub-py/blob/master/LICENSE.md
- https://github.com/sentinel-hub/sentinelhub-py
- https://www.sentinel-hub.com/pricing/
- https://www.planet.com/pricing/
- `../sources/evidence/pricing.md`

---

## 1. Purpose

Python library for requesting and processing satellite imagery through Sentinel Hub services, with area-of-interest requests, custom band arithmetic evalscripts and batch processing.

## Journalism / investigative use case

Programmatic acquisition of satellite imagery for a specific place and date range — the step before analysis in any before-and-after story about destruction, construction, deforestation or industrial activity. Server-side band arithmetic means you can request a burn or vegetation index directly rather than downloading whole scenes.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Area-of-interest requests with server-side processing avoid downloading gigabyte scenes, which makes iterative satellite investigation practical on an ordinary connection
- Evalscript support lets you compute indices (NDVI, NBR, false colour) at request time — the analytical techniques used in environmental and conflict reporting, available in one call
- MIT licensed with active maintenance (v3.12.1 released 2026-11-06, same-day push) and a clean tracker (24 open issues)
- Gives access to Sentinel-1 radar as well as optical data, which is decisive for cloudy regions and night-time analysis where optical imagery is useless

## 5. Cons

- MATERIAL COST AND LICENCE UNCERTAINTY: the library is free but the service is not, and pricing could NOT be verified in this session — sentinel-hub.com/pricing redirects to planet.com/pricing, which rendered no prices (re-verified 2026-11-17). Treat satellite access as an unpriced dependency requiring a vendor quote
- Sentinel Hub is now part of Planet, so the previously available free and research tiers cannot be confirmed as still offered — a continuity risk for any workflow built on them
- Your area-of-interest requests go to the vendor, disclosing exactly which locations and dates you are investigating — a serious consideration when the target is a military or industrial site
- Processing-unit accounting is complex, so costs are hard to predict before you start; 916 stars means a modest community

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 916 stars with 24 open issues, release v3.12.1 on 2026-11-06 with same-day push, MIT licence. The pricing-page redirect chain was verified twice (session 1 on 2026-11-16 and again on 2026-11-17), and in both cases no prices were retrievable — recorded in sources/evidence/pricing.md.

## 7. Assessment

Technically the best route to commercial satellite imagery, and the one item in this segment where I cannot give you a cost. Before building anything on it, get a written quote and confirm whether research or non-profit access still exists post-acquisition. For your profile the strategic hedge is to build your analysis on openly licensed Sentinel and Landsat data accessed through pystac or Planetary Computer wherever the story allows, and reserve commercial tasking for cases where nothing else will do — because an unpriced dependency in the middle of an investigation is a planning risk, not just a budget one.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-06, latest release v3.12.1 published the same day, 916 stars, 24 open issues. Current releases under commercial maintenance; the uncertainty is commercial (post-acquisition product direction), not technical.

## 9. Licensing

**Licence:** MIT (library) _(SPDX verified)_

**Model / data licence:** Imagery licences vary by source: Sentinel data is openly licensed under the Copernicus terms; commercial constellations accessed through the service carry restrictive per-scene terms including limits on redistribution of imagery and sometimes of derived products.

**Restrictions:** Library is unrestricted. The imagery is where the restrictions are, and they matter for publication: confirm redistribution rights for any commercial scene you intend to publish, including whether you may publish a derived index image.

**Licence evidence:** https://github.com/sentinel-hub/sentinelhub-py/blob/master/LICENSE.md

## 10. Costs

Library free. Service: **not publicly listed — quote required** (verified 2026-11-17: sentinel-hub.com/pricing redirects to planet.com/pricing, which rendered no prices). Historical free and research tiers cannot be confirmed. Budget as an unknown pending a vendor quote; do not plan against any figure from secondary sources.

## 11. Privacy and data flows

Area-of-interest requests disclose the coordinates and dates you are investigating to the vendor. For sensitive sites this is a real exposure — consider whether openly licensed data retrieved from a public archive (less targeted) is sufficient.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Service pricing not publicly listed — quote required; post-acquisition availability of free/research tiers unconfirmed
- Requests disclose target coordinates and dates to the vendor

## 13. Alternatives

- pystac plus a public STAC catalogue for openly licensed Sentinel/Landsat data at no cost
- [Microsoft Planetary Computer](OSINT-C2-45.md) for free access to a large open-imagery catalogue
- Copernicus Open Access Hub / Dataspace directly for Sentinel data

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/sentinel-hub/sentinelhub-py
- https://www.sentinel-hub.com/pricing/
- https://www.planet.com/pricing/
- `../sources/evidence/pricing.md`

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

← 264. [Hyphe](OSINT-C1-21.md) · 266. [bellingcat/EDGAR](OSINT-C3-16.md) →
