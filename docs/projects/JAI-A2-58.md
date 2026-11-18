# Whisper

`JAI-A2-58` · **88/100** · overall rank 52 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 20) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 12) |
| **Subcategory** | Transcription (reference model) |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenAI |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/openai/whisper) · [Documentation](https://github.com/openai/whisper#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 88/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | MIT (weights). |
| **Restrictions** | None — unusually clean for a model of this capability. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. GPU with ~10GB VRAM for large-v3, or slow CPU inference. Note the separate OpenAI hosted Whisper API is a paid service under OpenAI's terms — a different thing from these weights, and inappropriate for sensitive audio.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/openai/whisper/blob/main/LICENSE
- https://github.com/openai/whisper

---

## 1. Purpose

Encoder-decoder speech model trained on 680,000 hours of multilingual audio, performing transcription, language identification and speech translation, released with MIT code and MIT weights.

## Journalism / investigative use case

Baseline transcription of interviews and leaked audio where model provenance matters, and the canonical implementation that nearly every newsroom transcription tool wraps — so its documented failure modes are the failure modes you will encounter whichever wrapper you deploy.

## 2. Audience

engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- MIT weights as well as MIT code — a genuinely unrestricted model, which is rare and removes every commercial-publication concern
- Multilingual performance across many languages from a single model, so one deployment covers a cross-border newsroom
- Reference status means every wrapper, benchmark and bug report in the ecosystem is interpretable against it
- Still the baseline against which newer ASR is measured, so quality is well characterised rather than claimed

## 5. Cons

- Documented hallucination on silence and poor recordings is the critical journalism risk: Whisper can emit fluent, plausible, entirely invented sentences, which is far more dangerous than a garbled transcript
- No speaker diarisation and only approximate word timestamps, so quote verification needs WhisperX or forced alignment
- large-v3 needs roughly 10GB VRAM, and the reference implementation is much slower than faster-whisper or whisper.cpp for the same output
- Repository has slowed: pushed 2026-08-31 with the last release v20250625 (2025-06-26) — OpenAI's attention is elsewhere, and the ecosystem forks are where development happens

## 6. Feedback (documented)

No individual user reports verified in this survey, but Whisper's hallucination behaviour on silence and low-quality audio is a widely documented phenomenon discussed extensively in the project's issue tracker and in published evaluations — I am treating it as an established property of the model rather than an anecdote. 112,964 stars, 186 open issues.

## 7. Assessment

Use the weights, not this implementation: faster-whisper or whisper.cpp give the same output far more efficiently. The operationally important point for your work is procedural rather than technical — any Whisper-derived transcript used for quotation must be checked against the audio at the quoted passage, because the model's failure mode is fluent invention. VAD preprocessing (which faster-whisper includes) materially reduces but does not eliminate this.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-08-31, latest release v20250625 (2025-06-26), 112,964 stars, 186 open issues. Nearly 17 months without a release and ~2.5 months since last push. Classified stable-low rather than declining because the artefact that matters — the weights — is final and unchanging, and the ecosystem maintains the tooling; but do not expect fixes from this repository.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** MIT (weights).

**Restrictions:** None — unusually clean for a model of this capability.

**Licence evidence:** https://github.com/openai/whisper/blob/main/LICENSE

## 10. Costs

No fee. GPU with ~10GB VRAM for large-v3, or slow CPU inference. Note the separate OpenAI hosted Whisper API is a paid service under OpenAI's terms — a different thing from these weights, and inappropriate for sensitive audio.

## 11. Privacy and data flows

Fully local inference after weight download; no audio leaves the machine. The confusion to guard against is between these local weights and OpenAI's hosted transcription API, which does transmit audio.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [faster-whisper](JAI-A2-17.md) for the same weights with much better throughput
- [whisper.cpp](JAI-A2-59.md) for CPU and field hardware
- NVIDIA Parakeet (CC-BY-4.0) for higher English accuracy

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/openai/whisper
- https://github.com/openai/whisper/blob/main/LICENSE

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

← 51. [WhisperX](JAI-A2-60.md) · 53. [yente](JAI-A2-61.md) →
