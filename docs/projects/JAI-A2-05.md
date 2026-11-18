# Buzz

`JAI-A2-05` · **90/100** · overall rank 39 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 14) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 9) |
| **Subcategory** | Transcription (desktop application) |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Chidi Williams |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/chidiwilliams/buzz) · [Documentation](https://chidiwilliams.github.io/buzz/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 90/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Whisper, whisper.cpp and faster-whisper weights are MIT. The optional OpenAI API mode uses a hosted model under OpenAI's terms instead. |
| **Restrictions** | None material for the local path. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free. Note the project also distributes a paid App Store build on some platforms as a convenience — the GitHub release is free. Real cost is reporter wait time on CPU; a modest GPU workstation shared by the newsroom removes it. If the OpenAI backend is enabled you incur per-minute API charges — verify current rates at point of use; not priced here.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/chidiwilliams/buzz/blob/main/LICENSE
- https://github.com/chidiwilliams/buzz
- https://chidiwilliams.github.io/buzz/

---

## 1. Purpose

Cross-platform desktop GUI over Whisper, whisper.cpp and faster-whisper that transcribes and translates audio and video files locally, exporting TXT, SRT and VTT.

## Journalism / investigative use case

The practical default for a reporter with no command line: drag a two-hour interview recording in, get a timestamped transcript and subtitles, with the audio never leaving the laptop. This is the tool that makes local transcription a newsroom policy rather than an engineering aspiration.

## 2. Audience

journalist

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Removes the engineering barrier entirely — installable app, no Python environment, which is what determines whether non-technical staff actually stop uploading interviews to cloud services
- 22,869 stars and only 20 open issues: an unusually healthy ratio indicating issues are actually closed
- Wraps the faster-whisper/whisper.cpp backends, so you get near-state-of-the-art local accuracy without the reporter choosing a backend
- Supports batch queues and subtitle export, covering the two things newsroom audio work actually needs

## 5. Cons

- Speaker diarisation is not a first-class feature, so multi-party interviews come out as undifferentiated text — the single biggest gap versus WhisperX or noScribe
- Large models are slow on CPU; a reporter on a laptop without a GPU will wait, and may be tempted toward the cloud option
- It ships an optional OpenAI API backend — a genuine foot-gun that uploads audio, and which needs an explicit newsroom policy or a locked-down build to prevent
- Single-maintainer project; the bus factor is one

## 6. Feedback (documented)

No individual user reports verified. The quantitative signal is unusually strong and checkable: 22.9k stars with 20 open issues on 2026-11-17 indicates both wide use and active triage — a better maintenance indicator than commit frequency alone.

## 7. Assessment

This is the tool I would actually deploy to reporters, with the OpenAI backend disabled by policy or configuration and the gap on diarisation covered by sending multi-speaker material to a WhisperX or noScribe pipeline. Its value is social, not technical: it changes behaviour. For media-in-exile contexts where uploading an interview could identify a source, that behavioural change is the whole point.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v1.4.5 (2026-08-23), 22,869 stars, 20 open issues. Recent push, recent release and a near-empty issue tracker together justify 'actively maintained' rather than push-recency alone.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Whisper, whisper.cpp and faster-whisper weights are MIT. The optional OpenAI API mode uses a hosted model under OpenAI's terms instead.

**Restrictions:** None material for the local path.

**Licence evidence:** https://github.com/chidiwilliams/buzz/blob/main/LICENSE

## 10. Costs

Free. Note the project also distributes a paid App Store build on some platforms as a convenience — the GitHub release is free. Real cost is reporter wait time on CPU; a modest GPU workstation shared by the newsroom removes it. If the OpenAI backend is enabled you incur per-minute API charges — verify current rates at point of use; not priced here.

## 11. Privacy and data flows

Local by default: audio is processed on the machine and nothing is uploaded. The exception is explicit and must be managed — selecting the OpenAI Whisper API backend sends the audio to OpenAI. For source protection, disable or remove that option and document the decision.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [noScribe](JAI-A2-31.md) where speaker-labelled interview transcripts and a correction editor are the priority
- [WhisperX](JAI-A2-60.md) for engineer-run pipelines needing diarisation and word-level timing
- [Subtitle Edit](JAI-A2-50.md) for caption production rather than transcription

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/chidiwilliams/buzz
- https://chidiwilliams.github.io/buzz/
- https://github.com/chidiwilliams/buzz/blob/main/LICENSE

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

← 38. [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) · 40. [EFF Rayhunter](SUR-B3-13.md) →
