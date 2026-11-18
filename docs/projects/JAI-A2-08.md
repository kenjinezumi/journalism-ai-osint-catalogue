# CTranslate2

`JAI-A2-08` · **84/100** · overall rank 114 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 48) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 28) |
| **Subcategory** | Local inference runtime |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenNMT / SYSTRAN |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Mixed |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/OpenNMT/CTranslate2) · [Documentation](https://opennmt.net/CTranslate2/) |

**Scores** — relevance 3/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Engine only. Converted weights retain the licence of the source model — converting a CC-BY-NC checkpoint does not make it permissive. |
| **Restrictions** | None from the engine. The frequent error is assuming the MIT engine licence launders a restricted model licence; it does not. |
| **Open-source status** | **Mixed** — Open-source code, data or models you load carrying their own terms, some non-commercial |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. The point of the project is to reduce infrastructure cost: CPU-only int8 inference on existing laptops versus GPU rental. Optional CUDA path needs a GPU. Estimate; assumes self-hosted.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/OpenNMT/CTranslate2/blob/master/LICENSE
- https://github.com/OpenNMT/CTranslate2
- https://opennmt.net/CTranslate2/

---

## 1. Purpose

C++/Python inference engine for transformer models with aggressive quantisation (int8, int16, float16), used to run translation and speech models far faster and smaller than the reference PyTorch implementations.

## Journalism / investigative use case

The engine that makes offline AI practical on newsroom hardware: int8 quantisation lets a 600M-1.3B translation model or Whisper large run on a CPU laptop instead of a cloud API, which is what turns 'we should process this locally' into something that actually finishes before deadline.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- The quantisation story is the decisive capability — it changes the hardware class needed, and therefore whether local processing is viable at all for a small newsroom
- Powers faster-whisper and Argos/LibreTranslate, so its reliability is already proven in the tools your reporters would use
- Active releases (v4.9.0, 2026-11-10) with CPU and CUDA backends maintained in parallel
- Small, dependency-light C++ core that you can actually build and audit

## 5. Cons

- Engineer-facing only: no UI, no file handling, and you must convert the model yourself with the source framework installed
- Quantisation costs measurable quality, and the loss is model- and language-dependent, so you need to evaluate rather than assume
- 276 open issues, and CUDA/cuDNN version mismatches are a recurring install failure that you will debug
- Supports a specific set of architectures — a new model family is not guaranteed to be convertible

## 6. Feedback (documented)

No individual user reports collected. Strong indirect evidence: faster-whisper (26.8k stars) and the Argos/LibreTranslate line both depend on CTranslate2, which is verifiable from their dependency declarations and constitutes real production use.

## 7. Assessment

For your profile this is foundational plumbing rather than a tool you use directly: you will meet it through faster-whisper and Argos. Install it directly when you need to run a specific translation model (NLLB, MADLAD) that no wrapper exposes, or when you need to squeeze a model onto field hardware. Budget evaluation time to measure the quantisation quality loss on your actual languages — do not accept it on faith.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-10, latest release v4.9.0 published the same day (2026-11-10), 4,755 stars, 276 open issues. A same-day push and release is a clear active signal; the open-issue count reflects breadth of hardware/driver combinations rather than neglect.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Engine only. Converted weights retain the licence of the source model — converting a CC-BY-NC checkpoint does not make it permissive.

**Restrictions:** None from the engine. The frequent error is assuming the MIT engine licence launders a restricted model licence; it does not.

**Licence evidence:** https://github.com/OpenNMT/CTranslate2/blob/master/LICENSE

## 10. Costs

No fee. The point of the project is to reduce infrastructure cost: CPU-only int8 inference on existing laptops versus GPU rental. Optional CUDA path needs a GPU. Estimate; assumes self-hosted.

## 11. Privacy and data flows

Entirely local, no telemetry, no network. One of the cleanest privacy profiles in the catalogue and the basis for the local-first transcription and translation stack.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [llama.cpp](JAI-A3-01.md) / whisper.cpp for GGUF-based local inference
- ONNX Runtime / sherpa-onnx for mobile and locked-down devices
- [vLLM](JAI-A3-03.md) when you have GPUs and need throughput over footprint

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/OpenNMT/CTranslate2
- https://opennmt.net/CTranslate2/
- https://github.com/OpenNMT/CTranslate2/blob/master/LICENSE

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

← 113. [Apache Solr](JAI-A2-01.md) · 115. [Global Fishing Watch API client](OSINT-C2-50.md) →
