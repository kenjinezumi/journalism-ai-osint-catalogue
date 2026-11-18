# Skyfield

`OSINT-C2-38` · **80/100** · overall rank 154 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 51) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 23) |
| **Subcategory** | Astronomical computation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Brandon Rhodes (skyfielders) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/skyfielders/python-skyfield) · [Documentation](https://rhodesmill.org/skyfield/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 80/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | JPL ephemeris files are US government data; TLE satellite element sets come from sources with their own terms (for example Space-Track registration requirements). |
| **Restrictions** | None on the code. Satellite TLE sources may require registration and restrict redistribution — check the source you use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Ephemeris files are a one-off download of tens to hundreds of MB. Negligible compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/skyfielders/python-skyfield/blob/master/LICENSE
- https://github.com/skyfielders/python-skyfield
- https://rhodesmill.org/skyfield/

---

## 1. Purpose

Python astronomy library computing high-precision positions of the Sun, Moon, planets, stars and Earth-orbiting satellites for any time and observer location, using JPL ephemerides and TLE data.

## Journalism / investigative use case

Programmatic verification at scale: check Moon phase and altitude for a hundred claimed timestamps in one pass, or compute whether a specific reconnaissance satellite was overhead at the moment an incident was recorded — a question that recurs in conflict reporting and that cannot be answered by eye.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Satellite-pass computation from TLE data is a distinctive investigative capability: establishing which imaging satellites could have seen an event tells you what imagery might exist and who holds it
- High precision with JPL ephemerides, so results are authoritative rather than approximate — appropriate when a published claim rests on them
- MIT licensed with outstanding documentation (the project's docs are unusually clear about astronomical pitfalls), which materially reduces the risk of misuse
- Pure Python, local, no API keys, so it runs anywhere including an isolated machine

## 5. Cons

- Requires understanding of reference frames, time scales (UTC versus TT versus UT1) and observer geometry; the library is correct but misuse is easy and silent
- TLE data for satellite computation must be obtained separately and goes stale quickly, so a pass computed from old elements can be wrong by kilometres
- No releases on GitHub (latest tag 1.55), so pinning relies on tags or PyPI
- 114 open issues on a single-maintainer project; last push 2026-09-29, so cadence is steady but not brisk

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,809 stars with 114 open issues, no release objects, latest tag 1.55, last push 2026-09-29, MIT licence. The library is widely used in the astronomy and satellite-tracking communities, which is relevant adjacent credibility.

## 7. Assessment

Adopt where astronomical checks need to be systematic rather than one-off — and specifically for the satellite-pass question, which is genuinely useful for knowing what imagery to request or FOIA. For your profile the practical caution is TLE freshness: fetch elements close in time to the event you are analysing, and record which element set you used, because a published claim about satellite coverage computed from stale TLEs is indefensible.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-29, no release objects, latest tag 1.55, 1,809 stars, 114 open issues. Six weeks since last push on a mature single-maintainer library with steady long-term development; stable rather than declining.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** JPL ephemeris files are US government data; TLE satellite element sets come from sources with their own terms (for example Space-Track registration requirements).

**Restrictions:** None on the code. Satellite TLE sources may require registration and restrict redistribution — check the source you use.

**Licence evidence:** https://github.com/skyfielders/python-skyfield/blob/master/LICENSE

## 10. Costs

No fee. Ephemeris files are a one-off download of tens to hundreds of MB. Negligible compute.

## 11. Privacy and data flows

Local computation; the only network activity is fetching ephemeris or TLE data, which discloses nothing about your case.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Stellarium](OSINT-C2-37.md) for visual rather than computational verification
- [SunCalc](OSINT-C2-18.md) or suncalc-py for simple solar geometry
- Space-Track or CelesTrak directly for satellite element sets

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/skyfielders/python-skyfield
- https://rhodesmill.org/skyfield/
- https://github.com/skyfielders/python-skyfield/blob/master/LICENSE

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

← 153. [Sherloq](OSINT-C2-12.md) · 155. [urlwatch](SUR-B1-16.md) →
