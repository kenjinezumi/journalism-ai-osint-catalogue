# Neo4j Community Edition

`OSINT-C3-35` · **81/100** · overall rank 142 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 45) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 10) |
| **Subcategory** | Graph database |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Neo4j Inc. |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 (Community Edition); Enterprise and Infinigraph editions are commercially licensed |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** — Community Edition free (GPL-3.0); Enterprise and Infinigraph quote-only; AuraDB Free USD 0, Professional from USD 0.09/GB/hour, Business Critical from USD 0.20/GB/hour (verified 2026-11-16) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/neo4j/neo4j) · [Documentation](https://neo4j.com/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 3/5 → **weighted 81/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 (Community Edition); Enterprise and Infinigraph editions are commercially licensed |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0 on Community Edition: embedding in a distributed product triggers copyleft, which is the deliberate commercial boundary. Enterprise features (clustering, role-based access control, multi-database) require a paid licence at a price not publicly listed. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** — Community Edition free (GPL-3.0); Enterprise and Infinigraph quote-only; AuraDB Free USD 0, Professional from USD 0.09/GB/hour, Business Critical from USD 0.20/GB/hour (verified 2026-11-16) |
| **Additional costs** | Optional paid Enterprise licence or metered AuraDB hosting; self-hosted JVM infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Community Edition: no licence fee, free download (verified 2026-11-16). Enterprise/Infinigraph: quote required, no public price. AuraDB: Free $0; Professional from $0.09/GB/hour (min 1GB); Business Critical from $0.20/GB/hour (min 2GB); Virtual Dedicated Cloud contact sales — hourly metering includes storage, compute, IO, network and backups (all verified 2026-11-16, USD). Self-hosting infrastructure: a JVM host with substantial RAM. Estimate for self-hosting.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://neo4j.com/pricing/
- https://github.com/neo4j/neo4j
- `../sources/recovered/cat/pricing.tsv`
- `../sources/evidence/pricing.md`

---

## 1. Purpose

Graph database with the Cypher query language, ACID transactions, indexing and a browser interface, available as a GPL-3-licensed Community Edition and commercial Enterprise editions.

## Journalism / investigative use case

A persistent, queryable investigation graph that several people share: load entities and relationships from leaks, registries and sanctions data, then answer questions in Cypher — 'find paths of length three between this politician and this company' — interactively rather than by rerunning a script.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Cypher makes relationship queries expressible and readable, which matters when an analyst rather than an engineer needs to ask the next question — path queries in particular are awkward in SQL and natural here
- Persistent and multi-user, so an investigation graph becomes shared infrastructure rather than one person's notebook state
- Browser interface lets a non-engineer explore and visualise query results directly, lowering the barrier to using the graph
- Community Edition is GPL-3 licensed and free to download (verified on the vendor pricing page), so the capability is genuinely available without a licence purchase

## 5. Cons

- Community Edition is deliberately limited — single database, no clustering, no role-based access control — and the Enterprise features that a multi-user newsroom might want are quote-only with no public price (verified on the vendor pricing page 2026-11-16)
- GPL-3 on the Community Edition constrains embedding it in a distributed product, and the licensing split is a deliberate commercial funnel
- Operating a JVM graph database with adequate memory is real infrastructure, and a badly tuned Neo4j performs poorly in ways that look like a data problem
- AuraDB, the managed option, is priced per GB-hour (from $0.09/GB/hour Professional, from $0.20/GB/hour Business Critical, verified 2026-11-16) and places your investigation graph in a vendor's cloud

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented pricing, verified on the vendor page 2026-11-16 and recorded in sources/recovered/cat/pricing.tsv: Community Edition GPL-3 and free to download; Enterprise and Infinigraph editions contact-sales (quote required); AuraDB Free $0, Professional from $0.09/GB/hour (minimum 1GB), Business Critical from $0.20/GB/hour (minimum 2GB), with hourly metering including storage, compute, IO, network and backups.

## 7. Assessment

Adopt the Community Edition for a shared investigation graph where Cypher's expressiveness earns its operational cost — which is mainly when several people need to ask relationship questions over months. For your profile avoid AuraDB for investigation data: per-GB-hour billing on a graph you will keep for years is both expensive and a custody decision. If Community Edition's single-database and access-control limits bind, consider whether DuckDB or a FollowTheMoney-based store would serve, since Enterprise pricing is quote-only.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived with continuous development under commercial maintenance. Vendor pricing page verified 2026-11-16 confirming Community Edition availability under GPL-3.

## 9. Licensing

**Licence:** GPL-3.0 (Community Edition); Enterprise and Infinigraph editions are commercially licensed _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0 on Community Edition: embedding in a distributed product triggers copyleft, which is the deliberate commercial boundary. Enterprise features (clustering, role-based access control, multi-database) require a paid licence at a price not publicly listed.

**Licence evidence:** https://neo4j.com/pricing/

## 10. Costs

Community Edition: no licence fee, free download (verified 2026-11-16). Enterprise/Infinigraph: quote required, no public price. AuraDB: Free $0; Professional from $0.09/GB/hour (min 1GB); Business Critical from $0.20/GB/hour (min 2GB); Virtual Dedicated Cloud contact sales — hourly metering includes storage, compute, IO, network and backups (all verified 2026-11-16, USD). Self-hosting infrastructure: a JVM host with substantial RAM. Estimate for self-hosting.

## 11. Privacy and data flows

Self-hosted Community Edition keeps the graph entirely on your infrastructure. AuraDB places it with the vendor, which for an investigation graph containing leak-derived entities is a significant custody decision.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Community Edition lacks access control and clustering; Enterprise pricing is quote-only

## 13. Alternatives

- DuckDB with recursive SQL for many relationship queries without a graph database
- [NetworkX](OSINT-C3-31.md) or igraph for analysis without persistence
- [Kùzu](JAI-A3-18.md) — AVOID, archived as of 2025-10-10

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/neo4j/neo4j
- https://neo4j.com/pricing/
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

← 141. [libimobiledevice](SUR-B3-14.md) · 143. [nomenklatura](JAI-A2-30.md) →
