# WebScrapBook

`OSINT-C1-40` · **70/100** · overall rank 272 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 100) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 30) |
| **Subcategory** | Annotated personal archive |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Danny Lin (danny0838) |
| **Maintenance** | Stable with low activity |
| **Licence** | MPL-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/danny0838/webscrapbook) · [Documentation](https://github.com/danny0838/webscrapbook/wiki) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 70/100**

---

## 1. Purpose

Browser extension that captures web pages into an organised personal archive with folder structure, annotations, highlighting and full-text search, optionally backed by a self-hosted server.

## Journalism / investigative use case

Build an annotated personal archive of captured pages, with highlighting and notes kept alongside the evidence — useful for a reporter working a long beat who wants their reading, marked up, in one searchable place rather than scattered across bookmarks and screenshots.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Annotation alongside capture is the distinguishing feature: your reasoning about why a page matters is stored with the page, which is exactly what is lost in a bare archive
- Optional self-hosted backend means a reporter's archive can be centralised and backed up without a third-party service
- Full-text search over captures makes an accumulated personal archive genuinely useful rather than a write-only pile
- MPL-2.0 with current activity (pushed 2026-09-28, tag 2.27.3) and a reasonable community (1,251 stars)

## 5. Cons

- Single-user tool by design: no team sharing or collaborative annotation, so it does not scale to an investigation team
- Idiosyncratic data format and a modest ecosystem, which creates a migration risk — an archive you cannot easily export into something else is a long-term liability
- No release objects on GitHub (tag 2.27.3 only), so pinning and upgrade planning are awkward
- Not WARC, so the same evidentiary limitations as other single-file approaches apply

## 6. Feedback (documented)

No individual user reports verified. Documented: 1,251 stars with 37 open issues, no release objects, latest tag 2.27.3, last push 2026-09-28, MPL-2.0. Lineage from the long-standing ScrapBook family of Firefox extensions.

## 7. Assessment

A reasonable personal-productivity choice for an individual investigator, but I would not standardise a newsroom on it because of the format lock-in and single-user design. For your profile the more durable pattern is ArchiveBox for capture plus a notes system you already trust, which separates the archive from the annotation layer and keeps both exportable. If a reporter already uses WebScrapBook happily, the self-hosted backend is worth enabling so their archive is backed up.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-28, no release objects, latest tag 2.27.3, 1,251 stars, 37 open issues. Two months since last push with ongoing tag-based versioning; a mature single-maintainer extension at steady low velocity.

## 9. Licensing

**Licence:** MPL-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** MPL-2.0 file-level copyleft on modifications; immaterial for ordinary use.

**Licence evidence:** https://github.com/danny0838/webscrapbook/blob/master/LICENSE

## 10. Costs

Free. Optional self-hosted backend is a small service. Negligible.

## 11. Privacy and data flows

Captures go to local disk or your own backend server — no third-party service involved, which is a strong position. The archive accumulates a record of a reporter's research interests, so device and backup security matter.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [ArchiveBox](OSINT-C1-28.md) plus a separate notes system for an exportable, team-visible equivalent
- [SingleFile](OSINT-C1-38.md) for capture without the archive-management layer
- Zotero for citation-oriented personal archiving with better export options

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/danny0838/webscrapbook
- https://github.com/danny0838/webscrapbook/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |

---

← 271. [unitedstates/congress](OSINT-C3-42.md) · 273. [US Senate Lobbying Disclosure Act database](SUR-B2-16.md) →
