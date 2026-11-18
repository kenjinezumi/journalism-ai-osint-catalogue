# wpull

`OSINT-C1-25` · **54/100** · overall rank 338 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 132) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 42) |
| **Subcategory** | Archival web crawling |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | ArchiveTeam |
| **Maintenance** | Dormant |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ArchiveTeam/wpull) · [Documentation](https://github.com/ArchiveTeam/wpull#readme) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 54/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0; immaterial given the recommendation not to use it. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Install effort on current Python is the real cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ArchiveTeam/wpull/blob/master/LICENSE.txt
- https://github.com/ArchiveTeam/wpull

---

## 1. Purpose

Python reimplementation of wget with WARC output, wget-compatible flags, a plugin/hook system and database-backed crawl state.

## Journalism / investigative use case

Wget-style recursive capture when you need WARC output and wget's familiar flag semantics — historically the engine beneath grab-site and a bridge for anyone who already thinks in wget options.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- wget-compatible flags lower the learning curve substantially for anyone who already uses wget, while adding proper WARC output
- Database-backed crawl state makes large crawls resumable, which plain wget does not do well
- Plugin hooks allow custom scope logic, which is how grab-site implemented live steering
- GPL-3.0 with a sizeable historical community (613 stars)

## 5. Cons

- Effectively dormant: last push 2024-04-29, no release objects (latest tag v2.0.3), and 208 open issues — the largest backlog-to-stars ratio in this subcategory
- Its dormancy propagates: grab-site depends on it, so two tools stall together
- Python dependency chain of this vintage is increasingly difficult to install on current interpreters
- Modern wget itself supports --warc, removing much of wpull's original rationale

## 6. Feedback (documented)

No individual user reports verified. Documented: last push 2024-04-29, 613 stars, 208 open issues, no releases, latest tag v2.0.3. The large unattended backlog alongside no commits for over two years is unambiguous.

## 7. Assessment

Avoid for new work. `wget --warc` covers the simple case with a maintained binary, and browsertrix-crawler covers the fidelity case. The only reason to touch wpull now is to understand or repair grab-site. For your profile, note the general pattern worth applying across this catalogue: when a tool's sole differentiator has been absorbed into a maintained upstream (here, wget's WARC support), the tool's dormancy is terminal rather than temporary.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-04-29, no release objects, latest tag v2.0.3, 613 stars, 208 open issues. Over two and a half years without commits and a very large open backlog. No deprecation notice, hence dormant rather than archived.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0; immaterial given the recommendation not to use it.

**Licence evidence:** https://github.com/ArchiveTeam/wpull/blob/master/LICENSE.txt

## 10. Costs

No fee. Install effort on current Python is the real cost.

## 11. Privacy and data flows

WARC written locally; nothing uploaded.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Dormant since April 2024 with a 208-issue backlog; superseded by wget's own WARC support

## 13. Alternatives

- wget --warc — maintained, simple, covers the core case
- [browsertrix-crawler](OSINT-C1-29.md) for dynamic content with WACZ output
- Heritrix for domain-scale archival crawls

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ArchiveTeam/wpull
- https://github.com/ArchiveTeam/wpull/blob/master/LICENSE.txt

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

← 337. [CenAlert](SUR-B1-10.md) · 339. [blockhash-python](OSINT-C2-09.md) →
