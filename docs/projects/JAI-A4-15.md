# Full Fact AI Trust Benchmark

`JAI-A4-15` · **58/100** · overall rank 334 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 127) |
| **Segment** | A4 · Fact-checking support and media verification (rank 15) |
| **Subcategory** | AI evaluation for fact-checking |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | Full Fact |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/FullFact/benchmark-public-release) · [Documentation](https://fullfact.org/) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 3/5 · privacy 3/5 · usability 2/5 · licence+cost 5/5 → **weighted 58/100**

---

## 1. Purpose

Benchmark and evaluation harness, authored by a fact-checking organisation, for assessing whether AI assistants behave acceptably on fact-checking-adjacent tasks.

## Journalism / investigative use case

Gives a newsroom a practitioner-authored rather than vendor-authored basis for deciding whether an AI assistant is fit to be placed near editorial fact-checking work — the question editors actually ask when a tool is pitched to them.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Authored by working fact-checkers, so the evaluation criteria reflect editorial requirements rather than benchmark convenience — a genuinely different and useful perspective
- Apache-2.0 and recently active (pushed 2026-11-03), so it reflects current model behaviour rather than a 2023 snapshot
- Evaluates third-party models and distributes none, so there is no model-licence complication

## 5. Cons

- Very low adoption signal (3 stars, 0 open issues) and early-stage: this is a published artefact rather than an established standard, and its results have not been widely replicated
- A benchmark, not a fact-checking tool — it tells you about a model, not about a claim
- Scores are probabilistic snapshots of specific model versions and go stale quickly as providers update models silently
- Running it sends benchmark prompts to the model providers under evaluation, which is inherent to the design but means your evaluation activity is visible to vendors

## 6. Feedback (documented)

No individual user reports verified — the 3-star count means there is effectively no community signal to report, which I note rather than inflate. Full Fact's institutional standing in fact-checking is well established; this specific artefact is new.

## 7. Assessment

Worth knowing about disproportionately to its adoption, because it is the only practitioner-authored evaluation in this catalogue and it answers a question your editors will ask. For your profile I would use its criteria as a checklist when assessing an AI tool rather than necessarily running the harness, and re-run or re-read it whenever you change model providers. Treat the specific scores as perishable.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-03, no releases, 3 stars, 0 open issues. Recent activity from an institutional maintainer; too new and too small to classify as actively maintained with confidence, and clearly not declining.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a — evaluates third-party models and distributes none.

**Restrictions:** None.

**Licence evidence:** https://github.com/FullFact/benchmark-public-release/blob/main/LICENSE

## 10. Costs

No software fee. Running it incurs the API charges of whichever models you benchmark (rates vary by provider and were not verified here). Cost is proportional to the number of models and prompts.

## 11. Privacy and data flows

Benchmark prompts are sent to the model providers under evaluation — inherent to the design. No sensitive material need be involved if you use the supplied prompts.

## 12. Verdict

**Reference only**

## 13. Alternatives

- AVeriTeC's evaluation design for a research-grade methodology — licence unconfirmed
- Building a newsroom-specific evaluation set from your own published fact-checks
- FEVER's annotation platform for constructing that set

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/FullFact/benchmark-public-release
- https://github.com/FullFact/benchmark-public-release/blob/main/LICENSE

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

← 333. [AASIST](JAI-A4-29.md) · 335. [Google Fact Check Tools API](JAI-A4-16.md) →
