# eyecite

`JAI-A2-16` · **79/100** · overall rank 169 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 67) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 40) |
| **Subcategory** | Legal citation extraction |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Free Law Project |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freelawproject/eyecite) · [Documentation](https://github.com/freelawproject/eyecite#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 79/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | reporters-db reference data is distributed separately by Free Law Project — check its own terms if you redistribute it. |
| **Restrictions** | None material for the code. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Pure CPU, negligible resources. No paid dependencies.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/freelawproject/eyecite/blob/main/LICENSE
- https://github.com/freelawproject/eyecite

---

## 1. Purpose

Python library that finds, parses and resolves US legal citations in text — full case citations, short forms, supra and id. references — and links them to canonical reporter data.

## Journalism / investigative use case

Turns a pile of court filings, briefs or agency decisions into a linked citation graph: which rulings a document relies on, and which other documents in your corpus cite the same case. That is a lead-generation move generic NER cannot make, and it surfaces the brief that quietly depends on a discredited precedent.

## 2. Audience

specialist investigator, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Solves a problem no general NLP tool solves — short-form and id. resolution requires domain logic, and eyecite implements it properly
- Built and used by Free Law Project behind CourtListener, so it is exercised against millions of real documents rather than a test set
- BSD-2-Clause, pure Python, no models to download — trivially auditable and air-gappable
- Genuinely complementary: the citation graph is a different axis of analysis from entities or topics

## 5. Cons

- US legal citation formats only — no coverage of other jurisdictions' conventions, which limits it for international investigations
- Resolution quality depends on the reporters-db reference dataset; gaps there become gaps in your graph
- No GitHub release objects (latest tag v2.7.8), so pinning relies on tags or PyPI rather than release notes
- 89 open issues against 303 stars; a specialist library with a small community, so edge cases on unusual filings may need your own fixes

## 6. Feedback (documented)

No individual user reports verified. The strongest documented signal is institutional: eyecite is a Free Law Project component used in CourtListener's production citation extraction, which is verifiable from the organisation's repositories. That is credible production evidence at scale within its jurisdiction.

## 7. Assessment

If you work on US courts, adopt it — there is no alternative of comparable quality, and the citation graph it produces is a distinctive reporting asset. If your work is non-US, it is irrelevant, and I would not try to generalise it. Scored on its intended specialist role: narrow scope is not a defect here, but it does cap journalism-wide relevance.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest tag v2.7.8, no release objects, 303 stars, 89 open issues. Current commits and an active 2.x tag line, backed by a functioning non-profit (Free Law Project) that depends on it operationally.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** reporters-db reference data is distributed separately by Free Law Project — check its own terms if you redistribute it.

**Restrictions:** None material for the code.

**Licence evidence:** https://github.com/freelawproject/eyecite/blob/main/LICENSE

## 10. Costs

No fee. Pure CPU, negligible resources. No paid dependencies.

## 11. Privacy and data flows

Entirely local, no network calls, no models — one of the cleanest profiles here. Safe on an air-gapped evidence machine.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [CourtListener](OSINT-C3-11.md)/RECAP for acquiring the filings in the first place
- Indigo or laws-africa tooling for non-US legislative documents
- Generic NER (spaCy) where citations are not the target

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/freelawproject/eyecite
- https://github.com/freelawproject/eyecite/blob/main/LICENSE

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

← 168. [Open Contracting Data Standard](SUR-B2-18.md) · 170. [RapidFuzz](JAI-A2-43.md) →
