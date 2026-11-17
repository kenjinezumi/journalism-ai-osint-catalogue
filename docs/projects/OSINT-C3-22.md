# OWASP Amass

`OSINT-C3-22` · **75/100** · overall rank 203 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 64) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 16) |
| **Subcategory** | Internet infrastructure mapping |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | OWASP Amass Project |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/owasp-amass/amass) · [Documentation](https://github.com/owasp-amass/amass/wiki) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 3/5 · licence+cost 4/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Network-mapping tool that performs attack-surface discovery through DNS enumeration, certificate transparency, web archives, API sources and optional active probing, building a graph of an organisation's internet assets.

## Journalism / investigative use case

Mapping the internet footprint of an organisation under investigation: a surveillance vendor's subdomains, staging environments, mail infrastructure and related domains — which reveals products, partners and sometimes customers that the public website does not mention.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Breadth of passive sources (certificate transparency, web archives, DNS datasets) means substantial discovery without touching the target, which is the right operational-security posture
- Builds a graph rather than a flat list, so relationships between assets are visible — useful for distinguishing a company's own infrastructure from a shared host
- OWASP project with institutional governance and a long track record, so it is not a weekend tool
- Forgotten staging and development subdomains are a recurring source of investigative material, and systematic enumeration is how you find them

## 5. Cons

- Active enumeration modes send traffic to the target and are detectable; defaults need deliberate configuration if you do not want to announce your interest
- Security-tooling heritage means the framing is penetration testing, and aggressive use against an organisation you do not have authorisation to test raises legal questions in some jurisdictions
- Some data sources require API keys, several of them paid, so full capability has a cost the free tool hides
- Output volume is large and noisy; separating the organisation's real assets from shared-hosting neighbours takes judgement

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under OWASP project governance. Amass is a standard tool in attack-surface discovery, which is well established in the security community.

## 7. Assessment

Adopt it for infrastructure mapping with passive sources only as the default — the passive discovery alone is usually enough and leaves no trace with the target. For your profile the sequence that works is Amass for enumeration, certificate transparency for ongoing monitoring, and RIR records for authoritative ownership before any published claim. Get a view on the legal position for active scanning in your jurisdiction before enabling it against a company.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under OWASP project governance with ongoing development. Maintenance assessed on activity and institutional backing; the project has a long continuous history.

## 9. Licensing

**Licence:** Apache-2.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Third-party data sources have their own terms; several require API keys.

**Restrictions:** Permissive as published. The constraints are legal (active scanning) and contractual (data-source API terms) rather than licence-based.

**Licence evidence:** https://github.com/owasp-amass/amass

## 10. Costs

No fee. Several optional data sources require paid API keys (prices vary; not verified here). Compute is modest. Estimate.

## 11. Privacy and data flows

Passive modes leave no trace with the target. Active modes are visible. Queries to third-party data sources disclose the organisations you are mapping to those providers.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Active scanning modes are detectable and may engage computer-misuse law

## 13. Alternatives

- [subfinder](OSINT-C3-23.md) for faster passive subdomain enumeration with less breadth
- [Metabigor](OSINT-C1-09.md) for keyless public-source footprinting
- certstream plus crt.sh for certificate-based discovery alone

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/owasp-amass/amass
- https://github.com/owasp-amass/amass/wiki

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

← 202. [OONI backend](SUR-B1-04.md) · 204. [RIPE Atlas tooling (Magellan CLI, Cousteau, Sagan)](SUR-B1-12.md) →
