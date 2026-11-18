# 4get

`OSINT-C1-02` · **68/100** · overall rank 278 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 103) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 32) |
| **Subcategory** | Meta-search |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | lolcat (self-hosted forge git.lolcat.ca) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0-only |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://git.lolcat.ca/lolcat/4get) · [Documentation](https://git.lolcat.ca/lolcat/4get) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 68/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0-only |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0-only network copyleft: modifying and exposing an instance obliges source publication. Upstream engines' terms on automated querying apply separately. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Minimal PHP host. Negligible infrastructure.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://git.lolcat.ca/lolcat/4get
- https://git.lolcat.ca/lolcat/4get/commits/branch/master

---

## 1. Purpose

Lightweight PHP metasearch proxy that queries multiple upstream engines without requiring JavaScript or accounts, returning plain aggregated results.

## Journalism / investigative use case

Query several engines without logging in or running JavaScript, and compare how different engines rank the same target — useful on a hardened or low-bandwidth machine where a full SearXNG deployment or a JavaScript-heavy interface is impractical.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- No JavaScript required, which makes it usable from a locked-down browser, a text browser or a minimal field device — a genuine niche that SearXNG does not fill as well
- Very small PHP deployment, so it runs on almost anything including shared hosting
- Verified actively developed: the project's own forge shows commits dated 2026-11-15, so despite being off GitHub it is current
- AGPL-3.0-only, so the privacy-preserving intent is legally reinforced for anyone redeploying it

## 5. Cons

- Not on GitHub but on a self-hosted forge, which means no GitHub API metadata, no dependency-scanner integration, and a smaller contributor pool — assessment depends on reading that forge directly
- Scraper breakage is routine and the smaller contributor base means slower repair than SearXNG
- Engine coverage and result quality are below SearXNG's
- Using someone else's public 4get instance means the operator sees your queries — the same caveat as any shared metasearch, and more acute with a small single-maintainer project

## 6. Feedback (documented)

No individual user reports verified. Verified directly from the project's forge on 2026-11-17: the master branch commit list shows commits dated 2026-11-15, confirming current development. No star or issue metrics are available because the project is not on GitHub, so community-size signals cannot be reported.

## 7. Assessment

A useful second option rather than a primary tool: I would deploy SearXNG as the newsroom instance and keep 4get in mind for the specific case of a no-JavaScript or very constrained client. For media-in-exile contexts that constraint is not hypothetical — a reporter on a hardened machine or a censored connection may genuinely need a text-only search path. Verify its liveness on the forge rather than assuming, since no GitHub signals exist.

## 8. Maintenance

**Actively maintained** — Project forge (git.lolcat.ca/lolcat/4get) read directly on 2026-11-17: master-branch commits dated 2026-11-15. HTTP 200 and a populated commit list. No GitHub metadata exists for this project, so star counts, issue counts and release objects are unavailable — classification rests on commit recency from the authoritative source.

## 9. Licensing

**Licence:** AGPL-3.0-only _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0-only network copyleft: modifying and exposing an instance obliges source publication. Upstream engines' terms on automated querying apply separately.

**Licence evidence:** https://git.lolcat.ca/lolcat/4get

## 10. Costs

No fee. Minimal PHP host. Negligible infrastructure.

## 11. Privacy and data flows

Your own instance proxies queries to upstream engines, so those engines see your server's IP. Using a public instance means the operator sees your queries — avoid public instances for investigative searches.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [SearXNG](OSINT-C1-01.md) as the primary self-hosted metasearch
- [LibreY](OSINT-C1-03.md) as another lightweight PHP option
- Direct engine queries through Tor Browser when the priority is unlinkability rather than aggregation

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

- https://git.lolcat.ca/lolcat/4get
- https://git.lolcat.ca/lolcat/4get/commits/branch/master

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

← 277. [smolagents](JAI-A3-11.md) · 279. [entity-fishing](JAI-A2-14.md) →
