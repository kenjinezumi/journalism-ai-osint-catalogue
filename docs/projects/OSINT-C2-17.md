# ShadowFinder

`OSINT-C2-17` · **91/100** · overall rank 35 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 14) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 5) |
| **Subcategory** | Chronolocation |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/ShadowFinder) · [Documentation](https://github.com/bellingcat/ShadowFinder#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## 1. Purpose

Tool that computes the set of possible locations consistent with an observed shadow length and a known timestamp, or the set of possible times consistent with a shadow at a known location, producing a map of candidate bands.

## Journalism / investigative use case

Classic chronolocation and geolocation: given a photo with a visible shadow and a claimed timestamp, narrow the possible latitudes and longitudes — or run it in reverse to test whether a claimed location and time are physically consistent with the shadow in the image. The reverse test is the stronger journalistic move, because it can falsify a claim outright.

## 2. Audience

specialist investigator, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Grounded in astronomy rather than machine learning, so the result is a deterministic physical constraint rather than a probabilistic guess — qualitatively stronger evidence than any model output here
- The reverse mode (test a claimed location and time for consistency) can falsify a claim, which is rarer and more valuable than narrowing a search
- MIT licensed, actively released (0.7.1 on 2026-09-03, same-day push), built by Bellingcat for practising investigators
- The Python/CLI route runs entirely locally and takes measurements as input, not the image itself — so nothing sensitive leaves the machine

## 5. Cons

- Output is a probabilistic band of candidate locations, not a point and not proof, and is only as good as its inputs: object height and shadow length must be estimated from the image, and that estimation is usually the dominant error source
- Requires a visible, measurable shadow with a known or estimable object height — a minority of photographs qualify
- The recommended Google Colab route executes in Google's cloud, which means the measurements (and potentially the image, if uploaded there) leave your control — use the local CLI instead for sensitive cases
- Narrow applicability and 13 open issues on a small project (628 stars)

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 628 stars with 13 open issues, release 0.7.1 on 2026-09-03 with same-day push, MIT licence; the Colab-based workflow is documented by the project. Shadow-based chronolocation is an established technique in open-source investigation practice.

## 7. Assessment

Adopt, and prefer the local CLI over the documented Colab route — that is the single most important operational point, because Colab puts your measurements and possibly the image into Google's infrastructure. For your profile the highest-value use is falsification: when a government or a propaganda account claims a video was shot at a given place and time, shadow geometry can show it was not, and that is a publishable finding grounded in physics rather than in a model's opinion. Document your height and length estimates, since they carry the error.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-03, latest release 0.7.1 published the same day, 628 stars, 13 open issues. Recent release from an institutional maintainer (Bellingcat) with a clean tracker.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — astronomical computation, no trained model. Depends on suncalc and timezone grid data.

**Restrictions:** None.

**Licence evidence:** https://github.com/bellingcat/ShadowFinder/blob/main/LICENSE

## 10. Costs

No fee. Negligible compute; runs on a laptop. The Colab route is free within Google's limits but is the option to avoid for sensitive work.

## 11. Privacy and data flows

The Python/CLI route runs entirely locally and takes measurements rather than the image itself — an excellent privacy position. The recommended Colab route executes in Google's cloud and should be avoided for unpublished material.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [SunCalc](OSINT-C2-18.md) or Skyfield for the underlying solar-position computation if you build your own tooling
- [GeoCLIP](OSINT-C2-16.md) to narrow the region before applying shadow constraints
- [Stellarium](OSINT-C2-37.md) for verifying night-sky rather than solar geometry

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/ShadowFinder
- https://github.com/bellingcat/ShadowFinder/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 34. [Scoop](OSINT-C1-36.md) · 36. [trafilatura](JAI-A1-01.md) →
