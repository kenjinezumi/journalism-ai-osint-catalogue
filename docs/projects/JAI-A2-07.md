# Carrot2

`JAI-A2-07` · **65/100** · overall rank 290 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 111) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 60) |
| **Subcategory** | Search-result clustering |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Carrot Search (open-source core) |
| **Maintenance** | Stable with low activity |
| **Licence** | BSD-3-Clause-style (custom Carrot2 BSD-style text read directly from carrot2.LICENSE; GitHub SPDX null) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/carrot2/carrot2) · [Documentation](https://carrot2.github.io/release/latest/doc/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 65/100**

---

## 1. Purpose

Search-results clustering engine that groups a result set into labelled thematic clusters, with Java and REST interfaces and connectors for Solr and Elasticsearch.

## Journalism / investigative use case

Attaches human-readable cluster labels to a search over a document archive, so a reporter who queries a leak for a company name sees the thematic shape of 3,000 hits — contracts, litigation, internal complaints — instead of a flat ranked list.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Designed for the exact newsroom problem of too many search hits, and produces short noun-phrase labels rather than word clouds
- Drops in behind an existing Solr or Elasticsearch index, so it is an incremental addition rather than a new system
- Licence question resolved in this survey: the open engine is a genuine BSD-style licence read from carrot2.LICENSE, not a restricted core
- Steady releases (release/4.8.6, 2026-03-08) from a commercial sponsor with a long track record

## 5. Cons

- Designed to cluster result sets of hundreds to a few thousand documents, not an entire corpus — it complements topic modelling rather than replacing it
- The higher-quality Lingo3G algorithm is a separate commercial product not in this repository, so the open version is deliberately the weaker tier
- JVM-only; awkward in a Python-centric stack except via the REST service
- Small community (859 stars, 17 open issues) means limited third-party examples and little journalism-specific documentation

## 6. Feedback (documented)

No user reports collected. The commercial-sponsor model (open core plus paid Lingo3G) is documented on the vendor site and is the key structural fact to understand; I did not verify Lingo3G pricing, which is not publicly listed in machine-readable form.

## 7. Assessment

A narrow, well-executed tool that earns its place only if you already run Solr or Elasticsearch over a corpus reporters search interactively. For your profile I would treat it as an optional UX improvement rather than a core component, and I would check whether BERTopic over the result set gives you enough without adding a JVM service. The open/commercial split is honest but means you are using the deliberately lesser algorithm.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release release/4.8.6 (2026-03-08), 859 stars, 17 open issues. GitHub's SPDX field is null and the licence was read from the repository's own carrot2.LICENSE file. Commits continue and issues are few; this is a mature component with modest change velocity rather than a declining one.

## 9. Licensing

**Licence:** BSD-3-Clause-style (custom Carrot2 BSD-style text read directly from carrot2.LICENSE; GitHub SPDX null) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Open engine is permissive. The restriction is commercial rather than legal: the best clustering algorithm (Lingo3G) is not included and requires a paid licence from Carrot Search — price not publicly listed, quote required.

**Licence evidence:** https://github.com/carrot2/carrot2/blob/master/carrot2.LICENSE

## 10. Costs

Open engine free. Lingo3G is a separate paid product with no public price list (quote required; not verified). Infrastructure: a small JVM service alongside your index. Estimate only.

## 11. Privacy and data flows

Fully local when self-hosted; clustering happens on your result sets with no outbound calls. If you use the hosted Carrot Search demo service instead, your queries and documents go to a third party — avoid for sensitive corpora.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [BERTopic](JAI-A2-04.md) for corpus-level topic discovery
- [txtai](JAI-A2-55.md) for semantic search plus clustering in one Python dependency
- Solr's own clustering component for a lighter integration

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/carrot2/carrot2
- https://github.com/carrot2/carrot2/blob/master/carrot2.LICENSE
- https://carrot2.github.io/release/latest/doc/

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

← 289. [YaCy](OSINT-C1-06.md) · 291. [Community Forensics](JAI-A4-21.md) →
