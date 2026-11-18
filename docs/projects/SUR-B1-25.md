# diffengine

`SUR-B1-25` · **50/100** · overall rank 345 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 79) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 26) |
| **Subcategory** | Stealth-edit tracking |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Documenting the Now (DocNow; transferred from edsu) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/DocNow/diffengine) · [Documentation](https://github.com/DocNow/diffengine#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 1/5 · privacy 3/5 · usability 1/5 · licence+cost 5/5 → **weighted 50/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None, but the code is effectively frozen. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Not worth operating as-is given dependency age.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/DocNow/diffengine/blob/main/LICENSE
- https://github.com/DocNow/diffengine
- `../sources/evidence/leads.md`

---

## 1. Purpose

Tool that watches RSS/Atom feeds, detects when article text changes after publication, generates a visual diff image, archives the versions to the Internet Archive and posts the diff to social media.

## Journalism / investigative use case

The reference design for publicly surfacing stealth edits to anything with a feed — news sites, ministry press-release feeds, agency blogs — with an Internet Archive snapshot attached to each detected change, making the before state independently verifiable.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- The design pattern is genuinely good: feed-driven detection, visual diff, third-party archive snapshot, public posting — each step reinforces the evidentiary value of the next
- Attaching an Internet Archive snapshot per change means the before state is attested by a third party, not just your local cache
- MIT licensed, and the repository transfer from edsu to DocNow is confirmed by redirect, so the lineage is traceable

## 5. Cons

- Unmaintained since 2020: last push 2020-06-25 and release v0.2.7 (2020-09-30), with 30 open issues — six years untouched
- Social integration is broken by default because it was built for a Twitter API that no longer works as assumed, so the publishing half of the design is dead
- Aged browser-automation dependencies (GeckoDriver/Firefox) and an old Python stack make installation a project in itself
- Only monitors content reachable through a feed, so pages without RSS/Atom are out of scope

## 6. Feedback (documented)

No individual user reports verified. Documented: last push 2020-06-25, release v0.2.7 (2020-09-30), 182 stars, 30 open issues; repository transfer edsu → DocNow confirmed by API redirect on 2026-11-17. Its social-posting dependency on the old Twitter API is the clearest cause of obsolescence.

## 7. Assessment

Reference only, but the design is worth stealing. For your profile, rebuild the pattern with current components: feedparser or a direct feed poller for detection, web-monitoring-diff for the diff, Scoop or the IA save endpoint for the snapshot, and an internal channel rather than a social platform for the notification. That gets you diffengine's evidentiary chain on maintained foundations in a day or two.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2020-06-25, latest release v0.2.7 (2020-09-30), 182 stars, 30 open issues. Six years without activity and a core integration (Twitter API) that no longer exists as assumed. No deprecation notice, hence dormant rather than archived.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, but the code is effectively frozen.

**Licence evidence:** https://github.com/DocNow/diffengine/blob/main/LICENSE

## 10. Costs

No fee. Not worth operating as-is given dependency age.

## 11. Privacy and data flows

Diffs stored locally, but the design is deliberately public: snapshots go to the Internet Archive and diff images were posted to social media. If you rebuild the pattern, decide consciously whether publication is wanted — for monitoring a target during an active investigation it is not.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Unmaintained since 2020; social integration depends on a withdrawn Twitter API

## 13. Alternatives

- [webchanges](SUR-B1-17.md) or changedetection.io for maintained feed and page monitoring
- web-monitoring-diff plus the IA save endpoint to reproduce the evidentiary chain
- [NewsDiffs](SUR-B1-26.md) — also dormant; see its entry

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/DocNow/diffengine
- https://github.com/DocNow/diffengine/blob/main/LICENSE
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |

---

← 344. [Andriller](SUR-B3-17.md) · 346. [DEFAME](JAI-A4-11.md) →
