# pywb

`OSINT-C1-27` · **81/100** · overall rank 145 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 46) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 16) |
| **Subcategory** | Archive replay |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/pywb) · [Documentation](https://pywb.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 81/100**

---

## 1. Purpose

Python web-archiving toolkit providing high-fidelity replay of WARC and WACZ collections, a recording proxy mode, collection management and a Wayback-style interface.

## Journalism / investigative use case

Stand up a private Wayback Machine over your own captures so editors and lawyers can click through dated versions of a government page side by side without relying on a public archive staying online — the piece that turns a WARC collection from a pile of files into usable evidence.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Turns inert WARC files into something a non-technical colleague can actually use, which is the difference between having evidence and being able to show it
- High replay fidelity by the standards of the field, maintained by the team that drives much of modern web-archiving practice
- Very actively maintained (v2.11.1 released 2026-11-14, pushed 2026-11-17) with a substantial community (1,720 stars)
- Also works as a recording proxy, so it can capture as well as replay — useful for a single integrated setup

## 5. Cons

- Replay and recording only: no change detection, diffing or alerting, so it is one component of a monitoring or evidence system rather than a solution
- Replay fidelity for heavily scripted modern pages remains an open problem in web archiving generally — pywb does as well as anything, which is not the same as perfectly
- GPL-3.0 copyleft is a consideration if you embed replay in a product you distribute
- 185 open issues and a configuration surface that takes learning; what it exposes to the network depends entirely on how you deploy it

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,720 stars with 185 open issues, release v-2.11.1 (2026-11-14), pushed 2026-11-17. pywb is used across the web-archiving community including by institutional archives, verifiable from IIPC community documentation.

## 7. Assessment

Adopt it as the replay layer for any serious capture programme — without replay, WARCs are write-only. For your profile the deployment decision that matters is access control: a pywb instance over an investigation's captures is a high-value target and must not be publicly reachable. Pair with OutbackCDX if the collection grows large enough that URL/timestamp lookup becomes slow.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v-2.11.1 (2026-11-14), 1,720 stars, 185 open issues. Current releases and same-day commits from an organisation whose core business this is.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Replayed content belongs to the original publishers.

**Restrictions:** GPL-3.0: distributing a modified pywb-based product triggers source-release obligations. Internal deployment is unaffected.

**Licence evidence:** https://github.com/webrecorder/pywb/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a small Python service plus storage for your WARC/WACZ collection — storage dominates and scales with capture volume. Operating effort is modest once configured.

## 11. Privacy and data flows

Serves local archive files; what it exposes to the network depends entirely on your deployment. A misconfigured public instance would publish your entire capture collection, including anything sensitive you captured — bind it internally and authenticate.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ReplayWeb.page](OSINT-C1-32.md) for single-file client-side replay with no server at all
- [Browsertrix](OSINT-C1-30.md) (the platform) if you want capture, storage and replay managed together
- [OutbackCDX](OSINT-C1-44.md) plus pywb for large collections needing fast URL indexing

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/pywb
- https://pywb.readthedocs.io/
- https://github.com/webrecorder/pywb/blob/main/LICENSE

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

← 144. [pyannote.audio](JAI-A2-41.md) · 146. [Timesketch](OSINT-C3-37.md) →
