# Unstructured

`JAI-A1-10` · **74/100** · overall rank 233 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 95) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 26) |
| **Subcategory** | Document ingestion ETL |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Unstructured Technologies |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Unstructured-IO/unstructured) · [Documentation](https://docs.unstructured.io/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 74/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Optional model-based partitioning uses models with their own licences — verify what you enable. |
| **Restrictions** | Library is permissive. The hosted API and some connectors are commercial products under separate terms. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Library free. Hosted API and enterprise features are priced separately (not verified in this survey). Self-hosted costs are CPU, or GPU if model-based partitioning is enabled. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Unstructured-IO/unstructured/blob/main/LICENSE.md
- https://github.com/Unstructured-IO/unstructured
- https://docs.unstructured.io/

---

## 1. Purpose

Open-source ETL library that partitions documents of many formats into structured elements (titles, narrative text, tables, list items) with connectors for storage systems and destinations.

## Journalism / investigative use case

Building a repeatable ingest pipeline over a mixed document set with element-level structure rather than flat text: knowing that a block is a table or a heading lets downstream search and extraction behave sensibly, which matters when the corpus is thousands of filings.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Element-level partitioning (title, narrative, table, list) is more useful than flat text for search ranking and for targeted extraction, and few open libraries provide it across formats
- Large connector ecosystem for sources and destinations, so ingest-to-index is configuration rather than code
- Apache-2.0 with very active development (0.27.37, 2026-11-06; pushed 2026-11-17) and a substantial community (15,755 stars)
- Scales to batch operation and is designed for pipelines rather than interactive use, which suits corpus work

## 5. Cons

- Commercial-product gravity: the open library is the free tier of a commercial platform, and the most convenient paths (hosted API, managed connectors) are paid — so check what you are depending on and whether a feature might move
- 456 open issues and rapid version churn (a 0.27.x line), so pinning is essential and upgrades need regression testing on your own documents
- Heavyweight dependency surface, with optional model-based partitioning that pulls in substantial extras
- Partition quality on complex PDFs is below Docling and Marker, so it is an ingest framework rather than a best-in-class parser

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 15,755 stars with 456 open issues, release 0.27.37 (2026-11-06), pushed 2026-11-17, Apache-2.0. The commercial-platform relationship is documented by the vendor; the open library is genuinely usable standalone.

## 7. Assessment

Consider it where you want an off-the-shelf ingest framework with connectors and can accept vendor-adjacent dependencies; prefer Docling plus your own orchestration where parsing fidelity and independence matter more. For your profile the risk to weigh is strategic rather than technical: building your core ingest on the free tier of a commercial product means your pipeline's future depends on that company's open-source commitment. Docling's LF AI & Data governance is a more durable foundation.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 0.27.37 (2026-11-06), 15,755 stars, 456 open issues. Same-day commits and frequent releases under commercial maintenance.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Optional model-based partitioning uses models with their own licences — verify what you enable.

**Restrictions:** Library is permissive. The hosted API and some connectors are commercial products under separate terms.

**Licence evidence:** https://github.com/Unstructured-IO/unstructured/blob/main/LICENSE.md

## 10. Costs

Library free. Hosted API and enterprise features are priced separately (not verified in this survey). Self-hosted costs are CPU, or GPU if model-based partitioning is enabled. Estimate.

## 11. Privacy and data flows

Local when self-hosted with local partitioning. Using the hosted API sends documents to the vendor — inappropriate for source material, and the easy path, so set the configuration deliberately.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [Docling](JAI-A2-12.md) for layout-aware parsing under neutral governance
- [Apache Tika](JAI-A2-02.md) plus your own orchestration for maximum format coverage
- [MarkItDown](JAI-A1-09.md) for quick triage without pipeline ambitions

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Unstructured-IO/unstructured
- https://docs.unstructured.io/
- https://github.com/Unstructured-IO/unstructured/blob/main/LICENSE.md

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

← 232. [M-Lab NDT server, ndt7 client and MSAK](SUR-B1-11.md) · 234. [wabac.js](OSINT-C1-33.md) →
