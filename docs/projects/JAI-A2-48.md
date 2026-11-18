# Splink

`JAI-A2-48` · **87/100** · overall rank 65 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 26) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 17) |
| **Subcategory** | Probabilistic record linkage |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | UK Ministry of Justice Analytical Services |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/moj-analytical-services/splink) · [Documentation](https://moj-analytical-services.github.io/splink/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 87/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. DuckDB backend runs locally with no infrastructure. Spark/Athena backends incur cloud costs and would move data to that infrastructure — avoid for sensitive linkage. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/moj-analytical-services/splink/blob/master/LICENSE
- https://github.com/moj-analytical-services/splink
- https://moj-analytical-services.github.io/splink/

---

## 1. Purpose

Probabilistic record-linkage library implementing the Fellegi-Sunter model with unsupervised parameter estimation (expectation maximisation), running on DuckDB, Spark, Athena or Postgres backends, with diagnostic visualisations.

## Journalism / investigative use case

Link people across two large datasets with no shared key — a sanctions list against a corporate registry, or a leak's client list against a property register — at a scale where dedupe would stall, and with auditable per-comparison match weights you can show an editor or a lawyer.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Produces an interpretable match weight per comparison rather than an opaque score, which is the difference between a defensible linkage and an assertion — the single most important property for published investigations
- Scales to tens of millions of records on a laptop via the DuckDB backend, which removes the infrastructure barrier that normally forces this work into a cluster
- Built and used by a government analytical service for operational data linkage, with published methodology — strong institutional provenance
- Excellent diagnostic charts (match weight waterfalls, parameter estimates) that make the model's behaviour inspectable rather than magical

## 5. Cons

- Requires genuine understanding of blocking rules and m/u probabilities; naive use produces confidently wrong links, and the library will not stop you
- Output is a probability, not a verdict — the adjudication threshold is an editorial decision that must be documented, and teams often skip that step
- v5 broke APIs relative to v3/v4, while most tutorials and blog posts still circulating describe the older versions — a real friction point (221 open issues)
- No built-in UI for human adjudication of borderline pairs, so you must build that review step yourself

## 6. Feedback (documented)

No individual user reports verified. Documented: MoJ Analytical Services is the maintainer and publishes its methodology, which is credible institutional production evidence; 2,588 stars, 221 open issues, v5.0.0 released 2026-09-18. Note that the v5 API break against widely circulating v3/v4 tutorials is verifiable from the project's own migration documentation.

## 7. Assessment

My recommended record-linkage tool for your work, replacing dedupe. The reason is specifically evidentiary: when a story asserts that two records are the same person, Splink lets you state the match weight and the comparison features that produced it. Budget time to learn the model properly — this is the one tool here where shallow use is actively dangerous — and build a small review interface for pairs above your threshold.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-11, latest release v5.0.0 (2026-09-18), 2,588 stars, 221 open issues. A major release in 2026 with current commits and public-sector institutional backing.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/moj-analytical-services/splink/blob/master/LICENSE

## 10. Costs

No fee. DuckDB backend runs locally with no infrastructure. Spark/Athena backends incur cloud costs and would move data to that infrastructure — avoid for sensitive linkage. Estimate.

## 11. Privacy and data flows

Local with the DuckDB backend, which is the recommended configuration for sensitive data. Choosing a cloud Spark or Athena backend relocates the data to that provider — a configuration decision with major privacy consequences.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [nomenklatura](JAI-A2-30.md) if your data is already in FollowTheMoney
- [dedupe](JAI-A2-11.md) for small analyst-driven jobs, with its maintenance caveat
- [RapidFuzz](JAI-A2-43.md) plus manual rules for trivially small matching tasks

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/moj-analytical-services/splink
- https://moj-analytical-services.github.io/splink/
- https://github.com/moj-analytical-services/splink/blob/master/LICENSE

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

← 64. [faster-whisper](JAI-A2-17.md) · 66. [Marker](JAI-A2-28.md) →
