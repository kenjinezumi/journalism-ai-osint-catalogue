# Overpass API

`OSINT-C2-23` · **73/100** · overall rank 235 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 80) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 32) |
| **Subcategory** | OpenStreetMap querying |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Roland Olbricht (drolbr) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/drolbr/Overpass-API) · [Documentation](https://dev.overpass-api.de/overpass-doc/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 2/5 · privacy 3/5 · usability 2/5 · licence+cost 4/5 → **weighted 73/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Database engine and query language for OpenStreetMap data, allowing selection of map features by tag, area, proximity and time, served via public instances or self-hosted.

## Journalism / investigative use case

The engine behind feature-based geolocation and infrastructure mapping: find every petrol station within 2km of a coordinate to match a photographed sign, enumerate all military installations tagged in a region, or extract every school in a district to cross-reference against a procurement dataset.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Tag-and-proximity querying is the core technique of feature-based geolocation — 'find places with a church, a water tower and a railway within 500m' is exactly how photographs get located
- Historical (attic) data support lets you query what OSM said at a past date, which is useful for establishing what existed when
- AGPL-3.0 and self-hostable, so a newsroom can run its own instance and keep queries private — a genuine advantage since queries reveal your area of interest
- Underpins overpass-turbo, overpy, OSMPythonTools and bellingcat/osm-search, so the whole OSM investigative toolchain rests on it

## 5. Cons

- Self-hosting is a serious undertaking: a full planet instance needs substantial disk and hours of import time, and most users therefore rely on public instances
- Public instances see your queries, which disclose precisely which locations and feature combinations you are investigating — a real operational-security consideration
- Query language is idiosyncratic and unforgiving; learning it takes real effort and errors often return empty results rather than diagnostics
- Slowing cadence: last push 2026-02-19 with the latest release osm3s_v0.7.62.4 from 2024-11-21, and 224 open issues

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 945 stars with 224 open issues, release osm3s_v0.7.62.4 (2024-11-21), last push 2026-02-19, AGPL-3.0. Its central position in OSM tooling is verifiable from the dependency relationships of overpass-turbo, overpy and bellingcat/osm-search.

## 7. Assessment

Essential capability, and for your profile the question is where you run it. Public instances are free and convenient but disclose your geolocation targets; a self-hosted regional extract (not the full planet) is a realistic middle path that keeps queries private and is far cheaper than a global instance. Given the slowing release cadence, note it as a dependency to watch — the public instances' continuity matters more to you than the repository's.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-02-19, latest release osm3s_v0.7.62.4 (2024-11-21), 945 stars, 224 open issues. Nine months without commits and two years since the last release, on infrastructure the whole OSM query ecosystem depends on. Declining rather than dormant; no deprecation notice and the public instances remain operational.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0 — a share-alike database licence with attribution and, for derived databases, share-alike obligations.

**Restrictions:** AGPL-3.0 on the engine. More importantly, ODbL on the DATA: publishing a derived database (not merely a map image) obliges you to license it under ODbL and attribute OSM. This catches newsrooms that publish extracted datasets without realising.

**Licence evidence:** https://github.com/drolbr/Overpass-API/blob/master/LICENSE

## 10. Costs

No fee. Public instances are free but rate-limited. Self-hosting estimate: a regional extract is feasible on one VM with a few hundred GB of disk; a full planet instance needs terabyte-class storage and a long import. Assumptions: self-hosted regional extract.

## 11. Privacy and data flows

Queries to a public instance disclose your area of interest and the feature combinations you are matching — which in a geolocation investigation is close to disclosing the case. Self-hosting eliminates this and is the reason to consider it.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Public-instance queries disclose geolocation targets; self-hosting is required for private querying

## 13. Alternatives

- bellingcat/osm-search for a journalist-friendly proximity-search interface over the same data
- [overpass-turbo](OSINT-C2-24.md) for interactive query development
- Downloading a regional OSM extract and querying it locally with PostGIS or DuckDB spatial

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/drolbr/Overpass-API
- https://dev.overpass-api.de/overpass-doc/
- https://github.com/drolbr/Overpass-API/blob/master/LICENSE

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

← 234. [wabac.js](OSINT-C1-33.md) · 236. [dedupe](JAI-A2-11.md) →
