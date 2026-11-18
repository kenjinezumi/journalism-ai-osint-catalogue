# Apache Tika

`JAI-A2-02` · **87/100** · overall rank 63 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 24) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 15) |
| **Subcategory** | Document ingestion and extraction |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Apache Software Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/apache/tika) · [Documentation](https://tika.apache.org/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 87/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material; note that Tika bundles many third-party parsers whose own notices are aggregated in NOTICE.txt and must be reproduced if you redistribute. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Operating cost is a JVM service: 2-4GB RAM per tika-server instance plus CPU proportional to corpus size; OCR, if enabled through Tesseract, dominates compute. Infrastructure estimate only, assuming self-hosted containers.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/apache/tika/blob/main/LICENSE.txt
- https://github.com/apache/tika
- https://tika.apache.org/

---

## 1. Purpose

One API over roughly 1,400 file formats that detects type, extracts text and returns metadata, available as a Java library, a REST server (tika-server) and a CLI.

## Journalism / investigative use case

The format-coverage backbone of leak processing: a single call handles PDFs, legacy Office, RTF, Outlook PST/MSG, archives and images, and the metadata it returns (authors, creation timestamps, producing software, revision history) is frequently the story itself — as it was in document-provenance work on leaked memos.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Format breadth no other single component matches, including the legacy and email formats that dominate real leaks and that modern Python-first parsers handle badly
- Returns metadata as a first-class output, not an afterthought — critical for provenance questions about who made a document and when
- Battle-tested as the extraction layer inside ICIJ extract, Datashare and the Aleph/OpenAleph ingest path, so your pipeline inherits a well-trodden route
- Stable, versioned ASF releases with a long compatibility record, so pinning a version is realistic

## 5. Cons

- Extraction only: no layout model, no table structure, no reading-order reconstruction — a two-column scanned report comes out interleaved and you need Surya/Docling-class tooling on top
- Parsing untrusted files in-process is a genuine security risk (parser CVEs are a recurring class); you must run tika-server sandboxed, which is extra architecture
- JVM footprint and startup cost make it awkward inside lightweight Python workers; most teams end up running it as a service
- No 'latest release' object exposed on GitHub (ASF distributes via dist.apache.org and git tags), so dependency tooling needs manual version tracking

## 6. Feedback (documented)

No direct user reports collected. Documented deployment evidence is strong and verifiable from source: ICIJ extract and Datashare both declare Tika as the extraction dependency, which is a credible production signal at terabyte scale.

## 7. Assessment

I would treat Tika as near-mandatory infrastructure rather than a choice, but always behind a sandbox. For your work the decisive property is that it is the only component that will not silently drop the ten-year-old .doc or the PST mailbox in a dump. Pair it with Dangerzone for anything from an unknown source, and do not expect it to solve layout — that is a separate stage.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, 4,153 stars, 64 open issues (low for a project this size, indicating issues are processed). ASF release process with a 2.x/3.x line and a security reporting channel. The low open-issue count relative to breadth is the strongest maintenance signal here.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material; note that Tika bundles many third-party parsers whose own notices are aggregated in NOTICE.txt and must be reproduced if you redistribute.

**Licence evidence:** https://github.com/apache/tika/blob/main/LICENSE.txt

## 10. Costs

No software fee. Operating cost is a JVM service: 2-4GB RAM per tika-server instance plus CPU proportional to corpus size; OCR, if enabled through Tesseract, dominates compute. Infrastructure estimate only, assuming self-hosted containers.

## 11. Privacy and data flows

Fully local processing; no network calls in the extraction path. The material privacy caveat is the inverse of the usual one — Tika extracts metadata you may not want to republish, so pair it with mat2 or an explicit scrubbing step before any document goes out.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Unstructured](JAI-A1-10.md) (Python-native, narrower format coverage, licence caveats)
- [Docling](JAI-A2-12.md) for layout-aware parsing
- [libpff](JAI-A1-12.md) / libratom specifically for PST/email forensics

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/apache/tika
- https://tika.apache.org/
- https://github.com/apache/tika/blob/main/LICENSE.txt

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

← 62. [SimpleX Chat](SUR-B3-25.md) · 64. [faster-whisper](JAI-A2-17.md) →
