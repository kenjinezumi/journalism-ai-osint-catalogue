# Camelot

`JAI-A2-06` · **85/100** · overall rank 88 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 33) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 22) |
| **Subcategory** | Table extraction |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | camelot-dev community (fork of the archived atlanhq/camelot) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/camelot-dev/camelot) · [Documentation](https://camelot-py.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## 1. Purpose

Python library that extracts tables from born-digital PDFs using two strategies — lattice (ruling-line detection) and stream (whitespace clustering) — and returns pandas DataFrames with a per-table accuracy score.

## Journalism / investigative use case

Pulling budget tables, campaign-finance schedules and procurement annexes out of text-layer PDFs into spreadsheets at scale. The per-table accuracy score is the underrated feature: it tells a reporter which of 400 extracted tables need manual checking, turning an unbounded verification task into a ranked one.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- The accuracy/whitespace score per table is a genuine auditability feature — few extractors tell you how confident they are
- Two complementary algorithms cover both ruled and unruled tables, which between them handle most government PDF conventions
- Community fork is demonstrably alive (v2.0.0 released 2026-06-04) after the original atlanhq repo went dead — the licence and lineage are clean
- Outputs straight to pandas/CSV, so it drops into an existing data-journalism workflow with no glue

## 5. Cons

- Requires a real text layer: scanned pages must be OCR'd first (OCRmyPDF), and this trips people up constantly
- Merged cells, tables spanning page breaks and rotated pages all degrade output; multi-page financial annexes usually need custom stitching code
- Ghostscript and OpenCV dependencies make the install heavier than pdfplumber's
- The widely-linked original repo (atlanhq/camelot) is dead, so most search results and old Stack Overflow answers point at the wrong project — a real practical trap

## 6. Feedback (documented)

No individual user reports verified. The documented community signal is the fork itself: the move from atlanhq to camelot-dev, with a 2.0.0 release in 2026, is evidence of a user base large enough to rescue the project. 3,857 stars, 58 open issues.

## 7. Assessment

Keep both Camelot and pdfplumber installed and choose per document — Camelot when the table has ruling lines and you want a confidence score, pdfplumber when you need character coordinates and a visual debugger. For your work the accuracy score is what justifies Camelot's extra install weight: it lets you build a pipeline that escalates low-confidence tables to a human rather than silently publishing a mis-parsed budget figure.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v2.0.0 (2026-06-04), 3,857 stars, 58 open issues. A major version in 2026 plus current commits on a community fork; classified active on release substance, not push recency.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Note Ghostscript is a runtime dependency and is AGPL-licensed when obtained from Artifex without a commercial licence — relevant if you redistribute a bundled product, not for internal use.

**Licence evidence:** https://github.com/camelot-dev/camelot/blob/master/LICENSE

## 10. Costs

No fee. CPU-only, negligible infrastructure. The real cost is engineer time writing per-document-family extraction rules and the human review of low-confidence tables. Ghostscript licensing could become a cost if you ship Camelot inside a commercial product.

## 11. Privacy and data flows

Fully local; no network calls. Safe for sensitive documents on an isolated machine.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [pdfplumber](JAI-A2-39.md) for coordinate-level control and visual debugging
- [Tabula](JAI-A2-53.md) for a no-code reporter-driven workflow
- [Surya](JAI-A2-52.md)/Marker or Docling for scanned or complex-layout tables where neither Camelot strategy applies

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/camelot-dev/camelot
- https://camelot-py.readthedocs.io/
- https://github.com/camelot-dev/camelot/blob/master/LICENSE

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

← 87. [n8n](JAI-A1-17.md) · 89. [DuckDB spatial extension](JAI-A1-19.md) →
