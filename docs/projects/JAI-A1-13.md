# libratom

`JAI-A1-13` · **75/100** · overall rank 209 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 84) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 21) |
| **Subcategory** | Email archive parsing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | RATOM project (University of North Carolina) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/libratom/libratom) · [Documentation](https://libratom.github.io/libratom/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

---

## 1. Purpose

Python library and CLI for parsing and processing PST and mbox email archives, extracting messages and attachments, generating reports and running spaCy entity extraction over message bodies.

## Journalism / investigative use case

A Python-native route into a leaked mailboxes with entity extraction built in: parse the PST, generate a report of senders, recipients and date ranges, and extract named entities from message bodies — a usable first pass on a mailbox without assembling four tools.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Python-native with integrated entity extraction, so a first-pass analysis of a mailbox (who, when, which names recur) is a single command rather than a pipeline project
- Built for archival processing of email collections by a research project focused on exactly that problem, so the reporting output is designed for exploring a collection
- MIT licensed and simple enough to read, with a clean tracker (7 open issues)
- Handles both PST and mbox, covering the two formats leaked mail actually arrives in

## 5. Cons

- Maintenance has slowed: last push 2026-01-31 with no release objects (tag 0.7.1), ten months before this survey — a research-project cadence
- Does not recover deleted items the way libpff does, so for the forensically interesting content you still need libpff
- Small community (130 stars), so unusual archives may need your own debugging
- Entity extraction inherits spaCy's limitations on OCR-noisy or non-English content, and mailbox text is often multilingual

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 130 stars with 7 open issues, no release objects, latest tag 0.7.1, last push 2026-01-31, MIT licence. The RATOM project's archival-email focus is documented and is the relevant context for the design.

## 7. Assessment

Useful as the convenient first pass on a mailbox, with libpff behind it for depth. For your profile the pattern I would use is: libratom for the quick who-talked-to-whom-and-when report that tells you whether the mailbox matters, then libpff plus a proper pipeline if it does. The slowing maintenance is tolerable for a parsing library but means pinning and being ready to own it.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-01-31, no release objects, latest tag 0.7.1, 130 stars, 7 open issues. Ten months without activity on a research-funded project — declining rather than dormant, with no deprecation notice.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** spaCy models used for entity extraction carry their own per-pipeline terms.

**Restrictions:** None material for the library.

**Licence evidence:** https://github.com/libratom/libratom/blob/master/LICENSE

## 10. Costs

No fee. CPU; disk for extracted content. Estimate.

## 11. Privacy and data flows

Entirely local processing of highly sensitive material; the same handling obligations as any mailbox extraction apply.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [libpff](JAI-A1-12.md) for deeper extraction including deleted items
- [Apache Tika](JAI-A2-02.md) for format coverage without email-specific reporting
- ePADD for archival email appraisal with a review interface

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/libratom/libratom
- https://libratom.github.io/libratom/
- https://github.com/libratom/libratom/blob/master/LICENSE

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

← 208. [dnstwist](OSINT-C3-25.md) · 210. [python-overpy](OSINT-C2-25.md) →
