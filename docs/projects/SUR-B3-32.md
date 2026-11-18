# ProofMode

`SUR-B3-32` · **73/100** · overall rank 238 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 61) |
| **Segment** | B3 · Protecting journalists and sources (rank 30) |
| **Subcategory** | Capture provenance |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Guardian Project |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/guardianproject/proofmode-android) · [Documentation](https://proofmode.org/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 73/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0: embedding the library in a distributed proprietary app triggers copyleft. Relevant if you build a newsroom contributor app around it. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free. No infrastructure unless you build a verification service around the proof bundles. Cost is contributor training and the storage of proof bundles alongside media.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/guardianproject/proofmode-android/blob/main/LICENSE
- https://github.com/guardianproject/proofmode-android
- https://proofmode.org/
- `../sources/evidence/leads.md`

---

## 1. Purpose

Android application and library that attaches verifiable provenance to photos and videos at capture time — cryptographic hashes, signatures, and optional sensor and network metadata — producing a proof bundle alongside the media.

## Journalism / investigative use case

Strengthening the evidentiary value of material captured by reporters or trained citizen witnesses: a photo taken with ProofMode carries a signed hash and capture context, so its integrity from the moment of capture can be demonstrated rather than asserted — which matters when a government claims footage was fabricated.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Provenance-at-capture is the strongest form of media verification, because it establishes integrity from origin rather than inferring manipulation afterwards — the same logic as C2PA but usable on an ordinary Android phone today
- Designed for human-rights documentation by an organisation with a long track record in that field, so the threat model matches journalism rather than commercial content authentication
- GPL-3.0 and actively maintained (3.5.1-BETA-3, 2026-11-13; pushed the same day), with a library form for embedding in a newsroom's own app
- Optional metadata levels let the user decide how much context to attach, which matters because sensor and network metadata can identify the photographer

## 5. Cons

- Only helps for media captured with it, so it does nothing for the overwhelming majority of material that arrives already made — it is a programme to run with trained contributors, not a verification tool for incoming content
- The metadata that makes proof strong (location, nearby networks, device identifiers) is exactly what can endanger the photographer, so the configuration is a direct trade-off between evidentiary value and source safety
- Beta release line (3.5.1-BETA-3) and a modest community (266 stars, 21 open issues); the GitHub repository is a mirror of Guardian Project's GitLab
- A signed hash proves the file has not changed since capture; it does not prove the scene was not staged, and that distinction will be lost on audiences unless carefully explained

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 266 stars with 21 open issues, release 3.5.1-BETA-3 (2026-11-13) with same-day push, GPL-3.0; the repository notes it is a mirror of the Guardian Project GitLab. The transfer guardianproject/proofmode → guardianproject/proofmode-android was confirmed by redirect in this session.

## 7. Assessment

Pilot it where you work with trained contributors or stringers whose material may be challenged — that is the case where capture-time provenance pays off. For your profile the configuration decision is the whole story: attach enough to prove integrity, and think hard before enabling location and network metadata, because a proof bundle that identifies where the photographer stood can be the thing that endangers them. Pair it with C2PA signing at publication so the chain extends from capture to story.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release 3.5.1-BETA-3 published the same day, 266 stars, 21 open issues, GPL-3.0. Same-day release and push from an established maintainer; the beta designation reflects the release line rather than inactivity.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0: embedding the library in a distributed proprietary app triggers copyleft. Relevant if you build a newsroom contributor app around it.

**Licence evidence:** https://github.com/guardianproject/proofmode-android/blob/main/LICENSE

## 10. Costs

Free. No infrastructure unless you build a verification service around the proof bundles. Cost is contributor training and the storage of proof bundles alongside media.

## 11. Privacy and data flows

Configurable, and the configuration is the privacy decision: full metadata strengthens proof and can identify the photographer, while minimal metadata is safer and weaker. Processing is local and nothing is uploaded by the app itself.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Proof-strengthening metadata can identify the photographer — configuration is a safety trade-off

## 13. Alternatives

- [c2pa-rs / c2patool](OSINT-C2-13.md) for provenance signing at the publication rather than capture stage
- Plain cryptographic hashing of captured files, published promptly, as a low-tech alternative
- Standard camera capture plus careful chain-of-custody documentation

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/guardianproject/proofmode-android
- https://proofmode.org/
- https://github.com/guardianproject/proofmode-android/blob/main/LICENSE
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |

---

← 237. [Marginalia Search](OSINT-C1-05.md) · 239. [SAM.gov](SUR-B2-15.md) →
