# monolith

`OSINT-C1-39` · **84/100** · overall rank 110 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 33) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 12) |
| **Subcategory** | Single-page capture |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Sunshine (Y2Z) |
| **Maintenance** | Actively maintained |
| **Licence** | 0BSD |
| **Licence type** | Public domain |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Y2Z/monolith) · [Documentation](https://github.com/Y2Z/monolith#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 84/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Public domain |
| **Exact licence (as recorded)** | 0BSD |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Captured content belongs to the original publisher. |
| **Restrictions** | None at all — 0BSD imposes no conditions, not even attribution. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. A single binary; negligible resources. Disk for output files.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Y2Z/monolith/blob/master/LICENSE
- https://github.com/Y2Z/monolith

---

## 1. Purpose

Rust CLI that downloads a web page and embeds all assets (CSS, images, fonts, scripts) into a single portable HTML file.

## Journalism / investigative use case

Scriptable bulk preservation of many URLs as portable single-file snapshots for later reading or diffing — the automation counterpart to SingleFile, suitable for preserving a list of a few thousand pages overnight.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- 0BSD licence — effectively public domain, the most permissive in this catalogue, with no attribution or copyleft obligation at all
- Single static Rust binary with no runtime dependencies, so it deploys anywhere including minimal containers and air-gapped machines
- Scriptable for bulk work, which SingleFile's extension form is not
- Actively maintained (v2.12.0, 2026-11-02; pushed 2026-11-13) with a large community (15,609 stars)

## 5. Cons

- No JavaScript execution path, so pages whose content is rendered client-side come out empty or partial — a severe limitation for modern portals and social media
- Not WARC: same evidentiary weakness as SingleFile, with no headers or capture provenance
- Embedded-asset output alters the document and can produce very large files for media-heavy pages
- 49 open issues; asset-inlining edge cases on complex sites are the recurring theme

## 6. Feedback (documented)

No individual user reports verified. Documented: 15,609 stars with 49 open issues, release v2.12.0 (2026-11-02), pushed 2026-11-13, 0BSD licence. The absence of JavaScript execution is documented by the project and is the main functional boundary.

## 7. Assessment

The right tool for bulk preservation of static pages — statutes, press-release archives, document indexes — where you want portable files and no infrastructure. For anything JavaScript-rendered it will fail quietly, which is the trap: check a sample before running a large job. For your profile the 0BSD licence is worth noting because it makes monolith trivially embeddable in any internal tooling with zero legal consideration, which is rare.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release v2.12.0 (2026-11-02), 15,609 stars, 49 open issues. Regular releases with current commits and a large community.

## 9. Licensing

**Licence:** 0BSD _(SPDX verified)_

**Model / data licence:** n/a. Captured content belongs to the original publisher.

**Restrictions:** None at all — 0BSD imposes no conditions, not even attribution.

**Licence evidence:** https://github.com/Y2Z/monolith/blob/master/LICENSE

## 10. Costs

No fee. A single binary; negligible resources. Disk for output files.

## 11. Privacy and data flows

Fetches target assets from your host and writes a local file; nothing is uploaded. The target sees your requests.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- No JavaScript execution — fails silently on client-rendered pages

## 13. Alternatives

- [SingleFile](OSINT-C1-38.md) for interactive and authenticated capture
- [browsertrix-crawler](OSINT-C1-29.md) where JavaScript rendering and WARC are needed
- wget --warc for bulk static capture with proper WARC output

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Y2Z/monolith
- https://github.com/Y2Z/monolith/blob/master/LICENSE

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

← 109. [Miniflux](JAI-A1-04.md) · 111. [Paperless-ngx](JAI-A2-38.md) →
