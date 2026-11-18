# ASVspoof 2021 baseline systems

`JAI-A4-30` · **46/100** · overall rank 349 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 136) |
| **Segment** | A4 · Fact-checking support and media verification (rank 23) |
| **Subcategory** | Audio spoofing evaluation |
| **Type** | prototype |
| **Bucket** | `uncertain` |
| **Maintainer** | ASVspoof challenge organisers |
| **Maintenance** | Dormant |
| **Licence** | NOT CONFIRMED — no root LICENSE file found (direct fetch of /blob/main/LICENSE returned 404); terms may differ per baseline subdirectory |
| **Licence type** | Unresolved |
| **Open-source status** | Unverified |
| **Software price** | **No software fee** |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/asvspoof-challenge/2021) · [Documentation](https://www.asvspoof.org/) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 1/5 · licence+cost 1/5 → **weighted 46/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Unresolved |
| **Exact licence (as recorded)** | NOT CONFIRMED — no root LICENSE file found (direct fetch of /blob/main/LICENSE returned 404); terms may differ per baseline subdirectory |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Not verified. ASVspoof evaluation data is obtained separately under its own terms. |
| **Restrictions** | Unresolved — treat reuse and redistribution as legally unclear. Per-subdirectory licences may differ, so a blanket assumption either way is unsafe. |
| **Open-source status** | **Unverified** — Licence could not be confirmed — reuse legally unresolved |
| **Software price** | **No software fee** |
| **Additional costs** | MATLAB (paid) only for the original baselines — Python ports avoid it; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee for the code. MATLAB (a paid product) is required for the original GMM baselines; Python ports avoid this. Evaluation data obtained separately. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/asvspoof-challenge/2021
- https://www.asvspoof.org/

> **Unresolved:** the licence could not be confirmed from the evidence gathered.

---

## 1. Purpose

Reference baseline implementations and the official evaluation/scoring code for the ASVspoof 2021 anti-spoofing challenge, covering logical access, physical access and speech deepfake tracks.

## Journalism / investigative use case

The reference implementations and, more importantly, the official scoring code for audio deepfake detection — what you use to independently compute equal error rate on your own test clips rather than accepting a vendor's self-reported number.

## 2. Audience

engineer, specialist investigator

## 3. Project type

prototype · bucket `uncertain`

## 4. Pros

- The official scoring code is the genuinely valuable artefact: it lets you measure a detector's performance on your own material with the field's standard metric, instead of trusting marketing
- Covers the speech deepfake track specifically, which is the track relevant to fabricated audio of public figures
- Fully local training, inference and scoring with no third-party API calls

## 5. Cons

- No root LICENSE file was found (a fetch of /blob/main/LICENSE returned 404), so licensing could not be confirmed and may differ per baseline subdirectory — treat reuse as legally unresolved
- MATLAB is required for the GMM baselines' original versions (Python ports are provided), which is a paid dependency for part of the repository
- Dormant: last push 2024-06-06, no releases, 259 stars, 16 open issues
- ASVspoof evaluation data is obtained separately under its own terms, so the benchmark is not self-contained

## 6. Feedback (documented)

No individual user reports verified. Documented: the absence of a root LICENSE file, verified in session 1 by a direct fetch returning 404, and retained as unresolved; the MATLAB requirement for original GMM baselines; last push 2024-06-06.

## 7. Assessment

Worth knowing for one specific purpose — computing EER yourself with the standard scoring code — which is a genuinely useful capability when assessing an audio-detection vendor. But the unresolved licence means I would not vendor this code into a newsroom product; read it, reimplement the metric (EER is a short, well-specified calculation), and avoid the licence question entirely. That is my recommendation for your profile: take the methodology, not the repository.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-06-06, no releases or tags, no detected licence, 259 stars, 16 open issues. Over two years inactive; challenge-cycle repositories are typically frozen after the event.

## 9. Licensing

**Licence:** NOT CONFIRMED — no root LICENSE file found (direct fetch of /blob/main/LICENSE returned 404); terms may differ per baseline subdirectory _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Not verified. ASVspoof evaluation data is obtained separately under its own terms.

**Restrictions:** Unresolved — treat reuse and redistribution as legally unclear. Per-subdirectory licences may differ, so a blanket assumption either way is unsafe.

**Licence evidence:** https://github.com/asvspoof-challenge/2021

## 10. Costs

No fee for the code. MATLAB (a paid product) is required for the original GMM baselines; Python ports avoid this. Evaluation data obtained separately. Estimate.

## 11. Privacy and data flows

Local training, inference and scoring; no third-party API calls.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- No licence file — reuse legally unresolved
- MATLAB dependency for original baselines

## 13. Alternatives

- Reimplementing EER yourself from the metric definition, avoiding the licence question
- [AASIST](JAI-A4-29.md) for an MIT-licensed detector with in-repo weights
- Commissioning an independent evaluation from an academic partner

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/asvspoof-challenge/2021
- https://www.asvspoof.org/

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

← 348. [Deepfake-Eval-2024](JAI-A4-31.md) · 350. [Noiseprint](JAI-A4-22.md) →
