# PySceneDetect

`OSINT-C2-10` · **94/100** · overall rank 15 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 8) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 3) |
| **Subcategory** | Video shot detection |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Brandon Castellano (Breakthrough) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Breakthrough/PySceneDetect) · [Documentation](https://www.scenedetect.com/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 94/100**

---

## 1. Purpose

Python library and CLI that detects shot boundaries in video using content, threshold, adaptive and histogram detectors, and can split video or export keyframes per scene.

## Journalism / investigative use case

First step in video verification: fragment an unknown clip into shots and pull one keyframe per shot so each frame can be reverse-image-searched, geolocated or compared against earlier uploads — the InVID/WeVerify keyframes workflow, runnable locally without uploading the video anywhere.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Reproduces the single most useful verification workflow (keyframes for reverse search) entirely locally, which the InVID plugin cannot
- Multiple detector algorithms with tunable thresholds, so you can handle both hard cuts and gradual transitions
- Very actively maintained (v0.7.3, 2026-11-08; pushed 2026-11-17) with a large community (5,526 stars) and good documentation
- BSD-3-Clause and scriptable, so it drops into a batch pipeline over an archive of collected video

## 5. Cons

- Detects cuts, not manipulation: it produces no authenticity judgement and no proof of anything — a point worth stating because shot-boundary anomalies get over-read
- Content-based detection is threshold-sensitive and can over- or under-segment heavily compressed, low-light or shaky footage, which is most citizen video
- Requires ffmpeg or mkvmerge for splitting, so deployment has an external dependency
- 61 open issues; tuning for a specific footage type takes experimentation

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 5,526 stars with 61 open issues, release v0.7.3 (2026-11-08), pushed 2026-11-17. The keyframe-per-shot workflow it enables is the documented basis of the InVID/WeVerify video-verification method.

## 7. Assessment

Adopt — it is the local foundation of video verification and the reason you do not need to upload a sensitive clip to a third-party keyframe service. For your profile the workflow to standardise: yt-dlp to capture at full bitrate, MediaInfo to establish whether it is an original, PySceneDetect for keyframes, then local reverse-image comparison via your ImageHash/PDQ index before resorting to any external search engine.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.7.3 (2026-11-08), 5,526 stars, 61 open issues. Same-day commits and a recent release from a long-standing single maintainer with consistent cadence.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/Breakthrough/PySceneDetect/blob/main/LICENSE

## 10. Costs

No fee. CPU-bound; ffmpeg required for splitting. Negligible infrastructure.

## 11. Privacy and data flows

Fully local — no network calls or API keys in the documented workflow, so the video never leaves your machine.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Katna](OSINT-C2-11.md) for keyframe selection optimised for visual quality — but note its stalled maintenance
- ffmpeg scene-detection filters for a dependency-free approximation
- InVID plugin for a one-click version that uploads the media

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Breakthrough/PySceneDetect
- https://www.scenedetect.com/
- https://github.com/Breakthrough/PySceneDetect/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 14. [Ollama](JAI-A3-02.md) · 16. [ReplayWeb.page](OSINT-C1-32.md) →
