# Zingg

`JAI-A1-20` · **56/100** · overall rank 336 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 129) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 32) |
| **Subcategory** | Entity resolution |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Zingg AI |
| **Maintenance** | Uncertain |
| **Licence** | AGPL-3.0 (project licensing — confirm from the repository licence file; open-core model with a separate commercial offering) |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/zinggAI/zingg) · [Documentation](https://docs.zingg.ai/) |

**Scores** — relevance 2/5 · capability 4/5 · maintenance 2/5 · privacy 4/5 · usability 2/5 · licence+cost 3/5 → **weighted 56/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Spark-based entity-resolution and identity-graph tool using active learning to train match models, with blocking, deduplication and linking across large datasets.

## Journalism / investigative use case

Entity resolution at a scale beyond Splink's comfortable range: linking tens of millions of records across several large datasets — a national property register against a company registry against a sanctions list — where Spark's distribution is the only practical route.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Spark backend means genuinely large-scale resolution is possible, which is the specific gap above Splink's DuckDB comfort zone
- Active learning reduces the labelling burden, so a domain expert trains the matcher with a manageable number of judgements
- Open-source core with documentation oriented to practical deployment rather than research
- Addresses identity-graph construction, which is the shape of the problem in cross-dataset investigation

## 5. Cons

- Spark is a heavy operational dependency: for most newsroom datasets it is unjustified overhead, and standing up a cluster to resolve a few million records is the wrong trade
- Commercial product behind the open core, so feature availability and direction follow the vendor — check what is in the open version before designing around it
- Smaller community than Splink in the investigative and public-sector space, so there is less accumulated guidance for this kind of data
- Match-quality interpretation is the same hard problem as any entity resolution, and Spark's distance from the data makes iterative inspection less convenient than DuckDB-backed Splink

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. Zingg is positioned as an enterprise entity-resolution tool with an open core; I verified no journalism deployment, so newsroom use is unestablished.

## 7. Assessment

Consider it only if your record volumes genuinely exceed what Splink handles on a single machine — which for most newsroom work they will not, since Splink is comfortable into the tens of millions with DuckDB. For your profile I would default to Splink for the auditability and the absence of Spark, and keep Zingg in mind for the exceptional case of a very large multi-dataset linkage project, ideally with a data-engineering partner.

## 8. Maintenance

**Uncertain** — Verified via the GitHub API 2026-11-17 as live and non-archived, but with an open-core commercial model where the relationship between the published repository and the commercial product is not clear from metadata alone. Classified Uncertain because open-core projects can quietly shift capability to the paid tier, and this survey did not assess that.

## 9. Licensing

**Licence:** AGPL-3.0 (project licensing — confirm from the repository licence file; open-core model with a separate commercial offering) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** AGPL-family copyleft on the open core would affect offering a modified service. More importantly, verify which capabilities are in the open version versus the commercial product before designing around it.

**Licence evidence:** https://github.com/zinggAI/zingg

## 10. Costs

Open core free. Spark cluster infrastructure is the real cost and it is substantial relative to single-machine alternatives. Commercial product priced separately (not verified). Estimate.

## 11. Privacy and data flows

Self-hosted Spark keeps data on your infrastructure; a cloud Spark deployment moves it to that provider.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Spark dependency is disproportionate for most newsroom volumes; open-core capability boundary unverified

## 13. Alternatives

- [Splink](JAI-A2-48.md) — recommended: auditable match weights, DuckDB backend, no Spark, actively maintained
- [nomenklatura](JAI-A2-30.md) where data is already in FollowTheMoney
- [dedupe](JAI-A2-11.md) for small analyst-driven jobs, with its maintenance caveat

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/zinggAI/zingg
- https://docs.zingg.ai/

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

← 335. [Google Fact Check Tools API](JAI-A4-16.md) · 337. [CenAlert](SUR-B1-10.md) →
