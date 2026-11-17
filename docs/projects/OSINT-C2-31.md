# mapillary_tools

`OSINT-C2-31` · **62/100** · overall rank 312 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 122) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 45) |
| **Subcategory** | Street-level imagery |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Mapillary (Meta) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mapillary/mapillary_tools) · [Documentation](https://github.com/mapillary/mapillary_tools#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 2/5 · usability 3/5 · licence+cost 4/5 → **weighted 62/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Command-line tools for processing and uploading street-level imagery to Mapillary, including geotagging from GPS tracks, sequence organisation and metadata handling.

## Journalism / investigative use case

Two uses: processing your own ground-truth imagery (a reporter driving a route with a dashcam) into a geotagged sequence for later reference, and understanding the metadata structure of Mapillary imagery you use for geolocation verification against a photograph.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Mapillary's crowd-sourced street-level imagery is often the only street-view coverage available in countries Google does not photograph — which is precisely where much conflict and corruption reporting happens
- Geotagging from GPS tracks lets a reporter turn a drive-through into a reusable, dated visual record of a location, useful when you cannot return
- BSD-2-Clause and actively maintained (v0.15.0, 2026-11-04; pushed 2026-11-16) with a clean tracker
- Processing happens locally, so you control what is uploaded and when

## 5. Cons

- Uploading contributes your imagery to a Meta-operated platform under its terms — a deliberate disclosure that also reveals where your reporter has been, with timestamps
- The tool is for contributing imagery, not for downloading it, so for geolocation verification you need the Mapillary API or streetlevel instead — a distinction that wastes people's time
- Narrow scope and engineer-facing; a reporter will not use it directly
- Coverage of the platform itself is uneven and contributor-dependent, so the imagery you want may simply not exist

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 320 stars with 33 open issues, release v0.15.0 (2026-11-04), pushed 2026-11-16, BSD-2-Clause. Mapillary's role as a street-level imagery source in regions without commercial coverage is well established in open-source investigation practice.

## 7. Assessment

Relevant mainly if your team does field work and wants to build a reusable visual record — in which case it is the right tool, with one serious caveat: uploading a geotagged sequence publishes where your reporter drove and when, which can endanger them or their sources in a hostile environment. Process locally, review carefully, and treat the upload decision as an editorial and security judgement rather than a technical step. For consuming imagery for geolocation, use streetlevel or the Mapillary API instead.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v0.15.0 (2026-11-04), 320 stars, 33 open issues. Regular releases under corporate maintenance.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** Imagery uploaded to Mapillary is licensed under the platform's terms (historically CC-BY-SA for the imagery database); imagery you consume from Mapillary carries those terms.

**Restrictions:** Code permissive. The imagery licensing is the substantive point: check Mapillary's current terms before republishing imagery from the platform in a story, and understand what rights you grant when uploading.

**Licence evidence:** https://github.com/mapillary/mapillary_tools/blob/main/LICENSE

## 10. Costs

No fee. Negligible compute; bandwidth for uploads. A Mapillary account is required to upload.

## 11. Privacy and data flows

Processing is local; uploading publishes geotagged imagery to a Meta-operated platform, disclosing locations and timestamps of your field movements. This is the dominant consideration for hostile-environment work.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Uploading discloses reporter movements with timestamps to a third-party platform

## 13. Alternatives

- [streetlevel](OSINT-C2-32.md) for downloading panoramas and metadata from Street View, Look Around and Mapillary for verification
- The Mapillary API directly for programmatic imagery access
- Keeping field imagery entirely internal with your own geotagging scripts (ExifTool can write GPS tags)

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/mapillary/mapillary_tools
- https://github.com/mapillary/mapillary_tools/blob/main/LICENSE

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

← 311. [Internet Society Pulse](SUR-B1-14.md) · 313. [OpenOversight](SUR-B2-12.md) →
