# Tesseract OCR

`JAI-A2-54` · **85/100** · overall rank 99 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 41) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 23) |
| **Subcategory** | OCR engine |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | tesseract-ocr community (Google-originated; UB Mannheim builds) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/tesseract-ocr/tesseract) · [Documentation](https://tesseract-ocr.github.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Apache-2.0 for tessdata traineddata from the same project (verify per language pack, since some community-contributed packs differ). |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU-only; OCR time is roughly linear in page count. Language packs are small. Among the cheapest capabilities in the catalogue.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE
- https://github.com/tesseract-ocr/tesseract
- https://tesseract-ocr.github.io/

---

## 1. Purpose

LSTM line-recognition OCR engine for 100+ languages with a CLI and the libtesseract C/C++ API, outputting text, hOCR, ALTO, TSV and searchable PDF, and trainable for new scripts.

## Journalism / investigative use case

Baseline fully offline OCR for scanned court filings, FOIA releases and paper archives — and more importantly, the engine underneath OCRmyPDF, Tika, ICIJ extract and Datashare, so its behaviour determines the text quality of most document pipelines you will build.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- The de facto standard: understanding Tesseract's behaviour means understanding the text quality of almost every open document pipeline, because they all wrap it
- Fully offline with 100+ language packs, CPU-only, and packaged in every distro — effectively zero friction to deploy anywhere, including air-gapped
- Apache-2.0 for both the engine and the tessdata traineddata from the same project, so there is no licence complication
- Still actively released (5.5.4, 2026-10-28) after decades, with 77,561 stars and a managed backlog

## 5. Cons

- Weak on handwriting and badly degraded scans — the ceiling that drives teams to Surya, Kraken or commercial OCR, and no amount of preprocessing removes it
- No layout or table-structure output beyond hOCR bounding boxes, so structure must come from another stage
- Per-language quality varies a lot, and the 'best' versus 'fast' traineddata choice materially changes both accuracy and runtime in ways that are not obvious
- 490 open issues; the project is maintained but changes slowly, and accuracy improvements come from newer neural OCR elsewhere

## 6. Feedback (documented)

No individual user reports verified. The adoption evidence is structural and verifiable from dependency declarations: OCRmyPDF, Apache Tika's OCR path, ICIJ extract, Datashare and Paperless-ngx all use Tesseract. 77,561 stars with 490 open issues and a release on 2026-10-28.

## 7. Assessment

Adopt by default, via OCRmyPDF rather than directly — the wrapper handles the preprocessing and PDF assembly you would otherwise write badly. For your profile the key judgement is knowing when to escalate: if Tesseract's output on a corpus is poor, no tuning will fix handwriting or heavy degradation, and the right move is Kraken (handwriting) or Surya/Marker (complex print) for that subset rather than more preprocessing.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release 5.5.4 (2026-10-28), 77,561 stars, 490 open issues. Current commits and point releases on the 5.x line from a community team; long-term stability is the defining characteristic.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Apache-2.0 for tessdata traineddata from the same project (verify per language pack, since some community-contributed packs differ).

**Restrictions:** None material.

**Licence evidence:** https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE

## 10. Costs

No fee. CPU-only; OCR time is roughly linear in page count. Language packs are small. Among the cheapest capabilities in the catalogue.

## 11. Privacy and data flows

Fully local with no network at inference. Language-pack downloads are the only external fetch and can be pre-staged.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [OCRmyPDF](JAI-A2-33.md) as the wrapper you should actually use
- [Surya](JAI-A2-52.md)/Marker where print accuracy is the constraint
- [Kraken](JAI-A2-26.md) for handwriting; PaddleOCR for CJK and Arabic

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/tesseract-ocr/tesseract
- https://tesseract-ocr.github.io/
- https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE

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

← 98. [RAGFlow](JAI-A3-06.md) · 100. [txtai](JAI-A2-55.md) →
