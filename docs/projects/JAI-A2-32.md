# NVIDIA NeMo Speech

`JAI-A2-32` · **73/100** · overall rank 240 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 97) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 51) |
| **Subcategory** | Transcription and diarisation framework |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | NVIDIA (repository reorganised from NVIDIA/NeMo to NVIDIA-NeMo/Speech) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (code) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/NVIDIA-NeMo/Speech) · [Documentation](https://docs.nvidia.com/nemo-framework/) |

**Scores** — relevance 3/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 2/5 · licence+cost 2/5 → **weighted 73/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Framework for training and running speech models — ASR (Parakeet, Canary), speaker diarisation (Sortformer), speech translation — with pretrained checkpoints distributed via HuggingFace and NVIDIA NGC.

## Journalism / investigative use case

High-accuracy English transcription and diarisation at archive scale, and the most realistic route to fine-tuning an ASR model on a dialect, accent or domain jargon that a specific investigation requires — for example months of regional-language broadcast monitoring where Whisper's accuracy is unacceptable.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Parakeet-class models lead open English ASR benchmarks and Sortformer is a genuine step up on diarisation accuracy over pyannote in published evaluations
- Fine-tuning is a first-class, documented workflow — the only practical option here if you need a model adapted to a specific accent or vocabulary
- Apache-2.0 code with institutional backing and very active development (pushed 2026-11-17, v3.0.0 2026-08-07)
- Covers ASR, diarisation and speech translation in one framework, reducing stack sprawl for a speech-heavy newsroom

## 5. Cons

- Checkpoint licences vary and the variation is material: nvidia/parakeet-tdt-0.6b-v2 is CC-BY-4.0 (commercial use allowed) while nvidia/diar_sortformer_4spk-v1 is CC-BY-NC-4.0 (non-commercial only), both read from the HuggingFace cards 2026-11-16 — so the best diarisation model is unusable in commercially published journalism
- NVIDIA-GPU-centric: no realistic CPU path, and the dependency stack is heavy
- The repository was reorganised (NVIDIA/NeMo now redirects to NVIDIA-NeMo/Speech), so older documentation, pinned paths and tutorials point at the previous structure
- 462 open issues and a steep learning curve; this is a research framework, not a tool

## 6. Feedback (documented)

No individual user reports verified. Documented, checkable: the split checkpoint licensing recorded from the HuggingFace model cards (CC-BY-4.0 for parakeet-tdt-0.6b-v2, CC-BY-NC-4.0 for diar_sortformer_4spk-v1); and the repository transfer confirmed via the GitHub API this session. 18,760 stars, 462 open issues.

## 7. Assessment

Worth it only if speech is central to your work and you have GPU capacity — otherwise faster-whisper plus pyannote is far less effort. The licence asymmetry is the decisive planning fact: you can publish commercially using Parakeet transcription, but not using Sortformer diarisation, so a commercially operated newsroom should pair Parakeet with pyannote rather than taking NeMo's full stack. Fine-tuning capability is the genuine unique value; budget real engineering time for it.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.0.0 (2026-08-07), 18,760 stars, 462 open issues. Daily commits with corporate backing; the repository reorganisation itself indicates active restructuring rather than drift.

## 9. Licensing

**Licence:** Apache-2.0 (code) _(SPDX verified)_

**Model / data licence:** VARIES AND MATTERS: nvidia/parakeet-tdt-0.6b-v2 = CC-BY-4.0 (commercial allowed); nvidia/diar_sortformer_4spk-v1 = CC-BY-NC-4.0 (non-commercial only). Read from HuggingFace cards 2026-11-16.

**Restrictions:** CC-BY-NC-4.0 on Sortformer diarisation weights bars use in commercially published journalism unless separately licensed or substituted. Do not assume NGO or non-profit status satisfies NonCommercial — it does not, where the output is commercially published.

**Licence evidence:** https://huggingface.co/nvidia/diar_sortformer_4spk-v1

## 10. Costs

No software fee. Requires NVIDIA GPU hardware or cloud GPU rental — the dominant cost, and fine-tuning multiplies it. Checkpoints are free to download. Infrastructure estimate; assumes self-hosted or rented GPU, no vendor licence.

## 11. Privacy and data flows

Local inference and training; checkpoints downloaded from NGC/HuggingFace. No inference-time external calls, so audio stays on your hardware.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- CC-BY-NC-4.0 on the Sortformer diarisation checkpoint — commercial-publication blocker for that specific model

## 13. Alternatives

- [faster-whisper](JAI-A2-17.md) plus pyannote for a lighter, licence-clean stack
- [sherpa-onnx](JAI-A2-46.md) for field and offline devices
- [Whisper](JAI-A2-58.md) large-v3 where fine-tuning is not needed

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/NVIDIA-NeMo/Speech
- https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2
- https://huggingface.co/nvidia/diar_sortformer_4spk-v1
- `../sources/evidence/leads.md`

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

← 239. [SAM.gov](SUR-B2-15.md) · 241. [Kraken](JAI-A2-26.md) →
