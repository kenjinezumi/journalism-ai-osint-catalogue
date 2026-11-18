# TruFor

`JAI-A4-18` · **61/100** · overall rank 315 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 117) |
| **Segment** | A4 · Fact-checking support and media verification (rank 9) |
| **Subcategory** | Image forgery localisation |
| **Type** | model |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | GRIP-UNINA (University of Naples Federico II) |
| **Maintenance** | Stable with low activity |
| **Licence** | NOT OSS — custom GRIP-UNINA terms: LICENSE.txt restricts use to informational and non-profit purposes |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/grip-unina/TruFor) · [Documentation](https://grip-unina.github.io/TruFor/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 1/5 → **weighted 61/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | NOT OSS — custom GRIP-UNINA terms: LICENSE.txt restricts use to informational and non-profit purposes |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same custom non-commercial GRIP-UNINA terms apply to the weights. |
| **Restrictions** | Commercial use is not permitted without separate permission. 'Informational and non-profit' does not clearly cover a commercially published investigation, and should not be assumed to. Redistribution is similarly restricted. |
| **Open-source status** | **Source available** — Restricted model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee for permitted non-profit/informational use. Commercial use requires permission — terms not publicly listed. GPU and Docker for inference.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/grip-unina/TruFor
- https://grip-unina.github.io/TruFor/

---

## 1. Purpose

Transformer-based image-forgery localisation model combining learned noise-residual fingerprints with RGB features, producing both a manipulation heatmap and a confidence/reliability map.

## Journalism / investigative use case

Second-opinion localisation on a single contested photo, where the reliability map is used to discount regions in which the model is unreliable — useful precisely because it tempers false alarms rather than producing a bare score.

## 2. Audience

specialist investigator, engineer

## 3. Project type

model · bucket `source-available-restricted`

## 4. Pros

- The reliability map is a genuine methodological advance for journalism: it tells you where not to trust the heatmap, which reduces the chance of publishing a false manipulation claim
- Strong published performance among localisation methods, from a group with a long forensics research record
- Inference runs locally inside Docker, so contested images need not leave the newsroom

## 5. Cons

- NOT open source: LICENSE.txt restricts use to informational and non-profit purposes, copyright GRIP-UNINA — a legal problem for any commercially operated newsroom and a blocker that is easy to miss because the code is on GitHub
- Outputs are probabilistic forensic signals, never conclusive proof of manipulation; platform recompression substantially degrades the signal
- Low activity (pushed 2025-05-29, no releases, 287 stars, 11 open issues) — a research release rather than a maintained tool
- Docker plus specific PyTorch versions; weights obtained per repository instructions rather than a package manager

## 6. Feedback (documented)

No individual user reports verified. Documented: the LICENSE.txt restriction to informational and non-profit use, read in session 1 and retained; PhotoHolmes independently flags TruFor's non-profit restriction in its own README, which corroborates the reading.

## 7. Assessment

Technically among the best available and legally unusable for a commercial newsroom without permission — that combination is the whole assessment. For your profile: if you work with a non-profit outlet or a research partner, this is a strong second opinion; if the outlet is commercially operated, either seek written permission from GRIP-UNINA or use CAT-Net, whose weights are CC-BY-4.0. Do not assume 'journalism is informational' satisfies an informational-use clause intended to exclude commercial deployment.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2025-05-29, no releases or tags, SPDX none, 287 stars, 11 open issues. Eighteen months since last push; a published research artefact that is complete rather than evolving.

## 9. Licensing

**Licence:** NOT OSS — custom GRIP-UNINA terms: LICENSE.txt restricts use to informational and non-profit purposes _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same custom non-commercial GRIP-UNINA terms apply to the weights.

**Restrictions:** Commercial use is not permitted without separate permission. 'Informational and non-profit' does not clearly cover a commercially published investigation, and should not be assumed to. Redistribution is similarly restricted.

**Licence evidence:** https://github.com/grip-unina/TruFor

## 10. Costs

No fee for permitted non-profit/informational use. Commercial use requires permission — terms not publicly listed. GPU and Docker for inference.

## 11. Privacy and data flows

Inference is local inside Docker, so images need not leave the newsroom. No third-party service documented.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Licence restricts use to informational and non-profit purposes — commercial newsroom use requires permission

## 13. Alternatives

- [CAT-Net](JAI-A4-19.md) — CC-BY-4.0 weights, commercially usable, JPEG-focused
- [PhotoHolmes](JAI-A4-17.md) to run several methods including permissive ones
- [Sherloq](OSINT-C2-12.md) for a fully local, GPL-3.0 manual forensics workbench

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/grip-unina/TruFor
- https://grip-unina.github.io/TruFor/

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

← 314. [uroman](JAI-A2-56.md) · 316. [theHarvester](OSINT-C3-28.md) →
