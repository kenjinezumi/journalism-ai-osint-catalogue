# ReplayWeb.page

`OSINT-C1-32` · **94/100** · overall rank 16 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 9) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 5) |
| **Subcategory** | Archive replay |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/replayweb.page) · [Documentation](https://replayweb.page/docs/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 94/100**

---

## 1. Purpose

Browser-based, fully client-side viewer that opens WARC and WACZ archives and replays them without any server, using service workers.

## Journalism / investigative use case

Let editors, lawyers and readers open and inspect an archived page themselves, offline, from a single file — which is what converts a capture into usable evidence in an editorial or legal conversation, with no infrastructure between them and the material.

## 2. Audience

journalist, newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Zero infrastructure and zero upload: hand someone a WACZ file and they can inspect it in a browser, which removes the single biggest practical barrier to using archived evidence
- Client-side replay means the archive is never transmitted anywhere, so you can share a capture with a lawyer without it touching a server
- Actively maintained (v2.5.4, 2026-10-22; pushed 2026-11-17) and part of the same suite that produces the captures
- Can be embedded in a story page, so readers can examine the archived source themselves

## 5. Cons

- Fidelity is bounded by the original capture — ReplayWeb.page cannot show what was never recorded, and users often misattribute capture gaps to the viewer
- Very large archives load slowly in a browser, so a multi-gigabyte collection is not a good fit for this path
- AGPL-3.0 affects embedding a modified version in a distributed product
- 119 open issues, mostly replay edge cases on complex sites — the general hard problem of web-archive replay

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,015 stars with 119 open issues, release v2.5.4 (2026-10-22), pushed 2026-11-17. Widely used as the reference WACZ viewer across the web-archiving community.

## 7. Assessment

Adopt — it is the piece that makes your captures socially useful. For your profile the highest-value application is legal and editorial review: a WACZ plus ReplayWeb.page lets counsel examine exactly what a page said without you building anything or exposing the archive. Embedding it in published stories is also worth considering where a source page is likely to change, since it lets readers verify your sourcing directly.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2.5.4 (2026-10-22), 1,015 stars, 119 open issues. Same-day commits and current releases within the Webrecorder suite.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: embedding a modified version in a distributed product triggers source obligations. Using the hosted viewer or an unmodified self-hosted copy is unaffected.

**Licence evidence:** https://github.com/webrecorder/replayweb.page/blob/main/LICENSE

## 10. Costs

Free. No infrastructure; optionally self-host the static viewer alongside your archives.

## 11. Privacy and data flows

Replay happens entirely client-side and archives are not uploaded — among the strongest privacy properties in this catalogue, and the reason it is safe to use for sensitive captures. If you use the hosted viewer, the page itself is loaded from Webrecorder but your archive file is not sent to them.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [pywb](OSINT-C1-27.md) for server-side replay over a large collection
- [wabac.js](OSINT-C1-33.md) to embed replay directly into your own application
- [OutbackCDX](OSINT-C1-44.md) plus pywb for indexed access at scale

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/replayweb.page
- https://replayweb.page/docs/
- https://github.com/webrecorder/replayweb.page/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 15. [PySceneDetect](OSINT-C2-10.md) · 17. [Uwazi](OSINT-C3-05.md) →
