# whisper.cpp

`JAI-A2-59` · **94/100** · overall rank 18 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 5) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 2) |
| **Subcategory** | Transcription (CPU runtime) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Georgi Gerganov / ggml-org |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ggml-org/whisper.cpp) · [Documentation](https://github.com/ggml-org/whisper.cpp#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 94/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | MIT (Whisper weights converted to GGML/GGUF). |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Runs on existing CPUs; model files are a few hundred MB to a few GB. Effectively zero marginal cost, which is a significant advantage for a small newsroom.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ggml-org/whisper.cpp/blob/master/LICENSE
- https://github.com/ggml-org/whisper.cpp

---

## 1. Purpose

Plain C/C++ implementation of Whisper inference using the ggml tensor library, with quantised GGUF models, no Python dependency, and backends for CPU, Metal, CUDA, Vulkan and OpenVINO.

## Journalism / investigative use case

Transcribing suspect audio and video locally so the words in a claimed 'leaked recording' can be checked, searched and quoted without uploading sensitive material to any service — and because it needs no Python, it runs on a hardened or borrowed machine where installing a toolchain is not an option.

## 2. Audience

engineer, journalist

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- No Python and no dependency hell: a single binary plus a model file, which is the most deployable transcription stack here and the right choice for a locked-down or borrowed laptop
- Quantised GGUF models run usably on ordinary CPUs and on Apple Silicon via Metal, removing the GPU requirement entirely
- Extremely active (pushed 2026-11-17, release v1.9.5 2026-10-06) with 55,264 stars and a large but managed backlog
- MIT code and MIT weights, so no licensing friction at all

## 5. Cons

- No built-in diarisation, so multi-speaker material needs a separate pipeline
- Quantisation trades accuracy for speed in ways that are model- and language-dependent, and the trade-off is not well documented for minority languages
- API churn across releases can break downstream wrappers — a recurring complaint given how many tools embed it (373 open issues)
- Still inherits Whisper's hallucination behaviour; the runtime does not fix the model's failure mode

## 6. Feedback (documented)

No individual user reports verified. Documented: 55,264 stars with 373 open issues and a release on 2026-10-06; whisper.cpp is embedded in Buzz, Subtitle Edit and numerous desktop tools, which is verifiable from those projects and is strong evidence of practical reliability.

## 7. Assessment

The transcription runtime I would standardise on for anything that must run on arbitrary hardware — field laptops, hostile-environment machines, a reporter's borrowed computer. For server-side batch work faster-whisper is better. The combination of 'single binary, no network, MIT weights' is uniquely well matched to media-in-exile constraints, and it is worth packaging a known-good binary plus model internally so reporters never download anything at the moment of need.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.9.5 (2026-10-06), 55,264 stars, 373 open issues. Daily commits and regular releases; the backlog reflects the number of platforms and wrappers rather than neglect.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** MIT (Whisper weights converted to GGML/GGUF).

**Restrictions:** None.

**Licence evidence:** https://github.com/ggml-org/whisper.cpp/blob/master/LICENSE

## 10. Costs

No fee. Runs on existing CPUs; model files are a few hundred MB to a few GB. Effectively zero marginal cost, which is a significant advantage for a small newsroom.

## 11. Privacy and data flows

Fully local; model files fetched once and then no network at all. The single most deployable privacy-preserving transcription option in the catalogue.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [faster-whisper](JAI-A2-17.md) for server-side batch throughput
- [Buzz](JAI-A2-05.md) for a GUI over this engine
- [sherpa-onnx](JAI-A2-46.md) for embedded and streaming use cases

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ggml-org/whisper.cpp
- https://github.com/ggml-org/whisper.cpp/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 17. [Uwazi](OSINT-C3-05.md) · 19. [OpenAleph](JAI-A2-35.md) →
