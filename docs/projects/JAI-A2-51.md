# sumy

`JAI-A2-51` · **72/100** · overall rank 257 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 103) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 56) |
| **Subcategory** | Summarisation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Michal Belica (miso-belica) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/miso-belica/sumy) · [Documentation](https://github.com/miso-belica/sumy#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, negligible compute, no paid dependencies.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/miso-belica/sumy/blob/main/LICENSE.rst
- https://github.com/miso-belica/sumy

---

## 1. Purpose

Classical extractive summarisation library implementing LexRank, LSA, TextRank, Luhn, SumBasic and KL-divergence summarisers for plain text in many languages.

## Journalism / investigative use case

Rapid triage of long documents where every summary sentence must be verbatim from the original: a 300-page inquiry report reduced to twenty of its own sentences, which a reporter can trust as quoted text rather than having to re-verify against a generative paraphrase.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Extractive by construction, so it cannot hallucinate — the single most important safety property for summarisation in journalism, and the reason to prefer it over an LLM for triage
- No models, no GPU, no network: an afternoon's integration with no infrastructure and no privacy surface
- Multiple algorithms let you compare outputs cheaply and pick one that suits your document type
- Stable and still released (v0.13.0, 2026-08-12) after many years; Apache-2.0

## 5. Cons

- Extractive summaries read disjointedly — useful for triage, unusable as published prose
- Quality drops sharply on short documents and on highly structured material such as spreadsheets, email headers or forms, which are common in leaks
- Sentence selection is frequency-driven, so it favours repetitive boilerplate and can miss the one anomalous sentence that is the actual story
- NLTK data dependency for tokenisation and stemming is a small but annoying extra download step

## 6. Feedback (documented)

No individual user reports verified. Documented: 3,701 stars with only 7 open issues — a finished library with minimal support burden, released 2026-08-12 and pushed 2026-11-11.

## 7. Assessment

A sensible, boring choice that I would use deliberately in place of an LLM for first-pass document triage, precisely because its failure mode is 'unhelpful' rather than 'confidently invented'. For your profile the pattern worth building is: sumy for a verbatim extract shown to the reporter, with the full document one click away — never an abstractive summary presented as the document's content.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-11, latest release v0.13.0 (2026-08-12), 3,701 stars, 7 open issues. Low change velocity with a current release and essentially no backlog — the textbook profile of a complete, maintained library rather than a declining one.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/miso-belica/sumy/blob/main/LICENSE.rst

## 10. Costs

No fee, negligible compute, no paid dependencies.

## 11. Privacy and data flows

Fully local, no model downloads beyond NLTK corpora, no network at runtime.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [BERTopic](JAI-A2-04.md) for thematic rather than per-document triage
- [txtai](JAI-A2-55.md) if you want semantic search plus optional abstractive summarisation in one stack
- A self-hosted LLM for abstractive summaries — accepting hallucination risk and a mandatory verification step

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/miso-belica/sumy
- https://github.com/miso-belica/sumy/blob/main/LICENSE.rst

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

← 256. [Hyperaudio Lite](JAI-A2-22.md) · 258. [suncalc-py](OSINT-C2-39.md) →
