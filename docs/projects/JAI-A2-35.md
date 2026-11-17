# OpenAleph

`JAI-A2-35` · **93/100** · overall rank 19 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 6) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 3) |
| **Subcategory** | Leak analysis platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | DARC — Data and Research Center (independent fork of alephdata/aleph) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/openaleph/openaleph) · [Documentation](https://openaleph.org/docs/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 93/100**

---

## 1. Purpose

Self-hosted investigative data platform that indexes documents and structured datasets as FollowTheMoney entities, provides full-text and entity search, cross-referencing between datasets, and collaborative collections.

## Journalism / investigative use case

The primary live candidate for standing up a searchable archive over a multi-million-document leak for a reporting team, with automatic cross-referencing of names in the leak against sanctions lists, PEP data and corporate registries — the capability that turns a document archive into an investigative lead generator.

## 2. Audience

engineer, newsroom analyst, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Cross-referencing across datasets is the distinguishing capability in this pillar: upload a leak and it tells you which names also appear in sanctions or registry data you have loaded
- Verified as the actively maintained path: GitHub API confirms fork=true with parent alephdata/aleph, and OpenAleph released 5.4.0 on 2026-11-16 while upstream Aleph last released 4.1.7 in October 2025
- MIT licensed, fully self-hostable, with no third-party calls required for core indexing — correct architecture for sensitive material
- Maintained in step with its own ingest stack (openaleph/ingest-file) and the FtM/OpenSanctions ecosystem, so the components are version-coherent

## 5. Cons

- Heavy infrastructure footprint: Elasticsearch, PostgreSQL, Redis and worker containers — the highest operational burden of any tool in this segment, and Elasticsearch index sizing is the main scaling cost at multi-million-document scale
- Smaller maintainer base than OCCRP-era Aleph (156 stars, 16 open issues) — institutionally backed by DARC but the contributor pool is thin, which is a continuity risk for a system holding your archive
- Upgrades across a forked lineage require care; you are now on DARC's release train, not OCCRP's
- Reporter-facing UX is functional rather than polished compared with Datashare

## 6. Feedback (documented)

No individual user reports verified. The decisive documented finding, established in this session: GitHub API reports openaleph/openaleph as fork=true with parent=alephdata/aleph, releasing 5.4.0 on 2026-11-16, while alephdata/aleph last pushed 2026-02-20 with release 4.1.7 (2025-10-27). This confirms the fork is the maintained path and the two are not interchangeable (recorded in sources/evidence/leads.md).

## 7. Assessment

If your work is entity-centric — ownership structures, sanctions exposure, cross-border networks — this is the platform I would build on, and the fork question is now settled in its favour. The honest caveat is operational: do not adopt OpenAleph without someone who can run Elasticsearch properly, because a badly operated index over your only copy of a leak is a serious risk. For a document-centric team without that capacity, Datashare desktop is the better answer.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, fork=true (parent alephdata/aleph), pushed_at 2026-11-16, latest release 5.4.0 (2026-11-16), 156 stars, 16 open issues. Same-day push and release on a 5.x line, with coordinated releases across openaleph/ingest-file. Active and institutionally maintained; small contributor base is the residual risk.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Datasets you load carry their own licences — notably OpenSanctions data is CC-BY-NC-4.0.

**Restrictions:** Code unrestricted. The licence risk sits in the data you ingest, not the platform.

**Licence evidence:** https://github.com/openaleph/openaleph/blob/main/LICENSE

## 10. Costs

No software fee. Infrastructure estimate for a few million documents: an Elasticsearch cluster (start at 2 nodes, 16-32GB RAM each), PostgreSQL, Redis, and worker containers for ingest/OCR — realistically a four-figure annual cloud bill or equivalent on-prem hardware, plus meaningful ops time. Assumptions: self-managed Elasticsearch, no managed service, OCR load moderate. The largest cost in the whole catalogue after human labour.

## 11. Privacy and data flows

Fully self-hosted with no third-party calls required for core indexing. Residual risks are operational and serious: the Elasticsearch index must never be exposed, backups contain the entire leak and need encryption, and access control within collections is your responsibility.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ICIJ Datashare](JAI-A2-23.md) where a reporter-facing UI and lower ops burden matter more than cross-referencing
- alephdata/aleph — reference only; use OpenAleph instead
- [Uwazi](OSINT-C3-05.md) for public-facing collections rather than internal investigation

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/openaleph/openaleph
- https://openaleph.org/docs/
- https://github.com/openaleph/openaleph/blob/main/LICENSE
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 18. [whisper.cpp](JAI-A2-59.md) · 20. [changedetection.io](SUR-B1-15.md) →
