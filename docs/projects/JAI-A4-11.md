# DEFAME

`JAI-A4-11` · **49/100** · overall rank 346 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 133) |
| **Segment** | A4 · Fact-checking support and media verification (rank 20) |
| **Subcategory** | Multimodal claim verification |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | multimodal-ai-lab (TU Darmstadt) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/multimodal-ai-lab/DEFAME) · [Documentation](https://github.com/multimodal-ai-lab/DEFAME#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 1/5 · usability 2/5 · licence+cost 3/5 → **weighted 49/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a by default — uses hosted LLMs (GPT-4o default); optional local GPU components pull third-party models whose licences were not verified. |
| **Restrictions** | Code permissive. The operative constraints are the third-party API terms for the LLM and search services. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | **Mandatory paid dependency** — mandatory paid dependency; self-hosted infrastructure |
| **Cost conditions** | **Mandatory paid dependency**; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Software free. Operation requires paid API keys: an LLM provider (GPT-4o-class token charges) plus search and reverse-image services — per-claim cost, rates not verified here. Optional CUDA GPU for local components. Real cost is per-use, not infrastructure.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/multimodal-ai-lab/DEFAME/blob/main/LICENSE
- https://github.com/multimodal-ai-lab/DEFAME

---

## 1. Purpose

Multimodal fact-verification framework that plans and executes a sequence of tools — web search, reverse image search, image forensics, geolocation — against an image-plus-text claim and produces a verdict with an evidence trail.

## Journalism / investigative use case

Verification of image-plus-text claims as they actually circulate on social media, where the claim is a photo with a caption. Its distinguishing output is a tool-by-tool evidence trail a journalist can audit, rather than a bare label.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Addresses the real shape of modern misinformation — captioned images — which text-only fact-verification systems structurally cannot handle
- The auditable per-tool evidence trail is the right design: a reporter can see which step produced which signal rather than trusting an end-to-end score
- Apache-2.0 with a tagged release (v2.1.0, 2025-04-17) and Dockerised deployment
- Architecturally modular, so the orchestration pattern is reusable even if you replace the default components

## 5. Cons

- NOT local by default: claim text and submitted images are sent to the configured LLM provider (GPT-4o by default) and to external search and reverse-image services — a disclosure for any unpublished image
- Research prototype: verdicts and the evidence chain are probabilistic model output requiring human adjudication, never proof; the image-forensics and geolocation outputs are leads, not determinations
- Activity has slowed (pushed 2026-05-21, release April 2025) and the community is small (62 stars), so you would own any maintenance
- Requires API keys for an LLM and for search/reverse-image tools, so operating cost is per-use and depends on third parties

## 6. Feedback (documented)

No individual user reports verified. Documented: the hosted-LLM default (GPT-4o) and required API keys are stated in the project's own configuration documentation; 62 stars with 4 open issues indicates a research release with limited uptake.

## 7. Assessment

The most interesting architecture in this subcategory and the one I would study before building anything similar — tool-orchestration with an auditable trail is the right pattern for verification automation. But I would not deploy it as shipped, because the default configuration sends source images to OpenAI and to Yandex-class reverse-search engines. For your profile the viable path is to reimplement the orchestration against a self-hosted model and local forensics (Sherloq, PhotoHolmes) for sensitive material, and use DEFAME as-is only on already-public images.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-05-21, latest release v2.1.0 (2025-04-17), 62 stars, 4 open issues. Six months since last push and nineteen months since the last release; academic-lab release pattern. Declining rather than dormant since commits continued into 2026.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a by default — uses hosted LLMs (GPT-4o default); optional local GPU components pull third-party models whose licences were not verified.

**Restrictions:** Code permissive. The operative constraints are the third-party API terms for the LLM and search services.

**Licence evidence:** https://github.com/multimodal-ai-lab/DEFAME/blob/main/LICENSE

## 10. Costs

Software free. Operation requires paid API keys: an LLM provider (GPT-4o-class token charges) plus search and reverse-image services — per-claim cost, rates not verified here. Optional CUDA GPU for local components. Real cost is per-use, not infrastructure.

## 11. Privacy and data flows

NOT local by default. Claim text and submitted images go to the configured LLM provider and to external search and reverse-image services. Unsuitable for unpublished or source-supplied imagery without reconfiguration to local components.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Hosted LLM and external search by default — images and claims leave your infrastructure

## 13. Alternatives

- InVID-WeVerify plugin for a journalist-usable (also non-local) equivalent
- [PhotoHolmes](JAI-A4-17.md) plus Sherloq plus ShadowFinder for a fully local manual workflow
- Reimplementing the orchestration pattern against a self-hosted model

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/multimodal-ai-lab/DEFAME
- https://github.com/multimodal-ai-lab/DEFAME/blob/main/LICENSE

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

← 345. [diffengine](SUR-B1-25.md) · 347. [LAA-Net](JAI-A4-28.md) →
