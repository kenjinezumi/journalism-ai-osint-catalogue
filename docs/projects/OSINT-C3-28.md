# theHarvester

`OSINT-C3-28` · **61/100** · overall rank 316 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 123) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 40) |
| **Subcategory** | Public-source footprinting |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Christian Martorella (laramies) |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-2.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/laramies/theHarvester) · [Documentation](https://github.com/laramies/theHarvester/wiki) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 2/5 · usability 4/5 · licence+cost 4/5 → **weighted 61/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Reconnaissance tool that gathers names, email addresses, subdomains, hosts and open ports for a domain from search engines, certificate transparency, scan databases and other public sources.

## Journalism / investigative use case

Building a picture of an organisation's people and infrastructure from public sources: staff email patterns, subdomains and hosts for a company under investigation — which supports both contact research and infrastructure mapping from a single pass.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Combines people and infrastructure discovery in one tool, which matches how an investigation into an organisation actually proceeds
- Many sources queried in parallel, so coverage is broader than any single source gives
- Long-established with a large community and wide packaging in security distributions
- Email-pattern discovery is practically useful for contact research, where knowing an organisation's address format lets you reach a named individual

## 5. Cons

- Harvesting email addresses creates a personal-data collection with data-protection obligations, which reporters routinely overlook — this is the item that most needs a policy
- Depends on search engines and third-party sources whose access has degraded substantially (the same anti-scraping pressure that killed automated dorking), so results are less complete than they once were
- Several sources require API keys, some paid, so full capability has a hidden cost
- Security-tooling framing, and aggressive use against an organisation raises the usual legal questions

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with a long history. The degradation of search-engine-based collection is corroborated by the independent findings on pagodo, dorks_hunter and Whoogle in this catalogue.

## 7. Assessment

Integrate it with lowered expectations and a data-protection decision made in advance. For your profile two points matter. First, search-engine sources are much weaker than they were, so treat subfinder plus certificate transparency as the reliable infrastructure path and theHarvester as supplementary. Second, the harvested email list is regulated personal data: decide retention and protection before you run it, not after, because an undocumented list of an organisation's staff addresses sitting on a laptop is a liability.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with continuing but modest development. Classified stable-low: the tool is maintained, but its effectiveness is constrained by external source availability rather than by code activity.

## 9. Licensing

**Licence:** GPL-2.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Third-party sources have their own terms.

**Restrictions:** Copyleft on the tool. The weightier obligations are data-protection ones attaching to harvested personal data.

**Licence evidence:** https://github.com/laramies/theHarvester

## 10. Costs

No fee. Several sources require API keys, some paid (not priced here). Negligible compute.

## 11. Privacy and data flows

Queries disclose the target domain to many third parties. More significantly, the output is a collection of other people's personal data, which makes you a data controller with the obligations that follow.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Harvested email addresses are regulated personal data requiring a retention and protection decision

## 13. Alternatives

- [subfinder](OSINT-C3-23.md) plus certificate transparency for infrastructure only, avoiding the personal-data collection
- [Photon](OSINT-C1-20.md) for site-specific contact harvesting
- Manual research for the handful of people who actually matter to the story

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/laramies/theHarvester
- https://github.com/laramies/theHarvester/wiki

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

← 315. [TruFor](JAI-A4-18.md) · 317. [LibreY](OSINT-C1-03.md) →
