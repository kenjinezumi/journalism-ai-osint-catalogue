# mat2

`SUR-B3-07` · **94/100** · overall rank 12 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 3) |
| **Segment** | B3 · Protecting journalists and sources (rank 2) |
| **Subcategory** | Metadata removal |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Julien Voisin (jvoisin) |
| **Maintenance** | Actively maintained |
| **Licence** | LGPL-3.0-or-later |
| **Licence type** | Weak copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/jvoisin/mat2) · [Documentation](https://0xacab.org/jvoisin/mat2) |
| **Also known as** | Metadata Anonymisation Toolkit 2 |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 94/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Weak copyleft |
| **Exact licence (as recorded)** | LGPL-3.0-or-later |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | LGPL-3.0-or-later: linking from a proprietary tool is permitted provided the library remains replaceable; modifications to mat2 itself must be shared. Suitable for building a newsroom wrapper around. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Per-format system libraries; negligible compute. No paid dependencies.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/jvoisin/mat2/blob/master/LICENSE
- https://github.com/jvoisin/mat2
- https://0xacab.org/jvoisin/mat2
- `../sources/recovered/cat/ground_truth.tsv`
- `../sources/evidence/leads.md`

---

## 1. Purpose

Metadata removal tool supporting a wide range of file formats — images, documents, audio, video, archives — that strips identifying metadata and can report which formats are supported on the current system.

## Journalism / investigative use case

The counterpart to verification: strip identifying metadata from images and documents before publishing or sharing them, so a published photo does not burn the source's device, location or filesystem trail. This is the step that has repeatedly failed in real cases where published files carried GPS coordinates or author names.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Breadth of format support means one tool covers the realistic range of files a newsroom publishes, rather than needing per-format handling
- Addresses a documented and recurring failure mode — published files leaking source-identifying metadata — with a simple, auditable intervention
- LGPL-3.0-or-later with exemplary maintenance: release 0.15.0 (2026-08-04), pushed 2026-11-15, and only 2 open issues against 394 stars
- Fully local processing, and `--check-dependencies` tells you honestly which formats your installation can actually clean

## 5. Cons

- Cleaning is best-effort and format-specific: unsupported formats may be refused or incompletely cleaned, so a silent partial clean is possible and you must check the tool's own report rather than assume success
- It cannot remove information in visible pixels — reflections, screen contents, identifiable surroundings, visible badges — which is a frequent and more serious disclosure route than metadata
- Per-format system library dependencies mean capability varies by installation, so a clean on one machine is not evidence of a clean on another
- CLI-oriented; a reporter needs either training or a wrapper, and the ones who most need it are least likely to use a terminal

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 394 stars with 2 open issues, release 0.15.0 (2026-08-04), pushed 2026-11-15, LGPL-3.0 (independently recorded in session 1's ground_truth.tsv). The canonical home is 0xacab.org (GitLab) with the GitHub repository as the primary mirror; session 1's candidate paths 0xacab/mat2 and rhaberkorn/mat2 are both 404s, verified in this session.

## 7. Assessment

Adopt and automate it into the publication path rather than relying on anyone to remember — metadata stripping is a checklist item that fails exactly when people are rushing to publish. For your profile the essential complement is a visual review step: mat2 handles the metadata, a human must handle what is visible in the frame, and in source-protection terms the pixels are usually the bigger risk. Record which formats your installation supports so you know what is actually being cleaned.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release 0.15.0 (2026-08-04), 394 stars, 2 open issues. Near-zero backlog with current commits — excellent single-maintainer discipline over many years.

## 9. Licensing

**Licence:** LGPL-3.0-or-later _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** LGPL-3.0-or-later: linking from a proprietary tool is permitted provided the library remains replaceable; modifications to mat2 itself must be shared. Suitable for building a newsroom wrapper around.

**Licence evidence:** https://github.com/jvoisin/mat2/blob/master/LICENSE

## 10. Costs

No fee. Per-format system libraries; negligible compute. No paid dependencies.

## 11. Privacy and data flows

Fully local processing — nothing uploaded, which is the point for source-protection work. The limitation to state plainly to colleagues: it cleans metadata, not content.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ExifTool](OSINT-C2-01.md) for inspecting what metadata exists before and after cleaning
- [Dangerzone](SUR-B3-03.md), whose pixel round-trip incidentally removes most metadata along with active content
- [PyMuPDF](JAI-A2-42.md) for true redaction of visible content in PDFs

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/jvoisin/mat2
- https://0xacab.org/jvoisin/mat2
- `../sources/recovered/cat/ground_truth.tsv`
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 11. [geopandas](OSINT-C2-21.md) · 13. [OCRmyPDF](JAI-A2-33.md) →
