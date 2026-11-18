# Argos Translate

`JAI-A2-03` · **79/100** · overall rank 166 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 66) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 39) |
| **Subcategory** | Machine translation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Argos Open Technologies (argosopentech) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/argosopentech/argos-translate) · [Documentation](https://www.argosopentech.com/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 79/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Per-package. Models derive from OPUS/OPUS-MT data and are mostly openly licensed, but terms vary by package and were NOT individually verified in this survey. |
| **Restrictions** | Code is unrestricted. The uncertainty is at the weights layer: verify the specific .argosmodel package licence before relying on it for commercial publication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU-only operation on commodity hardware; each language pair is a few hundred MB of disk. Model downloads come from the Argos package index — one-time egress, then zero. Infrastructure estimate assuming a laptop or small VM.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/argosopentech/argos-translate/blob/master/LICENSE
- https://github.com/argosopentech/argos-translate
- https://www.argosopentech.com/

---

## 1. Purpose

Offline neural machine translation library and CLI built on CTranslate2 and SentencePiece, with per-language-pair model packages installed as .argosmodel files.

## Journalism / investigative use case

Air-gapped batch translation of a document dump on an evidence machine: the Python API makes it straightforward to script gisting of thousands of foreign-language files so reporters can triage what needs professional human translation, with no API key and no text leaving the room.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Genuinely offline after model download — the single most important property for leak material, and the reason it underpins LibreTranslate
- Model packages are self-contained files you can stage onto an air-gapped machine, which is rare among MT stacks
- MIT code with a small dependency surface (ctranslate2, sentencepiece, stanza), so it installs reliably and is easy to audit
- Translation is fast enough on CPU for bulk triage, so no GPU budget is required

## 5. Cons

- Language coverage is narrower than NLLB or MADLAD, and many pairs route through English, compounding errors on e.g. Ukrainian→Arabic
- Plain text and HTML only — no document-format preservation, so you lose the layout that often carries meaning in forms and filings
- Quality on low-resource and dialectal material is well below commercial MT and below human usability for anything you intend to quote
- The 'latest release' object on GitHub is v1.4.0 (2021) while the current tag is v1.11.0 — release metadata is inconsistent and versioning signals are weak

## 6. Feedback (documented)

No individual user reports collected. The meaningful adoption signal is structural: LibreTranslate is built on Argos and has ~17.8k stars, which is secondary evidence that the engine works at service scale. Quality complaints on low-resource pairs are a known general property of OPUS-derived models rather than a specific documented issue I verified.

## 7. Assessment

Use it as a triage instrument, never as a translation of record. For your context the right pattern is Argos (or LibreTranslate over it) for bulk gisting inside the perimeter, with a human translator for anything that reaches publication. Check the licence of each .argosmodel you install rather than assuming the MIT code licence covers the weights.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, 6,668 stars, 171 open issues, current tag v1.11.0 (GitHub's 'latest release' object is stale at v1.4.0 from 2021-08-24). Classified active on commit recency and tag progression; the stale release object and 171 open issues temper this — issue throughput looks thinner than commit activity.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Per-package. Models derive from OPUS/OPUS-MT data and are mostly openly licensed, but terms vary by package and were NOT individually verified in this survey.

**Restrictions:** Code is unrestricted. The uncertainty is at the weights layer: verify the specific .argosmodel package licence before relying on it for commercial publication.

**Licence evidence:** https://github.com/argosopentech/argos-translate/blob/master/LICENSE

## 10. Costs

No fee. CPU-only operation on commodity hardware; each language pair is a few hundred MB of disk. Model downloads come from the Argos package index — one-time egress, then zero. Infrastructure estimate assuming a laptop or small VM.

## 11. Privacy and data flows

No network calls at inference once models are present; the only network event is the initial package-index fetch, which you can perform on a separate machine and transfer. This makes it suitable for air-gapped evidence handling — an advantage LibreTranslate's public API does not have.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [LibreTranslate](JAI-A2-27.md) for a self-hosted HTTP endpoint over the same engine
- [Helsinki-NLP OPUS-MT](JAI-A2-21.md) for direct HuggingFace control over specific pairs
- [CTranslate2](JAI-A2-08.md) directly if you want to run NLLB/MADLAD-class models for better low-resource coverage

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/argosopentech/argos-translate
- https://www.argosopentech.com/
- https://github.com/argosopentech/argos-translate/blob/master/LICENSE

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

← 165. [wayback (Python client for the Internet Archive Wayback Machine)](SUR-B1-22.md) · 167. [GeoCLIP](OSINT-C2-16.md) →
