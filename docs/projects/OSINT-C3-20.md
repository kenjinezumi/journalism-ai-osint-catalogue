# ethereum-etl

`OSINT-C3-20` · **69/100** · overall rank 274 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 101) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 32) |
| **Subcategory** | Blockchain analysis |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | blockchain-etl |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/blockchain-etl/ethereum-etl) · [Documentation](https://ethereum-etl.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 69/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Tool that exports Ethereum blockchain data — blocks, transactions, token transfers, logs, contracts — into CSV, JSON or a data warehouse for SQL analysis.

## Journalism / investigative use case

Following cryptocurrency flows with your own data rather than a commercial analytics platform: export the transactions and token transfers around a set of addresses into a database and analyse the flows yourself, which is both cheaper and more defensible than citing a vendor's attribution.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Gives you the raw data, so your analysis is reproducible and your conclusions are yours — unlike commercial blockchain-analytics tools whose attribution methods are proprietary and unexaminable
- Export to a warehouse means SQL analysis over blockchain data, which is far more tractable for a data journalist than an API-by-API approach
- Open source and free against public blockchain data, so the only cost is infrastructure
- Established tooling in the blockchain data ecosystem with a clear scope

## 5. Cons

- Requires an archive node or a node-provider endpoint: running your own archive node is a serious storage commitment, and using a provider means disclosing your queries to them
- Addresses are pseudonymous, and attributing an address to a person or organisation is the hard part that this does not help with — exactly where commercial tools add their (proprietary) value
- Data volume is very large: exporting a meaningful slice of Ethereum history is terabyte-scale, so scoping matters
- Ethereum-specific, with sibling projects for other chains of varying maintenance quality

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. The blockchain-etl family is established in the data-engineering side of blockchain analysis; journalism use is plausible but unverified here.

## 7. Assessment

Use it when a story turns on cryptocurrency flows and you want analysis you can defend — the reproducibility argument against commercial attribution tools is strong, since you cannot explain in print what a vendor's proprietary clustering did. For your profile the honest limitation is attribution: the blockchain tells you what moved where, and connecting an address to a named person requires conventional reporting (exchange records, leaks, admissions). Scope your export tightly and budget node access.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with modest ongoing activity. Classified stable-low: the export logic is largely stable because the data model is, so low velocity is less concerning than it would be for a scraper.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Blockchain data is public by design.

**Restrictions:** Permissive as published.

**Licence evidence:** https://github.com/blockchain-etl/ethereum-etl

## 10. Costs

No software fee. The real costs are node access — running an archive node is multi-terabyte storage, and a commercial node provider charges per request (not priced here) — plus warehouse storage for exports. This is the most infrastructure-heavy item in this segment. Estimate.

## 11. Privacy and data flows

If you run your own node, your queries disclose nothing. Using a commercial node provider discloses which addresses you are investigating to that provider — a meaningful exposure when the subject may be a well-resourced actor.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Requires archive-node access or a commercial provider; address attribution is not solved by this tool

## 13. Alternatives

- BlockSci for academic-grade blockchain analysis with its own infrastructure requirements
- [GraphSense](OSINT-C3-21.md) for a platform-oriented approach to cryptocurrency flow analysis
- Commercial analytics (Chainalysis class) for attribution, accepting proprietary methods and cost

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/blockchain-etl/ethereum-etl
- https://ethereum-etl.readthedocs.io/

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

← 273. [US Senate Lobbying Disclosure Act database](SUR-B2-16.md) · 275. [security-misc (Kicksecure)](SUR-B3-21.md) →
