# LibreY

`OSINT-C1-03` · **61/100** · overall rank 317 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 124) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 39) |
| **Subcategory** | Meta-search |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Ahwx and contributors |
| **Maintenance** | Stable with low activity |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Ahwxorg/LibreY) · [Documentation](https://github.com/Ahwxorg/LibreY#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 3/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 61/100**

---

## 1. Purpose

Lightweight self-hosted metasearch front end in PHP that proxies queries to several upstream engines and aggregates results, with optional instance federation.

## Journalism / investigative use case

Lightweight self-hosted meta-search for quick multi-engine checks when a full SearXNG deployment is overkill — for instance a per-investigation throwaway instance on cheap hosting, kept separate from the newsroom's main search path.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Very small footprint: a PHP host is enough, so standing up a disposable instance for one investigation is realistic
- Keeps query logs off commercial search providers in the same way SearXNG does, at a fraction of the operational weight
- AGPL-3.0, so redeployments inherit the same openness obligation

## 5. Cons

- Smaller engine coverage and a slower cadence than SearXNG — last push 2026-06-10, five months before this survey
- Small community (328 stars, 25 open issues), so scraper breakage may persist longer than in SearXNG
- No release objects at all, so there is no version to pin and upgrades mean tracking the default branch
- PHP deployment is a different operational idiom from the rest of a typical Python/TypeScript newsroom stack

## 6. Feedback (documented)

No individual user reports verified. Documented: 328 stars with 25 open issues, no releases, last push 2026-06-10. Positioned by its own documentation as a lighter alternative to SearXNG, which matches the metadata picture.

## 7. Assessment

Hard to justify over SearXNG for a primary instance, given SearXNG's much faster scraper repair and larger engine set. Where LibreY earns consideration is the disposable-instance pattern: cheap, fast to deploy, and discardable after an investigation — which has a genuine operational-security logic if you do not want all of an investigation's queries traceable to one long-lived server. Treat as a secondary option and check its liveness before relying on it.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-06-10, no releases or tags, 328 stars, 25 open issues. Five months quiet. For a metasearch project — where upstream engines change constantly — five months of silence is more concerning than it would be for a stable library, so this classification is cautious rather than generous.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0 network copyleft on modified public instances. Upstream engine terms apply separately.

**Licence evidence:** https://github.com/Ahwxorg/LibreY/blob/main/LICENSE

## 10. Costs

No fee. A minimal PHP host; negligible.

## 11. Privacy and data flows

Queries are proxied to upstream engines from your instance. Self-hosting keeps logs local; a public instance exposes your queries to its operator.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [SearXNG](OSINT-C1-01.md) — the recommended primary choice
- [4get](OSINT-C1-02.md) for a no-JavaScript lightweight option with more recent commits
- Tor Browser plus direct engine queries for unlinkability

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Ahwxorg/LibreY
- https://github.com/Ahwxorg/LibreY/blob/main/LICENSE

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

← 316. [theHarvester](OSINT-C3-28.md) · 318. [Kùzu](JAI-A3-18.md) →
