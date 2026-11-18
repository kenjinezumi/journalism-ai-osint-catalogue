# LibreTranslate

`JAI-A2-27` · **85/100** · overall rank 85 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 31) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 21) |
| **Subcategory** | Machine translation service |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | LibreTranslate community (Piero Toffanin and contributors) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/LibreTranslate/LibreTranslate) · [Documentation](https://libretranslate.com/docs/) |

**Scores** — relevance 5/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Inherits Argos Translate model packages (largely open, derived from OPUS/OPUS-MT data); verify per language pair. |
| **Restrictions** | AGPL-3.0: if you modify LibreTranslate and provide it over a network, you must offer your modified source to users. Running it unmodified for internal use carries no obligation. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee for self-hosting. Infrastructure estimate: one CPU VM with 4-8GB RAM serves a small newsroom; each language pair adds a few hundred MB of models. The hosted libretranslate.com service has paid API tiers whose current prices were NOT verified in this survey. Assumptions: self-hosted Docker, CPU-only.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/LibreTranslate/LibreTranslate/blob/main/LICENSE
- https://github.com/LibreTranslate/LibreTranslate
- https://libretranslate.com/docs/

---

## 1. Purpose

Self-hostable translation API and web UI built on Argos Translate, with a REST interface, language auto-detection, API-key management and rate limiting.

## Journalism / investigative use case

A newsroom-run translation endpoint so no document text leaves the organisation: point OpenAleph, Datashare or your own ingest pipeline at it for bulk gisting of foreign-language material, and give reporters a browser UI that looks like the cloud services they would otherwise paste leaked text into.

## 2. Audience

engineer, journalist

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Replaces the behaviour you most need to stop — pasting sensitive text into a public translation site — with something that looks the same but stays inside the perimeter
- REST API with rate limiting and keys makes it a shared newsroom service rather than a personal tool
- Dockerised and genuinely easy to deploy; one of the lower-effort self-hosting jobs in this catalogue
- Large community (17,778 stars) and current releases (v1.9.6, 2026-05-26)

## 5. Cons

- Translation quality is well below commercial MT on low-resource pairs because it inherits Argos/OPUS models — adequate for triage, not for publication
- AGPL-3.0 network copyleft applies if you expose a modified instance to users, which is exactly the deployment shape most newsrooms want — unmodified deployment is fine, but customising the UI creates an obligation
- No translation memory, glossary or human-review workflow, so terminology consistency across an investigation is unmanaged
- The public libretranslate.com API is the same software but a third party — the convenience path is the insecure one, and staff will find it

## 6. Feedback (documented)

No individual user reports verified. Documented signals: 17,778 stars and 136 open issues indicate wide adoption with active triage; the project documents both self-hosted and hosted (paid) options, so the hosted-versus-self-hosted distinction is explicit rather than hidden.

## 7. Assessment

I would deploy this for any newsroom handling foreign-language material — the privacy argument is decisive and the deployment cost is low. Two concrete controls: block libretranslate.com at the network level so staff use your instance, and keep your deployment unmodified (configuration, not code changes) to avoid the AGPL publication obligation. Accept that output is triage-grade and route anything quotable to a human translator.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v1.9.6 (2026-05-26), 17,778 stars, 136 open issues. Current commits, periodic releases, large community. Classified active on the combination rather than push recency alone.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** Inherits Argos Translate model packages (largely open, derived from OPUS/OPUS-MT data); verify per language pair.

**Restrictions:** AGPL-3.0: if you modify LibreTranslate and provide it over a network, you must offer your modified source to users. Running it unmodified for internal use carries no obligation.

**Licence evidence:** https://github.com/LibreTranslate/LibreTranslate/blob/main/LICENSE

## 10. Costs

No software fee for self-hosting. Infrastructure estimate: one CPU VM with 4-8GB RAM serves a small newsroom; each language pair adds a few hundred MB of models. The hosted libretranslate.com service has paid API tiers whose current prices were NOT verified in this survey. Assumptions: self-hosted Docker, CPU-only.

## 11. Privacy and data flows

Fully local when self-hosted — the core reason to run it. The counterpart risk is explicit: the public API sends text to a third party and must be avoided for leak material. Model downloads occur on first run.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Argos Translate](JAI-A2-03.md) directly for scripted batch work without a service
- [Helsinki-NLP OPUS-MT](JAI-A2-21.md) via CTranslate2 for better per-pair control
- A commercial MT API only for already-public material

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/LibreTranslate/LibreTranslate
- https://libretranslate.com/docs/
- https://github.com/LibreTranslate/LibreTranslate/blob/main/LICENSE

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

← 84. [OONI Probe Multiplatform](SUR-B1-02.md) · 86. [Heritrix 3](OSINT-C1-22.md) →
