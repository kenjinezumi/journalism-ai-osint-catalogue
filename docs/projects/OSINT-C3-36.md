# Maltego

`OSINT-C3-36` · **59/100** · overall rank 325 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 128) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 41) |
| **Subcategory** | Link analysis platform |
| **Type** | application |
| **Bucket** | `proprietary-service` |
| **Maintainer** | Maltego Technologies |
| **Maintenance** | Actively maintained |
| **Licence** | Proprietary commercial licence; Community Edition is a restricted free tier |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://docs.maltego.com/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 1/5 · usability 4/5 · licence+cost 1/5 → **weighted 59/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Commercial link-analysis platform with a graph interface and a transform ecosystem that queries data sources — infrastructure, corporate, social, breach and commercial intelligence — and expands entities into a visual graph.

## Journalism / investigative use case

The commercial benchmark for graph-based investigation: start from a name, domain or company and expand through transforms to related entities, building a visual network. Many OSINT training curricula teach it, so a newsroom hiring an experienced investigator may inherit it as an expectation.

## 2. Audience

specialist investigator

## 3. Project type

application · bucket `proprietary-service`

## 4. Pros

- Transform ecosystem is the product: hundreds of integrated data sources queried through one interface, which no open tool matches for breadth of commercial data
- Graph-first interface suits investigative reasoning and is genuinely effective for exploring entity relationships interactively
- Established in the field with extensive training material, so an experienced investigator is likely to be productive immediately
- Credit-based model means light use can be genuinely cheap, including a free Community Edition tier

## 5. Cons

- NOT open source: proprietary software with a credit-metered pricing model, and the costs are substantial at professional tiers — Entry EUR3,000/year (10,000 credits/month, includes Hunchly) and Professional EUR7,500/year (20,000-40,000 credits/month, up to 5 users, billed per seat), with Enterprise quote-only (all verified on the vendor pricing page 2026-11-16)
- Every transform query discloses your target to Maltego and to the underlying data provider — for a surveillance-industry investigation that is a material exposure, and the convenience of the interface makes it easy to forget
- Community Edition is restricted to graph-only use with 200 or 1,000 credits per month, which is enough to learn the tool and not to run an investigation
- Credit consumption is hard to predict, so budgeting is awkward and an exploratory session can consume a month's allowance

## 6. Feedback (documented)

No individual user reports verified in this survey. Pricing verified on the vendor page 2026-11-16 and recorded in sources/recovered/cat/pricing.tsv: Basic free forever (200 credits/month) or Basic+ (1,000 credits/month), Community Edition graph only; Entry EUR3,000/year including Hunchly; Professional EUR7,500/year, up to 5 users, billed per seat; Enterprise custom quote for 5+ users. Maltego's prominence in OSINT training is well documented.

## 7. Assessment

Reference only for your profile, and deliberately so: the open chain in this catalogue (subfinder, httpx, asn, certstream, NetworkX, Gephi) covers most of what Maltego's infrastructure transforms do, at no licence cost and without disclosing your targets to a commercial platform. The case for buying it is an experienced investigator who is already fast in it, or a specific commercial data source you cannot otherwise reach. If you do, budget per-seat annually and treat every transform as a disclosure.

## 8. Maintenance

**Actively maintained** — Commercial product under continuous vendor development; pricing page verified live 2026-11-16 with current tier structure. No repository to assess — maintenance is inferred from the operating commercial service and active vendor documentation, which is the only evidence available for proprietary software.

## 9. Licensing

**Licence:** Proprietary commercial licence; Community Edition is a restricted free tier _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Transform data comes from many providers under their own terms, several of which restrict redistribution of results.

**Restrictions:** Proprietary throughout. Data-provider terms restrict republication of transform results, which matters if a graph is the basis of a published graphic.

**Licence evidence:** https://www.maltego.com/pricing/

## 10. Costs

Verified 2026-11-16 from the vendor pricing page: Basic free forever (200 credits/month) or Basic+ (1,000 credits/month), Community Edition graph only; Entry EUR3,000/year (10,000 credits/month, includes Hunchly); Professional EUR7,500/year (20,000-40,000 credits/month, up to 5 users, billed per seat); Enterprise custom quote (5+ users). Credits are consumed per transform, so operating cost scales with investigation intensity and is hard to forecast.

## 11. Privacy and data flows

The weakest point for investigative use: every transform discloses your target entity to Maltego and to the underlying data provider, continuously through an investigation. For work on a surveillance vendor or a state actor, that is an exposure the open alternatives avoid.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Proprietary with substantial per-seat annual cost; every transform discloses investigation targets to the vendor and data providers

## 13. Alternatives

- The open chain: subfinder plus httpx plus asn plus certstream for discovery, NetworkX for analysis, Gephi for visualisation — no licence cost and no target disclosure
- [SpiderFoot](OSINT-C3-29.md) for automated open-source breadth, accepting its own disclosure footprint
- Hunchly (bundled with Maltego Entry) separately, for browsing-session capture

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `docs-reviewed`

- https://www.maltego.com/pricing/
- `../sources/recovered/cat/pricing.tsv`
- `../sources/evidence/pricing.md`

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

← 324. [FEVER platform and baselines](JAI-A4-06.md) · 326. [Froide](JAI-A1-29.md) →
