# dnstwist

`OSINT-C3-25` · **75/100** · overall rank 208 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 67) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 18) |
| **Subcategory** | Domain analysis |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Marcin Ulikowski (elceef) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/elceef/dnstwist) · [Documentation](https://dnstwist.it/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

---

## 1. Purpose

Tool that generates and tests permutations of a domain name — typos, homoglyphs, character swaps, alternative TLDs — to find registered lookalike domains, with DNS, WHOIS and page-similarity checks.

## Journalism / investigative use case

Finding impersonation infrastructure aimed at your own outlet or at a story's subject: lookalike domains are used for phishing journalists and for publishing fake versions of news sites, and dnstwist finds the registered ones systematically rather than by accident.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Directly protective as well as investigative: running it against your own domain finds the lookalikes being prepared to phish your staff or impersonate your publication, which is a realistic threat to exile media
- Homoglyph detection catches the internationalised-domain tricks that are invisible to the eye, which is exactly how credential-phishing domains evade notice
- Page-similarity checking distinguishes a parked typo-squat from an active clone of your site — the difference between noise and an incident
- Long-established, widely packaged and MIT licensed

## 5. Cons

- Permutation generation produces a large candidate space, so results need filtering and most registered hits are commercial typo-squatting rather than targeted impersonation
- DNS and WHOIS checks against many candidates are visible to resolvers and registries, and WHOIS data availability has degraded substantially under privacy rules
- Finding a lookalike domain tells you it exists, not who registered it — attribution needs registrar records, certificate data or hosting analysis
- Maintenance cadence is steady rather than brisk

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with a long history. dnstwist is a standard tool for lookalike-domain detection, well established in the security community.

## 7. Assessment

Adopt it and run it on a schedule against your own domains — this is one of the few tools in the catalogue that protects you directly, and for a media-in-exile outlet impersonation and credential phishing are concrete rather than theoretical risks. Pair it with certificate-transparency monitoring, which catches lookalikes at the moment a certificate is issued, often before the site is live. Treat discovered domains as leads for attribution work.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with a long release history and steady rather than frequent updates. Classified stable-low: the permutation logic is mature and the tool is feature-complete for its purpose.

## 9. Licensing

**Licence:** Apache-2.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Permissive as published.

**Licence evidence:** https://github.com/elceef/dnstwist

## 10. Costs

No fee. Negligible compute. Optional paid data sources for richer WHOIS or registration data (not priced here).

## 11. Privacy and data flows

DNS and WHOIS lookups are visible to resolvers and registries. Checking your own domain's permutations discloses little of consequence; checking a target's may indicate interest.

## 12. Verdict

**Adopt**

## 13. Alternatives

- certstream monitoring for lookalike detection at certificate issuance — faster and fully passive
- Commercial brand-protection services, which are more thorough and expensive
- Manual registry searches for a specific suspected domain

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/elceef/dnstwist
- https://dnstwist.it/

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

← 207. [Citizen Lab URL test lists](SUR-B1-06.md) · 209. [libratom](JAI-A1-13.md) →
