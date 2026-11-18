# OCRmyPDF

`JAI-A2-33` · **94/100** · overall rank 13 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 3) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 1) |
| **Subcategory** | OCR pipeline |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | James R. Barlow and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | MPL-2.0 |
| **Licence type** | Weak copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ocrmypdf/OCRmyPDF) · [Documentation](https://ocrmypdf.readthedocs.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 94/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Weak copyleft |
| **Exact licence (as recorded)** | MPL-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a (Tesseract traineddata is separately licensed, generally Apache-2.0 from the tesseract-ocr project). |
| **Restrictions** | MPL-2.0 file-level copyleft: modifications to OCRmyPDF's own files must be shared if distributed. Ghostscript is a runtime dependency with AGPL terms from Artifex absent a commercial licence — relevant only if you redistribute a bundle. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU-bound; OCR time is roughly linear in page count, so a large scan dump is a compute-hours cost on commodity hardware. Containerised deployment keeps operating effort low. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ocrmypdf/OCRmyPDF/blob/main/LICENSE
- https://github.com/ocrmypdf/OCRmyPDF
- https://ocrmypdf.readthedocs.io/

---

## 1. Purpose

Adds a searchable text layer to scanned PDFs using Tesseract while preserving the original page images, with deskewing, cleaning, optimisation and PDF/A output.

## Journalism / investigative use case

The standard first pass on a scan dump: makes thousands of image-only PDFs grep-able and ingestable by DocumentCloud, OpenAleph or Datashare while preserving the original page images as evidence — the preservation property is what makes it safe to run across source material.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Preserves the original page image alongside the text layer, so the evidentiary artefact is never replaced by a machine interpretation — the right default for journalism
- Idempotent, resumable and designed for batch operation over huge directories; genuinely reliable at scale, which is rare in OCR tooling
- Exceptionally well documented and released very frequently (v17.14.2, 2026-11-16) with only 69 open issues against 35,338 stars
- PDF/A output and optimisation make the results archive-grade and much smaller, which matters for long-term storage costs

## 5. Cons

- Inherits Tesseract's accuracy ceiling: degraded scans, handwriting and unusual fonts come out poorly and no amount of preprocessing fixes it
- Produces a PDF, not structured data — no table extraction, no layout model, so it is the start of a pipeline rather than an answer
- MPL-2.0 file-level copyleft is mild but non-zero if you vendor modified source into a proprietary product
- Dependency chain (Tesseract, Ghostscript, optional jbig2enc/unpaper) makes reproducible installs fiddly outside containers

## 6. Feedback (documented)

No individual user reports verified. The quantitative evidence is unusually strong: 35,338 stars with 69 open issues and a release on 2026-11-16 — among the healthiest maintenance profiles in the entire catalogue. Widely used as the OCR step in self-hosted document stacks (Paperless-ngx depends on this toolchain).

## 7. Assessment

Adopt without reservation as the default OCR step for scanned material. Its value for your work is not accuracy — that is Tesseract's limit — but operational reliability and evidentiary integrity: it will finish a 200,000-page job and the originals will still be there. Where accuracy is insufficient, escalate specific documents to Surya/Marker or Kraken rather than changing the default.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v17.14.2 (2026-11-16), 35,338 stars, 69 open issues. Same-day push and release, major version 17, minimal backlog — maintenance quality is evidenced by issue throughput, not just commit frequency.

## 9. Licensing

**Licence:** MPL-2.0 _(SPDX verified)_

**Model / data licence:** n/a (Tesseract traineddata is separately licensed, generally Apache-2.0 from the tesseract-ocr project).

**Restrictions:** MPL-2.0 file-level copyleft: modifications to OCRmyPDF's own files must be shared if distributed. Ghostscript is a runtime dependency with AGPL terms from Artifex absent a commercial licence — relevant only if you redistribute a bundle.

**Licence evidence:** https://github.com/ocrmypdf/OCRmyPDF/blob/main/LICENSE

## 10. Costs

No fee. CPU-bound; OCR time is roughly linear in page count, so a large scan dump is a compute-hours cost on commodity hardware. Containerised deployment keeps operating effort low. Estimate.

## 11. Privacy and data flows

Fully local, no network calls, no telemetry. Safe on an air-gapped evidence machine.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Surya](JAI-A2-52.md) or Marker where Tesseract's accuracy is the binding constraint
- PaddleOCR for CJK and Arabic scans
- [Dangerzone](SUR-B3-03.md) first, if the PDFs come from an untrusted source

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ocrmypdf/OCRmyPDF
- https://ocrmypdf.readthedocs.io/
- https://github.com/ocrmypdf/OCRmyPDF/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 12. [mat2](SUR-B3-07.md) · 14. [Ollama](JAI-A3-02.md) →
