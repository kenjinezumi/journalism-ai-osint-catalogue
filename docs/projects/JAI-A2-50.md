# Subtitle Edit

`JAI-A2-50` · **77/100** · overall rank 194 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 80) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 45) |
| **Subcategory** | Subtitle and caption editing |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Nikolaj Olsson (SubtitleEdit) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/SubtitleEdit/subtitleedit) · [Documentation](https://www.nikse.dk/subtitleedit/help) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

---

## 1. Purpose

Desktop subtitle editor supporting 200+ subtitle formats with waveform and spectrogram display, synchronisation tools, OCR of hardcoded subtitles, and integrated Whisper transcription backends.

## Journalism / investigative use case

Turning raw transcripts into broadcast-ready captions, and precisely re-timing or verifying subtitles on leaked or downloaded video evidence against the waveform — including OCR-ing burned-in subtitles from a video where no transcript exists, which is a common verification task on circulated clips.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Waveform and spectrogram view makes manual verification of what was actually said at a given moment practical for a non-engineer — the cheapest route to audio verification
- Subtitle OCR extracts text from burned-in captions, a capability almost nothing else in this catalogue offers and which matters for verifying re-uploaded or re-captioned clips
- Integrated Whisper backends mean transcription and caption editing happen in one tool
- Extremely active (pushed 2026-11-17, release v5.4.0 2026-11-06) and mature after many years

## 5. Cons

- Windows-centric: the native build is Windows and other platforms rely on Wine or a less complete port, which is a real constraint in a mixed newsroom
- Online machine-translation features call third-party services and would send subtitle text off-machine — must be switched off by policy for sensitive material
- Dense UI aimed at professional subtitlers rather than reporters; the learning curve is non-trivial despite the GUI
- 199 open issues; feature breadth means edge-case bugs across the 200+ formats

## 6. Feedback (documented)

No individual user reports verified. Documented: 15,028 stars with 199 open issues, same-day push on 2026-11-17 and a release on 2026-11-06 — sustained single-maintainer activity over more than a decade. Widely used in the subtitling community; no journalism deployment verified.

## 7. Assessment

Useful in two distinct roles: caption production for published video, and forensic verification of what a clip actually says. For your profile the second is the more interesting one — the spectrogram plus subtitle-OCR combination is a genuine verification capability. The controls needed are a Windows machine (or a tested Wine setup) and switching off the online translation services before any sensitive file is opened.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v5.4.0 (2026-11-06), tag v5.5.0-beta8, 15,028 stars, 199 open issues. Continuous development with regular releases and betas from a long-standing maintainer.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the editor; bundled Whisper backends use MIT weights.

**Restrictions:** None material.

**Licence evidence:** https://github.com/SubtitleEdit/subtitleedit/blob/main/LICENSE.txt

## 10. Costs

Free. No infrastructure. Optional Whisper backends run locally. If online MT is enabled, third-party service terms and possible costs apply — not priced here.

## 11. Privacy and data flows

Local by default. The explicit exception is the optional machine-translation features, which transmit subtitle text to third-party services; disable them for any sensitive file. Subtitle OCR and waveform analysis are entirely local.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Hyperaudio Lite](JAI-A2-22.md) for publishing interactive transcripts rather than editing captions
- [WhisperX](JAI-A2-60.md) for automated word-level timing at scale
- [noScribe](JAI-A2-31.md) where the artefact is an interview transcript, not captions

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/SubtitleEdit/subtitleedit
- https://www.nikse.dk/subtitleedit/help
- https://github.com/SubtitleEdit/subtitleedit/blob/main/LICENSE.txt

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

← 193. [Sigstore Cosign](JAI-A3-20.md) · 195. [tippecanoe](JAI-A1-23.md) →
