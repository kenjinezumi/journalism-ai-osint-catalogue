# AVeriTeC dataset and baseline

`JAI-A4-07` · **36/100** · overall rank 357 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 142) |
| **Segment** | A4 · Fact-checking support and media verification (rank 29) |
| **Subcategory** | Fact-verification benchmark |
| **Type** | prototype |
| **Bucket** | `uncertain` |
| **Maintainer** | Michael Schlichtkrull and collaborators (academic) |
| **Maintenance** | Dormant |
| **Licence** | NOT CONFIRMED — no LICENSE/COPYING file in the repository root, GitHub licence API reports none, README has no licence section |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MichSchli/AVeriTeC) · [Documentation](https://fever.ai/dataset/averitec.html) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 1/5 · privacy 1/5 · usability 2/5 · licence+cost 1/5 → **weighted 36/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Benchmark of real-world claims checked by fact-checking organisations, modelling verification as question generation, question answering over open web evidence, and the production of a written justification.

## Journalism / investigative use case

The closest public benchmark to actual fact-checking practice: it models verification the way a fact-checker works — asking sub-questions, finding evidence for each, then writing a justification — so it is the right yardstick for judging whether an AI assistant could plausibly support a desk.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `uncertain`

## 4. Pros

- Built from real claims already checked by fact-checking organisations, so performance figures mean substantially more than FEVER's Wikipedia-derived scores
- The question-answer-justify decomposition matches editorial method and makes model output auditable step by step rather than as a bare label
- Includes a written-justification requirement, which exposes models that get the label right for the wrong reasons

## 5. Cons

- Licence could NOT be confirmed: no LICENSE or COPYING file in the repository root, GitHub API reports no detected licence, and the README has no licence section — redistribution and commercial terms are unknown and this is unresolved
- Requires a Google Programmable Search API key and CSE ID for coarse retrieval, so claim text and generated queries are sent to Google's Search API — not a local pipeline
- Dormant: last push 2024-11-27, no releases, 84 stars
- Verdicts are probabilistic model outputs requiring human adjudication, and the benchmark's own task remains far from solved

## 6. Feedback (documented)

No individual user reports verified. The documented finding is the licence gap, verified in session 1 by checking for LICENSE/COPYING and the GitHub licence API, and retained here as unresolved. The benchmark is well cited in the automated-fact-checking literature.

## 7. Assessment

Valuable intellectually, unusable as infrastructure. For your profile the right use is to borrow its evaluation design — decompose a claim into sub-questions, require an evidence trail and a written justification — when assessing any AI tool a vendor pitches to your newsroom. Do not redistribute the dataset or build a product on it until the licence position is clarified with the authors.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-11-27, no releases, no tags, no detected licence, 84 stars, 4 open issues. Two years without activity; typical academic release-and-move-on pattern.

## 9. Licensing

**Licence:** NOT CONFIRMED — no LICENSE/COPYING file in the repository root, GitHub licence API reports none, README has no licence section _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a — no weights distributed. Dataset terms also unconfirmed.

**Restrictions:** Unresolved. Treat redistribution and commercial use as legally unclear until clarified with the authors. Note that the underlying claims come from fact-checking organisations whose own content terms may also apply.

**Licence evidence:** https://github.com/MichSchli/AVeriTeC

## 10. Costs

No software fee. Requires a Google Programmable Search API key (paid above the free quota — current rates not verified here) and large local disk, plus an LLM for question generation (cost depends on provider). Estimate.

## 11. Privacy and data flows

NOT local: claim text and generated queries are sent to Google's Search API, and depending on model choice to an LLM provider. Retrieved pages are cached locally. Unsuitable for unpublished claims about sensitive subjects.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- No licence file — redistribution and commercial use legally unresolved
- Requires Google Search API; not a local pipeline

## 13. Alternatives

- FEVER where a clearly licensed benchmark is required
- [X-FACT](JAI-A4-08.md) for multilingual evaluation under an MIT licence
- [Full Fact AI Trust Benchmark](JAI-A4-15.md) for a practitioner-authored evaluation of assistant tools

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/MichSchli/AVeriTeC
- https://fever.ai/dataset/averitec.html

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

← 356. [Loki (OpenFactVerification)](JAI-A4-10.md) · 358. [CooRnet](JAI-A4-14.md) →
