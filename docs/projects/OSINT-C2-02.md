# PyExifTool

`OSINT-C2-02` · **72/100** · overall rank 250 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 85) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 33) |
| **Subcategory** | Metadata extraction |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | sylikc and contributors |
| **Maintenance** | Dormant |
| **Licence** | GPL-3.0-or-later OR BSD (dual-licensed; user may choose) — GitHub reports NOASSERTION |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/sylikc/pyexiftool) · [Documentation](https://sylikc.github.io/pyexiftool/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python wrapper that runs ExifTool as a persistent subprocess and exposes its output as Python dictionaries, avoiding per-file process startup cost.

## Journalism / investigative use case

The practical way to metadata-profile a dump of thousands of images — clustering a leaked image set by camera body, software signature or capture-time gaps — inside a Python pipeline rather than by shelling out per file.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Persistent-process design makes bulk metadata extraction fast enough for corpus-scale work, where naive per-file invocation would take hours
- Returns structured dictionaries, so clustering by device or detecting timestamp anomalies becomes a few lines of pandas
- Dual-licensed GPL-3.0-or-later OR BSD (user's choice), which is unusually flexible and removes the copyleft concern for a newsroom codebase
- Thin wrapper, so it inherits ExifTool's full capability without reimplementing anything

## 5. Cons

- Inherits every interpretive caveat of ExifTool — metadata is editable and routinely stripped, so outputs support leads rather than conclusions
- A wrapper, not a forensic method: it adds convenience, not analytical capability
- Dormant: last push 2023-11-26 with release v0.5.6 (2023-10-22) and 28 open issues — three years without activity
- Requires the ExifTool binary installed separately, so deployment has two moving parts and version skew between them is a real source of surprise

## 6. Feedback (documented)

No individual user reports verified. Documented: 197 stars with 28 open issues, release v0.5.6 (2023-10-22), last push 2023-11-26, SPDX NOASSERTION with the dual GPL/BSD choice declared in the repository.

## 7. Assessment

Still usable despite dormancy, because it is a thin wrapper around a tool that is itself impeccably maintained — the dependency-rot risk is low and the failure mode would be obvious. For your profile I would use it for bulk profiling work and pin both it and the ExifTool binary version in the pipeline. If it ever breaks, calling ExifTool with `-j` (JSON output) directly via subprocess is a half-hour replacement, which is worth knowing before you depend on it.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2023-11-26, latest release v0.5.6 (2023-10-22), 197 stars, 28 open issues. Three years without commits. Mitigated by its nature: a thin wrapper over a stable CLI interface has very little surface to rot.

## 9. Licensing

**Licence:** GPL-3.0-or-later OR BSD (dual-licensed; user may choose) — GitHub reports NOASSERTION _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** The BSD option removes any copyleft concern for a newsroom codebase — choose it explicitly and record the choice.

**Licence evidence:** https://github.com/sylikc/pyexiftool

## 10. Costs

No fee. Requires the ExifTool binary. Negligible resources.

## 11. Privacy and data flows

Local only; no network calls documented. Safe on an isolated machine.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Dormant since 2023; have a direct-subprocess fallback in mind

## 13. Alternatives

- Calling `exiftool -j` directly via subprocess — a trivial and fully maintained substitute
- [Exiv2](OSINT-C2-03.md) bindings for a C++-backed library path
- [Apache Tika](JAI-A2-02.md) for metadata across a wider range of document formats

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/sylikc/pyexiftool
- https://sylikc.github.io/pyexiftool/

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

← 249. [Klaxon Cloud (DocumentCloud Add-On)](SUR-B1-19.md) · 251. [rtl-ais](OSINT-C2-49.md) →
