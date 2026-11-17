# ArchiveWeb.page

`OSINT-C1-31` · **94/100** · overall rank 9 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 6) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 4) |
| **Subcategory** | Manual browser capture |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/archiveweb.page) · [Documentation](https://archiveweb.page/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 94/100**

---

## 1. Purpose

Chromium browser extension and desktop app that records your browsing session into a WARC/WACZ archive, capturing exactly what you saw including pages behind authentication.

## Journalism / investigative use case

Manually capture a social post, story or logged-in page exactly as seen, producing a replayable file for the evidence locker — the only practical way to preserve content behind a login you legitimately hold, which automated crawlers cannot reach.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Captures authenticated and interactive content that no crawler can reach, which covers a large share of what actually needs preserving (social posts, logged-in dashboards, paywalled filings)
- Produces WACZ — the same evidentiary format as browsertrix-crawler — so manual captures sit alongside automated ones in one collection
- Usable by a reporter with no technical skill: start recording, browse, export
- Actively maintained (v0.17.1, 2026-09-04; pushed 2026-11-09) with a substantial community (1,629 stars)

## 5. Cons

- Manual, one-page-at-a-time workflow, so it does not scale and depends on reporter discipline at the moment of capture
- Large captures strain browser storage, and losing an unexported archive to a browser profile reset is a real failure mode
- Chromium-only, which is a constraint for newsrooms standardised on Firefox
- AGPL-3.0 matters only if you redistribute a modified version; 115 open issues reflect the variety of sites users try to capture

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,629 stars with 115 open issues, release v0.17.1 (2026-09-04), pushed 2026-11-09. Part of the Webrecorder suite used across the web-archiving community.

## 7. Assessment

Deploy it to reporters as the standard way to preserve anything they see that matters — the authenticated-capture capability has no real alternative. For your profile the operational rules are: export to a WACZ file immediately rather than leaving archives in the browser profile, and be aware that a capture of a logged-in session contains session material and personal account context, so handle the file as sensitive. Pair with ReplayWeb.page so colleagues can open captures without any setup.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-09, latest release v0.17.1 (2026-09-04), 1,629 stars, 115 open issues. Regular releases from a funded organisation; part of a coherently maintained suite.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Captured content belongs to the original publishers.

**Restrictions:** AGPL-3.0; immaterial for ordinary use as an extension.

**Licence evidence:** https://github.com/webrecorder/archiveweb.page/blob/main/LICENSE

## 10. Costs

Free. No infrastructure. Storage is local browser profile until exported.

## 11. Privacy and data flows

The archive is stored in the browser profile until exported and nothing is uploaded by default — a strong privacy position. The caveat is the content: capturing a logged-in page records your session context, so exported files may contain account identifiers and should be treated accordingly.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [SingleFile](OSINT-C1-38.md) for a lighter single-HTML snapshot (weaker provenance, no WARC)
- [Scoop](OSINT-C1-36.md) for a provenance-attested single-page capture from the command line
- [browsertrix-crawler](OSINT-C1-29.md) where the content is publicly reachable and automation is possible

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/archiveweb.page
- https://archiveweb.page/
- https://github.com/webrecorder/archiveweb.page/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 8. [OpenSanctions (dataset)](OSINT-C3-01.md) · 10. [FreshRSS](JAI-A1-03.md) →
