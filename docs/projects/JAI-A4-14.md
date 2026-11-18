# CooRnet

`JAI-A4-14` · **36/100** · overall rank 358 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 143) |
| **Segment** | A4 · Fact-checking support and media verification (rank 30) |
| **Subcategory** | Coordinated behaviour detection |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Fabio Giglietto |
| **Maintenance** | Archived or discontinued |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/fabiogiglietto/CooRnet) · [Documentation](https://github.com/fabiogiglietto/CooRnet#readme) |

**Scores** — relevance 2/5 · capability 1/5 · maintenance 0/5 · privacy 2/5 · usability 2/5 · licence+cost 5/5 → **weighted 36/100**

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
| **Restrictions** | None, but the code is frozen and inoperable. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Not operable — CrowdTangle, its required data source, is shut down.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/fabiogiglietto/CooRnet/blob/master/LICENSE
- https://github.com/fabiogiglietto/CooRnet

---

## 1. Purpose

R package that detected coordinated link-sharing behaviour across Facebook and Instagram using CrowdTangle data, producing co-sharing networks of pages and groups.

## Journalism / investigative use case

Historically the standard tool for showing that a false claim was amplified by a coordinated page network; now relevant mainly for reproducing or auditing published investigations that used it.

## 2. Audience

specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Established the methodology that CooRTweet and successors implement, and remains the citation for a body of published investigations
- MIT licensed with a clean reference implementation of coordinated link-sharing detection
- Zero open issues at archival — it was a finished, working tool for its data source

## 5. Cons

- ARCHIVED and functionally dead: GitHub API confirms archived=true with last push 2024-08-14, which coincides with CrowdTangle's shutdown — its only data source no longer exists
- Even with a data substitute, the package's assumptions are CrowdTangle-shaped (page/group entities, specific field names)
- Facebook/Instagram only, so it never covered the platforms where much coordination now occurs
- Its fate is a general warning: tools built on a single proprietary platform API inherit that API's lifespan

## 6. Feedback (documented)

No individual user reports verified. The documented decisive facts: archived=true per the GitHub API on 2026-11-17, and the alignment of its final push (2024-08-14) with the discontinuation of the CrowdTangle data source it depended on.

## 7. Assessment

Reference only, and a useful cautionary case for your planning: the single most consequential dependency in social-media research is not the library but the data source, and proprietary research APIs have been withdrawn repeatedly. Use CooRTweet, which is data-source agnostic, and design any monitoring you build so the collection layer can be replaced without rewriting the analysis.

## 8. Maintenance

**Archived or discontinued** — GitHub API 2026-11-17: archived=true, pushed_at 2024-08-14, no releases, 75 stars, 0 open issues. Archived by the maintainer; the underlying CrowdTangle API was discontinued, so the data layer is gone as well as the code being frozen.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, but the code is frozen and inoperable.

**Licence evidence:** https://github.com/fabiogiglietto/CooRnet/blob/master/LICENSE

## 10. Costs

No fee. Not operable — CrowdTangle, its required data source, is shut down.

## 11. Privacy and data flows

Historically sent URL lists to Meta's CrowdTangle API; now inoperable.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Archived, and its sole data source (CrowdTangle) was discontinued

## 13. Alternatives

- [CooRTweet](JAI-A4-13.md) — the recommended, data-source-agnostic successor
- 4CAT for collection plus network analysis on platforms that remain accessible
- Published methodology papers for citing the method without running the code

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/fabiogiglietto/CooRnet
- https://github.com/fabiogiglietto/CooRnet/blob/master/LICENSE

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

← 357. [AVeriTeC dataset and baseline](JAI-A4-07.md) · 359. [pagodo](OSINT-C1-07.md) →
