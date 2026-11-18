# FollowTheMoney (alephdata 3.x line)

`JAI-A2-18` · **77/100** · overall rank 186 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 74) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 44) |
| **Subcategory** | Data model and ontology |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | originally OCCRP/Aleph; active development moved to OpenSanctions |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/alephdata/followthemoney) · [Documentation](https://followthemoney.tech/) |
| **Also known as** | FtM |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 2/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Staff effort |
| **Cost conditions** | Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Cost is engineer time writing and maintaining mappings — realistically days per complex source dataset. No paid dependencies.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/alephdata/followthemoney/blob/main/LICENSE
- https://github.com/alephdata/followthemoney
- https://github.com/opensanctions/followthemoney
- https://followthemoney.tech/
- `../sources/evidence/leads.md`

---

## 1. Purpose

Entity schema and data model for investigative data — Person, Company, Ownership, Payment, Membership and related types — with validation, mapping from tabular sources, and export helpers.

## Journalism / investigative use case

The shared vocabulary that makes cross-dataset linking possible: map a leak, a corporate registry and a sanctions list into the same Person/Company/Ownership schema so the records can actually be compared rather than merely co-located. Aleph, OpenAleph, yente and nomenklatura all build on it.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Solves the modelling problem that otherwise blocks every cross-dataset investigation, and does so with a vocabulary designed by investigative practitioners
- Ecosystem effect: adopting FtM gives you free interoperability with OpenAleph, yente, nomenklatura and OpenSanctions data
- MIT and pure Python — easy to adopt incrementally for a single dataset without buying into a platform
- Well-documented schema reference at followthemoney.tech with worked mapping examples

## 5. Cons

- THIS repository is the stale 3.x line: pushed 2026-02-28, latest release v3.8.2 (2025-03-24). Active 4.x development is at opensanctions/followthemoney (v4.11.3, 2026-11-07) and the old URL does NOT redirect — anyone pinning from alephdata is on an abandoned major version
- It is an ontology, not a tool: mapping messy real data into it is substantial, unglamorous work that teams consistently underestimate
- The schema is opinionated towards financial-crime and corporate investigation; fitting other domains (health records, environmental data) requires compromise
- Governance churn across the alephdata/OpenSanctions split is itself a planning risk for a long-lived archive

## 6. Feedback (documented)

No individual user reports. The decisive documented finding from this session's verification: two live repositories exist with the same name and no redirect between them, with a two-major-version gap (3.8.2 versus 4.11.3). That is a concrete dependency trap, verified via the GitHub API on 2026-11-17 and recorded in sources/evidence/leads.md.

## 7. Assessment

Adopt the model, but from the OpenSanctions repository, not this one. I am cataloguing the alephdata repo separately precisely because it is the URL most documentation and search results still point at, and following it silently puts you on a dead 3.x branch. For your work the ontology is worth the mapping effort if you expect to combine datasets more than once; for a single one-off dataset it is overhead.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-02-28, latest release v3.8.2 (2025-03-24), latest tag v3.8.4, 309 stars, 69 open issues. Nearly nine months without a push and over a year without a release, while the same-named OpenSanctions repository released v4.11.3 on 2026-11-07. Declining rather than archived because no deprecation notice is posted — which is itself the hazard.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/alephdata/followthemoney/blob/main/LICENSE

## 10. Costs

No fee. Cost is engineer time writing and maintaining mappings — realistically days per complex source dataset. No paid dependencies.

## 11. Privacy and data flows

Local library only; no network calls, no telemetry.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- This repository is a stale major version with no deprecation notice; development moved to opensanctions/followthemoney and the old URL does not redirect

## 13. Alternatives

- opensanctions/followthemoney — the actively maintained 4.x line, use this instead
- [nomenklatura](JAI-A2-30.md) and rigour from the same ecosystem for resolution and normalisation
- Plain schema design plus Splink if you only ever link two datasets

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/alephdata/followthemoney
- https://github.com/opensanctions/followthemoney
- https://followthemoney.tech/
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

← 185. [Delta Chat / chatmail core](SUR-B3-26.md) · 187. [Media Cloud API client](JAI-A1-14.md) →
