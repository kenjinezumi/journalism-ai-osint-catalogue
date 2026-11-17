# faster-whisper

`JAI-A2-17` · **87/100** · overall rank 64 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 25) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 16) |
| **Subcategory** | Transcription (library) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | SYSTRAN (transferred from guillaumekln) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/SYSTRAN/faster-whisper) · [Documentation](https://github.com/SYSTRAN/faster-whisper#readme) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 87/100**

---

## 1. Purpose

Reimplementation of Whisper inference on CTranslate2, delivering several-fold throughput and memory improvements over the reference implementation, with batched inference and Silero VAD integration.

## Journalism / investigative use case

Bulk processing of large audio archives — a press-conference backlog, months of monitored broadcast, a seized recording collection — where throughput per GPU-hour decides whether the investigation is affordable at all.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Throughput and memory profile are the decisive practical advantage: the same GPU budget transcribes several times more audio than reference Whisper
- Integrated VAD removes long silences, which both speeds processing and reduces Whisper's well-known tendency to hallucinate text over silence
- 26,821 stars with only 21 open issues — an exceptionally clean tracker indicating real triage, and the strongest maintenance signal in the transcription subcategory
- MIT code and MIT weights, so there is no licence friction for commercial publication

## 5. Cons

- No speaker diarisation — you must add pyannote or WhisperX, and that pulls in HuggingFace gating
- The latest release (v1.2.1, 2025-10-31) predates roughly a year of commits, so pinning to a release loses fixes while tracking main loses reproducibility; this is a real operational annoyance
- CUDA/cuDNN version mismatches are the standard install failure, and the error messages are unhelpful
- Repository was transferred from guillaumekln to SYSTRAN — the old URL redirects, but SBOMs, pinned git URLs and provenance records should be updated to the canonical path

## 6. Feedback (documented)

No individual user reports verified. Documented signals: 21 open issues against 26.8k stars (strong triage evidence); and the project's own README documents the benchmark claims, which are project claims rather than independently verified measurements. Widely used as the backend of Buzz and WhisperX, verifiable from those projects' dependencies.

## 7. Assessment

The default engine for any batch transcription work you build, with the caveat that you must decide explicitly between a stale release tag and a moving main branch — I would pin a specific commit and record it in the pipeline's provenance notes. Combine with pyannote for diarisation only if you can accept the HuggingFace gate; otherwise accept unlabelled speakers. Repository transfer verified in this session: guillaumekln/faster-whisper now redirects to SYSTRAN/faster-whisper.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-12, latest release v1.2.1 (2025-10-31), latest tag v1.2.1, 26,821 stars, 21 open issues. The near-empty issue tracker alongside recent commits is the key evidence; the year-old release tag is a release-hygiene gap, not evidence of abandonment.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** MIT — Whisper weights, CTranslate2-converted.

**Restrictions:** None material.

**Licence evidence:** https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE

## 10. Costs

No fee. Cost is compute: a single mid-range NVIDIA GPU transcribes faster than real time by a wide margin, so a modest on-prem GPU is usually cheaper than per-minute commercial ASR for sustained volume. CPU int8 works for light use. Infrastructure estimate; assumes self-hosted GPU and large-v3-class model.

## 11. Privacy and data flows

Local inference; audio never leaves the machine. The only network event is the first-run weights download from HuggingFace, which can be pre-staged for air-gapped operation.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [whisper.cpp](JAI-A2-59.md) for CPU-only and field hardware
- [WhisperX](JAI-A2-60.md) when you need diarisation and word-level alignment
- [NVIDIA NeMo Speech](JAI-A2-32.md) for peak English accuracy — but check the per-checkpoint licence, some are CC-BY-NC

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/SYSTRAN/faster-whisper
- https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE
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

← 63. [Apache Tika](JAI-A2-02.md) · 65. [Splink](JAI-A2-48.md) →
