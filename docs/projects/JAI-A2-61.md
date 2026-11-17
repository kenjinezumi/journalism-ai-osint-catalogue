# yente

`JAI-A2-61` · **88/100** · overall rank 53 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 21) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 13) |
| **Subcategory** | Sanctions and PEP screening API |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenSanctions |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (code) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opensanctions/yente) · [Documentation](https://www.opensanctions.org/docs/yente/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 3/5 → **weighted 88/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Self-hostable entity-matching API that indexes OpenSanctions (or your own FollowTheMoney) data in Elasticsearch/OpenSearch and exposes search, match and OpenRefine-compatible reconciliation endpoints.

## Journalism / investigative use case

Screen a leaked client or shareholder list against sanctions and PEP data in bulk on your own infrastructure, then reconcile the same spreadsheet from OpenRefine — without the names ever leaving your network. That last property is the whole argument: using a hosted screening API would disclose your investigation's targets to a vendor.

## 2. Audience

engineer, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Solves a specific and serious operational-security problem: bulk screening without telling a third party who you are investigating
- OpenRefine-compatible reconciliation endpoint means an analyst can reconcile a spreadsheet against sanctions data entirely in-house — the fix for OpenRefine's one privacy flaw
- MIT licensed, actively released (v5.5.1, 2026-10-30), maintained by the organisation that produces the data
- Returns scored candidates with the matching features, so adjudication is informed rather than binary

## 5. Cons

- The code is MIT but the data it exists to serve is CC-BY-NC-4.0: commercial use of OpenSanctions data requires a paid licence (quote required), which directly affects a commercially operated newsroom
- Requires Elasticsearch or OpenSearch plus a bulk data load — real infrastructure, and the index must be refreshed as sanctions data changes
- Matching returns scored candidates that still need human adjudication; a high score is not a finding, and treating it as one risks defaming someone with a similar name
- Small project (184 stars, 49 open issues) tightly coupled to the OpenSanctions ecosystem

## 6. Feedback (documented)

No individual user reports verified. The documented licensing split, verified from the vendor's own licensing page in session 1 and reconfirmed this session: code MIT, data CC-BY-NC-4.0 with commercial use requiring a paid licence; Screening API sold as prepaid credit bundles, Screening Licence and Reseller/OEM quote-only (opensanctions.org/licensing, 2026-11-16).

## 7. Assessment

Adopt it specifically to keep screening in-house — the privacy argument is decisive and this is the only tool here that delivers it. Then resolve the data licence separately and in writing: if your outlet is commercially operated, 'we are journalism so it is non-commercial' is not a defensible reading of CC-BY-NC, and you should price the OpenSanctions commercial licence before building a workflow on it. Using the data for reporting leads versus building a paid product are different positions and should be decided explicitly.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v5.5.1 (2026-10-30), 184 stars, 49 open issues. Frequent releases tracking the OpenSanctions data pipeline; maintained by a commercial entity that depends on it.

## 9. Licensing

**Licence:** MIT (code) _(SPDX verified)_

**Model / data licence:** OpenSanctions data is CC-BY-NC-4.0; commercial use requires a paid licence (price not publicly listed — quote required).

**Restrictions:** The restriction is on the data, not the code. Commercial newsrooms cannot assume NGO-style non-commercial status. Loading your own FtM data instead avoids the issue entirely.

**Licence evidence:** https://www.opensanctions.org/licensing/

## 10. Costs

Software free. Infrastructure: Elasticsearch/OpenSearch node plus periodic bulk data loads — estimate one 8-16GB VM for a newsroom-scale index. Data licence for commercial use: quote required, not publicly listed (verified 2026-11-16). OpenSanctions also sells a hosted Screening API using prepaid credit bundles with free credits on signup.

## 11. Privacy and data flows

Queries stay local once the index is built — the key privacy win over hosted screening APIs, which see every name you check. The index data itself is licensed separately. Residual risk: the Elasticsearch index must not be exposed.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- OpenSanctions data is CC-BY-NC-4.0 — commercial-use licence required, price not publicly listed

## 13. Alternatives

- [nomenklatura](JAI-A2-30.md) for batch resolution rather than an API
- OpenSanctions hosted Screening API where in-house infrastructure is not viable — but it discloses your query targets
- Loading your own FollowTheMoney datasets into yente to avoid the data-licence question

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/opensanctions/yente
- https://www.opensanctions.org/docs/yente/
- https://www.opensanctions.org/licensing/
- `../sources/evidence/leads.md`

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

← 52. [Whisper](JAI-A2-58.md) · 54. [iLEAPP](SUR-B3-15.md) →
