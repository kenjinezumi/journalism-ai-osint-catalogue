# pHash

`OSINT-C2-08` · **66/100** · overall rank 288 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 107) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 43) |
| **Subcategory** | Perceptual hashing (audio/video) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Aetilius |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/aetilius/pHash) · [Documentation](https://www.phash.org/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 66/100**

---

## 1. Purpose

C++ library implementing perceptual hashes for images, audio and video, with DCT, radial and marr-hildreth image hashes plus audio and video fingerprinting.

## Journalism / investigative use case

Match a short audio or video clip against a reference library to identify re-used broadcast or propaganda material, where image-only hashing is insufficient — for instance recognising that a 'new' leaked recording is a segment of a years-old broadcast.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Audio fingerprinting is the distinguishing capability and a real gap elsewhere in this catalogue: almost nothing open lets you match audio clips against a reference library
- Multiple image hash algorithms including radial and marr-hildreth, which behave differently under rotation and blur than DCT hashes
- Still receiving commits (pushed 2026-06-09) with an essentially empty issue tracker (2 open)
- Long-established algorithms with published descriptions, so the method is citable in a methodology note

## 5. Cons

- GPL-3.0 copyleft constrains embedding in closed newsroom products — a real consideration if you build a service around it
- Low-level library with sparse modern documentation; audio and video hashing need careful parameterisation and there is little guidance
- Matches are similarity signals only, and audio fingerprinting degrades with heavy compression or background noise
- No releases at all and a C++ toolchain with CImg and FFmpeg dependencies, so building it is a project

## 6. Feedback (documented)

No individual user reports verified. Documented: 664 stars with 2 open issues, no releases, last push 2026-06-09, GPL-3.0. The near-empty tracker on a library of this age more likely reflects low use than perfect quality.

## 7. Assessment

Worth the build effort only if audio matching is a specific need — and for monitoring broadcast or propaganda reuse, it genuinely is. For your profile I would scope it narrowly: build a reference library of the broadcasts and recordings relevant to one investigation, fingerprint incoming clips against it, and treat matches as leads. For image work, PDQ and ImageHash are better supported and easier.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-06-09, no releases or tags, 664 stars, 2 open issues. Five months since last push on a long-established library with minimal churn; stable rather than declining, though documentation and release engineering are effectively absent.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0 copyleft: embedding in a closed-source newsroom product triggers source obligations. Internal use and CLI invocation are unaffected.

**Licence evidence:** https://github.com/aetilius/pHash/blob/master/LICENSE

## 10. Costs

No fee. C++ toolchain, CImg, FFmpeg for video/audio. Build effort is the real cost; no paid dependencies.

## 11. Privacy and data flows

Entirely local, no network, no models.

## 12. Verdict

**Monitor**

## 13. Alternatives

- ThreatExchange vPDQ/TMK+PDQF for video matching with better support
- Chromaprint/AcoustID for audio fingerprinting with a maintained ecosystem
- [ImageHash](OSINT-C2-05.md) for the image-only case

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/aetilius/pHash
- https://www.phash.org/
- https://github.com/aetilius/pHash/blob/master/LICENSE

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

← 287. [imagededup](OSINT-C2-07.md) · 289. [YaCy](OSINT-C1-06.md) →
