# Helsinki-NLP OPUS-MT

`JAI-A2-21` · **76/100** · overall rank 199 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 82) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 46) |
| **Subcategory** | Machine translation |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | Helsinki-NLP (University of Helsinki Language Technology group) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (code in Opus-MT and OPUS-MT-train) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Helsinki-NLP/Opus-MT) · [Documentation](https://github.com/Helsinki-NLP/Opus-MT-train) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 76/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (code in Opus-MT and OPUS-MT-train) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | CC-BY-4.0 verified on the HuggingFace card for Helsinki-NLP/opus-mt-ru-en; coverage varies, check each pair. |
| **Restrictions** | CC-BY-4.0 requires attribution — include the model card citation in your methodology note. No non-commercial restriction on the verified pair. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. CPU inference, a few hundred MB per pair. No paid dependencies.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://huggingface.co/Helsinki-NLP/opus-mt-ru-en
- https://github.com/Helsinki-NLP/Opus-MT

---

## 1. Purpose

Family of several hundred bilingual and multilingual neural MT models trained on the OPUS parallel corpora, distributed via HuggingFace with Marian/CTranslate2-compatible weights.

## Journalism / investigative use case

The default open weights for cross-border reporting: translate Russian, Ukrainian, Arabic, Turkish, Chinese or Balkan-language documents locally, with a weights licence that permits commercial publication — the specific combination most other MT options fail.

## 2. Audience

engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- CC-BY-4.0 weights (verified on the Helsinki-NLP/opus-mt-ru-en card) permit commercial publication, which NLLB's CC-BY-NC and many research models do not
- Hundreds of directly-trained language pairs, so you can avoid English pivoting for the pairs that matter to your reporting region
- Small models — a pair is typically a few hundred MB and runs on CPU, making per-language deployment practical on field hardware
- Converts cleanly to CTranslate2, so the same weights power Argos/LibreTranslate and your own batch pipelines

## 5. Cons

- Quality varies sharply by pair and many pairs were trained on pre-2020 OPUS data, so they are weak on current slang, OCR noise and code-switching — all characteristic of leaked material
- Bilingual models mean many files to manage and a routing decision per document; language-ID errors silently produce nonsense
- The Opus-MT repository itself is low-activity (pushed 2026-02-23, no releases or tags) — the models live on HuggingFace, so repository metadata understates the project's liveness but also means no version discipline
- Licence must be checked per pair: CC-BY-4.0 is verified for ru-en but coverage was not confirmed across all cards

## 6. Feedback (documented)

No individual user reports verified. Documented signal: OPUS-MT weights are the basis of Argos Translate's model packages and of many LibreTranslate deployments, which is credible evidence of practical usability. Licence was read from one HuggingFace card (opus-mt-ru-en) and generalised with explicit uncertainty.

## 7. Assessment

The pragmatic choice when you need commercially usable, locally runnable MT for a specific language pair. Build your pipeline to record which model ID and revision translated each document, because quality differences between pairs are large enough to affect editorial confidence in a quoted passage. Where quality is insufficient and the material is not commercially published, NLLB may be better — but check that distinction deliberately rather than letting a model choice create a licence problem.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: Helsinki-NLP/Opus-MT archived=false, pushed_at 2026-02-23, no releases, no tags, 876 stars, 57 open issues. The models are maintained on HuggingFace rather than through repository releases, so repo quiescence understates activity; however, there is no visible release cadence to evidence active maintenance. Classified stable-low: the model family is functionally complete and widely consumed.

## 9. Licensing

**Licence:** MIT (code in Opus-MT and OPUS-MT-train) _(SPDX verified)_

**Model / data licence:** CC-BY-4.0 verified on the HuggingFace card for Helsinki-NLP/opus-mt-ru-en; coverage varies, check each pair.

**Restrictions:** CC-BY-4.0 requires attribution — include the model card citation in your methodology note. No non-commercial restriction on the verified pair.

**Licence evidence:** https://huggingface.co/Helsinki-NLP/opus-mt-ru-en

## 10. Costs

No fee. CPU inference, a few hundred MB per pair. No paid dependencies.

## 11. Privacy and data flows

Local inference after download; nothing leaves the machine. Weights can be staged offline.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Argos Translate](JAI-A2-03.md) for a packaged offline library over the same lineage
- NLLB-200 or MADLAD-400 via CTranslate2 for better low-resource coverage — but verify the licence, NLLB is CC-BY-NC
- Commercial MT APIs only for non-sensitive public material

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/Helsinki-NLP/Opus-MT
- https://huggingface.co/Helsinki-NLP/opus-mt-ru-en

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

← 198. [OONI Data (oonidata / oonipipeline)](SUR-B1-05.md) · 200. [SpyGuard](SUR-B3-12.md) →
