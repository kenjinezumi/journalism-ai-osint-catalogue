# Paperless-ngx

`JAI-A2-38` · **84/100** · overall rank 111 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 46) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 26) |
| **Subcategory** | Document management |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | paperless-ngx community |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/paperless-ngx/paperless-ngx) · [Documentation](https://docs.paperless-ngx.com/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a — the tagging classifier is trained locally on your own documents. |
| **Restrictions** | GPL-3.0: distribution of a modified version obliges source release. Internal newsroom use is unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: one small VM or NAS container with PostgreSQL or SQLite plus Redis; storage proportional to document volume. Among the cheapest self-hosted options here, with low operating effort. Assumptions: Docker Compose deployment, tens of thousands of documents.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/paperless-ngx/paperless-ngx/blob/main/LICENSE
- https://github.com/paperless-ngx/paperless-ngx
- https://docs.paperless-ngx.com/

---

## 1. Purpose

Self-hosted document-management system that ingests scans and PDFs, OCRs them via the OCRmyPDF/Tesseract toolchain, applies machine-learning-assisted tagging and correspondent detection, and provides full-text search.

## Journalism / investigative use case

A practical self-hosted archive for a moderate corpus of source documents where reporters need reliable OCR search plus tagging without engineering support — for example a bureau's accumulated FOIA responses, court filings and leaked paperwork across years of reporting.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Genuinely turnkey: a documented Docker Compose deployment gets a working searchable archive in an afternoon, which is unmatched among self-hosted document systems here
- Automatic tagging and correspondent inference reduce the filing discipline required from reporters — the reason archives actually stay organised
- Outstanding maintenance profile: release v3.5.0 on 2026-11-17 with only 8 open issues against 48,191 stars
- Fully local with no third-party calls, and a large non-journalism user base that keeps it robust and well documented

## 5. Cons

- Architected around personal and office document volumes, not million-document leak triage — it will slow and become unpleasant well before leak scale
- No clustering, topic discovery or entity extraction, so it organises documents but does not help you find the story inside them
- GPL-3.0 affects redistribution inside proprietary tooling (irrelevant for internal use)
- Its document model assumes a tidy archive of discrete documents; messy dumps with duplicates and fragments fit poorly without preprocessing

## 6. Feedback (documented)

No individual user reports verified. The checkable maintenance evidence is exceptional: 48,191 stars with 8 open issues and a same-day release (2026-11-17) indicates an unusually disciplined maintainer team. No journalism-specific deployment verified; the user base is predominantly self-hosting enthusiasts.

## 7. Assessment

The right answer for the newsroom-archive problem that OpenAleph and Datashare over-serve: if you need somewhere to put documents permanently and find them later, this costs a fraction of the operational effort. For your profile I would run it as the standing bureau archive and reserve Datashare/OpenAleph for individual investigations with a document dump. Do not expect it to do analysis.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.5.0 (2026-11-17), 48,191 stars, 8 open issues. Same-day release and a near-empty tracker at very large scale — the strongest issue-throughput evidence in the catalogue.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a — the tagging classifier is trained locally on your own documents.

**Restrictions:** GPL-3.0: distribution of a modified version obliges source release. Internal newsroom use is unaffected.

**Licence evidence:** https://github.com/paperless-ngx/paperless-ngx/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure estimate: one small VM or NAS container with PostgreSQL or SQLite plus Redis; storage proportional to document volume. Among the cheapest self-hosted options here, with low operating effort. Assumptions: Docker Compose deployment, tens of thousands of documents.

## 11. Privacy and data flows

Fully local, no third-party calls, classifier trained in place. Residual considerations are ordinary server hygiene: backups contain everything, and the web UI needs authentication and TLS.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ICIJ Datashare](JAI-A2-23.md) for investigation-scale document sets
- [Uwazi](OSINT-C3-05.md) for public-facing collections
- Mayan EDMS as an alternative self-hosted DMS with a different feature balance

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/paperless-ngx/paperless-ngx
- https://docs.paperless-ngx.com/
- https://github.com/paperless-ngx/paperless-ngx/blob/main/LICENSE

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

← 110. [monolith](OSINT-C1-39.md) · 112. [SunCalc](OSINT-C2-18.md) →
