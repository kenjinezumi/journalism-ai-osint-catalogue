# Datasette

`JAI-A2-09` · **93/100** · overall rank 21 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 7) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 4) |
| **Subcategory** | Data publishing and exploration |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Simon Willison |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/simonw/datasette) · [Documentation](https://docs.datasette.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 93/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material; permissive and safe for commercial publishing products. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Self-hosting is trivially cheap (a small VM or container). If you use the publish path to a commercial PaaS you pay that provider's rates — verify at point of use; not priced here. Operating effort is low, which is much of the value.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/simonw/datasette/blob/main/LICENSE
- https://github.com/simonw/datasette
- https://docs.datasette.io/

---

## 1. Purpose

Web application that serves one or more SQLite databases as a browsable, queryable, JSON-API-exposed website, with a large plugin ecosystem and publishing subcommands.

## Journalism / investigative use case

The fastest route from 'we have extracted the leak into a table' to 'reporters can search it': point Datasette at a SQLite file of document text and metadata and the team has faceted search, saved queries and CSV export within an hour. Also the standard way to publish a cleaned subset alongside a story so readers can check the data themselves.

## 2. Audience

engineer, newsroom analyst, journalist

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Time-to-usefulness is unmatched in this catalogue — a single command turns a file into a shared research tool, which is decisive under deadline
- Plugin ecosystem (datasette-search-all, full-text search, cluster maps, graphs) covers most newsroom asks without custom code
- Read-only by design, so handing reporters a URL cannot corrupt the dataset — a genuine safety property in a shared investigation
- Exceptional documentation and an articulated data-journalism design philosophy; the maintainer is embedded in this community

## 5. Cons

- SQLite FTS is excellent for structured extracts but is not a substitute for a sharded index over millions of full documents — it will not replace Solr/Elasticsearch at leak scale
- The publish subcommands intentionally push data to third-party hosts (Vercel, Cloud Run, Fly); running one against unvetted data is a one-command leak, and that risk sits right next to the normal workflow
- 666 open issues across the core project and a long-running 1.0 alpha line, so the stable release (0.65.x) and the alpha (1.0a43) diverge and plugin compatibility needs checking
- Read-only means annotation, tagging and collaborative review must live in another tool

## 6. Feedback (documented)

No individual reports verified, but Datasette's role in data journalism is documented by the project itself and by its plugin ecosystem's orientation (publishing, mapping, CSV export). 11,590 stars, 666 open issues. I did not verify specific newsroom deployments, so treat named-outlet claims as unestablished.

## 7. Assessment

I would adopt this immediately and keep it permanently in the toolkit — it is the lowest-effort, highest-return item in the document pillar. The one governance rule I would write down: `datasette publish` is forbidden on any database derived from source material, because the gap between 'share internally' and 'upload to a public host' is a single subcommand. Pair with a real search engine for full-document scale.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 0.65.6 (2026-11-15), current tag 1.0a43, 11,590 stars, 666 open issues. Frequent point releases on the stable line plus an in-progress 1.0; the open-issue count is large but the release cadence is the stronger signal.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material; permissive and safe for commercial publishing products.

**Licence evidence:** https://github.com/simonw/datasette/blob/main/LICENSE

## 10. Costs

No fee. Self-hosting is trivially cheap (a small VM or container). If you use the publish path to a commercial PaaS you pay that provider's rates — verify at point of use; not priced here. Operating effort is low, which is much of the value.

## 11. Privacy and data flows

Local and self-hostable with no outbound calls in normal operation. The explicit exception is the publishing subcommands, which are designed to move data off-premises; treat them as a separate, policy-controlled action rather than part of the analysis workflow.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Apache Solr](JAI-A2-01.md) or OpenSearch for full-document scale
- [VisiData](JAI-A2-57.md) for terminal-based exploration of the same data
- DuckDB plus a notebook where analysis rather than sharing is the goal

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/simonw/datasette
- https://docs.datasette.io/
- https://github.com/simonw/datasette/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 20. [changedetection.io](SUR-B1-15.md) · 22. [SecureDrop](SUR-B3-01.md) →
