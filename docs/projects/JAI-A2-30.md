# nomenklatura

`JAI-A2-30` · **81/100** · overall rank 143 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 59) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 34) |
| **Subcategory** | Entity resolution |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenSanctions |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Mixed |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opensanctions/nomenklatura) · [Documentation](https://github.com/opensanctions/nomenklatura#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 2/5 · licence+cost 5/5 → **weighted 81/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the code. Note that OpenSanctions DATA is CC-BY-NC-4.0 and separately licensed — see the OpenSanctions entry. |
| **Restrictions** | Code unrestricted. The restriction appears if you resolve against OpenSanctions data commercially — that is a data-licence question, not a code one. |
| **Open-source status** | **Mixed** — Open-source code, restricted data licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Optional Elasticsearch/OpenSearch and Redis for candidate generation at scale; CPU-bound otherwise. The dominant cost is human adjudication time on borderline pairs. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/opensanctions/nomenklatura/blob/main/LICENSE
- https://github.com/opensanctions/nomenklatura

---

## 1. Purpose

Entity-resolution and deduplication toolkit for FollowTheMoney data: candidate generation, scoring algorithms, an interactive adjudication loop, and a resolver file recording every merge decision.

## Journalism / investigative use case

The deduplication engine behind OpenSanctions: merge the same oligarch or company across sanctions lists, leaks and corporate registries while keeping an auditable record of every merge a human approved — so a later challenge to 'how do you know these are the same person' has a documented answer.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- The resolver file is the standout feature: entity-resolution decisions become a version-controlled artefact rather than a black box, which is exactly what investigative accountability requires
- Battle-tested in production on OpenSanctions' own cross-source dataset, which is one of the larger continuously-resolved entity datasets in existence
- Interactive adjudication keeps a human in the loop on borderline merges rather than silently guessing
- Current and frequently released (4.17.3, 2026-10-21) under MIT

## 5. Cons

- Only speaks FollowTheMoney, so arbitrary CSVs must first be mapped into the ontology — a non-trivial modelling step that is the real adoption cost
- Documentation assumes familiarity with the OpenSanctions pipeline; there is no standalone tutorial for a newsroom coming in cold
- Resolver files become long-lived artefacts that must be managed and migrated, and a corrupted or lost resolver loses your merge history
- Enrichment connectors can query external APIs (OpenCorporates, Wikidata) — off by default, but a configuration mistake would send entity names to a third party

## 6. Feedback (documented)

No individual user reports verified. The production signal is verifiable from the OpenSanctions codebase: nomenklatura is the resolution layer of a publicly operated dataset, released on a regular cadence (273 stars, 19 open issues).

## 7. Assessment

If you adopt FollowTheMoney, adopt nomenklatura with it — the pairing is what gives you auditable cross-dataset identity. If you are not using FtM, Splink is the better general-purpose choice and nomenklatura's mapping overhead is not worth it. For your profile the resolver-as-artefact design is the strongest argument: it converts a methodological weakness of investigative data work into something you can show an editor or a lawyer.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 4.17.3 (2026-10-21), latest tag 4.18.0, 273 stars, 19 open issues. Frequent releases, commercial-entity backing (OpenSanctions Datenbanken GmbH), low backlog.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the code. Note that OpenSanctions DATA is CC-BY-NC-4.0 and separately licensed — see the OpenSanctions entry.

**Restrictions:** Code unrestricted. The restriction appears if you resolve against OpenSanctions data commercially — that is a data-licence question, not a code one.

**Licence evidence:** https://github.com/opensanctions/nomenklatura/blob/main/LICENSE

## 10. Costs

No fee. Optional Elasticsearch/OpenSearch and Redis for candidate generation at scale; CPU-bound otherwise. The dominant cost is human adjudication time on borderline pairs. Estimate.

## 11. Privacy and data flows

Local by default. Enrichment connectors to OpenCorporates or Wikidata must be explicitly configured and would disclose the names you are resolving — review before enabling on a confidential list.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Splink](JAI-A2-48.md) for general-purpose probabilistic linkage without the FtM requirement
- [rigour](JAI-A2-44.md) for the normalisation stage that precedes resolution
- [dedupe](JAI-A2-11.md) for small analyst-driven jobs, with the maintenance caveat noted in its entry

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/opensanctions/nomenklatura
- https://github.com/opensanctions/nomenklatura/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |

---

← 142. [Neo4j Community Edition](OSINT-C3-35.md) · 144. [pyannote.audio](JAI-A2-41.md) →
