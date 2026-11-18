# Miniflux

`JAI-A1-04` · **84/100** · overall rank 109 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 45) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 12) |
| **Subcategory** | Feed aggregation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Frédéric Guillot |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/miniflux/v2) · [Documentation](https://miniflux.app/docs/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. A small VM plus PostgreSQL. The project also offers a paid hosted version — prices not verified here. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/miniflux/v2/blob/main/LICENSE
- https://github.com/miniflux/v2
- https://miniflux.app/docs/

---

## 1. Purpose

Minimalist self-hosted feed reader written in Go, with a single binary, PostgreSQL storage, filtering rules, full-text extraction and a Google Reader-compatible API.

## Journalism / investigative use case

The same monitoring role as FreshRSS with a deliberately smaller surface: a single Go binary and a database, which suits an engineer who wants feed infrastructure that will keep working for years without attention.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Single static binary plus PostgreSQL is about as low-maintenance as self-hosted infrastructure gets — a meaningful advantage when the alternative is another PHP application to patch
- Opinionated minimalism means fewer features to misconfigure and a much smaller attack surface than a feature-rich reader
- Apache-2.0 with consistent releases (2.3.5, 2026-11-02; pushed 2026-11-12) and a healthy tracker (290 open issues against 9,949 stars)
- Google Reader-compatible API means existing mobile and desktop clients work, so reporters can use whatever reader they like

## 5. Cons

- Deliberately feature-light: no labels-and-rules sophistication to match FreshRSS, so managing several hundred feeds is less comfortable
- Single-maintainer project, which for infrastructure you depend on for years is a real consideration even with the current good cadence
- PostgreSQL requirement adds a stateful dependency that the single-binary story otherwise avoids
- Same feed-discovery gap as any reader: sources without feeds need a generator

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 9,949 stars with 290 open issues, release 2.3.5 (2026-11-02), pushed 2026-11-12, Apache-2.0. Known in the self-hosting community specifically for its minimalism and stability.

## 7. Assessment

A reasonable alternative to FreshRSS where you value operational simplicity over feature depth, which for an engineering-led team is a legitimate preference. For your profile I would choose FreshRSS if non-technical reporters will use the web interface and manage their own filters, and Miniflux if the reader is primarily a machine-readable monitoring substrate with reporters using their own clients. Either is better than none, and the choice is lower-stakes than it looks.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-12, latest release 2.3.5 (2026-11-02), 9,949 stars, 290 open issues. Regular releases from a single long-committed maintainer.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/miniflux/v2/blob/main/LICENSE

## 10. Costs

No fee. A small VM plus PostgreSQL. The project also offers a paid hosted version — prices not verified here. Estimate.

## 11. Privacy and data flows

Self-hosted; feed list and reading behaviour stay internal.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [FreshRSS](JAI-A1-03.md) for richer filtering and a reporter-facing interface
- [RSSHub](JAI-A1-05.md) for generating missing feeds
- Commercial readers — avoid for monitoring, since the feed list reveals editorial interests

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/miniflux/v2
- https://miniflux.app/docs/
- https://github.com/miniflux/v2/blob/main/LICENSE

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

← 108. [VisiData](JAI-A2-57.md) · 110. [monolith](OSINT-C1-39.md) →
