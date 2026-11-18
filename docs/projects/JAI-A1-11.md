# MinerU

`JAI-A1-11` · **71/100** · overall rank 262 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 105) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 27) |
| **Subcategory** | Document parsing |
| **Type** | framework |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | OpenDataLab (Shanghai AI Laboratory) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 with ADDITIONAL TERMS recorded as restrictive (session 1 read the licence text; GitHub reports NOASSERTION) — read the full terms before commercial use |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opendatalab/MinerU) · [Documentation](https://mineru.net/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 2/5 → **weighted 71/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | Apache-2.0 with ADDITIONAL TERMS recorded as restrictive (session 1 read the licence text; GitHub reports NOASSERTION) — read the full terms before commercial use |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Model weights distributed separately; terms NOT verified in this survey. |
| **Restrictions** | Material and unresolved: the additional terms layered on Apache-2.0 were recorded as restrictive and have not been characterised in detail here. Obtain a legal reading before commercial deployment or redistribution. |
| **Open-source status** | **Source available** — Source published under a restricted, non-OSI licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. GPU host required for the full pipeline — the dominant cost. Model weight downloads. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/opendatalab/MinerU
- `../sources/recovered/a1disc/notes.md`

---

## 1. Purpose

Document-extraction pipeline that converts PDFs and Office documents into Markdown and JSON with layout detection, reading-order reconstruction, formula and table recognition.

## Journalism / investigative use case

High-quality conversion of technical and academic-style documents — scientific reports, engineering filings, financial statements with formulae — where layout and formula recognition matter and generic extractors produce unusable output.

## 2. Audience

engineer

## 3. Project type

framework · bucket `source-available-restricted`

## 4. Pros

- Formula recognition is a genuine differentiator for technical documents, which appear in environmental, medical and engineering investigations and defeat most extractors
- Strong performance on Chinese-language documents, reflecting its origins — relevant if your work covers Chinese corporate or state material
- Very large adoption (83,798 stars) with frequent releases (mineru-4.2.3, 2026-11-16) and an almost empty issue tracker (9 open)
- Produces both Markdown and structured JSON, so it serves reading and programmatic use

## 5. Cons

- LICENCE CAUTION: GitHub reports NOASSERTION and session 1's licence inspection recorded 'Apache-2.0 plus additional terms (restrictive)' — so the licence is not plain Apache-2.0 and the additional terms must be read before commercial use or redistribution. This is exactly the pattern that catches newsrooms out
- GPU effectively required for the full pipeline, so it is server-side infrastructure rather than a laptop tool
- Model weights are distributed separately and their terms were not verified in this survey
- Documentation is strongest in Chinese, and the English materials lag — a real friction for a non-Chinese-speaking team

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 83,798 stars with 9 open issues, release mineru-4.2.3 (2026-11-16), pushed 2026-11-16, SPDX NOASSERTION. Session 1's a1disc/notes.md independently recorded 'MinerU Apache-2.0+additional terms (restrictive)' after reading the licence text — a finding this entry carries forward and flags as requiring legal review.

## 7. Assessment

Technically impressive and licence-ambiguous, which for your profile means: evaluate it on technical documents where its formula and layout handling would materially help, but get the additional licence terms read before anything built on it reaches publication. Docling remains the safer default for general use. If your work involves Chinese-language corporate or state documents, MinerU's advantage there may justify the legal review.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release mineru-4.2.3 published the same day, 83,798 stars, 9 open issues, SPDX NOASSERTION. Same-day release and push with near-zero backlog at very large scale — excellent activity, with licensing as the open question.

## 9. Licensing

**Licence:** Apache-2.0 with ADDITIONAL TERMS recorded as restrictive (session 1 read the licence text; GitHub reports NOASSERTION) — read the full terms before commercial use _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Model weights distributed separately; terms NOT verified in this survey.

**Restrictions:** Material and unresolved: the additional terms layered on Apache-2.0 were recorded as restrictive and have not been characterised in detail here. Obtain a legal reading before commercial deployment or redistribution.

**Licence evidence:** https://github.com/opendatalab/MinerU

## 10. Costs

No fee. GPU host required for the full pipeline — the dominant cost. Model weight downloads. Estimate.

## 11. Privacy and data flows

Local processing after weights download; no inference-time external calls in the self-hosted path. A hosted service exists at mineru.net, which would involve sending documents to the operator.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Licence is Apache-2.0 plus unread additional terms recorded as restrictive — legal review required before commercial use

## 13. Alternatives

- [Docling](JAI-A2-12.md) for a clean MIT position with good layout handling
- [Marker](JAI-A2-28.md)/Surya where the weights threshold is acceptable
- PaddleOCR for Chinese-language OCR with Apache-2.0 code

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/opendatalab/MinerU
- `../sources/recovered/a1disc/notes.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 261. [webappanalyzer](SUR-B2-07.md) · 263. [Exiv2](OSINT-C2-03.md) →
