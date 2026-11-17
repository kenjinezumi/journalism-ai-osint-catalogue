# Fetch (Meedan ClaimReview aggregator)

`JAI-A4-03` · **43/100** · overall rank 352 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 138) |
| **Segment** | A4 · Fact-checking support and media verification (rank 25) |
| **Subcategory** | Fact-check feed aggregation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Meedan |
| **Maintenance** | Archived or discontinued |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/meedan/fetch) · [Documentation](https://github.com/meedan/fetch#readme) |

**Scores** — relevance 2/5 · capability 2/5 · maintenance 0/5 · privacy 3/5 · usability 2/5 · licence+cost 5/5 → **weighted 43/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Service that pulls fact-check outputs from heterogeneous publisher feeds and normalises them into ClaimReview-structured records for indexing.

## Journalism / investigative use case

Reference implementation for normalising fact-check feeds so a newsroom can query across many fact-checking organisations' outputs from one index — in principle letting a desk check 'has anyone already debunked this?' without visiting a dozen sites.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Addresses a genuine interoperability gap: fact-check publication formats are inconsistent and ClaimReview normalisation is the accepted fix
- MIT licensed with the ClaimReview mapping patterns readable in source — useful as documentation even if you do not run it
- Authored by an organisation deeply involved in fact-check interoperability standards

## 5. Cons

- ARCHIVED — GitHub API confirms archived=true, last push 2026-05-21. It is read-only and will receive no fixes
- Feed adapters for third-party sites rot quickly by nature; an archived adapter collection is close to worthless operationally
- Essentially no community (1 star, 9 open issues at archival)
- Fetches from third-party fact-checker sites, so your crawling pattern is visible to them

## 6. Feedback (documented)

No individual user reports. The decisive documented fact is the archival status, confirmed by the GitHub API on 2026-11-17 (archived=true). That makes all other assessment secondary.

## 7. Assessment

Reference only. Read it to understand ClaimReview normalisation patterns, then use the Google Fact Check Tools API or ClaimsKG for the actual lookup. For your profile the lesson generalises: feed-adapter collections are the most perishable category of software in this catalogue, and depending on an unmaintained one means silent coverage loss rather than visible failure.

## 8. Maintenance

**Archived or discontinued** — GitHub API 2026-11-17: archived=true, pushed_at 2026-05-21, latest tag v0.184.9, 1 star, 9 open issues. Archived by the maintainer — the strongest possible maintenance signal, and unambiguous.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, but the code is frozen.

**Licence evidence:** https://github.com/meedan/fetch/blob/master/LICENSE

## 10. Costs

No fee. Not worth operating.

## 11. Privacy and data flows

Fetches from third-party fact-checker sites and APIs; your crawling traffic is visible to them. No credentials required for most sources.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Archived by the maintainer — do not build on it

## 13. Alternatives

- [Google Fact Check Tools API](JAI-A4-16.md) for claim lookup (hosted, Google terms)
- [ClaimsKG extractor](JAI-A4-09.md) for building your own cross-organisation fact-check database — but note its own licence is unconfirmed
- [Meedan Check](JAI-A4-01.md), which supersedes this component operationally

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/meedan/fetch
- https://github.com/meedan/fetch/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |

---

← 351. [dorks_hunter](OSINT-C1-08.md) · 353. [FacTool](JAI-A4-12.md) →
