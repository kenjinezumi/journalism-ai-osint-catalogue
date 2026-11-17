# WhisperX

`JAI-A2-60` · **88/100** · overall rank 51 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 19) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 11) |
| **Subcategory** | Transcription with alignment and diarisation |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Max Bain (m-bain) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/m-bain/whisperX) · [Documentation](https://github.com/m-bain/whisperX#readme) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 88/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Pipeline combining faster-whisper transcription, wav2vec2 forced alignment for word-level timestamps, VAD-based batching and pyannote speaker diarisation.

## Journalism / investigative use case

Producing quote-accurate, speaker-attributed transcripts of multi-party interviews and hearings where you must jump to the exact second a phrase was spoken to verify it — the combination that turns a machine transcript into something an editor can check line by line.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Word-level timestamps from forced alignment are materially more accurate than Whisper's native estimates, which is what makes quote verification practical at scale
- Bundles the three stages (transcribe, align, diarise) that every newsroom audio pipeline needs, saving substantial integration work
- BSD-2-Clause and actively released (v3.8.6, 2026-05-25) with 25,401 stars
- VAD-based batching gives a large throughput gain over sequential processing

## 5. Cons

- Heavy dependency stack (faster-whisper, pyannote.audio, torchaudio, ffmpeg) and ~10GB VRAM for large-v3 plus diarisation — the most demanding transcription option here
- Diarisation inherits pyannote's weaknesses: it degrades on overlapping speech and telephone-band audio, which describes much covertly recorded material
- Alignment-model coverage is uneven outside major languages, so word-level timing quality varies by language in a way that is easy to overlook
- Obtaining diarisation weights requires accepting pyannote's HuggingFace gate, which discloses your identity to the model authors

## 6. Feedback (documented)

No individual user reports verified. Documented: 25,401 stars, 219 open issues, last release v3.8.6 (2026-05-25) with commits through 2026-11-12. The HuggingFace gating requirement is documented on pyannote's model card and is the most commonly reported setup obstacle for this project.

## 7. Assessment

The right choice for an engineer-run interview and hearing pipeline, and the one I would build on for any investigation where quotes must be verifiable to the second. For your profile: pre-fetch the pyannote weights centrally, pin the whole stack in a container because the dependency graph is fragile, and check alignment quality explicitly for each non-major language before trusting the timestamps editorially.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-12, latest release v3.8.6 (2026-05-25), 25,401 stars, 219 open issues. Current commits with a release about six months old; active but with a slower release cadence than its dependencies, so pinning matters.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** Mixed: Whisper MIT; wav2vec2 aligners vary by language; pyannote diarisation weights MIT but gated on HuggingFace.

**Restrictions:** No field-of-use restrictions found. The practical constraint is the pyannote access gate; check individual wav2vec2 aligner licences for less common languages.

**Licence evidence:** https://github.com/m-bain/whisperX/blob/main/LICENSE

## 10. Costs

No fee. GPU with ~10GB VRAM recommended; CPU operation is impractical for the full pipeline. One GPU host serves a small newsroom's audio needs. Infrastructure estimate.

## 11. Privacy and data flows

Local inference end to end; audio does not leave the machine. One-time external touchpoint is the gated pyannote weights download, best performed centrally.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Gated pyannote diarisation weights — plan a central download for air-gapped deployments

## 13. Alternatives

- [noScribe](JAI-A2-31.md) for a desktop application with the same capabilities for non-engineers
- [faster-whisper](JAI-A2-17.md) alone if speaker attribution is unnecessary
- [Montreal Forced Aligner](JAI-A2-29.md) for phone-level forensic alignment against a known transcript

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/m-bain/whisperX
- https://github.com/m-bain/whisperX/blob/main/LICENSE
- https://huggingface.co/pyannote/speaker-diarization-3.1

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

← 50. [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) · 52. [Whisper](JAI-A2-58.md) →
