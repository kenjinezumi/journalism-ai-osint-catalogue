# Stellarium

`OSINT-C2-37` · **86/100** · overall rank 77 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 23) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 10) |
| **Subcategory** | Night-sky verification |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Stellarium developers |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Stellarium/stellarium) · [Documentation](https://stellarium.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 86/100**

---

## 1. Purpose

Planetarium application that renders a photorealistic sky for any location, date and time, including stars, planets, the Moon's phase and position, satellites and atmospheric effects.

## Journalism / investigative use case

Verifying or falsifying night-time imagery: set the claimed location and timestamp, and check whether the Moon's phase and position, and the visible star field, match what the photograph or video shows. A waxing Moon in a video claimed to be from a night when the Moon was waning is a hard contradiction.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Night-sky geometry is deterministic astronomy, so a mismatch is a strong falsification rather than a probabilistic hint — among the most reliable verification techniques available
- Moon phase and position are visible in a large share of night-time footage and are trivially checkable, making this a high-yield, low-effort test
- Visual output is immediately persuasive to an editor: you can show the rendered sky beside the frame
- Mature, actively released (v26.3, 2026-09-28) with a large community (10,183 stars) and GPL-2.0 licensing

## 5. Cons

- Light pollution, cloud, lens characteristics and exposure all affect what a camera actually records, so an apparent mismatch can be a photographic artefact rather than a false claim — interpretation requires care
- Only applicable to imagery where sky is visible and identifiable, which excludes most footage
- Desktop application with a learning curve around setting location, time zone and field of view correctly; a wrong time-zone entry produces a false contradiction
- 413 open issues and a large feature surface aimed at amateur astronomy rather than forensic use

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 10,183 stars with 413 open issues, release v26.3 (2026-09-28), pushed 2026-11-16, GPL-2.0. Night-sky verification is an established technique in open-source investigation practice, though I verified no specific case through this tool.

## 7. Assessment

Adopt as a standard check on night-time imagery — it costs minutes and can falsify a claim outright. For your profile the discipline that matters is the same one that bedevils shadow analysis: get the time zone and the UTC offset right before concluding anything, and prefer Moon phase (robust) over faint-star fields (sensitive to exposure and light pollution) as the basis of a published contradiction.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v26.3 (2026-09-28), 10,183 stars, 413 open issues. Regular versioned releases over many years from an established community team.

## 9. Licensing

**Licence:** GPL-2.0 _(SPDX verified)_

**Model / data licence:** Bundled star catalogues and satellite TLE data have their own sources and terms; the application fetches updates for some datasets.

**Restrictions:** GPL-2.0 on the application; immaterial for desktop analytical use.

**Licence evidence:** https://github.com/Stellarium/stellarium/blob/master/COPYING

## 10. Costs

No fee. Runs on an analyst workstation. No paid dependencies.

## 11. Privacy and data flows

Local rendering; the location and time you enter stay on your machine. Optional satellite-orbit data updates fetch from external sources, which discloses nothing about your case.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Skyfield](OSINT-C2-38.md) for programmatic computation of the same astronomy inside a pipeline
- [SunCalc](OSINT-C2-18.md) for solar rather than stellar geometry
- [ShadowFinder](OSINT-C2-17.md) for daytime shadow-based chronolocation

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Stellarium/stellarium
- https://stellarium.org/
- https://github.com/Stellarium/stellarium/blob/master/COPYING

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

← 76. [sentence-transformers](JAI-A2-45.md) · 78. [warcio](OSINT-C1-41.md) →
