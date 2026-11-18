# OutbackCDX

`OSINT-C1-44` · **75/100** · overall rank 216 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 72) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 21) |
| **Subcategory** | Archive indexing |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | International Internet Preservation Consortium (IIPC) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/iipc/outbackcdx) · [Documentation](https://github.com/iipc/outbackcdx#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 75/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: a JVM service plus RocksDB storage for the index (a fraction of the WARC collection size) — modest relative to the WARC storage it serves. Assumptions: self-hosted alongside an existing archive.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/iipc/outbackcdx/blob/master/LICENSE
- https://github.com/iipc/outbackcdx

---

## 1. Purpose

RocksDB-backed CDX index server that provides fast URL and timestamp lookup over large WARC collections, compatible with pywb and OpenWayback front ends.

## Journalism / investigative use case

Index a large in-house WARC collection so investigators can query by URL and timestamp like the public Wayback Machine — the component that makes a multi-terabyte capture collection usable rather than theoretically searchable.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Solves the scaling problem that makes large private archives unusable: without a proper CDX index, URL lookup over terabytes of WARC is impractically slow
- Compatible with pywb and OpenWayback, so it slots into the standard replay stack without custom work
- Apache-2.0 under IIPC stewardship — the web-archiving standards body — which is a strong continuity signal for long-lived infrastructure
- Actively maintained (1.3.0, 2026-09-30; pushed 2026-11-13) with a small clean backlog

## 5. Cons

- Infrastructure component only: it requires a pywb or OpenWayback front end and real operations capacity, so it is the third piece of a three-piece stack
- Java plus RocksDB storage is another operational idiom to maintain alongside your other systems
- Tiny community (46 stars, 19 open issues), so operational knowledge comes from IIPC community documentation rather than Stack Overflow
- Only worth deploying above a scale most newsrooms never reach — below a few hundred GB, pywb alone is fine

## 6. Feedback (documented)

No individual user reports verified. Documented: 46 stars with 19 open issues, release 1.3.0 (2026-09-30), last push 2026-11-13, Apache-2.0. Used by national and institutional web archives within the IIPC community, which is the relevant production context.

## 7. Assessment

Only relevant if your capture programme grows to the point where pywb's own indexing becomes the bottleneck — which happens around the multi-terabyte mark, not before. For your profile I would note it as the known upgrade path rather than deploy it now: build with pywb, and if the collection grows large enough that lookups become slow, OutbackCDX is the standard answer and it slots in without changing the rest of the stack.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release 1.3.0 (2026-09-30), 46 stars, 19 open issues. Current releases under IIPC stewardship with institutional production use; small community reflects the narrow operator audience rather than low maintenance.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/iipc/outbackcdx/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a JVM service plus RocksDB storage for the index (a fraction of the WARC collection size) — modest relative to the WARC storage it serves. Assumptions: self-hosted alongside an existing archive.

## 11. Privacy and data flows

Index queries stay within your infrastructure — no external calls. As with pywb, the index must not be publicly exposed, since it reveals every URL you have captured.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [pywb](OSINT-C1-27.md)'s built-in indexing for collections below the terabyte scale
- CDXJ files generated by warcio for simple lookup needs
- OpenWayback for an alternative front end

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/iipc/outbackcdx
- https://github.com/iipc/outbackcdx/blob/master/LICENSE

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

← 215. [Open-Meteo](OSINT-C2-41.md) · 217. [titiler](JAI-A1-27.md) →
