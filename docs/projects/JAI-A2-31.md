# noScribe

`JAI-A2-31` · **91/100** · overall rank 32 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 10) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 7) |
| **Subcategory** | Transcription (desktop application) |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Kai Dröge (kaixxx) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/kaixxx/noScribe) · [Documentation](https://github.com/kaixxx/noScribe#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 91/100**

---

## 1. Purpose

Desktop application that combines Whisper transcription with pyannote speaker diarisation and ships a built-in transcript editor synchronised to the audio, aimed at qualitative-interview research.

## Journalism / investigative use case

Purpose-built for the investigative interview workflow: a long multi-party interview comes out speaker-labelled, and the correction editor lets the reporter verify every quote against the audio before publication — closing the gap between machine transcript and quotable text.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Speaker labelling plus an audio-synced correction editor in one installable app — the combination Buzz lacks and that interview-based reporting actually needs
- Designed by a qualitative-research academic, so the assumptions (long recordings, verbatim accuracy, speaker attribution) match investigative interviewing rather than media captioning
- Fully local, GPL-3.0, with no cloud option at all — there is no misconfiguration that uploads your interview
- Current releases (v0.8, 2026-10-06) and an active repository

## 5. Cons

- CPU transcription of a long interview takes hours; without a GPU the workflow is overnight-batch rather than interactive
- Single-maintainer project (2,252 stars, 58 open issues) — the bus factor is one, which matters for a tool in a publication-critical path
- pyannote diarisation weights are gated on HuggingFace: you must accept the gate and pre-fetch weights, which both discloses your HuggingFace identity once and complicates air-gapped installation
- GPL-3.0 constrains embedding it inside a proprietary newsroom system (not a problem for desktop use)

## 6. Feedback (documented)

No individual user reports verified. Documented context: the project is explicitly aimed at qualitative social research and is cited in that community; 2,252 stars with 58 open issues. The HuggingFace gating requirement for pyannote weights is documented by pyannote itself and is a known friction point rather than a noScribe defect.

## 7. Assessment

The better choice than Buzz specifically for interview-driven investigations, because speaker attribution and the verification editor are where quote errors actually occur. For your profile I would deploy noScribe to reporters who do interviews and Buzz to those who process miscellaneous audio, pre-fetching the pyannote weights centrally so individual journalists never need a HuggingFace account — that removes the one privacy wrinkle.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-09, latest release v0.8 (2026-10-06), 2,252 stars, 58 open issues. Regular releases from a single maintainer; activity is current and release-backed.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** Whisper weights MIT; pyannote diarisation weights MIT but gated behind a HuggingFace access agreement.

**Restrictions:** GPL-3.0 limits incorporation into closed-source newsroom tooling. The pyannote gate is an access condition, not a use restriction, but it requires an account.

**Licence evidence:** https://github.com/kaixxx/noScribe/blob/main/LICENSE

## 10. Costs

Free. Real cost is wait time on CPU, or one shared GPU workstation. No paid dependencies.

## 11. Privacy and data flows

Local processing with no cloud transcription path — the strongest privacy posture among desktop transcription apps. One-time external touchpoint: accepting the pyannote HuggingFace gate and downloading weights, which can be done once centrally and then distributed internally.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Buzz](JAI-A2-05.md) for simpler, faster general transcription without diarisation
- [WhisperX](JAI-A2-60.md) for engineer-run batch pipelines with the same diarisation stack
- [Subtitle Edit](JAI-A2-50.md) when the output is captions rather than an interview record

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/kaixxx/noScribe
- https://github.com/kaixxx/noScribe/blob/main/LICENSE
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
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 31. [Docling](JAI-A2-12.md) · 33. [pdfplumber](JAI-A2-39.md) →
