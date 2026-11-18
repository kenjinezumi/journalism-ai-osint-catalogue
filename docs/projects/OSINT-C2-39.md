# suncalc-py

`OSINT-C2-39` · **72/100** · overall rank 258 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 90) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 35) |
| **Subcategory** | Solar position computation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Kyle Barron |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/kylebarron/suncalc-py) · [Documentation](https://github.com/kylebarron/suncalc-py#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, negligible resources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/kylebarron/suncalc-py/blob/master/LICENSE
- https://github.com/kylebarron/suncalc-py

---

## 1. Purpose

Python port of suncalc.js computing sun position, sunrise and sunset times and twilight phases, with vectorised operation over arrays of times and locations.

## Journalism / investigative use case

Batch solar-geometry checks inside a Python pipeline: given a table of claimed locations and timestamps from social posts or testimony, compute the expected sun azimuth and elevation for each and flag the ones inconsistent with the lighting in the attached imagery.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Vectorised over arrays, so checking thousands of claimed location-time pairs is a single operation — the capability that makes systematic consistency screening possible
- Faithful port of a well-tested JavaScript library, so results are comparable with suncalc-based tools including ShadowFinder
- MIT licensed, tiny dependency surface, local computation only
- Still maintained (pushed 2026-11-02) for a small utility library

## 5. Cons

- No release objects (latest tag v0.1.3), and the pre-1.0 version number signals a small project you should pin by commit
- Thin wrapper over simple astronomy: for higher precision or satellite work, Skyfield is the correct tool
- Same interpretive caveat as all solar geometry: a mismatch may reflect terrain shadowing, obstruction or a wrong time-zone assumption rather than a false claim
- Tiny community (69 stars, 15 open issues) with little documentation beyond the README

## 6. Feedback (documented)

No individual user reports verified — 69 stars means minimal community signal. Documented: no releases, latest tag v0.1.3, last push 2026-11-02, MIT, 15 open issues.

## 7. Assessment

Integrate it specifically for batch screening, which is where it beats both SunCalc (JavaScript) and ShadowFinder (one case at a time). For your profile the valuable application is triage over a large collection of geotagged or location-claimed posts: compute expected sun position for each, and surface the handful whose lighting is implausible for manual review. Keep Skyfield available for anything where precision matters.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-02, no releases, latest tag v0.1.3, 69 stars, 15 open issues. Recent commits on a small utility; feature-complete for its scope.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/kylebarron/suncalc-py/blob/master/LICENSE

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Local computation, no network calls.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Skyfield](OSINT-C2-38.md) for higher precision and satellite computation
- [SunCalc](OSINT-C2-18.md) (JavaScript) for browser-side checks
- [ShadowFinder](OSINT-C2-17.md) for the full shadow-geometry workflow on a single case

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/kylebarron/suncalc-py
- https://github.com/kylebarron/suncalc-py/blob/master/LICENSE

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

← 257. [sumy](JAI-A2-51.md) · 259. [kuroi](JAI-A4-24.md) →
