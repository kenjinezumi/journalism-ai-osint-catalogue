# olmOCR

`JAI-A2-34` · **72/100** · overall rank 246 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 101) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 54) |
| **Subcategory** | Document parsing (VLM) |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | Allen Institute for AI (AI2) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | Apache-2.0 |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/allenai/olmocr) · [Documentation](https://olmocr.allenai.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 2/5 · privacy 4/5 · usability 2/5 · licence+cost 5/5 → **weighted 72/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Apache-2.0 on the HuggingFace card for allenai/olmOCR-2-7B-1025; fine-tuned from Qwen2.5-VL-7B-Instruct, so Qwen's terms also apply to derivatives. AI2 additionally frames use under its Responsible Use Guidelines. |
| **Restrictions** | No revenue threshold or NC clause found. Residual complexity: the base-model terms flow through, and AI2's guidelines are stated expectations rather than licence conditions. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Requires a GPU host (24GB+ VRAM class for the 7B model with vLLM) — the dominant cost, whether owned or rented. Weights are free. Infrastructure estimate; assumes self-hosted GPU.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://huggingface.co/allenai/olmOCR-2-7B-1025
- https://github.com/allenai/olmocr
- https://olmocr.allenai.org/

---

## 1. Purpose

Vision-language-model pipeline for linearising PDFs into clean text with correct reading order, fine-tuned from Qwen2.5-VL and distributed with open weights plus a batch inference toolkit.

## Journalism / investigative use case

Genuinely open-weights VLM OCR — rare in this category — so a newsroom can run state-of-the-art document linearisation on its own GPU with no licence threshold and no vendor seeing the documents. The practical use is converting large scanned report archives into reliable text where Tesseract garbles multi-column layout.

## 2. Audience

engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- Apache-2.0 weights (allenai/olmOCR-2-7B-1025 HuggingFace card) — the only VLM-OCR option here without an OpenRAIL-M or revenue-threshold condition, which makes it the licence-safe high-accuracy choice
- Reading-order linearisation is the specific strength: multi-column reports and footnote-heavy documents come out in the order a human would read them
- Published with a documented evaluation methodology by a research institute, so quality claims are traceable rather than marketing
- Batch toolkit is designed for corpus-scale processing, not single-document demos

## 5. Cons

- No repository activity since 2026-03-25 — nine months quiet, so the current release should be treated as a snapshot rather than a maintained product
- Requires a sizeable NVIDIA GPU with vLLM or SGLang; not laptop-viable, which excludes it from reporter-facing workflows
- Fine-tuned from Qwen2.5-VL, so Qwen's terms also apply to the derived weights, and AI2 frames use under its Responsible Use Guidelines — a soft-law layer above the Apache-2.0 label
- VLM OCR can hallucinate plausible text where the image is unreadable, which is a more dangerous failure mode than Tesseract's obvious garbage

## 6. Feedback (documented)

No individual user reports verified. Documented: 19,829 stars and 93 open issues indicate strong initial adoption; the nine-month commit gap since 2026-03-25 is the key checkable maintenance fact. AI2's published evaluation is a project claim with methodology disclosed, not independent verification.

## 7. Assessment

Attractive on licensing and quality but the maintenance gap makes it a conditional choice: I would use it for a defined batch job on a specific archive, pinning the release, rather than building a standing pipeline on it. For your profile the Apache-2.0 weights are the reason to prefer it over Marker when your organisation exceeds Datalab's threshold. Add a verification step — VLM hallucination means a spot-check protocol against page images is mandatory before any extracted text is quoted.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-03-25, latest release v0.4.27 (2026-03-12), 19,829 stars, 93 open issues. No commits for nearly nine months against substantial adoption and an open backlog. Classified declining rather than dormant because the project is recent and institutionally owned, but there is no evidence of ongoing work and no deprecation statement either way.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Apache-2.0 on the HuggingFace card for allenai/olmOCR-2-7B-1025; fine-tuned from Qwen2.5-VL-7B-Instruct, so Qwen's terms also apply to derivatives. AI2 additionally frames use under its Responsible Use Guidelines.

**Restrictions:** No revenue threshold or NC clause found. Residual complexity: the base-model terms flow through, and AI2's guidelines are stated expectations rather than licence conditions.

**Licence evidence:** https://huggingface.co/allenai/olmOCR-2-7B-1025

## 10. Costs

No fee. Requires a GPU host (24GB+ VRAM class for the 7B model with vLLM) — the dominant cost, whether owned or rented. Weights are free. Infrastructure estimate; assumes self-hosted GPU.

## 11. Privacy and data flows

Local inference once weights are downloaded; no external calls. Fully compatible with an isolated processing environment, which is its main advantage over hosted document AI.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- No repository activity since March 2026 — do not build a long-lived pipeline on it without accepting fork responsibility

## 13. Alternatives

- [Docling](JAI-A2-12.md) for a maintained, licence-clean, CPU-viable alternative
- [Marker](JAI-A2-28.md) for higher accuracy if the Datalab weights threshold is acceptable
- [Surya](JAI-A2-52.md) for the layout/OCR models without a full VLM

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/allenai/olmocr
- https://huggingface.co/allenai/olmOCR-2-7B-1025
- https://olmocr.allenai.org/

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

← 245. [py-wacz](OSINT-C1-43.md) · 247. [asn (nitefood)](OSINT-C3-27.md) →
