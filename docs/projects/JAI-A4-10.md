# Loki (OpenFactVerification)

`JAI-A4-10` · **38/100** · overall rank 356 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 141) |
| **Segment** | A4 · Fact-checking support and media verification (rank 28) |
| **Subcategory** | LLM-assisted claim verification |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Libr-AI |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Libr-AI/OpenFactVerification) · [Documentation](https://github.com/Libr-AI/OpenFactVerification#readme) |

**Scores** — relevance 2/5 · capability 2/5 · maintenance 1/5 · privacy 1/5 · usability 3/5 · licence+cost 3/5 → **weighted 38/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a — calls hosted LLM APIs rather than bundling weights; those providers' terms govern use. |
| **Restrictions** | Code unrestricted. The binding constraints are the third-party API terms you must accept to run it at all. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | **Mandatory paid dependency** — mandatory paid dependency; self-hosted infrastructure |
| **Cost conditions** | **Mandatory paid dependency**; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Software free, but operation requires paid APIs: an OpenAI key (token charges — current rates not verified here) and a Serper search key (paid above free tier — not verified here). Running it over a long document is a real per-use cost, not an estimate of infrastructure.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Libr-AI/OpenFactVerification/blob/main/LICENSE
- https://github.com/Libr-AI/OpenFactVerification

---

## 1. Purpose

Pipeline that decomposes a text into discrete checkable claims, retrieves evidence via a search API, and uses an LLM to produce per-claim verdicts with cited sources.

## Journalism / investigative use case

First-pass screening of a long text — a press release, transcript, filed story or AI-generated draft — into a ranked list of discrete checkable claims with candidate evidence links, which a journalist then verifies manually.

## 2. Audience

engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Claim decomposition is the genuinely useful part: turning prose into an enumerated list of atomic factual assertions is tedious human work and the model does it adequately
- MIT licensed with a clear pipeline structure, so the decomposition stage can be reused independently of the verdict stage
- Produces cited evidence links rather than bare verdicts, which at least makes the output checkable

## 5. Cons

- NOT local: an OPENAI_API_KEY is required for all tasks per the README, and a SERPER_API_KEY for evidence retrieval — submitted text and generated queries go to OpenAI and a Google Search proxy. Unsuitable for unpublished material
- Verdicts are LLM-generated probabilistic assessments with known failure modes — hallucinated reasoning, over-trust in low-quality retrieved sources, sensitivity to prompt and search ranking — so they are assistance, not adjudication
- Dormant: last push 2024-10-03, latest release v0.0.2 (2024-04-21), 1,165 stars with only 3 open issues — the low issue count here reflects abandonment rather than triage
- Hard-wired to specific providers, so swapping in a self-hosted model is a code change rather than configuration

## 6. Feedback (documented)

No individual user reports verified. Documented: the mandatory OpenAI and Serper API keys stated in the project's README; dormancy since October 2024; 1,165 stars indicating initial interest that did not convert into sustained maintenance.

## 7. Assessment

Avoid for new deployment as an end-to-end tool: it is dormant and its architecture sends your text to third parties by design. If claim decomposition is what you want, reimplement that one stage against a self-hosted model — it is a modest prompt-engineering task and keeps the material inside the perimeter. The broader judgement for your work: LLM verdict generation on public-interest claims is the wrong shape of automation, because the expensive part of fact-checking is evidence judgement, which is exactly what the model does worst.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-10-03, latest release v0.0.2 (2024-04-21), 1,165 stars, 3 open issues. Over two years inactive. The very low open-issue count against high stars indicates the tracker is unattended rather than well managed.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — calls hosted LLM APIs rather than bundling weights; those providers' terms govern use.

**Restrictions:** Code unrestricted. The binding constraints are the third-party API terms you must accept to run it at all.

**Licence evidence:** https://github.com/Libr-AI/OpenFactVerification/blob/main/LICENSE

## 10. Costs

Software free, but operation requires paid APIs: an OpenAI key (token charges — current rates not verified here) and a Serper search key (paid above free tier — not verified here). Running it over a long document is a real per-use cost, not an estimate of infrastructure.

## 11. Privacy and data flows

NOT local. Submitted text, extracted claims and generated queries are sent to OpenAI and Serper. Unsuitable for unpublished material, source documents, or anything whose subject should not learn it is being checked.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Requires OpenAI and Serper API keys — text leaves your infrastructure by design
- Dormant since October 2024

## 13. Alternatives

- [FacTool](JAI-A4-12.md) for a similar architecture — but it shares the hosted-API dependency and is also dormant
- A self-hosted LLM performing claim decomposition only, with human evidence judgement
- [DEFAME](JAI-A4-11.md) for multimodal claims with an auditable tool-by-tool evidence trail — also hosted-LLM dependent by default

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Libr-AI/OpenFactVerification
- https://github.com/Libr-AI/OpenFactVerification/blob/main/LICENSE

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

← 355. [Whoogle Search](OSINT-C1-04.md) · 357. [AVeriTeC dataset and baseline](JAI-A4-07.md) →
