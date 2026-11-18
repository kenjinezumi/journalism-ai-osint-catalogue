# GlotLID

`JAI-A2-20` · **68/100** · overall rank 280 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 109) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 58) |
| **Subcategory** | Language identification |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | cisnlp (University of Munich / CIS) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 with additional notices (LICENSE file read directly: 'Apache License 2.0 plus notices', with appended notices on training data and model behaviour; GitHub API reports NOASSERTION) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/cisnlp/GlotLID) · [Documentation](https://github.com/cisnlp/GlotLID#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 68/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 with additional notices (LICENSE file read directly: 'Apache License 2.0 plus notices', with appended notices on training data and model behaviour; GitHub API reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Apache-2.0 with the same additional notices. |
| **Restrictions** | No field-of-use restriction found. The appended notices are disclaimers about training-data provenance rather than usage limits, but read them before redistributing the model file. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. One model file (hundreds of MB for the full label set), CPU inference, negligible cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/cisnlp/GlotLID/blob/main/LICENSE
- https://github.com/cisnlp/GlotLID

---

## 1. Purpose

FastText-based language identification model covering over 2,000 language labels with script codes, built to address the low-resource-language gap in standard LID models.

## Journalism / investigative use case

Identifies the languages fastText's lid.176 silently misses — minority, diaspora and regional languages in a document dump — so a multilingual leak gets routed to the right translator or MT model instead of being mislabelled as the nearest major language. Because labels carry script codes it distinguishes Serbian in Cyrillic from Serbian in Latin, which matters for sourcing and for choosing a transliteration path.

## 2. Audience

engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- Coverage of low-resource and minority languages is the whole point and is directly relevant to media-in-exile and diaspora reporting, where major-language LID fails
- Script codes in the label set solve a real routing problem that language-only labels cannot
- FastText-based: a single model file, millisecond inference on CPU, trivially air-gappable
- Licence clarified in this survey — the LICENSE file reads as Apache-2.0 plus notices, not an unknown 'Other'

## 5. Cons

- Thousands of labels mean many confusable low-confidence classes; without a confidence threshold you will get plausible-looking wrong answers on short strings
- No tagged releases at all and a research-project cadence, so there is no version to pin other than a commit and a model file hash
- The appended notices warn about training-data provenance and model behaviour — a soft caveat that the labels carry research-grade rather than production guarantees
- Small community (228 stars, 4 open issues): if it breaks, you are on your own

## 6. Feedback (documented)

No user reports collected. Documented context is academic: GlotLID is published research addressing documented failures of lid.176 on low-resource languages. The tiny issue tracker (4 open) reflects a small user base rather than strong triage.

## 7. Assessment

Worth adopting as a routing component in any multilingual ingest pipeline, with a confidence floor and a fallback to 'unknown' rather than a forced guess — a mislabelled language quietly corrupts every downstream step. For your profile the low-resource coverage is the specific reason to prefer it over fastText lid.176. Because there are no releases, record the model file's hash alongside your pipeline version so results stay reproducible.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-09, no releases and no tags, 228 stars, 4 open issues. Recent commits but no release engineering; characteristic of a maintained research artefact. Classified stable-low rather than active because there is no release cadence to evidence active maintenance, and not dormant because commits are current.

## 9. Licensing

**Licence:** Apache-2.0 with additional notices (LICENSE file read directly: 'Apache License 2.0 plus notices', with appended notices on training data and model behaviour; GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Apache-2.0 with the same additional notices.

**Restrictions:** No field-of-use restriction found. The appended notices are disclaimers about training-data provenance rather than usage limits, but read them before redistributing the model file.

**Licence evidence:** https://github.com/cisnlp/GlotLID/blob/main/LICENSE

## 10. Costs

No fee. One model file (hundreds of MB for the full label set), CPU inference, negligible cost.

## 11. Privacy and data flows

Fully local after downloading the model file from HuggingFace; no inference-time network calls.

## 12. Verdict

**Integrate**

## 13. Alternatives

- fastText lid.176 where only major languages matter and speed is paramount
- CLD3 as a lightweight browser/embedded alternative with narrower coverage
- Per-document manual review for the small number of documents that will actually be quoted

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/cisnlp/GlotLID
- https://github.com/cisnlp/GlotLID/blob/main/LICENSE

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

← 279. [entity-fishing](JAI-A2-14.md) · 281. [Awesome Website Change Monitoring](SUR-B1-24.md) →
