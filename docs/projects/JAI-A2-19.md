# GLiNER

`JAI-A2-19` · **81/100** · overall rank 139 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 57) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 32) |
| **Subcategory** | Zero-shot entity extraction |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | Urchade Zaratiana and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (code) |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/urchade/GLiNER) · [Documentation](https://github.com/urchade/GLiNER#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 81/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | Apache-2.0 (code) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | SPLIT AND MATERIAL: v2.1 checkpoints (urchade/gliner_small-v2.1, urchade/gliner_multi-v2.1) are Apache-2.0; older v0/v1 checkpoints (urchade/gliner_base, gliner_multi, gliner_small/medium/large-v1) are CC-BY-NC-4.0, research only. |
| **Restrictions** | Using a v0/v1 checkpoint in commercially published journalism breaches CC-BY-NC-4.0. The code licence does not cure this. Verify the checkpoint, not the repository. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee for the Apache-2.0 path. CPU inference is viable; a small GPU speeds bulk sweeps. No paid dependencies. Estimate only.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/urchade/GLiNER/blob/main/LICENSE
- https://github.com/urchade/GLiNER
- https://huggingface.co/urchade/gliner_multi-v2.1

---

## 1. Purpose

Compact bidirectional-transformer NER model that extracts arbitrary user-specified entity types at inference time without retraining, running on CPU or a small GPU.

## Journalism / investigative use case

Define bespoke labels for one investigation — 'shell company', 'vessel', 'bank account', 'politically exposed person' — and sweep a leak for them without annotating training data and without sending documents to an API. That flexibility is what spaCy's fixed label set cannot give you.

## 2. Audience

engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- Zero-shot custom labels change the economics of entity extraction for investigations, where the interesting entity type is always project-specific
- Small enough to run on CPU, so it is deployable on an isolated evidence machine rather than requiring GPU infrastructure
- Apache-2.0 code with Apache-2.0 v2.1 checkpoints available — a genuinely open path exists
- Active development (v0.2.30, 2026-11-02) with a multilingual checkpoint line

## 5. Cons

- Licence trap, verified and material: the older but still widely cited v0/v1 checkpoints (gliner_base, gliner_multi, gliner_small/medium/large-v1) are CC-BY-NC-4.0 and unusable by a commercial newsroom; only the v2.1 line (gliner_small-v2.1, gliner_multi-v2.1) is Apache-2.0
- Recall is prompt-sensitive: label wording materially changes what you find, which makes systematic coverage hard to evidence in a methodology note
- Long documents must be chunked, and entities spanning chunk boundaries are missed
- Extracts but does not link or deduplicate — 'Rosneft Trading' and 'OOO Rosneft-Trading' remain separate strings until you add rigour/nomenklatura

## 6. Feedback (documented)

No individual user reports verified. The documented, checkable finding is the split model licensing recorded in session 1 and retained here: HuggingFace cards for the v0/v1 checkpoints state cc-by-nc-4.0 while the v2.1 cards state apache-2.0. 4,270 stars, 54 open issues.

## 7. Assessment

High-value and I would use it, but with a hard rule: pin a v2.1 Apache-2.0 checkpoint and record the exact model ID in the pipeline, because the NC checkpoints are the ones most tutorials link to. Treat its output as a candidate list for human review rather than a finding — prompt sensitivity means absence of a hit is not evidence of absence. Pair with rigour for normalisation before any matching.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-11, latest release v0.2.30 (2026-11-02), 4,270 stars, 54 open issues. Frequent releases on a 0.2.x line with current commits; research-origin project that has sustained a release cadence.

## 9. Licensing

**Licence:** Apache-2.0 (code) _(SPDX verified)_

**Model / data licence:** SPLIT AND MATERIAL: v2.1 checkpoints (urchade/gliner_small-v2.1, urchade/gliner_multi-v2.1) are Apache-2.0; older v0/v1 checkpoints (urchade/gliner_base, gliner_multi, gliner_small/medium/large-v1) are CC-BY-NC-4.0, research only.

**Restrictions:** Using a v0/v1 checkpoint in commercially published journalism breaches CC-BY-NC-4.0. The code licence does not cure this. Verify the checkpoint, not the repository.

**Licence evidence:** https://github.com/urchade/GLiNER/blob/main/LICENSE

## 10. Costs

No fee for the Apache-2.0 path. CPU inference is viable; a small GPU speeds bulk sweeps. No paid dependencies. Estimate only.

## 11. Privacy and data flows

Local inference after checkpoint download; no text leaves the machine. Weights can be pre-staged for air-gapped use.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- CC-BY-NC-4.0 on the v0/v1 checkpoints — a commercial-use blocker if the wrong model ID is pinned

## 13. Alternatives

- [spaCy](JAI-A2-47.md) with EntityRuler gazetteers when target names are known in advance
- [Stanza](JAI-A2-49.md) for non-English NER with conventional label sets
- [Presidio](JAI-A2-40.md) when the goal is finding and redacting personal data rather than investigative entities

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/urchade/GLiNER
- https://huggingface.co/urchade/gliner_multi-v2.1
- https://github.com/urchade/GLiNER/blob/main/LICENSE

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

← 138. [EDGI web-monitoring-diff](SUR-B1-21.md) · 140. [ICIJ extract](JAI-A2-24.md) →
