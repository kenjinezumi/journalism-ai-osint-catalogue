# Katna

`OSINT-C2-11` · **64/100** · overall rank 294 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 111) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 44) |
| **Subcategory** | Video keyframe selection |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Kepler Lab |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/keplerlab/katna) · [Documentation](https://katna.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 64/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python library that selects representative keyframes from video by scoring frames for blur, brightness, contrast and visual diversity, and can also crop images intelligently.

## Journalism / investigative use case

Automatically pick the most informative, least blurry frames from shaky phone footage to use as geolocation and reverse-image-search candidates — the difference between reverse-searching a motion-blurred frame and a sharp one.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Frame quality scoring (blur, brightness, contrast) is genuinely useful for geolocation work, where a sharp frame is worth ten blurry ones
- Diversity-aware selection avoids returning ten near-identical frames from a static shot, which naive per-shot extraction does
- MIT licensed with a small clean dependency set (OpenCV, FFmpeg) and no API keys

## 5. Cons

- Frame selection is optimised for visual appeal and diversity, not evidential completeness, so it can discard the one frame that matters — always verify against the full video, which is a real and easy-to-miss failure mode
- Maintenance has stalled: last push 2024-08-06, no releases (tag v0.9.2), 401 stars — over two years quiet
- Narrow scope: it chooses frames and does not detect shots, so it complements rather than replaces PySceneDetect
- Small community means little guidance on parameter choice for investigative rather than thumbnail-generation use

## 6. Feedback (documented)

No individual user reports verified. Documented: 401 stars with 10 open issues, no releases (tag v0.9.2), last push 2024-08-06, MIT licence. Its design intent (thumbnail and highlight selection) is documented by the project and explains the appeal-over-completeness bias.

## 7. Assessment

Useful as a ranking aid on top of PySceneDetect's shot segmentation, not as a replacement for it — and never as a filter that decides which frames a human sees. For your profile the correct pattern is: PySceneDetect for all shot boundaries, Katna to rank frames within shots by quality, human review of the ranked list with the full video available. Given the dormancy I would not build anything load-bearing on it.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-08-06, no releases, latest tag v0.9.2, 401 stars, 10 open issues. Over two years without activity; OpenCV-dependent code of this age will eventually break on new releases.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/keplerlab/katna/blob/master/LICENSE

## 10. Costs

No fee. CPU only; OpenCV and FFmpeg dependencies. Negligible.

## 11. Privacy and data flows

Entirely local.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Dormant since 2024; frame selection optimises for appeal rather than completeness

## 13. Alternatives

- [PySceneDetect](OSINT-C2-10.md) for shot detection and keyframe export — maintained and the better foundation
- A simple Laplacian-variance blur score written yourself, which is a few lines and removes the dependency
- ffmpeg thumbnail filter for a crude equivalent

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/keplerlab/katna
- https://katna.readthedocs.io/
- https://github.com/keplerlab/katna/blob/master/LICENSE

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

← 293. [warcprox](OSINT-C1-42.md) · 295. [Overview](OSINT-C3-04.md) →
