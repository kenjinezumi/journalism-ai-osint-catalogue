# wayback (Python client for the Internet Archive Wayback Machine)

`SUR-B1-22` · **79/100** · overall rank 165 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 46) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 11) |
| **Subcategory** | Archive access |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Environmental Data and Governance Initiative (EDGI) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/edgi-govdata-archiving/wayback) · [Documentation](https://wayback.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 79/100**

---

## 1. Purpose

Python client for the Internet Archive's Wayback Machine CDX and Memento endpoints, enumerating captures of a URL and retrieving the exact archived bytes for a given timestamp.

## Journalism / investigative use case

Enumerate every archived capture of a government URL and pull the exact bytes of two dates to prove what a page said before and after an edit — without screen-scraping the Wayback web interface, which breaks and is unreliable at scale.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Gives you the exact archived bytes rather than a rendered screenshot, which is what you need for a defensible before-and-after comparison
- Proper CDX enumeration means you can find the captures that exist rather than guessing dates — the step most manual Wayback research gets wrong
- BSD-3-Clause, well documented, actively released (v0.5.1, 2026-06-19) by the team that uses it in production monitoring
- Turns a third-party archive into a programmable evidence source, which is extremely cost-effective compared with running your own crawls retrospectively

## 5. Cons

- Only as good as the Internet Archive's crawl coverage: pages never captured, captured rarely, or excluded by robots or takedown cannot be reconstructed — and coverage of non-Western government sites is notably thin
- No diffing, scheduling or alerting of its own; it is an access library
- Your query pattern is visible to the Internet Archive, so enumerating captures of a specific target discloses your interest to a third party
- Small community (94 stars, 25 open issues), and IA endpoint behaviour and rate limits can change outside your control

## 6. Feedback (documented)

No individual user reports verified. Documented: release v0.5.1 (2026-06-19), last push 2026-11-06, 94 stars with 25 open issues; in production use within EDGI's monitoring stack. Internet Archive coverage limitations are a well-documented general property of web archiving rather than a defect of this client.

## 7. Assessment

Adopt it — the cost-benefit is excellent, because it lets you reconstruct history you never captured yourself. Two disciplines for your work: treat absence of captures as absence of evidence rather than evidence of no change, and start your own forward capture (Scoop, ArchiveBox) for any target that matters, because relying solely on IA means your evidence depends on someone else's crawler and someone else's takedown policy.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-06, latest release v0.5.1 (2026-06-19), 94 stars, 25 open issues. Regular releases under institutional maintenance with production use behind EDGI's monitoring.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** Archived content belongs to the original publishers; Internet Archive access terms apply to retrieval.

**Restrictions:** None material for the client. Republishing archived content raises the original publisher's rights, which is a separate editorial/legal judgement.

**Licence evidence:** https://github.com/edgi-govdata-archiving/wayback/blob/main/LICENSE

## 10. Costs

No fee. Negligible compute. The Internet Archive is a free service; heavy querying should be rate-limited out of courtesy rather than cost.

## 11. Privacy and data flows

Sends the URLs you query to the Internet Archive and pulls archived content back, so your query pattern — which targets you are researching — is visible to IA. Consider this when researching a sensitive target.

## 12. Verdict

**Adopt**

## 13. Alternatives

- waybackpack or waybackpy as alternative Python clients
- [Scoop](OSINT-C1-36.md) or ArchiveBox for forward capture under your own control
- [pywb](OSINT-C1-27.md) to serve your own captures alongside IA material

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/edgi-govdata-archiving/wayback
- https://wayback.readthedocs.io/
- https://github.com/edgi-govdata-archiving/wayback/blob/main/LICENSE

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

← 164. [Stanza](JAI-A2-49.md) · 166. [Argos Translate](JAI-A2-03.md) →
