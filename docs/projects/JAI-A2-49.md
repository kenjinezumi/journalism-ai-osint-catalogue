# Stanza

`JAI-A2-49` · **79/100** · overall rank 164 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 65) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 38) |
| **Subcategory** | Multilingual NLP |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Stanford NLP Group |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (GitHub licence detection reports 'Other'; the LICENSE file read directly is the Apache License 2.0, Copyright 2019 Board of Trustees of Leland Stanford Junior University) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/stanfordnlp/stanza) · [Documentation](https://stanfordnlp.github.io/stanza/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 3/5 → **weighted 79/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Neural NLP pipeline covering tokenisation, lemmatisation, POS tagging, dependency parsing, NER and coreference for 70+ languages, with a Python bridge to Java CoreNLP.

## Journalism / investigative use case

Entity extraction from non-English leaks — Russian, Arabic, Ukrainian and Chinese registries and correspondence — where English-first pipelines fail. It is also the bridge to CoreNLP's SUTime for normalising the date expressions that structure a timeline from narrative documents.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Language coverage (70+) is the broadest in this subcategory and the specific reason to carry it alongside spaCy for cross-border work
- CoreNLP bridge gives access to SUTime date normalisation and OpenIE relation extraction, neither of which spaCy provides
- Academically grounded with consistent Universal Dependencies annotations, so cross-language processing is methodologically coherent
- Actively released (v1.15.1, 2026-11-14) with a long institutional track record at Stanford

## 5. Cons

- Model licensing is the open question: the code is Apache-2.0 (verified by reading the LICENSE file, since GitHub reports 'Other'), but the Available Models documentation page states no licence for the downloadable model archives, and training treebanks and NER corpora may carry their own restrictions — an unresolved commercial-use risk
- Slower than spaCy by a wide margin on large corpora because the models are heavier neural pipelines
- NER label sets vary by language, so merging entities across languages needs a mapping layer you build yourself
- 103 open issues and an academic support model — responses are not guaranteed

## 6. Feedback (documented)

No individual user reports verified. The documented finding carried forward and retained here is the licensing gap: GitHub SPDX reports NOASSERTION, the LICENSE file is Apache-2.0 (Copyright 2019 Board of Trustees of Leland Stanford Junior University), and the models page states no licence for the model archives. That combination is a genuine unresolved risk, not an oversight in this survey.

## 7. Assessment

Carry it specifically for non-English material, where it is the strongest open option. But treat the model licensing as an open compliance question before anything built on it is commercially published: the code licence is clear and the weights licence is not. For your profile I would ask Stanford directly or restrict Stanza's output to internal lead generation rather than published derived datasets until that is resolved. Marking this entry's licence confidence as medium for exactly that reason.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release v1.15.1 (2026-11-14), 7,917 stars, 103 open issues. Current releases on a 1.15.x line with university backing; sustained over many years.

## 9. Licensing

**Licence:** Apache-2.0 (GitHub licence detection reports 'Other'; the LICENSE file read directly is the Apache License 2.0, Copyright 2019 Board of Trustees of Leland Stanford Junior University) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** NOT verified and materially uncertain — the Available Models documentation page states no licence for the downloadable model archives, and training treebanks/NER corpora may carry their own restrictions.

**Restrictions:** Code is permissive. Model archives have no stated licence, so commercial redistribution of outputs or weights is legally unclear. Treat as an open question, not a permission.

**Licence evidence:** https://github.com/stanfordnlp/stanza/blob/main/LICENSE

## 10. Costs

No fee. GPU recommended for large corpora; CPU is workable but slow. CoreNLP bridge adds a JVM. Estimate.

## 11. Privacy and data flows

Local inference; model archives downloaded from Stanford or HuggingFace on first use. No inference-time network calls.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Model-archive licence is unstated — unresolved commercial-use risk for derived published datasets

## 13. Alternatives

- [spaCy](JAI-A2-47.md) for speed on major languages
- [GLiNER](JAI-A2-19.md) for custom entity types with a clearer Apache-2.0 weights path
- PaddleOCR/PP-Structure plus GLiNER for CJK document pipelines

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/stanfordnlp/stanza
- https://stanfordnlp.github.io/stanza/available_models.html
- https://github.com/stanfordnlp/stanza/blob/main/LICENSE

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

← 163. [ingest-file (OpenAleph fork)](JAI-A2-25.md) · 165. [wayback (Python client for the Internet Archive Wayback Machine)](SUR-B1-22.md) →
