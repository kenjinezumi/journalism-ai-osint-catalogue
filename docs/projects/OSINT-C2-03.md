# Exiv2

`OSINT-C2-03` · **71/100** · overall rank 263 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 92) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 37) |
| **Subcategory** | Metadata extraction |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Exiv2 community |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-2.0-or-later (GitHub reports NOASSERTION) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Exiv2/exiv2) · [Documentation](https://exiv2.org/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 71/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-2.0-or-later (GitHub reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-2.0-or-later: linking it into a closed-source product triggers copyleft. Historically a commercial licence has been available from the project — confirm current terms if you need one. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. C++ build toolchain; optional zlib/expat. Negligible runtime cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Exiv2/exiv2/blob/main/COPYING
- https://github.com/Exiv2/exiv2
- https://exiv2.org/

---

## 1. Purpose

C++ library and CLI for reading and writing image metadata — EXIF, IPTC, XMP and several maker-note dialects — with a stable API used by many desktop applications.

## Journalism / investigative use case

Embed metadata extraction into a newsroom ingest pipeline so every incoming image is automatically parsed for timestamps and GPS before an analyst sees it — the library route when you want metadata handling compiled into a service rather than shelling out to a Perl script.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- C++ library with a stable API makes it the right choice for embedding in a service, where ExifTool's subprocess model is awkward
- Used by many desktop photo applications, so its parsing is exercised against a very wide range of real files
- Actively maintained (v0.28.9, 2026-08-30; pushed 2026-11-16) with a long release history
- GPL-2.0-or-later with a commercial licence also historically available — read the distribution you obtain

## 5. Cons

- Narrower maker-note coverage than ExifTool, so for forensic depth on camera-specific fields ExifTool remains better
- Same fundamental caveat as all metadata tools: metadata is writer-controlled and routinely stripped, so it corroborates rather than proves
- Engineer-facing with no analyst UI, and the C++ toolchain requirement makes it a heavier dependency than a Python wrapper
- 226 open issues, a substantial backlog reflecting the long tail of format edge cases

## 6. Feedback (documented)

No individual user reports verified. Documented: 1,173 stars with 226 open issues, release v0.28.9 (2026-08-30), pushed 2026-11-16, SPDX NOASSERTION with GPL-2.0-or-later as the stated licence.

## 7. Assessment

Choose it over ExifTool only when you need in-process metadata handling in a compiled service; otherwise ExifTool's coverage wins. For your profile that means Exiv2 is a build-time decision for a custom ingest service, not a tool you reach for interactively. If you are already running Apache Tika in the ingest path, its metadata output may make Exiv2 unnecessary.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v0.28.9 (2026-08-30), 1,173 stars, 226 open issues. Regular point releases on the 0.28 line with current commits from a community team.

## 9. Licensing

**Licence:** GPL-2.0-or-later (GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** GPL-2.0-or-later: linking it into a closed-source product triggers copyleft. Historically a commercial licence has been available from the project — confirm current terms if you need one.

**Licence evidence:** https://github.com/Exiv2/exiv2/blob/main/COPYING

## 10. Costs

No fee. C++ build toolchain; optional zlib/expat. Negligible runtime cost.

## 11. Privacy and data flows

Entirely local, no network calls.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [ExifTool](OSINT-C2-01.md) for maximum coverage via CLI
- [Apache Tika](JAI-A2-02.md) if you already run it for document metadata
- [PyExifTool](OSINT-C2-02.md) for a Python-native path

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/Exiv2/exiv2
- https://exiv2.org/

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

← 262. [MinerU](JAI-A1-11.md) · 264. [Hyphe](OSINT-C1-21.md) →
