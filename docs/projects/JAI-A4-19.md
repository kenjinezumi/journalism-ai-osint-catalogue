# CAT-Net

`JAI-A4-19` · **63/100** · overall rank 303 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 115) |
| **Segment** | A4 · Fact-checking support and media verification (rank 8) |
| **Subcategory** | Image splicing detection |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | Myung-Joon Kwon (mjkwon2021) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 (code), per the README licence section; GitHub API reports no detected licence |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mjkwon2021/CAT-Net) · [Documentation](https://github.com/mjkwon2021/CAT-Net#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 4/5 → **weighted 63/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 (code), per the README licence section; GitHub API reports no detected licence |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | CC-BY-4.0 for pretrained weights and released datasets, per the README licence section. |
| **Restrictions** | CC-BY-4.0 requires attribution — cite the model in any methodology note. No non-commercial restriction, which is the key advantage. Because GitHub detects no licence file, confirm the README statement against the repository before commercial reliance. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. GPU for inference. Weights from third-party file hosts (mirror them). Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/mjkwon2021/CAT-Net

---

## 1. Purpose

Neural network that detects and localises spliced regions in JPEG images by tracing compression-artefact inconsistencies, using both RGB and DCT-domain streams.

## Journalism / investigative use case

Spotting spliced-in regions in JPEGs that still retain their original compression history — for example a photo circulated as a camera original rather than a platform re-encode, where a pasted element carries a different compression signature from its surroundings.

## 2. Audience

specialist investigator, engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- CC-BY-4.0 pretrained weights and Apache-2.0 code per the README licence section — a commercially usable combination, which is rare among forensic models and is the main reason to prefer it over TruFor
- Compression-artefact tracing is a physically grounded signal rather than a learned style cue, so a positive finding is more explainable to an editor
- Still receiving commits (pushed 2026-10-15) years after publication

## 5. Cons

- Depends on JPEG compression artefacts, so its signal is weak or absent for PNGs, screenshots and heavily re-encoded images — which is the state most social-media images arrive in, sharply limiting real-world applicability
- v1 handles splicing only, not other manipulation classes, so a negative result says very little
- Pretrained and trained weights are hosted on Google Drive and Baiduyun — an availability and supply-chain risk, and awkward for automated deployment
- 44 open issues against 317 stars with no releases or tags; GitHub reports no SPDX licence, so the Apache-2.0/CC-BY-4.0 position rests on the README rather than a detected licence file

## 6. Feedback (documented)

No individual user reports verified. Documented: the README licence section stating Apache-2.0 code and CC-BY-4.0 weights and datasets (read in session 1, retained); weights hosted on Google Drive and Baiduyun; 317 stars with 44 open issues.

## 7. Assessment

The commercially usable forensic localisation model in this catalogue, which makes it the default choice for a commercial newsroom despite TruFor's technical edge. Its real limitation is scope: it answers a narrow question about JPEG splicing, and the images you most want to check have usually been recompressed past the point where it helps. Use it when you have what purports to be a camera original, mirror the weights locally rather than depending on Google Drive, and treat output as a lead.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-15, no releases or tags, SPDX none, 317 stars, 44 open issues. Commits within the last month but no release engineering and a sizeable backlog; a research artefact receiving occasional attention.

## 9. Licensing

**Licence:** Apache-2.0 (code), per the README licence section; GitHub API reports no detected licence _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** CC-BY-4.0 for pretrained weights and released datasets, per the README licence section.

**Restrictions:** CC-BY-4.0 requires attribution — cite the model in any methodology note. No non-commercial restriction, which is the key advantage. Because GitHub detects no licence file, confirm the README statement against the repository before commercial reliance.

**Licence evidence:** https://github.com/mjkwon2021/CAT-Net

## 10. Costs

No fee. GPU for inference. Weights from third-party file hosts (mirror them). Estimate.

## 11. Privacy and data flows

Weights pulled from Google Drive/Baiduyun on setup; inference is local thereafter, so contested images stay in the newsroom.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [TruFor](JAI-A4-18.md) for stronger localisation — but non-commercial licence only
- [PhotoHolmes](JAI-A4-17.md) to compare several methods including this one
- [Sherloq](OSINT-C2-12.md)'s JPEG ghost and ELA panels for a quicker manual check

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/mjkwon2021/CAT-Net

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
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 302. [Alegre (Meedan)](JAI-A4-02.md) · 304. [Conifer](OSINT-C1-35.md) →
