# CooRTweet

`JAI-A4-13` · **77/100** · overall rank 188 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 76) |
| **Segment** | A4 · Fact-checking support and media verification (rank 4) |
| **Subcategory** | Coordinated behaviour detection |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Nicola Righetti and collaborators |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (project-stated; GitHub API reports SPDX NOASSERTION) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/nicolarighetti/CooRTweet) · [Documentation](https://github.com/nicolarighetti/CooRTweet#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 77/100**

---

## 1. Purpose

R package that detects coordinated sharing behaviour in social-media data by finding accounts repeatedly posting the same content within a short time window, and builds the resulting co-sharing network.

## Journalism / investigative use case

Investigating whether a claim's apparent virality is organic or amplified: identify clusters of accounts pushing the same content in lockstep, which is a standard evidentiary step in disinformation-campaign reporting and one that holds up editorially when the method is stated.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Platform-agnostic by design: analysis is fully local on data you already hold and the package does not call platform APIs — which is why it survived CrowdTangle's shutdown while CooRnet did not
- Implements a published, citable method, so a story can state the parameters (time window, repetition threshold) and be reproduced
- Active maintenance (pushed 2026-11-08) under MIT, with a tiny issue backlog
- Outputs a network you can inspect in Gephi or igraph, making the finding visual and checkable rather than a single statistic

## 5. Cons

- Detects statistical co-occurrence, not intent — a cluster may be a campaign, a fan community, a newsletter or an artefact of the sampling window, and the method cannot distinguish these
- You must supply the social-media data yourself, which after the platform API withdrawals is now the hard part of the whole workflow
- Results are highly sensitive to the chosen time window and repetition threshold; different defensible parameters produce different networks, so parameter choices must be published
- R-based, which is a mismatch if your stack is Python/TypeScript, and GitHub reports NOASSERTION for the licence although the project states MIT

## 6. Feedback (documented)

No individual user reports verified. Documented: active commits through 2026-11-08 with 57 stars and 1 open issue; the method derives from published coordinated-behaviour research. CooRnet's archival (same research area, CrowdTangle-dependent) is the instructive contrast and is verified in this catalogue.

## 7. Assessment

The right tool for this analysis today, precisely because it is data-source agnostic. For your profile the binding constraint is not the tool but data acquisition — budget your effort there. Two editorial disciplines are non-negotiable: publish the parameters, and corroborate any cluster with non-statistical evidence (account creation patterns, shared infrastructure, content provenance) before characterising it as coordinated.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-08, no release objects, 57 stars, 1 open issue. Current commits from an active academic maintainer; note GitHub reports SPDX NOASSERTION while the project states MIT, so the licence label here rests on the project's own declaration.

## 9. Licensing

**Licence:** MIT (project-stated; GitHub API reports SPDX NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** None material, but the SPDX mismatch means confirm the LICENSE file before redistributing.

**Licence evidence:** https://github.com/nicolarighetti/CooRTweet

## 10. Costs

No fee. Runs on a laptop in R. The real cost is obtaining social-media data — which after platform API restrictions may require paid research access, scraping (with its own legal and operational risk), or partnership with an academic data holder. Not priced here.

## 11. Privacy and data flows

Analysis is fully local on data you already hold; the package makes no platform API calls. Data acquisition is the step with privacy and legal implications, not the analysis.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [CooRnet](JAI-A4-14.md) — archived, reference only
- 4CAT plus Zeeschuimer for data collection to feed this analysis
- [Gephi](OSINT-C3-33.md) or igraph for visualising and interrogating the resulting network

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/nicolarighetti/CooRTweet

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 187. [Media Cloud API client](JAI-A1-14.md) · 189. [Zoekplaatje](OSINT-C1-11.md) →
