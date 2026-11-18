# InVID-WeVerify Verification Plugin

`JAI-A4-04` · **82/100** · overall rank 126 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 53) |
| **Segment** | A4 · Fact-checking support and media verification (rank 2) |
| **Subcategory** | Media verification toolkit |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | AFP Medialab / vera.ai consortium |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (extension code) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/AFP-Medialab/verification-plugin) · [Documentation](https://weverify.eu/verification-plugin/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 1/5 · usability 5/5 · licence+cost 4/5 → **weighted 82/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (extension code) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the extension; deepfake and forensics models run on AFP/vera.ai backend services, weights not distributed and model licences not verified. |
| **Restrictions** | Extension code unrestricted. The backend services operate under the consortium's terms, not an open licence, so the analytical capability is not self-hostable. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free to use. No infrastructure. The cost is non-monetary: dependency on third-party backends you do not control and cannot audit.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/AFP-Medialab/verification-plugin/blob/master/LICENSE
- https://github.com/AFP-Medialab/verification-plugin
- https://weverify.eu/verification-plugin/

---

## 1. Purpose

Browser extension aggregating verification tools: video keyframe extraction, reverse image search across multiple engines, EXIF inspection, magnifier and forensic filters, deepfake and synthetic-media detection panels, archiving and OCR.

## Journalism / investigative use case

Front-line triage of a viral image or video claim: establish whether media is recycled, find the earliest appearance, inspect metadata, and gather forensic signals before publishing a verification. It is the single most widely used verification tool among working journalists, because it puts a dozen techniques one click away.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Breadth and accessibility: a reporter with no technical background can run keyframe extraction plus multi-engine reverse search in under a minute, which is why it dominates practical newsroom verification
- Actively maintained with a current release (v0.94, 2026-11-03) and pushed 2026-11-17, backed by AFP and an EU research consortium rather than a volunteer
- Extension code is MIT, so the client side is auditable
- Consolidates workflows (keyframes, reverse search, EXIF, archiving) that would otherwise require four separate tools and manual file shuffling

## 5. Cons

- NOT local-only, and this is the critical caveat: media submitted for keyframes, forensics, deepfake detection, translation or archiving is uploaded to AFP/vera.ai backend services, and reverse search sends it to Google, Baidu and Yandex. Submitting unpublished source material is a disclosure
- Forensic and deepfake panel outputs are probabilistic signals and investigative leads, NOT conclusive proof of manipulation or synthesis — false positives and negatives occur, and platform recompression degrades every forensic signal
- Matomo analytics is present in the extension, so usage telemetry exists
- Backend model weights are not distributed and their licences were not verified, so you cannot reproduce or audit the detector outputs

## 6. Feedback (documented)

No individual user reports verified in this survey, but the plugin's standing among verification practitioners is well documented by the InVID/WeVerify/vera.ai projects and by its adoption in verification training curricula. The upload-to-backend behaviour and the Matomo analytics are documented in the project's own privacy information — treat these as project-disclosed facts, not inferences.

## 7. Assessment

Adopt it for public, already-circulating media — that is the case it is built for and it is excellent there. Write an explicit rule against using it on unpublished source material, because the convenient buttons are the ones that upload. For media-in-exile work, note additionally that reverse-image search through Yandex or Baidu discloses the image to jurisdictions you may be investigating. Treat every forensic panel as a lead that must be corroborated by non-forensic reporting.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.94 (2026-11-03), 53 stars, 28 open issues. Same-day push with a current release; funded consortium backing (AFP Medialab, vera.ai). Star count understates adoption because users install from browser stores, not GitHub.

## 9. Licensing

**Licence:** MIT (extension code) _(SPDX verified)_

**Model / data licence:** n/a for the extension; deepfake and forensics models run on AFP/vera.ai backend services, weights not distributed and model licences not verified.

**Restrictions:** Extension code unrestricted. The backend services operate under the consortium's terms, not an open licence, so the analytical capability is not self-hostable.

**Licence evidence:** https://github.com/AFP-Medialab/verification-plugin/blob/master/LICENSE

## 10. Costs

Free to use. No infrastructure. The cost is non-monetary: dependency on third-party backends you do not control and cannot audit.

## 11. Privacy and data flows

The weakest privacy profile among widely recommended verification tools, and it must be understood plainly: media sent to the forensics, deepfake, keyframe, translation or archiving panels is uploaded to AFP/vera.ai; reverse-image search sends the image to Google, Baidu and Yandex; Matomo analytics records usage. Appropriate for public media, inappropriate for unpublished source material.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Uploads media to third-party backends — unsuitable for unpublished or source-sensitive material

## 13. Alternatives

- [Sherloq](OSINT-C2-12.md) for a fully local image-forensics workbench
- [PySceneDetect](OSINT-C2-10.md) plus ExifTool plus ImageHash for a local equivalent of the keyframe and metadata workflow
- Hosted verification services only where the media is already public

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/AFP-Medialab/verification-plugin
- https://weverify.eu/verification-plugin/
- https://github.com/AFP-Medialab/verification-plugin/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 125. [subfinder](OSINT-C3-23.md) · 127. [BERTopic](JAI-A2-04.md) →
