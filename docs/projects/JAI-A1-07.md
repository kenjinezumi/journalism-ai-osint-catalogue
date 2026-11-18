# feedparser

`JAI-A1-07` · **86/100** · overall rank 79 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 30) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 6) |
| **Subcategory** | Feed parsing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Kurt McKee (kurtmckee) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause (resolved by reading the repository licence; GitHub reports NOASSERTION — independently recorded in session 1's a1disc/notes.md) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/kurtmckee/feedparser) · [Documentation](https://feedparser.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 5/5 → **weighted 86/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause (resolved by reading the repository licence; GitHub reports NOASSERTION — independently recorded in session 1's a1disc/notes.md) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, negligible resources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/kurtmckee/feedparser/blob/develop/LICENSE
- https://github.com/kurtmckee/feedparser
- https://feedparser.readthedocs.io/
- `../sources/recovered/a1disc/notes.md`

---

## 1. Purpose

Python library that parses RSS, Atom and RDF feeds of any version, normalising their inconsistencies and handling malformed markup, date formats and character encodings.

## Journalism / investigative use case

The parsing layer in any custom monitoring pipeline: real-world feeds from government and regional sources are frequently malformed, use obsolete formats or carry broken date fields, and feedparser absorbs that mess so your code sees consistent records.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Handles the pathological real-world feeds that a strict XML parser rejects — which is most government and small-publisher feeds, so this is where the practical value sits
- Date normalisation across a dozen malformed conventions is work you would otherwise redo badly, and dates matter for monitoring
- Licence resolved in this survey: BSD-2-Clause (GitHub reports NOASSERTION), actively maintained (v6.0.14, 2026-07-30; pushed 2026-11-02)
- Two decades of accumulated edge-case handling with 2,458 stars; stable API so pipelines keep working

## 5. Cons

- GitHub reports SPDX NOASSERTION, so automated licence scanning does not resolve it — the BSD-2-Clause position comes from reading the repository and should be recorded explicitly
- Parsing only: no fetching, scheduling, deduplication or storage, so it is one component among several
- 123 open issues on a mature library, mostly long-tail format edge cases
- Feed parsing is a solved problem, so the library's ceiling is 'does not get in the way' rather than any differentiating capability

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 2,458 stars with 123 open issues, release v6.0.14 (2026-07-30), pushed 2026-11-02, SPDX NOASSERTION with the licence resolved to BSD-2-Clause — consistent with session 1's a1disc/notes.md, which independently recorded feedparser as BSD-2-Clause after reading the licence text.

## 7. Assessment

Adopt it whenever you write feed-handling code rather than parsing XML yourself — the malformed-feed handling alone justifies it. For your profile this is uninteresting infrastructure that prevents a specific recurring bug: a monitoring job that silently drops items because one publisher emits a non-standard date. Record the BSD-2-Clause licence reference in your compliance notes given the SPDX gap.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-02, latest release v6.0.14 (2026-07-30), 2,458 stars, 123 open issues, SPDX NOASSERTION. Regular releases on a mature library from a committed maintainer.

## 9. Licensing

**Licence:** BSD-2-Clause (resolved by reading the repository licence; GitHub reports NOASSERTION — independently recorded in session 1's a1disc/notes.md) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/kurtmckee/feedparser/blob/develop/LICENSE

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Pure parsing; no network calls of its own.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [FreshRSS](JAI-A1-03.md) or Miniflux if you want a reader rather than a library
- Direct XML parsing — not recommended, given real-world feed quality
- [trafilatura](JAI-A1-01.md) for article content once a feed gives you URLs

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/kurtmckee/feedparser
- https://feedparser.readthedocs.io/
- `../sources/recovered/a1disc/notes.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 78. [warcio](OSINT-C1-41.md) · 80. [meteostat](OSINT-C2-40.md) →
