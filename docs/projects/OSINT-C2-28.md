# Nominatim

`OSINT-C2-28` · **84/100** · overall rank 107 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 32) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 15) |
| **Subcategory** | Geocoding |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenStreetMap / osm-search |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/osm-search/Nominatim) · [Documentation](https://nominatim.org/release-docs/latest/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 84/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Geocoding and reverse-geocoding engine over OpenStreetMap data, resolving place names and addresses to coordinates and vice versa, self-hostable or used via the OSM-operated public service.

## Journalism / investigative use case

Batch-geocode a leaked or scraped dataset of addresses — property registers, company filings, aid-delivery records — so it can be mapped and spatially joined. Reverse geocoding also turns coordinates in image metadata or ADS-B records into readable place names for a story.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Self-hostable, which is the decisive property for batch geocoding: a dataset of addresses sent to a commercial geocoder discloses your entire investigation to that vendor
- GPL-3.0 with active maintenance (v5.3.3, 2026-10-14) and a documented import process, so a regional instance is a realistic project
- Reverse geocoding is as well supported as forward, which matters for turning coordinates into publishable place descriptions
- No API key or quota when self-hosted, so batch work over hundreds of thousands of records is practical

## 5. Cons

- Self-hosting is a real undertaking: a planet import needs terabyte-class disk and many hours; a regional extract is far more manageable but still a day's work
- The OSM public instance has a strict usage policy that forbids heavy batch use, so the convenient path is explicitly not available for the main use case
- Geocoding accuracy depends on OSM address coverage, which is excellent in some countries and poor in others — and silent mismatches (a street name matched in the wrong city) are the dangerous failure mode
- 102 open issues and operational complexity around index tuning and updates

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 4,571 stars with 102 open issues, release v5.3.3 (2026-10-14), pushed 2026-11-16, GPL-3.0. The OSM Foundation's usage policy for the public instance (which restricts bulk geocoding) is documented by the project and is the key operational constraint.

## 7. Assessment

Self-host a regional instance if geocoding is a recurring need — the privacy and quota arguments both point the same way, and a country-level extract is affordable. For your profile the essential quality control is to validate a sample of geocoded results manually and to record match confidence, because a dataset where 8% of addresses resolved to the wrong city will produce a map that looks right and is wrong.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v5.3.3 (2026-10-14), 4,571 stars, 102 open issues. Regular releases on a 5.x line under OSM-adjacent institutional maintenance.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0.

**Restrictions:** GPL-3.0 on the engine. ODbL applies to the data: publishing a geocoded derived database triggers attribution and share-alike obligations. The OSM public instance's usage policy additionally restricts bulk use — a service term, not a licence term.

**Licence evidence:** https://github.com/osm-search/Nominatim/blob/master/COPYING

## 10. Costs

No fee. Self-hosting estimate: a country-sized extract needs roughly tens to low hundreds of GB of disk and a few hours of import on a modest VM; a full planet instance needs terabyte-class storage and substantially more. Assumptions: PostgreSQL/PostGIS backend, regional extract.

## 11. Privacy and data flows

Self-hosting keeps the addresses you geocode entirely private — the main reason to do it, since batch-geocoding an investigation's address list through a commercial API hands over the target list. The public OSM instance sees queries and disallows bulk use.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Public instance forbids bulk geocoding; self-hosting required for the primary use case

## 13. Alternatives

- [Photon](OSINT-C1-20.md) (komoot) for a faster, more typo-tolerant self-hosted geocoder
- [Pelias](OSINT-C2-30.md) for a modular geocoder combining multiple data sources
- Commercial geocoding APIs only for non-sensitive data, accepting the disclosure

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/osm-search/Nominatim
- https://nominatim.org/release-docs/latest/
- https://github.com/osm-search/Nominatim/blob/master/COPYING

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

← 106. [ALEAPP](SUR-B3-16.md) · 108. [VisiData](JAI-A2-57.md) →
