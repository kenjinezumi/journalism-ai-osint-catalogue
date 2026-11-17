# Photon (komoot geocoder)

`OSINT-C2-29` · **85/100** · overall rank 94 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 29) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 14) |
| **Subcategory** | Geocoding |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | komoot |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/komoot/photon) · [Documentation](https://photon.komoot.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## 1. Purpose

Elasticsearch/OpenSearch-based geocoder over OpenStreetMap data, designed for fast typo-tolerant search-as-you-type and reverse geocoding, with prebuilt import dumps available.

## Journalism / investigative use case

Fast, typo-tolerant geocoding of messy address data — the common case with leaked registries, handwritten records and OCR output where addresses are misspelled, abbreviated or partially transcribed and a strict geocoder returns nothing.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Typo tolerance is the practical differentiator over Nominatim for investigative data, which is almost always dirty — an OCR'd address with two character errors still resolves
- Prebuilt import dumps mean you can stand up an instance without running the OSM import yourself, which removes the main operational barrier
- Apache-2.0 (more permissive than Nominatim's GPL-3.0) with active maintenance (1.3.0, 2026-08-07; pushed 2026-11-15)
- Self-hosted, so batch geocoding of sensitive address lists stays internal

## 5. Cons

- Requires Elasticsearch or OpenSearch, adding a stateful service to operate alongside whatever else you run
- Typo tolerance cuts both ways: a fuzzy match to the wrong place looks like a successful geocode, so confidence thresholds and manual validation matter more here than with a strict geocoder
- Address coverage is still bounded by OSM, so countries with thin address data remain difficult regardless of matching quality
- Not distinguished from the unrelated s0md3v/Photon crawler in search results, which causes genuine confusion when researching it; 41 open issues

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,197 stars with 41 open issues, release 1.3.0 (2026-08-07), pushed 2026-11-15, Apache-2.0. The public photon.komoot.io instance exists for light use; komoot operates it as a courtesy, so heavy batch use should be self-hosted.

## 7. Assessment

My preferred self-hosted geocoder for investigative data specifically because the input is usually dirty — and the prebuilt dumps make it the faster of the two to deploy. For your profile pair it with a validation step: record the match score for every geocoded row, review everything below a threshold manually, and never map a dataset without reporting the proportion that failed or matched weakly. That reporting discipline is what makes a geocoded map defensible.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release 1.3.0 (2026-08-07), 3,197 stars, 41 open issues. Regular releases under corporate maintenance (komoot) with a clean tracker.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0; prebuilt import dumps are derived OSM data and carry the same obligations.

**Restrictions:** Code permissive. ODbL applies to the data and to derived databases you publish.

**Licence evidence:** https://github.com/komoot/photon/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a JVM service plus an Elasticsearch/OpenSearch node — one moderate VM for a country-scale index. Prebuilt dumps save the import compute. Assumptions: regional index, self-hosted.

## 11. Privacy and data flows

Self-hosted geocoding keeps your address lists internal. The public komoot instance sees whatever you send it — avoid for investigative data.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Nominatim](OSINT-C2-28.md) for strict matching and the reference OSM geocoder
- [Pelias](OSINT-C2-30.md) where you need to blend OSM with other address sources
- libpostal for address parsing and normalisation before geocoding

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/komoot/photon
- https://photon.komoot.io/
- https://github.com/komoot/photon/blob/master/LICENSE

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

← 93. [OSMnx](OSINT-C2-26.md) · 95. [PMTiles](JAI-A1-24.md) →
