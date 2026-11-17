# Scoop

`OSINT-C1-36` · **91/100** · overall rank 34 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 13) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 7) |
| **Subcategory** | Provenance-attested capture |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Harvard Library Innovation Lab |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/harvard-lil/scoop) · [Documentation](https://github.com/harvard-lil/scoop#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## 1. Purpose

Single-page capture engine that records a URL to WARC/WACZ with extensive provenance metadata — capture timestamps, DNS and certificate information, and optional cryptographic signing.

## Journalism / investigative use case

Capture a single official page at the moment you read it, with provenance metadata attached, so the capture stands up later as evidence of what the page said before a quiet edit — the closest thing in this catalogue to a notarised screenshot.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Provenance metadata is the differentiator: capture-time DNS and certificate details plus optional signing make the capture harder to dispute than a plain WARC, let alone a screenshot
- Built by Harvard LIL, whose work on Perma.cc gives it genuine credibility in legal-evidence contexts — relevant if a capture may end up in a filing
- MIT licensed with current releases (0.7.0, 2026-09-25, same-day push) and a small, clean backlog (13 open issues)
- Single-page scope keeps it simple and fast: one command, one evidential artefact

## 5. Cons

- Single-page scope by design — no crawling, scheduling, diffing or alerting, so it complements rather than replaces a crawler
- The detailed signing and provenance formats were not individually verified in this survey beyond the maintainers' description, so treat the cryptographic strength as documented-but-unverified here
- Node.js plus a Chromium-family browser, and replay still needs ReplayWeb.page or pywb
- Small community (217 stars), so integration knowledge is limited to the project's own documentation

## 6. Feedback (documented)

No individual user reports verified. Documented: 217 stars with 13 open issues, release 0.7.0 on 2026-09-25 with same-day push, MIT licence. Harvard LIL's broader work (Perma.cc) is well established in legal-citation preservation, which is relevant institutional context rather than direct evidence for Scoop.

## 7. Assessment

Adopt it as the capture tool for the specific pages a story will cite — the provenance metadata is exactly what you want when a government later claims the page never said that. For your profile the workflow is: browsertrix-crawler for breadth, Scoop for the handful of pages that carry the story, both into one collection with ReplayWeb.page for review. I would verify the signing format details with the maintainers before relying on cryptographic attestation in a legal context, since this survey did not.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-25, latest release 0.7.0 published the same day, 217 stars, 13 open issues. Current releases under institutional maintenance at Harvard LIL; small but well-kept.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Captured content belongs to the original publisher.

**Restrictions:** None.

**Licence evidence:** https://github.com/harvard-lil/scoop/blob/main/LICENSE

## 10. Costs

No fee. Node.js plus a browser; negligible per-capture cost. Storage for WACZ files.

## 11. Privacy and data flows

Captures are written locally to files you control with no third-party submission by default — appropriate for sensitive targets. Your capture request is visible to the target site in the normal way.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Perma.cc](OSINT-C1-37.md) (hosted, from the same lab) where a public permanent citation link is wanted
- [ArchiveWeb.page](OSINT-C1-31.md) for manual capture of authenticated pages
- [browsertrix-crawler](OSINT-C1-29.md) for multi-page capture

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/harvard-lil/scoop
- https://github.com/harvard-lil/scoop/blob/main/LICENSE

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
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 33. [pdfplumber](JAI-A2-39.md) · 35. [ShadowFinder](OSINT-C2-17.md) →
