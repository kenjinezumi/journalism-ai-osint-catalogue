# FaceForensics++

`JAI-A4-26` · **42/100** · overall rank 354 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 140) |
| **Segment** | A4 · Fact-checking support and media verification (rank 27) |
| **Subcategory** | Deepfake detection dataset |
| **Type** | dataset |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | Technical University of Munich (ondyari) |
| **Maintenance** | Dormant |
| **Licence** | MIT (code); data under the separate 'FaceForensics Terms of Use' research agreement — not an SPDX open licence |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ondyari/FaceForensics) · [Documentation](https://github.com/ondyari/FaceForensics#readme) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 1/5 · privacy 3/5 · usability 2/5 · licence+cost 1/5 → **weighted 42/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Large dataset of manipulated face videos produced with several face-swap and reenactment methods at multiple compression levels, plus baseline detection code.

## Journalism / investigative use case

The canonical reference corpus behind most published face-swap detectors — useful to a newsroom's technical partner for sanity-checking any vendor-pitched detector, and to reporters as the citation for why detector accuracy figures in press materials should be distrusted.

## 2. Audience

engineer, specialist investigator

## 3. Project type

dataset · bucket `source-available-restricted`

## 4. Pros

- The reference dataset for the whole subfield, so understanding it is understanding what published detector numbers actually mean
- Multiple compression levels included, which is what allows honest measurement of the degradation that destroys real-world detection
- MIT code licence for the baseline implementations

## 5. Cons

- Data is released under the separate 'FaceForensics Terms of Use' — a research-oriented PDF agreement, not an SPDX open licence — and access requires completing a Google Form for approval, so it is not freely usable infrastructure
- Dated relative to current generators: it predates modern diffusion and audio-driven video synthesis, so a detector trained only on FF++ transfers poorly to 2024-2026 in-the-wild fakes. Any detector claiming high FF++ accuracy has told you almost nothing
- Dormant: last push 2022-12-08, 98 open issues against 2,804 stars
- The access flow routes through a Google Form and the authors' email, which discloses your organisation's interest

## 6. Feedback (documented)

No individual user reports verified. Documented: the separate FaceForensics Terms of Use (research-oriented agreement, not SPDX) and the Google Form access requirement; last push 2022-12-08; 2,804 stars with 98 open issues.

## 7. Assessment

Reference only, and specifically useful as a rhetorical instrument: when a vendor cites FF++ performance, the correct response is that FF++ predates the generators in use today. For your profile there is no reason to obtain the dataset unless you are training detectors, which I would not recommend a newsroom do. The dataset's real contribution to your work is the argument it supports about detector limits.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2022-12-08, no releases, SPDX NOASSERTION, 2,804 stars, 98 open issues. Four years inactive with a large backlog. The dataset itself is static, so dormancy mainly affects the baseline code.

## 9. Licensing

**Licence:** MIT (code); data under the separate 'FaceForensics Terms of Use' research agreement — not an SPDX open licence _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** FaceForensics Terms of Use (research-oriented PDF agreement, approval required).

**Restrictions:** Dataset access is gated and governed by a research-use agreement. Not usable as commercial infrastructure; redistribution is prohibited. Terms must be read before any use.

**Licence evidence:** https://github.com/ondyari/FaceForensics

## 10. Costs

No fee. Access requires a Google Form application and approval. Large download; GPU for any training. Estimate.

## 11. Privacy and data flows

The dataset request flows through a Google Form and the authors' email, disclosing your organisation's interest; the download script pulls from the project's servers. Your own case material is not involved.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Gated research-use dataset agreement — not usable as commercial infrastructure
- Predates current generative models, limiting relevance

## 13. Alternatives

- [Deepfake-Eval-2024](JAI-A4-31.md) for in-the-wild evaluation data closer to current conditions
- [DeepfakeBench](JAI-A4-25.md) for a unified evaluation framework — non-commercial licence
- Not training detectors at all, which is my recommendation for a newsroom

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/ondyari/FaceForensics

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

← 353. [FacTool](JAI-A4-12.md) · 355. [Whoogle Search](OSINT-C1-04.md) →
