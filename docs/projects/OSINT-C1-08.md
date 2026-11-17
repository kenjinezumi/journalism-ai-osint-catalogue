# dorks_hunter

`OSINT-C1-08` · **43/100** · overall rank 351 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 135) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 43) |
| **Subcategory** | Search dorking |
| **Type** | cli |
| **Bucket** | `uncertain` |
| **Maintainer** | six2dez |
| **Maintenance** | Stable with low activity |
| **Licence** | NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/six2dez/dorks_hunter) · [Documentation](https://github.com/six2dez/dorks_hunter#readme) |

**Scores** — relevance 2/5 · capability 2/5 · maintenance 3/5 · privacy 2/5 · usability 3/5 · licence+cost 1/5 → **weighted 43/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Script that runs a curated set of Google dork queries against a target domain to find exposed documents, configuration files, login panels and third-party exposures.

## Journalism / investigative use case

One of the few dorking helpers still receiving commits after pagodo's archival, for quick exposed-file discovery on a domain — for example surfacing a council's inadvertently public document directory.

## 2. Audience

engineer

## 3. Project type

cli · bucket `uncertain`

## 4. Pros

- Still receiving commits (pushed 2026-07-14) after the archival of pagodo, so it is the most current option in a collapsing niche
- Curated dork set is narrower and more practical than the full GHDB, which makes manual review of results feasible
- Simple enough to read in full and adapt, which is how it should be used given the reliability problem

## 5. Cons

- UNLICENSED: the GitHub API reports no detected licence and session-1 inspection found none, so reuse and redistribution are legally unresolved
- Reliability is bounded by Google's 2026 anti-scraping changes, the same constraint that killed pagodo — expect intermittent and silent failure
- Release metadata is effectively absent (v1.0 from 2022-08-03 against current commits), so there is no meaningful version to pin
- Dork queries are issued to Google from your IP, producing an attributable pattern

## 6. Feedback (documented)

No individual user reports verified. Documented: no licence detected by the GitHub API (verified session 1, retained); 350 stars with 0 open issues; last push 2026-07-14; release v1.0 dated 2022-08-03. The zero-issue count on a scraping tool in 2026 more likely reflects an unattended tracker than a flawless tool.

## 7. Assessment

Not something I would depend on: unlicensed and built on a capability Google has largely closed. Read the dork list, use the patterns manually, and if exposed-document discovery matters to a beat, build it on a direct crawl (katana, Photon) which is both lawful under the target's robots posture and reliable. The licence gap alone should keep it out of any newsroom codebase.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-07-14, latest release v1.0 (2022-08-03), no detected licence, 350 stars, 0 open issues. Four months since last push on a script-sized project; activity continues but the upstream capability is degraded, which matters more than cadence here.

## 9. Licensing

**Licence:** NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unresolved: without a licence, you have no granted rights to copy, modify or redistribute. Do not vendor it into a newsroom codebase. Automated Google querying also breaches Google's terms.

**Licence evidence:** https://github.com/six2dez/dorks_hunter

## 10. Costs

No fee. Low value per unit of effort given reliability problems.

## 11. Privacy and data flows

Dork queries are issued to Google from your IP, producing a visible and attributable pattern tied to your investigation.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- No licence — reuse legally unresolved
- Automated Google dorking degraded by anti-scraping measures

## 13. Alternatives

- Manual dorking through SearXNG
- [katana](OSINT-C1-15.md) or Photon for direct enumeration of a target domain
- [uncover](OSINT-C1-10.md) for exposed-service discovery via scan-database APIs

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/six2dez/dorks_hunter

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

← 350. [Noiseprint](JAI-A4-22.md) · 352. [Fetch (Meedan ClaimReview aggregator)](JAI-A4-03.md) →
