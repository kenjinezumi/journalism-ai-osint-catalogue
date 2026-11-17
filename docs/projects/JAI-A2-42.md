# PyMuPDF

`JAI-A2-42` · **86/100** · overall rank 73 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 28) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 19) |
| **Subcategory** | PDF manipulation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Artifex Software |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 (dual-licensed; Artifex sells a commercial licence) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/pymupdf/PyMuPDF) · [Documentation](https://pymupdf.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 2/5 → **weighted 86/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python bindings to MuPDF providing fast text and image extraction, page rendering, annotation, document assembly and true redaction that removes underlying content.

## Journalism / investigative use case

Fastest route to rasterising pages for OCR at corpus scale, and — critically — to applying genuine redactions that delete the underlying text rather than drawing a black rectangle over it. That distinction is a documented real-world newsroom failure mode: published PDFs whose 'redactions' were copy-pasteable.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- True redaction (apply_redactions removes the content stream text) prevents the single most embarrassing and dangerous document-publishing failure in journalism
- Significantly faster than pdfminer-based libraries for rendering and bulk text extraction, which matters when rasterising hundreds of thousands of pages
- Very actively maintained (pushed 2026-11-17, release 2.1 on 2026-11-02) with a small backlog (79 open issues against 11,147 stars)
- Single bundled dependency (MuPDF) makes deployment simple compared with Ghostscript-dependent alternatives

## 5. Cons

- AGPL-3.0 is the decisive caveat: embedding PyMuPDF in a network-facing newsroom service triggers source-release obligations unless you buy Artifex's commercial licence — and the commercial price is not publicly listed
- The dual-licence model means your compliance position depends on how you deploy, not just what you build — an easy thing to get wrong late in a project
- API has changed across major versions (1.x to 2.x naming), so older tutorials and code break
- Rendering fidelity and text-extraction ordering can differ from pdfplumber, so results are not interchangeable between libraries

## 6. Feedback (documented)

No individual user reports verified. Documented: AGPL-3.0 confirmed via GitHub API and the repository licence; Artifex's commercial licensing is advertised on its site without a public price (quote required, not verified here). 11,147 stars, 79 open issues, release 2026-11-02.

## 7. Assessment

Use it for internal batch processing and redaction, where AGPL is harmless; think carefully before putting it inside a public-facing service. For your profile the redaction capability alone justifies having it in the toolkit — I would build a small internal redaction utility around it rather than relying on a GUI tool. If you need a permissive alternative for a product you ship, pypdf (BSD-style) or pdfminer.six cover extraction but not fast rendering or true redaction.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 2.1 (2026-11-02), 11,147 stars, 79 open issues. Commercial vendor backing with frequent releases and prompt issue handling.

## 9. Licensing

**Licence:** AGPL-3.0 (dual-licensed; Artifex sells a commercial licence) _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0 network copyleft is material: offering a modified or even unmodified PyMuPDF-based service over a network obliges you to provide corresponding source under AGPL terms, unless you hold Artifex's commercial licence. Commercial licence price is not publicly listed — quote required.

**Licence evidence:** https://github.com/pymupdf/PyMuPDF/blob/main/COPYING

## 10. Costs

Free under AGPL-3.0. Commercial licence from Artifex: price not publicly listed (quote required, not verified in this survey). No infrastructure beyond Python; CPU-bound.

## 11. Privacy and data flows

Fully local, no network calls. Good fit for isolated evidence machines.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- AGPL-3.0 network copyleft if deployed inside a public-facing service without a commercial licence

## 13. Alternatives

- pypdf (BSD-3-Clause) for licence-clean extraction and page manipulation
- [pdfplumber](JAI-A2-39.md) for auditable coordinate-level extraction
- Ghostscript/qpdf for rasterisation if AGPL is unacceptable and you can tolerate slower performance

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/pymupdf/PyMuPDF
- https://pymupdf.readthedocs.io/
- https://github.com/pymupdf/PyMuPDF/blob/main/COPYING

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

← 72. [GDAL](OSINT-C2-20.md) · 74. [Apktool](SUR-B2-05.md) →
