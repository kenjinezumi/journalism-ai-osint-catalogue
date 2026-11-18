# uroman

`JAI-A2-56` · **62/100** · overall rank 314 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 116) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 61) |
| **Subcategory** | Transliteration |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | USC Information Sciences Institute (isi-nlp) |
| **Maintenance** | Dormant |
| **Licence** | MIT-style permissive with an added acknowledgement condition (LICENSE.txt grants MIT-equivalent rights but states 'Any publication of projects using uroman shall acknowledge its use'; GitHub API reports NOASSERTION) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/isi-nlp/uroman) · [Documentation](https://github.com/isi-nlp/uroman#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 62/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT-style permissive with an added acknowledgement condition (LICENSE.txt grants MIT-equivalent rights but states 'Any publication of projects using uroman shall acknowledge its use'; GitHub API reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a — rule tables, no trained weights. |
| **Restrictions** | Acknowledgement is a publication obligation: any publication of a project using uroman must acknowledge it. Not a use restriction, but it must be tracked so the credit actually appears. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, negligible resources, no paid dependencies.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/isi-nlp/uroman/blob/master/LICENSE.txt
- https://github.com/isi-nlp/uroman

---

## 1. Purpose

Universal romaniser that converts text in virtually any script to the Latin alphabet using rule tables, with no trained model and no language specification required.

## Journalism / investigative use case

Makes non-Latin-script corpora searchable and joinable: romanise Arabic, Cyrillic, Devanagari, Thai or Chinese names so a sanctions list, a corporate registry and a leaked ledger can be fuzzy-matched in one Latin-script index — the step that makes cross-script name matching possible at all.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Script-agnostic with no language detection required, so it handles a mixed-script corpus without routing logic — a genuine simplification
- Rule-based and deterministic: the same input always romanises identically, which is what a reproducible matching pipeline needs
- No models, no dependencies of consequence, entirely offline — trivially deployable on an evidence machine
- Covers an unusually wide range of scripts for a single tool, including ones with little other tooling

## 5. Cons

- Romanisation is lossy and irreversible: distinct names can collide, which creates false matches that must be adjudicated
- Output follows no single standard scheme (not ALA-LC, not BGN/PCGN), so it is a matching aid rather than a citable rendering — never use uroman output as a published name spelling
- Licence carries a non-standard condition: the LICENSE.txt grants MIT-equivalent rights but states that 'Any publication of projects using uroman shall acknowledge its use', so it is not a clean SPDX identifier (GitHub reports NOASSERTION)
- Dormant: last push 2024-07-26 with release v1.3.1 (2024-06-28) and 17 open issues

## 6. Feedback (documented)

No individual user reports verified. Documented: the acknowledgement clause read directly from LICENSE.txt in session 1 and retained; last push 2024-07-26; 258 stars. uroman is a well-cited research tool in MT and cross-lingual IR, which is adjacent-field credibility rather than journalism evidence.

## 7. Assessment

Use it as a matching-key generator, never as a name renderer, and remember the acknowledgement condition — for your work that means a line in the methodology note of any story whose matching depended on it, which is a trivial obligation but a real one. The dormancy is acceptable here because rule tables do not rot the way a dependency-heavy library does; the risk is that an unsupported script or a bug will never be fixed.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-07-26, latest release v1.3.1 (2024-06-28), 258 stars, 17 open issues. Over two years without activity. Classified dormant; mitigated by the nature of the tool — deterministic rule tables with no dependency surface degrade far more slowly than typical software.

## 9. Licensing

**Licence:** MIT-style permissive with an added acknowledgement condition (LICENSE.txt grants MIT-equivalent rights but states 'Any publication of projects using uroman shall acknowledge its use'; GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a — rule tables, no trained weights.

**Restrictions:** Acknowledgement is a publication obligation: any publication of a project using uroman must acknowledge it. Not a use restriction, but it must be tracked so the credit actually appears.

**Licence evidence:** https://github.com/isi-nlp/uroman/blob/master/LICENSE.txt

## 10. Costs

No fee, negligible resources, no paid dependencies.

## 11. Privacy and data flows

Entirely local, no network, no models.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [rigour](JAI-A2-44.md) for corporate-name normalisation within Latin script
- ICU transliteration for standards-conformant, citable transliteration schemes
- Language-specific transliteration libraries where a published rendering is required

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/isi-nlp/uroman
- https://github.com/isi-nlp/uroman/blob/master/LICENSE.txt

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

← 313. [OpenOversight](SUR-B2-12.md) · 315. [TruFor](JAI-A4-18.md) →
