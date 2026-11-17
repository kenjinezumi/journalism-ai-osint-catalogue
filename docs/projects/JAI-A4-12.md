# FacTool

`JAI-A4-12` · **42/100** · overall rank 353 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 139) |
| **Segment** | A4 · Fact-checking support and media verification (rank 26) |
| **Subcategory** | LLM output factuality checking |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | GAIR-NLP (Shanghai Jiao Tong University) |
| **Maintenance** | Dormant |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/GAIR-NLP/factool) · [Documentation](https://github.com/GAIR-NLP/factool#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 1/5 · privacy 1/5 · usability 2/5 · licence+cost 3/5 → **weighted 42/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Framework for detecting factual errors in generated text across scenarios (knowledge-based QA, code, maths, scientific review) by extracting claims, collecting evidence and scoring factuality.

## Journalism / investigative use case

Auditing AI-generated or AI-assisted copy before publication — the practical question of whether a draft produced with model assistance contains invented facts — and as a reusable claim-extraction-plus-evidence-collection component inside a newsroom verification pipeline.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Framed honestly as error detection in generated text rather than adjudication of public claims, which is the correct and narrower problem
- Multi-scenario design (including code and maths) makes it useful for auditing a wider range of AI-assisted outputs than prose alone
- Apache-2.0 and architecturally clear, so the claim-extraction stage is reusable in isolation

## 5. Cons

- NOT local: requires an OpenAI API key and a search API (Serper or Google) for the knowledge-QA scenario, so submitted text, extracted claims and generated queries go to third parties
- Dormant: last push 2024-08-19, no releases or tags, 937 stars with 24 open issues — initial interest that did not sustain maintenance
- Outputs are probabilistic factuality signals for triage, not conclusive verification; the paper's own framing is error detection, which users routinely over-read
- Tied to specific providers, so substituting a self-hosted model requires code changes

## 6. Feedback (documented)

No individual user reports verified. Documented: the required OpenAI and search API keys stated in the README; no activity since August 2024; 937 stars with 24 open issues.

## 7. Assessment

The use case — checking AI-assisted copy for invented facts — is one your newsroom will genuinely need as model-assisted drafting spreads. But this implementation is dormant and routes your unpublished copy through OpenAI, which is the wrong trade for a newsroom. I would implement the same check internally: extract claims with a self-hosted model, verify against your own document archive and a controlled search path, and keep the draft inside the building. Keep FacTool as a design reference.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-08-19, no releases, no tags, 937 stars, 24 open issues. Over two years inactive with an open backlog.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a — orchestrates hosted LLM APIs.

**Restrictions:** Code permissive; third-party API terms govern actual use.

**Licence evidence:** https://github.com/GAIR-NLP/factool/blob/main/LICENSE

## 10. Costs

Software free; operation requires paid OpenAI and search API keys (rates not verified here). Per-use cost scales with document length.

## 11. Privacy and data flows

NOT local — submitted text, extracted claims and generated search queries go to the configured LLM provider and search API. Unsuitable for unpublished copy about sensitive subjects.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Requires hosted LLM and search APIs
- Dormant since August 2024

## 13. Alternatives

- A self-hosted LLM performing claim extraction, with verification against your own archive
- Loki for a similar pipeline — equally dormant and equally hosted-API dependent
- Editorial process: a second human reading the draft against sources, which remains the reliable control

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/GAIR-NLP/factool
- https://github.com/GAIR-NLP/factool/blob/main/LICENSE

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

← 352. [Fetch (Meedan ClaimReview aggregator)](JAI-A4-03.md) · 354. [FaceForensics++](JAI-A4-26.md) →
