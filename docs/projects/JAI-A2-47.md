# spaCy

`JAI-A2-47` · **90/100** · overall rank 44 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 16) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 10) |
| **Subcategory** | Named entity recognition |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Explosion AI |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/explosion/spaCy) · [Documentation](https://spacy.io/usage) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 5/5 → **weighted 90/100**

---

## 1. Purpose

Production-oriented NLP library providing tokenisation, part-of-speech tagging, dependency parsing, named-entity recognition and rule-based matching, with trained pipelines for around 25 languages.

## Journalism / investigative use case

Baseline workhorse for pulling person, organisation, location and money mentions out of leaked documents and mailboxes. The EntityRuler is the feature that matters most in practice: reporters supply a gazetteer of target names and companies, and the pipeline flags every occurrence across a corpus before any statistical NER runs.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Fast, stable and predictable at corpus scale — the practical default when you need to process a million documents on CPU without GPU infrastructure
- EntityRuler and the Matcher let you encode editorial knowledge (target lists, aliases) deterministically, which is both more accurate and more defensible than a statistical guess
- Documentation is the best in the NLP ecosystem and the API has been stable for years, so pipelines keep working
- MIT licensed with mostly-MIT English pipelines, and a commercially sustainable company behind it

## 5. Cons

- Statistical NER degrades noticeably on OCR-noisy leak text, unusual transliterations and non-Latin scripts — exactly the material investigations contain
- No entity linking to real-world identifiers out of the box, so 'Rosneft' stays a string rather than becoming an entity
- Fixed label set unless you retrain, which makes investigation-specific types (vessel, shell company) impractical — GLiNER is the better answer there
- Model package licences vary: en_core_web_* are MIT but some non-English packages carry corpus-derived terms, and these were not individually verified

## 6. Feedback (documented)

No individual user reports verified. Documented: 34,061 stars, 276 open issues, pushed 2026-10-27 with release-v3.8.18 (2026-10-26) and a v4.0.0.dev10 tag in progress. spaCy is a dependency of Presidio and many newsroom pipelines, which is verifiable from those projects.

## 7. Assessment

Adopt as the baseline, but use it the right way round: gazetteer matching first (high precision, defensible), statistical NER second (recall, needs review). For your profile the honest limitation is non-Latin scripts and OCR noise, where Stanza or GLiNER will outperform it — keep all three available and choose per corpus rather than standardising on one.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-27, latest release release-v3.8.18 (2026-10-26), tag v4.0.0.dev10, 34,061 stars, 276 open issues. Regular 3.8.x maintenance releases plus a v4 development line; commercial company backing. Three weeks since last push is normal for a mature library.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Varies by pipeline package: en_core_web_* are MIT; some non-English packages carry corpus-derived terms. Not individually verified in this survey.

**Restrictions:** Code unrestricted. Check the specific language pipeline's licence before commercial use — a few derive from restrictively licensed treebanks.

**Licence evidence:** https://github.com/explosion/spaCy/blob/master/LICENSE

## 10. Costs

No fee. CPU-efficient; large-scale NER over millions of documents is a compute-hours cost on commodity hardware. Explosion sells Prodigy (annotation tool) separately — a paid product, price not verified here, and not required.

## 11. Privacy and data flows

Local-only inference; only the initial model download touches the network. Suitable for air-gapped work once packages are staged.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [GLiNER](JAI-A2-19.md) for investigation-specific custom entity types
- [Stanza](JAI-A2-49.md) for better non-English accuracy
- [entity-fishing](JAI-A2-14.md) when you need Wikidata identifiers rather than strings

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/explosion/spaCy
- https://spacy.io/usage
- https://github.com/explosion/spaCy/blob/master/LICENSE

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

← 43. [vLLM](JAI-A3-03.md) · 45. [Qubes OS](SUR-B3-20.md) →
