# ExifTool

`OSINT-C2-01` · **96/100** · overall rank 1 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 1) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 1) |
| **Subcategory** | Metadata extraction |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Phil Harvey |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/exiftool/exiftool) · [Documentation](https://exiftool.org/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 96/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0 (the upstream distribution is also offered under the Artistic Licence — check the distribution you obtain). Embedding in a closed-source newsroom product would trigger copyleft; calling the CLI as a subprocess does not. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, no infrastructure, no paid dependencies. Among the cheapest high-value capabilities here.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/exiftool/exiftool/blob/master/LICENSE
- https://github.com/exiftool/exiftool
- https://exiftool.org/

---

## 1. Purpose

Perl library and command-line tool that reads, writes and edits metadata in several hundred file formats, covering EXIF, IPTC, XMP, GPS, maker notes and embedded thumbnails.

## Journalism / investigative use case

First step on almost every image verification: dump the full metadata block to read capture time, GPS coordinates, device and lens, software history and embedded thumbnails. An embedded thumbnail that disagrees with the main image is a classic indicator that the visible picture was edited after capture.

## 2. Audience

journalist, newsroom analyst, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Unmatched format and maker-note coverage — it reads proprietary camera fields no other tool parses, which is often where the useful capture detail lives
- The embedded-thumbnail extraction is a genuine forensic technique, not just metadata reading, and it has broken real cases
- Entirely local with no dependencies beyond Perl, so it runs on an air-gapped evidence machine and nothing is transmitted
- Exceptionally maintained for a single-maintainer project: release 13.64 and a near-empty tracker (19 open issues against 5,268 stars)

## 5. Cons

- Metadata is evidence about a file, not about reality: every field can be written or stripped — by ExifTool itself — so a plausible EXIF block is corroboration, never authentication
- Most social platforms strip metadata on upload, so for the majority of circulating images there is simply nothing to read, and reporters misread that absence as suspicious
- The output is dense and expert-oriented; a non-specialist will not know which of 400 fields matter
- Perl dependency is unusual in a modern stack, and the write capability makes it easy to alter evidence accidentally if used carelessly

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 5,268 stars with only 19 open issues and a current tag (13.64), pushed 2026-11-16 — extraordinary maintenance consistency over two decades. ExifTool is the de facto standard underneath most other metadata tooling, verifiable from PyExifTool, Sherloq and ArchiveBox all depending on it.

## 7. Assessment

Adopt unconditionally: it is the baseline instrument for image and document files and there is no substitute. For your profile two disciplines matter. First, work on copies — ExifTool can write, and an accidental write destroys the evidential value of the original. Second, train reporters that stripped metadata is the normal case for social media, so 'no EXIF' is not a finding. Pair with MediaInfo for video containers, where ExifTool is weaker.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest tag 13.64, no GitHub release objects (releases are published on exiftool.org), 5,268 stars, 19 open issues. Continuous releases over twenty years from a single maintainer with near-zero backlog — the strongest issue-throughput record in the catalogue.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0 (the upstream distribution is also offered under the Artistic Licence — check the distribution you obtain). Embedding in a closed-source newsroom product would trigger copyleft; calling the CLI as a subprocess does not.

**Licence evidence:** https://github.com/exiftool/exiftool/blob/master/LICENSE

## 10. Costs

No fee, no infrastructure, no paid dependencies. Among the cheapest high-value capabilities here.

## 11. Privacy and data flows

Entirely local; nothing is transmitted, which makes it safe for source-sensitive material. The inverse risk matters more: ExifTool reveals GPS and device data in files you may intend to publish, so it is also the tool that tells you what to strip.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [PyExifTool](OSINT-C2-02.md) to drive it from a Python pipeline
- [Exiv2](OSINT-C2-03.md) for a C++ library embedding path
- [MediaInfo](OSINT-C2-04.md) for video container and encoder analysis
- [mat2](SUR-B3-07.md) for removing rather than reading metadata

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/exiftool/exiftool
- https://exiftool.org/
- https://github.com/exiftool/exiftool/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

2. [llama.cpp](JAI-A3-01.md) →
