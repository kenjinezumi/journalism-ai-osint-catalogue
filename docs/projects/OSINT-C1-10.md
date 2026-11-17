# uncover

`OSINT-C1-10` · **75/100** · overall rank 205 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 65) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 20) |
| **Subcategory** | Exposed-infrastructure discovery |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | ProjectDiscovery |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/projectdiscovery/uncover) · [Documentation](https://github.com/projectdiscovery/uncover#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 2/5 · usability 4/5 · licence+cost 3/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Unified CLI that queries multiple internet-scan databases (Shodan, Censys, FOFA, Hunter, ZoomEye, Netlas and others) with one syntax and returns matching hosts.

## Journalism / investigative use case

Find exposed servers, cameras or admin panels tied to an entity under investigation across several scan databases with one query — the practical route from 'this company sells interception gear' to 'these are its internet-facing systems and certificates'.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- One query syntax across many scan vendors removes a real friction: each vendor's query language differs and comparing results by hand is error-prone
- Multiple sources mitigate single-vendor coverage gaps, which are substantial and uneven by region
- MIT, single Go binary, very actively maintained (pushed 2026-11-17) with only 6 open issues
- Pairs naturally with certificate-transparency and ASN work to build an infrastructure picture of a vendor or state agency

## 5. Cons

- Requires API keys for Shodan, Censys, FOFA, Hunter, ZoomEye and similar — several of which are paid, so the capability has a real recurring cost that the free tool hides
- Your queries and target identifiers are sent to commercial scan vendors, who therefore learn exactly which organisations you are investigating — a serious operational-security consideration when the target is a surveillance company
- Infrastructure focus only: it maps hosts, not people or social activity
- Scan-database results are snapshots that can be months stale, so a host appearing or disappearing is weak evidence without corroboration

## 6. Feedback (documented)

No individual user reports verified. Documented: 3,120 stars with 6 open issues and same-day pushes (2026-11-17), release v1.2.1 (2026-05-20). ProjectDiscovery maintains a well-known suite of such tools with consistent release discipline.

## 7. Assessment

Valuable for surveillance-industry investigation, with the privacy trade-off stated plainly: you are telling a commercial scan vendor which companies you are looking at. For your profile I would use a dedicated account and egress not linked to the newsroom's main identity, prefer Metabigor's keyless sources for the first pass, and reserve uncover for when you need depth. Verify any host attribution against RIR and certificate data before publishing.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.2.1 (2026-05-20), 3,120 stars, 6 open issues. Same-day commits with a very clean tracker under an organisation that maintains a consistent tool suite.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — the scan data belongs to the respective vendors under their terms.

**Restrictions:** Code unrestricted. The binding constraints are each scan vendor's API terms, which typically restrict redistribution of their data — relevant if you want to publish a dataset derived from their results.

**Licence evidence:** https://github.com/projectdiscovery/uncover/blob/main/LICENSE

## 10. Costs

Software free. Real cost is the API keys: Shodan, Censys, FOFA, Hunter and ZoomEye each have free tiers with tight quotas and paid tiers above them — current prices not verified in this survey (check each vendor). Budget for at least one paid subscription if this is a regular workflow.

## 11. Privacy and data flows

Your queries and target identifiers are sent to commercial scan vendors. This is the weakest point: investigating a surveillance vendor while telling a scan provider exactly who you are looking at is a genuine exposure. Use separated accounts and egress.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Queries disclose your investigation targets to commercial scan vendors; several required APIs are paid

## 13. Alternatives

- [Metabigor](OSINT-C1-09.md) for keyless public-source footprinting first
- Direct certificate-transparency queries (certstream, crt.sh) which disclose less
- amass for subdomain enumeration from your own vantage point

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/projectdiscovery/uncover
- https://github.com/projectdiscovery/uncover/blob/main/LICENSE

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

← 204. [RIPE Atlas tooling (Magellan CLI, Cousteau, Sagan)](SUR-B1-12.md) · 206. [Ushahidi Platform](OSINT-C3-07.md) →
