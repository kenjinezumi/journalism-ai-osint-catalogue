# libpff

`JAI-A1-12` · **87/100** · overall rank 58 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 22) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 5) |
| **Subcategory** | Email archive parsing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Joachim Metz (libyal) |
| **Maintenance** | Actively maintained |
| **Licence** | LGPL-3.0 |
| **Licence type** | Weak copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/libyal/libpff) · [Documentation](https://github.com/libyal/libpff/wiki) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 87/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Weak copyleft |
| **Exact licence (as recorded)** | LGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | LGPL-3.0 permits linking from your own tooling provided the library remains replaceable; modifications must be shared. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. C build toolchain; disk for extracted messages and attachments, which can exceed the PST size. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/libyal/libpff/blob/main/COPYING.LESSER
- https://github.com/libyal/libpff
- https://github.com/libyal/libpff/wiki

---

## 1. Purpose

Library and tools to read Microsoft Personal Folder File formats (PST, OST, PAB), extracting messages, attachments, folder structure and metadata including recovery of deleted items.

## Journalism / investigative use case

Leaked mailboxes arrive as PST files, and this is the tool that opens them: extract messages, folder hierarchies and attachments at scale, including items deleted but still recoverable — which in a mailbox leak is frequently where the material nobody intended to keep is found.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Deleted-item recovery from PST is a distinctive investigative capability: the messages someone deleted are often the most significant, and generic mail converters do not retrieve them
- Reverse-engineered format documentation published alongside the code, so the extraction is explicable and defensible if challenged
- LGPL-3.0 with active maintenance (pushed 2026-11-08, tag 20261030) from a maintainer with a long forensic-tooling record
- Handles the awkward older PST variants that modern tools reject, which matters because leaked mailboxes are frequently old

## 5. Cons

- Low-level C library with tooling that assumes forensic literacy: errors are cryptic and the output needs post-processing before reporters can use it
- No releases in the GitHub sense (date-stamped tags only), so pinning means recording a tag and the documentation is wiki-based
- 375 stars and 16 open issues — a specialist project where you may be on your own for an unusual file
- Extraction only: deduplication, threading, search and review all happen in other tools, so it is one stage of a mailbox pipeline

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 375 stars with 16 open issues, latest tag 20261030, pushed 2026-11-08, LGPL-3.0. The libyal projects are standard components in digital-forensics tooling, which is the relevant adjacent evidence.

## 7. Assessment

Adopt it as the PST entry point for any mailbox leak, and plan the pipeline around it: libpff to extract, Tika or your own code to normalise, datasketch to deduplicate threads, and a search index for review. For your profile the deleted-item recovery is the detail worth knowing about and building into the process explicitly, because it will not happen by default and it is frequently where the story is.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-08, no release objects, latest tag 20261030, 375 stars, 16 open issues. Date-stamped tag releases on a regular cadence from a long-committed maintainer.

## 9. Licensing

**Licence:** LGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** LGPL-3.0 permits linking from your own tooling provided the library remains replaceable; modifications must be shared.

**Licence evidence:** https://github.com/libyal/libpff/blob/main/COPYING.LESSER

## 10. Costs

No fee. C build toolchain; disk for extracted messages and attachments, which can exceed the PST size. Estimate.

## 11. Privacy and data flows

Entirely local. The extracted mailbox is among the most sensitive material a newsroom handles — encrypted storage and strict access control are essential.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [libratom](JAI-A1-13.md) for a Python-native approach to PST and mbox with research-oriented tooling
- readpst (libpst) as an alternative extractor
- [Apache Tika](JAI-A2-02.md), which can read PST via libraries but without deleted-item recovery

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/libyal/libpff
- https://github.com/libyal/libpff/wiki
- https://github.com/libyal/libpff/blob/main/COPYING.LESSER

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 57. [NetworkX](OSINT-C3-31.md) · 59. [OpenRefine](JAI-A2-36.md) →
