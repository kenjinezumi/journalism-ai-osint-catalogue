# warcprox

`OSINT-C1-42` · **64/100** · overall rank 293 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 110) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 34) |
| **Subcategory** | Recording proxy |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Internet Archive |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-2.0-or-later (declared in packaging metadata; no LICENSE file and GitHub reports no SPDX) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/internetarchive/warcprox) · [Documentation](https://github.com/internetarchive/warcprox#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 3/5 · usability 2/5 · licence+cost 4/5 → **weighted 64/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

HTTP/HTTPS man-in-the-middle proxy that writes every request and response passing through it into WARC files, used as the recording layer for browser-driven crawls.

## Journalism / investigative use case

Record every request made during a browsing or scraping session into WARC, so collection and evidence capture happen in one pass — you browse or scrape normally and come away with an evidentiary record of everything the server actually sent.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Capture-by-proxy means any tool or browser you point at it produces WARC output, including tools that have no archiving support of their own — a genuinely elegant architecture
- Records the actual HTTP exchanges including headers, which is what gives WARC its evidentiary value over rendered snapshots
- Apache-adjacent open licensing, actively released (v2.13.1, 2026-05-11) under Internet Archive maintenance, and the recording layer beneath brozzler
- Pairs with any scraping workflow, so an existing Scrapy or Playwright collection can become evidentiary with no code changes

## 5. Cons

- All proxied traffic, including credentials and session tokens, is written into your WARCs — a serious handling consideration that is easy to overlook and makes the output highly sensitive
- Requires installing a local CA certificate in the browser to intercept TLS, which is a security-posture change on the capture machine that must be reversed afterwards
- The licence is declared only in packaging metadata rather than a LICENSE file (GitHub reports no SPDX), so the GPL-2.0-or-later position needs confirmation for compliance records
- Operator-level tool with 27 open issues and six months since the last push (2026-06-17); not something a reporter would run

## 6. Feedback (documented)

No individual user reports verified. Documented: 469 stars with 27 open issues, release v2.13.1 (2026-05-11), last push 2026-06-17, SPDX none with GPL-2.0-or-later declared in packaging metadata (verified session 1, retained). Production use at the Internet Archive via brozzler.

## 7. Assessment

Powerful and genuinely useful for turning any collection into evidence, with two cautions I would treat as mandatory for your context. First, WARCs produced by proxying a logged-in session contain your credentials and tokens — encrypt them and restrict access, or scrub before sharing. Second, the local CA certificate weakens the capture machine's TLS trust model while installed, so use a dedicated capture VM rather than a reporter's daily laptop.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-06-17, latest release v2.13.1 (2026-05-11), SPDX none, 469 stars, 27 open issues. Five months since last push on a mature component under institutional maintenance; stable rather than declining, since brozzler's continued releases depend on it.

## 9. Licensing

**Licence:** GPL-2.0-or-later (declared in packaging metadata; no LICENSE file and GitHub reports no SPDX) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** GPL-2.0-or-later per packaging metadata. The absence of a LICENSE file is a compliance-record weakness — cite the packaging metadata explicitly if your legal team requires it.

**Licence evidence:** https://github.com/internetarchive/warcprox

## 10. Costs

No fee. A small Python service plus WARC storage. Negligible infrastructure; non-trivial setup time for the CA certificate arrangement.

## 11. Privacy and data flows

All proxied traffic, including credentials and session tokens, is written into your WARCs — treat output as highly sensitive. The local CA certificate installation changes the trust posture of the capture machine for as long as it is present.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- WARCs contain credentials and session tokens from proxied traffic; requires installing a local CA certificate

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md), which handles capture internally without a proxy or CA certificate
- [mitmproxy](SUR-B2-06.md) for traffic inspection without WARC output
- [Scoop](OSINT-C1-36.md) or ArchiveWeb.page for capture without changing the machine's trust store

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/internetarchive/warcprox

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

← 292. [GraphSense](OSINT-C3-21.md) · 294. [Katna](OSINT-C2-11.md) →
