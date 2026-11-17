# sugartrail

`OSINT-C3-19` · **75/100** · overall rank 212 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 69) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 19) |
| **Subcategory** | Corporate network analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/sugartrail) · [Documentation](https://github.com/bellingcat/sugartrail#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Tool that builds a network graph from UK Companies House data, following officers, addresses and company relationships outward from a starting entity to map connected corporate structures.

## Journalism / investigative use case

Mapping a UK corporate network from one starting point: begin with a company or director and follow officers, shared addresses and appointments to reveal the cluster of entities around them — the standard method for exposing shell-company networks and the addresses that host hundreds of them.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Automates the manual click-through that UK corporate investigation otherwise requires, which is the difference between mapping ten companies and mapping four hundred
- Address-based traversal is particularly productive: a single accommodation address hosting hundreds of companies is a recurring and reportable pattern that this surfaces directly
- Built by Bellingcat for investigators, so the traversal logic reflects how corporate-network investigation actually proceeds
- Companies House data is openly licensed and free via API, so the whole capability costs nothing

## 5. Cons

- UK only, and tightly coupled to Companies House's data model, so it is a template rather than a tool elsewhere
- Network expansion grows combinatorially: an unconstrained traversal from a busy address produces an unusable graph, so hop limits and filtering are essential and require judgement
- Shared officers and addresses indicate association, not wrongdoing — a company-formation agent's address legitimately hosts thousands of companies, and publishing a network as evidence of impropriety would be wrong
- Small project; verify liveness and API compatibility before relying on it

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under Bellingcat's maintenance. Bellingcat's published UK corporate-network investigations are the relevant context for the method's productivity.

## 7. Assessment

Adopt it for UK corporate work and treat the output as a map requiring interpretation. For your profile the two disciplines are hop limits (constrain the traversal or drown) and the formation-agent caveat (a shared address is usually a service provider, not a conspiracy). The transferable value is the method: any jurisdiction with an open company register supports the same traversal, and building it for your region is a contained project with high investigative return.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under Bellingcat's maintenance, with modest activity typical of a focused investigative tool. Classified stable-low; verify Companies House API compatibility before relying on it.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** UK Companies House data is published under the Open Government Licence, which permits reuse with attribution.

**Restrictions:** Code permissive as published. Companies House data requires OGL attribution — straightforward but a real publication obligation.

**Licence evidence:** https://github.com/bellingcat/sugartrail

## 10. Costs

No fee. Companies House API is free with rate limits. Negligible compute. Estimate.

## 11. Privacy and data flows

Queries go to Companies House, disclosing the companies you are investigating to a UK government system. Public-register research, so unremarkable.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- UK only; shared addresses and officers indicate association, not wrongdoing

## 13. Alternatives

- Companies House API directly with your own traversal logic
- OpenCorporates for multi-jurisdiction corporate data, with its own access terms
- Building an equivalent traversal for another jurisdiction's open register — the transferable approach

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/bellingcat/sugartrail

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

← 211. [Ragas](JAI-A3-13.md) · 213. [eScriptorium](JAI-A2-15.md) →
