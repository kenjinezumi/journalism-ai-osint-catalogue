# ingest-file (OpenAleph fork)

`JAI-A2-25` · **79/100** · overall rank 163 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 64) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 37) |
| **Subcategory** | Bulk extraction pipeline |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenAleph / DARC (maintained fork of the archived alephdata/ingest-file) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/openaleph/ingest-file) · [Documentation](https://openaleph.org/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 79/100**

---

## 1. Purpose

Worker service that ingests heterogeneous files — documents, mailboxes, archives, images, spreadsheets — converts and OCRs them, and emits FollowTheMoney entities for indexing by OpenAleph.

## Journalism / investigative use case

The extraction and OCR stage of an entity-centric leak pipeline: it turns a directory of mixed attachments, PST mailboxes and scans into structured FtM records, so the archive can be cross-referenced against sanctions lists and registries rather than merely searched.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Emits FollowTheMoney entities rather than plain text, which is what enables cross-dataset linking downstream — a materially different output from Tika-only pipelines
- Maintained fork of an archived upstream, with releases tracking OpenAleph (5.4.0, 2026-11-12), so the lineage problem is solved rather than inherited
- Handles mailbox and archive formats that defeat most Python-first ingest tools, via Tika and LibreOffice-family converters
- Containerised worker model scales horizontally and isolates parsing of untrusted files

## 5. Cons

- Very small contributor base (15 stars, 8 open issues) — it exists to serve OpenAleph and is not a general-purpose library with a community behind it
- AGPL-3.0 copyleft affects redistribution of modified services, which matters if you build a product around the ingest stage
- OCR throughput is the usual bottleneck on scanned corpora and the fork does not change that ceiling
- Effectively coupled to OpenAleph: using it standalone means adopting the FtM model and writing your own consumer

## 6. Feedback (documented)

No user reports collected. The relevant documented finding is lineage, verified this session: the upstream alephdata/ingest-file is archived while this fork releases in step with OpenAleph 5.4.0 (2026-11-12) — concrete evidence that the maintained path has moved.

## 7. Assessment

Only adopt it as part of an OpenAleph deployment; as a standalone ingest library ICIJ extract or plain Tika is a better fit. Its catalogue value is that it answers the question 'is Aleph's ingest stack dead?' — the upstream is, this fork is not. For your profile that distinction is the actionable fact.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 5.4.0 (2026-11-12), 15 stars, 8 open issues. Releases are version-locked to OpenAleph, which is itself actively released; maintenance is institutional (DARC) rather than community-driven.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: modified network-service redistribution triggers source-release obligations. Internal use is unaffected.

**Licence evidence:** https://github.com/openaleph/ingest-file/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure: containerised workers sized to OCR load, plus the OpenAleph stack it feeds. Estimate only.

## 11. Privacy and data flows

Local processing in worker containers; no external calls required. Container isolation is a genuine security benefit when parsing untrusted files.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [ICIJ extract](JAI-A2-24.md) for a standalone Solr-targeted pipeline
- [Apache Tika](JAI-A2-02.md) server for format extraction without the FtM layer
- [Docling](JAI-A2-12.md) where layout fidelity matters more than entity emission

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/openaleph/ingest-file
- https://openaleph.org/docs/
- https://github.com/openaleph/ingest-file/blob/main/LICENSE

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

← 162. [httpx](OSINT-C3-24.md) · 164. [Stanza](JAI-A2-49.md) →
