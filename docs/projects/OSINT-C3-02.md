# Aleph (alephdata, original)

`OSINT-C3-02` · **77/100** · overall rank 184 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 61) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 14) |
| **Subcategory** | Investigative data platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | OCCRP (original; development has moved to the OpenAleph fork) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/alephdata/aleph) · [Documentation](https://docs.aleph.occrp.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 2/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Investigative data platform that indexes documents and structured datasets as FollowTheMoney entities, with search, cross-referencing between datasets and collaborative collections — the original OCCRP implementation.

## Journalism / investigative use case

The system that established this category and still runs OCCRP's own network. Catalogued here separately from OpenAleph because it is the repository most documentation, tutorials and search results point at, and because knowing which line is maintained is a concrete planning fact.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- The origin of the FollowTheMoney ecosystem and of entity-centric investigative search, so understanding it explains OpenAleph, yente, nomenklatura and much of the OSINT data tooling in this catalogue
- MIT licensed with a substantial deployment history across investigative networks (2,513 stars)
- OCCRP continues to operate Aleph for its own network, so the software works and is in production use
- Documentation is more extensive than the fork's, reflecting years of deployment experience

## 5. Cons

- Maintenance of the public repository has visibly slowed: last push 2026-02-20 and latest release 4.1.7 (2025-10-27) — nine months without a push and over a year without a release, while the OpenAleph fork released 5.4.0 on 2026-11-16
- No deprecation notice, which is the hazard: a newsroom following the documentation will deploy the less-maintained line without knowing a divergence exists
- Heavy infrastructure (Elasticsearch, PostgreSQL, Redis, ingest workers) for a version that is no longer the development focus
- The ecosystem has moved: ingest-file's maintained fork is OpenAleph's, and FollowTheMoney's active line is OpenSanctions', so building on alephdata means assembling a stale stack

## 6. Feedback (documented)

No individual user reports verified in this survey. The decisive documented facts, verified this session: alephdata/aleph archived=false, pushed 2026-02-20, release 4.1.7 (2025-10-27); openaleph/openaleph is a GitHub fork with parent=alephdata/aleph, pushed 2026-11-16, release 5.4.0 the same day. Recorded in sources/evidence/leads.md L3, and consistent with session 1's ground_truth.tsv note 'superseded by openaleph fork'.

## 7. Assessment

Reference only — deploy OpenAleph instead. The reason this entry exists is that the divergence is invisible unless you check: alephdata/aleph is not archived, its documentation is better, and it is what search results surface, so a team acting reasonably will choose the wrong one. For your profile the single actionable fact is to point every link, bookmark and internal note at OpenAleph and the OpenSanctions FollowTheMoney line.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-02-20, latest release 4.1.7 (2025-10-27), 2,513 stars, 69 open issues on the related followthemoney repository. Nine months without a push and thirteen without a release, while the fork releases monthly. Declining rather than archived — and the absence of a deprecation notice is itself the risk.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Loaded datasets carry their own licences.

**Restrictions:** None material on the code.

**Licence evidence:** https://github.com/alephdata/aleph/blob/main/LICENSE

## 10. Costs

No software fee. Infrastructure equivalent to OpenAleph's (Elasticsearch cluster, PostgreSQL, Redis, workers) — a four-figure annual commitment plus ops time, which is not worth spending on the less-maintained line. Estimate.

## 11. Privacy and data flows

Self-hosted with no required third-party calls, as with OpenAleph.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Development has moved to the OpenAleph fork; no deprecation notice makes the stale line easy to adopt by mistake

## 13. Alternatives

- [OpenAleph](JAI-A2-35.md) — the maintained fork, use this instead
- [ICIJ Datashare](JAI-A2-23.md) for a document-centric alternative with lower operational burden
- [Hoover](OSINT-C3-03.md) or Uwazi for lighter document-platform needs

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/alephdata/aleph
- https://github.com/openaleph/openaleph
- `../sources/evidence/leads.md`
- `../sources/recovered/cat/ground_truth.tsv`

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

← 183. [OpenDroneMap (ODM)](OSINT-C2-46.md) · 185. [Delta Chat / chatmail core](SUR-B3-26.md) →
