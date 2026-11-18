# browsertrix-behaviors

`OSINT-C1-34` · **78/100** · overall rank 181 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 59) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 18) |
| **Subcategory** | Capture behaviours |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/browsertrix-behaviors) · [Documentation](https://github.com/webrecorder/browsertrix-behaviors#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0; minimal practical effect when used inside your own capture pipeline rather than redistributed. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. No separate infrastructure — it runs inside the capture browser. Cost is engineer time if you write custom behaviours.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/webrecorder/browsertrix-behaviors/blob/main/LICENSE
- https://github.com/webrecorder/browsertrix-behaviors

---

## 1. Purpose

Library of site-specific and generic in-page behaviours (autoscroll, autoplay, expand-comments, platform-specific handlers) that run inside the capture browser to make dynamic content load before it is recorded.

## Journalism / investigative use case

Make automated captures of infinite-scroll social feeds and video pages actually complete, rather than capturing the first screen — the difference between archiving a post and archiving a post with its 400 comments.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Directly addresses the main failure mode of automated social-media capture: content that only loads on interaction, which is most of what matters on a social post
- Modular per-site behaviours mean a newsroom can write its own for a platform or portal that matters to its beat
- Actively maintained in lockstep with the crawler (v0.16.0 released 2026-11-10, same-day push) with a tiny backlog (7 open issues)
- AGPL-3.0 but used as a component inside your own capture pipeline, where the obligation is minimal

## 5. Cons

- Only as good as the per-site behaviour coverage: a platform without a behaviour, or one that has changed its markup, captures incompletely and often silently
- Requires a browser capture host (Browsertrix or ArchiveWeb.page) — it does nothing standalone
- Writing a new behaviour means reverse-engineering a platform's DOM, which is real work and breaks when the platform changes
- Very small community (60 stars), so you are unlikely to find a third-party behaviour for a niche target

## 6. Feedback (documented)

No individual user reports verified. Documented: 60 stars with 7 open issues, release v0.16.0 on 2026-11-10 with same-day push. Production use is evidenced by browsertrix-crawler's dependency on it.

## 7. Assessment

You will use this implicitly through browsertrix-crawler rather than directly, and the reason to know it exists is operational: when a social capture comes out incomplete, the behaviour coverage is the thing to check and potentially extend. For your profile the actionable point is that writing a custom behaviour for a platform central to your reporting is a tractable piece of work with outsized evidentiary payoff — and worth doing before you need the capture, not after.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-10, latest release v0.16.0 published the same day, 60 stars, 7 open issues. Released in lockstep with the crawler it serves; small, focused and current.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0; minimal practical effect when used inside your own capture pipeline rather than redistributed.

**Licence evidence:** https://github.com/webrecorder/browsertrix-behaviors/blob/main/LICENSE

## 10. Costs

No fee. No separate infrastructure — it runs inside the capture browser. Cost is engineer time if you write custom behaviours.

## 11. Privacy and data flows

Runs inside the capture browser; no separate data flows of its own.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Manual capture with ArchiveWeb.page where a behaviour does not exist
- Writing a custom behaviour for a platform central to your beat
- Accepting partial captures and documenting the limitation in your methodology note

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/browsertrix-behaviors
- https://github.com/webrecorder/browsertrix-behaviors/blob/main/LICENSE

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

← 180. [RSS-Bridge](JAI-A1-06.md) · 182. [kepler.gl](JAI-A1-25.md) →
