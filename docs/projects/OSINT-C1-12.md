# name-variant-search

`OSINT-C1-12` · **80/100** · overall rank 156 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 52) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 17) |
| **Subcategory** | Name variant generation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/name-variant-search) · [Documentation](https://bellingcat.github.io/name-variant-search/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 5/5 · licence+cost 5/5 → **weighted 80/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. No infrastructure; self-hosting is a static file.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/bellingcat/name-variant-search/blob/main/LICENSE
- https://github.com/bellingcat/name-variant-search
- https://bellingcat.github.io/name-variant-search/

---

## 1. Purpose

Browser-based tool that generates transliteration and spelling variants of a personal name across scripts and conventions, producing a list of alternative spellings to search for.

## Journalism / investigative use case

Expand searches for a person whose name is transliterated inconsistently across Russian, Ukrainian, Arabic or other scripts — the difference between finding three records and finding thirty, and a routine failure point in cross-border investigation.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Addresses a specific, high-frequency failure in cross-border research that reporters usually handle badly by guessing a couple of spellings
- Runs client-side in a hosted static page, so the name you enter is not transmitted — a genuinely important property when the name is a sensitive subject
- Built by Bellingcat for practising investigators, so the variant conventions reflect real research needs rather than linguistic completeness
- MIT licensed and trivial to self-host as a static page if you prefer not to rely on the hosted version

## 5. Cons

- Heuristic variant generation only: it produces candidate spellings, not a verified list, and will both miss real variants and generate spellings nobody uses
- No search execution or results — you take the list elsewhere, so it is one step in a manual workflow
- Small project (56 stars, 2 open issues) with no releases and last push 2026-06-25
- Variant quality depends on the source script and convention; coverage for less common scripts was not evaluated in this survey

## 6. Feedback (documented)

No individual user reports verified. Documented: 56 stars, 2 open issues, no releases, last push 2026-06-25, MIT licence. Bellingcat's tool suite is widely used in the investigative community, which is relevant context rather than specific evidence for this tool.

## 7. Assessment

A small, sharp utility worth having bookmarked and worth self-hosting as a static page so you are not dependent on the hosted copy. For your profile the correct use is to feed its output into a systematic search across SearXNG, Marginalia and your own document archive, keeping a record of which spellings were searched — because 'we searched for the name' is a weak methodological claim and 'we searched these fourteen transliterations' is a strong one.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-06-25, no releases or tags, 56 stars, 2 open issues. Five months quiet on a small static tool that is functionally complete; low risk from dormancy since there is no dependency surface to rot.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/bellingcat/name-variant-search/blob/main/LICENSE

## 10. Costs

No fee. No infrastructure; self-hosting is a static file.

## 11. Privacy and data flows

Name input is processed client-side in the hosted static page, so the name is not transmitted to a server. Self-hosting removes even the page-load disclosure to the hosting provider.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [uroman](JAI-A2-56.md) for systematic romanisation in a pipeline rather than interactively
- [rigour](JAI-A2-44.md) for corporate rather than personal name normalisation
- Manual transliteration tables for a specific language pair where precision matters

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/name-variant-search
- https://bellingcat.github.io/name-variant-search/
- https://github.com/bellingcat/name-variant-search/blob/main/LICENSE

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

← 155. [urlwatch](SUR-B1-16.md) · 157. [Tor Browser Launcher](SUR-B3-29.md) →
