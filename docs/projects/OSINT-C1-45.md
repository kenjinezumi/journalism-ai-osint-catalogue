# yt-dlp

`OSINT-C1-45` · **95/100** · overall rank 6 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 3) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 2) |
| **Subcategory** | Media capture |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | yt-dlp community |
| **Maintenance** | Actively maintained |
| **Licence** | Unlicense |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/yt-dlp/yt-dlp) · [Documentation](https://github.com/yt-dlp/yt-dlp#readme) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 95/100**

---

## 1. Purpose

Command-line media downloader supporting well over a thousand sites, retrieving video, audio, subtitles, thumbnails and uploader metadata at the highest available quality, with extensive format and post-processing control.

## Journalism / investigative use case

The workhorse for securing a copy of social video before deletion — pulling the highest available bitrate (crucial because compression destroys the artefacts forensic analysis relies on), plus uploader metadata, upload timestamps, subtitles and thumbnails. For verification work, the bitrate point is decisive: a re-encoded copy from a screen recording is forensically useless.

## 2. Audience

journalist, newsroom analyst, engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Highest-available-quality retrieval preserves the forensic signal that any re-encoding destroys, which makes it the correct first step before any media verification
- Captures uploader metadata, upload timestamps, subtitles and thumbnails alongside the media — often the evidentiary context that matters more than the video itself
- Unlicense (public domain) and extraordinarily active (208,589 stars, release 2026.10.26, pushed 2026-11-17), with extractors updated continuously as platforms change
- Covers over a thousand sites, so it works on the regional and niche platforms where much relevant material actually lives

## 5. Cons

- A capture tool with no verification logic and no authenticity judgement — it tells you nothing about whether the content is real
- Extractors break frequently when platforms change, so you must pin or update often and expect occasional silent format downgrades that quietly reduce quality
- Contacts the target platform directly from the operator's machine, so your IP and request pattern are visible to that platform — and for a high-volume capture campaign that is an identifiable footprint
- Downloading may breach platform terms of service and, depending on jurisdiction and purpose, raises copyright questions that are a legal rather than technical matter

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 208,589 stars with 2,790 open issues, release 2026.10.26, pushed 2026-11-17 — the largest community in this catalogue, with a backlog that reflects the constant churn of platform extractors rather than neglect. The project itself notes platform-specific constraints in its documentation.

## 7. Assessment

Adopt unconditionally as the media-capture step — the quality-preservation property alone makes it non-negotiable before verification work. For your profile the operational points are: capture from a dedicated egress rather than the newsroom address when the uploader should not know you are looking, record the yt-dlp version and the full metadata JSON alongside the media so the capture is documented, and update frequently because a stale extractor silently gives you a lower-quality file. Treat the terms-of-service and copyright questions as editorial decisions, taken knowingly.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 2026.10.26, 208,589 stars, 2,790 open issues. Continuous releases on a date-based scheme with same-day commits; the huge issue count is intrinsic to maintaining a thousand platform extractors against constant upstream change.

## 9. Licensing

**Licence:** Unlicense _(SPDX verified)_

**Model / data licence:** n/a. Downloaded content belongs to the original rights holders.

**Restrictions:** None from the licence — the Unlicense is a public-domain dedication. The real constraints are external: platform terms of service and copyright in the downloaded material, both of which are editorial and legal judgements rather than licence issues.

**Licence evidence:** https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE

## 10. Costs

No fee. FFmpeg/FFprobe strongly recommended; yt-dlp-ejs with a JavaScript runtime for some sites. Storage for high-bitrate media is the real cost and grows quickly. Estimate.

## 11. Privacy and data flows

Contacts the target platform directly from the operator's machine, so IP and request pattern are visible to that platform. For sensitive subjects, capture from a dedicated egress. Downloaded metadata may include personal information about uploaders, which attracts your own data-protection obligations.

## 12. Verdict

**Adopt**

## 13. Alternatives

- gallery-dl for image-focused platform capture
- [browsertrix-crawler](OSINT-C1-29.md) or ArchiveWeb.page to capture the surrounding page as evidence of context
- Platform-specific archival tools where yt-dlp lacks an extractor

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/yt-dlp/yt-dlp
- https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 5. [Signal (Android client)](SUR-B3-23.md) · 7. [browsertrix-crawler](OSINT-C1-29.md) →
