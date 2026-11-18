# ICIJ Datashare

`JAI-A2-23` · **92/100** · overall rank 25 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 8) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 5) |
| **Subcategory** | Leak analysis platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | International Consortium of Investigative Journalists |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ICIJ/datashare) · [Documentation](https://icij.gitbook.io/datashare/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 92/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the platform; bundled NER models carry their own terms and were not individually verified. |
| **Restrictions** | AGPL-3.0 network copyleft: modifying Datashare and offering it over a network to third parties obliges you to publish your modified source. Running it unmodified for your own newsroom is unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Desktop mode: zero infrastructure. Server mode estimate: an Elasticsearch node with 8-16GB RAM, PostgreSQL, Redis and worker capacity — realistically one well-provisioned VM for a few hundred thousand documents, scaling with OCR load. Assumptions: self-hosted, no managed Elasticsearch. Operating effort is the dominant cost in server mode.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ICIJ/datashare/blob/master/LICENSE
- https://github.com/ICIJ/datashare
- https://icij.gitbook.io/datashare/

---

## 1. Purpose

Self-hosted document-analysis platform that extracts text and entities from a document collection and gives journalists a search, tagging and review interface, available as a desktop application or a multi-user server deployment.

## Journalism / investigative use case

The reference end-to-end newsroom stack for a leaked document set: one journalist can run it as a desktop app over 50,000 files, or a cross-border team can run it in server mode and share tags and saved searches across an investigation — the architecture ICIJ built for its own cross-border projects.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Built by the organisation that runs the largest cross-border leak investigations, so the workflow assumptions (tagging, batch search, team sharing) match how reporting actually happens
- Desktop mode is the standout feature: a journalist with no infrastructure gets OCR plus NER plus search on their own laptop, with the documents never leaving it
- Explicitly designed so no external cloud services are required — the README states sensitive material stays under your control, which is the correct architecture for source protection
- Very active: pushed 2026-11-17 with release 21.24.2 on 2026-11-16, and multiple NER backends (CoreNLP, Ixa Pipes, MITIE) bundled

## 5. Cons

- Server mode needs real infrastructure — Elasticsearch, PostgreSQL, Redis — and the operational capacity to run them; this is where small newsrooms stall
- Entity types are limited to person/organisation/location, so it indexes and surfaces rather than resolving entities; cross-document identity work needs nomenklatura or manual effort
- AGPL-3.0 obligations apply if you modify it and host it for others, which constrains building a customised newsroom service on top
- Elasticsearch dependency carries the Elastic licensing question that Solr/OpenSearch avoid — relevant if you redistribute a bundled deployment

## 6. Feedback (documented)

No individual user reports verified. The strongest documented signal is institutional: ICIJ builds and uses Datashare for its own investigations, and the release cadence (21.24.x in November 2026) reflects a tool under continuous internal use. 783 stars, 76 open issues.

## 7. Assessment

For a small newsroom I would recommend Datashare desktop over almost anything else in this pillar — it is the shortest path from 'we received a dump' to 'reporters are searching it' without an engineer. In server mode the choice between Datashare and OpenAleph is close: Datashare has the better reporter UI and institutional backing; OpenAleph has the stronger entity model and cross-referencing against sanctions and registry data. If your investigations are document-centric, choose Datashare; if they are entity-centric, choose OpenAleph.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 21.24.2 (2026-11-16), 783 stars, 76 open issues. Daily-scale commits, releases within the week, and an institutional owner that depends on the tool operationally — the strongest form of maintenance evidence available.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a for the platform; bundled NER models carry their own terms and were not individually verified.

**Restrictions:** AGPL-3.0 network copyleft: modifying Datashare and offering it over a network to third parties obliges you to publish your modified source. Running it unmodified for your own newsroom is unaffected.

**Licence evidence:** https://github.com/ICIJ/datashare/blob/master/LICENSE

## 10. Costs

No software fee. Desktop mode: zero infrastructure. Server mode estimate: an Elasticsearch node with 8-16GB RAM, PostgreSQL, Redis and worker capacity — realistically one well-provisioned VM for a few hundred thousand documents, scaling with OCR load. Assumptions: self-hosted, no managed Elasticsearch. Operating effort is the dominant cost in server mode.

## 11. Privacy and data flows

Designed for local custody: no third-party services are required, documents remain on your hardware, and desktop mode keeps everything on one machine. Residual risks: Elasticsearch must not be exposed, and in server mode the index becomes a high-value target that needs encryption at rest and strict access control.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [OpenAleph](JAI-A2-35.md) where entity cross-referencing against sanctions and registries is the priority
- [Uwazi](OSINT-C3-05.md) for public-facing document collections
- [Paperless-ngx](JAI-A2-38.md) for a small internal archive with far lower operational cost

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ICIJ/datashare
- https://icij.gitbook.io/datashare/
- https://github.com/ICIJ/datashare/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 24. [Dangerzone](SUR-B3-03.md) · 26. [OnionShare](SUR-B3-04.md) →
