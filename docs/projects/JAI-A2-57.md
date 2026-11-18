# VisiData

`JAI-A2-57` · **84/100** · overall rank 108 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 44) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 25) |
| **Subcategory** | Tabular data exploration |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Saul Pwanson |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/saulpw/visidata) · [Documentation](https://www.visidata.org/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0: redistribution of a modified version obliges source release. Internal newsroom use is unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Runs anywhere Python runs, including a small VM. Optional per-format loader libraries. Negligible cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/saulpw/visidata/blob/develop/LICENSE.gpl3
- https://github.com/saulpw/visidata
- https://www.visidata.org/docs/

---

## 1. Purpose

Terminal spreadsheet and data-exploration tool that opens dozens of formats (CSV, JSON, SQLite, Parquet, XLSX, HTML tables and more), with frequency analysis, filtering, reshaping, joins and a replayable command log.

## Journalism / investigative use case

First-look tool on a messy leaked dataset: profile a 10-million-row CSV, spot encoding and type breakage, and build a cleaning recipe — all over SSH on an air-gapped evidence machine where no GUI is available. That last property is why it is in this catalogue rather than a general data tool.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Works over SSH on a headless evidence machine, which is exactly where sensitive data should be processed and where OpenRefine cannot go
- Frequency-table-first workflow surfaces data-quality problems (stray encodings, impossible dates, duplicate keys) in seconds rather than after an hour of pandas
- The command log is replayable, so an exploration session becomes a reproducible script — a real methodology asset
- Handles very large files without loading everything into memory, unlike OpenRefine's JVM heap limits

## 5. Cons

- Steep keyboard-driven learning curve; a reporter will not pick it up unaided, so it is an analyst/engineer tool despite being an 'application'
- GPL-3.0 affects redistribution inside proprietary tooling (irrelevant for internal use)
- Exploration and reshaping rather than probabilistic linkage — pair it with Splink or dedupe for matching work
- Terminal rendering of wide tables is cramped; some data shapes are genuinely easier to see in a GUI

## 6. Feedback (documented)

No individual user reports verified. Documented: 9,473 stars with only 8 open issues and a release v3.5 (2026-10-28) — excellent issue throughput. VisiData is a well-known tool in the data-journalism community, reflected in its documentation and conference presence; no specific deployment verified.

## 7. Assessment

Adopt it for anyone on your team who works in a terminal, specifically because it is the only serious data-exploration tool that works well on a locked-down headless box. The pairing I would standardise: VisiData for profiling and cleaning recipes on the evidence machine, Datasette for sharing the result with reporters, Splink when linkage is needed. The learning curve is real but one afternoon gets an analyst productive.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-11, latest release v3.5 (2026-10-28), 9,473 stars, 8 open issues. Recent release and a near-empty backlog from a long-standing single maintainer.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0: redistribution of a modified version obliges source release. Internal newsroom use is unaffected.

**Licence evidence:** https://github.com/saulpw/visidata/blob/develop/LICENSE.gpl3

## 10. Costs

No fee. Runs anywhere Python runs, including a small VM. Optional per-format loader libraries. Negligible cost.

## 11. Privacy and data flows

Fully local with no network calls, and usable over SSH on an isolated machine — a deliberate privacy advantage over GUI tools that require the data on a workstation.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [OpenRefine](JAI-A2-36.md) for a GUI-based, reporter-accessible workflow
- [Datasette](JAI-A2-09.md) for sharing and browsing rather than cleaning
- DuckDB plus a notebook for heavier analytical work

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/saulpw/visidata
- https://www.visidata.org/docs/
- https://github.com/saulpw/visidata/blob/develop/LICENSE.gpl3

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |

---

← 107. [Nominatim](OSINT-C2-28.md) · 109. [Miniflux](JAI-A1-04.md) →
