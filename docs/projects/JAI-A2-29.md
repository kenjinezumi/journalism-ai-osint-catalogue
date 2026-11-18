# Montreal Forced Aligner

`JAI-A2-29` · **67/100** · overall rank 285 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 110) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 59) |
| **Subcategory** | Audio alignment |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Montreal Corpus Tools (McGill) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) · [Documentation](https://montreal-forced-aligner.readthedocs.io/) |

**Scores** — relevance 2/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 67/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Pretrained acoustic models and dictionaries are distributed separately per language — verify each; some derive from corpora with their own terms. |
| **Restrictions** | Code permissive. Per-language model and dictionary terms need checking before commercial use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Costs are a conda environment, a PostgreSQL instance and CPU time proportional to audio hours; plus specialist time to build dictionaries. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/main/LICENSE
- https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner
- https://montreal-forced-aligner.readthedocs.io/

---

## 1. Purpose

Kaldi-based forced aligner that time-aligns a known transcript to an audio recording at word and phone level, with pretrained acoustic models and pronunciation dictionaries for many languages.

## Journalism / investigative use case

Authenticating or precisely timestamping a known transcript against a recording — essential when you must demonstrate that a specific phrase occurs at a specific moment in leaked audio, or when verifying that a circulating 'transcript' of a speech matches the actual recording.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Produces phone-level timing that no ASR system gives you, which is what makes forensic-grade claims about audio possible
- Pretrained models and dictionaries for a wide range of languages, so it is not English-only like much speech tooling
- Mature, academically grounded and actively released (v3.4.4, 2026-11-16) — unusual longevity for a research tool
- Deterministic: given the same inputs it produces the same alignment, which is what an evidentiary workflow needs

## 5. Cons

- Aligns, does not recognise — you must supply a correct transcript, so it complements rather than replaces transcription
- Requires a pronunciation dictionary for the language, and out-of-dictionary proper names (ubiquitous in investigations) degrade alignment precisely where it matters
- Conda-only installation plus a PostgreSQL corpus database is an awkward and heavy dependency chain
- 292 open issues against 1,918 stars — the highest backlog ratio in this subcategory, suggesting support demand exceeds capacity

## 6. Feedback (documented)

No individual user reports verified. Documented signals: active releases through 2026-11-16 alongside a 292-issue backlog — a maintained project with a support deficit. Strong adoption in phonetics/linguistics research; no journalism deployment verified.

## 7. Assessment

A specialist instrument: adopt it only when an audio-authentication or precise-timestamping question is actually on the table, in which case nothing else does the job. For your profile I would install it on demand rather than keep it in the standard stack, and I would pre-build a custom pronunciation dictionary for the proper names central to the investigation — that single step is what determines whether the alignment is usable.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v3.4.4 published the same day (2026-11-16), 1,918 stars, 292 open issues. Same-day push and release demonstrates active maintenance; the large backlog is a responsiveness limitation rather than evidence of decline.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Pretrained acoustic models and dictionaries are distributed separately per language — verify each; some derive from corpora with their own terms.

**Restrictions:** Code permissive. Per-language model and dictionary terms need checking before commercial use.

**Licence evidence:** https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/main/LICENSE

## 10. Costs

No fee. Costs are a conda environment, a PostgreSQL instance and CPU time proportional to audio hours; plus specialist time to build dictionaries. Estimate.

## 11. Privacy and data flows

Fully local; model and dictionary downloads from the project index are the only network events. Suitable for sensitive audio on isolated hardware.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [WhisperX](JAI-A2-60.md), whose wav2vec2 alignment gives word-level timing with far less setup and is sufficient for most quote-verification needs
- [Subtitle Edit](JAI-A2-50.md) for manual waveform-based verification by a non-engineer
- Praat for forensic phonetic analysis by a specialist

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner
- https://montreal-forced-aligner.readthedocs.io/
- https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/main/LICENSE

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

← 284. [Hierarchical-Localization (hloc)](OSINT-C2-35.md) · 286. [LoFTR](OSINT-C2-34.md) →
