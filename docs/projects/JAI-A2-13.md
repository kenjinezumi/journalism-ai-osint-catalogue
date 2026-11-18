# DocumentCloud

`JAI-A2-13` · **74/100** · overall rank 221 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 90) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 48) |
| **Subcategory** | Document publishing platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | MuckRock |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MuckRock/documentcloud) · [Documentation](https://www.documentcloud.org/help/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 2/5 · usability 4/5 · licence+cost 4/5 → **weighted 74/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the platform. Cloud OCR add-ons operate under the respective vendor's terms. |
| **Restrictions** | AGPL-3.0 network copyleft: if you modify DocumentCloud and offer it to users over a network, you must release your modified source. Material if you intend a customised newsroom deployment. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Hosted DocumentCloud access has historically been free to verified journalists with paid organisational tiers; current prices were NOT verified in this survey — treat as not publicly verified here and check with MuckRock. Cloud OCR add-ons incur the underlying vendor's per-page charges (not priced here). Self-hosting costs are Django app servers, object storage and a search index, plus substantial undocumented-deployment engineering effort.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/MuckRock/documentcloud/blob/master/LICENSE
- https://github.com/MuckRock/documentcloud
- https://www.documentcloud.org/help/

> **Unresolved:** the price is not established by these records — this is not a statement that it is free.

---

## 1. Purpose

Hosted and open-source platform for uploading, OCR-ing, searching, annotating and embedding primary-source documents, with an Add-On framework for automation.

## Journalism / investigative use case

Where processed documents go to become public evidence: a reporter uploads a 900-page FOIA release, annotates the three paragraphs that matter, and embeds the viewer in the story so readers can read the original. The Add-On model also automates alerts when new documents matching a query appear.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Purpose-built for journalism by a journalism organisation — annotation, embedding and public-document norms are first-class, not adapted from enterprise DMS
- The Add-On framework (and Klaxon Cloud as an add-on) lets a newsroom automate monitoring and extraction without running infrastructure
- AGPL-3.0 with a real public repository, so the self-hosting option legally exists even if it is not turnkey
- Long institutional history (originally IRE/ProPublica lineage, now MuckRock) means the hosted service is unlikely to vanish abruptly

## 5. Cons

- Self-hosting is not a documented turnkey path: Django plus object storage plus a search index, with little deployment documentation — the 54 stars and 56 open issues reflect a repo that exists more for transparency than for third-party operators
- The best-performing OCR add-ons are third-party cloud APIs (Google Cloud Vision, Azure Document Intelligence class services), so the accurate path sends your pages to a vendor
- The hosted platform stores documents on MuckRock infrastructure under its terms — a third-party custody decision that is unacceptable for unpublished source material in a hostile-state threat model
- No GitHub release objects; versioning is informal (latest tag is 'staging-lambda-test'), making a self-hosted deployment hard to pin

## 6. Feedback (documented)

No individual user reports verified. Documented signals: an active hosted service with public newsroom document collections, against a small code repository (54 stars) with informal tagging. The OCR add-on architecture routing to commercial cloud OCR is documented in the add-on repositories.

## 7. Assessment

Use the hosted service for documents you have decided to publish; do not use it as your working archive for unpublished material, and do not plan to self-host it unless you are prepared for undocumented Django operations. For your profile the clean division is: OpenAleph or Datashare inside the perimeter for analysis, DocumentCloud at the end for publication and reader-facing embedding. The OCR add-on question has a local answer — OCR with OCRmyPDF before upload rather than using a cloud add-on.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, no release objects, latest tag 'staging-lambda-test', 54 stars, 56 open issues. The hosted service is the primary artefact and is live; the repository is maintained alongside it but is not packaged for external deployment. Active, with the caveat that activity is service-driven rather than release-driven.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a for the platform. Cloud OCR add-ons operate under the respective vendor's terms.

**Restrictions:** AGPL-3.0 network copyleft: if you modify DocumentCloud and offer it to users over a network, you must release your modified source. Material if you intend a customised newsroom deployment.

**Licence evidence:** https://github.com/MuckRock/documentcloud/blob/master/LICENSE

## 10. Costs

Hosted DocumentCloud access has historically been free to verified journalists with paid organisational tiers; current prices were NOT verified in this survey — treat as not publicly verified here and check with MuckRock. Cloud OCR add-ons incur the underlying vendor's per-page charges (not priced here). Self-hosting costs are Django app servers, object storage and a search index, plus substantial undocumented-deployment engineering effort.

## 11. Privacy and data flows

The hosted service places documents in MuckRock's custody — appropriate for material destined for publication, not for unpublished source documents. Documents can be kept private within the platform, but that is a policy control on someone else's infrastructure, not a technical guarantee under your control. The high-accuracy OCR add-ons send page images to third-party cloud vendors.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Hosted custody of documents is unsuitable for unpublished sensitive material in a hostile-state threat model

## 13. Alternatives

- [OpenAleph](JAI-A2-35.md) or ICIJ Datashare for in-perimeter analysis
- [Uwazi](OSINT-C3-05.md) for a public-facing human-rights document collection you host yourself
- [Paperless-ngx](JAI-A2-38.md) for a modest self-hosted internal archive

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/MuckRock/documentcloud
- https://www.documentcloud.org/help/
- https://github.com/MuckRock/documentcloud/blob/master/LICENSE

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

← 220. [warn-scraper](JAI-A1-30.md) · 222. [MuckRock](OSINT-C3-15.md) →
