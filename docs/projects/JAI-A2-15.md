# eScriptorium

`JAI-A2-15` · **75/100** · overall rank 213 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 86) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 47) |
| **Subcategory** | Handwritten text recognition platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Scripta / PSL (École Pratique des Hautes Études) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://gitlab.com/scripta/escriptorium) · [Documentation](https://gitlab.com/scripta/escriptorium/-/wikis/home) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 75/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a — uses externally supplied Kraken models, whose terms vary per model (Zenodo-published models carry individual licences). |
| **Restrictions** | Code permissive. Verify the licence of any pretrained Kraken model you import. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Real costs: a GPU host for training and inference, a multi-service Django deployment, and — dominantly — human transcription labour to build ground truth. Estimate; assumes self-hosted GPU and a small transcription team.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://gitlab.com/scripta/escriptorium/-/blob/develop/LICENSE
- https://gitlab.com/scripta/escriptorium
- https://gitlab.com/scripta/escriptorium/-/wikis/home

---

## 1. Purpose

Web platform for transcribing manuscript and printed images at scale, wrapping Kraken for segmentation and recognition, with collaborative correction, model training and export to ALTO/PAGE XML.

## Journalism / investigative use case

Gives a non-engineer team a shared interface over a scanned handwritten archive — colonial-era registers, handwritten ledgers, court records — where reporters' corrections become training data that improves recognition across the remaining thousands of pages. The compounding-accuracy loop is what makes an otherwise impossible archive investigation tractable.

## 2. Audience

newsroom analyst, specialist investigator, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- The human-in-the-loop training loop is the real capability: accuracy on a specific hand improves as the team transcribes, rather than being fixed by a generic model
- Turns Kraken from an engineer's CLI into something a research team can use collaboratively, with task assignment and review
- Exports ALTO and PAGE XML, the standards archives and downstream search tools expect, so the output is not a dead end
- Verified active: GitLab API 2026-11-16 last activity, release v26.10 (2026-11-12) — a current project, not a stalled academic prototype

## 5. Cons

- Non-trivial sysadmin burden: Django, PostgreSQL, Redis, Celery workers and GPU scheduling — a bigger operational commitment than any other OCR tool here
- Hosted on GitLab, so it is invisible to GitHub-centric discovery and dependency tooling; no GitHub stars to gauge community size (81 GitLab stars)
- Throughput is bounded by your own GPU, and HTR training is slow — expect days, not hours, for a usable custom model
- Documentation is wiki-based and assumes digital-humanities conventions rather than newsroom workflows

## 6. Feedback (documented)

No user reports collected in this survey. Documented context: eScriptorium is the reference platform in the digital-humanities HTR community and is the standard front end for Kraken, which is a real adoption signal in that adjacent field. No journalism deployment verified — treat newsroom use as unestablished.

## 7. Assessment

The right tool for a specific and uncommon problem: a large handwritten archive that a team must transcribe together. If your material is typed or printed, Tesseract/OCRmyPDF or Surya will serve you far more cheaply. For media-in-exile work on historical state records this is one of very few viable options, and because it is fully self-hosted it keeps a politically sensitive archive on your own hardware. I would pilot it only with a committed transcription team, since the value depends on sustained human input.

## 8. Maintenance

**Actively maintained** — GitLab API 2026-11-17 (project scripta/escriptorium): last_activity_at 2026-11-16, release v26.10 released 2026-11-12, tags v26.10 and v26.10b3 dated 2026-11-05, 81 stars, not archived. Dated releases plus current activity; institutional (PSL/EPHE) backing.

## 9. Licensing

**Licence:** MIT _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a — uses externally supplied Kraken models, whose terms vary per model (Zenodo-published models carry individual licences).

**Restrictions:** Code permissive. Verify the licence of any pretrained Kraken model you import.

**Licence evidence:** https://gitlab.com/scripta/escriptorium/-/blob/develop/LICENSE

## 10. Costs

No software fee. Real costs: a GPU host for training and inference, a multi-service Django deployment, and — dominantly — human transcription labour to build ground truth. Estimate; assumes self-hosted GPU and a small transcription team.

## 11. Privacy and data flows

Fully self-hosted; images and transcriptions stay on your server with no third-party calls. Appropriate for politically sensitive archives, with the usual caveat that server security and access control are entirely your responsibility.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [Kraken](JAI-A2-26.md) alone for engineer-driven batch HTR without the collaborative layer
- Transkribus for a hosted alternative with a published price list — but it places material with a third party
- [Surya](JAI-A2-52.md) or PaddleOCR where the material is printed rather than handwritten

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://gitlab.com/scripta/escriptorium
- https://gitlab.com/scripta/escriptorium/-/wikis/home

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |

---

← 212. [sugartrail](OSINT-C3-19.md) · 214. [igraph](OSINT-C3-32.md) →
