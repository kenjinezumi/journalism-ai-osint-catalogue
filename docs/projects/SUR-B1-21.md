# EDGI web-monitoring-diff

`SUR-B1-21` · **81/100** · overall rank 138 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 38) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 8) |
| **Subcategory** | HTML diffing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Environmental Data and Governance Initiative (EDGI) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/edgi-govdata-archiving/web-monitoring-diff) · [Documentation](https://edgi-govdata-archiving.github.io/web-monitoring-diff/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 81/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0: embedding in a distributed product triggers source-release obligations. Internal use unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Processes content in memory or over a local HTTP endpoint; negligible infrastructure. Cost is engineer time on per-site noise filtering.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/edgi-govdata-archiving/web-monitoring-diff/blob/main/LICENSE
- https://github.com/edgi-govdata-archiving/web-monitoring-diff
- https://edgi-govdata-archiving.github.io/web-monitoring-diff/

---

## 1. Purpose

Python library and optional HTTP service providing multiple diff algorithms for web content — HTML source, rendered text, links, and side-by-side visual comparison — tuned for comparing archived captures.

## Journalism / investigative use case

Produces the side-by-side and inline HTML diffs that let a reporter see exactly which sentences, links or data tables were removed from an official page between two archived captures — the artefact that turns 'the page changed' into a publishable finding.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Multiple diff types (source, text, links) let you ask different questions: a removed link to a dataset is a different story from reworded guidance, and link diffing surfaces quiet removals that text diffing misses
- Purpose-built for archived government pages rather than generic text, so it handles the templating realities of agency sites better than off-the-shelf diff
- Usable as a library or an HTTP endpoint, so it integrates into either a pipeline or a platform
- Actively released (v0.3.0, 2026-11-13, same-day push) and deliberately decoupled from the storage platform

## 5. Cons

- A component rather than a product: no scheduling, storage, alerting or UI, so it only earns its place inside a larger system you build or run
- HTML diffing of heavily templated government pages still needs filtering to suppress navigation, timestamp and session noise — the library helps but does not solve this, and tuning is per-site work
- GPL-3.0 copyleft affects redistribution inside a product
- 47 open issues against 26 stars — a high ratio indicating known rough edges in a small project

## 6. Feedback (documented)

No individual user reports verified. Documented: release v0.3.0 on 2026-11-13 with same-day push; 26 stars with 47 open issues. In production use behind EDGI's own monitoring programme, which is verifiable from the sibling repository's configuration.

## 7. Assessment

Worth adopting as the diffing layer whenever you build monitoring yourself, because the link-diff capability in particular catches removals that text diffs hide — and quiet removal of a dataset link is a recurring story. Budget per-site filtering work; that is the real cost and it is unavoidable with any HTML diffing approach. Pair with web-monitoring-db for storage and triage, or with your own capture pipeline.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release v0.3.0 published the same day, 26 stars, 47 open issues. Current releases under institutional maintenance; the backlog reflects the difficulty of HTML diffing rather than neglect.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0: embedding in a distributed product triggers source-release obligations. Internal use unaffected.

**Licence evidence:** https://github.com/edgi-govdata-archiving/web-monitoring-diff/blob/main/LICENSE

## 10. Costs

No fee. Processes content in memory or over a local HTTP endpoint; negligible infrastructure. Cost is engineer time on per-site noise filtering.

## 11. Privacy and data flows

Processes content in memory or over a local HTTP endpoint with no outbound data flows of its own — one of the cleanest privacy profiles in this segment.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Standard diff tooling plus html2text for simpler needs
- [changedetection.io](SUR-B1-15.md)'s built-in diffing if you use that platform
- git-based diffing via shot-scraper for a lighter approach

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/edgi-govdata-archiving/web-monitoring-diff
- https://edgi-govdata-archiving.github.io/web-monitoring-diff/
- https://github.com/edgi-govdata-archiving/web-monitoring-diff/blob/main/LICENSE

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
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 137. [dump1090 (FlightAware fork)](OSINT-C2-47.md) · 139. [GLiNER](JAI-A2-19.md) →
