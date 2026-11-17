# Kraken

`JAI-A2-26` · **73/100** · overall rank 241 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 98) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 52) |
| **Subcategory** | Handwritten and historical OCR |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Benjamin Kiessling (mittagessen) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mittagessen/kraken) · [Documentation](https://kraken.re/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 73/100**

---

## 1. Purpose

Trainable OCR and handwritten-text-recognition engine with baseline segmentation, support for right-to-left and bidirectional scripts, and ALTO/PAGE XML output.

## Journalism / investigative use case

The practical open engine for archival investigations — handwritten registers, ledgers, colonial-era records, Arabic and Hebrew manuscripts — where a model fine-tuned on a few hundred transcribed lines of the specific hand turns an unreadable archive into searchable text.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Fine-tuning on a small ground-truth set is the capability that matters: generic OCR fails on a specific hand, and Kraken is designed for exactly that adaptation
- First-class support for right-to-left and bidirectional scripts, a genuine gap in Tesseract's practical quality
- Outputs ALTO and PAGE XML, so transcriptions feed archival search systems and remain usable long term
- Current releases (7.1, 2026-08-05) and a clean tracker (29 open issues) for a specialist tool

## 5. Cons

- Steep learning curve: segmentation models, recognition models and ground-truth formats are all concepts you must learn before results improve
- Accuracy on an unseen hand usually requires fine-tuning with manually transcribed lines — the human cost is the real cost, often days of transcription
- Public models are published on Zenodo with per-model terms that vary and were not individually verified, so licence diligence is per model
- CLI-only; a team workflow requires eScriptorium on top, which is a much larger deployment

## 6. Feedback (documented)

No user reports collected. Documented context: Kraken is the recognition engine behind eScriptorium and the standard choice in digital-humanities HTR — strong adjacent-field adoption evidence, no verified journalism deployment.

## 7. Assessment

Use it when the material is handwritten or in a non-Latin historical script and nothing else works; otherwise Tesseract, Surya or PaddleOCR will cost you far less. For your profile the deciding question is whether you have the human capacity to produce ground truth — without that, Kraken's main advantage is unavailable and you are better off with a general OCR engine plus manual reading.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-10, latest release 7.1 (2026-08-05), latest tag 7.1.1, 1,107 stars, 29 open issues. Major-version releases on a regular cadence from a single academic maintainer; low issue count indicates attention. Single-maintainer bus factor is the risk, not activity.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Varies by model — public models are published on Zenodo with per-model terms; not individually verified in this survey.

**Restrictions:** Code permissive. Verify the licence of each Zenodo-published model before commercial use; some academic models carry non-commercial or attribution conditions.

**Licence evidence:** https://github.com/mittagessen/kraken/blob/main/LICENSE

## 10. Costs

No fee. A GPU materially accelerates training and inference. The dominant cost is human transcription to build ground truth — budget days of specialist labour per hand. Estimate.

## 11. Privacy and data flows

Local; optional model fetch from Zenodo is the only network event. Suitable for sensitive archives on isolated hardware.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [eScriptorium](JAI-A2-15.md) for a collaborative team interface over the same engine
- Transkribus as a hosted alternative with published pricing — but it moves material to a third party
- [Surya](JAI-A2-52.md) or PaddleOCR for printed or modern typeset material

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/mittagessen/kraken
- https://kraken.re/
- https://github.com/mittagessen/kraken/blob/main/LICENSE

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

← 240. [NVIDIA NeMo Speech](JAI-A2-32.md) · 242. [sherpa-onnx](JAI-A2-46.md) →
