# ClaimBuster-Spotter

`JAI-A4-05` · **51/100** · overall rank 342 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 131) |
| **Segment** | A4 · Fact-checking support and media verification (rank 18) |
| **Subcategory** | Check-worthiness detection |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | University of Texas at Arlington (utaresearch) |
| **Maintenance** | Dormant |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/utaresearch/claimbuster-spotter) · [Documentation](https://idir.uta.edu/claimbuster/) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 1/5 · privacy 4/5 · usability 2/5 · licence+cost 3/5 → **weighted 51/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | NOT verified — trained checkpoints are not clearly licensed in-repo; the hosted ClaimBuster API has its own terms. |
| **Restrictions** | GPL-3.0 on code limits embedding in proprietary newsroom tooling. Checkpoint licensing is unresolved, so redistribution of trained weights is legally unclear. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. TensorFlow-era dependencies make the install awkward; CPU or modest GPU sufficient. ClaimBuster datasets requested separately.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/utaresearch/claimbuster-spotter/blob/master/LICENSE
- https://github.com/utaresearch/claimbuster-spotter
- https://idir.uta.edu/claimbuster/

---

## 1. Purpose

Transformer-based model that scores sentences for check-worthiness — how much a statement looks like a factual claim a fact-checker would want to verify.

## Journalism / investigative use case

Automatically rank sentences from debate transcripts, speeches or long interviews by check-worthiness so a fact-checking desk can prioritise which statements to verify under deadline — triage, when a two-hour speech produces 800 sentences and the desk has three hours.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Addresses a real deadline problem — prioritisation, not adjudication — and is honest about being a ranking signal
- Can run locally with no third-party calls for the models in this repository, unlike the hosted claimbuster.org API
- GPL-3.0 code with published research behind the approach, so the method is citable in a methodology note

## 5. Cons

- Dormant: last push 2023-11-29, no releases or tags, 87 stars with 26 open issues — a research artefact that has stopped moving
- Check-worthiness scores are probabilistic prioritisation signals, not judgements of truth: a high score means 'worth checking', not 'false', and this is routinely misread
- Trained predominantly on US political discourse, so transfer to other political cultures and languages is unevidenced
- Trained checkpoints are not clearly licensed in-repo, and the hosted ClaimBuster API has separate terms — using the hosted API sends your text to the university's service

## 6. Feedback (documented)

No individual user reports verified. Documented: the dormancy (no push since November 2023), the GPL-3.0 code licence, and the unclear checkpoint licensing. The ClaimBuster project itself is well cited in the automated-fact-checking literature, which is research credibility rather than deployment evidence.

## 7. Assessment

Not something I would deploy in 2026: dormant, US-centric, and the capability can be reproduced with a modern instruction-tuned model and a clear prompt, with better multilingual coverage. Its catalogue value is conceptual — check-worthiness as a distinct, modest, well-scoped task is the right way to apply automation to fact-checking, as opposed to asking a model for verdicts. Keep as reference.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2023-11-29, no releases, no tags, 87 stars, 26 open issues. Three years without activity and an open backlog; no deprecation notice. Dormant rather than archived.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** NOT verified — trained checkpoints are not clearly licensed in-repo; the hosted ClaimBuster API has its own terms.

**Restrictions:** GPL-3.0 on code limits embedding in proprietary newsroom tooling. Checkpoint licensing is unresolved, so redistribution of trained weights is legally unclear.

**Licence evidence:** https://github.com/utaresearch/claimbuster-spotter/blob/master/LICENSE

## 10. Costs

No fee. TensorFlow-era dependencies make the install awkward; CPU or modest GPU sufficient. ClaimBuster datasets requested separately.

## 11. Privacy and data flows

Runs locally with no third-party calls for the in-repo models. Using claimbuster.org's hosted API instead sends your text to that service — avoid for unpublished material.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Dormant since 2023; checkpoint licensing unresolved

## 13. Alternatives

- A self-hosted instruction-tuned LLM with an explicit check-worthiness prompt, which covers more languages
- Loki or FacTool for claim extraction — but note both default to hosted LLM APIs
- Manual triage by an editor, which remains competitive for a single speech

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/utaresearch/claimbuster-spotter
- https://idir.uta.edu/claimbuster/
- https://github.com/utaresearch/claimbuster-spotter/blob/master/LICENSE

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

← 341. [X-FACT](JAI-A4-08.md) · 343. [SelfBlendedImages (SBI)](JAI-A4-27.md) →
