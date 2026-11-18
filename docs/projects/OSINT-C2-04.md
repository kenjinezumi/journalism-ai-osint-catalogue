# MediaInfo

`OSINT-C2-04` · **88/100** · overall rank 56 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 18) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 6) |
| **Subcategory** | Video container analysis |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | MediaArea |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MediaArea/MediaInfo) · [Documentation](https://mediaarea.net/MediaInfo) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 88/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material — permissive and safe to embed. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, no infrastructure. MediaArea offers paid support and custom development — optional, not required.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/MediaArea/MediaInfo/blob/master/LICENSE
- https://github.com/MediaArea/MediaInfo
- https://mediaarea.net/MediaInfo

---

## 1. Purpose

GUI and CLI tool reporting technical and tag information for video and audio files: container structure, codecs, bitrates, frame rates, encoder identification and writing-application fields.

## Journalism / investigative use case

Establish provenance signals on a submitted video before content analysis: which app or device wrote the file, whether the container layout matches a direct camera export or a WhatsApp/Telegram re-encode, and whether two 'different' files share an identical encoder fingerprint — which is how you spot that a 'new' video is a re-upload.

## 2. Audience

journalist, newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Container and encoder fingerprinting answers the question reporters actually have about a video file — where has this been — which no content-analysis tool addresses
- Identifies platform re-encodes, so you can tell a camera original from a WhatsApp forward, which determines whether any forensic analysis is even worth attempting
- Fully local file inspection with no network dependency, appropriate for source-supplied material
- Actively maintained (v26.10, 2026-10-06; pushed 2026-11-14) with both GUI and CLI, so analysts and pipelines are both served

## 5. Cons

- Reports only what the file declares: metadata is trivially stripped or forged, and almost every social platform re-encodes on upload, destroying original encoder fields — so absence of suspicious metadata means nothing
- 224 open issues, a large backlog for a tool of this scope
- Interpreting container fingerprints requires experience; the raw report does not say 'this is a WhatsApp re-encode', you must know the signatures
- Build-time GUI toolkit choice makes self-building awkward; most users take vendor packages

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 2,070 stars with 224 open issues, release v26.10 (2026-10-06), pushed 2026-11-14, BSD-2-Clause. MediaInfo is a standard tool in media and archiving workflows, reflected in its packaging across distributions.

## 7. Assessment

Adopt as the mandatory first step on any submitted video, before anyone attempts forensic analysis — because it tells you whether the file is a camera original (worth analysing) or a platform re-encode (largely not). For your profile the high-value practice is building an internal reference of encoder fingerprints for the platforms and apps your region uses, so a reporter can be told 'this came through Telegram' rather than having to interpret the raw report.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v26.10 (2026-10-06), 2,070 stars, 224 open issues. Regular dated releases from a dedicated organisation (MediaArea) that also maintains MediaInfoLib and related tooling.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material — permissive and safe to embed.

**Licence evidence:** https://github.com/MediaArea/MediaInfo/blob/master/LICENSE

## 10. Costs

No fee, no infrastructure. MediaArea offers paid support and custom development — optional, not required.

## 11. Privacy and data flows

Entirely local file inspection with no network dependency.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ExifTool](OSINT-C2-01.md) for metadata on image and document files
- ffprobe (FFmpeg) for a scriptable subset of the same container information
- [PySceneDetect](OSINT-C2-10.md) for content-level rather than container-level video analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/MediaArea/MediaInfo
- https://mediaarea.net/MediaInfo
- https://github.com/MediaArea/MediaInfo/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 55. [MobSF (Mobile Security Framework)](SUR-B2-04.md) · 57. [NetworkX](OSINT-C3-31.md) →
