# SelfBlendedImages (SBI)

`JAI-A4-27` · **51/100** · overall rank 343 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 132) |
| **Segment** | A4 · Fact-checking support and media verification (rank 19) |
| **Subcategory** | Deepfake detection |
| **Type** | prototype |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | Kaede Shiohara (mapooon), University of Tokyo |
| **Maintenance** | Stable with low activity |
| **Licence** | Custom research-only terms — authors state code and pretrained model are 'freely available for research purpose'; commercial use requires a separate licence agreement |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mapooon/SelfBlendedImages) · [Documentation](https://github.com/mapooon/SelfBlendedImages#readme) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 1/5 → **weighted 51/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | Custom research-only terms — authors state code and pretrained model are 'freely available for research purpose'; commercial use requires a separate licence agreement |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same research-only terms apply to the pretrained model. |
| **Restrictions** | Commercial use prohibited without a separate agreement. A commercially published investigation is not research use. |
| **Open-source status** | **Source available** — Source published under a restricted, non-OSI licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee for research use; commercial use requires a negotiated agreement (terms not publicly listed). GPU for inference; weights from Google Drive.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/mapooon/SelfBlendedImages

---

## 1. Purpose

Face-manipulation detection method trained on synthetically self-blended images rather than on specific deepfake generators, aiming for generator-agnostic detection.

## Journalism / investigative use case

A generator-agnostic face-manipulation detector worth running as one signal in an ensemble, since it was designed for the case journalists actually face — a fake made with a tool nobody has trained on.

## 2. Audience

engineer, specialist investigator

## 3. Project type

prototype · bucket `source-available-restricted`

## 4. Pros

- The training approach (self-blending real faces rather than collecting generator outputs) directly targets the generalisation problem, which is the right instinct for real-world verification
- Authors report honest cross-dataset figures rather than only in-domain results — roughly 93.8% AUC on Celeb-DF and 97.9% on DFD but only about 73.0% on DFDC — which is the useful disclosure
- Local inference, so case material stays in the newsroom

## 5. Cons

- Licence is custom research-only: the authors state the code and pretrained model are 'freely available for research purpose' and commercial use requires a separate licence agreement — not usable by a commercial newsroom without permission
- Probabilistic signal only, never conclusive proof of manipulation; and the authors' own spread (73.0% to 97.9% AUC depending on test set) shows how much performance depends on what the fake was made with
- Pretrained weights hosted on Google Drive — availability and supply-chain risk
- Low activity (pushed 2026-03-13, no releases, 277 stars, 26 open issues) and a preprocessing pipeline requiring facial landmark detection

## 6. Feedback (documented)

No individual user reports verified. Documented from the repository: the research-only licence statement requiring a separate agreement for commercial use, and the authors' reported cross-dataset AUCs (≈93.8% Celeb-DF, ≈97.9% DFD, ≈73.0% DFDC) — these are author-reported figures, not independent measurements.

## 7. Assessment

Methodologically one of the better ideas in deepfake detection and legally unavailable to a commercial newsroom. For your profile the honest conclusion across this whole subcategory is uncomfortable but important: the open detectors are either non-commercial, dormant, or demonstrably unreliable in the wild, so a newsroom's synthetic-media strategy should rest on provenance (C2PA, source contact, earliest-upload tracing) rather than detection. Keep SBI as a research-partner option.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-03-13, no releases or tags, SPDX NOASSERTION, 277 stars, 26 open issues. Eight months since last push; a complete research release with light attention.

## 9. Licensing

**Licence:** Custom research-only terms — authors state code and pretrained model are 'freely available for research purpose'; commercial use requires a separate licence agreement _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same research-only terms apply to the pretrained model.

**Restrictions:** Commercial use prohibited without a separate agreement. A commercially published investigation is not research use.

**Licence evidence:** https://github.com/mapooon/SelfBlendedImages

## 10. Costs

No fee for research use; commercial use requires a negotiated agreement (terms not publicly listed). GPU for inference; weights from Google Drive.

## 11. Privacy and data flows

Local inference; weight download from Google Drive is the only external touchpoint. Case images stay local.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Research-only licence; commercial use requires a separate agreement

## 13. Alternatives

- [Community Forensics](JAI-A4-21.md) for an MIT-licensed detector usable commercially
- [LAA-Net](JAI-A4-28.md) for compression-robust detection — also academic-licence restricted
- Provenance-based verification rather than detection, which I would prioritise

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/mapooon/SelfBlendedImages

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

← 342. [ClaimBuster-Spotter](JAI-A4-05.md) · 344. [Andriller](SUR-B3-17.md) →
