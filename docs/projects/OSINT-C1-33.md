# wabac.js

`OSINT-C1-33` · **74/100** · overall rank 234 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 79) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 24) |
| **Subcategory** | Archive replay component |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/wabac.js) · [Documentation](https://github.com/webrecorder/wabac.js#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 2/5 · licence+cost 3/5 → **weighted 74/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

JavaScript service-worker library that implements web-archive replay in the browser, providing the engine beneath ReplayWeb.page and ArchiveWeb.page.

## Journalism / investigative use case

Embed archive replay directly into a newsroom web application or story page without a replay server — for instance a story template where every cited source opens as its archived capture inline.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Lets you build archive replay into your own product rather than iframing someone else's viewer, which matters for a newsroom with a custom publishing stack
- Client-side by construction, so embedding it does not create a server-side archive-hosting liability
- Actively maintained (v2.27.4, 2026-10-22; pushed 2026-11-13) and the same engine proven in ReplayWeb.page
- Small, focused library with a clear purpose and a tiny issue backlog (16 open)

## 5. Cons

- Library-level component not used directly by journalists, so its value depends entirely on you building something around it
- Requires a modern browser with service-worker support, and service-worker scope rules are a recurring source of integration difficulty
- AGPL-3.0 on a component you embed in a published web application needs genuine legal consideration — this is the case where the licence actually bites
- Tiny community (130 stars), so integration problems are yours to solve

## 6. Feedback (documented)

No individual user reports verified. Documented: 130 stars with 16 open issues, release v2.27.4 (2026-10-22), pushed 2026-11-13. Its production use is evidenced by ReplayWeb.page and ArchiveWeb.page depending on it.

## 7. Assessment

Only relevant if you are building a publishing feature around archived evidence — which is a genuinely good idea for an investigative outlet, since inline verifiable sources are a differentiator. Before committing, get a view on the AGPL question: embedding wabac.js in your public site is the scenario the licence is written for, and whether your site counts as a modified network service is a question for counsel, not for me. If that is a problem, ReplayWeb.page as a separate hosted viewer sidesteps it.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release v2.27.4 (2026-10-22), 130 stars, 16 open issues. Current releases within the Webrecorder suite; small but actively maintained.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** Material here: embedding an AGPL-3.0 library in a public web application is precisely the network-service case the licence addresses. Take legal advice before shipping it in a proprietary publishing stack.

**Licence evidence:** https://github.com/webrecorder/wabac.js/blob/main/LICENSE

## 10. Costs

No fee. No infrastructure (client-side). Cost is engineer integration time plus a legal review of the AGPL position.

## 11. Privacy and data flows

Client-side only — the archive is processed in the reader's browser and not transmitted to your server, which is also a hosting-cost and liability advantage.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- AGPL-3.0 embedding in a public web application — legal review required

## 13. Alternatives

- [ReplayWeb.page](OSINT-C1-32.md) as a standalone viewer, avoiding the embedding question
- [pywb](OSINT-C1-27.md) for server-side replay you control
- A simple link to a downloadable WACZ plus instructions, which costs nothing

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/wabac.js
- https://github.com/webrecorder/wabac.js/blob/main/LICENSE

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

← 233. [Unstructured](JAI-A1-10.md) · 235. [Overpass API](OSINT-C2-23.md) →
