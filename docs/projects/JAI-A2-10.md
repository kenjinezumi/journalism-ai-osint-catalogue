# datasketch

`JAI-A2-10` · **83/100** · overall rank 117 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 49) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 29) |
| **Subcategory** | Near-duplicate detection |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Eric Zhu |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ekzhu/datasketch) · [Documentation](https://ekzhu.com/datasketch/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 83/100**

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

**Recorded cost detail.** No fee. CPU-only and cheap; memory scales with the number of hashed documents. A persistent LSH index adds a Redis instance. Infrastructure estimate only.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ekzhu/datasketch/blob/master/LICENSE
- https://github.com/ekzhu/datasketch
- https://ekzhu.com/datasketch/

---

## 1. Purpose

Probabilistic data-structure library providing MinHash, MinHash LSH, LSH Forest, Weighted MinHash, HyperLogLog and LSH Ensemble for sub-linear similarity search over large sets.

## Journalism / investigative use case

Deduplicating a leak before anyone reads it: collapse thousands of near-identical email chains, repeated attachments and boilerplate contracts into representative clusters, so a reporting team reads 40,000 distinct documents instead of 200,000 mostly-redundant ones.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Solves the single highest-leverage preprocessing problem in leak work — redundancy — and does so at a scale where exact comparison is impossible
- MinHash LSH with Redis or Cassandra backing lets the index persist and grow across ingest batches rather than being rebuilt
- Small, well-documented, dependency-light (NumPy), and easy to reason about when you must defend the methodology
- Steady releases (v2.0.0, 2026-07-05) and 2,980 stars with a manageable issue count

## 5. Cons

- Approximate by design: thresholds must be tuned and will produce false pairs, so a human-visible review step is mandatory before anything is discarded
- Shingling choices (word vs character n-grams, size) materially change results, and there is no newsroom-oriented guidance on picking them
- No document-level UI or report — you are building the dedup workflow around it
- Says nothing about which duplicate is canonical; provenance decisions (which copy is the evidence of record) are entirely yours

## 6. Feedback (documented)

No user reports collected. 2,980 stars with 71 open issues on 2026-11-17 indicates a stable, maintained library with modest support load. No journalism-specific deployment verified.

## 7. Assessment

Unglamorous and high value: deduplication is where leak processing time is actually won or lost, and this is the right primitive for it. For your profile I would wire it into ingest immediately after text extraction, keep every duplicate (never delete — mark and cluster), and record the shingle and threshold parameters as part of the corpus methodology so a later challenge can be answered.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-26, latest release v2.0.0 (2026-07-05), 2,980 stars, 71 open issues. A 2.0 release in 2026 plus commits within the last month; low-churn library behaviour, judged active on release substance.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/ekzhu/datasketch/blob/master/LICENSE

## 10. Costs

No fee. CPU-only and cheap; memory scales with the number of hashed documents. A persistent LSH index adds a Redis instance. Infrastructure estimate only.

## 11. Privacy and data flows

Fully local. If you configure a Redis or Cassandra backend, the hashes (not the documents) live there — still treat that store as sensitive, since MinHash signatures over a confidential corpus are themselves disclosive about its contents.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ImageHash](OSINT-C2-05.md) / imagededup for the same problem on images
- [RapidFuzz](JAI-A2-43.md) for short-string rather than document-level similarity
- [Splink](JAI-A2-48.md) where the goal is record linkage with probabilities rather than near-duplicate collapse

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ekzhu/datasketch
- https://ekzhu.com/datasketch/
- https://github.com/ekzhu/datasketch/blob/master/LICENSE

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

← 116. [Browsertrix](OSINT-C1-30.md) · 118. [Huginn](JAI-A1-16.md) →
