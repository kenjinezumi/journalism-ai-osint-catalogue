# MarkItDown

`JAI-A1-09` · **83/100** · overall rank 124 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 52) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 14) |
| **Subcategory** | Document conversion |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Microsoft |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/microsoft/markitdown) · [Documentation](https://github.com/microsoft/markitdown#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 83/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the core; optional model-based converters depend on whatever model you configure. |
| **Restrictions** | Code unrestricted. Verify the licence of any model-based converter you enable. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU-light for most formats. If model-based conversion paths are enabled, those costs apply (not priced here).

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/microsoft/markitdown/blob/main/LICENSE
- https://github.com/microsoft/markitdown

---

## 1. Purpose

Python utility that converts many file and document formats — Office documents, PDFs, HTML, images, audio, archives — into Markdown suitable for text processing and language-model input.

## Journalism / investigative use case

Fast, uniform conversion of a mixed document set into readable Markdown for triage and search: a folder containing Word files, spreadsheets, PDFs and web captures becomes one consistent text corpus in a single command, which is often all you need before deciding what deserves careful extraction.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Format breadth with almost no configuration: for quick triage of a heterogeneous dump it is the lowest-effort option in this catalogue
- MIT licensed with enormous adoption (195,958 stars) and active maintenance (v0.1.9, 2026-10-21; pushed 2026-11-07)
- Markdown output is both human-readable and well-suited to downstream search or model input, so one conversion serves several purposes
- Simple enough to drop into a pipeline in minutes, which matters when a document set arrives at short notice

## 5. Cons

- Conversion fidelity is shallow compared with Docling or Marker: layout, reading order and table structure are not properly modelled, so complex documents lose structure silently
- 818 open issues against a very fast-growing project — expect rough edges and API churn, and pin the version
- Designed primarily to feed language models, so defaults optimise for 'text a model can read' rather than for evidentiary fidelity, and the distinction matters when an extraction may be quoted
- Some converters may invoke external services or models depending on configuration, which needs checking before running it on sensitive material

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 195,958 stars with 818 open issues, release v0.1.9 (2026-10-21), pushed 2026-11-07, MIT licence. The scale of adoption is clear; the issue count reflects very rapid growth rather than neglect.

## 7. Assessment

Use it for triage and not for evidence. The honest division for your profile is: MarkItDown to see what is in a folder quickly, Docling or Marker for documents whose structure matters and whose extraction may be quoted, and the original file always retained. Check the configuration before running it on source material, since some conversion paths can reach for external services, and that would be an unacceptable disclosure for leaked documents.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-07, latest release v0.1.9 (2026-10-21), 195,958 stars, 818 open issues. Current commits and releases under corporate maintenance; the enormous backlog is a function of explosive adoption.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the core; optional model-based converters depend on whatever model you configure.

**Restrictions:** Code unrestricted. Verify the licence of any model-based converter you enable.

**Licence evidence:** https://github.com/microsoft/markitdown/blob/main/LICENSE

## 10. Costs

No fee. CPU-light for most formats. If model-based conversion paths are enabled, those costs apply (not priced here).

## 11. Privacy and data flows

Local for the standard converters. The item to verify is whether any enabled converter calls an external service — check before processing source documents.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Docling](JAI-A2-12.md) for layout-aware, provenance-preserving conversion
- [Apache Tika](JAI-A2-02.md) for maximum format coverage with metadata
- [Marker](JAI-A2-28.md) where conversion accuracy is the priority and the weights licence is acceptable

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/microsoft/markitdown
- https://github.com/microsoft/markitdown/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 123. [VeraCrypt](SUR-B3-22.md) · 125. [subfinder](OSINT-C3-23.md) →
