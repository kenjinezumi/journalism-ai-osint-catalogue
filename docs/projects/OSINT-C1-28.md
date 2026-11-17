# ArchiveBox

`OSINT-C1-28` · **91/100** · overall rank 30 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 12) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 6) |
| **Subcategory** | Self-hosted archiving |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Nick Sweeting and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ArchiveBox/ArchiveBox) · [Documentation](https://docs.archivebox.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## 1. Purpose

Self-hosted web-archiving application that takes URLs from many input formats and saves each as HTML, PDF, screenshot, WARC, SingleFile, readability text, media and more, with a browsable index.

## Journalism / investigative use case

Build your own tamper-evident archive of official pages and documents on a schedule, so that when an agency rewrites or deletes a page you hold dated local copies rather than depending on a third-party archive — and because it saves several formats per URL, you have both a readable copy and a WARC.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Multi-format capture per URL is the distinguishing feature: a PDF for an editor, a screenshot for a story, a WARC for evidence, and readability text for search — all from one ingest
- Everything stored on your own disk by default, with a browsable index that a non-engineer can use
- Very large community (29,045 stars) and active development (pushed 2026-11-17, release v0.9.77 2026-10-27)
- Accepts input from browser bookmarks, RSS, text files and more, so getting URLs in is never the obstacle

## 5. Cons

- Not a change-detection tool: it captures and preserves, and diffing between snapshots is explicitly not its job — pair it with webchanges or EDGI tooling for monitoring
- Heavy dependency surface (Chromium/Playwright, wget, curl, yt-dlp, singlefile, readability and other extractor binaries), so installs break and upgrades need care
- Long-running release-candidate versions (current tag v0.9.78rc242) blur the stable/unstable line and make pinning a judgement call
- Archive size grows quickly with multi-format capture — storage planning is a real requirement, not an afterthought

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 29,045 stars with 157 open issues, release v0.9.77 (2026-10-27), current tag v0.9.78rc242, pushed 2026-11-17. The extended release-candidate numbering is visible in the tag itself and is a genuine versioning concern for operators.

## 7. Assessment

My recommended default for a newsroom's own archive of source pages, because the multi-format output serves the editorial, evidentiary and search needs simultaneously. For your profile: pin to a stable release rather than an rc tag, plan storage explicitly (multi-format capture is several times the page size), and keep the instance internal — an exposed ArchiveBox index is a list of everything your newsroom has found interesting. Note the optional extractors that can submit URLs to the Internet Archive; disable those for sensitive targets.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.9.77 (2026-10-27), current tag v0.9.78rc242, 29,045 stars, 157 open issues. Same-day commits and recent releases with a very large community; the prolonged rc series is a release-engineering characteristic rather than a decline signal.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Archived content belongs to the original publishers.

**Restrictions:** None material. Note the bundled extractors carry their own licences (yt-dlp is Unlicense, SingleFile AGPL-3.0), which matters only if you redistribute a bundle.

**Licence evidence:** https://github.com/ArchiveBox/ArchiveBox/blob/dev/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a container host plus substantial storage — budget several times the raw page size per URL because of multi-format capture; a few thousand pages with media can reach hundreds of GB. Assumptions: self-hosted Docker, default extractor set.

## 11. Privacy and data flows

Everything is stored on your own disk by default. Two things to control: optional extractors can submit URLs to the Internet Archive (disclosing your interest to a third party and making the URL public), and the index itself is a sensitive artefact that must not be publicly reachable.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Browsertrix](OSINT-C1-30.md) (platform) for team-scale crawling with managed replay
- [Scoop](OSINT-C1-36.md) for single-page captures with provenance attestation
- [pywb](OSINT-C1-27.md) plus browsertrix-crawler for a WARC-first architecture

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ArchiveBox/ArchiveBox
- https://docs.archivebox.io/
- https://github.com/ArchiveBox/ArchiveBox/blob/dev/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 29. [QGIS](OSINT-C2-19.md) · 31. [Docling](JAI-A2-12.md) →
