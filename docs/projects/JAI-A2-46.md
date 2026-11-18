# sherpa-onnx

`JAI-A2-46` · **73/100** · overall rank 242 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 99) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 53) |
| **Subcategory** | On-device speech recognition |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | k2-fsa / Next-gen Kaldi |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/k2-fsa/sherpa-onnx) · [Documentation](https://k2-fsa.github.io/sherpa/onnx/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 73/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Varies per exported checkpoint (Whisper, Zipformer, Paraformer and others distributed separately) — verify the specific model. |
| **Restrictions** | Code permissive. Checkpoint licences vary; some research models carry non-commercial terms, so check the specific archive you deploy. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Engineering time for integration; runs on existing or low-cost hardware |
| **Cost conditions** | Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Runs on existing or cheap hardware (a Raspberry Pi class device suffices for small models), which is part of the point. Engineering time for integration is the real cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/k2-fsa/sherpa-onnx/blob/master/LICENSE
- https://github.com/k2-fsa/sherpa-onnx
- https://k2-fsa.github.io/sherpa/onnx/

---

## 1. Purpose

ONNX-Runtime-based speech toolkit providing streaming and offline ASR, TTS, VAD, speaker identification and keyword spotting with bindings for a dozen languages and builds for Android, iOS, Raspberry Pi and desktop.

## Journalism / investigative use case

Transcription on locked-down or offline hardware — field laptops, phones, a Raspberry Pi in a monitoring setup — for hostile-environment reporting where sending audio to any server, or even installing Python and PyTorch, is unacceptable.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Explicitly built for no-internet operation on constrained devices, which is the specific requirement that disqualifies most of the transcription stack here
- Extremely broad platform and language-binding support (Android, iOS, embedded, C/C++/Rust/Go/Swift/Kotlin), so it embeds into a custom field application
- Streaming ASR enables live monitoring use cases — a radio or broadcast feed transcribed continuously on local hardware
- Very active (pushed 2026-11-17) with frequent prebuilt artefact releases, so you rarely compile from source

## 5. Cons

- Model-zoo quality varies widely by language, and the best models are English and Chinese; a minority-language deployment may be unusable
- Diarisation and speaker handling are simpler than pyannote or NeMo Sortformer
- Sprawling documentation with many model/runtime combinations, and you must match versions carefully — 648 open issues reflects this complexity
- Release tagging is chaotic (latest release artefacts carry names like 'react-fa'), making version pinning awkward

## 6. Feedback (documented)

No individual user reports verified. Documented: 16,005 stars with 648 open issues and continuous commits. The Next-gen Kaldi project has an established research reputation; no journalism deployment verified.

## 7. Assessment

The correct choice for a narrow but important case: embedded or field transcription with no network. For routine newsroom transcription, whisper.cpp is simpler and has better multilingual quality. For your profile I would reach for sherpa-onnx when building something — a monitoring appliance, a phone app for reporters in the field — rather than when transcribing files. Evaluate the specific language model before committing, since quality variance is the main risk.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, frequent release artefacts, 16,005 stars, 648 open issues. High commit velocity with institutional research backing; release hygiene is poor but activity is unambiguous.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Varies per exported checkpoint (Whisper, Zipformer, Paraformer and others distributed separately) — verify the specific model.

**Restrictions:** Code permissive. Checkpoint licences vary; some research models carry non-commercial terms, so check the specific archive you deploy.

**Licence evidence:** https://github.com/k2-fsa/sherpa-onnx/blob/master/LICENSE

## 10. Costs

No fee. Runs on existing or cheap hardware (a Raspberry Pi class device suffices for small models), which is part of the point. Engineering time for integration is the real cost.

## 11. Privacy and data flows

Designed for no-internet operation; nothing leaves the device. Among the strongest privacy profiles in the catalogue, and the right building block for a field device that must not phone home.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [whisper.cpp](JAI-A2-59.md) for simpler CPU transcription of files
- [faster-whisper](JAI-A2-17.md) for server-side batch throughput
- Vosk as an older alternative for embedded offline ASR

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/k2-fsa/sherpa-onnx
- https://k2-fsa.github.io/sherpa/onnx/
- https://github.com/k2-fsa/sherpa-onnx/blob/master/LICENSE

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

← 241. [Kraken](JAI-A2-26.md) · 243. [Juriscraper](OSINT-C3-12.md) →
