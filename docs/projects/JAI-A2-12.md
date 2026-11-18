# Docling

`JAI-A2-12` · **91/100** · overall rank 31 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 9) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 6) |
| **Subcategory** | Document parsing and layout |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | docling-project (IBM Research origin, now LF AI & Data) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/docling-project/docling) · [Documentation](https://docling-project.github.io/docling/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | NOT individually verified. Layout and TableFormer models are distributed via HuggingFace under the docling-project organisation; per-model terms unconfirmed as of 2026-11-17. |
| **Restrictions** | Code is unrestricted. Residual uncertainty at the weights layer — confirm the licence of each model you pull before relying on it for commercial publication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. CPU-viable for born-digital documents; a GPU materially helps the VLM pipelines and large scanned batches. First run downloads models from HuggingFace (one-off egress; can be pre-staged). Infrastructure estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/docling-project/docling/blob/main/LICENSE
- https://github.com/docling-project/docling
- https://docling-project.github.io/docling/

---

## 1. Purpose

Document conversion library that parses PDF, DOCX, PPTX, XLSX, HTML and images into a unified DoclingDocument model with layout, reading order and table structure, exporting to Markdown, JSON and HTML.

## Journalism / investigative use case

Permissively licensed, fully local parsing for sensitive leaks where even model-weight restrictions are unacceptable — the key differentiator against Marker/Surya. The unified document model with page provenance means you can cite 'page 14, table 2' back to the original, which matters when an extraction becomes evidence.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- MIT code with layout and TableFormer models published by the project itself — the only strong layout-aware parser in this catalogue without an OpenRAIL-M or revenue-threshold condition
- Unified DoclingDocument model preserves reading order, table structure and page provenance, which is what makes repeatable newsroom ingest possible
- Backed by LF AI & Data with a very high release cadence (v2.150.1, 2026-11-14) and 70,691 stars — exceptional institutional and community momentum
- Pluggable OCR backends (Tesseract, EasyOCR, RapidOCR) and optional VLM pipelines, so you can trade accuracy for speed per corpus

## 5. Cons

- The release cadence is itself a cost: API churn across 2.x point releases means pinning is mandatory and upgrades need regression tests on your own documents
- OCR quality is entirely the plugged-in backend's — Docling does not fix Tesseract's weakness on degraded scans
- Model licences were not individually verified in this survey: layout and TableFormer weights are distributed via HuggingFace under the docling-project org and per-model terms remain unconfirmed, so the 'fully permissive' claim is strong for code and probable but unverified for weights
- 1,071 open issues; at this growth rate support is diluted and you should expect to read source

## 6. Feedback (documented)

No individual user reports verified. The quantitative signals are strong and checkable: 70,691 stars and a release on 2026-11-14 indicate rapid adoption. The 1,071 open issues are documented evidence of support strain. No journalism-specific deployment verified.

## 7. Assessment

My recommended default parser for sensitive material, specifically because it sidesteps the weights-licence problem that makes Marker and Surya awkward for a commercially operated newsroom. Two conditions: pin the version, and verify the specific model weights you download rather than inheriting my 'probable' assessment. If you need maximum accuracy on messy multi-column scans and your revenue is under Datalab's threshold, Marker may still beat it — evaluate both on your own documents.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2.150.1 (2026-11-14), 70,691 stars, 1,071 open issues. Release-per-week cadence plus LF AI & Data governance; the maintenance question here is churn, not neglect.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** NOT individually verified. Layout and TableFormer models are distributed via HuggingFace under the docling-project organisation; per-model terms unconfirmed as of 2026-11-17.

**Restrictions:** Code is unrestricted. Residual uncertainty at the weights layer — confirm the licence of each model you pull before relying on it for commercial publication.

**Licence evidence:** https://github.com/docling-project/docling/blob/main/LICENSE

## 10. Costs

No fee. CPU-viable for born-digital documents; a GPU materially helps the VLM pipelines and large scanned batches. First run downloads models from HuggingFace (one-off egress; can be pre-staged). Infrastructure estimate.

## 11. Privacy and data flows

Local processing. Two external touchpoints to manage: first-run model download from HuggingFace, and the optional remote VLM backends, which send page content to whatever endpoint you configure. Both are controllable; neither is on by default for the standard pipeline.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Marker](JAI-A2-28.md) for peak accuracy if the Datalab weights threshold is acceptable
- [Apache Tika](JAI-A2-02.md) for format breadth without layout
- [Unstructured](JAI-A1-10.md) as a competing Python-native parser (check its licence tiers)

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/docling-project/docling
- https://docling-project.github.io/docling/
- https://github.com/docling-project/docling/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 30. [ArchiveBox](OSINT-C1-28.md) · 32. [noScribe](JAI-A2-31.md) →
