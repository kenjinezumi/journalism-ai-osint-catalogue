# ICIJ extract

`JAI-A2-24` · **81/100** · overall rank 140 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 58) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 33) |
| **Subcategory** | Bulk extraction pipeline |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | International Consortium of Investigative Journalists |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ICIJ/extract) · [Documentation](https://github.com/ICIJ/extract#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 81/100**

---

## 1. Purpose

JVM command-line tool that walks a file tree or archive, extracts text and metadata via Apache Tika with parallel workers and Redis-backed queueing, OCRs images, and writes results to Solr or Elasticsearch.

## Journalism / investigative use case

Purpose-built for this domain: the lineage ICIJ used to process multi-terabyte leaks, designed to chew through millions of mixed files, OCR the scanned ones at scale, and feed a search index — the unglamorous stage where most home-grown leak pipelines fall over.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Engineered for the specific failure modes of real leaks — resumable queues, parallel workers, per-file error isolation so one corrupt PDF does not kill a run
- Direct Solr/Elasticsearch output means it slots into an index-first architecture without intermediate storage
- MIT licensed and used by ICIJ at terabyte scale: the most relevant provenance any tool in this subcategory can have
- Current activity (pushed 2026-11-13, tag 9.23.0) with a very clean issue tracker (4 open)

## 5. Cons

- No tagged GitHub releases (only tags), no UI, and documentation written for operators who already understand the architecture — the learning curve is real
- Small user base outside ICIJ, so community answers to operational problems are scarce
- The OCR step is only as good as Tesseract, which caps accuracy on degraded scans regardless of throughput
- JVM plus Redis plus a search index is three moving parts before you have indexed a single document

## 6. Feedback (documented)

No individual user reports verified. The institutional signal is the point: ICIJ maintains and uses it, and the 4 open issues against 257 stars indicate a small but attended project. No third-party newsroom deployment verified.

## 7. Assessment

Choose extract when you are deliberately building an index-first architecture at a scale where Datashare's bundled ingest is the bottleneck. For most of your likely work, Datashare or OpenAleph's ingest-file already wraps this capability with a UI, and standing up extract separately is only justified by scale or by a bespoke index schema. Its credibility is high; its audience is narrow.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest tag 9.23.0, no release objects, 257 stars, 4 open issues. Recent commits and a 9.x tag line, maintained by an organisation that runs it in production. The absence of release objects is a hygiene gap, not an activity signal.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material; note it bundles Tika, whose third-party notices must be reproduced on redistribution.

**Licence evidence:** https://github.com/ICIJ/extract/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure: JVM workers scaled to CPU count, Redis, plus the downstream index. OCR dominates compute on scanned corpora — budget CPU-hours roughly proportional to page count. Estimate; assumes self-hosted.

## 11. Privacy and data flows

Fully self-hosted and designed for controlled leak handling; no external calls in the extraction path.

## 12. Verdict

**Integrate**

## 13. Alternatives

- openaleph/ingest-file for the same stage inside an OpenAleph deployment
- [Apache Tika](JAI-A2-02.md) server plus your own queue if you want Python-native orchestration
- Datashare, which bundles this capability behind a UI

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ICIJ/extract
- https://github.com/ICIJ/extract/blob/master/LICENSE

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

← 139. [GLiNER](JAI-A2-19.md) · 141. [libimobiledevice](SUR-B3-14.md) →
