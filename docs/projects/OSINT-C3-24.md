# httpx

`OSINT-C3-24` · **79/100** · overall rank 162 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 54) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 13) |
| **Subcategory** | Internet infrastructure probing |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | ProjectDiscovery |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/projectdiscovery/httpx) · [Documentation](https://github.com/projectdiscovery/httpx#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 2/5 · usability 4/5 · licence+cost 5/5 → **weighted 79/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Fast multi-purpose HTTP toolkit that probes a list of hosts and reports status codes, titles, technologies, certificates, response hashes and screenshots.

## Journalism / investigative use case

Turning a list of discovered hostnames into a picture of what is actually running: which of a vendor's two hundred subdomains respond, what their page titles say, which share a TLS certificate — the triage step that identifies the handful worth looking at by hand.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Page titles and certificate details at scale are remarkably informative: a title like 'Lawful Interception Management Console' on a staging subdomain is the kind of finding that makes a story
- Response hashing groups identical pages, which quickly separates real applications from parked-domain boilerplate
- MIT licensed, very fast, and composes directly with subfinder and katana in a pipeline
- Optional screenshots give a visual record of what was live at a point in time — useful evidence if the page disappears

## 5. Cons

- Active by nature: it sends requests to every host, so the target sees your probing — this is the step where passive reconnaissance becomes visible, and that should be a deliberate decision
- Aggressive default concurrency can look hostile and may trip protections; rate limits need setting
- Security-tooling framing, so the defaults and documentation assume authorised testing
- Output needs interpretation: a 403 may mean an interesting restricted application or nothing at all

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under ProjectDiscovery's maintenance, consistent with the organisation's observed release discipline.

## 7. Assessment

Adopt it as the triage step after passive enumeration, with concurrency reduced and a deliberate decision that you are willing to be seen probing. For your profile the valuable practice is capturing screenshots and titles as evidence at the moment of probing, because an interesting staging subdomain tends to disappear shortly after someone notices it has been found. Route the traffic through an egress not attributable to your newsroom.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under ProjectDiscovery's maintenance, consistent with same-day commit and regular release patterns observed across their suite in this catalogue.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** Code unrestricted. Probing a third party's infrastructure may engage computer-misuse law depending on jurisdiction and intensity — a legal question to settle before use.

**Licence evidence:** https://github.com/projectdiscovery/httpx/blob/main/LICENSE.md

## 10. Costs

No fee. Negligible compute; bandwidth proportional to the host list.

## 11. Privacy and data flows

Active: the target sees your requests and can identify your IP and pattern. Use a dedicated egress and conservative rate limits.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Active probing is visible to the target and may engage computer-misuse law

## 13. Alternatives

- Manual browsing of the handful of hosts you most care about, which is slower and invisible
- [shot-scraper](SUR-B1-23.md) for screenshot capture with a browser rather than a security tool
- Passive sources only, accepting that you learn less

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/projectdiscovery/httpx
- https://github.com/projectdiscovery/httpx/blob/main/LICENSE.md

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 161. [EDGI web-monitoring-db](SUR-B1-20.md) · 163. [ingest-file (OpenAleph fork)](JAI-A2-25.md) →
