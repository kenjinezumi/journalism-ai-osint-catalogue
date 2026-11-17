# pyannote.audio

`JAI-A2-41` · **81/100** · overall rank 144 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 60) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 35) |
| **Subcategory** | Speaker diarisation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Hervé Bredin / pyannote (commercial arm pyannote.ai) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/pyannote/pyannote-audio) · [Documentation](https://github.com/pyannote/pyannote-audio#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 81/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Neural speaker-diarisation toolkit providing pretrained pipelines for voice activity detection, speaker segmentation, embedding and clustering, answering 'who spoke when' in an audio recording.

## Journalism / investigative use case

The de facto open diarisation layer for newsroom pipelines: separating speakers in interviews, conference calls and intercepted audio before transcription, so a transcript attributes each statement to a person rather than producing an undifferentiated wall of text.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- The reference open diarisation implementation — WhisperX, noScribe and most newsroom transcription stacks depend on it, so it is the de facto standard
- Very actively developed with a 4.x line (4.1.0 released 2026-11-17) and an exceptionally clean tracker (35 open issues against 10,806 stars)
- MIT licensed with the project stating the pipeline 'will always remain open-source' on its model card — a meaningful commitment given the commercial arm
- Modular: VAD, segmentation and embedding components can be used separately or retrained on your own audio

## 5. Cons

- Weights are gated: the speaker-diarization-3.1 model card requires agreeing to share your HuggingFace information to access the model — a real blocker for air-gapped work and a disclosure for anonymity-sensitive users, since the model authors learn your identity at download time
- Accuracy drops materially on overlapping speech, telephone-band audio and recordings with many speakers — exactly the conditions of covertly recorded material
- Increasingly coupled to a commercial offering (pyannote.ai) whose Precision models are better than the open ones, creating a structural incentive toward the paid tier
- Engineer-facing: no UI, and tuning clustering parameters for a specific recording type takes experimentation

## 6. Feedback (documented)

No individual user reports verified. Documented and checkable: the HuggingFace model card for pyannote/speaker-diarization-3.1 states the information-sharing requirement and also states the pipeline will remain open source. The commercial pyannote.ai price list was verified in session 1: Diarization Precision-3 batch at EUR0.112/hour of audio, Community-1 batch EUR0.035/hour, Live-1 streaming EUR0.198/hour, plus Developer EUR19/month and Starter EUR99/month subscriptions (vendor page, 2026-11-16).

## 7. Assessment

Necessary rather than optional if you need speaker attribution, and the gating is a manageable but real nuisance: download the weights once on a non-sensitive machine with an organisational HuggingFace account, then distribute internally so individual journalists never authenticate. For media-in-exile work that one-time disclosure matters and should be a deliberate decision. Where diarisation accuracy on bad audio is critical, benchmark against NeMo Sortformer — but note Sortformer's CC-BY-NC licence blocks commercial publication.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 4.1.0 published the same day, 10,806 stars, 35 open issues. Same-day push and release plus a very low backlog at scale; the commercial arm appears to sustain rather than starve the open project, though that balance is worth monitoring.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** MIT but GATED — the speaker-diarization-3.1 card requires agreeing to share your HuggingFace information to access the model. The card also states the pipeline will remain open-source.

**Restrictions:** No field-of-use restriction, but access is conditioned on identity disclosure to HuggingFace and the model authors. That is an access barrier with privacy consequences rather than a licence limitation.

**Licence evidence:** https://huggingface.co/pyannote/speaker-diarization-3.1

## 10. Costs

Open library free. GPU recommended for throughput. The hosted pyannote.ai alternative is priced per audio-hour (Precision-3 batch EUR0.112/h; Community-1 batch EUR0.035/h; Live-1 EUR0.198/h) with Developer EUR19/month and Starter EUR99/month tiers including matching credit — verified 2026-11-16, EUR, usage-based. Using the hosted service means uploading audio.

## 11. Privacy and data flows

Inference is local and audio stays on your machine. The gate is the privacy cost: obtaining weights discloses your HuggingFace identity. Pre-staging weights solves this for downstream users. Never use the hosted API for source-sensitive audio.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Gated weights requiring HuggingFace identity disclosure — plan a one-time central download for air-gapped or anonymity-sensitive deployments

## 13. Alternatives

- NVIDIA NeMo Sortformer for higher accuracy — but CC-BY-NC-4.0 blocks commercial publication
- [WhisperX](JAI-A2-60.md), which wraps pyannote with alignment and transcription
- Accepting unlabelled transcripts where speaker attribution is not editorially necessary

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/pyannote/pyannote-audio
- https://huggingface.co/pyannote/speaker-diarization-3.1
- https://www.pyannote.ai/pricing
- `../sources/recovered/cat/pricing.tsv`

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

← 143. [nomenklatura](JAI-A2-30.md) · 145. [pywb](OSINT-C1-27.md) →
