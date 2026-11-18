# PaddleOCR / PP-StructureV3

`JAI-A2-37` · **78/100** · overall rank 175 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 70) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 43) |
| **Subcategory** | OCR and document structure |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | PaddlePaddle (Baidu) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (code) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/PaddlePaddle/PaddleOCR) · [Documentation](https://paddlepaddle.github.io/PaddleOCR/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 (code) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | NOT verified. Per-model weights are distributed via HuggingFace/ModelScope and were not individually confirmed as of 2026-11-17. |
| **Restrictions** | Code permissive. Unresolved uncertainty at the weights layer — check the specific model card before commercial redistribution. Do not assume the Apache-2.0 code licence covers the weights. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. CPU inference is workable; GPU is much faster for bulk. First run fetches weights (can be pre-staged). Engineering time for the PaddlePaddle runtime is the real cost. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/PaddlePaddle/PaddleOCR/blob/main/LICENSE
- https://github.com/PaddlePaddle/PaddleOCR
- https://paddlepaddle.github.io/PaddleOCR/

---

## 1. Purpose

OCR and document-structure toolkit covering text detection and recognition in 80+ languages, plus PP-Structure for layout analysis, table recognition and key-information extraction.

## Journalism / investigative use case

The strongest open option for Chinese, Arabic and Cyrillic document sets — a real gap in Tesseract's practical quality — and for turning scanned reports with tables into structured output on self-hosted hardware, for example Chinese corporate filings or Russian procurement scans.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Non-Latin script accuracy, particularly Chinese, is materially better than Tesseract and is the specific reason to carry this dependency
- PP-StructureV3 bundles layout analysis, table recognition and key-information extraction, covering a pipeline that would otherwise need several tools
- Apache-2.0 code with an enormous user base (92,800 stars) and a manageable issue count (266), indicating real triage
- Runs locally on CPU or GPU with pre-stageable weights, so it fits an isolated processing environment

## 5. Cons

- The PaddlePaddle runtime is heavier and less familiar than PyTorch; dependency conflicts and platform-specific build problems are the common complaint and cost real engineering time
- Model weights were not individually verified: code is Apache-2.0 but per-model weights are distributed via HuggingFace/ModelScope and their terms need per-model checking before commercial redistribution
- Last push 2026-09-16 with the latest release v3.7.0 (2026-06-11) — still recent but the slowest cadence among the leading OCR projects here
- Documentation quality varies between Chinese and English versions, and the English docs lag

## 6. Feedback (documented)

No individual user reports verified. Documented: 92,800 stars with 266 open issues — one of the most-starred projects in the catalogue with evidence of active triage. The weights-licensing uncertainty is an explicit gap carried forward from session 1 and not resolved here.

## 7. Assessment

Carry it specifically for CJK, Arabic and Cyrillic material, where it earns its install weight; do not make it your general OCR default over OCRmyPDF/Tesseract or Docling, because the runtime burden is not justified for Latin-script work. Before any commercial publication built on its structured output, verify the licence of the specific model weights you downloaded — that is the one open risk in this entry.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-16, latest release v3.7.0 (2026-06-11), 92,800 stars, 266 open issues. Two months since last push and five since the last release — slower than peers but well within normal for a 3.x line with corporate backing. Classified active, with cadence noted.

## 9. Licensing

**Licence:** Apache-2.0 (code) _(SPDX verified)_

**Model / data licence:** NOT verified. Per-model weights are distributed via HuggingFace/ModelScope and were not individually confirmed as of 2026-11-17.

**Restrictions:** Code permissive. Unresolved uncertainty at the weights layer — check the specific model card before commercial redistribution. Do not assume the Apache-2.0 code licence covers the weights.

**Licence evidence:** https://github.com/PaddlePaddle/PaddleOCR/blob/main/LICENSE

## 10. Costs

No fee. CPU inference is workable; GPU is much faster for bulk. First run fetches weights (can be pre-staged). Engineering time for the PaddlePaddle runtime is the real cost. Estimate.

## 11. Privacy and data flows

Local inference; first run fetches weights from HuggingFace/ModelScope, which can be done once and staged offline. No inference-time calls, so documents stay local.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Surya](JAI-A2-52.md) or Marker for Latin-script accuracy with simpler dependencies
- Tesseract via OCRmyPDF as the reliable baseline
- [Docling](JAI-A2-12.md) where a permissive and verified weights position is required

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/PaddlePaddle/PaddleOCR
- https://paddlepaddle.github.io/PaddleOCR/
- https://github.com/PaddlePaddle/PaddleOCR/blob/main/LICENSE

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

← 174. [OpenSecrets lobbying data](SUR-B2-17.md) · 176. [PyBGPStream / libbgpstream](SUR-B1-08.md) →
