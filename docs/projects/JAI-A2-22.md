# Hyperaudio Lite

`JAI-A2-22` · **72/100** · overall rank 256 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 102) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 55) |
| **Subcategory** | Transcript publishing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Hyperaudio (Mark Boas) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/hyperaudio/hyperaudio-lite) · [Documentation](https://hyperaud.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

---

## 1. Purpose

Lightweight dependency-free JavaScript library that binds a timed transcript to an audio or video element, giving click-to-seek, karaoke-style highlighting and in-transcript search.

## Journalism / investigative use case

Publishing the evidence alongside the story: an embeddable, searchable transcript of an interview or council hearing where a reader can click any sentence and hear it in the original recording. That turns 'we have a recording' into verifiable published evidence and pre-empts quote-distortion accusations.

## 2. Audience

engineer, journalist

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Solves the last-mile publishing problem that transcription tools ignore — the reader-facing artefact, not the transcript file
- No dependencies and entirely client-side, so it adds no backend, no tracking and no third-party scripts to a story page
- MIT and tiny, so a newsroom front-end developer can adapt it in an afternoon
- Maintained by the team that has worked on this specific problem for years, with a current release (v2.6.6, 2026-09-21)

## 5. Cons

- Presentation layer only: the timed transcript must be produced elsewhere (WhisperX, noScribe) and converted to the expected HTML/WebVTT shape
- Small niche project (183 stars, 42 open issues) — the open-issue-to-star ratio is high, suggesting limited maintainer bandwidth relative to requests
- Accessibility, styling and mobile behaviour are largely left to the implementer, so a polished result takes design work
- Whatever you publish is public by design, so redaction decisions must be final before the transcript is embedded — there is no partial-disclosure mechanism

## 6. Feedback (documented)

No individual user reports verified. Hyperaudio's lineage in media/journalism prototyping is long-standing and documented by the project, but I verified no specific newsroom deployment; treat adoption as plausible rather than evidenced.

## 7. Assessment

A small, high-leverage addition if your newsroom publishes audio-based investigations. For your profile the integration is trivial relative to the editorial payoff, and the privacy profile is clean — no third-party player, no tracking. The one discipline it demands is that the transcript be redaction-final, since publishing a clickable transcript exposes every word of the recording you ship with it.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-30, latest release v2.6.6 (2026-09-21), 183 stars, 42 open issues. Regular small releases from a small team; functionally complete library with modest change velocity.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — playback library, no model.

**Restrictions:** None.

**Licence evidence:** https://github.com/hyperaudio/hyperaudio-lite/blob/main/LICENSE

## 10. Costs

No fee, no infrastructure beyond your existing web hosting. Cost is front-end developer time for styling and accessibility.

## 11. Privacy and data flows

Entirely client-side with no network calls of its own, so it introduces no tracking into a story page — notably better than embedding a third-party player. The published transcript and media are public by definition.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Subtitle Edit](JAI-A2-50.md) to produce and verify the timed file first
- Custom WebVTT plus a standard HTML5 player if you need less than Hyperaudio offers
- oTranscribe for transcription-time workflows rather than publishing

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/hyperaudio/hyperaudio-lite
- https://hyperaud.io/
- https://github.com/hyperaudio/hyperaudio-lite/blob/main/LICENSE

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

← 255. [Frictionless Data (frictionless-py)](OSINT-C3-40.md) · 257. [sumy](JAI-A2-51.md) →
