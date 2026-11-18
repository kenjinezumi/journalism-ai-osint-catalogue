# SunCalc

`OSINT-C2-18` · **84/100** · overall rank 112 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 34) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 16) |
| **Subcategory** | Solar position computation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Vladimir Agafonkin (mourner) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mourner/suncalc) · [Documentation](https://github.com/mourner/suncalc#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, no dependencies, no infrastructure.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/mourner/suncalc/blob/master/LICENSE
- https://github.com/mourner/suncalc

---

## 1. Purpose

Tiny JavaScript library computing sun and moon position, sunrise/sunset and twilight phases, and lunar illumination for a given date and location.

## Journalism / investigative use case

The primitive behind shadow and lighting verification: given a claimed location and timestamp, compute where the sun should have been and check whether shadow direction, length and light quality in the photo agree — a cheap, strong consistency test that can contradict a claimed time or place.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Deterministic astronomical computation, so the result is a physical fact rather than an estimate — the strongest epistemic footing available in image verification
- Extremely small and dependency-free, trivially embeddable in a newsroom verification tool or a browser-side check
- BSD-2-Clause, actively released (v2.1.4 on 2026-11-10, same-day push) with a large user base (3,514 stars) and a tiny backlog (10 open issues)
- Pure computation with no network calls, so it is safe to run client-side on sensitive cases

## 5. Cons

- It computes astronomy, not verification: it cannot tell you anything about the image, and all the interpretive work remains yours
- A 'mismatch' is a probabilistic indication that may reflect a wrong coordinate, a wrong timezone assumption, terrain shadowing or an obstruction rather than a false claim — timezone errors in particular are the classic self-inflicted wound
- JavaScript-first, so a Python pipeline needs suncalc-py or an equivalent port
- Does not handle atmospheric refraction edge cases or complex terrain, so near-horizon calculations need care

## 6. Feedback (documented)

No individual user reports verified. Documented: 3,514 stars with 10 open issues, release v2.1.4 on 2026-11-10 with same-day push, BSD-2-Clause. Widely used as the computation layer in geolocation tooling, including ShadowFinder's dependency on suncalc.

## 7. Assessment

Integrate it as the computational core of any lighting or shadow verification you build — and the reason to use it rather than reimplementing is simply that solar-position maths is easy to get subtly wrong. For your profile the practical warning is timezone handling: most false 'inconsistencies' in shadow analysis come from a wrong UTC offset or an unaccounted daylight-saving change, so make the timezone explicit and record it in the methodology note.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-10, latest release v2.1.4 published the same day, 3,514 stars, 10 open issues. Recent release on a long-stable library from a well-known maintainer; minimal backlog.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/mourner/suncalc/blob/master/LICENSE

## 10. Costs

No fee, no dependencies, no infrastructure.

## 11. Privacy and data flows

Pure computation with no network calls; safe to run client-side on sensitive cases.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [suncalc-py](OSINT-C2-39.md) for a Python port of the same calculations
- [Skyfield](OSINT-C2-38.md) for higher-precision astronomy including star and planet positions
- [ShadowFinder](OSINT-C2-17.md), which wraps this computation into an investigative workflow

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/mourner/suncalc
- https://github.com/mourner/suncalc/blob/master/LICENSE

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

← 111. [Paperless-ngx](JAI-A2-38.md) · 113. [Apache Solr](JAI-A2-01.md) →
