# subfinder

`OSINT-C3-23` · **83/100** · overall rank 125 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 39) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 8) |
| **Subcategory** | Internet infrastructure mapping |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | ProjectDiscovery |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/projectdiscovery/subfinder) · [Documentation](https://github.com/projectdiscovery/subfinder#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 83/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Third-party data sources have their own terms. |
| **Restrictions** | Code unrestricted. Data-source terms apply to API-key-based sources. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Optional API keys for wider coverage, some paid (not priced here). Negligible compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/projectdiscovery/subfinder/blob/main/LICENSE.md
- https://github.com/projectdiscovery/subfinder

---

## 1. Purpose

Fast passive subdomain-enumeration tool that queries many online sources — certificate transparency, DNS datasets, search engines, scan databases — and returns discovered subdomains.

## Journalism / investigative use case

The quick first step in mapping a target's infrastructure: enumerate a surveillance vendor's or front company's subdomains in seconds from passive sources, which frequently surfaces product names, customer portals and regional deployments.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Passive-only by design, so it leaves no trace with the target — the correct default for investigating an organisation that would react to being probed
- Very fast and composable: it does one thing and pipes into httpx or your own tooling, which fits a scripted workflow
- MIT licensed and actively maintained by an organisation with consistent release discipline across its tool suite
- No API keys needed for useful results, though adding them widens coverage

## 5. Cons

- Subdomains only, so it is one dimension of infrastructure mapping — Amass gives you the broader graph
- Coverage depends on third-party sources, so results vary over time and an absent subdomain means nothing
- Queries disclose the domains you are enumerating to the data sources, several of which are commercial
- Security-tooling context means the documentation assumes penetration-testing framing

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under ProjectDiscovery's maintenance, consistent with the release discipline observed across their other tools in this catalogue (katana, uncover).

## 7. Assessment

Adopt it as the fast first pass before Amass — seconds of passive enumeration often answers the question, and only if it does not do you need the heavier tool. For your profile the practical chain is subfinder to enumerate, httpx to see what responds, and manual review of anything unexpected; staging and admin subdomains are where the interesting material is, and they are usually found in the first thirty seconds.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under ProjectDiscovery's maintenance, whose other tools in this catalogue (katana, uncover) show same-day commits and regular releases — a consistent organisational pattern.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Third-party data sources have their own terms.

**Restrictions:** Code unrestricted. Data-source terms apply to API-key-based sources.

**Licence evidence:** https://github.com/projectdiscovery/subfinder/blob/main/LICENSE.md

## 10. Costs

No fee. Optional API keys for wider coverage, some paid (not priced here). Negligible compute.

## 11. Privacy and data flows

Passive with respect to the target. The data sources learn which domains you enumerate.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Amass for broader infrastructure graphing
- crt.sh queries for certificate-transparency-only discovery
- [Metabigor](OSINT-C1-09.md) for ASN and netblock mapping rather than subdomains

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/projectdiscovery/subfinder
- https://github.com/projectdiscovery/subfinder/blob/main/LICENSE.md

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
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 124. [MarkItDown](JAI-A1-09.md) · 126. [InVID-WeVerify Verification Plugin](JAI-A4-04.md) →
