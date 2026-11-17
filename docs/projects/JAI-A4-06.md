# FEVER platform and baselines

`JAI-A4-06` · **60/100** · overall rank 324 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 121) |
| **Segment** | A4 · Fact-checking support and media verification (rank 10) |
| **Subcategory** | Fact-verification benchmark |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | FEVER workshop organisers (repository under awslabs) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/awslabs/fever) · [Documentation](https://fever.ai/) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 60/100**

---

## 1. Purpose

Benchmark dataset, annotation platform and baseline systems for fact extraction and verification: given a claim, retrieve evidence sentences from Wikipedia and classify as supported, refuted or not-enough-info.

## Journalism / investigative use case

Standard reference point for evaluating any evidence-retrieval-plus-entailment pipeline before trusting it on real claims. The annotation platform is independently reusable for building a newsroom's own claim/evidence gold set — which is the only honest way to know whether a tool works on your material.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- The reusable annotation platform is the underrated asset: it lets you construct your own labelled claim/evidence set rather than extrapolating from published benchmarks
- Fully local once the data is downloaded, with no API keys required — unusual among fact-verification tooling
- Apache-2.0 code and a widely cited benchmark, so results are comparable to the published literature
- Establishes the discipline of measuring retrieval and entailment separately, which is diagnostically useful

## 5. Cons

- Claims are human-written over Wikipedia, not real-world political or social-media claims, so FEVER scores systematically overstate real-world performance — the single most important caveat when a vendor cites a FEVER number
- Baseline checkpoints are downloaded separately and their licences were not verified; the Wikipedia evidence corpus is CC-BY-SA, which carries ShareAlike obligations on derived corpora
- Low activity: pushed 2026-02-20, no releases or tags, 130 stars — a benchmark artefact rather than a maintained product
- Verdicts are probabilistic classifications, never proof, and the three-way label scheme does not match editorial reality

## 6. Feedback (documented)

No individual user reports verified. Documented: FEVER is among the most cited benchmarks in automated fact verification; its Wikipedia-derived construction and the resulting optimism bias are discussed in the subsequent literature (including AVeriTeC's framing of why a more realistic benchmark was needed).

## 7. Assessment

Useful to you as a measuring instrument and an annotation tool, not as a capability. Concretely: when someone proposes an AI fact-checking tool, ask what it scores on real claims rather than FEVER, and use the annotation platform to build a small gold set from your own published fact-checks to test it. That is a higher-value use of FEVER than running its baselines.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-02-20, no releases or tags, 130 stars, 1 open issue. Benchmark artefacts are expected to be static once published; the near-empty issue tracker is consistent with a finished research release rather than neglect.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** NOT verified — baseline checkpoints are downloaded separately. The Wikipedia evidence corpus is CC-BY-SA.

**Restrictions:** Code permissive. CC-BY-SA on the Wikipedia evidence corpus imposes attribution and ShareAlike obligations if you redistribute a derived evidence corpus.

**Licence evidence:** https://github.com/awslabs/fever/blob/master/LICENSE

## 10. Costs

No fee. Requires substantial local disk for the Wikipedia dump and dataset, plus a Python ML stack. No paid APIs. Estimate.

## 11. Privacy and data flows

Fully local once data is downloaded; no third-party API keys required. Suitable for use on an isolated machine.

## 12. Verdict

**Reference only**

## 13. Alternatives

- AVeriTeC for a benchmark closer to real fact-checking practice — but its licence is unconfirmed
- [X-FACT](JAI-A4-08.md) for multilingual claim classification evaluation
- Building your own gold set from your newsroom's published fact-checks, using FEVER's annotation platform

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/awslabs/fever
- https://fever.ai/
- https://github.com/awslabs/fever/blob/master/LICENSE

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

← 323. [VFRAME](OSINT-C2-14.md) · 325. [Maltego](OSINT-C3-36.md) →
