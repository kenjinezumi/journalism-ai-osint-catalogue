# juditha

`OSINT-C3-09` · **63/100** · overall rank 307 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 119) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 39) |
| **Subcategory** | Entity lookup service |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Data and Research Center (DARC) |
| **Maintenance** | Uncertain |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/dataresearchcenter/juditha) · [Documentation](https://github.com/dataresearchcenter/juditha#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 63/100**

---

## 1. Purpose

Fast lookup service for canonical entity names, built to check whether a string matches a known entity in a reference dataset such as OpenSanctions or a FollowTheMoney collection.

## Journalism / investigative use case

High-speed name checking inside an ingest pipeline: as documents are processed, test every extracted name against a reference set of sanctioned entities and known companies, so flagged documents surface immediately rather than after a separate screening pass.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Designed for the pipeline position where screening actually belongs — at ingest, not as a later batch — which shortens the time between receiving documents and knowing which matter
- Built by DARC, the same organisation maintaining OpenAleph, so it fits coherently with the FollowTheMoney and OpenSanctions stack
- Narrow scope done well: fast canonical-name lookup rather than a general matching framework, which makes it comprehensible and replaceable
- Self-hosted, so the names you check are not disclosed to anyone

## 5. Cons

- Very small project with minimal community, so documentation is thin and you are reliant on the maintainer's context — a real adoption cost
- Name lookup is not entity resolution: a match is a string correspondence requiring adjudication, and treating it as identification would produce false allegations
- Tightly coupled to the FollowTheMoney and OpenSanctions ecosystem, so its value depends on having adopted that stack
- Maintenance follows one organisation's needs, so continuity depends on DARC's priorities

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under DARC's maintenance, in the same organisation that maintains OpenAleph. No independent deployment verified.

## 7. Assessment

Integrate it if you have adopted the OpenAleph and OpenSanctions stack and want screening at ingest — the pipeline position is the right one and the component is small enough to understand. For your profile the caution is interpretive rather than technical: a name match at ingest is a flag for human attention, and the pipeline should route flagged documents to a reviewer rather than labelling them. Outside that ecosystem, rigour plus RapidFuzz over your own reference list does the same job.

## 8. Maintenance

**Uncertain** — Verified via the GitHub API 2026-11-17 as live and non-archived under DARC's maintenance. The project is small with limited release history, and its continuity depends on one organisation's internal needs — classified Uncertain rather than inferring health from the parent organisation's activity on other repositories.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Reference data you load carries its own licence — OpenSanctions data is CC-BY-NC-4.0, which applies to this use.

**Restrictions:** Code permissive as published. The data licence is the operative restriction if you load OpenSanctions.

**Licence evidence:** https://github.com/dataresearchcenter/juditha

## 10. Costs

No fee. A small service plus the reference dataset. Negligible infrastructure. Estimate.

## 11. Privacy and data flows

Self-hosted lookups disclose nothing externally — the key property for screening names from a confidential document set.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [yente](JAI-A2-61.md) for a fuller self-hosted matching API over the same data
- [rigour](JAI-A2-44.md) plus RapidFuzz over your own reference list for a dependency-light equivalent
- [nomenklatura](JAI-A2-30.md) for batch resolution rather than inline lookup

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/dataresearchcenter/juditha

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

← 306. [HURIDOCS preserve](OSINT-C3-10.md) · 308. [CouncilSearcher](OSINT-C1-14.md) →
