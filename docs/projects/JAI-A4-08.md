# X-FACT

`JAI-A4-08` · **52/100** · overall rank 341 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 130) |
| **Segment** | A4 · Fact-checking support and media verification (rank 17) |
| **Subcategory** | Multilingual fact-verification benchmark |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | University of Utah NLP (utahnlp) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/utahnlp/x-fact) · [Documentation](https://github.com/utahnlp/x-fact#readme) |

**Scores** — relevance 2/5 · capability 2/5 · maintenance 1/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 52/100**

---

## 1. Purpose

Multilingual benchmark of claims and fact-check verdicts drawn from fact-checking sites in 25 languages, with harmonised labels for evaluating cross-lingual claim classification.

## Journalism / investigative use case

Lets a newsroom test whether an automated claim-classification or claim-matching approach actually transfers to the languages it publishes in, rather than assuming English-trained performance carries over — a directly relevant question for any outlet publishing in several languages or in exile.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Multilingual coverage (25 languages) is the specific gap it fills; almost every other benchmark here is English-only
- MIT licensed, which — unusually among these academic datasets — makes reuse legally clear
- Fully local with no API keys required, so evaluation can run on an isolated machine

## 5. Cons

- A benchmark, not a tool: it classifies claims against labels from fact-checking sites without retrieving evidence, so models trained on it learn surface and metadata cues as much as factuality — a known shortcut problem
- Labels harmonised across organisations with different verdict scales, which introduces mapping noise that limits how precisely results can be interpreted
- Dormant: last push 2024-10-04, no releases, 31 stars — minimal community
- No weights distributed, so you must bring your own multilingual model

## 6. Feedback (documented)

No individual user reports verified. Documented: MIT licence confirmed via the GitHub API; 31 stars and no activity since October 2024. Cited in the multilingual fact-checking literature.

## 7. Assessment

Narrow but legitimately useful to you for one specific decision: before trusting any claim-matching component across your publication languages, measure it here. Treat the absolute numbers sceptically because of the evidence-free task design, but the relative drop between English and your other languages is the informative signal — and that drop is usually large. Keep as a reference instrument.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-10-04, no releases or tags, 31 stars, 1 open issue. Over two years inactive; static dataset artefact, which limits the practical harm of dormancy.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — no weights distributed. Note the underlying claims derive from fact-checking sites whose own content terms may apply to redistribution.

**Restrictions:** Code and dataset packaging are MIT. Upstream publisher content rights are a residual consideration if you republish claim text.

**Licence evidence:** https://github.com/utahnlp/x-fact/blob/main/LICENSE

## 10. Costs

No fee. Python ML stack plus whichever multilingual model you evaluate; GPU helpful. No paid APIs.

## 11. Privacy and data flows

Local; no API keys required.

## 12. Verdict

**Reference only**

## 13. Alternatives

- AVeriTeC for a more realistic task design — but licence unconfirmed
- FEVER for English evidence-retrieval evaluation
- Building a gold set from your own newsroom's multilingual fact-checks

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/utahnlp/x-fact
- https://github.com/utahnlp/x-fact/blob/main/LICENSE

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

← 340. [SuperGlue (pretrained network)](OSINT-C2-33.md) · 342. [ClaimBuster-Spotter](JAI-A4-05.md) →
