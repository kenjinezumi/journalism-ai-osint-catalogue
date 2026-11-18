# Kùzu

`JAI-A3-18` · **61/100** · overall rank 318 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 118) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 20) |
| **Subcategory** | Knowledge graphs |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Kùzu Inc. |
| **Maintenance** | Archived or discontinued |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/kuzudb/kuzu) · [Documentation](https://docs.kuzudb.com/) |

**Scores** — relevance 2/5 · capability 4/5 · maintenance 0/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 61/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None, and the MIT licence means a fork is legally straightforward — though maintaining a database engine is not. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Not worth adopting; any use means accepting fork-and-maintain responsibility for a database engine.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/kuzudb/kuzu/blob/master/LICENSE
- https://github.com/kuzudb/kuzu
- `../sources/evidence/leads.md`

---

## 1. Purpose

Embeddable property-graph database with Cypher query support, columnar storage and vectorised execution, designed as the graph equivalent of DuckDB.

## Journalism / investigative use case

Would have been the natural choice for an investigation graph: an embedded property-graph database with Cypher, so entity-relationship analysis over a leak could run in-process with no server — the pattern DuckDB established for tabular analysis.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- The embedded property-graph model is exactly right for investigative graph analysis: Cypher queries over entities and relationships with no server to operate
- Columnar vectorised execution gave genuinely good performance on analytical graph queries, better than embedded alternatives
- MIT licensed with a clean design and good documentation at the point development stopped

## 5. Cons

- ARCHIVED: the GitHub API reports archived=true with the final release v0.11.3 on 2025-10-10 and the last push the same day — read-only, with 4,022 stars at archival. This is a significant loss in a category with few good options
- A graph database holding your investigation data is the worst category of dependency to have frozen: migration means re-modelling, not just re-importing
- Commercial company behind it, and the archival suggests the business did not sustain the open project — a pattern worth noting when evaluating other open-core graph tools
- No successor named in the repository, so the migration path is yours to choose

## 6. Feedback (documented)

No individual user reports verified. The decisive documented fact, established in this session: archived=true per the GitHub API on 2026-11-17, final release v0.11.3 (2025-10-10), 4,022 stars — recorded in sources/evidence/leads.md L10. This is a recent archival of a tool that was gaining adoption, and it has not propagated into most recommendation lists.

## 7. Assessment

Avoid for new deployment, and know the archival if you see Kùzu recommended — it was a genuinely good answer to embedded graph analysis and is now frozen. For your profile the practical alternatives are Neo4j Community (a server, GPL-3.0) for property-graph work, DuckDB with recursive SQL for many graph-shaped questions, or NetworkX for in-memory analysis. The broader lesson for your planning: open-core commercial infrastructure can be withdrawn, and a graph database is an expensive thing to migrate away from.

## 8. Maintenance

**Archived or discontinued** — GitHub API 2026-11-17: archived=true, pushed_at 2025-10-10, latest release v0.11.3 published the same day, 4,022 stars, MIT licence. Archived by the maintainer with a final release — unambiguous and recent.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, and the MIT licence means a fork is legally straightforward — though maintaining a database engine is not.

**Licence evidence:** https://github.com/kuzudb/kuzu/blob/master/LICENSE

## 10. Costs

No fee. Not worth adopting; any use means accepting fork-and-maintain responsibility for a database engine.

## 11. Privacy and data flows

Embedded and local, which was part of its appeal.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Archived as of 2025-10-10 — a frozen database engine is an unacceptable dependency for investigation data

## 13. Alternatives

- [Neo4j Community Edition](OSINT-C3-35.md) for property-graph work with Cypher, accepting a server and GPL-3.0
- DuckDB with recursive SQL for many relationship queries without a graph database
- [NetworkX](OSINT-C3-31.md) or igraph for in-memory graph analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/kuzudb/kuzu
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |

---

← 317. [LibreY](OSINT-C1-03.md) · 319. [Microsoft Planetary Computer](OSINT-C2-45.md) →
